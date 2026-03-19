# Data Governance Policy

**Organization:** {organization_name}
**Policy No:** {policy_number} | **Version:** {version}
**Effective Date:** {date}
**Owner:** {data_governance_owner}
**Approved By:** {approver}

## 1. Purpose

Establish standards for data classification, ownership, quality, retention, access control, and auditing across OT and IT systems to ensure data integrity, security, and regulatory compliance.

## 2. Scope

This policy applies to all operational and engineering data generated, collected, stored, or transmitted by {organization_name} control systems, historians, and associated infrastructure.

## 3. Data Classification

| Classification | Definition | Examples | Handling Requirements |
|---|---|---|---|
| Critical | Loss or corruption causes safety risk or regulatory violation | SIS logic, protection settings, safety records | Encrypted storage, dual backup, restricted access |
| Confidential | Business-sensitive, competitive impact if disclosed | Engineering designs, vendor contracts, cost data | Access on need-to-know, encrypted in transit |
| Internal | Operational data for internal use | Process data, historian tags, maintenance logs | Standard access controls, regular backup |
| Public | No sensitivity, may be shared externally | Published specs, marketing materials | No restrictions |

## 4. Data Ownership

| Role | Responsibilities |
|---|---|
| Data Owner | Accountable for data classification, quality, and lifecycle decisions. Typically the engineering or operations manager for the relevant system. |
| Data Steward | Day-to-day management of data quality, metadata, and access requests. Typically a senior engineer or data analyst. |
| Data Custodian | Technical implementation of storage, backup, and security controls. Typically IT/OT infrastructure team. |
| Data Consumer | Uses data per classification rules. Reports quality issues to Data Steward. |

### Ownership Register

| Data Domain | Data Owner | Data Steward | System of Record |
|---|---|---|---|
| {Process control data} | {name/role} | {name/role} | {historian/DCS} |
| {Safety system records} | {name/role} | {name/role} | {SIS engineering tool} |
| {Maintenance records} | {name/role} | {name/role} | {CMMS} |

## 5. Data Quality Standards

| Dimension | Standard | Measurement |
|---|---|---|
| Accuracy | Data reflects the real-world value within instrument tolerance | Calibration records, cross-checks |
| Completeness | No gaps in time-series data > {n} seconds without documented reason | Historian gap reports |
| Timeliness | Data available within {n} seconds of generation | End-to-end latency monitoring |
| Consistency | Same data produces same result across all consuming systems | Cross-system reconciliation |
| Validity | Data conforms to defined format, range, and engineering units | Input validation, range checks |

## 6. Retention Policy

| Data Type | Retention Period | Storage Tier | Disposal Method |
|---|---|---|---|
| Safety records (SIS proof tests, trip reports) | Plant lifetime + 5 years | Archive (immutable) | Approved destruction per regulatory body |
| Process historian data | {10} years | Online 2 years, then archive | Secure deletion |
| Event / alarm logs | {5} years | Online 1 year, then archive | Secure deletion |
| Engineering configuration backups | Current + 2 prior versions | Online | Overwrite on new version |
| Project documentation | {10} years post-project close | Archive | Review and extend or destroy |

## 7. Access Control

| Principle | Implementation |
|---|---|
| Least privilege | Users granted minimum access required for their role |
| Role-based access (RBAC) | Access defined by role, not individual — see role matrix |
| Separation of duties | No single person can modify and approve safety-critical data |
| Multi-factor authentication | Required for remote access and safety-critical systems |
| Access review | Quarterly review of access rights; revoke within 24h of role change |

## 8. Audit Requirements

| Audit Type | Frequency | Scope | Responsible |
|---|---|---|---|
| Access log review | Monthly | Review login events, failed attempts, privilege changes | Data Custodian |
| Data quality audit | Quarterly | Sample historian data for completeness and accuracy | Data Steward |
| Classification review | Annually | Verify data classification remains appropriate | Data Owner |
| Policy compliance audit | Annually | Full policy compliance assessment | Internal Audit / Governance |
| Regulatory audit | Per regulatory schedule | As defined by applicable regulation | Compliance team |

## 9. Revision History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | {date} | {author} | Initial release |
