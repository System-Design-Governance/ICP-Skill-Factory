# ICP Skill Factory — Naming and ID Conventions

**Version:** v1.1 (2026-03-13)
**Source:** Extracted from `skill-factory-deliverable.md` Section 2

---

## 1. Skill ID Pattern (ADR-004)

**Format:** `SK-D{nn}-{nnn}` (Hybrid: Stable Domain Prefix + Sequential Skill Number)

| Entity | Pattern | Example | Notes |
|--------|---------|---------|-------|
| Domain (Level 1) | `D{nn}` | `D01` | Stable; from Phase 1 |
| Subdomain (Level 2) | `D{nn}.{n}` | `D01.2` | Stable; from Phase 1 |
| Skill Candidate | `SC-D{nn}-{nnn}` | `SC-D01-017` | Pre-validation |
| Skill (Validated) | `SK-D{nn}-{nnn}` | `SK-D01-003` | Promoted from SC |
| Sub-skill (Atomic) | `SK-D{nn}-{nnn}.{a}` | `SK-D01-003.a` | Alphabetic suffix |
| Composition Pattern | `CP-{nnn}` | `CP-001` | Cross-domain patterns |
| Decision Record | `ADR-{nnn}` | `ADR-004` | Architecture decisions |

### Why This Pattern

1. Domain prefix provides instant human readability without full lookup
2. Sequential number is stable under subdomain reorganization
3. The SC → SK promotion path gives a clear lifecycle signal
4. The `.a` / `.b` sub-skill notation avoids deep nesting while allowing decomposition
5. Zero-padded 3-digit sequence supports up to 999 skills per domain

---

## 2. Naming Conventions

1. **Bilingual requirement**: Every skill has both an English canonical name (used in IDs, APIs, machine contexts) and a Chinese display name (used in UI, reports, training).
   - Example: `SK-D01-003` → EN: "Zone/Conduit Topology Design" / ZH: "Zone/Conduit 拓撲設計"

2. **Name format**: English names use Title Case with no abbreviations except industry-standard ones:
   - Allowed abbreviations: SCADA, EMS, DERMS, VPP, HMI, PLC, RTU, SIEM, SBOM, TRA, FAT, SAT, OPC UA

3. **Verb-first for action skills**: Skills representing actions start with a verb:
   - "Perform TRA", "Design Zone/Conduit Architecture", "Execute FAT Procedure"

4. **Noun-first for knowledge skills**: Skills representing knowledge domains use noun phrases:
   - "IEC 62443 Compliance Framework", "Power System Protection Theory"

5. **No redundant domain prefix in name**: Since the domain is encoded in the ID, the name should not repeat it.
   - Bad: "OT Cybersecurity Risk Assessment"
   - Good: "Risk Assessment and Threat Modeling"

---

## 3. Skill Type Taxonomy

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

## 4. Overlap Resolution Rules

### Protocol Subdomains (CHG-004)
- **D02.3** = Architecture-level protocol selection and topology design
- **D05.5** = Device-level protocol configuration and gateway setup
- **D07.2** = Cross-system protocol translation

### Change Management (CHG-005)
- **D10.2** = Project-specific change requests (execution)
- **D11.2** = Standard operating procedure that D10.2 instances follow (governance)

### Pre-Gate / Post-Gate Boundary (ADR-005)
- **D14** = Pre-Gate 0 → Gate 0（合約簽訂前的技術執行）
- **D10** = Post-contract kickoff → project closure including decommissioning（R1–R5）
- Gate 0 approval / contract award is the lifecycle boundary
- D14.1 scope framing feeds D10.1 requirements baseline

### VPP 電力面 / 控制面邊界（REC-002, R3 新增）
- **D03.4** = VPP 的電力系統面：聚合策略、調度邏輯、市場參與規則
- **D05.2** = VPP 的控制系統面：DERMS 軟體配置、通訊設定、即時控制迴路
- 區分原則：標的為「電力系統行為」歸 D03.4，標的為「控制軟體配置」歸 D05.2

### 資料分析 / AI 輔助工程邊界（REC-001, R3 新增）
- **D12.3** = 以能源資料為標的的分析建模（含使用 AI/ML 作為工具）
- **D13.2** = 以工程流程為標的的 AI 輔助能力（如 AI 輔助設計審查、自動化文件生成）
- 區分原則：標的為「資料」歸 D12，標的為「工程流程」歸 D13

### 能力管理歸屬（ADR-006, R3 新增）
- **D11.6** = 工程能力管理（通用），涵蓋所有領域的能力框架、培訓、資格追蹤
- 安全能力（源自 ID03 §5.3.3）為首要實例化案例
- 各領域專業能力認證（D03 電力、D04 保護等）統一於 D11.6 管理，不在各域重複建立

---

## 5. Dependency Reference Rules

### SC-ID Placeholder During Phase 3

During Phase 3 skill authoring, many dependencies reference skills that have not yet been promoted from SC (candidate) to SK (validated). The following rules apply:

1. **Use SC-ID as placeholder**: When a dependency target has not yet been authored as a full SK definition, reference it by its SC-ID (e.g., `SC-D01-005`).
2. **Mark with `⏳`**: Append the ⏳ symbol to indicate the reference is a placeholder awaiting promotion.
   - Example: `SC-D01-005 ⏳: Asset Inventory Development — provides the asset baseline`
3. **Promotion updates**: When the target skill is authored and promoted to SK, all placeholder references should be updated in a single pass per batch.
4. **Phase 4 reconciliation**: Phase 4 (Dependency Mapping) will perform a full cross-reference audit to ensure no stale SC-IDs remain.

---

## 6. File Naming Conventions

- Kebab-case for all file names: `phase1-domain-map-approved.md`
- Phase-prefixed folder numbering: `00-governance/`, `01-domain-map/`, etc.
- ADR files: `ADR-{nnn}-{short-description}.md`
- Skill definition files: `SK-D{nn}-{nnn}.md`
