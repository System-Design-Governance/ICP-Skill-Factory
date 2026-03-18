---
name: site-assessment
description: >
  現場評估與基礎設施。
  Conduct on-site survey of the project location to assess physical environment, infrastructure constraints, and operational conditions that impact syst。Identify, document, and catalog the existing infrastructure at the project site, covering automatio
  MANDATORY TRIGGERS: 現場評估與基礎設施, 現場勘查與限制條件文件, 既有基礎設施清冊, NDA 與保密協議管理, physical-environment, contract-management, Site Survey and Constraint Documentation, NDA, feasibility-input, site assessment, site-assessment, asset-discovery.
  Use this skill for site assessment tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 現場評估與基礎設施

本 Skill 整合 3 個工程技能定義，提供現場評估與基礎設施的完整工作流程。
適用領域：Pre-Gate & Presales（D14）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-033, SK-D14-001

---

## 1. 輸入

- Customer/employer site access arrangements and safety requirements
- Project scope and general requirements (from SK-D14-001)
- Available site documentation (floor plans, cabinet layouts, cable routes, electrical diagrams)
- Site survey checklist (physical, environmental, network, safety categories)
- Previous site survey reports (if brownfield with prior work)
- Customer/employer site documentation: as-built drawings, equipment lists, network diagrams, maintenance records
- Site survey access (from SK-D14-011 — often conducted in the same site visit)
- Customer/employer technical contacts for equipment identification
- Vendor documentation for existing systems (model numbers, firmware versions where accessible)
- ICP standard NDA template (ID25, Tier 3: MF-AM-07-09 Mutual Non-Disclosure Agreement)
- Customer/employer proposed NDA (if customer-initiated)
- Project scope description (from SK-D14-001 or preliminary engagement terms)

---

## 2. 工作流程

### Step 1: 現場勘查與限制條件文件
**SK 來源**：SK-D14-011 — Site Survey and Constraint Documentation

執行現場勘查與限制條件文件：Conduct on-site survey of the project location to assess physical environment, infrastructure constraints, and operational conditions that impact syst

**本步驟交付物**：
- Site Survey Report:
- Physical environment assessment: building layout, room dimensions, cabinet space availability, floor loading capacity, cable routing options
- Environmental conditions: temperature/humidity ranges, dust/contamination levels, vibration exposure, EMI sources

### Step 2: 既有基礎設施清冊
**SK 來源**：SK-D14-012 — Existing Infrastructure Inventory

執行既有基礎設施清冊：Identify, document, and catalog the existing infrastructure at the project site, covering automation systems, network equipment, servers, security app

**本步驟交付物**：
- Existing Infrastructure Inventory Register:
- Automation systems: PLCs/RTUs, HMIs, SCADA servers, historians, engineering workstations — manufacturer, model, firmware version, age
- Network equipment: switches, routers, firewalls, media converters — manufacturer, model, configuration status (managed/unmanaged)

### Step 3: NDA 與保密協議管理
**SK 來源**：SK-D14-017 — NDA and Confidentiality Agreement Management

執行NDA 與保密協議管理：Manage the preparation, review, execution, and tracking of Non-Disclosure Agreements (NDAs) and confidentiality agreements required before sensitive p

**本步驟交付物**：
- Executed NDA Register: tracking table of all NDAs with: parties, effective date, expiry date, scope of information covered, special terms, status (Dra
- NDA Scope Customization Notes: per-agreement documentation of scope adjustments from standard template (if any)
- Obligation Tracking Calendar: NDA expiry alerts, renewal requirements, information return/destruction obligations post-expiry

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Site Survey Report: | Markdown |
| 2 | Physical environment assessment: building layout, room dimensions, cabinet space availability, floor loading capacity, cable routing options | 依需求 |
| 3 | Environmental conditions: temperature/humidity ranges, dust/contamination levels, vibration exposure, EMI sources | 依需求 |
| 4 | Electrical infrastructure: power supply availability, UPS capacity, grounding quality, cable tray capacity | 依需求 |
| 5 | Network infrastructure: existing cable plant, fiber routes, wireless coverage, patch panel availability | 依需求 |
| 6 | Physical security: access control to equipment rooms, CCTV coverage, perimeter security | 依需求 |
| 7 | Existing Infrastructure Inventory Register: | 依需求 |
| 8 | Automation systems: PLCs/RTUs, HMIs, SCADA servers, historians, engineering workstations — manufacturer, model, firmware version, age | 依需求 |
| 9 | Network equipment: switches, routers, firewalls, media converters — manufacturer, model, configuration status (managed/unmanaged) | 依需求 |
| 10 | Server infrastructure: physical/virtual servers, operating systems, virtualization platforms | 依需求 |
| 11 | Communication infrastructure: cable plant type (copper/fiber), cable routes, patch panels, wireless APs | 依需求 |
| 12 | Security appliances: existing firewalls, IDS/IPS, antivirus servers, SIEM (if any) | 依需求 |

---

## 4. 適用標準

- IEC 62443-3-2: Security Risk Assessment — physical security considerations for zone/conduit design
- IEC 61511: Functional Safety — safety system zone identification (supplementary)
- Local building codes and safety regulations
- GOV-SD: Pre-Gate 0 — site survey findings feed feasibility assessment, which is one of the 5 Gate 0 inputs
- IEC 62443-3-2: Security Risk Assessment — existing system characterization as input to zone/conduit methodology
- IEC 62443-2-4: SP.02.01 — system architecture documentation including existing infrastructure
- GOV-SD: Pre-Gate 0 — existing infrastructure baseline feeds feasibility assessment and concept architecture, both Gate 0
- ID25 (Tier 3): MF-AM-07-09 Mutual Non-Disclosure Agreement — ICP standard NDA template
- ISO 27001 Annex A.13.2: Information transfer — confidentiality agreements for information exchange
- GOV-SD: Pre-Gate 0 — NDA execution should precede technical information exchange; part of engagement initiation

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Site survey report covers all six assessment categories: physical, environmental | ✅ 已驗證 |
| 2 | Constraint register produced with minimum 10 documented constraints (for a typic | ✅ 已驗證 |
| 3 | Photographic evidence captured for all Hard severity constraints — annotated pho | ✅ 已驗證 |
| 4 | Environmental conditions documented with measured values (temperature range, hum | ✅ 已驗證 |
| 5 | Site access requirements documented for subsequent visits — logistics informatio | ✅ 已驗證 |
| 6 | Survey findings directly usable as input to feasibility assessment (SK-D14-003 ⏳ | ✅ 已驗證 |
| 7 | Inventory register covers all six infrastructure categories: automation, network | ✅ 已驗證 |
| 8 | Every identified item has: location, manufacturer, model, condition assessment,  | ✅ 已驗證 |
| 9 | End-of-life risk register produced: all equipment past or within 2 years of end- | ✅ 已驗證 |
| 10 | Integration impact assessment completed: existing infrastructure compatibility w | ✅ 已驗證 |
| 11 | Gap summary identifies infrastructure categories requiring new deployment — suff | ✅ 已驗證 |
| 12 | Inventory register format compatible with SK-D01-005 (Asset Inventory Developmen | ✅ 已驗證 |
| 13 | NDA register maintained: all active NDAs tracked with parties, dates, scope, and | ✅ 已驗證 |
| 14 | NDA executed before technical information exchange begins — compliance verified  | ✅ 已驗證 |
| 15 | NDA scope covers all categories of sensitive information to be exchanged (techni | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D14-011 | | Junior (< 2 yr) | 3–5 person-days | Assumes single-site survey, 1 day on-site + 2–4 days documenta |
| SK-D14-011 | | Senior (5+ yr) | 2–3 person-days | Same scope; senior conducts efficient focused survey with rapid |
| SK-D14-011 | Notes: Multi-site projects require one survey per site. Remote/international sites add travel time.  |
| SK-D14-012 | | Junior (< 2 yr) | 3–5 person-days | Assumes single-site, ~50–100 existing devices; includes on-sit |
| SK-D14-012 | | Senior (5+ yr) | 2–3 person-days | Same scope; senior conducts efficient focused assessment with r |
| SK-D14-012 | Notes: Effort scales with site size and equipment count. Large industrial sites with hundreds of leg |
| SK-D14-017 | | Junior (< 2 yr) | 1–2 person-days | Assumes standard bilateral NDA using ICP template; includes pr |
| SK-D14-017 | | Senior (5+ yr) | 0.5–1 person-days | Same scope; senior handles standard NDAs efficiently | |

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
現場評估與基礎設施已完成。
📋 執行範圍：3 個工程步驟（SK-D14-011, SK-D14-012, SK-D14-017）
📊 交付物清單：
  - Site Survey Report:
  - Physical environment assessment: building layout, room dimensions, cabinet space availability, floor loading capacity, cable routing options
  - Environmental conditions: temperature/humidity ranges, dust/contamination levels, vibration exposure, EMI sources
  - Electrical infrastructure: power supply availability, UPS capacity, grounding quality, cable tray capacity
  - Network infrastructure: existing cable plant, fiber routes, wireless coverage, patch panel availability
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
| Domain | D14 (Pre-Gate & Presales) |
| SK 覆蓋 | SK-D14-011, SK-D14-012, SK-D14-017 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D14-011 | Site Survey and Constraint Documentation | 現場勘查與限制條件文件 | Conduct on-site survey of the project location to assess phy |
| SK-D14-012 | Existing Infrastructure Inventory | 既有基礎設施清冊 | Identify, document, and catalog the existing infrastructure  |
| SK-D14-017 | NDA and Confidentiality Agreement Management | NDA 與保密協議管理 | Manage the preparation, review, execution, and tracking of N |

<!-- Phase 5 Wave 2 deepened: SK-D14-011, SK-D14-012, SK-D14-017 -->