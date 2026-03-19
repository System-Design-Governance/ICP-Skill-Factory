# Contract Technical Scope Summary

**Project:** {project_name}
**Contract No:** {contract_number}
**Revision:** {revision} | **Date:** {date}
**Prepared By:** {author}
**Approved By:** {approver}

## Purpose

Summarize the technical scope of work into structured work packages with deliverables, acceptance criteria, and responsibilities for clear project execution and tracking.

## Project Overview

| Field | Detail |
|---|---|
| Client | {client_name} |
| Site / Location | {site_location} |
| Contract Type | {Lump Sum / T&M / Cost Plus / Unit Rate} |
| Contract Duration | {start_date} to {end_date} |
| Key Standards | {IEC 61131, IEC 62443, local codes} |

## Work Package Summary

| WP No | Work Package | Description | Deliverables | Acceptance Criteria | Timeline | Dependencies | Responsible Party | Status |
|---|---|---|---|---|---|---|---|---|
| WP-01 | {Engineering Design} | {Detailed design for control system} | {SDD, I/O List, Network Diagrams, ICD} | {Client review and approval, compliance matrix complete} | {start - end date} | {None / WP-xx} | {Contractor / Client / Vendor} | {Not Started / In Progress / Complete} |
| WP-02 | {Hardware Procurement} | {Procure control system hardware} | {Equipment, shipping docs, certificates} | {Delivery inspection passed, quantities match PO} | {dates} | {WP-01} | | |
| WP-03 | {Software Development} | {Application software and HMI} | {Software package, test report} | {FAT passed per approved test plan} | {dates} | {WP-01} | | |
| WP-04 | {Factory Acceptance Test} | {System FAT at vendor facility} | {FAT report, punch list} | {All critical tests pass, punch list agreed} | {dates} | {WP-02, WP-03} | | |
| WP-05 | {Installation} | {On-site installation and cabling} | {As-built drawings, installation report} | {Installation inspection passed} | {dates} | {WP-04} | | |
| WP-06 | {Commissioning & SAT} | {Site commissioning and SAT} | {SAT report, defect log, handover package} | {SAT passed, system accepted for operation} | {dates} | {WP-05} | | |
| WP-07 | {Training} | {Operator and maintenance training} | {Training materials, attendance records} | {Training evaluation score >= 80%} | {dates} | {WP-03} | | |
| WP-08 | {Documentation} | {As-built documentation package} | {O&M Manual, as-built drawings, config backups} | {Document transmittal accepted by client} | {dates} | {WP-06} | | |

## Exclusions

| Item | Reason |
|---|---|
| {Civil works / building modifications} | {By client / separate contractor} |
| {Third-party system modifications} | {Out of scope per contract clause {n}} |
| {description} | {reason} |

## Assumptions

- {Client provides site access and power by {date}}
- {Existing network infrastructure is functional and available}
- {Third-party system interfaces documented and frozen by {date}}

## Key Milestones

| Milestone | Target Date | Contractual Obligation | Status |
|---|---|---|---|
| Design Approval (Gate 2) | {date} | {Yes / No} | |
| FAT Complete | {date} | {Yes} | |
| Delivery to Site | {date} | {Yes} | |
| SAT Complete / Handover | {date} | {Yes} | |
| Warranty End | {date} | {Yes} | |

## Revision History

| Rev | Date | Author | Description |
|---|---|---|---|
| 0 | {date} | {author} | Initial issue |
