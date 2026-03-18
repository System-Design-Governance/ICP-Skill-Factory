---
name: security-monitoring-incident-response
description: >
  安全監控與事件回應。
  Configure Security Information and Event Management (SIEM) systems for OT/ICS environments, including log source integration, correlation rule develop。Design security alarm rules and correlation logic for detecting cybersecurity threats in OT/ICS env
  MANDATORY TRIGGERS: SIEM 配置與調校, 安全事件調查與鑑識, 安全告警規則設計, 持續安全監控, 事件回應程序撰寫, 安全監控與事件回應, 威脅情資蒐集與分析, alerting, anomaly-detection, OT-forensics, threat-analysis, evidence-preservation, SIEM Configuration and Tuning, log-aggregation, vulnerability-intelligence.
  Use this skill for security monitoring incident response tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 安全監控與事件回應

本 Skill 整合 6 個工程技能定義，提供安全監控與事件回應的完整工作流程。
適用領域：OT Cybersecurity（D01）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D01-002, SK-D01-005, SK-D01-006, SK-D01-007, SK-D01-009

---

## 1. 輸入

- Security Alarm Rule Design specification (from SK-D01-015: Security Alarm Rule Design)
- Approved Zone/Conduit Architecture (from SK-D01-001: Zone/Conduit Architecture Design)
- Inventory of OT/ICS assets and systems that generate logs (asset inventory with system types, locations, protocols)
- Network and data flow diagrams showing log source locations (from SK-D02-004 ⏳)
- Security monitoring requirements (from SK-D01-009 ⏳: Security Monitoring Plan Development)
- SIEM platform specifications (vendor documentation, available integrations, storage capacity, retention policy)
- Security Level Targets (SL-T) per zone (from SK-D01-010 ⏳: Security Level Target Assessment)
- Preliminary and Detailed Threat and Risk Assessment reports (from SK-D01-006 ⏳ and SK-D01-007 ⏳)
- Approved network and data flow diagrams (from SK-D02-004 ⏳)
- Asset inventory with system criticality and function (from SK-D01-005 ⏳)
- Security monitoring requirements and KPIs (from SK-D01-009 ⏳: Security Monitoring Plan Development)
- Organization's information security policy framework (ISMS context)

---

## 2. 工作流程

### Step 1: SIEM 配置與調校
**SK 來源**：SK-D01-014 — SIEM Configuration and Tuning

執行SIEM 配置與調校：Configure Security Information and Event Management (SIEM) systems for OT/ICS environments, including log source integration, correlation rule develop

**本步驟交付物**：
- SIEM configuration baseline (XML, JSON, or native format exports per SIEM vendor)
- Log source integration checklist: source ID, source type, protocol/method, data format, sample validation
- Correlation rule library: rule ID, trigger condition, severity level, action (alert, escalation, block), testing results

### Step 2: 安全告警規則設計
**SK 來源**：SK-D01-015 — Security Alarm Rule Design

執行安全告警規則設計：Design security alarm rules and correlation logic for detecting cybersecurity threats in OT/ICS environments. This skill defines the abstract alarm ca

**本步驟交付物**：
- Alarm Category Specification: list of security events to monitor (authentication events, access control violations, anomalous data flows, policy breac
- Alarm Hierarchy and Severity Classification Table: alarm ID, alarm name, trigger condition (English description), severity level (Critical/High/Medium
- Correlation Rule Specification: rule ID, rule name, component events (alarm triggers that feed the rule), time window, aggregation logic, resulting al

### Step 3: 事件回應程序撰寫
**SK 來源**：SK-D01-016 — Incident Response Procedure Development

執行事件回應程序撰寫：Develop a comprehensive incident response procedure that defines the end-to-end workflow for identifying, classifying, responding to, and recovering f

**本步驟交付物**：
- Incident Response Procedure Document (structured per ID24 exemplar format):
- Incident definition and scope (affecting confidentiality, integrity, availability of systems/services/networks)
- Incident response workflow flowchart (threat intelligence → evaluation → notification → emergency → restoration → improvement → record keeping)

### Step 4: 安全事件調查與鑑識
**SK 來源**：SK-D01-017 — Security Incident Investigation and Forensics

執行安全事件調查與鑑識：- **Pitfall:** Modifying evidence during analysis, compromising chain of custody. **Guidance:** Use write-blocking tools for disk imaging; analyze evi

**本步驟交付物**：
- Investigation Authorization Document:** Formal approval to conduct forensic investigation with scope and constraints defined
- Volatile Data Preservation Log:** Documentation of memory capture, running processes, network connections captured with timestamps
- Forensic Image Inventory:** Listing of all systems imaged with timestamps, hash values (MD5/SHA-256), acquisition tool, and storage location

### Step 5: 持續安全監控
**SK 來源**：SK-D01-018 — Continuous Security Monitoring

執行持續安全監控：- **Pitfall:** Deploying SIEM without establishing baselines, leading to excessive false positive alerts. **Guidance:** Establish operational baseline

**本步驟交付物**：
- SIEM Configuration Documentation:** Data sources configured, collection validation, log retention policy, access controls, integrity protection
- Operational Baseline Report:** Established baselines for user behavior, network traffic, system performance, and data access patterns (from SK-D08-007
- Detection Rule Library:** Documented collection of anomaly detection rules, threat intelligence signatures, alert thresholds, and tuning decisions

### Step 6: 威脅情資蒐集與分析
**SK 來源**：SK-D01-032 — Threat Intelligence Collection and Analysis

執行威脅情資蒐集與分析：- **Pitfall:** Collecting threat intelligence without analysis, leading to information overload. **Guidance:** Filter threat intelligence by organizat

**本步驟交付物**：
- Threat Intelligence Program Charter:** Defined intelligence requirements, collection sources, roles/responsibilities, database standards, disseminatio
- Threat Intelligence Collection Plan:** Sources subscribed, collection frequency, update schedule, points of contact for each source
- Threat Intelligence Database:** Maintained registry of vulnerabilities, threat actors, IOCs, and attack patterns with analysis and sources

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | SIEM configuration baseline (XML, JSON, or native format exports per SIEM vendor) | 依需求 |
| 2 | Log source integration checklist: source ID, source type, protocol/method, data format, sample validation | Markdown |
| 3 | Correlation rule library: rule ID, trigger condition, severity level, action (alert, escalation, block), testing results | 依需求 |
| 4 | Alert threshold tuning documentation: metric, baseline, threshold value, justification, anomaly detection parameters | 依需求 |
| 5 | SIEM dashboard specifications: dashboard name, key metrics, alert aggregation, SLA indicators | 依需求 |
| 6 | Operational runbook: log data retention policy, archive procedure, search methodology, backup/recovery | 依需求 |
| 7 | Alarm Category Specification: list of security events to monitor (authentication events, access control violations, anomalous data flows, policy breac | Markdown |
| 8 | Alarm Hierarchy and Severity Classification Table: alarm ID, alarm name, trigger condition (English description), severity level (Critical/High/Medium | 依需求 |
| 9 | Correlation Rule Specification: rule ID, rule name, component events (alarm triggers that feed the rule), time window, aggregation logic, resulting al | 依需求 |
| 10 | Anomaly Detection Baseline Specification: metric (e.g., event rate, data volume, user behavior), baseline value (derived from historical data or opera | 依需求 |
| 11 | Alarm-to-Incident Mapping: which alarms trigger incident classification per D07.3 (Incident Severity Classification) | 依需求 |
| 12 | Integration mapping with SK-D05-006 (Alarm Hierarchy) documenting how functional alarms and security alarms coexist in the unified alarm system | 依需求 |

---

## 4. 適用標準

- IEC 62443-3-3: System Security Requirements — security monitoring and detection as a control requirement
- IEC 62443-4-1: Component Security Requirements — secure configuration and hardening of SIEM appliances
- IEC 62443-2-4: Technical Security Measures — monitoring, logging, and audit requirements
- NIST SP 800-82 Rev. 3: Guide to OT Security — logging and event monitoring guidance (supplementary)
- NIST Cybersecurity Framework (CSF): Detect function — event detection and analysis
- IEC 62443-3-3: System Security Requirements — security monitoring and detection as a foundational control
- IEC 62443-3-2: Security Risk Assessment for System Design — threat identification drives alarm rule design
- IEC 62443-1-1: Terminology, concepts and models — alarm terminology and classification
- NIST SP 800-82 Rev. 3: Guide to OT Security — event and anomaly detection guidance (supplementary)
- NIST Cybersecurity Framework (CSF): Detect function — continuous monitoring and anomaly detection

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | All log sources specified in the alarm rule design are integrated into SIEM and  | ✅ 已驗證 |
| 2 | At least 80% of log entries are successfully parsed and normalized into searchab | ✅ 已驗證 |
| 3 | Every correlation rule has been tested with synthetic/historical data and produc | ✅ 已驗證 |
| 4 | Alert threshold tuning baseline is documented with rationale; false positive rat | ✅ 已驗證 |
| 5 | SIEM dashboards display key metrics (active alerts, event throughput, zone-level | ✅ 已驗證 |
| 6 | Operational runbook includes step-by-step procedures for dashboard review, alert | ✅ 已驗證 |
| 7 | Integration testing confirms end-to-end alert flow: trigger condition → alert ge | ✅ 已驗證 |
| 8 | Every material threat from the detailed risk assessment has at least one corresp | ✅ 已驗證 |
| 9 | Alarm hierarchy covers at least 5 security event categories: authentication, aut | ✅ 已驗證 |
| 10 | Severity levels are consistently applied: Critical (immediate escalation, busine | ✅ 已驗證 |
| 11 | Correlation rules are technically feasible (e.g., multi-event correlation window | ✅ 已驗證 |
| 12 | Alarm categories are validated by SAC and OT operations stakeholders; feedback i | ✅ 已驗證 |
| 13 | Mapping to SK-D05-006 is complete; no naming conflicts or ambiguities in unified | ✅ 已驗證 |
| 14 | Design includes documented rationale for threshold values and anomaly detection  | ✅ 已驗證 |
| 15 | Procedure covers the complete incident lifecycle: identification → classificatio | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D01-014 | | Junior (< 2 yr) | 12–18 person-days | Assumes ~30 log sources, 15–20 correlation rules, basic dash |
| SK-D01-014 | | Senior (5+ yr) | 5–8 person-days | Same scope; senior can leverage SIEM templates, automated tunin |
| SK-D01-014 | Notes: Complex OT environments with diverse protocols (Modbus, IEC 60870-5-104, DNP3) may require cu |
| SK-D01-015 | | Junior (< 2 yr) | 8–12 person-days | Assumes ~20–30 alarm categories, 10–15 correlation rules, mod |
| SK-D01-015 | | Senior (5+ yr) | 3–5 person-days | Same scope; senior can leverage threat libraries and alarm temp |
| SK-D01-016 | | Junior (< 2 yr) | 8–12 person-days | Assumes adaptation of ICP template to project-specific contex |
| SK-D01-016 | | Senior (5+ yr) | 4–6 person-days | Same scope; senior efficiently maps organizational ISMS to proj |
| SK-D01-016 | Notes: Effort increases significantly if the customer requires sector-specific regulatory compliance |

---

## 7. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 輸入完整性 | 所有必要輸入文件已讀取並摘要 |
| 2 | 流程覆蓋 | 6 個工作步驟皆已執行並有產出 |
| 3 | 輸出完整性 | 所有交付物已產出、格式正確、非空白 |
| 4 | 標準合規 | 產出引用的標準版本正確 |
| 5 | 術語一致 | 專案術語、縮寫與 glossary 一致 |
| 6 | 跨步驟一致 | 各步驟產出間無矛盾（如數量、SL等級） |
| 7 | 依賴追溯 | 外部依賴 SK 的輸入已驗證可用 |

---

## 8. 人類審核閘門

完成所有工作步驟後，暫停並向使用者提交審核：

```
安全監控與事件回應已完成。
📋 執行範圍：6 個工程步驟（SK-D01-014, SK-D01-015, SK-D01-016, SK-D01-017, SK-D01-018, SK-D01-032）
📊 交付物清單：
  - SIEM configuration baseline (XML, JSON, or native format exports per SIEM vendor)
  - Log source integration checklist: source ID, source type, protocol/method, data format, sample validation
  - Correlation rule library: rule ID, trigger condition, severity level, action (alert, escalation, block), testing results
  - Alert threshold tuning documentation: metric, baseline, threshold value, justification, anomaly detection parameters
  - SIEM dashboard specifications: dashboard name, key metrics, alert aggregation, SLA indicators
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
| Domain | D01 (OT Cybersecurity) |
| SK 覆蓋 | SK-D01-014, SK-D01-015, SK-D01-016, SK-D01-017, SK-D01-018, SK-D01-032 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D01-014 | SIEM Configuration and Tuning | SIEM 配置與調校 | Configure Security Information and Event Management (SIEM) s |
| SK-D01-015 | Security Alarm Rule Design | 安全告警規則設計 | Design security alarm rules and correlation logic for detect |
| SK-D01-016 | Incident Response Procedure Development | 事件回應程序撰寫 | Develop a comprehensive incident response procedure that def |
| SK-D01-017 | Security Incident Investigation and Forensics | 安全事件調查與鑑識 | - **Pitfall:** Modifying evidence during analysis, compromis |
| SK-D01-018 | Continuous Security Monitoring | 持續安全監控 | - **Pitfall:** Deploying SIEM without establishing baselines |
| SK-D01-032 | Threat Intelligence Collection and Analysis | 威脅情資蒐集與分析 | - **Pitfall:** Collecting threat intelligence without analys |

<!-- Phase 5 Wave 2 deepened: SK-D01-014, SK-D01-015, SK-D01-016, SK-D01-017, SK-D01-018, SK-D01-032 -->