# ICP Skill Factory

**Domain Skill Governance System for Energy Systems Engineering**

This repository is the single source of truth for ICP's engineering skill taxonomy, registry, and governance. It covers OT cybersecurity, SCADA/EMS/DERMS, power systems, protection engineering, VPP, industrial automation, and pre-gate engineering.

## Repository Structure

```
icp-skill-factory/
├── 00-governance/          Cross-cutting governance artifacts
│   ├── CONVENTIONS.md      Naming, ID rules, style guide
│   ├── SCHEMA.md           Skill Registry Schema (v1.2: 13 YAML + 14 prose)
│   ├── CHANGELOG.md        Cross-phase change log
│   └── decisions/          Architecture Decision Records (ADR-001–007)
├── 01-domain-map/          Phase 1: Domain taxonomy
│   ├── phase1-skill-domain-map.md      Original map (preserved)
│   ├── phase1-review-changelog.md      Stage B review findings
│   ├── phase1-revision-r2.md           R2 revision document
│   └── phase1-domain-map-approved.md   Approved baseline for Phase 2
├── 02-skill-candidates/    Phase 2: Capability extraction
│   ├── extraction-methodology.md       How candidates were extracted
│   ├── skill-candidate-inventory.md    171 candidates across 14 domains (R5)
│   ├── duplicate-normalization-review.md  Dedup analysis
│   └── sources/                        Per-source extraction notes
├── 03-skill-definitions/   Phase 3: Full skill authoring (COMPLETE, Phase 4 凍結)
│   ├── template.md         27-field skill definition template (v1.1.0)
│   └── registry/           171 individual skill files (SK-Dnn-nnn.md)
├── 04-review/              Review reports and plans (Phase 3–5)
├── 05-cowork-skills/       Phase 5: Claude Cowork SKILL.md + Plugins
│   ├── {skill-name}/SKILL.md   51 executable skill specifications
│   └── plugins/                5 role-based .plugin packages
├── source-documents/       Input PDFs + governance repositories
│   ├── ID01–ID14 (*.pdf)       Tier 2: Exemplar project documents
│   ├── ID21–ID25 (*.pdf)       Tier 3: Organizational procedures
│   ├── system-design/          Tier 1: System Design Governance Charter
│   ├── system-design-people/   Tier 1: Role definitions, JD & KPI
│   └── project-governance/     Power Platform governance (tangentially related)
├── 04-dependency-map/      Phase 4: Dependency mapping (not executed)
├── 05-conflict-analysis/   Phase 5: Overlap analysis (planned)
├── 06-refactoring/         Phase 6: Taxonomy refactoring (planned)
└── 07-evolution/           Phase 7: Governance and evolution (planned)
```

## Current Status

| Phase | Status | Key Metric |
|-------|--------|-----------|
| Phase 1: Domain Map | COMPLETE (R5) | 14 domains, 73 subdomains, 10 boundary rules |
| Phase 2: Skill Extraction | COMPLETE (R5) | 171 candidates post-normalization; 3-tier source hierarchy |
| Phase 3: Skill Definitions | COMPLETE | 171/171 authored; schema v1.2 (13 YAML + 14 prose); Phase 4 review passed |
| Phase 5: Cowork Skills | IN PROGRESS | 51 SKILL.md; 5 Plugins; 5/51 production-grade (Tier A) |
| Phase 4 Dependency Map | NOT EXECUTED | composition_patterns deferred |
| Phase 6–7 | PLANNED | See TODO files |

### Phase 5 Maturity

| Tier | Skills | Avg Lines | Status |
|------|--------|-----------|--------|
| A (Production) | 5 (arch-diagram, cbom-builder, presales, compliance-gap-assessor, threat-risk-assessment) | 507 | Verified, deployable |
| B (Skeleton) | 46 | ~199 | Structure complete, needs deep content |

### 5 Role-Based Plugins

| Plugin | Role | Skills |
|--------|------|--------|
| icp-seceng | SAC (Security Engineering) | 10 |
| icp-sysarch | SYS (System Architecture) | 16 |
| icp-integration | SYS (Integration & Verification) | 13 |
| icp-governance | GOV (Engineering Governance) | 7 |
| icp-presales | PGS (Pre-Gate Support) | 5 |

## Key References

- **Skill ID Pattern**: `SK-D{nn}-{nnn}` — see `00-governance/CONVENTIONS.md`
- **Schema**: see `00-governance/SCHEMA.md` (v1.2 — YAML/prose separation)
- **Architecture Decisions**: see `00-governance/decisions/ADR-001` through `ADR-007`
- **Approved Domain Map**: see `01-domain-map/phase1-domain-map-approved.md`
- **Forensic Review**: see `04-review/full-forensic-review.md`

## Source Documents Note

- `source-documents/project-governance/` contains Power Platform governance documentation (v5.0). This is a separate institutional governance system that is **tangentially related** to the Skill Factory. It serves as a reference for governance methodology patterns but is not a direct input to SK definitions.

## Owner

Victor Liu, Intelligent Cloud Plus Corp (ICP)
