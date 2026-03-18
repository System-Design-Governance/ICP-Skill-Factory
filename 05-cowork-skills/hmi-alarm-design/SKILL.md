---
name: hmi-alarm-design
description: >
  人機介面與告警設計。
  Design Human-Machine Interface (HMI) screens for SCADA/EMS/DERMS operator workstations following ISA-101 HMI design guidelines. This skill covers scre。Design the alarm management system including alarm priority hierarchy (Critical/High/Medium/Low/Inf
  MANDATORY TRIGGERS: 人機介面與告警設計, 告警層級配置設計, HMI 畫面設計, IEC-62682, Alarm Hierarchy and Configuration Design, ISA-101, DERMS, alarm-management, visualization, alarm-hierarchy, hmi alarm design.
  Use this skill for hmi alarm design tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 人機介面與告警設計

本 Skill 整合 2 個工程技能定義，提供人機介面與告警設計的完整工作流程。
適用領域：Control Systems（D05）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-015, SK-D01-019, SK-D01-020, SK-D02-001, SK-D05-001, SK-D05-002

---

## 1. 輸入

- System Architecture Design and SCADA/EMS/DERMS functional specification (from SK-D05-001 ⏳ and SK-D05-002 ⏳)
- Process flow diagrams and operational procedures (from SK-D05-001 ⏳: Process Flow Mapping)
- Operator role profile analysis with permission matrix (from SK-D01-020: Role-Based Access Control Design)
- Alarm hierarchy and priority definitions (from SK-D05-006: Alarm Hierarchy and Configuration Design)
- Device network topology and real-time data availability (from SK-D02-001 ⏳: OT Network Topology Design)
- Operator workstation hardware specifications (monitors, input devices, ambient conditions)
- Process Flow Diagrams and process operating envelopes (normal, abnormal, emergency conditions) (from SK-D05-001 ⏳: Process Flow Mapping)
- Equipment specifications and failure modes (FMEA or HAZOP results, if available)
- Operational procedures and operator response expectations (from SK-D05-003 ⏳: Operational Procedures Development)
- Security Alarm Rule Design output (from SK-D01-015: Security Alarm Rule Design)
- Historical alarm data or benchmark alarm counts from similar systems

---

## 2. 工作流程

### Step 1: HMI 畫面設計
**SK 來源**：SK-D05-005 — HMI Screen Design

執行HMI 畫面設計：Design Human-Machine Interface (HMI) screens for SCADA/EMS/DERMS operator workstations following ISA-101 HMI design guidelines. This skill covers scre

**本步驟交付物**：
- HMI Screen Specification Document: screen templates for each operational view (overview dashboard, zone control, generator/asset control, alarms, tren
- Screen Layout Diagrams (mockups or wireframes) showing navigation hierarchy, element placement, and role-specific variants
- Color Palette and Coding Standard document (per ISA-101 Section 5.3): normal state colors, alarm colors (red/yellow/blue), trends, process states

### Step 2: 告警層級配置設計
**SK 來源**：SK-D05-006 — Alarm Hierarchy and Configuration Design

執行告警層級配置設計：Design the alarm management system including alarm priority hierarchy (Critical/High/Medium/Low/Information), alarm rationalization, alarm shelving an

**本步驟交付物**：
- Alarm Management Strategy Document: philosophy and governance framework for alarm management, including alarm performance targets (e.g., max 10 alarms
- Alarm Rationalization Report: justification for each alarm (why this parameter is alarmed, trigger thresholds, operator response)
- Alarm Database/Register: structured list of all alarm tags with fields: alarm ID, description, priority level, trigger condition/threshold, alarm mess

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | HMI Screen Specification Document: screen templates for each operational view (overview dashboard, zone control, generator/asset control, alarms, tren | 依需求 |
| 2 | Screen Layout Diagrams (mockups or wireframes) showing navigation hierarchy, element placement, and role-specific variants | 依需求 |
| 3 | Color Palette and Coding Standard document (per ISA-101 Section 5.3): normal state colors, alarm colors (red/yellow/blue), trends, process states | 依需求 |
| 4 | Navigation Map: screen relationships, drill-down paths, context switching rules, role-based screen visibility matrix | Markdown |
| 5 | HMI Object Library: standard symbols, gauges, trend displays, alarm displays with interaction rules | 依需求 |
| 6 | Integration Matrix: mapping HMI screen elements to backend data tags, control objects, and command routes per SK-D05-002 ⏳ | Markdown |
| 7 | Alarm Management Strategy Document: philosophy and governance framework for alarm management, including alarm performance targets (e.g., max 10 alarms | 依需求 |
| 8 | Alarm Rationalization Report: justification for each alarm (why this parameter is alarmed, trigger thresholds, operator response) | Markdown |
| 9 | Alarm Database/Register: structured list of all alarm tags with fields: alarm ID, description, priority level, trigger condition/threshold, alarm mess | Markdown |
| 10 | Alarm Display Specification: alarm presentation rules for HMI screens, filtering, sorting, grouping, and acknowledgment logic | 依需求 |
| 11 | Security Alarm Integration Matrix: mapping security alarms from SK-D01-015 to the general alarm hierarchy | Markdown |
| 12 | Alarm Testing and Validation Plan: procedure for commissioning and validating alarm behavior | 依需求 |

---

## 4. 適用標準

- ISA-101:2015 — Criterion 5 (Human-Machine Interfaces): screen hierarchy, color coding, alarm presentation, operator guid
- ISA-82.00.01 — Graphic Symbols for Process Displays: standard symbols for equipment, processes, and control elements
- IEC 60417 — Graphical Symbols for Use on Equipment: general-purpose symbols for HMI screens
- ANSI/ISA-18.2 — Standard for Alarm Management for the Process Industries: alarm display and acknowledgment interaction p
- ISO 11064 — Ergonomics of Human-System Interaction: control room design, workstation layout, and visual ergonomics
- IEC 62443-3-3 — System Security Requirements and Security Levels: security presentation and operator awareness of securi
- ISA-18.2:2016 — Management of Alarm Systems for the Process Industries: alarm design principles, rationalization methodo
- IEC 62682:2015 — Procedures for Performance Evaluation of Alarm Systems: quantitative alarm performance metrics and test
- ANSI/ISA-101:2015 — Criterion 5: Alarm Display and Acknowledgment — alarm presentation and human factors
- IEC 60812 — Failure Mode and Effects Analysis (FMEA): systematic approach to identifying alarms for failure modes

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | All major operational views (overview, zone/asset control, alarms, trending, rep | ✅ 已驗證 |
| 2 | Screen navigation hierarchy is documented with state diagrams showing drill-down | ✅ 已驗證 |
| 3 | Color palette follows ISA-101 Section 5.3 specifications for normal/alert/alarm/ | ✅ 已驗證 |
| 4 | Alarm display design includes priority color coding, acknowledgment affordance,  | ✅ 已驗證 |
| 5 | Role-based screen visibility matrix is complete and traceable to SK-D01-020 perm | ✅ 已驗證 |
| 6 | HMI-to-data-tag mapping is complete and validated against SK-D05-002 ⏳ data mode | ✅ 已驗證 |
| 7 | Screen layout meets ergonomic guidelines per ISO 11064 for typical operator work | ✅ 已驗證 |
| 8 | Design documentation includes design rationale for screen grouping, information  | ✅ 已驗證 |
| 9 | Alarm hierarchy (Critical/High/Medium/Low/Information) is fully defined with obj | ✅ 已驗證 |
| 10 | Every safety-critical failure mode and security-critical event has a correspondi | ✅ 已驗證 |
| 11 | Alarm rationalization report justifies each alarm and documents why non-alarmed  | ✅ 已驗證 |
| 12 | All alarms from SK-D01-015 (Security Alarm Rules) are integrated into the alarm  | ✅ 已驗證 |
| 13 | Alarm thresholds are technically sound and traceable to process engineering or e | ✅ 已驗證 |
| 14 | Suppression/shelving rules are documented with clear conditions for when alarms  | ✅ 已驗證 |
| 15 | Alarm message text is clear, actionable, and includes recommended operator respo | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D05-005 | | Junior (< 2 yr) | 10–16 person-days | Assumes single SCADA system with 5–10 major operational view |
| SK-D05-005 | | Senior (5+ yr) | 5–8 person-days | Same scope; senior can leverage component libraries and HMI des |
| SK-D05-006 | | Junior (< 2 yr) | 12–18 person-days | Assumes single system with 200–400 alarm points; includes ra |
| SK-D05-006 | | Senior (5+ yr) | 6–10 person-days | Same scope; senior can leverage prior alarm frameworks and app |

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
人機介面與告警設計已完成。
📋 執行範圍：2 個工程步驟（SK-D05-005, SK-D05-006）
📊 交付物清單：
  - HMI Screen Specification Document: screen templates for each operational view (overview dashboard, zone control, generator/asset control, alarms, tren
  - Screen Layout Diagrams (mockups or wireframes) showing navigation hierarchy, element placement, and role-specific variants
  - Color Palette and Coding Standard document (per ISA-101 Section 5.3): normal state colors, alarm colors (red/yellow/blue), trends, process states
  - Navigation Map: screen relationships, drill-down paths, context switching rules, role-based screen visibility matrix
  - HMI Object Library: standard symbols, gauges, trend displays, alarm displays with interaction rules
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
| Domain | D05 (Control Systems) |
| SK 覆蓋 | SK-D05-005, SK-D05-006 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D05-005 | HMI Screen Design | HMI 畫面設計 | Design Human-Machine Interface (HMI) screens for SCADA/EMS/D |
| SK-D05-006 | Alarm Hierarchy and Configuration Design | 告警層級配置設計 | Design the alarm management system including alarm priority  |

<!-- Phase 5 Wave 2 deepened: SK-D05-005, SK-D05-006 -->