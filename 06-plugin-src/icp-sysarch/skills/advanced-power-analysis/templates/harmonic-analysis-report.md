# Harmonic Analysis Report

**Project:** {Project Name}
**Study ID:** {HA-YYYY-NNN}
**Author:** {Author}
**Date:** {YYYY-MM-DD}
**Software:** {e.g., ETAP / DIgSILENT / measurement instrument model}
**Standard:** IEEE 519-2022

## 1. Study Scope

{Describe the scope and motivation for this harmonic study. Examples:
- New VFD installation: assess harmonic injection at PCC
- Capacitor bank addition: evaluate resonance risk
- Compliance verification for utility interconnection agreement
- Periodic monitoring per plant maintenance program}

### 1.1 System Under Study

- **Facility:** {Plant / Substation name}
- **Voltage levels:** {e.g., 69 kV, 11.4 kV, 380 V}
- **Point of Common Coupling (PCC):** {Bus ID, voltage level}
- **Short-circuit capacity at PCC (Isc):** {kA}
- **Maximum demand load current (IL):** {A}
- **Isc/IL ratio:** {value -- determines IEEE 519 current distortion limits}

## 2. Measurement Points

| Point ID | Location | Voltage Level | Instrument | Measurement Period | Sampling |
|---|---|---|---|---|---|
| {MP-01} | {Main switchgear Bus A} | {11.4 kV} | {Fluke 1760 / Dranetz} | {7 days continuous} | {10-min aggregation per IEC 61000-4-30} |
| {MP-02} | {VFD input bus} | {380 V} | {PQ analyzer model} | {7 days continuous} | {10-min aggregation} |
| {MP-03} | {PCC metering point} | {69 kV} | {CT/PT + analyzer} | {7 days continuous} | {10-min aggregation} |

## 3. THD Results

| Point ID | Location | THDv (%) | IEEE 519 Limit (%) | Compliant? | THDi (%) | IEEE 519 Limit (%) | Compliant? |
|---|---|---|---|---|---|---|---|
| {MP-01} | {Bus A} | {3.2} | {5.0} | {Yes} | {8.1} | {8.0} | {No} |
| {MP-02} | {VFD input} | {6.8} | {5.0} | {No} | {28.5} | {--} | {N/A (not PCC)} |
| {MP-03} | {PCC} | {2.1} | {5.0} | {Yes} | {4.5} | {8.0} | {Yes} |

## 4. Individual Harmonic Levels

### Voltage Harmonics at {MP-01}

| Harmonic Order | Frequency (Hz) | Measured (%) | IEEE 519 Limit (%) | Status |
|---|---|---|---|---|
| 3rd | {180} | {1.8} | {3.0} | {OK} |
| 5th | {300} | {4.2} | {3.0} | {Exceeds} |
| 7th | {420} | {2.1} | {3.0} | {OK} |
| 11th | {660} | {1.5} | {3.0} | {OK} |
| 13th | {780} | {0.9} | {3.0} | {OK} |

### Current Harmonics at {MP-01}

| Harmonic Order | Frequency (Hz) | Measured (%) | IEEE 519 Limit (%) | Status |
|---|---|---|---|---|
| 5th | {300} | {5.8} | {7.0} | {OK} |
| 7th | {420} | {4.2} | {7.0} | {OK} |
| 11th | {660} | {3.1} | {3.5} | {OK} |
| 13th | {780} | {2.8} | {3.5} | {OK} |

## 5. Resonance Analysis

| Resonance Order | Frequency (Hz) | Impedance Peak (ohm) | Risk | Mitigation |
|---|---|---|---|---|
| {4.7} | {282} | {high} | {Near 5th harmonic -- amplification risk} | {Detune capacitor bank to 4.3rd} |

## 6. IEEE 519 Compliance Summary

| Criterion | PCC Result | Limit | Compliant? |
|---|---|---|---|
| THDv (95th percentile) | {2.1%} | {5.0%} | {Yes} |
| Individual voltage harmonic | {max 1.2% at 5th} | {3.0%} | {Yes} |
| THDi (95th percentile) | {4.5%} | {8.0%} | {Yes} |
| Individual current harmonic | {max 3.8% at 5th} | {7.0%} | {Yes} |

## 7. Filter Design Recommendations

{If non-compliant, recommend mitigation:}

1. **Passive filter:** {e.g., 5th harmonic C-type filter rated at X kvar, tuned to 282 Hz}
2. **Active filter:** {e.g., 100 A active harmonic filter at VFD bus}
3. **Multi-pulse drive:** {e.g., Replace 6-pulse VFD with 18-pulse to reduce 5th/7th}
4. **Capacitor detuning:** {e.g., Add 7% detuning reactor to existing capacitor bank}

## 8. References

- IEEE 519-2022: Standard for Harmonic Control in Electric Power Systems
- IEC 61000-4-30: Power quality measurement methods
- {Site one-line diagram: DWG-XXX}
- {Equipment harmonic data sheets from manufacturers}
