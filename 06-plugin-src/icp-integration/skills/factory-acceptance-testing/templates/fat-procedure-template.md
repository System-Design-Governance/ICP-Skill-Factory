# Factory Acceptance Test (FAT) Procedure

**Project:** {project_name}
**System Under Test:** {system_name}
**Document No:** {doc_number} | **Revision:** {revision}
**Prepared By:** {author} | **Date:** {date}

## 1. System Under Test

| Item | Detail |
|---|---|
| System / Equipment | {system_name} |
| Manufacturer | {manufacturer} |
| Model / Part Number | {model} |
| Serial Number(s) | {serial_numbers} |
| Firmware / Software Version | {version} |
| Contract Reference | {contract_number} |

## 2. Test Environment

| Item | Detail |
|---|---|
| Location | {vendor_factory_address} |
| Test Bench Configuration | {bench setup description} |
| Simulated I/O | {I/O simulator details} |
| Network Setup | {switches, IP configuration} |
| Power Supply | {voltage, UPS, grounding} |
| Reference Documents | {ICD, FDS, datasheet revisions} |

## 3. Prerequisites

- [ ] Design documentation approved and at current revision
- [ ] Test environment set up and verified
- [ ] Test instruments calibrated (certificates available)
- [ ] Software/firmware loaded to specified version
- [ ] Witness notification sent (minimum {n} business days)
- [ ] Safety briefing completed for all attendees

## 4. Test Cases

### 4.1 Functional Tests

| TC-ID | Description | Steps | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|
| FAT-F-001 | {Power-on and self-diagnostics} | 1. {step} 2. {step} | {expected} | | |
| FAT-F-002 | {Input signal processing} | 1. {step} 2. {step} | {expected} | | |
| FAT-F-003 | {Output actuation verification} | 1. {step} 2. {step} | {expected} | | |

### 4.2 Integration Tests

| TC-ID | Description | Steps | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|
| FAT-I-001 | {Communication with upstream system} | 1. {step} 2. {step} | {expected} | | |
| FAT-I-002 | {Data exchange accuracy} | 1. {step} 2. {step} | {expected} | | |

### 4.3 Performance Tests

| TC-ID | Description | Steps | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|
| FAT-P-001 | {Response time under rated load} | 1. {step} 2. {step} | {expected} | | |
| FAT-P-002 | {Throughput / scan cycle time} | 1. {step} 2. {step} | {expected} | | |

### 4.4 Security Tests

| TC-ID | Description | Steps | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|
| FAT-S-001 | {Authentication and access control} | 1. {step} 2. {step} | {expected} | | |
| FAT-S-002 | {Unused ports disabled} | 1. {step} 2. {step} | {expected} | | |

## 5. Acceptance Criteria

- All functional test cases: 100% Pass
- Integration test cases: 100% Pass
- Performance test cases: within specified tolerances
- Security test cases: 100% Pass
- No open Critical or Major defects at FAT close-out

## 6. Witness Sign-off

| Role | Name | Organization | Signature | Date |
|---|---|---|---|---|
| Vendor Test Lead | {name} | {company} | | |
| Client Witness | {name} | {company} | | |
| Project Engineer | {name} | {company} | | |

## 7. Punch List

| Punch ID | Description | Severity | Responsible | Target Date | Status |
|---|---|---|---|---|---|
| PL-001 | {description} | {Critical/Major/Minor} | {person} | {date} | {Open/Closed} |
| PL-002 | | | | | |

## 8. Attachments

- [ ] Test instrument calibration certificates
- [ ] Configuration backup files
- [ ] Screen captures / photos of test results
- [ ] Network capture logs (if applicable)
