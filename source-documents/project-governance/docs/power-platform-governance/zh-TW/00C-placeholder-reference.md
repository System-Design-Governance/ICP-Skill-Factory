# 占位符與環境變數參考清單

**文件版本**：v1.0
**生效日期**：2026-02-09
**文件擁有者**：System Design Governance Function
**文件性質**：環境部署參考

---

## 本文件目的

本文件集中列出 SOP 文件中所有需要替換的占位符（Placeholder）。請在環境準備階段填寫實際值，以便在後續文件中統一參考。

---

## 占位符清單

### 1. Service Principal 相關

| 占位符 | 說明 | 您的實際值 | 出現位置 |
|:--------|:------|:-----------|:---------|
| `<Flow-Service-Principal-ID>` | Flow Service Principal 的 GUID | ________________ | 05 文件 GOV-017 |
| `{Flow Service Principal User ID}` | 同上（另一種寫法） | ________________ | 05 文件多處 |
| `GOV-FlowServicePrincipal` | Service Principal 顯示名稱 | ________________ | 01、02 文件 |

#### 取得方式

1. **Azure Portal 取得 GUID**：
   - 導覽路徑：Azure Portal → Azure Active Directory → Enterprise applications
   - 搜尋您建立的 Service Principal 名稱
   - 複製 **Object ID**

2. **Power Platform Admin Center 確認**：
   - 導覽路徑：Power Platform Admin Center → Environments → {環境} → Settings → Application users
   - 找到您的 Service Principal，複製 **Application ID**

---

### 2. 組織與環境相關

| 占位符 | 說明 | 您的實際值 | 出現位置 |
|:--------|:------|:-----------|:---------|
| `{org}` | Dataverse 環境的組織名稱 | ________________ | 06 文件 HTTP URI |
| `{tenant-id}` | Azure AD 租戶 ID | ________________ | 07 文件認證 |
| `{client-id}` | Azure AD 應用程式 ID | ________________ | 07 文件認證 |
| `{client-secret}` | Azure AD 應用程式密鑰 | ________________ | 07 文件認證 |

#### 取得方式

1. **取得組織名稱（org）**：
   - 導覽路徑：Power Apps Maker Portal → Settings (齒輪) → Session details
   - 從 Instance url 中提取（例如：`org12345` from `https://org12345.crm.dynamics.com`）

2. **取得租戶 ID**：
   - 導覽路徑：Azure Portal → Azure Active Directory → Overview
   - 複製 **Tenant ID**

---

### 3. URL 相關

| 占位符 | 說明 | 您的實際值 | 出現位置 |
|:--------|:------|:-----------|:---------|
| `{{base_url}}` | Dataverse Web API Base URL | ________________ | 07 文件測試案例 |
| `{Power App URL}` | 治理系統 Power App URL | ________________ | 05、06 文件通知 |
| `{Approvals App URL}` | Approvals App URL | ________________ | 05 文件通知 |
| `{SharePoint Site URL}` | 治理文件庫 SharePoint Site | ________________ | 03、05 文件 |

#### 取得方式

1. **Dataverse Base URL**：
   - 格式：`https://{org}.api.crm.dynamics.com/api/data/v9.2`
   - 範例：`https://org12345.api.crm.dynamics.com/api/data/v9.2`

2. **Power App URL**：
   - 導覽路徑：Power Apps Maker Portal → Apps → {您的 App} → Details
   - 複製 **Web link**

3. **Approvals App URL**：
   - 固定值：`https://flow.microsoft.com/manage/approvals`

---

### 4. Email 與通知相關

| 占位符 | 說明 | 您的實際值 | 出現位置 |
|:--------|:------|:-----------|:---------|
| `GOV-GovernanceLead@contoso.com` | Governance Lead 收件人 | ________________ | 05、06 文件 |
| `GOV-EngineeringManagement@contoso.com` | Engineering Management 收件人 | ________________ | 05、06 文件 |
| `GOV-SystemAdmin@contoso.com` | System Admin 收件人 | ________________ | 05、06 文件 |
| `GOV-Architects@contoso.com` | Architects 群組 | ________________ | 05 文件 |
| `GOV-SecurityReviewers@contoso.com` | Security Reviewers 群組 | ________________ | 05 文件 |
| `GOV-QAReviewers@contoso.com` | QA Reviewers 群組 | ________________ | 05 文件 |

#### 建議做法

1. **使用 Mail-enabled Security Group**：
   - 每個收件人應設定為 Microsoft 365 Security Group
   - 確保群組已啟用 Email 功能（Mail-enabled）

2. **命名建議**：
   - 保持 `GOV-` 前綴以識別治理系統相關群組
   - 範例：`GOV-GovernanceLead@yourcompany.com`

---

### 5. Teams 通知相關

| 占位符 | 說明 | 您的實際值 | 出現位置 |
|:--------|:------|:-----------|:---------|
| `{治理團隊 Team}` | Teams Team 名稱或 ID | ________________ | 05、06 文件 |
| `{違規通知 Channel}` | Teams Channel 名稱或 ID | ________________ | 05、06 文件 |
| `{一般通知 Channel}` | Teams Channel 名稱或 ID | ________________ | 05 文件 |

#### 取得方式

1. **取得 Team ID**：
   - 在 Teams 中，右鍵點擊 Team → Get link to team
   - 從 URL 中提取 `groupId` 參數

2. **取得 Channel ID**：
   - 在 Teams 中，右鍵點擊 Channel → Get link to channel
   - 從 URL 中提取 `channel` 參數

#### 建議 Channel 結構

```
治理系統 Team
├── General（一般通知）
├── Violations（違規通知）
├── Approvals（審批通知）
└── System（系統通知）
```

---

### 6. 測試帳號相關

| 占位符 | 說明 | 您的實際值 | 出現位置 |
|:--------|:------|:-----------|:---------|
| `testuser1@contoso.com` | System Architect 測試帳號 | ________________ | 07 文件 |
| `testuser2@contoso.com` | Project Manager 測試帳號 | ________________ | 07 文件 |
| `testgovlead@contoso.com` | Governance Lead 測試帳號 | ________________ | 07 文件 |
| `testsecurity@contoso.com` | Security Reviewer 測試帳號 | ________________ | 07 文件 |
| `testqa@contoso.com` | QA Reviewer 測試帳號 | ________________ | 07 文件 |
| `testadmin@contoso.com` | System Admin 測試帳號 | ________________ | 07 文件 |

#### 建議做法

1. **使用獨立測試帳號**：避免使用生產環境帳號進行測試
2. **角色對應**：確保測試帳號已加入對應的 Security Group
3. **授權確認**：確保測試帳號具有必要的 Power Platform 授權

---

## 環境準備檢查清單

完成占位符填寫後，請確認以下項目：

- [ ] 所有 Service Principal 相關占位符已填寫
- [ ] 所有 URL 相關占位符已填寫
- [ ] 所有 Email 相關占位符已填寫（或已建立對應群組）
- [ ] 所有 Teams 相關占位符已填寫（或已建立對應 Channel）
- [ ] 所有測試帳號已建立並加入對應群組

---

## 占位符替換建議

### 全域替換方式

在建置過程中，可使用以下方式快速替換占位符：

1. **文字編輯器**：使用「尋找與取代」功能
2. **命令列**：使用 `sed` 或 PowerShell `-replace`

### 範例（PowerShell）

```powershell
# 替換 Service Principal GUID
(Get-Content .\05-core-flows-implementation-runbook.md) -replace '<Flow-Service-Principal-ID>', 'actual-guid-here' | Set-Content .\05-core-flows-implementation-runbook.md

# 替換 Email
(Get-Content .\05-core-flows-implementation-runbook.md) -replace 'GOV-GovernanceLead@contoso.com', 'governance-lead@yourcompany.com' | Set-Content .\05-core-flows-implementation-runbook.md
```

> **注意**：建議在替換前備份原始文件。

---

**文件結束**

**下一步**：完成占位符填寫後，請繼續依 00A-build-order-and-bootstrap.md 開始建置。
