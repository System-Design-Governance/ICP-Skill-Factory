# EPCI 成本風險因子資料庫

> 基於 Formosa 6 ONS EPCI 專案實績校正（NT$285M）

---

## 1. 風險因子總覽

| # | 風險因子 | 類別 | 典型機率 | 典型影響 | F6 實績 |
|---|---------|------|---------|---------|--------|
| CR-E01 | PRP 設備數量低估 | Technical | 60% | 基礎×5-10% | 交換機 15→27 台（+80%），影響 ~15M |
| CR-E02 | Cybersecurity scope 未定 | Scope | 40% | ±30-50M | 30-38M 待定區間 |
| CR-E03 | Scope boundary 爭議 | Scope | 30% | ±5-10M | DGA 移除 -3.2M |
| CR-E04 | 供應商交期延遲 | Supply | 35% | 基礎×2-5% | — |
| CR-E05 | 現場環境限制 | Schedule | 25% | 基礎×3-5% | 離岸鹽霧環境 |
| CR-E06 | 匯率波動 (EUR/USD) | Financial | 20% | 基礎×1-3% | EUR 設備約 5% |
| CR-E07 | 電力系統整合複雜度 | Technical | 30% | 基礎×3-8% | IEC 61850 多廠牌整合 |
| CR-E08 | 業主介面需求變更 | Scope | 40% | 基礎×2-5% | TPC SCADA 介面 |
| CR-E09 | 離岸運輸/安裝風險 | Schedule | 20% | 基礎×1-3% | 海運+吊裝 |
| CR-E10 | 人力資源不足 | Resource | 25% | 基礎×2-4% | 資安+電力雙專長稀缺 |

---

## 2. 三情境模型校正

### 2.1 通用 IT/OT 案（<100M）

| 情境 | Contingency % | 適用條件 |
|------|-------------|---------|
| Low | 3% | Scope 明確、單站、無 PRP |
| Baseline | 5% | 標準 OT/ICS 案 |
| High | 10% | 多站、PRP、scope 爭議 |

### 2.2 大型 EPCI 案（>100M）

| 情境 | Contingency % | 適用條件 |
|------|-------------|---------|
| Low | 3% | Scope 完全鎖定、單一站點 |
| Baseline | 5% | 標準 EPCI（F6 對齊值） |
| High | 10% | 多站 + PRP + 離岸 + scope 爭議 |

> **F6 實績**：G5 佔比 13.3%（含 Risk 5% + PM + 差旅），Risk 單獨佔 5%。

### 2.3 原有 4%/10%/24% 為何偏高

- 24% High scenario 在投標場景中不具競爭力
- 業界 EPC 慣例 contingency 為 3-10%
- 超過 10% 通常表示 scope 定義不足，應回到需求釐清階段

---

## 3. 風險因子詳述

### CR-E01: PRP 設備數量低估

**描述**：PRP 雙骨幹架構使交換機需求倍增，概念階段容易以單網估算。

**影響計算**：
```
低估金額 = (實際交換機數 - 估算數) × 平均單價
F6 案例：(27 - 15) × ~1.2M = ~14.4M
```

**緩解策略**：
- 概念設計階段即使用 PRP 三倍化精算（見 cbom-builder epci_substation_patterns.md §3）
- Port budget 驗證作為 T06a 精算回圈觸發條件

### CR-E02: Cybersecurity scope 未定

**描述**：OT Cybersecurity 在變電所 EPCI 中常是最後確定的 scope，金額波動大。

**影響計算**：
```
影響範圍 = Cybersecurity 子系統總額（通常佔 G1 的 15-25%）
F6 案例：30-38M 待定（佔 285M 的 10.5-13.3%）
```

**緩解策略**：
- 在 CBOM 中分別列出「含 Cyber」和「不含 Cyber」兩版金額
- Gate 0 時要求業主明確 Cybersecurity scope
- 納入 Open Items Register

### CR-E03: Scope boundary 爭議

**描述**：EPCI 合約邊界模糊導致品項歸屬爭議。

**F6 案例**：DGA（溶解氣體分析）設備移除 -3.2M（非 OT cybersecurity scope）。

**緩解策略**：
- SOW 分析時明確列出 In/Out scope 邊界表
- 爭議品項在 CBOM 中標記 `[Scope TBD]`
- 假設清單標記 `[$]`

---

## 4. CBOM 版本演化摘要模板

Gate 0 Decision Package 中必須包含此摘要，讓決策者理解成本收斂過程：

```markdown
## CBOM 版本演化摘要

| 版本 | 日期 | 金額 (TWD) | Δ vs 前版 | 主要變更 | 觸發原因 |
|------|------|-----------|----------|---------|---------|
| v0.1 | YYYY-MM-DD | xxxM | — | 初版 | T06 初版 |
| v0.n | YYYY-MM-DD | xxxM | ±xM | {變更摘要} | {觸發原因} |
| v1.0 | YYYY-MM-DD | xxxM | ±xM | 定版 | T08 Global Review |

**可信度評估**：
- 迭代次數：{n} 次
- 最大單次修正：±{x}M（{原因}）
- 最終版穩定性：最後 {n} 版金額波動 < {x}%
- 殘餘不確定性：{列出 TBD 品項和 Open Items}
```
