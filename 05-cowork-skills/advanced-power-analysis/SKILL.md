---
name: advanced-power-analysis
description: >
  進階電力分析與模擬。
  Analyze harmonic distortion in electrical networks caused by power electronics devices (inverters, variable frequency drives, rectifiers) and design p。Simulate transient stability behavior of power systems under fault and disturbance conditions using
  MANDATORY TRIGGERS: 諧波分析與濾波器設計, 暫態穩定度模擬, 進階電力分析與模擬, 電力系統建模, VFD, Harmonic Analysis and Filter Design, Transient Stability Simulation, PSS/E, harmonic-distortion, Power System Modeling (ETAP/PSS/E), network-model, power-quality.
  Use this skill for advanced power analysis tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 進階電力分析與模擬

本 Skill 整合 3 個工程技能定義，提供進階電力分析與模擬的完整工作流程。
適用領域：Power System Analysis（D03）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D03-001, SK-D03-002, SK-D03-003, SK-D03-004, SK-D06-006, SK-D08-001

---

## 1. 輸入

- Power System Model with component impedance details (from SK-D03-010: Power System Modeling)
- Equipment inventory specifying power electronics (inverters, VFDs, rectifiers, switching power supplies):
- Device type, rating, control mode
- Switching frequency and modulation type
- Current injection characteristics and harmonic spectra (from manufacturer or measurement)
- Geographic location and interconnection point
- Power System Model with dynamic generator models (from SK-D03-010: Power System Modeling):
- Synchronous machine models (subtransient, transient reactances, time constants)
- Generator control models (automatic voltage regulators, speed governors, stabilizers)
- Load models (frequency-dependent load behavior, motor startup transients)
- FACTS device models (if present: SVC, STATCOM, HVDC controllers)
- Short-circuit analysis and system X/R ratios (from SK-D03-002: Short Circuit Analysis)

---

## 2. 工作流程

### Step 1: 諧波分析與濾波器設計
**SK 來源**：SK-D03-008 — Harmonic Analysis and Filter Design

執行諧波分析與濾波器設計：Analyze harmonic distortion in electrical networks caused by power electronics devices (inverters, variable frequency drives, rectifiers) and design p

**本步驟交付物**：
- Harmonic Analysis Report including:
- Identified harmonic sources and their current injection characteristics
- Harmonic current propagation and voltage distortion throughout the network

### Step 2: 暫態穩定度模擬
**SK 來源**：SK-D03-009 — Transient Stability Simulation

執行暫態穩定度模擬：Simulate transient stability behavior of power systems under fault and disturbance conditions using time-domain simulation tools (ETAP, PSS/E). Determ

**本步驟交付物**：
- Transient Stability Study Report including:
- Rotor angle, frequency, and voltage time-domain profiles for each synchronous generator and critical bus
- Generator stability margin assessment: swing curves showing stability or instability outcome

### Step 3: 電力系統建模
**SK 來源**：SK-D03-010 — Power System Modeling (ETAP/PSS/E)

執行電力系統建模：Build and maintain power system simulation models in ETAP and/or PSS/E software platforms, including comprehensive network topology representation, co

**本步驟交付物**：
- ETAP and/or PSS/E Power System Model Files:
- Complete network model with all buses, branches, and components
- Validated against baseline power flow and short-circuit data

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Harmonic Analysis Report including: | Markdown |
| 2 | Identified harmonic sources and their current injection characteristics | 依需求 |
| 3 | Harmonic current propagation and voltage distortion throughout the network | 依需求 |
| 4 | Bus-by-bus harmonic voltage and current profiles | 依需求 |
| 5 | Identification of resonance conditions (if present) | 依需求 |
| 6 | Comparison to IEEE 519 and customer compatibility limits | 依需求 |
| 7 | Transient Stability Study Report including: | Markdown |
| 8 | Rotor angle, frequency, and voltage time-domain profiles for each synchronous generator and critical bus | 依需求 |
| 9 | Generator stability margin assessment: swing curves showing stability or instability outcome | 依需求 |
| 10 | Critical clearing time (CCT) for each defined fault scenario (time at which fault must be cleared to avoid instability) | 依需求 |
| 11 | System frequency deviation and inertial response during and after fault | 依需求 |
| 12 | Oscillation frequency and damping ratio assessment (identification of poorly damped electromechanical modes) | 依需求 |

---

## 4. 適用標準

- IEEE Std 519-2022: IEEE Recommended Practices and Requirements for Harmonic Control in Electric Power Systems
- IEC 61000-2-2: Electromagnetic compatibility (EMC) — Environment — compatibility levels for industrial establishments
- IEC 61000-3-6: Electromagnetic compatibility (EMC) — Limits for harmonic current emissions
- IEC 61000-4-7: Electromagnetic compatibility (EMC) — Testing and measurement techniques — general guide on harmonics and
- IEC 62443-3-2: Security Risk Assessment — power quality faults as indicators of system compromise
- NEMA TR4: NEMA Application Guide for AC Adjustable Frequency Power Drive Systems
- IEEE Std 399: IEEE Recommended Practice for Industrial and Commercial Power Systems Analysis
- IEEE Std 1159: IEEE Recommended Practice for Monitoring Electric Power Quality
- NERC Reliability Standards:
- EOP-005: System Restoration (stability during black-start and restoration)

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Harmonic analysis covers all non-linear loads and power electronics devices in t | ✅ 已驗證 |
| 2 | Harmonic voltage and current distortion calculated at minimum at all network bus | ✅ 已驗證 |
| 3 | All predicted harmonic levels comply with IEEE 519 Recommended Practice (or cust | ✅ 已驗證 |
| 4 | Filter design validated with resonance analysis: no resonance peaks near power e | ✅ 已驗證 |
| 5 | Individual harmonic attenuation (at least 3rd, 5th, 7th, 11th, 13th) and filter  | ✅ 已驗證 |
| 6 | Power factor impact of filter installation assessed; no capacitor over-voltage c | ✅ 已驗證 |
| 7 | Filter sizing validated for continuous operation and transient overload conditio | ✅ 已驗證 |
| 8 | Harmonic analysis and filter design reviewed and approved by SYS, PRAC, and veri | ✅ 已驗證 |
| 9 | Dynamic system model includes all synchronous generators, AVRs, governors, and l | ✅ 已驗證 |
| 10 | Transient stability simulation covers minimum 15 defined contingency scenarios ( | ✅ 已驗證 |
| 11 | Critical clearing times (CCT) determined for all high-severity contingencies; no | ✅ 已驗證 |
| 12 | All generator rotor angle swings remain < 90° during faults and return to stable | ✅ 已驗證 |
| 13 | System frequency deviation stays within ±5% (or customer-specified limit) and re | ✅ 已驗證 |
| 14 | Protection relay clearing times shown to be achievable and coordinated with stab | ✅ 已驗證 |
| 15 | Damping of post-fault oscillations assessed: damping ratio > 0.05 (5%) for criti | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D03-008 | | Junior (< 2 yr) | 8–12 person-days | Assumes single-site harmonic survey, 3–5 non-linear loads, pa |
| SK-D03-008 | | Senior (5+ yr) | 4–7 person-days | Same scope; senior leverages filter design templates and prior  |
| SK-D03-008 | Notes: Complex systems with multiple interconnected networks or custom active filter tuning may requ |
| SK-D03-009 | | Junior (< 2 yr) | 12–18 person-days | Assumes medium system (15–20 generators), 10–15 contingency  |
| SK-D03-009 | | Senior (5+ yr) | 6–10 person-days | Same scope; senior leverages prior contingency lists, standard |
| SK-D03-009 | Notes: Large systems (50+ generators, multi-area) may require 1.5–2× effort. Custom generator contro |
| SK-D03-010 | | Junior (< 2 yr) | 15–25 person-days | Assumes medium-complexity system (10–20 generators, 30–50 bu |
| SK-D03-010 | | Senior (5+ yr) | 8–12 person-days | Same scope; senior leverages template models and parameter dat |

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
進階電力分析與模擬已完成。
📋 執行範圍：3 個工程步驟（SK-D03-008, SK-D03-009, SK-D03-010）
📊 交付物清單：
  - Harmonic Analysis Report including:
  - Identified harmonic sources and their current injection characteristics
  - Harmonic current propagation and voltage distortion throughout the network
  - Bus-by-bus harmonic voltage and current profiles
  - Identification of resonance conditions (if present)
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
| SK 覆蓋 | SK-D03-008, SK-D03-009, SK-D03-010 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D03-008 | Harmonic Analysis and Filter Design | 諧波分析與濾波器設計 | Analyze harmonic distortion in electrical networks caused by |
| SK-D03-009 | Transient Stability Simulation | 暫態穩定度模擬 | Simulate transient stability behavior of power systems under |
| SK-D03-010 | Power System Modeling (ETAP/PSS/E) | 電力系統建模 | Build and maintain power system simulation models in ETAP an |

<!-- Phase 5 Wave 2 deepened: SK-D03-008, SK-D03-009, SK-D03-010 -->