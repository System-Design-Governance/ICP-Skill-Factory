# ICP Skill Factory — Stages A/B/C Consolidated Deliverable

**Project:** Energy Systems Engineering Skill Architecture
**Document:** Skill Factory Repository Framework + Phase 1 Review + Phase 2 Skill Candidate Extraction
**Version:** v1.1 (R2 — D14 added, D10 re-scoped)
**Date:** 2026-03-13
**Author:** Claude (Engineering Skill Architecture Expert)
**Owner:** Victor Liu, ICP

---

## Section 1: Stage A — Repository Framework

### 1.1 Directory Structure

The Skill Factory repository is the single source of truth for all skill governance artifacts. The structure below separates concerns by phase, supports incremental growth, and is compatible with both human navigation and automated tooling.

```
icp-skill-factory/
│
├── 00-governance/
│   ├── skill-governance-workplan.md
│   ├── skill-governance-workplan-zh.md
│   ├── CONVENTIONS.md                    # Naming, ID rules, style guide
│   ├── SCHEMA.md                         # Skill Registry Schema definition
│   ├── CHANGELOG.md                      # Cross-phase change log
│   └── decisions/
│       ├── ADR-001-protection-independence.md
│       ├── ADR-002-data-platform-independence.md
│       ├── ADR-003-engineering-automation.md
│       └── ADR-004-skill-id-pattern.md
│
├── 01-domain-map/
│   ├── phase1-skill-domain-map.md        # Original Phase 1 output (preserved)
│   ├── phase1-review-changelog.md        # Stage B review findings
│   └── phase1-domain-map-approved.md     # Approved map for Phase 2 entry
│
├── 02-skill-candidates/
│   ├── extraction-methodology.md         # How candidates were extracted
│   ├── skill-candidate-inventory.md      # Full inventory grouped by domain
│   ├── duplicate-normalization-review.md # Dedup and normalization analysis
│   └── sources/
│       ├── ID01-extraction-notes.md      # Per-source extraction traceability
│       ├── ID02-extraction-notes.md
│       ├── ID03-extraction-notes.md
│       └── practical-engineering-notes.md
│
├── 03-skill-definitions/                 # Phase 3 (future)
│   ├── template.md
│   └── registry/
│       └── (skill definition files, one per skill)
│
├── 04-dependency-map/                    # Phase 4 (future)
│   ├── dependency-matrix.md
│   ├── composition-patterns.md
│   └── visualizations/
│
├── 05-conflict-analysis/                 # Phase 5 (future)
│   ├── overlap-matrix.md
│   └── boundary-report.md
│
├── 06-refactoring/                       # Phase 6 (future)
│   ├── proposals.md
│   └── architecture-v2.md
│
├── 07-evolution/                         # Phase 7 (future)
│   ├── emerging-skills.md
│   ├── automation-heatmap.md
│   └── governance-process.md
│
└── source-documents/
    ├── ID01__ICP - The SI,SM Project and System Security Management Guideline_Ver1.0_26-05-2025.pdf
    ├── ID02__ICP - The SI,SM Project and System Security Management Guideline – Annexes_Ver1.1_26-05-2025.pdf
    └── ID03__ICP - SI-SM Project Security Management Planning Guideline_Ver1.0_26-05-2025.pdf
```

### 1.2 Directory Design Rationale

Each phase gets a numbered top-level folder (`01-` through `07-`) matching the project work plan. The `00-governance/` folder holds cross-cutting artifacts that govern the entire system. The `source-documents/` folder preserves input materials with their original filenames for audit traceability.

Within each phase folder, the naming convention follows a predictable pattern: the primary deliverable is named after the phase purpose (e.g., `skill-candidate-inventory.md`), supporting analysis is in clearly labeled companion files, and raw working notes go into a `sources/` subfolder when needed.

### 1.3 Initial Operating Files

The following files are created at repository initialization:

| File | Purpose | Status |
|------|---------|--------|
| `00-governance/CONVENTIONS.md` | Naming, ID rules, bilingual conventions | Defined in Section 2 |
| `00-governance/SCHEMA.md` | Skill Registry Schema (20+ fields) | Defined in Section 2 |
| `00-governance/CHANGELOG.md` | Running log of structural decisions | Initialized |
| `01-domain-map/phase1-skill-domain-map.md` | Phase 1 original output | Existing |
| `00-governance/skill-governance-workplan.md` | Project work plan | Existing |

### 1.4 Readiness Checklist

| # | Criterion | Status |
|---|-----------|--------|
| 1 | Directory structure defined and documented | DONE |
| 2 | Skill Registry Schema finalized (20+ fields) | DONE (Section 2) |
| 3 | Skill ID pattern evaluated and proposed | DONE (Section 2) |
| 4 | Naming conventions documented | DONE (Section 2) |
| 5 | Phase 1 domain map reviewed against quality criteria | DONE (Section 3) |
| 6 | Approved domain map baseline established | DONE (Section 4) |
| 7 | Source documents cataloged with extraction notes | DONE (Section 5) |
| 8 | Phase 2 extraction methodology documented | DONE (Section 5) |
| 9 | Skill candidate inventory produced | DONE (Section 6) |
| 10 | Duplicate/normalization review completed | DONE (Section 7) |

---

## Section 2: Skill Registry Schema and ID Rules

### 2.1 Skill ID Pattern — Evaluation and Proposal

Three candidate patterns were evaluated:

**Option A — Flat Sequential**
Format: `SK-0001`, `SK-0002`, ...
Pros: Simple, no hierarchy baked in. Cons: No information carried in the ID; requires lookup for every operation. Poor for human scanning.

**Option B — Hierarchical Dotted (Phase 1 style)**
Format: `D01.2.003` (Domain.Subdomain.Sequence)
Pros: Instantly readable hierarchy; matches existing Phase 1 IDs. Cons: Refactoring a domain or subdomain forces mass ID changes. Tight coupling between taxonomy and identity.

**Option C — Hybrid: Stable Domain Prefix + Sequential Skill Number** ← PROPOSED
Format: `SK-D01-003`
- `SK` = Skill (entity type prefix)
- `D01` = Domain code (stable, rarely changes)
- `003` = Sequential number within that domain (zero-padded, 3 digits)

For skill candidates (pre-validation), use: `SC-D01-017`
- `SC` = Skill Candidate (not yet promoted to SK)

For sub-skills (atomic decomposition of a skill): `SK-D01-003.a`, `SK-D01-003.b`

**Why Option C wins:**

1. Domain prefix provides instant human readability without full lookup
2. Sequential number is stable under subdomain reorganization — if D01.2 merges into D01.1, skills keep their IDs
3. The SC → SK promotion path gives a clear lifecycle signal
4. The `.a` / `.b` sub-skill notation avoids deep nesting while allowing decomposition
5. Zero-padded 3-digit sequence supports up to 999 skills per domain (sufficient for 13 domains × ~15 skills each)

**ADR-004: Skill ID Pattern Decision**
Decision: Adopt Option C (Hybrid: `SK-D01-NNN`) as the canonical Skill ID pattern.
Rationale: Balances readability, stability under refactoring, and lifecycle clarity. The domain prefix is coarse enough to survive taxonomy changes; the sequential number is decoupled from subdomain structure.

### 2.2 Full Entity ID Reference

| Entity | Pattern | Example | Notes |
|--------|---------|---------|-------|
| Domain (Level 1) | `D{nn}` | `D01` | Stable; from Phase 1 |
| Subdomain (Level 2) | `D{nn}.{n}` | `D01.2` | Stable; from Phase 1 |
| Skill Candidate | `SC-D{nn}-{nnn}` | `SC-D01-017` | Pre-validation |
| Skill (Validated) | `SK-D{nn}-{nnn}` | `SK-D01-003` | Promoted from SC |
| Sub-skill (Atomic) | `SK-D{nn}-{nnn}.{a}` | `SK-D01-003.a` | Alphabetic suffix |
| Composition Pattern | `CP-{nnn}` | `CP-001` | Cross-domain patterns |
| Decision Record | `ADR-{nnn}` | `ADR-004` | Architecture decisions |

### 2.3 Naming Conventions

1. **Bilingual requirement**: Every skill has both an English canonical name (used in IDs, APIs, machine contexts) and a Chinese display name (used in UI, reports, training). Example: `SK-D01-003` → EN: "Zone/Conduit Topology Design" / ZH: "Zone/Conduit 拓撲設計"
2. **Name format**: English names use Title Case with no abbreviations except industry-standard ones (SCADA, EMS, DERMS, VPP, HMI, PLC, RTU, SIEM, SBOM, TRA, FAT, SAT, OPC UA)
3. **Verb-first for action skills**: Skills representing actions start with a verb: "Perform TRA", "Design Zone/Conduit Architecture", "Execute FAT Procedure"
4. **Noun-first for knowledge skills**: Skills representing knowledge domains use noun phrases: "IEC 62443 Compliance Framework", "Power System Protection Theory"
5. **No redundant domain prefix in name**: Since the domain is encoded in the ID, the name should not repeat it. Bad: "OT Cybersecurity Risk Assessment". Good: "Risk Assessment and Threat Modeling"

### 2.4 Skill Registry Schema (24 Fields)

| # | Field | Type | Required | Description |
|---|-------|------|----------|-------------|
| 1 | `skill_id` | String | Yes | Canonical ID per §2.2 pattern |
| 2 | `skill_name_en` | String | Yes | English canonical name |
| 3 | `skill_name_zh` | String | Yes | Chinese display name |
| 4 | `domain_id` | FK → Domain | Yes | Parent Level 1 domain (D01–D13) |
| 5 | `subdomain_id` | FK → Subdomain | Yes | Parent Level 2 subdomain (D01.1–D13.4) |
| 6 | `skill_type` | Enum | Yes | One of: Analysis, Design, Engineering, Testing, Documentation, Management, Verification, Governance, Integration, Operations |
| 7 | `tier` | Enum | Yes | One of: T1-Domain, T2-CapabilityGroup, T3-Skill, T4-AtomicSubskill |
| 8 | `description` | Text | Yes | 2–4 sentence scope description |
| 9 | `inputs` | Text[] | Yes | What this skill consumes (documents, data, decisions) |
| 10 | `outputs` | Text[] | Yes | What this skill produces (deliverables, artifacts, states) |
| 11 | `tools` | Text[] | No | Typical tools/platforms used |
| 12 | `standards` | Text[] | No | Applicable standards (IEC 62443, IEEE 2030, etc.) |
| 13 | `iec62443_lifecycle_stage` | Enum[] | No | Applicable stages: R0, R1, R2, R3, R4, R5 |
| 14 | `roles` | Text[] | No | ICP roles that perform this skill (PM, PJS, SAC, STC, TST, VER, VAL, CSA, SYS, DES, etc.) |
| 15 | `dependencies_hard` | FK[] → Skill | No | Skills required before this one can execute |
| 16 | `dependencies_soft` | FK[] → Skill | No | Skills that enhance this one's effectiveness |
| 17 | `automation_potential` | Enum | No | Full, Partial, Human-Only |
| 18 | `maturity` | Enum | Yes | Draft, Active, Deprecated, Retired |
| 19 | `source_documents` | Text[] | Yes | Source traceability (document IDs + section refs) |
| 20 | `confidence` | Enum | Yes | High, Medium, Low — extraction confidence |
| 21 | `owner` | String | No | Person or team responsible |
| 22 | `version` | SemVer | Yes | Skill definition version (e.g., 1.0.0) |
| 23 | `created_date` | Date | Yes | When the skill was first registered |
| 24 | `tags` | Text[] | No | Free-form tags for search/filtering |

### 2.5 Skill Type Taxonomy

| Skill Type | Definition | Example |
|------------|-----------|---------|
| Analysis | Examining data/systems to produce findings | Risk Assessment, Power Flow Analysis |
| Design | Creating specifications, architectures, plans | Zone/Conduit Architecture Design |
| Engineering | Implementing/configuring technical systems | SCADA Database Configuration |
| Testing | Verifying/validating against requirements | FAT Execution, Penetration Testing |
| Documentation | Producing written deliverables | TRA Report Writing, SOP Authoring |
| Management | Coordinating people, processes, resources | Project Security Planning |
| Verification | Independent check of process/output compliance | Security Design Review |
| Governance | Defining/enforcing standards and policies | Security Policy Development |
| Integration | Connecting disparate systems/data | Protocol Gateway Configuration |
| Operations | Ongoing monitoring, maintenance, response | Security Monitoring, Incident Response |

---

## Section 3: Stage B — Review of Phase 1 Domain Map

### 3.1 Review Methodology

The Phase 1 domain map (v1.0, 13 domains, 66 subdomains) was evaluated against 10 quality criteria. Each criterion is scored Pass / Partial / Fail, with specific findings and recommended corrections.

### 3.2 Quality Criteria Assessment

#### Criterion 1: Completeness — Does every engineering capability have a home?

**Score: PARTIAL**

Findings:
- The 13 domains cover the core engineering workflow comprehensively from design through decommissioning.
- **Gap G1**: No explicit home for **Safety Instrumented System (SIS) security** — ID01 §7.4.1.7 and ID02 A.9 §12 describe SIS-specific security skills (SIS network isolation, SIS logic solver security, SIS bypass management). Currently these would scatter across D01, D04, and D05 without a clear subdomain.
- **Gap G2**: No explicit home for **Personnel Security & Competency Management** — ID01 §6.3 and ID03 §5.3.3 describe detailed competency frameworks, security training programs, and background checks. These are not engineering governance (D11) — they are security-program-specific personnel management.
- **Gap G3**: **Decommissioning/Disposal** skills (ID01 §6.5.3: preserve information, sanitize media, dispose hardware) have no clear subdomain. They partially overlap D08 (Testing/Commissioning) and D01 (Security), but neither is a natural fit.

Recommended corrections:
- G1: Add `D01.7 SIS 安全 (Safety Instrumented System Security)` under D01
- G2: Fold into D11 by adding `D11.6 安全能力管理 (Security Competency Management)` — this keeps governance cohesive while giving it a dedicated slot
- G3: Add `D08.6 系統除役 (System Decommissioning)` under D08

#### Criterion 2: MECE Quality — Are domains mutually exclusive?

**Score: PARTIAL**

Findings:
- **Overlap O1**: D02.3 (通訊架構 Communication Architecture) vs. D05.5 (通訊協定整合 Protocol Integration) vs. D07.2 (協定橋接與轉換 Protocol Bridging). Three subdomains all touch industrial communication protocols. The boundary is ambiguous: where does "architecture" end and "integration" begin?
- **Overlap O2**: D10.4 (變更管理 Change Management) vs. D11.2 (工程流程標準化 Process Standardization). Change management is both a project-level activity (D10) and a governance process (D11). ID01 §6.4 and §6.5.2.3 treat CCM as a security governance function.
- **Overlap O3**: D01.3 (合規與稽核 Compliance/Audit) vs. D11.5 (標準與規範管理 Standards Management). Both touch standards compliance, but from different angles.

Recommended corrections:
- O1: Clarify boundary rule — D02.3 = architecture-level protocol selection and topology; D05.5 = device-level protocol configuration; D07.2 = cross-system protocol translation. Add a boundary note to each subdomain description.
- O2: Accept as designed overlap with explicit resolution rule — D10.4 handles project-specific change requests; D11.2 handles the standard operating procedure that D10.4 instances follow. Document this in CONVENTIONS.md.
- O3: No change needed. D01.3 is security-framework compliance; D11.5 is engineering standards compliance. Different subjects, same verb.

#### Criterion 3: Scalability — Can the structure absorb 150+ skills without strain?

**Score: PASS**

Findings: 13 domains × ~5 subdomains each = 66 slots. Target is 150–220 atomic skills, giving ~2.5–3.3 skills per subdomain on average. This is a comfortable density. The 3-digit sequential ID supports up to 999 skills per domain. No structural changes needed.

#### Criterion 4: Practical Fit — Does it match how ICP engineers actually work?

**Score: PASS**

Findings: The domain structure aligns with ICP's organizational units visible in ID01 Figure 1 (智慧技術處, 專案與工程管理處, 總管理處) and the role decomposition in ID03 Table 1 (SYS/DES/DEV/TL/AN/PR/IMP team, INT/TST team, VER/VAL team). The separation of D04 (Protection) from D03 (Power System) matches the distinct relay engineering specialty. D12 (Data Platform) independence matches the growing data engineering function.

#### Criterion 5: Governance vs. Execution Separation

**Score: PASS**

Findings: D11 (Engineering Governance) is cleanly separated from execution domains. D10 (Project Engineering) handles execution-level project coordination while D11 handles process standardization and quality assurance. The only minor tension is the change management overlap noted in O2 above, which is resolvable by convention.

#### Criterion 6: Missing Domains

**Score: PARTIAL**

Findings:
- **No missing Level 1 domains identified.** The 13 domains provide full coverage.
- The Phase 1 "待確認事項" asked about HSE (Health/Safety/Environmental) and procurement engineering. HSE is correctly excluded — it's outside the engineering skill scope. Procurement is covered by D10.3 (成本估算與報價) and D10.6 (售前技術支援). No new domains needed.

#### Criterion 7: Overlapping Subdomains

**Score: PARTIAL** (See O1, O2, O3 in Criterion 2)

#### Criterion 8: Naming Consistency

**Score: PARTIAL**

Findings:
- **N1**: Most subdomain names use Chinese noun phrases, but the English domain IDs in the Level 1 table use inconsistent styles: some are compound nouns (OT-CYBERSECURITY), some are gerunds (TESTING-COMMISSIONING). Recommend standardizing to compound nouns throughout.
- **N2**: Subdomain skill examples (技能範例 column) mix granularity levels — some are atomic actions ("防火牆規則規劃"), others are broad capabilities ("Zone/Conduit 拓撲設計"). This is acceptable for Phase 1 but should be normalized in Phase 2.

Recommended corrections:
- N1: Rename `TESTING-COMMISSIONING` → `TEST-COMMISSIONING` for consistency. Minor; defer to Phase 2 if disruptive.

#### Criterion 9: AI Agent Navigability

**Score: PASS**

Findings: The bilingual ID + name scheme, MECE structure, and planned metadata schema (Section 2) provide the information an AI agent needs for skill selection. The dependency graph (Phase 4) will complete the picture.

#### Criterion 10: Standards Alignment

**Score: PASS**

Findings: The domain map naturally accommodates skills derived from IEC 62443 (D01), IEC 61850/DNP3/OPC UA (D02, D05, D07), IEEE 2030 (D03), and NERC CIP (D01). The lifecycle stages R0–R5 from the ICP guidelines map cleanly onto D10 (project phases) and D01 (security lifecycle).

### 3.3 Review Change Log

| Change ID | Type | Target | Description | Impact |
|-----------|------|--------|-------------|--------|
| CHG-001 | Add | D01.7 | Add "SIS 安全 (Safety Instrumented System Security)" subdomain | +1 subdomain |
| CHG-002 | Add | D11.6 | Add "安全能力管理 (Security Competency Management)" subdomain | +1 subdomain |
| CHG-003 | Add | D08.6 | Add "系統除役 (System Decommissioning)" subdomain | +1 subdomain |
| CHG-004 | Clarify | D02.3, D05.5, D07.2 | Add boundary rules for communication/protocol subdomains | No structural change |
| CHG-005 | Clarify | D10.4, D11.2 | Add resolution rule for change management overlap | No structural change |
| CHG-006 | Note | N/A | Flag naming inconsistency in English domain IDs for future normalization | Deferred |
| CHG-007 | Add | D14 | Add new Level 1 domain: PRE-GATE-ENGINEERING 前置技術工程 with 6 subdomains | +1 domain, +6 subdomains |
| CHG-008 | Modify | D10 | Re-scope D10 to post-acceptance project technical management; migrate pre-gate subdomains to D14 | D10: 6→4 subdomains |
| CHG-009 | Add | ADR-005 | Architecture Decision Record for D14 independence from D10 | Documents lifecycle boundary decision |
| CHG-010 | Add | Dependency Notes | D14 connects to D01, D02, D09, D10, D11 as feeder domain | Formalizes cross-domain data flow |

**Net effect: 13 domains → 14 domains (+1 D14), 66 subdomains → 75 subdomains (+9 net)**

> **See `phase1-revision-r2.md` for the full R2 revision document including ADR-005, dependency diagrams, and skill candidate migration table.**

---

## Section 4: Approved Domain Map for Phase 2

The following is the approved baseline domain map incorporating all CHG-001 through CHG-006 corrections. Changes from the original Phase 1 map are marked with ★.

### Level 1 — 14 Engineering Skill Domains (R2: +1 D14, D10 re-scoped)

| # | Domain ID | Domain Name | Description |
|---|-----------|-------------|-------------|
| D01 | OT-CYBERSECURITY | OT 資訊安全 | OT/ICS security architecture, risk assessment, compliance, and protection |
| D02 | SYSTEM-ARCHITECTURE | 系統架構設計 | OT/IT system architecture, network topology, interface design |
| D03 | POWER-SYSTEM | 電力系統工程 | Power system analysis, design, simulation, renewable integration |
| D04 | PROTECTION | 保護工程 | Protection coordination, relay engineering, fault analysis |
| D05 | CONTROL-SYSTEM | 控制系統工程 | SCADA, EMS, DERMS, VPP design, configuration, tuning |
| D06 | PANEL-ENGINEERING | 盤櫃工程 | Electrical panel design, wiring, terminal planning |
| D07 | INTEGRATION | 系統整合工程 | Cross-system interface integration, protocol bridging, data exchange |
| D08 | TESTING-COMMISSIONING | 測試與試車 | FAT, SAT, commissioning, performance testing |
| D09 | ENGINEERING-DOCS | 工程文件管理 | Technical documentation, design reports, document governance |
| D10 | PROJECT-ENGINEERING | 專案工程 | ★ **Post-acceptance** project technical management: requirements tracking, change management, technical coordination, contract technical management |
| D11 | ENGINEERING-GOVERNANCE | 工程治理 | Process standardization, quality control, design review, knowledge management |
| D12 | DATA-PLATFORM | 能源資料平台 | Energy data acquisition, storage, analytics, visualization |
| D13 | ENGINEERING-AUTOMATION | 工程自動化 | Engineering automation tools, AI-assisted design, CI/CD |
| D14 | PRE-GATE-ENGINEERING | 前置技術工程 | ★ **NEW** Pre-Gate 0 → Gate 0 technical execution: requirement clarification, site survey, feasibility architecture, cost basis, Gate 0 input package |

### Level 2 — 75 Subdomains (R2: D14 added, D10 re-scoped)

**D01 — OT 資訊安全 (7 subdomains, +1)**

| ID | Subdomain | Description |
|----|-----------|-------------|
| D01.1 | 安全架構設計 | Zone/Conduit architecture, defense-in-depth, security zone partitioning |
| D01.2 | 風險評估與威脅建模 | Asset identification, threat analysis, risk quantification |
| D01.3 | 合規與稽核 | IEC 62443/ISO 27001 compliance assessment, gap analysis |
| D01.4 | 安全監控與事件回應 | Real-time monitoring, anomaly detection, incident response |
| D01.5 | 安全加固與組態管理 | Device hardening, access control, patch management |
| D01.6 | 供應鏈安全 | Vendor risk assessment, component security verification |
| D01.7 ★ | SIS 安全 | Safety Instrumented System security isolation, SIS-specific controls |

Boundary note for D01.7: Covers security controls specific to SIS/safety systems per IEC 62443 and IEC 61511 interface requirements. General OT security controls remain in D01.1–D01.6.

**D02 — 系統架構設計 (6 subdomains, unchanged)**

| ID | Subdomain | Description |
|----|-----------|-------------|
| D02.1 | OT 網路架構 | Industrial network topology, VLAN planning, redundancy |
| D02.2 | 系統介面設計 | Subsystem interface definition, data exchange specs |
| D02.3 | 通訊架構 | Protocol selection and architecture-level communication design |
| D02.4 | 高可用與冗餘設計 | Reliability design, fault tolerance, disaster recovery |
| D02.5 | 雲端與邊緣架構 | Hybrid cloud, edge computing deployment |
| D02.6 | 架構評審與決策 | ADR writing, technology selection evaluation |

Boundary note for D02.3 (CHG-004): D02.3 covers architecture-level protocol selection and topology design. Device-level protocol configuration belongs to D05.5. Cross-system protocol translation belongs to D07.2.

**D03 — 電力系統工程 (6 subdomains, unchanged)**

| ID | Subdomain | Description |
|----|-----------|-------------|
| D03.1 | 電力系統分析 | Power flow, short circuit, stability analysis |
| D03.2 | 再生能源整合 | Solar/wind grid integration, power forecasting |
| D03.3 | 儲能系統工程 | BESS design, control strategy, economic assessment |
| D03.4 | 虛擬電廠 | VPP architecture, DER aggregation, dispatch |
| D03.5 | 電力品質 | Harmonics, power factor, voltage regulation |
| D03.6 | 電力系統模擬 | System modeling, transient simulation, event replay |

**D04 — 保護工程 (4 subdomains, unchanged)**

| ID | Subdomain | Description |
|----|-----------|-------------|
| D04.1 | 保護協調 | Protection coordination, relay settings |
| D04.2 | 繼電器工程 | Relay selection, parameter setting, testing |
| D04.3 | 保護邏輯設計 | Protection logic diagrams, interlock logic |
| D04.4 | 故障分析 | Fault recording analysis, protection action assessment |

**D05 — 控制系統工程 (6 subdomains, unchanged)**

| ID | Subdomain | Description |
|----|-----------|-------------|
| D05.1 | SCADA 系統設計 | SCADA architecture, database, point list |
| D05.2 | EMS / DERMS 配置 | Energy/DER management system configuration |
| D05.3 | HMI 設計 | Human-machine interface design, alarm configuration |
| D05.4 | PLC / RTU 程式設計 | Controller programming and debugging |
| D05.5 | 通訊協定整合 | Device-level protocol configuration, gateway setup |
| D05.6 | 控制策略設計 | Automatic control logic, dispatch strategy, optimization |

**D06 — 盤櫃工程 (4 subdomains, unchanged)**

| ID | Subdomain | Description |
|----|-----------|-------------|
| D06.1 | 盤面佈局設計 | Panel component layout, thermal planning |
| D06.2 | 配線設計 | Wiring diagrams, terminal planning, wire labeling |
| D06.3 | 施工圖繪製 | Fabrication drawings, cutout drawings, installation |
| D06.4 | 元件選型與規範 | Component selection, technical specifications |

**D07 — 系統整合工程 (4 subdomains, unchanged)**

| ID | Subdomain | Description |
|----|-----------|-------------|
| D07.1 | 系統對接設計 | Subsystem integration design and planning |
| D07.2 | 協定橋接與轉換 | Cross-system protocol translation, gateway configuration |
| D07.3 | 資料整合 | Cross-system data consolidation, normalization |
| D07.4 | 第三方系統整合 | External system (ERP, GIS, weather) interfacing |

**D08 — 測試與試車 (6 subdomains, +1)**

| ID | Subdomain | Description |
|----|-----------|-------------|
| D08.1 | 工廠驗收測試 (FAT) | Pre-shipment functional verification |
| D08.2 | 現場驗收測試 (SAT) | On-site functional and performance verification |
| D08.3 | 試車程序 | System startup, step-by-step commissioning |
| D08.4 | 效能測試與驗證 | Performance benchmarking, stress testing |
| D08.5 | 問題追蹤與缺陷管理 | Defect tracking, severity classification, fix verification |
| D08.6 ★ | 系統除役 | System decommissioning: data preservation, media sanitization, hardware disposal |

**D09 — 工程文件管理 (5 subdomains, unchanged)**

| ID | Subdomain | Description |
|----|-----------|-------------|
| D09.1 | 設計文件撰寫 | Design reports, specifications, system descriptions |
| D09.2 | 圖面管理 | Engineering drawings (SLD, wiring, layout) management |
| D09.3 | 會議與溝通記錄 | Meeting minutes, action items, technical memos |
| D09.4 | 文件交付與版控 | Document packaging, submission, version control |
| D09.5 | 技術寫作 | Operation manuals, maintenance manuals, training materials |

**D10 — 專案工程 (4 subdomains) ★ RE-SCOPED to post-acceptance**

Pre-gate subdomains (D10.1 需求分析, D10.2 技術可行性評估, D10.3 成本估算與報價, D10.6 售前技術支援) migrated to D14 per CHG-008.

| ID | Subdomain | Description |
|----|-----------|-------------|
| D10.1 ★ | 專案需求管理 | Post-contract requirements tracking, decomposition, traceability, scope baseline maintenance |
| D10.2 ★ | 變更管理 | Design change evaluation, impact analysis, approval workflow |
| D10.3 ★ | 技術協調 | Cross-department/vendor technical coordination, RFI management |
| D10.4 ★ | 合約技術管理 | Technical scope tracking against contract, deliverable acceptance criteria, technical dispute resolution |

Boundary rule (D10/D14): Gate 0 approval / contract award is the lifecycle boundary. D14 operates Pre-Gate 0 → Gate 0. D10 operates post-contract kickoff → project closure. D14.1 scope framing feeds D10.1 requirements baseline.

**D11 — 工程治理 (6 subdomains, +1)**

| ID | Subdomain | Description |
|----|-----------|-------------|
| D11.1 | 設計審查 | Design review, stage-gate review, approval |
| D11.2 | 工程流程標準化 | SOP definition, process documentation, continuous improvement |
| D11.3 | 品質管控 | Quality planning, audit execution, nonconformance management |
| D11.4 | 知識管理 | Knowledge capture, structuring, sharing, lessons learned |
| D11.5 | 標準與規範管理 | Internal design standards, external standards tracking |
| D11.6 ★ | 安全能力管理 | Security competency frameworks, training programs, qualification tracking |

**D12 — 能源資料平台 (5 subdomains, unchanged)**

| ID | Subdomain | Description |
|----|-----------|-------------|
| D12.1 | 資料擷取與採集 | Field device data acquisition, protocol parsing, edge processing |
| D12.2 | 資料儲存與管理 | Time-series databases, data lakes, data lifecycle |
| D12.3 | 資料分析與建模 | Energy data analytics, forecasting models, optimization |
| D12.4 | 視覺化與儀表板 | Monitoring dashboards, reports, real-time visualization |
| D12.5 | 資料治理 | Data standards, metadata management, access control |

**D13 — 工程自動化 (4 subdomains, unchanged)**

| ID | Subdomain | Description |
|----|-----------|-------------|
| D13.1 | 工程工具開發 | Automated calculation, document generation, validation tools |
| D13.2 | AI 輔助工程 | AI/ML in engineering design, analysis, decision support |
| D13.3 | CI/CD 與 DevOps | Automated build, test, deployment of engineering deliverables |
| D13.4 | 工作流程自動化 | Repetitive workflow orchestration, automated reporting |

**D14 — 前置技術工程 (6 subdomains) ★ NEW**

Pre-Gate 0 → Gate 0 technical execution. Primary role: Concept System Architect / Feasibility Owner. This is a technical execution domain, not a business development function.

| ID | Subdomain | Description |
|----|-----------|-------------|
| D14.1 | 需求釐清與範圍框定 | Customer/stakeholder requirement elicitation, scope boundary definition, ambiguity resolution |
| D14.2 | 現場勘查與技術探勘 | Physical site assessment, existing infrastructure inventory, environmental constraints, brownfield integration |
| D14.3 | 可行性評估與概念架構 | Technical feasibility, concept system architecture, technology selection, POC design, preliminary Zone/Conduit concept |
| D14.4 | 成本基礎與 BOM 工程 | Engineering-grade cost estimation, preliminary CBOM, labor hour baseline, vendor pricing, cost risk contingency |
| D14.5 | 基線清冊準備 | Preliminary asset inventory, existing system baseline, interface point enumeration, legacy capability assessment |
| D14.6 | 前置風險評估與 Gate 0 輸入包 | Preliminary HLCRA, security classification input, risk-informed scope recommendations, Gate 0 decision package assembly |

D14 dependency connections: D14→D01 (HLCRA/security classification feeds TRA), D14→D02 (concept architecture feeds detailed design), D14→D09 (preliminary docs enter governance pipeline), D14→D10 (scope/cost baseline feeds project execution), D14→D11 (Gate 0 package feeds gate review). See `phase1-revision-r2.md` for full dependency diagram.

### Approved Map Statistics (R2)

| Metric | Original | R1 | R2 |
|--------|----------|-----|-----|
| Level 1 Domains | 13 | 13 | **14** |
| Level 2 Subdomains | 66 | 69 | **75** |
| Boundary clarifications | 0 | 3 | **4** |
| ADRs | 3 | 4 | **5** (+ ADR-005 Pre-Gate Independence) |

---

## Section 5: Stage C — Phase 2 Extraction Methodology

### 5.1 Source Document Register

| Source ID | Document Title | Version | Key Content Areas |
|-----------|---------------|---------|-------------------|
| ID01 | SI/SM Project and System Security Management Guideline | v1.0 | Security policy, org roles, CCM, secure development lifecycle (R0–R5), gate reviews, OT security practices (planning, TRA, detailed RA, countermeasures, testing, O&M), risk management |
| ID02 | SI/SM Security Management Guideline — Annexes | v1.1 | Practice examples (12 template TOCs), policy/procedure annexes (competency, independence, integrity verification), verification checklists (8 checklists covering security plan, TRA, network architecture, asset inventory, security design, countermeasures, acceptance testing, O&M) |
| ID03 | SI-SM Project Security Management Planning Guideline | v1.0 | Planning guideline: project overview, security policy, assurance organization, roles/responsibility assignment (Tables 1 & 2), competency requirements, security performance targets, security program activities, assurance approach, lifecycle management |
| PRAC | Practical Engineering Knowledge | N/A | Capabilities implied by ICP's tool stacks, workflows, and industry practice not explicitly documented in ID01–ID03 |

### 5.2 Extraction Method

**Step 1: Section-by-Section Scanning**
Each source document's table of contents and section headings are mapped to potential skill candidates. Every section heading that implies an action, deliverable, or competency generates a candidate.

**Step 2: Verb-Action Extraction**
Within each section, sentences containing action verbs (design, implement, perform, conduct, review, verify, validate, assess, configure, document, develop, plan, execute, test, monitor) are flagged as skill indicators.

**Step 3: Deliverable-Implied Extraction**
Tables listing deliverables (ID03 Table 2: Doc IDs 0.01–3.20) imply skills required to produce those deliverables. Each deliverable generates at least one skill candidate.

**Step 4: Role-Implied Extraction**
Role responsibility descriptions (ID01 Table 1, Table 2; ID03 §5.3.2) imply skills that role-holders must possess.

**Step 5: Practical Engineering Augmentation**
Skills that are industry-standard practice but not explicitly documented in ID01–ID03 are added with source = PRAC. These include tool-specific skills, emerging technology skills, and cross-domain workflow skills.

**Step 6: Normalization**
Each candidate is normalized to: a verb-noun phrase (English), a corresponding Chinese name, and mapped to exactly one subdomain.

**Step 7: Classification**
Each candidate is tagged with: skill_type, applicable lifecycle stages, source traceability, and confidence level.

---

## Section 6: Phase 2 Skill Candidate Inventory

### Legend

- **Source**: ID01/ID02/ID03 = document source with section reference; PRAC = practical engineering knowledge
- **Confidence**: H = High (directly stated in source), M = Medium (strongly implied), L = Low (inferred from context)
- **Type**: ANA=Analysis, DES=Design, ENG=Engineering, TST=Testing, DOC=Documentation, MGT=Management, VER=Verification, GOV=Governance, INT=Integration, OPS=Operations

---

### D01 — OT Cybersecurity (28 candidates)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D01-001 | Zone/Conduit Architecture Design | Zone/Conduit 架構設計 | D01.1 | DES | R1,R2 | ID01 §7.4.1.2; ID02 A.9 §10.2 | H |
| SC-D01-002 | Defense-in-Depth Strategy Design | 縱深防禦策略設計 | D01.1 | DES | R1,R2 | ID01 §6.5.1.3; ID02 A.9 §2 | H |
| SC-D01-003 | Firewall Rule Planning | 防火牆規則規劃 | D01.1 | ENG | R2,R3 | ID02 A.9 §10.1 | H |
| SC-D01-004 | Network Segmentation Documentation | 網路分段文件 | D01.1 | DOC | R2,R3 | ID01 §7.4.1.2; ID02 C.3 | H |
| SC-D01-005 | Asset Inventory Development | 資產清冊建立 | D01.2 | ANA | R0,R1 | ID01 §7.2.1; ID02 A.6; ID02 C.4 | H |
| SC-D01-006 | Threat and Risk Assessment (Preliminary) | 初步威脅風險評估 | D01.2 | ANA | R1 | ID01 §7.2; ID02 A.8 | H |
| SC-D01-007 | Detailed Risk Assessment | 詳細風險評估 | D01.2 | ANA | R2 | ID01 §7.3; ID03 §5.6.4 | H |
| SC-D01-008 | STRIDE/DREAD Threat Modeling | STRIDE/DREAD 威脅建模 | D01.2 | ANA | R1,R2 | ID01 §5.0 ref[32]; PRAC | M |
| SC-D01-009 | Risk Classification Matrix Development | 風險分類矩陣建立 | D01.2 | ANA | R1 | ID03 §5.4.1 | H |
| SC-D01-010 | Security Level Target (SL-T) Assessment | 安全等級目標評估 | D01.3 | ANA | R1 | ID01 §6.5.1.2; ID03 §5.4.2 | H |
| SC-D01-011 | IEC 62443 Compliance Gap Analysis | IEC 62443 合規差距分析 | D01.3 | ANA | R1,R4 | ID01 §6.6.3; ID02 C.1-C.8 | H |
| SC-D01-012 | Security Audit Execution | 安全稽核執行 | D01.3 | VER | R4 | ID01 §7.8.3.1 | H |
| SC-D01-013 | Gate Review Preparation and Execution | 閘門審查準備與執行 | D01.3 | GOV | R0-R5 | ID01 §6.5.1.1.3, §6.5.1.2.4 | H |
| SC-D01-014 | SIEM Configuration and Tuning | SIEM 配置與調校 | D01.4 | ENG | R3,R4 | ID01 §7.8.4.2; ID02 A.4 §9 | H |
| SC-D01-015 | Security Alarm Rule Design | 安全告警規則設計 | D01.4 | DES | R3 | ID01 §7.8.4.1 | H |
| SC-D01-016 | Incident Response Procedure Development | 事件回應程序撰寫 | D01.4 | DOC | R3,R4 | ID01 §7.8.5; ID03 §5.5.2 | H |
| SC-D01-017 | Security Incident Investigation and Forensics | 安全事件調查與鑑識 | D01.4 | ANA | R4 | ID01 §6.5.2.5 | M |
| SC-D01-018 | Continuous Security Monitoring | 持續安全監控 | D01.4 | OPS | R4 | ID01 §6.5.2.6; §7.8.4.2 | H |
| SC-D01-019 | Endpoint Hardening Implementation | 端點安全加固實施 | D01.5 | ENG | R3 | ID01 §7.4.1.5; ID02 A.10 | H |
| SC-D01-020 | Account and Access Control Management | 帳號與存取控制管理 | D01.5 | ENG | R3,R4 | ID01 §7.4.1.3; ID02 A.4 §4 | H |
| SC-D01-021 | Security Patch Management | 安全補丁管理 | D01.5 | OPS | R3,R4 | ID01 §7.4.1.11; ID02 A.4 §8.5 | H |
| SC-D01-022 | Backup and Restore Procedure Design | 備份與還原程序設計 | D01.5 | DES | R3 | ID01 §7.4.1.12; ID02 A.4 §6 | H |
| SC-D01-023 | Malware Protection Implementation | 惡意程式防護實施 | D01.5 | ENG | R3 | ID01 §7.4.1.10; ID02 A.4 §7 | H |
| SC-D01-024 | Vendor Security Risk Assessment | 供應商安全風險評估 | D01.6 | ANA | R0,R1 | ID01 §7.1.1.2; ID02 A.2 | H |
| SC-D01-025 | SBOM Analysis and Management | SBOM 分析與管理 | D01.6 | ANA | R3,R4 | ID03 §5.3.1; PRAC | M |
| SC-D01-026 | Third-Party Component Security Verification | 第三方元件安全驗證 | D01.6 | VER | R2,R3 | ID01 §6.4; ID02 B.3 | M |
| SC-D01-027 | SIS Security Control Implementation | SIS 安全控制實施 | D01.7★ | ENG | R2,R3 | ID01 §7.4.1.7; ID02 A.9 §12 | H |
| SC-D01-028 | Remote Access Security Configuration | 遠端存取安全配置 | D01.5 | ENG | R3 | ID01 §7.4.1.8; ID02 A.9 §9 | H |

---

### D02 — System Architecture (12 candidates)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D02-001 | OT Network Topology Design | OT 網路拓撲設計 | D02.1 | DES | R1,R2 | ID02 A.7; ID01 §7.4.1.2 | H |
| SC-D02-002 | Network Redundancy Design (RSTP/Ring) | 網路冗餘設計 | D02.1 | DES | R2 | PRAC | M |
| SC-D02-003 | Interface Control Document (ICD) Development | 介面控制文件撰寫 | D02.2 | DOC | R2 | PRAC | M |
| SC-D02-004 | Data Flow Diagram Development | 資料流圖繪製 | D02.2 | DOC | R1,R2 | ID02 A.5; ID01 §7.2.1 | H |
| SC-D02-005 | Industrial Protocol Architecture Design | 工業協定架構設計 | D02.3 | DES | R1,R2 | PRAC | M |
| SC-D02-006 | High-Availability Architecture Design | 高可用架構設計 | D02.4 | DES | R2 | PRAC | M |
| SC-D02-007 | RTO/RPO Planning | RTO/RPO 規劃 | D02.4 | DES | R2 | PRAC | M |
| SC-D02-008 | Edge Computing Deployment Design | 邊緣計算部署設計 | D02.5 | DES | R2 | PRAC | L |
| SC-D02-009 | Architecture Decision Record (ADR) Writing | 架構決策記錄撰寫 | D02.6 | DOC | R1,R2 | PRAC | M |
| SC-D02-010 | Technology Selection Evaluation | 技術選型評估 | D02.6 | ANA | R0,R1 | PRAC | M |
| SC-D02-011 | Simple Network Diagram Development | 簡易網路圖繪製 | D02.1 | DOC | R1 | ID02 A.7; ID03 Table 2 Doc 1.05 | H |
| SC-D02-012 | Architecture Review Facilitation | 架構審查主持 | D02.6 | GOV | R2 | ID01 §7.3.2 | H |

---

### D03 — Power System Engineering (10 candidates)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D03-001 | Power Flow Analysis | 潮流分析 | D03.1 | ANA | R1,R2 | PRAC | H |
| SC-D03-002 | Short Circuit Current Analysis | 短路電流分析 | D03.1 | ANA | R1,R2 | PRAC | H |
| SC-D03-003 | Voltage Stability Assessment | 電壓穩定度評估 | D03.1 | ANA | R2 | PRAC | M |
| SC-D03-004 | PV System Grid Integration Design | PV 系統併網設計 | D03.2 | DES | R1,R2 | PRAC | M |
| SC-D03-005 | BESS Capacity Planning | BESS 容量規劃 | D03.3 | DES | R1,R2 | PRAC | M |
| SC-D03-006 | VPP Dispatch Algorithm Design | VPP 調度演算法設計 | D03.4 | DES | R2 | PRAC | M |
| SC-D03-007 | DER Aggregation Strategy Design | DER 聚合策略設計 | D03.4 | DES | R1,R2 | PRAC | M |
| SC-D03-008 | Harmonic Analysis and Filter Design | 諧波分析與濾波器設計 | D03.5 | ANA | R2 | PRAC | M |
| SC-D03-009 | Transient Stability Simulation | 暫態穩定度模擬 | D03.6 | ANA | R2 | PRAC | M |
| SC-D03-010 | Power System Modeling (ETAP/PSS/E) | 電力系統建模 | D03.6 | ENG | R2 | PRAC | M |

---

### D04 — Protection Engineering (6 candidates)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D04-001 | Overcurrent Protection Coordination | 過電流保護協調 | D04.1 | DES | R2 | PRAC | H |
| SC-D04-002 | Distance Protection Setting Calculation | 距離保護整定計算 | D04.1 | ANA | R2 | PRAC | M |
| SC-D04-003 | Relay Selection and Parameter Setting | 繼電器選型與參數設定 | D04.2 | ENG | R2,R3 | PRAC | H |
| SC-D04-004 | Protection Logic Diagram Development | 保護邏輯圖繪製 | D04.3 | DES | R2 | PRAC | M |
| SC-D04-005 | Fault Recording Analysis | 故障錄波分析 | D04.4 | ANA | R4 | PRAC | M |
| SC-D04-006 | Protection Relay Testing | 保護繼電器測試 | D04.2 | TST | R3 | PRAC | H |

---

### D05 — Control System Engineering (14 candidates)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D05-001 | SCADA Point List Development | SCADA 點位清單建立 | D05.1 | ENG | R2 | PRAC | H |
| SC-D05-002 | SCADA Database Structure Design | SCADA 資料庫結構設計 | D05.1 | DES | R2 | PRAC | H |
| SC-D05-003 | EMS AGC Configuration | EMS AGC 配置 | D05.2 | ENG | R2,R3 | PRAC | M |
| SC-D05-004 | DERMS DER Management Strategy Setting | DERMS DER 管理策略設定 | D05.2 | ENG | R2,R3 | PRAC | M |
| SC-D05-005 | HMI Screen Design | HMI 畫面設計 | D05.3 | DES | R2,R3 | PRAC | H |
| SC-D05-006 | Alarm Hierarchy and Configuration Design | 告警層級配置設計 | D05.3 | DES | R2,R3 | PRAC | H |
| SC-D05-007 | PLC Ladder Logic Programming | PLC 階梯圖程式撰寫 | D05.4 | ENG | R2,R3 | PRAC | H |
| SC-D05-008 | Structured Text Programming | 結構化文字程式開發 | D05.4 | ENG | R2,R3 | PRAC | M |
| SC-D05-009 | Modbus Mapping Configuration | Modbus 映射配置 | D05.5 | ENG | R3 | PRAC | H |
| SC-D05-010 | IEC 61850 SCL Configuration | IEC 61850 SCL 配置 | D05.5 | ENG | R3 | PRAC | M |
| SC-D05-011 | OPC UA Server/Client Configuration | OPC UA 伺服器/客戶端配置 | D05.5 | ENG | R3 | PRAC | M |
| SC-D05-012 | PID Control Tuning | PID 控制調參 | D05.6 | ENG | R3 | PRAC | M |
| SC-D05-013 | Load Management Strategy Design | 負載管理策略設計 | D05.6 | DES | R2 | PRAC | M |
| SC-D05-014 | Frequency Regulation Control Design | 頻率調節控制設計 | D05.6 | DES | R2 | PRAC | M |

---

### D06 — Panel Engineering (6 candidates)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D06-001 | Panel Layout Design and Thermal Calculation | 盤面佈局設計與散熱計算 | D06.1 | DES | R2 | PRAC | H |
| SC-D06-002 | Wiring Diagram Development | 配線圖繪製 | D06.2 | DES | R2 | PRAC | H |
| SC-D06-003 | Terminal Block Schedule Development | 端子排表建立 | D06.2 | DOC | R2 | PRAC | H |
| SC-D06-004 | Fabrication Drawing Production (CAD) | 施工圖 CAD 出圖 | D06.3 | ENG | R2 | PRAC | H |
| SC-D06-005 | Wire Sizing Calculation | 線徑選用計算 | D06.2 | ANA | R2 | PRAC | M |
| SC-D06-006 | Component Selection and Specification Writing | 元件選型與規範書撰寫 | D06.4 | DES | R1,R2 | PRAC | H |

---

### D07 — Integration Engineering (7 candidates)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D07-001 | Interface Integration Matrix Development | 介面整合矩陣建立 | D07.1 | DOC | R2 | PRAC | M |
| SC-D07-002 | System Integration Architecture Diagram | 系統整合架構圖繪製 | D07.1 | DES | R2 | PRAC | M |
| SC-D07-003 | Protocol Gateway Configuration | 協定閘道配置 | D07.2 | ENG | R3 | PRAC | H |
| SC-D07-004 | Data Format Conversion Design | 資料格式轉換設計 | D07.2 | DES | R2,R3 | PRAC | M |
| SC-D07-005 | Cross-System Data Model Alignment | 跨系統資料模型對齊 | D07.3 | DES | R2 | PRAC | M |
| SC-D07-006 | Timestamp Synchronization Design | 時間戳同步設計 | D07.3 | DES | R2,R3 | PRAC | M |
| SC-D07-007 | Third-Party API Integration | 第三方 API 串接 | D07.4 | INT | R3 | PRAC | M |

---

### D08 — Testing & Commissioning (12 candidates)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D08-001 | FAT Procedure Development | FAT 程序撰寫 | D08.1 | DOC | R3 | ID01 §6.5.1.4; ID02 A.11 | H |
| SC-D08-002 | Security FAT Test Case Design | 安全 FAT 測試案例設計 | D08.1 | TST | R3 | ID02 A.11; ID03 Table 2 Doc 3.07 | H |
| SC-D08-003 | SAT Procedure Development | SAT 程序撰寫 | D08.2 | DOC | R3 | ID02 A.11; ID03 Table 2 Doc 3.12 | H |
| SC-D08-004 | Site Acceptance Testing Execution | 現場驗收測試執行 | D08.2 | TST | R3 | ID01 §7.6; ID02 C.7 | H |
| SC-D08-005 | System Security Acceptance Testing | 系統安全驗收測試 | D08.2 | TST | R3 | ID01 §6.5.1.4.3; §7.6 | H |
| SC-D08-006 | Commissioning Plan Development | 試車計畫撰寫 | D08.3 | DOC | R3 | PRAC | H |
| SC-D08-007 | Performance Baseline Establishment | 性能基線建立 | D08.4 | TST | R3 | PRAC | M |
| SC-D08-008 | Application Security Testing Execution | 應用安全測試執行 | D08.4 | TST | R3 | ID01 §6.5.1.4.2; §7.5 | H |
| SC-D08-009 | Penetration Testing Execution | 滲透測試執行 | D08.4 | TST | R3 | ID01 §6.5.1.4.4; ID03 Table 2 Doc 3.17 | H |
| SC-D08-010 | Vulnerability Scanning and Reporting | 弱點掃描與報告 | D08.4 | TST | R3,R4 | ID02 A.12 | H |
| SC-D08-011 | Defect Report Writing and Severity Classification | 缺陷報告撰寫與分級 | D08.5 | DOC | R3 | PRAC | H |
| SC-D08-012 | System Decommissioning Execution | 系統除役執行 | D08.6★ | OPS | R5 | ID01 §6.5.3 | H |

---

### D09 — Engineering Documentation (8 candidates)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D09-001 | System Design Description Writing | 系統設計說明書撰寫 | D09.1 | DOC | R2 | PRAC | H |
| SC-D09-002 | Security Functional Description Specification | 安全功能描述規範撰寫 | D09.1 | DOC | R3 | ID02 A.9; ID03 Table 2 Doc 3.02 | H |
| SC-D09-003 | Single-Line Diagram (SLD) Development | 單線圖繪製 | D09.2 | DES | R2 | PRAC | H |
| SC-D09-004 | Document Delivery Checklist Management | 文件交付清單管理 | D09.4 | MGT | R3 | ID03 §5.5.3 | H |
| SC-D09-005 | Version Control and Archiving | 版本控制與歸檔 | D09.4 | MGT | R0-R5 | PRAC | M |
| SC-D09-006 | Operation Manual Writing | 操作手冊撰寫 | D09.5 | DOC | R3 | PRAC | H |
| SC-D09-007 | SOP Development | SOP 編撰 | D09.5 | DOC | R3,R4 | PRAC | H |
| SC-D09-008 | Training Material Development | 培訓教材製作 | D09.5 | DOC | R3,R4 | ID01 §6.3; ID03 §5.3.3 | M |

---

### D10 — Project Engineering (5 candidates) ★ RE-SCOPED to post-acceptance

8 candidates migrated to D14. 1 new candidate added. See `phase1-revision-r2.md` for migration table.

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D10-001 | Requirements Traceability Matrix Management | 需求追溯矩陣管理 | D10.1 | DOC | R1,R2 | PRAC | M |
| SC-D10-002 | Change Request Evaluation and Impact Analysis | 變更申請評估與影響分析 | D10.2 | ANA | R1-R4 | ID01 §6.5.2.3; §7.8.7 | H |
| SC-D10-003 | Management of Change (MOC) Execution | 變更管理執行 | D10.2 | MGT | R1-R4 | ID01 §7.8.7.1; ID03 §5.7.1 | H |
| SC-D10-004 | Technical Clarification Meeting Facilitation | 技術澄清會議主持 | D10.3 | MGT | R1-R3 | PRAC | M |
| SC-D10-005 | Contract Technical Scope Tracking | 合約技術範圍追蹤 | D10.4 | MGT | R1-R4 | PRAC | H |

---

### D14 — Pre-Gate Engineering (16 candidates) ★ NEW DOMAIN

10 candidates migrated from former D10 + 6 new candidates.

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D14-001 | Requirements Specification Development | 需求規格書撰寫 | D14.1 | DOC | Pre-R0 | ID03 §5.1.1; Table 2 Doc 0.01 | H |
| SC-D14-002 | Stakeholder Analysis | 利害關係人分析 | D14.1 | ANA | Pre-R0 | PRAC | M |
| SC-D14-003 | Technical Feasibility Assessment | 技術可行性評估 | D14.3 | ANA | Pre-R0 | PRAC | H |
| SC-D14-004 | Technical Risk Matrix Development | 技術風險矩陣建立 | D14.6 | ANA | Pre-R0 | PRAC | M |
| SC-D14-005 | CBOM Development | CBOM 編制 | D14.4 | ENG | Pre-R0 | PRAC | H |
| SC-D14-006 | Labor Hour Estimation | 工時估算 | D14.4 | ANA | Pre-R0 | PRAC | H |
| SC-D14-007 | RFI Response Preparation | RFI 回覆準備 | D14.1 | DOC | Pre-R0 | PRAC | M |
| SC-D14-008 | Technical Proposal Writing | 技術提案撰寫 | D14.3 | DOC | Pre-R0 | PRAC | H |
| SC-D14-009 | POC Planning and Execution | POC 規劃與執行 | D14.3 | MGT | Pre-R0 | PRAC | M |
| SC-D14-010 | Tender Security Requirements Definition | 投標安全需求定義 | D14.6 | DOC | Pre-R0 | ID01 §6.5.1.1.1; ID03 Table 1 SSA-PRO-001 | H |
| SC-D14-011 | Site Survey and Constraint Documentation | 現場勘查與限制條件文件 | D14.2 | ANA | Pre-R0 | PRAC | H |
| SC-D14-012 | Existing Infrastructure Inventory | 既有基礎設施清冊 | D14.2 | DOC | Pre-R0 | PRAC | H |
| SC-D14-013 | Concept Zone/Conduit Architecture | 概念 Zone/Conduit 架構 | D14.3 | DES | Pre-R0 | PRAC; ID01 §6.5.1.1 | M |
| SC-D14-014 | Preliminary Security Classification | 初步安全分類 | D14.6 | ANA | Pre-R0 | ID03 §5.4.1; ID01 §6.5.1.2 | H |
| SC-D14-015 | Gate 0 Decision Package Assembly | Gate 0 決策包組裝 | D14.6 | DOC | Pre-R0 | ID01 §6.5.1.1.3; ID03 §5.5.2 | H |
| SC-D14-016 | Cost Risk Contingency Analysis | 成本風險餘裕分析 | D14.4 | ANA | Pre-R0 | PRAC | M |

---

### D11 — Engineering Governance (12 candidates)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D11-001 | Design Review Checklist Development | 設計審查清單建立 | D11.1 | GOV | R2 | PRAC | H |
| SC-D11-002 | Stage-Gate Review Facilitation | 階段閘門審查主持 | D11.1 | GOV | R0-R5 | ID01 §6.5.1.1.3 - §6.5.3.4 | H |
| SC-D11-003 | Critical Security Design Review | 關鍵安全設計審查 | D11.1 | VER | R2 | ID01 §7.3.2 | H |
| SC-D11-004 | Engineering SOP Development | 工程 SOP 制定 | D11.2 | GOV | R0-R5 | PRAC | H |
| SC-D11-005 | Process Efficiency Analysis | 流程效率分析 | D11.2 | ANA | R4 | PRAC | L |
| SC-D11-006 | Quality Plan Development | 品質計畫撰寫 | D11.3 | DOC | R1 | PRAC | H |
| SC-D11-007 | Nonconformance Management | 不合格項管理 | D11.3 | MGT | R3,R4 | ID01 §6.6.4 | M |
| SC-D11-008 | Lessons Learned Management | 經驗學習管理 | D11.4 | MGT | R4,R5 | PRAC | M |
| SC-D11-009 | Technical Knowledge Base Development | 技術知識庫建置 | D11.4 | ENG | R4 | PRAC | L |
| SC-D11-010 | Internal Design Standards Maintenance | 內部設計標準維護 | D11.5 | GOV | R0-R5 | PRAC | M |
| SC-D11-011 | Security Competency Framework Development | 安全能力框架建立 | D11.6★ | GOV | R0 | ID01 §6.3; ID03 §5.3.3 | H |
| SC-D11-012 | Security Training Program Management | 安全培訓計畫管理 | D11.6★ | MGT | R0-R5 | ID01 §6.3; ID03 §5.3.3 | H |

---

### D12 — Energy Data Platform (8 candidates)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D12-001 | Data Acquisition Architecture Design | 資料採集架構設計 | D12.1 | DES | R2 | PRAC | M |
| SC-D12-002 | Protocol Parser Development | 協定解析器開發 | D12.1 | ENG | R2,R3 | PRAC | M |
| SC-D12-003 | Time-Series Database Selection and Configuration | 時序資料庫選型與配置 | D12.2 | ENG | R2 | PRAC | M |
| SC-D12-004 | Data Retention Policy Design | 資料保留策略設計 | D12.2 | DES | R2 | PRAC | M |
| SC-D12-005 | Load Forecasting Model Development | 負載預測模型開發 | D12.3 | ENG | R2,R3 | PRAC | M |
| SC-D12-006 | Monitoring Dashboard Design | 監控儀表板設計 | D12.4 | DES | R3 | PRAC | M |
| SC-D12-007 | Data Dictionary Development | 資料字典建立 | D12.5 | DOC | R2 | PRAC | M |
| SC-D12-008 | Data Access Policy Design | 資料存取政策設計 | D12.5 | GOV | R2 | PRAC | M |

---

### D13 — Engineering Automation (6 candidates)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D13-001 | Automated Calculation Script Development | 自動化計算腳本開發 | D13.1 | ENG | R2,R3 | PRAC | M |
| SC-D13-002 | Document Generator Development | 文件產生器開發 | D13.1 | ENG | R3 | PRAC | M |
| SC-D13-003 | AI-Assisted Design Review | AI 輔助設計審查 | D13.2 | ENG | R2 | PRAC | L |
| SC-D13-004 | Automated Skill Invocation | 自動化技能調用 | D13.2 | ENG | R2-R4 | PRAC | L |
| SC-D13-005 | Automated Test Pipeline Development | 自動化測試管線開發 | D13.3 | ENG | R3 | PRAC | M |
| SC-D13-006 | Review Workflow Automation | 審查工作流程自動化 | D13.4 | ENG | R2-R4 | PRAC | L |

### Inventory Statistics

| Domain | Candidates | From ID01-03 | From PRAC | High Conf. | Med Conf. | Low Conf. |
|--------|-----------|-------------|-----------|-----------|----------|----------|
| D01 | 28 | 24 | 4 | 23 | 5 | 0 |
| D02 | 12 | 4 | 8 | 4 | 7 | 1 |
| D03 | 10 | 0 | 10 | 2 | 7 | 1 |
| D04 | 6 | 0 | 6 | 3 | 3 | 0 |
| D05 | 14 | 0 | 14 | 5 | 9 | 0 |
| D06 | 6 | 0 | 6 | 4 | 2 | 0 |
| D07 | 7 | 0 | 7 | 1 | 6 | 0 |
| D08 | 12 | 9 | 3 | 10 | 1 | 1 |
| D09 | 8 | 3 | 5 | 5 | 3 | 0 |
| D10 ★ | 5 | 2 | 3 | 2 | 2 | 1 |
| D11 | 12 | 5 | 7 | 6 | 3 | 3 |
| D12 | 8 | 0 | 8 | 0 | 8 | 0 |
| D13 | 6 | 0 | 6 | 0 | 3 | 3 |
| D14 ★ | 16 | 4 | 12 | 8 | 5 | 3 |
| **Total** | **150** | **51** | **99** | **73** | **64** | **13** |

*Note: Pre-normalization total is 150. After Section 7 merge (SC-D09-007 into SC-D11-004), post-normalization total is **149**.*

---

## Section 7: Duplicate and Normalization Review

### 7.1 Near-Duplicate Pairs Detected

| Pair | Candidate A | Candidate B | Verdict | Resolution |
|------|-------------|-------------|---------|------------|
| 1 | SC-D01-003 Firewall Rule Planning | SC-D01-004 Network Segmentation Documentation | NOT DUPLICATE | Different outputs: A produces rules, B produces documentation. Both retained. |
| 2 | SC-D01-006 TRA (Preliminary) | SC-D01-007 Detailed Risk Assessment | NOT DUPLICATE | Different lifecycle stages (R1 vs R2) and depth. Both retained as separate skills. |
| 3 | SC-D02-005 Protocol Architecture Design | SC-D05-009/010/011 Protocol Configuration | NOT DUPLICATE | D02.3 is architecture-level; D05.5 is device-level. Boundary rule CHG-004 applies. |
| 4 | SC-D01-012 Security Audit Execution | SC-D11-002 Stage-Gate Review Facilitation | NOT DUPLICATE | Audits verify compliance to standards; stage-gate reviews verify project milestone readiness. |
| 5 | SC-D09-007 SOP Development | SC-D11-004 Engineering SOP Development | MERGE | Both produce SOPs. **Resolution: Keep SC-D11-004 (governance owns the SOP process). Remove SC-D09-007 and reference SC-D11-004 from D09.** |
| 6 | SC-D10-008 Change Request Evaluation | SC-D10-009 MOC Execution | NOT DUPLICATE | Evaluation (analysis) vs. execution (management). Different skill types. |
| 7 | SC-D01-016 IR Procedure Development | SC-D01-017 Security Incident Investigation | NOT DUPLICATE | Writing the procedure vs. executing the investigation. Different lifecycle relevance. |

### 7.2 Normalization Actions

| Action | SC ID | Change | Rationale |
|--------|-------|--------|-----------|
| MERGE | SC-D09-007 | Remove; reference SC-D11-004 | SOP ownership belongs to governance |
| RENAME | SC-D08-005 | "System Security Acceptance Testing" → "Security Acceptance Testing Execution" | Verb-first consistency |
| RENAME | SC-D01-018 | "Continuous Security Monitoring" → "Security Monitoring Operations" | Clarify it's an ongoing operation |

### 7.3 Post-Normalization Count

After merging SC-D09-007 into SC-D11-004, the total candidate count is **149 skill candidates** across 14 domains (R2 revised).

### 7.4 Priority Candidates for Phase 3

The following 20 candidates are recommended for priority definition in Phase 3, based on: high confidence, high cross-domain impact, and criticality to ICP's core business:

| Priority | SC ID | Skill Name | Rationale |
|----------|-------|-----------|-----------|
| 1 | SC-D01-006 | Threat and Risk Assessment (Preliminary) | Foundation for all security decisions |
| 2 | SC-D01-007 | Detailed Risk Assessment | Key R2 deliverable |
| 3 | SC-D01-001 | Zone/Conduit Architecture Design | Core IEC 62443 skill |
| 4 | SC-D01-010 | SL-T Assessment | Drives all security requirements |
| 5 | SC-D01-011 | IEC 62443 Compliance Gap Analysis | Highest client-facing value |
| 6 | SC-D01-005 | Asset Inventory Development | Prerequisite for TRA |
| 7 | SC-D01-019 | Endpoint Hardening Implementation | Most common R3 deliverable |
| 8 | SC-D08-005 | Security Acceptance Testing Execution | Client handover gate |
| 9 | SC-D08-009 | Penetration Testing Execution | High-value verification skill |
| 10 | SC-D14-010 | Tender Security Requirements Definition | Business development critical (now in D14) |
| 11 | SC-D01-013 | Gate Review Preparation and Execution | Lifecycle governance backbone |
| 12 | SC-D02-001 | OT Network Topology Design | Architecture foundation |
| 13 | SC-D05-001 | SCADA Point List Development | Core control system skill |
| 14 | SC-D01-024 | Vendor Security Risk Assessment | Supply chain criticality |
| 15 | SC-D14-005 | CBOM Development | Revenue-critical (now in D14) |
| 16 | SC-D09-002 | Security Functional Description Specification | Key R3 document |
| 17 | SC-D11-002 | Stage-Gate Review Facilitation | Process governance core |
| 18 | SC-D01-020 | Account and Access Control Management | Highest-frequency security control |
| 19 | SC-D14-015 | Gate 0 Decision Package Assembly | Pre-gate lifecycle entry point |
| 20 | SC-D14-003 | Technical Feasibility Assessment | Pre-gate core engineering skill |

---

## Section 8: Recommended Next Actions

### 8.1 Immediate Actions (This Week)

1. **Create repository directory structure** on disk matching Section 1.1. Copy existing files into their designated locations.
2. **Write ADR-004** (Skill ID Pattern) as a standalone file in `00-governance/decisions/`.
3. **Instantiate CONVENTIONS.md and SCHEMA.md** from Sections 2.3 and 2.4 respectively.
4. **Archive the original Phase 1 map** as `phase1-skill-domain-map.md` (read-only) and create the approved baseline as `phase1-domain-map-approved.md` per Section 4.

### 8.2 Phase 3 Entry Criteria (Confirmed Met)

| Criterion | Status |
|-----------|--------|
| Approved domain map with boundary rules | Section 4 |
| Skill Registry Schema finalized | Section 2.4 |
| Skill ID convention established | Section 2.1–2.2 |
| Skill candidate inventory ≥100 candidates | 149 candidates (R2) |
| Duplicate review completed | Section 7 |
| Priority candidates identified for first batch | 20 candidates (includes D14) |

### 8.3 Phase 3 Recommendations

1. **Start with the 20 priority candidates** from Section 7.4. Write full skill definitions using the 24-field schema.
2. **Begin with D01 (OT Cybersecurity)** — it has the most candidates (28), the richest source material (all three PDFs), and the highest client-facing impact.
3. **Use the IEC 62443 lifecycle stages** as an organizing lens for defining inputs/outputs and dependencies.
4. **Read remaining pages of ID01, ID02, ID03** (pages 21+) to extract additional skill candidates from the detailed security countermeasure sections, verification checklists, and O&M procedures. The current extraction covers pages 1–20 of each document; significant additional material exists.

### 8.4 Known Gaps for Future Resolution

| Gap | Description | Phase to Address |
|-----|-------------|-----------------|
| Incomplete PDF extraction | Only pages 1–20 of each PDF were extracted; ID01 has 204+ pages, ID02 has 125+ pages, ID03 has 70+ pages | Phase 2 supplement or early Phase 3 |
| D12/D13 low-confidence candidates | Data platform and automation skills are primarily PRAC-sourced with no document backing | Phase 3 (validate with domain experts) |
| Cross-domain skill chains | Some skills span multiple domains (e.g., "Design security architecture" touches D01 + D02) | Phase 4 (Dependency Mapping) |
| Lifecycle stage mapping validation | IEC 62443 R0–R5 assignments need verification against ID01 §8.2 mapping table | Phase 3 |

---

*End of Deliverable — v1.0, 2026-03-13*
