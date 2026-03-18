```{=latex}
\newpage
```

# Appendix D: Integrated Risk Assessment Templates

## Purpose {#appD-purpose}

本附錄提供整合式風險評估（IEC 62443-3-2 + FMEA + HAZOP）之最小可用模板，供 Gate 1 至 Gate 3 使用。各模板僅定義必要欄位結構，不限制使用工具（Excel / Word / 專用系統皆可）。

### 風險判定規則之唯一來源聲明 {#appD-single-source}

**本附錄僅提供風險評估之模板結構，不定義風險判定規則。** 所有風險相關之規範定義，以 Appendix C 為唯一來源：

| 規範項目 | 權威來源 | 本附錄定位 |
|---------|---------|-----------|
| 風險矩陣（Risk Matrix） | Appendix C | 不重複定義 |
| 風險等級定義（Low/Medium/High/Critical） | Appendix C | 僅引用，不重新詮釋 |
| 風險接受權限 | 主文件 5.2 節 + Appendix C | 不重複定義 |
| Likelihood / Impact 評分準則 | Appendix C | 不重複定義 |
| RPN 閾值與計算方式（FMEA） | Appendix C | 不重複定義 |

**一致性要求**：當專案使用本附錄模板進行風險評估時，所有風險等級之判定必須依據 Appendix C 所定義之風險矩陣與評分準則。若本附錄之欄位說明與 Appendix C 有歧義，以 Appendix C 為準。

### 使用邊界聲明 {#appD-usage-boundary}

- 本附錄僅為**模板集合**，不構成完整風險分析報告
- Gate 3 **不要求**重新執行完整 FMEA / HAZOP，僅要求殘餘風險可追溯至本附錄定義之風險來源（Risk Source ID）
- 各模板之執行深度（Lite / Full）依主文件 3.2 節規定，本附錄不另行定義

---

## IEC 62443-3-2 Zone & Conduit Diagram Template {#appD-zone-conduit}

### 適用 Gate

- **Gate 1**：設計基線建立（必要交付物）
- **Gate 2**：變更時更新

### 輸入來源

- 系統架構圖
- 網路拓撲圖
- 資產清單（Gate 0 產出）

### 必填欄位（Must）

| 欄位 | 說明 |
|------|------|
| Zone ID | 唯一識別碼（如 Z-001） |
| Zone Name | Zone 名稱 |
| Target SL | 目標安全等級（SL 1-4） |
| Assets | Zone 內資產清單 |
| Conduit ID | 連接此 Zone 之 Conduit 識別碼 |

### Conduit 定義表

| 欄位 | 說明 |
|------|------|
| Conduit ID | 唯一識別碼（如 C-001） |
| Source Zone | 來源 Zone ID |
| Target Zone | 目標 Zone ID |
| Protocol | 通訊協定 |
| Direction | 資料流向（單向/雙向） |

### 選填欄位（Optional）

- Zone 物理位置
- Conduit 頻寬限制
- 備援路徑說明

---

## IEC 62443-3-2 Threat Scenario Template {#appD-threat-scenario}

### 適用 Gate

- **Gate 1**：威脅情境分析（整合式風險評估之一部分）
- **Gate 2**：變更影響評估時更新

### 輸入來源

- Zone & Conduit Diagram（見「IEC 62443-3-2 Zone & Conduit Diagram Template」）
- 資產清單
- FR/SR 檢查表（Appendix A）

### 必填欄位（Must）

| 欄位 | 說明 |
|------|------|
| Threat ID | 唯一識別碼，格式：**T-XXX** |
| Threat Name | 威脅名稱 |
| Target Zone/Conduit | 受影響之 Zone 或 Conduit ID |
| Threat Source | 威脅來源（內部/外部/供應鏈） |
| Attack Vector | 攻擊向量簡述 |
| Affected FR | 受影響之 FR（FR1-FR7） |
| Likelihood | High / Medium / Low |
| Impact | High / Medium / Low |
| Inherent Risk | Critical / High / Medium / Low |

### 選填欄位（Optional）

- STRIDE 分類
- MITRE ATT&CK 對應
- 參考 CVE

### 輸出

- 產出之 Threat ID 作為殘餘風險清單（Appendix C）之 Risk Source ID

---

## FMEA Worksheet Template {#appD-fmea}

### 適用 Gate

- **Gate 1**：整合式風險評估之失效模式分析
- **Gate 2**：設計變更時更新

### 輸入來源

- 系統元件清單
- 功能規格書
- 歷史失效紀錄（如有）

### 必填欄位（Must）

| 欄位 | 說明 |
|------|------|
| FM ID | 唯一識別碼，格式：**FM-XXX** |
| Component | 元件/子系統名稱 |
| Function | 元件功能 |
| Failure Mode | 失效模式描述 |
| Failure Effect | 失效影響（局部/系統/安全） |
| Severity | High / Medium / Low |
| Occurrence | High / Medium / Low |
| Detection | High / Medium / Low（偵測難度） |
| Risk Level | Critical / High / Medium / Low |

### 評分說明

評分準則與風險等級計算方式，依 Appendix C 所定義之風險矩陣與評分表為準。本節僅說明欄位用途：

- **Severity**：失效對系統/安全之影響程度（評分準則見 Appendix C）
- **Occurrence**：失效發生可能性（評分準則見 Appendix C）
- **Detection**：現有機制偵測失效之能力（評分準則見 Appendix C）
- **Risk Level**：依 Appendix C 風險矩陣計算

### 選填欄位（Optional）

- 建議控制措施
- 責任單位
- 預計改善時程

### 輸出

- 產出之 FM ID 作為殘餘風險清單（Appendix C）之 Risk Source ID

### 治理一致性說明

Lite 或完整 FMEA 分析之選擇，依主文件 3.2 節與 Gate 定義判定，本附錄不重複定義 Lite / Full 判定規則。

---

## HAZOP Worksheet Template {#appD-hazop}

### 適用 Gate

- **Gate 1**：整合式風險評估之操作偏差分析
- **Gate 2**：流程變更時更新

### 輸入來源

- 操作流程圖（P&ID 或流程敘述）
- 操作程序書
- 人機介面設計

### 必填欄位（Must）

| 欄位 | 說明 |
|------|------|
| HAZ ID | 唯一識別碼，格式：**HAZ-XXX** |
| Process Node | 流程節點/步驟 |
| Parameter | 操作參數（如流量、溫度、指令） |
| Guide Word | 偏差導引詞（No/More/Less/Reverse/Other） |
| Deviation | 偏差描述 |
| Cause | 可能原因 |
| Consequence | 偏差後果 |
| Likelihood | High / Medium / Low |
| Severity | High / Medium / Low |
| Risk Level | Critical / High / Medium / Low |

### Guide Word 標準定義

| Guide Word | 意義 |
|------------|------|
| No / None | 完全無動作或流量 |
| More | 參數過高 |
| Less | 參數過低 |
| Reverse | 方向相反 |
| Part of | 僅部分完成 |
| Other than | 非預期操作 |
| Early / Late | 時序偏差 |

### 選填欄位（Optional）

- 現有防護措施
- 建議改善措施
- 責任單位

### 輸出

- 產出之 HAZ ID 作為殘餘風險清單（Appendix C）之 Risk Source ID

### 治理一致性說明

Lite 或完整 HAZOP 分析之選擇，依主文件 3.2 節與 Gate 定義判定，本附錄不重複定義 Lite / Full 判定規則。

---

## Risk Source ID 編碼規則 {#appD-risk-source-id}

### 編碼格式

| 分析方法 | ID 前綴 | 格式範例 | 說明 |
|---------|--------|---------|------|
| IEC 62443-3-2 Threat Scenario | T- | T-001, T-042 | 資安威脅情境 |
| FMEA Failure Mode | FM- | FM-001, FM-SYS-003 | 失效模式（可加子系統代碼） |
| HAZOP Deviation | HAZ- | HAZ-001, HAZ-P02-D01 | 操作偏差（可加流程節點代碼） |
| Threat Modeling (STRIDE) | TM- | TM-001, TM-S-005 | 設計層級威脅（可加 STRIDE 類別） |

### 編碼原則

1. **唯一性**：同一專案內 ID 不得重複
2. **可追溯**：ID 須可追溯至原始分析工作表
3. **版本管理**：ID 一經指派不得變更，僅可標註廢止
4. **跨文件引用**：殘餘風險清單（Appendix C）之 Risk Source ID 必須使用本規則

### Gate 3 追溯驗證

QA Team 於 Gate 3 執行 20% 抽查時，須驗證：

- 殘餘風險之 Risk Source ID 存在於對應分析工作表
- Risk Source ID 格式符合本節規則
- 風險等級評估與原始分析一致

### 治理用途說明

Risk Source ID 為**治理追溯用途**，用於建立殘餘風險與原始分析之關聯。專案不要求維持特定分析工具或格式，只要能依 ID 回查至原始分析紀錄即可（tool-agnostic）。

---

## Document Control {#appD-doc-control}

- **Version**: 1.0
- **Effective Date**: 2026-01-09
- **Owner**: System Design Governance Function
- **Review Cycle**: 與主文件同步

本附錄之修訂依主文件 6.2 節流程辦理。

---

**文件結束**
