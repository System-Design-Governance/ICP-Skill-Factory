---
name: control-strategy-configuration
description: >
  Configure control strategies including AGC, DERMS, PID tuning, load management,
  and frequency regulation for power system operations.
  MANDATORY TRIGGERS: 控制策略, control strategy, AGC, automatic generation control,
  DERMS, PID, PID tuning, 負載管理, load management, 頻率調節, frequency regulation,
  demand response, 需量反應, load shedding, 卸載, droop, 合成慣量, synthetic inertia,
  ACE, participation factor, Ziegler-Nichols.
  Use this skill for AGC, DERMS, PID, load management, and frequency regulation design.
---

# 控制策略配置 (Control Strategy Configuration)

整合 5 個 SK，涵蓋 AGC、DERMS、PID、負載管理與頻率調節。

---

## 0. 初始化

1. 電力系統模型已建立
2. 發電/負載資料已取得
3. 控制目標與約束條件已確認

---

## 1. 工作流程

### Step 1: AGC 配置 (SK-D05-003)

**ACE 計算**：

```
ACE = (Pa - Ps) - 10β(Fa - Fs)
- Pa: 實際功率交換
- Ps: 排程功率交換
- β: 頻率偏差係數 (MW/0.1Hz)
- Fa/Fs: 實際/排程頻率
```

**步驟**：設定 ACE 公式參數 → 定義參與因子 (participation factor) → 設定 deadband → 配置 ramp rate 限制 → 模擬驗證

**⚠️ 避坑**：participation factor 總和必須為 1；ramp rate 需考慮機組實際響應能力

### Step 2: DERMS 配置 (SK-D05-004)

| 功能 | 說明 | 關鍵參數 |
|------|------|---------|
| DER 監控 | 即時狀態收集 | 更新週期 ≤5s |
| 調度控制 | 有功/無功指令下發 | 響應時間 ≤30s |
| 預測 | 發電/負載預測 | 15min/1hr ahead |
| 優化 | 經濟調度/電壓管理 | 目標函數定義 |

**步驟**：DER 註冊與建模 → 通訊介面配置 (IEEE 2030.5) → 控制模式設定 (local/remote) → 調度邏輯配置 → 測試驗證

### Step 3: PID 調諧 (SK-D05-012)

**Ziegler-Nichols 方法**：

| 控制器 | Kp | Ti | Td |
|--------|----|----|-----|
| P | 0.5Ku | — | — |
| PI | 0.45Ku | Pu/1.2 | — |
| PID | 0.6Ku | Pu/2 | Pu/8 |

*Ku: 極限增益, Pu: 極限週期*

**步驟**：識別受控程序特性 → 選擇調諧方法 (Z-N/Cohen-Coon/自動) → 設定初始參數 → 階躍測試 → 微調 (overshoot <10%, settling <5τ)

**⚠️ 避坑**：Z-N 方法偏積極，OT 環境常需降低增益 25-50%

### Step 4: 負載管理 (SK-D05-013)

| 策略 | 觸發條件 | 動作 | 恢復 |
|------|---------|------|------|
| Demand Response | 尖峰/價格訊號 | 減載非關鍵負載 | 自動 |
| Load Shedding | 頻率 <49.0Hz | 依優先序卸載 | 手動確認 |
| Peak Shaving | 需量接近契約 | BESS 放電 | SOC 回復 |

**步驟**：負載分類 (可卸/不可卸) → 優先序設定 → 觸發條件定義 → 卸載量計算 → 恢復程序 → 測試驗證

### Step 5: 頻率調節 (SK-D05-014)

**Droop 設定**：

```
Droop = (Δf/fn) / (ΔP/Pn) × 100%
典型值: 4-5% (即頻率變化 1% → 功率變化 20-25%)

合成慣量 (Synthetic Inertia):
- 適用: 逆變器型 DER (PV/BESS)
- 原理: df/dt 偵測 → 快速功率注入
- 響應時間: <100ms
```

**步驟**：設定 droop 參數 → 配置合成慣量 (BESS/inverter) → 頻率保護整合 (UFLS) → 動態模擬驗證 → 與 AGC 協調

**⚠️ 避坑**：droop 過小導致功率擺盪；合成慣量需足夠 BESS 容量支撐

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | AGC ACE 收斂至 deadband 內 |
| 2 | DERMS 調度指令響應 ≤30s |
| 3 | PID overshoot <10%、穩態誤差 <1% |
| 4 | 負載卸載測試通過 |
| 5 | 頻率響應符合電網規範 |
| 6 | 所有控制策略有降級模式 |

---

## 3. 人類審核閘門

```
控制策略完成。AGC 機組：{n} | PID 迴路：{n} | 卸載層級：{levels}
👉 請 SYS + Control Engineer 審核。
```

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D05-003 | AGC Configuration | ACE、participation factor |
| SK-D05-004 | DERMS | DER 管理、調度控制 |
| SK-D05-012 | PID Tuning | Ziegler-Nichols、調諧方法 |
| SK-D05-013 | Load Management | Demand response、load shedding |
| SK-D05-014 | Frequency Regulation | Droop、synthetic inertia |

<!-- Phase 6: Enhanced 2026-03-19. -->
