---
name: cad-documentation
description: >
  CAD 與元件規範。
  Produce fabrication-ready CAD drawings for control panel and equipment cabinet manufacturing, enabling the fabrication shop and assembly teams to cons。- Maintain and refine component selection criteria based on field failure data and supply chain exp
  MANDATORY TRIGGERS: CAD 與元件規範, 元件選型與規範書撰寫, 施工圖 CAD 出圖, selection, Fabrication Drawing Production (CAD), fabrication-drawing, component, mechanical-design, specification, cad documentation, Component Selection and Specification Writing.
  Use this skill for cad documentation tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# CAD 與元件規範

本 Skill 整合 2 個工程技能定義，提供CAD 與元件規範的完整工作流程。
適用領域：Panel & Electrical Engineering（D06）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D02-003, SK-D04-001, SK-D06-002, SK-D06-003, SK-D06-005

---

## 1. 輸入

- Functional electrical schematic diagrams (from SK-D04-001 ⏳: Functional Electrical Schematic Design)
- Wiring diagram and terminal block schedule (from SK-D06-002: Wiring Diagram Development; SK-D06-003: Terminal Block Schedule Development)
- Equipment and component datasheets (relay modules, PLC, drives, power supplies, terminal blocks, DIN rails, cable ducts)
- Panel specification document (internal/external dimensions, material, mounting location, NEMA/IP rating requirements)
- Wire sizing results and cable schedule (from SK-D06-005: Wire Sizing Calculation; SK-D02-003 ⏳: Interface Control Document)
- Control panel layout standards and organizational design guidelines
- Design requirements specification (DRS) complete and approved
- System architecture and functional block diagram defined
- OT/ICS operating environment profile established (temperature, humidity, pollution, vibration)
- IEC 62443 security level (SL) target assigned for the system or functional group
- Component selection criteria and approval authority matrix defined
- Vendor qualification and approved parts list (APL) available

---

## 2. 工作流程

### Step 1: 施工圖 CAD 出圖
**SK 來源**：SK-D06-004 — Fabrication Drawing Production (CAD)

執行施工圖 CAD 出圖：Produce fabrication-ready CAD drawings for control panel and equipment cabinet manufacturing, enabling the fabrication shop and assembly teams to cons

**本步驟交付物**：
- Fabrication drawing set (PDF and native CAD format, e.g., .dwg or .sldprt):
- Front panel (face) elevation with component cutouts, indicator light positions, pushbutton positions, selector switch locations, and nameplate locatio
- Rear panel (back) elevation with terminal block arrangement, cable duct routing, cable entry knockouts, grounding point locations, and mounting rails

### Step 2: 元件選型與規範書撰寫
**SK 來源**：SK-D06-006 — Component Selection and Specification Writing

執行元件選型與規範書撰寫：- Maintain and refine component selection criteria based on field failure data and supply chain experience

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Fabrication drawing set (PDF and native CAD format, e.g., .dwg or .sldprt): | 依需求 |
| 2 | Front panel (face) elevation with component cutouts, indicator light positions, pushbutton positions, selector switch locations, and nameplate locatio | 依需求 |
| 3 | Rear panel (back) elevation with terminal block arrangement, cable duct routing, cable entry knockouts, grounding point locations, and mounting rails | 依需求 |
| 4 | Left/right side panels (if applicable) showing cable routing and ventilation requirements | 依需求 |
| 5 | Top view showing DIN rail layout, component mounting positions, and cable tray/duct routing | 依需求 |
| 6 | Detail views of critical features: drilling patterns with hole positions and dimensions, DIN rail mounting details, cable entry grommet locations | 依需求 |

---

## 4. 適用標準

- IEC 60617: Graphical symbols for use in electrical and electronics engineering — symbol conventions for panel layout dia
- IEC 61439-1 / IEC 61439-2: Low-voltage switchgear and control gear assemblies — panel design, safety, and assembly stand
- IEC 61131-2: Programmable controllers, Part 2: Equipment requirements and tests — cabinet and panel mechanical and envir
- ISO 1219 (Fluid Power): Graphic symbols and circuit diagrams (if hydraulic/pneumatic systems are integrated)
- NEMA/IEC enclosure ratings (e.g., NEMA 4/IEC IP66 for outdoor cabinets) — environmental sealing and material specificati
- Customer or organizational CAD standards and drawing conventions
- IEC 62443-1-1: Terminology and concepts
- IEC 62443-3-3: System design and engineering
- IEC 60721-3: Environmental conditions classification (degree of contamination, temperature, humidity)
- Component datasheets (relay, switch, power supply, communication module, terminal block manufacturers)

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Fabrication drawings completely define the physical structure and component layo | ✅ 已驗證 |
| 2 | All component mounting positions (relays, PLC, drives, terminal blocks, DIN rail | ✅ 已驗證 |
| 3 | All drilling patterns, knockout locations, and cable entry points are dimensione | ✅ 已驗證 |
| 4 | DIN rail layout clearly shows the planned layout of relay modules, drives, and I | ✅ 已驗證 |
| 5 | Cable duct and conduit routing is shown in plan (top view) and elevations (front | ✅ 已驗證 |
| 6 | Nameplate and labeling specification includes font size, color, position, and me | ✅ 已驗證 |
| 7 | Material schedule lists all structural materials, paints, coatings, gaskets, and | ✅ 已驗證 |
| 8 | Assembly instructions or notes are clear enough for shop personnel to assemble t | ✅ 已驗證 |
| 9 | All components selected meet specified electrical ratings, environmental require | ✅ 已驗證 |
| 10 | Specification sheets document: part number, functional description, electrical r | ✅ 已驗證 |
| 11 | Component selections validated against interoperability matrix with existing inf | ✅ 已驗證 |
| 12 | Supply chain risk assessment completed: no single-source critical components wit | ✅ 已驗證 |
| 13 | Design engineer and procurement approval obtained on component specification she | ✅ 已驗證 |
| 14 | Traceability established: each component traces to design requirement and forwar | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D06-004 | | Junior (< 2 yr) | 6–10 person-days | Single panel, standard enclosure, <50 I/O; includes drafting, |
| SK-D06-004 | | Senior (5+ yr) | 3–5 person-days | Same scope; senior can leverage panel design templates, paramet |
| SK-D06-006 | Specification sheet cycle time: average time from requirement extraction to sign-off (target: <5 bus |

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
CAD 與元件規範已完成。
📋 執行範圍：2 個工程步驟（SK-D06-004, SK-D06-006）
📊 交付物清單：
  - Fabrication drawing set (PDF and native CAD format, e.g., .dwg or .sldprt):
  - Front panel (face) elevation with component cutouts, indicator light positions, pushbutton positions, selector switch locations, and nameplate locatio
  - Rear panel (back) elevation with terminal block arrangement, cable duct routing, cable entry knockouts, grounding point locations, and mounting rails
  - Left/right side panels (if applicable) showing cable routing and ventilation requirements
  - Top view showing DIN rail layout, component mounting positions, and cable tray/duct routing
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
| SK 覆蓋 | SK-D06-004, SK-D06-006 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D06-004 | Fabrication Drawing Production (CAD) | 施工圖 CAD 出圖 | Produce fabrication-ready CAD drawings for control panel and |
| SK-D06-006 | Component Selection and Specification Writing | 元件選型與規範書撰寫 | - Maintain and refine component selection criteria based on  |

<!-- Phase 5 Wave 2 deepened: SK-D06-004, SK-D06-006 -->