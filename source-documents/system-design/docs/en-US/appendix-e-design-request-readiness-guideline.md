```{=latex}
\newpage
```

# Appendix E: Design Request Readiness Guideline

> **IMPORTANT NOTICE**: This English version is provided for reference and external review only. The official governance of record is the zh-TW (Traditional Chinese) version. In case of any discrepancy, the zh-TW version shall prevail.

---

## Document Classification {#doc-classification}

**Document Type**: Informative Appendix (Non-normative)

**Important Statement**:

- This document is an **Informative Appendix** (non-normative) to the System Design Governance main document
- This document **does not constitute mandatory compliance requirements** for the Design Requesting Function
- This document provides guidance to help the Design Requesting Function assess whether their design request is ready for Gate 0
- Compliance with this document is voluntary and **does not affect Gate 0 acceptance decision**

---

## Purpose {#purpose}

This document provides guidance for the Design Requesting Function to self-assess the readiness of design requests before formal submission, helping to:

1. Understand the Gate 0 quality thresholds defined in the main document
2. Prepare information that helps the System Design Department assess these thresholds
3. Avoid common issues that lead to "Not Accepted" or "Conditional Acceptance" outcomes
4. Improve request quality and accelerate the acceptance decision process

---

## Quality Threshold Interpretation {#threshold-interpretation}

### Understanding the Main Document's Quality Thresholds

The main document defines four quality thresholds for Gate 0 acceptance decisions. Below is an interpretation to help the Design Requesting Function understand each threshold's meaning:

#### Comprehensibility

**Main Document Definition**: The design request's objectives, scope, and expected outcomes can be understood by the System Design Department

**Self-Assessment Questions**:
- Can I explain the purpose of this design request in one sentence?
- After this design is completed, what can business/users do that they couldn't do before?
- What is the expected outcome of this design?

**Common Issues**:
- Request objectives are too abstract (e.g., "improve system performance")
- Expected outcomes are not defined
- Technical solution is described without explaining the problem being solved

#### Evaluability

**Main Document Definition**: Sufficient information is provided to assess technical feasibility and preliminary risk assumptions

**Self-Assessment Questions**:
- Have I provided enough background for the system design team to understand the technical context?
- Are there known technical constraints or dependencies?
- Are there any special requirements (security, compliance, performance)?

**Common Issues**:
- No information about existing systems or technical environment
- Technical constraints or dependencies not disclosed
- Special requirements not mentioned upfront

#### Accountable Owner

**Main Document Definition**: A clear Design Requesting Function exists who is accountable for the business rationale of the design request

**Self-Assessment Questions**:
- Who has authority to decide the scope and priority of this request?
- Who can confirm the business rationale if asked?
- If requirements change, who is the final confirmer?

**Common Issues**:
- No clear accountable party, multiple stakeholders without decision authority
- Contact person provided but unclear authority
- Business rationale cannot be articulated

#### Scope Stability

**Main Document Definition**: The request's objectives and scope are sufficiently stable to avoid major changes during the design phase

**Self-Assessment Questions**:
- Have the main requirements been confirmed?
- Is there a risk of significant changes?
- Are there pending decisions that could affect scope?

**Common Issues**:
- Requirements still in exploration stage, not stabilized
- Dependent decisions not yet made
- Scope definition uses vague terms (e.g., "and other related functions")

---

## Readiness Self-Assessment Checklist {#self-assessment}

The Design Requesting Function may use the following checklist for self-assessment before formal submission. **This checklist is non-mandatory guidance only**.

### Objective Clarity Check

- [ ] I can explain the purpose of this design request in one sentence
- [ ] I can describe the expected outcome after design completion
- [ ] I can explain the business impact if this design is not done

### Scope Boundary Check

- [ ] I can list the systems/modules/functions included in scope
- [ ] I can list what is explicitly excluded from scope
- [ ] Scope definition does not use vague terms

### Information Completeness Check

- [ ] I have provided known technical constraints
- [ ] I have described existing systems or technical environment
- [ ] I have identified special requirements (security/compliance/performance) if any

### Ownership Clarity Check

- [ ] A clear Design Requesting Function is identified
- [ ] This person has authority over requirement decisions
- [ ] This person can articulate the business rationale

### Scope Stability Check

- [ ] Main requirements have been confirmed
- [ ] No known pending decisions that could significantly affect scope
- [ ] Requirements are not still in exploration stage

---

## Good vs. Poor Request Examples {#examples}

### Example 1: Objective Description

**Poor Example**:
> "We need to improve system performance"

**Issues**: Objective is vague, no specific metrics or expected outcomes

**Good Example**:
> "To meet Q3 business growth projections, we need to improve the order processing system's throughput from current 100 orders/minute to 500 orders/minute, while maintaining response time under 2 seconds"

**Why It's Good**: Has specific metrics, clear business driver, measurable expected outcome

### Example 2: Scope Description

**Poor Example**:
> "Implement user management functionality and other related functions"

**Issues**: "Other related functions" is vague, scope boundary unclear

**Good Example**:
> "Scope includes: user registration, login, password reset, role management. Explicit exclusions: social login integration (planned for Phase 2), single sign-on with external systems (to be assessed separately)"

**Why It's Good**: Clear inclusion list, explicit exclusions, no vague terms

### Example 3: Technical Context

**Poor Example**:
> "Please design a new module"

**Issues**: No context about existing system, no known constraints

**Good Example**:
> "This module needs to integrate with our existing Spring Boot backend (v2.7). Database is PostgreSQL 14, with approximately 1 million user records. Need to comply with company API Gateway standards. Known constraint: cannot modify existing user table structure as it's used by multiple systems"

**Why It's Good**: Technical environment described, known constraints disclosed, integration points identified

---

## Common Pitfalls to Avoid {#pitfalls}

### Pitfall 1: Solution Prescription

**Symptom**: Request specifies technical solution without explaining the problem

**Example**: "Please use microservices architecture to rebuild the user module"

**Better Approach**: First explain the problem (e.g., "Current user module has scalability issues under high load"), then collaborate with the design team on solution options

### Pitfall 2: Scope Creep Language

**Symptom**: Using open-ended language that makes scope unbounded

**Examples**: "and any other necessary functions", "all related improvements", "comprehensive solution"

**Better Approach**: Use explicit lists, mark items as "included" vs "excluded", use "TBD in future phases" for deferred items

### Pitfall 3: Missing Stakeholders

**Symptom**: Starting design process without key stakeholder alignment

**Impact**: Frequent requirement changes during design, wasted design effort

**Better Approach**: Ensure key stakeholders have aligned on scope before submission, document any pending decisions

### Pitfall 4: Unrealistic Timeline Expectations

**Symptom**: Timeline expectations based on wishful thinking rather than scope understanding

**Example**: "This should be a quick change" (without understanding complexity)

**Better Approach**: Provide timeline drivers (e.g., contract deadline, regulatory requirement) rather than duration estimates; let the design team assess complexity

---

## When NOT to Submit {#when-not-to-submit}

Consider delaying submission if:

1. **Still Exploring**: Requirements are still being discussed with stakeholders, not stabilized
2. **Pending Major Decisions**: Key decisions that could significantly affect scope are pending
3. **No Clear Owner**: Cannot identify who is accountable for the business rationale
4. **Cannot Articulate Purpose**: Unable to explain in one sentence why this design is needed

In these situations, consider:
- Using Pre-Gate0 consultation to help clarify
- Completing internal alignment before formal submission
- Breaking down a large request into smaller, more stable pieces

---

## Document Control {#doc-control}

- **Version**: 1.0
- **Effective Date**: 2026-01-21
- **Owner**: System Design Governance Function
- **Classification**: Informative Appendix (Non-normative)
- **Review Cycle**: Synchronized with main document

This appendix's revisions follow the procedure in Section 6.2 of the main document. Informative appendix content adjustments are minor revisions and require notification only.

---

**End of Document**
