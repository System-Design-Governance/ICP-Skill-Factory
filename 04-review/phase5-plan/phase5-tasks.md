# Tasks — Phase 5 Cowork SKILL.md 轉換 (Wave 1)

更新日期：2026-03-16
版本：v1.0
負責人：Victor Liu (Controller)

---

## 任務清單

### 準備工作

| ID | Task | Owner | Status | Input | Output | DoD |
|----|------|-------|--------|-------|--------|-----|
| T01 | 建立 SKILL.md 轉換模板 | Executor | TODO | 現有 4 個 SKILL.md + SK-D01-001 (Golden) | `templates/skill-conversion-template.md` | 模板包含：YAML frontmatter 骨架、標準 section 結構（Overview → Workflow → Templates → Tools → Quality Checklist → Human Review Gates）、MANDATORY TRIGGERS 撰寫指引 |

### Wave 1 轉換 — 4 個 SKILL.md

| ID | Task | Owner | Status | Input | Output | DoD |
|----|------|-------|--------|-------|--------|-----|
| T02 | 增強 compliance-gap-assessor SKILL.md | Executor | TODO | SK-D01-011,012,013,029 + 現有 scaffold (167行) | `.skills/skills/compliance-gap-assessor/SKILL.md` | (1) YAML description 含中英文 MANDATORY TRIGGERS (2) 從 scaffold 狀態升級為完整實作 (3) 新增 workflow steps、輸出模板、quality checklist、human review gates (4) 200-500 行 |
| T03 | 增強 arch-diagram SKILL.md | Executor | TODO | SK-D01-001,002, SK-D02-001,004,011 + 現有 (501行) | `.skills/skills/arch-diagram/SKILL.md` | (1) 整合 SK-D01-001 的 Zone/Conduit 設計知識 (2) 整合 SK-D02-001 的 OT 網路拓撲設計 (3) 補充 Acceptance Criteria 和 Human Review gate (4) 保持現有渲染規範不變 |
| T04 | 增強 cbom-builder SKILL.md | Executor | TODO | SK-D14-005,006,007 + 現有 (512行) | `.skills/skills/cbom-builder/SKILL.md` | (1) 整合 D14 成本估算 SK 的 Inputs/Outputs/Acceptance Criteria (2) 補充 IEC 62443 相關的安全設備成本估算邏輯 (3) 新增 Human Review gate |
| T05 | 增強 presales SKILL.md | Executor | TODO | SK-D14-001~004,008~010 + 現有 (385行) | `.skills/skills/presales/SKILL.md` | (1) 整合 D14 售前流程 SK 的 workflow knowledge (2) 補充 IEC 62443 lifecycle 對應的 presales 階段 (3) 強化 feasibility assessment section 的 domain-specific criteria |

### Wave 1 Review

| ID | Task | Owner | Status | Input | Output | DoD |
|----|------|-------|--------|-------|--------|-----|
| T06 | 結構驗證：4 個 SKILL.md 格式合規性 | Reviewer | TODO | 4 個更新後的 SKILL.md | `04-review/phase5-w1-review.md` | (1) YAML frontmatter 含 name + description + MANDATORY TRIGGERS (2) 每個 SKILL.md 有 workflow steps (3) 有 output templates (4) 有 human review gates (5) 行數 200-500 |
| T07 | 內容驗證：SK 規格書知識保留度 | Reviewer | TODO | 4 個 SKILL.md + 對應 SK 定義 | 同上 | 每個 SKILL.md 保留對應 SK 的：(1) Description 核心要素 (2) Inputs/Outputs 完整性 (3) Standards 引用 (4) Acceptance Criteria 可量化條件 |
| T08 | Controller 審核 Wave 1 成果 | Controller | TODO | `04-review/phase5-w1-review.md` + 4 個 SKILL.md | Controller 書面確認 | Review Report 無 Critical 缺陷；Controller 確認 4 個 SKILL.md 可用於日常設計工作 |

---

## 執行順序

```
T01 (模板) → T02+T03+T04+T05 (可平行) → T06+T07 (Review) → T08 (Controller)
```

## 狀態統計

- TODO：8
- IN_PROGRESS：0
- DONE：0
- BLOCKED：0

---

*Phase 5 Tasks v1.0 (Wave 1) — Planner 產出*
