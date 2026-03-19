# Device Hardening Checklist

| Field | Value |
|-------|-------|
| Device Name | {device_name} |
| Device Type | PLC / RTU / HMI / Switch / Firewall / Server |
| Manufacturer / Model | {vendor} / {model} |
| Firmware Version | {current_version} |
| Zone / Location | {zone} / {physical_location} |
| Assessed By | {assessor} |
| Date | {date} |

## 1. Credential Management

| # | Item | Standard | Current | Compliant | Action |
|---|------|----------|---------|-----------|--------|
| 1.1 | Default credentials changed | All factory defaults replaced | {status} | Y / N / NA | {action} |
| 1.2 | Password complexity enforced | Min 12 chars, mixed case + special | {status} | Y / N / NA | {action} |
| 1.3 | Shared accounts eliminated | Individual accounts per operator | {status} | Y / N / NA | {action} |
| 1.4 | Service account passwords rotated | Rotated per policy schedule | {status} | Y / N / NA | {action} |

## 2. Unused Ports and Services

| # | Item | Standard | Current | Compliant | Action |
|---|------|----------|---------|-----------|--------|
| 2.1 | Unused physical ports disabled | No open Ethernet/USB/serial ports | {status} | Y / N / NA | {action} |
| 2.2 | Unused network services disabled | Only required services running | {status} | Y / N / NA | {action} |
| 2.3 | Unused protocols disabled | No Telnet, FTP, SNMP v1/v2 | {status} | Y / N / NA | {action} |
| 2.4 | Web interfaces secured or disabled | HTTPS only or disabled if unused | {status} | Y / N / NA | {action} |

## 3. Firmware and Patch Management

| # | Item | Standard | Current | Compliant | Action |
|---|------|----------|---------|-----------|--------|
| 3.1 | Firmware at latest stable version | Vendor-recommended version | {status} | Y / N / NA | {action} |
| 3.2 | Security patches applied | All applicable patches installed | {status} | Y / N / NA | {action} |
| 3.3 | Patch validation tested | Tested in staging before production | {status} | Y / N / NA | {action} |

## 4. Logging and Monitoring

| # | Item | Standard | Current | Compliant | Action |
|---|------|----------|---------|-----------|--------|
| 4.1 | Audit logging enabled | Auth, config changes, alarms logged | {status} | Y / N / NA | {action} |
| 4.2 | Log forwarding configured | Logs sent to central SIEM/syslog | {status} | Y / N / NA | {action} |
| 4.3 | NTP synchronization | Time synced to authoritative source | {status} | Y / N / NA | {action} |
| 4.4 | Log retention adequate | Min 90 days local, 1 yr centralized | {status} | Y / N / NA | {action} |

## 5. Access Control

| # | Item | Standard | Current | Compliant | Action |
|---|------|----------|---------|-----------|--------|
| 5.1 | Role-based access configured | Least privilege per role | {status} | Y / N / NA | {action} |
| 5.2 | Session timeout configured | Auto-logout after inactivity | {status} | Y / N / NA | {action} |
| 5.3 | Remote access restricted | VPN/jump-host only, MFA enabled | {status} | Y / N / NA | {action} |
| 5.4 | Login banner displayed | Legal/warning banner on access | {status} | Y / N / NA | {action} |

## 6. Physical Security

| # | Item | Standard | Current | Compliant | Action |
|---|------|----------|---------|-----------|--------|
| 6.1 | Physical access restricted | Locked cabinet/room, access log | {status} | Y / N / NA | {action} |
| 6.2 | USB ports physically secured | Blocked or tamper-evident | {status} | Y / N / NA | {action} |
| 6.3 | Console port secured | Physical access control on serial | {status} | Y / N / NA | {action} |

## 7. Backup and Recovery

| # | Item | Standard | Current | Compliant | Action |
|---|------|----------|---------|-----------|--------|
| 7.1 | Configuration backed up | Current config stored securely | {status} | Y / N / NA | {action} |
| 7.2 | Backup tested/verified | Restore tested within last cycle | {status} | Y / N / NA | {action} |
| 7.3 | Recovery procedure documented | Step-by-step restore procedure | {status} | Y / N / NA | {action} |

## Summary

- **Total Items**: {count}
- **Compliant**: {count} | **Non-Compliant**: {count} | **N/A**: {count}
- **Compliance Rate**: {percentage}%
- **Critical Findings**: {list_critical_items}

**Sign-off**: {assessor} | Date: {date}
