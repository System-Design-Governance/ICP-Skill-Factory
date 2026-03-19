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
