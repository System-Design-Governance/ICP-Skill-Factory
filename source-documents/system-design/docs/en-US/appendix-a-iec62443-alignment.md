```{=latex}
\newpage
\begin{landscape}
\pagestyle{landscapepage}
\enableLandscapeHeaderFooter
```

# Appendix A: IEC 62443 Alignment

> **IMPORTANT NOTICE**: This English version is provided for reference and external review only. The official governance of record is the zh-TW (Traditional Chinese) version. In case of any discrepancy, the zh-TW version shall prevail.

---

## Purpose and Scope {#appA-purpose}

This appendix provides the alignment mapping between the System Design Governance main document and the IEC 62443 standard series, serving as the basis for verifying compliance during Gate reviews. This appendix provides implementation details and does not introduce new governance processes or roles; all mandatory requirements are defined in the main document.

---

## How to Use This Appendix During Gate Reviews {#appA-usage}

- **Gate 0**: Use the "SL Decision Record Template" to document the target SL proposal and underlying assumptions
- **Gate 1**: Use the "Primary Mapping Table" SR checklist to verify that the design covers the necessary security requirements for the target SL; use the "Gate 1 Compliance Checklist" to confirm all required deliverables
- **Gate 2**: When design changes affect Zone/Conduit or SL levels, re-review the affected SR items in the "Primary Mapping Table"; use the "Gate 2 Compliance Checklist"
- **Gate 3**: Use the "Primary Mapping Table" to verify that residual risks are mapped to relevant SRs; use the "Gate 3 Compliance Checklist" to confirm compliance delivery completeness
- **Audit Preparation**: The "Secondary Mapping" provides evidence mapping for IEC 62443-2-4 (procedural requirements) and IEC 62443-3-2 (risk assessment) for quick audit indexing
- **SL Change Management**: Any SL level adjustment shall update the "SL Decision Record Template" and follow the approval process defined in the main document

---

## IEC 62443 Reference Model Summary {#appA-reference-model}

The IEC 62443 standard series structure is as follows; this governance framework primarily aligns with 2-4, 3-2, and 3-3:

| Standard Number | Standard Name | Relationship to This Governance Framework |
|-----------------|---------------|-------------------------------------------|
| IEC 62443-1-1 | Concepts and Models | Terminology definition reference |
| IEC 62443-2-4 | Security Program Requirements for IACS Service Providers | Procedural and process requirements, aligning with Gate mechanism and document management |
| IEC 62443-3-2 | Security Risk Assessment for System Design | Risk assessment methodology, aligning with Section 3.2 Integrated Risk Assessment in the main document |
| IEC 62443-3-3 | System Security Requirements and Security Levels | System security requirements, aligning with design baseline and SR checklist |
| IEC 62443-4-2 | Technical Security Requirements for IACS Components | Component security requirements, component supplier responsibility, referenced in procurement specifications by this framework |

**Security Level (SL) Definitions**:
- **SL 1**: Protection against casual or coincidental violation
- **SL 2**: Protection against intentional violation using simple means
- **SL 3**: Protection against intentional violation using sophisticated means
- **SL 4**: Protection against intentional violation using sophisticated means with extensive resources

**Important Note**: Target SL is project-specific, proposed at Gate 0 and confirmed at Gate 1; this framework does not prescribe a specific SL level.

---

## Primary Mapping Table: IEC 62443-3-3 Foundational Requirements {#appA-primary-mapping}

### Coverage Rule {#appA-coverage-rule}

All IEC 62443-3-3 System Requirements (SR) shall be covered in the project-specific SR checklist. This section provides a normative template and mapping methodology; projects shall complete the actual mapping status according to the target SL level.

**Status Definitions**:
| Status | Definition | Evidence Requirements |
|--------|------------|----------------------|
| Implemented | Design includes corresponding control measures | Design documentation clearly describes control measures, traceable to SR |
| Planned | Design will include but not yet completed | Acceptable for Gate 1 Lite; shall be upgraded to Implemented before Gate 3 |
| N/A | Assessed as not applicable to this project | Shall document justification and obtain Approver sign-off |

### FR-SR Mapping Template {#appA-fr-sr-mapping}

The following is the SR mapping template for the seven Foundational Requirements (FR) of IEC 62443-3-3. Projects shall copy this template and complete the actual status.

#### FR1: Identification and Authentication Control (IAC)

| SR ID | SR Description | Governance Control Point | Expected Evidence | Gate 1 Lite Minimum Requirement | Gate 3 Complete Requirement | Status |
|-------|----------------|--------------------------|-------------------|--------------------------------|----------------------------|--------|
| SR 1.1 | Human User Identification and Authentication | Gate 1: Design Baseline Document | Authentication mechanism design specification | Identify authentication requirements | Complete authentication design and test plan | |
| SR 1.2 | Software Process and Device Identification | Gate 1: Design Baseline Document | Software/device identification mechanism | Identify software and devices requiring identification | Complete identification mechanism design | |
| SR 1.3 | Account Management | Gate 1: Design Baseline Document | Account management process design | Account lifecycle definition | Complete account management design | |
| SR 1.4 | Identifier Management | Gate 1: Design Baseline Document | Identifier management rules | Identifier naming conventions | Complete identifier management design | |
| SR 1.5 | Authenticator Management | Gate 1: Design Baseline Document | Authenticator management mechanism | Password/credential policy | Complete authenticator management design | |
| SR 1.6 | Wireless Access Management | Gate 1: Design Baseline Document | Wireless access control design | Identify wireless access points | Complete wireless security design (if applicable) | |
| SR 1.7 | Strength of Password-based Authentication | Gate 1: Design Baseline Document | Password strength rules | Password policy definition | Password strength implementation verification | |
| SR 1.8 | PKI Certificates | Gate 1: Design Baseline Document | PKI design document | PKI requirement identification | Complete PKI design (if applicable) | |
| SR 1.9 | Strength of Public Key Authentication | Gate 1: Design Baseline Document | Public key authentication design | Public key authentication requirements | Public key strength verification | |
| SR 1.10 | Authenticator Feedback | Gate 1: Design Baseline Document | Authentication feedback design | UI authentication feedback requirements | Authentication feedback implementation | |
| SR 1.11 | Unsuccessful Login Attempts | Gate 1: Design Baseline Document | Failed login handling | Failed login handling policy | Failed login handling implementation | |
| SR 1.12 | System Use Notification | Gate 1: Design Baseline Document | System use notification | Notification requirement definition | Notification implementation | |
| SR 1.13 | Access via Untrusted Networks | Gate 1: Zone & Conduit Diagram | Untrusted network access control | Zone boundary identification | Complete boundary control design | |

#### FR2: Use Control (UC)

| SR ID | SR Description | Governance Control Point | Expected Evidence | Gate 1 Lite Minimum Requirement | Gate 3 Complete Requirement | Status |
|-------|----------------|--------------------------|-------------------|--------------------------------|----------------------------|--------|
| SR 2.1 | Authorization Enforcement | Gate 1: Design Baseline Document | Authorization mechanism design | Authorization model definition | Complete authorization implementation design | |
| SR 2.2 | Wireless Use Control | Gate 1: Design Baseline Document | Wireless use control | Wireless use policy | Wireless control implementation (if applicable) | |
| SR 2.3 | Use Control for Portable/Mobile Devices | Gate 1: Design Baseline Document | Mobile device control | Mobile device policy | Mobile device control implementation | |
| SR 2.4 | Mobile Code | Gate 1: Design Baseline Document | Mobile code control | Mobile code policy | Mobile code control implementation | |
| SR 2.5 | Session Lock | Gate 1: Design Baseline Document | Session lock | Lock policy definition | Lock mechanism implementation | |
| SR 2.6 | Remote Session Termination | Gate 1: Design Baseline Document | Remote session termination | Termination policy definition | Termination mechanism implementation | |
| SR 2.7 | Concurrent Session Control | Gate 1: Design Baseline Document | Concurrent session control | Concurrent session policy definition | Concurrent session control implementation | |
| SR 2.8 | Auditable Events | Gate 1: Design Baseline Document | Auditable event definition | Audit event list | Complete audit design | |
| SR 2.9 | Audit Storage Capacity | Gate 1: Design Baseline Document | Audit storage capacity | Storage requirement assessment | Storage design and protection | |
| SR 2.10 | Response to Audit Processing Failures | Gate 1: Design Baseline Document | Audit failure response | Failure handling policy | Failure handling implementation | |
| SR 2.11 | Timestamps | Gate 1: Design Baseline Document | Timestamp mechanism | Time synchronization requirements | Timestamp implementation | |
| SR 2.12 | Non-repudiation | Gate 1: Design Baseline Document | Non-repudiation mechanism | Non-repudiation requirements | Non-repudiation implementation (per SL) | |

#### FR3: System Integrity (SI)

| SR ID | SR Description | Governance Control Point | Expected Evidence | Gate 1 Lite Minimum Requirement | Gate 3 Complete Requirement | Status |
|-------|----------------|--------------------------|-------------------|--------------------------------|----------------------------|--------|
| SR 3.1 | Communication Integrity | Gate 1: Design Baseline Document | Communication integrity mechanism | Integrity requirement identification | Integrity mechanism design | |
| SR 3.2 | Malicious Code Protection | Gate 1: Design Baseline Document | Malicious code protection | Protection policy definition | Protection mechanism design | |
| SR 3.3 | Security Functionality Verification | Gate 1: Design Baseline Document | Security functionality verification | Verification requirement definition | Verification procedure design | |
| SR 3.4 | Software and Information Integrity | Gate 1: Design Baseline Document | Software/information integrity | Integrity requirements | Integrity protection design | |
| SR 3.5 | Input Validation | Gate 1: Design Baseline Document | Input validation mechanism | Validation requirement identification | Validation mechanism design | |
| SR 3.6 | Deterministic Output | Gate 1: Design Baseline Document | Deterministic output | Output requirement definition | Output mechanism design | |
| SR 3.7 | Error Handling | Gate 1: Design Baseline Document | Error handling mechanism | Error handling policy | Error handling design | |
| SR 3.8 | Session Integrity | Gate 1: Design Baseline Document | Session integrity | Integrity requirements | Integrity mechanism design | |
| SR 3.9 | Protection of Audit Information | Gate 1: Design Baseline Document | Audit information protection | Protection requirement definition | Protection mechanism design | |

#### FR4: Data Confidentiality (DC)

| SR ID | SR Description | Governance Control Point | Expected Evidence | Gate 1 Lite Minimum Requirement | Gate 3 Complete Requirement | Status |
|-------|----------------|--------------------------|-------------------|--------------------------------|----------------------------|--------|
| SR 4.1 | Information Confidentiality | Gate 1: Design Baseline Document | Information confidentiality design | Confidentiality requirement identification | Confidentiality control design | |
| SR 4.2 | Information Persistence | Gate 1: Design Baseline Document | Information persistence control | Data retention requirements | Data sanitization design | |
| SR 4.3 | Use of Cryptography | Gate 1: Design Baseline Document | Cryptographic mechanism design | Cryptographic requirement identification | Cryptographic implementation design | |

#### FR5: Restricted Data Flow (RDF)

| SR ID | SR Description | Governance Control Point | Expected Evidence | Gate 1 Lite Minimum Requirement | Gate 3 Complete Requirement | Status |
|-------|----------------|--------------------------|-------------------|--------------------------------|----------------------------|--------|
| SR 5.1 | Network Segmentation | Gate 1: Zone & Conduit Diagram | Network segmentation design | Zone boundary definition | Complete segmentation design | |
| SR 5.2 | Zone Boundary Protection | Gate 1: Zone & Conduit Diagram | Zone boundary protection | Boundary control identification | Boundary protection design | |
| SR 5.3 | General Purpose Person-to-Person Communication Restrictions | Gate 1: Design Baseline Document | Communication restriction design | Restriction requirement identification | Restriction mechanism design | |
| SR 5.4 | Application Partitioning | Gate 1: Design Baseline Document | Application partitioning | Partitioning requirement identification | Partitioning design | |

#### FR6: Timely Response to Events (TRE)

| SR ID | SR Description | Governance Control Point | Expected Evidence | Gate 1 Lite Minimum Requirement | Gate 3 Complete Requirement | Status |
|-------|----------------|--------------------------|-------------------|--------------------------------|----------------------------|--------|
| SR 6.1 | Audit Log Accessibility | Gate 1: Design Baseline Document | Audit log access | Access requirement definition | Access mechanism design | |
| SR 6.2 | Continuous Monitoring | Gate 1: Design Baseline Document | Continuous monitoring design | Monitoring requirement identification | Monitoring mechanism design | |

#### FR7: Resource Availability (RA)

| SR ID | SR Description | Governance Control Point | Expected Evidence | Gate 1 Lite Minimum Requirement | Gate 3 Complete Requirement | Status |
|-------|----------------|--------------------------|-------------------|--------------------------------|----------------------------|--------|
| SR 7.1 | Denial of Service Protection | Gate 1: Design Baseline Document | DoS protection design | Protection requirement identification | Protection mechanism design | |
| SR 7.2 | Resource Management | Gate 1: Design Baseline Document | Resource management design | Resource requirement identification | Resource management design | |
| SR 7.3 | Control System Backup | Gate 1: Design Baseline Document | Backup design | Backup requirement definition | Backup mechanism design | |
| SR 7.4 | Control System Recovery and Reconstitution | Gate 1: Design Baseline Document | Recovery design | Recovery requirement definition | Recovery mechanism design | |
| SR 7.5 | Emergency Power | Gate 1: Design Baseline Document | Emergency power design | Power requirement identification | Power design (if applicable) | |
| SR 7.6 | Network and Security Configuration Settings | Gate 1: Design Baseline Document | Configuration management design | Configuration requirement definition | Configuration management design | |
| SR 7.7 | Least Functionality | Gate 1: Design Baseline Document | Least functionality design | Functionality minimization policy | Functionality minimization design | |
| SR 7.8 | Control System Component Inventory | Gate 1: Design Baseline Document | Component inventory management | Component inventory requirements | Component inventory design | |

### SR Checklist Usage Notes {#appA-sr-checklist-notes}

- **Gate 1 Lite**: Status may be Planned, but shall document expected completion timeframe
- **Gate 3**: All applicable SR Status shall be Implemented or N/A; N/A shall have signed-off justification
- **SR and Residual Risk Association**: If the Gate 3 residual risk register contains security-related risks, they shall reference the corresponding SR ID
- **SL Level Mapping**: Different SL levels have different strength requirements for SRs (e.g., SR 1.7 password strength requirements differ between SL 2 and SL 3); projects shall complete requirements according to the target SL

---

## Secondary Mapping: IEC 62443-2-4 and 62443-3-2 Linkage {#appA-secondary-mapping}

### IEC 62443-2-4 Program Requirements Mapping {#appA-2-4-mapping}

IEC 62443-2-4 defines security program requirements for service providers. The Gate mechanism of this governance framework provides the following evidence mapping:

| 62443-2-4 Requirement Area | Governance Control Point | Expected Evidence | Responsible Role |
|---------------------------|--------------------------|-------------------|------------------|
| SP.01 Security Management | Gate 0 through Gate 3 complete execution | Gate review records, approval documents | System Design Governance Function |
| SP.02 Configuration Management | Gate 2: Design Change Management | Change records, version management documents | System Architect |
| SP.03 Remote Access | Gate 1: Design Baseline Document | Remote access design, Zone & Conduit Diagram | System Architect |
| SP.04 Event Management | Gate 1: Design Baseline Document | Event management design, audit design | System Architect |
| SP.05 Account Management | Gate 1: Design Baseline Document | Account management design (maps to FR1) | System Architect |
| SP.06 Patch Management | Gate 2: Design Change Management | Patch procedure design, change control | System Architect |
| SP.07 Backup/Restore | Gate 1: Design Baseline Document | Backup/restore design (maps to FR7) | System Architect |
| SP.08 Malware Protection | Gate 1: Design Baseline Document | Malware protection design (maps to FR3) | System Architect |

### IEC 62443-3-2 Risk Assessment Mapping {#appA-3-2-mapping}

IEC 62443-3-2 defines risk assessment methodology for system design. The Integrated Risk Assessment of this governance framework (Section 3.2 of the main document) provides the following mapping:

| 62443-3-2 Requirement | Governance Control Point | Expected Evidence | Responsible Role |
|----------------------|--------------------------|-------------------|------------------|
| ZCR 1: Asset Identification | Gate 0: Risk Assessment Strategy | Asset inventory, Zone definition | System Architect |
| ZCR 2: Zone and Conduit Model | Gate 1: Zone & Conduit Diagram | Zone & Conduit Diagram (Lite or full version) | System Architect |
| ZCR 3: Risk Assessment | Gate 1: Integrated Risk Assessment Report | IEC 62443-3-2 + FMEA + HAZOP report | System Architect |
| ZCR 4: Security Requirements | Gate 1: IEC 62443 Alignment Checklist | "Primary Mapping Table" SR checklist in this appendix | System Architect |
| ZCR 5: Security Countermeasures | Gate 1: Design Baseline Document | Control measure design mapped to SR | System Architect |
| ZCR 6: Documentation | Gate 3: Final Design Package | All design documents, consistent versions | System Architect |
| ZCR 7: Risk Acceptance | Gate 3: Residual Risk Register | Residual risk register (using Appendix C template) | Risk Acceptance Authority |

### Role of FMEA and HAZOP in Integrated Risk Assessment {#appA-fmea-hazop-role}

The Integrated Risk Assessment of this governance framework requires IEC 62443-3-2, FMEA (Failure Mode and Effects Analysis), and HAZOP (Hazard and Operability Study) to be executed in parallel (see Section 3.2 of the main document). FMEA and HAZOP are not IEC 62443 compliance frameworks; they serve as supplementary inputs for IEC 62443-3-2 threat identification, ensuring risk identification covers failure modes and operational deviations beyond cybersecurity threats.

**Audit Evidence Traceability**:

- **IEC 62443-3-2 Threat Scenario**: Identifies cybersecurity threats, produces Threat Scenario ID (e.g., T-001)
- **FMEA Failure Mode**: Identifies system failure modes, produces Failure Mode ID (e.g., FM-SYS-001)
- **HAZOP Deviation**: Identifies operational process deviations, produces Deviation ID (e.g., HAZ-P001-D01)

Each risk item in the Gate 3 residual risk register shall have a Risk Source ID traceable to at least one of the above three sources. This traceability mechanism ensures all residual risks have clear analytical basis rather than being generated without foundation. For FMEA and HAZOP templates and scoring methods, refer to Appendix D.

---

## Security Level (SL) Determination Guidance {#appA-sl-guidance}

### SL Determination Process {#appA-sl-process}

Per Section 5.1 of the main document:

1. **Gate 0**: System Architect proposes target SL level based on system purpose, threat environment, and customer requirements
2. **Gate 1**: Complete SL level determination, verify design satisfies security requirements for target SL
3. **Gate 2**: If design changes affect SL level, reassessment and approval are required
4. **Gate 3**: Confirm residual risks do not affect target SL level declaration

**SL Changes Require Approval**: SL level downgrade shall be signed-off and accepted by Stakeholders (see Section 5.1 of the main document).

### SL Decision Record Template {#appA-sl-template}

Projects shall use the following template at each Gate to record SL decisions and attach to Gate review documents:

```{=latex}
\begin{center}
\begin{tabular}{|p{12cm}|}
\hline
\multicolumn{1}{|c|}{\textbf{SL DECISION RECORD}} \\
\hline
\textbf{Project ID:} \underline{\hspace{4cm}} \\[0.3em]
\textbf{Gate:} $\square$ Gate 0 \quad $\square$ Gate 1 \quad $\square$ Gate 2 \quad $\square$ Gate 3 \\[0.3em]
\textbf{Date:} \underline{\hspace{3cm}} (YYYY-MM-DD) \\
\hline
\textbf{Target SL:} $\square$ SL 1 \quad $\square$ SL 2 \quad $\square$ SL 3 \quad $\square$ SL 4 \\[0.3em]
\textbf{SL Rationale:} \underline{\hspace{8cm}} \\[0.3em]
\underline{\hspace{11cm}} \\
\hline
\textbf{SL Changed from Previous Gate?} $\square$ Yes \quad $\square$ No \\[0.3em]
If Yes, Previous SL: \underline{\hspace{1.5cm}} Change Reason: \underline{\hspace{4cm}} \\[0.3em]
Change Approved By: \underline{\hspace{3cm}} Date: \underline{\hspace{2.5cm}} \\
\hline
\textbf{Applicable Zones} (if multiple SL): \\[0.3em]
\quad Zone Name: \underline{\hspace{3cm}} Target SL: \underline{\hspace{1.5cm}} \\[0.3em]
\quad Zone Name: \underline{\hspace{3cm}} Target SL: \underline{\hspace{1.5cm}} \\
\hline
\textbf{Prepared By:} \underline{\hspace{3cm}} (System Architect) \\[0.3em]
\textbf{Reviewed By:} \underline{\hspace{3cm}} (Security Team) \\[0.3em]
\textbf{Approved By:} \underline{\hspace{3cm}} (Gate Approver) \\[0.3em]
\textbf{Approval Date:} \underline{\hspace{3cm}} \\
\hline
\end{tabular}
\end{center}
```

---

## Gate-Ready Compliance Checklists {#appA-gate-checklists}

The following checklists are for use during each Gate review. Each checklist item shall indicate passing criteria and evidence source.

### Gate 0 Compliance Checklist {#appA-gate0-checklist}

**Important Statement**: Gate 0 is an Acceptance Decision. This checklist is used to verify whether the design request meets the quality thresholds defined in the main document. This checklist **does not constitute mandatory submission requirements for the Design Requesting Function**; rather, it serves as verification criteria used by the System Design Department when making the acceptance decision.

| # | Checklist Item | Corresponding Quality Threshold | Verification Criteria | Pass |
|---|----------------|--------------------------------|----------------------|------|
| 1 | Request objective clarity | Comprehensibility | Design request objectives and expected outcomes can be understood by the team | [ ] |
| 2 | Scope definability | Comprehensibility + Scope Stability | Design scope has identifiable boundaries, inclusion and exclusion criteria are clear | [ ] |
| 3 | Technical assessability | Evaluability | Sufficient information provided to conduct preliminary technical feasibility assessment | [ ] |
| 4 | Risk assumption identifiability | Evaluability | Sufficient information provided to identify preliminary risk assumptions | [ ] |
| 5 | Design Requesting Function identified | Accountable Owner | Clear DRF exists who is accountable for business rationale of the design request | [ ] |
| 6 | Scope stability assessment | Scope Stability | Request objectives and scope are sufficiently stable to avoid major changes during design phase | [ ] |

**Acceptance Decision Result**:

| All Items Pass | Items 1-5 Pass but Item 6 Conditional | Any of Items 1-5 Fail |
|----------------|--------------------------------------|----------------------|
| **Accepted** | **Conditional Acceptance** (specify stability requirements) | **Not Accepted** (specify deficiency items) |

**Gate 0 Approver**: Engineering Management

### Gate 1 Compliance Checklist {#appA-gate1-checklist}

| # | Checklist Item | Passing Criteria | Evidence Source | Pass |
|---|----------------|------------------|-----------------|------|
| 1 | Design baseline document complete | Includes system architecture diagram, interface definitions, data flow diagram | Design Baseline Document | [ ] |
| 2 | Integrated risk assessment completed | IEC 62443-3-2, FMEA, HAZOP all have outputs (Lite or full version) | Integrated Risk Assessment Report | [ ] |
| 3 | Zone & Conduit Diagram established | At least critical trust boundaries identified | Zone & Conduit Diagram | [ ] |
| 4 | IEC 62443 alignment checklist completed | "Primary Mapping Table" SR checklist filled, all applicable SRs have Status | IEC 62443 Alignment Checklist | [ ] |
| 5 | Requirements traceability matrix established | Critical design decisions traceable to requirements | Requirements Traceability Matrix | [ ] |
| 6 | Target SL level confirmed | SL Decision Record updated | SL Decision Record | [ ] |
| 7 | Security control measures defined | High-risk items have corresponding control measures | Design Baseline Document, Risk Assessment Report | [ ] |
| 8 | Document version numbers marked | All documents have version number, date, owner | Document Headers | [ ] |
| 9 | Review sign-off completed | Security Team, QA Team reviews completed | Review Sign-off Record | [ ] |

**Gate 1 Approver**: System Design Governance Function

### Gate 2 Compliance Checklist {#appA-gate2-checklist}

| # | Checklist Item | Passing Criteria | Evidence Source | Pass |
|---|----------------|------------------|-----------------|------|
| 1 | Change description and rationale recorded | Change content and rationale clear | Change Request Document | [ ] |
| 2 | Impact analysis completed | Affected modules, interfaces, requirements identified | Impact Analysis Document | [ ] |
| 3 | Risk assessment updated | Per Section 3.2.5 trigger conditions, affected analyses updated | Updated Risk Assessment Document | [ ] |
| 4 | IEC 62443 alignment reviewed | If change affects SR mapping, "Primary Mapping Table" checklist updated | Updated SR Checklist | [ ] |
| 5 | SL level impact assessed | If SL affected, SL Decision Record updated and approved | SL Decision Record | [ ] |
| 6 | Design document version incremented | Post-change document versions consistently incremented | Updated Design Documents | [ ] |
| 7 | Major changes approved | If meeting major change definition, Engineering Management approved | Approval Record | [ ] |

**Gate 2 Approver**: Engineering Management

### Gate 3 Compliance Checklist {#appA-gate3-checklist}

| # | Checklist Item | Passing Criteria | Evidence Source | Pass |
|---|----------------|------------------|-----------------|------|
| 1 | Final design package complete | All documents have version number, release date, document owner | Final Design Package | [ ] |
| 2 | Document versions consistent | All documents reference same baseline version number | Version Consistency Check | [ ] |
| 3 | Integrated risk assessment is full version | Gate 1 Lite upgraded to full version | Full Version Risk Assessment Report | [ ] |
| 4 | IEC 62443 alignment checklist complete | All applicable SR Status is Implemented or N/A (with signed-off justification) | Completed SR Checklist | [ ] |
| 5 | Residual risk register complete | Uses Appendix C template, each risk has Risk Source ID | Residual Risk Register | [ ] |
| 6 | Residual risk traceability valid | QA Team spot-checked at least 20% of high-risk items | QA Spot-Check Record | [ ] |
| 7 | Residual risks accepted with sign-off | Per Section 5.2 of main document authority levels | Risk Acceptance Sign-off Record | [ ] |
| 8 | SL level declaration valid | Residual risks do not affect target SL level | SL Decision Record | [ ] |
| 9 | Design delivery checklist complete | Gate 1, Gate 2 requirements satisfied | Design Delivery Checklist | [ ] |
| 10 | Handover meeting held | Design team and execution team held handover meeting | Handover Meeting Minutes | [ ] |
| 11 | Handover confirmation recorded | Handover meeting minutes record "Project execution unit has completed handover confirmation" | Handover Meeting Minutes | [ ] |
| 12 | Dual sign-off completed | System Architect + Project Manager signed off | Handover Meeting Minutes Sign-off | [ ] |

**Gate 3 Approver**: System Design Governance Function

---

## Document Control {#appA-doc-control}

- **Version**: 1.0
- **Effective Date**: 2026-01-08
- **Owner**: System Design Governance Function
- **Approved By**: Engineering Management
- **Review Cycle**: Synchronized with main document, at least annually

Revisions to this appendix follow the procedure in Section 6.2 of the main document. Appendix content adjustments are minor revisions and require notification only.

---

## CHANGELOG

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-09 | Initial release aligned with System Design Governance v1.0 |

**Key Changes (relative to original version)**:

1. **Structure Reorganization**: Changed from simple Mapping Table to comprehensive structure covering usage guidelines, complete FR1-FR7 SR mapping, and Gate checklists
2. **Removed Incorrect References**: Deleted terms not existing in main document such as "Design Review Phase 2", replaced with correct Gate names
3. **Removed Default SL 2 Declaration**: Original version claimed "default to SL 2 baseline" but main document has no such provision; corrected to "target SL is project-specific"
4. **Added Complete FR1-FR7 SR Mapping Template**: Provided copyable SR checklist template covering all IEC 62443-3-3 SRs
5. **Added Status Definitions**: Clearly defined meaning and evidence requirements for Implemented/Planned/N/A
6. **Added IEC 62443-2-4 and 3-2 Mapping Tables**: Supplemented Gate evidence mapping for procedural requirements and risk assessment methodology
7. **Added SL Decision Record Template**: Provided SL decision record template attachable to Gate documents
8. **Added Gate 0-3 Complete Checklists**: Each Gate has specific checklist items, passing criteria, and evidence sources
9. **Aligned Main Document Terminology**: Unified use of System Design Governance Function, System Architect, Handover Meeting Minutes and other terms
10. **Added Document Version Control**: Added version information per Section 6.2 of main document requirements

---

**End of Document**

```{=latex}
\disableLandscapeHeaderFooter
\end{landscape}
\pagestyle{fancy}
```
