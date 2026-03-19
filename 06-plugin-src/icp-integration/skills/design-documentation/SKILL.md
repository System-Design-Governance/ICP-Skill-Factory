---
name: design-documentation
description: >
  設計文件撰寫：SDD、會議紀錄、版本控制、技術寫作。
  MANDATORY TRIGGERS: 設計文件, design documentation, SDD, 會議紀錄, meeting minutes,
  版控, version control, 技術寫作, technical writing.
  Use this skill for design documentation tasks in OT/ICS cybersecurity projects.
---

# 設計文件撰寫 (Design Documentation)

整合 4 個 SK，涵蓋 SDD 撰寫、會議紀錄、版本控制、技術寫作。

---

## 0. 初始化

1. 安全架構設計 (D01)、系統架構 (D02)、控制設計 (D05) 已完成
2. 專案文件管理系統已建立 (Git/SharePoint/Confluence)
3. 文件範本與編號規則已定義
4. 版本控制工具已選定並配置

---

## 1. 工作流程

### Step 1: 系統設計說明書撰寫 (SK-D09-001)

**SDD 文件結構 (IEEE 1016)**：

| 章節 | 內容 |
|------|------|
| 1. System Overview | 系統目標、範圍、利害關係人 |
| 2. Design Entities | 子系統分解、元件清單 |
| 3. Design Views | 架構圖、資料流、部署圖 |
| 4. Interface Specs | 系統間介面規格 |
| 5. Design Rationale | 設計決策與替代方案分析 |
| 6. Quality Attributes | 效能、可靠性、安全性需求 |

**步驟**：
1. 蒐集 D01-D07 各域設計產出
2. 整合為統一敘事：從系統目標 → 架構 → 元件 → 介面
3. 嵌入所有架構圖並與文字交叉引用
4. 建立需求追蹤矩陣：需求 → 架構 → 元件 → 實作
5. 記錄設計決策與理由 (Design Decision Record)
6. 提交 SAC + SYS + QAM 審核簽核

**⚠️ 避坑**：
- 各域設計用詞不一致 → SDD 內部自相矛盾
- 圖文不符 → 圖是舊版、文字是新版
- 追蹤矩陣有空白 → 某些需求無對應設計

### Step 2: 會議紀錄 (SK-D09-003)

**會議紀錄範本**：

| 欄位 | 內容 |
|------|------|
| 會議名稱 | e.g., Design Review #3 |
| 日期/時間 | ISO 8601 格式 |
| 出席者 | 姓名 + 角色 |
| 議程 | 編號議題清單 |
| 決議事項 | 每議題的決定 + 負責人 + 期限 |
| Action Items | ID、描述、owner、deadline、status |
| 下次會議 | 日期 + 議題預告 |

**步驟**：
1. 會前準備議程並發送
2. 會中即時記錄（不是會後回憶）
3. 決議事項以明確動詞開頭 (e.g., "SYS 將於 03/25 前更新 SDD §3.2")
4. 24h 內發送紀錄並要求確認
5. 追蹤 Action Items 至完成

**⚠️ 避坑**：決議寫成「討論了 X」而非「決定了 Y」→ 事後無法追溯

### Step 3: 版本控制與歸檔 (SK-D09-004)

**版本號規範**：

| 格式 | 意義 | 範例 |
|------|------|------|
| 0.x | Draft (未審核) | 0.1, 0.2 |
| 1.0 | 首次核准發行 | 1.0 |
| 1.x | 小修 (不影響設計) | 1.1, 1.2 |
| 2.0 | 重大修訂 | 2.0 |
| x.x-RC | Release Candidate | 1.0-RC1 |

**步驟**：
1. 建立版本號規範並培訓團隊
2. 配置版控工具 (Git for code/config, DMS for documents)
3. 定義 baseline：每個 Gate 鎖定一次 baseline
4. 變更流程：變更請求 → CCB 審核 → 更新 → 新版號
5. 歸檔策略：retention period、格式遷移、存取控制
6. 稽核日誌：誰在何時改了什麼

**⚠️ 避坑**：
- 用 email 傳檔案而非版控 → 「最終版 v3_final_FINAL.docx」
- 未鎖 baseline → 設計文件被悄悄改動，追蹤斷裂

### Step 4: 技術寫作 (SK-D09-005)

**技術寫作原則**：

| 原則 | 說明 |
|------|------|
| 受眾導向 | 工程師 vs. 操作員 vs. 管理層 → 不同深度 |
| 一致性 | 術語、縮寫、格式全文統一 |
| 可追蹤 | 每個 claim 引用來源 (標準、設計文件) |
| 主動語態 | "系統執行..." 而非 "被執行的是..." |
| 圖文並茂 | 複雜概念用圖表 + 文字雙重解釋 |

**步驟**：
1. 確定受眾與文件用途
2. 建立術語表 (glossary) 並與專案術語對齊
3. 撰寫初稿 → peer review → 修訂
4. 格式檢查：標題層級、編號、交叉引用
5. 品質檢查：拼字、文法、一致性

**⚠️ 避坑**：寫了沒人讀 → 因為太長/太抽象/格式混亂

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | SDD 結構符合 IEEE 1016 且涵蓋 D01-D07 所有設計 |
| 2 | 需求追蹤矩陣無空白 (每需求有對應設計) |
| 3 | 所有會議紀錄含決議 + Action Items + owner + deadline |
| 4 | 版控規範已實施，所有文件有版本號 |
| 5 | 術語表已建立且全文一致 |
| 6 | SDD 經 SAC + SYS + QAM 簽核 |

---

## 3. 人類審核閘門

```
設計文件撰寫完成。
📋 範圍：4 個工程步驟 (SK-D09-001, SK-D09-003, SK-D09-004, SK-D09-005)
📊 交付物：SDD、會議紀錄、版控規範、術語表
⚠️ 待確認：{TBD 項目}
👉 請 SYS + QAM 審核。
```

---

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D09-001 | SDD Writing | IEEE 1016 結構、設計整合、追蹤矩陣 |
| SK-D09-003 | Meeting Minutes | 紀錄範本、決議追蹤、Action Items |
| SK-D09-004 | Document Version Control | 版本號、baseline、變更流程、歸檔 |
| SK-D09-005 | Technical Writing | 受眾導向、一致性、可追蹤、圖文並茂 |

<!-- Phase 6: Enhanced 2026-03-19. -->
