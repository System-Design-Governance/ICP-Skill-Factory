---
name: commissioning-defect-management
description: >
  試運行與缺陷管理：缺陷追蹤分級與試車程序開發。
  MANDATORY TRIGGERS: 缺陷管理, defect management, 試車, commissioning, 問題追蹤,
  defect tracking, snag list, punch list.
  Use this skill for commissioning planning and defect management in OT/ICS projects.
---

# 試運行與缺陷管理 (Commissioning & Defect Management)

整合 2 個 SK，涵蓋缺陷報告撰寫/分級與試車程序開發。

---

## 0. 初始化

1. FAT/SAT/SIT 已進行或計畫中
2. 缺陷追蹤系統已選定 (JIRA, Azure DevOps, etc.)
3. 嚴重度分級標準已與客戶對齊
4. 試車時程與資源已初步規劃

---

## 1. 工作流程

### Step 1: 缺陷報告撰寫與分級 (SK-D08-011)

**嚴重度分級**：

| 等級 | 定義 | 回應時限 | 範例 |
|------|------|----------|------|
| Critical | 系統無法運作或安全風險 | 立即 | 控制迴路失效、未授權存取 |
| Major | 主要功能受損但有 workaround | 24h | 告警延遲、報表錯誤 |
| Minor | 次要功能問題 | 1 week | UI 排版、非關鍵資料遺漏 |
| Cosmetic | 外觀/文件問題 | 下次 release | 拼字錯誤、顏色不一致 |

**缺陷報告必要欄位**：

| 欄位 | 說明 |
|------|------|
| Defect ID | 唯一識別碼 |
| Title | 簡明描述 |
| Description | 詳細問題描述 |
| Reproduction Steps | 重現步驟 |
| Expected vs. Actual | 預期行為 vs. 實際行為 |
| Severity | Critical/Major/Minor/Cosmetic |
| Discovery Phase | FAT / SAT / SIT |
| Affected Component | 受影響元件/系統 |
| Evidence | 截圖、log、trace |
| Resolution | 建議修復方式 + owner + deadline |

**步驟**：
1. 發現問題 → 立即記錄（避免遺忘細節）
2. 撰寫重現步驟（第三者可依步驟重現）
3. 評估嚴重度（考慮 OT 環境：安全 > 功能 > 外觀）
4. 附上證據（截圖、log 片段、network trace）
5. 建議修復方式與驗收標準
6. 登錄追蹤系統、指定 owner

**⚠️ 避坑**：
- 缺陷描述含糊 (e.g., "系統有問題") → 開發者無法重現
- OT 環境 severity 誤判：IT 思維下 Minor 的問題在 OT 可能是 Critical (e.g., 1s 通訊延遲)
- 未記錄 discovery phase → 無法分析缺陷逃逸率

### Step 2: 試車程序開發 (SK-D08-013)

**試車計畫架構**：

| 階段 | 內容 | 前置條件 |
|------|------|----------|
| Pre-commissioning | 硬體安裝完成確認、軟體部署 | 施工完成 |
| FAT 整合 | FAT 結果確認、未決項清單 | FAT 完成 |
| SAT 整合 | SAT 執行、現場驗證 | 系統安裝完成 |
| SIT 整合 | 跨系統整合測試 | SAT 通過 |
| Performance | 效能驗證、壓力測試 | SIT 通過 |
| Handover | 文件交付、訓練、簽核 | 全部測試通過 |

**步驟**：
1. 定義試車範圍與目標
2. 建立 FAT→SAT→SIT 執行序列與決策閘門
3. 規劃資源：人員、設備、場地、時程
4. 定義安全程序：LOTO、緊急關機、人員安全
5. 建立應變計畫：測試失敗 → 升級 → 重測 → go/no-go 決策
6. 定義 handover checklist：文件、訓練、保固、支援轉移
7. 設計簽核流程：FAT/SAT/SIT 各階段簽核 + 最終移交簽核

**⚠️ 避坑**：
- 未定義 go/no-go 標準 → 帶著未解缺陷上線
- Handover 遺漏訓練 → 操作人員不會用系統
- 試車時程過於樂觀 → 缺陷修復時間被壓縮

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | 缺陷報告含完整必要欄位且可重現 |
| 2 | 嚴重度分級與 OT 業務影響對齊 |
| 3 | 試車計畫含 FAT→SAT→SIT 完整序列 |
| 4 | Go/no-go 標準已定義 (Critical=0, Major 有 workaround) |
| 5 | Handover checklist 含文件、訓練、保固 |
| 6 | 應變計畫含升級路徑與重測程序 |

---

## 3. 人類審核閘門

```
試運行與缺陷管理完成。
📋 範圍：2 個工程步驟 (SK-D08-011, SK-D08-013)
📊 交付物：缺陷報告範本/分級標準、試車計畫文件
⚠️ 待確認：{TBD 項目}
👉 請 PM + STC + 客戶代表審核。
```

---

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D08-011 | Defect Tracking | 缺陷撰寫、severity 分級、追蹤系統、root cause |
| SK-D08-013 | Commissioning Procedure | 試車序列、go/no-go、handover、應變 |

<!-- Phase 6: Enhanced 2026-03-19. -->
