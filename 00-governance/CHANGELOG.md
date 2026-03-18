# ICP Skill Factory — Change Log

All notable changes to the Skill Factory repository are documented here.

---

## [R5] — 2026-03-13

### 審查來源
- 16 new source documents (ID04–ID14 dummy project deliverables, ID21–ID25 organizational procedures)
- 2 governance repositories (GOV-SD: system-design, GOV-SDP: system-design-people) — **Tier 1 authoritative**
- User correction: dummy project = format exemplar only; actual governance from system-design + system-design-people folders

### Architecture Decision
- **R5-ADR-001**: Source Authority Hierarchy — 3-tier source classification (Tier 1 Governance > Tier 2 Exemplar > Tier 3 Contextual). When governance-level sources conflict with dummy project documents, governance prevails.

### Phase 1 Domain Map Update (Rolling)
- **CHG-019**: Domain map upgraded to R5. No new domains or subdomains. 10 subdomain descriptions enriched with ▲ governance annotations (D01.2, D01.3, D11.1–D11.3, D11.6, D14.3, D14.4).
- **CHG-020**: 4 new boundary rules added:
  - BOUNDARY-007: FAT/SAT/SIT Testing Distinction
  - BOUNDARY-008: Data Classification vs. Asset Classification
  - BOUNDARY-009: Design-Time vs. Execution-Time Authority (from GOV-SD)
  - BOUNDARY-010: CBOM vs. EBOM (from GOV-SD)

### Phase 2 Skill Candidate Update (Rolling)
- **CHG-021**: 23 new skill candidates added (8 from Tier 1 governance, 15 from Tier 2/3 exemplars)
  - Governance-derived (▲): SC-D01-035, SC-D01-036, SC-D11-017–SC-D11-021, SC-D14-018
  - Exemplar-derived (△): SC-D01-029–SC-D01-034, SC-D08-013–SC-D08-014, SC-D09-009, SC-D10-007, SC-D11-013–SC-D11-016, SC-D14-017
- **CHG-022**: SC-D11-002 (Stage-Gate Review Facilitation) superseded by SC-D11-017 (Gate Review Governance). SC-D11-002 retained as alias.
- **CHG-023**: 19 existing candidates upgraded to H+ confidence (Tier 2 exemplar + Tier 1 governance confirmation)
- **CHG-024**: Inventory legend updated with: source tier annotations, H+ confidence definition, R5 markers (▲△)

### Statistics
- Source documents: 3 + PRAC → **19 + PRAC + 2 GOV** (3 tiers)
- Domains: 14（不變）
- Subdomains: 73（不變）
- Boundary Rules: 6 → **10** (+4)
- ADRs: 6 → **7** (+R5-ADR-001)
- Skill candidates (pre-norm): 150 → **173** (+23)
- Skill candidates (post-norm): 149 → **171** (+22; SC-D11-002 superseded)
- H confidence: 73 → **75** (+21 new H, −19 upgraded to H+)
- H+ confidence: 0 → **19** (upgraded from H with Tier 2 exemplar + Tier 1 governance)
- H + H+ total: 73 → **94** (+21 net)
- M confidence: 64 → **67**
- L confidence: 13（不變）

---

## [R4] — 2026-03-13

### 審查來源
- Phase 3 啟動前模板審查（由 Victor Liu 核准全部 5 項調整）

### Schema Changes
- **CHG-015**: SCHEMA.md 從 24 欄位擴展為 **27 欄位**。新增：
  - #25 `acceptance_criteria`（驗收準則，Required）
  - #26 `estimated_effort`（預估工時，Optional）
  - #27 `composition_patterns`（組合模式，Optional）
- **CHG-016**: template.md 升級至 v1.1.0，對應新增 Acceptance Criteria、Estimated Effort、Composition Patterns 三個段落

### Convention Changes
- **CHG-017**: CONVENTIONS.md 新增 §5 Dependency Reference Rules，定義 SC-ID placeholder 機制（⏳ 標記），解決 Phase 3 撰寫時依賴目標尚未 promote 的問題

### Phase 3 Kickoff
- **CHG-018**: 產出首份 Golden Example — `SK-D01-001.md`（Zone/Conduit Architecture Design），作為後續批量撰寫的品質基準

### Bug Fix
- **ERR-002**: README.md 子領域計數由錯誤的 75 修正為 73（與 R3 CHANGELOG 一致）

### Statistics
- Schema fields: 24 → **27**
- Template version: 1.0.0 → **1.1.0**
- Skill definitions authored: 0 → **1** (SK-D01-001, golden example)
- Domains: 14（不變）
- Subdomains: 73（不變）
- Boundary Rules: 6（不變）
- ADRs: 6（不變）
- Skill candidates: 149（不變）

---

## [R3] — 2026-03-13

### 審查來源
- `01-domain-map/phase1-formal-review-r3.md`（正式獨立審查報告）

### Changed（必須修正 Mandatory Fixes）
- **CHG-011 (FIX-001)**: D08.6 系統除役遷移至 D10.5 系統除役與資產處置。除役為 R5 生命週期活動，歸屬測試域（R3）不當。D08 縮減為 5 個子領域，D10 擴充為 5 個子領域。
- **CHG-012 (FIX-002)**: D11.6 由「安全能力管理」更名為「工程能力管理」，泛化為跨域能力框架。安全能力作為首要實例化案例。新增 ADR-006。
- **CHG-013 (FIX-003)**: D14.5 由「基線清冊準備」重定位為「利害關係人分析與介面清冊」，消除與 D14.2 的資產盤點功能重疊。原資產基線功能併入 D14.2。
- **CHG-014 (REC-006)**: D14.1 補充「需求衝突解決」、D14.3 補充「方案比較分析」。

### Added（建議修正 Recommended Fixes）
- Boundary Rule: D03.4/D05.2 邊界（VPP 電力面 vs. 控制面）(REC-002)
- Boundary Rule: D12.3/D13.2 邊界（標的物原則：資料 vs. 流程）(REC-001)
- ADR-006: 工程能力管理通用化決策

### Skill Candidate Impact
- SC-D08-012 遷移至 SC-D10-006（System Decommissioning Execution）
- SC-D14-002 由 D14.1 遷至 D14.5（Stakeholder Analysis）
- SC-D11-011, SC-D11-012 更名（安全→工程能力/培訓）

### Bug Fix
- **ERR-001**: 子領域總數由宣稱 75 修正為實際 **73**。R2 誤算淨變動為 +6（實際 D14 +6, D10 −2 = +4；69 + 4 = 73）。

### Statistics
- Domains: 14（不變）
- Subdomains: **73**（R2 誤為 75，本次勘誤；±0 net: D08 −1, D10 +1, D14.5 重定位）
- Boundary Rules: 4 → 6
- ADRs: 5 → 6
- Skill candidates: 149（不變，僅遷移與更名）

---

## [R2] — 2026-03-13

### Added
- D14 PRE-GATE-ENGINEERING (前置技術工程) as new Level 1 domain with 6 subdomains (CHG-007)
- ADR-005: Pre-Gate Independence decision record (CHG-009)
- Dependency notes connecting D14 to D01, D02, D09, D10, D11 (CHG-010)
- 16 skill candidates under D14 (10 migrated from D10, 6 new)

### Changed
- D10 re-scoped to post-acceptance project technical management only (CHG-008)
- D10 reduced from 6 to 4 subdomains; pre-gate subdomains migrated to D14

### Statistics
- Domains: 13 → 14
- Subdomains: 66 → ~~75~~ 73（R3 勘誤：實際淨變動 +4 非 +6）
- ADRs: 4 → 5
- Skill candidates: 149 (post-normalization)

---

## [R1] — 2026-03-13

### Added
- D01.7 SIS 安全 (Safety Instrumented System Security) subdomain (CHG-001)
- D11.6 安全能力管理 (Security Competency Management) subdomain (CHG-002)
- D08.6 系統除役 (System Decommissioning) subdomain (CHG-003)
- Boundary rules for protocol subdomains D02.3/D05.5/D07.2 (CHG-004)
- Resolution rule for change management overlap D10.4/D11.2 (CHG-005)
- ADR-004: Skill ID Pattern decision

### Noted
- Naming inconsistency in English domain IDs flagged for future normalization (CHG-006)

### Statistics
- Domains: 13 (unchanged)
- Subdomains: 66 → 69
- ADRs: 3 → 4

---

## [v1.0] — 2026-03-13

### Added
- Initial Phase 1 domain map: 13 domains, 66 subdomains
- ADR-001: Protection Independence
- ADR-002: Data Platform Independence
- ADR-003: Engineering Automation
- Skill Registry Schema (24 fields)
- Repository framework and directory structure
- Extraction methodology and 150 skill candidates (pre-normalization)

---

## [Bootstrap] — 2026-03-13

### Added
- Repository directory structure created
- Governance files initialized (CONVENTIONS.md, SCHEMA.md, CHANGELOG.md)
- Source documents copied to `source-documents/`
- Consolidated deliverable split into individual phase files
- Skill definition template created
- Phase 4–7 TODO stubs created
