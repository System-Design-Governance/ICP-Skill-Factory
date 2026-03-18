---
name: electrical-mechanical-design
description: >
  電氣機械設計。
  Design control panel physical layouts including component placement, cable routing, thermal management, and ergonomic considerations for electrical co。Develop detailed wiring diagrams showing all electrical connections between components within contr
  MANDATORY TRIGGERS: 盤面佈局設計與散熱計算, 線徑選用計算, 配線圖繪製, 端子排表建立, 電氣機械設計, electrical-design, NEMA-ratings, cable-selection, electrical mechanical design, Panel Layout Design and Thermal Calculation, layout-design, control-panel, wiring-diagram.
  Use this skill for electrical mechanical design tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 電氣機械設計

本 Skill 整合 4 個工程技能定義，提供電氣機械設計的完整工作流程。
適用領域：Panel & Electrical Engineering（D06）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D02-003, SK-D03-001, SK-D04-001, SK-D05-001, SK-D06-004, SK-D06-006

---

## 1. 輸入

- Equipment and component list from SK-D06-006: Component Selection and Procurement (including power ratings, thermal dissipation, dimensions, mounting 
- System Architecture Design and functional requirements (from SK-D05-001 ⏳ and SK-D05-002 ⏳)
- Electrical single-line diagram and control wiring schematic (from SK-D06-002 ⏳: Single-Line Diagram and Control Wiring Design)
- Panel environmental specifications: installation location (indoor/outdoor), ambient temperature range, humidity, IP/NEMA rating requirement
- Customer panel standard or guidelines (if applicable)
- Cabling specifications and voltage drop calculations (from SK-D06-002 ⏳)
- Functional electrical schematic diagrams (from SK-D04-001 ⏳: Functional Electrical Schematic Design; or delivered as part of detailed design package)
- Equipment data sheets and datasheets (relay modules, drives, power supplies, I/O modules)
- Terminal block schedule (from SK-D06-003: Terminal Block Schedule Development; or developed iteratively)
- Wire sizing calculation results (from SK-D06-005: Wire Sizing Calculation)
- Control panel layout and fabrication drawings (from SK-D06-004: Fabrication Drawing Production)
- Cable schedule with cable IDs, types, and routing paths (from SK-D06-002 or SK-D02-003 ⏳: Interface Control Document)

---

## 2. 工作流程

### Step 1: 盤面佈局設計與散熱計算
**SK 來源**：SK-D06-001 — Panel Layout Design and Thermal Calculation

執行盤面佈局設計與散熱計算：Design control panel physical layouts including component placement, cable routing, thermal management, and ergonomic considerations for electrical co

**本步驟交付物**：
- Panel Layout Drawing (CAD format, typically AutoCAD or equivalent): top, front, side, and interior views showing component locations, mounting heights
- Component Placement Table: detailed location, orientation, and mounting method for each component with reference to electrical drawings
- Thermal Calculation and Analysis Report: steady-state heat dissipation calculation per IEC 62208, cooling method selection (natural/forced/active), ve

### Step 2: 配線圖繪製
**SK 來源**：SK-D06-002 — Wiring Diagram Development

執行配線圖繪製：Develop detailed wiring diagrams showing all electrical connections between components within control panels and between panels and field devices. Wir

**本步驟交付物**：
- Complete wiring diagram set in PDF and CAD formats (.dwg for AutoCAD Electrical or .eplan for EPLAN)
- Wire number list: wire ID, source terminal, destination terminal, wire gauge, color code, cable reference
- Cable schedule reference matrix linking wiring diagram wire numbers to physical cable labels

### Step 3: 端子排表建立
**SK 來源**：SK-D06-003 — Terminal Block Schedule Development

執行端子排表建立：Develop comprehensive terminal block schedules documenting all terminal blocks installed in control panels and instrument cabinets. A terminal block s

**本步驟交付物**：
- Terminal Block Schedule (structured table format, PDF and Excel):
- Terminal block ID (panel ID + block number, e.g., "PLC-TB-01")
- Terminal ID within block (e.g., "1", "2", ..., "12")

### Step 4: 線徑選用計算
**SK 來源**：SK-D06-005 — Wire Sizing Calculation

執行線徑選用計算：Calculate and select appropriate wire/cable sizes for both control circuits (low-current signal wiring) and power circuits (high-current power distrib

**本步驟交付物**：
- Wire Sizing Calculation Report (structured table or narrative document):
- Circuit ID (from schematic, e.g., "Motor_M01_Power", "Sensor_S001_Signal")
- Circuit description and purpose (e.g., "480V 3-phase power to Motor 1", "4-20mA analog input from pressure transmitter")

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Panel Layout Drawing (CAD format, typically AutoCAD or equivalent): top, front, side, and interior views showing component locations, mounting heights | 依需求 |
| 2 | Component Placement Table: detailed location, orientation, and mounting method for each component with reference to electrical drawings | 依需求 |
| 3 | Thermal Calculation and Analysis Report: steady-state heat dissipation calculation per IEC 62208, cooling method selection (natural/forced/active), ve | Markdown |
| 4 | Cable Routing Diagram: conduit/tray layout showing separation of power, control, and signal cables; grounding path routing; electromagnetic compatibil | 依需求 |
| 5 | Panel Assembly Procedure: step-by-step instructions for component mounting, wiring, testing, and acceptance | 依需求 |
| 6 | Thermal Management Specification: cooling system selection (fan size/capacity, filter maintenance intervals, thermostat setpoints if active climate co | 依需求 |
| 7 | Complete wiring diagram set in PDF and CAD formats (.dwg for AutoCAD Electrical or .eplan for EPLAN) | 依需求 |
| 8 | Wire number list: wire ID, source terminal, destination terminal, wire gauge, color code, cable reference | Markdown |
| 9 | Cable schedule reference matrix linking wiring diagram wire numbers to physical cable labels | Markdown |
| 10 | Connection verification report: checklist of all connections verified against schematic and component datasheets | Markdown |
| 11 | Revision-controlled diagram file with tracking of engineering changes per SK-D09-005 | 依需求 |
| 12 | Terminal Block Schedule (structured table format, PDF and Excel): | 依需求 |

---

## 4. 適用標準

- IEC 62208:2016 — Safety of Machinery — Graphical Symbols for Operator Controls and Signalling Devices — thermal and encl
- IEC 61551:2021 — Safety of Machinery — Thermal Equipment — thermal dissipation and ventilation requirements
- NEMA 250 (IEC 60529 equivalent) — Enclosure Types (4, 4X, 4D, 12, 12K, 13, etc.) and environmental protection ratings
- IEC 60204-1 — Safety of Machinery — Electrical Equipment of Machines (Section 6: Thermal considerations and cooling)
- IEC 61000-6-2 / IEC 61000-6-4 — Electromagnetic Compatibility — requirements for EMC in industrial environments (informs
- VDI 3341 (optional, German standard) — Design and implementation of electrical control panels for machinery
- ISO 11064 — Ergonomics of Human-System Interaction — control room/panel ergonomics
- IEC 60617: Graphical symbols for use in electrical and electronics engineering — symbol definitions and wiring diagram c
- IEC 61346: Structured Principles and Reference Designations for Electric Devices and Systems — wire and component labeli
- IEC 61810-1: Electromechanical elementary relays — device reference designations

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Layout drawing is complete and clear: all components are located and dimensioned | ✅ 已驗證 |
| 2 | Component placement rationale is documented: grouping of related components (e.g | ✅ 已驗證 |
| 3 | Thermal calculation is performed per IEC 62208 methodology: heat dissipation is  | ✅ 已驗證 |
| 4 | Worst-case thermal scenario is analyzed: maximum ambient temperature + maximum c | ✅ 已驗證 |
| 5 | Cable separation and routing follows electromagnetic compatibility practices: po | ✅ 已驗證 |
| 6 | NEMA/IP rating is verified: enclosure sealing, ventilation openings, and compone | ✅ 已驗證 |
| 7 | Panel assembly procedure is documented with clear step-by-step instructions, tor | ✅ 已驗證 |
| 8 | BOM is complete and accurate, linked to approved component selections from SK-D0 | ✅ 已驗證 |
| 9 | Every wire in the functional schematic is explicitly numbered in the wiring diag | ✅ 已驗證 |
| 10 | Every wire number is cross-referenced to source terminal, destination terminal,  | ✅ 已驗證 |
| 11 | Wire gauges and colors match the results of SK-D06-005 (Wire Sizing Calculation) | ✅ 已驗證 |
| 12 | All terminal block references point to valid entries in SK-D06-003 (Terminal Blo | ✅ 已驗證 |
| 13 | Diagram is drawn to IEC 60617 symbol standards and IEC 61346 reference designati | ✅ 已驗證 |
| 14 | Cable schedules are complete: every inter-panel cable and field device cable is  | ✅ 已驗證 |
| 15 | Connection verification report documents 100% review of all connections against  | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D06-001 | | Junior (< 2 yr) | 8–12 person-days | Assumes single enclosure, ~15–25 major components, natural ve |
| SK-D06-001 | | Senior (5+ yr) | 4–7 person-days | Same scope; senior can rapidly develop layouts from templates a |
| SK-D06-001 | Notes: Large multi-enclosure systems or active cooling (HVAC) may require 1.5–2× effort due to compl |
| SK-D06-002 | | Junior (< 2 yr) | 5–8 person-days | Single panel or modular subsystem; includes symbol drawing, wi |
| SK-D06-002 | | Senior (5+ yr) | 2–3 person-days | Same scope; senior can leverage templates, macro automation, an |
| SK-D06-003 | | Junior (< 2 yr) | 3–5 person-days | Single panel or modular subsystem (~50–100 I/O terminals); inc |
| SK-D06-003 | | Senior (5+ yr) | 1–2 person-days | Same scope; senior can leverage automated schedule generation t |
| SK-D06-005 | | Junior (< 2 yr) | 2–4 person-days | ~20–50 circuits; includes load analysis review, table lookups, |

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
電氣機械設計已完成。
📋 執行範圍：4 個工程步驟（SK-D06-001, SK-D06-002, SK-D06-003, SK-D06-005）
📊 交付物清單：
  - Panel Layout Drawing (CAD format, typically AutoCAD or equivalent): top, front, side, and interior views showing component locations, mounting heights
  - Component Placement Table: detailed location, orientation, and mounting method for each component with reference to electrical drawings
  - Thermal Calculation and Analysis Report: steady-state heat dissipation calculation per IEC 62208, cooling method selection (natural/forced/active), ve
  - Cable Routing Diagram: conduit/tray layout showing separation of power, control, and signal cables; grounding path routing; electromagnetic compatibil
  - Panel Assembly Procedure: step-by-step instructions for component mounting, wiring, testing, and acceptance
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
| Domain | D06 (Panel & Electrical Engineering) |
| SK 覆蓋 | SK-D06-001, SK-D06-002, SK-D06-003, SK-D06-005 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D06-001 | Panel Layout Design and Thermal Calculation | 盤面佈局設計與散熱計算 | Design control panel physical layouts including component pl |
| SK-D06-002 | Wiring Diagram Development | 配線圖繪製 | Develop detailed wiring diagrams showing all electrical conn |
| SK-D06-003 | Terminal Block Schedule Development | 端子排表建立 | Develop comprehensive terminal block schedules documenting a |
| SK-D06-005 | Wire Sizing Calculation | 線徑選用計算 | Calculate and select appropriate wire/cable sizes for both c |

<!-- Phase 5 Wave 2 deepened: SK-D06-001, SK-D06-002, SK-D06-003, SK-D06-005 -->