# Acceptance Criteria — OT 架構圖自動化工具鏈

版本：v1.0
更新日期：2026-03-04

---

## 全域 DoD（所有任務通用）

- [ ] 輸出檔案存在於 03_work/ 指定路徑
- [ ] 文件 / 程式碼使用 UTF-8 編碼
- [ ] 無破碎的佔位符（如 [TBD]、[TODO]）
- [ ] Self-Check 清單已附上且無 FAIL 項目

---

## 程式碼任務 DoD

- [ ] Python 語法正確，可執行（python -c "import gen_d2" 無報錯）
- [ ] 函式有對應 Rulebook ID 的 inline 註解（如 `# T-04: gw 必須第一個`）
- [ ] 無硬編碼的色碼，色碼統一從常數或 R-BR-01 表格取用
- [ ] 所有 CLI 入口支援 --help

---

## project_template.yaml DoD（T01）

- [ ] 包含 project / scada / dmz / enterprise / network / field_control / field_devices / comm_styles 所有頂層 key
- [ ] 每個欄位有 inline 中文說明
- [ ] 以 Framework §4.2 的 project.yaml 範例驗證：模板能涵蓋範例中全部欄位

---

## component_library.yaml DoD（T02）

- [ ] 至少包含以下 5 個設備定義（Framework §3.4）：
  - SW-MOXA-EDS-408A（SWITCH_PRP）
  - GW-ADV-IEC7442（GATEWAY）
  - RTU-TPRI-RSG007R（RTU）
  - FW-MOXA-EDR-GN010（FIREWALL）
  - IED-SEL-487E（IED_PROTECTION）
- [ ] 所有必填欄位（id / category / vendor / model / display_name / d2_class / protocols）非空
- [ ] category 值均在 §3.3 合法列表內

---

## gen_d2.py 功能 DoD（T03~T13）

- [ ] **R-D2-01**：輸出的 .d2 含 `layout-engine: dagre`，無 elk 字樣
- [ ] **R-D2-02**：輸出的 .d2 無 `title:` 和 `legend:` 節點
- [ ] **R-D2-03 / T-04**：L1 Zone 子群組宣告順序為 gw → rtu_panels → mcc → statcom（不論 project.yaml 中順序）
- [ ] **R-D2-05**：L0 子群組宣告順序為 r_group 在前、solar 在後
- [ ] **T-05 / R-D2-06**：LAN-A 骨幹連線只有第一條保留 label，其餘為 `""`；LAN-B 同理
- [ ] **T-06**：connected_to=null 的設備完全不產生連線宣告
- [ ] **T-07**：enterprise.enabled=false 時 L4 Zone 及所有 L4 連線完全省略
- [ ] **T-08**：statcom.enabled=false 時 statcom 子群組完全省略
- [ ] **R-D2-08**：所有子群組使用 `class: zone_sub`，無硬編碼 fill/stroke
- [ ] **R-D2-09**：所有連線使用 inline style，無 `class:` 引用
- [ ] **R-D2-10**：所有連線 label 無 `\n` 字元

---

## gen_d2.py 整合測試 DoD（T14）

- [ ] 以 Framework §4.2 的 project.yaml（6 feeders、PRP 開啟、STATCOM 開啟、enterprise 開啟）執行無報錯
- [ ] 輸出 L2 edge switch 數量 = feeder_groups 數 × 2 = 12
- [ ] validate_config() 能偵測無效的 comm_styles key，輸出具體錯誤訊息
- [ ] .d2 可通過 `d2 --dry-run` 語法驗證

---

## optimize_svg.py DoD（T15~T19）

- [ ] **R-PP-01**：八步驟依序執行，順序不可跳
- [ ] **R-PP-02**：Title Bar 存在於 y=0~110；背景 #0C3467；左側 6px #008EC3 條；三行文字格式符合規格
- [ ] **R-PP-03**：Legend 為浮層（非頁尾全寬）；位置由 find_empty_zone() 動態決定，不硬編碼
- [ ] **R-PP-04**：fix_dasharray() 正確修正所有 dasharray > 8 的值
- [ ] **R-PP-05**：含 CONN_KEYWORDS 的連線 label 均有白底 rect 墊底
- [ ] 輸出 SVG 可在 Chrome / Firefox 直接開啟，無 XML 解析錯誤
- [ ] 輸出 SVG viewBox height 大於 diagram_raw.svg（Step 3 content shift +110px，Title Bar 空間）

---

## check_collision.py DoD（T20）

- [ ] `python check_collision.py <svg_path>` 輸出 a_class 整數 + 受影響節點列表
- [ ] a_class == 0 → 顯示 "Green ✅"；1~4 → "Yellow ⚠️"；≥ 5 → "Red ❌"
- [ ] 錯誤的 svg_path 時輸出友好錯誤訊息並 exit code 1

---

## 全流程 End-to-End DoD（T22）

- [ ] 依 §10.1 SOP 8 步驟完整執行，無 unhandled exception
- [ ] `check_collision.py` 回報 a_class < 5（Yellow 以上）
- [ ] §12.3 D2 源碼自我檢查清單全部通過
- [ ] §12.3 SVG 後製自我檢查清單全部通過

---

## Release DoD（T25，最終關卡）

- [ ] 04_review/review_report.md 中無 🔴 Critical 缺陷
- [ ] 所有 T01~T24 任務狀態為 DONE
- [ ] 04_review/change_log.md 已更新
- [ ] 05_release/ 目錄包含：gen_d2.py、optimize_svg.py、check_collision.py、component_library.yaml、project_template.yaml、Makefile / run.sh、diagram_final.svg（範例輸出）
- [ ] 05_release/release_notes.md 存在，列出版本號、交付物清單、已知限制
