---
name: ai-workflow-automation
description: >
  AI 與工作流自動化。
  Develop and deploy AI-assisted tools for automated design review, including rule-based checking of naming conventions and document completeness, patte。Design and implement automated workflows that chain multiple engineering skills into repeatable pip
  MANDATORY TRIGGERS: AI 輔助設計審查, AI 與工作流自動化, 自動化技能調用, 審查工作流程自動化, engineering-review, repeatable-processes, skill-chaining, design-errors, finding-tracking, workflow-management, design-review, Review Workflow Automation.
  Use this skill for ai workflow automation tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# AI 與工作流自動化

本 Skill 整合 3 個工程技能定義，提供AI 與工作流自動化的完整工作流程。
適用領域：Automation & AI（D13）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D02-012, SK-D09-005, SK-D11-001, SK-D11-003, SK-D11-006, SK-D11-010

---

## 1. 輸入

- Design artifacts in standardized formats (requirements specifications, architecture diagrams, datasheets, drawings, interface control documents)
- Design standards and templates (from SK-D11-010: Internal Design Standards Maintenance)
- Rule sets and pattern definitions (naming conventions, completeness criteria, error patterns)
- Design review checklist (from SK-D11-006: Quality Plan Development)
- Historical design review findings and lessons learned
- Tool platform specifications (cloud vs. on-premise, API interfaces, compliance requirements)
- Skill definitions and interface contracts (inputs/outputs for each skill to be chained)
- Example or baseline execution data (input test sets, expected outputs)
- Requirements for the specific pipeline (e.g., "asset inventory to zone/conduit" or "point list to HMI")
- Validation rules (data schemas, acceptable value ranges, required fields)
- Error handling requirements (retry logic, notification triggers, manual escalation criteria)
- Orchestration platform specifications (on-premise, cloud, latency/throughput constraints)

---

## 2. 工作流程

### Step 1: AI 輔助設計審查
**SK 來源**：SK-D13-003 — AI-Assisted Design Review

執行AI 輔助設計審查：Develop and deploy AI-assisted tools for automated design review, including rule-based checking of naming conventions and document completeness, patte

**本步驟交付物**：
- AI-assisted review tool (implemented as script, plugin, or service)
- Rule configuration library:
- Naming convention rules (zone names, conduit IDs, device tags, document sections)

### Step 2: 自動化技能調用
**SK 來源**：SK-D13-004 — Automated Skill Invocation

執行自動化技能調用：Design and implement automated workflows that chain multiple engineering skills into repeatable pipelines, enabling complex multi-step processes to ex

**本步驟交付物**：
- Orchestration workflow definition (DAG/pipeline configuration, skill invocation order, dependencies)
- Input/output validation schema and implementation (JSON Schema, Pydantic models, or equivalent)
- Workflow execution engine/service (script, containerized function, or cloud orchestration job)

### Step 3: 審查工作流程自動化
**SK 來源**：SK-D13-006 — Review Workflow Automation

執行審查工作流程自動化：Automate engineering review workflows including review assignment and routing, checklist generation, finding tracking and resolution verification, and

**本步驟交付物**：
- Review workflow orchestration specification:
- Document intake and classification (automatic detection of document type and applicable review scope)
- Reviewer assignment rules (based on expertise, availability, conflict-of-interest checks)

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | AI-assisted review tool (implemented as script, plugin, or service) | 依需求 |
| 2 | Rule configuration library: | 依需求 |
| 3 | Naming convention rules (zone names, conduit IDs, device tags, document sections) | 依需求 |
| 4 | Completeness checks (required fields, cross-references, traceability matrix entries) | Markdown |
| 5 | Consistency checks (nomenclature consistency across documents, matching definitions, aligned data flows) | 依需求 |
| 6 | Error pattern detectors (common design mistakes, missing security controls, untraceable requirements) | 依需求 |
| 7 | Orchestration workflow definition (DAG/pipeline configuration, skill invocation order, dependencies) | 依需求 |
| 8 | Input/output validation schema and implementation (JSON Schema, Pydantic models, or equivalent) | 依需求 |
| 9 | Workflow execution engine/service (script, containerized function, or cloud orchestration job) | 依需求 |
| 10 | Error handling and logging implementation: | 依需求 |
| 11 | Exception catching and classification | 依需求 |
| 12 | Detailed event logging for audit and diagnosis | 依需求 |

---

## 4. 適用標準

- IEC 62443-3-2: Security Risk Assessment for System Design — requirements for design review completeness
- IEC 62443-1-1: Terminology, concepts and models — design artifact nomenclature standards
- ISO/IEC 42001: AI Management System — governance and quality standards for AI-assisted tools
- IEC 62443-4-1: Product Development — lifecycle and design assurance requirements
- Best practice: Design review checklists from NIST SP 800-82, NERC CIP OE standards
- IEC 62443-4-2: Security-Oriented Design and Development — secure coding for automation scripts
- ISO/IEC 42001: Artificial Intelligence Management System (if AI/ML skills are chained)
- Best practice: DAG design patterns from Apache Airflow, Kubernetes deployment patterns
- NIST SP 800-53: Audit logging and change control requirements
- IEC 62443-1-1: Terminology, concepts and models — review and approval documentation

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Rule set covers all items in SK-D11-006 Quality Plan design review checklist (10 | ✅ 已驗證 |
| 2 | Tool correctly detects naming convention violations, missing required fields, an | ✅ 已驗證 |
| 3 | Pattern matching identifies ≥95% of injected error scenarios (common design mist | ✅ 已驗證 |
| 4 | Consistency verification confirms traceability matrix completeness and validates | ✅ 已驗證 |
| 5 | Tool produces actionable review report: each finding includes rule violated, art | ✅ 已驗證 |
| 6 | Performance meets usability threshold: review execution on typical design packag | ✅ 已驗證 |
| 7 | Integration with document management and/or CI/CD pipeline tested and operationa | ✅ 已驗證 |
| 8 | Tool and rules approved by SYS, SAC, and QA; training materials prepared for des | ✅ 已驗證 |
| 9 | Workflow DAG/pipeline configuration documents all skill dependencies and executi | ✅ 已驗證 |
| 10 | Input validation detects 100% of schema violations (missing required fields, inv | ✅ 已驗證 |
| 11 | Output validation confirms each skill's outputs match expected schema before pas | ✅ 已驗證 |
| 12 | Pipeline execution latency meets specification for target use case (e.g., < 30 m | ✅ 已驗證 |
| 13 | Error handling tested: exceptions caught, logged, and escalated correctly; rollb | ✅ 已驗證 |
| 14 | Pipeline successfully executes end-to-end on representative input sets (minimum  | ✅ 已驗證 |
| 15 | Monitoring and alerting functional: pipeline failures trigger notifications with | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D13-003 | | Junior (< 2 yr) | 25–35 person-days | Includes tool development, rule configuration, validation on |
| SK-D13-003 | | Senior (5+ yr) | 15–20 person-days | Same scope; leverages prior automation experience and interna |
| SK-D13-003 | Notes: Tool sophistication and rule set complexity drive effort. Initial deployment targets 20–30 de |
| SK-D13-004 | | Junior (< 2 yr) | 15–25 person-days | Per pipeline; includes orchestration design, validation impl |
| SK-D13-004 | | Senior (5+ yr) | 8–15 person-days | Same scope; leverages prior orchestration experience and inter |
| SK-D13-004 | Notes: Simple 2–3 skill chains typically require 10–15 person-days. Complex multi-branch pipelines w |
| SK-D13-006 | | Junior (< 2 yr) | 20–30 person-days | Includes workflow design, automation implementation, DMS int |
| SK-D13-006 | | Senior (5+ yr) | 12–18 person-days | Same scope; leverages prior workflow automation experience an |

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
AI 與工作流自動化已完成。
📋 執行範圍：3 個工程步驟（SK-D13-003, SK-D13-004, SK-D13-006）
📊 交付物清單：
  - AI-assisted review tool (implemented as script, plugin, or service)
  - Rule configuration library:
  - Naming convention rules (zone names, conduit IDs, device tags, document sections)
  - Completeness checks (required fields, cross-references, traceability matrix entries)
  - Consistency checks (nomenclature consistency across documents, matching definitions, aligned data flows)
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
| SK 覆蓋 | SK-D13-003, SK-D13-004, SK-D13-006 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D13-003 | AI-Assisted Design Review | AI 輔助設計審查 | Develop and deploy AI-assisted tools for automated design re |
| SK-D13-004 | Automated Skill Invocation | 自動化技能調用 | Design and implement automated workflows that chain multiple |
| SK-D13-006 | Review Workflow Automation | 審查工作流程自動化 | Automate engineering review workflows including review assig |

<!-- Phase 5 Wave 2 deepened: SK-D13-003, SK-D13-004, SK-D13-006 -->