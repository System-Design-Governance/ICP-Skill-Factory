# Alarm Rationalization Worksheet

**Project:** {Project Name}
**System / Area:** {e.g., Unit 1 Boiler / Water Treatment / Substation A}
**Author:** {Author}
**Date:** {YYYY-MM-DD}
**Revision:** {Rev}
**Standard:** ISA-18.2 / IEC 62682

## 1. Purpose

Document the alarm rationalization process for {system/area}, ensuring each alarm
is justified, properly prioritized, and has a defined operator response per
ISA-18.2 requirements.

## 2. Priority Definitions (per ISA-18.2)

| Priority | Response Time | Consequence if Missed | Example |
|---|---|---|---|
| Critical | Immediate (< 5 min) | Safety incident, environmental release, major equipment damage | Gas leak, overpressure |
| High | < 15 min | Significant production loss, equipment damage | Pump cavitation, high temperature |
| Medium | < 30 min | Minor production impact, abnormal condition | Filter differential pressure high |
| Low | < 60 min | Informational, maintenance trigger | Runtime counter, minor deviation |

## 3. Alarm Rationalization Register

| # | Tag | Description | Current Priority | Proposed Priority | Cause | Consequence if Not Addressed | Operator Response | Required Response Time | ISA-18.2 Category | Disposition |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | {TT-101-HH} | {Bearing Temp Very High} | {High} | {Critical} | {Lubrication failure, overload} | {Bearing seizure, shaft damage} | {Trip unit, notify maintenance} | {Immediate} | {Safety} | {Keep, re-prioritize} |
| 2 | {PT-201-H} | {Discharge Press High} | {High} | {Medium} | {Downstream valve closed, process upset} | {Relief valve lift, production loss} | {Check downstream valves, reduce speed} | {15 min} | {Equipment} | {Keep} |
| 3 | {LT-301-L} | {Tank Level Low} | {Medium} | {Medium} | {Inlet valve closed, supply interruption} | {Pump dry run} | {Open inlet valve, check supply} | {30 min} | {Equipment} | {Keep} |
| 4 | {FT-401-H} | {Flow High} | {High} | {Low} | {Valve malfunction} | {Minor overflow to drain} | {Verify valve position, adjust setpoint} | {60 min} | {Efficiency} | {Downgrade} |
| 5 | {XS-501} | {Valve Limit Switch} | {Medium} | {--} | {Nuisance alarm during normal cycling} | {None} | {None required} | {--} | {--} | {Remove} |
| 6 | {TS-601-HH} | {Ambient Temp High} | {Low} | {--} | {Weather, HVAC failure} | {Equipment derate} | {No direct action possible} | {--} | {--} | {Convert to event/journal} |

## 4. Alarm Performance Metrics (Current State)

| Metric | Current Value | ISA-18.2 Target | Status |
|---|---|---|---|
| Alarms per 10 min (avg) | {value} | {< 1 per 10 min} | {OK / Exceeds} |
| Alarms per 10 min (peak) | {value} | {< 10 per 10 min} | {OK / Exceeds} |
| % Chattering alarms | {value} | {< 1%} | {OK / Exceeds} |
| % Stale alarms (standing > 24 hr) | {value} | {< 5%} | {OK / Exceeds} |
| % Priority Critical | {value} | {< 5% of total} | {OK / Exceeds} |
| % Priority High | {value} | {< 15% of total} | {OK / Exceeds} |
| % Priority Medium | {value} | {< 30% of total} | {OK / Exceeds} |
| % Priority Low | {value} | {remaining} | |

## 5. Alarm Suppression / Shelving Rules

| Condition | Suppression Type | Duration | Authorization |
|---|---|---|---|
| {Equipment out of service} | {State-based suppression} | {Until return to service} | {Shift supervisor} |
| {Maintenance activity} | {Operator shelve} | {Max 8 hours, auto-return} | {Operator L2} |
| {Startup / Shutdown} | {State-based suppression} | {Per mode transition} | {Automatic} |

## 6. Action Items

| # | Action | Responsible | Due Date | Status |
|---|---|---|---|---|
| 1 | {Remove nuisance alarm XS-501 from alarm system} | {control engineer} | {date} | {Pending} |
| 2 | {Re-prioritize TT-101-HH to Critical} | {control engineer} | {date} | {Pending} |
| 3 | {Add deadband to FT-401-H to reduce chattering} | {control engineer} | {date} | {Pending} |
| 4 | {Convert TS-601-HH to journal event} | {control engineer} | {date} | {Pending} |

## 7. References

- ISA-18.2-2016: Management of Alarm Systems for the Process Industries
- IEC 62682: Management of alarm systems for the process industries
- {Site alarm philosophy document reference}
