# ADR-001: Protection Engineering Independence

**Status:** Accepted
**Date:** 2026-03-13
**Context:** Phase 1 Domain Map Design

## Decision

Maintain Protection Engineering (D04) as an independent Level 1 domain, separate from Power System Engineering (D03) and Control System Engineering (D05).

## Rationale

Protection relay engineering is a distinct specialty within ICP's organization. It requires specialized skills (fault analysis, coordination studies, relay settings) that do not overlap with general power system design or control system configuration. ICP employs dedicated protection engineers with specific certification requirements.

## Consequences

- D04 has its own subdomain structure (4 subdomains)
- Protection-related skills are concentrated in one domain for clear ownership
- Cross-domain dependencies exist with D03 (power system data) and D05 (control integration) but are managed via dependency mapping (Phase 4)
