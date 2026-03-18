---
name: quality-assurance
description: >
  品質保證與管理。
  **Example: Quality Plan for Critical Infrastructure SCADA Modernization**。This skill encompasses the design and execution of a comprehensive Stakeholder Communication Plan that identifies all project stakeholders, defines th。Classify and grade all in
  MANDATORY TRIGGERS: 品質計畫撰寫, 資訊資產分類分級, 品質保證與管理, 不合格項管理, nonconformance, information-classification, Information Asset Classification and Grading, information-security, quality assurance, data-classification, management, Nonconformance Management.
  Use this skill for quality assurance tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 品質保證與管理

本 Skill 整合 3 個工程技能定義，提供品質保證與管理的完整工作流程。
適用領域：Governance & Process（D11）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-005, SK-D01-006, SK-D01-020, SK-D01-024, SK-D01-033, SK-D02-009

---

## 1. 輸入

- Project Charter and Statement of Work (SOW) — defines stakeholder expectations and communication contractual requirements
- Stakeholder Analysis and Register (from SK-D11-001: Project Planning) — identifies stakeholders, their roles, interests, and influence levels
- Project Schedule and Milestones (from SK-D11-001: Project Planning) — drives communication timing and frequency
- Project Risk Register (from SK-D11-017: Risk Management Plan) — high-risk items may require targeted stakeholder communication
- Organizational communication policies and escalation procedures
- Prior project communication plans and lessons learned (for template and best practices)
- Data Classification Policy ID23 (organizational standard for asset grades, protection criteria, handling rules)
- Asset inventory with data type/sensitivity assessment (from SK-D01-005 or equivalent, listing information assets in scope)
- Preliminary risk assessment findings (asset criticality, threat landscape from SK-D01-006 ⏳)
- Regulatory/contractual data protection requirements (GDPR, NDA terms, customer DPA, industry standards)
- Information flow and system architecture diagram (understanding which assets move where)
- Existing classification precedents or legacy grading schemes (for consistency and transition planning)

---

## 2. 工作流程

### Step 1: 品質計畫撰寫
**SK 來源**：SK-D11-006 — Quality Plan Development

執行品質計畫撰寫：**Example: Quality Plan for Critical Infrastructure SCADA Modernization**

### Step 2: 不合格項管理
**SK 來源**：SK-D11-007 — Nonconformance Management

執行不合格項管理：This skill encompasses the design and execution of a comprehensive Stakeholder Communication Plan that identifies all project stakeholders, defines th

**本步驟交付物**：
- Stakeholder Communication Plan: document specifying stakeholder groups, communication objectives for each group, communication content and frequency, 
- Stakeholder Register: structured list of stakeholders with contact information, role, communication preferences, and frequency
- Communication Schedule: calendar of recurring communications (status reports, reviews, approval gates) aligned with project milestones

### Step 3: 資訊資產分類分級
**SK 來源**：SK-D11-013 — Information Asset Classification and Grading

執行資訊資產分類分級：Classify and grade all information assets (documents, data files, configurations, credentials, test results, audit records) according to organizationa

**本步驟交付物**：
- Information Asset Classification Matrix**: listing of all information assets with assigned grades (Confidentiality, Integrity, Availability levels), h
- Asset Classification Register**: structured inventory (Excel/Airtable) organized by asset type, grade, owner, custodian, retention period, and audit t
- Classification Criteria Mapping Document**: rationale for each asset's grade, traceable to ID23 policy, risk assessment, and regulatory drivers

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Stakeholder Communication Plan: document specifying stakeholder groups, communication objectives for each group, communication content and frequency,  | 依需求 |
| 2 | Stakeholder Register: structured list of stakeholders with contact information, role, communication preferences, and frequency | Markdown |
| 3 | Communication Schedule: calendar of recurring communications (status reports, reviews, approval gates) aligned with project milestones | Markdown |
| 4 | Communication Templates: email templates, status report formats, presentation decks for consistency and efficiency | Markdown |
| 5 | Escalation Procedures: decision authority levels and escalation paths for different issue categories | 依需求 |
| 6 | Communication Effectiveness Metrics: methods for measuring stakeholder satisfaction, information timeliness, and engagement | 依需求 |
| 7 | Information Asset Classification Matrix**: listing of all information assets with assigned grades (Confidentiality, Integrity, Availability levels), h | Markdown |
| 8 | Asset Classification Register**: structured inventory (Excel/Airtable) organized by asset type, grade, owner, custodian, retention period, and audit t | 依需求 |
| 9 | Classification Criteria Mapping Document**: rationale for each asset's grade, traceable to ID23 policy, risk assessment, and regulatory drivers | 依需求 |
| 10 | Data Handling and Protection Requirements Table**: per-grade specifications for: | 依需求 |
| 11 | Access authorization (who may view/modify) | 依需求 |
| 12 | Encryption requirements (at rest and in transit) | 依需求 |

---

## 4. 適用標準

- IEC 62443-3-3 (Secure Design):** Design must demonstrate compliance with security requirements; quality plan must verify
- IEC 62443-1-1 (Governance):** Design verification and acceptance are governance activities; quality plan documents the g
- Functional Safety (IEC 61511, IEC 61508):** Safety-critical design requires functional safety assessment; quality plan m
- Industry Standards:** Industry-specific design standards (NERC CIP for power, API 1164 for oil & gas) may mandate specif
- Design Change Control:** Changes to approved designs are subject to change control; quality plan enforces change control
- Project Management Institute (PMI) PMBOK: Stakeholder Engagement Plan and Communication Management standards
- ISO 21500: Guidance on project management — stakeholder engagement principles
- IEC 62443-1-1: Terminology and concepts — stakeholder engagement in secure system development
- Organizational communication policies and procedures
- Regulatory communication requirements (if applicable to the project)

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Quality objectives statement specifies minimum 5 quality objectives with measura | ✅ 已驗證 |
| 2 | Stakeholder expectations document identifies quality expectations from engineeri | ✅ 已驗證 |
| 3 | Verification methods table assigns to each major deliverable: specific verificat | ✅ 已驗證 |
| 4 | Acceptance criteria checklist, for each major deliverable, specifies minimum 8-1 | ✅ 已驗證 |
| 5 | Hold points document identifies minimum 4 critical gates in design execution whe | ✅ 已驗證 |
| 6 | Quality records specification identifies all records to be maintained (design re | ✅ 已驗證 |
| 7 | Roles and responsibilities matrix assigns quality responsibilities to specific p | ✅ 已驗證 |
| 8 | Verification schedule integrates quality activities into project timeline; shows | ✅ 已驗證 |
| 9 | Communication Plan identifies all significant stakeholders (customer, regulatory | ✅ 已驗證 |
| 10 | Communication Plan defines specific communication objectives for each major proj | ✅ 已驗證 |
| 11 | Escalation procedures clearly define decision authority levels (e.g., issues res | ✅ 已驗證 |
| 12 | Communication Schedule is aligned with project milestones and gate reviews; recu | ✅ 已驗證 |
| 13 | All stakeholders have received and acknowledged the Communication Plan; preferen | ✅ 已驗證 |
| 14 | Communication effectiveness is monitored through periodic stakeholder surveys or | ✅ 已驗證 |
| 15 | 100% of identified information assets in scope have a documented classification  | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D11-007 | | Junior (< 2 yr) | 3–6 person-days | Assumes 5–10 stakeholder groups, single-site project; includes |
| SK-D11-007 | | Senior (5+ yr) | 1–3 person-days | Same scope; senior can rapidly establish communication structur |
| SK-D11-007 | Notes: Multi-site or multi-customer projects may require 1.5–2× effort. Ongoing execution of communi |
| SK-D11-013 | | Junior (< 2 yr) | 5–8 person-days | Assumes ~100 distinct information assets; requires SME input f |
| SK-D11-013 | | Senior (5+ yr) | 2–4 person-days | Leverages classification templates and rapid asset type recogni |
| SK-D11-013 | Notes: Classification of 500+ assets or complex multi-stakeholder data flows may require 1.5–2× effo |

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
品質保證與管理已完成。
📋 執行範圍：3 個工程步驟（SK-D11-006, SK-D11-007, SK-D11-013）
📊 交付物清單：
  - Stakeholder Communication Plan: document specifying stakeholder groups, communication objectives for each group, communication content and frequency, 
  - Stakeholder Register: structured list of stakeholders with contact information, role, communication preferences, and frequency
  - Communication Schedule: calendar of recurring communications (status reports, reviews, approval gates) aligned with project milestones
  - Communication Templates: email templates, status report formats, presentation decks for consistency and efficiency
  - Escalation Procedures: decision authority levels and escalation paths for different issue categories
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
| SK 覆蓋 | SK-D11-006, SK-D11-007, SK-D11-013 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D11-006 | Quality Plan Development | 品質計畫撰寫 | **Example: Quality Plan for Critical Infrastructure SCADA Mo |
| SK-D11-007 | Nonconformance Management | 不合格項管理 | This skill encompasses the design and execution of a compreh |
| SK-D11-013 | Information Asset Classification and Grading | 資訊資產分類分級 | Classify and grade all information assets (documents, data f |

<!-- Phase 5 Wave 2 deepened: SK-D11-006, SK-D11-007, SK-D11-013 -->