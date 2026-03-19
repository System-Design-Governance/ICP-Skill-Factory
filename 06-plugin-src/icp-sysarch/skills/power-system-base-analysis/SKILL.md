---
name: power-system-base-analysis
description: >
  Perform power system base analysis including load flow (power flow), short circuit calculation,
  and voltage stability analysis using ETAP/PSS/E tools.
  MANDATORY TRIGGERS: 潮流分析, power flow, 短路分析, short circuit, 電壓穩定, voltage stability,
  ETAP, PSS/E, load flow, 負載潮流, 故障電流, fault current, V-Q, 無功補償,
  reactive power, contingency analysis, IEC 60909.
  Use this skill for power flow, short circuit, and voltage stability studies.
---

# 電力系統基礎分析 (Power System Base Analysis)

整合 3 個 SK，涵蓋潮流、短路與電壓穩定分析。

---

## 0. 初始化

1. 單線圖 (SLD) 已完成
2. 設備參數已收集 (阻抗、額定值、tap 位置)
3. 負載資料已取得 (MW/MVAr, power factor)
4. 分析工具已備妥 (ETAP 或 PSS/E)

---

## 1. 工作流程

### Step 1: 潮流分析 (SK-D03-001)

**分析情境**：

| 情境 | 負載條件 | 發電條件 | 目的 |
|------|---------|---------|------|
| Peak Load | 最大負載 | 全發電 | 設備容量確認 |
| Light Load | 最小負載 | 部分發電 | 過電壓風險 |
| N-1 Contingency | Peak | 移除單一元件 | 可靠度驗證 |
| Emergency | Peak | 移除關鍵饋線 | 極端情境 |

**步驟**：建立系統模型 → 設定 swing bus/PV bus/PQ bus → 執行 Newton-Raphson 收斂 → 分析匯流排電壓 (0.95-1.05 pu) → 線路負載率 (<80%) → Contingency 分析

**⚠️ 避坑**：潮流不收斂常因 reactive power 不足或 tap 設定錯誤；N-1 需逐一移除非僅最壞

### Step 2: 短路分析 (SK-D03-002)

**IEC 60909 計算**：

```
Ik" = c × Un / (√3 × Zk)
- c: 電壓因子 (1.0/1.1)
- Zk: 短路阻抗 (正序)
- 考慮: 三相/單相/兩相短路
```

**步驟**：設定故障類型與位置 → 計算 Ik" (初始短路電流) → Ip (峰值) → Ik (穩態) → 比對設備額定值 → 確認斷路器啟斷容量

**⚠️ 避坑**：馬達貢獻不可忽略；必須考慮系統擴充後的故障電流成長

### Step 3: 電壓穩定分析 (SK-D03-003)

**V-Q 靈敏度分析**：

| 匯流排 | V-Q 靈敏度 | 穩定裕度 | 補償建議 |
|--------|-----------|---------|---------|
| Bus-A | 高 (>0.05) | 不足 | 加裝 SVC/STATCOM |
| Bus-B | 中 | 足夠 | 監控 |
| Bus-C | 低 | 充裕 | 無需 |

**步驟**：執行 V-Q 曲線分析 → 識別弱匯流排 → 計算無功補償需求 (MVAr) → 選定補償設備 (capacitor bank/SVC/STATCOM) → 驗證補償後電壓

**⚠️ 避坑**：capacitor bank 有電壓崩潰風險 (V 低時 Q 輸出降低)；需搭配 OLTC 協調

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | 所有情境潮流收斂、電壓在 0.95-1.05 pu |
| 2 | N-1 Contingency 無過載/電壓違限 |
| 3 | 短路電流不超過設備額定 |
| 4 | IEC 60909 計算方法正確引用 |
| 5 | V-Q 穩定裕度已確認 |
| 6 | 無功補償方案已定義 |

---

## 3. 人類審核閘門

```
電力分析完成。潮流情境：{n} | 短路最大：{kA} | 弱匯流排：{buses}
👉 請 PE + SYS 審核。
```

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D03-001 | Power Flow Analysis | Newton-Raphson、contingency、ETAP/PSS/E |
| SK-D03-002 | Short Circuit Analysis | IEC 60909、故障電流計算 |
| SK-D03-003 | Voltage Stability | V-Q 靈敏度、無功補償 |

<!-- Phase 6: Enhanced 2026-03-19. -->
