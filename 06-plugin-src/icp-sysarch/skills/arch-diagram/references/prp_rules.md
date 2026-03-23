# IEC 62439-3 PRP Architecture Rules

> Based on F6 ONS project lessons (46-node protection diagram, PRP dual-network)

---

## 1. PRP Correct Topology

```
         LAN-A (Independent Physical Network)     LAN-B (Independent Physical Network)
     ┌──────────────────────┐               ┌──────────────────────┐
     │ Core-A  Bay-A1  ...  │               │ Core-B  Bay-B1  ...  │
     └───┬───────┬──────────┘               └───┬───────┬──────────┘
         │       │                               │       │
         │    Port-A                          Port-B     │
         │    ┌──┴──────────────────────────────┴──┐     │
         │    │   DANP Device (7SJ82/6MD85)        │     │
         │    │   Single MAC + Single IP            │     │
         │    └────────────────────────────────────┘     │
```

## 2. Key Rules

| Rule | Description |
|------|-------------|
| **DANP Dual-NIC** | Each PRP device has 2 Ethernet ports, connecting to LAN-A and LAN-B Bay Switches respectively |
| **LAN Complete Isolation** | LAN-A and LAN-B have **no** switch-to-switch cross-links |
| **RedBox vs DANP** | RedBox bridges non-PRP devices; SIPROTEC 5 is DANP (native PRP), no RedBox needed |
| **Switch Not PRP-Aware** | PRP intelligence is at endpoints (DANP), switches are standard Ethernet |
| **SCADA Server = DANP** | SCADA Server needs dual NIC + PRP driver, presents single logical interface |
| **Same MAC/IP** | DANP's two ports share the same MAC address and IP address |

## 3. gen_d2.py PRP Implementation

```python
# gen_conn_inter_zone() — L2→L1 connections
# When prp=true, each Bay generates LAN-A + LAN-B connections
lines.append(emit_connection(f"L2.lana.SW_{feeder}_A", target_node, ...))
if prp:
    lines.append(emit_connection(f"L2.lanb.SW_{feeder}_B", target_node, ..., label=""))
```

## 4. Common Errors

| Error | Correct |
|-------|---------|
| ❌ L2→L1 only connects LAN-A | ✅ Must connect both LAN-A and LAN-B |
| ❌ IED connects via BCU | ✅ IED and BCU are parallel on PRP Station Bus |
| ❌ IED connects via RedBox | ✅ SIPROTEC 5 is DANP, direct PRP connection |
| ❌ LAN-B shows abbreviated names | ✅ LAN-A and LAN-B Bay Switch descriptions must be identical |
| ❌ Non-OT devices on PRP network | ✅ CCTV/ACS/TEL/PWR use Ethernet VLAN, not PRP |
| ❌ Mixed diagram (OT+IT) sets `prp_enabled: true` | ✅ Mixed diagrams set `false`; PRP shown only in PROT-specific diagram |
| ❌ IT Switch (FortiSwitch) appears in LAN-B | ✅ Only OT IEC 61850 devices have LAN-B |
| ❌ Non-PRP diagram zone labeled "LAN-A" | ✅ Use specific names: "Ethernet VLAN" / "Modbus TCP Network" / "Fortinet Managed Network" |
| ❌ Non-PRP diagram switch labeled "Core Switch A" | ✅ Drop the "A" (implies a B exists), use "Core Switch" |
| ❌ Non-PRP diagram link labeled "PRP LAN-A" | ✅ Use actual protocol: "Ethernet" / "Modbus TCP" |

## 5. PRP Cost Impact

| Item | Without PRP | With PRP | Multiplier |
|------|------------|----------|-----------|
| L2 Station Switches | 2 | 4 | ×2 |
| Bay Switches | n | n×4 | ×4 |
| RedBox | 0 | 10-20 | New |
| Fiber | Base | ×2 | ×2 |
| **Total Network Devices** | ~8 | ~48+ | **×3~6** |

F6 Actual: 15 switches estimated → 27 actual (+80%).
