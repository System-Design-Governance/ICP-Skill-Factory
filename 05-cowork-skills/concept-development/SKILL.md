---
name: concept-development
description: >
  概念設計與初步評估。
  Concept Zone/Conduit Architecture development is the lightweight, advisory predecessor to the full Zone/Conduit Architecture Design skill (SK-D01-001)。Perform the preliminary security classification for the SuC, establishing initial Security Level Ta
  MANDATORY TRIGGERS: 概念 Zone/Conduit 架構, 概念設計與初步評估, Pre-Gate 0 需求釐清與可行性輸入, 初步安全分類, Gate-0, requirement-clarification, concept-design, security-classification, zone-conduit, IEC-62443, governance-alignment, feasibility-input.
  Use this skill for concept development tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 概念設計與初步評估

本 Skill 整合 3 個工程技能定義，提供概念設計與初步評估的完整工作流程。
適用領域：Pre-Gate & Presales（D14）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D14-001, SK-D14-003, SK-D14-005, SK-D14-010, SK-D14-011, SK-D14-012

---

## 1. 輸入

- Customer operational requirements and constraints from SK-D14-001 ⏳
- Site survey findings and network topology from SK-D14-011 ⏳
- Infrastructure inventory and discovery data from SK-D14-012 ⏳
- Security classification and protection profile from SK-D14-014 ⏳
- Regulatory and standards alignment requirements
- Customer risk appetite and resilience targets
- Customer/employer security requirements (from SK-D14-010)
- General requirements specification (from SK-D14-001)
- Concept Zone/Conduit architecture (from SK-D14-013 ⏳) — if available at this stage
- Existing infrastructure inventory (from SK-D14-012) — brownfield security posture baseline
- Site survey findings (from SK-D14-011) — physical security constraints
- ID03 §5.4.1: Risk classification methodology

---

## 2. 工作流程

### Step 1: 概念 Zone/Conduit 架構
**SK 來源**：SK-D14-013 — Concept Zone/Conduit Architecture

執行概念 Zone/Conduit 架構：Concept Zone/Conduit Architecture development is the lightweight, advisory predecessor to the full Zone/Conduit Architecture Design skill (SK-D01-001)

**本步驟交付物**：
- Concept Zone/Conduit architecture diagram (logical, non-binding)
- Zone/Conduit mapping to functional/operational requirements
- Preliminary security control allocation to zones

### Step 2: 初步安全分類
**SK 來源**：SK-D14-014 — Preliminary Security Classification

執行初步安全分類：Perform the preliminary security classification for the SuC, establishing initial Security Level Target (SL-T) proposals per system zone and an overal

**本步驟交付物**：
- Preliminary Security Classification Report:
- Project security risk classification: overall risk category (High / Medium / Low) with justification
- Proposed SL-T per zone: initial Security Level Target assignments based on customer requirements, industry norms, and preliminary threat landscape ass

### Step 3: Pre-Gate 0 需求釐清與可行性輸入
**SK 來源**：SK-D14-018 — Pre-Gate 0 Requirement Clarification & Feasibility Input

執行Pre-Gate 0 需求釐清與可行性輸入：Orchestrate the complete Pre-Gate 0 input preparation workflow, ensuring all 5 mandatory Gate 0 inputs are produced, quality-checked, and delivered wi

**本步驟交付物**：
- Pre-Gate 0 Workflow Tracker: status dashboard tracking all 5 mandatory inputs through their production stages
- Input Quality Pre-Check: per-input quality assessment before Gate 0 package assembly (SK-D14-015)
- Non-Binding Boundary Verification: confirmation that all Pre-Gate 0 outputs carry appropriate advisory disclaimers per GOV-SD

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Concept Zone/Conduit architecture diagram (logical, non-binding) | 依需求 |
| 2 | Zone/Conduit mapping to functional/operational requirements | 依需求 |
| 3 | Preliminary security control allocation to zones | 依需求 |
| 4 | Communication conduit specifications (bandwidth, latency, reliability requirements) | 依需求 |
| 5 | Architectural assumptions and dependencies documentation | 依需求 |
| 6 | Alignment statement to IEC 62443 foundational requirements (purview, lifecycle, etc.) | 依需求 |
| 7 | Preliminary Security Classification Report: | Markdown |
| 8 | Project security risk classification: overall risk category (High / Medium / Low) with justification | 依需求 |
| 9 | Proposed SL-T per zone: initial Security Level Target assignments based on customer requirements, industry norms, and preliminary threat landscape ass | 依需求 |
| 10 | Classification rationale: per-zone justification linking SL-T to customer requirements, industry sector norms, and threat exposure | 依需求 |
| 11 | Scope implications: how the proposed SL-T levels affect project scope, effort, and cost (higher SL = more controls = more effort) | 依需求 |
| 12 | Uncertainty assessment: confidence level of preliminary classification, key assumptions, and factors that may change during formal R1 assessment | 依需求 |

---

## 4. 適用標準

- IEC 62443-1-1:2013 "Cybersecurity for industrial automation and control systems – Part 1-1" §6.5.1.1
- IEC 62443-3-3:2013 "System security requirements and security levels"
- NIST SP 800-82 "Guide to Industrial Control Systems Security"
- ISO/IEC 27001:2022 "Information security management systems"
- IEC 62443-3-2: Security Risk Assessment — security level target framework
- IEC 62443-3-3: System Security Requirements — SL definitions (SL-1 through SL-4)
- ID03 §5.4.1: Risk classification matrix and methodology
- ID01 §6.5.1.2: Systems security classification — project initiation security planning
- GOV-SD: Gate 0 — preliminary security classification informs scope stability assessment; SL Decision Lifecycle begins at
- GOV-SD: Pre-Gate 0 boundary — 5 mandatory Gate 0 inputs; non-binding advisory status; 15-working-day responsibility hand

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Concept Zone/Conduit architecture diagram includes at minimum 3 security zones o | ✅ 已驗證 |
| 2 | Each zone is mapped to customer operational requirements from SK-D14-001 ⏳ | ✅ 已驗證 |
| 3 | Communication conduit specifications include required bandwidth, latency, and re | ✅ 已驗證 |
| 4 | Security control allocation to zones is documented with rationale | ✅ 已驗證 |
| 5 | Architecture documentation carries explicit "non-binding concept" label and disc | ✅ 已驗證 |
| 6 | Architectural assumptions are listed and validated against site survey findings | ✅ 已驗證 |
| 7 | Alignment statement confirms that concept architecture does not preclude detaile | ✅ 已驗證 |
| 8 | Feasibility assessment identifies preliminary technical risks and architectural  | ✅ 已驗證 |
| 9 | Project security risk classification assigned (High/Medium/Low) with documented  | ✅ 已驗證 |
| 10 | Proposed SL-T assigned per identified zone with per-zone rationale linking to sp | ✅ 已驗證 |
| 11 | Scope implications documented: how proposed SL-T levels affect project effort, c | ✅ 已驗證 |
| 12 | Uncertainty assessment included: confidence level stated, key assumptions listed | ✅ 已驗證 |
| 13 | Security ambition summary produced: one-page executive-ready document suitable f | ✅ 已驗證 |
| 14 | Classification marked as preliminary/indicative per GOV-SD — explicitly states t | ✅ 已驗證 |
| 15 | All 5 mandatory Gate 0 inputs produced and tracked through production stages — w | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D14-014 | | Junior (< 2 yr) | 3–5 person-days | Assumes medium-complexity project, ~5 zones; includes analysis |
| SK-D14-014 | | Senior (5+ yr) | 2–3 person-days | Same scope; senior leverages sector SL-T benchmarks and rapid c |
| SK-D14-018 | | Junior (< 2 yr) | 3–5 person-days | Orchestration/coordination effort only (individual deliverable |
| SK-D14-018 | | Senior (5+ yr) | 2–3 person-days | Same scope; senior manages workflow efficiently with minimal ov |
| SK-D14-018 | Notes: This is an orchestration/management overhead skill — the actual deliverable production effort |

---

## 7. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 輸入完整性 | 所有必要輸入文件已讀取並摘要 |
| 2 | 流程覆蓋 | 3 個工作步驟皆已執行並有產出 |
| 3 | 輸出完整性 | 所有交付物已產出、格式正確、非空白 |
| 4 | 標準合規 | 產出引用的標準版本正確 |
| 5 | 術語一致 | 專案術語、縮寫與 glossary 一致 |
| 6 | 跨步驟一致 | 各步驟產出間無矛盾（如數量、SL等級） |

---

## 8. 人類審核閘門

完成所有工作步驟後，暫停並向使用者提交審核：

```
概念設計與初步評估已完成。
📋 執行範圍：3 個工程步驟（SK-D14-013, SK-D14-014, SK-D14-018）
📊 交付物清單：
  - Concept Zone/Conduit architecture diagram (logical, non-binding)
  - Zone/Conduit mapping to functional/operational requirements
  - Preliminary security control allocation to zones
  - Communication conduit specifications (bandwidth, latency, reliability requirements)
  - Architectural assumptions and dependencies documentation
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
| Domain | D14 (Pre-Gate & Presales) |
| SK 覆蓋 | SK-D14-013, SK-D14-014, SK-D14-018 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D14-013 | Concept Zone/Conduit Architecture | 概念 Zone/Conduit 架構 | Concept Zone/Conduit Architecture development is the lightwe |
| SK-D14-014 | Preliminary Security Classification | 初步安全分類 | Perform the preliminary security classification for the SuC, |
| SK-D14-018 | Pre-Gate 0 Requirement Clarification & Feasibility Input | Pre-Gate 0 需求釐清與可行性輸入 | Orchestrate the complete Pre-Gate 0 input preparation workfl |

<!-- Phase 5 Wave 2 deepened: SK-D14-013, SK-D14-014, SK-D14-018 -->