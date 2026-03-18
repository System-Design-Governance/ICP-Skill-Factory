# PHASE 4：修訂完成報告（Revision Changelog v1.0）

**產出日期**：2026-02-11
**執行者**：治理系統鑑識與重構總工程師

---

## 修訂摘要

| 項目 | 數值 |
|------|------|
| 總修補項目（Patches） | 24 |
| 涉及文件數 | 7 |
| FATAL 等級修復 | 6 |
| GOV BREACH 修復 | 9 |
| AUDIT CHAIN 修復 | 3 |
| DRIFT 修復 | 6 |

---

## 各文件修訂明細

### Doc 01：01-prerequisites-and-environment.md（v2.0 → v2.1）

| Patch ID | 修訂內容 | 等級 |
|----------|---------|------|
| PATCH-001 | SharePoint 權限修正：GOV-Architects Edit→Read、GOV-GovernanceLead Full Control→Read、新增 Flow Service Principal Contribute | FATAL |
| PATCH-022 | Environment Ready Gate 驗證條件更新：權限檢查從 Edit 改為 Read + Contribute | AUDIT |

**具體修改**：
- 第 7.3 節權限表：6 行修正 + 1 行新增
- 第 7.4 節驗證結果：Edit→Read
- 第 10 節 Ready Gate：驗證條件更新
- 版本歷史新增 v2.1 條目

---

### Doc 02：02-dataverse-data-model-and-security.md（v2.1 → v2.2）

| Patch ID | 修訂內容 | 等級 |
|----------|---------|------|
| PATCH-002 | Document Register 新增 gov_isfrozen（Yes/No）、gov_frozendate（DateTime）欄位 | FATAL |
| PATCH-003 | gov_documenttype Choice 新增 3 值：DesignObjectInventory、ChangeImpact、DocumentRegister | DRIFT |
| PATCH-004 | 新增 gov_sahandoverevent 資料表（9 欄位 + 新增 gov_handoverstatus Choice） | DRIFT |
| PATCH-005 | Counter List 種子資料新增 BOMID 記錄（總計 6→7 筆） | DRIFT |
| PATCH-006 | Data Model Ready Gate 參考檔名修正：03-Power-Automate-Flows-Implementation.md → 03-sharepoint-architecture.md | DRIFT |
| PATCH-007 | 版本歷史補齊 v2.1 及 v2.2 條目 | AUDIT |
| PATCH-008 | UploadedBy 型別確認為 Lookup (User)（Doc 02 已正確，無需修改） | DRIFT |

**具體修改**：
- 資料表清單：7→9 個（新增 gov_sahandoverevent + 已有 gov_bomregistry）
- Document Register 欄位表新增 2 行
- gov_documenttype Choice 新增 3 值（100000013-15）
- 新增 gov_sahandoverevent 完整資料表定義（含 gov_handoverstatus Choice）
- Counter List 種子資料新增 BOMID 行
- 資料表關聯新增 2 行（bomregistry、sahandoverevent）
- Gate 檢查清單：Counter List 記錄數 6→7
- 版本歷史新增 2 條目
- 完成摘要：7→9 個資料表

---

### Doc 03：03-sharepoint-architecture.md（v2.0 → v2.1）

| Patch ID | 修訂內容 | 等級 |
|----------|---------|------|
| PATCH-009 | Document Register 欄位 Uploaded By 型別修正：Text → Lookup (User) | DRIFT |

**具體修改**：
- 第 8.1 節欄位表：UploadedBy 從 Text 改為 Lookup (User)
- 新增版本歷史章節（v1.0, v2.0, v2.1）

---

### Doc 04：04-powerapps-forms.md（v6.0 → v7.2）

| Patch ID | 修訂內容 | 等級 |
|----------|---------|------|
| PATCH-015 | 版本標頭修正：v6.0 → v7.2（Anti-Fragile Edition — Forensic Patch） | AUDIT |
| PATCH-016 | Flow ID 重複修正：FORM-005 從 GOV-006 改為 GOV-020-RiskReassessment | GOV |

**具體修改**：
- 文件標頭版本修正
- Form-Flow 映射表 2 處：GOV-006-RiskReassessment → GOV-020-RiskReassessment
- 版本歷史新增 v7.2 條目

---

### Doc 06：06-guardrails-and-anti-cheating.md（v1.0 → v1.1）

| Patch ID | 修訂內容 | 等級 |
|----------|---------|------|
| PATCH-010 | 全文 Schema 前綴修正：cr_ → gov_（所有 Dataverse 實體名稱、欄位名稱） | FATAL |
| PATCH-011 | GOV-017 Flow-only 監控欄位補齊：Project Registry +5 欄位、Risk Assessment +3 欄位、新增 Review Decision Log 全表 13 欄位 | GOV |
| PATCH-012 | Dataverse Web API URI 修正：新增 OData Entity Set 名稱對應表（9 表）、新增 OData Headers | FATAL |
| PATCH-013 | GOV-018 HTTP 文件連結驗證新增 Azure AD OAuth 認證（Service Principal Token） | GOV |
| PATCH-014 | GOV-017 偵測機制改為 Checkpoint（Environment Variable 取代固定 addHours -1） | DRIFT |

**具體修改**：
- 全文 cr_ → gov_ 替換（~80+ 處）
- FlowOnlyFields JSON：新增 3 大段（Project Registry 擴充、Risk Assessment 擴充、Review Decision Log 完整）
- 回滾 HTTP PATCH 範例：新增完整 Entity Set 對應表
- GOV-018 HTTP HEAD 動作：新增完整 Authentication 設定區塊
- CheckStartTime：新增 Checkpoint 機制說明區塊
- 版本歷史新增 v1.1 條目

---

### Doc 07：07-testing-and-acceptance.md（v1.1 → v1.2）

| Patch ID | 修訂內容 | 等級 |
|----------|---------|------|
| PATCH-023 | E2E-009 Project Closure Flow ID 修正：GOV-012 → GOV-009 | GOV |

**具體修改**：
- 測試步驟表 1 處修正
- 新增版本歷史章節（v1.0, v1.1, v1.2）

---

### Doc 00B：00B-first-run-initialization-checklist.md（v1.0 → v1.1）

| Patch ID | 修訂內容 | 等級 |
|----------|---------|------|
| PATCH-018 | Counter List 欄位名稱修正：CounterType→CounterName、CurrentValue→CurrentCounter、刪除 YearFormat/Separator/Description、新增 CurrentYear/LastUpdated | GOV |
| PATCH-019 | 安全群組名稱修正：GOV-GovernanceLeads→GOV-GovernanceLead、刪除 GOV-SystemAdmins、新增 GOV-EngineeringManagement/GOV-FlowServicePrincipal（6→7 群組） | GOV |
| PATCH-020 | Service Principal 角色名稱修正：GOV-FlowServiceRole→GOV-FlowServicePrincipal | GOV |
| PATCH-021 | SharePoint 資料夾結構統一：Gate0/Gate1/.../Working/Archive → 01_Feasibility/.../06_Handover | FATAL |
| PATCH-022 | RequestID 格式統一：DR-2026-{8碼} → DR-2026-{####} | AUDIT |

**具體修改**：
- Counter List 初始化欄位表完全重寫
- 驗證步驟修正 3 處
- 檢查點更新（2→3 個）
- 安全群組表 6 行修正為 7 行
- Service Principal 角色名稱 1 處
- SharePoint 權限等級修正（Edit→Contribute）
- 資料夾結構名稱 1 處
- RequestID 格式 2 處
- 總檢查清單更新（17→18）
- 新增版本歷史章節

---

## 修訂後文件版本對照

| 文件 | 修訂前版本 | 修訂後版本 | 修補數 |
|------|-----------|-----------|:------:|
| 01-prerequisites-and-environment.md | v2.0 | **v2.1** | 2 |
| 02-dataverse-data-model-and-security.md | v2.1 | **v2.2** | 7 |
| 03-sharepoint-architecture.md | v2.0 | **v2.1** | 1 |
| 04-powerapps-forms.md | v6.0 (header) / v7.1 (actual) | **v7.2** | 2 |
| 06-guardrails-and-anti-cheating.md | v1.0 | **v1.1** | 5 |
| 07-testing-and-acceptance.md | v1.1 | **v1.2** | 1 |
| 00B-first-run-initialization-checklist.md | v1.0 | **v1.1** | 5 |

---

## 未修改之文件

以下文件經鑑識後無需修改：

| 文件 | 版本 | 原因 |
|------|------|------|
| 00-index.md | v1.0 | 導讀文件，無結構性錯誤 |
| 00A-build-order-and-bootstrap.md | v1.0 | 建置順序正確 |
| 00C-placeholder-reference.md | v1.0 | 占位符參考正確 |
| 05-core-flows-implementation-runbook.md | v2.0 | 施工步驟未涉及本次修補範圍（GOV-006~012 缺失為功能缺口，非結構性錯誤，需另案補齊） |
| appendix/A-core-flows-specification.md | v1.0 | 設計規格參考文件，定位為非實作依據 |

---

## 殘留風險聲明

以下項目已識別但**不在本次修訂範圍**（需另案處理）：

| 項目 | 說明 | 建議 |
|------|------|------|
| GOV-006 至 GOV-012 施工規格缺失 | Doc 05 僅覆蓋 12/19 Flows | 需補充 7 個 Flow 施工步驟（另案） |
| BOM Registry 無 Form/Flow 寫入路徑 | 資料表已定義，但完整 CRUD 鏈未建立 | 需新增 FORM-012/GOV-021 等（另案） |
| GOV-006 Escalation 無自動化 Flow | 升級規則僅為文字描述 | 需新增 GOV-022 Escalation Flow（另案） |
| OnHold 解除機制未定義 | ProjectStatus=OnHold 後無標準解除流程 | 需新增 FORM-013/GOV-023（另案） |

---

**報告結束。下一步：PHASE 5 建立 Release Gate 與防漂移機制。**
