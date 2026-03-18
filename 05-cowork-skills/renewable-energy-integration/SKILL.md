---
name: renewable-energy-integration
description: >
  可再生能源併網。
  - Assuming inverter manufacturer's anti-islanding protection is sufficient without independent verification。- Sizing BESS for peak power without considering energy duration adequacy—high power alone insufficient for grid services。Design Virtual Power
  MANDATORY TRIGGERS: PV 系統併網設計, BESS 容量規劃, 可再生能源併網, DER 聚合策略設計, VPP 調度演算法設計, system, der, bess, dispatch, strategy, DER, PV System Grid Integration Design, renewable energy integration.
  Use this skill for renewable energy integration tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 可再生能源併網

本 Skill 整合 4 個工程技能定義，提供可再生能源併網的完整工作流程。
適用領域：Power System Analysis（D03）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D03-001, SK-D03-002, SK-D03-003, SK-D03-009, SK-D03-010

---

## 1. 輸入

- Power system model and network constraints (from SK-D03-010: Power System Modeling)
- DER asset inventory with technical specifications:
- Power rating, energy capacity, ramp rates, min/max output
- Response time, control modes (voltage/frequency droop, active power-frequency, reactive power-voltage)
- Degradation models and state-of-health parameters
- Geographic location and interconnection point

---

## 2. 工作流程

### Step 1: PV 系統併網設計
**SK 來源**：SK-D03-004 — PV System Grid Integration Design

執行PV 系統併網設計：- Assuming inverter manufacturer's anti-islanding protection is sufficient without independent verification

**本步驟交付物**：
- PV system grid integration design report documenting all design decisions and calculations
- Single-line electrical diagram showing: PV array, inverter(s), disconnect switches, protection relays, transformer, grid connection point, DERMS inter
- Anti-islanding protection specification: frequency/voltage trip thresholds, passive impedance range, test procedure verification

### Step 2: BESS 容量規劃
**SK 來源**：SK-D03-005 — BESS Capacity Planning

執行BESS 容量規劃：- Sizing BESS for peak power without considering energy duration adequacy—high power alone insufficient for grid services

**本步驟交付物**：
- BESS Capacity Planning report documenting all design decisions, calculations, and justifications
- Capacity specification summary: energy capacity (MWh), power capacity (MW), energy:power ratio, duration at rated power
- Grid services specification: power and energy requirements for each service (frequency regulation, peak shaving, arbitrage, voltage support)

### Step 3: VPP 調度演算法設計
**SK 來源**：SK-D03-006 — VPP Dispatch Algorithm Design

執行VPP 調度演算法設計：Design Virtual Power Plant dispatch algorithms that optimize Distributed Energy Resource (DER) allocation based on market signals, grid operating cons

**本步驟交付物**：
- VPP Dispatch Algorithm Specification Document including:
- Objective function(s) with mathematical formulation and weights
- Decision variables (DER power setpoints, storage charging/discharging, load control)

### Step 4: DER 聚合策略設計
**SK 來源**：SK-D03-007 — DER Aggregation Strategy Design

執行DER 聚合策略設計：- Assuming aggregation communication latency can be ignored: 100ms latency is critical for frequency response

**本步驟交付物**：
- DER Aggregation Strategy Design report documenting all aggregation decisions and rationale
- DER asset inventory: location, type, capacity, control capability, communication interface for all assets
- Aggregation topology diagram: DERMS, aggregator hierarchy, aggregation groups, DER assets with connectivity

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | PV system grid integration design report documenting all design decisions and calculations | Markdown |
| 2 | Single-line electrical diagram showing: PV array, inverter(s), disconnect switches, protection relays, transformer, grid connection point, DERMS inter | 依需求 |
| 3 | Anti-islanding protection specification: frequency/voltage trip thresholds, passive impedance range, test procedure verification | 依需求 |
| 4 | Power quality analysis report: harmonic spectrum analysis, flicker calculation results, compliance verification | Markdown |
| 5 | DERMS communication interface specification: protocol selection, data point list, update frequency, security requirements | Markdown |
| 6 | Protection relay coordination study: trip point summary table, time-current characteristic curves | 依需求 |
| 7 | BESS Capacity Planning report documenting all design decisions, calculations, and justifications | Markdown |
| 8 | Capacity specification summary: energy capacity (MWh), power capacity (MW), energy:power ratio, duration at rated power | 依需求 |
| 9 | Grid services specification: power and energy requirements for each service (frequency regulation, peak shaving, arbitrage, voltage support) | 依需求 |
| 10 | Charge/discharge protocol design: power profile diagram for each grid service, daily cycle definition, maximum depth-of-discharge | 依需求 |
| 11 | State-of-charge management strategy: minimum/maximum operating SOC values, emergency reserve quantity, reserve release policy | 依需求 |
| 12 | Cycle life analysis: projected equivalent full cycles over system lifetime, degradation curve showing capacity fade vs. time | 依需求 |

---

## 4. 適用標準

- PV system grid integration design is critical to IEC 62443 control system security. The communication interfaces connect
- BESS capacity planning is foundational to IEC 62443 security in energy systems. The EMS/DERMS communication interfaces t
- IEC 62443-3-3: System Security Requirements and Security Levels — control system resilience and secure dispatch logic
- IEEE 1547: Standard for Interconnection and Interoperability of Distributed Energy and Storage Devices with Associated E
- NERC CIP-005, CIP-007: Cyber security standards for critical DER control systems
- ISO 50001: Energy Management Systems — efficiency targets in dispatch algorithm design
- Market rules (CAISO, ERCOT, PJM, etc.) for reserve and ancillary service participation if grid-connected
- DER aggregation strategy design is critical to IEC 62443 security in distributed energy systems. The DERMS platform and 

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Anti-islanding protection verified through simulation per IEEE 1547 test procedu | ✅ 已驗證 |
| 2 | Harmonic distortion analysis completed with grid impedance variation: THD remain | ✅ 已驗證 |
| 3 | Voltage flicker analysis: flicker perception probability <1% per IEC 61000-3-7 | ✅ 已驗證 |
| 4 | DERMS communication specification: protocol choice justified, latency quantified | ✅ 已驗證 |
| 5 | Protection relay coordination: all trip sequences verified to prevent unwanted c | ✅ 已驗證 |
| 6 | Grid operator review: design submitted and approved per interconnection requirem | ✅ 已驗證 |
| 7 | Power capacity justified: maximum of simultaneous charging, discharging, and ser | ✅ 已驗證 |
| 8 | Energy capacity justified: minimum 4-hour duration standard applied, specific en | ✅ 已驗證 |
| 9 | Cycle life analysis completed: projected cycles over 10-year life span with spec | ✅ 已驗證 |
| 10 | Cost analysis: LCOE calculated and compared to alternative technologies for iden | ✅ 已驗證 |
| 11 | SOC management strategy: operating window defined, minimum reserve quantified, e | ✅ 已驗證 |
| 12 | EMS/DERMS communication specification complete: protocol choice justified, data  | ✅ 已驗證 |
| 13 | Thermal analysis: maximum temperature during sustained discharge confirmed withi | ✅ 已驗證 |
| 14 | Objective function explicitly defined with mathematical formulation and all deci | ✅ 已驗證 |
| 15 | Constraint set covers 100% of grid operating limits (voltage, frequency, thermal | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D03-006 | | Junior (< 2 yr) | 20–30 person-days | Assumes single-objective optimization, 5–10 DER assets, medi |
| SK-D03-006 | | Senior (5+ yr) | 10–15 person-days | Same scope; senior leverages optimization libraries, prior di |
| SK-D03-006 | Notes: Multi-objective dispatch (revenue + emissions + resilience) or large DER fleet (50+ assets) m |

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
可再生能源併網已完成。
📋 執行範圍：4 個工程步驟（SK-D03-004, SK-D03-005, SK-D03-006, SK-D03-007）
📊 交付物清單：
  - PV system grid integration design report documenting all design decisions and calculations
  - Single-line electrical diagram showing: PV array, inverter(s), disconnect switches, protection relays, transformer, grid connection point, DERMS inter
  - Anti-islanding protection specification: frequency/voltage trip thresholds, passive impedance range, test procedure verification
  - Power quality analysis report: harmonic spectrum analysis, flicker calculation results, compliance verification
  - DERMS communication interface specification: protocol selection, data point list, update frequency, security requirements
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
| SK 覆蓋 | SK-D03-004, SK-D03-005, SK-D03-006, SK-D03-007 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D03-004 | PV System Grid Integration Design | PV 系統併網設計 | - Assuming inverter manufacturer's anti-islanding protection |
| SK-D03-005 | BESS Capacity Planning | BESS 容量規劃 | - Sizing BESS for peak power without considering energy dura |
| SK-D03-006 | VPP Dispatch Algorithm Design | VPP 調度演算法設計 | Design Virtual Power Plant dispatch algorithms that optimize |
| SK-D03-007 | DER Aggregation Strategy Design | DER 聚合策略設計 | - Assuming aggregation communication latency can be ignored: |

<!-- Phase 5 Wave 2 deepened: SK-D03-004, SK-D03-005, SK-D03-006, SK-D03-007 -->