# System Decommissioning Checklist

**Project:** {project_name}
**System:** {system_name}
**Asset ID:** {asset_id}
**Decommissioning Date:** {date}
**Prepared By:** {author}
**Approved By:** {approver}

## 1. Pre-decommissioning

| No | Check Item | Responsible | Status | Date | Notes |
|---|---|---|---|---|---|
| 1.1 | Decommissioning plan approved | {project_manager} | {Done / Pending} | | |
| 1.2 | Replacement system operational and accepted | {engineer} | | | |
| 1.3 | Stakeholders notified (operations, maintenance, IT, security) | {coordinator} | | | |
| 1.4 | Regulatory notifications filed (if required) | {compliance} | | | |
| 1.5 | Contracts/licenses reviewed for termination requirements | {procurement} | | | |

## 2. Data Backup

| No | Data Category | Backup Required (Y/N) | Backup Method | Backup Location | Verified By | Date |
|---|---|---|---|---|---|---|
| 2.1 | Configuration files | {Y/N} | {Export / Image / Manual copy} | {server path / media label} | {verifier} | |
| 2.2 | Historical process data | {Y/N} | {Database export / Historian archive} | {location} | | |
| 2.3 | Event and alarm logs | {Y/N} | {Log export} | {location} | | |
| 2.4 | User accounts and permissions | {Y/N} | {Export} | {location} | | |
| 2.5 | Application software / source code | {Y/N} | {Repository archive / Media copy} | {location} | | |
| 2.6 | Licenses and activation keys | {Y/N} | {Document / Screenshot} | {location} | | |
| 2.7 | Engineering documentation (as-built) | {Y/N} | {PDF archive} | {location} | | |

## 3. Media Sanitization

| No | Media Type | Serial / ID | Sanitization Method | Standard Reference | Performed By | Date | Verified By |
|---|---|---|---|---|---|---|---|
| 3.1 | {Hard disk drive} | {serial} | {Overwrite / Degauss / Physical destruction} | {NIST SP 800-88} | {person} | | {verifier} |
| 3.2 | {SSD / Flash} | {serial} | {Crypto erase / Physical destruction} | {NIST SP 800-88} | | | |
| 3.3 | {Removable media (USB, CF card)} | {id} | {Overwrite / Physical destruction} | {NIST SP 800-88} | | | |
| 3.4 | {Backup tapes} | {id} | {Degauss / Physical destruction} | {NIST SP 800-88} | | | |
| 3.5 | {PLC / Controller memory} | {tag/serial} | {Factory reset / Memory clear} | {Vendor procedure} | | | |

## 4. Physical Disposal

| No | Item | Asset Tag | Disposal Method | Disposal Vendor | Tracking No | Date |
|---|---|---|---|---|---|---|
| 4.1 | {Control panel / Cabinet} | {asset_tag} | {Return to vendor / Recycle / Scrap / Reuse} | {vendor_name} | {tracking} | |
| 4.2 | {Network equipment} | {asset_tag} | | | | |
| 4.3 | {Workstations / Servers} | {asset_tag} | | | | |
| 4.4 | {Cables and wiring} | N/A | {Recycle / Scrap} | | | |
| 4.5 | {UPS / Batteries} | {asset_tag} | {Hazmat recycling} | | | |

## 5. Environmental Compliance

| No | Check Item | Applicable (Y/N) | Regulation | Compliance Evidence | Status |
|---|---|---|---|---|---|
| 5.1 | Hazardous material identification (batteries, CRTs, mercury) | {Y/N} | {local regulation ref} | {manifest / certificate} | |
| 5.2 | WEEE / e-waste disposal compliance | {Y/N} | {EU WEEE / local equivalent} | {recycler certificate} | |
| 5.3 | Refrigerant recovery (if HVAC involved) | {Y/N} | {regulation ref} | {recovery certificate} | |
| 5.4 | Oil / fluid disposal (transformers, hydraulics) | {Y/N} | {regulation ref} | {disposal manifest} | |

## 6. Certificate of Destruction

| Field | Detail |
|---|---|
| System / Asset | {system_name / asset_id} |
| Destruction Method | {method_summary} |
| Destruction Date | {date} |
| Destruction Vendor | {vendor_name, contact} |
| Certificate Number | {cert_number} |
| Witness | {witness_name} |

## 7. Regulatory Filing

| No | Filing Requirement | Authority | Due Date | Filed By | Confirmation | Status |
|---|---|---|---|---|---|---|
| 7.1 | {Asset disposal notification} | {regulatory_body} | {date} | {person} | {ref number} | {Complete / Pending} |
| 7.2 | {Environmental report} | {EPA / local authority} | {date} | | | |
| 7.3 | {License deactivation} | {vendor / authority} | {date} | | | |

## 8. Sign-off

| Role | Name | Signature | Date |
|---|---|---|---|
| Decommissioning Lead | {name} | | |
| IT/OT Security | {name} | | |
| Environmental / HSE | {name} | | |
| Asset Manager | {name} | | |
