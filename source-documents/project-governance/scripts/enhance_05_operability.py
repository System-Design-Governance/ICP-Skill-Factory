#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
05 文件操作可執行性補強工具
為每個 Flow 補充 Trigger、前置條件、I/O 定義、失敗排查指引
"""

import re

# 定義每個 Flow 的補充內容
FLOW_ENHANCEMENTS = {
    'GOV-015': {
        'trigger': """### Trigger 條件

**觸發時機**：被其他 Flow 呼叫時（Child Flow）

**觸發者**：
- GOV-001（專案建立通知）
- GOV-002（Gate 轉換請求通知）
- GOV-003（審批決策通知）
- GOV-005（風險評估通知）
- GOV-017/018（違規偵測通知）

**觸發事件**：
- 專案狀態變更
- 審批決策完成
- 風險評估完成
- 違規事件偵測

**觸發方式**：HTTP POST 呼叫（由 Parent Flow 透過 Connection Reference 呼叫）
""",
        'preconditions': """### 前置條件

**必要條件**：
1. ✅ Service Principal 連線已建立
2. ✅ Teams/Email Connector 連線已建立
3. ✅ Parent Flow 正確傳入 NotificationType、RecipientEmail、Message

**不需要前置資料**：
- 此為 Child Flow，不直接存取 Dataverse
- 所有必要資訊由 Parent Flow 提供

**狀態前置條件**：無（純通知 Flow，不檢查狀態）
""",
        'io_definition': """### Flow I/O 定義

#### Input（來自 Parent Flow）

| 參數名稱 | 資料型別 | 來源 | 必填 | 說明 |
|---------|---------|------|------|------|
| NotificationType | String | Parent Flow | ✓ | 通知類型（Email, Teams, Both） |
| RecipientEmail | String | Parent Flow | ✓ | 收件人 Email 地址 |
| RecipientName | String | Parent Flow | ✗ | 收件人姓名（可選） |
| Subject | String | Parent Flow | ✓ | 通知主旨 |
| Message | String | Parent Flow | ✓ | 通知內容（支援 HTML） |
| Priority | String | Parent Flow | ✗ | 優先級（High/Normal/Low），預設 Normal |

#### Output（無 Dataverse 寫入）

| 輸出項目 | 型別 | 目標 | 說明 |
|---------|------|------|------|
| StatusCode | Number | 回傳給 Parent Flow | 200 = 成功，500 = 失敗 |
| ErrorMessage | String | 回傳給 Parent Flow | 失敗時的錯誤訊息 |

**無 Dataverse 寫入操作**（純通知 Flow）
""",
        'troubleshooting': """### 常見失敗情境與排查指引

#### 情境 1：Email 發送失敗

**錯誤訊息**：`Office365Outlook.SendEmailV2 failed: Unauthorized`

**可能原因**：
- Service Principal 的 Email Connector 權限不足
- 收件人 Email 格式錯誤

**排查步驟**：
1. 檢查 Service Principal 是否有 Mail.Send 權限
2. 驗證 RecipientEmail 格式（必須為有效 Email）
3. 檢查 Connection Reference 是否正確綁定

**解決方案**：
```
修正 RecipientEmail 格式
或重新授權 Email Connector
```

---

#### 情境 2：Teams 訊息發送失敗

**錯誤訊息**：`Teams.PostMessage failed: Bot not found`

**可能原因**：
- Teams Connector 未正確設定
- 收件人無 Teams 帳號

**排查步驟**：
1. 確認 Teams Connector 已授權
2. 驗證收件人有 Teams 帳號
3. 檢查 Channel/Chat ID 是否正確

**解決方案**：
```
改用 Email 通知
或確認 Teams 設定
```

---

#### 情境 3：通知內容為空

**錯誤訊息**：無錯誤，但收到空白通知

**可能原因**：
- Parent Flow 未正確傳入 Message
- HTML 格式錯誤

**排查步驟**：
1. 檢查 Parent Flow 的 Message 欄位
2. 驗證 HTML 語法
3. 檢查動態內容是否正確展開

**解決方案**：
```
修正 Parent Flow 的 Message 組合邏輯
```
"""
    },

    'GOV-013': {
        'trigger': """### Trigger 條件

**觸發時機**：被其他 Flow 呼叫時（Child Flow）

**觸發者**：
- GOV-005（風險評估時計算風險等級）
- GOV-006（風險重新評估時）

**觸發事件**：
- 風險評估提交（Likelihood + Impact 輸入完成）
- 緩解措施更新（需重新計算殘餘風險）

**觸發方式**：HTTP POST 呼叫

**呼叫時機**：Parent Flow 在寫入 Dataverse 前，先計算 RiskLevel
""",
        'preconditions': """### 前置條件

**必要條件**：
1. ✅ Parent Flow 正確傳入 Likelihood 和 Impact 值
2. ✅ Likelihood 和 Impact 必須為有效的 OptionSet 值（100000000~100000004）

**輸入值域檢查**：
- Likelihood: 100000000 (VeryLow) ~ 100000004 (VeryHigh)
- Impact: 100000000 (Negligible) ~ 100000004 (Critical)

**不需要前置資料**：此為純計算 Flow，不存取 Dataverse

**狀態前置條件**：無
""",
        'io_definition': """### Flow I/O 定義

#### Input（來自 Parent Flow）

| 參數名稱 | 資料型別 | 來源 | 必填 | 有效值範圍 |
|---------|---------|------|------|-----------|
| Likelihood | Number | Parent Flow | ✓ | 100000000~100000004 |
| Impact | Number | Parent Flow | ✓ | 100000000~100000004 |

**OptionSet 值對照**：
- 100000000: VeryLow / Negligible
- 100000001: Low / Minor
- 100000002: Medium / Moderate
- 100000003: High / Major
- 100000004: VeryHigh / Critical

#### Output（回傳給 Parent Flow）

| 輸出項目 | 型別 | 值範圍 | 說明 |
|---------|------|--------|------|
| RiskLevel | Number | 100000000~100000002 | 計算出的風險等級 |
| RiskLevelLabel | String | Low/Medium/High | 風險等級文字描述 |

**RiskLevel 對照**：
- 100000000: Low（低風險）
- 100000001: Medium（中等風險）
- 100000002: High（高風險）

**無 Dataverse 寫入操作**（由 Parent Flow 負責寫入）
""",
        'troubleshooting': """### 常見失敗情境與排查指引

#### 情境 1：計算結果錯誤

**症狀**：風險等級與預期不符

**可能原因**：
- Likelihood 或 Impact 值錯誤
- 風險矩陣邏輯錯誤

**排查步驟**：
1. 檢查 Input 的 Likelihood 和 Impact 值
2. 驗證風險矩陣計算邏輯（見步驟 4-11）
3. 確認 Switch 條件的 OptionSet 值正確

**解決方案**：
```
根據風險矩陣手動驗證：
VeryHigh Impact + High Likelihood = High Risk (100000002)
Low Impact + Low Likelihood = Low Risk (100000000)
```

---

#### 情境 2：無效的 OptionSet 值

**錯誤訊息**：Switch 條件無匹配，返回預設值

**可能原因**：
- Parent Flow 傳入的值不在有效範圍
- OptionSet 值使用錯誤（如使用 900000000 系列）

**排查步驟**：
1. 檢查 Parent Flow 的 Likelihood/Impact 來源
2. 確認使用 100000000 系列值（非 900000000）
3. 驗證 Dataverse Choice Set 定義

**解決方案**：
```
修正 Parent Flow 的 OptionSet 值映射
確保使用 02 文件定義的值
```

---

#### 情境 3：Parent Flow 未接收到結果

**症狀**：Parent Flow 的 RiskLevel 欄位為空

**可能原因**：
- Child Flow 回傳格式錯誤
- Parent Flow 未正確讀取 Response

**排查步驟**：
1. 檢查 Child Flow 的 Response 步驟
2. 驗證 Parent Flow 的接收邏輯
3. 確認 JSON 格式正確

**解決方案**：
```
Parent Flow 使用：
outputs('Invoke_Risk_Calculator')?['body']?['RiskLevel']
```
"""
    },

    'GOV-001': {
        'trigger': """### Trigger 條件

**觸發時機**：使用者透過 Power Apps 提交專案建立表單時

**觸發者**：
- System Architect（系統架構師）
- 透過 Power Apps「專案建立表單」提交

**觸發事件**：
- Power Apps 呼叫此 Flow（使用 PowerApps.Run 按鈕）
- 或透過 HTTP Request 觸發（若使用 Web Form）

**觸發方式**：
- **方式 A**（推薦）：PowerApps Trigger（當使用者點擊表單「提交」按鈕時）
- **方式 B**：HTTP Request Trigger（若使用外部整合）

**不會自動觸發**：此 Flow 必須由使用者主動觸發
""",
        'preconditions': """### 前置條件

**Dataverse 前置資料**：
1. ✅ `gov_counterlist` 資料表已建立
2. ✅ Counter List 必須有一筆記錄：
   - `gov_countername = 'ProjectRequest'`
   - `gov_prefix = 'DR'`
   - `gov_currentyear = 當年（如 2026）`
   - `gov_currentcounter = 初始值（如 0）`

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
""",
        'io_definition': """### Flow I/O 定義

#### Input（來自 Power Apps 或 HTTP Request）

| 參數名稱 | 資料型別 | 來源 | 必填 | 對應 Dataverse 欄位 |
|---------|---------|------|------|-------------------|
| Title | String (Max: 200) | Power Apps | ✓ | gov_title |
| ProjectType | Choice | Power Apps | ✓ | gov_projecttype |
| TargetSL | Choice | Power Apps | ✓ | gov_targetsl |
| SystemArchitect | Lookup (User) | Power Apps | ✓ | gov_systemarchitect |
| ProjectManager | Lookup (User) | Power Apps | ✗ | gov_projectmanager |
| ProjectDescription | String (Max: 2000) | Power Apps | ✗ | gov_projectdescription |

**ProjectType 有效值**：
- 100000000: NewSystem
- 100000001: MajorArchChange
- 100000002: SecurityCritical
- 100000003: ComplianceChange

**TargetSL 有效值**：
- 100000000: SL1
- 100000001: SL2
- 100000002: SL3
- 100000003: SL4

#### Output（寫入 Dataverse）

**主要寫入目標**：`gov_projectregistry`

| 欄位名稱 | 值來源 | 設定方式 | 說明 |
|---------|--------|---------|------|
| gov_requestid | Flow 產生 | concat('DR-', formatDateTime(utcNow(), 'yyyy'), '-', substring(guid(), 0, 8)) | 主鍵（如 DR-2026-a1b2c3d4） |
| gov_title | Input | 直接使用 | 專案名稱 |
| gov_projecttype | Input | 直接使用 | 專案類型 |
| gov_targetsl | Input | 直接使用 | 目標安全等級 |
| gov_systemarchitect | Input | 直接使用 | 系統架構師 |
| gov_projectmanager | Input | 直接使用（可空） | 專案經理 |
| gov_projectdescription | Input | 直接使用（可空） | 專案描述 |
| gov_currentgate | Flow 設定 | 100000000 (Pending) | PreGate0 狀態 |
| gov_requeststatus | Flow 設定 | 100000000 (None) | 尚未提交審批 |
| gov_projectstatus | Flow 設定 | 100000000 (Active) | 專案已啟動 |
| gov_documentfreezestatus | Flow 設定 | 100000000 (NotFrozen) | 文件未凍結 |
| gov_sharepointfolderurl | Flow 產生 | SharePoint 資料夾 URL | 專案文件夾連結 |

**次要寫入目標**：`gov_reviewdecisionlog`（一筆建立事件記錄）

| 欄位名稱 | 值來源 | 說明 |
|---------|--------|------|
| gov_reviewid | Flow 產生 | concat(RequestID, '-CREATE') |
| gov_reviewtype | Flow 設定 | 100000000 (ProjectCreation) |
| gov_parentproject | 上一步建立的專案 | Lookup 至 gov_projectregistry |
| gov_submittedby | 當前使用者 | User().Email |
| gov_submitteddate | Flow 設定 | utcNow() |
| gov_decision | Flow 設定 | 100000003 (Executed) |

#### SharePoint Output

**建立資料夾**：`/Projects/{RequestID}-{Title}`

**子資料夾結構**：
- 00-Gate0
- 01-Gate1
- 02-Gate2
- 03-Gate3
- 99-Archive
"""
    }
}

def enhance_flow_section(content: str, flow_id: str, enhancement: dict) -> str:
    """為指定 Flow 的章節插入補強內容"""

    # 找到該 Flow 的章節起始位置
    flow_pattern = rf'(## {flow_id}：[^\n]+\n+### 基本資訊)'

    match = re.search(flow_pattern, content)
    if not match:
        print(f"  [!] Flow {flow_id} 章節未找到，跳過")
        return content

    # 在「基本資訊」之後插入補強內容
    insert_pos = match.end()

    # 組合補強內容
    enhancement_text = "\n\n"

    if 'trigger' in enhancement:
        enhancement_text += enhancement['trigger'] + "\n"

    if 'preconditions' in enhancement:
        enhancement_text += enhancement['preconditions'] + "\n"

    if 'io_definition' in enhancement:
        enhancement_text += enhancement['io_definition'] + "\n"

    # 在「建立步驟」章節之前插入（通常在 Input Schema 之後）
    # 但「常見失敗情境」應該放在「驗收測試」之後

    # 將補強內容插入
    content = content[:insert_pos] + enhancement_text + content[insert_pos:]

    return content

def add_troubleshooting_section(content: str, flow_id: str, troubleshooting: str) -> str:
    """在驗收測試之後新增失敗排查章節"""

    # 找到該 Flow 的驗收測試章節結束位置
    # 通常是下一個 ## 章節之前

    flow_section_pattern = rf'(## {flow_id}：[^\n]+.*?)(## \w+-\d+：|\Z)'
    match = re.search(flow_section_pattern, content, re.DOTALL)

    if not match:
        print(f"  [!] Flow {flow_id} 整體章節未找到，跳過失敗排查")
        return content

    flow_content = match.group(1)
    next_section_start = match.start(2)

    # 在該 Flow 章節的最後（下一個章節之前）插入
    insert_content = "\n" + troubleshooting + "\n"

    content = content[:next_section_start] + insert_content + content[next_section_start:]

    return content

def add_general_troubleshooting_chapter(content: str) -> str:
    """在文件末尾（附錄 D 之前）新增通用失敗排查章節"""

    general_troubleshooting = """

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
1. 使用錯誤的 OptionSet 值系列（900000000 vs 100000000）
2. OptionSet 值不存在於 Dataverse 定義中

**排查步驟**：
1. 檢查 Flow 中使用的 OptionSet 值
2. 對照 02-dataverse-data-model-and-security.md 的定義
3. 確認使用 100000000 系列（非 900000000）

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
HTTP 500: Internal Server Error
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
確認 Value 為 100000000 系列
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
"""

    # 在附錄 D 之前插入
    appendix_d_pattern = r'(---\n\n## 附錄 D：專案狀態語意對照表)'
    match = re.search(appendix_d_pattern, content)

    if match:
        insert_pos = match.start()
        content = content[:insert_pos] + general_troubleshooting + "\n\n" + content[insert_pos:]
    else:
        # 如果找不到附錄 D，就放在文件最末
        content += general_troubleshooting

    return content

def main():
    file_path = r"c:\Users\victo\OneDrive\文件\開發\治理系統\System-Design-Governance\docs\power-platform-governance\zh-TW\05-core-flows-implementation-runbook.md"

    print("="*80)
    print("05 Document Operability Enhancement Tool")
    print("="*80)
    print()

    # 讀取文件
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("[1/3] Enhancing Flow sections...")

    # 為每個 Flow 新增補強內容
    for flow_id, enhancement in FLOW_ENHANCEMENTS.items():
        print(f"  - Processing {flow_id}...")
        content = enhance_flow_section(content, flow_id, enhancement)

        if 'troubleshooting' in enhancement:
            content = add_troubleshooting_section(content, flow_id, enhancement['troubleshooting'])

    print("\n[2/3] Adding general troubleshooting chapter...")
    content = add_general_troubleshooting_chapter(content)

    print("\n[3/3] Writing enhanced document...")

    # 寫回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print()
    print("="*80)
    print("[OK] Operability enhancement completed!")
    print("="*80)
    print()
    print("Enhanced sections:")
    print(f"  - Added Trigger/Preconditions/I/O for {len(FLOW_ENHANCEMENTS)} Flows")
    print(f"  - Added troubleshooting guides for {len(FLOW_ENHANCEMENTS)} Flows")
    print(f"  - Added general troubleshooting chapter (7 common scenarios)")
    print()

if __name__ == "__main__":
    main()
