---
name: process-development
description: >
  流程開發與優化。
  Develop, maintain, and govern Standard Operating Procedures (SOPs) for engineering activities across all IEC 62443 project lifecycle stages (R0 throug。- Analysis paralysis delaying implementation actions。Integrate cybersecurity requirements into proc
  MANDATORY TRIGGERS: 採購安全需求整合, SI/SM 專案安全管理計畫撰寫, 標準歸屬與例外裁定, 流程效率分析, 工程 SOP 制定, 流程開發與優化, ID06, SI/SM Project Security Management Plan Development, escalation, IEC-62443-2-4, procurement-security, SM, security-management-plan, Engineering SOP Development.
  Use this skill for process development tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 流程開發與優化

本 Skill 整合 5 個工程技能定義，提供流程開發與優化的完整工作流程。
適用領域：Governance & Process（D11）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D01-006, SK-D01-007, SK-D01-024, SK-D08-001, SK-D11-001

---

## 1. 輸入

- Project Charter and Security Policy framework (from project initialization, per ID01 §6.5.1.2)
- Stakeholder roles and responsibilities matrix (RACI, from SK-D11-001)
- Existing SOP templates and organizational process standards
- Regulatory, contractual, and compliance requirements (from Scope Definition, ID01 §6.5.1.1)
- Technical skill requirements and work instructions from SMEs across D01–D14 domains
- Process change requests from project teams, audit findings, or management reviews
- Security architecture and security level requirements from D01 design (specifically: Zone/Conduit Architecture SK-D01-001, Network Security Device Req
- Procurement Security Procedure ID22 (organizational standard for security in vendor selection, RFQ/RFP requirements, vendor agreements, supply chain r
- Preliminary vendor list and product options (identified during architectural design phase)
- Risk assessment findings relevant to supply chain and third-party components (from SK-D01-006 ⏳)
- Security control requirements and specifications (from detailed design, D01 domain skills)
- Vendor certifications and security claims documentation (ISO 27001, IEC 62443, NIST compliance, etc.)

---

## 2. 工作流程

### Step 1: 工程 SOP 制定
**SK 來源**：SK-D11-004 — Engineering SOP Development

執行工程 SOP 制定：Develop, maintain, and govern Standard Operating Procedures (SOPs) for engineering activities across all IEC 62443 project lifecycle stages (R0 throug

**本步驟交付物**：
- SOP Master Document Suite**: complete set of engineering SOPs organized by domain (D01–D14) and lifecycle stage (R0–R5), each in template format with:
- Purpose, scope, applicability (which roles, which lifecycle stages)
- Prerequisites and entry criteria

### Step 2: 流程效率分析
**SK 來源**：SK-D11-005 — Process Efficiency Analysis

執行流程效率分析：- Analysis paralysis delaying implementation actions

### Step 3: 採購安全需求整合
**SK 來源**：SK-D11-015 — Procurement Security Requirements Integration

執行採購安全需求整合：Integrate cybersecurity requirements into procurement processes per organizational procurement security procedure (ID22 Tier 3 standard), ensuring tha

**本步驟交付物**：
- Security Requirements Specification for Procurement (SRSP)**: document translating security control requirements into procurement language, including:
- Required vendor certifications/attestations (ISO 27001, IEC 62443 Curve certification, NIST compliance, etc.)
- Technical security specifications for products (e.g., encryption algorithms, key management, logging capabilities, FIPS compliance)

### Step 4: SI/SM 專案安全管理計畫撰寫
**SK 來源**：SK-D11-016 — SI/SM Project Security Management Plan Development

執行SI/SM 專案安全管理計畫撰寫：Develop the comprehensive Security Management Plan (SMP) for System Integrator (SI) and Security Maintenance (SM) projects per IEC 62443-2-4, using ID

**本步驟交付物**：
- Security Management Plan document (per ID06 structure, 45+ pages):
- Executive summary: project security governance overview, key stakeholders, lifecycle applicability
- Security organization and roles: organizational structure, role definitions, responsibilities matrix (RACI: Responsible, Accountable, Consulted, Infor

### Step 5: 標準歸屬與例外裁定
**SK 來源**：SK-D11-019 — Standards Ownership & Exception Arbitration

執行標準歸屬與例外裁定：Manage the ownership, maintenance, and exception arbitration for engineering standards used across all projects, per GOV-SDP governance framework. Thi

**本步驟交付物**：
- Standards Register (living document): inventory of all active standards, with fields: standard ID, standard name, version, owner name/role, effective 
- Standards Owner Assignment Matrix: ownership assignments per standard, with roles and contact information; covers all standards in register
- Exception Request Decision Record (L1/L2/L3 per request): exception request ID, standard being deviated from, deviation description, business justific

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | SOP Master Document Suite**: complete set of engineering SOPs organized by domain (D01–D14) and lifecycle stage (R0–R5), each in template format with: | 依需求 |
| 2 | Purpose, scope, applicability (which roles, which lifecycle stages) | 依需求 |
| 3 | Prerequisites and entry criteria | 依需求 |
| 4 | Step-by-step process flow with decision points | 依需求 |
| 5 | Roles and responsibilities (who performs, who reviews/approves) | 依需求 |
| 6 | Quality acceptance criteria (observable, measurable) | 依需求 |
| 7 | Security Requirements Specification for Procurement (SRSP)**: document translating security control requirements into procurement language, including: | 依需求 |
| 8 | Required vendor certifications/attestations (ISO 27001, IEC 62443 Curve certification, NIST compliance, etc.) | 依需求 |
| 9 | Technical security specifications for products (e.g., encryption algorithms, key management, logging capabilities, FIPS compliance) | 依需求 |
| 10 | Vendor security evaluation criteria and scoring matrix (security features, audit results, industry reputation, response time to vulnerabilities) | Markdown |
| 11 | Supply chain integrity requirements (secure delivery, tamper detection, software bill of materials (SBOM) requirements) | 依需求 |
| 12 | Support and vulnerability response SLA expectations | 依需求 |

---

## 4. 適用標準

- IEC 62443-2-1: Security Management System — establishes requirements for documented procedures and process control
- IEC 62443-3-2 §7.1.1: Specification of Security Requirements — procedures and controls required for security engineering
- ISO 9001:2015 §4.4: Determination of Scope, §8.1 Operational Planning and Control — organizational process documentation
- PRAC: Industry standard practice for IEC 62443 governance SOP structures and lifecycle management
- Tier**: T3-Skill
- Maturity Level**: Active
- Version**: 1.0.0
- Created Date**: 2026-03-16
- Owner Role**: Head of System Design (GOV-SDP)
- IEC 62443-2-1 §5.2.1 (Supply Chain Security) and §7.2 (Third-Party Risk Management) — framework for managing security th

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | SOP Master Suite covers all mandatory activities for at least two consecutive li | ✅ 已驗證 |
| 2 | Every SOP includes explicit entry criteria, step-by-step process, decision rules | ✅ 已驗證 |
| 3 | Every SOP specifies roles with RACI accountability (Responsible, Accountable, Co | ✅ 已驗證 |
| 4 | Version Control Log is current within 5 business days of any SOP change; all ver | ✅ 已驗證 |
| 5 | 100% of in-scope stakeholders have completed SOP training with documented acknow | ✅ 已驗證 |
| 6 | Compliance monitoring records for the past 90 days exist, showing at least one s | ✅ 已驗證 |
| 7 | All SOPs are cross-referenced to applicable standards sections (IEC 62443, proje | ✅ 已驗證 |
| 8 | Complete process maps documenting current-state workflows | ✅ 已驗證 |
| 9 | Identified bottlenecks with root cause analysis | ✅ 已驗證 |
| 10 | Quantified cycle time reduction opportunities | ✅ 已驗證 |
| 11 | Value stream analysis with waste elimination strategies | ✅ 已驗證 |
| 12 | Prioritized improvement recommendations with expected impact estimates | ✅ 已驗證 |
| 13 | Baseline metrics and efficiency measurements established | ✅ 已驗證 |
| 14 | Clear handoff to SK-D11-004 with actionable improvement recommendations | ✅ 已驗證 |
| 15 | Stakeholder alignment on priority improvement initiatives | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D11-004 | | Junior (< 2 yr) | 10–15 person-days per SOP suite (R0–R2 scope) | Requires significant SME review  |
| SK-D11-004 | | Senior (5+ yr) | 5–8 person-days per SOP suite | Leverages templates, can rapidly incorporate mult |
| SK-D11-004 | Notes: Full R0–R5 portfolio (6 lifecycle suites) typically requires 60–90 person-days for an establi |
| SK-D11-015 | | Junior (< 2 yr) | 6–10 person-days | Developing SRSP and RFQ/RFP appendix; assumes 3–5 primary ven |
| SK-D11-015 | | Senior (5+ yr) | 3–5 person-days | Leverages procurement security templates and vendor scorecard p |
| SK-D11-015 | Notes: Large vendor base (>10 vendors) or highly complex security specifications (e.g., cryptographi |
| SK-D11-016 | | Junior (< 2 yr) | 12–18 person-days | Assumes single-site project, ~50–100 assets, with ID06 templ |
| SK-D11-016 | | Senior (5+ yr) | 6–10 person-days | Same scope; senior leverages prior project SMP and ID06 templa |

---

## 7. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 輸入完整性 | 所有必要輸入文件已讀取並摘要 |
| 2 | 流程覆蓋 | 5 個工作步驟皆已執行並有產出 |
| 3 | 輸出完整性 | 所有交付物已產出、格式正確、非空白 |
| 4 | 標準合規 | 產出引用的標準版本正確 |
| 5 | 術語一致 | 專案術語、縮寫與 glossary 一致 |
| 6 | 跨步驟一致 | 各步驟產出間無矛盾（如數量、SL等級） |
| 7 | 依賴追溯 | 外部依賴 SK 的輸入已驗證可用 |

---

## 8. 人類審核閘門

完成所有工作步驟後，暫停並向使用者提交審核：

```
流程開發與優化已完成。
📋 執行範圍：5 個工程步驟（SK-D11-004, SK-D11-005, SK-D11-015, SK-D11-016, SK-D11-019）
📊 交付物清單：
  - SOP Master Document Suite**: complete set of engineering SOPs organized by domain (D01–D14) and lifecycle stage (R0–R5), each in template format with:
  - Purpose, scope, applicability (which roles, which lifecycle stages)
  - Prerequisites and entry criteria
  - Step-by-step process flow with decision points
  - Roles and responsibilities (who performs, who reviews/approves)
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
| SK 覆蓋 | SK-D11-004, SK-D11-005, SK-D11-015, SK-D11-016, SK-D11-019 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D11-004 | Engineering SOP Development | 工程 SOP 制定 | Develop, maintain, and govern Standard Operating Procedures  |
| SK-D11-005 | Process Efficiency Analysis | 流程效率分析 | - Analysis paralysis delaying implementation actions |
| SK-D11-015 | Procurement Security Requirements Integration | 採購安全需求整合 | Integrate cybersecurity requirements into procurement proces |
| SK-D11-016 | SI/SM Project Security Management Plan Development | SI/SM 專案安全管理計畫撰寫 | Develop the comprehensive Security Management Plan (SMP) for |
| SK-D11-019 | Standards Ownership & Exception Arbitration | 標準歸屬與例外裁定 | Manage the ownership, maintenance, and exception arbitration |

<!-- Phase 5 Wave 2 deepened: SK-D11-004, SK-D11-005, SK-D11-015, SK-D11-016, SK-D11-019 -->