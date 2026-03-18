```{=latex}
\newpage
```

# Appendix D: Integrated Risk Assessment Templates

> **IMPORTANT NOTICE**: This English version is provided for reference and external review only. The official governance of record is the zh-TW (Traditional Chinese) version. In case of any discrepancy, the zh-TW version shall prevail.

---

## Purpose {#appD-purpose}

This appendix provides minimum viable templates for Integrated Risk Assessment (IEC 62443-3-2 + FMEA + HAZOP) for use from Gate 1 through Gate 3. Each template defines only the required field structure and does not restrict the tools used (Excel / Word / dedicated systems are all acceptable).

Risk level definitions and acceptance authority follow Chapter 5 of the main document and Appendix C; this appendix does not repeat them.

### Usage Boundary Statement {#appD-usage-boundary}

- This appendix is a **template collection only** and does not constitute a complete risk analysis report
- Gate 3 **does not require** re-executing complete FMEA / HAZOP; only requires that residual risks are traceable to the Risk Source IDs defined in this appendix
- The execution depth (Lite / Full) for each template follows Section 3.2 of the main document; this appendix does not separately define Lite / Full determination rules

---

## IEC 62443-3-2 Zone & Conduit Diagram Template {#appD-zone-conduit}

### Applicable Gates

- **Gate 1**: Design baseline establishment (required deliverable)
- **Gate 2**: Update when changes occur

### Input Sources

- System architecture diagram
- Network topology diagram
- Asset inventory (Gate 0 output)

### Required Fields (Must)

| Field | Description |
|-------|-------------|
| Zone ID | Unique identifier (e.g., Z-001) |
| Zone Name | Zone name |
| Target SL | Target Security Level (SL 1-4) |
| Assets | Asset list within the Zone |
| Conduit ID | Conduit identifier connecting to this Zone |

### Conduit Definition Table

| Field | Description |
|-------|-------------|
| Conduit ID | Unique identifier (e.g., C-001) |
| Source Zone | Source Zone ID |
| Target Zone | Target Zone ID |
| Protocol | Communication protocol |
| Direction | Data flow direction (unidirectional/bidirectional) |

### Optional Fields

- Zone physical location
- Conduit bandwidth constraints
- Backup path description

---

## IEC 62443-3-2 Threat Scenario Template {#appD-threat-scenario}

### Applicable Gates

- **Gate 1**: Threat scenario analysis (part of integrated risk assessment)
- **Gate 2**: Update during change impact assessment

### Input Sources

- Zone & Conduit Diagram (see "IEC 62443-3-2 Zone & Conduit Diagram Template")
- Asset inventory
- FR/SR checklist (Appendix A)

### Required Fields (Must)

| Field | Description |
|-------|-------------|
| Threat ID | Unique identifier, format: **T-XXX** |
| Threat Name | Threat name |
| Target Zone/Conduit | Affected Zone or Conduit ID |
| Threat Source | Threat source (internal/external/supply chain) |
| Attack Vector | Brief attack vector description |
| Affected FR | Affected FR (FR1-FR7) |
| Likelihood | High / Medium / Low |
| Impact | High / Medium / Low |
| Inherent Risk | Critical / High / Medium / Low |

### Optional Fields

- STRIDE classification
- MITRE ATT&CK mapping
- Reference CVE

### Output

- Generated Threat ID serves as Risk Source ID for residual risk register (Appendix C)

---

## FMEA Worksheet Template {#appD-fmea}

### Applicable Gates

- **Gate 1**: Failure mode analysis in integrated risk assessment
- **Gate 2**: Update when design changes occur

### Input Sources

- System component list
- Functional specifications
- Historical failure records (if available)

### Required Fields (Must)

| Field | Description |
|-------|-------------|
| FM ID | Unique identifier, format: **FM-XXX** |
| Component | Component/subsystem name |
| Function | Component function |
| Failure Mode | Failure mode description |
| Failure Effect | Failure effect (local/system/safety) |
| Severity | High / Medium / Low |
| Occurrence | High / Medium / Low |
| Detection | High / Medium / Low (detection difficulty) |
| Risk Level | Critical / High / Medium / Low |

### Scoring Guidance

- **Severity**: Impact of failure on system/safety
- **Occurrence**: Likelihood of failure occurring
- **Detection**: Ability of existing mechanisms to detect failure (High = difficult to detect)
- **Risk Level**: Calculated per Section 5.2 risk matrix of main document

### Optional Fields

- Recommended control measures
- Responsible unit
- Expected improvement timeline

### Output

- Generated FM ID serves as Risk Source ID for residual risk register (Appendix C)

### Governance Consistency Note

Selection between Lite or full FMEA analysis is determined per Section 3.2 of main document and Gate definitions; this appendix does not repeat Lite / Full determination rules.

---

## HAZOP Worksheet Template {#appD-hazop}

### Applicable Gates

- **Gate 1**: Operational deviation analysis in integrated risk assessment
- **Gate 2**: Update when process changes occur

### Input Sources

- Process flow diagrams (P&ID or process descriptions)
- Operating procedures
- Human-machine interface design

### Required Fields (Must)

| Field | Description |
|-------|-------------|
| HAZ ID | Unique identifier, format: **HAZ-XXX** |
| Process Node | Process node/step |
| Parameter | Operating parameter (e.g., flow, temperature, command) |
| Guide Word | Deviation guide word (No/More/Less/Reverse/Other) |
| Deviation | Deviation description |
| Cause | Possible causes |
| Consequence | Deviation consequences |
| Likelihood | High / Medium / Low |
| Severity | High / Medium / Low |
| Risk Level | Critical / High / Medium / Low |

### Standard Guide Word Definitions

| Guide Word | Meaning |
|------------|---------|
| No / None | Complete absence of action or flow |
| More | Parameter too high |
| Less | Parameter too low |
| Reverse | Direction reversed |
| Part of | Only partially completed |
| Other than | Unintended operation |
| Early / Late | Timing deviation |

### Optional Fields

- Existing safeguards
- Recommended improvements
- Responsible unit

### Output

- Generated HAZ ID serves as Risk Source ID for residual risk register (Appendix C)

### Governance Consistency Note

Selection between Lite or full HAZOP analysis is determined per Section 3.2 of main document and Gate definitions; this appendix does not repeat Lite / Full determination rules.

---

## Risk Source ID Encoding Rules {#appD-risk-source-id}

### Encoding Format

| Analysis Method | ID Prefix | Format Example | Description |
|-----------------|-----------|----------------|-------------|
| IEC 62443-3-2 Threat Scenario | T- | T-001, T-042 | Cybersecurity threat scenario |
| FMEA Failure Mode | FM- | FM-001, FM-SYS-003 | Failure mode (may include subsystem code) |
| HAZOP Deviation | HAZ- | HAZ-001, HAZ-P02-D01 | Operational deviation (may include process node code) |
| Threat Modeling (STRIDE) | TM- | TM-001, TM-S-005 | Design-level threat (may include STRIDE category) |

### Encoding Principles

1. **Uniqueness**: IDs shall not be duplicated within the same project
2. **Traceability**: IDs shall be traceable to the original analysis worksheet
3. **Version Control**: Once assigned, IDs shall not be changed; may only be marked as deprecated
4. **Cross-document Reference**: Risk Source ID in residual risk register (Appendix C) shall use this rule

### Gate 3 Traceability Verification

When QA Team performs the 20% spot-check at Gate 3, they shall verify:

- Residual risk's Risk Source ID exists in corresponding analysis worksheet
- Risk Source ID format complies with this section's rules
- Risk level assessment is consistent with original analysis

### Governance Purpose Note

Risk Source ID is for **governance traceability purposes**, used to establish the linkage between residual risks and original analyses. Projects are not required to maintain specific analysis tools or formats; as long as the ID can be traced back to the original analysis record (tool-agnostic).

---

## Document Control {#appD-doc-control}

- **Version**: 1.0
- **Effective Date**: 2026-01-09
- **Owner**: System Design Governance Function
- **Review Cycle**: Synchronized with main document

Revisions to this appendix follow the procedure in Section 6.2 of the main document.

---

**End of Document**
