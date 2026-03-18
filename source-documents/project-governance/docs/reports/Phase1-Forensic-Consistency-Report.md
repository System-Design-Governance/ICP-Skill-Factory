# PHASE 1：文件一致性鑑識報告

**報告版本**：v1.0
**產出日期**：2026-02-11
**執行者**：治理系統鑑識與重構總工程師
**報告性質**：鑑識級完整檢查結果

---

## A. 文件地圖（Document Map）

| # | 文件 | 版本 | 權威定位 | 前置文件 | 引用鏈 |
|---|------|------|---------|---------|--------|
| 00 | 00-index.md | v1.0 | 導覽文件 | 無 | → 00A, 00B, 00C, 01-07 |
| 00A | 00A-build-order-and-bootstrap.md | v1.0 | 建置順序權威 | 00 | → 01-07（Phase 分割） |
| 00B | 00B-first-run-initialization-checklist.md | v1.0 | 初始化檢查清單 | Phase 1 完成 | → 02（Counter List）, 01（Groups） |
| 00C | 00C-placeholder-reference.md | v1.0 | 環境變數參考 | 無 | ← 05, 06, 07 引用 |
| 01 | 01-prerequisites-and-environment.md | v2.0 | **施工權威**（環境） | 無 | → 02 |
| 02 | 02-dataverse-data-model-and-security.md | v2.1* | **施工權威**（資料模型）| 01 | → 03 |
| 03 | 03-sharepoint-architecture.md | v2.0 | **施工權威**（SharePoint）| 01, 02 | → 04 |
| 04 | 04-powerapps-forms.md | v7.1** | **施工權威**（表單）| 01, 02, 03 | → 05 |
| 05 | 05-core-flows-implementation-runbook.md | v2.0 | **唯一 Flow 實作權威** | 01, 02, 03, 04(P1) | → 04(P3), 07 |
| 06 | 06-guardrails-and-anti-cheating.md | — | **治理語意權威**（設計說明）| 05 | ← 02, 05 交叉引用 |
| 07 | 07-testing-and-acceptance.md | — | **測試權威** | 全部 | ← 04, 05, 06 |
| A | appendix/A-core-flows-specification.md | v1.0 | **參考規格**（禁止作為實作依據）| 無 | ← 00 聲明其定位 |

> \* v2.1 版本號出現於文件標頭，但版本歷史僅記錄至 v2.0。
> \** v7.1 為實際最新版，但文件標頭聲稱 v6.0（Anti-Fragile Edition）。

---

## B. Red Flag 表（依嚴重度排序）

### 致命錯位（FATAL）— 會使系統無法正確建置或產生不可逆資料

| ID | 問題描述 | 涉及文件 | 影響 |
|----|---------|---------|------|
| **RF-FATAL-001** | **Schema 前綴衝突 `cr_` vs `gov_`**：Doc 06 全文使用 `cr_projectregistry`、`cr_reviewdecisionlog`、`cr_riskassessmenttable`、`cr_governanceviolationlog` 等前綴；Doc 02/05 定義為 `gov_` 前綴 | 06 vs 02, 05 | GOV-017 Guardrail Monitor 的 Audit Log 查詢將使用錯誤 Schema Name，**回傳零筆結果**，造成完全的治理防線繞過（三道防線第二道全失效） |
| **RF-FATAL-002** | **SharePoint 權限矛盾**：Doc 01 設定 GOV-Architects = **Edit**、GOV-GovernanceLead = **Full Control**；Doc 03（SharePoint 權威文件）設定 GOV-Architects = **Read**、GOV-GovernanceLead = **Read** | 01 vs 03 | 若依 Doc 01 權限建置，人類帳號可直接寫入專案資料夾，**整體 SharePoint 治理原則崩壞**（Doc 03 原則一至原則四全部失效） |
| **RF-FATAL-003** | **Document Register 缺失凍結欄位**：Doc 03 引用 `Document Register.IsFrozen` 與 `Document Register.FrozenDate`，但 Doc 02（資料模型權威）未定義 `gov_isfrozen` 及 `gov_frozendate` 欄位 | 03 vs 02 | GOV-014 Document Freeze 無法在 Document Register 層級執行凍結，**文件凍結機制部分失效** |
| **RF-FATAL-004** | **SharePoint 資料夾結構三方矛盾**：Doc 03 定義 `01_Feasibility/02_Risk_Assessment/03_Design/04_Security/05_Test/06_Handover`；Doc 00B 測試驗證使用 `Gate0/Gate1/Gate2/Gate3/_Working/_Archive`；Appendix A 使用 `_Working/Gate0/Gate1/Gate2/Gate3` | 03 vs 00B vs App-A | GOV-001 建立的資料夾結構無法確定，**文件歸檔路徑錯亂**，GOV-005 Document Intake 無法將文件放入正確位置 |
| **RF-FATAL-005** | **7 支 Flow 缺失施工規格**：Doc 05（唯一 Flow 實作權威）僅涵蓋 GOV-001~005 與 GOV-013~019（12 支），**GOV-006~012（7 支）完全無施工說明**。Doc 04 已定義 FORM-006~011 會呼叫這些 Flow | 05 vs 04, 07, App-A | Gate Cancellation、Lite Upgrade、Document Unfreeze、Project Closure、Project Suspension、Gate Rollback、Project Archival **7 大情境無法施工** |
| **RF-FATAL-006** | **Dataverse Web API URI 格式錯誤**：Doc 06 回滾機制使用 `{table-plural-name}` 占位符，但未提供正確的 Dataverse OData 複數名稱對應 | 06 | 自動回滾 HTTP PATCH 請求將回傳 **404 Not Found**，GOV-017 回滾功能全面失效 |

---

### 治理破口（GOV BREACH）— 可能繞過治理閉環

| ID | 問題描述 | 涉及文件 | 影響 |
|----|---------|---------|------|
| **RF-GOV-001** | **Counter List 欄位定義雙源衝突**：Doc 00B 使用 `CounterType/CurrentValue/YearFormat/Separator/Description`；Doc 02 定義為 `CounterName/CurrentYear/CurrentCounter/Prefix/LastUpdated/LastUpdatedBy` | 00B vs 02 | 依 Doc 00B 初始化 Counter List 將寫入不存在的欄位，**GOV-001 首次執行必定失敗** |
| **RF-GOV-002** | **安全群組命名不一致**：Doc 01 定義 `GOV-GovernanceLead`（單數）；Doc 00B 使用 `GOV-GovernanceLeads`（複數）+ `GOV-SystemAdmins`（不存在於 Doc 01）；Doc 00B 漏列 `GOV-EngineeringManagement` | 00B vs 01 | 初始化檢查清單驗證的群組與實際建立的群組不匹配，**初始化驗證假通過** |
| **RF-GOV-003** | **Service Principal 角色名稱衝突**：Doc 00B 使用 `GOV-FlowServiceRole`；Doc 02 使用 `GOV-FlowServicePrincipal` | 00B vs 02 | 角色指派將引用不存在的名稱 |
| **RF-GOV-004** | **Flow ID 重複**：Doc 04 將 FORM-005 對應 `GOV-006-RiskReassessment`，同時將 FORM-006 對應 `GOV-006-GateCancellation`。一個 ID 對兩個不同 Flow | 04 | 無法區分兩支 Flow，建置時 ID 衝突 |
| **RF-GOV-005** | **8 支 Flow-only 欄位未被 GOV-017 監控**：`gov_riskacceptancedate`、`gov_riskowner`、`gov_executiveapprover`、`gov_reworkcount`、`gov_lastreworkdate`、`gov_riskownerreviewstatus`、`gov_executivereviewstatus`、`gov_residualrisklevel` 均不在 Doc 06 的偵測清單中 | 06 vs 02, 05 | 這 8 個欄位可被人為竄改而**不被偵測或回滾** |
| **RF-GOV-006** | **違規升級無自動化**：Doc 06 定義 Level 2（24h）和 Level 3（48h）升級規則，但無對應 Flow（如 GOV-020）實作升級自動化 | 06 | 違規事件可**無限期未處理**而無人被通知 |
| **RF-GOV-007** | **GOV-018 文件連結驗證缺少認證**：HTTP HEAD 請求未附帶 Azure AD 認證 Token，SharePoint 連結會回傳 403 | 06 | 所有文件連結驗證都會回報**假陽性違規** |
| **RF-GOV-008** | **BOM Registry 無寫入路徑**：Doc 02 定義 `gov_bomregistry` 資料表，Doc 07 有 E2E-010~013 BOM 測試案例，但 Doc 05 **無任何 Flow 寫入此表** | 02, 05, 07 | BOM 資料無法透過任何合規路徑建立 |
| **RF-GOV-009** | **OnHold 解鎖機制未定義**：E2E-004 指出 ReworkCount ≥ 3 自動觸發 OnHold，需 Engineering Management 解除，但**無對應 Form/Flow/流程** | 07 | 專案進入 OnHold 後**無合法路徑恢復** |

---

### 稽核斷鏈（AUDIT CHAIN BREAK）— Event append-only 被破壞或版本追溯斷裂

| ID | 問題描述 | 涉及文件 | 影響 |
|----|---------|---------|------|
| **RF-AUDIT-001** | **Doc 02 版本標頭與歷史不符**：標頭宣告 v2.1（2026-02-09），版本歷史僅記錄 v1.0 與 v2.0（均為 2026-01-28），v2.1 無 Changelog | 02 | 無法追溯 v2.0 → v2.1 的變更內容 |
| **RF-AUDIT-002** | **Doc 04 版本標頭與歷史矛盾**：標頭宣告 v6.0，版本歷史實際最新為 v7.1，同一天（2026-02-11）從 v4.0 → v7.1 連續發版 5 次 | 04 | 文件版本不可信，無法進行合規稽核 |
| **RF-AUDIT-003** | **RequestID 格式三方矛盾**：Doc 01 定義 `DR-{YYYY}-{####}`（4 位序號）；Doc 00B 驗證 `DR-2026-{8碼}`（8 位）；Appendix A 使用 `DR-{YYYY}-{ShortGuid}`（GUID） | 01, 00B, App-A | 無法確認 RequestID 的正確格式，**稽核無法驗證 ID 合規性** |

---

### 架構漂移（ARCHITECTURAL DRIFT）— 多份文件宣告不同真相

| ID | 問題描述 | 涉及文件 | 影響 |
|----|---------|---------|------|
| **RF-DRIFT-001** | **Doc 02 Gate 參考指向不存在的檔案**：Line 1735 寫 "禁止進入 `03-Power-Automate-Flows-Implementation.md`"，正確應為 `03-sharepoint-architecture.md` | 02 | 引導錯誤，讀者可能找不到下一份文件 |
| **RF-DRIFT-002** | **Document Register.UploadedBy 型別衝突**：Doc 02 定義為 `Lookup (User)`；Doc 03 描述為 `Text`（Email） | 02 vs 03 | Flow 寫入資料型別不匹配，Lookup 傳 Email 會失敗 |
| **RF-DRIFT-003** | **文件凍結雙重真相來源**：Doc 03 在 Document Register 層級追蹤凍結（IsFrozen/FrozenDate）；Doc 02 在 Project Registry 層級追蹤凍結（gov_documentfreezestatus/gov_documentfreezedate）。兩份文件各自宣告不同的凍結判定來源 | 02 vs 03 | 凍結狀態的 Source of Truth 不明確 |
| **RF-DRIFT-004** | **FORM-004~011 規格嚴重不足**：Doc 04 僅以 1-2 行描述 8 支表單，無欄位定義、無驗證規則、無 Flow 參數對應 | 04 | 8 支表單無法依 SOP 施工 |
| **RF-DRIFT-005** | **GOV-017 偵測時間窗有盲區**：使用 `addHours(utcNow(), -1)` 相對偏移而非 checkpoint 機制，若 Flow 延遲執行則產生偵測缺口 | 06 | 5~60 分鐘偵測盲區 |
| **RF-DRIFT-006** | **System Architect 欄位分類混亂**：Doc 04 同時標記為「使用者輸入」但 DisplayMode.View（不可編輯），又標記為「非 Flow-Only」，且存在 Email string vs User Lookup 型別混淆 | 04 | 開發者無法確定正確的資料傳遞方式 |
| **RF-DRIFT-007** | **Doc 03 DocumentType 與 Doc 02 不完全一致**：Doc 03 新增 `DesignObjectInventory`、`ChangeImpact`、`DocumentRegister` 三個 DocumentType 但 Doc 02 的 `gov_documenttype` Choice 清單中無此三個值 | 03 vs 02 | Document Intake 使用未定義的 DocumentType 值將失敗 |
| **RF-DRIFT-008** | **Approval Record (APR-xxx) 實體未定義**：Doc 07 AC-008 引用 `APR-003`（Layer 3 approval record），但所有文件中無此實體的 Schema 定義 | 07 | 測試案例引用不存在的資料結構 |

---

### 低效與噪音問題（LOW）

| ID | 問題描述 | 涉及文件 |
|----|---------|---------|
| RF-LOW-001 | Scheduled Flows 時區硬編碼為 UTC+8，不適用多區域部署 | 06 |
| RF-LOW-002 | Teams 通知 Channel 占位符（TODO-004）未解析 | 06, 00C |
| RF-LOW-003 | Application Insights Instrumentation Key 為 TODO 狀態 | 07 |
| RF-LOW-004 | 測試資料清理腳本僅涵蓋 2/8 資料表 | 07 |
| RF-LOW-005 | Gate 下拉選單無 fallback（Switch 回傳空陣列無錯誤提示）| 04 |
| RF-LOW-006 | Doc 04 同日發版 5 次（v4.0→v7.1），無正式 Release Cycle | 04 |

---

## C. 權威宣告衝突摘要

以下為多份文件同時宣告自己為真相來源但內容矛盾之情境：

| 衝突主題 | 文件 A 宣告 | 文件 B 宣告 | 裁決建議 |
|---------|------------|------------|---------|
| SharePoint 網站權限 | Doc 01：Architects=Edit, GovLead=Full | Doc 03：所有人類=Read | **Doc 03 為 SharePoint 權威，採信 Doc 03** |
| 資料夾結構 | Doc 03：以文件類型命名（01_Feasibility…） | App-A/00B：以 Gate 命名（Gate0, Gate1…） | **Doc 03 為 SharePoint 權威，採信 Doc 03** |
| Counter List 欄位 | Doc 02：CounterName/CurrentYear/CurrentCounter | Doc 00B：CounterType/CurrentValue | **Doc 02 為資料模型權威，採信 Doc 02** |
| 文件凍結位置 | Doc 02：Project Registry 層級 | Doc 03：Document Register 層級 | **需統一，建議兩層皆追蹤（見 Phase 3）** |
| Schema 前綴 | Doc 06：`cr_` 前綴 | Doc 02/05：`gov_` 前綴 | **Doc 02 為資料模型權威，Doc 06 必須修正為 `gov_`** |
| Flow 實作範圍 | Doc 05：12 支 Flow | App-A/04/07：19 支 Flow | **Doc 05 缺 7 支，需補齊** |

---

## D. 統計摘要

| 嚴重度分類 | 數量 | 可建置阻斷 |
|-----------|:----:|:---------:|
| 致命錯位（FATAL） | 6 | 是 |
| 治理破口（GOV BREACH） | 9 | 部分 |
| 稽核斷鏈（AUDIT CHAIN） | 3 | 否（但稽核不過）|
| 架構漂移（DRIFT） | 8 | 部分 |
| 低效與噪音（LOW） | 6 | 否 |
| **總計** | **32** | — |

---

## E. PHASE 1 結論

**當前文件集無法直接用於建置部署。**

存在 6 個致命錯位，任一個都會導致系統核心功能失效：
1. Guardrail Monitor 因 Schema 前綴錯誤而完全失效
2. SharePoint 權限可能允許人類直接寫入
3. Document Freeze 缺欄位無法執行
4. 資料夾結構三方矛盾
5. 7 支 Flow 無施工規格
6. 自動回滾 API 路徑錯誤

**下一步**：進入 PHASE 2 建構完整情境一致性矩陣，確認所有情境的端到端路徑。

---

**報告結束**
