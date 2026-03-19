# Architecture Decision Record

**ADR ID:** {ADR-YYYY-NNN}
**Title:** {Short descriptive title, e.g., "Use MQTT broker at edge for telemetry aggregation"}
**Status:** {Proposed / Accepted / Deprecated / Superseded by ADR-YYYY-NNN}
**Date:** {YYYY-MM-DD}
**Author:** {Author}
**Reviewers:** {Reviewer 1, Reviewer 2}

## Context

{Describe the situation and forces at play. What is the problem or opportunity?
Include relevant constraints such as:
- Operational requirements (latency, bandwidth, availability)
- Environmental factors (remote site, limited connectivity, harsh conditions)
- Security requirements (IEC 62443 security level, zone/conduit model)
- Existing infrastructure and integration points
- Team capabilities and vendor support

Example: "The remote substation generates 50,000 data points at 1-second intervals.
Current architecture sends all data to the central SCADA historian over a 4G link
with 200 ms latency and 10 Mbps bandwidth. During peak load the link saturates,
causing data loss of up to 8%."}

## Decision

{State the decision clearly and concisely.

Example: "We will deploy an edge computing gateway (model X) at the substation to
perform local data aggregation, compression, and store-and-forward. Only exception
reports and 1-minute averages will be transmitted to the central historian. Raw
1-second data will be retained locally for 30 days."}

## Alternatives Considered

| # | Alternative | Pros | Cons | Why Rejected |
|---|---|---|---|---|
| 1 | {e.g., Upgrade WAN link to 100 Mbps} | {Simple, no edge logic} | {High recurring cost, single point of failure} | {Cost exceeds budget by 3x} |
| 2 | {e.g., Reduce scan rate to 10 s} | {No new hardware} | {Loses transient event data} | {Unacceptable for protection analysis} |
| 3 | {e.g., Cloud-based edge processing} | {Scalable, managed service} | {Latency, internet dependency} | {Site has no reliable internet} |

## Consequences

### Positive
- {Reduced WAN bandwidth usage by ~85%}
- {Local buffering eliminates data loss during link outages}
- {Enables future local analytics without central dependency}

### Negative
- {Additional hardware to maintain at remote site}
- {Edge gateway becomes a new asset requiring patching and monitoring}
- {Adds complexity to the data flow architecture}

### Risks and Mitigations
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| {Edge gateway hardware failure} | {Low} | {High} | {Redundant gateway in hot-standby} |
| {Firmware vulnerability} | {Medium} | {High} | {Quarterly patch cycle per IEC 62443} |

## Compliance Notes

- IEC 62443 SL: {SL-T for the edge zone}
- Relevant standards: {IEC 61850, IEEE 1547, OPC UA, etc.}

## Review Date

**Next review:** {YYYY-MM-DD, typically 6-12 months from decision date}

{If the technology landscape, requirements, or constraints change materially
before the review date, trigger an early review.}
