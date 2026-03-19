# OT Firewall Rule Template

| Field | Value |
|-------|-------|
| Firewall Name | {firewall_name} |
| Firewall Model | {vendor} / {model} |
| Location | {zone_boundary} |
| Policy Owner | {owner} |
| Last Review Date | {date} |
| Next Review Date | {date} |

## Rule Set

| Rule # | Source Zone | Source IP / Subnet | Dest Zone | Dest IP / Subnet | Protocol | Port | Action | Justification | Expiry | Ticket # |
|--------|-----------|-------------------|-----------|------------------|----------|------|--------|---------------|--------|----------|
| 1 | {zone} | {ip/cidr} | {zone} | {ip/cidr} | TCP | {port} | Allow | {business justification} | {date or Permanent} | {change_ticket} |
| 2 | {zone} | {ip/cidr} | {zone} | {ip/cidr} | UDP | {port} | Allow | {business justification} | {date or Permanent} | {change_ticket} |
| ... | | | | | | | | | | |
| 998 | Any | Any | Any | Any | Any | Any | Deny | Default deny -- log all | Permanent | Baseline |
| 999 | Any | Any | Any | Any | Any | Any | Drop | Implicit drop | Permanent | Baseline |

## Common OT Protocol Ports Reference

| Protocol | Port(s) | Typical Use | Notes |
|----------|---------|-------------|-------|
| Modbus TCP | 502 | PLC communication | No built-in auth; restrict by IP |
| EtherNet/IP | 44818, 2222 | CIP-based devices | Implicit + explicit messaging |
| OPC UA | 4840 | Historian, SCADA | Use certificate-based auth |
| OPC DA/DCOM | 135 + dynamic | Legacy SCADA | Avoid; migrate to OPC UA |
| DNP3 | 20000 | Substation/utility SCADA | Consider Secure Authentication |
| IEC 61850 MMS | 102 | Substation automation | GOOSE on layer 2, MMS on TCP |
| IEC 60870-5-104 | 2404 | Telecontrol | Limited security; use VPN |
| S7comm | 102 | Siemens PLC | No encryption; restrict tightly |
| BACnet | 47808 (UDP) | Building automation | Restrict to BMS zone |
| HTTPS (management) | 443 | Device web interfaces | Certificate-based access preferred |
| SSH | 22 | Secure CLI access | Key-based auth preferred |
| Syslog | 514 (UDP/TCP) | Log forwarding | One-directional to SIEM |
| NTP | 123 (UDP) | Time synchronization | One-directional to NTP server |

## Rule Review Criteria

- All rules must have a documented business justification
- Temporary rules must include an expiry date and associated change ticket
- Rules permitting traffic from higher to lower security zones require additional approval
- "Any" in source or destination is prohibited for Allow rules
- Bi-directional rules should be split into two unidirectional rules
- Rules must be reviewed at minimum annually or upon network change

## Change Log

| Date | Change Description | Changed By | Approved By | Ticket # |
|------|-------------------|------------|-------------|----------|
| {date} | {description} | {name} | {name} | {ticket} |
