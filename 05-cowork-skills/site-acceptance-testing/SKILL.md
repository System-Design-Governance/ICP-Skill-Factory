---
name: site-acceptance-testing
description: >
  現場驗收測試。
  Develop Site Acceptance Testing (SAT) procedures adapted from FAT procedures (SK-D08-001) for field conditions, verifying that the system operates cor。Execute the Site Acceptance Test (SAT) at the project site after system installation, verifying tha
  MANDATORY TRIGGERS: 現場驗收測試, 現場驗收測試執行, 系統安全驗收測試, SAT 程序撰寫, SIT 測試協定撰寫, site-verification, integration-validation, acceptance-testing, Site Acceptance Testing Execution, FR-SR, site acceptance testing, Gate-3-blocker, SAT Procedure Development.
  Use this skill for site acceptance testing tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 現場驗收測試

本 Skill 整合 4 個工程技能定義，提供現場驗收測試的完整工作流程。
適用領域：Testing & Commissioning（D08）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D01-007, SK-D01-019, SK-D01-020, SK-D01-021, SK-D01-022

---

## 1. 輸入

- FAT procedures and test cases (from SK-D08-001 ⏳: Factory Acceptance Test Development)
- Site environment specification: ambient temperature, humidity, EMI/RFI levels, altitude, corrosive atmosphere (if applicable)
- Site network topology and data flow diagrams (from SK-D02-004 ⏳)
- Site IT/OT integration requirements and existing site systems (SCADA, ERP, MES, historian)
- Site-specific data sources and loads: weather data, market data, sensor inputs
- Security FAT test cases (from SK-D08-002) adapted for site-specific authentication and network connectivity
- SAT Procedure Document (from SK-D08-003 ⏳) — defines test cases, pass/fail criteria, and execution sequence for site testing
- FAT Results Report — baseline results from factory testing; SAT verifies site-environment consistency
- As-built system documentation: actual device configurations, IP addresses, cable schedules, installed firmware versions
- Site-specific conditions: physical environment, existing infrastructure, employer network policies, electromagnetic environment
- Security design documentation: Zone/Conduit architecture (SK-D01-001), hardening configurations (SK-D01-019), access control policy (SK-D01-020)
- Customer/employer SAT witness requirements and acceptance criteria

---

## 2. 工作流程

### Step 1: SAT 程序撰寫
**SK 來源**：SK-D08-003 — SAT Procedure Development

執行SAT 程序撰寫：Develop Site Acceptance Testing (SAT) procedures adapted from FAT procedures (SK-D08-001) for field conditions, verifying that the system operates cor

**本步驟交付物**：
- SAT Procedure Manual: overview of SAT scope, site environment validation requirements, site-specific test scenarios, site acceptance criteria, and tes
- SAT Test Case Adaptation Document: list of FAT test cases adapted for site conditions, with site-specific modifications and rationale
- Environmental Testing Procedures: validation of system operation under site-specific environmental conditions (temperature, humidity, EMI, altitude), 

### Step 2: 現場驗收測試執行
**SK 來源**：SK-D08-004 — Site Acceptance Testing Execution

執行現場驗收測試執行：Execute the Site Acceptance Test (SAT) at the project site after system installation, verifying that all security and functional requirements operate 

**本步驟交付物**：
- SAT Execution Report (per ID14 exemplar format):
- Test execution summary: total tests, pass/fail/blocked/deferred counts
- Per test case: test ID, execution date, tester, actual result, pass/fail status, evidence (screenshots, log excerpts, scan results)

### Step 3: 系統安全驗收測試
**SK 來源**：SK-D08-005 — Security Acceptance Testing Execution

執行系統安全驗收測試：Execute security-specific acceptance tests that verify the implementation status of every applicable Security Requirement (SR) defined in the FR/SR ma

**本步驟交付物**：
- SR Verification Report:
- Per-SR status matrix: SR ID, SR description, zone applicability, verification method (test/inspection/review), test result, status (Implemented / Plan
- SR coverage summary: total applicable SRs, count per status (Implemented / Planned / N/A), coverage percentage

### Step 4: SIT 測試協定撰寫
**SK 來源**：SK-D08-013 — Site Integration Test (SIT) Protocol Development

執行SIT 測試協定撰寫：Site Integration Test (SIT) Protocol Development defines the comprehensive testing approach for verifying end-to-end system integration across multipl

**本步驟交付物**：
- SIT test protocol document detailing test strategy, scope, and overall approach
- Test categories aligned with SIT phase requirements (cross-system data flows, protocol interoperability, security integration, performance)
- Test case specifications with preconditions, test steps, expected results, and acceptance criteria

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | SAT Procedure Manual: overview of SAT scope, site environment validation requirements, site-specific test scenarios, site acceptance criteria, and tes | 依需求 |
| 2 | SAT Test Case Adaptation Document: list of FAT test cases adapted for site conditions, with site-specific modifications and rationale | Markdown |
| 3 | Environmental Testing Procedures: validation of system operation under site-specific environmental conditions (temperature, humidity, EMI, altitude),  | 依需求 |
| 4 | Site Integration Test Procedures: verification of connectivity with site IT/OT systems, data flow validation, network performance under site condition | 依需求 |
| 5 | Site-Specific Security SAT Procedures: verification of access control using site-specific accounts and network credentials, security alarm testing usi | 依需求 |
| 6 | Site Data Source and Load Testing Procedures: validation with real site data sources (weather feeds, grid operator interfaces), load testing with repr | 依需求 |
| 7 | SAT Execution Report (per ID14 exemplar format): | Markdown |
| 8 | Test execution summary: total tests, pass/fail/blocked/deferred counts | 依需求 |
| 9 | Per test case: test ID, execution date, tester, actual result, pass/fail status, evidence (screenshots, log excerpts, scan results) | 依需求 |
| 10 | Site-specific verification results: | 依需求 |
| 11 | Physical security: cabinet locks, physical port status, environmental controls | 依需求 |
| 12 | Network connectivity: actual routes, latency measurements, firewall rule verification in production | 依需求 |

---

## 4. 適用標準

- IEC 62443 series (all parts): foundational IEC 62443 lifecycle framework establishing FAT/SAT/SIT distinction
- IEC 61508 Part 7: Guidelines for functional safety — system acceptance in operational environment
- NIST SP 800-82 Rev. 3: Guide to OT Security — guidance on field validation and site-specific security testing
- IEC 61010-1: Safety requirements for electrical equipment for measurement, control, and laboratory use — safety consider
- Site-specific standards and procedures: site safety manual, environmental specifications, operational procedures
- IEC 62443-2-4 SP.09.01–SP.09.04: Verification and validation — site acceptance testing requirements
- IEC 62443-3-3: System Security Requirements — SR verification in production environment
- ISO 17025: Testing competence requirements (supplementary)
- GOV-SD: Gate 3 delivery checklist — SAT completion is a prerequisite for system handover; SAT results serve as productio
- GOV-SD: 12-item Gate 3 checklist — SAT evidence must be included in the delivery package

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | SAT procedure manual covers all FAT test cases with documented site-specific ada | ✅ 已驗證 |
| 2 | Environmental testing procedures validate system operation under site-specific t | ✅ 已驗證 |
| 3 | Site integration test procedures cover all site IT/OT system integrations with e | ✅ 已驗證 |
| 4 | Security SAT procedures validate access control with site-specific accounts and  | ✅ 已驗證 |
| 5 | Site-specific data source and load testing procedures exercise the system with r | ✅ 已驗證 |
| 6 | Operational scenario testing covers typical operational workflows and emergency  | ✅ 已驗證 |
| 7 | Acceptance criteria are explicitly defined per test scenario; success metrics ar | ✅ 已驗證 |
| 8 | SAT procedures have been reviewed and approved by STC, site operations lead, and | ✅ 已驗證 |
| 9 | All mandatory SAT test cases executed with results recorded: 100% coverage of se | ✅ 已驗證 |
| 10 | Pass rate meets Gate 3 threshold: all Critical and High severity test cases pass | ✅ 已驗證 |
| 11 | Site-specific conditions verified: physical security, network connectivity in pr | ✅ 已驗證 |
| 12 | FAT-to-SAT deviation analysis completed: all differences between factory and sit | ✅ 已驗證 |
| 13 | SAT Completion Certificate signed by Security Engineering Role and customer/empl | ✅ 已驗證 |
| 14 | Punch list produced with priority assignments: all outstanding items have owner, | ✅ 已驗證 |
| 15 | 100% of applicable SRs in the FR/SR mapping matrix have a verified status (Imple | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D08-003 | | Junior (< 2 yr) | 6–12 person-days | Assumes adaptation of ~30–40 FAT test cases, moderate site co |
| SK-D08-003 | | Senior (5+ yr) | 3–6 person-days | Same scope; senior can leverage prior SAT experience and reusab |
| SK-D08-003 | Notes: Greenfield sites with simpler environments may require less effort. Brownfield sites with com |
| SK-D08-004 | | Junior (< 2 yr) | 10–15 person-days | Assumes single-site, ~50 devices, ~100 test cases; includes  |
| SK-D08-004 | | Senior (5+ yr) | 5–8 person-days | Same scope; senior leverages efficient test execution and rapid |
| SK-D08-005 | | Junior (< 2 yr) | 15–20 person-days | Assumes ~60 applicable SRs, single-site; includes scanning,  |
| SK-D08-005 | | Senior (5+ yr) | 8–12 person-days | Same scope; senior leverages automated scanning pipelines and  |
| SK-D08-005 | Notes: Effort scales with SR count (proportional to zone count × SL level). High-SL zones (SL-3, SL- |

---

## 7. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 輸入完整性 | 所有必要輸入文件已讀取並摘要 |
| 2 | 流程覆蓋 | 4 個工作步驟皆已執行並有產出 |
| 3 | 輸出完整性 | 所有交付物已產出、格式正確、非空白 |
| 4 | 標準合規 | 產出引用的標準版本正確 |
| 5 | 術語一致 | 專案術語、縮寫與 glossary 一致 |
| 6 | 跨步驟一致 | 各步驟產出間無矛盾（如數量、SL等級） |
| 7 | 依賴追溯 | 外部依賴 SK 的輸入已驗證可用 |

---

## 8. 人類審核閘門

完成所有工作步驟後，暫停並向使用者提交審核：

```
現場驗收測試已完成。
📋 執行範圍：4 個工程步驟（SK-D08-003, SK-D08-004, SK-D08-005, SK-D08-013）
📊 交付物清單：
  - SAT Procedure Manual: overview of SAT scope, site environment validation requirements, site-specific test scenarios, site acceptance criteria, and tes
  - SAT Test Case Adaptation Document: list of FAT test cases adapted for site conditions, with site-specific modifications and rationale
  - Environmental Testing Procedures: validation of system operation under site-specific environmental conditions (temperature, humidity, EMI, altitude), 
  - Site Integration Test Procedures: verification of connectivity with site IT/OT systems, data flow validation, network performance under site condition
  - Site-Specific Security SAT Procedures: verification of access control using site-specific accounts and network credentials, security alarm testing usi
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
| SK 覆蓋 | SK-D08-003, SK-D08-004, SK-D08-005, SK-D08-013 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D08-003 | SAT Procedure Development | SAT 程序撰寫 | Develop Site Acceptance Testing (SAT) procedures adapted fro |
| SK-D08-004 | Site Acceptance Testing Execution | 現場驗收測試執行 | Execute the Site Acceptance Test (SAT) at the project site a |
| SK-D08-005 | Security Acceptance Testing Execution | 系統安全驗收測試 | Execute security-specific acceptance tests that verify the i |
| SK-D08-013 | Site Integration Test (SIT) Protocol Development | SIT 測試協定撰寫 | Site Integration Test (SIT) Protocol Development defines the |

<!-- Phase 5 Wave 2 deepened: SK-D08-003, SK-D08-004, SK-D08-005, SK-D08-013 -->