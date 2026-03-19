# Dashboard Design Specification

**Project:** {project_name}
**Dashboard Name:** {dashboard_name}
**Document No:** {doc_number} | **Revision:** {revision}
**Prepared By:** {author} | **Date:** {date}

## 1. Dashboard Overview

| Item | Detail |
|---|---|
| Dashboard Name | {dashboard_name} |
| Purpose | {brief description of what decisions this dashboard supports} |
| Target Audience | {Operations Manager / Control Room Operator / Maintenance Lead / Executive} |
| Access Level | {Role-based: who can view, who can configure} |
| Platform | {Grafana / Power BI / SCADA built-in / Custom web} |

## 2. Key Performance Indicators (KPIs)

| KPI ID | KPI Name | Definition | Unit | Target | Warning Threshold | Critical Threshold |
|---|---|---|---|---|---|---|
| KPI-001 | {Overall Equipment Effectiveness} | {Availability x Performance x Quality} | {% } | {> 85%} | {< 80%} | {< 70%} |
| KPI-002 | {Energy Consumption Rate} | {kWh per unit produced} | {kWh/unit} | {< n} | {> n} | {> n} |
| KPI-003 | {Mean Time Between Failures} | {Total operating hours / number of failures} | {hours} | {> n} | {< n} | {< n} |
| KPI-004 | {Alarm Rate} | {Alarms per operator per hour} | {alarms/hr} | {< 6} | {> 10} | {> 20} |
| KPI-005 | {description} | {formula} | {unit} | {target} | {warning} | {critical} |

## 3. Data Sources

| Source ID | System | Data Type | Connection Method | Refresh Capability |
|---|---|---|---|---|
| DS-001 | {Process Historian} | {Time-series process data} | {OPC HDA / SQL / REST API} | {Real-time / 1s minimum} |
| DS-002 | {SCADA} | {Alarm and event logs} | {Database query / OPC A&E} | {Near real-time} |
| DS-003 | {CMMS} | {Work orders, asset data} | {REST API / ODBC} | {Hourly batch} |
| DS-004 | {ERP} | {Production orders, inventory} | {API / File export} | {Daily batch} |

## 4. Refresh Rate

| View | Refresh Interval | Justification |
|---|---|---|
| Real-time overview | {5 seconds} | {Operator situational awareness} |
| Trend charts | {30 seconds} | {Performance monitoring} |
| KPI summary | {5 minutes} | {Management review} |
| Historical reports | {On-demand} | {Analysis and reporting} |

## 5. Layout Wireframe

```
+-----------------------------------------------+
|  Header: {Dashboard Name}  |  Filters: Date Range | Area | Unit  |
+-------------------+---------------------------+
|  KPI Cards        |  Main Trend Chart          |
|  [KPI-001: OEE]   |  {Primary process variable |
|  [KPI-002: Energy] |   with setpoint overlay}   |
|  [KPI-003: MTBF]  |                           |
|  [KPI-004: Alarms] |                           |
+-------------------+---------------------------+
|  Bar Chart: Production by Unit  |  Alarm Summary Table  |
|  {Stacked bars, color by status} |  {Top 10 most frequent} |
+--------------------------------+---------------------+
|  Footer: Last Updated: {timestamp}  |  Data Source Status  |
+-----------------------------------------------+
```

## 6. Drill-down Logic

| From (Parent View) | Click Target | Navigates To | Filter Applied |
|---|---|---|---|
| KPI Card — OEE | OEE value | OEE Breakdown (Availability, Performance, Quality) | Current time range |
| Main Trend Chart | Data point | Detailed trend with raw data overlay | +/- 1 hour around point |
| Alarm Summary | Alarm row | Alarm detail view with event history | Selected alarm tag |
| Production Bar Chart | Bar segment | Unit-level production detail | Selected unit |

## 7. Alert Thresholds

| Alert ID | KPI / Signal | Condition | Severity | Notification Method | Recipients |
|---|---|---|---|---|---|
| ALT-001 | {KPI-001 OEE} | {< 70% for > 15 min} | {Critical} | {Email + SMS} | {Operations Manager} |
| ALT-002 | {KPI-004 Alarm Rate} | {> 20/hr for > 30 min} | {Warning} | {Email} | {Control Room Supervisor} |
| ALT-003 | {Data source offline} | {No data for > 5 min} | {Critical} | {Dashboard banner + Email} | {IT/OT Support} |

## 8. Design Guidelines

- Use consistent color scheme: Green (normal), Yellow (warning), Red (critical), Grey (no data)
- Minimize visual clutter — maximum 6-8 visual elements per screen
- Ensure readability at control room viewing distance (minimum 14pt font for key values)
- All timestamps displayed in site local time with timezone label
- Provide export capability (CSV/PDF) for all tabular data

## 9. Revision History

| Rev | Date | Author | Description |
|---|---|---|---|
| 0 | {date} | {author} | Initial specification |
