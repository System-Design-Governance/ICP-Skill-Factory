---
name: renewable-energy-integration
description: >
  Integrate renewable energy sources including PV grid connection, BESS sizing, VPP dispatch,
  and DER aggregation for power system applications.
  MANDATORY TRIGGERS: 再生能源, renewable energy, PV, 太陽能, solar, BESS, 儲能,
  energy storage, VPP, 虛擬電廠, virtual power plant, DER, 分散式能源,
  distributed energy resource, 併網, grid connection, inverter, 逆變器.
  Use this skill for PV integration, BESS design, VPP dispatch, and DER aggregation.
---

# 再生能源整合 (Renewable Energy Integration)

整合 4 個 SK，涵蓋 PV 併網、儲能、虛擬電廠與分散式能源聚合。

---

## 0. 初始化

1. 電力系統基礎分析已完成 (潮流/短路)
2. 再生能源場址資料已取得 (日照/風速/容量)
3. 電網併接規範已確認 (台電/IEEE 1547)

---

## 1. 工作流程

### Step 1: PV 併網設計 (SK-D03-004)

| 項目 | 規範 | 關鍵參數 |
|------|------|---------|
| 逆變器選型 | IEEE 1547 | P/Q capability, THD <5% |
| 反孤島保護 | IEEE 1547.1 | 偵測時間 <2s |
| 電力品質 | IEEE 519 | 諧波限值、功率因數 |
| 功率控制 | 台電併網規範 | 功率斜率限制 |

**步驟**：PV 容量計算 → 逆變器配置 (string/central/micro) → 反孤島保護設計 → 電力品質評估 → 併網點 (POI) 保護協調

**⚠️ 避坑**：雲遮效應造成功率驟變需 ramp rate 控制；反孤島偵測不可與電壓穩定保護衝突

### Step 2: 儲能系統設計 (SK-D03-005)

```markdown
BESS 設計參數：
- 容量: {MWh} = Peak Shaving 需求 × 持續時間
- 功率: {MW} = 最大充放電需求
- SOC 操作範圍: 10%-90% (延長壽命)
- 循環壽命: >6000 cycles @ 80% DOD
- 熱管理: HVAC, 溫度 15-35°C
- BMS: cell balancing, fault protection
```

**步驟**：應用場景定義 (削峰/調頻/備用) → 容量/功率計算 → 電池化學選擇 (LFP/NMC) → SOC 管理策略 → 熱管理設計 → BMS 整合

**⚠️ 避坑**：SOC 極端值 (<5% 或 >95%) 加速衰退；熱失控風險需消防設計

### Step 3: VPP 調度 (SK-D03-006)

**調度優化**：

| 目標 | 約束 | 演算法 |
|------|------|--------|
| 最小化成本 | 功率平衡、SOC 限制 | MILP |
| 最大化收益 | 市場價格、併網限制 | Dynamic Programming |
| 削峰填谷 | 需量契約、設備壽命 | Rule-based + Opt |

**步驟**：DER 資源盤點 → 預測模型 (負載/發電) → 調度演算法設計 → 市場參與策略 → 即時調度與回饋

### Step 4: DER 聚合管理 (SK-D03-007)

**聚合架構**：DER → 聚合器 (DERMS) → 電力交易平台/調度中心

**步驟**：DER 拓撲設計 → 通訊協定選定 (IEEE 2030.5/OpenADR) → 聚合控制策略 → 資安防護 (加密/認證) → 合規檢查

**⚠️ 避坑**：DER 通訊延遲影響調度精度；需考慮 DER owner 退出的降級策略

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | PV 併網通過電力品質模擬 (THD, flicker) |
| 2 | 反孤島保護符合 IEEE 1547 |
| 3 | BESS 容量/功率滿足應用場景 |
| 4 | SOC 管理策略含壽命保護 |
| 5 | VPP 調度演算法驗證完成 |
| 6 | DER 通訊與資安設計已定義 |
| 7 | 併網規範合規確認 |

---

## 3. 人類審核閘門

```
再生能源整合完成。PV：{MW} | BESS：{MWh} | DER 數：{n}
👉 請 PE + SYS 審核。
```

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D03-004 | PV Grid Connection | 逆變器、反孤島、電力品質 |
| SK-D03-005 | BESS Design | 容量/SOC/循環壽命/熱管理 |
| SK-D03-006 | VPP Dispatch | 調度優化、市場策略 |
| SK-D03-007 | DER Aggregation | 聚合拓撲、資安、OpenADR |

<!-- Phase 6: Enhanced 2026-03-19. -->
