# Industrial Protocol Comparison Matrix

**Author:** {Author}
**Date:** {YYYY-MM-DD}
**Revision:** {Rev}

## 1. Overview

This reference compares commonly used industrial communication protocols for
OT/SCADA systems, covering performance, security, and applicability to help
select the right protocol for each integration scenario.

## 2. Protocol Comparison

| Attribute | Modbus RTU | Modbus TCP | DNP3 | IEC 61850 (MMS/GOOSE) | OPC UA | IEC 60870-5-104 |
|---|---|---|---|---|---|---|
| **Layer** | Serial (RS-485) | TCP/IP | Serial or TCP/IP | TCP/IP + Ethernet L2 | TCP/IP | TCP/IP |
| **Data Rate** | 9600-115200 bps | 10/100 Mbps (Ethernet) | 9600-115200 (serial), Ethernet | 100 Mbps+ | 10/100/1000 Mbps | 10/100 Mbps |
| **Max Nodes** | 247 per segment | Limited by network | 65534 addresses | Per substation (IED-based) | Unlimited (server-client) | 65534 addresses |
| **Topology** | Multidrop bus | Star / switched | Point-to-point or multidrop | Switched Ethernet, redundant | Client-server, pub-sub | Point-to-point |
| **Data Model** | Registers + coils (flat) | Registers + coils (flat) | Points with classes | Logical nodes (object-oriented) | Information model (object-oriented) | Information objects |
| **Timestamps** | None | None | Yes (ms resolution) | Yes (us resolution, GOOSE) | Yes (configurable) | Yes (ms resolution) |
| **Event Reporting** | Poll only | Poll only | Unsolicited + poll | Reports + GOOSE events | Subscriptions + events | Spontaneous + poll |
| **Security Features** | None | None (add VPN/TLS externally) | Secure Authentication v5 (SAv5) | Role-based access, TLS (Ed.2) | Built-in security policies (Basic256Sha256, certificates) | None native (add TLS/VPN) |
| **Interoperability** | Excellent (de facto standard) | Excellent | Good (utility standard) | Good (IEC conformance testing) | Excellent (cross-vendor) | Good (utility standard) |
| **Standardization** | Modbus.org specification | Modbus.org specification | IEEE 1815 | IEC 61850 series | IEC 62541 / OPC Foundation | IEC 60870-5-104 |

## 3. Use Case Suitability

| Use Case | Recommended Protocol(s) | Rationale |
|---|---|---|
| Simple I/O polling (PLC-to-PLC) | Modbus RTU/TCP | Low complexity, universal support |
| SCADA telemetry (utility WAN) | DNP3, IEC 60870-5-104 | Designed for WAN, event-driven, timestamps |
| Substation automation | IEC 61850 | Native power system data model, GOOSE for fast tripping |
| Enterprise-to-OT integration | OPC UA | Secure, platform-independent, rich data model |
| Edge computing / IoT gateway | OPC UA, MQTT + Sparkplug B | Pub-sub capable, modern security |
| Safety / protection signaling | IEC 61850 GOOSE, hardwired | Sub-4ms Ethernet-based trip signals |
| Legacy device integration | Modbus RTU | Widest device support, simple wiring |
| Multi-vendor historian collection | OPC UA (or OPC DA legacy) | Vendor-neutral, aggregation server pattern |

## 4. Security Comparison Detail

| Security Feature | Modbus RTU/TCP | DNP3 SAv5 | IEC 61850 Ed.2 | OPC UA |
|---|---|---|---|---|
| Authentication | None | HMAC challenge-response | TLS certificates | X.509 certificates |
| Encryption | None | None (auth only) | TLS 1.2+ | AES-256 (Security Policy) |
| Integrity | None | HMAC-SHA-256 | TLS | SHA-256 signatures |
| Role-based Access | None | User-based (SAv5) | Access control per LN | Role-based (per spec) |
| Audit Logging | None | Critical ASDU logging | Security event log | Built-in audit trail |
| IEC 62443 Alignment | Requires compensating controls | Partial (SL-1 to SL-2) | SL-2 capable | SL-2 to SL-3 capable |

## 5. Performance Characteristics

| Metric | Modbus RTU | Modbus TCP | DNP3 | IEC 61850 GOOSE | OPC UA |
|---|---|---|---|---|---|
| Typical poll cycle | 100 ms - 1 s | 10-100 ms | 1-10 s (integrity) | N/A (event-driven) | 100 ms - 1 s |
| Event latency | N/A (poll-based) | N/A (poll-based) | < 1 s (unsolicited) | < 4 ms (L2 multicast) | < 100 ms (subscription) |
| Bandwidth efficiency | Low (poll overhead) | Low (poll overhead) | Medium (event-driven) | High (L2, minimal overhead) | Medium-High |
| Store-and-forward | No | No | Yes (event buffers) | No (real-time only) | Yes (configurable) |

## 6. Selection Decision Guide

When choosing a protocol, consider:

1. **Existing infrastructure:** What protocols are already in use at the site?
2. **Device support:** Does the field device support the desired protocol?
3. **Security requirements:** What IEC 62443 security level is targeted?
4. **Performance needs:** Is sub-second event detection required?
5. **WAN or LAN:** Is communication over a wide-area network?
6. **Data model complexity:** Simple registers vs. structured object model?
7. **Regulatory requirements:** Does the utility or authority mandate a protocol?

## 7. References

- Modbus: modbus.org/specs
- DNP3: IEEE 1815-2012
- IEC 61850: IEC 61850 series (Parts 1-10)
- OPC UA: IEC 62541 / opcfoundation.org
- IEC 60870-5-104: IEC 60870-5-104:2006
- Security: IEC 62443 series
