# Design Review Checklist

**Project:** {project_name}
**System / Deliverable:** {system_name}
**Review Type:** {Conceptual / Preliminary / Detailed / Final}
**Reviewer:** {reviewer_name} | **Date:** {date}

## Review Summary

| Metric | Count |
|---|---|
| Total Items | {n} |
| Pass | {n} |
| Fail | {n} |
| N/A | {n} |
| Actions Required | {n} |

## Checklist

### Architecture

| Item | Review Question | Status | Finding | Severity | Action Required | Owner |
|---|---|---|---|---|---|---|
| ARCH-01 | System architecture diagram current and approved? | {Pass/Fail/N-A} | {finding or "OK"} | {Critical/Major/Minor} | {action} | {owner} |
| ARCH-02 | Redundancy design meets availability requirements? | | | | | |
| ARCH-03 | Scalability provisions adequate for future expansion? | | | | | |
| ARCH-04 | Single points of failure identified and mitigated? | | | | | |
| ARCH-05 | Technology selection justified and supportable? | | | | | |

### Security

| Item | Review Question | Status | Finding | Severity | Action Required | Owner |
|---|---|---|---|---|---|---|
| SEC-01 | Network segmentation per IEC 62443 zone model? | | | | | |
| SEC-02 | Authentication and access control defined for all roles? | | | | | |
| SEC-03 | Remote access design reviewed and approved? | | | | | |
| SEC-04 | Audit logging requirements addressed? | | | | | |
| SEC-05 | Patch management strategy documented? | | | | | |

### Standards Compliance

| Item | Review Question | Status | Finding | Severity | Action Required | Owner |
|---|---|---|---|---|---|---|
| STD-01 | Applicable standards identified and listed? | | | | | |
| STD-02 | Design compliant with referenced IEC/IEEE/local standards? | | | | | |
| STD-03 | Hazardous area classification applied correctly? | | | | | |
| STD-04 | SIL requirements addressed per IEC 61511? | | | | | |
| STD-05 | Electrical design per local wiring code? | | | | | |

### Documentation

| Item | Review Question | Status | Finding | Severity | Action Required | Owner |
|---|---|---|---|---|---|---|
| DOC-01 | Document numbering follows project convention? | | | | | |
| DOC-02 | Revision history complete and accurate? | | | | | |
| DOC-03 | Cross-references valid (no broken links)? | | | | | |
| DOC-04 | All TBD/TBC items resolved for this review stage? | | | | | |
| DOC-05 | Deliverable list complete per contract requirements? | | | | | |

## Severity Definitions

| Severity | Definition |
|---|---|
| Critical | Must resolve before proceeding — safety, regulatory, or fundamental design flaw |
| Major | Significant issue that must resolve before next project gate |
| Minor | Improvement needed but does not block progress |

## Sign-off

| Role | Name | Disposition | Signature | Date |
|---|---|---|---|---|
| Lead Reviewer | {name} | {Approved / Approved with comments / Not approved} | | |
| Design Engineer | {name} | {Acknowledged} | | |
| Project Manager | {name} | {Acknowledged} | | |
