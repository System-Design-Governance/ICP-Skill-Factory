---
name: gate0-decision-package
description: >
  Gate 0 決策與成本分析。
  Assemble, verify completeness of, and package the Gate 0 decision package that consolidates all Pre-Gate 0 deliverables into a structured submission f。Cost Risk Contingency Analysis evaluates cost exposure and calculates risk-adjusted contingency res
  MANDATORY TRIGGERS: Gate 0 決策與成本分析, Gate 0 決策包組裝, 成本風險餘裕分析, contingency-planning, governance, decision-package, gate-review, gate0 decision package, Pre-R0, Gate 0 Decision Package Assembly, risk-analysis.
  Use this skill for gate0 decision package tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# Gate 0 決策與成本分析

本 Skill 整合 2 個工程技能定義，提供Gate 0 決策與成本分析的完整工作流程。
適用領域：Pre-Gate & Presales（D14）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D14-001, SK-D14-003, SK-D14-004, SK-D14-005, SK-D14-006, SK-D14-008

---

## 1. 輸入

- Requirement clarification record (from SK-D14-001 + stakeholder Q&A records)
- Risk pre-disclosure list (from SK-D14-003 — risk identification output)
- Feasibility assessment (from SK-D14-003)
- CBOM (from SK-D14-005)
- Concept architecture (from SK-D14-013 ⏳)
- Preliminary security classification (from SK-D14-014) — supports scope stability assessment
- Component Bill of Materials (CBOM) with unit costs from SK-D14-005 ⏳
- Risk matrix and cost risk assessments from SK-D14-004 ⏳
- Labor hours and staffing estimates from SK-D14-006 ⏳
- Historical cost variance data from similar projects (if available)
- Market volatility and supply chain risk factors
- Currency exchange rates (for multi-region deployments)

---

## 2. 工作流程

### Step 1: Gate 0 決策包組裝
**SK 來源**：SK-D14-015 — Gate 0 Decision Package Assembly

執行Gate 0 決策包組裝：Assemble, verify completeness of, and package the Gate 0 decision package that consolidates all Pre-Gate 0 deliverables into a structured submission f

**本步驟交付物**：
- Gate 0 Decision Package:
- Package cover sheet: project name, customer, package version, submission date, Pre-Gate Design Support owner
- Completeness checklist: all 5 mandatory inputs verified present and current

### Step 2: 成本風險餘裕分析
**SK 來源**：SK-D14-016 — Cost Risk Contingency Analysis

執行成本風險餘裕分析：Cost Risk Contingency Analysis evaluates cost exposure and calculates risk-adjusted contingency reserves for the Component Bill of Materials (CBOM) an

**本步驟交付物**：
- Cost Risk Assessment Report identifying cost drivers and exposure areas
- Contingency Reserve Calculation showing base cost, risk factors, and contingency percentage
- Risk-Adjusted Project Budget with low/baseline/high scenarios

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Gate 0 Decision Package: | 依需求 |
| 2 | Package cover sheet: project name, customer, package version, submission date, Pre-Gate Design Support owner | 依需求 |
| 3 | Completeness checklist: all 5 mandatory inputs verified present and current | Markdown |
| 4 | Quality threshold assessment: | 依需求 |
| 5 | Comprehensibility: are the deliverables understandable to Gate 0 reviewers? | 依需求 |
| 6 | Evaluability: do the deliverables contain sufficient information for informed decision-making? | 依需求 |
| 7 | Cost Risk Assessment Report identifying cost drivers and exposure areas | Markdown |
| 8 | Contingency Reserve Calculation showing base cost, risk factors, and contingency percentage | 依需求 |
| 9 | Risk-Adjusted Project Budget with low/baseline/high scenarios | 依需求 |
| 10 | Contingency Allocation by risk category (supply chain, labor escalation, scope change, technical) | 依需求 |
| 11 | Cost Risk Mitigation strategies and triggers for contingency draw-down | 依需求 |
| 12 | Cost Baseline and Budget Constraint documentation for Gate 0 approval | 依需求 |

---

## 4. 適用標準

- GOV-SD: Gate 0 framework — 5 mandatory inputs, 4 quality thresholds, blocking conditions, responsibility handover within
- GOV-SDP: Pre-Gate Design Support Role — Gate 0 package quality is a role KPI; responsibility handover marks end of Pre-G
- ID01 §6.5.1.1.3: Gate 0 review requirements
- ID03 §5.5.2: Security program activities — Gate 0 as project initiation gate
- IEC 62443-1-1:2013 "Cybersecurity for industrial automation and control systems – Part 1-1"
- PMBOK (Project Management Body of Knowledge) Guide – 6th Edition or later
- ISO 21500:2021 "Guidance on project management"
- NIST SP 800-82 "Guide to ICS Security"

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | All 5 mandatory Gate 0 inputs present and verified current: requirement clarific | ✅ 已驗證 |
| 2 | Quality threshold assessment completed for all 4 thresholds (comprehensibility,  | ✅ 已驗證 |
| 3 | Cross-reference matrix demonstrates traceability: requirements → feasibility → C | ✅ 已驗證 |
| 4 | Known gaps and open issues documented with owner and proposed resolution path —  | ✅ 已驗證 |
| 5 | Gate 0 briefing summary produced: 2–3 page executive summary covering project ov | ✅ 已驗證 |
| 6 | Pre-Gate 0 responsibility handover note prepared: confirms 15-working-day handov | ✅ 已驗證 |
| 7 | Cost Risk Assessment Report identifies at minimum 5 distinct cost risk drivers w | ✅ 已驗證 |
| 8 | Contingency Reserve Calculation shows base cost, risk adjustments, and contingen | ✅ 已驗證 |
| 9 | Risk-Adjusted Budget includes three scenarios: low (base – minimal contingency), | ✅ 已驗證 |
| 10 | Contingency allocation by category (supply chain, labor, scope, technical) sums  | ✅ 已驗證 |
| 11 | Cost sensitivity analysis quantifies impact of at minimum 3 key risk materializa | ✅ 已驗證 |
| 12 | Cost Risk Mitigation strategies are documented with specific triggers for contin | ✅ 已驗證 |
| 13 | Cost Baseline and contingency reserve approved by Finance and Project Leadership | ✅ 已驗證 |
| 14 | Contingency reserve is formally separated in budget documentation (not hidden in | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D14-015 | | Junior (< 2 yr) | 3–5 person-days | Assumes all 5 inputs already produced; includes assembly, qual |
| SK-D14-015 | | Senior (5+ yr) | 2–3 person-days | Same scope; senior conducts efficient quality assessment and ra |

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
Gate 0 決策與成本分析已完成。
📋 執行範圍：2 個工程步驟（SK-D14-015, SK-D14-016）
📊 交付物清單：
  - Gate 0 Decision Package:
  - Package cover sheet: project name, customer, package version, submission date, Pre-Gate Design Support owner
  - Completeness checklist: all 5 mandatory inputs verified present and current
  - Quality threshold assessment:
  - Comprehensibility: are the deliverables understandable to Gate 0 reviewers?
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
| SK 覆蓋 | SK-D14-015, SK-D14-016 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D14-015 | Gate 0 Decision Package Assembly | Gate 0 決策包組裝 | Assemble, verify completeness of, and package the Gate 0 dec |
| SK-D14-016 | Cost Risk Contingency Analysis | 成本風險餘裕分析 | Cost Risk Contingency Analysis evaluates cost exposure and c |

<!-- Phase 5 Wave 2 deepened: SK-D14-015, SK-D14-016 -->