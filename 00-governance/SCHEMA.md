# ICP Skill Factory — Skill Registry Schema

**Version:** v1.2 (2026-03-18)
**Source:** Extracted from `skill-factory-deliverable.md` Section 2.4; extended in R4 review; v1.2 clarifies YAML vs prose structure per ADR-007
**Total Fields:** 27 (13 YAML metadata + 14 prose sections)

---

## Schema Structure (ADR-007)

Each SK-Dnn-nnn.md file consists of two parts:

1. **YAML Metadata Block** (inside ` ```yaml ` fenced code block under `## Metadata`) — 13 structured fields for machine-readable indexing
2. **Prose Sections** (individual `##` headers) — 14 human-readable sections providing detailed skill specification

This separation was an implicit design decision during Phase 3 batch authoring. Fields 8–17 in the original v1.0 flat schema evolved into prose sections because their content is inherently narrative (multi-paragraph descriptions, bulleted lists, structured tables) rather than single-value metadata. See `decisions/ADR-007-yaml-prose-separation.md`.

---

## Part A: YAML Metadata Fields (13 fields)

These fields appear inside the ` ```yaml ` block under `## Metadata`:

| # | Field | Type | Required | Description |
|---|-------|------|----------|-------------|
| 1 | `skill_id` | String | Yes | Canonical ID per CONVENTIONS.md §1 pattern |
| 2 | `skill_name_en` | String | Yes | English canonical name |
| 3 | `skill_name_zh` | String | Yes | Chinese display name |
| 4 | `domain_id` | FK → Domain | Yes | Parent Level 1 domain (D01–D14) |
| 5 | `subdomain_id` | FK → Subdomain | Yes | Parent Level 2 subdomain (D01.1–D14.6) |
| 6 | `skill_type` | Enum | Yes | One of: Analysis, Design, Engineering, Testing, Documentation, Management, Verification, Governance, Integration, Operations |
| 7 | `tier` | Enum | Yes | One of: T1-Domain, T2-CapabilityGroup, T3-Skill, T4-AtomicSubskill |
| 8 | `maturity` | Enum | Yes | Draft, Active, Deprecated, Retired |
| 9 | `version` | SemVer | Yes | Skill definition version (e.g., 1.0.0) |
| 10 | `created_date` | Date | Yes | When the skill was first registered |
| 11 | `confidence` | Enum | Yes | H+, H, M, L — extraction confidence |
| 12 | `owner` | String | No | Person or team responsible (e.g., "SAC (Security Architect)") |
| 13 | `tags` | Text[] | No | Free-form tags for search/filtering |

**Optional YAML field** (present in some files):

| # | Field | Type | Required | Description |
|---|-------|------|----------|-------------|
| 14 | `composition_patterns` | FK[] → CP | Optional / Deferred | Composition Patterns this skill participates in. Phase 4 (Dependency Mapping) was not executed; this field is empty (`[]`) in all 171 SK files. |

---

## Part B: Prose Sections (14 sections)

These appear as `##` headers after the YAML metadata block:

| # | Section Header | Required | Content |
|---|---------------|----------|---------|
| 1 | `## Description` | Yes | 2–4 sentence scope description; boundary clarification; key concepts |
| 2 | `## Inputs` | Yes | What this skill consumes (documents, data, upstream SK outputs) |
| 3 | `## Outputs` | Yes | What this skill produces (deliverables, artifacts, states) |
| 4 | `## Tools` | No | Typical tools/platforms used |
| 5 | `## Standards` | No | Applicable standards (IEC 62443, IEEE, NIST, ISO) |
| 6 | `## IEC 62443 Lifecycle Stages` | No | Applicable stages: Pre-R0, R0, R1, R2, R3, R4, R5 |
| 7 | `## Roles` | No | ICP roles that perform this skill |
| 8 | `## Dependencies` | No | Hard (required) and soft (enhancing) skill dependencies |
| 9 | `## Automation Potential` | No | Full, Partial, or Human-Only assessment with rationale |
| 10 | `## Acceptance Criteria` | Yes | Observable conditions that define "done well" (3–6 items) |
| 11 | `## Estimated Effort` | No | Junior vs. senior person-day baselines with project context |
| 12 | `## Composition Patterns` | No | Cross-reference to CP-nnn patterns (deferred to Phase 4) |
| 13 | `## Source Traceability` | Yes | Document IDs + section references tracing to source materials |
| 14 | `## Footer` | Yes | Version stamp line |

**Sections NOT present in SK definitions** (by design):

| Section | Status | Rationale |
|---------|--------|-----------|
| `## Workflow` / `## Process` | Not in SK | SK definitions are knowledge specifications, not operational procedures. Workflow steps are constructed in SKILL.md (Phase 5) from SK Description + Outputs + Acceptance Criteria. |
| `## Pitfalls` / `## Anti-patterns` | Not in SK | Domain-specific pitfalls are built in SKILL.md from practitioner knowledge and source documents, not extracted from SK definitions. Two SK files (SK-D02-001, SK-D03-001) contain ad-hoc pitfall sub-sections within Description, but this is not standardized. |

---

## Field Notes

### Tier Hierarchy
- **T1-Domain**: Top-level domain capability (e.g., "OT Cybersecurity")
- **T2-CapabilityGroup**: Subdomain-level grouping (e.g., "Risk Assessment & Threat Modeling")
- **T3-Skill**: Actionable engineering skill (e.g., "Detailed Risk Assessment")
- **T4-AtomicSubskill**: Smallest decomposable unit (e.g., "CVSS Scoring for OT Assets")

### Lifecycle Stages
- **Pre-R0**: Pre-project concept and feasibility (D14 domain)
- **R0**: Project initiation, scope definition
- **R1**: Security requirements, preliminary TRA
- **R2**: Detailed design, detailed risk assessment
- **R3**: Production, verification, validation
- **R4**: Operations and maintenance
- **R5**: Decommissioning

### Automation Potential
- **Full**: Can be fully automated by AI/tools (e.g., document generation, compliance checking)
- **Partial**: Requires human judgment with tool assistance (e.g., risk assessment, architecture review)
- **Human-Only**: Requires human expertise and cannot be automated (e.g., stakeholder negotiation, site survey)

### Acceptance Criteria
- Each criterion should be **observable and verifiable** (not subjective)
- Use the pattern: "[Deliverable/state] [verb] [measurable condition]"
- Example: "Zone/Conduit diagram covers 100% of identified assets"
- Example: "Risk register entries each include CVSS v3.1 score"
- Aim for 3–6 criteria per skill; avoid vague language like "adequate" or "appropriate"

### Estimated Effort
- Provides a baseline for CBOM labor estimation and project planning
- `junior`: Effort for a person with < 2 years domain experience
- `senior`: Effort for a person with 5+ years domain experience
- `notes`: Context (e.g., "assumes single-site deployment", "per 50 assets")
- These are planning baselines, not commitments; actual effort depends on project scope

### Composition Patterns
- References `CP-{nnn}` IDs defined in Phase 4 (dependency mapping)
- Phase 4 was not executed; this field is empty in all 171 SK files
- A skill may participate in multiple patterns (e.g., a risk assessment skill in both "Initial Security Assessment" and "Periodic Security Review" patterns)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-03-13 | Initial 27-field flat schema |
| v1.1 | 2026-03-13 | Added acceptance_criteria, estimated_effort, composition_patterns (R4 review) |
| v1.2 | 2026-03-18 | Clarified YAML (13) vs prose (14) separation; documented Workflow/Pitfalls absence; composition_patterns marked Optional/Deferred; added ADR-007 reference |
