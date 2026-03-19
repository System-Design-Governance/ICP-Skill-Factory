# SCADA Point List

**Project:** {Project Name}
**System / Area:** {e.g., Substation A / Water Treatment Plant}
**Author:** {Author}
**Date:** {YYYY-MM-DD}
**Revision:** {Rev}
**SCADA Platform:** {e.g., Wonderware / Ignition / VTScada / ClearSCADA}

## 1. Conventions

- **Point ID format:** {SITE}-{AREA}-{DEVICE}-{TYPE}{SEQ} (e.g., SS01-BUS1-VT01-AI001)
- **Data types:** BOOL, INT16, UINT16, INT32, FLOAT32, STRING
- **Quality codes:** Good / Bad / Uncertain (OPC UA standard)
- **Alarm priority:** 1 = Critical, 2 = High, 3 = Medium, 4 = Low, 5 = Journal

## 2. Analog Input Points

| Point ID | Description | Source Device | Protocol | Register / Address | Data Type | Raw Min | Raw Max | EU Min | EU Max | Eng. Units | Deadband | Scan Rate | HH Limit | H Limit | L Limit | LL Limit | Alarm Priority |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| {SS01-BUS1-VT01-AI001} | {Bus 1 Voltage} | {RTU-01} | {Modbus TCP} | {40001-40002} | {FLOAT32} | {0} | {32767} | {0} | {15.0} | {kV} | {0.1} | {1 s} | {12.5} | {12.0} | {10.0} | {9.5} | {2} |
| {SS01-TR01-CT01-AI002} | {Transformer T1 Current} | {RTU-01} | {Modbus TCP} | {40003-40004} | {FLOAT32} | {0} | {32767} | {0} | {1200} | {A} | {1.0} | {1 s} | {1100} | {1000} | {--} | {--} | {2} |
| {SS01-TR01-TT01-AI003} | {T1 Winding Temp} | {RTU-01} | {Modbus TCP} | {40005-40006} | {FLOAT32} | {0} | {1000} | {0} | {150} | {deg C} | {0.5} | {5 s} | {120} | {105} | {--} | {--} | {1} |

## 3. Analog Output Points

| Point ID | Description | Target Device | Protocol | Register / Address | Data Type | EU Min | EU Max | Eng. Units | Scan Rate | Access Level |
|---|---|---|---|---|---|---|---|---|---|---|
| {SS01-CAP1-AO001} | {Capacitor Bank Setpoint} | {RTU-01} | {Modbus TCP} | {40101} | {INT16} | {0} | {100} | {%} | {on change} | {Operator L2} |

## 4. Digital Input Points (Status)

| Point ID | Description | Source Device | Protocol | Register / Address | Data Type | State 0 Text | State 1 Text | Alarm on State | Alarm Priority | Scan Rate |
|---|---|---|---|---|---|---|---|---|---|---|
| {SS01-CB01-DI001} | {CB-01 Status} | {RTU-01} | {Modbus TCP} | {10001} | {BOOL} | {Open} | {Closed} | {0 = Alarm} | {1} | {1 s} |
| {SS01-CB01-DI002} | {CB-01 Spring Charged} | {RTU-01} | {Modbus TCP} | {10002} | {BOOL} | {Not Charged} | {Charged} | {0 = Alarm} | {3} | {5 s} |
| {SS01-DR01-DI003} | {Door Intrusion} | {RTU-01} | {Modbus TCP} | {10003} | {BOOL} | {Secure} | {Open} | {1 = Alarm} | {2} | {1 s} |

## 5. Digital Output Points (Control)

| Point ID | Description | Target Device | Protocol | Register / Address | Data Type | Command 0 | Command 1 | Interlock | Access Level | Confirm Required |
|---|---|---|---|---|---|---|---|---|---|---|
| {SS01-CB01-DO001} | {CB-01 Trip/Close} | {RTU-01} | {DNP3} | {CROB idx 0} | {BOOL} | {Trip} | {Close} | {Sync check} | {Operator L3} | {Yes} |

## 6. Calculated / Derived Points

| Point ID | Description | Formula / Source | Eng. Units | Update Rate |
|---|---|---|---|---|
| {SS01-BUS1-CALC001} | {Bus 1 Active Power} | {AI001 * AI002 * cos(phi)} | {MW} | {1 s} |
| {SS01-TR01-CALC002} | {T1 Loading %} | {(CALC001 / T1_Rating) * 100} | {%} | {1 s} |

## 7. Summary Statistics

| Category | Count |
|---|---|
| Analog Inputs | {N} |
| Analog Outputs | {N} |
| Digital Inputs | {N} |
| Digital Outputs | {N} |
| Calculated Points | {N} |
| **Total Points** | **{N}** |
