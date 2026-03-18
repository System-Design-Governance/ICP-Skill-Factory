# ICP Skill Factory — Extraction Methodology (Phase 2)

**Version:** v1.0 (2026-03-13)

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
