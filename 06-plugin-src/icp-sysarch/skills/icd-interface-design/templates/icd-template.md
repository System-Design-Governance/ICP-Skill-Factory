# Interface Control Document (ICD)

**Project:** {Project Name}
**Document ID:** {ICD-XXX-YYY}
**Author:** {Author}
**Date:** {YYYY-MM-DD}
**Revision:** {Rev}
**Status:** {Draft / Under Review / Approved}

## 1. Purpose

This ICD defines the interface between {System A} and {System B}, specifying
protocol, data format, timing, error handling, and security requirements to
ensure interoperability and maintainability.

## 2. Interface Register

| Interface ID | System A | System B | Protocol | Data Format | Direction | Frequency / Trigger | Error Handling | Security Req. | Responsible Party |
|---|---|---|---|---|---|---|---|---|---|
| {IF-001} | {e.g., PLC-01} | {e.g., SCADA Server} | {Modbus TCP} | {Register map per Section 3} | {A -> B} | {1 s poll} | {Timeout 3 s, retry x2, alarm on fail} | {VPN / TLS / None} | {Vendor X / ICP} |
| {IF-002} | {e.g., SCADA Server} | {e.g., Historian} | {OPC UA} | {OPC UA node set} | {A -> B} | {On change, 500 ms deadband} | {Store-and-forward on disconnect} | {OPC UA Security Policy Basic256Sha256} | {ICP} |
| {IF-003} | {e.g., RTU-05} | {e.g., Control Center} | {DNP3} | {DNP3 point list} | {Bidirectional} | {Unsolicited + integrity poll 60 s} | {SAv5 auth, link retry} | {DNP3 Secure Auth v5} | {Vendor Y} |

## 3. Data Mapping Details

### IF-001: {PLC-01} to {SCADA Server}

| Register Address | Data Point | Data Type | Scaling | Eng. Units | R/W | Description |
|---|---|---|---|---|---|---|
| 40001 | {Bus Voltage} | {FLOAT32} | {x0.1} | {kV} | R | {Main bus voltage measurement} |
| 40003 | {Active Power} | {FLOAT32} | {x0.01} | {MW} | R | {Total active power} |
| 40005 | {CB Status} | {UINT16} | {bit 0} | {0=Open,1=Closed} | R | {Circuit breaker status} |
| 00001 | {CB Trip Cmd} | {BOOL} | {--} | {1=Trip} | W | {Circuit breaker trip command} |

## 4. Timing and Sequencing

- **Normal scan cycle:** {1 second}
- **Priority data (e.g., trips):** {< 100 ms via exception-based reporting}
- **Startup sequence:** {System A must be online before System B initiates polling}
- **Graceful shutdown:** {System A sends shutdown notification, System B switches to last-known-good}

## 5. Error Handling and Diagnostics

| Condition | Detection Method | Response | Notification |
|---|---|---|---|
| Communication timeout | {No response in 3 s} | {Retry x2, then set quality bad} | {Alarm to HMI} |
| Data out of range | {Value exceeds eng. limits} | {Clamp and flag quality uncertain} | {Event log} |
| Authentication failure | {SA challenge fail} | {Block session, log event} | {Security alarm} |

## 6. Security Requirements

- Network segmentation: {Zone / Conduit per IEC 62443}
- Authentication: {method}
- Encryption: {method or N/A}
- Access control: {role-based per IEC 62443-3-3 SR 1.1}

## 7. Testing and Acceptance

- [ ] Communication link established and verified
- [ ] All data points read correctly with expected scaling
- [ ] Write commands verified with proper authorization
- [ ] Failover / error handling tested per Section 5
- [ ] Security controls verified per Section 6

## 8. Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| System A Owner | {name} | | {date} |
| System B Owner | {name} | | {date} |
| Integration Lead | {name} | | {date} |
