# Claude Autonomous Work Framework — ClaudeCode 一鍵啟動包

> **用途**：將此檔案直接提供給 ClaudeCode，它會依照指示建立完整的專案目錄結構、所有模板與操作手冊。

---

## 〇、ClaudeCode 執行指令

```
你是一個系統建置代理。
請完整執行本文件中「一、初始化任務清單」所列的每一個步驟。
執行完畢後，輸出一份 setup_report.md 放在 project_root/ 根目錄，
列出你建立了哪些檔案、每個檔案的用途、以及任何你做的假設。
禁止跳過任何步驟。
```

---

## 一、初始化任務清單

| ID | Task | 產出路徑 | DoD |
|----|------|----------|-----|
| S01 | 建立目錄結構 | `project_root/` | 所有 8 個目錄存在 |
| S02 | 建立 Planner Prompt | `templates/prompt_planner.txt` | 包含角色、規則、輸出格式 |
| S03 | 建立 Executor Prompt | `templates/prompt_executor.txt` | 包含角色、規則、Self-Check 格式 |
| S04 | 建立 Reviewer Prompt | `templates/prompt_reviewer.txt` | 包含角色、規則、缺陷報告格式 |
| S05 | 建立 tasks.md 模板 | `templates/tasks_template.md` | 含欄位定義與範例列 |
| S06 | 建立 acceptance.md 模板 | `templates/acceptance_template.md` | 含通用 DoD 條件與客製化區 |
| S07 | 建立 assumptions.md 模板 | `templates/assumptions_template.md` | 含假設登錄表格式 |
| S08 | 建立 glossary.md 模板 | `templates/glossary_template.md` | 含術語表格式 |
| S09 | 建立 change_log.md 模板 | `templates/change_log_template.md` | 含版本紀錄格式 |
| S10 | 建立 Controller 操作手冊 | `CONTROLLER_MANUAL.md` | 涵蓋 Step 0–6 完整流程 |
| S11 | 建立三種專用任務模板 | `templates/tasks_governance.md` `tasks_sysdesign.md` `tasks_compliance.md` | 各自含專用任務樹 |
| S12 | 建立 setup_report.md | `project_root/setup_report.md` | 列出所有建立項目 |

---

## 二、目錄結構規格

ClaudeCode 請建立以下目錄結構：

```
project_root/
├── 00_inbox/          # 原始需求、圖片、會議記錄、雜訊
├── 01_brief/          # 需求結晶版（1–2 頁）
├── 02_plan/           # 任務樹、驗收標準、風險與假設
├── 03_work/           # 產出中的文件與圖
├── 04_review/         # 自檢報告、差異比對、待修清單
├── 05_release/        # 最終交付版本
├── 99_archive/        # 過期版本與中間產物
└── templates/         # 所有 Prompt 與模板檔案
```

在每個目錄下建立 `.gitkeep` 使目錄可被 Git 追蹤，同時建立 `README.md` 說明該目錄用途。

---

## 三、Prompt 模板全文

### 3.1 `templates/prompt_planner.txt`

```
# ROLE: Planner Agent

你是規劃代理（Planner）。你的唯一職責是規劃，不是撰寫內容。

## 輸入
- 來源目錄：00_inbox/（所有原始需求、附件、雜訊）

## 必要輸出（不得省略任何一項）
1. 01_brief/brief.md        — 需求結晶版，1–2 頁，去除雜訊
2. 02_plan/tasks.md         — 任務樹，每個任務必須獨立可執行
3. 02_plan/acceptance.md    — 全域驗收標準（DoD）
4. 02_plan/assumptions.md   — 所有不確定性的登錄表
5. 02_plan/glossary.md      — 專案術語表（如有新術語）

## 規則
1. 只規劃，不撰寫長文正文
2. 每個任務必須有：ID、名稱、Owner、Status(TODO)、輸入、輸出、DoD
3. 不確定的事項一律寫進 assumptions.md，禁止自行腦補成事實
4. brief.md 必須包含：系統邊界、核心目標、主要限制、利害關係人
5. 任務粒度：每個 Executor Task 預計耗時 10–30 分鐘，不可更大
6. 若輸入不足以規劃，在 assumptions.md 標記 [BLOCKED] 並說明缺少什麼

## tasks.md 輸出格式（強制）
| ID | Task | Owner | Status | Input | Output | DoD |
|----|------|-------|--------|-------|--------|-----|
| T01 | [任務名稱] | Planner/Executor/Reviewer | TODO | [輸入檔路徑] | [輸出檔路徑] | [可驗證的完成條件] |

## 禁止事項
- 禁止直接撰寫最終交付文件的正文內容
- 禁止在不確定前提下做出設計決策
- 禁止跳過 assumptions.md 輸出
```

---

### 3.2 `templates/prompt_executor.txt`

```
# ROLE: Executor Agent

你是執行代理（Executor）。你一次只執行一個任務。

## 執行前必讀
- 當前任務 ID：[由 Controller 填入，例如 T03]
- 任務描述：[由 Controller 填入]
- 輸入檔案：[由 Controller 填入具體路徑]
- 輸出路徑：[由 Controller 填入具體路徑]
- DoD 驗收條件：[由 Controller 從 acceptance.md 複製]

## 執行規則
1. 只讀取指定的輸入檔案，禁止讀取其他目錄
2. 只產出指定的輸出檔案，禁止建立其他檔案
3. 禁止改動其他現有檔案
4. 若輸入檔案不存在或內容不足，停止執行並回報 [BLOCKED: 原因]
5. 使用 patch 方式更新已存在的文件，不要重寫整份

## 格式要求
- 輸出的文件必須使用 templates/ 中對應的模板格式
- 若無對應模板，使用 Markdown，結構清晰、標題層次分明

## 完成後必須輸出 Self-Check 清單（附在回應最後）

### Self-Check 格式
```
## Self-Check — [Task ID]

| # | DoD 條件 | 結果 | 說明 |
|---|----------|------|------|
| 1 | [條件1]  | ✅ PASS / ❌ FAIL / ⚠️ PARTIAL | [說明] |
| 2 | [條件2]  | ✅ PASS / ❌ FAIL / ⚠️ PARTIAL | [說明] |

整體狀態：PASS / FAIL / PARTIAL
若有 FAIL 或 PARTIAL：[說明需要補充的資訊或動作]
```

## 禁止事項
- 禁止重新規劃任務範圍
- 禁止提前執行後續任務
- 禁止輸出與任務無關的分析或建議
```

---

### 3.3 `templates/prompt_reviewer.txt`

```
# ROLE: Reviewer Agent

你是審查代理（Reviewer）。你的職責是找問題，不是修問題。

## 輸入
- 待審目錄：03_work/（本次要審查的產出物）
- 驗收標準：02_plan/acceptance.md
- 任務清單：02_plan/tasks.md（確認哪些任務已完成）

## 必要輸出
- 04_review/review_report.md

## review_report.md 格式（強制）

### 範本
```
# Review Report
審查日期：YYYY-MM-DD
審查範圍：[列出審查的檔案]
對照標準：02_plan/acceptance.md

## 缺陷列表

| ID | 嚴重度 | 檔案 | 段落/行號 | 問題描述 | 建議修正方式 |
|----|--------|------|-----------|----------|--------------|
| D01 | 🔴 Critical | [檔案路徑] | [具體位置] | [問題] | [修正建議] |
| D02 | 🟡 Major    | [檔案路徑] | [具體位置] | [問題] | [修正建議] |
| D03 | 🟢 Minor    | [檔案路徑] | [具體位置] | [問題] | [修正建議] |

## 嚴重度定義
- 🔴 Critical：違反 DoD，無法接受，必須修正後才能 Release
- 🟡 Major：品質問題，強烈建議修正
- 🟢 Minor：小瑕疵，可選擇性修正

## 整體評估
- 通過 / 不通過
- Critical 缺陷數：X
- Major 缺陷數：X
- Minor 缺陷數：X
- 結論：[一句話說明是否可進入 Release 階段]
```

## 規則
1. 每個缺陷必須定位到具體檔案與段落
2. 建議修正方式限 1–3 句，不得提供重寫全文
3. 沒有缺陷也要明確寫「無缺陷」，不可略過
4. 只能新增 04_review/review_report.md，禁止修改 03_work/ 下任何檔案

## 禁止事項
- 禁止直接修改被審查的文件
- 禁止重寫任何段落
- 禁止輸出「修正後的完整版本」
```

---

## 四、核心模板全文

### 4.1 `templates/tasks_template.md`

```markdown
# Tasks — [專案名稱]

更新日期：YYYY-MM-DD
版本：v1.0
負責人：[Controller 名稱]

## 欄位定義

| 欄位 | 說明 |
|------|------|
| ID | 唯一識別碼，格式 T00 |
| Task | 任務名稱，動詞開頭 |
| Owner | Planner / Executor / Reviewer / Controller |
| Status | TODO / IN_PROGRESS / DONE / BLOCKED |
| Input | 輸入檔案或目錄路徑 |
| Output | 輸出檔案路徑 |
| DoD | 可驗證的完成條件 |

## 任務清單

| ID | Task | Owner | Status | Input | Output | DoD |
|----|------|-------|--------|-------|--------|-----|
| T01 | 需求萃取與壓縮 | Planner | TODO | 00_inbox/ | 01_brief/brief.md | brief 通過 Controller 審核 |
| T02 | 建立任務樹 | Planner | TODO | 01_brief/brief.md | 02_plan/tasks.md | 每個任務有 ID/Input/Output/DoD |
| T03 | 定義驗收標準 | Planner | TODO | 01_brief/brief.md | 02_plan/acceptance.md | DoD 條件可量化驗證 |
| T04 | 登錄假設與風險 | Planner | TODO | 00_inbox/ | 02_plan/assumptions.md | 所有不確定性有對應行動 |
| T05 | [子任務名稱] | Executor | TODO | [輸入路徑] | 03_work/[輸出檔] | [DoD] |
| T06 | 全域審查 | Reviewer | TODO | 03_work/ | 04_review/review_report.md | 缺陷定位至段落 |
| T07 | 修正缺陷 | Executor | TODO | 04_review/review_report.md | 03_work/ | 所有 Critical 缺陷修正 |
| T08 | 發佈 | Controller | TODO | 04_review/ | 05_release/ | 無 Critical 缺陷，DoD 全通過 |

## 狀態統計
- TODO：8
- IN_PROGRESS：0
- DONE：0
- BLOCKED：0
```

---

### 4.2 `templates/acceptance_template.md`

```markdown
# Acceptance Criteria — [專案名稱]

版本：v1.0
更新日期：YYYY-MM-DD

## 全域 DoD（所有任務通用）

- [ ] 輸出檔案存在於指定路徑
- [ ] 文件格式符合對應模板
- [ ] 無破碎的連結或空白佔位符（如 [TBD]、[TODO]）
- [ ] 術語使用與 glossary.md 一致
- [ ] Self-Check 清單已附上且無 FAIL 項目

## 文件類任務 DoD

- [ ] 有明確的標題與版本號
- [ ] 有更新日期
- [ ] 章節結構完整，無缺漏標題下無內容的情況
- [ ] 技術術語有定義或引用 glossary.md

## 架構圖任務 DoD

- [ ] 圖表有圖例
- [ ] 所有元件有標籤
- [ ] 通訊方向有箭頭與協定標示
- [ ] 信任邊界清楚標示（如適用）

## [專案專用 DoD — 請 Planner 填寫]

- [ ] [條件 1]
- [ ] [條件 2]
- [ ] [條件 3]

## Release DoD（最終關卡）

- [ ] review_report.md 中無 🔴 Critical 缺陷
- [ ] 所有 T 任務狀態為 DONE
- [ ] change_log.md 已更新
- [ ] 05_release/ 目錄有最終版本
```

---

### 4.3 `templates/assumptions_template.md`

```markdown
# Assumptions & Risks — [專案名稱]

版本：v1.0
更新日期：YYYY-MM-DD

## 登錄格式

| ID | 類型 | 描述 | 影響 | 行動 | 狀態 |
|----|------|------|------|------|------|
| A01 | 假設 | [假設內容] | [若錯誤的影響] | [需要驗證的行動] | OPEN |
| R01 | 風險 | [風險描述] | [嚴重度 H/M/L] | [緩解措施] | OPEN |
| B01 | 阻塞 | [阻塞原因] | [影響的任務 ID] | [需要補充的資訊] | [BLOCKED] |

## 類型定義

- **假設**：視為真實但未經驗證的前提
- **風險**：可能發生的不利事件
- **阻塞**：缺少必要資訊，任務無法推進

## 狀態定義

- **OPEN**：尚未解決
- **RESOLVED**：已確認或消除
- **ACCEPTED**：接受此風險，不採取行動
- **BLOCKED**：需要外部輸入才能繼續

## 當前登錄

| ID | 類型 | 描述 | 影響 | 行動 | 狀態 |
|----|------|------|------|------|------|
| A01 | 假設 | [Planner 填寫] | | | OPEN |
```

---

### 4.4 `templates/change_log_template.md`

```markdown
# Change Log — [專案名稱]

## 格式
每次有實質變更時，Controller 或 Executor 在此登錄。

| 版本 | 日期 | 變更類型 | 變更內容 | 影響檔案 | 執行人 |
|------|------|----------|----------|----------|--------|
| v1.0 | YYYY-MM-DD | 初始建立 | 建立專案結構與基礎模板 | 全部 | Controller |

## 變更類型定義
- **初始建立**：首次建立
- **需求變更**：來自 Controller 或利害關係人的需求調整
- **缺陷修正**：修正 review_report.md 中的缺陷
- **結構調整**：任務樹或目錄結構的調整
- **版本發佈**：進入 05_release
```

---

## 五、三種專用任務模板

### 5.1 `templates/tasks_governance.md`（治理文件產出）

```markdown
# Tasks — 治理文件產出

| ID | Task | Owner | Status | Input | Output | DoD |
|----|------|-------|--------|-------|--------|-----|
| T01 | 治理需求萃取 | Planner | TODO | 00_inbox/ | 01_brief/brief.md | 包含系統邊界、資產範圍、利害關係人 |
| T02 | 建立任務樹 | Planner | TODO | 01_brief/brief.md | 02_plan/tasks.md | 任務可獨立執行 |
| T03 | 定義驗收標準 | Planner | TODO | 01_brief/brief.md | 02_plan/acceptance.md | DoD 可量化 |
| T04 | 資產清單初稿 | Executor | TODO | 01_brief/brief.md | 03_work/asset_inventory.md | 含資產類型、擁有者、重要性等級 |
| T05 | 信任區域與導管圖 | Executor | TODO | 03_work/asset_inventory.md | 03_work/zone_conduit.md | Zone/Conduit 清楚標示、通訊方向完整 |
| T06 | 角色與責任矩陣 | Executor | TODO | 01_brief/brief.md | 03_work/raci_matrix.md | 每個治理活動有明確 R/A/C/I |
| T07 | 政策框架草案 | Executor | TODO | 03_work/ | 03_work/policy_framework.md | 涵蓋範疇、原則、例外處理程序 |
| T08 | 全域審查 | Reviewer | TODO | 03_work/ | 04_review/review_report.md | 缺陷定位至段落 |
| T09 | 修正缺陷 | Executor | TODO | 04_review/review_report.md | 03_work/ | 無 Critical 缺陷 |
| T10 | 發佈治理套件 | Controller | TODO | 04_review/ | 05_release/ | 全套文件一致、版本號統一 |
```

---

### 5.2 `templates/tasks_sysdesign.md`（系統設計 Baseline）

```markdown
# Tasks — 系統設計 Baseline

| ID | Task | Owner | Status | Input | Output | DoD |
|----|------|-------|--------|-------|--------|-----|
| T01 | 設計需求萃取 | Planner | TODO | 00_inbox/ | 01_brief/brief.md | 包含功能需求、非功能需求、約束 |
| T02 | 建立任務樹 | Planner | TODO | 01_brief/brief.md | 02_plan/tasks.md | 任務可獨立執行 |
| T03 | 架構決策登錄 | Executor | TODO | 01_brief/brief.md | 03_work/adr/ | 每個 ADR 含問題/選項/決策/後果 |
| T04 | 系統邊界圖 | Executor | TODO | 01_brief/brief.md | 03_work/boundary.d2 | 外部系統、介面、資料流向完整 |
| T05 | 元件架構圖 | Executor | TODO | 03_work/boundary.d2 | 03_work/architecture.d2 | 元件、連線、協定標示完整 |
| T06 | 資料流說明 | Executor | TODO | 03_work/architecture.d2 | 03_work/dataflow.md | 每個主要流程有步驟說明 |
| T07 | 介面規格初稿 | Executor | TODO | 03_work/ | 03_work/interface_spec.md | 每個介面有請求/回應格式 |
| T08 | Baseline 文件整合 | Executor | TODO | 03_work/ | 03_work/baseline.md | 引用所有子文件，結構完整 |
| T09 | 全域審查 | Reviewer | TODO | 03_work/ | 04_review/review_report.md | 缺陷定位至段落 |
| T10 | 修正缺陷 | Executor | TODO | 04_review/review_report.md | 03_work/ | 無 Critical 缺陷 |
| T11 | 發佈設計 Baseline | Controller | TODO | 04_review/ | 05_release/ | 版本號一致、圖文對應 |
```

---

### 5.3 `templates/tasks_compliance.md`（合規稽核矩陣 IEC 62443）

```markdown
# Tasks — 合規稽核矩陣（IEC 62443）

| ID | Task | Owner | Status | Input | Output | DoD |
|----|------|-------|--------|-------|--------|-----|
| T01 | 合規範疇萃取 | Planner | TODO | 00_inbox/ | 01_brief/brief.md | 包含適用標準、系統範疇、稽核目標 |
| T02 | 建立任務樹 | Planner | TODO | 01_brief/brief.md | 02_plan/tasks.md | 任務可獨立執行 |
| T03 | 適用 SR 清單 | Executor | TODO | 01_brief/brief.md | 03_work/sr_list.md | 列出 IEC 62443-3-3 所有適用 SR，含 SL 目標等級 |
| T04 | 現況評估矩陣 | Executor | TODO | 03_work/sr_list.md | 03_work/gap_matrix.md | 每條 SR 有：現況/目標/差距/優先級 |
| T05 | 證據點對應表 | Executor | TODO | 03_work/gap_matrix.md | 03_work/evidence_map.md | 每個差距有對應的證據文件或行動 |
| T06 | Zone/Conduit 對應 SR | Executor | TODO | 03_work/ | 03_work/zone_sr_mapping.md | Zone 與 SR 雙向可追溯 |
| T07 | IEC 62443-4-2 元件需求 | Executor | TODO | 03_work/sr_list.md | 03_work/cr_mapping.md | CR 對應 SR，含元件類型 |
| T08 | 稽核摘要報告初稿 | Executor | TODO | 03_work/ | 03_work/audit_summary.md | 含整體合規度、Critical Gap、建議行動 |
| T09 | 全域審查 | Reviewer | TODO | 03_work/ | 04_review/review_report.md | 缺陷定位至段落 |
| T10 | 修正缺陷 | Executor | TODO | 04_review/review_report.md | 03_work/ | 無 Critical 缺陷 |
| T11 | 發佈合規套件 | Controller | TODO | 04_review/ | 05_release/ | 矩陣與報告版本號一致 |
```

---

## 六、Controller 操作手冊

完整內容將建立於 `CONTROLLER_MANUAL.md`，以下是 ClaudeCode 建立時的全文：

```markdown
# Controller 操作手冊

版本：v1.0

---

## 你的角色

Controller 是這套工作流的唯一人類決策點。
你不寫內容，你決定：什麼時候開始、什麼任務執行、什麼時候放行。

---

## Step 0 — 準備 Inbox

1. 將所有原始需求放入 `00_inbox/`
   - 會議記錄、需求文件、圖片、郵件截圖、草稿 — 通通放進去
   - 不需要整理，這是 Planner 的工作
2. 在 `00_inbox/` 建立 `_meta.md`，說明：
   - 本次任務的最終目標（一句話）
   - 截止日期
   - 主要利害關係人
   - 已知限制或禁忌

## Step 1 — 觸發 Planner

對 ClaudeCode 輸入：

```
請使用 templates/prompt_planner.txt 的角色定義。
輸入目錄：00_inbox/
請產出：
- 01_brief/brief.md
- 02_plan/tasks.md
- 02_plan/acceptance.md
- 02_plan/assumptions.md
```

**你要審查的事**：
- [ ] brief.md 是否正確反映你的真實目標？
- [ ] tasks.md 的任務粒度是否合適（不是太大）？
- [ ] assumptions.md 是否有遺漏的重要假設？
- [ ] DoD 是否可以被客觀驗證？

**放行條件**：以上全部打勾才進 Step 2。

---

## Step 2 — 選定執行範圍

1. 打開 `02_plan/tasks.md`
2. 決定這次 Session 要跑哪些任務 ID
3. 建議一次只跑 1–3 個任務，避免 Token 過大

**選任務原則**：
- 依照依賴關係順序（輸入必須已存在）
- 優先跑 Critical Path 上的任務
- Blocked 任務跳過，先解決阻塞

---

## Step 3 — 觸發 Executor

對 ClaudeCode 輸入（每次只跑一個任務）：

```
請使用 templates/prompt_executor.txt 的角色定義。
當前任務 ID：[填入，例如 T05]
任務描述：[從 tasks.md 複製]
輸入檔案：[從 tasks.md 複製]
輸出路徑：[從 tasks.md 複製]
DoD 驗收條件：[從 acceptance.md 複製對應條件]
```

**你要審查的事**：
- [ ] Self-Check 清單是否全部 PASS？
- [ ] 輸出檔案是否存在於正確路徑？
- [ ] 有無意外修改其他檔案？

**放行條件**：Self-Check 無 FAIL 才繼續下一個任務。

---

## Step 4 — 觸發 Reviewer

當所有 Executor 任務完成後：

```
請使用 templates/prompt_reviewer.txt 的角色定義。
審查目錄：03_work/
驗收標準：02_plan/acceptance.md
輸出：04_review/review_report.md
```

**你要審查的事**：
- [ ] 所有應審文件都有被審到？
- [ ] Critical 缺陷是否可接受（不能有漏報）？

---

## Step 5 — 修正缺陷

**只修 Reviewer 點名的段落**，對 ClaudeCode 輸入：

```
請使用 templates/prompt_executor.txt 的角色定義。
當前任務：修正缺陷
輸入：04_review/review_report.md
只修正以下缺陷 ID：[列出 D01, D02...]
使用 patch 方式，不要重寫整份文件。
```

重複 Step 4 → Step 5 直到無 Critical 缺陷。

---

## Step 6 — 打包 Release

```
請將 03_work/ 中的最終交付物複製至 05_release/。
更新 04_review/change_log.md，登錄本次版本。
產出 05_release/release_notes.md，列出：
- 版本號
- 交付物清單
- 已知限制
- 下一版計畫（如有）
```

**最終放行檢查**：
- [ ] 無 Critical 缺陷
- [ ] change_log.md 已更新
- [ ] 05_release/ 有完整交付物

---

## 效率提示

| 情況 | 做法 |
|------|------|
| Token 超出限制 | 縮小任務範圍，一次只給一個輸入檔 |
| Executor 一直 FAIL Self-Check | 檢查 DoD 是否過嚴或輸入不足 |
| Reviewer 找不到缺陷 | acceptance.md 可能過於模糊，需補充具體條件 |
| 任務依賴不清楚 | 在 tasks.md 新增「依賴」欄位 |
| 需求中途改變 | 回到 Step 1，更新 brief.md，再走一遍 |

---

## 反常識提醒

> 不要把所有輸入一次丟給 LLM。
> 真正省 Token 的方式是工程拆分，讓每次對話只包含最小必要資訊。
```

---

## 七、執行完畢後的驗證清單

ClaudeCode 完成後，請確認以下項目均存在：

```
project_root/
├── 00_inbox/README.md
├── 01_brief/README.md
├── 02_plan/README.md
├── 03_work/README.md
├── 04_review/README.md
├── 05_release/README.md
├── 99_archive/README.md
├── templates/
│   ├── prompt_planner.txt
│   ├── prompt_executor.txt
│   ├── prompt_reviewer.txt
│   ├── tasks_template.md
│   ├── tasks_governance.md
│   ├── tasks_sysdesign.md
│   ├── tasks_compliance.md
│   ├── acceptance_template.md
│   ├── assumptions_template.md
│   └── change_log_template.md
├── CONTROLLER_MANUAL.md
└── setup_report.md
```

---

*Claude Autonomous Work Framework v1.0 — 讓 LLM 以最少 Token 做到最大產出*
