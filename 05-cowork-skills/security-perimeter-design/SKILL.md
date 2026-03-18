---
name: security-perimeter-design
description: >
  安全邊界設計。
  Translate the approved Zone/Conduit Architecture (SK-D01-001) into a detailed set of firewall rules and access control lists (ACLs) that enforce inter。Compile and integrate all network segmentation implementation artifacts into a comprehensive, verif
  MANDATORY TRIGGERS: 安全邊界設計, 網路分段文件, 防火牆規則規劃, access-control, Network Segmentation Documentation, zone-conduit, IEC-62443, verification, network-segmentation, security perimeter design, documentation.
  Use this skill for security perimeter design tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 安全邊界設計

本 Skill 整合 2 個工程技能定義，提供安全邊界設計的完整工作流程。
適用領域：OT Cybersecurity（D01）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D01-005, SK-D01-010, SK-D02-001, SK-D02-004

---

## 1. 輸入

- Approved Zone/Conduit Architecture Diagram (from SK-D01-001: Zone/Conduit Architecture Design)
- Conduit Specification Table: source zone → destination zone, allowed protocols, direction, authentication requirements (from SK-D01-001)
- Asset Inventory Register with IP/MAC addresses and zone assignments (from SK-D01-005 ⏳: Asset Inventory Development)
- Data Flow Diagram showing inter-asset communication flows (from SK-D02-004 ⏳: Data Flow Diagram Development)
- Firewall device specifications and available rule formats (e.g., Palo Alto Networks, Fortinet, Cisco ASA)
- Customer security policy and exception procedures
- Approved Zone/Conduit Architecture Diagram and documentation (from SK-D01-001)
- Detailed Firewall Rule Specification and priority matrix (from SK-D01-003 ⏳)
- VLAN assignment table: VLAN ID, VLAN name, zone membership, IP subnet, routing scope
- Network ACL specifications (router/switch-level access control lists)
- Physical network topology diagram with device locations and interconnections (from SK-D02-001 ⏳)
- Logical network topology diagram showing zone boundaries and inter-zone conduits

---

## 2. 工作流程

### Step 1: 防火牆規則規劃
**SK 來源**：SK-D01-003 — Firewall Rule Planning

執行防火牆規則規劃：Translate the approved Zone/Conduit Architecture (SK-D01-001) into a detailed set of firewall rules and access control lists (ACLs) that enforce inter

**本步驟交付物**：
- Detailed Firewall Rule Specification Table: rule ID, source zone/IP (or subnet), destination zone/IP (or subnet), protocol, port(s), action (allow/den
- Firewall Rule Priority/Order Documentation: rule precedence and conflicts resolution matrix
- Denial/Exception Log: any requested rules denied by security policy, with documented rationale and approval

### Step 2: 網路分段文件
**SK 來源**：SK-D01-004 — Network Segmentation Documentation

執行網路分段文件：Compile and integrate all network segmentation implementation artifacts into a comprehensive, verification-ready documentation package that demonstrat

**本步驟交付物**：
- Network Segmentation Functional Design Specification: comprehensive narrative document covering zone definitions, conduit policies, firewall rule stra
- Network Segmentation Design Verification Package: evidence matrix linking each design requirement (from ID02 Annex C.3) to implemented control, with s
- Integrated Zone/Conduit Architecture Diagram with VLAN overlay: zones, conduits, firewall devices, key IP subnets labeled

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Detailed Firewall Rule Specification Table: rule ID, source zone/IP (or subnet), destination zone/IP (or subnet), protocol, port(s), action (allow/den | 依需求 |
| 2 | Firewall Rule Priority/Order Documentation: rule precedence and conflicts resolution matrix | Markdown |
| 3 | Denial/Exception Log: any requested rules denied by security policy, with documented rationale and approval | 依需求 |
| 4 | Firewall Configuration Narrative Document: section within Security Implementation Specification (per ID02 Annex A.9 §10.1) | 依需求 |
| 5 | Rule Testing Plan: test cases for verification that rules enforce intended communication paths and block unintended paths (per ID02 C.3 design verific | 依需求 |
| 6 | Network Segmentation Functional Design Specification: comprehensive narrative document covering zone definitions, conduit policies, firewall rule stra | 依需求 |
| 7 | Network Segmentation Design Verification Package: evidence matrix linking each design requirement (from ID02 Annex C.3) to implemented control, with s | Markdown |
| 8 | Integrated Zone/Conduit Architecture Diagram with VLAN overlay: zones, conduits, firewall devices, key IP subnets labeled | 依需求 |
| 9 | Master Device Configuration Reference Table: device ID, device type, interface VLAN assignments, relevant rules/ACLs, firmware/software version | 依需求 |
| 10 | Network Segmentation Change Management Procedure: process for requesting, approving, and documenting changes to firewall rules, VLANs, and ACLs in pro | 依需求 |
| 11 | Operational Handover Package: network segmentation summary for network operations and help desk (condensed, training-suitable version) | 依需求 |

---

## 4. 適用標準

- IEC 62443-3-2: Security Risk Assessment — firewall rule design as implementation of zone/conduit policies
- IEC 62443-3-3: System Security Requirements and Security Levels — SL-specific access control enforcement
- ID02 Annex A.9 §10.1: Network security device configuration and rule documentation standards
- NIST SP 800-82 Rev. 3: OT Security — firewall best practices for industrial networks (supplementary)
- IEC 62443-3-3: System Security Requirements and Security Levels — network segmentation as security requirement fulfilmen
- ID01 §7.4.1.2: Network segmentation implementation documentation standards and scope
- ID02 Annex C.3: Design Verification Checklist — completeness criteria and evidence matrix for network segmentation
- ID02 Annex A.9 §10.1: Network security documentation and implementation standards
- NIST SP 800-82 Rev. 3: OT Security — network segmentation best practices (supplementary)

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Every allowed communication path defined in the approved Conduit Specification T | ✅ 已驗證 |
| 2 | Every rule specifies: source (IP/zone), destination (IP/zone), protocol, port, a | ✅ 已驗證 |
| 3 | No overlapping or conflicting rules exist (conflicts identified and resolved wit | ✅ 已驗證 |
| 4 | Denial/exception log documents all requested rules that were denied by policy, w | ✅ 已驗證 |
| 5 | Rule specification covers both unicast and any broadcast/multicast communication | ✅ 已驗證 |
| 6 | All rules include default-deny catch-all rules at the end of each direction to e | ✅ 已驗證 |
| 7 | Rule testing plan is complete and traceability to zone/conduit architecture is b | ✅ 已驗證 |
| 8 | Network Segmentation Design Specification covers all zones and conduits with cle | ✅ 已驗證 |
| 9 | Design Verification Package (ID02 C.3 checklist) shows evidence for 100% of appl | ✅ 已驗證 |
| 10 | Integrated Zone/Conduit/VLAN diagram clearly shows all zones, inter-zone conduit | ✅ 已驗證 |
| 11 | Master Device Configuration Reference Table covers all relevant network security | ✅ 已驗證 |
| 12 | Change Management Procedure is documented and approved by operations team before | ✅ 已驗證 |
| 13 | Operational Handover Package is prepared in condensed, training-suitable format  | ✅ 已驗證 |
| 14 | All documentation is reviewed and signed off by SAC and PE/O, with approval date | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D01-003 | | Junior (< 2 yr) | 6–10 person-days | Assumes ~30 conduits, standard protocols; includes rule speci |
| SK-D01-003 | | Senior (5+ yr) | 3–5 person-days | Same scope; senior leverages firewall vendor knowledge and patt |
| SK-D01-004 | | Junior (< 2 yr) | 10–16 person-days | Assumes ~30 conduits, 5–8 zones, 2 major firewall devices; i |
| SK-D01-004 | | Senior (5+ yr) | 5–8 person-days | Same scope; senior leverages template systems and efficient doc |

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
安全邊界設計已完成。
📋 執行範圍：2 個工程步驟（SK-D01-003, SK-D01-004）
📊 交付物清單：
  - Detailed Firewall Rule Specification Table: rule ID, source zone/IP (or subnet), destination zone/IP (or subnet), protocol, port(s), action (allow/den
  - Firewall Rule Priority/Order Documentation: rule precedence and conflicts resolution matrix
  - Denial/Exception Log: any requested rules denied by security policy, with documented rationale and approval
  - Firewall Configuration Narrative Document: section within Security Implementation Specification (per ID02 Annex A.9 §10.1)
  - Rule Testing Plan: test cases for verification that rules enforce intended communication paths and block unintended paths (per ID02 C.3 design verific
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
| Domain | D01 (OT Cybersecurity) |
| SK 覆蓋 | SK-D01-003, SK-D01-004 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D01-003 | Firewall Rule Planning | 防火牆規則規劃 | Translate the approved Zone/Conduit Architecture (SK-D01-001 |
| SK-D01-004 | Network Segmentation Documentation | 網路分段文件 | Compile and integrate all network segmentation implementatio |

<!-- Phase 5 Wave 2 deepened: SK-D01-003, SK-D01-004 -->