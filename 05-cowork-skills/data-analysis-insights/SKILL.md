---
name: data-analysis-insights
description: >
  資料分析與應用。
  Develop load forecasting models (statistical and machine-learning-based) for predicting electrical demand at various time horizons including day-ahead。This skill encompasses the design of monitoring and analytics dashboards that provide operators and
  MANDATORY TRIGGERS: 資料分析與應用, 資料存取政策設計, 負載預測模型開發, 資料字典建立, 監控儀表板設計, dashboard, machine-learning, access, Data Dictionary Development, dispatch-optimization, Monitoring Dashboard Design, DERMS, Data Access Policy Design.
  Use this skill for data analysis insights tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 資料分析與應用

本 Skill 整合 4 個工程技能定義，提供資料分析與應用的完整工作流程。
適用領域：Energy Data Platform（D12）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D01-014, SK-D01-020, SK-D01-033, SK-D04-005, SK-D05-005

---

## 1. 輸入

- Historical load data (consumption records, 15-minute or hourly intervals, minimum 2 years of data)
- Weather data sources (temperature, humidity, solar irradiance, wind speed, cloud cover)
- Calendar and special event information (holidays, planned outages, demand response events)
- System topology and zone definitions (from SK-D01-001) — understanding service areas and customer categories
- Operational constraints and objectives (demand response targets, renewable penetration goals)
- EMS/DERMS system specifications and data interfaces (API contracts, data formats, update frequencies)
- Data Acquisition Architecture (from SK-D12-001: Data Acquisition Architecture) — available data sources and schema
- SIEM Design (from SK-D01-014: SIEM Design and Implementation) — security event data structure and queries
- KPI and Metrics Requirements: business, operational, and security KPIs to be displayed (from project requirements or operations team)
- HMI Screen Design (from SK-D05-005: HMI Screen Design) — design consistency and screen layout standards
- Access Control Policies (from SK-D01-020: Account and Access Control) — role-based dashboard access and data filtering
- System Performance and Data Refresh Requirements: latency tolerance, acceptable query load on backend systems

---

## 2. 工作流程

### Step 1: 負載預測模型開發
**SK 來源**：SK-D12-005 — Load Forecasting Model Development

執行負載預測模型開發：Develop load forecasting models (statistical and machine-learning-based) for predicting electrical demand at various time horizons including day-ahead

**本步驟交付物**：
- Load forecasting model(s) in deployable format (Python pickle, ONNX, PMML, or cloud ML endpoint)
- Model training and validation report including:
- Feature importance analysis

### Step 2: 監控儀表板設計
**SK 來源**：SK-D12-006 — Monitoring Dashboard Design

執行監控儀表板設計：This skill encompasses the design of monitoring and analytics dashboards that provide operators and managers with real-time visibility into operationa

**本步驟交付物**：
- Dashboard Design Specification: dashboard layout, widget definitions, data sources for each widget, refresh rates, drill-down navigation paths
- Dashboard Prototype or Wireframes: visual mockups showing dashboard layout and widget placement for each dashboard type (operational, security, execut
- Data Integration Specification: data sources for each dashboard, queries or API calls to retrieve data, data transformation logic (if needed)

### Step 3: 資料字典建立
**SK 來源**：SK-D12-007 — Data Dictionary Development

執行資料字典建立：This skill encompasses the development of a comprehensive master Data Dictionary that serves as the authoritative reference for all data elements acro

**本步驟交付物**：
- Master Data Dictionary: comprehensive document organized by system/domain, listing all data elements with metadata (name, type, unit, range, source, c
- Data Element Metadata Catalog: structured database or spreadsheet with searchable index of all data elements and their properties
- Data Naming Conventions and Standards: guidelines for data element naming, abbreviations, units, and metadata documentation

### Step 4: 資料存取政策設計
**SK 來源**：SK-D12-008 — Data Access Policy Design

執行資料存取政策設計：This skill encompasses the design of data access policies that define who can read, write, or modify operational data across OT/IT systems, implementi

**本步驟交付物**：
- Data Access Policy Document: policy statement specifying data access principles, role definitions, access control requirements, and audit requirements
- Role and Permission Matrix: table defining which roles have read/write/execute access to which data categories/elements; matrix includes justification
- Access Control Specifications: technical specifications for implementing RBAC in database, application, and data platform layers

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Load forecasting model(s) in deployable format (Python pickle, ONNX, PMML, or cloud ML endpoint) | 依需求 |
| 2 | Model training and validation report including: | Markdown |
| 3 | Feature importance analysis | 依需求 |
| 4 | Model accuracy metrics (MAPE, RMSE, MAE) by forecast horizon and seasonal period | 依需求 |
| 5 | Comparison of statistical vs. ML-based approaches | 依需求 |
| 6 | Cross-validation results and overfitting analysis | 依需求 |
| 7 | Dashboard Design Specification: dashboard layout, widget definitions, data sources for each widget, refresh rates, drill-down navigation paths | 依需求 |
| 8 | Dashboard Prototype or Wireframes: visual mockups showing dashboard layout and widget placement for each dashboard type (operational, security, execut | 依需求 |
| 9 | Data Integration Specification: data sources for each dashboard, queries or API calls to retrieve data, data transformation logic (if needed) | 依需求 |
| 10 | Widget and Layout Templates: reusable dashboard components and layout patterns for consistency across dashboards | 依需求 |
| 11 | Role-Based Access Control (RBAC) Matrix: role definitions, dashboards accessible per role, data filtering rules per role | Markdown |
| 12 | Performance and Scalability Plan: query optimization techniques, caching strategies, acceptable query response times, system load testing results | 依需求 |

---

## 4. 適用標準

- IEC 62443-3-3: System Security Requirements and Security Levels — security requirements for model data and APIs
- ISO/IEC 42001: Artificial Intelligence Management System — governance and quality standards for ML-based forecasting
- NERC EOP (Energy Operations Standard) — reliability requirements for forecast inputs to dispatch optimization
- Best practice: MISO/PJM Load Forecasting Methodologies (available from RTOs)
- NIST SP 800-53: Security Controls for predictive analytics systems
- IEC 62443-3-3: System security requirements — security dashboard design requirements
- NIST SP 800-82 Rev. 3: Guide to OT Security — operational monitoring and visibility
- Information visualization best practices (Tufte, Few, Cleveland) — effective chart and dashboard design
- Web accessibility standards (WCAG 2.1) — accessibility for vision-impaired users
- Usability standards (ISO 9241: Ergonomics) — user interface design and efficiency

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Model architecture documented and rationale provided for statistical vs. ML-base | ✅ 已驗證 |
| 2 | Feature engineering pipeline includes at minimum: historical load lags (7d, 14d, | ✅ 已驗證 |
| 3 | Model accuracy meets targets: MAPE ≤ 5% for day-ahead, ≤ 8% for hour-ahead (or d | ✅ 已驗證 |
| 4 | Cross-validation on hold-out test data confirms model generalizes to unseen peri | ✅ 已驗證 |
| 5 | Real-time scoring interface specified and tested: latency < specification, handl | ✅ 已驗證 |
| 6 | Integration test with EMS/DERMS confirms forecasts accepted by dispatch optimiza | ✅ 已驗證 |
| 7 | Model retraining procedure documented and validated: includes data quality check | ✅ 已驗證 |
| 8 | Code review completed and approved by both SYS and DAT roles | ✅ 已驗證 |
| 9 | Dashboard Design Specification documents all dashboard types (operational, secur | ✅ 已驗證 |
| 10 | For each dashboard widget: data source, query/API call, refresh rate, and visual | ✅ 已驗證 |
| 11 | Drill-down navigation is clearly mapped: users can navigate from summary metrics | ✅ 已驗證 |
| 12 | Role-based access control matrix specifies which roles can view which dashboards | ✅ 已驗證 |
| 13 | Dashboard prototype or wireframes have been reviewed by operational stakeholders | ✅ 已驗證 |
| 14 | Performance testing confirms dashboard queries complete within acceptable respon | ✅ 已驗證 |
| 15 | Data Dictionary includes 100% of data elements from all identified OT and IT sys | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D12-005 | | Junior (< 2 yr) | 20–30 person-days | Includes data exploration, feature engineering experimentati |
| SK-D12-005 | | Senior (5+ yr) | 10–15 person-days | Same scope; leverages prior ML/forecasting experience and int |
| SK-D12-005 | Notes: Multi-zone forecasting (e.g., forecast per feeder or customer class) scales roughly linearly. |
| SK-D12-006 | | Junior (< 2 yr) | 10–16 person-days | Assumes 4–6 dashboards, 15–20 total widgets, greenfield desi |
| SK-D12-006 | | Senior (5+ yr) | 5–8 person-days | Same scope; senior can rapidly design effective visualizations  |
| SK-D12-006 | Notes: Dashboards with complex data transformations or advanced visualization (geographic maps, 3D v |
| SK-D12-007 | | Junior (< 2 yr) | 10–16 person-days | Assumes 200–400 data elements across 5–8 systems, greenfield |
| SK-D12-007 | | Senior (5+ yr) | 5–8 person-days | Same scope; senior can rapidly standardize naming conventions a |

---

## 7. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 輸入完整性 | 所有必要輸入文件已讀取並摘要 |
| 2 | 流程覆蓋 | 4 個工作步驟皆已執行並有產出 |
| 3 | 輸出完整性 | 所有交付物已產出、格式正確、非空白 |
| 4 | 標準合規 | 產出引用的標準版本正確 |
| 5 | 術語一致 | 專案術語、縮寫與 glossary 一致 |
| 6 | 跨步驟一致 | 各步驟產出間無矛盾（如數量、SL等級） |
| 7 | 依賴追溯 | 外部依賴 SK 的輸入已驗證可用 |

---

## 8. 人類審核閘門

完成所有工作步驟後，暫停並向使用者提交審核：

```
資料分析與應用已完成。
📋 執行範圍：4 個工程步驟（SK-D12-005, SK-D12-006, SK-D12-007, SK-D12-008）
📊 交付物清單：
  - Load forecasting model(s) in deployable format (Python pickle, ONNX, PMML, or cloud ML endpoint)
  - Model training and validation report including:
  - Feature importance analysis
  - Model accuracy metrics (MAPE, RMSE, MAE) by forecast horizon and seasonal period
  - Comparison of statistical vs. ML-based approaches
⚠️ 待確認事項：{列出 TBD 項目或需人工判斷的假設}
👉 請審核以上成果，確認 PASS / FAIL / PASS with Conditions。
```

**判定標準**：
- **PASS**：成果完整且正確，可進入下一階段或歸檔
- **FAIL**：發現重大缺漏或錯誤，需返工後重新提交
- **PASS with Conditions**：整體接受，但需補充特定項目後完成

---

## 9. IEC 62443 生命週期對應

| 項目 | 值 |
|------|---|
| 主要生命週期階段 | 依專案階段 |
| Domain | D12 (Energy Data Platform) |
| SK 覆蓋 | SK-D12-005, SK-D12-006, SK-D12-007, SK-D12-008 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D12-005 | Load Forecasting Model Development | 負載預測模型開發 | Develop load forecasting models (statistical and machine-lea |
| SK-D12-006 | Monitoring Dashboard Design | 監控儀表板設計 | This skill encompasses the design of monitoring and analytic |
| SK-D12-007 | Data Dictionary Development | 資料字典建立 | This skill encompasses the development of a comprehensive ma |
| SK-D12-008 | Data Access Policy Design | 資料存取政策設計 | This skill encompasses the design of data access policies th |

<!-- Phase 5 Wave 2 deepened: SK-D12-005, SK-D12-006, SK-D12-007, SK-D12-008 -->