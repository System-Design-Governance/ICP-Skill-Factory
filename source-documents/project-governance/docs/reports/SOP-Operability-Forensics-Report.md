# SOP 傻瓜可執行性鑑識報告

## SOP-Operability-Forensics-Report

**報告類型**：SOP Operability Forensics Analysis
**報告日期**：2026-02-09
**分析範圍**：Power Platform 治理系統建置手冊（00-07 文件 + Appendix A）
**分析目的**：判斷 SOP 是否達到「傻瓜可執行」標準

---

## 執行摘要（總評結論）

| 評估維度 | 結論 | 說明 |
|---------|:----:|------|
| **整體可操作性** | **B+** | 核心流程可執行，但存在若干會卡住新進人員的缺口 |
| **P0 嚴重問題** | 3 項 | 將導致執行中斷，必須修補 |
| **P1 高風險問題** | 7 項 | 將導致誤用或數據不一致，應優先修補 |
| **P2 中風險問題** | 8 項 | 造成小摩擦或語義模糊，建議修補 |

### 總評

本 SOP 文件集在**架構設計、流程覆蓋度、驗證檢查點**三方面達到優秀水準，具備以下優點：

1. **明確的章節相依性宣告**：00-index.md 明確指出禁止跳章、每章有 Gate 檢查點
2. **傻瓜照做格式**：各章採用「操作路徑 + 設定值 + 驗證結果」三段式結構
3. **Flow-only 欄位保護完整**：三道防線架構（FLS + GOV-017 + GOV-018）設計完備
4. **測試案例覆蓋充分**：E2E-001~013 + AC-001~008 涵蓋主流程與反作弊

然而，存在以下會導致「傻瓜卡住」的問題：

- **文件間循環相依**：04 文件需要 05 的 Flow，05 文件要求返回 04 連接，但未明確說明順序
- **重複內容造成混淆**：GOV-017/018/019 在 05 與 06 文件皆有詳細步驟，版本難以追溯
- **占位符未完整列表**：Service Principal GUID、Email 地址等占位符散落各處，缺乏統一清單

**結論**：**有條件可執行**。在修補 P0 問題後，新進人員可依 SOP 完成治理系統建置。

---

## SOP 入口與路徑圖

### 文件清單與相依關係

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    Power Platform 治理系統 SOP 路徑圖                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  00-index.md（導讀）                                                      │
│       │                                                                  │
│       ▼                                                                  │
│  01-prerequisites-and-environment.md（環境建置）                          │
│       │ ✓ Environment Ready Gate（30 項檢核）                             │
│       ▼                                                                  │
│  02-dataverse-data-model-and-security.md（資料模型）                      │
│       │ ✓ Data Model Ready Gate                                          │
│       │ ⚠ 建立 Choice 欄位時引用「第 5 章」但實際在本章建立               │
│       ▼                                                                  │
│  03-sharepoint-architecture.md（SharePoint）                              │
│       │ ✓ SharePoint Ready Gate                                          │
│       ▼                                                                  │
│  04-powerapps-forms.md（Power Apps）                                      │
│       │ ⚠ 需要 05 文件的 Flow 才能完成                                    │
│       │ ↺ 循環相依                                                        │
│       ▼                                                                  │
│  05-core-flows-implementation-runbook.md（Flow 施工）【唯一實作依據】      │
│       │ ✓ Flow Ready Gate                                                │
│       │ ⚠ 要求「返回 04 章完成 Flow 連接」                                │
│       │ ⚠ GOV-017/018/019 內容與 06 重複                                  │
│       ▼                                                                  │
│  06-guardrails-and-anti-cheating.md（Guardrails）                         │
│       │ ⚠ 與 05 文件 GOV-017/018/019 步驟重複                             │
│       │ ⚠ 含 5 個 TODO 項目（占位符未填寫）                               │
│       ▼                                                                  │
│  07-testing-and-acceptance.md（測試與驗收）                               │
│       │ ✓ E2E-001~013 完整測試案例                                       │
│       │ ✓ AC-001~008 反作弊測試案例                                      │
│       ▼                                                                  │
│  [完成]                                                                   │
│                                                                          │
│  appendix/A-core-flows-specification.md                                   │
│       │ ⚠ 僅供參考，禁止作為實作依據（00-index 已聲明）                   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### 實際執行順序建議

| 順序 | 文件 | 執行內容 | 相依檢查 |
|:----:|------|---------|---------|
| 1 | 00-index.md | 閱讀導讀，理解文件定位 | 無 |
| 2 | 01-prerequisites | 建立環境、Service Principal、Security Groups | 無 |
| 3 | 02-dataverse | 建立 Tables、Columns、Choice Sets、FLS | 01 Environment Ready Gate |
| 4 | 03-sharepoint | 建立 Site、Document Libraries、權限 | 01 Environment Ready Gate |
| 5 | 04-powerapps **階段一** | 建立 App 框架、表單 UI（不含 Flow 連接） | 02 + 03 Ready Gate |
| 6 | 05-core-flows | 建立所有 GOV-001~019 Flow | 02 + 03 Ready Gate |
| 7 | 04-powerapps **階段二** | 連接 Flow 至 Power Apps、發佈 | 05 Flow Ready Gate |
| 8 | 06-guardrails | **僅閱讀確認**（實作已在 05 完成） | 05 Ready Gate |
| 9 | 07-testing | 執行 E2E + AC 測試案例 | 04 階段二 + 05 Ready Gate |

---

## P0 嚴重問題清單（將導致執行中斷）

### P0-001：文件間循環相依未明確解法

| 項目 | 內容 |
|------|------|
| **問題描述** | 04 文件需要 05 的 Flow 才能完成 Power Apps 建置；05 文件末尾要求「返回 04 章完成 Flow 連接」。新進人員無法判斷應先完成哪個文件。 |
| **影響範圍** | 04-powerapps-forms.md、05-core-flows-implementation-runbook.md |
| **卡住情境** | 執行者在 04 章建立表單時發現需要 Flow URL，但 Flow 尚未建立；跳到 05 章建立 Flow 後又被要求返回 04 章。 |
| **具體位置** | 04 文件 FORM-001 Power Apps 表單呼叫 Flow 設定；05 文件末尾「完成本章後必須返回執行的步驟」 |
| **建議修補** | 在 04 文件開頭新增「本章分兩階段」說明，明確定義階段一（UI 建置）可獨立完成，階段二（Flow 連接）需等 05 章完成後返回執行。 |

### P0-002：GOV-017/018/019 在 05 與 06 文件重複

| 項目 | 內容 |
|------|------|
| **問題描述** | GOV-017（Guardrail Monitor）、GOV-018（Compliance Reconciler）、GOV-019（SLA Monitor）在 05 文件與 06 文件皆有完整施工步驟，且內容不完全一致。 |
| **影響範圍** | 05-core-flows-implementation-runbook.md（1463-1678 行）、06-guardrails-and-anti-cheating.md（全文） |
| **卡住情境** | 執行者不知道應依據哪份文件建置 GOV-017/018/019，且兩份文件的步驟編號、細節略有差異。 |
| **具體位置** | 05 文件「Guardrail 監控機制實作」區塊 vs 06 文件全文 |
| **建議修補** | 06 文件定位為「設計說明與稽核參考」，移除施工步驟，保留架構說明、監控指標、通知範本；05 文件為唯一施工依據。 |

### P0-003：Counter List 初始化步驟缺失

| 項目 | 內容 |
|------|------|
| **問題描述** | GOV-001 Flow 依賴 Counter List 產生 RequestID，但無任何文件明確說明如何初始化 Counter List（建立記錄、設定初始值）。 |
| **影響範圍** | 02-dataverse-data-model-and-security.md、05-core-flows-implementation-runbook.md |
| **卡住情境** | 執行者建立 Counter List 資料表後，首次執行 GOV-001 Flow 會因 Counter List 無記錄而失敗。 |
| **具體位置** | 02 文件 gov_counterlist 資料表建立（僅定義結構，無初始化步驟） |
| **建議修補** | 在 02 文件 gov_counterlist 章節末尾新增「初始化步驟」：建立一筆記錄，CounterType = 'RequestID'，CurrentValue = 0。 |

---

## P1 高風險問題清單（將導致誤用或數據不一致）

### P1-001：02 文件引用「第 5 章建立」的 Choice Set 實際在本章建立

| 項目 | 內容 |
|------|------|
| **問題描述** | 02 文件第 311 行：「Sync this choice with 選擇 gov_currentgate（全域選項集，將在第 5 章建立）」，但全域選項集實際上應在 02 文件中建立，05 文件不負責建立選項集。 |
| **影響範圍** | 02-dataverse-data-model-and-security.md |
| **誤用情境** | 執行者跳過建立選項集，等待 05 章提供，導致 02 章無法完成。 |
| **建議修補** | 刪除「將在第 5 章建立」，改為「請先在下方『全域選項集建立』章節建立此選項集」。 |

### P1-002：Service Principal GUID 占位符散落各處

| 項目 | 內容 |
|------|------|
| **問題描述** | 多處使用 `<Flow-Service-Principal-ID>` 或 `{Flow Service Principal User ID}` 占位符，但無統一表格列出所有需替換的位置。 |
| **影響範圍** | 05 文件、06 文件 |
| **誤用情境** | 執行者遺漏部分替換，導致 GOV-017 篩選條件錯誤，無法正確排除 Flow 自身的修改。 |
| **建議修補** | 在 01 文件「Service Principal 建立」章節末尾，新增「占位符替換清單」表格，列出所有需替換 GUID 的文件與位置。 |

### P1-003：06 文件含 5 個未完成 TODO 項目

| 項目 | 內容 |
|------|------|
| **問題描述** | 06 文件末尾「TODO 清單」包含 5 個未填寫的項目（TODO-001~005），包括 Service Principal GUID、Teams Channel ID 等。 |
| **影響範圍** | 06-guardrails-and-anti-cheating.md（900-911 行） |
| **誤用情境** | 執行者依據 06 文件建置 GOV-017，但缺乏必要的 GUID 與 Channel ID，無法完成設定。 |
| **建議修補** | 將 TODO 項目移至 01 文件的「環境準備清單」，確保在環境準備階段即收集所有必要資訊。 |

### P1-004：Email 地址占位符未提供替換指引

| 項目 | 內容 |
|------|------|
| **問題描述** | 多處使用 `GOV-GovernanceLead@contoso.com`、`GOV-SystemAdmin@contoso.com` 等占位符，但未明確說明應替換為實際組織的 Email 地址或 Security Group。 |
| **影響範圍** | 05 文件、06 文件、07 文件 |
| **誤用情境** | 執行者直接使用 `@contoso.com` 地址，通知無法送達。 |
| **建議修補** | 在 01 文件新增「通知收件人清單」表格，明確對應每個角色的實際 Email 或 Security Group。 |

### P1-005：測試案例 HTTP URL 使用 `{{base_url}}` 未定義

| 項目 | 內容 |
|------|------|
| **問題描述** | 07 文件測試案例使用 `{{base_url}}/gov_projectregistries` 格式，但未說明 `{{base_url}}` 的取得方式。 |
| **影響範圍** | 07-testing-and-acceptance.md |
| **誤用情境** | 執行者不知道如何取得 Dataverse 環境的 Base URL，無法執行 HTTP 驗證。 |
| **建議修補** | 在 07 文件開頭新增「測試環境準備」章節，說明 Base URL 格式為 `https://{org}.api.crm.dynamics.com/api/data/v9.2`，並提供取得方式。 |

### P1-006：BOM Registry 欄位在 07 測試案例出現但 02 未完整定義

| 項目 | 內容 |
|------|------|
| **問題描述** | 07 文件 E2E-010~013 測試 BOM Registry，但 02 文件的 gov_bomregistry 欄位定義未包含部分測試案例引用的欄位（如 `gov_terminationreason`、`gov_closuredate`）。 |
| **影響範圍** | 02-dataverse-data-model-and-security.md、07-testing-and-acceptance.md |
| **誤用情境** | 執行者依 02 文件建立 BOM Registry 後，07 文件測試案例無法執行。 |
| **建議修補** | 檢視 07 文件測試案例引用的所有欄位，確保 02 文件有完整定義。 |

### P1-007：專案終止欄位（TerminationReason 等）未在 02 文件定義

| 項目 | 內容 |
|------|------|
| **問題描述** | 07 文件 E2E-008 測試專案終止流程，引用 `gov_terminationreason`、`gov_terminationdate`、`gov_terminatedby` 欄位，但 02 文件 gov_projectregistry 未定義這些欄位。 |
| **影響範圍** | 02-dataverse-data-model-and-security.md、07-testing-and-acceptance.md |
| **誤用情境** | 執行者完成 02 文件後發現無法執行 E2E-008 測試。 |
| **建議修補** | 在 02 文件 gov_projectregistry 欄位清單補充終止相關欄位。 |

---

## P2 中風險問題清單（造成小摩擦或語義模糊）

### P2-001：驗證步驟缺乏具體預期值

| 項目 | 內容 |
|------|------|
| **問題描述** | 部分「確認此步驟成功」的驗證點僅描述「應成功」，缺乏具體預期值或錯誤訊息比對。 |
| **影響範圍** | 05 文件多處驗證步驟 |
| **摩擦情境** | 執行者不確定「成功」的具體表現為何。 |
| **建議修補** | 為每個驗證步驟補充具體預期值（如 HTTP 200、特定欄位值、Flow Run History 顯示 Succeeded）。 |

### P2-002：Publisher Prefix 說明不足

| 項目 | 內容 |
|------|------|
| **問題描述** | 文件使用 `gov_` 作為 Publisher Prefix，但未說明如何在環境中設定此 Prefix。 |
| **影響範圍** | 01 文件、02 文件 |
| **摩擦情境** | 若環境 Publisher Prefix 不是 `gov_`，所有 Schema Name 都需要調整。 |
| **建議修補** | 在 01 文件新增「Publisher Prefix 設定」步驟，說明如何確認或設定 Publisher Prefix 為 `gov_`。 |

### P2-003：OptionSet 數值對照表分散

| 項目 | 內容 |
|------|------|
| **問題描述** | OptionSet 數值對照表（如 CurrentGate 的 100000000~100000004）分散在 02 文件與 05 文件附錄，查閱不便。 |
| **影響範圍** | 02 文件、05 文件 |
| **摩擦情境** | 執行者需在多處查找 OptionSet 數值。 |
| **建議修補** | 在 02 文件集中定義所有 OptionSet 數值對照表，05 文件附錄僅引用 02 文件。 |

### P2-004：Connection Reference 命名規則僅在 05 文件說明

| 項目 | 內容 |
|------|------|
| **問題描述** | Connection Reference 命名規則（CR-Dataverse-SPN、CR-SharePoint-SPN 等）僅在 05 文件說明，但 01 文件建立 Service Principal 時應同步建立。 |
| **影響範圍** | 01 文件、05 文件 |
| **摩擦情境** | 執行者在 05 章發現需要 Connection Reference，需返回建立。 |
| **建議修補** | 在 01 文件 Service Principal 章節後新增「Connection Reference 預建立」步驟。 |

### P2-005：SharePoint 權限設定與 Flow Service Principal 關聯不明確

| 項目 | 內容 |
|------|------|
| **問題描述** | 03 文件說明 Flow Service Principal 為唯一 SharePoint 寫入者，但未明確說明如何將 Service Principal 加入 SharePoint Site 權限。 |
| **影響範圍** | 03-sharepoint-architecture.md |
| **摩擦情境** | 執行者不知道如何授權 Service Principal 存取 SharePoint。 |
| **建議修補** | 在 03 文件「權限設定」章節新增「授權 Service Principal 存取 SharePoint」步驟。 |

### P2-006：05 文件 Flow 依賴順序圖位置過後

| 項目 | 內容 |
|------|------|
| **問題描述** | 05 文件的 Flow 依賴順序圖在文件後段，執行者可能在建立 GOV-001 時不知道依賴關係。 |
| **影響範圍** | 05-core-flows-implementation-runbook.md |
| **摩擦情境** | 執行者可能先建立錯誤順序的 Flow。 |
| **建議修補** | 將 Flow 依賴順序圖移至 05 文件開頭，作為「建置順序總覽」。 |

### P2-007：07 文件測試帳號命名不一致

| 項目 | 內容 |
|------|------|
| **問題描述** | 07 文件使用 `testuser1@contoso.com`、`testgovlead@contoso.com` 等，部分測試案例使用不同命名。 |
| **影響範圍** | 07-testing-and-acceptance.md |
| **摩擦情境** | 執行者需建立多個測試帳號，但清單不完整。 |
| **建議修補** | 在 07 文件開頭新增「測試帳號清單」表格，統一列出所有測試所需帳號與角色。 |

### P2-008：附錄 A 定位說明在多處重複

| 項目 | 內容 |
|------|------|
| **問題描述** | 「附錄 A 僅供參考、禁止作為實作依據」的聲明在 00 文件與 05 文件重複，但語氣略有不同。 |
| **影響範圍** | 00-index.md、05-core-flows-implementation-runbook.md |
| **摩擦情境** | 執行者對附錄 A 的定位產生疑惑。 |
| **建議修補** | 統一聲明語言，僅在 00 文件定義，其他文件引用 00 文件即可。 |

---

## 端到端演練摘要

### 模擬情境：新進 Power Platform 開發人員首次建置治理系統

| 階段 | 執行結果 | 卡點說明 |
|------|---------|---------|
| **閱讀 00-index** | ✅ 順利 | 清楚理解文件結構與禁止行為 |
| **執行 01-prerequisites** | ⚠ 輕微卡點 | 30 項 Environment Ready Gate 完整，但 Service Principal GUID 記錄位置不明確 |
| **執行 02-dataverse** | ⚠ 輕微卡點 | Choice 欄位建立時被「第 5 章建立」誤導；Counter List 無初始化步驟 |
| **執行 03-sharepoint** | ✅ 順利 | 步驟完整，權限設定清晰 |
| **執行 04-powerapps** | ❌ **卡住** | 需要 Flow URL 才能完成表單建置，但 Flow 尚未建立 |
| **跳至 05-core-flows** | ⚠ 輕微卡點 | GOV-001 依賴 Counter List，但 Counter List 無記錄導致首次執行失敗 |
| **返回 04-powerapps** | ✅ 順利 | 連接 Flow 後可完成發佈 |
| **閱讀 06-guardrails** | ⚠ **混淆** | 發現 GOV-017/018/019 步驟與 05 文件重複，不知以哪份為準 |
| **執行 07-testing** | ⚠ 輕微卡點 | `{{base_url}}` 未定義；部分測試案例引用的欄位在 02 文件未定義 |

### 演練結論

1. **可完成度**：約 85%。在遇到循環相依時需自行判斷順序，有一定經驗者可完成。
2. **首次執行時間**：預估 3-5 個工作日（含除錯與查找時間）。
3. **修補後預估時間**：2-3 個工作日。

---

## 建議修補策略

### 優先順序

| 優先級 | 修補項目 | 工作量 | 影響範圍 |
|:------:|---------|:------:|---------|
| **1** | P0-001 循環相依解法 | 小 | 04 文件 |
| **2** | P0-002 GOV-017/018/019 重複內容 | 中 | 05、06 文件 |
| **3** | P0-003 Counter List 初始化 | 小 | 02 文件 |
| **4** | P1-001 Choice Set 引用修正 | 小 | 02 文件 |
| **5** | P1-002~004 占位符統一清單 | 中 | 01 文件 |
| **6** | P1-005~007 欄位定義補齊 | 中 | 02、07 文件 |
| **7** | P2-001~008 雜項修補 | 小 | 各文件 |

### 修補原則

1. **不修改 Dataverse 資料模型**：僅補充文件說明，不新增 Entity 或欄位（除非 02 文件遺漏）
2. **不修改 Gate 流程**：Gate 邏輯不變，僅補充文件說明
3. **僅 SOP 層面修補**：透過新增章節、調整順序、補充說明來解決問題

---

## 附錄：逐文件檢核摘要

### 00-index.md
- **優點**：明確宣告閱讀順序、禁止行為、建置方式
- **問題**：無（本文件為導讀，不含施工步驟）

### 01-prerequisites-and-environment.md
- **優點**：30 項 Environment Ready Gate 完整，Service Principal 建立步驟詳盡
- **問題**：缺乏 Connection Reference 預建立、占位符統一清單

### 02-dataverse-data-model-and-security.md
- **優點**：Entity 三層分類清晰、Flow-only 欄位定義完整、FLS 設定詳盡
- **問題**：Choice Set 引用錯誤、Counter List 無初始化、部分測試案例欄位未定義

### 03-sharepoint-architecture.md
- **優點**：資料夾結構清晰、權限模型明確
- **問題**：Service Principal 授權步驟可加強

### 04-powerapps-forms.md
- **優點**：11 個表單定義完整、驗證邏輯清楚
- **問題**：循環相依未解決，需明確兩階段建置

### 05-core-flows-implementation-runbook.md
- **優點**：19 條 Flow 施工步驟完整、Pre-check 清單詳盡、錯誤代碼完整
- **問題**：與 06 文件 GOV-017/018/019 重複

### 06-guardrails-and-anti-cheating.md
- **優點**：三道防線架構說明清晰、通知範本完整
- **問題**：施工步驟與 05 文件重複、含 5 個 TODO 項目

### 07-testing-and-acceptance.md
- **優點**：E2E + AC 測試案例覆蓋充分、預期結果明確
- **問題**：{{base_url}} 未定義、部分欄位在 02 文件未定義

---

**報告結束**

**鑑識執行人員**：Claude Opus 4.5
**鑑識日期**：2026-02-09
**鑑識工具**：SOP Operability Forensics Framework v1.0
