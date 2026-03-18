# Assumptions & Risks — Phase 5 (Wave 1)

版本：v1.0
更新日期：2026-03-16

---

| ID | 類型 | 描述 | 影響 | 行動 | 狀態 |
|----|------|------|------|------|------|
| A01 | 假設 | 現有 4 個 SKILL.md 的結構可作為轉換目標的權威範本 | 若現有 skill 結構有設計缺陷，Wave 1 產出會繼承 | Controller 在 T01 模板審核時確認結構合理性 | OPEN |
| A02 | 假設 | Cowork 的 SKILL.md 載入機制僅需要 YAML frontmatter 的 name + description 欄位 | 若有其他必要欄位，SKILL.md 可能無法載入 | 參考現有已成功載入的 skill 確認最小必要欄位 | OPEN |
| A03 | 假設 | 增強現有 scaffold 比從零撰寫更高效且風險更低 | 若 scaffold 結構與 SK 規格差異過大，整合可能比重寫更耗時 | T02 執行時評估，若整合困難則回報 Controller 決定是否重寫 | OPEN |
| A04 | 假設 | SK 規格書中的 Acceptance Criteria 可直接轉化為 SKILL.md 的 Quality Checklist | 若 SK 的 AC 太偏向「人類能力評估」而非「Claude 可執行驗證」，需重新設計 | Executor 在轉換時標記不可自動化的 AC，改寫為可執行版本 | OPEN |
| R01 | 風險 | 增強後的 SKILL.md 可能破壞現有已運作的功能 | arch-diagram (501行) 和 cbom-builder (512行) 已有完整實作，修改可能引入 regression | T03/T04 使用增量修改而非全文重寫；修改前備份原檔 | OPEN |
| R02 | 風險 | 多個 SK 聚合為 1 個 SKILL.md 時可能資訊衝突或冗餘 | 同 subdomain 的 SK 可能有重疊的 Inputs/Tools/Standards | Executor 在聚合時去重並標記衝突，Controller 決定取捨 | OPEN |
| R03 | 風險 | Wave 1 模式若不穩定，Wave 2+ 擴展會放大問題 | 錯誤的轉換模式在 40-60 個 SKILL.md 中重複 | Wave 1 Review 必須嚴格，Controller 確認模式後才啟動 Wave 2 | OPEN |

---

*Phase 5 Assumptions & Risks v1.0 — Planner 產出*
