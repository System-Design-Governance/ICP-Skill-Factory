---
name: protocol-data-conversion
description: >
  協議與資料轉換。
  Configure protocol gateway devices that translate between different industrial protocols, enabling interoperability across heterogeneous OT/ICS system。Data Format Conversion Design specifies the logical and technical approach for translating heteroge
  MANDATORY TRIGGERS: 協定閘道配置, 時間戳同步設計, 協議與資料轉換, 資料格式轉換設計, 跨系統資料模型對齊, iec-61850, Protocol Gateway Configuration, Data Format Conversion Design, security-hardening, gateway-config, data, format, protocol-gateway.
  Use this skill for protocol data conversion tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 協議與資料轉換

本 Skill 整合 4 個工程技能定義，提供協議與資料轉換的完整工作流程。
適用領域：System Integration（D07）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D02-001, SK-D02-003, SK-D02-004, SK-D02-006, SK-D07-001

---

## 1. 輸入

- Protocol Gateway hardware specifications and datasheet (from vendor or procurement)
- Network architecture and zone/conduit diagram (from SK-D01-001)
- Data flow diagram identifying required protocol translations (from SK-D02-004 ⏳)
- Source and destination protocol specifications (Modbus, DNP3, IEC 61850, OPC UA technical standards)
- Security requirements and access control policies (from SK-D01-002, SK-D01-003)
- Failover and redundancy strategy (from SK-D02-006 ⏳)
- System architecture diagram from SK-D07-002 (identifies system boundaries and communication links requiring conversion)
- Data model specifications from each subsystem (Modbus registers, IEC 61850 data objects, DNP3 points, OPC UA attributes)
- Protocol documentation (IEC 61850, Modbus, DNP3, OPC UA specification references)
- Unit conversion requirements and normalization rules from engineering specifications
- Timestamp and time synchronization requirements
- Security and logging requirements for conversion operations

---

## 2. 工作流程

### Step 1: 協定閘道配置
**SK 來源**：SK-D07-003 — Protocol Gateway Configuration

執行協定閘道配置：Configure protocol gateway devices that translate between different industrial protocols, enabling interoperability across heterogeneous OT/ICS system

**本步驟交付物**：
- Protocol Gateway Configuration Document: hardware model, firmware version, enabled protocols, protocol mapping table
- Protocol Mapping Table: source protocol → destination protocol, translation rules, data type conversions, timing and latency specifications
- Data Point Mapping Table: source device → source data point → gateway mapping → destination device → destination data point, with validation rules

### Step 2: 資料格式轉換設計
**SK 來源**：SK-D07-004 — Data Format Conversion Design

執行資料格式轉換設計：Data Format Conversion Design specifies the logical and technical approach for translating heterogeneous data formats and protocols across integrated 

**本步驟交付物**：
- Data format conversion specification document with detailed mapping rules
- Protocol translation matrix showing source and target protocol elements, data types, and transformation logic
- Unit conversion and normalization rules handbook

### Step 3: 跨系統資料模型對齊
**SK 來源**：SK-D07-005 — Cross-System Data Model Alignment

執行跨系統資料模型對齊：Cross-System Data Model Alignment establishes semantic consistency and unified naming conventions for data exchanged between heterogeneous OT/IT syste

**本步驟交付物**：
- Data model alignment specification document with unified naming conventions and point mapping rules
- CIM/OPC UA information model mappings showing alignment between source systems and standardized models
- Point mapping matrix or spreadsheet documenting cross-system mappings for all exchange points

### Step 4: 時間戳同步設計
**SK 來源**：SK-D07-006 — Timestamp Synchronization Design

執行時間戳同步設計：Timestamp Synchronization Design defines the architecture and protocols for maintaining precise time synchronization across distributed OT/ICS systems

**本步驟交付物**：
- Time synchronization architecture design specifying protocol selection (NTP, PTP, IRIG-B) and synchronization hierarchy
- Grandmaster clock and secondary time source specifications with redundancy planning
- Accuracy requirements and acceptable time drift specifications for each subsystem class

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Protocol Gateway Configuration Document: hardware model, firmware version, enabled protocols, protocol mapping table | 依需求 |
| 2 | Protocol Mapping Table: source protocol → destination protocol, translation rules, data type conversions, timing and latency specifications | 依需求 |
| 3 | Data Point Mapping Table: source device → source data point → gateway mapping → destination device → destination data point, with validation rules | 依需求 |
| 4 | Failover Configuration Specification: redundancy model (active-passive, active-active), switchover triggers, test procedures | 依需求 |
| 5 | Gateway Security Hardening Checklist: firmware version verification, unused service disablement, access control enforcement, audit log configuration | Markdown |
| 6 | Network Connectivity Diagram showing gateway placement within zone/conduit architecture | 依需求 |
| 7 | Data format conversion specification document with detailed mapping rules | 依需求 |
| 8 | Protocol translation matrix showing source and target protocol elements, data types, and transformation logic | Markdown |
| 9 | Unit conversion and normalization rules handbook | 依需求 |
| 10 | Data model mapping spreadsheets or UML diagrams | 依需求 |
| 11 | Conversion test case definitions and expected result specifications | 依需求 |
| 12 | Implementation guide for SK-D07-003 conversion logic development | 依需求 |

---

## 4. 適用標準

- IEC 62443-2-4: Technical security measures for OT/ICS systems — protocol and interface protection requirements
- IEC 61850: Communication networks and systems for power utility automation — for gateway handling IEC 61850 protocols
- Modbus Organization: Modbus TCP specification — for gateway handling Modbus protocols
- DNP3 Technical Committee: DNP3 Secure Authentication specification — for secure DNP3 gateway operation
- OPC Foundation: OPC UA Specification — for OPC UA protocol gateway configuration
- IEC 62443-3-3: System Security Requirements and Security Levels — gateway security hardening baselines
- IEC 61850: Communication networks and systems in substations
- IEC 61970: Energy management system application program interface (EMS-API)
- Modbus Organization: Modbus Protocol Specification
- IEEE 1815 (DNP3): Electric Power Systems Communications and Control

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Gateway hardware is certified/approved for the industrial environment (temperatu | ✅ 已驗證 |
| 2 | Protocol mapping table is complete: every source protocol data point has a defin | ✅ 已驗證 |
| 3 | Data point mapping table is bidirectional (where applicable) and includes valida | ✅ 已驗證 |
| 4 | Failover configuration is tested: manual switchover triggers, recovery timing, a | ✅ 已驗證 |
| 5 | Security hardening checklist is 100% complete: firmware version documented and v | ✅ 已驗證 |
| 6 | Gateway configuration has been reviewed and approved by SAC or STC; protocol tra | ✅ 已驗證 |
| 7 | Data format conversion specification document is complete and includes conversio | ✅ 已驗證 |
| 8 | Protocol translation matrix is defined with explicit mappings between source and | ✅ 已驗證 |
| 9 | Unit conversion rules are documented for all physical quantities crossing subsys | ✅ 已驗證 |
| 10 | Timestamp normalization approach is defined, including time zone handling, synch | ✅ 已驗證 |
| 11 | Conversion test cases are defined with input/output examples that demonstrate co | ✅ 已驗證 |
| 12 | Security review confirms that conversion logic does not introduce data disclosur | ✅ 已驗證 |
| 13 | Data model alignment specification document is complete and includes unified nam | ✅ 已驗證 |
| 14 | CIM/OPC UA information model mappings are defined, showing how source system dat | ✅ 已驗證 |
| 15 | Point mapping matrix is comprehensive, documenting all cross-system mappings wit | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D07-003 | | Junior (< 2 yr) | 5–8 person-days | Assumes single gateway, 2–3 protocol translations, straightfor |
| SK-D07-003 | | Senior (5+ yr) | 2–3 person-days | Same scope; senior can leverage prior gateway configurations an |
| SK-D07-003 | Notes: Complex gateways with many-to-many protocol translations or custom transformation logic may r |
| SK-D07-004 | | Role            | Days (4-hour work units) | |
| SK-D07-004 | | Junior          | 10–14 days               | |
| SK-D07-004 | | Senior          | 5–7 days                 | |
| SK-D07-005 | | Role            | Days (4-hour work units) | |
| SK-D07-005 | | Junior          | 14–18 days               | |

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
協議與資料轉換已完成。
📋 執行範圍：4 個工程步驟（SK-D07-003, SK-D07-004, SK-D07-005, SK-D07-006）
📊 交付物清單：
  - Protocol Gateway Configuration Document: hardware model, firmware version, enabled protocols, protocol mapping table
  - Protocol Mapping Table: source protocol → destination protocol, translation rules, data type conversions, timing and latency specifications
  - Data Point Mapping Table: source device → source data point → gateway mapping → destination device → destination data point, with validation rules
  - Failover Configuration Specification: redundancy model (active-passive, active-active), switchover triggers, test procedures
  - Gateway Security Hardening Checklist: firmware version verification, unused service disablement, access control enforcement, audit log configuration
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
| Domain | D07 (System Integration) |
| SK 覆蓋 | SK-D07-003, SK-D07-004, SK-D07-005, SK-D07-006 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D07-003 | Protocol Gateway Configuration | 協定閘道配置 | Configure protocol gateway devices that translate between di |
| SK-D07-004 | Data Format Conversion Design | 資料格式轉換設計 | Data Format Conversion Design specifies the logical and tech |
| SK-D07-005 | Cross-System Data Model Alignment | 跨系統資料模型對齊 | Cross-System Data Model Alignment establishes semantic consi |
| SK-D07-006 | Timestamp Synchronization Design | 時間戳同步設計 | Timestamp Synchronization Design defines the architecture an |

<!-- Phase 5 Wave 2 deepened: SK-D07-003, SK-D07-004, SK-D07-005, SK-D07-006 -->