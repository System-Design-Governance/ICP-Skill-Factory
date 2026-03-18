
# 設計治理系統：測試與驗收手冊

**文件編號**：IMPL-07-TEST-ACCEPTANCE
**版本**：1.3
**最後更新**：2026-02-11
**適用範圍**：系統整合測試、反作弊測試、部署檢查、上線驗收標準
**前置文件**：01-06 實作文件

---


## 第一部分：測試環境準備

## 測試環境架構

### 環境清單

| 環境代號 | 用途 | Dataverse 環境名稱 | Flow 狀態 | 適用對象 |
|:--------|:-----|:------------------|:---------|:--------|
| **DEV** | 開發測試 | dev-governance | Unpublished | 開發人員 |
| **QA** | 整合測試 | qa-governance | Published（僅測試使用者） | 測試團隊 |
| **UAT** | 使用者驗收測試 | uat-governance | Published（限定使用者） | 業務代表、審核者 |
| **PROD** | 正式環境 | prod-governance | Published（全公司） | 全體使用者 |

### 建立 QA 環境

**導覽路徑**：
1. 開啟 Power Platform Admin Center：`https://admin.powerplatform.microsoft.com`
2. 左側導覽 → 「環境」
3. 點擊「+ 新增」

**欄位設定**：
| 欄位 | 設定值 |
|:----|:------|
| 名稱 | `qa-governance` |
| 類型 | Sandbox |
| 區域 | （依公司政策選擇） |
| 目的 | 測試 |
| 建立資料庫 | 是 |
| 語言 | 繁體中文 |
| 貨幣 | TWD |

**確認此步驟成功**：
- [ ] 環境清單中出現 `qa-governance`
- [ ] 環境狀態顯示為「就緒」
- [ ] 可以開啟 Maker Portal 並連接到此環境

---

## 測試資料準備

### 測試專案定義

**測試專案 1（Happy Path 測試用）**：
```
Title: "TEST-NewSystem-001"
ProjectType: NewSystem
TargetSL: SL2
SystemArchitect: testuser1@contoso.com
ProjectManager: testuser2@contoso.com
ProjectDescription: "測試專案 - 驗證完整 Gate 流程"
```

**測試專案 2（Anti-Cheating 測試用）**：
```
Title: "TEST-MajorArchChange-002"
ProjectType: MajorArchChange
TargetSL: SL3
SystemArchitect: testuser3@contoso.com
ProjectManager: testuser4@contoso.com
ProjectDescription: "測試專案 - 驗證反作弊機制"
```

**測試專案 3（拒絕路徑測試用）**：
```
Title: "TEST-Enhancement-003"
ProjectType: Enhancement
TargetSL: SL1
SystemArchitect: testuser5@contoso.com
ProjectManager: testuser6@contoso.com
ProjectDescription: "測試專案 - 驗證 Rework 機制"
```

### 測試使用者帳號

| 帳號 | 角色 | 用途 |
|:----|:-----|:----|
| `testuser1@contoso.com` | System Architect | 一般操作測試 |
| `testuser2@contoso.com` | Project Manager | PM 操作測試 |
| `testsecurity@contoso.com` | Security Reviewer | Security Review 測試 |
| `testqa@contoso.com` | QA Reviewer | QA Review 測試 |
| `testgovlead@contoso.com` | Governance Lead | Governance Approval 測試 |
| `testem@contoso.com` | Engineering Management | Gate 0/2 審批測試 |
| `testexec@contoso.com` | Executive Management | High Risk Acceptance 測試 |

### 建立測試使用者

**導覽路徑**：
1. Microsoft Entra 管理中心：`https://entra.microsoft.com`
2. 左側導覽 → 「使用者」→「所有使用者」
3. 點擊「+ 新增使用者」→「建立新使用者」

**欄位設定（以 testuser1 為例）**：
| 欄位 | 設定值 |
|:----|:------|
| 使用者主體名稱 | `testuser1` |
| 郵件暱稱 | `testuser1` |
| 顯示名稱 | `Test User 1 (System Architect)` |
| 密碼 | （自動產生或自訂） |
| 帳戶已啟用 | 是 |

**確認此步驟成功**：
- [ ] 使用者帳號已建立
- [ ] 可以使用帳號登入 Power Apps

---

## 測試工具準備

### 必要工具清單

| 工具 | 用途 | 取得方式 |
|:----|:-----|:--------|
| **Power Apps Test Studio** | UI 自動化測試 | Power Apps Maker Portal 內建 |
| **Postman** | HTTP API 測試 | `https://www.postman.com/downloads/` |
| **Power Automate Run History** | Flow 執行驗證 | Power Automate Portal 內建 |
| **Dataverse Web API** | 直接資料驗證 | OData Endpoint |
| **Application Insights** | 監控與錯誤追蹤 | Azure Portal |

### 設定 Postman 環境

**步驟 1：建立新環境**

**導覽路徑**：Postman → Environments → Create Environment

**環境變數設定**：
| 變數名稱 | 值 |
|:--------|:--|
| `base_url` | `https://<org>.api.crm.dynamics.com/api/data/v9.2` |
| `access_token` | （每次測試前取得新 Token） |
| `org_id` | （您的 Dataverse 組織 ID） |

**步驟 2：建立測試請求集合**

建立新 Collection：「Governance System Tests」

**請求範例 - 查詢專案狀態**：
```http
GET {{base_url}}/gov_projectregistries?$filter=gov_requestid eq 'DR-2026-0001'&$select=gov_requestid,gov_currentgate,gov_projectstatus,gov_requeststatus

Headers:
Authorization: Bearer {{access_token}}
Content-Type: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**確認此步驟成功**：
- [ ] Postman 環境已建立
- [ ] 可以成功發送請求並取得回應

---

## 第二部分：端對端測試案例

## 完整 Gate 流程測試（Happy Path）

### 測試目標
驗證專案從建立到 Gate 3 通過的完整流程，確保所有 Flows 正確協作。

### 測試案例 E2E-001：專案建立至 Gate 3 完整流程

#### Phase 1：專案建立（GOV-001）

**前置條件**：
- 測試使用者 `testuser1@contoso.com` 已登入 Power Apps
- 無重複的 RequestID

**測試步驟**：

| 步驟 | 操作 | 導覽路徑 |
|:----|:-----|:--------|
| 1 | 開啟專案建立 Form | Power Apps → Design Governance → 專案建立 |
| 2 | 填寫專案名稱 | Title: `TEST-NewSystem-001` |
| 3 | 選擇專案類型 | ProjectType: `NewSystem` |
| 4 | 選擇目標 SL | TargetSL: `SL2` |
| 5 | 選擇 System Architect | `testuser1@contoso.com` |
| 6 | 選擇 Project Manager | `testuser2@contoso.com` |
| 7 | 填寫專案描述 | ProjectDescription: `測試專案描述` |
| 8 | 點擊「提交」按鈕 | 等待 Flow 執行完成（約 5-10 秒） |

**預期結果驗證**：

| 驗證項目 | 預期值 | 驗證方法 |
|:--------|:------|:--------|
| HTTP 回應 | 200 OK | Power Apps 畫面顯示成功 |
| RequestID | `DR-2026-{ShortGuid}` | 畫面顯示新建立的 RequestID |
| CurrentGate | `Pending` | 查詢 Dataverse |
| ProjectStatus | `Active` | 查詢 Dataverse |
| RequestStatus | `None` | 查詢 Dataverse |
| SharePoint 資料夾 | 建立 6 個資料夾 | 查看 SharePoint 文件庫 |
| Review Decision Log | 新增 1 筆 `ProjectCreation` | 查詢 Dataverse |
| 通知 | System Architect 收到「專案已建立」通知 | 檢查 Email + Teams |

**Dataverse 驗證查詢**：
```http
GET {{base_url}}/gov_projectregistries?$filter=gov_title eq 'TEST-NewSystem-001'&$select=gov_requestid,gov_currentgate,gov_projectstatus,gov_requeststatus,createdon
```

**確認此步驟成功**：
- [ ] 畫面顯示「專案建立成功」
- [ ] RequestID 已產生
- [ ] SharePoint 資料夾已建立

---

#### Phase 2：Gate 0 審批流程（GOV-002 + GOV-003）

**前置條件**：
- Phase 1 已完成（CurrentGate = Pending）

**步驟 2.1：上傳 Gate 0 必要文件**

| 步驟 | 操作 | 導覽路徑 |
|:----|:-----|:--------|
| 1 | 開啟文件上傳 Form | Power Apps → Design Governance → 文件上傳 |
| 2 | 選擇專案 | `TEST-NewSystem-001` |
| 3 | 上傳技術可行性評估 | DocumentType: `TechnicalFeasibility` |
| 4 | 上傳初步風險清單 | DocumentType: `PreliminaryRiskList` |
| 5 | 上傳風險評估策略 | DocumentType: `RiskAssessmentStrategy` |

**步驟 2.2：提交 Gate 0 申請**

| 步驟 | 操作 | 導覽路徑 |
|:----|:-----|:--------|
| 1 | 開啟 Gate 申請 Form | Power Apps → Design Governance → Gate 申請 |
| 2 | 選擇專案 | `TEST-NewSystem-001` |
| 3 | 選擇 RequestedGate | `Gate0` |
| 4 | 點擊「提交」 | 等待 Flow 執行完成 |

**步驟 2.3：Engineering Management 審批**

| 步驟 | 操作 | 導覽路徑 |
|:----|:-----|:--------|
| 1 | 登入 Approvals App | `testem@contoso.com` 帳號 |
| 2 | 開啟審批請求 | 找到「Gate 0 審批請求 - DR-2026-xxx」 |
| 3 | 點擊 Approve | 填寫 Comments：「通過 Gate 0 審批」 |
| 4 | 點擊 Submit | 等待 Flow 執行完成 |

**預期結果驗證**：

| 驗證項目 | 預期值 | 驗證方法 |
|:--------|:------|:--------|
| CurrentGate | `Gate0` | 查詢 Dataverse |
| Gate0PassedDate | `{當前時間}` | 查詢 Dataverse |
| RequestStatus | `None` | 查詢 Dataverse |
| Review Decision Log | Decision = `Approved` | 查詢 Dataverse |
| 通知 | System Architect 收到「Gate 0 已通過」 | 檢查 Email + Teams |

**確認此步驟成功**：
- [ ] CurrentGate 已更新為 Gate0
- [ ] Gate0PassedDate 已記錄
- [ ] 通知已發送

---

#### Phase 3：Gate 1 審批流程（三層審批）

**前置條件**：
- Phase 2 已完成（CurrentGate = Gate0）

**步驟 3.1：上傳 Gate 1 必要文件（7 份）**

| DocumentType | 檔案說明 |
|:------------|:--------|
| `DesignBaseline` | 設計基線文件 |
| `RiskAssessment` | 風險評估報告 |
| `IEC62443Checklist` | IEC 62443 檢查表 |
| `ThreatModel` | 威脅模型分析 |
| `RequirementTraceability` | 需求追溯矩陣 |
| `DocumentRegister` | 文件清冊 |
| `DesignObjectInventory` | 設計物件清單 |

**步驟 3.2：提交 Gate 1 申請**

| 步驟 | 操作 |
|:----|:-----|
| 1 | 開啟 Gate 申請 Form |
| 2 | 選擇專案 `TEST-NewSystem-001` |
| 3 | 選擇 RequestedGate: `Gate1` |
| 4 | 點擊「提交」 |

**步驟 3.3：第一層審批 - Security Review**

| 步驟 | 操作 | 執行者 |
|:----|:-----|:------|
| 1 | 登入 Approvals App | `testsecurity@contoso.com` |
| 2 | 開啟「Gate 1 Security Review」 | 找到對應的審批請求 |
| 3 | 點擊 Approve | Comments：「Security Review 通過」 |

**步驟 3.4：第二層審批 - QA Review**

| 步驟 | 操作 | 執行者 |
|:----|:-----|:------|
| 1 | 等待第一層完成後 | 系統自動發送第二層審批請求 |
| 2 | 登入 Approvals App | `testqa@contoso.com` |
| 3 | 開啟「Gate 1 QA Review」 | 找到對應的審批請求 |
| 4 | 點擊 Approve | Comments：「QA Review 通過」 |

**步驟 3.5：第三層審批 - Governance Approval**

| 步驟 | 操作 | 執行者 |
|:----|:-----|:------|
| 1 | 等待第二層完成後 | 系統自動發送第三層審批請求 |
| 2 | 登入 Approvals App | `testgovlead@contoso.com` |
| 3 | 開啟「Gate 1 Governance Approval」 | 找到對應的審批請求 |
| 4 | 點擊 Approve | Comments：「Governance Approval 通過」 |

**預期結果驗證**：

| 驗證項目 | 預期值 |
|:--------|:------|
| CurrentGate | `Gate1` |
| Gate1PassedDate | `{當前時間}` |
| Gate1SecurityReviewStatus | `Approved` |
| Gate1QAReviewStatus | `Approved` |
| Gate1GovernanceReviewStatus | `Approved` |
| Review Decision Log | 3 筆審批記錄 |

**確認此步驟成功**：
- [ ] 三層審批皆已完成
- [ ] CurrentGate 已更新為 Gate1
- [ ] 所有審批狀態已記錄

---

#### Phase 4：Gate 2 審批流程

**前置條件**：
- Phase 3 已完成（CurrentGate = Gate1）

**步驟 4.1：上傳 Gate 2 必要文件（2 份）**

| DocumentType | 檔案說明 |
|:------------|:--------|
| `TestResults` | 測試結果報告 |
| `IntegrationReport` | 整合測試報告 |

**步驟 4.2：提交 Gate 2 申請並審批**

（步驟同 Gate 0，由 Engineering Management 審批）

**預期結果驗證**：

| 驗證項目 | 預期值 |
|:--------|:------|
| CurrentGate | `Gate2` |
| Gate2PassedDate | `{當前時間}` |

---

#### Phase 5：Risk Acceptance（GOV-013 + GOV-004）

**前置條件**：
- Phase 4 已完成（CurrentGate = Gate2）

**步驟 5.1：建立風險評估記錄**

| 步驟 | 操作 | 導覽路徑 |
|:----|:-----|:--------|
| 1 | 開啟風險評估 Form | Power Apps → Design Governance → 風險評估 |
| 2 | 選擇專案 | `TEST-NewSystem-001` |
| 3 | 新增風險項目 | RiskCategory: `Technical`, RiskLevel: `Medium` |
| 4 | 設定風險負責人 | RiskOwner: `testem@contoso.com` |
| 5 | 點擊「儲存」 | |

**步驟 5.2：提交 Gate 3 申請（觸發 Risk Acceptance）**

| 步驟 | 操作 |
|:----|:-----|
| 1 | 開啟 Gate 申請 Form |
| 2 | 選擇專案 `TEST-NewSystem-001` |
| 3 | 選擇 RequestedGate: `Gate3` |
| 4 | 點擊「提交」 |

**系統自動行為**：
1. GOV-002 呼叫 GOV-013 Risk Level Calculator
2. GOV-013 計算 HighestResidualRiskLevel = Medium
3. GOV-002 呼叫 GOV-004 Risk Acceptance
4. GOV-004 發送 Approval 給 Risk Owner

**步驟 5.3：Risk Owner 審批**

| 步驟 | 操作 | 執行者 |
|:----|:-----|:------|
| 1 | 登入 Approvals App | `testem@contoso.com` |
| 2 | 開啟「Risk Acceptance」請求 | |
| 3 | 點擊 Approve | Comments：「Medium Risk 可接受」 |

**預期結果驗證**：

| 驗證項目 | 預期值 |
|:--------|:------|
| RiskAcceptanceStatus | `Accepted` |
| RiskOwner | `testem@contoso.com` |
| RiskAcceptanceDate | `{當前時間}` |

---

#### Phase 6：Gate 3 審批流程（雙層審批）

**前置條件**：
- Phase 5 已完成（RiskAcceptanceStatus = Accepted）

**步驟 6.1：上傳 Gate 3 必要文件**

| DocumentType | 檔案說明 |
|:------------|:--------|
| `FinalTestReport` | 最終測試報告 |
| `HandoverDocument` | 交接文件 |
| `ResidualRiskList` | 殘餘風險清單 |

**步驟 6.2：QA Review 審批**

| 步驟 | 操作 | 執行者 |
|:----|:-----|:------|
| 1 | 登入 Approvals App | `testqa@contoso.com` |
| 2 | 開啟「Gate 3 QA Review」 | |
| 3 | 點擊 Approve | Comments：「QA Review 通過」 |

**步驟 6.3：Governance Approval 審批**

| 步驟 | 操作 | 執行者 |
|:----|:-----|:------|
| 1 | 登入 Approvals App | `testgovlead@contoso.com` |
| 2 | 開啟「Gate 3 Governance Approval」 | |
| 3 | 點擊 Approve | Comments：「Governance Approval 通過」 |

**預期結果驗證**：

| 驗證項目 | 預期值 | 驗證方法 |
|:--------|:------|:--------|
| CurrentGate | `Gate3` | 查詢 Dataverse |
| Gate3PassedDate | `{當前時間}` | 查詢 Dataverse |
| DocumentFreezeStatus | `Frozen` | 查詢 Dataverse |
| SharePoint 資料夾 | 唯讀權限 | 嘗試上傳新文件（應失敗） |

**確認此步驟成功**：
- [ ] CurrentGate = Gate3
- [ ] 所有 GatePassedDate 皆有值
- [ ] DocumentFreezeStatus = Frozen
- [ ] SharePoint 資料夾已設為唯讀

---

## 拒絕路徑測試（Rejection Path）

### 測試案例 E2E-002：Gate 0 審批拒絕與重工

**測試目標**：驗證審批拒絕時，系統正確處理 Rework 流程。

**前置條件**：
- 測試專案已建立（CurrentGate = Pending）
- Gate 0 申請已提交（RequestStatus = Pending）

**測試步驟**：

| 步驟 | 操作 | 執行者 |
|:----|:-----|:------|
| 1 | 登入 Approvals App | `testem@contoso.com` |
| 2 | 開啟「Gate 0 審批請求」 | |
| 3 | 點擊 **Reject** | |
| 4 | 填寫 Comments | 「文件不齊全，請補充技術可行性評估」 |
| 5 | 點擊 Submit | |

**預期結果驗證**：

| 驗證項目 | 預期值 | 驗證方法 |
|:--------|:------|:--------|
| CurrentGate | `Pending`（保持不變） | 查詢 Dataverse |
| RequestStatus | `None`（已清空） | 查詢 Dataverse |
| ReworkCount | `1`（遞增） | 查詢 Dataverse |
| Review Decision Log | Decision = `Rejected` | 查詢 Dataverse |
| 通知 | System Architect 收到「Gate 0 被拒絕」通知 + 拒絕原因 | 檢查 Email + Teams |
| GOV-016 | Rework Loop Handler 已執行 | 查看 Flow Run History |

**確認此步驟成功**：
- [ ] ReworkCount 已遞增
- [ ] 通知包含拒絕原因
- [ ] 專案可重新提交 Gate 0 申請

---

### 測試案例 E2E-003：Gate 1 第二層拒絕（QA Reject）

**測試目標**：驗證多層審批中，任一層拒絕則終止流程。

**前置條件**：
- 專案已通過 Gate 0（CurrentGate = Gate0）
- Gate 1 申請已提交
- Security Review 已 Approve

**測試步驟**：

| 步驟 | 操作 | 執行者 |
|:----|:-----|:------|
| 1 | Security Review Approve | `testsecurity@contoso.com` |
| 2 | 登入 Approvals App | `testqa@contoso.com` |
| 3 | 開啟「Gate 1 QA Review」 | |
| 4 | 點擊 **Reject** | |
| 5 | 填寫 Comments | 「需求追溯矩陣不完整」 |
| 6 | 點擊 Submit | |

**預期結果驗證**：

| 驗證項目 | 預期值 |
|:--------|:------|
| CurrentGate | `Gate0`（保持不變） |
| Gate1SecurityReviewStatus | `Approved` |
| Gate1QAReviewStatus | `Rejected` |
| Gate1GovernanceReviewStatus | `null`（未執行） |
| 通知 | System Architect 收到「QA Review 被拒絕」通知 |
| Flow 終止 | Governance Approval 未發送 |

**確認此步驟成功**：
- [ ] 第三層審批未執行
- [ ] ReworkCount 已遞增
- [ ] 專案可重新提交 Gate 1 申請

---

### 測試案例 E2E-004：重工次數達到上限（OnHold）

**測試目標**：驗證 ReworkCount >= 3 時，專案自動暫停。

**前置條件**：
- 專案 ReworkCount = 2（已被拒絕 2 次）
- Gate 0 申請第 3 次被拒絕

**測試步驟**：

| 步驟 | 操作 |
|:----|:-----|
| 1 | 提交 Gate 0 申請（第 3 次） |
| 2 | Engineering Management Reject |

**預期結果驗證**：

| 驗證項目 | 預期值 | 驗證方法 |
|:--------|:------|:--------|
| ReworkCount | `3` | 查詢 Dataverse |
| ProjectStatus | `OnHold` | 查詢 Dataverse |
| 通知 | System Architect + PM + Governance Lead 收到「合規警報」 | 檢查 Email + Teams |
| 通知內容 | 「專案重工次數已達 3 次，專案已自動暫停」 | 檢查通知內容 |

**確認此步驟成功**：
- [ ] ProjectStatus = OnHold
- [ ] 專案無法繼續提交 Gate 申請
- [ ] 需 Engineering Management 解除 OnHold

---

## 冪等性與並發測試

### 測試案例 E2E-005：重複提交相同 RequestID

**測試目標**：驗證系統拒絕重複的 RequestID。

**前置條件**：
- 專案已建立，RequestID = `DR-2026-0001`

**測試步驟**：

| 步驟 | 操作 |
|:----|:-----|
| 1 | 使用相同 RequestID 再次呼叫 GOV-001 |

**預期結果驗證**：

| 驗證項目 | 預期值 |
|:--------|:------|
| HTTP Response | 400 Bad Request |
| ErrorCode | `ERR-001-010` |
| Message | 「RequestID 已存在」 |
| Project Registry 記錄數 | 仍為 1 筆（未重複建立） |

---

### 測試案例 E2E-006：並行 Gate Request

**測試目標**：驗證同一專案的並行請求序列執行。

**測試步驟**：

| 步驟 | 操作 |
|:----|:-----|
| 1 | 使用 Postman 同時發送兩筆 Gate 0 Request（間隔 < 1 秒） |
| 2 | Request 1：Gate0 申請 |
| 3 | Request 2：Gate0 申請（重複） |

**預期結果驗證**：

| 驗證項目 | 預期值 |
|:--------|:------|
| Request 1 | 正常執行，RequestStatus = Pending |
| Request 2 | 回傳錯誤 ERR-002-058（RequestStatus 衝突） |
| 執行順序 | Request 2 的處理時間 > Request 1 的開始時間 |

---

## PreGate0 與專案狀態測試

### 測試案例 E2E-007：PreGate0 狀態驗證

**測試目標**：驗證專案建立後進入 PreGate0 狀態（Active + Pending），確認專案一建立即進入治理監控範圍。

**前置條件**：
- 測試使用者 `testuser1@contoso.com` 已登入 Power Apps
- Counter List 中有可用的序號
- 無重複的 RequestID

**測試步驟**：

| 步驟 | 操作 | 導覽路徑 |
|:----|:-----|:--------|
| 1 | 開啟專案建立 Form | Power Apps → Design Governance → 專案建立 |
| 2 | 填寫專案名稱 | Title: `TEST-PreGate0-001` |
| 3 | 選擇專案類型 | ProjectType: `NewSystem` |
| 4 | 選擇目標 SL | TargetSL: `SL2` |
| 5 | 選擇 System Architect | `testuser1@contoso.com` |
| 6 | 選擇 Project Manager | `testuser2@contoso.com` |
| 7 | 填寫專案描述 | ProjectDescription: `PreGate0 狀態測試專案` |
| 8 | 點擊「提交」按鈕 | 等待 GOV-001 執行完成（約 5-10 秒） |

**預期結果驗證**：

| 驗證項目 | 預期值 | 驗證方法 | 說明 |
|:--------|:------|:--------|:-----|
| HTTP 回應 | 200 OK | Power Apps 畫面顯示成功 | |
| RequestID | `DR-2026-{ShortGuid}` | 畫面顯示新建立的 RequestID | |
| **ProjectStatus** | **Active** | 查詢 Dataverse | PreGate0 狀態的第一個條件 |
| **CurrentGate** | **Pending** | 查詢 Dataverse | PreGate0 狀態的第二個條件 |
| RequestStatus | `None` | 查詢 Dataverse | 尚未提交任何 Gate 申請 |
| SharePoint 資料夾 | 已建立 6 個子資料夾 | 查看 SharePoint 文件庫 | 專案資料夾在 PreGate0 即建立 |
| Review Decision Log | 1 筆 `ProjectCreation` | 查詢 Dataverse | 已進入治理監控範圍 |
| 通知 | System Architect 收到「專案已建立」 | 檢查 Email + Teams | |

**Dataverse 驗證查詢**：
```http
GET {{base_url}}/gov_projectregistries?$filter=gov_title eq 'TEST-PreGate0-001'&$select=gov_requestid,gov_currentgate,gov_projectstatus,gov_requeststatus,createdon

預期回應：
{
    "gov_requestid": "DR-2026-xxxx",
    "gov_currentgate": 807660000,  // Pending
    "gov_projectstatus": 807660000, // Active
    "gov_requeststatus": 807660000, // None
    "createdon": "2026-02-08T..."
}
```

**確認此步驟成功**：
- [ ] ProjectStatus = Active (807660000)
- [ ] CurrentGate = Pending (807660000)
- [ ] 專案處於 PreGate0 狀態（Active + Pending 組合）
- [ ] SharePoint 資料夾已建立（不等待 Gate 0 通過）
- [ ] 專案已進入治理監控範圍（有 Review Decision Log）

**PreGate0 狀態說明**：
- PreGate0 **不是**獨立的專案狀態
- PreGate0 = `ProjectStatus: Active (807660000)` + `CurrentGate: Pending (807660000)`
- 專案建立後即處於 Active 狀態，證明專案一旦建立即進入治理範圍
- Draft 狀態已淘汰，不存在「草稿」概念

---

### 測試案例 E2E-008：Terminated 異常終止流程

**測試目標**：驗證專案在任一階段可被異常終止，且終止後狀態為 Terminated（非 Closed）。

**前置條件**：
- 測試專案已建立且處於 Active 狀態
- CurrentGate 可為任一狀態（Pending / Gate0 / Gate1 / Gate2）
- 使用者具有終止專案的權限

**測試步驟**：

| 步驟 | 操作 | 導覽路徑 |
|:----|:-----|:--------|
| 1 | 開啟專案終止 Form | Power Apps → Design Governance → 專案終止 |
| 2 | 選擇專案 | 選擇要終止的測試專案 |
| 3 | 選擇終止原因 | TerminationReason: `BusinessDecision` |
| 4 | 填寫終止說明 | TerminationComments: `業務需求變更，專案不再繼續` |
| 5 | 確認終止決策 | 勾選「我確認終止此專案」 |
| 6 | 點擊「提交終止申請」 | 等待 Flow 執行完成 |

**步驟 2：Governance Lead 審批終止**

| 步驟 | 操作 | 執行者 |
|:----|:-----|:------|
| 1 | 登入 Approvals App | `testgovlead@contoso.com` |
| 2 | 開啟「專案終止審批」 | 找到對應的終止請求 |
| 3 | 點擊 Approve | Comments：「同意終止，業務需求確實已變更」 |
| 4 | 點擊 Submit | 等待 Flow 執行完成 |

**預期結果驗證**：

| 驗證項目 | 預期值 | 驗證方法 | 說明 |
|:--------|:------|:--------|:-----|
| **ProjectStatus** | **Terminated (807660003)** | 查詢 Dataverse | 異常終止狀態 |
| CurrentGate | `{終止前的值}`（保持不變） | 查詢 Dataverse | 記錄終止發生在哪個 Gate |
| TerminationReason | `BusinessDecision` | 查詢 Dataverse | 記錄終止原因 |
| TerminationDate | `{當前時間}` | 查詢 Dataverse | 記錄終止時間 |
| TerminatedBy | `testgovlead@contoso.com` | 查詢 Dataverse | 記錄決策者 |
| DocumentFreezeStatus | `NotFrozen` | 查詢 Dataverse | Terminated 不凍結文件 |
| SharePoint 資料夾 | 仍可存取（唯讀） | 查看 SharePoint | 保留稽核記錄 |
| Review Decision Log | 新增 `ProjectTermination` | 查詢 Dataverse | 記錄終止決策 |
| 通知 | System Architect + PM 收到終止通知 | 檢查 Email + Teams | |

**Dataverse 驗證查詢**：
```http
GET {{base_url}}/gov_projectregistries?$filter=gov_projectstatus eq 807660003&$select=gov_requestid,gov_projectstatus,gov_currentgate,gov_terminationreason,gov_terminationdate,gov_terminatedby

預期回應：
{
    "gov_requestid": "DR-2026-xxxx",
    "gov_projectstatus": 807660003,  // Terminated
    "gov_currentgate": 807660001,    // 例：Gate0（終止前的狀態）
    "gov_terminationreason": "BusinessDecision",
    "gov_terminationdate": "2026-02-08T...",
    "gov_terminatedby": {...}
}
```

**確認此步驟成功**：
- [ ] ProjectStatus = Terminated (807660003)
- [ ] 終止原因與時間已記錄
- [ ] DocumentFreezeStatus = NotFrozen（異常終止不凍結）
- [ ] 專案無法繼續提交 Gate 申請
- [ ] 稽核記錄已保留（Review Decision Log + SharePoint）

**Terminated vs Closed 區別**：
- **Terminated（異常終止）**：
  - 未通過 Gate 3
  - 可能在任何階段終止
  - 需記錄終止原因與決策者
  - 文件不凍結（保留現狀）
  - 無法恢復為 Active

- **Closed（正常結案）**：
  - 必須通過 Gate 3
  - 所有文件已凍結
  - 殘餘風險已接受
  - 交付物完整

---

### 測試案例 E2E-009：Closed 正常結案流程

**測試目標**：驗證專案通過 Gate 3 後執行結案流程，狀態變更為 Closed 且文件凍結。

**前置條件**：
- 專案已通過 Gate 3（CurrentGate = Gate3）
- DocumentFreezeStatus = Frozen（文件已在 Gate 3 通過時自動凍結）
- 所有殘餘風險已接受（RiskAcceptanceStatus = Accepted）
- 所有必要文件已上傳且凍結

**測試步驟**：

| 步驟 | 操作 | 導覽路徑 |
|:----|:-----|:--------|
| 1 | 確認 Gate 3 已通過 | 查詢 Dataverse：CurrentGate = Gate3 |
| 2 | 確認文件已凍結 | 查詢 Dataverse：DocumentFreezeStatus = Frozen |
| 3 | 開啟專案結案 Form | Power Apps → Design Governance → 專案結案 |
| 4 | 選擇專案 | 選擇要結案的測試專案 |
| 5 | 選擇結案類型 | ClosureType: `Closed`（正常結案） |
| 6 | 填寫結案摘要 | ClosureSummary: `專案已完成所有交付物，通過所有 Gate` |
| 7 | 確認交付物完整 | 勾選「確認所有交付物已完成」 |
<!-- Phase 3: GOV-009 尚未實作，此測試案例暫時跳過 -->
| 8 | 點擊「提交結案」 | 等待 GOV-009 執行完成 |

**步驟 2：Governance Lead 審批結案**

| 步驟 | 操作 | 執行者 |
|:----|:-----|:------|
| 1 | 登入 Approvals App | `testgovlead@contoso.com` |
| 2 | 開啟「專案結案審批」 | 找到對應的結案請求 |
| 3 | 驗證結案條件 | 確認 Gate 3 已通過、文件已凍結 |
| 4 | 點擊 Approve | Comments：「確認結案條件符合，同意結案」 |
| 5 | 點擊 Submit | 等待 Flow 執行完成 |

**預期結果驗證**：

| 驗證項目 | 預期值 | 驗證方法 | 說明 |
|:--------|:------|:--------|:-----|
| **ProjectStatus** | **Closed (807660002)** | 查詢 Dataverse | 正常結案狀態 |
| CurrentGate | `Gate3` | 查詢 Dataverse | 保持 Gate 3 |
| **DocumentFreezeStatus** | **Frozen (807660001)** | 查詢 Dataverse | 文件已凍結 |
| ClosureDate | `{當前時間}` | 查詢 Dataverse | 記錄結案時間 |
| ClosedBy | `testgovlead@contoso.com` | 查詢 Dataverse | 記錄結案審批者 |
| Gate3PassedDate | `{有值}` | 查詢 Dataverse | 確認已通過 Gate 3 |
| RiskAcceptanceStatus | `Accepted` | 查詢 Dataverse | 殘餘風險已接受 |
| SharePoint 資料夾權限 | 唯讀 | 嘗試上傳文件（應失敗） | 文件凍結生效 |
| Review Decision Log | 新增 `ProjectClosure` | 查詢 Dataverse | 記錄結案決策 |
| 通知 | System Architect + PM 收到結案通知 | 檢查 Email + Teams | |

**Dataverse 驗證查詢**：
```http
GET {{base_url}}/gov_projectregistries?$filter=gov_projectstatus eq 807660002&$select=gov_requestid,gov_projectstatus,gov_currentgate,gov_documentfreezestatus,gov_gate3passeddate,gov_closuredate,gov_closedby

預期回應：
{
    "gov_requestid": "DR-2026-xxxx",
    "gov_projectstatus": 807660002,           // Closed
    "gov_currentgate": 807660004,             // Gate3
    "gov_documentfreezestatus": 807660001,    // Frozen
    "gov_gate3passeddate": "2026-02-07T...",
    "gov_closuredate": "2026-02-08T...",
    "gov_closedby": {...}
}
```

**SharePoint 凍結驗證**：
```
步驟：嘗試在專案資料夾上傳新文件
預期結果：權限被拒絕（Error: Access Denied）
```

**確認此步驟成功**：
- [ ] ProjectStatus = Closed (807660002)
- [ ] CurrentGate = Gate3（必須先通過 Gate 3）
- [ ] DocumentFreezeStatus = Frozen（文件凍結）
- [ ] SharePoint 資料夾為唯讀（無法上傳新文件）
- [ ] 結案日期與審批者已記錄
- [ ] 專案無法再進行任何修改（終態）

**Closed 結案條件驗證**：
1. ✅ 必須通過 Gate 3
2. ✅ 文件狀態必須為 Frozen
3. ✅ 所有殘餘風險必須已接受
4. ✅ 所有必要文件已上傳
5. ✅ Governance Lead 審批通過

**Closed 狀態特性**：
- Closed 為**終態**，無法恢復為 Active
- 若需重啟專案，必須建立新的 Project Registry
- 文件凍結確保稽核記錄的完整性
- 保留期限依組織政策（通常 7 年）

---

## BOM 分層治理測試

### 測試案例 E2E-010：CBOM 建立與狀態流轉

**測試目標**：驗證 Commercial BOM (CBOM) 的建立、版本追蹤與 Gate 0 核准定版流程。

**前置條件**：
- 測試專案已建立（CurrentGate = Pending）
- 使用者 `testuser1@contoso.com` 具備 Pre-Gate Design Support 角色

**測試步驟**：

| 步驟 | 操作 | 導覽路徑 |
|:----|:-----|:--------|
| 1 | 開啟 BOM 建立 Form | Power Apps → Design Governance → BOM Registry |
| 2 | 選擇專案 | 關聯至測試專案 |
| 3 | 選擇 BOM Type | `CBOM` |
| 4 | 填寫 BOM 名稱 | BOMName: `TEST-CBOM-001` |
| 5 | 填寫 BOM 版本 | BOMVersion: `v1.0` |
| 6 | 上傳 BOM 文件 | DocumentLink: SharePoint URL |
| 7 | 點擊「提交」按鈕 | 等待 Flow 執行完成 |

**預期結果驗證（建立時）**：

| 驗證項目 | 預期值 | 驗證方法 |
|:--------|:------|:--------|
| BOM Type | `CBOM` | 查詢 Dataverse |
| BOM Status | `Draft` | 查詢 Dataverse |
| BOM Binding Scope | `CommercialBindingOnly` | 查詢 Dataverse |
| BOM Owner Role | `PreGateDesignSupport` | 查詢 Dataverse |
| Linkage Gate | `Pending` | 查詢 Dataverse |

**步驟 2：CBOM 用於報價**

| 步驟 | 操作 |
|:----|:-----|
| 1 | 模擬 CBOM 用於報價（觸發狀態變更 Flow） |
| 2 | 驗證 BOM Status 變更為 `Quoted` |
| 3 | 驗證 QuotedDate 與 QuotedVersionSnapshot 已記錄 |

**預期結果驗證（報價後）**：

| 驗證項目 | 預期值 |
|:--------|:------|
| BOM Status | `Quoted` |
| QuotedDate | `{報價時間}` |
| QuotedVersionSnapshot | `v1.0` |

**步驟 3：Gate 0 核准後 CBOM 定版**

| 步驟 | 操作 |
|:----|:-----|
| 1 | 完成 Gate 0 核准流程（參考 E2E-001 Phase 2） |
| 2 | 驗證 CBOM Status 自動變更為 `Gate0Approved` |

**預期結果驗證（Gate 0 後）**：

| 驗證項目 | 預期值 |
|:--------|:------|
| BOM Status | `Gate0Approved` |
| Gate0ApprovedDate | `{Gate 0 核准時間}` |
| Linkage Gate | `Gate0` |

**確認此步驟成功**：
- [ ] CBOM 狀態流轉：Draft → Quoted → Gate0Approved
- [ ] 報價版本已記錄（版本快照）
- [ ] Gate 0 核准後 CBOM 定版

---

### 測試案例 E2E-011：EBOM 建立與基線管理

**測試目標**：驗證 Engineering BOM (EBOM) 的建立、與 CBOM 關聯、基線管理與凍結流程。

**前置條件**：
- 測試專案已通過 Gate 0（CurrentGate = Gate0）
- 存在已核准的 CBOM（BOM Status = Gate0Approved）
- 使用者 `testuser1@contoso.com` 具備 System Architect 角色

**測試步驟**：

| 步驟 | 操作 | 導覽路徑 |
|:----|:-----|:--------|
| 1 | 開啟 BOM 建立 Form | Power Apps → Design Governance → BOM Registry |
| 2 | 選擇專案 | 關聯至測試專案 |
| 3 | 選擇 BOM Type | `EBOM` |
| 4 | 選擇來源 CBOM | 關聯至 E2E-010 建立的 CBOM |
| 5 | 填寫 BOM 名稱 | BOMName: `TEST-EBOM-001` |
| 6 | 填寫 BOM 版本 | BOMVersion: `v1.0` |
| 7 | 上傳 BOM 文件 | DocumentLink: SharePoint URL |
| 8 | 標註是否存在差異 | CBOMEBOMVariance: `Yes` |
| 9 | 填寫差異說明 | VarianceDescription: `技術評估後調整規格` |
| 10 | 點擊「提交」按鈕 | 等待 Flow 執行完成 |

**預期結果驗證（建立時）**：

| 驗證項目 | 預期值 | 驗證方法 |
|:--------|:------|:--------|
| BOM Type | `EBOM` | 查詢 Dataverse |
| BOM Status | `Draft` | 查詢 Dataverse |
| BOM Binding Scope | `EngineeringBaseline` | 查詢 Dataverse |
| BOM Owner Role | `SystemArchitect` | 查詢 Dataverse |
| Source CBOM | `{CBOM ID}` | 查詢 Dataverse（Lookup） |
| CBOM EBOM Variance | `Yes` | 查詢 Dataverse |

**步驟 2：Gate 1 核准後 EBOM 納入基線**

| 步驟 | 操作 |
|:----|:-----|
| 1 | 完成 Gate 1 核准流程（參考 E2E-001 Phase 3） |
| 2 | 驗證 EBOM Status 自動變更為 `Baseline` |

**預期結果驗證（Gate 1 後）**：

| 驗證項目 | 預期值 |
|:--------|:------|
| BOM Status | `Baseline` |
| BaselineDate | `{Gate 1 核准時間}` |
| Linkage Gate | `Gate1` |

**步驟 3：Gate 3 前 EBOM 凍結**

| 步驟 | 操作 |
|:----|:-----|
| 1 | 完成 Gate 3 流程（或 DocumentFreeze 流程） |
| 2 | 驗證 EBOM Status 自動變更為 `Frozen` |

**預期結果驗證（凍結後）**：

| 驗證項目 | 預期值 |
|:--------|:------|
| BOM Status | `Frozen` |
| FrozenDate | `{凍結時間}` |

**確認此步驟成功**：
- [ ] EBOM 狀態流轉：Draft → Baseline → Frozen
- [ ] EBOM 與 CBOM 關聯正確（Source CBOM）
- [ ] CBOM-EBOM 差異已記錄

---

### 測試案例 E2E-012：CBOM 商務可用性驗證

**測試目標**：驗證 CBOM 的「商務可用 / 設計不拘束」語義，確認報價後版本保留且 EBOM 可調整。

**前置條件**：
- CBOM 已建立並用於報價（Status = Quoted）
- Gate 0 已核准（CBOM Status = Gate0Approved）

**測試步驟**：

| 步驟 | 操作 | 預期結果 |
|:----|:-----|:--------|
| 1 | 查詢 CBOM 的 QuotedVersionSnapshot | 版本號與報價時一致 |
| 2 | 建立 EBOM 並標註與 CBOM 存在差異 | 允許建立，差異已記錄 |
| 3 | 驗證 CBOM 狀態未變更 | CBOM 仍為 Gate0Approved |
| 4 | 驗證商務可用性 | CBOM 可被報價系統引用 |

**預期結果驗證**：

| 驗證項目 | 預期值 | 說明 |
|:--------|:------|:-----|
| CBOM 版本追溯 | QuotedVersionSnapshot 存在 | 報價版本可追溯 |
| EBOM 調整權限 | System Architect 可調整 | 設計不拘束 |
| 差異記錄 | CBOMEBOMVariance = Yes | 差異已記錄 |
| 差異通知 | VarianceNotifiedDate 存在 | 業務部門已通知 |

**確認此步驟成功**：
- [ ] CBOM「商務可用」：報價系統可引用
- [ ] CBOM「設計不拘束」：EBOM 可與 CBOM 不同
- [ ] 報價版本可追溯
- [ ] 差異處理責任明確

---

### 測試案例 E2E-013：BOM 責任追溯驗證

**測試目標**：驗證 BOM 責任追溯機制，確認 CBOM 與 EBOM 當責歸屬正確。

**前置條件**：
- CBOM 與 EBOM 均已建立
- 專案已通過 Gate 1

**測試步驟**：

| 步驟 | 操作 | 驗證項目 |
|:----|:-----|:--------|
| 1 | 查詢 CBOM 的 BOM Owner Role | `PreGateDesignSupport` |
| 2 | 查詢 EBOM 的 BOM Owner Role | `SystemArchitect` |
| 3 | 查詢 CBOM 的 Created By | Pre-Gate Design Support 使用者 |
| 4 | 查詢 EBOM 的 Created By | System Architect 使用者 |
| 5 | 驗證 Source CBOM 關聯 | EBOM 正確關聯至 CBOM |

**Dataverse 驗證查詢**：
```http
GET {{base_url}}/gov_bomregistries?$filter=gov_parentproject/gov_requestid eq 'DR-2026-xxxx'&$select=gov_bomid,gov_bomtype,gov_bomownerrole,gov_bomstatus,_gov_sourcecbom_value&$expand=gov_createdby($select=fullname)

預期回應：
[
    {
        "gov_bomid": "BOM-CBOM-001",
        "gov_bomtype": 807660000,  // CBOM
        "gov_bomownerrole": 807660000,  // PreGateDesignSupport
        "gov_bomstatus": 807660002,  // Gate0Approved
        "_gov_sourcecbom_value": null,
        "gov_createdby": { "fullname": "Pre-Gate Design Support User" }
    },
    {
        "gov_bomid": "BOM-EBOM-001",
        "gov_bomtype": 807660001,  // EBOM
        "gov_bomownerrole": 807660001,  // SystemArchitect
        "gov_bomstatus": 807660003,  // Baseline
        "_gov_sourcecbom_value": "{CBOM-GUID}",
        "gov_createdby": { "fullname": "System Architect User" }
    }
]
```

**確認此步驟成功**：
- [ ] 商務依據 → CBOM → Pre-Gate Design Support（責任追溯正確）
- [ ] 設計基線 → EBOM → System Architect（責任追溯正確）
- [ ] EBOM 與 CBOM 關聯可追溯

---

### 測試案例 E2E-014：Baseline Seeding 驗證

**測試目標**：驗證 GOV-001 建立專案時，自動產生 13 筆 Planned Document Register 基線記錄。

**前置條件**：
- GOV-001 Flow 已部署
- Counter List 已初始化

**測試步驟**：

| 步驟 | 操作 | 預期結果 |
|:----|:-----|:--------|
| 1 | 透過 FORM-001 建立新專案 | GOV-001 成功執行，回傳 RequestID |
| 2 | 查詢 Document Register（ParentProject = 新專案） | 存在 13 筆記錄 |
| 3 | 驗證每筆記錄的 DocumentRole | 全部為 Planned（807660000） |
| 4 | 驗證每筆記錄的 DeliverablePackage | 全部為 CoreDeliverable（807660000） |
| 5 | 驗證 SharePointFileLink | 全部為空白（尚未上傳） |
| 6 | 驗證 DocumentType 覆蓋範圍 | 覆蓋 Baseline Matrix 中 RequiredForGate ≠ '-' 的所有 13 個 DocumentType |

**Dataverse 驗證查詢**：
```http
GET {{base_url}}/gov_documentregisters?$filter=_gov_parentproject_value eq '{ProjectId}' and gov_documentrole eq 807660000&$select=gov_documentid,gov_documenttype,gov_documentrole,gov_deliverablepackage,gov_sharepointfilelink&$count=true

預期：$count = 13, 全部 gov_documentrole = 807660000, gov_sharepointfilelink = null
```

**確認此步驟成功**：
- [ ] 建立專案後 Document Register 存在 13 筆 Planned 記錄
- [ ] 覆蓋所有 13 個必要 DocumentType
- [ ] 所有記錄 DeliverablePackage = CoreDeliverable
- [ ] 所有記錄 SharePointFileLink 為空白

---

### 測試案例 E2E-015：Draft 版本推進驗證

**測試目標**：驗證 GOV-005 上傳文件時的版本推進機制：Planned→Draft、重複上傳產生 Superseded 鏈。

**前置條件**：
- 專案已建立（含 13 筆 Planned 基線記錄）
- GOV-005 Flow 已部署

**測試步驟**：

| 步驟 | 操作 | 預期結果 |
|:----|:-----|:--------|
| 1 | 上傳 TechnicalFeasibility 文件（v1.0） | Planned 記錄更新為 Draft，SharePointFileLink 填入 URL |
| 2 | 查詢 Document Register（同專案同 DocumentType） | 僅 1 筆記錄，DocumentRole = Draft |
| 3 | 再次上傳 TechnicalFeasibility 文件（v2.0） | 舊 Draft→Superseded，新 Draft 建立 |
| 4 | 查詢 Document Register（同專案同 DocumentType） | 2 筆記錄：1 筆 Superseded + 1 筆 Draft |
| 5 | 驗證 Superseded 記錄的 SupersededBy | 指向新 Draft 記錄 |
| 6 | 驗證 Planned 記錄數量 | 從 13 筆降為 12 筆（TechnicalFeasibility 已被上傳） |

**確認此步驟成功**：
- [ ] 首次上傳：Planned→Draft 正確轉換
- [ ] 重複上傳：舊 Draft→Superseded，新 Draft 建立
- [ ] SupersededBy 回填正確
- [ ] Planned 記錄數量正確遞減

---

### 測試案例 E2E-016：Superseded 不可逆驗證

**測試目標**：驗證 Superseded 記錄不可被覆蓋或復原，Approved/Frozen 記錄不可被上傳覆蓋。

**前置條件**：
- 已有 Superseded 記錄（E2E-015 完成後）

**測試步驟**：

| 步驟 | 操作 | 預期結果 |
|:----|:-----|:--------|
| 1 | 嘗試透過 Dataverse API 修改 Superseded 記錄的 DocumentRole | GOV-017 偵測到違規（Flow-only 欄位被修改） |
| 2 | 嘗試上傳已有 Approved 版本的 DocumentType | 新版本為 Draft，Approved 版本不受影響 |
| 3 | 查詢 Link 欄位 | 仍指向 Approved 版本（非新 Draft） |

**確認此步驟成功**：
- [ ] Superseded 記錄的 DocumentRole 不可被人工修改
- [ ] Approved 版本不因新上傳而被覆蓋
- [ ] Link 欄位優先指向 Approved 版本

---

### 測試案例 E2E-017：Link 目標規則驗證

**測試目標**：驗證 GOV-005 回寫 Project Registry Link 時的目標規則（Approved 優先，Draft 次之）。

**前置條件**：
- 同一 DocumentType 存在多個版本

**測試步驟**：

| 步驟 | 操作 | 預期結果 |
|:----|:-----|:--------|
| 1 | 上傳 DesignBaseline v1.0（Draft） | gov_designbaselinelink = v1.0 的 URL |
| 2 | 模擬 Gate 審批通過，v1.0 設為 Approved | gov_designbaselinelink 仍 = v1.0 的 URL |
| 3 | 上傳 DesignBaseline v2.0（Draft） | gov_designbaselinelink 仍 = v1.0 的 URL（Approved 優先） |
| 4 | 模擬 Gate 審批通過，v2.0 設為 Approved | gov_designbaselinelink = v2.0 的 URL |

**確認此步驟成功**：
- [ ] 僅有 Draft 時，Link 指向最新 Draft
- [ ] 有 Approved 時，Link 指向最新 Approved（忽略 Draft）
- [ ] 新 Approved 覆蓋舊 Approved 的 Link

---

### 測試案例 E2E-018：Deliverable Package 初始化驗證

**測試目標**：驗證 Baseline Seeding 的 DeliverablePackage 預設值，以及 GOV-005 接受不同 DeliverablePackage 的上傳。

**前置條件**：
- 專案已建立（含 Baseline Seeding）

**測試步驟**：

| 步驟 | 操作 | 預期結果 |
|:----|:-----|:--------|
| 1 | 查詢所有 Planned 記錄的 DeliverablePackage | 全部為 CoreDeliverable |
| 2 | 上傳 Other 類型文件，DeliverablePackage = AdHoc | 新建 Draft 記錄，DeliverablePackage = AdHoc |
| 3 | 上傳 DesignBaseline，DeliverablePackage = SupplementaryDeliverable | 新建 Draft 記錄（非更新 Planned，因為 Planned 為 CoreDeliverable） |
| 4 | 查詢 Logical Document Key 唯一性 | ParentProject + DocumentType + DeliverablePackage + DocumentRole 唯一 |

**確認此步驟成功**：
- [ ] Baseline Seeding 全部為 CoreDeliverable
- [ ] AdHoc 上傳正確建立
- [ ] 不同 DeliverablePackage 不衝突

---

## 第三部分：反作弊測試案例

## GOV-017 Guardrail Monitor 測試

### 測試案例 AC-001：偵測人為修改 Flow-only 欄位（CurrentGate）

**測試目標**：驗證 GOV-017 能偵測並自動回滾未授權的 Flow-only 欄位修改。

**前置條件**：
- 專案已建立（CurrentGate = Pending）
- GOV-017 每小時執行一次

**測試步驟**：

| 步驟 | 操作 | 說明 |
|:----|:-----|:----|
| 1 | 使用 Dataverse Web API 直接修改 CurrentGate | 模擬未授權修改 |
| 2 | 等待 GOV-017 下一次執行 | 最多等待 1 小時 |
| 3 | 查看 Governance Violation Log | 驗證違規記錄 |

**步驟 1 詳細操作（Postman）**：

```http
PATCH {{base_url}}/gov_projectregistries(<project-id>)
Authorization: Bearer {{access_token}}
Content-Type: application/json

{
    "gov_currentgate": 807660002
}
```

> **註**：`807660002` 代表 Gate1 的 OptionSet 值

**預期結果驗證**：

| 驗證項目 | 預期值 | 驗證方法 |
|:--------|:------|:--------|
| Governance Violation Log | 新增 1 筆違規記錄 | 查詢 Dataverse |
| ViolatedEntity | `ProjectRegistry` | Governance Violation Log |
| ViolatedField | `CurrentGate` | Governance Violation Log |
| OldValue | `Pending` | Governance Violation Log |
| NewValue | `Gate1` | Governance Violation Log |
| ModifiedBy | 測試使用者 Email | Governance Violation Log |
| RollbackStatus | `Closed` | Governance Violation Log |
| CurrentGate | `Pending`（已自動回滾） | 查詢 Project Registry |
| 通知 | Governance Lead + EM 收到「高優先級」違規通知 | 檢查 Email + Teams |

**驗證自動回滾查詢**：
```http
GET {{base_url}}/gov_projectregistries(<project-id>)?$select=gov_currentgate
```

**預期回應**：
```json
{
    "gov_currentgate": 807660000  // Pending（已回滾）
}
```

**確認此步驟成功**：
- [ ] 違規記錄已建立
- [ ] CurrentGate 已回滾至原值
- [ ] 違規通知已發送

---

### 測試案例 AC-002：偵測人為修改 Review Decision Log

**測試目標**：驗證 GOV-017 能偵測對 Review Decision Log 的未授權修改。

**前置條件**：
- Gate 0 申請已提交（Decision = Pending）

**測試步驟**：

| 步驟 | 操作 |
|:----|:-----|
| 1 | 使用 Dataverse Web API 直接修改 Review Decision Log |
| 2 | 嘗試將 Decision 改為 Approved |
| 3 | 等待 GOV-017 下一次執行 |

**步驟 1 詳細操作（Postman）**：

```http
PATCH {{base_url}}/gov_reviewdecisionlogs(<review-id>)
Authorization: Bearer {{access_token}}
Content-Type: application/json

{
    "gov_decision": 807660001,
    "gov_approvedby": "hacker@contoso.com"
}
```

**預期結果驗證**：

| 驗證項目 | 預期值 |
|:--------|:------|
| Governance Violation Log | 新增 2 筆違規記錄（Decision + ApprovedBy） |
| Decision | `Pending`（已自動回滾） |
| ApprovedBy | `null`（已自動回滾） |
| 通知 | Governance Lead + EM 收到違規通知 |

**確認此步驟成功**：
- [ ] 所有修改皆已回滾
- [ ] 違規記錄完整

---

### 測試案例 AC-003：Field-Level Security 阻擋測試

**測試目標**：驗證 FLS 能在修改時直接拒絕。

**前置條件**：
- 使用一般使用者帳號（非 Flow Service Principal）

**測試步驟**：

| 步驟 | 操作 |
|:----|:-----|
| 1 | 登入 Power Apps（一般使用者） |
| 2 | 開啟 Model-driven App 的進階尋找 |
| 3 | 嘗試編輯 Project Registry 的 CurrentGate 欄位 |

**預期結果**：

| 驗證項目 | 預期值 |
|:--------|:------|
| UI 行為 | 欄位顯示為唯讀或不可見 |
| 若使用 API | 回傳 403 Forbidden |
| 錯誤訊息 | `SecLib::AccessCheckEx failed` |

**確認此步驟成功**：
- [ ] 無法透過 UI 修改 Flow-only 欄位
- [ ] 無法透過 API 修改 Flow-only 欄位

---

## GOV-018 Compliance Reconciler 測試

### 測試案例 AC-004：偵測 CurrentGate 與 Review Decision Log 不一致

**測試目標**：驗證 GOV-018 能偵測 Aggregate 狀態與 Event Log 不一致。

**前置條件**：
- 專案已通過 Gate 0（CurrentGate = Gate0）
- 人為繞過 FLS 修改 CurrentGate = Gate1（但 Review Decision Log 最新記錄為 Gate0）

**測試步驟**：

| 步驟 | 操作 |
|:----|:-----|
| 1 | 人為修改 Project Registry.CurrentGate = Gate1 |
| 2 | 等待 GOV-018 下一次執行（每日 00:00 UTC+8） |
| 3 | 查看 Governance Violation Log |

**預期結果驗證**：

| 驗證項目 | 預期值 |
|:--------|:------|
| Governance Violation Log | 新增 1 筆不一致記錄 |
| ViolationType | `ComplianceInconsistency` |
| ExpectedValue | `Gate0`（根據 Review Decision Log） |
| ActualValue | `Gate1`（Project Registry 當前值） |
| RollbackStatus | `ManualRequired`（需人工處理） |
| 通知 | Governance Lead 收到「合規警報」（High Priority） |

**確認此步驟成功**：
- [ ] 不一致已被偵測
- [ ] 通知已發送
- [ ] 專案被標記為需調查

---

### 測試案例 AC-005：偵測 SharePoint 文件連結失效

**測試目標**：驗證 GOV-018 能偵測文件連結與實際檔案不一致。

**前置條件**：
- 專案已上傳 Gate 0 必要文件
- Document Register 中有 TechnicalFeasibilityLink

**測試步驟**：

| 步驟 | 操作 |
|:----|:-----|
| 1 | 直接在 SharePoint 上刪除 TechnicalFeasibility.pdf |
| 2 | 等待 GOV-018 下一次執行 |
| 3 | 查看 Governance Violation Log |

**預期結果驗證**：

| 驗證項目 | 預期值 |
|:--------|:------|
| Governance Violation Log | 新增 1 筆不一致記錄 |
| ViolatedField | `TechnicalFeasibilityLink` |
| ExpectedValue | 「檔案存在（HTTP 200）」 |
| ActualValue | 「檔案不存在（HTTP 404）」 |
| 通知 | Governance Lead 收到「合規警報」 |

---

## GOV-019 SLA Monitor 測試

### 測試案例 AC-006：偵測 Gate 0 審批超時

**測試目標**：驗證 GOV-019 能偵測並通知審批超過 SLA。

**前置條件**：
- Gate 0 申請已提交（RequestStatus = Pending）
- 需調整測試資料使 SubmittedDate 為 3 個工作日前

**測試步驟**：

| 步驟 | 操作 |
|:----|:-----|
| 1 | 修改 Review Decision Log.SubmittedDate 為 3 個工作日前 |
| 2 | 等待 GOV-019 下一次執行（每小時） |
| 3 | 查看通知 |

**預期結果驗證**：

| 驗證項目 | 預期值 |
|:--------|:------|
| SLA 計算 | WaitingDays = 3 工作日 > SLA 2 工作日 |
| 通知 | Governance Lead + EM 收到「SLA 警報」 |
| 通知內容 | 「Gate0 審批已超過 SLA（2 工作日），當前已等待 3 工作日」 |
| 通知優先級 | High Priority |

**確認此步驟成功**：
- [ ] SLA 違規已偵測
- [ ] 通知已發送給正確的收件者
- [ ] 通知內容正確顯示超時天數

---

## 直接 SharePoint 上傳測試

### 測試案例 AC-007：偵測直接 SharePoint 上傳（孤兒檔案）

**測試目標**：驗證直接上傳到 SharePoint 的檔案會被偵測並隔離。

**前置條件**：
- 專案資料夾已建立
- 使用者有 SharePoint 寫入權限（測試用）

**測試步驟**：

| 步驟 | 操作 |
|:----|:-----|
| 1 | 開啟 SharePoint 專案資料夾 |
| 2 | 直接拖曳上傳 `Unauthorized.pdf` |
| 3 | 等待 GOV-017 下一次執行 |

**預期結果驗證**：

| 驗證項目 | 預期值 |
|:--------|:------|
| 上傳行為 | 應被 SharePoint 權限拒絕（如果 FLS 正確設定） |
| 若繞過權限 | GOV-017 偵測到孤兒檔案 |
| 檔案處置 | 移動到隔離區 `/Quarantine/UnregisteredFiles/` |
| 通知 | 上傳者收到「未授權檔案上傳」警告 |
| 違規記錄 | Governance Violation Log 新增 1 筆 |

**確認此步驟成功**：
- [ ] 正確的權限設定下，直接上傳被拒絕
- [ ] 若有孤兒檔案，已被移到隔離區

---

## 審批順序跳過測試

### 測試案例 AC-008：嘗試跳過審批層級

**測試目標**：驗證系統強制審批順序，無法跳過層級。

**前置條件**：
- Gate 1 申請已提交
- Security Review 尚未完成

**測試步驟**：

| 步驟 | 操作 |
|:----|:-----|
| 1 | Governance Lead 嘗試直接 Approve Gate 1 |
| 2 | （在 Security Review 完成前） |

**預期結果驗證**：

| 驗證項目 | 預期值 |
|:--------|:------|
| Governance Lead 視角 | 尚未收到 Approval 請求（因為尚未輪到） |
| 技術層面 | APR-003（Layer 3）尚未建立 |
| 若嘗試手動觸發 | 系統拒絕，回傳審查順序錯誤 |

**確認此步驟成功**：
- [ ] 審批請求只在前序層級完成後才發送
- [ ] 無法繞過審批順序

---

## System Architect 欄位測試案例（v1.1 新增）

### 測試案例 SA-001：SA 欄位正確使用 User 記錄

**測試目標**：驗證專案建立時 System Architect 欄位正確使用 User 記錄（varCurrentUser），而非 email 字串（varCurrentUserEmail）。

**前置條件**：
- 測試使用者已登入 Power Apps
- App.OnStart 已正確設定 varCurrentUser、varCurrentUserEmail、varCurrentUserName

**測試步驟**：

| 步驟 | 操作 | 預期結果 |
|:----|:-----|:--------|
| 1 | 開啟專案建立 Form | Form 正常載入 |
| 2 | 檢視 System Architect 欄位顯示值 | 顯示 varCurrentUserName（名稱），非 email |
| 3 | 填寫專案資料並提交 | 成功建立專案 |
| 4 | 查詢 Dataverse gov_systemarchitect 欄位 | 值為 User Lookup（包含 User GUID） |

**Dataverse 驗證查詢**：
```http
GET {{base_url}}/gov_projectregistries?$filter=gov_title eq 'TEST-SA-001'&$select=gov_requestid,_gov_systemarchitect_value&$expand=gov_systemarchitect($select=fullname,internalemailaddress)
```

**預期回應格式**：
```json
{
    "_gov_systemarchitect_value": "<user-guid>",
    "gov_systemarchitect": {
        "fullname": "Test User 1",
        "internalemailaddress": "testuser1@contoso.com"
    }
}
```

**確認此步驟成功**：
- [ ] System Architect 欄位顯示名稱（非 email）
- [ ] Dataverse 記錄包含 User Lookup（有 GUID）
- [ ] 可展開 gov_systemarchitect 取得 User 完整資訊

---

### 測試案例 SA-002：SA 欄位顯示視覺規格驗證

**測試目標**：驗證 System Architect 欄位使用正確的視覺規格（非 Flow-Only 樣式）。

**測試步驟**：

| 步驟 | 操作 | 驗證項目 |
|:----|:-----|:--------|
| 1 | 開啟專案建立 Form | - |
| 2 | 檢視 lblS2_ArchitectLabel | 文字為 "System Architect"（無 "(System-controlled)"） |
| 3 | 檢視 lblS2_ArchitectValue 背景色 | 使用 varNeutralLighter（非 varFlowOnlyBg） |
| 4 | 檢視 lblS2_ArchitectValue 文字色 | 使用 varTextBase（非 varTextSecondary） |

**預期視覺規格**：

| 屬性 | 錯誤值（v1.0） | 正確值（v1.1） |
|:-----|:-------------|:-------------|
| 標籤 | "System Architect (System-controlled)" | "System Architect" |
| Fill | varFlowOnlyBg (#EFEFEF) | varNeutralLighter (#F5F5F5) |
| Color | varTextSecondary (#666666) | varTextBase (#2D2D2D) |

**確認此步驟成功**：
- [ ] 標籤無 "(System-controlled)" 後綴
- [ ] 背景色非 varFlowOnlyBg
- [ ] 文字色非 varTextSecondary

---

### 測試案例 SA-003：專案篩選器正確比對 User Lookup

**測試目標**：驗證專案選擇器（Filter）正確比對 gov_systemarchitect Lookup 欄位。

**前置條件**：
- 已存在至少 2 個專案，由不同 System Architect 建立
- testuser1 為 Project A 的 SA
- testuser2 為 Project B 的 SA

**測試步驟**：

| 步驟 | 操作 | 預期結果 |
|:----|:-----|:--------|
| 1 | 以 testuser1 登入，開啟 Gate 申請 Form | Form 載入 |
| 2 | 展開專案選擇器 | 僅顯示 testuser1 為 SA 的專案 |
| 3 | 驗證 Project B 不在清單中 | Project B（testuser2 的專案）不出現 |

**正確的 Filter 公式**：
```
Filter(
    gov_projectregistry,
    gov_projectstatus = "Active" And
    gov_systemarchitect.'Primary Email' = varCurrentUserEmail And
    gov_requeststatus = "None"
)
```

**確認此步驟成功**：
- [ ] 專案選擇器僅顯示當前使用者為 SA 的專案
- [ ] 其他 SA 的專案不會出現在清單中

---

### 測試案例 SA-004：SA Handover 流程驗證

**測試目標**：驗證 System Architect 移交流程正確執行，Event Log 正確記錄。

**前置條件**：
- 專案已建立，SA 為 testuser1
- testuser1 或 Governance Lead 發起移交

**測試步驟**：

| 步驟 | 操作 | 預期結果 |
|:----|:-----|:--------|
| 1 | 開啟 SA Handover Form | Form 載入 |
| 2 | 選擇專案 | 顯示當前 SA 資訊 |
| 3 | 選擇新 SA（testuser3） | ComboBox 顯示 testuser3 |
| 4 | 選擇移交原因 | RoleChange |
| 5 | 提交移交請求 | 成功，進入 PendingAcceptance 狀態 |
| 6 | testuser3 登入確認接受 | 移交完成 |
| 7 | 查詢 Project Registry | gov_systemarchitect 已更新為 testuser3 |
| 8 | 查詢 SA Handover Event Log | 記錄完整移交歷程 |

**Event Log 驗證查詢**：
```http
GET {{base_url}}/gov_sahandoverevents?$filter=_gov_parentproject_value eq '<project-id>'&$orderby=createdon desc
```

**預期 Event Log 內容**：

| 欄位 | 預期值 |
|:-----|:------|
| OriginalSA | testuser1 |
| NewSA | testuser3 |
| HandoverReason | RoleChange |
| RequestedBy | testuser1 |
| Status | Completed |
| AcceptedDate | {有值} |

**確認此步驟成功**：
- [ ] 移交請求成功建立
- [ ] 新 SA 收到通知
- [ ] 確認後 gov_systemarchitect 更新
- [ ] Event Log 完整記錄移交歷程
- [ ] 原始 SA 記錄保留（Append-Only）

---

### 測試案例 SA-005：Presales 專案 SA 記錄保護

**測試目標**：驗證 Presales 類型專案的 SA 歷史記錄完整保護。

**前置條件**：
- 專案類型為 Presales
- 已執行多次 SA Handover

**測試步驟**：

| 步驟 | 操作 | 預期結果 |
|:----|:-----|:--------|
| 1 | 建立 Presales 專案（SA = testuser1） | 成功 |
| 2 | 執行 SA Handover（→ testuser2） | Event Log 記錄 |
| 3 | 執行 SA Handover（→ testuser3） | Event Log 記錄 |
| 4 | 查詢所有 SA Handover Events | 完整歷程（3 筆） |
| 5 | 驗證無法刪除 Event Log 記錄 | 刪除失敗或被拒絕 |

**Event Log 歷程查詢**：
```http
GET {{base_url}}/gov_sahandoverevents?$filter=_gov_parentproject_value eq '<project-id>'&$orderby=createdon asc
```

**預期歷程**：

| 順序 | OriginalSA | NewSA | Status |
|:----|:-----------|:------|:-------|
| 1 | (Initial) | testuser1 | Initial |
| 2 | testuser1 | testuser2 | Completed |
| 3 | testuser2 | testuser3 | Completed |

**確認此步驟成功**：
- [ ] 所有 SA 變更歷程完整保留
- [ ] Event Log 為 Append-Only（無法刪除）
- [ ] Presales 轉正式專案時歷程保留

---

## 第四部分：部署檢查程序

## Pre-Deployment Checklist

### 環境準備檢查

| 檢查項目 | 負責人 | QA | UAT | PROD | 狀態 |
|:--------|:------|:---:|:---:|:---:|:---:|
| Dataverse 環境已建立 | IT Admin | ☐ | ☐ | ☐ | |
| SharePoint 文件庫已建立 | SharePoint Admin | ☐ | ☐ | ☐ | |
| Teams Channel 已建立 | Teams Admin | ☐ | ☐ | ☐ | |
| Security Groups 已建立（7 個） | Entra ID Admin | ☐ | ☐ | ☐ | |
| Service Principal 已建立並授權 | IT Admin | ☐ | ☐ | ☐ | |
| Field-Level Security Profile 已配置 | Dataverse Admin | ☐ | ☐ | ☐ | |
| Dataverse Audit 已啟用 | Dataverse Admin | ☐ | ☐ | ☐ | |
| Application Insights 已設定 | DevOps | ☐ | ☐ | ☐ | |

### Security Groups 建立檢查

| Group 名稱 | 類型 | 成員已加入 | 狀態 |
|-----------|------|:---:|:---:|
| GOV-EngineeringManagement | Mail-enabled Security Group | ☐ | |
| GOV-SecurityReviewers | Mail-enabled Security Group | ☐ | |
| GOV-QAReviewers | Mail-enabled Security Group | ☐ | |
| GOV-GovernanceLead | Mail-enabled Security Group | ☐ | |
| GOV-ExecutiveManagement | Mail-enabled Security Group | ☐ | |
| GOV-FlowServicePrincipal | Service Principal | ☐ | |
| GOV-Architects | Security Group | ☐ | |

### Dataverse 資料表檢查

| 資料表 | Schema 正確 | FLS 配置 | 稽核啟用 | 狀態 |
|-------|:---:|:---:|:---:|:---:|
| Project Registry | ☐ | ☐ | ☐ | |
| Review Decision Log | ☐ | ☐ | ☐ | |
| Document Register | ☐ | ☐ | ☐ | |
| Risk Assessment Table | ☐ | ☐ | ☐ | |
| Governance Violation Log | ☐ | ☐ | ☐ | |
| Approval Records | ☐ | ☐ | ☐ | |

---

## Solution 部署程序

### 從 DEV 匯出 Solution

**導覽路徑**：
1. Power Apps Maker Portal（DEV 環境）：`https://make.powerapps.com`
2. 左側導覽 → 「解決方案」
3. 選擇「Governance Flows Solution」
4. 點擊「匯出」

**匯出設定**：
| 設定項目 | 值 |
|:--------|:--|
| 匯出類型 | 受控（Managed） |
| 發行者 | （選擇您的發行者） |
| 版本 | （遞增版本號，如 1.0.0.1） |

**確認此步驟成功**：
- [ ] Solution Zip 檔案已下載
- [ ] 檔案大小合理（非空白）

---

### 匯入 Solution 至目標環境

**導覽路徑**：
1. Power Apps Maker Portal（目標環境）
2. 左側導覽 → 「解決方案」
3. 點擊「匯入」
4. 上傳 Solution Zip 檔案

**匯入步驟**：
| 步驟 | 操作 |
|:----|:-----|
| 1 | 選擇 Solution Zip 檔案 |
| 2 | 點擊「下一步」 |
| 3 | 確認 Connection References |
| 4 | 為每個 Connection Reference 選擇或建立連線 |
| 5 | 點擊「匯入」 |
| 6 | 等待匯入完成（可能需要數分鐘） |

**確認此步驟成功**：
- [ ] 匯入狀態顯示「成功」
- [ ] 無錯誤訊息
- [ ] Solution 出現在解決方案清單中

---

### 設定 Connection References

**導覽路徑**：
1. 開啟「Governance Flows Solution」
2. 點擊「Connection References」

**必要的 Connections**：

| Connection Reference | 連線類型 | 設定方式 |
|:--------------------|:--------|:--------|
| Dataverse Connection | Microsoft Dataverse | 使用 Service Principal 帳號 |
| SharePoint Connection | SharePoint | 使用 Service Principal 帳號 |
| Office 365 Outlook | Office 365 Outlook | 使用通知發送帳號 |
| Microsoft Teams | Microsoft Teams | 使用 Teams Bot 帳號 |
| Approvals | Approvals | 預設連線 |

**步驟**：
| 步驟 | 操作 |
|:----|:-----|
| 1 | 選擇 Connection Reference |
| 2 | 點擊「設定連線」 |
| 3 | 選擇現有連線或建立新連線 |
| 4 | 點擊「儲存」 |
| 5 | 重複上述步驟，直到所有 Connection References 皆已設定 |

**確認此步驟成功**：
- [ ] 所有 Connection References 皆已設定
- [ ] 連線狀態皆為「已連線」

---

### 啟用 Flows

**導覽路徑**：
1. 開啟「Governance Flows Solution」
2. 點擊「Cloud flows」

**啟用順序**（依照相依性）：

| 順序 | Flow 名稱 | 類型 |
|:----|:---------|:-----|
| 1 | GOV-015：Notification Handler | Child Flow |
| 2 | GOV-016：Rework Loop Handler | Child Flow |
| 3 | GOV-013：Risk Level Calculator | Child Flow |
| 4 | GOV-014：Document Freeze | Child Flow |
| 5 | GOV-005：Document Intake and Register | Parent Flow |
| 6 | GOV-004：Risk Acceptance | Parent Flow |
| 7 | GOV-003：Gate Approval Orchestrator | Parent Flow |
| 8 | GOV-002：Gate Transition Request | Parent Flow |
| 9 | GOV-001：Create Project | Parent Flow |
| 10 | GOV-017：Guardrail Monitor | Scheduled Flow |
| 11 | GOV-018：Compliance Reconciler | Scheduled Flow |
| 12 | GOV-019：SLA Monitor | Scheduled Flow |

**啟用步驟**：
| 步驟 | 操作 |
|:----|:-----|
| 1 | 選擇 Flow |
| 2 | 點擊「開啟」（Turn on） |
| 3 | 驗證 Flow 狀態為「開啟」 |
| 4 | 重複上述步驟，按順序啟用所有 Flows |

**確認此步驟成功**：
- [ ] 所有 Flows 皆已啟用
- [ ] 無啟用錯誤

---

## Smoke Tests（冒煙測試）

### GOV-001 Create Project 測試

**測試目的**：驗證專案建立流程正常運作。

**測試步驟**：
| 步驟 | 操作 | 預期結果 |
|:----|:-----|:--------|
| 1 | 開啟 Power Apps「專案建立 Form」 | Form 正常載入 |
| 2 | 填寫測試資料：Title = `SMOKE-TEST-001` | 欄位可正常輸入 |
| 3 | 點擊「提交」 | 顯示成功訊息 |
| 4 | 查詢 Dataverse | 記錄已建立 |
| 5 | 查看 SharePoint | 資料夾已建立 |

**確認此步驟成功**：
- [ ] 專案已建立
- [ ] SharePoint 資料夾已建立
- [ ] 通知已發送

---

### GOV-017 Guardrail Monitor 測試

**測試目的**：驗證監控 Flow 正常執行。

**測試步驟**：
| 步驟 | 操作 | 預期結果 |
|:----|:-----|:--------|
| 1 | Power Automate Portal → GOV-017 | Flow 頁面正常載入 |
| 2 | 點擊「測試」→「手動」 | 測試開始執行 |
| 3 | 等待執行完成 | 狀態顯示「成功」 |
| 4 | 檢視執行歷史 | 無錯誤訊息 |

**確認此步驟成功**：
- [ ] GOV-017 可手動觸發
- [ ] 執行無錯誤

---

### GOV-015 Notification Handler 測試

**測試目的**：驗證通知發送功能正常。

**測試步驟**：
| 步驟 | 操作 | 預期結果 |
|:----|:-----|:--------|
| 1 | 透過 GOV-001 觸發通知 | 專案建立觸發通知 |
| 2 | 檢查 Email 收件匣 | 收到「專案已建立」Email |
| 3 | 檢查 Teams | 收到 Teams 訊息 |

**確認此步驟成功**：
- [ ] Email 通知已發送
- [ ] Teams 通知已發送

---

## Post-Deployment Checklist

### 功能驗證檢查

| 驗證項目 | QA | UAT | PROD | 狀態 |
|---------|:---:|:---:|:---:|:---:|
| 專案建立成功（GOV-001） | ☐ | ☐ | ☐ | |
| 文件上傳成功（GOV-005） | ☐ | ☐ | ☐ | |
| Gate 申請成功（GOV-002） | ☐ | ☐ | ☐ | |
| 審批流程運作（GOV-003） | ☐ | ☐ | ☐ | |
| 通知發送正常（GOV-015） | ☐ | ☐ | ☐ | |
| 監控 Flow 執行正常 | ☐ | ☐ | ☐ | |

### 安全性驗證檢查

| 驗證項目 | QA | UAT | PROD | 狀態 |
|---------|:---:|:---:|:---:|:---:|
| FLS 阻擋 Flow-only 欄位修改 | ☐ | ☐ | ☐ | |
| SharePoint 權限正確設定 | ☐ | ☐ | ☐ | |
| Review Decision Log 為 Append-only | ☐ | ☐ | ☐ | |
| GOV-017 正確偵測違規 | ☐ | ☐ | ☐ | |
| GOV-018 正確偵測不一致 | ☐ | ☐ | ☐ | |

### 效能驗證檢查

| 驗證項目 | 基準值 | 實測值 | 狀態 |
|:--------|:------|-------|:---:|
| GOV-001 執行時間 | < 10 秒 | | ☐ |
| GOV-002 執行時間 | < 6 秒 | | ☐ |
| GOV-017 執行時間 | < 60 秒 | | ☐ |
| GOV-018 執行時間 | < 10 分鐘 | | ☐ |

---

## 監控與警報設定

### Application Insights 設定

**導覽路徑**：
1. Azure Portal：`https://portal.azure.com`
2. 搜尋「Application Insights」
3. 選擇或建立 Resource

**設定步驟**：
| 步驟 | 操作 |
|:----|:-----|
| 1 | 建立 Application Insights Resource |
| 2 | 複製 Instrumentation Key |
| 3 | Power Platform Admin Center → 環境設定 |
| 4 | 啟用「Flow 分析」 |
| 5 | 貼上 Application Insights Connection String |

### 警報規則設定

**必要的警報規則**：

| 警報名稱 | 條件 | 嚴重性 | 通知對象 |
|:--------|:-----|:------|:--------|
| Flow 失敗率警報 | 失敗率 > 5%（過去 15 分鐘） | 高 | DevOps Team |
| GOV-017 違規偵測 | 違規計數 > 0（過去 1 小時） | 高 | Governance Lead |
| GOV-019 SLA 違規 | 違規計數 > 3（過去 1 小時） | 中 | Engineering Management |
| Flow 執行時間過長 | 執行時間 > 5 分鐘 | 低 | DevOps Team |

**設定步驟**：
| 步驟 | 操作 |
|:----|:-----|
| 1 | Application Insights → 「警示」 |
| 2 | 點擊「新增警示規則」 |
| 3 | 設定條件（依上表） |
| 4 | 設定動作群組（Email + SMS） |
| 5 | 儲存警示規則 |

**確認此步驟成功**：
- [ ] 所有警報規則已建立
- [ ] 測試警報可正常發送

---

## 第五部分：上線驗收標準

## 功能完整性驗收

### 核心功能驗收

| 驗收項目 | 驗收標準 | 驗收方法 | 狀態 |
|---------|---------|---------|:---:|
| **專案建立** | 可成功建立專案，產生 RequestID | 執行 E2E-001 Phase 1 | ☐ |
| **文件上傳** | 可上傳文件至正確的 SharePoint 資料夾 | 執行 E2E-001 步驟 2.1 | ☐ |
| **Gate 0 審批** | 單層審批流程正確運作 | 執行 E2E-001 Phase 2 | ☐ |
| **Gate 1 審批** | 三層序列審批流程正確運作 | 執行 E2E-001 Phase 3 | ☐ |
| **Gate 2 審批** | 單層審批流程正確運作 | 執行 E2E-001 Phase 4 | ☐ |
| **Risk Acceptance** | 風險計算與接受流程正確運作 | 執行 E2E-001 Phase 5 | ☐ |
| **Gate 3 審批** | 雙層審批 + Document Freeze 正確運作 | 執行 E2E-001 Phase 6 | ☐ |
| **拒絕與重工** | Rework 流程正確運作 | 執行 E2E-002, E2E-003 | ☐ |
| **OnHold 機制** | ReworkCount >= 3 自動暫停 | 執行 E2E-004 | ☐ |

### 通知驗收

| 通知類型 | Email | Teams | 驗收方法 | 狀態 |
|---------|:---:|:---:|---------|:---:|
| 專案建立通知 | ☐ | ☐ | E2E-001 Phase 1 | |
| Gate 通過通知 | ☐ | ☐ | E2E-001 每個 Phase | |
| Gate 拒絕通知 | ☐ | ☐ | E2E-002, E2E-003 | |
| OnHold 通知 | ☐ | ☐ | E2E-004 | |
| 違規警報 | ☐ | ☐ | AC-001, AC-002 | |
| SLA 警報 | ☐ | ☐ | AC-006 | |

---

## 治理完整性驗收

### Event Sourcing 驗收

| 驗收項目 | 驗收標準 | 驗收方法 | 狀態 |
|---------|---------|---------|:---:|
| **事件記錄完整** | 所有治理決策皆有 Review Decision Log 記錄 | 查詢 Dataverse | ☐ |
| **狀態可重建** | 從 Event Log 可重建 Project Registry 狀態 | GOV-018 驗證 | ☐ |
| **Event Log 不可變** | Review Decision Log 為 Append-only | 嘗試修改應失敗 | ☐ |
| **審計軌跡完整** | 所有操作有 Actor + Timestamp | 查詢 Event Log | ☐ |

### BOM 分層治理驗收

| 驗收項目 | 驗收標準 | 驗收方法 | 狀態 |
|---------|---------|---------|:---:|
| **CBOM 建立** | Pre-Gate Design Support 可建立 CBOM | E2E-010 | ☐ |
| **CBOM 狀態流轉** | Draft → Quoted → Gate0Approved | E2E-010 | ☐ |
| **CBOM 報價版本追溯** | 報價後版本快照正確記錄 | E2E-012 | ☐ |
| **EBOM 建立** | System Architect 可建立 EBOM | E2E-011 | ☐ |
| **EBOM 狀態流轉** | Draft → Baseline → Frozen | E2E-011 | ☐ |
| **CBOM-EBOM 關聯** | EBOM 正確關聯至 Source CBOM | E2E-011 | ☐ |
| **差異記錄** | CBOM-EBOM 差異正確記錄與通知 | E2E-012 | ☐ |
| **責任追溯** | 商務 → CBOM → Presales；設計 → EBOM → SA | E2E-013 | ☐ |

### 反作弊驗收

| 驗收項目 | 驗收標準 | 驗收方法 | 狀態 |
|---------|---------|---------|:---:|
| **FLS 阻擋有效** | Flow-only 欄位無法被人為修改 | AC-003 | ☐ |
| **GOV-017 偵測有效** | 1 小時內偵測並回滾未授權修改 | AC-001, AC-002 | ☐ |
| **GOV-018 偵測有效** | 每日偵測 Aggregate vs Event 不一致 | AC-004, AC-005 | ☐ |
| **GOV-019 偵測有效** | SLA 超時正確通知 | AC-006 | ☐ |
| **審批順序強制** | 無法跳過審批層級 | AC-008 | ☐ |
| **孤兒檔案偵測** | 未透過 Form 上傳的檔案被偵測 | AC-007 | ☐ |
| **BOM 狀態保護** | BOM Status 僅 Flow 可修改 | 嘗試直接修改應失敗 | ☐ |

### 權限驗收

| 驗收項目 | 驗收標準 | 驗收方法 | 狀態 |
|---------|---------|---------|:---:|
| **Flow Service Principal** | 可寫入 Flow-only 欄位 | Smoke Test | ☐ |
| **System Architect** | 只能讀取 Flow-only 欄位 | 嘗試修改應失敗 | ☐ |
| **Reviewer** | 只能透過 Approvals 審批 | 嘗試直接修改應失敗 | ☐ |
| **SharePoint 權限** | Gate 資料夾只有 Flow 可寫入 | 嘗試直接上傳應失敗 | ☐ |

---

## 效能與穩定性驗收

### 效能基準

| Flow | 平均執行時間 | 95th Percentile | 驗收標準 | 狀態 |
|------|-----------|----------------|---------|:---:|
| GOV-001 | | | < 10 秒 | ☐ |
| GOV-002 | | | < 6 秒 | ☐ |
| GOV-003 | | | 視審批時間 | ☐ |
| GOV-017 | | | < 60 秒 | ☐ |
| GOV-018 | | | < 10 分鐘 | ☐ |
| GOV-019 | | | < 5 分鐘 | ☐ |

### 穩定性驗收

| 驗收項目 | 驗收標準 | 驗收方法 | 狀態 |
|---------|---------|---------|:---:|
| **Flow 成功率** | > 99% | Application Insights | ☐ |
| **連續執行穩定** | 連續 7 天無錯誤 | Flow Run History | ☐ |
| **並發處理** | 同時 10 筆請求無錯誤 | 負載測試 | ☐ |
| **錯誤回復** | 暫時性錯誤自動重試成功 | 模擬錯誤測試 | ☐ |

---

## 文件與培訓驗收

### 文件完整性

| 文件 | 已完成 | 已審核 | 狀態 |
|-----|:---:|:---:|:---:|
| 01-Prerequisites-and-Environment.md | ☐ | ☐ | |
| 02-Dataverse-Data-Model-and-Security.md | ☐ | ☐ | |
| 03-SharePoint-Architecture.md | ☐ | ☐ | |
| 04-PowerApps-Forms.md | ☐ | ☐ | |
| 05-PowerAutomate-Core-Flows.md | ☐ | ☐ | |
| 06-Guardrails-and-AntiCheating.md | ☐ | ☐ | |
| 07-Testing-and-Acceptance.md | ☐ | ☐ | |
| 使用者操作手冊 | ☐ | ☐ | |
| 管理員操作手冊 | ☐ | ☐ | |

### 培訓完成

| 培訓對象 | 培訓內容 | 已完成 | 狀態 |
|---------|---------|:---:|:---:|
| System Architect | 專案建立、文件上傳、Gate 申請 | ☐ | |
| Project Manager | 專案監控、狀態查詢 | ☐ | |
| Security Reviewer | Security Review 操作 | ☐ | |
| QA Reviewer | QA Review 操作 | ☐ | |
| Governance Lead | 全流程操作、違規處理 | ☐ | |
| Engineering Management | 審批操作、OnHold 處理 | ☐ | |
| IT Admin | 系統維護、問題排查 | ☐ | |

---

## 上線核准

### 上線前最終檢查

| 檢查項目 | 負責人 | 簽核 | 日期 |
|:--------|:------|:---:|-----|
| 所有功能測試通過 | QA Lead | ☐ | |
| 所有反作弊測試通過 | Security Lead | ☐ | |
| 效能符合基準 | DevOps Lead | ☐ | |
| 文件已完成並審核 | Documentation Lead | ☐ | |
| 培訓已完成 | Training Lead | ☐ | |
| 回滾程序已準備 | DevOps Lead | ☐ | |

### 上線核准簽核

| 簽核者 | 角色 | 簽核 | 日期 |
|-------|-----|:---:|-----|
| | Project Manager | ☐ | |
| | Governance Lead | ☐ | |
| | IT Director | ☐ | |
| | Security Officer | ☐ | |

---

## 第六部分：完成定義（Done Definition）

## 測試階段完成定義

### 單元測試完成定義

- [ ] 所有 19 個 Flows 皆有對應的測試案例
- [ ] 所有 Happy Path 測試通過
- [ ] 所有 Rejection Path 測試通過
- [ ] 所有驗證失敗案例測試通過
- [ ] 測試覆蓋率 >= 80%

### 整合測試完成定義

- [ ] E2E-001（完整 Gate 流程）測試通過
- [ ] E2E-002（Gate 0 拒絕與重工）測試通過
- [ ] E2E-003（Gate 1 第二層拒絕）測試通過
- [ ] E2E-004（OnHold 機制）測試通過
- [ ] E2E-005（冪等性測試）測試通過
- [ ] E2E-006（並發測試）測試通過
- [ ] E2E-010（CBOM 建立與狀態流轉）測試通過
- [ ] E2E-011（EBOM 建立與基線管理）測試通過
- [ ] E2E-012（CBOM 商務可用性驗證）測試通過
- [ ] E2E-013（BOM 責任追溯驗證）測試通過
- [ ] E2E-014（Baseline Seeding 驗證）測試通過
- [ ] E2E-015（Draft 版本推進驗證）測試通過
- [ ] E2E-016（Superseded 不可逆驗證）測試通過
- [ ] E2E-017（Link 目標規則驗證）測試通過
- [ ] E2E-018（Deliverable Package 初始化驗證）測試通過

### 反作弊測試完成定義

- [ ] AC-001（偵測 CurrentGate 修改）測試通過
- [ ] AC-002（偵測 Review Decision Log 修改）測試通過
- [ ] AC-003（FLS 阻擋測試）測試通過
- [ ] AC-004（Compliance 不一致偵測）測試通過
- [ ] AC-005（SharePoint 文件連結失效偵測）測試通過
- [ ] AC-006（SLA 超時偵測）測試通過
- [ ] AC-007（孤兒檔案偵測）測試通過
- [ ] AC-008（審批順序強制）測試通過

---

## 部署階段完成定義

### QA 環境部署完成定義

- [ ] Solution 成功匯入
- [ ] 所有 Connection References 已設定
- [ ] 所有 Flows 已啟用
- [ ] Smoke Tests 全部通過
- [ ] 整合測試全部通過

### UAT 環境部署完成定義

- [ ] Solution 成功匯入
- [ ] 所有 Connection References 已設定
- [ ] 所有 Flows 已啟用
- [ ] 業務代表 UAT 測試通過
- [ ] 業務代表簽核確認

### PROD 環境部署完成定義

- [ ] Pre-Deployment Checklist 全部勾選
- [ ] Solution 成功匯入
- [ ] 所有 Connection References 已設定
- [ ] 所有 Flows 已啟用
- [ ] Smoke Tests 全部通過
- [ ] 監控與警報已設定
- [ ] 回滾程序已準備並測試

---

## 上線驗收完成定義

### 功能驗收完成定義

- [ ] 所有核心功能驗收項目通過
- [ ] 所有通知類型正常發送
- [ ] 所有角色可正常執行其職責

### 治理驗收完成定義

- [ ] Event Sourcing 驗收項目全部通過
- [ ] 反作弊驗收項目全部通過
- [ ] 權限驗收項目全部通過
- [ ] 審計軌跡完整可追溯

### 效能與穩定性驗收完成定義

- [ ] 所有 Flow 執行時間符合基準
- [ ] Flow 成功率 > 99%
- [ ] 連續 7 天無錯誤

### 文件與培訓驗收完成定義

- [ ] 所有實作文件已完成並審核
- [ ] 所有角色培訓已完成
- [ ] 使用者手冊已發布

### 上線核准完成定義

- [ ] 所有簽核者已簽核
- [ ] 上線日期已確認
- [ ] 回滾計畫已準備
- [ ] 支援團隊待命

---

## TODO 清單（資訊不足項目）

以下項目在 SOP 文件中未提供完整資訊，需在實作時補充：

| TODO 項目 | 缺失資訊 | 影響步驟 |
|:---------|:--------|:--------|
| **Application Insights Instrumentation Key** | 需建立 Azure 資源後取得 | 4.5 監控設定 |
| **測試環境 URL** | 需建立環境後取得 | 所有測試步驟 |
| **測試使用者密碼** | 需建立使用者後設定 | 1.2.3 測試使用者 |
| **SharePoint Site URL** | 需建立 Site 後取得 | SharePoint 相關測試 |
| **Teams Channel ID** | 需建立 Channel 後取得 | 通知測試 |
| **Security Group Object ID** | 需建立 Group 後取得 | 權限測試 |
| **Service Principal GUID** | 需建立 Service Principal 後取得 | FLS 測試 |
| **負載測試工具** | SOP 未指定使用何種工具 | 5.3.2 負載測試 |

---

## 附錄：測試資料清理腳本

### 清理測試專案

**PowerShell 腳本**：
```powershell
# 連接至 Dataverse
Connect-CrmOnline -ServerUrl "https://<org>.crm.dynamics.com"

# 刪除測試專案
$projects = Get-CrmRecords -EntityLogicalName "gov_projectregistry" `
                           -FilterAttribute "gov_title" `
                           -FilterOperator "like" `
                           -FilterValue "TEST-%"

foreach ($project in $projects.CrmRecords) {
    Remove-CrmRecord -EntityLogicalName "gov_projectregistry" `
                     -Id $project.ProjectRegistryId
    Write-Host "Deleted project: $($project.gov_requestid)"
}

# 刪除測試 Review Decision Log
$reviews = Get-CrmRecords -EntityLogicalName "gov_reviewdecisionlog" `
                          -FilterAttribute "gov_parentproject" `
                          -FilterOperator "like" `
                          -FilterValue "DR-TEST-%"

foreach ($review in $reviews.CrmRecords) {
    Remove-CrmRecord -EntityLogicalName "gov_reviewdecisionlog" `
                     -Id $review.ReviewDecisionLogId
}

Write-Host "Test data cleanup completed."
```

---

## 附錄：常見問題排查

### Flow 執行失敗：SecLib::AccessCheckEx failed

**原因**：Service Principal 無權限寫入 Flow-only 欄位。

**解決步驟**：
1. 檢查 Field-Level Security Profile 設定
2. 確認 Service Principal 已加入 FLS Profile 的 Team
3. 重新測試

### Approval 未發送給審核者

**原因**：Security Group 成員未正確設定。

**解決步驟**：
1. 檢查 Entra ID Security Group 成員清單
2. 確認 Group 為 Mail-enabled
3. 測試 Approvals App 是否能正常接收通知

### GOV-017 無法自動回滾

**原因**：Audit Log 查詢失敗或 OldValue 為 null。

**解決步驟**：
1. 檢查 Dataverse Audit 是否啟用
2. 驗證 Audit Log 保留期限（預設 90 天）
3. 若 OldValue = null，需手動回滾並更新 RollbackStatus = ManualRequired

### SharePoint 文件庫權限設定失敗

**原因**：SharePoint API 權限不足。

**解決步驟**：
1. 檢查 Service Principal 是否有 SharePoint Site Collection Administrator 權限
2. 使用 PnP PowerShell 手動設定權限
3. 驗證 SharePoint Connection 是否正確

---

## 附錄：測試案例覆蓋率報告

### Coverage Summary

| Flow | Test Cases | Happy Path | Rejection Path | Anti-Cheating | Integration |
|------|-----------|:---:|:---:|:---:|:---:|
| **GOV-001** | 3 | ✓ | ✓ | - | ✓ |
| **GOV-002** | 3 | ✓ | ✓ | - | ✓ |
| **GOV-003** | 4 | ✓ | ✓ | - | ✓ |
| **GOV-004** | 3 | ✓ | ✓ | - | ✓ |
| **GOV-005** | 2 | ✓ | ✓ | - | ✓ |
| **GOV-013** | 1 | ✓ | - | - | ✓ |
| **GOV-014** | 1 | ✓ | - | - | ✓ |
| **GOV-015** | 1 | ✓ | - | - | ✓ |
| **GOV-016** | 2 | ✓ | ✓ | - | ✓ |
| **GOV-017** | 3 | ✓ | - | ✓ | - |
| **GOV-018** | 2 | ✓ | - | ✓ | - |
| **GOV-019** | 1 | ✓ | - | ✓ | - |

### 總覆蓋率

| 測試類型 | 覆蓋率 |
|:--------|:------|
| Happy Path | 100%（12/12） |
| Rejection Path | 58%（7/12） |
| Anti-Cheating | 25%（3/12） |
| Integration | 75%（9/12） |

---

## 版本歷史

| 版本 | 日期 | 變更說明 |
|:-----|:-----|:---------|
| 1.0 | 2026-01-29 | 初版建立 |
| 1.1 | 2026-02-09 | 新增 BOM 測試案例 |
| 1.2 | 2026-02-11 | 鑑識修訂：E2E-009 Project Closure Flow ID 修正（GOV-012→GOV-009） |
| 1.3 | 2026-02-11 | 日常流程修訂：新增 5 個 E2E 測試案例（E2E-014 Baseline Seeding、E2E-015 Draft 版本推進、E2E-016 Superseded 不可逆、E2E-017 Link 目標規則、E2E-018 Deliverable Package 初始化）；更新 E2E 完成定義清單 |

---

**文件結束**

本文件定義了設計治理系統的完整測試與驗收標準。所有測試案例必須在上線前通過，所有驗收項目必須簽核完成，方可正式上線。

**文件狀態**：正式發佈
**最後更新**：2026-01-29


---

## P0 修正紀錄

**修正日期**：2026-02-08
**修正依據**：02-dataverse-data-model-and-security.md（權威來源）
**修正理由**：移除已淘汰的專案狀態

### 修正項目

1. 修正 DEV 環境 Flow 狀態: Draft→Unpublished（Flow 發佈狀態）
2. 修正 RollbackStatus 值: Completed→Closed

### 狀態對照表

| 已淘汰狀態 | 正確狀態 | OptionSet 值 | 說明 |
|:----------|:--------|:------------|:-----|
| Completed | Closed | 807660002 | 專案正常結案 |
| Cancelled | Terminated | 807660003 | 專案異常終止 |
| Draft（Flow） | Unpublished | N/A | Flow 發佈狀態，非專案狀態 |

**重要**：
- 專案狀態僅有：Active (807660000)、OnHold (807660001)、Closed (807660002)、Terminated (807660003)
- Draft 已淘汰，專案建立即為 Active 狀態
- PreGate0 = Active + currentgate = Pending (807660000)

**修正執行人員**：Claude Sonnet 4.5
**修正工具**：fix_p0_deprecated_states.py
