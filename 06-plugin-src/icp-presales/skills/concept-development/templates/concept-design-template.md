# Concept Design Document

| Field | Value |
|-------|-------|
| Project | {project_name} |
| Client | {client_name} |
| Document ID | {doc_id} |
| Author | {author} |
| Date | {date} |
| Version | {version} |
| Status | Draft / Review / Approved |

## 1. Executive Summary

{2-3 paragraphs summarizing the project need, proposed approach, key benefits, estimated cost range, and timeline. Written for management audience.}

## 2. Current State Assessment

### 2.1 Existing Architecture

{Description of client's current OT/ICS architecture, including network topology, control systems, and security posture. Reference site assessment if available.}

### 2.2 Identified Gaps and Risks

| # | Gap / Risk | Impact | Priority |
|---|-----------|--------|----------|
| 1 | {description} | {safety / operational / compliance} | {High / Medium / Low} |
| 2 | {description} | {impact} | {priority} |

### 2.3 Regulatory and Standards Requirements

- {IEC 62443 requirements applicable to this project}
- {Industry-specific regulations (NERC CIP, NIS2, etc.)}
- {Client-specific policies or standards}

## 3. Proposed Architecture

### 3.1 Zone and Conduit Design

| Zone ID | Zone Name | Purdue Level | SL-T | Key Assets | Description |
|---------|-----------|-------------|------|------------|-------------|
| Z-01 | {name} | {level} | SL-{n} | {assets} | {description} |
| Z-02 | {name} | {level} | SL-{n} | {assets} | {description} |

| Conduit ID | Source Zone | Dest Zone | Protocols | Security Controls |
|-----------|-----------|-----------|-----------|-------------------|
| C-01 | Z-01 | Z-02 | {protocols} | {firewall, IDS, data diode} |

### 3.2 Architecture Diagram

{Reference to architecture diagram file or embed description of logical/physical layout.}

### 3.3 Key Design Decisions

| # | Decision | Rationale | Alternatives Considered |
|---|----------|-----------|------------------------|
| 1 | {decision} | {rationale} | {alternatives} |
| 2 | {decision} | {rationale} | {alternatives} |

## 4. Technology Selection

| Component | Recommended Product | Vendor | Justification |
|-----------|-------------------|--------|---------------|
| Firewall (IT/OT boundary) | {product} | {vendor} | {reason} |
| IDS/IPS (OT network) | {product} | {vendor} | {reason} |
| SIEM | {product} | {vendor} | {reason} |
| Endpoint protection | {product} | {vendor} | {reason} |
| Remote access | {product} | {vendor} | {reason} |
| Backup solution | {product} | {vendor} | {reason} |

## 5. High-Level Bill of Materials

| # | Item | Description | Qty | Unit Cost | Extended Cost |
|---|------|-------------|-----|-----------|---------------|
| 1 | {item} | {description} | {qty} | {cost} | {total} |
| 2 | {item} | {description} | {qty} | {cost} | {total} |
| | | | | **Subtotal (Equipment)** | **{total}** |
| | | | | **Professional Services** | **{total}** |
| | | | | **Contingency ({%})** | **{total}** |
| | | | | **Grand Total** | **{total}** |

## 6. Implementation Timeline

| Phase | Description | Duration | Dependencies |
|-------|-------------|----------|--------------|
| Phase 1 | {description, e.g., Network segmentation} | {weeks} | {dependencies} |
| Phase 2 | {description, e.g., Security monitoring} | {weeks} | Phase 1 |
| Phase 3 | {description, e.g., Hardening and policies} | {weeks} | Phase 1 |
| Phase 4 | {description, e.g., Testing and handover} | {weeks} | Phase 2, 3 |
| | **Total Duration** | **{weeks}** | |

## 7. Cost Estimate Summary

| Category | Estimated Cost | Confidence |
|----------|---------------|------------|
| Hardware and Software | {amount} | {+/- %}  |
| Professional Services | {amount} | {+/- %} |
| Training | {amount} | {+/- %} |
| Annual Support/Licensing | {amount} | {+/- %} |
| **Total CAPEX** | **{amount}** | |
| **Annual OPEX** | **{amount}** | |

## 8. Assumptions and Constraints

- {assumption or constraint}
- {assumption or constraint}

## 9. Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Sponsor | {name} | ___________ | {date} |
| Technical Lead | {name} | ___________ | {date} |
| Client Representative | {name} | ___________ | {date} |
