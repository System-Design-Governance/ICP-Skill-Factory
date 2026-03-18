# Domain Skill Governance System — Project Work Plan

**Project:** Energy Systems Engineering Skill Architecture
**Coordinator:** Claude (AI Project Coordinator)
**Owner:** Victor Liu, ICP
**Date:** 2026-03-13
**Team Size:** Small (5–15 engineers/architects)
**Target Granularity:** Full decomposition (~100+ atomic skills)

---

## 1. Project Overview

This project designs, validates, and establishes a complete Skill Governance System for an engineering domain spanning Energy Systems, SCADA/EMS/DERMS, Virtual Power Plants, OT/IT cybersecurity, and engineering automation. The system will serve human engineers, system architects, AI agents, and automation workflows as the authoritative registry of capabilities, dependencies, and evolution paths.

### Success Criteria

- Every capability in the domain is represented as a named, scoped, versioned skill
- Dependency graph is complete and acyclic at the composition layer
- Overlap between skills is explicitly documented with resolution rules
- The architecture supports AI agent skill selection and chaining
- A forward-looking roadmap identifies emerging skills and automation candidates

---

## 2. Phase Breakdown

### Phase 1 — Domain Skill Discovery

**Purpose:** Exhaustively enumerate all capabilities present in the domain before imposing any structure. This raw inventory prevents premature categorization from hiding important skills.

| Task | Description | Priority | Est. Effort |
|------|-------------|----------|-------------|
| 1.1 Seed skill list from domain descriptions | Extract candidate skills from each of the 11 domain areas listed in the project context | Critical | 1 session |
| 1.2 Expand via capability decomposition | For each domain area, ask "what atomic actions can an engineer or agent perform?" and list them | Critical | 1–2 sessions |
| 1.3 Cross-reference industry standards | Map skills against IEC 62443, IEEE 2030, IEC 61850, NERC CIP, and relevant NIST frameworks to find compliance-driven skills | High | 1 session |
| 1.4 Identify tooling-implied skills | Examine typical tool stacks (SCADA platforms, EMS, DERMS, data lakes, CI/CD pipelines) and extract skills they imply | High | 1 session |
| 1.5 Capture tacit/workflow skills | Identify skills that live in processes rather than tools — incident response, design review, commissioning, handoff procedures | Medium | 1 session |
| 1.6 Consolidate raw inventory | Merge, de-duplicate, and tag each candidate skill with source and confidence level | Critical | 0.5 session |

**Expected Output:** Raw skill inventory (flat list, ~120–180 candidate skills), each tagged with domain area, source, and initial confidence.

---

### Phase 2 — Skill Architecture Design

**Purpose:** Impose a hierarchical structure on the raw inventory. Define layers, categories, and naming conventions that will govern the entire system.

| Task | Description | Priority | Est. Effort |
|------|-------------|----------|-------------|
| 2.1 Define architecture layers | Establish 3–4 layers: Domain → Capability Group → Skill → Sub-skill (atomic) | Critical | 0.5 session |
| 2.2 Define category taxonomy | Create the top-level groupings (e.g., Power Systems, Control Systems, Cybersecurity, Data Platforms, Engineering Process) | Critical | 1 session |
| 2.3 Establish naming conventions | Define skill ID format, versioning scheme, and metadata schema | High | 0.5 session |
| 2.4 Map skills to architecture | Place every raw skill into the hierarchy; flag orphans and mismatches | Critical | 1–2 sessions |
| 2.5 Validate coverage | Check each domain area has adequate skill coverage; identify gaps | High | 0.5 session |
| 2.6 Define skill metadata schema | Specify the fields every skill definition must carry (ID, name, scope, inputs, outputs, tools, owner, maturity, etc.) | Critical | 0.5 session |

**Expected Output:** Skill Architecture Diagram (tree structure), Naming Convention Spec, Metadata Schema, and initial skill-to-category mapping.

---

### Phase 3 — Skill Definition

**Purpose:** Write the full definition for every skill in the architecture. Each definition is precise enough for an AI agent to determine whether it possesses the skill and for a human to assess proficiency.

| Task | Description | Priority | Est. Effort |
|------|-------------|----------|-------------|
| 3.1 Define template | Finalize the skill definition template with all required and optional fields | Critical | 0.5 session |
| 3.2 Write Tier-1 definitions (Domain-level) | Define the ~5–7 top-level domain skills | High | 0.5 session |
| 3.3 Write Tier-2 definitions (Capability Groups) | Define the ~15–25 capability group skills | Critical | 1–2 sessions |
| 3.4 Write Tier-3 definitions (Skills) | Define the ~40–60 core skills with full scope, inputs, outputs, tooling | Critical | 2–3 sessions |
| 3.5 Write Tier-4 definitions (Atomic Sub-skills) | Define the ~50–80 atomic sub-skills | High | 2–3 sessions |
| 3.6 Peer review pass | Cross-check definitions for consistency, completeness, and boundary clarity | Critical | 1 session |

**Expected Output:** Complete Skill Definition Registry (~100–150 entries), each with full metadata.

---

### Phase 4 — Skill Dependency Mapping

**Purpose:** Identify which skills require, enable, or enhance other skills. This graph powers AI agent planning, training path design, and impact analysis.

| Task | Description | Priority | Est. Effort |
|------|-------------|----------|-------------|
| 4.1 Define dependency types | Establish relationship vocabulary: requires, enhances, enables, composes, conflicts-with | Critical | 0.5 session |
| 4.2 Map hard dependencies | For each skill, list skills it cannot function without | Critical | 1–2 sessions |
| 4.3 Map soft dependencies | For each skill, list skills that improve its effectiveness | High | 1 session |
| 4.4 Map composition patterns | Identify common skill chains (e.g., "feasibility assessment" = architecture-design + compliance-check + cost-estimation) | High | 1 session |
| 4.5 Validate acyclicity | Check the hard-dependency graph for cycles; resolve any found | Critical | 0.5 session |
| 4.6 Generate dependency visualization | Produce a dependency graph (Mermaid or D2) | Medium | 0.5 session |

**Expected Output:** Dependency matrix, composition patterns catalog, dependency graph visualization, cycle analysis report.

---

### Phase 5 — Skill Conflict Analysis

**Purpose:** Detect overlapping scopes, redundant skills, and boundary ambiguities that would confuse agents or create governance disputes.

| Task | Description | Priority | Est. Effort |
|------|-------------|----------|-------------|
| 5.1 Pairwise overlap detection | Compare every skill pair within the same capability group for scope overlap | Critical | 1–2 sessions |
| 5.2 Cross-group overlap detection | Compare skills across capability groups that share similar inputs/outputs/tools | High | 1 session |
| 5.3 Redundancy classification | Classify overlaps as: exact duplicate, partial overlap, complementary, or false positive | Critical | 0.5 session |
| 5.4 Boundary ambiguity report | Document cases where two skills have unclear boundaries and propose resolution | High | 0.5 session |
| 5.5 Agent selection conflict analysis | Simulate scenarios where an AI agent might incorrectly select between competing skills | Medium | 0.5 session |

**Expected Output:** Conflict matrix, redundancy report, boundary clarification recommendations, agent disambiguation rules.

---

### Phase 6 — Skill Refactoring

**Purpose:** Based on conflict analysis and dependency mapping, propose structural improvements — merges, splits, renames, re-scoping, and new abstractions.

| Task | Description | Priority | Est. Effort |
|------|-------------|----------|-------------|
| 6.1 Propose merges | Identify skills that should be combined | High | 0.5 session |
| 6.2 Propose splits | Identify skills that are too broad and should be decomposed further | High | 0.5 session |
| 6.3 Propose re-scoping | Identify skills whose boundaries need adjustment | High | 0.5 session |
| 6.4 Propose new abstractions | Identify missing higher-order skills that would simplify the architecture | Medium | 0.5 session |
| 6.5 Impact analysis | For each refactoring proposal, assess impact on dependencies and consumers | Critical | 1 session |
| 6.6 Produce refactored architecture | Apply approved changes and produce the v2 skill architecture | Critical | 1 session |

**Expected Output:** Refactoring proposals (with justification and impact), approved refactored architecture v2.

---

### Phase 7 — Skill Evolution Planning

**Purpose:** Look forward to identify emerging skills, automation candidates, and governance processes for maintaining the system over time.

| Task | Description | Priority | Est. Effort |
|------|-------------|----------|-------------|
| 7.1 Emerging technology scan | Identify skills that will be needed in 1–3 years (AI-driven grid, battery storage, hydrogen, etc.) | High | 1 session |
| 7.2 Automation opportunity mapping | For each existing skill, assess automation potential (full, partial, human-only) | High | 1 session |
| 7.3 AI agent capability roadmap | Define which skills should be delegable to AI agents and in what order | High | 1 session |
| 7.4 Governance process design | Define how new skills are proposed, reviewed, approved, and retired | Critical | 0.5 session |
| 7.5 Versioning and lifecycle rules | Define skill maturity stages (draft → active → deprecated → retired) | High | 0.5 session |
| 7.6 Maintenance schedule | Define review cadence and triggers for skill updates | Medium | 0.5 session |

**Expected Output:** Future skill candidates, automation heat map, AI agent delegation roadmap, governance process document, lifecycle rules.

---

## 3. Execution Order

```
Phase 1 ──→ Phase 2 ──→ Phase 3 ──→ Phase 4 ──┐
                                                 ├──→ Phase 6 ──→ Phase 7
                                         Phase 5 ┘
```

Phases 4 and 5 feed independently into Phase 6. All other phases are strictly sequential.

**Critical path:** Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 6 → Phase 7

---

## 4. Total Effort Estimate

| Phase | Est. Sessions | Cumulative |
|-------|--------------|------------|
| Phase 1 — Discovery | 5–7 | 5–7 |
| Phase 2 — Architecture | 4–5 | 9–12 |
| Phase 3 — Definitions | 7–10 | 16–22 |
| Phase 4 — Dependencies | 4–5 | 20–27 |
| Phase 5 — Conflicts | 3–5 | 23–32 |
| Phase 6 — Refactoring | 3–4 | 26–36 |
| Phase 7 — Evolution | 4–5 | 30–41 |

A "session" = one focused execution block within a conversation turn.

---

## 5. Expected Final Deliverables

| # | Deliverable | Format |
|---|-------------|--------|
| 1 | Raw Skill Inventory | Markdown table |
| 2 | Skill Architecture (hierarchical tree) | Markdown + Mermaid diagram |
| 3 | Naming Convention & Metadata Schema | Markdown spec |
| 4 | Complete Skill Definition Registry | Markdown (or XLSX if preferred) |
| 5 | Dependency Matrix & Graph | Markdown table + Mermaid/D2 visualization |
| 6 | Composition Patterns Catalog | Markdown |
| 7 | Conflict & Redundancy Report | Markdown |
| 8 | Refactoring Proposals & v2 Architecture | Markdown |
| 9 | Future Skill Candidates & Automation Heat Map | Markdown |
| 10 | Governance Process & Lifecycle Rules | Markdown |

---

## 6. Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Scope creep from over-decomposition | Bloated skill registry that nobody maintains | Cap atomic skills at meaningful action boundaries; merge below threshold |
| Domain knowledge gaps | Missing skills in specialized areas (e.g., hydrogen integration, advanced DERMS) | Cross-reference against standards and industry publications |
| Circular dependencies | Breaks agent planning and training paths | Validate acyclicity in Phase 4; resolve immediately |
| Architecture bias toward current tooling | Future-blind skill definitions | Separate "what" (skill) from "how" (tool) in definitions |

---

## 7. Awaiting Confirmation

**This plan is ready for review.** No phases will be executed until you confirm.

Please review and let me know:

1. **Approve as-is** — I will begin Phase 1 immediately
2. **Modify scope** — Adjust granularity, add/remove phases, change priorities
3. **Add constraints** — Specific standards, existing skill inventories, or tools to incorporate
4. **Change deliverable format** — Switch any output to XLSX, DOCX, or other format
