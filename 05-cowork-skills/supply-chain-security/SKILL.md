---
name: supply-chain-security
description: >
  供應鏈安全管理。
  Evaluate and score the cybersecurity risk posture of vendors, subcontractors, and component suppliers participating in the SuC delivery, covering vend。Analyze and manage Software Bill of Materials (SBOM) for OT/ICS components, including SBOM generati
  MANDATORY TRIGGERS: 供應商安全管理計畫撰寫, 第三方元件安全驗證, 供應商安全風險評估, 供應鏈安全管理, SBOM 分析與管理, Vendor Security Risk Assessment, Supply Chain Security, Governance, third-party, Vendor Management, vendor-risk, procurement, vulnerability-assessment.
  Use this skill for supply chain security tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 供應鏈安全管理

本 Skill 整合 4 個工程技能定義，提供供應鏈安全管理的完整工作流程。
適用領域：OT Cybersecurity（D01）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D01-005, SK-D01-007, SK-D01-010, SK-D02-001, SK-D14-018

---

## 1. 輸入

- Vendor information packages: company profiles, security certifications (ISO 27001, IEC 62443-4-1), product security documentation
- ICP Procurement and Supplier Management Procedure (ID22, Tier 3) — qualification scoring criteria and approved vendor list process
- Asset inventory with vendor-supplied components identified (from SK-D01-005)
- Customer/employer requirements for supply chain security (contractual obligations)
- IEC 62443-2-4 supply chain security requirements
- GOV-SD Gate 0 scope — supply chain risk is an explicit Gate 0 consideration
- Component list from system design (hardware BOM, firmware versions, operating system versions, application software package list from SK-D02-001 ⏳ and
- SBOMs from hardware/software vendors (CycloneDX, SPDX, or proprietary formats; sourced through vendor datasheets, supply agreements, or vendor portals
- NIST National Vulnerability Database (NVD) access and/or commercial CVE database subscriptions (NVD, CVE Details, Qualys, Rapid7, etc.)
- Existing component license database (if available from procurement/legal)
- System architecture and component deployment mapping (which components run in which zones, criticality levels)
- Change management records for component updates or substitutions during project lifecycle

---

## 2. 工作流程

### Step 1: 供應商安全風險評估
**SK 來源**：SK-D01-024 — Vendor Security Risk Assessment

執行供應商安全風險評估：Evaluate and score the cybersecurity risk posture of vendors, subcontractors, and component suppliers participating in the SuC delivery, covering vend

**本步驟交付物**：
- Vendor Security Risk Assessment Report:
- Vendor identification and scope of supply (hardware, software, services)
- Security capability evaluation: certification status, secure development lifecycle maturity, vulnerability disclosure process, patch support commitmen

### Step 2: SBOM 分析與管理
**SK 來源**：SK-D01-025 — SBOM Analysis and Management

執行SBOM 分析與管理：Analyze and manage Software Bill of Materials (SBOM) for OT/ICS components, including SBOM generation and collection from vendors, vulnerability match

**本步驟交付物**：
- Consolidated SBOM in standardized format (CycloneDX or SPDX XML): component name, version, vendor, component type, hash/checksum for verification
- SBOM Mapping Table: system component → SBOM entry → version → deployment location (zone/system) → criticality level
- CVE Matching Report: component name, version, identified CVEs (CVE ID, base score, affected versions), publication date, criticality classification pe

### Step 3: 第三方元件安全驗證
**SK 來源**：SK-D01-026 — Third-Party Component Security Verification

執行第三方元件安全驗證：Conduct systematic security verification of third-party software, firmware, and hardware components before integration into the System under Considera

**本步驟交付物**：
- Third-Party Component Security Verification Report (per component or component family): component name, version, vendor, assessment date, vulnerabilit
- Compliance Assessment Matrix: component security properties vs. project requirements (encryption algorithms, key lengths, authentication methods, logg
- Vulnerability Remediation Plan (if conditional approval): list of identified vulnerabilities, vendor patch availability, patch validation timeline, in

### Step 4: 供應商安全管理計畫撰寫
**SK 來源**：SK-D01-031 — Vendor Security Management Plan Development

執行供應商安全管理計畫撰寫：Develop the Vendor Security Management Plan per ID05 format exemplar, establishing the framework for vendor security evaluation, ongoing monitoring, a

**本步驟交付物**：
- Vendor Security Management Plan (formal document)
- Executive summary and scope of vendor management
- Vendor categorization framework (criticality, risk level)

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Vendor Security Risk Assessment Report: | Markdown |
| 2 | Vendor identification and scope of supply (hardware, software, services) | 依需求 |
| 3 | Security capability evaluation: certification status, secure development lifecycle maturity, vulnerability disclosure process, patch support commitmen | 依需求 |
| 4 | Qualification scoring per ID22 criteria: quality system, delivery capability, technical competence, security posture (weighted scoring) | 依需求 |
| 5 | Risk rating per vendor: High / Medium / Low with justification | 依需求 |
| 6 | Compensating controls for vendors with identified gaps (contractual security requirements, inspection clauses, escrow agreements) | 依需求 |
| 7 | Consolidated SBOM in standardized format (CycloneDX or SPDX XML): component name, version, vendor, component type, hash/checksum for verification | 依需求 |
| 8 | SBOM Mapping Table: system component → SBOM entry → version → deployment location (zone/system) → criticality level | 依需求 |
| 9 | CVE Matching Report: component name, version, identified CVEs (CVE ID, base score, affected versions), publication date, criticality classification pe | Markdown |
| 10 | Component Lifecycle Tracking Register: component ID, introduction date, version history, replacement dates, end-of-life status | 依需求 |
| 11 | License Compliance Inventory: component name, version, license type (proprietary, Apache 2.0, GPL v3, etc.), organizational license policy compatibili | 依需求 |
| 12 | Third-Party Component Risk Summary (input to SK-D01-026): total components analyzed, vulnerable component count, critical/high/medium/low vulnerabilit | 依需求 |

---

## 4. 適用標準

- IEC 62443-2-4 SP.01.01–SP.01.04: Service provider capability requirements (security competence, supply chain management)
- IEC 62443-4-1: Product Security Development Life-Cycle Requirements — vendor maturity assessment basis
- ISO 27001 Annex A.15: Supplier Relationships
- ISO 28000: Supply Chain Security Management (supplementary)
- GOV-SD: Gate 0 supply chain risk consideration — vendor risk assessment must be available before Gate 0 approval
- IEC 62443-4-2: Supply Chain & Lifecycle Requirements — SBOM and component security management
- NTIA "Minimum Elements for Software Transparency": SBOM format and content requirements
- NIST SP 800-53 Rev. 5, SA-3 System Development Life Cycle: supply chain risk management, component tracking
- NIST Cybersecurity Framework (CSF): Govern and Manage supply chain risks
- SPDX (Software Package Data Exchange): SBOM interchange format standard

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Every vendor supplying hardware, software, or security services to the SuC has a | ✅ 已驗證 |
| 2 | Qualification scoring completed per ID22 criteria for all vendors, with weighted | ✅ 已驗證 |
| 3 | Vendor risk register maintained with review schedule: High-risk vendors reviewed | ✅ 已驗證 |
| 4 | Vendor security requirements specification produced: contractual security clause | ✅ 已驗證 |
| 5 | Gate 0 supply chain risk summary delivered as part of Gate 0 decision package (p | ✅ 已驗證 |
| 6 | No vendor with High risk rating without documented compensating controls and exp | ✅ 已驗證 |
| 7 | SBOMs collected for 100% of third-party software components and 80%+ of hardware | ✅ 已驗證 |
| 8 | SBOM consolidation is complete: all component versions deployed in the system ar | ✅ 已驗證 |
| 9 | CVE matching is performed against current NVD snapshot; all critical and high-se | ✅ 已驗證 |
| 10 | Component lifecycle register accounts for all component introductions, version u | ✅ 已驗證 |
| 11 | License compliance inventory is complete and reviewed by legal; no unapproved li | ✅ 已驗證 |
| 12 | Continuous monitoring plan is established with defined check cadence (at least q | ✅ 已驗證 |
| 13 | SBOM and associated analyses are version-controlled and audit-traceable (change  | ✅ 已驗證 |
| 14 | Every third-party component in the SuC BoM has a corresponding security verifica | ✅ 已驗證 |
| 15 | Vulnerability scan reports document CVE count, CVSS scores, and vendor patch/rem | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D01-024 | | Junior (< 2 yr) | 8–12 person-days | Assumes 5–10 vendors, initial qualification; includes questio |
| SK-D01-024 | | Senior (5+ yr) | 4–6 person-days | Same scope; senior leverages existing vendor assessment templat |
| SK-D01-024 | Notes: Effort scales with vendor count and supply chain complexity. Projects with COTS-heavy archite |
| SK-D01-025 | | Junior (< 2 yr) | 10–15 person-days | Assumes ~80–120 components, partial SBOM availability from v |
| SK-D01-025 | | Senior (5+ yr) | 4–7 person-days | Same scope; senior can leverage automated SBOM tools, batch CVE |
| SK-D01-025 | Notes: Greenfield projects with good vendor SBOM support may require 5–8 days less effort. Brownfiel |
| SK-D01-026 | | Junior (< 2 yr) | 4–6 person-days | Assumes ~20 components, standard tools and checklists; include |
| SK-D01-026 | | Senior (5+ yr) | 2–3 person-days | Same scope; senior leverages vendor relationships and known com |

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
供應鏈安全管理已完成。
📋 執行範圍：4 個工程步驟（SK-D01-024, SK-D01-025, SK-D01-026, SK-D01-031）
📊 交付物清單：
  - Vendor Security Risk Assessment Report:
  - Vendor identification and scope of supply (hardware, software, services)
  - Security capability evaluation: certification status, secure development lifecycle maturity, vulnerability disclosure process, patch support commitmen
  - Qualification scoring per ID22 criteria: quality system, delivery capability, technical competence, security posture (weighted scoring)
  - Risk rating per vendor: High / Medium / Low with justification
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
| SK 覆蓋 | SK-D01-024, SK-D01-025, SK-D01-026, SK-D01-031 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D01-024 | Vendor Security Risk Assessment | 供應商安全風險評估 | Evaluate and score the cybersecurity risk posture of vendors |
| SK-D01-025 | SBOM Analysis and Management | SBOM 分析與管理 | Analyze and manage Software Bill of Materials (SBOM) for OT/ |
| SK-D01-026 | Third-Party Component Security Verification | 第三方元件安全驗證 | Conduct systematic security verification of third-party soft |
| SK-D01-031 | Vendor Security Management Plan Development | 供應商安全管理計畫撰寫 | Develop the Vendor Security Management Plan per ID05 format  |

<!-- Phase 5 Wave 2 deepened: SK-D01-024, SK-D01-025, SK-D01-026, SK-D01-031 -->