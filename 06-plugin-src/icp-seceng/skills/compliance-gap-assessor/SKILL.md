---
name: compliance-gap-assessor
description: >
  Compliance gap analysis toolkit for IEC 62443, ISO 27001, and related cybersecurity frameworks.
  Generates structured gap matrices mapping current state vs. required controls, produces
  remediation roadmaps with effort/cost estimates, and tracks compliance progress across
  multiple frameworks with overlap detection. Supports both Presales-level quick assessment (±20%)
  and Implementation-level detailed assessment with evidence tracking.
  MANDATORY TRIGGERS: 合規差距分析, compliance gap analysis, IEC 62443 assessment,
  ISO 27001 gap, 合規矩陣, compliance matrix, gap assessment, 差距評估,
  security compliance audit, 資安合規稽核, framework gap, 框架差距,
  control mapping, 控制項對照, 合規評估, compliance assessment,
  IEC 62443 SL, security level assessment, 安全等級評估,
  Annex C checklist, 合規稽核, audit execution, 安全稽核,
  gate review compliance, 閘門審查合規, security management plan compliance.
  Use this skill whenever the user wants to assess compliance gaps against cybersecurity
  frameworks, generate gap matrices, or build remediation roadmaps for IT/OT infrastructure.
  For strategic compliance sequencing and budget justification, use ciso-advisor instead.
  For full presales proposal workflows, use presales instead.
---

# 合規差距評估器 (Compliance Gap Assessor)

針對 IEC 62443、ISO 27001 及相關資安框架的合規差距分析、矩陣生成與補救路線圖。
整合 SK-D01-011 (Gap Analysis)、SK-D01-012 (Audit Execution)、SK-D01-013 (Gate Review) 的領域知識。

## 適用範圍

電力、石油天然氣、水處理、製造業等 OT 環境的合規評估，以及 IT 環境的 ISO 27001 / SOC 2 差距分析。
精度定位：Presales 級快速評估 (±20%) 或 Implementation 級詳細評估。

---

## 0. 初始化與輸入確認

啟動本 Skill 後，先向用戶確認以下參數：

1. **評估模式**：Quick (Presales ±20%) 或 Detailed (Implementation 級)
2. **目標框架**：IEC 62443-3-3 / ISO 27001:2022 / NIST CSF 2.0 / SOC 2 / 多框架
3. **評估範圍**：系統邊界（SuC）、場域、組織邊界
4. **目標安全等級**（IEC 62443 限定）：SL-T 1~4
5. **現有文件**：是否提供了政策、程序、技術文件、稽核報告等
6. **輸出格式**：Markdown 報告 / Excel 矩陣 (.xlsx) / 兩者皆有

若用戶未指定，預設為：Quick 模式 + IEC 62443-3-3 + Markdown 輸出。

---

## 1. 支援框架

| 框架 | 版本 | 適用場景 | 控制項數量 |
|------|------|---------|----------|
| IEC 62443-3-3 | Ed. 1.0 | OT/ICS 系統安全需求 | 51 SRs (7 FRs) |
| IEC 62443-4-2 | Ed. 1.0 | OT 元件安全需求 | 對應 3-3 SRs |
| IEC 62443-2-1 | Ed. 1.0 | 安全管理系統 (CSMS) | Annex C C.1-C.8 |
| ISO 27001:2022 | Annex A | IT 資訊安全管理 | 93 controls (4 themes) |
| NIST CSF 2.0 | v2.0 | 通用網路安全框架 | 6 Functions, 22 Categories |
| SOC 2 | Type II | SaaS/服務提供商 | 5 Trust Service Criteria |

---

## 2. 差距評估工作流

### Phase 1: 範圍定義

1. 確認目標框架（可多框架）
2. 定義評估範圍（系統/場域/組織邊界）
3. 確認目標安全等級（IEC 62443: SL-T 1~4）
4. 收集現有文件（政策、程序、技術文件、稽核報告）
5. 確認 IEC 62443 lifecycle 階段（R1 baseline 或 R4 verification）

若用戶提供了現有文件，先閱讀並摘要關鍵控制項實施狀態。
若無文件輸入，以「全部未實作」為保守假設並註明。

### Phase 2: 控制項盤點

對每個控制項評估現況：

| 狀態 | 定義 | 分數 |
|------|------|------|
| ✅ Implemented | 完整實作並有證據 | 100% |
| 🟡 Partial | 部分實作或缺文件 | 50% |
| 🔴 Gap | 未實作 | 0% |
| ⬜ N/A | 不適用（附理由） | 排除 |

**Quick 模式**：僅評估 FR 層級（7 個 Functional Requirements），SR 層級以推論填入。
**Detailed 模式**：逐 SR 評估，每個 SR 需有證據引用或缺失說明。

### Phase 3: 差距矩陣生成

#### IEC 62443-3-3 差距矩陣模板

```markdown
| FR | SR | 控制項描述 | SL-1 | SL-2 | SL-3 | SL-4 | 現況 | 差距 | 補救措施 | 估計工時 | 優先級 |
|----|-----|----------|------|------|------|------|------|------|---------|---------|--------|
| FR1 | SR 1.1 | Human user identification and authentication | R | R | R | R | 🟡 | Partial | 部署 MFA | 40h | HIGH |
| FR1 | SR 1.2 | Software process and device identification | — | R | R | R | 🔴 | Gap | 實作設備憑證 | 80h | HIGH |
```

R = Required, — = Not required at this SL

#### ISO 27001:2022 差距矩陣模板

```markdown
| Theme | # | 控制項 | 適用 | 現況 | 差距 | 補救措施 | 估計工時 | 優先級 |
|-------|---|--------|------|------|------|---------|---------|--------|
| Organizational | A.5.1 | Policies for information security | ✅ | ✅ | — | — | — | — |
| People | A.6.1 | Screening | ✅ | 🟡 | Partial | 完善背景查核程序 | 20h | MEDIUM |
```

#### IEC 62443-2-1 Annex C 稽核矩陣模板 (SK-D01-012 整合)

```markdown
| Checklist | Item # | 稽核項目 | 現況 | 證據 | 發現 | 嚴重度 | 矯正措施 | 負責人 | 目標日期 |
|-----------|--------|---------|------|------|------|--------|---------|--------|---------|
| C.1 | C.1.1 | CSMS scope definition | ✅ | Policy doc v2.1 | — | — | — | — | — |
| C.2 | C.2.3 | Risk assessment methodology | 🟡 | Partial | 方法論已定義但未涵蓋 OT | MEDIUM | 擴展 RA 範圍 | SAC | 2026-Q3 |
```

### Phase 4: 補救路線圖

依優先級排序，產出分階段補救計畫：

```markdown
## 補救路線圖

### Phase 1: Quick Wins (0-3 個月)
- 現有控制項的文件補齊
- 政策/程序撰寫
- 基礎設定強化

### Phase 2: Core Controls (3-6 個月)
- 技術控制項實作
- 存取控制強化
- 監控機制建立

### Phase 3: Advanced Controls (6-12 個月)
- 進階安全機制
- 持續監控
- 稽核準備

| 階段 | 控制項數 | 估計工時 | 估計成本 | 完成後覆蓋率 |
|------|---------|---------|---------|------------|
```

### Phase 5: 閘門審查合規包 (SK-D01-013 整合)

若用戶的評估目的是準備閘門審查（Gate Review），額外產出：

```markdown
## Gate Review 合規就緒度檢查

| Gate | 必要交付物 | 現況 | 版本 | 負責人 | 就緒狀態 |
|------|-----------|------|------|--------|---------|
| Gate 0 | Security Management Plan | ✅ | v1.2 | SAC | Ready |
| Gate 1 | Preliminary TRA Report | 🟡 | Draft | STC | Pending Review |
| Gate 2 | Detailed Design Package | 🔴 | — | DES | Not Started |
| Gate 3 | FAT/SAT Records + Compliance Evidence | 🔴 | — | QA | Not Started |
```

---

## 3. 框架重疊偵測

當客戶需要同時符合多個框架時，識別重疊控制項以減少重複工作：

### IEC 62443 ↔ ISO 27001 對照表 (部分)

| IEC 62443 SR | ISO 27001 Control | 重疊程度 | 說明 |
|-------------|-------------------|---------|------|
| SR 1.1 Human user ID & auth | A.8.5 Secure authentication | HIGH | 核心認證需求相同 |
| SR 1.3 Account management | A.5.18 Access rights | HIGH | 帳號生命週期管理 |
| SR 2.1 Authorization enforcement | A.8.3 Information access restriction | HIGH | 存取控制 |
| SR 3.3 Security functionality verification | A.8.8 Management of technical vulnerabilities | MEDIUM | 範圍不同但互補 |
| SR 5.1 Network segmentation | A.8.22 Networks segregation | HIGH | 網路隔離 |
| SR 6.1 Audit log accessibility | A.8.15 Logging | HIGH | 日誌需求 |

---

## 4. 與其他 Skill 的協作

| 協作 Skill | 整合點 | 資料流向 |
|-----------|--------|---------|
| **ciso-advisor** | 合規路線圖的戰略優先級排序 | compliance-gap-assessor 矩陣 → ciso-advisor 排序/預算 |
| **presales T04** | 可行性評估中的合規差距 | compliance-gap-assessor 結果 → presales feasibility §2 |
| **senior-security** | 安全控制的技術實作細節 | compliance-gap-assessor 補救措施 → senior-security 實作 |
| **arch-diagram** | Zone/Conduit SL 標註 | compliance-gap-assessor SL 評估 → arch-diagram Zone SL |

---

## 5. 輸出格式

| 請求 | 產出 |
|------|------|
| 「做一個 IEC 62443 差距分析」 | FR/SR 差距矩陣 + 補救路線圖 |
| 「ISO 27001 合規評估」 | Annex A 差距矩陣 + 補救路線圖 |
| 「同時評估 62443 和 27001」 | 雙框架矩陣 + 重疊分析 + 合併路線圖 |
| 「合規現況報告」 | 執行摘要 + 覆蓋率儀表板 + 風險排序 |
| 「準備 Gate Review」 | 差距矩陣 + 閘門就緒度檢查 + 交付物缺口清單 |
| 「安全稽核」 | Annex C 稽核矩陣 + 發現清單 + 矯正措施追蹤 |

---

## 6. 品質檢查清單 (Quality Checklist)

完成差距評估後，Claude 自行驗證以下條件：

- [ ] 差距矩陣涵蓋目標框架的所有適用控制項（無遺漏）
- [ ] 每個差距項目有：現況狀態、差距描述、補救措施、估計工時、優先級
- [ ] 補救路線圖按優先級分階段，每階段有時程和預期覆蓋率
- [ ] Quick 模式：矩陣不超過 2 頁；Detailed 模式：每個 SR 有證據引用
- [ ] 無泛化語言（如「加強安全」）；所有差距和措施必須具體可量化
- [ ] 若為多框架評估，重疊偵測已執行且節省工時已計算
- [ ] 若為 Gate Review，閘門就緒度檢查表已包含且所有必要交付物已列出

---

## 7. 人類審核閘門 (Human Review Gate)

### 審核時機

差距矩陣與補救路線圖產出後，**必須提示用戶進行審核**：

```
合規差距評估已完成，請審核以下項目：
1. 差距矩陣的「現況」評估是否與實際狀態一致？
2. 補救措施的優先級排序是否符合組織策略？
3. 工時估計是否合理？
4. 是否有需要調整的 N/A 項目？

請確認後我將產出最終報告，或指出需要修正的項目。
```

### 審核標準

- **PASS**：用戶確認矩陣內容正確，或僅有 Minor 修正
- **FAIL**：用戶指出重大評估錯誤（如將已實作項目標為 Gap），需修正後重新審核
- **PASS with conditions**：用戶接受但要求補充特定項目

---

## 8. IEC 62443 Lifecycle 對應

| Lifecycle Stage | 本 Skill 角色 | 典型輸出 |
|----------------|-------------|---------|
| R1 (Security Requirements) | 建立合規基線 | 初始差距矩陣 + SL-T 對照 |
| R2 (Detailed Design) | 驗證設計合規性 | 設計階段差距更新 |
| R3 (Implementation) | 追蹤實作進度 | 控制項實作狀態追蹤 |
| R4 (Verification) | 執行合規驗證 | 最終差距矩陣 + 稽核報告 |
| R5 (Maintenance) | 持續合規監控 | 週期性差距評估更新 |

---

## 9. Source Traceability

- SK-D01-011: IEC 62443 Compliance Gap Analysis — 差距分析核心方法論
- SK-D01-012: Security Audit Execution — Annex C 稽核矩陣整合
- SK-D01-013: Gate Review Preparation — 閘門審查合規包整合
- SK-D01-029: Security Management Plan Development — 安全管理計畫合規基線
- ID01 §6.6.3, §7.8.3.1: IEC 62443-2-1 合規稽核程序要求
- ID02 C.1-C.8: IEC 62443-2-1 Annex C 驗證查核表
