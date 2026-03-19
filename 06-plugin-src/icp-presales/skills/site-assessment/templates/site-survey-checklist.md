# OT Site Survey Checklist

| Field | Value |
|-------|-------|
| Site / Facility | {facility_name} |
| Client | {client_name} |
| Survey Date | {date} |
| Surveyor(s) | {names} |
| Project Reference | {project_id} |

## 1. Network Topology Observation

| # | Item | Observations | Photos/Diagrams |
|---|------|--------------|-----------------|
| 1.1 | Network architecture overview (flat vs. segmented) | {description} | {ref} |
| 1.2 | Number and type of network switches (managed/unmanaged) | {description} | {ref} |
| 1.3 | Firewall presence between IT and OT | {yes/no, model, config status} | {ref} |
| 1.4 | DMZ architecture (present / absent) | {description} | {ref} |
| 1.5 | Wireless access points in OT environment | {description} | {ref} |
| 1.6 | Network redundancy (ring, RSTP, dual-homed) | {description} | {ref} |
| 1.7 | Available network diagrams (current accuracy) | {description} | {ref} |

## 2. Asset Enumeration

| # | Item | Observations | Count |
|---|------|--------------|-------|
| 2.1 | PLCs / RTUs (vendor, model, firmware) | {description} | {n} |
| 2.2 | HMIs / Operator Workstations (OS, version) | {description} | {n} |
| 2.3 | Engineering Workstations | {description} | {n} |
| 2.4 | SCADA / DCS Servers | {description} | {n} |
| 2.5 | Historians | {description} | {n} |
| 2.6 | Network devices (switches, routers, firewalls) | {description} | {n} |
| 2.7 | IoT / IIoT devices (sensors, gateways) | {description} | {n} |
| 2.8 | Safety systems (SIS, ESD, F&G) | {description} | {n} |

## 3. Physical Security

| # | Item | Observations | Adequate |
|---|------|--------------|----------|
| 3.1 | Perimeter fencing and access control | {description} | Y / N |
| 3.2 | Control room access (badge, key, biometric) | {description} | Y / N |
| 3.3 | Cabinet/panel locks | {description} | Y / N |
| 3.4 | CCTV coverage of critical areas | {description} | Y / N |
| 3.5 | Visitor management process | {description} | Y / N |
| 3.6 | USB port accessibility | {description} | Y / N |

## 4. Environmental Conditions

| # | Item | Observations | Concern |
|---|------|--------------|---------|
| 4.1 | Temperature and humidity control (server/control rooms) | {description} | Y / N |
| 4.2 | Dust / corrosive atmosphere | {description} | Y / N |
| 4.3 | EMI / RFI sources near OT equipment | {description} | Y / N |
| 4.4 | Power quality (UPS, surge protection, grounding) | {description} | Y / N |
| 4.5 | Cable routing and labeling quality | {description} | Y / N |

## 5. Existing Security Controls

| # | Item | Present | Details |
|---|------|---------|---------|
| 5.1 | Antivirus / endpoint protection on OT hosts | Y / N | {product, version, update status} |
| 5.2 | Patch management process for OT systems | Y / N | {frequency, method} |
| 5.3 | Backup procedures for PLC programs and configs | Y / N | {frequency, storage location} |
| 5.4 | Password policy enforcement | Y / N | {details} |
| 5.5 | Log collection and monitoring | Y / N | {SIEM, syslog, local only} |
| 5.6 | Intrusion detection (NIDS) in OT network | Y / N | {product, coverage} |
| 5.7 | Asset inventory maintained | Y / N | {tool, accuracy, last update} |

## 6. Communication Paths

| # | Item | Observations |
|---|------|--------------|
| 6.1 | OT protocols in use (Modbus, EtherNet/IP, OPC, DNP3, etc.) | {list} |
| 6.2 | IT-OT data flows (historian to enterprise, MES integration) | {description} |
| 6.3 | External data flows (vendor telemetry, cloud services) | {description} |
| 6.4 | Inter-site communication (WAN, VPN tunnels) | {description} |

## 7. Remote Access

| # | Item | Observations | Risk Level |
|---|------|--------------|------------|
| 7.1 | Remote access method (VPN, RDP, TeamViewer, vendor portal) | {description} | {H/M/L} |
| 7.2 | Multi-factor authentication for remote access | Y / N | {H/M/L} |
| 7.3 | Vendor remote access (always-on vs. on-demand) | {description} | {H/M/L} |
| 7.4 | Remote access logging and monitoring | Y / N | {H/M/L} |
| 7.5 | Jump host / bastion host architecture | Y / N | {H/M/L} |

## Survey Summary

- **Key Findings**: {top 3-5 observations}
- **Immediate Risks Identified**: {any critical issues requiring urgent attention}
- **Recommended Next Steps**: {assessment, design, remediation priorities}
- **Estimated Asset Count**: {total OT devices observed}
- **Network Complexity**: {Low / Medium / High}

**Surveyor Sign-off**: {name} | Date: {date}
