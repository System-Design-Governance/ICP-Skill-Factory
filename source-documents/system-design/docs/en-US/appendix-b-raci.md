```{=latex}
\newpage
\begin{landscape}
\pagestyle{landscapepage}
\enableLandscapeHeaderFooter
```

# Appendix B: RACI Matrix

> **IMPORTANT NOTICE**: This English version is provided for reference and external review only. The official governance of record is the zh-TW (Traditional Chinese) version. In case of any discrepancy, the zh-TW version shall prevail.

---

## Introduction {#appB-introduction}

This appendix defines the responsibility assignment for each role in the System Design Governance process.

**RACI Code Definitions**:
- **R** (Responsible): Performs the activity
- **A** (Accountable): Ultimate owner, bears responsibility for outcomes
- **C** (Consulted): Provides input and opinions
- **I** (Informed): Notified of results

### Governance Position {#appB-governance-position}

This RACI Matrix serves as the execution-level responsibility mapping table for the main document "System Design Governance", with the following purposes:

- **Gate Review Responsibility Determination**: Clarifies the Approver, Accountable party, and participants for each Gate
- **Design Delivery Responsibility Transfer**: Defines responsibility boundaries at Gate 3 handover
- **Risk Acceptance and Audit Evidence**: Distinguishes design responsibility from risk ownership
- **Dispute Resolution Basis**: When responsibility attribution is disputed, this appendix serves as the determination basis

All role and activity definitions in this appendix are governed by Chapter 3 (Design Gates), Chapter 4 (Roles & Accountability), and Chapter 5 (Risk Acceptance) of the main document.

---

### Approver Uniqueness Principle {#appB-approver-principle}

**Each Gate has only one Approver**; this is a core principle of this governance framework. The role marked **A** in the RACI table is the sole Approver for that Gate, bearing ultimate responsibility for the passage decision.

**Regarding Authorization and Delegation**:

1. **Authorization relationships do not appear in the RACI table**: If the Approver delegates review execution to another party per organizational authorization, such authorization arrangements are internal organizational matters and do not change the responsibility attribution shown in the RACI table.

2. **Responsibility is not diluted by delegation**: Regardless of whether delegation occurs, ultimate responsibility for Gate passage remains with the Approver shown in the RACI table.

3. **Table marking principle**: The RACI table only marks "responsibility attribution," not "execution method" or "authorization arrangements."

---

## Gate-based RACI Matrix {#appB-gate-raci}

### Gate 0: Project Initiation Review (Project Initiation & Feasibility) {#appB-gate0}

```{=latex}
\begin{tabularx}{\linewidth}{|L{5.5cm}|Z|Z|Z|Z|Z|Z|Z|}
\hline
\textbf{Activity} & \textbf{System Architect} & \textbf{Security Team} & \textbf{QA Team} & \textbf{Project Manager} & \textbf{Design Requesting Function} & \textbf{Risk Acceptance Authority} & \textbf{Engineering Management} \\
\hline
Design request submission and confirmation & C & I & I & C & R/A & - & I \\
\hline
Technical feasibility assessment & R/A & C & I & C & C & - & I \\
\hline
Preliminary risk register establishment & R & R & I & C & I & - & I \\
\hline
Risk assessment strategy definition & R/A & C & I & I & I & - & I \\
\hline
Target SL level proposal & R & R & I & I & I & - & I \\
\hline
\textbf{Gate 0 Review \& Approval} & R & C & I & C & C & - & \textbf{A} \\
\hline
\end{tabularx}
```

### Gate 1: Design Baseline Establishment (Design Baseline & Risk Identification) {#appB-gate1}

```{=latex}
\begin{tabularx}{\linewidth}{|L{5.5cm}|Z|Z|Z|Z|Z|Z|Z|}
\hline
\textbf{Activity} & \textbf{System Architect} & \textbf{Security Team} & \textbf{QA Team} & \textbf{Project Manager} & \textbf{Design Requesting Function} & \textbf{Risk Acceptance Authority} & \textbf{Engineering Management} \\
\hline
Design baseline document preparation & R/A & C & C & I & I & - & I \\
\hline
Integrated risk assessment (IEC 62443-3-2 + FMEA + HAZOP) & R/A & R & C & I & I & - & I \\
\hline
Zone \& Conduit Diagram & R/A & R & I & I & I & - & I \\
\hline
IEC 62443 alignment checklist & R & R/A & C & I & I & - & I \\
\hline
Requirements traceability matrix & R/A & C & R & I & C & - & I \\
\hline
\textbf{Gate 1 Review \& Approval} & R & R & R & I & I & - & \textbf{A} \\
\hline
\end{tabularx}
```

### Gate 2: Design Change Management (Design Change & Deviation Control) {#appB-gate2}

```{=latex}
\begin{tabularx}{\linewidth}{|L{5.5cm}|Z|Z|Z|Z|Z|Z|Z|}
\hline
\textbf{Activity} & \textbf{System Architect} & \textbf{Security Team} & \textbf{QA Team} & \textbf{Project Manager} & \textbf{Design Requesting Function} & \textbf{Risk Acceptance Authority} & \textbf{Engineering Management} \\
\hline
Requirement change confirmation & C & I & I & C & R/A & - & I \\
\hline
Change description and impact analysis & R/A & C & C & I & C & - & I \\
\hline
Risk assessment update & R/A & R & C & I & I & - & I \\
\hline
Design document version update & R/A & I & C & I & I & - & I \\
\hline
SL level impact assessment & R & R/A & I & I & I & - & C \\
\hline
\textbf{Gate 2 Review \& Approval} & R & C & C & I & I & - & \textbf{A} \\
\hline
\end{tabularx}
```

### Gate 3: Design Delivery and Responsibility Transfer (Design Handover & Risk Transfer) {#appB-gate3}

```{=latex}
\begin{tabularx}{\linewidth}{|L{5.5cm}|Z|Z|Z|Z|Z|Z|Z|}
\hline
\textbf{Activity} & \textbf{System Architect} & \textbf{Security Team} & \textbf{QA Team} & \textbf{Project Manager} & \textbf{Design Requesting Function} & \textbf{Risk Acceptance Authority} & \textbf{Engineering Management} \\
\hline
Final design package preparation & R/A & C & R & I & I & I & I \\
\hline
Residual risk register compilation & R/A & R & C & I & I & C & I \\
\hline
Residual risk traceability verification (20\% spot-check) & C & C & R/A & I & I & I & I \\
\hline
\textbf{Residual risk acceptance sign-off} & I & C & I & R & I & \textbf{A} & C (Critical Risk) \\
\hline
Handover meeting convening and recording & R & I & I & R & I & R & I \\
\hline
\textbf{Gate 3 Review \& Approval} & R & C & R & I & I & I & \textbf{A} \\
\hline
\end{tabularx}
```

---

## RACI Rules {#appB-rules}

### Single Accountable Principle {#appB-single-accountable}

- **Each Gate has only one Approver (A)**: Prevents diffusion of authority, ensures someone bears ultimate responsibility for Gate passage
- **Multiple Responsible (R) and Consulted (C) allowed**: Execution and consultation can be shared among multiple parties
- **R/A combined notation**: Indicates the role both performs and bears ultimate responsibility (common for System Architect's design outputs)

### Gate 3 Special Rules {#appB-gate3-special}

- **Risk Acceptance and Gate Approval shall be separated**:
  - Residual risk acceptance: By Risk Acceptance Authority (per Section 5.2 of main document tiering)
  - Gate 3 passage: By System Design Governance Function
- **Reason for separation**: Risk bearer and design reviewer have different responsibilities and shall not be held by the same role

### QA Team Role Constraints {#appB-qa-constraints}

- QA Team shall not serve as Approver for any Gate
- QA Team may only serve as Responsible (performing review) or Consulted (providing opinions)
- QA Team's traceability verification is an independent review; results are for Approver reference

---

## Role Definitions {#appB-role-definitions}

### System Architect {#appB-role-architect}

**Scope of Responsibility**:
- Accountable for design content correctness and risk disclosure completeness
- Accountable for all design documents
- Participates in all reviews from Gate 0 through Gate 3

**Responsibility Boundaries**:
- **Shall not** accept residual risks on behalf of the project execution unit
- **Shall not** serve as Gate Approver (only Responsible)
- After Gate 3, design responsibility transfers to the project execution unit

### Security Team {#appB-role-security}

**Scope of Responsibility**:
- Responsible for security requirement definition, threat modeling, IEC 62443 alignment verification
- Performs cybersecurity threat identification portion of integrated risk assessment
- Reviews security control measure effectiveness

**Responsibility Boundaries**:
- **Shall not** determine SL level independently (shall collaborate with System Architect)
- **Shall not** accept risks on behalf of Risk Acceptance Authority

### QA Team {#appB-role-qa}

**Scope of Responsibility**:
- Responsible for design document completeness and traceability review
- Performs Gate 3 residual risk traceability verification (at least 20% spot-check)
- Verifies version consistency

**Responsibility Boundaries**:
- **Shall not** serve as Approver for any Gate
- **Shall not** accept risks or approve design passage
- Review results are advisory; final decisions rest with Approver

### Project Manager {#appB-role-pm}

**Scope of Responsibility**:
- Responsible for overall project coordination and governance process compliance
- Manages stakeholder communication and meeting convening
- Co-signatory for Gate 3 handover meeting

**Responsibility Boundaries**:
- **Shall not** approve design Gate passage (unless explicitly authorized in main document)
- **May** serve as Risk Acceptance Authority for Low/Medium Risk (per Section 5.2 of main document)
- Accountable for process compliance, not accountable for design content correctness

### Design Requesting Function {#appB-role-drf}

**Scope of Responsibility**:
- The sole legitimate source for design request submission
- Accountable for the business purpose, operational necessity, or strategic rationale of design requests
- Confirms the reasonableness of requirement changes

**RACI Roles**:
- **Gate 0**: Design request submission and confirmation (R/A), Technical feasibility assessment and review (C)
- **Gate 1**: Requirements traceability matrix review (C)
- **Gate 2**: Requirement change confirmation (R/A), Change impact analysis (C)
- **Gate 3**: Does not participate

**Responsibility Boundaries**:
- **Shall not** serve as Approver for Gate 1 through Gate 3
- **Shall not** bear technical decision responsibility for design solutions, security architecture, or risk controls
- **Shall not** participate in design content review (only provides confirmation on requirement scope and business rationale)

**Role Mapping**: Depending on organizational structure, this may be filled by Business Owner, Product Owner, Requirement Owner, or an authorized project sponsor.

**Relationship with Business Owner**:

- **Business Owner as DRF**: When Business Owner serves as the Design Requesting Function, they are responsible for design request submission and business rationale confirmation (Gate 0, Gate 2)
- **Business Owner as RAA**: When Business Owner participates in Risk Acceptance Authority (High Risk scenarios), they are responsible for residual risk acceptance sign-off (Gate 3)
- **No Role Confusion**: When the same person exercises different responsibilities at different times, sign-off records shall be maintained separately, and DRF duties shall not be exercised in place of RAA duties

### Risk Acceptance Authority {#appB-role-raa}

**Scope of Responsibility**:
- Appears only at Gate 3, responsible for residual risk acceptance sign-off
- Tiered per Section 5.2 of main document:
  - Low Risk: Project Manager
  - Medium Risk: Project Manager + Security Lead
  - High Risk: Project Manager + Security Lead + Business Owner
  - Critical Risk: Escalation to Engineering Management required, with additional mitigation plan

**Responsibility Boundaries**:
- **Not equivalent to** Gate Approver (Gate passage and risk acceptance are different decisions)
- After risk acceptance, consequences of that risk are borne by the accepting party
- **Shall not** be held by System Architect or System Design Governance Function

### Engineering Management {#appB-role-engmgmt}

**Scope of Responsibility**:
- Approver for Gate 0 and Gate 2
- Delegates Gate 1 and Gate 3 passage to System Design Governance Function
- Final decision maker for dispute escalation
- Approves additional mitigation plans for Critical Risk

**Responsibility Boundaries**:
- Accountable for resource allocation and project initiation decisions
- Not directly accountable for design technical content (System Architect is accountable)

---

## Escalation Path {#appB-escalation}

When cross-departmental responsibility attribution is disputed, follow this escalation path (per Section 4.3 of main document):

| Level | Participants | Time Limit | Description |
|-------|--------------|------------|-------------|
| Level 1 | System Architect + Project Manager + QA Team | 3 business days | Team-level negotiation, attempt technical resolution |
| Level 2 | System Design Governance Function | 5 business days | Department-level arbitration, determination based on main document |
| Level 3 | Engineering Management | 10 business days | Management final decision |

**Gate Correspondence Notes**:
- Disputes typically occur at **Gate 1** (design baseline scope) and **Gate 3** (residual risk acceptance)
- During dispute period, the Gate is considered "not passed"; project shall not proceed to next phase
- Exception scenario: If involving "emergency security patch" (Section 2.2.1 of main document), exception mechanism may be initiated in parallel

---

## Communication Matrix {#appB-communication}

| Information | Frequency | Format | Owner | Recipients |
|-------------|-----------|--------|-------|-----------|
| Design Requirement Specification | Gate 0 | Requirement Document | Design Requesting Function | System Architect, Project Manager |
| Gate Review Record | Per Gate | Meeting minutes | System Design Governance Function | All roles |
| Integrated Risk Assessment Report | Gate 1 / Gate 2 | Report | System Architect | Security Team, QA Team, Engineering Management |
| Residual Risk Register | Gate 3 | Register (Appendix C template) | System Architect | Risk Acceptance Authority, QA Team |
| Design Handover Meeting Minutes | Gate 3 | Meeting minutes | Project Manager | System Architect, Project Execution Unit |
| Design Change Notice | As needed | Change Record | System Architect | Security Team, QA Team, Engineering Management, Design Requesting Function |
| Requirement Change Confirmation | As needed | Confirmation Record | Design Requesting Function | System Architect, Project Manager |

---

## Document Control {#appB-doc-control}

- **Version**: 1.0
- **Effective Date**: 2026-01-08
- **Owner**: System Design Governance Function
- **Review Cycle**: Synchronized with main document

Revisions to this appendix follow the procedure in Section 6.2 of the main document.

---

**End of Document**

```{=latex}
\disableLandscapeHeaderFooter
\end{landscape}
\pagestyle{fancy}
```
