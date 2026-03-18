# ADR-002: Data Platform Independence

**Status:** Accepted
**Date:** 2026-03-13
**Context:** Phase 1 Domain Map Design

## Decision

Maintain Energy Data Platform (D12) as an independent Level 1 domain, separate from Control System Engineering (D05) and Integration Engineering (D07).

## Rationale

Data engineering is a growing function within ICP that encompasses data acquisition, time-series storage, analytics, visualization, and data governance. While data flows through control systems (D05) and integration points (D07), the platform engineering skills required to build and maintain the data infrastructure are distinct. The separation also accommodates the emerging data engineering team structure within ICP.

## Consequences

- D12 has its own subdomain structure (5 subdomains)
- Data pipeline skills are distinct from control system configuration skills
- Cross-domain dependencies with D05 (data sources) and D07 (integration points) managed in Phase 4
