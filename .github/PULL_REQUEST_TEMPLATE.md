## 變更類型

請勾選本次 PR 涉及的變更類型：

- [ ] SK 定義（`03-skill-definitions/`）
- [ ] SKILL.md（`05-cowork-skills/`）
- [ ] Plugin（`06-plugin-src/`）
- [ ] 治理文件（`00-governance/`）
- [ ] CI/CD 或工具鏈
- [ ] 文件或 README

---

## Skill 資訊

| 欄位 | 值 |
|------|-----|
| **Skill ID(s)** | <!-- 例：SK-D01-003, SK-D02-010 --> |
| **Plugin 歸屬** | <!-- 例：icp-seceng / icp-sysarch / icp-integration / icp-governance / icp-presales / N/A --> |
| **影響的 Domain** | <!-- 例：D01, D02 --> |

---

## 變更說明

<!-- 簡述本次變更的目的與內容 -->

---

## 自檢清單

### SK 定義變更
- [ ] YAML Metadata 13 個必填欄位皆存在且格式正確
- [ ] `skill_id` 符合 `SK-D{nn}-{nnn}` 格式
- [ ] `skill_type` 為合法 Enum 值（10 種之一）
- [ ] 必填 Prose Section 皆存在（Description, Inputs, Outputs, Acceptance Criteria, Source Traceability, Footer）
- [ ] Acceptance Criteria 為 3–6 項，可觀察且可驗證
- [ ] 無 `## Workflow` 或 `## Pitfalls` 章節（設計決策 ADR-007）
- [ ] Overlap Resolution Rules 檢查通過

### SKILL.md 變更
- [ ] 品質等級達 B 以上（≥ 100 行）
- [ ] 引用對應 SK 定義
- [ ] 觸發詞無衝突（已掃描 `05-cowork-skills/*/SKILL.md`）
- [ ] 模板與參考檔案存在且非空

### Plugin 變更
- [ ] `plugin.json` 格式正確（name, version, description, author）
- [ ] version 遵循 SemVer
- [ ] 所有 `skills/` 子目錄包含有效 SKILL.md

### 治理文件變更
- [ ] 版本號已遞增
- [ ] `CHANGELOG.md` 已更新
- [ ] 不違反既有 ADR 決策

---

## 備註

<!-- 任何額外說明、截圖、或討論事項 -->
