# Phase 1 Domain Map — Revision R2

**Revision:** R2 (adds D14, re-scopes D10)
**Date:** 2026-03-13
**Baseline:** Approved Map v1.0 (13 domains, 69 subdomains)
**Revised:** 14 domains, 75 subdomains

---

## Revision Change Log

| Change ID | Type | Target | Description | Impact | Rationale |
|-----------|------|--------|-------------|--------|-----------|
| CHG-007 | ADD | D14 | Add new Level 1 domain: PRE-GATE-ENGINEERING 前置技術工程 | +1 domain, +6 subdomains | Pre-Gate 0 → Gate 0 technical execution (concept architecture, feasibility, site survey, cost basis) is a distinct engineering discipline with its own deliverables, roles (Concept System Architect / Feasibility Owner), and lifecycle position. Previously absorbed into D10, but D10 conflates pre-contract technical scoping with post-acceptance project engineering. Splitting them respects the lifecycle boundary at contract award / Gate 0 approval. |
| CHG-008 | MODIFY | D10 | Re-scope D10 to post-acceptance project technical management only | 3 subdomains removed, 1 renamed | D10 previously held pre-gate subdomains (D10.1 需求分析, D10.2 技術可行性評估, D10.3 成本估算與報價, D10.6 售前技術支援). These are moved to D14 or redefined. D10 retains post-acceptance scope: requirements management (post-contract), change management, technical coordination, and adds contract technical management. |
| CHG-009 | ADD | ADR-005 | Architecture Decision Record for D14 independence | No structural change | Documents the rationale for separating pre-gate engineering from project engineering. |
| CHG-010 | ADD | Dependency Notes | Add D14 dependency connections to D01, D02, D09, D10, D11 | No structural change | D14 is a feeder domain whose outputs become inputs to downstream project execution domains. |

---

## ADR-005: Separate Pre-Gate Engineering as Independent Domain

**Status:** Accepted
**Date:** 2026-03-13

**Context:**
In ICP's IEC 62443-aligned project lifecycle, the period from Pre-Gate 0 (opportunity identification) through Gate 0 (project initiation approval) involves substantial technical engineering work: site surveys, feasibility architecture, preliminary risk assessments, cost basis engineering, and Gate 0 input package preparation. This work is performed by a Concept System Architect or Feasibility Owner — a technical execution role, not a business sales role.

Previously, this work was scattered across D10 (Project Engineering) subdomains D10.1 (需求分析), D10.2 (技術可行性評估), D10.3 (成本估算與報價), and D10.6 (售前技術支援). This created two problems:

1. **Lifecycle conflation**: D10 mixed pre-contract scoping (where ICP doesn't yet have a project) with post-contract execution (where ICP has a signed engagement). These have different stakeholder relationships, approval gates, deliverable quality bars, and cost recovery models.
2. **Role confusion**: Pre-gate technical work is engineering, not sales. The old D10.6 label "售前技術支援" (Pre-sales Technical Support) frames the architect as a support function to sales rather than an independent technical authority.

**Decision:**
Create D14 PRE-GATE-ENGINEERING (前置技術工程) as an independent Level 1 domain. Re-scope D10 to cover post-acceptance project engineering exclusively. The lifecycle boundary is Gate 0 / contract award: everything before it belongs to D14, everything after belongs to D10.

**Consequences:**
- D14 gives pre-gate engineering its own skill taxonomy, maturity tracking, and competency path
- D10 becomes cleaner and more focused on project execution management
- Skills that span the boundary (e.g., requirements management evolves from D14 scoping into D10 tracking) are handled through dependency links, not subdomain sharing
- The 4-tier hierarchy naturally accommodates this: D14 skills feed D10 skills as dependencies

---

## Revised Level 1 — 14 Engineering Skill Domains

| # | Domain ID | Domain Name (ZH) | Domain Name (EN) | Description |
|---|-----------|------------------|-------------------|-------------|
| D01 | OT-CYBERSECURITY | OT 資訊安全 | OT Cybersecurity | OT/ICS security architecture, risk assessment, compliance, and protection |
| D02 | SYSTEM-ARCHITECTURE | 系統架構設計 | System Architecture | OT/IT system architecture, network topology, interface design |
| D03 | POWER-SYSTEM | 電力系統工程 | Power System Engineering | Power system analysis, design, simulation, renewable integration |
| D04 | PROTECTION | 保護工程 | Protection Engineering | Protection coordination, relay engineering, fault analysis |
| D05 | CONTROL-SYSTEM | 控制系統工程 | Control System Engineering | SCADA, EMS, DERMS, VPP design, configuration, tuning |
| D06 | PANEL-ENGINEERING | 盤櫃工程 | Panel Engineering | Electrical panel design, wiring, terminal planning |
| D07 | INTEGRATION | 系統整合工程 | Integration Engineering | Cross-system interface integration, protocol bridging, data exchange |
| D08 | TESTING-COMMISSIONING | 測試與試車 | Testing & Commissioning | FAT, SAT, commissioning, performance testing, decommissioning |
| D09 | ENGINEERING-DOCS | 工程文件管理 | Engineering Documentation | Technical documentation, design reports, document governance |
| D10 | PROJECT-ENGINEERING | 專案工程 | Project Engineering | **Post-acceptance** project technical management: requirements tracking, change management, technical coordination, contract technical management |
| D11 | ENGINEERING-GOVERNANCE | 工程治理 | Engineering Governance | Process standardization, quality control, design review, knowledge management |
| D12 | DATA-PLATFORM | 能源資料平台 | Energy Data Platform | Energy data acquisition, storage, analytics, visualization |
| D13 | ENGINEERING-AUTOMATION | 工程自動化 | Engineering Automation | Engineering automation tools, AI-assisted design, CI/CD |
| **D14** | **PRE-GATE-ENGINEERING** | **前置技術工程** | **Pre-Gate Engineering** | **Pre-Gate 0 → Gate 0 technical execution: requirement clarification, site survey, feasibility architecture, cost basis engineering, Gate 0 input package** |

**Total: 14 Level 1 Domains**

---

## Revised Level 2 — All Subdomains (75 total)

### D01 — OT 資訊安全 (7 subdomains) — unchanged from R1

| ID | Subdomain | Description |
|----|-----------|-------------|
| D01.1 | 安全架構設計 | Zone/Conduit architecture, defense-in-depth, security zone partitioning |
| D01.2 | 風險評估與威脅建模 | Asset identification, threat analysis, risk quantification |
| D01.3 | 合規與稽核 | IEC 62443/ISO 27001 compliance assessment, gap analysis |
| D01.4 | 安全監控與事件回應 | Real-time monitoring, anomaly detection, incident response |
| D01.5 | 安全加固與組態管理 | Device hardening, access control, patch management |
| D01.6 | 供應鏈安全 | Vendor risk assessment, component security verification |
| D01.7 | SIS 安全 | Safety Instrumented System security isolation, SIS-specific controls |

### D02 — 系統架構設計 (6 subdomains) — unchanged

| ID | Subdomain | Description |
|----|-----------|-------------|
| D02.1 | OT 網路架構 | Industrial network topology, VLAN planning, redundancy |
| D02.2 | 系統介面設計 | Subsystem interface definition, data exchange specs |
| D02.3 | 通訊架構 | Protocol selection and architecture-level communication design |
| D02.4 | 高可用與冗餘設計 | Reliability design, fault tolerance, disaster recovery |
| D02.5 | 雲端與邊緣架構 | Hybrid cloud, edge computing deployment |
| D02.6 | 架構評審與決策 | ADR writing, technology selection evaluation |

### D03 — 電力系統工程 (6 subdomains) — unchanged

| ID | Subdomain | Description |
|----|-----------|-------------|
| D03.1 | 電力系統分析 | Power flow, short circuit, stability analysis |
| D03.2 | 再生能源整合 | Solar/wind grid integration, power forecasting |
| D03.3 | 儲能系統工程 | BESS design, control strategy, economic assessment |
| D03.4 | 虛擬電廠 | VPP architecture, DER aggregation, dispatch |
| D03.5 | 電力品質 | Harmonics, power factor, voltage regulation |
| D03.6 | 電力系統模擬 | System modeling, transient simulation, event replay |

### D04 — 保護工程 (4 subdomains) — unchanged

| ID | Subdomain | Description |
|----|-----------|-------------|
| D04.1 | 保護協調 | Protection coordination, relay settings |
| D04.2 | 繼電器工程 | Relay selection, parameter setting, testing |
| D04.3 | 保護邏輯設計 | Protection logic diagrams, interlock logic |
| D04.4 | 故障分析 | Fault recording analysis, protection action assessment |

### D05 — 控制系統工程 (6 subdomains) — unchanged

| ID | Subdomain | Description |
|----|-----------|-------------|
| D05.1 | SCADA 系統設計 | SCADA architecture, database, point list |
| D05.2 | EMS / DERMS 配置 | Energy/DER management system configuration |
| D05.3 | HMI 設計 | Human-machine interface design, alarm configuration |
| D05.4 | PLC / RTU 程式設計 | Controller programming and debugging |
| D05.5 | 通訊協定整合 | Device-level protocol configuration, gateway setup |
| D05.6 | 控制策略設計 | Automatic control logic, dispatch strategy, optimization |

### D06 — 盤櫃工程 (4 subdomains) — unchanged

| ID | Subdomain | Description |
|----|-----------|-------------|
| D06.1 | 盤面佈局設計 | Panel component layout, thermal planning |
| D06.2 | 配線設計 | Wiring diagrams, terminal planning, wire labeling |
| D06.3 | 施工圖繪製 | Fabrication drawings, cutout drawings, installation |
| D06.4 | 元件選型與規範 | Component selection, technical specifications |

### D07 — 系統整合工程 (4 subdomains) — unchanged

| ID | Subdomain | Description |
|----|-----------|-------------|
| D07.1 | 系統對接設計 | Subsystem integration design and planning |
| D07.2 | 協定橋接與轉換 | Cross-system protocol translation, gateway configuration |
| D07.3 | 資料整合 | Cross-system data consolidation, normalization |
| D07.4 | 第三方系統整合 | External system (ERP, GIS, weather) interfacing |

### D08 — 測試與試車 (6 subdomains) — unchanged

| ID | Subdomain | Description |
|----|-----------|-------------|
| D08.1 | 工廠驗收測試 (FAT) | Pre-shipment functional verification |
| D08.2 | 現場驗收測試 (SAT) | On-site functional and performance verification |
| D08.3 | 試車程序 | System startup, step-by-step commissioning |
| D08.4 | 效能測試與驗證 | Performance benchmarking, stress testing |
| D08.5 | 問題追蹤與缺陷管理 | Defect tracking, severity classification, fix verification |
| D08.6 | 系統除役 | System decommissioning: data preservation, media sanitization, hardware disposal |

### D09 — 工程文件管理 (5 subdomains) — unchanged

| ID | Subdomain | Description |
|----|-----------|-------------|
| D09.1 | 設計文件撰寫 | Design reports, specifications, system descriptions |
| D09.2 | 圖面管理 | Engineering drawings (SLD, wiring, layout) management |
| D09.3 | 會議與溝通記錄 | Meeting minutes, action items, technical memos |
| D09.4 | 文件交付與版控 | Document packaging, submission, version control |
| D09.5 | 技術寫作 | Operation manuals, maintenance manuals, training materials |

### D10 — 專案工程 (4 subdomains) — ★ REVISED: re-scoped to post-acceptance

Previous D10 had 6 subdomains. The following were **migrated to D14**:
- D10.1 (需求分析 — pre-contract scope) → merged into D14.1
- D10.2 (技術可行性評估) → migrated to D14.3
- D10.3 (成本估算與報價) → migrated to D14.4
- D10.6 (售前技術支援) → dissolved; POC/bid support absorbed into D14.3 and D14.6

Retained and re-numbered:

| ID | Subdomain | Description |
|----|-----------|-------------|
| D10.1 ★ | 專案需求管理 (Project Requirements Management) | Post-contract requirements tracking, decomposition, traceability, and scope baseline maintenance. Receives initial scope from D14.1. |
| D10.2 ★ | 變更管理 (Change Management) | Design change evaluation, impact analysis, approval workflow (previously D10.4) |
| D10.3 ★ | 技術協調 (Technical Coordination) | Cross-department/vendor technical coordination, RFI management (previously D10.5) |
| D10.4 ★ | 合約技術管理 (Contract Technical Management) | Technical scope tracking against contract, deliverable acceptance criteria management, technical dispute resolution |

Boundary rule for D10/D14: The lifecycle boundary is **Gate 0 approval / contract award**. D14 operates from opportunity identification through Gate 0 input package delivery. D10 operates from project kickoff (post-contract) through project closure. Requirements evolve across the boundary: D14.1 captures and frames initial requirements → D10.1 manages them as contractual baseline.

### D11 — 工程治理 (6 subdomains) — unchanged from R1

| ID | Subdomain | Description |
|----|-----------|-------------|
| D11.1 | 設計審查 | Design review, stage-gate review, approval |
| D11.2 | 工程流程標準化 | SOP definition, process documentation, continuous improvement |
| D11.3 | 品質管控 | Quality planning, audit execution, nonconformance management |
| D11.4 | 知識管理 | Knowledge capture, structuring, sharing, lessons learned |
| D11.5 | 標準與規範管理 | Internal design standards, external standards tracking |
| D11.6 | 安全能力管理 | Security competency frameworks, training programs, qualification tracking |

### D12 — 能源資料平台 (5 subdomains) — unchanged

| ID | Subdomain | Description |
|----|-----------|-------------|
| D12.1 | 資料擷取與採集 | Field device data acquisition, protocol parsing, edge processing |
| D12.2 | 資料儲存與管理 | Time-series databases, data lakes, data lifecycle |
| D12.3 | 資料分析與建模 | Energy data analytics, forecasting models, optimization |
| D12.4 | 視覺化與儀表板 | Monitoring dashboards, reports, real-time visualization |
| D12.5 | 資料治理 | Data standards, metadata management, access control |

### D13 — 工程自動化 (4 subdomains) — unchanged

| ID | Subdomain | Description |
|----|-----------|-------------|
| D13.1 | 工程工具開發 | Automated calculation, document generation, validation tools |
| D13.2 | AI 輔助工程 | AI/ML in engineering design, analysis, decision support |
| D13.3 | CI/CD 與 DevOps | Automated build, test, deployment of engineering deliverables |
| D13.4 | 工作流程自動化 | Repetitive workflow orchestration, automated reporting |

### D14 — 前置技術工程 (6 subdomains) — ★ NEW

Pre-Gate 0 through Gate 0 technical execution. The Concept System Architect / Feasibility Owner is the primary role. This is a **technical execution domain**, not a business development function. The engineer in this domain produces engineering deliverables (feasibility studies, concept architectures, cost basis, preliminary risk packages) that feed into the Gate 0 decision and subsequent project execution.

| ID | Subdomain | Description |
|----|-----------|-------------|
| D14.1 | 需求釐清與範圍框定 (Requirement Clarification & Scope Framing) | Customer/stakeholder requirement elicitation, scope boundary definition, requirement ambiguity resolution, preliminary requirement traceability. Operates on raw RFP/RFI/SOW inputs to produce structured scope definition. |
| D14.2 | 現場勘查與技術探勘 (Site Survey & Technical Discovery) | Physical site assessment, existing infrastructure inventory, environmental constraints documentation, network/power topology discovery, brownfield integration assessment. Produces site survey report and constraint register. |
| D14.3 | 可行性評估與概念架構 (Feasibility & Concept Architecture) | Technical feasibility analysis, concept-level system architecture, technology selection rationale, POC design where needed, preliminary security architecture (Zone/Conduit concept). Produces feasibility report and concept architecture document. |
| D14.4 | 成本基礎與 BOM 工程 (Cost Basis & BOM Engineering) | Engineering-grade cost estimation, preliminary CBOM development, labor hour estimation baseline, vendor pricing coordination, cost risk contingency analysis. Produces cost basis document and draft BOM. |
| D14.5 | 基線清冊準備 (Baseline Inventory Preparation) | Preliminary asset inventory, existing system baseline documentation, interface point enumeration, legacy system capability assessment. Feeds into D01.5 (asset inventory) and D01.6 (TRA asset list) after Gate 0. |
| D14.6 | 前置風險評估與 Gate 0 輸入包 (Pre-Risk Assessment & Gate 0 Input Package) | Preliminary high-level cybersecurity risk assessment (HLCRA), security classification input, risk-informed scope recommendations, Gate 0 decision package assembly. Consolidates D14.1–D14.5 outputs into a formal Gate 0 submission. |

---

## Domain Dependency Notes — D14 Connections

D14 is a **feeder domain** in the skill dependency graph. Its outputs become formal inputs to downstream domains after Gate 0 approval.

```
D14 PRE-GATE-ENGINEERING
│
├──→ D01 OT-CYBERSECURITY
│    D14.6 (HLCRA, security classification) → D01.2 (full TRA input)
│    D14.5 (baseline inventory) → D01.5 (asset inventory baseline)
│    D14.3 (concept Zone/Conduit) → D01.1 (detailed security architecture)
│
├──→ D02 SYSTEM-ARCHITECTURE
│    D14.3 (concept architecture) → D02.1 (detailed OT network design)
│    D14.2 (site survey, existing topology) → D02.1 (brownfield constraints)
│    D14.3 (technology selection) → D02.6 (formal ADR)
│
├──→ D09 ENGINEERING-DOCS
│    D14.1–D14.6 all produce preliminary documents that become
│    inputs to D09's formal document governance pipeline
│
├──→ D10 PROJECT-ENGINEERING
│    D14.1 (scope framing) → D10.1 (project requirements baseline)
│    D14.4 (cost basis) → D10 (project budget baseline)
│    D14.6 (Gate 0 package) → D10 (project initiation input)
│
└──→ D11 ENGINEERING-GOVERNANCE
     D14.6 (Gate 0 package) → D11.1 (Gate 0 review input)
     D14.3 (concept architecture) → D11.1 (design review subject)
     All D14 work follows D11.2 (SOP) and D11.5 (standards)
```

### Reverse Dependencies (D14 consumes from)

```
D11 ENGINEERING-GOVERNANCE → D14
    D11.2 (SOPs) define how D14 work is conducted
    D11.5 (standards) constrain D14 deliverable format

D01 OT-CYBERSECURITY → D14
    D01.3 (compliance framework knowledge) informs D14.6 security classification

D09 ENGINEERING-DOCS → D14
    D09.4 (document templates, version control) provide D14 deliverable format
```

---

## Revised Statistics

| Metric | R1 Approved | R2 Revised | Delta |
|--------|-------------|------------|-------|
| Level 1 Domains | 13 | **14** | +1 |
| Level 2 Subdomains | 69 | **75** | +6 (D14: +6, D10: −2 net) |
| ADRs | 4 | **5** | +1 (ADR-005) |
| Boundary rules | 3 | **4** | +1 (D10/D14 lifecycle boundary) |

### Subdomain count by domain

| Domain | R1 Count | R2 Count | Change |
|--------|----------|----------|--------|
| D01 | 7 | 7 | — |
| D02 | 6 | 6 | — |
| D03 | 6 | 6 | — |
| D04 | 4 | 4 | — |
| D05 | 6 | 6 | — |
| D06 | 4 | 4 | — |
| D07 | 4 | 4 | — |
| D08 | 6 | 6 | — |
| D09 | 5 | 5 | — |
| D10 | 6 | **4** | −2 (re-scoped, subdomains migrated to D14) |
| D11 | 6 | 6 | — |
| D12 | 5 | 5 | — |
| D13 | 4 | 4 | — |
| D14 | — | **6** | +6 (new domain) |
| **Total** | **69** | **75** | **+6** |

---

## Skill Candidate Migration Impact (for Phase 2 update)

The following Phase 2 skill candidates from the previous inventory require re-assignment:

| Previous SC ID | Previous Domain | Skill Name | New Domain | New SC ID | Action |
|----------------|----------------|-----------|------------|-----------|--------|
| SC-D10-001 | D10.1 | Requirements Specification Development | D14.1 | SC-D14-001 | MIGRATE — pre-contract scope work |
| SC-D10-002 | D10.1 | Requirements Traceability Matrix | D10.1 (stays) | SC-D10-001 | RENUMBER — post-contract tracking |
| SC-D10-003 | D10.1 | Stakeholder Analysis | D14.1 | SC-D14-002 | MIGRATE — pre-gate activity |
| SC-D10-004 | D10.2 | Technical Feasibility Assessment | D14.3 | SC-D14-003 | MIGRATE |
| SC-D10-005 | D10.2 | Technical Risk Matrix Development | D14.6 | SC-D14-004 | MIGRATE — feeds Gate 0 |
| SC-D10-006 | D10.3 | CBOM Development | D14.4 | SC-D14-005 | MIGRATE |
| SC-D10-007 | D10.3 | Labor Hour Estimation | D14.4 | SC-D14-006 | MIGRATE |
| SC-D10-008 | D10.4 | Change Request Evaluation | D10.2 | SC-D10-002 | RENUMBER (stays in D10) |
| SC-D10-009 | D10.4 | MOC Execution | D10.2 | SC-D10-003 | RENUMBER (stays in D10) |
| SC-D10-010 | D10.5 | Technical Clarification Meeting | D10.3 | SC-D10-004 | RENUMBER (stays in D10) |
| SC-D10-011 | D10.5 | RFI Response Preparation | D14.1 | SC-D14-007 | MIGRATE — pre-contract RFI |
| SC-D10-012 | D10.6 | Technical Proposal Writing | D14.3 | SC-D14-008 | MIGRATE |
| SC-D10-013 | D10.6 | POC Planning and Execution | D14.3 | SC-D14-009 | MIGRATE |
| SC-D10-014 | D10.6 | Tender Security Requirements Definition | D14.6 | SC-D14-010 | MIGRATE |

### New D14 Skill Candidates (added from practical engineering knowledge)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D14-011 | Site Survey and Constraint Documentation | 現場勘查與限制條件文件 | D14.2 | ANA | Pre-R0 | PRAC | H |
| SC-D14-012 | Existing Infrastructure Inventory | 既有基礎設施清冊 | D14.2 | DOC | Pre-R0 | PRAC | H |
| SC-D14-013 | Concept Zone/Conduit Architecture | 概念 Zone/Conduit 架構 | D14.3 | DES | Pre-R0 | PRAC; ID01 §6.5.1.1 | M |
| SC-D14-014 | Preliminary Security Classification | 初步安全分類 | D14.6 | ANA | Pre-R0 | ID03 §5.4.1; ID01 §6.5.1.2 | H |
| SC-D14-015 | Gate 0 Decision Package Assembly | Gate 0 決策包組裝 | D14.6 | DOC | Pre-R0 | ID01 §6.5.1.1.3; ID03 §5.5.2 | H |
| SC-D14-016 | Cost Risk Contingency Analysis | 成本風險餘裕分析 | D14.4 | ANA | Pre-R0 | PRAC | M |

### New D10 Skill Candidate (post-acceptance addition)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D10-005 | Contract Technical Scope Tracking | 合約技術範圍追蹤 | D10.4 | MGT | R1-R4 | PRAC | H |

### Revised Inventory Count

| Category | Previous | Revised | Delta |
|----------|----------|---------|-------|
| D10 candidates | 14 | 5 | −9 (8 migrated to D14, 1 new) |
| D14 candidates | 0 | 16 | +16 (10 migrated + 6 new) |
| Total all domains | 142 | **149** | +7 |

---

## Revised Domain Architecture Tree

```
Engineering Skills 工程技能體系
│
├─ D01 OT Cybersecurity OT 資訊安全 (7 subdomains)
│   ├─ D01.1 安全架構設計
│   ├─ D01.2 風險評估與威脅建模
│   ├─ D01.3 合規與稽核
│   ├─ D01.4 安全監控與事件回應
│   ├─ D01.5 安全加固與組態管理
│   ├─ D01.6 供應鏈安全
│   └─ D01.7 SIS 安全
│
├─ D02 System Architecture 系統架構設計 (6 subdomains)
│   ├─ D02.1 OT 網路架構
│   ├─ D02.2 系統介面設計
│   ├─ D02.3 通訊架構
│   ├─ D02.4 高可用與冗餘設計
│   ├─ D02.5 雲端與邊緣架構
│   └─ D02.6 架構評審與決策
│
├─ D03 Power System Engineering 電力系統工程 (6 subdomains)
│   ├─ D03.1 電力系統分析
│   ├─ D03.2 再生能源整合
│   ├─ D03.3 儲能系統工程
│   ├─ D03.4 虛擬電廠
│   ├─ D03.5 電力品質
│   └─ D03.6 電力系統模擬
│
├─ D04 Protection Engineering 保護工程 (4 subdomains)
│   ├─ D04.1 保護協調
│   ├─ D04.2 繼電器工程
│   ├─ D04.3 保護邏輯設計
│   └─ D04.4 故障分析
│
├─ D05 Control System Engineering 控制系統工程 (6 subdomains)
│   ├─ D05.1 SCADA 系統設計
│   ├─ D05.2 EMS / DERMS 配置
│   ├─ D05.3 HMI 設計
│   ├─ D05.4 PLC / RTU 程式設計
│   ├─ D05.5 通訊協定整合
│   └─ D05.6 控制策略設計
│
├─ D06 Panel Engineering 盤櫃工程 (4 subdomains)
│   ├─ D06.1 盤面佈局設計
│   ├─ D06.2 配線設計
│   ├─ D06.3 施工圖繪製
│   └─ D06.4 元件選型與規範
│
├─ D07 Integration Engineering 系統整合工程 (4 subdomains)
│   ├─ D07.1 系統對接設計
│   ├─ D07.2 協定橋接與轉換
│   ├─ D07.3 資料整合
│   └─ D07.4 第三方系統整合
│
├─ D08 Testing & Commissioning 測試與試車 (6 subdomains)
│   ├─ D08.1 工廠驗收測試 (FAT)
│   ├─ D08.2 現場驗收測試 (SAT)
│   ├─ D08.3 試車程序
│   ├─ D08.4 效能測試與驗證
│   ├─ D08.5 問題追蹤與缺陷管理
│   └─ D08.6 系統除役
│
├─ D09 Engineering Documentation 工程文件管理 (5 subdomains)
│   ├─ D09.1 設計文件撰寫
│   ├─ D09.2 圖面管理
│   ├─ D09.3 會議與溝通記錄
│   ├─ D09.4 文件交付與版控
│   └─ D09.5 技術寫作
│
├─ D10 Project Engineering 專案工程 (4 subdomains) ★ RE-SCOPED
│   ├─ D10.1 專案需求管理 (post-contract)
│   ├─ D10.2 變更管理
│   ├─ D10.3 技術協調
│   └─ D10.4 合約技術管理
│
├─ D11 Engineering Governance 工程治理 (6 subdomains)
│   ├─ D11.1 設計審查
│   ├─ D11.2 工程流程標準化
│   ├─ D11.3 品質管控
│   ├─ D11.4 知識管理
│   ├─ D11.5 標準與規範管理
│   └─ D11.6 安全能力管理
│
├─ D12 Energy Data Platform 能源資料平台 (5 subdomains)
│   ├─ D12.1 資料擷取與採集
│   ├─ D12.2 資料儲存與管理
│   ├─ D12.3 資料分析與建模
│   ├─ D12.4 視覺化與儀表板
│   └─ D12.5 資料治理
│
├─ D13 Engineering Automation 工程自動化 (4 subdomains)
│   ├─ D13.1 工程工具開發
│   ├─ D13.2 AI 輔助工程
│   ├─ D13.3 CI/CD 與 DevOps
│   └─ D13.4 工作流程自動化
│
└─ D14 Pre-Gate Engineering 前置技術工程 (6 subdomains) ★ NEW
    ├─ D14.1 需求釐清與範圍框定
    ├─ D14.2 現場勘查與技術探勘
    ├─ D14.3 可行性評估與概念架構
    ├─ D14.4 成本基礎與 BOM 工程
    ├─ D14.5 基線清冊準備
    └─ D14.6 前置風險評估與 Gate 0 輸入包
```

---

## Approval Confirmation

This revision (R2) is the approved baseline for Phase 2 skill candidate extraction. The previous R1 map is archived as historical reference. Phase 2 work should use R2 domain assignments and skill candidate IDs.

**Gate criteria for Phase 2 entry (re-confirmed):**
- [x] Domain map revised with D14 and D10 re-scope
- [x] ADR-005 documents the decision
- [x] Dependency notes connect D14 to D01, D02, D09, D10, D11
- [x] Skill candidate migration table produced
- [x] Statistics updated: 14 domains, 75 subdomains, 149 candidates

---

*End of Revision R2 — 2026-03-13*

---

> **R3 勘誤（2026-03-13）：** 本文件多處宣稱子領域總數為 75，實際加總為 **73**。
> 誤差來源：R2 淨變動計為 +6（D14: +6），但遺漏 D10 縮減 −2，實際淨變動為 +4（69 + 4 = 73）。
> 本文件作為歷史紀錄保留原文不改，正確數字見 `phase1-domain-map-approved.md` R3 版本。
