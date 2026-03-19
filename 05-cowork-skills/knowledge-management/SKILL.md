---
name: knowledge-management
description: >
  知識管理 — 涵蓋外部標準追蹤、知識庫管理、設計模式庫、能力評估、跨專案知識轉移、安全實施計畫及工程指標。
  MANDATORY TRIGGERS: 知識管理, knowledge management, 標準追蹤, standards tracking, 知識庫, knowledge repository, 設計模式, design pattern, 能力評估, competency, 跨專案, cross-project, 工程指標, engineering metrics
  Use this skill for knowledge management tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 知識管理 Knowledge Management

本 Skill 整合 7 個工程技能定義，提供知識管理的完整工作流程。
適用領域：Governance & Process（D11）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方 §1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認 SK-D11-004, SK-D11-006, SK-D11-011, SK-D14-001 產出已可用

---

## 1. 輸入

- 利害關係人溝通需求與偏好
- 組織資料分類政策 (ID23) 與 ISO 27001 Annex A
- 安全需求規格 (from SK-D14-001)
- 工程能力框架 (from SK-D11-011)
- KPI 評估結果與能力缺口分析
- 設計標準庫現有內容 (from SK-D11-010)
- 採購安全程序 (ID22)
- 專案學習記錄與品質指標

---

## 2. 工作流程

### Step 1 — 利害關係人溝通計畫 (SK-D11-007)

| 項目 | 內容 |
|------|------|
| 目的 | 建立全面的利害關係人溝通計畫，確保及時、適當的資訊流通 |
| 範圍 | 專案啟動至營運移交 |
| 執行者 | Project Manager |

**交付物**：溝通計畫、利害關係人登記冊、溝通時程表、溝通範本、升級程序、溝通效能指標

### Step 2 — 設計標準庫維護 (SK-D11-010)

| 項目 | 內容 |
|------|------|
| 目的 | 維護內部設計標準、範本與參考架構庫 |
| 範圍 | 設計範本、技術標準、流程標準、參考架構 |
| 執行者 | Head of System Design (GOV-SDP) |

**交付物**：標準庫（集中式版本控管儲存庫）、每項標準的適用性聲明與規格、標準建立與退役程序

### Step 3 — 訓練計畫管理 (SK-D11-012)

| 項目 | 內容 |
|------|------|
| 目的 | 規劃、執行與管理年度工程訓練計畫 |
| 整合 | 能力缺口 (SK-D11-011) 驅動訓練計畫 |
| 執行者 | Training Manager / Head of System Design |

**交付物**：年度訓練計畫（需求分析、課程清單、交付時程、預算、成功指標）、訓練效能報告、認證追蹤登記冊

### Step 4 — 資訊資產分類 (SK-D11-013)

| 項目 | 內容 |
|------|------|
| 目的 | 依 ID23 政策分類所有資訊資產，指定保密與完整性保護等級 |
| 依據 | ID23, ISO 27001 Annex A |
| 執行者 | Information Security Officer |

**交付物**：資訊資產分類矩陣、資產分類登記冊、分類標準對應文件、資料處理與保護需求表

### Step 5 — 採購安全需求整合 (SK-D11-015)

| 項目 | 內容 |
|------|------|
| 目的 | 將網路安全需求整合至採購流程 |
| 依據 | ID22 採購安全程序 |
| 執行者 | Procurement Security Lead |

**交付物**：採購安全需求規格 (SRSP)、RFQ/RFP 安全附錄、廠商安全評估清單、採購安全合規監控日誌

### Step 6 — 安全管理計畫撰寫 (SK-D11-016)

| 項目 | 內容 |
|------|------|
| 目的 | 建立 SI/SM 專案安全管理計畫 (SMP) |
| 依據 | IEC 62443-2-4, ID06 (45+ 頁範本) |
| 執行者 | Security Manager / SAC |

**交付物**：安全管理計畫文件（組織、角色、政策、程序、合規要求、風險管理、變更管理、訓練需求）

### Step 7 — 標準歸屬與例外裁定 (SK-D11-019)

| 項目 | 內容 |
|------|------|
| 目的 | 管理工程標準的歸屬、維護與例外裁定 |
| 升級 | L1 專案層級 / L2 跨專案 / L3 組織標準變更 |
| 執行者 | Standards Committee / Head of System Design |

**交付物**：標準登記冊、標準歸屬矩陣、例外請求決策記錄 (L1/L2/L3)、例外追蹤登記冊、標準維護時程表

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | 利害關係人溝通計畫與登記冊 | Markdown / Excel |
| 2 | 設計標準庫 | Wiki / Markdown |
| 3 | 年度訓練計畫與認證追蹤 | Excel |
| 4 | 資訊資產分類矩陣與登記冊 | Excel |
| 5 | 採購安全需求規格 (SRSP) | Markdown |
| 6 | 安全管理計畫 (SMP) | Word |
| 7 | 標準登記冊與例外追蹤 | Excel |

---

## 4. 適用標準

- IEC 62443-2-4 — SI/SM 安全管理
- IEC 62443-2-1 §5.2.1 — 供應鏈安全
- ISO 27001 Annex A — 資訊安全控制
- ID22 — 採購安全程序
- ID23 — 資料分類政策
- GOV-SDP — 組織治理框架

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | 溝通計畫識別所有主要利害關係人 | 含資訊需求與偏好 |
| 2 | 溝通時程對齊專案里程碑與 Gate 審查 | 含日期與分發方式 |
| 3 | 標準庫集中化、版本控管、可存取 | 採用率 >=80% |
| 4 | 每項標準含適用性聲明與至少一個範例 | 有建立與退役程序 |
| 5 | 訓練計畫連結能力框架缺口 | 每項缺口有對應訓練 |
| 6 | 訓練效能至少達 Kirkpatrick Level 2 | 有訓後評量 |
| 7 | 100% 範圍內資產有分類等級 | 可追溯至 ID23 政策 |
| 8 | SRSP 對應 100% D01 安全控制需求 | 無孤立安全控制 |
| 9 | SMP 完成 ID06 所有章節 | 無範本佔位符 |
| 10 | 標準登記冊季度更新 | 每項有命名歸屬者 |
| 11 | 例外請求含 L1/L2/L3 升級標準 | 非主觀判定 |

---

## 6. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 輸入完整性 | 所有必要輸入已讀取並摘要 |
| 2 | 流程覆蓋 | 7 個工作步驟皆已執行並有產出 |
| 3 | 輸出完整性 | 所有交付物已產出且非空白 |
| 4 | 標準合規 | 引用標準版本正確 |
| 5 | 跨步驟一致 | 各步驟產出間無矛盾 |
| 6 | 依賴追溯 | 外部依賴 SK 的輸入已驗證可用 |

---

## 7. 人類審核閘門

完成所有工作步驟後，**暫停**並向使用者提交審核：

```
知識管理已完成。
執行範圍：7 個工程步驟（SK-D11-007, SK-D11-010, SK-D11-012, SK-D11-013, SK-D11-015, SK-D11-016, SK-D11-019）
交付物：溝通計畫、設計標準庫、訓練計畫、資產分類、SRSP、SMP、標準登記冊
待確認事項：{列出 TBD 項目或需人工判斷的假設}
請審核以上成果，確認 PASS / FAIL / PASS with Conditions。
```

判定：PASS / FAIL / PASS with Conditions

---

## 8. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 |
|--------|---------|---------|
| SK-D11-007 | Stakeholder Communication Plan | 利害關係人溝通計畫 |
| SK-D11-010 | Internal Design Standards Library | 內部設計標準庫 |
| SK-D11-012 | Training Program Management | 訓練計畫管理 |
| SK-D11-013 | Information Asset Classification | 資訊資產分類 |
| SK-D11-015 | Procurement Security Requirements Integration | 採購安全需求整合 |
| SK-D11-016 | Security Management Plan Development | 安全管理計畫撰寫 |
| SK-D11-019 | Standards Ownership & Exception Arbitration | 標準歸屬與例外裁定 |
