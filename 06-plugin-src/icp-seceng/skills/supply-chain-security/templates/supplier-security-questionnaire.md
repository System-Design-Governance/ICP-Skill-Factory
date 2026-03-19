# OT Vendor / Supplier Security Questionnaire

| Field | Value |
|-------|-------|
| Vendor Company Name | {vendor_name} |
| Product / Service | {product_or_service} |
| Questionnaire Completed By | {respondent_name, title} |
| Date | {date} |
| ICP Project Reference | {project_id} |

## Section 1: Company Information

| # | Question | Response |
|---|----------|----------|
| 1.1 | Company legal name and headquarters location | {response} |
| 1.2 | Number of employees (total and in security roles) | {response} |
| 1.3 | Primary contact for security inquiries | {name, email, phone} |
| 1.4 | Countries where development/manufacturing occurs | {response} |
| 1.5 | Subcontractors used for development or components | {response} |

## Section 2: Security Certifications

| # | Question | Response | Evidence |
|---|----------|----------|----------|
| 2.1 | Is your organization certified to IEC 62443-4-1 (Secure Product Development Lifecycle)? | Yes / No / In Progress | {cert_number} |
| 2.2 | Are your products certified to IEC 62443-4-2 (Component Security)? | Yes / No / In Progress | {cert_number, SL achieved} |
| 2.3 | Do you hold ISO 27001 certification? | Yes / No / In Progress | {cert_number} |
| 2.4 | Do you hold SOC 2 Type II or equivalent? | Yes / No | {report_date} |
| 2.5 | Other relevant certifications (Common Criteria, FIPS, etc.)? | {response} | {details} |

## Section 3: Secure Development Lifecycle (SDL)

| # | Question | Response |
|---|----------|----------|
| 3.1 | Do you follow a documented secure development lifecycle? | Yes / No |
| 3.2 | Do you perform threat modeling during design phase? | Yes / No |
| 3.3 | Do you perform static and dynamic code analysis? | Yes / No |
| 3.4 | Do you perform penetration testing before release? | Yes / No |
| 3.5 | Do you use a Software Bill of Materials (SBOM) for your products? | Yes / No |
| 3.6 | What SBOM format do you use? (SPDX, CycloneDX, other) | {response} |
| 3.7 | Do you scan for known vulnerabilities in third-party components? | Yes / No |

## Section 4: Vulnerability Disclosure and Management

| # | Question | Response |
|---|----------|----------|
| 4.1 | Do you have a public vulnerability disclosure policy? | Yes / No |
| 4.2 | URL of vulnerability disclosure page | {url} |
| 4.3 | Average time from vulnerability report to advisory publication | {days} |
| 4.4 | Average time from advisory to patch availability | {days} |
| 4.5 | Do you publish CVEs for identified vulnerabilities? | Yes / No |
| 4.6 | Do you participate in ICS-CERT coordinated disclosure? | Yes / No |

## Section 5: Patch Management

| # | Question | Response |
|---|----------|----------|
| 5.1 | How frequently do you release security patches? | {schedule} |
| 5.2 | Do you provide patch impact assessments for OT environments? | Yes / No |
| 5.3 | Do you test patches against OT operational scenarios? | Yes / No |
| 5.4 | Do you support automated patch deployment? | Yes / No |
| 5.5 | What is your patch notification mechanism? | {email, portal, RSS, etc.} |

## Section 6: End-of-Life (EOL) Policy

| # | Question | Response |
|---|----------|----------|
| 6.1 | What is the minimum supported product lifecycle? | {years} |
| 6.2 | How much advance notice is given before EOL? | {months} |
| 6.3 | Do you provide security patches during extended support? | Yes / No |
| 6.4 | Do you provide migration paths to successor products? | Yes / No |
| 6.5 | What is your data/configuration migration support? | {response} |

## Section 7: Supply Chain Integrity

| # | Question | Response |
|---|----------|----------|
| 7.1 | Do you verify the integrity of components from your suppliers? | Yes / No |
| 7.2 | Do you use hardware root of trust or secure boot? | Yes / No |
| 7.3 | Do you sign firmware and software updates cryptographically? | Yes / No |
| 7.4 | Do you perform background checks on development staff? | Yes / No |
| 7.5 | Do you have anti-counterfeit measures for hardware? | Yes / No |

## Scoring Summary

| Section | Max Score | Vendor Score | Notes |
|---------|----------|-------------|-------|
| Certifications | {max} | {score} | {notes} |
| SDL Practices | {max} | {score} | {notes} |
| Vulnerability Management | {max} | {score} | {notes} |
| Patch Management | {max} | {score} | {notes} |
| EOL Policy | {max} | {score} | {notes} |
| Supply Chain Integrity | {max} | {score} | {notes} |
| **Total** | **{max}** | **{score}** | **{risk_rating}** |

**Risk Rating**: {Low / Medium / High / Unacceptable}
**Recommendation**: {Approve / Approve with Conditions / Reject}
**Reviewed By**: {reviewer_name} | Date: {date}
