# 首次上線初始化清單

**文件版本**：v1.1
**生效日期**：2026-02-09
**文件擁有者**：System Design Governance Function
**文件性質**：一次性執行清單

---

## 本文件目的

本文件列出治理系統**首次上線前必須執行的初始化步驟**。

> **重要**：本清單僅需執行一次。執行完成後，系統即可正常運作，不需再次執行。

---

## 執行時機

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            初始化執行時機                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Phase 1 完成（環境、Dataverse、SharePoint、Power Apps UI）                  │
│                              │                                              │
│                              ▼                                              │
│                    ┌─────────────────────┐                                  │
│                    │   執行本初始化清單    │  ← 您現在在這裡                   │
│                    └─────────────────────┘                                  │
│                              │                                              │
│                              ▼                                              │
│  Phase 2 開始（建立 Flows）                                                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 初始化清單

### 1. Counter List 初始化

> **為何需要**：GOV-001 Flow 使用 Counter List 產生 RequestID。若 Counter List 無記錄，GOV-001 首次執行將失敗。

#### 操作步驟

1. **導覽路徑**：
   - 開啟瀏覽器，前往：https://make.powerapps.com
   - 右上角確認已選擇正確環境（如 GOV-PROD）
   - 左側選單 → **Tables** → 搜尋 `Counter List` → 點擊進入

2. **新增記錄**：
   - 點擊 **Data** 標籤
   - 點擊 **+ New row**

3. **填寫欄位**：

| 欄位 | 填寫值 | 說明 |
|:------|:-------|:------|
| CounterName | `ProjectRequest` | 計數器名稱（必填，對應 Doc 02 Schema: gov_countername） |
| Current Year | `2026` | 當前年份（必填） |
| Current Counter | `0` | 初始值（必填） |
| Prefix | `DR` | RequestID 前綴 |
| Last Updated | `{執行日期}` | 初始化日期 |

4. **儲存**：
   - 點擊 **Save & Close**

#### 驗證

```
驗證步驟：
1. 返回 Counter List 資料表的 Data 標籤
2. 確認存在一筆記錄
3. 確認欄位值：
   - CounterName = ProjectRequest
   - Current Counter = 0
   - Current Year = 2026

預期結果：存在一筆 CounterName 為 ProjectRequest 的記錄。
```

- [ ] **檢查點 1.1**：Counter List 存在 CounterName = ProjectRequest 的記錄
- [ ] **檢查點 1.2**：Current Counter 初始值為 0
- [ ] **檢查點 1.3**：Current Year 為 2026

---

### 2. Security Group 成員確認

> **為何需要**：Flow 發送 Approval 與通知時需要知道收件群組。若群組無成員，通知將無法送達。

#### 操作步驟

1. **導覽路徑**：
   - 前往：https://entra.microsoft.com
   - 左側選單 → **Groups** → **All groups**

2. **確認以下群組存在且有成員**：

| 群組名稱 | 用途 | 最少成員數 |
|---------|------|:----------:|
| GOV-Architects | System Architects 群組 | 1 |
| GOV-SecurityReviewers | Security 審核群組 | 1 |
| GOV-QAReviewers | QA 審核群組 | 1 |
| GOV-EngineeringManagement | 工程主管群組 | 1 |
| GOV-GovernanceLead | Governance Lead 群組 | 1 |
| GOV-ExecutiveManagement | Executive 審核群組 | 1 |
| GOV-FlowServicePrincipal | Flow 服務帳號群組 | 1 |

3. **若群組不存在**：
   - 返回 01-prerequisites-and-environment.md 建立群組

4. **若群組無成員**：
   - 點擊群組 → Members → Add members
   - 新增至少一位成員

#### 驗證

- [ ] **檢查點 2.1**：所有 7 個群組存在（與 Doc 01 第 5 章一致）
- [ ] **檢查點 2.2**：每個群組至少有 1 位成員

---

### 3. Service Principal 權限確認

> **為何需要**：Flow Service Principal 需要 Dataverse 與 SharePoint 的寫入權限。若權限不足，Flow 將無法寫入資料。

#### 操作步驟

1. **確認 Dataverse Application User**：
   - 導覽路徑：Power Platform Admin Center → Environments → {環境} → Settings → Users + permissions → Application users
   - 確認 `GOV-FlowServicePrincipal` 存在
   - 確認已指派 Security Role：`GOV-FlowServicePrincipal`

2. **確認 SharePoint 權限**：
   - 導覽路徑：SharePoint Admin Center → Sites → {治理系統 Site}
   - 確認 `GOV-FlowServicePrincipal` 具有 **Contribute** 權限

#### 驗證

- [ ] **檢查點 3.1**：Service Principal 為 Dataverse Application User
- [ ] **檢查點 3.2**：Service Principal 具有 Dataverse 寫入權限
- [ ] **檢查點 3.3**：Service Principal 具有 SharePoint 寫入權限

---

### 4. Connection Reference 建立確認

> **為何需要**：所有 Flow 使用 Connection Reference 而非個人連線，確保人員異動不影響系統運作。

#### 操作步驟

1. **導覽路徑**：
   - Power Automate Portal → Solutions → {治理系統 Solution}
   - 篩選：Type = Connection Reference

2. **確認以下 Connection Reference 存在**：

| Connection Reference 名稱 | Connector | 身分 |
|:--------------------------|:-----------|:------|
| CR-Dataverse-SPN | Microsoft Dataverse | Flow Service Principal |
| CR-SharePoint-SPN | SharePoint | Flow Service Principal |
| CR-Approvals | Approvals | Flow Service Principal |
| CR-Outlook | Office 365 Outlook | Flow Service Principal |
| CR-Teams | Microsoft Teams | Flow Service Principal |

3. **若 Connection Reference 不存在**：
   - 點擊 **New** → **Connection Reference**
   - 填寫 Display Name
   - 選擇 Connector
   - 選擇或建立使用 Service Principal 的 Connection

#### 驗證

- [ ] **檢查點 4.1**：所有 5 個 Connection Reference 存在
- [ ] **檢查點 4.2**：每個 Connection Reference 已連接至有效 Connection

---

### 5. Dataverse Audit 啟用確認

> **為何需要**：GOV-017 Guardrail Monitor 需要查詢 Dataverse Audit Log 來偵測違規修改。若 Audit 未啟用，GOV-017 無法運作。

#### 操作步驟

1. **導覽路徑**：
   - Power Platform Admin Center → Environments → {環境} → Settings → Audit and logs → Audit settings

2. **確認設定**：

| 設定項目 | 必須值 |
|:---------|:-------|
| Start Auditing | **On** |
| Log access | On（建議） |
| Read logs | On（建議） |

3. **確認資料表層級 Audit**：
   - Power Apps Maker Portal → Tables → {每個治理資料表} → Properties
   - 確認 **Enable auditing** 已勾選

#### 驗證

- [ ] **檢查點 5.1**：環境層級 Audit 已啟用
- [ ] **檢查點 5.2**：gov_projectregistry Audit 已啟用
- [ ] **檢查點 5.3**：gov_reviewdecisionlog Audit 已啟用
- [ ] **檢查點 5.4**：gov_riskassessmenttable Audit 已啟用

---

### 6. 首次測試專案建立（Flow 建立後執行）

> **為何需要**：確認 GOV-001 Flow 可正確產生 RequestID 並寫入 Dataverse。

#### 執行時機

此步驟需在 **Phase 2 完成 GOV-001 Flow 建立後**執行。

#### 操作步驟

1. **使用 Postman 或 Power Apps 提交專案建立請求**

2. **填寫測試資料**：

| 欄位 | 測試值 |
|:------|:-------|
| Title | `INIT-TEST-001` |
| ProjectType | `NewSystem` |
| TargetSL | `SL2` |
| SystemArchitect | `{您的 Email}` |
| ProjectDescription | `首次初始化測試專案` |

3. **等待 GOV-001 執行完成**（約 5-10 秒）

#### 驗證

1. **查詢 Project Registry**：
   - 導覽路徑：Power Apps Maker Portal → Tables → Project Registry → Data
   - 找到 Title = `INIT-TEST-001` 的記錄

2. **確認欄位值**：

| 欄位 | 預期值 |
|:------|:-------|
| RequestID | `DR-2026-{####}`（4 位序號，如 DR-2026-0001） |
| CurrentGate | `Pending` |
| ProjectStatus | `Active` |
| RequestStatus | `None` |

3. **確認 Counter List 已遞增**：
   - 查詢 Counter List
   - Current Value 應從 0 變為 1

4. **確認 SharePoint 資料夾已建立**：
   - 導覽路徑：SharePoint Site → Documents → {RequestID}
   - 確認存在 6 個子資料夾（01_Feasibility, 02_Risk_Assessment, 03_Design, 04_Security, 05_Test, 06_Handover）

- [ ] **檢查點 6.1**：RequestID 格式正確（DR-2026-####，如 DR-2026-0001）
- [ ] **檢查點 6.2**：Counter List Current Value 已遞增
- [ ] **檢查點 6.3**：SharePoint 資料夾已建立
- [ ] **檢查點 6.4**：Review Decision Log 存在一筆 ProjectCreation 記錄

---

## 初始化完成確認

### 總檢查清單

| 區塊 | 檢查點數 | 全部通過 |
|------|:--------:|:--------:|
| 1. Counter List 初始化 | 3 | ☐ |
| 2. Security Group 成員確認 | 2 | ☐ |
| 3. Service Principal 權限確認 | 3 | ☐ |
| 4. Connection Reference 建立確認 | 2 | ☐ |
| 5. Dataverse Audit 啟用確認 | 4 | ☐ |
| 6. 首次測試專案建立 | 4 | ☐ |
| **總計** | **18** | ☐ |

### 初始化完成宣告

當上述 18 個檢查點全部通過後，請在下方簽核：

```
初始化執行日期：____________________
執行人員：____________________
驗證人員：____________________
備註：____________________
```

---

## 後續步驟

初始化完成後：

1. **繼續 Phase 2**：建立所有 GOV Flows（05 文件）
2. **完成 Phase 3**：連接 Flow 至 Power Apps、執行測試（04 文件階段二 + 07 文件）
3. **正式啟用**：通知使用者系統上線

---

## 故障排除

### 問題 1：GOV-001 執行失敗，錯誤訊息包含「Counter List」

**原因**：Counter List 未初始化或記錄不存在

**解決方式**：
1. 確認 Counter List 存在 CounterName = `ProjectRequest` 的記錄
2. 確認 Current Value 欄位有值（數字）

### 問題 2：GOV-001 執行失敗，錯誤訊息包含「Unauthorized」或「Forbidden」

**原因**：Service Principal 權限不足

**解決方式**：
1. 確認 Service Principal 為 Dataverse Application User
2. 確認已指派正確的 Security Role
3. 確認 Security Role 對 gov_projectregistry 有 Create 權限

### 問題 3：SharePoint 資料夾未建立

**原因**：Service Principal 無 SharePoint 寫入權限

**解決方式**：
1. 確認 Service Principal 在 SharePoint Site 具有 Edit 權限
2. 確認 SharePoint Site URL 在環境變數中正確設定

### 問題 4：通知未送達

**原因**：Security Group 無成員或 Email 設定錯誤

**解決方式**：
1. 確認目標 Security Group 有成員
2. 確認 Security Group 為 Mail-enabled
3. 檢查 Flow 中的收件人設定

---

**文件結束**

---

## 版本歷史

| 版本 | 日期 | 變更說明 |
|:------|:------|:----------|
| v1.0 | 2026-02-09 | 初版建立 |
| v1.1 | 2026-02-11 | 鑑識修訂：Counter List 欄位名稱對齊 Doc 02（CounterType→CounterName, CurrentValue→CurrentCounter）、安全群組名稱對齊 Doc 01（7 群組）、Service Principal 角色名稱修正、SharePoint 資料夾結構對齊 Doc 03、RequestID 格式統一為 DR-{YYYY}-{####} |

---

**下一步**：完成本清單後，請繼續 Phase 2（05-core-flows-implementation-runbook.md）。
