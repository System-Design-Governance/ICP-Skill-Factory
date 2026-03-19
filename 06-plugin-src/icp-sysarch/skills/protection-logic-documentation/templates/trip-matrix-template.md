# Trip Matrix

**Project:** {Project Name}
**System / Unit:** {e.g., Gas Turbine GT-01 / Transformer T1 / Feeder F3}
**Author:** {Author}
**Date:** {YYYY-MM-DD}
**Revision:** {Rev}

## 1. Purpose

This trip matrix defines the complete mapping from input signals through logic
conditions to output actions for {system/unit}, ensuring all protective trips,
interlocks, and permissives are documented and testable.

## 2. Signal Legend

| Abbreviation | Meaning |
|---|---|
| DI | Digital Input |
| AI | Analog Input (with threshold) |
| DO | Digital Output |
| SOE | Sequence of Events |
| T | Time Delay (seconds) |

## 3. Trip Matrix

| # | Input Signal | Signal Type | Logic Condition | Output Action | Time Delay | Interlock | Priority | Bypass Allowed? | Test Procedure Ref |
|---|---|---|---|---|---|---|---|---|---|
| 1 | {Overspeed 110%} | AI | {Speed > 110% AND Run_Mode = TRUE} | {Master Trip, Fuel Valve Close} | {0 s} | {None} | {1 - Safety} | {No} | {TP-001} |
| 2 | {Bearing Temp HH} | AI | {Temp > {85 deg C} AND Run_Mode = TRUE} | {Unit Trip} | {0 s} | {None} | {1 - Safety} | {No} | {TP-002} |
| 3 | {Bearing Temp H} | AI | {Temp > {75 deg C}} | {Alarm only} | {5 s} | {None} | {3 - Warning} | {N/A} | {TP-003} |
| 4 | {Lube Oil Press LL} | AI | {Press < {0.5 bar} AND Run_Mode = TRUE} | {Unit Trip} | {3 s} | {Bypass during startup < 30 s} | {1 - Safety} | {Startup only} | {TP-004} |
| 5 | {Emergency Stop} | DI | {E-Stop = Pressed} | {Master Trip, all outputs de-energize} | {0 s} | {None} | {0 - E-Stop} | {No} | {TP-005} |
| 6 | {Fire Detection} | DI | {Fire_Zone_1 = TRUE OR Fire_Zone_2 = TRUE} | {Unit Trip, Fire Suppression Activate} | {0 s} | {Suppression arm switch ON} | {0 - E-Stop} | {No} | {TP-006} |
| 7 | {Generator Diff (87G)} | DI | {Relay 87G Trip contact} | {Generator CB Open, Field Breaker Open} | {0 s} | {None} | {1 - Safety} | {No} | {TP-007} |
| 8 | {Reverse Power (32)} | DI | {Relay 32 Trip contact} | {Generator CB Open} | {per relay setting} | {Unit in sync} | {2 - Equipment} | {No} | {TP-008} |

## 4. Priority Definitions

| Priority Level | Category | Description | Response |
|---|---|---|---|
| 0 | Emergency Stop | Immediate personnel safety | Hardwired, de-energize to trip |
| 1 | Safety Trip | Equipment/process safety critical | Automatic trip, no operator override |
| 2 | Equipment Protection | Prevent equipment damage | Automatic trip, timed override during startup |
| 3 | Warning / Alarm | Abnormal condition | Alarm only, operator action required |

## 5. Interlock Summary

| Interlock ID | Description | Condition | Affected Outputs |
|---|---|---|---|
| {IL-001} | {Start permissive} | {Lube oil press > 1.0 bar AND turning gear disengaged AND no active trips} | {Start command enabled} |
| {IL-002} | {Sync permissive} | {Voltage match < 5% AND freq match < 0.1 Hz AND phase < 10 deg} | {Sync CB close enabled} |
| {IL-003} | {Load rejection} | {Grid CB open AND unit running} | {Reduce to house load / trip} |

## 6. Test Procedure Cross-Reference

| Test ID | Trip Matrix Row(s) | Test Method | Acceptance Criteria |
|---|---|---|---|
| {TP-001} | {Row 1} | {Simulate overspeed via test input} | {Trip within 100 ms} |
| {TP-002} | {Row 2} | {Force AI value above threshold} | {Trip with correct time delay} |
| {TP-005} | {Row 5} | {Press physical E-Stop button} | {All outputs de-energize within 500 ms} |

## 7. Revision History

| Rev | Date | Author | Description |
|---|---|---|---|
| {A} | {YYYY-MM-DD} | {name} | {Initial issue} |
| {B} | {YYYY-MM-DD} | {name} | {Added fire suppression interlock} |
