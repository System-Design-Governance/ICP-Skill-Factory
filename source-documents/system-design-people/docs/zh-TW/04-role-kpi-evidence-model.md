# 角色 KPI 與證據模型

## Role-Based KPI and Evidence Model

**文件編號：** GOV-02-002
**文件版本：** 1.1
**生效日期：** 2026-02-09
**文件層級：** 角色治理文件
**依據文件：** GOV-02-001 角色定義與職責說明

---

## 文件目的

本文件從各角色之**當責（Accountabilities）**推導可觀測之 KPI，並定義客觀之證據來源，使管理層能夠在不依賴主觀判斷之情況下評估角色績效。

本文件**非**目標設定文件，而是**治理可觀測性設計（Governance Observability Design）**文件。

---

## 推導原則

| 原則 | 說明 |
|-----|------|
| KPI 僅從當責推導 | KPI 須對應角色之當責，非職責或活動 |
| 證據強制對應 | 每個 KPI 須對應至少一個可審查、可稽核、可重現之證據來源 |
| 避免主觀指標 | 不使用努力程度、投入時間或活動數量作為 KPI |
| 設計時權限範圍 | KPI 反映設計時權限，不涉及執行結果 |
| 門檻保留 | 除邏輯上無法避免者外，不指定數值目標 |

---

## Head of System Design KPI 與證據

### KPI 類別

1. Standard System Integrity（標準體系完整性）
2. Exception Governance Quality（例外治理品質）
3. Gate Decision Quality（Gate 決策品質）
4. Dispute Resolution Effectiveness（爭議解決有效性）
5. Technical Direction Coherence（技術方向一致性）

### KPI 明細

| KPI | 定義 | 合規條件 | 證據來源 |
|:-----------------------|:------------------------|:------------------|:------------------------|
| Standard System Completeness | 所有宣稱擁有之標準皆已正式定義、發布並納入版本控制 | 所有標準皆有對應文件且具備必要元資料 | 標準清冊、各標準文件元資料頁、版本控制紀錄 |
| Standard Coherence | 所有標準間無衝突、無重疊定義 | 無標準間衝突之正式回報 | 標準回饋紀錄、例外申請紀錄 |
| Exception Ruling Traceability | 所有例外裁決紀錄皆具備必要欄位 | 所有欄位皆完整填寫 | 例外裁決紀錄、例外清冊 |
| Gate 0/Gate 2 Decision Documentation | 所有決策皆有可追溯之紀錄 | 每個決策皆有核准紀錄 | Gate 0/Gate 2 核准紀錄、Gate 審查紀錄 |
| Level 3 Dispute Resolution Closure | 所有 Level 3 爭議皆經正式裁決並結案 | 所有爭議皆有裁決紀錄 | Level 3 爭議裁決紀錄、爭議清單 |
| SL Decision Record Approval Completeness | 所有 SL Decision Record 皆經正式核准 | 所有 SL Decision Record 皆有核准簽核 | SL Decision Record、Gate 審查紀錄 |

---

## System Design Governance Lead KPI 與證據

### KPI 類別

1. Governance Framework Currency（治理框架時效性）
2. Gate Execution Consistency（Gate 執行一致性）
3. Compliance Verification Coverage（合規驗證覆蓋度）
4. Dispute Resolution Timeliness（爭議解決時效）
5. Interface Compatibility Assurance（介面相容性保證）

### KPI 明細

| KPI | 定義 | 合規條件 | 證據來源 |
|:-----------------------|:------------------------|:------------------|:------------------------|
| Governance Framework Currency | 治理框架標準具備年度審查紀錄 | 所有文件未超過 12 個月未審查 | 主文件及附錄審查紀錄、年度審查會議紀錄 |
| Gate Review Record Completeness | 所有 Gate 1/3 審查皆有完整紀錄 | 紀錄包含所有必要欄位 | Gate 1/3 審查紀錄、簽核紀錄 |
| Standard Compliance Verification Coverage | 所有受治理專案皆經合規驗證 | 所有專案皆有驗證紀錄 | 合規驗證紀錄、受治理專案清單 |
| Level 2 Dispute Resolution Timeliness | Level 2 爭議於 5 個工作日內仲裁 | 仲裁日期與提出日期間隔 ≤ 5 個工作日 | Level 2 爭議仲裁紀錄、爭議清單 |
| External Unit Compatibility Assessment Completion | 所有外部單位皆經相容性評估 | 所有單位皆有評估紀錄 | 外部單位相容性評估紀錄、外部單位清單 |
| Handover Record Integrity | 所有 Gate 3 交接皆有完整紀錄 | 紀錄包含交接事項、簽核、確認聲明 | 交接會議紀錄、Gate 3 審查紀錄 |

---

## System Architect KPI 與證據

### KPI 類別

1. Architecture Standard Quality（架構標準品質）
2. Technical Baseline Currency（技術基線時效性）
3. Design Document Integrity（設計文件完整性）
4. Technical Feasibility Assessment Coverage（技術可行性評估覆蓋度）
5. Design Defect Containment（設計缺陷攔截）

### KPI 明細

| KPI | 定義 | 合規條件 | 證據來源 |
|:-----------------------|:------------------------|:------------------|:------------------------|
| Architecture Standard Executability | 標準條款皆可被具體執行 | 年度內無「無法執行」之正式回報 | 標準回饋紀錄、例外申請紀錄 |
| Technical Baseline Document Currency | 技術基線標準文件於規定週期內審查 | 未超過審查週期 | 技術基線標準文件、版本控制紀錄 |
| Design Baseline Completeness | 所有 Gate 1 通過專案具備完整設計基線（含 EBOM） | 文件集符合完整性要求且 EBOM 已納入基線 | 設計基線文件集、Engineering BOM (EBOM)、Gate 1 審查紀錄 |
| Technical Feasibility Assessment Traceability | 所有 Gate 0 核准專案皆有評估紀錄 | 每專案皆有評估紀錄 | 技術可行性評估紀錄、Gate 0 核准紀錄 |
| Design Change Impact Analysis Coverage | 所有 Gate 2 變更皆有影響分析 | 每變更皆有分析文件 | 影響分析文件、設計變更紀錄 |
| Final Design Package Completeness | 所有 Gate 3 文件包皆通過交付檢查 | 通過 12 項檢查 | 最終設計文件包、設計交付檢查表 |

---

## Security Engineering Role KPI 與證據

### KPI 類別

1. Security Standard Quality（安全標準品質）
2. Risk Assessment Standard Quality（風險評估標準品質）
3. Threat Analysis Completeness（威脅分析完整性）
4. IEC 62443 Compliance Verification（IEC 62443 合規驗證）
5. Residual Risk Traceability（殘餘風險可追溯性）

### KPI 明細

| KPI | 定義 | 合規條件 | 證據來源 |
|:-----------------------|:------------------------|:------------------|:------------------------|
| Security Standard Executability | 安全標準條款皆可被具體執行 | 年度內無「無法執行」之正式回報 | 標準回饋紀錄、例外申請紀錄 |
| Risk Assessment Template Usability | 風險評估範本可直接使用 | 年度內無「無法使用」之正式回報 | 標準回饋紀錄、範本修訂紀錄 |
| Threat Scenario Coverage | 威脅情境分析涵蓋 IEC 62443-3-2 要求類別 | 所有報告皆包含完整分析 | 整合式風險評估報告、Zone & Conduit 分析工作表 |
| SR Checklist Traceability | 「Implemented」項目皆有對應證據引用 | 證據引用有效 | SR 檢查表、被引用之設計證據文件 |
| SL Alignment Verification at Each Gate | SL Decision Record 於各 Gate 皆有更新 | 各 Gate 皆有更新/確認紀錄 | SL Decision Record、Gate 審查紀錄 |
| Residual Risk Source Traceability | 殘餘風險皆可追溯至有效來源 ID | ID 可於分析工作表中查得 | 殘餘風險清單、威脅情境/FMEA/HAZOP 工作表 |

---

## Design QA Role KPI 與證據

### KPI 類別

1. QA Standard Quality（QA 標準品質）
2. Document Completeness Verification（文件完整性驗證）
3. Traceability Matrix Integrity（追溯矩陣完整性）
4. Document Register Accuracy（文件清冊準確性）
5. Conformity Review Coverage（符合性審查覆蓋度）

### KPI 明細

| KPI | 定義 | 合規條件 | 證據來源 |
|:-----------------------|:------------------------|:------------------|:------------------------|
| QA Standard Executability | QA 標準條款皆可被具體執行 | 年度內無「無法執行」之正式回報 | 標準回饋紀錄、例外申請紀錄 |
| Gate 3 Delivery Checklist Pass Rate Auditability | 所有 Gate 3 皆執行交付檢查 | 12 項檢查皆有明確結果 | 設計交付檢查表、Gate 3 審查紀錄 |
| Traceability Matrix Completeness | 所有專案皆有完整追溯矩陣 | 矩陣涵蓋所有設計需求 | 需求追溯矩陣、設計需求規格 |
| Traceability Sampling Verification Execution | 所有 Gate 3 皆執行 20% 抽查 | 抽查紀錄包含樣本與結果 | 追溯性抽查紀錄、Gate 3 審查紀錄 |
| Document Register Accuracy | 文件清冊與實際文件一致 | 抽查一致率符合標準 | 文件清冊、設計文件抽查比對 |
| Version Consistency Verification at Gate 3 | 所有 Gate 3 文件包版本一致 | 驗證紀錄顯示一致 | 版本一致性驗證紀錄、Gate 3 文件包 |

---

## Design Governance Coordinator KPI 與證據

### KPI 類別

1. Gate Process Coordination Effectiveness（Gate 流程協調有效性）
2. Meeting Record Completeness（會議紀錄完整性）
3. Version Control Integrity（版本控制完整性）

### KPI 明細

| KPI | 定義 | 合規條件 | 證據來源 |
|:-----------------------|:------------------------|:------------------|:------------------------|
| Gate Meeting Record Completeness | 所有 Gate 會議皆有完整紀錄 | 紀錄包含議程、決議、待辦事項 | Gate 會議紀錄、Gate 審查紀錄 |
| Action Item Tracking Closure | 所有待辦事項皆有追蹤紀錄 | 於下一 Gate 前結案或展延 | 流程追蹤表、Gate 會議紀錄 |
| Document Version Control Integrity | 所有治理文件皆納入版本控制 | 版本變更有對應紀錄 | 版本控制紀錄、治理文件 |
| Process Reminder Timeliness | 所有流程提醒皆於規定時點發送 | 發送紀錄顯示準時 | 流程提醒發送紀錄、流程追蹤表 |

---

## Pre-Gate Design Support KPI 與證據

**角色定位**：Concept System Architect / Feasibility Owner - Gate 0 執行角色

### KPI 類別

1. Gate 0 Input Document Quality（Gate 0 輸入文件品質）
2. Requirement Clarification Adoption（需求釐清採用度）
3. Rework Reduction Effectiveness（返工降低效果）
4. Risk Pre-disclosure Quality（風險預揭露品質）
5. Conceptual Deliverable Completeness（概念產出完整性）

### KPI 設計原則

**本角色之 KPI 設計遵循以下原則**：

| 原則 | 說明 |
|-----|------|
| 僅衡量可驗證貢獻 | KPI 須可於後續 Gate 階段驗證，非自我宣稱 |
| 不涉及商務結果 | 不以成交率、商務金額或客戶滿意度為指標 |
| 後向驗證機制 | KPI 分數須待後續 Gate 結果確認後方可生效 |
| 負向驗證優先 | 以「未發生返工」「未出現重複風險」等負向指標為主 |
| Gate 0 輸入當責 | 本角色對 Gate 0 所有輸入文件品質負當責 |

### KPI 明細

| KPI | 定義 | 合規條件 | 證據來源 |
|:-----------------------|:------------------------|:------------------|:------------------------|
| Gate 0 Input Document Completeness | Gate 0 所有必要輸入文件皆已產出 | 5 項必要文件皆存在 | Gate 0 文件包檢查表 |
| Requirement Clarification Adoption Rate | 需求釐清紀錄於 Gate 0 評估中被引用之比例 | Gate 0 核准文件引用需求釐清紀錄 | Gate 0 核准紀錄、需求釐清紀錄引用追溯 |
| Rework Reduction Traceability | Gate 1 後設計變更中因「需求澄清不足」導致之變更比例 | 相關變更比例低於組織門檻 | 設計變更紀錄、變更類別分析 |
| Risk Pre-disclosure Non-recurrence | 預揭露之風險於後續 Gate 未重複出現為新識別風險 | 殘餘風險清單無預揭露風險之重複識別 | 風險預揭露清單、殘餘風險清單交叉比對 |
| CBOM Completeness | Commercial BOM (CBOM) 包含必要項目且標註正確 | CBOM 具備「商務可用 / 設計不拘束」標註及 BOM Type 宣告 | Commercial BOM (CBOM)、標註檢查紀錄、BOM Type 欄位 |
| Concept Architecture Completeness | 概念架構圖包含必要元件且標註正確 | 架構圖具備「Conceptual / Non-binding」標註 | Concept Architecture、標註檢查紀錄 |
| Gate 0 Responsibility Handover Completion | Gate 0 核准後責任移轉紀錄完整 | 交接紀錄具備必要簽核 | Gate 0 責任移轉紀錄 |

### Gate 0 必要輸入文件

**Pre-Gate Design Support 須產出以下 5 項 Gate 0 必要輸入文件**：

| 文件 | 性質 | 必要欄位 |
|-----|------|---------|
| 需求釐清紀錄 | 正式文件 | 釐清項目、結果、日期、確認簽核 |
| 風險預揭露清單 | 正式文件 | 風險 ID、描述、揭露日期、追溯 ID |
| 技術可行性初評 | 建議性質 | 評估結論、建議事項 |
| Commercial BOM (CBOM) | Commercially Usable / Design Non-binding | 設備清單、規格初估、BOM Type 宣告、商務可用/設計不拘束標註 |
| 概念系統架構圖（Concept Architecture） | Conceptual / Non-binding | 系統架構、Non-binding 標註 |

### KPI 生效時點

**重要說明**：Pre-Gate Design Support 之 KPI 分數須待後續 Gate 結果驗證後方可確認。

| KPI | 評估時點 | 生效條件 |
|-----|---------|---------|
| Gate 0 Input Document Completeness | Gate 0 提交時 | 即時評估 |
| Requirement Clarification Adoption Rate | Gate 0 核准後 | Gate 0 文件引用需求釐清紀錄 |
| Rework Reduction Traceability | Gate 1 後 30 日 | 設計變更紀錄分析完成 |
| Risk Pre-disclosure Non-recurrence | Gate 3 完成後 | 殘餘風險清單與預揭露清單比對完成 |
| CBOM Completeness | Gate 0 提交時 | 即時評估 |
| Concept Architecture Completeness | Gate 0 提交時 | 即時評估 |
| Gate 0 Responsibility Handover Completion | Gate 0 核准後 15 日 | 交接紀錄完成 |

### 潛在誤用防範

| 潛在誤用 | 防範措施 |
|---------|---------|
| 以預釐清數量評估（鼓勵膨脹） | 僅評估被採用之預釐清，非總數量 |
| 以自評品質評估（鼓勵美化） | 以後續 Gate 之客觀驗證為準 |
| 將商務結果納入評估 | 明確禁止以成交率或商務金額為 KPI |
| 規避返工責任 | 返工分析由設計角色執行，非 Pre-Gate Design Support 自評 |
| 概念產出作為正式設計使用 | 強制標註 Non-binding，正式設計由 System Architect 重新產出 |
| CBOM 作為設計基線使用 | CBOM 明確標註「商務可用 / 設計不拘束」，EBOM 由 System Architect 於 Gate 1 產出 |
| 報價後 CBOM 版本遺失 | 報價後須保留 CBOM 版本，納入版本追溯紀錄 |

### 禁止之 KPI 類型

以下類型之 KPI **不得**用於評估 Pre-Gate Design Support 角色：

| 禁止類型 | 理由 |
|---------|------|
| 成交率或商務金額 | 非技術貢獻指標，破壞角色定位 |
| 客戶滿意度評分 | 主觀評價，非可驗證貢獻 |
| 預釐清活動數量 | 鼓勵膨脹，非品質導向 |
| Gate 0 通過率 | Gate 決策責任歸屬 Head of System Design，非本角色 |
| 設計缺陷責任 | Gate 0 後設計責任移轉至 System Architect |
| 概念產出之正式使用後果 | 概念產出明確標註 Non-binding |

---

## 證據控制驗證

### 證據可控性矩陣

| 證據類型 | 控制角色 | 驗證 |
|---------|---------|-----|
| 標準文件（含版本、審查紀錄） | 各標準擁有角色 | ✓ |
| 例外裁決紀錄 | Head of System Design | ✓ |
| Gate 審查紀錄 | System Design Governance Lead | ✓ |
| 設計基線文件集 | System Architect | ✓ |
| Engineering BOM (EBOM) | System Architect | ✓ |
| 技術可行性評估紀錄 | System Architect | ✓ |
| SL Decision Record | Security Engineering Role | ✓ |
| 整合式風險評估報告 | Security Engineering Role | ✓ |
| SR 檢查表 | Security Engineering Role | ✓ |
| 殘餘風險清單 | Security Engineering Role | ✓ |
| 需求追溯矩陣 | Design QA Role | ✓ |
| 文件清冊 | Design QA Role | ✓ |
| 設計交付檢查表 | Design QA Role | ✓ |
| Gate 會議紀錄 | Design Governance Coordinator | ✓ |
| 版本控制紀錄 | Design Governance Coordinator | ✓ |
| 需求釐清紀錄 | Pre-Gate Design Support | ✓ |
| 風險預揭露清單 | Pre-Gate Design Support | ✓ |
| Commercial BOM (CBOM) | Pre-Gate Design Support | ✓ |
| 概念系統架構圖（Concept Architecture） | Pre-Gate Design Support | ✓ |
| 技術可行性初評 | Pre-Gate Design Support | ✓ |
| Gate 0 責任移轉紀錄 | Pre-Gate Design Support + System Architect | ✓ |
| 需求釐清採用追溯紀錄 | System Design Governance Lead（驗證）| ✓ |

### 設計時權限驗證

所有 KPI 皆反映設計時權限，不涉及：
- [x] 執行階段結果
- [x] 運行階段事件
- [x] 實作品質
- [x] 部署成效

---

## 潛在誤用防範

### 通用誤用防範

| 潛在誤用 | 防範措施 |
|---------|---------|
| 以數量評估績效（鼓勵膨脹） | 僅評估必要項目之完整性與可追溯性 |
| 以速度評估績效（鼓勵草率） | 不設時效 KPI，僅評估紀錄完整性 |
| 將執行階段問題歸責於設計 | 明確區分設計時權限範圍 |
| 以比率方向評估績效（鼓勵偏頗） | 僅評估紀錄存在與完整性，不評估核准/拒絕比率 |

### 角色特定誤用防範

| 角色 | 潛在誤用 | 防範措施 |
|-----|---------|---------|
| Head of System Design | 以例外核准數量評估 | 僅評估紀錄完整性 |
| System Design Governance Lead | 以 Gate 通過率評估 | 僅評估審查紀錄完整性 |
| System Architect | 以文件數量評估 | 僅評估必要文件之存在 |
| Security Engineering Role | 以風險數量評估 | 僅評估可追溯性 |
| Design QA Role | 以發現數量評估 | 僅評估覆蓋度與紀錄完整性 |
| Design Governance Coordinator | 以會議數量評估 | 僅評估必要會議之紀錄 |
| Pre-Gate Design Support | 以預釐清數量或商務成果評估 | 僅評估後續 Gate 可驗證之貢獻 |

---

## 假設條件

1. **證據可及性**：所有列舉之證據皆為角色可控或可取得之文件/紀錄
2. **紀錄系統存在**：組織具備文件管理系統、版本控制系統及紀錄保存機制
3. **標準回饋機制**：組織具備正式之標準回饋蒐集與處理機制
4. **歸責分析能力**：組織具備執行設計缺陷歸責分析之能力與程序

---

*文件結束*
