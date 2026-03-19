---
name: protection-coordination
description: >
  Design protection coordination including overcurrent relay settings (TCC curves),
  distance relay zones, relay selection with IEC 61850 GOOSE, and relay testing procedures.
  MANDATORY TRIGGERS: 保護協調, protection coordination, 過電流, overcurrent, 距離保護,
  distance protection, 繼電器, relay, TCC, relay testing, relay selection,
  IEC 61850 GOOSE, zone protection, 保護整定, relay setting.
  Use this skill for overcurrent/distance protection design, relay selection, and testing.
---

# 保護協調設計 (Protection Coordination)

整合 4 個 SK，涵蓋過電流、距離保護、繼電器選型與測試。

---

## 0. 初始化

1. 短路分析已完成 (最大/最小故障電流)
2. 單線圖 (SLD) 含保護設備位置
3. 設備額定值已收集 (CT/PT ratio, 斷路器)

---

## 1. 工作流程

### Step 1: 過電流保護協調 (SK-D04-001)

**TCC 曲線設定原則**：

| 層級 | 元件 | 設定原則 | 時間間隔 |
|------|------|---------|---------|
| 最下游 | Fuse/MCCB | 保護電纜/負載 | — |
| 中游 | Feeder Relay | 上下游協調 | CTI ≥0.3s |
| 上游 | Main Relay | 後備保護 | CTI ≥0.3s |
| 最上游 | Utility Relay | 系統保護 | 與台電協調 |

**步驟**：收集 CT ratio → 計算 pickup (1.2-1.5× FLA) → 選擇曲線型式 (IEC SI/VI/EI) → 設定 time dial → 繪製 TCC → 驗證全範圍協調 (最大/最小故障)

**⚠️ 避坑**：CT 飽和影響協調；DG 併入改變故障電流方向需重新檢討

### Step 2: 距離保護設定 (SK-D04-002)

| Zone | 覆蓋範圍 | 時間 | 設定值 |
|------|---------|------|--------|
| Zone 1 | 80% 本線路 | 瞬時 | 0.8 × Z_line |
| Zone 2 | 100% 本線 + 20% 次線 | 0.3-0.5s | 1.2 × Z_line |
| Zone 3 | 後備 (100% 次線) | 1.0-1.5s | 視系統而定 |

**步驟**：計算線路阻抗 → 設定各 Zone reach → 考慮 infeed effect → 設定 Mho/Quad 特性 → 驗證 load encroachment → 方向元件設定

**⚠️ 避坑**：Zone 3 過度覆蓋可能導致誤跳 (類似 2003 北美大停電)；負載阻抗不可進入保護區

### Step 3: 繼電器選型 (SK-D04-003)

| 考量 | 內容 |
|------|------|
| 保護功能 | 50/51, 21, 87, 27/59 |
| 通訊 | IEC 61850 GOOSE/MMS |
| I/O | DI/DO/AI 數量 |
| 冗餘 | 主保護 + 後備保護 |

**步驟**：定義保護功能需求 → 評估 IEC 61850 支援 → 確認 GOOSE 互通性 → 選定廠牌型號 → 整合至 SAS 架構

### Step 4: 繼電器測試 (SK-D04-006)

**測試項目**：

| 測試類型 | 方法 | 驗證項目 |
|----------|------|---------|
| 一次注入 | CT 一次側加電流 | 整體迴路正確性 |
| 二次注入 | 測試器注入 CT 二次側 | 繼電器設定值 |
| 功能測試 | 模擬故障情境 | 跳脫邏輯/時間 |
| GOOSE 測試 | IEC 61850 訊號 | 通訊正確性 |

**⚠️ 避坑**：一次注入需停電且安全措施；測試完必須恢復正常設定

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | TCC 全範圍協調 (CTI ≥0.3s) |
| 2 | Distance zone 設定經計算驗證 |
| 3 | 無 load encroachment 風險 |
| 4 | 繼電器功能測試 100% 通過 |
| 5 | GOOSE 通訊測試通過 |
| 6 | 測試報告完整 (含設定值記錄) |

---

## 3. 人類審核閘門

```
保護協調完成。Relay 數：{n} | TCC 層級：{levels} | 測試通過率：{%}
👉 請 PE + FAT 工程師審核。
```

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D04-001 | Overcurrent Coordination | TCC 曲線、pickup、time dial |
| SK-D04-002 | Distance Protection | Zone 1/2/3、Mho/Quad |
| SK-D04-003 | Relay Selection | IEC 61850 GOOSE、SAS 整合 |
| SK-D04-006 | Relay Testing | 一次/二次注入、功能測試 |

<!-- Phase 6: Enhanced 2026-03-19. -->
