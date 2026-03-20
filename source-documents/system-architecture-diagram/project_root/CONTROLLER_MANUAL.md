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
