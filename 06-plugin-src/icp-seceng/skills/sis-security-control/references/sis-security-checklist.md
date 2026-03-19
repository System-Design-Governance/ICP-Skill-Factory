# SIS/SIF Security Controls Checklist (IEC 61511 + IEC 62443)

| Field | Value |
|-------|-------|
| Facility | {facility_name} |
| SIS System | {sis_system_name} |
| Logic Solver | {vendor} / {model} |
| SIL Rating | SIL {1 / 2 / 3} |
| Assessed By | {assessor} |
| Date | {date} |

## 1. Physical Separation and Isolation

| # | Control | Standard Ref | Status | Compliant | Action |
|---|---------|-------------|--------|-----------|--------|
| 1.1 | SIS is physically separate from BPCS | IEC 61511-1 Cl. 11.2.4 | {status} | Y / N / NA | {action} |
| 1.2 | SIS uses dedicated I/O (not shared with BPCS) | IEC 61511-1 Cl. 11.2.4 | {status} | Y / N / NA | {action} |
| 1.3 | SIS power supply is independent from BPCS | IEC 61511-1 Cl. 11.6 | {status} | Y / N / NA | {action} |
| 1.4 | SIS cabinets are in locked, access-controlled enclosures | IEC 62443-3-3 SR 2.1 | {status} | Y / N / NA | {action} |
| 1.5 | Physical access to SIS requires documented authorization | IEC 62443-2-1 | {status} | Y / N / NA | {action} |
| 1.6 | SIS engineering workstation is air-gapped or strictly isolated | Best practice | {status} | Y / N / NA | {action} |

## 2. Logic Solver Hardening

| # | Control | Standard Ref | Status | Compliant | Action |
|---|---------|-------------|--------|-----------|--------|
| 2.1 | Default credentials changed on logic solver | IEC 62443-4-2 CR 1.1 | {status} | Y / N / NA | {action} |
| 2.2 | Logic solver is in RUN mode with key switch locked | Vendor best practice | {status} | Y / N / NA | {action} |
| 2.3 | Programming access requires physical key or hardware enable | IEC 62443-3-3 SR 1.1 | {status} | Y / N / NA | {action} |
| 2.4 | Unused communication ports disabled | IEC 62443-4-2 CR 7.7 | {status} | Y / N / NA | {action} |
| 2.5 | Firmware is at vendor-recommended version | IEC 62443-2-3 | {status} | Y / N / NA | {action} |
| 2.6 | USB ports disabled or physically blocked | Best practice | {status} | Y / N / NA | {action} |
| 2.7 | SIS logic solver audit trail / event log enabled | IEC 62443-3-3 SR 6.1 | {status} | Y / N / NA | {action} |

## 3. Communication Isolation

| # | Control | Standard Ref | Status | Compliant | Action |
|---|---------|-------------|--------|-----------|--------|
| 3.1 | SIS network is on a separate VLAN/physical network from BPCS | IEC 62443-3-3 SR 5.1 | {status} | Y / N / NA | {action} |
| 3.2 | SIS-to-BPCS communication is one-directional (SIS -> BPCS) | IEC 61511-1 Cl. 11.2.4 | {status} | Y / N / NA | {action} |
| 3.3 | Data diode or hardware-enforced unidirectional gateway in use | Best practice for SIL 3 | {status} | Y / N / NA | {action} |
| 3.4 | No direct connection from SIS to enterprise/IT network | IEC 62443-3-3 SR 5.2 | {status} | Y / N / NA | {action} |
| 3.5 | Firewall rules between SIS and BPCS follow least-privilege | IEC 62443-3-3 SR 5.2 | {status} | Y / N / NA | {action} |
| 3.6 | Remote access to SIS is prohibited or requires dual authorization | IEC 62443-3-3 SR 1.13 | {status} | Y / N / NA | {action} |

## 4. Change Management

| # | Control | Standard Ref | Status | Compliant | Action |
|---|---------|-------------|--------|-----------|--------|
| 4.1 | SIS logic changes follow formal Management of Change (MOC) | IEC 61511-1 Cl. 5.2.6 | {status} | Y / N / NA | {action} |
| 4.2 | SIS program changes require independent verification | IEC 61511-1 Cl. 12 | {status} | Y / N / NA | {action} |
| 4.3 | SIS logic baseline is stored securely with integrity verification | IEC 62443-3-3 SR 3.4 | {status} | Y / N / NA | {action} |
| 4.4 | All SIS changes are logged with who/what/when/why | IEC 62443-3-3 SR 6.1 | {status} | Y / N / NA | {action} |
| 4.5 | SIS change approval requires functional safety + cybersecurity review | Best practice | {status} | Y / N / NA | {action} |
| 4.6 | Rollback procedure exists and is tested for SIS logic changes | Best practice | {status} | Y / N / NA | {action} |

## 5. Periodic Testing and Validation

| # | Control | Standard Ref | Status | Compliant | Action |
|---|---------|-------------|--------|-----------|--------|
| 5.1 | Proof test intervals are defined per SIF SIL requirements | IEC 61511-1 Cl. 16 | {status} | Y / N / NA | {action} |
| 5.2 | Proof test results are documented and trends analyzed | IEC 61511-1 Cl. 16 | {status} | Y / N / NA | {action} |
| 5.3 | SIS cybersecurity assessment is performed periodically | IEC 62443-2-1 | {status} | Y / N / NA | {action} |
| 5.4 | SIS logic is compared against baseline after any maintenance | IEC 62443-3-3 SR 3.4 | {status} | Y / N / NA | {action} |
| 5.5 | SIS backup and recovery is tested annually | IEC 62443-3-3 SR 7.3 | {status} | Y / N / NA | {action} |
| 5.6 | SIS-specific incident response procedures are tested | IEC 62443-2-1 | {status} | Y / N / NA | {action} |

## Summary

| Section | Total Items | Compliant | Non-Compliant | N/A |
|---------|------------|-----------|---------------|-----|
| Physical Separation | {count} | {count} | {count} | {count} |
| Logic Solver Hardening | {count} | {count} | {count} | {count} |
| Communication Isolation | {count} | {count} | {count} | {count} |
| Change Management | {count} | {count} | {count} | {count} |
| Periodic Testing | {count} | {count} | {count} | {count} |
| **Total** | **{count}** | **{count}** | **{count}** | **{count}** |

**Overall Compliance**: {percentage}%
**Critical Gaps**: {list any non-compliant items with safety implications}
**Sign-off**: {assessor} | {date}
