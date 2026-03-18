---
name: security-testing
description: >
  安全性與性能測試。
  Establish performance baselines for OT/ICS systems during commissioning that serve as the reference metrics for subsequent anomaly detection, operatio。Execute application-level security testing for OT/ICS software components including SCADA servers, 
  MANDATORY TRIGGERS: 應用安全測試執行, 安全檢驗測試協定撰寫, 弱點掃描與報告, 安全性與性能測試, 滲透測試執行, 性能基線建立, security testing, capacity-planning, Security Inspection and Test Protocol Development, ot-metrics, ot-security, rules-of-engagement, performance-baseline, ot-scanning.
  Use this skill for security testing tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 安全性與性能測試

本 Skill 整合 5 個工程技能定義，提供安全性與性能測試的完整工作流程。
適用領域：Testing & Commissioning（D08）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D01-005, SK-D01-006, SK-D01-007, SK-D01-014, SK-D02-001

---

## 1. 輸入

- System architecture documentation and network topology (from SK-D01-001, SK-D02-001 ⏳)
- Device inventory with performance requirements (from SK-D01-005 ⏳: Asset Inventory Development)
- Operational procedures and normal operating hours (from SK-D10-001 ⏳)
- Security monitoring infrastructure (SIEM, network analyzer, device logs) deployed and operational
- Monitoring tool configuration and data collection agents installed on critical systems
- Historical baseline data from similar systems (if available)
- Security test plan and test case designs (from SK-D08-002: Security FAT Test Case Design)
- Application design documentation: architecture, component diagrams, data flows (from SK-D05-001 ⏳ and domain D05)
- Security requirements specification: authentication, authorization, input validation, cryptography requirements (from SK-D01-005, SK-D01-006)
- OWASP Top 10 and OT-adapted application security requirements (from organizational security standards)
- Application source code (for code review and white-box testing, if available)
- Compiled applications, installers, and deployment configurations

---

## 2. 工作流程

### Step 1: 性能基線建立
**SK 來源**：SK-D08-007 — Performance Baseline Establishment

執行性能基線建立：Establish performance baselines for OT/ICS systems during commissioning that serve as the reference metrics for subsequent anomaly detection, operatio

**本步驟交付物**：
- Performance Baseline Report: summary of baseline metrics, collection methodology, measurement period, statistical summaries (mean, std deviation, min/
- Baseline Metrics Table: per-device/per-protocol baseline data organized by metric type (throughput Mbps, latency ms, CPU %, memory %, security events/
- Network Throughput Baseline: aggregate and per-conduit network throughput measurements (bytes/sec, packets/sec), peak and off-peak characterization

### Step 2: 應用安全測試執行
**SK 來源**：SK-D08-008 — Application Security Testing Execution

執行應用安全測試執行：Execute application-level security testing for OT/ICS software components including SCADA servers, HMI (Human-Machine Interface) applications, web-bas

**本步驟交付物**：
- Application Security Test Execution Report: executive summary, scope, test methodology, test environment description, findings summary (by severity an
- Test Case Execution Log: per-test-case results (pass/fail), evidence (screenshots, logs), observed behavior, any exceptions or deviations
- Vulnerability Findings Report: discovered vulnerabilities organized by severity (Critical, High, Medium, Low), with detailed description, affected com

### Step 3: 滲透測試執行
**SK 來源**：SK-D08-009 — Penetration Testing Execution

執行滲透測試執行：Execute penetration testing against OT/ICS systems following pre-approved rules of engagement that prioritize operational safety and system continuity

**本步驟交付物**：
- Penetration Testing Engagement Report: executive summary, scope, methodology, testing phases, findings summary by severity
- Network Penetration Testing Report: network reconnaissance findings, identified vulnerabilities, successful exploitations, lateral movement chains, pe
- Application Penetration Testing Report: web application findings, API vulnerabilities, authentication bypass techniques, privilege escalation paths, d

### Step 4: 弱點掃描與報告
**SK 來源**：SK-D08-010 — Vulnerability Scanning and Reporting

執行弱點掃描與報告：Execute vulnerability scanning using OT-aware vulnerability scanning tools, analyze discovered vulnerabilities, classify each finding by severity usin

**本步驟交付物**：
- Vulnerability Assessment Report: executive summary, scan scope, scanning methodology, vulnerability statistics (by severity, by asset type, by vulnera
- Detailed Vulnerability Findings: per-vulnerability listing with: vulnerability ID (CVE), affected asset/service, vulnerability description, CVSS score
- Vulnerability Remediation Roadmap: prioritized list of remediation actions with severity, exploitability assessment, business impact, implementation e

### Step 5: 安全檢驗測試協定撰寫
**SK 來源**：SK-D08-014 — Security Inspection and Test Protocol Development

執行安全檢驗測試協定撰寫：Security Inspection and Test Protocol Development creates comprehensive testing protocols covering 14 security categories identified in the ID14 exemp

**本步驟交付物**：
- Security inspection and test protocol document covering all 14 security categories with unified approach
- Category-specific test specifications for each of the 14 domains (network, access control, endpoint, encryption, logging, backup, patch, malware, SIS,
- Test case definitions with preconditions, procedures, expected results, and acceptance criteria for each category

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Performance Baseline Report: summary of baseline metrics, collection methodology, measurement period, statistical summaries (mean, std deviation, min/ | Markdown |
| 2 | Baseline Metrics Table: per-device/per-protocol baseline data organized by metric type (throughput Mbps, latency ms, CPU %, memory %, security events/ | 依需求 |
| 3 | Network Throughput Baseline: aggregate and per-conduit network throughput measurements (bytes/sec, packets/sec), peak and off-peak characterization | 依需求 |
| 4 | Response Time Baseline: protocol response times (MODBUS register read latency, DNP3 poll cycle time, HMI command response time), percentile distributi | 依需求 |
| 5 | Device Resource Utilization Baseline: per-device CPU, memory, disk I/O, network interface utilization under normal loads | 依需求 |
| 6 | Protocol Latency Baseline: application-layer protocol latencies (IEC 60870-5-104 ASDU latency, Ethernet/IP message latency, serial protocol response t | 依需求 |
| 7 | Application Security Test Execution Report: executive summary, scope, test methodology, test environment description, findings summary (by severity an | Markdown |
| 8 | Test Case Execution Log: per-test-case results (pass/fail), evidence (screenshots, logs), observed behavior, any exceptions or deviations | 依需求 |
| 9 | Vulnerability Findings Report: discovered vulnerabilities organized by severity (Critical, High, Medium, Low), with detailed description, affected com | Markdown |
| 10 | Input Validation Test Report: injection attack attempts (SQL injection, command injection, LDAP injection, XXE), buffer overflow attempts, format stri | Markdown |
| 11 | Authentication and Access Control Test Report: weak credential policies, authentication bypass attempts, privilege escalation paths, unauthorized acce | Markdown |
| 12 | Session Management Test Report: session token generation, token lifetime and invalidation, concurrent session handling, session fixation and hijacking | Markdown |

---

## 4. 適用標準

- IEC 62443-1-1: Terminology, concepts, and models — baseline concepts within OT security monitoring
- IEC 62443-4-1: Secure product development — baseline measurement practices
- NIST SP 800-82 Rev. 3: Guide to OT Security — performance baseline for anomaly detection
- IEEE 1415: Guide for Induction Machinery Maintenance Testing and Failure Analysis — equipment baseline metrics
- PRAC: Industry standard practice for establishing baselines in OT/ICS commissioning and operational handover
- ID01 §6.5.1.4.2: Development and testing security requirements — application security testing as part of development and
- ID01 §7.5: Software development lifecycle requirements and secure coding practices — application testing validates SDL c
- OWASP Testing Guide: comprehensive application security testing methodology adapted for OT/ICS
- OWASP Top 10 (2021): application security vulnerabilities most critical to web and OT applications
- IEC 62443-4-1: Secure product development — secure development practices that application testing validates

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Baseline collection methodology is documented: measurement period duration, samp | ✅ 已驗證 |
| 2 | Collection period is appropriate: minimum 2–4 weeks post-startup to ensure syste | ✅ 已驗證 |
| 3 | Network throughput baseline covers all conduits: aggregate throughput, per-proto | ✅ 已驗證 |
| 4 | Response time baseline includes all critical protocols: MODBUS, DNP3, HMI, OPC U | ✅ 已驗證 |
| 5 | Device resource utilization baseline is available for all critical devices: CPU, | ✅ 已驗證 |
| 6 | Protocol latency baseline is documented with sample size and measurement methodo | ✅ 已驗證 |
| 7 | Security event rate baseline is established with clear normal vs. suspicious eve | ✅ 已驗證 |
| 8 | Baseline validation confirms data quality: completeness (>95% data points collec | ✅ 已驗證 |
| 9 | Test plan is approved by STC and development team: scope, test environment, test | ✅ 已驗證 |
| 10 | All test cases from SK-D08-002 are executed; any skipped test cases have documen | ✅ 已驗證 |
| 11 | Test environment is isolated and does not impact production systems | ✅ 已驗證 |
| 12 | Input validation testing covers: SQL injection, command injection, LDAP injectio | ✅ 已驗證 |
| 13 | Authentication testing includes: weak credential policies, authentication bypass | ✅ 已驗證 |
| 14 | Session management testing covers: token generation randomness, token lifetime,  | ✅ 已驗證 |
| 15 | API testing (if applicable) verifies: endpoint authentication, input validation, | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D08-007 | | Junior (< 2 yr) | 5–8 person-days | Assumes moderate system complexity, straightforward measuremen |
| SK-D08-007 | | Senior (5+ yr) | 2–4 person-days | Same scope; senior can leverage prior baseline methodologies an |
| SK-D08-008 | | Junior (< 2 yr) | 10–16 person-days | Assumes moderate application complexity, OWASP Top 10 covera |
| SK-D08-008 | | Senior (5+ yr) | 5–10 person-days | Same scope; senior can leverage automated tools, prior applica |
| SK-D08-008 | Notes: Complex applications with many custom components, APIs, or cryptographic functions may requir |
| SK-D08-009 | | Junior (< 2 yr) | 15–25 person-days | Assumes moderate system complexity, straightforward network  |
| SK-D08-009 | | Senior (5+ yr) | 10–18 person-days | Same scope; senior can leverage prior penetration testing exp |
| SK-D08-009 | Notes: Complex systems with OT protocols, PLCs, or specialized hardware require advanced OT-specific |

---

## 7. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 輸入完整性 | 所有必要輸入文件已讀取並摘要 |
| 2 | 流程覆蓋 | 5 個工作步驟皆已執行並有產出 |
| 3 | 輸出完整性 | 所有交付物已產出、格式正確、非空白 |
| 4 | 標準合規 | 產出引用的標準版本正確 |
| 5 | 術語一致 | 專案術語、縮寫與 glossary 一致 |
| 6 | 跨步驟一致 | 各步驟產出間無矛盾（如數量、SL等級） |
| 7 | 依賴追溯 | 外部依賴 SK 的輸入已驗證可用 |

---

## 8. 人類審核閘門

完成所有工作步驟後，暫停並向使用者提交審核：

```
安全性與性能測試已完成。
📋 執行範圍：5 個工程步驟（SK-D08-007, SK-D08-008, SK-D08-009, SK-D08-010, SK-D08-014）
📊 交付物清單：
  - Performance Baseline Report: summary of baseline metrics, collection methodology, measurement period, statistical summaries (mean, std deviation, min/
  - Baseline Metrics Table: per-device/per-protocol baseline data organized by metric type (throughput Mbps, latency ms, CPU %, memory %, security events/
  - Network Throughput Baseline: aggregate and per-conduit network throughput measurements (bytes/sec, packets/sec), peak and off-peak characterization
  - Response Time Baseline: protocol response times (MODBUS register read latency, DNP3 poll cycle time, HMI command response time), percentile distributi
  - Device Resource Utilization Baseline: per-device CPU, memory, disk I/O, network interface utilization under normal loads
⚠️ 待確認事項：{列出 TBD 項目或需人工判斷的假設}
👉 請審核以上成果，確認 PASS / FAIL / PASS with Conditions。
```

**判定標準**：
- **PASS**：成果完整且正確，可進入下一階段或歸檔
- **FAIL**：發現重大缺漏或錯誤，需返工後重新提交
- **PASS with Conditions**：整體接受，但需補充特定項目後完成

---

## 9. IEC 62443 生命週期對應

| 項目 | 值 |
|------|---|
| 主要生命週期階段 | 依專案階段 |
| Domain | D08 (Testing & Commissioning) |
| SK 覆蓋 | SK-D08-007, SK-D08-008, SK-D08-009, SK-D08-010, SK-D08-014 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D08-007 | Performance Baseline Establishment | 性能基線建立 | Establish performance baselines for OT/ICS systems during co |
| SK-D08-008 | Application Security Testing Execution | 應用安全測試執行 | Execute application-level security testing for OT/ICS softwa |
| SK-D08-009 | Penetration Testing Execution | 滲透測試執行 | Execute penetration testing against OT/ICS systems following |
| SK-D08-010 | Vulnerability Scanning and Reporting | 弱點掃描與報告 | Execute vulnerability scanning using OT-aware vulnerability  |
| SK-D08-014 | Security Inspection and Test Protocol Development | 安全檢驗測試協定撰寫 | Security Inspection and Test Protocol Development creates co |

<!-- Phase 5 Wave 2 deepened: SK-D08-007, SK-D08-008, SK-D08-009, SK-D08-010, SK-D08-014 -->