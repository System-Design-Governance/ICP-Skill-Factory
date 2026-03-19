# Site Acceptance Test (SAT) Procedure

**Project:** {project_name}
**Site:** {site_name} | **Location:** {address}
**Document No:** {doc_number} | **Revision:** {revision}
**Prepared By:** {author} | **Date:** {date}

## 1. Site Conditions

| Item | Detail |
|---|---|
| Site Name / Unit | {site_name} |
| Ambient Temperature | {temperature_range} |
| Power Supply Confirmed | {Yes/No — voltage, phase, grounding verified} |
| Network Infrastructure Ready | {Yes/No — cables, switches, patch panels installed} |
| Safety Permits Obtained | {Hot work / LOTO / Confined space as required} |
| Site Contact | {name, phone} |

## 2. Pre-commissioning Checks

- [ ] Equipment installed per approved installation drawings
- [ ] Cable terminations verified (continuity, insulation resistance)
- [ ] Grounding and bonding measured and within specification
- [ ] Power supply voltage and phase rotation confirmed
- [ ] Environmental conditions within equipment rating (temperature, humidity)
- [ ] Network connectivity verified (ping test to all endpoints)
- [ ] FAT punch list items closed or accepted for SAT

## 3. Test Cases

### 3.1 Field I/O Verification

| TC-ID | Description | Steps | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|
| SAT-IO-001 | {Analog input calibration check} | 1. Apply known signal at field device 2. Verify reading at controller/HMI | {Within +/- 0.5% of span} | | |
| SAT-IO-002 | {Digital input verification} | 1. Actuate field contact 2. Confirm state change | {Correct state, < 100 ms} | | |
| SAT-IO-003 | {Analog output loop test} | 1. Command output from HMI 2. Measure at field device | {Within +/- 0.5% of span} | | |
| SAT-IO-004 | {Digital output verification} | 1. Command output 2. Confirm field device actuation | {Correct actuation} | | |

### 3.2 Communication Tests

| TC-ID | Description | Steps | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|
| SAT-COM-001 | {Controller-to-SCADA link} | 1. {step} 2. {step} | {All points updating, no comm errors} | | |
| SAT-COM-002 | {Redundancy failover} | 1. Disconnect primary path 2. Monitor switchover | {< {n} ms failover, no data loss} | | |

### 3.3 Alarm Tests

| TC-ID | Description | Steps | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|
| SAT-ALM-001 | {High-priority alarm activation} | 1. Force process variable above setpoint 2. Check HMI and annunciator | {Alarm displayed, audible alert, correct priority} | | |
| SAT-ALM-002 | {Alarm acknowledgment and reset} | 1. Acknowledge alarm 2. Clear condition 3. Verify reset | {Proper state transitions per ISA 18.2} | | |

### 3.4 Performance Tests

| TC-ID | Description | Steps | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|
| SAT-PERF-001 | {System response time} | 1. Initiate command 2. Measure end-to-end latency | {< {n} seconds} | | |
| SAT-PERF-002 | {Sustained load operation} | 1. Run under rated load for {n} hours 2. Monitor diagnostics | {No errors, CPU < {n}%} | | |

## 4. Acceptance Criteria

- 100% of field I/O points verified against loop drawings
- All communication paths operational including redundant paths
- All configured alarms tested per alarm rationalization database
- System performance within contract specifications
- No open Critical defects; Major defects have agreed remediation plan

## 5. Defect Log

| Defect ID | Date | Description | Severity | Assigned To | Target Date | Status |
|---|---|---|---|---|---|---|
| SAT-D-001 | {date} | {description} | {Critical/Major/Minor} | {person} | {date} | {Open/Resolved/Deferred} |
| SAT-D-002 | | | | | | |

## 6. Handover Checklist

- [ ] All SAT test cases passed or deferred with client approval
- [ ] As-built drawings updated and submitted
- [ ] Configuration backup taken and stored
- [ ] O&M documentation delivered
- [ ] Operator training completed
- [ ] Spare parts delivered and inventoried
- [ ] Warranty period start date agreed: {date}

## 7. Approvals

| Role | Name | Signature | Date |
|---|---|---|---|
| Site Test Lead | {name} | | |
| Client Representative | {name} | | |
| Project Manager | {name} | | |
