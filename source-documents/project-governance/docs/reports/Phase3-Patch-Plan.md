# PHASE 3：結構性修補計畫（Patch Plan v1.0）

**版本**：v1.0
**產出日期**：2026-02-11
**執行者**：治理系統鑑識與重構總工程師

---

## 修訂順序與理由

修補必須依以下順序執行，每一步都建立在前一步的結果之上：

```
Step 1: 收斂單一真相來源（解決權威衝突）
    │
Step 2: 修復資料模型缺口（Doc 02）
    │
Step 3: 統一 SharePoint 架構（Doc 03 + Doc 01）
    │
Step 4: 修復 Guardrail Schema 前綴（Doc 06）
    │
Step 5: 補齊 Flow 施工規格映射（Doc 05 + Doc 04）
    │
Step 6: 修復輔助文件一致性（Doc 00B, 00C）
    │
Step 7: 修復測試案例與版本追溯（Doc 07 + 全部）
```

---

## Patch 項目清單

### PATCH-001：Doc 01 SharePoint 權限修正（RF-FATAL-002）

| 項目 | 內容 |
|------|------|
| **修補目標** | 消除 Doc 01 與 Doc 03 的 SharePoint 權限矛盾 |
| **涉及文件** | 01-prerequisites-and-environment.md |
| **具體修改** | 第 7.3 節「設定 SharePoint 權限」：將 GOV-Architects 從 **Edit** 改為 **Read**；將 GOV-GovernanceLead 從 **Full Control** 改為 **Read**；保留 Flow Service Principal 為唯一 Contribute 主體 |
| **權威依據** | Doc 03 為 SharePoint 權威文件，原則三明確宣告「正式專案檔案寫入權專屬 Flow Service Principal」 |
| **欄位新增/刪除** | 無 |
| **回歸測試** | 驗證 Doc 01 權限表與 Doc 03 權限矩陣完全一致 |
| **風險** | 低 — 僅修改文字描述 |

---

### PATCH-002：Doc 02 補充 Document Register 凍結欄位（RF-FATAL-003, RF-DRIFT-003）

| 項目 | 內容 |
|------|------|
| **修補目標** | 在 Document Register 資料表新增 `gov_isfrozen` 與 `gov_frozendate` 欄位，使 Doc 03 凍結設計可實作 |
| **涉及文件** | 02-dataverse-data-model-and-security.md |
| **具體修改** | gov_documentregister 欄位定義表新增兩列 |
| **欄位新增** | `gov_isfrozen`（Yes/No, Flow-only, Default: No）、`gov_frozendate`（Date and Time, Flow-only） |
| **權威裁決** | 凍結狀態雙層追蹤：Project Registry 層級（已有 gov_documentfreezestatus）+ Document Register 層級（新增 gov_isfrozen），前者為專案整體凍結狀態，後者為個別文件凍結狀態 |
| **回歸測試** | 驗證 GOV-014 可同時更新兩層凍結狀態 |
| **風險** | 低 — 新增欄位，不影響既有結構 |

---

### PATCH-003：Doc 02 補充 DocumentType Choice 三個遺漏值（RF-DRIFT-007）

| 項目 | 內容 |
|------|------|
| **修補目標** | 使 Doc 02 的 gov_documenttype Choice 與 Doc 03 的 DocumentType 清單一致 |
| **涉及文件** | 02-dataverse-data-model-and-security.md |
| **具體修改** | gov_documenttype Choice 新增三個值 |
| **欄位新增** | `DesignObjectInventory`（100000013）、`ChangeImpact`（100000014）、`DocumentRegister`（100000015） |
| **回歸測試** | 驗證所有 DocumentType 值在 Dataverse 與 Doc 03 對應表中一致 |

---

### PATCH-004：Doc 02 補充 SA Handover Event 資料表（SCN-017）

| 項目 | 內容 |
|------|------|
| **修補目標** | 將 Doc 04 提及的 SA Handover Event 資料表正式納入資料模型 |
| **涉及文件** | 02-dataverse-data-model-and-security.md |
| **具體修改** | 新增 gov_sahandoverevent 資料表定義 |
| **欄位新增** | gov_handoverid(PK), gov_parentproject(Lookup), gov_originalsa(Lookup User), gov_newsa(Lookup User), gov_handoverreason(Text), gov_handoverstatus(Choice), gov_requesteddate(DateTime), gov_accepteddate(DateTime), gov_comments(Text) — 全部 Flow-only |
| **回歸測試** | 驗證 FORM-001B 與 GOV-001B 可正確引用此表 |

---

### PATCH-005：Doc 02 補充 BOM Registry 種子資料與 Counter List 對應（SCN-018, SCN-019）

| 項目 | 內容 |
|------|------|
| **修補目標** | 為 BOM Registry 新增 Counter List 種子記錄（BOMID） |
| **涉及文件** | 02-dataverse-data-model-and-security.md |
| **具體修改** | Counter List 種子資料表新增一列：CounterName=BOMID, Prefix=BOM |
| **回歸測試** | 驗證 Counter List 有 7 筆記錄（原 6 + BOMID） |

---

### PATCH-006：Doc 02 修正 Gate 參考檔名（RF-DRIFT-001）

| 項目 | 內容 |
|------|------|
| **修補目標** | 修正 Data Model Ready Gate 的後續文件引用 |
| **涉及文件** | 02-dataverse-data-model-and-security.md |
| **具體修改** | Line 1735：`03-Power-Automate-Flows-Implementation.md` → `03-sharepoint-architecture.md` |
| **回歸測試** | 驗證所有 Gate 參考指向正確檔案 |

---

### PATCH-007：Doc 02 修正版本歷史（RF-AUDIT-001）

| 項目 | 內容 |
|------|------|
| **修補目標** | 補齊 v2.1 版本記錄 |
| **涉及文件** | 02-dataverse-data-model-and-security.md |
| **具體修改** | 版本歷史表新增 v2.1 條目，說明新增 BOM Registry 資料表、SA Handover Event 資料表、Document Register 凍結欄位、DocumentType 補齊 |

---

### PATCH-008：Doc 02 修正 UploadedBy 欄位型別（RF-DRIFT-002）

| 項目 | 內容 |
|------|------|
| **修補目標** | 統一 Document Register.UploadedBy 型別 |
| **涉及文件** | 02-dataverse-data-model-and-security.md（權威）, 03-sharepoint-architecture.md（需對齊） |
| **權威裁決** | Doc 02 定義為 Lookup (User)，此為正確型別。Doc 03 第 7.2 節描述需更正為 Lookup 一致 |
| **回歸測試** | 驗證 GOV-005 傳入 User Lookup 物件 |

---

### PATCH-009：Doc 03 修正 Document Register 欄位描述（RF-DRIFT-002）

| 項目 | 內容 |
|------|------|
| **修補目標** | 使 Doc 03 的 Document Register 欄位描述與 Doc 02 一致 |
| **涉及文件** | 03-sharepoint-architecture.md |
| **具體修改** | 第 8.1 節 Document Register 欄位表：`Uploaded By` 從 `Text` 改為 `Lookup (User)`；新增 `gov_isfrozen` 與 `gov_frozendate` 欄位描述以對齊 PATCH-002 |

---

### PATCH-010：Doc 06 全文 Schema 前綴修正（RF-FATAL-001）

| 項目 | 內容 |
|------|------|
| **修補目標** | 將 Doc 06 全文 `cr_` 前綴替換為 `gov_` |
| **涉及文件** | 06-guardrails-and-anti-cheating.md |
| **具體修改** | 全域替換：`cr_projectregistry` → `gov_projectregistry`；`cr_reviewdecisionlog` → `gov_reviewdecisionlog`；`cr_riskassessmenttable` → `gov_riskassessmenttable`；`cr_governanceviolationlog` → `gov_governanceviolationlog`；所有 `cr_` 欄位前綴 → `gov_` |
| **回歸測試** | 驗證 Doc 06 無任何 `cr_` 出現；所有 Schema Name 與 Doc 02 定義一致 |
| **風險** | 中 — 全文替換需仔細檢查是否有非目標替換 |

---

### PATCH-011：Doc 06 補齊 8 個遺漏的 Flow-only 監控欄位（RF-GOV-005）

| 項目 | 內容 |
|------|------|
| **修補目標** | GOV-017 監控清單補齊所有 Flow-only 欄位 |
| **涉及文件** | 06-guardrails-and-anti-cheating.md |
| **具體修改** | Flow-only 欄位 JSON 清單新增：gov_riskacceptancedate, gov_riskowner, gov_executiveapprover, gov_reworkcount, gov_lastreworkdate, gov_riskownerreviewstatus, gov_executivereviewstatus, gov_residualrisklevel |
| **回歸測試** | 驗證 GOV-017 JSON 清單與 Doc 02 的 Flow-only 欄位清單完全一致 |

---

### PATCH-012：Doc 06 修正 Dataverse Web API URI（RF-FATAL-006）

| 項目 | 內容 |
|------|------|
| **修補目標** | 修正回滾 HTTP PATCH 的 URI 格式 |
| **涉及文件** | 06-guardrails-and-anti-cheating.md |
| **具體修改** | 提供 Dataverse OData 實體集名稱對應表（gov_projectregistry → gov_projectregistries 等），並修正 PATCH URI 範例 |
| **回歸測試** | 驗證 HTTP PATCH URI 可成功呼叫 Dataverse API |

---

### PATCH-013：Doc 06 GOV-018 文件連結驗證新增認證（RF-GOV-007）

| 項目 | 內容 |
|------|------|
| **修補目標** | HTTP HEAD 請求加入 Azure AD 認證 |
| **涉及文件** | 06-guardrails-and-anti-cheating.md |
| **具體修改** | GOV-018 文件連結驗證步驟新增 Authentication 設定：使用 Service Principal OAuth Token |
| **回歸測試** | 驗證 HEAD 請求對 SharePoint URL 回傳 200 而非 403 |

---

### PATCH-014：Doc 06 GOV-017 偵測改為 Checkpoint 機制（RF-DRIFT-005）

| 項目 | 內容 |
|------|------|
| **修補目標** | 消除偵測時間窗盲區 |
| **涉及文件** | 06-guardrails-and-anti-cheating.md |
| **具體修改** | 將 `addHours(utcNow(), -1)` 改為讀取上次成功執行時間戳記（存於 Environment Variable 或 Counter List），執行結束時更新時間戳記 |
| **回歸測試** | 驗證連續兩次執行無時間缺口 |

---

### PATCH-015：Doc 04 修正版本標頭（RF-AUDIT-002）

| 項目 | 內容 |
|------|------|
| **修補目標** | 版本標頭與實際版本一致 |
| **涉及文件** | 04-powerapps-forms.md |
| **具體修改** | 標頭版本從 v6.0 修正為 v7.2（本次修訂），並在版本歷史中新增 v7.2 條目 |

---

### PATCH-016：Doc 04 修正 Flow ID 重複（RF-GOV-004）

| 項目 | 內容 |
|------|------|
| **修補目標** | 消除 GOV-006 ID 重複 |
| **涉及文件** | 04-powerapps-forms.md |
| **具體修改** | 重新分配 Flow ID：FORM-005 → GOV-020-RiskReassessment（新 ID）；FORM-006 → GOV-006-GateCancellation（保留） |
| **回歸測試** | 驗證所有 Form-Flow 映射表無 ID 重複 |

---

### PATCH-017：Doc 04 修正 Project Closure Flow ID（SCN-014）

| 項目 | 內容 |
|------|------|
| **修補目標** | 統一 Project Closure 的 Flow ID |
| **涉及文件** | 04-powerapps-forms.md, 07-testing-and-acceptance.md |
| **權威裁決** | 採用 GOV-009（Doc 04 定義），Doc 07 的 GOV-012 修正為 GOV-009 |

---

### PATCH-018：Doc 00B 修正 Counter List 欄位（RF-GOV-001）

| 項目 | 內容 |
|------|------|
| **修補目標** | 使初始化清單的欄位名稱與 Doc 02 一致 |
| **涉及文件** | 00B-first-run-initialization-checklist.md |
| **具體修改** | CounterType → CounterName；CurrentValue → CurrentCounter；刪除 YearFormat/Separator/Description（Doc 02 無此欄位）；新增 CurrentYear = 2026, LastUpdated = 執行日期 |

---

### PATCH-019：Doc 00B 修正安全群組名稱（RF-GOV-002）

| 項目 | 內容 |
|------|------|
| **修補目標** | 使群組名稱與 Doc 01 一致 |
| **涉及文件** | 00B-first-run-initialization-checklist.md |
| **具體修改** | GOV-GovernanceLeads → GOV-GovernanceLead；刪除 GOV-SystemAdmins（Doc 01 無此群組）；新增 GOV-EngineeringManagement、GOV-FlowServicePrincipal |

---

### PATCH-020：Doc 00B 修正 Service Principal 角色名稱（RF-GOV-003）

| 項目 | 內容 |
|------|------|
| **修補目標** | 角色名稱與 Doc 02 一致 |
| **涉及文件** | 00B-first-run-initialization-checklist.md |
| **具體修改** | GOV-FlowServiceRole → GOV-FlowServicePrincipal |

---

### PATCH-021：Doc 00B 修正 SharePoint 資料夾結構（RF-FATAL-004）

| 項目 | 內容 |
|------|------|
| **修補目標** | 統一資料夾結構為 Doc 03 權威版本 |
| **涉及文件** | 00B-first-run-initialization-checklist.md |
| **具體修改** | 驗證步驟中的資料夾：Gate0/Gate1/Gate2/Gate3/_Working/_Archive → 01_Feasibility/02_Risk_Assessment/03_Design/04_Security/05_Test/06_Handover |

---

### PATCH-022：Doc 00B 修正 RequestID 格式（RF-AUDIT-003）

| 項目 | 內容 |
|------|------|
| **修補目標** | 統一 RequestID 格式 |
| **涉及文件** | 00B-first-run-initialization-checklist.md, 01-prerequisites-and-environment.md |
| **權威裁決** | 採用 Doc 01 格式 `DR-{YYYY}-{####}`（4 位序號），Doc 00B 的 `{8碼}` 修正為 `{####}` |

---

### PATCH-023：Doc 07 修正 GOV-012 引用（PATCH-017 連動）

| 項目 | 內容 |
|------|------|
| **修補目標** | E2E-009 中 GOV-012 修正為 GOV-009 |
| **涉及文件** | 07-testing-and-acceptance.md |
| **具體修改** | 所有 GOV-012 引用替換為 GOV-009 |

---

### PATCH-024：全部文件版本號更新

| 項目 | 內容 |
|------|------|
| **修補目標** | 所有修改文件版本號 +0.1，附 Changelog |
| **涉及文件** | 01, 02, 03, 04, 06, 07, 00B |
| **具體修改** | 見 PHASE 4 各文件 Changelog |

---

## 修訂順序總表

| 優先序 | Patch ID | 目標文件 | 修補類型 | 阻斷等級 |
|:------:|----------|---------|---------|:--------:|
| 1 | PATCH-010 | Doc 06 | Schema 前綴全文修正 | FATAL |
| 2 | PATCH-012 | Doc 06 | API URI 修正 | FATAL |
| 3 | PATCH-001 | Doc 01 | SharePoint 權限修正 | FATAL |
| 4 | PATCH-002 | Doc 02 | Document Register 凍結欄位 | FATAL |
| 5 | PATCH-021 | Doc 00B | 資料夾結構統一 | FATAL |
| 6 | PATCH-003 | Doc 02 | DocumentType Choice 補齊 | DRIFT |
| 7 | PATCH-004 | Doc 02 | SA Handover Event 資料表 | DRIFT |
| 8 | PATCH-005 | Doc 02 | BOM Counter List | DRIFT |
| 9 | PATCH-006 | Doc 02 | Gate 參考檔名修正 | DRIFT |
| 10 | PATCH-007 | Doc 02 | 版本歷史補齊 | AUDIT |
| 11 | PATCH-008 | Doc 02 | UploadedBy 型別確認 | DRIFT |
| 12 | PATCH-009 | Doc 03 | Document Register 欄位對齊 | DRIFT |
| 13 | PATCH-011 | Doc 06 | 監控欄位補齊 | GOV |
| 14 | PATCH-013 | Doc 06 | HTTP 認證 | GOV |
| 15 | PATCH-014 | Doc 06 | Checkpoint 機制 | DRIFT |
| 16 | PATCH-015 | Doc 04 | 版本標頭修正 | AUDIT |
| 17 | PATCH-016 | Doc 04 | Flow ID 重複修正 | GOV |
| 18 | PATCH-017 | Doc 04+07 | Project Closure ID 統一 | GOV |
| 19 | PATCH-018 | Doc 00B | Counter List 欄位 | GOV |
| 20 | PATCH-019 | Doc 00B | 安全群組名稱 | GOV |
| 21 | PATCH-020 | Doc 00B | SP 角色名稱 | GOV |
| 22 | PATCH-022 | Doc 00B+01 | RequestID 格式 | AUDIT |
| 23 | PATCH-023 | Doc 07 | GOV-012→009 | GOV |
| 24 | PATCH-024 | 全部 | 版本號+Changelog | AUDIT |

---

**報告結束。下一步：PHASE 4 執行修訂。**
