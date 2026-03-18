# Power Platform 治理系統建置手冊

**文件版本**：v1.0
**生效日期**：2026-02-09
**文件擁有者**：System Design Governance Function
**核准單位**：Engineering Management

---

## 本手冊之用途與適用對象

本手冊為 Design Governance System（Power Platform 版本）之**唯一官方建置指南**，涵蓋從環境準備至上線驗收的完整實作程序。

### 適用對象

| 角色 | 適用章節 |
|:------|:----------|
| Power Platform 管理員 | 全部章節 |
| Power Platform 開發人員 | 第 2 至第 7 章 |
| 資安稽核人員 | 第 6 章、第 7 章、附錄 A |
| 專案管理人員 | 第 1 章、第 7 章 |

### 本手冊之定位

本手冊為**施工級文件**，採用「傻瓜照做」原則撰寫：

- 所有步驟皆包含完整 UI 操作路徑
- 所有驗證皆為可觀察、可確認的具體結果
- 禁止跳過任何驗證步驟
- 禁止在未完成前置文件的情況下進入後續文件

---

## 新手快速導覽

> **第一次部署？請先閱讀以下文件。**

### 首次部署必讀文件

| 優先順序 | 文件 | 說明 | 類型 |
|:--------:|------|------|:----:|
| 1 | **00A-build-order-and-bootstrap.md** | 建置順序與階段說明 | 導覽 |
| 2 | **00B-first-run-initialization-checklist.md** | 首次上線初始化清單 | 檢查清單 |
| 3 | **00C-placeholder-reference.md** | 占位符與環境變數參考 | 參考 |

### 文件類型說明

| 類型 | 說明 | 使用方式 |
|:------|:------|:---------|
| **施工文件** | 包含具體操作步驟 | 逐步照做 |
| **設計說明** | 解釋機制設計意圖 | 理解後備查 |
| **檢查清單** | 一次性執行項目 | 勾選完成 |
| **參考文件** | 環境變數、占位符 | 按需查閱 |

### 文件分類

| 類型 | 對應文件 |
|:------|:---------|
| **施工文件** | 01、02、03、04、05、07 |
| **設計說明** | 06、附錄 A |
| **導覽與參考** | 00、00A、00B、00C |

### 建議閱讀順序（首次部署）

```
Step 1: 閱讀本文件（00-index.md）
        │
Step 2: 閱讀建置順序（00A-build-order-and-bootstrap.md）
        │
Step 3: 瀏覽占位符清單（00C-placeholder-reference.md）
        │
Step 4: 開始 Phase 1 建置（依 00A 文件指引）
        │
Step 5: 執行首次初始化（00B-first-run-initialization-checklist.md）
        │
Step 6: 繼續 Phase 2、Phase 3
        │
Step 7: 執行測試與驗收（07）
```

---

## 主閱讀順序

**必須依序閱讀並完成以下章節**：

| 順序 | 章節 | 內容概述 |
|:------|:------|:----------|
| 1 | 治理系統環境建置與前置條件指南 | Microsoft 365 租戶、Power Platform 環境、Entra ID 群組、Service Principal |
| 2 | Dataverse 資料模型與安全性建置指南 | 資料表建立、欄位定義、Field-Level Security、安全角色 |
| 3 | SharePoint 架構與文件管理建置指南 | 網站建立、文件庫結構、權限設定、Document Freeze 機制 |
| 4 | Power Apps 治理表單建置指南 | Canvas App 建立、表單設計、驗證邏輯 |
| 5 | **Power Automate 核心 Flows 施工手冊** | **Flow 實作之唯一依據** |
| 6 | Guardrails 與反作弊機制實作規格 | 監控機制、違規偵測、自動回滾 |
| 7 | 測試與驗收手冊 | 測試案例、驗收標準、上線檢查 |

> **警告**：禁止跳過任何章節。每章結尾皆設有 Gate 檢查點，未通過者禁止進入下一章。

---

## 實作依據聲明

### 唯一允許之 Flow 實作依據

**第 5 章「Power Automate 核心 Flows 施工手冊」為所有 Power Automate Flow 實作之唯一官方依據。**

- 本章採用「傻瓜照做」格式，提供逐步施工指引
- 禁止參照任何其他文件進行 Flow 實作
- 違反此規定所建置之 Flow 將不被視為合規

### 附錄文件之定位

**附錄 A「Power Automate 核心 Flows 設計規格」僅供以下用途**：

| 允許用途 | 說明 |
|:----------|:------|
| 理解設計意圖 | 供架構師理解系統設計背景 |
| 稽核審查 | 供稽核人員驗證實作是否符合設計 |
| 未來改版參考 | 供維護人員理解原始設計決策 |

**附錄文件禁止作為實作依據。** 任何人員若依據附錄進行實作，該實作將被視為未遵循治理程序。

---

## 文件建置方式

### 唯一允許之建置方式

本手冊輸出為 PDF 或 DOCX 格式時，**必須透過專案 Makefile 執行**：

```bash
# 建置 PDF 與 DOCX
make DOMAIN=project-governance DOCSET=power-platform-governance LANG=zh-TW all

# 僅建置 PDF
make DOMAIN=project-governance DOCSET=power-platform-governance LANG=zh-TW pdf

# 僅建置 DOCX
make DOMAIN=project-governance DOCSET=power-platform-governance LANG=zh-TW docx
```

### 禁止行為

以下行為**嚴格禁止**：

| 禁止行為 | 原因 |
|:----------|:------|
| 直接執行 `pandoc` 命令 | 無法確保格式一致性 |
| 自行修改 Pandoc 參數 | 可能破壞文件結構 |
| 繞過 Makefile 執行建置 | 無法確保輸出符合治理要求 |
| 手動編輯 PDF/DOCX 輸出檔案 | 輸出檔案為唯讀產物 |

---

## 文件版本與更新原則

### 版本控制

| 項目 | 規則 |
|:------|:------|
| 版本格式 | v主版本.次版本（如 v1.0、v1.1、v2.0） |
| 主版本變更 | 架構性變更、新增或移除主要章節 |
| 次版本變更 | 內容修正、補充說明、錯誤修復 |

### 更新程序

1. 所有變更必須在 Markdown 來源檔案中進行
2. 變更後必須更新文件版本號與生效日期
3. 重大變更必須經過治理負責人核准
4. 更新後必須重新執行 `make` 產生新版 PDF/DOCX

### 變更紀錄

| 版本 | 日期 | 變更說明 |
|:------|:------|:----------|
| v1.0 | 2026-01-30 | 初版建立，整合 temp 目錄文件 |

---

## 文件結構總覽

```
domains/project-governance/docs/power-platform-governance/zh-TW/
├── 00-index.md                              ← 本文件（導讀）
├── 00A-build-order-and-bootstrap.md         ← 建置順序與啟動指南【首次部署必讀】
├── 00B-first-run-initialization-checklist.md← 首次上線初始化清單【一次性執行】
├── 00C-placeholder-reference.md             ← 占位符與環境變數參考
├── 01-prerequisites-and-environment.md      ← 環境建置
├── 02-dataverse-data-model-and-security.md  ← 資料模型
├── 03-sharepoint-architecture.md            ← SharePoint 架構
├── 04-powerapps-forms.md                    ← Power Apps 表單
├── 05-core-flows-implementation-runbook.md  ← Flow 施工手冊【唯一實作依據】
├── 06-guardrails-and-anti-cheating.md       ← Guardrails 機制【治理語意權威】
├── 07-testing-and-acceptance.md             ← 測試與驗收
└── appendix/
    └── A-core-flows-specification.md        ← 設計規格【僅供參考】
```

---

## 開始建置

完成閱讀本導讀後，請依以下順序開始：

1. **首次部署者**：請先閱讀 **00A-build-order-and-bootstrap.md**，理解三階段建置流程
2. **環境準備**：瀏覽 **00C-placeholder-reference.md**，準備所需的環境變數與占位符
3. **開始建置**：依 00A 文件指引，從 Phase 1（01 章）開始

**下一步**：00A-build-order-and-bootstrap.md（建置順序與啟動指南）
