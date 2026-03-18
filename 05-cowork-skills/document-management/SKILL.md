---
name: document-management
description: >
  文件與版本管理。
  This skill encompasses the systematic management of all project document deliverables per the contract and ID03 requirements, tracking each deliverabl。- Analyze archive retrieval metrics to identify indexing gaps or process inefficiencies
  MANDATORY TRIGGERS: 文件與版本管理, 版本控制與歸檔, 文件交付清單管理, gate-control, deliverable-tracking, project-management, Document Delivery Checklist Management, document-management, contract-compliance, document management, Version Control and Archiving.
  Use this skill for document management tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 文件與版本管理

本 Skill 整合 2 個工程技能定義，提供文件與版本管理的完整工作流程。
適用領域：Documentation（D09）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D08-001, SK-D11-001, SK-D11-005, SK-D11-006

---

## 1. 輸入

- Contract and Statement of Work (SOW) specifying deliverable requirements and delivery schedule
- Project schedule and milestone dates (from SK-D11-001: Project Planning)
- Design plan and work breakdown structure (WBS) identifying which skill/discipline is responsible for each deliverable
- Technical specifications for deliverable format, quality standards, and review criteria (per ID03 §5.5.3)
- Gate 3 (Design Review) checklist template and review criteria
- Previous deliverable checklists from similar projects (for template adaptation)
- Project governance structure defined: CCB authority, approval matrix, change request procedures
- Document classification scheme established (e.g., specification, design, test, security assessment, SOP)
- Archive storage location(s) identified and approved: local network, enterprise repository, cloud platform
- Retention policy framework developed aligned with regulatory requirements and organizational needs
- Version control tools selected and configured: document management system (DMS) or revision control system (RCS)
- Team training planned on version control and archiving procedures

---

## 2. 工作流程

### Step 1: 文件交付清單管理
**SK 來源**：SK-D09-004 — Document Delivery Checklist Management

執行文件交付清單管理：This skill encompasses the systematic management of all project document deliverables per the contract and ID03 requirements, tracking each deliverabl

**本步驟交付物**：
- Document Delivery Checklist (DDC): master spreadsheet/document listing all contractual deliverables with status (Draft, Under Review, Approved, Delive
- Deliverable Status Report: monthly or gate-level report summarizing completeness percentage, at-risk deliverables, and mitigation actions
- Gate 3 Delivery Verification Checklist: formal sign-off confirming all design-phase deliverables meet quality and completeness criteria

### Step 2: 版本控制與歸檔
**SK 來源**：SK-D09-005 — Version Control and Archiving

執行版本控制與歸檔：- Analyze archive retrieval metrics to identify indexing gaps or process inefficiencies

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Document Delivery Checklist (DDC): master spreadsheet/document listing all contractual deliverables with status (Draft, Under Review, Approved, Delive | Markdown |
| 2 | Deliverable Status Report: monthly or gate-level report summarizing completeness percentage, at-risk deliverables, and mitigation actions | Markdown |
| 3 | Gate 3 Delivery Verification Checklist: formal sign-off confirming all design-phase deliverables meet quality and completeness criteria | Markdown |
| 4 | Deliverable Handover Record: signed acknowledgment from customer upon final delivery of all project documents | 依需求 |
| 5 | Lessons Learned on Deliverable Management: process improvements for tracking and delivery efficiency | 依需求 |

---

## 4. 適用標準

- ID03 §5.5.3: Document Delivery Checklist Management — primary procedural requirements for tracking and delivery
- ID01 §7.0: Design Phase requirements — all design deliverables must conform to ID01 standards
- ID02 Annex A: Security countermeasure documentation — ensures all security deliverables are included
- Project management best practices (PMBOK, ISO 21500) for deliverable tracking
- Contractual requirements per SOW and customer specifications
- IEC 62443-1-1: Terminology and concepts
- IEC 62443-3-3: System design and engineering; documentation requirements
- ISO 9001: Quality management; document control
- ISO 27001: Information security; asset management and documentation
- Project-specific document control procedures

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | DDC includes 100% of deliverables specified in the contract and SOW, organized b | ✅ 已驗證 |
| 2 | Each deliverable has a clearly assigned owner, planned delivery date, and docume | ✅ 已驗證 |
| 3 | DDC status is updated at least monthly and reported at all project gate reviews  | ✅ 已驗證 |
| 4 | All at-risk deliverables (past due or approaching deadline) have documented miti | ✅ 已驗證 |
| 5 | Gate 3 sign-off confirms that all design-phase deliverables are complete, approv | ✅ 已驗證 |
| 6 | Final project closeout includes a Deliverable Handover Record signed by both pro | ✅ 已驗證 |
| 7 | Version numbering scheme documented and communicated; consistent application acr | ✅ 已驗證 |
| 8 | Change tracking mechanism implemented in all documents; change history visible f | ✅ 已驗證 |
| 9 | Baseline management process defined with CCB authority, change request form, and | ✅ 已驗證 |
| 10 | Archive storage location configured with appropriate access controls, backup str | ✅ 已驗證 |
| 11 | Retention policy documented by document type; retention tracking system implemen | ✅ 已驗證 |
| 12 | Retrieval index and search procedures documented; archive custodian designated | ✅ 已驗證 |
| 13 | All team members trained on version control and archiving procedures | ✅ 已驗證 |
| 14 | Audit of archive demonstrates 100% traceability of document versions and changes | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D09-004 | | Junior (< 2 yr) | 2–4 person-days | Assumes single-site project with 30–50 contractual deliverable |
| SK-D09-004 | | Senior (5+ yr) | 1–2 person-days | Same scope; senior can rapidly establish DDC template, identify |
| SK-D09-004 | Notes: Multi-site or phased projects may require 1.5–2× effort. Ongoing maintenance throughout proje |
| SK-D09-005 | Archive retrieval speed: average time to locate and retrieve historical document <24 hours |

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
文件與版本管理已完成。
📋 執行範圍：2 個工程步驟（SK-D09-004, SK-D09-005）
📊 交付物清單：
  - Document Delivery Checklist (DDC): master spreadsheet/document listing all contractual deliverables with status (Draft, Under Review, Approved, Delive
  - Deliverable Status Report: monthly or gate-level report summarizing completeness percentage, at-risk deliverables, and mitigation actions
  - Gate 3 Delivery Verification Checklist: formal sign-off confirming all design-phase deliverables meet quality and completeness criteria
  - Deliverable Handover Record: signed acknowledgment from customer upon final delivery of all project documents
  - Lessons Learned on Deliverable Management: process improvements for tracking and delivery efficiency
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
| Domain | D09 (Documentation) |
| SK 覆蓋 | SK-D09-004, SK-D09-005 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D09-004 | Document Delivery Checklist Management | 文件交付清單管理 | This skill encompasses the systematic management of all proj |
| SK-D09-005 | Version Control and Archiving | 版本控制與歸檔 | - Analyze archive retrieval metrics to identify indexing gap |

<!-- Phase 5 Wave 2 deepened: SK-D09-004, SK-D09-005 -->