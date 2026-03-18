---
name: scada-foundation
description: >
  SCADA 基礎構建。
  Develop the comprehensive SCADA point list defining all monitored and controlled points including: point ID, description, data type, scaling factors, 。Design the SCADA real-time database structure including point database schema, historical data tabl
  MANDATORY TRIGGERS: SCADA 資料庫結構設計, SCADA 基礎構建, SCADA 點位清單建立, Master Data Management, SCADA Database Structure Design, Data Management, Data Acquisition, SCADA Point List Development, scada foundation, Real-time Database, Point Configuration.
  Use this skill for scada foundation tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# SCADA 基礎構建

本 Skill 整合 2 個工程技能定義，提供SCADA 基礎構建的完整工作流程。
適用領域：Control Systems（D05）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D03-001, SK-D03-002, SK-D04-004, SK-D05-003, SK-D05-010, SK-D06-002

---

## 1. 輸入

- One-line diagram and network topology (substations, circuits, equipment locations)
- Equipment specifications (transformers, circuit breakers, disconnects, capacitor banks, DERs)
- Instrumentation schedule (PT/CT ratings, RTU/PMU point counts, analog/digital I/O counts)
- Protection logic diagrams (trip signals, alarm outputs from relays/IEDs)
- Operational procedures and control requirements (load flow targets, voltage regulation setpoints)
- SCADA architecture design (RTU/FEP configuration, polling intervals, data retention policy)
- SCADA point list (SK-D05-001) with all field definitions: point ID, data type, scaling, scan rate
- SCADA platform architecture and database backend selection (relational, time-series, hybrid)
- Real-time data flow requirements (polling intervals, latency targets, data rate projections)
- Historical data retention policy (archival duration, query performance targets)
- Calculated point specifications (derived values, aggregations, filtering logic)
- Security and audit requirements (access logging, data change tracking, encryption)

---

## 2. 工作流程

### Step 1: SCADA 點位清單建立
**SK 來源**：SK-D05-001 — SCADA Point List Development

執行SCADA 點位清單建立：Develop the comprehensive SCADA point list defining all monitored and controlled points including: point ID, description, data type, scaling factors, 

**本步驟交付物**：
- Master SCADA point list (Excel/database format with all fields)
- Point ID naming convention specification and examples
- Data type reference guide (analog, digital, status, calculated points)

### Step 2: SCADA 資料庫結構設計
**SK 來源**：SK-D05-002 — SCADA Database Structure Design

執行SCADA 資料庫結構設計：Design the SCADA real-time database structure including point database schema, historical data tables, event logging schema, and calculated point defi

**本步驟交付物**：
- Real-time database schema design document
- Point database table structure (point metadata, current values, timestamps)
- Calculated point definition and refresh schedules

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Master SCADA point list (Excel/database format with all fields) | Markdown |
| 2 | Point ID naming convention specification and examples | 依需求 |
| 3 | Data type reference guide (analog, digital, status, calculated points) | 依需求 |
| 4 | Scaling and engineering units table (for instrument transforms) | 依需求 |
| 5 | Alarm limit specification for each monitored point | 依需求 |
| 6 | Scan rate and priority classification (real-time, near-real-time, historical) | 依需求 |
| 7 | Real-time database schema design document | 依需求 |
| 8 | Point database table structure (point metadata, current values, timestamps) | 依需求 |
| 9 | Calculated point definition and refresh schedules | 依需求 |
| 10 | Data type mapping (SCADA abstraction → database native types) | 依需求 |
| 11 | Historical data tables and partitioning scheme | 依需求 |
| 12 | Time-series table design with appropriate indexing | 依需求 |

---

## 4. 適用標準

- ANSI/IEEE 1379 (Standard Guide for Application of Power Apparatus Protective Relays)
- IEEE C37.2 (Electrical and Electronics Graphic Symbols)
- IEC 61850-7-4 (Logical Nodes and Data Objects for IEC 61850)
- NERC CIP-005 (Physical and Electronic Perimeter Security)
- NERC CIP-013 (Cyber Security Supply Chain Risk Management)
- ISO/IEC 27001 (Information Security Management Systems)
- ISO/IEC 13249-3 (SQL/MED — Management of External Data)
- ANSI SQL (Standard Query Language for database design)
- IEEE 1637 (Guide for Steady-State Load Flow Studies)
- IEC 61850-6 (Configuration Language for IEC 61850)

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Point list includes all monitored field devices: analog inputs (voltage, current | ✅ 已驗證 |
| 2 | Every point has unique, descriptive ID following enterprise naming convention (e | ✅ 已驗證 |
| 3 | Data type specified for all points (16-bit/32-bit integer, floating-point, enume | ✅ 已驗證 |
| 4 | Scaling factors and engineering units documented (MVA, kV, A, °C, percentage, pp | ✅ 已驗證 |
| 5 | Alarm limits defined for all analog points (high/low alarm thresholds, rate-of-c | ✅ 已驗證 |
| 6 | Scan rates assigned with documented rationale (critical protection signals: 100  | ✅ 已驗證 |
| 7 | Data source mapping complete: RTU ID, coil/register address, communication proto | ✅ 已驗證 |
| 8 | IEC 61850 Logical Node cross-reference provided (e.g., MMXU for metering points, | ✅ 已驗證 |
| 9 | Real-time point database schema includes: point ID (primary key), current value, | ✅ 已驗證 |
| 10 | Calculated point table defined with: definition logic, input points, refresh rat | ✅ 已驗證 |
| 11 | Historical data tables partitioned by time (daily or monthly) for optimal query  | ✅ 已驗證 |
| 12 | Aggregation tables created for common query patterns (hourly/daily min/max/avg f | ✅ 已驗證 |
| 13 | Event logging schema captures: event ID, timestamp, point ID, old/new value, ala | ✅ 已驗證 |
| 14 | Change audit log records: change timestamp, user ID, object type, object ID, bef | ✅ 已驗證 |
| 15 | Communications event log tracks: RTU/FEP connection status changes, protocol err | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D05-001 | | Requirements definition & stakeholder review | 12 hours | Operational needs, monitoring/control sc |
| SK-D05-001 | | Network topology & equipment extraction | 16 hours | One-line analysis, protection logic review, i |
| SK-D05-001 | | Point ID naming convention development | 4 hours | Standard definition, examples, documentation | |
| SK-D05-001 | | Master point list creation | 24 hours | Equipment-by-equipment point enumeration, data type assign |
| SK-D05-001 | | Scaling & alarm limit specification | 16 hours | Engineering units, threshold definition, rate-of- |
| SK-D05-001 | | Scan rate & priority classification | 8 hours | RTU/FEP capacity analysis, real-time vs. historica |
| SK-D05-001 | | Data source & RTU addressing mapping | 12 hours | Communication protocol assignment, address alloc |
| SK-D05-001 | | IEC 61850 Logical Node cross-reference | 8 hours | LN/DO mapping for digital substation interfaces |

---

## 7. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 輸入完整性 | 所有必要輸入文件已讀取並摘要 |
| 2 | 流程覆蓋 | 2 個工作步驟皆已執行並有產出 |
| 3 | 輸出完整性 | 所有交付物已產出、格式正確、非空白 |
| 4 | 標準合規 | 產出引用的標準版本正確 |
| 5 | 術語一致 | 專案術語、縮寫與 glossary 一致 |
| 6 | 跨步驟一致 | 各步驟產出間無矛盾（如數量、SL等級） |

---

## 8. 人類審核閘門

完成所有工作步驟後，暫停並向使用者提交審核：

```
SCADA 基礎構建已完成。
📋 執行範圍：2 個工程步驟（SK-D05-001, SK-D05-002）
📊 交付物清單：
  - Master SCADA point list (Excel/database format with all fields)
  - Point ID naming convention specification and examples
  - Data type reference guide (analog, digital, status, calculated points)
  - Scaling and engineering units table (for instrument transforms)
  - Alarm limit specification for each monitored point
⚠️ 待確認事項：{列出 TBD 項目或需人工判斷的假設}
👉 請審核以上成果，確認 PASS / FAIL / PASS with Conditions。
```

**判定標準**：
- **PASS**：成果完整且正確，可進入下一階段或歸檔
- **FAIL**：發現重大缺漏或錯誤，需返工後重新提交
- **PASS with Conditions**：整體接受，但需補充特定項目後完成

---

## 9. IEC 62443 生命週期對應

| 項目 | 值 |
|------|---|
| 主要生命週期階段 | 依專案階段 |
| Domain | D05 (Control Systems) |
| SK 覆蓋 | SK-D05-001, SK-D05-002 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D05-001 | SCADA Point List Development | SCADA 點位清單建立 | Develop the comprehensive SCADA point list defining all moni |
| SK-D05-002 | SCADA Database Structure Design | SCADA 資料庫結構設計 | Design the SCADA real-time database structure including poin |

<!-- Phase 5 Wave 2 deepened: SK-D05-001, SK-D05-002 -->