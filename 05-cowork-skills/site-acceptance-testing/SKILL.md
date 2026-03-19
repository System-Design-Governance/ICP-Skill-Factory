---
name: site-acceptance-testing
description: >
  現場驗收測試：SAT 程序、SAT 執行、SIT 執行、效能驗證。
  MANDATORY TRIGGERS: SAT, 現場驗收, site acceptance, SIT, 系統整合測試,
  性能驗證, performance verification, site test.
  Use this skill for site acceptance and integration testing in OT/ICS projects.
---

# 現場驗收測試 (Site Acceptance Testing)

整合 4 個 SK，涵蓋 SAT 程序開發、SAT/SIT 執行、效能驗證。

---

## 0. 初始化

1. FAT 已完成且結果報告已產出 (SK-D08-001, SK-D08-002)
2. 系統已安裝於現場、網路已佈建
3. 現場環境資訊已取得 (溫度、濕度、EMI、海拔)
4. 現場 IT/OT 系統整合需求已確認
5. 明確區分：SAT = 現場單系統驗收；SIT = 跨系統端對端整合

---

## 1. 工作流程

### Step 1: SAT 程序撰寫 (SK-D08-003)

**SAT vs. FAT 差異**：

| 面向 | FAT | SAT |
|------|-----|-----|
| 地點 | 工廠/整合商 | 現場 |
| 環境 | 受控 | 實際 (溫度/EMI/濕度) |
| 網路 | 模擬 | 現場 topology |
| 整合 | Standalone | 與現場系統連線 |
| 資料 | 模擬資料 | 真實 data source |

**步驟**：
1. 從 FAT 程序適配：保留核心案例、新增現場特定場景
2. 新增環境測試：系統在實際溫度/EMI 條件下運行
3. 新增現場網路測試：實際路由、延遲、防火牆規則
4. 新增真實資料源測試：天氣、感測器、電網介面
5. 定義現場安全限制：進出管制、LOTO 程序

**⚠️ 避坑**：直接複製 FAT 程序 → 未考慮現場環境差異，測試無意義

### Step 2: SAT 執行 (SK-D08-004)

**執行流程**：
1. Pre-SAT 檢查：硬體安裝完成、軟體部署、網路連通
2. 依 SAT 程序逐案例執行
3. 每案例記錄：日期、測試者、實際結果、pass/fail、證據
4. 偏差記錄：FAT 結果 vs. SAT 結果差異 + root cause
5. 缺陷登記：失敗案例 → snag list (severity + owner + deadline)
6. 產出 SAT 完成證書 (所有 mandatory 案例 pass)

**⚠️ 避坑**：
- 未比對 FAT/SAT 結果差異 → 現場新增問題被忽略
- As-built 文件未同步更新 → 設計文件與實際配置不符

### Step 3: SIT 執行 (SK-D08-005)

**SIT 測試重點**：

| 類別 | 驗證項目 |
|------|----------|
| 跨系統資料流 | SCADA→Historian→報表 全程驗證 |
| 協定互通 | 異廠商設備間通訊 |
| 安全 SR 驗證 | 每個 SR：Implemented / Planned / N/A |
| SL 達成 | 每 Zone 的 SL-Achieved vs. SL-Target |
| 端對端延遲 | 事件產生 → 顯示/告警 的總延遲 |

**步驟**：
1. 從 FR/SR 矩陣建立 SR 驗證清單
2. 逐 SR 執行測試：test / inspection / review
3. 記錄每 SR 狀態 + 證據
4. 失敗 SR → compensating control 提案 + risk acceptance
5. 產出 SL 達成摘要 (per zone)
6. 編譯 Gate 3 安全證據包

**⚠️ 避坑**：SR 狀態標為 N/A 但未附理由 → Gate 3 審核退件

### Step 4: 效能驗證 (SK-D08-006)

**效能指標**：

| 指標 | 測量方法 | 典型門檻 |
|------|----------|----------|
| 響應時間 | 事件→HMI 顯示 | < 2 s |
| 吞吐量 | 同時處理點位數 | ≥ 設計值 |
| CPU/Memory | 穩態負載 | < 70% |
| 通訊可靠度 | 丟包率 | < 0.1% |
| Failover 時間 | 主→備切換 | < 30 s |

**步驟**：
1. 定義效能基準 (from 設計規格)
2. 配置監控工具 (SNMP、system monitor、network analyzer)
3. 穩態測試：正常負載持續運行 24h+
4. 尖峰測試：模擬最大負載場景
5. 壓力測試：超過設計值觀察降級行為
6. Failover 測試：切斷主系統觀察切換

**⚠️ 避坑**：僅測穩態 → 尖峰時系統崩潰未被發現

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | SAT 程序已從 FAT 適配並新增現場場景 |
| 2 | SAT 100% mandatory 案例 pass |
| 3 | 所有適用 SR 已驗證 (Implemented/Planned/N/A + 理由) |
| 4 | 每 Zone SL-Achieved ≥ SL-Target |
| 5 | 效能指標符合設計規格 |
| 6 | Gate 3 安全證據包已編譯 |
| 7 | Snag list 所有 Critical/Major 項已解決或有核准 workaround |

---

## 3. 人類審核閘門

```
現場驗收完成。
📋 範圍：4 個工程步驟 (SK-D08-003~006)
📊 交付物：SAT 報告、SR 驗證報告、效能報告、Gate 3 證據包
⚠️ 待確認：{TBD 項目}
👉 請 STC + 現場 OPS + 客戶代表審核。
```

---

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D08-003 | SAT Procedure | FAT→SAT 適配、環境測試、現場整合 |
| SK-D08-004 | SAT Execution | 逐案例執行、偏差記錄、snag list |
| SK-D08-005 | SIT Execution | SR 驗證、SL 達成、Gate 3 證據 |
| SK-D08-006 | Performance Verification | 響應時間、吞吐量、failover |

<!-- Phase 6: Enhanced 2026-03-19. -->
