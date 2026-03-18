---
name: commissioning-defect-management
description: >
  試運行與缺陷管理。
  Develop the comprehensive commissioning plan that orchestrates system startup, functional validation, performance verification, safety system testing,。Author defect reports that document issues, anomalies, and failures discovered during Factory Accep
  MANDATORY TRIGGERS: 試車計畫撰寫, 試運行與缺陷管理, 缺陷報告撰寫與分級, commissioning, defect-reporting, sat, nonconformance, commissioning defect management, quality-assurance, fat-sat-sit, testing.
  Use this skill for commissioning defect management tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 試運行與缺陷管理

本 Skill 整合 2 個工程技能定義，提供試運行與缺陷管理的完整工作流程。
適用領域：Testing & Commissioning（D08）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D01-006, SK-D02-001, SK-D08-001, SK-D08-002, SK-D08-003

---

## 1. 輸入

- FAT procedures and expected results (from SK-D08-001 ⏳)
- SAT procedures adapted for site environment (from SK-D08-003)
- SIT procedures and integration test scenarios (from SK-D08-013 ⏳)
- System design documentation: architecture, zone/conduit diagram (from SK-D01-001), network topology (from SK-D02-001 ⏳)
- Security requirements and compliance checklist (from SK-D01-006, SK-D01-007, SK-D01-002)
- Operational procedures and training materials (from SK-D10-001 ⏳, SK-D10-002 ⏳)
- Test execution logs and test case results (from SK-D08-001 ⏳, SK-D08-003, SK-D08-002, SK-D08-008, SK-D08-009, SK-D08-010)
- System design and specification documents (baseline against which defects are assessed)
- Security requirements and acceptance criteria (from SK-D01-005, SK-D01-006)
- Severity classification standard and business impact criteria (from organizational test and quality standards)
- Evidence of discovered issues: screenshots, logs, network traces, system state data
- Reproduction environment and test data (for verifying and documenting reproducibility)

---

## 2. 工作流程

### Step 1: 試車計畫撰寫
**SK 來源**：SK-D08-006 — Commissioning Plan Development

執行試車計畫撰寫：Develop the comprehensive commissioning plan that orchestrates system startup, functional validation, performance verification, safety system testing,

**本步驟交付物**：
- Commissioning Plan Master Document: executive summary, commissioning objectives, scope definition, FAT/SAT/SIT integration strategy, schedule, resourc
- Commissioning Sequence Diagram: timeline showing FAT → SAT → SIT execution, overlaps, decision gates, contingency paths, and handover milestones
- Pre-Commissioning Checklist: system readiness verification (hardware installation complete, software deployed, documentation ready, training complete)

### Step 2: 缺陷報告撰寫與分級
**SK 來源**：SK-D08-011 — Defect Report Writing and Severity Classification

執行缺陷報告撰寫與分級：Author defect reports that document issues, anomalies, and failures discovered during Factory Acceptance Test (FAT), Site Acceptance Test (SAT), and S

**本步驟交付物**：
- Defect Report (per issue): defect ID, title, description, reproduction steps, test case reference, expected behavior vs. actual behavior, severity cla
- Defect Severity Assessment: severity level justification (Critical/Major/Minor/Cosmetic), impact statement (operational, safety, schedule, cost)
- Defect Impact Narrative: business impact description (e.g., "Prevents system startup", "Causes intermittent data loss during peak load", "Cosmetic UI 

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Commissioning Plan Master Document: executive summary, commissioning objectives, scope definition, FAT/SAT/SIT integration strategy, schedule, resourc | 依需求 |
| 2 | Commissioning Sequence Diagram: timeline showing FAT → SAT → SIT execution, overlaps, decision gates, contingency paths, and handover milestones | 依需求 |
| 3 | Pre-Commissioning Checklist: system readiness verification (hardware installation complete, software deployed, documentation ready, training complete) | Markdown |
| 4 | FAT Execution Plan: FAT procedure schedule, resource requirements, test environment setup, factory location and duration, FAT acceptance criteria | 依需求 |
| 5 | SAT Execution Plan: SAT procedure schedule, site access and coordination, environmental monitoring setup, site integration testing timeline, SAT accep | 依需求 |
| 6 | SIT Execution Plan: integration testing with existing site IT/OT systems, enterprise data flow validation, system performance under production loads,  | 依需求 |
| 7 | Defect Report (per issue): defect ID, title, description, reproduction steps, test case reference, expected behavior vs. actual behavior, severity cla | Markdown |
| 8 | Defect Severity Assessment: severity level justification (Critical/Major/Minor/Cosmetic), impact statement (operational, safety, schedule, cost) | 依需求 |
| 9 | Defect Impact Narrative: business impact description (e.g., "Prevents system startup", "Causes intermittent data loss during peak load", "Cosmetic UI  | 依需求 |
| 10 | Defect Reproduction Package: step-by-step reproduction procedure, test data, environment configuration, screenshots/logs as evidence | 依需求 |
| 11 | Defect Resolution Recommendation: suggested fix, acceptance criteria for resolved defect, responsible party, target resolution date | 依需求 |
| 12 | Defect Tracking Records: linkage to nonconformance management system (SK-D11-007 ⏳), resolution status tracking, reopened/rejected status | 依需求 |

---

## 4. 適用標準

- IEC 62443 series (all parts): foundational framework for commissioning within IEC 62443 lifecycle
- IEC 61508 Part 6: Guidelines for functional safety — commissioning and operational phases
- IEC 61010-1: Safety requirements — safety validation during commissioning
- NIST SP 800-82 Rev. 3: Guide to OT Security — security commissioning and go-live validation
- IEEE 1491: Guide for Management of Software Development — software commissioning practices
- ASME B&PV Code: mechanical acceptance testing (if applicable to the system)
- Site-specific standards: site safety procedures, environmental specifications, operational procedures, IT/OT governance
- IEC 62443 series: quality and testing within IEC 62443 lifecycle framework
- IEEE 829: Software and Systems Test Documentation — defect report structure and content standards
- IEEE 1028: Software Reviews and Audits — review of defect reports as part of quality assurance

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Commissioning plan integrates FAT, SAT, and SIT with explicit sequencing, depend | ✅ 已驗證 |
| 2 | Pre-commissioning checklist covers: system readiness (installation, deployment,  | ✅ 已驗證 |
| 3 | FAT execution plan specifies schedule, resource allocation, location, duration,  | ✅ 已驗證 |
| 4 | SAT execution plan specifies schedule, site coordination, environmental monitori | ✅ 已驗證 |
| 5 | SIT execution plan specifies enterprise system integrations, performance validat | ✅ 已驗證 |
| 6 | Safety and hazardous operations procedures are documented; lockout/tagout and em | ✅ 已驗證 |
| 7 | Post-commissioning handover checklist covers: training verification, operational | ✅ 已驗證 |
| 8 | Contingency plan addresses failed tests: escalation procedures, remediation work | ✅ 已驗證 |
| 9 | Defect report structure is complete: defect ID, title, description, reproduction | ✅ 已驗證 |
| 10 | Defect description is clear and specific: not vague or subjective; describes obs | ✅ 已驗證 |
| 11 | Reproduction steps are detailed enough for independent verification: test data,  | ✅ 已驗證 |
| 12 | Evidence (screenshots, logs) is included: supports reproduction and severity ass | ✅ 已驗證 |
| 13 | Severity classification is appropriate and consistently applied: Critical defect | ✅ 已驗證 |
| 14 | Business impact is articulated: operational impact, safety implications, schedul | ✅ 已驗證 |
| 15 | All Critical defects have root cause assessment: identify whether issue is desig | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D08-006 | | Junior (< 2 yr) | 8–14 person-days | Assumes moderate system complexity, straightforward FAT/SAT/S |
| SK-D08-006 | | Senior (5+ yr) | 4–7 person-days | Same scope; senior can leverage prior commissioning plans and r |
| SK-D08-006 | Notes: Complex systems with many IT/OT integrations (SIT) or hazardous operations may require 1.5–2× |
| SK-D08-011 | | Junior (< 2 yr) | 0.5–1.5 person-days per 10 defects | Assumes standard severity mix, straightforw |
| SK-D08-011 | | Senior (5+ yr) | 0.25–0.75 person-days per 10 defects | Same scope; senior can prioritize and tria |
| SK-D08-011 | Notes: Complex defects requiring root cause analysis or requiring developer/system expert involvemen |

---

## 7. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 輸入完整性 | 所有必要輸入文件已讀取並摘要 |
| 2 | 流程覆蓋 | 2 個工作步驟皆已執行並有產出 |
| 3 | 輸出完整性 | 所有交付物已產出、格式正確、非空白 |
| 4 | 標準合規 | 產出引用的標準版本正確 |
| 5 | 術語一致 | 專案術語、縮寫與 glossary 一致 |
| 6 | 跨步驟一致 | 各步驟產出間無矛盾（如數量、SL等級） |

---

## 8. 人類審核閘門

完成所有工作步驟後，暫停並向使用者提交審核：

```
試運行與缺陷管理已完成。
📋 執行範圍：2 個工程步驟（SK-D08-006, SK-D08-011）
📊 交付物清單：
  - Commissioning Plan Master Document: executive summary, commissioning objectives, scope definition, FAT/SAT/SIT integration strategy, schedule, resourc
  - Commissioning Sequence Diagram: timeline showing FAT → SAT → SIT execution, overlaps, decision gates, contingency paths, and handover milestones
  - Pre-Commissioning Checklist: system readiness verification (hardware installation complete, software deployed, documentation ready, training complete)
  - FAT Execution Plan: FAT procedure schedule, resource requirements, test environment setup, factory location and duration, FAT acceptance criteria
  - SAT Execution Plan: SAT procedure schedule, site access and coordination, environmental monitoring setup, site integration testing timeline, SAT accep
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
| SK 覆蓋 | SK-D08-006, SK-D08-011 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D08-006 | Commissioning Plan Development | 試車計畫撰寫 | Develop the comprehensive commissioning plan that orchestrat |
| SK-D08-011 | Defect Report Writing and Severity Classification | 缺陷報告撰寫與分級 | Author defect reports that document issues, anomalies, and f |

<!-- Phase 5 Wave 2 deepened: SK-D08-006, SK-D08-011 -->