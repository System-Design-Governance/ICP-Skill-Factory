# AI Review Assistant Configuration

**Project:** {project_name}
**Configuration Name:** {config_name}
**Version:** {version} | **Date:** {date}
**Owner:** {config_owner}

## 1. Review Scope

| Parameter | Setting |
|---|---|
| Document Types | {Design specs, drawings, test reports, procedures} |
| File Formats | {.docx, .pdf, .xlsx, .dwg, .md} |
| Review Stages | {Preliminary / Detailed Design / IFC / As-Built} |
| Excluded Items | {Draft watermarked documents, superseded revisions} |

### Scope Boundaries

| In Scope | Out of Scope |
|---|---|
| Technical content accuracy | Commercial / pricing content |
| Standards compliance | Legal contract terms |
| Cross-reference consistency | Artistic / layout preferences |
| Completeness checks | Subjective engineering judgment |

## 2. Quality Criteria

| Criterion ID | Category | Description | Applicable Doc Types |
|---|---|---|---|
| QC-001 | Completeness | All required sections present per template | All |
| QC-002 | Consistency | Tag names, units, and references match across documents | Design specs, drawings |
| QC-003 | Standards | Correct standard referenced and edition cited | All |
| QC-004 | Formatting | Document numbering, revision, headers per convention | All |
| QC-005 | Technical | Engineering values within expected ranges | Calculations, datasheets |
| QC-006 | Traceability | Requirements traced to design and test references | Specs, test reports |

## 3. Check Rules

| Rule ID | Rule Description | Check Method | Example |
|---|---|---|---|
| CHK-001 | Document number follows naming convention {PRJ}-{DIS}-{SEQ}-{REV} | Regex pattern match | ABC-ELE-001-A |
| CHK-002 | All referenced documents exist in document register | Cross-reference lookup | Reference to non-existent ICD |
| CHK-003 | Engineering units consistent (no mixed metric/imperial) | Unit detection and comparison | kW vs HP in same document |
| CHK-004 | Revision history updated for current revision | Section content check | Rev B document with only Rev A in history |
| CHK-005 | All {placeholder} tags replaced with actual values | Pattern scan for curly braces | Remaining {TBD} or {TBC} |
| CHK-006 | Approval signatures present for issued documents | Signature block completeness | Missing approver on Rev 0 |
| CHK-007 | Cable/tag cross-references match I/O list | Database cross-check | Tag in drawing not in I/O list |

## 4. Severity Classification

| Severity | Definition | Action Required | SLA |
|---|---|---|---|
| Critical | Error that would cause safety risk, regulatory non-compliance, or system malfunction | Must fix before issue | Immediate |
| Major | Significant technical error or omission that impacts design intent | Must fix before next gate | 5 business days |
| Minor | Inconsistency or formatting issue with no functional impact | Fix before final issue | Next revision cycle |
| Observation | Suggestion for improvement, not a defect | Consider for adoption | No deadline |

## 5. Auto-fix Rules

| Rule ID | Condition | Auto-fix Action | Requires Human Confirmation |
|---|---|---|---|
| AF-001 | Date format inconsistent | Normalize to {YYYY-MM-DD} | No |
| AF-002 | Trailing whitespace or extra blank lines | Remove automatically | No |
| AF-003 | {placeholder} text detected | Highlight and flag — do not replace | Yes |
| AF-004 | Missing revision history entry | Add skeleton entry for current rev | Yes |
| AF-005 | Unit abbreviation non-standard | Suggest standard abbreviation | Yes |

## 6. Human Escalation Triggers

| Trigger | Condition | Escalate To |
|---|---|---|
| Safety-related finding | Any Critical severity on safety documents | Lead Engineer + Safety Manager |
| Ambiguous requirement | Requirement text cannot be verified automatically | Document Author |
| Conflicting references | Two referenced documents contradict each other | Design Lead |
| Scope boundary | Finding falls outside defined review scope | Review Coordinator |
| Confidence below threshold | AI confidence < {70%} on a finding | Human Reviewer |

## 7. Report Format

### Report Structure

```
1. Executive Summary
   - Total findings: {n} (Critical: {n}, Major: {n}, Minor: {n}, Observation: {n})
   - Documents reviewed: {n}
   - Review duration: {n} minutes

2. Findings Table
   | Finding ID | Document | Location | Rule | Severity | Description | Suggested Fix |

3. Auto-fix Summary
   | Fix ID | Document | Change Made | Status |

4. Escalation Log
   | Escalation ID | Trigger | Assigned To | Status |

5. Appendix
   - Configuration version used
   - Rules applied
   - Documents in scope
```

### Output Options

| Format | Use Case |
|---|---|
| Markdown | Integration with documentation systems |
| JSON | API consumption and dashboard integration |
| PDF | Formal review record for filing |

## 8. Revision History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | {date} | {author} | Initial configuration |
