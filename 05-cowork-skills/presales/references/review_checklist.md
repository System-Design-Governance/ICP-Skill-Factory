# Presales 全域審查檢查清單

本文件供 Reviewer 在 Phase 3 (T08) 使用，定義所有必須執行的交叉一致性檢查。

---

## A. 交叉一致性檢查

### A1. 架構圖元件 vs CBOM 品項
- architecture.md 中每個硬體/軟體元件是否有對應 CBOM 行項目
- CBOM 品項編號 (CBOM-H01~Hnn, CBOM-S01~Snn) 是否與 architecture.md 元件表一致
- 數量是否一致（如 AP 數量、讀卡機數量）

### A2. 可行性估計 vs CBOM 總額
- feasibility.md 的成本估計範圍與 CBOM 總額的比較
- 若差距超過 30%，標記為 🔴 Critical 並分析根因
- 檢查各分類（硬體/軟體/ISP/人工）是否分別合理

### A3. 文件清冊 vs CBOM 人天
- doc_inventory.md 中每份文件是否有對應 CBOM 人工品項
- 目標：100% 文件覆蓋率（25/25 而非 6/25）
- 若文件含於某工作項目中，需在 CBOM 對照表中明確標註

### A4. Zone/Conduit 一致性
- architecture.md 文字描述 vs D2/Mermaid 圖中的 Zone 和 Conduit 是否完全對應
- Zone 數量、名稱、包含元件是否一致
- Conduit 數量、連接的 Zone、協定是否一致

### A5. 假設跨檔案追溯
- assumptions.md 中每個假設 (A01~Ann) 是否在至少一份交付物中被引用
- 標記 [$] 的假設是否都有對應 CBOM 行項目
- [BLOCKED] 項目是否影響估算精度，是否有備註說明

---

## B. SOW 覆蓋度檢查

### B1. 明確需求
- 逐項對照 SOW/需求書中的每個交付要求
- 每項需求必須在 architecture.md 或 doc_inventory.md 中有對應
- 使用表格列出：需求 | 涵蓋位置 | 涵蓋方式 | 狀態

### B2. 隱性需求
- brief.md 中的 IR-XX 項目是否全部有對應交付物
- 常漏項目：教育訓練、退場計畫、資產清冊、變更管理

---

## C. 合規性檢查

### C1. ER/標準條款覆蓋
- 列出適用的 ER/標準條款
- 每條是否在 architecture.md 的設計中有應對，或在 doc_inventory.md 的文件中有交付
- 使用表格：ER 條款 | 內容概要 | 架構/文件涵蓋 | 狀態

### C2. Gap Analysis 準備度
- 是否已有初步 Gap Analysis（即使只是 TODO）
- CBOM 中是否編列 Gap Analysis 人天

---

## D. 數值一致性檢查

### D1. 元件數量
- 逐項比對：architecture.md 規格 vs CBOM 數量
- 特別注意：AP 數量、端點授權數、讀卡機/門鎖數

### D2. 營運期間
- 所有文件中的營運期間（月數）是否一致
- ISP 月費、軟體授權、月維護的月份數是否與營運期間對齊

### D3. 成本範圍
- CBOM 成本基礎 vs feasibility 報價範圍的比率是否合理
- 一般而言 CBOM 成本基礎約為報價的 60-80%（含利潤/管銷後）

---

## E. 品質問題

### E1. TBD 項目
- 是否有未標記原因的 [TBD]
- 有原因的 TBD 是否登錄在 assumptions.md

### E2. 術語一致性
- 四份交付物中的術語是否與 glossary.md 一致
- 特別注意：品牌名稱、Zone 名稱、文件編號

### E3. 邏輯缺口
- 是否有設備在 architecture.md 中但沒有安裝工時
- 是否有文件在 doc_inventory.md 中但沒有編製工時
- 是否有假設影響成本但 CBOM 未反映

---

## 缺陷報告格式

每項缺陷必須包含：
- **ID**：E01, E02, ...
- **嚴重度**：🔴 Critical | 🟡 Major | 🟢 Minor
- **分類**：A/B/C/D/E 中的哪個
- **描述**：問題是什麼
- **位置**：具體到哪個檔案的哪個段落/表格
- **建議修正**：1-3 句，具體可執行
