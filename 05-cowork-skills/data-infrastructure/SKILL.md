---
name: data-infrastructure
description: >
  資料採集與基礎設施。
  Design the data acquisition architecture for collecting operational data from OT field devices, SCADA systems, and smart meters. This skill covers the。Develop protocol parsers and drivers for collecting data from operational technology (OT) devices u
  MANDATORY TRIGGERS: 資料採集架構設計, 資料保留策略設計, 時序資料庫選型與配置, 協定解析器開發, 資料採集與基礎設施, Modbus, edge-processing, configuration, data, design, data-acquisition, time, error-handling.
  Use this skill for data infrastructure tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 資料採集與基礎設施

本 Skill 整合 4 個工程技能定義，提供資料採集與基礎設施的完整工作流程。
適用領域：Energy Data Platform（D12）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D01-020, SK-D01-024, SK-D01-033, SK-D02-001, SK-D05-008

---

## 1. 輸入

- System architecture and network topology (from SK-D02-001 ⏳: OT Network Topology Design)
- Single-Line Diagram with metering and SCADA monitoring points identified (from SK-D09-003 ⏳: SLD Development, or D09 equipment design)
- SCADA/DCS system architecture and available data points (from customer specifications or legacy system documentation)
- Operational data requirements specification:
- What data must be collected (real-time power flows, voltages, temperatures, etc.)
- Collection frequency / latency requirements (real-time vs. interval-based)
- Data Acquisition Architecture specification (from SK-D12-001)
- Device inventory and communication specifications (protocol type, register maps, point lists)
- Protocol standards documentation (Modbus TCP/RTU, IEC 61850 MMS, DNP3, OPC UA specifications)
- Security requirements from design review (data validation rules, allowed message types, anomaly thresholds)
- System environment specifications (hardware, operating system, runtime constraints)
- Test data sets and device communication logs for validation

---

## 2. 工作流程

### Step 1: 資料採集架構設計
**SK 來源**：SK-D12-001 — Data Acquisition Architecture Design

執行資料採集架構設計：Design the data acquisition architecture for collecting operational data from OT field devices, SCADA systems, and smart meters. This skill covers the

**本步驟交付物**：
- Data Acquisition Architecture Diagram showing:
- Data sources (field devices, SCADA systems, meters) and their locations
- Data collection protocols per source/zone

### Step 2: 協定解析器開發
**SK 來源**：SK-D12-002 — Protocol Parser Development

執行協定解析器開發：Develop protocol parsers and drivers for collecting data from operational technology (OT) devices using industrial protocols (Modbus, IEC 61850 MMS, D

**本步驟交付物**：
- Protocol parser/driver source code (C, Python, or language per architecture specification)
- Parser configuration files (register maps, message templates, protocol-specific parameters)
- Error handling and logging specifications (malformed packet detection, security event logging)

### Step 3: 時序資料庫選型與配置
**SK 來源**：SK-D12-003 — Time-Series Database Selection and Configuration

執行時序資料庫選型與配置：This skill encompasses the evaluation, selection, and configuration of time-series database platforms suitable for storing operational data from OT/IC

**本步驟交付物**：
- Database Selection Matrix: comparison of candidate time-series database platforms against evaluation criteria (performance, scalability, cost, vendor 
- Database Sizing Calculations: estimated storage requirements based on data volumes, retention periods, and compression; hardware specifications (CPU, 
- Database Configuration Documentation: detailed specifications for deployment including replication settings, retention policies, query optimization pa

### Step 4: 資料保留策略設計
**SK 來源**：SK-D12-004 — Data Retention Policy Design

執行資料保留策略設計：This skill encompasses the design of data retention policies that specify how long operational data, security logs, and audit data will be retained, a

**本步驟交付物**：
- Data Retention Policy Document: policy statement specifying retention periods by data classification, archival procedures, deletion schedules, and sec
- Data Retention Matrix: table showing data element/type, classification level, minimum retention period, archival method, and deletion trigger
- Storage Tiering Plan: design for hot storage (active queryable data), warm storage (less frequently accessed), and cold storage (archive) with transit

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Data Acquisition Architecture Diagram showing: | 依需求 |
| 2 | Data sources (field devices, SCADA systems, meters) and their locations | 依需求 |
| 3 | Data collection protocols per source/zone | 依需求 |
| 4 | Data collection points (RTU, gateway, edge processor) | 依需求 |
| 5 | Data flows (source → collector → processing → storage) | 依需求 |
| 6 | Polling frequencies / event triggers per data source | 依需求 |
| 7 | Protocol parser/driver source code (C, Python, or language per architecture specification) | 依需求 |
| 8 | Parser configuration files (register maps, message templates, protocol-specific parameters) | 依需求 |
| 9 | Error handling and logging specifications (malformed packet detection, security event logging) | 依需求 |
| 10 | Protocol-specific security validation rules and implementation code | 依需求 |
| 11 | Unit test suite with protocol-level edge cases (oversized packets, invalid message types, sequence violations) | 依需求 |
| 12 | Integration test results demonstrating parser functioning with live/simulated devices | 依需求 |

---

## 4. 適用標準

- IEC 60870-5-104: Telecontrol equipment and systems — DNP3 alternative and industry standard protocol
- IEC 61850: Communication networks and systems for power utility automation — modern data model for power system data
- Modbus Organization Modbus/TCP specification — widely used legacy protocol in industrial automation
- DNP3 Technical Committee DNP3 standard — North American utility standard
- IEC 62443-4-1 & 4-2: Security for Industrial Automation and Control Systems — data protection and secure communication r
- NERC CIP (North America): Critical Infrastructure Protection standards for operational data handling
- IEC 61508: Functional Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems — data quality and 
- IEC 62443-4-2: Security-Oriented Design and Development — secure coding practices for critical control system software
- Modbus Organization Technical Committee: Modbus TCP, Modbus RTU specifications (if Modbus used)
- IEC 61850: Communication networks and systems for power utility automation (if IEC 61850 used)

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Data Acquisition Architecture Diagram covers 100% of identified data sources: fi | ✅ 已驗證 |
| 2 | For each data source, the selected collection protocol is justified with referen | ✅ 已驗證 |
| 3 | Polling frequencies and event-driven triggers are specified for each data stream | ✅ 已驗證 |
| 4 | Data quality validation rules are defined for all data streams; accuracy and com | ✅ 已驗證 |
| 5 | Security requirements for data-in-transit (encryption, authentication, access co | ✅ 已驗證 |
| 6 | Edge processing strategy (if used) is documented with clear roles: local alertin | ✅ 已驗證 |
| 7 | Bandwidth and latency impact assessment is complete; impacts on network design ( | ✅ 已驗證 |
| 8 | Architecture has been reviewed and approved by SYS, SAC, and SCADA Integrator (o | ✅ 已驗證 |
| 9 | Parser correctly interprets all specified industrial protocol message formats (M | ✅ 已驗證 |
| 10 | Data extraction from device registers/points matches documented specifications w | ✅ 已驗證 |
| 11 | All malformed packet types (oversized, invalid message structure, out-of-sequenc | ✅ 已驗證 |
| 12 | Security validation rules reject unauthorized message types and anomalous commun | ✅ 已驗證 |
| 13 | Error handling and logging meet completeness criteria: every error condition is  | ✅ 已驗證 |
| 14 | Unit test coverage ≥ 90% for parser code; integration testing confirms successfu | ✅ 已驗證 |
| 15 | Parser performance meets architecture specification: message latency < specifica | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D12-001 | | Junior System Architect (< 2 yr) | 8–12 person-days | Moderate complexity project, ~20–30 data poi |
| SK-D12-001 | | Senior System Architect (5+ yr) | 4–6 person-days | Same scope; senior leverages protocol librarie |
| SK-D12-001 | Notes: Complex multi-site deployments or projects with aggressive data collection requirements (sub- |
| SK-D12-002 | | Junior (< 2 yr) | 15–25 person-days | Per protocol; includes research, development, testing, docum |
| SK-D12-002 | | Senior (5+ yr) | 7–12 person-days | Same scope; leverages prior experience with protocol parsing p |
| SK-D12-002 | Notes: Multi-protocol parsers scale sub-linearly if protocols share similar structures (e.g., Modbus |
| SK-D12-003 | | Junior (< 2 yr) | 8–12 person-days | Assumes evaluation of 3–4 platforms, single-site deployment,  |
| SK-D12-003 | | Senior (5+ yr) | 4–6 person-days | Same scope; senior has strong knowledge of platform strengths/w |

---

## 7. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 輸入完整性 | 所有必要輸入文件已讀取並摘要 |
| 2 | 流程覆蓋 | 4 個工作步驟皆已執行並有產出 |
| 3 | 輸出完整性 | 所有交付物已產出、格式正確、非空白 |
| 4 | 標準合規 | 產出引用的標準版本正確 |
| 5 | 術語一致 | 專案術語、縮寫與 glossary 一致 |
| 6 | 跨步驟一致 | 各步驟產出間無矛盾（如數量、SL等級） |
| 7 | 依賴追溯 | 外部依賴 SK 的輸入已驗證可用 |

---

## 8. 人類審核閘門

完成所有工作步驟後，暫停並向使用者提交審核：

```
資料採集與基礎設施已完成。
📋 執行範圍：4 個工程步驟（SK-D12-001, SK-D12-002, SK-D12-003, SK-D12-004）
📊 交付物清單：
  - Data Acquisition Architecture Diagram showing:
  - Data sources (field devices, SCADA systems, meters) and their locations
  - Data collection protocols per source/zone
  - Data collection points (RTU, gateway, edge processor)
  - Data flows (source → collector → processing → storage)
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
| Domain | D12 (Energy Data Platform) |
| SK 覆蓋 | SK-D12-001, SK-D12-002, SK-D12-003, SK-D12-004 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D12-001 | Data Acquisition Architecture Design | 資料採集架構設計 | Design the data acquisition architecture for collecting oper |
| SK-D12-002 | Protocol Parser Development | 協定解析器開發 | Develop protocol parsers and drivers for collecting data fro |
| SK-D12-003 | Time-Series Database Selection and Configuration | 時序資料庫選型與配置 | This skill encompasses the evaluation, selection, and config |
| SK-D12-004 | Data Retention Policy Design | 資料保留策略設計 | This skill encompasses the design of data retention policies |

<!-- Phase 5 Wave 2 deepened: SK-D12-001, SK-D12-002, SK-D12-003, SK-D12-004 -->