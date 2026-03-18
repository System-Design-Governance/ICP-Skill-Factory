# Phase 4 Brief — Skill Definition 修正與標準化

版本：v1.0
更新日期：2026-03-16
Controller：Victor Liu

---

## 系統邊界

本次修正作業範圍限於 `03-skill-definitions/registry/` 下的 171 個 SK-Dnn-nnn.md 檔案。不涉及新增技能定義、不涉及 Cowork SKILL.md 轉換（Phase 5 範疇）、不涉及上游治理文件（00-governance/）的變更。

## 核心目標

將 Phase 3 產出的 171 個 skill definition 從「初稿品質」提升至「標準化品質」，使所有檔案達到 Golden Format 合規、27-field schema 完整、跨參照正確，為後續 Cowork SKILL.md 轉換建立可靠的規格基礎。

## 成功標準（一句話）

171/171 檔案全部通過 Golden Format 結構驗證 + 27-field YAML 完整性驗證 + 跨參照有效性驗證。

## 主要限制

- 修正作業不改變技能的領域歸屬與 ID 編碼
- 不重新定義 schema（繼續使用 v1.1.0）
- Bare YAML 檔案的 prose 補寫以現有 YAML metadata 為種子，不引入未經源文件佐證的新資訊
- 所有修正必須經 Reviewer 驗證後才能進入 Release

## 利害關係人

- Controller（決策）：Victor Liu
- Executor（執行）：Claude Agent
- Reviewer（審查）：Claude Agent（獨立 session）

## 輸入來源

- `04-review/forensic-review-report.md` — 缺陷清單 D01-D08
- `03-skill-definitions/registry/SK-D01-001.md` — Golden Example
- `00-governance/SCHEMA.md` — 27-field schema v1.1.0
- `02-skill-candidates/skill-candidate-inventory.md` — domain_id / subdomain_id 正規對照

---

*Phase 4 Brief v1.0 — Planner 產出*
