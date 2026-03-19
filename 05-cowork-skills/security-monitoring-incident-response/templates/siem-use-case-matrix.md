# SIEM Use Case Matrix -- OT/ICS Environment

| Field | Value |
|-------|-------|
| Facility | {facility_name} |
| SIEM Platform | {siem_product} |
| Version | {version} |
| Last Updated | {date} |

## Use Case Inventory

| UC-ID | Category | Description | Data Source(s) | Detection Logic | Severity | Response Action |
|-------|----------|-------------|----------------|-----------------|----------|-----------------|
| UC-001 | Authentication | Failed login attempts to OT device (>5 in 10 min) | Syslog, AD logs | Threshold: count(failed_auth) > 5 within 600s per source IP | High | Lock account, alert IR team, verify device status |
| UC-002 | Authentication | Login outside approved maintenance window | OT device logs, AD | Time-based: login event NOT within scheduled window | Medium | Alert OT engineer, verify authorization |
| UC-003 | Authentication | Default/service account interactive login | AD, local auth logs | Match: known service accounts with interactive session | Critical | Immediate investigation, potential credential compromise |
| UC-004 | Network | New device on OT network segment | NAC, DHCP, IDS | New MAC/IP not in approved asset inventory | High | Quarantine port, identify device, alert security |
| UC-005 | Network | Traffic crossing zone boundary (unauthorized) | Firewall logs, IDS | Flow not matching approved conduit policy | High | Block flow, alert IR team, review firewall rules |
| UC-006 | Network | Outbound connection from OT to internet | Firewall, proxy logs | OT source IP with destination outside OT/DMZ | Critical | Block immediately, investigate source, forensic capture |
| UC-007 | Network | Port scan detected in OT network | IDS/IPS, netflow | >20 unique dest ports from single source in 60s | High | Isolate source, investigate, check for lateral movement |
| UC-008 | Process | PLC program change detected | PLC audit log, IDS | Config-change event or logic-download detected | Critical | Verify against MOC, compare to baseline, alert OT engineer |
| UC-009 | Process | Firmware update on OT device | Device logs, NMS | Firmware-change event outside change window | Critical | Halt update if possible, verify authorization and integrity |
| UC-010 | Process | HMI alarm flood (>50 alarms in 5 min) | Alarm server, historian | Threshold: alarm_count > 50 within 300s | High | Alert operator, check for attack-induced condition |
| UC-011 | Process | Process value outside safety limits | Historian, SCADA | Analog value breaches high-high or low-low setpoint | Critical | Cross-check with SIS, verify sensor integrity |
| UC-012 | Malware | Known ICS malware signature detected | AV, EDR, IDS | Signature match for ICS-targeted malware (Triton, Industroyer) | Critical | Isolate host, engage IR, preserve evidence |
| UC-013 | Malware | Executable file transfer to OT zone | Firewall, DLP | File transfer with executable extension into OT segment | High | Block transfer, alert security, scan source |
| UC-014 | Access | Remote access session to OT (VPN/jump host) | VPN logs, jump host | Remote session initiated, log duration and actions | Medium | Log and monitor, alert if outside window |
| UC-015 | Access | Privileged escalation on OT system | OS logs, AD | Privilege escalation event on OT host | High | Investigate, verify authorization, review actions taken |
| UC-016 | Compliance | Logging gap detected (device stopped sending logs) | SIEM health monitor | No events from monitored source for >30 min | Medium | Check device connectivity, verify agent/syslog status |

## Data Source Requirements

| Data Source | Protocol | Collection Method | Retention |
|-------------|----------|-------------------|-----------|
| OT Firewalls | Syslog (UDP/TCP 514) | Log forwarder | 1 year |
| PLC/RTU Audit Logs | Vendor-specific | Polling agent or passive capture | 1 year |
| Windows AD/Event Logs | WinRM / WEF | Agent-based collection | 1 year |
| IDS/IPS Alerts | Syslog / API | Direct integration | 1 year |
| Historian | SQL / API | Scheduled query | Per historian policy |
| VPN/Jump Host | Syslog | Log forwarder | 1 year |
| Network Flows | NetFlow/IPFIX | Flow collector | 90 days |

## Tuning and Review Schedule

| Activity | Frequency | Responsible |
|----------|-----------|-------------|
| False positive review | Weekly | SOC Analyst |
| Detection rule tuning | Monthly | Security Engineer |
| New use case development | Quarterly | OT Security Lead |
| Full use case audit | Annually | CISO / OT Security |
