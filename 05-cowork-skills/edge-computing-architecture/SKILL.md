---
name: edge-computing-architecture
description: >
  邊緣計算與架構決策。
  Design edge computing deployment architecture for operational technology (OT) environments, placing computational resources and data processing logic 。Supersedes ADR-20250601-data-integration-strategy (CSV export approach)。**Example: Industrial Firew
  MANDATORY TRIGGERS: 技術選型評估, 架構決策記錄撰寫, 邊緣計算部署設計, 架構審查主持, 邊緣計算與架構決策, edge-computing, fog-computing, IEC-62443, Architecture Review Facilitation, quality-assurance, design-review, Technology Selection Evaluation, edge computing architecture.
  Use this skill for edge computing architecture tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 邊緣計算與架構決策

本 Skill 整合 4 個工程技能定義，提供邊緣計算與架構決策的完整工作流程。
適用領域：System Architecture（D02）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D01-006, SK-D01-024, SK-D02-001, SK-D02-003, SK-D02-004

---

## 1. 輸入

- System Architecture Design (from SK-D02-001: System Partitioning and Functional Architecture)
- Zone/Conduit Architecture Design (from SK-D01-001: Zone/Conduit Architecture Design)
- Data Flow Diagram (from SK-D02-004 ⏳: Data Flow Diagram Development)
- Real-Time Processing Requirements (latency targets, throughput requirements, processing complexity per data stream)
- Network Topology and Available Bandwidth (site locations, network link capacities, latency between sites and central facility)
- Existing SCADA/EMS System Architecture (legacy system constraints, protocol compatibility requirements)
- System Architecture Design Documents (outputs from architecture design skills: SK-D02-001, SK-D02-003, SK-D02-006, SK-D02-007, SK-D02-008, etc.)
- System Requirements Specification (functional and non-functional requirements that the architecture must satisfy)
- Preliminary Risk and Threat Assessment (from SK-D01-006 ⏳: Threat and Risk Assessment — Preliminary)
- Project Schedule and Resource Plan (to coordinate review scheduling)
- Organization's Architecture Review Procedure Documentation (review criteria, reviewer qualifications, escalation procedures)

---

## 2. 工作流程

### Step 1: 邊緣計算部署設計
**SK 來源**：SK-D02-008 — Edge Computing Deployment Design

執行邊緣計算部署設計：Design edge computing deployment architecture for operational technology (OT) environments, placing computational resources and data processing logic 

**本步驟交付物**：
- Edge Computing Architecture Diagram (D2 / Visio format)
- Physical site layout showing edge node locations
- Logical architecture showing edge-to-cloud communication paths

### Step 2: 架構決策記錄撰寫
**SK 來源**：SK-D02-009 — Architecture Decision Record (ADR) Writing

執行架構決策記錄撰寫：Supersedes ADR-20250601-data-integration-strategy (CSV export approach)

### Step 3: 技術選型評估
**SK 來源**：SK-D02-010 — Technology Selection Evaluation

執行技術選型評估：**Example: Industrial Firewall Selection for Manufacturing Plant**

### Step 4: 架構審查主持
**SK 來源**：SK-D02-012 — Architecture Review Facilitation

執行架構審查主持：Facilitate formal architecture review sessions per IEC 62443-3-2 and the ICP procedures document (ID01 §7.3.2), ensuring that system architecture desi

**本步驟交付物**：
- Architecture Review Session Minutes (documented record of the review)
- Review date, attendees, architecture design elements reviewed
- Review questions asked and design team responses

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Edge Computing Architecture Diagram (D2 / Visio format) | 依需求 |
| 2 | Physical site layout showing edge node locations | 依需求 |
| 3 | Logical architecture showing edge-to-cloud communication paths | 依需求 |
| 4 | Data processing pipeline showing filtering/aggregation at edge and central facility | 依需求 |
| 5 | Edge Node Specification Document | 依需求 |
| 6 | Edge node placement strategy: which data sources have co-located edge nodes vs. regional aggregation points | 依需求 |
| 7 | Architecture Review Session Minutes (documented record of the review) | 依需求 |
| 8 | Review date, attendees, architecture design elements reviewed | 依需求 |
| 9 | Review questions asked and design team responses | 依需求 |
| 10 | Findings: deficiencies, risks, or inconsistencies identified | 依需求 |
| 11 | Findings and Observations Report (detailed analysis of review findings) | Markdown |
| 12 | Categorization: Critical (must be resolved before design approval), Major (significant risk or inconsistency), Minor (improvement suggestion) | 依需求 |

---

## 4. 適用標準

- IEC 62443-3-2: Security Risk Assessment for System Design — edge computing architecture security risks
- IEC 62443-3-3: System Security Requirements and Security Levels — edge node security classification
- IEC 62443-4-2: Product Cybersecurity Competencies and Responsibilities — edge computing product security requirements
- IEC 61850: Communication networks and systems for power utility automation — OT protocol standards and integration
- MQTT v3.1.1 / v5.0: Standard protocol for edge-to-cloud messaging
- OPC UA Specification: Industrial automation interoperability standard
- IEC 62443-1-1 Governance:** Design decisions subject to change control and architecture review are documented via ADRs a
- Design Traceability:** ADRs provide traceability from requirements to design rationale, supporting compliance audits.
- Regulatory Evidence:** For regulated industries, ADRs provide documented evidence of reasoned decision-making during des
- Design Change Control:** ADRs identify superseded decisions and provide change impact analysis, supporting change contro

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Edge node placement strategy is justified: for each edge node location, document | ✅ 已驗證 |
| 2 | Local processing logic is specified to sufficient detail that it can be implemen | ✅ 已驗證 |
| 3 | Edge-to-cloud communication is fully specified: protocol, message format, freque | ✅ 已驗證 |
| 4 | All edge-to-cloud interfaces have been added to the Zone/Conduit Architecture or | ✅ 已驗證 |
| 5 | Edge node security architecture is complete: authentication/authorization mechan | ✅ 已驗證 |
| 6 | Offline resilience procedures are documented: local data buffering capacity, ret | ✅ 已驗證 |
| 7 | Integration with existing SCADA/EMS systems is validated: compatibility with leg | ✅ 已驗證 |
| 8 | Edge computing architecture has been reviewed and approved by SYS, STC, INF, and | ✅ 已驗證 |
| 9 | ADR title concisely describes the decision (e.g., "Use OPC UA for Plant-to-Enter | ✅ 已驗證 |
| 10 | Context section identifies business drivers, technical constraints, and regulato | ✅ 已驗證 |
| 11 | Decision statement specifies the chosen approach, scope, and key implementation  | ✅ 已驗證 |
| 12 | Consequences section identifies at least three positive and two negative consequ | ✅ 已驗證 |
| 13 | Alternatives section describes at least two viable alternatives with documented  | ✅ 已驗證 |
| 14 | Rationale section provides evidence-based justification (cost comparison, perfor | ✅ 已驗證 |
| 15 | ADR status and date are specified; if superseding a prior ADR, reference the pri | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D02-008 | | Junior (< 2 yr) | 7–12 person-days | Assumes 3–5 edge node locations, standard MQTT/OPC UA protoco |
| SK-D02-008 | | Senior (5+ yr) | 3–5 person-days | Same scope; leverages edge computing patterns and protocol expe |
| SK-D02-008 | Notes: Designs with legacy SCADA/EMS systems requiring custom protocol bridges may require 1.5–2× ef |
| SK-D02-012 | | Junior (< 2 yr) | 2–4 person-days | Assumes single architecture design scope (e.g., one skill outp |
| SK-D02-012 | | Senior (5+ yr) | 1–2 person-days | Same scope; leverages prior review experience and understanding |
| SK-D02-012 | Notes: Comprehensive architecture reviews covering multiple design skills (5+ outputs) may require 3 |

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
邊緣計算與架構決策已完成。
📋 執行範圍：4 個工程步驟（SK-D02-008, SK-D02-009, SK-D02-010, SK-D02-012）
📊 交付物清單：
  - Edge Computing Architecture Diagram (D2 / Visio format)
  - Physical site layout showing edge node locations
  - Logical architecture showing edge-to-cloud communication paths
  - Data processing pipeline showing filtering/aggregation at edge and central facility
  - Edge Node Specification Document
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
| SK 覆蓋 | SK-D02-008, SK-D02-009, SK-D02-010, SK-D02-012 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D02-008 | Edge Computing Deployment Design | 邊緣計算部署設計 | Design edge computing deployment architecture for operationa |
| SK-D02-009 | Architecture Decision Record (ADR) Writing | 架構決策記錄撰寫 | Supersedes ADR-20250601-data-integration-strategy (CSV expor |
| SK-D02-010 | Technology Selection Evaluation | 技術選型評估 | **Example: Industrial Firewall Selection for Manufacturing P |
| SK-D02-012 | Architecture Review Facilitation | 架構審查主持 | Facilitate formal architecture review sessions per IEC 62443 |

<!-- Phase 5 Wave 2 deepened: SK-D02-008, SK-D02-009, SK-D02-010, SK-D02-012 -->