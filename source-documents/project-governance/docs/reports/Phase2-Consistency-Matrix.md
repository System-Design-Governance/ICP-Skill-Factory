# PHASE 2：全系統情境一致性矩陣

**報告版本**：v1.0
**產出日期**：2026-02-11
**執行者**：治理系統鑑識與重構總工程師

---

## A. 完整情境一致性矩陣（Consistency Matrix）

### 矩陣說明

每列代表一個治理情境，包含從入口表單到測試案例的完整端到端路徑。
標示 `⚠` 表示存在不一致或缺口。

---

### SCN-001：專案建立（Project Creation）

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-001 | — |
| 入口表單 | FORM-001（Project Creation） | ✓ |
| 呼叫 Flow | GOV-001（Create Project） | ✓ |
| Trigger 類型 | HTTP Request（from Power Apps Button.OnSelect） | ✓ |
| Flow Input Contract | Title, SystemArchitect, ProjectManager, ProjectType, TargetSL, ProjectDescription | ⚠ SA 型別爭議 |
| 寫入 Dataverse Table | gov_projectregistry（建立）, gov_reviewdecisionlog（建立）, gov_counterlist（更新） | ✓ |
| 寫入 Column | gov_requestid, gov_title, gov_projecttype, gov_targetsl, gov_systemarchitect, gov_projectmanager, gov_projectdescription, gov_currentgate=Pending, gov_requeststatus=None, gov_projectstatus=Active, gov_documentfreezestatus=NotFrozen, gov_sharepointfolderurl | ✓ |
| SharePoint 動作 | 建立專案根目錄 + 6 個子資料夾 | ⚠ **資料夾名稱矛盾** |
| SharePoint 權限主體 | Flow SP = Contribute; 所有人類群組 = Read | ⚠ **Doc 01 vs Doc 03 矛盾** |
| Guardrail 監控點 | GOV-017 監控 gov_requestid, gov_currentgate, gov_requeststatus 等 Flow-only 欄位 | ⚠ **Doc 06 Schema 前綴錯誤** |
| Review Decision Log | 寫入 ReviewType=ProjectCreation, Decision=Executed | ✓ |
| 對應測試案例 | E2E-001 Phase 1, E2E-005, E2E-007 | ✓ |

**問題清單**：
1. SystemArchitect 參數：User Lookup 物件 vs Email 字串未統一（RF-DRIFT-006）
2. 資料夾結構：Doc 03 vs 00B vs App-A 三方矛盾（RF-FATAL-004）
3. SharePoint 權限：Doc 01 給 Architects Edit，Doc 03 給 Read（RF-FATAL-002）
4. GOV-017 偵測使用 `cr_` 前綴，無法偵測違規（RF-FATAL-001）

---

### SCN-002：Gate 0 申請與審批

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-002 | — |
| 入口表單 | FORM-002（Gate Transition Request） | ✓ |
| 呼叫 Flow | GOV-002（Gate Transition Request）→ GOV-003（Gate Approval Orchestrator） | ✓ |
| Trigger 類型 | HTTP Request → Child Flow（Manual） | ✓ |
| Flow Input Contract | ProjectId, RequestedGate=Gate0 | ✓ |
| 寫入 Dataverse Table | gov_projectregistry（更新）, gov_reviewdecisionlog（建立） | ✓ |
| 寫入 Column | gov_requeststatus=Pending→Approved/Rejected, gov_currentgate=Gate0（if approved）, gov_gate0passeddate, gov_requestedgate | ✓ |
| SharePoint 動作 | 無 | ✓ |
| Guardrail 監控點 | GOV-017 監控 gov_currentgate, gov_requeststatus | ⚠ Schema 前綴 |
| Approval 主體 | GOV-EngineeringManagement（1 層） | ✓ |
| Review Decision Log | ReviewType=Gate0Request, Decision=Approved/Rejected | ✓ |
| 對應測試案例 | E2E-001 Phase 2, E2E-002 | ✓ |

**問題清單**：
1. GOV-017 Schema 前綴錯誤（RF-FATAL-001）

---

### SCN-003：Gate 1 三層審批

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-003 | — |
| 入口表單 | FORM-002（Gate Transition Request） | ✓ |
| 呼叫 Flow | GOV-002 → GOV-003（3 層序列審批） | ✓ |
| Trigger 類型 | HTTP Request → Child Flow | ✓ |
| Flow Input Contract | ProjectId, RequestedGate=Gate1 | ✓ |
| 寫入 Dataverse Table | gov_projectregistry, gov_reviewdecisionlog | ✓ |
| 寫入 Column | gov_gate1securityreviewstatus, gov_gate1securityreviewer, gov_gate1securityreviewdate, gov_gate1qareviewstatus, gov_gate1qareviewer, gov_gate1qareviewdate, gov_gate1governancereviewstatus, gov_gate1governancereviewer, gov_gate1governancereviewdate, gov_currentgate=Gate1, gov_gate1passeddate | ✓ |
| Approval 主體（序列） | Layer 1: GOV-SecurityReviewers → Layer 2: GOV-QAReviewers → Layer 3: GOV-GovernanceLead | ✓ |
| Review Decision Log | ReviewType=Gate1Request, 含三層審批紀錄 | ✓ |
| 對應測試案例 | E2E-001 Phase 3, E2E-003 | ✓ |

**問題清單**：
1. GOV-017 Schema 前綴錯誤（RF-FATAL-001）

---

### SCN-004：Gate 2 審批

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-004 | — |
| 入口表單 | FORM-002 | ✓ |
| 呼叫 Flow | GOV-002 → GOV-003（1 層） | ✓ |
| Approval 主體 | GOV-EngineeringManagement（1 層） | ✓ |
| 寫入 Column | gov_currentgate=Gate2, gov_gate2passeddate | ✓ |
| 對應測試案例 | E2E-001 Phase 4 | ✓ |

---

### SCN-005：風險接受（Risk Acceptance）

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-005 | — |
| 入口表單 | FORM-002（Gate 3 觸發時自動連鎖） | ✓ |
| 呼叫 Flow | GOV-002 → GOV-013（Risk Level Calculator）→ GOV-004（Risk Acceptance） | ✓ |
| Trigger 類型 | Child Flow chain | ✓ |
| 寫入 Dataverse Table | gov_projectregistry, gov_reviewdecisionlog, gov_riskassessmenttable | ✓ |
| 寫入 Column | gov_riskacceptancestatus, gov_riskacceptancedate, gov_riskowner, gov_highestresidualrisklevel | ✓ |
| Approval 主體 | Risk Owner（動態路由）, Executive Management（若 High Risk） | ⚠ Risk Owner 決定機制未明確 |
| 對應測試案例 | E2E-001 Phase 5 | ✓ |

**問題清單**：
1. Risk Owner 如何決定未在任何文件中明確說明（RF-GOV-009 相關）
2. gov_riskowner 未被 GOV-017 監控（RF-GOV-005）

---

### SCN-006：Gate 3 審批 + Document Freeze

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-006 | — |
| 入口表單 | FORM-002 | ✓ |
| 呼叫 Flow | GOV-002 → GOV-003（2 層：QA + Governance）→ GOV-014（Document Freeze） | ✓ |
| 寫入 Column | gov_currentgate=Gate3, gov_gate3passeddate, gov_documentfreezestatus=Frozen, gov_documentfreezedate | ✓ |
| SharePoint 動作 | GOV-014 移除 Flow SP Contribute、授予 Read | ✓ |
| Guardrail | GOV-017 監控 gov_documentfreezestatus | ⚠ Schema 前綴 |
| Review Decision Log | ReviewType=Gate3Request + ReviewType=DocumentFreeze | ✓ |
| 對應測試案例 | E2E-001 Phase 6 | ✓ |

**問題清單**：
1. Doc 03 預期 Document Register 有 IsFrozen，Doc 02 不存在此欄位（RF-FATAL-003）
2. GOV-017 Schema 前綴（RF-FATAL-001）

---

### SCN-007：文件上傳（Document Intake）

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-007 | — |
| 入口表單 | FORM-003（Document Intake） | ✓ |
| 呼叫 Flow | GOV-005（Document Intake and Register） | ✓ |
| Trigger 類型 | HTTP Request | ✓ |
| Flow Input Contract | ProjectId, DocumentType, File, DocumentVersion | ✓ |
| 寫入 Dataverse Table | gov_documentregister（建立）, gov_projectregistry（更新對應 Link 欄位） | ✓ |
| 寫入 Column（Document Register） | gov_documentid, gov_parentproject, gov_documenttype, gov_documentname, gov_sharepointfilelink, gov_uploadedby, gov_uploadeddate | ✓ |
| SharePoint 動作 | 上傳檔案至對應子資料夾 | ⚠ 資料夾對應不確定 |
| 對應測試案例 | E2E-001 涵蓋 | ✓ |

**問題清單**：
1. DocumentType 新增 3 個值（DesignObjectInventory, ChangeImpact, DocumentRegister）在 Doc 03 但不在 Doc 02 Choice 清單中（RF-DRIFT-007）
2. UploadedBy 型別：Doc 02 = Lookup(User), Doc 03 = Text(Email)（RF-DRIFT-002）
3. 資料夾名稱矛盾（RF-FATAL-004）

---

### SCN-008：Gate 申請拒絕與 Rework

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-008 | — |
| 入口表單 | （無，由 Approval 拒絕觸發） | ✓ |
| 呼叫 Flow | GOV-003（拒絕路徑）→ GOV-016（Rework Loop Handler） | ✓ |
| 寫入 Column | gov_requeststatus=Rejected→None, gov_reworkcount++, gov_lastreworkdate | ✓ |
| 特殊邏輯 | ReworkCount ≥ 3 → gov_projectstatus=OnHold | ⚠ |
| 對應測試案例 | E2E-002, E2E-003, E2E-004 | ✓ |

**問題清單**：
1. OnHold 解鎖機制無 Form/Flow（RF-GOV-009）
2. gov_reworkcount 未被 GOV-017 監控（RF-GOV-005）

---

### SCN-009：Gate 取消（Gate Cancellation）

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-009 | — |
| 入口表單 | FORM-006（Gate Cancellation） | ✓ |
| 呼叫 Flow | GOV-006（Gate Request Cancellation） | ⚠ |
| Trigger 類型 | HTTP Request（推測） | ⚠ |
| Flow 施工規格 | **不存在** | ❌ |
| 對應測試案例 | 無專屬測試 | ❌ |

**問題清單**：
1. GOV-006 在 Doc 05 無施工規格（RF-FATAL-005）
2. GOV-006 ID 與 Risk Reassessment 重複（RF-GOV-004）
3. 無測試案例覆蓋

---

### SCN-010：風險項目建立（Risk Item Creation）

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-010 | — |
| 入口表單 | FORM-004（Risk Item Creation） | ⚠ 規格不足 |
| 呼叫 Flow | GOV-004-RiskItemCreate（Doc 04 記載） | ⚠ |
| Flow 施工規格 | **不存在**（Doc 05 的 GOV-004 = Risk Acceptance，非 Risk Item Create） | ❌ |
| 寫入 Dataverse Table | gov_riskassessmenttable（推測） | ⚠ |
| 對應測試案例 | 無專屬測試 | ❌ |

**問題清單**：
1. FORM-004 僅 1-2 行描述（RF-DRIFT-004）
2. Flow 名稱衝突：Doc 04 稱 GOV-004-RiskItemCreate，但 Doc 05 的 GOV-004 = Risk Acceptance
3. 無施工規格、無測試

---

### SCN-011：風險重評估（Risk Reassessment）

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-011 | — |
| 入口表單 | FORM-005（Risk Reassessment） | ⚠ 規格不足 |
| 呼叫 Flow | GOV-006-RiskReassessment（Doc 04 記載） | ⚠ ID 衝突 |
| Flow 施工規格 | **不存在** | ❌ |
| 對應測試案例 | 無專屬測試 | ❌ |

---

### SCN-012：Lite → Full Upgrade

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-012 | — |
| 入口表單 | FORM-007（Lite Upgrade） | ⚠ 規格不足 |
| 呼叫 Flow | GOV-007（Lite to Full Upgrade） | ⚠ |
| Flow 施工規格 | **不存在** | ❌ |
| 對應測試案例 | 無專屬測試 | ❌ |

---

### SCN-013：文件解凍（Document Unfreeze Exception）

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-013 | — |
| 入口表單 | FORM-008（Document Unfreeze） | ⚠ 規格不足 |
| 呼叫 Flow | GOV-008（Document Unfreeze Exception） | ⚠ |
| Flow 施工規格 | **不存在** | ❌ |
| 特殊邏輯 | 需 Governance Lead + Engineering Management 雙層審批 | Doc 03 描述 |
| 對應測試案例 | 無專屬測試 | ❌ |

---

### SCN-014：專案關閉（Project Closure）

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-014 | — |
| 入口表單 | FORM-009（Project Closure） | ⚠ 規格不足 |
| 呼叫 Flow | GOV-009（Project Closure）— Doc 04 記載；Doc 07 引用 GOV-012 | ⚠ ID 衝突 |
| Flow 施工規格 | **不存在** | ❌ |
| 前置條件 | CurrentGate=Gate3, DocumentFreezeStatus=Frozen, RiskAcceptanceStatus=Accepted | Doc 07 |
| 寫入 Column | gov_projectstatus=Closed（推測） | ⚠ |
| 對應測試案例 | E2E-009 | ✓ |

**問題清單**：
1. Doc 04 稱 GOV-009，Doc 07 稱 GOV-012 — Flow ID 衝突
2. 無施工規格

---

### SCN-015：專案暫停（Project Suspension）

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-015 | — |
| 入口表單 | FORM-010（Project Suspension） | ⚠ 規格不足 |
| 呼叫 Flow | GOV-010（Project Suspension/Resume） | ⚠ |
| Flow 施工規格 | **不存在** | ❌ |
| 對應測試案例 | 無專屬測試 | ❌ |

---

### SCN-016：緊急文件上傳（Emergency Document）

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-016 | — |
| 入口表單 | FORM-011（Emergency Document） | ⚠ 規格不足 |
| 呼叫 Flow | GOV-011（Emergency Document） | ⚠ |
| Flow 施工規格 | **不存在** | ❌ |
| 特殊邏輯 | 先上傳至 _Quarantine → Flow 移至正式資料夾 | Doc 03 描述 |
| 對應測試案例 | 無專屬測試 | ❌ |

---

### SCN-017：SA 移交（SA Handover）

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-017 | — |
| 入口表單 | FORM-001B（SA Handover） | ✓ |
| 呼叫 Flow | GOV-001B-SAHandover | ⚠ |
| Flow 施工規格 | **不存在**（Doc 05 無此 Flow） | ❌ |
| 寫入 Dataverse Table | gov_sahandoverevent（Doc 04 提及但 Doc 02 未定義） | ❌ |
| 對應測試案例 | SA-004, SA-005 | ✓ |

**問題清單**：
1. `gov_sahandoverevent` 資料表未在 Doc 02 中定義
2. GOV-001B 無施工規格
3. Presales Append-Only 規則無技術強制機制

---

### SCN-018：CBOM 建立與狀態流轉

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-018 | — |
| 入口表單 | （未定義） | ❌ |
| 呼叫 Flow | （未定義） | ❌ |
| 寫入 Dataverse Table | gov_bomregistry | ⚠ Doc 02 有定義 |
| Flow 施工規格 | **不存在** | ❌ |
| 對應測試案例 | E2E-010, E2E-012, E2E-013 | ✓ |

**問題清單**：
1. BOM Registry 資料表已定義但無 Form 入口、無 Flow 寫入路徑（RF-GOV-008）
2. 有測試但無實作

---

### SCN-019：EBOM 建立與基線管理

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-019 | — |
| 入口表單 | （未定義） | ❌ |
| 呼叫 Flow | （未定義） | ❌ |
| 寫入 Dataverse Table | gov_bomregistry | ⚠ |
| 對應測試案例 | E2E-011, E2E-013 | ✓ |

**問題清單**：同 SCN-018

---

### SCN-020：Guardrail 監控（排程）

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-020 | — |
| 入口表單 | 無（排程觸發） | ✓ |
| 呼叫 Flow | GOV-017（Guardrail Monitor） | ✓ |
| Trigger 類型 | Scheduled（每小時） | ✓ |
| 寫入 Dataverse Table | gov_governanceviolationlog（建立）, 各表（回滾） | ✓ |
| 對應測試案例 | AC-001, AC-002, AC-003, AC-007 | ✓ |

**問題清單**：
1. Schema 前綴全錯 `cr_` vs `gov_`（RF-FATAL-001）
2. 回滾 HTTP URI 格式錯（RF-FATAL-006）
3. 8 個欄位未被監控（RF-GOV-005）
4. 偵測時間窗有盲區（RF-DRIFT-005）

---

### SCN-021：合規性對帳（排程）

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-021 | — |
| 入口表單 | 無（排程觸發） | ✓ |
| 呼叫 Flow | GOV-018（Compliance Reconciler） | ✓ |
| Trigger 類型 | Scheduled（每日 00:00 UTC+8） | ✓ |
| 寫入 Dataverse Table | gov_governanceviolationlog | ✓ |
| 對應測試案例 | AC-004, AC-005 | ✓ |

**問題清單**：
1. Schema 前綴錯（RF-FATAL-001）
2. HTTP 文件連結驗證缺認證（RF-GOV-007）

---

### SCN-022：SLA 監控（排程）

| 項目 | 值 | 狀態 |
|------|-----|:----:|
| 情境代號 | SCN-022 | — |
| 入口表單 | 無（排程觸發） | ✓ |
| 呼叫 Flow | GOV-019（SLA Monitor） | ✓ |
| Trigger 類型 | Scheduled（每日） | ✓ |
| 動作 | 讀取 Review Decision Log → 呼叫 GOV-015 通知 | ✓ |
| 對應測試案例 | AC-006 | ✓ |

---

## B. 錯位與缺口清單（Gap Analysis）

### 1. 完全斷鏈情境（有表單無 Flow 施工規格）

| 情境 | 表單 | 預期 Flow | Doc 05 是否涵蓋 | 狀態 |
|------|------|----------|:---------------:|:----:|
| SCN-009 Gate Cancellation | FORM-006 | GOV-006 | ❌ | 斷鏈 |
| SCN-010 Risk Item Create | FORM-004 | GOV-004* | ❌ 名稱衝突 | 斷鏈 |
| SCN-011 Risk Reassessment | FORM-005 | GOV-006* | ❌ ID 重複 | 斷鏈 |
| SCN-012 Lite Upgrade | FORM-007 | GOV-007 | ❌ | 斷鏈 |
| SCN-013 Document Unfreeze | FORM-008 | GOV-008 | ❌ | 斷鏈 |
| SCN-014 Project Closure | FORM-009 | GOV-009/012 | ❌ ID 衝突 | 斷鏈 |
| SCN-015 Project Suspension | FORM-010 | GOV-010 | ❌ | 斷鏈 |
| SCN-016 Emergency Document | FORM-011 | GOV-011 | ❌ | 斷鏈 |
| SCN-017 SA Handover | FORM-001B | GOV-001B | ❌ | 斷鏈 |

### 2. 有 Flow 規格但無情境入口

| Flow | 有施工規格 | 情境入口 | 狀態 |
|------|:---------:|---------|:----:|
| GOV-013 Risk Level Calculator | ✓ | 由 GOV-002 呼叫（Child Flow） | ✓ 正常 |
| GOV-014 Document Freeze | ✓ | 由 GOV-003 呼叫（Child Flow） | ✓ 正常 |
| GOV-015 Notification Handler | ✓ | 由多個 Parent Flow 呼叫 | ✓ 正常 |
| GOV-016 Rework Loop Handler | ✓ | 由 GOV-003 呼叫 | ✓ 正常 |

### 3. 有資料表但無寫入路徑

| Dataverse Table | Doc 02 定義 | 有 Flow 寫入 | 有 Form 入口 |
|-----------------|:-----------:|:------------:|:------------:|
| gov_bomregistry | ✓ | ❌ | ❌ |
| gov_sahandoverevent* | ❌（僅 Doc 04 提及）| ❌ | ✓（FORM-001B）|

### 4. 有狀態更新但未寫 Review Decision Log

| 情境 | 狀態變更 | 是否寫 RDL | 問題 |
|------|---------|:----------:|------|
| OnHold（ReworkCount≥3） | gov_projectstatus=OnHold | ❌ 未確認 | 自動觸發的狀態變更可能無稽核記錄 |
| OnHold 解鎖 | gov_projectstatus=Active | 機制不存在 | 無法產生任何記錄 |

### 5. 測試案例涵蓋率

| 情境 | 有完整測試案例 | 有部分測試 | 無測試 |
|------|:------------:|:---------:|:------:|
| SCN-001 至 SCN-008 | ✓（8 個） | — | — |
| SCN-009 至 SCN-017 | — | — | ❌（9 個無測試）|
| SCN-018, SCN-019 | ✓（BOM 測試）| — | — |
| SCN-020 至 SCN-022 | ✓（3 個） | — | — |
| **總計** | 13/22 | 0 | **9/22（41%）** |

---

## C. PHASE 2 結論

### 矩陣覆蓋統計

| 指標 | 值 |
|------|-----|
| 總情境數 | 22 |
| 完全覆蓋（Form + Flow + Test） | 11（50%）|
| 部分覆蓋（缺 Flow 或 Test） | 2（9%）|
| 斷鏈（缺 Flow 施工規格） | 9（41%）|
| 架構不一致問題數 | 32（Phase 1 已列舉）|

### 關鍵發現

1. **41% 情境斷鏈**：9/22 情境有表單但無 Flow 施工規格
2. **BOM 全面斷鏈**：資料表已定義、測試已寫，但無 Form、無 Flow
3. **Flow ID 衝突**：GOV-004（Risk Acceptance vs Risk Item Create）、GOV-006（Gate Cancel vs Risk Reassessment）、GOV-009/012（Project Closure）
4. **所有 Guardrail 情境**（SCN-020~022）因 Schema 前綴錯誤而全面失效

**下一步**：進入 PHASE 3 制定修補計畫。

---

**報告結束**
