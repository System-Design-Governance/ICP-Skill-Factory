# ICP Skill Factory — Duplicate and Normalization Review

**Version:** R2 (2026-03-13)

### 7.1 Near-Duplicate Pairs Detected

| Pair | Candidate A | Candidate B | Verdict | Resolution |
|------|-------------|-------------|---------|------------|
| 1 | SC-D01-003 Firewall Rule Planning | SC-D01-004 Network Segmentation Documentation | NOT DUPLICATE | Different outputs: A produces rules, B produces documentation. Both retained. |
| 2 | SC-D01-006 TRA (Preliminary) | SC-D01-007 Detailed Risk Assessment | NOT DUPLICATE | Different lifecycle stages (R1 vs R2) and depth. Both retained as separate skills. |
| 3 | SC-D02-005 Protocol Architecture Design | SC-D05-009/010/011 Protocol Configuration | NOT DUPLICATE | D02.3 is architecture-level; D05.5 is device-level. Boundary rule CHG-004 applies. |
| 4 | SC-D01-012 Security Audit Execution | SC-D11-002 Stage-Gate Review Facilitation | NOT DUPLICATE | Audits verify compliance to standards; stage-gate reviews verify project milestone readiness. |
| 5 | SC-D09-007 SOP Development | SC-D11-004 Engineering SOP Development | MERGE | Both produce SOPs. **Resolution: Keep SC-D11-004 (governance owns the SOP process). Remove SC-D09-007 and reference SC-D11-004 from D09.** |
| 6 | SC-D10-008 Change Request Evaluation | SC-D10-009 MOC Execution | NOT DUPLICATE | Evaluation (analysis) vs. execution (management). Different skill types. |
| 7 | SC-D01-016 IR Procedure Development | SC-D01-017 Security Incident Investigation | NOT DUPLICATE | Writing the procedure vs. executing the investigation. Different lifecycle relevance. |

### 7.2 Normalization Actions

| Action | SC ID | Change | Rationale |
|--------|-------|--------|-----------|
| MERGE | SC-D09-007 | Remove; reference SC-D11-004 | SOP ownership belongs to governance |
| RENAME | SC-D08-005 | "System Security Acceptance Testing" → "Security Acceptance Testing Execution" | Verb-first consistency |
| RENAME | SC-D01-018 | "Continuous Security Monitoring" → "Security Monitoring Operations" | Clarify it's an ongoing operation |

### 7.3 Post-Normalization Count

After merging SC-D09-007 into SC-D11-004, the total candidate count is **149 skill candidates** across 14 domains (R2 revised).

### 7.4 Priority Candidates for Phase 3

The following 20 candidates are recommended for priority definition in Phase 3, based on: high confidence, high cross-domain impact, and criticality to ICP's core business:

| Priority | SC ID | Skill Name | Rationale |
|----------|-------|-----------|-----------|
| 1 | SC-D01-006 | Threat and Risk Assessment (Preliminary) | Foundation for all security decisions |
| 2 | SC-D01-007 | Detailed Risk Assessment | Key R2 deliverable |
| 3 | SC-D01-001 | Zone/Conduit Architecture Design | Core IEC 62443 skill |
| 4 | SC-D01-010 | SL-T Assessment | Drives all security requirements |
| 5 | SC-D01-011 | IEC 62443 Compliance Gap Analysis | Highest client-facing value |
| 6 | SC-D01-005 | Asset Inventory Development | Prerequisite for TRA |
| 7 | SC-D01-019 | Endpoint Hardening Implementation | Most common R3 deliverable |
| 8 | SC-D08-005 | Security Acceptance Testing Execution | Client handover gate |
| 9 | SC-D08-009 | Penetration Testing Execution | High-value verification skill |
| 10 | SC-D14-010 | Tender Security Requirements Definition | Business development critical (now in D14) |
| 11 | SC-D01-013 | Gate Review Preparation and Execution | Lifecycle governance backbone |
| 12 | SC-D02-001 | OT Network Topology Design | Architecture foundation |
| 13 | SC-D05-001 | SCADA Point List Development | Core control system skill |
| 14 | SC-D01-024 | Vendor Security Risk Assessment | Supply chain criticality |
| 15 | SC-D14-005 | CBOM Development | Revenue-critical (now in D14) |
| 16 | SC-D09-002 | Security Functional Description Specification | Key R3 document |
| 17 | SC-D11-002 | Stage-Gate Review Facilitation | Process governance core |
| 18 | SC-D01-020 | Account and Access Control Management | Highest-frequency security control |
| 19 | SC-D14-015 | Gate 0 Decision Package Assembly | Pre-gate lifecycle entry point |
| 20 | SC-D14-003 | Technical Feasibility Assessment | Pre-gate core engineering skill |
