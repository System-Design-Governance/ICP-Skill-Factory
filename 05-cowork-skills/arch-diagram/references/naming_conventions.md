# Device Naming Conventions

> Cross-diagram label consistency rules based on F6 ONS project

---

## 1. node_label Field (gen_d2.py)

The `node_label` field in YAML overrides the default "RTU" label for L1 devices:

| Diagram | `node_label` Value | Actual Device |
|---------|-------------------|---------------|
| PROT | `"BCU"` | 6MD85 Bay Controller |
| CCTV | `"NVR"` | Network Video Recorder |
| ACS | `"ACS Panel"` | Access Control Panel |
| TEL | `"PBX"` | IP-PBX System |
| TPC | `"BCU"` + `"SPS"` | Bay Controller + SPS Controller |
| PWR | `"RTU"` | SICAM A8000 (correct) |
| SCADA | `"RTU"` | SICAM A8000 (correct) |
| Overview | `"BCU"` + `"RTU"` | Separate labels |

## 2. Cross-Diagram Label Unification

| Device | Unified Label | Do NOT Use |
|--------|--------------|-----------|
| WinCC OA SCADA Server | "WinCC OA Server x 2" | ❌ "SCADA Server x 2" (too generic) |
| FortiGate Firewall | Main: "FortiGate 80F HA x 3" / Sub: "FortiGate (See DWG-SCADA)" | ❌ "OT Firewall" (no model) |
| FortiSwitch Core | "FortiSwitch 448E x 5" | ❌ "L3 Core Switch" (no model) |
| GPS Time Sync | "GPS/PTP x 2 IRIG-B" | ❌ "NTP Server" (too generic) |
| Legend RTU Icon | "BCU / RTU / IED" | ❌ "RTU / IED" (missing BCU) |
| Legend RedBox Icon | "DANP (PRP Dual-NIC)" | ❌ "RedBox" |

## 3. Chinese Removal Rules

All diagram labels must be in English. The following Chinese text must be replaced during patch:

| Original | Replace With |
|----------|-------------|
| `輔助設備` | `Auxiliary` |
| `SCADA 伺服器群` | Context-dependent (`SCADA / HMI`, `VMS / SCADA Integration`, etc.) |
| `HMI 及監控桌` | Remove |
| `MCC 群` | Context-dependent (`RCP Panel`, `PoE Switch`, `Bay LV Panel`, etc.) |
| `Gateway 責任分界點` | `Offshore SCADA Client` |
| `LAN-A（IEC 62439-3 獨立實體網路）` | `LAN-A (IEC 62439-3)` |

## 4. CBOM Alignment

Device labels must include **model + quantity** for CBOM traceability:

```
"7SL86 x 8\n87L Line Diff (M+B)"  →  CBOM-H101 (7SL86, Qty 8)
"FortiSwitch 124F x 22"           →  CBOM-H401 (8) + H402 (5) + ... = 22
```

## 5. SPS Special Rules

- SPS is **Curtailment** (降載), NOT UFLS/UVLS (those are load-side concepts)
- SPS curtailment targets are **WTG SCADA + ONS PCC CB** (our equipment), placed at L1
- SPS curtailment targets are NOT TPC's CB/DS/ES (those go in L0 as TPC-side equipment)

## 6. MCC Naming

MCC in this context does NOT mean "Motor Control Center". It represents different devices per diagram:
- PROT: RCP Panel / PoE Switch / Interface Panel
- SCADA: varies by context
- Replaced by patch_all.py per-diagram
