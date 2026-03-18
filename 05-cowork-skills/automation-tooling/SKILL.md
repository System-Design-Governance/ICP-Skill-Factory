---
name: automation-tooling
description: >
  自動化工具開發。
  The Automated Calculation Script Development skill develops and deploys reusable calculation scripts (Python, MATLAB, Excel VBA) that automate repetit。The Document Generator Development skill creates automated systems that produce engineering deliver
  MANDATORY TRIGGERS: 文件產生器開發, 自動化計算腳本開發, 自動化測試管線開發, 自動化工具開發, Document Generator Development, generator, pipeline, script, Automated Test Pipeline Development, Automated Calculation Script Development, automation tooling, document.
  Use this skill for automation tooling tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 自動化工具開發

本 Skill 整合 3 個工程技能定義，提供自動化工具開發的完整工作流程。
適用領域：Automation & AI（D13）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-014, SK-D07-005, SK-D12-001, SK-D13-003, SK-D13-004, SK-D13-006

---

## 1. 輸入

- Engineering calculation methodologies and technical standards (IEC 60287, IEEE 45, IEC 60050)
- Cable and equipment specifications (conductors, insulation, ratings)
- System parameters (voltages, currents, fault levels, duty cycles)
- Protection device data (coordination curves, settings, time-current characteristics)
- Load flow analysis data and thermal boundary conditions
- Design constraints and acceptance criteria
- Structured engineering data sources (CAD extracts, database queries, configuration management systems)
- Document template specifications (layout, formatting, required sections)
- Mapping definitions (data-to-template field associations)
- Quality validation rules and acceptance criteria for generated documents
- Output format specifications (DOCX, XLSX, PDF rendering requirements)
- Organizational style guides and document standards

---

## 2. 工作流程

### Step 1: 自動化計算腳本開發
**SK 來源**：SK-D13-001 — Automated Calculation Script Development

執行自動化計算腳本開發：The Automated Calculation Script Development skill develops and deploys reusable calculation scripts (Python, MATLAB, Excel VBA) that automate repetit

**本步驟交付物**：
- Calculation scripts (Python, MATLAB, or VBA implementations)
- Input specification and validation procedures
- Calculation methodology documentation (technical approach and formula justification)

### Step 2: 文件產生器開發
**SK 來源**：SK-D13-002 — Document Generator Development

執行文件產生器開發：The Document Generator Development skill creates automated systems that produce engineering deliverables (point lists, wiring schedules, test reports,

**本步驟交付物**：
- Document Generator Implementation (software module or application)
- Template Library (DOCX, XLSX, PDF templates for all supported document types)
- Data Source Integration Specifications and connectors

### Step 3: 自動化測試管線開發
**SK 來源**：SK-D13-005 — Automated Test Pipeline Development

執行自動化測試管線開發：The Automated Test Pipeline Development skill establishes continuous verification systems for OT/ICS system configurations, security baselines, and co

**本步驟交付物**：
- Automated test pipeline implementation (infrastructure and orchestration)
- Test script library (configuration validation, security baseline, compliance tests)
- Test environment setup and management procedures

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Calculation scripts (Python, MATLAB, or VBA implementations) | 依需求 |
| 2 | Input specification and validation procedures | 依需求 |
| 3 | Calculation methodology documentation (technical approach and formula justification) | 依需求 |
| 4 | Verification and testing procedures (unit tests, regression tests) | 依需求 |
| 5 | Output templates and example calculations | 依需求 |
| 6 | User guide and troubleshooting documentation | 依需求 |
| 7 | Document Generator Implementation (software module or application) | 依需求 |
| 8 | Template Library (DOCX, XLSX, PDF templates for all supported document types) | 依需求 |
| 9 | Data Source Integration Specifications and connectors | 依需求 |
| 10 | Quality Validation Framework (automated document review rules) | 依需求 |
| 11 | Generator User Guide and Administration Documentation | 依需求 |
| 12 | Example Generated Documents (one per template type) | 依需求 |

---

## 4. 適用標準

- IEC 60287 (Electric cables - calculation of the current rating)
- IEEE 45 (Recommended Practice for Electrical Installations on Shipboard and Other Marine Applications)
- IEC 60050 (International Electrotechnical Vocabulary)
- ISO 80000 (Quantities and units)
- Organizational calculation standards and design procedures
- IEC 62443 Documentation Requirements (systems and component assurance records)
- ISO/IEC 27001 Document Management (if handling classified or sensitive data)
- Organizational technical documentation standards
- Industry standards for electrical and automation engineering deliverables
- IEC 62443 Systems and Component Assurance (all parts, especially 3-3 for configuration and compliance)

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Scripts implement all required calculation types (cable sizing, voltage drop, pr | ✅ 已驗證 |
| 2 | Input validation rejects out-of-range or malformed inputs with clear error messa | ✅ 已驗證 |
| 3 | Script results match manually calculated results within engineering tolerance (t | ✅ 已驗證 |
| 4 | Unit test coverage exceeds 85% of code paths; regression tests validate calculat | ✅ 已驗證 |
| 5 | User documentation includes methodology explanation, input parameter definitions | ✅ 已驗證 |
| 6 | Scripts are deployable via version control with change tracking and rollback cap | ✅ 已驗證 |
| 7 | Document generators automatically produce all required deliverable types (point  | ✅ 已驗證 |
| 8 | Generated documents are consistently formatted and properly structured according | ✅ 已驗證 |
| 9 | Templates support all required output formats (DOCX, XLSX, PDF) with correct ren | ✅ 已驗證 |
| 10 | Data integration from multiple sources (CAD, databases, configuration systems) i | ✅ 已驗證 |
| 11 | Quality validation framework automatically detects missing fields, formatting er | ✅ 已驗證 |
| 12 | Automated generator reduces manual document creation effort by at least 70% whil | ✅ 已驗證 |
| 13 | Automated test pipeline successfully validates all major configuration areas (OS | ✅ 已驗證 |
| 14 | Security baseline testing detects deviations from hardened configurations and fa | ✅ 已驗證 |
| 15 | Compliance testing demonstrates coverage of IEC 62443 applicable requirements an | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D13-001 | | Role | Junior (hours) | Senior (hours) | |
| SK-D13-002 | | Role | Junior (hours) | Senior (hours) | |
| SK-D13-005 | | Role | Junior (hours) | Senior (hours) | |

---

## 7. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 輸入完整性 | 所有必要輸入文件已讀取並摘要 |
| 2 | 流程覆蓋 | 3 個工作步驟皆已執行並有產出 |
| 3 | 輸出完整性 | 所有交付物已產出、格式正確、非空白 |
| 4 | 標準合規 | 產出引用的標準版本正確 |
| 5 | 術語一致 | 專案術語、縮寫與 glossary 一致 |
| 6 | 跨步驟一致 | 各步驟產出間無矛盾（如數量、SL等級） |

---

## 8. 人類審核閘門

完成所有工作步驟後，暫停並向使用者提交審核：

```
自動化工具開發已完成。
📋 執行範圍：3 個工程步驟（SK-D13-001, SK-D13-002, SK-D13-005）
📊 交付物清單：
  - Calculation scripts (Python, MATLAB, or VBA implementations)
  - Input specification and validation procedures
  - Calculation methodology documentation (technical approach and formula justification)
  - Verification and testing procedures (unit tests, regression tests)
  - Output templates and example calculations
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
| Domain | D13 (Automation & AI) |
| SK 覆蓋 | SK-D13-001, SK-D13-002, SK-D13-005 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D13-001 | Automated Calculation Script Development | 自動化計算腳本開發 | The Automated Calculation Script Development skill develops  |
| SK-D13-002 | Document Generator Development | 文件產生器開發 | The Document Generator Development skill creates automated s |
| SK-D13-005 | Automated Test Pipeline Development | 自動化測試管線開發 | The Automated Test Pipeline Development skill establishes co |

<!-- Phase 5 Wave 2 deepened: SK-D13-001, SK-D13-002, SK-D13-005 -->