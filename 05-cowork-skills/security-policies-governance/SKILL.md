---
name: security-policies-governance
description: >
  安全政策與治理。
  - **Pitfall:** Overly stringent policies disconnected from OT operational reality. **Guidance:** Validate policies with OT/ICS operators and system en。Develop the data classification policy that defines classification levels, labeling requirements, h
  MANDATORY TRIGGERS: 資料分類政策制定, 安全解決方案整合計畫撰寫, 安全政策與治理, integration-planning, security-architecture, Data Handling, ISO 27001, plan, procedures, development, system-design.
  Use this skill for security policies governance tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 安全政策與治理

本 Skill 整合 3 個工程技能定義，提供安全政策與治理的完整工作流程。
適用領域：OT Cybersecurity（D01）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D01-007, SK-D01-011, SK-D01-014, SK-D01-015, SK-D01-028

---

## 1. 輸入

- IEC 62443-2-1 requirements for security program management (ID02 §4.0-§9.0)
- IEC 62443-3-3 functional requirements that policies must support (ID01 §6.0 security requirements)
- ID07 Security Policies and Procedures Plan format exemplar and template
- Preliminary threat assessment from SK-D01-006 or SK-D01-008
- Defense-in-depth strategy from SK-D01-002
- IEC 62443 compliance gap analysis from SK-D01-011
- ISO 27001 Annex A and data classification guidance
- ID23 (Tier 3) data classification exemplar and framework
- Organizational information governance policies
- Industry/regulatory data protection requirements (GDPR, HIPAA, etc., as applicable)
- Project data types and sensitivity assessment
- Risk assessment findings (from SK-D01-006)

---

## 2. 工作流程

### Step 1: 
**SK 來源**：SK-D01-030 — Security Policies and Procedures Plan Development

執行：- **Pitfall:** Overly stringent policies disconnected from OT operational reality. **Guidance:** Validate policies with OT/ICS operators and system en

**本步驟交付物**：
- Security Policies and Procedures Plan Master Document:** Comprehensive policy plan per ID07 format, including executive summary, policy framework, det
- Policy Administration Guide:** Guidance for policy owners, administrators, and auditors on policy maintenance, exception handling, and periodic review
- Role and Responsibility Matrix (RACI):** Clear definition of responsibilities for security policy compliance, enforcement, and oversight

### Step 2: 資料分類政策制定
**SK 來源**：SK-D01-033 — Data Classification Policy Development

執行資料分類政策制定：Develop the data classification policy that defines classification levels, labeling requirements, handling rules, and access restrictions for project 

**本步驟交付物**：
- Data Classification Policy (formal document)
- Classification level definitions (e.g., Public, Internal, Confidential, Restricted)
- Classification criteria and decision rules per level

### Step 3: 安全解決方案整合計畫撰寫
**SK 來源**：SK-D01-034 — Security Solution Integration Plan Development

執行安全解決方案整合計畫撰寫：Develop the Security Solution Integration Plan documenting how individual security controls (firewalls, SIEM, endpoint protection, access control, bac

**本步驟交付物**：
- Security Solution Integration Plan (master document) containing:
- Executive summary: security vision, key integration principles, phasing overview
- Control inventory and sourcing: each control (firewall, SIEM, PAM, backup, etc.), vendor/COTS product, key specifications

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Security Policies and Procedures Plan Master Document:** Comprehensive policy plan per ID07 format, including executive summary, policy framework, det | 依需求 |
| 2 | Policy Administration Guide:** Guidance for policy owners, administrators, and auditors on policy maintenance, exception handling, and periodic review | 依需求 |
| 3 | Role and Responsibility Matrix (RACI):** Clear definition of responsibilities for security policy compliance, enforcement, and oversight | Markdown |
| 4 | Policy Implementation Roadmap:** Sequencing of policy activation across organizational phases, including dependencies and training requirements | 依需求 |
| 5 | Training Materials:** Policy summaries, awareness briefings, and role-specific procedural guidance for target audience | 依需求 |
| 6 | Policy Compliance Checklist:** Assessment tool for verifying policy implementation and identifying non-compliance | Markdown |
| 7 | Data Classification Policy (formal document) | 依需求 |
| 8 | Classification level definitions (e.g., Public, Internal, Confidential, Restricted) | 依需求 |
| 9 | Classification criteria and decision rules per level | 依需求 |
| 10 | Data labeling and marking requirements (physical and digital) | 依需求 |
| 11 | Handling and protection requirements for each classification level | 依需求 |
| 12 | Access restriction rules and approval authority by classification | 依需求 |

---

## 4. 適用標準

- IEC 62443-1-1: Security terminology and foundational concepts
- IEC 62443-2-1: Security Program Requirements (ID02); security policies and procedures are core program elements
- IEC 62443-3-3: System Security Requirements (functional requirements that policies must support)
- ID07 Exemplar: Format and content framework for security policies and procedures plan
- ISO/IEC 27001: Information security policy and procedure management practices (where applicable beyond OT scope)
- Regulatory frameworks: NERC CIP (North American power/utility security), FDA 21 CFR Part 11 (where applicable), jurisdic
- ISO/IEC 27001:2022 (Information security management system)
- Annex A (Control objectives and controls, particularly A.5 and A.6)
- ISO/IEC 27002:2022 (Code of practice for information security controls)
- IEC 62443-3-2 (Risk assessment and security classification)

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Plan covers all six core policy domains (§4.0 account management, §5.0 system ha | ✅ 已驗證 |
| 2 | Each policy includes specific, measurable requirements (not vague directives lik | ✅ 已驗證 |
| 3 | Policy requirements are explicitly linked to IEC 62443-3-3 functional requiremen | ✅ 已驗證 |
| 4 | Policy is operationally feasible: addresses OT/ICS constraints (process safety,  | ✅ 已驗證 |
| 5 | Role and responsibility matrix defines clear accountability for policy complianc | ✅ 已驗證 |
| 6 | All policies have explicit approval authority, approval status, and effective da | ✅ 已驗證 |
| 7 | Policies are cross-referenced to corresponding implementation skills (SK-D01-019 | ✅ 已驗證 |
| 8 | Exception approval workflow is defined with clear authority levels and documenta | ✅ 已驗證 |
| 9 | The Data Classification Policy follows a clear, logical structure covering defin | ✅ 已驗證 |
| 10 | Classification levels are defined with specific criteria and examples (e.g., Pub | ✅ 已驗證 |
| 11 | Each classification level specifies handling requirements including encryption,  | ✅ 已驗證 |
| 12 | Labeling and marking standards are defined for both physical documents and digit | ✅ 已驗證 |
| 13 | Data access restriction rules are explicit for each classification level, with d | ✅ 已驗證 |
| 14 | Data retention and disposal requirements are specified per classification level, | ✅ 已驗證 |
| 15 | Data sharing and transfer restrictions are documented, including geographic rest | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D01-033 | | Security Architect | 20 hours | 10 hours | Lead policy author and framework definition | |
| SK-D01-033 | | Compliance/DPO | 16 hours | 8 hours | Regulatory requirement integration and review | |
| SK-D01-033 | | Information Governance Manager | 8 hours | 4 hours | Organizational framework alignment | |
| SK-D01-033 | | Data Owner Representatives | 12 hours | 8 hours | Sensitivity and handling requirements input (per |
| SK-D01-033 | | Legal/Regulatory Counsel | 8 hours | 4 hours | Compliance verification | |
| SK-D01-033 | | **Total** | **64 hours** | **34 hours** | Highly dependent on organizational complexity and regula |
| SK-D01-034 | | Junior (< 2 yr) | 12–18 person-days | Assumes ~8–12 security controls, 3–4 integration phases, mod |
| SK-D01-034 | | Senior (5+ yr) | 5–8 person-days | Same scope; senior can leverage integration templates, risk lib |

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
安全政策與治理已完成。
📋 執行範圍：3 個工程步驟（SK-D01-030, SK-D01-033, SK-D01-034）
📊 交付物清單：
  - Security Policies and Procedures Plan Master Document:** Comprehensive policy plan per ID07 format, including executive summary, policy framework, det
  - Policy Administration Guide:** Guidance for policy owners, administrators, and auditors on policy maintenance, exception handling, and periodic review
  - Role and Responsibility Matrix (RACI):** Clear definition of responsibilities for security policy compliance, enforcement, and oversight
  - Policy Implementation Roadmap:** Sequencing of policy activation across organizational phases, including dependencies and training requirements
  - Training Materials:** Policy summaries, awareness briefings, and role-specific procedural guidance for target audience
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
| SK 覆蓋 | SK-D01-030, SK-D01-033, SK-D01-034 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D01-030 | Security Policies and Procedures Plan Development |  | - **Pitfall:** Overly stringent policies disconnected from O |
| SK-D01-033 | Data Classification Policy Development | 資料分類政策制定 | Develop the data classification policy that defines classifi |
| SK-D01-034 | Security Solution Integration Plan Development | 安全解決方案整合計畫撰寫 | Develop the Security Solution Integration Plan documenting h |

<!-- Phase 5 Wave 2 deepened: SK-D01-030, SK-D01-033, SK-D01-034 -->