# Dataverse 資料模型與安全性建置指南

**文件版本**：v2.4
**建立日期**：2026-02-09
**最後更新**：2026-03-05
**適用系統**：Design Governance System（Dataverse 架構）
**前置文件**：01-prerequisites-and-environment.md
**後續文件**：03-sharepoint-architecture.md

---


## 文件使用說明

### 文件定位

本文件為 Design Governance System 建置的**第二份實作文件**，涵蓋所有 Dataverse 資料模型與安全性設定。

**前置條件**：必須完成 01-Prerequisites-and-Environment.md 的 Environment Ready Gate。

### 章節相依性

| 章節 | 相依於 | 影響的後續功能 |
|:-----------------|:-------------------------|:----------------------|
| 3. Record Owner 策略 | 01 文件 Service Principal | 所有資料記錄的擁有權控制 |
| 4. 資料表建立 | 無 | 所有資料存取 |
| 7. Flow-only 欄位 | 4 | 治理邏輯完整性 |
| 8. Field-Level Security | 4, 7 | 欄位層級存取控制 |
| 9. 非授權修改偵測 | 7, 8 | GOV-017/018 監控流程 |
| 10. 違規事件模型 | 9 | SOP-04/05 監控與回應 |

### Dataverse 基本概念說明

若您第一次使用 Dataverse，請先理解以下概念：

| 概念 | 說明 | 類比 |
|:----------------|:------------------------------|:----------------|
| **Table（資料表）** | 儲存資料的結構，類似資料庫中的表格 | Excel 工作表 |
| **Column（欄位）** | 資料表中的屬性，定義資料類型 | Excel 欄位標題 |
| **Row（記錄）** | 資料表中的一筆資料 | Excel 資料列 |
| **Owner（擁有者）** | 每筆記錄的擁有者，決定基本存取權限 | 文件擁有者 |
| **Lookup（查閱）** | 參考其他資料表的欄位，建立關聯 | Excel VLOOKUP |
| **Choice（選項集）** | 預定義的選項清單 | Excel 下拉選單 |
| **Security Role（安全角色）** | 定義使用者對資料表的存取權限 | 資料夾權限 |
| **Field Security Profile** | 定義使用者對特定欄位的存取權限 | 欄位層級權限 |

---

## 資料模型架構總覽

### Entity 三層分類

本治理系統採用三層 Entity 分類架構：

| Entity 類型 | 特性 | 可修改性 | 範例 |
|:--------------------------|:---------------------|:--------------------------|:------------------------|
| **Event Entity（事件實體）** | 不可變，記錄歷史事件 | Append-Only（僅新增） | Review Decision Log |
| **Aggregate Entity（聚合實體）** | 記錄當前狀態，由 Event 推導 | 狀態欄位僅 Flow 可改 | Project Registry |
| **Reference Entity（參考實體）** | 主資料，作為 Lookup 參考 | 系統管理員可改 | Counter List |

### 資料表清單

| 資料表 Schema Name | 顯示名稱 | Entity 類型 | 用途 | Record Owner |
|:------------------------------|:------------------------|:------------------------|:------------------------|:------------------------|
| `gov_projectregistry` | Project Registry | Aggregate | 專案主檔 | Flow Service Principal |
| `gov_reviewdecisionlog` | Review Decision Log | Event | 審批事件記錄 | Flow Service Principal |
| `gov_riskassessmenttable` | Risk Assessment Table | Event + Aggregate | 風險評估 | Flow Service Principal |
| `gov_exceptionwaiverlog` | Exception Waiver Log | Event | 例外豁免記錄 | Flow Service Principal |
| `gov_documentregister` | Document Register | Reference | 文件清冊 | Flow Service Principal |
| `gov_governanceviolationlog` | Governance Violation Log | Event | 治理違規記錄 | Flow Service Principal |
| `gov_bomregistry` | BOM Registry | Aggregate | 物料清單（CBOM/EBOM）| Flow Service Principal |
| `gov_sahandoverevent` | SA Handover Event | Event | SA 交接記錄 | Flow Service Principal |
| `gov_counterlist` | Counter List | Reference | 流水號產生器 | Flow Service Principal |
| `gov_standardfeedback` | Standard Feedback | Event | 標準回饋記錄 | Flow Service Principal |
| `gov_disputelog` | Dispute Log | Event | 爭議記錄 | Flow Service Principal |
| `gov_actionitem` | Action Item | Event + Aggregate | 行動項目追蹤 | Flow Service Principal |
| `gov_standardsregistry` | Standards Registry | Reference | 部門標準登錄冊 | Flow Service Principal |
| `gov_processlog` | Process Log | Event | 流程提醒日誌 | Flow Service Principal |
| `gov_externalunit` | External Unit | Reference | 外部單位登錄 | Flow Service Principal |
| `gov_srcompliancesummary` | SR Compliance Summary | Reference | SR 合規摘要 | Flow Service Principal |

### Entity Relationship Diagram

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              治理資料模型                                        │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │                    gov_projectregistry（專案主檔）                        │   │
│  │  RequestID (PK) │ Title │ CurrentGate │ RequestStatus │ Owner=Flow      │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                    │                                            │
│        ┌───────────────────────────┼───────────────────────┬───────────┐       │
│        │ 1:N                       │ 1:N                   │ 1:N       │ 1:N   │
│        ▼                           ▼                       ▼           ▼       │
│  ┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐ ┌────────┐│
│  │gov_reviewdecision│   │gov_riskassessment│   │gov_documentregist│ │gov_bom ││
│  │       log        │   │      table       │   │       er         │ │registry││
│  │  Owner=Flow      │   │   Owner=Flow     │   │   Owner=Flow     │ │Owner=  ││
│  └──────────────────┘   └──────────────────┘   └──────────────────┘ │ Flow   ││
│            │                       │                                 └────────┘│
│            │ 1:N                   │ N:1                      (CBOM/EBOM)       │
│            ▼                       ▼                                            │
│  ┌──────────────────┐   ┌──────────────────┐                                   │
│  │gov_exceptionwaiver│   │gov_governance   │                                   │
│  │       log        │   │  violationlog   │                                   │
│  │   Owner=Flow     │   │   Owner=Flow    │                                   │
│  └──────────────────┘   └──────────────────┘                                   │
│                                                                                 │
│  ┌─────────────────────────── KPI 證據採集層 ──────────────────────────┐   │
│  │                                                                       │   │
│  │  gov_standardfeedback ──┐                                             │   │
│  │  gov_disputelog ────────┤                                             │   │
│  │  gov_actionitem ────────┼──▶ gov_projectregistry                      │   │
│  │  gov_processlog ────────┤                                             │   │
│  │  gov_srcompliancesummary┘                                             │   │
│  │                                                                       │   │
│  │  gov_standardsregistry    （獨立，無專案關聯）                          │   │
│  │  gov_externalunit         （獨立，無專案關聯）                          │   │
│  │                                                                       │   │
│  └───────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
│  ┌──────────────────────── 專案支援層 ────────────────────────────┐   │
│  │                                                                       │   │
│  │  gov_sahandoverevent ──────▶ gov_projectregistry                      │   │
│  │   Owner=Flow                 （SA 交接事件，N:1）                      │   │
│  │                                                                       │   │
│  │  gov_counterlist             （獨立，流水號產生器）                     │   │
│  │   Owner=Flow                                                          │   │
│  │                                                                       │   │
│  └───────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Record Owner 治理策略

### 為何 Record Owner 必須為 Flow Service Principal

> **核心原則：所有治理核心資料表的 Record Owner 一律為 Flow Service Principal。**
> **任何人類使用者不得成為 Record Owner。**

#### Dataverse Owner 機制說明

在 Dataverse 中，每筆記錄（Row）都有一個 **Owner** 欄位，決定：
- 誰可以讀取此記錄（基於安全角色的 User/Business Unit/Organization 層級）
- 誰可以修改此記錄
- 誰可以刪除此記錄

**預設行為**：當使用者透過 UI 或 API 建立記錄時，Owner 自動設為該使用者。

#### 為何禁止人類使用者成為 Owner

| 風險 | 說明 | 後果 |
|:------------------------|:------------------------------|:------------------------------|
| **治理邏輯繞過** | Owner 對自己的記錄有完整權限，可繞過 Field-Level Security | 人類可修改 Flow-only 欄位 |
| **離職風險** | 若 Owner 離職，該帳號停用後可能影響記錄存取 | 專案記錄無法修改或存取 |
| **權限過度集中** | Owner 可刪除自己的記錄 | 稽核記錄可被刪除 |
| **稽核追溯困難** | 無法區分「Owner 身份修改」與「Flow 修改」 | 治理閉環無法驗證 |

#### Record Owner 策略設計

| 資料表 | Record Owner | 建立方式 | 理由 |
|:------------------------------|:------------------------|:------------------------------|:--------------------------------------------------|
| gov_projectregistry | Flow Service Principal | 僅 GOV-001 Flow 可建立 | 確保 RequestID 由 Flow 產生，狀態欄位僅 Flow 可控制 |
| gov_reviewdecisionlog | Flow Service Principal | 僅 GOV Flow 可建立 | Event 記錄為不可變稽核證據 |
| gov_riskassessmenttable | Flow Service Principal | 僅 GOV-005/006 Flow 可建立 | 風險等級由 Flow 計算 |
| gov_exceptionwaiverlog | Flow Service Principal | 僅 GOV-009 Flow 可建立 | 豁免狀態由 Flow 控制 |
| gov_documentregister | Flow Service Principal | 僅 GOV-005 Flow 可建立 | 文件連結由 Flow 產生 |
| gov_governanceviolationlog | Flow Service Principal | 僅 GOV-017/018 Flow 可建立 | 違規記錄為最高機密稽核證據 |
| gov_bomregistry | Flow Service Principal | 僅 GOV Flow 可建立 | BOM 狀態由 Flow 控制，確保 CBOM/EBOM 狀態流轉正確 |
| gov_counterlist | Flow Service Principal | 初始由管理員建立，後續僅 Flow 可更新 | 流水號僅 Flow 可遞增 |
| gov_standardfeedback | Flow Service Principal | 僅 GOV-022 Flow 可建立 | 標準回饋紀錄為稽核證據 |
| gov_disputelog | Flow Service Principal | 僅 GOV-023 Flow 可建立 | 爭議紀錄為稽核證據 |
| gov_actionitem | Flow Service Principal | 僅 GOV-024 Flow 可建立 | 行動項目狀態由 Flow 控制 |
| gov_standardsregistry | Flow Service Principal | 初始由管理員建立，後續 GovLead 可更新 | 標準清冊為治理基礎資料 |
| gov_processlog | Flow Service Principal | 僅 GOV-015 Flow 可建立 | 流程日誌為自動記錄 |
| gov_externalunit | Flow Service Principal | 初始由管理員建立，後續 GovLead 可更新 | 外部單位為治理基礎資料 |
| gov_srcompliancesummary | Flow Service Principal | 初始由管理員建立，後續 GovLead 可更新 | SR 合規記錄為評估基礎 |
| gov_sahandoverevent | Flow Service Principal | 僅 GOV Flow 可建立 | SA 交接事件為稽核證據 |

### 技術實作：確保 Owner 為 Flow Service Principal

> **注意**：以下說明 Owner 設定的技術原理。實際的 Flow 建立將於第 05 章執行，此處僅說明設計目的與預期行為。

#### 方法一：Flow 建立記錄時指定 Owner（於第 05 章實作）

**設計規格**：所有 GOV Flow 在執行「Create a new row」動作時，必須明確指定 Owner 為 Flow Service Principal。

預期設定結構：
```
操作：Dataverse - Add a new row
設定：
  - Table name: gov_projectregistry
  - Owner: GOV-FlowServicePrincipal（Application User ID）
  - 其他欄位...
```

**此設定將於第 05 章「Power Automate 核心 Flows 施工手冊」中實際執行**。

#### 方法二：Business Rule 強制設定 Owner（本章可選配置）

**操作路徑**：
1. Power Apps Maker Portal → Tables → gov_projectregistry
2. 選擇 **Business rules** 標籤
3. 點擊 **+ New business rule**

**Business Rule 設定**：
```
名稱：Force Owner to Flow Service Principal
觸發條件：Entity = gov_projectregistry, Scope = Entity
條件：Owner 不等於 [Flow Service Principal ID]
動作：Set Field Value - Owner = [Flow Service Principal ID]
```

**注意**：Business Rule 在記錄儲存前執行，可強制修正 Owner。

#### 方法三：安全角色限制 Create 權限

**設計原則**：僅授予 Flow Service Principal 的安全角色 Create 權限。

| 安全角色 | gov_projectregistry Create 權限 |
|:------------------------------|:-------------------------------|
| GOV-SystemArchitect | **None**（無法直接建立） |
| GOV-FlowServicePrincipal | **Organization**（可建立） |

**結果**：人類使用者無法直接建立 Project Registry 記錄，必須透過 Flow。

### 驗證 Record Owner 設定

**驗證測試**：

```
**本章可執行之測試**（驗證安全角色限制）：
1. 使用 System Architect 帳號登入 Power Apps
2. 嘗試直接在 Project Registry 資料表新增記錄
3. 預期結果：操作失敗，顯示「存取被拒」或按鈕不存在

**待第 05 章完成後執行之測試**（驗證 Flow Owner 設定）：
> 以下測試需於第 05 章 Flow 建立並第 04 章 Power Apps 建立後執行。
4. 透過 Power Apps Form 提交專案建立請求
5. GOV-001 Flow 執行完成後，查詢新建立的記錄
6. 檢查 Owner 欄位
預期結果：Owner 顯示為 GOV-FlowServicePrincipal
```

---

## Dataverse 資料表建立

### 建立資料表的操作步驟

**導航路徑**：
1. 開啟瀏覽器，前往：https://make.powerapps.com
2. 右上角確認已選擇正確環境（如 GOV-PROD）
3. 左側選單 → **Tables**
4. 點擊 **+ New table** → **New table (advanced)**

**每個資料表建立步驟**：
1. 填寫基本資訊（Display name, Schema name, Primary column）
2. 展開 Advanced options，啟用 Auditing
3. 點擊 Save，等待資料表建立完成
4. 選擇 Columns 標籤，逐一新增欄位
5. 設定資料表關聯

---

### gov_projectregistry（專案主檔）

#### 資料表設定

**操作步驟**：
1. Tables → + New table (advanced)
2. 填寫以下設定：

| 設定欄位 | 填寫值 |
|:--------------------------------|:------------------------------------------------------|
| Display name | `Project Registry` |
| Plural name | `Project Registries` |
| Schema name | `gov_projectregistry`（確認前綴為 gov_） |
| Primary column - Display name | `RequestID` |
| Primary column - Schema name | `gov_requestid` |

3. 展開 **Advanced options**：

| 設定欄位 | 填寫值 |
|:--------------------------------|:------------------------------------------------------|
| Schema name | `gov_projectregistry` |
| Type | Standard |
| Record ownership | **User or team** |
| ✓ Enable attachments | 勾選 |
| ✓ Track changes | 勾選 |
| ✓ Enable auditing | 勾選 |

4. 點擊 **Save**

#### 欄位定義

**操作步驟**：對每個欄位執行
1. 選擇 Columns 標籤
2. 點擊 **+ New column**
3. 填寫欄位設定
4. 點擊 **Save**

| 欄位顯示名稱 | Schema Name | 資料類型 | 格式/設定 | 必填 | Flow-only |
|:-----------------------------|:-------------------------------|:---------------------|:------------------------|:---:|:---------:|
| RequestID | gov_requestid | Single line of text | Max: 20 | Yes | Yes |
| Title | gov_title | Single line of text | Max: 200 | Yes | No |
| Project Type | gov_projecttype | Choice | gov_projecttype | Yes | No |
| Target SL | gov_targetsl | Choice | gov_targetsl | Yes | No |
| System Architect | gov_systemarchitect | Lookup | User table | Yes | No |
| Project Manager | gov_projectmanager | Lookup | User table | No | No |
| Project Description | gov_projectdescription | Multiple lines of text | Max: 2000 | No | No |
| Current Gate | gov_currentgate | Choice | gov_currentgate | Yes | **Yes** |
| Request Status | gov_requeststatus | Choice | gov_requeststatus | Yes | **Yes** |
| Project Status | gov_projectstatus | Choice | gov_projectstatus | Yes | **Yes** |
| Requested Gate | gov_requestedgate | Choice | gov_currentgate | No | **Yes** |
| Document Freeze Status | gov_documentfreezestatus | Choice | gov_documentfreezestatus | Yes | **Yes** |
| Document Freeze Date | gov_documentfreezedate | Date and Time | Date and time | No | **Yes** |
| Gate 0 Passed Date | gov_gate0passeddate | Date and Time | Date and time | No | **Yes** |
| Gate 1 Passed Date | gov_gate1passeddate | Date and Time | Date and time | No | **Yes** |
| Gate 2 Passed Date | gov_gate2passeddate | Date and Time | Date and time | No | **Yes** |
| Gate 3 Passed Date | gov_gate3passeddate | Date and Time | Date and time | No | **Yes** |
| Risk Acceptance Status | gov_riskacceptancestatus | Choice | gov_riskacceptancestatus | No | **Yes** |
| Risk Acceptance Date | gov_riskacceptancedate | Date and Time | Date and time | No | **Yes** |
| Risk Owner | gov_riskowner | Lookup | User table | No | **Yes** |
| Executive Approver | gov_executiveapprover | Lookup | User table | No | **Yes** |
| Highest Residual Risk Level | gov_highestresidualrisklevel | Choice | gov_risklevel | No | **Yes** |
| Rework Count | gov_reworkcount | Whole number | Min: 0, Max: 100 | No | **Yes** |
| Last Rework Date | gov_lastreworkdate | Date and Time | Date and time | No | **Yes** |
| Technical Feasibility Link | gov_technicalfeasibilitylink | URL | Max: 500 | No | No |
| Initial Risk List Link | gov_initialrisklistlink | URL | Max: 500 | No | No |
| Risk Assessment Strategy Link | gov_riskassessmentstrategylink | URL | Max: 500 | No | No |
| Design Baseline Link | gov_designbaselinelink | URL | Max: 500 | No | No |
| Risk Assessment Link | gov_riskassessmentlink | URL | Max: 500 | No | No |
| IEC 62443 Checklist Link | gov_iec62443checklistlink | URL | Max: 500 | No | No |
| Threat Model Link | gov_threatmodellink | URL | Max: 500 | No | No |
| Test Plan Link | gov_testplanlink | URL | Max: 500 | No | No |
| Test Report Link | gov_testreportlink | URL | Max: 500 | No | No |
| Handover Meeting Link | gov_handovermeetinglink | URL | Max: 500 | No | No |
| Residual Risk List Link | gov_residualrisklistlink | URL | Max: 500 | No | No |
| Requirement Traceability Link | gov_requirementtraceabilitylink | URL | Max: 500 | No | No |
| Design Object Inventory Link | gov_designobjectinventorylink | URL | Max: 500 | No | No |
| Document Register Link | gov_documentregisterlink | URL | Max: 500 | No | No |
| Change Impact Link | gov_changeimpactlink | URL | Max: 500 | No | No |
| SharePoint Folder URL | gov_sharepointfolderurl | URL | Max: 500 | No | **Yes** |
| Rework Reason Category | gov_reworkreasoncategory | Choice | gov_reworkreasoncategory | No | **Yes** |

**建立 Choice 欄位的操作步驟**（以 Current Gate 為例）：
1. + New column
2. Display name: `Current Gate`
3. Data type: **Choice**
4. 在 Sync this choice with 選擇 **gov_currentgate**（全域選項集，將在第 5 章建立）
5. Required: **Business required**
6. 展開 Advanced options
7. Schema name: `gov_currentgate`
8. 點擊 Save

**建立 Lookup 欄位的操作步驟**（以 System Architect 為例）：
1. + New column
2. Display name: `System Architect`
3. Data type: **Lookup**
4. Related table: 搜尋並選擇 **User**
5. Required: **Business required**
6. 展開 Advanced options
7. Schema name: `gov_systemarchitect`
8. 點擊 Save

---

### gov_reviewdecisionlog（審批決策記錄）

#### 資料表設定

| 設定欄位 | 填寫值 |
|:--------------------------------|:------------------------------------------------------|
| Display name | `Review Decision Log` |
| Plural name | `Review Decision Logs` |
| Schema name | `gov_reviewdecisionlog` |
| Primary column - Display name | `ReviewID` |
| Primary column - Schema name | `gov_reviewid` |
| Type | Standard |
| ✓ Enable auditing | 勾選 |

#### 欄位定義

| 欄位顯示名稱 | Schema Name | 資料類型 | 必填 | Flow-only |
|:------------------------------|:------------------------------|:--------------------------|:---:|:---------------------------|
| ReviewID | gov_reviewid | Single line of text (50) | Yes | Yes |
| Review Type | gov_reviewtype | Choice (gov_reviewtype) | Yes | **Yes** |
| Parent Project | gov_parentproject | Lookup (gov_projectregistry) | Yes | **Yes** |
| Submitted By | gov_submittedby | Lookup (User) | Yes | **Yes** |
| Submitted Date | gov_submitteddate | Date and Time | Yes | **Yes** |
| Approved By | gov_approvedby | Lookup (User) | No | **Yes** |
| Decision | gov_decision | Choice (gov_decision) | Yes | **Yes** |
| Requested Gate | gov_requestedgate | Choice (gov_currentgate) | No | **Yes** |
| Comments | gov_comments | Multiple lines of text (4000) | No | **No**（唯一允許人類填寫） |
| Reviewed Date | gov_revieweddate | Date and Time | No | **Yes** |
| Trigger Flow Run ID | gov_triggerflowrunid | Single line of text (100) | No | **Yes** |
| Gate 1 Security Review Status | gov_gate1securityreviewstatus | Choice (gov_layerreviewstatus) | No | **Yes** |
| Gate 1 Security Reviewer | gov_gate1securityreviewer | Lookup (User) | No | **Yes** |
| Gate 1 Security Review Date | gov_gate1securityreviewdate | Date and Time | No | **Yes** |
| Gate 1 Security Comments | gov_gate1securitycomments | Multiple lines of text (2000) | No | No |
| Gate 1 QA Review Status | gov_gate1qareviewstatus | Choice (gov_layerreviewstatus) | No | **Yes** |
| Gate 1 QA Reviewer | gov_gate1qareviewer | Lookup (User) | No | **Yes** |
| Gate 1 QA Review Date | gov_gate1qareviewdate | Date and Time | No | **Yes** |
| Gate 1 QA Comments | gov_gate1qacomments | Multiple lines of text (2000) | No | No |
| Gate 1 Governance Review Status | gov_gate1governancereviewstatus | Choice (gov_layerreviewstatus) | No | **Yes** |
| Gate 1 Governance Reviewer | gov_gate1governancereviewer | Lookup (User) | No | **Yes** |
| Gate 1 Governance Review Date | gov_gate1governancereviewdate | Date and Time | No | **Yes** |
| Gate 1 Governance Comments | gov_gate1governancecomments | Multiple lines of text (2000) | No | No |
| Gate 3 Risk Acceptance Status | gov_gate3riskacceptancestatus | Choice (gov_layerreviewstatus) | No | **Yes** |
| Gate 3 Approval Status | gov_gate3approvalstatus | Choice (gov_layerreviewstatus) | No | **Yes** |
| Risk Owner Review Status | gov_riskownerreviewstatus | Choice (gov_layerreviewstatus) | No | **Yes** |
| Executive Review Status | gov_executivereviewstatus | Choice (gov_layerreviewstatus) | No | **Yes** |
| Rejection Reasons | gov_rejectionreasons | Multiple lines of text (2000) | No | **Yes** |
| Rejected By | gov_rejectedby | Lookup (User) | No | **Yes** |
| SL Decision Level | gov_sldecisionlevel | Choice（gov_sldecisionlevel） | No | **Yes** |
| SL Approved By | gov_slapprovedby | Lookup (User) | No | **Yes** |
| SL Approved Note | gov_slapprovednote | Multiple lines of text (2000) | No | No |

---

### gov_riskassessmenttable（風險評估表）

#### 資料表設定

| 設定欄位 | 填寫值 |
|:--------------------------------|:------------------------------------------------------|
| Display name | `Risk Assessment Table` |
| Plural name | `Risk Assessments` |
| Schema name | `gov_riskassessmenttable` |
| Primary column - Display name | `RiskID` |
| Primary column - Schema name | `gov_riskid` |

#### 欄位定義

| 欄位顯示名稱 | Schema Name | 資料類型 | 必填 | Flow-only |
|:------------------------------|:------------------------------|:--------------------------|:---:|:---------------------------|
| RiskID | gov_riskid | Single line of text (30) | Yes | Yes |
| Parent Project | gov_parentproject | Lookup (gov_projectregistry) | Yes | **Yes** |
| Risk Description | gov_riskdescription | Multiple lines of text (4000) | Yes | No |
| Risk Category | gov_riskcategory | Choice (gov_riskcategory) | No | No |
| Likelihood | gov_likelihood | Choice (gov_likelihood) | No | No |
| Impact | gov_impact | Choice (gov_impact) | No | No |
| Risk Level | gov_risklevel | Choice (gov_risklevel) | Yes | **Yes** |
| Mitigation Plan | gov_mitigationplan | Multiple lines of text (4000) | No | No |
| Mitigation Status | gov_mitigationstatus | Choice (gov_mitigationstatus) | No | No |
| Residual Risk Level | gov_residualrisklevel | Choice (gov_risklevel) | No | **Yes** |
| Risk Acceptance Status | gov_riskacceptancestatus | Choice (gov_riskacceptancestatus) | Yes | **Yes** |
| Risk Accepted By | gov_riskacceptedby | Lookup (User) | No | **Yes** |
| Risk Acceptance Date | gov_riskacceptancedate | Date and Time | No | **Yes** |
| Initial Assessment Date | gov_initialassessmentdate | Date and Time | Yes | **Yes** |
| Initial Assessed By | gov_initialassessedby | Lookup (User) | Yes | **Yes** |
| Last Reassessment Date | gov_lastreassessmentdate | Date and Time | No | **Yes** |
| Reassessed By | gov_reassessedby | Lookup (User) | No | **Yes** |
| Reassessment Count | gov_reassessmentcount | Whole number | No | **Yes** |
| Risk Status | gov_riskstatus | Choice (gov_riskstatus) | Yes | **Yes** |
| Comments | gov_comments | Multiple lines of text (2000) | No | No |

---

### gov_exceptionwaiverlog（例外豁免記錄）

#### 資料表設定

| 設定欄位 | 填寫值 |
|:--------------------------------|:------------------------------------------------------|
| Display name | `Exception Waiver Log` |
| Schema name | `gov_exceptionwaiverlog` |
| Primary column - Display name | `WaiverID` |

#### 欄位定義

| 欄位顯示名稱 | Schema Name | 資料類型 | 必填 | Flow-only |
|:------------------------------|:------------------------------|:--------------------------|:---:|:---------------------------|
| WaiverID | gov_waiverid | Single line of text (30) | Yes | Yes |
| Parent Project | gov_parentproject | Lookup (gov_projectregistry) | Yes | **Yes** |
| Waiver Type | gov_waivertype | Choice (gov_waivertype) | Yes | No |
| Waiver Reason | gov_waiverreason | Multiple lines of text (4000) | Yes | No |
| Requested By | gov_requestedby | Lookup (User) | Yes | **Yes** |
| Requested Date | gov_requesteddate | Date and Time | Yes | **Yes** |
| Waiver Status | gov_waiverstatus | Choice (gov_waiverstatus) | Yes | **Yes** |
| Approval Status | gov_approvalstatus | Choice (gov_decision) | Yes | **Yes** |
| Approved By | gov_approvedby | Lookup (User) | No | **Yes** |
| Approved Date | gov_approveddate | Date and Time | No | **Yes** |
| Expiry Date | gov_expirydate | Date Only | No | No |
| Conditions | gov_conditions | Multiple lines of text (2000) | No | No |
| Related Risk | gov_relatedrisk | Lookup (gov_riskassessmenttable) | No | No |
| Comments | gov_comments | Multiple lines of text (2000) | No | No |

---

### gov_documentregister（文件清冊）

#### 資料表設定

| 設定欄位 | 填寫值 |
|:--------------------------------|:------------------------------------------------------|
| Display name | `Document Register` |
| Schema name | `gov_documentregister` |
| Primary column - Display name | `DocumentID` |

#### 欄位定義

| 欄位顯示名稱 | Schema Name | 資料類型 | 必填 | Flow-only |
|:------------------------------|:------------------------------|:--------------------------|:---:|:---------------------------|
| DocumentID | gov_documentid | Single line of text (100) | Yes | Yes |
| Parent Project | gov_parentproject | Lookup (gov_projectregistry) | Yes | **Yes** |
| Document Type | gov_documenttype | Choice (gov_documenttype) | Yes | No |
| Document Name | gov_documentname | Single line of text (255) | Yes | No |
| Document Version | gov_documentversion | Single line of text (20) | No | No |
| SharePoint File Link | gov_sharepointfilelink | URL (500) | Yes | **Yes** |
| Uploaded By | gov_uploadedby | Lookup (User) | Yes | **Yes** |
| Uploaded Date | gov_uploadeddate | Date and Time | Yes | **Yes** |
| Review Status | gov_reviewstatus | Choice (gov_documentreviewstatus) | No | **Yes** |
| Reviewed By | gov_reviewedby | Lookup (User) | No | **Yes** |
| Reviewed Date | gov_revieweddate | Date and Time | No | **Yes** |
| Required For Gate | gov_requiredforgate | Multiple lines of text (100) | No | No |
| File Size | gov_filesize | Whole number | No | **Yes** |
| Is Frozen | gov_isfrozen | Yes/No | No | **Yes** |
| Frozen Date | gov_frozendate | Date and Time | No | **Yes** |
| Comments | gov_comments | Multiple lines of text (1000) | No | No |
| Document Role | gov_documentrole | Choice (gov_documentrole) | Yes | **Yes** |
| Deliverable Package | gov_deliverablepackage | Choice (gov_deliverablepackage) | No | No |
| Superseded By | gov_supersededby | Lookup (gov_documentregister) | No | **Yes** |

> **gov_documentrole 說明**：標記文件目前在版本生命週期中的狀態。GOV-001 建立基線時設為 `Planned`；GOV-005 上傳時設為 `Draft`；Gate 審批通過後由 Flow 設為 `Approved`；新版本上傳時，舊版本由 Flow 設為 `Superseded`。`Frozen` 僅在 Gate 3 通過後由文件凍結 Flow 設定。
>
> **gov_supersededby 說明**：當一份文件被新版本取代時，此欄位指向取代它的新版本 Document Register 記錄。形成版本鏈（Version Chain），可追溯任一文件的完整修訂歷程。

---

### gov_governanceviolationlog（治理違規記錄）

> **重要**：此資料表為治理系統的核心稽核資料表，記錄所有偵測到的違規行為。
> 與 SOP-04（Testing Runbook）與 SOP-05（Roles and Governance Boundaries）的監控流程直接銜接。

#### 資料表設定

| 設定欄位 | 填寫值 |
|:--------------------------------|:------------------------------------------------------|
| Display name | `Governance Violation Log` |
| Schema name | `gov_governanceviolationlog` |
| Primary column - Display name | `ViolationID` |
| Primary column - Schema name | `gov_violationid` |

#### 欄位定義

| 欄位顯示名稱 | Schema Name | 資料類型 | 必填 | Flow-only | 說明 |
|:------------------------------|:-------------------------------|:------------------------------|:----:|:----------|:------------------------|
| ViolationID | gov_violationid | Single line of text (30) | Yes | Yes | 違規事件唯一識別碼 |
| Violation Type | gov_violationtype | Choice (gov_violationtype) | Yes | **Yes** | 違規類型 |
| Violated Entity | gov_violatedentity | Choice (gov_violatedentity) | Yes | **Yes** | 違規的資料表 |
| Violated Field | gov_violatedfield | Single line of text (100) | Yes | **Yes** | 違規的欄位名稱 |
| Violated Record ID | gov_violatedrecordid | Single line of text (100) | Yes | **Yes** | 違規記錄的主鍵 |
| Parent Project | gov_parentproject | Lookup (gov_projectregistry) | No | **Yes** | 關聯專案（若適用） |
| Old Value | gov_oldvalue | Multiple lines of text (4000) | No | **Yes** | 修改前的值 |
| New Value | gov_newvalue | Multiple lines of text (4000) | No | **Yes** | 修改後的值 |
| Modified By | gov_modifiedby | Lookup (User) | Yes | **Yes** | 執行修改的身分 |
| Modified By Type | gov_modifiedbytype | Choice (gov_modifiedbytype) | Yes | **Yes** | 修改者類型（User/App/API） |
| Modified Date | gov_modifieddate | Date and Time | Yes | **Yes** | 修改發生時間 |
| Detected Date | gov_detecteddate | Date and Time | Yes | **Yes** | 違規偵測時間 |
| Detected By Flow | gov_detectedbyflow | Single line of text (50) | Yes | **Yes** | 偵測的 Flow 名稱 |
| Detection Method | gov_detectionmethod | Choice (gov_detectionmethod) | Yes | **Yes** | 偵測方法 |
| Violation Source | gov_violationsource | Choice (gov_violationsource) | Yes | **Yes** | 違規來源 |
| Client IP Address | gov_clientipaddress | Single line of text (50) | No | **Yes** | 來源 IP |
| User Agent | gov_useragent | Single line of text (500) | No | **Yes** | 瀏覽器/API 用戶端資訊 |
| Rollback Status | gov_rollbackstatus | Choice (gov_rollbackstatus) | Yes | **Yes** | 回滾狀態 |
| Rollback Date | gov_rollbackdate | Date and Time | No | **Yes** | 回滾執行時間 |
| Rollback By | gov_rollbackby | Single line of text (100) | No | **Yes** | 執行回滾的 Flow |
| Severity | gov_severity | Choice (gov_severity) | Yes | **Yes** | 嚴重程度 |
| Resolution Status | gov_resolutionstatus | Choice (gov_resolutionstatus) | Yes | **Yes** | 處理狀態 |
| Resolution Notes | gov_resolutionnotes | Multiple lines of text (4000) | No | No | 處理說明 |
| Resolved By | gov_resolvedby | Lookup (User) | No | **Yes** | 處理者 |
| Resolved Date | gov_resolveddate | Date and Time | No | **Yes** | 處理時間 |
| SOP Reference | gov_sopreference | Single line of text (50) | No | **Yes** | 相關 SOP 編號 |
| Notification Sent | gov_notificationsent | Yes/No | Yes | **Yes** | 通知是否已發送 |
| Notification Recipients | gov_notificationrecipients | Multiple lines of text (500) | No | **Yes** | 通知收件人清單 |

---

### gov_bomregistry（物料清單）

> **重要**：此資料表記錄專案之 Commercial BOM (CBOM) 與 Engineering BOM (EBOM)，
> 支援 BOM 分層語義治理。

#### 資料表設定

| 設定欄位 | 填寫值 |
|:--------------------------------|:------------------------------------------------------|
| Display name | `BOM Registry` |
| Plural name | `BOM Registries` |
| Schema name | `gov_bomregistry` |
| Primary column - Display name | `BOMID` |
| Primary column - Schema name | `gov_bomid` |
| Type | Standard |
| ✓ Enable auditing | 勾選 |

#### 欄位定義

| 欄位顯示名稱 | Schema Name | 資料類型 | 必填 | Flow-only | 說明 |
|:------------------------------|:-------------------------------|:------------------------------|:----:|:----------|:------------------------|
| BOMID | gov_bomid | Single line of text (30) | Yes | Yes | BOM 唯一識別碼 |
| Parent Project | gov_parentproject | Lookup (gov_projectregistry) | Yes | **Yes** | 關聯專案 |
| BOM Type | gov_bomtype | Choice (gov_bomtype) | Yes | **Yes** | BOM 類型（CBOM/EBOM） |
| BOM Binding Scope | gov_bombindingscope | Choice (gov_bombindingscope) | Yes | **Yes** | 拘束範圍（商務/工程基線） |
| BOM Owner Role | gov_bomownerrole | Choice (gov_bomownerrole) | Yes | **Yes** | 當責角色（Presales/System Architect） |
| BOM Status | gov_bomstatus | Choice (gov_bomstatus) | Yes | **Yes** | BOM 狀態 |
| Linkage Gate | gov_linkagegate | Choice (gov_currentgate) | Yes | **Yes** | 關聯 Gate |
| BOM Version | gov_bomversion | Single line of text (20) | Yes | No | 版本號 |
| BOM Name | gov_bomname | Single line of text (255) | Yes | No | BOM 名稱 |
| BOM Description | gov_bomdescription | Multiple lines of text (2000) | No | No | BOM 說明 |
| Document Link | gov_documentlink | URL (500) | No | **Yes** | SharePoint 文件連結 |
| Created By | gov_createdby | Lookup (User) | Yes | **Yes** | 建立者 |
| Created Date | gov_createddate | Date and Time | Yes | **Yes** | 建立日期 |
| Quoted Date | gov_quoteddate | Date and Time | No | **Yes** | 報價使用日期（CBOM） |
| Quoted Version Snapshot | gov_quotedversionsnapshot | Single line of text (20) | No | **Yes** | 報價時版本快照（CBOM） |
| Gate0 Approved Date | gov_gate0approveddate | Date and Time | No | **Yes** | Gate 0 核准日期（CBOM） |
| Baseline Date | gov_baselinedate | Date and Time | No | **Yes** | 基線建立日期（EBOM） |
| Frozen Date | gov_frozendate | Date and Time | No | **Yes** | 凍結日期（EBOM） |
| Source CBOM | gov_sourcecbom | Lookup (gov_bomregistry) | No | **Yes** | 來源 CBOM（EBOM 追溯用） |
| CBOM EBOM Variance | gov_cbomebomvariance | Yes/No | No | **Yes** | 是否存在 CBOM-EBOM 差異 |
| Variance Description | gov_variancedescription | Multiple lines of text (4000) | No | No | 差異說明 |
| Variance Notified Date | gov_variancenotifieddate | Date and Time | No | **Yes** | 差異通知日期 |
| Last Modified Date | gov_lastmodifieddate | Date and Time | No | **Yes** | 最後修改日期 |
| Last Modified By | gov_lastmodifiedby | Lookup (User) | No | **Yes** | 最後修改者 |
| Comments | gov_comments | Multiple lines of text (2000) | No | No | 備註 |

#### BOM Type 說明

| BOM Type | 說明 | 適用階段 | 當責角色 |
|:-----------------|:------------------------------|:------------------------|:------------------------|
| CBOM | Commercial BOM - 商務報價用 | Pre-Gate 0 至 Gate 0 | Pre-Gate Design Support |
| EBOM | Engineering BOM - 設計基線用 | Gate 1 之後 | System Architect |

#### BOM Status 流轉

**CBOM 狀態流轉**：

```
Draft → Quoted → Gate0 Approved
  │        │           │
  │        │           └─ Gate 0 核准定版
  │        └─ 已用於報價，版本須保留
  └─ 初稿，可自由修改
```

**EBOM 狀態流轉**：

```
Draft → Baseline → Frozen
  │         │         │
  │         │         └─ Gate 3 前凍結，變更須經 Gate 2
  │         └─ Gate 1 核准，納入設計基線
  └─ System Architect 編製中
```

---

### gov_sahandoverevent（SA 交接事件）

> **說明**：此資料表記錄 System Architect 交接事件，支援 SA 變更時的治理追溯。

#### 資料表設定

| 設定欄位 | 填寫值 |
|:--------------------------------|:------------------------------------------------------|
| Display name | `SA Handover Event` |
| Plural name | `SA Handover Events` |
| Schema name | `gov_sahandoverevent` |
| Primary column - Display name | `HandoverID` |
| Primary column - Schema name | `gov_handoverid` |
| Type | Standard |
| ✓ Enable auditing | 勾選 |

#### 欄位定義

| 欄位顯示名稱 | Schema Name | 資料類型 | 必填 | Flow-only | 說明 |
|:------------------------------|:-------------------------------|:------------------------------|:----:|:----------|:------------------------|
| HandoverID | gov_handoverid | Single line of text (30) | Yes | Yes | 交接事件唯一識別碼 |
| Parent Project | gov_parentproject | Lookup (gov_projectregistry) | Yes | **Yes** | 關聯專案 |
| Original SA | gov_originalsa | Lookup (User) | Yes | **Yes** | 原系統架構師 |
| New SA | gov_newsa | Lookup (User) | Yes | **Yes** | 新系統架構師 |
| Handover Reason | gov_handoverreason | Multiple lines of text (2000) | Yes | No | 交接原因 |
| Handover Status | gov_handoverstatus | Choice (gov_handoverstatus) | Yes | **Yes** | 交接狀態 |
| Requested Date | gov_requesteddate | Date and Time | Yes | **Yes** | 申請日期 |
| Accepted Date | gov_accepteddate | Date and Time | No | **Yes** | 接受日期 |
| Comments | gov_comments | Multiple lines of text (2000) | No | No | 備註 |

#### gov_handoverstatus（交接狀態）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | Pending | 待接受 |
| 807660001 | Accepted | 已接受 |
| 807660002 | Rejected | 已拒絕 |
| 807660003 | Completed | 已完成 |

---

### gov_counterlist（流水號產生器）

#### 資料表設定

| 設定欄位 | 填寫值 |
|:--------------------------------|:------------------------------------------------------|
| Display name | `Counter List` |
| Schema name | `gov_counterlist` |
| Primary column - Display name | `CounterName` |

#### 欄位定義

| 欄位顯示名稱 | Schema Name | 資料類型 | 必填 | Flow-only |
|:------------------------------|:------------------------------|:--------------------------|:---:|:---------------------------|
| CounterName | gov_countername | Single line of text (50) | Yes | No |
| Current Year | gov_currentyear | Whole number | Yes | **Yes** |
| Current Counter | gov_currentcounter | Whole number | Yes | **Yes** |
| Prefix | gov_prefix | Single line of text (10) | Yes | No |
| Last Updated | gov_lastupdated | Date and Time | Yes | **Yes** |
| Last Updated By | gov_lastupdatedby | Lookup (User) | No | **Yes** |

---

### gov_standardfeedback（標準回饋記錄）

> **說明**：此資料表記錄部門標準執行過程中的回饋，包含無法執行、標準衝突與改善建議。
> 作為 KPI 證據採集的核心事件表之一。

#### 資料表設定

| 設定欄位 | 填寫值 |
|:--------------------------------|:------------------------------------------------------|
| Display name | `Standard Feedback` |
| Plural name | `Standard Feedbacks` |
| Schema name | `gov_standardfeedback` |
| Primary column - Display name | `FeedbackID` |
| Primary column - Schema name | `gov_feedbackid` |
| Type | Standard |
| ✓ Enable auditing | 勾選 |

#### 欄位定義

| 欄位顯示名稱 | Schema Name | 資料類型 | 必填 | Flow-only | 說明 |
|:------------------------------|:-------------------------------|:------------------------------|:----:|:----------|:------------------------|
| FeedbackID | gov_feedbackid | Single line of text (30) | Yes | Yes | 主欄位，Counter 自動產生（前綴 FB） |
| Standard ID | gov_standardid | Single line of text (100) | Yes | No | 被回報標準的識別碼 |
| Feedback Type | gov_feedbacktype | Choice（gov_feedbacktype） | Yes | No | 回饋類型 |
| Reported By | gov_reportedby | Lookup (User) | Yes | **Yes** | 系統填入提報人 |
| Reported Date | gov_reporteddate | Date and Time | Yes | **Yes** | 系統時戳 |
| Resolution Status | gov_feedbackresolutionstatus | Choice（gov_feedbackresolutionstatus） | Yes | **Yes** | 初始值 Open (807660000) |
| Resolution Date | gov_resolutiondate | Date and Time | No | **Yes** | 解決日期 |
| Resolution Notes | gov_resolutionnotes | Multiple lines of text (4000) | No | No | 解決說明 |
| Related Standard | gov_relatedstandard | Single line of text (200) | No | No | 標準名稱參考 |
| Description | gov_description | Multiple lines of text (4000) | Yes | No | 回饋詳細內容 |
| Related Project | gov_parentproject | Lookup (gov_projectregistry) | No | No | 選填，若回饋與特定專案相關 |

---

### gov_disputelog（爭議記錄）

> **說明**：此資料表記錄跨部門爭議的提報、仲裁與解決過程，
> 支援 Level 2（部門級仲裁）與 Level 3（跨部門級裁決）的爭議管理。

#### 資料表設定

| 設定欄位 | 填寫值 |
|:--------------------------------|:------------------------------------------------------|
| Display name | `Dispute Log` |
| Plural name | `Dispute Logs` |
| Schema name | `gov_disputelog` |
| Primary column - Display name | `DisputeID` |
| Primary column - Schema name | `gov_disputeid` |
| Type | Standard |
| ✓ Enable auditing | 勾選 |

#### 欄位定義

| 欄位顯示名稱 | Schema Name | 資料類型 | 必填 | Flow-only | 說明 |
|:------------------------------|:-------------------------------|:------------------------------|:----:|:----------|:------------------------|
| DisputeID | gov_disputeid | Single line of text (30) | Yes | Yes | 主欄位，Counter 自動產生（前綴 DSP） |
| Dispute Level | gov_disputelevel | Choice（gov_disputelevel） | Yes | No | 爭議層級 |
| Raised By | gov_raisedby | Lookup (User) | Yes | **Yes** | 提報人 |
| Raised Date | gov_raiseddate | Date and Time | Yes | **Yes** | 提報日期 |
| Assigned Mediator | gov_assignedmediator | Lookup (User) | No | **Yes** | 指派仲裁人 |
| Mediation Date | gov_mediationdate | Date and Time | No | **Yes** | 調解日期 |
| Resolution Date | gov_disputeresolutiondate | Date and Time | No | **Yes** | 解決日期 |
| Closed Date | gov_closeddate | Date and Time | No | **Yes** | 結案日期 |
| Resolution Result | gov_disputeresolutionresult | Choice（gov_disputeresolutionresult） | No | **Yes** | 爭議解決結果 |
| Description | gov_description | Multiple lines of text (4000) | Yes | No | 爭議說明 |
| Related Project | gov_parentproject | Lookup (gov_projectregistry) | Yes | No | 關聯專案 |

---

### gov_actionitem（行動項目）

> **說明**：此資料表追蹤 Gate 審查後產生的行動項目，
> 每個行動項目關聯至特定的審查記錄，確保審查結論可追蹤。

#### 資料表設定

| 設定欄位 | 填寫值 |
|:--------------------------------|:------------------------------------------------------|
| Display name | `Action Item` |
| Plural name | `Action Items` |
| Schema name | `gov_actionitem` |
| Primary column - Display name | `ActionItemID` |
| Primary column - Schema name | `gov_actionitemid` |
| Type | Standard |
| ✓ Enable auditing | 勾選 |

#### 欄位定義

| 欄位顯示名稱 | Schema Name | 資料類型 | 必填 | Flow-only | 說明 |
|:------------------------------|:-------------------------------|:------------------------------|:----:|:----------|:------------------------|
| ActionItemID | gov_actionitemid | Single line of text (30) | Yes | Yes | 主欄位，Counter 自動產生（前綴 ACT） |
| Related Gate Review | gov_relatedgatereview | Lookup (gov_reviewdecisionlog) | Yes | **Yes** | 所屬 Gate 審查記錄 |
| Description | gov_description | Multiple lines of text (4000) | Yes | No | 待辦描述 |
| Assigned To | gov_assignedto | Lookup (User) | Yes | No | 負責人 |
| Due Date | gov_duedate | Date and Time | Yes | No | 截止日 |
| Completion Date | gov_completiondate | Date and Time | No | **Yes** | 完成日期 |
| Status | gov_actionitemstatus | Choice（gov_actionitemstatus） | Yes | **Yes** | 初始值 Open (807660000) |
| Related Project | gov_parentproject | Lookup (gov_projectregistry) | Yes | No | 關聯專案 |

---

### gov_standardsregistry（部門標準登錄冊）

> **說明**：此資料表維護部門標準清冊，記錄每份標準的擁有角色、審查週期與版本資訊。
> 作為治理基礎參考資料，由管理員初始建立，後續由 GovLead 維護。

#### 資料表設定

| 設定欄位 | 填寫值 |
|:--------------------------------|:------------------------------------------------------|
| Display name | `Standards Registry` |
| Plural name | `Standards Registries` |
| Schema name | `gov_standardsregistry` |
| Primary column - Display name | `StandardID` |
| Primary column - Schema name | `gov_standardregistryid` |
| Type | Standard |
| ✓ Enable auditing | 勾選 |

#### 欄位定義

| 欄位顯示名稱 | Schema Name | 資料類型 | 必填 | Flow-only | 說明 |
|:------------------------------|:-------------------------------|:------------------------------|:----:|:----------|:------------------------|
| StandardID | gov_standardregistryid | Single line of text (30) | Yes | No | 主欄位，手動填入 |
| Standard Name | gov_standardname | Single line of text (200) | Yes | No | 標準名稱 |
| Document Category | gov_documentcategory | Choice（gov_documentcategory） | Yes | No | 文件分類 |
| Owner Role | gov_ownerrole | Single line of text (100) | Yes | No | 擁有角色 |
| Review Cycle | gov_reviewcycle | Choice（gov_reviewcycle） | Yes | No | 審查週期 |
| Last Review Date | gov_lastreviewdate | Date and Time | No | No | 上次審查日期 |
| Next Review Date | gov_nextreviewdate | Date and Time | No | No | 下次審查日期 |
| Current Version | gov_currentversion | Single line of text (20) | No | No | 目前版本 |
| Status | gov_standardstatus | Choice（gov_standardstatus） | Yes | No | 標準狀態 |
| SharePoint Link | gov_sharepointlink | URL (500) | No | No | 文件連結 |

---

### gov_processlog（流程提醒日誌）

> **說明**：此資料表記錄治理流程中所有自動提醒的發送記錄，
> 包含 Gate 截止提醒、文件審查提醒、風險重評估提醒等。

#### 資料表設定

| 設定欄位 | 填寫值 |
|:--------------------------------|:------------------------------------------------------|
| Display name | `Process Log` |
| Plural name | `Process Logs` |
| Schema name | `gov_processlog` |
| Primary column - Display name | `LogID` |
| Primary column - Schema name | `gov_processlogid` |
| Type | Standard |
| ✓ Enable auditing | 勾選 |

#### 欄位定義

| 欄位顯示名稱 | Schema Name | 資料類型 | 必填 | Flow-only | 說明 |
|:------------------------------|:-------------------------------|:------------------------------|:----:|:----------|:------------------------|
| LogID | gov_processlogid | Single line of text (30) | Yes | **Yes** | 主欄位，Counter 自動產生（前綴 PLG） |
| Reminder Type | gov_remindertype | Choice（gov_remindertype） | Yes | **Yes** | 提醒類型 |
| Scheduled Time | gov_scheduledtime | Date and Time | Yes | **Yes** | 排定發送時間 |
| Actual Sent Time | gov_actualsenttime | Date and Time | No | **Yes** | 實際發送時間 |
| Recipient | gov_recipient | Single line of text (200) | Yes | **Yes** | 收件人 Email |
| Status | gov_processlogstatus | Choice（gov_processlogstatus） | Yes | **Yes** | 發送狀態 |
| Related Project | gov_parentproject | Lookup (gov_projectregistry) | No | **Yes** | 關聯專案 |
| Triggered By Flow | gov_triggeredbyflow | Single line of text (100) | No | **Yes** | 觸發 Flow 名稱 |

---

### gov_externalunit（外部單位登錄）

> **說明**：此資料表登錄專案涉及的外部單位，記錄介面類型與評估狀態。
> 作為治理基礎參考資料，由管理員初始建立，後續由 GovLead 維護。

#### 資料表設定

| 設定欄位 | 填寫值 |
|:--------------------------------|:------------------------------------------------------|
| Display name | `External Unit` |
| Plural name | `External Units` |
| Schema name | `gov_externalunit` |
| Primary column - Display name | `UnitID` |
| Primary column - Schema name | `gov_externalunitid` |
| Type | Standard |
| ✓ Enable auditing | 勾選 |

#### 欄位定義

| 欄位顯示名稱 | Schema Name | 資料類型 | 必填 | Flow-only | 說明 |
|:------------------------------|:-------------------------------|:------------------------------|:----:|:----------|:------------------------|
| UnitID | gov_externalunitid | Single line of text (30) | Yes | No | 主欄位，手動填入 |
| Unit Name | gov_unitname | Single line of text (200) | Yes | No | 單位名稱 |
| Interface Type | gov_interfacetype | Choice（gov_interfacetype） | Yes | No | 介面類型 |
| Assessment Status | gov_assessmentstatus | Choice（gov_assessmentstatus） | Yes | No | 評估狀態 |
| Assessment Date | gov_assessmentdate | Date and Time | No | No | 評估日期 |
| Assessor | gov_assessor | Lookup (User) | No | No | 評估人員 |
| Notes | gov_notes | Multiple lines of text (4000) | No | No | 備註 |

---

### gov_srcompliancesummary（SR 合規摘要）

> **說明**：此資料表記錄每個專案的系統需求（SR）合規狀態，
> 作為評估基礎資料，追蹤各 SR 項目的實施情況與證據連結。

#### 資料表設定

| 設定欄位 | 填寫值 |
|:--------------------------------|:------------------------------------------------------|
| Display name | `SR Compliance Summary` |
| Plural name | `SR Compliance Summaries` |
| Schema name | `gov_srcompliancesummary` |
| Primary column - Display name | `SRID` |
| Primary column - Schema name | `gov_srcomplianceid` |
| Type | Standard |
| ✓ Enable auditing | 勾選 |

#### 欄位定義

| 欄位顯示名稱 | Schema Name | 資料類型 | 必填 | Flow-only | 說明 |
|:------------------------------|:-------------------------------|:------------------------------|:----:|:----------|:------------------------|
| SRID | gov_srcomplianceid | Single line of text (30) | Yes | No | 主欄位，手動填入 |
| Parent Project | gov_parentproject | Lookup (gov_projectregistry) | Yes | No | 關聯專案 |
| SR Number | gov_srnumber | Single line of text (20) | Yes | No | SR 編號（如 SR-1.1） |
| Status | gov_srcompliancestatus | Choice（gov_srcompliancestatus） | Yes | No | 合規狀態 |
| Evidence Link | gov_evidencelink | URL (500) | No | No | 證據文件連結 |
| Review Date | gov_reviewdate | Date and Time | No | No | 審查日期 |

---

## 選項集（Choice Sets）定義

### 建立全域選項集的操作步驟

**操作路徑**：
1. Power Apps Maker Portal → **Solutions**
2. 找到或建立治理系統 Solution（若無，點擊 + New solution）
3. 開啟 Solution → **+ New** → **More** → **Choice**

**對每個選項集執行**：
1. 填寫 Display name 和 Schema name
2. 逐一新增選項（Label 和 Value）
3. 點擊 Save

### 選項集清單

#### gov_projecttype（專案類型）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | NewSystem | 全新系統開發 |
| 807660001 | MajorArchChange | 重大架構變更 |
| 807660002 | SecurityCritical | 安全關鍵變更 |
| 807660003 | ComplianceChange | 合規性變更 |

#### gov_targetsl（目標安全等級）

| Value | Label |
|:----------|:------------------------------|
| 807660000 | SL1 |
| 807660001 | SL2 |
| 807660002 | SL3 |
| 807660003 | SL4 |

#### gov_currentgate（當前 Gate）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | Pending | 尚未開始 |
| 807660001 | Gate0 | Gate 0 已通過 |
| 807660002 | Gate1 | Gate 1 已通過 |
| 807660003 | Gate2 | Gate 2 已通過 |
| 807660004 | Gate3 | Gate 3 已通過 |

#### gov_requeststatus（審批請求狀態）

| Value | Label |
|:----------|:------------------------------|
| 807660000 | None |
| 807660001 | Pending |
| 807660002 | UnderReview |
| 807660003 | Approved |
| 807660004 | Rejected |

#### gov_projectstatus（專案狀態）

| Value | Label |
|:----------|:------------------------------|
| 807660000 | Active |
| 807660001 | OnHold |
| 807660002 | Closed |
| 807660003 | Terminated |

#### gov_documentfreezestatus（文件凍結狀態）

| Value | Label |
|:----------|:------------------------------|
| 807660000 | NotFrozen |
| 807660001 | Frozen |

#### gov_decision（審批決策）

| Value | Label |
|:----------|:------------------------------|
| 807660000 | Pending |
| 807660001 | Approved |
| 807660002 | Rejected |
| 807660003 | Executed |

#### gov_reviewtype（審批類型）

| Value | Label |
|:----------|:------------------------------|
| 807660000 | ProjectCreation |
| 807660001 | Gate0Request |
| 807660002 | Gate1Request |
| 807660003 | Gate2Request |
| 807660004 | Gate3Request |
| 807660005 | RiskInitialAssessment |
| 807660006 | RiskReassessment |
| 807660007 | RiskAcceptance |
| 807660008 | DocumentFreeze |
| 807660009 | LiteToFullUpgrade |
| 807660010 | ExceptionWaiverRequest |
| 807660011 | ExceptionWaiverApproval |
| 807660012 | ProjectClosure |

#### gov_risklevel（風險等級）

| Value | Label |
|:----------|:------------------------------|
| 807660000 | Low |
| 807660001 | Medium |
| 807660002 | High |

#### gov_riskacceptancestatus（風險接受狀態）

| Value | Label |
|:----------|:------------------------------|
| 807660000 | Pending |
| 807660001 | Accepted |
| 807660002 | Rejected |
| 807660003 | NotRequired |

#### gov_riskcategory（風險類別）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | TechnicalRisk | 技術風險 |
| 807660001 | SecurityRisk | 安全風險 |
| 807660002 | ComplianceRisk | 合規風險 |
| 807660003 | OperationalRisk | 營運風險 |
| 807660004 | PerformanceRisk | 效能風險 |
| 807660005 | IntegrationRisk | 整合風險 |

#### gov_likelihood（可能性）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | VeryLow | 極低（發生機率 < 10%） |
| 807660001 | Low | 低（發生機率 10-30%） |
| 807660002 | Medium | 中（發生機率 30-60%） |
| 807660003 | High | 高（發生機率 60-85%） |
| 807660004 | VeryHigh | 極高（發生機率 > 85%） |

#### gov_impact（影響程度）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | Negligible | 可忽略（最小影響） |
| 807660001 | Minor | 輕微（小範圍影響） |
| 807660002 | Moderate | 中等（部分功能受影響） |
| 807660003 | Major | 重大（主要功能受影響） |
| 807660004 | Critical | 嚴重（系統無法運作） |

#### gov_mitigationstatus（緩解狀態）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | NotStarted | 尚未開始 |
| 807660001 | InProgress | 進行中 |
| 807660002 | Completed | 已完成 |
| 807660003 | Verified | 已驗證 |
| 807660004 | NotRequired | 不需要 |

#### gov_riskstatus（風險狀態）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | Open | 開放（風險尚未處理） |
| 807660001 | UnderReview | 審查中 |
| 807660002 | Mitigated | 已緩解 |
| 807660003 | Accepted | 已接受 |
| 807660004 | Closed | 已關閉 |

#### gov_layerreviewstatus（層級審批狀態）

| Value | Label |
|:----------|:------------------------------|
| 807660000 | Pending |
| 807660001 | Approved |
| 807660002 | Rejected |
| 807660003 | Skipped |

#### gov_documenttype（文件類型）

| Value | Label | 必要於 Gate |
|:----------|:------------------------------|:--------------|
| 807660000 | TechnicalFeasibility | Gate 0 |
| 807660001 | InitialRiskList | Gate 0 |
| 807660002 | RiskAssessmentStrategy | Gate 0 |
| 807660003 | DesignBaseline | Gate 1 |
| 807660004 | RiskAssessment | Gate 1 |
| 807660005 | IEC62443Checklist | Gate 1 |
| 807660006 | ThreatModel | Gate 1 |
| 807660007 | RequirementTraceability | Gate 1 |
| 807660008 | TestPlan | Gate 1 |
| 807660009 | TestReport | Gate 2, 3 |
| 807660010 | HandoverMeeting | Gate 3 |
| 807660011 | ResidualRiskList | Gate 3 |
| 807660012 | Other | - |
| 807660013 | DesignObjectInventory | Gate 1 |
| 807660014 | ChangeImpact | Gate 2 |
| 807660015 | DocumentRegister | - |

#### gov_documentreviewstatus（文件審查狀態）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | Pending | 待審查 |
| 807660001 | UnderReview | 審查中 |
| 807660002 | Approved | 已核准 |
| 807660003 | Rejected | 已拒絕 |
| 807660004 | RevisionRequired | 需修訂 |

#### gov_bomtype（BOM 類型）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | CBOM | Commercial BOM - 商務報價用 |
| 807660001 | EBOM | Engineering BOM - 設計基線用 |

#### gov_bombindingscope（BOM 拘束範圍）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | CommercialBindingOnly | 商務拘束（設計不拘束） |
| 807660001 | EngineeringBaseline | 工程基線（設計拘束） |

#### gov_bomownerrole（BOM 當責角色）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | PreGateDesignSupport | Pre-Gate Design Support / Presales |
| 807660001 | SystemArchitect | System Architect |

#### gov_bomstatus（BOM 狀態）

| Value | Label | 說明 | 適用類型 |
|:----------|:------------------------------|:----------------------------------------------|---------|
| 807660000 | Draft | 初稿，可自由修改 | CBOM, EBOM |
| 807660001 | Quoted | 已用於報價，版本須保留 | CBOM |
| 807660002 | Gate0Approved | Gate 0 核准定版 | CBOM |
| 807660003 | Baseline | 已納入設計基線 | EBOM |
| 807660004 | Frozen | 凍結，變更須經 Gate 2 | EBOM |

#### gov_documentrole（文件角色／版本狀態）

> **用途**：標記 Document Register 中每筆記錄在版本生命週期中的狀態。此為 Flow-only 欄位，僅由 GOV-001（基線播種）、GOV-005（上傳與版本推進）、Gate 審批 Flow 及文件凍結 Flow 寫入。

| Value | Label | 說明 | 設定時機 |
|:----------|:------------------------------|:----------------------------------------------|---------|
| 807660000 | Planned | 基線佔位——專案建立時由 GOV-001 自動產生 | GOV-001 Baseline Seeding |
| 807660001 | Draft | 已上傳但尚未通過審查 | GOV-005 Upload |
| 807660002 | Active | 目前有效的草稿（同一 DocumentType 僅一份 Active） | GOV-005 版本推進 |
| 807660003 | Superseded | 已被新版本取代 | GOV-005 版本推進（舊版自動標記） |
| 807660004 | Approved | 通過 Gate 審查核准 | Gate 審批 Flow |
| 807660005 | Frozen | Gate 3 通過後凍結，不可再修改 | 文件凍結 Flow |

#### gov_deliverablepackage（交付物包裝類型）

> **用途**：區分同一 DocumentType 下的不同交付物層級。搭配 Logical Document Key（ParentProject + DocumentType + DeliverablePackage + DocumentRole）實現唯一識別，避免 DocumentType 選項集無限膨脹。

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | CoreDeliverable | 核心交付物——Gate 檢查必要文件 |
| 807660001 | SupplementaryDeliverable | 補充交付物——非 Gate 必要但建議提供 |
| 807660002 | AdHoc | 臨時上傳——不綁定特定 Gate 需求 |

#### gov_waivertype（豁免類型）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | DocumentWaiver | 文件豁免 |
| 807660001 | TimelineWaiver | 時程豁免 |
| 807660002 | RequirementWaiver | 需求豁免 |
| 807660003 | ProcessWaiver | 流程豁免 |
| 807660004 | SecurityWaiver | 安全豁免 |

#### gov_waiverstatus（豁免狀態）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | Pending | 待審批 |
| 807660001 | Approved | 已核准 |
| 807660002 | Rejected | 已拒絕 |
| 807660003 | Expired | 已過期 |
| 807660004 | Revoked | 已撤銷 |

#### gov_violationtype（違規類型）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | UnauthorizedFieldModification | 未授權欄位修改（修改 Flow-only 欄位） |
| 807660001 | StateLogInconsistency | 狀態與記錄不一致 |
| 807660002 | DocumentLinkInvalid | 文件連結失效 |
| 807660003 | DocumentReviewTimeout | 文件審查超時 |
| 807660004 | BypassedApproval | 繞過審批流程 |
| 807660005 | UnauthorizedRecordCreation | 未授權建立記錄 |
| 807660006 | UnauthorizedRecordDeletion | 未授權刪除記錄 |
| 807660007 | DirectAPIAccess | 直接 API 存取 |

#### gov_violatedentity（違規 Entity）

| Value | Label |
|:----------|:------------------------------|
| 807660000 | ProjectRegistry |
| 807660001 | ReviewDecisionLog |
| 807660002 | RiskAssessmentTable |
| 807660003 | ExceptionWaiverLog |
| 807660004 | DocumentRegister |
| 807660005 | CounterList |
| 807660006 | BOMRegistry |
| 807660007 | StandardFeedback |
| 807660008 | DisputeLog |
| 807660009 | ActionItem |
| 807660010 | StandardsRegistry |
| 807660011 | ProcessLog |
| 807660012 | ExternalUnit |
| 807660013 | SRComplianceSummary |
| 807660014 | SAHandoverEvent |

#### gov_rollbackstatus（回滾狀態）

| Value | Label |
|:----------|:------------------------------|
| 807660000 | Completed |
| 807660001 | ManualRequired |
| 807660002 | Pending |
| 807660003 | NotApplicable |
| 807660004 | Failed |

#### gov_violationsource（違規來源）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | PowerAppsUI | 透過 Power Apps UI 直接修改 |
| 807660001 | DataverseAPI | 透過 Dataverse Web API |
| 807660002 | PowerAutomateFlow | 透過非授權 Flow |
| 807660003 | ExternalIntegration | 外部系統整合 |
| 807660004 | PostmanOrScript | Postman 或腳本 |
| 807660005 | ExcelImport | Excel 匯入 |
| 807660006 | Unknown | 無法識別來源 |

#### gov_modifiedbytype（修改者類型）

| Value | Label |
|:----------|:------------------------------|
| 807660000 | HumanUser |
| 807660001 | ApplicationUser |
| 807660002 | ServicePrincipal |
| 807660003 | SystemAccount |

#### gov_detectionmethod（偵測方法）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | AuditLogQuery | 查詢 Dataverse Audit Log |
| 807660001 | StateLogReconciliation | 狀態與記錄對帳 |
| 807660002 | RealTimePluginDetection | 即時 Plugin 偵測 |
| 807660003 | ScheduledReconciliation | 排程對帳 |

#### gov_severity（嚴重程度）

| Value | Label | 回應時限 |
|:----------|:------------------------------|:-----------------|
| 807660000 | Critical | 立即回應 |
| 807660001 | High | 4 小時內 |
| 807660002 | Medium | 24 小時內 |
| 807660003 | Low | 72 小時內 |

#### gov_resolutionstatus（處理狀態）

| Value | Label |
|:----------|:------------------------------|
| 807660000 | Open |
| 807660001 | Investigating |
| 807660002 | Resolved |
| 807660003 | FalsePositive |
| 807660004 | Escalated |

#### gov_feedbacktype（回饋類型）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | CannotExecute | 無法執行 |
| 807660001 | Conflict | 標準衝突 |
| 807660002 | Improvement | 改善建議 |

#### gov_feedbackresolutionstatus（回饋處理狀態）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | Open | 開放 |
| 807660001 | InProgress | 處理中 |
| 807660002 | Resolved | 已解決 |
| 807660003 | Rejected | 已拒絕 |

#### gov_disputelevel（爭議層級）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | Level2 | 第二級，部門級仲裁 |
| 807660001 | Level3 | 第三級，跨部門級裁決 |

#### gov_disputeresolutionresult（爭議解決結果）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | Resolved | 已解決 |
| 807660001 | Escalated | 已升級 |
| 807660002 | Withdrawn | 已撤回 |

#### gov_actionitemstatus（行動項目狀態）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | Open | 開放 |
| 807660001 | InProgress | 進行中 |
| 807660002 | Completed | 已完成 |
| 807660003 | Cancelled | 已取消 |

#### gov_documentcategory（標準文件分類）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | Architecture | 架構類 |
| 807660001 | Security | 安全類 |
| 807660002 | QA | 品質類 |
| 807660003 | Governance | 治理類 |

#### gov_reviewcycle（審查週期）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | Annual | 年度 |
| 807660001 | SemiAnnual | 半年 |
| 807660002 | Quarterly | 季度 |

#### gov_standardstatus（標準狀態）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | Active | 有效 |
| 807660001 | UnderReview | 審查中 |
| 807660002 | Retired | 已退役 |

#### gov_remindertype（提醒類型）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | GateDeadline | Gate 截止提醒 |
| 807660001 | DocumentReview | 文件審查提醒 |
| 807660002 | RiskReassessment | 風險重評估提醒 |
| 807660003 | General | 一般提醒 |

#### gov_processlogstatus（流程日誌狀態）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | Sent | 已發送 |
| 807660001 | Failed | 發送失敗 |
| 807660002 | Skipped | 已跳過 |

#### gov_interfacetype（介面類型）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | Upstream | 上游 |
| 807660001 | Downstream | 下游 |
| 807660002 | Peer | 同級 |
| 807660003 | Regulatory | 法規主管機關 |

#### gov_assessmentstatus（評估狀態）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | NotAssessed | 尚未評估 |
| 807660001 | InProgress | 評估中 |
| 807660002 | Assessed | 已評估 |
| 807660003 | NeedsReassessment | 需重新評估 |

#### gov_reworkreasoncategory（Rework 原因分類）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | RequirementClarificationDeficiency | 需求釐清不足 |
| 807660001 | DesignError | 設計錯誤 |
| 807660002 | CustomerRequirementChange | 客戶需求變更 |
| 807660003 | Other | 其他 |

#### gov_sldecisionlevel（SL 決策層級）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | SL1 | SL1 |
| 807660001 | SL2 | SL2 |
| 807660002 | SL3 | SL3 |
| 807660003 | SL4 | SL4 |

#### gov_srcompliancestatus（SR 合規狀態）

| Value | Label | 說明 |
|:----------|:------------------------------|:----------------------------------------------|
| 807660000 | Implemented | 已實施 |
| 807660001 | NotApplicable | 不適用 |
| 807660002 | Partial | 部分實施 |

---

## Document Baseline Matrix（文件基線矩陣）— 單一權威

> **重要**：此矩陣為治理系統中所有文件相關映射的**唯一權威來源**。
> Doc 03（SharePoint）、Doc 04（Forms）、Doc 05（Flows）及 Appendix A 皆必須引用本表，**不得各自維護第二份對照表**。
> 若映射需修改，僅修改本表，其他文件自動跟隨。

### 矩陣定義

| DocumentType | Value | RequiredForGate | SharePointFolder | ProjectRegistryLinkField | DefaultDeliverablePackage |
|:-----------------------|:----------:|:------------:|:-----------------|:-------------------------------|:------------------------|
| TechnicalFeasibility | 807660000 | Gate 0 | 01_Feasibility | gov_technicalfeasibilitylink | CoreDeliverable |
| InitialRiskList | 807660001 | Gate 0 | 01_Feasibility | gov_initialrisklistlink | CoreDeliverable |
| RiskAssessmentStrategy | 807660002 | Gate 0 | 01_Feasibility | gov_riskassessmentstrategylink | CoreDeliverable |
| DesignBaseline | 807660003 | Gate 1 | 03_Design | gov_designbaselinelink | CoreDeliverable |
| RiskAssessment | 807660004 | Gate 1 | 02_Risk_Assessment | gov_riskassessmentlink | CoreDeliverable |
| IEC62443Checklist | 807660005 | Gate 1 | 04_Security | gov_iec62443checklistlink | CoreDeliverable |
| ThreatModel | 807660006 | Gate 1 | 04_Security | gov_threatmodellink | CoreDeliverable |
| RequirementTraceability | 807660007 | Gate 1 | 03_Design | gov_requirementtraceabilitylink | CoreDeliverable |
| TestPlan | 807660008 | Gate 1 | 05_Test | gov_testplanlink | CoreDeliverable |
| TestReport | 807660009 | Gate 2, 3 | 05_Test | gov_testreportlink | CoreDeliverable |
| HandoverMeeting | 807660010 | Gate 3 | 06_Handover | gov_handovermeetinglink | CoreDeliverable |
| ResidualRiskList | 807660011 | Gate 3 | 06_Handover | gov_residualrisklistlink | CoreDeliverable |
| Other | 807660012 | - | 01_Feasibility | - | AdHoc |
| DesignObjectInventory | 807660013 | Gate 1 | 03_Design | gov_designobjectinventorylink | CoreDeliverable |
| ChangeImpact | 807660014 | Gate 2 | 03_Design | gov_changeimpactlink | CoreDeliverable |
| DocumentRegister | 807660015 | - | 06_Handover | gov_documentregisterlink | SupplementaryDeliverable |

### 矩陣欄位說明

| 欄位 | 說明 |
|:------------------------------|:----------------------------------------------|
| DocumentType | 對應 gov_documenttype Choice 的 Label（第 5 章） |
| Value | 對應 gov_documenttype Choice 的數值 |
| RequiredForGate | 該文件類型必須在哪個 Gate 前完成上傳。`-` 表示非 Gate 必要 |
| SharePointFolder | GOV-005 上傳時的目標子資料夾名稱（對應 Doc 03 第 5 章資料夾結構） |
| ProjectRegistryLinkField | GOV-005 成功上傳後，將 SharePoint URL 回寫至 gov_projectregistry 的哪個 Link 欄位。`-` 表示不回寫 |
| DefaultDeliverablePackage | GOV-001 基線播種時的預設 gov_deliverablepackage 值 |

### 使用規則

1. **GOV-001 基線播種**：專案建立時，遍歷本矩陣中 `RequiredForGate ≠ -` 的所有列，為每列在 Document Register 建立一筆 `DocumentRole = Planned` 的記錄
2. **GOV-005 上傳路由**：接收使用者上傳時，根據 DocumentType 查閱本矩陣取得 `SharePointFolder`，將檔案上傳至 `{ProjectFolder}/{SharePointFolder}/` 下
3. **GOV-005 Link 回寫**：上傳完成後，根據 `ProjectRegistryLinkField` 將 SharePoint URL 寫入 Project Registry 對應欄位
4. **Link 目標規則**：回寫至 ProjectRegistryLinkField 的 URL 優先選擇同 DocumentType 下最新的 `Approved` 版本；若無 Approved 版本，則選擇最新的 `Active` Draft

---

## 資料表關聯設定

### 關聯定義清單

| 主資料表 | 關聯資料表 | Lookup 欄位 | 關聯類型 | 刪除行為 |
|:---------------------|:-----------------------------|:----------------|:----------:|:----------:|
| gov_projectregistry | gov_reviewdecisionlog | gov_parentproject | N:1 | **Restrict** |
| gov_projectregistry | gov_riskassessmenttable | gov_parentproject | N:1 | **Restrict** |
| gov_projectregistry | gov_exceptionwaiverlog | gov_parentproject | N:1 | **Restrict** |
| gov_projectregistry | gov_documentregister | gov_parentproject | N:1 | **Restrict** |
| gov_projectregistry | gov_governanceviolationlog | gov_parentproject | N:1 | Remove Link |
| gov_projectregistry | gov_bomregistry | gov_parentproject | N:1 | **Restrict** |
| gov_projectregistry | gov_sahandoverevent | gov_parentproject | N:1 | **Restrict** |
| gov_riskassessmenttable | gov_exceptionwaiverlog | gov_relatedrisk | N:1 | Remove Link |
| gov_projectregistry | gov_standardfeedback | gov_parentproject | N:1 | Remove Link |
| gov_projectregistry | gov_disputelog | gov_parentproject | N:1 | **Restrict** |
| gov_projectregistry | gov_actionitem | gov_parentproject | N:1 | **Restrict** |
| gov_reviewdecisionlog | gov_actionitem | gov_relatedgatereview | N:1 | **Restrict** |
| gov_projectregistry | gov_processlog | gov_parentproject | N:1 | Remove Link |
| gov_projectregistry | gov_srcompliancesummary | gov_parentproject | N:1 | **Restrict** |
| gov_documentregister | gov_documentregister | gov_supersededby | N:1 | Remove Link |
| gov_bomregistry | gov_bomregistry | gov_sourcecbom | N:1 | Remove Link |

> **說明**：「關聯類型 N:1」表示從關聯資料表（Many 端）指向主資料表（One 端）的 Lookup 關聯方向。

### 設定刪除行為的操作步驟

**操作路徑**：
1. Power Apps Maker Portal → Tables → gov_projectregistry
2. 選擇 **Relationships** 標籤
3. 找到與 gov_reviewdecisionlog 的關聯
4. 點擊關聯 → **Edit**
5. 展開 **Advanced options**
6. Type of behavior: 選擇 **Referential, Restrict Delete**
7. 點擊 **Save**

**Restrict Delete 效果**：
- 若 Project Registry 有關聯的 Review Decision Log，則禁止刪除該專案
- 這確保稽核記錄不會因專案刪除而遺失

---

## Flow-only 欄位設計與保護

### Flow-only 欄位定義

**Flow-only 欄位**：僅允許 Power Automate Flow（以 Service Principal 身份執行）寫入的欄位。
人類使用者透過任何介面（Power Apps、Dataverse 直接編輯、API）皆無權修改。

### 為何需要 Flow-only 欄位

| 風險 | 若允許人類修改 | 後果 |
|:------------------------|:------------------------------|:------------------------------|
| 治理繞過 | 人類直接修改 CurrentGate = Gate3 | 跳過所有 Gate 審批 |
| 稽核偽造 | 人類修改 ApprovedBy = 其他人 | 偽造審批者身份 |
| 證據竄改 | 人類修改 Decision = Approved | 偽造審批結果 |
| 時間偽造 | 人類修改 ReviewedDate | 偽造審批時間 |

### Flow-only 欄位完整清單

#### gov_projectregistry Flow-only 欄位

| 欄位 | 為何必須為 Flow-only | 被繞過的後果 |
|:-------------------------------|:----------------------------------------------|:------------------------------|
| gov_requestid | 專案識別碼必須由系統產生 | 識別碼重複或偽造 |
| gov_currentgate | Gate 狀態必須由審批結果推導 | 跳過 Gate 審批 |
| gov_requeststatus | 審批狀態必須由 Flow 控制 | 繞過審批流程 |
| gov_projectstatus | 專案狀態必須由 Flow 控制 | 任意關閉專案 |
| gov_requestedgate | 申請 Gate 必須由表單觸發 Flow 設定 | 偽造申請 |
| gov_documentfreezestatus | 文件凍結必須由 Gate 3 通過觸發 | 解凍已凍結文件 |
| gov_documentfreezedate | 凍結時間必須由系統記錄 | 偽造時間 |
| gov_gate0passeddate | Gate 通過時間必須由系統記錄 | 偽造時間 |
| gov_gate1passeddate | 同上 | 同上 |
| gov_gate2passeddate | 同上 | 同上 |
| gov_gate3passeddate | 同上 | 同上 |
| gov_riskacceptancestatus | Risk Acceptance 必須由 Approval 觸發 | 繞過風險接受 |
| gov_riskacceptancedate | 接受時間必須由系統記錄 | 偽造時間 |
| gov_riskowner | Risk Owner 必須由 Approval 回應設定 | 偽造 Owner |
| gov_executiveapprover | 執行長審批者必須由 Approval 設定 | 偽造審批者 |
| gov_highestresidualrisklevel | 必須由 Flow 計算 | 繞過風險等級判斷 |
| gov_reworkcount | 重工次數必須由 Flow 累計 | 重設重工次數 |
| gov_lastreworkdate | 重工時間必須由系統記錄 | 偽造時間 |
| gov_sharepointfolderurl | SharePoint URL 必須由 Flow 產生 | 偽造連結 |

#### gov_reviewdecisionlog Flow-only 欄位

| 欄位 | 為何必須為 Flow-only |
|:-------------------------------|:----------------------------------------------|
| gov_reviewid | 事件識別碼必須由系統產生 |
| gov_reviewtype | 事件類型必須由 Flow 設定 |
| gov_parentproject | 關聯專案必須由 Flow 設定 |
| gov_submittedby | 提交者必須由系統自動記錄 |
| gov_submitteddate | 提交時間必須由系統記錄 |
| gov_approvedby | 審批者必須由 Approval 回應設定 |
| gov_decision | 審批結果必須由 Approval 回應設定 |
| gov_requestedgate | 申請 Gate 必須由 Flow 設定 |
| gov_revieweddate | 審批時間必須由系統記錄 |
| gov_triggerflowrunid | Flow Run ID 必須由系統記錄 |
| gov_gate1securityreviewstatus | 必須由 Security Reviewer Approval 設定 |
| gov_gate1securityreviewer | 必須由 Approval 回應設定 |
| gov_gate1securityreviewdate | 必須由系統記錄 |
| gov_gate1qareviewstatus | 必須由 QA Reviewer Approval 設定 |
| gov_gate1qareviewer | 必須由 Approval 回應設定 |
| gov_gate1qareviewdate | 必須由系統記錄 |
| gov_gate1governancereviewstatus | 必須由 Governance Lead Approval 設定 |
| gov_gate1governancereviewer | 必須由 Approval 回應設定 |
| gov_gate1governancereviewdate | 必須由系統記錄 |
| gov_gate3riskacceptancestatus | 必須由 Risk Acceptance Approval 設定 |
| gov_gate3approvalstatus | 必須由 Gate 3 Approval 設定 |
| gov_riskownerreviewstatus | 必須由 Risk Owner Approval 設定 |
| gov_executivereviewstatus | 必須由 Executive Approval 設定 |
| gov_rejectionreasons | 必須由 Flow 記錄 |
| gov_rejectedby | 必須由 Approval 回應設定 |

#### 其他資料表 Flow-only 欄位

**gov_riskassessmenttable**：
- gov_riskid, gov_parentproject, gov_risklevel, gov_residualrisklevel
- gov_riskacceptancestatus, gov_riskacceptedby, gov_riskacceptancedate
- gov_initialassessmentdate, gov_initialassessedby
- gov_lastreassessmentdate, gov_reassessedby, gov_reassessmentcount, gov_riskstatus

**gov_exceptionwaiverlog**：
- gov_waiverid, gov_parentproject, gov_requestedby, gov_requesteddate
- gov_waiverstatus, gov_approvalstatus, gov_approvedby, gov_approveddate

**gov_documentregister**：
- gov_documentid, gov_parentproject, gov_sharepointfilelink
- gov_uploadedby, gov_uploadeddate, gov_reviewstatus, gov_reviewedby, gov_revieweddate, gov_filesize
- gov_documentrole, gov_supersededby
- gov_isfrozen, gov_frozendate

**gov_governanceviolationlog**：
- 所有欄位皆為 Flow-only（僅 GOV-017/018 可寫入）

**gov_counterlist**：
- gov_currentyear, gov_currentcounter, gov_lastupdated, gov_lastupdatedby

#### gov_standardfeedback Flow-only 欄位

| 欄位 | 為何必須為 Flow-only |
|:------------------------------|:----------------------------------------------|
| gov_feedbackid | Counter 產生的唯一識別碼，不可由使用者修改 |
| gov_reportedby | 系統自動填入提報人，防止冒名提報 |
| gov_reporteddate | 系統時戳，確保時間線不可竄改 |
| gov_feedbackresolutionstatus | 解決狀態由 Flow 控制，確保流程閉環 |
| gov_resolutiondate | 系統時戳，解決日期不可回溯修改 |

#### gov_disputelog Flow-only 欄位

| 欄位 | 為何必須為 Flow-only |
|:------------------------------|:----------------------------------------------|
| gov_disputeid | Counter 產生的唯一識別碼，不可由使用者修改 |
| gov_raisedby | 系統自動填入提報人，防止冒名提報 |
| gov_raiseddate | 系統時戳，確保時間線不可竄改 |
| gov_assignedmediator | 仲裁人由 Flow 依爭議層級自動指派 |
| gov_mediationdate | 系統時戳，調解日期不可回溯修改 |
| gov_disputeresolutiondate | 系統時戳，解決日期不可回溯修改 |
| gov_closeddate | 系統時戳，結案日期不可回溯修改 |
| gov_disputeresolutionresult | 解決結果由 Flow 控制，確保流程閉環 |

#### gov_actionitem Flow-only 欄位

| 欄位 | 為何必須為 Flow-only |
|:------------------------------|:----------------------------------------------|
| gov_actionitemid | Counter 產生的唯一識別碼，不可由使用者修改 |
| gov_relatedgatereview | 關聯審查記錄由 Flow 自動設定，不可變更 |
| gov_completiondate | 系統時戳，完成日期不可回溯修改 |
| gov_actionitemstatus | 行動項目狀態由 Flow 控制，確保流程閉環 |

#### gov_processlog Flow-only 欄位

| 欄位 | 為何必須為 Flow-only |
|:------------------------------|:----------------------------------------------|
| gov_processlogid | Counter 產生的唯一識別碼，不可由使用者修改 |
| gov_remindertype | 提醒類型由 Flow 自動設定 |
| gov_scheduledtime | 排定時間由 Flow 自動設定 |
| gov_actualsenttime | 實際發送時間由系統記錄 |
| gov_recipient | 收件人由 Flow 根據角色自動填入 |
| gov_processlogstatus | 發送狀態由 Flow 控制 |
| gov_parentproject | 關聯專案由 Flow 自動設定 |
| gov_triggeredbyflow | 觸發 Flow 名稱由系統自動記錄 |

#### gov_reviewdecisionlog Flow-only 欄位（新增）

- `gov_sldecisionlevel`：SL 決策由 Gate 審批 Flow 自動記錄
- `gov_slapprovedby`：SL 核准人由 Flow 從審批結果自動填入

#### gov_projectregistry Flow-only 欄位（新增）

- `gov_reworkreasoncategory`：Rework 原因由 GOV-002 Flow 自動記錄

#### gov_bomregistry Flow-only 欄位

| 欄位 | 為何必須為 Flow-only |
|:------------------------------|:----------------------------------------------|
| gov_bomid | Counter 產生的唯一識別碼，不可由使用者修改 |
| gov_parentproject | 關聯專案由 Flow 自動設定 |
| gov_bomtype | BOM 類型由 Flow 根據建立情境自動設定 |
| gov_bombindingscope | 拘束範圍由 Flow 根據 BOM 類型自動設定 |
| gov_bomownerrole | 當責角色由 Flow 根據建立情境自動設定 |
| gov_bomstatus | BOM 狀態由 Flow 控制，確保狀態流轉正確 |
| gov_linkagegate | 關聯 Gate 由 Flow 根據專案進度自動設定 |
| gov_documentlink | SharePoint 文件連結由 Flow 產生 |
| gov_createdby | 建立者由系統自動記錄 |
| gov_createddate | 系統時戳，建立日期不可回溯修改 |
| gov_quoteddate | 報價日期由 Flow 記錄（CBOM） |
| gov_quotedversionsnapshot | 報價時版本快照由 Flow 記錄（CBOM） |
| gov_gate0approveddate | Gate 0 核准日期由 Flow 記錄（CBOM） |
| gov_baselinedate | 基線建立日期由 Flow 記錄（EBOM） |
| gov_frozendate | 凍結日期由 Flow 記錄（EBOM） |
| gov_sourcecbom | 來源 CBOM 關聯由 Flow 自動設定（EBOM） |
| gov_cbomebomvariance | 差異標記由 Flow 自動判斷 |
| gov_variancenotifieddate | 差異通知日期由系統記錄 |
| gov_lastmodifieddate | 系統時戳，最後修改日期不可回溯修改 |
| gov_lastmodifiedby | 最後修改者由系統自動記錄 |

#### gov_sahandoverevent Flow-only 欄位

| 欄位 | 為何必須為 Flow-only |
|:------------------------------|:----------------------------------------------|
| gov_handoverid | Counter 產生的唯一識別碼，不可由使用者修改 |
| gov_parentproject | 關聯專案由 Flow 自動設定 |
| gov_originalsa | 原 SA 由 Flow 自動帶入，防止篡改 |
| gov_newsa | 新 SA 由 Flow 自動設定 |
| gov_handoverstatus | 交接狀態由 Flow 控制，確保流程閉環 |
| gov_requesteddate | 系統時戳，申請日期不可回溯修改 |
| gov_accepteddate | 系統時戳，接受日期不可回溯修改 |

### Flow-only 欄位保護機制總覽

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        Flow-only 欄位保護架構                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  第 1 層：Field-Level Security（欄位層級安全）                               │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  GOV-FlowOnly-ReadWrite Profile → Flow Service Principal → 可讀寫    │   │
│  │  GOV-FlowOnly-ReadOnly Profile → 所有其他使用者 → 僅可讀             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    ▼                                        │
│  第 2 層：Security Role（安全角色）                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  GOV-SystemArchitect → Create = None（無法直接建立記錄）              │   │
│  │  GOV-FlowServicePrincipal → Create = Organization（可建立記錄）       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    ▼                                        │
│  第 3 層：偵測與回滾（GOV-017 Guardrail Monitor）                            │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  每小時查詢 Dataverse Audit Log                                       │   │
│  │  偵測 ModifiedBy ≠ Flow Service Principal 的 Flow-only 欄位修改       │   │
│  │  → 寫入 Governance Violation Log                                      │   │
│  │  → 自動回滾至原始值                                                    │   │
│  │  → 發送高優先級通知                                                    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Field-Level Security 實作步驟

### Field-Level Security 運作原理

**Field-Level Security（FLS）** 在 Dataverse 中提供欄位層級的存取控制，獨立於資料表層級的安全角色。

**運作流程**：
1. 對欄位啟用「Column Security」
2. 建立「Field Security Profile」
3. 在 Profile 中設定欄位權限（Read / Create / Update）
4. 將使用者或團隊指派至 Profile

**重要**：啟用 Column Security 後，未被任何 Profile 授權的使用者將**完全無法看到**該欄位。

### 步驟一：對 Flow-only 欄位啟用 Column Security

**對 gov_projectregistry 的每個 Flow-only 欄位執行以下步驟**：

**操作路徑**：
1. Power Apps Maker Portal → Tables → gov_projectregistry
2. 選擇 **Columns** 標籤
3. 點擊欄位名稱（例如：gov_currentgate）
4. 點擊右上角的 **Advanced options**（或展開進階選項）
5. 找到 **Enable column security** 選項
6. 將開關切換為 **On**
7. 點擊 **Save**

**對以下所有 Flow-only 欄位重複上述步驟**：

**gov_projectregistry**：
- [ ] gov_currentgate
- [ ] gov_requeststatus
- [ ] gov_projectstatus
- [ ] gov_requestedgate
- [ ] gov_documentfreezestatus
- [ ] gov_documentfreezedate
- [ ] gov_gate0passeddate
- [ ] gov_gate1passeddate
- [ ] gov_gate2passeddate
- [ ] gov_gate3passeddate
- [ ] gov_riskacceptancestatus
- [ ] gov_riskacceptancedate
- [ ] gov_riskowner
- [ ] gov_executiveapprover
- [ ] gov_highestresidualrisklevel
- [ ] gov_reworkcount
- [ ] gov_lastreworkdate
- [ ] gov_sharepointfolderurl

**gov_reviewdecisionlog**：
- [ ] gov_reviewtype
- [ ] gov_parentproject
- [ ] gov_submittedby
- [ ] gov_submitteddate
- [ ] gov_approvedby
- [ ] gov_decision
- [ ] gov_requestedgate
- [ ] gov_revieweddate
- [ ] gov_triggerflowrunid
- [ ] gov_gate1securityreviewstatus
- [ ] gov_gate1securityreviewer
- [ ] gov_gate1securityreviewdate
- [ ] gov_gate1qareviewstatus
- [ ] gov_gate1qareviewer
- [ ] gov_gate1qareviewdate
- [ ] gov_gate1governancereviewstatus
- [ ] gov_gate1governancereviewer
- [ ] gov_gate1governancereviewdate
- [ ] gov_gate3riskacceptancestatus
- [ ] gov_gate3approvalstatus
- [ ] gov_riskownerreviewstatus
- [ ] gov_executivereviewstatus
- [ ] gov_rejectionreasons
- [ ] gov_rejectedby

**對其他資料表的 Flow-only 欄位重複上述步驟**。

### 步驟二：建立 Field Security Profile - GOV-FlowOnly-ReadWrite

**操作路徑**：
1. Power Platform admin center → Environments → 選擇環境
2. 點擊 **Settings**
3. 展開 **Users + permissions** → **Field security profiles**
4. 點擊 **+ New profile**

**填寫 Profile 設定**：

| 設定欄位 | 填寫值 |
|:--------------------------------|:------------------------------------------------------|
| Name | `GOV-FlowOnly-ReadWrite` |
| Description | `Flow Service Principal 對 Flow-only 欄位的完整存取權限。僅指派給 GOV-FlowServicePrincipal。` |

**點擊 Create**。

### 步驟三：設定 GOV-FlowOnly-ReadWrite 的欄位權限

**操作路徑**：
1. 開啟剛建立的 GOV-FlowOnly-ReadWrite Profile
2. 選擇 **Field Permissions** 標籤
3. 點擊 **+ Add**

**設定 gov_projectregistry 欄位權限**：

1. 在 Entity 下拉選單選擇 **Project Registry (gov_projectregistry)**
2. 勾選所有已啟用 Column Security 的欄位
3. 對每個欄位設定權限：

| 欄位 | Read | Create | Update |
|:-------------------------------|:--------|:--------|:--------|
| gov_currentgate | Yes | Yes | Yes |
| gov_requeststatus | Yes | Yes | Yes |
| gov_projectstatus | Yes | Yes | Yes |
| （所有其他 Flow-only 欄位） | Yes | Yes | Yes |

4. 點擊 **Save**

**對其他資料表重複上述步驟**：
- gov_reviewdecisionlog
- gov_riskassessmenttable
- gov_exceptionwaiverlog
- gov_documentregister
- gov_governanceviolationlog
- gov_counterlist

### 步驟四：將 Flow Service Principal 指派至 GOV-FlowOnly-ReadWrite

**操作路徑**：
1. 在 GOV-FlowOnly-ReadWrite Profile 頁面
2. 選擇 **Users** 標籤
3. 點擊 **+ Add users**
4. 搜尋 `GOV-FlowServicePrincipal`（這是您在 01 文件建立的 Application User）
5. 選擇並點擊 **Add**

**驗證結果**：
- [ ] Users 標籤顯示 GOV-FlowServicePrincipal

### 步驟五：建立 Field Security Profile - GOV-FlowOnly-ReadOnly

**操作路徑**：
1. Field security profiles → + New profile

**填寫 Profile 設定**：

| 設定欄位 | 填寫值 |
|:--------------------------------|:------------------------------------------------------|
| Name | `GOV-FlowOnly-ReadOnly` |
| Description | `所有人類使用者對 Flow-only 欄位的唯讀存取權限。禁止修改。` |

**點擊 Create**。

### 步驟六：設定 GOV-FlowOnly-ReadOnly 的欄位權限

**操作路徑**：
1. 開啟 GOV-FlowOnly-ReadOnly Profile
2. 選擇 Field Permissions 標籤
3. 點擊 + Add

**設定欄位權限**（對所有 Flow-only 欄位）：

| 欄位 | Read | Create | Update |
|:-------------------------------|:--------|:--------|:--------|
| gov_currentgate | **Yes** | **No** | **No** |
| gov_requeststatus | **Yes** | **No** | **No** |
| （所有其他 Flow-only 欄位） | **Yes** | **No** | **No** |

### 步驟七：將所有 GOV 團隊指派至 GOV-FlowOnly-ReadOnly

**操作路徑**：
1. 在 GOV-FlowOnly-ReadOnly Profile 頁面
2. 選擇 **Teams** 標籤
3. 點擊 **+ Add teams**
4. 逐一搜尋並選擇：
   - GOV-Architects
   - GOV-SecurityReviewers
   - GOV-QAReviewers
   - GOV-EngineeringManagement
   - GOV-GovernanceLead
   - GOV-ExecutiveManagement
5. 點擊 **Add**

**驗證結果**：
- [ ] Teams 標籤顯示 6 個團隊

### Field-Level Security 驗證測試

**測試 FLS-001：Flow Service Principal 可寫入 Flow-only 欄位**

```
測試前置條件：
- GOV-001 Flow 已建立並可執行
- 或使用 Power Automate 建立測試 Flow

測試步驟：
1. 執行 GOV-001 Flow（或測試 Flow）
2. Flow 嘗試建立 Project Registry 記錄，設定 gov_currentgate = Pending
3. 查詢 Dataverse，確認記錄已建立

預期結果：
- [ ] 記錄建立成功
- [ ] gov_currentgate 欄位值為 Pending
- [ ] Owner 為 GOV-FlowServicePrincipal
```

**測試 FLS-002：人類使用者無法修改 Flow-only 欄位（透過 UI）**

```
測試步驟：
1. 使用 System Architect 帳號登入 Power Apps
2. 開啟 Project Registry 資料表
3. 找到一筆記錄，點擊編輯
4. 嘗試修改 Current Gate 欄位

預期結果：
- [ ] Current Gate 欄位顯示為灰色（無法編輯）
- [ ] 或欄位完全不顯示
- [ ] 或點擊後顯示「您沒有權限修改此欄位」
```

**測試 FLS-003：人類使用者可讀取 Flow-only 欄位**

```
測試步驟：
1. 使用 System Architect 帳號登入 Power Apps
2. 開啟 Project Registry 資料表
3. 找到一筆記錄

預期結果：
- [ ] 可看到 Current Gate 欄位及其值
- [ ] 可看到 Request Status 欄位及其值
- [ ] 所有 Flow-only 欄位皆可讀取
```

---

## 防止與偵測非授權資料修改

### 非授權修改的風險來源

> **警告：Field-Level Security 僅能防止透過 Power Apps UI 的修改。**
> **以下途徑可能繞過 FLS 進行非授權修改：**

| 風險來源 | 說明 | 風險等級 |
|:------------------------------|:----------------------------------------------|:------------|
| **Dataverse Web API** | 開發者可直接呼叫 API 修改資料 | 高 |
| **Postman / HTTP Client** | 使用 Postman 等工具發送 API 請求 | 高 |
| **PowerShell Script** | 使用 PowerShell 與 Dataverse SDK 修改資料 | 高 |
| **外部系統整合** | 透過 Connector 或自訂整合寫入資料 | 中 |
| **Power Automate（非授權 Flow）** | 未經授權的 Flow 嘗試修改資料 | 中 |
| **Excel 匯入** | 透過 Excel 匯入功能批量修改 | 中 |
| **Canvas App 直接連線** | Canvas App 直接連線 Dataverse 修改 | 中 |

### 為何 FLS 無法完全防止 API 修改

**技術原因**：
1. FLS 在 UI 層面運作，API 呼叫可能繞過
2. 若攻擊者取得有效的 OAuth Token，可直接呼叫 API
3. Application User 若權限設定不當，可能被濫用

**結論**：必須建立「偵測與回應」機制，作為 FLS 的補強。

### 偵測機制設計

#### GOV-017 Guardrail Monitor（每小時執行）

**功能**：查詢 Dataverse Audit Log，偵測非 Flow Service Principal 的 Flow-only 欄位修改。

**偵測邏輯**：

```
輸入：過去 1 小時的 Dataverse Audit Log

For each audit record:
    IF (
        EntityName IN [gov_projectregistry, gov_reviewdecisionlog, ...]
        AND AttributeName IN [Flow-only 欄位清單]
        AND ModifiedBy ≠ GOV-FlowServicePrincipal
    ) THEN:
        1. 判定為違規
        2. 建立 Governance Violation Log 記錄
        3. 嘗試自動回滾（將欄位改回 OldValue）
        4. 發送高優先級通知給 Governance Lead
```

**Audit Log 查詢欄位**：

| Audit Log 欄位 | 用途 |
|:------------------------------|:----------------------------------------------|
| ObjectId | 被修改記錄的 ID |
| EntityName | 被修改的資料表 |
| AttributeName | 被修改的欄位 |
| OldValue | 修改前的值 |
| NewValue | 修改後的值 |
| ModifiedBy | 執行修改的使用者 |
| ModifiedOn | 修改時間 |
| Operation | 操作類型（Update, Create, Delete） |

#### GOV-018 Compliance Reconciler（每日執行）

**功能**：驗證 Dataverse 狀態與 Review Decision Log 的一致性。

**偵測邏輯**：

```
輸入：所有 Active 專案

For each project:
    1. 查詢 Project Registry.CurrentGate
    2. 查詢 Review Decision Log 的最新審批記錄
    3. IF (CurrentGate 與最新審批記錄不一致) THEN:
        - 判定為「State-Log Inconsistency」違規
        - 建立 Governance Violation Log 記錄
        - 發送高優先級通知
```

### 違規來源識別方法

**GOV-017 如何判斷違規來源**：

| 判斷條件 | 違規來源 |
|:----------------------------------------------|:------------------------------|
| ModifiedBy = Human User + User Agent 包含 "PowerApps" | PowerAppsUI |
| ModifiedBy = Human User + User Agent 包含 "Postman" | PostmanOrScript |
| ModifiedBy = Application User（非 Flow SP） | ExternalIntegration |
| ModifiedBy = Human User + 無 User Agent | DataverseAPI |
| ModifiedBy = System Account | Unknown |

**User Agent 取得方式**：
- Dataverse Audit Log 的 Request 資訊中可能包含 User Agent
- 若無法取得，標記為 Unknown

### 自動回滾機制

**回滾邏輯**：

```
IF (ViolationType = UnauthorizedFieldModification) THEN:
    1. 取得 OldValue（從 Audit Log）
    2. 使用 Flow Service Principal 執行 Update 操作
    3. 將欄位改回 OldValue
    4. 更新 Governance Violation Log:
        - RollbackStatus = Completed
        - RollbackDate = Now()
        - RollbackBy = GOV-017
```

**回滾失敗處理**：

```
IF (回滾操作失敗) THEN:
    1. 更新 Governance Violation Log:
        - RollbackStatus = ManualRequired
        - Severity = Critical
    2. 發送緊急通知給 Governance Lead + System Administrator
    3. 通知內容包含手動回滾指引
```

### 禁止事項與對應偵測機制

| 禁止事項 | 技術限制 | 偵測機制 | 回應動作 |
|:------------------------------|:-------------------------------|:-------------------------------|:------------------------------|
| 人類修改 Flow-only 欄位 | Field-Level Security（FLS） | GOV-017 Audit Log 查詢 | 自動回滾 + 通知 |
| 直接建立 Project Registry | Security Role（Create = None） | GOV-017 Owner 檢查 | 標記記錄 + 通知 |
| 刪除 Review Decision Log | Security Role（Delete = None） + Restrict Delete | GOV-017 Delete 操作查詢 | 通知（無法回滾刪除） |
| 直接呼叫 Dataverse API | 無法完全禁止 | GOV-017 偵測 | 記錄 + 通知 + 回滾 |
| Postman 修改資料 | 無法完全禁止 | GOV-017 User Agent 分析 | 記錄 + 通知 + 回滾 |
| 外部系統整合寫入 | Application User 權限控制 | GOV-017 Application User 監控 | 記錄 + 通知 + 回滾 |
| Excel 匯入 | 可停用 Excel 匯入功能 | GOV-017 批量修改偵測 | 記錄 + 通知 |

### 停用可能的繞過途徑

#### 停用 Excel 匯入功能

**操作路徑**：
1. Power Platform admin center → Environments → 選擇環境
2. Settings → Features
3. 找到 **Excel export/import** → 設為 **Off**

#### 限制 Dataverse API 存取

**操作路徑**：
1. Entra admin center → Applications → App registrations
2. 找到可能的第三方應用程式
3. 撤銷 Dataverse API 權限

#### 限制 Canvas App 直接連線

**設計原則**：
- 所有 Canvas App 必須透過 Power Automate Flow 寫入資料
- 禁止 Canvas App 直接使用 Dataverse Connector 的 Patch 函數修改 Flow-only 欄位

---

## 治理違規事件資料模型

### 與 SOP-04 / SOP-05 的銜接

**gov_governanceviolationlog** 資料表是治理違規的完整記錄，與以下 SOP 直接銜接：

| SOP | 銜接方式 |
|:------------------------------|:----------------------------------------------|
| **SOP-04 Testing Runbook** | 4.7 節「Guardrail Monitor 測試」使用 Governance Violation Log 驗證偵測功能 |
| **SOP-05 Roles and Boundaries** | 1.2 節「治理閉環驗證」使用 Governance Violation Log 確認違規已處理 |
| **SOP-05 Chapter 1** | 4.1 節「GOV-017 Guardrail Monitor」寫入 Governance Violation Log |
| **SOP-05 Chapter 1** | 4.2 節「GOV-018 Compliance Reconciler」寫入 Governance Violation Log |

### Governance Violation Log 完整欄位說明

| 欄位 | 說明 | 來源 | SOP 用途 |
|:------------------------------|:----------------------------------------------|:---------------------|:------------------------|
| ViolationID | 違規事件唯一識別碼 | 系統產生 | 追溯用 |
| Violation Type | 違規類型 | GOV-017/018 判定 | SOP-05 分類 |
| Violated Entity | 違規的資料表 | Audit Log | 定位問題 |
| Violated Field | 違規的欄位 | Audit Log | 定位問題 |
| Violated Record ID | 違規記錄的主鍵 | Audit Log | 回滾用 |
| Parent Project | 關聯專案 | 查詢 | SOP-04 報告 |
| Old Value | 修改前的值 | Audit Log | 回滾用 |
| New Value | 修改後的值 | Audit Log | 證據保存 |
| Modified By | 執行修改的身分 | Audit Log | 追究責任 |
| Modified By Type | 修改者類型 | 判定邏輯 | SOP-05 分析 |
| Modified Date | 修改發生時間 | Audit Log | 時間軸 |
| Detected Date | 偵測時間 | GOV-017/018 | 效能指標 |
| Detected By Flow | 偵測的 Flow | GOV-017/018 | 追溯用 |
| Detection Method | 偵測方法 | GOV-017/018 | SOP-04 驗證 |
| Violation Source | 違規來源 | 判定邏輯 | SOP-05 分析 |
| Client IP Address | 來源 IP | Audit Log（若有） | 調查用 |
| User Agent | 用戶端資訊 | Audit Log（若有） | 判斷來源 |
| Rollback Status | 回滾狀態 | GOV-017 | 處理追蹤 |
| Rollback Date | 回滾時間 | GOV-017 | 處理追蹤 |
| Severity | 嚴重程度 | 判定邏輯 | SOP-05 優先級 |
| Resolution Status | 處理狀態 | Governance Lead | SOP-05 追蹤 |
| Resolution Notes | 處理說明 | Governance Lead | 稽核用 |
| Resolved By | 處理者 | Governance Lead | 追溯用 |
| Resolved Date | 處理時間 | Governance Lead | SOP-05 KPI |
| SOP Reference | 相關 SOP | GOV-017/018 | 引用 |
| Notification Sent | 通知狀態 | GOV-017/018 | 追蹤 |
| Notification Recipients | 收件人 | GOV-017/018 | 追蹤 |

### 違規事件處理流程

```
違規發生
    │
    ▼
GOV-017/018 偵測
    │
    ├─────────────────────────────────────────────┐
    │                                             │
    ▼                                             ▼
建立 Governance Violation Log              自動回滾（若適用）
    │                                             │
    ├─────────────────────────────────────────────┘
    │
    ▼
發送通知給 Governance Lead
    │
    ▼
Governance Lead 調查
    │
    ├── 誤操作 → 更新 Resolution Status = Resolved, Notes = "誤操作，已教育使用者"
    │
    ├── 惡意行為 → 更新 Resolution Status = Escalated, Severity = Critical
    │               → 通知 System Administrator 撤銷權限
    │
    └── 誤報 → 更新 Resolution Status = FalsePositive, Notes = "誤報原因"
    │
    ▼
關閉違規事件
```

### 違規事件報告（SOP-04 用）

**每日違規摘要報告欄位**：

| 報告欄位 | 資料來源 |
|:------------------------------|:----------------------------------------------|
| 報告日期 | 系統產生 |
| 總違規數 | COUNT(ViolationID) WHERE DetectedDate = 今日 |
| 按類型分類 | GROUP BY ViolationType |
| 按嚴重程度分類 | GROUP BY Severity |
| 自動回滾成功數 | COUNT WHERE RollbackStatus = Completed |
| 需人工處理數 | COUNT WHERE RollbackStatus = ManualRequired |
| 未解決數 | COUNT WHERE ResolutionStatus = Open |

---

## 安全角色與權限矩陣

### 安全角色清單

| 角色 Schema Name | 顯示名稱 | 用途 |
|:------------------------------|:------------------------------|:------------------------------|
| gov_systemarchitect | GOV-SystemArchitect | 系統架構師 |
| gov_projectmanager | GOV-ProjectManager | 專案經理 |
| gov_securityreviewer | GOV-SecurityReviewer | 安全審查員 |
| gov_qareviewer | GOV-QAReviewer | 品質審查員 |
| gov_engineeringmanagement | GOV-EngineeringManagement | 工程主管 |
| gov_governancelead | GOV-GovernanceLead | 治理負責人 |
| gov_executivemanagement | GOV-ExecutiveManagement | 執行長 |
| gov_flowserviceprincipal | GOV-FlowServicePrincipal | Flow 服務帳號 |

### 建立安全角色的操作步驟

**操作路徑**：
1. Power Platform admin center → Environments → 選擇環境
2. Settings → Users + permissions → Security roles
3. 點擊 **+ New role**

**對每個角色執行**：
1. 填寫 Role Name
2. 選擇 Business Unit（根業務單位）
3. 設定各資料表的權限
4. 點擊 Save and Close

### 權限矩陣

#### gov_projectregistry 權限

| 權限 | SystemArchitect | PM | Reviewers | EM | GovLead | Executive | FlowSP |
|-----|:---------------:|:--:|:---------:|:--:|:-------:|:---------:|:------:|
| Create | None | None | None | None | None | None | **Org** |
| Read | Org | Org | Org | Org | Org | Org | Org |
| Write | User* | User* | None | None | None | None | **Org** |
| Delete | None | None | None | None | None | None | None |
| Append | Org | Org | None | None | None | None | Org |
| AppendTo | Org | Org | Org | Org | Org | Org | Org |

*User = 僅限自己為 SystemArchitect 的記錄的非 Flow-only 欄位

#### gov_reviewdecisionlog 權限

| 權限 | SystemArchitect | PM | Reviewers | EM | GovLead | Executive | FlowSP |
|-----|:---------------:|:--:|:---------:|:--:|:-------:|:---------:|:------:|
| Create | None | None | None | None | None | None | **Org** |
| Read | Org | Org | Org | Org | Org | Org | Org |
| Write | None | None | None | None | None | None | **Org** |
| Delete | None | None | None | None | None | None | None |

#### gov_governanceviolationlog 權限

| 權限 | SystemArchitect | PM | Reviewers | EM | GovLead | Executive | FlowSP |
|-----|:---------------:|:--:|:---------:|:--:|:-------:|:---------:|:------:|
| Create | None | None | None | None | None | None | **Org** |
| Read | None | None | None | None | **Org** | None | Org |
| Write | None | None | None | None | User** | None | **Org** |
| Delete | None | None | None | None | None | None | None |

**僅 Governance Lead 可讀取違規記錄，並可更新 Resolution Notes

#### gov_standardfeedback 權限

| 權限 | SystemArchitect | PM | Reviewers | EM | GovLead | Executive | FlowSP |
|-----|:---------------:|:--:|:---------:|:--:|:-------:|:---------:|:------:|
| Create | None | None | None | None | None | None | **Org** |
| Read | Org | Org | Org | Org | Org | Org | Org |
| Write | None | None | None | None | None | None | **Org** |
| Delete | None | None | None | None | None | None | None |

#### gov_disputelog 權限

| 權限 | SystemArchitect | PM | Reviewers | EM | GovLead | Executive | FlowSP |
|-----|:---------------:|:--:|:---------:|:--:|:-------:|:---------:|:------:|
| Create | None | None | None | None | None | None | **Org** |
| Read | Org | Org | Org | Org | Org | Org | Org |
| Write | None | None | None | None | None | None | **Org** |
| Delete | None | None | None | None | None | None | None |

#### gov_actionitem 權限

| 權限 | SystemArchitect | PM | Reviewers | EM | GovLead | Executive | FlowSP |
|-----|:---------------:|:--:|:---------:|:--:|:-------:|:---------:|:------:|
| Create | None | None | None | None | None | None | **Org** |
| Read | Org | Org | Org | Org | Org | Org | Org |
| Write | None | None | None | None | None | None | **Org** |
| Delete | None | None | None | None | None | None | None |

#### gov_processlog 權限

| 權限 | SystemArchitect | PM | Reviewers | EM | GovLead | Executive | FlowSP |
|-----|:---------------:|:--:|:---------:|:--:|:-------:|:---------:|:------:|
| Create | None | None | None | None | None | None | **Org** |
| Read | Org | Org | Org | Org | Org | Org | Org |
| Write | None | None | None | None | None | None | **Org** |
| Delete | None | None | None | None | None | None | None |

#### gov_standardsregistry 權限

| 權限 | SystemArchitect | PM | Reviewers | EM | GovLead | Executive | FlowSP |
|-----|:---------------:|:--:|:---------:|:--:|:-------:|:---------:|:------:|
| Create | None | None | None | None | User | None | **Org** |
| Read | Org | Org | Org | Org | Org | Org | Org |
| Write | None | None | None | None | User | None | **Org** |
| Delete | None | None | None | None | None | None | None |

#### gov_externalunit 權限

| 權限 | SystemArchitect | PM | Reviewers | EM | GovLead | Executive | FlowSP |
|-----|:---------------:|:--:|:---------:|:--:|:-------:|:---------:|:------:|
| Create | None | None | None | None | User | None | **Org** |
| Read | Org | Org | Org | Org | Org | Org | Org |
| Write | None | None | None | None | User | None | **Org** |
| Delete | None | None | None | None | None | None | None |

#### gov_srcompliancesummary 權限

| 權限 | SystemArchitect | PM | Reviewers | EM | GovLead | Executive | FlowSP |
|-----|:---------------:|:--:|:---------:|:--:|:-------:|:---------:|:------:|
| Create | None | None | None | None | User | None | **Org** |
| Read | Org | Org | Org | Org | Org | Org | Org |
| Write | None | None | None | None | User | None | **Org** |
| Delete | None | None | None | None | None | None | None |

#### gov_riskassessmenttable 權限

| 權限 | SystemArchitect | PM | Reviewers | EM | GovLead | Executive | FlowSP |
|-----|:---------------:|:--:|:---------:|:--:|:-------:|:---------:|:------:|
| Create | None | None | None | None | None | None | **Org** |
| Read | Org | Org | Org | None | Org | None | Org |
| Write | None | None | None | None | None | None | **Org** |
| Delete | None | None | None | None | None | None | None |

#### gov_exceptionwaiverlog 權限

| 權限 | SystemArchitect | PM | Reviewers | EM | GovLead | Executive | FlowSP |
|-----|:---------------:|:--:|:---------:|:--:|:-------:|:---------:|:------:|
| Create | None | None | None | None | None | None | **Org** |
| Read | Org | None | None | None | Org | None | Org |
| Write | None | None | None | None | None | None | **Org** |
| Delete | None | None | None | None | None | None | None |

#### gov_documentregister 權限

| 權限 | SystemArchitect | PM | Reviewers | EM | GovLead | Executive | FlowSP |
|-----|:---------------:|:--:|:---------:|:--:|:-------:|:---------:|:------:|
| Create | None | None | None | None | None | None | **Org** |
| Read | Org | Org | None | None | Org | None | Org |
| Write | None | None | None | None | User** | None | **Org** |
| Delete | None | None | None | None | None | None | None |

**GovLead 僅可更新備註（comments）欄位

#### gov_bomregistry 權限

| 權限 | SystemArchitect | PM | Reviewers | EM | GovLead | Executive | FlowSP |
|-----|:---------------:|:--:|:---------:|:--:|:-------:|:---------:|:------:|
| Create | None | None | None | None | None | None | **Org** |
| Read | Org | None | None | None | Org | None | Org |
| Write | None | None | None | None | None | None | **Org** |
| Delete | None | None | None | None | None | None | None |

#### gov_sahandoverevent 權限

| 權限 | SystemArchitect | PM | Reviewers | EM | GovLead | Executive | FlowSP |
|-----|:---------------:|:--:|:---------:|:--:|:-------:|:---------:|:------:|
| Create | None | None | None | None | None | None | **Org** |
| Read | Org | None | None | None | Org | None | Org |
| Write | None | None | None | None | None | None | **Org** |
| Delete | None | None | None | None | None | None | None |

#### gov_counterlist 權限

| 權限 | SystemArchitect | PM | Reviewers | EM | GovLead | Executive | FlowSP |
|-----|:---------------:|:--:|:---------:|:--:|:-------:|:---------:|:------:|
| Create | None | None | None | None | None | None | **Org** |
| Read | None | None | None | None | None | None | Org |
| Write | None | None | None | None | None | None | **Org** |
| Delete | None | None | None | None | None | None | None |

### 將安全角色指派給團隊

**操作路徑**：
1. Power Platform admin center → Settings → Teams
2. 選擇團隊（如 GOV-Architects）
3. 點擊 **Manage security roles**
4. 勾選對應的安全角色（如 GOV-SystemArchitect）
5. 點擊 **Save**

**指派對應表**：

| 團隊 | 安全角色 |
|:------------------------------|:------------------------------|
| GOV-Architects | GOV-SystemArchitect |
| GOV-SecurityReviewers | GOV-SecurityReviewer |
| GOV-QAReviewers | GOV-QAReviewer |
| GOV-EngineeringManagement | GOV-EngineeringManagement |
| GOV-GovernanceLead | GOV-GovernanceLead |
| GOV-ExecutiveManagement | GOV-ExecutiveManagement |
| GOV-FlowServicePrincipal | GOV-FlowServicePrincipal |

---

## 種子資料建置

### Counter List 種子資料

**操作步驟**：
1. 使用 System Administrator 帳號
2. Power Apps Maker Portal → Tables → gov_counterlist
3. 選擇 **Data** 標籤
4. 點擊 **+ New row**

**建立以下記錄**：

| CounterName | Current Year | Current Counter | Prefix |
|:---------------------|:--------------|:----------------|:-------|
| RequestID | 2026 | 0 | DR |
| ReviewID | 2026 | 0 | RV |
| RiskID | 2026 | 0 | RISK |
| DocumentID | 2026 | 0 | DOC |
| WaiverID | 2026 | 0 | WVR |
| ViolationID | 2026 | 0 | VIO |
| BOMID | 2026 | 0 | BOM |
| FeedbackID | 2026 | 0 | FB |
| DisputeID | 2026 | 0 | DSP |
| ActionItemID | 2026 | 0 | ACT |
| ProcessLogID | 2026 | 0 | PLG |
| HandoverID | 2026 | 0 | HO |

**重要**：建立後，必須將這些記錄的 Owner 變更為 Flow Service Principal。

**變更 Owner 步驟**：
1. 開啟每筆 Counter List 記錄
2. 點擊 **Assign**
3. 選擇 **User or team**
4. 搜尋 `GOV-FlowServicePrincipal`
5. 點擊 **Assign**

---

## 資料模型準備完成判定（Data Model Ready Gate）

### 本章說明

> **重要：未通過本章所有檢查項目，禁止進入 03-sharepoint-architecture.md。**

### Data Model Ready Gate 檢查清單

#### 資料表建立（第 4 章）

| 檢查項目 | 驗證方法 | 結果 |
|:----------------------------------------------|:----------------------------------------------|:----------|
| [ ] gov_projectregistry 已建立 | Tables 列表可見此資料表 | Pass / Fail |
| [ ] gov_reviewdecisionlog 已建立 | Tables 列表可見此資料表 | Pass / Fail |
| [ ] gov_riskassessmenttable 已建立 | Tables 列表可見此資料表 | Pass / Fail |
| [ ] gov_exceptionwaiverlog 已建立 | Tables 列表可見此資料表 | Pass / Fail |
| [ ] gov_documentregister 已建立 | Tables 列表可見此資料表 | Pass / Fail |
| [ ] gov_governanceviolationlog 已建立 | Tables 列表可見此資料表 | Pass / Fail |
| [ ] gov_counterlist 已建立 | Tables 列表可見此資料表 | Pass / Fail |
| [ ] gov_standardfeedback 已建立 | Tables 列表可見此資料表 | Pass / Fail |
| [ ] gov_disputelog 已建立 | Tables 列表可見此資料表 | Pass / Fail |
| [ ] gov_actionitem 已建立 | Tables 列表可見此資料表 | Pass / Fail |
| [ ] gov_standardsregistry 已建立 | Tables 列表可見此資料表 | Pass / Fail |
| [ ] gov_processlog 已建立 | Tables 列表可見此資料表 | Pass / Fail |
| [ ] gov_externalunit 已建立 | Tables 列表可見此資料表 | Pass / Fail |
| [ ] gov_srcompliancesummary 已建立 | Tables 列表可見此資料表 | Pass / Fail |
| [ ] gov_bomregistry 已建立 | Tables 列表可見此資料表 | Pass / Fail |
| [ ] gov_sahandoverevent 已建立 | Tables 列表可見此資料表 | Pass / Fail |
| [ ] 所有資料表已啟用 Auditing | 每個資料表的 Advanced options 顯示 Enable auditing = On | Pass / Fail |

#### 選項集建立（第 5 章）

| 檢查項目 | 驗證方法 | 結果 |
|:----------------------------------------------|:----------------------------------------------|:----------|
| [ ] 所有 50 個選項集已建立 | Solution → 篩選 Type = Choice，顯示 50 個選項集（含 gov_documentrole, gov_deliverablepackage, gov_handoverstatus 及 15 個新增選項集） | Pass / Fail |
| [ ] 每個選項集的選項值正確 | 逐一開啟確認 | Pass / Fail |

#### Document Baseline Matrix 驗證

| 檢查項目 | 驗證方法 | 結果 |
|:----------------------------------------------|:----------------------------------------------|:----------|
| [ ] gov_projectregistry 包含 15 個 Link 欄位 | Columns 標籤計算 URL 型別欄位數（含 SharePointFolderURL） | Pass / Fail |
| [ ] gov_documentregister 包含 gov_documentrole 欄位 | Columns 標籤可見此欄位且型別為 Choice | Pass / Fail |
| [ ] gov_documentregister 包含 gov_deliverablepackage 欄位 | Columns 標籤可見此欄位且型別為 Choice | Pass / Fail |
| [ ] gov_documentregister 包含 gov_supersededby 欄位 | Columns 標籤可見此欄位且型別為 Lookup | Pass / Fail |

#### 資料表關聯（第 6 章）

| 檢查項目 | 驗證方法 | 結果 |
|:----------------------------------------------|:----------------------------------------------|:----------|
| [ ] gov_reviewdecisionlog → gov_projectregistry 關聯已建立 | Relationships 標籤可見 | Pass / Fail |
| [ ] 關聯的刪除行為為 Restrict | 編輯關聯，Type of behavior = Referential, Restrict Delete | Pass / Fail |
| [ ] gov_standardfeedback → gov_projectregistry 關聯已建立 | Relationships 標籤可見 | Pass / Fail |
| [ ] gov_disputelog → gov_projectregistry 關聯已建立 | Relationships 標籤可見 | Pass / Fail |
| [ ] gov_actionitem → gov_reviewdecisionlog 關聯已建立 | Relationships 標籤可見 | Pass / Fail |
| [ ] gov_processlog → gov_projectregistry 關聯已建立 | Relationships 標籤可見 | Pass / Fail |
| [ ] gov_srcompliancesummary → gov_projectregistry 關聯已建立 | Relationships 標籤可見 | Pass / Fail |

#### Flow-only 欄位保護（第 7, 8 章）

| 檢查項目 | 驗證方法 | 結果 |
|:----------------------------------------------|:----------------------------------------------|:----------|
| [ ] 所有 Flow-only 欄位已啟用 Column Security | 每個欄位的 Advanced options → Enable column security = On | Pass / Fail |
| [ ] GOV-FlowOnly-ReadWrite Profile 已建立 | Field security profiles 列表可見 | Pass / Fail |
| [ ] GOV-FlowOnly-ReadOnly Profile 已建立 | Field security profiles 列表可見 | Pass / Fail |
| [ ] Flow Service Principal 已指派至 ReadWrite Profile | Profile → Users 標籤顯示 | Pass / Fail |
| [ ] 所有 GOV 團隊已指派至 ReadOnly Profile | Profile → Teams 標籤顯示 6 個團隊 | Pass / Fail |

#### Field-Level Security 功能測試

| 檢查項目 | 驗證方法 | 結果 |
|:----------------------------------------------|:----------------------------------------------|:----------|
| [ ] 人類使用者無法修改 Flow-only 欄位 | 測試 FLS-002 執行結果 | Pass / Fail |
| [ ] 人類使用者可讀取 Flow-only 欄位 | 測試 FLS-003 執行結果 | Pass / Fail |

#### 安全角色（第 11 章）

| 檢查項目 | 驗證方法 | 結果 |
|:----------------------------------------------|:----------------------------------------------|:----------|
| [ ] 8 個安全角色已建立 | Security roles 列表顯示 | Pass / Fail |
| [ ] 各團隊已指派正確的安全角色 | 每個團隊 → Manage security roles | Pass / Fail |
| [ ] 人類角色無 Create 權限（事件資料表） | 安全角色設定確認 | Pass / Fail |
| [ ] GovLead 有 User 級 Create/Write（參考資料表） | gov_standardsregistry, gov_externalunit, gov_srcompliancesummary 安全角色確認 | Pass / Fail |
| [ ] Flow SP 角色有完整權限 | 安全角色設定確認 | Pass / Fail |
| [ ] 7 個新資料表的安全角色矩陣已設定 | 逐一比對權限矩陣 | Pass / Fail |

#### 種子資料（第 12 章）

| 檢查項目 | 驗證方法 | 結果 |
|:----------------------------------------------|:----------------------------------------------|:----------|
| [ ] Counter List 有 12 筆記錄 | 查詢 gov_counterlist 記錄數 | Pass / Fail |
| [ ] Counter List 記錄的 Owner 為 Flow SP | 每筆記錄的 Owner 欄位確認 | Pass / Fail |

### Gate 通過判定

**通過條件**：上述所有檢查項目的結果皆為 Pass。

### Data Model Ready Gate 簽核

```
Data Model Ready Gate 簽核記錄
=============================
檢查日期：____年____月____日
檢查者：________________（姓名 + 職稱）

檢查結果摘要：
- 資料表建立：____ / 17 項通過
- 選項集建立：____ / 2 項通過
- Document Baseline Matrix 驗證：____ / 4 項通過
- 資料表關聯：____ / 7 項通過
- Flow-only 欄位保護：____ / 5 項通過
- FLS 功能測試：____ / 2 項通過
- 安全角色：____ / 6 項通過
- 種子資料：____ / 2 項通過

總計：____ / 45 項通過

Gate 判定：[ ] 通過  [ ] 未通過

若通過，已授權進入 03-sharepoint-architecture.md

簽核者簽名：________________
簽核日期：____年____月____日
```

---

## 附錄：故障排解

### Column Security 啟用後欄位消失

**症狀**：啟用 Column Security 後，使用者看不到該欄位

**原因**：使用者未被指派至任何包含該欄位的 Field Security Profile

**解決方法**：
1. 確認使用者所屬團隊已指派至 GOV-FlowOnly-ReadOnly Profile
2. 確認 Profile 中該欄位的 Read 權限為 Yes
3. 等待 15 分鐘讓權限生效

### Flow 無法寫入 Flow-only 欄位

**症狀**：Power Automate Flow 執行時出現權限錯誤

**原因**：Flow 未使用 Service Principal 執行，或 Service Principal 未指派至 ReadWrite Profile

**解決方法**：
1. 確認 Flow 的 Connection 使用 Service Principal
2. 確認 Service Principal 已指派至 GOV-FlowOnly-ReadWrite Profile
3. 確認 Service Principal 的安全角色有 Write 權限

### Restrict Delete 無法設定

**症狀**：無法將關聯的刪除行為設為 Restrict

**原因**：可能已有違反 Restrict 條件的資料存在

**解決方法**：
1. 先刪除所有測試資料
2. 再設定 Restrict Delete
3. 或使用 Solution 匯入預先設定好的關聯

---

## 附錄：版本歷史

| 版本 | 日期 | 變更說明 |
|:--------|:------------|:----------------------------------------------|
| v1.0 | 2026-01-28 | 初版建立 |
| v2.0 | 2026-01-28 | 新增 Record Owner 策略、非授權修改偵測、違規事件模型、FLS 實作步驟 |
| v2.1 | 2026-02-09 | 新增 BOM Registry 資料表 |
| v2.2 | 2026-02-11 | 鑑識修訂：新增 Document Register 凍結欄位（gov_isfrozen, gov_frozendate）、SA Handover Event 資料表、DocumentType 補齊 3 值（DesignObjectInventory, ChangeImpact, DocumentRegister）、Counter List 新增 BOMID 種子記錄、修正 Gate 參考檔名、版本歷史補齊 |
| v2.3 | 2026-02-11 | 日常流程修訂：(1) gov_projectregistry 新增 4 個 Link 欄位（RequirementTraceability, DesignObjectInventory, DocumentRegister, ChangeImpact）；(2) gov_documentregister 新增 3 個欄位（gov_documentrole, gov_deliverablepackage, gov_supersededby）；(3) 新增 gov_documentrole 選項集（6 值：Planned/Draft/Active/Superseded/Approved/Frozen）；(4) 新增 gov_deliverablepackage 選項集（3 值：CoreDeliverable/SupplementaryDeliverable/AdHoc）；(5) 新增 Document Baseline Matrix 章節（單一權威文件基線矩陣，16 列映射）；(6) Flow-only 欄位清單更新；(7) Data Model Ready Gate 檢查清單更新（25→29 項） |
| v2.4 | 2026-03-05 | KPI 證據採集支援：新增 7 資料表（gov_standardfeedback, gov_disputelog, gov_actionitem, gov_standardsregistry, gov_processlog, gov_externalunit, gov_srcompliancesummary）、15 個新選項集、gov_reviewdecisionlog 新增 SL Decision 欄位、gov_projectregistry 新增 Rework Reason Category、6 個新關聯、7 個新安全矩陣、4 個新 Counter 種子 |

---

## 本章完成摘要

**完成本章後，您現在具備**：

| 項目 | 狀態 |
|:----------------------------------------------|:----------|
| 16 個治理核心資料表 | 已建立 |
| 所有資料表欄位（含 Flow-only 欄位標記） | 已定義 |
| 50 個選項集（Choice）含 gov_documentrole, gov_deliverablepackage, gov_handoverstatus 及 15 個新增選項集 | 已建立 |
| Document Baseline Matrix（單一權威文件基線矩陣） | 已定義 |
| 資料表關聯性 | 已建立 |
| Field-Level Security Profile | 已設定 |
| Flow-only 欄位保護 | 已啟用 |
| 安全角色 | 已建立並指派 |
| 種子資料（Counter List，12 筆） | 已建立 |
| Data Model Ready Gate（45 項檢查） | 已通過 |

**此刻您不需要做的事**：

- 不需要建立 Power Automate Flow（第 05 章）
- 不需要建立 Power Apps（第 04 章）
- 不需要測試完整的端對端流程（第 07 章）

**待第 05 章完成後返回執行**：

- 驗證 Flow Owner 設定是否正確
- 驗證 Record Owner 強制為 Flow Service Principal

**下一章將完成**：

- SharePoint 網站權限精細設定
- 文件庫結構建立
- Document Freeze 機制概念說明

---

**文件結束**

**下一步**：通過 Data Model Ready Gate 後，請繼續參閱 [03-sharepoint-architecture.md](03-sharepoint-architecture.md) 進行 SharePoint 架構建置。
