# EPCI 變電所提案工作流模式

> 基於 Formosa 6 ONS EPCI 專案實績（NT$285M，12 版迭代）

---

## 1. 工作流總覽

大型 EPCI 變電所提案不是線性流程，而是**迭代收斂**的過程。

```
需求分析 → Scope 界定 → 子系統分解 → 概念架構
    ↓
CBOM 初版 → 交叉驗證 → 精算修正 → 底層清帳
    ↓              ↑___________|（迭代）
報價單比對 → Scope Boundary Audit → 版本發布
```

**F6 實績**：從 v0.1 到 v1.1 經歷 12 次迭代，主要修正原因：
- PRP 交換機數量修正（+80%）
- DGA 子系統移除（-3.2M）
- Cybersecurity scope 界定（30-38M 待定區間）
- 底層清帳發現公式/遺漏差異（~20M）

---

## 2. 需求分析階段（T01-T03）

### 2.1 EPCI 特有需求萃取

| 維度 | 重點 | F6 案例 |
|------|------|--------|
| 合規要求 | IEC 62443 SL-T、IEC 61850 Edition | IEC 62443 SL-2/SL-3 混合 |
| 通訊架構 | PRP/HSR 需求、Station Bus 規格 | PRP LAN-A/B 雙骨幹 |
| 站點數量 | 多站點分拆、站間通訊 | ONS + OnSWST |
| 業主介面 | TPC/SCADA 介面、既有設備整合 | 業主 SCADA 饋入 |
| Scope 邊界 | 明確 In/Out scope | Cybersecurity scope 爭議 |

### 2.2 隱性需求辨識（EPCI 級）

除通用隱性需求外，變電所 EPCI 案常見：
- PRP RedBox（非 PRP 原生設備的轉換需求）
- GPS/PTP 時間同步（保護功能依賴精確時間）
- 備品策略（離岸站點的現場備品倉需求）
- 環境防護（鹽霧/濕度/溫度對設備選型的影響）
- 退場/換約費用（長期營運合約的退出成本）

---

## 3. Scope 界定決策點

大型 EPCI 案最關鍵的 Presales 決策：

| 決策點 | 影響範圍 | F6 案例 |
|--------|---------|--------|
| Cybersecurity scope 含/不含 | 30-50M 級差異 | 30-38M 待定 |
| PRP vs 單網 | 交換機數量 ×2-3 | 15→27 台 |
| 備品含/不含 | 5-10% 設備成本 | 含關鍵備品 |
| CCTV 含/不含 | 獨立子系統 | F6 不含 |
| 訓練範圍 | 人天差異 2-10 天 | 含基礎訓練 |

**原則**：模糊 scope 一律假設「含」並估算，在假設清單中標記 `[$]`，留待 Gate 0 決策。

---

## 4. T05→T06 介面（Architecture-CBOM Mapping）

架構設計產出的「設備清冊」必須與 CBOM 行項目 1:1 對應：

```markdown
| 架構元件 | Zone | Purdue Level | CBOM 品項 | 數量 | 備註 |
|---------|------|-------------|----------|------|------|
| PRP Switch LAN-A | L2 | Bay Level | CBOM-H15 | 12 | 每 Bay 2 台 |
| FortiGate 60F | DMZ | L3.5 | CBOM-H01 | 2 | ONS + OnSWST 各一 |
```

此 mapping table 為 T08 Global Review 的核心驗證依據。

---

## 5. CBOM 版本演化追蹤

每次 CBOM 重大修正須記錄：

```markdown
| 版本 | 日期 | 金額 (TWD) | 主要變更 | 觸發原因 |
|------|------|-----------|---------|---------|
| v0.1 | 2026-03-01 | 250M | 初版 15 子系統 | T06 初版 |
| v0.5 | 2026-03-10 | 268M | PRP 精算 15→27 台 | Port budget 驗證 |
| v0.8 | 2026-03-15 | 288M | Cybersecurity scope 含入 | Scope 決策 |
| v0.9 | 2026-03-18 | 268M | 底層清帳修正 | T08 清帳 |
| v1.0 | 2026-03-20 | 285M | DGA 移除 + 最終調整 | 報價單比對 |
```

此表格為 Gate 0 Decision Package 的必要組件。

---

## 6. Presales → Detailed Design 傳遞

Pre-Gate 0 結束時，以下知識必須正式傳遞：

| 交付物 | 傳遞對象 | 格式 |
|--------|---------|------|
| CBOM 定版 + 版本演化 | PM/Procurement | Excel + 演化摘要 |
| 架構圖 + Zone/Conduit | SYS Architect | D2/Mermaid + 定義表 |
| Open Items Register | PM/SYS/SAC | Markdown 表格 |
| 假設清單 | PM | assumptions.md |
| 風險矩陣 | PM/SAC | risk_matrix.md |

**傳遞儀式**：Gate 0 核准後 5 個工作天內完成正式交接會議。
