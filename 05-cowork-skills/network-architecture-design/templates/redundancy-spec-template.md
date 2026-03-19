# Network Redundancy Specification

**Project:** {Project Name}
**Site:** {Site / Facility Name}
**Author:** {Author}
**Date:** {YYYY-MM-DD}
**Revision:** {Rev}

## 1. Scope

This document specifies the network redundancy design for {system/area}, ensuring
continuous communication in the event of a single point of failure.

## 2. Redundancy Design Summary

| # | System / Segment | Redundancy Type | Primary Path | Secondary Path | Failover Time Target | Verified Failover Time | Test Date |
|---|---|---|---|---|---|---|---|
| 1 | {e.g., Control Network Ring A} | {RSTP / MRP / HSR / PRP / Dual-homing} | {Switch-A -> Switch-B via fibre} | {Switch-A -> Switch-C via fibre} | {< 50 ms} | {measured value} | {YYYY-MM-DD} |
| 2 | {e.g., SCADA Backbone} | {RSTP / Ring / Dual-homing} | {Primary uplink} | {Secondary uplink} | {< 200 ms} | {measured value} | {YYYY-MM-DD} |
| 3 | {e.g., Safety Network} | {PRP / HSR} | {LAN A path} | {LAN B path} | {0 ms (hitless)} | {measured value} | {YYYY-MM-DD} |

## 3. Failover Test Procedure

For each entry above, conduct the following:

1. Establish baseline traffic (ping + sustained data flow).
2. Disconnect the primary path (physically or via managed switch port disable).
3. Record time to restore communication on secondary path.
4. Verify no data loss beyond acceptable threshold.
5. Reconnect primary path; confirm reconvergence.

## 4. Acceptance Criteria

- Failover time must meet or exceed the target listed above.
- No undetected packet loss during failover for safety-critical systems.
- Reconvergence after primary path restoration must complete within {X} seconds.

## 5. Notes

- {Any site-specific constraints, cable routing considerations, or vendor requirements}
- Reference standards: IEC 62439 (PRP/HSR), IEEE 802.1D (RSTP), IEC 62443 (security)

## 6. Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Network Engineer | {name} | | {date} |
| OT Security Lead | {name} | | {date} |
| Project Manager | {name} | | {date} |
