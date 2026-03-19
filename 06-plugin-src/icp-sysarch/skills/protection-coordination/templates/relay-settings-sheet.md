# Relay Settings Calculation Sheet

**Project:** {Project Name}
**Study ID:** {PS-YYYY-NNN}
**Author:** {Author}
**Date:** {YYYY-MM-DD}
**Software:** {e.g., ETAP / CAPE / manual calculation}

## 1. System Data

| Parameter | Value |
|---|---|
| System Voltage | {kV} |
| System Frequency | {50 / 60 Hz} |
| Max 3-Phase Fault Current at Relay Location | {kA} |
| Max Phase-Ground Fault Current | {kA} |
| Min Fault Current (remote end) | {kA} |
| Max Load Current | {A} |
| CT Location | {description} |
| PT Location | {description} |

## 2. Relay Settings Register

| Relay ID | Location | Manufacturer | Model | CT Ratio | PT Ratio | Function |
|---|---|---|---|---|---|---|
| {R-001} | {Feeder F1 CB} | {SEL / ABB / Siemens} | {SEL-751} | {600/5} | {11400/110} | {Overcurrent (50/51)} |
| {R-002} | {Transformer T1 HV} | {SEL} | {SEL-387} | {200/5} | {69000/110} | {Differential (87)} |
| {R-003} | {Bus Tie CB} | {ABB} | {REF615} | {1200/5} | {11400/110} | {Overcurrent + Directional} |

## 3. Overcurrent Settings (ANSI 50/51)

| Setting | R-001 | R-002 | R-003 | Basis |
|---|---|---|---|---|
| **Phase Time-Overcurrent (51P)** | | | | |
| Pickup Current (A secondary) | {6.0} | {4.5} | {8.0} | {1.2x max load / CT ratio} |
| Pickup Current (A primary) | {720} | {180} | {1920} | |
| Time Dial Setting (TDS) | {3.0} | {2.5} | {5.0} | {Coordination study} |
| Curve Type | {IEEE Very Inverse} | {IEEE Extremely Inverse} | {IEC Standard Inverse} | |
| Trip Time at Max Fault | {0.15 s} | {0.10 s} | {0.25 s} | |
| Trip Time at Min Fault | {1.2 s} | {0.8 s} | {2.0 s} | |
| **Phase Instantaneous (50P)** | | | | |
| Pickup Current (A secondary) | {60.0} | {40.0} | {80.0} | {1.25x max through-fault} |
| Pickup Current (A primary) | {7200} | {1600} | {19200} | |
| Time Delay | {0.00 s} | {0.00 s} | {0.05 s} | |
| **Ground Time-Overcurrent (51G)** | | | | |
| Pickup Current (A secondary) | {1.0} | {0.5} | {1.5} | |
| Time Dial Setting (TDS) | {2.0} | {1.5} | {3.0} | |
| Curve Type | {IEEE Very Inverse} | {IEEE Very Inverse} | {IEC Standard Inverse} | |

## 4. Distance Protection Settings (ANSI 21) -- if applicable

| Setting | Zone 1 | Zone 2 | Zone 3 | Basis |
|---|---|---|---|---|
| Reach (ohm secondary) | {Z1 = 0.8x line Z} | {Z2 = 1.2x line Z} | {Z3 = 1.2x(line Z + adj line Z)} | |
| Reach (ohm primary) | {value} | {value} | {value} | |
| Time Delay | {0.00 s} | {0.30 s} | {0.60 s} | |
| Angle (MTA) | {75 deg} | {75 deg} | {75 deg} | |

## 5. Coordination Margins

| Upstream Relay | Downstream Relay | Fault Location | Upstream Trip Time | Downstream Trip Time | Coordination Margin | Adequate? |
|---|---|---|---|---|---|---|
| {R-003} | {R-001} | {Feeder F1 bus} | {0.55 s} | {0.15 s} | {0.40 s} | {Yes (>0.3 s)} |
| {R-001} | {R-Downstream} | {End of feeder} | {1.20 s} | {0.70 s} | {0.50 s} | {Yes (>0.3 s)} |

**Required coordination time interval (CTI):** {0.3 s for digital relays, 0.4 s for electromechanical}

## 6. Verification and Testing

| Relay ID | Test Type | Test Current | Expected Trip Time | Measured Trip Time | Pass/Fail | Tester | Date |
|---|---|---|---|---|---|---|---|
| {R-001} | {51P pickup} | {6.0 A sec} | {pickup} | {value} | | {name} | {date} |
| {R-001} | {51P timing} | {30 A sec} | {0.25 s} | {value} | | {name} | {date} |
| {R-001} | {50P inst.} | {60 A sec} | {< 50 ms} | {value} | | {name} | {date} |

## 7. Notes

- {Special considerations for motor starting, transformer inrush, cold load pickup}
- {Reference coordination curve plots: file reference}
- {Applicable standards: IEC 60255, IEEE C37.112, CNS}
