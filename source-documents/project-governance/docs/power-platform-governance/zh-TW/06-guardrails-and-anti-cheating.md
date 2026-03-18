# Guardrails 與反作弊機制實作規格

## 文件控制資訊

| 項目 | 內容 |
|:------|:------|
| 文件編號 | IMPL-06-GOV-GUARDRAILS-001 |
| 版本 | 1.1 |
| 分類 | 實作規格 |
| 前置文件 | 02-dataverse-data-model-and-security.md、05-core-flows-implementation-runbook.md |
| 權威來源 | SOP-03-v4-Part3、SOP-04-v2-Part3、SOP-04-v2-Part4 |
| 適用對象 | Power Platform 開發人員、治理系統維護人員、資安稽核人員 |

---

## 文件權威宣告

> **本文件為治理控制機制之唯一權威定義。**

### 本文件之權威範圍

| 權威範圍 | 說明 |
|:---------|:------|
| **Guardrail 機制設計** | 三道防線架構、偵測邏輯、回滾機制的設計意圖與行為定義 |
| **違規判斷標準** | 何為違規、違規嚴重程度、違規處理方式 |
| **通知與升級規則** | 通知對象、升級層級、回應時限 |
| **監控指標與 KPI** | Guardrail 相關的監控指標定義與目標值 |

### 本文件與 05 文件之關係

| 文件 | 定位 | 權威範圍 |
|:------|:------|:---------|
| **本文件（06）** | 治理語意權威 | Guardrail 機制的「是什麼」與「為什麼」 |
| **05 文件** | 施工步驟權威 | GOV-017/018/019 的「如何建置」 |

### 權威解讀原則

1. **行為解讀**：當需判斷某項修改是否為「違規」時，以本文件定義為準
2. **機制設計**：當需理解 Guardrail 的設計意圖時，以本文件說明為準
3. **施工步驟**：當需建置 GOV-017/018/019 Flow 時，以 05 文件步驟為準
4. **衝突處理**：若 05 文件施工步驟與本文件設計意圖有衝突，以本文件設計意圖為準，但不得擅自修改 05 文件步驟，應回報 Governance Function 處理

### 適用聲明

本文件適用於以下情境：

| 情境 | 使用方式 |
|:------|:---------|
| 稽核審查 | 依本文件判斷系統行為是否符合設計 |
| 違規處理 | 依本文件判斷違規類型與處理方式 |
| 爭議仲裁 | 依本文件定義作為裁決依據 |
| 機制理解 | 依本文件理解 Guardrail 設計意圖 |

> **注意**：GOV-017/018/019 的施工步驟請以 05-core-flows-implementation-runbook.md 為準。本文件中的步驟說明僅供理解設計意圖，不作為施工依據。

---

## 機制總覽

### Guardrail 三道防線架構

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           治理系統 Guardrail 三道防線                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  【第一道防線】Field-Level Security                                           │
│  ├── 預防性控制：禁止人類使用者直接修改 Flow-only 欄位                         │
│  ├── 設定位置：Dataverse → Tables → Field-Level Security Profile             │
│  └── 失敗時：Dataverse 回傳權限錯誤，操作直接被拒絕                            │
│                                                                             │
│  【第二道防線】GOV-017 Guardrail Monitor                                      │
│  ├── 偵測性控制：每小時偵測繞過 Field-Level Security 的違規修改                │
│  ├── 觸發方式：Recurrence（每小時整點）                                       │
│  ├── 偵測來源：Dataverse Audit Log                                           │
│  └── 失敗時：自動回滾 + 發送高優先級違規通知                                   │
│                                                                             │
│  【第三道防線】GOV-018 Compliance Reconciler                                  │
│  ├── 對帳性控制：每日比對 Event Entity 與 Aggregate Entity 狀態一致性          │
│  ├── 觸發方式：Recurrence（每日 00:00 UTC+8）                                 │
│  ├── 偵測範圍：CurrentGate vs Review Decision Log、文件連結有效性             │
│  └── 失敗時：建立合規警報，通知 Governance Lead 人工處理                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 監控 Flow 清單

| Flow ID | Flow 名稱 | 觸發方式 | 執行頻率 | 主要功能 |
|:---------|:----------|:---------|:---------|:---------|
| GOV-017 | Guardrail Monitor | Recurrence | 每小時 | 偵測 Flow-only 欄位違規修改並自動回滾 |
| GOV-018 | Compliance Reconciler | Recurrence | 每日 | 對帳 Event Entity 與 Aggregate Entity 一致性 |
| GOV-019 | SLA Monitor | Recurrence | 每日 | 監控 Gate 審批是否超過 SLA |

---

## GOV-017：Guardrail Monitor 實作步驟

### 建立 Cloud Flow

#### 步驟 2.1.1：建立新的 Cloud Flow

1. **導覽路徑**：Power Automate Portal → Solutions → {治理系統 Solution} → New → Automation → Cloud flow → Scheduled
2. **Flow 名稱**：`GOV-017-Guardrail-Monitor`
3. **描述**：`每小時偵測 Flow-only 欄位違規修改並自動回滾`

#### 步驟 2.1.2：設定 Recurrence Trigger

1. **Trigger 設定**：
   - **Frequency**：Hour
   - **Interval**：1
   - **Time zone**：(UTC+08:00) Taipei
   - **Start time**：留空（立即開始）
   - **On these days**：全選（每天執行）
   - **At these hours**：全選（每小時執行）
   - **At these minutes**：0（整點執行）

2. **驗證設定正確**：
   - 點擊 Trigger → Show advanced options
   - 確認 Time zone 為 Taipei

**確認此步驟成功**：Trigger 下方顯示「Recurrence: Every 1 Hour」

---

### 查詢 Dataverse Audit Log（過去 1 小時）

#### 步驟 2.2.1：新增「初始化變數」動作

1. **動作名稱**：Initialize variable - ViolationList
2. **設定**：
   - **Name**：`ViolationList`
   - **Type**：Array
   - **Value**：`[]`

#### 步驟 2.2.2：新增「初始化變數」動作 - 時間範圍

1. **動作名稱**：Initialize variable - CheckStartTime
2. **設定**：
   - **Name**：`CheckStartTime`
   - **Type**：String
   - **Value**：使用 Checkpoint 機制（見下方說明）

> **Checkpoint 機制（取代固定 addHours -1）**：
> 為避免固定時間窗造成偵測盲區（Flow 延遲或失敗重試時），改為讀取上次成功執行時間：
>
> ```
> 讀取 Environment Variable 'GOV017_LastCheckpoint'
>   → 若存在：CheckStartTime = GOV017_LastCheckpoint
>   → 若不存在：CheckStartTime = addHours(utcNow(), -1)（首次執行 fallback）
>
> Flow 成功結束時：
>   → 更新 Environment Variable 'GOV017_LastCheckpoint' = utcNow()
> ```
>
> 此機制確保連續執行之間無偵測缺口，即使 Flow 延遲 30 分鐘執行，也不會遺漏偵測。

#### 步驟 2.2.3：新增「List rows」動作查詢 Audit Log

1. **動作名稱**：List rows - Get Audit Logs
2. **Connector**：Microsoft Dataverse
3. **動作**：List rows
4. **設定**：
   - **Table name**：Audits（系統內建表，Schema name: `audit`）
   - **Select columns**：`createdon,objectid,attributemask,changedata,userid,objecttypecode`
   - **Filter rows**：
     ```
     createdon gt @{variables('CheckStartTime')} and
     _userid_value ne '<Flow-Service-Principal-ID>' and
     (objecttypecode eq 'gov_projectregistry' or objecttypecode eq 'gov_reviewdecisionlog' or objecttypecode eq 'gov_riskassessmenttable')
     ```
   - **Row count**：1000

> **重要**：請將 `<Flow-Service-Principal-ID>` 替換為實際的 Flow Service Principal GUID。

**確認此步驟成功**：執行測試，檢查是否能查詢到 Audit Log 記錄

---

### 定義 Flow-only 欄位清單

#### 步驟 2.3.1：新增「Compose」動作定義欄位清單

1. **動作名稱**：Compose - FlowOnlyFields
2. **Inputs**：
   ```json
   {
       "gov_projectregistry": [
           "gov_currentgate",
           "gov_requeststatus",
           "gov_projectstatus",
           "gov_documentfreezestatus",
           "gov_gate0passeddate",
           "gov_gate1passeddate",
           "gov_gate2passeddate",
           "gov_gate3passeddate",
           "gov_riskacceptancestatus",
           "gov_highestresidualrisklevel",
           "gov_riskowner",
           "gov_executiveapprover",
           "gov_reworkcount",
           "gov_lastreworkdate",
           "gov_riskacceptancedate",
           "createdby",
           "createdon",
           "modifiedby",
           "modifiedon"
       ],
       "gov_riskassessmenttable": [
           "gov_risklevel",
           "gov_riskacceptancestatus",
           "gov_riskacceptedby",
           "gov_riskacceptancedate",
           "gov_residualrisklevel",
           "gov_riskowner",
           "gov_riskownerreviewstatus"
       ],
       "gov_reviewdecisionlog": [
           "gov_reviewid",
           "gov_reviewtype",
           "gov_decision",
           "gov_approvedby",
           "gov_revieweddate",
           "gov_triggerflowrunid",
           "gov_gate1securityreviewstatus",
           "gov_gate1qareviewstatus",
           "gov_gate1governancereviewstatus",
           "gov_gate3riskacceptancestatus",
           "gov_gate3approvalstatus",
           "gov_riskownerreviewstatus",
           "gov_executivereviewstatus"
       ]
   }
   ```

---

### 篩選違規記錄

#### 步驟 2.4.1：新增「Apply to each」迴圈

1. **動作名稱**：Apply to each - Process Audit Records
2. **Select an output from previous steps**：`@{outputs('List_rows_-_Get_Audit_Logs')?['body/value']}`

#### 步驟 2.4.2：在迴圈內新增「Condition」動作

1. **動作名稱**：Condition - Is Flow-only Field
2. **設定條件**：
   - **Condition**：使用運算式
   ```
   @contains(
       outputs('Compose_-_FlowOnlyFields')?[items('Apply_to_each_-_Process_Audit_Records')?['objecttypecode']],
       items('Apply_to_each_-_Process_Audit_Records')?['attributemask']
   )
   ```

#### 步驟 2.4.3：在 If yes 分支新增「Append to array variable」

1. **動作名稱**：Append to array variable - Add to ViolationList
2. **設定**：
   - **Name**：`ViolationList`
   - **Value**：
     ```json
     {
         "AuditId": "@{items('Apply_to_each_-_Process_Audit_Records')?['auditid']}",
         "ViolatedEntity": "@{items('Apply_to_each_-_Process_Audit_Records')?['objecttypecode']}",
         "ViolatedRecord": "@{items('Apply_to_each_-_Process_Audit_Records')?['objectid']}",
         "ViolatedField": "@{items('Apply_to_each_-_Process_Audit_Records')?['attributemask']}",
         "ChangeData": "@{items('Apply_to_each_-_Process_Audit_Records')?['changedata']}",
         "ModifiedBy": "@{items('Apply_to_each_-_Process_Audit_Records')?['_userid_value']}",
         "DetectedDate": "@{utcNow()}"
     }
     ```

**確認此步驟成功**：執行測試，若有違規記錄，ViolationList 應包含違規項目

---

### 處理違規記錄

#### 步驟 2.5.1：新增「Condition」檢查是否有違規

1. **動作名稱**：Condition - Has Violations
2. **設定條件**：
   - **Condition**：`@length(variables('ViolationList'))` is greater than `0`

#### 步驟 2.5.2：在 If yes 分支新增「Apply to each」迴圈

1. **動作名稱**：Apply to each - Process Violations
2. **Select an output from previous steps**：`@{variables('ViolationList')}`

---

### 寫入 Governance Violation Log

#### 步驟 2.6.1：在 Process Violations 迴圈內新增「Add a new row」

1. **動作名稱**：Add a new row - Create Violation Log
2. **Connector**：Microsoft Dataverse
3. **動作**：Add a new row
4. **設定**：
   - **Table name**：Governance Violation Logs（Schema: `gov_governanceviolationlog`）
   - **欄位對應**：
     | 欄位 | 值 |
     |------|---|
     | Violation ID | `@{guid()}` |
     | Violated Entity | `@{items('Apply_to_each_-_Process_Violations')?['ViolatedEntity']}` |
     | Violated Field | `@{items('Apply_to_each_-_Process_Violations')?['ViolatedField']}` |
     | Violated Record | `@{items('Apply_to_each_-_Process_Violations')?['ViolatedRecord']}` |
     | Change Data | `@{items('Apply_to_each_-_Process_Violations')?['ChangeData']}` |
     | Modified By | `@{items('Apply_to_each_-_Process_Violations')?['ModifiedBy']}` |
     | Detected Date | `@{utcNow()}` |
     | Rollback Status | `Pending` |

**確認此步驟成功**：執行測試後，檢查 Governance Violation Log Table 是否新增記錄

---

### 執行自動回滾

#### 步驟 2.7.1：新增「Parse JSON」解析 Change Data

1. **動作名稱**：Parse JSON - Parse ChangeData
2. **Content**：`@{items('Apply_to_each_-_Process_Violations')?['ChangeData']}`
3. **Schema**：
   ```json
   {
       "type": "object",
       "properties": {
           "oldValue": { "type": ["string", "integer", "null"] },
           "newValue": { "type": ["string", "integer", "null"] }
       }
   }
   ```

#### 步驟 2.7.2：新增「Condition」檢查 OldValue 是否可取得

1. **動作名稱**：Condition - Can Rollback
2. **設定條件**：
   - **Condition**：`@body('Parse_JSON_-_Parse_ChangeData')?['oldValue']` is not equal to `null`

#### 步驟 2.7.3：在 If yes 分支新增「Update a row」執行回滾

1. **動作名稱**：Update a row - Rollback Change
2. **Connector**：Microsoft Dataverse
3. **動作**：Update a row
4. **設定**：
   - **Table name**：動態選擇（使用運算式）
     ```
     @{items('Apply_to_each_-_Process_Violations')?['ViolatedEntity']}
     ```
   - **Row ID**：`@{items('Apply_to_each_-_Process_Violations')?['ViolatedRecord']}`
   - **欄位**：動態設定被違規修改的欄位為 OldValue

> **注意**：由於 Dataverse Connector 不支援動態 Table 和 Column，需使用 HTTP with Azure AD Connector 或 Dataverse Web API 實作。

**替代實作方式（使用 HTTP with Azure AD）**：

```http
PATCH https://{org}.api.crm.dynamics.com/api/data/v9.2/{entity-set-name}({record-id})

Headers:
- Authorization: Bearer {token}  ← 使用 Service Principal OAuth Token（見下方認證說明）
- Content-Type: application/json
- OData-MaxVersion: 4.0
- OData-Version: 4.0

Body:
{
    "{field-schema-name}": {oldValue}
}
```

**Dataverse OData Entity Set 名稱對應表**：

| Dataverse Table Schema Name | OData Entity Set Name |
|:--------|:----------------------|
| gov_projectregistry | gov_projectregistries |
| gov_reviewdecisionlog | gov_reviewdecisionlogs |
| gov_riskassessmenttable | gov_riskassessmenttables |
| gov_exceptionwaiverlog | gov_exceptionwaiverlogs |
| gov_documentregister | gov_documentregisters |
| gov_governanceviolationlog | gov_governanceviolationlogs |
| gov_bomregistry | gov_bomregistries |
| gov_counterlist | gov_counterlists |
| gov_sahandoverevent | gov_sahandoverevents |

> **重要**：Dataverse Web API 使用 Entity Set Name（複數形式），不是 Table Schema Name。使用錯誤名稱會導致 404 Not Found。

#### 步驟 2.7.4：更新 Violation Log 的 Rollback Status

**在 If yes（回滾成功）分支**：
1. **動作名稱**：Update a row - Mark Rollback Completed
2. **設定**：
   - **Table name**：Governance Violation Logs
   - **Row ID**：`@{outputs('Add_a_new_row_-_Create_Violation_Log')?['body/gov_governanceviolationlogid']}`
   - **Rollback Status**：`Completed`

**在 If no（無法回滾）分支**：
1. **動作名稱**：Update a row - Mark Manual Required
2. **設定**：
   - **Rollback Status**：`ManualRequired`

---

### 發送違規通知

#### 步驟 2.8.1：新增「Send an email (V2)」動作

1. **動作名稱**：Send an email - Violation Notification
2. **Connector**：Office 365 Outlook
3. **設定**：
   - **To**：`GOV-GovernanceLead@contoso.com; GOV-EngineeringManagement@contoso.com`
   - **Subject**：`【高優先級】偵測到治理違規 - @{items('Apply_to_each_-_Process_Violations')?['ViolatedEntity']}.@{items('Apply_to_each_-_Process_Violations')?['ViolatedField']}`
   - **Importance**：High
   - **Body**：
     ```html
     <h2>治理系統偵測到違規行為</h2>

     <table border="1" cellpadding="5">
         <tr><td><b>違規者</b></td><td>@{items('Apply_to_each_-_Process_Violations')?['ModifiedBy']}</td></tr>
         <tr><td><b>偵測時間</b></td><td>@{utcNow()}</td></tr>
         <tr><td><b>違規 Entity</b></td><td>@{items('Apply_to_each_-_Process_Violations')?['ViolatedEntity']}</td></tr>
         <tr><td><b>違規欄位</b></td><td>@{items('Apply_to_each_-_Process_Violations')?['ViolatedField']}</td></tr>
         <tr><td><b>違規記錄</b></td><td>@{items('Apply_to_each_-_Process_Violations')?['ViolatedRecord']}</td></tr>
         <tr><td><b>變更資料</b></td><td>@{items('Apply_to_each_-_Process_Violations')?['ChangeData']}</td></tr>
         <tr><td><b>回滾狀態</b></td><td>@{if(equals(outputs('Condition_-_Can_Rollback')?['status'], 'Succeeded'), 'Completed - 已自動回滾', 'ManualRequired - 需人工處理')}</td></tr>
     </table>

     <h3>需執行的動作：</h3>
     <ol>
         <li>確認違規原因（誤操作 / 惡意繞過）</li>
         <li>若 RollbackStatus = ManualRequired，請手動回滾並更新狀態</li>
         <li>聯絡違規者，說明治理原則</li>
     </ol>

     <p><a href="{Power App URL}">查看違規記錄</a></p>
     ```

#### 步驟 2.8.2：新增「Post message in a chat or channel」動作

1. **動作名稱**：Post message - Teams Notification
2. **Connector**：Microsoft Teams
3. **設定**：
   - **Post as**：Flow bot
   - **Post in**：Channel
   - **Team**：{治理團隊 Team}
   - **Channel**：{違規通知 Channel}
   - **Message**：同 Email 內容（使用 Adaptive Card 格式）

**確認此步驟成功**：執行測試，確認 Email 與 Teams 訊息皆正確發送

---

### 設定 Try-Catch 錯誤處理

#### 步驟 2.9.1：將所有主要動作放入 Scope

1. **動作名稱**：Scope - Try
2. 將步驟 2.2 至 2.8 的所有動作移至此 Scope 內

#### 步驟 2.9.2：新增 Catch Scope

1. **動作名稱**：Scope - Catch
2. **設定 Configure run after**：
   - 點擊 Scope - Catch → ... → Configure run after
   - 勾選：has failed、has timed out
   - 取消勾選：is successful、is skipped

#### 步驟 2.9.3：在 Catch Scope 內新增錯誤通知

1. **動作名稱**：Send an email - Error Notification
2. **設定**：
   - **To**：`GOV-SystemAdmin@contoso.com`
   - **Subject**：`GOV-017 Guardrail Monitor 執行失敗`
   - **Body**：
     ```
     Flow 執行發生錯誤：

     Flow Run ID: @{workflow()?['run']?['name']}
     錯誤時間: @{utcNow()}

     請檢查 Power Automate Run History 以取得詳細錯誤訊息。
     ```

---

### 儲存並啟用 Flow

1. **儲存**：點擊右上角「Save」
2. **測試**：點擊「Test」→ Manually → Run flow
3. **驗證**：檢查 Flow Run History 是否顯示 Succeeded
4. **啟用**：Flow 預設為開啟狀態，確認 Status = On

**確認此步驟成功**：
- Flow Run History 顯示 Succeeded
- 每小時整點自動執行

---

## GOV-018：Compliance Reconciler 實作步驟

### 建立 Cloud Flow

#### 步驟 3.1.1：建立新的 Scheduled Cloud Flow

1. **導覽路徑**：Power Automate Portal → Solutions → {治理系統 Solution} → New → Automation → Cloud flow → Scheduled
2. **Flow 名稱**：`GOV-018-Compliance-Reconciler`
3. **描述**：`每日對帳 Event Entity 與 Aggregate Entity 狀態一致性`

#### 步驟 3.1.2：設定 Recurrence Trigger

1. **Trigger 設定**：
   - **Frequency**：Day
   - **Interval**：1
   - **Time zone**：(UTC+08:00) Taipei
   - **At these hours**：0（凌晨 00:00 執行）
   - **At these minutes**：0

---

### 對帳一：CurrentGate vs Review Decision Log

#### 步驟 3.2.1：查詢所有 Active 專案

1. **動作名稱**：List rows - Get Active Projects
2. **設定**：
   - **Table name**：Project Registries
   - **Filter rows**：`gov_projectstatus eq 'Active'`
   - **Select columns**：`gov_projectregistryid,gov_requestid,gov_currentgate`

#### 步驟 3.2.2：建立對帳迴圈

1. **動作名稱**：Apply to each - Reconcile Projects
2. **Select an output from previous steps**：`@{outputs('List_rows_-_Get_Active_Projects')?['body/value']}`

#### 步驟 3.2.3：查詢對應的 Review Decision Log

1. **動作名稱**：List rows - Get Latest Approved Gate
2. **設定**：
   - **Table name**：Review Decision Logs
   - **Filter rows**：
     ```
     gov_parentproject eq '@{items('Apply_to_each_-_Reconcile_Projects')?['gov_requestid']}' and
     gov_reviewtype in ('Gate0Request','Gate1Request','Gate2Request','Gate3Request') and
     gov_decision eq 'Approved'
     ```
   - **Order by**：`gov_revieweddate desc`
   - **Row count**：1

#### 步驟 3.2.4：比對 CurrentGate 與 Review Decision Log

1. **動作名稱**：Condition - Gates Match
2. **設定條件**（需依 ReviewType 推導預期的 CurrentGate）：
   - 使用「Compose」動作定義對應關係：
     ```json
     {
         "Gate0Request": "Gate0",
         "Gate1Request": "Gate1",
         "Gate2Request": "Gate2",
         "Gate3Request": "Gate3"
     }
     ```
   - **Condition**：Project.CurrentGate equals ExpectedGate

#### 步驟 3.2.5：若不一致，寫入 Governance Violation Log

**在 If no 分支**：
1. **動作名稱**：Add a new row - Log Compliance Inconsistency
2. **設定**：
   - **Table name**：Governance Violation Logs
   - **欄位對應**：
     | 欄位 | 值 |
     |------|---|
     | Violation ID | `@{guid()}` |
     | Violated Entity | `gov_projectregistry` |
     | Violated Field | `gov_currentgate` |
     | Violated Record | `@{items('Apply_to_each_-_Reconcile_Projects')?['gov_projectregistryid']}` |
     | Expected Value | `@{ExpectedGate from ReviewType}` |
     | Actual Value | `@{items('Apply_to_each_-_Reconcile_Projects')?['gov_currentgate']}` |
     | Violation Type | `ComplianceInconsistency` |
     | Detected Date | `@{utcNow()}` |
     | Rollback Status | `ManualRequired` |

---

### 對帳二：文件連結有效性驗證

#### 步驟 3.3.1：查詢所有已通過 Gate 0 的專案

1. **動作名稱**：List rows - Get Projects with Documents
2. **設定**：
   - **Table name**：Project Registries
   - **Filter rows**：`gov_currentgate ne 'Pending' and gov_projectstatus eq 'Active'`
   - **Select columns**：`gov_projectregistryid,gov_requestid,gov_technicalfeasibilitylink,gov_initialrisklistlink,gov_riskassessmentstrategylink`

#### 步驟 3.3.2：驗證每個文件連結

1. **動作名稱**：Apply to each - Validate Document Links
2. 對於每個文件連結欄位：
   - **動作名稱**：HTTP - Check Document Exists
   - **Method**：HEAD
   - **URI**：`@{items('Apply_to_each')?['gov_technicalfeasibilitylink']}`
   - **Authentication**：
     - **Authentication type**：Active Directory OAuth
     - **Authority**：`https://login.microsoftonline.com/<tenant-id>`
     - **Tenant**：`<tenant-id>`
     - **Audience**：`https://<tenant>.sharepoint.com`
     - **Client ID**：`<Flow-Service-Principal-Client-ID>`
     - **Credential Type**：Secret
     - **Secret**：`<Flow-Service-Principal-Client-Secret>`
   - **驗證**：HTTP Status Code = 200

#### 步驟 3.3.3：若文件不存在，寫入 Violation Log

**若 HTTP Status ≠ 200**：
1. **動作名稱**：Add a new row - Log Missing Document
2. **設定**：
   - **Violated Field**：`{對應的文件連結欄位名稱}`
   - **Expected Value**：`檔案存在（HTTP 200）`
   - **Actual Value**：`檔案不存在（HTTP @{outputs('HTTP_-_Check_Document_Exists')?['statusCode']}）`
   - **Rollback Status**：`ManualRequired`

---

### 發送每日合規報告

#### 步驟 3.4.1：統計今日偵測到的不一致

1. **動作名稱**：List rows - Get Today's Violations
2. **設定**：
   - **Table name**：Governance Violation Logs
   - **Filter rows**：`gov_detecteddate ge @{startOfDay(utcNow())} and gov_violationtype eq 'ComplianceInconsistency'`

#### 步驟 3.4.2：發送每日合規報告 Email

1. **動作名稱**：Send an email - Daily Compliance Report
2. **設定**：
   - **To**：`GOV-GovernanceLead@contoso.com`
   - **Subject**：`每日合規對帳報告 - @{formatDateTime(utcNow(), 'yyyy-MM-dd')}`
   - **Body**：
     ```html
     <h2>每日合規對帳報告</h2>

     <p><b>報告日期</b>：@{formatDateTime(utcNow(), 'yyyy-MM-dd')}</p>
     <p><b>偵測到的不一致數量</b>：@{length(outputs('List_rows_-_Get_Today_Violations')?['body/value'])}</p>

     <h3>不一致清單</h3>
     <table border="1" cellpadding="5">
         <tr>
             <th>專案 ID</th>
             <th>違規欄位</th>
             <th>預期值</th>
             <th>實際值</th>
             <th>狀態</th>
         </tr>
         @{動態產生表格內容}
     </table>

     <p>若有需要人工處理的項目，請至 Governance Violation Log 查看詳細資訊。</p>
     ```

**確認此步驟成功**：
- 每日凌晨 00:00 自動執行
- Governance Lead 收到每日合規報告

---

## GOV-019：SLA Monitor 實作步驟

### 建立 Cloud Flow

1. **Flow 名稱**：`GOV-019-SLA-Monitor`
2. **Trigger**：Recurrence（每日 09:00 UTC+8）

### 定義 SLA 閾值

1. **動作名稱**：Compose - SLA Thresholds
2. **Inputs**：
   ```json
   {
       "Gate0": 2,
       "Gate1": 5,
       "Gate2": 3,
       "Gate3": 5
   }
   ```

> 單位：工作日

### 查詢所有待審批的 Gate 申請

1. **動作名稱**：List rows - Get Pending Requests
2. **設定**：
   - **Table name**：Project Registries
   - **Filter rows**：`gov_requeststatus eq 'Pending' or gov_requeststatus eq 'UnderReview'`
   - **Select columns**：`gov_projectregistryid,gov_requestid,gov_requestedgate,gov_requeststatus,modifiedon`

### 計算等待天數並檢查 SLA

1. **動作名稱**：Apply to each - Check SLA
2. 在迴圈內：
   - 計算等待天數：`@{div(sub(ticks(utcNow()), ticks(items('Apply_to_each')?['modifiedon'])), 864000000000)}`
   - 比對 SLA 閾值

### 發送 SLA 超時通知

若等待天數 > SLA 閾值：
1. **動作名稱**：Send an email - SLA Violation
2. **設定**：
   - **To**：對應的審核群組 + Governance Lead
   - **Subject**：`【SLA 超時警報】Gate @{RequestedGate} 審批已等待 @{WaitingDays} 天`
   - **Importance**：High

---

## 未授權變更偵測機制詳細說明

### 偵測原理

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        未授權變更偵測流程                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. 使用者嘗試修改 Dataverse 資料                                              │
│     └─→ 若使用 Power Apps 表單：被 Field-Level Security 阻擋（直接失敗）       │
│     └─→ 若使用 Web API / Model-Driven App：可能繞過 Field-Level Security      │
│                                                                             │
│  2. Dataverse 自動記錄 Audit Log                                              │
│     ├─→ 記錄：Changed Entity, Changed Field, Old Value, New Value            │
│     ├─→ 記錄：Modified By（修改者 User ID）                                   │
│     └─→ 記錄：Modified On（修改時間）                                         │
│                                                                             │
│  3. GOV-017 每小時查詢 Audit Log                                              │
│     ├─→ 篩選條件：過去 1 小時內                                                │
│     ├─→ 篩選條件：Modified By ≠ Flow Service Principal                       │
│     └─→ 篩選條件：Changed Field ∈ Flow-only 欄位清單                          │
│                                                                             │
│  4. 若偵測到違規                                                              │
│     ├─→ 寫入 Governance Violation Log                                        │
│     ├─→ 嘗試自動回滾（若 Old Value 可取得）                                    │
│     └─→ 發送高優先級通知給 Governance Lead + Engineering Management           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Flow-only 欄位完整清單

| Entity | 欄位名稱（Schema Name） | 顯示名稱 | 說明 |
|:--------|:----------------------|:---------|:------|
| **Project Registry** | gov_currentgate | 當前 Gate | 狀態機核心欄位 |
| | gov_requeststatus | 申請狀態 | 追蹤 Gate 申請進度 |
| | gov_projectstatus | 專案狀態 | Active / Closed / Archived |
| | gov_documentfreezestatus | 文件凍結狀態 | Not Frozen / Frozen |
| | gov_gate0passeddate | Gate 0 通過日期 | |
| | gov_gate1passeddate | Gate 1 通過日期 | |
| | gov_gate2passeddate | Gate 2 通過日期 | |
| | gov_gate3passeddate | Gate 3 通過日期 | |
| | gov_riskacceptancestatus | 風險接受狀態 | |
| | gov_highestresidualrisklevel | 最高殘餘風險等級 | |
| | createdby | 建立者 | 系統欄位 |
| | createdon | 建立日期 | 系統欄位 |
| | modifiedby | 修改者 | 系統欄位 |
| | modifiedon | 修改日期 | 系統欄位 |
| **Review Decision Log** | gov_reviewid | 審核 ID | |
| | gov_reviewtype | 審核類型 | |
| | gov_decision | 決策 | Pending / Approved / Rejected |
| | gov_approvedby | 核准者 | |
| | gov_revieweddate | 審核日期 | |
| | gov_triggerflowrunid | 觸發 Flow Run ID | |
| **Risk Assessment Table** | gov_risklevel | 風險等級 | |
| | gov_riskacceptancestatus | 風險接受狀態 | |
| | gov_riskacceptedby | 風險接受者 | |
| | gov_riskacceptancedate | 風險接受日期 | |

---

## 回滾執行機制詳細說明

### 自動回滾流程

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          自動回滾執行流程                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Step 1：解析 Dataverse Audit Log 的 Change Data                             │
│          ├─→ 取得 Old Value（修改前的值）                                     │
│          └─→ 取得 New Value（修改後的值，即違規的值）                          │
│                                                                             │
│  Step 2：檢查 Old Value 是否可取得                                            │
│          ├─→ 若 Old Value ≠ null → 可自動回滾                                │
│          └─→ 若 Old Value = null → 需人工處理                                │
│                                                                             │
│  Step 3：執行回滾（使用 Dataverse Web API）                                   │
│          ├─→ PATCH https://{org}.api.crm.dynamics.com/api/data/v9.2/{table}({id})
│          ├─→ Body: { "{field}": {oldValue} }                                 │
│          └─→ 使用 Flow Service Principal 身分執行                            │
│                                                                             │
│  Step 4：更新 Governance Violation Log                                        │
│          ├─→ 回滾成功：RollbackStatus = Completed                            │
│          └─→ 回滾失敗：RollbackStatus = ManualRequired                       │
│                                                                             │
│  Step 5：發送回滾結果通知                                                      │
│          ├─→ 回滾成功：「違規修改已自動回滾」                                   │
│          └─→ 回滾失敗：「違規修改無法自動回滾，需人工處理」                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 人工回滾處理程序

當 RollbackStatus = ManualRequired 時，Governance Lead 需執行以下步驟：

1. **查詢 Governance Violation Log**
   - 導覽路徑：Power Apps → Model-Driven App → Governance Violation Log
   - 篩選條件：RollbackStatus = ManualRequired

2. **確認違規內容**
   - 檢視 Violated Entity、Violated Field、Violated Record
   - 檢視 Change Data 取得 Old Value 與 New Value

3. **手動回滾**
   - 導覽路徑：Power Apps → Model-Driven App → {Violated Entity}
   - 找到對應的 Violated Record
   - 將 Violated Field 改回預期值（或 Old Value，若可取得）

4. **更新 Violation Log 狀態**
   - 將 RollbackStatus 更新為 `ManualCompleted`
   - 填寫 Resolution Notes

5. **聯絡違規者**
   - 確認違規原因（誤操作 / 惡意繞過）
   - 說明治理原則與政策

---

## 通知與升級規則

### 通知對象矩陣

| 事件類型 | 通知對象 | 通知方式 | 優先級 |
|:---------|:---------|:---------|:--------|
| Flow-only 欄位違規修改 | Governance Lead + Engineering Management | Email + Teams | High |
| 自動回滾成功 | Governance Lead | Email + Teams | Normal |
| 無法自動回滾（需人工處理） | Governance Lead | Email + Teams | High |
| 合規對帳不一致 | Governance Lead | Email | High |
| 文件連結失效 | Governance Lead + System Architect | Email | Normal |
| SLA 超時（> 閾值） | 對應審核群組 + Governance Lead | Email + Teams | High |
| SLA 即將超時（> 閾值 - 1 天） | 對應審核群組 | Email | Normal |
| GOV-017/018/019 執行失敗 | System Administrator | Email | High |

### 升級規則

| 層級 | 條件 | 升級對象 | 預期回應時間 |
|:------|:------|:---------|:-------------|
| **Level 1** | 首次偵測到違規 | Governance Lead | 4 小時內確認 |
| **Level 2** | 違規未處理超過 24 小時 | Engineering Management | 8 小時內處理 |
| **Level 3** | 違規未處理超過 48 小時 | CTO / Governance Owner | 4 小時內介入 |
| **Level 4** | 同一使用者月內違規 > 2 次 | Engineering Management + HR | 啟動懲處程序 |

### 通知範本

#### 範本 1：違規偵測通知

```
主旨：【高優先級】偵測到治理違規 - {ViolatedEntity}.{ViolatedField}

治理系統偵測到違規行為：

┌────────────────────────────────────────────────────────┐
│ 違規者        │ {ModifiedBy}                           │
│ 偵測時間      │ {DetectedDate}                         │
│ 違規 Entity   │ {ViolatedEntity}                       │
│ 違規欄位      │ {ViolatedField}                        │
│ 違規記錄      │ {ViolatedRecord}                       │
│ 修改前值      │ {OldValue}                             │
│ 修改後值      │ {NewValue}                             │
│ 回滾狀態      │ {RollbackStatus}                       │
└────────────────────────────────────────────────────────┘

需執行的動作：
1. 確認違規原因（誤操作 / 惡意繞過）
2. 若 RollbackStatus = ManualRequired，請手動回滾並更新狀態
3. 聯絡違規者，說明治理原則

查看違規記錄：{Power App URL}
```

#### 範本 2：SLA 超時通知

```
主旨：【SLA 超時警報】Gate {RequestedGate} 審批已等待 {WaitingDays} 天

專案審批 SLA 超時警報：

┌────────────────────────────────────────────────────────┐
│ 專案 ID       │ {RequestID}                            │
│ 專案名稱      │ {Title}                                │
│ 申請 Gate     │ {RequestedGate}                        │
│ 申請日期      │ {SubmittedDate}                        │
│ 等待天數      │ {WaitingDays} 天                        │
│ SLA 閾值      │ {SLAThreshold} 工作日                   │
│ 當前審核者    │ {CurrentApprover}                      │
└────────────────────────────────────────────────────────┘

請儘速完成審批。若有疑問，請聯絡 Governance Function。

查看審批請求：{Approvals App URL}
```

---

## 監控指標與 KPI

### 監控儀表板指標

| 指標名稱 | 計算方式 | 目標值 | 警報閾值 |
|:---------|:---------|:--------|:---------|
| 每月治理違規次數 | COUNT(Governance Violation Log) WHERE DetectedDate in 本月 | ≤ 5 次 | > 10 次 |
| 自動回滾成功率 | Completed / (Completed + ManualRequired) × 100% | ≥ 80% | < 60% |
| 合規對帳不一致數 | COUNT(Violations WHERE ViolationType = ComplianceInconsistency) | 0 | > 0 |
| SLA 超時率 | 超時申請數 / 總申請數 × 100% | ≤ 5% | > 15% |
| 單一使用者月違規次數 | MAX(COUNT(Violations) GROUP BY ModifiedBy) | ≤ 2 次 | > 2 次 |

### Power BI 報表建議

1. **違規趨勢圖**
   - X 軸：月份
   - Y 軸：違規次數
   - 系列：依 ViolatedEntity 區分

2. **違規者排行榜**
   - 顯示 Top 10 違規者
   - 包含違規次數與最近違規日期

3. **回滾狀態分布**
   - 圓餅圖顯示 Completed vs ManualRequired vs ManualCompleted

4. **SLA 達成率趨勢**
   - 依 Gate 類型顯示每月 SLA 達成率

---

## 完成定義（Done Definition）

### GOV-017 Guardrail Monitor 完成定義

- [ ] Flow 已建立於 Solution 內，名稱為 `GOV-017-Guardrail-Monitor`
- [ ] Recurrence Trigger 設定為每小時整點執行（UTC+8）
- [ ] 能正確查詢過去 1 小時的 Dataverse Audit Log
- [ ] 能正確識別 Flow-only 欄位的違規修改
- [ ] 違規記錄正確寫入 Governance Violation Log
- [ ] 自動回滾功能正常運作（Old Value 可取得時）
- [ ] 違規通知正確發送給 Governance Lead + Engineering Management
- [ ] Try-Catch 錯誤處理正常運作
- [ ] Flow 已通過 Anti-Cheating Test（Test Case 17.1, 17.2）

### GOV-018 Compliance Reconciler 完成定義

- [ ] Flow 已建立於 Solution 內，名稱為 `GOV-018-Compliance-Reconciler`
- [ ] Recurrence Trigger 設定為每日 00:00 執行（UTC+8）
- [ ] CurrentGate vs Review Decision Log 對帳功能正常運作
- [ ] 文件連結有效性驗證功能正常運作
- [ ] 不一致記錄正確寫入 Governance Violation Log
- [ ] 每日合規報告正確發送給 Governance Lead
- [ ] Flow 已通過 Compliance Test（Test Case 18.1, 18.2）

### GOV-019 SLA Monitor 完成定義

- [ ] Flow 已建立於 Solution 內，名稱為 `GOV-019-SLA-Monitor`
- [ ] Recurrence Trigger 設定為每日 09:00 執行（UTC+8）
- [ ] SLA 閾值正確設定（Gate 0: 2 天, Gate 1: 5 天, Gate 2: 3 天, Gate 3: 5 天）
- [ ] 超時通知正確發送給對應審核群組
- [ ] Flow 已通過 SLA Test（Test Case 19.1）

### 整體 Guardrail 機制完成定義

- [ ] Field-Level Security Profile 已正確設定所有 Flow-only 欄位
- [ ] Flow Service Principal 具備所有 Flow-only 欄位的寫入權限
- [ ] 人類使用者無法直接修改 Flow-only 欄位（Field-Level Security 阻擋）
- [ ] 繞過 Field-Level Security 的修改能被 GOV-017 偵測並回滾
- [ ] 合規對帳不一致能被 GOV-018 偵測並記錄
- [ ] SLA 超時能被 GOV-019 偵測並通知
- [ ] 所有通知管道（Email + Teams）正常運作
- [ ] 升級規則已設定並能正確觸發
- [ ] Power BI 監控儀表板已建立並顯示正確數據

---

## TODO 清單

以下項目因 SOP 文件資訊不足，需後續補充：

| TODO 項目 | 缺失內容 | 影響步驟 |
|:----------|:---------|:---------|
| TODO-001 | Flow Service Principal 的實際 GUID | 2.2.3 的 Filter rows 條件 |
| TODO-002 | Dataverse Audit Log 的確切 Schema Name | 2.2.3 的 Table name |
| TODO-003 | GOV-018 文件連結驗證的 HTTP 認證方式 | 3.3.2 的 HTTP 動作設定 |
| TODO-004 | Teams 違規通知 Channel 的實際 ID | 2.8.2 的 Teams 設定 |
| TODO-005 | Power BI 報表的詳細設計規格 | 8.2 的儀表板實作 |

---

## 文件修訂記錄

| 版本 | 日期 | 修訂內容 | 修訂者 |
|:------|:------|:---------|:--------|
| 1.0 | 2026-01-29 | 初版建立 | Implementation Team |
| 1.1 | 2026-02-11 | 鑑識修訂：Schema 前綴 cr_→gov_ 全文修正、Flow-only 監控欄位補齊（+8 欄位 + Review Decision Log 全表）、Dataverse Web API URI 修正（含 Entity Set 對應表）、GOV-018 HTTP 認證補齊（Azure AD OAuth）、GOV-017 Checkpoint 機制取代固定時間窗 | Forensic Restructuring |
