---
name: sis-security-control
description: >
  安全儀控系統實施。
  Design and implement cybersecurity controls for Safety Instrumented Systems (SIS) that enforce IEC 62443 security requirements while preserving the Sa
  MANDATORY TRIGGERS: 安全儀控系統實施, SIS 安全控制實施, IEC-61511, access-control, IEC-62443, safety-security, functional-safety, network-isolation, SIS Security Control Implementation, sis.
  Use this skill for sis security control tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 安全儀控系統實施

本 Skill 整合 1 個工程技能定義，提供安全儀控系統實施的完整工作流程。
適用領域：OT Cybersecurity（D01）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D01-003, SK-D01-007, SK-D01-010

---

## 1. 輸入

- Approved SIS System Architecture (safety system P&ID, functional safety block diagrams from IEC 61511 engineering phase)
- SIS Safety Requirements Specification (SIL targets per IEC 61511 Annex B)
- Zone/Conduit Architecture Design with SIS zone definition (from SK-D01-001, where SIS is designated as a dedicated high-SL zone)
- IEC 62443 Security Requirements for the SIS zone (SL-T assignment, from SK-D01-007 ⏳)
- Existing SIS network topology, communication protocols, and device list (HMI, PLC, RTU, I/O modules, operator interfaces)
- Safety-critical network communication requirements: latency bounds, reliability requirements, diagnostic message frequencies

---

## 2. 工作流程

### Step 1: SIS 安全控制實施
**SK 來源**：SK-D01-027 — SIS Security Control Implementation

執行SIS 安全控制實施：Design and implement cybersecurity controls for Safety Instrumented Systems (SIS) that enforce IEC 62443 security requirements while preserving the Sa

**本步驟交付物**：
- SIS Security Architecture Specification: dedicated network segmentation for SIS, isolation mechanisms (air gap, demilitarized zone, application-level 
- SIS Network Isolation Design: network topology with firewall rules separating SIS from non-safety OT and IT networks, conduit specifications for SIS-t
- SIS Change Management Procedure: change process for SIS security controls, including change impact assessment for functional safety, SIL re-validation

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | SIS Security Architecture Specification: dedicated network segmentation for SIS, isolation mechanisms (air gap, demilitarized zone, application-level  | 依需求 |
| 2 | SIS Network Isolation Design: network topology with firewall rules separating SIS from non-safety OT and IT networks, conduit specifications for SIS-t | 依需求 |
| 3 | SIS Change Management Procedure: change process for SIS security controls, including change impact assessment for functional safety, SIL re-validation | 依需求 |
| 4 | Security-Safety Conflict Resolution Log: documented cases where security requirements and safety requirements compete, the chosen resolution (security | 依需求 |
| 5 | SIS Cybersecurity Assessment Report: mapping of IEC 62443 security requirements to SIS control implementation, verification that SIL certification is  | Markdown |
| 6 | SIS Operator Training Plan: administrative access control, authentication procedures, and security awareness training with explicit coverage of safety | 依需求 |

---

## 4. 適用標準

- IEC 62443-3-3: System Security Requirements and Security Levels — SIS security requirements
- IEC 62443-1-1: Terminology, concepts and models — security vs. safety concepts and boundaries
- IEC 61511-1: Functional Safety: Safety Instrumented Systems for the Process Industry Sector — SIL definition, certificat
- IEC 61508: Functional Safety of Electrical/Electronic/Programmable Electronic Safety-Related Systems — foundational safe
- IEC 62443-2-1: Security Management System for IACS — security governance including SIS domain
- ID01 §7.4.1.7: SIS-specific security requirements and safety-security conflict resolution procedures
- ID02 Annex A.9 §12: SIS security control documentation and approval procedures

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | SIS is designated as a dedicated high-SL security zone with explicit isolation f | ✅ 已驗證 |
| 2 | Network isolation mechanism is specified and documented: air gap, dedicated fire | ✅ 已驗證 |
| 3 | SIS access control policy permits administrative access only through defined aut | ✅ 已驗證 |
| 4 | SIS communication conduits specify protocols, latency bounds, and reliability gu | ✅ 已驗證 |
| 5 | SIS Change Management Procedure defines dual-sign-off requirement (Security Arch | ✅ 已驗證 |
| 6 | Security-Safety Conflict Resolution Log documents at least one identified confli | ✅ 已驗證 |
| 7 | Functional Safety Engineer has reviewed SIS security architecture and issued wri | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D01-027 | | Junior (< 2 yr) | 12–18 person-days | Requires collaboration with safety engineer; includes confli |
| SK-D01-027 | | Senior (5+ yr) | 8–12 person-days | Same scope; senior leverages prior safety-security integration |
| SK-D01-027 | Notes: New SIS deployments (greenfield) typically require moderate effort. Upgrades to existing SIL- |

---

## 7. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 輸入完整性 | 所有必要輸入文件已讀取並摘要 |
| 2 | 流程覆蓋 | 1 個工作步驟皆已執行並有產出 |
| 3 | 輸出完整性 | 所有交付物已產出、格式正確、非空白 |
| 4 | 標準合規 | 產出引用的標準版本正確 |
| 5 | 術語一致 | 專案術語、縮寫與 glossary 一致 |
| 6 | 跨步驟一致 | 各步驟產出間無矛盾（如數量、SL等級） |

---

## 8. 人類審核閘門

完成所有工作步驟後，暫停並向使用者提交審核：

```
安全儀控系統實施已完成。
📋 執行範圍：1 個工程步驟（SK-D01-027）
📊 交付物清單：
  - SIS Security Architecture Specification: dedicated network segmentation for SIS, isolation mechanisms (air gap, demilitarized zone, application-level 
  - SIS Network Isolation Design: network topology with firewall rules separating SIS from non-safety OT and IT networks, conduit specifications for SIS-t
  - SIS Change Management Procedure: change process for SIS security controls, including change impact assessment for functional safety, SIL re-validation
  - Security-Safety Conflict Resolution Log: documented cases where security requirements and safety requirements compete, the chosen resolution (security
  - SIS Cybersecurity Assessment Report: mapping of IEC 62443 security requirements to SIS control implementation, verification that SIL certification is 
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
| SK 覆蓋 | SK-D01-027 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D01-027 | SIS Security Control Implementation | SIS 安全控制實施 | Design and implement cybersecurity controls for Safety Instr |

<!-- Phase 5 Wave 2 deepened: SK-D01-027 -->