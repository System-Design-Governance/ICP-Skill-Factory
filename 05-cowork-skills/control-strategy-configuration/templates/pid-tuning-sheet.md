# PID Tuning Record

**Project:** {Project Name}
**System / Unit:** {e.g., Boiler Drum Level / Compressor Suction Pressure}
**Author:** {Author}
**Date:** {YYYY-MM-DD}
**Revision:** {Rev}
**Controller Platform:** {e.g., Siemens S7-1500 / Allen-Bradley ControlLogix / DCS vendor}

## 1. Loop Identification

| Item | Value |
|---|---|
| Loop Tag | {e.g., LIC-101} |
| Process Variable (PV) | {e.g., Drum Level} |
| Setpoint (SP) | {e.g., 50% level} |
| Control Output (CO) | {e.g., Feedwater Valve FV-101 position, 0-100%} |
| Measurement Range | {e.g., 0-100% (0-1000 mm)} |
| Output Range | {e.g., 0-100% (4-20 mA)} |
| Control Action | {Direct / Reverse} |
| Scan / Execution Rate | {e.g., 100 ms / 250 ms / 1 s} |

## 2. Process Characteristics (from step test or model)

| Parameter | Value | Method |
|---|---|---|
| Process Gain (Kp) | {value, units} | {Step test / model identification} |
| Dead Time (Td) | {seconds} | |
| Time Constant (Tau) | {seconds} | |
| Td / Tau Ratio | {value} | {< 0.2 = easy, > 0.5 = difficult} |

## 3. Tuning Parameters

| Parameter | Initial Value | Final Value | Units | Notes |
|---|---|---|---|---|
| Proportional Gain (Kp) | {value} | {value} | {%/% or dimensionless} | |
| Integral Time (Ti) | {value} | {value} | {seconds or repeats/min} | |
| Derivative Time (Td) | {value} | {value} | {seconds} | {0 if PID not required} |
| Anti-Windup | {Enabled / Disabled} | {Enabled} | | {Clamp integrator when output saturates} |
| Output High Limit | {value} | {value} | {%} | |
| Output Low Limit | {value} | {value} | {%} | |
| Setpoint Ramp Rate | {value} | {value} | {units/s} | {If applicable} |
| Filter on PV | {value} | {value} | {seconds} | {First-order filter time constant} |
| Deadband | {value} | {value} | {eng. units} | |

### Tuning Method Used

{e.g., Ziegler-Nichols / Cohen-Coon / Lambda Tuning / IMC / Manual fine-tuning}

**Rationale:** {e.g., "Lambda tuning selected for smooth response; lambda = 3x dead time
to prioritize robustness over speed."}

## 4. Performance Criteria and Results

| Criterion | Target | Before Tuning | After Tuning | Pass? |
|---|---|---|---|---|
| Overshoot (%) | {< 10%} | {value} | {value} | {Y/N} |
| Settling Time (s) | {< 60 s} | {value} | {value} | {Y/N} |
| Rise Time (s) | {< 20 s} | {value} | {value} | {Y/N} |
| Steady-State Error | {< 1% of range} | {value} | {value} | {Y/N} |
| Oscillation | {None sustained} | {describe} | {describe} | {Y/N} |
| Disturbance Rejection | {Return to SP within 30 s} | {value} | {value} | {Y/N} |

## 5. Test Conditions

| Test # | Test Type | SP Change / Disturbance | Load Condition | Date | Time |
|---|---|---|---|---|---|
| 1 | {SP step +10%} | {50% -> 60%} | {75% load} | {YYYY-MM-DD} | {HH:MM} |
| 2 | {SP step -10%} | {60% -> 50%} | {75% load} | {YYYY-MM-DD} | {HH:MM} |
| 3 | {Disturbance} | {Upstream pressure drop 5%} | {100% load} | {YYYY-MM-DD} | {HH:MM} |

## 6. Trend Capture Reference

{Attach or reference trend screenshots/files showing PV, SP, and CO for each test.}

- Test 1 trend: {file reference or embedded}
- Test 2 trend: {file reference or embedded}
- Test 3 trend: {file reference or embedded}

## 7. Notes

- {Any special operating modes: cascade, ratio, feedforward}
- {Interaction with other loops}
- {Conditions where manual mode is preferred}
- {Re-tuning triggers: process change, equipment modification, seasonal variation}

## 8. Sign-off

| Role | Name | Date |
|---|---|---|
| Control Engineer | {name} | {date} |
| Process Engineer | {name} | {date} |
| Operations | {name} | {date} |
