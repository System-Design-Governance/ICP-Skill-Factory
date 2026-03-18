---
name: plc-programming
description: >
  PLC 程式開發。
  Develop Programmable Logic Controller (PLC) ladder logic programs for industrial automation sequences including motor control, valve sequencing, inter。Develop Structured Text (ST) programs per IEC 61131-3 standard for complex control algorithms, math
  MANDATORY TRIGGERS: PLC 階梯圖程式撰寫, PLC 程式開發, 結構化文字程式開發, Structured Text Programming, PLC Ladder Logic Programming, state-machine, safety-logic, PLC-programming, structured-text, IEC-61131-3, interlocking.
  Use this skill for plc programming tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# PLC 程式開發

本 Skill 整合 2 個工程技能定義，提供PLC 程式開發的完整工作流程。
適用領域：Control Systems（D05）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-020, SK-D05-001, SK-D09-005, SK-D10-002, SK-D10-003

---

## 1. 輸入

- Logic Design Specification: functional requirements for motor start/stop sequences, valve control, interlocking rules, and safety logic from control d
- PLC Hardware Configuration: I/O module types and counts, available memory, processor scan time, communication modules (Ethernet, Modbus, Profibus, etc
- I/O Mapping Table: tag definitions (motor names, valve names, sensor names), address allocation, signal type (discrete/analog), safety-related vs. non
- Supervisory Interface Requirements (from SK-D05-001 ⏳: SCADA/RTU Architecture Design): command/status signal list, setpoint ranges, alarm thresholds
- PLC Access Control Policy (from SK-D01-020 ⏳: Cybersecurity Access Control Design): program upload/download authorization, password requirements, firm
- Change Management Procedure (from SK-D10-003 ⏳: System Change Management Procedure Design): configuration baseline documentation, change approval work
- Algorithm Design Specification: functional requirements for control algorithms (e.g., PID tuning, load forecasting, optimization logic), mathematical 
- PLC Hardware and Runtime Environment: processor type, available memory, execution cycle time, programming framework (IEC 61131-3 runtime, proprietary 
- Structured Text Language Features: available data types, function block libraries (both vendor-supplied and custom), debugging capabilities
- Interface Requirements (from SK-D05-001 ⏳: SCADA/RTU Architecture Design): input/output variable list, data types, update rates, setpoint ranges
- Software Development Standards (from SK-D09-005 ⏳: Software Development Standards and Versioning): naming conventions, code documentation format, test
- PLC Access Control Policy (from SK-D01-020 ⏳: Cybersecurity Access Control Design): program modification authorization, firmware version control

---

## 2. 工作流程

### Step 1: PLC 階梯圖程式撰寫
**SK 來源**：SK-D05-007 — PLC Ladder Logic Programming

執行PLC 階梯圖程式撰寫：Develop Programmable Logic Controller (PLC) ladder logic programs for industrial automation sequences including motor control, valve sequencing, inter

**本步驟交付物**：
- PLC Ladder Logic Source Code: documented rung-by-rung implementation with inline comments, addressing IEC 61131-3 conventions
- Logic Documentation: rung descriptions, function block usage, variable/tag definitions, cross-reference lists (which rung affects which output)
- I/O Mapping Verification: source/sink addressing validation, unused I/O identification, conflict detection (e.g., contradictory command logic)

### Step 2: 結構化文字程式開發
**SK 來源**：SK-D05-008 — Structured Text Programming

執行結構化文字程式開發：Develop Structured Text (ST) programs per IEC 61131-3 standard for complex control algorithms, mathematical computations, and state machine implementa

**本步驟交付物**：
- Structured Text Source Code: documented function blocks and programs with inline comments, adhering to IEC 61131-3 syntax and naming conventions
- Algorithm Implementation Document: function block descriptions, algorithm flow diagrams, variable definitions, data type specifications
- Unit Test Suite: test cases covering all major code paths, boundary conditions, error handling, expected outputs with acceptance criteria

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | PLC Ladder Logic Source Code: documented rung-by-rung implementation with inline comments, addressing IEC 61131-3 conventions | 依需求 |
| 2 | Logic Documentation: rung descriptions, function block usage, variable/tag definitions, cross-reference lists (which rung affects which output) | Markdown |
| 3 | I/O Mapping Verification: source/sink addressing validation, unused I/O identification, conflict detection (e.g., contradictory command logic) | 依需求 |
| 4 | Test Plan: unit test cases for each major logic block (motor sequence, valve control, interlocking), acceptance criteria | 依需求 |
| 5 | Safety Logic Verification Report: proof that safety interlocks are correctly implemented, timing analysis for critical sequences | Markdown |
| 6 | Programmer's Guide: installation instructions, program load procedure, parameter adjustment procedures, troubleshooting checklist | Markdown |
| 7 | Structured Text Source Code: documented function blocks and programs with inline comments, adhering to IEC 61131-3 syntax and naming conventions | 依需求 |
| 8 | Algorithm Implementation Document: function block descriptions, algorithm flow diagrams, variable definitions, data type specifications | 依需求 |
| 9 | Unit Test Suite: test cases covering all major code paths, boundary conditions, error handling, expected outputs with acceptance criteria | 依需求 |
| 10 | Performance Analysis Report: execution time per function block, memory utilization, latency impact on control loop response time | Markdown |
| 11 | Code Review Checklist: validation against software development standards (SK-D09-005), security review against access control policy (SK-D01-020) | Markdown |
| 12 | Integration and System Test Plan: ST program interaction with other PLC logic (ladder logic, other ST blocks), SCADA signal verification | 依需求 |

---

## 4. 適用標準

- IEC 61131-3: Programmable controllers — Part 3: Programming languages (ladder diagram syntax and semantics)
- IEC 61508: Functional Safety of Electrical/Electronic/Programmable Electronic Safety-Related Systems (if SIL-rated logic
- IEC 62061: Safety of machinery — Functional safety of safety-related control systems
- IEC 62443-3-3: System Security Requirements and Security Levels — control system security requirements for PLC configura
- IEC 62443-4-1: Security of Product Development — secure PLC firmware and configuration management
- Vendor-Specific Programming Standards: manufacturer best practices for code readability and maintainability
- IEC 61131-3: Programmable controllers — Part 3: Programming languages (Structured Text syntax, semantics, and execution 
- IEC 61508: Functional Safety of Electrical/Electronic/Programmable Electronic Safety-Related Systems (if safety-critical
- IEC 62443-3-3: System Security Requirements and Security Levels — control system security and integrity requirements
- IEC 62443-4-1: Security of Product Development — secure software development practices and version control

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | All logic blocks specified in the design are implemented in ladder logic with cl | ✅ 已驗證 |
| 2 | I/O mapping is verified end-to-end: every tag is addressed, no conflicts between | ✅ 已驗證 |
| 3 | Safety-critical interlocks (e.g., preventing simultaneous contradictory commands | ✅ 已驗證 |
| 4 | Timing analysis confirms that critical sequences (e.g., motor start ramp time) m | ✅ 已驗證 |
| 5 | Static code analysis (IEC 61131-3 compliance checker) confirms syntax correctnes | ✅ 已驗證 |
| 6 | Unit test cases cover 100% of major logic blocks with documented pass/fail resul | ✅ 已驗證 |
| 7 | PLC program is under version control (Git/SVN) with documented change history an | ✅ 已驗證 |
| 8 | Program change authorization follows SK-D10-003 procedures: approval log, baseli | ✅ 已驗證 |
| 9 | All algorithm functions specified in the design are implemented in ST with corre | ✅ 已驗證 |
| 10 | ST source code adheres to IEC 61131-3 syntax and complies with software developm | ✅ 已驗證 |
| 11 | All variables are declared with explicit data types; no implicit type conversion | ✅ 已驗證 |
| 12 | Unit test cases cover 100% of major code paths (including error handling and bou | ✅ 已驗證 |
| 13 | Performance analysis confirms that ST program execution time fits within the PLC | ✅ 已驗證 |
| 14 | Code review (per SK-D09-005) confirms readability, maintainability, and complian | ✅ 已驗證 |
| 15 | Algorithm integrity verification (per SK-D10-002) is implemented: checksum/hash  | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D05-007 | | Junior (< 2 yr) | 5–10 person-days | Assumes straightforward logic (20–50 rungs), single PLC, <30  |
| SK-D05-007 | | Senior (5+ yr) | 2–5 person-days | Same scope; senior leverages reusable ladder logic templates an |
| SK-D05-007 | Notes: Complex interlocking (>100 rungs), multi-PLC coordination, or SIL-rated safety logic may requ |
| SK-D05-008 | | Junior (< 2 yr) | 8–15 person-days | Assumes 200–400 lines of ST code, 2–4 function blocks, straig |
| SK-D05-008 | | Senior (5+ yr) | 4–8 person-days | Same scope; senior leverages reusable ST templates, rapid algor |
| SK-D05-008 | Notes: Complex state machines (>5 states), mathematical optimization algorithms, or multi-threaded c |

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
PLC 程式開發已完成。
📋 執行範圍：2 個工程步驟（SK-D05-007, SK-D05-008）
📊 交付物清單：
  - PLC Ladder Logic Source Code: documented rung-by-rung implementation with inline comments, addressing IEC 61131-3 conventions
  - Logic Documentation: rung descriptions, function block usage, variable/tag definitions, cross-reference lists (which rung affects which output)
  - I/O Mapping Verification: source/sink addressing validation, unused I/O identification, conflict detection (e.g., contradictory command logic)
  - Test Plan: unit test cases for each major logic block (motor sequence, valve control, interlocking), acceptance criteria
  - Safety Logic Verification Report: proof that safety interlocks are correctly implemented, timing analysis for critical sequences
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
| SK 覆蓋 | SK-D05-007, SK-D05-008 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D05-007 | PLC Ladder Logic Programming | PLC 階梯圖程式撰寫 | Develop Programmable Logic Controller (PLC) ladder logic pro |
| SK-D05-008 | Structured Text Programming | 結構化文字程式開發 | Develop Structured Text (ST) programs per IEC 61131-3 standa |

<!-- Phase 5 Wave 2 deepened: SK-D05-007, SK-D05-008 -->