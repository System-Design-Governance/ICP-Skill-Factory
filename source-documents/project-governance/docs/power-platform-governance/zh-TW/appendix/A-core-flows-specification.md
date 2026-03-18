# Power Automate 核心 Flows 設計規格

> **警告：本文件為設計規格，不得作為實作依據。**
>
> 實作請一律以主文件「05-core-flows-implementation-runbook.md」為準。
> 本文件僅供理解設計意圖、稽核審查與未來改版參考使用。

---

## 文件控制資訊

| 項目 | 內容 |
|:-----|:----|
| 文件編號 | IMPL-05-GOV-FLOWS-001 |
| 版本 | 1.1 |
| 分類 | **設計規格（僅供參考，禁止作為實作依據）** |
| 實作依據 | **05-core-flows-implementation-runbook.md** |
| 適用對象 | 設計審查人員、稽核人員、架構師 |

---

## 治理架構原則重申

### Flow 層責任邊界

Power Automate 作為**治理邏輯層**，其職責嚴格界定如下：

**Flow 允許執行之操作**：
| 操作類型 | 說明 |
|:--------|:----|
| 驗證前置條件（Pre-check） | 檢查 Gate 前置條件、文件完整性、狀態機合法轉移 |
| 路由審核請求 | 依 Gate 類型發送 Approval 至對應審核群組 |
| 等待人類決策 | 使用 `Start and wait for an approval` 等待人類回覆 |
| 記錄人類決策 | 將 Approval 回覆寫入 Review Decision Log |
| 更新狀態機欄位 | 依人類決策更新 CurrentGate、RequestStatus 等 |
| 計算客觀數值 | 計算 HighestResidualRiskLevel 等可客觀判定之數值 |
| 觸發後續流程 | Gate 3 通過後自動呼叫文件凍結等後續 Flow |

**Flow 禁止執行之操作**：
| 禁止操作 | 設計原因 |
|:--------|:--------|
| Flow 不得做出 Approve 決策 | 違反「人類決策」原則 |
| Flow 不得接受風險 | 風險接受必須由 Risk Owner 執行 |
| Flow 不得覆寫人類決策 | Review Decision Log 為 Append-only |
| Flow 不得跳過人工審查 | 違反「職責分離」原則 |
| Flow 不得自動判定 Gate 通過 | CurrentGate 轉移必須依據人類核准 |

### Flow Service Principal 獨占寫入權

所有治理關鍵欄位（Flow-only 欄位）僅允許 Flow Service Principal 寫入：

| Entity | Flow-only 欄位 |
|:-------|:-------------|
| Project Registry | CurrentGate, RequestStatus, ProjectStatus, DocumentFreezeStatus, Gate0/1/2/3PassedDate, RiskAcceptanceStatus, HighestResidualRiskLevel, CreatedBy, CreatedOn, ModifiedBy, ModifiedOn |
| Review Decision Log | ReviewID, ReviewType, Decision, ApprovedBy, ReviewedDate, TriggerFlowRunId |
| Risk Assessment Table | RiskLevel, RiskAcceptanceStatus, RiskAcceptedBy, RiskAcceptanceDate |

**技術強制執行**：
- Dataverse Field-Level Security Profile 設定
- GOV-017 Guardrail Monitor 每小時偵測並自動回滾違規修改

---

## Flow 建立順序與依賴關係

### 建議建立順序

基於 Flow 間的呼叫依賴關係，建議依以下順序建立：

```
Phase 1：基礎設施 Flows（無依賴）
├── GOV-015：Notification Handler（通知處理器）
└── GOV-013：Risk Level Calculator（風險等級計算器）

Phase 2：核心治理 Flows
├── GOV-014：Document Freeze（文件凍結）
├── GOV-016：Rework Loop Handler（打回重送處理器）
├── GOV-004：Risk Acceptance（風險接受）
├── GOV-003：Gate Approval Orchestrator（Gate 審批編排器）
├── GOV-005：Document Intake and Register（文件上傳登記）
├── GOV-002：Gate Transition Request（Gate 推進申請）
└── GOV-001：Create Project（建立專案）

Phase 3：例外與生命週期 Flows
├── GOV-006：Gate Request Cancellation
├── GOV-007：Lite to Full Upgrade
├── GOV-008：Document Unfreeze Exception
├── GOV-009：Project Closure
├── GOV-010：Project Suspension/Resume
├── GOV-011：Gate Rollback Exception
└── GOV-012：Project Archival

Phase 4：監控與稽核 Flows
├── GOV-017：Guardrail Monitor
├── GOV-018：Compliance Reconciler
└── GOV-019：SLA Monitor
```

### Flow 依賴關係圖

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        父 Flow → 子 Flow 呼叫關係                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  FORM-001 ──→ GOV-001 Create Project                                    │
│                    └── 呼叫 GOV-015 Notification Handler                │
│                                                                         │
│  FORM-002 ──→ GOV-002 Gate Transition Request                           │
│                    ├── 呼叫 GOV-003 Gate Approval Orchestrator          │
│                    │        ├── 呼叫 GOV-015 Notification Handler       │
│                    │        ├── 呼叫 GOV-016 Rework Loop Handler        │
│                    │        └── 呼叫 GOV-014 Document Freeze（Gate 3）  │
│                    ├── 呼叫 GOV-013 Risk Level Calculator（Gate 3）     │
│                    └── 呼叫 GOV-004 Risk Acceptance（Gate 3）           │
│                             └── 呼叫 GOV-015 Notification Handler       │
│                                                                         │
│  FORM-005 ──→ GOV-005 Document Intake and Register                      │
│                    └── 呼叫 GOV-015 Notification Handler                │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Parent Flow vs Child Flow 分類

| 類型 | Flow ID | Trigger 方式 | 說明 |
|:----|:--------|:-----------|:----|
| **Parent Flow** | GOV-001 | HTTP Request | 由 FORM-001 觸發 |
| **Parent Flow** | GOV-002 | HTTP Request | 由 FORM-002 觸發 |
| **Parent Flow** | GOV-005 | HTTP Request | 由 FORM-005 觸發 |
| **Parent Flow** | GOV-006~012 | HTTP Request | 由對應 FORM 觸發 |
| **Child Flow** | GOV-003 | Child Flow Trigger | 由 GOV-002 呼叫 |
| **Child Flow** | GOV-004 | Child Flow Trigger | 由 GOV-002 呼叫（Gate 3） |
| **Child Flow** | GOV-013 | Child Flow Trigger | 由 GOV-002 呼叫（Gate 3） |
| **Child Flow** | GOV-014 | Child Flow Trigger | 由 GOV-003 呼叫（Gate 3 通過後） |
| **Child Flow** | GOV-015 | Child Flow Trigger | 由所有 Flow 呼叫 |
| **Child Flow** | GOV-016 | Child Flow Trigger | 由 GOV-003 呼叫（審批拒絕時） |
| **Scheduled Flow** | GOV-017 | Recurrence（每小時） | 自動執行 |
| **Scheduled Flow** | GOV-018 | Recurrence（每日） | 自動執行 |
| **Scheduled Flow** | GOV-019 | Recurrence（每日） | 自動執行 |

---

## 核心 Flows 詳細規格（GOV-001 至 GOV-005）

### GOV-001：Create Project（建立專案）

#### Trigger 定義

| 項目 | 設定值 |
|:----|:-------|
| Trigger 類型 | HTTP Request |
| HTTP Method | POST |
| 來源 | FORM-001 Intake Form（Power Apps） |
| 連線方式 | Solution 內 Environment Variable 引用 |

#### Input Schema（輸入契約）

```json
{
    "type": "object",
    "properties": {
        "Title": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255,
            "description": "專案名稱"
        },
        "SystemArchitect": {
            "type": "string",
            "format": "email",
            "description": "系統架構師 Email"
        },
        "ProjectManager": {
            "type": "string",
            "format": "email",
            "description": "專案經理 Email"
        },
        "ProjectType": {
            "type": "string",
            "enum": ["NewSystem", "MajorArchChange", "SecurityCritical", "ComplianceChange"],
            "description": "專案類型"
        },
        "TargetSL": {
            "type": "string",
            "enum": ["SL1", "SL2", "SL3", "SL4"],
            "description": "目標安全等級"
        },
        "ProjectDescription": {
            "type": "string",
            "maxLength": 2000,
            "description": "專案說明（可選）"
        },
        "SubmittedBy": {
            "type": "string",
            "format": "email",
            "description": "表單提交者 Email（由 Power Apps 自動帶入 claims('upn')）"
        }
    },
    "required": ["Title", "SystemArchitect", "ProjectManager", "ProjectType", "TargetSL", "SubmittedBy"]
}
```

#### Pre-conditions（前置條件驗證）

| Pre-check | 條件 | 驗證方式 | 錯誤代碼 |
|:----------|:----|:--------|:--------|
| PC-001-01 | SubmittedBy 必須在 GOV-Architects 群組中 | Office 365 Groups - Get group members | ERR-001-002 |
| PC-001-02 | 所有必填欄位已填寫且符合格式 | HTTP Request Schema 自動驗證 | ERR-001-001 |

**不滿足時回應**：
- ERR-001-002：HTTP 403 Forbidden，「僅授權架構師可建立專案。請聯絡 Governance Function 申請權限。」
- ERR-001-001：HTTP 400 Bad Request，「必填欄位未填寫或格式錯誤：{欄位名稱}」

#### Main Steps（主要執行步驟）

```
Step 1：產生 RequestID
├── 格式：DR-{Year}-{ShortGuid}
├── 範例：DR-2026-3f4a8b2c
└── 使用 GUID 前 8 碼確保唯一性

Step 2：檢查 RequestID 唯一性（Idempotency）
├── 查詢 Project Registry 是否已存在相同 RequestID
├── 若存在：重新產生（最多重試 3 次）
└── 若 3 次仍衝突：Terminate with ERR-001-010

Step 3：建立 Project Registry 記錄
├── CurrentGate = "Pending"
├── RequestStatus = "None"
├── ProjectStatus = "Active"
├── DocumentFreezeStatus = "Not Frozen"
├── RiskAssessmentType = "Full"
├── CreatedBy = "Flow Service Principal"
└── CreatedOn = utcNow()

Step 4：建立 SharePoint 文件資料夾結構（對齊 Doc 03）
├── /{RequestID}（專案主資料夾）
├── /{RequestID}/01_Feasibility
├── /{RequestID}/02_Risk_Assessment
├── /{RequestID}/03_Design
├── /{RequestID}/04_Security
├── /{RequestID}/05_Test
└── /{RequestID}/06_Handover

Step 5：Baseline Seeding — 建立 Document Register 基線記錄
├── 遍歷 Doc 02 Baseline Matrix 中 RequiredForGate ≠ '-' 的 DocumentType（13 筆）
├── 為每個 DocumentType 建立一筆 Document Register 記錄
├── DocumentRole = Planned（100000000）
├── DeliverablePackage = CoreDeliverable（100000000）
├── SharePointFileLink = 空白（尚未上傳）
└── DocumentID = DOC-{RequestID}-{DocumentType}-PLANNED

Step 6：寫入 Review Decision Log
├── ReviewType = "ProjectCreation"
├── Decision = "Executed"
├── TriggerFlowRunId = workflow().run.name
└── ParentProject = {RequestID}

Step 7：回傳成功訊息給 Power Apps
└── HTTP 200 OK，包含 RequestID、Message、Data、BaselineSeededCount
```

#### Output Schema（輸出契約）

**成功回應（HTTP 200）**：
```json
{
    "Status": "Success",
    "RequestID": "DR-2026-3f4a8b2c",
    "Message": "專案已建立成功",
    "Data": {
        "Title": "IEC 62443 Firewall Upgrade",
        "SystemArchitect": "alice@company.com",
        "ProjectManager": "bob@company.com",
        "CurrentGate": "Pending",
        "ProjectStatus": "Active"
    }
}
```

**失敗回應（HTTP 4xx/5xx）**：
```json
{
    "Status": "Failed",
    "ErrorCode": "ERR-001-002",
    "Message": "僅授權架構師可建立專案",
    "Details": {
        "SubmittedBy": "unauthorized@company.com"
    }
}
```

#### Compensating Transaction（補償交易）

| 失敗情境 | 補償動作 |
|:--------|:--------|
| SharePoint 資料夾建立失敗 | 刪除已建立的 Project Registry 記錄 |
| Review Decision Log 寫入失敗 | 刪除 Project Registry 記錄與 SharePoint 資料夾 |

---

### GOV-002：Gate Transition Request（Gate 推進申請）

#### Trigger 定義

| 項目 | 設定值 |
|:----|:-------|
| Trigger 類型 | HTTP Request |
| HTTP Method | POST |
| 來源 | FORM-002 Gate Request Form（Power Apps） |
| 並行控制 | On（Concurrency Key = ProjectId，Parallelism = 1） |

#### Input Schema（輸入契約）

```json
{
    "type": "object",
    "properties": {
        "ProjectId": {
            "type": "integer",
            "description": "Project Registry 的 ID"
        },
        "RequestedGate": {
            "type": "string",
            "enum": ["Gate0", "Gate1", "Gate2", "Gate3"],
            "description": "申請的 Gate"
        },
        "SubmittedBy": {
            "type": "string",
            "format": "email",
            "description": "表單提交者 Email"
        },
        "Comments": {
            "type": "string",
            "maxLength": 2000,
            "description": "附加說明（可選）"
        }
    },
    "required": ["ProjectId", "RequestedGate", "SubmittedBy"]
}
```

#### Pre-conditions（前置條件驗證）

| Pre-check | 條件 | 錯誤代碼 |
|:----------|:----|:--------|
| PC-002-01 | ProjectId 存在於 Project Registry | ERR-002-001 |
| PC-002-02 | SubmittedBy = Project.SystemArchitect | ERR-002-003 |
| PC-002-03 | ProjectStatus = Active | ERR-002-005 |
| PC-002-04 | RequestStatus = None（無進行中申請） | ERR-002-058 |
| PC-002-05 | CurrentGate 符合 RequestedGate 前置條件 | ERR-002-0XX |
| PC-002-06 | 必要文件已上傳（依 Gate 而異） | ERR-002-0XX |

**Gate 狀態轉移前置條件**：

| RequestedGate | 必須 CurrentGate | 錯誤代碼 |
|:-------------|:----------------|:--------|
| Gate0 | Pending | ERR-002-020 |
| Gate1 | Gate0 | ERR-002-040 |
| Gate2 | Gate1 或 Gate2 | ERR-002-050 |
| Gate3 | Gate2 | ERR-002-053 |

**必要文件檢查**：

| Gate | 必要文件欄位 |
|:----|:-----------|
| Gate0 | TechnicalFeasibilityLink, InitialRiskListLink, RiskAssessmentStrategyLink, TargetSL |
| Gate1 | DesignBaselineLink, RiskAssessmentLink, IEC62443ChecklistLink, RequirementTraceabilityLink, DocumentRegisterLink, DesignObjectInventoryLink, RiskAssessmentType |
| Gate2 | ChangeImpactLink, ChangeDescription |
| Gate3 | ResidualRiskLink, HandoverMeetingLink, Risk Register 至少有一筆風險項目 |

#### Main Steps（主要執行步驟）

```
Step 1：取得專案資訊
└── Dataverse - Get a row by ID (Project Registry)

Step 2：執行所有 Pre-checks
└── 任一失敗則 Terminate 並回傳錯誤

Step 3：寫入 Review Decision Log
├── ReviewType = "Gate{X}Request"
├── Decision = "Pending"
├── TriggerFlowRunId = workflow().run.name
└── ParentProject = {RequestID}

Step 4：更新 Project Registry
├── RequestStatus = "Pending"
├── RequestedGate = {RequestedGate}
└── ModifiedBy = "Flow Service Principal"

Step 5：條件分支 - 依 RequestedGate 區分
├── Gate 0/1/2：直接呼叫 GOV-003 Gate Approval Orchestrator
└── Gate 3：
    ├── 5-1：呼叫 GOV-013 Risk Level Calculator
    ├── 5-2：更新 Project Registry.HighestResidualRiskLevel
    ├── 5-3：呼叫 GOV-004 Risk Acceptance
    └── 5-4：等待 GOV-004 完成後，呼叫 GOV-003

Step 6：回傳成功訊息給 Power Apps
```

#### Gate 3 特殊處理流程

```
┌───────────────────────────────────────────────────────────────┐
│                    Gate 3 申請執行流程                          │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  GOV-002 Gate Transition Request (Gate 3)                     │
│      │                                                        │
│      ├──→ GOV-013 Risk Level Calculator                       │
│      │        └── 計算 HighestResidualRiskLevel               │
│      │            (High / Medium / Low)                       │
│      │                                                        │
│      ├──→ 更新 Project Registry                               │
│      │        └── HighestResidualRiskLevel = {計算結果}        │
│      │                                                        │
│      ├──→ GOV-004 Risk Acceptance                             │
│      │        └── 依風險等級發送給對應 Risk Owner              │
│      │            ├── High：CTO                               │
│      │            ├── Medium：事業單位主管                     │
│      │            └── Low：部門主管                            │
│      │                                                        │
│      └──→ GOV-003 Gate Approval Orchestrator (Gate 3)         │
│               └── 雙層審批（QA → Governance）                  │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

---

### GOV-003：Gate Approval Orchestrator（Gate 審批編排器）

#### Trigger 定義

| 項目 | 設定值 |
|:----|:-------|
| Trigger 類型 | Child Flow（When Power Automate V2） |
| 來源 | GOV-002 Gate Transition Request |
| 並行控制 | 由父 Flow 控制（Concurrency Key = ProjectId） |

#### Input Schema（輸入契約）

```json
{
    "type": "object",
    "properties": {
        "ProjectId": {
            "type": "integer",
            "description": "Project Registry 的 ID"
        },
        "RequestedGate": {
            "type": "string",
            "enum": ["Gate0", "Gate1", "Gate2", "Gate3"],
            "description": "申請的 Gate"
        }
    },
    "required": ["ProjectId", "RequestedGate"]
}
```

#### Pre-conditions（前置條件驗證）

| Pre-check | 條件 | 錯誤代碼 |
|:----------|:----|:--------|
| PC-003-01 | RequestStatus = Pending（由 GOV-002 設定） | ERR-003-001 |
| PC-003-02 | Gate 3 限定：RiskAcceptanceStatus = Accepted | ERR-003-010 |

#### 審批流程矩陣

| Gate | 審批層級數 | 審批順序 | 審批群組 |
|:----|:----------|:--------|:--------|
| Gate 0 | 1 層 | Engineering Management | GOV-EngineeringManagement |
| Gate 1 | 3 層 | Security → QA → Governance | GOV-SecurityReviewers → GOV-QAReviewers → GOV-GovernanceLead |
| Gate 2 | 1 層 | Engineering Management | GOV-EngineeringManagement |
| Gate 3 | 2 層 | QA → Governance | GOV-QAReviewers → GOV-GovernanceLead |

#### Gate 1 三層審批流程詳細步驟

```
┌───────────────────────────────────────────────────────────────────────┐
│                     Gate 1 三層序列審批流程                              │
├───────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  Step 1：更新 RequestStatus = UnderReview                              │
│      │                                                                │
│      ▼                                                                │
│  Step 2：發送 Approval 給 Security Team (Layer 1 of 3)                 │
│      │                                                                │
│      ├── Approve → 更新 Gate1SecurityReviewStatus = Approved          │
│      │             繼續 Step 3                                         │
│      │                                                                │
│      └── Reject → 更新 Decision = Rejected                            │
│                   RequestStatus = None                                │
│                   呼叫 GOV-016 Rework Loop Handler                    │
│                   呼叫 GOV-015 Notification Handler                   │
│                   Terminate（不繼續後續審批）                          │
│                                                                       │
│  Step 3：發送 Approval 給 QA Team (Layer 2 of 3)                       │
│      │                                                                │
│      ├── Approve → 更新 Gate1QAReviewStatus = Approved                │
│      │             繼續 Step 4                                         │
│      │                                                                │
│      └── Reject → （同上，Terminate）                                  │
│                                                                       │
│  Step 4：發送 Approval 給 Governance Function (Layer 3 of 3)           │
│      │                                                                │
│      ├── Approve → 更新 Decision = Approved                           │
│      │             CurrentGate = Gate1                                │
│      │             Gate1PassedDate = utcNow()                         │
│      │             RequestStatus = None                               │
│      │             呼叫 GOV-015 Notification Handler                  │
│      │                                                                │
│      └── Reject → （同上，Terminate）                                  │
│                                                                       │
└───────────────────────────────────────────────────────────────────────┘
```

#### Gate 3 審批後自動觸發文件凍結

```
Gate 3 Governance Approve:
    │
    ├── 更新 CurrentGate = Gate3
    ├── 更新 Gate3PassedDate = utcNow()
    │
    └── 呼叫 GOV-014 Document Freeze
            │
            ├── 更新 Document Register（IsFrozen = Yes）
            ├── SharePoint Check Out to System Account
            └── 更新 Project Registry（DocumentFreezeStatus = Frozen）
```

#### Approval 內容範本

**Gate 1 Security Review Approval 範本**：
```
Title：Gate 1 Security Review - {RequestID}

Details：
專案名稱：{Title}
審批層級：Security Review（Layer 1 of 3）

必要文件：
✓ 設計基線文件
✓ 風險評估報告
✓ IEC 62443 檢查表
✓ 威脅模型分析

請審核：
- 安全設計是否符合 IEC 62443-3-3 要求
- 威脅模型是否涵蓋所有攻擊路徑
- 風險評估是否完整

[查看專案詳情] → Power App URL
```

---

### GOV-004：Risk Acceptance（風險接受）

#### Trigger 定義

| 項目 | 設定值 |
|:----|:-------|
| Trigger 類型 | Child Flow（When Power Automate V2） |
| 來源 | GOV-002 Gate Transition Request（Gate 3 限定） |

#### Input Schema（輸入契約）

```json
{
    "type": "object",
    "properties": {
        "ProjectId": {
            "type": "integer",
            "description": "Project Registry 的 ID"
        }
    },
    "required": ["ProjectId"]
}
```

#### 風險等級對應 Risk Owner 矩陣

| HighestResidualRiskLevel | Risk Owner 角色 | 審批群組 |
|:------------------------|:---------------|:--------|
| High | CTO（技術長） | GOV-RiskOwnerHigh |
| Medium | 事業單位主管 | GOV-RiskOwnerMedium |
| Low | 部門主管 | GOV-RiskOwnerLow |

#### Main Steps（主要執行步驟）

```
Step 1：取得專案資訊與風險等級
├── 讀取 Project Registry
└── 取得 HighestResidualRiskLevel

Step 2：取得所有風險項目清單
└── 查詢 Risk Assessment Table（ParentProject = RequestID）

Step 3：依風險等級發送 Risk Acceptance Approval
├── 決定 Approver 群組（依 HighestResidualRiskLevel）
└── 發送 Approval

Step 4：處理 Approval 回應
├── Approve：
│   ├── 更新 Review Decision Log（Decision = Approved）
│   ├── 更新 Risk Assessment Table（RiskAcceptanceStatus = Accepted）
│   ├── 更新 Project Registry（RiskAcceptanceStatus = Accepted）
│   └── 回傳成功給父 Flow
│
└── Reject：
    ├── 更新 Review Decision Log（Decision = Rejected）
    ├── 更新 Project Registry（RiskAcceptanceStatus = Rejected）
    └── 回傳失敗給父 Flow
```

#### Risk Acceptance Approval 內容範本

```
Title：風險接受審批 - {RequestID}

Details：
專案名稱：{Title}
最高殘餘風險等級：{HighestResidualRiskLevel}

風險項目清單：
┌──────────────────┬──────────┬────────────────────────┐
│ 風險 ID          │ 風險等級  │ 風險描述               │
├──────────────────┼──────────┼────────────────────────┤
│ RSK-001          │ High     │ 未經加密的資料傳輸      │
│ RSK-002          │ Medium   │ 認證機制強度不足        │
│ RSK-003          │ Low      │ 日誌記錄不完整          │
└──────────────────┴──────────┴────────────────────────┘

請確認：
- 您了解上述殘餘風險並接受其存在
- 風險緩解措施已充分評估
- 組織可承擔這些風險

[查看風險評估詳情] → Power App URL
```

---

### GOV-005：Document Upload and Register（文件上傳登記）

#### Trigger 定義

| 項目 | 設定值 |
|:----|:-------|
| Trigger 類型 | HTTP Request |
| HTTP Method | POST |
| 來源 | FORM-003 Document Upload Form（Power Apps） |

#### Input Schema（輸入契約）

```json
{
    "type": "object",
    "properties": {
        "ProjectId": { "type": "string", "description": "gov_projectregistryid (GUID)" },
        "FileName": { "type": "string", "maxLength": 255 },
        "FileContent": { "type": "string", "description": "Base64 encoded file content" },
        "DocumentType": {
            "type": "string",
            "enum": ["TechnicalFeasibility", "InitialRiskList", "RiskAssessmentStrategy",
                     "DesignBaseline", "RiskAssessment", "IEC62443Checklist", "ThreatModel",
                     "RequirementTraceability", "TestPlan", "TestReport", "HandoverMeeting",
                     "ResidualRiskList", "Other", "DesignObjectInventory", "ChangeImpact",
                     "DocumentRegister"]
        },
        "DocumentName": { "type": "string", "maxLength": 255 },
        "DocumentVersion": { "type": "string", "maxLength": 20, "pattern": "^v\\d+\\.\\d+$" },
        "DeliverablePackage": {
            "type": "string",
            "enum": ["CoreDeliverable", "SupplementaryDeliverable", "AdHoc"],
            "default": "CoreDeliverable"
        },
        "Comments": { "type": "string", "maxLength": 1000 },
        "SubmittedBy": { "type": "string", "format": "email" }
    },
    "required": ["ProjectId", "FileName", "FileContent", "DocumentType", "DocumentName", "DocumentVersion", "SubmittedBy"]
}
```

#### Pre-conditions（前置條件驗證）

| Pre-check | 條件 | 錯誤代碼 |
|:----------|:----|:--------|
| PC-005-01 | ProjectId 存在於 Project Registry | ERR-005-001 |
| PC-005-02 | ProjectStatus = Active | ERR-005-002 |
| PC-005-03 | DocumentFreezeStatus ≠ Frozen（文件未凍結） | ERR-005-003 |
| PC-005-04 | SubmittedBy = Project.SystemArchitect | ERR-005-004 |
| PC-005-05 | FileContent 非空白 | ERR-005-005 |
| PC-005-06 | DocumentType 有效 | ERR-005-006 |

#### Main Steps（主要執行步驟）

```
Step 1：取得專案資訊 + 執行所有 Pre-checks
└── 任一失敗則 Terminate 並回傳錯誤

Step 2：決定 SharePoint 目標資料夾（查閱 Doc 02 Baseline Matrix）
├── TechnicalFeasibility, InitialRiskList, RiskAssessmentStrategy, Other → 01_Feasibility
├── RiskAssessment → 02_Risk_Assessment
├── DesignBaseline, RequirementTraceability, DesignObjectInventory, ChangeImpact → 03_Design
├── IEC62443Checklist, ThreatModel → 04_Security
├── TestPlan, TestReport → 05_Test
└── HandoverMeeting, ResidualRiskList, DocumentRegister → 06_Handover

Step 3：上傳檔案至 SharePoint
├── 將 Base64 轉為 Binary 後上傳
├── 目標路徑：/{RequestID}/{SharePointFolder}/{FileName}
└── 取得上傳後的 SharePoint URL

Step 4：版本推進（Version Progression）
├── 查詢同專案同 DocumentType 的 Active/Draft 記錄
├── 將所有現有 Active/Draft 標記為 Superseded（gov_documentrole = 100000003）
└── 回填 gov_supersededby 指向即將建立的新記錄

Step 5：建立/更新 Document Register 記錄
├── 若存在 Planned 記錄（Baseline Seeding 產生）→ 更新該記錄為 Draft
├── 若無 Planned 記錄 → 新建 Draft 記錄
├── DocumentRole = Draft（100000001）
├── DeliverablePackage = {輸入值}
├── SharePointFileLink = {Step 3 URL}
├── UploadedBy = {SubmittedBy}
└── UploadedDate = utcNow()

Step 6：更新 Project Registry Link（Link 目標規則）
├── 查閱 Baseline Matrix 取得 ProjectRegistryLinkField
├── Link 目標：優先最新 Approved，次選最新 Active/Draft
└── 更新對應 {DocumentType}Link 欄位

Step 7：發送通知
└── 通知文件審查者

Step 8：回傳成功訊息給 Power Apps
└── 包含 DocumentID、SharePointURL、DocumentRole、SupersededCount
```

#### DocumentType 與 SharePoint 資料夾對應

> **權威來源**：Doc 02 Document Baseline Matrix。下表為快速參考副本。

| DocumentType | 目標 SharePoint 資料夾 | 對應 Project Registry 欄位 |
|:------------|:--------------------|:------------------------|
| TechnicalFeasibility | 01_Feasibility | gov_technicalfeasibilitylink |
| InitialRiskList | 01_Feasibility | gov_initialrisklistlink |
| RiskAssessmentStrategy | 01_Feasibility | gov_riskassessmentstrategylink |
| DesignBaseline | 03_Design | gov_designbaselinelink |
| RiskAssessment | 02_Risk_Assessment | gov_riskassessmentlink |
| IEC62443Checklist | 04_Security | gov_iec62443checklistlink |
| ThreatModel | 04_Security | gov_threatmodellink |
| RequirementTraceability | 03_Design | gov_requirementtraceabilitylink |
| TestPlan | 05_Test | gov_testplanlink |
| TestReport | 05_Test | gov_testreportlink |
| HandoverMeeting | 06_Handover | gov_handovermeetinglink |
| ResidualRiskList | 06_Handover | gov_residualrisklistlink |
| DesignObjectInventory | 03_Design | gov_designobjectinventorylink |
| ChangeImpact | 03_Design | gov_changeimpactlink |
| DocumentRegister | 06_Handover | gov_documentregisterlink |
| Other | 01_Feasibility | -（不回寫） |

---

## Idempotency（冪等性）處理

### 設計原則

每個 Flow 必須保證：**同一請求多次執行結果相同，不會產生重複資料**。

### 各 Flow 冪等性策略

| Flow | 冪等性策略 | 實作方式 |
|:----|:----------|:--------|
| GOV-001 | RequestID 唯一性檢查 | 產生 RequestID 後查詢是否已存在，若存在則重新產生（最多 3 次） |
| GOV-002 | RequestStatus 狀態檢查 | Pre-check 4 驗證 RequestStatus = None，若有進行中申請則阻斷 |
| GOV-003 | RequestStatus 狀態檢查 | Pre-check 1 驗證 RequestStatus = Pending，確保僅執行一次 |
| GOV-004 | RiskAcceptanceStatus 狀態檢查 | 檢查 RiskAcceptanceStatus 是否已為 Accepted/Rejected |
| GOV-005 | 版本推進（Version Progression） | 不阻斷重複上傳，改為將舊版標記為 Superseded 並建立新版 Draft |

### 冪等性實作範例（GOV-002）

```
Pre-check 4：重複申請檢查

Action: Get a row by ID (Dataverse)
Table: Project Registry
Row ID: @{triggerBody()?['ProjectId']}

Condition: RequestStatus equals 'None'
├── True: 繼續執行（允許新申請）
└── False: Terminate
    ├── HTTP Status: 409 Conflict
    ├── ErrorCode: ERR-002-058
    └── Message: "專案有進行中的 Gate 申請（RequestStatus = {RequestStatus}），
                 請先撤銷或等待審批完成"
```

---

## Concurrency（並行控制）處理

### 設計原則

防止同一專案的多個請求同時執行，造成狀態不一致或 Race Condition。

### 各 Flow 並行控制策略

| Flow | 並行控制策略 | 設定值 |
|:----|:-----------|:------|
| GOV-001 | Off | 不需並行控制（每次產生新 RequestID） |
| GOV-002 | On | Concurrency Key = ProjectId，Parallelism = 1 |
| GOV-003 | 由父 Flow 控制 | 不需額外設定 |
| GOV-004 | 由父 Flow 控制 | 不需額外設定 |
| GOV-005 | On | Concurrency Key = ProjectId，Parallelism = 1 |
| GOV-006~012 | On | Concurrency Key = ProjectId，Parallelism = 1 |
| GOV-017~019 | Off | 排程 Flow，每次執行獨立 |

### 並行控制設定方式

```
Flow Settings → Settings → Concurrency Control

├── Concurrency Control: On
├── Degree of Parallelism: 1
└── Concurrency Key（運算式）: @{triggerBody()?['ProjectId']}

說明：
- 若同一 ProjectId 有多個請求同時送入
- 僅執行第一個，其餘排隊等待
- 第一個請求執行完成後，才執行下一個
```

### Optimistic Locking（樂觀鎖）

除了 Concurrency Control 外，關鍵更新操作使用 Optimistic Locking 防止 Race Condition：

```
Step 1：讀取記錄時，記錄 ModifiedOn
Action: Get a row by ID (Dataverse)
→ 儲存 OriginalModifiedOn = outputs('Get_project')?['body/ModifiedOn']

Step 2：更新前驗證 ModifiedOn 未被修改
Action: Update a row (Dataverse)
Precondition (OData Filter): ModifiedOn eq '@{variables('OriginalModifiedOn')}'

若 Precondition 不滿足：
├── 代表資料已被其他 Flow 修改
├── Update 失敗
└── 進入 Catch Scope 處理（重試或終止）
```

---

## Failure Handling（失敗處理）

### Try-Catch Scope 標準實作

```
┌─────────────────────────────────────────────────────────────────┐
│ Scope: Try                                                      │
│     ├── Step 1：...                                             │
│     ├── Step 2：...                                             │
│     ├── Step 3：...                                             │
│     └── Step N：...                                             │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ Run after: Failed, Timed out
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ Scope: Catch                                                    │
│     │                                                           │
│     ├── Action: Compose error message                           │
│     │   Inputs: @{result('Try')?[0]?['error']?['message']}      │
│     │                                                           │
│     ├── Action: Add a new row (Flow Execution Error Log)        │
│     │   Columns:                                                │
│     │       - FlowName: @{workflow()?['name']}                  │
│     │       - FlowRunId: @{workflow()?['run']?['name']}         │
│     │       - ErrorMessage: @{outputs('Compose_error')}         │
│     │       - ErrorDate: @{utcNow()}                            │
│     │                                                           │
│     ├── Action: Send an email to System Administrator           │
│     │   Subject: Flow 執行失敗 - @{workflow()?['name']}         │
│     │   Body: 錯誤訊息：@{outputs('Compose_error')}             │
│     │                                                           │
│     └── Action: Respond to PowerApp with HTTP 500               │
│         Body: {"Status": "Failed", "ErrorCode": "ERR-SYSTEM-500",│
│                "Message": "Flow 執行失敗，請聯絡系統管理員"}      │
└─────────────────────────────────────────────────────────────────┘
```

### Compensating Transaction（補償交易）

| Flow | 失敗情境 | 補償動作 |
|:----|:--------|:--------|
| GOV-001 | SharePoint 資料夾建立失敗 | 刪除 Project Registry 記錄 |
| GOV-001 | Review Decision Log 寫入失敗 | 刪除 Project Registry + SharePoint 資料夾 |
| GOV-002 | Review Decision Log 寫入後更新 Project Registry 失敗 | 刪除 Review Decision Log 記錄 |
| GOV-003 | 發送 Approval 後 Flow 失敗 | 無法撤回 Approval，發送錯誤通知給審核者，System Administrator 手動處理 |
| GOV-005 | Document Register 寫入後更新 Project Registry 失敗 | 刪除 Document Register + SharePoint 文件 |

### 不可補償之情境

以下情境無法自動補償，需 System Administrator 手動介入：

| 情境 | 原因 | 處理方式 |
|:----|:-----|:--------|
| 已發送的 Approval | Microsoft Approvals 無撤回 API | 發送通知給審核者，請勿審批此請求 |
| 已發送的 Email | Email 無法撤回 | 發送更正通知 |
| Dataverse Audit Log | 系統層級不可刪除 | 無需處理（保留為稽核證據） |

---

## Ready Gate 驗證清單

### Flow 建立前必要條件

| # | 驗證項目 | 驗證方式 |
|:--|:--------|:--------|
| 1 | Dataverse Tables 已建立 | 確認 Project Registry、Review Decision Log、Document Register 等 Table 存在 |
| 2 | Field-Level Security Profile 已設定 | 確認 Flow Service Principal Profile 已建立並指派 |
| 3 | Flow Service Principal 已設定 | 確認 Application User 已建立並具備 System Administrator 角色 |
| 4 | Office 365 Groups 已建立 | 確認 GOV-Architects、GOV-SecurityReviewers 等群組存在 |
| 5 | SharePoint Site 與 Library 已建立 | 確認 Design Documents Library 存在 |
| 6 | Solution 已建立 | 確認治理系統 Solution 存在 |
| 7 | Environment Variables 已設定 | 確認 Flow URL 使用 Environment Variable 引用 |

### Flow 部署後驗證項目

| # | 驗證項目 | 驗證方式 |
|:--|:--------|:--------|
| 8 | Flow Connection 使用 Service Principal | 檢查 Flow Connection 是否使用 Service Account |
| 9 | Concurrency Control 正確設定 | 檢查 GOV-002、GOV-005 等 Flow 的並行控制設定 |
| 10 | Try-Catch Scope 已實作 | 檢查每個 Flow 是否包含 Try-Catch Scope |
| 11 | Error Response 格式正確 | 測試錯誤情境，驗證回傳格式符合規格 |
| 12 | Pre-checks 阻斷功能正常 | 測試各種前置條件不滿足情境 |
| 13 | Approval 發送給正確群組 | 測試 Gate 申請，驗證 Approval 發送對象 |
| 14 | 狀態轉移正確 | 測試 Gate 0 → 1 → 2 → 3 轉移 |
| 15 | Document Freeze 觸發正常 | 測試 Gate 3 通過後文件凍結 |
| 16 | Notification 發送正常 | 驗證 Teams + Email 通知 |
| 17 | Audit Trail 完整 | 檢查 Review Decision Log 記錄 |
| 18 | Compensating Transaction 正常 | 測試失敗情境，驗證補償動作執行 |

### 整合測試案例

| # | 測試案例 | 預期結果 |
|:--|:--------|:--------|
| 19 | 非授權使用者建立專案 | HTTP 403，ErrorCode: ERR-001-002 |
| 20 | 重複提交 Gate 申請 | HTTP 409，ErrorCode: ERR-002-058 |
| 21 | Gate 1 未滿足文件前置條件 | HTTP 400，ErrorCode: ERR-002-04X |
| 22 | Gate 1 三層審批任一層拒絕 | RequestStatus = None，Notification 發送給 System Architect |
| 23 | Gate 3 Risk Acceptance 未完成即申請審批 | HTTP 400，ErrorCode: ERR-003-010 |
| 24 | Gate 3 通過後文件自動凍結 | DocumentFreezeStatus = Frozen，IsFrozen = Yes |
| 25 | 文件已凍結後嘗試上傳 | HTTP 400，ErrorCode: ERR-005-003 |
| 26 | 同一專案兩個 Gate 申請同時送入 | 第一個執行，第二個排隊等待 |
| 27 | Flow 執行中途失敗 | 補償交易執行，錯誤通知發送給 System Administrator |

---

## 文件修訂記錄

| 版本 | 日期 | 修訂內容 | 修訂者 |
|:----|:-----|:--------|:------|
| 1.0 | 2026-01-29 | 初版建立 | Implementation Team |
| 1.1 | 2026-02-11 | 日常流程修訂：(1) GOV-001 子資料夾對齊 Doc 03（Gate0/Gate1...→01_Feasibility/02_Risk_Assessment...）；(2) GOV-001 新增 Baseline Seeding 步驟（13 筆 Planned Document Register）；(3) GOV-005 完整重寫：Base64 上傳、版本推進（Superseded 鏈）、Link 目標規則、Planned→Draft 更新；(4) DocumentType→Folder 對應表對齊 Doc 02 Baseline Matrix；(5) 新增 ERR-005-005/006 錯誤碼 | Governance Engineering |

---

## 附錄：錯誤代碼總表

| ErrorCode | HTTP Status | Flow | 說明 |
|:----------|:-----------|:----|:----|
| ERR-001-001 | 400 | GOV-001 | 必填欄位未填寫或格式錯誤 |
| ERR-001-002 | 403 | GOV-001 | 僅授權架構師可建立專案 |
| ERR-001-010 | 500 | GOV-001 | RequestID 產生失敗（重試 3 次仍衝突） |
| ERR-002-001 | 404 | GOV-002 | 專案不存在 |
| ERR-002-003 | 403 | GOV-002 | 僅專案 System Architect 可提交 Gate 申請 |
| ERR-002-005 | 400 | GOV-002 | 專案狀態不允許提交申請 |
| ERR-002-020 | 400 | GOV-002 | Gate 0 前置條件不滿足（CurrentGate ≠ Pending） |
| ERR-002-021~023 | 400 | GOV-002 | Gate 0 必要文件未上傳 |
| ERR-002-040 | 400 | GOV-002 | Gate 1 前置條件不滿足（CurrentGate ≠ Gate0） |
| ERR-002-041~047 | 400 | GOV-002 | Gate 1 必要文件未上傳 |
| ERR-002-050 | 400 | GOV-002 | Gate 2 前置條件不滿足 |
| ERR-002-051~052 | 400 | GOV-002 | Gate 2 必要文件未上傳 |
| ERR-002-053 | 400 | GOV-002 | Gate 3 前置條件不滿足（CurrentGate ≠ Gate2） |
| ERR-002-054~057 | 400 | GOV-002 | Gate 3 前置條件未滿足 |
| ERR-002-058 | 409 | GOV-002 | 專案有進行中的 Gate 申請 |
| ERR-003-001 | 400 | GOV-003 | RequestStatus 必須為 Pending |
| ERR-003-010 | 400 | GOV-003 | Risk Acceptance 尚未完成（Gate 3） |
| ERR-005-001 | 404 | GOV-005 | 專案不存在 |
| ERR-005-002 | 400 | GOV-005 | 專案狀態不允許上傳 |
| ERR-005-003 | 400 | GOV-005 | 文件已凍結，不允許上傳 |
| ERR-005-004 | 403 | GOV-005 | 僅專案 System Architect 可上傳文件 |
| ERR-005-005 | 400 | GOV-005 | 檔案內容為空白（Base64 為空） |
| ERR-005-006 | 400 | GOV-005 | DocumentType 無效 |
| ERR-013-001 | 400 | GOV-013 | Risk Register 中無此專案的風險項目 |
| ERR-SYSTEM-500 | 500 | All | Flow 執行失敗，請聯絡系統管理員 |

---

## 附錄：Flow 執行時間限制

| 限制項目 | 限制值 | 緩解方案 |
|:--------|:------|:--------|
| Flow 執行超時 | 30 天 | Approval 設定合理超時通知（7 天未回覆發送提醒） |
| Dataverse API Rate Limit | 6,000 次 / 5 分鐘 / 使用者 | 使用 Service Account 執行 Flow |
| HTTP Request 超時 | 2 分鐘 | 長時間操作改用 Child Flow 或 Queue |
| Approval 無法撤回 | - | 發送前確保所有 Pre-checks 已通過 |
