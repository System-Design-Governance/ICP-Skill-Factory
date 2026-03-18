<!-- Filename: System_Design_Governance.md -->

# System Design Governance

> **IMPORTANT NOTICE**: This English version is provided for reference and external review only. The official governance of record is the zh-TW (Traditional Chinese) version. In case of any discrepancy, the zh-TW version shall prevail.

## Purpose and Authority {#purpose-and-authority}

This document defines the **governance principles, responsibility boundaries, and decision-making processes** for the system design phase within the organization. Its objectives are to:

- Ensure consistency in system design decisions regarding security, quality, and compliance
- Clearly separate design responsibility, risk disclosure, and execution responsibility
- Serve as the formal basis for project initiation, design delivery, and audit determination

### Governance Status and Mandatory Statement

**This document serves as the authoritative reference for all system design governance documents and carries the following mandatory requirements:**

1. **Mandatory Scope**: All projects involving system architecture, security-critical design, or risk assumptions **shall comply** with the governance requirements defined in this document and its appendices.

2. **Authorization Source**: This document is issued by the System Design Governance Function and approved for implementation by Engineering Management.

3. **Effective Date**: From 2026-01-08, all newly initiated projects shall comply with this document. Ongoing projects involving major design changes shall also comply with Gate 2 and Gate 3 requirements.

### Consequences of Non-Compliance

Projects that fail to comply with this governance document shall face the following institutional consequences:

- **Gate 0 Not Passed**: The project shall not be initiated; no external commitments regarding timeline or resources shall be made
- **Gate 1 Not Completed**: The project shall not proceed to the detailed design phase; implementation shall not begin
- **Gate 2 Not Executed**: Design changes shall not be implemented; the project shall be suspended until deviation records are completed
- **Gate 3 Not Delivered**: Design responsibility cannot be transferred; the System Design Department shall not acknowledge design delivery as complete
- **Audit Non-Compliance**: The project cannot pass IEC 62443-2-4 compliance audit, affecting product certification and external delivery

**Important Statement**: The purpose of this document is not to obstruct project execution, but to ensure that design decisions are made and handed over responsibly. The value of governance lies not in avoiding all risks, but in ensuring that every risk has a designated owner.

---

## Pre-Gate0 Clarification Boundary {#pre-gate0-boundary}

### Governance Responsibility Start Point Declaration {#governance-start-point}

**This governance framework's responsibility applicability has Gate 0 approval as the explicit start point.**

Before Gate 0 approval, any form of discussion, clarification, consultation, concept exploration, or assistance does **not** establish the following effects:

1. **Does Not Constitute Acceptance**: Pre-Gate0 interactions do not represent that the System Design Department has accepted the design request. No commitment to formal design deliverables shall be interpreted from these interactions.

2. **Does Not Constitute Responsibility Assumption**: Before Gate 0 approval, the System Design Department does not bear design responsibility for the requirements. All discussions are of an advisory nature; the requesting party shall make their own judgments and decisions.

3. **Does Not Constitute Resource Commitment**: Pre-Gate0 discussions do not trigger resource allocation. Any resource estimates or preliminary scheduling are solely for the requesting party's reference in initiating Gate 0.

4. **Does Not Constitute Delivery Commitment**: Before Gate 0 approval, there is no design delivery timeline. Any timeline discussions are exploratory only and do not constitute commitments.

### Support Positioning for Pre-Gate0 Stage {#pre-gate0-support}

The System Design Department **may** provide the following support during the Pre-Gate0 stage, but this support is at the discretion of the System Design Department and is not a governance obligation:

- Preliminary technical consultation
- Scope clarification assistance
- Information completeness recommendations
- Risk assessment strategy suggestions

**Important Reminder**: The above support is provided to help the Design Requesting Function prepare for Gate 0 and is not in itself part of the governance process.

### Design Requesting Function {#design-requesting-function}

**Design Requesting Function (DRF)** refers to the **sole legitimate source** for submitting design requests to the System Design Department. This role is accountable for the **business purpose, operational necessity, or strategic rationale** of the design request.

**Role Mapping**: Depending on organizational structure, this may be filled by Business Owner, Product Owner, Requirement Owner, or an authorized project sponsor.

**Relationship with Risk Acceptance Authority (RAA)**:

- **DRF as Business Owner**: When Business Owner serves as the Design Requesting Function, they are responsible for design request submission and business rationale confirmation (Gate 0, Gate 2)
- **Business Owner as RAA**: When Business Owner participates in Risk Acceptance Authority (High Risk scenarios), they are responsible for residual risk acceptance sign-off (Gate 3)
- **No Role Confusion**: When the same person exercises different responsibilities at different times, sign-off records shall be maintained separately, and DRF duties shall not be exercised in place of RAA duties

For detailed role responsibilities and RACI assignment, refer to **Appendix B: RACI Matrix**.

---

## Applicability and Scope {#applicability-and-scope}

### Applicability Criteria

This governance document applies to projects meeting **any of the following conditions** and **shall not be bypassed**:

#### Mandatory Application Types

| Project Type | Criteria | Minimum Gate Requirements |
|--------------|----------|---------------------------|
| **New System Development** | System or platform designed from scratch | Gate 0 through Gate 3 (all required) |
| **Major Architecture Changes** | Affects core system architecture, data flow, or external interfaces | Gate 1 through Gate 3 |
| **Security-Critical Functions** | Involves authentication, authorization, encryption, or critical data protection | Gate 1 through Gate 3 |
| **Compliance Risk Changes** | Affects IEC 62443 SL level or regulatory compliance | Gate 2 through Gate 3 |

#### Applicability Determination Process

If the project sponsor or project manager has questions regarding "whether this document applies," the following process shall be followed:

1. **Initial Self-Assessment**: The Project Manager conducts an initial assessment based on the above criteria
2. **Consultation Confirmation**: If questions remain, submit a written inquiry to the System Design Governance Function
3. **Formal Determination**: The System Design Governance Function shall provide a written determination within 3 business days
4. **Record Retention**: The determination result shall be included in project documentation as audit evidence

**Determination Principle**: When in doubt, adopt the "conservative interpretation" principle: **if uncertain, treat as applicable**.

### Exception Handling Mechanism

If deviation from this governance process is required due to schedule, business, or technical constraints, the following exception handling mechanism shall be followed:

#### Exception Application Conditions

Exception applications are limited to the following scenarios:

- **Emergency Security Patches**: A security incident has occurred requiring immediate remediation, and the complete Gate process cannot be awaited
- **Regulatory Mandatory Requirements**: Mandatory changes required by external regulations or authorities with explicit deadlines
- **Critical Business Commitments**: Signed business commitments where breach would result in significant legal or financial losses

**The following reasons shall not be accepted for exception applications**: "Tight project schedule," "Insufficient resources," "Customer requests acceleration," "Work has already started"

#### Exception Application Process

1. **Applicant**: The Project Manager or Department Head submits a written exception application
2. **Application Content** shall include: Which Gates or governance requirements are being deviated from, why normal process cannot be followed (must meet the exception application conditions above), risk assessment and mitigation measures, expected date to fulfill governance requirements
3. **Approval Authority**:
   - Gate 0 / Gate 1 Exception: Requires Engineering Management approval
   - Gate 2 Exception: Requires System Design Governance Function approval
   - Gate 3 Exception: Requires joint approval from Engineering Management and the Risk Acceptance Authority
4. **Record Retention**: All exception applications and approval records shall be included in project documentation and reviewed during annual audits

#### Exception Consequences and Remediation

Even with exception approval, the following requirements shall be observed:

- **Risk Bearing**: Risks arising during the exception period shall be jointly borne by the exception approver and the project execution unit
- **Remediation Requirements**: The exception approval document shall specify which Gates must be completed and the completion deadline; if overdue, the matter shall be escalated to Engineering Management for decision and may result in project or delivery suspension
- **Audit Tracking**: Exception cases shall be included in the priority audit list until remediation measures are completed

---

## Governance Model and Design Gates

System design governance operates through a **Gate mechanism**, ensuring design decisions are reviewed, confirmed, and handed over at appropriate points.

### Core Principles of Design Governance

This governance framework is built upon the following core principles, and all Gate reviews shall verify that these principles are implemented:

- **Security by Design**: Security requirements shall be incorporated from the early design stage, not added as an afterthought. Gate 0 shall identify security requirements; Gate 1 shall define security control measures.

- **Traceability**: All critical design decisions shall be traceable to requirements and risk assumptions. All design documents from Gate 1 through Gate 3 shall include a requirements traceability matrix.

- **Compliance Alignment**: Design shall comply with applicable regulations and standards (such as IEC 62443). Gate 1 shall complete the IEC 62443 alignment checklist (see Appendix A).

- **Risk-based Decision Making**: Design trade-offs shall be based on risk, not solely on technical feasibility. All major decisions from Gate 0 through Gate 3 shall include risk assessment records.

### Integrated Design Risk Assessment

This governance framework requires that risk assessment during the system design phase **shall adopt an integrated methodology**, combining the following three analysis methods:

1. **IEC 62443-3-2**: Identify cybersecurity threats, assess security risks, define Zones/Conduits, select security control measures
2. **FMEA (Failure Mode and Effects Analysis)**: Identify system/subsystem/component failure modes, assess failure consequences, define detection and mitigation measures
3. **HAZOP (Hazard and Operability Study)**: Identify operational process deviations, assess deviation consequences, define protective measures and operational procedures

**Integration Principle**: The three methods cannot substitute for each other; all shall be executed. Gate 3 residual risks shall be traceable to at least one of these three methods; otherwise, the risk record shall be deemed invalid.

#### Risk Assessment Governance Timeline

| Gate | Risk Assessment Requirements | Minimum Acceptable Form | Responsible Role |
|------|------------------------------|-------------------------|------------------|
| Gate 0 | Submit risk assessment strategy and scope | Written explanation of the scope and depth for all three methods | System Architect |
| Gate 1 | Complete preliminary risk assessment | Lite form (see definition below) | System Architect |
| Gate 2 | Design changes trigger risk reassessment | Update affected analysis items | System Architect |
| Gate 3 | Residual risk traceability and acceptance | Full version (see definition below) | System Architect + Risk Acceptance Authority |

#### Gate 1 Lite Risk Assessment Definition

If the project adopts the Lite form at Gate 1, the minimum acceptable content for each method is as follows:

- **IEC 62443-3-2 Lite**: Initial Zone & Conduit Diagram, threat scenario list, preliminary target SL level mapping
- **FMEA Lite**: Top-level Failure Modes, S/O/D scoring, control measures for high-risk items
- **HAZOP Lite**: Critical process Guide Word analysis, protective measures for high-consequence deviations

**Common Lite Requirements**: Written records with version number, date, participating analyst signatures, and review sign-off records are required

#### Full Version Risk Assessment Requirements

Full version risk assessment shall be completed before Gate 3. Each method shall include:

- **IEC 62443-3-2 Full Version**: Final Zone & Conduit Diagram, complete Threat Modeling, Security Requirements Traceability Matrix, Risk Treatment Plan
- **FMEA Full Version**: Complete RPN calculation (S×O×D), Action Plans for all high-risk items, post-improvement RPN verification
- **HAZOP Full Version**: Complete Guide Word analysis, Risk Ranking, operational procedure recommendations

**Common Full Version Requirements**: Formal templates shall be used (see Appendix D), complete review and sign-off chain, version management and change history

**Transitional Rule When Appendix D Is Not Yet Published**: If Appendix D has not been formally published, the project may use equivalent formats that meet the content requirements of this section, but shall not claim "compliance with Appendix D" in any document, nor use this as evidence of Gate 1 or Gate 3 completeness.

#### Lite Upgrade Rules and Restrictions

If the Lite form is used to pass Gate 1, it shall be upgraded to the full version before Gate 3. If not upgraded, Gate 3 shall not be released.

**Lite Scope Restrictions**: For projects classified as "Security-Critical Functions" and "Major Architecture Changes" as defined above, Gate 1 shall not use Lite as the final deliverable basis. Such projects shall complete at least the IEC 62443-3-2 Full Version before entering any implementation or procurement.

#### Design Change Risk Reassessment Trigger Conditions

When Gate 2 design changes meet any of the following conditions, the corresponding risk assessment shall be updated:

- **Triggers for IEC 62443-3-2 Update**: Zone/Conduit boundary changes, external interface changes, security control measure changes, SL level adjustments
- **Triggers for FMEA Update**: System architecture changes, failure detection mechanism changes, redundancy design changes, critical component changes
- **Triggers for HAZOP Update**: Operational process changes, control logic changes, human-machine interface changes, safety interlock changes

The updated document version number shall be incremented and re-reviewed and signed off.

#### Residual Risk Traceability Requirements

Each risk item in the Gate 3 residual risk list shall be traceable to at least one of the following sources:

- IEC 62443-3-2 Threat Scenario ID
- FMEA Failure Mode ID
- HAZOP Deviation ID

If a risk cannot provide a source ID, the risk record shall be deemed invalid, and Gate 3 shall not be released. The QA Team shall spot-check at least 20% of high-risk items for traceability validity during the Gate 3 review.

### Design Governance Gate Definitions

#### Governance Role Definitions

This document adopts the following role model:

- **Owner**: The Owner of this document is the System Design Governance Function
- **Accountable**: The role responsible for Gate output content, typically the System Architect
- **Approver**: The single role with authority to decide whether a Gate passes
- **Required Reviewers**: Shall complete review and sign-off, but do not independently hold release authority
- **Co-signers**: Shall jointly sign to share responsibility for matters such as risk acceptance, but this does not represent Gate release authority

**Important Principle**: Each Gate has only one Approver to avoid dispersed authority and responsibility.

#### Gate Architecture Overview

| Gate | Purpose | Trigger Timing | Minimum Output Requirements | Blocking Conditions |
|------|---------|----------------|-----------------------------|--------------------|
| Gate 0 | Acceptance decision: determine if design request meets quality thresholds | After DRF submits request | Technical feasibility assessment, preliminary risk list, risk assessment strategy | Quality thresholds not met |
| Gate 1 | Design baseline establishment and preliminary risk disclosure | After preliminary design completion | Design baseline document, integrated risk assessment, IEC 62443 alignment checklist, requirements traceability matrix | Security requirements undefined |
| Gate 2 | Design change and deviation management | When design changes occur | Change impact analysis, risk reassessment | Major changes not approved |
| Gate 3 | Design delivery and residual risk responsibility transfer | Before design completion and delivery | Final design documents, residual risk list, handover meeting minutes | Residual risks not accepted |

#### Gate 0: Acceptance Decision (Project Initiation Review) {#gate0-acceptance}

**Purpose**: Determine whether a design request meets the acceptance quality thresholds for entering the formal governance process. Gate 0 is an **Acceptance Decision**, not document checklist validation.

**Trigger Timing**: After the Design Requesting Function submits a design request, before formal project initiation.

**Acceptance Quality Thresholds**:

Gate 0 determines whether the design request reaches an acceptable quality level for the System Design Department to commence formal design activities. The quality thresholds are:

1. **Comprehensibility**: The design request's objectives, scope, and expected outcomes can be understood by the System Design Department
2. **Evaluability**: Sufficient information is provided to assess technical feasibility and preliminary risk assumptions
3. **Accountable Owner**: A clear Design Requesting Function exists who is accountable for the business rationale of the design request
4. **Scope Stability**: The request's objectives and scope are sufficiently stable to avoid major changes during the design phase

**Determination Result Categories**:

- **Accepted**: Meets all quality thresholds, formal design activities commence
- **Conditional Acceptance**: Partially meets thresholds, supplementary information required, may enter Gate 0 upon completion
- **Not Accepted**: Does not meet quality thresholds, remains in Pre-Gate0 clarification

**Gate 0 Outputs** (Generated by System Design Department after acceptance decision):

1. Technical feasibility assessment report (including technology selection, architecture concept)
2. Preliminary risk list (including at least security, compliance, and technical risks)
3. Target IEC 62443 SL level proposal
4. Risk assessment strategy and scope document (explicitly stating the scope and depth of IEC 62443-3-2, FMEA, and HAZOP methods)
5. Preliminary resource and schedule estimates

**Important Statement**: Gate 0 outputs are produced by the System Design Department following the acceptance decision. These are not mandatory submission requirements for the Design Requesting Function. The Design Requesting Function's obligation is to provide information sufficient for the System Design Department to assess whether the acceptance quality thresholds are met.

**Blocking Conditions**: No unit willing to accept critical technical risks, obvious violation of regulations or company policies, resource requirements far exceeding company capacity

**Consequences of Not Passing**: Project shall not be initiated, no external commitments regarding timeline or functionality shall be made, formal development resources shall not be allocated

**Responsible Roles**:

- Accountable: System Architect
- Approver: Engineering Management

#### Gate 1: Design Baseline Establishment

**Purpose**: Establish the design baseline, ensuring the design direction is correct and risks have been sufficiently identified.

**Trigger Timing**: After preliminary design completion, before starting detailed design.

**Minimum Output Requirements**:

1. Design baseline document (including system architecture diagram, interface definitions, data flow diagram)
2. Integrated risk assessment report (Lite or full version as per requirements above)
3. IEC 62443 alignment checklist (see Appendix A)
4. Requirements traceability matrix

**Blocking Conditions**: Security requirements undefined or control measures insufficient, IEC 62443 alignment check incomplete, critical design decisions not traceable to requirements, major risks not identified

**Consequences of Not Passing**: Shall not proceed to detailed design phase, implementation or procurement shall not begin

**Responsible Roles**:

- Accountable: System Architect
- Approver: System Design Governance Function
- Required Reviewers: Security Team, QA Team

#### Gate 2: Design Change Management

**Purpose**: Manage design changes, ensuring changes do not introduce unevaluated risks.

**Trigger Timing**: After design baseline establishment, when any design change occurs.

**Minimum Output Requirements**:

1. Change description and rationale
2. Impact analysis
3. Risk reassessment (updated according to trigger conditions above)
4. Updated design documents (version number incremented)

**Blocking Conditions**: Major changes not approved by Engineering Management, changes causing SL level reduction not accepted, changes introducing new high risks without control measures

**Consequences of Not Passing**: Changes shall not be implemented, project suspended until deviation records are completed

**Responsible Roles**:

- Accountable: System Architect
- Approver: Engineering Management (may delegate the Governance Function to execute review and consolidation, but release authority and responsibility remain with Engineering Management; only one Approver shall appear on documentation)

**Major Change Definition**: Affects core system architecture or external interfaces, changes SL level, adds or removes security control measures, affects signed contract commitments

#### Gate 3: Design Delivery and Responsibility Transfer

**Purpose**: Complete design delivery, transfer design responsibility to the project execution unit, and ensure residual risks have been accepted.

**Trigger Timing**: After detailed design completion, before delivery for implementation.

**Minimum Output Requirements**:

1. Final design document package (all documents marked with version number, release date, document owner; referenced version numbers shall be consistent)
2. Residual risk list (using the Appendix C template, shall meet traceability requirements above)
3. Design delivery checklist
4. Handover meeting minutes (shall record "project execution unit has completed handover confirmation," signed by both parties)

**Blocking Conditions**: Residual risks not signed off for acceptance, risk list contains items that cannot be traced, documents incomplete or version inconsistent, Gate 1 Lite not upgraded to full version, handover meeting minutes do not record handover confirmation

**Consequences of Not Passing**: Design responsibility cannot be transferred, project execution unit shall not claim "design has been delivered," proceeding to implementation without completing Gate 3 shall be treated as a deviation from governance process, requiring exception mechanism activation and responsibility determination by Engineering Management

**Responsible Roles**:

- Accountable: System Architect
- Approver: System Design Governance Function (release prerequisite: residual risks have been signed off by the authority defined below, handover meeting minutes record handover confirmation)
- Required Reviewers: QA Team
- Risk Acceptance Authority: Defined by residual risk management below, separate from Approver

**Post-Design Delivery Responsibility Boundaries**:

- System Design Department: Responsible for design content correctness and risk disclosure completeness, but not responsible for implementation results
- Project Execution Unit: Responsible for implementation results, residual risk assumption, and subsequent operational risks
- Dispute Resolution: Determined by Engineering Management

---

## Roles, Handover, and Accountability

### Role Separation Principle

This governance framework clearly distinguishes three responsibility entities:

| Responsibility Entity | Scope of Responsibility | Responsibility Endpoint |
|-----------------------|-------------------------|-------------------------|
| System Design Department | Design content correctness, risk disclosure completeness, IEC 62443 compliance | Gate 3 delivery completion |
| Project Execution Department | Implementation results, residual risk assumption decisions, risk management during execution | Project closure |
| Operations and Maintenance Department | Operational risks, system maintenance, incident response | System decommissioning |

**Important Principles**:

- The System Design Department is not responsible for implementation results
- The Project Execution Department is not responsible for design content correctness
- The Operations and Maintenance Department is not responsible for design or implementation defects

### Delivery and Responsibility Transfer Timing

Responsibility transfer occurs at the following points:

1. **Upon Gate 3 Completion**: Design responsibility transfers from the System Design Department to the Project Execution Department
2. **Upon Project Closure**: Implementation responsibility transfers from the Project Execution Department to the Operations and Maintenance Department
3. **Upon System Decommissioning**: All responsibilities terminate

**Responsibility Transfer Prerequisites**: Completion of corresponding Gate review, written handover documents, handover meeting convened and minutes retained, receiving unit written sign-off confirmation

**Consequences of Failed Responsibility Transfer**: Responsibility remains with the original unit, receiving unit has the right to refuse to accept subsequent risks

### Dispute Resolution and Escalation Mechanism

When cross-departmental disputes arise regarding responsibility attribution, the following escalation path shall be followed:

- **Level 1** (within 3 business days): System Architect + Project Manager + QA Team three-party negotiation
- **Level 2** (within 5 business days): Submit to System Design Governance Function for arbitration
- **Level 3** (within 10 business days): Submit to Engineering Management for final decision

**Important Principle**: During disputes, the project shall not proceed to the next phase. Exception scenario: If involving "Emergency Security Patches" as defined above, emergency measures may continue, but the exception mechanism shall be activated simultaneously.

For detailed role and responsibility matrix, please refer to **Appendix B: RACI Matrix**.

---

## Risk and Compliance Alignment

### IEC 62443 Standard Alignment

For the correspondence between this governance model and IEC 62443-2-4 and IEC 62443-3-3, please refer to **Appendix A: IEC 62443 Alignment**.

**IEC 62443 SL Determination Timeline**:

- Gate 0: Propose target SL level (preliminary assumption)
- Gate 1: Complete SL level determination and alignment check
- Gate 2: If design changes affect SL level, reassessment and approval are required
- Gate 3: Confirm residual risks do not affect target SL level declaration

**Non-Compliance Handling**: If the design cannot meet the target SL level, the target SL level shall be lowered (requires stakeholder sign-off acceptance) or the design shall be revised. "Technical limitations" shall not be used as a reason to bypass IEC 62443 requirements.

### Residual Risk Management

Risks that cannot be fully eliminated during the design phase are called **residual risks** and shall be explicitly disclosed at Gate 3 delivery with responsibility transfer completed.

**Recording Requirements**: Use the Appendix C template; each residual risk shall include risk description, inherent risk level, implemented control measures, residual risk level, risk acceptance decision and sign-off.

**Risk Level Determination Basis**:

- Risk level (Low / Medium / High / Critical) shall be based on the risk matrix defined in Appendix C
- Risk levels shall not be assigned based solely on subjective judgment
- Likelihood and Impact scoring basis and calculation process shall be retained
- Auditors shall be able to recalculate the same result during audits; otherwise, the risk assessment shall be deemed invalid

**FMEA RPN Special Requirements**: Severity, Occurrence, and Detection scoring basis and RPN threshold shall be recorded; post-improvement RPN shall be recalculated.

**Risk Level Consistency Requirements**: When the same risk appears in different documents or sections, the risk level shall be consistent and shall be based on the residual risk list; if there are discrepancies, they shall be explained in the handover meeting minutes.

**Residual Risk Acceptance Authority**:

- Low Risk: Accepted by Project Manager
- Medium Risk: Jointly accepted by Project Manager + Security Lead
- High Risk: Jointly accepted by Project Manager + Security Lead + Business Owner
- Critical Risk: Shall be escalated to Engineering Management with an additional mitigation plan developed

**Consequences of Residual Risks Not Accepted**: Gate 3 cannot be completed, design responsibility cannot be transferred, project shall not proceed to implementation phase

**Important Principle**: Acceptance of residual risks is the responsibility and right of the Project Execution Unit. The System Design Department shall not accept residual risks on behalf of the Project Execution Unit.

---

## Governance Interface Compatibility {#governance-interface}

### Purpose Statement {#interface-purpose}

This chapter provides interface specifications for external functions (e.g., External Contractors, Customer Project Teams, Cross-Organization Units) to integrate their internal processes with this governance framework. The interface specifications are designed to ensure governance compatibility without mandating changes to external organizations' internal procedures.

### Core Interface Concept: Pipeline Interface {#pipeline-interface}

This governance framework provides a "Pipeline Interface" allowing external functions to connect their internal processes to the governance mechanism:

```
[External Function Internal Process] → [Governance Interface Adapter] → [Gate Mechanism]
```

**Interface Design Principles**:

1. **Tool Agnostic**: The governance framework does not mandate specific tools. External functions may use any document management system, project management tools, or workflows
2. **Abstraction over Implementation**: The interface defines "what needs to be provided," not "how to produce it"
3. **Role Mapping Instead of Role Specification**: External functions map their internal roles to governance roles rather than creating new positions
4. **Decision Point Alignment**: Identify existing internal decision points as potential Gate triggers rather than adding new approval layers

### Interface Adapter Elements {#interface-elements}

When external functions integrate with this governance framework, the following elements shall be defined:

#### Element 1: Role Mapping Table {#role-mapping}

| Governance Framework Role | External Function Corresponding Role | Responsibility Scope Description |
|---------------------------|--------------------------------------|----------------------------------|
| Design Requesting Function | [To be mapped] | Accountable for business rationale of design requests |
| System Architect | [To be mapped] | Accountable for design content correctness |
| Risk Acceptance Authority | [To be mapped] | Decides whether to accept residual risks |

**Mapping Rules**:

- Each governance role may be mapped to one or more external roles, but responsibility shall remain clear
- Roles mapped to Design Requesting Function shall have authority over requirement decisions
- Roles mapped to Risk Acceptance Authority shall have authority over risk acceptance decisions
- Mapping results shall be documented at Gate 0 and reviewed when changes occur

#### Element 2: Decision Point Mapping {#decision-point-mapping}

| Governance Gate | External Function Decision Point | Trigger Mechanism |
|-----------------|----------------------------------|-------------------|
| Gate 0 Acceptance Decision | [To be mapped] | [To be described] |
| Gate 1 Design Baseline Review | [To be mapped] | [To be described] |
| Gate 2 Design Change Approval | [To be mapped] | [To be described] |
| Gate 3 Design Delivery Confirmation | [To be mapped] | [To be described] |

**Mapping Principles**:

- Existing decision points may be reused, provided they achieve equivalent governance effects
- If no corresponding decision point exists, new review points may be added
- Mapping results shall be confirmed by the System Design Governance Function

#### Element 3: Auditability Requirements {#auditability-requirements}

Regardless of what tools or processes external functions use, the following records shall be producible for audits:

| Record Type | Minimum Content Requirements | Retention Period |
|-------------|------------------------------|------------------|
| Gate Review Record | Date, Participants, Determination Result, Approval | Project Duration + 3 Years |
| Design Document Version History | Version Number, Change Summary, Approver | Project Duration + 3 Years |
| Risk Acceptance Record | Risk ID, Level, Accepting Party, Sign-off Date | Project Duration + 5 Years |

### External Function Integration Process {#integration-process}

```
1. Identify: Review this governance framework's Gate definitions and role definitions
2. Map: Complete Role Mapping Table and Decision Point Mapping
3. Confirm: Submit mapping results to System Design Governance Function for confirmation
4. Execute: Execute governance process according to confirmed mapping
5. Audit: Produce required records during audits
```

### Non-Negotiable Constraints {#non-negotiable}

When integrating with the governance framework, the following constraints shall not be bypassed regardless of external process complexity:

1. **Single Approver Principle**: Each Gate shall have only one Approver; no ambiguity is allowed
2. **Risk Acceptance Separation**: Risk Acceptance Authority and Gate Approver shall not be the same role
3. **Traceability Requirements**: Residual risks shall be traceable to risk assessment; untraceable risks are invalid
4. **Version Consistency**: Gate 3 document package versions shall be consistent; no partial delivery
5. **Record Retention**: Audit records shall meet minimum retention period requirements

### Compatibility Validation {#compatibility-validation}

External functions may conduct compatibility self-assessment using the following checklist before formal integration:

| Validation Item | Pass Criteria |
|-----------------|---------------|
| Role Mapping Complete | All governance roles have mapped counterparts |
| Decision Point Mapping Complete | All Gates have corresponding trigger mechanisms |
| Record Production Capability | Capable of producing records meeting audit requirements |
| Responsibility Boundaries Clear | Clear definitions of who is accountable for what at each Gate |
| Single Approver Confirmed | Each Gate has only one Approver identified |

---

## Document Control and Review {#document-control}

### Document Version Information

- **Version**: 1.2
- **Effective Date**: 2026-01-21
- **Owner**: System Design Governance Function
- **Approved By**: Engineering Management
- **Review Cycle**: At least once per year, or upon major governance changes

### Document Revision and Change Management

Revision process for this document: Change proposal → Impact assessment → Stakeholder review → Engineering Management approval and publication

**Major Revisions** (require re-approval): Changes to Gate definitions or blocking conditions, changes to responsibility attribution or Approval Authority, changes to mandatory requirements or exception handling mechanism

**Minor Revisions** (notification only): Text clarification or example supplements, appendix content adjustments, formatting or layout adjustments

### Gate Deliverable Version Management Requirements

Each Gate deliverable shall include the following identifiers:

| Identifier Field | Required | Description |
|------------------|----------|-------------|
| Version Number | Yes | Use Major.Minor format |
| Release Date | Yes | ISO format YYYY-MM-DD |
| Document Owner | Yes | Role responsible for document content |
| Review Sign-off Record | Yes | Reviewer, date, sign-off result |
| Change Summary | Required after Gate 2 | Summary of changes in this version |

**Version Number Increment Rules**:

- Major change (v1.x → v2.0): Major design changes approved at Gate 2
- Minor change (v1.0 → v1.1): General design changes approved at Gate 2

**Gate 3 Document Package Version Consistency**: All documents shall reference the same baseline version number. If inconsistent, the reason shall be explained and approved by the Approver. If versions are inconsistent, Gate 3 shall not be released.

### Related Documents

This document, together with the following documents, constitutes the system design governance system:

**Normative Appendices** (Binding, shall be complied with):

- **Appendix A: IEC 62443 Alignment** — Standard alignment mapping and Gate checklists
- **Appendix B: RACI Matrix** — Detailed responsibility assignment matrix for all Gates
- **Appendix C: Residual Risk Template** — Risk matrix, scoring table, threshold definitions (Single Source for risk level rules)
- **Appendix D: Integrated Risk Assessment Templates** — IEC 62443-3-2, FMEA, HAZOP templates and Risk Source ID coding rules

**Informative Appendix** (Reference Only, Non-binding):

- **Appendix E: Design Request Readiness Guideline** — Guidance for Design Requesting Function to assess request readiness (Non-mandatory)

**Internal Control Documents** (Internal to System Design Department, Does not bind external parties):

- **Internal Design Request Intake Criteria** — Internal evaluation criteria for Pre-Gate0 request assessment

**Document Priority**: This document is the authoritative governance reference; normative appendices provide implementation details and shall be complied with. Informative appendices are for reference only. In case of conflict, this main document shall prevail.

---

## References

**Normative References (Mandatory Compliance)**:

- IEC 62443-2-4:2015 - Security program requirements for IACS service providers
- IEC 62443-3-2:2020 - Security risk assessment for system design
- IEC 62443-3-3:2013 - System security requirements and security levels

**Informative References**:

- ISO/IEC 27001:2013 - Information security management systems
- NIST Cybersecurity Framework
- IEC 60812:2018 - Failure modes and effects analysis (FMEA and FMECA)
- IEC 61882:2016 - Hazard and operability studies (HAZOP studies)
- Company internal project management system documents (ISO 9001)

---

**End of Document**
