---
name: protocol-data-conversion
description: >
  協定轉換與資料格式處理：閘道組態、資料格式轉換、時間同步、資料驗證。
  MANDATORY TRIGGERS: 協定轉換, protocol conversion, 閘道, gateway, 時間同步, time sync,
  NTP, PTP, 資料驗證, data validation, data format, 資料格式.
  Use this skill for protocol gateway configuration and data conversion tasks in OT/ICS projects.
---

# 協定與資料轉換 (Protocol & Data Conversion)

整合 4 個 SK，涵蓋閘道組態、格式轉換、時間同步、資料驗證。

---

## 0. 初始化

1. 介面整合矩陣已完成 (SK-D07-001)
2. 通訊協定與資料流圖已定義
3. 安全區/管道架構已確定 (SK-D01-001)
4. 時間精度需求已從系統需求提取

---

## 1. 工作流程

### Step 1: 協定閘道組態 (SK-D07-003)

**常見協定轉換場景**：

| 來源協定 | 目標協定 | 典型場景 | 閘道方案 |
|----------|----------|----------|----------|
| Modbus RTU | Modbus TCP | Serial→Ethernet 升級 | Serial-to-Ethernet converter |
| DNP3 Serial | IEC 60870-5-104 | 跨廠商整合 | Protocol gateway appliance |
| OPC-DA | OPC-UA | Legacy→Modern SCADA | OPC-UA wrapper |
| Proprietary | MQTT/REST | IoT 邊緣整合 | Edge gateway + custom driver |

**步驟**：
1. 從介面矩陣識別需要協定轉換的介面
2. 選擇閘道硬體/軟體方案 (效能、安全、成本)
3. 配置來源端連線參數 (port, baud rate, address)
4. 配置目標端連線參數
5. 設定點位映射表：來源暫存器 → 目標標籤
6. 配置安全設定：TLS、認證、ACL
7. 效能測試：延遲 < 需求值、吞吐量 ≥ 需求值

**⚠️ 避坑**：
- 點位映射錯誤 → 控制指令送到錯誤設備，可能造成安全事故
- 閘道成為單點故障 → 需 redundant pair 或 failover 機制
- 未設定 timeout/retry → 通訊中斷時閘道 hang 住

### Step 2: 資料格式轉換設計 (SK-D07-004)

**轉換層級**：

| 層級 | 內容 | 範例 |
|------|------|------|
| Encoding | 字元編碼/二進位格式 | Big-endian → Little-endian |
| Schema | 結構映射 | XML → JSON, CSV → Parquet |
| Semantics | 意義對應 | Vendor tag name → 標準命名 |
| Unit | 單位轉換 | °F → °C, PSI → kPa |
| Quality | 品質碼對應 | OPC quality → IEC quality code |

**步驟**：
1. 建立來源/目標資料模型對照表
2. 定義轉換規則 (公式、查表、條件邏輯)
3. 處理例外：null 值、超範圍值、品質碼異常
4. 實作並單元測試轉換邏輯
5. 驗證轉換正確性：round-trip test

**⚠️ 避坑**：Endianness 錯誤 → 數值完全錯誤但格式看似正常，難以察覺

### Step 3: 時間同步組態 (SK-D07-005)

**時間同步協定比較**：

| 協定 | 精度 | 適用場景 | 網路需求 |
|------|------|----------|----------|
| NTP | 1-10 ms | SCADA、Historian | UDP 123 |
| PTP (IEEE 1588) | < 1 μs | 保護繼電器、PMU | PTP-capable switches |
| IRIG-B | < 1 μs | Substation LAN | 專用纜線 |
| GPS | < 100 ns | 主時鐘源 | GPS 天線 |

**步驟**：
1. 依系統精度需求選擇同步協定
2. 設計時鐘階層：GPS → Grandmaster → Boundary Clock → Slave
3. 配置 NTP/PTP server 與 client
4. 設定 holdover 策略 (GPS 失鎖時的行為)
5. 配置監控告警：時間偏差 > 門檻值 → 告警

**⚠️ 避坑**：
- 事件記錄時戳不同步 → 事故調查時序混亂，無法重建事件鏈
- PTP 經過非 PTP switch → 精度從 μs 退化到 ms

### Step 4: 資料驗證 (SK-D07-006)

**驗證規則類型**：

| 類型 | 規則 | 範例 |
|------|------|------|
| Range | 值域檢查 | 0 ≤ 電壓 ≤ 500 kV |
| Rate | 變化率檢查 | ΔT/Δt ≤ 5°C/min |
| Consistency | 跨點一致性 | P = V × I (±5%) |
| Completeness | 完整性 | 必要欄位不可為 null |
| Timeliness | 時效性 | 資料延遲 < 30 s |
| Format | 格式 | ISO 8601 時戳 |

**步驟**：
1. 從系統需求提取驗證規則
2. 分類規則為 hard (reject) vs. soft (flag + pass)
3. 實作驗證邏輯 (edge side 或 platform side)
4. 定義失敗處理：reject、substitute (last known good)、flag
5. 配置驗證結果日誌與儀表板

**⚠️ 避坑**：驗證規則過嚴 → 合法突波被丟棄；過鬆 → 髒資料進入分析管線

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | 所有需轉換介面已配置閘道且點位映射正確 |
| 2 | 資料格式轉換通過 round-trip 驗證 |
| 3 | 時間同步精度符合系統需求 (NTP ≤ 10ms / PTP ≤ 1μs) |
| 4 | 驗證規則覆蓋所有關鍵資料點 |
| 5 | 閘道 failover 測試通過 |
| 6 | 驗證失敗處理邏輯已測試 (reject / substitute / flag) |

---

## 3. 人類審核閘門

```
協定與資料轉換完成。
📋 範圍：4 個工程步驟 (SK-D07-003~006)
📊 交付物：閘道組態 ({n} 台)、轉換規則 ({m} 條)、時間同步架構、驗證規則集
⚠️ 待確認：{TBD 項目}
👉 請 SYS + Protocol Engineer 審核。
```

---

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D07-003 | Protocol Gateway Config | 閘道選型、點位映射、安全設定、failover |
| SK-D07-004 | Data Format Conversion | Encoding/Schema/Semantics/Unit 轉換 |
| SK-D07-005 | Time Sync Config | NTP/PTP/IRIG-B 階層設計、holdover |
| SK-D07-006 | Data Validation | Range/Rate/Consistency 規則、失敗處理 |

<!-- Phase 6: Enhanced 2026-03-19. -->
