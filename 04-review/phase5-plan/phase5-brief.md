# Phase 5 Brief — Cowork SKILL.md 轉換

版本：v1.0
更新日期：2026-03-16
Controller：Victor Liu

---

## 系統邊界

將 `03-skill-definitions/registry/` 中的 171 個 SK-Dnn-nnn.md 規格書，按 subdomain 聚合後轉換為可執行的 Cowork SKILL.md 檔案，部署至 `.skills/skills/` 目錄。本次 Wave 1 僅處理已有 scaffold 的 4 個 skill（compliance-gap-assessor、arch-diagram、cbom-builder、presales），驗證轉換模式後再擴展。

## 核心目標

建立可重複的「SK 規格書 → SKILL.md 執行手冊」轉換流程，並以 Wave 1 的 4 個 skill 作為模式驗證。轉換後的 SKILL.md 應能讓 Claude 在 Cowork 模式下直接執行對應的設計工作，由人類 Review 成果。

## 成功標準

Wave 1 的 4 個 SKILL.md 通過以下驗證：(1) YAML frontmatter 正確觸發、(2) workflow 步驟可執行、(3) 輸出模板完整、(4) 人類審核閘門存在。

## 主要限制

- 不修改上游 SK 定義（Phase 4 已凍結）
- 現有 4 個 scaffold 的既有內容盡量保留並增強，不從零重寫
- 轉換後的 SKILL.md 必須相容現有 Cowork skill 載入機制（YAML frontmatter: name + description with MANDATORY TRIGGERS）
- 每個 SKILL.md 控制在 200-500 行內（參考現有 skills 長度）

## 利害關係人

- Controller：Victor Liu
- Executor：Claude Agent
- Reviewer：Claude Agent（獨立 session）

## 輸入來源

- `03-skill-definitions/registry/SK-*.md` — 171 個標準化規格書
- `.skills/skills/compliance-gap-assessor/SKILL.md` — 167 行 scaffold
- `.skills/skills/arch-diagram/SKILL.md` — 501 行 已實作
- `.skills/skills/cbom-builder/SKILL.md` — 512 行 已實作
- `.skills/skills/presales/SKILL.md` — 385 行 已實作
- `04-review/forensic-review-report.md` — 轉換映射規則

## Wave 1 SK→SKILL 映射

| Cowork Skill | 主要 SK 來源 | Subdomain 聚合 |
|-------------|-------------|---------------|
| compliance-gap-assessor | SK-D01-011, D01-012, D01-013, D01-029 | D01.3 合規與稽核 |
| arch-diagram | SK-D01-001, D01-002, D02-001, D02-004, D02-011 | D01.1 + D02.1 架構設計 |
| cbom-builder | SK-D14-005, D14-006, D14-007 | D14.3 成本估算 |
| presales | SK-D14-001 ~ D14-004, D14-008 ~ D14-010 | D14.1 + D14.2 售前流程 |

---

*Phase 5 Brief v1.0 — Planner 產出*
