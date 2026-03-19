---
name: electrical-mechanical-design
description: >
  Design electrical and mechanical aspects including panel layout with thermal calculation,
  wiring diagrams, terminal block schedules, and wire sizing calculations.
  MANDATORY TRIGGERS: 盤面佈局, panel layout, 配線圖, wiring diagram, 端子排, terminal block,
  線徑, wire sizing, 散熱, thermal, panel design, IEC 62208, IEC 61346,
  IEC 60617, IEC 60228, IEC 60364, 電氣設計, electrical design.
  Use this skill for panel layout, wiring, terminal block, and wire sizing design.
---

# 電氣機構設計 (Electrical & Mechanical Design)

整合 4 個 SK，涵蓋盤面佈局、配線圖、端子排與線徑計算。

---

## 0. 初始化

1. 設備清單已確認 (含尺寸/發熱量)
2. 單線圖 (SLD) 已完成
3. 安裝場所環境條件已確認 (溫度/IP 等級)

---

## 1. 工作流程

### Step 1: 盤面佈局與散熱計算 (SK-D06-001)

**佈局原則 (IEC 62208)**：

| 區域 | 位置 | 設備 |
|------|------|------|
| 上層 | 盤頂 | 指示燈、端子排 (低發熱) |
| 中層 | 眼高 | HMI、繼電器、量表 |
| 下層 | 盤底 | 斷路器、變壓器 (高發熱) |
| 門板 | 前門 | 操作按鈕、指示器 |

**散熱計算**：

```
P_total = Σ 設備發熱量 (W)
T_rise = P_total / (k × A)
- k: 散熱係數 (5.5 W/m²·K 自然對流)
- A: 盤體有效散熱面積 (m²)

若 T_rise + T_ambient > 55°C:
  → 加裝風扇/熱交換器/空調
  風扇: 適用 ΔT ≤15°C
  空調: 適用 ΔT >15°C 或高粉塵
```

**步驟**：設備尺寸排列 → 散熱計算 → 走線空間預留 (≥20%) → IP 等級確認 → 接地銅排規劃 → 出圖 (front/rear view)

**⚠️ 避坑**：忘記計算 wire duct 空間；高發熱設備集中會產生熱點

### Step 2: 配線圖 (SK-D06-002)

**IEC 61346/60617 規範**：

| 圖面類型 | 內容 | 用途 |
|----------|------|------|
| 迴路圖 | 單一迴路完整接線 | 調試依據 |
| 內部配線圖 | 盤內接線 | 盤廠施工 |
| 外部配線圖 | 盤間接線 | 現場施工 |
| 接地圖 | 接地系統 | 安全 |

**步驟**：從 SLD 展開迴路 → 標註設備代號 (IEC 61346) → 標註端子編號 → 標註線號/線徑/顏色 → 交叉參考 (cross-reference) → 審查一致性

**⚠️ 避坑**：線號不唯一導致配線錯誤；交叉參考必須雙向正確

### Step 3: 端子排規劃 (SK-D06-003)

**端子排配置表**：

```
| TB No. | Terminal | From        | To          | Wire  | Color |
|--------|----------|-------------|-------------|-------|-------|
| TB1    | 1        | CB1-a1      | Relay-1A    | 2.5mm²| Red   |
| TB1    | 2        | CB1-a2      | Relay-1B    | 2.5mm²| Red   |
| TB1    | 3        | CT1-S1      | Relay-IA    | 2.5mm²| Black |
| TB1    | 4        | CT1-S2      | Relay-IB    | 2.5mm²| Black |
| TB1    | 5        | SPARE       | —           | —     | —     |
```

**步驟**：依迴路分群 → 編排端子號 → 預留 spare (≥10%) → 標註 From/To → 產出端子排圖 → 與配線圖交叉驗證

**⚠️ 避坑**：電力與信號端子需分離；spare 不足日後擴充困難

### Step 4: 線徑計算 (SK-D06-005)

**IEC 60228/60364 計算**：

```
1. 載流量: I_design ≤ I_z × k1 × k2 × k3
   - k1: 環境溫度修正 (40°C → 0.87)
   - k2: 並排修正 (3 排 → 0.70)
   - k3: 管路修正

2. 壓降: ΔV = I × (R·cosφ + X·sinφ) × L × 2
   - 允許: 主幹 ≤3%, 分路 ≤5%

3. 短路耐受: A ≥ I_sc × √t / k
   - k: 銅 = 115, 鋁 = 76
```

**步驟**：確定負載電流 → 選初始線徑 (載流量) → 壓降驗算 → 短路耐受驗算 → 取三者最大 → 選定標準線徑

**⚠️ 避坑**：壓降計算要用實際路徑長度 (非直線距離)；並排修正常被遺漏

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | 盤面佈局含散熱計算且 T < 55°C |
| 2 | 配線圖符合 IEC 61346/60617 |
| 3 | 所有線號唯一且交叉參考正確 |
| 4 | 端子排含 ≥10% spare |
| 5 | 線徑通過載流量/壓降/短路三重驗算 |
| 6 | 圖面已出 front/rear view |

---

## 3. 人類審核閘門

```
電氣機構設計完成。盤數：{n} | 迴路圖：{n} | 端子數：{total}
👉 請 EE + 盤廠審核。
```

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D06-001 | Panel Layout | 佈局原則、散熱計算、IEC 62208 |
| SK-D06-002 | Wiring Diagram | IEC 61346/60617、迴路圖 |
| SK-D06-003 | Terminal Block | 端子排配置、spare 規劃 |
| SK-D06-005 | Wire Sizing | 載流量/壓降/短路、IEC 60228/60364 |

<!-- Phase 6: Enhanced 2026-03-19. -->
