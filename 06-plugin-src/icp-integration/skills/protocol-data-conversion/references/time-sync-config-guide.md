# NTP/PTP Time Synchronization Configuration Guide

## 1. Overview

Accurate time synchronization is critical in OT environments for event sequencing, fault analysis, protection coordination, and regulatory compliance. This guide covers NTP and PTP configuration for industrial control systems per IEC 62439 and IEEE 1588.

## 2. NTP Stratum Hierarchy

| Stratum | Role | Typical Source | Accuracy |
|---|---|---|---|
| Stratum 0 | Reference clock | GPS receiver, atomic clock, CDMA | < 1 us |
| Stratum 1 | Primary server | Directly connected to Stratum 0 | < 10 us |
| Stratum 2 | Secondary server | Syncs from Stratum 1 | < 100 us |
| Stratum 3 | Local server | Syncs from Stratum 2 | < 1 ms |
| Stratum 4+ | Client | Syncs from upstream | < 10 ms |

### NTP Configuration Checklist
- [ ] Deploy minimum two Stratum 1 servers per site for redundancy
- [ ] Configure `prefer` keyword for GPS-backed source
- [ ] Set `maxpoll` and `minpoll` intervals (recommended: minpoll 4, maxpoll 6 for OT)
- [ ] Enable NTP authentication (symmetric key or Autokey)
- [ ] Restrict NTP access via `restrict` directives (deny by default, allow known subnets)
- [ ] Monitor offset and jitter via `ntpq -p` or SNMP traps

## 3. PTP (IEEE 1588) Clock Roles

| Role | Function | Deployment |
|---|---|---|
| Grandmaster Clock (GM) | Authoritative time source for the PTP domain | Typically GPS-disciplined; one per PTP domain (plus hot standby) |
| Boundary Clock (BC) | Terminates and re-distributes PTP on each port | Installed in managed Ethernet switches at network boundaries |
| Transparent Clock (TC) | Measures and corrects residence time without terminating PTP | Layer-2 switches in the data path |
| Ordinary Clock (OC) | End device — slave that synchronizes to GM | IEDs, PLCs, RTUs, merging units |

### PTP Profile Selection

| Profile | Standard | Use Case | Accuracy Target |
|---|---|---|---|
| Default (IEEE 1588) | IEEE 1588-2008 | General-purpose | < 1 us |
| Power Profile | IEEE C37.238 / IEC 61850-9-3 | Substation automation, synchrophasors | < 1 us |
| Telecom Profile | ITU-T G.8275.1 | Carrier-grade synchronization | < 1.5 us |
| Utility Profile | IEC 62439-3 (PRP/HSR) | Redundant substation networks | < 1 us |

## 4. Accuracy Requirements per IEC 62439

| Application | Required Accuracy | Recommended Protocol |
|---|---|---|
| Sampled Values (IEC 61850-9-2) | < 1 us | PTP (Power Profile) |
| GOOSE messaging | < 1 ms (typical) | PTP or NTP Stratum 2+ |
| Event logging / SOE | < 1 ms | PTP or NTP Stratum 2 |
| SCADA polling | < 10 ms | NTP Stratum 3 |
| Historian timestamping | < 100 ms | NTP Stratum 3 |
| Business / IT systems | < 1 s | NTP Stratum 4 |

## 5. OT-Specific Considerations

### 5.1 GPS Source
- Install GPS antenna with clear sky view (minimum 4 satellites)
- Use surge-protected antenna cable with low-loss coaxial (< 50 m recommended)
- Configure GNSS receiver for GPS+GLONASS+Galileo multi-constellation for resilience
- Provide backup battery or capacitor for receiver holdover

### 5.2 Holdover
Holdover is the ability to maintain accurate time when the GPS reference is lost.

| Oscillator Type | Holdover (1 us accuracy) | Cost | Use Case |
|---|---|---|---|
| TCXO | Minutes | Low | Non-critical clients |
| OCXO | Hours to 1 day | Medium | Substation grandmaster |
| Rubidium | Days to weeks | High | Critical infrastructure, IEC 61850 SV |

### 5.3 Network Design for PTP
- Use PTP-aware (boundary clock or transparent clock) switches end-to-end
- Avoid asymmetric paths — ensure equal forward/reverse latency
- Separate PTP traffic on a dedicated VLAN where possible
- PTP domain separation: use different domain numbers for independent systems

## 6. Troubleshooting Quick Reference

| Symptom | Likely Cause | Action |
|---|---|---|
| Large offset (> 10 ms) | GPS antenna fault or cable loss | Check antenna, verify satellite lock |
| Jitter spikes | Non-PTP-aware switch in path | Replace with boundary/transparent clock switch |
| Slave not syncing | Firewall blocking UDP 319/320 | Open PTP ports, verify VLAN tagging |
| Holdover drift exceeding spec | Oscillator aging or temperature | Calibrate or upgrade oscillator |
| NTP auth failure | Key mismatch or expired key | Verify key ID and secret on both ends |
