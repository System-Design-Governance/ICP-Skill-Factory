# Phase 3 Execution Plan — Skill Definition Authoring

**Date:** 2026-03-13
**Status:** ACTIVE
**Schema:** 27-field (v1.1.0)
**Target:** 170 remaining skill definitions (171 total − 1 golden example)
**Quality Benchmark:** SK-D01-001 (Golden Example)

---

## 1. Execution Strategy

### Stage 1: H+ Candidates First (19 skills, Batches 1–4)

H+ candidates have both Tier 2 deliverable exemplars and Tier 1 governance confirmation, providing the richest source material for complete 27-field authoring. These span D01, D02, D08, D09, D11 — delivering immediate breadth.

### Stage 2: Gate Lifecycle Order (151 remaining, Batches 5–35+)

After H+ completion, remaining candidates are authored in lifecycle order:
Pre-R0 → R0/R1 → R2 → R3 → R4/R5

This follows the natural dependency chain (upstream skills first), minimizing ⏳ placeholder usage and simplifying Phase 4 dependency mapping.

### Batch Size: 5 per batch

Full 27-field authoring at Golden Example quality. Each batch produces 5 `SK-Dnn-nnn.md` files in `03-skill-definitions/registry/`.

---

## 2. Stage 1 Batch Plan — H+ Candidates

### Batch 1: D01 Risk & Asset Foundation

| # | SC ID → SK ID | Skill Name | Tier 2 Exemplar | Tier 1 Governance |
|---|---------------|-----------|-----------------|-------------------|
| 1 | SC-D01-005 → SK-D01-005 | Asset Inventory Development | ID09: 30-column asset inventory | GOV-SD: Gate 1 prerequisite |
| 2 | SC-D01-006 → SK-D01-006 | TRA (Preliminary) | ID11: 27-entry threat-vuln matrix | GOV-SD: Gate 1 Lite path; IEC 62443-3-2 |
| 3 | SC-D01-007 → SK-D01-007 | Detailed Risk Assessment | ID11: DTRA framework | GOV-SD: Gate 3 Complete (mandatory upgrade) |
| 4 | SC-D01-013 → SK-D01-013 | Gate Review Preparation and Execution | ID04 §10.0: Gate deliverable mapping | GOV-SD: 4-gate framework with blocking conditions |
| 5 | SC-D01-016 → SK-D01-016 | Incident Response Procedure Development | ID24: 4-level classification | — (org procedure) |

### Batch 2: D01 Hardening & Security Controls

| # | SC ID → SK ID | Skill Name | Tier 2 Exemplar | Tier 1 Governance |
|---|---------------|-----------|-----------------|-------------------|
| 6 | SC-D01-019 → SK-D01-019 | Endpoint Hardening Implementation | ID12 §4–5 + ID13 | GOV-SD: Gate 3 countermeasure evidence |
| 7 | SC-D01-020 → SK-D01-020 | Account and Access Control Management | ID07 §4.0 | GOV-SD: FR-SR verification |
| 8 | SC-D01-021 → SK-D01-021 | Security Patch Management | ID07 §8.0 | GOV-SD: Gate 2 change trigger |
| 9 | SC-D01-022 → SK-D01-022 | Backup and Restore Procedure Design | ID07 §6.0 | — |
| 10 | SC-D01-023 → SK-D01-023 | Malware Protection Implementation | ID07 §7.0 + ID12 §4.1–4.2 | GOV-SD: FR-SR verification |

### Batch 3: Cross-Domain (D01, D02, D08)

| # | SC ID → SK ID | Skill Name | Tier 2 Exemplar | Tier 1 Governance |
|---|---------------|-----------|-----------------|-------------------|
| 11 | SC-D01-024 → SK-D01-024 | Vendor Security Risk Assessment | ID05 + ID22 | GOV-SD: Gate 0 supply chain |
| 12 | SC-D02-004 → SK-D02-004 | Data Flow Diagram Development | ID08: 16 inter-zone data flows | GOV-SD: Zone/Conduit Gate 1 mandatory |
| 13 | SC-D02-011 → SK-D02-011 | Simple Network Diagram Development | ID10: Purdue level mapping | GOV-SD: Gate 1 input |
| 14 | SC-D08-001 → SK-D08-001 | FAT Procedure Development | ID14: 14-category protocol | GOV-SD: Gate 3 testing evidence |
| 15 | SC-D08-004 → SK-D08-004 | Site Acceptance Testing Execution | ID14: SAT categories | GOV-SD: SAT for Gate 3 |

### Batch 4: Cross-Domain (D08, D09, D11)

| # | SC ID → SK ID | Skill Name | Tier 2 Exemplar | Tier 1 Governance |
|---|---------------|-----------|-----------------|-------------------|
| 16 | SC-D08-005 → SK-D08-005 | Security Acceptance Testing Execution | ID14: SR 1.01–SR 2.05+ | GOV-SD: SR verification = Gate 3 blocker |
| 17 | SC-D09-002 → SK-D09-002 | Security Functional Desc Specification | ID12: 97-page SP mapping | GOV-SD: SR checklist feeder |
| 18 | SC-D11-011 → SK-D11-011 | Engineering Competency Framework Dev | ID21: QP-02 procedure | GOV-SDP: role-based competency + KPIs |
| 19 | SC-D11-012 → SK-D11-012 | Engineering Training Program Management | ID21: annual training plan | GOV-SDP: annual governance cycle |

---

## 3. Stage 2 Batch Plan — Lifecycle Order (Outline)

After Stage 1 completion (19 H+ done + 1 golden = 20/171), Stage 2 proceeds:

| Phase | Lifecycle | Domains | Est. Candidates | Est. Batches |
|-------|-----------|---------|----------------|-------------|
| 2A | Pre-R0 | D14 (primary) | ~16 | 3–4 |
| 2B | R0/R1 | D01, D02, D11 | ~25 | 5 |
| 2C | R2 | D01–D07, D11 | ~35 | 7 |
| 2D | R3 | D01, D05, D08, D09 | ~45 | 9 |
| 2E | R4/R5 | D01, D10, D11 | ~30 | 6 |

Total Stage 2: ~151 candidates / ~30 batches

---

## 4. Authoring Rules

### ID Promotion
- Candidates promote from `SC-Dnn-nnn` to `SK-Dnn-nnn` upon Phase 3 authoring
- File name: `SK-Dnn-nnn.md` in `03-skill-definitions/registry/`

### Dependency References
- Use ⏳ symbol for skills not yet authored (per CONVENTIONS.md §5)
- As Stage 1 completes, update earlier SK files to remove ⏳ from now-authored dependencies

### Governance Enrichment (R5 Rule)
For skills with Tier 1 governance confirmation:
- **Roles** section must reference the 7 GOV-SDP roles where applicable
- **Acceptance Criteria** must include gate-alignment criteria (which gate this feeds, blocking conditions)
- **Description** must note design-time vs. execution-time authority boundary where relevant

### Quality Checklist (per batch)
- [ ] All 27 fields populated (or explicitly marked N/A with rationale)
- [ ] Description includes scope boundary vs. adjacent skills
- [ ] Inputs reference upstream SK/SC IDs with ⏳ where applicable
- [ ] Acceptance criteria are observable and verifiable (no "adequate"/"appropriate")
- [ ] Source traceability includes both Tier 1 and Tier 2 references where H+
- [ ] Effort estimates are plausible relative to Golden Example baseline

---

## 5. Progress Tracker

| Batch | Stage | Candidates | Status | Date |
|-------|-------|-----------|--------|------|
| 0 | — | SK-D01-001 (Golden Example) | COMPLETE | 2026-03-13 |
| 1 | 1-H+ | SK-D01-005, 006, 007, 013, 016 | COMPLETE | 2026-03-13 |
| 2 | 1-H+ | SK-D01-019, 020, 021, 022, 023 | COMPLETE | 2026-03-13 |
| 3 | 1-H+ | SK-D01-024, SK-D02-004, 011, SK-D08-001, 004 | COMPLETE | 2026-03-13 |
| 4 | 1-H+ | SK-D08-005, SK-D09-002, SK-D11-011, 012 | COMPLETE | 2026-03-16 |
| 5 | 2A-PreR0 | SK-D14-001, 010, 011, 012, 014 | COMPLETE | 2026-03-16 |
| 6 | 2A-PreR0 | SK-D14-003, 005, 006, 008, 015 | COMPLETE | 2026-03-16 |
| 7 | 2A-PreR0 | SK-D14-017, 018, 002, 004, 007 | COMPLETE | 2026-03-16 |
| 8 | 2A+R0 | SK-D14-009, 013, 016 + SK-D11-004, 013, 015, 016, 017, 019 | COMPLETE | 2026-03-16 |
| 9 | 2B-R0/R1 | SK-D01-009, 010, 029, 031, 033 | COMPLETE | 2026-03-16 |
| 10 | 2B-R0/R1 | SK-D01-002, 008, 011, 030, 035 | COMPLETE | 2026-03-16 |
| 11 | 2B-R0/R1 | SK-D02-001, 005, 009, 010, SK-D11-006 | COMPLETE | 2026-03-16 |
| 12 | 2B-R1/R2 | SK-D03-001, 002, 004, 005, 007 | COMPLETE | 2026-03-16 |
| 13 | 2B-R1 | SK-D06-006, SK-D09-005, SK-D10-001, 002, 003 | COMPLETE | 2026-03-16 |
| 14 | 2B-R1 | SK-D10-004, 005, SK-D01-036, SK-D11-014, 021 | COMPLETE | 2026-03-16 |
| 15 | 2C-R2 | SK-D01-003, 004, 026, 027, SK-D02-002 | COMPLETE | 2026-03-16 |
| 16 | 2C-R2 | SK-D02-003, 006, 007, 008, 012 | COMPLETE | 2026-03-16 |
| 17 | 2C-R2 | SK-D03-003, 006, 008, 009, 010 | COMPLETE | 2026-03-16 |
| 18 | 2C-R2 | SK-D04-001, 002, 004, SK-D05-001, 002 | COMPLETE | 2026-03-16 |
| 19 | 2C-R2 | SK-D05-005, 006, 013, 014, SK-D06-001 | COMPLETE | 2026-03-16 |
| 20 | 2C-R2 | SK-D06-002, 003, 004, 005, SK-D07-001 | COMPLETE | 2026-03-16 |
| 21 | 2C-R2 | SK-D07-002, 004, 005, 006, SK-D09-001 | COMPLETE | 2026-03-16 |
| 22 | 2C-R2 | SK-D09-003, SK-D11-001, 003, 020, SK-D12-001 | COMPLETE | 2026-03-16 |
| 23 | 2C-R2 | SK-D12-003, 004, 007, 008, SK-D13-001 | COMPLETE | 2026-03-16 |
| 24 | 2C-R2 | SK-D04-003, SK-D05-003, 004, 007, 008 | COMPLETE | 2026-03-16 |
| 25 | 2C-R2 | SK-D12-002, 005, SK-D13-003, 004, 006 + SK-D11-010, 018 | COMPLETE | 2026-03-16 |
| 26 | 2D-R3 | SK-D01-014, 015, 025, 028, 034 | COMPLETE | 2026-03-16 |
| 27 | 2D-R3 | SK-D04-006, SK-D05-009, 010, 011, 012 | COMPLETE | 2026-03-16 |
| 28 | 2D-R3 | SK-D07-003, 007, SK-D08-002, 003, 006 | COMPLETE | 2026-03-16 |
| 29 | 2D-R3 | SK-D08-007, 008, 009, 010, 011 | COMPLETE | 2026-03-16 |
| 30 | 2D-R3 | SK-D08-013, 014, SK-D09-004, 006, 008 | COMPLETE | 2026-03-16 |
| 31 | 2D-R3 | SK-D09-009, SK-D10-007, SK-D11-007, SK-D12-006, SK-D13-002, 005 | COMPLETE | 2026-03-16 |
| 32 | 2E-R4 | SK-D01-012, 017, 018, 032, SK-D04-005 | COMPLETE | 2026-03-16 |
| 33 | 2E-R4/R5 | SK-D10-006, SK-D11-005, 008, 009 | COMPLETE | 2026-03-16 |

**Phase 3 COMPLETE: 171/171 skills authored (2026-03-16)**
