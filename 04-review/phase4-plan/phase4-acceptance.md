# Acceptance Criteria — Phase 4 Skill Definition 修正與標準化

版本：v1.0
更新日期：2026-03-16

---

## 全域 DoD（所有任務通用）

- [ ] 輸出檔案存在於指定路徑
- [ ] 檔案內容無破碎的連結或空白佔位符（如 [TBD]、[TODO]、[PLACEHOLDER]）
- [ ] 修改僅限於指定範圍，未意外變更其他檔案內容
- [ ] Self-Check 清單已附上且無 FAIL 項目

---

## P0 — Bare YAML 補全 DoD（T01-T07）

- [ ] 每個修正檔案包含完整的 YAML metadata 區塊（```yaml 柵欄格式）
- [ ] YAML 區塊包含 13 個必要欄位：skill_id, skill_name_en, skill_name_zh, domain_id, subdomain_id, skill_type, tier, maturity, version, created_date, confidence, owner, tags, composition_patterns
- [ ] YAML 區塊之後包含 12 個標準 ## prose sections：Description, Inputs, Outputs, Tools, Standards, IEC 62443 Lifecycle Stages, Roles, Dependencies, Acceptance Criteria, Estimated Effort, Composition Patterns, Source Traceability
- [ ] 每個 prose section 有實質內容（非空、非佔位符），最少 2 句話
- [ ] Description section 與 YAML 中的 skill 相關欄位語義一致
- [ ] Dependencies section 使用標準格式（### Hard Prerequisites / ### Soft Recommendations）
- [ ] 檔案末尾有 footer 行：`*Validated from template v1.1.0 | ...*`
- [ ] prose 內容不引入未經源文件佐證的技術規格（以現有 YAML 和 domain 知識為基礎）

## P1a — YAML 欄位補全 DoD（T08-T09）

- [ ] 171/171 檔案均包含 domain_id 欄位，值格式為 `D{nn}`，與 skill_id 中的域編碼一致
- [ ] 171/171 檔案均包含 subdomain_id 欄位，值格式為 `D{nn}.{n}`，與 skill-candidate-inventory.md 對照一致
- [ ] 171/171 檔案均包含 skill_name_en 欄位，值為英文字串
- [ ] 171/171 檔案均包含 tags 欄位，值為 YAML list 格式 `[tag1, tag2, ...]`
- [ ] 171/171 檔案均包含 composition_patterns 欄位
- [ ] 新增欄位的插入位置不破壞現有 YAML 結構

## P1b — 無效參照修正 DoD（T11）

- [ ] SK-D04-008 所有引用已修正（移除或重映射至 D04 域有效 SK ID）
- [ ] SK-D08-012 所有引用已修正為 SK-D10-006
- [ ] SK-D11-002 所有引用已修正為 SK-D11-017
- [ ] 修正後的參照目標在 registry/ 中有對應的 .md 檔案

## P1c — 全域 SC→SK 替換 DoD（T10）

- [ ] `grep -r 'SC-D[0-9]' registry/` 結果為空（0 matches）
- [ ] 替換後的 SK-Dnn-nnn 參照全部指向 registry/ 中存在的檔案（交叉驗證通過）
- [ ] 未將 3 個已知無效 ID（D04-008, D08-012, D11-002）從 SC- 替換為 SK-（這些在 T11 中已個別處理）

## P2 — 格式統一 DoD（T12-T13）

- [ ] 171/171 檔案的 YAML metadata 均使用 ```yaml ... ``` 柵欄格式（非 --- frontmatter）
- [ ] 0 個檔案使用 `---` 作為 YAML 分隔符
- [ ] 所有 prose section 標題名稱與 Golden Example (SK-D01-001) 完全一致
- [ ] 無非標準標題殘留（如 Core Identity, Governance, Technical Reference 等）

## P3 — Minor 修正 DoD（T14-T15）

- [ ] 循環硬依賴數量 = 0（驗證方式：圖論拓撲排序無環）
- [ ] SK-D10-006 結構完整度 ≥95%（12 個標準 sections 中至少 11 個存在且有實質內容）

---

## Reviewer 驗證 DoD（T16-T19）

- [ ] T16 結構驗證覆蓋 171/171 檔案，每個檢查項報告 PASS/FAIL 數量
- [ ] T17 參照驗證三項全 PASS（SC 殘留=0、SK 全有效、無循環依賴）
- [ ] T18 品質抽樣 17 個檔案中 ≥15 個 PASS（≥88% 通過率）
- [ ] T19 Review Report 使用 Framework 標準格式，含缺陷列表、嚴重度分類、整體評估

## Release DoD（T20-T21）

- [ ] Review Report 中 🔴 Critical 缺陷數 = 0
- [ ] Review Report 中 🟡 Major 缺陷數 ≤ 3
- [ ] Controller 書面確認 "RELEASE APPROVED"
- [ ] README.md 已更新 Phase 4 狀態

---

*Phase 4 Acceptance Criteria v1.0 — Planner 產出*
