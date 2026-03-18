# ADR-005: Pre-Gate Engineering Independence

**Status:** Accepted
**Date:** 2026-03-13
**Context:** Phase 1 R2 Revision — D14 Domain Addition

## Decision

Establish D14 PRE-GATE-ENGINEERING (前置技術工程) as an independent Level 1 domain, separate from D10 PROJECT-ENGINEERING (專案工程). Use Gate 0 approval / contract award as the lifecycle boundary.

## Context

The original Phase 1 map placed pre-gate activities (requirements analysis, feasibility assessment, cost estimation, pre-sales technical support) under D10 alongside post-contract project management. This created a lifecycle mismatch: pre-gate work operates under uncertainty, concept-level fidelity, and business development constraints, while post-contract work operates under contractual scope, detailed engineering standards, and formal change control.

## Rationale

1. **Lifecycle clarity**: Pre-Gate 0 → Gate 0 is a fundamentally different operating context from post-contract execution. Different deliverable standards, approval authorities, and risk tolerances apply.
2. **Role clarity**: D14 is owned by the Concept System Architect / Feasibility Owner role, not the Project Manager. This is a technical execution domain, not a business development function.
3. **Data flow**: D14 produces inputs that D10 consumes (scope baseline, cost basis, preliminary architecture). Making this a formal domain boundary makes the handoff explicit and auditable.
4. **IEC 62443 alignment**: D14 maps to Pre-R0 lifecycle stage, filling a gap in the original R0-R5 mapping.

## Boundary Rule

- **D14**: Pre-Gate 0 → Gate 0 (concept, feasibility, preliminary architecture, cost basis, Gate 0 input package)
- **D10**: Post-contract kickoff → project closure (requirements tracking, change management, technical coordination, contract technical management)
- Gate 0 approval / contract award is the dividing line

## Dependencies

- D14 → D01: HLCRA / security classification feeds TRA
- D14 → D02: Concept architecture feeds detailed design
- D14 → D09: Preliminary docs enter governance pipeline
- D14 → D10: Scope/cost baseline feeds project execution
- D14 → D11: Gate 0 package feeds gate review

## Consequences

- D10 reduced from 6 to 4 subdomains (pre-gate subdomains migrated to D14)
- D14 has 6 subdomains and 16 skill candidates
- 10 skill candidates migrated from D10 to D14 with new SC-D14-xxx IDs
- Pre-R0 lifecycle stage now has a formal domain home
