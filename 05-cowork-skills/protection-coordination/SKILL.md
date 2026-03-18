---
name: protection-coordination
description: >
  保護協調與整定。
  Design overcurrent protection coordination schemes for power distribution networks, determining relay settings, time-current curves, and coordination 。Calculate distance relay settings (Zone 1/2/3 reach, time delays) for transmission and sub-transmis
  MANDATORY TRIGGERS: 過電流保護協調, 繼電器選型與參數設定, 距離保護整定計算, 保護繼電器測試, 保護協調與整定, Distance Relays, primary-injection, relay-coordination, Impedance Protection, testing, Protection Engineering, Power Distribution, overcurrent.
  Use this skill for protection coordination tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 保護協調與整定

本 Skill 整合 4 個工程技能定義，提供保護協調與整定的完整工作流程。
適用領域：Protection & Relay（D04）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-020, SK-D02-001, SK-D03-001, SK-D03-010, SK-D04-004, SK-D05-001

---

## 1. 輸入

- Network topology and one-line diagram (power distribution system model)
- Fault study results (three-phase and single-phase fault currents at all network nodes)
- Equipment ratings (transformer impedances, line impedances, generation capacities)
- Existing relay settings (where applicable for legacy systems)
- Operational constraints (load flow profiles, seasonal variations)
- Regulatory and utility standards (e.g., IEEE C37.112, IEC 60255)
- Power system impedance model (source impedances, line impedances, transformer impedances)
- Transmission line positive/zero-sequence impedances and distribution
- Fault study results (maximum and minimum fault currents, SIR values)
- Distance relay manufacturer specifications and user manuals
- Network expansion plans (future generator/load connection points)
- Coordination requirements with adjacent substations (voltage levels, relay types)

---

## 2. 工作流程

### Step 1: 過電流保護協調
**SK 來源**：SK-D04-001 — Overcurrent Protection Coordination

執行過電流保護協調：Design overcurrent protection coordination schemes for power distribution networks, determining relay settings, time-current curves, and coordination 

**本步驟交付物**：
- Overcurrent protection coordination scheme design document
- Relay settings schedule (pickup currents, time-multiplier settings, instantaneous settings)
- Time-current characteristic curves (TCC plots) showing coordination margins

### Step 2: 距離保護整定計算
**SK 來源**：SK-D04-002 — Distance Protection Setting Calculation

執行距離保護整定計算：Calculate distance relay settings (Zone 1/2/3 reach, time delays) for transmission and sub-transmission line protection using impedance-based calculat

**本步驟交付物**：
- Distance relay setting calculation report
- Zone reach settings (Zone 1: typically 80% of line length; Zone 2: 120% + margin; Zone 3: backup reach)
- Time delay settings for each zone (instantaneous for Zone 1, delayed for Zone 2/3)

### Step 3: 繼電器選型與參數設定
**SK 來源**：SK-D04-003 — Relay Selection and Parameter Setting

執行繼電器選型與參數設定：Select appropriate protection relays (overcurrent, distance, differential, impedance-based, etc.) based on system requirements, operational constraint

**本步驟交付物**：
- Relay Selection Summary: relay type, manufacturer, model, nameplate ratings, installed location
- Relay Parameter Setting Sheet: pickup values (A or V), time delays, curve characteristics, communication settings per relay
- IEC 61850 GOOSE Subscription List: data attributes subscribed, logical nodes involved, reporting frequency

### Step 4: 保護繼電器測試
**SK 來源**：SK-D04-006 — Protection Relay Testing

執行保護繼電器測試：Execute comprehensive protection relay testing on installed relays in a power generation or distribution system, validating their correct configuratio

**本步驟交付物**：
- Relay Test Report (primary and secondary injection results, trip time measurements)
- GOOSE Communication Test Report (IEC 61850 signal transmission and timing validation)
- Relay Coordination Verification Report (selectivity confirmation with adjacent zones)

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Overcurrent protection coordination scheme design document | 依需求 |
| 2 | Relay settings schedule (pickup currents, time-multiplier settings, instantaneous settings) | 依需求 |
| 3 | Time-current characteristic curves (TCC plots) showing coordination margins | 依需求 |
| 4 | Coordination interval analysis (minimum and maximum clearing times) | 依需求 |
| 5 | Selective tripping matrices defining primary and backup protection zones | 依需求 |
| 6 | Sensitivity analysis (impact of load variation on coordination) | 依需求 |
| 7 | Distance relay setting calculation report | Markdown |
| 8 | Zone reach settings (Zone 1: typically 80% of line length; Zone 2: 120% + margin; Zone 3: backup reach) | 依需求 |
| 9 | Time delay settings for each zone (instantaneous for Zone 1, delayed for Zone 2/3) | 依需求 |
| 10 | R-X plane plots showing relay characteristics and coordination margins | 依需求 |
| 11 | Sensitivity analysis (SIR margin, load encroachment risk assessment) | 依需求 |
| 12 | Setting verification checklist and relay parameter export files | Markdown |

---

## 4. 適用標準

- IEEE C37.112 (Inverse-Time Characteristics of AC Time Overcurrent Relays)
- IEEE C37.96 (Design, Testing, and Applications of Protection Systems)
- IEC 60255-3 (Electronic Measuring Equipment — Performance Characteristics)
- IEC 60909 (Short Circuit Currents in Three-Phase AC Systems)
- ANSI/IEEE C37.95 (Guide for Protection of Power Transformers)
- IEEE C37.2 (Electrical and Electronics Graphic Symbols and Electrical and Electronics Diagrams)
- IEC 60255-8 (Electronic Measuring Equipment — Security Functions)
- IEC 61869-2 (Instrument Transformers: Additional Requirements for Current Transformers)
- IEC 61850 (Power Systems Management and Associated Information Exchange)
- ANSI/IEEE C37.240 (Standard for Relay Communications Protocol — COMTRADE)

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | All coordination intervals (between primary and backup devices) meet minimum sta | ✅ 已驗證 |
| 2 | TCC plots demonstrate non-intersecting curves for all coordination pairs | ✅ 已驗證 |
| 3 | Sensitivity analysis confirms coordination margin maintained across ±20% fault c | ✅ 已驗證 |
| 4 | Relay settings comply with manufacturer specifications and ANSI/IEEE standards | ✅ 已驗證 |
| 5 | Selective tripping sequence verified; no unwanted multi-zone trips for single fa | ✅ 已驗證 |
| 6 | Load flow analysis confirms coordination settings do not trigger nuisance trips  | ✅ 已驗證 |
| 7 | Documentation includes equipment nameplate references and validation dates | ✅ 已驗證 |
| 8 | Zone 1 reach set to 80–90% of protected line impedance (eliminating infeed bias) | ✅ 已驗證 |
| 9 | Zone 2 reach set to 120–150% of protected line impedance with adequate margin to | ✅ 已驗證 |
| 10 | Zone 3 reach provides backup protection to adjacent line (typically 50–75% of ad | ✅ 已驗證 |
| 11 | Time delays comply with coordination intervals (Zone 2: 0.3–0.5 sec delay; Zone  | ✅ 已驗證 |
| 12 | R-X characteristic plot demonstrates no load encroachment under maximum load flo | ✅ 已驗證 |
| 13 | Sensitivity ratio (SIR) margin maintained above minimum threshold (typically >1. | ✅ 已驗證 |
| 14 | Relay setting parameters exported and cross-checked against manufacturer specifi | ✅ 已驗證 |
| 15 | Contingency analysis confirms reach adequacy if adjacent protection zone is unav | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D04-001 | | Data collection & network analysis | 10 hours | Gather fault currents, impedances, existing settin |
| SK-D04-001 | | Relay selection & setting calculation | 20 hours | TCC plots, pickup/time settings, zone reach | |
| SK-D04-001 | | ETAP coordination study setup | 15 hours | Model validation, coordination module configuration | |
| SK-D04-001 | | Coordination validation & optimization | 20 hours | Iterative TCC analysis, sensitivity studies | |
| SK-D04-001 | | Documentation & sign-off | 10 hours | Final coordination scheme report, settings archive | |
| SK-D04-001 | | **Total Estimated Effort** | **75 hours** | For medium-complexity distribution network (50–100 sub |
| SK-D04-002 | | Impedance model extraction & validation | 8 hours | Extract from ETAP/PowerFactory, verify against |
| SK-D04-002 | | Zone reach calculation (Zones 1–3) | 12 hours | R-X plane analysis, SIR margin verification | |

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
保護協調與整定已完成。
📋 執行範圍：4 個工程步驟（SK-D04-001, SK-D04-002, SK-D04-003, SK-D04-006）
📊 交付物清單：
  - Overcurrent protection coordination scheme design document
  - Relay settings schedule (pickup currents, time-multiplier settings, instantaneous settings)
  - Time-current characteristic curves (TCC plots) showing coordination margins
  - Coordination interval analysis (minimum and maximum clearing times)
  - Selective tripping matrices defining primary and backup protection zones
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
| Domain | D04 (Protection & Relay) |
| SK 覆蓋 | SK-D04-001, SK-D04-002, SK-D04-003, SK-D04-006 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D04-001 | Overcurrent Protection Coordination | 過電流保護協調 | Design overcurrent protection coordination schemes for power |
| SK-D04-002 | Distance Protection Setting Calculation | 距離保護整定計算 | Calculate distance relay settings (Zone 1/2/3 reach, time de |
| SK-D04-003 | Relay Selection and Parameter Setting | 繼電器選型與參數設定 | Select appropriate protection relays (overcurrent, distance, |
| SK-D04-006 | Protection Relay Testing | 保護繼電器測試 | Execute comprehensive protection relay testing on installed  |

<!-- Phase 5 Wave 2 deepened: SK-D04-001, SK-D04-002, SK-D04-003, SK-D04-006 -->