---
name: protection-logic-documentation
description: >
  保護邏輯與故障分析。
  Develop protection logic diagrams (Boolean logic expressions, trip matrices, interlocking sequences) for relay-based and IED-based protection schemes.。- **Pitfall:** Analyzing incomplete fault recording data (missing phase, inadequate pre-fault or po
  MANDATORY TRIGGERS: 故障錄波分析, 保護邏輯與故障分析, 保護邏輯圖繪製, Protection Engineering, Protection Logic Diagram Development, digital-fault-recorder, Relay Schemes, Logic Design, Digital Substation, IED Configuration, Fault Recording Analysis.
  Use this skill for protection logic documentation tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 保護邏輯與故障分析

本 Skill 整合 2 個工程技能定義，提供保護邏輯與故障分析的完整工作流程。
適用領域：Protection & Relay（D04）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D03-002, SK-D04-001, SK-D04-002, SK-D04-003, SK-D05-003, SK-D05-010

---

## 1. 輸入

- Protection coordination scheme design (from SK-D04-001, SK-D04-002)
- Relay settings and time delays (overcurrent, distance, differential thresholds)
- Equipment protection strategy (transformer protection scheme, line protection, bus protection)
- Digital relay/IED specifications and logic programming capabilities
- Control system interlocking requirements (breaker lockout, synchro-check, reclosure logic)
- Standard control sequences (ANSI/IEEE device numbering, IEC 61850 logic node definitions)
- Digital fault recorder data files from deployed DFRs (high-resolution waveform samples from fault event)
- Protection relay event logs and disturbance records (timestamp, protection function, trip signal, measured values)
- Protection setting documentation (relay curves, time delays, pickup thresholds) from SK-D04-001 or SK-D04-002
- System architecture and single-line diagram showing equipment arrangement, protection zones, and relay locations
- Operational baseline data (normal voltage, current, frequency profiles) from SK-D08-007 (Performance Baseline)
- Historical fault event database or prior analysis reports for similar fault types (for comparison)

---

## 2. 工作流程

### Step 1: 保護邏輯圖繪製
**SK 來源**：SK-D04-004 — Protection Logic Diagram Development

執行保護邏輯圖繪製：Develop protection logic diagrams (Boolean logic expressions, trip matrices, interlocking sequences) for relay-based and IED-based protection schemes.

**本步驟交付物**：
- Protection logic diagram (graphical representation: AND/OR/NOT logic gates or hardwired diagram)
- Trip matrix table (input conditions → trip signal output mapping)
- Boolean logic expressions (formal notation for each trip function)

### Step 2: 故障錄波分析
**SK 來源**：SK-D04-005 — Fault Recording Analysis

執行故障錄波分析：- **Pitfall:** Analyzing incomplete fault recording data (missing phase, inadequate pre-fault or post-fault window). **Guidance:** Establish data retr

**本步驟交付物**：
- Digital Fault Recorder Data Archive:** Stored DFR data files from fault event with metadata (location, timestamp, triggering event)
- Fault Analysis Report:** Executive summary, waveform analysis results, sequence-of-events timeline, protection operation verification, root cause dete
- Waveform Analysis Plots:** Three-phase voltage and current waveforms with annotations showing fault characteristics, protection function detection poi

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Protection logic diagram (graphical representation: AND/OR/NOT logic gates or hardwired diagram) | 依需求 |
| 2 | Trip matrix table (input conditions → trip signal output mapping) | Markdown |
| 3 | Boolean logic expressions (formal notation for each trip function) | 依需求 |
| 4 | Interlocking sequence documentation (breaker trip hierarchy, blocking conditions) | 依需求 |
| 5 | IED configuration parameter list (for programmable devices) | Markdown |
| 6 | Logic timing diagram (trip signal propagation and time delays) | 依需求 |
| 7 | Digital Fault Recorder Data Archive:** Stored DFR data files from fault event with metadata (location, timestamp, triggering event) | 依需求 |
| 8 | Fault Analysis Report:** Executive summary, waveform analysis results, sequence-of-events timeline, protection operation verification, root cause dete | Markdown |
| 9 | Waveform Analysis Plots:** Three-phase voltage and current waveforms with annotations showing fault characteristics, protection function detection poi | 依需求 |
| 10 | Sequence-of-Events Timeline:** Detailed chronological record with timestamps showing fault inception, relay operation, trip command, and fault clearin | 依需求 |
| 11 | Protection Operation Assessment:** Verification that each protection function operated correctly with supporting calculations and comparisons to setti | 依需求 |
| 12 | Root Cause Analysis Report:** Technical findings on fault origin, contributing factors, and any equipment deficiencies identified | Markdown |

---

## 4. 適用標準

- ANSI/IEEE C37.2 (Electrical and Electronics Graphic Symbols)
- ANSI/IEEE C37.90 (Relays and Relay Systems Associated with Electric Power Apparatus)
- IEC 61850-7-4 (Power Systems Management and Associated Information Exchange — Logical Nodes)
- IEC 61850-8-1 (Specific Communication Service Mapping — ACSI)
- IEC 60947-13 (Low-voltage Switchgear and Controlgear — Microprocessor-based Protection Devices)
- IEC 62443-3-3 (Security Requirements for Industrial Automation and Control Systems)
- Power System Protection Standards:**
- ANSI/IEEE C37.90: Surge Withstand Capability Tests for Protective Relays and Relay Systems
- ANSI/IEEE C37.112: Application of Protective Relays Used for System Protection and Sectionalizing Systems
- IEC 60255 series: Measurement and control systems for power systems; protective relay testing

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Logic diagrams clearly represent all primary and backup protection functions | ✅ 已驗證 |
| 2 | Trip matrices completely map all input conditions (threshold crossings, time del | ✅ 已驗證 |
| 3 | Boolean logic expressions are formally correct and unambiguous (no logical hazar | ✅ 已驗證 |
| 4 | Interlocking sequences prevent unwanted simultaneous trips and ensure hierarchic | ✅ 已驗證 |
| 5 | Timing diagram demonstrates adequate delay coordination (0.2–0.5 sec spacing bet | ✅ 已驗證 |
| 6 | All ANSI/IEEE device numbers assigned correctly and cross-referenced in one-line | ✅ 已驗證 |
| 7 | IEC 61850 Logical Node mapping provided for IED-based implementations | ✅ 已驗證 |
| 8 | Logic validation confirms no orphaned signals, floating inputs, or unreachable l | ✅ 已驗證 |
| 9 | Fault recording data is successfully extracted from DFRs and validated for time  | ✅ 已驗證 |
| 10 | Waveform analysis characterizes fault type (SLG/LL/3LG), magnitude, and location | ✅ 已驗證 |
| 11 | Sequence-of-events timeline is reconstructed with millisecond-level timing showi | ✅ 已驗證 |
| 12 | Protection relay operation is verified against setting design; any deviations ar | ✅ 已驗證 |
| 13 | Root cause of fault event is determined and documented with supporting evidence  | ✅ 已驗證 |
| 14 | If protection deficiencies are identified, specific recommendations for SK-D04-0 | ✅ 已驗證 |
| 15 | Formal analysis report is produced with waveform plots, timeline graphics, and c | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D04-004 | | Protection requirement review & relay settings reconciliation | 8 hours | Validate coordination in |
| SK-D04-004 | | Logic diagram development (primary & backup logic) | 16 hours | Graphical design, gate-level repre |
| SK-D04-004 | | Trip matrix creation & Boolean expression formulation | 10 hours | Formal logic notation, exhausti |
| SK-D04-004 | | Interlocking sequence design & timing analysis | 12 hours | Breaker sequencing, blocking condition |
| SK-D04-004 | | IEC 61850 mapping (for IED-based schemes) | 8 hours | Logical Node selection, SCL input preparatio |
| SK-D04-004 | | Simulation/validation testing & hazard checking | 10 hours | Logic simulation, race condition anal |
| SK-D04-004 | | Documentation & sign-off | 6 hours | Final diagrams, validation report, archival | |
| SK-D04-004 | | **Total Estimated Effort** | **70 hours** | For medium-complexity multi-zone protection scheme (3– |

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
保護邏輯與故障分析已完成。
📋 執行範圍：2 個工程步驟（SK-D04-004, SK-D04-005）
📊 交付物清單：
  - Protection logic diagram (graphical representation: AND/OR/NOT logic gates or hardwired diagram)
  - Trip matrix table (input conditions → trip signal output mapping)
  - Boolean logic expressions (formal notation for each trip function)
  - Interlocking sequence documentation (breaker trip hierarchy, blocking conditions)
  - IED configuration parameter list (for programmable devices)
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
| SK 覆蓋 | SK-D04-004, SK-D04-005 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D04-004 | Protection Logic Diagram Development | 保護邏輯圖繪製 | Develop protection logic diagrams (Boolean logic expressions |
| SK-D04-005 | Fault Recording Analysis | 故障錄波分析 | - **Pitfall:** Analyzing incomplete fault recording data (mi |

<!-- Phase 5 Wave 2 deepened: SK-D04-004, SK-D04-005 -->