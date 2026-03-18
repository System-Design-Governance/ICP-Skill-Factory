# Power Automate 核心 Flows 治理內核架構憲法

**文件編號**：IMPL-05A-RUNBOOK
**版本**：10.0
**最後更新**：2026-03-05
**適用對象**：第一次實作 Power Platform 的工程人員
**文件性質**：Single Source of Truth（唯一權威施工依據）
**成熟度等級**：L5（制度級 Institutional Governance）

> **本文件為 Flow 實作的唯一權威依據。** 禁止參照附錄中的設計規格文件進行實作。
> Flow 不得硬編碼任何業務常數（含資料夾名稱、OptionSet 映射）。Dataverse 為唯一事實來源。
> 所有 Parent Flow 回傳必須包含 `FlowRunId` 以支援端對端追溯。
> v5.0 修訂方向：制度級成熟化改造 — Error Envelope 標準化、FlowRunId Writeback、Counter 併發策略、Gate 狀態轉換矩陣、稽核不可變性原則、IEC 62443 證據鏈映射。

---

## Flow Governance Design Principles（架構原則）

本文件所有 Flow 必須遵循以下不可違反的治理原則：

| # | 原則 | 說明 | 違反後果 |
|:-----|:--------------------------|:----------------------------------------------|:-------------------------------|
| P-01 | **Dataverse 是唯一事實來源** | Flow 不得硬編碼業務常數（如 DocumentType 清單、Gate 矩陣、資料夾名稱、OptionSet 映射）。所有業務資料必須從 Dataverse 讀取 | 變更時必須改 Flow，無法由業務人員維護 |
| P-02 | **Trigger 單一化** | Power Apps 觸發的 Flow 一律使用 `Power Apps (V2)` Trigger。Child Flow 一律使用 `Manually trigger a flow`。Scheduled Flow 一律使用 `Recurrence` | Trigger 混亂導致呼叫失敗 |
| P-03 | **GUID 一律為 Text** | 所有 Dataverse 主鍵（`gov_*id`）在 Flow 中以 Text 類型傳遞，不得使用 integer | 型別不匹配導致查詢失敗 |
| P-04 | **回傳模式統一（Error Envelope）** | 所有 Power Apps 觸發的 Flow 使用 `Respond to a PowerApp or flow` 回傳，必須包含完整 Error Envelope：StatusCode / Status / ErrorCode / ErrorStage / Message / FlowRunId / Timestamp | Power Apps 無法正確處理回傳或追溯 |
| P-05 | **OptionSet 不可混用** | 所有 OptionSet 值必須使用 Dataverse 定義的 807660000 系列數值，禁止使用任意整數（如 1, 2, 3） | 資料不一致，查詢失敗 |
| P-06 | **Counter List 序號** | RequestID 必須使用 Counter List 機制，禁止使用 `guid()` 產生 | 序號不連續，無法追蹤 |
| P-07 | **Child Flow 鎖定** | 所有 Child Flow 必須勾選「Only other flows can trigger」，禁止手動觸發 | 繞過 Parent Flow 的 Pre-check |
| P-08 | **補零使用 concat + substring** | 禁止使用 `padLeft`（Power Automate 不支援）。補零使用 `concat('0000', ...) + substring + sub + length`。見下方「P-08 標準補零範本」 | Flow 執行失敗 |
| P-09 | **主路徑零 HTTP** | 主施工路徑不得出現 HTTP Request/Response。HTTP 僅限 Guardrail 查詢 Audit API | Trigger 混亂，回傳格式不一致 |
| P-10 | **MVP / Hardened 雙軌** | 開發階段允許 MVP 模式（個人連線），但 PROD 必須為 Hardened 模式（SPN + FLS） | 生產環境無法維護 |
| P-11 | **Folder Baseline Dataverse 化** | SharePoint 資料夾名稱不得硬寫於 Flow。必須從 Dataverse `gov_documentfolderbaseline` 讀取資料夾結構 | 資料夾異動時必須改 Flow |
| P-12 | **FlowRunId 端對端追溯** | 所有 Parent Flow 回傳必須包含 `FlowRunId`（`workflow()?['run']?['name']`），寫入 Review Decision Log 並回傳給 Power Apps | 無法追溯 Flow 執行記錄 |
| P-13 | **OptionSet Mapping Table 去耦合** | 禁止在 Flow 中以 Switch/if 將文字硬轉為 OptionSet 數值。必須從 Dataverse Mapping Table 讀取對應關係 | OptionSet 異動時必須改 Flow |
| P-14 | **稽核記錄不可變（Audit Immutability）** | Review Decision Log、Governance Violation Log 等稽核記錄一經建立禁止 Update / Delete。如需修正，必須新增一筆修正記錄（Correction Record）並引用原記錄 GUID | 稽核證據被竄改，無法通過 IEC 62443 稽核 |
| P-15 | **Gate 狀態轉換合法性** | CurrentGate 只能依合法路徑遞進（見「Gate State Transition Matrix」章節）。任何繞過合法轉換的操作由 Guardrail 偵測並記錄違規 | Gate 被非法跳級，審查記錄不完整 |
| P-16 | **FlowRunId Writeback** | 所有 Parent Flow 執行完成後，必須將 FlowRunId 與執行狀態回寫至 Project Registry（`gov_lastflowrunid` / `gov_lastflowstatus`），形成可查詢的執行歷史 | 無法從 Dataverse 端查詢最近一次 Flow 執行狀態 |

#### P-08 標準補零範本（唯一核准方式，可直接貼入 Expression 欄）

> **以下為唯一核准的補零運算式。** 禁止使用 `padLeft`、`formatNumber` 或任何其他方式。

**補零至 4 位（適用 RequestID 序號）**——直接貼入 Compose 的 Expression 欄位：

```
substring(concat('0000', string(variables('varNextSeq'))), sub(length(concat('0000', string(variables('varNextSeq')))), 4), 4)
```

**原理拆解**（不需要貼，僅供理解）：

```
假設 varNextSeq = 7（整數）

第 1 步：string(variables('varNextSeq'))         → '7'          ← 整數必須先用 string() 轉為文字
第 2 步：concat('0000', '7')                     → '00007'      ← 前面補 4 個零
第 3 步：length('00007')                          → 5
第 4 步：sub(5, 4)                                → 1            ← 起始位置 = 總長度 - 目標位數
第 5 步：substring('00007', 1, 4)                 → '0007'       ← 取最後 4 位
```

> **整數 → 字串注意事項**：
> - `variables('varNextSeq')` 的型別為 Integer，**不能直接 concat**，必須用 `string()` 包裹
> - `int(formatDateTime(utcNow(), 'yyyy'))` 回傳整數，串接 RequestID 時必須用 `string()` 轉換：`string(outputs('Compose-CurrentYear'))`
> - 若忘記 `string()`，Power Automate 會報錯：`InvalidTemplate: Unable to process template language expressions`

---

## Trigger 與 Source of Invocation 規範

### Trigger 類型矩陣

| Trigger 類型 | 適用 Flow | 呼叫方式 | 備註 |
|:--------------------------|:----------------------|:----------------------------------------------|:-------------------------------|
| **Power Apps (V2)** | GOV-001, GOV-002, GOV-005, GOV-022, GOV-023, GOV-024 | Power Apps 中以 `FlowName.Run(參數...)` 呼叫 | Input 全部為 Text；Output 透過 Respond to a PowerApp or flow |
| **Manually trigger a flow** | GOV-003, GOV-004, GOV-013A, GOV-013B, GOV-014, GOV-015, GOV-016 | Parent Flow 中以「Run a Child Flow」動作呼叫 | 必須勾選「Only other flows can trigger」`[Governance Critical Control]` |
| **Recurrence** | GOV-017, GOV-018, GOV-019 | 依排程自動執行 | 不得由 Power Apps 或其他 Flow 觸發 |

### 禁止使用的 Trigger

| 禁止 Trigger | 原因 | 替代方案 |
|:--------------------------|:----------------------------------------------|:-------------------------------|
| When a HTTP request is received | 無法控制呼叫來源、無內建驗證、回傳格式不統一 | Power Apps (V2) 或 Manually trigger a flow |
| Automated — When a record is created/modified | 可能觸發連鎖反應、難以控制執行順序 | 由 Parent Flow 明確呼叫 |

---

## Flow 類型矩陣

| Flow ID | 名稱 | 類型 | Trigger | 呼叫來源 | 可直接被 Power Apps 呼叫 |
|:--------|:----------------------------------------------|:----------|:----------------------|:----------------------|:----------------------|
| GOV-001 | Create Project | Parent | Power Apps (V2) | FORM-001 | ✅ |
| GOV-002 | Gate Transition Request | Parent | Power Apps (V2) | FORM-002 | ✅ |
| GOV-003 | Gate Approval Orchestrator | Child | Manually trigger | GOV-002 | ❌ |
| GOV-004 | Risk Acceptance | Child | Manually trigger | GOV-002 | ❌ |
| GOV-005 | Document Upload and Register | Parent | Power Apps (V2) | FORM-003 | ✅ |
| GOV-013A | Risk Score Calculator | Child | Manually trigger | GOV-002 | ❌ |
| GOV-013B | Risk Aggregator | Child | Manually trigger | GOV-002 | ❌ |
| GOV-014 | Document Freeze | Child | Manually trigger | GOV-003 | ❌ |
| GOV-015 | Notification Handler | Child | Manually trigger | GOV-001/002/003/005 等 | ❌ |
| GOV-016 | Rework Loop Handler | Child | Manually trigger | GOV-003 | ❌ |
| GOV-017 | Guardrail Monitor | Scheduled | Recurrence (1h) | 系統排程 | ❌ |
| GOV-018 | Compliance Reconciler | Scheduled | Recurrence (1d) | 系統排程 | ❌ |
| GOV-019 | SLA Monitor | Scheduled | Recurrence (1d) | 系統排程 | ❌ |

---

## 共通回傳模型（Unified Response Model）

### Power Apps 觸發 Flow 回傳標準

所有由 Power Apps 觸發的 Flow（GOV-001, GOV-002, GOV-005）必須使用 `Respond to a PowerApp or flow` 動作回傳，且**必須**遵循以下 **Canonical Error Envelope（v5.0 標準回傳信封）**：

| 欄位 | 類型 | 必要 | 成功時 | 失敗時 | 說明 |
|:--------------------------|:----------|:------:|:----------------------|:----------------------|:----------------------------------------------|
| StatusCode | Number | ✓ | `200` | `400` / `500` | HTTP 語意狀態碼。200 = 成功，400 = 業務驗證失敗（Pre-check / Guard Clause），500 = 系統例外（Catch） |
| Status | Text | ✓ | `Success` | `Failed` | 文字狀態，供 Power Apps 判斷 |
| ErrorCode | Text | ✓ | （空白） | `ERR-001-xxx` | 錯誤代碼（見本文件「錯誤代碼與處置方式對照」） |
| ErrorStage | Text | ✓ | （空白） | 階段名稱 | 失敗發生的 Flow 階段。如 `PreCheck`、`CounterUpdate`、`DataverseWrite`、`SharePointProvision`、`Notification`、`CatchHandler` |
| Message | Text | ✓ | 成功訊息 | 錯誤訊息 | 結果訊息，Power Apps 端必須以 `Notify()` 顯示 |
| PrimaryId | Text | ✓ | 主記錄 GUID | （空白） | 主要產出記錄的 GUID（如 ProjectRowId、ReviewRowId、DocumentRegisterRowId） |
| PrimaryLink | Text | ✗ | URL | （空白） | 主要產出連結（如 SharePoint URL），無則空白 |
| FlowRunId | Text | ✓ | Run ID | Run ID | `workflow()?['run']?['name']`，用於端對端追溯 |
| Timestamp | Text | ✓ | ISO 8601 | ISO 8601 | `utcNow()`，Flow 回應時的 UTC 時間戳記 |

> **StatusCode 語意規則（v5.0 新增）**：
> - **200**：所有業務邏輯成功完成（包含子 Flow 呼叫成功）
> - **400**：業務驗證失敗。包含 Pre-check 不通過（如 ERR-002-001 專案不存在）、Guard Clause 觸發（如 ERR-001-COUNTER 記錄不存在）、文件驗證失敗等。ErrorStage 標示失敗階段
> - **500**：系統例外。Try-Catch 中的 Catch 路徑觸發，表示非預期錯誤。ErrorStage = `CatchHandler`

> **ErrorStage 標準值域（v5.0 新增）**：
>
> | ErrorStage 值 | 觸發時機 | 範例 |
> |:--------------------------|:----------------------------------------------|:-------------------------------|
> | `PreCheck` | Pre-check 驗證失敗（專案不存在、權限不足、狀態不允許） | ERR-002-001, ERR-002-003 |
> | `CounterUpdate` | Counter List 讀取或更新失敗 | ERR-001-COUNTER |
> | `UserLookup` | 使用者 email Lookup 查無結果 | ERR-001-USER |
> | `OptionSetMapping` | OptionSet 映射讀取失敗 | ERR-001-011 |
> | `DataverseWrite` | Dataverse 寫入失敗 | ERR-005-002 |
> | `SharePointProvision` | SharePoint 資料夾 / 檔案建立失敗 | PROVISION_FAIL |
> | `DocumentValidation` | 文件類型 / 映射驗證失敗 | ERR-005-006 |
> | `ApprovalProcess` | 審批流程失敗 | ERR-003-001 |
> | `Notification` | 通知發送失敗（非致命） | WARN-015-001 |
> | `CatchHandler` | Try-Catch 的 Catch 路徑觸發 | ERR-SYSTEM-500 |

> **FlowRunId（P-12 原則）**：每次 Flow 執行產生唯一的 Run ID，Power Apps 可用於查詢 Flow Run History、
> 關聯 Review Decision Log 的 `gov_triggerflowrunid` 欄位，實現完整的端對端稽核追溯鏈。

> **Timestamp（v5.0 新增）**：使用 `utcNow()` 產生 ISO 8601 格式時間戳記（如 `2026-02-14T08:30:00Z`）。
> 此欄位記錄 Flow 回應當下的精確時間，可用於：
> - 比對 Flow Run History 時間軸
> - 跨時區稽核一致性
> - 效能分析（Trigger 時間 vs 回應時間差）

> **Power Apps 端必須接收並顯示 Message（落地必做）**：
> Power Apps 呼叫 Flow 後，**必須**檢查回傳的 `Status` 欄位，若為 `Failed`，則以 `Notify()` 函數顯示 `Message` 欄位內容。
> 範例 Power Apps 公式：
> ```
> If(
>     varFlowResult.Status = "Failed",
>     Notify(
>         varFlowResult.Message & " [" & varFlowResult.ErrorCode & "]",
>         NotificationType.Error
>     )
> )
> ```
> 若不顯示 Message，使用者在操作失敗時將看不到任何錯誤原因，無法自行排查。

各 Flow 的 PrimaryId / PrimaryLink 對應：

| Flow | PrimaryId 來源 | PrimaryLink 來源 | 額外回傳欄位 |
|:--------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| GOV-001 | gov_projectregistryid | SharePoint 專案資料夾 URL | RequestID, FolderLink, FlowRunId, Timestamp |
| GOV-002 | Review Decision Log GUID | （無） | ReviewRowId, FlowRunId, Timestamp |
| GOV-005 | gov_documentregisterid | SharePoint 檔案 URL | SharePointFileLink, DocumentRegisterRowId, FlowRunId, Timestamp |

### Child Flow 回傳標準

所有 Child Flow 使用 `Respond to a PowerApp or flow` 回傳，最低欄位：

| 欄位 | 類型 | 必要 | 說明 |
|:--------------------------|:----------------------|:------:|:----------------------------------------------|
| StatusCode | Number | ✓ | `200` / `400` / `500`（與 Parent Flow 同語意） |
| Status | Text | ✓ | `Success` 或 `Failed` |
| ErrorCode | Text | ✓ | 錯誤代碼（成功時為空白） |
| ErrorMessage | Text | ✓ | 失敗時的錯誤訊息（成功時為空白） |

> **Child Flow 不需回傳 FlowRunId / Timestamp**：因為 Child Flow 的 Run ID 由 Parent Flow 的 Run History 自動追溯。
> Parent Flow 負責在最終 Respond 中帶入自身的 FlowRunId 與 Timestamp。

---

## 共通 Error Handling 模式（Try-Catch Scope）

所有 Flow 必須實作以下 Try-Catch 結構：

```
Flow 結構（Error Envelope v5.0）：
┌─ Trigger
├─ Initialize variables（若需要）
├─ Scope: Try-MainLogic
│   ├─ Pre-check（驗證）→ 失敗時 StatusCode=400, ErrorStage=PreCheck
│   ├─ 主要邏輯
│   ├─ FlowRunId Writeback（P-16 原則）
│   └─ Respond to a PowerApp or flow（成功 → StatusCode=200）
└─ Scope: Catch-ErrorHandler
    ├─ Compose: 擷取錯誤訊息
    ├─ FlowRunId Writeback（P-16 原則，Status=Failed）
    └─ Respond to a PowerApp or flow（失敗 → StatusCode=500, ErrorStage=CatchHandler）
```

**Catch Scope 設定**：
- Configure run after → 取消「成功」→ 勾選「已失敗」與「已逾時」

**ErrorMessage 擷取表達式**：
```
@{coalesce(result('Try-MainLogic')?[0]?['error']?['message'], '未知錯誤')}
```

> **注意**：同一 Flow 中只能有一個 `Respond to a PowerApp or flow` 動作會實際執行。
> Try 成功與 Catch 失敗中的 Respond 互斥，符合此限制。

---

## Flow Concurrency Policy

| Flow | Concurrency | Parallelism | Key | 原因 |
|:--------|:----------------------|:----------------------|:----------------------------------------------|:----------------------------------------------|
| GOV-001 | **Required（必須啟用）** | 1 | N/A | 專案建立通常低頻，但 Counter List 需序列化保護。跳過此設定將導致 RequestID 重複（Counter List Race Condition） |
| GOV-002 | **必須開啟** | 1 | `triggerBody()['ProjectId']` | 同一專案不可同時有兩筆 Gate 申請 |
| GOV-003 | 不開啟 | N/A | N/A | 由 GOV-002 控制，單一 Parent 不會重複呼叫 |
| GOV-004 | 不開啟 | N/A | N/A | 由 GOV-002 控制 |
| GOV-005 | **必須開啟** | 1 | `concat(triggerBody()['ProjectId'], '-', triggerBody()['DocumentType'])` | 使用 ProjectId + DocumentType 作為 Key，允許同專案不同文件類型並行上傳，同時防止同文件類型的版本競爭 |
| GOV-013A | 不開啟 | N/A | N/A | 純計算 Flow（單筆風險評分），無寫入衝突 |
| GOV-013B | 不開啟 | N/A | N/A | 純聚合 Flow（最高風險等級），無寫入衝突 |
| GOV-015 | 不開啟（允許平行） | N/A | N/A | 純通知 Flow，平行發送無衝突 |
| GOV-017 | 不開啟 | N/A | N/A | Scheduled，每小時一次 |
| GOV-018 | 不開啟 | N/A | N/A | Scheduled，每日一次 |
| GOV-019 | 不開啟 | N/A | N/A | Scheduled，每日一次 |

### 開啟 Concurrency Control 步驟

1. 開啟 Flow → 點擊 Trigger
2. 點擊 Trigger 右上角「...」→「設定」
3. 找到「並行控制」區段 → 開關切換為「開啟」
4. 「平行處理原則程度」設為 `1`
5. 點擊「完成」

---

## Counter List 併發策略（Concurrency Strategy）

### 架構模型：Optimistic Increment（樂觀遞增）

GOV-001 使用 Counter List 機制產生連續的 RequestID（如 DR-2026-0001）。
目前採用**樂觀遞增（Optimistic Increment）**模型：

```
┌─ GOV-001 Flow 啟動
├─ 1. List rows：讀取 Counter List（gov_countername = 'ProjectRequest'）
├─ 2. Compose：currentSeq = gov_nextseq
├─ 3. Update a row：gov_nextseq = currentSeq + 1
├─ 4. 使用 currentSeq 產生 RequestID
└─ 繼續建立專案
```

### 併發風險分析

| 情境 | 風險等級 | 說明 |
|:----------------------------------------------|:----------|:----------------------------------------------|
| 單使用者連續建立 | 無 | 序列化執行，無衝突 |
| 兩人同時建立（GOV-001 Concurrency = 1） | **無** | Power Automate Concurrency Control = 1 確保序列化 |
| 兩人同時建立（GOV-001 Concurrency 未開啟） | **中** | 可能讀取到同一 nextseq 值，導致重複 RequestID |
| 大量同時建立（>10 併發） | **高** | 即使開啟 Concurrency，排隊深度可能超出 Flow 逾時上限 |

### 防護措施（目前版本）

| # | 措施 | 說明 |
|:-----|:--------------------------|:----------------------------------------------|
| C-01 | **Concurrency Control = 1** | GOV-001 已設定 Parallelism = 1，確保同一時間只有一個 Flow Instance 讀寫 Counter |
| C-02 | **Guard Clause** | 步驟 3A.1b 驗證 Counter 記錄存在，不存在則 ERR-001-COUNTER |
| C-03 | **年份跨年重置** | 步驟 3A.3 判斷年份變化，自動重置序號為 1 |

### 已知限制與未來升級路徑

| 限制 | 影響 | 未來升級方案 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| 非 Transaction 等級隔離 | 極端情況下可能讀取髒值（Dirty Read） | 升級至 Dataverse Transaction API（ChangeSet Batch）或 Custom API with Pessimistic Lock |
| 無 Unique Constraint | RequestID 重複不會被 Dataverse 擋下 | 在 gov_requestid 欄位上建立 Alternate Key，由 Dataverse 強制唯一性 |
| 排隊深度無上限 | 大量併發時排隊時間可能超出 Flow 5 分鐘逾時 | 在 Power Apps 端加入「請勿重複點擊」提示 + varBusy 控制（已在 v4.3 PowerFx 範本實作） |

> **重要**：目前 Concurrency Control = 1 已足夠保護 Counter List 的一致性。
> 在日常使用場景（每日 < 50 筆專案建立）下，不需要額外的 Transaction 保護。
> 若系統擴展至每日 > 200 筆併發建立，則應優先實作 Alternate Key + Transaction API。

---

## OptionSet 值使用規則

**不可違反原則**：所有 OptionSet 值必須使用 Dataverse 定義的 `807660000` 系列數值。
Flow 中**禁止**使用任意整數（如 1, 2, 3）作為 Switch/Condition 的判斷值。
Flow 中**禁止**以 Switch/if 將文字硬轉為 OptionSet 數值（P-13 原則）。必須從 Dataverse `gov_optionsetmapping` 讀取映射。

> OptionSet 數值一旦發佈至 PROD，**不可更改**。若需修改，必須制定 Migration 計畫，
> 包含舊值→新值的資料轉換腳本與回滾方案。

---

## Flow Version Governance（版本治理）

### 版本管理原則

所有 Flow 的版本管理遵循以下治理規範：

| # | 規則 | 說明 |
|:-----|:--------------------------|:----------------------------------------------|
| V-01 | **Solution 版本控制** | 所有 Flow 必須在 Solution 內管理，版本號遵循 `Major.Minor.Build.Revision` 格式 |
| V-02 | **禁止 PROD 直接修改** | PROD 環境的 Flow 為 Managed Solution，禁止直接修改。所有變更必須在 DEV 完成後匯出 |
| V-03 | **變更記錄義務** | 每次 Flow 修改必須在 Review Decision Log 新增一筆 FlowVersionChange 記錄 |
| V-04 | **回滾計畫** | 每次 PROD 部署前必須準備上一版 Solution 的匯入包作為回滾方案 |
| V-05 | **FlowRunId 追溯** | 每次 Flow 執行的 Run ID 必須寫入 `gov_triggerflowrunid`，確保異常時可追溯至具體執行記錄 |

### Solution 版本號規則

| 版本變更 | 何時遞增 | 範例 |
|:----------------------|:----------------------------------------------|:-------------------------------|
| **Major** | 架構性變更（新增/移除 Flow、Trigger 類型變更） | 1.0 → 2.0 |
| **Minor** | 功能性變更（新增步驟、修改邏輯、新增回傳欄位） | 1.0 → 1.1 |
| **Build** | 修復性變更（Bug fix、錯誤訊息修正） | 1.0.0 → 1.0.1 |

### 部署流程

```
DEV（開發）→ 匯出 Unmanaged Solution
    ↓
QA（測試）→ 匯入 Managed Solution → 執行完整測試
    ↓
UAT（驗收）→ 匯入 Managed Solution → 業務驗收
    ↓
PROD（正式）→ 匯入 Managed Solution → Smoke Test → 啟用
```

### Drift Governance（漂移治理）

| 檢查項目 | 頻率 | 檢查方式 | 不一致處理 |
|:----------------------------------------------|:----------|:----------------------------------------------|:-------------------------------|
| Flow 數量一致性 | 每次部署後 | 比對 DEV vs PROD Solution 的 Flow 清單 | 重新匯出並匯入 |
| Flow 版本一致性 | 每週 | 比對 Solution 版本號 | 若 PROD 落後 DEV，排定部署 |
| Connection Reference 一致性 | 每次部署後 | 確認所有 CR- 已指派 PROD 連線 | 重新指派 |
| 未納管 Flow 偵測 | 每月 | GOV-017 掃描環境中非 Solution 內的 Flow | 納入 Solution 或刪除 |

---

## 施工模式制度（MVP / Hardened）

### MVP 模式 `[Development Allowed]`

| 項目 | MVP 模式規則 |
|:--------------------------|:--------------------------------------------------------------|
| **適用場景** | 功能驗證、PoC、首次跑通 |
| **Connection Reference** | 可使用個人帳號連線（不需 Service Principal） |
| **FLS** | 可暫時跳過 Field-Level Security 設定 |
| **上線許可** | **禁止上 PROD** |
| **Solution** | 仍須加入 Solution（便於後續切換） |

### Hardened 模式 `[Production Mandatory]`

| 項目 | Hardened 模式規則 |
|:--------------------------|:--------------------------------------------------------------|
| **適用場景** | UAT、PROD、正式上線 |
| **Connection Reference** | 必須使用 Service Principal Connection Reference（CR-xxx-SPN） |
| **FLS** | 必須完成所有 FLS 設定（Flow-only 欄位保護） |
| **上線許可** | 允許上線 |
| **Dataverse Audit** | 必須啟用 |

> **切換規則**：從 MVP 切換至 Hardened 時，必須逐條 Flow 將個人連線替換為 CR-xxx-SPN Connection Reference。

---

## 施工前檢查清單

進入 Power Automate 建立任何 Flow 之前，必須先選定施工模式，再依對應清單逐項確認。

### 施工模式選擇

> **完整施工模式規範請見前文「施工模式制度（MVP / Hardened）」章節。**
> 此處僅提供快速參照：MVP 模式標記 `[Development Allowed]`、Hardened 模式標記 `[Production Mandatory]`。
> 下方檢查清單中標記 `[Hardened]` 的項目，在 MVP 模式下可暫時跳過。

## Dataverse 環境

| 檢查項目 | 如何確認已具備 | 對應測試案例 |
|:----------------------------------------------|:----------------------------------------------|:-------------------------------|
| DEV 環境已建立 | Power Platform Admin Center → 環境 → 確認「dev-governance」存在且狀態為「就緒」 | 07文件 1.1 |
| Dataverse 資料庫已啟用 | 開啟 Maker Portal → 選擇 dev-governance 環境 → 左側選單出現「Dataverse」→「資料表」 | 07文件 1.1 |
| 所有治理資料表已建立 | Dataverse → 資料表 → 確認存在：Project Registry、Review Decision Log、Document Register、Risk Assessment Table、Governance Violation Log | 07文件 4.1.3 |
| `[Hardened]` Field-Level Security Profile 已建立 | 進階設定 → 安全性 → 欄位安全性設定檔 → 確認存在「Flow Service Principal Only」 | 07文件 AC-003 |
| `[Hardened]` 所有 Flow-only 欄位已設定 FLS | 開啟「Flow Service Principal Only」Profile → 確認下列欄位已加入（詳見 0.1.1） | 07文件 AC-003 |
| `[Hardened]` Dataverse Audit 已啟用 | 進階設定 → 稽核 → 確認「開始稽核」已啟用，且三個核心資料表皆啟用欄位層級稽核 | 07文件 AC-001 |

### Flow-only 欄位清單（必須設定 FLS）

**Project Registry（gov_projectregistry）**：
```
gov_currentgate
gov_requeststatus
gov_projectstatus
gov_documentfreezestatus
gov_gate0passeddate
gov_gate1passeddate
gov_gate2passeddate
gov_gate3passeddate
gov_riskacceptancestatus
gov_riskacceptancedate
gov_riskowner
gov_executiveapprover
gov_highestresidualrisklevel
gov_reworkcount
gov_lastreworkdate
gov_lastflowrunid
gov_lastflowstatus
gov_submittedby
gov_submittedat
gov_sharepointprovisionstatus
createdby
createdon
modifiedby
modifiedon
```

**Review Decision Log（gov_reviewdecisionlog）**：
```
gov_reviewid
gov_reviewtype
gov_decision
gov_approvedby
gov_revieweddate
gov_triggerflowrunid
gov_gate1securityreviewstatus
gov_gate1qareviewstatus
gov_gate1governancereviewstatus
gov_gate3qareviewstatus
gov_gate3governancereviewstatus
gov_riskownerreviewstatus
gov_executivereviewstatus
```

**Risk Assessment Table（gov_riskassessmenttable）**：
```
gov_risklevel
gov_residualrisklevel
gov_riskacceptancestatus
gov_riskacceptedby
gov_riskacceptancedate
```

## Service Principal `[Hardened]`

> **MVP 模式**：以下 Service Principal 項目可暫時跳過。MVP 模式下所有 Connector 使用您的個人帳號連線即可先行跑通。

| 檢查項目 | 如何確認已具備 |
|:--------------------------------------|:----------------------------------------------|
| `[Hardened]` Application Registration 已建立 | Azure Portal → Microsoft Entra ID → 應用程式註冊 → 確認存在「GOV-Flow-ServicePrincipal」 |
| `[Hardened]` Client Secret 已建立且未過期 | 應用程式註冊 → 憑證與密碼 → 確認有未過期的 Client Secret（記錄到期日：__________） |
| `[Hardened]` Application User 已建立 | Power Platform Admin Center → 環境 → dev-governance → 設定 → 使用者 + 權限 → 應用程式使用者 → 確認存在 |
| `[Hardened]` Application User 具備正確角色 | 應用程式使用者詳細資料 → 角色 → 確認具備「System Administrator」或自訂「Flow Executor」角色 |
| `[Hardened]` Application User 已加入 FLS Profile | 進階設定 → 安全性 → 欄位安全性設定檔 → Flow Service Principal Only → 使用者 → 確認已加入 |

## SharePoint

| 檢查項目 | 如何確認已具備 |
|:--------------------------------------|:----------------------------------------------|
| SharePoint Site 已建立 | 開啟 SharePoint → 確認「Design Governance」Site 存在 |
| Document Library 已建立 | Site 內容 → 確認存在「Design Documents」文件庫 |
| Service Principal 有 Site Collection Admin 權限 | Site 設定 → 網站集合管理員 → 確認 GOV-Flow-ServicePrincipal 已加入 |

## Security Groups（必須為 Mail-enabled Security Group）

| 群組名稱 | Object ID | 如何確認已具備 |
|:--------------------------|:----------------------|:----------------------------------------------|
| GOV-Architects | __________ | Entra ID → 群組 → 搜尋「GOV-Architects」→ 確認存在且已加入成員 |
| GOV-EngineeringManagement | __________ | 同上，且確認為 Mail-enabled |
| GOV-SecurityReviewers | __________ | 同上，且確認為 Mail-enabled |
| GOV-QAReviewers | __________ | 同上，且確認為 Mail-enabled |
| GOV-GovernanceLead | __________ | 同上，且確認為 Mail-enabled |
| GOV-ExecutiveManagement | __________ | 同上，且確認為 Mail-enabled |

## Solution

| 檢查項目 | 如何確認已具備 |
|:--------------------------------------|:----------------------------------------------|
| Solution 已建立 | Maker Portal → 解決方案 → 確認存在「DesignGovernanceSystem」（Unmanaged） |
| Publisher Prefix | 確認 Publisher Prefix 為「gov」或您組織的自訂前綴 |
| 所有 Dataverse 元件已加入 Solution | 開啟 Solution → 確認所有資料表、欄位、關聯性皆已加入 |

---

## 核心原則與禁止事項

## 絕對禁止事項

| 禁止行為 | 做了會造成的後果 | 對應 Guardrail |
|:----------------------------------------------|:----------------------------------------------|:-------------------------------|
| 在 PROD 環境直接新增或修改 Flow | 無法追蹤版本、無法回滾、破壞 Solution 一致性 | 無 |
| 把連線綁到個人帳號 | 該使用者離職後 Flow 全部失效、無法轉移維護權 | GOV-017 偵測 |
| 讓人類帳號直接修改 Flow-only 欄位 | 違反治理完整性、將被 GOV-017 偵測並自動回滾 | GOV-017 回滾 |
| 讓人類帳號直接寫入 SharePoint Gate 資料夾 | 繞過治理流程、無 Document Register 記錄、審計軌跡斷裂 | GOV-017 偵測孤兒檔案 |
| 在 Flow 中自動判定 Approve（無人類審批） | 違反「人類決策」原則、違規將被 GOV-018 偵測並通報 | GOV-018 不一致偵測 |
| 修改 Review Decision Log 既有記錄 | 違反 Append-only 原則、破壞審計軌跡、違規將被 GOV-017 偵測 | GOV-017 回滾 |
| 跳過 Pre-check 直接執行主邏輯 | 產生無效資料、狀態機混亂、無法追蹤錯誤來源 | GOV-018 不一致偵測 |
| 建立 Flow 但不加入 Solution | 無法匯出至其他環境、無法版本控制 | 無 |

## 必須遵守事項

| 必須遵守 | 原因 | 驗證方式 |
|:----------------------------------------------|:----------------------------------------------|:-------------------------------|
| 所有 Flow 必須加入 Solution | 才能匯出至 QA、UAT、PROD | 在 Solution 內確認 Flow 存在 |
| 所有 Flow 必須使用 Connection Reference `[Hardened]` | 跨環境部署時才能重新指派連線（MVP 模式可先用個人連線） | 開啟 Flow → 確認每個 Connector 使用 CR- 開頭的連線 |
| 所有 Flow 必須實作 Try-Catch Scope | 才能捕捉錯誤並記錄 | 開啟 Flow → 確認有 Catch Scope |
| 所有 Trigger Flow 必須驗證 SubmittedBy | 防止未授權存取 | 確認 Pre-check 存在 |
| 所有由 Power Apps 呼叫的 Flow 必須使用 Respond to a PowerApp or flow 回傳結果 | Power Apps 才能正確接收回傳值 | 確認 Respond Action 存在且包含 Status 欄位 |
| 所有狀態更新必須同時寫入 Review Decision Log | 才能保持完整審計軌跡 | 確認 Add row to RDL 存在 |
| Flow 名稱必須以 GOV-XXX 開頭 | 便於識別與管理 | 確認命名 |

---

## Connection Reference 保護機制

## Connection Reference 命名規則

> **MVP 模式**：MVP 模式下可先不建立 Connection Reference，直接在每個 Action 中選擇您的**個人帳號連線**。
> 後續切換至 Hardened 模式時，再建立下表所有 CR- 開頭的 Connection Reference 並逐條 Flow 替換。

| Connection Reference 名稱 | 連線類型 | 驗證方式 | MVP 模式替代 | Hardened DEV 綁定 | PROD 綁定 |
|:----------------------------------------------|:----------------------|:----------------------------------------------|:----------------------|:----------------------------------------------|:-------------------------------|
| CR-Dataverse-SPN | Microsoft Dataverse | Service Principal | 個人帳號連線 | GOV-Flow-ServicePrincipal (DEV) | GOV-Flow-ServicePrincipal (PROD) |
| CR-SharePoint-SPN | SharePoint | Service Principal | 個人帳號連線 | GOV-Flow-ServicePrincipal (DEV) | GOV-Flow-ServicePrincipal (PROD) |
| CR-Outlook-SPN | Office 365 Outlook | Service Principal | 個人帳號連線 | GOV-Flow-ServicePrincipal (DEV) | GOV-Flow-ServicePrincipal (PROD) |
| CR-Teams-SPN | Microsoft Teams | Service Principal | 個人帳號連線 | GOV-Flow-ServicePrincipal (DEV) | GOV-Flow-ServicePrincipal (PROD) |
| CR-Approvals | Approvals | 使用者帳號（可接受） | 個人帳號連線 | 共用服務帳號 | 共用服務帳號 |
| CR-Office365Groups | Office 365 Groups | Service Principal | 個人帳號連線 | GOV-Flow-ServicePrincipal (DEV) | GOV-Flow-ServicePrincipal (PROD) |

## 為何必須使用 Service Principal

| 使用個人帳號的風險 | Service Principal 如何解決 |
|:----------------------------------------------|:----------------------------------------------|
| 人員離職後連線失效 | Service Principal 不會離職，永久有效 |
| 密碼過期導致 Flow 失敗 | Client Secret 可設定較長期限並提前更新 |
| 無法追蹤是哪個 Flow 執行操作 | 所有操作皆由同一 Service Principal 執行，可透過 Flow Run ID 追蹤 |
| 權限過大或過小 | Service Principal 權限可精確控制 |

## 建立 Connection Reference 步驟（逐步點擊）

**步驟 1**：開啟 Maker Portal → 解決方案 → 開啟「DesignGovernanceSystem」

**步驟 2**：點擊左上角「+ 新增」→「更多」→「連接參考」

**步驟 3**：填寫以下欄位
```
顯示名稱：CR-Dataverse-SPN
描述：Dataverse 連線（Service Principal）
連接器：Microsoft Dataverse
```

**步驟 4**：在「連線」區段點擊「+ 新增連線」

**步驟 5**：選擇驗證類型「Service principal (client credentials)」

**步驟 6**：填寫以下資訊
```
租用戶識別碼：{您的 Azure AD Tenant ID}
用戶端識別碼：{GOV-Flow-ServicePrincipal 的 Application (client) ID}
用戶端密碼：{您的 Client Secret}
```

**步驟 7**：點擊「建立」

**步驟 8**：回到 Connection Reference 頁面，在「連線」下拉選單選擇剛建立的連線

**步驟 9**：點擊「儲存」

**驗證成功**：Connection Reference 清單中出現「CR-Dataverse-SPN」，狀態為「已連線」

## DEV 與 PROD 連線綁定差異

| 環境 | Connection Reference 行為 | 連線指向 |
|:----------|:----------------------------------------------|:----------------------------------------------|
| DEV | Unmanaged Solution，可直接修改 | DEV 環境的 Service Principal 連線 |
| PROD | Managed Solution，匯入時系統提示重新指派 | PROD 環境的 Service Principal 連線 |

**PROD 匯入時必做步驟**：
1. 匯入 Solution 時，系統會顯示「設定連接參考」畫面
2. 對每個 CR- 開頭的 Connection Reference，選擇或建立對應的 PROD 連線
3. 確認所有 Connection Reference 皆已指派
4. 點擊「匯入」

---

## 建置順序總覽

## Flow 建置順序表（依賴性強制順序）

必須依照以下順序建立 Flow，不可跳過或顛倒順序。

| 順序 | Phase | Flow ID | Flow 名稱 | Trigger 類型 | 依賴的 Flow | SLA/排程 |
|:-----|:----------|:--------|:----------------------------------------------|:----------------------|:----------------------------------------------|:-------------------------------|
| 1 | Phase 1 | GOV-015 | Notification Handler | Child Flow | 無 | N/A |
| 2 | Phase 1 | GOV-013A | Risk Score Calculator | Child Flow | 無 | N/A |
| 2a | Phase 1 | GOV-013B | Risk Aggregator | Child Flow | GOV-013A | N/A |
| 3 | Phase 2 | GOV-014 | Document Freeze | Child Flow | GOV-015 | N/A |
| 4 | Phase 2 | GOV-016 | Rework Loop Handler | Child Flow | GOV-015 | N/A |
| 5 | Phase 2 | GOV-004 | Risk Acceptance | Child Flow | GOV-015 | N/A |
| 6 | Phase 2 | GOV-003 | Gate Approval Orchestrator | Child Flow | GOV-015, GOV-016, GOV-014 | Gate 0/2 SLA 2天，Gate 1/3 SLA 3天 |
| 7 | Phase 3 | GOV-005 | Document Upload and Register | Power Apps (V2) | GOV-015 | N/A |
| 8 | Phase 3 | GOV-002 | Gate Transition Request | Power Apps (V2) | GOV-003, GOV-004, GOV-013B | N/A |
| 9 | Phase 3 | GOV-001 | Create Project | Power Apps (V2) | GOV-015 | N/A |
| 10 | Phase 4 | GOV-017 | Guardrail Monitor | Recurrence | 無 | 每小時執行 |
| 11 | Phase 4 | GOV-018 | Compliance Reconciler | Recurrence | 無 | 每日 00:00 UTC+8 |
| 12 | Phase 4 | GOV-019 | SLA Monitor | Recurrence | GOV-015 | 每日執行 |
| 13 | Phase 3 | GOV-020 | Document Inventory Parser | Power Apps (V2) | GOV-015 | N/A |
| 14 | Phase 3 | GOV-022 | Standard Feedback Handler | Power Apps (V2) | GOV-015 | N/A |
| 15 | Phase 3 | GOV-023 | Dispute Handler | Power Apps (V2) | GOV-015 | N/A |
| 16 | Phase 3 | GOV-024 | Action Item Tracker | Power Apps (V2) | GOV-015 | N/A |

## 各 Flow 依賴資源總表

| Flow ID | Connection References | Dataverse Tables | SharePoint | 對應測試案例 |
|:--------|:----------------------------------------------|:----------------------------------------------|:----------------------|:-------------------------------|
| GOV-001 | CR-Dataverse-SPN, CR-SharePoint-SPN, CR-Office365Groups | Project Registry, Review Decision Log, Document Register, Counter List | Design Documents | E2E-001 Phase 1 |
| GOV-002 | CR-Dataverse-SPN | Project Registry, Review Decision Log, Risk Assessment Table | 無 | E2E-001 Phase 2~6 |
| GOV-003 | CR-Dataverse-SPN, CR-Approvals | Project Registry, Review Decision Log | 無 | E2E-001 Phase 2~6 |
| GOV-004 | CR-Dataverse-SPN, CR-Approvals | Project Registry, Review Decision Log, Risk Assessment Table | 無 | E2E-001 Phase 5 |
| GOV-005 | CR-Dataverse-SPN, CR-SharePoint-SPN | Project Registry, Document Register, Review Decision Log | Design Documents | E2E-001 步驟 2.1 |
| GOV-013A | CR-Dataverse-SPN | Risk Assessment Table | 無 | E2E-001 Phase 5 |
| GOV-013B | CR-Dataverse-SPN | Risk Assessment Table | 無 | E2E-001 Phase 5 |
| GOV-014 | CR-Dataverse-SPN, CR-SharePoint-SPN | Project Registry, Document Register | Design Documents | E2E-001 Phase 6 |
| GOV-015 | CR-Outlook-SPN, CR-Teams-SPN | 無 | 無 | 全部通知測試 |
| GOV-016 | CR-Dataverse-SPN | Project Registry | 無 | E2E-002, E2E-004 |
| GOV-017 | CR-Dataverse-SPN | Project Registry, Review Decision Log, Governance Violation Log, Audit Log | 無 | AC-001, AC-002 |
| GOV-018 | CR-Dataverse-SPN | Project Registry, Review Decision Log | 無 | AC-004, AC-005 |
| GOV-019 | CR-Dataverse-SPN | Review Decision Log | 無 | AC-006 |
| GOV-020 | CR-Dataverse-SPN, CR-SharePoint-SPN, CR-Excel-SPN | Project Registry, Document Register | Design Documents | E2E-020 |
| GOV-022 | CR-Dataverse-SPN | Standard Feedback | 無 | E2E-022 |
| GOV-023 | CR-Dataverse-SPN | Dispute Log | 無 | E2E-023 |
| GOV-024 | CR-Dataverse-SPN | Action Item | 無 | E2E-024 |

---

## 共通建置規則

## Try-Catch Scope 標準結構

每個 Flow 的主邏輯必須包在 Scope 中，結構如下：

```
Flow 開始
    │
    ▼
┌─────────────────────────────────────────┐
│ Scope: Try-MainLogic                     │
│   ├── Pre-check Actions                  │
│   ├── Main Logic Actions                 │
│   └── Response Action (成功)             │
└─────────────────────────────────────────┘
    │
    │ Configure run after: Failed, TimedOut
    ▼
┌─────────────────────────────────────────┐
│ Scope: Catch-ErrorHandler                │
│   ├── Compose: ErrorMessage              │
│   ├── Compensating Transaction（若需要） │
│   └── Response Action (失敗)             │
└─────────────────────────────────────────┘
```

### 中文介面動作名稱速查

> **重要**：Power Automate 中文介面的動作名稱可能與英文不同，以下為常用動作的對照。
> 找不到動作時，請在搜尋列輸入 **英文關鍵字**（搜尋列始終支援英文搜尋）。

| 英文動作名稱 | 中文介面可能名稱 | 搜尋關鍵字 | 所在分類 | 找不到時替代路徑 |
|:----------------------------------------------|:----------------------------------------------|:----------------------|:----------------------------------------------|:----------------------------------------------|
| Compose | 撰寫、組成 | `compose` | 資料作業（Data Operations）/ Built-in | 搜尋 `data operations` → 展開分類 → 第一個就是 |
| Scope | 範圍 | `scope` | 控制項（Control）/ Built-in | 搜尋 `control` → 展開分類 → 找「範圍」 |
| Condition | 條件 | `condition` | 控制項（Control）/ Built-in | 搜尋 `control` → 展開 → 找「條件」 |
| Switch | 切換 | `switch` | 控制項（Control）/ Built-in | 搜尋 `control` → 展開 → 找「切換」 |
| Apply to each | 套用至每個項目 | `apply to each` | 控制項（Control）/ Built-in | 搜尋 `each` 也可找到 |
| Do until | 執行直到 | `do until` | 控制項（Control）/ Built-in | 搜尋 `until` → 選擇「控制項」下的結果 |
| Initialize variable | 初始化變數 | `initialize variable` | 變數（Variable）/ Built-in | 搜尋 `variable` → 展開分類 → 第一個 |
| Set variable | 設定變數 | `set variable` | 變數（Variable）/ Built-in | 搜尋 `variable` → 展開分類 → 第二個 |
| Filter array | 篩選陣列 | `filter array` | 資料作業（Data Operations）/ Built-in | 搜尋 `filter` |
| Add a new row | 新增資料列 | `add a new row` | Microsoft Dataverse / Connector | 搜尋 `dataverse` → 展開 Connector → 找「新增」 |
| Update a row | 更新資料列 | `update a row` | Microsoft Dataverse / Connector | 搜尋 `dataverse` → 展開 → 找「更新」 |
| Delete a row | 刪除資料列 | `delete a row` | Microsoft Dataverse / Connector | 搜尋 `dataverse` → 展開 → 找「刪除」 |
| List rows | 列出資料列 | `list rows` | Microsoft Dataverse / Connector | 搜尋 `dataverse` → 展開 → 找「列出」 |
| Get a row by ID | 依識別碼取得資料列 | `get a row` | Microsoft Dataverse / Connector | 搜尋 `dataverse` → 展開 → 找「取得」 |
| Create new folder | 建立新資料夾 | `create new folder` | SharePoint / Connector | 搜尋 `sharepoint` → 展開 → 找「建立新資料夾」 |
| Create file | 建立檔案 | `create file` | SharePoint / Connector | 搜尋 `sharepoint` → 展開 → 找「建立檔案」 |
| Get file content | 取得檔案內容 | `get file content` | SharePoint / Connector | 搜尋 `sharepoint` → 展開 → 找「取得檔案內容」 |
| Send an email (V2) | 傳送電子郵件 (V2) | `send an email` | Office 365 Outlook / Connector | 搜尋 `outlook` → 展開 → 選有 `(V2)` 的版本 |
| Start and wait for an approval | 啟動核准並等待 | `approval` | Approvals / Connector | 搜尋 `approval` → 選「啟動並等待核准」 |
| Respond to a PowerApp or flow | 回應 PowerApp 或流程 | `respond` | Power Apps / Built-in | 搜尋 `powerapps` → 找「回應」 |
| Run a Child Flow | 執行子流程 | `run a child flow` | 流程（Flows）/ Built-in | 搜尋 `child flow` 或 `子流程` |
| Terminate | 終止 | `terminate` | 控制項（Control）/ Built-in | 搜尋 `control` → 展開 → 找「終止」 |
| HTTP | HTTP | `http` | HTTP / Built-in | ⚠ **僅 Guardrail Flow 可使用**（P-09 原則） |
| Send an HTTP request | 傳送 HTTP 要求 | `send http` | SharePoint / Connector | ⚠ 此為 SharePoint HTTP Request，非通用 HTTP |

> **搜尋常見問題**：
> - 搜尋列預設只顯示前幾筆結果，若動作名稱較長（如 `Respond to a PowerApp or flow`），請使用**縮寫關鍵字**（如 `respond`）
> - 中文介面搜尋列**始終接受英文關鍵字**，遇到找不到的動作時，切換為英文搜尋最可靠
> - 若搜尋結果出現多個同名動作（如 SharePoint 和 OneDrive 都有 `Create file`），請確認選擇正確的 **Connector 分類**
> - 點擊「+ 新增步驟」（中文：「+ 新增步驟」）後，搜尋列才會出現

> **Compose 特別注意**：在中文介面下「Compose」可能顯示為「**撰寫**」或「**組成**」。
> 若在動作清單中找不到，請直接在搜尋列輸入 **`compose`** 英文關鍵字，它位於「**資料作業**」（Data Operations）分類下。

### 建立 Try-Catch Scope 步驟（逐步點擊）

**步驟 1**：在 Flow 設計器中，點擊「+ 新增步驟」

**步驟 2**：搜尋 `scope` → 選擇「**控制項**」分類下的「**Scope**」（中文可能顯示為「**範圍**」）

**步驟 3**：點擊 Scope 標題，重新命名為「Try-MainLogic」

**步驟 4**：將所有主要邏輯 Action 拖曳至此 Scope 內

**步驟 5**：在 Try-MainLogic 下方，再新增一個「Scope」，命名為「Catch-ErrorHandler」

**步驟 6**：點擊「Catch-ErrorHandler」右上角的「...」選單

**步驟 7**：選擇「設定在之後執行」（Configure run after）

**步驟 8**：取消勾選「成功」

**步驟 9**：勾選「已失敗」與「已逾時」

**步驟 10**：點擊「完成」

### ErrorMessage Compose 表達式

在 Catch-ErrorHandler 內新增 Compose Action（搜尋 `compose` → 選擇「**資料作業**」下的「**Compose**」，中文介面可能顯示為「**撰寫**」），使用以下表達式：

```
coalesce(
    result('Try-MainLogic')?[0]?['error']?['message'],
    '未知錯誤'
)
```

### Dataverse 使用者 Lookup 寫入標準步驟

> **用途**：當 Flow 需要將使用者 email 寫入 Dataverse 的 Lookup（使用者）欄位時（例如 GOV-001 寫入 SystemArchitect），
> 必須先查詢 `systemusers` 取得 systemuserid，再以 OData bind 格式寫入。
> **禁止直接將裸 GUID 填入 Lookup 欄位**，否則會出現 `ODataUnrecognizedPathException` 或 `The URI is not valid` 錯誤。

**步驟 1**：查詢 systemuser

```
Action：List rows (Dataverse)
    （搜尋 list rows → 選擇「Microsoft Dataverse」下的「List rows」，中文為「列出資料列」）
    連線：CR-Dataverse-SPN [MVP: 使用個人帳號連線]
    Table name：Users（systemusers）
    Filter rows：internalemailaddress eq '@{triggerBody()['SubmittedByEmail']}'
    Row count：1
    重新命名為「Get_SystemUser」
```

**步驟 2**：取出 systemuserid

```
Action：Compose
    重新命名為「Compose-SystemUserId」
    Inputs：@{first(outputs('Get_SystemUser')?['body/value'])?['systemuserid']}
```

**步驟 1b**：Guard Clause — 使用者不存在時立即終止

```
Action：Condition（檢查使用者是否存在）
    （搜尋 condition → 選擇「控制項」下的「Condition」，中文可能為「條件」）
    條件：length(outputs('Get_SystemUser')?['body/value']) is equal to 0

    True 分支（使用者不存在 → 終止）：
      Action：Respond to a PowerApp or flow
        StatusCode: 400, Status: Failed, ErrorCode: ERR-001-USER,
        ErrorStage: UserLookup,
        Message: 找不到使用者帳號，請確認 Email 正確,
        FlowRunId: @{workflow()?['run']?['name']}, Timestamp: @{utcNow()}
      Action：Terminate → Status: Failed

    False 分支（使用者存在 → 繼續步驟 2）
```

> **為什麼必須加 Guard Clause**：若略過此檢查，`first()` 會回傳 null，
> 後續 Lookup 寫入會出現 `recordId missing` 或 `The URI is not valid` 錯誤，
> 且錯誤訊息不會指向真正原因（email 查無使用者），大幅增加排查難度。

**步驟 3**：在 Add a new row / Update a row 中寫入 Lookup 欄位

```
在 Dataverse「Add a new row」或「Update a row」Action 中，
Lookup 欄位的正確寫入方式取決於介面模式：

【方式 A：Power Automate 設計器 UI 模式（推薦）】
    直接在 Lookup 欄位的下拉選單中選擇「輸入自訂值」，
    然後貼上以下格式的值：
    /systemusers(@{outputs('Compose-SystemUserId')})

【方式 B：Expression 模式】
    若使用 Peek code 或進階表達式：
    concat('/systemusers(', outputs('Compose-SystemUserId'), ')')
```

> **常見錯誤與解法**：
> | 錯誤訊息 | 原因 | 解法 |
> |:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
> | `ODataUnrecognizedPathException` | 直接填入 GUID 字串而非 `/systemusers({guid})` 格式 | 改用上述 `/systemusers(...)` 格式 |
> | `The URI is not valid` | GUID 格式錯誤或多了空白 | 確認 Compose 輸出為純 GUID（無大括號、無空白） |
> | `recordId missing` 或 `Parameter 'recordId' is required` | Lookup 欄位收到 null（通常因為 email 查無使用者而 first() 回傳 null） | 加入步驟 1b Guard Clause，在查無使用者時立即終止 |
> | `Resource not found` | email 查無對應使用者 | 確認 email 正確且該使用者存在於 Dataverse 環境中 |

**GOV-001 實際使用範例**（Step 6 建立 Project Registry 時寫入 SystemArchitect 欄位）：
```
欄位：gov_systemarchitect（Lookup → User）
值：/systemusers(@{outputs('Compose-SystemUserId')})
```

---

## Concurrency Control 設定

> **完整 Concurrency Policy 請見文件開頭「Flow Concurrency Policy」章節。**
> 以下僅列出需要開啟 Concurrency Control 的 Flow 與其 Key。

| Flow ID | 是否開啟 | Parallelism | Concurrency Key |
|:--------|:----------------------------------------------|:----------------------|:----------------------------------------------|
| GOV-001 | **Required（必須啟用）** | 1 | N/A |
| GOV-002 | **必須** | 1 | `triggerBody()['ProjectId']` |
| GOV-005 | **必須** | 1 | `concat(triggerBody()['ProjectId'], '-', triggerBody()['DocumentType'])` |

---

## Step 0：Power Apps ↔ Flow 連線必檢清單（建任何 Flow 前必讀）

> **為什麼需要 Step 0？** Power Apps 呼叫 Flow 時「沒反應」是最常見的卡關原因，且錯誤訊息通常不明確。
> 以下 6 項必須在建第一支 Flow 之前全部確認，否則後續施工會反覆卡關。

### 必檢 1：Flow 必須使用 Power Apps (V2) Trigger + 同 Solution

| 確認項目 | 如何確認 | 常見錯誤 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| Flow 使用 **Power Apps (V2)** Trigger | 開啟 Flow → 確認第一個 Trigger 顯示「Power Apps (V2)」 | 若使用舊版「Power Apps」Trigger（無 V2 標記），回傳功能會受限 |
| Flow 與 App 在**同一個 Solution** 內 | Maker Portal → 解決方案 → 開啟 Solution → 確認 Flow 和 App 都列在其中 | Flow 在 Solution 外建立 → Power Apps 看不到該 Flow |

> **注意**：在 Solution「外」建立 Flow 再事後移入 Solution，有時仍會無法被 App 辨識。建議**一律在 Solution 內直接建立 Flow**。

### 必檢 2：Power Apps 端必須加入 Flow + Refresh + 重新發布

建好 Flow 後，Power Apps 端**必須**執行以下 3 步驟才能呼叫 Flow：

```
步驟 A：在 Power Apps Studio 中，左側面板「Power Automate」→ 點擊「+ 新增流程」→ 選擇剛建好的 Flow
步驟 B：若列表沒出現 Flow，點擊右上角「⋯」→「重新整理」（Refresh）
步驟 C：加入 Flow 後，必須「發佈」（Publish）App，否則正式 App 仍然看不到新 Flow
```

> **常見陷阱**：只在 Studio 測試通過但忘記發佈 → 正式 App 用舊版本 → Flow 不會觸發。

### 必檢 3：連線必須已授權完成

| 確認項目 | 如何確認 | 常見錯誤 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| Flow 所有 Action 的連線皆為「已連線」狀態 | 開啟 Flow → 檢查每個 Action 右上角是否有 ⚠️ 標記 | 新建 Flow 後未授權 SharePoint 或 Dataverse 連線 → Flow 可開啟但 App 呼叫時靜默失敗 |
| 測試 Flow 時選擇的連線帳號與正式執行帳號一致 | MVP 模式使用個人帳號；Hardened 使用 Service Principal | 連線過期或帳號切換後未重新授權 |

> **驗證方式**：在 Flow 頁面點擊「測試」→「手動」→ 輸入測試參數 → 確認可以跑到最後一步。
> **但手動測試成功不代表 App 可呼叫**（見必檢 4）。

### 必檢 4：App 端 E2E 測試是唯一的通過標準

| 動作 | 目的 |
|:----------------------------------------------|:----------------------------------------------|
| 在 Power Apps Studio 中以「預覽」模式執行完整操作 | 驗證 App 能成功觸發 Flow 並取回結果 |
| 檢查 Flow Run History 確認有觸發記錄 | 排除「App 端根本沒送出」的可能 |
| 發布後在正式 App 中再測一次 | 排除「發布前後行為不一致」的可能 |

> **唯一合格標準**：正式發布的 App → 使用者點擊操作 → Flow Run History 出現成功記錄 → App 畫面顯示預期結果。

### 必檢 5：Flow 名稱與狀態

| 確認項目 | 說明 |
|:----------------------------------------------|:----------------------------------------------|
| Flow 名稱不含特殊字元 | 名稱中有 `/`、`\`、`#` 等特殊字元可能導致 Power Apps 無法識別 Flow |
| Flow 名稱改過後 App 端必須重新整理 | 若修改了 Flow 名稱（含加空格、改大小寫），Power Apps 中的舊名稱引用會失效 → 必須在 App 中移除舊 Flow → 重新加入 → 重新發佈 |
| Flow 狀態為 **On** | Flow 預設建立後可能為 Off，必須手動啟用 → Maker Portal → 開啟 Flow → 右上角「開啟」 |

### 必檢 6：確認使用正確環境

| 確認項目 | 如何確認 |
|:----------------------------------------------|:----------------------------------------------|
| Maker Portal 右上角顯示的環境名稱是 **DEV** 而非 PROD 或 Default | 點擊右上角「環境」下拉確認 |
| Power Apps Studio 的環境與 Flow 所在環境一致 | 若 App 在 DEV、Flow 在 PROD → App 永遠找不到 Flow |
| 瀏覽器沒有快取到舊環境的 Session | 若切換環境後仍然看到舊資料 → 清除瀏覽器快取或開無痕視窗 |

### 必檢 7：常見無觸發排查流程圖

```
Power Apps 呼叫 Flow 沒反應？
    │
    ├── 環境正確嗎？（App 和 Flow 在同一個環境）→ 不確定 → 必檢 6
    │
    ├── Flow Run History 有記錄？
    │     ├── 有 → Flow 有觸發但失敗 → 看錯誤訊息
    │     └── 沒有 → App 端根本沒送出
    │               ├── Flow 有加入 App？ → 沒有 → 必檢 2
    │               ├── Flow 在同一 Solution？ → 沒有 → 必檢 1
    │               ├── Flow 狀態是 On？ → 不是 → 必檢 5
    │               ├── Flow 名稱改過？ → 有 → 必檢 5（重新加入）
    │               └── 連線已授權？ → 沒有 → 必檢 3
    │
    └── App 有收到回傳？
          ├── 有 Status=Failed → 看 ErrorCode + Message
          └── 沒有回傳 → 檢查 Respond 動作是否在 Scope 內正確設定
```

---

## Power Apps 呼叫 Flow 標準範本（PowerFx）

> **用途**：Power Apps 端呼叫任何 Parent Flow（GOV-001、GOV-002、GOV-005）時，**必須**使用以下標準範本。
> 此範本包含：載入狀態控制、錯誤攔截、回傳狀態判斷、使用者訊息顯示。
> 不使用此範本 → 使用者在操作失敗時看不到任何錯誤訊息，無法排查問題。

### GOV-001 呼叫範本（專案建立 — FORM-001 提交按鈕 OnSelect）

```
// ===== GOV-001 Create Project 呼叫範本 =====
// 將以下代碼貼到提交按鈕的 OnSelect 屬性

// 1. 顯示載入中 + 防止重複點擊
UpdateContext({varBusy: true});
Notify("正在建立專案...", NotificationType.Information);

// 2. 呼叫 Flow + 錯誤攔截
IfError(
    Set(
        varFlowResult,
        GOV001CreateProject.Run(
            txtTitle.Text,                    // Title
            cmbArchitect.Selected.Email,      // SystemArchitectEmail
            cmbPM.Selected.Email,             // ProjectManagerEmail
            cmbSecurity.Selected.Email,       // SecurityReviewerEmail
            cmbQA.Selected.Email,             // QAReviewerEmail
            cmbProjectType.Selected.Value,    // ProjectType
            cmbTargetSL.Selected.Value,       // TargetSL
            txtDescription.Text,              // ProjectDescription
            User().Email                      // SubmittedByEmail
        )
    ),
    // Flow 觸發本身失敗（連線斷線、Flow 關閉等）
    Notify("Flow 觸發失敗，請檢查連線與 Flow 狀態", NotificationType.Error);
    UpdateContext({varBusy: false});
    // 此處 return 防止繼續執行
);

// 3. 關閉載入狀態
UpdateContext({varBusy: false});

// 4. 判斷回傳狀態
If(
    IsBlank(varFlowResult) || IsEmpty(varFlowResult),
    Notify("未收到 Flow 回傳，請檢查 Flow Run History", NotificationType.Error),

    varFlowResult.Status = "Success",
    Notify(
        "專案建立成功：" & varFlowResult.RequestID,
        NotificationType.Success
    );
    // 可選：導覽到專案詳情頁
    // Navigate(scrProjectDetail),

    // Status = Failed
    Notify(
        "建立失敗：" & varFlowResult.Message & " (" & varFlowResult.ErrorCode & ")",
        NotificationType.Error
    )
);
```

### GOV-002 呼叫範本（Gate 申請 — FORM-002 提交按鈕 OnSelect）

```
// ===== GOV-002 Gate Transition 呼叫範本 =====

UpdateContext({varBusy: true});
Notify("正在提交 Gate 申請...", NotificationType.Information);

IfError(
    Set(
        varFlowResult,
        GOV002GateTransition.Run(
            Text(varSelectedProject.gov_projectregistryid),  // ProjectId
            ddRequestedGate.Selected.Value,                   // RequestedGate
            User().Email,                                     // SubmittedByEmail
            txtComments.Text                                  // Comments
        )
    ),
    Notify("Flow 觸發失敗", NotificationType.Error);
    UpdateContext({varBusy: false});
);

UpdateContext({varBusy: false});

If(
    varFlowResult.Status = "Success",
    Notify("Gate 申請已提交", NotificationType.Success),
    Notify(varFlowResult.Message & " (" & varFlowResult.ErrorCode & ")", NotificationType.Error)
);
```

### GOV-005 呼叫範本（文件上傳 — FORM-003 上傳按鈕 OnSelect）

```
// ===== GOV-005 Document Upload 呼叫範本 =====

UpdateContext({varBusy: true});
Notify("正在上傳文件...", NotificationType.Information);

IfError(
    Set(
        varFlowResult,
        GOV005DocumentUpload.Run(
            Text(varSelectedProject.gov_projectregistryid),  // ProjectId
            attUpload.FileName,                               // FileName
            JSON(attUpload.Content, JSONFormat.IncludeBinaryData),  // FileContent (Base64)
            ddDocumentType.Selected.Value,                    // DocumentType
            txtDocName.Text,                                  // DocumentName
            varChangeType,                                    // ChangeType（"Major" 或 "Minor"）
            txtDocVersion.Text,                               // DocumentVersion
            ddPackage.Selected.Value,                         // DeliverablePackage
            txtDocComments.Text,                              // Comments
            User().Email                                      // SubmittedBy
        )
    ),
    Notify("Flow 觸發失敗", NotificationType.Error);
    UpdateContext({varBusy: false});
);

UpdateContext({varBusy: false});

If(
    varFlowResult.Status = "Success",
    Notify("文件上傳成功", NotificationType.Success),
    Notify(varFlowResult.Message & " (" & varFlowResult.ErrorCode & ")", NotificationType.Error)
);
```

### PowerFx 範本使用注意事項

| 項目 | 說明 |
|:--------------------------|:--------------------------------------------------------------|
| `varBusy` | 建議在提交按鈕的 `DisplayMode` 屬性設定 `If(varBusy, DisplayMode.Disabled, DisplayMode.Edit)`，防止使用者重複點擊 |
| `IfError` | 包裹整個 `.Run()` 呼叫，攔截 Flow 觸發本身的失敗（如連線過期、Flow 關閉） |
| `varFlowResult.Status` | **必須**檢查回傳的 Status 欄位，不可假設呼叫成功 |
| `varFlowResult.Message` | 失敗時**必須**顯示 Message 欄位，否則使用者無法知道錯誤原因 |
| `varFlowResult.FlowRunId` | 可選：顯示於畫面上方便使用者回報問題時提供 FlowRunId 給管理員查詢 |
| `JSON(..., JSONFormat.IncludeBinaryData)` | GOV-005 上傳檔案時，必須以此方式將附件轉為 Base64 字串 |

---

## 逐條 Flow 傻瓜施工步驟

## GOV-015：Notification Handler

### A. 基本資訊

| 項目 | 值 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 統一處理所有通知發送，包含 Email 與 Teams 訊息；被各 Parent Flow 以 Child Flow 方式呼叫 |
| Trigger 類型 | Manually trigger a flow（Child Flow）`[Governance Critical Control]` 必須勾選「Only other flows can trigger」 |
| 呼叫此 Flow 的來源 | GOV-001, GOV-002, GOV-003, GOV-004, GOV-005, GOV-016, GOV-017, GOV-018, GOV-019, GOV-022, GOV-023, GOV-024 |
| Connection References | CR-Outlook-SPN, CR-Teams-SPN |
| 對應測試案例 | 07文件 4.3.3 |

> **為何不加 Try-Catch Scope**：此 Flow 為純通知邏輯，不寫入 Dataverse，**通知失敗不影響主流程狀態**。若 Email 或 Teams 發送失敗，Parent Flow 的 Catch-ErrorHandler 會處理整體錯誤。**刻意不加 Try-Catch** 以維持結構簡潔；若需記錄通知失敗，可在 Parent Flow 的 Catch 路徑中判斷。

> **Try-Catch 例外核准說明**：GOV-015 為唯一免除 Try-Catch 的 Flow。
> 原因：通知失敗為非關鍵性失敗，不應透過例外傳播中斷呼叫它的 Parent Flow。
> Go-live 驗收時，此項目須由 Governance Lead 手動核准豁免，並記錄在 Review Decision Log 中。

---

### B. Step 0：建構前必確認事項（必讀）

| # | 確認項目 | 確認方式 | 不符處置 |
|:-----|:--------------------------|:----------------------------------------------|:-------------------------------|
| B1 | GOV-015 已在 Solution 內建立 | Maker Portal → 解決方案 → 確認清單 | 先在 Solution 內新建 Flow |
| B2 | Trigger 為「Manually trigger a flow」且已勾選「Only other flows can trigger」 | 開啟 Flow → Trigger 卡片 → Advanced options | 未勾選則所有 Parent Flow 的 Run a Child Flow 找不到此 Flow |
| B3 | CR-Outlook-SPN Connection Reference 已建立並授權 | Solution → Connection References → CR-Outlook-SPN → 確認無 ⚠️ | 點擊 Connection Reference → 重新指派連線；Service Principal 需有 Mail.Send 權限 |
| B4 | CR-Teams-SPN Connection Reference 已建立並授權 | Solution → Connection References → CR-Teams-SPN → 確認無 ⚠️ | 同上；Service Principal 需有 Teams Channel 的 Post 權限 |
| B5 | 已確認 Teams Channel 名稱（治理通知 Channel）與 Team 名稱 | Teams 客戶端 → 確認 Channel 存在 | Flow 步驟 5 的 Channel 設定將引用此名稱 |

---

### C. NotificationType 有效值清單

所有 Parent Flow 呼叫 GOV-015 時，**NotificationType 必須使用以下值之一**（大小寫敏感）：

| NotificationType 值 | 觸發來源 | 語意 |
|:----------------------------------------------|:----------------------------------------------|:-------------------------------|
| `ProjectCreated` | GOV-001 | 新專案建立通知 |
| `GateApproved` | GOV-003 | Gate 審批通過通知 |
| `GateRejected` | GOV-003 | Gate 審批拒絕通知 |
| `ReworkRequired` | GOV-016 | 退回重工通知 |
| `RiskAccepted` | GOV-004 | 風險接受通知 |
| `RiskRejected` | GOV-004 | 風險拒絕通知 |
| `DocumentUploaded` | GOV-005 | 文件上傳通知 |
| `ComplianceAlert` | GOV-017, GOV-018 | 合規違規偵測通知 |
| `SLAViolation` | GOV-019 | SLA 超時通知 |
| `StandardFeedbackReceived` | GOV-022 | 標準回饋已提交通知 |
| `DisputeSubmitted` | GOV-023 | 爭議已提報通知 |
| `ActionItemAssigned` | GOV-024 | 行動項目已指派通知 |
| `SystemError` | 各 Flow Catch 路徑 | 系統錯誤通知 |

> **本 Flow 不依據 NotificationType 做分支邏輯**：所有類型都走相同的 Email + Teams 發送路徑。NotificationType 僅寫入 Email Body 供收件人識別。

---

### D. Input Schema

| 參數名稱 | 資料類型 | 必填 | 說明 |
|:--------------------------|:----------------------|:------:|:----------------------------------------------|
| NotificationType | Text | 是 | 見 C 節有效值清單 |
| RecipientEmail | Text | 是 | 收件者 Email（支援多收件人以分號分隔） |
| Subject | Text | 是 | Email 主旨（建議含 `【】` 標記方便識別） |
| Body | Text | 是 | Email 內文（純文字或 HTML） |
| ProjectId | Text | 否 | 專案編號（用於通知 Footer；不填則顯示空白） |
| ReminderType | Text | 否 | 提醒類型（對應 gov_remindertype OptionSet Value），選填；傳入時觸發 Process Log 寫入 |
| CallingFlowName | Text | 否 | 呼叫方 Flow 名稱（如 GOV-022），選填；寫入 gov_triggeredbyflow 供追溯 |

---

### E. 建立步驟（逐步點擊）

**Step 1：在 Solution 內建立新 Flow**

1. Maker Portal → 解決方案 → DesignGovernanceSystem → + 新增 → 自動化 → Cloud flow → 立即

**Step 2：設定 Trigger**

1. 搜尋 `manually` → 選擇「Manually trigger a flow（手動觸發 Flow）」
2. 點擊「+ Add an input」，依序加入 5 個輸入：
   - 選擇「**Text**」→ 名稱填入 `NotificationType`
   - 選擇「**Text**」→ 名稱填入 `RecipientEmail`
   - 選擇「**Text**」→ 名稱填入 `Subject`
   - 選擇「**Text**」→ 名稱填入 `Body`
   - 選擇「**Text**」→ 名稱填入 `ProjectId` → 點擊「Show advanced options（顯示進階選項）」→ 取消勾選「Required（必要）」
   - 選擇「**Text**」→ 名稱填入 `ReminderType` → 取消勾選「Required（必要）」
   - 選擇「**Text**」→ 名稱填入 `CallingFlowName` → 取消勾選「Required（必要）」
3. 點擊 Trigger 右上角 `...` → 「Settings」→ 啟用「**Only other flows can trigger**」

**Step 3：新增 Compose（組合完整 Email 內文）**

1. 點擊「+ New step（+ 新增步驟）」
2. 搜尋 `compose` → 選擇「資料作業（Data Operation）」下的「Compose（撰寫）」
3. 命名：`Compose-FullEmailBody`
4. Inputs 填入：
   ```
   @{triggerBody()?['Body']}

   ───────────────────────────────────
   通知類型：@{triggerBody()?['NotificationType']}
   專案編號：@{triggerBody()?['ProjectId']}
   發送時間：@{formatDateTime(utcNow(), 'yyyy-MM-dd HH:mm:ss')} UTC
   此通知由設計治理系統自動發送，請勿回覆。
   ```

**Step 4：新增 Send an email (V2)**

1. 點擊「+ New step」
2. 搜尋 `send an email` → 選擇「**Office 365 Outlook**」下的「Send an email (V2)（傳送電子郵件 (V2)）」
3. 連線選擇：`CR-Outlook-SPN`
4. 欄位設定：
   - To：選擇動態內容 → `RecipientEmail`
   - Subject：選擇動態內容 → `Subject`
   - Body：選擇動態內容 → `Compose-FullEmailBody` 的「輸出」

**Step 5：新增 Post message in a chat or channel**

1. 點擊「+ New step」
2. 搜尋 `post message` → 選擇「**Microsoft Teams**」下的「Post message in a chat or channel（在聊天或頻道中張貼訊息）」
3. 連線選擇：`CR-Teams-SPN`
4. 欄位設定：
   - Post as: `Flow bot`
   - Post in: `Channel`
   - Team: 選擇治理團隊（例：`Design Governance`）
   - Channel: 選擇通知 Channel（例：`治理通知`）
   - Message:
     ```
     **@{triggerBody()?['Subject']}**

     @{outputs('Compose-FullEmailBody')}
     ```

**Step 5.5：Write Process Log（流程提醒日誌寫入）**

> **說明**：此步驟將通知發送結果寫入 `gov_processlog`，支援 COORD-K4 KPI 計算。僅當呼叫方傳入 ReminderType 時才寫入日誌。

1. 點擊「+ New step」
2. 搜尋 `condition` → 選擇「控制項」下的「Condition」
3. 重新命名為「Is_ProcessLogEnabled」
4. 條件設定：
   - 左側：運算式 → `not(empty(triggerBody()?['ReminderType']))`
   - 運算子：is equal to
   - 右側：`true`
   - 說明：僅當呼叫方傳入 ReminderType 時才寫入日誌

**If Yes（ReminderType 有值 → 寫入 Process Log）**：

```
a. List rows (Dataverse)
   Table name：Counter List
   Filter rows：gov_countername eq 'ProcessLogID'
   Row count：1
   重新命名為「Get_ProcessLogCounter」

b. Compose
   重新命名為「Compose-NewProcessLogCounter」
   Inputs：運算式 → add(first(outputs('Get_ProcessLogCounter')?['body/value'])?['gov_currentcounter'], 1)

c. Compose
   重新命名為「Compose-ProcessLogID」
   Inputs：運算式 →
   concat(first(outputs('Get_ProcessLogCounter')?['body/value'])?['gov_prefix'], '-', string(first(outputs('Get_ProcessLogCounter')?['body/value'])?['gov_currentyear']), '-', substring(concat('0000', string(outputs('Compose-NewProcessLogCounter'))), sub(length(concat('0000', string(outputs('Compose-NewProcessLogCounter')))), 4), 4))

d. Update a row (Dataverse)
   Table name：Counter List
   Row ID：first(outputs('Get_ProcessLogCounter')?['body/value'])?['gov_counterlistid']
   gov_currentcounter：outputs('Compose-NewProcessLogCounter')
   重新命名為「Update_ProcessLogCounter」

e. Add a new row (Dataverse)
   Table name：Process Log
   重新命名為「Create_ProcessLog」
   欄位對應：
     gov_processlogid：@{outputs('Compose-ProcessLogID')}
     gov_remindertype：@{int(triggerBody()?['ReminderType'])}
     gov_scheduledtime：@{utcNow()}
     gov_actualsenttime：@{utcNow()}
     gov_recipient：@{triggerBody()?['RecipientEmail']}
     gov_processlogstatus：807660000（Sent）
     gov_parentproject：@{if(empty(triggerBody()?['ProjectId']), null, triggerBody()?['ProjectId'])}
     gov_triggeredbyflow：@{triggerBody()?['CallingFlowName']}
```

**If No（ReminderType 為空 → 跳過）**：不做任何事

---

**Step 6：新增 Respond to a PowerApp or flow**

1. 點擊「+ New step」
2. 搜尋 `respond` → 選擇「Respond to a PowerApp or flow（回應 PowerApp 或流程）」
3. 點擊「+ Add an output」→ 選擇「**Text**」→ 名稱填入 `Status` → 值填入 `Success`

**Step 7：儲存 Flow**

1. 點擊左上角 Flow 名稱 → 輸入：`GOV-015-NotificationHandler`
2. 點擊「Save（儲存）」

---

### F. 最小驗證流程（建構完成後立即執行）

**如何手動觸發 GOV-015（不依賴 Parent Flow）：**
1. Power Automate → My flows → `GOV-015-NotificationHandler`
2. 「Test（測試）」→「Manually（手動）」→「Test flow」
3. 填入以下測試參數 → 點擊「Run flow」

**測試參數範例：**
```
NotificationType: ProjectCreated
RecipientEmail:   [你自己的 Email]
Subject:          【測試】GOV-015 Notification Handler 驗證
Body:             這是一封 GOV-015 的手動測試通知，用於確認 Email 與 Teams 通知正常運作。
ProjectId:        TEST-001
```

**在 Run History 確認（Power Automate → My flows → GOV-015 → 28 day run history）：**
1. 找到剛才的執行記錄 → 確認整條 Flow 綠色
2. 展開 `Compose-FullEmailBody` → 確認 Outputs 包含 Body、通知類型、專案編號、時間戳記
3. 展開 `Send an email (V2)` → 確認 Status 為 `succeeded`（並確認信件已到收件匣）
4. 展開 `Post message in a chat or channel` → 確認 Status 為 `succeeded`（並確認 Teams Channel 出現訊息）
5. 展開 `Respond to a PowerApp or flow` → 確認 `Status` = `Success`

**驗收對照表（對應 07文件 4.3.3）：**

| 驗收項目 | Run History 位置 | 預期結果 |
|:----------------------------------------------|:----------------------------------------------|:-------------------------------|
| Flow 執行成功 | 執行記錄狀態 | 整條 Flow 綠色打勾 |
| Email 已送出 | 展開 `Send an email (V2)` → 看 Status | `succeeded`；信箱收到信件 |
| Teams 訊息已發送 | 展開 `Post message in a chat or channel` → 看 Status | `succeeded`；Teams Channel 出現訊息 |
| Respond 回傳正確 | 展開 `Respond to a PowerApp or flow` → 看 Outputs | `Status = Success` |

---

### G. 常見失敗原因（可觀測訊號 + Run History 定位）

| # | 可觀測訊號 | 根本原因 | Run History 定位方式 | 修正方法 |
|:-----|:-------------------|:--------------------------|:----------------------------------------------|:-------------------------------|
| G1 | `Send an email (V2)` 失敗：`Unauthorized` | CR-Outlook-SPN 連線過期或 Service Principal 無 Mail.Send 權限 | Run History → 展開 `Send an email (V2)` → 看 Error message | 重新授權 CR-Outlook-SPN；在 Azure AD → App Registrations → 確認 Mail.Send 權限已授予 |
| G2 | `Send an email (V2)` 失敗：`Invalid recipient` | RecipientEmail 格式錯誤或為空 | Run History → 展開 Trigger → 看 Inputs 的 RecipientEmail 值 | 確認 Parent Flow 傳入有效的 Email 格式（支援分號分隔多收件人） |
| G3 | `Post message in a chat or channel` 失敗：`Bot not found` | CR-Teams-SPN 未授權，或 Team/Channel 名稱錯誤 | Run History → 展開 `Post message in a chat or channel` → 看 Error message | 確認 CR-Teams-SPN 連線有效；確認 Step 5 的 Team 與 Channel 下拉選到正確值（建立時就已綁定，非動態內容） |
| G4 | Email 送達但內文為空 | Parent Flow 傳入的 Body 為空字串或 null | Run History → 展開 Trigger → 看 Inputs 的 Body 值 | 確認 Parent Flow 的 Body 組合邏輯；在 Parent Flow 中加 Compose 先確認 Body 非空再呼叫 015 |
| G5 | Parent Flow 的 `Run a Child Flow` 找不到 GOV-015 | Trigger 未勾選「Only other flows can trigger」，或 Flow 不在同一 Solution | Parent Flow 編輯模式 → Run a Child Flow → Flow 下拉清單無 GOV-015 | 開啟 GOV-015 → Trigger Settings → 勾選 Only other flows；確認 GOV-015 在同一 Solution |
| G6 | Flow 成功但沒有收到 Email（Run History 顯示 succeeded） | Email 被過濾到垃圾郵件或封鎖清單 | Run History → Send an email (V2) → 確認 Status = succeeded | 在 Email 客戶端檢查垃圾郵件；確認 Service Principal 的寄件人地址未被封鎖 |
| G7 | Teams 訊息格式亂（Markdown 未渲染） | Message 欄位使用純文字模式而非 Adaptive Card 或 HTML | Run History → 展開 `Post message in a chat or channel` → 看 Message Inputs | Teams Channel Message 不渲染所有 Markdown；改用 HTML 格式或 Adaptive Card |
| G8 | Parent Flow 收到 015 結果但 `Status` 不是 `Success` | Respond Action 設定錯誤（欄位名稱拼錯）| Run History → 展開 Respond → 看 Outputs 的 Status 值 | 確認 Respond 的欄位名稱為 `Status`（大小寫敏感），值為 `Success` |

## GOV-013A：Risk Score Calculator

### A. 基本資訊

| 項目 | 值 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 接收單筆風險項目的 Likelihood 與 Impact，計算該筆的 RiskScore（0~16）並判定 RiskLevel（Low / Medium / High） |
| Trigger 類型 | Manually trigger a flow（Child Flow）`[Governance Critical Control]` 必須勾選「Only other flows can trigger」 |
| 呼叫此 Flow 的來源 | GOV-013B（由 Apply to each 逐筆呼叫） |
| Connection References | **無**（純計算 Flow，不存取任何 Connector） |
| 對應測試案例 | 07文件 E2E-001 Phase 5 |

> **為何不加 Try-Catch Scope**：此 Flow 無外部 Connector，不會產生連線逾時或系統例外。所有錯誤路徑（輸入範圍驗證）均已用 Condition + Respond 明確處理，**刻意不加 Try-Catch** 以維持結構簡潔。

---

### B. Step 0：建構前必確認事項（必讀）

| # | 確認項目 | 確認方式 | 不符處置 |
|:-----|:--------------------------|:----------------------------------------------|:-------------------------------|
| B1 | GOV-013A 已在 Solution 內建立 | Maker Portal → 解決方案 → 確認清單 | 先在 Solution 內新建 Flow |
| B2 | Trigger 為「Manually trigger a flow」且已勾選「Only other flows can trigger」 | 開啟 Flow → Trigger 卡片 → Advanced options | 未勾選則 GOV-013B 的 Run a Child Flow 找不到此 Flow |
| B3 | 所有 `Respond to a PowerApp or flow` 的輸出欄位集合**必須完全一致** | — | 成功 Respond 與失敗 Respond 必須有相同的 5 個欄位（RiskScore 填 0、ErrorMessage 填空字串） |
| B4 | `Set variable` 之前**必須先** `Initialize variable`，且 Initialize variable 只能放在 Flow 最頂層 | — | 未先 Initialize → 儲存時報「Variable not found」 |
| B5 | Likelihood / Impact 是 Dataverse OptionSet 欄位，值為 807660000 系列（不是 1~5） | 對照本節 C 表 | 誤用 1~5 則 RiskScore 計算結果錯誤 |

---

### C. Input / Output Schema 與 OptionSet 數值對照表

**Input Schema：**

| 參數名稱 | 資料類型 | 必填 | 說明 |
|:--------------------------|:----------------------|:------:|:----------------------------------------------|
| Likelihood | Number | 是 | OptionSet 值（807660000~807660004） |
| Impact | Number | 是 | OptionSet 值（807660000~807660004） |

**Likelihood / Impact 值對照：**

| OptionSet 值 | 正規化值（計算用）| 語意 |
|:----------|:--------------------------------------|:------|
| 807660000 | 0 | Very Low / Negligible |
| 807660001 | 1 | Low / Minor |
| 807660002 | 2 | Medium / Moderate |
| 807660003 | 3 | High / Major |
| 807660004 | 4 | Very High / Critical |

**RiskScore 計算公式：**
```
RiskScore = (Likelihood − 807660000) × (Impact − 807660000)
範圍：0（最低 0×0）~ 16（最高 4×4）
```

**RiskLevel 判定閾值與 Output Schema：**

| 條件 | RiskLevel 值 | RiskLevelLabel | 輸出欄位 |
|:----------------------------------------------|:----------|:----------------------------------------------|:----------------------------------------------|
| RiskScore ≥ 8 | 807660002 | `High` | Status / RiskScore / RiskLevel / RiskLevelLabel / ErrorMessage |
| RiskScore ≥ 3（且 < 8） | 807660001 | `Medium` | 同上 |
| RiskScore < 3 | 807660000 | `Low` | 同上 |
| 輸入驗證失敗 | 807660000 | `Invalid` | Status=Failed / RiskScore=0 / RiskLevel=807660000 / RiskLevelLabel=Invalid / ErrorMessage=說明 |

---

### D. 建立步驟（逐步點擊）

**Step 1：建立 Trigger**

1. Maker Portal → 解決方案 → DesignGovernanceSystem → + 新增 → 自動化 → Cloud flow → 立即
2. 搜尋 `manually` → 選擇「Manually trigger a flow（手動觸發 Flow）」
3. 點擊「+ Add an input」：
   - 選擇「**Number**」→ 名稱填入 `Likelihood`
   - 點擊「+ Add an input」→ 選擇「**Number**」→ 名稱填入 `Impact`
4. 點擊 Trigger 右上角 `...` → 「Settings（設定）」→ 啟用「**Only other flows can trigger**」

**Step 2：Initialize variable — RiskLevel**

1. 點擊「+ New step（+ 新增步驟）」
2. 搜尋 `initialize variable` → 選擇「Variable（變數）」下的「Initialize variable（初始化變數）」
3. 設定：Name = `RiskLevel`、Type = `Integer`、Value = `807660000`
4. 命名此 Action：`Init-RiskLevel`

**Step 3：Initialize variable — RiskLevelLabel**

1. 點擊「+ New step」→ 搜尋 `initialize variable` → 選擇「Initialize variable」
2. 設定：Name = `RiskLevelLabel`、Type = `String`、Value = `Low`
3. 命名此 Action：`Init-RiskLevelLabel`

> **重要**：Steps 2 和 3 必須在 Flow **最頂層**（Trigger 正下方），不可放在任何 Scope 或 Condition 內。

**Step 4：Input 範圍驗證**

1. 點擊「+ New step」→ 搜尋 `condition` → 選擇「控制項（Control）」下的「Condition（條件）」
2. 命名：`Condition-ValidateInput`
3. 加入 4 個條件（全部 AND）— 每個條件的 Left value 點擊「fx」切換 Expression 模式輸入：

   | Left value（Expression） | 運算子 | Right value |
   |:----------------------------------------------|:----------------------|:-------------------------------|
   | `triggerBody()?['Likelihood']` | is greater than or equal to | `807660000` |
   | `triggerBody()?['Likelihood']` | is less than or equal to | `807660004` |
   | `triggerBody()?['Impact']` | is greater than or equal to | `807660000` |
   | `triggerBody()?['Impact']` | is less than or equal to | `807660004` |

4. **False 分支（輸入無效）**：
   - 加入「Respond to a PowerApp or flow（回應 PowerApp 或流程）」→ 命名：`Respond-ValidationFailed`
   - 加入 5 個輸出欄位（**順序與 Step 7 的 Respond-Success 完全一致**）：

     | 類型 | 欄位名稱 | 值 |
     |:----------|:----------------------------------------------|:----------------------------------------------|
     | Text | `Status` | `Failed` |
     | Number | `RiskScore` | `0` |
     | Number | `RiskLevel` | `807660000` |
     | Text | `RiskLevelLabel` | `Invalid` |
     | Text | `ErrorMessage` | `Likelihood 或 Impact 值超出有效範圍（807660000~807660004）` |

   - 在 Respond-ValidationFailed 下方加入「Terminate（終止）」→ Status: `Cancelled`

**Step 5：計算 RiskScore（在 Condition-ValidateInput 之後，主流程中）**

✅ [已修正 BUG-024] 風險評分公式安全性確認（原審計報告誤判為 division by zero）

1. 點擊「+ New step」→ 搜尋 `compose` → 選擇「資料作業（Data Operation）」下的「Compose（撰寫）」
2. 命名：`Compose-RiskScore`
3. Inputs（切換 Expression 模式）：
   ```
   mul(
     sub(triggerBody()?['Likelihood'], 807660000),
     sub(triggerBody()?['Impact'], 807660000)
   )
   ```
   > 例：Likelihood=`807660003`（High=3）× Impact=`807660004`（Critical=4）= **12 → High**

> **[BUG-024] 公式安全性說明**：
>
> 此公式使用 **`mul()`（乘法）**，不使用 `div()`（除法），**不存在除以零的風險**。
> 原審計報告 BUG-024 誤將此標記為「division by zero」，實際情況如下：
>
> | 輸入情境 | Likelihood | Impact | sub 後值 | RiskScore | 分類 |
> |:----------------------------------------------|:----------|:----------|:----------------------------------------------|:----------|:-------------------------------|
> | 最低風險 | 807660000 | 807660000 | 0 × 0 | 0 | Low（有效） |
> | 中等風險 | 807660002 | 807660002 | 2 × 2 | 4 | Medium（有效） |
> | 最高風險 | 807660004 | 807660004 | 4 × 4 | 16 | High（有效） |
>
> - **RiskScore = 0（兩者均為 Low）是有效結果**，代表最低風險等級，Step 6 正確分類為 Low。
> - **Step 4 的 `Condition-ValidateInput`** 已確保輸入在 `[807660000, 807660004]` 範圍內，
>   防止負值（`sub` 結果 < 0）導致意外分類。
> - 若未來修改公式加入 `div()` 正規化（如除以 16 換算 0~1.0），
>   則需加入 `Condition-ValidRiskScores` 防止分母為 0。目前公式 **無需此額外守衛**。

**Step 6：判定 RiskLevel（High ≥ 8）**

1. 點擊「+ New step」→ 搜尋 `condition` → 命名：`Condition-IsHigh`
2. 設定：Left value（Expression）= `outputs('Compose-RiskScore')`，Operator = `is greater than or equal to`，Right value = `8`
3. **True 分支（High）**：
   - 加入「Set variable（設定變數）」→ Name: `RiskLevel`，Value: `807660002`
   - 再加「Set variable」→ Name: `RiskLevelLabel`，Value: `High`
4. **False 分支（判定 Medium）**：
   - 加入「Condition（條件）」→ 命名：`Condition-IsMedium`
   - 設定：Left = `outputs('Compose-RiskScore')`，Operator = `is greater than or equal to`，Right = `3`
   - **True 分支（Medium）**：Set variable → `RiskLevel` = `807660001`；Set variable → `RiskLevelLabel` = `Medium`
   - **False 分支（Low）**：**不加任何 Action**（初始值 807660000 / Low 即為正確）

**Step 7：回傳成功結果**

1. 在所有 Condition 之後（Flow 最末端），加入「Respond to a PowerApp or flow（回應 PowerApp 或流程）」
2. 命名：`Respond-Success`
3. 加入 5 個輸出欄位（**與 Respond-ValidationFailed 的欄位名稱、順序完全一致**）：

   | 類型 | 欄位名稱 | 值 |
   |:----------|:----------------------------------------------|:----------------------------------------------|
   | Text | `Status` | `Success` |
   | Number | `RiskScore` | 動態內容 → `Compose-RiskScore` 的「輸出」 |
   | Number | `RiskLevel` | 動態內容 → Variables 的 `RiskLevel` |
   | Text | `RiskLevelLabel` | 動態內容 → Variables 的 `RiskLevelLabel` |
   | Text | `ErrorMessage` | （空字串，佔位用） |

**Step 8：儲存**

1. 點擊左上角 Flow 名稱 → 輸入：`GOV-013A-RiskScoreCalculator`
2. 點擊「Save（儲存）」→ 等待成功

---

### E. 最小驗證流程（建構完成後立即執行）

**如何手動觸發 013A（不依賴 GOV-013B）：**
1. Power Automate → My flows → `GOV-013A-RiskScoreCalculator`
2. 點擊「Test（測試）」→「Manually（手動）」→「Test flow」
3. 填入 Likelihood 與 Impact 值 → 點擊「Run flow」

**5 個必做測試案例：**

| # | Likelihood | Impact | 預期 RiskScore | 預期 RiskLevel | 預期 RiskLevelLabel |
|:-----|:----------|:----------|:-------------------------------|:-------------------------------|:-------------------------------|
| T1 | `807660004` | `807660004` | 16 | 807660002 | High |
| T2 | `807660003` | `807660003` | 9 | 807660002 | High（邊界 ≥8） |
| T3 | `807660002` | `807660002` | 4 | 807660001 | Medium（邊界 ≥3） |
| T4 | `807660001` | `807660001` | 1 | 807660000 | Low |
| T5 | `807660000` | `807660000` | 0 | 807660000 | Low |

**失敗路徑驗證：**

| # | Likelihood | Impact | 預期 Status | 預期 ErrorMessage |
|:-----|:----------|:----------|:-------------------------------|:----------------------------------------------|
| T6 | `99999999` | `807660000` | Failed | 含「超出有效範圍」 |
| T7 | `807660000` | `807660005` | Failed | 含「超出有效範圍」 |

**在 Run History 確認（Power Automate → My flows → GOV-013A → 28 day run history）：**
1. 點入執行記錄 → 確認整條 Flow 綠色
2. 展開 `Compose-RiskScore` → Outputs 確認數值符合預期
3. 展開 `Condition-IsHigh` / `Condition-IsMedium` → 確認走正確分支
4. 展開 `Respond-Success` → 確認 5 個欄位的值（Status / RiskScore / RiskLevel / RiskLevelLabel / ErrorMessage）

---

### F. 常見失敗原因（可觀測訊號 + Run History 定位）

| # | 可觀測訊號 | 根本原因 | Run History 定位方式 | 修正方法 |
|:-----|:-------------------|:--------------------------|:----------------------------------------------|:-------------------------------|
| F1 | GOV-013B 呼叫 013A 收到 `Status = Failed` | Likelihood / Impact 值不在 807660000~807660004 範圍 | 013A Run History → 展開 `Condition-ValidateInput` → 確認 False 分支觸發 | 確認 013B 傳入 `gov_likelihood` / `gov_impact` 的 Dataverse OptionSet 原始值（807660000 系列）而非 Label 文字 |
| F2 | `Compose-RiskScore` 輸出恆為 0 | Likelihood 或 Impact 傳入了 0（整數）而非 807660000 | 013A Run History → 展開 Trigger → 看 Inputs 的 Likelihood 和 Impact 值 | 確認 013B 的 Apply to each 用 `items()?['gov_likelihood']` 動態內容，而非硬編碼的 1~5 |
| F3 | `Respond-Success` 的 RiskLevel 恆為 807660000（Low） | Set variable 未執行，或 Condition 條件方向錯誤 | 013A Run History → 展開 `Condition-IsHigh` 和 `Condition-IsMedium` → 確認 True/False 走向 | 確認兩個 Set variable（RiskLevel 與 RiskLevelLabel）在各自 Condition 的 True 分支內，且 Operator 為 `is greater than or equal to` |
| F4 | 儲存 Flow 時報錯「Variable 'RiskLevel' not found」 | Initialize variable 被放入 Condition 或 Scope 內部 | Power Automate 編輯器 → 確認 Init-RiskLevel 的位置 | 將 Init-RiskLevel 和 Init-RiskLevelLabel 移到 Flow 最頂層（Trigger 正下方） |
| F5 | 013B 的「Run a Child Flow」下拉清單找不到 013A | Trigger 未勾選「Only other flows can trigger」，或 Flow 不在同一 Solution | 013B 編輯模式 → CallChildFlow-013A → Flow 下拉選單空白或無 013A | 開啟 013A → Trigger → Settings → 勾選 Only other flows；確認 013A 在同一 Solution |
| F6 | 013B 呼叫 013A 後 GOV-002 收到 schema mismatch 錯誤 | Respond-ValidationFailed 與 Respond-Success 的欄位集合不一致 | 比對兩個 Respond Action 的欄位清單 | 確認兩個 Respond 各有完全相同的 5 個欄位：Status、RiskScore、RiskLevel、RiskLevelLabel、ErrorMessage |

---

## GOV-013B：Risk Aggregator

### A. 基本資訊

| 項目 | 值 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 查詢指定專案的所有風險項目，逐筆呼叫 GOV-013A 計算 RiskScore，聚合出最高殘餘風險等級（HighestRiskLevel）回傳給 GOV-002 |
| Trigger 類型 | Manually trigger a flow（Child Flow）`[Governance Critical Control]` 必須勾選「Only other flows can trigger」 |
| 呼叫此 Flow 的來源 | GOV-002（Gate 3 申請時） |
| Connection References | CR-Dataverse-SPN |
| 對應測試案例 | 07文件 E2E-001 Phase 5 |

> **Apply to each 失敗處理說明**：若某筆 GOV-013A 回傳 Failed，此 Flow **不中斷**，繼續處理其他項目，以最高成功計算值作為 HighestRiskLevel 回傳。MVP 版本可接受此行為。

---

### B. Step 0：建構前必確認事項（必讀）

| # | 確認項目 | 確認方式 | 不符處置 |
|:-----|:--------------------------|:----------------------------------------------|:-------------------------------|
| B1 | GOV-013A 已建立且處於**開啟**狀態 | Power Automate → My flows → 確認 GOV-013A 狀態為 On | 先完成 GOV-013A 並通過 E. 最小驗證 |
| B2 | Risk Assessment Table 存在且有 `gov_likelihood`、`gov_impact`、`_gov_parentproject_value` 欄位 | Maker Portal → Dataverse → Tables → 搜尋 Risk Assessment | 先完成 02 文件 Dataverse Schema 建置 |
| B3 | CR-Dataverse-SPN Connection Reference 已指向有效 Service Principal 連線 | Solution → Connection References → CR-Dataverse-SPN | 先設定 Connection Reference |
| B4 | `Initialize variable` 必須在 Flow 最頂層，不可放在任何 Scope、Condition 或 Apply to each 內 | — | 放錯位置 → Flow 儲存時直接報錯 |
| B5 | Filter rows 的 Lookup 欄位格式：`_欄位名稱_value`（前後有底線），GUID 需用單引號包住 | 參考 D. 施工步驟 Step 3 | 格式錯誤 → List rows 回傳 0 筆但不報錯 |
| B6 | 所有 `Respond to a PowerApp or flow` 輸出欄位集合**完全一致**（5 個欄位） | 比對 Respond-NoRiskItems 與 Respond-Success | 欄位不一致 → GOV-002 收到 schema mismatch 500 |

---

### C. OptionSet 數值對照表

**RiskLevel 值（HighestLevel 追蹤變數）：**

| OptionSet 值 | 語意 | Label |
|:----------|:--------------------------------------|:------|
| 807660000 | Low（初始值） | `Low` |
| 807660001 | Medium | `Medium` |
| 807660002 | High | `High` |

> **HighestLevel 初始值為 807660000**：代表「尚未發現比 Low 更高的風險」。只有當 GOV-013A 計算結果更高時才更新此變數。

**Output Schema（成功與失敗的 Respond 欄位必須完全一致）：**

| 欄位名稱 | 類型 | 成功值 | 失敗值 |
|:----------------------------------------------|:----------|:----------------------------------------------|:----------------------------------------------|
| `Status` | Text | `Success` | `Failed` |
| `HighestRiskLevel` | Text | `High` / `Medium` / `Low` | （空字串） |
| `TotalRiskCount` | Number | 風險項目總數 | `0` |
| `ErrorCode` | Text | （空字串） | `ERR-013B-001` |
| `Message` | Text | （空字串） | 此專案無風險項目記錄 |

---

### D. 建立步驟（逐步點擊）

**Step 1：建立 Trigger**

1. Maker Portal → 解決方案 → DesignGovernanceSystem → + 新增 → 自動化 → Cloud flow → 立即
2. 搜尋 `manually` → 選擇「Manually trigger a flow（手動觸發 Flow）」
3. 點擊「+ Add an input」→ 選擇「**Text**」→ 名稱填入 `ProjectId`
4. 點擊 Trigger 右上角 `...` → 「Settings」→ 啟用「**Only other flows can trigger**」

**Step 2：Initialize variable — HighestLevel**

1. 點擊「+ New step（+ 新增步驟）」
2. 搜尋 `initialize variable` → 選擇「Variable（變數）」下的「Initialize variable（初始化變數）」
3. 設定：Name = `HighestLevel`、Type = `Integer`、Value = `807660000`
4. 命名：`Init-HighestLevel`

> **必須在 Flow 最頂層**（Trigger 正下方）。不可移入任何 Condition 或 Apply to each。

**Step 3：查詢此專案所有風險項目**

1. 點擊「+ New step」→ 搜尋 `list rows` → 選擇「Microsoft Dataverse」下的「List rows（列出資料列）」
2. 命名：`List-RiskItems`
3. 設定：
   - Table name: `Risk Assessment Table`（gov_riskassessment）
   - Filter rows:
     ```
     _gov_parentproject_value eq '@{triggerBody()?['ProjectId']}' and gov_residualrisklevel ne null
     ```
   - Select columns: `gov_riskassessmentid,gov_likelihood,gov_impact,gov_residualrisklevel`

> **Filter rows 注意事項**：`_gov_parentproject_value` 是 Lookup 欄位的 OData 名稱（前後有底線）；GUID 值必須用**單引號**包住。`gov_residualrisklevel ne null` 過濾掉殘餘風險等級未評估的記錄，避免 null 值導致比較失敗。

**Step 4：Condition — 是否有風險項目**

1. 搜尋 `condition` → 選擇「控制項（Control）」下的「Condition（條件）」
2. 命名：`Condition-HasRiskItems`
3. Left value（Expression 模式）：`length(outputs('List-RiskItems')?['body/value'])`，Operator：`is greater than`，Right value：`0`

**Step 5：False 分支（無風險項目或所有項目殘餘風險未評估 → 回傳 Failed）**

1. 在 False 分支加入「Respond to a PowerApp or flow（回應 PowerApp 或流程）」
2. 命名：`Respond-NoRiskItems`
3. 加入 5 個輸出欄位（順序必須與 Respond-Success 完全一致，見 C 節 Output Schema）：
   - Text → `Status` → `Failed`
   - Text → `HighestRiskLevel` → （空字串）
   - Number → `TotalRiskCount` → `0`
   - Text → `ErrorCode` → `ERR-013-INCOMPLETE`
   - Text → `Message` → `此專案無風險項目記錄或殘餘風險等級尚未評估（gov_residualrisklevel 為空）`

> **ERR-013-INCOMPLETE 說明**：當 Filter rows 加入 `gov_residualrisklevel ne null` 後，若所有風險項目的殘餘風險等級均未評估，查詢結果為 0 筆，Flow 進入 False 分支並回傳此錯誤碼，提示管理員完成所有風險項目的殘餘風險評估後再提交 Gate 申請。

**Step 6：True 分支 — Apply to each（逐筆計算）**

1. 在 True 分支加入「Apply to each（套用至每一個）」
2. 命名：`ForEach-RiskItem`
3. Select an output（Expression 模式）：`outputs('List-RiskItems')?['body/value']`

**Step 6.0：在 ForEach-RiskItem 內第一個 Action — Null 殘餘風險等級守衛**

在 Apply to each 內第一個 Action 前加入 Condition：
1. 搜尋 `condition` → 命名：`Condition-HasResidualRiskLevel`
2. 條件：`empty(items('ForEach-RiskItem')?['gov_residualrisklevel']) is equal to false`
3. True 分支（已評估殘餘風險等級）→ 繼續比較風險等級（呼叫 GOV-013A）
4. False 分支（殘餘風險等級未評估）→ （跳過此項 — 殘餘風險等級未評估，不計入聚合）

**Step 6.1：在 ForEach-RiskItem 內（Condition True 分支）— 呼叫 GOV-013A**

1. 在 Condition-HasResidualRiskLevel 的 **True 分支**，點擊「+ Add an action」
2. 搜尋 `run a child flow` → 選擇「Flows（流程）」下的「Run a Child Flow（執行子流程）」
3. 命名：`CallChildFlow-013A`
4. 設定：
   - Flow: 選擇 `GOV-013A-RiskScoreCalculator`
   - Likelihood: 動態內容 → `items('ForEach-RiskItem')?['gov_likelihood']`
   - Impact: 動態內容 → `items('ForEach-RiskItem')?['gov_impact']`

**Step 6.2：在 ForEach-RiskItem 內（Condition True 分支，接在 CallChildFlow-013A 之後）— 更新最高等級**

1. 搜尋 `condition` → 命名：`Condition-UpdateHighest`
2. 設定（Expression 模式）：
   - Left: `outputs('CallChildFlow-013A')?['body/RiskLevel']`
   - Operator: `is greater than`
   - Right: `variables('HighestLevel')`
3. **True 分支（更高 → 更新變數）**：
   - 加入「Set variable（設定變數）」→ Name: `HighestLevel`，Value（Expression）: `outputs('CallChildFlow-013A')?['body/RiskLevel']`

**Step 7：Apply to each 結束後 — Compose 轉換 Label**

1. 在 Condition-HasRiskItems True 分支的 **ForEach-RiskItem 之後**，搜尋 `compose` → 命名：`Compose-HighestLabel`
2. Inputs（Expression 模式）：
   ```
   if(
     equals(variables('HighestLevel'), 807660002),
     'High',
     if(
       equals(variables('HighestLevel'), 807660001),
       'Medium',
       'Low'
     )
   )
   ```

**Step 8：True 分支末端 — 回傳成功結果**

1. 搜尋 `respond` → 命名：`Respond-Success`
2. 加入 5 個輸出欄位（**與 Respond-NoRiskItems 欄位名稱、順序完全一致**）：
   - Text → `Status` → `Success`
   - Text → `HighestRiskLevel` → 動態內容 → `Compose-HighestLabel` 的「輸出」
   - Number → `TotalRiskCount` → Expression: `length(outputs('List-RiskItems')?['body/value'])`
   - Text → `ErrorCode` → （空字串）
   - Text → `Message` → （空字串）

**Step 9：儲存**

1. 點擊左上角 Flow 名稱 → 輸入：`GOV-013B-RiskAggregator`
2. 點擊「Save（儲存）」→ 等待成功

---

### E. 最小驗證流程（建構完成後立即執行）

**前提：已有測試專案，且 Risk Assessment Table 有 2~3 筆對應的風險項目。**

**製造測試資料（若無）：**
- Dataverse → Risk Assessment Table → + New row
- gov_parentproject: Lookup 選擇測試專案
- gov_likelihood: `807660003`（High），gov_impact: `807660004`（Critical）→ 預期 RiskScore=12 → High

**手動觸發 013B：**
1. Power Automate → My flows → `GOV-013B-RiskAggregator`
2. 「Test（測試）」→「Manually（手動）」→「Test flow」
3. 填入：`ProjectId` = `[測試專案的 gov_projectregistryid GUID]` → 點擊「Run flow」

**在 Run History 逐步確認（Power Automate → My flows → GOV-013B → 28 day run history）：**
1. 點入執行記錄 → 確認整條 Flow 綠色
2. 展開 `List-RiskItems` → Outputs 的 `value` 陣列有資料（若空 → 確認 Filter rows 語法與 B5）
3. 確認 `Condition-HasRiskItems` 走 True 分支
4. 展開 `ForEach-RiskItem` → 點進每次迭代：
   - 確認 `CallChildFlow-013A` 執行成功
   - 確認 `Condition-UpdateHighest` 走向符合預期
5. 展開 `Compose-HighestLabel` → 確認輸出為 `High` / `Medium` / `Low`
6. 展開 `Respond-Success` → 確認 Status=`Success`、HighestRiskLevel 符合預期、TotalRiskCount 正確

**無風險項目測試：** 用不存在 Risk Assessment 記錄的專案 ID 觸發 → 確認 `Condition-HasRiskItems` 走 False → `Respond-NoRiskItems` Status=`Failed`、ErrorCode=`ERR-013B-001`

---

### F. 常見失敗原因（可觀測訊號 + Run History 定位）

| # | 可觀測訊號 | 根本原因 | Run History 定位方式 | 修正方法 |
|:-----|:-------------------|:--------------------------|:----------------------------------------------|:-------------------------------|
| F1 | `List-RiskItems` 回傳 0 筆但確定有資料 | Filter rows 語法錯誤（Lookup 欄位格式或單引號遺漏） | Run History → 展開 `List-RiskItems` → 看 Inputs 的 Filter 字串 | 確認格式：`_gov_parentproject_value eq '@{triggerBody()?['ProjectId']}'`（含單引號） |
| F2 | `CallChildFlow-013A` 下拉清單找不到 GOV-013A | GOV-013A 未勾選 Only other flows，或不在同一 Solution | 013B 編輯模式 → CallChildFlow-013A → Flow 欄位空白 | 開啟 013A → Trigger Settings → 勾選 Only other flows；確認在同一 Solution |
| F3 | `CallChildFlow-013A` 執行失敗，013A Status=Failed | gov_likelihood 或 gov_impact 傳入值超出範圍 | 013A Run History → Trigger Inputs → 確認 Likelihood/Impact 值 | 確認 Risk Assessment Table 欄位型別是 OptionSet（807660000 系列）而非整數文字 |
| F4 | `Condition-UpdateHighest` 恆走 False（HighestLevel 永不更新） | Expression 中 Action 名稱與 CallChildFlow-013A 的實際命名不符 | Run History → 展開 CallChildFlow-013A → 看 Outputs 的欄位名稱 | 確認 `outputs('CallChildFlow-013A')?['body/RiskLevel']` 中的 Action 名稱與實際完全一致 |
| F5 | GOV-002 收到 013B 結果但 HighestRiskLevel 為空 | Respond-Success 的 HighestRiskLevel 引用路徑錯誤 | 013B Run History → 展開 Respond-Success → 看 HighestRiskLevel 欄位值 | 確認 Respond-Success 的 HighestRiskLevel 引用 `outputs('Compose-HighestLabel')` |
| F6 | GOV-002 報 schema mismatch 錯誤 | Respond-NoRiskItems 與 Respond-Success 的欄位集合不一致 | 比對兩個 Respond Action 的欄位清單 | 確認兩個 Respond 各有完全相同的 5 個欄位：Status、HighestRiskLevel、TotalRiskCount、ErrorCode、Message |
| F7 | ForEach 跳過所有 items（迭代 0 次） | Apply to each 的輸入未正確設為 List-RiskItems 的 body value | Run History → 展開 ForEach-RiskItem → 看 items 數量 | 確認 Apply to each 的輸入為 `outputs('List-RiskItems')?['body/value']`（含 body/value 路徑） |
| F8 | HighestLevel 永遠是初始值 Low（即使有 High 風險項目） | Condition-UpdateHighest 條件方向錯誤（Left/Right 對調） | Run History → ForEach → 展開 Condition-UpdateHighest → 確認 Left 是 GOV-013A RiskLevel，Right 是 HighestLevel | 確認 Left（GOV-013A 計算結果）> Right（現有 HighestLevel），Operator = `is greater than` |

## GOV-001：Create Project

### 基本資訊

### Trigger 條件

**觸發時機**：使用者透過 Power Apps FORM-001 提交專案建立表單時

**觸發者**：System Architect（系統架構師），透過 Power Apps「專案建立表單」點擊「提交」按鈕

**觸發方式**：**Power Apps (V2)** Trigger — Power Apps 中以 `FlowName.Run(參數...)` 呼叫，Flow 可透過 `Respond to a PowerApp or flow` 回傳結果

**不會自動觸發**：此 Flow 必須由使用者在 Power Apps 內主動觸發

### 前置條件

**Dataverse 前置資料**：
1. ✅ `gov_counterlist` 資料表已建立
2. ✅ Counter List 必須有一筆記錄，欄位如下：
   - `gov_countername = 'ProjectRequest'`（Text，用於查詢定位）
   - `gov_prefix = 'DR'`（Text，RequestID 前綴）
   - `gov_currentyear = 當年（如 2026）`（Whole Number）
   - `gov_nextseq = 初始值 1`（Whole Number，下一個可用序號）
   - **Row ID 取得方式**：在 Dataverse「Counter List」資料表 → 開啟該筆記錄 → 網址列中 `id=` 後面的 GUID 即為 Row ID，或使用 `List rows` 搭配 Filter `gov_countername eq 'ProjectRequest'` 查詢取得

**SharePoint 前置條件**：
1. ✅ SharePoint Site 已建立（如：/sites/GOV-Projects）
2. ✅ 根目錄已存在「Projects」文件庫

**Service Principal 前置條件**：
1. ✅ GOV-FlowServicePrincipal 已建立
2. ✅ 已授予 Dataverse 和 SharePoint 權限

**使用者輸入前置條件**：
1. ✅ Title（專案名稱）已填寫
2. ✅ ProjectType 已選擇
3. ✅ TargetSL 已選擇
4. ✅ SystemArchitect 已選擇
5. ✅ ProjectDescription 已填寫

**狀態前置條件**：無（這是建立新專案，無既有狀態）

### Flow I/O 定義

#### Input（Power Apps (V2) Trigger 參數）

以下參數在 Trigger 中以「Text input」定義，Power Apps 以 `.Run()` 呼叫時依序傳入。

| 參數名稱 | Trigger Input 類型 | 必填 | 對應 Dataverse 欄位 | 說明 |
|:--------------------------|:----------------------|:------:|:----------------------------------------------|:----------------------------------------------|
| Title | Text | ✓ | gov_title | 專案名稱（Max 200） |
| SystemArchitectEmail | Text | ✓ | gov_systemarchitect | SA 的 Email 地址 |
| ProjectManagerEmail | Text | ✓ | gov_projectmanager | PM 的 Email 地址 |
| SecurityReviewerEmail | Text | ✗ | （通知用） | 安全審查者 Email |
| QAReviewerEmail | Text | ✗ | （通知用） | QA 審查者 Email |
| ProjectType | Text | ✓ | gov_projecttype | 文字值（需 Flow 內轉換為 OptionSet） |
| TargetSL | Text | ✓ | gov_targetsl | 文字值（需 Flow 內轉換為 OptionSet） |
| ProjectDescription | Text | ✗ | gov_projectdescription | 專案描述（Max 2000） |
| SubmittedByEmail | Text | ✓ | （稽核用） | 提交者 Email |

**ProjectType / TargetSL 文字值 → OptionSet 對應**：

> **P-13 原則**：以下對應關係的唯一權威來源為 Dataverse `gov_optionsetmapping` 資料表。
> Flow 中禁止以 Switch/if 硬編碼此映射。下表僅為初始資料參考：

| FieldName | TextValue | NumericValue | 說明 |
|:----------------------------------------------|:----------------------------------------------|:----------|:----------------------------------------------|
| ProjectType | NewSystem | 807660000 | 新系統 |
| ProjectType | MajorArchChange | 807660001 | 重大架構變更 |
| ProjectType | SecurityCritical | 807660002 | 安全關鍵 |
| ProjectType | ComplianceChange | 807660003 | 合規變更 |
| TargetSL | SL1 | 807660000 | 安全等級 1 |
| TargetSL | SL2 | 807660001 | 安全等級 2 |
| TargetSL | SL3 | 807660002 | 安全等級 3 |
| TargetSL | SL4 | 807660003 | 安全等級 4 |

#### Output（回傳給 Power Apps + 寫入 Dataverse）

**回傳給 Power Apps**（透過 Respond to a PowerApp or flow）：

| 輸出參數 | 類型 | 說明 |
|:----------------------------------------------|:----------|:----------------------------------------------|
| Status | Text | `Success` 或 `Failed` |
| ErrorCode | Text | 錯誤代碼（成功時為空白） |
| Message | Text | 結果訊息 |
| RequestID | Text | 產生的專案編號（如 `DR-2026-0001`） |
| ProjectRowId | Text | Dataverse 記錄 GUID |
| FolderLink | Text | SharePoint 專案主資料夾 URL |
| FlowRunId | Text | Flow 執行 Run ID（`workflow()?['run']?['name']`），用於端對端追溯 |

**主要寫入目標**：`gov_projectregistry`

| 欄位名稱 | 值來源 | 設定方式 | 說明 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| gov_requestid | Counter List 產生 | `concat('DR-', string(年份), '-', 補零序號)` | 主鍵（如 DR-2026-0001） |
| gov_title | Input | 直接使用 | 專案名稱 |
| gov_projecttype | Input 轉換 | Mapping Table 讀取文字值 → OptionSet 數值（P-13 原則） | 專案類型 |
| gov_targetsl | Input 轉換 | Mapping Table 讀取文字值 → OptionSet 數值（P-13 原則） | 目標安全等級 |
| gov_systemarchitect | Input | 直接使用 | 系統架構師 Email |
| gov_projectmanager | Input | 直接使用（可空） | 專案經理 Email |
| gov_projectdescription | Input | 直接使用（可空） | 專案描述 |
| gov_currentgate | Flow 設定 | 807660000 (Pending) | PreGate0 狀態 |
| gov_requeststatus | Flow 設定 | 807660000 (None) | 尚未提交審批 |
| gov_projectstatus | Flow 設定 | 807660000 (Active) | 專案已啟動 |
| gov_documentfreezestatus | Flow 設定 | 807660000 (NotFrozen) | 文件未凍結 |
| gov_sharepointfolderurl | Flow 產生 | SharePoint 資料夾 URL | 專案文件夾連結 |

**次要寫入目標**：`gov_reviewdecisionlog`（一筆建立事件記錄）

| 欄位名稱 | 值來源 | 說明 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| gov_reviewid | Flow 產生 | concat(RequestID, '-CREATE') |
| gov_reviewtype | Flow 設定 | 807660000 (ProjectCreation) |
| gov_parentproject | 上一步建立的專案 | Lookup 至 gov_projectregistry |
| gov_submittedby | Input | SubmittedByEmail |
| gov_submitteddate | Flow 設定 | utcNow() |
| gov_decision | Flow 設定 | 807660003 (Executed) |

#### SharePoint Output

**建立資料夾**：`/Documents/{RequestID}`

**子資料夾結構**（P-11 原則：從 Dataverse `gov_documentfolderbaseline` 讀取，不得硬寫）：
- 由 Dataverse Document Folder Baseline 資料表驅動
- 初始值對齊 Doc 03 第 5 章：01_Feasibility, 02_Risk_Assessment, 03_Design, 04_Security, 05_Test, 06_Handover
- 若業務需新增子資料夾，僅需在 Dataverse 新增記錄，無需修改 Flow



| 項目 | 值 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 接收 Power Apps 提交的專案建立請求，建立專案記錄與 SharePoint 資料夾，回傳結果給 Power Apps |
| Trigger 類型 | **Power Apps (V2)** |
| 觸發來源 | FORM-001 Intake Form（Power Apps），以 `GOV001CreateProject.Run(...)` 呼叫 |
| Connection References | CR-Dataverse-SPN, CR-SharePoint-SPN, CR-Office365Groups `[MVP: 全部使用個人帳號連線]` |
| Concurrency Control | Off |
| 對應測試案例 | 07文件 E2E-001 Phase 1, 4.3.1 |

> **Input / Output 完整定義請見上方「Flow I/O 定義」章節。**
> Choice 欄位由 Power Apps 傳入文字值，Flow 內部以 Mapping Table 轉換為 OptionSet 數值（P-13 原則）。

### 建立步驟（逐步點擊）

**步驟 1**：建立 Power Apps (V2) Trigger
```
1. Maker Portal → 解決方案 → DesignGovernanceSystem → + 新增 → 自動化 → Cloud flow → 立即
2. 搜尋 power apps → 選擇「Power Apps (V2)」Trigger
   （中文介面搜尋 power apps 即可找到，分類為「Power Apps」）
3. 點擊「+ Add an input」（中文：「+ 新增輸入」），依序新增以下參數：
   - 選擇「Text」→ 標題填入 Title
   - 選擇「Text」→ 標題填入 SystemArchitectEmail
   - 選擇「Text」→ 標題填入 ProjectManagerEmail
   - 選擇「Text」→ 標題填入 SecurityReviewerEmail（取消勾選「必要」）
   - 選擇「Text」→ 標題填入 QAReviewerEmail（取消勾選「必要」）
   - 選擇「Text」→ 標題填入 ProjectType
   - 選擇「Text」→ 標題填入 TargetSL
   - 選擇「Text」→ 標題填入 ProjectDescription（取消勾選「必要」）
   - 選擇「Text」→ 標題填入 SubmittedByEmail
```

> **Power Apps 呼叫方式**（在 FORM-001 的「提交」按鈕 OnSelect）：
> ```
> Set(varFlowResult,
>     GOV001CreateProject.Run(
>         txtTitle.Text,
>         ddSystemArchitect.Selected.Email,
>         ddProjectManager.Selected.Email,
>         txtSecurityReviewer.Text,
>         txtQAReviewer.Text,
>         ddProjectType.Selected.Value,
>         ddTargetSL.Selected.Value,
>         txtDescription.Text,
>         User().Email
>     )
> );
> ```

**步驟 2**：Pre-check 1（驗證提交者權限）
```
Action：List group members (Office 365 Groups)
  （搜尋 list group members → 選擇「Office 365 Groups」Connector）
  連線：CR-Office365Groups
  Group Id：{貼上 GOV-Architects 的 Object ID}

Action：Filter array
  （搜尋 filter array → 選擇「資料作業」下的「Filter array」，中文可能為「篩選陣列」）
  From：outputs('List_group_members')?['value']
  Condition（進階模式）：
  @equals(toLower(item()?['mail']), toLower(triggerBody()['SubmittedByEmail']))

Action：Condition
  （搜尋 condition → 選擇「控制項」下的「Condition」，中文可能為「條件」）
  條件：length(body('Filter_array')) is greater than 0

  False 分支：
    Action：Respond to a PowerApp or flow
      （搜尋 respond → 選擇「Respond to a PowerApp or flow」，中文可能為「回應 PowerApp 或流程」）
      點擊「+ Add an output」，新增以下輸出（Canonical Error Envelope v5.0）：
        - Number：StatusCode → 400
        - Text：Status → Failed
        - Text：ErrorCode → ERR-001-002
        - Text：ErrorStage → PreCheck
        - Text：Message → 僅授權架構師可建立專案
        - Text：RequestID → （空白）
        - Text：ProjectRowId → （空白）
        - Text：FolderLink → （空白）
        - Text：FlowRunId → @{workflow()?['run']?['name']}
        - Text：Timestamp → @{utcNow()}
    Action：Terminate
      （搜尋 terminate → 選擇「控制項」下的「Terminate」，中文可能為「終止」）
      Status：Failed
      Code：ERR-001-002
      Message：僅授權架構師可建立專案
```

**步驟 3**：宣告變數（必須在 Trigger 之後、Scope 之前）
```
重要：Power Automate 規定 Initialize variable 只能放在 Flow 的最頂層，
     不可放在 Scope、Condition、Apply to each 等區塊內。

3.1  Action：Initialize variable
     （搜尋 initialize variable → 選擇「變數」下的「Initialize variable」，中文為「初始化變數」）
     Name：varNextSeq
     Type：Integer
     Value：0

3.2  Action：Initialize variable
     Name：RequestID
     Type：String
     Value：（留空）
```

**步驟 3A**：讀取 Counter List 並產生 RequestID
```
3A.1  Action：List rows (Dataverse)
      （搜尋 list rows → 選擇「Microsoft Dataverse」下的「List rows」，中文為「列出資料列」）
      連線：CR-Dataverse-SPN [MVP: 使用個人帳號連線]
      Table name：Counter List（gov_counterlist）
      Filter rows：gov_countername eq 'ProjectRequest'
      Row count：1
      重新命名為「Get_Counter」

      ⚠ Guard Clause（防呆）：Counter List 記錄不存在時的處理
      ────────────────────────────────────────
      3A.1b  Action：Condition（檢查 Counter 記錄是否存在）
             條件：length(outputs('Get_Counter')?['body/value']) is equal to 0

             True 分支（Counter 記錄不存在 → 立即終止）：
               Action：Respond to a PowerApp or flow
                 StatusCode: 400, Status: Failed, ErrorCode: ERR-001-COUNTER,
                 ErrorStage: CounterUpdate,
                 Message: Counter List 中找不到 ProjectRequest 記錄，請先建立初始資料,
                 RequestID: (空), ProjectRowId: (空), FolderLink: (空),
                 FlowRunId: @{workflow()?['run']?['name']},
                 Timestamp: @{utcNow()}
               Action：Terminate → Status: Failed

             False 分支（記錄存在 → 繼續）：
               （接下去 3A.2）

      ⚠ recordId 來源：後續步驟中使用的 Row ID 必須來自 Get_Counter 的結果主鍵：
         first(outputs('Get_Counter')?['body/value'])?['gov_counterlistid']
         不可手動貼固定 GUID，因為 DEV / PROD 的記錄 ID 不同。
      ────────────────────────────────────────

3A.2  Action：Compose
      （搜尋 compose → 選擇「資料作業」下的「Compose」，中文可能為「撰寫」）
      重新命名為「Compose-CurrentYear」
      Inputs：@{int(formatDateTime(utcNow(), 'yyyy'))}

3A.3  Action：Condition（判斷年份是否跨年）
      （搜尋 condition → 選擇「控制項」下的「Condition」，中文可能為「條件」）
      條件：outputs('Compose-CurrentYear') is not equal to first(outputs('Get_Counter')?['body/value'])?['gov_currentyear']

      True 分支（跨年 → 重置序號為 1）：
        Action：Set variable
          （搜尋 set variable → 選擇「變數」下的「Set variable」，中文為「設定變數」）
          Name：varNextSeq
          Value：1
        Action：Update a row (Dataverse)
          （搜尋 update a row → 選擇「Microsoft Dataverse」下的「Update a row」，中文為「更新資料列」）
          Table name：Counter List
          Row ID：@{first(outputs('Get_Counter')?['body/value'])?['gov_counterlistid']}
          gov_currentyear：@{outputs('Compose-CurrentYear')}
          gov_nextseq：2（下一次可用序號）

      False 分支（同年 → 讀取當前序號並遞增）：
        Action：Set variable
          Name：varNextSeq
          Value：@{first(outputs('Get_Counter')?['body/value'])?['gov_nextseq']}
        Action：Update a row (Dataverse)
          Table name：Counter List
          Row ID：@{first(outputs('Get_Counter')?['body/value'])?['gov_counterlistid']}
          gov_nextseq：@{add(variables('varNextSeq'), 1)}

3A.4  Action：Compose（補零序號 — P-08 標準範本）
      （搜尋 compose → 選擇「資料作業」下的「Compose」，中文可能為「撰寫」）
      重新命名為「Compose-PaddedSeq」
      Inputs — 直接將以下整段貼入 Expression 欄位（不要手打）：

      substring(concat('0000', string(variables('varNextSeq'))), sub(length(concat('0000', string(variables('varNextSeq')))), 4), 4)

      ⚠ 重要：
      - varNextSeq 是整數（Integer），concat 只接受字串，所以必須用 string() 包裹
      - 不要用 padLeft — Power Automate 不支援此函數，會直接報錯
      - 表達式中不需要加 @{} 前後綴，Power Automate Expression 欄位會自動處理
      - 原理說明請見前文「P-08 標準補零範本」章節

3A.5  Action：Compose
      重新命名為「Compose-RequestID」
      Inputs — 直接將以下整段貼入 Expression 欄位：

      concat(first(outputs('Get_Counter')?['body/value'])?['gov_prefix'], '-', string(outputs('Compose-CurrentYear')), '-', outputs('Compose-PaddedSeq'))

      ⚠ 注意：outputs('Compose-CurrentYear') 是整數（因為 int(formatDateTime(...))），
         必須用 string() 包裹才能 concat，否則會報 InvalidTemplate 錯誤

      結果範例：DR-2026-0001

3A.6  Action：Set variable
      Name：RequestID
      Value：@{outputs('Compose-RequestID')}
```

> **補零說明**：上述以 `concat('0000', ...)` 加上 `substring` + `sub` + `length` 組合實現補零效果。
> 若需更長的補零位數（如 6 位），將 `'0000'` 改為 `'000000'`，將 `4` 改為 `6`。
>
> **Initialize variable 限制**：`Initialize variable` 只能放在 Flow 最頂層（Trigger 正下方），不可放在 Scope、Condition、Apply to each 內。若需在分支中改值，請使用 `Set variable`。

**步驟 4**：建立 Scope: Try-MainLogic
```
搜尋 scope → 選擇「控制項」下的「Scope」（中文可能為「範圍」）
重新命名為「Try-MainLogic」
將以下步驟 5 ~ 步驟 10 的所有 Action 放入此 Scope
```

**步驟 5**：ProjectType / TargetSL 文字轉 OptionSet（P-13 原則：Mapping Table 去耦合）
```
說明：禁止在 Flow 中以 Switch/if 將文字硬轉為 OptionSet 數值（P-13 原則）。
     必須從 Dataverse「OptionSet Mapping Table」（gov_optionsetmapping）讀取對應關係。
     若業務需新增或修改 OptionSet 值，僅需修改 Dataverse 資料表，無需修改 Flow。

5.1 Action：List rows (Dataverse)（讀取 ProjectType 映射）
    （搜尋 list rows → 選擇「Microsoft Dataverse」下的「List rows」，中文為「列出資料列」）
    連線：CR-Dataverse-SPN
    Table name：OptionSet Mapping（gov_optionsetmapping）
    Filter rows：gov_fieldname eq 'ProjectType' and gov_textvalue eq '@{triggerBody()['ProjectType']}'
    Row count：1
    重新命名為「Lookup_ProjectType」

5.2 Action：Compose
    （搜尋 compose → 選擇「資料作業」下的「Compose」，中文可能為「撰寫」）
    重新命名為「Compose-ProjectTypeValue」
    Inputs：@{first(outputs('Lookup_ProjectType')?['body/value'])?['gov_numericvalue']}

5.3 Action：Condition（驗證 ProjectType 映射存在）
    （搜尋 condition → 選擇「控制項」下的「Condition」，中文可能為「條件」）
    條件：length(outputs('Lookup_ProjectType')?['body/value']) is equal to 0

    True 分支：
      Respond to a PowerApp or flow →
      StatusCode: 400, Status: Failed, ErrorCode: ERR-001-011,
      ErrorStage: OptionSetMapping,
      Message: 無效的 ProjectType 值, RequestID: (空), ProjectRowId: (空), FolderLink: (空),
      FlowRunId: @{workflow()?['run']?['name']}, Timestamp: @{utcNow()}
      Terminate → Failed

5.4 Action：List rows (Dataverse)（讀取 TargetSL 映射）
    Table name：OptionSet Mapping（gov_optionsetmapping）
    Filter rows：gov_fieldname eq 'TargetSL' and gov_textvalue eq '@{triggerBody()['TargetSL']}'
    Row count：1
    重新命名為「Lookup_TargetSL」

5.4a Guard Clause（TargetSL mapping 查無結果）：
    Condition：length(outputs('Lookup_TargetSL')?['body/value']) is equal to 0
    True → Respond to a PowerApp or flow
      StatusCode：400
      Status：Failed
      ErrorCode：ERR-001-011
      ErrorStage：OptionSetMapping
      ErrorMessage：TargetSL mapping not found — 請確認 gov_optionsetmapping 資料表中有對應的 TargetSL 設定
    → Terminate

5.5 Action：Compose
    重新命名為「Compose-TargetSLValue」
    Inputs：@{first(outputs('Lookup_TargetSL')?['body/value'])?['gov_numericvalue']}

預期 Dataverse OptionSet Mapping 資料表結構：
    gov_fieldname: Text（如 ProjectType, TargetSL）
    gov_textvalue: Text（如 NewSystem, SL1）
    gov_numericvalue: Whole Number（如 807660000, 807660001）
    gov_displayname: Text（人類可讀名稱，如「新系統」、「安全等級 1」）
    gov_isactive: Boolean（是否啟用）
```

**步驟 6**：建立 Project Registry 記錄
```
Action：Add a new row (Dataverse)
  （搜尋 add a new row → 選擇「Microsoft Dataverse」下的「Add a new row」，中文為「新增資料列」）
  連線：CR-Dataverse-SPN
  Table name：Project Registry
  重新命名為「Add_Project_Registry」

  欄位對應：
    gov_requestid：@{variables('RequestID')}
    gov_title：@{triggerBody()['Title']}
    gov_systemarchitect：@{triggerBody()['SystemArchitectEmail']}
    gov_projectmanager：@{triggerBody()['ProjectManagerEmail']}
    gov_projecttype：@{outputs('Compose-ProjectTypeValue')}
    gov_targetsl：@{outputs('Compose-TargetSLValue')}
    gov_projectdescription：@{triggerBody()['ProjectDescription']}
    gov_currentgate：807660000（Pending）
    gov_requeststatus：807660000（None）
    gov_projectstatus：807660000（Active）
    gov_documentfreezestatus：807660000（Not Frozen）
    gov_reworkcount：0
    gov_submittedby：@{triggerBody()['SubmittedByEmail']}
    gov_submittedat：@{utcNow()}
    gov_sharepointprovisionstatus：807660000（NotStarted）
```

> **v5.0 新增欄位說明**：
> - `gov_submittedby`：記錄實際提交 Flow 的使用者 Email（而非 SystemArchitect，兩者可能不同）
> - `gov_submittedat`：記錄 Flow 執行當下的 UTC 時間，而非 Dataverse 的 createdon（createdon 可能有數秒延遲）
> - `gov_sharepointprovisionstatus`：初始為 NotStarted，步驟 7 成功後更新為 Success，失敗時為 Failed（見步驟 7 fault tolerance）

**步驟 7**：建立 SharePoint 資料夾結構（Dataverse 驅動，P-11 原則）

> **前置條件**：執行此步驟前，Dataverse `gov_documentfolderbaseline` 資料表必須已建立且包含初始資料。
> 若資料表為空，Apply to each 不會報錯但會跳過，導致 SharePoint 只有主資料夾而沒有子資料夾。

**`gov_documentfolderbaseline` 資料表欄位需求**：

| 欄位 Schema Name | 欄位類型 | 必填 | 說明 |
|:----------------------------------------------|:----------------------|:------:|:----------------------------------------------|
| `gov_foldername` | Text (100) | 是 | 子資料夾名稱，如 `01_Feasibility` |
| `gov_sortorder` | Whole Number | 是 | 建立順序（由小到大） |
| `gov_isactive` | Yes/No | 是 | 是否啟用（停用的資料夾不會建立） |
| `gov_description` | Text (500) | 否 | 資料夾用途說明 |

**最低初始資料（6 筆，由管理員在 Dataverse 中建立）**：

| gov_foldername | gov_sortorder | gov_isactive | gov_description |
|:----------------------------------------------|:----------|:----------|:----------------------------------------------|
| 01_Feasibility | 1 | Yes | 可行性評估文件 |
| 02_Risk_Assessment | 2 | Yes | 風險評估文件 |
| 03_Design | 3 | Yes | 設計文件 |
| 04_Security | 4 | Yes | 資安審查文件 |
| 05_Test | 5 | Yes | 測試文件 |
| 06_Handover | 6 | Yes | 交付文件 |

```
說明：資料夾名稱不得硬寫於 Flow。必須從 Dataverse「Document Folder Baseline」
     資料表（gov_documentfolderbaseline）讀取資料夾結構。
     若業務需新增或移除子資料夾，僅需修改 Dataverse 資料表，無需修改 Flow。

     ⚠ v5.0 Fault Tolerance：SharePoint 步驟被包在 Scope: Try-SharePointProvision 中。
     若 SharePoint 建立失敗，專案記錄仍然建立成功（ProvisionStatus = Failed），
     Flow 回傳 PROVISION_FAIL 警告，管理員可後續手動建立資料夾。

Scope: Try-SharePointProvision（搜尋 scope → 新增「Scope」，重新命名）
  ├── 以下 7.1 ~ 7.3 放在此 Scope 內 ──

7.1 Action：Create new folder (SharePoint)（建立專案主資料夾）
    （搜尋 create new folder → 選擇「SharePoint」下的「Create new folder」，中文為「建立新資料夾」）
    連線：CR-SharePoint-SPN [MVP: 使用個人帳號連線]
    Site Address：選擇 Design Governance Site
    List or Library：Design Documents
    Folder Path：@{variables('RequestID')}
    重新命名為「Create_SharePoint_Root_Folder」

7.2 Action：List rows (Dataverse)（讀取子資料夾定義）
    （搜尋 list rows → 選擇「Microsoft Dataverse」下的「List rows」，中文為「列出資料列」）
    連線：CR-Dataverse-SPN [MVP: 使用個人帳號連線]
    Table name：Document Folder Baseline（gov_documentfolderbaseline）
    Filter rows：gov_isactive eq true
    Order by：gov_sortorder asc
    重新命名為「List_FolderBaseline」

    ⚠ 若此 Action 回傳 0 筆記錄，表示資料表為空或沒有 gov_isactive = true 的記錄。
      請先到 Dataverse → Document Folder Baseline 確認已建立上表 6 筆初始資料。

7.3 Action：Apply to each（對每筆 Folder Baseline 建立子資料夾）
    （搜尋 apply to each → 選擇「控制項」下的「Apply to each」，中文為「套用至每一個」）
    Select an output：outputs('List_FolderBaseline')?['body/value']

    Action：Create new folder (SharePoint)
      （搜尋 create new folder → 選擇「SharePoint」下的「Create new folder」，中文為「建立新資料夾」）
      連線：CR-SharePoint-SPN [MVP: 使用個人帳號連線]
      Site Address：選擇 Design Governance Site
      List or Library：Design Documents
      Folder Path：@{variables('RequestID')}/@{items('Apply_to_each')?['gov_foldername']}
      重新命名為「Create_Subfolder」

  └── Scope 結束 ──

7.4 Action：Update a row (Dataverse)（ProvisionStatus = Success）
    設定 Configure run after：Try-SharePointProvision → 僅勾選「成功」
    Table name：Project Registry
    Row ID：@{outputs('Add_Project_Registry')?['body/gov_projectregistryid']}
    gov_sharepointprovisionstatus：807660001（Success）
    重新命名為「Update_ProvisionStatus_Success」

Scope: Catch-SharePointProvision（SharePoint 建立失敗的容錯處理）
    設定 Configure run after：Try-SharePointProvision → 取消「成功」→ 勾選「已失敗」與「已逾時」

    Action：Update a row (Dataverse)（ProvisionStatus = Failed）
      Table name：Project Registry
      Row ID：@{outputs('Add_Project_Registry')?['body/gov_projectregistryid']}
      gov_sharepointprovisionstatus：807660002（Failed）
      重新命名為「Update_ProvisionStatus_Failed」

    ⚠ 注意：SharePoint 建立失敗時，Flow 不會終止。
      專案記錄已在步驟 6 成功建立，Baseline Seeding（步驟 7.5）仍會繼續執行。
      成功回應中的 FolderLink 將為空白，Message 包含 PROVISION_FAIL 警告。
```

> **SharePoint Provision Fault Tolerance（v5.0）**：
> 將 SharePoint 操作包在獨立 Scope 中，使 SharePoint 暫時不可用時不阻擋專案建立。
> 管理員可透過 `gov_sharepointprovisionstatus = Failed` 篩選出需要手動補建資料夾的專案。
> 此設計遵循「Dataverse 是唯一事實來源」原則——專案存在於 Dataverse 即為已建立。

**步驟 7.5**：Baseline Seeding — 建立 Document Register 基線記錄（Dataverse 驅動）

> **前置條件**：Dataverse `Document Baseline Matrix` 資料表必須已建立且包含初始資料。
> 若資料表為空，Apply to each 不會報錯但會跳過，導致 Document Register 沒有 Planned 記錄。

**Document Baseline Matrix 必要欄位（Flow 讀取時使用的欄位）**：

| 欄位 Schema Name | 欄位類型 | 必填 | 說明 |
|:----------------------------------------------|:----------------------|:------:|:----------------------------------------------|
| `gov_documenttypename` | Text | 是 | DocumentType 文字名稱（如 TechnicalFeasibility） |
| `gov_documenttypevalue` | Whole Number | 是 | DocumentType OptionSet 數值（807660000 系列） |
| `gov_requiredforgate` | Text | 是 | 必須在哪個 Gate 前提交（如 Gate0、Gate1、`-` 表示不強制） |
| `gov_deliverablepackage` | Text | 否 | 所屬交付包名稱 |
| `gov_sharepointfolder` | Text | 是 | 對應 SharePoint 子資料夾名稱（供 GOV-005 使用） |
| `gov_projectregistrylinkfield` | Text | 是 | 對應 Project Registry 的 Link 欄位名稱（供 GOV-005 使用） |

> **初始資料筆數**：至少 13 筆（對應 13 種 DocumentType），RequiredForGate 不等於 `-` 的記錄會被 Seeding。
> 具體 DocumentType 清單請見本文件「DocumentType 與目標資料夾對應」章節。

```
說明：從 Dataverse「Document Baseline Matrix」資料表讀取所有 RequiredForGate ≠ '-' 的記錄，
     為每筆記錄建立一筆 DocumentRole = Planned 的 Document Register。
     Flow 不得硬編碼 DocumentType 清單。（P-01 原則：Dataverse 是唯一事實來源）

Action：List rows (Dataverse)
  （搜尋 list rows → 選擇「Microsoft Dataverse」下的「List rows」，中文為「列出資料列」）
  Table name：Document Baseline Matrix
  Filter rows：gov_requiredforgate ne '-'
  重新命名為「List_BaselineMatrix」

Action：Apply to each（對每筆 Baseline Matrix 記錄建立 Planned Document Register）
  （搜尋 apply to each → 選擇「控制項」下的「Apply to each」，中文為「套用至每一個」）
  Select an output：outputs('List_BaselineMatrix')?['body/value']

  Action：Add a new row (Dataverse)
    （搜尋 add a new row → 選擇「Microsoft Dataverse」下的「Add a new row」，中文為「新增資料列」）
    Table name：Document Register
    欄位對應：
      gov_documentid：@{concat('DOC-', variables('RequestID'), '-', items('Apply_to_each')?['gov_documenttypename'], '-PLANNED')}
      gov_parentproject：@{outputs('Add_Project_Registry')?['body/gov_projectregistryid']}
      gov_documenttype：@{items('Apply_to_each')?['gov_documenttypevalue']}
      gov_documentname：@{concat(items('Apply_to_each')?['gov_documenttypename'], ' (Planned)')}
      gov_documentversion：（空白）
      gov_sharepointfilelink：（空白）
      gov_requiredforgate：@{items('Apply_to_each')?['gov_requiredforgate']}
      gov_documentrole：807660000（Planned）
      gov_deliverablepackage：@{items('Apply_to_each')?['gov_deliverablepackage']}
      gov_uploadedby：（空白，尚未上傳）
      gov_uploadeddate：（空白）
      gov_reviewstatus：（空白）
      gov_isfrozen：false
      gov_comments：Baseline seeding - auto-created at project creation

Baseline Seeding 完成後預期結果：
  - Document Register 新增 N 筆記錄（= Document Baseline Matrix 中 RequiredForGate ≠ '-' 的記錄數）
  - 每筆記錄 DocumentRole = Planned
  - SharePointFileLink 為空白（尚未上傳）
  - 若業務需新增或移除 DocumentType，僅需修改 Dataverse Baseline Matrix 資料表，無需修改 Flow
```

**步驟 8**：寫入 Review Decision Log
```
Action：Add a new row (Dataverse)
Table name：Review Decision Log

欄位對應：
  gov_reviewid：@{concat('RDL-', variables('RequestID'), '-', formatDateTime(utcNow(), 'yyyyMMddHHmmss'))}
  gov_reviewtype：807660000（ProjectCreation）
  gov_parentproject：@{outputs('Add_Project_Registry')?['body/gov_projectregistryid']}
  gov_decision：807660003（Executed）
  gov_revieweddate：@{utcNow()}
  gov_triggerflowrunid：@{workflow()?['run']?['name']}
  gov_comments：專案已建立
```

**步驟 9**：呼叫 GOV-015 發送通知
```
Action：Run a Child Flow
  （搜尋 run a child flow → 選擇「流程」下的「Run a Child Flow」，中文為「執行子流程」）
  Child Flow：GOV-015-NotificationHandler

  輸入：
    NotificationType：ProjectCreated
    RecipientEmail：@{triggerBody()['SystemArchitectEmail']}
    Subject：專案已建立 - @{variables('RequestID')}
    Body：您的專案「@{triggerBody()['Title']}」已成功建立。請準備 Gate 0 必要文件後申請進入 Gate 0。
    ProjectId：@{variables('RequestID')}
```

**步驟 9A**：FlowRunId Writeback（P-16 原則 — 回寫執行狀態至 Project Registry）
```
Action：Update a row (Dataverse)
  （搜尋 update a row → 選擇「Microsoft Dataverse」下的「Update a row」，中文為「更新資料列」）
  連線：CR-Dataverse-SPN [MVP: 使用個人帳號連線]
  Table name：Project Registry
  Row ID：@{outputs('Add_Project_Registry')?['body/gov_projectregistryid']}
  重新命名為「Writeback_FlowRunId_Success」

  欄位對應：
    gov_lastflowrunid：@{workflow()?['run']?['name']}
    gov_lastflowstatus：807660000（Success）
```

> **P-16 原則**：此步驟將 Flow 執行的 Run ID 與狀態回寫至 Project Registry，
> 使管理員可直接在 Dataverse 端查詢「最近一次 Flow 執行狀態」而無需開啟 Flow Run History。
> Catch 路徑也必須執行 Writeback（見步驟 11），但 Status 為 Failed。

**步驟 10**：成功回應（回傳給 Power Apps — Canonical Error Envelope v5.0）
```
Action：Respond to a PowerApp or flow
  （搜尋 respond → 選擇「Respond to a PowerApp or flow」，中文為「回應 PowerApp 或流程」）
  點擊「+ Add an output」，依序新增：
    - Number：StatusCode → 200
    - Text：Status → Success
    - Text：ErrorCode → （空白）
    - Text：ErrorStage → （空白）
    - Text：Message → 專案建立成功
    - Text：RequestID → @{variables('RequestID')}
    - Text：ProjectRowId → @{outputs('Add_Project_Registry')?['body/gov_projectregistryid']}
    - Text：FolderLink → @{outputs('Create_SharePoint_Root_Folder')?['body/{Link}']}
    - Text：FlowRunId → @{workflow()?['run']?['name']}
    - Text：Timestamp → @{utcNow()}
```

> **Power Apps 接收回傳值**：
> ```
> // 在 Power Apps 中取得 Flow 回傳值
> If(varFlowResult.status = "Success",
>     Notify("專案建立成功：" & varFlowResult.requestid, NotificationType.Success);
>     Navigate(ProjectDetailScreen, ScreenTransition.None),
>     Notify("建立失敗：" & varFlowResult.message, NotificationType.Error)
> );
> ```

**步驟 11**：建立 Scope: Catch-ErrorHandler
```
搜尋 scope → 新增「Scope」，重新命名為「Catch-ErrorHandler」
設定 Configure run after：點擊「...」→「設定在之後執行」→ 取消「成功」→ 勾選「已失敗」與「已逾時」

內容：
  Action：Compose（擷取錯誤訊息）
    （搜尋 compose → 選擇「資料作業」下的「Compose」，中文可能為「撰寫」）
    重新命名為「Compose-ErrorMessage」
    Inputs：@{coalesce(result('Try-MainLogic')?[0]?['error']?['message'], '未知錯誤')}

  Action：Condition（檢查 Project Registry 是否已建立）
    條件：outputs('Add_Project_Registry')?['body/gov_projectregistryid'] is not equal to null

    True 分支（補償交易 — Compensating Transaction）：
      Action：Delete a row (Dataverse)
        （搜尋 delete a row → 選擇「Microsoft Dataverse」下的「Delete a row」，中文為「刪除資料列」）
        Table：Project Registry
        Row ID：@{outputs('Add_Project_Registry')?['body/gov_projectregistryid']}
        重新命名為「Delete_ProjectRegistryRecord」

      ✅ [已修正 BUG-015] SharePoint 刪除需先確認資料夾是否曾建立
      Action：Condition（資料夾是否已建立？）
        重新命名為「Is_FolderCreated」
        條件：equals(result('Try-SharePointProvision')?[0]?['status'], 'Succeeded')
        （只有在 Try-SharePointProvision Scope 成功執行時，才嘗試刪除資料夾）

        True 分支（資料夾曾建立，嘗試刪除）：
          Action：Delete folder (SharePoint)
            Folder Path：@{variables('RequestID')}
            Configure run after：成功 + 失敗（不論結果繼續執行 — 確保 Respond 一定送出）

        False 分支（資料夾從未建立，跳過）：
          （不做任何事）

      ✅ [已修正 BUG-028] 雙重失敗保護：Delete_ProjectRegistryRecord 若也失敗，回寫 FlowRunId
      Action：Update a row (Dataverse)
        Configure run after：Delete_ProjectRegistryRecord → 勾選「已失敗」（只在刪除失敗時執行）
        重新命名為「Writeback_OrphanRecord」
        Table name：Project Registry
        Row ID：@{outputs('Add_Project_Registry')?['body/gov_projectregistryid']}
        欄位對應：
          gov_lastflowstatus：807660001（Failed）
          gov_lastflowrunid：workflow()?['run']?['name']
          gov_lasterrorcode：ERR-001-SYSTEM
        說明：若補償刪除也失敗，孤兒記錄上仍有 FlowRunId，操作員可透過此 ID 追蹤根因

  Action：Respond to a PowerApp or flow
    點擊「+ Add an output」，新增：
      - Number：StatusCode → 500
      - Text：Status → Failed
      - Text：ErrorCode → ERR-SYSTEM-500
      - Text：ErrorStage → CatchHandler
      - Text：Message → @{outputs('Compose-ErrorMessage')}
      - Text：RequestID → （空白）
      - Text：ProjectRowId → （空白）
      - Text：FolderLink → （空白）
      - Text：FlowRunId → @{workflow()?['run']?['name']}
      - Text：Timestamp → @{utcNow()}
```

> **注意**：同一 Flow 中只能有一個 `Respond to a PowerApp or flow` 動作會實際執行。
> 因為 Try 成功時步驟 10 回應，失敗時 Catch 中回應，兩者不會同時執行，符合限制。
> **FlowRunId 與 Timestamp 必須在成功與失敗回應中都包含**，確保 Power Apps 端無論結果均可追溯。

> **P-16 Writeback 在 GOV-001 Catch 中的特殊處理**：
> GOV-001 的 Catch 執行補償交易（刪除 Project Registry 記錄），因此不再 Writeback。
> 但 GOV-002 / GOV-005 的 Catch 不會刪除 Project Registry，因此**必須**在 Catch 中執行
> `Writeback_FlowRunId_Failed`（gov_lastflowstatus = 807660001 Failed）。

**步驟 12**：儲存
```
點擊左上角 Flow 名稱（預設顯示「Untitled」）
輸入名稱：GOV-001-CreateProject
點擊「Save」（中文：「儲存」）
```

### 驗收測試（對應 07文件）

| 測試項目 | 操作方式 | 預期結果 | 07文件對應 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|:-------------------------------|
| 未授權使用者建立專案 | 使用非 GOV-Architects 成員 Email 呼叫 Flow | 回傳 Status = Failed，Terminate ERR-001-002 | E2E-001 |
| 授權使用者建立專案 | 在 Power Apps FORM-001 點擊「提交」 | 回傳 Status = Success，RequestID 格式為 DR-YYYY-NNNN | E2E-001 Phase 1 |
| RequestID 連續性 | 連續建立兩個專案 | 序號連續遞增（如 DR-2026-0001、DR-2026-0002） | E2E-001 Phase 1 |
| Counter List 更新 | 查詢 Counter List | gov_nextseq 已遞增 | E2E-001 Phase 1 |
| Dataverse 記錄 | 查詢 Project Registry | 新增 1 筆，CurrentGate = Pending | E2E-001 Phase 1 |
| SharePoint 資料夾 | 開啟 SharePoint Design Documents | 出現專案主資料夾與 **6 個子資料夾**（01_Feasibility ~ 06_Handover） | E2E-001 Phase 1 |
| Baseline Seeding | 查詢 Document Register（ParentProject = 新專案） | 新增 **13 筆** DocumentRole = Planned 記錄 | E2E-013 |
| Review Decision Log | 查詢 Review Decision Log | 新增 1 筆 ProjectCreation 記錄 | E2E-001 Phase 1 |
| 通知發送 | 檢查 SystemArchitect Email + Teams | 收到「專案已建立」通知 | 4.3.3 |
| Power Apps 回傳 | 在 Power Apps 中檢查 varFlowResult | 包含 Status, RequestID, ProjectRowId, FolderLink, FlowRunId 五個欄位 | E2E-001 Phase 1 |

### Deprecated 做法（禁止使用）

> **以下為 v3.0 以前的舊做法，已在 v4.1 全面移除。**
> 此做法僅供學習測試，**禁止在 Production 使用**。
> 若發現現有環境仍使用以下做法，必須遷移至上述 Dataverse 驅動版本。

**Deprecated 1：硬寫 6 個 Create folder Action（已由 Step 7 取代）**

```
❌ 禁止使用 — 舊做法：在 Flow 中逐一硬寫 6 個 Create new folder 動作
   Create new folder → 01_Feasibility
   Create new folder → 02_Risk_Assessment
   Create new folder → 03_Design
   Create new folder → 04_Security
   Create new folder → 05_Test
   Create new folder → 06_Handover

✅ 正確做法：Step 7（Dataverse gov_documentfolderbaseline 驅動 + Apply to each）
   新增或移除子資料夾時，僅需修改 Dataverse 資料表，不需修改 Flow。
```

**Deprecated 2：硬寫 13 筆 DocumentType JSON 陣列（已由 Step 7.5 取代）**

```
❌ 禁止使用 — 舊做法：在 Flow 中以 Compose 建立 JSON 陣列，內含 13 筆 DocumentType 常數
   Compose-DocumentTypes → [{"type":"TechnicalFeasibility","gate":"Gate0"}, ...]

✅ 正確做法：Step 7.5（Dataverse Document Baseline Matrix 驅動 + Apply to each）
   新增或移除 DocumentType 時，僅需修改 Dataverse 資料表，不需修改 Flow。
```

---

## GOV-002：Gate Transition Request

### A. 基本資訊

| 項目 | 值 |
|:--------------------------|:--------------------------------------------------------------|
| Flow 名稱 | GOV-002 Gate Transition Request |
| 目的 | 處理 Gate 推進申請，驗證前置條件，呼叫 GOV-003 進行審批編排 |
| Trigger 類型 | **Power Apps (V2)** |
| 觸發來源 | FORM-002 Gate Request Form（Power Apps），以 `GOV002GateTransition.Run(...)` 呼叫 |
| Connection References | CR-Dataverse-SPN（MVP 模式可先用個人連線） |
| Concurrency Control | **必須開啟**（Key = `triggerBody()['ProjectId']`，Parallelism = 1） |
| 依賴 Child Flow | GOV-003（Gate Approval Orchestrator）、GOV-004（Risk Acceptance，僅 Gate3）、GOV-013B（Risk Aggregator，僅 Gate3）、GOV-015（Notification Handler） |
| 對應測試案例 | 07文件 E2E-001 Phase 2~6 |

### Step 0：GOV-002 起手式必檢 12 項

> **為什麼需要 Step 0？** Power Apps 呼叫 Flow「沒反應」或回傳 schema mismatch 是最常見的卡關原因。
> 以下 12 項必須在建 GOV-002 之前或建完之後逐一確認，有任何一項未通過就不要進入驗收。

**必檢 1：Flow 在同一環境同一 Solution**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 確保 App 能看到 Flow |
| 操作路徑 | Maker Portal → 右上角確認環境為 **DEV** → 左側「解決方案」→ 開啟你的 Solution → 確認 GOV-002 Flow 和 Canvas App 都列在 Solution 清單中 |
| 成功長相 | Solution 內同時看到 GOV-002 Flow 和 Canvas App 兩個項目 |
| 失敗長相 | Flow 不在清單中，或 Flow 在另一個 Solution |
| 下一步 | 在 Solution 內直接新建 Flow（不要在 Solution 外建再移入）；若已建在外面，刪除後在 Solution 內重建 |

**必檢 2：Flow 被 App 加入**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 確保 Power Apps 知道要呼叫哪支 Flow |
| 操作路徑 | Power Apps Studio → 左側面板 → 點擊「Power Automate」圖示（閃電符號）→ 確認 GOV-002 出現在已加入的 Flow 清單 |
| 成功長相 | 清單中看到 `GOV-002 Gate Transition Request` |
| 失敗長相 | 清單為空或找不到此 Flow |
| 下一步 | 點擊「+ 新增流程」→ 在列表選擇 GOV-002 → 若列表沒出現，點右上角「⋯」→「重新整理」（Refresh）→ 加入後必須「發佈」App |

**必檢 3：Connection Reference 已授權**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 確保 Flow 所有 Action 有可用連線 |
| 操作路徑 | 開啟 GOV-002 Flow → 逐一檢查每個 Dataverse Action 右上角是否有 ⚠️ 標記 → 若有則點擊 → 選擇已授權的連線 |
| 成功長相 | 所有 Action 右上角無 ⚠️ 標記，連線顯示為已連線（綠色勾勾） |
| 失敗長相 | 某個 Action 右上角有 ⚠️ 或紅色警告 |
| 下一步 | 點擊該 Action → 「變更連線」→ 選擇 CR-Dataverse-SPN（MVP 模式選個人帳號）→ 授權 → Save |

**必檢 4：Trigger 是 Power Apps (V2)**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 舊版 Trigger 不支援 Respond 回傳，必須用 V2 |
| 操作路徑 | 開啟 GOV-002 Flow → 檢查第一個 Trigger 卡片標題 |
| 成功長相 | 標題顯示「**Power Apps (V2)**」，有 V2 字樣 |
| 失敗長相 | 標題顯示「Power Apps」但無 V2 |
| 下一步 | 刪除此 Trigger → 重新搜尋 `power apps` → 選擇有 **(V2)** 的版本 → 重新加入所有 Input 參數 |

**必檢 5：Flow 狀態是 On**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | Flow 關閉時 App 呼叫會靜默失敗 |
| 操作路徑 | Maker Portal → 解決方案 → 開啟 GOV-002 Flow → 看上方狀態列 |
| 成功長相 | 狀態列顯示「**開啟**」（On） |
| 失敗長相 | 狀態列顯示「關閉」（Off） |
| 下一步 | 點擊右上角「開啟」按鈕 |

**必檢 6：Flow 名稱改過後重新加入 App**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 改名後 App 中的舊引用會失效 |
| 操作路徑 | 確認 Flow 名稱與 App 中的引用名稱一致 → Power Apps Studio → 左側 Power Automate 面板 → 確認 Flow 名稱無驚嘆號 |
| 成功長相 | Flow 名稱旁無警告圖示，PowerFx 中的 `GOV002GateTransition` 無紅色底線 |
| 失敗長相 | 名稱旁有 ⚠️，或 PowerFx 公式出現紅色底線「找不到 Flow」 |
| 下一步 | App 中移除舊 Flow → 重新加入更名後的 Flow → 更新 PowerFx 中的 Flow 名稱 → 重新發佈 App |

**必檢 7：Respond 動作位置與 Scope 正確**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | Respond 放錯位置會導致「多個 Respond 同時執行」錯誤 |
| 操作路徑 | 開啟 GOV-002 Flow → 確認所有 `Respond to a PowerApp or flow` 動作都在 Scope 內部 → 成功 Respond 在 `Try-MainLogic` 的最末端 → 失敗 Respond 在 `Catch-ErrorHandler` 內 → 中途 Pre-check 失敗的 Respond 後面緊跟 Terminate |
| 成功長相 | Flow 執行時只有一個 Respond 被執行（Try 成功 XOR Catch 失敗） |
| 失敗長相 | 執行時報錯「A 'Respond' action has already been executed」 |
| 下一步 | 確認每個 Pre-check 失敗的 Respond 後面都有 Terminate（搜尋 `terminate`）→ 確認 Catch Scope 的 Configure run after 不含「成功」 |

**必檢 8：Run History 有記錄**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 確認 App 端確實有送出呼叫到 Flow |
| 操作路徑 | 從 App 點一次提交按鈕 → Maker Portal → 解決方案 → 開啟 GOV-002 → 左側「28 天執行歷程記錄」（28-day run history） |
| 成功長相 | 看到一筆新的 Run 記錄（時間為剛剛） |
| 失敗長相 | 28 天歷程記錄完全沒有新記錄 |
| 下一步 | 依照文件開頭「必檢 7 排查流程圖」逐步排查：環境 → Solution → App 加入 → Flow 狀態 → 連線 |

**必檢 9：Concurrency Control 已開啟（Parallelism = 1）**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 避免同一專案同時有兩筆 Gate 申請造成資料衝突 |
| 操作路徑 | 開啟 GOV-002 Flow → 點擊 Trigger → 右上角「...」→「設定」→ 找到「並行控制」區段 |
| 成功長相 | 並行控制開關為「開啟」，「平行處理原則程度」顯示 `1` |
| 失敗長相 | 開關為關閉，或程度不是 1 |
| 下一步 | 開關切換為「開啟」→ 程度設為 `1` → 點擊「完成」 |

**必檢 10：所有 Respond 的欄位集合完全一致**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 成功（200）與失敗（400/500）的 Respond schema 不一致時，Power Automate 會報 schema mismatch 錯誤 |
| 操作路徑 | 開啟 GOV-002 Flow → 找到所有 `Respond to a PowerApp or flow` 動作 → 逐一確認每個 Respond 都包含以下 8 個欄位：StatusCode、Status、ErrorCode、ErrorStage、Message、ReviewRowId、FlowRunId、Timestamp |
| 成功長相 | 每個 Respond（不論 200 / 400 / 500）都有完全相同的 8 個欄位，失敗時 ReviewRowId 填空白字串 |
| 失敗長相 | 成功 Respond 有 ReviewRowId 但某個失敗 Respond 沒有 → 報錯「status code 200 schema must match」 |
| 下一步 | 在所有失敗 Respond 中補上缺少的欄位，值填空白字串 `""` |

**必檢 11：Catch Scope 的 Configure run after 正確**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | Catch 必須在 Try 失敗時才執行 |
| 操作路徑 | 點擊 `Catch-ErrorHandler` Scope 右上角「...」→「設定在之後執行」（Configure run after） |
| 成功長相 | 「成功」未勾選，「已失敗」與「已逾時」已勾選 |
| 失敗長相 | 「成功」被勾選 → Catch 和 Try 同時執行 → 雙重 Respond 報錯 |
| 下一步 | 取消勾選「成功」→ 勾選「已失敗」與「已逾時」→ 點擊「完成」 |

**必檢 12：所有 Input 參數型別皆為 Text**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | Power Apps 呼叫 Flow 時如果型別不匹配會靜默失敗 |
| 操作路徑 | 開啟 GOV-002 Flow → 點擊 Trigger → 檢查每個 Input 參數的類型 |
| 成功長相 | ProjectId = Text、RequestedGate = Text、SubmittedByEmail = Text、Comments = Text |
| 失敗長相 | 有參數使用 Number 或 Yes/No 類型 |
| 下一步 | 刪除錯誤類型的參數 → 重新以 Text 類型加入 → Save |

### B. 先決條件清單

開始建置 GOV-002 之前，以下項目必須已完成：

| 先決條件 | 如何確認 |
|:--------------------------------------|:----------------------------------------------|
| Dataverse 資料表 `Project Registry` 已建立且包含所有必要欄位 | Maker Portal → Dataverse → 資料表 → 確認 Project Registry 存在 |
| Dataverse 資料表 `Review Decision Log` 已建立 | 同上確認 Review Decision Log 存在 |
| GOV-015（Notification Handler）已建立並測試通過 | Flow 列表中 GOV-015 狀態為 On |
| GOV-003（Gate Approval Orchestrator）已建立並測試通過 | Flow 列表中 GOV-003 狀態為 On |
| GOV-013B（Risk Aggregator）已建立（僅 Gate3 需要） | Flow 列表中 GOV-013B 狀態為 On |
| GOV-004（Risk Acceptance）已建立（僅 Gate3 需要） | Flow 列表中 GOV-004 狀態為 On |
| Connection Reference 已建立並授權 | 解決方案 → Connection References → CR-Dataverse-SPN 狀態為「已連線」 |
| Canvas App（FORM-002）已存在於同一 Solution | 解決方案 → 確認 App 在清單中 |

### C. Input Schema（Power Apps (V2) Trigger 參數）

在 Trigger 中以「+ Add an input」逐一新增以下參數，**全部使用 Text 類型**：

| 參數名稱 | Input 類型 | 必填 | 說明 |
|:--------------------------|:----------------------|:------:|:----------------------------------------------|
| ProjectId | **Text** | ✓ | **Dataverse 的 gov_projectregistryid（GUID 字串）**，非整數。Power Apps 以 `Text(ThisItem.gov_projectregistryid)` 取得 |
| RequestedGate | **Text** | ✓ | `Gate0` / `Gate1` / `Gate2` / `Gate3`（純文字，非 OptionSet 值） |
| SubmittedByEmail | **Text** | ✓ | 提交者 Email，如 `user@company.com` |
| Comments | **Text** | ✗ | 備註（可空白） |
| ReworkReasonCategory | **Text** | ✗ | Rework 原因分類 OptionSet Value（僅 Rework 時需填，選填） |

> **重要：ProjectId 為 GUID 字串（Text），不是 integer。**
> Dataverse 的主鍵 `gov_projectregistryid` 為 GUID 格式（如 `a1b2c3d4-e5f6-7890-abcd-ef1234567890`）。
> Power Apps 端取得方式：`Text(BrowseGallery.Selected.gov_projectregistryid)`
> Flow 端使用方式：直接作為 `Get a row by ID` 的 Row ID 參數

### D. Output Schema（Canonical Error Envelope v5.0 — 成功與失敗 Schema 完全一致）

> **關鍵規則：所有 Respond 動作（200 / 400 / 500）必須回傳完全相同的 8 個欄位。**
> 若成功時多了一個欄位，或失敗時少了一個欄位，Power Automate 會報 `status code 200 schema must match` 錯誤。

| 輸出參數 | 類型 | 200 成功時的值 | 400 業務失敗時的值 | 500 系統例外時的值 |
|:----------------------------------------------|:----------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| StatusCode | Number | `200` | `400` | `500` |
| Status | Text | `Success` | `Failed` | `Failed` |
| ErrorCode | Text | `""` (空白字串) | `ERR-002-xxx` | `ERR-SYSTEM-500` |
| ErrorStage | Text | `""` (空白字串) | `PreCheck` | `CatchHandler` |
| Message | Text | `Gate 申請已提交` | 具體錯誤訊息 | `@{outputs('Compose-ErrorMessage')}` |
| ReviewRowId | Text | `{Review Decision Log GUID}` | `""` (空白字串) | `""` (空白字串) |
| FlowRunId | Text | `@{workflow()?['run']?['name']}` | `@{workflow()?['run']?['name']}` | `@{workflow()?['run']?['name']}` |
| Timestamp | Text | `@{utcNow()}` | `@{utcNow()}` | `@{utcNow()}` |

> **踩雷點**：失敗 Respond 中如果省略 ReviewRowId 欄位（而非填空白字串），Power Automate 會認為 schema 不一致而報錯。
> 必須在失敗 Respond 中明確加入 `ReviewRowId: ""`。

### Pre-check 清單與錯誤代碼

| Pre-check | 條件 | ErrorCode | 說明 |
|:----------------------------------------------|:----------------------------------------------|:-------------------------------|:----------------------------------------------|
| 1. 專案存在 | ProjectId 存在於 Project Registry | ERR-002-001 | 專案不存在 |
| 2. 提交者權限 | SubmittedByEmail = Project.SystemArchitect | ERR-002-003 | 僅專案 System Architect 可提交 Gate 申請 |
| 3. 專案狀態 | ProjectStatus = Active（807660000） | ERR-002-005/006/007/008 | 非 Active 狀態不允許提交申請（OnHold→006，Closed→007，Terminated→008，未知→005） |
| 4. 無進行中申請 | RequestStatus = None（807660000） | ERR-002-058 | 專案有進行中的 Gate 申請 |
| 5. CurrentGate 前置條件 | 依 RequestedGate 驗證（見下表） | ERR-002-020~053 | Gate 前置條件不滿足 |
| 6. 必要文件齊全 | 依 RequestedGate 驗證文件連結 | ERR-002-021~057 | 必要文件未上傳 |

### Gate 前置條件驗證

| RequestedGate | 必須滿足的 CurrentGate | ErrorCode |
|:----------------------------------------------|:----------------------------------------------|:-------------------------------|
| Gate0 | Pending（807660000） | ERR-002-020 |
| Gate1 | Gate0（807660001） | ERR-002-040 |
| Gate2 | Gate1（807660002）或 Gate2（807660003）；重送時額外需 reworkcount > 0 + requeststatus = None | ERR-002-050；重送路徑驗證失敗 → ERR-002-010 |
| Gate3 | Gate2（807660003） | ERR-002-053 |

### Gate 必要文件（OData Filter 欄位名稱）

**Gate 0**：
```
gov_technicalfeasibilitylink is not null AND
gov_initialrisklistlink is not null AND
gov_riskassessmentstrategylink is not null
```

**Gate 1**：
```
gov_designbaselinelink is not null AND
gov_riskassessmentlink is not null AND
gov_iec62443checklistlink is not null AND
gov_requirementtraceabilitylink is not null AND
gov_documentregisterlink is not null AND
gov_designobjectinventorylink is not null
```

**Gate 2**：
```
gov_changeimpactlink is not null
```

**Gate 3**：
```
gov_residualrisklink is not null AND
gov_handovermeetinglink is not null
```

### E. 建立步驟（逐步點擊）

> 以下從「Create Flow」開始，到「Save」結束。每步都寫出搜尋關鍵字與 UI 位置。

**步驟 1：建立 Flow + Power Apps (V2) Trigger**

```
1. Maker Portal → 左側「解決方案」→ 開啟你的 Solution
2. 上方「+ 新增」→「自動化」→「雲端流程」→「自動化」
   （英文路徑：+ New → Automation → Cloud flow → Automated）
3. 跳出建立畫面後，在搜尋列輸入 power apps
4. 選擇「Power Apps (V2)」（注意：必須選有 V2 的版本）
5. 點擊「建立」
6. 點擊 Flow 名稱（左上角），改為「GOV-002 Gate Transition Request」
7. 在 Trigger 卡片中，點擊「+ Add an input」逐一新增參數：
   → 選擇 Text → 輸入名稱 ProjectId
   → 選擇 Text → 輸入名稱 RequestedGate
   → 選擇 Text → 輸入名稱 SubmittedByEmail
   → 選擇 Text → 輸入名稱 Comments
```

**步驟 2：開啟 Concurrency Control**

```
1. 點擊 Trigger 卡片右上角「...」
2. 選擇「設定」（Settings）
3. 找到「並行控制」（Concurrency Control）區段
4. 將開關切換為「開啟」（On）
5. 「平行處理原則程度」（Degree of Parallelism）設為 1
6. 點擊「完成」（Done）
```

**步驟 3：Initialize variable**

```
Action: + 新增步驟 → 搜尋 initialize variable → 選擇「變數」下的「Initialize variable」
  （中文：「初始化變數」）
  Name：varProjectId
  Type：String（字串）
  Value：點擊欄位 → 動態內容 → 選擇「ProjectId」（來自 Trigger）
```

**步驟 4：建立 Try-MainLogic Scope**

```
Action: + 新增步驟 → 搜尋 scope → 選擇「控制項」下的「Scope」
  （中文可能為「範圍」）
  點擊 Scope 標題 → 重新命名為「Try-MainLogic」
```

> 以下步驟 5 ~ 步驟 14 都在 Try-MainLogic 內部建立。

**步驟 5：Get Project（在 Try-MainLogic 內部）**

```
在 Try-MainLogic 內部，點擊「+ 新增步驟」
  → 搜尋 get a row → 選擇「Microsoft Dataverse」下的「Get a row by ID」
  （中文：「依識別碼取得資料列」）
  連線：選擇 CR-Dataverse-SPN（MVP 模式：選個人帳號的 Dataverse 連線）
  Table name：Project Registry（下拉選擇，或搜尋 project）
  Row ID：點擊欄位 → 切換到「運算式」(Expression) → 輸入：
    variables('varProjectId')
  點擊「確定」
  重新命名此 Action 為「Get_Project」
```

**步驟 6：Pre-check 1 — 專案存在**

```
如果 Get_Project 這個 Action 失敗（表示 ProjectId 查無記錄），Flow 會直接進入 Catch。
因此不需要額外的 Condition。Get a row by ID 查不到時會拋出 404 錯誤，Catch 會捕獲。
```

**步驟 7：Pre-check 2 — 提交者權限**

```
在 Get_Project 下方，+ 新增步驟 → 搜尋 condition → 選擇「控制項」下的「Condition」
  （中文：「條件」）
  重新命名為「PreCheck_SubmitterAuth」
  條件設定：
    左側：點擊欄位 → 動態內容 → 選擇「SubmittedByEmail」（來自 Trigger）
    運算子：is equal to（等於）
    右側：點擊欄位 → 運算式 → 輸入：
      outputs('Get_Project')?['body/gov_systemarchitect']
    點擊「確定」

  False 分支（提交者非 System Architect）：
    + 新增步驟 → 搜尋 respond → 選擇「Respond to a PowerApp or flow」
    （中文：「回應 PowerApp 或流程」）
    逐一加入輸出欄位（點擊「+ Add an output」）：
      Number → StatusCode → 400
      Text → Status → Failed
      Text → ErrorCode → ERR-002-003
      Text → ErrorStage → PreCheck
      Text → Message → 僅專案 System Architect 可提交 Gate 申請
      Text → ReviewRowId → （空白，直接留空）
      Text → FlowRunId → 運算式：workflow()?['run']?['name']
      Text → Timestamp → 運算式：utcNow()

    + 新增步驟 → 搜尋 terminate → 選擇「控制項」下的「Terminate」
    （中文：「終止」）
    Status：Cancelled（取消）

  True 分支（通過）：不放任何 Action，繼續往下
```

> **⚠ 每個 Pre-check 失敗的 Respond 必須包含完整 8 個欄位（含 ReviewRowId 空白字串），且 Respond 後面必須接 Terminate。**

**步驟 8：Pre-check 3 — 專案狀態 Active**

```
在 PreCheck_SubmitterAuth 的 True 分支後方（或在 Condition 外部的下一步）：
  + 新增步驟 → Condition
  重新命名為「PreCheck_ProjectActive」
  條件：
    左側：運算式 → outputs('Get_Project')?['body/gov_projectstatus']
    運算子：is equal to
    右側：807660000（Active）

  False 分支（非 Active 狀態 — 使用 Switch 區分不同非法狀態）：
    + 新增步驟 → Switch
    重新命名為「Switch_ProjectStatusError」
    On：運算式 → outputs('Get_Project')?['body/gov_projectstatus']

    Pre-check 3 更新後邏輯：

    Switch gov_projectstatus：
      Case 807660001（OnHold）：
        → Respond 400, ERR-002-006, "專案目前暫停（OnHold）— 請聯繫 PM 恢復後再提交"
      Case 807660002（Closed）：
        → Respond 400, ERR-002-007, "專案已結案（Closed）— 無法提交 Gate 申請"
      Case 807660003（Terminated）：
        → Respond 400, ERR-002-008, "專案已終止（Terminated）— 無法提交 Gate 申請"
      Default（非 807660000 Active 的其他值）：
        → Respond 400, ERR-002-005, "專案狀態不允許（未知狀態）"
    + Terminate（Cancelled）

  True 分支：繼續
```

**步驟 9：Pre-check 4 — 無進行中申請**

```
+ 新增步驟 → Condition
  重新命名為「PreCheck_NoPendingRequest」
  條件：
    左側：運算式 → outputs('Get_Project')?['body/gov_requeststatus']
    運算子：is equal to
    右側：807660000（None）

  False 分支：
    Respond → StatusCode: 400, Status: Failed, ErrorCode: ERR-002-058,
    ErrorStage: PreCheck, Message: 專案有進行中的 Gate 申請，
    ReviewRowId: "", FlowRunId: workflow()?['run']?['name'], Timestamp: utcNow()
    + Terminate（Cancelled）

  True 分支：繼續
```

**步驟 10：Switch — Gate 前置條件與文件驗證**

```
+ 新增步驟 → 搜尋 switch → 選擇「控制項」下的「Switch」
  （中文可能為「切換」）
  On：點擊欄位 → 動態內容 → 選擇「RequestedGate」（來自 Trigger）

  Case Gate0：
    Condition：CurrentGate = 807660000（Pending）→ 否則 Respond 400 ERR-002-020 + Terminate
    Condition：gov_technicalfeasibilitylink is not null AND gov_initialrisklistlink is not null AND gov_riskassessmentstrategylink is not null
    → 否則 Respond 400 ERR-002-021 + Terminate

  Case Gate1：
    Condition：CurrentGate = 807660001（Gate0）→ 否則 Respond 400 ERR-002-040 + Terminate
    Condition：6 個文件欄位皆 not null → 否則 Respond 400 ERR-002-041 + Terminate

  Case Gate2：
    Condition：CurrentGate = 807660002（Gate1）OR 807660003（Gate2）
    → 否則 Respond 400 ERR-002-050 + Terminate
    ✅ [已修正 BUG-016] 當 CurrentGate = 807660003（Gate2 重送路徑），額外驗證 Rework 上下文：
    Condition：Is_Gate2Rework（僅在 CurrentGate = 807660003 時觸發）
      條件：greater(outputs('Get_Project')?['body/gov_reworkcount'], 0)
            AND equals(outputs('Get_Project')?['body/gov_requeststatus'], 807660000)
      （gov_reworkcount > 0 = 曾觸發 Rework；gov_requeststatus = None = 前次申請已清除）
      False 分支（無有效 Rework 事件）：
        Respond to a PowerApp or flow
          StatusCode：400
          Status：Failed
          ErrorCode：ERR-002-010
          ErrorStage：PreCheck
          ErrorMessage：Gate2 重送必須在有效的 Rework 事件後才能提交。
                        目前 gov_reworkcount = 0 或 gov_requeststatus 非 None，
                        無法確認此次提交源自正式 Rework 流程。
          ReviewRowId：""
          FlowRunId：workflow()?['run']?['name']
          Timestamp：utcNow()
        + Terminate（Cancelled）
      True 分支：繼續（Rework 上下文有效，允許 Gate2 重送審查）

    > 實作說明：在 Switch Case Gate2 的 Condition（CurrentGate 通過）後，
    > 增加「If CurrentGate equals 807660003」內部 Condition，名為 Is_Gate2Rework。
    > 此 Condition 僅在 CurrentGate = 807660003 路徑上執行；
    > 若 CurrentGate = 807660002（Gate1 → Gate2 首次），直接跳過此 Condition。
    > 在 Power Automate 中以 Condition 的「僅在 True 時執行後續步驟」邏輯實作：
    >   外層 Condition（CurrentGate OR）通過後，
    >   加入 Condition：equals(outputs('Get_Project')?['body/gov_currentgate'], 807660003)
    >   True 分支：再加入 Is_Gate2Rework Condition（reworkcount > 0 AND requeststatus = 0）
    >   False 分支（currentgate = 807660002）：直接通過

    Condition：gov_changeimpactlink is not null → 否則 Respond 400 ERR-002-051 + Terminate

  Case Gate3：
    Condition：CurrentGate = 807660003（Gate2）→ 否則 Respond 400 ERR-002-053 + Terminate
    Condition：gov_residualrisklink is not null AND gov_handovermeetinglink is not null
    → 否則 Respond 400 ERR-002-057 + Terminate

  ⚠ 每個失敗 Respond 都必須帶完整 8 個欄位（含 ReviewRowId: ""）
```

**步驟 10.5-A：Pre-check — 必要文件已上傳（無 Planned 狀態遺留）**

```
✅ [已修正 BUG-009] Gate 審批前必須確認此 Gate 的所有必要文件已上傳（非 Planned 狀態）

+ 新增步驟 → 搜尋 list rows → 選擇「Microsoft Dataverse」下的「List rows」
  重新命名為「Check_PlannedDocs」
  Table name：Document Register
  Filter rows：_gov_parentproject_value eq '@{variables('varProjectId')}'
              and gov_requiredforgate eq '@{triggerBody()?['RequestedGate']}'
              and gov_documentrole eq 807660000
              （807660000 = Planned：代表已列入清冊但從未上傳）
  Row count：1

+ 新增步驟 → Condition
  重新命名為「PreCheck_NoPlannedRequired」
  條件：length(outputs('Check_PlannedDocs')?['body/value']) is equal to 0
  （0 筆 = 沒有仍在 Planned 的必要文件 = 全部已上傳 = 可繼續）

  False 分支（仍有未上傳的必要文件）：
    Respond to a PowerApp or flow
      StatusCode：400
      Status：Failed
      ErrorCode：ERR-002-009
      ErrorStage：PreCheck
      ErrorMessage：此 Gate 仍有必要文件尚未上傳（狀態仍為 Planned）。
                    請先完成所有必要文件上傳後再提交 Gate 申請。
      ReviewRowId：""
      FlowRunId：workflow()?['run']?['name']
      Timestamp：utcNow()
    + Terminate（Cancelled）

  True 分支：繼續
```

**步驟 10.5-B：解析 RequestedGate → OptionSet 整數值**

```
✅ [已修正 BUG-007] 新增 Compose 步驟，將 RequestedGate 文字轉換為 gov_requestedgate OptionSet 整數

+ 新增步驟 → Compose
  重新命名為「Compose-RequestedGateOptionSet」
  Inputs：運算式 →
  if(equals(triggerBody()?['RequestedGate'], 'Gate0'), 807660001,
  if(equals(triggerBody()?['RequestedGate'], 'Gate1'), 807660002,
  if(equals(triggerBody()?['RequestedGate'], 'Gate2'), 807660003,
  if(equals(triggerBody()?['RequestedGate'], 'Gate3'), 807660004,
  807660000))))

  對照表：Gate0=807660001, Gate1=807660002, Gate2=807660003, Gate3=807660004
  （807660000 為預設值，代表輸入錯誤——應由 Pre-check 在更早時阻擋）

> **設計說明**：P-13 禁止在業務邏輯中硬編碼，但 RequestedGate 是 Trigger 輸入參數（固定 4 個值）。
> 使用 nested if() 屬於「輸入參數標準化」，是唯一需要維護此映射的地方。
```

**步驟 11：新增 Review Decision Log 記錄**

```
+ 新增步驟 → 搜尋 add a new row → 選擇「Microsoft Dataverse」下的「Add a new row」
  （中文：「新增資料列」）
  Table name：Review Decision Log
  欄位對應：
    gov_parentproject：@{variables('varProjectId')}（Lookup → 點擊進階 → 貼上 GUID）
    gov_requestedgate：outputs('Compose-RequestedGateOptionSet')（✅ 使用上方 Compose 結果）
    gov_decision：807660000（Pending）
    gov_submittedby：@{triggerBody()['SubmittedByEmail']}
    gov_comments：@{triggerBody()['Comments']}
    gov_triggerflowrunid：運算式 → workflow()?['run']?['name']
  重新命名為「Create_ReviewDecisionLog」
```

**步驟 12：更新 Project Registry（RequestStatus = Pending）**

```
+ 新增步驟 → 搜尋 update a row → 選擇「Microsoft Dataverse」下的「Update a row」
  （中文：「更新資料列」）
  Table name：Project Registry
  Row ID：@{variables('varProjectId')}
  欄位對應：
    gov_requeststatus：807660001（Pending）
```

**步驟 13：Gate3 特殊處理 + 呼叫 GOV-003**

```
+ 新增步驟 → Condition
  重新命名為「Is_Gate3」
  條件：RequestedGate is equal to Gate3

  True 分支（Gate3）：
    a. Run a Child Flow → 搜尋 child flow → 選擇 GOV-013B Risk Aggregator
       Input：ProjectId = @{variables('varProjectId')}
    b. Update a row → Project Registry → gov_highestresidualrisklevel = GOV-013B 回傳值
    c. Run a Child Flow → GOV-004 Risk Acceptance
    d. Condition：GOV-004 回傳 Status = Success AND RiskAcceptanceStatus = Accepted?
       True：Run a Child Flow → GOV-003 Gate Approval Orchestrator
       False：Update a row → Project Registry → gov_requeststatus = 807660000（None）
              → Respond 400, ERR-002-RISK, PreCheck, 風險未被接受，Gate3 申請取消,
                ReviewRowId: "", FlowRunId, Timestamp + Terminate

  False 分支（非 Gate3）：
    Run a Child Flow → GOV-003 Gate Approval Orchestrator
```

**步驟 14：FlowRunId Writeback（成功）+ 成功 Respond**

```
（P-16 原則）
+ 新增步驟 → Update a row → Project Registry
  Row ID：@{variables('varProjectId')}
  gov_lastflowrunid：運算式 → workflow()?['run']?['name']
  gov_lastflowstatus：807660000（Success）

+ 新增步驟 → Respond to a PowerApp or flow
  （搜尋 respond → 選擇「Respond to a PowerApp or flow」）
  逐一加入輸出欄位：
    Number → StatusCode → 200
    Text → Status → Success
    Text → ErrorCode → （空白）
    Text → ErrorStage → （空白）
    Text → Message → Gate 申請已提交
    Text → ReviewRowId → 運算式：outputs('Create_ReviewDecisionLog')?['body/gov_reviewdecisionlogid']
    Text → FlowRunId → 運算式：workflow()?['run']?['name']
    Text → Timestamp → 運算式：utcNow()
```

> 步驟 14 是 Try-MainLogic 的最後一步。以下建立 Catch Scope。

**步驟 15：建立 Catch-ErrorHandler Scope**

```
在 Try-MainLogic Scope 下方（不是內部）：
  + 新增步驟 → 搜尋 scope → 選擇 Scope → 重新命名為「Catch-ErrorHandler」

  設定 Configure run after：
    點擊 Catch-ErrorHandler 右上角「...」→「設定在之後執行」（Configure run after）
    → 取消勾選「成功」
    → 勾選「已失敗」與「已逾時」
    → 點擊「完成」
```

**步驟 16：Catch 內部 — ErrorMessage + Writeback + Respond**

```
在 Catch-ErrorHandler 內部：

a. + 新增步驟 → 搜尋 compose → 選擇「資料作業」下的「Compose」
   （中文可能為「撰寫」）
   重新命名為「Compose-ErrorMessage」
   Inputs：切換到「運算式」→ 輸入：
     coalesce(result('Try-MainLogic')?[0]?['error']?['message'], '未知錯誤')
   點擊「確定」

b. + 新增步驟 → Update a row → Project Registry（P-16 原則）
   Row ID：@{variables('varProjectId')}
   gov_lastflowrunid：運算式 → workflow()?['run']?['name']
   gov_lastflowstatus：807660001（Failed）

c. + 新增步驟 → Respond to a PowerApp or flow
   逐一加入輸出欄位：
     Number → StatusCode → 500
     Text → Status → Failed
     Text → ErrorCode → ERR-SYSTEM-500
     Text → ErrorStage → CatchHandler
     Text → Message → 點擊欄位 → 動態內容 → 選擇「Compose-ErrorMessage」的 Outputs
     Text → ReviewRowId → （空白字串）
     Text → FlowRunId → 運算式：workflow()?['run']?['name']
     Text → Timestamp → 運算式：utcNow()
```

**步驟 17：Save**

```
點擊右上角「儲存」（Save）→ 等待儲存完成
若出現驗證錯誤，根據錯誤訊息逐一修正 → 重新儲存
```

### F. 必做設定檢核點

建完 Flow 後，逐項確認以下設定：

| 檢核項目 | 確認方式 | 預期結果 |
|:----------------------------------------------|:----------------------------------------------|:-------------------------------|
| Concurrency Control | Trigger → 設定 → 並行控制 | 開啟，程度 = 1 |
| Trigger 類型 | Trigger 卡片標題 | Power Apps (V2) |
| Connection Reference | 每個 Dataverse Action 右上角 | 無 ⚠️ 標記 |
| Input 參數數量與類型 | Trigger → 4 個參數 | ProjectId(Text), RequestedGate(Text), SubmittedByEmail(Text), Comments(Text) |
| Respond 欄位一致性 | 逐一開啟每個 Respond Action | 所有 Respond 都有完整 8 個欄位 |
| Catch Configure run after | Catch Scope → 設定在之後執行 | 成功未勾選，已失敗 + 已逾時已勾選 |
| Pre-check Terminate | 每個失敗 Respond 後方 | 都有 Terminate（Cancelled） |
| Flow 名稱 | Flow 左上角 | `GOV-002 Gate Transition Request`（無特殊字元） |
| Flow 狀態 | Flow 頁面上方 | On（開啟） |

### K. Power Apps 端呼叫範本（PowerFx）

**GOV-002 呼叫參數清單**（全部為 Text）：

| 參數順序 | 參數名稱 | Power Apps 端取值方式 | 說明 |
|:----------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| 1 | ProjectId | `Text(varSelectedProject.gov_projectregistryid)` | GUID 字串 |
| 2 | RequestedGate | `ddRequestedGate.Selected.Value` | Gate0/Gate1/Gate2/Gate3 |
| 3 | SubmittedByEmail | `User().Email` | 當前使用者 Email |
| 4 | Comments | `txtComments.Text` | 備註文字 |

**可直接貼到 FORM-002 提交按鈕 OnSelect 的 PowerFx 範本**：

```
// ===== GOV-002 Gate Transition 呼叫範本 =====
// 將以下代碼貼到 FORM-002 提交按鈕的 OnSelect 屬性

// 1. 顯示載入中 + 防止重複點擊
UpdateContext({varBusy: true});
Notify("正在提交 Gate 申請...", NotificationType.Information);

// 2. 呼叫 Flow + 錯誤攔截
IfError(
    Set(
        varFlowResult,
        GOV002GateTransition.Run(
            Text(varSelectedProject.gov_projectregistryid),  // ProjectId (GUID → Text)
            ddRequestedGate.Selected.Value,                   // RequestedGate
            User().Email,                                     // SubmittedByEmail
            txtComments.Text                                  // Comments
        )
    ),
    // Flow 觸發本身失敗（連線斷線、Flow 關閉等）
    Notify("Flow 觸發失敗，請檢查連線與 Flow 狀態", NotificationType.Error);
    UpdateContext({varBusy: false});
);

// 3. 關閉載入狀態
UpdateContext({varBusy: false});

// 4. 判斷回傳狀態（必須顯示 Message 與 ErrorCode）
If(
    IsBlank(varFlowResult) || IsEmpty(varFlowResult),
    Notify("未收到 Flow 回傳，請檢查 Flow Run History", NotificationType.Error),

    varFlowResult.Status = "Success",
    Notify(
        "Gate 申請已提交，審批追蹤 ID：" & varFlowResult.ReviewRowId,
        NotificationType.Success
    ),

    // Status = Failed → 必須顯示 Message 與 ErrorCode
    Notify(
        varFlowResult.Message & " [" & varFlowResult.ErrorCode & "]",
        NotificationType.Error
    )
);
```

> **必做**：提交按鈕的 `DisplayMode` 屬性設定 `If(varBusy, DisplayMode.Disabled, DisplayMode.Edit)` 防止重複點擊。

### G. 最小驗證流程

完成建置後，按以下順序驗證：

**第 1 步：從 Power Apps 點一次提交按鈕**

```
1. 在 Power Apps Studio 中開啟 FORM-002（預覽模式或已發佈 App）
2. 選擇一個狀態為 Active 的測試專案
3. 選擇 RequestedGate = Gate0（最簡單的測試路徑）
4. 點擊「提交」按鈕
5. 觀察畫面是否出現 Notify 訊息
```

**第 2 步：去哪裡看 Flow Run History**

```
1. Maker Portal → 左側「解決方案」→ 開啟你的 Solution
2. 找到「GOV-002 Gate Transition Request」→ 點擊開啟
3. 左側面板「28 天執行歷程記錄」（28-day run history）
4. 找到最新的一筆 Run 記錄 → 點擊開啟
```

**第 3 步：成功時 Run History 預期看到的畫面**

```
所有 Action 都是綠色勾勾（✓），具體順序：
  ✓ Power Apps (V2) Trigger
  ✓ Initialize variable (varProjectId)
  ✓ Scope: Try-MainLogic
    ✓ Get_Project
    ✓ PreCheck_SubmitterAuth → True
    ✓ PreCheck_ProjectActive → True
    ✓ PreCheck_NoPendingRequest → True
    ✓ Switch (RequestedGate)
      ✓ Case Gate0 → 條件通過 + 文件通過
    ✓ Create_ReviewDecisionLog
    ✓ Update Project Registry (RequestStatus = Pending)
    ✓ Is_Gate3 → False
      ✓ Run GOV-003
    ✓ FlowRunId Writeback (Success)
    ✓ Respond (200 Success)
  ⊘ Scope: Catch-ErrorHandler（灰色跳過 = 正常）
```

**第 4 步：失敗時分類排查**

| Run History 畫面 | 分類 | 排查方式 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| Try-MainLogic 內某個 PreCheck Condition 走到 False → Respond 400 → Terminate | **PreCheck 400（業務驗證失敗）** | 展開失敗的 Respond Action → 看 ErrorCode 與 Message → 根據錯誤代碼修正測試資料（如專案狀態不對、提交者不對、文件未上傳） |
| Try-MainLogic 整體失敗（紅色 ✗）→ Catch-ErrorHandler 執行 → Respond 500 | **Catch 500（系統例外）** | 展開 Catch 內的 Compose-ErrorMessage → 看錯誤訊息 → 常見原因：連線過期、GUID 格式錯、Child Flow 不存在 |
| Trigger 本身就失敗 | **Trigger 失敗** | 檢查 Step 0 必檢清單：連線、環境、Solution、Flow 狀態 |
| Run History 完全沒有記錄 | **App 端未送出** | 依文件開頭「必檢 7 排查流程圖」逐步排查 |

### H. 常見失敗原因與對應排查路徑

| 編號 | 失敗現象 | 根因 | 排查路徑 |
|:----------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| H1 | App 點按鈕後無任何反應，Flow Run History 無記錄 | Flow 未加入 App / Flow 關閉 / 環境不一致 | Step 0 必檢 1~6、8 |
| H2 | Run History 顯示 `status code 200 schema must match` | 成功與失敗 Respond 的欄位集合不一致 | Step 0 必檢 10 → 確認所有 Respond 都有完整 8 個欄位 |
| H3 | ErrorCode = ERR-002-001，Message = 專案不存在 | ProjectId 傳入的值不是有效 GUID | 確認 Power Apps 端使用 `Text(varSelectedProject.gov_projectregistryid)` 而非 `varSelectedProject.gov_requestid` |
| H4 | ErrorCode = ERR-002-003，Message = 非授權提交者 | 當前使用者不是該專案的 System Architect | 確認 Project Registry 中 gov_systemarchitect 欄位值與 User().Email 一致 |
| H5 | ErrorCode = ERR-002-058，Message = 有進行中申請 | 之前的 Gate 申請尚未完成（RequestStatus 不是 None） | 等前一個審批完成，或手動將 RequestStatus 改回 None（僅 DEV 環境） |
| H6 | Catch 500，ErrorMessage = `The requested record was not found` | Get_Project 查不到 ProjectId | 確認 GUID 格式正確，確認 Project Registry 資料表中確實有該記錄 |
| H7 | Catch 500，ErrorMessage = `Child flow failed` | GOV-003 或 GOV-013B 或 GOV-004 執行失敗 | 開啟對應 Child Flow 的 Run History 查看具體錯誤 |
| H8 | Catch 500，ErrorMessage = `connection not configured` | Connection Reference 未授權或已過期 | Step 0 必檢 3 → 重新授權連線 |
| H9 | 報錯「A 'Respond' action has already been executed」 | 多個 Respond 同時執行（Pre-check 失敗的 Respond 後面沒接 Terminate） | Step 0 必檢 7 → 確認每個 Pre-check 失敗 Respond 後面有 Terminate |
| H10 | Flow 成功但 App 端顯示空白結果 | Power Apps 端 PowerFx 沒有用 `Set(varFlowResult, ...)` 接收回傳 | 確認使用完整 PowerFx 範本，特別是 `Set(varFlowResult, GOV002GateTransition.Run(...))` |

---

## GOV-003：Gate Approval Orchestrator

### A. 基本資訊

| 項目 | 值 |
|:--------------------------|:--------------------------------------------------------------|
| Flow 名稱 | GOV-003 Gate Approval Orchestrator |
| 目的 | 依 Gate 類型編排單層/多層審批流程，處理 Approve/Reject 回應；Gate 通過時自動將此 Gate 必要文件（gov_requiredforgate）批次更新為 Approved（Option A），並觸發後續 Child Flow |
| Trigger 類型 | **Manually trigger a flow**（Child Flow）`[Governance Critical Control]` 必須勾選「Only other flows can trigger」 |
| 呼叫此 Flow 的來源 | GOV-002（Gate Transition Request） |
| Connection References | CR-Dataverse-SPN, CR-Approvals `[MVP: 全部使用個人帳號連線]` |
| Concurrency Control | **不開啟**（由 GOV-002 的 Concurrency = 1 控制，同一專案不會重複呼叫） |
| 依賴 Child Flow | GOV-014（Document Freeze，僅 Gate3）、GOV-015（Notification Handler）、GOV-016（Rework Loop Handler，僅 Reject） |
| 對應測試案例 | 07文件 E2E-001 Phase 2~6, E2E-002, E2E-003 |

### Step 0：GOV-003 起手式必檢 8 項

> **為什麼需要 Step 0？** 「Start and wait for an approval」動作找不到收件人、SLA 超時沒處理、Approve/Reject 寫入欄位錯誤是最常見的卡關原因。

**必檢 1：Flow 在同一 Solution 內**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 確保 GOV-002 可以呼叫 GOV-003 |
| 操作路徑 | Maker Portal → 解決方案 → 開啟你的 Solution → 確認 GOV-003 在清單中 |
| 成功長相 | Solution 內看到 GOV-003 Flow |
| 失敗長相 | Flow 不在 Solution 清單 |
| 下一步 | 在 Solution 內直接新建 Flow |

**必檢 2：Trigger 是「Manually trigger a flow」且勾選 Only other flows**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | Child Flow 必須用此 Trigger，否則 Parent 無法以「Run a Child Flow」呼叫 |
| 操作路徑 | 開啟 GOV-003 → 檢查 Trigger 卡片標題 |
| 成功長相 | 標題顯示「Manually trigger a flow」 |
| 失敗長相 | 標題顯示 Power Apps (V2) 或其他 Trigger |
| 下一步 | 刪除 Trigger → 搜尋 `manually trigger` → 選擇正確版本 |

**必檢 3：Approvals Connector 已授權**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 「Start and wait for an approval」需要 Approvals Connector 連線 |
| 操作路徑 | 開啟 GOV-003 → 找到 Approval 動作 → 檢查右上角是否有 ⚠️ |
| 成功長相 | 連線顯示已連線（綠色勾勾） |
| 失敗長相 | 右上角有 ⚠️ 標記 |
| 下一步 | 點擊該 Action → 「變更連線」→ 選擇 CR-Approvals（MVP 模式用個人帳號）→ 授權 |

**必檢 4：Security Group 為 Mail-enabled 且有成員**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | Approval 收件人使用 Security Group Email，若群組非 Mail-enabled 則 Approval 動作會失敗 |
| 操作路徑 | Entra ID → 群組 → 搜尋 GOV-EngineeringManagement / GOV-SecurityReviewers / GOV-QAReviewers / GOV-GovernanceLead → 確認 Email 欄位有值 |
| 成功長相 | 每個群組都有 Email 地址（如 `gov-engmgmt@company.com`），且至少有 1 名成員 |
| 失敗長相 | Email 欄位空白，或群組無成員 |
| 下一步 | 到 Entra ID 將群組類型改為 Mail-enabled Security Group → 加入成員 |

**必檢 5：Dataverse Connection Reference 已授權**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 更新 Review Decision Log 和 Project Registry 需要 Dataverse 連線 |
| 操作路徑 | 開啟 GOV-003 → 檢查所有 Dataverse Action 右上角是否有 ⚠️ |
| 成功長相 | 所有 Action 無 ⚠️ |
| 失敗長相 | 某個 Action 有 ⚠️ |
| 下一步 | 點擊 Action → 選擇已授權的 Dataverse 連線 |

**必檢 6：Review Decision Log 有層級審批狀態欄位**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 多層審批需要記錄每一層的審批狀態 |
| 操作路徑 | Dataverse → 資料表 → Review Decision Log → 確認欄位存在 |
| 成功長相 | 有 gov_gate1securityreviewstatus、gov_gate1qareviewstatus、gov_gate1governancereviewstatus、gov_gate3qareviewstatus、gov_gate3governancereviewstatus 等欄位 |
| 失敗長相 | 欄位不存在 |
| 下一步 | 依 02 文件建立缺失欄位 |

**必檢 7：GOV-014、GOV-015、GOV-016 已建立且狀態為 On**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | GOV-003 需要呼叫這些 Child Flow |
| 操作路徑 | Maker Portal → 解決方案 → 確認 GOV-014、GOV-015、GOV-016 都在清單中且狀態為 On |
| 成功長相 | 三支 Flow 都存在且狀態為 On |
| 失敗長相 | 某支 Flow 不存在或狀態為 Off |
| 下一步 | 先建立缺失的 Child Flow → 開啟 |

**必檢 8：Flow 狀態是 On**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | GOV-002 呼叫 GOV-003 時若 GOV-003 為 Off，GOV-002 會進入 Catch |
| 操作路徑 | Maker Portal → 解決方案 → 開啟 GOV-003 → 看上方狀態列 |
| 成功長相 | 狀態列顯示「開啟」（On） |
| 失敗長相 | 狀態列顯示「關閉」（Off） |
| 下一步 | 點擊右上角「開啟」按鈕 |

### B. 先決條件清單

| 先決條件 | 如何確認 |
|:--------------------------------------|:----------------------------------------------|
| GOV-002 已建立（Parent Flow） | Flow 列表中 GOV-002 狀態為 On |
| GOV-015 Notification Handler 已建立 | Flow 列表中 GOV-015 狀態為 On |
| GOV-016 Rework Loop Handler 已建立 | Flow 列表中 GOV-016 狀態為 On |
| GOV-014 Document Freeze 已建立（僅 Gate3 需要） | Flow 列表中 GOV-014 狀態為 On |
| Dataverse 資料表 Review Decision Log 已建立且有審批狀態欄位 | Maker Portal → Dataverse → 確認存在 |
| Dataverse 資料表 Project Registry 已建立 | 同上 |
| Security Groups 已建立且為 Mail-enabled | Entra ID → 群組 → 確認 Email 有值 |
| CR-Approvals Connection Reference 已授權 | 解決方案 → Connection References → 確認已連線 |

### C. Input Schema（Child Flow Trigger 參數）

在 Trigger 中以「+ Add an input」逐一新增以下參數，**全部使用 Text 類型**：

| 參數名稱 | Input 類型 | 必填 | 說明 |
|:--------------------------|:----------------------|:------:|:----------------------------------------------|
| ProjectId | **Text** | ✓ | gov_projectregistryid（GUID 字串） |
| RequestedGate | **Text** | ✓ | `Gate0` / `Gate1` / `Gate2` / `Gate3` |

### D. Output Schema（Child Flow 回傳標準）

| 輸出參數 | 類型 | 200 成功時 | 400/500 失敗時 |
|:----------------------------------------------|:----------|:----------------------------------------------|:----------------------------------------------|
| StatusCode | Number | `200` | `400` / `500` |
| Status | Text | `Success` | `Failed` |
| ErrorCode | Text | `""` | `ERR-003-xxx` |
| ErrorMessage | Text | `審批已完成` | 具體錯誤訊息 |

> **Child Flow 不需回傳 FlowRunId / Timestamp**：Parent Flow（GOV-002）負責回傳自身的 FlowRunId 與 Timestamp。

### E. 審批矩陣（權威來源：SOP-04-v2-Part3）

| Gate | 審批層級 | 審批者（Security Group Email） | SLA |
|:----------|:----------------------------------------------|:----------------------------------------------|:-------------------------------|
| Gate 0 | 單層 | GOV-EngineeringManagement | 2 工作日 |
| Gate 1 | 三層序列 | Layer 1: GOV-SecurityReviewers → Layer 2: GOV-QAReviewers → Layer 3: GOV-GovernanceLead | 3 工作日 |
| Gate 2 | 單層 | GOV-EngineeringManagement | 2 工作日 |
| Gate 3 | 雙層序列 | Layer 1: GOV-QAReviewers → Layer 2: GOV-GovernanceLead | 3 工作日 |

> **收件人來源**：審批收件人一律使用 Entra ID 的 Mail-enabled Security Group Email 地址。
> 不得在 Flow 中硬寫個人 Email。Security Group 成員變更時無需修改 Flow。

### F. 建立步驟（逐步點擊）

> 以下從「Create Flow」開始，到「Save」結束。每步都寫出搜尋關鍵字與 UI 位置。

**步驟 1：建立 Flow + Manually trigger a flow**

```
1. Maker Portal → 左側「解決方案」→ 開啟你的 Solution
2. 上方「+ 新增」→「自動化」→「雲端流程」→「立即」
   （英文路徑：+ New → Automation → Cloud flow → Instant）
3. 搜尋 manually trigger → 選擇「Manually trigger a flow」
4. 點擊「建立」
5. 點擊 Flow 名稱（左上角），改為「GOV-003 Gate Approval Orchestrator」
6. 在 Trigger 卡片中，點擊「+ Add an input」逐一新增：
   → 選擇 Text → 輸入名稱 ProjectId
   → 選擇 Text → 輸入名稱 RequestedGate
```

**步驟 2：Initialize variables**

```
Action: + 新增步驟 → 搜尋 initialize variable → 選擇「變數」下的「Initialize variable」
  Name：varProjectId
  Type：String
  Value：點擊欄位 → 動態內容 → 選擇「ProjectId」（來自 Trigger）

Action: Initialize variable
  Name：varApprovalOutcome
  Type：String
  Value：（空白）

Action: Initialize variable
  Name：varLastApproverEmail
  Type：String
  Value：（空白）

Action: Initialize variable
  Name：varSLDecisionLevel
  Type：String
  Value：（空白）
  說明：當 Gate 審查涉及 Security Level 判定時，由審批流程中填入 SL 等級值

Action: Initialize variable
  Name：varSLApprovedNote
  Type：String
  Value：（空白）
  說明：SL 決策備註，由審批者在 Approval 回應中提供
```

**步驟 3：建立 Try-MainLogic Scope**

```
Action: + 新增步驟 → 搜尋 scope → 選擇「控制項」下的「Scope」
  點擊 Scope 標題 → 重新命名為「Try-MainLogic」
```

> 以下步驟 4 ~ 步驟 13 都在 Try-MainLogic 內部建立。

**步驟 4：Get Project（在 Try-MainLogic 內部）**

```
在 Try-MainLogic 內部，+ 新增步驟
  → 搜尋 get a row → 選擇「Microsoft Dataverse」下的「Get a row by ID」
  連線：CR-Dataverse-SPN（MVP 模式：選個人帳號）
  Table name：Project Registry
  Row ID：運算式 → variables('varProjectId')
  重新命名為「Get_Project」
```

**步驟 5：Get Review Decision Log**

```
+ 新增步驟 → 搜尋 list rows → 選擇「Microsoft Dataverse」下的「List rows」
  Table name：Review Decision Log
  Filter rows：_gov_parentproject_value eq '@{variables('varProjectId')}' and gov_decision eq 807660000
  Row count：1
  Sort by：createdon desc
  重新命名為「Get_ReviewRecord」
```

**步驟 6：Switch — 依 RequestedGate 分派審批**

```
+ 新增步驟 → 搜尋 switch → 選擇「控制項」下的「Switch」
  On：動態內容 → 選擇「RequestedGate」（來自 Trigger）
```

> **Gate 0 與 Gate 2 為單層審批（步驟 7），Gate 1 為三層審批（步驟 8），Gate 3 為雙層審批（步驟 9）。**
> 以下先說明單層審批的完整做法，再以此為基礎擴展多層。

**步驟 7：Case Gate0 / Gate2 — 單層審批**

```
在 Switch 的 Case Gate0（或 Case Gate2）內：

a. + 新增步驟 → 搜尋 start and wait → 選擇「Approvals」下的
   「Start and wait for an approval」
   （中文：「啟動及等候核准」）
   重新命名為「Approval_Gate0」（或 Approval_Gate2）

   設定：
     Approval type：Approve/Reject - First to respond
       （「核准/拒絕 - 由最先回應者決定」）
     Title：Gate 0 審批 - @{outputs('Get_Project')?['body/gov_requestid']}
       （或 Gate 2 審批 - ...）
     Assigned to：
       ★ 關鍵：在此欄位輸入 Security Group Email ★
       Gate 0 / Gate 2 → 輸入 GOV-EngineeringManagement 群組的 Email
       （例如 gov-engmgmt@company.com）
     Details：
       專案：@{outputs('Get_Project')?['body/gov_requestid']}
       申請 Gate：@{triggerBody()?['RequestedGate']}
       申請者：@{outputs('Get_Project')?['body/gov_submittedby']}
     Item link：（可留空或填 Power Apps URL）
     Item link description：查看專案詳情

b. Set variable
   Name：varLastApproverEmail
   Value：動態內容 → outputs('Approval_Gate0')?['body/responder']?['email']
   （Gate2 使用 outputs('Approval_Gate2')?['body/responder']?['email']）

c. Set variable
   Name：varApprovalOutcome
   Value：動態內容 → 選擇「Outcome」（來自 Approval 動作）
```

> **⚠ 「Assigned to」欄位必須填 Mail-enabled Security Group 的 Email 地址。**
> 不要填個人 Email。群組內的所有成員都會收到審批通知，第一個回應者的決定即為最終結果。

**步驟 8：Case Gate1 — 三層序列審批**

```
在 Switch 的 Case Gate1 內：

── Layer 1：Security Review ──

a. + 新增步驟 → Start and wait for an approval
   重新命名為「Approval_Gate1_Layer1_Security」
   Approval type：Approve/Reject - First to respond
   Title：[Gate 1 - Security Review] @{outputs('Get_Project')?['body/gov_requestid']}
   Assigned to：GOV-SecurityReviewers 群組的 Email

b. Condition：Layer1 結果判斷
   條件：outputs('Approval_Gate1_Layer1_Security')?['body/outcome'] is equal to Approve

   False 分支（Reject）：
     Set variable → varApprovalOutcome = Reject
     Update a row → Review Decision Log
       gov_gate1securityreviewstatus：807660002（Rejected）
       gov_decision：807660002（Rejected）
       gov_approvedby：outputs('Approval_Gate1_Layer1_Security')?['body/responder']?['email']
       gov_revieweddate：utcNow()
       gov_comments：outputs('Approval_Gate1_Layer1_Security')?['body/comments']
     → 跳到步驟 10 的 Reject 處理（Terminate 此 Case）

   True 分支（Approve）：
     Update a row → Review Decision Log
       gov_gate1securityreviewstatus：807660001（Approved）
     → 繼續 Layer 2

── Layer 2：QA Review ──

c. + 新增步驟 → Start and wait for an approval
   重新命名為「Approval_Gate1_Layer2_QA」
   Approval type：Approve/Reject - First to respond
   Title：[Gate 1 - QA Review] @{outputs('Get_Project')?['body/gov_requestid']}
   Assigned to：GOV-QAReviewers 群組的 Email

d. Condition：Layer2 結果判斷（同 Layer1 模式）
   False 分支（Reject）：
     Set variable → varApprovalOutcome
     Value：Reject
     Update a row → Review Decision Log
       gov_gate1qareviewstatus：807660002（Rejected）
       gov_decision：807660002（Rejected）
     → Terminate（Cancelled）
   True → 更新 gov_gate1qareviewstatus = Approved → 繼續 Layer 3

── Layer 3：Governance Lead Review ──

e. + 新增步驟 → Start and wait for an approval
   重新命名為「Approval_Gate1_Layer3_Governance」
   Approval type：Approve/Reject - First to respond
   Title：[Gate 1 - Governance Review] @{outputs('Get_Project')?['body/gov_requestid']}
   Assigned to：GOV-GovernanceLead 群組的 Email

f. Condition：Layer3 結果判斷
   False 分支（Reject）：
     Set variable → varApprovalOutcome
     Value：Reject
     Update a row → Review Decision Log
       gov_gate1governancereviewstatus：807660002（Rejected）
       gov_decision：807660002（Rejected）
     → Terminate（Cancelled）
   True → 更新 gov_gate1governancereviewstatus = Approved
          Set variable → varLastApproverEmail
          Value：outputs('Approval_Gate1_Layer3_Governance')?['body/responder']?['email']
          Set variable → varApprovalOutcome = Approve
```

> **⚠ 多層審批的關鍵規則**：
> 1. 每一層的 Approval 必須等上一層完成才開始（序列，非平行）
> 2. 任何一層 Reject → 立即停止後續層級 → 進入 Reject 處理
> 3. 所有層級都 Approve → 才進入 Approve 處理
> 4. 每一層的審批結果都必須寫入 Review Decision Log 的對應欄位

**步驟 9：Case Gate3 — 雙層序列審批**

```
在 Switch 的 Case Gate3 內：

── Layer 1：QA Review ──

a. Start and wait for an approval → 「Approval_Gate3_Layer1_QA」
   Assigned to：GOV-QAReviewers 群組的 Email
   Title：[Gate 3 - QA Review] @{outputs('Get_Project')?['body/gov_requestid']}

b. Condition：Reject → 更新 gov_gate3qareviewstatus = Rejected + Terminate
              Approve → 更新 gov_gate3qareviewstatus = Approved → 繼續 Layer 2

── Layer 2：Governance Lead Review ──

c. Start and wait for an approval → 「Approval_Gate3_Layer2_Governance」
   Assigned to：GOV-GovernanceLead 群組的 Email
   Title：[Gate 3 - Governance Review] @{outputs('Get_Project')?['body/gov_requestid']}

d. Condition：Reject → 更新 gov_gate3governancereviewstatus = Rejected + Terminate
              Approve → 更新 gov_gate3governancereviewstatus = Approved
                        Set variable → varLastApproverEmail
                        Value：outputs('Approval_Gate3_Layer2_Governance')?['body/responder']?['email']
                        Set variable → varApprovalOutcome = Approve
```

**步驟 10：Approve 處理（Switch 之後）**

```
Switch 結束後（所有 Case 匯合處）：

+ 新增步驟 → Condition
  重新命名為「Is_Approved」
  條件：variables('varApprovalOutcome') is equal to Approve

  True 分支（Approve）：

  a. Update a row → Review Decision Log
     （搜尋 update a row → 選擇 Microsoft Dataverse）
     Table name：Review Decision Log
     Row ID：first(outputs('Get_ReviewRecord')?['body/value'])?['gov_reviewdecisionlogid']
     欄位對應：
       gov_decision：807660001（Approved）
       gov_approvedby：動態內容 → variables('varLastApproverEmail')
       gov_revieweddate：utcNow()
       gov_comments：最後一層 Approval 的 comments

  b. Update a row → Project Registry
     Table name：Project Registry
     Row ID：@{variables('varProjectId')}
     欄位對應：
       gov_currentgate：RequestedGate 對應的 OptionSet 值
         Gate0 → 807660001
         Gate1 → 807660002
         Gate2 → 807660003
         Gate3 → 807660004
       gov_requeststatus：807660000（None）
       Gate{X}PassedDate 欄位：utcNow()
         Gate0 → gov_gate0passeddate
         Gate1 → gov_gate1passeddate
         Gate2 → gov_gate2passeddate
         Gate3 → gov_gate3passeddate

  c. List rows → Document Register（批次核准此 Gate 的必要文件）
     [Option A：Gate 通過 = 文件自動 Approved]
     （搜尋 list rows → 選擇「Microsoft Dataverse」下的「List rows」）
     Table name：Document Register
     Filter rows：_gov_parentproject_value eq '@{variables('varProjectId')}'
                  and gov_requiredforgate eq '@{triggerBody()?['RequestedGate']}'
                  and (gov_documentrole eq 807660001 or gov_documentrole eq 807660002)
                  （Draft = 807660001，Active = 807660002；跳過 Planned/Superseded/Approved/Frozen）
     重新命名為「List_RequiredDocs_ForGate」

  d. Apply to each
     重新命名為「ApproveEach_RequiredDoc」
     Select an output from previous steps：動態內容 → List_RequiredDocs_ForGate → value

     在 Apply to each 內部：
       + 新增步驟 → Update a row → Document Register
       重新命名為「Update_DocToApproved」
       Table name：Document Register
       Row ID：動態內容 → items('ApproveEach_RequiredDoc')?['gov_documentregisterid']
       欄位對應：
         gov_documentrole：807660004（Approved）
         gov_approveddate：utcNow()

  e. Run a Child Flow → GOV-015 Notification Handler
     （搜尋 run a child flow → 選擇「Flows」下的「Run a Child Flow」）
     Child Flow：GOV-015-NotificationHandler
     NotificationType：GateApproved
     RecipientEmail：@{outputs('Get_Project')?['body/gov_submittedby']}
     Subject：Gate @{triggerBody()?['RequestedGate']} 已核准 - @{outputs('Get_Project')?['body/gov_requestid']}
     Body：您的 Gate 申請已獲核准。
     ProjectId：@{variables('varProjectId')}

  f. Write SL Decision Record（SL 決策記錄寫入）

     說明：當 Gate 審查涉及 Security Level 判定時，記錄 SL 決策至審查記錄，
     支援 HEAD-K6 / SEC-K5 KPI 計算。

     + 新增步驟 → 搜尋 condition → 選擇「控制項」下的「Condition」
       重新命名為「Is_SLDecisionAvailable」
       條件設定：
         左側：運算式 → not(empty(variables('varSLDecisionLevel')))
         運算子：is equal to
         右側：true

     If Yes（SL 決策有值 → 寫入 SL Decision Record）：
       + 新增步驟 → 搜尋 update a row → 選擇「Microsoft Dataverse」下的「Update a row」
       Table name：Review Decision Log
       Row ID：first(outputs('Get_ReviewRecord')?['body/value'])?['gov_reviewdecisionlogid']
       欄位對應：
         gov_sldecisionlevel：@{int(variables('varSLDecisionLevel'))}
         gov_slapprovedby：（從審批結果 Lookup User）
         gov_slapprovednote：@{variables('varSLApprovedNote')}
       重新命名為「Update_SLDecisionRecord」

     If No（無 SL 決策 → 跳過）：不做任何事

  False 分支（Reject）：見步驟 11
```

> **⚠ CurrentGate OptionSet 對應表（不可硬猜）**：
>
> | RequestedGate (Text) | OptionSet 值 | 欄位 |
> |:----------------------------------------------|:----------|:----------------------------------------------|
> | Gate0 | 807660001 | gov_gate0passeddate |
> | Gate1 | 807660002 | gov_gate1passeddate |
> | Gate2 | 807660003 | gov_gate2passeddate |
> | Gate3 | 807660004 | gov_gate3passeddate |

**步驟 11：Reject 處理（Is_Approved False 分支）**

> ⚠ 通知邏輯說明：
>   - 若 ReworkCount < 3（呼叫 GOV-016）：由 GOV-016 負責發送 GateRejected 通知，GOV-003 不再直接呼叫 GOV-015。
>   - 若 ReworkCount ≥ 3（不呼叫 GOV-016，專案轉為 OnHold）：GOV-003 直接呼叫 GOV-015 發送 GateRejected 通知。

```
a. Update a row → Review Decision Log
   gov_decision：807660002（Rejected）
   gov_approvedby：拒絕層 Approval 的 responder email
   gov_revieweddate：utcNow()
   gov_comments：拒絕層 Approval 的 comments

b. Update a row → Project Registry
   Row ID：@{variables('varProjectId')}
   gov_requeststatus：807660000（None）
   （⚠ CurrentGate 保持不變 — Reject 不推進 Gate）

c. Run a Child Flow → GOV-016 Rework Loop Handler
   Child Flow：GOV-016-ReworkLoopHandler
   ProjectId：@{variables('varProjectId')}

d. Condition：Is_ReworkThresholdReached
   條件：variables('varReworkCount') greater than or equal to 3

   True（OnHold 路徑 — GOV-016 未呼叫，GOV-003 直接通知）：
     Run a Child Flow → GOV-015 Notification Handler
       NotificationType：GateRejected
       RecipientEmail：@{outputs('Get_Project')?['body/gov_submittedby']}
       Subject：Gate @{triggerBody()?['RequestedGate']} 已駁回（已達重工上限）- @{outputs('Get_Project')?['body/gov_requestid']}
       Body：您的 Gate 申請已被駁回，且已達重工次數上限，專案轉為 OnHold。
       ProjectId：@{variables('varProjectId')}

   False（正常 Reject 路徑 — GOV-016 已呼叫並負責通知）：
     （不做任何事 — 通知由 GOV-016 發送）
```

**步驟 12：Gate 3 特殊處理 — 呼叫 GOV-014 Document Freeze**

```
在步驟 10 的 Approve True 分支最後（GOV-015 通知之後）：

+ 新增步驟 → Condition
  重新命名為「Is_Gate3_Approved」
  條件：triggerBody()?['RequestedGate'] is equal to Gate3
  （varApprovalOutcome 已在外層 Is_Approved 確認為 Approve，此處無需重複驗證）

  True 分支：
    Run a Child Flow → GOV-014 Document Freeze
    Child Flow：GOV-014-DocumentFreeze
    ProjectId：@{variables('varProjectId')}

  False 分支：（不做任何事）
```

> **⚠ Gate 3 Approve 後必須呼叫 GOV-014。** 若 GOV-014 執行失敗，GOV-003 會進入 Catch，
> 但 Gate 3 已寫入 Approved 狀態。此為已知的部分完成風險，需人工介入重新執行凍結。

**步驟 13：成功 Respond**

```
在 Try-MainLogic 最後（Is_Approved 之後）：

+ 新增步驟 → Respond to a PowerApp or flow
  Number → StatusCode → 200
  Text → Status → Success
  Text → ErrorCode → （空白）
  Text → ErrorMessage → 審批已完成
```

> 步驟 13 是 Try-MainLogic 的最後一步。以下建立 Catch Scope。

**步驟 14：建立 Catch-ErrorHandler Scope**

```
在 Try-MainLogic Scope 下方（不是內部）：
  + 新增步驟 → Scope → 重新命名為「Catch-ErrorHandler」

  設定 Configure run after：
    點擊 Catch-ErrorHandler 右上角「...」→「設定在之後執行」
    → 取消勾選「成功」
    → 勾選「已失敗」與「已逾時」
    → 點擊「完成」
```

**步驟 15：Catch 內部 — ErrorMessage + Respond**

```
在 Catch-ErrorHandler 內部：

a. Compose → 重新命名為「Compose-ErrorMessage」
   Inputs：運算式 → coalesce(result('Try-MainLogic')?[0]?['error']?['message'], '未知錯誤')

b. Respond to a PowerApp or flow
   Number → StatusCode → 500
   Text → Status → Failed
   Text → ErrorCode → ERR-003-SYSTEM
   Text → ErrorMessage → 動態內容 → Compose-ErrorMessage 的 Outputs
```

**步驟 16：Save**

```
點擊右上角「儲存」（Save）→ 等待儲存完成
```

### G. SLA 超時處理

> **「Start and wait for an approval」預設會無限等待。** 若審批者未在 SLA 內回應，Flow 會持續等待直到 30 天自動逾時。

| 處理方式 | 說明 |
|:----------------------------------------------|:----------------------------------------------|
| **目前版本（MVP）** | 不設超時，依賴 GOV-019 SLA Monitor 每日排程掃描逾期審批並發送催辦通知 |
| **Hardened 版本** | 在每個 Approval 動作上設定 Timeout：`Settings → Timeout → PT48H`（2 工作日）或 `PT72H`（3 工作日）→ 超時後 Approval 動作回傳 outcome = 空白 → 加入 Condition 判斷 outcome 是否為空 → 空白視為逾時 → 發送催辦通知 + 可選自動重送 |

> **設定 Timeout 的 UI 路徑**：
> 點擊 Approval 動作右上角「...」→「設定」（Settings）→ 找到「Timeout」欄位 → 輸入 ISO 8601 Duration 格式（如 `PT48H` = 48 小時，`P3D` = 3 天）

### H. 必做設定檢核點

| 檢核項目 | 確認方式 | 預期結果 |
|:----------------------------------------------|:----------------------------------------------|:-------------------------------|
| Trigger 類型 | Trigger 卡片標題 | Manually trigger a flow |
| Input 參數 | Trigger → 2 個參數 | ProjectId(Text), RequestedGate(Text) |
| Approvals Connector | Approval 動作右上角 | 無 ⚠️ 標記 |
| Dataverse Connector | 每個 Dataverse Action 右上角 | 無 ⚠️ 標記 |
| Security Group Email | Approval 動作 Assigned to | 填的是群組 Email，非個人 Email |
| Catch Configure run after | Catch Scope → 設定在之後執行 | 成功未勾選，已失敗 + 已逾時已勾選 |
| Gate3 → GOV-014 呼叫 | Gate3 Approve 後 | 有 Run a Child Flow → GOV-014 |
| Flow 名稱 | Flow 左上角 | `GOV-003 Gate Approval Orchestrator` |

### I. 最小驗證流程

**第 1 步：從 GOV-002 觸發一筆 Gate0 申請**

```
1. 在 Power Apps 中選擇一個 Active 測試專案（CurrentGate = Pending）
2. 提交 Gate0 申請
3. GOV-002 會呼叫 GOV-003
```

**第 2 步：檢查 Approval 通知**

```
1. 開啟 GOV-EngineeringManagement 群組成員的 Email 或 Teams
2. 確認收到 Approval 通知
3. 點擊「Approve」
```

**第 3 步：去哪裡看 GOV-003 Run History**

```
1. Maker Portal → 解決方案 → 開啟 GOV-003
2. 左側「28 天執行歷程記錄」
3. 找到最新一筆 → 點擊開啟
```

**第 4 步：成功時 Run History 預期看到的畫面**

```
所有 Action 都是綠色勾勾：
  ✓ Manually trigger a flow
  ✓ Initialize variable (varProjectId)
  ✓ Initialize variable (varApprovalOutcome)
  ✓ Scope: Try-MainLogic
    ✓ Get_Project
    ✓ Get_ReviewRecord
    ✓ Switch (RequestedGate)
      ✓ Case Gate0
        ✓ Approval_Gate0（Outcome = Approve）
        ✓ Set variable (varApprovalOutcome = Approve)
    ✓ Is_Approved → True
      ✓ Update Review Decision Log（Decision = Approved）
      ✓ Update Project Registry（CurrentGate = Gate0）
      ✓ List_RequiredDocs_ForGate（回傳此 Gate 必要文件清單）
      ✓ ApproveEach_RequiredDoc（逐筆 Update_DocToApproved = 807660004）
      ✓ Run GOV-015 Notification
      ✓ Is_Gate3_Approved → False（跳過）
    ✓ Respond (200 Success)
  ⊘ Scope: Catch-ErrorHandler（灰色跳過 = 正常）
```

**第 5 步：失敗時分類排查**

| Run History 畫面 | 分類 | 排查方式 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| Approval 動作失敗（紅色 ✗） | **Approval Connector 問題** | 檢查 CR-Approvals 連線 → 確認 Security Group Email 有效 |
| Approval 完成但後續 Update 失敗 | **Dataverse 寫入問題** | 展開失敗 Action → 看欄位是否存在、OptionSet 值是否正確 |
| GOV-014 呼叫失敗（僅 Gate3） | **Child Flow 問題** | 開啟 GOV-014 Run History 查看具體錯誤 |
| Catch 執行 + Respond 500 | **系統例外** | 展開 Compose-ErrorMessage 看錯誤訊息 |

### J. 常見失敗原因與對應排查路徑

| 編號 | 失敗現象 | 根因 | 排查路徑 |
|:----------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| J1 | Approval 動作失敗，錯誤 `The recipient address is not valid` | Security Group 非 Mail-enabled 或無 Email | Entra ID → 群組 → 確認 Email 欄位有值 |
| J2 | Approval 動作失敗，錯誤 `No recipients found` | Security Group 無成員 | Entra ID → 群組 → 確認至少有 1 名成員 |
| J3 | Approve 後 CurrentGate 沒更新 | Update a row 的 OptionSet 值填錯 | 確認 Gate0=807660001, Gate1=807660002, Gate2=807660003, Gate3=807660004 |
| J4 | Reject 後 CurrentGate 被清空 | Reject 分支不應更新 CurrentGate | 確認 Reject 只更新 RequestStatus=None，不動 CurrentGate |
| J5 | 多層審批的第 2 層沒觸發 | Layer 1 Reject 後沒接 Terminate，繼續執行 Layer 2 | 確認 Reject 分支末尾有 Terminate（Cancelled） |
| J6 | Gate 3 通過但文件沒凍結 | 未呼叫 GOV-014 或 GOV-014 執行失敗 | 確認 Is_Gate3_Approved 條件正確 → 開啟 GOV-014 Run History |
| J7 | GOV-015 通知未送達 | GOV-015 未建立或 Email Connector 問題 | 確認 GOV-015 狀態為 On → 開啟 GOV-015 Run History |
| J8 | Flow 等待超過 30 天後自動失敗 | Approval 無人回應，超過 Flow 最長運行時間 | 使用 GOV-019 SLA Monitor 監控逾期審批 |
| J9 | Gate1 三層審批只記錄了最後一層的 approvedby | 只在最後寫入 approvedby | 確認每一層的審批結果都分別寫入對應的 reviewstatus 欄位 |
| J10 | Catch 報錯 `Child flow GOV-016 not found` | GOV-016 未建立或不在同一 Solution | 確認 GOV-016 在 Solution 內且狀態為 On |
| J11 | Gate 通過但必要文件狀態未更新為 Approved | List_RequiredDocs_ForGate Filter 條件有誤，或 Document Register 中 gov_requiredforgate 欄位值格式與 RequestedGate 不符 | 展開 List_RequiredDocs_ForGate → 確認 Filter rows 正確 → 確認文件欄位值為「Gate0」/「Gate1」/「Gate2」/「Gate3」文字格式（非 OptionSet 數字） |
| J12 | ApproveEach_RequiredDoc 失敗，錯誤 `Record not found` | Apply to each 內的 Row ID 欄位名稱錯誤（應為 gov_documentregisterid） | 展開失敗的 Update_DocToApproved → 確認 Row ID 使用 `items('ApproveEach_RequiredDoc')?['gov_documentregisterid']` |

---

## GOV-004：Risk Acceptance

### A. 基本資訊

| 項目 | 值 |
|:--------------------------|:--------------------------------------------------------------|
| Flow 名稱 | GOV-004 Risk Acceptance |
| 目的 | Gate 3 申請時，依最高殘餘風險等級決定是否需要 Risk Owner / Executive 審批 |
| Trigger 類型 | **Manually trigger a flow**（Child Flow）`[Governance Critical Control]` 必須勾選「Only other flows can trigger」 |
| 呼叫此 Flow 的來源 | GOV-002（Gate 3 限定，在 GOV-013B 之後呼叫） |
| Connection References | CR-Dataverse-SPN, CR-Approvals `[MVP: 全部使用個人帳號連線]` |
| Concurrency Control | **不開啟**（由 GOV-002 的 Concurrency = 1 控制） |
| 依賴 Child Flow | GOV-015（Notification Handler） |
| 對應測試案例 | 07文件 E2E-001 Phase 5 |

### Step 0：GOV-004 起手式必檢 6 項

> **為什麼需要 Step 0？** Risk Owner Email 查無人、Executive Group 非 Mail-enabled、Low 風險卻發了審批 — 是最常見的卡關原因。

**必檢 1：Flow 在同一 Solution 內**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 確保 GOV-002 可以呼叫 GOV-004 |
| 操作路徑 | Maker Portal → 解決方案 → 確認 GOV-004 在清單中 |
| 成功長相 | Solution 內看到 GOV-004 Flow |
| 失敗長相 | Flow 不在 Solution 清單 |
| 下一步 | 在 Solution 內直接新建 Flow |

**必檢 2：Trigger 是「Manually trigger a flow」**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | Child Flow 必須用此 Trigger |
| 操作路徑 | 開啟 GOV-004 → 檢查 Trigger 卡片標題 |
| 成功長相 | 標題顯示「Manually trigger a flow」 |
| 失敗長相 | 使用了其他 Trigger 類型 |
| 下一步 | 刪除 Trigger → 搜尋 `manually trigger` → 選擇正確版本 |

**必檢 3：Project Registry 有 Risk Owner 與 Executive Approver 欄位**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | Medium 風險需要查詢 Risk Owner Email，High 風險還需要 Executive 審批 |
| 操作路徑 | Dataverse → 資料表 → Project Registry → 確認欄位存在 |
| 成功長相 | 有 gov_riskowner（Text，Email）和 gov_executiveapprover（Text，Email）欄位 |
| 失敗長相 | 欄位不存在 |
| 下一步 | 依 02 文件建立缺失欄位 |

**必檢 4：測試專案的 Risk Owner 欄位有值**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | Medium/High 風險的 Approval 收件人從 Project Registry 的 gov_riskowner 讀取 |
| 操作路徑 | Dataverse → Project Registry → 開啟測試專案 → 檢查 gov_riskowner 欄位 |
| 成功長相 | 欄位有有效的 Email 地址（如 `riskowner@company.com`） |
| 失敗長相 | 欄位為空 |
| 下一步 | 在 Project Registry 中填入 Risk Owner 的 Email |

**必檢 5：GOV-ExecutiveManagement 群組為 Mail-enabled（僅 High 風險需要）**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | High 風險第二層審批收件人 |
| 操作路徑 | Entra ID → 群組 → 搜尋 GOV-ExecutiveManagement → 確認 Email 有值 |
| 成功長相 | 群組有 Email 地址且至少有 1 名成員 |
| 失敗長相 | Email 欄位空白或無成員 |
| 下一步 | 設為 Mail-enabled Security Group → 加入成員 |

**必檢 6：Approvals 與 Dataverse Connector 已授權**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | Flow 需要 Approval 和 Dataverse 連線 |
| 操作路徑 | 開啟 GOV-004 → 檢查所有 Action 右上角 |
| 成功長相 | 所有 Action 無 ⚠️ 標記 |
| 失敗長相 | 某 Action 有 ⚠️ |
| 下一步 | 點擊 → 選擇已授權的連線 |

### B. 先決條件清單

| 先決條件 | 如何確認 |
|:--------------------------------------|:----------------------------------------------|
| GOV-002 已建立（Parent Flow） | Flow 列表中 GOV-002 狀態為 On |
| GOV-013B Risk Aggregator 已建立（產出 HighestResidualRiskLevel） | Flow 列表中 GOV-013B 狀態為 On |
| GOV-015 Notification Handler 已建立 | Flow 列表中 GOV-015 狀態為 On |
| Project Registry 有 gov_riskowner、gov_executiveapprover 欄位 | Maker Portal → Dataverse → 確認存在 |
| Project Registry 有 gov_riskacceptancestatus、gov_riskacceptancedate 欄位 | 同上 |
| GOV-ExecutiveManagement Security Group 已建立且 Mail-enabled | Entra ID → 確認 |

### C. Input Schema（Child Flow Trigger 參數）

| 參數名稱 | Input 類型 | 必填 | 說明 |
|:--------------------------|:----------------------|:------:|:----------------------------------------------|
| ProjectId | **Text** | ✓ | gov_projectregistryid（GUID 字串） |
| HighestResidualRiskLevel | **Text** | ✓ | 由 GOV-013B 計算回傳（`High` / `Medium` / `Low`） |

### D. Output Schema（Child Flow 回傳）

| 輸出參數 | 類型 | 說明 |
|:----------------------------------------------|:----------|:----------------------------------------------|
| StatusCode | Number | `200`（成功）/ `400`（風險未被接受）/ `500`（系統例外） |
| Status | Text | `Success` / `Rejected` / `Failed` |
| RiskAcceptanceStatus | Text | `Accepted` / `Rejected` |
| RiskAcceptanceType | Text | `AutoAccepted`（Low）/ `SingleLayer`（Medium）/ `DualLayer`（High） |
| ErrorCode | Text | 錯誤代碼（成功時為空白） |
| ErrorMessage | Text | 錯誤訊息（成功時為空白） |

> **GOV-002 如何使用 GOV-004 回傳**：
> GOV-002 檢查 `Status = Success AND RiskAcceptanceStatus = Accepted` 才繼續呼叫 GOV-003。
> 若 `RiskAcceptanceStatus = Rejected`，GOV-002 會回覆 400 ERR-002-RISK 給 Power Apps。

### E. 風險等級審批矩陣（權威來源：SOP-04-v2-Part3）

| 風險等級 | 審批層級 | 審批者 | 處理方式 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| **Low** | 無（自動接受） | N/A | 不發 Approval → 直接寫入 RiskAcceptanceStatus = Accepted, RiskOwner = `Auto-Accepted` |
| **Medium** | 單層 | Risk Owner（從 Project Registry `gov_riskowner` 讀取） | 發送 Approval → 等待 Risk Owner 回應 |
| **High** | 雙層序列 | Layer 1: Risk Owner → Layer 2: GOV-ExecutiveManagement（Security Group Email） | 兩層皆 Approve → Accepted；任一層 Reject → Rejected |

> **Risk Owner 來源**：從 `outputs('Get_Project')?['body/gov_riskowner']` 讀取。
> 此欄位必須在建立專案時（FORM-001）或 Gate 0 後由 System Architect 填入。
> **不得硬寫 Email**。

### F. 建立步驟（逐步點擊）

**步驟 1：建立 Flow + Manually trigger a flow**

```
1. Maker Portal → 解決方案 → 開啟 Solution
2. + 新增 → 自動化 → 雲端流程 → 立即
3. 搜尋 manually trigger → 選擇「Manually trigger a flow」→ 建立
4. 改名為「GOV-004 Risk Acceptance」
5. + Add an input：
   → Text → ProjectId
   → Text → HighestResidualRiskLevel
```

**步驟 2：Initialize variables**

```
Action: Initialize variable
  Name：varProjectId
  Type：String
  Value：動態內容 → ProjectId

Action: Initialize variable
  Name：varRiskAcceptanceStatus
  Type：String
  Value：（空白）

Action: Initialize variable
  Name：varRiskAcceptanceType
  Type：String
  Value：（空白）
```

**步驟 3：建立 Try-MainLogic Scope**

```
+ 新增步驟 → Scope → 重新命名為「Try-MainLogic」
```

**步驟 4：Get Project（在 Try-MainLogic 內部）**

```
+ 新增步驟 → Get a row by ID（Dataverse）
  Table name：Project Registry
  Row ID：運算式 → variables('varProjectId')
  重新命名為「Get_Project」
```

**步驟 4b：Guard Clause — Risk Owner 空值檢查**

```
在 Switch 前新增 Condition，重新命名為「Check_RiskOwnerNotNull」：

Guard Clause（Risk Owner 空值檢查）：
在 Switch 前新增 Condition：
條件：empty(outputs('Get_Project')?['body/gov_riskowner']) is equal to true
      AND HighestResidualRiskLevel is not equal to Low（807660000）

True（Risk Owner 為空且非 Low 風險）：
  Respond to a PowerApp or flow
    StatusCode：400
    Status：Failed
    ErrorCode：ERR-004-002
    ErrorStage：PreCheck
    ErrorMessage：Risk Owner 未設定 — 請在 Project Registry 填入 gov_riskowner 後再執行 Risk Acceptance
```

**步驟 5：Switch — 依 HighestResidualRiskLevel 分派**

```
+ 新增步驟 → Switch
  On：動態內容 → HighestResidualRiskLevel

  ⚠ 三個 Case：Low、Medium、High
```

**步驟 6：Case Low — 自動接受（不發 Approval）**

```
Case 值：Low

a. Set variable
   Name：varRiskAcceptanceStatus
   Value：Accepted

b. Set variable
   Name：varRiskAcceptanceType
   Value：AutoAccepted

c. Update a row → Project Registry
   Row ID：@{variables('varProjectId')}
   欄位對應：
     gov_riskacceptancestatus：807660001（Accepted）
     gov_riskacceptancecomments：Auto-Accepted (Low Risk — no manual approval required)
     gov_riskaccepteddate：utcNow()
   ⚠ Low 風險路徑：
     不更新 gov_riskowner（保留原有負責人資訊）
     僅更新：
       gov_riskacceptancestatus：807660001（Accepted）
       gov_riskacceptancecomments：Auto-Accepted (Low Risk — no manual approval required)
       gov_riskaccepteddate：utcNow()
```

> **⚠ Low 風險不發 Approval。** 直接寫入 Accepted 狀態。gov_riskowner 保留原有值，不覆寫，以維護責任人資訊。

**步驟 7：Case Medium — 單層 Risk Owner 審批**

```
Case 值：Medium

a. + 新增步驟 → Start and wait for an approval
   重新命名為「Approval_RiskOwner」
   Approval type：Approve/Reject - First to respond
   Title：[Risk Acceptance - Medium] @{outputs('Get_Project')?['body/gov_requestid']}
   Assigned to：
     ★ 動態內容 → 選擇 Get_Project 下的 gov_riskowner ★
     （這會填入 Project Registry 中的 Risk Owner Email）
   Details：
     專案：@{outputs('Get_Project')?['body/gov_requestid']}
     最高殘餘風險等級：Medium
     Risk Owner 請審核是否接受此風險等級。

b. Condition：判斷 Outcome
   條件：outputs('Approval_RiskOwner')?['body/outcome'] is equal to Approve

   True 分支（Approve）：
     Set variable → varRiskAcceptanceStatus = Accepted
     Set variable → varRiskAcceptanceType = SingleLayer
     Update a row → Project Registry
       gov_riskacceptancestatus：807660001（Accepted）
       gov_riskacceptancedate：utcNow()
       gov_riskowner：outputs('Approval_RiskOwner')?['body/responder']?['email']

   False 分支（Reject）：
     Set variable → varRiskAcceptanceStatus = Rejected
     Set variable → varRiskAcceptanceType = SingleLayer
     Update a row → Project Registry
       gov_riskacceptancestatus：807660002（Rejected）
       gov_riskowner：outputs('Approval_RiskOwner')?['body/responder']?['email']
```

> **⚠ User Lookup 的關鍵**：
> `Assigned to` 欄位不要手動輸入 Email，必須用動態內容選取 `Get_Project` 的 `gov_riskowner`。
> 這樣當 Risk Owner 變更時，無需修改 Flow。
> 若 `gov_riskowner` 為空，Approval 動作會失敗 → Catch 500。
> 因此 Step 0 必檢 4（Risk Owner 有值）非常重要。

**步驟 8：Case High — 雙層序列審批**

```
Case 值：High

── Layer 1：Risk Owner ──

a. Start and wait for an approval → 「Approval_High_Layer1_RiskOwner」
   Assigned to：動態內容 → Get_Project 下的 gov_riskowner
   Title：[Risk Acceptance - High - Layer 1] @{outputs('Get_Project')?['body/gov_requestid']}

b. Condition：Layer1 結果
   Reject → Set varRiskAcceptanceStatus = Rejected, varRiskAcceptanceType = DualLayer
            Update Project Registry → gov_riskacceptancestatus = 807660002（Rejected）
            → 跳出（不繼續 Layer 2）

   Approve → 繼續 Layer 2
            Update a row → Project Registry
              gov_riskownerreviewstatus：807660001（Approved）

── Layer 2：Executive Management ──

c. Start and wait for an approval → 「Approval_High_Layer2_Executive」
   Assigned to：GOV-ExecutiveManagement 群組的 Email
     ★ 此處填 Security Group Email（如 gov-exec@company.com）★
   Title：[Risk Acceptance - High - Layer 2 Executive] @{outputs('Get_Project')?['body/gov_requestid']}

d. Condition：Layer2 結果
   Reject → Set varRiskAcceptanceStatus = Rejected, varRiskAcceptanceType = DualLayer
            Update Project Registry → gov_riskacceptancestatus = 807660002（Rejected）
              gov_executivereviewstatus：807660002（Rejected）

   Approve → Set varRiskAcceptanceStatus = Accepted, varRiskAcceptanceType = DualLayer
             Update Project Registry →
               gov_riskacceptancestatus：807660001（Accepted）
               gov_riskacceptancedate：utcNow()
               gov_riskowner：Layer1 responder email
               gov_executiveapprover：Layer2 responder email
               gov_executivereviewstatus：807660001（Approved）
```

> **⚠ High 風險 gov_riskowner 與 gov_executiveapprover 寫入規則**：
> - `gov_riskowner`：寫入 Layer 1 Risk Owner Approval 的 `responder/email`
> - `gov_executiveapprover`：寫入 Layer 2 Executive Approval 的 `responder/email`
> - 兩欄位都是 Text 類型（不是 Lookup），直接寫入 Email 字串

**步驟 9：Switch 後 — 發送通知**

```
Switch 結束後（所有 Case 匯合處）：

+ 新增步驟 → Run a Child Flow → GOV-015 Notification Handler
  NotificationType：RiskAccepted（或 RiskRejected，依 varRiskAcceptanceStatus 判斷）
  RecipientEmail：@{outputs('Get_Project')?['body/gov_submittedby']}
  Subject：風險接受結果 - @{outputs('Get_Project')?['body/gov_requestid']}
  Body：最高殘餘風險等級 @{triggerBody()?['HighestResidualRiskLevel']}，接受狀態：@{variables('varRiskAcceptanceStatus')}
  ProjectId：@{variables('varProjectId')}
```

**步驟 10：成功 Respond**

```
+ 新增步驟 → Respond to a PowerApp or flow
  Number → StatusCode → 200（若 Accepted）或 400（若 Rejected）
  Text → Status → Success（若 Accepted）或 Rejected（若 Rejected）
  Text → RiskAcceptanceStatus → @{variables('varRiskAcceptanceStatus')}
  Text → RiskAcceptanceType → @{variables('varRiskAcceptanceType')}
  Text → ErrorCode → （空白）
  Text → ErrorMessage → （空白）

⚠ 重要：Rejected 不是系統錯誤，是正常的業務結果。
  StatusCode 用 400 而非 500，Status 用 Rejected 而非 Failed。
  GOV-002 根據 RiskAcceptanceStatus 判斷是否繼續。
```

> **Respond 的 StatusCode 判斷邏輯**：
> - Accepted → StatusCode = 200, Status = Success
> - Rejected → StatusCode = 400, Status = Rejected
> 可用 `If` 運算式：`if(equals(variables('varRiskAcceptanceStatus'),'Accepted'),200,400)`

**步驟 11：Catch-ErrorHandler Scope**

```
在 Try-MainLogic 下方（不是內部）：
  + 新增步驟 → Scope → 重新命名為「Catch-ErrorHandler」
  Configure run after：取消「成功」→ 勾選「已失敗」與「已逾時」

內部：
  a. Compose → 「Compose-ErrorMessage」
     Inputs：coalesce(result('Try-MainLogic')?[0]?['error']?['message'], '未知錯誤')

  b. Respond to a PowerApp or flow
     StatusCode → 500
     Status → Failed
     RiskAcceptanceStatus → （空白）
     RiskAcceptanceType → （空白）
     ErrorCode → ERR-004-SYSTEM
     ErrorMessage → Compose-ErrorMessage Outputs
```

**步驟 12：Save**

```
點擊右上角「儲存」→ 等待完成
```

### G. 必做設定檢核點

| 檢核項目 | 確認方式 | 預期結果 |
|:----------------------------------------------|:----------------------------------------------|:-------------------------------|
| Trigger 類型 | Trigger 卡片標題 | Manually trigger a flow |
| Input 參數 | Trigger → 2 個參數 | ProjectId(Text), HighestResidualRiskLevel(Text) |
| Low 路徑 | Switch Case Low | 不發 Approval，直接寫入 Accepted |
| Medium 收件人 | Approval_RiskOwner 的 Assigned to | 動態內容 gov_riskowner（非硬寫 Email） |
| High Layer2 收件人 | Approval_High_Layer2_Executive 的 Assigned to | GOV-ExecutiveManagement 群組 Email |
| Respond 欄位 | 所有 Respond 動作 | 都有 StatusCode, Status, RiskAcceptanceStatus, RiskAcceptanceType, ErrorCode, ErrorMessage |
| Catch Configure run after | Catch Scope 設定 | 成功未勾選，已失敗 + 已逾時已勾選 |
| Flow 名稱 | Flow 左上角 | `GOV-004 Risk Acceptance` |

### H. 最小驗證流程

**第 1 步：準備三筆測試專案**

```
在 Dataverse Project Registry 中準備：
  - 專案 A：gov_highestresidualrisklevel 由 GOV-013B 計算為 Low
  - 專案 B：gov_highestresidualrisklevel = Medium，gov_riskowner = 有效 Email
  - 專案 C：gov_highestresidualrisklevel = High，gov_riskowner = 有效 Email
```

**第 2 步：測試 Low 路徑（最簡單）**

```
1. 從 GOV-002 觸發 Gate3 申請（專案 A，Low 風險）
2. GOV-002 呼叫 GOV-013B → 回傳 Low → 呼叫 GOV-004
3. 開啟 GOV-004 Run History → 預期：
   ✓ Switch → Case Low
   ✓ Set variable (Accepted, AutoAccepted)
   ✓ Update Project Registry
   ✓ Respond (200, Accepted, AutoAccepted)
   ⊘ Catch-ErrorHandler（灰色跳過）
4. Dataverse 驗證：gov_riskacceptancestatus = 807660001, gov_riskowner = Auto-Accepted
```

**第 3 步：測試 Medium 路徑**

```
1. 觸發 Gate3 申請（專案 B，Medium 風險）
2. Risk Owner 收到 Approval 通知 → 點擊 Approve
3. Run History 預期：Switch → Case Medium → Approval → Approve → Update → Respond (200)
4. Dataverse 驗證：gov_riskacceptancestatus = 807660001, gov_riskowner = approver Email
```

**第 4 步：失敗時分類排查**

| Run History 畫面 | 分類 | 排查方式 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| Switch Case 正確，但 Approval 失敗 | **收件人問題** | 檢查 gov_riskowner 是否有值、Email 格式是否正確 |
| Approval 完成但 Update 失敗 | **Dataverse 寫入問題** | 確認 gov_riskacceptancestatus 欄位存在、OptionSet 值正確 |
| Switch 走到 Default（不匹配任何 Case） | **HighestResidualRiskLevel 值錯誤** | 確認 GOV-013B 回傳值為 `High`、`Medium`、`Low`（注意大小寫） |
| Catch 執行 | **系統例外** | 展開 Compose-ErrorMessage 看具體錯誤 |

### I. 常見失敗原因與對應排查路徑

| 編號 | 失敗現象 | 根因 | 排查路徑 |
|:----------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| I1 | Approval 失敗 `recipient not found` | Project Registry 的 gov_riskowner 為空 | Step 0 必檢 4 → 確認 Risk Owner Email 已填入 |
| I2 | Low 風險卻發了 Approval 通知 | Switch 的 Case 值大小寫不對（如 `low` vs `Low`） | 確認 GOV-013B 回傳值為 `Low`（首字母大寫） |
| I3 | High 風險 Layer 2 沒觸發 | Layer 1 Reject 後沒 Set variable 就跳出 | 確認 Reject 分支正確設定 varRiskAcceptanceStatus = Rejected |
| I4 | GOV-002 收到 GOV-004 回傳 Rejected 但報 500 | GOV-002 沒處理 GOV-004 的 Rejected 狀態 | 確認 GOV-002 步驟 13 有判斷 RiskAcceptanceStatus = Accepted 才繼續 |
| I5 | gov_riskowner 欄位被清空或被 `Auto-Accepted` 覆寫 | Low 路徑不應更新 gov_riskowner | 確認 Case Low 的 Update row 不包含 gov_riskowner 欄位；Low 路徑僅更新 gov_riskacceptancestatus 與 gov_riskacceptancecomments |
| I6 | Executive Group Approval 失敗 | GOV-ExecutiveManagement 非 Mail-enabled 或無成員 | Step 0 必檢 5 |
| I7 | Rejected 後 GOV-002 端顯示成功 | GOV-004 Respond 的 StatusCode 始終為 200 | 確認 Rejected 時 StatusCode = 400, Status = Rejected |
| I8 | Catch 報錯 `The specified row was not found` | ProjectId 無效（GOV-002 傳錯值） | 確認 GOV-002 傳入正確的 GUID 字串 |

---

## GOV-005：Document Upload and Register

### A. 基本資訊

| 項目 | 值 |
|:--------------------------|:--------------------------------------------------------------|
| Flow 名稱 | GOV-005 Document Upload and Register |
| 目的 | 接收 Base64 檔案上傳，寫入 SharePoint；以 **FileName 優先／DocumentType 備援** 雙軌模式識別文件身份，自動遞增整數版本號（`gov_versionnumber`），Supersede 含 Approved 舊版本，審核重啟由 GOV-018 自動偵測，回寫 Project Registry Link |
| Trigger 類型 | **Power Apps (V2)** |
| 觸發來源 | FORM-003 Document Upload Form（Power Apps），以 `GOV005DocumentUpload.Run(...)` 呼叫 |
| Connection References | CR-Dataverse-SPN, CR-SharePoint-SPN（MVP 模式可先用個人連線） |
| Concurrency Control | **必須開啟**（Key = ProjectId + DocumentType，Parallelism = 1） |
| 依賴 Child Flow | GOV-015（Notification Handler） |
| 對應測試案例 | 07文件 E2E-001 步驟 2.1, E2E-014, E2E-015, E2E-016 |

### Step 0：GOV-005 起手式必檢 13 項

> **為什麼需要 Step 0？** Base64 轉換出錯（多了 `data:...;base64,` 前綴）、SharePoint 路徑不存在、檔案大小超限 — 是 GOV-005 最常見的三大卡關原因。必檢 11~13 是 FileName 優先版本控制與文件清冊整合所需的 Schema 前置條件。

**必檢 1：Flow 在同一環境同一 Solution**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 確保 FORM-003 能看到 Flow |
| 操作路徑 | Maker Portal → 解決方案 → 確認 GOV-005 和 Canvas App 都在同一 Solution |
| 成功長相 | Solution 內同時看到 GOV-005 和 FORM-003 |
| 失敗長相 | Flow 或 App 不在清單中 |
| 下一步 | 在 Solution 內直接新建 Flow |

**必檢 2：Flow 被 App 加入**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 確保 Power Apps 知道要呼叫哪支 Flow |
| 操作路徑 | Power Apps Studio → 左側 Power Automate 圖示 → 確認 GOV-005 在已加入清單 |
| 成功長相 | 清單中看到 `GOV-005 Document Upload and Register` |
| 失敗長相 | 清單為空或找不到 |
| 下一步 | 點「+ 新增流程」→ 選 GOV-005 → 加入後發佈 App |

**必檢 3：Trigger 是 Power Apps (V2)**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 舊版 Trigger 不支援 Respond 回傳 |
| 操作路徑 | 開啟 GOV-005 → 檢查 Trigger 卡片標題 |
| 成功長相 | 標題顯示「Power Apps (V2)」 |
| 失敗長相 | 無 V2 字樣 |
| 下一步 | 刪除 Trigger → 重建為 Power Apps (V2) → 重新加入所有 9 個 Input 參數 |

**必檢 4：SharePoint Site 與 Document Library 存在**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | SharePoint Create file 的目標位置必須存在 |
| 操作路徑 | SharePoint → Design Governance Site → 文件庫 → 確認「Design Documents」存在 |
| 成功長相 | 文件庫存在且可開啟 |
| 失敗長相 | 404 或找不到文件庫 |
| 下一步 | 依 03 文件建立 SharePoint Site 與 Document Library |

**必檢 5：專案資料夾結構已建立（由 GOV-001 建立）**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | GOV-005 上傳的目標路徑為 `/Documents/{RequestId}/{TargetFolder}/`，其中 `{RequestId}` 資料夾由 GOV-001 建立 |
| 操作路徑 | SharePoint → Design Documents → 確認測試專案的資料夾存在（如 `DR-2026-0001/`）且子資料夾齊全 |
| 成功長相 | 看到 `01_Feasibility`、`02_Risk_Assessment`、`03_Design` 等子資料夾 |
| 失敗長相 | 專案資料夾不存在 |
| 下一步 | 先執行 GOV-001 建立專案（GOV-001 會自動建立 SharePoint 資料夾結構） |

**必檢 6：SharePoint Connection Reference 已授權**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | Create file (SharePoint) 需要 SharePoint 連線 |
| 操作路徑 | 開啟 GOV-005 → 找到 SharePoint Action → 檢查右上角 |
| 成功長相 | 無 ⚠️ 標記 |
| 失敗長相 | 有 ⚠️ |
| 下一步 | 點擊 → 選擇 CR-SharePoint-SPN（MVP 用個人帳號） |

**必檢 7：Document Baseline Matrix 有資料**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | GOV-005 從此資料表讀取 DocumentType → SharePoint 資料夾映射（P-13 原則） |
| 操作路徑 | Dataverse → 資料表 → Document Baseline Matrix → 開啟 → 確認有記錄 |
| 成功長相 | 有至少 15 筆記錄，每筆都有 gov_documenttypename 和 gov_sharepointfolder |
| 失敗長相 | 資料表為空 |
| 下一步 | 依 02 文件建立 Document Baseline Matrix 種子資料 |

**必檢 8：所有 Respond 的欄位集合完全一致（9 欄位）**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 成功（200）與失敗（400/500）的 Respond schema 不一致時會報 schema mismatch |
| 操作路徑 | 開啟 GOV-005 → 找到所有 Respond 動作 → 確認每個都有 9 個欄位：StatusCode、Status、ErrorCode、ErrorStage、Message、SharePointFileLink、DocumentRegisterRowId、FlowRunId、Timestamp |
| 成功長相 | 每個 Respond 都有完全相同的 9 個欄位 |
| 失敗長相 | 失敗 Respond 缺少 SharePointFileLink 或 DocumentRegisterRowId |
| 下一步 | 在失敗 Respond 中補上缺少的欄位，值填空白字串 |

**必檢 9：Concurrency Control 已開啟（Parallelism = 1）**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 同一專案同時上傳可能造成版本推進衝突 |
| 操作路徑 | Trigger → 設定 → 並行控制 |
| 成功長相 | 開啟，程度 = 1 |
| 失敗長相 | 關閉 |
| 下一步 | 開啟 → 程度 1 |

**必檢 10：所有 Input 參數型別皆為 Text**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | FileContent 是 Base64 字串，必須是 Text 類型 |
| 操作路徑 | Trigger → 檢查 9 個 Input 參數類型 |
| 成功長相 | 全部為 Text |
| 失敗長相 | 有參數使用 File 或 Binary 類型 |
| 下一步 | 刪除錯誤類型的參數 → 重新以 Text 類型加入 |

**必檢 11：Document Register 資料表有 `gov_filename` 欄位**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | FileName 優先查詢以此欄位作為篩選鍵；欄位不存在則雙軌查詢完全失效 |
| 操作路徑 | Maker Portal → Dataverse → 資料表 → Document Register → 資料行 → 確認有 `gov_filename`（文字，建議最多 500 字元） |
| 成功長相 | 資料行清單中看到 `gov_filename`，類型為「文字」 |
| 失敗長相 | 找不到 `gov_filename` |
| 下一步 | 資料行 → 新增資料行 → 顯示名稱「FileName」→ 名稱自動產生 `gov_filename` → 類型「文字」→ 儲存 |

**必檢 12：Document Register 資料表有版本號三欄位（Major / Minor / Label）**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | Major.Minor 版本號需要兩個整數欄位做運算，加一個文字欄位存顯示值（如「2.1」）；整數欄位不存在則 `add()` 報型別錯誤 |
| 操作路徑 | Maker Portal → Dataverse → 資料表 → Document Register → 資料行 → 確認有以下三欄位 |
| 欄位 1 | `gov_versionnumber_major`（整數）— 大版本號 |
| 欄位 2 | `gov_versionnumber_minor`（整數）— 小版本號 |
| 欄位 3 | `gov_versionlabel`（文字，建議 20 字元）— 顯示版本，如 `2.1` |
| 成功長相 | 三個欄位全部存在，類型正確 |
| 失敗長相 | 任一欄位缺失 |
| 下一步 | 資料行 → 新增資料行 → 三欄依序建立：`gov_versionnumber_major`（整數）、`gov_versionnumber_minor`（整數）、`gov_versionlabel`（文字）→ 儲存 |

**必檢 13：Document Register 資料表有 `gov_expectedfilename` 欄位**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | GOV-020 文件清冊解析後，將預期交付檔名存入此欄位；GOV-005 Phase 1B 用此欄位做 Planned 記錄匹配；欄位不存在則清冊整合完全無法運作 |
| 操作路徑 | Maker Portal → Dataverse → 資料表 → Document Register → 資料行 → 確認有 `gov_expectedfilename`（文字，建議最多 500 字元） |
| 成功長相 | 資料行清單中看到 `gov_expectedfilename`，類型為「文字」 |
| 失敗長相 | 找不到 `gov_expectedfilename` |
| 下一步 | 資料行 → 新增資料行 → 顯示名稱「ExpectedFileName」→ 類型「文字」→ 儲存 |

### B. 先決條件清單

| 先決條件 | 如何確認 |
|:--------------------------------------|:----------------------------------------------|
| SharePoint Site「Design Governance」已建立 | SharePoint → 確認 Site 存在 |
| Document Library「Design Documents」已建立 | Site → 確認文件庫存在 |
| 測試專案已由 GOV-001 建立（含 SharePoint 資料夾結構） | SharePoint → 確認 `DR-2026-xxxx/` 資料夾及子資料夾存在 |
| Document Baseline Matrix 已有種子資料 | Dataverse → 確認至少 15 筆記錄 |
| GOV-015 Notification Handler 已建立 | Flow 列表中 GOV-015 狀態為 On |
| CR-SharePoint-SPN 已授權 | 解決方案 → Connection References → 確認已連線 |

### Pre-check 清單

| Pre-check | 條件 | ErrorCode |
|:----------------------------------------------|:----------------------------------------------|:-------------------------------|
| 專案存在 | ProjectId 存在 | ERR-005-001 |
| 專案狀態 | ProjectStatus = Active | ERR-005-002 |
| 文件未凍結 | DocumentFreezeStatus ≠ Frozen | ERR-005-003 |
| 提交者權限 | SubmittedBy = SystemArchitect | ERR-005-004 |
| 檔案內容 | FileContent 非空白（Base64） | ERR-005-005 |
| DocumentType 有效 | DocumentType 存在於 gov_documenttype Choice | ERR-005-006 |

### DocumentType 與目標資料夾對應

> **重要**：此對應關係的**唯一權威來源**為 Doc 02 的 **Document Baseline Matrix**。
> 本 Flow 必須查閱該矩陣的 `SharePointFolder` 欄位決定上傳目標。
> 下表為快速參考副本，若有不一致以 Doc 02 Baseline Matrix 為準。

| DocumentType | 目標資料夾（SharePointFolder） |
|:----------------------------------------------|:----------------------------------------------|
| TechnicalFeasibility | 01_Feasibility |
| InitialRiskList | 01_Feasibility |
| RiskAssessmentStrategy | 01_Feasibility |
| DesignBaseline | 03_Design |
| RiskAssessment | 02_Risk_Assessment |
| IEC62443Checklist | 04_Security |
| ThreatModel | 04_Security |
| RequirementTraceability | 03_Design |
| TestPlan | 05_Test |
| TestReport | 05_Test |
| HandoverMeeting | 06_Handover |
| ResidualRiskList | 06_Handover |
| Other | 01_Feasibility |
| DesignObjectInventory | 03_Design |
| ChangeImpact | 03_Design |
| DocumentRegister | 06_Handover |

### Input 定義（Power Apps (V2) Trigger 參數）

在 Trigger 中以「+ Add an input」逐一新增以下參數：

| 參數名稱 | Input 類型 | 必填 | 說明 |
|:--------------------------|:----------------------|:------:|:----------------------------------------------|
| ProjectId | Text | ✓ | **Dataverse 的 gov_projectregistryid（GUID 字串）**，Power Apps 以 `Text(ThisItem.gov_projectregistryid)` 取得 |
| FileName | Text | ✓ | 上傳檔名（含副檔名），如 `DesignBaseline_v1.0.pdf` |
| FileContent | Text | ✓ | **Base64 編碼的檔案內容**（見下方限制說明） |
| DocumentType | Text | ✓ | TechnicalFeasibility / InitialRiskList / DesignBaseline / ... （見 DocumentType 對應表） |
| DocumentName | Text | ✓ | 文件顯示名稱 |
| DocumentVersion | Text | ✓ | 顯示用版本號（如 `v2.1`）；系統版本號由 `gov_versionnumber_major/minor` 自動管理 |
| **ChangeType** | Text | ✓ | **`Major`（大改版）或 `Minor`（小異動）**；決定 Major 版本遞增還是 Minor 版本遞增 |
| DeliverablePackage | Text | ✗ | CoreDeliverable / SupplementaryDeliverable / AdHoc（預設 CoreDeliverable） |
| Comments | Text | ✗ | 備註 |
| SubmittedBy | Text | ✓ | 提交者 Email |

### Base64 上傳限制（Power Apps 端必讀）

> **重要**：Power Apps 傳送 Base64 字串至 Flow 時，受限於 Power Automate 的 Request Size Limit。
> 超過限制會導致 Flow 呼叫直接失敗（Request Entity Too Large），且**不會觸發 Flow 內任何錯誤處理**。

| 限制項目 | 建議值 | 說明 |
|:----------------------------------------------|:-------------------------------|:----------------------------------------------|
| 單檔上限 | **10 MB**（Base64 前的原始大小） | Base64 編碼後約 13.3 MB，仍在 Power Automate 100 MB Request 限制內，但實測建議控制在 10 MB 以內 |
| 允許副檔名 | `.pdf`, `.docx`, `.xlsx`, `.pptx`, `.png`, `.jpg`, `.zip` | 禁止 `.exe`, `.bat`, `.cmd`, `.ps1`, `.vbs`, `.js` 等可執行檔 |
| Power Apps 端驗證 | 在 OnSelect **呼叫 Flow 之前**檢查 | 若超過大小或副檔名不合規，直接 `Notify()` 阻止，不呼叫 Flow |

> **Power Apps 端驗證範例**（在 FORM-003 的「上傳」按鈕 OnSelect 最前面加入）：
> ```
> // 檢查檔案大小（10 MB = 10485760 bytes）
> If(
>     First(AttachmentControl.Attachments).Size > 10485760,
>     Notify("檔案大小超過 10 MB 限制", NotificationType.Error);
>     false,
>     true
> )
> ```

### Output 定義（Respond to a PowerApp or flow — Canonical Error Envelope v5.0）

| 輸出參數 | 類型 | 說明 |
|:----------------------------------------------|:----------------------|:----------------------------------------------|
| StatusCode | Number | `200` / `400` / `500` |
| Status | Text | `Success` 或 `Failed` |
| ErrorCode | Text | 錯誤代碼（成功時為空白） |
| ErrorStage | Text | 失敗階段（成功時為空白） |
| Message | Text | 結果訊息 |
| SharePointFileLink | Text | 上傳後的 SharePoint 檔案 URL |
| DocumentRegisterRowId | Text | Document Register 記錄 GUID |
| FlowRunId | Text | `workflow()?['run']?['name']`，用於端對端追溯 |
| Timestamp | Text | `utcNow()`，回應時間戳記 |

### 文件身份識別模型（FileName 優先雙軌架構）

> **設計背景**：治理系統除 Gate 規定的強制文件（以 DocumentType 定義 Slot）外，也接收各專案不同的設計產出文件。
> 設計產出文件的名稱因專案而異，無法以 DocumentType 唯一識別同一份文件，必須以 **FileName** 作為主鍵。

#### 雙軌查詢流程圖

```
上傳觸發
    │
    ▼
Phase 1：以 FileName 查詢 Document Register
  └─ filter: 同 ProjectId + gov_filename eq FileName + 非 Superseded
    │
    ├─ [命中] → 版本推進路徑 A（FileName 更新）
    │           VersionNumber = max現有版本 + 1
    │           Supersede 所有命中記錄（含 Approved）
    │           MatchedByFileName = true
    │           → 步驟 7 建立新記錄（Draft, VersionNumber, FileName）
    │           → GOV-018 自動偵測 Approved 消失 → 觸發審核重啟通知
    │
    └─ [未命中] → Phase 1B：查詢 gov_expectedfilename（GOV-020 預建 Planned 記錄）
                  filter: 同 ProjectId + gov_expectedfilename eq FileName + role = Planned
                  │
                  ├─ [命中] → 版本路徑 C（首次實際交付，升級 Planned → Draft）
                  │           MajorVersion = 1, MinorVersion = 0（versionlabel = "1.0"）
                  │           不執行 Supersede（直接更新 Planned 記錄）
                  │           → 步驟 7 UPDATE 現有 Planned 記錄為 Draft
                  │
                  └─ [未命中] → Phase 2：以 DocumentType 查詢（治理文件 Slot 模式）
                                filter: 同 ProjectId + gov_documenttype OptionSet + 非 Superseded
                                │
                                ├─ [命中] → 版本推進路徑 B（DocType 更新）
                                │           MajorVersion/MinorVersion = max + 1（依 ChangeType）
                                │           Supersede 所有命中記錄（含 Approved）
                                │           → 步驟 7 新增 Draft 記錄
                                │
                                └─ [未命中] → Phase 3：全新文件
                                              MajorVersion = 1, MinorVersion = 0
                                              → 步驟 7 新增第一筆記錄
```

#### 關鍵設計決策

| 決策項 | 採用方案 | 理由 |
|:-------------------------------|:----------------------------------------------|:----------------------------------------------|
| **D1 身份主鍵** | FileName 優先（Phase 1），ExpectedFileName 次之（Phase 1B），DocumentType 備援（Phase 2） | 設計產出文件必須以 FileName 識別；清冊預建的 Planned 記錄以 ExpectedFileName 銜接；治理 Gate 文件以 DocumentType Slot 管理 |
| **D2 版本號** | Major.Minor 雙整數（`gov_versionnumber_major` + `gov_versionnumber_minor`），`gov_versionlabel` 存顯示值（如 `2.1`），`gov_documentversion` 仍保留使用者輸入 | 整數可精確加法，浮點數不可靠；ChangeType 參數決定遞增哪一位 |
| **D3 大小寫** | OData `eq` 對 Dataverse 文字欄位預設大小寫不敏感；`trim()` 去除前後空格 | 防止 `Design.pdf` 與 `design.pdf` 建立重複記錄 |
| **D4 跨 DocumentType 同 FileName** | Phase 1 FileName 優先，命中即視為同一文件 | 相同檔名即使切換 DocumentType 也視為版本更新，不建立獨立文件線 |
| **D5 Approved 也 Supersede** | 是，Approved 記錄也納入 Supersede 範圍 | 審核也要重新來——新版本上傳後舊版 Approved 失效，GOV-018 自動偵測合規缺口並觸發重審 |
| **D6 Phase 1B 不 Supersede** | Phase 1B 命中 Planned 記錄時，直接 UPDATE 升級（不 Supersede + 新建）| Planned 記錄是空殼，沒有舊版本可 Supersede；直接升級保留同一 Row ID |

#### 審核重啟機制說明

> **「審核也要重新來」的實現方式**：
> 1. 新版本上傳 → Step 6 將舊 Approved 記錄改為 Superseded（`gov_documentrole = 807660003`）
> 2. 新 Draft 記錄建立（`gov_documentrole = 807660001`）— 尚未審核
> 3. **GOV-018 Compliance Monitor**（定時執行）偵測到：該 DocumentType 的 Approved 記錄消失
> 4. GOV-018 將對應 Gate 標記為 `ComplianceAlert` → 通知 System Architect 重新提交審核
> 5. 不需要在 GOV-005 內直接修改 Review Decision Log（避免過度耦合，由 GOV-018 統一協調）

### 建立步驟（逐步點擊）

**步驟 1**：建立 Power Apps (V2) Trigger
```
1. 在 Solution 內新增 Cloud flow → 自動化
2. 搜尋 power apps → 選擇「Power Apps (V2)」Trigger
3. 逐一新增 input 參數：
   + Add an input → Text → ProjectId
   + Add an input → Text → FileName
   + Add an input → Text → FileContent
   + Add an input → Text → DocumentType
   + Add an input → Text → DocumentName
   + Add an input → Text → DocumentVersion
   + Add an input → Text → ChangeType
   + Add an input → Text → DeliverablePackage
   + Add an input → Text → Comments
   + Add an input → Text → SubmittedBy
4. 開啟 Concurrency Control：
   點擊 Trigger 右上角「...」→「設定」→ 並行控制 → 開啟 → 程度 1
```

**步驟 2**：Initialize variables（必須在 Trigger 正下方，Flow 最頂層）
```
Action：Initialize variable
  （搜尋 initialize → 選擇「Variable」下的「Initialize variable」，中文為「初始化變數」）
  Name：TargetFolder
  Type：String
  Value：（空白）

Action：Initialize variable
  Name：NewDocumentId
  Type：String
  Value：（空白）

Action：Initialize variable
  Name：MajorVersion
  Type：Integer
  Value：1
  說明：Major 版本號（重大改版 +1，小改版不變；全新文件初始為 1）

Action：Initialize variable
  Name：MinorVersion
  Type：Integer
  Value：0
  說明：Minor 版本號（小改版 +1，重大改版歸零；全新文件初始為 0）
       → 第一版永遠顯示為 1.0

Action：Initialize variable
  Name：MatchedByFileName
  Type：Boolean
  Value：false
  說明：記錄是否由 Phase 1 FileName 查詢命中（影響 Step 7A SupersededBy 回填路徑）

Action：Initialize variable
  Name：MatchedByExpectedFileName
  Type：Boolean
  Value：false
  說明：記錄是否由 Phase 1B ExpectedFileName 查詢命中（影響 Step 7 選擇 Update 還是 Add）

Action：Initialize variable
  Name：PlannedRecordId
  Type：String
  Value：（空白）
  說明：Phase 1B 命中時存入 Planned 記錄的 GUID，供 Step 7 直接 UPDATE（不 Add new row）

Action：Initialize variable
  Name：SupersededIds
  Type：Array
  Value：[]
  （Value 欄位：點擊「表達式」模式 → 輸入 [] → 確認）
  說明：收集步驟 6 中被 Supersede 的所有記錄 GUID，供步驟 7A 回填 gov_supersededby
```

**步驟 3**：Pre-check（驗證專案狀態）
```
Action：Get a row by ID (Dataverse)
  （搜尋 get a row → 選擇「Microsoft Dataverse」下的「Get a row by ID」，中文為「依識別碼取得資料列」）
  連線：CR-Dataverse-SPN（MVP 模式：個人連線）
  Table name：Project Registry
  Row ID：@{triggerBody()['ProjectId']}

Action：Condition（專案狀態檢查）
  （搜尋 condition → 選擇「控制項」下的「Condition」，中文可能為「條件」）
  條件（全部為 AND）：
  - outputs('Get_Project')?['body/gov_projectstatus'] eq 807660000（Active）
  - outputs('Get_Project')?['body/gov_documentfreezestatus'] ne 807660001（Frozen）
  - triggerBody()['FileContent'] is not empty

  False 分支：
    Action：Respond to a PowerApp or flow
      StatusCode: 400, Status: Failed, ErrorCode: ERR-005-002/003/005,
      ErrorStage: PreCheck,
      Message: 專案非 Active/已凍結/檔案空白,
      SharePointFileLink: (空), DocumentRegisterRowId: (空),
      FlowRunId: @{workflow()?['run']?['name']}, Timestamp: @{utcNow()}
    Action：Terminate
      （搜尋 terminate → 選擇「控制項」下的「Terminate」，中文為「終止」）
      Status：Cancelled
    ⚠ 每個 Respond Failed 都必須包含完整 Error Envelope：StatusCode, Status, ErrorCode, ErrorStage, Message, FlowRunId, Timestamp（v5.0）
```

**步驟 4**：解析 SharePointFolder（P-11 + P-13 原則：從 Dataverse 讀取，不得硬寫）
```
說明：禁止在 Flow 中以 Switch 硬編碼 DocumentType → 資料夾的映射（P-13 原則）。
     必須從 Dataverse「Document Baseline Matrix」讀取 SharePointFolder 欄位。

Action：List rows (Dataverse)
  （搜尋 list rows → 選擇「Microsoft Dataverse」下的「List rows」，中文為「列出資料列」）
  連線：CR-Dataverse-SPN
  Table name：Document Baseline Matrix
  Filter rows：gov_documenttypename eq '@{triggerBody()['DocumentType']}'
  Row count：1
  重新命名為「Lookup_FolderMapping」

Action：Condition（驗證 DocumentType 映射存在）
  （搜尋 condition → 選擇「控制項」下的「Condition」，中文可能為「條件」）
  條件：length(outputs('Lookup_FolderMapping')?['body/value']) is equal to 0

  True 分支：
    Respond to a PowerApp or flow →
    StatusCode: 400, Status: Failed, ErrorCode: ERR-005-006,
    ErrorStage: DocumentValidation,
    Message: 無效的 DocumentType 值, FlowRunId: @{workflow()?['run']?['name']},
    Timestamp: @{utcNow()}
    Terminate → Cancelled

Action：Set variable
  Name：TargetFolder
  Value：@{first(outputs('Lookup_FolderMapping')?['body/value'])?['gov_sharepointfolder']}

注意：Document Baseline Matrix 的 gov_sharepointfolder 欄位即為目標資料夾名稱
     （如 01_Feasibility, 02_Risk_Assessment 等）。
     若業務需新增 DocumentType 或變更資料夾對應，僅需修改 Dataverse 資料表，無需修改 Flow。
```

**步驟 5**：上傳檔案至 SharePoint
```
Action：Create file (SharePoint)
  （搜尋 create file → 選擇「SharePoint」下的「Create file」，中文為「建立檔案」）
  連線：CR-SharePoint-SPN（MVP 模式：個人連線）
  Site Address：選擇 Design Governance Site
  Folder Path：/Documents/@{outputs('Get_Project')?['body/gov_requestid']}/@{variables('TargetFolder')}
  File Name：@{triggerBody()['FileName']}
  File Content：@{base64ToBinary(triggerBody()['FileContent'])}

Action：Compose（取得 SharePoint URL）
  （搜尋 compose → 選擇「資料作業」下的「Compose」，中文可能為「撰寫」）
  重新命名為「SharePointFileURL」
  Inputs：@{outputs('Create_file')?['body/{Link}']}
```

**步驟 6**：文件身份識別與版本推進（FileName 優先雙軌模式）
```
設計說明：
  Phase 1（FileName 主鍵查詢）：
    同專案下 gov_filename 完全相符且非 Superseded 的所有記錄
    → 命中：所有記錄（含 Approved）全部 Supersede → ChangeType 決定 Major+1 或 Minor+1
    → MatchedByFileName = true → 審核重啟由 GOV-018 偵測 Approved 消失後自動觸發

  Phase 1B（ExpectedFileName 查詢，僅 Phase 1 無命中時執行）：
    GOV-020 文件清冊預建的 Planned 記錄（gov_expectedfilename 欄位）
    → 命中：MajorVersion = 1, MinorVersion = 0 → 直接升級 Planned → Draft（不 Supersede）
    → MatchedByExpectedFileName = true，PlannedRecordId 記錄 GUID

  Phase 2（DocumentType 備援，僅 Phase 1 和 1B 均無命中時執行）：
    同專案下同 DocumentType 且非 Superseded 的所有記錄
    → 命中：所有記錄（含 Approved）全部 Supersede → ChangeType 決定 Major+1 或 Minor+1

  Phase 3（三者均無命中）：
    全新文件，MajorVersion = 1、MinorVersion = 0（初始值），不需 Supersede 任何記錄

⚠ Dataverse OData 對文字欄位的 eq 比較預設大小寫不敏感（'Design.pdf' 等同 'design.pdf'）
⚠ trim() 去除 FileName 首尾空格，防止因空格不同而建立重複記錄

--- Phase 1：FileName 主鍵查詢 ---

Action：List rows (Dataverse)
  （搜尋 list rows → 選擇「Microsoft Dataverse」下的「List rows」，中文為「列出資料列」）
  Table name：Document Register
  Filter rows：_gov_parentproject_value eq '@{triggerBody()['ProjectId']}'
               and gov_filename eq '@{trim(triggerBody()['FileName'])}'
               and gov_documentrole ne 807660003
  Order By：gov_versionnumber desc
  重新命名為「Lookup_ByFileName」

Action：Condition（Phase 1 — FileName 有命中？）
  （搜尋 condition → 選擇「控制項」下的「Condition」）
  條件：length(outputs('Lookup_ByFileName')?['body/value']) greater than 0

  ┌─ True 分支（FileName 命中 → 版本推進路徑 A）：

    // 1. 取得現有 Major / Minor 版本號（null 防護）
    Action：Compose
      重新命名為「Compose-CurrentMajor-Phase1」
      Inputs：@{coalesce(first(outputs('Lookup_ByFileName')?['body/value'])?['gov_versionnumber_major'], 1)}
      說明：取現有最高 Major 版本號；null（舊記錄無此欄位）預設 1

    Action：Compose
      重新命名為「Compose-CurrentMinor-Phase1」
      Inputs：@{coalesce(first(outputs('Lookup_ByFileName')?['body/value'])?['gov_versionnumber_minor'], 0)}
      說明：取現有 Minor 版本號；null 預設 0

    // 2. 根據 ChangeType 決定新版本號
    Action：Condition（ChangeType = Major？）
      （搜尋 condition → 選擇「控制項」下的「Condition」）
      條件：triggerBody()['ChangeType'] is equal to 'Major'

      True 分支（重大改版 → Major +1，Minor 歸零）：
        Action：Set variable → Name：MajorVersion → Value：@{add(outputs('Compose-CurrentMajor-Phase1'), 1)}
        Action：Set variable → Name：MinorVersion → Value：0

      False 分支（小幅修訂 → Minor +1，Major 不變）：
        Action：Set variable → Name：MajorVersion → Value：@{outputs('Compose-CurrentMajor-Phase1')}
        Action：Set variable → Name：MinorVersion → Value：@{add(outputs('Compose-CurrentMinor-Phase1'), 1)}

    Action：Set variable → Name：MatchedByFileName → Value：true

    // 3. Supersede 所有命中記錄（含 Approved）
    Action：Apply to each
      （搜尋 apply to each → 選擇「控制項」下的「Apply to each」，中文為「套用至每一個」）
      Output From：outputs('Lookup_ByFileName')?['body/value']
      重新命名為「ForEach-Supersede-Phase1」

      Action：Update a row (Dataverse)
        （搜尋 update a row → 選擇「Microsoft Dataverse」下的「Update a row」）
        Table name：Document Register
        Row ID：@{items('ForEach-Supersede-Phase1')?['gov_documentregisterid']}
        欄位對應：
          gov_documentrole：807660003（Superseded）
          gov_supersededdate：@{utcNow()}

      Action：Append to array variable
        （搜尋 append to array variable → 選擇「Variable」下的「Append to array variable」）
        Name：SupersededIds
        Value：@{items('ForEach-Supersede-Phase1')?['gov_documentregisterid']}

  └─ False 分支（Phase 1 無命中 → 進入 Phase 1B ExpectedFileName 查詢）：

    // Phase 1B：查詢 GOV-020 文件清冊預建的 Planned 記錄
    Action：List rows (Dataverse)
      （搜尋 list rows → 選擇「Microsoft Dataverse」下的「List rows」）
      Table name：Document Register
      Filter rows：_gov_parentproject_value eq '@{triggerBody()['ProjectId']}'
                   and gov_expectedfilename eq '@{trim(triggerBody()['FileName'])}'
                   and gov_documentrole eq 807660000
      重新命名為「Lookup_ByExpectedFileName」
      說明：僅查 Planned（807660000）；這些是 GOV-020 預建的空殼記錄，等待第一次實際上傳

    Action：Condition（Phase 1B — ExpectedFileName 有命中？）
      條件：length(outputs('Lookup_ByExpectedFileName')?['body/value']) greater than 0

      ┌─ True 分支（Phase 1B 命中 → 首次實際交付，升級 Planned → Draft）：

          // MajorVersion = 1, MinorVersion = 0 保持初始值（第一次交付永遠是 1.0）
          // ChangeType 在此路徑無效（沒有舊版本可做 Minor 遞增）
          Action：Set variable → Name：MatchedByExpectedFileName → Value：true
          Action：Set variable
            Name：PlannedRecordId
            Value：@{first(outputs('Lookup_ByExpectedFileName')?['body/value'])?['gov_documentregisterid']}
          說明：不執行 Supersede；不 Append 到 SupersededIds；步驟 7 直接 UPDATE 此 Planned 記錄

          ✅ [已修正 BUG-020-A] Phase 1B 文件類型一致性驗證

          Action：Compose
            重新命名為「Compose-DocTypeInt-Phase1B」
            Inputs：運算式 →
            if(equals(triggerBody()?['DocumentType'], 'TechnicalFeasibility'), 807660000,
            if(equals(triggerBody()?['DocumentType'], 'InitialRiskList'), 807660001,
            if(equals(triggerBody()?['DocumentType'], 'RiskAssessmentStrategy'), 807660002,
            if(equals(triggerBody()?['DocumentType'], 'DesignBaseline'), 807660003,
            if(equals(triggerBody()?['DocumentType'], 'RiskAssessment'), 807660004,
            if(equals(triggerBody()?['DocumentType'], 'IEC62443Checklist'), 807660005,
            if(equals(triggerBody()?['DocumentType'], 'ThreatModel'), 807660006,
            if(equals(triggerBody()?['DocumentType'], 'RequirementTraceability'), 807660007,
            if(equals(triggerBody()?['DocumentType'], 'TestPlan'), 807660008,
            if(equals(triggerBody()?['DocumentType'], 'TestReport'), 807660009,
            if(equals(triggerBody()?['DocumentType'], 'HandoverMeeting'), 807660010,
            if(equals(triggerBody()?['DocumentType'], 'ResidualRiskList'), 807660011,
            if(equals(triggerBody()?['DocumentType'], 'Other'), 807660012,
            if(equals(triggerBody()?['DocumentType'], 'DesignObjectInventory'), 807660013,
            if(equals(triggerBody()?['DocumentType'], 'ChangeImpact'), 807660014,
            if(equals(triggerBody()?['DocumentType'], 'DocumentRegister'), 807660015,
            -1))))))))))))))))
            說明：將 Trigger 輸入的 DocumentType 文字轉換為 OptionSet 整數，
                 供後續 Condition-DocTypeMatch 與 Update_PlannedToDraft gov_documenttype 欄位使用

          Action：Condition（文件類型與清冊定義一致？）
            重新命名為「Condition-DocTypeMatch」
            條件：outputs('Compose-DocTypeInt-Phase1B') is equal to
                  first(outputs('Lookup_ByExpectedFileName')?['body/value'])?['gov_documenttype']
            （比對上傳者宣告的 DocumentType OptionSet 整數 vs Planned 記錄中 GOV-020 定義的類型）

            False 分支（文件類型不符 → 拒絕上傳）：
              Respond to a PowerApp or flow
                StatusCode：400
                Status：Failed
                ErrorCode：ERR-005-019
                ErrorStage：DocumentTypeValidation
                ErrorMessage：上傳文件的類型（DocumentType）與文件清冊中的定義不符。
                              清冊定義類型：@{first(outputs('Lookup_ByExpectedFileName')?['body/value'])?['gov_documenttype']}
                              上傳宣告類型：@{outputs('Compose-DocTypeInt-Phase1B')}
                              請確認文件類型後重新上傳，或聯繫 PM 確認清冊定義是否正確。
                ReviewRowId：""
                FlowRunId：workflow()?['run']?['name']
                Timestamp：utcNow()
              + Terminate（Cancelled）

            True 分支：類型一致，繼續升級 Planned → Draft

      └─ False 分支（Phase 2 — DocumentType 備援查詢）：

          ✅ [已修正 BUG-010] Phase 2 前置步驟：動態解析 DocumentType → OptionSet 整數

          Action：Compose
            重新命名為「Compose-DocTypeInt」
            Inputs：運算式 →
            if(equals(triggerBody()?['DocumentType'], 'TechnicalFeasibility'), 807660000,
            if(equals(triggerBody()?['DocumentType'], 'InitialRiskList'), 807660001,
            if(equals(triggerBody()?['DocumentType'], 'RiskAssessmentStrategy'), 807660002,
            if(equals(triggerBody()?['DocumentType'], 'DesignBaseline'), 807660003,
            if(equals(triggerBody()?['DocumentType'], 'RiskAssessment'), 807660004,
            if(equals(triggerBody()?['DocumentType'], 'IEC62443Checklist'), 807660005,
            if(equals(triggerBody()?['DocumentType'], 'ThreatModel'), 807660006,
            if(equals(triggerBody()?['DocumentType'], 'RequirementTraceability'), 807660007,
            if(equals(triggerBody()?['DocumentType'], 'TestPlan'), 807660008,
            if(equals(triggerBody()?['DocumentType'], 'TestReport'), 807660009,
            if(equals(triggerBody()?['DocumentType'], 'HandoverMeeting'), 807660010,
            if(equals(triggerBody()?['DocumentType'], 'ResidualRiskList'), 807660011,
            if(equals(triggerBody()?['DocumentType'], 'Other'), 807660012,
            if(equals(triggerBody()?['DocumentType'], 'DesignObjectInventory'), 807660013,
            if(equals(triggerBody()?['DocumentType'], 'ChangeImpact'), 807660014,
            if(equals(triggerBody()?['DocumentType'], 'DocumentRegister'), 807660015,
            -1))))))))))))))))
            （-1 = 未知 DocumentType → Phase 3 新文件路徑）

          Action：Condition（DocumentType 有效？）
            重新命名為「Condition-ValidDocType」
            條件：outputs('Compose-DocTypeInt') is not equal to -1
            False → 直接跳至 Phase 3（此 DocumentType 未在 Baseline Matrix 定義，視為全新文件）

          Action：List rows (Dataverse)
            Table name：Document Register
            Filter rows：_gov_parentproject_value eq '@{triggerBody()['ProjectId']}'
                         and gov_documenttype eq @{outputs('Compose-DocTypeInt')}
                         and gov_documentrole ne 807660003
            Order By：gov_versionnumber_major desc, gov_versionnumber_minor desc
            重新命名為「Lookup_ByDocType」
            說明：使用 Compose-DocTypeInt 動態取得整數值，不硬編碼（遵守 P-13）；
                 gov_documentrole ne 807660003 已排除 Superseded（Planned 包含在內）

          Action：Condition（Phase 2 — DocumentType 有命中？）
            條件：length(outputs('Lookup_ByDocType')?['body/value']) greater than 0

            ┌─ True 分支（DocumentType 命中 → 版本推進路徑 B）：

                Action：Compose
                  重新命名為「Compose-CurrentMajor-Phase2」
                  Inputs：@{coalesce(first(outputs('Lookup_ByDocType')?['body/value'])?['gov_versionnumber_major'], 1)}

                Action：Compose
                  重新命名為「Compose-CurrentMinor-Phase2」
                  Inputs：@{coalesce(first(outputs('Lookup_ByDocType')?['body/value'])?['gov_versionnumber_minor'], 0)}

                Action：Condition（ChangeType = Major？）
                  條件：triggerBody()['ChangeType'] is equal to 'Major'
                  True：Set MajorVersion = @{add(outputs('Compose-CurrentMajor-Phase2'), 1)}, Set MinorVersion = 0
                  False：Set MajorVersion = @{outputs('Compose-CurrentMajor-Phase2')}, Set MinorVersion = @{add(outputs('Compose-CurrentMinor-Phase2'), 1)}

                Action：Apply to each
                  Output From：outputs('Lookup_ByDocType')?['body/value']
                  重新命名為「ForEach-Supersede-Phase2」

                  Action：Update a row (Dataverse)
                    Table name：Document Register
                    Row ID：@{items('ForEach-Supersede-Phase2')?['gov_documentregisterid']}
                    欄位對應：
                      gov_documentrole：807660003（Superseded）
                      gov_supersededdate：@{utcNow()}

                  Action：Append to array variable
                    Name：SupersededIds
                    Value：@{items('ForEach-Supersede-Phase2')?['gov_documentregisterid']}

            └─ False 分支（Phase 3 — 全新文件，三者均無命中）：

                Action：Compose
                  重新命名為「Compose-NewDocumentFlag」
                  Inputs：true
                  說明：Run History 標記用；MajorVersion=1, MinorVersion=0（初始值）；無需 Supersede

注意：Phase 1 和 Phase 2 的 Filter 均含 gov_documentrole ne 807660003（排除 Superseded），
     但 Planned（807660000）會被包含進來。若 Phase 1 命中 Planned 記錄（理論上不應發生，
     因為 Planned 記錄的 gov_filename 應為 null），同樣 Supersede 並在步驟 7 新建 Draft。
     Phase 1B 已精確篩選 role = 807660000 的 Planned 記錄，兩者不會重複命中。
```

**步驟 6.9**：解析 DeliverablePackage → OptionSet 整數（路徑 A / B 共用前置步驟）
```
✅ [已修正 GAP-005-A] 將 Trigger 輸入的 DeliverablePackage 文字轉換為 OptionSet 整數，
   供步驟 7 路徑 A（Update_PlannedToDraft）與路徑 B（Add_DocumentRegister）共用

+ 新增步驟 → Compose
  重新命名為「Compose-DeliverablePackageInt」
  位置：步驟 6 結尾（步驟 7 Condition 之前，Phase 分叉之外）
  Inputs：運算式 →
  if(equals(triggerBody()?['DeliverablePackage'], 'CoreDeliverable'), 807660000,
  if(equals(triggerBody()?['DeliverablePackage'], 'SupplementaryDeliverable'), 807660001,
  if(equals(triggerBody()?['DeliverablePackage'], 'AdHoc'), 807660002,
  807660000)))
  （預設 807660000 = CoreDeliverable；未填寫或未知值均視為 CoreDeliverable）

  對照表：
    CoreDeliverable        → 807660000（主要交付文件）
    SupplementaryDeliverable → 807660001（輔助交付文件）
    AdHoc                  → 807660002（臨時性文件）
    （空白 / 未知）          → 807660000（預設 CoreDeliverable）

> 此步驟必須放在步驟 7 的 Condition（MatchedByExpectedFileName = true）**之前**，
> 確保無論進入路徑 A 還是路徑 B，outputs('Compose-DeliverablePackageInt') 均已就緒。
> 對應 GOV-020 的 Compose-DeliverablePackageInt（相同映射邏輯，此處為 GOV-005 獨立實例）。
```

**步驟 7**：建立/更新 Document Register 記錄（Draft）
```
說明：步驟 7 根據步驟 6 的結果分兩條路徑：
  路徑 A（MatchedByExpectedFileName = true）：Phase 1B 命中 Planned 記錄
    → UPDATE 現有 Planned 記錄為 Draft，填入實際檔案資訊
    → 保留同一 Row ID（不新建記錄）
  路徑 B（其他所有情況）：Phase 1 / Phase 2 / Phase 3
    → ADD a new row 作為新 Draft 記錄

Action：Condition（Path A — Phase 1B Planned 升級路徑？）
  （搜尋 condition → 選擇「控制項」下的「Condition」）
  條件：variables('MatchedByExpectedFileName') is equal to true

  ┌─ True 分支（路徑 A：UPDATE 現有 Planned 記錄 → Draft）：

      Action：Update a row (Dataverse)
        （搜尋 update a row → 選擇「Microsoft Dataverse」下的「Update a row」）
        連線：CR-Dataverse-SPN（MVP 模式：個人連線）
        Table name：Document Register
        Row ID：@{variables('PlannedRecordId')}
        重新命名為「Update_PlannedToDraft」
        欄位對應：
          gov_documentname：@{triggerBody()['DocumentName']}
          gov_documentversion：@{triggerBody()['DocumentVersion']}
          gov_filename：@{trim(triggerBody()['FileName'])}
          gov_versionnumber_major：@{variables('MajorVersion')}
          gov_versionnumber_minor：@{variables('MinorVersion')}
          gov_versionlabel：@{concat(variables('MajorVersion'), '.', variables('MinorVersion'))}
          gov_sharepointfilelink：@{outputs('SharePointFileURL')}
          gov_uploadedby：@{triggerBody()['SubmittedBy']}
          gov_uploadeddate：@{utcNow()}
          gov_documentrole：807660001（Draft）
          gov_documenttype：@{outputs('Compose-DocTypeInt-Phase1B')}  ✅ [已修正 BUG-020-B]
          gov_deliverablepackage：@{outputs('Compose-DeliverablePackageInt')}  ✅ [已修正 GAP-005-A]
          gov_comments：@{triggerBody()['Comments']}
        說明：gov_documenttype 由 Compose-DocTypeInt-Phase1B 提供（BUG-020 修正）；
             gov_deliverablepackage 由步驟 6.9 的 Compose-DeliverablePackageInt 提供（GAP-005-A 修正）。

      Action：Set variable
        Name：NewDocumentId
        Value：@{variables('PlannedRecordId')}
        說明：Planned 記錄已升級為 Draft，Row ID 不變

  └─ False 分支（路徑 B：ADD 新 Draft 記錄）：

      ✅ [已修正 GAP-005-B] 路徑 B 前置步驟：解析 DocumentType → OptionSet 整數

      Action：Compose
        重新命名為「Compose-DocTypeInt-PathB」
        位置：Add_DocumentRegister 之前（False 分支最頂端）
        Inputs：運算式 →
        if(equals(triggerBody()?['DocumentType'], 'TechnicalFeasibility'), 807660000,
        if(equals(triggerBody()?['DocumentType'], 'InitialRiskList'), 807660001,
        if(equals(triggerBody()?['DocumentType'], 'RiskAssessmentStrategy'), 807660002,
        if(equals(triggerBody()?['DocumentType'], 'DesignBaseline'), 807660003,
        if(equals(triggerBody()?['DocumentType'], 'RiskAssessment'), 807660004,
        if(equals(triggerBody()?['DocumentType'], 'IEC62443Checklist'), 807660005,
        if(equals(triggerBody()?['DocumentType'], 'ThreatModel'), 807660006,
        if(equals(triggerBody()?['DocumentType'], 'RequirementTraceability'), 807660007,
        if(equals(triggerBody()?['DocumentType'], 'TestPlan'), 807660008,
        if(equals(triggerBody()?['DocumentType'], 'TestReport'), 807660009,
        if(equals(triggerBody()?['DocumentType'], 'HandoverMeeting'), 807660010,
        if(equals(triggerBody()?['DocumentType'], 'ResidualRiskList'), 807660011,
        if(equals(triggerBody()?['DocumentType'], 'Other'), 807660012,
        if(equals(triggerBody()?['DocumentType'], 'DesignObjectInventory'), 807660013,
        if(equals(triggerBody()?['DocumentType'], 'ChangeImpact'), 807660014,
        if(equals(triggerBody()?['DocumentType'], 'DocumentRegister'), 807660015,
        null))))))))))))))))
        說明：路徑 B 包含 Phase 1（FileName 命中）、Phase 2（DocType 命中）、Phase 3（全新文件）。
             Phase 1 路徑從未執行 Compose-DocTypeInt，故需在此處獨立計算。
             Phase 3（未知 DocumentType）回傳 null → gov_documenttype 寫入 null（Dataverse 空值）。
             此處用 null（非 -1）以確保 Dataverse 欄位接受空值而不是無效整數。

      Action：Add a new row (Dataverse)
        （搜尋 add a new row → 選擇「Microsoft Dataverse」下的「Add a new row」，中文為「新增資料列」）
        連線：CR-Dataverse-SPN（MVP 模式：個人連線）
        Table name：Document Register
        重新命名為「Add_DocumentRegister」
        欄位對應：
          gov_documentid：@{concat('DOC-', outputs('Get_Project')?['body/gov_requestid'], '-', triggerBody()['DocumentType'], '-', formatDateTime(utcNow(), 'yyyyMMddHHmmss'))}
          gov_parentproject：@{triggerBody()['ProjectId']}
          gov_documenttype：@{outputs('Compose-DocTypeInt-PathB')}  ✅ [已修正 GAP-005-B]
          gov_documentname：@{triggerBody()['DocumentName']}
          gov_documentversion：@{triggerBody()['DocumentVersion']}
          gov_filename：@{trim(triggerBody()['FileName'])}
          gov_versionnumber_major：@{variables('MajorVersion')}
          gov_versionnumber_minor：@{variables('MinorVersion')}
          gov_versionlabel：@{concat(variables('MajorVersion'), '.', variables('MinorVersion'))}
          gov_sharepointfilelink：@{outputs('SharePointFileURL')}
          gov_uploadedby：@{triggerBody()['SubmittedBy']}
          gov_uploadeddate：@{utcNow()}
          gov_documentrole：807660001（Draft）
          gov_deliverablepackage：@{outputs('Compose-DeliverablePackageInt')}  ✅ [已修正 GAP-005-A]
          gov_requiredforgate：（從 Baseline Matrix 對應，或留空）
          gov_isfrozen：false
          gov_comments：@{triggerBody()['Comments']}

      Action：Set variable
        Name：NewDocumentId
        Value：@{outputs('Add_DocumentRegister')?['body/gov_documentregisterid']}

說明（gov_versionlabel）：concat(MajorVersion, '.', MinorVersion) → "1.0", "2.3" 等，作為顯示字串存入文字欄位。
說明（gov_documentversion）：使用者輸入的顯示版本（如 "v2.1 草稿"），與系統版本並存，供業務顯示用。
說明（路徑 A 特點）：gov_expectedfilename 欄位不需更新（已由 GOV-020 填入，保留作為文件清冊追蹤憑證）。
```

**步驟 7A**：SupersededBy 回填（版本鏈可追溯性）
```
說明：步驟 7 已取得新 Document Register 記錄的 GUID（variables('NewDocumentId')）。
     以此 ID 回填步驟 6 中被 Supersede 的所有舊記錄的 gov_supersededby 欄位，
     建立完整的版本鏈（舊記錄 → 新記錄的單向指標）。
     收集容器：variables('SupersededIds')（步驟 6 Apply to each 中逐一 Append）。

Action：Condition（是否有需回填的記錄？）
  （搜尋 condition → 選擇「控制項」下的「Condition」）
  條件：length(variables('SupersededIds')) greater than 0

  True 分支（有被 Supersede 的記錄 → 執行回填）：
    Action：Apply to each
      （搜尋 apply to each → 選擇「控制項」下的「Apply to each」）
      Output From：variables('SupersededIds')
      重新命名為「ForEach-Backfill-SupersededBy」

      Action：Update a row (Dataverse)
        （搜尋 update a row → 選擇「Microsoft Dataverse」下的「Update a row」）
        Table name：Document Register
        Row ID：@{items('ForEach-Backfill-SupersededBy')}
        欄位對應：
          gov_supersededby：@{variables('NewDocumentId')}
        說明：gov_supersededby 為 Lookup 欄位，指向 Document Register 同資料表的另一筆記錄。
             若尚未在 Dataverse Schema 建立此欄位，請先依 02 文件建立後再操作此步驟。

  False 分支（全新文件，無 Superseded 記錄 → 跳過）：
    不需要任何操作

前置條件確認：gov_supersededby 欄位需為 Document Register → Document Register 的 Lookup 欄位。
             建立方式：Dataverse → 資料表 → Document Register → 資料行 → 新增資料行
             → 顯示名稱「SupersededBy」→ 類型「查詢」→ 相關資料表選「Document Register」→ 儲存
```

**步驟 8**：更新 Project Registry Link（Link 目標規則）
```
✅ [已修正 BUG-022] 將 {最佳目標 URL} 佔位符替換為具體的「Approved 優先，否則當前上傳 URL」實作

說明：根據 Doc 02 Baseline Matrix 的 ProjectRegistryLinkField，
     將 SharePoint URL 回寫至 Project Registry 對應欄位。

Link 目標規則（實作）：
  優先使用此 ProjectId + DocumentType 最新已核准（Approved）版本的 URL；
  若無 Approved 記錄（含文件首次上傳的 Draft 狀態），改用本次上傳 URL。
  > 設計說明：Project Registry 的 link 欄位應始終指向「已核准的最新版本」，
  >           而非草稿版本。若使用者剛上傳了 Draft，link 指向 Draft 僅是暫時狀態，
  >           GOV-003 審批通過後 gov_documentrole 更新為 Approved，
  >           下次上傳或 GOV-018 偵測後會再次更新此 link。

說明（P-13 原則）：禁止以 Switch 硬編碼 DocumentType → LinkField 映射。
  步驟 4 的 Lookup_FolderMapping 已從 Document Baseline Matrix 讀取該筆記錄，
  直接取用 gov_projectregistrylinkfield 欄位即可。

Action：Condition（檢查是否有對應 Link 欄位）
  （搜尋 condition → 選擇「控制項」下的「Condition」，中文可能為「條件」）
  條件：first(outputs('Lookup_FolderMapping')?['body/value'])?['gov_projectregistrylinkfield'] is not empty

  True 分支（有對應 Link 欄位 → 查詢最佳 URL + 回寫）：

    // Step 8-1：將 DocumentType 文字轉換為 OptionSet 整數（供 List 過濾用）
    Action：Compose
      重新命名為「Compose-DocTypeInt-Step8」
      Inputs：運算式 →
      if(equals(triggerBody()?['DocumentType'], 'TechnicalFeasibility'), 807660000,
      if(equals(triggerBody()?['DocumentType'], 'InitialRiskList'), 807660001,
      if(equals(triggerBody()?['DocumentType'], 'RiskAssessmentStrategy'), 807660002,
      if(equals(triggerBody()?['DocumentType'], 'DesignBaseline'), 807660003,
      if(equals(triggerBody()?['DocumentType'], 'RiskAssessment'), 807660004,
      if(equals(triggerBody()?['DocumentType'], 'IEC62443Checklist'), 807660005,
      if(equals(triggerBody()?['DocumentType'], 'ThreatModel'), 807660006,
      if(equals(triggerBody()?['DocumentType'], 'RequirementTraceability'), 807660007,
      if(equals(triggerBody()?['DocumentType'], 'TestPlan'), 807660008,
      if(equals(triggerBody()?['DocumentType'], 'TestReport'), 807660009,
      if(equals(triggerBody()?['DocumentType'], 'HandoverMeeting'), 807660010,
      if(equals(triggerBody()?['DocumentType'], 'ResidualRiskList'), 807660011,
      if(equals(triggerBody()?['DocumentType'], 'Other'), 807660012,
      if(equals(triggerBody()?['DocumentType'], 'DesignObjectInventory'), 807660013,
      if(equals(triggerBody()?['DocumentType'], 'ChangeImpact'), 807660014,
      if(equals(triggerBody()?['DocumentType'], 'DocumentRegister'), 807660015,
      -1))))))))))))))))
      說明：-1 代表 Phase 3 全新 DocumentType，Dataverse 不存在此值 → List 將回傳 0 筆 → 自動 fallback 至當前上傳 URL

    // Step 8-2：查詢此 DocumentType 在此專案的最新 Approved 版本
    Action：List rows (Dataverse)
      重新命名為「List_ApprovedVersions」
      Table name：Document Register
      Filter rows：_gov_parentproject_value eq '@{variables('varProjectId')}'
                   and gov_documenttype eq @{outputs('Compose-DocTypeInt-Step8')}
                   and gov_documentrole eq 807660004
                   and gov_documentregisterid ne '@{variables('NewDocumentId')}'
      Order By：createdon desc
      Row count（Top count）：1
      說明：807660004 = Approved；排除剛上傳的記錄本身（它是 Draft，不是 Approved）

    // Step 8-3：決定最佳目標 URL
    Action：Compose
      重新命名為「Compose-BestTargetURL」
      Inputs：運算式 →
      if(
        and(
          greater(length(outputs('List_ApprovedVersions')?['body/value']), 0),
          not(empty(first(outputs('List_ApprovedVersions')?['body/value'])?['gov_sharepointfilelink']))
        ),
        first(outputs('List_ApprovedVersions')?['body/value'])?['gov_sharepointfilelink'],
        outputs('SharePointFileURL')
      )
      說明：有 Approved 記錄且 link 非空 → 用 Approved 版本 URL；否則 → 用本次上傳 URL（當前 Draft）

    // Step 8-4：回寫至 Project Registry
    Action：Update a row (Dataverse)
      （搜尋 update a row → 選擇「Microsoft Dataverse」下的「Update a row」，中文為「更新資料列」）
      重新命名為「Update_ProjectRegistryLink」
      Table name：Project Registry
      Row ID：@{variables('varProjectId')}
      欄位對應（動態欄位名稱 — 以 run() expression 或 Patch 方式設定）：
        @{first(outputs('Lookup_FolderMapping')?['body/value'])?['gov_projectregistrylinkfield']}
        → 值：@{outputs('Compose-BestTargetURL')}

      > 操作說明：Power Automate 不支援直接用動態字串作為欄位名稱。
      > 請使用「Show advanced options」→「Add dynamic properties」→
      > 輸入運算式 first(outputs('Lookup_FolderMapping')?['body/value'])?['gov_projectregistrylinkfield']
      > 作為欄位鍵，值設定為 outputs('Compose-BestTargetURL')。
      > 或改用 Dataverse HTTP Connector（PATCH）方式動態設定欄位名稱：
      >   URI：/api/data/v9.2/gov_projectregistries(@{variables('varProjectId')})
      >   Headers：Content-Type: application/json
      >   Body：{ "@{first(outputs('Lookup_FolderMapping')?['body/value'])?['gov_projectregistrylinkfield']}" :
      >           "@{outputs('Compose-BestTargetURL')}" }

  False 分支（無對應 Link 欄位 → 跳過，如 Other 類型）：
    不需要任何操作
```

**步驟 9**：發送通知
```
Action：Run a Child Flow
  （搜尋 run a child flow → 選擇「Flows」下的「Run a Child Flow」，中文為「執行子流程」）
  Child Flow：GOV-015-NotificationHandler
  輸入：
    NotificationType：DocumentUploaded
    RecipientEmail：GOV-Architects（或文件審查者）
    Subject：文件已上傳 - @{triggerBody()['DocumentName']}
    Body：專案 @{outputs('Get_Project')?['body/gov_requestid']} 的文件「@{triggerBody()['DocumentName']}」已上傳。
```

**步驟 9A**：FlowRunId Writeback（P-16 原則）
```
Action：Update a row (Dataverse)
  連線：CR-Dataverse-SPN [MVP: 使用個人帳號連線]
  Table name：Project Registry
  Row ID：@{triggerBody()['ProjectId']}
  重新命名為「Writeback_FlowRunId_Success」

  欄位對應：
    gov_lastflowrunid：@{workflow()?['run']?['name']}
    gov_lastflowstatus：807660000（Success）
```

**步驟 10**：成功回應（回傳給 Power Apps — Canonical Error Envelope v5.0）
```
Action：Respond to a PowerApp or flow
  （搜尋 respond → 選擇「Respond to a PowerApp or flow」，中文為「回應 PowerApp 或流程」）
  點擊「+ Add an output」，依序新增：
    - Number：StatusCode → 200
    - Text：Status → Success
    - Text：ErrorCode → （空白）
    - Text：ErrorStage → （空白）
    - Text：Message → 文件上傳成功
    - Text：SharePointFileLink → @{outputs('SharePointFileURL')}
    - Text：DocumentRegisterRowId → @{variables('NewDocumentId')}
    - Text：FlowRunId → @{workflow()?['run']?['name']}
    - Text：Timestamp → @{utcNow()}
```

> **Power Apps 接收回傳值**：
> ```
> // 在 Power Apps 中取得 Flow 回傳值
> If(varUploadResult.status = "Success",
>     Notify("文件上傳成功", NotificationType.Success);
>     // 可透過 varUploadResult.sharepointfilelink 開啟檔案
>     Launch(varUploadResult.sharepointfilelink),
>     Notify("上傳失敗：" & varUploadResult.message, NotificationType.Error)
> );
> ```

**步驟 11**：Catch-ErrorHandler
```
搜尋 scope → 新增「Scope」（中文可能為「範圍」），重新命名為「Catch-ErrorHandler」
設定 Configure run after：點擊「...」→「設定在之後執行」→ 取消「成功」→ 勾選「已失敗」與「已逾時」

內容：
  Action：Compose（擷取錯誤訊息）
    （搜尋 compose → 選擇「資料作業」下的「Compose」，中文可能為「撰寫」）
    重新命名為「Compose-ErrorMessage」
    Inputs：@{coalesce(result('Try-MainLogic')?[0]?['error']?['message'], '未知錯誤')}

  Action：Update a row (Dataverse)（Writeback_FlowRunId_Failed — P-16 原則）
    Table name：Project Registry
    Row ID：@{triggerBody()['ProjectId']}
    gov_lastflowrunid：@{workflow()?['run']?['name']}
    gov_lastflowstatus：807660001（Failed）

  Action：Respond to a PowerApp or flow
    點擊「+ Add an output」，新增：
      - Number：StatusCode → 500
      - Text：Status → Failed
      - Text：ErrorCode → ERR-SYSTEM-500
      - Text：ErrorStage → CatchHandler
      - Text：Message → @{outputs('Compose-ErrorMessage')}
      - Text：SharePointFileLink → （空白）
      - Text：DocumentRegisterRowId → （空白）
      - Text：FlowRunId → @{workflow()?['run']?['name']}
      - Text：Timestamp → @{utcNow()}
```

> **注意**：同一 Flow 中只能有一個 `Respond to a PowerApp or flow` 動作會實際執行。
> 步驟 3 的 Pre-check 失敗、步驟 10 的成功回應、步驟 11 的 Catch 錯誤回應，三者互斥。
> **FlowRunId 與 Timestamp 必須在所有回應路徑中都包含**。
> **P-16 Writeback**：Catch 中必須先回寫 FlowRunId（Failed）再 Respond，確保 Dataverse 端可查詢失敗記錄。

**步驟 12**：儲存
```
點擊左上角 Flow 名稱（預設顯示「Untitled」）
輸入名稱：GOV-005-DocumentUpload
點擊「Save」（中文：「儲存」）
```

> **Power Apps 呼叫方式**（在 FORM-003 的「上傳」按鈕 OnSelect）：
> ```
> // 先驗證檔案大小與副檔名
> If(
>     First(AttachmentControl.Attachments).Size > 10485760,
>     Notify("檔案大小超過 10 MB 限制", NotificationType.Error),
>     Set(varUploadResult,
>         GOV005DocumentUpload.Run(
>             Text(varSelectedProject.gov_projectregistryid),
>             First(AttachmentControl.Attachments).Name,
>             Mid(
>                 JSON(First(AttachmentControl.Attachments).Value, JSONFormat.IncludeBinaryData),
>                 Find(",", JSON(First(AttachmentControl.Attachments).Value, JSONFormat.IncludeBinaryData)) + 1,
>                 Len(JSON(First(AttachmentControl.Attachments).Value, JSONFormat.IncludeBinaryData))
>             ),
>             ddDocumentType.Selected.Value,
>             txtDocumentName.Text,
>             varChangeType,
>             txtDocumentVersion.Text,
>             ddDeliverablePackage.Selected.Value,
>             txtComments.Text,
>             User().Email
>         )
>     );
>     If(varUploadResult.status = "Success",
>         Notify("文件上傳成功", NotificationType.Success),
>         Notify(varUploadResult.message, NotificationType.Error)
>     )
> );
> ```

### K. Power Apps 端呼叫範本（PowerFx）

**GOV-005 呼叫參數清單**（全部為 Text）：

| 參數順序 | 參數名稱 | Power Apps 端取值方式 | 說明 |
|:----------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| 1 | ProjectId | `Text(varSelectedProject.gov_projectregistryid)` | GUID 字串 |
| 2 | FileName | `First(AttachmentControl.Attachments).Name` | 原始檔名含副檔名 |
| 3 | FileContent | **見下方 Base64 轉換公式** | Base64 編碼字串 |
| 4 | DocumentType | `ddDocumentType.Selected.Value` | 下拉選單值 |
| 5 | DocumentName | `txtDocumentName.Text` | 顯示名稱 |
| 6 | ChangeType | `varChangeType` | **`Major` 或 `Minor`**；決定版本號遞增方式（必填） |
| 7 | DocumentVersion | `txtDocumentVersion.Text` | 如 v1.0 |
| 8 | DeliverablePackage | `ddDeliverablePackage.Selected.Value` | 可空白 |
| 9 | Comments | `txtComments.Text` | 可空白 |
| 10 | SubmittedBy | `User().Email` | 當前使用者 |

**Base64 轉換 — 最關鍵的踩雷點**：

> **⚠ Power Apps 的 `JSON()` 函數產出的 Base64 字串帶有 `data:...;base64,` 前綴。**
> Flow 端的 `base64ToBinary()` 函數**不接受**這個前綴。
> 必須在 Power Apps 端用 `Mid()` 截掉前綴，只傳純 Base64 部分。

```
// ❌ 錯誤寫法 — 直接傳 JSON() 結果
JSON(First(AttachmentControl.Attachments).Value, JSONFormat.IncludeBinaryData)
// 結果：data:application/pdf;base64,JVBERi0xLjQK...
// Flow 端 base64ToBinary() 會報錯！

// ✅ 正確寫法 — 用 Mid() 截掉前綴
With(
    {varBase64Full: JSON(First(AttachmentControl.Attachments).Value, JSONFormat.IncludeBinaryData)},
    Mid(
        varBase64Full,
        Find(",", varBase64Full) + 1,
        Len(varBase64Full)
    )
)
// 結果：JVBERi0xLjQK...（純 Base64，無前綴）
```

**可直接貼到 FORM-003 上傳按鈕 OnSelect 的完整 PowerFx 範本**：

```
// ===== GOV-005 Document Upload 呼叫範本 =====

// 1. 前置驗證 — 檔案大小（10 MB = 10485760 bytes）
If(
    IsEmpty(AttachmentControl.Attachments),
    Notify("請先選擇檔案", NotificationType.Error);
    false,
    First(AttachmentControl.Attachments).Size > 10485760,
    Notify("檔案大小超過 10 MB 限制，請壓縮或分割檔案", NotificationType.Error);
    false,
    true
);

// 2. 防止重複點擊
UpdateContext({varBusy: true});
Notify("正在上傳文件...", NotificationType.Information);

// 3. Base64 轉換 + Flow 呼叫
IfError(
    With(
        {
            varBase64Full: JSON(
                First(AttachmentControl.Attachments).Value,
                JSONFormat.IncludeBinaryData
            )
        },
        Set(
            varUploadResult,
            GOV005DocumentUpload.Run(
                Text(varSelectedProject.gov_projectregistryid),
                First(AttachmentControl.Attachments).Name,
                Mid(varBase64Full, Find(",", varBase64Full) + 1, Len(varBase64Full)),
                ddDocumentType.Selected.Value,
                txtDocumentName.Text,
                varChangeType,
                txtDocumentVersion.Text,
                ddDeliverablePackage.Selected.Value,
                txtComments.Text,
                User().Email
            )
        )
    ),
    Notify("Flow 觸發失敗，請檢查連線與 Flow 狀態", NotificationType.Error);
    UpdateContext({varBusy: false});
);

// 4. 關閉載入狀態
UpdateContext({varBusy: false});

// 5. 判斷回傳（必須顯示 Message 與 ErrorCode）
If(
    IsBlank(varUploadResult) || IsEmpty(varUploadResult),
    Notify("未收到 Flow 回傳，請檢查 Flow Run History", NotificationType.Error),

    varUploadResult.Status = "Success",
    Notify(
        "文件上傳成功：" & varUploadResult.SharePointFileLink,
        NotificationType.Success
    ),

    Notify(
        varUploadResult.Message & " [" & varUploadResult.ErrorCode & "]",
        NotificationType.Error
    )
);
```

> **必做**：上傳按鈕的 `DisplayMode` 屬性設定 `If(varBusy, DisplayMode.Disabled, DisplayMode.Edit)` 防止重複點擊。

### G. 最小驗證流程

**第 1 步：準備測試資料**

```
1. 確認有一個 Active 狀態的測試專案（由 GOV-001 建立）
2. 準備兩個小型 PDF 檔案（< 1 MB），分別命名為：
   - test-design-v1.pdf（第一次上傳）
   - test-design-v1.pdf（第二次上傳同名檔案 → 觸發 FileName 版本推進）
   注意：兩個都叫 test-design-v1.pdf，內容可以不同（用不同內容測試版本控制）
3. 確認 SharePoint 專案資料夾已存在（如 /Documents/DR-2026-0001/）
4. 確認 Document Register 資料表有 gov_filename 和 gov_versionnumber 欄位（必檢 11、12）
```

**第 2 步：首次上傳（Phase 3 全新文件路徑）**

```
1. 開啟 FORM-003（預覽模式或已發佈 App）
2. 選擇測試專案
3. 選擇 DocumentType = TechnicalFeasibility（對應 01_Feasibility）
4. 附加 test-design-v1.pdf（第一個版本）
5. 填入 DocumentName = 「測試設計文件」，DocumentVersion = v1.0
6. ChangeType = "Major"（首次上傳選 Major，1.0 起算）
7. 點擊「上傳」按鈕
8. 預期 Notify 訊息：「文件上傳成功」（Status = Success）
```

**第 3 步：去哪裡看 Flow Run History**

```
1. Maker Portal → 解決方案 → 開啟 GOV-005
2. 左側「28 天執行歷程記錄」
3. 找到最新一筆 → 點擊開啟
```

**第 4 步：首次上傳時 Run History 預期看到的畫面（Phase 3 路徑）**

```
  ✓ Power Apps (V2) Trigger（含 ChangeType = "Major"）
  ✓ Initialize variable (TargetFolder)
  ✓ Initialize variable (NewDocumentId)
  ✓ Initialize variable (MajorVersion) → 1
  ✓ Initialize variable (MinorVersion) → 0
  ✓ Initialize variable (MatchedByFileName) → false
  ✓ Initialize variable (MatchedByExpectedFileName) → false
  ✓ Initialize variable (PlannedRecordId) → ""
  ✓ Initialize variable (SupersededIds) → []
  ✓ Scope: Try-MainLogic
    ✓ Get_Project
    ✓ Condition（專案狀態）→ True
    ✓ Lookup_FolderMapping
    ✓ Condition（DocumentType 映射存在）→ False（有記錄）
    ✓ Set variable (TargetFolder = 01_Feasibility)
    ✓ Create file (SharePoint)
    ✓ Compose (SharePointFileURL)
    ✓ Lookup_ByFileName（0 筆 → Phase 1 無命中）
    ✓ Condition（Phase 1 FileName 命中？）→ False
    ✓ Lookup_ByExpectedFileName（0 筆 → Phase 1B 無命中）
    ✓ Condition（Phase 1B ExpectedFileName 命中？）→ False
    ✓ Lookup_ByDocType（0 筆 → Phase 2 無命中 → 全新文件）
    ✓ Condition（Phase 2 DocType 命中？）→ False
    ✓ Compose-NewDocumentFlag → true
    ✓ Condition（Path A — Phase 1B Planned 升級？）→ False（走路徑 B）
    ✓ Add_DocumentRegister（major=1, minor=0, versionlabel="1.0", gov_filename=test-design-v1.pdf）
    ✓ Set variable (NewDocumentId)
    ✓ Condition（SupersededIds 長度 > 0）→ False（無需回填）
    ✓ Update Project Registry Link
    ✓ Run GOV-015 Notification
    ✓ Writeback_FlowRunId_Success
    ✓ Respond (200 Success)
  ⊘ Scope: Catch-ErrorHandler（灰色跳過 = 正常）
```

**第 5 步：驗證首次上傳結果**

```
1. SharePoint → Design Documents → DR-2026-xxxx → 01_Feasibility → 確認 test-design-v1.pdf 存在
2. Dataverse → Document Register → 找到新建記錄 → 確認：
   - gov_filename = test-design-v1.pdf
   - gov_versionnumber_major = 1
   - gov_versionnumber_minor = 0
   - gov_versionlabel = "1.0"
   - gov_documentrole = 807660001（Draft）
   - gov_documentversion = v1.0（使用者輸入）
```

**第 6 步：第二次上傳同名檔案（Phase 1 FileName 版本推進路徑）**

```
情境 A（重大改版）：
  ChangeType = "Major" → 版本從 1.0 → 2.0

情境 B（小幅修訂）：
  ChangeType = "Minor" → 版本從 1.0 → 1.1

操作步驟：
1. 準備第二個 test-design-v1.pdf（內容不同，模擬更新後的設計文件）
2. 在 FORM-003 重複上傳步驟（同一專案、同 DocumentType、同 FileName）
3. DocumentVersion 填 v2.0 或 v1.1（顯示用）
4. ChangeType 選 Major 或 Minor（測試兩種情境）
5. 點擊「上傳」
6. 預期 Notify：「文件上傳成功」
```

**第 7 步：驗證 FileName 版本推進結果（最重要的驗收點）**

```
Run History 預期（Phase 1 路徑 + ChangeType = Major）：
  ✓ Lookup_ByFileName → 1 筆（找到 v1.0 Draft 記錄）
  ✓ Condition（Phase 1 FileName 命中？）→ True
  ✓ Compose-CurrentMajor-Phase1 → 1（gov_versionnumber_major）
  ✓ Compose-CurrentMinor-Phase1 → 0（gov_versionnumber_minor）
  ✓ Condition（ChangeType = Major？）→ True
    ✓ Set variable (MajorVersion) → 2（1 + 1）
    ✓ Set variable (MinorVersion) → 0（歸零）
  ✓ Set variable (MatchedByFileName) → true
  ✓ ForEach-Supersede-Phase1（對 v1.0 記錄）：
      ✓ Update a row → gov_documentrole = 807660003（Superseded）
      ✓ Append to array variable (SupersededIds) → 加入 v1.0 GUID
  ✓ Condition（Path A — Phase 1B Planned？）→ False（走路徑 B）
  ✓ Add_DocumentRegister（major=2, minor=0, versionlabel="2.0", gov_filename=test-design-v1.pdf）
  ✓ Condition（SupersededIds 長度 > 0）→ True
  ✓ ForEach-Backfill-SupersededBy：
      ✓ Update a row（v1.0 記錄）→ gov_supersededby = v2.0 GUID

Run History 預期（ChangeType = Minor 情境）：
  ✓ Condition（ChangeType = Major？）→ False
    ✓ Set variable (MajorVersion) → 1（不變）
    ✓ Set variable (MinorVersion) → 1（0 + 1）
  ✓ Add_DocumentRegister（major=1, minor=1, versionlabel="1.1"）

Dataverse 驗收（Major 情境）：
  v1.0 記錄：gov_documentrole = Superseded, gov_supersededby = v2.0 GUID, gov_supersededdate ≠ null
  v2.0 記錄：gov_documentrole = Draft, gov_versionnumber_major=2, gov_versionnumber_minor=0, gov_versionlabel="2.0"

Dataverse 驗收（Minor 情境）：
  v1.0 記錄：gov_documentrole = Superseded
  v1.1 記錄：gov_documentrole = Draft, gov_versionnumber_major=1, gov_versionnumber_minor=1, gov_versionlabel="1.1"
```

**第 8 步：失敗時分類排查**

| Run History 畫面 | 分類 | 排查方式 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| Pre-check Condition → False → Respond 400 | **業務驗證失敗** | 看 ErrorCode：ERR-005-002（專案非 Active）/ ERR-005-003（已凍結）/ ERR-005-005（檔案空白） |
| Lookup_FolderMapping → 0 筆 → Respond 400 | **DocumentType 映射失敗** | 確認 Document Baseline Matrix 有此 DocumentType 的記錄 |
| Create file 失敗 | **SharePoint 寫入失敗** | 確認資料夾存在、連線授權、檔案大小 |
| Trigger 本身失敗 | **Base64 問題** | 確認 Power Apps 端正確截掉 `data:...;base64,` 前綴 |
| Run History 無記錄 | **App 端未送出** | 依 Step 0 必檢 1~3 排查 |
| Lookup_ByFileName 報錯 | **Schema 缺失** | 確認 Document Register 有 gov_filename 欄位（必檢 11） |
| Compose-MaxVersion 報型別錯誤 | **Schema 缺失** | 確認 Document Register 有 gov_versionnumber 整數欄位（必檢 12） |
| 版本推進後舊記錄未變 Superseded | **Phase 1 Filter 錯誤** | 確認 Lookup_ByFileName Filter 包含 `gov_documentrole ne 807660003` 且 gov_filename 欄位存在且有值 |

### H. 常見失敗原因與對應排查路徑

| 編號 | 失敗現象 | 根因 | 排查路徑 |
|:----------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| H1 | Create file 報錯 `The file or folder does not exist` | SharePoint 專案資料夾不存在（GOV-001 未建立） | 確認 GOV-001 已成功建立專案 → SharePoint 有 `DR-xxxx` 資料夾及子資料夾 |
| H2 | Create file 報錯 `The body of the request is too large` | 檔案超過 Request Size Limit | Power Apps 端必須在呼叫 Flow 前檢查 `Attachments.Size <= 10485760` |
| H3 | Create file 成功但檔案損毀無法開啟 | Base64 字串帶有 `data:...;base64,` 前綴 | Power Apps 端必須用 `Mid(varBase64Full, Find(",", varBase64Full)+1, Len(varBase64Full))` 截掉前綴 |
| H4 | DocumentType 映射失敗（ERR-005-006） | Document Baseline Matrix 中無此 DocumentType 記錄 | 確認 Dataverse → Document Baseline Matrix → 搜尋該 DocumentType 名稱（注意大小寫完全一致） |
| H5 | 版本推進沒生效（舊記錄沒變 Superseded） | Lookup_ByFileName 或 Lookup_ByDocType 的 Filter 漏填或條件錯誤 | 確認 Filter 包含 `gov_documentrole ne 807660003`（排除 Superseded）且 gov_filename 欄位有值；Phase 1 命中需要 gov_filename 不為 null |
| H6 | Project Registry Link 沒更新 | Baseline Matrix 的 gov_projectregistrylinkfield 為空 | 確認 Baseline Matrix 中此 DocumentType 的 Link 欄位名稱已填入 |
| H7 | 已凍結專案仍可上傳（ERR-005-003 未觸發） | Pre-check 的 DocumentFreezeStatus 判斷條件寫反 | 確認條件為 `ne 807660001`（ne = not equal，807660001 = Frozen） |
| H8 | Schema mismatch 報錯 | 成功 Respond 有 SharePointFileLink 但失敗 Respond 沒有 | 確認所有 Respond（200/400/500）都有完整 9 個欄位，失敗時填空白字串 |
| H9 | Power Apps 收到空白結果 | 未用 `Set(varUploadResult, GOV005DocumentUpload.Run(...))` 接收 | 確認 PowerFx 用 `Set()` 而非直接 `GOV005DocumentUpload.Run()` |
| H10 | 檔案上傳到錯誤資料夾 | Document Baseline Matrix 的 gov_sharepointfolder 值錯誤 | 確認 Dataverse 中 TechnicalFeasibility → 01_Feasibility、DesignBaseline → 03_Design 等映射正確 |
| H11 | Lookup_ByFileName 報錯「Invalid filter」或「欄位不存在」 | Document Register 缺少 gov_filename 欄位（必檢 11 未執行） | Dataverse → Document Register → 資料行 → 新增 gov_filename（文字）欄位 → 儲存 → 重新執行 |
| H12 | Compose-CurrentMajor/Minor 報「InvalidTemplate」或 add() 失敗 | Document Register 缺少 gov_versionnumber_major 或 gov_versionnumber_minor 整數欄位（必檢 12 未執行） | Dataverse → Document Register → 資料行 → 新增 gov_versionnumber_major（整數）和 gov_versionnumber_minor（整數）→ 儲存；欄位類型必須為整數，不可為文字 |
| H13 | 同名檔案上傳後版本號沒有遞增（第二版 major 還是 1，minor 還是 0） | Lookup_ByFileName 查詢 0 筆（Phase 1 未命中），原因是第一版的 gov_filename 欄位為空 | 確認步驟 7 的 Add_DocumentRegister（路徑 B）有填入 gov_filename 欄位；已有的舊記錄需手動補填 gov_filename 值才能被 Phase 1 命中 |
| H14 | SupersededBy 回填失敗（ForEach-Backfill 報錯） | gov_supersededby 欄位不存在或類型非 Lookup | Dataverse → Document Register → 資料行 → 新增 gov_supersededby（查詢 → 相關資料表 Document Register）→ 儲存 |
| H15 | 版本推進後舊版 Approved 記錄未觸發審核重啟通知 | GOV-018 尚未建立或未正確執行（正常現象，審核重啟由 GOV-018 定時偵測而非即時推播） | 確認 GOV-018 Compliance Reconciler 已建立並處於 On 狀態；等待 GOV-018 下次定時執行（通常每日 0:00）後查看通知 |
| H16 | 版本號沒有正確遞增（ChangeType = Minor 但 Major 也 +1，或相反） | ChangeType 輸入值非 `Major` / `Minor`（大小寫或空格錯誤） | 確認 Power Apps 端下拉選單的 Value 精確為 `Major` 或 `Minor`（區分大小寫）；Condition 表達式為 `triggerBody()['ChangeType'] is equal to 'Major'` |
| H17 | Phase 1B Lookup_ByExpectedFileName 報「欄位不存在」 | Document Register 缺少 gov_expectedfilename 欄位（必檢 13 未執行） | Dataverse → Document Register → 資料行 → 新增 gov_expectedfilename（文字）欄位 → 儲存；需由 GOV-020 在建立 Planned 記錄時填入此值 |
| H18 | Phase 1B 命中但步驟 7 還是 Add 新記錄（Planned 沒升級） | variables('MatchedByExpectedFileName') 條件在步驟 7 的 Condition 寫法錯誤 | 確認步驟 7 的 Condition 為 `variables('MatchedByExpectedFileName') is equal to true`，而非 equals('MatchedByExpectedFileName', true) 等寫法 |

### 驗收測試（對應 07文件）

| 測試項目 | 操作方式 | 預期結果 | 07文件對應 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|:-------------------------------|
| 首次上傳（Phase 3 全新文件） | 在 FORM-003 上傳全新 FileName 的文件 | Status=Success，Document Register 建立 gov_versionnumber=1, gov_filename=FileName | E2E-014 |
| FileName 版本推進（Phase 1） | 再次上傳同 FileName（不同內容） | 舊記錄→Superseded，新記錄 gov_versionnumber=2，SupersededBy 回填 | E2E-014 |
| Approved 也被 Supersede | 先 Approve 一筆文件，再上傳同 FileName | 舊 Approved 記錄→Superseded，新 Draft 記錄建立 | E2E-014 |
| DocumentType 備援（Phase 2） | 上傳 FileName 從未出現過、但 DocumentType 有舊記錄的文件 | Phase 1 無命中→Phase 2 命中→舊記錄 Superseded，新 Draft 建立 | E2E-014 |
| Link 回寫 | 上傳後查詢 Project Registry | 對應 Link 欄位已更新為最新 URL | E2E-016 |
| 凍結阻斷 | 對已凍結專案上傳 | 回傳 Status=Failed，ErrorCode = ERR-005-003 | E2E-001 |
| Base64 上傳 | 透過 FORM-003 提交含檔案 | SharePoint 目標資料夾出現檔案 | E2E-001 |
| Power Apps 回傳 | 在 Power Apps 中檢查 varUploadResult | 包含 Status, SharePointFileLink, DocumentRegisterRowId | E2E-001 |
| 檔案過大 | 在 FORM-003 上傳 > 10 MB 檔案 | Power Apps 端直接阻擋，不呼叫 Flow | E2E-001 |

---

## GOV-014：Document Freeze

### A. 基本資訊

| 項目 | 值 |
|:--------------------------|:--------------------------------------------------------------|
| Flow 名稱 | GOV-014 Document Freeze |
| 目的 | Gate 3 通過後自動執行：凍結 Dataverse Document Register 記錄、移除 SharePoint 寫入權限、建立凍結稽核紀錄 |
| Trigger 類型 | **Manually trigger a flow**（Child Flow）`[Governance Critical Control]` 必須勾選「Only other flows can trigger」 |
| 呼叫此 Flow 的來源 | GOV-003（Gate Approval Orchestrator，僅 Gate 3 Approve 後呼叫） |
| Connection References | CR-Dataverse-SPN, CR-SharePoint-SPN `[MVP: 全部使用個人帳號連線]` |
| Concurrency Control | **不開啟**（由 GOV-002 的 Concurrency = 1 控制） |
| 對應測試案例 | 07文件 E2E-001 Phase 6 |

> **觸發鏈**：
> ```
> Gate 3 Approved → GOV-003 → 呼叫 GOV-014 Document Freeze
> ```
> GOV-014 **只允許在 Gate 3 通過後被呼叫**。Pre-check 會驗證 CurrentGate 是否為 Gate3。

### Step 0：GOV-014 起手式必檢 6 項

> **為什麼需要 Step 0？** SharePoint 權限移除失敗（Service Principal 無 Site Collection Admin 權限）和「已凍結的專案再次被凍結」是最常見的問題。

**必檢 1：Flow 在同一 Solution 內**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 確保 GOV-003 可以呼叫 GOV-014 |
| 操作路徑 | Maker Portal → 解決方案 → 確認 GOV-014 在清單中 |
| 成功長相 | Solution 內看到 GOV-014 |
| 失敗長相 | Flow 不在清單 |
| 下一步 | 在 Solution 內新建 |

**必檢 2：Trigger 是「Manually trigger a flow」**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | Child Flow 必須用此 Trigger |
| 操作路徑 | 開啟 GOV-014 → 檢查 Trigger 標題 |
| 成功長相 | 「Manually trigger a flow」 |
| 失敗長相 | 其他 Trigger 類型 |
| 下一步 | 刪除 → 重建正確 Trigger |

**必檢 3：SharePoint Connection Reference 已授權且有足夠權限**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 移除 Contribute 權限需要 Site Collection Admin 等級的權限 |
| 操作路徑 | 開啟 GOV-014 → 找到 SharePoint 相關 Action → 確認無 ⚠️ |
| 成功長相 | 連線已授權，Service Principal 是 Site Collection Admin |
| 失敗長相 | 連線有 ⚠️ 或權限不足 |
| 下一步 | 重新授權連線；將 Service Principal 加入 Site Collection Admin |

**必檢 4：Dataverse Connection Reference 已授權**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 需要更新 Project Registry 和 Document Register |
| 操作路徑 | 檢查所有 Dataverse Action 右上角 |
| 成功長相 | 無 ⚠️ |
| 失敗長相 | 有 ⚠️ |
| 下一步 | 點擊 → 選擇已授權連線 |

**必檢 5：Document Register 有 gov_isfrozen 和 gov_frozendate 欄位**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 凍結時需要更新這些欄位 |
| 操作路徑 | Dataverse → 資料表 → Document Register → 確認欄位存在 |
| 成功長相 | 有 gov_isfrozen（Yes/No）和 gov_frozendate（DateTime） |
| 失敗長相 | 欄位不存在 |
| 下一步 | 依 02 文件建立欄位 |

**必檢 6：Flow 狀態是 On**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | GOV-003 呼叫時 GOV-014 必須為開啟狀態 |
| 操作路徑 | Flow 上方狀態列 |
| 成功長相 | On |
| 失敗長相 | Off |
| 下一步 | 開啟 |

### B. 先決條件清單

| 先決條件 | 如何確認 |
|:--------------------------------------|:----------------------------------------------|
| GOV-003 已建立（呼叫來源） | Flow 列表中 GOV-003 狀態為 On |
| Project Registry 有 gov_documentfreezestatus 和 gov_documentfreezedate 欄位 | Dataverse → 確認存在 |
| Document Register 有 gov_isfrozen 和 gov_frozendate 欄位 | Dataverse → 確認存在 |
| Review Decision Log 已建立 | Dataverse → 確認存在 |
| SharePoint Site 的 Service Principal 有 Site Collection Admin 權限 | SharePoint → Site 設定 → 確認 |
| 測試專案已通過 Gate 3（CurrentGate = Gate3） | Dataverse → Project Registry → 確認 |

### C. Input Schema（Child Flow Trigger 參數）

| 參數名稱 | Input 類型 | 必填 | 說明 |
|:--------------------------|:----------------------|:------:|:----------------------------------------------|
| ProjectId | **Text** | ✓ | gov_projectregistryid（GUID 字串） |

### D. Output Schema（Child Flow 回傳）

| 輸出參數 | 類型 | 200 成功時 | 400 前置條件失敗 | 500 系統例外 |
|:----------------------------------------------|:----------------------|:-------------------------------|:-------------------------------|:-------------------------------|
| StatusCode | Number | `200` | `400` | `500` |
| Status | Text | `Success` | `Failed` | `Failed` |
| ErrorCode | Text | `""` | `ERR-014-xxx` | `ERR-014-SYSTEM` |
| ErrorMessage | Text | `文件凍結已完成` | 具體錯誤訊息 | 系統錯誤訊息 |

### E. Pre-check 清單

| Pre-check | 條件 | ErrorCode | 說明 |
|:----------------------------------------------|:----------------------------------------------|:-------------------------------|:----------------------------------------------|
| 1. 專案存在 | ProjectId 存在於 Project Registry | ERR-014-001 | 專案不存在 |
| 2. CurrentGate = Gate3 | `gov_currentgate eq 807660004` | ERR-014-002 | **只允許 Gate 3 通過後執行凍結** |
| 3. 尚未凍結 | `gov_documentfreezestatus ne 807660001` | ERR-014-003 | 已凍結的專案不可重複凍結 |

> **⚠ Pre-check 2 是 GOV-014 最重要的防護。** 確保不會在 Gate 3 之前意外凍結文件。

### F. 建立步驟（逐步點擊）

**步驟 1：建立 Flow + Manually trigger a flow**

```
1. Maker Portal → 解決方案 → 開啟 Solution
2. + 新增 → 自動化 → 雲端流程 → 立即
3. 搜尋 manually trigger → 選擇「Manually trigger a flow」→ 建立
4. 改名為「GOV-014 Document Freeze」
5. + Add an input → Text → ProjectId
```

**步驟 2：Initialize variable**

```
Action: Initialize variable
  Name：varProjectId
  Type：String
  Value：動態內容 → ProjectId
```

**步驟 3：建立 Try-MainLogic Scope**

```
+ 新增步驟 → Scope → 重新命名為「Try-MainLogic」
```

> 以下步驟 4 ~ 步驟 11 在 Try-MainLogic 內部建立。

**步驟 4：Get Project（在 Try-MainLogic 內部）**

```
+ 新增步驟 → Get a row by ID（Dataverse）
  Table name：Project Registry
  Row ID：運算式 → variables('varProjectId')
  重新命名為「Get_Project」
```

**步驟 5：Pre-check — CurrentGate = Gate3**

```
+ 新增步驟 → Condition
  重新命名為「PreCheck_IsGate3」
  條件：outputs('Get_Project')?['body/gov_currentgate'] is equal to 807660004

  False 分支（CurrentGate 不是 Gate3）：
    Respond to a PowerApp or flow
      StatusCode → 400
      Status → Failed
      ErrorCode → ERR-014-002
      ErrorMessage → 僅 Gate 3 通過後才能執行文件凍結，目前 CurrentGate 非 Gate3
    Terminate → Cancelled

  True 分支：繼續
```

**步驟 6：Pre-check — 尚未凍結**

```
+ 新增步驟 → Condition
  重新命名為「PreCheck_NotFrozen」
  條件：outputs('Get_Project')?['body/gov_documentfreezestatus'] is not equal to 807660001

  False 分支（已凍結）：
    Respond → StatusCode 400, ErrorCode ERR-014-003,
    ErrorMessage 此專案文件已凍結，不可重複凍結
    + Terminate → Cancelled

  True 分支：繼續
```

**步驟 7：更新 Project Registry 凍結狀態**

```
+ 新增步驟 → Update a row（Dataverse）
  Table name：Project Registry
  Row ID：@{variables('varProjectId')}
  欄位對應：
    gov_documentfreezestatus：807660001（Frozen）
    gov_documentfreezedate：utcNow()
  重新命名為「Freeze_ProjectRegistry」
```

**步驟 8：凍結所有 Document Register 記錄**

```
a. + 新增步驟 → List rows（Dataverse）
   Table name：Document Register
   Filter rows：_gov_parentproject_value eq '@{variables('varProjectId')}'
   重新命名為「List_AllDocuments」

b. + 新增步驟 → Apply to each
   （搜尋 apply to each → 選擇「控制項」下的「Apply to each」）
   Select an output from previous steps：outputs('List_AllDocuments')?['body/value']

   內部：
     Update a row（Dataverse）
     Table name：Document Register
     Row ID：@{items('Apply_to_each')?['gov_documentregisterid']}
     欄位對應：
       gov_isfrozen：true（Yes/No 類型選 Yes）
       gov_frozendate：utcNow()
```

> **⚠ 凍結的對象是「該專案的所有 Document Register 記錄」。**
> 包含 Draft、Active、Approved、Superseded 狀態的記錄全部標記為 Frozen。
> 這確保任何版本的文件都無法被修改。

**步驟 9：移除 SharePoint 寫入權限**

```
說明：將 Flow Service Principal 對專案資料夾的權限從 Contribute 降為 Read。
     凍結後所有主體（包含 Flow）都只有 Read 權限。

a. + 新增步驟 → 搜尋 send an http request to sharepoint
   → 選擇「SharePoint」下的「Send an HTTP request to SharePoint」
   （中文：「將 HTTP 要求傳送到 SharePoint」）
   連線：CR-SharePoint-SPN
   Site Address：選擇 Design Governance Site
   Method：POST
   Uri：
     _api/web/GetFolderByServerRelativeUrl('/sites/DesignGovernance/Design Documents/@{outputs('Get_Project')?['body/gov_requestid']}')/ListItemAllFields/breakroleinheritance(copyRoleAssignments=true,clearSubscopes=true)
   Headers：
     Accept: application/json;odata=nometadata
     Content-Type: application/json;odata=nometadata
   Body：（空白）
   重新命名為「BreakInheritance」

   ⚠ MVP 模式替代方案：若不使用 REST API，可手動到 SharePoint 設定資料夾權限。
   此步驟在 MVP 模式下可暫時跳過，改為人工操作。

b. + 新增步驟 → Send an HTTP request to SharePoint
   Method：POST
   Uri：
     _api/web/GetFolderByServerRelativeUrl('/sites/DesignGovernance/Design Documents/@{outputs('Get_Project')?['body/gov_requestid']}')/ListItemAllFields/roleassignments/removeroleassignment(principalid=@{Service Principal ID},roledefid=1073741827)
   重新命名為「RemoveContribute」

   ⚠ principalid 為 Service Principal 的 SharePoint User ID（非 Azure AD Object ID）。
   ⚠ roledefid=1073741827 為 Contribute 角色。
   ⚠ MVP 模式：手動到 SharePoint → 資料夾 → 管理存取 → 移除 Contribute。
```

> **MVP 模式簡化**：步驟 9 的 SharePoint REST API 操作較為複雜。
> MVP 模式下可將步驟 9 替換為一個 Compose 動作記錄「需手動凍結 SharePoint 權限」，
> 並在 GOV-015 通知中提醒管理員手動操作。
> Hardened 模式再改為完整的 REST API 自動化。

**步驟 10：寫入凍結稽核記錄**

```
+ 新增步驟 → Add a new row（Dataverse）
  Table name：Review Decision Log
  欄位對應：
    gov_parentproject：@{variables('varProjectId')}（Lookup → 進階 → 貼 GUID）
    gov_reviewtype：807660008（DocumentFreeze）
    gov_decision：807660001（Approved / Executed）
    gov_approvedby：Flow Service Principal（或 Auto-Executed）
    gov_revieweddate：utcNow()
    gov_comments：Document Freeze executed after Gate 3 approval
    gov_triggerflowrunid：運算式 → workflow()?['run']?['name']
  重新命名為「Create_FreezeAuditLog」
```

**步驟 11：成功 Respond**

```
+ 新增步驟 → Respond to a PowerApp or flow
  Number → StatusCode → 200
  Text → Status → Success
  Text → ErrorCode → （空白）
  Text → ErrorMessage → 文件凍結已完成
```

> 步驟 11 是 Try-MainLogic 最後一步。

**步驟 12：建立 Catch-ErrorHandler Scope**

```
在 Try-MainLogic 下方：
  + 新增步驟 → Scope → 重新命名為「Catch-ErrorHandler」
  Configure run after：取消「成功」→ 勾選「已失敗」與「已逾時」

內部：
  a. Compose → 「Compose-ErrorMessage」
     Inputs：coalesce(result('Try-MainLogic')?[0]?['error']?['message'], '未知錯誤')

  b. Respond to a PowerApp or flow
     StatusCode → 500
     Status → Failed
     ErrorCode → ERR-014-SYSTEM
     ErrorMessage → Compose-ErrorMessage Outputs
```

**步驟 13：Save**

```
點擊右上角「儲存」→ 等待完成
```

### G. 必做設定檢核點

| 檢核項目 | 確認方式 | 預期結果 |
|:----------------------------------------------|:----------------------------------------------|:-------------------------------|
| Trigger 類型 | Trigger 卡片標題 | Manually trigger a flow |
| Input 參數 | Trigger → 1 個參數 | ProjectId(Text) |
| Pre-check Gate3 | PreCheck_IsGate3 Condition | 檢查 gov_currentgate = 807660004 |
| Pre-check NotFrozen | PreCheck_NotFrozen Condition | 檢查 gov_documentfreezestatus ≠ 807660001 |
| Apply to each | 凍結所有 Document Register | 更新 gov_isfrozen = true, gov_frozendate |
| 稽核記錄 | Create_FreezeAuditLog | ReviewType = DocumentFreeze |
| Catch Configure run after | Catch Scope 設定 | 成功未勾選，已失敗 + 已逾時已勾選 |
| Flow 名稱 | Flow 左上角 | `GOV-014 Document Freeze` |

### H. 最小驗證流程

**第 1 步：準備測試專案**

```
在 Dataverse 中確認有一個測試專案：
  - CurrentGate = Gate3（807660004）← 表示已通過 Gate 3
  - DocumentFreezeStatus = NotFrozen（807660000）
  - 至少有 1 筆 Document Register 記錄（gov_isfrozen = false）
  - SharePoint 有對應的專案資料夾
```

**第 2 步：觸發 GOV-014**

```
方式一（透過 GOV-003）：
  提交 Gate 3 申請 → 所有審批者 Approve → GOV-003 自動呼叫 GOV-014

方式二（直接測試 GOV-014）：
  開啟 GOV-014 → 點擊「Test」→「Manually」→ 輸入 ProjectId → Run
```

**第 3 步：成功時 Run History 預期畫面**

```
  ✓ Manually trigger a flow
  ✓ Initialize variable (varProjectId)
  ✓ Scope: Try-MainLogic
    ✓ Get_Project
    ✓ PreCheck_IsGate3 → True
    ✓ PreCheck_NotFrozen → True
    ✓ Freeze_ProjectRegistry（DocumentFreezeStatus = Frozen）
    ✓ List_AllDocuments
    ✓ Apply to each（每筆 Document Register → IsFrozen = true）
    ✓ BreakInheritance（SharePoint）
    ✓ RemoveContribute（SharePoint）
    ✓ Create_FreezeAuditLog
    ✓ Respond (200 Success)
  ⊘ Scope: Catch-ErrorHandler（灰色跳過 = 正常）
```

**第 4 步：成功判定 — 必須全部通過**

| 驗證項目 | 預期值 | 驗證方法 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| Project Registry: DocumentFreezeStatus | `Frozen`（807660001） | Dataverse 查詢 |
| Project Registry: DocumentFreezeDate | 有值（當前時間） | Dataverse 查詢 |
| Document Register: gov_isfrozen | 所有記錄皆為 `true` | Dataverse → List rows → 確認 |
| Document Register: gov_frozendate | 所有記錄皆有值 | Dataverse → List rows → 確認 |
| SharePoint 資料夾 | 嘗試上傳新文件 → 應失敗 | SharePoint → 進入資料夾 → 拖曳檔案 → 應顯示權限不足 |
| Review Decision Log | 新增一筆 ReviewType = DocumentFreeze | Dataverse 查詢 |
| GOV-005 上傳阻斷 | 對已凍結專案呼叫 GOV-005 → 回傳 ERR-005-003 | 從 Power Apps 嘗試上傳 |

**第 5 步：失敗時分類排查**

| Run History 畫面 | 分類 | 排查方式 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| PreCheck_IsGate3 → False → Respond 400 | **Gate3 前置條件** | 確認專案 CurrentGate = 807660004（Gate3） |
| PreCheck_NotFrozen → False → Respond 400 | **已凍結** | 專案已凍結過，不可重複凍結 |
| Apply to each 失敗 | **Document Register 更新問題** | 確認 gov_isfrozen 欄位存在且類型為 Yes/No |
| SharePoint REST API 失敗 | **SharePoint 權限問題** | 確認 Service Principal 有 Site Collection Admin 權限 |
| Catch 執行 | **系統例外** | 展開 Compose-ErrorMessage 看具體錯誤 |

### I. 常見失敗原因與對應排查路徑

| 編號 | 失敗現象 | 根因 | 排查路徑 |
|:----------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| I1 | PreCheck 報 ERR-014-002 | 專案尚未通過 Gate 3（CurrentGate ≠ 807660004） | 確認 Gate 3 審批已全部完成（GOV-003 → Approve → 更新 CurrentGate） |
| I2 | PreCheck 報 ERR-014-003 | 專案已凍結過 | 正常行為 — 不可重複凍結。若需解凍，須走 FORM-008 例外流程 |
| I3 | SharePoint BreakInheritance 報 403 | Service Principal 沒有 Site Collection Admin 權限 | SharePoint → Site 設定 → 網站集合管理員 → 加入 Service Principal |
| I4 | Apply to each 很慢（數十秒） | 專案有大量 Document Register 記錄 | 正常 — Apply to each 逐筆更新。可考慮使用 Batch Update 優化 |
| I5 | Document Register 記錄的 gov_isfrozen 沒更新 | Apply to each 的 Update 動作缺少 gov_isfrozen 欄位 | 確認 Update 動作有設定 gov_isfrozen = true 和 gov_frozendate = utcNow() |
| I6 | 凍結後 GOV-005 仍可上傳 | GOV-005 的 Pre-check 沒檢查 DocumentFreezeStatus | 確認 GOV-005 步驟 3 有 `gov_documentfreezestatus ne 807660001` 條件 |
| I7 | Review Decision Log 稽核記錄未建立 | Create_FreezeAuditLog Action 失敗 | 確認 Review Decision Log 資料表存在、gov_reviewtype 有 807660008 值 |
| I8 | GOV-003 呼叫 GOV-014 但 GOV-014 為 Off | Flow 狀態關閉 | 開啟 GOV-014 Flow |
| I9 | 凍結後仍可在 SharePoint 手動上傳 | BreakInheritance 或 RemoveContribute 失敗但未被捕獲 | MVP 模式下手動到 SharePoint 設定權限；Hardened 模式確認 REST API 回傳 200 |
| I10 | 重複凍結時報 500 而非 400 | PreCheck_NotFrozen 條件寫反 | 確認條件為 `is not equal to 807660001`（不等於 Frozen） |

---

## GOV-016：Rework Loop Handler

### A. 基本資訊

| 項目 | 值 |
|:--------------------------|:--------------------------------------------------------------|
| Flow 名稱 | GOV-016 Rework Loop Handler |
| 目的 | 審批 Reject 後遞增 ReworkCount、記錄 LastReworkDate、當 ReworkCount ≥ 3 時自動暫停專案（OnHold），並觸發通知 |
| Trigger 類型 | **Manually trigger a flow**（Child Flow）`[Governance Critical Control]` 必須勾選「Only other flows can trigger」 |
| 呼叫此 Flow 的來源 | GOV-003（Gate Approval Orchestrator，任何 Gate 任何層級的 Reject 後） |
| Connection References | CR-Dataverse-SPN `[MVP: 個人帳號連線]` |
| Concurrency Control | **不開啟**（由 GOV-002 的 Concurrency = 1 控制） |
| 依賴 Child Flow | GOV-015（Notification Handler） |
| 對應測試案例 | 07文件 E2E-002, E2E-003, E2E-004 |

> **觸發時機**：GOV-003 在任何 Gate、任何審批層級收到 Reject 後，立即呼叫 GOV-016。
> GOV-016 負責 Rework 計數與狀態管理；GOV-003 負責通知與 Terminate。

### Step 0：GOV-016 起手式必檢 5 項

**必檢 1：Flow 在同一 Solution 內且狀態為 On**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | GOV-003 能在 Reject 分支呼叫 GOV-016 |
| 操作路徑 | Maker Portal → 解決方案 → 確認 GOV-016 存在且狀態為 On |
| 成功長相 | Solution 內看到 GOV-016，狀態為 On |
| 失敗長相 | 不存在或狀態 Off |
| 下一步 | 建立後開啟 |

**必檢 2：Trigger 是「Manually trigger a flow」**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | Child Flow 必須用此 Trigger |
| 操作路徑 | 開啟 GOV-016 → 確認 Trigger 標題 |
| 成功長相 | Manually trigger a flow |
| 失敗長相 | 其他 Trigger 類型 |
| 下一步 | 刪除 → 重建 |

**必檢 3：Project Registry 有 gov_reworkcount 和 gov_lastreworkdate 欄位**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 這兩個欄位是 GOV-016 寫入的核心目標 |
| 操作路徑 | Dataverse → 資料表 → Project Registry → 確認欄位存在 |
| 成功長相 | gov_reworkcount（Whole number, Min 0 Max 100）、gov_lastreworkdate（DateTime） |
| 失敗長相 | 欄位不存在 |
| 下一步 | 依 02 文件建立欄位 |

**必檢 4：GOV-015 已建立且狀態為 On**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | GOV-016 需要呼叫 GOV-015 發送 Rejected 通知 |
| 操作路徑 | 確認 GOV-015 在 Solution 內且 On |
| 成功長相 | GOV-015 狀態為 On |
| 失敗長相 | 不存在或 Off |
| 下一步 | 先建立 GOV-015 |

**必檢 5：Dataverse Connection Reference 已授權**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 更新 Project Registry 需要 Dataverse 連線 |
| 操作路徑 | 開啟 GOV-016 → 所有 Dataverse Action 無 ⚠️ |
| 成功長相 | 無 ⚠️ |
| 失敗長相 | 有 ⚠️ |
| 下一步 | 點擊 → 選擇已授權連線 |

### B. 先決條件清單

| 先決條件 | 如何確認 |
|:--------------------------------------|:----------------------------------------------|
| GOV-003 已建立（呼叫來源） | Flow 列表中 GOV-003 狀態為 On |
| GOV-015 已建立（通知） | Flow 列表中 GOV-015 狀態為 On |
| Project Registry 有 gov_reworkcount、gov_lastreworkdate 欄位 | Dataverse → 確認存在 |
| Project Registry 的 gov_projectstatus OptionSet 有 OnHold（807660001）值 | Dataverse → 確認 OptionSet 值存在 |

### C. Input Schema

| 參數名稱 | Input 類型 | 必填 | 說明 |
|:--------------------------|:----------------------|:------:|:----------------------------------------------|
| ProjectId | **Text** | ✓ | gov_projectregistryid（GUID 字串） |
| RequestedGate | **Text** | ✓ | 本次被 Reject 的 Gate（Gate0/Gate1/Gate2/Gate3），用於通知內文 |

### D. Output Schema（Child Flow 回傳）

| 輸出參數 | 類型 | 200 成功時 | 500 系統例外 |
|:----------------------------------------------|:----------------------|:-------------------------------|:-------------------------------|
| StatusCode | Number | `200` | `500` |
| Status | Text | `Success` | `Failed` |
| ErrorCode | Text | `""` | `ERR-016-SYSTEM` |
| ErrorMessage | Text | `Rework 記錄已更新` | 系統錯誤訊息 |

### E. Rework 狀態機

**ReworkCount 驅動的狀態轉換**：

```
任意 Gate 審批 Reject
        ↓
GOV-003 呼叫 GOV-016（傳入 ProjectId + RequestedGate）
        ↓
GOV-016 讀取當前 gov_reworkcount（例如當前值為 N）
        ↓
GOV-016 更新：
  gov_reworkcount = N + 1
  gov_lastreworkdate = utcNow()
        ↓
        ├── N + 1 < 3 → 正常重工
        │     ProjectStatus 保持不變（Active）
        │     → 通知 System Architect + PM：「審批已駁回，請修改後重新提交」
        │     → 專案可重新提交同一 Gate 申請
        │
        └── N + 1 ≥ 3 → 達到重工上限，自動暫停
              gov_projectstatus = OnHold（807660001）
              → 通知 System Architect + PM + Governance Lead：「重工次數已達 3 次，專案已暫停」
              → 專案無法再提交 Gate 申請，須 Engineering Management 解除 OnHold
```

**欄位更新一覽**：

| 欄位 | 操作 | 值 | 說明 |
|:----------------------------------------------|:-------------------------------|:-------------------------------|:----------------------------------------------|
| gov_reworkcount | +1 遞增 | 當前值 + 1 | **必須以 `add()` 運算式遞增，不可硬寫** |
| gov_lastreworkdate | 設定 | `utcNow()` | 本次 Reject 的系統時間 |
| gov_projectstatus | 僅當 ReworkCount ≥ 3 時更新 | `807660001`（OnHold） | 不滿足條件時**不可動此欄位** |

**GOV-016 絕對不可修改的欄位**（稽核不可變記錄）：

| 欄位 | 原因 |
|:----------------------------------------------|:----------------------------------------------|
| gov_currentgate | Reject 不推進 Gate，必須維持原值 |
| gov_requeststatus | 已由 GOV-003 設回 None，GOV-016 不再動 |
| gov_gate0/1/2/3passeddate | 通過日期不可偽造，只有 Approve 路徑才能寫入 |
| gov_documentfreezestatus | 凍結狀態由 GOV-014 管理 |
| gov_riskacceptancestatus | 風險接受狀態由 GOV-004 管理 |
| createdby, createdon | 系統稽核欄位，Dataverse 自動管理 |

> **⚠ 若 GOV-017 偵測到上述欄位被 GOV-016 修改，會自動回滾並記錄違規。**
> GOV-016 的 Update a row 動作**只能**填入 gov_reworkcount、gov_lastreworkdate、gov_projectstatus（條件限制下）。

### F. 建立步驟（逐步點擊）

**步驟 1：建立 Flow + Manually trigger a flow**

```
1. Maker Portal → 解決方案 → 開啟 Solution
2. + 新增 → 自動化 → 雲端流程 → 立即
3. 搜尋 manually trigger → 選擇「Manually trigger a flow」→ 建立
4. 改名為「GOV-016 Rework Loop Handler」
5. + Add an input：
   → Text → ProjectId
   → Text → RequestedGate
```

**步驟 2：Initialize variable**

```
Action: Initialize variable
  Name：varProjectId
  Type：String
  Value：動態內容 → ProjectId
```

**步驟 3：建立 Try-MainLogic Scope**

```
+ 新增步驟 → Scope → 重新命名為「Try-MainLogic」
```

**步驟 4：Get Project（在 Try-MainLogic 內部）**

```
+ 新增步驟 → Get a row by ID（Dataverse）
  Table name：Project Registry
  Row ID：運算式 → variables('varProjectId')
  重新命名為「Get_Project」
```

**步驟 5：Compose 計算新 ReworkCount**

```
+ 新增步驟 → Compose
  重新命名為「Compose-NewReworkCount」
  Inputs：運算式 → add(int(outputs('Get_Project')?['body/gov_reworkcount']), 1)

  ⚠ 說明：
  - 必須用 add() 運算式讀取「當前值 + 1」
  - 不可硬寫固定數字（如直接填 1）
  - int() 確保型別轉換正確（Dataverse Whole number 回傳為字串）
```

**步驟 6：Update Project Registry — 遞增 ReworkCount**

```
+ 新增步驟 → Update a row（Dataverse）
  Table name：Project Registry
  Row ID：@{variables('varProjectId')}
  欄位對應：
    gov_reworkcount：@{outputs('Compose-NewReworkCount')}
    gov_lastreworkdate：utcNow()
  重新命名為「Update_ReworkCount」

  ⚠ 只填這兩個欄位，其他欄位一律不動。
```

**步驟 7：Condition — ReworkCount ≥ 3 判斷**

```
+ 新增步驟 → Condition
  重新命名為「Is_OnHoldThreshold」
  條件：outputs('Compose-NewReworkCount') is greater than or equal to 3

  True 分支（≥ 3，需要 OnHold）：

    a. Update a row → Project Registry
       Row ID：@{variables('varProjectId')}
       欄位對應：
         gov_projectstatus：807660001（OnHold）
       重新命名為「Set_ProjectOnHold」
       ⚠ 此 Update 只填 gov_projectstatus，不動其他欄位

    b. Run a Child Flow → GOV-015 Notification Handler
       Child Flow：GOV-015-NotificationHandler
       NotificationType：ComplianceAlert
       RecipientEmail：@{outputs('Get_Project')?['body/gov_submittedby']}
         （⚠ 也可同時通知 GOV-GovernanceLead，可傳兩次呼叫或以分號分隔）
       Subject：【合規警示】重工次數已達 @{outputs('Compose-NewReworkCount')} 次，專案已暫停 - @{outputs('Get_Project')?['body/gov_requestid']}
       Body：專案 @{outputs('Get_Project')?['body/gov_requestid']} 的 Gate @{triggerBody()?['RequestedGate']} 審批已駁回，累計重工次數已達 @{outputs('Compose-NewReworkCount')} 次（上限 3 次），專案已自動暫停（OnHold）。請聯絡 Engineering Management 解除暫停。
       ProjectId：@{variables('varProjectId')}

  False 分支（< 3，正常重工）：

    Run a Child Flow → GOV-015 Notification Handler
    NotificationType：GateRejected
    RecipientEmail：@{outputs('Get_Project')?['body/gov_submittedby']}
    Subject：Gate @{triggerBody()?['RequestedGate']} 已駁回（第 @{outputs('Compose-NewReworkCount')} 次） - @{outputs('Get_Project')?['body/gov_requestid']}
    Body：您的 Gate @{triggerBody()?['RequestedGate']} 申請已被駁回。這是第 @{outputs('Compose-NewReworkCount')} 次重工。請檢視審批意見後重新提交。
    ProjectId：@{variables('varProjectId')}
```

**步驟 8：成功 Respond**

```
+ 新增步驟 → Respond to a PowerApp or flow
  Number → StatusCode → 200
  Text → Status → Success
  Text → ErrorCode → （空白）
  Text → ErrorMessage → Rework 記錄已更新
```

**步驟 9：Catch-ErrorHandler Scope**

```
在 Try-MainLogic 下方：
  + 新增步驟 → Scope → 重新命名為「Catch-ErrorHandler」
  Configure run after：取消「成功」→ 勾選「已失敗」與「已逾時」

  內部：
    a. Compose → 「Compose-ErrorMessage」
       Inputs：coalesce(result('Try-MainLogic')?[0]?['error']?['message'], '未知錯誤')

    b. Respond to a PowerApp or flow
       StatusCode → 500
       Status → Failed
       ErrorCode → ERR-016-SYSTEM
       ErrorMessage → Compose-ErrorMessage Outputs
```

**步驟 10：Save**

```
點擊右上角「儲存」→ 等待完成
```

### G. 必做設定檢核點

| 檢核項目 | 確認方式 | 預期結果 |
|:----------------------------------------------|:----------------------------------------------|:-------------------------------|
| Trigger 類型 | Trigger 卡片標題 | Manually trigger a flow |
| Input 參數 | Trigger → 2 個參數 | ProjectId(Text), RequestedGate(Text) |
| ReworkCount 遞增 | Compose-NewReworkCount 運算式 | `add(int(...gov_reworkcount...), 1)` 非硬寫 |
| Update 欄位 | Update_ReworkCount Action | 只有 gov_reworkcount + gov_lastreworkdate |
| OnHold 條件 | Is_OnHoldThreshold | ≥ 3 才觸發 OnHold |
| OnHold 欄位 | Set_ProjectOnHold Action | 只有 gov_projectstatus = 807660001 |
| Catch Configure run after | Catch Scope 設定 | 成功未勾選，已失敗 + 已逾時已勾選 |

### H. 最小驗證流程

**第 1 步：準備測試資料**

```
在 Dataverse 中確認有一個測試專案：
  - ProjectStatus = Active（807660000）
  - gov_reworkcount = 0（初始值）
  - RequestedGate = Gate0（最簡路徑）
  - 已提交 Gate0 申請（RequestStatus = Pending）
```

**第 2 步：觸發 Reject（第 1 次 Rework）**

```
1. 開啟審批通知 Email → 點擊「Reject」→ 填寫 Comments → 提交
2. 或直接測試 GOV-016：
   Maker Portal → GOV-016 → Test → Manually
   → 輸入 ProjectId（測試專案 GUID）
   → 輸入 RequestedGate（Gate0）
   → Run
```

**第 3 步：Run History 預期畫面（第 1 次 Rework）**

```
  ✓ Manually trigger a flow
  ✓ Initialize variable (varProjectId)
  ✓ Scope: Try-MainLogic
    ✓ Get_Project（gov_reworkcount 當前值 = 0）
    ✓ Compose-NewReworkCount（結果 = 1）
    ✓ Update_ReworkCount（gov_reworkcount = 1, gov_lastreworkdate = 現在時間）
    ✓ Is_OnHoldThreshold（1 < 3 → False）
      ✓ False 分支：Run GOV-015（GateRejected 通知）
    ✓ Respond (200 Success)
  ⊘ Scope: Catch-ErrorHandler（灰色跳過 = 正常）
```

**第 4 步：驗證 Dataverse 狀態（第 1 次 Rework）**

```
查詢 Project Registry：
  ✓ gov_reworkcount = 1
  ✓ gov_lastreworkdate = 剛才的時間
  ✓ gov_projectstatus = 807660000（Active，保持不變）
  ✓ gov_currentgate = Pending（保持不變，Reject 不推進 Gate）
```

**第 5 步：測試第 3 次 Rework（OnHold 觸發）**

```
將測試專案的 gov_reworkcount 手動設為 2（模擬已駁回兩次）
再次觸發 GOV-016

預期結果：
  ✓ Compose-NewReworkCount = 3
  ✓ Is_OnHoldThreshold → True
    ✓ Set_ProjectOnHold（gov_projectstatus = 807660001）
    ✓ Run GOV-015（ComplianceAlert 通知）
  ✓ Respond (200 Success)

Dataverse 驗證：
  ✓ gov_reworkcount = 3
  ✓ gov_projectstatus = 807660001（OnHold）
  ✓ System Architect + PM + Governance Lead 收到 ComplianceAlert 通知
```

### I. 常見失敗原因與對應排查路徑

| 編號 | 失敗現象（可觀測訊號） | 根因 | Run History 定位 | 排查路徑 |
|:----------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| I1 | Compose-NewReworkCount 報錯 `Value could not be converted to Integer` | Dataverse 回傳的 gov_reworkcount 為 null（欄位首次為空） | 展開 Get_Project → 看 body/gov_reworkcount 值是否 null | 確認 gov_reworkcount 欄位預設值設為 0；或在 Compose 改用 `add(int(coalesce(outputs('Get_Project')?['body/gov_reworkcount'], '0')), 1)` |
| I2 | Update_ReworkCount 成功但 gov_reworkcount 沒增加（值還是 0） | Compose 運算式硬寫為 1 而非遞增 | 展開 Compose-NewReworkCount → 看 Inputs 是否為 `add(int(...), 1)` | 改用正確的遞增運算式 `add(int(outputs('Get_Project')?['body/gov_reworkcount']), 1)` |
| I3 | ReworkCount 達到 3 但 ProjectStatus 沒變 OnHold | Is_OnHoldThreshold 條件用了「大於」而非「大於等於」 | 展開 Is_OnHoldThreshold → 看條件是 `> 3` 還是 `>= 3` | 改為 `greater than or equal to 3`（即 `>= 3`） |
| I4 | GOV-017 發現 GOV-016 修改了 gov_currentgate（違規） | Update_ReworkCount 誤加了 gov_currentgate 欄位 | GOV-017 Run History → 找違規記錄 → 確認是 GOV-016 造成的 | 從 Update_ReworkCount 移除 gov_currentgate 欄位 |
| I5 | GOV-015 通知未送達 | GOV-015 未建立或狀態 Off | 展開 Run a Child Flow → 看回傳 Status 是否 Success | Step 0 必檢 4 |
| I6 | Catch 500，錯誤訊息 `The specified row was not found` | ProjectId 為空或無效 GUID | 展開 Get_Project → 看 Row ID 值 | 確認 GOV-003 傳給 GOV-016 的 ProjectId 正確 |
| I7 | OnHold 後仍可提交 Gate 申請 | GOV-002 Pre-check 沒檢查 ProjectStatus ≠ OnHold | GOV-002 Run History → 看 Pre-check 是否通過 | 確認 GOV-002 步驟 8 有 `gov_projectstatus eq 807660000`（Active） |
| I8 | 每次重工都收到兩封 Rejected 通知 | GOV-003 已發一封通知，GOV-016 又發一封 | 兩個 GOV-015 Run 記錄，時間相近 | 確認 GOV-003 Reject 分支和 GOV-016 各自負責的通知類型不重疊 |

---

## Guardrail 監控機制實作

> **文件權威關係說明**
>
> 本章節（GOV-017、GOV-018、GOV-019）為 Guardrail 機制的**施工步驟權威**。
>
> - **施工步驟**：以本章節為準
> - **治理語意、違規判斷、通知規則**：以 **06-guardrails-and-anti-cheating.md** 為權威
>
> 若對機制設計有疑問，請參閱 06 文件。

## GOV-017：Guardrail Monitor（權威來源：SOP-04-v2-Part3）

### A. 基本資訊

| 項目 | 值 |
|:--------------------------|:--------------------------------------------------------------|
| Flow 名稱 | GOV-017 Guardrail Monitor |
| 目的 | 每小時掃描 Dataverse Audit Log，偵測人為修改 Flow-only 欄位的違規行為，自動回滾違規修改，發送違規通知 |
| Trigger 類型 | **Recurrence（Schedule）** |
| 執行頻率 | 每 1 小時（整點，00:00, 01:00 ... 23:00 UTC+8） |
| Connection References | CR-Dataverse-SPN `[MVP: 個人帳號連線]` |
| 依賴 Child Flow | GOV-015（Notification Handler） |
| 對應測試案例 | 07文件 AC-001, AC-002 |

> **治理語意權威**：本 Flow 的治理語意與違規判斷依據請以 **06-guardrails-and-anti-cheating.md** 為權威。本章節僅提供施工步驟。

### Step 0：GOV-017 起手式必檢 6 項

**必檢 1：Dataverse Audit 功能已啟用**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | GOV-017 依賴 Dataverse Audit Log 才能查到人為修改記錄 |
| 操作路徑 | Maker Portal → 設定 → 進階設定 → 稽核 → 確認「開始稽核」已勾選 → 確認 Project Registry、Review Decision Log、Risk Assessment Table 三個資料表都啟用欄位層級稽核 |
| 成功長相 | 進入 Project Registry 稽核記錄頁可看到歷史修改 |
| 失敗長相 | 稽核頁為空或功能未啟用 |
| 下一步 | 到進階設定啟用稽核 → 為每個資料表啟用欄位層級稽核 |

**必檢 2：Flow Service Principal 有 Dataverse Audit 查詢權限**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | HTTP 動作查詢 `/api/data/v9.2/audits` 需要 System Administrator 或 Auditor 角色 |
| 操作路徑 | Power Platform Admin Center → 環境 → 應用程式使用者 → 確認 Service Principal 有 System Administrator 角色 |
| 成功長相 | 角色已指派 |
| 失敗長相 | 查詢 Audit 時報 401 或 403 |
| 下一步 | 指派 System Administrator 角色（或最小化的 Service Reader + Auditor 角色） |

**必檢 3：Connection Reference 已授權**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | HTTP 動作和 Dataverse 動作都需要連線 |
| 操作路徑 | 開啟 GOV-017 → 所有動作無 ⚠️ |
| 成功長相 | 無 ⚠️ |
| 失敗長相 | 有 ⚠️ |
| 下一步 | 選擇已授權連線 |

**必檢 4：Governance Violation Log 資料表已建立**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 違規記錄要寫入此資料表 |
| 操作路徑 | Dataverse → 資料表 → 確認 gov_governanceviolationlog 存在 |
| 成功長相 | 資料表存在且有 gov_violationtype、gov_rollbackstatus 等欄位 |
| 失敗長相 | 資料表不存在 |
| 下一步 | 依 02 文件建立資料表 |

**必檢 5：GOV-015 已建立且狀態為 On**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 違規通知需要呼叫 GOV-015 |
| 操作路徑 | 確認 GOV-015 狀態為 On |
| 成功長相 | On |
| 失敗長相 | Off |
| 下一步 | 開啟 GOV-015 |

**必檢 6：Flow 狀態是 On**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | Recurrence Flow 必須為 On 才會定時觸發 |
| 操作路徑 | 確認 GOV-017 狀態為 On |
| 成功長相 | On |
| 失敗長相 | Off |
| 下一步 | 開啟 GOV-017 |

### B. 先決條件清單

| 先決條件 | 如何確認 |
|:--------------------------------------|:----------------------------------------------|
| Dataverse Audit 功能已啟用 | 進階設定 → 稽核 → 確認開啟 |
| Project Registry、Review Decision Log 資料表已啟用欄位層級稽核 | 資料表設定 → 稽核 → 確認 |
| Governance Violation Log 資料表已建立 | Dataverse → 確認存在 |
| Flow Service Principal 有 System Administrator 角色 | Power Platform Admin Center → 確認 |
| GOV-015 Notification Handler 已建立 | Flow 列表中 GOV-015 狀態為 On |

### C. Recurrence Trigger 設定

```
Trigger: Recurrence
  （搜尋 recurrence → 選擇「Schedule」下的「Recurrence」，中文為「週期」）

設定欄位：
  Interval：1
  Frequency：Hour（小時）
  Time Zone：(UTC+08:00) Taipei（台北）
    ★ 關鍵：必須設定 Time Zone。若不設定，Recurrence 預設使用 UTC，
      導致實際執行時間偏移 8 小時，與預期不一致。
  Start time：（選填，若填入則指定首次執行時間）
```

> **時區設定操作路徑**：
> 點擊 Recurrence Trigger 右上角「...」→「設定」→「顯示進階選項」→ 找到「時區」下拉 → 選擇「(UTC+08:00) Taipei」

> **為什麼要設 UTC+8 而非 UTC？**
> Governance Lead 需要在上班時間（08:00~18:00 UTC+8）收到違規通知。
> 若設 UTC，每次執行的本地時間將比預期晚 8 小時。

### D. Audit Log 查詢方法選擇

GOV-017 有兩種查詢方式，依環境條件選擇：

| 方式 | 動作名稱 | 前提 | 優點 | 缺點 |
|:-------------------------------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| **方式一（推薦）** | Send an HTTP Request to Dataverse | Service Principal 有 System Administrator 角色 | 可查真正的 Audit Log，包含 OldValue/NewValue | 需要 Hardened 連線 |
| **方式二（MVP）** | List rows（Dataverse） | 任何 Dataverse 連線 | 設定簡單 | 無 OldValue，回滾較難；僅能偵測 `modifiedon` 不能偵測具體欄位 |

**方式一：Send an HTTP Request to Dataverse（推薦）**

> **UI 路徑**：搜尋 `send an http request to dataverse` → 選擇「Microsoft Dataverse」下的「Send an HTTP Request」（不是「HTTP」，不是「SharePoint」的）

```
Action：Send an HTTP Request（Dataverse）
  重新命名為「Query_AuditLog」
  連線：CR-Dataverse-SPN
  Method：GET
  URI：/api/data/v9.2/audits?$filter=createdon gt @{outputs('Compose-OneHourAgo')}&$select=auditid,createdon,objecttypecode,_objectid_value,operation,attributemask,changeddata,_userid_value&$orderby=createdon desc&$top=500
```

> **⚠ URI 組合要點**：
> 1. 使用相對路徑（不含 `https://{org}.api.crm.dynamics.com`）— 「Send an HTTP Request（Dataverse）」動作會自動補上環境 URL
> 2. `createdon gt @{...}` 中的 OData 時間格式必須是 ISO 8601（`addHours(utcNow(), -1)` 回傳的格式符合）
> 3. `$top=500` 限制最多回傳 500 筆，避免超出 Flow 記憶體上限
> 4. ~~`attributemask`~~ **不可**用於欄位名稱比對 — 它是整數位元遮罩（如 786432），不含欄位邏輯名稱
> 5. **`changeddata`** 是正確的欄位：包含 JSON 格式的 changedAttributes 陣列，每個元素有 `attributeLogicalName`、`oldValue`、`newValue`

> **⚠ 動作選錯的常見錯誤**：
> - 不要選「HTTP」（無授權頭）
> - 不要選「SharePoint」的「Send an HTTP Request」（不同 Connector）
> - 正確的是「Microsoft Dataverse」Connector 下的「Send an HTTP Request」

**方式二：List rows（Dataverse）——MVP 替代方案**

```
Action：List rows（Dataverse）
  重新命名為「List_RecentlyModified」
  Table name：Project Registry
  Filter rows：modifiedon gt @{outputs('Compose-OneHourAgo')} and _modifiedby_value ne '{Flow Service Principal User ID}'
    ★ 關鍵：排除 Flow Service Principal 本身的修改（否則每次 Flow 更新都會觸發虛假警報）
  Select columns：gov_projectregistryid,gov_currentgate,gov_requeststatus,gov_projectstatus,gov_documentfreezestatus,gov_reworkcount,modifiedon,_modifiedby_value

  ⚠ Flow Service Principal User ID 的取得方式：
  Power Platform Admin Center → 環境 → 設定 → 使用者 + 權限 → 應用程式使用者
  → 開啟 Service Principal → 複製「使用者識別碼」（GUID 格式）
```

### E. 建立步驟（逐步點擊）

**步驟 1：建立 Flow + Recurrence Trigger**

```
1. Maker Portal → 解決方案 → 開啟 Solution
2. + 新增 → 自動化 → 雲端流程 → 已排程
   （英文：+ New → Automation → Cloud flow → Scheduled）
3. 在建立畫面設定：
   Flow 名稱：GOV-017 Guardrail Monitor
   Repeat every：1 Hour
   Starting：（今天日期 08:00）
4. 點擊「建立」
5. 設定 Time Zone：
   點擊 Recurrence Trigger → 「顯示進階選項」→ 時區 → 選「(UTC+08:00) Taipei」
```

**步驟 2：計算查詢時間範圍**

```
+ 新增步驟 → Compose
  重新命名為「Compose-OneHourAgo」
  Inputs：運算式 → addHours(utcNow(), -1)

+ 新增步驟 → Compose
  重新命名為「Compose-CurrentTime」
  Inputs：運算式 → utcNow()
```

**步驟 3：查詢 Audit Log（方式一）或 List rows（方式二）**

```
【方式一 — Audit Log】
+ 新增步驟 → 搜尋 send an http request → 選擇「Microsoft Dataverse」下的「Send an HTTP Request」
  連線：CR-Dataverse-SPN
  Method：GET
  URI：/api/data/v9.2/audits?$filter=createdon gt @{outputs('Compose-OneHourAgo')}&$select=auditid,createdon,objecttypecode,_objectid_value,operation,attributemask,changeddata,_userid_value&$orderby=createdon desc&$top=500
  重新命名為「Query_AuditLog」

【方式二 — List rows（MVP）】
+ 新增步驟 → List rows（Dataverse）
  Table name：Project Registry
  Filter rows：modifiedon gt @{outputs('Compose-OneHourAgo')} and _modifiedby_value ne '{Service Principal User ID}'
  重新命名為「List_RecentlyModified」
```

**步驟 4：篩選 Flow-only 欄位違規**

```
【方式一的後續】
+ 新增步驟 → 搜尋 filter array → 選擇「資料作業」下的「Filter array」
  重新命名為「Filter_FlowOnlyViolations」
  From：outputs('Query_AuditLog')?['body/value']
  條件（進階模式 — 點擊「進階模式」輸入以下運算式）：
    @or(
        contains(string(item()?['changeddata']), 'gov_currentgate'),
        contains(string(item()?['changeddata']), 'gov_requeststatus'),
        contains(string(item()?['changeddata']), 'gov_projectstatus'),
        contains(string(item()?['changeddata']), 'gov_documentfreezestatus'),
        contains(string(item()?['changeddata']), 'gov_decision'),
        contains(string(item()?['changeddata']), 'gov_approvedby'),
        contains(string(item()?['changeddata']), 'gov_reworkcount'),
        contains(string(item()?['changeddata']), 'gov_lastreworkdate')
    )

  ✅ [已修正 BUG-001] 使用 changeddata（非 attributemask）
  說明：
  - attributemask 是整數位元遮罩（如 786432），string() 只會產生 "786432"，
    永遠無法 contains 到欄位邏輯名稱（原始設計完全失效）。
  - changeddata 是 JSON 字串，格式如：
    {"changedAttributes":[{"attributeLogicalName":"gov_currentgate","oldValue":"...","newValue":"..."}]}
    使用 contains(string(changeddata), 'gov_currentgate') 可正確偵測到欄位名稱。
  - string() 確保型別轉換，避免 contains() 對 null 報錯。
```

**步驟 5：Condition — 有無違規記錄**

```
+ 新增步驟 → Condition
  重新命名為「Has_Violations」
  條件：length(body('Filter_FlowOnlyViolations')) is greater than 0

  False 分支（無違規）：
    + 新增步驟 → Terminate
      Status：Succeeded（正常結束，無需處理）
    ⚠ 這裡的 Terminate 是正常結束，不是錯誤

  True 分支（有違規）：繼續步驟 6
```

**步驟 6：Apply to each — 對每筆違規逐一處理**

```
在 Has_Violations 的 True 分支：

+ 新增步驟 → Apply to each
  Select an output from previous steps：body('Filter_FlowOnlyViolations')

  內部動作：

  a. Compose 解析違規資訊
     重新命名為「Compose-ViolationInfo」
     Inputs：
       ObjectId：items()?['_objectid_value']
       Entity：items()?['objecttypecode']
       AttributeMask：items()?['attributemask']
       OldValue：items()?['changeddata']（JSON 中的 OldValue 欄位）
       ModifiedBy：items()?['_userid_value']
       ViolationTime：items()?['createdon']

  b. Add a new row → Governance Violation Log
     gov_violationtype：807660001（FlowOnlyFieldModified）
     gov_violationtime：items()?['createdon']
     gov_violatinguser：items()?['_userid_value']
     gov_violationentity：items()?['objecttypecode']
     gov_violationfield：items()?['attributemask']
     gov_violationrecordid：items()?['_objectid_value']
     gov_oldvalue：解析 changeddata 中的 OldValue
     gov_newvalue：解析 changeddata 中的 NewValue
     gov_rollbackstatus：807660000（Pending）
     重新命名為「Create_ViolationLog」

  c. Condition：OldValue is not null（可自動回滾判斷）
     條件：empty(items()?['changeddata']) is equal to false

     True 分支（有 OldValue → 自動回滾）：
       Update a row → 違規的資料表（objecttypecode 對應的 Table）
         Row ID：items()?['_objectid_value']
         欄位：依 attributemask 決定回滾哪個欄位 = 解析 changeddata 的 OldValue
         重新命名為「Rollback_ViolatedField」

       Update a row → Governance Violation Log
         Row ID：outputs('Create_ViolationLog')?['body/gov_governanceviolationlogid']
         gov_rollbackstatus：807660001（Closed — 已回滾）
         重新命名為「Update_ViolationLog_Closed」

     False 分支（OldValue 無法取得 → 人工回滾）：
       Update a row → Governance Violation Log
         gov_rollbackstatus：807660002（ManualRequired）

  ✅ [已修正 GAP-017-A] 在通知前加入 Compose-RollbackStatusLabel，替換 {RollbackStatus} 佔位符

  d-0. Compose → Compose-RollbackStatusLabel
       （搜尋 compose → 選擇「資料作業」下的「Compose」）
       重新命名為「Compose-RollbackStatusLabel」
       位置：Run a Child Flow（GOV-015）之前
       Inputs：運算式 →
       if(
         equals(result('Rollback_ViolatedField')?[0]?['status'], 'Succeeded'),
         '已自動回滾（gov_rollbackstatus = Closed）',
         '需人工處理（gov_rollbackstatus = ManualRequired）'
       )
       說明：result('Rollback_ViolatedField')?[0]?['status'] 取得 Update 回滾動作的執行狀態。
            'Succeeded' → 自動回滾成功；其他（'Failed'/'Skipped'）→ 需人工處理。
            result() 函數在 Power Automate 中可跨 Condition 分支存取先前動作結果，
            無論 Rollback_ViolatedField 是否在此路徑上執行，均安全返回狀態或 null。

  d. Run a Child Flow → GOV-015 Notification Handler
     NotificationType：ViolationDetected
     RecipientEmail：GOV-GovernanceLead 群組 Email
     Subject：【高優先級】偵測到治理違規 - @{items()?['objecttypecode']}.@{items()?['changeddata']}
     Body：
       違規時間：@{items()?['createdon']}
       違規者：@{items()?['_userid_value']}
       違規欄位：@{items()?['changeddata']}
       違規記錄 ID：@{items()?['_objectid_value']}
       自動回滾狀態：@{outputs('Compose-RollbackStatusLabel')}  ✅ [已修正 GAP-017-A]
     ProjectId：（若 objecttypecode = gov_projectregistry，填入 ObjectId）
```

**步驟 7：Save**

```
點擊右上角「儲存」
```

### F. 回滾 Dataverse 違規修改的注意事項

> **⚠ 自動回滾是 GOV-017 最難實作的部分。** 以下是逐步說明。

**如何取得 OldValue**：

```
changeddata 欄位是 JSON 字串，格式如下：
{
  "changedAttributes": [
    {
      "logicalName": "gov_currentgate",
      "oldValue": {"Value": 807660001},
      "newValue": {"Value": 807660003}
    }
  ]
}

取得 OldValue 的運算式：
first(
  filter(
    json(items()?['changeddata'])?['changedAttributes'],
    item()?['logicalName'] eq 'gov_currentgate'
  )
)?['oldValue']?['Value']
```

**回滾 Update a row 的 Row ID**：

```
Row ID 使用：items()?['_objectid_value']
（注意：是 _objectid_value，加底線，是 Lookup 格式）
```

**哪些欄位不可自動回滾（即使有 OldValue）**：

| 欄位 | 原因 |
|:----------------------------------------------|:----------------------------------------------|
| gov_gate0/1/2/3passeddate | 回滾通過日期可能造成 Gate 狀態不一致 |
| createdby, createdon | 系統稽核欄位，不可修改 |
| gov_triggerflowrunid | Flow Run 記錄不可偽造 |

> **MVP 模式簡化**：若自動回滾實作複雜，可先只做：
> 1. 偵測並記錄到 Governance Violation Log（RollbackStatus = ManualRequired）
> 2. 發送通知給 Governance Lead
> 3. 人工回滾
> Hardened 版本再實作自動 OldValue 解析和回滾。

### G. RollbackStatus 值定義

| OptionSet 值 | 顯示值 | 說明 | 後續處理 |
|:----------|:-------------------------------|:----------------------------------------------|:----------------------------------------------|
| 807660000 | Pending | 剛偵測到，尚未處理 | 等待 GOV-017 處理 |
| 807660001 | Closed | 已自動回滾成功 | 無需人工介入 |
| 807660002 | ManualRequired | 無法自動回滾（OldValue 無法取得或欄位不可自動回滾） | 需 Governance Lead 手動處理 |

### H. 最小驗證流程

**第 1 步：製造一個人為違規**

```
在 DEV 環境（確認 FLS 未啟用，否則操作會被擋住）：
1. Dataverse → Project Registry → 開啟任一 Active 專案
2. 手動修改 gov_currentgate 欄位（例如從 Gate0 改為 Gate2）
3. 儲存
4. 記錄修改時間
```

**第 2 步：等待 GOV-017 執行，或手動觸發**

```
方式一：等待下一個整點（最多等 1 小時）
方式二：手動觸發測試：
  開啟 GOV-017 → 點擊「Test」→「Manually」→「Run flow」
  （注意：手動觸發時 Recurrence 的時間參數不生效，Compose-OneHourAgo 仍以 utcNow()-1h 計算）
```

**第 3 步：Run History 預期畫面**

```
  ✓ Recurrence Trigger
  ✓ Compose-OneHourAgo
  ✓ Compose-CurrentTime
  ✓ Query_AuditLog（或 List_RecentlyModified）
  ✓ Filter_FlowOnlyViolations
  ✓ Has_Violations → True（有 gov_currentgate 違規記錄）
    ✓ Apply to each（1 筆違規）
      ✓ Compose-ViolationInfo
      ✓ Create_ViolationLog
      ✓ Condition：OldValue is not null → True
        ✓ Rollback_ViolatedField（gov_currentgate 回滾為 Gate0）
        ✓ Update_ViolationLog_Closed
      ✓ Run GOV-015（ViolationDetected 通知）
```

**第 4 步：驗證回滾成功**

```
Dataverse → Project Registry → 確認 gov_currentgate 已回滾為 Gate0（807660001）
Dataverse → Governance Violation Log → 確認新增一筆記錄：
  gov_rollbackstatus = Closed
  gov_violationfield = gov_currentgate
Governance Lead Email/Teams → 確認收到違規通知
```

### I. 常見失敗原因與對應排查路徑

| 編號 | 失敗現象（可觀測訊號） | Run History 定位 | 排查路徑 |
|:----------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| I1 | Query_AuditLog 報 401/403 | 展開 Query_AuditLog → 看 Response Status Code | Service Principal 未指派 System Administrator 角色；或 CR-Dataverse-SPN 未授權 |
| I2 | Query_AuditLog 回傳 0 筆（已有人為修改但查無資料） | 展開 Query_AuditLog → 看 body/value 是否為空陣列 | Dataverse Audit 功能未啟用；或查詢時間範圍過窄（剛啟用 Audit 不會有歷史資料）；或 Service Principal 在 FLS 模式下修改無法被稽核 |
| I3 | Filter_FlowOnlyViolations 報錯 `contains: argument is not a string` | 展開 Filter_FlowOnlyViolations → 看哪個 contains 失敗 | attributemask 為 null → 改用 `contains(string(coalesce(item()?['attributemask'], '')), ...)` |
| I4 | Has_Violations 條件判斷錯誤（有違規但走了 False 分支） | 展開 Has_Violations → 看 Condition 結果 | 確認 `length()` 的輸入是 `body('Filter_FlowOnlyViolations')` 而非 `outputs('Filter_FlowOnlyViolations')` |
| I5 | Rollback_ViolatedField 失敗 `PicklistMapping` 錯誤 | 展開 Rollback → 看錯誤訊息 | OldValue 是文字格式（如 "Gate0"），但欄位是 OptionSet 需要數字（807660001）→ 需要先做映射轉換 |
| I6 | Governance Lead 未收到通知（GOV-015 失敗） | 展開 Run GOV-015 → 看回傳 Status | GOV-015 狀態 Off；或 Email Connector 未授權；或 GOV-GovernanceLead 群組無 Email |
| I7 | Flow 未按整點觸發（每次執行時間不對） | Run History → 看 Trigger 執行時間 | Recurrence Time Zone 未設定或設錯 → 確認設為 (UTC+08:00) Taipei |
| I8 | 回滾後被再次修改（違規者重複操作） | Governance Violation Log → 同一 Record 多筆記錄 | GOV-017 只能偵測不能預防 → 必須設定 FLS 才能從根本阻止人為修改 |

---

## GOV-018：Compliance Reconciler

### A. 基本資訊

| 項目 | 值 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 每日掃描所有 Active 專案，比對 Project Registry 的 `gov_currentgate` 與 Review Decision Log 最新核准記錄是否一致；發現不一致時寫入 Governance Violation Log 並通知 Governance Lead |
| Trigger 類型 | Recurrence（Schedule） |
| 執行頻率 | 每日 00:00 UTC+8（對應 UTC 16:00） |
| Connection References | CR-Dataverse-SPN |
| 對應測試案例 | AC-004, AC-005 |
| 依賴 Flow | GOV-015 NotificationHandler（子 Flow） |

> **治理語意權威**：本 Flow 的治理語意與一致性判斷依據請以 **06-guardrails-and-anti-cheating.md** 為權威。本章節僅提供施工步驟。

---

### B. Step 0：建構前必確認事項（必讀，否則必出錯）

在 Power Automate 建立此 Flow **之前**，請逐項確認：

| # | 確認項目 | 確認方式 | 不符處置 |
|:-----|:--------------------------|:----------------------------------------------|:-------------------------------|
| B1 | Dataverse 中 `Project Registry` 資料表存在且有 `gov_currentgate`、`gov_projectstatus`、`gov_projectname` 欄位 | Maker Portal → Dataverse → Tables → 搜尋 Project Registry | 先完成 02 文件 Dataverse Schema 建置 |
| B2 | `Review Decision Log` 資料表存在且有 `gov_requestedgate`、`gov_decision`、`gov_revieweddate`、`_gov_parentproject_value` 欄位 | 同上 | 先完成 Dataverse Schema 建置 |
| B3 | `Governance Violation Log` 資料表存在且有 `gov_violationtype`、`gov_expectedvalue`、`gov_actualvalue`、`gov_rollbackstatus`、`gov_parentproject` 欄位 | 同上 | 先完成 Dataverse Schema 建置 |
| B4 | GOV-015 NotificationHandler 已建立且處於**開啟**狀態 | Solution → Flows → 確認 GOV-015 狀態 | 先啟動 GOV-015 |
| B5 | CR-Dataverse-SPN Connection Reference 已指向有效 Service Principal 連線 | Solution → Connection References → CR-Dataverse-SPN | 先設定 Connection Reference |
| B6 | Service Principal 對 `Project Registry`、`Review Decision Log`、`Governance Violation Log` 均有讀寫權限 | Dataverse Security → 確認 SPN 角色 | 先設定 Dataverse 安全性角色 |

---

### C. Recurrence Trigger 設定（必須明確設定時區）

> **常見陷阱**：若不設定 Time Zone，Recurrence 預設為 UTC，導致台灣時間每天 08:00 才執行（比預期晚 8 小時）。

**在 Power Automate 設定方式：**
1. 新增 Trigger → 搜尋 `Recurrence` → 選擇「排程」下的「Recurrence」
2. 點選「Show advanced options（顯示進階選項）」
3. 填入以下值：

```
Trigger: Recurrence
Interval: 1
Frequency: Day
Time Zone: (UTC+08:00) Taipei
At These Hours: 0
At These Minutes: 0
```

> **驗證**：儲存後在 Flow Overview 頁面，確認「Next run」時間顯示為台灣時間 00:00。

---

### D. 一致性檢查邏輯說明

GOV-018 的核心邏輯是：

> **「Project Registry 的 `gov_currentgate`，應等於該專案在 Review Decision Log 中最新一筆 Approved 記錄的 `gov_requestedgate`」**

| 情境 | 正常（一致） | 異常（違規） |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| Gate1 申請已核准 | `gov_currentgate = 807660002`（Gate1已通過），最新 Approved 記錄 `gov_requestedgate = 807660002` | `gov_currentgate` 被人為改成 `807660003`，但 Log 中最新 Approved 只到 Gate1 |
| 無任何 Approved 記錄 | `gov_currentgate = 807660000`（Pending 初始） | `gov_currentgate != 807660000`（從未核准過卻有 Gate 值） |

**✅ [已修正 BUG-002] OptionSet 對照表（`gov_currentgate` / `gov_requestedgate`）：**

| 值 | 意義 |
|:----------|:----------------------------------------------|
| 807660000 | Pending（初始，尚未通過任何 Gate） |
| 807660001 | Gate0 已通過（Gate0 審批通過後 GOV-003 寫入） |
| 807660002 | Gate1 已通過（Gate1 審批通過後 GOV-003 寫入） |
| 807660003 | Gate2 已通過（Gate2 審批通過後 GOV-003 寫入） |
| 807660004 | Gate3 已通過（Gate3 審批通過後 GOV-003 寫入，最終狀態） |

> **一致性比對語義說明**：
> `gov_requestedgate`（RDL）= 「此次申請要通過的目標 Gate」
> `gov_currentgate`（Project Registry）= 「目前已通過的最高 Gate」
> 兩者使用相同 OptionSet 系列，Gate N 審批通過後，GOV-003 將 gov_currentgate 更新為相同值。
> 因此一致性條件為 **直接相等比對**（無需 offset）：
> `gov_requestedgate（RDL）== gov_currentgate（Project Registry）`

**`gov_decision` OptionSet（Review Decision Log）：**

| 值 | 意義 |
|:----------|:----------------------------------------------|
| 807660000 | Pending（待審批） |
| 807660001 | Approved（已核准） |
| 807660002 | Rejected（已拒絕） |

**`gov_rollbackstatus` OptionSet（Governance Violation Log）：**

| 值 | 意義 |
|:----------|:----------------------------------------------|
| 807660000 | Pending（待處理） |
| 807660001 | Closed（已處理） |
| 807660002 | ManualRequired（需人工介入） |

---

### E. 施工步驟（逐步建構）

> 建議**先完成 B. Step 0** 所有確認項目，再開始建構。

**Step 1：建立 Try-Catch Scope 外框**

1. 新增 Scope Action → 命名為 `Try-MainLogic`
2. 再新增第二個 Scope → 命名為 `Catch-ErrorHandler`
3. 在 `Catch-ErrorHandler` 上設定「Configure run after」：勾選 **Failed** 和 **Timed out**，取消勾選 Success

**Step 2：在 Try-MainLogic 內 — 列出所有 Active 專案**

1. 搜尋 `list rows` → 選擇「Microsoft Dataverse」下的「List rows（列出資料列）」
2. 命名：`List-ActiveProjects`
3. 設定：
   - Table name: `Project Registry`（gov_projectregistry）
   - Filter rows: `gov_projectstatus eq 807660000`
   - Select columns: `gov_projectregistryid,gov_currentgate,gov_projectname`

> **效能提示**：Select columns 只取必要欄位，可顯著降低每次 API 呼叫的資料傳輸量。

**Step 3：加入 Apply to each**

1. 搜尋 `apply to each` → 選擇「控制項」下的「Apply to each（套用至每一個）」
2. 命名：`ForEach-ActiveProject`
3. Input：選擇 `List-ActiveProjects` 的 `body/value`

**Step 4：在 Apply to each 內 — 查詢最新 Approved 記錄**

1. 搜尋 `list rows` → 選擇「Microsoft Dataverse」下的「List rows（列出資料列）」
2. 命名：`List-LatestApprovedReview`
3. 設定：
   - Table name: `Review Decision Log`（gov_reviewdecisionlog）
   - Filter rows:
     ```
     _gov_parentproject_value eq '@{items('ForEach-ActiveProject')?['gov_projectregistryid']}' and gov_decision eq 807660001
     ```
   - Order By: `gov_revieweddate desc`
   - Row count: `1`（只取最新一筆）

> **注意**：`_gov_parentproject_value` 是 Lookup 欄位的 OData 格式（前置 `_`，後置 `_value`）。

**Step 5：用 Compose 計算 ExpectedGate**

✅ [已修正 BUG-023] 新增語義說明，避免建構者誤加 offset (+1) 而導致比對邏輯錯誤

1. 搜尋 `compose` → 選擇「資料作業」下的「Compose（撰寫）」
2. 命名：`Compose-ExpectedGate`
3. Inputs 表達式（使用 Expression 模式輸入）：
   ```
   if(
     empty(outputs('List-LatestApprovedReview')?['body/value']),
     807660000,
     first(outputs('List-LatestApprovedReview')?['body/value'])?['gov_requestedgate']
   )
   ```
   > 若無任何 Approved 記錄，預期 CurrentGate 應為初始值 `807660000`。

> **⚠ 一致性比對語義（BUG-023 說明，請務必閱讀）**：
>
> 初次看到 `Compose-ExpectedGate` 直接取用 `gov_requestedgate` 時，
> 開發者常有疑問：「Gate0 申請通過後，RequestedGate = 807660001，
> 但 CurrentGate 應該從 807660000 → 807660001，為何不需要 +1？」
>
> 關鍵在於此系統的 OptionSet 設計：
> - `gov_requestedgate = 807660001` 的語義是「要申請通過 **Gate0**（第 0 道關卡）」
> - `gov_currentgate = 807660001` 的語義是「**Gate0 已通過**（目前最高通過狀態）」
> - 兩者的整數值 **807660001 代表的是同一件事：Gate0 通過狀態**
>
> 因此 GOV-003 審批通過後，直接將 `gov_currentgate` 設為與 `gov_requestedgate` 相同的整數值：
> `gov_requestedgate = 807660001 → GOV-003 設定 gov_currentgate = 807660001`
>
> 這意味著一致性條件就是 **直接相等**（`==`）：
> `ExpectedGate（來自 RDL.gov_requestedgate）== CurrentGate（來自 Project Registry.gov_currentgate）`
>
> **絕對不要加 offset（+1 或 -1）**，否則 GOV-018 將誤判所有正常專案為不一致。
> 參見 Section D「OptionSet 對照表」中的「一致性比對語義說明」。

**Step 6：用 Compose 取得 CurrentGate**

1. 搜尋 `compose` → 命名：`Compose-CurrentGate`
2. Inputs：
   ```
   @{items('ForEach-ActiveProject')?['gov_currentgate']}
   ```

**Step 7：加入 Condition — 一致性判斷**

1. 搜尋 `condition` → 選擇「控制項」下的「Condition（條件）」
2. 命名：`Condition-GateConsistency`
3. 設定：
   - Left value: `@{outputs('Compose-CurrentGate')}`
   - Operator: `is not equal to`
   - Right value: `@{outputs('Compose-ExpectedGate')}`

**Step 8：True 分支（不一致 → 記錄違規並通知）**

**Step 8a：寫入 Governance Violation Log**

1. 搜尋 `add a new row` → 選擇「Microsoft Dataverse」下的「Add a new row（新增資料列）」
2. 命名：`AddRow-ViolationLog`
3. 設定：
   - Table name: `Governance Violation Log`（gov_governanceviolationlog）
   - gov_violationtype: `ComplianceInconsistency`
   - gov_expectedvalue: `@{outputs('Compose-ExpectedGate')}`
   - gov_actualvalue: `@{outputs('Compose-CurrentGate')}`
   - gov_rollbackstatus: `807660002`（ManualRequired — 此 Flow 不自動回滾，需人工處理）
   - gov_parentproject（Lookup）: `gov_projectregistry(@{items('ForEach-ActiveProject')?['gov_projectregistryid']})`

> **注意**：Lookup 欄位必須使用 `EntityName(GUID)` 格式，不得只填 GUID 字串。

**Step 8b：呼叫 GOV-015 發送通知**

1. 搜尋 `run a child flow` → 選擇「Flows」下的「Run a Child Flow（執行子流程）」
2. 命名：`CallChildFlow-Notify-ComplianceViolation`
3. 設定：
   - Flow: `GOV-015 NotificationHandler`
   - NotificationType: `ComplianceAlert`
   - RecipientEmail: `[GOV-GovernanceLead 郵件群組]`（從環境變數或 Dataverse Config 取得）
   - Subject: `【治理警報】專案 Gate 狀態不一致`
   - Body:
     ```
     專案 @{items('ForEach-ActiveProject')?['gov_projectname']} 的 gov_currentgate（@{outputs('Compose-CurrentGate')}）與 Review Decision Log 不一致。
     預期值：@{outputs('Compose-ExpectedGate')}
     實際值：@{outputs('Compose-CurrentGate')}
     請至 Governance Violation Log 確認並手動修正。
     ```

**Step 9：False 分支（一致 → 不處理）**

False 分支保持空白。

**Step 10：在 Catch-ErrorHandler 內加入錯誤記錄**

1. 搜尋 `compose` → 命名 `Compose-CatchError`
2. Inputs：
   ```
   Flow Run Error in GOV-018 Compliance Reconciler at @{utcNow()} | Error: @{actions('Try-MainLogic')?['error']}
   ```
3. （可選）呼叫 GOV-015 通知管理員：NotificationType 設為 `SystemError`

---

### F. 最小驗證流程（MVP 測試，建構完成後立即執行）

> 目標：不等到隔天 00:00，立即驗證 GOV-018 基本運作。

1. **製造不一致狀態（人工注入）**
   - Dataverse → Project Registry → 找一個 Active 測試專案
   - 直接修改 `gov_currentgate` 欄位，使其與 Review Decision Log 最新 Approved 記錄不一致
   - 例：若最新 Approved 是 Gate1（807660001），將 `gov_currentgate` 改成 807660002

2. **手動觸發 Flow**
   - Power Automate → My flows → `GOV-018 Compliance Reconciler`
   - 點選「Run（執行）」→「Run flow（立即執行）」

3. **查看 Run History（定位方式）**
   - Power Automate → My flows → GOV-018 → 點選「28 day run history（28 天執行歷程）」
   - 找到剛才的執行 → 確認狀態為 `Succeeded（成功）`
   - 點進去 → 展開 `ForEach-ActiveProject` → 找測試專案對應的迭代（第幾個 item）
   - 確認 `Condition-GateConsistency` 的結果為 **True（不一致）**
   - 確認 `AddRow-ViolationLog` 執行成功（綠色打勾）

4. **確認 Governance Violation Log 有新記錄**
   - Dataverse → Governance Violation Log → 確認有一筆新記錄：
     - gov_violationtype = ComplianceInconsistency
     - gov_expectedvalue ≠ gov_actualvalue
     - gov_rollbackstatus = ManualRequired（807660002）

5. **確認通知已發送**
   - 查看 `CallChildFlow-Notify-ComplianceViolation` 執行成功
   - 查看 GOV-015 Run History 有對應記錄

6. **恢復測試資料並驗證無誤路徑**
   - 將測試專案 `gov_currentgate` 改回正確值
   - 重新手動觸發 → 確認 `Condition-GateConsistency` 為 **False（一致）**，無新違規記錄

---

### G. 常見失敗原因（可觀測訊號 + Run History 定位方式）

| # | 可觀測訊號 | 根本原因 | Run History 定位方式 | 修正方法 |
|:-----|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| G1 | Flow 成功但 Violation Log 無新記錄 | 測試資料實際一致，或 Condition 邏輯錯誤 | Run History → 展開 ForEach → 看 `Condition-GateConsistency` 結果是否為 False | 確認測試資料確實不一致；確認 ExpectedGate 與 CurrentGate 的實際值 |
| G2 | `List-LatestApprovedReview` 傳回空陣列（查無資料） | Filter 語法錯誤或 Lookup 欄位名稱錯誤 | Run History → 展開 `List-LatestApprovedReview` → 看 Inputs 的 Filter 字串與 Outputs 的 value | 確認 `_gov_parentproject_value` 格式（含前後底線）；確認 gov_decision OptionSet 值為 807660001 |
| G3 | `Compose-ExpectedGate` 傳回 null 或報錯 | `first()` 對空陣列操作失敗 | Run History → 展開 `Compose-ExpectedGate` → 看 Expression 執行結果 | 使用 `if(empty(...), 807660000, first(...)...)` 加入空陣列防護 |
| G4 | `AddRow-ViolationLog` 失敗（400 錯誤） | Lookup 欄位格式錯誤 | Run History → 展開 `AddRow-ViolationLog` → 看 Error message body | 確認 gov_parentproject 格式為 `gov_projectregistry(GUID)` 而非純 GUID 字串 |
| G5 | Flow 只掃描部分 Active 專案 | List rows 預設上限 5000 筆，未啟用 Pagination | Run History → 展開 `List-ActiveProjects` → 確認 Outputs 的 `@odata.nextLink` 是否存在 | 啟用 List rows 的「Enable Pagination（啟用分頁）」，Threshold 設為 10000 |
| G6 | Apply to each 執行極慢（> 5 分鐘） | 每筆專案都發 List rows 查詢，筆數多時耗時長 | Run History → 展開 Apply to each → 觀察每次迭代的耗時 | MVP 可接受；若效能問題嚴重，考慮 Batch 查詢優化 |
| G7 | Flow 在非預期時間執行 | Time Zone 未設定 | Run History → 看每筆執行的 Start time 是否為 00:00 UTC+8 | 確認 Recurrence Trigger 設定為 `(UTC+08:00) Taipei`，At These Hours: 0 |
| G8 | 通知未收到但 GOV-015 呼叫成功 | GOV-015 內部通知失敗（SMTP 或收件人設定問題） | 查看 GOV-015 Run History → 展開通知 Action 看錯誤 | 先獨立測試 GOV-015，確認通知功能正常 |

---

## GOV-019：SLA Monitor

### A. 基本資訊

| 項目 | 值 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 每日掃描所有 Pending 狀態的審批記錄（Review Decision Log），比對等待天數是否超過對應 Gate 的 SLA；超時時通知 Governance Lead 與 Engineering Management |
| Trigger 類型 | Recurrence（Schedule） |
| 執行頻率 | 每日 08:00 UTC+8（對應 UTC 00:00）—上班前推送 |
| Connection References | CR-Dataverse-SPN |
| 對應測試案例 | AC-006 |
| 依賴 Flow | GOV-015 NotificationHandler（子 Flow） |

> **治理語意權威**：本 Flow 的治理語意與 SLA 超時判斷依據請以 **06-guardrails-and-anti-cheating.md** 與 SOP-04 為權威。本章節僅提供施工步驟。

---

### B. Step 0：建構前必確認事項（必讀，否則必出錯）

| # | 確認項目 | 確認方式 | 不符處置 |
|:-----|:--------------------------|:----------------------------------------------|:-------------------------------|
| B1 | Review Decision Log 資料表有 `gov_decision`、`gov_requestedgate`、`gov_submitteddate`、`_gov_parentproject_value` 欄位 | Maker Portal → Dataverse → Tables → Review Decision Log | 先完成 Dataverse Schema 建置 |
| B2 | `gov_submitteddate` 欄位有資料（非 null）且格式為 datetime | Dataverse 直接查詢一筆 Pending 記錄 | 確認 GOV-002 正確寫入 gov_submitteddate |
| B3 | GOV-015 NotificationHandler 已建立且處於**開啟**狀態 | Solution → Flows → 確認 GOV-015 狀態 | 先啟動 GOV-015 |
| B4 | CR-Dataverse-SPN Connection Reference 已指向有效 Service Principal 連線 | Solution → Connection References | 先設定 Connection Reference |
| B5 | Service Principal 對 `Review Decision Log` 有讀取權限，對 `Governance Violation Log` 有寫入權限 | 確認 SPN 安全性角色 | 先設定 Dataverse 安全性角色 |
| B6 | 已確認 SLA 定義（來源：SOP-04）與本節 C 表一致 | 對照 C. SLA 定義表 | 若不一致，以 SOP-04 為準修正本節 |

---

### C. SLA 定義（來源：SOP-04，施工時以此為準）

| Gate | SLA（工作日） | MVP 閾值（日曆天，含緩衝） | `gov_requestedgate` OptionSet 值 |
|:-------------------------------|:-------------------------------|:-------------------------------|:-------------------------------|
| Gate 0 | 2 工作日 | 3 | 807660000 |
| Gate 1 | 3 工作日 | 4 | 807660001 |
| Gate 2 | 2 工作日 | 3 | 807660002 |
| Gate 3 | 3 工作日 | 4 | 807660003 |

> **MVP 說明**：Power Automate 標準函數無法計算「工作日」（需排除假日）。MVP 使用**日曆天數**作為近似值，設定放寬係數（工作日 + 1 = 日曆天閾值）。未來可接入 Microsoft 365 Calendar API 改為精確工作日計算。

---

### D. Recurrence Trigger 設定（必須明確設定時區）

> **常見陷阱**：若不設定 Time Zone，Recurrence 預設為 UTC，導致台灣時間下午 16:00 才執行，喪失「上班前通知」效果。

**在 Power Automate 設定方式：**
1. 新增 Trigger → 搜尋 `Recurrence` → 選擇「排程」下的「Recurrence」
2. 點選「Show advanced options（顯示進階選項）」
3. 填入以下值：

```
Trigger: Recurrence
Interval: 1
Frequency: Day
Time Zone: (UTC+08:00) Taipei
At These Hours: 8
At These Minutes: 0
```

---

### E. 施工步驟（逐步建構）

**Step 1：建立 Try-Catch Scope 外框**

1. 新增 Scope → 命名 `Try-MainLogic`
2. 再新增 Scope → 命名 `Catch-ErrorHandler`
3. `Catch-ErrorHandler` 設定「Configure run after」：勾選 **Failed** 和 **Timed out**，取消 Success

**Step 2：在 Try-MainLogic 內 — 取得今日 Ticks（用於 SLA 計算）**

1. 搜尋 `compose` → 命名 `Compose-TodayTicks`
2. Inputs（切換到 Expression 模式）：
   ```
   ticks(utcNow())
   ```

**Step 3：列出所有 Pending 審批記錄**

1. 搜尋 `list rows` → 選擇「Microsoft Dataverse」下的「List rows（列出資料列）」
2. 命名：`List-PendingReviews`
3. 設定：
   - Table name: `Review Decision Log`（gov_reviewdecisionlog）
   - Filter rows: `gov_decision eq 807660000`（Pending）
   - Select columns: `gov_reviewdecisionlogid,gov_requestedgate,gov_submitteddate,_gov_parentproject_value,gov_parentprojectname`

> **注意**：若 Pending 記錄可能超過 5000 筆，啟用「Enable Pagination（啟用分頁）」，Threshold 設為 10000。

**Step 4：加入 Apply to each**

1. 搜尋 `apply to each` → 選擇「控制項」下的「Apply to each（套用至每一個）」
2. 命名：`ForEach-PendingReview`
3. Input：`List-PendingReviews` 的 `body/value`

**Step 5：在 Apply to each 內 — 計算等待天數**

1. 搜尋 `compose` → 命名 `Compose-WaitingDays`
2. Inputs（Expression 模式）：
   ```
   div(
     sub(
       outputs('Compose-TodayTicks'),
       ticks(items('ForEach-PendingReview')?['gov_submitteddate'])
     ),
     864000000000
   )
   ```
   > **說明**：`ticks()` 回傳 100 奈秒計數。1 天 = 864,000,000,000 ticks（24 × 60 × 60 × 10,000,000）。結果為日曆天整數。

> **⚠ SLA 天數計算說明（Floor 除法行為）**：
> `div(sub(ticks(utcNow()), ticks(submittedDate)), 864000000000)` 使用整數除法，
> 不滿整天（24小時）的部分會被截斷。一個「逾期 5 天 23 小時」的申請計算結果為 5（未逾期），
> 而非 6。為補償此誤差，SLA 閾值判斷建議使用 `greaterOrEquals(計算結果, threshold - 1)` 或
> 將閾值設定為 `(SLA天數 - 1)` 以提前 1 天觸發催辦通知。

**Step 6：用 Switch 取得對應 Gate 的 SLA 閾值**

1. 搜尋 `switch` → 選擇「控制項」下的「Switch（切換）」
2. 命名：`Switch-GetSLAThreshold`
3. On：`@{items('ForEach-PendingReview')?['gov_requestedgate']}`
4. 加入以下 4 個 Cases（每個 Case 內加一個 Compose 動作，名稱各不相同）：

   | Case 值 | 命名 Compose | Inputs |
   |:-------------------------------|:----------------------------------------------|:-------------------------------|
   | `807660000` | `Compose-SLAThreshold-Gate0` | `3` |
   | `807660001` | `Compose-SLAThreshold-Gate1` | `4` |
   | `807660002` | `Compose-SLAThreshold-Gate2` | `3` |
   | `807660003` | `Compose-SLAThreshold-Gate3` | `4` |
   | Default | `Compose-SLAThreshold-Default` | `3` |

   > **重要**：每個 Case 的 Compose 名稱必須唯一，以避免 Power Automate 動作名稱衝突。Switch 結束後，使用以下 Compose 統一取得閾值：
   > + 新增步驟 → Compose → 重新命名為「Compose-SLAThresholdFinal」
   >   Inputs：運算式 →
   >   coalesce(
   >     outputs('Compose-SLAThreshold-Gate0'),
   >     outputs('Compose-SLAThreshold-Gate1'),
   >     outputs('Compose-SLAThreshold-Gate2'),
   >     outputs('Compose-SLAThreshold-Gate3'),
   >     outputs('Compose-SLAThreshold-Default')
   >   )
   > 後續步驟中使用 outputs('Compose-SLAThresholdFinal') 替代原本的 outputs('Compose-SLAThreshold')

**Step 7：加入 Condition — SLA 判斷**

1. 搜尋 `condition` → 選擇「控制項」下的「Condition（條件）」
2. 命名：`Condition-SLAViolated`
3. 設定：
   - Left value: `@{outputs('Compose-WaitingDays')}`
   - Operator: `is greater than`
   - Right value: `@{outputs('Compose-SLAThresholdFinal')}`

> **注意**：若想等於 SLA 天數當天就通知，改用 `is greater than or equal to`。

**Step 8：True 分支（超過 SLA）**

**Step 8a：（可選）寫入 Governance Violation Log**

1. 搜尋 `add a new row` → 命名 `AddRow-SLAViolation`
2. 設定：
   - Table name: `Governance Violation Log`
   - gov_violationtype: `SLAViolation`
   - gov_expectedvalue: `@{outputs('Compose-SLAThresholdFinal')} 天`
   - gov_actualvalue: `@{outputs('Compose-WaitingDays')} 天`
   - gov_rollbackstatus: `807660002`（ManualRequired）
   - gov_parentproject: `gov_projectregistry(@{items('ForEach-PendingReview')?['_gov_parentproject_value']})`

**Step 8b：呼叫 GOV-015 發送 SLA 通知**

1. 搜尋 `run a child flow` → 命名 `CallChildFlow-Notify-SLAViolation`
2. 設定：
   - Flow: `GOV-015 NotificationHandler`
   - NotificationType: `SLAViolation`
   - RecipientEmail: `[GOV-GovernanceLead];[GOV-EngineeringManagement]`（以分號分隔）
   - Subject:
     ```
     【SLA 警報】Gate @{items('ForEach-PendingReview')?['gov_requestedgate']} 審批已逾期
     ```
   - Body:
     ```
     專案 @{items('ForEach-PendingReview')?['gov_parentprojectname']} 的 Gate @{items('ForEach-PendingReview')?['gov_requestedgate']} 審批已等待 @{outputs('Compose-WaitingDays')} 天，超過 SLA @{outputs('Compose-SLAThresholdFinal')} 天。
     提交時間：@{items('ForEach-PendingReview')?['gov_submitteddate']}
     請至 Review Decision Log 確認審批進度。
     ```

**Step 9：False 分支（未超過 SLA）**

False 分支保持空白。

**Step 10：Catch-ErrorHandler 內加入錯誤記錄**

1. 搜尋 `compose` → 命名 `Compose-CatchError`
2. Inputs：
   ```
   Flow Run Error in GOV-019 SLA Monitor at @{utcNow()} | Error: @{actions('Try-MainLogic')?['error']}
   ```

---

### F. 最小驗證流程（MVP 測試，建構完成後立即執行）

**前提：已有測試用的 Pending 審批記錄，且 `gov_submitteddate` 值足夠舊。**

1. **製造超時狀態（人工注入）**
   - Dataverse → Review Decision Log → 找一筆 `gov_decision = 807660000（Pending）` 的測試記錄
   - 將 `gov_submitteddate` 改為 7 天前的日期（確保超過所有 Gate 的 SLA 閾值）

2. **手動觸發 Flow**
   - Power Automate → My flows → `GOV-019 SLA Monitor`
   - 點選「Run（執行）」→「Run flow（立即執行）」

3. **查看 Run History（定位方式）**
   - Power Automate → My flows → GOV-019 → 點選「28 day run history（28 天執行歷程）」
   - 找到執行記錄 → 確認狀態為 `Succeeded（成功）`
   - 點進去 → 展開 `ForEach-PendingReview` → 找測試記錄對應的迭代
   - 確認 `Compose-WaitingDays` 輸出值 > 0（預期約 7）
   - 確認 `Switch-GetSLAThreshold` 進入正確的 Case（非 Default）
   - 確認 `Condition-SLAViolated` 結果為 **True**

4. **確認通知已發送**
   - 查看 `CallChildFlow-Notify-SLAViolation` 執行成功
   - 查看 GOV-015 Run History 有對應記錄
   - 確認通知信件已送達指定信箱

5. **確認 Governance Violation Log 有記錄（若已建構 Step 8a）**
   - Dataverse → Governance Violation Log → 確認有 gov_violationtype = SLAViolation 的新記錄

6. **測試無超時情境**
   - 將測試記錄的 `gov_submitteddate` 改為今天
   - 重新手動觸發
   - 確認 `Condition-SLAViolated` 為 **False**，無通知發出

---

### G. 常見失敗原因（可觀測訊號 + Run History 定位方式）

| # | 可觀測訊號 | 根本原因 | Run History 定位方式 | 修正方法 |
|:-----|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| G1 | Flow 成功但未發出任何通知 | 所有 Pending 記錄未超時，或 List rows 查無資料 | Run History → 展開 `List-PendingReviews` → 確認 Outputs 的 value 陣列是否有資料 | 確認測試資料 gov_decision = 807660000；確認 gov_submitteddate 足夠舊 |
| G2 | `Compose-WaitingDays` 輸出 0 或負數 | gov_submitteddate 欄位為 null 或未來時間 | Run History → 展開 `Compose-WaitingDays` → 看 `ticks(items()['gov_submitteddate'])` 的值 | 確認 GOV-002 正確寫入 gov_submitteddate；確認時間格式為 ISO 8601（含 UTC 標記 Z） |
| G3 | `Condition-SLAViolated` 恆為 False | SLA 閾值太大，或 WaitingDays 計算結果為字串型別無法比較 | Run History → 展開 `Compose-WaitingDays` 與 `Compose-SLAThresholdFinal` → 確認兩者都是數字 | 在 Condition 中加 `int()` 轉換：`@{int(outputs('Compose-WaitingDays'))}` |
| G4 | Switch 恆進入 Default（SLA 值恆為 3） | gov_requestedgate 的實際值不符合 Case 定義 | Run History → 展開 `ForEach-PendingReview` → 確認 `items()?['gov_requestedgate']` 的實際值 | 確認 OptionSet 值（807660000~807660003）；確認 Switch Case 值與 OptionSet 完全一致 |
| G5 | Flow 掃描不到部分 Pending 記錄 | List rows 未啟用 Pagination（> 5000 筆截斷） | Run History → 展開 `List-PendingReviews` → 確認 Outputs 中 `@odata.nextLink` 是否存在 | 啟用 List rows 的「Enable Pagination」，Threshold 設為 10000 |
| G6 | `AddRow-SLAViolation` 失敗（400 錯誤） | Lookup 欄位格式錯誤 | Run History → 展開 `AddRow-SLAViolation` → 看 Error body | 確認 gov_parentproject 格式：`gov_projectregistry(GUID)` |
| G7 | 同一筆記錄每天重複通知（預期行為） | 設計如此；若需去重，需加入已存在違規記錄的查詢 | Run History → 確認同一 Review ID 每天都觸發 True 分支 | 加入 List rows 查詢已存在的 SLAViolation 記錄；若有未關閉記錄則跳過（MVP 可接受重複通知） |
| G8 | Flow 在非預期時間執行 | Time Zone 未設定或設錯 | Run History → 看 Start time 是否為 08:00 UTC+8 | 確認 Recurrence 設定為 `(UTC+08:00) Taipei`，At These Hours: 8 |

---

## GOV-020：Document Inventory Parser（文件清冊解析器）

### A. 基本資訊

| 項目 | 值 |
|:--------------------------|:--------------------------------------------------------------|
| Flow 名稱 | GOV-020 Document Inventory Parser |
| 目的 | 接收系統設計師上傳的 Excel 文件清冊，解析每一列，在 Document Register 預建 Planned 記錄（含 gov_expectedfilename），供 GOV-005 Phase 1B 匹配；同時自身也作為 DocumentInventory 類型的 Draft 記錄寫入 Document Register |
| Trigger 類型 | **Power Apps (V2)** |
| 觸發來源 | FORM-003 或專屬 FORM-006 Document Inventory Upload Form |
| Connection References | CR-Dataverse-SPN, CR-SharePoint-SPN, CR-Excel-SPN（Excel Online Business） |
| Concurrency Control | **建議開啟**（Parallelism = 1，防止同一專案重複解析） |
| 依賴 Child Flow | GOV-015（Notification Handler） |
| 前置 Flow | GOV-001（專案須已建立） |
| 對應測試案例 | 07文件 E2E-020 |

> **設計定位**：GOV-020 是 GOV-005 Phase 1B 的「前置建倉」步驟。
> 文件清冊列出的每個預期交付文件，在 Dataverse 建立 Planned 記錄（空殼），
> 等待設計師實際上傳對應檔案時，GOV-005 Phase 1B 自動識別並升級為 Draft。

### Step 0：GOV-020 起手式必檢 8 項

> **為什麼需要 Step 0？** Excel Online Business 連線是最常見的卡關原因；Excel 需要已發佈為「資料表（Table）」格式，Action 才能讀取欄位。

**必檢 1：Excel 清冊範本已建立並上傳至 SharePoint**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | GOV-020 使用「List rows present in a table」讀取 Excel，Excel 需先存在於 SharePoint |
| 操作路徑 | SharePoint → Design Documents → Templates → 確認有 `DocumentInventory_Template.xlsx` |
| 成功長相 | 可在 SharePoint 找到並開啟模板 |
| 失敗長相 | 找不到文件 |
| 下一步 | 依 B. 節建立 Excel 範本 → 上傳至 SharePoint Templates 資料夾 |

**必檢 2：Excel 中有名為「DocumentInventory」的資料表（Table）**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 「List rows present in a table」Action 需要指定 Table 名稱（非 Sheet 名稱） |
| 操作路徑 | 開啟 Excel → 選取資料範圍 → 插入 → 資料表 → 名稱改為 `DocumentInventory` |
| 成功長相 | Excel 功能區顯示「資料表名稱：DocumentInventory」 |
| 失敗長相 | Power Automate 連線後 Table 下拉清單為空 |
| 下一步 | 在 Excel 中建立具名資料表 → 重新上傳至 SharePoint |

**必檢 3：Excel Online Business Connection Reference 已授權**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | 讀取 SharePoint 上的 Excel 需要 Excel Online Business 連線 |
| 操作路徑 | Maker Portal → 解決方案 → Connection References → 找到 CR-Excel-SPN → 確認已連線（無 ⚠️） |
| 成功長相 | 顯示已連線帳號 |
| 失敗長相 | 有 ⚠️ 標記 |
| 下一步 | 點擊 → 選擇服務主體或個人帳號連線 |

**必檢 4：SharePoint Templates 資料夾已存在**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | GOV-020 將收到的 Excel 寫入此資料夾後再讀取 |
| 操作路徑 | SharePoint → Design Documents → 確認有 `Templates` 資料夾（含 `{ProjectId}/` 子結構） |
| 成功長相 | 資料夾存在 |
| 失敗長相 | 找不到 |
| 下一步 | 手動在 SharePoint 建立 `Templates` 資料夾；或由 GOV-001 擴充自動建立 |

**必檢 5：Document Register 有 gov_expectedfilename 欄位（必檢 13 同 GOV-005）**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | GOV-020 寫入 Planned 記錄時填入 gov_expectedfilename；欄位不存在則 Add a row 失敗 |
| 操作路徑 | Dataverse → Document Register → 資料行 → 確認有 gov_expectedfilename（文字） |
| 成功長相 | 欄位存在 |
| 失敗長相 | 欄位不存在 |
| 下一步 | 建立欄位（參見 GOV-005 必檢 13） |

**必檢 6：GOV-005 已建立且處於 On 狀態**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | GOV-020 的 Planned 記錄需要 GOV-005 Phase 1B 才能承接升級；無法在 GOV-020 自己測試此連鎖 |
| 操作路徑 | Flow 清單 → GOV-005 → 狀態為「開啟」 |
| 成功長相 | 狀態為 On |
| 失敗長相 | Off 或不存在 |
| 下一步 | 先完成 GOV-005 建立 |

**必檢 7：DocumentInventory OptionSet 值已加入 Document Register 的 gov_documenttype**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | GOV-020 自身也需要在 Document Register 建一筆清冊記錄，DocumentType = DocumentInventory |
| 操作路徑 | Dataverse → 選擇集 → gov_documenttype → 確認有 DocumentInventory 選項 |
| 成功長相 | 有 DocumentInventory 選項（對應整數值） |
| 失敗長相 | 找不到 |
| 下一步 | 選擇集 → gov_documenttype → 新增標籤「DocumentInventory」→ 儲存 → 記錄 OptionSet 整數值 |

**必檢 8：所有 Respond 的欄位集合完全一致（Canonical Error Envelope v5.0）**

| 項目 | 內容 |
|:--------------------------|:--------------------------------------------------------------|
| 目的 | GOV-020 有多個 Respond 路徑（Pre-check 失敗、解析失敗、成功），Schema 不一致報錯 |
| 操作路徑 | 開啟 GOV-020 → 找到所有 Respond → 確認每個都有 9 欄位 + `PlannedCount` 共 10 欄位 |
| 成功長相 | 所有 Respond 欄位完全相同 |
| 失敗長相 | 有 Respond 欄位數量不一致 |
| 下一步 | 在失敗 Respond 補上缺少的欄位，值填空白字串或 0 |

### B. Excel 文件清冊範本規格

#### 必要欄位（Excel Table 欄位名稱必須完全一致）

| 欄位名稱（Table Header） | 類型 | 必填 | 說明 |
|:----------------------------------------------|:----------------------|:------:|:----------------------------------------------|
| **DocumentName** | 文字 | ✓ | 文件顯示名稱，如「系統設計基準文件」 |
| **ExpectedFileName** | 文字 | ✓ | 預期上傳的完整檔名（含副檔名），如 `DesignBaseline_Campus.pdf`；此值寫入 gov_expectedfilename |
| **DocumentType** | 文字 | ✓ | 對應 gov_documenttype 的 OptionSet 文字名稱，如 `DesignBaseline` |
| **RequiredForGate** | 文字 | ✓ | 對應交付的 Gate（Gate0 / Gate1 / Gate2 / Gate3 / NA） |
| **DeliverablePackage** | 文字 | ✗ | CoreDeliverable / SupplementaryDeliverable / AdHoc（留空預設 CoreDeliverable） |
| **Description** | 文字 | ✗ | 文件說明（可空白） |

> **⚠ 範本規則**：
> 1. 欄位名稱大小寫必須完全一致（ExpectedFileName 不可寫成 expectedfilename）
> 2. 不可合併儲存格
> 3. 第一列必須是標題列（Power Automate 自動識別 Table Header）
> 4. 範本下載：在 SharePoint → Design Documents → Templates → `DocumentInventory_Template.xlsx`

### C. Input / Output 定義

**Input（Power Apps (V2) Trigger 參數）**：

| 參數名稱 | 類型 | 必填 | 說明 |
|:--------------------------|:----------------------|:------:|:----------------------------------------------|
| ProjectId | Text | ✓ | Dataverse gov_projectregistryid（GUID） |
| FileName | Text | ✓ | Excel 清冊檔名（含副檔名），如 `DocInventory_Campus_v1.0.xlsx` |
| FileContent | Text | ✓ | Base64 編碼的 Excel 檔案內容（參見 GOV-005 Base64 限制說明） |
| SubmittedBy | Text | ✓ | 提交者 Email |

**Output（Canonical Error Envelope v5.0 + PlannedCount）**：

| 輸出參數 | 類型 | 說明 |
|:----------------------------------------------|:----------------------|:----------------------------------------------|
| StatusCode | Number | 200 / 400 / 500 |
| Status | Text | Success / Failed |
| ErrorCode | Text | 錯誤代碼（成功時空白） |
| ErrorStage | Text | 失敗階段（成功時空白） |
| Message | Text | 結果訊息 |
| SharePointFileLink | Text | 清冊 Excel 的 SharePoint URL |
| DocumentRegisterRowId | Text | 清冊本身在 Document Register 的 GUID |
| FlowRunId | Text | `workflow()?['run']?['name']` |
| Timestamp | Text | `utcNow()` |
| PlannedCount | Number | 本次成功建立的 Planned 記錄數量（0 表示清冊解析成功但無新記錄需建立） |

### D. 建立步驟（逐步點擊）

**步驟 1**：建立 Power Apps (V2) Trigger + Initialize variables
```
Action：Power Apps (V2) Trigger
  + Add an input → Text → ProjectId
  + Add an input → Text → FileName
  + Add an input → Text → FileContent
  + Add an input → Text → SubmittedBy

Action：Initialize variable（必須在 Trigger 正下方，Flow 最頂層）
  Name：InventoryFilePath
  Type：String
  Value：（空白）
  說明：存放 Excel 寫入 SharePoint 後的完整路徑，供 List rows 使用

Action：Initialize variable
  Name：PlannedCount
  Type：Integer
  Value：0
  說明：記錄成功建立的 Planned 記錄總數，回傳給 Power Apps

Action：Initialize variable
  Name：InventoryDocId
  Type：String
  Value：（空白）
  說明：存放清冊本身在 Document Register 的 GUID
```

**步驟 2**：Pre-check（驗證專案狀態）
```
Action：Get a row by ID (Dataverse)
  Table name：Project Registry
  Row ID：@{triggerBody()['ProjectId']}
  重新命名為「Get_Project」

Action：Condition（專案為 Active？）
  條件：outputs('Get_Project')?['body/gov_projectstatus'] is equal to 807660000
  False 分支：
    Respond to a PowerApp or flow → StatusCode: 400, Status: Failed,
    ErrorCode: ERR-020-001, ErrorStage: PreCheck,
    Message: 專案不存在或非 Active 狀態,
    SharePointFileLink: （空白）, DocumentRegisterRowId: （空白）,
    FlowRunId: @{workflow()?['run']?['name']}, Timestamp: @{utcNow()},
    PlannedCount: 0
    Terminate → Cancelled
```

**步驟 3**：上傳 Excel 至 SharePoint（暫存供後續讀取）
```
說明：先將 Excel 寫入 SharePoint，再由 List rows 讀取內容。
     這是 Power Automate 讀取動態 Excel 的唯一實用方式
     （List rows 需要 SharePoint 上的實際檔案路徑，不支援純記憶體 Base64 操作）。

Action：Create file (SharePoint)
  （搜尋 create file → 選擇「SharePoint」下的「Create file」）
  連線：CR-SharePoint-SPN
  Site Address：選擇 Design Governance Site
  Folder Path：/Documents/Templates/@{triggerBody()['ProjectId']}
  File Name：@{triggerBody()['FileName']}
  File Content：@{base64ToBinary(triggerBody()['FileContent'])}
  重新命名為「Upload_InventoryExcel」

Action：Compose（取得 SharePoint URL）
  重新命名為「Compose-InventoryFileURL」
  Inputs：@{outputs('Upload_InventoryExcel')?['body/{Link}']}

Action：Set variable
  Name：InventoryFilePath
  Value：/Documents/Templates/@{triggerBody()['ProjectId']}/@{triggerBody()['FileName']}
  說明：List rows 使用此路徑，格式為相對路徑（從 Document Library 根目錄起）
```

**步驟 4**：讀取 Excel 清冊內容
```
Action：List rows present in a table (Excel Online Business)
  （搜尋 list rows present → 選擇「Excel Online (Business)」下的「List rows present in a table」）
  連線：CR-Excel-SPN（MVP 模式：個人帳號 Excel Online Business 連線）
  Location：選擇 SharePoint Site（Design Governance Site）
  Document Library：Documents
  File：@{variables('InventoryFilePath')}
  Table：DocumentInventory
  重新命名為「List_InventoryRows」

Action：Condition（有資料列？）
  條件：length(outputs('List_InventoryRows')?['body/value']) greater than 0
  False 分支：
    Respond to a PowerApp or flow → StatusCode: 400, Status: Failed,
    ErrorCode: ERR-020-002, ErrorStage: ExcelParse,
    Message: Excel 清冊無資料列，請確認 Table 名稱為 DocumentInventory 且有至少一列資料,
    SharePointFileLink: @{outputs('Compose-InventoryFileURL')},
    DocumentRegisterRowId: （空白）,
    FlowRunId: @{workflow()?['run']?['name']}, Timestamp: @{utcNow()},
    PlannedCount: 0
    Terminate → Cancelled

⚠ 注意：File 欄位的路徑分隔符號在 Excel Online Business Action 中可能需要使用「/」（正斜線）。
        若路徑錯誤，Action 本身會失敗進入 Catch。
```

**步驟 5**：逐列建立 Planned 記錄（Apply to each）
```
Action：Apply to each
  （搜尋 apply to each → 選擇「控制項」下的「Apply to each」）
  Output From：outputs('List_InventoryRows')?['body/value']
  重新命名為「ForEach-InventoryRow」

  // 5a. 檢查此 ExpectedFileName 是否已存在 Planned 記錄（防重複建立）
  Action：List rows (Dataverse)
    Table name：Document Register
    Filter rows：_gov_parentproject_value eq '@{triggerBody()['ProjectId']}'
                 and gov_expectedfilename eq '@{trim(items('ForEach-InventoryRow')?['ExpectedFileName'])}'
                 and gov_documentrole eq 807660000
    Row count：1
    重新命名為「Check_DuplicatePlanned」
    說明：重複執行文件清冊時，已存在的 Planned 記錄不再重複建立

  // 5b. 只在無重複記錄時建立
  Action：Condition（此 ExpectedFileName 的 Planned 記錄是否已存在？）
    條件：length(outputs('Check_DuplicatePlanned')?['body/value']) is equal to 0

    True 分支（不存在 → 建立新 Planned 記錄）：

      ✅ [已修正 BUG-013] Add_PlannedRecord 前置步驟：動態解析三個 OptionSet 欄位

      // 5b-1. 解析 DocumentType OptionSet
      Action：Compose
        重新命名為「Compose-DocTypeInt」
        Inputs：運算式 →
        if(equals(items('ForEach-InventoryRow')?['DocumentType'], 'TechnicalFeasibility'), 807660000,
        if(equals(items('ForEach-InventoryRow')?['DocumentType'], 'InitialRiskList'), 807660001,
        if(equals(items('ForEach-InventoryRow')?['DocumentType'], 'RiskAssessmentStrategy'), 807660002,
        if(equals(items('ForEach-InventoryRow')?['DocumentType'], 'DesignBaseline'), 807660003,
        if(equals(items('ForEach-InventoryRow')?['DocumentType'], 'RiskAssessment'), 807660004,
        if(equals(items('ForEach-InventoryRow')?['DocumentType'], 'IEC62443Checklist'), 807660005,
        if(equals(items('ForEach-InventoryRow')?['DocumentType'], 'ThreatModel'), 807660006,
        if(equals(items('ForEach-InventoryRow')?['DocumentType'], 'RequirementTraceability'), 807660007,
        if(equals(items('ForEach-InventoryRow')?['DocumentType'], 'TestPlan'), 807660008,
        if(equals(items('ForEach-InventoryRow')?['DocumentType'], 'TestReport'), 807660009,
        if(equals(items('ForEach-InventoryRow')?['DocumentType'], 'HandoverMeeting'), 807660010,
        if(equals(items('ForEach-InventoryRow')?['DocumentType'], 'ResidualRiskList'), 807660011,
        if(equals(items('ForEach-InventoryRow')?['DocumentType'], 'Other'), 807660012,
        if(equals(items('ForEach-InventoryRow')?['DocumentType'], 'DesignObjectInventory'), 807660013,
        if(equals(items('ForEach-InventoryRow')?['DocumentType'], 'ChangeImpact'), 807660014,
        if(equals(items('ForEach-InventoryRow')?['DocumentType'], 'DocumentRegister'), 807660015,
        -1))))))))))))))))

      // 5b-2. DocumentType 有效性檢查
      Action：Condition
        重新命名為「Condition-ValidDocType」
        條件：outputs('Compose-DocTypeInt') is not equal to -1
        False 分支（未知 DocumentType）：
          Append to array variable → varSkippedRows
          Value：@{items('ForEach-InventoryRow')?['DocumentName']} — Unknown DocumentType: @{items('ForEach-InventoryRow')?['DocumentType']}
          → （跳過此列，繼續 ForEach）

        True 分支（繼續）：

      // 5b-3. 解析 RequiredForGate OptionSet
      Action：Compose
        重新命名為「Compose-RequiredGateInt」
        Inputs：運算式 →
        if(equals(items('ForEach-InventoryRow')?['RequiredForGate'], 'Gate0'), 'Gate0',
        if(equals(items('ForEach-InventoryRow')?['RequiredForGate'], 'Gate1'), 'Gate1',
        if(equals(items('ForEach-InventoryRow')?['RequiredForGate'], 'Gate2'), 'Gate2',
        if(equals(items('ForEach-InventoryRow')?['RequiredForGate'], 'Gate3'), 'Gate3',
        '-'))))
        （'-' = 非 Gate 強制文件，對應 Excel 中的 '-' 或空白）

        **注意**：gov_requiredforgate 在 02-dataverse-data-model 中定義為 Text 欄位（Multiple lines of text, 100），此處使用的值為文字格式的 Gate 代碼（如 'Gate0', 'Gate1'），非 OptionSet 整數。

      // 5b-4. 解析 DeliverablePackage OptionSet
      Action：Compose
        重新命名為「Compose-DeliverablePackageInt」
        Inputs：運算式 →
        if(equals(items('ForEach-InventoryRow')?['DeliverablePackage'], 'CoreDeliverable'), 807660000,
        if(equals(items('ForEach-InventoryRow')?['DeliverablePackage'], 'SupplementaryDeliverable'), 807660001,
        if(equals(items('ForEach-InventoryRow')?['DeliverablePackage'], 'AdHoc'), 807660002,
        807660000)))
        （預設 807660000 = CoreDeliverable）

      Action：Add a new row (Dataverse)
        （搜尋 add a new row → 選擇「Microsoft Dataverse」下的「Add a new row」）
        連線：CR-Dataverse-SPN
        Table name：Document Register
        重新命名為「Add_PlannedRecord」
        欄位對應：
          gov_documentid：@{concat('PLN-', outputs('Get_Project')?['body/gov_requestid'], '-', items('ForEach-InventoryRow')?['DocumentType'], '-', formatDateTime(utcNow(), 'yyyyMMddHHmmss'))}
          gov_parentproject：@{triggerBody()['ProjectId']}
          gov_documenttype：outputs('Compose-DocTypeInt')
          gov_documentname：@{items('ForEach-InventoryRow')?['DocumentName']}
          gov_expectedfilename：@{trim(items('ForEach-InventoryRow')?['ExpectedFileName'])}
          gov_requiredforgate：outputs('Compose-RequiredGateInt')
          gov_deliverablepackage：outputs('Compose-DeliverablePackageInt')
          gov_documentrole：807660000（Planned）
          gov_isfrozen：false
          gov_comments：@{items('ForEach-InventoryRow')?['Description']}
        說明：gov_filename 不填（尚未實際上傳）；gov_versionnumber_major/minor 不填（待 GOV-005 Phase 1B 時設定）

      Action：Increment variable
        （搜尋 increment variable → 選擇「Variable」下的「Increment variable」）
        Name：PlannedCount
        Value：1

    False 分支（已存在 → 跳過，不重複建立）：
      Action：Compose（記錄跳過）
        重新命名為「Compose-SkipDuplicate」
        Inputs：@{concat('跳過重複：', items('ForEach-InventoryRow')?['ExpectedFileName'])}
```

**步驟 6**：清冊本身建立 Document Register 記錄
```
說明：文件清冊 Excel 本身也是一份治理文件，需要在 Document Register 建立記錄（DocumentType = DocumentInventory），
     並套用 GOV-005 的 FileName 版本控制邏輯（但此處為簡化版：直接新建 Draft，不做 Phase 查詢）。

Action：Add a new row (Dataverse)
  Table name：Document Register
  重新命名為「Add_InventoryDocRecord」
  欄位對應：
    gov_documentid：@{concat('INV-', outputs('Get_Project')?['body/gov_requestid'], '-', formatDateTime(utcNow(), 'yyyyMMddHHmmss'))}
    gov_parentproject：@{triggerBody()['ProjectId']}
    gov_documenttype：@{DocumentInventory 的 OptionSet 整數值}
    gov_documentname：@{triggerBody()['FileName']}
    gov_filename：@{trim(triggerBody()['FileName'])}
    gov_versionnumber_major：1
    gov_versionnumber_minor：0
    gov_versionlabel：1.0
    gov_sharepointfilelink：@{outputs('Compose-InventoryFileURL')}
    gov_uploadedby：@{triggerBody()['SubmittedBy']}
    gov_uploadeddate：@{utcNow()}
    gov_documentrole：807660001（Draft）
    gov_deliverablepackage：807660000（CoreDeliverable）
    gov_isfrozen：false

Action：Set variable
  Name：InventoryDocId
  Value：@{outputs('Add_InventoryDocRecord')?['body/gov_documentregisterid']}
```

**步驟 7**：發送通知
```
Action：Run a Child Flow
  Child Flow：GOV-015-NotificationHandler
  輸入：
    NotificationType：DocumentUploaded
    RecipientEmail：@{triggerBody()['SubmittedBy']}
    Subject：文件清冊已上傳 — @{outputs('Get_Project')?['body/gov_requestid']}
    Body：專案 @{outputs('Get_Project')?['body/gov_requestid']} 的文件清冊已解析完成，共建立 @{variables('PlannedCount')} 筆預期交付文件記錄。請前往 Document Register 確認後，依序上傳各設計文件。
```

**步驟 8**：成功回應
```
Action：Respond to a PowerApp or flow
  - Number：StatusCode → 200
  - Text：Status → Success
  - Text：ErrorCode → （空白）
  - Text：ErrorStage → （空白）
  - Text：Message → 文件清冊解析完成，已建立 @{variables('PlannedCount')} 筆 Planned 記錄
  - Text：SharePointFileLink → @{outputs('Compose-InventoryFileURL')}
  - Text：DocumentRegisterRowId → @{variables('InventoryDocId')}
  - Text：FlowRunId → @{workflow()?['run']?['name']}
  - Text：Timestamp → @{utcNow()}
  - Number：PlannedCount → @{variables('PlannedCount')}
```

**步驟 9**：Catch-ErrorHandler
```
Scope：Catch-ErrorHandler
設定 Configure run after：取消「成功」→ 勾選「已失敗」與「已逾時」

Action：Compose-ErrorMessage
  Inputs：@{coalesce(result('Try-MainLogic')?[0]?['error']?['message'], '未知錯誤')}

Action：Respond to a PowerApp or flow
  - Number：StatusCode → 500
  - Text：Status → Failed
  - Text：ErrorCode → ERR-SYSTEM-500
  - Text：ErrorStage → CatchHandler
  - Text：Message → @{outputs('Compose-ErrorMessage')}
  - Text：SharePointFileLink → （空白）
  - Text：DocumentRegisterRowId → （空白）
  - Text：FlowRunId → @{workflow()?['run']?['name']}
  - Text：Timestamp → @{utcNow()}
  - Number：PlannedCount → 0
```

**步驟 10**：儲存
```
點擊左上角 Flow 名稱 → 輸入「GOV-020-DocumentInventoryParser」→ 點擊「Save」
```

### E. 最小驗證流程

**第 1 步：準備 Excel 清冊測試檔**
```
1. 開啟 DocumentInventory_Template.xlsx（從 SharePoint Templates 下載）
2. 填入 3 列測試資料：
   列 1：DocumentName=「設計基準文件」, ExpectedFileName=DesignBaseline_Campus.pdf,
         DocumentType=DesignBaseline, RequiredForGate=Gate1
   列 2：DocumentName=「風險評估報告」, ExpectedFileName=RiskAssessment_Campus.pdf,
         DocumentType=RiskAssessment, RequiredForGate=Gate1
   列 3：DocumentName=「IEC62443清查表」, ExpectedFileName=IEC62443_Campus.xlsx,
         DocumentType=IEC62443Checklist, RequiredForGate=Gate2
3. 確認 Table 名稱為 DocumentInventory（Excel → 插入 → 資料表 → 查看名稱）
4. 存檔
```

**第 2 步：從 Power Apps 上傳清冊**
```
1. 開啟 FORM-003 或 FORM-006
2. 選擇測試專案（Active 狀態）
3. 選擇並附加準備好的 DocumentInventory_Template.xlsx
4. 點擊「上傳清冊」按鈕
5. 預期 Notify 訊息：「文件清冊解析完成，已建立 3 筆 Planned 記錄」
```

**第 3 步：驗收 Dataverse 記錄**
```
1. Dataverse → Document Register → 篩選 gov_parentproject = 測試專案
2. 確認有 3 筆 gov_documentrole = Planned（807660000）的新記錄
3. 每筆確認：
   - gov_expectedfilename 有值（DesignBaseline_Campus.pdf 等）
   - gov_filename 為空（尚未實際上傳）
   - gov_versionnumber_major / minor 為空（待第一次上傳時設定）
4. 另確認有 1 筆 gov_documenttype = DocumentInventory 的 Draft 記錄（清冊本身）
```

**第 4 步：驗證 Phase 1B 銜接（用 GOV-005 上傳對應檔案）**
```
1. 在 FORM-003 上傳 DesignBaseline_Campus.pdf（FileName 完全一致）
2. ChangeType = Major（首次交付）
3. 觀察 GOV-005 Run History：
   ✓ Lookup_ByFileName → 0 筆（Phase 1 無命中）
   ✓ Lookup_ByExpectedFileName → 1 筆（Phase 1B 命中 Planned 記錄！）
   ✓ Condition（Phase 1B 命中？）→ True
   ✓ Set MatchedByExpectedFileName = true
   ✓ Set PlannedRecordId = （Planned 記錄 GUID）
   ✓ Condition（Path A — Phase 1B Planned 升級？）→ True
   ✓ Update_PlannedToDraft（Planned 記錄升級為 Draft）
4. Dataverse 確認：
   該記錄 gov_documentrole = 807660001（Draft）
   gov_filename = DesignBaseline_Campus.pdf（已填入）
   gov_versionnumber_major = 1, gov_versionnumber_minor = 0
   gov_versionlabel = "1.0"
```

**第 5 步：驗收 GOV-018 清冊追蹤（延伸驗證）**
```
若 GOV-018 已設定監控 Planned 記錄交付狀態：
1. 等待 GOV-018 下次執行（或手動觸發）
2. 確認 GOV-018 識別出「已 Planned 但尚未上傳」的 2 筆記錄（RiskAssessment、IEC62443Checklist）
3. 確認系統發出「預期交付物缺漏」通知
```

### F. 常見失敗原因與排查

| 編號 | 失敗現象 | 根因 | 排查路徑 |
|:----------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| F1 | List rows present in a table 報錯「找不到 Table」 | Excel 中的 Table 名稱不是 DocumentInventory，或未建立為 Table（僅為普通儲存格範圍） | 開啟 Excel → 選取資料範圍 → 插入 → 資料表 → 名稱確認為 `DocumentInventory`（區分大小寫） |
| F2 | List rows present in a table 報錯「找不到檔案」 | InventoryFilePath 路徑計算錯誤，或 SharePoint 資料夾不存在 | 確認步驟 3 的 Folder Path 格式正確；確認 SharePoint 有 `/Documents/Templates/{ProjectId}/` 資料夾 |
| F3 | Excel Online Business 連線 ⚠️ 報錯 | CR-Excel-SPN 未授權或已失效 | 解決方案 → Connection References → CR-Excel-SPN → 重新連線 |
| F4 | Apply to each 內 Add_PlannedRecord 失敗（400 錯誤） | DocumentType 文字值無法對應到 OptionSet 整數值 | 確認 Excel 清冊的 DocumentType 欄位值（如 `DesignBaseline`）完全符合 Baseline Matrix 中的記錄；步驟 5 的 gov_documenttype 需正確填入整數值 |
| F5 | 重複執行清冊後 Planned 記錄重複建立 | Check_DuplicatePlanned Filter 條件錯誤，或 gov_expectedfilename 欄位為空導致查詢永遠 0 筆 | 確認步驟 5a 的 Filter 包含 `gov_expectedfilename eq '...'` 且 `gov_documentrole eq 807660000`；確認欄位名稱拼寫正確 |
| F6 | GOV-005 Phase 1B 沒有命中 Planned 記錄（明明清冊有列出） | ExpectedFileName 與 GOV-005 上傳的 FileName 不完全一致（多空格、大小寫差異之外的問題，如副檔名大小寫） | 確認 Dataverse 中 Planned 記錄的 gov_expectedfilename 值 = `DesignBaseline_Campus.pdf`；Dataverse OData 大小寫不敏感但空格敏感，需確認兩端都有 trim() |
| F7 | PlannedCount 回傳 0（但清冊有資料） | Increment variable Action 放在 Condition False 分支（跳過）而非 True 分支（建立成功後） | 確認 Increment variable 在步驟 5b 的 True 分支（Add_PlannedRecord 成功後） |
| F8 | Power Apps 收到 PlannedCount = null | Respond 的 PlannedCount 欄位類型設為 Text 而非 Number | 確認 Respond Action 中 PlannedCount 使用「+ Add an output → Number」而非 Text |

---

## GOV-022：Standard Feedback Handler

### A. 基本資訊

| 項目 | 值 |
|:------------------------------|:----------------------------------------------|
| Flow 名稱 | GOV-022 Standard Feedback Handler |
| 目的 | 接收標準回饋表單提交，建立 gov_standardfeedback 記錄，通知標準擁有者 |
| Trigger 類型 | **Power Apps (V2)** |
| 觸發來源 | FORM-012（標準回饋表單） |
| Connection References | CR-Dataverse-SPN |
| Concurrency Control | Off（低頻操作） |
| 依賴 Child Flow | GOV-015（Notification Handler） |
| 對應測試案例 | E2E-022 |

### Step 0：Standard Feedback Handler 起手式必檢 6 項

**必檢 1**：環境確認

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| 目的 | 確認位於正確環境（如 GOV-PROD） |
| 操作路徑 | Maker Portal → 右上角環境名稱 |
| 成功長相 | 右上角顯示正確環境名稱 |
| 失敗長相 | 環境名稱不符 |
| 下一步 | 切換至正確環境 |

**必檢 2**：Connection Reference 確認

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| 目的 | 確認 CR-Dataverse-SPN 已連接至 Flow Service Principal |
| 操作路徑 | 解決方案 → Connection References → CR-Dataverse-SPN |
| 成功長相 | Connection Reference 狀態為 Connected |
| 失敗長相 | 狀態為 Disconnected 或 Error |
| 下一步 | 重新連線 CR-Dataverse-SPN |

**必檢 3**：gov_standardfeedback 資料表確認

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| 目的 | 確認資料表存在且有正確的 11 個欄位 |
| 操作路徑 | Tables → 搜尋 gov_standardfeedback → 確認存在 |
| 成功長相 | 資料表出現在列表中，有正確的 11 個欄位 |
| 失敗長相 | 資料表不存在 |
| 下一步 | 依 02 文件建立資料表 |

**必檢 4**：Counter List 種子確認

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| 目的 | 確認 Counter List 存在 CounterName = FeedbackID 的記錄 |
| 操作路徑 | Tables → Counter List → Data → 搜尋 FeedbackID |
| 成功長相 | 存在一筆記錄，Prefix = FB |
| 失敗長相 | 無 FeedbackID 記錄 |
| 下一步 | 新增一筆記錄：CounterName=FeedbackID, Prefix=FB, CurrentCounter=0, CurrentYear=2026 |

**必檢 5**：GOV-015 Notification Handler 已就緒

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| 目的 | 確認 Child Flow 可用 |
| 操作路徑 | My flows → 確認 GOV-015 存在且狀態為 On |
| 成功長相 | Flow 狀態為 On |
| 失敗長相 | Flow 不存在或狀態為 Off |
| 下一步 | 先建立 GOV-015 或開啟 |

**必檢 6**：安全角色確認

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| 目的 | 確認 Flow Service Principal 對 gov_standardfeedback 有 Create/Read/Write 權限 |
| 操作路徑 | Security Roles → Flow Service Principal → 確認 gov_standardfeedback 權限 |
| 成功長相 | Security Role 矩陣已設定 |
| 失敗長相 | 權限未設定 |
| 下一步 | 設定 Security Role 權限 |

### B. 先決條件清單

| 先決條件 | 確認方式 |
|:------------------------------|:----------------------------------------------|
| gov_standardfeedback 資料表已建立 | Tables 列表可見 |
| Counter List 含 FeedbackID 記錄 | Counter List Data 標籤確認 |
| GOV-015 已部署且狀態 On | My flows 確認 |
| Connection Reference CR-Dataverse-SPN 已連接 | Solution → Connection References |

### C. Input Schema（Power Apps V2 Trigger 參數）

| Parameter Name | Type | Required | Description |
|:------------------------------|:------|:---:|:----------------------------------------------|
| FeedbackType | Text | Yes | 回饋類型 OptionSet Value（807660000=CannotExecute / 807660001=Conflict / 807660002=Improvement） |
| StandardID | Text | Yes | 被回報標準的識別碼 |
| Description | Text | Yes | 回饋詳細內容 |
| RelatedStandard | Text | No | 相關標準名稱 |
| RelatedProjectId | Text | No | 關聯專案 GUID（選填） |
| SubmittedByEmail | Text | Yes | 提報人 Email |

### D. Output Schema（Canonical Error Envelope v5.0）

| Output Parameter | Type | 200 Success | 400 Failure | 500 System Failure |
|:------------------------------|:------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| StatusCode | Number | 200 | 400 | 500 |
| Status | Text | Success | Failed | Failed |
| ErrorCode | Text | （空白） | ERR-022-0XX | ERR-SYSTEM-500 |
| ErrorStage | Text | （空白） | PreCheck / CounterUpdate / CreateRecord | CatchHandler |
| Message | Text | 標準回饋已成功提交，FeedbackID: {ID} | 具體錯誤訊息 | @{outputs('Compose-ErrorOutput')} |
| FlowRunId | Text | @{workflow()?['run']?['name']} | same | same |
| Timestamp | Text | @{utcNow()} | same | same |
| FeedbackID | Text | FB-2026-XXXX | （空白） | （空白） |

### E. 建立步驟（逐步點擊）

**Step 1：Trigger — Power Apps (V2)**

```
1. 新增 Flow → 選擇「Power Apps (V2)」trigger
2. 點擊 Flow 名稱（左上角），改為「GOV-022 Standard Feedback Handler」
3. 新增 6 個 Input（全部選擇 Text 類型）：
   → 選擇 Text → 輸入名稱 FeedbackType
   → 選擇 Text → 輸入名稱 StandardID
   → 選擇 Text → 輸入名稱 Description
   → 選擇 Text → 輸入名稱 RelatedStandard（取消勾選 Required）
   → 選擇 Text → 輸入名稱 RelatedProjectId（取消勾選 Required）
   → 選擇 Text → 輸入名稱 SubmittedByEmail
```

**Step 2：Initialize Variables**

```
Action: + 新增步驟 → 搜尋 initialize variable → 選擇「變數」下的「Initialize variable」
  Name：varFeedbackType
  Type：String
  Value：點擊欄位 → 動態內容 → 選擇「FeedbackType」（來自 Trigger）

Action: Initialize variable
  Name：varStandardID
  Type：String
  Value：動態內容 → 選擇「StandardID」

Action: Initialize variable
  Name：varDescription
  Type：String
  Value：動態內容 → 選擇「Description」

Action: Initialize variable
  Name：varRelatedStandard
  Type：String
  Value：動態內容 → 選擇「RelatedStandard」

Action: Initialize variable
  Name：varRelatedProjectId
  Type：String
  Value：動態內容 → 選擇「RelatedProjectId」

Action: Initialize variable
  Name：varSubmittedByEmail
  Type：String
  Value：動態內容 → 選擇「SubmittedByEmail」

Action: Initialize variable
  Name：varFeedbackID
  Type：String
  Value：（空白）
```

**Step 3：建立 Try Scope**

```
Action: + 新增步驟 → 搜尋 scope → 選擇「控制項」下的「Scope」
  點擊 Scope 標題 → 重新命名為「Try」
```

> 以下 Step 3.1 ~ Step 3.6 都在 Try 內部建立。

**Step 3.1：Pre-Check — Is_InputValid**

```
在 Try 內部，+ 新增步驟
  → 搜尋 condition → 選擇「控制項」下的「Condition」
  重新命名為「Is_InputValid」
  條件設定：
    左側：運算式 →
      and(not(empty(triggerBody()['StandardID'])), not(empty(triggerBody()['FeedbackType'])), not(empty(triggerBody()['Description'])), not(empty(triggerBody()['SubmittedByEmail'])))
    運算子：is equal to
    右側：true

  If No（必要欄位缺失）：
    a. Respond to a PowerApp or flow
       （搜尋 respond → 選擇「Respond to a PowerApp or flow」）
       逐一加入輸出欄位：
         Number → StatusCode → 400
         Text → Status → Failed
         Text → ErrorCode → ERR-022-001
         Text → ErrorStage → PreCheck
         Text → Message → 必要輸入欄位缺失：請確認 StandardID、FeedbackType、Description、SubmittedByEmail 均有填寫
         Text → FlowRunId → 運算式：workflow()?['run']?['name']
         Text → Timestamp → 運算式：utcNow()
         Text → FeedbackID → （空白）
       重新命名為「Respond_400_InputInvalid」

    b. Terminate
       Status：Failed

  If Yes（繼續）：
    進入 Step 3.2
```

**Step 3.2：Get & Increment Counter**

```
在 Is_InputValid 的 If Yes 分支內：

a. + 新增步驟 → 搜尋 list rows → 選擇「Microsoft Dataverse」下的「List rows」
   連線：CR-Dataverse-SPN（MVP 模式：選個人帳號）
   Table name：Counter List
   Filter rows：gov_countername eq 'FeedbackID'
   Row count：1
   重新命名為「Get_FeedbackCounter」

b. + 新增步驟 → 搜尋 compose → 選擇「資料作業」下的「Compose」
   重新命名為「Compose-NewCounter」
   Inputs：運算式 → add(first(outputs('Get_FeedbackCounter')?['body/value'])?['gov_currentcounter'], 1)

c. + 新增步驟 → Compose
   重新命名為「Compose-FeedbackID」
   Inputs：運算式 →
     concat(first(outputs('Get_FeedbackCounter')?['body/value'])?['gov_prefix'], '-', string(first(outputs('Get_FeedbackCounter')?['body/value'])?['gov_currentyear']), '-', substring(concat('0000', string(outputs('Compose-NewCounter'))), sub(length(concat('0000', string(outputs('Compose-NewCounter')))), 4), 4))

d. + 新增步驟 → 搜尋 set variable → 選擇「變數」下的「Set variable」
   Name：varFeedbackID
   Value：動態內容 → 選擇 Compose-FeedbackID 的 Outputs

e. + 新增步驟 → 搜尋 update a row → 選擇「Microsoft Dataverse」下的「Update a row」
   Table name：Counter List
   Row ID：運算式 → first(outputs('Get_FeedbackCounter')?['body/value'])?['gov_counterlistid']
   gov_currentcounter：動態內容 → Compose-NewCounter 的 Outputs
   重新命名為「Update_FeedbackCounter」
```

**Step 3.3：Create Standard Feedback Record**

```
+ 新增步驟 → 搜尋 add a new row → 選擇「Microsoft Dataverse」下的「Add a new row」
  （中文：「新增資料列」）
  Table name：Standard Feedback
  重新命名為「Create_StandardFeedback」
  欄位對應：
    gov_feedbackid：@{variables('varFeedbackID')}
    gov_standardid：@{variables('varStandardID')}
    gov_feedbacktype：運算式 → int(variables('varFeedbackType'))
    gov_reporteddate：運算式 → utcNow()
    gov_feedbackresolutionstatus：807660000
    gov_description：@{variables('varDescription')}
    gov_relatedstandard：@{variables('varRelatedStandard')}
```

> **注意**：gov_reportedby（Lookup User）需透過 Office 365 Users connector 查詢 SubmittedByEmail 取得 User ID，或直接使用 Dataverse User 表查詢。gov_parentproject 僅在 varRelatedProjectId 非空時設定。

**Step 3.4：Send Notification via GOV-015**

```
+ 新增步驟 → 搜尋 run a child flow → 選擇「Flows」下的「Run a Child Flow」
  Child Flow：GOV-015 Notification Handler
  Input：
    NotificationType：StandardFeedbackReceived
    RecipientGroup：GOV-GovernanceLead
    RecipientEmail：（GOV-GovernanceLead 群組 Email）
    Subject：運算式 → concat('【標準回饋】', variables('varFeedbackID'), '：', variables('varStandardID'))
    Body：運算式 → concat('標準 ', variables('varStandardID'), ' 收到', variables('varFeedbackType'), '類型回饋。', decodeUriComponent('%0A'), '提報人：', variables('varSubmittedByEmail'), decodeUriComponent('%0A'), '說明：', variables('varDescription'))
    ProjectId：@{variables('varRelatedProjectId')}
    ReminderType：（空白，此為事件通知非提醒）
    CallingFlowName：GOV-022
  重新命名為「Call_GOV015_Notification」
```

**Step 3.5：FlowRunId Writeback**

```
+ 新增步驟 → 搜尋 update a row → 選擇「Microsoft Dataverse」下的「Update a row」
  Table name：Standard Feedback
  Row ID：運算式 → outputs('Create_StandardFeedback')?['body/gov_standardfeedbackid']
  欄位對應：
    gov_lastflowrunid：運算式 → workflow()?['run']?['name']
    gov_lastflowstatus：Success
  重新命名為「Writeback_FlowRunId」
```

**Step 3.6：Respond to Power App（200 Success）**

```
+ 新增步驟 → 搜尋 respond → 選擇「Respond to a PowerApp or flow」
  逐一加入輸出欄位：
    Number → StatusCode → 200
    Text → Status → Success
    Text → ErrorCode → （空白）
    Text → ErrorStage → （空白）
    Text → Message → 運算式 → concat('標準回饋已成功提交，FeedbackID: ', variables('varFeedbackID'))
    Text → FlowRunId → 運算式：workflow()?['run']?['name']
    Text → Timestamp → 運算式：utcNow()
    Text → FeedbackID → 動態內容 → varFeedbackID
  重新命名為「Respond_200_Success」
```

**Step 4：建立 Catch Scope**

```
在 Try Scope 下方（不是內部）：
  + 新增步驟 → 搜尋 scope → 選擇 Scope → 重新命名為「Catch」

  設定 Configure run after：
    點擊 Catch 右上角「...」→「設定在之後執行」（Configure run after）
    → 取消勾選「成功」
    → 勾選「已失敗」與「已逾時」

  在 Catch 內部：

  a. + 新增步驟 → Compose
     重新命名為「Compose-ErrorOutput」
     Inputs：運算式 → result('Try')

  b. + 新增步驟 → Respond to a PowerApp or flow
     逐一加入輸出欄位：
       Number → StatusCode → 500
       Text → Status → Failed
       Text → ErrorCode → ERR-SYSTEM-500
       Text → ErrorStage → CatchHandler
       Text → Message → 運算式 → string(outputs('Compose-ErrorOutput'))
       Text → FlowRunId → 運算式：workflow()?['run']?['name']
       Text → Timestamp → 運算式：utcNow()
       Text → FeedbackID → （空白）
     重新命名為「Respond_500_SystemError」
```

### F. 必做設定檢核點

| # | 檢核項目 | 驗證方式 | 預期結果 |
|:--|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| 1 | Trigger 類型為 Power Apps (V2) | Flow 編輯器確認 | Power Apps (V2) |
| 2 | 所有 Input 皆為 Text 類型 | Trigger 設定確認 | 6 個 Text Input |
| 3 | Try/Catch Scope 結構完整 | 確認 Catch 的 run after 設定 | has failed, has timed out |
| 4 | Success/Failure Respond 欄位一致 | 比對兩個 Respond | 8 個欄位完全相同 |
| 5 | Counter 更新在 Create Record 之前 | 步驟順序確認 | Counter → Create |
| 6 | Flow 名稱正確 | Flow properties | GOV-022 Standard Feedback Handler |

### G. 最小驗證流程

**第 1 步**：準備測試資料

```
1. 確認 Counter List 存在 FeedbackID 記錄（Prefix=FB, Counter=0）
2. 確認 gov_standardfeedback 資料表存在
```

**第 2 步**：執行測試

```
使用 Power Apps 或 Postman 呼叫 GOV-022
傳入：
  FeedbackType：807660000
  StandardID：TEST-STD-001
  Description：測試回饋
  SubmittedByEmail：{您的 Email}
  RelatedStandard：（空白）
  RelatedProjectId：（空白）
```

**第 3 步**：確認 Run History

```
1. Flow 執行狀態為 Succeeded
2. 回傳 StatusCode=200, FeedbackID=FB-2026-0001
```

**第 4 步**：確認 Dataverse 記錄

```
1. gov_standardfeedback 存在一筆記錄，FeedbackID=FB-2026-0001
2. Counter List FeedbackID 的 CurrentCounter 從 0 變為 1
```

### I. 常見失敗原因與對應排查路徑

| # | 失敗現象 | 根本原因 | 排查路徑 |
|:--|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| 1 | ERR-022-001 | 必要欄位缺失 | 確認 FORM-012 提交時有傳入所有必要參數 |
| 2 | ERR-022-002 | Counter List 無 FeedbackID 記錄 | 確認 Counter List 已初始化 |
| 3 | ERR-022-003 | Dataverse 寫入失敗 | 確認 Flow SP 對 gov_standardfeedback 有 Create 權限 |
| 4 | ERR-022-004 | GOV-015 呼叫失敗 | 確認 GOV-015 已部署且狀態為 On |
| 5 | 500 System Error | Scope 內未預期錯誤 | 查看 Flow Run History 的 Catch Scope 輸出 |

---

## GOV-023：Dispute Handler

### A. 基本資訊

| 項目 | 值 |
|:------------------------------|:----------------------------------------------|
| Flow 名稱 | GOV-023 Dispute Handler |
| 目的 | 接收爭議提報，建立 gov_disputelog 記錄，指派預設調解人，發送通知 |
| Trigger 類型 | **Power Apps (V2)** |
| 觸發來源 | FORM-013（爭議提報表單） |
| Connection References | CR-Dataverse-SPN |
| Concurrency Control | Off（低頻操作） |
| 依賴 Child Flow | GOV-015（Notification Handler） |
| 對應測試案例 | E2E-023 |

### Step 0：Dispute Handler 起手式必檢 6 項

**必檢 1**：環境確認

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| 目的 | 確認位於正確環境（如 GOV-PROD） |
| 操作路徑 | Maker Portal → 右上角環境名稱 |
| 成功長相 | 右上角顯示正確環境名稱 |
| 失敗長相 | 環境名稱不符 |
| 下一步 | 切換至正確環境 |

**必檢 2**：Connection Reference 確認

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| 目的 | 確認 CR-Dataverse-SPN 已連接至 Flow Service Principal |
| 操作路徑 | 解決方案 → Connection References → CR-Dataverse-SPN |
| 成功長相 | Connection Reference 狀態為 Connected |
| 失敗長相 | 狀態為 Disconnected 或 Error |
| 下一步 | 重新連線 CR-Dataverse-SPN |

**必檢 3**：gov_disputelog 資料表確認

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| 目的 | 確認資料表存在且有正確欄位 |
| 操作路徑 | Tables → 搜尋 gov_disputelog → 確認存在 |
| 成功長相 | 資料表出現在列表中 |
| 失敗長相 | 資料表不存在 |
| 下一步 | 依 02 文件建立資料表 |

**必檢 4**：Counter List 種子確認

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| 目的 | 確認 Counter List 存在 CounterName = DisputeID 的記錄 |
| 操作路徑 | Tables → Counter List → Data → 搜尋 DisputeID |
| 成功長相 | 存在一筆記錄，Prefix = DSP |
| 失敗長相 | 無 DisputeID 記錄 |
| 下一步 | 新增一筆記錄：CounterName=DisputeID, Prefix=DSP, CurrentCounter=0, CurrentYear=2026 |

**必檢 5**：GOV-015 Notification Handler 已就緒

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| 目的 | 確認 Child Flow 可用 |
| 操作路徑 | My flows → 確認 GOV-015 存在且狀態為 On |
| 成功長相 | Flow 狀態為 On |
| 失敗長相 | Flow 不存在或狀態為 Off |
| 下一步 | 先建立 GOV-015 或開啟 |

**必檢 6**：GOV-GovernanceLead Security Group 確認

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| 目的 | 確認 GOV-GovernanceLead 群組為 Mail-enabled 且有成員（用於指派預設調解人） |
| 操作路徑 | Entra ID → 群組 → 搜尋 GOV-GovernanceLead → 確認 Email 有值且有成員 |
| 成功長相 | 群組有 Email 地址且至少有 1 名成員 |
| 失敗長相 | Email 欄位空白或群組無成員 |
| 下一步 | 將群組類型改為 Mail-enabled Security Group → 加入成員 |

### B. 先決條件清單

| 先決條件 | 確認方式 |
|:------------------------------|:----------------------------------------------|
| gov_disputelog 資料表已建立 | Tables 列表可見 |
| Counter List 含 DisputeID 記錄 | Counter List Data 標籤確認 |
| GOV-015 已部署且狀態 On | My flows 確認 |
| GOV-GovernanceLead 群組已建立且有成員 | Entra ID 確認 |
| Connection Reference CR-Dataverse-SPN 已連接 | Solution → Connection References |

### C. Input Schema（Power Apps V2 Trigger 參數）

| Parameter Name | Type | Required | Description |
|:------------------------------|:------|:---:|:----------------------------------------------|
| DisputeLevel | Text | Yes | 爭議等級 OptionSet Value（807660000=Low / 807660001=Medium / 807660002=High） |
| Description | Text | Yes | 爭議詳細內容 |
| RelatedProjectId | Text | Yes | 關聯專案 GUID |
| SubmittedByEmail | Text | Yes | 提報人 Email |

### D. Output Schema（Canonical Error Envelope v5.0）

| Output Parameter | Type | 200 Success | 400 Failure | 500 System Failure |
|:------------------------------|:------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| StatusCode | Number | 200 | 400 | 500 |
| Status | Text | Success | Failed | Failed |
| ErrorCode | Text | （空白） | ERR-023-0XX | ERR-SYSTEM-500 |
| ErrorStage | Text | （空白） | PreCheck / CounterUpdate / CreateRecord | CatchHandler |
| Message | Text | 爭議已成功提報，DisputeID: {ID} | 具體錯誤訊息 | @{outputs('Compose-ErrorOutput')} |
| FlowRunId | Text | @{workflow()?['run']?['name']} | same | same |
| Timestamp | Text | @{utcNow()} | same | same |
| DisputeID | Text | DSP-2026-XXXX | （空白） | （空白） |

### E. 建立步驟（逐步點擊）

**Step 1：Trigger — Power Apps (V2)**

```
1. 新增 Flow → 選擇「Power Apps (V2)」trigger
2. 點擊 Flow 名稱（左上角），改為「GOV-023 Dispute Handler」
3. 新增 4 個 Input（全部選擇 Text 類型）：
   → 選擇 Text → 輸入名稱 DisputeLevel
   → 選擇 Text → 輸入名稱 Description
   → 選擇 Text → 輸入名稱 RelatedProjectId
   → 選擇 Text → 輸入名稱 SubmittedByEmail
```

**Step 2：Initialize Variables**

```
Action: + 新增步驟 → 搜尋 initialize variable → 選擇「變數」下的「Initialize variable」
  Name：varDisputeLevel
  Type：String
  Value：點擊欄位 → 動態內容 → 選擇「DisputeLevel」（來自 Trigger）

Action: Initialize variable
  Name：varDescription
  Type：String
  Value：動態內容 → 選擇「Description」

Action: Initialize variable
  Name：varRelatedProjectId
  Type：String
  Value：動態內容 → 選擇「RelatedProjectId」

Action: Initialize variable
  Name：varSubmittedByEmail
  Type：String
  Value：動態內容 → 選擇「SubmittedByEmail」

Action: Initialize variable
  Name：varDisputeID
  Type：String
  Value：（空白）

Action: Initialize variable
  Name：varMediatorEmail
  Type：String
  Value：（空白）
  說明：預設調解人 Email，從 GOV-GovernanceLead 群組查詢取得
```

**Step 3：建立 Try Scope**

```
Action: + 新增步驟 → 搜尋 scope → 選擇「控制項」下的「Scope」
  點擊 Scope 標題 → 重新命名為「Try」
```

> 以下 Step 3.1 ~ Step 3.7 都在 Try 內部建立。

**Step 3.1：Pre-Check — Is_InputValid**

```
在 Try 內部，+ 新增步驟
  → 搜尋 condition → 選擇「控制項」下的「Condition」
  重新命名為「Is_InputValid」
  條件設定：
    左側：運算式 →
      and(not(empty(triggerBody()['DisputeLevel'])), not(empty(triggerBody()['Description'])), not(empty(triggerBody()['RelatedProjectId'])), not(empty(triggerBody()['SubmittedByEmail'])))
    運算子：is equal to
    右側：true

  If No（必要欄位缺失）：
    a. Respond to a PowerApp or flow
       逐一加入輸出欄位：
         Number → StatusCode → 400
         Text → Status → Failed
         Text → ErrorCode → ERR-023-001
         Text → ErrorStage → PreCheck
         Text → Message → 必要輸入欄位缺失：請確認 DisputeLevel、Description、RelatedProjectId、SubmittedByEmail 均有填寫
         Text → FlowRunId → 運算式：workflow()?['run']?['name']
         Text → Timestamp → 運算式：utcNow()
         Text → DisputeID → （空白）
       重新命名為「Respond_400_InputInvalid」

    b. Terminate
       Status：Failed

  If Yes（繼續）：
    進入 Step 3.2
```

**Step 3.2：Get & Increment Counter**

```
在 Is_InputValid 的 If Yes 分支內：

a. + 新增步驟 → 搜尋 list rows → 選擇「Microsoft Dataverse」下的「List rows」
   連線：CR-Dataverse-SPN（MVP 模式：選個人帳號）
   Table name：Counter List
   Filter rows：gov_countername eq 'DisputeID'
   Row count：1
   重新命名為「Get_DisputeCounter」

b. + 新增步驟 → Compose
   重新命名為「Compose-NewCounter」
   Inputs：運算式 → add(first(outputs('Get_DisputeCounter')?['body/value'])?['gov_currentcounter'], 1)

c. + 新增步驟 → Compose
   重新命名為「Compose-DisputeID」
   Inputs：運算式 →
     concat(first(outputs('Get_DisputeCounter')?['body/value'])?['gov_prefix'], '-', string(first(outputs('Get_DisputeCounter')?['body/value'])?['gov_currentyear']), '-', substring(concat('0000', string(outputs('Compose-NewCounter'))), sub(length(concat('0000', string(outputs('Compose-NewCounter')))), 4), 4))

d. + 新增步驟 → Set variable
   Name：varDisputeID
   Value：動態內容 → 選擇 Compose-DisputeID 的 Outputs

e. + 新增步驟 → Update a row
   Table name：Counter List
   Row ID：運算式 → first(outputs('Get_DisputeCounter')?['body/value'])?['gov_counterlistid']
   gov_currentcounter：動態內容 → Compose-NewCounter 的 Outputs
   重新命名為「Update_DisputeCounter」
```

**Step 3.3：Create Dispute Log Record**

```
+ 新增步驟 → 搜尋 add a new row → 選擇「Microsoft Dataverse」下的「Add a new row」
  （中文：「新增資料列」）
  Table name：Dispute Log
  重新命名為「Create_DisputeLog」
  欄位對應：
    gov_disputeid：@{variables('varDisputeID')}
    gov_disputelevel：運算式 → int(variables('varDisputeLevel'))
    gov_description：@{variables('varDescription')}
    gov_parentproject：@{variables('varRelatedProjectId')}（Lookup → 點擊進階 → 貼上 GUID）
    gov_raiseddate：運算式 → utcNow()
    gov_raisedby：@{variables('varSubmittedByEmail')}
```

**Step 3.4：Lookup Default Mediator from GOV-GovernanceLead**

```
a. + 新增步驟 → 搜尋 list rows → 選擇「Microsoft Dataverse」下的「List rows」
   Table name：System User
   Filter rows：gov_securitygroup eq 'GOV-GovernanceLead'
   Row count：1
   重新命名為「Get_DefaultMediator」

   說明：此步驟查詢 GOV-GovernanceLead 群組的第一位成員作為預設調解人。
   替代方案：若使用 Office 365 Groups connector，可改用「List group members」
   動作查詢群組成員清單，取第一筆的 mail 欄位。

b. + 新增步驟 → Compose
   重新命名為「Compose-MediatorEmail」
   Inputs：運算式 →
     if(greater(length(outputs('Get_DefaultMediator')?['body/value']), 0),
       first(outputs('Get_DefaultMediator')?['body/value'])?['internalemailaddress'],
       'gov-governance-lead@company.com')
   說明：若查詢到成員則使用其 Email，否則使用群組 Email 作為 fallback

c. + 新增步驟 → Set variable
   Name：varMediatorEmail
   Value：動態內容 → Compose-MediatorEmail 的 Outputs
```

**Step 3.5：Update Dispute Record with Assigned Mediator**

```
+ 新增步驟 → 搜尋 update a row → 選擇「Microsoft Dataverse」下的「Update a row」
  Table name：Dispute Log
  Row ID：運算式 → outputs('Create_DisputeLog')?['body/gov_disputelogid']
  欄位對應：
    gov_assignedmediator：@{variables('varMediatorEmail')}
  重新命名為「Update_AssignMediator」
```

**Step 3.6：Send Notification via GOV-015**

```
+ 新增步驟 → 搜尋 run a child flow → 選擇「Flows」下的「Run a Child Flow」
  Child Flow：GOV-015 Notification Handler
  Input：
    NotificationType：DisputeSubmitted
    RecipientGroup：（空白）
    RecipientEmail：@{variables('varMediatorEmail')}
    Subject：運算式 → concat('【爭議提報】', variables('varDisputeID'), '：等級 ', variables('varDisputeLevel'))
    Body：運算式 → concat('專案 ', variables('varRelatedProjectId'), ' 收到爭議提報。', decodeUriComponent('%0A'), '提報人：', variables('varSubmittedByEmail'), decodeUriComponent('%0A'), '爭議等級：', variables('varDisputeLevel'), decodeUriComponent('%0A'), '說明：', variables('varDescription'), decodeUriComponent('%0A'), '請以調解人身份處理此爭議。')
    ProjectId：@{variables('varRelatedProjectId')}
    ReminderType：（空白，此為事件通知非提醒）
    CallingFlowName：GOV-023
  重新命名為「Call_GOV015_Notification」
```

**Step 3.7：FlowRunId Writeback + Respond 200 Success**

```
a. + 新增步驟 → Update a row
   Table name：Dispute Log
   Row ID：運算式 → outputs('Create_DisputeLog')?['body/gov_disputelogid']
   gov_lastflowrunid：運算式 → workflow()?['run']?['name']
   gov_lastflowstatus：Success
   重新命名為「Writeback_FlowRunId」

b. + 新增步驟 → Respond to a PowerApp or flow
   逐一加入輸出欄位：
     Number → StatusCode → 200
     Text → Status → Success
     Text → ErrorCode → （空白）
     Text → ErrorStage → （空白）
     Text → Message → 運算式 → concat('爭議已成功提報，DisputeID: ', variables('varDisputeID'))
     Text → FlowRunId → 運算式：workflow()?['run']?['name']
     Text → Timestamp → 運算式：utcNow()
     Text → DisputeID → 動態內容 → varDisputeID
   重新命名為「Respond_200_Success」
```

**Step 4：建立 Catch Scope**

```
在 Try Scope 下方（不是內部）：
  + 新增步驟 → 搜尋 scope → 選擇 Scope → 重新命名為「Catch」

  設定 Configure run after：
    點擊 Catch 右上角「...」→「設定在之後執行」（Configure run after）
    → 取消勾選「成功」
    → 勾選「已失敗」與「已逾時」

  在 Catch 內部：

  a. + 新增步驟 → Compose
     重新命名為「Compose-ErrorOutput」
     Inputs：運算式 → result('Try')

  b. + 新增步驟 → Respond to a PowerApp or flow
     逐一加入輸出欄位：
       Number → StatusCode → 500
       Text → Status → Failed
       Text → ErrorCode → ERR-SYSTEM-500
       Text → ErrorStage → CatchHandler
       Text → Message → 運算式 → string(outputs('Compose-ErrorOutput'))
       Text → FlowRunId → 運算式：workflow()?['run']?['name']
       Text → Timestamp → 運算式：utcNow()
       Text → DisputeID → （空白）
     重新命名為「Respond_500_SystemError」
```

### F. 必做設定檢核點

| # | 檢核項目 | 驗證方式 | 預期結果 |
|:--|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| 1 | Trigger 類型為 Power Apps (V2) | Flow 編輯器確認 | Power Apps (V2) |
| 2 | 所有 Input 皆為 Text 類型 | Trigger 設定確認 | 4 個 Text Input |
| 3 | Try/Catch Scope 結構完整 | 確認 Catch 的 run after 設定 | has failed, has timed out |
| 4 | Success/Failure Respond 欄位一致 | 比對兩個 Respond | 8 個欄位完全相同 |
| 5 | Counter 更新在 Create Record 之前 | 步驟順序確認 | Counter → Create |
| 6 | Mediator 指派在 Create Record 之後 | 步驟順序確認 | Create → Lookup Mediator → Update |
| 7 | Flow 名稱正確 | Flow properties | GOV-023 Dispute Handler |

### G. 最小驗證流程

**第 1 步**：準備測試資料

```
1. 確認 Counter List 存在 DisputeID 記錄（Prefix=DSP, Counter=0）
2. 確認 gov_disputelog 資料表存在
3. 確認 GOV-GovernanceLead 群組至少有 1 名成員
```

**第 2 步**：執行測試

```
使用 Power Apps 或 Postman 呼叫 GOV-023
傳入：
  DisputeLevel：807660000
  Description：測試爭議提報
  RelatedProjectId：{測試專案 GUID}
  SubmittedByEmail：{您的 Email}
```

**第 3 步**：確認 Run History

```
1. Flow 執行狀態為 Succeeded
2. 回傳 StatusCode=200, DisputeID=DSP-2026-0001
```

**第 4 步**：確認 Dataverse 記錄

```
1. gov_disputelog 存在一筆記錄，DisputeID=DSP-2026-0001
2. gov_assignedmediator 已填入調解人 Email
3. Counter List DisputeID 的 CurrentCounter 從 0 變為 1
```

**第 5 步**：確認通知

```
1. 調解人收到 DisputeSubmitted 通知 Email
2. 通知內容包含 DisputeID、爭議等級、提報人資訊
```

### I. 常見失敗原因與對應排查路徑

| # | 失敗現象 | 根本原因 | 排查路徑 |
|:--|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| 1 | ERR-023-001 | 必要欄位缺失 | 確認 FORM-013 提交時有傳入所有必要參數 |
| 2 | ERR-023-002 | Counter List 無 DisputeID 記錄 | 確認 Counter List 已初始化 |
| 3 | ERR-023-003 | Dataverse 寫入失敗 | 確認 Flow SP 對 gov_disputelog 有 Create 權限 |
| 4 | ERR-023-004 | 預設調解人查詢失敗 | 確認 GOV-GovernanceLead 群組已建立且有成員 |
| 5 | ERR-023-005 | GOV-015 呼叫失敗 | 確認 GOV-015 已部署且狀態為 On |
| 6 | 500 System Error | Scope 內未預期錯誤 | 查看 Flow Run History 的 Catch Scope 輸出 |

---

## GOV-024：Action Item Tracker

### A. 基本資訊

| 項目 | 值 |
|:------------------------------|:----------------------------------------------|
| Flow 名稱 | GOV-024 Action Item Tracker |
| 目的 | 接收 Gate 審批後的行動項目建立，追蹤完成狀態 |
| Trigger 類型 | **Power Apps (V2)** |
| 觸發來源 | FORM-014（行動項目建立表單） |
| Connection References | CR-Dataverse-SPN |
| Concurrency Control | Off（低頻操作） |
| 依賴 Child Flow | GOV-015（Notification Handler） |
| 對應測試案例 | E2E-024 |

### Step 0：Action Item Tracker 起手式必檢 6 項

**必檢 1**：環境確認

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| 目的 | 確認位於正確環境（如 GOV-PROD） |
| 操作路徑 | Maker Portal → 右上角環境名稱 |
| 成功長相 | 右上角顯示正確環境名稱 |
| 失敗長相 | 環境名稱不符 |
| 下一步 | 切換至正確環境 |

**必檢 2**：Connection Reference 確認

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| 目的 | 確認 CR-Dataverse-SPN 已連接至 Flow Service Principal |
| 操作路徑 | 解決方案 → Connection References → CR-Dataverse-SPN |
| 成功長相 | Connection Reference 狀態為 Connected |
| 失敗長相 | 狀態為 Disconnected 或 Error |
| 下一步 | 重新連線 CR-Dataverse-SPN |

**必檢 3**：gov_actionitem 資料表確認

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| 目的 | 確認資料表存在且有正確欄位 |
| 操作路徑 | Tables → 搜尋 gov_actionitem → 確認存在 |
| 成功長相 | 資料表出現在列表中 |
| 失敗長相 | 資料表不存在 |
| 下一步 | 依 02 文件建立資料表 |

**必檢 4**：Counter List 種子確認

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| 目的 | 確認 Counter List 存在 CounterName = ActionItemID 的記錄 |
| 操作路徑 | Tables → Counter List → Data → 搜尋 ActionItemID |
| 成功長相 | 存在一筆記錄，Prefix = ACT |
| 失敗長相 | 無 ActionItemID 記錄 |
| 下一步 | 新增一筆記錄：CounterName=ActionItemID, Prefix=ACT, CurrentCounter=0, CurrentYear=2026 |

**必檢 5**：GOV-015 Notification Handler 已就緒

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| 目的 | 確認 Child Flow 可用 |
| 操作路徑 | My flows → 確認 GOV-015 存在且狀態為 On |
| 成功長相 | Flow 狀態為 On |
| 失敗長相 | Flow 不存在或狀態為 Off |
| 下一步 | 先建立 GOV-015 或開啟 |

**必檢 6**：gov_reviewdecisionlog 資料表確認

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| 目的 | 確認 Review Decision Log 資料表存在（用於驗證 RelatedGateReviewId） |
| 操作路徑 | Tables → 搜尋 gov_reviewdecisionlog → 確認存在 |
| 成功長相 | 資料表出現在列表中 |
| 失敗長相 | 資料表不存在 |
| 下一步 | 依 02 文件建立資料表 |

### B. 先決條件清單

| 先決條件 | 確認方式 |
|:------------------------------|:----------------------------------------------|
| gov_actionitem 資料表已建立 | Tables 列表可見 |
| gov_reviewdecisionlog 資料表已建立 | Tables 列表可見 |
| Counter List 含 ActionItemID 記錄 | Counter List Data 標籤確認 |
| GOV-015 已部署且狀態 On | My flows 確認 |
| Connection Reference CR-Dataverse-SPN 已連接 | Solution → Connection References |

### C. Input Schema（Power Apps V2 Trigger 參數）

| Parameter Name | Type | Required | Description |
|:------------------------------|:------|:---:|:----------------------------------------------|
| RelatedGateReviewId | Text | Yes | 關聯 Gate 審查記錄 GUID（gov_reviewdecisionlogid） |
| Description | Text | Yes | 行動項目描述 |
| AssignedToEmail | Text | Yes | 負責人 Email |
| DueDate | Text | Yes | 到期日（ISO 8601 格式，如 2026-04-01） |
| RelatedProjectId | Text | Yes | 關聯專案 GUID |
| SubmittedByEmail | Text | Yes | 建立者 Email |

### D. Output Schema（Canonical Error Envelope v5.0）

| Output Parameter | Type | 200 Success | 400 Failure | 500 System Failure |
|:------------------------------|:------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| StatusCode | Number | 200 | 400 | 500 |
| Status | Text | Success | Failed | Failed |
| ErrorCode | Text | （空白） | ERR-024-0XX | ERR-SYSTEM-500 |
| ErrorStage | Text | （空白） | PreCheck / CounterUpdate / CreateRecord | CatchHandler |
| Message | Text | 行動項目已成功建立，ActionItemID: {ID} | 具體錯誤訊息 | @{outputs('Compose-ErrorOutput')} |
| FlowRunId | Text | @{workflow()?['run']?['name']} | same | same |
| Timestamp | Text | @{utcNow()} | same | same |
| ActionItemID | Text | ACT-2026-XXXX | （空白） | （空白） |

### E. 建立步驟（逐步點擊）

**Step 1：Trigger — Power Apps (V2)**

```
1. 新增 Flow → 選擇「Power Apps (V2)」trigger
2. 點擊 Flow 名稱（左上角），改為「GOV-024 Action Item Tracker」
3. 新增 6 個 Input（全部選擇 Text 類型）：
   → 選擇 Text → 輸入名稱 RelatedGateReviewId
   → 選擇 Text → 輸入名稱 Description
   → 選擇 Text → 輸入名稱 AssignedToEmail
   → 選擇 Text → 輸入名稱 DueDate
   → 選擇 Text → 輸入名稱 RelatedProjectId
   → 選擇 Text → 輸入名稱 SubmittedByEmail
```

**Step 2：Initialize Variables**

```
Action: + 新增步驟 → 搜尋 initialize variable → 選擇「變數」下的「Initialize variable」
  Name：varRelatedGateReviewId
  Type：String
  Value：點擊欄位 → 動態內容 → 選擇「RelatedGateReviewId」（來自 Trigger）

Action: Initialize variable
  Name：varDescription
  Type：String
  Value：動態內容 → 選擇「Description」

Action: Initialize variable
  Name：varAssignedToEmail
  Type：String
  Value：動態內容 → 選擇「AssignedToEmail」

Action: Initialize variable
  Name：varDueDate
  Type：String
  Value：動態內容 → 選擇「DueDate」

Action: Initialize variable
  Name：varRelatedProjectId
  Type：String
  Value：動態內容 → 選擇「RelatedProjectId」

Action: Initialize variable
  Name：varSubmittedByEmail
  Type：String
  Value：動態內容 → 選擇「SubmittedByEmail」

Action: Initialize variable
  Name：varActionItemID
  Type：String
  Value：（空白）
```

**Step 3：建立 Try Scope**

```
Action: + 新增步驟 → 搜尋 scope → 選擇「控制項」下的「Scope」
  點擊 Scope 標題 → 重新命名為「Try」
```

> 以下 Step 3.1 ~ Step 3.7 都在 Try 內部建立。

**Step 3.1：Pre-Check — Is_InputValid**

```
在 Try 內部，+ 新增步驟
  → 搜尋 condition → 選擇「控制項」下的「Condition」
  重新命名為「Is_InputValid」
  條件設定：
    左側：運算式 →
      and(not(empty(triggerBody()['RelatedGateReviewId'])), not(empty(triggerBody()['Description'])), not(empty(triggerBody()['AssignedToEmail'])), not(empty(triggerBody()['DueDate'])), not(empty(triggerBody()['RelatedProjectId'])), not(empty(triggerBody()['SubmittedByEmail'])))
    運算子：is equal to
    右側：true

  If No（必要欄位缺失）：
    a. Respond to a PowerApp or flow
       逐一加入輸出欄位：
         Number → StatusCode → 400
         Text → Status → Failed
         Text → ErrorCode → ERR-024-001
         Text → ErrorStage → PreCheck
         Text → Message → 必要輸入欄位缺失：請確認 RelatedGateReviewId、Description、AssignedToEmail、DueDate、RelatedProjectId、SubmittedByEmail 均有填寫
         Text → FlowRunId → 運算式：workflow()?['run']?['name']
         Text → Timestamp → 運算式：utcNow()
         Text → ActionItemID → （空白）
       重新命名為「Respond_400_InputInvalid」

    b. Terminate
       Status：Failed

  If Yes（繼續）：
    進入 Step 3.2
```

**Step 3.2：Validate RelatedGateReviewId**

```
在 Is_InputValid 的 If Yes 分支內：

a. + 新增步驟 → 搜尋 get a row → 選擇「Microsoft Dataverse」下的「Get a row by ID」
   連線：CR-Dataverse-SPN（MVP 模式：選個人帳號）
   Table name：Review Decision Log
   Row ID：運算式 → variables('varRelatedGateReviewId')
   重新命名為「Get_GateReviewRecord」

   說明：若 RelatedGateReviewId 不存在，此步驟會失敗，
   由 Catch Scope 捕捉並回傳 500 錯誤。
   若需更精確的錯誤處理，可在此步驟後新增 Condition 檢查。

b. + 新增步驟 → Condition
   重新命名為「Is_GateReviewValid」
   條件設定：
     左側：運算式 → not(empty(outputs('Get_GateReviewRecord')?['body/gov_reviewdecisionlogid']))
     運算子：is equal to
     右側：true

   If No（Gate Review 記錄不存在）：
     a. Respond to a PowerApp or flow
        Number → StatusCode → 400
        Text → Status → Failed
        Text → ErrorCode → ERR-024-002
        Text → ErrorStage → PreCheck
        Text → Message → 指定的 Gate Review 記錄不存在，請確認 RelatedGateReviewId 正確
        Text → FlowRunId → 運算式：workflow()?['run']?['name']
        Text → Timestamp → 運算式：utcNow()
        Text → ActionItemID → （空白）
      重新命名為「Respond_400_GateReviewNotFound」

     b. Terminate
        Status：Failed

   If Yes（繼續）：
     進入 Step 3.3
```

**Step 3.3：Get & Increment Counter**

```
a. + 新增步驟 → List rows
   Table name：Counter List
   Filter rows：gov_countername eq 'ActionItemID'
   Row count：1
   重新命名為「Get_ActionItemCounter」

b. + 新增步驟 → Compose
   重新命名為「Compose-NewCounter」
   Inputs：運算式 → add(first(outputs('Get_ActionItemCounter')?['body/value'])?['gov_currentcounter'], 1)

c. + 新增步驟 → Compose
   重新命名為「Compose-ActionItemID」
   Inputs：運算式 →
     concat(first(outputs('Get_ActionItemCounter')?['body/value'])?['gov_prefix'], '-', string(first(outputs('Get_ActionItemCounter')?['body/value'])?['gov_currentyear']), '-', substring(concat('0000', string(outputs('Compose-NewCounter'))), sub(length(concat('0000', string(outputs('Compose-NewCounter')))), 4), 4))

d. + 新增步驟 → Set variable
   Name：varActionItemID
   Value：動態內容 → 選擇 Compose-ActionItemID 的 Outputs

e. + 新增步驟 → Update a row
   Table name：Counter List
   Row ID：運算式 → first(outputs('Get_ActionItemCounter')?['body/value'])?['gov_counterlistid']
   gov_currentcounter：動態內容 → Compose-NewCounter 的 Outputs
   重新命名為「Update_ActionItemCounter」
```

**Step 3.4：Create Action Item Record**

```
+ 新增步驟 → 搜尋 add a new row → 選擇「Microsoft Dataverse」下的「Add a new row」
  （中文：「新增資料列」）
  Table name：Action Item
  重新命名為「Create_ActionItem」
  欄位對應：
    gov_actionitemid：@{variables('varActionItemID')}
    gov_description：@{variables('varDescription')}
    gov_assignedto：@{variables('varAssignedToEmail')}
    gov_duedate：@{variables('varDueDate')}
    gov_parentproject：@{variables('varRelatedProjectId')}（Lookup → 點擊進階 → 貼上 GUID）
    gov_relatedgatereview：@{variables('varRelatedGateReviewId')}（Lookup → 點擊進階 → 貼上 GUID）
    gov_createdbyemail：@{variables('varSubmittedByEmail')}
    gov_createdon：運算式 → utcNow()
    gov_actionitemstatus：807660000（Open）
```

**Step 3.5：Send Notification via GOV-015**

```
+ 新增步驟 → 搜尋 run a child flow → 選擇「Flows」下的「Run a Child Flow」
  Child Flow：GOV-015 Notification Handler
  Input：
    NotificationType：ActionItemAssigned
    RecipientGroup：（空白）
    RecipientEmail：@{variables('varAssignedToEmail')}
    Subject：運算式 → concat('【行動項目指派】', variables('varActionItemID'), '：請於 ', variables('varDueDate'), ' 前完成')
    Body：運算式 → concat('您被指派了一項行動項目。', decodeUriComponent('%0A'), '行動項目 ID：', variables('varActionItemID'), decodeUriComponent('%0A'), '說明：', variables('varDescription'), decodeUriComponent('%0A'), '到期日：', variables('varDueDate'), decodeUriComponent('%0A'), '建立者：', variables('varSubmittedByEmail'), decodeUriComponent('%0A'), '請於到期日前完成並更新狀態。')
    ProjectId：@{variables('varRelatedProjectId')}
    ReminderType：（空白，此為事件通知非提醒）
    CallingFlowName：GOV-024
  重新命名為「Call_GOV015_Notification」
```

**Step 3.6：FlowRunId Writeback**

```
+ 新增步驟 → 搜尋 update a row → 選擇「Microsoft Dataverse」下的「Update a row」
  Table name：Action Item
  Row ID：運算式 → outputs('Create_ActionItem')?['body/gov_actionitemid']
  欄位對應：
    gov_lastflowrunid：運算式 → workflow()?['run']?['name']
    gov_lastflowstatus：Success
  重新命名為「Writeback_FlowRunId」
```

**Step 3.7：Respond to Power App（200 Success）**

```
+ 新增步驟 → 搜尋 respond → 選擇「Respond to a PowerApp or flow」
  逐一加入輸出欄位：
    Number → StatusCode → 200
    Text → Status → Success
    Text → ErrorCode → （空白）
    Text → ErrorStage → （空白）
    Text → Message → 運算式 → concat('行動項目已成功建立，ActionItemID: ', variables('varActionItemID'))
    Text → FlowRunId → 運算式：workflow()?['run']?['name']
    Text → Timestamp → 運算式：utcNow()
    Text → ActionItemID → 動態內容 → varActionItemID
  重新命名為「Respond_200_Success」
```

**Step 4：建立 Catch Scope**

```
在 Try Scope 下方（不是內部）：
  + 新增步驟 → 搜尋 scope → 選擇 Scope → 重新命名為「Catch」

  設定 Configure run after：
    點擊 Catch 右上角「...」→「設定在之後執行」（Configure run after）
    → 取消勾選「成功」
    → 勾選「已失敗」與「已逾時」

  在 Catch 內部：

  a. + 新增步驟 → Compose
     重新命名為「Compose-ErrorOutput」
     Inputs：運算式 → result('Try')

  b. + 新增步驟 → Respond to a PowerApp or flow
     逐一加入輸出欄位：
       Number → StatusCode → 500
       Text → Status → Failed
       Text → ErrorCode → ERR-SYSTEM-500
       Text → ErrorStage → CatchHandler
       Text → Message → 運算式 → string(outputs('Compose-ErrorOutput'))
       Text → FlowRunId → 運算式：workflow()?['run']?['name']
       Text → Timestamp → 運算式：utcNow()
       Text → ActionItemID → （空白）
     重新命名為「Respond_500_SystemError」
```

### F. 必做設定檢核點

| # | 檢核項目 | 驗證方式 | 預期結果 |
|:--|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| 1 | Trigger 類型為 Power Apps (V2) | Flow 編輯器確認 | Power Apps (V2) |
| 2 | 所有 Input 皆為 Text 類型 | Trigger 設定確認 | 6 個 Text Input |
| 3 | Try/Catch Scope 結構完整 | 確認 Catch 的 run after 設定 | has failed, has timed out |
| 4 | Success/Failure Respond 欄位一致 | 比對兩個 Respond | 8 個欄位完全相同 |
| 5 | Counter 更新在 Create Record 之前 | 步驟順序確認 | Counter → Create |
| 6 | GateReview 驗證在 Create Record 之前 | 步驟順序確認 | Get_GateReviewRecord → Create |
| 7 | Flow 名稱正確 | Flow properties | GOV-024 Action Item Tracker |

### G. 最小驗證流程

**第 1 步**：準備測試資料

```
1. 確認 Counter List 存在 ActionItemID 記錄（Prefix=ACT, Counter=0）
2. 確認 gov_actionitem 資料表存在
3. 確認至少有一筆 Review Decision Log 記錄（取得其 GUID 作為測試用）
```

**第 2 步**：執行測試

```
使用 Power Apps 或 Postman 呼叫 GOV-024
傳入：
  RelatedGateReviewId：{Review Decision Log 記錄 GUID}
  Description：測試行動項目
  AssignedToEmail：{指派人 Email}
  DueDate：2026-04-01
  RelatedProjectId：{測試專案 GUID}
  SubmittedByEmail：{您的 Email}
```

**第 3 步**：確認 Run History

```
1. Flow 執行狀態為 Succeeded
2. 回傳 StatusCode=200, ActionItemID=ACT-2026-0001
```

**第 4 步**：確認 Dataverse 記錄

```
1. gov_actionitem 存在一筆記錄，ActionItemID=ACT-2026-0001
2. gov_relatedgatereview 已正確關聯到 Review Decision Log 記錄
3. gov_assignedto 已填入指派人 Email
4. gov_duedate 已填入 2026-04-01
5. Counter List ActionItemID 的 CurrentCounter 從 0 變為 1
```

**第 5 步**：確認通知

```
1. 指派人收到 ActionItemAssigned 通知 Email
2. 通知內容包含 ActionItemID、說明、到期日
```

### I. 常見失敗原因與對應排查路徑

| # | 失敗現象 | 根本原因 | 排查路徑 |
|:--|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| 1 | ERR-024-001 | 必要欄位缺失 | 確認 FORM-014 提交時有傳入所有必要參數 |
| 2 | ERR-024-002 | RelatedGateReviewId 不存在 | 確認 Review Decision Log 記錄 GUID 正確 |
| 3 | ERR-024-003 | Counter List 無 ActionItemID 記錄 | 確認 Counter List 已初始化 |
| 4 | ERR-024-004 | Dataverse 寫入失敗 | 確認 Flow SP 對 gov_actionitem 有 Create 權限 |
| 5 | ERR-024-005 | GOV-015 呼叫失敗 | 確認 GOV-015 已部署且狀態為 On |
| 6 | 500 System Error | Scope 內未預期錯誤 | 查看 Flow Run History 的 Catch Scope 輸出 |

---

## 最小可用上線檢核

## DEV 完成定義

| # | 檢核項目 | 驗證方式 | 對應測試案例 | 狀態 |
|:-----|:----------------------------------------------|:----------------------------------------------|:-------------------------------|:------:|
| 1 | 所有 17 條 Flow 已建立 | Solution 內確認 Flow 清單 | N/A | ☐ |
| 2 | 所有 Flow 使用 Connection Reference | 每條 Flow 的 Connections 皆指向 CR- | N/A | ☐ |
| 3 | 所有 Flow 已實作 Try-Catch | 每條 Flow 有 Catch Scope | N/A | ☐ |
| 4 | GOV-001 可建立專案 | 測試執行 | E2E-001 Phase 1 | ☐ |
| 5 | GOV-002 可提交 Gate 申請 | 測試執行 | E2E-001 Phase 2 | ☐ |
| 6 | GOV-003 三層審批正常 | 測試執行 | E2E-001 Phase 3 | ☐ |
| 7 | GOV-005 可上傳文件（Base64 模式） | 測試執行 | E2E-001 步驟 2.1, E2E-014 | ☐ |
| 8 | GOV-017 可偵測違規 | 手動修改 CurrentGate 後等待偵測 | AC-001 | ☐ |
| 9 | GOV-017 可自動回滾 | 驗證違規記錄的 RollbackStatus = Closed | AC-001 | ☐ |
| 10 | Pre-check 正確阻斷 | 測試各種違規情境 | E2E-001~006 | ☐ |
| 11 | 並行控制正常 | 同時發送兩筆 Gate Request | E2E-006 | ☐ |

## QA 環境部署完成定義

| # | 檢核項目 | 驗證方式 | 狀態 |
|:-----|:----------------------------------------------|:----------------------------------------------|:------:|
| 1 | Solution 成功匯入（Managed） | 匯入狀態顯示成功 | ☐ |
| 2 | 所有 Connection References 已重新指派 | 每個 CR- 指向 QA 環境連線 | ☐ |
| 3 | 所有 Flow 已啟用 | Flow 狀態皆為「開啟」 | ☐ |
| 4 | Smoke Test 通過 | 執行 07文件 4.3.1~4.3.3 | ☐ |
| 5 | 整合測試全部通過 | 執行 07文件 E2E-001~006 | ☐ |
| 6 | 反作弊測試全部通過 | 執行 07文件 AC-001~008 | ☐ |

## PROD 匯入後必要檢查

| # | 檢核項目 | 操作方式 | 狀態 |
|:-----|:----------------------------------------------|:----------------------------------------------|:------:|
| 1 | Solution 匯入成功 | 匯入狀態顯示成功 | ☐ |
| 2 | Connection Reference 重新指派 | 每個 CR- 指向 PROD 連線 | ☐ |
| 3 | 所有 Flow 預設為 Off | 確認所有 Flow 狀態為 Off | ☐ |
| 4 | 依序啟用 Child Flows | GOV-015 → GOV-013A → GOV-013B → GOV-014 → GOV-016 → GOV-004 → GOV-003 | ☐ |
| 5 | 依序啟用 Parent Flows | GOV-005 → GOV-002 → GOV-001 | ☐ |
| 6 | 啟用 Scheduled Flows | GOV-017, GOV-018, GOV-019 | ☐ |
| 7 | Smoke Test 通過 | 建立一個測試專案（PROD-SMOKE-TEST） | ☐ |
| 8 | GOV-017 首次執行成功 | 查看 Run History，確認無錯誤 | ☐ |

---

## 禁止上線條件

以下任一條件成立，禁止上線：

| # | 禁止上線條件 | 原因 | 驗證方式 |
|:-----|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| 1 | GOV-017 Guardrail Monitor 測試失敗 | 無法偵測違規修改，治理完整性無法保護 | AC-001, AC-002 必須通過 |
| 2 | GOV-017 無法自動回滾 | 違規修改無法復原，系統狀態可能不一致 | AC-001 中 RollbackStatus 必須為 Closed |
| 3 | GOV-018 Compliance Reconciler 測試失敗 | 無法偵測 Aggregate 與 Event 不一致 | AC-004 必須通過 |
| 4 | GOV-019 SLA Monitor 測試失敗 | 無法偵測審批超時 | AC-006 必須通過 |
| 5 | 任何 Pre-check 無法正確阻斷違規操作 | 允許繞過治理規則 | E2E-001~006 所有 Pre-check 測試必須通過 |
| 6 | Connection 使用個人帳號 | 人員異動將導致系統癱瘓 | 每個 Connection Reference 必須指向 Service Principal |
| 7 | Flow 未加入 Solution | 無法版本控制與回滾 | 所有 Flow 必須在 Solution 清單中 |
| 8 | Try-Catch 未實作 | 錯誤發生時無法捕捉並記錄 | 每條 Flow 必須有 Catch Scope。**例外**：GOV-015 Notification Handler 設計上免除 Try-Catch（通知失敗不應中斷主流程）。驗收時，GOV-015 可跳過此項目，但須人工記錄例外核准。 |
| 9 | FLS 未正確設定 | Flow-only 欄位可被人類修改 | AC-003 必須通過 |
| 10 | Dataverse Audit 未啟用 | GOV-017 無法查詢修改記錄 | 環境設定中「開始稽核」必須啟用 |
| 11 | 必要 Security Group 不存在 | Approval 無法發送給正確群組 | 所有群組必須存在且已設定成員 |
| 12 | GOV-014 Document Freeze 測試失敗 | Gate 3 通過後文件無法凍結 | E2E-001 Phase 6 必須通過 |

---

## 附錄

## 常用表達式範例

| 用途 | 表達式 |
|:----------------------------------------------|:--------------------------------------------------------------|
| 補零至 N 位（以 4 位為例） | `substring(concat('0000', string(數值)), sub(length(concat('0000', string(數值))), 4), 4)` |
| 產生 RequestID（Counter List） | `concat(Prefix, '-', string(Year), '-', PaddedSeq)`（詳見 GOV-001 步驟 3） |
| 產生唯一識別碼（非 RequestID 用途） | `concat('前綴-', formatDateTime(utcNow(), 'yyyyMMddHHmmss'))` |
| 取得當前時間（UTC） | `utcNow()` |
| 轉換為 UTC+8 顯示 | `convertTimeZone(utcNow(), 'UTC', 'Taipei Standard Time')` |
| 格式化日期 | `formatDateTime(utcNow(), 'yyyy-MM-dd HH:mm:ss')` |
| 取得陣列長度 | `length(outputs('List_rows')?['body/value'])` |
| 取得 Flow Run ID | `workflow()?['run']?['name']` |
| 取得 Flow 名稱 | `workflow()?['name']` |
| 取得 Trigger 輸入欄位 | `triggerBody()?['欄位名稱']` |
| 取得 Action 輸出 | `outputs('Action名稱')?['body/欄位名稱']` |
| Coalesce（取第一個非 null） | `coalesce(值1, 值2, '預設值')` |
| 字串轉小寫 | `toLower('字串')` |
| 加減小時 | `addHours(utcNow(), -1)` |
| 計算日期差（天） | `div(sub(ticks(utcNow()), ticks(日期)), 864000000000)` |
| Base64 轉 Binary | `base64ToBinary(base64字串)` |
| 擷取錯誤訊息 | `result('Scope名稱')?[0]?['error']?['message']` |
| Approval Outcome | `outputs('Approval_Action')?['body/outcome']` |
| Approval Responder Email | `outputs('Approval_Action')?['body/responder']?['email']` |

## Dataverse 欄位 Schema Name 對照

| 顯示名稱 | Schema Name | 資料類型 |
|:----------------------------------------------|:----------------------------------------------|:-------------------------------|
| RequestID | gov_requestid | 文字 |
| Title | gov_title | 文字 |
| CurrentGate | gov_currentgate | 選項集 |
| RequestStatus | gov_requeststatus | 選項集 |
| ProjectStatus | gov_projectstatus | 選項集 |
| DocumentFreezeStatus | gov_documentfreezestatus | 選項集 |
| ReworkCount | gov_reworkcount | 整數 |
| SystemArchitect | gov_systemarchitect | 文字 |
| ProjectManager | gov_projectmanager | 文字 |
| HighestResidualRiskLevel | gov_highestresidualrisklevel | 選項集 |
| RiskAcceptanceStatus | gov_riskacceptancestatus | 選項集 |
| Gate0PassedDate | gov_gate0passeddate | 日期時間 |
| Gate1PassedDate | gov_gate1passeddate | 日期時間 |
| Gate2PassedDate | gov_gate2passeddate | 日期時間 |
| Gate3PassedDate | gov_gate3passeddate | 日期時間 |
| LastFlowRunId | gov_lastflowrunid | 文字 |
| LastFlowStatus | gov_lastflowstatus | 選項集 |
| SubmittedBy | gov_submittedby | 文字 |
| SubmittedAt | gov_submittedat | 日期時間 |
| SharePointProvisionStatus | gov_sharepointprovisionstatus | 選項集 |
| TechnicalFeasibilityLink | gov_technicalfeasibilitylink | URL |
| DesignBaselineLink | gov_designbaselinelink | URL |

## OptionSet 值對照

### CurrentGate

| 顯示值 | 數值 |
|:-------------------------------|:----------|
| Pending | 807660000 |
| Gate0 | 807660001 |
| Gate1 | 807660002 |
| Gate2 | 807660003 |
| Gate3 | 807660004 |

### RequestStatus

| 顯示值 | 數值 |
|:-------------------------------|:----------|
| None | 807660000 |
| Pending | 807660001 |
| UnderReview | 807660002 |

### ProjectStatus

| 顯示值 | 數值 |
|:-------------------------------|:----------|
| Active | 807660000 |
| OnHold | 807660001 |
| Closed | 807660002 |
| Terminated | 807660003 |

### RiskLevel / ResidualRiskLevel

| 顯示值 | 數值 |
|:-------------------------------|:----------|
| Low | 807660000 |
| Medium | 807660001 |
| High | 807660002 |

### Decision

| 顯示值 | 數值 |
|:-------------------------------|:----------|
| Pending | 807660000 |
| Approved | 807660001 |
| Rejected | 807660002 |
| Executed | 807660003 |

### RollbackStatus

| 顯示值 | 數值 |
|:-------------------------------|:----------|
| Pending | 807660000 |
| Closed | 807660001 |
| ManualRequired | 807660002 |

### ReviewType

| 顯示值 | 數值 |
|:-------------------------------|:----------|
| ProjectCreation | 807660000 |
| Gate0Request | 807660001 |
| Gate1Request | 807660002 |
| Gate2Request | 807660003 |
| Gate3Request | 807660004 |
| RiskAcceptance | 807660005 |
| DocumentFreeze | 807660006 |
| DocumentUpload | 807660007 |

### ProjectType

| 顯示值 | 數值 |
|:-------------------------------|:----------|
| NewSystem | 807660000 |
| MajorArchChange | 807660001 |
| SecurityCritical | 807660002 |
| ComplianceChange | 807660003 |

### LastFlowStatus（v5.0 新增）

| 顯示值 | 數值 | 說明 |
|:-------------------------------|:----------|:----------------------------------------------|
| Success | 807660000 | Flow 執行成功 |
| Failed | 807660001 | Flow 執行失敗（含 400 / 500） |

### SharePointProvisionStatus（v5.0 新增）

| 顯示值 | 數值 | 說明 |
|:-------------------------------|:----------|:----------------------------------------------|
| NotStarted | 807660000 | 尚未開始建立 |
| Success | 807660001 | 建立成功 |
| Failed | 807660002 | 建立失敗（專案已建立，但 SharePoint 未就緒） |

### TargetSL

| 顯示值 | 數值 |
|:-------------------------------|:----------|
| SL1 | 807660000 |
| SL2 | 807660001 |
| SL3 | 807660002 |
| SL4 | 807660003 |

---

## Gate State Transition Matrix（P-15 原則）

### 合法狀態轉換矩陣

下表定義 `gov_currentgate` 的所有合法與非法轉換路徑。GOV-002 / GOV-003 / GOV-017 必須依此矩陣驗證。

| 來源狀態 (CurrentGate) | → Pending | → Gate0 | → Gate1 | → Gate2 | → Gate3 |
|:----------------------------------------------|:-------------------------------|:-------------------------------|:-------------------------------|:-------------------------------|:-------------------------------|
| **Pending** | — | ✅ GOV-003 | ❌ | ❌ | ❌ |
| **Gate0** | ❌ | — | ✅ GOV-003 | ❌ | ❌ |
| **Gate1** | ❌ | ❌ | — | ✅ GOV-003 | ❌ |
| **Gate2** | ❌ | ❌ | ❌ | ✅ GOV-003 (Rework) | ✅ GOV-003 |
| **Gate3** | ❌ | ❌ | ❌ | ❌ | — |

> **說明**：
> - ✅ = 合法轉換，由 GOV-003（Approval Handler）在審批通過後執行
> - ❌ = 非法轉換，任何嘗試都應被 GOV-002 Pre-check 或 GOV-017 Guardrail 攔截
> - Gate2 → Gate2 為 Rework 場景（GOV-016 觸發後重新提交 Gate 2 審查）
> - Gate3 為終態，通過後觸發 GOV-014 Document Freeze

### 合法轉換觸發條件

| 轉換 | 觸發 Flow | 前置條件 | ErrorCode（不滿足時） |
|:----------------------------------------------|:-------------------------------|:----------------------------------------------|:-------------------------------|
| Pending → Gate0 | GOV-003 | GOV-002 Pre-check 通過 + Gate0 文件齊全 + 審批 Approved | ERR-002-020 |
| Gate0 → Gate1 | GOV-003 | GOV-002 Pre-check 通過 + Gate1 文件齊全 + 三層審批 Approved | ERR-002-040 |
| Gate1 → Gate2 | GOV-003 | GOV-002 Pre-check 通過 + Gate2 文件齊全 + 審批 Approved | ERR-002-050 |
| Gate2 → Gate2 | GOV-003 | Rework 後重新提交 Gate2 + 審批 Approved | ERR-002-050 |
| Gate2 → Gate3 | GOV-003 | GOV-002 Pre-check 通過 + Gate3 文件齊全 + Risk Acceptance + 雙層審批 Approved | ERR-002-053 |

### 非法轉換偵測（GOV-017 Guardrail）

GOV-017 每小時掃描 Project Registry，偵測以下非法狀態：

| 非法情境 | 偵測條件 | 處理方式 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| Gate 跳級（如 Pending → Gate2） | CurrentGate 值跳過中間 Gate 且無對應 RDL 記錄 | 記錄 Governance Violation Log，通知管理員 |
| Gate 降級（如 Gate2 → Gate0） | CurrentGate 值低於上次記錄的最高 Gate | 記錄 Governance Violation Log，通知管理員 |
| 無 RDL 記錄的 Gate 變更 | CurrentGate 變更但 Review Decision Log 無對應 Approved 記錄 | 記錄 Governance Violation Log，可能為手動竄改 |
| Gate3 後 CurrentGate 被修改 | Gate3 已通過（Gate3PassedDate 非 null）但 CurrentGate ≠ Gate3 | 記錄 Governance Violation Log，嚴重違規 |

> **P-15 原則強制性**：Gate State Transition Matrix 為不可違反的治理規則。
> 任何繞過合法路徑的操作（如直接在 Dataverse 修改 CurrentGate）都會被 GOV-017 偵測並記錄。
> FLS 已保護 `gov_currentgate` 欄位，僅 Flow Service Principal 可寫入。

---

## 錯誤代碼與處置方式對照

| ErrorCode | StatusCode | ErrorStage | 嚴重性 | 說明 | 處置方式 |
|:-------------------------------|:----------|:----------------------------------------------|:-------------------------------|:----------------------------------------------|:----------------------------------------------|
| ERR-001-001 | 400 | PreCheck | Validation | 必填欄位未填寫 | 檢查 Power Apps Form 必填驗證 |
| ERR-001-002 | 400 | PreCheck | Authorization | 非授權架構師 | 確認提交者已加入 GOV-Architects 群組 |
| ERR-001-010 | 400 | CounterUpdate | System | RequestID 產生失敗 | 檢查 Counter List 記錄是否存在（gov_countername = 'ProjectRequest'），確認 gov_nextseq 欄位值有效 |
| ERR-001-COUNTER | 400 | CounterUpdate | Validation | Counter List 記錄不存在 | 在 Dataverse 建立 ProjectRequest Counter 記錄 |
| ERR-001-USER | 400 | UserLookup | Validation | 使用者 email 查無人 | 確認 Email 拼寫與 Entra ID 一致 |
| ERR-001-011 | 400 | OptionSetMapping | Validation | OptionSet 映射不存在 | 確認 gov_optionsetmapping 已建立對應記錄 |
| ERR-002-001 | 400 | PreCheck | Validation | 專案不存在 | 確認 ProjectId 正確 |
| ERR-002-003 | 400 | PreCheck | Authorization | 非專案 SA | 僅 SystemArchitect 可提交申請 |
| ERR-002-005 | 400 | PreCheck | Validation | 專案狀態不允許（未知狀態） | 確認 gov_projectstatus 為有效值 |
| ERR-002-006 | 400 | PreCheck | Validation | 專案目前暫停（OnHold） | 請聯繫 PM 恢復後再提交 |
| ERR-002-007 | 400 | PreCheck | Validation | 專案已結案（Closed） | 已結案專案無法提交 Gate 申請 |
| ERR-002-008 | 400 | PreCheck | Validation | 專案已終止（Terminated） | 已終止專案無法提交 Gate 申請 |
| ERR-002-009 | 400 | PreCheck | Validation | 此 Gate 有必要文件仍為 Planned（未上傳） | 完成所有必要文件上傳後再提交 Gate 申請 |
| ERR-002-010 | 400 | PreCheck | Validation | Gate2 重送時無有效 Rework 事件 | gov_reworkcount > 0 且 gov_requeststatus = None（807660000）才能重送 Gate2 |
| ERR-002-020 | 400 | PreCheck | Validation | Gate 0 前置條件不滿足 | CurrentGate 必須為 Pending |
| ERR-002-040 | 400 | PreCheck | Validation | Gate 1 前置條件不滿足 | CurrentGate 必須為 Gate0 |
| ERR-002-050 | 400 | PreCheck | Validation | Gate 2 前置條件不滿足 | CurrentGate 必須為 Gate1 或 Gate2 |
| ERR-002-053 | 400 | PreCheck | Validation | Gate 3 前置條件不滿足 | CurrentGate 必須為 Gate2 |
| ERR-002-058 | 400 | PreCheck | Conflict | 有進行中申請 | 等待現有申請完成或撤銷 |
| ERR-003-001 | 400 | ApprovalProcess | Validation | RequestStatus 非 Pending | 確認 GOV-002 已正確更新狀態 |
| ERR-003-010 | 400 | ApprovalProcess | Validation | Risk Acceptance 未完成 | Gate 3 必須先完成 Risk Acceptance |
| ERR-004-001 | 400 | DataverseWrite | Validation | 風險等級未計算 | 先呼叫 GOV-013B |
| ERR-005-001 | 400 | PreCheck | Validation | 專案不存在 | 確認 ProjectId 正確 |
| ERR-005-003 | 400 | PreCheck | Validation | 文件已凍結 | Gate 3 通過後不可上傳 |
| ERR-005-006 | 400 | DocumentValidation | Validation | DocumentType 映射不存在 | 確認 Document Baseline Matrix 已建立對應記錄 |
| ERR-005-019 | 400 | DocumentTypeValidation | Validation | Phase 1B 文件類型與清冊定義不符 | 上傳宣告的 DocumentType 與 GOV-020 文件清冊 Planned 記錄 gov_documenttype 不一致 |
| ERR-013-001 | 400 | DataverseWrite | Validation | 無風險項目 | 先在 Risk Assessment Table 建立記錄 |
| ERR-014-001 | 400 | PreCheck | Validation | CurrentGate 非 Gate3 | Document Freeze 僅適用於 Gate 3 通過後 |
| PROVISION_FAIL | 400 | SharePointProvision | System | SharePoint 資料夾建立失敗 | 確認 SharePoint 連線正常、Site 存在、權限充足 |
| ERR-SYSTEM-500 | 500 | CatchHandler | System | 系統錯誤 | 查看 Flow Run History 錯誤詳情，使用 FlowRunId 定位 |

## 測試案例交叉參照索引

| Flow ID | 對應 07文件測試案例 |
|:-------------------------------|:----------------------------------------------|
| GOV-001 | E2E-001 Phase 1, E2E-005, 4.3.1 |
| GOV-002 | E2E-001 Phase 2~6, E2E-006 |
| GOV-003 | E2E-001 Phase 2~6, E2E-002, E2E-003, AC-008 |
| GOV-004 | E2E-001 Phase 5 |
| GOV-005 | E2E-001 步驟 2.1 |
| GOV-013A | E2E-001 Phase 5（單項計算） |
| GOV-013B | E2E-001 Phase 5（彙總） |
| GOV-014 | E2E-001 Phase 6 |
| GOV-015 | 4.3.3 |
| GOV-016 | E2E-002, E2E-003, E2E-004 |
| GOV-017 | AC-001, AC-002, AC-007, 4.3.2 |
| GOV-018 | AC-004, AC-005 |
| GOV-019 | AC-006 |

---

## Evidence Chain Mapping（IEC 62443 稽核證據鏈）

### 目的

本節定義 Flow 執行過程中產生的每筆資料記錄如何對應到 IEC 62443 稽核證據要求。
當稽核員要求「證明某個 Gate 確實經過審批」或「證明風險評估已執行」時，
可透過以下對應表快速定位證據來源。

### 證據鏈對應矩陣

| 稽核問題 | 證據來源（Dataverse 表） | 關鍵欄位 | 產生 Flow | 追溯鍵 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|:-------------------------------|:----------------------------------------------|
| 專案何時建立？由誰建立？ | Project Registry | gov_submittedat, gov_submittedby, createdon | GOV-001 | gov_projectregistryid |
| Gate X 是否通過？何時通過？ | Project Registry | gov_gate{X}passeddate, gov_currentgate | GOV-003 | gov_projectregistryid |
| Gate X 審批由誰執行？決定為何？ | Review Decision Log | gov_approvedby, gov_decision, gov_revieweddate | GOV-003 | gov_triggerflowrunid |
| 風險評估是否完成？最高風險等級？ | Risk Assessment Table + Project Registry | gov_residualrisklevel, gov_highestresidualrisklevel | GOV-013A/B | gov_projectregistryid |
| Risk Acceptance 是否由授權人員簽署？ | Risk Assessment Table | gov_riskacceptedby, gov_riskacceptancedate | GOV-004 | gov_riskassessmenttableid |
| 文件是否已上傳至正確位置？ | Document Register | gov_sharepointfilelink, gov_documenttype | GOV-005 | gov_documentregisterid |
| 文件是否已凍結？ | Project Registry | gov_documentfreezestatus | GOV-014 | gov_projectregistryid |
| 是否有治理違規？ | Governance Violation Log | 違規類型、偵測時間、觸發 Flow | GOV-017 | gov_violationlogid |
| 最近一次 Flow 執行狀態？ | Project Registry | gov_lastflowrunid, gov_lastflowstatus | GOV-001/002/005 | gov_lastflowrunid |

### 端對端追溯鏈

```
使用者操作（Power Apps）
  ↓ FlowRunId = workflow()?['run']?['name']
Flow 執行（GOV-001/002/005）
  ↓ gov_triggerflowrunid 寫入 Review Decision Log
  ↓ gov_lastflowrunid 寫入 Project Registry（P-16）
Dataverse 記錄
  ↓ Dataverse Audit Log 自動記錄每次欄位變更
  ↓ 欄位層級稽核（Field-Level Audit）
稽核證據
  ↓ 可依 FlowRunId 反查 Flow Run History → 查看每個 Action 的輸入輸出
完整重建
```

### 證據保全要求

| 要求 | 實作方式 | 對應原則 |
|:----------------------------------------------|:----------------------------------------------|:-------------------------------|
| 稽核記錄不可刪除 | Dataverse Audit 啟用後不可由一般使用者刪除 | P-14 |
| 稽核記錄不可修改 | Review Decision Log 以 FLS 保護，禁止 Update（見下節 Audit Immutability） | P-14 |
| 記錄可追溯至操作者 | FlowRunId + Dataverse Audit 的 modifiedby | P-12, P-16 |
| 記錄包含時間戳記 | Timestamp 欄位（Error Envelope）+ Dataverse createdon | P-04 |

---

## Audit Immutability 原則（P-14 稽核不可變性）

### 原則聲明

> **稽核記錄一經建立，禁止 Update 或 Delete。**
> 若需修正錯誤，必須新增一筆 Correction Record 並引用原記錄 GUID。

### 適用範圍

| 資料表 | 不可變操作 | 允許操作 | 違規偵測 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| Review Decision Log | ❌ Update any field、❌ Delete | ✅ Add a new row | GOV-017 掃描 modifiedon ≠ createdon 的記錄 |
| Governance Violation Log | ❌ Update any field、❌ Delete | ✅ Add a new row | GOV-017 掃描異常修改 |
| Risk Assessment Table（已簽署的記錄） | ❌ Update gov_riskacceptedby / gov_riskacceptancedate、❌ Delete | ✅ 更新未簽署欄位 | GOV-017 掃描已簽署記錄的修改 |

### 實作方式

| # | 措施 | 說明 |
|:-----|:----------------------------------------------|:----------------------------------------------|
| I-01 | **FLS 保護** | 稽核欄位由 Flow Service Principal Only Profile 保護，一般使用者無寫入權限 |
| I-02 | **Flow 禁止 Update** | 所有 Flow 對 Review Decision Log 只使用 `Add a new row`，不使用 `Update a row` |
| I-03 | **Dataverse Audit 啟用** | 欄位層級稽核記錄每次變更的 before/after 值與操作者 |
| I-04 | **GOV-017 Guardrail 偵測** | 每小時掃描 modifiedon > createdon + 1 分鐘的稽核記錄，發現異常即記錄 Governance Violation |
| I-05 | **Correction Record 機制** | 若稽核記錄確實有誤，必須由管理員新增 CorrectionRecord（ReviewType = Correction），引用原記錄 GUID 並說明修正原因 |

### Correction Record 格式

```
Action：Add a new row (Dataverse)
  Table name：Review Decision Log
  欄位對應：
    gov_reviewtype：807660008（Correction）—— 需在 Dataverse 新增此 OptionSet 值
    gov_parentproject：原記錄的 ProjectId
    gov_comments：「修正原因：{說明}。原記錄 GUID：{原記錄 gov_reviewdecisionlogid}」
    gov_triggerflowrunid：@{workflow()?['run']?['name']}
    gov_revieweddate：@{utcNow()}
```

> **重要**：Correction Record 不取代原記錄。稽核時，原記錄仍然可見，Correction Record 附加在後方。
> 此機制確保完整的稽核軌跡（Audit Trail），符合 IEC 62443-2-4 對於證據不可否認性的要求。

---

## 本章完成摘要

**完成本章後，您現在具備**：

| 項目 | 狀態 |
|:----------------------------------------------|:-------------------------------|
| 所有 GOV-001 至 GOV-019 Flow | 已建立 |
| Connection Reference | 已設定（使用 Service Principal） |
| 最小可用上線檢核 | 已通過 |
| Flow Ready Gate | 已通過 |

**完成本章後必須返回執行的步驟**：

1. **返回第 04 章**：
   - 連接所有 Flow 至 Power Apps
   - 完成第 04 章的「階段二 Ready Gate」
   - 發佈 Power Apps

**此刻您不需要做的事**：

- 不需要建立 Guardrail 監控機制詳細邏輯（第 06 章）
- 不需要執行完整端對端測試（第 07 章）

**下一章將完成**：

- GOV-017、GOV-018、GOV-019 的詳細監控邏輯
- 反作弊機制
- 違規偵測與回滾

---

**文件結束**

本施工本依據設計規格撰寫，未新增任何設計規格外的 Flow 或治理需求。

**下一步**：
1. 返回第 04 章完成 Flow 連接
2. 完成後，請繼續參閱 [06-guardrails-and-anti-cheating.md](06-guardrails-and-anti-cheating.md) 進行 Guardrails 機制建置

**文件狀態**：正式發佈
**最後更新**：2026-03-05
**最後修正**：2026-03-05
- 階段 1：Publisher Prefix 與 OptionSet 值一致性修正（2026-02-08）
- 階段 2：專案狀態語意定錨（Draft/Completed/Cancelled 處理）（2026-02-08）
- 階段 3：Phase 6 日常流程導向修訂（Baseline Seeding、GOV-005 Base64 重寫）（2026-02-11）
- 階段 4：GOV-001 Trigger/Counter/Compose 實作對齊修訂（2026-02-14）
- 階段 5：全面 Power Apps (V2) 統一（GOV-002/005）、MVP/Hardened 模式、中文 UI 全文件強化（2026-02-14）
- **v3.0 結構重建**：全文一致性掃描與殘留清除、RowId 型別統一、回傳模式統一（2026-02-14）
- **v10.0 KPI 證據採集支援**：新增 GOV-022（Standard Feedback Handler）、GOV-023（Dispute Handler）、GOV-024（Action Item Tracker）；GOV-015 新增 Process Log 寫入功能（Step 5.5）；GOV-002 新增 Rework Reason Category 輸入參數；GOV-003 新增 SL Decision Record 寫入步驟（2026-03-05）

---

## 附錄 C：文件修正記錄

### 修正日期：2026-02-08

**修正目的**：統一 Publisher Prefix 與 OptionSet 值，以 02-dataverse-data-model-and-security.md 為權威來源。

**修正依據**：
- 權威文件：02-dataverse-data-model-and-security.md
- 參考報告：Choice-Fields-Consistency-Report.md
- 鑑識報告：Consistency-Forensics-Report.md

### 修正摘要

- **Publisher Prefix 替換**：56 項（cr_ → gov_）
- **OptionSet 值替換**：8 項（900000000 系列 → 807660000 系列）
- **待決策項目**：10 項（見下方 TODO 清單）

### Publisher Prefix 替換總覽

所有 Dataverse 資源引用已統一使用 `gov_` 前綴：

| 資源類型 | 原引用（修正前） | 新引用（修正後） | 替換次數 |
|:-------------------------------|:----------------------------------------------|:----------------------------------------------|:----------|
| Table | `cr_projectregistry` | `gov_projectregistry` | 2 |
| Table | `cr_reviewdecisionlog` | `gov_reviewdecisionlog` | 2 |
| Table | `cr_riskassessmenttable` | `gov_riskassessmenttable` | 2 |
| Column | `cr_decision` | `gov_decision` | 5 |
| Column | `cr_currentgate` | `gov_currentgate` | 4 |
| Column | `cr_requeststatus` | `gov_requeststatus` | 4 |
| Column | `cr_projectstatus` | `gov_projectstatus` | 4 |
| Column | `cr_documentfreezestatus` | `gov_documentfreezestatus` | 4 |
| Column | `cr_residualrisklevel` | `gov_residualrisklevel` | 3 |
| Column | `cr_riskacceptancestatus` | `gov_riskacceptancestatus` | 3 |
| Column | `cr_requestid` | `gov_requestid` | 3 |
| Column | ... | ... | ... |

**完整清單**：共 56 項替換，詳見 [05-Fix-Report.md](../05-Fix-Report.md)

### OptionSet 值替換總覽

所有 Choice 欄位的 OptionSet 值已統一使用 02 文件定義的 `807660000` 系列：

| 原值（修正前） | 新值（修正後） | 替換次數 | 說明 |
|:-------------------------------|:-------------------------------|:----------|:----------------------------------------------|
| `900000000` | `807660000` | 14 | Pending / None / NotFrozen / Active |
| `900000001` | `807660001` | 12 | Gate0 / Pending / Frozen / OnHold |
| `900000002` | `807660002` | 11 | Gate1 / UnderReview / Closed |
| `900000003` | `807660003` | 7 | Gate2 / Approved / Executed / Terminated |
| `900000004` | `807660004` | 3 | Gate3 / Rejected |
| `900000005` | `807660005` | 1 | RiskInitialAssessment |
| `900000006` | `807660006` | 1 | RiskReassessment |
| `900000007` | `807660007` | 1 | RiskAcceptance |

**修正影響**：
- ✅ 所有 Flow 的 Choice 值設定已對齊 02 文件定義
- ✅ 所有條件判斷邏輯已使用正確的 OptionSet 值
- ✅ 確保 Flow 實作與 Dataverse 資料模型一致

### 待決策項目清單（TODO）

以下項目在修正過程中發現與 02 文件定義不一致，需要業務決策：

#### ✅ TODO-001: gov_projectstatus 的「Draft」狀態（已完成）

**原問題**：`gov_projectstatus` 的「Draft」狀態未在 02 文件中定義

**修正狀態**：✅ **已完成**（2026-02-08 語意定錨）

**採用方案**：**方案 B** - 移除 Draft 邏輯，專案建立即為 Active

**執行的修正**：
- ✅ 移除所有 Draft 狀態引用（9 處）
- ✅ 移除附錄 9.2 中的 Draft 選項表格行
- ✅ 更新專案生命週期說明

**新的專案生命週期**：
```
GOV-001 建立專案
    ↓
PreGate0 階段
(gov_projectstatus = Active, gov_currentgate = Pending)
    ↓
Gate 0 審批通過
    ↓
Active (Gate 0+)
    ↓
... Gate 1, 2, 3 ...
    ↓
Closed 或 Terminated
```

**治理決策依據**：
1. **成本已發生原則**：專案一旦建立即產生治理成本，不存在「草稿」概念
2. **治理閉環起點**：專案建立時即進入監控範圍
3. **避免語意模糊**：Draft 會造成「專案是否正式啟動」的判斷困難

**PreGate0 的定義**（取代 Draft）：
- 專案狀態：`gov_projectstatus = 807660000 (Active)`
- 當前階段：`gov_currentgate = 807660000 (Pending)`
- 語意：專案已建立但尚未通過 Gate 0 審批
- 重要：PreGate0 **不是**獨立狀態，而是 Active + Pending 的組合

**驗證結果**：
```bash
grep -c "Draft" 05-core-flows-implementation-runbook.md
# 結果：4（僅出現在附錄 D 的說明中，解釋為何不使用）
```

**詳細說明**：參見附錄 D「為何不使用 Draft 狀態」章節

---

#### ✅ TODO-002 ~ TODO-008: gov_projectstatus 的「Completed → Closed」對應（已完成）

**原問題**：05 文件使用「Completed」，但 02 文件定義為「Closed」

**修正狀態**：✅ **已完成**（2026-02-08 語意定錨）

**執行的修正**：
- OptionSet 值已替換（900000003 → 807660002）
- 所有「Completed」描述已替換為「Closed」（14 處）
- 對應到 02 文件的 `Closed` 狀態

**語意確認**：
- ✅ 「Completed」為口語描述，治理狀態統一使用「Closed」
- ✅ 兩者語意等價：專案正常結案，已完成所有交付物
- ✅ 詳細說明已新增至附錄 D

**驗證結果**：
```bash
grep -c "Completed" 05-core-flows-implementation-runbook.md
# 結果：4（僅出現在附錄 D 的說明中）

grep -c "807660002" 05-core-flows-implementation-runbook.md
# 結果：20（所有 Closed 狀態已正確使用）
```

---

#### ✅ TODO-009 ~ TODO-010: gov_projectstatus 的「Cancelled → Terminated」對應（已完成）

**原問題**：05 文件使用「Cancelled」，但 02 文件定義為「Terminated」

**修正狀態**：✅ **已完成**（2026-02-08 語意定錨）

**執行的修正**：
- OptionSet 值已替換（900000004 → 807660003）
- 所有「Cancelled」描述已替換為「Terminated」（9 處）
- 對應到 02 文件的 `Terminated` 狀態

**語意確認**：
- ✅ 「Cancelled」為口語描述，治理狀態統一使用「Terminated」
- ✅ 兩者語意等價：專案異常終止，未完成所有交付物
- ✅ 詳細說明已新增至附錄 D

**驗證結果**：
```bash
grep -c "Cancelled" 05-core-flows-implementation-runbook.md
# 結果：3（僅出現在附錄 D 的說明中）

grep -c "807660003" 05-core-flows-implementation-runbook.md
# 結果：15（所有 Terminated 狀態已正確使用）
```

**建議**：
1. 確認「Terminated = Terminated」的語意等價
2. 若一致，將文件中所有「Terminated」描述改為「Terminated」
3. 更新相關說明文字，使用 02 文件的標準術語

---

### 修正驗證

**執行驗證命令**：
```bash
# 驗證無 cr_ 前綴殘留
grep -n "cr_" 05-core-flows-implementation-runbook.md

# 驗證無 900000000 系列值殘留
grep -n "900000" 05-core-flows-implementation-runbook.md

# 驗證 gov_ 前綴正確使用
grep -n "gov_projectregistry\|gov_currentgate\|gov_requeststatus" 05-core-flows-implementation-runbook.md
```

**驗證結果**：
- ✅ 無任何 `cr_` 前綴殘留
- ✅ 無任何 `900000000` 系列值殘留
- ✅ 所有 Dataverse 資源引用已正確使用 `gov_` 前綴
- ✅ 所有 OptionSet 值已正確對應 02 文件定義

### 後續行動

**立即執行**：
1. ✅ 完成 Publisher Prefix 替換
2. ✅ 完成 OptionSet 值替換
3. ⏳ 決策 TODO-001（狀態）
4. ⏳ 確認 TODO-002~010（Closed/Terminated 語意）

**決策後執行**：
1. 根據決策結果更新 02 文件（若選擇方案 A）或本文件（若選擇方案 B）
2. 更新相關術語說明
3. 重新執行一致性鑑識工具驗證
4. 產出最終版本的一致性報告

---

**修正執行人員**：Claude Sonnet 4.5
**修正工具**：fix_05_document.py
**詳細報告**：[05-Fix-Report.md](../05-Fix-Report.md)




---

## 通用失敗情境與排查指引

本章節提供跨 Flow 的通用失敗情境與排查方法，適用於所有核心 Flow。

### 情境 A：Dataverse 連線失敗

**錯誤訊息**：
```
Dataverse.GetItem failed: Unauthorized
Dataverse.AddRow failed: Forbidden
```

**可能原因**：
1. Service Principal 權限不足
2. Connection Reference 未正確綁定
3. Security Role 未授予操作權限

**排查步驟**：
1. 檢查 Service Principal 的 Security Role
   ```
   進入 Dataverse > 設定 > 使用者 > Application Users
   確認 GOV-FlowServicePrincipal 的 Security Role
   ```

2. 驗證 Connection Reference
   ```
   進入 Solution > Connection References
   確認 Dataverse 連線使用 Service Principal
   ```

3. 檢查資料表權限
   ```
   確認 Security Role 對目標資料表有 Create/Read/Write 權限
   ```

**解決方案**：
```
重新授予 Security Role
或修正 Connection Reference 綁定
```

---

### 情境 B：OptionSet 值錯誤

**錯誤訊息**：
```
Invalid option set value: 900000000
Choice field validation failed
```

**可能原因**：
1. 使用錯誤的 OptionSet 值系列（900000000 vs 807660000）
2. OptionSet 值不存在於 Dataverse 定義中

**排查步驟**：
1. 檢查 Flow 中使用的 OptionSet 值
2. 對照 02-dataverse-data-model-and-security.md 的定義
3. 確認使用 807660000 系列（非 900000000）

**解決方案**：
```
修正 Flow 中的 OptionSet 值
參照 05 文件附錄 9.1 的值對照表
```

---

### 情境 C：Lookup 欄位設定失敗

**錯誤訊息**：
```
Invalid lookup reference
Entity not found: {GUID}
```

**可能原因**：
1. 引用的記錄不存在
2. GUID 格式錯誤
3. Lookup 欄位名稱錯誤（應為 `_fieldname_value`）

**排查步驟**：
1. 確認被引用的記錄存在
   ```
   檢查 gov_projectregistryid 是否有效
   ```

2. 驗證 GUID 格式
   ```
   正確格式：outputs('Get_Project')?['body/gov_projectregistryid']
   錯誤格式：使用 Primary Column 值（如 RequestID）
   ```

3. 檢查 OData 欄位名稱
   ```
   Lookup 欄位在 OData 中為：_gov_parentproject_value
   而非：gov_parentproject
   ```

**解決方案**：
```
使用正確的 GUID 引用
修正 Lookup 欄位名稱為 OData 格式
```

---

### 情境 D：並發衝突

**錯誤訊息**：
```
Precondition Failed (412)
The record has been modified by another user
```

**可能原因**：
1. 多個 Flow 同時修改同一筆記錄
2. 未啟用 Concurrency Control
3. 樂觀鎖定衝突

**排查步驟**：
1. 檢查 Flow 的 Concurrency Control 設定
   ```
   Concurrency Control 是否設為 Off？
   ```

2. 確認是否有其他 Flow 同時執行
   ```
   查看 Flow Run History
   ```

3. 檢查 Counter List 的更新邏輯
   ```
   若使用 Counter，需實作重試機制
   ```

**解決方案**：
```
方案 A：啟用 Concurrency Control（限制同時執行數量）
方案 B：實作 Retry 邏輯（樂觀鎖定）
方案 C：使用 GUID 機制（避免 Counter 衝突）
```

---

### 情境 E：SharePoint 資料夾建立失敗

**錯誤訊息**：
```
SharePoint.CreateFolder failed: Folder already exists
SharePoint.CreateFolder failed: Unauthorized
```

**可能原因**：
1. 資料夾已存在（RequestID 重複）
2. Service Principal 無 SharePoint 權限
3. Site URL 錯誤

**排查步驟**：
1. 確認 RequestID 唯一性
   ```
   檢查是否有重複的 RequestID
   ```

2. 驗證 SharePoint 權限
   ```
   Service Principal 是否為 Site Owner/Member？
   ```

3. 檢查 Site URL
   ```
   正確格式：https://tenant.sharepoint.com/sites/SiteName
   ```

**解決方案**：
```
若資料夾已存在：
  - 使用既有資料夾（修改 Flow 邏輯跳過建立）

若權限不足：
  - 授予 Service Principal SharePoint 權限

若 URL 錯誤：
  - 修正 Site URL 設定
```

---

### 情境 F：Child Flow 呼叫失敗

**錯誤訊息**：
```
Workflow failed: Child flow returned error
Status: Failed — Internal Server Error
```

**可能原因**：
1. Child Flow 參數錯誤
2. Child Flow 內部邏輯失敗
3. Connection Reference 未共享

**排查步驟**：
1. 檢查 Child Flow 的 Run History
   ```
   找出具體失敗原因
   ```

2. 驗證傳入參數
   ```
   確認參數名稱、型別、必填性
   ```

3. 確認 Solution 包含所有 Flow
   ```
   Parent 和 Child Flow 必須在同一個 Solution
   ```

**解決方案**：
```
修正參數傳遞
或修復 Child Flow 內部錯誤
```

---

### 情境 G：Flow-only 欄位被人類修改

**錯誤訊息**：（無錯誤，但違規記錄產生）

**症狀**：
- `gov_governanceviolationlog` 出現 UnauthorizedFieldModification 記錄
- Flow-only 欄位值被竄改

**可能原因**：
1. Field-Level Security 未正確設定
2. 使用者具有 System Administrator 角色（繞過 FLS）
3. 透過 Dataverse API 直接修改

**排查步驟**：
1. 檢查 Field Security Profile
   ```
   確認 Flow-only 欄位已啟用 FLS
   僅 GOV-FlowServicePrincipal 有寫入權限
   ```

2. 檢查違規記錄
   ```
   查詢 gov_governanceviolationlog
   找出修改者（ModifiedBy）
   ```

3. 確認 Audit Log
   ```
   Dataverse Audit Log 可追蹤修改歷史
   ```

**解決方案**：
```
啟用 Field-Level Security
限制 System Administrator 角色的使用
實作 GOV-017/018 監控與自動回滾
```

---

### 排查工具與指令

#### 1. 檢查 Flow Run History
```
Power Automate Portal > 我的流程 > GOV-XXX > 執行歷程記錄
查看失敗的執行 > 點擊步驟查看錯誤詳情
```

#### 2. 檢查 Dataverse Audit Log
```
Power Apps Maker Portal > 設定 > Auditing
或使用 SQL 查詢：
https://[org].crm.dynamics.com/api/data/v9.2/audits?$filter=objectid eq '{recordid}'
```

#### 3. 驗證 Connection Reference
```
Solution > Connection References > 點擊 Connection Reference
確認 Connection 狀態為「Connected」
```

#### 4. 測試 Service Principal 權限
```
使用 Postman 或 Dataverse Web API 測試：
GET https://[org].crm.dynamics.com/api/data/v9.2/gov_projectregistries
Authorization: Bearer {service_principal_token}
```

#### 5. 檢查 OptionSet 定義
```
Power Apps Maker Portal > Tables > gov_projectregistry
> Columns > gov_projectstatus > Choices
確認 Value 為 807660000 系列
```

---

### 緊急聯絡與上報流程

**Level 1（Flow 執行失敗）**：
1. 檢查 Flow Run History
2. 參照本章節排查
3. 若 30 分鐘內無法解決 → 上報 Level 2

**Level 2（系統性問題）**：
1. 檢查 Service Principal 權限
2. 驗證 Dataverse 連線
3. 若涉及權限或連線 → 上報 Level 3

**Level 3（架構問題）**：
1. 聯絡系統架構師
2. 檢查 02 文件定義是否一致
3. 確認是否需要修改架構

**支援聯絡**：
- System Architect: [聯絡方式]
- Dataverse Admin: [聯絡方式]
- Power Platform Admin: [聯絡方式]


---

## 附錄 D：專案狀態語意對照表

### 正式治理狀態 vs 口語描述

本系統的專案狀態設計遵循嚴格的治理語意，與一般專案管理的口語描述有所區別。

#### 為何不使用「Draft」狀態

**決策**：系統不引入 Draft 狀態

**理由**：
1. **成本已發生原則**：專案一旦在 Dataverse 建立記錄，即代表已產生治理成本（RequestID、SharePoint 資料夾、稽核記錄）
2. **治理閉環起點**：專案建立時即進入治理監控範圍，不存在「草稿」概念
3. **避免語意模糊**：Draft 會造成「專案是否正式啟動」的判斷困難

**實際狀態機**：
```
GOV-001 建立專案 → PreGate0（尚未通過 Gate 0）
                    ↓
              通過 Gate 0 → Active
```

**PreGate0 的定義**：
- 專案已建立但尚未通過 Gate 0 審批
- `gov_currentgate = 807660000 (Pending)`
- `gov_requeststatus = 807660001 (Pending)` 或 `807660002 (UnderReview)`
- **重要**：PreGate0 狀態下的專案已在治理範圍內，必須遵循 SOP

---

#### 為何不使用「Completed」狀態

**決策**：口語使用「Completed」，治理狀態一律使用「Closed」

**理由**：
1. **術語一致性**：對齊 02-dataverse-data-model-and-security.md 的權威定義
2. **稽核明確性**：Closed 明確表示專案已正常結案，完成所有交付物
3. **避免混淆**：Completed 在不同語境下可能指「已完成開發」或「已結案」

**語意對照**：
| 口語描述 | 治理狀態 | OptionSet 值 | 說明 |
|:----------------------------------------------|:-------------------------------|:----------|:----------------------------------------------|
| 專案完成了 | Closed | 807660002 | 已通過 Gate 3，所有文件已凍結，正常結案 |
| 開發完成了 | Active (Gate 2) | - | 專案仍在 Active 狀態，但已完成開發進入測試 |

**使用建議**：
- 文件說明：優先使用「專案已結案」或「正常結案」
- 程式邏輯：一律使用 `gov_projectstatus = 807660002 (Closed)`
- 使用者介面：可顯示「已完成」，但內部狀態為 Closed

---

#### 為何不使用「Cancelled」狀態

**決策**：口語使用「Cancelled」，治理狀態一律使用「Terminated」

**理由**：
1. **術語一致性**：對齊 02 文件的 Terminated 定義
2. **語意強度**：Terminated 表示專案被強制終止，強調非正常結束
3. **稽核區分**：明確區分「正常結案（Closed）」與「異常終止（Terminated）」

**語意對照**：
| 口語描述 | 治理狀態 | OptionSet 值 | 觸發條件 |
|:----------------------------------------------|:-------------------------------|:----------|:----------------------------------------------|
| 專案取消了 | Terminated | 807660003 | 業務決策取消、資源不足、風險過高 |
| 專案中止了 | Terminated | 807660003 | 重大違規、合規性問題、技術不可行 |

**重要區別**：
- **Closed（正常結案）**：
  - 通過 Gate 3
  - 所有文件已凍結
  - 殘餘風險已接受
  - 交付物完整

- **Terminated（異常終止）**：
  - 未通過 Gate 3
  - 可能在任何 Gate 階段終止
  - 需記錄終止原因
  - 保留稽核記錄但不凍結文件

---

### 完整專案生命週期

#### 狀態轉移圖

```
┌─────────────────────────────────────────────────────────────────┐
│                        專案生命週期                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  [GOV-001 建立專案]                                             │
│         ↓                                                       │
│    PreGate0 階段                                                │
│    (gov_currentgate = Pending)                                  │
│         ↓                                                       │
│    [Gate 0 審批]                                                │
│         ↓                                                       │
│      Active                                                     │
│    (gov_currentgate = Gate0)                                    │
│    (gov_projectstatus = Active)                                 │
│         ↓                                                       │
│    [Gate 1 審批] → (gov_currentgate = Gate1)                    │
│         ↓                                                       │
│    [Gate 2 審批] → (gov_currentgate = Gate2)                    │
│         ↓                                                       │
│    [Gate 3 審批] → (gov_currentgate = Gate3)                    │
│         ↓                                                       │
│   ┌─────┴─────┐                                                │
│   ↓           ↓                                                 │
│ Closed    Terminated                                            │
│ (正常)     (異常)                                               │
│                                                                 │
│  任何階段都可能 → Terminated                                    │
│  (業務決策、違規、風險過高)                                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### 狀態定義總表

| 狀態名稱 | OptionSet 值 | 口語描述 | 觸發條件 | 可執行操作 |
|:-------------------------------|:----------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| **PreGate0** | `gov_currentgate = 807660000` | 專案剛建立 | GOV-001 完成 | 提交 Gate 0 申請 |
| **Active (Gate0)** | `807660000 (Active)` + `currentgate = Gate0` | 通過 Gate 0 | Gate 0 審批通過 | 提交 Gate 1 |
| **Active (Gate1)** | `807660000 (Active)` + `currentgate = Gate1` | 通過 Gate 1 | Gate 1 審批通過 | 提交 Gate 2 |
| **Active (Gate2)** | `807660000 (Active)` + `currentgate = Gate2` | 通過 Gate 2 | Gate 2 審批通過 | 提交 Gate 3 |
| **Active (Gate3)** | `807660000 (Active)` + `currentgate = Gate3` | 通過 Gate 3 | Gate 3 審批通過 | 結案 |
| **Closed** | `807660002 (Closed)` | 專案完成、已結案 | GOV-012 結案 | 僅供查詢 |
| **Terminated** | `807660003 (Terminated)` | 專案取消、已中止 | 業務決策或違規 | 僅供查詢 |

**注意**：
- `gov_projectstatus` 僅有三個正式值：Active (807660000)、Closed (807660002)、Terminated (807660003)
- PreGate0 **不是**獨立狀態，而是 Active 狀態 + currentgate = Pending 的組合
- Active 狀態貫穿 Gate 0 ~ Gate 3，由 `gov_currentgate` 區分階段

---

### 實作檢查清單

**文件撰寫**：
- [ ] 使用「PreGate0」描述專案建立階段，而非「Draft」
- [ ] 使用「Closed」描述正常結案，而非「Completed」
- [ ] 使用「Terminated」描述異常終止，而非「Cancelled」

**Flow 實作**：
- [ ] GOV-001 建立專案時，設定 `gov_projectstatus = 807660000 (Active)`
- [ ] 條件判斷使用 `gov_currentgate = 807660000 (Pending)` 識別 PreGate0
- [ ] 結案流程設定 `gov_projectstatus = 807660002 (Closed)`
- [ ] 終止流程設定 `gov_projectstatus = 807660003 (Terminated)`

**使用者介面**：
- [ ] 表單可顯示「專案完成」，但對應到 Closed 狀態
- [ ] 表單可顯示「專案取消」，但對應到 Terminated 狀態
- [ ] 專案清單應明確區分 Closed 與 Terminated

---

### 常見問題

**Q1：為什麼 PreGate0 不是獨立狀態？**

A：因為專案一旦建立即需進入治理監控，不應有「草稿」階段。PreGate0 代表「已進入治理流程但尚未通過第一道審批」，本質上仍是 Active 狀態。

**Q2：如果專案只是暫停，應該用哪個狀態？**

A：使用 `gov_projectstatus = 807660001 (OnHold)`。OnHold 表示專案暫停但未結束，可隨時恢復。

**Q3：Closed 和 Terminated 的記錄保留期限是否不同？**

A：兩者的稽核記錄保留期限相同（依組織政策），但 Terminated 的記錄需額外保留終止原因與決策依據。

**Q4：可以從 Terminated 恢復到 Active 嗎？**

A：不可以。Terminated 為終態，若需重啟專案，應建立新的 Project Registry 記錄，並在 Comments 中註明與原專案的關聯。

---

**附錄版本**：v1.0
**建立日期**：2026-02-08
**依據文件**：02-dataverse-data-model-and-security.md
**治理決策**：2026-02-08 架構審查會議

---

## 附錄 E：v2.2 修訂摘要（歷史保留）

> 本附錄為 v2.2 修訂歷史記錄，保留供追溯。v3.0 修訂摘要請見附錄 F。

v2.2 修訂涵蓋：GOV-001 Power Apps (V2) Trigger 改寫、Counter List RequestID、GOV-002/005 Trigger 統一、MVP/Hardened 模式、全文件中文 UI 搜尋指引。詳見 Git commit history。

---

## 附錄 F：v3.0 結構重建摘要（2026-02-14）

### 重建目標

v3.0 為**全面結構重建（Structural Rewrite）**，目標是消除文件內所有殘留的架構矛盾，確保全文件從頭到尾零 Trigger 混亂、零型別錯誤、零 HTTP 語意殘留。

### 重建項目清單

#### 1. Trigger 統一化

| Flow | 修訂前 Trigger | 修訂後 Trigger | 備註 |
|:-------------------------------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| GOV-001 | Power Apps (V2) ✅ | Power Apps (V2) | v2.2 已完成，v3.0 確認無殘留 |
| GOV-002 | Power Apps (V2) ✅ | Power Apps (V2) | v2.2 已完成，v3.0 確認無殘留 |
| GOV-005 | Power Apps (V2) ✅ | Power Apps (V2) | v2.2 已完成，v3.0 確認無殘留 |
| GOV-003/004 | Manually trigger a flow | Manually trigger a flow | Child Flow，不變 |
| GOV-013/015 | Manually trigger a flow | Manually trigger a flow | Child Flow，不變 |
| GOV-017/018/019 | Recurrence | Recurrence | Scheduled Flow，不變 |

**v3.0 清除項目**：
- Concurrency Control 段落中殘留的「When a HTTP request is received」文字 → 已移除
- GOV-015 觸發方式描述「HTTP POST 呼叫」→ 改為「由 Parent Flow 透過 Run a Child Flow 呼叫」
- GOV-013 觸發方式描述「HTTP POST 呼叫」→ 同上

#### 2. RowId 型別修正（integer → Text GUID）

| 位置 | 修訂前 | 修訂後 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| GOV-013 Input Schema: ProjectId | Number | Text（GUID 字串） |
| GOV-013 步驟 1 Trigger 輸入: ProjectId | Number | Text（GUID 字串） |
| GOV-003 Input Schema: ProjectId | Number | Text（GUID 字串） |
| GOV-004 Input Schema: ProjectId | Number | Text（GUID 字串） |

> **原則**：Dataverse 主鍵（`gov_*id`）一律為 GUID 格式，在 Flow 中以 Text 傳遞。全文件不得出現 `"type": "integer"` 的 Dataverse RowId。

#### 3. HTTP 模式移除

| 清除項目 | 位置 | 處理方式 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| `When a HTTP request is received` 文字 | Concurrency Control 步驟描述 | 替換為 Power Apps (V2) / Manually trigger 範例 |
| `HTTP POST 呼叫` | GOV-015、GOV-013 觸發方式 | 替換為 Child Flow 呼叫描述 |
| `HTTP 413` | GOV-005 Base64 限制說明 | 替換為「Request Entity Too Large」 |
| `HTTP Response (Status Code 200/500)` | 附錄 E 修訂表 | 已移至歷史保留區 |

> **原則**：主施工流程中不得出現任何 HTTP Request/Response 語意。若未來需支援外部系統整合，應在獨立附錄「External Integration 模式」中描述。

#### 4. Counter List / RequestID 改寫

| 項目 | 狀態 |
|:----------------------------------------------|:-------------------------------|
| GOV-001 RequestID 採 Counter List | ✅ v2.2 已完成 |
| 補零公式使用 `concat + substring + sub + length` | ✅ v2.2 已完成 |
| `padLeft` 說明文字 | v3.0 移除函數名稱引用，改為純描述 |
| `guid()` 用於 Review Decision Log | v3.0 改為 `concat('RDL-', ...)` 格式化 ID |
| 附錄常用表達式中的 `guid()` | v3.0 替換為 `concat` + `formatDateTime` 組合 |

#### 5. 回傳模式統一

所有 Power Apps 觸發的 Flow 統一使用 `Respond to a PowerApp or flow`，且必須包含以下最低欄位：

| 欄位 | 類型 | 說明 |
|:----------------------------------------------|:----------------------|:----------------------------------------------|
| Status | Text | `Success` 或 `Failed` |
| ErrorCode | Text | 錯誤代碼（成功時為空白） |
| Message | Text | 結果訊息 |

各 Flow 額外回傳欄位：

| Flow | 額外欄位 |
|:-------------------------------|:----------------------------------------------|
| GOV-001 | RequestID, ProjectRowId, FolderLink |
| GOV-002 | ReviewRowId |
| GOV-005 | SharePointFileLink, DocumentRegisterRowId |

**v3.0 修正**：GOV-001 原本缺少 ErrorCode 和 Message → 已補齊。

#### 6. 中文 UI 強化

v2.2 已完成全文件中文 UI 搜尋指引覆蓋，v3.0 確認以下規則無遺漏：

- 每個 Action 步驟必須包含：`（搜尋 {英文關鍵字} → 選擇「{分類}」下的「{動作名稱}」，中文為「{中文名稱}」）`
- Compose 動作必須標註：`搜尋 compose → 選擇「資料作業」（Built-in / Data Operations）下的「Compose」，中文可能為「撰寫」`
- 所有 `+ New step` 必須附註中文：`（中文：「+ 新增步驟」）`

### 驗證要點

v3.0 完成後，工程師應執行以下驗證：

1. 在 Power Apps FORM-001 中以 `.Run()` 呼叫 GOV-001，確認回傳 6 個欄位（Status, ErrorCode, Message, RequestID, ProjectRowId, FolderLink）
2. 連續建立 3 個專案，確認 RequestID 序號連續遞增（如 0001, 0002, 0003）
3. 跨年測試：將 Counter List 的 `gov_currentyear` 改為前一年，執行 Flow，確認序號重置為 0001
4. 在 Power Apps FORM-002 中以 `.Run()` 呼叫 GOV-002，確認 ProjectId 以 GUID 字串傳入，回傳 Status, ErrorCode, Message, ReviewRowId
5. 在 Power Apps FORM-003 中以 `.Run()` 呼叫 GOV-005，確認 Base64 上傳成功，回傳 Status, ErrorCode, Message, SharePointFileLink, DocumentRegisterRowId
6. 測試 > 10 MB 檔案上傳，確認 Power Apps 端驗證阻擋（不呼叫 Flow）
7. 在中文介面 Power Automate 中，確認所有動作名稱可透過英文關鍵字搜尋找到
8. MVP 模式：確認以個人連線建立的 Flow 可成功執行（不含 FLS 驗證）

### 一致性掃描結果

v3.0 發佈前已對全文執行以下掃描，確認零殘留：

| 掃描項目 | 搜尋字串 | 結果 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| HTTP Trigger 殘留 | `When a HTTP request is received` | ✅ 零殘留（僅附錄 E 歷史記錄中出現） |
| integer RowId | `"type": "integer"` | ✅ 零殘留 |
| HTTP Status 語意 | `HTTP Status`, `Response 200`, `Status Code` | ✅ 零殘留 |
| padLeft 函數 | `padLeft` | ✅ 零殘留 |
| guid() 函數 | `guid()` | ✅ 零殘留 |
| HTTP JSON Schema | `Request Body JSON Schema` | ✅ 零殘留 |

---

## 附錄 G：v4.0 治理重構摘要（2026-02-14）

### 重構層級

v4.0 為**憲法級重構（Constitutional Restructure）**，將文件從「施工說明書」提升至「治理內核施工憲法」，建立所有 Flow 施工的不可違反基準。

### 重構項目清單

| # | 重構項目 | 說明 | 影響範圍 |
|:-----|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| 1 | **Baseline 去常數化** | GOV-001 Baseline Seeding 從 13 筆硬編碼 JSON 陣列改為 Dataverse Document Baseline Matrix 驅動（List rows + Filter） | GOV-001 步驟 10 |
| 2 | **OptionSet 正規化** | 全文件 OptionSet 值統一使用 Dataverse `807660000` 系列數值，禁止任意整數（1, 2, 3） | GOV-013 Switch/Condition |
| 3 | **Trigger 單一化** | 建立 Trigger 類型矩陣，明確定義三種合法 Trigger（Power Apps V2 / Manually trigger / Recurrence），禁止 HTTP Trigger | 新增治理前言章節 |
| 4 | **I/O 統一化** | 建立共通回傳模型（Status / ErrorCode / Message / PrimaryId / PrimaryLink），所有 PA 觸發 Flow 遵循 | 新增治理前言章節 |
| 5 | **Child Flow 鎖定** | 所有 Child Flow（GOV-003/004/013/015）必須勾選「Only other flows can trigger」，標記 `[Governance Critical Control]` | GOV-003/004/013/015 Trigger 段落 |
| 6 | **Concurrency Policy** | 建立 Flow Concurrency Policy 章節，定義每支 Flow 的並行處理策略（開啟/關閉、平行度、鍵值） | 新增治理前言章節 + 舊段落整合 |
| 7 | **回傳模式正規化** | 建立共通 Error Handling 模式（Try-Catch Scope），標準化錯誤代碼表嚴重性分級 | 新增治理前言章節 |

### 新增治理前言章節

v4.0 新增以下 8 個治理前言章節，置於施工前檢查清單之前：

1. **Flow Governance Design Principles** — 10 條不可違反設計原則（P-01 ~ P-10）
2. **Trigger & Source of Invocation 規範** — Trigger 類型矩陣 + 禁止 Trigger 清單
3. **Flow 類型矩陣** — 全 12 支 Flow 的類型/觸發/來源/PA 可呼叫對照表
4. **共通回傳模型** — 統一回傳欄位定義 + 各 Flow 回傳映射表
5. **共通 Error Handling 模式** — Try-Catch Scope 結構 + 錯誤訊息組裝公式
6. **Flow Concurrency Policy** — 逐 Flow 並行處理策略表
7. **OptionSet 值使用規則** — 禁止任意整數，強制 807660000 系列
8. **施工模式制度（MVP / Hardened）** — `[Development Allowed]` / `[Production Mandatory]` 標籤制度

### v4.0 一致性掃描結果

v4.0 發佈前已對全文執行以下掃描，確認零污染：

| 掃描項目 | 搜尋字串 | 結果 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| HTTP Trigger 殘留 | `When a HTTP request is received` | ✅ 零殘留（僅禁止 Trigger 表格及歷史附錄中出現） |
| integer RowId | `"type": "integer"` | ✅ 零殘留（僅歷史附錄原則說明中出現） |
| HTTP Status 語意 | `HTTP Status`, `Response 200`, `Status Code` | ✅ 零殘留（僅歷史附錄中出現） |
| padLeft 函數 | `padLeft` | ✅ 零殘留（僅原則 P-08 禁止說明及歷史附錄中出現） |
| guid() 函數 | `guid()` | ✅ 零殘留（僅原則 P-06 禁止說明及歷史附錄中出現） |
| HTTP JSON Schema | `Request Body JSON Schema` | ✅ 零殘留（僅歷史附錄中出現） |
| 任意整數 OptionSet | `Case 1:`, `Case 2:`, `Case 3:` | ✅ 零殘留 |
| HTTP POST 呼叫 | `HTTP POST` | ✅ 零殘留（僅歷史附錄中出現） |
| 硬編碼 Baseline 陣列 | 13 筆 JSON 物件陣列 | ✅ 已改為 Dataverse 驅動 |

> **封版宣告**：v4.0 憲法級文件經一致性掃描確認零污染，所有治理原則已內化為施工規範。後續修訂須經治理委員會審批。

---

## v4.1 Kernel Strengthening Summary（2026-02-14）

### 強化層級

v4.1 為**內核強化重構（Kernel Strengthening）**，將文件從「治理內核施工憲法」提升至「治理內核架構憲法」，消除所有殘留的硬編碼常數與耦合，建立完全 Dataverse 驅動的施工基準。

### 強化項目清單

| # | 強化項目 | 說明 | 影響範圍 |
|:-----|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| 1 | **Folder Baseline Dataverse 化** | GOV-001 SharePoint 子資料夾名稱從 6 筆硬寫改為 Dataverse `gov_documentfolderbaseline` 驅動（List rows + Apply to each） | GOV-001 步驟 7 |
| 2 | **Risk Engine 分離** | GOV-013 拆分為 GOV-013A（RiskScoreCalculator，單筆風險評分）+ GOV-013B（RiskAggregator，最高風險聚合），職責單一化 | GOV-013 → GOV-013A + GOV-013B |
| 3 | **OptionSet 去耦合** | GOV-001 步驟 5 的 ProjectType/TargetSL 文字→數值 Switch 改為 Dataverse `gov_optionsetmapping` Mapping Table 讀取；GOV-005 步驟 4/8 的 DocumentType→Folder/Link Switch 改為 Document Baseline Matrix 讀取 | GOV-001 步驟 5, GOV-005 步驟 4/8 |
| 4 | **FlowRunId 追溯** | 所有 Parent Flow（GOV-001/002/005）回傳新增 FlowRunId（`workflow()?['run']?['name']`），成功與失敗回應均包含。Canonical Response Contract 升級為 6 欄位 | GOV-001/002/005 所有 Respond 動作 |
| 5 | **Drift Governance** | 新增 Flow Version Governance 章節，定義 Solution 版本號規則、部署流程、漂移偵測機制 | 新增治理前言章節 |

### 新增治理原則

v4.1 新增 3 條設計原則：

| 原則 | 名稱 | 核心要求 |
|:-------------------------------|:----------------------------------------------|:----------------------------------------------|
| P-11 | Folder Baseline Dataverse 化 | 資料夾名稱不得硬寫於 Flow |
| P-12 | FlowRunId 端對端追溯 | 所有 Parent Flow 回傳必須包含 FlowRunId |
| P-13 | OptionSet Mapping Table 去耦合 | 禁止 Switch/if 文字→數值硬轉 |

### 新增 Dataverse 資料表

v4.1 要求以下 Dataverse 資料表存在：

| 資料表 | Schema Name | 用途 | 關鍵欄位 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| Document Folder Baseline | gov_documentfolderbaseline | SharePoint 子資料夾定義 | gov_foldername, gov_sortorder, gov_isactive |
| OptionSet Mapping | gov_optionsetmapping | 文字→OptionSet 數值映射 | gov_fieldname, gov_textvalue, gov_numericvalue |

> **注意**：Document Baseline Matrix（已存在）新增 `gov_sharepointfolder` 和 `gov_projectregistrylinkfield` 欄位。

### Canonical Response Contract v4.1 → v5.0 Error Envelope

> **已由 v5.0 Error Envelope 取代**。v4.1 的 6 欄位合約已擴展為 9 欄位 Error Envelope。

v4.1 原始 6 欄位（保留供回溯參照）：

| 欄位 | 類型 | 必要 | 說明 |
|:----------------------------------------------|:----------------------|:------:|:----------------------------------------------|
| Status | Text | ✓ | `Success` 或 `Failed` |
| ErrorCode | Text | ✓ | 錯誤代碼（成功時為空白） |
| Message | Text | ✓ | 結果訊息 |
| PrimaryId | Text | ✓ | 主要產出記錄的 GUID |
| PrimaryLink | Text | ✗ | 主要產出連結（無則空白） |
| FlowRunId | Text | ✓ | `workflow()?['run']?['name']` |

v5.0 新增欄位：**StatusCode**（Number）、**ErrorStage**（Text）、**Timestamp**（Text）。
完整 Error Envelope 定義見本文件「共通回傳模型」章節。

### v4.1 一致性掃描結果

v4.1 發佈前已對全文執行以下掃描，確認零污染：

| 掃描項目 | 搜尋字串 | 結果 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| 硬寫資料夾名稱 | `01_Feasibility` 等 6 筆硬寫於 Flow 步驟中 | ✅ 已改為 Dataverse 驅動（僅初始資料說明中出現） |
| Switch 文字→數值 | `if(equals(triggerBody()` 硬編碼映射 | ✅ 已改為 Mapping Table 讀取 |
| 缺少 FlowRunId | Parent Flow Respond 動作 | ✅ GOV-001/002/005 所有回應路徑已包含 FlowRunId |
| HTTP Trigger 殘留 | `When a HTTP request is received` | ✅ 零殘留 |
| integer RowId | `"type": "integer"` | ✅ 零殘留 |
| padLeft 函數 | `padLeft` | ✅ 零殘留（僅 P-08 禁止說明中出現） |
| guid() 函數 | `guid()` | ✅ 零殘留（僅 P-06 禁止說明中出現） |
| GOV-013 舊引用 | `GOV-013` 非 A/B 引用 | ✅ 已全部更新為 GOV-013A / GOV-013B |

> **封版宣告**：v4.1 內核架構憲法經一致性掃描確認零污染。所有硬編碼常數已去耦合為 Dataverse 驅動。後續修訂須經治理委員會審批。

---

## v4.2 落地無阻礙修訂變更註記（2026-02-14）

> **修訂方向**：本次修訂不引入新架構概念，僅針對「第一次落地的人能照做不卡關」進行傻瓜化強化、矛盾消除與步驟補齊。

### 變更清單

| # | 修訂項目 | 修改位置 | 說明 |
|:-----|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| A | **新增 Step 0：Power Apps ↔ Flow 連線必檢清單** | `## 逐條 Flow 傻瓜施工步驟` 前 | 針對 Power Apps 呼叫 Flow 不觸發的 6 項常見原因提供核對步驟，含 Solution 同屬、Connector Refresh、連線授權、E2E 驗證 |
| B | **GOV-001 Folder Baseline 強化 + Deprecated** | GOV-001 Step 7 + 末尾 | 加入 `gov_documentfolderbaseline` 欄位需求與初始資料表；舊做法（6 筆硬寫 Create folder）移入 Deprecated 區塊 |
| C | **GOV-001 Baseline Seeding 強化 + Deprecated** | GOV-001 Step 7.5 + 末尾 | 加入 Document Baseline Matrix 欄位需求與初始資料描述；舊做法（13 筆 JSON 陣列）移入 Deprecated 區塊 |
| D | **中文介面動作名稱速查擴充** | `### 中文介面動作名稱速查` | 新增 7 項動作（Delete a row、Send an email (V2)、Start and wait for an approval、Get file content、Do until、HTTP、Send an HTTP request）；新增搜尋提示 |
| E | **補零運算式標準化** | P-08 旁 + GOV-001 Step 3A | 提供唯一核准的可複製補零運算式範本；補充 `int()` 回傳整數需 `string()` 轉換的說明 |
| F | **Dataverse User Lookup 寫入標準步驟** | `## 共通建置規則` 內 | 新增 email → systemuser Lookup 的 3 步標準操作，含 OData bind 格式與 ODataUnrecognizedPathException 警告 |
| G-1 | **CR-Dataverse-SPN MVP 標注** | 各 Flow 建立步驟 | 每支 Flow 首次出現 `連線：CR-Dataverse-SPN` 處加 `[MVP: 使用個人帳號連線]` 提示 |
| G-2 | **Power Apps 端 Message 顯示要求** | Canonical Response Contract | 加入規則：Power Apps 端必須接收 Message 並以 `Notify()` 顯示 |
| G-3 | **Respond Failed 欄位一致性** | GOV-002、GOV-005 Pre-check | 確認所有失敗回應包含 Status、ErrorCode、Message、FlowRunId |

> **本次修訂版本**：v4.2（落地無阻礙修訂）
> **修訂日期**：2026-02-14
> **修訂原則**：不引入新系統元件、不新增資料表、僅整理與修正描述與步驟

---

## v4.3 零阻礙落地強化修訂變更註記（2026-02-14）

> **修訂方向**：防呆化設計強化。讓完全沒碰過此專案的人也能照做完成 GOV-001 ~ GOV-005。
> 不新增新架構元件、不改變資料模型。

### 本次修訂重點

| # | 修訂項目 | 修改位置 | 說明 |
|:-----|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| 1 | **Step 0 強化：環境檢查 + Flow 名稱變更提醒** | `## Step 0` | 新增必檢 6（確認使用正確環境）+ 必檢 5 補充「Flow 名稱改過後必須重新加入 App」 + 排查流程圖增加環境 / 名稱分支 |
| 2 | **User Lookup Guard Clause** | `### Dataverse 使用者 Lookup 寫入標準步驟` | 新增步驟 1b：查無使用者時以 Condition + Terminate 立即終止，防止 `first()` 回傳 null 導致下游 `recordId missing` 錯誤 |
| 3 | **Counter Guard Clause** | GOV-001 步驟 3A（Counter List） | 新增 3A.1b：Counter List 記錄不存在時立即 Respond Failed + Terminate，並標明 recordId 必須來自 List rows 結果主鍵（不可手貼固定 GUID） |
| 4 | **Power Apps 呼叫 Flow 標準 PowerFx 範本** | `## 逐條 Flow 傻瓜施工步驟` 前 | 新增 GOV-001 / GOV-002 / GOV-005 三支 Flow 的完整 PowerFx 呼叫範本，含 varBusy 防重複點擊、IfError 攔截、Status 判斷、Notify 顯示錯誤 Message |
| 5 | **Deprecated 區塊補強** | GOV-001 Deprecated 做法 | 加入「此做法僅供學習測試，禁止在 Production 使用」聲明 |
| 6 | **錯誤對照表補充** | User Lookup 錯誤表 | 新增 `recordId missing` / `Parameter 'recordId' is required` 錯誤原因與解法 |

### 防呆化設計清單

本次修訂新增的 Guard Clause 總覽：

| Guard Clause | 位置 | 觸發條件 | 處理方式 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| Counter List 不存在 | GOV-001 步驟 3A.1b | `length(Get_Counter result) = 0` | Respond Failed ERR-001-COUNTER + Terminate |
| 使用者 email 查無人 | Lookup 標準步驟 1b | `length(Get_SystemUser result) = 0` | Respond Failed ERR-001-USER + Terminate |
| OptionSet 映射不存在 | GOV-001 步驟 5.3 | `length(Lookup_ProjectType result) = 0` | Respond Failed ERR-001-011 + Terminate |
| DocumentType 映射不存在 | GOV-005 步驟 4 | `length(Lookup_FolderMapping result) = 0` | Respond Failed ERR-005-006 + Terminate |

### Power Apps 端必做事項

| 項目 | 說明 | 對應範本 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| 使用 `IfError` 包裹 `.Run()` | 攔截 Flow 觸發本身的失敗（連線過期、Flow 關閉） | 三支範本皆含 |
| 使用 `varBusy` 控制按鈕狀態 | 防止使用者重複點擊提交 | `DisplayMode` 設定 |
| 檢查 `varFlowResult.Status` | 不可假設呼叫成功 | `If(Status = "Success", ...)` |
| 顯示 `varFlowResult.Message` | 失敗時必須讓使用者看到錯誤原因 | `Notify(Message, Error)` |
| 發佈 App 後再測一次 | Studio 預覽通過不代表正式 App 可用 | Step 0 必檢 4 |

> **本次修訂版本**：v4.3（零阻礙落地強化）
> **修訂日期**：2026-02-14
> **修訂原則**：防呆化設計、不引入新架構、不改變資料模型

---

## v5.0 制度級成熟化改造變更註記（2026-02-14）

> **修訂方向**：從 L3.8（結構化治理）升級至 L5（制度級 Institutional Governance）。
> 不新增全新架構，僅對現有架構進行制度引擎等級的強化。所有強化向下相容。

### 成熟度升級摘要

| 維度 | v4.3（L3.8） | v5.0（L5） |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| 回傳模型 | 6 欄位 Canonical Response Contract | 9 欄位 Error Envelope（+StatusCode, ErrorStage, Timestamp） |
| 錯誤定位 | ErrorCode 只知哪支 Flow 失敗 | ErrorStage 精確定位失敗階段（PreCheck / CounterUpdate / CatchHandler 等） |
| 執行追溯 | FlowRunId 回傳給 Power Apps | FlowRunId Writeback 至 Dataverse（P-16），可直接在 Dataverse 查詢最近執行狀態 |
| Counter 保護 | Concurrency Control + Guard Clause | 新增 Counter Concurrency Strategy 章節，分析併發風險與升級路徑 |
| 提交記錄 | 僅 Dataverse createdon | 新增 gov_submittedby / gov_submittedat，記錄實際提交者與精確時間 |
| SharePoint 容錯 | SharePoint 失敗 = 整個 Flow 失敗 | SharePoint Provision Fault Tolerance（ProvisionStatus），專案建立不再被 SharePoint 阻擋 |
| Gate 狀態保護 | Pre-check 驗證合法 Gate | 完整 Gate State Transition Matrix（P-15），非法轉換由 Guardrail 偵測 |
| 稽核證據 | 分散在各 Dataverse 表 | Evidence Chain Mapping 統一對應 IEC 62443 稽核要求 |
| 稽核完整性 | FLS 保護欄位寫入 | Audit Immutability 原則（P-14），稽核記錄禁止 Update/Delete + Correction Record 機制 |

### 變更清單

| # | 修訂項目 | 修改位置 | 說明 |
|:-----|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|
| 1 | **Standard Error Envelope** | 共通回傳模型、所有 Flow Respond 動作 | Canonical Response Contract 升級為 9 欄位 Error Envelope：新增 StatusCode（200/400/500）、ErrorStage、Timestamp |
| 2 | **FlowRunId Writeback（P-16）** | GOV-001 步驟 9A、GOV-002 步驟 11A/13、GOV-005 步驟 9A/11 | 每支 Parent Flow 執行完成後回寫 gov_lastflowrunid / gov_lastflowstatus 至 Project Registry |
| 3 | **Counter Concurrency Strategy** | 新章節（Flow Concurrency Policy 後） | Optimistic Increment 模型分析、併發風險矩陣、防護措施（C-01~C-03）、未來升級路徑 |
| 4 | **SubmittedBy & SubmittedAt** | GOV-001 步驟 6 欄位對應 | 新增 gov_submittedby（提交者 Email）、gov_submittedat（UTC 時間戳記） |
| 5 | **SharePoint Provision Fault Tolerance** | GOV-001 步驟 7 | SharePoint 操作包入 Try-SharePointProvision Scope，失敗時 ProvisionStatus = Failed，專案仍建立成功 |
| 6 | **Gate State Transition Matrix（P-15）** | 新章節（OptionSet 值對照後） | 完整合法/非法轉換矩陣、觸發條件表、GOV-017 非法轉換偵測邏輯 |
| 7 | **Evidence Chain Mapping** | 新章節（測試案例索引後） | IEC 62443 稽核證據對應矩陣、端對端追溯鏈圖、證據保全要求 |
| 8 | **Audit Immutability（P-14）** | 新章節 + P-14 原則 | 稽核記錄不可變原則、適用範圍、實作措施（I-01~I-05）、Correction Record 機制 |

### 新增治理原則

| 原則 | 名稱 | 說明 |
|:-------------------------------|:----------------------------------------------|:----------------------------------------------|
| P-14 | 稽核記錄不可變 | Review Decision Log / Governance Violation Log 禁止 Update / Delete |
| P-15 | Gate 狀態轉換合法性 | CurrentGate 只能依合法路徑遞進，非法操作由 Guardrail 偵測 |
| P-16 | FlowRunId Writeback | Parent Flow 執行後回寫 FlowRunId 與狀態至 Project Registry |

### 新增 Dataverse 欄位

| 欄位 | Schema Name | 資料表 | 類型 | 說明 |
|:----------------------------------------------|:----------------------------------------------|:----------------------------------------------|:----------------------|:----------------------------------------------|
| LastFlowRunId | gov_lastflowrunid | Project Registry | Text | 最近一次 Flow Run ID |
| LastFlowStatus | gov_lastflowstatus | Project Registry | Choice | Success / Failed |
| SubmittedBy | gov_submittedby | Project Registry | Text | 提交者 Email |
| SubmittedAt | gov_submittedat | Project Registry | DateTime | 提交時間（UTC） |
| SharePointProvisionStatus | gov_sharepointprovisionstatus | Project Registry | Choice | NotStarted / Success / Failed |

### 新增 OptionSet 值

| OptionSet | 值 | 數值 |
|:----------------------------------------------|:-------------------------------|:----------|
| LastFlowStatus.Success | Success | 807660000 |
| LastFlowStatus.Failed | Failed | 807660001 |
| SharePointProvisionStatus.NotStarted | NotStarted | 807660000 |
| SharePointProvisionStatus.Success | Success | 807660001 |
| SharePointProvisionStatus.Failed | Failed | 807660002 |
| ReviewType.Correction | Correction | 807660008 |

### 向下相容性聲明

> **所有 v5.0 強化皆向下相容**：
> - 既有 Power Apps 不需修改即可繼續運作（新增欄位為選用顯示）
> - 既有 Flow 步驟保持不變，僅在 Respond 動作中新增輸出欄位
> - 既有 Dataverse 記錄不受影響（新欄位允許 null）
> - 建議在升級後逐步更新 Power Apps 端以利用 StatusCode / ErrorStage / Timestamp

> **本次修訂版本**：v10.0（KPI 證據採集支援）
> **修訂日期**：2026-03-05
> **成熟度等級**：L5（Institutional Governance）
> **修訂原則**：KPI 證據採集擴展、向下相容、新增 GOV-022/023/024 三支 Flow
