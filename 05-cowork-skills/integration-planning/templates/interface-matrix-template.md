# Interface Integration Matrix

**Project:** {project_name}
**Revision:** {revision} | **Date:** {date}
**Prepared By:** {author} | **Approved By:** {approver}

## Purpose

This matrix tracks all system-to-system interfaces, their protocols, data elements, and current integration status. Use it as the single source of truth for interface planning and verification.

## Interface Matrix

| Interface ID | System A | System B | Protocol | Data Elements | Direction | Frequency | Owner | Status | Test Method |
|---|---|---|---|---|---|---|---|---|---|
| IF-001 | {system_a} | {system_b} | {Modbus TCP/OPC UA/MQTT/API} | {tag list or data set} | {A->B / B->A / Bidirectional} | {Real-time / 1s / 10s / On-change / Daily} | {responsible_person} | {Planned / In-Dev / Tested / Approved} | {Loopback / Simulation / Live} |
| IF-002 | | | | | | | | | |
| IF-003 | | | | | | | | | |
| IF-004 | | | | | | | | | |
| IF-005 | | | | | | | | | |

## Interface Categories

| Category | Description | Examples |
|---|---|---|
| Process Control | Real-time control signals | PLC-to-SCADA, PLC-to-PLC |
| Data Historian | Time-series data collection | SCADA-to-Historian, IoT-to-Cloud |
| Business Systems | Enterprise integration | MES-to-ERP, CMMS-to-ERP |
| Safety | Safety-related interfaces | SIS-to-PLC, Fire&Gas-to-ESD |
| External | Third-party / utility | Utility SCADA, Vendor remote access |

## Status Definitions

| Status | Meaning |
|---|---|
| Planned | Interface identified, design not started |
| In-Dev | Interface under development or configuration |
| Tested | FAT or bench-level testing complete |
| Approved | SAT complete, accepted for operation |
| Deferred | Postponed to future phase |

## Notes

- {Add interface-specific constraints, bandwidth requirements, or firewall rules here}
- All safety-related interfaces (Category: Safety) require independent verification per IEC 61511.
- Protocol version and firmware compatibility must be confirmed before integration testing.

## Revision History

| Rev | Date | Author | Description |
|---|---|---|---|
| 0 | {date} | {author} | Initial release |
