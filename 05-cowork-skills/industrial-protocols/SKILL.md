---
name: industrial-protocols
description: >
  工業通訊協議配置。
  Configure Modbus register mapping between SCADA/RTU master stations and field devices (power meters, protection relays, switchgear controllers, energy。Configure IEC 61850 Substation Configuration Language (SCL) files and digital substation integratio
  MANDATORY TRIGGERS: 工業通訊協議配置, Modbus 映射配置, IEC 61850 SCL 配置, OPC UA 伺服器/客戶端配置, register-mapping, data-type-mapping, GOOSE, IT-OT-integration, digital-substation, industrial-IoT, polling-schedule, industrial protocols.
  Use this skill for industrial protocols tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 工業通訊協議配置

本 Skill 整合 3 個工程技能定義，提供工業通訊協議配置的完整工作流程。
適用領域：Control Systems（D05）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D01-002, SK-D01-003, SK-D02-001, SK-D02-004, SK-D02-005

---

## 1. 輸入

- Approved Data Flow Diagram and data exchange specifications (from SK-D02-004 ⏳: Data Flow Diagram Development)
- Device point lists: tag names, units, data types, ranges, update frequency requirements (from SK-D02-001 ⏳: OT Network Topology Design)
- Zone/Conduit architecture and security requirements (from SK-D01-001: Zone/Conduit Architecture Design)
- SCADA/RTU platform documentation (ModbusPlus configuration manual, Wonderware, IGS, etc.)
- Field device datasheets (meter registers, relay contact lists, inverter modbus register maps)
- Network topology and bandwidth constraints (from SK-D02-001)
- Approved protection logic and schemes (from SK-D04-004: Advanced Protection Schemes)
- IED Capability Descriptions (ICD) from device vendors (relays, merging units, bay controllers)
- System architecture and signal requirements (from SK-D02-004 ⏳: Data Flow Diagram Development)
- GOOSE signal specifications: priority, integrity checking requirements (from SK-D04-001, SK-D04-003)
- Sampled value stream requirements: current/voltage signals, reporting intervals (from SK-D04-002 ⏳: Protection Coordination Design)
- Zone/Conduit security boundaries and authentication/encryption policies (from SK-D01-001: Zone/Conduit Architecture Design)

---

## 2. 工作流程

### Step 1: Modbus 映射配置
**SK 來源**：SK-D05-009 — Modbus Mapping Configuration

執行Modbus 映射配置：Configure Modbus register mapping between SCADA/RTU master stations and field devices (power meters, protection relays, switchgear controllers, energy

**本步驟交付物**：
- Modbus Register Mapping Table (Excel/CSV): device, register address, data type (coil/discrete/holding/input), units, scaling factor, polling frequency
- Modbus Configuration Files (per SCADA platform export format): .csv, .xml, or vendor-specific format
- Modbus Address Conflict Report: verification that all addresses are unique within the system

### Step 2: IEC 61850 SCL 配置
**SK 來源**：SK-D05-010 — IEC 61850 SCL Configuration

執行IEC 61850 SCL 配置：Configure IEC 61850 Substation Configuration Language (SCL) files and digital substation integration for protection relays, merging units, SCADA serve

**本步驟交付物**：
- System Configuration Description (SCD) file (.xml per IEC 61850-5-92): complete system topology, all devices, communication bindings
- IED Configuration Files: device-specific GOOSE control blocks, sampled value streams, MMS access lists
- GOOSE Signal Assignment Table: signal ID, source device, destination device, priority, latency requirement, integrity checking method

### Step 3: OPC UA 伺服器/客戶端配置
**SK 來源**：SK-D05-011 — OPC UA Server/Client Configuration

執行OPC UA 伺服器/客戶端配置：Configure OPC UA (OLE for Process Control Unified Architecture) servers and clients for secure data exchange between IT and OT systems in industrial a

**本步驟交付物**：
- OPC UA Server Information Model Definition (.xml per OPC UA specification): object types, variables, methods, event structures
- OPC UA Endpoint Configuration Specification: endpoint URLs, security policies, user authentication methods, access control lists
- Security Policy and Certificate Management Plan: certificate hierarchy, root/intermediate/leaf certificate assignments, renewal procedures

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Modbus Register Mapping Table (Excel/CSV): device, register address, data type (coil/discrete/holding/input), units, scaling factor, polling frequency | 依需求 |
| 2 | Modbus Configuration Files (per SCADA platform export format): .csv, .xml, or vendor-specific format | 依需求 |
| 3 | Modbus Address Conflict Report: verification that all addresses are unique within the system | Markdown |
| 4 | Polling Schedule Specification: polling intervals, timeout values, retry logic, bandwidth utilization analysis | 依需求 |
| 5 | Security Implementation Checklist: confirmation that all Zone/Conduit conduit specifications are reflected in Modbus authentication/encryption configu | Markdown |
| 6 | RTU Device Configuration Scripts (if applicable): Modbus device configuration files for field equipment | 依需求 |
| 7 | System Configuration Description (SCD) file (.xml per IEC 61850-5-92): complete system topology, all devices, communication bindings | 依需求 |
| 8 | IED Configuration Files: device-specific GOOSE control blocks, sampled value streams, MMS access lists | Markdown |
| 9 | GOOSE Signal Assignment Table: signal ID, source device, destination device, priority, latency requirement, integrity checking method | 依需求 |
| 10 | Sampled Value Configuration: channel specifications, reporting intervals, quality indicators | Markdown |
| 11 | MMS Report Configuration: report control blocks, trigger conditions, buffering strategy | Markdown |
| 12 | SCL Validation Report: schema validation, consistency checks across SCD | Markdown |

---

## 4. 適用標準

- Modbus Organization: Modbus Application Protocol Specification V1.1b3
- Modbus/TCP: IEC 61158-5-104 and IEC 61784-1-5-4
- Modbus RTU: IEC 61158-2 (serial communication)
- IEC 62443-3-3: System Security Requirements — conduit-based Modbus security controls
- NIST SP 800-82 Rev. 3: Guide to OT Security — secure SCADA data exchange
- IEC 61850-5-92: Implementation guideline for the use of security — SCL security profile
- IEC 61850-5-94: Implementation Guideline for the use of IEC 61850/IEC 61869-9 for power quality measurement
- IEC 61850-7-410: Power Systems Management and Associated Information Exchange — communication for protection equipment
- IEC 61850-8-1: Communication networks and systems — GOOSE and sampled value protocols
- IEC 61869-9: Instrument transformers — digital interface for instrument transformers

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | All data points in the approved Data Flow Diagram have corresponding Modbus regi | ✅ 已驗證 |
| 2 | Register addresses are unique across all devices; no address collisions or confl | ✅ 已驗證 |
| 3 | Data type mapping (coil vs. discrete vs. holding/input register) is appropriate  | ✅ 已驗證 |
| 4 | Scaling factors (if applicable) are documented and verified to preserve measurem | ✅ 已驗證 |
| 5 | Polling frequencies are feasible for the SCADA platform and do not exceed RTU/de | ✅ 已驗證 |
| 6 | Network bandwidth utilization is within 70% of available bandwidth under peak po | ✅ 已驗證 |
| 7 | Security requirements from Zone/Conduit conduit specifications are reflected: au | ✅ 已驗證 |
| 8 | Error handling strategy (timeouts, retries, failover) is specified and consisten | ✅ 已驗證 |
| 9 | SCD file passes IEC 61850-5-92 schema validation with zero errors | ✅ 已驗證 |
| 10 | All protection logic signals (overcurrent, distance, differential, etc.) from SK | ✅ 已驗證 |
| 11 | Every GOOSE signal has a defined priority, latency requirement, and integrity ch | ✅ 已驗證 |
| 12 | Sampled value streams are configured for all required current and voltage inputs | ✅ 已驗證 |
| 13 | MMS report control blocks are configured with appropriate trigger conditions and | ✅ 已驗證 |
| 14 | Network VLAN assignments and switch timing are specified to meet GOOSE communica | ✅ 已驗證 |
| 15 | Cybersecurity parameters (encryption, authentication) in SCD match Zone/Conduit  | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D05-009 | | Junior (< 2 yr) | 5–10 person-days | Assumes 40–80 data points, straightforward 1:1 register mappi |
| SK-D05-009 | | Senior (5+ yr) | 2–4 person-days | Can optimize addresses, develop custom scaling functions, ident |
| SK-D05-010 | | Junior (< 2 yr) | 8–15 person-days | Assumes 20–40 IEDs, 50–100 GOOSE signals, single protection s |
| SK-D05-010 | | Senior (5+ yr) | 3–7 person-days | Can leverage SCL templates, optimize signal paths, resolve mult |
| SK-D05-011 | | Junior (< 2 yr) | 10–18 person-days | Assumes 50–100 data points, single OPC UA server, basic RBAC |
| SK-D05-011 | | Senior (5+ yr) | 4–8 person-days | Can design optimized information models, establish certificate  |
| SK-D05-011 | Notes: Effort scales with the number of data points and complexity of access control requirements. S |

---

## 7. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 輸入完整性 | 所有必要輸入文件已讀取並摘要 |
| 2 | 流程覆蓋 | 3 個工作步驟皆已執行並有產出 |
| 3 | 輸出完整性 | 所有交付物已產出、格式正確、非空白 |
| 4 | 標準合規 | 產出引用的標準版本正確 |
| 5 | 術語一致 | 專案術語、縮寫與 glossary 一致 |
| 6 | 跨步驟一致 | 各步驟產出間無矛盾（如數量、SL等級） |

---

## 8. 人類審核閘門

完成所有工作步驟後，暫停並向使用者提交審核：

```
工業通訊協議配置已完成。
📋 執行範圍：3 個工程步驟（SK-D05-009, SK-D05-010, SK-D05-011）
📊 交付物清單：
  - Modbus Register Mapping Table (Excel/CSV): device, register address, data type (coil/discrete/holding/input), units, scaling factor, polling frequency
  - Modbus Configuration Files (per SCADA platform export format): .csv, .xml, or vendor-specific format
  - Modbus Address Conflict Report: verification that all addresses are unique within the system
  - Polling Schedule Specification: polling intervals, timeout values, retry logic, bandwidth utilization analysis
  - Security Implementation Checklist: confirmation that all Zone/Conduit conduit specifications are reflected in Modbus authentication/encryption configu
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
| SK 覆蓋 | SK-D05-009, SK-D05-010, SK-D05-011 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D05-009 | Modbus Mapping Configuration | Modbus 映射配置 | Configure Modbus register mapping between SCADA/RTU master s |
| SK-D05-010 | IEC 61850 SCL Configuration | IEC 61850 SCL 配置 | Configure IEC 61850 Substation Configuration Language (SCL)  |
| SK-D05-011 | OPC UA Server/Client Configuration | OPC UA 伺服器/客戶端配置 | Configure OPC UA (OLE for Process Control Unified Architectu |

<!-- Phase 5 Wave 2 deepened: SK-D05-009, SK-D05-010, SK-D05-011 -->