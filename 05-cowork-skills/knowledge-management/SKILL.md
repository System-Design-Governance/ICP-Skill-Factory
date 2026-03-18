---
name: knowledge-management
description: >
  知識與能力管理。
  - Lessons collection becoming bureaucratic burden reducing participation。- Knowledge base becoming outdated or stale without maintenance。Maintain the library of internal design standards, templates, and reference architectures used across projects to
  MANDATORY TRIGGERS: 經驗學習管理, 工程能力框架建立, 內部設計標準維護, 技術知識庫建置, 工程培訓計畫管理, 知識與能力管理, qualification, collection, Personnel Security Qualification Management, kpi, Internal Design Standards Maintenance, Engineering Training Program Management, certification, RACI.
  Use this skill for knowledge management tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 知識與能力管理

本 Skill 整合 7 個工程技能定義，提供知識與能力管理的完整工作流程。
適用領域：Governance & Process（D11）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D09-008, SK-D10-001, SK-D11-006, SK-D11-013, SK-D11-017, SK-D11-019

---

## 1. 輸入

- Project design artifacts and lessons learned (successful designs, common design errors, improvement areas)
- Industry best practices and standards (IEC 62443, NIST SP 800-82, utility/industrial automation best practices)
- Customer requirements and preferences (may drive customization of standard templates)
- Feedback from project teams (usability of standards, gaps in coverage, requests for new standards)
- Regulatory and compliance requirements (must be incorporated into standards)
- Technology and product evolution (new tools, libraries, or approaches that should be standardized)
- GOV-SDP People Handbook (Tier 1): 7 role definitions with job descriptions, RACI matrices, KPI definitions (6+ KPIs per role with SMART targets)
- GOV-SDP scoring model: RCW (Role Complexity Weight), AF (Allocation Factor), PVF (Performance Verification Factor) formula
- IEC 62443-2-4 SP.01.01–SP.01.03: Service provider staffing and qualification requirements
- ICP organizational structure: department mandate, reporting lines, team composition
- Industry competency frameworks: IEC 62443, NIST NICE, ISA/IEC certification programs
- ID21 (Tier 3): QP-02 Personnel and Training Management Procedure — organizational training governance

---

## 2. 工作流程

### Step 1: 經驗學習管理
**SK 來源**：SK-D11-008 — Lessons Learned Management

執行經驗學習管理：- Lessons collection becoming bureaucratic burden reducing participation

### Step 2: 技術知識庫建置
**SK 來源**：SK-D11-009 — Technical Knowledge Base Development

執行技術知識庫建置：- Knowledge base becoming outdated or stale without maintenance

### Step 3: 內部設計標準維護
**SK 來源**：SK-D11-010 — Internal Design Standards Maintenance

執行內部設計標準維護：Maintain the library of internal design standards, templates, and reference architectures used across projects to ensure consistency, quality, and eff

**本步驟交付物**：
- Standards library (centralized, versioned repository):
- Design templates (architecture patterns, security zone templates, network segmentation templates)
- Technical standards (naming conventions, notation standards, technical decision documentation format)

### Step 4: 工程能力框架建立
**SK 來源**：SK-D11-011 — Engineering Competency Framework Development

執行工程能力框架建立：Develop and maintain the engineering competency framework that defines role-based capability requirements, proficiency levels, assessment criteria, an

**本步驟交付物**：
- Engineering Competency Framework Document:
- Role Taxonomy: 7 functional roles with clear role boundaries
- Head of System Design (department leadership, gate authority)

### Step 5: 工程培訓計畫管理
**SK 來源**：SK-D11-012 — Engineering Training Program Management

執行工程培訓計畫管理：Plan, execute, and manage the annual engineering training program that develops personnel competencies aligned with the Engineering Competency Framewo

**本步驟交付物**：
- Annual Training Plan Document:
- Training needs analysis: aggregated competency gaps across all roles, prioritized by business impact and gap severity
- Training curriculum: course/module inventory mapped to competency framework items

### Step 6: 
**SK 來源**：SK-D11-014 — Personnel Security Qualification Management

執行：Personnel security qualification management is a foundational control for confidentiality, integrity, and availability assurance. It bridges organizat

**本步驟交付物**：
- Background verification completion records
- Security clearance register (tracking table with clearance levels, issue/expiration dates)
- Certification tracking register (certifications held, renewal dates)

### Step 7: 
**SK 來源**：SK-D11-021 — Role KPI Evidence Collection & Scoring

執行：Role KPI Evidence Collection & Scoring operationalizes the GOV-SDP performance management system, translating organizational strategy into individual 

**本步驟交付物**：
- SMART KPI definitions per role (with success criteria and measurement methodology)
- Evidence collection records (organized by KPI with source documentation)
- RCW assessments per role with adjustment history

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Standards library (centralized, versioned repository): | 依需求 |
| 2 | Design templates (architecture patterns, security zone templates, network segmentation templates) | 依需求 |
| 3 | Technical standards (naming conventions, notation standards, technical decision documentation format) | 依需求 |
| 4 | Process standards (design review procedures, design change management process, approval workflow) | 依需求 |
| 5 | Reference architectures (proven solutions for common system types: greenfield SCADA, brownfield integration, distributed control) | 依需求 |
| 6 | Standards documentation for each standard: | 依需求 |
| 7 | Engineering Competency Framework Document: | 依需求 |
| 8 | Role Taxonomy: 7 functional roles with clear role boundaries | 依需求 |
| 9 | Head of System Design (department leadership, gate authority) | 依需求 |
| 10 | Security Architect (SAC — zone/conduit design, SL decision) | 依需求 |
| 11 | System Architect (SYS — system topology, integration architecture) | 依需求 |
| 12 | Security Engineering Role (implementation, SR verification) | 依需求 |

---

## 4. 適用標準

- Tier**: T3-Skill
- Maturity Level**: Active
- Version**: 1.0.0
- Created Date**: 2026-03-16
- Owner Role**: PM (Project Manager)
- Owner Role**: Head of System Design (GOV-SDP)
- IEC 62443-1-1: Terminology, concepts and models — foundational concepts for all standards
- IEC 62443-3-2: Security Risk Assessment for System Design — standards for zone/conduit and risk assessment
- ISO 9001: Quality Management — standards lifecycle and documentation control
- Best practice: Configuration Management and Change Control from CMMI, RUP, and industry standards organizations

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Systematic lessons learned collection at all project phases | ✅ 已驗證 |
| 2 | 100% of significant issues documented with root cause analysis | ✅ 已驗證 |
| 3 | Lessons categorized and indexed in searchable knowledge system | ✅ 已驗證 |
| 4 | Documented linkage between lessons and SK-D11-009 knowledge base entries | ✅ 已驗證 |
| 5 | Minimum 80% project team participation in lessons learned workshops | ✅ 已驗證 |
| 6 | Measurable reduction in recurring issues across projects (year-over-year) | ✅ 已驗證 |
| 7 | Demonstrated implementation of lessons in subsequent projects | ✅ 已驗證 |
| 8 | Regular reporting on organizational learning progress and impact | ✅ 已驗證 |
| 9 | Comprehensive knowledge base structure documented and implemented | ✅ 已驗證 |
| 10 | Minimum 50+ reference architectures documented and maintained | ✅ 已驗證 |
| 11 | Complete design pattern library with code examples and rationale | ✅ 已驗證 |
| 12 | Solved problem database covering 80%+ common technical issues | ✅ 已驗證 |
| 13 | Vendor-specific guides for all supported platforms and products | ✅ 已驗證 |
| 14 | Content submission and review workflow established and active | ✅ 已驗證 |
| 15 | Knowledge base search performance optimization (< 1 second queries) | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D11-010 | | Senior (5+ yr) | 2–3 days/month ongoing | Monthly maintenance including feedback processing, minor |
| SK-D11-011 | | Junior (< 2 yr) | 15–20 person-days | Assumes initial framework creation for 7 roles; includes rol |
| SK-D11-011 | | Senior (5+ yr) | 8–12 person-days | Same scope; senior leverages industry framework patterns and G |
| SK-D11-011 | Notes: Initial framework creation is a one-time effort; annual maintenance requires 3–5 person-days  |
| SK-D11-012 | | Junior (< 2 yr) | 10–15 person-days | Assumes 7-role department, ~15–20 engineers; includes needs  |
| SK-D11-012 | | Senior (5+ yr) | 5–8 person-days | Same scope; senior leverages established training templates and |
| SK-D11-012 | Notes: Annual training plan is a recurring deliverable; initial creation requires more effort (15–20 |
| SK-D11-014 | Average time from role assignment to access authorization completion (target: ≤5 business days) |

---

## 7. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 輸入完整性 | 所有必要輸入文件已讀取並摘要 |
| 2 | 流程覆蓋 | 7 個工作步驟皆已執行並有產出 |
| 3 | 輸出完整性 | 所有交付物已產出、格式正確、非空白 |
| 4 | 標準合規 | 產出引用的標準版本正確 |
| 5 | 術語一致 | 專案術語、縮寫與 glossary 一致 |
| 6 | 跨步驟一致 | 各步驟產出間無矛盾（如數量、SL等級） |
| 7 | 依賴追溯 | 外部依賴 SK 的輸入已驗證可用 |

---

## 8. 人類審核閘門

完成所有工作步驟後，暫停並向使用者提交審核：

```
知識與能力管理已完成。
📋 執行範圍：7 個工程步驟（SK-D11-008, SK-D11-009, SK-D11-010, SK-D11-011, SK-D11-012, SK-D11-014, SK-D11-021）
📊 交付物清單：
  - Standards library (centralized, versioned repository):
  - Design templates (architecture patterns, security zone templates, network segmentation templates)
  - Technical standards (naming conventions, notation standards, technical decision documentation format)
  - Process standards (design review procedures, design change management process, approval workflow)
  - Reference architectures (proven solutions for common system types: greenfield SCADA, brownfield integration, distributed control)
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
| Domain | D11 (Governance & Process) |
| SK 覆蓋 | SK-D11-008, SK-D11-009, SK-D11-010, SK-D11-011, SK-D11-012, SK-D11-014, SK-D11-021 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D11-008 | Lessons Learned Management | 經驗學習管理 | - Lessons collection becoming bureaucratic burden reducing p |
| SK-D11-009 | Technical Knowledge Base Development | 技術知識庫建置 | - Knowledge base becoming outdated or stale without maintena |
| SK-D11-010 | Internal Design Standards Maintenance | 內部設計標準維護 | Maintain the library of internal design standards, templates |
| SK-D11-011 | Engineering Competency Framework Development | 工程能力框架建立 | Develop and maintain the engineering competency framework th |
| SK-D11-012 | Engineering Training Program Management | 工程培訓計畫管理 | Plan, execute, and manage the annual engineering training pr |
| SK-D11-014 | Personnel Security Qualification Management |  | Personnel security qualification management is a foundationa |
| SK-D11-021 | Role KPI Evidence Collection & Scoring |  | Role KPI Evidence Collection & Scoring operationalizes the G |

<!-- Phase 5 Wave 2 deepened: SK-D11-008, SK-D11-009, SK-D11-010, SK-D11-011, SK-D11-012, SK-D11-014, SK-D11-021 -->