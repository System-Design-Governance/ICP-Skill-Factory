---
name: requirements-traceability
description: >
  需求與變更管理。
  - Analyze post-test gap closure data: which requirement types consistently show late closure? Refine requirement specification approach。- Analyze post-implementation change data: which impact areas consistently show estimation errors? Refine estimati
  MANDATORY TRIGGERS: 需求與變更管理, 工作許可流程管理, 變更申請評估與影響分析, 需求追溯矩陣管理, 變更管理執行, Change Request Evaluation and Impact Analysis, requirements, requirements traceability, permit, moc, Requirements Traceability Matrix Management, analysis, management.
  Use this skill for requirements traceability tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 需求與變更管理

本 Skill 整合 4 個工程技能定義，提供需求與變更管理的完整工作流程。
適用領域：Project Engineering（D10）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D10-004, SK-D10-005

---

## 1. 輸入

- Customer requirements specification (CRS) or functional specification document (FSD) approved and baselined
- System requirements specification (SRS) complete and approved
- High-level system architecture defined with major functional components identified
- IEC 62443 security level (SL) target assigned
- Verification and validation plan (V&V Plan) framework established: verification methods, test approach, acceptance criteria
- RTM tool selected and configured: spreadsheet, dedicated requirements management tool, or integrated development environment (IDE)
- Change request form and process defined: submission format, required information, routing procedures
- CCB (Configuration Control Board) established with clear authority matrix: approvers by change type/scope
- Baseline requirements, design, and test plan established and baselined
- Project schedule, budget, and resource plan baselined
- IEC 62443 security level (SL) target and threat model documented
- Security impact assessment criteria defined: what constitutes a security-affecting change

---

## 2. 工作流程

### Step 1: 需求追溯矩陣管理
**SK 來源**：SK-D10-001 — Requirements Traceability Matrix Management

執行需求追溯矩陣管理：- Analyze post-test gap closure data: which requirement types consistently show late closure? Refine requirement specification approach

### Step 2: 變更申請評估與影響分析
**SK 來源**：SK-D10-002 — Change Request Evaluation and Impact Analysis

執行變更申請評估與影響分析：- Analyze post-implementation change data: which impact areas consistently show estimation errors? Refine estimation methods

### Step 3: 變更管理執行
**SK 來源**：SK-D10-003 — Management of Change (MOC) Execution

執行變更管理執行：- Analyze MOC execution metrics: which types of changes consistently exceed schedule/cost estimates? Refine planning approach

### Step 4: 工作許可流程管理
**SK 來源**：SK-D10-007 — Permit to Work (PtW) Process Management

執行工作許可流程管理：The Permit to Work (PtW) Process Management skill establishes and maintains formal authorization procedures for controlling access to operational OT/I

**本步驟交付物**：
- Permit to Work process procedure (ID04 §12.0-aligned)
- Work permit templates (hot work, electrical, confined space, system modification)
- Risk assessment templates for each permit type

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Permit to Work process procedure (ID04 §12.0-aligned) | 依需求 |
| 2 | Work permit templates (hot work, electrical, confined space, system modification) | 依需求 |
| 3 | Risk assessment templates for each permit type | 依需求 |
| 4 | Authorization matrix and approval chain documentation | Markdown |
| 5 | Permit tracking and closure verification checklists | Markdown |
| 6 | Audit trail and record retention procedures | 依需求 |

---

## 4. 適用標準

- IEC 62443-1-1: Terminology and concepts
- IEC 62443-3-3: System design and engineering; requirements management and traceability
- IEC 62443-4-1: Product development (establishes requirements for secure product design)
- IEEE 830: Software requirements specification
- ISO/IEC/IEEE 42010: Architecture description
- Project Customer Requirements Specification (CRS) / Functional Specification Document (FSD)
- Project System Requirements Specification (SRS)
- Verification and Validation Plan (V&V Plan)
- IEC 62443-3-3: System design and engineering; Management of Change (§7.8.7, §7.8.7.1)
- IEC 62443-4-1: Product development (secure design practices)

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | RTM structure defined with all required columns (requirement, design response, t | ✅ 已驗證 |
| 2 | 100% of customer requirements identified, prioritized, and entered into RTM with | ✅ 已驗證 |
| 3 | Backward traceability verified: every design element mapped to ≥1 requirement | ✅ 已驗證 |
| 4 | Forward traceability verified: every requirement has ≥1 design response document | ✅ 已驗證 |
| 5 | Verification traceability verified: every requirement has ≥1 test case and plann | ✅ 已驗證 |
| 6 | Bi-directional traceability complete: no unmapped requirements, no orphan design | ✅ 已驗證 |
| 7 | Change control process implemented: all RTM changes require approval and impact  | ✅ 已驗證 |
| 8 | RTM baseline approved by customer, system architect, and QA lead | ✅ 已驗證 |
| 9 | Change request form complete with clear description, rationale, affected items,  | ✅ 已驗證 |
| 10 | Technical feasibility assessment documented: design impact, implementation appro | ✅ 已驗證 |
| 11 | Security impact assessment completed and documented (if change is security-affec | ✅ 已驗證 |
| 12 | Impact on target SL identified | ✅ 已驗證 |
| 13 | Required security verification activities defined | ✅ 已驗證 |
| 14 | Security officer sign-off obtained | ✅ 已驗證 |
| 15 | Schedule impact analysis documented: affected activities, effort estimates, crit | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D10-001 | Forward traceability: 100% of requirements have ≥1 design response; average design response time <3  |
| SK-D10-001 | Verification traceability: 100% of requirements have test case(s); average test case development tim |
| SK-D10-001 | Gap closure rate: all identified gaps tracked; 100% critical gaps closed; closure cycle time <5 busi |
| SK-D10-001 | Audit findings: RTM audits identify <5% data inconsistencies; issues corrected within 3 days |
| SK-D10-002 | Evaluation cycle time: average time from change submission to CCB decision ≤5 business days (for sta |
| SK-D10-003 | Design peer review completion: 100% of design changes reviewed by qualified peer; average review cyc |
| SK-D10-003 | Baseline release timeliness: new baseline released within 2 business days of change closure |
| SK-D10-007 | | Role | Junior (hours) | Senior (hours) | |

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
需求與變更管理已完成。
📋 執行範圍：4 個工程步驟（SK-D10-001, SK-D10-002, SK-D10-003, SK-D10-007）
📊 交付物清單：
  - Permit to Work process procedure (ID04 §12.0-aligned)
  - Work permit templates (hot work, electrical, confined space, system modification)
  - Risk assessment templates for each permit type
  - Authorization matrix and approval chain documentation
  - Permit tracking and closure verification checklists
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
| Domain | D10 (Project Engineering) |
| SK 覆蓋 | SK-D10-001, SK-D10-002, SK-D10-003, SK-D10-007 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D10-001 | Requirements Traceability Matrix Management | 需求追溯矩陣管理 | - Analyze post-test gap closure data: which requirement type |
| SK-D10-002 | Change Request Evaluation and Impact Analysis | 變更申請評估與影響分析 | - Analyze post-implementation change data: which impact area |
| SK-D10-003 | Management of Change (MOC) Execution | 變更管理執行 | - Analyze MOC execution metrics: which types of changes cons |
| SK-D10-007 | Permit to Work (PtW) Process Management | 工作許可流程管理 | The Permit to Work (PtW) Process Management skill establishe |

<!-- Phase 5 Wave 2 deepened: SK-D10-001, SK-D10-002, SK-D10-003, SK-D10-007 -->