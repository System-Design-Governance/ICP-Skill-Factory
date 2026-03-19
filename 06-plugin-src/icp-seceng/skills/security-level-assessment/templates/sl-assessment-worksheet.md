# Security Level Assessment Worksheet (IEC 62443-3-3)

| Field | Value |
|-------|-------|
| Project / Facility | {project_name} |
| Zone Under Assessment | {zone_name} |
| Zone Description | {zone_description} |
| Assessment Date | {date} |
| Assessor(s) | {assessor_names} |
| SL-T Basis | Risk assessment reference: {tra_document_id} |

## Zone Context

- **Zone ID**: {zone_id}
- **Purdue Level(s)**: {0 / 1 / 2 / 3 / 3.5}
- **Assets in Zone**: {list of key assets}
- **Connected Conduits**: {conduit_ids and destinations}
- **SL-T (Target)**: SL {1 / 2 / 3 / 4} (determined from risk assessment)

## SL-T vs SL-A Gap Analysis

### FR 1 -- Identification and Authentication Control (IAC)

| SR | Security Requirement | RE | SL-T | SL-A | Gap | Remediation |
|----|---------------------|----|------|------|-----|-------------|
| 1.1 | Human user identification and authentication | - | {0-4} | {0-4} | {Y/N} | {action if gap} |
| 1.1 | Human user identification and authentication | RE1 | {0-4} | {0-4} | {Y/N} | {action} |
| 1.2 | Software process and device identification | - | {0-4} | {0-4} | {Y/N} | {action} |
| 1.3 | Account management | - | {0-4} | {0-4} | {Y/N} | {action} |
| 1.4 | Identifier management | - | {0-4} | {0-4} | {Y/N} | {action} |
| 1.5 | Authenticator management | - | {0-4} | {0-4} | {Y/N} | {action} |
| 1.6 | Wireless access management | - | {0-4} | {0-4} | {Y/N} | {action} |
| 1.7 | Strength of password-based authentication | - | {0-4} | {0-4} | {Y/N} | {action} |
| 1.8 | PKI certificates | - | {0-4} | {0-4} | {Y/N} | {action} |
| 1.9 | Strength of public key authentication | - | {0-4} | {0-4} | {Y/N} | {action} |

### FR 2 -- Use Control (UC)

| SR | Security Requirement | RE | SL-T | SL-A | Gap | Remediation |
|----|---------------------|----|------|------|-----|-------------|
| 2.1 | Authorization enforcement | - | {0-4} | {0-4} | {Y/N} | {action} |
| 2.2 | Wireless use control | - | {0-4} | {0-4} | {Y/N} | {action} |
| 2.3 | Use control for portable/mobile devices | - | {0-4} | {0-4} | {Y/N} | {action} |
| 2.4 | Mobile code | - | {0-4} | {0-4} | {Y/N} | {action} |
| 2.5 | Session lock | - | {0-4} | {0-4} | {Y/N} | {action} |
| 2.6 | Remote session termination | - | {0-4} | {0-4} | {Y/N} | {action} |

### FR 3 -- System Integrity (SI)

| SR | Security Requirement | RE | SL-T | SL-A | Gap | Remediation |
|----|---------------------|----|------|------|-----|-------------|
| 3.1 | Communication integrity | - | {0-4} | {0-4} | {Y/N} | {action} |
| 3.2 | Malicious code protection | - | {0-4} | {0-4} | {Y/N} | {action} |
| 3.3 | Security functionality verification | - | {0-4} | {0-4} | {Y/N} | {action} |
| 3.4 | Software and information integrity | - | {0-4} | {0-4} | {Y/N} | {action} |
| 3.5 | Input validation | - | {0-4} | {0-4} | {Y/N} | {action} |

### FR 4 -- Data Confidentiality (DC)

| SR | Security Requirement | RE | SL-T | SL-A | Gap | Remediation |
|----|---------------------|----|------|------|-----|-------------|
| 4.1 | Information confidentiality | - | {0-4} | {0-4} | {Y/N} | {action} |
| 4.2 | Information persistence | - | {0-4} | {0-4} | {Y/N} | {action} |

### FR 5 -- Restricted Data Flow (RDF)

| SR | Security Requirement | RE | SL-T | SL-A | Gap | Remediation |
|----|---------------------|----|------|------|-----|-------------|
| 5.1 | Network segmentation | - | {0-4} | {0-4} | {Y/N} | {action} |
| 5.2 | Zone boundary protection | - | {0-4} | {0-4} | {Y/N} | {action} |
| 5.3 | General purpose person-to-person communication | - | {0-4} | {0-4} | {Y/N} | {action} |
| 5.4 | Application partitioning | - | {0-4} | {0-4} | {Y/N} | {action} |

### FR 6 -- Timely Response to Events (TRE)

| SR | Security Requirement | RE | SL-T | SL-A | Gap | Remediation |
|----|---------------------|----|------|------|-----|-------------|
| 6.1 | Audit log accessibility | - | {0-4} | {0-4} | {Y/N} | {action} |
| 6.2 | Continuous monitoring | - | {0-4} | {0-4} | {Y/N} | {action} |

### FR 7 -- Resource Availability (RA)

| SR | Security Requirement | RE | SL-T | SL-A | Gap | Remediation |
|----|---------------------|----|------|------|-----|-------------|
| 7.1 | Denial of service protection | - | {0-4} | {0-4} | {Y/N} | {action} |
| 7.2 | Resource management | - | {0-4} | {0-4} | {Y/N} | {action} |
| 7.3 | Control system backup | - | {0-4} | {0-4} | {Y/N} | {action} |
| 7.4 | Control system recovery | - | {0-4} | {0-4} | {Y/N} | {action} |
| 7.5 | Emergency power | - | {0-4} | {0-4} | {Y/N} | {action} |
| 7.6 | Network and security configuration settings | - | {0-4} | {0-4} | {Y/N} | {action} |

## Gap Summary

| FR | Total SRs | Gaps Found | Gap % | Priority Remediations |
|----|-----------|------------|-------|-----------------------|
| FR 1 (IAC) | {count} | {count} | {%} | {top items} |
| FR 2 (UC) | {count} | {count} | {%} | {top items} |
| FR 3 (SI) | {count} | {count} | {%} | {top items} |
| FR 4 (DC) | {count} | {count} | {%} | {top items} |
| FR 5 (RDF) | {count} | {count} | {%} | {top items} |
| FR 6 (TRE) | {count} | {count} | {%} | {top items} |
| FR 7 (RA) | {count} | {count} | {%} | {top items} |

**Overall SL-A Achieved**: SL {1 / 2 / 3 / 4}
**SL-T Required**: SL {1 / 2 / 3 / 4}
**Assessment Result**: {Compliant / Gap Identified -- remediation required}
