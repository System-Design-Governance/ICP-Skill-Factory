# Internal Design Request Intake Criteria

> **IMPORTANT NOTICE**: This English version is provided for reference and external review only. The official governance of record is the zh-TW (Traditional Chinese) version. In case of any discrepancy, the zh-TW version shall prevail.

---

## Document Classification {#doc-classification}

**Document Type**: Internal Control Document

**Important Statement**:

- This document is **NOT** part of the System Design Governance main document or its normative appendices
- This document serves as **internal operational guidance** for the System Design Department to assess the readiness of Pre-Gate0 requests
- The criteria in this document **do not constitute submission obligations for external parties**
- The Design Requesting Function is not bound by this document; their obligations are defined in the main document

---

## Purpose {#purpose}

This document provides internal evaluation criteria for the System Design Department to assess design request intake, helping the team to:

1. Evaluate whether Pre-Gate0 requests meet the quality thresholds for entering Gate 0 review
2. Identify supplementary information needed to assist the Design Requesting Function in preparation
3. Provide consistent evaluation standards to reduce subjective judgment variations

---

## Intake Evaluation Rubric {#evaluation-rubric}

### Evaluation Dimensions and Guidelines

The following evaluation dimensions correspond to the Gate 0 quality thresholds defined in the main document (Comprehensibility, Evaluability, Accountable Owner, Scope Stability).

#### Dimension 1: Request Objective Clarity (Corresponds to: Comprehensibility)

| Rating | Description |
|--------|-------------|
| ✅ Sufficient | Request objective is clear, expected outcome can be described, team can understand what the design needs to achieve |
| ⚠️ Partial | Request objective is generally understandable, but some details need clarification |
| ❌ Insufficient | Request objective is vague, team cannot understand what needs to be designed |

**Supplementary Suggestions** (if rated "Partial" or "Insufficient"):
- Ask DRF: "After this design is completed, what can business/users do that they couldn't do before?"
- Ask DRF: "What would be the impact if this design is not done?"

#### Dimension 2: Scope Boundary Identifiability (Corresponds to: Evaluability + Scope Stability)

| Rating | Description |
|--------|-------------|
| ✅ Sufficient | Design scope has clear boundaries, clear what is in scope and what is out of scope |
| ⚠️ Partial | Scope is generally identifiable, but boundaries are vague or still changing |
| ❌ Insufficient | Scope is completely uncertain, or still in exploration stage |

**Supplementary Suggestions** (if rated "Partial" or "Insufficient"):
- Ask DRF: "What systems/modules/functions does this request cover?"
- Ask DRF: "What is explicitly not in scope for this design?"

#### Dimension 3: Stakeholders and Requirement Owner (Corresponds to: Accountable Owner)

| Rating | Description |
|--------|-------------|
| ✅ Sufficient | Clear Design Requesting Function exists who is accountable for business rationale of the request |
| ⚠️ Partial | Contact person exists but responsibilities unclear, or authorization not confirmed |
| ❌ Insufficient | No clear requirement owner, or multiple parties without decision authority |

**Supplementary Suggestions** (if rated "Partial" or "Insufficient"):
- Confirm: "Who has authority to decide the scope and priority of this request?"
- Confirm: "If requirements change, who is the final confirmer?"

#### Dimension 4: Technical and Risk Information (Corresponds to: Evaluability)

| Rating | Description |
|--------|-------------|
| ✅ Sufficient | Sufficient information provided for preliminary technical feasibility assessment and risk identification |
| ⚠️ Partial | Some information available, but insufficient to identify main risk assumptions |
| ❌ Insufficient | Extremely insufficient information, cannot perform any technical assessment |

**Supplementary Suggestions** (if rated "Partial" or "Insufficient"):
- Ask: "What are the known technical constraints or dependencies?"
- Ask: "Are there any special security, compliance, or performance requirements?"
- Ask: "Are there existing systems or interfaces that need to be integrated?"

#### Dimension 5: Urgency and Driving Factors (Auxiliary Assessment)

| Rating | Description |
|--------|-------------|
| ✅ Sufficient | Clear timeline driving factors exist (e.g., contract, regulation, business commitment) |
| ⚠️ Partial | Timeline expectations exist but driving factors unclear |
| ❌ Insufficient | No timeline information or "as soon as possible" without concrete basis |

**Supplementary Suggestions** (if rated "Partial" or "Insufficient"):
- Ask: "Are there external timeline constraints (contract, regulation, business)?"
- Ask: "What are the consequences of delay?"

---

## Intake Decision Matrix {#decision-matrix}

### Evaluation Result Determination

| Dimensions 1-4 Rating Combination | Recommended Decision |
|---------------------------------|---------------------|
| All ✅ | **May enter Gate 0 review** |
| Contains 1-2 ⚠️, no ❌ | **Conditional entry**: List items to supplement, may enter Gate 0 after DRF supplements |
| Contains ❌ | **Remain in Pre-Gate0 clarification**: Assist DRF in clarification, re-evaluate after improvement |

### Legitimate Reasons for Refusing Intake (Internal Reference)

The following scenarios may serve as legitimate reasons for refusing entry to Gate 0 review:

- Cannot identify Design Requesting Function
- Request objective cannot be understood by the team
- Scope is still in exploration stage, not stabilized
- Information insufficient to identify any basic risk assumptions
- Requesting party cannot answer "what would happen if this is not done"

---

## Request Submission Template (Optional) {#submission-template}

**Usage Instructions**: The following template is an **internal auxiliary tool** for the System Design Department to suggest to DRF for reference use. It **does not constitute external submission obligations**.

### Design Request Information Summary

```
1. Request Title: _______________

2. Request Objective:
   - What problem is this design solving?
   - What can be achieved after completion?

3. Scope Description:
   - What systems/modules/functions are covered?
   - What is explicitly not in scope?

4. Design Requesting Function:
   - Name/Unit: _______________
   - Accountable for business rationale: ☐ Yes

5. Known Constraints and Dependencies:
   - Technical constraints:
   - Security/Compliance requirements:
   - Dependent systems/interfaces:

6. Timeline and Driving Factors:
   - Expected completion time:
   - Driving factors (contract/regulation/business):
   - Impact of delay:

7. Supplementary Information:
   - Reference documents/existing designs:
   - Related contacts:
```

---

## Clarification vs. Rejection {#clarification-vs-rejection}

### Internal Behavior Guidelines

| Scenario | Recommended Behavior |
|----------|---------------------|
| DRF actively cooperates, information gradually supplemented | Continue to assist clarification, enter Gate 0 when ready |
| DRF cannot provide key information but not unwilling | Help identify information sources, suggest phased clarification |
| DRF refuses to provide basic information | Document communication process, formally notify cannot enter Gate 0 |
| Requirements continue to change, cannot stabilize | Suggest waiting until requirements stabilize before resubmitting |

### Suggested Communication Phrasing

**When assisting clarification**:
> "To help us more accurately evaluate this request, could you please supplement the following information: ..."

**When refusing entry to Gate 0**:
> "The information currently provided is not yet sufficient for a formal technical feasibility assessment. We suggest supplementing the following content before resubmitting for Gate 0 review: ..."

---

## Document Control {#doc-control}

- **Version**: 1.0
- **Effective Date**: 2026-01-21
- **Owner**: System Design Governance Function
- **Classification**: Internal Control Document (Non-normative Appendix)
- **Review Cycle**: Adjusted as per internal operational needs

**Revision Note**: Revisions to this document do not need to follow the formal procedure in Section 6.2 of the main document; managed internally by the System Design Department.

---

**End of Document**
