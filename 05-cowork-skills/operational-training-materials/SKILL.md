---
name: operational-training-materials
description: >
  操作與培訓教材。
  This skill encompasses the authoring of comprehensive Operation Manuals for OT/ICS systems, written specifically for plant operators and maintenance t。This skill encompasses the design and development of comprehensive training materials for system op
  MANDATORY TRIGGERS: 培訓教材製作, 操作手冊撰寫, 操作與培訓教材, operator-training, kirkpatrick-framework, security-training, operational-documentation, operator-manual, learning-evaluation, safety-procedures, Operation Manual Writing.
  Use this skill for operational training materials tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 操作與培訓教材

本 Skill 整合 2 個工程技能定義，提供操作與培訓教材的完整工作流程。
適用領域：Documentation（D09）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-018, SK-D01-020, SK-D01-024, SK-D05-001, SK-D05-005, SK-D05-010

---

## 1. 輸入

- System functional design specification and control logic (from SK-D05-001: Control System Functional Specification)
- HMI screen design and operator interface specifications (from SK-D05-005: HMI Screen Design)
- Alarm and event list with response procedures (from SK-D05-010: Alarm and Event Management)
- System safety analysis and operational hazards assessment (from SK-D01-018: Safety Instrumented System Design)
- Security operational procedures and access control policies (from SK-D01-020: Account and Access Control)
- Startup/shutdown sequences from commissioning plan (from SK-D07-001: Commissioning Plan)
- System functional design and operation procedures (from SK-D05-001: Control System Functional Specification and SK-D09-006: Operation Manual Writing)
- Security policies and access control procedures (from SK-D01-020: Account and Access Control)
- Alarm and event procedures (from SK-D05-010: Alarm and Event Management)
- HMI screen designs and operator interface (from SK-D05-005: HMI Screen Design)
- Cybersecurity incident response procedures (from SK-D01-024: Incident Response Planning)
- Safety procedures and SIL requirements (from SK-D01-018: Safety Instrumented System Design)

---

## 2. 工作流程

### Step 1: 操作手冊撰寫
**SK 來源**：SK-D09-006 — Operation Manual Writing

執行操作手冊撰寫：This skill encompasses the authoring of comprehensive Operation Manuals for OT/ICS systems, written specifically for plant operators and maintenance t

**本步驟交付物**：
- Operation Manual: comprehensive document organized by procedure type (startup, normal operation, alarm response, troubleshooting, shutdown, security p
- Quick Reference Cards: laminated or digital single-page procedure summaries for critical operations (startup, emergency shutdown, critical alarms)
- Operator Procedure Checklist: step-by-step checklist format for operators to verify procedure completion

### Step 2: 培訓教材製作
**SK 來源**：SK-D09-008 — Training Material Development

執行培訓教材製作：This skill encompasses the design and development of comprehensive training materials for system operators, administrators, and maintenance personnel 

**本步驟交付物**：
- Instructor Guides: complete lesson plans with learning objectives, content outline, delivery notes, timing, and assessment methods
- Learner Workbooks: participant handouts with key concepts, practice exercises, case studies, and self-assessment questions
- Presentation Decks: slides with speaker notes, illustrations, videos, and interactive elements

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Operation Manual: comprehensive document organized by procedure type (startup, normal operation, alarm response, troubleshooting, shutdown, security p | 依需求 |
| 2 | Quick Reference Cards: laminated or digital single-page procedure summaries for critical operations (startup, emergency shutdown, critical alarms) | 依需求 |
| 3 | Operator Procedure Checklist: step-by-step checklist format for operators to verify procedure completion | Markdown |
| 4 | Troubleshooting Decision Tree: visual flowcharts for diagnosing and resolving common operational issues | 依需求 |
| 5 | Glossary and Abbreviation Reference: definitions of technical terms and system-specific abbreviations | 依需求 |
| 6 | Appendices: alarm tables, setpoint reference, contact information for support, spare parts lists | Markdown |
| 7 | Instructor Guides: complete lesson plans with learning objectives, content outline, delivery notes, timing, and assessment methods | 依需求 |
| 8 | Learner Workbooks: participant handouts with key concepts, practice exercises, case studies, and self-assessment questions | 依需求 |
| 9 | Presentation Decks: slides with speaker notes, illustrations, videos, and interactive elements | 依需求 |
| 10 | Hands-On Exercise Scenarios: realistic simulations or lab setups for practical skill development | Markdown |
| 11 | Assessment Tools: quizzes, practical tests, and competency checklists aligned with Kirkpatrick L2 and L3 objectives | Markdown |
| 12 | Training Schedule and Audience Matrix: mapping training modules to audience roles and competency requirements | Markdown |

---

## 4. 適用標準

- ANSI Z535.1: Safety Color Coding — for warning and safety labels in manuals
- IEEE 1063: Standard for Software User Documentation
- IEC 62443-3-3: System security requirements — security-relevant operational procedures must align
- IEC 61508: Functional safety — safety-critical procedures must reference SIL requirements
- Plain language standards (PLAIN Act, European Plain Language Initiative) — for readability and accessibility
- Kirkpatrick Model (Kirkpatrick and Kirkpatrick, 2016) — four levels of training evaluation (L1–L4)
- ADDIE Model (Analysis, Design, Development, Implementation, Evaluation) — instructional design framework
- IEC 62443-3-3: System security requirements — security training content requirements
- IEEE 1484.12.1: Learning Objects Metadata — for LMS integration and reusability
- Adult Learning Principles (Knowles, Merriam, Bierema) — andragogy principles for effective instruction

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Operation Manual covers all operational modes and procedures: startup, normal op | ✅ 已驗證 |
| 2 | Every alarm listed in the Alarm and Event Management register has a documented r | ✅ 已驗證 |
| 3 | Manual is written in plain language appropriate for plant operators; technical t | ✅ 已驗證 |
| 4 | All security-relevant operational procedures (access control, password managemen | ✅ 已驗證 |
| 5 | Manual includes illustrations, screenshots, or flowcharts for at least 80% of pr | ✅ 已驗證 |
| 6 | Manual has been reviewed and approved by the Operations Lead and at least one pl | ✅ 已驗證 |
| 7 | Training materials cover all required competencies: system startup, normal opera | ✅ 已驗證 |
| 8 | Learning objectives are clearly stated for each training module, written in meas | ✅ 已驗證 |
| 9 | Content is organized with clear prerequisite sequencing; advanced topics build o | ✅ 已驗證 |
| 10 | Assessment methods (quizzes, practical exercises, competency checklists) are ali | ✅ 已驗證 |
| 11 | Instructor guides include delivery notes, timing guidance, answer keys, and faci | ✅ 已驗證 |
| 12 | Training materials have been reviewed by both Subject Matter Experts (technical  | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D09-006 | | Junior (< 2 yr) | 12–18 person-days | Assumes ~50 operational procedures, moderate complexity, gre |
| SK-D09-006 | | Senior (5+ yr) | 6–10 person-days | Same scope; senior can rapidly synthesize procedures from desi |
| SK-D09-006 | Notes: Systems with high operational complexity (multi-mode, many alarms) may require 1.5–2× effort. |
| SK-D09-008 | | Junior (< 2 yr) | 18–24 person-days | Assumes 6–8 training modules, 20–30 hours total learner cont |
| SK-D09-008 | | Senior (5+ yr) | 10–14 person-days | Same scope; senior can rapidly design learning objectives, se |
| SK-D09-008 | Notes: Systems with high operational complexity or specialized audiences may require 1.5–2× effort.  |

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
操作與培訓教材已完成。
📋 執行範圍：2 個工程步驟（SK-D09-006, SK-D09-008）
📊 交付物清單：
  - Operation Manual: comprehensive document organized by procedure type (startup, normal operation, alarm response, troubleshooting, shutdown, security p
  - Quick Reference Cards: laminated or digital single-page procedure summaries for critical operations (startup, emergency shutdown, critical alarms)
  - Operator Procedure Checklist: step-by-step checklist format for operators to verify procedure completion
  - Troubleshooting Decision Tree: visual flowcharts for diagnosing and resolving common operational issues
  - Glossary and Abbreviation Reference: definitions of technical terms and system-specific abbreviations
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
| Domain | D09 (Documentation) |
| SK 覆蓋 | SK-D09-006, SK-D09-008 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D09-006 | Operation Manual Writing | 操作手冊撰寫 | This skill encompasses the authoring of comprehensive Operat |
| SK-D09-008 | Training Material Development | 培訓教材製作 | This skill encompasses the design and development of compreh |

<!-- Phase 5 Wave 2 deepened: SK-D09-006, SK-D09-008 -->