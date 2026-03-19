---
name: scada-foundation
description: >
  Design SCADA point lists (ID/type/scale/alarm/scan rate) and real-time database structures
  including historical data and event logging schemas.
  MANDATORY TRIGGERS: SCADA, 點位清單, point list, SCADA DB, 資料庫結構, database structure,
  point configuration, 掃描速率, scan rate, 即時資料庫, real-time database,
  historian, 歷史資料, event logging, 事件記錄.
  Use this skill for SCADA point list design and database structure definition.
---

# SCADA 基礎設計 (SCADA Foundation)

整合 2 個 SK，涵蓋點位清單與資料庫結構設計。

---

## 0. 初始化

1. 系統架構與通訊協定已確定
2. I/O 清單已從 P&ID / SLD 產出
3. 告警需求已初步定義

---

## 1. 工作流程

### Step 1: 點位清單設計 (SK-D05-001)

**點位命名規範**：

```
{Station}_{System}_{Device}_{Signal}_{Type}
範例: SS01_XFMR_TR01_WINDING_TEMP_AI
      SS01_FDR_F01_CB_STATUS_DI
      SS01_FDR_F01_CB_TRIP_DO
```

**點位欄位定義**：

| 欄位 | 說明 | 範例 |
|------|------|------|
| Point ID | 唯一識別碼 | SS01_TR01_TEMP_AI |
| Point Type | AI/AO/DI/DO/CI | AI |
| Engineering Unit | 工程單位 | °C |
| Raw Range | 原始範圍 | 4-20 mA |
| Eng Range | 工程範圍 | 0-150 °C |
| Scan Rate | 掃描週期 | 1 s |
| Alarm HH/H/L/LL | 告警門檻 | 120/100/10/5 |
| Deadband | 變化門檻 | 0.5 °C |
| Source | 來源設備/協定 | RTU-01/Modbus |

**步驟**：從 I/O 清單匯入 → 套用命名規範 → 設定 scaling (raw→eng) → 定義 scan rate (依重要性) → 設定 alarm limits → 定義 deadband → 審查與去重

**⚠️ 避坑**：命名不一致會造成維護噩夢；scan rate 過快浪費頻寬、過慢漏事件

### Step 2: 資料庫結構設計 (SK-D05-002)

**三層架構**：

| 層級 | 用途 | 保留期 | 技術 |
|------|------|--------|------|
| Real-time DB | 即時值顯示/控制 | 當前值 | In-memory |
| Historical DB | 趨勢分析/報表 | 1-5 年 | Time-series DB |
| Event/SOE DB | 事件追溯/稽核 | 5-10 年 | Relational DB |

**Historical 儲存估算**：

```
每日資料量 = 點位數 × 每秒取樣數 × 86400 × 每筆 bytes
範例: 10000 點 × 1/s × 86400 × 20B = ~16 GB/day
年: ~5.8 TB (未壓縮), 壓縮後 ~1-2 TB
```

**步驟**：設計 real-time DB schema → 設計 historical storage (壓縮/歸檔策略) → 設計 event/SOE table → 定義 data retention policy → 備份策略

**⚠️ 避坑**：historical DB 不壓縮會快速耗盡儲存；event log 必須含 ms 時戳

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | 所有 I/O 點位已建檔且命名一致 |
| 2 | Scaling/alarm/deadband 已設定 |
| 3 | Scan rate 依重要性分級 |
| 4 | Historical DB 儲存估算完成 |
| 5 | Data retention policy 已定義 |
| 6 | Event/SOE 時戳精度 ≤1ms |

---

## 3. 人類審核閘門

```
SCADA 基礎完成。點位數：{n} | Historical：{TB}/年 | Retention：{年}
👉 請 SYS + SCADA 工程師審核。
```

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D05-001 | Point List Design | 命名規範、scaling、alarm、scan rate |
| SK-D05-002 | DB Structure | Real-time/Historical/Event、儲存估算 |

<!-- Phase 6: Enhanced 2026-03-19. -->
