# 第二輪一致性鑑識報告

**報告日期**：2026-02-08
**鑑識範圍**：語意一致性檢查（Phase 1 & 2 已完成）
**權威來源**：02-dataverse-data-model-and-security.md、05-core-flows-implementation-runbook.md

---

## 執行摘要

- **總問題數**：39
- **P0（阻斷上線）**：2
- **P1（高風險）**：31
- **P2（中風險）**：3

---

## 問題清單

### ISSUE-R2-001: 使用已淘汰的專案狀態

**風險等級**：P0（阻斷上線）

**問題描述**：
以下文件仍使用已被淘汰的專案狀態（Draft/Completed/Cancelled），與治理決策不一致。

**影響範圍**：

#### 04-powerapps-forms.md

| 行號 | 已淘汰狀態 | 正確狀態 | 上下文 |
|-----|----------|---------|--------|
| 1290 | `Completed` | `Closed` |   ``` ddClosureType.Items = ["Completed", "Cancell... |
| 1290 | `Cancelled` | `Terminated` | reType.Items = ["Completed", "Cancelled", "OnHold"... |

**修正建議**：

- **Completed** → `Closed`
  - 原因：術語一致性，對齊 02 文件權威定義
  - OptionSet 值：100000002
- **Cancelled** → `Terminated`
  - 原因：明確區分正常結案與異常終止
  - OptionSet 值：100000003

#### 07-testing-and-acceptance.md

| 行號 | 已淘汰狀態 | 正確狀態 | 上下文 |
|-----|----------|---------|--------|
| 20 | `Draft` | `PreGate0 (Active + Pending)` | V** | 開發測試 | dev-governance | Draft | 開發人員 | | **Q... |
| 655 | `Completed` | `Closed` | ion Log | | RollbackStatus | `Completed` | Governa... |
| 1497 | `Completed` | `Closed` | Write-Host "Test data cleanup completed." ```  ---... |

**修正建議**：

- **Completed** → `Closed`
  - 原因：術語一致性，對齊 02 文件權威定義
  - OptionSet 值：100000002
- **Draft** → `PreGate0 (Active + Pending)`
  - 原因：專案一旦建立即進入治理範圍，不存在草稿狀態
  - OptionSet 值：N/A (使用 Active + currentgate = Pending 組合)

### ISSUE-R2-002: 仍使用 cr_ Prefix

**風險等級**：P1（高風險）

**問題描述**：
以下文件仍使用 cr_ prefix，應替換為 gov_。

#### 07-testing-and-acceptance.md

- **總計**：27 處

**範例**（前 5 處）：

| 行號 | 舊引用 | 正確引用 |
|-----|--------|---------|
| 149 | `cr_projectregistries` | `gov_projectregistries` |
| 149 | `cr_requestid` | `gov_requestid` |
| 149 | `cr_requestid` | `gov_requestid` |
| 149 | `cr_currentgate` | `gov_currentgate` |
| 149 | `cr_projectstatus` | `gov_projectstatus` |
| ... | ... | ... |

**修正方式**：執行 `fix_05_document.py` 腳本進行批次替換

### ISSUE-R2-003: 仍使用 900000000 系列 OptionSet 值

**風險等級**：P1（高風險）

**問題描述**：
以下文件仍使用 900000000 系列 OptionSet 值，應替換為 100000000 系列。

#### 07-testing-and-acceptance.md

- **總計**：4 處

**範例**（前 5 處）：

| 行號 | 舊值 | 新值 |
|-----|------|------|
| 639 | `900000002` | `100000002` |
| 643 | `900000002` | `100000002` |
| 667 | `900000000` | `100000000` |
| 701 | `900000001` | `100000001` |

**修正方式**：執行 `fix_05_document.py` 腳本進行批次替換

### ISSUE-R2-004: 測試案例涵蓋範圍不足

**風險等級**：P2（中風險）

**問題描述**：
測試文件缺少以下關鍵狀態轉換的測試案例。

**缺少的測試案例**：

#### PreGate0 階段測試

- **描述**：專案建立後但尚未提交 Gate 0 申請的狀態
- **測試情境**：建立專案 → 驗證 currentgate = Pending, projectstatus = Active

#### Terminated 流程測試

- **描述**：專案異常終止的完整流程
- **測試情境**：專案任意階段 → 終止決策 → 驗證 projectstatus = Terminated

#### Closed 流程測試

- **描述**：專案正常結案的完整流程
- **測試情境**：Gate 3 通過 → 結案流程 → 驗證 projectstatus = Closed, documentfreezestatus = Frozen

**修正建議**：在 07-testing-and-acceptance.md 新增對應測試案例

---

## 修正優先級建議

### P0 - 立即修正（阻斷上線）

1. **ISSUE-R2-001**：修正 04-powerapps-forms.md 中的已淘汰狀態
   - 影響：使用者介面會顯示錯誤的狀態選項
   - 預估工時：0.5 小時

### P1 - 高優先級（1 週內完成）

2. **ISSUE-R2-002/003**：修正 07 文件中的 cr_ prefix 和 900000000 值
   - 影響：測試案例會使用錯誤的欄位名稱和值
   - 預估工時：1 小時（可使用腳本自動修正）

### P2 - 中優先級（2 週內完成）

3. **ISSUE-R2-004**：補充缺失的測試案例
   - 影響：關鍵狀態轉換未經測試
   - 預估工時：4 小時

---

## 附錄：治理狀態權威定義

### gov_projectstatus（專案狀態）

| OptionSet 值 | 狀態名稱 | 說明 | 觸發條件 |
|------------|---------|------|---------|
| 100000000 | Active | 專案進行中 | GOV-001 建立專案 |
| 100000001 | OnHold | 專案暫停 | 業務決策暫停 |
| 100000002 | Closed | 正常結案 | GOV-012 結案流程 |
| 100000003 | Terminated | 異常終止 | 業務決策或違規終止 |

### 已淘汰狀態

| 已淘汰 | 正確狀態 | 原因 |
|-------|---------|------|
| Draft | PreGate0 (Active + Pending) | 專案一旦建立即進入治理範圍，不存在草稿狀態 |
| Completed | Closed | 術語一致性，對齊 02 文件權威定義 |
| Cancelled | Terminated | 明確區分正常結案與異常終止 |

---

**報告產生工具**：round2_forensics.py
**後續文件**：各文件的修正執行計畫