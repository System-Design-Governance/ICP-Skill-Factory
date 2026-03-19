---
name: advanced-power-analysis
description: >
  Perform advanced power system analysis including harmonic analysis with filter design,
  transient stability simulation, and power system modeling in ETAP/PSS/E.
  MANDATORY TRIGGERS: 諧波分析, harmonic, harmonic analysis, 暫態穩定, transient stability,
  電力建模, power system modeling, 濾波器, filter design, IEEE 519, THD,
  ETAP modeling, PSS/E modeling, 暫態模擬, transient simulation.
  Use this skill for harmonic studies, transient stability, and power system modeling.
---

# 進階電力分析 (Advanced Power Analysis)

整合 3 個 SK，涵蓋諧波分析、暫態穩定與電力系統建模。

---

## 0. 初始化

1. 電力系統基礎分析已完成 (潮流/短路)
2. 非線性負載清單已取得 (VFD, UPS, rectifier)
3. 系統動態參數已收集 (發電機慣量、勵磁器、調速器)

---

## 1. 工作流程

### Step 1: 諧波分析與濾波器設計 (SK-D03-008)

**IEEE 519 限值**：

| 電壓等級 | THD_V 限值 | 個別諧波 |
|----------|-----------|---------|
| ≤1 kV | 8.0% | 5.0% |
| 1-69 kV | 5.0% | 3.0% |
| 69-161 kV | 2.5% | 1.5% |

**步驟**：識別諧波源 (VFD/UPS/整流器) → 建立頻率掃描模型 → 計算各匯流排 THD → 比對 IEEE 519 限值 → 設計濾波器 (passive/active)

**濾波器設計**：

```
被動式濾波器 (Tuned Filter):
- 調諧頻率: f = 1/(2π√(LC))
- 品質因數: Q = R/(ωL) — 典型 30-60
- 容量: 依諧波電流量決定 (MVAr)

主動式濾波器 (APF):
- 適用: 諧波源變動大、多次諧波
- 容量: 通常為負載容量 25-30%
```

**⚠️ 避坑**：被動濾波器可能與系統產生並聯共振；capacitor bank 切換會影響調諧點

### Step 2: 暫態穩定模擬 (SK-D03-009)

| 事件類型 | 模擬時間 | 關注指標 |
|----------|---------|---------|
| 三相短路清除 | 10 s | 臨界清除時間 (CCT) |
| 發電機跳脫 | 30 s | 頻率偏移、功角擺動 |
| 大負載投入 | 10 s | 電壓驟降恢復 |
| 再生能源驟降 | 30 s | 頻率穩定 |

**步驟**：定義暫態事件情境 → 設定動態模型 (generator/exciter/governor) → 執行時域模擬 → 分析功角/頻率/電壓曲線 → 判定穩定性 → 必要時加裝 PSS/SVC

**⚠️ 避坑**：模型參數不準導致結果失真；CCT 需留安全裕度 (≥100ms)

### Step 3: 電力系統建模 (SK-D03-010)

**建模流程**：

| 元件 | 必要參數 | 資料來源 |
|------|---------|---------|
| 發電機 | Xd, Xd', Xd", H, T'do | 原廠 datasheet |
| 變壓器 | Z%, tap range, vector group | 試驗報告 |
| 線路 | R, X, B (per km) | 製造商/手冊 |
| 負載 | P, Q, ZIP model | 現場量測 |

**步驟**：收集設備參數 → 建立 ETAP/PSS/E 模型 → 模型驗證 (與實測比對) → 版本管理 → 定期更新

**⚠️ 避坑**：模型必須定期校驗；參數缺失時的合理假設需文件化

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | 所有匯流排 THD 符合 IEEE 519 |
| 2 | 濾波器設計含共振檢查 |
| 3 | 暫態穩定模擬涵蓋所有關鍵事件 |
| 4 | CCT 留有安全裕度 |
| 5 | 電力模型已驗證 (與實測誤差 <5%) |
| 6 | 模型版本管理機制已建立 |

---

## 3. 人類審核閘門

```
進階分析完成。THD 最大：{%} | CCT 最小：{ms} | 模型元件：{n}
👉 請 PE 審核。
```

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D03-008 | Harmonic Analysis | IEEE 519、濾波器設計、頻率掃描 |
| SK-D03-009 | Transient Stability | 時域模擬、CCT、PSS |
| SK-D03-010 | Power System Modeling | ETAP/PSS/E、參數收集、模型驗證 |

<!-- Phase 6: Enhanced 2026-03-19. -->
