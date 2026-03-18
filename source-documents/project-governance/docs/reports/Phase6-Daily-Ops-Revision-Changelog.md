# PHASE 6：日常流程導向修訂報告（Daily Ops Revision Changelog v1.0）

**產出日期**：2026-02-11
**執行者**：日常流程導向鑑識與修訂總工程師
**修訂範圍**：8 大目標 — Document Register Baseline Seeding、GOV-005 Base64 Upload Redesign、Deliverable Packages、Version Progression、Link Update Rules、Cross-Document Consistency、Operational Visibility、Test Manual Updates

---

## 修訂摘要

| 項目 | 數值 |
|------|------|
| 總修訂項目 | 42 |
| 涉及文件數 | 8 |
| 新增 Choice Set | 2（gov_documentrole, gov_deliverablepackage） |
| 新增 Dataverse 欄位 | 7（4 Link + 3 DocumentRegister） |
| 新增 E2E 測試案例 | 5（E2E-014 ~ E2E-018） |
| 新增 Anti-Drift 規則 | 5（ADR-007 ~ ADR-010, ADR-A06） |
| Flow 重寫 | 2（GOV-001 擴充, GOV-005 完整重寫） |

---

## 各文件修訂明細

### Doc 02：02-dataverse-data-model-and-security.md（v2.2 → v2.3）

| # | 修訂內容 | 目標對應 | 影響範圍 |
|:-:|---------|---------|---------|
| 1 | gov_projectregistry 新增 4 個 Link 欄位：gov_requirementtraceabilitylink, gov_designobjectinventorylink, gov_documentregisterlink, gov_changeimpactlink | 目標 5 | Doc 05 GOV-005 Link 回寫 |
| 2 | gov_documentregister 新增 3 個欄位：gov_documentrole (Choice), gov_deliverablepackage (Choice), gov_supersededby (Lookup) | 目標 3, 4 | Doc 05 GOV-005, Doc 07 E2E-015/016 |
| 3 | 新增 gov_documentrole 選項集（6 值：Planned/Draft/Active/Superseded/Approved/Frozen） | 目標 4 | Doc 05 GOV-001/005, Doc 07 |
| 4 | 新增 gov_deliverablepackage 選項集（3 值：CoreDeliverable/SupplementaryDeliverable/AdHoc） | 目標 3 | Doc 04 FORM-003, Doc 05 GOV-001/005 |
| 5 | 新增 Document Baseline Matrix 章節 — 16 列映射表（DocumentType→RequiredForGate→SharePointFolder→ProjectRegistryLinkField→DefaultDeliverablePackage） | 目標 1, 6 | Doc 03, 05, Appendix A（皆引用此矩陣） |
| 6 | Flow-only 欄位清單更新：gov_documentregister 新增 gov_documentrole, gov_supersededby | 目標 4 | Doc 06 GOV-017 監控 |
| 7 | Data Model Ready Gate 檢查清單更新：選項集 20→22、新增 Baseline Matrix 驗證區塊（4 項）、總計 25→29 項 | 目標 6 | 部署前驗證 |
| 8 | 版本歷史新增 v2.3 條目 | - | - |
| 9 | 完成摘要更新：反映新增內容 | - | - |

---

### Doc 03：03-sharepoint-architecture.md（v2.1 → v2.2）

| # | 修訂內容 | 目標對應 | 影響範圍 |
|:-:|---------|---------|---------|
| 1 | DocumentType→Folder 對應表修正 4 處：RiskAssessmentStrategy→01_Feasibility, ThreatModel→04_Security, ChangeImpact→03_Design, DocumentRegister→06_Handover | 目標 6 | 對齊 Doc 02 Baseline Matrix |
| 2 | 對應表新增 TestPlan, Other 兩列 | 目標 6 | 完整覆蓋所有 16 個 DocumentType |
| 3 | 對應表標註 Doc 02 Baseline Matrix 為唯一權威來源 | 目標 6 | ADR-A06 防漂移 |
| 4 | Document Register 欄位表新增 3 欄位（gov_documentrole, gov_deliverablepackage, gov_supersededby） | 目標 3, 4 | 與 Doc 02 一致 |
| 5 | GOV-005 連結建立流程完整重寫：Base64 上傳模式 + 版本推進 + Link 目標規則 | 目標 2, 4, 5 | 與 Doc 05 GOV-005 一致 |
| 6 | 版本歷史新增 v2.2 條目 | - | - |

---

### Doc 04：04-powerapps-forms.md（v7.2 → v7.3）

| # | 修訂內容 | 目標對應 | 影響範圍 |
|:-:|---------|---------|---------|
| 1 | FORM-003 移除 txtS3_SharePointLink 控制項 | 目標 2 | 使用者不再需要手動貼 Link |
| 2 | FORM-003 新增 attS3_FileUpload（Attachment 控制項，Base64 傳至 Flow） | 目標 2 | GOV-005 接收 Base64 |
| 3 | FORM-003 新增 ddS3_DeliverablePackage 下拉選單 | 目標 3 | GOV-005 接收 DeliverablePackage |
| 4 | FORM-003 新增完整檔案上傳 JSON Schema（提交至 Flow 的 payload） | 目標 2 | 完整 Input/Output 定義 |
| 5 | 文件類型選項新增 TestPlan, Other | 目標 6 | 覆蓋所有 DocumentType |
| 6 | 版本歷史新增 v7.3 條目 | - | - |

---

### Doc 05：05-core-flows-implementation-runbook.md（v2.0 → v2.1）

| # | 修訂內容 | 目標對應 | 影響範圍 |
|:-:|---------|---------|---------|
| 1 | GOV-001 SharePoint Output 子資料夾修正：Gate0/Gate1/Gate2/Gate3/_Working → 01_Feasibility/02_Risk_Assessment/03_Design/04_Security/05_Test/06_Handover | 目標 6 | 對齊 Doc 03 |
| 2 | GOV-001 步驟 7 子資料夾建立修正（5→6 個子資料夾） | 目標 6 | 同上 |
| 3 | GOV-001 新增步驟 7.5 Baseline Seeding：遍歷 13 個 DocumentType 建立 Planned 記錄 | 目標 1 | E2E-014 |
| 4 | GOV-001 驗收測試新增 Baseline Seeding 驗證行 | 目標 1 | Doc 07 E2E-014 |
| 5 | GOV-005 完整重寫：名稱改為 Document Upload and Register | 目標 2 | 全文件鏈 |
| 6 | GOV-005 觸發來源修正：FORM-005→FORM-003 | 目標 6 | 消除映射矛盾 |
| 7 | GOV-005 新增完整 Input Schema（Base64 模式，含 DeliverablePackage） | 目標 2, 3 | Doc 04 FORM-003 |
| 8 | GOV-005 新增 Pre-check ERR-005-005（檔案內容空白）、ERR-005-006（DocumentType 無效） | 目標 2 | 錯誤處理 |
| 9 | GOV-005 DocumentType→Folder 對應表改為引用 Doc 02 Baseline Matrix | 目標 6 | ADR-A06 防漂移 |
| 10 | GOV-005 新增步驟 3（SharePointFolder 解析）、步驟 4（SharePoint 上傳）、步驟 5（版本推進）、步驟 6（建立/更新 Document Register）、步驟 7（Link 回寫） | 目標 2, 4, 5 | 核心邏輯 |
| 11 | GOV-005 新增完整驗收測試表（5 項） | 目標 8 | Doc 07 |
| 12 | DEV 完成定義：GOV-005 測試更新為 Base64 模式 | 目標 8 | - |

---

### Appendix A：A-core-flows-specification.md（v1.0 → v1.1）

| # | 修訂內容 | 目標對應 | 影響範圍 |
|:-:|---------|---------|---------|
| 1 | GOV-001 Step 4 子資料夾名稱修正（Gate→Topic-based） | 目標 6 | 與 Doc 05 一致 |
| 2 | GOV-001 新增 Step 5 Baseline Seeding 規格 | 目標 1 | 設計規格完整 |
| 3 | GOV-005 完整重寫：標題、Trigger、Input Schema、Pre-conditions、Main Steps、DocumentType 對應表 | 目標 2, 3, 4, 5 | 設計規格完整 |
| 4 | GOV-005 冪等性策略改為版本推進（Version Progression） | 目標 4 | 設計語意 |
| 5 | 新增 ERR-005-005, ERR-005-006 錯誤碼 | 目標 2 | 錯誤碼總表 |
| 6 | 版本歷史新增 v1.1 條目 | - | - |

---

### Doc 07：07-testing-and-acceptance.md（v1.2 → v1.3）

| # | 修訂內容 | 目標對應 | 影響範圍 |
|:-:|---------|---------|---------|
| 1 | 新增 E2E-014：Baseline Seeding 驗證（13 筆 Planned 記錄） | 目標 1, 8 | GOV-001 |
| 2 | 新增 E2E-015：Draft 版本推進驗證（Planned→Draft、Draft→Superseded 鏈） | 目標 4, 8 | GOV-005 |
| 3 | 新增 E2E-016：Superseded 不可逆驗證（Flow-only 保護、Approved 優先） | 目標 4, 8 | GOV-017 |
| 4 | 新增 E2E-017：Link 目標規則驗證（Approved > Draft） | 目標 5, 8 | GOV-005 |
| 5 | 新增 E2E-018：Deliverable Package 初始化驗證 | 目標 3, 8 | GOV-001/005 |
| 6 | E2E 完成定義清單新增 5 項 | 目標 8 | 上線驗收 |
| 7 | 版本歷史新增 v1.3 條目 | - | - |

---

### Phase 5：Phase5-Release-Gate-and-Anti-Drift.md（v1.0 → v1.1）

| # | 修訂內容 | 目標對應 | 影響範圍 |
|:-:|---------|---------|---------|
| 1 | A-1 Dataverse 驗證新增 3 項（A-1.7~A-1.9）：DocumentRegister 新欄位、ProjectRegistry Link 欄位、Baseline Matrix 存在性 | 目標 6 | Release Gate |
| 2 | A-5 測試覆蓋率新增 3 項（A-5.4~A-5.6）：E2E-014/015/016/017 存在性 | 目標 8 | Release Gate |
| 3 | Release Gate 總計更新：22→28 項 | - | 部署前驗證 |
| 4 | 新增 4 條 Anti-Drift 規則（ADR-007~ADR-010）：Baseline Matrix 單一修改點、Baseline Seeding 同步、Version Progression 不可繞過、Link 回寫依據 Baseline Matrix | 目標 6 | 日常維護 |
| 5 | 新增 1 條權威文件規則（ADR-A06）：Baseline Matrix 為唯一權威 | 目標 6 | 日常維護 |

---

## 修訂後文件版本對照

| 文件 | 修訂前版本 | 修訂後版本 | 修補數 |
|------|-----------|-----------|:------:|
| 02-dataverse-data-model-and-security.md | v2.2 | **v2.3** | 9 |
| 03-sharepoint-architecture.md | v2.1 | **v2.2** | 6 |
| 04-powerapps-forms.md | v7.2 | **v7.3** | 6 |
| 05-core-flows-implementation-runbook.md | v2.0 | **v2.1** | 12 |
| appendix/A-core-flows-specification.md | v1.0 | **v1.1** | 6 |
| 07-testing-and-acceptance.md | v1.2 | **v1.3** | 7 |
| Phase5-Release-Gate-and-Anti-Drift.md | v1.0 | **v1.1** | 5 |

---

## Consistency Checklist — 8 大目標達成狀態

### 目標 1：Document Register Baseline Seeding

| 檢查項目 | 達成 | 位置 |
|---------|:----:|------|
| GOV-001 建立專案時自動產生 Planned 記錄 | ✅ | Doc 05 步驟 7.5 |
| Baseline Matrix 定義所有 RequiredForGate 文件類型 | ✅ | Doc 02 Baseline Matrix（13 筆 RequiredForGate ≠ '-'） |
| 每筆 Planned 記錄含 DocumentRole = Planned | ✅ | Doc 05 步驟 7.5 欄位對應 |
| 每筆 Planned 記錄含 DeliverablePackage = CoreDeliverable | ✅ | Doc 05 步驟 7.5 欄位對應 |
| 測試案例存在 | ✅ | Doc 07 E2E-014 |

### 目標 2：GOV-005 Base64 Upload Redesign

| 檢查項目 | 達成 | 位置 |
|---------|:----:|------|
| FORM-003 提供 Attachment 控制項（非 SharePoint Link） | ✅ | Doc 04 FORM-003 attS3_FileUpload |
| GOV-005 接收 Base64 FileContent | ✅ | Doc 05 GOV-005 Input Schema |
| GOV-005 上傳至 SharePoint 並回寫 URL | ✅ | Doc 05 GOV-005 步驟 4 + 7 |
| Pre-check 包含 FileContent 非空白驗證 | ✅ | Doc 05 GOV-005 ERR-005-005 |
| Appendix A 設計規格一致 | ✅ | Appendix A GOV-005 |

### 目標 3：Deliverable Packages

| 檢查項目 | 達成 | 位置 |
|---------|:----:|------|
| gov_deliverablepackage Choice 已定義（3 值） | ✅ | Doc 02 第 5 章 |
| gov_documentregister 包含 gov_deliverablepackage 欄位 | ✅ | Doc 02 第 4 章 |
| FORM-003 提供 DeliverablePackage 下拉選單 | ✅ | Doc 04 FORM-003 ddS3_DeliverablePackage |
| Baseline Seeding 預設 CoreDeliverable | ✅ | Doc 05 步驟 7.5 + Doc 02 Baseline Matrix DefaultDeliverablePackage |
| 測試案例存在 | ✅ | Doc 07 E2E-018 |

### 目標 4：Version Progression Strategy

| 檢查項目 | 達成 | 位置 |
|---------|:----:|------|
| gov_documentrole Choice 已定義（6 值） | ✅ | Doc 02 第 5 章 |
| gov_supersededby Lookup 已定義 | ✅ | Doc 02 第 4 章 gov_documentregister |
| GOV-005 執行版本推進（Draft→Superseded 鏈） | ✅ | Doc 05 GOV-005 步驟 5 |
| Planned→Draft 轉換（首次上傳） | ✅ | Doc 05 GOV-005 步驟 6 |
| SupersededBy 回填 | ✅ | Doc 05 GOV-005 步驟 5+6 |
| gov_documentrole, gov_supersededby 為 Flow-only | ✅ | Doc 02 第 7 章 |
| 測試案例存在 | ✅ | Doc 07 E2E-015, E2E-016 |

### 目標 5：Project Registry Link Update Rules

| 檢查項目 | 達成 | 位置 |
|---------|:----:|------|
| Baseline Matrix 定義 ProjectRegistryLinkField | ✅ | Doc 02 Baseline Matrix |
| GOV-005 實作 Link 目標規則（Approved > Draft） | ✅ | Doc 05 GOV-005 步驟 7 |
| 15 個 Link 欄位存在於 gov_projectregistry | ✅ | Doc 02 第 4 章（11 原有 + 4 新增） |
| 測試案例存在 | ✅ | Doc 07 E2E-017 |

### 目標 6：Cross-Document Consistency

| 檢查項目 | 達成 | 位置 |
|---------|:----:|------|
| SharePoint 子資料夾名稱一致（Doc 03 = Doc 05 = Appendix A = Doc 00B） | ✅ | 全部統一為 01_Feasibility ~ 06_Handover |
| DocumentType→Folder 映射一致（Doc 02 = Doc 03 = Doc 05 = Appendix A） | ✅ | 以 Doc 02 Baseline Matrix 為唯一權威，其餘引用 |
| GOV-005 觸發來源一致（Doc 04 FORM-003 = Doc 05 GOV-005 = Appendix A） | ✅ | 全部統一為 FORM-003 |
| DocumentType 選項完整覆蓋（16 值） | ✅ | Doc 02/03/04/05/Appendix A 全部包含 TestPlan, Other |
| 防漂移規則已建立 | ✅ | Phase 5 ADR-007~ADR-010, ADR-A06 |

### 目標 7：Operational Visibility（最低可用 View/Dashboard 規格）

| 檢查項目 | 達成 | 位置 |
|---------|:----:|------|
| Document Baseline Matrix 提供完整映射視圖 | ✅ | Doc 02 Baseline Matrix 章節 |
| 版本推進鏈可透過 SupersededBy 追溯 | ✅ | Doc 02 gov_supersededby 說明 |
| Planned 記錄可識別尚未上傳的必要文件 | ✅ | DocumentRole = Planned 且 SharePointFileLink 空白 |

> **注意**：本輪不實作 BI Dashboard。上述規格為最低可用的「查詢式」可見度。正式 Dashboard 需另案。

### 目標 8：Test Manual Updates

| 檢查項目 | 達成 | 位置 |
|---------|:----:|------|
| E2E-014 Baseline Seeding 測試 | ✅ | Doc 07 |
| E2E-015 Draft 版本推進測試 | ✅ | Doc 07 |
| E2E-016 Superseded 不可逆測試 | ✅ | Doc 07 |
| E2E-017 Link 目標規則測試 | ✅ | Doc 07 |
| E2E-018 Deliverable Package 初始化測試 | ✅ | Doc 07 |
| E2E 完成定義清單已更新 | ✅ | Doc 07 |

---

## 總結

| 指標 | 值 |
|------|---|
| 8 大目標 | **全部達成** |
| 修訂文件數 | 8 |
| 新增結構（Choice Set, 欄位, 測試案例, ADR 規則） | 2 + 7 + 5 + 5 = **19 項** |
| Flow 重寫 | 2（GOV-001 擴充 + GOV-005 完整重寫） |
| 跨文件矛盾消除 | 4 處（子資料夾、DocumentType 映射、觸發來源、TestPlan/Other 缺失） |
| 單一權威來源建立 | Doc 02 Document Baseline Matrix |

---

**PHASE 6 完成。日常流程導向鑑識與修訂任務結束。**
