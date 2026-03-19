---
name: cad-documentation
description: >
  Produce fabrication-ready CAD drawings and component selection specifications for OT/ICS
  control panels and equipment cabinets. Covers fabrication drawings (elevations, drilling,
  DIN rail, knockouts) and component selection with cybersecurity alignment.
  MANDATORY TRIGGERS: CAD, 施工圖, fabrication drawing, 元件選型, component selection,
  規範書, specification writing, CAD 出圖, panel drawing, 盤櫃圖面,
  元件規格, component specification, BOM, 加工圖.
  Use this skill for fabrication drawing production and component specification in OT/ICS projects.
---

# CAD 出圖與元件選型 (CAD Documentation & Component Selection)

整合 2 個 SK，產出盤櫃加工圖和元件選型規範。

---

## 0. 初始化

1. **盤面佈局**：Panel layout design 已完成 (SK-D06-001)
2. **配線圖**：Wiring diagram 已完成 (SK-D06-002)
3. **CAD 工具**：AutoCAD/EPLAN/SolidWorks 可用

---

## 1. 工作流程

### Step 1: 施工圖 CAD 出圖 (SK-D06-004)

**產出圖面**：
- 正面/背面 elevation drawings
- Drilling pattern (含公差 ±0.5mm)
- DIN rail layout
- Cable routing paths
- Knockout positions
- Assembly sequence

**CAD 規範**：
```
圖框：A3 (420×297mm)
比例：1:1 (detail 2:1)
圖層：PANEL-OUTLINE / COMPONENT / DRILL / CABLE / DIM / TEXT
字型：微軟正黑體 or Arial
尺寸標注：mm, 公差 ±0.5mm
```

**⚠️ 避坑**：
- 散熱空間不足 → 預留 component 間 ≥10mm gap
- Knockout 位置與 cable gland 不對齊 → 先確認 cable 數量和方向
- 未考慮維護空間 → 門打開後能否操作所有 component

### Step 2: 元件選型與規範書 (SK-D06-006)

**選型評估矩陣**：
```markdown
| 元件 | 候選 A | 候選 B | 候選 C | 權重 |
|------|--------|--------|--------|------|
| 技術規格 | 8/10 | 7/10 | 9/10 | 30% |
| IEC 62443 合規 | 7/10 | 9/10 | 6/10 | 25% |
| 供應鏈穩定性 | 9/10 | 6/10 | 8/10 | 20% |
| 生命週期支援 | 8/10 | 8/10 | 5/10 | 15% |
| 成本 | 7/10 | 9/10 | 7/10 | 10% |
| **加權總分** | **7.85** | **7.65** | **7.15** | — |
```

**規範書內容**：electrical ratings、environmental conditions (IP/NEMA)、cybersecurity considerations (IEC 62443-4-2)、vendor references

**⚠️ 避坑**：
- 只看價格不看 EOL → 選到即將停產的元件
- 未考慮 IEC 62443 → 安全審查時被退回
- 單一供應商 → 供應鏈風險

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | 圖面含所有 views (正面/背面/側面) |
| 2 | Drilling pattern 含公差 |
| 3 | BOM 與圖面元件 1:1 對應 |
| 4 | 元件選型有 ≥3 候選比較 |
| 5 | IEC 62443-4-2 合規評估 |
| 6 | 供應鏈風險評估 |

---

## 3. 人類審核閘門

```
CAD 出圖完成。圖面：{n} 張 | 元件：{c} 項 | BOM 對應：{pct}%
👉 請 DES (設計工程師) 審核。
```

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D06-004 | Fabrication Drawing (CAD) | Elevation, drilling, DIN rail, knockout |
| SK-D06-006 | Component Selection & Spec | 選型矩陣、IEC 62443-4-2、供應鏈 |

<!-- Phase 6: Enhanced 2026-03-19. -->
