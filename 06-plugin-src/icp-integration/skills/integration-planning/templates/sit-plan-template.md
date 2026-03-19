# System Integration Test (SIT) Plan

**Project:** {project_name}
**Document No:** {doc_number} | **Revision:** {revision}
**Prepared By:** {author} | **Date:** {date}
**Approved By:** {approver}

## 1. Scope

### 1.1 Objective
Verify that all integrated systems operate correctly as a unified solution, confirming data flow, functional interoperability, and performance under expected operating conditions.

### 1.2 Systems in Scope
| System | Version/Model | Role |
|---|---|---|
| {system_1} | {version} | {Primary control / Data source / HMI} |
| {system_2} | {version} | {description} |
| {system_3} | {version} | {description} |

### 1.3 Out of Scope
- {Items explicitly excluded from this SIT cycle}

## 2. Test Environment

| Item | Detail |
|---|---|
| Location | {Lab / Staging site / Production site} |
| Network Configuration | {VLAN layout, IP ranges, firewall rules} |
| Simulators Required | {I/O simulator, process simulator, load generator} |
| Test Tools | {Protocol analyzer, packet capture, historian replay} |

## 3. Prerequisites

- [ ] All individual system FATs completed and accepted
- [ ] Network infrastructure installed and verified
- [ ] Interface Control Documents (ICDs) approved at current revision
- [ ] Test data sets prepared and loaded
- [ ] All personnel briefed on safety procedures
- [ ] Rollback plan documented and approved

## 4. Test Cases

| TC-ID | Description | Steps | Expected Result | Actual Result | Pass/Fail | Tester | Date |
|---|---|---|---|---|---|---|---|
| SIT-001 | {End-to-end data flow from sensor to HMI} | 1. {step} 2. {step} 3. {step} | {expected_outcome} | | | | |
| SIT-002 | {Alarm propagation across systems} | 1. {step} 2. {step} | {expected_outcome} | | | | |
| SIT-003 | {Failover / redundancy switchover} | 1. {step} 2. {step} | {expected_outcome} | | | | |
| SIT-004 | {Performance under peak load} | 1. {step} 2. {step} | {expected_outcome} | | | | |
| SIT-005 | {Security — unauthorized access attempt} | 1. {step} 2. {step} | {expected_outcome} | | | | |

## 5. Schedule

| Phase | Start Date | End Date | Duration | Responsible |
|---|---|---|---|---|
| Environment Setup | {date} | {date} | {days} | {person} |
| Functional Tests | {date} | {date} | {days} | {person} |
| Performance Tests | {date} | {date} | {days} | {person} |
| Regression / Re-test | {date} | {date} | {days} | {person} |
| Report & Sign-off | {date} | {date} | {days} | {person} |

## 6. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Test environment does not replicate site conditions | Medium | High | Validate environment against site survey data |
| Vendor firmware mismatch | Low | High | Confirm versions against ICD before SIT start |
| {risk} | {L/M/H} | {L/M/H} | {mitigation} |

## 7. Entry / Exit Criteria

**Entry:** All prerequisites checked, environment validated, test team available.
**Exit:** All critical and major test cases pass; no open Severity 1/2 defects; sign-off obtained.

## 8. Approvals

| Role | Name | Signature | Date |
|---|---|---|---|
| Test Lead | {name} | | |
| Project Manager | {name} | | |
| Client Representative | {name} | | |
