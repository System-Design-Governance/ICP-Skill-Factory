# ICP Skill Factory — Approved Domain Map (Phase 1 Baseline)

**Version:** R5 (2026-03-13)
**Status:** APPROVED for Phase 3 Entry
**Change History:** See `phase1-review-changelog.md`, `phase1-formal-review-r3.md`, and `../02-skill-candidates/sources/R5-new-source-analysis.md`

本文件為整合 R3 審查修正及 R5 治理文件滾動更新後的正式基線。
Changes from the original Phase 1 map are marked with ★. R3 changes are marked with ◆. R5 governance enrichments are marked with ▲.

### Level 1 — 14 Engineering Skill Domains (R3: D08/D10/D11/D14 修正)

| # | Domain ID | Domain Name | Description |
|---|-----------|-------------|-------------|
| D01 | OT-CYBERSECURITY | OT 資訊安全 | OT/ICS security architecture, risk assessment, compliance, and protection |
| D02 | SYSTEM-ARCHITECTURE | 系統架構設計 | OT/IT system architecture, network topology, interface design |
| D03 | POWER-SYSTEM | 電力系統工程 | Power system analysis, design, simulation, renewable integration |
| D04 | PROTECTION | 保護工程 | Protection coordination, relay engineering, fault analysis |
| D05 | CONTROL-SYSTEM | 控制系統工程 | SCADA, EMS, DERMS, VPP design, configuration, tuning |
| D06 | PANEL-ENGINEERING | 盤櫃工程 | Electrical panel design, wiring, terminal planning |
| D07 | INTEGRATION | 系統整合工程 | Cross-system interface integration, protocol bridging, data exchange |
| D08 | TESTING-COMMISSIONING | 測試與試車 | ◆ FAT, SAT, commissioning, performance testing（D08.6 除役遷出至 D10.5） |
| D09 | ENGINEERING-DOCS | 工程文件管理 | Technical documentation, design reports, document governance |
| D10 | PROJECT-ENGINEERING | 專案工程 | ★◆ **Post-acceptance** project technical management: requirements tracking, change management, technical coordination, contract technical management, system decommissioning |
| D11 | ENGINEERING-GOVERNANCE | 工程治理 | Process standardization, quality control, design review, knowledge management |
| D12 | DATA-PLATFORM | 能源資料平台 | Energy data acquisition, storage, analytics, visualization |
| D13 | ENGINEERING-AUTOMATION | 工程自動化 | Engineering automation tools, AI-assisted design, CI/CD |
| D14 | PRE-GATE-ENGINEERING | 前置技術工程 | ★ **NEW** Pre-Gate 0 → Gate 0 technical execution: requirement clarification, site survey, feasibility architecture, cost basis, Gate 0 input package |

### Level 2 — 73 Subdomains (R3: 修正 R2 算術錯誤 75→73)

**D01 — OT 資訊安全 (7 subdomains, +1)**

| ID | Subdomain | Description |
|----|-----------|-------------|
| D01.1 | 安全架構設計 | Zone/Conduit architecture, defense-in-depth, security zone partitioning |
| D01.2 | 風險評估與威脅建模 | Asset identification, threat analysis, risk quantification. ▲ GOV-SD mandates triple-method integrated risk assessment: IEC 62443-3-2 + FMEA (RPN) + HAZOP. Risk source traceability required (T-XXX/FM-XXX/HAZ-XXX). |
| D01.3 | 合規與稽核 | IEC 62443/ISO 27001 compliance assessment, gap analysis. ▲ GOV-SD defines SL Decision Lifecycle: Gate 0 propose → Gate 1 confirm → Gate 2 re-evaluate → Gate 3 validate. |
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

**D08 — 測試與試車 (5 subdomains) ◆ D08.6 遷出至 D10.5**

| ID | Subdomain | Description |
|----|-----------|-------------|
| D08.1 | 工廠驗收測試 (FAT) | Pre-shipment functional verification |
| D08.2 | 現場驗收測試 (SAT) | On-site functional and performance verification |
| D08.3 | 試車程序 | System startup, step-by-step commissioning |
| D08.4 | 效能測試與驗證 | Performance benchmarking, stress testing |
| D08.5 | 問題追蹤與缺陷管理 | Defect tracking, severity classification, fix verification |

FIX-001 說明：原 D08.6 系統除役（R5 生命週期活動）歸屬不當於測試域（R3 活動），已遷移至 D10.5。

**D09 — 工程文件管理 (5 subdomains, unchanged)**

| ID | Subdomain | Description |
|----|-----------|-------------|
| D09.1 | 設計文件撰寫 | Design reports, specifications, system descriptions |
| D09.2 | 圖面管理 | Engineering drawings (SLD, wiring, layout) management |
| D09.3 | 會議與溝通記錄 | Meeting minutes, action items, technical memos |
| D09.4 | 文件交付與版控 | Document packaging, submission, version control |
| D09.5 | 技術寫作 | Operation manuals, maintenance manuals, training materials |

**D10 — 專案工程 (5 subdomains) ★◆ RE-SCOPED to post-acceptance + decommissioning**

Pre-gate subdomains (D10.1 需求分析, D10.2 技術可行性評估, D10.3 成本估算與報價, D10.6 售前技術支援) migrated to D14 per CHG-008. D08.6 系統除役遷入為 D10.5 per FIX-001。

| ID | Subdomain | Description |
|----|-----------|-------------|
| D10.1 ★ | 專案需求管理 | Post-contract requirements tracking, decomposition, traceability, scope baseline maintenance |
| D10.2 ★ | 變更管理 | Design change evaluation, impact analysis, approval workflow |
| D10.3 ★ | 技術協調 | Cross-department/vendor technical coordination, RFI management |
| D10.4 ★ | 合約技術管理 | Technical scope tracking against contract, deliverable acceptance criteria, technical dispute resolution |
| D10.5 ◆ | 系統除役與資產處置 | System decommissioning planning, data preservation, media sanitization, hardware disposal, R5 lifecycle management |

Boundary rule (D10/D14): Gate 0 approval / contract award is the lifecycle boundary. D14 operates Pre-Gate 0 → Gate 0. D10 operates post-contract kickoff → project closure including decommissioning (R1–R5). D14.1 scope framing feeds D10.1 requirements baseline.

**D11 — 工程治理 (6 subdomains, +1)**

| ID | Subdomain | Description |
|----|-----------|-------------|
| D11.1 | 設計審查 | Design review, stage-gate review, approval. ▲ GOV-SD defines 4-gate control framework (Gate 0–3) with explicit blocking conditions per gate, 12-item Gate 3 delivery checklist. |
| D11.2 | 工程流程標準化 | SOP definition, process documentation, continuous improvement. ▲ GOV-SDP establishes standards ownership system, exception ruling process, dispute escalation L1→L2→L3 with SLAs. |
| D11.3 | 品質管控 | Quality planning, audit execution, nonconformance management. ▲ GOV-SDP defines 7 functional roles with RACI mapping across all gates, role-based KPI evidence model. |
| D11.4 | 知識管理 | Knowledge capture, structuring, sharing, lessons learned |
| D11.5 | 標準與規範管理 | Internal design standards, external standards tracking |
| D11.6 ★◆▲ | 工程能力管理 | Engineering competency frameworks, training programs, qualification tracking（涵蓋安全能力作為首要實例化案例，並擴展至全領域工程能力認證；see ADR-006）. ▲ GOV-SDP provides SMART KPI definitions per role, RCW/AF/PVF scoring formula, annual governance cycle with data freeze and settlement. |

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
| D14.1 ◆ | 需求釐清與範圍框定 | Customer/stakeholder requirement elicitation, scope boundary definition, ambiguity resolution, requirement conflict resolution, preliminary requirement traceability |
| D14.2 ◆ | 現場勘查與技術探勘 | Physical site assessment, existing infrastructure inventory（含資產基線）, environmental constraints, brownfield integration assessment |
| D14.3 ◆▲ | 可行性評估與概念架構 | Technical feasibility analysis, concept system architecture, alternative comparison analysis, technology selection, POC design, preliminary Zone/Conduit concept. ▲ GOV-SD defines Pre-Gate Design Support role producing 5 Gate 0 inputs; output is advisory (non-binding). |
| D14.4 ▲ | 成本基礎與 BOM 工程 | Engineering-grade cost estimation, preliminary CBOM, labor hour baseline, vendor pricing, cost risk contingency. ▲ GOV-SD: CBOM = commercially quotable / design non-binding; EBOM supersedes at Gate 1. CBOM↔EBOM delta is business unit responsibility. |
| D14.5 ◆ | 利害關係人分析與介面清冊 | Stakeholder identification and expectation alignment, cross-system interface point enumeration, legacy system capability assessment, integration constraint summary |
| D14.6 | 前置風險評估與 Gate 0 輸入包 | Preliminary HLCRA, security classification input, risk-informed scope recommendations, Gate 0 decision package assembly |

FIX-003 說明：原 D14.5「基線清冊準備」與 D14.2「現場勘查」存在資產盤點功能重疊，已重定位為「利害關係人分析與介面清冊」，補充原 D14 缺少的利害關係人管理面向。原資產基線功能併入 D14.2。

D14 dependency connections: D14→D01 (HLCRA/security classification feeds TRA), D14→D02 (concept architecture feeds detailed design), D14→D09 (preliminary docs enter governance pipeline), D14→D10 (scope/cost baseline feeds project execution), D14→D11 (Gate 0 package feeds gate review). See `phase1-revision-r2.md` for full dependency diagram.

### Boundary Notes (R3 新增 ◆; R5 新增 ▲)

Boundary note for D03.4/D05.2 (REC-002): D03.4 涵蓋 VPP 的電力系統面（聚合策略、調度邏輯、市場參與規則），D05.2 涵蓋 VPP 的控制系統面（DERMS 軟體配置、通訊設定、即時控制迴路）。區分原則：標的為「電力系統行為」歸 D03.4，標的為「控制軟體配置」歸 D05.2。

Boundary note for D12.3/D13.2 (REC-001): D12.3 涵蓋以能源資料為標的的分析建模（含使用 AI/ML 作為工具），D13.2 涵蓋以工程流程為標的的 AI 輔助能力（如 AI 輔助設計審查、自動化文件生成）。區分原則：標的為「資料」歸 D12，標的為「工程流程」歸 D13。

▲ Boundary note for D01.2 (BOUNDARY-009, from GOV-SD): Design-time authority (Pre-Gate 0 through Gate 3) belongs to System Design Department. Execution-time (post-Gate 3 handover) belongs to project execution unit. Gate 3 handover = clean responsibility transfer; design approval ≠ risk acceptance (separate signers).

▲ Boundary note for D14.4 (BOUNDARY-010, from GOV-SD): CBOM (D14.4) = commercially quotable / design non-binding; produced by Pre-Gate Design Support. EBOM = design-binding; produced by System Architect at Gate 1+. CBOM↔EBOM delta is business unit responsibility, NOT design department responsibility.

### Approved Map Statistics (R5)

| Metric | Original | R1 | R2 | R3 | R5 |
|--------|----------|-----|-----|-----|-----|
| Level 1 Domains | 13 | 13 | 14 | 14 | **14** |
| Level 2 Subdomains | 66 | 69 | ~~75~~ 73 | 73 | **73** |
| Boundary clarifications | 0 | 3 | 4 | 6 | **10** (+BOUNDARY-007/008/009/010) |
| ADRs | 3 | 4 | 5 | 6 | **7** (+R5-ADR-001 Source Authority Hierarchy) |
| Source documents | 3 + PRAC | — | — | — | **19 + PRAC + 2 GOV** |
| Source tiers | 1 | — | — | — | **3** (Tier 1 Governance / Tier 2 Exemplar / Tier 3 Contextual) |

◆ERR 勘誤：R2 原宣稱 75 個子領域，實際加總為 73（D14 +6, D10 −2 = 淨 +4；69 + 4 = 73）。R2 誤將淨變動計為 +6，忽略 D10 縮減 −2。R3 修正。
