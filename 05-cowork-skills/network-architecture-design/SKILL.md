---
name: network-architecture-design
description: >
  網路架構設計。
  Design network redundancy architecture for OT networks to meet operational availability requirements while integrating with Zone/Conduit security arch。Design high-availability (HA) architecture for operational technology (OT) and industrial control s
  MANDATORY TRIGGERS: 高可用架構設計, 網路冗餘設計, 網路架構設計, RTO/RPO 規劃, rstp, OT-systems, network-availability, IEC-62443, High-Availability Architecture Design, business-continuity, dual-homing, RTO/RPO Planning.
  Use this skill for network architecture design tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 網路架構設計

本 Skill 整合 3 個工程技能定義，提供網路架構設計的完整工作流程。
適用領域：System Architecture（D02）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D01-003, SK-D01-006, SK-D01-010, SK-D01-022, SK-D02-001

---

## 1. 輸入

- Approved Zone/Conduit Architecture Design with network segmentation policy (from SK-D01-001)
- OT Network Topology Design (physical and logical) with identified critical segments (from SK-D02-001 ⏳)
- Asset Inventory Register with network connectivity and criticality (from SK-D01-005 ⏳)
- Operational Availability Requirements specification: acceptable downtime (RTO), recovery time objective (RPO) per network segment or subsystem
- Firewall architecture and device placement (from SK-D01-003 ⏳: Firewall Rule Planning)
- Existing redundancy infrastructure (if brownfield: current switches, links, protocol configuration)
- System Architecture Design (from SK-D02-001: System Partitioning and Functional Architecture)
- Zone/Conduit Architecture Design (from SK-D01-001: Zone/Conduit Architecture Design)
- Operational Requirements and SLAs (Availability targets, MTBF/MTTR requirements, tolerable outage windows)
- Infrastructure Constraints (physical site layout, network topology, power distribution, environmental conditions)
- Business Continuity Requirements (from customer SOW or SLAs)
- Threat and Risk Assessment (from SK-D01-006 ⏳: Threat and Risk Assessment — Preliminary; common-cause failure modes)

---

## 2. 工作流程

### Step 1: 網路冗餘設計
**SK 來源**：SK-D02-002 — Network Redundancy Design

執行網路冗餘設計：Design network redundancy architecture for OT networks to meet operational availability requirements while integrating with Zone/Conduit security arch

**本步驟交付物**：
- Network Redundancy Architecture Specification: chosen redundancy topology (RSTP mesh, ring, dual-homing), technology rationale (why RSTP vs. ring topo
- Redundancy Topology Diagram: network topology with redundant links highlighted, link costs/priorities indicated, root bridge/ring supervisor placement
- Failover Timing and Recovery Plan: calculated failover time for each critical redundancy path, convergence validation criteria, and timing test proced

### Step 2: 高可用架構設計
**SK 來源**：SK-D02-006 — High-Availability Architecture Design

執行高可用架構設計：Design high-availability (HA) architecture for operational technology (OT) and industrial control systems (ICS) to ensure service continuity in the fa

**本步驟交付物**：
- High-Availability Architecture Diagram (D2 / Visio format)
- Logical architecture showing redundancy relationships
- Physical site layout showing standby resource locations

### Step 3: RTO/RPO 規劃
**SK 來源**：SK-D02-007 — RTO/RPO Planning

執行RTO/RPO 規劃：Define Recovery Time Objective (RTO) and Recovery Point Objective (RPO) targets for each system tier and critical service, and design the backup and r

**本步驟交付物**：
- RTO/RPO Target Matrix (table format)
- Rows: each system tier / critical service
- Columns: Service Name, Business Criticality (H/M/L), RTO Target (hours/minutes), RPO Target (hours/minutes), Rationale

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Network Redundancy Architecture Specification: chosen redundancy topology (RSTP mesh, ring, dual-homing), technology rationale (why RSTP vs. ring topo | 依需求 |
| 2 | Redundancy Topology Diagram: network topology with redundant links highlighted, link costs/priorities indicated, root bridge/ring supervisor placement | 依需求 |
| 3 | Failover Timing and Recovery Plan: calculated failover time for each critical redundancy path, convergence validation criteria, and timing test proced | 依需求 |
| 4 | VLAN/Zone Compatibility Analysis: verification that redundant links do not create unintended communication paths between security zones, and confirmat | 依需求 |
| 5 | Redundancy Configuration Template: switch/router configuration snippets for RSTP priority, ring supervisor setup, dual-homing interface configuration, | 依需求 |
| 6 | Operational Handover Procedure: runbook for network operators describing redundancy monitoring, failover expectations, and manual intervention trigger | 依需求 |
| 7 | High-Availability Architecture Diagram (D2 / Visio format) | 依需求 |
| 8 | Logical architecture showing redundancy relationships | 依需求 |
| 9 | Physical site layout showing standby resource locations | 依需求 |
| 10 | HA Configuration Specification Document with sections for: | 依需求 |
| 11 | Server/System Redundancy Model (active/active, active/passive, N+1, N+M) | 依需求 |
| 12 | Database Replication Strategy (synchronous, asynchronous, failover trigger conditions) | 依需求 |

---

## 4. 適用標準

- IEC 62443-3-2: Security Risk Assessment — network availability as resilience requirement
- IEC 62443-3-3: System Security Requirements and Security Levels — SL-specific availability requirements
- IEEE 802.1D-2004: Media Access Control (MAC) Bridges — Spanning Tree Protocol (STP/RSTP foundation)
- IEC 61850-90-13: Communication systems and devices for power utility automation — RSTP guidance for power systems (suppl
- NIST SP 800-82 Rev. 3: Guide to OT Security — network redundancy best practices for critical infrastructure (supplementa
- IEC 62443-3-2: Security Risk Assessment for System Design — HA architecture risk considerations
- IEC 62443-3-3: System Security Requirements and Security Levels — availability as a security property; SL-T per system t
- NIST SP 800-82 Rev. 3: Guide to OT Security — network redundancy and resilience guidance
- IEEE 1366: Standard Guide for Reliability Measurement of Electric Power Delivery Systems — availability metrics and defi
- IEC 62443-3-2: Security Risk Assessment for System Design — recovery objectives as part of security requirements

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Chosen redundancy mechanism (RSTP, ring, dual-homing) is justified with explicit | ✅ 已驗證 |
| 2 | Redundancy topology diagram shows all redundant links with root bridge/ring supe | ✅ 已驗證 |
| 3 | Failover timing requirement is specified for each critical segment (in milliseco | ✅ 已驗證 |
| 4 | VLAN/zone compatibility analysis confirms that redundant links do not bypass fir | ✅ 已驗證 |
| 5 | Failover recovery procedure is documented with convergence validation criteria a | ✅ 已驗證 |
| 6 | Configuration template covers all devices involved in redundancy (switches, rout | ✅ 已驗證 |
| 7 | Operational handover procedure is prepared for network operations team with runb | ✅ 已驗證 |
| 8 | HA architecture design covers all system tiers and critical services identified  | ✅ 已驗證 |
| 9 | Each system tier has an assigned redundancy model (hot/warm/cold standby) with d | ✅ 已驗證 |
| 10 | Failover procedures are fully specified: health check intervals, failure detecti | ✅ 已驗證 |
| 11 | HA mechanisms (database replication, network synchronization) have explicit secu | ✅ 已驗證 |
| 12 | Architecture is traceable to the operational requirements specification: each av | ✅ 已驗證 |
| 13 | HA design has been reviewed for consistency with the Zone/Conduit Architecture;  | ✅ 已驗證 |
| 14 | Design has been reviewed and approved by SYS, INF, and PE/O | ✅ 已驗證 |
| 15 | All system tiers and critical services identified in the system architecture hav | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D02-002 | | Junior (< 2 yr) | 6–10 person-days | Assumes standard RSTP topology, ~10 redundant links; includes |
| SK-D02-002 | | Senior (5+ yr) | 3–6 person-days | Same scope; senior leverages RSTP knowledge and vendor tool fam |
| SK-D02-002 | Notes: Complex multi-protocol redundancy (RSTP + ring hybrid, customer-specific availability targets |
| SK-D02-006 | | Junior (< 2 yr) | 6–10 person-days | Assumes single-site system, 3–4 system tiers, standard redund |
| SK-D02-006 | | Senior (5+ yr) | 3–4 person-days | Same scope; leverages prior HA patterns and vendor knowledge | |
| SK-D02-007 | | Junior (< 2 yr) | 5–8 person-days | Assumes 4–6 system tiers, standard backup strategies; includes |
| SK-D02-007 | | Senior (5+ yr) | 2–3 person-days | Same scope; leverages prior RTO/RPO experience and backup strat |
| SK-D02-007 | Notes: Complex multi-tier systems with inter-service recovery dependencies may require 1.5–2× effort |

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
網路架構設計已完成。
📋 執行範圍：3 個工程步驟（SK-D02-002, SK-D02-006, SK-D02-007）
📊 交付物清單：
  - Network Redundancy Architecture Specification: chosen redundancy topology (RSTP mesh, ring, dual-homing), technology rationale (why RSTP vs. ring topo
  - Redundancy Topology Diagram: network topology with redundant links highlighted, link costs/priorities indicated, root bridge/ring supervisor placement
  - Failover Timing and Recovery Plan: calculated failover time for each critical redundancy path, convergence validation criteria, and timing test proced
  - VLAN/Zone Compatibility Analysis: verification that redundant links do not create unintended communication paths between security zones, and confirmat
  - Redundancy Configuration Template: switch/router configuration snippets for RSTP priority, ring supervisor setup, dual-homing interface configuration,
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
| SK 覆蓋 | SK-D02-002, SK-D02-006, SK-D02-007 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D02-002 | Network Redundancy Design | 網路冗餘設計 | Design network redundancy architecture for OT networks to me |
| SK-D02-006 | High-Availability Architecture Design | 高可用架構設計 | Design high-availability (HA) architecture for operational t |
| SK-D02-007 | RTO/RPO Planning | RTO/RPO 規劃 | Define Recovery Time Objective (RTO) and Recovery Point Obje |

<!-- Phase 5 Wave 2 deepened: SK-D02-002, SK-D02-006, SK-D02-007 -->