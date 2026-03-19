---
name: data-infrastructure
description: >
  資料基礎設施：資料擷取架構、TSDB 設計、資料治理、資料管線。
  MANDATORY TRIGGERS: 資料基礎設施, data infrastructure, TSDB, 時序資料庫,
  資料擷取, data acquisition, 資料治理, data governance, data pipeline.
  Use this skill for data infrastructure design in OT/ICS and energy analytics projects.
---

# 資料基礎設施 (Data Infrastructure)

整合 4 個 SK，涵蓋資料擷取、時序資料庫、資料治理、資料管線。

---

## 0. 初始化

1. 系統架構與網路拓撲已確定 (SK-D02-001)
2. SCADA 點位清單已完成 (SK-D05-001)
3. 安全區/管道架構已定義 (SK-D01-001)
4. 資料使用需求已從業務端蒐集 (監控/分析/報表)

---

## 1. 工作流程

### Step 1: 資料擷取架構設計 (SK-D12-001)

**擷取模式比較**：

| 模式 | 延遲 | 適用場景 | 頻寬需求 |
|------|------|----------|----------|
| Polling | 秒級 | 固定週期讀取 (SCADA) | 穩定、可預測 |
| Event-driven | 毫秒級 | 狀態變化觸發 (SOE) | 突發、不可預測 |
| Buffered | 分鐘級 | 邊緣暫存後批次上傳 | 低 (集中傳輸) |
| Streaming | 亞秒級 | 即時分析 (PMU) | 高、持續 |

**步驟**：
1. 盤點所有資料來源：SCADA、RTU、智慧電表、感測器、外部 API
2. 定義每來源的擷取模式與頻率
3. 設計邊緣處理邏輯：本地濾波、聚合、品質標記
4. 設計安全措施：傳輸加密、認證、ACL
5. 估算資料量：每日 GB、年度 TB
6. 設計 redundancy：主/備擷取路徑

**⚠️ 避坑**：
- Polling 過頻 → 頻寬飽和、設備過載
- 未做邊緣濾波 → 大量雜訊進入 TSDB，儲存暴增
- 安全措施不足 → 資料在傳輸中被竄改

### Step 2: 時序資料庫設計 (SK-D12-002)

**TSDB 選型考量**：

| 因素 | InfluxDB | TimescaleDB | PI System | Historian |
|------|----------|-------------|-----------|-----------|
| 寫入速度 | 高 | 高 | 高 | 中 |
| 壓縮率 | 好 | 中 | 優秀 | 好 |
| 查詢彈性 | InfluxQL/Flux | SQL | PI SDK | 專用 API |
| OT 整合 | 需開發 | 需開發 | 原生 | 原生 |
| 授權模式 | 開源/商業 | 開源/商業 | 商業 | 商業 |

**儲存估算公式**：
```
Daily = points × samples/s × 86400 × bytes/sample
範例: 10000 × 1/s × 86400 × 16B ≈ 13.8 GB/day
Year (uncompressed): ~5 TB → compressed: ~1-1.5 TB (10:1)
```

**步驟**：
1. 選擇 TSDB (基於效能、成本、整合性)
2. 設計 schema：measurement/tag/field 規範
3. 定義 retention policy：hot (30d) → warm (1y) → cold (5y+)
4. 設計 downsampling：raw (1s) → 1min avg → 1h avg → daily
5. 配置備份策略：增量 + 全量
6. 效能測試：寫入速率、查詢延遲

**⚠️ 避坑**：
- 未做 downsampling → 歷史查詢極慢
- Tag cardinality 爆炸 → index 膨脹，效能崩潰
- 未規劃 retention → 磁碟滿了才發現

### Step 3: 資料治理 (SK-D12-005)

**治理框架**：

| 面向 | 內容 |
|------|------|
| 資料分類 | 即時操作 / 歷史分析 / 機密 / 公開 |
| 品質標準 | 完整性、準確性、時效性 指標 |
| 存取控制 | 角色 × 資料集 矩陣 |
| 血緣追蹤 | 資料從來源到消費的全路徑 |
| 合規 | 法規保留期、隱私要求 |

**步驟**：
1. 建立資料分類標準
2. 定義資料品質 KPI (e.g., completeness ≥ 99.5%)
3. 建立存取控制矩陣：誰可看/改/刪哪些資料
4. 實作血緣追蹤 (data lineage)
5. 定義法規合規要求 (retention、privacy)
6. 指定 Data Steward 角色

**⚠️ 避坑**：治理只有文件沒有執行 → 形同虛設

### Step 4: 資料管線 (SK-D12-006)

**管線架構**：

```
Source → Ingestion → Validation → Transform → Store → Serve
  │         │           │           │         │        │
  OT      Kafka/     SK-D07-006   ETL/     TSDB    API/
 devices  MQTT       rules       Stream           Dashboard
```

**步驟**：
1. 設計 ingestion layer (message broker 選型)
2. 整合 SK-D07-006 驗證規則
3. 設計 ETL/ELT 流程 (transform logic)
4. 配置 store layer (TSDB + cold storage)
5. 設計 serve layer (API、query endpoint)
6. 實作監控：pipeline lag、throughput、error rate
7. 設計 failure handling：dead letter queue、retry、alerting

**⚠️ 避坑**：
- 管線無監控 → 資料靜默丟失數天才發現
- 未設 dead letter queue → 異常資料直接丟棄、無法事後分析

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | 所有資料來源已接入擷取管線 |
| 2 | TSDB 寫入/查詢效能符合設計規格 |
| 3 | Retention policy 已配置且 downsampling 運作正常 |
| 4 | 資料治理框架已實施 (分類、ACL、品質 KPI) |
| 5 | 管線監控含 lag、throughput、error rate |
| 6 | Failure handling 已測試 (dead letter queue、retry) |

---

## 3. 人類審核閘門

```
資料基礎設施完成。
📋 範圍：4 個工程步驟 (SK-D12-001, 002, 005, 006)
📊 交付物：擷取架構、TSDB 設計、治理框架、管線配置
⚠️ 待確認：{TBD 項目}
👉 請 SYS + Data Engineer 審核。
```

---

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D12-001 | Data Acquisition | 擷取模式、邊緣處理、資料量估算 |
| SK-D12-002 | TSDB Design | 選型、schema、retention、downsampling |
| SK-D12-005 | Data Governance | 分類、品質 KPI、存取控制、血緣 |
| SK-D12-006 | Data Pipeline | Ingestion→Validate→Transform→Store→Serve |

<!-- Phase 6: Enhanced 2026-03-19. -->
