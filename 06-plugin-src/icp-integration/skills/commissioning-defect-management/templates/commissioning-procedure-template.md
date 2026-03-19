# Commissioning Procedure

**Project:** {project_name}
**System:** {system_name}
**Document No:** {doc_number} | **Revision:** {revision}
**Prepared By:** {author} | **Date:** {date}
**Approved By:** {approver}

## 1. System Description

| Item | Detail |
|---|---|
| System Name | {system_name} |
| Location / Area | {plant_area} |
| Purpose | {brief functional description} |
| Design Reference | {FDS/SDD document number} |
| Related Systems | {upstream and downstream systems} |

## 2. Pre-checks

### 2.1 Mechanical / Electrical

- [ ] Equipment installed per approved drawings
- [ ] Power supply verified (voltage, phase, grounding)
- [ ] Cable terminations checked (torque, insulation resistance)
- [ ] Grounding resistance measured: {value} ohms (requirement: < {spec} ohms)
- [ ] UPS battery test passed

### 2.2 Instrumentation

- [ ] All instruments calibrated with certificates on file
- [ ] Loop checks completed (reference: loop check sheets)
- [ ] Valve stroke tests completed

### 2.3 Control System

- [ ] Software/firmware at approved version: {version}
- [ ] Configuration backup taken and stored at: {backup_location}
- [ ] Network connectivity verified (ping test, VLAN assignment)
- [ ] Time synchronization confirmed (NTP/PTP source locked)

### 2.4 Safety

- [ ] LOTO procedures in place
- [ ] Safety system (SIS/ESD) in bypass with proper authorization
- [ ] Fire suppression / gas detection operational
- [ ] Emergency contacts posted at site

## 3. Step-by-step Startup Sequence

| Step | Action | Expected Result | Verified By | Date/Time |
|---|---|---|---|---|
| 1 | Energize control system power supply | System boots, no hardware faults | | |
| 2 | Verify controller diagnostics — all modules healthy | Green status on all I/O cards | | |
| 3 | Establish communication links | All remote devices online | | |
| 4 | Enable analog inputs — verify live readings | Readings match field instruments within tolerance | | |
| 5 | Enable digital inputs — verify field contact states | All states correct vs. field | | |
| 6 | Test outputs in manual mode (one at a time) | Each output responds correctly | | |
| 7 | Remove SIS bypass, confirm safety functions active | Safety interlocks armed, trip test passed | | |
| 8 | Switch to automatic mode | System controlling to setpoint | | |
| 9 | Run for observation period ({n} hours) | Stable operation, no alarms | | |
| 10 | Declare system commissioned | All criteria met | | |

## 4. Performance Verification

| Parameter | Design Spec | Measured Value | Pass/Fail |
|---|---|---|---|
| {Response time} | {< n seconds} | {value} | |
| {Accuracy} | {+/- n%} | {value} | |
| {CPU utilization} | {< n%} | {value} | |
| {Communication uptime} | {> 99.9%} | {value} | |

## 5. Safety Validation

- [ ] Emergency shutdown (ESD) trip test performed — system tripped within {n} ms
- [ ] Safety Instrumented Function (SIF) proof test passed
- [ ] Fire and gas detection functional test passed
- [ ] All safety-related alarms verified at HMI and field annunciator

## 6. Sign-off

| Role | Name | Signature | Date |
|---|---|---|---|
| Commissioning Lead | {name} | | |
| Operations Representative | {name} | | |
| Safety Officer | {name} | | |
| Project Manager | {name} | | |

## 7. Attachments

- [ ] Completed pre-check records
- [ ] Calibration certificates
- [ ] Configuration backup confirmation
- [ ] Performance test data sheets
- [ ] Defect log (reference: DEF-xxx)
