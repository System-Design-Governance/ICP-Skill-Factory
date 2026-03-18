# SOP 修補計畫

## SOP-Patch-Plan

**計畫類型**：SOP Documentation Patch Plan
**計畫日期**：2026-02-09
**依據報告**：SOP-Operability-Forensics-Report.md
**修補原則**：僅 SOP 層面修補，不修改 Dataverse 資料模型、不修改 Gate 流程

---

## 修補清單總覽

| 編號 | 優先級 | 問題編號 | 修補標的 | 工作量 |
|:----:|:------:|---------|---------|:------:|
| PATCH-001 | P0 | P0-001 | 04 文件循環相依解法 | 小 |
| PATCH-002 | P0 | P0-002 | 05/06 文件 GOV-017/018/019 重複消除 | 中 |
| PATCH-003 | P0 | P0-003 | 02 文件 Counter List 初始化 | 小 |
| PATCH-004 | P1 | P1-001 | 02 文件 Choice Set 引用修正 | 小 |
| PATCH-005 | P1 | P1-002~004 | 01 文件占位符統一清單 | 中 |
| PATCH-006 | P1 | P1-005 | 07 文件 Base URL 說明 | 小 |
| PATCH-007 | P1 | P1-006~007 | 02 文件欄位定義補齊 | 中 |
| PATCH-008 | P2 | P2-001~008 | 各文件雜項修補 | 小 |

---

## PATCH-001：04 文件循環相依解法

### 基本資訊

| 項目 | 內容 |
|------|------|
| **檔名/位置** | `domains/project-governance/docs/power-platform-governance/zh-TW/04-powerapps-forms.md` |
| **問題編號** | P0-001 |
| **工作量** | 小（約 30 分鐘） |

### 建議內容

在 04 文件「文件使用說明」章節後新增以下內容：

```markdown
## 本章建置順序說明

> **重要**：本章分為兩個階段執行，中間需穿插第 05 章。

### 階段一：Power Apps 框架建置（本章前半）

**執行時機**：完成 02、03 章的 Ready Gate 後立即執行

**執行內容**：
1. 建立 Canvas App
2. 建立所有表單 UI（FORM-001 至 FORM-011）
3. 設定表單驗證邏輯
4. **暫停**：此時表單的「Submit」按鈕尚未連接 Flow

**完成標誌**：
- [ ] 所有表單 UI 已建立
- [ ] 驗證邏輯已設定
- [ ] 表單可預覽但提交功能尚未完成

### 穿插執行第 05 章

**執行時機**：完成階段一後

**執行內容**：
1. 建立所有 GOV-001 至 GOV-019 Flow
2. 完成 05 章的 Flow Ready Gate

### 階段二：Flow 連接與發佈（本章後半）

**執行時機**：完成 05 章的 Flow Ready Gate 後返回執行

**執行內容**：
1. 將所有表單的「Submit」按鈕連接至對應的 Flow
2. 測試表單提交功能
3. 發佈 Power Apps

**完成標誌**：
- [ ] 所有表單已連接 Flow
- [ ] 表單提交測試通過
- [ ] Power Apps 已發佈

---

### 階段流程圖

```
04 章 階段一（UI 建置）
        │
        ▼
   05 章（Flow 建置）
        │
        ▼
04 章 階段二（Flow 連接 + 發佈）
        │
        ▼
   06 章（Guardrails 確認）
```
```

### 目的與驗證方式

| 項目 | 內容 |
|------|------|
| **目的** | 消除執行者對文件循環相依的困惑，明確定義兩階段建置順序 |
| **驗證方式** | 新進人員可無卡點完成 04 → 05 → 04 的穿插執行 |

### 風險等級

| 等級 | 說明 |
|:----:|------|
| **低** | 僅新增說明文字，不影響現有內容 |

---

## PATCH-002：05/06 文件 GOV-017/018/019 重複消除

### 基本資訊

| 項目 | 內容 |
|------|------|
| **檔名/位置** | `06-guardrails-and-anti-cheating.md` |
| **問題編號** | P0-002 |
| **工作量** | 中（約 2 小時） |

### 建議內容

**方案 A（建議採用）**：重新定位 06 文件

將 06 文件從「施工文件」轉型為「設計說明與稽核參考」：

1. **保留內容**：
   - Guardrail 三道防線架構說明
   - 監控 Flow 清單（概覽表格）
   - 偵測原理圖
   - Flow-only 欄位完整清單
   - 回滾執行機制說明
   - 通知與升級規則
   - 監控指標與 KPI
   - 通知範本

2. **移除內容**：
   - GOV-017 實作步驟（2.1~2.9 節）
   - GOV-018 實作步驟（3.1~3.4 節）
   - GOV-019 實作步驟

3. **新增內容**：
   在文件開頭新增定位聲明：

```markdown
## 文件定位

**本文件為 Guardrail 機制的設計說明與稽核參考文件。**

### 本文件用途

| 用途 | 說明 |
|------|------|
| 理解 Guardrail 設計 | 供架構師理解三道防線的設計意圖 |
| 稽核審查 | 供稽核人員驗證 GOV-017/018/019 是否符合設計 |
| 監控指標參考 | 供維運人員理解監控指標與 KPI |
| 通知範本參考 | 供維運人員自訂通知內容 |

### 本文件禁止用途

| 禁止用途 | 正確做法 |
|---------|---------|
| 作為 GOV-017/018/019 的實作依據 | 請依據 **05-core-flows-implementation-runbook.md** 進行實作 |

> **警告**：GOV-017/018/019 的唯一施工依據為第 05 章。本文件的任何步驟描述僅供理解設計意圖，禁止直接用於實作。
```

### 目的與驗證方式

| 項目 | 內容 |
|------|------|
| **目的** | 消除 05/06 文件的內容重複，明確 06 文件定位為「設計說明」而非「施工文件」 |
| **驗證方式** | 執行者在建置 GOV-017/018/019 時僅參考 05 文件，不會因 06 文件的不同版本步驟而混淆 |

### 風險等級

| 等級 | 說明 |
|:----:|------|
| **中** | 需移除大量內容，但不影響系統功能，僅影響文件結構 |

---

## PATCH-003：02 文件 Counter List 初始化

### 基本資訊

| 項目 | 內容 |
|------|------|
| **檔名/位置** | `02-dataverse-data-model-and-security.md` |
| **問題編號** | P0-003 |
| **工作量** | 小（約 15 分鐘） |

### 建議內容

在 02 文件 `gov_counterlist` 章節末尾新增：

```markdown
### Counter List 初始化步驟

> **重要**：此步驟必須在 05 章建立 GOV-001 Flow 前完成。若未初始化，GOV-001 首次執行將因 Counter List 無記錄而失敗。

#### 操作步驟

1. **導覽路徑**：Power Apps Maker Portal → Tables → Counter List → Data → + New row

2. **填寫以下欄位**：

| 欄位 | 填寫值 |
|------|-------|
| Counter Type | `RequestID` |
| Current Value | `0` |
| Prefix | `DR` |
| Year Format | `yyyy` |
| Description | `專案 RequestID 流水號產生器` |

3. **點擊 Save**

#### 驗證步驟

1. 查詢 Counter List 資料表
2. 確認有一筆 Counter Type = `RequestID` 的記錄
3. 確認 Current Value = 0

**確認此步驟成功**：Counter List 中存在 RequestID 類型的記錄，初始值為 0。
```

### 目的與驗證方式

| 項目 | 內容 |
|------|------|
| **目的** | 確保 GOV-001 首次執行時 Counter List 有可用記錄，避免 Flow 執行失敗 |
| **驗證方式** | 執行 GOV-001 時成功產生 `DR-2026-{ShortGuid}` 格式的 RequestID |

### 風險等級

| 等級 | 說明 |
|:----:|------|
| **低** | 僅新增初始化步驟說明 |

---

## PATCH-004：02 文件 Choice Set 引用修正

### 基本資訊

| 項目 | 內容 |
|------|------|
| **檔名/位置** | `02-dataverse-data-model-and-security.md` |
| **問題編號** | P1-001 |
| **工作量** | 小（約 10 分鐘） |

### 建議內容

修正第 311 行附近的 Choice 欄位建立說明：

**修正前**：
```markdown
4. 在 Sync this choice with 選擇 **gov_currentgate**（全域選項集，將在第 5 章建立）
```

**修正後**：
```markdown
4. 在 Sync this choice with 選擇 **gov_currentgate**（全域選項集，請先在本章「全域選項集建立」章節建立）

> **注意**：若 gov_currentgate 選項集尚未建立，請先跳至本章「全域選項集建立」章節完成建立後再返回。
```

### 目的與驗證方式

| 項目 | 內容 |
|------|------|
| **目的** | 消除執行者對「第 5 章建立」的誤解，避免跳過選項集建立 |
| **驗證方式** | 執行者在建立 Choice 欄位時正確找到選項集定義位置 |

### 風險等級

| 等級 | 說明 |
|:----:|------|
| **低** | 僅修正引用說明 |

---

## PATCH-005：01 文件占位符統一清單

### 基本資訊

| 項目 | 內容 |
|------|------|
| **檔名/位置** | `01-prerequisites-and-environment.md` |
| **問題編號** | P1-002、P1-003、P1-004 |
| **工作量** | 中（約 1 小時） |

### 建議內容

在 01 文件 Environment Ready Gate 後新增：

```markdown
## 占位符與環境變數清單

> **重要**：以下清單包含所有需在後續文件中替換的占位符。請在完成環境準備後，將實際值記錄於此清單，以便在後續文件中統一替換。

### Service Principal 相關

| 占位符 | 說明 | 您的實際值 | 使用位置 |
|--------|------|-----------|---------|
| `<Flow-Service-Principal-ID>` | Flow Service Principal 的 GUID | ________________ | 05 文件 GOV-017 篩選條件 |
| `{Flow Service Principal User ID}` | 同上（另一種寫法） | ________________ | 05 文件多處 |
| `{org}` | Dataverse 環境的組織名稱 | ________________ | 06 文件 HTTP 請求 URI |

### 取得 Service Principal GUID 的方法

1. **導覽路徑**：Azure Portal → Azure Active Directory → Enterprise applications
2. 搜尋 `GOV-FlowServicePrincipal`
3. 複製 **Object ID**（即 GUID）

### 通知收件人相關

| 占位符 | 說明 | 您的實際值 | 使用位置 |
|--------|------|-----------|---------|
| `GOV-GovernanceLead@contoso.com` | Governance Lead 收件人 | ________________ | 05、06 文件通知設定 |
| `GOV-EngineeringManagement@contoso.com` | Engineering Management 收件人 | ________________ | 05、06 文件通知設定 |
| `GOV-SystemAdmin@contoso.com` | System Admin 收件人 | ________________ | 05、06 文件錯誤通知 |
| `{治理團隊 Team}` | Teams Team 名稱或 ID | ________________ | 05、06 文件 Teams 通知 |
| `{違規通知 Channel}` | Teams Channel 名稱或 ID | ________________ | 05、06 文件 Teams 通知 |

### 建議做法

1. **使用 Security Group**：建議將上述收件人設定為 Microsoft 365 Security Group，而非個人 Email
2. **使用 Mail-enabled Security Group**：確保 Security Group 可接收 Email
3. **記錄 Teams Team/Channel ID**：可透過 Teams URL 取得

### 環境 URL 相關

| 占位符 | 說明 | 您的實際值 | 使用位置 |
|--------|------|-----------|---------|
| `{{base_url}}` | Dataverse Web API Base URL | ________________ | 07 文件測試案例 |
| `{Power App URL}` | 治理系統 Power App URL | ________________ | 05、06 文件通知連結 |
| `{Approvals App URL}` | Power Automate Approvals App URL | ________________ | 05 文件通知連結 |

### 取得 Base URL 的方法

1. **格式**：`https://{org}.api.crm.dynamics.com/api/data/v9.2`
2. **取得方式**：
   - Power Apps Maker Portal → Settings (齒輪) → Session details
   - 複製 Instance url
   - 加上 `/api/data/v9.2` 後綴
```

### 目的與驗證方式

| 項目 | 內容 |
|------|------|
| **目的** | 集中列出所有占位符，避免執行者在後續文件中遺漏替換 |
| **驗證方式** | 執行者在 01 章即記錄所有必要資訊，後續文件無需返回查找 |

### 風險等級

| 等級 | 說明 |
|:----:|------|
| **低** | 僅新增參考清單 |

---

## PATCH-006：07 文件 Base URL 說明

### 基本資訊

| 項目 | 內容 |
|------|------|
| **檔名/位置** | `07-testing-and-acceptance.md` |
| **問題編號** | P1-005 |
| **工作量** | 小（約 15 分鐘） |

### 建議內容

在 07 文件開頭新增：

```markdown
## 測試環境準備

### 必要工具

| 工具 | 用途 | 取得方式 |
|------|------|---------|
| Postman 或 Bruno | HTTP 請求測試 | 官網下載 |
| Azure AD Token | API 認證 | 下方說明 |
| 測試帳號 | 模擬不同角色 | 01 文件 Security Group 成員 |

### 環境變數設定

本文件的測試案例使用以下環境變數，請在執行前設定：

| 變數名稱 | 說明 | 取得方式 |
|---------|------|---------|
| `{{base_url}}` | Dataverse Web API Base URL | 格式：`https://{org}.api.crm.dynamics.com/api/data/v9.2` |
| `{{access_token}}` | Azure AD Bearer Token | 下方說明 |

### 取得 Base URL

1. **導覽路徑**：Power Apps Maker Portal → Settings (齒輪) → Session details
2. 複製 **Instance url**（例如：`https://org12345.crm.dynamics.com`）
3. 加上 `/api/data/v9.2` 後綴
4. 完整格式：`https://org12345.api.crm.dynamics.com/api/data/v9.2`

### 取得 Access Token

**方法一：使用 Azure AD 應用程式註冊**

```http
POST https://login.microsoftonline.com/{tenant-id}/oauth2/v2.0/token
Content-Type: application/x-www-form-urlencoded

client_id={client-id}
&client_secret={client-secret}
&scope=https://{org}.crm.dynamics.com/.default
&grant_type=client_credentials
```

**方法二：使用 Postman Authorization**

1. 在 Postman 選擇 Authorization → OAuth 2.0
2. 設定 Token URL：`https://login.microsoftonline.com/{tenant-id}/oauth2/v2.0/token`
3. 設定 Scope：`https://{org}.crm.dynamics.com/.default`
4. 點擊 Get New Access Token

### 測試帳號清單

| 帳號 | 角色 | 用途 |
|------|------|------|
| `testuser1@{domain}` | System Architect | 提交專案、Gate 申請 |
| `testuser2@{domain}` | Project Manager | 專案檢視 |
| `testgovlead@{domain}` | Governance Lead | 審批、違規處理 |
| `testsecurity@{domain}` | Security Reviewer | Gate 1 Security 審批 |
| `testqa@{domain}` | QA Reviewer | Gate 1 QA 審批 |
| `testadmin@{domain}` | System Admin | 環境管理、錯誤通知 |
```

### 目的與驗證方式

| 項目 | 內容 |
|------|------|
| **目的** | 確保執行者在執行測試案例前已準備好環境變數與測試帳號 |
| **驗證方式** | 執行者可成功執行 HTTP 請求驗證 Dataverse 資料 |

### 風險等級

| 等級 | 說明 |
|:----:|------|
| **低** | 僅新增環境準備說明 |

---

## PATCH-007：02 文件欄位定義補齊

### 基本資訊

| 項目 | 內容 |
|------|------|
| **檔名/位置** | `02-dataverse-data-model-and-security.md` |
| **問題編號** | P1-006、P1-007 |
| **工作量** | 中（約 1 小時） |

### 建議內容

在 02 文件 `gov_projectregistry` 欄位清單補充以下欄位：

```markdown
#### 專案終止相關欄位（補充）

| 欄位顯示名稱 | Schema Name | 資料類型 | 必填 | Flow-only | 說明 |
|-------------|-------------|---------|------|-----------|------|
| Termination Reason | gov_terminationreason | Choice (gov_terminationreason) | No | **Yes** | 終止原因（BusinessDecision / TechnicalIssue / ResourceConstraint / Other） |
| Termination Date | gov_terminationdate | Date and Time | No | **Yes** | 終止時間 |
| Terminated By | gov_terminatedby | Lookup (User) | No | **Yes** | 終止決策者 |
| Termination Comments | gov_terminationcomments | Multiple lines of text (2000) | No | No | 終止說明 |

#### 專案結案相關欄位（補充）

| 欄位顯示名稱 | Schema Name | 資料類型 | 必填 | Flow-only | 說明 |
|-------------|-------------|---------|------|-----------|------|
| Closure Date | gov_closuredate | Date and Time | No | **Yes** | 結案時間 |
| Closed By | gov_closedby | Lookup (User) | No | **Yes** | 結案審批者 |
| Closure Summary | gov_closuresummary | Multiple lines of text (2000) | No | No | 結案摘要 |

#### 新增 Choice Set：gov_terminationreason

| 顯示值 | 數值 | 說明 |
|-------|------|------|
| BusinessDecision | 100000000 | 業務決策終止 |
| TechnicalIssue | 100000001 | 技術問題終止 |
| ResourceConstraint | 100000002 | 資源限制終止 |
| Other | 100000003 | 其他原因終止 |
```

### 目的與驗證方式

| 項目 | 內容 |
|------|------|
| **目的** | 確保 07 文件測試案例引用的欄位皆在 02 文件定義 |
| **驗證方式** | 執行 E2E-008、E2E-009 測試案例無欄位缺失錯誤 |

### 風險等級

| 等級 | 說明 |
|:----:|------|
| **中** | 需新增欄位定義，但為補充遺漏而非變更設計 |

---

## PATCH-008：各文件雜項修補

### 基本資訊

| 項目 | 內容 |
|------|------|
| **檔名/位置** | 多個文件 |
| **問題編號** | P2-001~008 |
| **工作量** | 小（約 30 分鐘） |

### 建議內容

#### P2-001：驗證步驟補充具體預期值

在 05 文件各「確認此步驟成功」區塊，補充具體預期值：

```markdown
**確認此步驟成功**：
- Flow Run History 顯示 **Succeeded**（綠色勾號）
- 執行時間 < 30 秒
- 無任何 Retry 紀錄
```

#### P2-002：Publisher Prefix 說明

在 01 文件「Solution 建立」章節新增：

```markdown
### Publisher Prefix 設定

> **注意**：本文件所有 Dataverse 資源使用 `gov_` 作為 Publisher Prefix。

#### 確認方式

1. **導覽路徑**：Power Apps Maker Portal → Solutions → {Solution} → Settings → Publisher
2. 確認 Prefix 欄位為 `gov`

#### 若需變更 Prefix

1. 建立新的 Publisher，設定 Prefix 為 `gov`
2. 將 Solution 的 Publisher 設定為新建立的 Publisher

> **警告**：若 Prefix 不是 `gov_`，所有後續文件的 Schema Name 皆需調整。建議統一使用 `gov_`。
```

#### P2-004：Connection Reference 預建立

在 01 文件「Service Principal 建立」章節後新增：

```markdown
### Connection Reference 預建立

> **建議**：在建立 Flow 前先建立 Connection Reference，可簡化後續 Flow 設定。

| Connection Reference 名稱 | Connector | 身分 |
|--------------------------|-----------|------|
| CR-Dataverse-SPN | Microsoft Dataverse | Flow Service Principal |
| CR-SharePoint-SPN | SharePoint | Flow Service Principal |
| CR-Approvals | Approvals | Flow Service Principal |
| CR-Outlook | Office 365 Outlook | Flow Service Principal |
| CR-Teams | Microsoft Teams | Flow Service Principal |

#### 建立步驟

1. **導覽路徑**：Power Automate Portal → Solutions → {Solution} → New → Connection Reference
2. 填寫 Display Name（如 `CR-Dataverse-SPN`）
3. 選擇 Connector（如 `Microsoft Dataverse`）
4. 選擇或建立使用 Flow Service Principal 的 Connection
5. 點擊 Create

重複以上步驟建立所有 Connection Reference。
```

#### P2-006：Flow 依賴順序圖前置

將 05 文件的 Flow 依賴順序圖移至文件開頭「文件使用說明」後：

```markdown
## Flow 建置順序總覽

> **重要**：請依以下順序建立 Flow，避免 Child Flow 尚未建立導致 Parent Flow 無法設定。

### 建置順序圖

```
第一批：Child Flows（無相依）
├── GOV-015 Notification Service
├── GOV-013 Risk Level Calculator
├── GOV-014 Document Freeze Controller
└── GOV-016 Rework Handler

第二批：依賴 Child Flows
├── GOV-004 Risk Acceptance (依賴 GOV-013)
├── GOV-003 Gate Approval Engine (依賴 GOV-015, GOV-016)
└── GOV-005 Document Intake (依賴 GOV-015)

第三批：依賴第二批
├── GOV-002 Gate Request Receiver (依賴 GOV-003, GOV-004)
└── GOV-001 Project Intake (依賴 GOV-015)

第四批：Scheduled Flows
├── GOV-017 Guardrail Monitor
├── GOV-018 Compliance Reconciler
└── GOV-019 SLA Monitor
```
```

### 目的與驗證方式

| 項目 | 內容 |
|------|------|
| **目的** | 消除各文件的小摩擦點，提升整體可操作性 |
| **驗證方式** | 新進人員無需在多處查找資訊，可順暢執行各文件 |

### 風險等級

| 等級 | 說明 |
|:----:|------|
| **低** | 皆為補充說明，不影響現有內容 |

---

## 修補執行計畫

### 執行順序

| 順序 | 修補編號 | 預估時間 | 相依性 |
|:----:|---------|:--------:|-------|
| 1 | PATCH-003 | 15 分鐘 | 無 |
| 2 | PATCH-004 | 10 分鐘 | 無 |
| 3 | PATCH-007 | 60 分鐘 | 無 |
| 4 | PATCH-005 | 60 分鐘 | 無 |
| 5 | PATCH-006 | 15 分鐘 | PATCH-005 |
| 6 | PATCH-001 | 30 分鐘 | 無 |
| 7 | PATCH-002 | 120 分鐘 | 無 |
| 8 | PATCH-008 | 30 分鐘 | 無 |

**總預估時間**：約 5.5 小時

### 驗證計畫

修補完成後，執行以下驗證：

1. **文件結構驗證**：確認所有修補內容已正確套用
2. **交叉引用驗證**：確認文件間引用正確
3. **新進人員模擬演練**：請一位未參與建置的人員依文件執行，記錄卡點
4. **端到端測試**：完成 07 文件所有測試案例

---

## 附錄：未納入修補範圍的項目

以下項目經評估後決定不納入本次修補：

| 項目 | 排除原因 |
|------|---------|
| 新增 Dataverse Entity | 超出「僅 SOP 層面修補」範圍 |
| 修改 Gate 流程邏輯 | 超出「僅 SOP 層面修補」範圍 |
| 新增 Flow | 超出「僅 SOP 層面修補」範圍 |
| 06 文件 TODO-005（Power BI 報表規格） | 屬於「nice to have」功能，非必要 |

---

**計畫結束**

**計畫撰寫人員**：Claude Opus 4.5
**計畫日期**：2026-02-09
**依據報告**：SOP-Operability-Forensics-Report.md
