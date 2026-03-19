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
