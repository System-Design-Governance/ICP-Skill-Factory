```{=latex}
\newpage
```

# Appendix C: Residual Risk Template

> **IMPORTANT NOTICE**: This English version is provided for reference and external review only. The official governance of record is the zh-TW (Traditional Chinese) version. In case of any discrepancy, the zh-TW version shall prevail.

---

## Purpose {#appC-purpose}

This appendix provides standardized templates for residual risk assessment and documentation, ensuring all identified risks undergo appropriate assessment and acceptance processes. This template is used for compiling the residual risk register at Gate 3 design delivery and serves as evidence documentation for IEC 62443 compliance audits.

---

## Risk Assessment Process {#appC-process}

### Risk Analysis Input Sources {#appC-input-sources}

Residual risks in this governance framework shall originate from the following approved risk analysis methods:

| Analysis Method | Identification Scope | Risk Source ID Format |
|-----------------|---------------------|----------------------|
| **IEC 62443-3-2** | Cybersecurity threats, Zone/Conduit boundary risks | T-XXX |
| **FMEA** | System/component failure modes | FM-XXX |
| **HAZOP** | Operational process deviations | HAZ-XXX |
| **Threat Modeling (e.g., STRIDE)** | Design-level cybersecurity threats | TM-XXX |

**Important Notes**:
- Each residual risk shall have a Risk Source ID for traceability to the original analysis document
- Risk items that cannot be traced to the above sources are considered invalid risk records; Gate 3 shall not be approved
- For execution steps, templates, and scoring methods of each analysis method, refer to **Appendix D: Integrated Risk Assessment Templates**

### Assessment Flow {#appC-assessment-flow}

1. **Threat Identification**: Output from the above analysis methods
2. **Inherent Risk Assessment**: Assessment before controls
3. **Control Measures Definition**: Define mitigation actions
4. **Residual Risk Calculation**: Risk remaining after controls
5. **Risk Acceptance Decision**: Accept/Mitigate/Transfer/Avoid

---

## Residual Risk Register Template {#appC-register-template}

### Risk ID: [RR-001]

#### Basic Information

| Field | Content |
|-------|---------|
| **Risk Title** | [Brief risk description] |
| **Risk Source ID** | [T-XXX / FM-XXX / HAZ-XXX / TM-XXX] |
| **Analysis Method** | [IEC 62443-3-2 / FMEA / HAZOP / Threat Modeling] |
| **Risk Owner** | [Responsible person] |
| **Date Identified** | [YYYY-MM-DD] |
| **Last Updated** | [YYYY-MM-DD] |

#### Threat Description

[Detailed description of the threat scenario, including attack vectors, failure modes, operational deviations, etc., depending on the Analysis Method]

#### Inherent Risk Assessment

| Factor | Rating | Justification |
|--------|--------|---------------|
| Likelihood | High / Medium / Low | [Rationale for likelihood rating] |
| Impact | High / Medium / Low | [Rationale for impact rating] |
| **Inherent Risk Level** | **Critical / High / Medium / Low** | [Combined assessment result] |

#### Implemented Controls

1. **Control 1**: [Control measure description]
   - Type: Preventive / Detective / Corrective
   - Effectiveness: High / Medium / Low

2. **Control 2**: [Control measure description]
   - Type: Preventive / Detective / Corrective
   - Effectiveness: High / Medium / Low

#### Residual Risk Assessment

| Factor | Rating | Justification |
|--------|--------|---------------|
| Likelihood (after controls) | High / Medium / Low | [Likelihood after applying controls] |
| Impact (after controls) | High / Medium / Low | [Impact after applying controls] |
| **Residual Risk Level** | **Critical / High / Medium / Low** | [Final residual risk level] |

#### Risk Treatment Decision

- [ ] Accept: Accept residual risk
- [ ] Mitigate: Additional mitigation measures required
- [ ] Transfer: Transfer risk (e.g., insurance)
- [ ] Avoid: Avoid risk (change design)

**Decision Rationale**: [Explanation of decision rationale]

#### Acceptance Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Risk Owner | | | |
| Security Lead | | | |
| Project Manager | | | |
| Business Owner | | | |

---

## Risk Matrix {#appC-risk-matrix}

### Likelihood Scale {#appC-likelihood-scale}

- **High**: Expected to occur (probability > 50%)
- **Medium**: Possible to occur (probability 10-50%)
- **Low**: Unlikely to occur (probability < 10%)

### Impact Scale {#appC-impact-scale}

- **High**: Severe impact on system availability, data integrity, or confidentiality
- **Medium**: Moderate impact, recoverable through backup or manual intervention
- **Low**: Minor impact, core functionality unaffected

### Risk Level Matrix {#appC-level-matrix}

|            | **Low Impact** | **Medium Impact** | **High Impact** |
|------------|----------------|-------------------|-----------------|
| **High Likelihood** | Medium | High | Critical |
| **Medium Likelihood** | Low | Medium | High |
| **Low Likelihood** | Low | Low | Medium |

---

## Risk Acceptance Criteria {#appC-acceptance-criteria}

Per Section 5.2 of the main document:

| Risk Level | Acceptance Authority |
|------------|---------------------|
| **Low** | Project Manager |
| **Medium** | Project Manager + Security Lead |
| **High** | Project Manager + Security Lead + Business Owner |
| **Critical** | Engineering Management, with additional mitigation plan required |

---

## Example: Sample Risk Entry {#appC-example}

### Risk ID: RR-001

#### Basic Information

| Field | Content |
|-------|---------|
| **Risk Title** | Unencrypted Internal API Communication |
| **Risk Source ID** | T-012 |
| **Analysis Method** | IEC 62443-3-2 |
| **Risk Owner** | System Architect |
| **Date Identified** | 2026-01-08 |
| **Last Updated** | 2026-01-08 |

#### Threat Description

Internal microservice API communication is unencrypted. If the internal network is compromised, attackers can intercept sensitive data (such as user authentication tokens). This threat was identified in the IEC 62443-3-2 threat scenario analysis (Threat Scenario T-012).

#### Inherent Risk Assessment

| Factor | Rating | Justification |
|--------|--------|---------------|
| Likelihood | Medium | Internal network is isolated but intrusion risk cannot be completely eliminated |
| Impact | High | May lead to authentication bypass and data leakage |
| **Inherent Risk Level** | **High** | Medium likelihood × High impact |

#### Implemented Controls

1. **Control 1**: Internal network isolation and firewall rules
   - Type: Preventive
   - Effectiveness: Medium

2. **Control 2**: Authentication verification at API Gateway layer
   - Type: Detective
   - Effectiveness: Medium

#### Residual Risk Assessment

| Factor | Rating | Justification |
|--------|--------|---------------|
| Likelihood (after controls) | Low | Internal network isolation reduces intrusion likelihood |
| Impact (after controls) | Medium | API Gateway can limit impact scope |
| **Residual Risk Level** | **Low** | Low likelihood × Medium impact |

#### Risk Treatment Decision

- [x] Accept: Accept residual risk

**Decision Rationale**: Considering performance requirements and existing internal network isolation measures, this residual risk is accepted. If risk level increases in the future, mTLS implementation will be evaluated.

---

## Document Control {#appC-doc-control}

- **Version**: 1.0
- **Effective Date**: 2026-01-08
- **Owner**: System Design Governance Function
- **Review Cycle**: Synchronized with main document

Revisions to this appendix follow the procedure in Section 6.2 of the main document.

---

**End of Document**
