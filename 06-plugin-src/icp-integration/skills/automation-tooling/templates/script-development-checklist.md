# Engineering Script Development Checklist

**Script Name:** {script_name}
**Purpose:** {brief_description}
**Author:** {author} | **Date:** {date}
**Language:** {Python / PowerShell / MATLAB / VBA}
**Version:** {version}

## 1. Requirements

- [ ] Functional requirements documented and approved
- [ ] Input data sources identified and accessible
- [ ] Output format and destination defined
- [ ] Performance requirements specified (execution time, memory)
- [ ] Target environment confirmed (OS, runtime version, dependencies)

### Requirements Summary

| Req ID | Description | Priority | Status |
|---|---|---|---|
| REQ-001 | {functional requirement} | {Must / Should / Nice-to-have} | {Draft / Approved} |
| REQ-002 | | | |
| REQ-003 | | | |

## 2. Input Validation

- [ ] All input parameters have defined types and acceptable ranges
- [ ] Missing or null inputs handled gracefully (default value or error)
- [ ] File inputs validated for existence, format, and encoding
- [ ] User-supplied values sanitized (no injection risk)
- [ ] Input size limits defined to prevent memory exhaustion

### Input Specification

| Parameter | Type | Valid Range / Format | Default | Required |
|---|---|---|---|---|
| {param_1} | {float} | {0.0 - 1000.0} | {none} | {Yes} |
| {param_2} | {string} | {file path, .csv extension} | {none} | {Yes} |
| {param_3} | {int} | {1 - 100} | {10} | {No} |

## 3. Calculation Logic

- [ ] Engineering formulas documented with source references
- [ ] Units of measurement specified for all variables
- [ ] Numerical precision and rounding rules defined
- [ ] Edge cases identified (division by zero, overflow, negative values)
- [ ] Calculation verified against manual example or reference tool

### Key Formulas

| Calculation | Formula | Source / Standard | Units |
|---|---|---|---|
| {description} | {formula} | {IEC / IEEE / textbook reference} | {units} |
| | | | |

## 4. Output Format

- [ ] Output structure defined (file format, columns, headers)
- [ ] Engineering units included in output
- [ ] Timestamp and metadata included for traceability
- [ ] Output file naming convention defined
- [ ] Output validated against expected results for test inputs

### Output Specification

| Output | Format | Destination | Example |
|---|---|---|---|
| {calculation results} | {CSV / JSON / Excel} | {file path or system} | {sample output} |
| {log file} | {text} | {log directory} | {sample log entry} |

## 5. Error Handling

- [ ] All exceptions caught and logged with meaningful messages
- [ ] Failure modes identified with recovery actions
- [ ] Partial results handled (save progress, resume capability)
- [ ] Exit codes defined (0 = success, non-zero = specific error)
- [ ] User notified of errors in a clear, actionable way

### Error Codes

| Code | Meaning | User Action |
|---|---|---|
| 0 | Success | None |
| 1 | Invalid input parameter | Check input values and retry |
| 2 | Input file not found | Verify file path |
| 3 | Calculation error | Review input data for anomalies |
| 99 | Unexpected error | Contact developer with log file |

## 6. Unit Tests

- [ ] Test cases cover normal operation (happy path)
- [ ] Test cases cover boundary conditions
- [ ] Test cases cover error conditions (bad input, missing file)
- [ ] Expected results calculated independently (manual or reference tool)
- [ ] All tests pass before release

### Test Cases

| Test ID | Description | Input | Expected Output | Pass/Fail |
|---|---|---|---|---|
| UT-001 | {Normal calculation} | {input values} | {expected result} | |
| UT-002 | {Boundary — maximum input} | {max values} | {expected result} | |
| UT-003 | {Error — missing file} | {invalid path} | {Error code 2} | |

## 7. Documentation

- [ ] Inline comments for non-obvious logic
- [ ] README or header block with usage instructions
- [ ] Input/output specification documented
- [ ] Dependencies listed with version requirements
- [ ] Change log maintained

## 8. Version Control

- [ ] Script stored in version-controlled repository
- [ ] Branch/tag created for each release
- [ ] Changes reviewed before merge (peer review)
- [ ] Release notes written for each version

### Version History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | {date} | {author} | Initial release |
