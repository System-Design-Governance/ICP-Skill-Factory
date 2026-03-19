# PRD — OT 架構圖自動化工具鏈

版本：v1.0
更新日期：2026-03-04
負責人：Controller
來源文件：00_inbox/OT_Architecture_Framework_v1.0.md

---

## 1. 系統邊界

**在範圍內：**
- `gen_d2.py`：讀取 project.yaml + component_library.yaml，套用 Rulebook，輸出 .d2 源碼
- `optimize_svg.py`：執行八步驟 SVG 後製（Title Bar、Legend 浮層、白底遮罩、畫布修正）
- `check_collision.py`：A 類碰撞快速檢查，輸出碰撞數量與受影響節點
- `component_library.yaml`：現有設備初始資料填充（≥ 5 個已知型號）
- `project_template.yaml`：完整空白專案模板（所有欄位含 inline 說明）

**在範圍外（本次迭代）：**
- DWG-L2 安全圖模板（下一迭代 v1.3）
- DWG-L3/L4 模板
- 多專案批次產圖
- CI/CD 整合

---

## 2. 核心目標

工程師填寫一份 `project.yaml`（只描述「有什麼」，不寫 D2 語法），執行 4 個指令，得到一份符合以下條件的 SVG 架構圖：

1. **拓撲正確**：Purdue Model 分層清晰，Zone & Conduit 符合 IEC 62443
2. **視覺合規**：品牌色碼 100% 來自 R-BR-01，無舊版顏色
3. **碰撞可接受**：A 類碰撞 < 5（Yellow 以上即達標，Green 為優秀）
4. **可讀性高**：Title Bar、Legend 浮層、連線 label 白底遮罩均到位

---

## 3. 主要限制

| 限制 | 說明 |
|------|------|
| Layout engine 固定為 dagre | ELK 有已知缺陷（KB-01, KB-03），不可切換 |
| 子群組宣告順序決定位置 | dagre 依宣告順序從左到右排列，T-04 是最關鍵規則 |
| D2 不支援 title/legend | 必須由 optimize_svg.py 後製注入（KB-01） |
| stroke-dash 自動乘以 stroke-width | 後製必須執行 fix_dasharray()（KB-02, R-PP-04） |
| 連線 label 禁止 `\n` | SVG 中被忽略，用兩空格替代（KB-05, R-D2-10） |

---

## 4. 利害關係人

| 角色 | 需求 |
|------|------|
| OT 工程師（主要使用者） | 只填 YAML，不需要懂 D2；能快速產圖、調整、再產圖 |
| 系統整合商 | 產出 DWG-L3 拓撲圖，含設備型號、IP、線號 |
| 資安審查 | 產出 DWG-L2 Zone & Conduit 圖（下一迭代） |
| 客戶 / 業主 | 產出 DWG-L1 全景圖（本迭代支援） |

---

## 5. 成功定義（Release DoD）

- [ ] 以 `00_inbox/OT_Architecture_Framework_v1.0.md` 中的 project.yaml 範例執行，全流程無報錯
- [ ] 產出的 SVG 可在瀏覽器直接開啟，無 XML 錯誤
- [ ] A 類碰撞數 < 5
- [ ] Title Bar 存在，Legend 為浮層，連線 label 有白底遮罩
- [ ] 所有 🔴 Rulebook 規則（R-D2-01~10、R-PP-01~05、R-BR-01）均未被違反
- [ ] `component_library.yaml` 有 ≥ 5 個設備定義

---

## 6. 參考規格摘要

完整規格詳見 `00_inbox/OT_Architecture_Framework_v1.0.md`：

| 章節 | 關鍵內容 |
|------|---------|
| §5.1 | gen_d2.py 全部函式設計與對應 Rulebook |
| §5.2 | optimize_svg.py 八步驟流程 |
| §5.3 | check_collision.py 規格與合格標準 |
| §6   | 拓撲 Rulebook（R-D2-01~11）|
| §7   | SVG 後製 Rulebook（R-PP-01~06）|
| §8   | 品牌色碼（R-BR-01~02）|
| §3   | component_library.yaml YAML 結構定義 |
| §4   | project.yaml 完整欄位規格 |
