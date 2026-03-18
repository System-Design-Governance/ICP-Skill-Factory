# Phase 4: Dependency Mapping — TODO

**Status:** Not Started
**Prerequisite:** Phase 3 (Skill Definitions) — at least priority batch of 20 skills defined

## Planned Deliverables

- [ ] `dependency-matrix.md` — Full skill dependency matrix (hard + soft dependencies)
- [ ] `composition-patterns.md` — Cross-domain skill composition patterns (CP-001, CP-002, ...)
- [ ] `visualizations/` — Dependency graph visualizations (D2/Mermaid)

## Key Tasks

1. Extract dependency declarations from Phase 3 skill definitions
2. Build adjacency matrix for all SK-xxx skills
3. Identify critical path chains (skills with most downstream dependents)
4. Detect circular dependencies and resolve
5. Identify cross-domain composition patterns
6. Generate visual dependency graphs per domain and cross-domain

## Notes

- D14 → D10 handoff chain is a known critical path
- D01 (OT Cybersecurity) has the highest expected fan-out
- Protocol subdomains (D02.3/D05.5/D07.2) need careful dependency tracing per CHG-004
