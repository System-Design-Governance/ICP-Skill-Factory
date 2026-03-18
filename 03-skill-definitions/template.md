# Skill Definition Template

Use this template to create full skill definitions in Phase 3. Copy this file and rename to `SK-D{nn}-{nnn}.md`.

---

## Metadata

```yaml
skill_id: SK-D00-000
skill_name_en: "[Verb-Noun Phrase]"
skill_name_zh: "[中文技能名稱]"
domain_id: D00
subdomain_id: D00.0
skill_type: Analysis | Design | Engineering | Testing | Documentation | Management | Verification | Governance | Integration | Operations
tier: T3-Skill
maturity: Draft
version: 1.0.0
created_date: YYYY-MM-DD
confidence: High | Medium | Low
owner: "[Person or Team]"
tags: []
composition_patterns: []
```

## Description

[2–4 sentence scope description. What does this skill do? What problem does it solve? What is the boundary of this skill versus related skills?]

## Inputs

- [Document, data, or decision this skill consumes]
- [Example: "Asset inventory from SC-D01-005"]
- [Example: "Customer requirements specification"]

## Outputs

- [Deliverable, artifact, or state this skill produces]
- [Example: "Threat and Risk Assessment Report"]
- [Example: "Updated risk register with CVSS scores"]

## Tools

- [Typical tools/platforms used]
- [Example: "ETAP, PSS/E, Microsoft Visio"]

## Standards

- [Applicable standards]
- [Example: "IEC 62443-3-2, IEC 62443-3-3"]

## IEC 62443 Lifecycle Stages

- [Pre-R0 | R0 | R1 | R2 | R3 | R4 | R5]

## Roles

- [ICP roles that perform this skill]
- [Example: "SAC (Security Architect), STC (Security Technical Consultant)"]

## Dependencies

### Hard Dependencies (Required Before Execution)

- [SK-D00-000: Skill Name — reason]

### Soft Dependencies (Enhances Effectiveness)

- [SK-D00-000: Skill Name — reason]

## Automation Potential

**Level:** Full | Partial | Human-Only

[1–2 sentence justification. What parts can be automated? What requires human judgment?]

## Acceptance Criteria

- [Observable, verifiable condition that defines "done well"]
- [Example: "Zone/Conduit diagram covers 100% of identified assets"]
- [Example: "Risk register entries each include CVSS v3.1 score"]
- [Aim for 3–6 criteria; avoid vague language like "adequate" or "appropriate"]

## Estimated Effort

| Level | Effort | Notes |
|-------|--------|-------|
| Junior (< 2 yr) | [N person-days] | [Assumptions, e.g., "single-site, ~50 assets"] |
| Senior (5+ yr) | [N person-days] | [Assumptions] |

## Composition Patterns

- [CP-{nnn}: Pattern Name — role this skill plays in the pattern]
- [Leave empty during Phase 3; populate in Phase 4]

## Source Traceability

- [Document ID + section reference]
- [Example: "ID01 §7.2; ID02 A.8"]
- [Example: "PRAC — industry standard practice"]

---

*Template version: 1.1.0 | Schema: 27 fields | See `00-governance/SCHEMA.md` for field definitions*
