---
name: design-review-governance
description: >
  設計審查治理 — 涵蓋設計審查清單建立、關鍵安全設計審查、閘門審查治理、設計品質驗證及變更影響分析。
  MANDATORY TRIGGERS: 設計審查, design review, Gate review, 閘門審查, 設計品質, design quality, 變更影響, change impact, RTM, 追溯性
  Use this skill for design review governance tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 設計審查治理 Design Review Governance

本 Skill 整合 5 個工程技能定義，提供設計審查與治理的完整工作流程。
適用領域：Governance & Process（D11）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方 §1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認 SK-D01-001, SK-D02-001, SK-D02-004, SK-D02-012, SK-D10-002 產出已可用

---

## 1. 輸入

- IEC 62443 系列安全需求 (ID01, ID02, ID03, ID04)
- 工程領域標準與設計實務 (IEEE Std 1012, domain-specific codes)
- 專案設計標準與客戶需求 (SOW, design guidelines)
- 已核准之安全功能描述規格 (SFDS) 及安全需求追溯矩陣
- Zone/Conduit 架構圖、網路拓撲與資料流圖
- 歷史設計缺陷資料與品質指標
- 變更請求及其安全影響評估結果 (from SK-D10-002)

---

## 2. 工作流程

### Step 1 — 設計審查清單建立 (SK-D11-001)

| 項目 | 內容 |
|------|------|
| 目的 | 建立涵蓋完整性、正確性、一致性與合規性的標準化審查清單 |
| 範圍 | 所有工程領域 D01–D12，驗證類別 C.1–C.8 (ID02 Annex C) |
| 執行者 | Governance Lead / Domain Lead |

**交付物**：設計審查清單範本、各工程領域專用清單 (D01–D12)、驗證類別清單 C.1–C.8、清單使用指引

**常見陷阱**：清單項目過於模糊 → 須使用可量測判定標準；未涵蓋 C.6 安全需求 → 須對照 SFDS 逐項確認

### Step 2 — 關鍵安全設計審查 (SK-D11-003)

| 項目 | 內容 |
|------|------|
| 目的 | 驗證安全需求正確轉換為設計、維持縱深防禦原則 |
| 依據 | IEC 62443-3-2 §7.3.2 |
| 執行者 | SAC / Senior Security Architect |

**交付物**：關鍵安全設計審查報告（範圍、SFDS 驗證結果、發現與風險評等）、更新後 RTM、縱深防禦評估、SAC 與 PE/O 簽核

**常見陷阱**：僅檢查功能面忽略縱深防禦；密碼學設計未審查金鑰管理與 crypto-agility

### Step 3 — 閘門審查治理 (SK-D11-017)

| 項目 | 內容 |
|------|------|
| 目的 | 治理 Gate 0–3 四階段審查，驗證阻斷條件並授權階段轉換 |
| 依據 | GOV-SD stage-gate process |
| 執行者 | Head of System Design |

**交付物**：各 Gate 審查記錄、阻斷條件驗證矩陣、階段轉換授權記錄、例外升級結果 (L1-L2-L3)

| Gate | 要點 |
|------|------|
| Gate 0 | 5 必要輸入 + 4 品質門檻 |
| Gate 1 | Lite/Complete 路徑選擇、TRA 驗證 |
| Gate 2 | 變更觸發、SLDR 更新 |
| Gate 3 | 12 項交付清單、20% 抽樣驗證、殘餘風險接受 |

### Step 4 — 設計品質與追溯性驗證 (SK-D11-018)

| 項目 | 內容 |
|------|------|
| 目的 | 驗證設計文件品質與需求追溯完整性 |
| 執行時機 | R1 設計基線驗證、R3 交付前驗證 |
| 執行者 | Design QA (GOV-SDP) |

**交付物**：設計品質驗證報告（追溯矩陣完整性、文件登記稽核、審查發現關閉驗證、驗收標準滿足檢查、品質指標）

### Step 5 — 設計變更影響分析 (SK-D11-020)

| 項目 | 內容 |
|------|------|
| 目的 | 分析設計變更的安全影響，判定是否需 SL-T 重新評估或重認證 |
| 觸發 | SK-D10-002 識別安全影響時 |
| 執行者 | SAC |

**交付物**：SL 決策記錄（變更 ID、影響分析、SL-T 變更建議、Zone/Conduit 重設計需求、資料流影響、重認證範圍）

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | 設計審查清單範本與領域專用清單 | Markdown / Excel |
| 2 | 關鍵安全設計審查報告 | Markdown |
| 3 | 需求追溯矩陣 (RTM) 更新 | Excel |
| 4 | Gate 審查記錄與阻斷條件驗證矩陣 | Markdown |
| 5 | 設計品質驗證報告 | Markdown |
| 6 | SL 決策記錄 | Markdown |

---

## 4. 適用標準

- IEC 62443-3-2 §7.3.2 — 安全設計審查與核准
- ID02 Annex C — 設計驗證清單 C.1–C.8
- IEEE Std 1012 — 軟體驗證與確認
- ISO/IEC/IEEE 42010 — 架構描述與驗證框架
- GOV-SD — 階段閘門治理流程

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | 審查清單覆蓋所有工程領域 D01–D12 | 各領域至少一份清單 |
| 2 | 清單對應驗證類別 C.1–C.8 | 100% 對應或記錄例外 |
| 3 | SFDS 所有安全需求已對應設計元素 | RTM 100% 覆蓋 |
| 4 | 無未處理之 Critical 發現 | Fail → Pass 或 Conditional Pass |
| 5 | 縱深防禦評估通過 | 無單點故障依賴 |
| 6 | 密碼學設計已審查 | 含金鑰管理與 crypto-agility |
| 7 | Gate 0–3 阻斷條件清單已定義 | 每項含具體驗證標準 |
| 8 | 階段轉換經 Head of System Design 授權 | 簽核記錄完整 |
| 9 | Gate 3 抽樣驗證已記錄 | >=20% 抽樣率 |
| 10 | 追溯矩陣 100% 填充 | 無未追溯需求 |
| 11 | 文件登記稽核通過 | 版本一致、無孤立文件 |
| 12 | SL 決策記錄完整 | 含影響分析與重認證範圍 |
| 13 | SAC 與 PE/O 簽核完成 | 審查記錄含簽核 |

---

## 6. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 輸入完整性 | 所有必要輸入已讀取並摘要 |
| 2 | 流程覆蓋 | 5 個工作步驟皆已執行並有產出 |
| 3 | 輸出完整性 | 所有交付物已產出且非空白 |
| 4 | 標準合規 | 引用標準版本正確 |
| 5 | 跨步驟一致 | 各步驟產出間無矛盾 |
| 6 | 依賴追溯 | 外部依賴 SK 的輸入已驗證可用 |

---

## 7. 人類審核閘門

完成所有工作步驟後，**暫停**並向使用者提交審核：

```
設計審查治理已完成。
執行範圍：5 個工程步驟（SK-D11-001, SK-D11-003, SK-D11-017, SK-D11-018, SK-D11-020）
交付物：審查清單、安全設計審查報告、Gate 審查記錄、品質驗證報告、SL 決策記錄
待確認事項：{列出 TBD 項目或需人工判斷的假設}
請審核以上成果，確認 PASS / FAIL / PASS with Conditions。
```

判定：PASS（完整正確）/ FAIL（重大缺漏需返工）/ PASS with Conditions（需補充特定項目）

---

## 8. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 |
|--------|---------|---------|
| SK-D11-001 | Design Review Checklist Development | 設計審查清單建立 |
| SK-D11-003 | Critical Security Design Review | 關鍵安全設計審查 |
| SK-D11-017 | Gate Review Governance & Blocking Condition Verification | 閘門審查治理與阻斷條件驗證 |
| SK-D11-018 | Design Quality & Traceability Verification | 設計品質與追溯性驗證 |
| SK-D11-020 | Design Change Impact Analysis & SL Recertification | 設計變更影響分析與SL重認證 |
