# ICS/OT Incident Response Plan

| Field | Value |
|-------|-------|
| Facility | {facility_name} |
| Plan Owner | {owner_name} |
| Version | {version} |
| Last Review | {date} |
| Next Review | {date} |

## 1. Purpose and Scope

This plan covers cybersecurity incident response for OT/ICS environments at {facility_name}, including SCADA, DCS, PLC, RTU, and associated network infrastructure.

**In Scope**: {list of OT systems and zones covered}
**Out of Scope**: {IT-only systems covered by separate IT IR plan}

## 2. Roles and Responsibilities

| Role | Name | Contact | Responsibility |
|------|------|---------|----------------|
| IR Lead | {name} | {phone/email} | Overall coordination, escalation decisions |
| OT Engineer | {name} | {phone/email} | Process safety assessment, control system actions |
| IT Security | {name} | {phone/email} | Network forensics, malware analysis |
| Plant Manager | {name} | {phone/email} | Authorization for operational changes |
| Safety Officer | {name} | {phone/email} | HSE impact assessment |
| Legal/Compliance | {name} | {phone/email} | Regulatory notification, evidence preservation |

## 3. Phase 1 -- Detection and Identification

- Monitor SIEM alerts, IDS/IPS, anomaly detection systems
- Correlate OT-specific indicators: unexpected logic changes, unauthorized connections, abnormal process values
- **Classification**: Severity 1 (Safety Impact) / Severity 2 (Operational Impact) / Severity 3 (Monitoring Only)

**OT-Specific Detection Sources**:
- Historian data anomalies (trend deviations outside process norms)
- Unauthorized PLC program changes (compare against baseline)
- New or unexpected network flows crossing zone boundaries
- HMI alarm floods or suppressed alarms

## 4. Phase 2 -- Triage and Assessment

- Determine if safety systems (SIS/ESD) are affected -- if YES, escalate immediately
- Assess blast radius: which zones, conduits, and assets are impacted
- Evaluate process safety impact vs. cybersecurity impact

**OT Triage Decision Tree**:
1. Is SIS/ESD compromised? -> Emergency shutdown protocol
2. Is process control affected? -> Engage OT engineer, consider manual operation
3. Is it IT-side only with no OT lateral movement? -> Standard IT IR with OT monitoring

## 5. Phase 3 -- Containment

**CRITICAL OT RULES**:
- **DO NOT** reboot PLCs or safety controllers without OT engineer approval
- **DO NOT** disconnect OT networks without assessing process safety impact
- **DO NOT** run antivirus scans on real-time control systems during production
- **DO** isolate affected segments at network boundary (firewall/switch ACL)
- **DO** preserve forensic evidence from historians and log servers before changes
- **DO** switch to manual operations if automated control is compromised

**Containment Actions**:

| Action | Responsible | Approval Required | Notes |
|--------|-------------|-------------------|-------|
| Block network segment at firewall | IT Security | IR Lead | Document rules changed |
| Disable compromised user accounts | IT Security | IR Lead | Coordinate with OT ops |
| Isolate affected HMI/workstation | OT Engineer | Plant Manager | Ensure backup HMI available |
| Enable enhanced logging | IT Security | None | Increase capture granularity |

## 6. Phase 4 -- Eradication

- Remove malware/unauthorized software using OT-approved tools
- Restore PLC/RTU programs from verified clean backups
- Reset all credentials that may have been compromised
- Patch exploited vulnerabilities (during maintenance window)
- **Preserve forensic images** before wiping any system

## 7. Phase 5 -- Recovery

- Restore systems from known-good backups in priority order (safety systems first)
- Validate PLC logic against engineering baseline before going live
- Perform functional testing of restored systems
- Monitor closely for 72 hours post-recovery for reinfection indicators
- Gradually return from manual to automated operations

**Recovery Priority Order**:
1. Safety Instrumented Systems (SIS)
2. Core process control (DCS/PLC)
3. SCADA/HMI
4. Historian and logging
5. Ancillary systems

## 8. Phase 6 -- Lessons Learned

- Conduct post-incident review within 2 weeks
- Document: timeline, root cause, what worked, what failed
- Update detection rules, firewall policies, and this IR plan
- Brief operations staff on indicators and revised procedures
- File regulatory notifications if required (NERC CIP, NIS2, etc.)

## Appendix A: Escalation Matrix

| Severity | Response Time | Notification | Authority |
|----------|--------------|--------------|-----------|
| Sev 1 -- Safety Impact | Immediate | Plant Manager + Safety + Executive | Emergency shutdown authorized |
| Sev 2 -- Operational Impact | < 1 hour | IR Lead + OT Engineer + Plant Manager | Containment authorized |
| Sev 3 -- Monitoring Only | < 4 hours | IR Lead + IT Security | Investigation authorized |

## Appendix B: Contact List

| Organization | Contact | Phone | Email | Role |
|-------------|---------|-------|-------|------|
| {vendor_name} | {contact} | {phone} | {email} | ICS vendor support |
| {cert_name} | {contact} | {phone} | {email} | National CERT/ICS-CERT |
| {law_enforcement} | {contact} | {phone} | {email} | Cyber crime reporting |
