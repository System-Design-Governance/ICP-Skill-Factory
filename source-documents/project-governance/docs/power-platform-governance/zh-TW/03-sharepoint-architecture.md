# SharePoint 架構與文件管理建置指南

**文件版本**：v2.2
**建立日期**：2026-01-29
**最後更新**：2026-02-11
**適用系統**：Design Governance System（Dataverse 架構）
**前置文件**：01-prerequisites-and-environment.md、02-dataverse-data-model-and-security.md
**後續文件**：04-powerapps-forms.md

---


## 治理核心原則聲明

### 不可違反之治理憲章

本章節定義 SharePoint 架構必須遵守之治理原則。以下原則**不可被任何角色、情境或緊急理由推翻**。

---

#### 原則一：Dataverse 為唯一治理真相來源

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  治理真相來源（Source of Truth）宣告                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ✓ Dataverse 為唯一治理真相來源                                              │
│  ✗ SharePoint 不承擔任何治理狀態或決策職責                                    │
│                                                                             │
│  所有治理判斷依據：                                                           │
│  - 專案狀態 → Dataverse Project Registry                                    │
│  - 文件狀態 → Dataverse Document Register                                   │
│  - 審批記錄 → Dataverse Review Decision Log                                 │
│  - 凍結狀態 → Dataverse Document Register.IsFrozen                          │
│                                                                             │
│  SharePoint 檔案之存在與否，不構成治理事實之依據。                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

#### 原則二：SharePoint 僅負責檔案儲存

| 職責範圍 | SharePoint | Dataverse |
|:--------|:-----------|:----------|
| 檔案實體儲存 | **✓ 負責** | ✗ 不負責 |
| 檔案版本歷程 | **✓ 負責** | ✗ 不負責 |
| 文件治理狀態 | ✗ 不負責 | **✓ 負責** |
| 文件審查狀態 | ✗ 不負責 | **✓ 負責** |
| 文件凍結判定 | ✗ 不負責 | **✓ 負責** |
| 專案 Gate 狀態 | ✗ 不負責 | **✓ 負責** |

**禁止事項**：
- 不得以 SharePoint 檔案屬性作為治理判斷依據
- 不得以 SharePoint 資料夾存在與否作為 Gate 通過條件
- 不得以 SharePoint 檔案修改日期作為文件版本依據

---

#### 原則三：正式專案檔案寫入權專屬 Flow Service Principal

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  寫入權限宣告                                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  正式專案資料夾（/Documents/{RequestID}/）之寫入權限：                        │
│                                                                             │
│  ✓ Flow Service Principal    → Contribute（唯一可寫入之主體）               │
│  ✗ Governance Lead          → Read（不得寫入）                              │
│  ✗ System Architect         → Read（不得寫入）                              │
│  ✗ 任何人類帳號              → Read（不得寫入）                              │
│                                                                             │
│  此原則無例外。                                                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

#### 原則四：人類帳號不得直接寫入正式治理資料夾

**明確禁止清單**：

| 禁止行為 | 違規後果 |
|:--------|:--------|
| 人類帳號拖曳檔案至專案資料夾 | 權限系統拒絕 |
| 人類帳號使用 SharePoint API 上傳 | 權限系統拒絕 |
| 人類帳號以任何方式寫入正式資料夾 | 權限系統拒絕 |
| 管理員帳號繞過權限寫入 | GOV-017 偵測、記錄違規、移至隔離區 |

**無論職位高低、緊急程度、業務需求，人類帳號直接寫入正式專案資料夾之行為，一律視為治理違規。**

---

#### 原則五：例外處理必須透過正式流程

```
緊急或例外情境處理原則：

1. 人類帳號不得以「緊急」為由直接上傳
2. 緊急文件處理必須透過 FORM-011 Emergency Document Request
3. 緊急文件之寫入仍由 Flow Service Principal 執行
4. 緊急處理全程留下稽核軌跡

不存在「人工補上傳」之合法操作路徑。
```

---

### 原則違反之後果

| 違反行為 | 偵測機制 | 系統回應 |
|:--------|:--------|:--------|
| 人類帳號嘗試寫入正式資料夾 | SharePoint 權限系統 | 拒絕寫入 |
| 管理員繞過權限寫入 | GOV-017 孤兒檔案偵測 | 移至隔離區、記錄違規、通知 |
| 直接修改 SharePoint 檔案屬性 | GOV-018 一致性檢查 | 偵測不一致、發出警報 |

---

## SharePoint 在治理架構中的定位

### 架構層次圖

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              治理系統架構                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                      表現層（Presentation Layer）                     │   │
│  │  Power Apps Forms (FORM-001 ~ FORM-011) │ Power BI Dashboards        │   │
│  │  （人類互動入口）                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    ▼                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                       邏輯層（Logic Layer）                           │   │
│  │              Power Automate Flows (GOV-001 ~ GOV-018)                │   │
│  │              （唯一具備治理資料寫入權之執行者）                         │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                          │                     │                            │
│                          ▼                     ▼                            │
│  ┌─────────────────────────────┐   ┌─────────────────────────────┐         │
│  │   治理真相來源               │   │   檔案儲存層                 │         │
│  │   Dataverse                 │   │   SharePoint                │         │
│  │   ─────────────────────     │   │   ─────────────────────     │         │
│  │   • Project Registry        │   │   • Documents Library       │         │
│  │   • Review Decision Log     │ ← │   • 專案資料夾（唯讀）       │         │
│  │   • Document Register       │   │   • 檔案版本歷程            │         │
│  │   • 所有治理狀態欄位         │   │   （不承擔治理職責）         │         │
│  └─────────────────────────────┘   └─────────────────────────────┘         │
│           ▲                                                                 │
│           │                                                                 │
│    治理判斷唯一依據                                                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### SharePoint 職責邊界

**SharePoint 負責**：

| 職責 | 說明 |
|:----|:----|
| 檔案實體儲存 | 儲存 PDF、Word、Excel 等文件檔案 |
| 版本歷程保留 | 透過 SharePoint 內建版本控制保留修改歷程 |
| 檔案預覽 | 提供線上預覽功能 |
| 檔案下載 | 提供檔案下載功能 |

**SharePoint 不負責**：

| 項目 | 正確來源 |
|:----|:--------|
| 文件是否完成上傳 | Dataverse Document Register 記錄存在與否 |
| 文件審查狀態 | Dataverse Document Register.ReviewStatus |
| 文件是否凍結 | Dataverse Document Register.IsFrozen |
| 文件類型 | Dataverse Document Register.DocumentType |
| 專案是否具備必要文件 | Dataverse Project Registry 對應欄位 |

---

## SharePoint 網站建立

### 建立治理專用網站

**操作路徑**：
1. 開啟瀏覽器，前往：`https://[租戶].sharepoint.com`
2. 點擊 **+ Create site**
3. 選擇 **Team site**

**網站設定**：

| 設定欄位 | 設定值 |
|:--------|:------|
| Site name | `Design Governance` |
| Group email address | `design-governance` |
| Site address | `design-governance` |
| Privacy settings | **Private - only members can access** |
| Language | Chinese (Traditional) 或 English |

### 記錄網站關鍵資訊

**建立完成後，記錄以下資訊**：

```
SharePoint 網站資訊記錄
========================
網站名稱：Design Governance
網站 URL：https://[租戶].sharepoint.com/sites/design-governance
文件庫 URL：https://[租戶].sharepoint.com/sites/design-governance/Shared%20Documents
Site ID：[使用 API 取得]
Library ID：[使用 API 取得]
```

### 取得 Site ID 與 Library ID

**使用 SharePoint REST API**：

```
Site ID：
GET https://[租戶].sharepoint.com/sites/design-governance/_api/site/id

Library ID：
GET https://[租戶].sharepoint.com/sites/design-governance/_api/web/lists/getbytitle('Documents')/id
```

**使用 PnP PowerShell**：

```powershell
Connect-PnPOnline -Url "https://[租戶].sharepoint.com/sites/design-governance" -Interactive

$site = Get-PnPSite -Includes Id
Write-Host "Site ID: $($site.Id)"

$lib = Get-PnPList -Identity "Documents"
Write-Host "Library ID: $($lib.Id)"
```

---

## 文件庫結構與設定

### 使用預設文件庫

**決策**：使用 SharePoint 建立時自動產生之「Documents」文件庫。

| 設定 | 值 |
|:----|:--|
| 文件庫名稱 | Documents |
| 內部名稱 | Shared Documents |
| URL 路徑 | /sites/design-governance/Shared%20Documents |

### 版本控制設定

**操作路徑**：
1. 進入 Documents 文件庫
2. 齒輪圖示 → **Library settings** → **Versioning settings**

**設定值**：

| 設定欄位 | 設定值 |
|:--------|:------|
| Content Approval | **No** |
| Document Version History | **Create major versions** |
| Keep the following number of major versions | **500** |
| Require documents to be checked out | **No** |

### 建立隔離區資料夾

**操作路徑**：
1. 進入 Documents 文件庫
2. 點擊 **+ New** → **Folder**
3. 輸入名稱：`_Quarantine`

**隔離區用途**：
- 存放 GOV-017 偵測到之孤兒檔案
- 存放人類帳號緊急上傳之暫存檔案（需後續正規化）
- 隔離區檔案不具治理效力

**隔離區權限**：

| 主體 | 權限 |
|:----|:----|
| GOV-GovernanceLead | Contribute |
| GOV-Architects | Contribute |
| Flow Service Principal | Contribute |
| 其他群組 | 無存取權限 |

---

## 資料夾結構設計原則

### 專案資料夾命名規則

```
資料夾命名格式：{RequestID}

範例：
/Documents/
├── _Quarantine/              ← 隔離區（人類可寫入，不具治理效力）
├── DR-2026-0001/             ← 正式專案資料夾（僅 Flow 可寫入）
│   ├── 01_Feasibility/
│   ├── 02_Risk_Assessment/
│   ├── 03_Design/
│   ├── 04_Security/
│   ├── 05_Test/
│   └── 06_Handover/
├── DR-2026-0002/
│   └── ...
```

### 子資料夾定義

| 序號 | 資料夾名稱 | 儲存分類 | 說明 |
|:----|:----------|:--------|:----|
| 01 | `01_Feasibility` | 可行性評估 | 專案啟動階段文件 |
| 02 | `02_Risk_Assessment` | 風險評估 | 風險相關文件 |
| 03 | `03_Design` | 設計文件 | 架構與設計文件 |
| 04 | `04_Security` | 安全文件 | 安全評估與檢查表 |
| 05 | `05_Test` | 測試文件 | 測試報告與追溯 |
| 06 | `06_Handover` | 交接文件 | 專案完成交接文件 |

### 資料夾建立方式

**資料夾建立權責**：

| 資料夾類型 | 建立方式 | 建立時機 |
|:----------|:--------|:--------|
| 專案根目錄 | GOV-001 Flow | 專案建立時 |
| 6 個子資料夾 | GOV-001 Flow | 專案建立時 |
| _Quarantine | 手動建立 | 系統初始化時 |

**禁止事項**：
- 禁止人工手動建立專案資料夾
- 禁止人工手動建立子資料夾
- 禁止人工重新命名資料夾

---

## DocumentType 與 SharePoint Folder 對應關係

### 設計原則：解耦合

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DocumentType 與 SharePoint Folder 對應原則                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  DocumentType = 治理語意分類（Dataverse 定義）                               │
│  SharePoint Folder = 實體儲存分類（檔案組織）                                │
│                                                                             │
│  二者非必然一對一對應。                                                       │
│                                                                             │
│  設計目標：                                                                  │
│  • 新增 DocumentType 時，不需修改 SharePoint 資料夾結構                      │
│  • 新增 Gate 時，不需修改 SharePoint 資料夾結構                              │
│  • SharePoint 資料夾結構穩定，不因治理規則演進而重構                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### DocumentType 定義（Dataverse）

| DocumentType | 中文名稱 | 說明 |
|:------------|:--------|:----|
| TechnicalFeasibility | 技術可行性評估 | 專案技術可行性分析 |
| InitialRiskList | 初步風險清單 | 專案初始風險識別 |
| RiskAssessmentStrategy | 風險評估策略 | 風險評估方法論 |
| DesignBaseline | 設計基線文件 | 架構設計基準 |
| RiskAssessment | 風險評估報告 | 完整風險評估結果 |
| IEC62443Checklist | IEC 62443 檢查表 | 安全標準符合性 |
| ThreatModel | 威脅模型分析 | 安全威脅建模 |
| RequirementTraceability | 需求追溯矩陣 | 需求與實作對應 |
| DocumentRegister | 文件清冊 | 專案文件索引 |
| DesignObjectInventory | 設計標的清冊 | 設計物件盤點 |
| ChangeImpact | 變更影響分析 | 變更影響評估 |
| TestReport | 測試報告 | 測試結果紀錄 |
| HandoverMeeting | 交接會議紀錄 | 專案交接紀錄 |
| ResidualRiskList | 殘餘風險清單 | 殘餘風險盤點 |

### SharePoint Folder 定義（實體儲存）

| Folder | 儲存分類 |
|:-------|:--------|
| 01_Feasibility | 可行性相關 |
| 02_Risk_Assessment | 風險相關 |
| 03_Design | 設計相關 |
| 04_Security | 安全相關 |
| 05_Test | 測試相關 |
| 06_Handover | 交接相關 |

### 對應關係表

> **重要**：此對應關係的**唯一權威來源**為 Doc 02（02-dataverse-data-model-and-security.md）中的 **Document Baseline Matrix** 章節。
> 本表為該矩陣的快速參考副本。若有不一致，以 Doc 02 Baseline Matrix 為準。

| DocumentType | 預設存放 Folder | 說明 |
|:------------|:---------------|:----|
| TechnicalFeasibility | 01_Feasibility | 可行性階段 |
| InitialRiskList | 01_Feasibility | 可行性階段 |
| RiskAssessmentStrategy | 01_Feasibility | 可行性階段 |
| DesignBaseline | 03_Design | 設計文件 |
| RiskAssessment | 02_Risk_Assessment | 風險評估 |
| IEC62443Checklist | 04_Security | 安全文件 |
| ThreatModel | 04_Security | 安全文件 |
| RequirementTraceability | 03_Design | 設計文件 |
| TestPlan | 05_Test | 測試文件 |
| TestReport | 05_Test | 測試文件 |
| HandoverMeeting | 06_Handover | 交接文件 |
| ResidualRiskList | 06_Handover | 交接文件 |
| Other | 01_Feasibility | 未分類文件 |
| DesignObjectInventory | 03_Design | 設計文件 |
| ChangeImpact | 03_Design | 設計文件 |
| DocumentRegister | 06_Handover | 交接文件 |

### 對應關係之可擴展性

**新增 DocumentType 時**：
- 於 Doc 02 的 Document Baseline Matrix 新增映射（**唯一修改點**）
- 於 Dataverse 新增 DocumentType Choice 值
- SharePoint 資料夾結構無需變更
- 本文件的對應關係表將自動跟隨 Doc 02 更新

**新增 Gate 時**：
- 於 Dataverse 調整 Gate 定義
- 調整 Flow 前置條件檢查邏輯
- SharePoint 資料夾結構無需變更

**對應關係調整時**：
- 僅需修改對應表
- 現有檔案保留於原位置
- 新檔案依新對應表存放

---

## 權限架構設計

### 權限設計總則

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  SharePoint 權限設計總則                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  正式專案資料夾（/Documents/{RequestID}/）：                                 │
│  ─────────────────────────────────────────                                  │
│  • Flow Service Principal → Contribute（唯一寫入者）                        │
│  • 所有人類帳號 → Read（僅讀取）                                            │
│                                                                             │
│  隔離區（/Documents/_Quarantine/）：                                        │
│  ────────────────────────────────                                          │
│  • Flow Service Principal → Contribute                                     │
│  • GOV-GovernanceLead → Contribute                                         │
│  • GOV-Architects → Contribute                                             │
│  • 其他 → 無存取                                                            │
│                                                                             │
│  隔離區檔案不具治理效力。                                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 網站層級權限

**操作路徑**：
1. 網站首頁 → 齒輪圖示 → **Site permissions**
2. 點擊 **Advanced permissions settings**

**權限設定**：

| Entra ID 群組 | SharePoint 權限層級 |
|:-------------|:------------------|
| GOV-Architects | **Read** |
| GOV-SecurityReviewers | **Read** |
| GOV-QAReviewers | **Read** |
| GOV-EngineeringManagement | **Read** |
| GOV-GovernanceLead | **Read** |
| GOV-ExecutiveManagement | **Read** |
| Flow Service Principal | **Contribute** |

### 專案資料夾權限（GOV-001 設定）

**GOV-001 Flow 於建立專案時執行以下權限設定**：

**Step 1：中斷權限繼承**

```
POST /_api/web/GetFolderByServerRelativeUrl('/sites/design-governance/Shared Documents/{RequestID}')/ListItemAllFields/BreakRoleInheritance(copyRoleAssignments=false, clearSubscopes=true)
```

**Step 2：授予 Flow Service Principal Contribute 權限**

```
POST /_api/web/GetFolderByServerRelativeUrl('/sites/design-governance/Shared Documents/{RequestID}')/ListItemAllFields/RoleAssignments/AddRoleAssignment(principalId={FlowServicePrincipalId}, roleDefId={ContributeRoleId})
```

**Step 3：授予所有群組 Read 權限**

```
對每個群組執行：
POST /_api/web/GetFolderByServerRelativeUrl('/sites/design-governance/Shared Documents/{RequestID}')/ListItemAllFields/RoleAssignments/AddRoleAssignment(principalId={GroupId}, roleDefId={ReadRoleId})

目標群組：
- GOV-Architects
- GOV-SecurityReviewers
- GOV-QAReviewers
- GOV-EngineeringManagement
- GOV-GovernanceLead
- GOV-ExecutiveManagement
```

### 權限設定後之效果

**正式專案資料夾權限矩陣**：

| 主體 | Create | Read | Update | Delete |
|:----|:-------|:----|:-------|:-------|
| Flow Service Principal | ✓ | ✓ | ✓ | ✓ |
| GOV-GovernanceLead | ✗ | ✓ | ✗ | ✗ |
| GOV-Architects | ✗ | ✓ | ✗ | ✗ |
| GOV-SecurityReviewers | ✗ | ✓ | ✗ | ✗ |
| GOV-QAReviewers | ✗ | ✓ | ✗ | ✗ |
| GOV-EngineeringManagement | ✗ | ✓ | ✗ | ✗ |
| GOV-ExecutiveManagement | ✗ | ✓ | ✗ | ✗ |

**Governance Lead 權限說明**：
- Governance Lead 對正式專案資料夾**僅具備 Read 權限**
- Governance Lead 不得直接上傳檔案至正式資料夾
- Governance Lead 之緊急處理需透過 FORM-011 流程

### 角色定義 ID 取得

**操作路徑**：
```
GET https://[租戶].sharepoint.com/sites/design-governance/_api/web/roledefinitions
```

**常用角色 ID**：

| 角色名稱 | 預設 ID |
|:--------|:-------|
| Full Control | 1073741829 |
| Contribute | 1073741827 |
| Read | 1073741826 |

---

## 直接上傳之禁止與偵測

### 直接上傳之定義

**直接上傳**係指以下行為：
- 人類帳號於 SharePoint UI 拖曳檔案至專案資料夾
- 人類帳號使用 SharePoint REST API 寫入專案資料夾
- 人類帳號使用任何工具繞過 Flow 寫入專案資料夾

### 直接上傳之治理問題

| 問題 | 說明 |
|:----|:----|
| Document Register 無記錄 | Dataverse 中無對應記錄，治理狀態不完整 |
| 審計軌跡缺失 | 無法追溯上傳者、上傳時間、上傳原因 |
| 版本控制失效 | 無法追蹤治理版本歷程 |
| Gate Pre-check 失敗 | 系統無法識別該檔案為有效文件 |

### 第一道防線：權限系統阻擋

**機制**：SharePoint 資料夾權限設定

**效果**：
- 人類帳號嘗試上傳時，SharePoint 回傳權限不足錯誤
- 使用者看到訊息：「您沒有權限將檔案上傳至此位置」

**涵蓋範圍**：
- 所有一般人類帳號
- 所有治理群組成員（含 Governance Lead）

### 第二道防線：GOV-017 孤兒檔案偵測

**執行頻率**：每小時

**偵測邏輯**：

```
對 SharePoint 所有專案資料夾中的檔案：
    若 Dataverse Document Register 中無對應記錄：
        → 該檔案為孤兒檔案
        → 移動至 _Quarantine 資料夾
        → 寫入 Governance Violation Log
        → 發送通知給 Governance Lead
```

**適用情境**：
- 管理員帳號繞過權限寫入（Site Collection Admin）
- 權限設定錯誤導致漏洞
- 系統異常導致未預期寫入

### 第三道防線：GOV-018 一致性檢查

**執行頻率**：每日

**檢查項目**：
- Document Register 記錄之 SharePoint 檔案是否存在
- SharePoint 檔案是否與 Document Register 記錄一致
- 專案資料夾結構是否完整

---

## 緊急與例外文件處理流程

### 設計原則

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  緊急與例外處理原則                                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  即使在緊急情況下：                                                          │
│  • 人類帳號不得直接寫入正式專案資料夾                                        │
│  • 檔案寫入仍必須由 Flow Service Principal 執行                              │
│  • 全程必須留下稽核軌跡                                                      │
│                                                                             │
│  不存在「人工補上傳」之合法操作路徑。                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 緊急文件處理流程

**流程名稱**：Emergency Document Request（緊急文件申請）

**使用情境**：
- 正常 Document Upload 流程因故無法使用
- 需於短時間內完成文件上傳

**流程步驟**：

```
Step 1：人類帳號上傳檔案至隔離區
────────────────────────────────
位置：/Documents/_Quarantine/
說明：隔離區允許人類帳號寫入，但檔案不具治理效力

Step 2：人類帳號提交 FORM-011 Emergency Document Request
────────────────────────────────────────────────────────
必填欄位：
- ProjectId（關聯專案）
- DocumentType（文件類型）
- QuarantineFilePath（隔離區檔案路徑）
- EmergencyReason（緊急原因，最少 50 字）
- RequestedBy（申請者）

Step 3：GOV-011 Flow 執行
────────────────────────
驗證步驟：
1. 驗證隔離區檔案存在
2. 驗證專案存在且狀態為 Active
3. 驗證文件類型有效

執行步驟：
1. 將檔案從隔離區移動至正式資料夾（由 Flow 執行）
2. 建立 Document Register 記錄
3. 更新 Project Registry 對應欄位
4. 寫入 Review Decision Log（記錄緊急處理）
5. 刪除隔離區原檔案
6. 發送通知

Step 4：稽核記錄
───────────────
Emergency Document Request 全程記錄於：
- Review Decision Log（ReviewType = EmergencyDocumentUpload）
- Governance Violation Log（ViolationType = EmergencyProcedure）
```

### 例外情況處理

**情況一：正常流程無法使用**

| 步驟 | 說明 |
|:----|:----|
| 1 | 人類帳號將檔案上傳至 _Quarantine |
| 2 | 提交 FORM-011 Emergency Document Request |
| 3 | Flow 驗證並執行正規化處理 |

**情況二：Gate 3 後需修改凍結文件**

| 步驟 | 說明 |
|:----|:----|
| 1 | 提交 FORM-008 Document Unfreeze Exception |
| 2 | 經雙層審批核准後，Flow 解除凍結 |
| 3 | 透過正常 Document Upload 流程上傳修正版本 |
| 4 | Flow 重新執行文件凍結 |

### 禁止之行為

| 禁止行為 | 說明 |
|:--------|:----|
| 以緊急為由直接上傳正式資料夾 | 權限系統阻擋，無法執行 |
| 請 IT Admin 代為上傳 | 違反治理原則，將被 GOV-017 偵測 |
| 事後「補上傳」已繞過之檔案 | 不存在合法路徑 |
| 修改 SharePoint 權限以允許上傳 | 違反治理原則，將被記錄為違規 |

---

## SharePoint 與 Dataverse 連結機制

### 連結架構

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        SharePoint-Dataverse 連結架構                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   SharePoint                           Dataverse                            │
│   ──────────                           ─────────                            │
│                                                                             │
│   /DR-2026-0001/                       Document Register                    │
│   └── 03_Design/                       ┌─────────────────────────────────┐ │
│       └── DesignBaseline_v1.0.pdf ───► │ DocumentID: DOC-...             │ │
│                                        │ SharePointFileLink: (URL)       │ │
│                                        │ ParentProject: DR-2026-0001     │ │
│                                        │ DocumentType: DesignBaseline    │ │
│                                        │ ReviewStatus: Approved          │ │
│                                        │ IsFrozen: No                    │ │
│                                        └─────────────────────────────────┘ │
│                                                    │                        │
│                                                    ▼                        │
│                                        Project Registry                     │
│                                        ┌─────────────────────────────────┐ │
│                                        │ RequestID: DR-2026-0001         │ │
│                                        │ DesignBaselineLink: (URL)       │ │
│                                        └─────────────────────────────────┘ │
│                                                                             │
│   治理判斷依據：Dataverse 記錄                                               │
│   SharePoint 檔案存在與否不影響治理判斷                                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Document Register 欄位

| 欄位名稱 | Schema Name | 類型 | 說明 |
|:--------|:-----------|:----|:----|
| Document ID | gov_documentid | Text | 文件唯一識別碼 |
| Parent Project | gov_parentproject | Lookup | 關聯至 Project Registry |
| Document Type | gov_documenttype | Choice | 文件類型 |
| Document Name | gov_documentname | Text | 文件顯示名稱 |
| Document Version | gov_documentversion | Text | 版本號 |
| SharePoint File Link | gov_sharepointfilelink | URL | SharePoint 檔案 URL |
| Uploaded By | gov_uploadedby | Lookup (User) | 上傳者 |
| Uploaded Date | gov_uploadeddate | DateTime | 上傳時間 |
| Review Status | gov_reviewstatus | Choice | 審查狀態 |
| Is Frozen | gov_isfrozen | Boolean | 是否凍結 |
| Frozen Date | gov_frozendate | DateTime | 凍結時間 |
| Document Role | gov_documentrole | Choice | 版本生命週期狀態（Planned/Draft/Active/Superseded/Approved/Frozen） |
| Deliverable Package | gov_deliverablepackage | Choice | 交付物包裝類型（CoreDeliverable/SupplementaryDeliverable/AdHoc） |
| Superseded By | gov_supersededby | Lookup | 指向取代本文件的新版本記錄 |

> **完整欄位定義請參閱 Doc 02 第 4 章 gov_documentregister。**

### 連結建立流程（GOV-005）

> **重要**：GOV-005 已改為 **Base64 上傳模式**。使用者不再需要提供 SharePoint 檔案連結。
> 完整施工步驟請參閱 Doc 05（05-core-flows-implementation-runbook.md）。

**GOV-005 Document Upload and Register 執行步驟**：

```
Step 1：驗證輸入
────────────────
- 驗證專案存在
- 驗證專案未凍結（IsFrozen ≠ true）
- 驗證 DocumentType 有效
- 接收 Base64 檔案內容（從 Power Apps 表單）

Step 2：上傳至 SharePoint
─────────────────────────
- 查閱 Doc 02 Baseline Matrix 取得 SharePointFolder
- 上傳檔案至 {ProjectFolder}/{SharePointFolder}/{FileName}
- 取得上傳後的 SharePoint URL

Step 3：版本推進（Version Progression）
───────────────────────────────────────
- 查詢同專案、同 DocumentType 的現有 Active 記錄
- 若存在 Active 記錄：標記為 Superseded，設定 SupersededBy 指向新記錄
- 新記錄設為 DocumentRole = Draft

Step 4：產生 DocumentID 並建立 Document Register 記錄
───────────────────────────────────────────────────
- 格式：DOC-{RequestID}-{DocumentType}-{序號}
- 寫入所有欄位（含 SharePointFileLink、DocumentRole、DeliverablePackage）

Step 5：更新 Project Registry Link
──────────────────────────────────
- 查閱 Baseline Matrix 取得 ProjectRegistryLinkField
- Link 目標規則：優先選最新 Approved，次選最新 Active Draft
- 更新對應 {DocumentType}Link 欄位

Step 6：發送通知
───────────────
- 通知文件審查者
```

---

## 文件凍結機制

### 凍結觸發條件

**觸發時機**：Gate 3 通過後自動執行

**觸發鏈**：
```
Gate 3 Approved → GOV-003 → 呼叫 GOV-014 Document Freeze
```

### 凍結執行步驟（GOV-014）

**Step 1：更新 Dataverse 凍結狀態**

```
更新 Project Registry：
- DocumentFreezeStatus = "Frozen"
- DocumentFreezeDate = utcNow()

更新所有相關 Document Register：
- IsFrozen = true
- FrozenDate = utcNow()
```

**Step 2：移除 SharePoint 寫入權限**

```
移除 Flow Service Principal 的 Contribute 權限
授予 Flow Service Principal Read 權限

結果：所有主體對專案資料夾皆為 Read 權限
```

**Step 3：寫入稽核記錄**

```
寫入 Review Decision Log：
- ReviewType = "DocumentFreeze"
- Decision = "Executed"
- ApprovedBy = "Flow Service Principal"
```

### 凍結後權限狀態

| 主體 | 凍結前 | 凍結後 |
|:----|:------|:------|
| Flow Service Principal | Contribute | **Read** |
| 所有人類帳號 | Read | Read |

### 解凍流程

**解凍必須透過 FORM-008 Document Unfreeze Exception**：
1. System Architect 提交 FORM-008
2. Governance Lead 審批
3. Engineering Management 審批
4. GOV-008 執行解凍
5. 更新 Dataverse 凍結狀態
6. 恢復 Flow Service Principal Contribute 權限

---

## SharePoint 架構準備完成判定

### 檢查清單

**類別 A：網站與文件庫（5 項）**

| 檢查項目 | 驗證方式 | 結果 |
|:--------|:--------|:----|
| [ ] SharePoint 網站已建立 | 瀏覽器可存取 | Pass / Fail |
| [ ] 網站 URL 已記錄 | 記錄表已填寫 | Pass / Fail |
| [ ] Site ID 已取得 | 記錄表已填寫 | Pass / Fail |
| [ ] Documents 文件庫存在 | 文件庫可見 | Pass / Fail |
| [ ] Library ID 已取得 | 記錄表已填寫 | Pass / Fail |

**類別 B：版本控制（3 項）**

| 檢查項目 | 驗證方式 | 結果 |
|:--------|:--------|:----|
| [ ] 版本歷程已啟用 | Library Settings 確認 | Pass / Fail |
| [ ] 保留 500 個主版本 | 設定值確認 | Pass / Fail |
| [ ] 不需 Check Out | 設定值確認 | Pass / Fail |

**類別 C：隔離區設定（3 項）**

| 檢查項目 | 驗證方式 | 結果 |
|:--------|:--------|:----|
| [ ] _Quarantine 資料夾已建立 | 文件庫可見 | Pass / Fail |
| [ ] _Quarantine 權限已設定 | 權限檢查 | Pass / Fail |
| [ ] 一般使用者無法存取 _Quarantine | 測試確認 | Pass / Fail |

**類別 D：網站權限（7 項）**

| 檢查項目 | 驗證方式 | 結果 |
|:--------|:--------|:----|
| [ ] GOV-Architects 為 Read | Site permissions 確認 | Pass / Fail |
| [ ] GOV-SecurityReviewers 為 Read | Site permissions 確認 | Pass / Fail |
| [ ] GOV-QAReviewers 為 Read | Site permissions 確認 | Pass / Fail |
| [ ] GOV-EngineeringManagement 為 Read | Site permissions 確認 | Pass / Fail |
| [ ] GOV-GovernanceLead 為 Read | Site permissions 確認 | Pass / Fail |
| [ ] GOV-ExecutiveManagement 為 Read | Site permissions 確認 | Pass / Fail |
| [ ] Flow Service Principal 為 Contribute | Site permissions 確認 | Pass / Fail |

**類別 E：權限驗證測試（5 項）**

| 檢查項目 | 驗證方式 | 結果 |
|:--------|:--------|:----|
| [ ] Architect 無法上傳至專案資料夾 | 測試確認 | Pass / Fail |
| [ ] Governance Lead 無法上傳至專案資料夾 | 測試確認 | Pass / Fail |
| [ ] 所有人類帳號僅能讀取 | 測試確認 | Pass / Fail |
| [ ] Architect 可寫入 _Quarantine | 測試確認 | Pass / Fail |
| [ ] Governance Lead 可寫入 _Quarantine | 測試確認 | Pass / Fail |

**類別 F：角色 ID 記錄（5 項）**

| 檢查項目 | 驗證方式 | 結果 |
|:--------|:--------|:----|
| [ ] Contribute Role ID 已記錄 | 記錄表已填寫 | Pass / Fail |
| [ ] Read Role ID 已記錄 | 記錄表已填寫 | Pass / Fail |
| [ ] Flow Service Principal ID 已記錄 | 記錄表已填寫 | Pass / Fail |
| [ ] 各群組 Principal ID 已記錄 | 記錄表已填寫 | Pass / Fail |
| [ ] ID 記錄表已交付 | 文件確認 | Pass / Fail |

### Ready Gate 通過條件

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SharePoint Ready Gate 通過條件                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  類別 A：網站與文件庫          5/5 項通過 ────────► ✓                        │
│  類別 B：版本控制              3/3 項通過 ────────► ✓                        │
│  類別 C：隔離區設定            3/3 項通過 ────────► ✓                        │
│  類別 D：網站權限              7/7 項通過 ────────► ✓                        │
│  類別 E：權限驗證測試          5/5 項通過 ────────► ✓                        │
│  類別 F：角色 ID 記錄          5/5 項通過 ────────► ✓                        │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│  總計：28/28 項通過                                                          │
│                                                                             │
│  ✅ SharePoint Ready Gate 通過                                              │
│     可進入 04-powerapps-forms.md                                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 附錄：SharePoint REST API 端點參考

**資料夾操作**：

| 操作 | Method | URI |
|:----|:-------|:----|
| 建立資料夾 | POST | `_api/web/folders` |
| 取得資料夾 | GET | `_api/web/GetFolderByServerRelativeUrl('{path}')` |

**權限操作**：

| 操作 | Method | URI |
|:----|:-------|:----|
| 中斷繼承 | POST | `_api/web/.../BreakRoleInheritance(copyRoleAssignments=false, clearSubscopes=true)` |
| 新增權限 | POST | `_api/web/.../RoleAssignments/AddRoleAssignment(principalId={id}, roleDefId={roleId})` |
| 移除權限 | POST | `_api/web/.../RoleAssignments/RemoveRoleAssignment(principalId={id}, roleDefId={roleId})` |

---

## 附錄：PnP PowerShell 指令參考

**連線**：
```powershell
Connect-PnPOnline -Url "https://[租戶].sharepoint.com/sites/design-governance" -Interactive
```

**資料夾操作**：
```powershell
Add-PnPFolder -Name "DR-2026-0001" -Folder "Shared Documents"
Get-PnPFolder -Url "Shared Documents/DR-2026-0001"
```

**權限操作**：
```powershell
Set-PnPFolderPermission -List "Documents" -Identity "DR-2026-0001" -User "flow-sp@tenant.onmicrosoft.com" -AddRole "Contribute"
Set-PnPFolderPermission -List "Documents" -Identity "DR-2026-0001" -Group "GOV-Architects" -AddRole "Read"
```

---

## 本章完成摘要

**完成本章後，您現在具備**：

| 項目 | 狀態 |
|:-----|:----|
| SharePoint 治理網站 | 已建立（含權限設定） |
| Design Documents 文件庫 | 已建立（含版本控制） |
| Quarantine 隔離區 | 已建立 |
| 網站層級權限 | 已設定（僅 Flow Service Principal 可寫入專案資料夾） |
| 各項 ID 記錄（Role ID、Principal ID） | 已記錄 |
| SharePoint Ready Gate | 已通過 |

**此刻您不需要做的事**：

- 不需要建立 Power Automate Flow（第 05 章）
- 不需要手動建立專案資料夾（由 Flow 自動建立）
- 不需要執行 Document Freeze（由 Flow 執行）
- 不需要測試完整端對端流程（第 07 章）

**本章說明但尚未實作的項目**：

- GOV-001 Flow 建立專案資料夾（第 05 章實作）
- GOV-014 Flow 執行 Document Freeze（第 05 章實作）
- GOV-017 Flow 偵測孤兒檔案（第 06 章實作）

**下一章將完成**：

- Power Apps Canvas App 建立
- 治理表單 UI 設計
- 表單驗證邏輯（UX 層）
- Flow 呼叫準備（待第 05 章 Flow 建立後連接）

---

## 版本歷史

| 版本 | 日期 | 變更說明 |
|:-----|:-----|:---------|
| v1.0 | 2026-01-29 | 初版建立 |
| v2.0 | 2026-01-29 | 新增治理核心原則聲明、權限精細設計、緊急文件處理流程 |
| v2.1 | 2026-02-11 | 鑑識修訂：Document Register 欄位 Uploaded By 型別修正（Text→Lookup User），對齊 Doc 02 權威定義 |
| v2.2 | 2026-02-11 | 日常流程修訂：(1) DocumentType→Folder 對應表修正 4 處（RiskAssessmentStrategy→01_Feasibility, ThreatModel→04_Security, ChangeImpact→03_Design, DocumentRegister→06_Handover），對齊 Doc 02 Baseline Matrix；(2) 新增 TestPlan/Other 映射行；(3) 對應表標註 Doc 02 Baseline Matrix 為單一權威來源；(4) Document Register 新增 3 欄位（gov_documentrole, gov_deliverablepackage, gov_supersededby）；(5) GOV-005 流程重寫為 Base64 上傳模式含版本推進 |

---

**文件結束**

**下一步**：通過 SharePoint Ready Gate 後，請繼續參閱 [04-powerapps-forms.md](04-powerapps-forms.md) 進行 Power Apps 表單建置。
