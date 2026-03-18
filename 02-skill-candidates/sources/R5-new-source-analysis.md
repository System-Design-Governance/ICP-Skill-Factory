# R5 New Source Document Analysis — Forensic Report

**Date:** 2026-03-13
**Version:** R5-v2 (governance-corrected)
**Analyst:** Claude (Opus 4.6) + Victor Liu
**Trigger:** 16 new source documents (ID04–ID14, ID21–ID25) + 2 governance repositories (GOV-SD, GOV-SDP)

---

## 0. Source Authority Hierarchy

> **Critical Design Decision (R5-ADR-001):** Source documents are classified into three authority tiers. When governance-level sources conflict with dummy project documents, the governance source prevails.

| Tier | Category | Source IDs | Authority | Usage in Skill Design |
|------|----------|-----------|-----------|----------------------|
| **Tier 1** | ICP Design Department Governance | GOV-SD, GOV-SDP | **Authoritative** — defines actual gate processes, roles, RACI, risk methodology, KPI evidence model | Skill behavior rules, acceptance criteria, role boundaries, lifecycle gates |
| **Tier 2** | Dummy Project Deliverables | ID04–ID14 | **Exemplar** — shows document types, format conventions, and general content direction for IEC 62443-2-4 compliance artifacts | H+ deliverable examples, document structure templates, output format references |
| **Tier 3** | ICP Organizational Procedures | ID21–ID25 | **Contextual** — org-level ISO/ISMS procedures that constrain but do not define design department governance | Environmental constraints, cross-department interface points |

**Implication:** The Gate 0–3 framework, 7 department roles, integrated risk assessment methodology (IEC 62443-3-2 + FMEA + HAZOP), and KPI evidence model come from Tier 1, NOT from the dummy project. ID04–ID14 merely illustrate what the deliverables look like, not how governance actually operates.

---

## 1. Source Document Register Update

### Group T1 — ICP Design Department Governance (Tier 1: Authoritative)

| Source ID | Document Title | Location | Key Content |
|-----------|---------------|----------|-------------|
| GOV-SD | System Design Governance Framework | source-documents/system-design/docs/zh-TW/ (7 files) | Gate 0–3 framework, RACI matrix, integrated risk assessment (IEC+FMEA+HAZOP), residual risk management, SL decision lifecycle, 12-item Gate 3 delivery checklist, dispute escalation, external unit interface |
| GOV-SDP | System Design People Handbook | source-documents/system-design-people/docs/zh-TW/ (11 files) | Department mandate (company-level technical authority), 7 role definitions with JDs, KPI evidence model (6+ KPIs per role with SMART targets), RCW/AF/PVF scoring formula, annual governance cycle, bonus mechanism, multi-role aggregation |

### Group T2 — Dummy Project Deliverables (Tier 2: Exemplar)

| Source ID | Document Title | Version | Pages | IEC 62443 Lifecycle | Primary Domain Impact |
|-----------|---------------|---------|-------|--------------------|-----------------------|
| ID04 | Security Management Plan | v1.0 | 15 | R0–R3 | D01.3, D09, D10, D11 |
| ID05 | Security Vendor Management Plan | v1.0 | 16 | R0–R4 | D01.6, D11 |
| ID06 | SI/SM Project Security Management Plan | v1.0 | 45+ | R0–R5 | D01.3, D11, D14 |
| ID07 | Security Policies and Procedures Plan | v1.0 | 46+ | R1–R4 | D01.5, D11.2 |
| ID08 | Data Flow Diagram | v1.0 | 12 | R1–R2 | D02.2 |
| ID09 | Inventory Asset List | v1.0 | 2 | R0–R1 | D01.2 |
| ID10 | Simple Network Diagram | v1.0 | 8 | R1 | D02.1 |
| ID11 | Threat and Risk Assessment Report | v1.0 | 27 | R1–R2 | D01.2 |
| ID12 | Security Functional Description Specifications | v1.3 | 97 | R3 | D01.5, D09.1 |
| ID13 | IACS Automation Solutions Asset Hardening | v1.0 | 12 | R3 | D01.5 |
| ID14 | OT Security Inspection and Test Protocol | v1.0 | 33 | R3 | D08.1, D08.2, D08.4 |

### Group T3 — ICP Organizational Procedures (Tier 3: Contextual)

| Source ID | Document Title | Version | Pages | Primary Domain Impact |
|-----------|---------------|---------|-------|-----------------------|
| ID21 | QP-02 Personnel and Training Management Procedure | v3.0 | 6 | D11.6 |
| ID22 | QP-07 Procurement and Supplier Management Procedure | v2.0 | 9 | D01.6 |
| ID23 | ISMS-P-03 Information Asset Management Procedure | v1.1 | 18 | D01.2, D11 |
| ID24 | ISMS-P-09 Information Security Incident Reporting and Response | v1.1 | 18 | D01.4 |
| ID25 | MF-AM-07-09 Mutual Non-Disclosure Agreement (NDA) | v1.0 | 3 | D11, D14 |

---

## 2. Phase 1 Domain Map Impact Assessment

### 2.1 Domain Structure Verdict: NO NEW DOMAINS REQUIRED; 2 SUBDOMAIN ENRICHMENTS

The existing 14 domains absorb all new sources. However, the governance framework reveals capability depth that enriches subdomain descriptions significantly, particularly in D11 (Governance) and D14 (Pre-Gate Engineering).

**Structural impact summary:**
- ID04–ID14 (Tier 2) are instantiations of skills already mapped — no structural change
- ID21–ID25 (Tier 3) ground existing D11 and D01.6 candidates — no structural change
- GOV-SD + GOV-SDP (Tier 1) reveal governance depth that was previously inferred but not documented — enriches D01.2, D11, D14 significantly

### 2.2 Subdomain Description Enrichments

#### Enrichments from Tier 1 Governance (Authoritative — behavior-defining)

| Subdomain | Current Description | Governance Enrichment |
|-----------|--------------------|-----------------------|
| D01.2 | 風險評估與威脅建模 | GOV-SD mandates **triple-method** integrated risk assessment: IEC 62443-3-2 + FMEA (RPN: S×O×D) + HAZOP (guide words). Risk source IDs must be traceable (T-XXX, FM-XXX, HAZ-XXX). Gate 1 Lite → Gate 3 Complete upgrade path. |
| D01.3 | 安全合規管理 | GOV-SD defines SL Decision Lifecycle across all 4 gates: Gate 0 propose → Gate 1 confirm → Gate 2 re-evaluate → Gate 3 validate. Non-compliance requires SL downgrade (not waiver). |
| D08.4 | 測試管理 | GOV-SD Gate 3 requires 12-item delivery checklist and residual risk 20% sampling verification — these are quality gates for testing, not just test execution. |
| D11.1 | 治理架構 | GOV-SD defines 4-gate control framework (Gate 0–3) with explicit blocking conditions per gate. GOV-SDP defines department as company-level technical authority (not execution unit). |
| D11.2 | 標準管理 | GOV-SDP establishes standards ownership system (each standard has assigned owner role), exception ruling process (legitimate causes enumerated), and dispute escalation (L1→L2→L3 with SLAs). |
| D11.3 | 組織管理 | GOV-SDP defines 7 functional roles with RACI mapping across all gates. Role KPIs are accountability-derived (not activity-based). Annual governance cycle with data freeze, settlement, and CRM mapping. |
| D11.6 | 工程能力管理 | GOV-SDP provides SMART KPI definitions per role, RCW scoring formula, AF allocation, PVF verification, bonus mechanism with safeguards. |
| D14.1 | 需求分析 | GOV-SD Pre-Gate 0 boundary: discussions before Gate 0 approval do NOT constitute formal requirement acceptance, resource commitment, or delivery obligation. |
| D14.3 | 可行性評估 | GOV-SD defines Pre-Gate Design Support role producing 5 Gate 0 inputs: requirement clarification record, risk pre-disclosure list, feasibility assessment, CBOM (commercially usable / design non-binding), concept architecture (conceptual / non-binding). |
| D14.5 | 商用物料清單 | GOV-SD establishes CBOM vs EBOM distinction: CBOM is commercially quotable but design non-binding; System Architect at Gate 1 can adjust/reject without violating commercial commitment. |

#### Enrichments from Tier 2 Deliverable Exemplars (Format references only)

| Subdomain | Current Description | Exemplar Enrichment |
|-----------|--------------------|--------------------|
| D01.2 | 風險評估與威脅建模 | ID11 provides a TRA report format example with 27-entry threat-vulnerability matrix |
| D01.4 | 安全監控與事件回應 | ID24 adds threat intelligence collection as a discipline within incident response |
| D01.5 | 安全加固與組態管理 | ID07 provides policy/procedure document templates; ID12 provides implementation screenshots; ID13 provides hardening checklists |
| D01.6 | 供應鏈安全 | ID05 provides vendor management plan format; ID22 provides procurement qualification scoring |
| D02.2 | 系統介面設計 | ID08 provides DFD format example with 16 numbered inter-zone data flows |
| D08.1/D08.2 | FAT/SAT | ID14 provides 14-category inspection protocol format spanning FAT, SAT, and SIT |
| D11.6 | 工程能力管理 | ID21 provides training management procedure format with forms |

### 2.3 Boundary Rules

**BOUNDARY-007: FAT / SAT / SIT Testing Distinction (from ID14, confirmed by GOV-SD Gate 3)**
- **FAT** (D08.1) = Factory testing at vendor premises, pre-shipment
- **SAT** (D08.2) = Site acceptance testing after installation at project site
- **SIT** (new explicit category under D08.2) = End-to-end integration testing with employer's existing systems; requires employer participation
- GOV-SD Gate 3 delivery checklist requires SIT completion evidence before handover

**BOUNDARY-008: Data Classification vs. Asset Classification (from ID23, GOV-SD)**
- **D01.2** = Physical/logical asset identification, criticality, network mapping (per-device)
- **D11 / D01.5** = Data classification policy (per-information-type: Public/Internal/Confidential/Restricted)
- Boundary: Asset classification is per-device → D01.2; Data classification is per-information-type → D11

**BOUNDARY-009: Design-Time vs. Execution-Time Authority (from GOV-SD) [NEW]**
- **Design-time** (Pre-Gate 0 through Gate 3) = System Design Department authority. Skills in this scope define design standards, gate readiness criteria, and risk methodology.
- **Execution-time** (Post-Gate 3 handover) = Project execution unit authority. System Design Department has no execution-time responsibility.
- Gate 3 handover creates a clean responsibility transfer boundary: design approval ≠ risk acceptance (separate signers).

**BOUNDARY-010: CBOM vs. EBOM (from GOV-SD) [NEW]**
- **CBOM** (D14.5) = Produced by Pre-Gate Design Support; commercially quotable; design non-binding. Status flow: Draft → Quoted → Gate 0 Approved.
- **EBOM** (D01.x or D14.x) = Produced by System Architect at Gate 1+; design-binding; may override CBOM content.
- CBOM↔EBOM delta is business unit responsibility, NOT design department responsibility.

---

## 3. Phase 2 Skill Candidate Impact

### 3.1 New Skill Candidates from Governance Framework (Tier 1) — 8 new

These candidates emerge from the actual governance framework and would NOT surface from dummy project analysis alone.

| Proposed SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|----------------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D01-035 | Integrated Risk Assessment Execution (IEC+FMEA+HAZOP) | 整合風險評估執行 | D01.2 | ANA | R1,R2 | GOV-SD (triple-method mandatory) | H |
| SC-D01-036 | Risk Source Traceability & Residual Risk Register | 風險溯源與殘餘風險登錄 | D01.2 | ANA | R1–R3 | GOV-SD (T-XXX/FM-XXX/HAZ-XXX coding; Gate 3 20% sampling) | H |
| SC-D11-017 | Gate Review Governance & Blocking Condition Verification | 階段審查治理與阻斷條件驗證 | D11.1 | GOV | R0–R3 | GOV-SD (4-gate blocking conditions; 12-item Gate 3 checklist) | H |
| SC-D11-018 | Design Quality & Traceability Verification | 設計品質與追溯性驗證 | D11.3 | VER | R1,R3 | GOV-SD (Design QA role; traceability matrix; document register) | H |
| SC-D11-019 | Standards Ownership & Exception Arbitration | 標準歸屬與例外裁定 | D11.2 | GOV | R0–R5 | GOV-SDP (standards ownership system; exception ruling; L1-L2-L3 escalation) | H |
| SC-D11-020 | Design Change Impact Analysis & SL Recertification | 設計變更影響分析與SL重認證 | D11.2 | ANA | R2 | GOV-SD (Gate 2 triggers; SL Decision Record update; zone/conduit change logic) | H |
| SC-D11-021 | Role KPI Evidence Collection & Scoring | 角色KPI證據收集與評分 | D11.6 | MGT | R0–R5 | GOV-SDP (SMART KPIs; RCW/AF/PVF formula; bonus mechanism) | M |
| SC-D14-018 | Pre-Gate 0 Requirement Clarification & Feasibility Input | Pre-Gate 0 需求釐清與可行性輸入 | D14.3 | ANA | Pre-R0 | GOV-SD (5 Gate 0 inputs; non-binding boundary; responsibility handover within 15 days) | H |

### 3.2 New Skill Candidates from Deliverable Exemplars (Tier 2) — 15 new

These candidates were identified from dummy project documents as deliverable-type skills with format examples available.

| Proposed SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|----------------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D01-029 | Security Management Plan Development | 安全管理計畫撰寫 | D01.3 | DOC | R0,R1 | ID04 (Tier 2 format example) | H |
| SC-D01-030 | Security Policies and Procedures Plan Development | 安全政策與程序計畫撰寫 | D01.5 | DOC | R1,R2 | ID07 (Tier 2 format example); ID01 §7.1.1.4 | H |
| SC-D01-031 | Vendor Security Management Plan Development | 供應商安全管理計畫撰寫 | D01.6 | DOC | R0,R1 | ID05 (Tier 2 format example); ID01 §7.1.1.2 | H |
| SC-D01-032 | Threat Intelligence Collection and Analysis | 威脅情資蒐集與分析 | D01.4 | ANA | R4 | ID24 §5.3–5.4 (Tier 3) | H |
| SC-D01-033 | Data Classification Policy Development | 資料分類政策制定 | D01.5 | GOV | R1 | ID23 (Tier 3); GOV-SD BOUNDARY-008 | H |
| SC-D01-034 | Security Solution Integration Plan Development | 安全解決方案整合計畫撰寫 | D01.5 | DOC | R3 | ID04 §5.0 (Tier 2 Gate 3 deliverable) | M |
| SC-D08-013 | Site Integration Test (SIT) Protocol Development | SIT 測試協定撰寫 | D08.2 | DOC | R3 | ID14 (Tier 2 SIT as distinct phase) | H |
| SC-D08-014 | Security Inspection and Test Protocol Development | 安全檢驗測試協定撰寫 | D08.4 | DOC | R3 | ID14 (Tier 2; 14-category example) | H |
| SC-D09-009 | Hardening Recommended Practices Document | 加固建議實踐文件撰寫 | D09.1 | DOC | R3 | ID13 (Tier 2 format example) | H |
| SC-D10-007 | Permit to Work (PtW) Process Management | 工作許可流程管理 | D10.2 | MGT | R3,R4 | ID04 §12.0 (Tier 2) | M |
| SC-D11-013 | Information Asset Classification and Grading | 資訊資產分類分級 | D11.3 | GOV | R0,R4 | ID23 (Tier 3 procedure) | H |
| SC-D11-014 | Personnel Security Qualification Management | 人員安全資格管理 | D11.6 | MGT | R0–R5 | ID21 (Tier 3 procedure); ID06 §5.4 | H |
| SC-D11-015 | Procurement Security Requirements Integration | 採購安全需求整合 | D11.2 | GOV | R0,R1 | ID22 (Tier 3 procedure) | H |
| SC-D11-016 | SI/SM Project Security Management Plan Development | SI/SM 專案安全管理計畫撰寫 | D11.2 | DOC | R0 | ID06 (Tier 2; 45+ pages) | H |
| SC-D14-017 | NDA and Confidentiality Agreement Management | NDA 與保密協議管理 | D14.1 | MGT | Pre-R0 | ID25 (Tier 3 template) | H |

### 3.3 Confidence Upgrades (20 existing candidates → H+)

H+ confidence is awarded when a **Tier 2 deliverable example** exists AND the skill's behavioral rules are confirmed by **Tier 1 governance**. The H+ designation now carries dual meaning: format exemplar available + governance-grounded behavior.

| SC ID | Skill Name | Old Conf. | New Conf. | Tier 2 Exemplar | Tier 1 Governance Confirmation |
|-------|-----------|-----------|-----------|----------------|-------------------------------|
| SC-D01-005 | Asset Inventory Development | H | H+ | ID09: 30-column asset inventory with zone mapping | GOV-SD: Gate 1 prerequisite; feeds Zone/Conduit diagram |
| SC-D01-006 | TRA (Preliminary) | H | H+ | ID11: 27-entry threat-vulnerability matrix | GOV-SD: Gate 1 Lite assessment path; IEC 62443-3-2 method |
| SC-D01-007 | Detailed Risk Assessment | H | H+ | ID11: DTRA framework with impact analysis | GOV-SD: Gate 3 Complete assessment (mandatory upgrade from Lite) |
| SC-D01-016 | Incident Response Procedure Development | H | H+ | ID24: 4-level classification procedure | — (org procedure, not design governance) |
| SC-D01-019 | Endpoint Hardening Implementation | H | H+ | ID12 §4–5: Cortex XDR screenshots; ID13: 3-category checklists | GOV-SD: Gate 3 countermeasure evidence required |
| SC-D01-020 | Account and Access Control Management | H | H+ | ID07 §4.0: account management policy with role matrix | GOV-SD: SR verification per FR-SR mapping |
| SC-D01-021 | Security Patch Management | H | H+ | ID07 §8.0: change and patch management procedure | GOV-SD: Gate 2 change management trigger |
| SC-D01-022 | Backup and Restore Procedure Design | H | H+ | ID07 §6.0: backup/restore procedure | — |
| SC-D01-023 | Malware Protection Implementation | H | H+ | ID07 §7.0 + ID12 §4.1–4.2: Palo Alto detail | GOV-SD: SR verification per FR-SR mapping |
| SC-D01-024 | Vendor Security Risk Assessment | H | H+ | ID05: vendor management plan; ID22: procurement scoring | GOV-SD: supply chain risk within Gate 0 scope |
| SC-D02-004 | Data Flow Diagram Development | H | H+ | ID08: 16 numbered inter-zone data flows | GOV-SD: Zone/Conduit diagram is Gate 1 mandatory |
| SC-D02-011 | Simple Network Diagram Development | H | H+ | ID10: Purdue level mapping | GOV-SD: network architecture as Gate 1 input |
| SC-D08-001 | FAT Procedure Development | H | H+ | ID14: 14-category inspection protocol | GOV-SD: testing evidence in Gate 3 checklist |
| SC-D08-004 | Site Acceptance Testing Execution | H | H+ | ID14: SAT-specific categories | GOV-SD: SAT completion for Gate 3 |
| SC-D08-005 | Security Acceptance Testing Execution | H | H+ | ID14: SR 1.01–SR 2.05+ cybersecurity tests | GOV-SD: SR verification = Gate 3 blocker |
| SC-D08-009 | Penetration Testing Execution | H | H | ID14: vulnerability scanning category | — (not governance-confirmed as mandatory) |
| SC-D09-002 | Security Functional Description Specification | H | H+ | ID12: 97-page IEC 62443-2-4 SP mapping | GOV-SD: design specification feeds SR checklist |
| SC-D11-011 | Engineering Competency Framework Development | H | H+ | ID21: QP-02 training procedure | GOV-SDP: role-based competency model with KPIs |
| SC-D11-012 | Engineering Training Program Management | H | H+ | ID21: annual training plan, evaluation | GOV-SDP: annual governance cycle includes competency review |
| SC-D01-013 | Gate Review Preparation and Execution | H | H+ | ID04 §10.0: Gate 1/2/3 deliverable mapping | GOV-SD: authoritative gate framework (4 gates with blocking conditions) |

### 3.4 Governance-Driven Upgrades to Existing Candidates (Non-H+ Changes)

The Tier 1 governance framework also enriches existing candidates that do NOT have Tier 2 exemplars:

| SC ID | Skill Name | Change | Governance Source |
|-------|-----------|--------|-------------------|
| SC-D01-001 | Zone/Conduit Architecture Design | Lifecycle confirmed: Gate 1 mandatory deliverable | GOV-SD §Gate 1 |
| SC-D01-010 | SL-T Assessment | SL Decision Lifecycle added: Gate 0 propose → Gate 1 confirm → Gate 2 re-evaluate → Gate 3 validate | GOV-SD |
| SC-D01-011 | IEC 62443 Compliance Gap Analysis | Now must reference FR-SR verification status (Implemented/Planned/N/A with sign-off) | GOV-SD Appendix A |
| SC-D14-003 | Technical Feasibility Assessment | Governance confirms Pre-Gate Design Support role as owner; output = advisory (non-binding) | GOV-SD Pre-Gate 0; GOV-SDP |
| SC-D14-005 | CBOM Development | CBOM vs EBOM distinction formalized; CBOM = commercially quotable / design non-binding | GOV-SD BOUNDARY-010 |
| SC-D14-010 | Tender Security Requirements Definition | Must reference Gate 0 quality thresholds (comprehensibility, evaluability, accountable owner, scope stability) | GOV-SD §Gate 0 |
| SC-D14-015 | Gate 0 Decision Package Assembly | 5 mandatory inputs defined; Pre-Gate Design Support KPIs apply | GOV-SD; GOV-SDP |
| SC-D11-002 | Stage-Gate Review Facilitation | Now replaced/superseded by SC-D11-017 (governance-authoritative gate review) | GOV-SD |

### 3.5 Near-Duplicate Check: Governance vs. Existing Candidates

| Pair | Existing | New Governance Candidate | Verdict | Resolution |
|------|----------|------------------------|---------|------------|
| 1 | SC-D01-006 TRA (Preliminary) | SC-D01-035 Integrated Risk Assessment (IEC+FMEA+HAZOP) | NOT DUPLICATE | SC-D01-006 = IEC 62443-3-2 only (ILRA). SC-D01-035 = triple-method integration (IEC+FMEA+HAZOP). SC-D01-035 is the governance-mandated comprehensive method. |
| 2 | SC-D01-013 Gate Review Prep | SC-D11-017 Gate Review Governance | NOT DUPLICATE | SC-D01-013 = preparing deliverables for a gate review (execution skill). SC-D11-017 = defining and enforcing gate blocking conditions (governance skill). |
| 3 | SC-D11-002 Stage-Gate Review Facilitation | SC-D11-017 Gate Review Governance | SUPERSEDE | SC-D11-017 is governance-grounded and more specific. **Resolution: SC-D11-002 superseded by SC-D11-017. Keep SC-D11-002 as alias referencing SC-D11-017.** |
| 4 | SC-D14-003 Technical Feasibility Assessment | SC-D14-018 Pre-Gate 0 Requirement Clarification | NOT DUPLICATE | SC-D14-003 = feasibility assessment output. SC-D14-018 = full Pre-Gate 0 input preparation (5 deliverables including feasibility). SC-D14-018 is a composition that includes SC-D14-003. |

### 3.6 Post-Update Statistics

| Metric | Before R5 | After R5 | Delta |
|--------|----------|---------|-------|
| Source documents | 3 + PRAC | 19 + PRAC + 2 GOV | +18 |
| Source tiers | 1 | 3 | +2 tiers |
| Domains | 14 | 14 | 0 |
| Subdomains | 73 | 73 | 0 |
| Boundary rules | 6 | 10 | +4 |
| Skill candidates (pre-norm) | 150 | 173 | +23 (15 Tier 2 + 8 Tier 1) |
| Skill candidates (post-norm) | 149 | 171 | +22 (SC-D11-002 superseded by SC-D11-017) |
| H confidence | 73 | 75 | +21 new H, −19 upgraded to H+ = net +2 |
| H+ confidence (with exemplar + governance) | 0 | 19 | +19 (upgraded from H) |
| H + H+ total | 73 | 94 | +21 net |
| M confidence | 64 | 67 | +3 new M |
| L confidence | 13 | 13 | 0 |
| ADRs | 6 | 7 | +1 (R5-ADR-001) |

---

## 4. Key Insights

### 4.1 The "Deliverable Exemplar" Pattern (from Tier 2)

Tier 2 documents provide concrete examples for skills previously described only abstractly. For H+ candidates, Phase 3 skill authors can reference:
- **Exemplar reference**: ID document as completed output example
- **Structure template**: Document TOC as output format guide
- **Acceptance criteria grounding**: Content quality baseline from the example

### 4.2 The "Governance Grounding" Pattern (from Tier 1) [NEW]

Tier 1 governance documents provide behavioral rules that constrain HOW skills execute, not just WHAT they produce. For governance-enriched candidates:
- **Gate alignment**: Which gate(s) the skill feeds into, and what blocking conditions apply
- **Role authority**: Which of the 7 roles owns the skill, and RACI assignments
- **Methodology mandate**: Whether the skill must use specific methods (e.g., triple risk assessment)
- **Acceptance authority**: Who can accept the skill's output (may differ from who produces it)
- **KPI linkage**: Which role KPIs measure this skill's quality

This pattern should be formalized in Phase 3 skill definitions as required fields for any D11/D14 skill and recommended fields for all gate-aligned skills.

### 4.3 Governance vs. Dummy Project Divergence Points

Key areas where Tier 1 governance OVERRIDES naive readings of Tier 2 dummy project:

| Topic | Dummy Project (ID04–ID14) Implies | Actual Governance (GOV-SD/SDP) States |
|-------|-----------------------------------|--------------------------------------|
| Risk assessment | Single-method TRA (IEC 62443 only) | Triple-method mandatory: IEC + FMEA + HAZOP |
| Gate framework | 3 gates (Gate 1/2/3) | 4 gates (Gate 0/1/2/3) with Pre-Gate 0 boundary |
| CBOM | Design input | Commercially quotable but design non-binding; EBOM supersedes |
| Risk acceptance | Implied in project management | Explicit authority hierarchy: PM → PM+Security → PM+Security+Business → Engineering Management |
| Role structure | Generic PM/security roles | 7 defined roles with RACI, KPIs, dispute escalation |
| Pre-gate activity | Not visible | Explicit Pre-Gate Design Support role with 5 deliverables, non-binding boundary |

---

## 5. Known Gaps Remaining

1. **ID12 pages 21–97 not fully extracted**: Additional security countermeasure implementations may yield granular sub-skills.

2. **ID06 pages 16–45 not fully extracted**: Detailed security program activities may enrich D11 and D14 candidates.

3. **ID07 pages 16–46 not fully extracted**: Additional procedures (logging/monitoring) may deepen D01.4 candidates.

4. **project-governance folder not deep-read**: Power Platform governance documents and forensic reports in `source-documents/project-governance/` may contain project execution governance that complements design governance.

5. **No IEC 62443-2-4 SP requirement traceability matrix**: ID12 references specific SP requirements but we lack a master SP mapping for compliance coverage analysis.

6. **GOV-SD appendices not fully mapped**: Appendix A (FR-SR mapping table), Appendix C (residual risk template), Appendix D (FMEA/HAZOP worksheets) contain detailed templates that could yield additional format-level skill refinements.
