---
name: control-strategy-configuration
description: >
  控制策略與配置。
  Configure Automatic Generation Control (AGC) functions within Energy Management System (EMS) platforms to implement frequency regulation and inter-are。Configure Distributed Energy Resource Management System (DERMS) strategies for DER dispatch, curtai
  MANDATORY TRIGGERS: 控制策略與配置, 頻率調節控制設計, DERMS DER 管理策略設定, 負載管理策略設計, EMS AGC 配置, PID 控制調參, DERMS DER Management Strategy Setting, inverter-based-resources, Load Management Strategy Design, participation-factor, PID-control, EMS, grid-forming, dispatch-algorithm.
  Use this skill for control strategy configuration tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 控制策略與配置

本 Skill 整合 5 個工程技能定義，提供控制策略與配置的完整工作流程。
適用領域：Control Systems（D05）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-016, SK-D01-020, SK-D02-001, SK-D03-006, SK-D03-007, SK-D04-001

---

## 1. 輸入

- Frequency Regulation Control Design (from SK-D05-014 ⏳: Frequency Regulation Control Design)
- EMS Software Platform Specification: vendor product (e.g., Siemens eMMS, ABB MMS, GE PSLV), available configuration modules
- Power System Model: bus admittance matrix, generator unit list, base case load flow
- Generator Unit Characteristics: response time, ramp rate limits (MW/min), mechanical power rating, governor droop settings
- SCADA Integration Specification (from SK-D05-001 ⏳: SCADA/RTU Architecture Design)
- Communication Network Bandwidth and Latency Data (from SK-D02-001: OT Network Topology Design)
- VPP Dispatch Algorithm Design (from SK-D03-006 ⏳: VPP Dispatch Algorithm Design)
- DER Aggregation Strategy Design (from SK-D03-007 ⏳: DER Aggregation Strategy Design)
- DERMS Platform Specification: vendor product (e.g., DNV GL Risco, AutoGrid, Stem), available optimization modules
- DER Fleet Inventory: device type, location, capacity (kW/kVAr), response time, communication protocol per resource
- Operational Envelope Data: power limits, ramping rates, minimum generation, reactive power capability, frequency support parameters
- Grid Service Requirements: frequency regulation, voltage support, demand response, congestion relief, reserve capacity

---

## 2. 工作流程

### Step 1: EMS AGC 配置
**SK 來源**：SK-D05-003 — EMS AGC Configuration

執行EMS AGC 配置：Configure Automatic Generation Control (AGC) functions within Energy Management System (EMS) platforms to implement frequency regulation and inter-are

**本步驟交付物**：
- AGC Configuration Parameter Table: ACE calculation coefficients, participation factor schedule, ramp rate limits per unit, frequency dead-band setting
- Tie-Line Bias Control Specification: bias coefficient, tie-line metering configuration, remote frequency signal integration
- Generator Unit Dispatch Logic: unit commitment algorithm, economic dispatch setpoint derivation, reserve margin maintenance

### Step 2: DERMS DER 管理策略設定
**SK 來源**：SK-D05-004 — DERMS DER Management Strategy Setting

執行DERMS DER 管理策略設定：Configure Distributed Energy Resource Management System (DERMS) strategies for DER dispatch, curtailment control, and optimization within Virtual Powe

**本步驟交付物**：
- DERMS Configuration Parameter Table: DER registration list, operational envelope constraints, priority rules for dispatch
- Dispatch Algorithm Implementation Specification: setpoint calculation logic, unit commitment constraints, economic dispatch constraints
- Grid Service Definition Matrix: service type, DER eligibility criteria, compensation mechanism, activation logic

### Step 3: PID 控制調參
**SK 來源**：SK-D05-012 — PID Control Tuning

執行PID 控制調參：Tune Proportional-Integral-Derivative (PID) controller parameters for critical process control loops in power generation, distribution, and energy sto

**本步驟交付物**：
- PID Tuning Report: selected tuning methodology, calculated parameters (Kp, Ki, Kd), anti-windup configuration, rationale and validation results
- Tuning Parameter Configuration: PLC/DCS configuration files (.csv, .xml, or vendor-specific export format) with final Kp, Ki, Kd, integral time limit,
- Loop Performance Validation Test Results: step response curves, frequency response plots (Bode diagrams if applicable), measurement of overshoot, sett

### Step 4: 負載管理策略設計
**SK 來源**：SK-D05-013 — Load Management Strategy Design

執行負載管理策略設計：Design load management strategies for demand response, load shedding, and load balancing in power distribution networks. This skill covers load priori

**本步驟交付物**：
- Load Management Strategy Document: overall philosophy and governance for load management, including performance objectives (peak reduction targets, re
- Load Priority Classification and Shedding Scheme Definition: categorized load groups (critical/high/medium/low priority), automatic shed stages with l
- Demand Response Integration Specification: interface with DERMS for demand-side flexibility, aggregator enrollment, incentive mechanisms, and telemetr

### Step 5: 頻率調節控制設計
**SK 來源**：SK-D05-014 — Frequency Regulation Control Design

執行頻率調節控制設計：Design frequency regulation control algorithms for grid-connected generation and energy storage assets, including droop control, Automatic Generation 

**本步驟交付物**：
- Frequency Regulation Strategy Document: overall framework for frequency control including primary response targets, AGC participation model, inertial 
- Primary Frequency Response Specification: droop control settings for synchronous and inverter-based generation, including gains (droop slope in Hz/MW)
- Synthetic Inertia Specification: virtual inertia algorithms for IBRs, including inertial response gain, damping ratio, and rate-of-change-of-frequency

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | AGC Configuration Parameter Table: ACE calculation coefficients, participation factor schedule, ramp rate limits per unit, frequency dead-band setting | 依需求 |
| 2 | Tie-Line Bias Control Specification: bias coefficient, tie-line metering configuration, remote frequency signal integration | 依需求 |
| 3 | Generator Unit Dispatch Logic: unit commitment algorithm, economic dispatch setpoint derivation, reserve margin maintenance | 依需求 |
| 4 | AGC Performance Monitoring Dashboard Design (feeds SK-D05-001 ⏳: EMS Functional Configuration) | 依需求 |
| 5 | Security Configuration: AGC setpoint change authorization rules (per SK-D01-020), audit logging requirements (per SK-D01-024) | 依需求 |
| 6 | Integration Checklist: EMS-SCADA-RTU signal mapping, polling frequency, latency tolerance analysis | Markdown |
| 7 | DERMS Configuration Parameter Table: DER registration list, operational envelope constraints, priority rules for dispatch | Markdown |
| 8 | Dispatch Algorithm Implementation Specification: setpoint calculation logic, unit commitment constraints, economic dispatch constraints | 依需求 |
| 9 | Grid Service Definition Matrix: service type, DER eligibility criteria, compensation mechanism, activation logic | Markdown |
| 10 | Aggregation Group Configuration: resource clustering strategy, communication topology, backup DER substitution rules | 依需求 |
| 11 | DER Communication Security Configuration (per SK-D01-016): authentication/encryption per DER type, timeout/watchdog settings | 依需求 |
| 12 | Performance Monitoring and Audit Strategy: dispatch efficiency metrics, grid service delivery verification, change audit trail | 依需求 |

---

## 4. 適用標準

- IEC 61970 / 61968: Common Information Model (CIM) for power systems — EMS data model
- IEC 61850-8-1: Communication networks and systems in substations — SCADA data binding
- IEC 62443-3-3: System Security Requirements and Security Levels — control system security requirements
- NERC EOP standards: Frequency Response and Reserves — AGC performance requirements (North American context)
- IEEE 1547: Standard for Interconnecting DERs with Electric Power Systems — relevant for DER AGC participation
- IEC 61970 / 61968: Common Information Model (CIM) for power systems — aggregation data structure
- IEC 61850-8-1: Communication networks and systems in substations — DER-DERMS communication protocol
- IEC 62443-3-3: System Security Requirements and Security Levels — DER management system security
- IEEE 1547: Standard for Interconnecting DERs with Electric Power Systems — DER operational characteristics and limits
- NIST SP 800-82 Rev. 3: Guide to Industrial Control Systems Security — aggregation system security framework (supplementa

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | ACE calculation formula is explicitly documented and traceable to the frequency  | ✅ 已驗證 |
| 2 | Participation factor values are assigned to all participating generators with do | ✅ 已驗證 |
| 3 | Ramp rate limits are set within generator mechanical constraints and validated a | ✅ 已驗證 |
| 4 | Tie-line bias control is properly tuned to maintain frequency stability under in | ✅ 已驗證 |
| 5 | All AGC configuration parameters are loaded into the EMS platform and verified a | ✅ 已驗證 |
| 6 | SCADA signal latency for AGC input signals meets the control loop response time  | ✅ 已驗證 |
| 7 | AGC configuration changes are protected by role-based access controls per SK-D01 | ✅ 已驗證 |
| 8 | Configuration has been reviewed and approved by both SYS and OPS | ✅ 已驗證 |
| 9 | All DERs in the fleet are registered in DERMS with correct capacity, location, a | ✅ 已驗證 |
| 10 | Operational envelope constraints (power limits, ramp rates, frequency support pa | ✅ 已驗證 |
| 11 | Dispatch algorithm implementation in DERMS matches the algorithm design (SK-D03- | ✅ 已驗證 |
| 12 | Grid service priority rules are clearly documented and reflect regulatory/market | ✅ 已驗證 |
| 13 | Aggregation group communication topology is tested end-to-end with latency and r | ✅ 已驗證 |
| 14 | DER-DERMS communication security (authentication, encryption, timeout watchdog)  | ✅ 已驗證 |
| 15 | Dispatch setpoint changes are protected by change control and audit logging per  | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D05-003 | | Junior (< 2 yr) | 5–8 person-days | Assumes single-area AGC, 5–15 participating generators, existi |
| SK-D05-003 | | Senior (5+ yr) | 2–4 person-days | Same scope; senior leverages standard AGC parameter libraries a |
| SK-D05-003 | Notes: Multi-area AGC or non-standard generator models may require 1.5–2× effort. Participation fact |
| SK-D05-004 | | Junior (< 2 yr) | 6–10 person-days | Assumes 20–50 DER units, single aggregation group, well-defin |
| SK-D05-004 | | Senior (5+ yr) | 3–5 person-days | Same scope; senior leverages standard DER parameter libraries a |
| SK-D05-004 | Notes: Multi-site aggregation or complex optimization algorithms may require 1.5–2× effort. Grid ser |
| SK-D05-012 | | Junior (< 2 yr) | 3–6 person-days per loop | Assumes simple first-order or second-order loops, str |
| SK-D05-012 | | Senior (5+ yr) | 1–3 person-days per loop | Can rapidly assess loop order, select tuning method, a |

---

## 7. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 輸入完整性 | 所有必要輸入文件已讀取並摘要 |
| 2 | 流程覆蓋 | 5 個工作步驟皆已執行並有產出 |
| 3 | 輸出完整性 | 所有交付物已產出、格式正確、非空白 |
| 4 | 標準合規 | 產出引用的標準版本正確 |
| 5 | 術語一致 | 專案術語、縮寫與 glossary 一致 |
| 6 | 跨步驟一致 | 各步驟產出間無矛盾（如數量、SL等級） |
| 7 | 依賴追溯 | 外部依賴 SK 的輸入已驗證可用 |

---

## 8. 人類審核閘門

完成所有工作步驟後，暫停並向使用者提交審核：

```
控制策略與配置已完成。
📋 執行範圍：5 個工程步驟（SK-D05-003, SK-D05-004, SK-D05-012, SK-D05-013, SK-D05-014）
📊 交付物清單：
  - AGC Configuration Parameter Table: ACE calculation coefficients, participation factor schedule, ramp rate limits per unit, frequency dead-band setting
  - Tie-Line Bias Control Specification: bias coefficient, tie-line metering configuration, remote frequency signal integration
  - Generator Unit Dispatch Logic: unit commitment algorithm, economic dispatch setpoint derivation, reserve margin maintenance
  - AGC Performance Monitoring Dashboard Design (feeds SK-D05-001 ⏳: EMS Functional Configuration)
  - Security Configuration: AGC setpoint change authorization rules (per SK-D01-020), audit logging requirements (per SK-D01-024)
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
| SK 覆蓋 | SK-D05-003, SK-D05-004, SK-D05-012, SK-D05-013, SK-D05-014 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D05-003 | EMS AGC Configuration | EMS AGC 配置 | Configure Automatic Generation Control (AGC) functions withi |
| SK-D05-004 | DERMS DER Management Strategy Setting | DERMS DER 管理策略設定 | Configure Distributed Energy Resource Management System (DER |
| SK-D05-012 | PID Control Tuning | PID 控制調參 | Tune Proportional-Integral-Derivative (PID) controller param |
| SK-D05-013 | Load Management Strategy Design | 負載管理策略設計 | Design load management strategies for demand response, load  |
| SK-D05-014 | Frequency Regulation Control Design | 頻率調節控制設計 | Design frequency regulation control algorithms for grid-conn |

<!-- Phase 5 Wave 2 deepened: SK-D05-003, SK-D05-004, SK-D05-012, SK-D05-013, SK-D05-014 -->