# RTO / RPO Target Matrix

**Project:** {Project Name}
**Site:** {Site / Facility Name}
**Author:** {Author}
**Date:** {YYYY-MM-DD}
**Revision:** {Rev}

## 1. Purpose

Define Recovery Time Objective (RTO) and Recovery Point Objective (RPO) targets
for each system to guide backup strategy, disaster recovery planning, and
business continuity procedures.

## 2. Definitions

- **RTO** -- Maximum acceptable downtime before the system must be restored.
- **RPO** -- Maximum acceptable data loss measured in time (how far back recovery goes).
- **Criticality** -- H = High (safety/production-critical), M = Medium (operational impact), L = Low (administrative).

## 3. RTO / RPO Matrix

| # | System / Application | Criticality | RTO | RPO | Backup Strategy | Recovery Procedure Ref | Last Test Date | Test Result |
|---|---|---|---|---|---|---|---|---|
| 1 | {e.g., SCADA Server} | H | {15 min} | {0 min (real-time replication)} | {Hot standby + DB replication} | {DR-PROC-001} | {YYYY-MM-DD} | {Pass/Fail} |
| 2 | {e.g., Historian} | H | {1 hr} | {5 min} | {Incremental backup every 5 min} | {DR-PROC-002} | {YYYY-MM-DD} | {Pass/Fail} |
| 3 | {e.g., HMI Workstation} | M | {4 hr} | {24 hr} | {Daily image backup} | {DR-PROC-003} | {YYYY-MM-DD} | {Pass/Fail} |
| 4 | {e.g., Engineering Workstation} | M | {8 hr} | {24 hr} | {Daily file backup} | {DR-PROC-004} | {YYYY-MM-DD} | {Pass/Fail} |
| 5 | {e.g., Network Switches Config} | H | {30 min} | {on change} | {Config export on change} | {DR-PROC-005} | {YYYY-MM-DD} | {Pass/Fail} |
| 6 | {e.g., PLC Programs} | H | {2 hr} | {on change} | {Version-controlled project files} | {DR-PROC-006} | {YYYY-MM-DD} | {Pass/Fail} |

## 4. Backup Verification Schedule

| Frequency | Activity | Responsible |
|---|---|---|
| Weekly | Verify backup job completion logs | {role} |
| Monthly | Test restore of one randomly selected system | {role} |
| Quarterly | Full DR drill covering all Criticality-H systems | {role} |
| Annually | Complete DR exercise with documented lessons learned | {role} |

## 5. Escalation Path

If RTO is exceeded during an actual incident:

1. **T + 0**: Initiate recovery procedure per reference document.
2. **T + RTO/2**: Notify {operations manager} of recovery status.
3. **T + RTO**: Escalate to {site manager / VP Operations}.
4. **T + 2x RTO**: Activate business continuity plan.

## 6. Notes

- {Regulatory requirements affecting retention periods}
- {Constraints on backup media, offsite storage, or cloud replication}
- Reference: IEC 62443-2-1 (IACS security management system)
