---
name: integration-planning
description: >
  整合規劃與架構。
  Develop the system-level interface integration matrix that comprehensively maps all inter-system communication interfaces within the overall OT/ICS so。System Integration Architecture Diagram design defines the complete visual and logical representati
  MANDATORY TRIGGERS: 整合規劃與架構, 介面整合矩陣建立, 系統整合架構圖繪製, architecture, security-zone, IEC-62443, system, diagram, system-architecture, integration, System Integration Architecture Diagram.
  Use this skill for integration planning tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 整合規劃與架構

本 Skill 整合 2 個工程技能定義，提供整合規劃與架構的完整工作流程。
適用領域：System Integration（D07）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D01-002, SK-D01-003, SK-D01-011, SK-D02-001, SK-D02-004

---

## 1. 輸入

- Functional architecture and system decomposition (from SK-D01-002 ⏳: Defense-in-Depth Strategy Design and SK-D01-011 ⏳: Functional Architecture Defini
- Zone/Conduit architecture (from SK-D01-001: Zone/Conduit Architecture Design)
- Network topology diagram (from SK-D02-001 ⏳: OT Network Topology Design; or being developed in parallel)
- Data flow diagrams (from SK-D02-004 ⏳: Data Flow Diagram Development)
- Functional and performance requirements (from customer SOW, NERC CIP, IEEE, IEC standards)
- Inter-system communication specifications and technical interface specifications from vendors (communication protocol documentation, API specification
- Security architecture design from SK-D01-001 (security zones, trust boundaries, access rules)
- System requirements and functional specifications from project scope documentation
- Network topology and physical site layout diagrams
- Legacy system inventories and technical datasheets
- Regulatory compliance requirements (IEC 62443, NERC CIP, grid codes)
- Protocol and interface specifications for candidate integration technologies

---

## 2. 工作流程

### Step 1: 介面整合矩陣建立
**SK 來源**：SK-D07-001 — Interface Integration Matrix Development

執行介面整合矩陣建立：Develop the system-level interface integration matrix that comprehensively maps all inter-system communication interfaces within the overall OT/ICS so

**本步驟交付物**：
- System-Level Interface Integration Matrix (structured table or spreadsheet):
- Interface ID (unique identifier, e.g., "INT-SCADA-RTU-01", "INT-EMS-DERMS-001")
- Source System (e.g., "SCADA Master", "EMS Server", "RTU-001", "PMU-002")

### Step 2: 系統整合架構圖繪製
**SK 來源**：SK-D07-002 — System Integration Architecture Diagram

執行系統整合架構圖繪製：System Integration Architecture Diagram design defines the complete visual and logical representation of heterogeneous OT/ICS system interconnections 

**本步驟交付物**：
- System integration architecture diagram (Visio, Draw.io, or AutoCAD format) showing all subsystems and interconnections
- Data flow diagram depicting information movement between systems with directionality and volume indicators
- Protocol stack matrices mapping which protocols operate on which communication links

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | System-Level Interface Integration Matrix (structured table or spreadsheet): | Markdown |
| 2 | Interface ID (unique identifier, e.g., "INT-SCADA-RTU-01", "INT-EMS-DERMS-001") | 依需求 |
| 3 | Source System (e.g., "SCADA Master", "EMS Server", "RTU-001", "PMU-002") | 依需求 |
| 4 | Destination System (e.g., "RTU", "Field Device", "Historian", "Protection Relay", "DMS") | 依需求 |
| 5 | Communication Protocol(s) (e.g., "Modbus TCP", "IEC 60870-5-104", "DNP3", "OPC-UA", "MQTT", "REST API") | 依需求 |
| 6 | Direction (unidirectional source → destination, or bidirectional) | 依需求 |
| 7 | System integration architecture diagram (Visio, Draw.io, or AutoCAD format) showing all subsystems and interconnections | 依需求 |
| 8 | Data flow diagram depicting information movement between systems with directionality and volume indicators | 依需求 |
| 9 | Protocol stack matrices mapping which protocols operate on which communication links | 依需求 |
| 10 | Security zone boundary overlay diagrams aligned with SK-D01-001 design | 依需求 |
| 11 | Integration topology documentation including equipment lists and communication link specifications | Markdown |
| 12 | Diagram validation checklist and completeness assessment | Markdown |

---

## 4. 適用標準

- IEC 62443-1-1: Terminology, concepts and models — interface and communication definitions in ICS context
- IEC 62443-3-2: Security Risk Assessment for System Design — interface-level risk assessment and control design
- IEC 62351-1 / IEC 62351-3: Power Systems Management and Associated Information Exchange Data and Communication Security 
- NERC CIP-005 / CIP-007: Cyber Security Standards for Critical Infrastructure Protection (if applicable to North American
- IEEE 1686 / IEEE 1815: Interfaces for distributed energy resources; DNP3 and IEC 61850 protocol standards
- IEC 61850: Communication networks and systems for power utility automation (protocol-level interface definitions)
- Customer security and interoperability standards
- IEC 62443-2-1: Establishing an industrial automation and control systems security program
- IEC 62443-3-3: System security requirements and security levels
- NIST SP 800-82: Guide to Industrial Control Systems (ICS) Security

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Every inter-system data exchange identified in the data flow diagram (SK-D02-004 | ✅ 已驗證 |
| 2 | Every matrix entry includes: source system, destination system, protocol, latenc | ✅ 已驗證 |
| 3 | 100% of interfaces crossing security zone boundaries are explicitly identified a | ✅ 已驗證 |
| 4 | For zone-crossing interfaces: authentication and encryption methods are specifie | ✅ 已驗證 |
| 5 | No interface has latency or protocol requirements that conflict with the securit | ✅ 已驗證 |
| 6 | All standard protocols are identified with their security strengths and weakness | ✅ 已驗證 |
| 7 | Legacy system interfaces are identified and their security constraints documente | ✅ 已驗證 |
| 8 | Interface compatibility analysis identifies any protocol conflicts or data model | ✅ 已驗證 |
| 9 | All major subsystems (SCADA, EMS, DERMS, historian, protection, metering) are id | ✅ 已驗證 |
| 10 | Data flow directions between systems are explicitly shown with annotations indic | ✅ 已驗證 |
| 11 | Security zone boundaries from SK-D01-001 are overlaid on the architecture diagra | ✅ 已驗證 |
| 12 | Protocol stacks for each communication link are specified in a matrix format, in | ✅ 已驗證 |
| 13 | The diagram has been reviewed and validated by at least the System Architect, Se | ✅ 已驗證 |
| 14 | Completeness assessment confirms that all known system interfaces, data requirem | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D07-001 | | Junior (< 2 yr) | 4–6 person-days | ~15–25 interfaces; includes discovery, protocol research, late |
| SK-D07-001 | | Senior (5+ yr) | 2–3 person-days | Same scope; senior can leverage protocol knowledge and pattern  |
| SK-D07-001 | Notes: Large distributed systems (> 50 interfaces, multiple sites, legacy heterogeneous subsystems)  |
| SK-D07-002 | | Role            | Days (4-hour work units) | |
| SK-D07-002 | | Junior          | 12–16 days               | |
| SK-D07-002 | | Senior          | 6–8 days                 | |

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
整合規劃與架構已完成。
📋 執行範圍：2 個工程步驟（SK-D07-001, SK-D07-002）
📊 交付物清單：
  - System-Level Interface Integration Matrix (structured table or spreadsheet):
  - Interface ID (unique identifier, e.g., "INT-SCADA-RTU-01", "INT-EMS-DERMS-001")
  - Source System (e.g., "SCADA Master", "EMS Server", "RTU-001", "PMU-002")
  - Destination System (e.g., "RTU", "Field Device", "Historian", "Protection Relay", "DMS")
  - Communication Protocol(s) (e.g., "Modbus TCP", "IEC 60870-5-104", "DNP3", "OPC-UA", "MQTT", "REST API")
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
| SK 覆蓋 | SK-D07-001, SK-D07-002 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D07-001 | Interface Integration Matrix Development | 介面整合矩陣建立 | Develop the system-level interface integration matrix that c |
| SK-D07-002 | System Integration Architecture Diagram | 系統整合架構圖繪製 | System Integration Architecture Diagram design defines the c |

<!-- Phase 5 Wave 2 deepened: SK-D07-001, SK-D07-002 -->