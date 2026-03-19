# Change Log — OT 架構圖自動化工具鏈

---

## v1.0.0  2026-03-04  初始發布

### 新增
- `gen_d2.py` — OT 架構圖 D2 源碼產生器，實作 T-01~T-08、R-D2-01~R-D2-10
- `optimize_svg.py` — 8 步驟 SVG 後製腳本，實作 R-PP-01~R-PP-06
- `check_collision.py` — A 類碰撞快速檢查（線段距離演算法）
- `component_library.yaml` — 10 個標準設備定義
- `project_template.yaml` — 帶 inline 說明的 project.yaml 模板
- `Makefile` / `run.sh` — 完整自動化 pipeline

### 已知限制
- 僅支援 dagre 佈局引擎（ELK 禁用，見 R-D2-01）
- D2 版本需 ≥ 0.6.0
- Python 需 ≥ 3.9

---

## Reviewer 修正紀錄（v1.0.0 → v1.0.0 release）

| ID | 修正內容 | 檔案:行號 |
|----|---------|----------|
| M-001 | HMI_A label double suffix（hmi_count=1 時） | gen_d2.py:424–428 |
| M-002 | check_collision.py stdout UTF-8 重設，恢復 emoji 狀態符號 | check_collision.py:13–15 |
| M-003 | validate_config() 新增 REQUIRED_COMM_KEYS 驗證 | gen_d2.py:313–322 |
| M-004 | ZONE_LABEL_PREFIXES "Field" 改為精確前綴 | check_collision.py:133 |
| M-005 | acceptance.md viewBox height 比較方向勘誤 | acceptance.md:80 |

---

## v1.0.1  2026-03-04  使用者回饋修正

### 修正（Legend 重疊、Zone 排序不工整、線路與文字交疊）

| ID | 修正內容 | 檔案 |
|----|---------|------|
| F-01 | `gen_conn_l0()` 連線方向由 L0→L1 反轉為 L1→L0（GW 為 MMS Client），讓 dagre 正確將 L0 排在 L1 下方，解決 Zone 排序問題 | gen_d2.py:886–914 |
| F-02 | Legend 位置改為固定放在圖表內容底部下方（y = canvas_h + TITLE_HEIGHT + 20），水平居中，根本解決 Legend 重疊問題 | optimize_svg.py:470–480 |
| F-03 | update_canvas() 新增 extra_h 參數，將 Legend 高度納入 viewBox 計算，確保 Legend 完整顯示在畫布內 | optimize_svg.py:394–416 |

---

## v1.0.2  2026-03-04  A1 圖紙輸出 + 元件庫擴充

### 新增

| ID | 修正/新增內容 | 檔案 |
|----|-------------|------|
| E-01 | `component_library.yaml` 擴充為 34 個標準設備（涵蓋 L4/DMZ/L3/L2/L1/L0 全層） | component_library.yaml |
| E-02 | `gen_d2.py` CLASSES_BLOCK 字型放大：Zone 容器 13→16 pt、子群組 11→13 pt、設備節點 10→12 pt（A1 可讀性）| gen_d2.py |
| E-03 | `optimize_svg.py` 新增 `set_paper_size()` 函式（Step 8b），在根 SVG 元素寫入 `width="841mm" height="594mm"`（A1 橫向），確保瀏覽器/印表機縮放至 A1 紙面 | optimize_svg.py |

### 驗證結果

- project_test.yaml → diagram_final.svg：A 類碰撞 0（Green ✅），SVG width="841mm" height="594mm"
- project_substation.yaml → substation_final.svg：A 類碰撞 0（Green ✅），SVG width="841mm" height="594mm"
