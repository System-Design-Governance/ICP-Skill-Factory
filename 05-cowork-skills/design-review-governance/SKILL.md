---
name: design-review-governance
description: >
  設計審查與治理。
  Develop standardized design review checklists covering completeness, correctness, consistency, and compliance criteria for engineering deliverables ac。Execute critical security design reviews per IEC 62443-3-2 §7.3.2 for security-impacting design del
  MANDATORY TRIGGERS: 階段審查治理與阻斷條件驗證, 設計品質與追溯性驗證, 設計變更影響分析與SL重認證, 設計審查清單建立, 設計審查與治理, 關鍵安全設計審查, Gate-1, GOV-SD, Gate Review Governance & Blocking Condition Verification, quality-assurance, Gate-0, stage-gate, document-register, Design Change Impact Analysis & SL Recertification.
  Use this skill for design review governance tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 設計審查與治理

本 Skill 整合 5 個工程技能定義，提供設計審查與治理的完整工作流程。
適用領域：Governance & Process（D11）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D01-007, SK-D01-013, SK-D02-001, SK-D02-004, SK-D02-012

---

## 1. 輸入

- IEC 62443 series security requirements (ID01, ID02, ID03, ID04)
- Engineering domain standards and design practices (IEEE Std 1012 for verification/validation; domain-specific codes per D01–D12)
- Project-specific design standards and customer requirements (SOW, design guidelines)
- Identified design defects from prior projects (lessons learned, quality metrics database)
- Regulatory and compliance requirements (NERC CIP, DO-178C, IEC 61508, jurisdiction-specific codes)
- Role definitions and competency requirements (who executes and reviews what)
- Approved Security Functional Description Specification (SFDS) with security requirements traceability matrix (from SK-D01-001 ⏳: SFDS Development)
- Security-impacting design deliverables covering:
- Zone/Conduit Architecture Diagram and specification (from SK-D01-001 ⏳: Zone/Conduit Architecture Design)
- Network topology and data flow diagrams (from SK-D02-001 ⏳: OT Network Topology Design; SK-D02-004 ⏳: Data Flow Diagram Development)
- Protection device selection and settings (from D04 protection engineering)
- Device hardening and access control design (from SK-D05-001 ⏳: Device Hardening Design)

---

## 2. 工作流程

### Step 1: 設計審查清單建立
**SK 來源**：SK-D11-001 — Design Review Checklist Development

執行設計審查清單建立：Develop standardized design review checklists covering completeness, correctness, consistency, and compliance criteria for engineering deliverables ac

**本步驟交付物**：
- Design Review Checklist Template (structured markdown or Excel) with governance-mandated sections
- Domain-specific checklists for each engineering domain (D01, D02, D03, D04, D05, D09, D10, D11, D12)
- Verification category checklists (C.1–C.8 from ID02 Annex C: Requirements Traceability, Completeness, Design Correctness, Design-Implementation Consis

### Step 2: 關鍵安全設計審查
**SK 來源**：SK-D11-003 — Critical Security Design Review

執行關鍵安全設計審查：Execute critical security design reviews per IEC 62443-3-2 §7.3.2 for security-impacting design deliverables, verifying that security requirements (fr

**本步驟交付物**：
- Critical Security Design Review Report documenting:
- Scope of review (which design deliverables and domains were reviewed)
- Verification results for each security requirement in the SFDS (requirement ID, design element that implements it, verification status: Pass, Fail, or

### Step 3: 階段審查治理與阻斷條件驗證
**SK 來源**：SK-D11-017 — Gate Review Governance & Blocking Condition Verification

執行階段審查治理與阻斷條件驗證：Govern the 4-gate review process (Gate 0–Gate 3) per GOV-SD, verifying that all gate-specific blocking conditions are satisfied before approving stage

**本步驟交付物**：
- Gate Review Record (per-gate): gate decision (Pass/Conditional Pass/Fail), evidence of condition verification, approval authority signature, date/time
- Gate 0 Decision: approval to proceed to R1 security requirements analysis, OR block with remediation requirements
- Gate 1 Decision: approval to proceed to R2 detailed security design, OR block with remediation requirements; includes Lite/Complete pathway authorizat

### Step 4: 設計品質與追溯性驗證
**SK 來源**：SK-D11-018 — Design Quality & Traceability Verification

執行設計品質與追溯性驗證：Verify design quality and traceability per the Design QA role responsibilities defined in governance structure (GOV-SD: Design QA). This verification 

**本步驟交付物**：
- Design Quality Verification Report including:
- Traceability matrix completeness assessment (percentage of requirements traced to design; any gaps identified and disposition)
- Document register audit results (all expected deliverables present; versions match requirements; approval signatures complete)

### Step 5: 設計變更影響分析與SL重認證
**SK 來源**：SK-D11-020 — Design Change Impact Analysis & SL Recertification

執行設計變更影響分析與SL重認證：Analyze the security impact of design changes per GOV-SD Gate 2 trigger criteria (Tier 1 governance decision point), determining whether changes requi

**本步驟交付物**：
- SL Decision Record documenting:
- Change ID, description, and affected system/zone(s)
- Impact analysis results: Does the change trigger SL-T reassessment? (Yes/No/Conditional)

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Design Review Checklist Template (structured markdown or Excel) with governance-mandated sections | Markdown |
| 2 | Domain-specific checklists for each engineering domain (D01, D02, D03, D04, D05, D09, D10, D11, D12) | Markdown |
| 3 | Verification category checklists (C.1–C.8 from ID02 Annex C: Requirements Traceability, Completeness, Design Correctness, Design-Implementation Consis | Markdown |
| 4 | Checklist usage guidance document (when to execute, roles, escalation procedures) | Markdown |
| 5 | Periodic checklist effectiveness review report (defect escape analysis, process improvement recommendations) | Markdown |
| 6 | Critical Security Design Review Report documenting: | Markdown |
| 7 | Scope of review (which design deliverables and domains were reviewed) | 依需求 |
| 8 | Verification results for each security requirement in the SFDS (requirement ID, design element that implements it, verification status: Pass, Fail, or | 依需求 |
| 9 | Findings: defects, gaps, or deviations from security requirements or standards | 依需求 |
| 10 | Risk assessment of findings (Critical, High, Medium, Low) with recommended mitigations | 依需求 |
| 11 | Defense-in-depth assessment: verification that multiple independent security layers are implemented | 依需求 |
| 12 | Gate Review Record (per-gate): gate decision (Pass/Conditional Pass/Fail), evidence of condition verification, approval authority signature, date/time | 依需求 |

---

## 4. 適用標準

- IEC 62443-3-2: Security Risk Assessment for System Design — design review and verification requirements
- IEC 62443-3-3: System Security Requirements and Security Levels — verification gates aligned to design phases
- IEEE Std 1012: Software Verification and Validation — structured V&V framework (applicable to automation system design)
- ISO/IEC/IEEE 42010: System and software engineering — architecture description framework, design review scope
- ID02 Annex C: Design Verification Checklist — primary normative reference for C.1–C.8 categories
- IEC 62443-3-2 §7.3.2: Review and Approval of Engineering Design Specifications for Security — critical review requiremen
- IEC 62443-3-2 §7.3.1: Detailed Design Specification for Hardening to SL4 — security design quality expectations
- IEC 62443-1-1: Terminology and Concepts — defense-in-depth principles
- ISO/IEC/IEEE 42010: System and software engineering — architecture description and verification framework
- ID02 Annex C: Design Verification Checklist — specifically C.6 (Security Requirements Implementation) and C.8 (Standards

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Checklists exist for all engineering domains (D01, D02, D03, D04, D05, D09, D10, | ✅ 已驗證 |
| 2 | Each checklist explicitly maps to verification categories C.1–C.8 per ID02 Annex | ✅ 已驗證 |
| 3 | Checklists include objective, measurable criteria (not vague or qualitative item | ✅ 已驗證 |
| 4 | Completeness criteria: checklist items cover 100% of identified design verificat | ✅ 已驗證 |
| 5 | Security-specific checklists (C.6) include all security requirements from the ap | ✅ 已驗證 |
| 6 | Checklist effectiveness has been validated: documented review of defect escape r | ✅ 已驗證 |
| 7 | All design and engineering team members have received training on checklist exec | ✅ 已驗證 |
| 8 | All security requirements in the approved SFDS have been mapped to design elemen | ✅ 已驗證 |
| 9 | Each security requirement has a corresponding design element that implements it, | ✅ 已驗證 |
| 10 | No Critical findings remain unaddressed (Fail status converted to Pass or Condit | ✅ 已驗證 |
| 11 | High-risk findings have documented mitigations or explicit risk acceptance by PE | ✅ 已驗證 |
| 12 | Defense-in-depth assessment confirms that security controls are independent and  | ✅ 已驗證 |
| 13 | Design review checklist (C.1–C.6) completion rate is 100%; any non-applicable it | ✅ 已驗證 |
| 14 | Cryptography design (if used) has been reviewed for key management, cryptographi | ✅ 已驗證 |
| 15 | Review has been signed off by SAC and PE/O per ID01 §7.4.2 review process | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D11-001 | | Governance Lead (Master) | 15–20 person-days | Initial development of 8–12 domain checklists inclu |
| SK-D11-001 | | Domain Lead (Senior) | 3–5 person-days | Development of domain-specific checklist for one engineer |
| SK-D11-001 | Notes: Ongoing maintenance and improvement is typically 1–2 person-days per quarter. Customization f |
| SK-D11-003 | | SAC / Senior Security Architect | 10–15 person-days | Complete security design review for greenfie |
| SK-D11-003 | | SAC with STC support | 8–12 person-days | Same scope with division of labor; STC provides technica |
| SK-D11-003 | Notes: Brownfield projects or projects with complex threat models may require 20+ days. Projects wit |
| SK-D11-017 | | Junior (< 2 yr) | 2–4 person-days per gate | Assumes 4 gates per project lifecycle; includes check |
| SK-D11-017 | | Senior (5+ yr) | 1–2 person-days per gate | Same scope; senior can efficiently verify conditions a |

---

## 7. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 輸入完整性 | 所有必要輸入文件已讀取並摘要 |
| 2 | 流程覆蓋 | 5 個工作步驟皆已執行並有產出 |
| 3 | 輸出完整性 | 所有交付物已產出、格式正確、非空白 |
| 4 | 標準合規 | 產出引用的標準版本正確 |
| 5 | 術語一致 | 專案術語、縮寫與 glossary 一致 |
| 6 | 跨步驟一致 | 各步驟產出間無矛盾（如數量、SL等級） |
| 7 | 依賴追溯 | 外部依賴 SK 的輸入已驗證可用 |

---

## 8. 人類審核閘門

完成所有工作步驟後，暫停並向使用者提交審核：

```
設計審查與治理已完成。
📋 執行範圍：5 個工程步驟（SK-D11-001, SK-D11-003, SK-D11-017, SK-D11-018, SK-D11-020）
📊 交付物清單：
  - Design Review Checklist Template (structured markdown or Excel) with governance-mandated sections
  - Domain-specific checklists for each engineering domain (D01, D02, D03, D04, D05, D09, D10, D11, D12)
  - Verification category checklists (C.1–C.8 from ID02 Annex C: Requirements Traceability, Completeness, Design Correctness, Design-Implementation Consis
  - Checklist usage guidance document (when to execute, roles, escalation procedures)
  - Periodic checklist effectiveness review report (defect escape analysis, process improvement recommendations)
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
| Domain | D11 (Governance & Process) |
| SK 覆蓋 | SK-D11-001, SK-D11-003, SK-D11-017, SK-D11-018, SK-D11-020 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D11-001 | Design Review Checklist Development | 設計審查清單建立 | Develop standardized design review checklists covering compl |
| SK-D11-003 | Critical Security Design Review | 關鍵安全設計審查 | Execute critical security design reviews per IEC 62443-3-2 § |
| SK-D11-017 | Gate Review Governance & Blocking Condition Verification | 階段審查治理與阻斷條件驗證 | Govern the 4-gate review process (Gate 0–Gate 3) per GOV-SD, |
| SK-D11-018 | Design Quality & Traceability Verification | 設計品質與追溯性驗證 | Verify design quality and traceability per the Design QA rol |
| SK-D11-020 | Design Change Impact Analysis & SL Recertification | 設計變更影響分析與SL重認證 | Analyze the security impact of design changes per GOV-SD Gat |

<!-- Phase 5 Wave 2 deepened: SK-D11-001, SK-D11-003, SK-D11-017, SK-D11-018, SK-D11-020 -->