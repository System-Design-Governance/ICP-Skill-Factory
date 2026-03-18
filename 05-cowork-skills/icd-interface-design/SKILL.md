---
name: icd-interface-design
description: >
  介面控制文件與通訊協定。
  Develop Interface Control Documents (ICDs) that define the technical interfaces between systems, subsystems, and external entities. An ICD is a formal。**Example: Utility SCADA System Protocol Architecture**
  MANDATORY TRIGGERS: 工業協定架構設計, 介面控制文件與通訊協定, 介面控制文件撰寫, system-integration, data-format, interface-control, IEC-62443, Interface Control Document (ICD) Development, protocol-specification, ICD, icd interface design.
  Use this skill for icd interface design tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 介面控制文件與通訊協定

本 Skill 整合 2 個工程技能定義，提供介面控制文件與通訊協定的完整工作流程。
適用領域：System Architecture（D02）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D01-010, SK-D02-001, SK-D02-004, SK-D02-010, SK-D02-011

---

## 1. 輸入

- Approved Network and Data Flow Diagrams (from SK-D02-004 ⏳: Data Flow Diagram Development; per ID01 §7.3.12)
- System Architecture Design (from SK-D01-001: Zone/Conduit Architecture Design and SK-D02-001: System Partitioning and Functional Architecture)
- Requirements Specification Document (functional and non-functional requirements for each subsystem)
- Protocol Standards and Technology Constraints (customer-approved technologies, legacy system interface requirements)
- Integration Plan (from SK-D02-010 ⏳: Integration Testing Plan Development)
- Security Requirements per Interface (from SK-D01-010 ⏳: Security Level Target Assessment and conduit specifications)

---

## 2. 工作流程

### Step 1: 介面控制文件撰寫
**SK 來源**：SK-D02-003 — Interface Control Document (ICD) Development

執行介面控制文件撰寫：Develop Interface Control Documents (ICDs) that define the technical interfaces between systems, subsystems, and external entities. An ICD is a formal

**本步驟交付物**：
- Interface Control Document (formal specification document, per ID01 §7.4.1 and Annex A.10)
- One ICD per interface; consolidated registry of all interfaces
- Fields per interface: Interface ID, Source System, Destination System, Protocol, Data Format, Timing Requirements, Authentication/Authorization, Error

### Step 2: 工業協定架構設計
**SK 來源**：SK-D02-005 — Industrial Protocol Architecture Design

執行工業協定架構設計：**Example: Utility SCADA System Protocol Architecture**

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Interface Control Document (formal specification document, per ID01 §7.4.1 and Annex A.10) | 依需求 |
| 2 | One ICD per interface; consolidated registry of all interfaces | 依需求 |
| 3 | Fields per interface: Interface ID, Source System, Destination System, Protocol, Data Format, Timing Requirements, Authentication/Authorization, Error | 依需求 |
| 4 | Interface Data Dictionary (detailed field-by-field specification for each message/data exchange) | 依需求 |
| 5 | Protocol Stack Diagram (visual representation of protocol layers per interface) | 依需求 |
| 6 | Integration Assumption and Constraint Document (compatibility, version management, legacy system mappings) | 依需求 |

---

## 4. 適用標準

- IEC 62443-3-2: Security Risk Assessment for System Design — interface security requirements allocation
- IEC 62443-3-3: System Security Requirements and Security Levels — security properties per interface
- IEC 62443-4-1: Product Development — secure design of interfaces and communication mechanisms
- IEEE 1220: Application and Management of the Systems Engineering Design Process — interface control document standard
- NERC CIP Reliability Standard (supplementary): Critical facility interface requirements documentation
- IEC 62443-3-3 (Secure Design):** Protocol architecture must support security zones and conduits; protocol selection must
- Functional Safety (IEC 61511, IEC 61508):** Safety-critical communication requires protocols with appropriate SIL/ASIL c
- Industry Standards:** Oil & gas (API 1164), power (NERC CIP, IEC 60870-5-104), water (IEC 60870-5-103) may mandate speci
- Data Privacy (GDPR, CCPA):** If protocol carries personal data, encryption and audit logging are mandatory compliance re

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | All system-to-system and system-to-external interfaces identified in the approve | ✅ 已驗證 |
| 2 | Each ICD entry specifies: Interface ID, Source System, Destination System, Proto | ✅ 已驗證 |
| 3 | Data format specifications are complete: field names, data types, units, valid v | ✅ 已驗證 |
| 4 | All interfaces with security requirements have explicit authentication, authoriz | ✅ 已驗證 |
| 5 | ICD document is traceable to the system requirements specification; every interf | ✅ 已驗證 |
| 6 | ICDs have been reviewed and approved by SYS and PE/O; all review findings are do | ✅ 已驗證 |
| 7 | Protocol allocation matrix assigns a primary protocol to each communication path | ✅ 已驗證 |
| 8 | Protocol selection justification document provides rationale for each selection  | ✅ 已驗證 |
| 9 | Interoperability assessment identifies all protocol translation points and speci | ✅ 已驗證 |
| 10 | Security properties table documents, for each protocol: native encryption suppor | ✅ 已驗證 |
| 11 | Migration plan specifies timeline for legacy protocol replacement with specific  | ✅ 已驗證 |
| 12 | Protocol performance requirements document maps latency, throughput, and reliabi | ✅ 已驗證 |
| 13 | Vendor analysis table summarizes, for each selected protocol and vendor: support | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D02-003 | | Junior (< 2 yr) | 5–8 person-days | Assumes 8–12 interfaces, standard protocols; includes document |
| SK-D02-003 | | Senior (5+ yr) | 2–3 person-days | Same scope; leverages protocol templates and prior ICD experien |

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
介面控制文件與通訊協定已完成。
📋 執行範圍：2 個工程步驟（SK-D02-003, SK-D02-005）
📊 交付物清單：
  - Interface Control Document (formal specification document, per ID01 §7.4.1 and Annex A.10)
  - One ICD per interface; consolidated registry of all interfaces
  - Fields per interface: Interface ID, Source System, Destination System, Protocol, Data Format, Timing Requirements, Authentication/Authorization, Error
  - Interface Data Dictionary (detailed field-by-field specification for each message/data exchange)
  - Protocol Stack Diagram (visual representation of protocol layers per interface)
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
| Domain | D02 (System Architecture) |
| SK 覆蓋 | SK-D02-003, SK-D02-005 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D02-003 | Interface Control Document (ICD) Development | 介面控制文件撰寫 | Develop Interface Control Documents (ICDs) that define the t |
| SK-D02-005 | Industrial Protocol Architecture Design | 工業協定架構設計 | **Example: Utility SCADA System Protocol Architecture** |

<!-- Phase 5 Wave 2 deepened: SK-D02-003, SK-D02-005 -->