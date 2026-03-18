---
name: system-decommissioning
description: >
  系統除役管理。
  Execute the secure decommissioning of OT/ICS systems from active operation per IEC 62443 lifecycle requirements (ID01 §6.5.3), ensuring no residual se
  MANDATORY TRIGGERS: 系統除役執行, 系統除役管理, credential-revocation, IEC-62443, System Decommissioning Execution, system decommissioning, decommissioning, lifecycle, data-destruction.
  Use this skill for system decommissioning tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 系統除役管理

本 Skill 整合 1 個工程技能定義，提供系統除役管理的完整工作流程。
適用領域：Project Engineering（D10）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-005, SK-D01-007, SK-D02-004, SK-D10-004, SK-D10-005

---

## 1. 輸入

- Approved decommissioning plan with sequencing schedule (from SK-D10-005: System Decommissioning Planning)
- Current system configuration documentation and asset inventory (from SK-D01-005: Asset Inventory Development)
- Active credential and certificate registry for the target system
- Vendor contract and license inventory for affected components
- Risk assessment for system removal impact (from SK-D01-007: Detailed Risk Assessment)
- Network dependency mapping showing interconnections with remaining systems (from SK-D02-004: Data Flow Diagram Development)

---

## 2. 工作流程

### Step 1: 系統除役執行
**SK 來源**：SK-D10-006 — System Decommissioning Execution

執行系統除役執行：Execute the secure decommissioning of OT/ICS systems from active operation per IEC 62443 lifecycle requirements (ID01 §6.5.3), ensuring no residual se

**本步驟交付物**：
- Data Destruction Certification Report: media type, destruction method (per NIST SP 800-88), verification evidence, chain of custody
- Credential and Certificate Revocation Log: revoked accounts, expired certificates, destroyed keys, timestamped confirmation
- Physical Equipment Removal Record: equipment ID, disposal method, receiving party, environmental compliance

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Data Destruction Certification Report: media type, destruction method (per NIST SP 800-88), verification evidence, chain of custody | Markdown |
| 2 | Credential and Certificate Revocation Log: revoked accounts, expired certificates, destroyed keys, timestamped confirmation | 依需求 |
| 3 | Physical Equipment Removal Record: equipment ID, disposal method, receiving party, environmental compliance | 依需求 |
| 4 | System Archive Package: final configuration snapshots, operational history, maintenance records for long-term retention | 依需求 |
| 5 | Post-Decommissioning Security Verification Report: scan results confirming zero residual access vectors | Markdown |
| 6 | Updated asset inventory reflecting removed systems | 依需求 |

---

## 4. 適用標準

- IEC 62443-2-1: Security Management System — decommissioning procedures
- IEC 62443-2-4: Security Program Requirements for IACS Service Providers — secure disposal requirements
- NIST SP 800-88 Rev. 1: Guidelines for Media Sanitization — data destruction methods and verification
- NIST SP 800-82 Rev. 3: Guide to OT Security — lifecycle management guidance
- Local regulatory requirements for hazardous material disposal and data privacy

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | All sensitive data on decommissioned systems is irrecoverably destroyed with doc | ✅ 已驗證 |
| 2 | 100% of system credentials, certificates, and cryptographic keys are revoked and | ✅ 已驗證 |
| 3 | Post-decommissioning network scan confirms zero residual access vectors from rem | ✅ 已驗證 |
| 4 | Physical equipment is securely removed and disposed per applicable regulatory an | ✅ 已驗證 |
| 5 | Complete system archive package is produced and stored in designated long-term r | ✅ 已驗證 |
| 6 | Updated asset inventory accurately reflects the removal of all decommissioned co | ✅ 已驗證 |
| 7 | All vendor licenses and support contracts for decommissioned systems are deactiv | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D10-006 | | Junior (< 2 yr) | 5–8 person-days | Single system, standard IT/OT equipment; requires senior overs |
| SK-D10-006 | | Senior (5+ yr) | 2–4 person-days | Same scope; experienced with media sanitization standards and c |

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
系統除役管理已完成。
📋 執行範圍：1 個工程步驟（SK-D10-006）
📊 交付物清單：
  - Data Destruction Certification Report: media type, destruction method (per NIST SP 800-88), verification evidence, chain of custody
  - Credential and Certificate Revocation Log: revoked accounts, expired certificates, destroyed keys, timestamped confirmation
  - Physical Equipment Removal Record: equipment ID, disposal method, receiving party, environmental compliance
  - System Archive Package: final configuration snapshots, operational history, maintenance records for long-term retention
  - Post-Decommissioning Security Verification Report: scan results confirming zero residual access vectors
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
| Domain | D10 (Project Engineering) |
| SK 覆蓋 | SK-D10-006 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D10-006 | System Decommissioning Execution | 系統除役執行 | Execute the secure decommissioning of OT/ICS systems from ac |

<!-- Phase 5 Wave 2 deepened: SK-D10-006 -->