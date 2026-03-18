# 治理系統環境建置與前置條件指南

**文件版本**：v2.1
**建立日期**：2026-01-28
**適用系統**：Design Governance System（Dataverse 架構）
**後續文件**：02-Dataverse-Data-Model-and-Security.md

---


## 文件使用說明

### 文件定位

本文件為 Design Governance System 建置的**第一份實作文件**，涵蓋所有環境與前置條件設定。

**必須先完成本文件所有步驟，才可進入後續文件**：
- 02-dataverse-data-model-and-security.md（Dataverse 資料模型）
- 03-sharepoint-architecture.md（SharePoint 架構）
- 04-powerapps-forms.md（Power Apps 表單）
- 05-core-flows-implementation-runbook.md（Power Automate Flow 施工）

### 讀者假設

本文件假設讀者：
- 第一次建置 Microsoft Power Platform 治理系統
- 具備 Microsoft 365 全域管理員或 Power Platform 管理員權限
- 可存取 Azure Portal 與 Microsoft Entra 管理中心

### 操作原則

- 所有步驟皆包含**完整 UI 操作路徑**
- 所有驗證皆為**可觀察、可確認**的具體結果
- **禁止**跳過任何驗證步驟
- **禁止**在未完成本文件所有檢查點前進入下一份文件

### 章節相依性說明

以下標示各章節的相依關係，以及對後續文件的影響：

| 章節 | 相依於 | 影響的後續文件/功能 |
|:-----|:-------|:------------------|
| 2. 租戶與授權 | 無 | 所有功能 |
| 3. 環境策略 | 無 | 所有功能（一旦決定不可變更） |
| 4. 環境建立 | 2, 3 | 所有 Dataverse 操作 |
| 5. Entra ID 群組 | 2 | 所有權限控制、審批路由 |
| 6. Service Principal | 2, 4 | **所有 Power Automate Flow**（見 6.6） |
| 7. SharePoint | 2 | 文件管理、Document Freeze |
| 8. Dataverse 權限 | 4, 5, 6 | 所有資料存取 |
| 10. Ready Gate | 1-9 | **不得進入 02 文件** |

---

## Microsoft 365 租戶與授權需求

### 租戶層級需求

| 需求項目 | 最低要求 | 驗證方法 |
|:--------|:--------|:--------|
| Microsoft 365 租戶 | 任何商業版租戶 | 登入 admin.microsoft.com 成功 |
| 全域管理員或 Power Platform 管理員 | 至少 1 位 | 見 2.3 驗證步驟 |
| Azure Active Directory（Entra ID） | 已啟用 | 登入 entra.microsoft.com 成功 |

### 使用者授權需求

**每位使用治理系統的使用者**必須具備以下授權之一：

| 授權方案 | 包含功能 | 適用角色 |
|:--------|:--------|:--------|
| **Power Apps Premium**（建議） | Dataverse 完整存取、Premium 連接器 | 所有角色 |
| **Power Apps per app** | 單一應用程式存取 | 僅查看者 |
| **Power Automate Premium** | Premium 連接器、子流程 | Flow 開發者 |
| **Dynamics 365 任一方案** | 包含 Power Apps + Dataverse | 已有 D365 授權者 |

**Flow Service Principal 授權**：
- Service Principal 執行 Flow **不需要**使用者授權
- 但需要 Power Automate Premium 授權指派給 Flow 擁有者（或使用 Service Principal 執行）

### 驗證步驟：確認管理員權限

**操作路徑**：
1. 開啟瀏覽器，前往：https://admin.microsoft.com
2. 使用您的管理員帳號登入
3. 左側選單 → **Users** → **Active users**
4. 搜尋您的帳號名稱
5. 點擊您的帳號 → **Manage roles**

**驗證結果**（必須滿足以下任一）：
- [ ] 畫面顯示 **Global administrator** 已勾選
- [ ] 畫面顯示 **Power Platform administrator** 已勾選

**若驗證失敗**：聯絡您的 IT 管理員取得必要權限。

### 驗證步驟：確認 Power Platform 管理中心存取

**操作路徑**：
1. 開啟瀏覽器，前往：https://admin.powerplatform.microsoft.com
2. 使用管理員帳號登入

**驗證結果**：
- [ ] 畫面顯示 Power Platform admin center 首頁
- [ ] 左側選單可見 **Environments** 選項
- [ ] 點擊 Environments 可看到環境清單（至少有 Default 環境）

**若驗證失敗**：您的帳號缺少 Power Platform 管理員權限。

### 驗證步驟：確認 Entra ID 管理中心存取

**操作路徑**：
1. 開啟瀏覽器，前往：https://entra.microsoft.com
2. 使用管理員帳號登入

**驗證結果**：
- [ ] 畫面顯示 Microsoft Entra admin center 首頁
- [ ] 左側選單可見 **Groups** 選項
- [ ] 點擊 Groups → All groups 可看到群組清單

**若驗證失敗**：您的帳號缺少 Entra ID 管理權限。

---

## 單一環境 vs 多環境策略

### 環境策略選項

本治理系統支援兩種環境策略：

| 策略 | 環境數量 | 適用情境 | 建議對象 |
|:----|:--------|:--------|:--------|
| **單一環境** | 1 個 | 小型團隊、概念驗證、快速部署 | 使用者 < 50 人 |
| **多環境** | 2-4 個 | 企業級部署、正式生產環境 | 使用者 >= 50 人 |

### 單一環境策略說明

**環境配置**：
```
┌─────────────────────────────────────┐
│         GOV-PROD（單一環境）          │
│  - 開發、測試、正式皆在此環境         │
│  - 所有使用者共用                     │
└─────────────────────────────────────┘
```

**優點**：
- 建置速度快
- 管理簡單
- 授權成本較低

**缺點**：
- 開發中的變更可能影響正式使用者
- 無法隔離測試資料
- 不符合企業級變更管理要求

### 多環境策略說明

**環境配置**：
```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   GOV-DEV   │ →  │   GOV-QA    │ →  │   GOV-UAT   │ →  │  GOV-PROD   │
│   開發環境   │    │   測試環境   │    │  使用者驗收  │    │   正式環境   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

**各環境用途**：

| 環境 | 用途 | 使用者 | 資料性質 |
|:----|:-----|:------|:--------|
| GOV-DEV | 開發與單元測試 | 開發團隊 | 測試資料 |
| GOV-QA | 整合測試 | 開發 + QA 團隊 | 測試資料 |
| GOV-UAT | 使用者驗收測試 | 業務使用者 | 模擬真實資料 |
| GOV-PROD | 正式生產環境 | 所有使用者 | 真實資料 |

**最小多環境配置**（2 個環境）：
```
┌─────────────┐    ┌─────────────┐
│   GOV-DEV   │ →  │  GOV-PROD   │
│  開發+測試   │    │   正式環境   │
└─────────────┘    └─────────────┘
```

---

### 治理不可逆警告

> **嚴重警告：環境策略一旦決定並正式上線後，禁止變更。**

#### 為何環境策略不可變更

| 變更類型 | 治理風險 | 稽核風險 |
|:--------|:--------|:--------|
| 單一環境 → 多環境 | 歷史審批記錄無法遷移，治理鏈斷裂 | 無法證明歷史專案經過正式審批 |
| 多環境 → 單一環境 | DEV/QA 環境的測試資料混入 PROD | 稽核軌跡混亂，無法區分測試與正式記錄 |
| 環境合併 | 專案識別碼（RequestID）可能重複 | Review Decision Log 關聯斷裂 |
| 環境拆分 | 進行中的審批流程中斷 | Approval 回應無法對應原始請求 |

#### 禁止事項

以下行為在正式上線後**禁止**執行：

1. **禁止**將 PROD 環境資料匯入 DEV 環境後再匯回 PROD
2. **禁止**刪除任何環境後重新建立同名環境
3. **禁止**變更環境的 Dataverse URL（組織 URL）
4. **禁止**將環境從一個租戶遷移至另一個租戶
5. **禁止**重設環境（Reset environment）

#### 變更環境策略的後果

若違反上述禁止事項，將導致：

| 後果類型 | 具體影響 |
|:--------|:--------|
| **治理鏈斷裂** | Project Registry 與 Review Decision Log 的關聯失效 |
| **稽核證據失效** | 無法證明「誰在何時審批了哪個專案」 |
| **Flow 執行失敗** | Service Principal 連線中斷，所有 GOV Flow 停止運作 |
| **Approval 失效** | 歷史 Approval 記錄與 Dataverse 記錄脫鉤 |
| **合規性破壞** | IEC 62443、ISO 27001 稽核無法通過 |

#### 環境策略決策記錄

**在繼續之前，您必須明確選擇環境策略並記錄：**

```
環境策略決策記錄
================
決策日期：____年____月____日
決策者：________________（姓名 + 職稱）
選擇的策略：[ ] 單一環境  [ ] 多環境（____個環境）

我已閱讀並理解：
[ ] 環境策略一旦正式上線後禁止變更
[ ] 變更環境策略將導致治理鏈斷裂與稽核證據失效
[ ] 此決策將影響所有後續文件的實作

決策者簽名：________________
```

---

## Power Platform 環境建立

### 建立環境前的決策確認

**在執行本節步驟前，必須完成**：
- [ ] 第 3.4.4 節的環境策略決策記錄

### 建立 Dataverse 環境（單一環境策略）

**操作路徑**：
1. 開啟瀏覽器，前往：https://admin.powerplatform.microsoft.com
2. 左側選單 → **Environments**
3. 點擊 **+ New** 按鈕

**填寫環境設定**：

| 設定欄位 | 填寫值 | 說明 |
|:--------|:------|:-----|
| Name | `GOV-PROD` | 環境顯示名稱 |
| Region | 選擇您的地理區域（如 Asia） | 資料存放位置 |
| Type | **Production** | 正式環境類型 |
| Purpose | `Design Governance System - Production` | 環境用途說明 |
| Create a database for this environment | **Yes**（必須勾選） | 啟用 Dataverse |

**點擊 Next 後，填寫 Dataverse 設定**：

| 設定欄位 | 填寫值 | 說明 |
|:--------|:------|:-----|
| Language | Chinese (Traditional) 或 English | 系統語言 |
| Currency | TWD 或 USD | 預設幣別 |
| Enable Dynamics 365 apps | **No** | 不需要 D365 應用程式 |
| Deploy sample apps and data | **No** | 不安裝範例資料 |
| Security group | 留空（稍後設定） | 存取控制 |

**點擊 Save**，等待環境建立完成（約 5-10 分鐘）。

### 建立 Dataverse 環境（多環境策略）

**對每個環境重複以下步驟**：

#### 建立 GOV-DEV 環境

| 設定欄位 | 填寫值 |
|:--------|:------|
| Name | `GOV-DEV` |
| Type | **Sandbox** |
| Purpose | `Design Governance System - Development` |

#### 建立 GOV-QA 環境（選用）

| 設定欄位 | 填寫值 |
|:--------|:------|
| Name | `GOV-QA` |
| Type | **Sandbox** |
| Purpose | `Design Governance System - Quality Assurance` |

#### 建立 GOV-UAT 環境（選用）

| 設定欄位 | 填寫值 |
|:--------|:------|
| Name | `GOV-UAT` |
| Type | **Sandbox** |
| Purpose | `Design Governance System - User Acceptance Testing` |

#### 建立 GOV-PROD 環境

| 設定欄位 | 填寫值 |
|:--------|:------|
| Name | `GOV-PROD` |
| Type | **Production** |
| Purpose | `Design Governance System - Production` |

### 驗證步驟：確認環境建立成功

**操作路徑**：
1. Power Platform admin center → Environments
2. 找到您建立的環境（如 GOV-PROD）
3. 點擊環境名稱進入詳細資訊頁面

**驗證結果**：
- [ ] 環境狀態（State）顯示為 **Ready**
- [ ] 環境類型（Type）顯示正確（Production 或 Sandbox）
- [ ] 環境 URL 顯示格式為 `https://org*****.crm**.dynamics.com`
- [ ] 點擊 Environment URL 可開啟 Dataverse 首頁

**記錄環境資訊**（後續步驟需要）：

```
環境資訊記錄
============
環境名稱：________________
環境 URL：https://________________________.crm__.dynamics.com
環境 ID：________________________________
建立日期：____年____月____日
```

### 啟用環境稽核功能

**操作路徑**：
1. Power Platform admin center → Environments → 選擇環境
2. 點擊 **Settings**（齒輪圖示）
3. 展開 **Audit and logs** → **Audit settings**

**設定稽核選項**：

| 設定項目 | 設定值 |
|:--------|:------|
| Start Auditing | **On** |
| Log access | **On** |
| Read logs | **On** |

**點擊 Save**。

**驗證結果**：
- [ ] Start Auditing 顯示為 On
- [ ] 畫面顯示 "Auditing is enabled"

---

## Entra ID 安全群組建立

### 安全群組清單

本治理系統需要建立以下 7 個安全群組：

| 群組名稱 | 用途 | 成員類型 |
|:--------|:-----|:--------|
| GOV-Architects | 系統架構師，可建立專案與申請 Gate | 人員 |
| GOV-SecurityReviewers | 安全審查員，執行 Gate 1 Security Review | 人員 |
| GOV-QAReviewers | 品質審查員，執行 Gate 1/3 QA Review | 人員 |
| GOV-EngineeringManagement | 工程主管，執行 Gate 0/2 Final Approval | 人員 |
| GOV-GovernanceLead | 治理負責人，執行 Gate 1/3 Governance Approval | 人員 |
| GOV-ExecutiveManagement | 執行長層級，執行 High Risk Acceptance | 人員 |
| GOV-FlowServicePrincipal | Flow 服務帳號，執行所有 Power Automate Flow | 服務主體 |

### 建立安全群組

**操作路徑**：
1. 開啟瀏覽器，前往：https://entra.microsoft.com
2. 左側選單 → **Groups** → **All groups**
3. 點擊 **+ New group**

**對每個群組執行以下步驟**：

#### 建立 GOV-Architects 群組

**填寫群組設定**：

| 設定欄位 | 填寫值 |
|:--------|:------|
| Group type | **Security** |
| Group name | `GOV-Architects` |
| Group description | `Design Governance System - System Architects who can create projects and request gate reviews` |
| Microsoft Entra roles can be assigned to the group | **No** |
| Membership type | **Assigned** |

**點擊 Create**。

#### 建立其他群組

對以下群組重複上述步驟：

| 群組名稱 | 描述 |
|:--------|:----|
| GOV-SecurityReviewers | `Security reviewers for Gate 1 security review` |
| GOV-QAReviewers | `QA reviewers for Gate 1/3 QA review` |
| GOV-EngineeringManagement | `Engineering management for Gate 0/2 approval` |
| GOV-GovernanceLead | `Governance leads for Gate 1/3 governance approval` |
| GOV-ExecutiveManagement | `Executive management for high risk acceptance` |
| GOV-FlowServicePrincipal | `Service principal for Power Automate flows` |

### 新增群組成員

**操作路徑**：
1. Entra admin center → Groups → All groups
2. 搜尋並點擊群組名稱（如 GOV-Architects）
3. 左側選單 → **Members**
4. 點擊 **+ Add members**
5. 搜尋並選擇要新增的使用者
6. 點擊 **Select**

**每個群組至少新增 1 位成員**（測試用途）。

### 驗證步驟：確認群組建立成功

**操作路徑**：
1. Entra admin center → Groups → All groups
2. 在搜尋框輸入 `GOV-`

**驗證結果**：
- [ ] 搜尋結果顯示 7 個群組
- [ ] 每個群組的 Group type 顯示為 Security
- [ ] 點擊每個群組，Members 頁面顯示至少 1 位成員

**記錄群組 Object ID**（後續步驟需要）：

```
群組 Object ID 記錄
==================
GOV-Architects: ____________________________________
GOV-SecurityReviewers: ____________________________________
GOV-QAReviewers: ____________________________________
GOV-EngineeringManagement: ____________________________________
GOV-GovernanceLead: ____________________________________
GOV-ExecutiveManagement: ____________________________________
GOV-FlowServicePrincipal: ____________________________________
```

---

## Flow 執行身分設定（Service Principal）

### 本章重要性說明

> **警告：本章設定的 Service Principal 為所有 Power Automate Flow 的執行身分。**
> **若此身分設定錯誤或權限不足，以下功能將完全失效：**

| 受影響文件/功能 | 失效後果 |
|:--------------|:--------|
| 02-dataverse-data-model-and-security.md | Field-Level Security 無法正確授權，Flow-only 欄位無法寫入 |
| 05-core-flows-implementation-runbook.md | 所有 GOV-001 至 GOV-019 Flow 執行失敗 |
| GOV-001: Create Project | 無法建立專案，RequestID 無法產生 |
| GOV-002/003: Gate Approval | 無法更新 CurrentGate，Gate 推進失敗 |
| GOV-004: Risk Acceptance | 無法更新 RiskAcceptanceStatus |
| GOV-014: Document Freeze | 無法凍結文件 |
| GOV-017: Guardrail Monitor | 無法偵測違規與自動回滾 |
| GOV-018: Compliance Reconciler | 無法執行每日合規性對帳 |

### Service Principal vs Service Account

| 選項 | 說明 | 優點 | 缺點 |
|:----|:-----|:----|:----|
| **Service Principal**（建議） | Azure AD 應用程式註冊 | 無需使用者授權、無密碼過期問題、可精細控制權限 | 設定較複雜 |
| **Service Account** | 專用使用者帳號 | 設定簡單 | 需要使用者授權、密碼會過期、權限較粗糙 |

**本文件採用 Service Principal 方案**。

### 建立 Azure AD 應用程式註冊

**操作路徑**：
1. 開啟瀏覽器，前往：https://entra.microsoft.com
2. 左側選單 → **Applications** → **App registrations**
3. 點擊 **+ New registration**

**填寫應用程式設定**：

| 設定欄位 | 填寫值 |
|:--------|:------|
| Name | `GOV-FlowServicePrincipal` |
| Supported account types | **Accounts in this organizational directory only (Single tenant)** |
| Redirect URI | 留空 |

**點擊 Register**。

### 記錄應用程式識別碼

**建立完成後，記錄以下資訊**：

```
Service Principal 資訊記錄
=========================
Application (client) ID: ____________________________________
Directory (tenant) ID: ____________________________________
Object ID: ____________________________________
```

### 建立用戶端密碼

**操作路徑**：
1. 在應用程式頁面，左側選單 → **Certificates & secrets**
2. 點擊 **+ New client secret**

**填寫密碼設定**：

| 設定欄位 | 填寫值 |
|:--------|:------|
| Description | `GOV Flow Execution Secret` |
| Expires | **24 months**（或依您的安全政策） |

**點擊 Add**。

**立即記錄密碼值**（離開此頁面後無法再次查看）：

```
Client Secret 記錄（機密資訊，請安全保管）
=========================================
Secret ID: ____________________________________
Value: ____________________________________
Expires: ____年____月____日
```

### 設定 API 權限

**操作路徑**：
1. 左側選單 → **API permissions**
2. 點擊 **+ Add a permission**

#### 新增 Dataverse API 權限

1. 選擇 **APIs my organization uses**
2. 搜尋 `Dataverse` 或 `Common Data Service`
3. 選擇 **Dataverse**
4. 選擇 **Delegated permissions**
5. 勾選 **user_impersonation**
6. 點擊 **Add permissions**

#### 新增 Microsoft Graph API 權限

1. 點擊 **+ Add a permission** → **Microsoft Graph**
2. 選擇 **Delegated permissions**
3. 搜尋並勾選：
   - `User.Read`
   - `Group.Read.All`
   - `Sites.ReadWrite.All`（SharePoint 存取）
4. 點擊 **Add permissions**

#### 授予管理員同意

1. 點擊 **Grant admin consent for [您的組織名稱]**
2. 確認對話框點擊 **Yes**

**驗證結果**：
- [ ] 所有權限的 Status 欄位顯示綠色勾勾與 "Granted for [組織名稱]"

### 將 Service Principal 新增為 Dataverse 使用者

**操作路徑**：
1. 開啟瀏覽器，前往：https://admin.powerplatform.microsoft.com
2. Environments → 選擇您的環境（如 GOV-PROD）
3. 點擊 **Settings** → **Users + permissions** → **Application users**
4. 點擊 **+ New app user**

**填寫應用程式使用者設定**：

| 設定欄位 | 填寫值 |
|:--------|:------|
| App | 選擇 `GOV-FlowServicePrincipal`（搜尋您剛建立的應用程式） |
| Business unit | 選擇根業務單位 |
| Security roles | 先選擇 **System Administrator**（稍後調整為自訂角色） |

**點擊 Create**。

### 驗證步驟：確認 Service Principal 設定成功

**驗證 1：確認應用程式註冊**

**操作路徑**：
1. Entra admin center → Applications → App registrations
2. 搜尋 `GOV-FlowServicePrincipal`

**驗證結果**：
- [ ] 應用程式存在於列表中
- [ ] Application (client) ID 與您記錄的值相符

**驗證 2：確認 API 權限**

**操作路徑**：
1. 點擊應用程式 → API permissions

**驗證結果**：
- [ ] Dataverse user_impersonation 權限狀態為 "Granted"
- [ ] Microsoft Graph User.Read 權限狀態為 "Granted"
- [ ] Microsoft Graph Group.Read.All 權限狀態為 "Granted"
- [ ] Microsoft Graph Sites.ReadWrite.All 權限狀態為 "Granted"

**驗證 3：確認 Dataverse 應用程式使用者**

**操作路徑**：
1. Power Platform admin center → Environments → 選擇環境
2. Settings → Users + permissions → Application users

**驗證結果**：
- [ ] `GOV-FlowServicePrincipal` 出現在應用程式使用者列表中
- [ ] 點擊該使用者，Security roles 顯示 System Administrator

### 將 Service Principal 加入 GOV-FlowServicePrincipal 群組

**操作路徑**：
1. Entra admin center → Groups → All groups
2. 搜尋並點擊 `GOV-FlowServicePrincipal`
3. 左側選單 → **Members** → **+ Add members**
4. 切換至 **Service principals** 標籤
5. 搜尋 `GOV-FlowServicePrincipal`（應用程式名稱）
6. 選擇並點擊 **Select**

**驗證結果**：
- [ ] 在 Members 頁面可看到 GOV-FlowServicePrincipal（類型為 Service principal）

---

## SharePoint 網站與文件庫建立

### 建立治理專用 SharePoint 網站

**操作路徑**：
1. 開啟瀏覽器，前往：https://[您的租戶].sharepoint.com
2. 點擊 **+ Create site**
3. 選擇 **Team site**

**填寫網站設定**：

| 設定欄位 | 填寫值 |
|:--------|:------|
| Site name | `Design Governance` |
| Group email address | `design-governance`（自動產生） |
| Site address | `design-governance`（自動產生） |
| Privacy settings | **Private - only members can access** |
| Language | Chinese (Traditional) 或 English |

**點擊 Create**，等待網站建立完成。

### 記錄 SharePoint 網站資訊

**建立完成後，記錄以下資訊**：

```
SharePoint 網站資訊記錄
======================
網站名稱：Design Governance
網站 URL：https://[租戶].sharepoint.com/sites/design-governance
網站 ID：（稍後從 API 取得）
```

### 建立文件庫結構

**操作路徑**：
1. 進入 Design Governance 網站
2. 左側選單 → **Documents**（預設文件庫）

**建立資料夾結構**（用於存放專案文件）：

此資料夾結構將由 GOV-001 Flow 自動建立，但需先確認文件庫存在。

**預設文件庫結構**：
```
Documents/
├── [專案資料夾將由 Flow 自動建立]
│   ├── 01_Feasibility/
│   ├── 02_Risk_Assessment/
│   ├── 03_Design/
│   ├── 04_Security/
│   ├── 05_Test/
│   └── 06_Handover/
```

### 設定 SharePoint 權限

**操作路徑**：
1. 網站首頁右上角 → 齒輪圖示 → **Site permissions**
2. 點擊 **Advanced permissions settings**

**新增群組權限**：

| 群組 | SharePoint 權限層級 |
|:----|:------------------|
| GOV-Architects | **Read**（讀取） |
| GOV-SecurityReviewers | **Read**（讀取） |
| GOV-QAReviewers | **Read**（讀取） |
| GOV-EngineeringManagement | **Read**（讀取） |
| GOV-GovernanceLead | **Read**（讀取） |
| GOV-ExecutiveManagement | **Read**（讀取） |
| Flow Service Principal | **Contribute**（參與） |

**操作步驟**：
1. 點擊 **Grant Permissions**
2. 在 "Share" 欄位輸入群組名稱（如 GOV-Architects）
3. 點擊下方的 **SHOW OPTIONS**
4. 取消勾選 "Send an email invitation"
5. 在 "Select a permission level" 選擇對應權限
6. 點擊 **Share**

### 驗證步驟：確認 SharePoint 設定成功

**驗證 1：確認網站可存取**

**操作路徑**：
1. 開啟瀏覽器，前往您記錄的網站 URL

**驗證結果**：
- [ ] 網站首頁正常顯示
- [ ] 左側選單可見 Documents

**驗證 2：確認文件庫存在**

**操作路徑**：
1. 左側選單 → Documents

**驗證結果**：
- [ ] 文件庫頁面正常顯示
- [ ] 頁面顯示 "Drag files here" 或類似提示

**驗證 3：確認群組權限**

**操作路徑**：
1. 齒輪圖示 → Site permissions → Advanced permissions settings
2. 點擊 "Check Permissions"
3. 輸入 GOV-Architects 群組中的某位成員名稱
4. 點擊 "Check Now"

**驗證結果**：
- [ ] 權限檢查顯示該使用者具有 Read 權限

---

## Dataverse 基礎權限設定

### 建立 Dataverse 團隊

**為何需要 Dataverse 團隊**：
- Entra ID 安全群組無法直接指派 Dataverse 安全角色
- 必須建立 Dataverse 團隊並連結至 Entra ID 群組
- 團隊類型必須為 **AAD Security Group**

**操作路徑**：
1. 開啟瀏覽器，前往：https://make.powerapps.com
2. 右上角切換至目標環境（如 GOV-PROD）
3. 左側選單 → **Settings**（齒輪圖示）→ **Advanced settings**
4. 這將開啟 Dynamics 365 設定介面
5. 上方選單 → **Settings** → **Security** → **Teams**

**對每個 Entra ID 群組建立對應的 Dataverse 團隊**：

#### 建立 GOV-Architects 團隊

1. 點擊 **+ New**
2. 填寫團隊設定：

| 設定欄位 | 填寫值 |
|:--------|:------|
| Team Name | `GOV-Architects` |
| Business Unit | 選擇根業務單位 |
| Administrator | 選擇管理員帳號 |
| Team Type | **AAD Security Group** |
| AAD Group | 搜尋並選擇 `GOV-Architects` |
| Membership Type | **Members and guests** |

3. 點擊 **Save**

#### 建立其他團隊

對以下群組重複上述步驟：

| Team Name | AAD Group |
|:----------|:----------|
| GOV-SecurityReviewers | GOV-SecurityReviewers |
| GOV-QAReviewers | GOV-QAReviewers |
| GOV-EngineeringManagement | GOV-EngineeringManagement |
| GOV-GovernanceLead | GOV-GovernanceLead |
| GOV-ExecutiveManagement | GOV-ExecutiveManagement |
| GOV-FlowServicePrincipal | GOV-FlowServicePrincipal |

### 驗證步驟：確認 Dataverse 團隊建立成功

**操作路徑**：
1. Dynamics 365 Settings → Security → Teams
2. 切換檢視為 "All AAD Security Group Teams"

**驗證結果**：
- [ ] 列表顯示 7 個團隊
- [ ] 每個團隊的 Team Type 顯示為 "AAD Security Group"
- [ ] 點擊每個團隊，AAD Group ID 欄位有值

### Field Security Profile 預備

**說明**：
Field Security Profile 的完整設定將在 02-Dataverse-Data-Model-and-Security.md 中執行。
本節僅確認環境已啟用 Field-Level Security 功能。

**驗證步驟**：

**操作路徑**：
1. Power Platform admin center → Environments → 選擇環境
2. Settings → Users + permissions → Field security profiles

**驗證結果**：
- [ ] 頁面正常顯示（可能為空白列表）
- [ ] 可看到 **+ New profile** 按鈕

---

## 環境命名慣例

### 命名慣例總表

| 資源類型 | 命名格式 | 範例 |
|:--------|:--------|:----|
| **環境** | `GOV-{ENV}` | `GOV-PROD`, `GOV-DEV` |
| **Entra ID 群組** | `GOV-{RoleName}` | `GOV-Architects` |
| **Service Principal** | `GOV-FlowServicePrincipal` | `GOV-FlowServicePrincipal` |
| **SharePoint 網站** | `design-governance` | `design-governance` |
| **Dataverse 資料表** | `gov_{tablename}` | `gov_projectregistry` |
| **Dataverse 欄位** | `gov_{fieldname}` | `gov_currentgate` |
| **選項集** | `gov_{choicename}` | `gov_projecttype` |
| **安全角色** | `GOV-{RoleName}` | `GOV-SystemArchitect` |
| **Power Automate Flow** | `GOV-{NNN}: {FlowName}` | `GOV-001: Create Project` |
| **Power Apps** | `Design Governance - {AppName}` | `Design Governance - Create Project` |
| **專案識別碼** | `DR-{YYYY}-{####}` | `DR-2026-0001` |
| **文件識別碼** | `DOC-{RequestID}-{DocType}-{###}` | `DOC-DR-2026-0001-RiskAssessment-001` |

### 命名慣例規則

1. **一致性**：所有治理系統資源皆以 `GOV-` 或 `gov_` 為前綴
2. **可讀性**：使用有意義的名稱，避免縮寫
3. **唯一性**：識別碼必須全域唯一
4. **不可變性**：資源建立後，名稱禁止變更

### 禁止事項

1. **禁止**使用中文命名 Dataverse 資源（Schema Name）
2. **禁止**使用空格（使用底線或連字號）
3. **禁止**使用特殊字元（除底線與連字號外）
4. **禁止**命名超過 100 個字元

---

## 環境準備完成判定（Environment Ready Gate）

### 本章說明

> **重要：未通過本章所有檢查項目，禁止進入 02-Dataverse-Data-Model-and-Security.md。**

本章提供環境準備的最終驗收清單。每個項目皆為**可觀察、可確認**的具體驗證。

### Environment Ready Gate 檢查清單

請逐一執行以下檢查，並在方框中打勾確認：

#### 租戶與授權（第 2 章）

| 檢查項目 | 驗證方法 | 結果 |
|:--------|:--------|:----|
| [ ] 可登入 Microsoft 365 管理中心 | 開啟 https://admin.microsoft.com，畫面顯示管理中心首頁 | Pass / Fail |
| [ ] 具備 Global Admin 或 Power Platform Admin 權限 | Users → 您的帳號 → Manage roles，顯示對應角色已勾選 | Pass / Fail |
| [ ] 可登入 Power Platform 管理中心 | 開啟 https://admin.powerplatform.microsoft.com，畫面顯示 Environments 列表 | Pass / Fail |
| [ ] 可登入 Entra ID 管理中心 | 開啟 https://entra.microsoft.com，畫面顯示管理中心首頁 | Pass / Fail |

#### 環境策略決策（第 3 章）

| 檢查項目 | 驗證方法 | 結果 |
|:--------|:--------|:----|
| [ ] 已完成環境策略決策記錄 | 第 3.4.4 節的決策記錄已填寫完整並簽名 | Pass / Fail |
| [ ] 已閱讀並理解治理不可逆警告 | 決策記錄中的三個確認項目皆已勾選 | Pass / Fail |

#### Power Platform 環境（第 4 章）

| 檢查項目 | 驗證方法 | 結果 |
|:--------|:--------|:----|
| [ ] 環境已建立且狀態為 Ready | Power Platform admin center → Environments，環境狀態顯示 Ready | Pass / Fail |
| [ ] 環境類型正確 | Production 環境類型顯示 Production，Sandbox 環境類型顯示 Sandbox | Pass / Fail |
| [ ] 環境 URL 可存取 | 點擊環境 URL，可開啟 Dataverse 首頁 | Pass / Fail |
| [ ] 環境稽核已啟用 | Settings → Audit settings，Start Auditing 顯示 On | Pass / Fail |
| [ ] 已記錄環境資訊 | 第 4.4 節的環境資訊記錄已填寫完整 | Pass / Fail |

#### Entra ID 安全群組（第 5 章）

| 檢查項目 | 驗證方法 | 結果 |
|:--------|:--------|:----|
| [ ] 7 個安全群組已建立 | Entra admin center → Groups，搜尋 GOV- 顯示 7 個群組 | Pass / Fail |
| [ ] 所有群組類型為 Security | 每個群組的 Group type 顯示 Security | Pass / Fail |
| [ ] 每個群組至少有 1 位成員 | 點擊每個群組 → Members，顯示至少 1 位成員 | Pass / Fail |
| [ ] 已記錄群組 Object ID | 第 5.4 節的 Object ID 記錄已填寫完整 | Pass / Fail |

#### Service Principal（第 6 章）

| 檢查項目 | 驗證方法 | 結果 |
|:--------|:--------|:----|
| [ ] 應用程式註冊已建立 | Entra admin center → App registrations，可找到 GOV-FlowServicePrincipal | Pass / Fail |
| [ ] Client Secret 已建立且已記錄 | 第 6.5 節的 Secret 記錄已填寫完整 | Pass / Fail |
| [ ] Dataverse API 權限已授予 | API permissions 頁面，Dataverse user_impersonation 狀態為 Granted | Pass / Fail |
| [ ] Microsoft Graph API 權限已授予 | API permissions 頁面，User.Read、Group.Read.All、Sites.ReadWrite.All 狀態皆為 Granted | Pass / Fail |
| [ ] Dataverse 應用程式使用者已建立 | Power Platform admin center → Application users，可找到 GOV-FlowServicePrincipal | Pass / Fail |
| [ ] Service Principal 已加入 GOV-FlowServicePrincipal 群組 | Entra admin center → GOV-FlowServicePrincipal 群組 → Members，顯示 Service Principal | Pass / Fail |
| [ ] 已記錄 Service Principal 資訊 | 第 6.4 節的 Application ID、Tenant ID、Object ID 已記錄 | Pass / Fail |

#### SharePoint（第 7 章）

| 檢查項目 | 驗證方法 | 結果 |
|:--------|:--------|:----|
| [ ] SharePoint 網站已建立 | 開啟記錄的網站 URL，網站首頁正常顯示 | Pass / Fail |
| [ ] Documents 文件庫存在 | 左側選單 → Documents，文件庫頁面正常顯示 | Pass / Fail |
| [ ] 群組權限已設定 | Site permissions → Check Permissions，GOV-Architects 成員顯示 Read 權限，Flow Service Principal 顯示 Contribute 權限 | Pass / Fail |
| [ ] 已記錄 SharePoint 網站資訊 | 第 7.2 節的網站 URL 已記錄 | Pass / Fail |

#### Dataverse 基礎設定（第 8 章）

| 檢查項目 | 驗證方法 | 結果 |
|:--------|:--------|:----|
| [ ] 7 個 Dataverse 團隊已建立 | Dynamics 365 Settings → Security → Teams，All AAD Security Group Teams 顯示 7 個團隊 | Pass / Fail |
| [ ] 所有團隊類型為 AAD Security Group | 每個團隊的 Team Type 顯示 AAD Security Group | Pass / Fail |
| [ ] 每個團隊已連結至對應的 Entra ID 群組 | 點擊每個團隊，AAD Group ID 欄位有值 | Pass / Fail |
| [ ] Field Security Profile 功能可存取 | Power Platform admin center → Field security profiles 頁面正常顯示 | Pass / Fail |

### Gate 通過判定

**通過條件**：上述所有檢查項目的結果皆為 Pass。

**若有任何項目為 Fail**：
1. 返回對應章節重新執行步驟
2. 完成後再次執行該檢查項目
3. 直到所有項目皆為 Pass

### Environment Ready Gate 簽核

```
Environment Ready Gate 簽核記錄
==============================
檢查日期：____年____月____日
檢查者：________________（姓名 + 職稱）

檢查結果摘要：
- 第 2 章（租戶與授權）：____ / 4 項通過
- 第 3 章（環境策略）：____ / 2 項通過
- 第 4 章（環境建立）：____ / 5 項通過
- 第 5 章（Entra ID 群組）：____ / 4 項通過
- 第 6 章（Service Principal）：____ / 7 項通過
- 第 7 章（SharePoint）：____ / 4 項通過
- 第 8 章（Dataverse 基礎）：____ / 4 項通過

總計：____ / 30 項通過

Gate 判定：[ ] 通過  [ ] 未通過

若通過，已授權進入 02-Dataverse-Data-Model-and-Security.md

簽核者簽名：________________
簽核日期：____年____月____日
```

---

## 附錄：故障排解

### 無法存取 Power Platform 管理中心

**症狀**：開啟 https://admin.powerplatform.microsoft.com 顯示「存取被拒」

**排解步驟**：
1. 確認您的帳號具備 Global Admin 或 Power Platform Admin 權限
2. 若權限剛指派，等待 15-30 分鐘後重試
3. 清除瀏覽器快取後重試
4. 使用無痕模式開啟

### 環境建立失敗

**症狀**：點擊 Create 後顯示錯誤訊息

**排解步驟**：
1. 確認您的租戶有足夠的環境配額（Production 環境通常有數量限制）
2. 確認所選區域支援 Dataverse
3. 檢查環境名稱是否與現有環境重複

### Service Principal 無法新增為 Dataverse 使用者

**症狀**：在 Application users 中搜尋不到應用程式

**排解步驟**：
1. 確認應用程式已在正確的租戶中建立
2. 確認已授予 Dataverse API 權限並已授予管理員同意
3. 等待 5-10 分鐘後重試（同步延遲）

### Entra ID 群組成員同步延遲

**症狀**：將使用者加入群組後，Dataverse 中未顯示

**排解步驟**：
1. Entra ID 群組成員同步至 Dataverse 最多需要 24 小時
2. 可手動觸發同步：Power Platform admin center → Environment → Users → Refresh
3. 確認 Dataverse 團隊類型為 AAD Security Group

---

## 附錄：相關資源連結

| 資源 | 連結 |
|:----|:----|
| Microsoft 365 管理中心 | https://admin.microsoft.com |
| Power Platform 管理中心 | https://admin.powerplatform.microsoft.com |
| Microsoft Entra 管理中心 | https://entra.microsoft.com |
| Power Apps Maker Portal | https://make.powerapps.com |
| Power Automate Portal | https://make.powerautomate.com |
| Microsoft Learn - Power Platform | https://learn.microsoft.com/power-platform |

---

## 附錄：版本歷史

| 版本 | 日期 | 變更說明 |
|:----|:-----|:--------|
| v1.0 | 2026-01-27 | 初版建立 |
| v2.0 | 2026-01-28 | 新增治理不可逆警告、Environment Ready Gate、Service Principal 相依性說明、驗證具體化 |
| v2.1 | 2026-02-11 | 鑑識修訂：SharePoint 權限修正（GOV-Architects: Edit→Read, GOV-GovernanceLead: Full Control→Read, 新增 Flow Service Principal: Contribute），對齊 Doc 03 權威定義 |

---

## 本章完成摘要

**完成本章後，您現在具備**：

| 項目 | 狀態 |
|:-----|:----|
| Microsoft 365 租戶與管理員權限 | 已驗證 |
| Power Platform 環境（含 Dataverse） | 已建立 |
| 7 個 Entra ID 安全群組 | 已建立 |
| Flow Service Principal（應用程式註冊） | 已建立並設定權限 |
| SharePoint 治理網站 | 已建立並設定權限 |
| 7 個 Dataverse 團隊（對應 Entra ID 群組） | 已建立 |
| Environment Ready Gate | 已通過 |

**此刻您不需要做的事**：

- 不需要建立任何 Dataverse 資料表（第 02 章）
- 不需要建立任何 Power Automate Flow（第 05 章）
- 不需要建立任何 Power Apps（第 04 章）

**下一章將完成**：

- Dataverse 資料模型建立（資料表、欄位、關聯性）
- Field-Level Security 設定
- 安全角色建立

---

**文件結束**

**下一步**：通過 Environment Ready Gate 後，請繼續參閱 [02-dataverse-data-model-and-security.md](02-dataverse-data-model-and-security.md) 進行 Dataverse 資料模型建置。
