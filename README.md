# ICP Skill Factory

**Domain Skill Governance System for Energy Systems Engineering**

This repository is the single source of truth for ICP's engineering skill taxonomy, registry, and governance. It covers OT cybersecurity, SCADA/EMS/DERMS, power systems, protection engineering, VPP, industrial automation, and pre-gate engineering.

## Repository Structure

```
icp-skill-factory/
├── 00-governance/            Cross-cutting governance artifacts
│   ├── CONVENTIONS.md        Naming, ID rules, style guide
│   ├── SCHEMA.md             Skill Registry Schema (v1.2: 13 YAML + 14 prose)
│   ├── CHANGELOG.md          Cross-phase change log
│   └── decisions/            Architecture Decision Records (ADR-001–007)
├── 01-domain-map/            Phase 1: Domain taxonomy
│   └── phase1-domain-map-approved.md   Approved baseline (R5)
├── 02-skill-candidates/      Phase 2: Capability extraction
│   ├── extraction-methodology.md       How candidates were extracted
│   ├── skill-candidate-inventory.md    171 candidates across 14 domains (R5)
│   └── sources/                        Per-source extraction notes
├── 03-skill-definitions/     Phase 3: Full skill authoring (COMPLETE, frozen)
│   ├── template.md           27-field skill definition template (v1.1.0)
│   └── registry/             171 individual skill files (SK-Dnn-nnn.md)
├── 04-review/                Forensic reviews and audit reports
├── 05-cowork-skills/         Phase 5/6: Claude Cowork SKILL.md + Plugins
│   ├── {skill-name}/SKILL.md     51 executable skill specifications
│   ├── {skill-name}/templates/   Skill-specific templates
│   ├── {skill-name}/references/  Skill-specific references
│   ├── packages/                 51 .skill ZIP packages
│   └── plugins/                  5 role-based .plugin ZIP packages
├── 06-plugin-src/            Plugin packaging source (5 plugins, 51 skills)
├── source-documents/         Input PDFs + governance repositories
│   ├── ID01–ID14 (*.pdf)         Tier 2: Exemplar project documents
│   ├── ID21–ID25 (*.pdf)         Tier 3: Organizational procedures
│   ├── system-design/            Tier 1: System Design Governance Charter
│   ├── system-design-people/     Tier 1: Role definitions, JD & KPI
│   └── project-governance/       Power Platform governance (tangential reference)
├── _archive/                 Historical snapshots and superseded plans
├── build-packages.py         Plugin/Skill ZIP packaging tool
└── README.md
```

## Current Status

| Phase | Status | Key Metric |
|-------|--------|-----------|
| Phase 1: Domain Map | **COMPLETE** (R5) | 14 domains, 73 subdomains, 10 boundary rules |
| Phase 2: Skill Extraction | **COMPLETE** (R5) | 171 candidates post-normalization; 3-tier source hierarchy |
| Phase 3: Skill Definitions | **COMPLETE** (frozen) | 171/171 authored; schema v1.2 (13 YAML + 14 prose) |
| Phase 5/6: Cowork Skills | **COMPLETE** | 51/51 SKILL.md deep-enhanced; 59 resource files; Final Review PASS |
| Plugin Packaging | **COMPLETE** | 5 .plugin + 51 .skill ZIP packages built |
| Phase 7: Evolution | **PLANNED** | Pending real-world deployment feedback |

### Skill Quality Tiers

| Tier | Count | Avg Lines | Description |
|------|-------|-----------|-------------|
| A+ (≥500L) | 4 | 649 | Operations manual grade (arch-diagram, cbom-builder, threat-risk-assessment, presales) |
| A (250-499L) | 3 | 277 | Deep enhanced (security-monitoring, security-hardening, compliance-gap-assessor) |
| B (100-249L) | 42 | ~170 | Standard enhanced, production-ready |
| C (<100L) | 2 | 96 | Content complete, slightly short |

**Total**: 9,747 lines across 51 SKILL.md | 59 templates/references

### 5 Role-Based Plugins

| Plugin | Role | Skills |
|--------|------|--------|
| icp-seceng | SAC (Security Engineering) | 10 |
| icp-sysarch | SYS (System Architecture) | 16 |
| icp-integration | SYS (Integration & Verification) | 13 |
| icp-governance | GOV (Engineering Governance) | 7 |
| icp-presales | PGS (Pre-Gate Support) | 5 |

### SK Traceability

- 51 SKILL.md reference **171/171** SK definitions (100% coverage)
- 0 SK omitted, 0 SK duplicated across skills

## Key References

- **Skill ID Pattern**: `SK-D{nn}-{nnn}` — see `00-governance/CONVENTIONS.md`
- **Schema**: see `00-governance/SCHEMA.md` (v1.2 — YAML/prose separation)
- **Architecture Decisions**: see `00-governance/decisions/ADR-001` through `ADR-007`
- **Approved Domain Map**: see `01-domain-map/phase1-domain-map-approved.md`
- **Final Review**: see `04-review/phase5-final-review.md`
- **Progress Forensics**: see `04-review/project-progress-forensics-2026-03-19.md`

## Source Documents Note

`source-documents/project-governance/` contains Power Platform governance documentation (v5.0). This is a separate institutional governance system that is **tangentially related** to the Skill Factory. It serves as a reference for governance methodology patterns but is not a direct input to SK definitions.

## Owner

Victor Liu, Intelligent Cloud Plus Corp (ICP)
