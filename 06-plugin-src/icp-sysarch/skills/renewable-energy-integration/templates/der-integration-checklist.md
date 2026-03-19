# DER Integration Checklist

**Project:** {Project Name}
**DER Site:** {Site Name / Location}
**Author:** {Author}
**Date:** {YYYY-MM-DD}
**Revision:** {Rev}

## 1. DER Identification

| Item | Value |
|---|---|
| DER Type | {Solar PV / Wind / BESS / Fuel Cell / Micro-turbine / Hybrid} |
| Rated Capacity | {kW / MW} |
| Inverter Model | {Manufacturer, Model} |
| Inverter Rating | {kVA, voltage, frequency} |
| Energy Storage (if any) | {Type, kWh capacity} |
| Expected Annual Generation | {MWh/yr} |

## 2. Interconnection Requirements

| # | Requirement | Specification | Status | Notes |
|---|---|---|---|---|
| 2.1 | Interconnection Point | {Bus / Feeder / Panel ID} | {Done / Pending} | |
| 2.2 | Voltage Level | {e.g., 380 V / 11.4 kV / 22.8 kV} | | |
| 2.3 | Interconnection Standard | {IEEE 1547 / CNS / Utility-specific} | | |
| 2.4 | Interconnection Agreement | {Agreement ref / status} | | |
| 2.5 | Metering Requirements | {Revenue meter type, CT/PT ratio} | | |
| 2.6 | Protection Coordination Study | {Study ref / completed?} | | |

## 3. Anti-Islanding Protection

| # | Requirement | Method / Setting | Verified |
|---|---|---|---|
| 3.1 | Passive anti-islanding | {Over/under voltage, over/under frequency} | {Y/N} |
| 3.2 | Active anti-islanding | {Frequency shift / impedance measurement} | {Y/N} |
| 3.3 | Direct transfer trip (DTT) | {Required? If yes, via what channel?} | {Y/N} |
| 3.4 | Islanding detection time | {< 2 seconds per IEEE 1547} | {Y/N} |
| 3.5 | Reconnection delay | {5 minutes per IEEE 1547-2018} | {Y/N} |

## 4. Power Quality Requirements

| # | Parameter | Limit | DER Compliance | Verified |
|---|---|---|---|---|
| 4.1 | Voltage regulation | {+/- 5% at PCC} | {inverter Volt-VAR mode} | {Y/N} |
| 4.2 | Voltage flicker | {Pst < 1.0, Plt < 0.65} | {ramp rate limiting} | {Y/N} |
| 4.3 | Harmonic distortion (THDi) | {< 5% per IEEE 519} | {inverter spec} | {Y/N} |
| 4.4 | DC injection | {< 0.5% of rated} | {isolation transformer / inverter} | {Y/N} |
| 4.5 | Power factor | {0.95 leading to 0.95 lagging} | {inverter reactive capability} | {Y/N} |
| 4.6 | Frequency ride-through | {per IEEE 1547-2018 Cat II/III} | {inverter firmware} | {Y/N} |
| 4.7 | Voltage ride-through | {per IEEE 1547-2018 Cat II/III} | {inverter firmware} | {Y/N} |

## 5. Communication and Control

| # | Requirement | Specification | Status |
|---|---|---|---|
| 5.1 | Communication Protocol | {Modbus TCP / DNP3 / IEC 61850 / SunSpec} | {Configured / Pending} |
| 5.2 | SCADA Integration | {Point list ref / monitoring scope} | |
| 5.3 | Remote Curtailment | {Utility or site operator can curtail output} | |
| 5.4 | Data Reporting | {Generation data to utility, interval} | |
| 5.5 | Grid Support Functions | {Volt-VAR, Volt-Watt, Freq-Watt enabled} | |

## 6. Cybersecurity Controls

| # | Control | Implementation | IEC 62443 Ref |
|---|---|---|---|
| 6.1 | Network segmentation | {DER on dedicated VLAN / zone} | SR 5.1 |
| 6.2 | Access control | {Role-based, unique credentials} | SR 1.1 |
| 6.3 | Firmware integrity | {Signed firmware, verified before install} | SR 3.4 |
| 6.4 | Audit logging | {All config changes logged} | SR 6.1 |
| 6.5 | Secure communication | {TLS / VPN for remote access} | SR 4.1 |
| 6.6 | Patch management | {Vendor patch schedule, test before deploy} | SR 3.3 |

## 7. Commissioning Sign-off

- [ ] All items in Sections 2-6 verified
- [ ] Anti-islanding test completed and documented
- [ ] Power quality measurements at PCC within limits
- [ ] Communication link to SCADA confirmed
- [ ] Cybersecurity controls verified

| Role | Name | Signature | Date |
|---|---|---|---|
| DER Installer | {name} | | {date} |
| Utility Representative | {name} | | {date} |
| Site Owner | {name} | | {date} |
