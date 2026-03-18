---
name: project-coordination
description: >
  專案協調與追蹤。
  Technical clarification meetings serve as a quality gate between customer/stakeholder expectations and engineering deliverables, preventing requiremen。Contract technical scope tracking is a primary control point for project success, preventing hidden
  MANDATORY TRIGGERS: 專案協調與追蹤, technical, contract, Contract Technical Scope Tracking, facilitation, clarification, meeting, scope, project coordination.
  Use this skill for project coordination tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 專案協調與追蹤

本 Skill 整合 2 個工程技能定義，提供專案協調與追蹤的完整工作流程。
適用領域：Project Engineering（D10）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-006, SK-D01-007, SK-D02-001, SK-D02-009, SK-D10-002, SK-D10-003

---

## 1. 輸入

- Customer/stakeholder requirements documentation with identified ambiguities
- Project schedule and resource availability
- Design and implementation approach documentation (if available)
- Previous technical clarification records and meeting minutes
- Risk register and change log
- Contract statement of work (SOW) with technical scope definition
- Project charter and approved project plan
- Work breakdown structure (WBS) and product breakdown structure (PBS)
- Stakeholder requirements documentation
- Change request log and approved change register
- Risk register with scope-related risks

---

## 2. 工作流程

### Step 1: 
**SK 來源**：SK-D10-004 — Technical Clarification Meeting Facilitation

執行：Technical clarification meetings serve as a quality gate between customer/stakeholder expectations and engineering deliverables, preventing requiremen

**本步驟交付物**：
- Technical clarification meeting agenda (with pre-meeting information package)
- Technical clarification records (ambiguity → clarification mapping)
- Action items list with assignments and tracking status

### Step 2: 
**SK 來源**：SK-D10-005 — Contract Technical Scope Tracking

執行：Contract technical scope tracking is a primary control point for project success, preventing hidden commitments and misalignment between customer expe

**本步驟交付物**：
- Approved scope baseline with traceability matrix
- Scope status reports with variance analysis
- Scope change requests and impacts

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Technical clarification meeting agenda (with pre-meeting information package) | 依需求 |
| 2 | Technical clarification records (ambiguity → clarification mapping) | 依需求 |
| 3 | Action items list with assignments and tracking status | Markdown |
| 4 | Meeting minutes with decisions, decisions rationale, and attendee sign-off | 依需求 |
| 5 | Stakeholder acceptance confirmation of clarifications | 依需求 |
| 6 | Approved scope baseline with traceability matrix | Markdown |
| 7 | Scope status reports with variance analysis | Markdown |
| 8 | Scope change requests and impacts | 依需求 |
| 9 | Updated WBS/PBS reflecting approved scope changes | 依需求 |
| 10 | Scope completion verification records | 依需求 |
| 11 | Scope-to-deliverables traceability matrix | Markdown |

---

## 4. 適用標準

- IEC 62443-4-1 (SD-2: Systems Security Requirements), IEC 62443-3-3 (System Security Audit), and organizational governanc
- IEC 62443-4-1 (SD-2: Systems Security Requirements and Impact Analysis), IEC 62443-3-3 (Verification and Validation), an

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Technical clarification meeting agenda is prepared with identified ambiguity ite | ✅ 已驗證 |
| 2 | Ambiguity items are classified by impact area (requirements, design, implementat | ✅ 已驗證 |
| 3 | Meeting duration, attendees, and scope are agreed upon in advance with customer/ | ✅ 已驗證 |
| 4 | Meeting facilitator guides discussion to systematically address each agenda item | ✅ 已驗證 |
| 5 | Technical clarification is recorded in real-time with agreed-upon terminology an | ✅ 已驗證 |
| 6 | Conflicting viewpoints are acknowledged, discussed, and resolved or escalated wi | ✅ 已驗證 |
| 7 | Meeting outcome is summarized with participants confirming understanding of clar | ✅ 已驗證 |
| 8 | Action items are assigned to responsible parties with defined due dates, priorit | ✅ 已驗證 |
| 9 | Contract technical scope is documented with clear delineation of included delive | ✅ 已驗證 |
| 10 | Scope baseline is approved by customer/stakeholder and project management and do | ✅ 已驗證 |
| 11 | Scope is mapped to work breakdown structure (WBS) and product breakdown structur | ✅ 已驗證 |
| 12 | Success criteria for scope completion are defined and measurable. | ✅ 已驗證 |
| 13 | Actual delivery progress is compared against scope baseline at defined reporting | ✅ 已驗證 |
| 14 | Scope variance is calculated and reported with root cause analysis for deviation | ✅ 已驗證 |
| 15 | Scope status is communicated to project management and customer/stakeholder thro | ✅ 已驗證 |

---

## 6. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 輸入完整性 | 所有必要輸入文件已讀取並摘要 |
| 2 | 流程覆蓋 | 2 個工作步驟皆已執行並有產出 |
| 3 | 輸出完整性 | 所有交付物已產出、格式正確、非空白 |
| 4 | 標準合規 | 產出引用的標準版本正確 |
| 5 | 術語一致 | 專案術語、縮寫與 glossary 一致 |
| 6 | 跨步驟一致 | 各步驟產出間無矛盾（如數量、SL等級） |

---

## 7. 人類審核閘門

完成所有工作步驟後，暫停並向使用者提交審核：

```
專案協調與追蹤已完成。
📋 執行範圍：2 個工程步驟（SK-D10-004, SK-D10-005）
📊 交付物清單：
  - Technical clarification meeting agenda (with pre-meeting information package)
  - Technical clarification records (ambiguity → clarification mapping)
  - Action items list with assignments and tracking status
  - Meeting minutes with decisions, decisions rationale, and attendee sign-off
  - Stakeholder acceptance confirmation of clarifications
⚠️ 待確認事項：{列出 TBD 項目或需人工判斷的假設}
👉 請審核以上成果，確認 PASS / FAIL / PASS with Conditions。
```

**判定標準**：
- **PASS**：成果完整且正確，可進入下一階段或歸檔
- **FAIL**：發現重大缺漏或錯誤，需返工後重新提交
- **PASS with Conditions**：整體接受，但需補充特定項目後完成

---

## 8. IEC 62443 生命週期對應

| 項目 | 值 |
|------|---|
| 主要生命週期階段 | 依專案階段 |
| Domain | D10 (Project Engineering) |
| SK 覆蓋 | SK-D10-004, SK-D10-005 |

---

## 9. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D10-004 | Technical Clarification Meeting Facilitation |  | Technical clarification meetings serve as a quality gate bet |
| SK-D10-005 | Contract Technical Scope Tracking |  | Contract technical scope tracking is a primary control point |

<!-- Phase 5 Wave 2 deepened: SK-D10-004, SK-D10-005 -->