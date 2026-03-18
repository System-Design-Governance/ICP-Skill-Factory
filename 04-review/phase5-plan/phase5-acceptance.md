# Acceptance Criteria — Phase 5 Cowork SKILL.md 轉換 (Wave 1)

版本：v1.0
更新日期：2026-03-16

---

## 全域 DoD

- [ ] 每個 SKILL.md 可被 Cowork 正確載入（YAML frontmatter 格式正確）
- [ ] 每個 SKILL.md 的 description 包含 MANDATORY TRIGGERS（中英文關鍵字）
- [ ] 不破壞現有 SKILL.md 的已實作功能

## YAML Frontmatter DoD

- [ ] 包含 `name:` 欄位（kebab-case）
- [ ] 包含 `description:` 欄位，使用 `>` 多行格式
- [ ] description 前半段：1-3 句功能描述
- [ ] description 中段：`MANDATORY TRIGGERS:` 後接 10-20 個中英文觸發關鍵字，逗號分隔
- [ ] description 後段：`Use this skill whenever...` 使用指引 + 邊界說明（何時不用此 skill）

## Workflow 內容 DoD

- [ ] 包含明確的步驟式 workflow（Step 1, 2, 3... 或 Phase 1, 2, 3...）
- [ ] 每個步驟有：輸入、動作、輸出
- [ ] 決策邏輯明確（if/when/unless 條件）
- [ ] 錯誤處理路徑存在（若輸入不足怎麼辦）

## 模板與工具 DoD

- [ ] 包含至少 1 個輸出模板（markdown table、報告結構、或 code block）
- [ ] 工具使用指引具體化（非「使用 Excel」而是「使用 openpyxl 建立 .xlsx」）
- [ ] 若需要檔案 I/O，指明路徑慣例

## 人類審核閘門 DoD

- [ ] 至少 1 個明確的 Human Review 節點
- [ ] 審核節點指明：審核什麼、誰審核、PASS/FAIL 條件
- [ ] 審核後的動作路徑（通過 → 下一步；不通過 → 修正/回退）

## SK 知識保留 DoD

- [ ] 對應 SK 的 Description 核心要素出現在 SKILL.md 的 Overview 或 Workflow 中
- [ ] 對應 SK 的 Inputs 反映在 SKILL.md 的輸入需求段落中
- [ ] 對應 SK 的 Outputs 反映在 SKILL.md 的輸出模板中
- [ ] 對應 SK 的 Standards 引用保留在 SKILL.md 中
- [ ] 對應 SK 的 Acceptance Criteria 轉化為 SKILL.md 的 Quality Checklist

## 量化指標

- [ ] 每個 SKILL.md 行數在 200-500 行之間
- [ ] Wave 1 Review Report 中 Critical 缺陷 = 0
- [ ] Controller 書面確認可用於日常設計工作

---

*Phase 5 Acceptance Criteria v1.0 — Planner 產出*
