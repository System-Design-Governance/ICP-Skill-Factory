# Panel Thermal Calculation Worksheet

**Project:** {Project Name}
**Panel ID:** {e.g., MCC-01 / CP-03 / RIO-Panel-A}
**Author:** {Author}
**Date:** {YYYY-MM-DD}
**Revision:** {Rev}
**Standard:** IEC 62208 / NEMA 250 / IEC 61439

## 1. Enclosure Data

| Parameter | Value | Units |
|---|---|---|
| Enclosure Type | {e.g., floor-standing / wall-mount / 19-inch rack} | |
| Protection Rating | {IP55 / NEMA 4X / IP65} | |
| Material | {Mild steel / Stainless 316 / GRP} | |
| External Dimensions (H x W x D) | {mm x mm x mm} | mm |
| Internal Volume | {liters} | L |
| Effective Surface Area (Ae) | {m2} | m2 |
| Surface Treatment | {painted RAL 7035 / polished SS} | |
| Installation Location | {Indoor / Outdoor / Sheltered} | |

## 2. Ambient Conditions

| Parameter | Value | Units |
|---|---|---|
| Max Ambient Temperature | {deg C} | deg C |
| Min Ambient Temperature | {deg C} | deg C |
| Design Ambient (worst case) | {deg C} | deg C |
| Solar Load (outdoor only) | {W/m2, typically 1000 W/m2 max} | W/m2 |
| Altitude | {m above sea level} | m |
| Derate Required (> 1000 m)? | {Yes / No, factor} | |

## 3. Heat Dissipation Inventory

| # | Component | Model / Rating | Power Dissipation (W) | Qty | Total Heat (W) | Source |
|---|---|---|---|---|---|---|
| 1 | {PLC CPU} | {Siemens 6ES7 515-2AM02} | {8} | {1} | {8} | {Datasheet} |
| 2 | {PLC I/O Module} | {DI 32ch} | {5} | {4} | {20} | {Datasheet} |
| 3 | {PLC I/O Module} | {AI 8ch} | {7} | {2} | {14} | {Datasheet} |
| 4 | {Power Supply} | {24VDC 20A} | {60} | {1} | {60} | {Datasheet (input W - output W)} |
| 5 | {Network Switch} | {Scalance XC208} | {12} | {1} | {12} | {Datasheet} |
| 6 | {Terminal Blocks} | {various} | {2} | {1 set} | {2} | {Estimate} |
| 7 | {Circuit Breakers} | {MCB 10A} | {3} | {6} | {18} | {Datasheet at rated current} |
| 8 | {Contactor} | {9A AC3} | {5} | {4} | {20} | {Datasheet coil + contacts} |
| 9 | {VFD} | {7.5 kW} | {300} | {1} | {300} | {Datasheet (typ 3-4% of rating)} |
| 10 | {Lighting + Heater} | {LED + anti-condensation} | {30} | {1} | {30} | {Specification} |
| | **TOTAL INTERNAL HEAT LOAD (Qi)** | | | | **{484}** | |

## 4. External Heat Gain (if applicable)

| Source | Heat Gain (W) | Notes |
|---|---|---|
| Solar radiation | {Ae_sun x solar load x absorption coeff} | {Outdoor panels only} |
| Adjacent hot surfaces | {value} | {e.g., next to boiler, transformer} |
| **Total External Heat Gain (Qe)** | **{value}** | |

**Total Heat Load (Qt) = Qi + Qe = {value} W**

## 5. Thermal Calculation

### 5.1 Natural Convection (sealed enclosure)

| Parameter | Formula | Value |
|---|---|---|
| Max allowable internal temp | {e.g., 55 deg C for electronics} | {deg C} |
| Temperature rise allowed (dT) | {T_internal_max - T_ambient_max} | {deg C} |
| Heat dissipation by convection | {Ae x k x dT} (k = 5.5 W/m2/K typical) | {W} |
| Sufficient without cooling? | {convection capacity > Qt ?} | {Yes / No} |

### 5.2 Required Cooling

| Parameter | Value |
|---|---|
| Cooling deficit | {Qt - natural dissipation capacity} W |
| Required cooling capacity | {deficit x 1.25 safety factor} W |
| Selected cooling method | {Fan + filter / Air-to-air heat exchanger / AC unit / Vortex cooler} |
| Selected unit model | {manufacturer, model} |
| Unit cooling capacity | {W at design dT} |
| Airflow | {m3/h} |
| Power consumption | {W} |
| Filter maintenance interval | {months} |

## 6. Temperature Budget Summary

| Location | Max Temperature | Limit | Status |
|---|---|---|---|
| Top of enclosure (hottest) | {deg C} | {55 deg C} | {OK / Exceeds} |
| PLC CPU area | {deg C} | {60 deg C per spec} | {OK / Exceeds} |
| VFD area | {deg C} | {50 deg C per spec} | {OK / Exceeds} |
| Bottom of enclosure (coolest) | {deg C} | {--} | {Reference} |

## 7. Design Notes

- {Component layout: heat-generating components (VFDs, power supplies) mounted at top with dedicated exhaust}
- {Internal airflow: maintain separation between power and control sections}
- {Anti-condensation heater: enable when internal temp approaches dew point}
- {Cable entry: sealed glands to maintain IP rating when cooling is external}
- {Derating: if altitude > 1000m, derate cooling capacity by {X}% per 1000m}

## 8. References

- IEC 62208: Empty enclosures -- heating and cooling
- IEC 61439-1: Low-voltage switchgear assemblies (temperature rise limits)
- Component datasheets: {list references}
