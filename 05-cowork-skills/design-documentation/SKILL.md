---
name: design-documentation
description: >
  設計文件撰寫。
  This skill encompasses the authoring of a comprehensive System Design Description (SDD) document that consolidates the outputs of security architectur。Author the Security Functional Description Specification (SFDS) document that maps IEC 62443-2-4 Se
  MANDATORY TRIGGERS: 系統設計說明書撰寫, 安全功能描述規範撰寫, 設計文件撰寫, 單線圖繪製, 加固建議實踐文件撰寫, SP-mapping, practices, Single-Line Diagram (SLD) Development, document, writing, single-line-diagram, SR-checklist, system.
  Use this skill for design documentation tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 設計文件撰寫

本 Skill 整合 4 個工程技能定義，提供設計文件撰寫的完整工作流程。
適用領域：Documentation（D09）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D01-003, SK-D01-007, SK-D01-010, SK-D01-014, SK-D01-016

---

## 1. 輸入

- Zone/Conduit architecture diagram and specification (from SK-D01-001: Zone/Conduit Architecture Design)
- Security requirements and security level allocations (from SK-D01-003: Security Requirements Specification)
- OT network topology and interconnection design (from SK-D02-001: OT Network Topology Design)
- Data flow diagrams and communication protocols (from SK-D02-004: Data Flow Diagram Development)
- Control system functional design and logic documents (from SK-D05-001: Control System Functional Specification)
- Panel layout, SCADA HMI, and graphical interface designs (from SK-D06-001: Panel Layout and Design Specification)
- FR/SR mapping matrix (from SK-D01-007) — defines which SRs apply per zone and their target SL
- Zone/Conduit architecture (from SK-D01-001) — security topology being described
- Detailed risk assessment results (from SK-D01-007) — countermeasure specifications per risk
- Endpoint hardening design (from SK-D01-019) — hardening configurations to document
- Account and access control design (from SK-D01-020) — RBAC framework to document
- Security patch management design (from SK-D01-021) — patch procedures to document

---

## 2. 工作流程

### Step 1: 系統設計說明書撰寫
**SK 來源**：SK-D09-001 — System Design Description Writing

執行系統設計說明書撰寫：This skill encompasses the authoring of a comprehensive System Design Description (SDD) document that consolidates the outputs of security architectur

**本步驟交付物**：
- System Design Description (SDD) document: consolidated master reference organized per IEEE 1016 sections (system overview, design rationale, decomposi
- Design traceability matrix: mapping requirements → architecture → components → implementation
- Consolidated design review matrix: showing all design review findings, resolutions, and approval signatures

### Step 2: 安全功能描述規範撰寫
**SK 來源**：SK-D09-002 — Security Functional Description Specification

執行安全功能描述規範撰寫：Author the Security Functional Description Specification (SFDS) document that maps IEC 62443-2-4 Service Provider (SP) requirements to the specific im

**本步驟交付物**：
- Security Functional Description Specification Document (per ID12 exemplar format):
- Document structure following IEC 62443-2-4 SP category organization:
- SP.01: Solution staffing and qualifications

### Step 3: 單線圖繪製
**SK 來源**：SK-D09-003 — Single-Line Diagram (SLD) Development

執行單線圖繪製：Develop single-line diagrams representing the electrical power distribution system including switchgear, transformers, generators, loads, protection d

**本步驟交付物**：
- Single-Line Diagram in CAD format (dwg, pdf) or vector format (visio, draw.io) with all major electrical components represented
- Equipment schedule/bill of materials cross-referenced to SLD (component ID, rating, settings)
- SLD legend and notation key per IEEE Std 91 or IEC 60617 standard

### Step 4: 加固建議實踐文件撰寫
**SK 來源**：SK-D09-009 — Hardening Recommended Practices Document

執行加固建議實踐文件撰寫：This skill encompasses the authoring of a comprehensive Hardening Recommended Practices document that provides device-specific and system-specific har

**本步驟交付物**：
- Hardening Recommended Practices Document: comprehensive guide organized by device/system type (OS hardening, application hardening, network device har
- Hardening Configuration Baselines: templates and parameter tables for each device type, showing "hardened" vs. "standard" settings with justification
- Device-Specific Hardening Checklists: per-device-type implementation checklists with step-by-step procedures, prerequisites, and verification steps

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | System Design Description (SDD) document: consolidated master reference organized per IEEE 1016 sections (system overview, design rationale, decomposi | 依需求 |
| 2 | Design traceability matrix: mapping requirements → architecture → components → implementation | Markdown |
| 3 | Consolidated design review matrix: showing all design review findings, resolutions, and approval signatures | Markdown |
| 4 | Design baseline release notes: version control, change history, and design baseline approval record | 依需求 |
| 5 | Integration checklist: verification that all design elements are complete, consistent, and ready for implementation phase | Markdown |
| 6 | Security Functional Description Specification Document (per ID12 exemplar format): | 依需求 |
| 7 | Document structure following IEC 62443-2-4 SP category organization: | 依需求 |
| 8 | SP.01: Solution staffing and qualifications | 依需求 |
| 9 | SP.02: Architecture design and engineering | 依需求 |
| 10 | SP.03: System hardening and configuration | 依需求 |
| 11 | SP.04: Wireless network security | 依需求 |
| 12 | Single-Line Diagram in CAD format (dwg, pdf) or vector format (visio, draw.io) with all major electrical components represented | 依需求 |

---

## 4. 適用標準

- IEEE 1016: Standard for Information Technology—Systems and Software Engineering—Systems and Software Design Documentatio
- ISO/IEC/IEEE 42010: Systems and software engineering—Architecture description
- IEC 62443-3-2: Security Risk Assessment and Countermeasure Implementation
- IEC 62443-3-3: System security requirements and security levels (requirements traceability)
- IEC 61508: Functional safety of electrical/electronic/programmable electronic safety-related systems (safety design docu
- IEC 62443-2-4: Security Program Requirements for IACS Service Providers — defines the SP requirement framework being map
- IEC 62443-3-3: System Security Requirements and Security Levels — SR categories mapped to SP implementation
- IEC 62443-4-2: Technical Security Requirements for IACS Components — device-level implementation references
- GOV-SD: SFDS feeds SR checklist for Gate 3 — design specification must demonstrate how each SR is addressed; SR status (
- IEC 60617: Graphical Symbols for Electrical and Electronics Diagrams — primary standard for SLD notation

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | SDD document is organized per IEEE 1016 structure and includes all mandatory sec | ✅ 已驗證 |
| 2 | Every requirement from the Security Requirements Specification (SK-D01-003) is t | ✅ 已驗證 |
| 3 | All architecture diagrams (Zone/Conduit, network topology, functional decomposit | ✅ 已驗證 |
| 4 | SDD covers 100% of the Bill of Materials (BOM) components with specifications, c | ✅ 已驗證 |
| 5 | Design review findings from all design gate reviews are documented, with resolut | ✅ 已驗證 |
| 6 | SDD has been formally reviewed and approved by SAC, SYS, and QAM, with signature | ✅ 已驗證 |
| 7 | SFDS covers 100% of applicable IEC 62443-2-4 SP requirements: every SP category  | ✅ 已驗證 |
| 8 | Each applicable SP requirement has: implementation description, evidence referen | ✅ 已驗證 |
| 9 | N/A determinations include documented rationale: why the SP requirement does not | ✅ 已驗證 |
| 10 | Zone-specific variations documented: where SR implementation differs by zone SL, | ✅ 已驗證 |
| 11 | SR checklist extractable from SFDS: every applicable SR has a clear status (Impl | ✅ 已驗證 |
| 12 | SFDS reviewed and approved by Security Engineering Role and Design QA Role; cros | ✅ 已驗證 |
| 13 | SLD covers 100% of electrical components in the system architecture: transformer | ✅ 已驗證 |
| 14 | All major electrical components are labeled with consistent nomenclature (compon | ✅ 已驗證 |
| 15 | SLD notation conforms to IEEE Std 91 or IEC 60617 standard; deviations documente | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D09-001 | | Junior (< 2 yr) | 12–16 person-days | Assumes single-site, 50–100 components, greenfield; includes |
| SK-D09-001 | | Senior (5+ yr) | 5–8 person-days | Same scope; senior leverages templates, can rapidly integrate m |
| SK-D09-001 | Notes: Brownfield projects with complex legacy interfaces may require 1.5–2× effort. Multi-site proj |
| SK-D09-002 | | Junior (< 2 yr) | 20–30 person-days | Assumes ~200 applicable SP requirements, 5–8 zones, medium-c |
| SK-D09-002 | | Senior (5+ yr) | 12–18 person-days | Same scope; senior leverages reusable SP implementation descr |
| SK-D09-003 | | Junior (< 2 yr) | 5–8 person-days | Assumes single-site radial or simple looped distribution syste |
| SK-D09-003 | | Senior (5+ yr) | 2–3 person-days | Same scope; senior leverages standard templates and prior proje |
| SK-D09-003 | Notes: Complex meshed networks or multi-site systems scale effort linearly. Integration of SCADA mon |

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
設計文件撰寫已完成。
📋 執行範圍：4 個工程步驟（SK-D09-001, SK-D09-002, SK-D09-003, SK-D09-009）
📊 交付物清單：
  - System Design Description (SDD) document: consolidated master reference organized per IEEE 1016 sections (system overview, design rationale, decomposi
  - Design traceability matrix: mapping requirements → architecture → components → implementation
  - Consolidated design review matrix: showing all design review findings, resolutions, and approval signatures
  - Design baseline release notes: version control, change history, and design baseline approval record
  - Integration checklist: verification that all design elements are complete, consistent, and ready for implementation phase
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
| SK 覆蓋 | SK-D09-001, SK-D09-002, SK-D09-003, SK-D09-009 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D09-001 | System Design Description Writing | 系統設計說明書撰寫 | This skill encompasses the authoring of a comprehensive Syst |
| SK-D09-002 | Security Functional Description Specification | 安全功能描述規範撰寫 | Author the Security Functional Description Specification (SF |
| SK-D09-003 | Single-Line Diagram (SLD) Development | 單線圖繪製 | Develop single-line diagrams representing the electrical pow |
| SK-D09-009 | Hardening Recommended Practices Document | 加固建議實踐文件撰寫 | This skill encompasses the authoring of a comprehensive Hard |

<!-- Phase 5 Wave 2 deepened: SK-D09-001, SK-D09-002, SK-D09-003, SK-D09-009 -->