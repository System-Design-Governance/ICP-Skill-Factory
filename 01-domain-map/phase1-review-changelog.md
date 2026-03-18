# Phase 1 Domain Map — Review Change Log

**Source:** Extracted from `skill-factory-deliverable.md` Section 3 (Stage B Review)
**Version:** R2 (2026-03-13)

---

## Review Methodology

The Phase 1 domain map (v1.0, 13 domains, 66 subdomains) was evaluated against 10 quality criteria. Each criterion is scored Pass / Partial / Fail, with specific findings and recommended corrections.

## Quality Criteria Assessment Summary

| # | Criterion | Score |
|---|-----------|-------|
| 1 | Completeness — Does every engineering capability have a home? | PARTIAL |
| 2 | MECE Quality — Are domains mutually exclusive? | PARTIAL |
| 3 | Scalability — Can the structure absorb 150+ skills? | PASS |
| 4 | Practical Fit — Match ICP engineer workflows? | PASS |
| 5 | Governance vs. Execution Separation | PASS |
| 6 | Missing Domains | PARTIAL |
| 7 | Overlapping Subdomains | PARTIAL |
| 8 | Naming Consistency | PARTIAL |
| 9 | AI Agent Navigability | PASS |
| 10 | Standards Alignment | PASS |

### Gaps Identified

- **G1**: No explicit home for SIS Security → Added D01.7
- **G2**: No explicit home for Personnel Security & Competency Management → Added D11.6
- **G3**: Decommissioning/Disposal skills had no clear subdomain → Added D08.6

### Overlaps Identified

- **O1**: D02.3 / D05.5 / D07.2 — protocol-related subdomains → Boundary rules added (CHG-004)
- **O2**: D10.4 / D11.2 — change management → Resolution rule added (CHG-005)
- **O3**: D01.3 / D11.5 — standards compliance → Accepted (different subjects)

### Naming Issues

- **N1**: Inconsistent English domain ID styles → Deferred to Phase 2
- **N2**: Mixed granularity in skill examples → To be normalized in Phase 2

---

## Change Log

| Change ID | Type | Target | Description | Impact |
|-----------|------|--------|-------------|--------|
| CHG-001 | Add | D01.7 | Add "SIS 安全 (Safety Instrumented System Security)" subdomain | +1 subdomain |
| CHG-002 | Add | D11.6 | Add "安全能力管理 (Security Competency Management)" subdomain | +1 subdomain |
| CHG-003 | Add | D08.6 | Add "系統除役 (System Decommissioning)" subdomain | +1 subdomain |
| CHG-004 | Clarify | D02.3, D05.5, D07.2 | Add boundary rules for communication/protocol subdomains | No structural change |
| CHG-005 | Clarify | D10.4, D11.2 | Add resolution rule for change management overlap | No structural change |
| CHG-006 | Note | N/A | Flag naming inconsistency in English domain IDs for future normalization | Deferred |
| CHG-007 | Add | D14 | Add new Level 1 domain: PRE-GATE-ENGINEERING 前置技術工程 with 6 subdomains | +1 domain, +6 subdomains |
| CHG-008 | Modify | D10 | Re-scope D10 to post-acceptance project technical management; migrate pre-gate subdomains to D14 | D10: 6→4 subdomains |
| CHG-009 | Add | ADR-005 | Architecture Decision Record for D14 independence from D10 | Documents lifecycle boundary decision |
| CHG-010 | Add | Dependency Notes | D14 connects to D01, D02, D09, D10, D11 as feeder domain | Formalizes cross-domain data flow |

**Net effect: 13 domains → 14 domains (+1 D14), 66 subdomains → ~~75~~ **73** subdomains (+4 net)**

> **R3 勘誤：** 原計 +9 net / 75 subdomains 有誤。正確計算：R1(69) + D14(+6) + D10(−2) = 73。淨變動 = +4。

See `phase1-revision-r2.md` for the full R2 revision document including ADR-005, dependency diagrams, and skill candidate migration table.
