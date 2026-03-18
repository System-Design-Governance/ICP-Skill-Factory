# Assumptions & Risks — Phase 4 Skill Definition 修正與標準化

版本：v1.0
更新日期：2026-03-16

---

## 登錄格式

| ID | 類型 | 描述 | 影響 | 行動 | 狀態 |
|----|------|------|------|------|------|
| A01 | 假設 | Golden Example SK-D01-001 是所有檔案的結構範本權威，其 12 個 prose sections 是完整且正確的 | 若 Golden Example 本身有缺陷，所有修正都會繼承該缺陷 | Controller 在 Step 1 審核時確認 SK-D01-001 是否為合適的範本 | OPEN |
| A02 | 假設 | skill-candidate-inventory.md 中的 domain_id / subdomain_id 對照表是正確且完整的 | 若對照表有誤，T08 補全的欄位值會不正確 | T08 執行前交叉比對 SCHEMA.md 和 01-domain-map 的域定義 | OPEN |
| A03 | 假設 | SC→SK 全域替換可以安全地將所有 SC-Dnn-nnn 替換為 SK-Dnn-nnn | 若有 SC- 參照指向 Phase 3 正規化中已合併/移除的 ID，替換後會產生無效參照 | T11（無效參照修正）必須在 T10（全域替換）之前執行；T10 執行後需跑交叉驗證 | OPEN |
| A04 | 假設 | 21 個 Bare YAML 檔案的現有 YAML metadata 中包含足夠資訊來推導 prose 內容 | 若 YAML 過於簡略，prose 補寫可能品質不足或需要額外源文件輸入 | Executor 在 T01-T07 遇到資訊不足時標記 [BLOCKED] 並回報 Controller | OPEN |
| A05 | 假設 | 35 個 --- frontmatter 格式的檔案在轉換為 ```yaml 柵欄格式後，YAML 內容語義不變 | 若有檔案使用了 YAML frontmatter 特殊語法（如 multi-document），轉換可能破壞結構 | T12 使用保守的轉換腳本，轉換後逐檔驗證 YAML 可解析性 | OPEN |
| R01 | 風險 | 平行 Agent 執行 T01-T07 時可能產生風格不一致 | 同為 Bare YAML 補寫，但不同 Agent 的措辭和深度可能有差異 | 每批次完成後由 Reviewer 做風格一致性抽檢；或改用單一 Agent 序列執行 | OPEN |
| R02 | 風險 | T10 全域 sed 替換可能意外修改 YAML 值或 prose 文本中的合法 SC- 字串 | 替換了不應該被替換的文字（如解釋性文字中提到 SC- 前綴的語境） | 替換前先做 dry-run（`sed -n 's/SC-D/SK-D/gp'`），人工審核輸出；替換腳本使用 word-boundary matching | OPEN |
| R03 | 風險 | Phase 4 修正過程中的 context window 限制可能導致單次 session 無法完成所有 P0 任務 | T01-T07 共 21 個檔案的 prose 補寫量大（估計 21×80 行 = 1,680 行新增內容），可能需要多個 session | 按 domain 分批執行，每個 session 處理 1-2 個 T 任務；每個 session 獨立 Self-Check | OPEN |
| R04 | 風險 | Bare YAML 檔案的 prose 補寫可能引入與現有 Golden Format 檔案不一致的技術描述 | 同一 subdomain 的兩個 skill，一個由 Phase 3 Agent 撰寫、一個由 Phase 4 Agent 補寫，可能在措辭和技術深度上有落差 | Phase 4 補寫時要求 Executor 先讀取同域已完成的 Golden Format 檔案作為風格參考 | OPEN |

---

## 類型定義

- **假設**：視為真實但未經驗證的前提
- **風險**：可能發生的不利事件

## 狀態定義

- **OPEN**：尚未解決
- **RESOLVED**：已確認或消除
- **ACCEPTED**：接受此風險，不採取行動
- **BLOCKED**：需要外部輸入才能繼續

---

*Phase 4 Assumptions & Risks v1.0 — Planner 產出*
