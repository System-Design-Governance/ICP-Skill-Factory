---
name: document-management
description: >
  文件管理：SLD 管理與文件交付追蹤。
  MANDATORY TRIGGERS: 文件管理, document management, SLD, 單線圖,
  文件交付, document delivery, deliverable tracking.
  Use this skill for document management and delivery tasks in OT/ICS projects.
---

# 文件管理 (Document Management)

整合 2 個 SK，涵蓋單線圖管理與文件交付清單管理。

---

## 0. 初始化

1. 電力系統架構與設備規格已確定
2. 合約交付物清單已從 SOW/ID03 提取
3. 文件管理系統已建立 (SharePoint/Confluence/DMS)
4. Gate 3 delivery checklist 已確認

---

## 1. 工作流程

### Step 1: 單線圖管理 (SK-D09-006)

**SLD 必要元素**：

| 元素 | 符號標準 | 說明 |
|------|----------|------|
| 變壓器 | IEC 60617 | 容量、電壓比、阻抗 |
| 斷路器 | IEEE Std 91 | 額定電流、斷路容量 |
| 保護繼電器 | ANSI device number | 功能代碼 (e.g., 87T) |
| 計量點 | CT/PT symbol | 比流器/比壓器 |
| 負載 | Load symbol | 額定功率、功率因數 |
| 匯流排 | Bus bar | 額定電壓、短路容量 |

**步驟**：
1. 從電力系統架構建立 SLD 初稿 (CAD 格式)
2. 標註所有設備：ID、額定值、設定值
3. 與設備清單交叉核對 (每個設備 ID 一一對應)
4. 覆蓋保護區域與協調曲線參考
5. 與 SK-D01-001 安全區邊界對齊
6. 審核：DES + PE + SYS 簽核

**⚠️ 避坑**：
- SLD 與設備清單不同步 → 施工時裝錯設備
- 保護區域遺漏 → 某段匯流排無保護
- 未標 CT/PT ratio → 計量數據錯誤

### Step 2: 文件交付清單管理 (SK-D09-008)

**文件生命週期**：

```
Draft → Internal Review → Revision → Customer Review → Approved → Delivered → Archived
```

**交付清單欄位**：

| 欄位 | 說明 |
|------|------|
| Doc ID | 文件編號 |
| Title | 文件名稱 |
| Type | 規格/圖面/報告/手冊 |
| Owner | 負責人 |
| Status | Draft/Review/Approved/Delivered |
| Due Date | 合約交付日 |
| Actual Date | 實際交付日 |
| Gate | 對應 Gate (G1/G2/G3) |
| Review Comments | 審核意見追蹤 |

**步驟**：
1. 從合約/SOW 提取所有必須交付的文件
2. 建立交付清單 (Excel 或 DMS tracker)
3. 指定每份文件的 owner + due date
4. 每週追蹤狀態更新
5. Gate 審核前 checklist 比對：所有 Gate-required 文件是否 Approved
6. 交付後歸檔並記錄客戶確認

**⚠️ 避坑**：
- 合約要求的文件遺漏未列入清單 → Gate 審核才發現缺件
- 狀態未即時更新 → PM 以為完成其實還在 Draft
- 交付格式不符合約 (e.g., 要求 PDF 卻給 .docx) → 退件

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | SLD 涵蓋 100% 電力設備且標註完整 |
| 2 | SLD 符號符合 IEC 60617 / IEEE Std 91 |
| 3 | 設備 ID 與設備清單一一對應 |
| 4 | 交付清單涵蓋合約所有必須文件 |
| 5 | Gate 前所有必要文件 status = Approved |
| 6 | 文件格式符合合約要求 |

---

## 3. 人類審核閘門

```
文件管理完成。
📋 範圍：2 個工程步驟 (SK-D09-006, SK-D09-008)
📊 交付物：SLD ({n} 張)、文件交付清單 ({m} 份文件追蹤)
⚠️ 待確認：{TBD 項目}
👉 請 DES + PM 審核。
```

---

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D09-006 | SLD Management | SLD 繪製、設備標註、保護區域、審核 |
| SK-D09-008 | Document Delivery | 交付清單、生命週期追蹤、Gate checklist |

<!-- Phase 6: Enhanced 2026-03-19. -->
