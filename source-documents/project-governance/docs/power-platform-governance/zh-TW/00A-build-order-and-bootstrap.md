# 建置順序與啟動指南

**文件版本**：v1.0
**生效日期**：2026-02-09
**文件擁有者**：System Design Governance Function
**文件性質**：首次建置必讀

---

## 本文件目的

本文件為 Power Platform 治理系統的**唯一建置順序權威指南**，解決以下問題：

- 04 章（Power Apps）需要 05 章（Flows）才能完成
- 05 章要求返回 04 章連接 Flow
- 新進人員不知如何處理此「看似循環」的相依關係

> **重要澄清**：本系統不存在真正的技術循環相依。04 章與 05 章的交織是**操作順序問題**，而非架構缺陷。本文件提供明確的分階段執行方式。

---

## 建置階段總覽

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        治理系統建置三階段流程                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  【Phase 1】基礎建設（可獨立完成）                                            │
│  ├── 01 環境與前置條件                                                       │
│  ├── 02 Dataverse 資料模型                                                   │
│  ├── 03 SharePoint 架構                                                      │
│  └── 04 Power Apps 階段一（UI 框架）                                         │
│                                                                             │
│  【Phase 2】Flow 建置（依賴 Phase 1）                                        │
│  └── 05 所有 GOV-001 至 GOV-020 Flow                                        │
│                                                                             │
│  【Phase 3】整合啟用（依賴 Phase 1 + Phase 2）                               │
│  ├── 04 Power Apps 階段二（連接 Flow）                                       │
│  ├── 06 Guardrails 確認（閱讀確認，非建置）                                  │
│  └── 07 測試與驗收                                                           │
│                                                                             │
│  【最後整合啟用點】                                                           │
│  └── Phase 3 完成後，系統正式可用                                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Phase 1：基礎建設

### 執行範圍

| 順序 | 文件 | 執行內容 | 完成標誌 |
|:----:|------|---------|---------|
| 1 | 00-index.md | 閱讀導讀 | 理解文件架構 |
| 2 | 00B-first-run-initialization-checklist.md | 閱讀首次初始化清單 | 理解初始化需求 |
| 3 | 01-prerequisites-and-environment.md | 環境建置 | Environment Ready Gate 通過 |
| 4 | 02-dataverse-data-model-and-security.md | 資料模型建置 | Data Model Ready Gate 通過 |
| 5 | 03-sharepoint-architecture.md | SharePoint 建置 | SharePoint Ready Gate 通過 |
| 6 | 04-powerapps-forms.md **階段一** | Power Apps UI 框架 | 表單 UI 完成（不含 Flow 連接） |

### 04 章階段一：可以做什麼

| 可執行項目 | 說明 |
|:-----------|:------|
| 建立 Canvas App | 建立應用程式框架 |
| 建立所有表單 UI | FORM-001 至 FORM-011 的介面設計 |
| 設定表單驗證邏輯 | 必填欄位、格式驗證等 |
| 設定資料來源連接 | 連接 Dataverse 資料表 |
| 預覽表單外觀 | 確認 UI 正確 |

### 04 章階段一：暫時不可用但不會失敗的項目

| 暫不可用項目 | 原因 | 影響 |
|:-------------|:------|:------|
| 表單「提交」按鈕功能 | Flow 尚未建立 | 按鈕可存在，但點擊後無動作或顯示錯誤 |
| Flow 連接設定 | Flow 尚未建立 | 此設定步驟跳過，等 Phase 3 返回 |

### Phase 1 完成檢查點

- [ ] Environment Ready Gate 30 項全部通過
- [ ] 8 個 Dataverse 資料表已建立
- [ ] 所有 Flow-only 欄位已設定 Field-Level Security
- [ ] SharePoint Site 與文件庫已建立
- [ ] Power Apps 所有表單 UI 已建立（「提交」功能除外）

---

## Phase 2：Flow 建置

### 執行範圍

| 順序 | 文件 | 執行內容 | 完成標誌 |
|:----:|------|---------|---------|
| 1 | 00B-first-run-initialization-checklist.md | **執行**首次初始化 | Counter List 已初始化 |
| 2 | 05-core-flows-implementation-runbook.md | 建立所有 Flow | Flow Ready Gate 通過 |

### Flow 建置順序（必須遵守）

```
第一批：Child Flows（無相依，可平行建置）
├── GOV-015 Notification Service
├── GOV-013 Risk Level Calculator
├── GOV-014 Document Freeze Controller
└── GOV-016 Rework Handler

第二批：依賴第一批
├── GOV-004 Risk Acceptance（依賴 GOV-013）
├── GOV-003 Gate Approval Engine（依賴 GOV-015, GOV-016）
└── GOV-005 Document Intake（依賴 GOV-015）

第三批：依賴第二批
├── GOV-002 Gate Request Receiver（依賴 GOV-003, GOV-004）
└── GOV-001 Project Intake（依賴 GOV-015）

第四批：Scheduled Flows（無相依，可最後建置）
├── GOV-017 Guardrail Monitor
├── GOV-018 Compliance Reconciler
└── GOV-019 SLA Monitor
```

### Phase 2 完成檢查點

- [ ] Counter List 已初始化（RequestID 初始值 = 0）
- [ ] 所有 19 條 Flow 已建立
- [ ] 所有 Flow 使用 Connection Reference（非個人連線）
- [ ] 所有 Flow 已實作 Try-Catch
- [ ] GOV-001 測試執行成功（建立一筆測試專案）

---

## Phase 3：整合啟用

### 執行範圍

| 順序 | 文件 | 執行內容 | 完成標誌 |
|:----:|------|---------|---------|
| 1 | 04-powerapps-forms.md **階段二** | 連接 Flow + 發佈 | App 已發佈 |
| 2 | 06-guardrails-and-anti-cheating.md | 閱讀確認 | 理解三道防線機制 |
| 3 | 07-testing-and-acceptance.md | 執行測試 | 所有測試案例通過 |

### 04 章階段二：返回完成的項目

| 執行項目 | 說明 |
|:---------|:------|
| 連接表單至 Flow | 將「提交」按鈕連接至對應的 GOV Flow |
| 測試表單提交 | 確認表單提交可觸發 Flow |
| 發佈 Power Apps | 將 App 發佈至使用者 |

### 06 章：閱讀確認（非建置）

> **重要**：06 章的 GOV-017/018/019 詳細內容為「設計說明」，**實作已在 05 章完成**。Phase 3 閱讀 06 章的目的是理解 Guardrail 機制，而非重複建置。

### Phase 3 完成檢查點

- [ ] 所有表單已連接對應 Flow
- [ ] Power Apps 已發佈
- [ ] E2E-001 至 E2E-013 測試案例通過
- [ ] AC-001 至 AC-008 反作弊測試案例通過

---

## 最後整合啟用點

### 啟用條件

以下條件**全部滿足**後，系統正式可用：

| # | 條件 | 驗證方式 |
|:---|:------|:---------|
| 1 | Phase 1 完成檢查點全部通過 | 檢查清單勾選 |
| 2 | Phase 2 完成檢查點全部通過 | 檢查清單勾選 |
| 3 | Phase 3 完成檢查點全部通過 | 檢查清單勾選 |
| 4 | 首次初始化清單已執行 | 00B 文件檢查點勾選 |
| 5 | 測試專案已成功走完完整流程 | 07 文件 Smoke Test 通過 |

### 啟用宣告

當上述條件全部滿足，系統管理員應：

1. 通知相關人員系統已上線
2. 啟用 Scheduled Flows（GOV-017, GOV-018, GOV-019）
3. 開始正式使用

---

## 常見問題

### Q1：我在 04 章發現需要 Flow URL，但 Flow 還沒建立怎麼辦？

**答**：這是正常的。請先完成 04 章階段一（UI 框架），跳過所有「連接 Flow」的步驟。等 Phase 2 完成後返回 Phase 3 執行。

### Q2：05 章末尾說「返回 04 章」，我應該什麼時候返回？

**答**：當 05 章的 Flow Ready Gate 通過後，立即返回。這就是 Phase 3 的起點。

### Q3：06 章的 GOV-017/018/019 內容跟 05 章重複，我要做兩次嗎？

**答**：不需要。實作只做一次（05 章）。06 章是設計說明，用於理解機制與稽核參考。

### Q4：如果我跳過某個 Phase 會怎樣？

**答**：系統將無法正常運作。例如：
- 跳過 Phase 1：Flow 無法存取 Dataverse
- 跳過 Phase 2：表單提交無法觸發任何動作
- 跳過 Phase 3：系統建置完成但未經測試驗證

### Q5：這個順序是強制的嗎？

**答**：是的。本文件定義的順序是經過驗證的唯一正確路徑。

---

## 附錄：為何不存在真正的循環相依

### 技術分析

| 相依關係 | 說明 | 結論 |
|:---------|:------|:------|
| 04 → 05 | Power Apps 需要 Flow URL | 04 的 **UI 建置**不需要 Flow，僅**連接**需要 |
| 05 → 02 | Flow 需要 Dataverse 表 | 02 在 05 之前，無循環 |
| 05 → 03 | Flow 需要 SharePoint | 03 在 05 之前，無循環 |

### 結論

04 與 05 之間**不是**真正的循環相依，而是：
- 04 章可拆分為「階段一：UI」與「階段二：連接」
- 05 章可獨立完成
- 只需將 04 章的「連接」部分延後到 05 章之後即可

本文件透過三階段分割，消除了操作層面的混淆。

---

**文件結束**

**下一步**：請依序閱讀 00B-first-run-initialization-checklist.md，然後開始 Phase 1 建置。
