---
name: power-system-base-analysis
description: >
  電力系統基礎分析。
  - Assuming base case convergence implies contingency stability—contingencies must be explicitly analyzed。- Neglecting motor contribution to fault current, resulting in underestimated fault levels。Assess voltage stability margins of power systems unde
  MANDATORY TRIGGERS: 短路電流分析, 電壓穩定度評估, 潮流分析, 電力系統基礎分析, ETAP, flow, reactive-power, Short Circuit Current Analysis, current, voltage-stability, PSS/E, Voltage Stability Assessment.
  Use this skill for power system base analysis tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 電力系統基礎分析

本 Skill 整合 3 個工程技能定義，提供電力系統基礎分析的完整工作流程。
適用領域：Power System Analysis（D03）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D03-009, SK-D03-010, SK-D04-001, SK-D04-006, SK-D06-005

---

## 1. 輸入

- Power System Model (from SK-D03-010: Power System Modeling)
- Load flow analysis results (from SK-D03-001: Power Flow Analysis)
- Short-circuit study results (from SK-D03-002: Short Circuit Analysis)
- System contingency list (N-1, N-2 scenarios)
- Operating point scenarios (light load, peak load, seasonal variations)
- Voltage stability criteria and limits (customer-specified or per IEEE 1015)

---

## 2. 工作流程

### Step 1: 潮流分析
**SK 來源**：SK-D03-001 — Power Flow Analysis

執行潮流分析：- Assuming base case convergence implies contingency stability—contingencies must be explicitly analyzed

**本步驟交付物**：
- Power flow analysis report documenting base case and contingency voltage profiles
- Equipment loading summary table showing maximum sustained amperage for each critical element
- Network one-line diagram annotated with normal and contingency power flows

### Step 2: 短路電流分析
**SK 來源**：SK-D03-002 — Short Circuit Current Analysis

執行短路電流分析：- Neglecting motor contribution to fault current, resulting in underestimated fault levels

**本步驟交付物**：
- Short circuit current analysis report documenting methodology, assumptions, and all calculated fault currents
- Fault current summary table showing magnitude, X/R ratio, and transient peak current for minimum 15 locations
- Network impedance consolidation spreadsheet showing source impedance buildup from utility to each fault location

### Step 3: 電壓穩定度評估
**SK 來源**：SK-D03-003 — Voltage Stability Assessment

執行電壓穩定度評估：Assess voltage stability margins of power systems under various loading conditions and contingency scenarios. Identifies voltage collapse risks and de

**本步驟交付物**：
- Voltage Stability Assessment Report detailing:
- V-Q sensitivity analysis at critical buses
- Voltage collapse point estimation under contingency scenarios

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Power flow analysis report documenting base case and contingency voltage profiles | Markdown |
| 2 | Equipment loading summary table showing maximum sustained amperage for each critical element | 依需求 |
| 3 | Network one-line diagram annotated with normal and contingency power flows | 依需求 |
| 4 | Zone boundary recommendations based on minimum inter-zone power exchange rates | 依需求 |
| 5 | Sensitivity analysis results showing system behavior under load ±10% variation | 依需求 |
| 6 | Solver convergence logs and timestamp documentation of analysis completion | 依需求 |
| 7 | Short circuit current analysis report documenting methodology, assumptions, and all calculated fault currents | Markdown |
| 8 | Fault current summary table showing magnitude, X/R ratio, and transient peak current for minimum 15 locations | 依需求 |
| 9 | Network impedance consolidation spreadsheet showing source impedance buildup from utility to each fault location | 依需求 |
| 10 | Protective device duty curve overlays showing calculated fault current against device interrupting rating | 依需求 |
| 11 | Equipment specification summary: transformer withstand ratings, breaker interrupting ratings, conductor ampacity | 依需求 |
| 12 | Sensitivity analysis results: fault current variation over ±10% impedance range at critical locations | 依需求 |

---

## 4. 適用標準

- Power flow analysis is foundational to IEC 62443 security control implementation. Accurate characterization of normal op
- Short circuit current analysis establishes the fault stress parameters necessary for IEC 62443 security zone resilience 
- IEEE 1015: IEEE Guide for Induction Machinery Maintenance Testing and Failure Analysis
- IEEE Std 1159: IEEE Recommended Practice for Monitoring Electric Power Quality
- IEC 61000-2-2: Environment for industrial installations — compatibility levels
- IEC 62443-3-2: Security Risk Assessment for System Design — voltage stability as a system resilience factor
- NERC Reliability Standards: EOP-005 (System Restoration), TOP-001 (Real-Time Reliability Monitoring)

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Model convergence achieved in ≥95% of defined scenarios | ✅ 已驗證 |
| 2 | Voltage margin (difference between calculated and limit voltage) documented for  | ✅ 已驗證 |
| 3 | Report completeness verified: all network buses and branches included in results | ✅ 已驗證 |
| 4 | Stakeholder sign-off obtained on zone boundary recommendations from power flow a | ✅ 已驗證 |
| 5 | Traceability matrix linking analysis assumptions to final engineering recommenda | ✅ 已驗證 |
| 6 | Fault current calculation methodology documented and justified in technical repo | ✅ 已驗證 |
| 7 | All network impedances traced to source documentation (equipment spec sheets, te | ✅ 已驗證 |
| 8 | Calculation results independently verified at ≥5 critical locations by second en | ✅ 已驗證 |
| 9 | Sensitivity analysis performed: fault currents recalculated with ±10% impedance  | ✅ 已驗證 |
| 10 | Traceability maintained from fault location through calculation to protective de | ✅ 已驗證 |
| 11 | Results presented in consistent format with units, assumptions, and calculation  | ✅ 已驗證 |
| 12 | Voltage stability assessment covers all critical system buses and 100% of define | ✅ 已驗證 |
| 13 | Voltage collapse margin determined with documented methodology (e.g., VLmin, rea | ✅ 已驗證 |
| 14 | All buses maintain voltage within specified limits (typically ±10% of nominal) u | ✅ 已驗證 |
| 15 | Reactive power compensation scheme specified with explicit device types, locatio | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D03-003 | | Junior (< 2 yr) | 10–15 person-days | Assumes medium system (10–20 buses), 5–10 contingency scenar |
| SK-D03-003 | | Senior (5+ yr) | 5–8 person-days | Same scope; senior leverages prior analysis tools and pattern r |
| SK-D03-003 | Notes: Large transmission systems (50+ buses) or novel grid topologies (high renewable penetration)  |

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
電力系統基礎分析已完成。
📋 執行範圍：3 個工程步驟（SK-D03-001, SK-D03-002, SK-D03-003）
📊 交付物清單：
  - Power flow analysis report documenting base case and contingency voltage profiles
  - Equipment loading summary table showing maximum sustained amperage for each critical element
  - Network one-line diagram annotated with normal and contingency power flows
  - Zone boundary recommendations based on minimum inter-zone power exchange rates
  - Sensitivity analysis results showing system behavior under load ±10% variation
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
| Domain | D03 (Power System Analysis) |
| SK 覆蓋 | SK-D03-001, SK-D03-002, SK-D03-003 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D03-001 | Power Flow Analysis | 潮流分析 | - Assuming base case convergence implies contingency stabili |
| SK-D03-002 | Short Circuit Current Analysis | 短路電流分析 | - Neglecting motor contribution to fault current, resulting  |
| SK-D03-003 | Voltage Stability Assessment | 電壓穩定度評估 | Assess voltage stability margins of power systems under vari |

<!-- Phase 5 Wave 2 deepened: SK-D03-001, SK-D03-002, SK-D03-003 -->