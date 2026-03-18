# Tasks — Phase 4 Skill Definition 修正與標準化

更新日期：2026-03-16
版本：v1.0
負責人：Victor Liu (Controller)

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
| 對應缺陷 | forensic-review-report.md 中的缺陷 ID |

---

## 任務清單

### P0 — Critical：21 個 Bare YAML 檔案補全 prose sections（對應 D01）

| ID | Task | Owner | Status | Input | Output | DoD | 對應缺陷 |
|----|------|-------|--------|-------|--------|-----|----------|
| T01 | 補寫 D07 域 4 個 Bare YAML 檔案的 prose sections | Executor | TODO | SK-D07-002, D07-004, D07-005, D07-006 + SK-D01-001 (Golden Example) | 同 4 個檔案（原地更新） | 每個檔案包含 ≥12 個 ## prose sections；YAML 保留為 ```yaml 柵欄格式；內容與 YAML metadata 中的 skill description 一致 | D01 |
| T02 | 補寫 D08 域 2 個 Bare YAML 檔案的 prose sections | Executor | TODO | SK-D08-013, D08-014 + Golden Example | 同 2 個檔案 | 同 T01 DoD | D01 |
| T03 | 補寫 D09 域 5 個 Bare YAML 檔案的 prose sections | Executor | TODO | SK-D09-001, D09-004, D09-006, D09-008, D09-009 + Golden Example | 同 5 個檔案 | 同 T01 DoD | D01 |
| T04 | 補寫 D10 域 1 個 Bare YAML 檔案的 prose sections | Executor | TODO | SK-D10-007 + Golden Example | 同 1 個檔案 | 同 T01 DoD | D01 |
| T05 | 補寫 D11 域 1 個 Bare YAML 檔案的 prose sections | Executor | TODO | SK-D11-007 + Golden Example | 同 1 個檔案 | 同 T01 DoD | D01 |
| T06 | 補寫 D12 域 4 個 Bare YAML 檔案的 prose sections | Executor | TODO | SK-D12-003, D12-004, D12-006, D12-007, D12-008 + Golden Example | 同 5 個檔案 | 同 T01 DoD | D01 |
| T07 | 補寫 D13 域 3 個 Bare YAML 檔案的 prose sections | Executor | TODO | SK-D13-001, D13-002, D13-005 + Golden Example | 同 3 個檔案 | 同 T01 DoD | D01 |

**T01-T07 小計：21 個檔案**

---

### P1 — Major：YAML 欄位補全 + 參照修正（對應 D03, D04, D05）

| ID | Task | Owner | Status | Input | Output | DoD | 對應缺陷 |
|----|------|-------|--------|-------|--------|-----|----------|
| T08 | 為 50 個檔案補全 domain_id 與 subdomain_id 欄位 | Executor | TODO | 50 個缺欄位檔案列表 + skill-candidate-inventory.md（domain/subdomain 正規對照表） | 同 50 個檔案（原地更新） | 171/171 檔案均含 domain_id 和 subdomain_id 欄位；欄位值與 skill_id 的 Dnn 編碼一致 | D03 |
| T09 | 為 50 個檔案補全 skill_name_en、tags、composition_patterns 欄位 | Executor | TODO | 同 50 個檔案 + SCHEMA.md 欄位定義 | 同 50 個檔案 | 171/171 檔案均含 skill_name_en、tags、composition_patterns；skill_name_en 從 skill_name 或 Description 推導 | D03 |
| T10 | 全域修正 SC- → SK- 過時參照（331 處） | Executor | TODO | 全部 171 個檔案 | 同（原地更新） | 0 個 SC-Dnn-nnn 參照殘留（排除合法的「尚未定義」標記）；修正後的 SK- 參照對應 registry/ 中的實際檔案 | D04 |
| T11 | 修正 3 處無效 SK- 參照 | Executor | TODO | SK-D03-002, D03-005, D03-007（含 SK-D04-008）；SK-D08-013, D08-014（含 SK-D08-012）；SK-D11-004（含 SK-D11-002） | 同 6 個檔案 | SK-D04-008 → 移除或重映射至 D04 域有效 ID；SK-D08-012 → SK-D10-006；SK-D11-002 → SK-D11-017 | D05 |

**T08-T11 依賴關係**：T08 與 T09 可平行執行；T10 需在 T11 完成後執行（先修正無效 ID，再做全域 SC→SK 替換）。

---

### P2 — Major：YAML-alt 格式統一（對應 D06）

| ID | Task | Owner | Status | Input | Output | DoD | 對應缺陷 |
|----|------|-------|--------|-------|--------|-----|----------|
| T12 | 將 35 個 --- frontmatter 格式統一為 ```yaml 柵欄格式 | Executor | TODO | 35 個使用 --- 分隔的檔案 | 同（原地更新） | 171/171 檔案均使用 ```yaml ... ``` 柵欄格式包裹 YAML metadata | D06 |
| T13 | 標準化 YAML-alt 檔案的 prose section 標題名稱 | Executor | TODO | 同 35 個檔案中有 prose 但標題名不符 Golden Format 的子集 | 同（原地更新） | 所有 prose section 標題與 Golden Example 一致：Description, Inputs, Outputs, Tools, Standards, IEC 62443 Lifecycle Stages, Roles, Dependencies, Acceptance Criteria, Estimated Effort, Composition Patterns, Source Traceability | D06 |

**T12-T13 依賴**：T13 在 T12 之後執行（先統一 YAML 柵欄，再處理 section headers）。

---

### P3 — Minor：個別修正（對應 D07, D08）

| ID | Task | Owner | Status | Input | Output | DoD | 對應缺陷 |
|----|------|-------|--------|-------|--------|-----|----------|
| T14 | 修正 2 組循環硬依賴 | Executor | TODO | 待識別的 2 組循環依賴檔案 | 同（原地更新） | Dependencies section 中無循環硬依賴（Hard Prerequisites 不可互指） | D07 |
| T15 | 重寫 SK-D10-006 使其符合 Golden Format | Executor | TODO | SK-D10-006（當前 54% 完整度）+ Golden Example | SK-D10-006 | 12 個標準 prose sections 全部存在且內容充實；結構完整度 ≥95% | D08 |

---

### R — Reviewer 審查

| ID | Task | Owner | Status | Input | Output | DoD | 對應缺陷 |
|----|------|-------|--------|-------|--------|-----|----------|
| T16 | 全域結構驗證（自動化腳本） | Reviewer | TODO | 全部 171 個檔案 | 04-review/phase4-review-structural.md | 檢查項：(1) ```yaml 柵欄存在 (2) 13 個 YAML 必要欄位存在 (3) 12 個 ## 標準 prose sections 存在 (4) footer 行存在。覆蓋率報告 171/171 per check | 全域 |
| T17 | 全域參照驗證（自動化腳本） | Reviewer | TODO | 全部 171 個檔案 | 04-review/phase4-review-references.md | 檢查項：(1) SC- 殘留數 = 0 (2) 所有 SK- 參照指向有效檔案 (3) 無循環硬依賴。三項全 PASS | D04, D05, D07 |
| T18 | 內容品質抽樣（10% = 17 檔案） | Reviewer | TODO | 隨機抽樣 17 個檔案，涵蓋 P0 修正檔案至少 5 個 | 04-review/phase4-review-quality.md | 每個抽樣檔案以 5 維度評分（結構/完整性/準確性/一致性/可用性），PASS 標準 ≥80% 得分 | 全域 |
| T19 | 編製 Phase 4 Review Report（彙整 T16-T18） | Reviewer | TODO | T16-T18 產出物 | 04-review/phase4-review-report.md | 使用 Framework 標準格式（缺陷列表 + 嚴重度 + 整體評估）；Release 條件：0 Critical、≤3 Major | 全域 |

---

### Release

| ID | Task | Owner | Status | Input | Output | DoD | 對應缺陷 |
|----|------|-------|--------|-------|--------|-----|----------|
| T20 | Controller 審核 Review Report 並決定放行 | Controller | TODO | 04-review/phase4-review-report.md | Controller 書面放行（chat 中確認） | Review Report 中 0 Critical 缺陷；Controller 書面確認 "RELEASE APPROVED" | — |
| T21 | 更新 README.md Phase 4 狀態 | Executor | TODO | README.md | README.md（更新） | Phase 4 列標示 COMPLETE + 日期 + 統計數字 | — |

---

## 執行順序與依賴圖

```
T01-T07 (P0, 可平行) ──→ T08+T09 (P1a, 可平行) ──→ T11 (P1b) ──→ T10 (P1c)
                                                                        ↓
                                                    T12 (P2a) ──→ T13 (P2b)
                                                                        ↓
                                                    T14+T15 (P3, 可平行)
                                                                        ↓
                                                    T16+T17 (R, 可平行) ──→ T18 ──→ T19
                                                                                       ↓
                                                                                 T20 (Controller)
                                                                                       ↓
                                                                                 T21 (Release)
```

**注意**：P0 的 T01-T07 與 P1 的 T08-T09 可以平行執行（不同檔案集，無衝突）。T10 全域 SC→SK 替換應最後執行，避免與 T01-T07 的 prose 補寫產生衝突。

## 狀態統計

- TODO：21
- IN_PROGRESS：0
- DONE：0
- BLOCKED：0

---

*Phase 4 Tasks v1.0 — Planner 產出*
