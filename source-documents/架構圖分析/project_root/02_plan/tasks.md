# Tasks — OT 架構圖自動化工具鏈

更新日期：2026-03-04（最後執行：2026-03-04）
版本：v1.1
負責人：Controller

---

## 欄位定義

| 欄位 | 說明 |
|------|------|
| ID | 唯一識別碼，格式 T00 |
| Task | 任務名稱，動詞開頭 |
| Owner | Planner / Executor / Reviewer / Controller |
| Status | TODO / IN_PROGRESS / DONE / BLOCKED |
| Input | 輸入檔案路徑 |
| Output | 輸出檔案路徑 |
| DoD | 可驗證的完成條件 |

---

## Phase 0：環境與基礎資料

| ID | Task | Owner | Status | Input | Output | DoD |
|----|------|-------|--------|-------|--------|-----|
| T01 | 建立 project_template.yaml | Executor | DONE | 00_inbox/OT_Architecture_Framework_v1.0.md §4 | 03_work/project_template.yaml | 所有欄位存在，含 inline 中文說明；以 Framework 範例 project.yaml 驗證欄位完整性 |
| T02 | 建立 component_library.yaml 初始資料 | Executor | DONE | 00_inbox/OT_Architecture_Framework_v1.0.md §3 | 03_work/component_library.yaml | ≥ 5 個設備定義，包含 SW-MOXA-EDS-408A、GW-ADV-IEC7442、RTU-TPRI-RSG007R、FW-MOXA-EDR-GN010、IED-SEL-487E；所有必填欄位非空 |

---

## Phase 1：gen_d2.py 實作

| ID | Task | Owner | Status | Input | Output | DoD |
|----|------|-------|--------|-------|--------|-----|
| T03 | 實作 load_config() + validate_config() | Executor | DONE | 00_inbox/OT_Architecture_Framework_v1.0.md §5.1 §4.2；03_work/component_library.yaml | 03_work/gen_d2.py（部分） | 能載入 project.yaml；validate_config() 驗證 connected_to 引用存在、comm_styles key 合法，錯誤時輸出具體錯誤訊息並中止 |
| T04 | 實作 gen_header()（CLASSES_BLOCK 常數） | Executor | DONE | 00_inbox/OT_Architecture_Framework_v1.0.md §8 R-BR-01、§6 R-D2-01 R-D2-08 | 03_work/gen_d2.py（部分） | 輸出含 vars.d2-config.layout-engine=dagre；CLASSES_BLOCK 包含所有 19 個 d2_class（scada_server/hmi_workstation/firewall/switch_prp 等）；品牌色碼 100% 符合 R-BR-01 |
| T05 | 實作 gen_l4() + gen_dmz() | Executor | DONE | 00_inbox/OT_Architecture_Framework_v1.0.md §5.1 T-07；03_work/gen_d2.py（T03/T04 完成） | 03_work/gen_d2.py（部分） | enterprise.enabled=false 時完全省略 L4 Zone（T-07）；DMZ 含 firewall + l3_switch + remote_access 可選節點；顏色符合 R-BR-01 |
| T06 | 實作 gen_l3()（HMI/historian/ntp/ups 開關） | Executor | DONE | 00_inbox/OT_Architecture_Framework_v1.0.md §5.1 T-02；03_work/gen_d2.py（T05 完成） | 03_work/gen_d2.py（部分） | hmi_count=1 只產 HMI_A（T-02）；hmi_count=2 產 HMI_A + HMI_B；historian/engineering_ws/ntp/ups_l3 各自可選；所有 class 引用合法 |
| T07 | 實作 gen_l2()（feeder_groups 動態展開） | Executor | DONE | 00_inbox/OT_Architecture_Framework_v1.0.md §5.1 T-01；03_work/gen_d2.py（T06 完成） | 03_work/gen_d2.py（部分） | prp_enabled=true 時每個 feeder_group 展開 SW_{id}_A + SW_{id}_B；prp_enabled=false 只展開 SW_{id}_A（T-01）；6 個 feeder_groups 產生正確數量節點 |
| T08 | 實作 gen_l1() + gen_l1_gw()（T-04 規則） | Executor | DONE | 00_inbox/OT_Architecture_Framework_v1.0.md §5.1 T-04 R-D2-03；03_work/gen_d2.py（T07 完成） | 03_work/gen_d2.py（部分） | L1 容器內子群組宣告順序強制為：gw 第一（T-04）；gateways.count=1 只產 GW_A（T-03）；count=2 產 GW_A + GW_B |
| T09 | 實作 gen_l1_rtu_panel() + gen_l1_mcc() + gen_l1_statcom() | Executor | DONE | 00_inbox/OT_Architecture_Framework_v1.0.md §5.1 T-01 T-08；03_work/gen_d2.py（T08 完成） | 03_work/gen_d2.py（部分） | rtu_panel 含 IED 子節點；redbox 受 prp_enabled 控制（T-01）；mcc 從 feeder_groups 展開，數量正確；statcom.enabled=false 完全省略（T-08） |
| T10 | 實作 gen_l0()（子群組順序：r_group 在前） | Executor | DONE | 00_inbox/OT_Architecture_Framework_v1.0.md §5.1 R-D2-05；03_work/gen_d2.py（T09 完成） | 03_work/gen_d2.py（部分） | r_group 永遠第一個宣告（對應 L1.gw 在左側，R-D2-05）；solar 第二個；connected_to=null 的設備仍產生節點（連線在 T12 跳過） |
| T11 | 實作 gen_conn_backbone()（T-05 骨幹 label 去重） | Executor | DONE | 00_inbox/OT_Architecture_Framework_v1.0.md §5.1 T-05 R-D2-06；03_work/gen_d2.py（T10 完成） | 03_work/gen_d2.py（部分） | LAN-A 骨幹連線只有第一條保留 label，其餘置空 ""（T-05）；LAN-B 同理；所有連線使用 inline style（R-D2-09） |
| T12 | 實作 gen_conn_l0()（T-06 null 跳過）+ resolve_target() + emit_connection() | Executor | DONE | 00_inbox/OT_Architecture_Framework_v1.0.md §5.1 T-06 R-D2-09 R-D2-10；03_work/gen_d2.py（T11 完成） | 03_work/gen_d2.py（部分） | connected_to=null 完全不產生連線宣告（T-06）；resolve_target() 正確將 YAML key（如 "gw_A"、"rtu_TPC"）轉為 D2 路徑；emit_connection() 使用 inline style 且 label 無 \n（R-D2-10） |
| T13 | 整合 gen_d2.py 主程式 + CLI 介面 | Executor | DONE | 00_inbox/OT_Architecture_Framework_v1.0.md §5.1；03_work/gen_d2.py（T03~T12 完成） | 03_work/gen_d2.py（完整） | `python gen_d2.py project.yaml` 可執行；輸出 output.d2；驗證 L1 子群組宣告順序為 gw→rtu_panels→mcc→statcom；D2 源碼無語法錯誤（可用 d2 --dry-run 驗證） |
| T14 | gen_d2.py 整合測試（使用 Framework 範例 project.yaml） | Executor | DONE | 00_inbox/OT_Architecture_Framework_v1.0.md §4.2（project.yaml 範例）；03_work/gen_d2.py（T13 完成） | 03_work/test_output.d2；03_work/gen_d2_test_report.md | 節點數量符合 project.yaml 設定（6 feeders × 2 edge switch = 12 edge switch）；T-04 驗證通過（gw 在第一位）；T-05 驗證通過（骨幹只有第一條 label）；無 validate_config 報錯 |

---

## Phase 2：optimize_svg.py 實作

| ID | Task | Owner | Status | Input | Output | DoD |
|----|------|-------|--------|-------|--------|-----|
| T15 | 實作 parse_svg() + remove_d2_artifacts() + shift_content(+110px) | Executor | DONE | 00_inbox/OT_Architecture_Framework_v1.0.md §5.2 R-PP-01 §7；03_work/test_output.d2（T14 完成後 d2 render 產出） | 03_work/optimize_svg.py（部分） | 正確取得 bounding box；移除 D2 殘留 title/legend；所有主圖元素 y 座標位移 +110px；Title Bar 空間保留正確 |
| T16 | 實作 fix_dasharray() + inject_title_bar() | Executor | DONE | 00_inbox/OT_Architecture_Framework_v1.0.md §7 R-PP-02 R-PP-04；03_work/optimize_svg.py（T15 完成） | 03_work/optimize_svg.py（部分） | fix_dasharray() 正確修正所有 > 8 的 dasharray 為 6,4；Title Bar 高度 110px，背景 #0C3467，左側 6px #008EC3 裝飾條；三行文字規格符合 R-PP-02 |
| T17 | 實作 find_empty_zone() + inject_legend() | Executor | DONE | 00_inbox/OT_Architecture_Framework_v1.0.md §7 R-PP-03 R-PP-06；03_work/optimize_svg.py（T16 完成） | 03_work/optimize_svg.py（部分） | find_empty_zone() 以 100px 步進掃描，不硬編碼座標（R-PP-06）；Legend 為 480px 寬雙欄浮層，外框符合 R-PP-03；包含所有元件類型與連線類型 |
| T18 | 實作 add_label_backgrounds() + update_canvas() | Executor | DONE | 00_inbox/OT_Architecture_Framework_v1.0.md §7 R-PP-05；03_work/optimize_svg.py（T17 完成） | 03_work/optimize_svg.py（完整） | 識別含 CONN_KEYWORDS 的 label 並在前一行插入 rect；fill=white, fill-opacity=0.85, rx=2；update_canvas() 正確更新 viewBox height；輸出為 UTF-8 有效 SVG |
| T19 | optimize_svg.py 整合測試 | Executor | DONE | 03_work/test_output.d2（d2 render 後的 diagram_raw.svg）；03_work/optimize_svg.py（T18 完成） | 03_work/diagram_final.svg；03_work/optimize_svg_test_report.md | Title Bar 位於 y=0~110；Legend 為浮層（非頁尾）；所有連線 label 有白底；SVG 可在瀏覽器開啟；viewBox height 小於 diagram_raw.svg |

---

## Phase 3：check_collision.py 實作

| ID | Task | Owner | Status | Input | Output | DoD |
|----|------|-------|--------|-------|--------|-----|
| T20 | 實作 quick_collision_check() + CLI 輸出 | Executor | DONE | 00_inbox/OT_Architecture_Framework_v1.0.md §5.3；03_work/diagram_final.svg（T19 完成） | 03_work/check_collision.py | `python check_collision.py diagram_final.svg` 輸出 a_class 數量 + 受影響節點列表；Green/Yellow/Red 狀態判斷正確（< 1 / 1–4 / ≥ 5）；可用於 T21 驗收 |

---

## Phase 4：Makefile + 全流程驗收

| ID | Task | Owner | Status | Input | Output | DoD |
|----|------|-------|--------|-------|--------|-----|
| T21 | 建立 Makefile / run.sh 完整 pipeline | Executor | DONE | 00_inbox/OT_Architecture_Framework_v1.0.md §10.1；03_work/gen_d2.py；03_work/optimize_svg.py；03_work/check_collision.py | 03_work/Makefile；03_work/run.sh | `make all` 或 `bash run.sh project.yaml` 依序執行 Step 1–6；任一步驟失敗時中止並輸出錯誤訊息；最終輸出 diagram_final.svg |
| T22 | 全流程 End-to-End 測試（SOP Step 1–8） | Executor | DONE | 03_work/（T01~T21 全部完成）；00_inbox/OT_Architecture_Framework_v1.0.md §10.1 project.yaml 範例 | 03_work/e2e_test_report.md；03_work/diagram_final.svg | 依 §10.1 SOP 完整執行 8 步驟無報錯；a_class < 5；§12.3 自我檢驗 Checklist 全部打勾 |
| T23 | Reviewer 全域審查 | Reviewer | DONE | 03_work/（T01~T22 全部完成）；02_plan/acceptance.md | 04_review/review_report.md | 缺陷定位至具體檔案與行號；Critical/Major/Minor 分類正確 |
| T24 | 修正 Reviewer 指出的缺陷 | Executor | DONE | 04_review/review_report.md | 03_work/（對應修正） | 所有 🔴 Critical 缺陷修正完畢；重跑 T22 驗證無退化 |
| T25 | 打包 Release | Controller | DONE | 03_work/（T24 完成）；04_review/review_report.md | 05_release/ | 無 Critical 缺陷；05_release/ 含完整交付物；change_log.md 已更新；release_notes.md 存在 |

---

## 狀態統計

- TODO：0
- IN_PROGRESS：0
- DONE：25（T01~T25）
- BLOCKED：0

---

## Critical Path

T01 → T02 → T03 → T04 → T05 → T06 → T07 → T08 → T09 → T10 → T11 → T12 → T13 → T14 → T15 → T16 → T17 → T18 → T19 → T20 → T21 → T22 → T23 → T24 → T25

**可並行的任務：**
- T01 和 T02 可並行（均為 Phase 0 資料準備，相互獨立）
- T15~T18 內部需依序執行（optimize_svg.py 八步驟有順序依賴）
- T20（check_collision.py）可在 T14 完成後即開始，不必等 T19
