# Threat & Risk Assessment Report

| Field | Value |
|-------|-------|
| Project | {project_name} |
| Facility / Site | {facility_name} |
| Assessment Date | {date} |
| Assessor(s) | {assessor_names} |
| Standard Reference | IEC 62443-3-2 |
| Document Revision | {revision} |

## 1. Scope

- **Systems in Scope**: {list of systems, zones, and conduits assessed}
- **Exclusions**: {any systems or areas explicitly excluded}
- **Assessment Boundary**: {physical and logical boundary description}

## 2. Asset Inventory

| Asset ID | Name | Type | Zone | Criticality | Owner |
|----------|------|------|------|-------------|-------|
| {id} | {name} | PLC / HMI / Server / Switch | {zone} | Critical / High / Medium / Low | {owner} |

## 3. Threat Catalog (STRIDE)

| Threat ID | STRIDE Category | Threat Description | Applicable Assets | Likelihood |
|-----------|----------------|--------------------|--------------------|------------|
| T-001 | Spoofing | {description} | {asset_ids} | {1-5} |
| T-002 | Tampering | {description} | {asset_ids} | {1-5} |
| T-003 | Repudiation | {description} | {asset_ids} | {1-5} |
| T-004 | Info Disclosure | {description} | {asset_ids} | {1-5} |
| T-005 | Denial of Service | {description} | {asset_ids} | {1-5} |
| T-006 | Elev. of Privilege | {description} | {asset_ids} | {1-5} |

## 4. Vulnerability Assessment

| Vuln ID | Description | Affected Asset | CVE (if any) | Exploitability | Current Mitigation |
|---------|-------------|----------------|--------------|----------------|--------------------|
| V-001 | {description} | {asset_id} | {cve} | {1-5} | {existing control} |

## 5. Risk Matrix (5x5)

| | Impact 1 (Negligible) | Impact 2 (Minor) | Impact 3 (Moderate) | Impact 4 (Major) | Impact 5 (Catastrophic) |
|---|---|---|---|---|---|
| **Likelihood 5 (Almost Certain)** | Medium | High | High | Critical | Critical |
| **Likelihood 4 (Likely)** | Low | Medium | High | High | Critical |
| **Likelihood 3 (Possible)** | Low | Medium | Medium | High | High |
| **Likelihood 2 (Unlikely)** | Low | Low | Medium | Medium | High |
| **Likelihood 1 (Rare)** | Low | Low | Low | Medium | Medium |

### Risk Register

| Risk ID | Threat | Vulnerability | Likelihood | Impact | Risk Rating | Priority |
|---------|--------|---------------|------------|--------|-------------|----------|
| R-001 | {threat_id} | {vuln_id} | {1-5} | {1-5} | {rating} | {1-N} |

## 6. Risk Treatment Plan

| Risk ID | Treatment Option | Proposed Control | Responsible | Target Date | Status |
|---------|-----------------|------------------|-------------|-------------|--------|
| R-001 | Mitigate / Accept / Transfer / Avoid | {control_description} | {owner} | {date} | Planned / In Progress / Complete |

## 7. Residual Risk Summary

| Risk ID | Initial Rating | Treatment Applied | Residual Rating | Acceptable (Y/N) |
|---------|---------------|-------------------|-----------------|-------------------|
| R-001 | {initial} | {treatment} | {residual} | {Y/N} |

**Overall Residual Risk Level**: {Low / Medium / High}

**Approval**: {approver_name} | Date: {date} | Signature: ___________
