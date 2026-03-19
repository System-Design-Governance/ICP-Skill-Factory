# PLC Logic Test Plan

**Project:** {Project Name}
**PLC System:** {e.g., PLC-01, Allen-Bradley ControlLogix / Siemens S7-1500}
**Program Version:** {version / revision}
**Author:** {Author}
**Date:** {YYYY-MM-DD}
**Revision:** {Rev}

## 1. Scope

This test plan covers functional verification of PLC logic for {system/area}.
All function blocks and control sequences are tested against design specifications
before commissioning.

## 2. Test Environment

| Item | Description |
|---|---|
| Test Method | {Simulation / Hardware-in-the-loop / Bench test with I/O} |
| PLC Hardware | {model, firmware version} |
| Simulation Tool | {e.g., PLCSIM Advanced / Factory I/O / Simulink} |
| I/O Forcing | {Allowed during test only, all forces removed before handover} |
| Test Instrument | {e.g., signal generator, decade box, test relay kit} |

## 3. Test Register

| Test ID | Function Block / Routine | Test Description | Preconditions | Input Conditions | Expected Output | Actual Output | Pass/Fail | Tester | Date | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| {TC-001} | {Motor Start/Stop (FB_Motor)} | {Start command with all permissives met} | {Motor ready, no faults, selector in Auto} | {Start_Cmd = TRUE} | {Motor_Run = TRUE, Starter DO energized} | {value} | | {name} | {date} | |
| {TC-002} | {Motor Start/Stop (FB_Motor)} | {Start command with interlock NOT met} | {Lube oil pressure low} | {Start_Cmd = TRUE} | {Motor_Run = FALSE, Alarm "Interlock not met"} | {value} | | {name} | {date} | |
| {TC-003} | {Motor Start/Stop (FB_Motor)} | {Running motor fault trip} | {Motor running normally} | {Overload_DI = TRUE} | {Motor_Run = FALSE, Trip latch set, Alarm} | {value} | | {name} | {date} | |
| {TC-004} | {Motor Start/Stop (FB_Motor)} | {Fault reset and restart} | {Motor tripped, fault cleared} | {Reset_Cmd = TRUE, then Start_Cmd = TRUE} | {Trip latch cleared, motor restarts} | {value} | | {name} | {date} | |
| {TC-005} | {Analog Scaling (FB_AI)} | {Input at 0% (4 mA)} | {Channel configured} | {Raw input = 4 mA (0 counts)} | {PV = 0.0 {eng. units}} | {value} | | {name} | {date} | |
| {TC-006} | {Analog Scaling (FB_AI)} | {Input at 100% (20 mA)} | {Channel configured} | {Raw input = 20 mA (max counts)} | {PV = {max eng. value}} | {value} | | {name} | {date} | |
| {TC-007} | {Analog Scaling (FB_AI)} | {Input out of range (wire break)} | {Channel configured} | {Raw input < 3.8 mA} | {PV = bad quality, wire break alarm} | {value} | | {name} | {date} | |
| {TC-008} | {Sequence Control (SFC_Startup)} | {Normal startup sequence} | {All permissives met} | {Start_Sequence = TRUE} | {Steps execute in order with correct timing} | {value} | | {name} | {date} | |
| {TC-009} | {Sequence Control (SFC_Startup)} | {Sequence abort mid-step} | {Sequence at Step 3} | {Abort_Cmd = TRUE} | {Safe shutdown, outputs de-energized in order} | {value} | | {name} | {date} | |
| {TC-010} | {PID Loop (FB_PID)} | {Setpoint step response} | {Loop in Auto, stable} | {SP change +10%} | {PV settles within {X} s, overshoot < {Y}%} | {value} | | {name} | {date} | |
| {TC-011} | {Communication (FB_Modbus)} | {Normal data exchange} | {Link established} | {Poll cycle running} | {All registers read correctly, quality Good} | {value} | | {name} | {date} | |
| {TC-012} | {Communication (FB_Modbus)} | {Communication failure} | {Cable disconnected} | {No response for 3 polls} | {Comm fail alarm, outputs go to failsafe} | {value} | | {name} | {date} | |
| {TC-013} | {Watchdog / Heartbeat} | {PLC watchdog timeout} | {PLC running} | {Force watchdog timer to expire} | {Safety relay de-energizes, alarm generated} | {value} | | {name} | {date} | |
| {TC-014} | {E-Stop} | {Hardware E-Stop pressed} | {System running normally} | {E-Stop DI = 0 (de-energize to trip)} | {All controlled outputs de-energize} | {value} | | {name} | {date} | |

## 4. I/O Force Log

All forces applied during testing must be logged and removed after test completion.

| Force # | Address | Description | Forced Value | Applied By | Time On | Time Off | Removed Verified |
|---|---|---|---|---|---|---|---|
| {F-001} | {I0.0} | {Lube oil pressure switch} | {TRUE} | {name} | {HH:MM} | {HH:MM} | {Y} |

**All forces removed and verified:** [ ] Yes, confirmed by {name} on {date}

## 5. Test Summary

| Category | Total Tests | Passed | Failed | Deferred |
|---|---|---|---|---|
| Motor Control | {N} | {N} | {N} | {N} |
| Analog Scaling | {N} | {N} | {N} | {N} |
| Sequence Control | {N} | {N} | {N} | {N} |
| PID Control | {N} | {N} | {N} | {N} |
| Communication | {N} | {N} | {N} | {N} |
| Safety Functions | {N} | {N} | {N} | {N} |
| **Total** | **{N}** | **{N}** | **{N}** | **{N}** |

## 6. Sign-off

| Role | Name | Signature | Date |
|---|---|---|---|
| PLC Programmer | {name} | | {date} |
| Test Witness | {name} | | {date} |
| Project Engineer | {name} | | {date} |
