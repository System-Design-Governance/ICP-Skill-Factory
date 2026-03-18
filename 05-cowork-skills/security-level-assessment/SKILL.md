---
name: security-level-assessment
description: >
  安全等級評估。
  Assess and assign Security Level Targets (SL-T) to each zone/conduit in the architecture per IEC 62443-3-3. SL-T defines the required security capabil
  MANDATORY TRIGGERS: 安全等級目標評估, 安全等級評估, SL-T Assessment, IEC 62443-3-3, Security Level Target (SL-T) Assessment, Security Level Target, security level assessment, Zone/Conduit Security, SL Decision Lifecycle.
  Use this skill for security level assessment tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 安全等級評估

本 Skill 整合 1 個工程技能定義，提供安全等級評估的完整工作流程。
適用領域：OT Cybersecurity（D01）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-006

---

## 1. 輸入

- Zone/Conduit architecture diagram (from SK-D01-001 or contemporaneous)
- Risk assessment findings (from SK-D01-006 or earlier risk analysis)
- IEC 62443-3-3 requirements and guidance
- Criticality and consequence analysis for each zone
- SL Decision Lifecycle process documentation
- Stakeholder risk tolerance and business impact constraints

---

## 2. 工作流程

### Step 1: 安全等級目標評估
**SK 來源**：SK-D01-010 — Security Level Target (SL-T) Assessment

執行安全等級目標評估：Assess and assign Security Level Targets (SL-T) to each zone/conduit in the architecture per IEC 62443-3-3. SL-T defines the required security capabil

**本步驟交付物**：
- SL-T Baseline Document
- SL-T assignment for each zone (SL-T 0 through SL-T 4)
- Justification for each SL-T assignment (linked to risk and consequence)

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | SL-T Baseline Document | 依需求 |
| 2 | SL-T assignment for each zone (SL-T 0 through SL-T 4) | 依需求 |
| 3 | Justification for each SL-T assignment (linked to risk and consequence) | 依需求 |
| 4 | SL-T matrix mapping zones to target levels | Markdown |
| 5 | Verification records (stakeholder sign-offs at each lifecycle stage) | 依需求 |
| 6 | SL Decision Lifecycle audit trail (initial → verified → updated → final) | 依需求 |

---

## 4. 適用標準

- IEC 62443-3-3 (Security for industrial automation and control systems – System security requirements and security levels
- IEC 62443-3-2 (Risk assessment and security classification)
- IEC 62443-1-1 (Concepts and models)
- GOV-SD SL Decision Lifecycle process

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Each zone in the architecture has an assigned SL-T (0 through 4) documented in t | ✅ 已驗證 |
| 2 | Each SL-T assignment is justified by explicit reference to risk level, consequen | ✅ 已驗證 |
| 3 | Justifications clearly link zone criticality, potential impact (safety, business | ✅ 已驗證 |
| 4 | The SL Decision Lifecycle is documented with evidence of progression through ini | ✅ 已驗證 |
| 5 | Stakeholder sign-offs are collected and recorded at the verified and final stage | ✅ 已驗證 |
| 6 | Any SL-T escalation or de-escalation decisions are documented with rationale and | ✅ 已驗證 |
| 7 | The SL-T Baseline is approved in writing by the Security Architect and at least  | ✅ 已驗證 |
| 8 | The SL-T assignment aligns with IEC 62443-3-3 target selection guidance (e.g., n | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D01-010 | | Security Architect | 20 hours | 10 hours | Lead assessment; senior role leverages IEC 62443-3-3 ex |
| SK-D01-010 | | Risk Manager | 8 hours | 4 hours | Risk and consequence input | |
| SK-D01-010 | | Zone Owner/Stakeholder | 12 hours | 8 hours | Per zone; multiple stakeholders may be involved | |
| SK-D01-010 | | Verification Lead | 6 hours | 4 hours | Lifecycle stage verification | |
| SK-D01-010 | | **Total** | **46 hours** | **26 hours** | Highly dependent on architecture complexity and number o |

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
安全等級評估已完成。
📋 執行範圍：1 個工程步驟（SK-D01-010）
📊 交付物清單：
  - SL-T Baseline Document
  - SL-T assignment for each zone (SL-T 0 through SL-T 4)
  - Justification for each SL-T assignment (linked to risk and consequence)
  - SL-T matrix mapping zones to target levels
  - Verification records (stakeholder sign-offs at each lifecycle stage)
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
| SK 覆蓋 | SK-D01-010 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D01-010 | Security Level Target (SL-T) Assessment | 安全等級目標評估 | Assess and assign Security Level Targets (SL-T) to each zone |

<!-- Phase 5 Wave 2 deepened: SK-D01-010 -->