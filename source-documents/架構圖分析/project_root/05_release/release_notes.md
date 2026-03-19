# Release Notes — OT 架構圖自動化工具鏈 v1.0.0

發布日期：2026-03-04
狀態：正式發布

---

## 版本號

**v1.0.0**（初始發布）

---

## 交付物清單

| 檔案 | 說明 |
|------|------|
| `gen_d2.py` | D2 源碼產生器（YAML → .d2），Python 3.9+，CLI |
| `optimize_svg.py` | SVG 後製腳本（8 步驟 pipeline），CLI |
| `check_collision.py` | A 類碰撞快速檢查，線段距離演算法，CLI |
| `component_library.yaml` | 設備元件庫，10 個標準設備定義 |
| `project_template.yaml` | project.yaml 模板（含 inline 中文說明） |
| `Makefile` | GNU Make 版本 pipeline |
| `run.sh` | Bash 版本 pipeline（跨平台） |
| `diagram_final.svg` | 範例輸出（project_test.yaml，6 feeders，PRP 開啟） |

---

## 快速開始

```bash
# 1. 複製模板
cp project_template.yaml myproject.yaml

# 2. 編輯 myproject.yaml（填入設備、連線資訊）

# 3. 執行 pipeline
bash run.sh myproject.yaml mydiagram

# 或使用 Makefile
make all PROJECT=myproject.yaml SVG_FINAL=mydiagram_final.svg
```

---

## 系統需求

| 項目 | 最低版本 |
|------|---------|
| Python | 3.9+ |
| d2 CLI | 0.6.0+ |
| PyYAML | 5.0+ |

安裝相依套件：
```bash
pip install pyyaml
```

---

## 已實作的 Rulebook 規則

### 拓撲規則（T-01~T-08）
- T-01：PRP/HSR 冗餘 edge switch 動態展開
- T-02：HMI 數量控制（A/B 雙機）
- T-03：Protocol Gateway 數量控制
- T-04：L1 子群組宣告順序強制（gw → rtu → mcc → statcom）
- T-05：骨幹連線 label 去重
- T-06：connected_to=null 完全跳過連線
- T-07：enterprise=false 省略 L4 Zone
- T-08：statcom=false 省略 STATCOM 子群組

### D2 語法規則（R-D2-01~R-D2-10）
- R-D2-01：強制 dagre 佈局引擎
- R-D2-02：禁止 title/legend D2 節點
- R-D2-03：L1 gw 子群組強制第一
- R-D2-04：A 類碰撞 = 0（Green）
- R-D2-05：L0 r_group 在前
- R-D2-06：骨幹 label 去重
- R-D2-08：classes 區塊包含所有設備 class
- R-D2-09：連線使用 inline style
- R-D2-10：連線 label 無換行字元

### SVG 後製規則（R-PP-01~R-PP-06）
- R-PP-01：8 步驟依序執行（不可跳過）
- R-PP-02：Title Bar 110px / #0C3467 / 左側 6px Sky Blue
- R-PP-03：Legend 浮層，動態定位
- R-PP-04：dasharray > 8 修正為 6,4
- R-PP-05：連線 label 白底墊底
- R-PP-06：Legend 位置不硬編碼

### 品牌色碼（R-BR-01~R-BR-02）
- Navy #0C3467、Sky #008EC3、Amber #F5A623
- Gray #9B9B9B、Red #c0392b、Green #2e7d32

---

## 已知限制

1. **SVG 後製依賴正規表達式解析**：不使用完整 XML 解析器，複雜嵌套結構可能有邊界情況。
2. **碰撞檢查為靜態分析**：基於文字元素座標與 path 線段距離，不模擬 D2 佈局引擎的實際碰撞解算。
3. **Legend 位置演算法**：以 100px 步進掃描，極度密集的圖表可能 fallback 至固定座標 (30, y_start)。
4. **comm_styles 必要 key**：project.yaml 必須定義完整的 13 個 comm_styles key（validate_config 會提前報錯）。
5. **Windows 環境**：需確保 Python stdout 為 UTF-8（check_collision.py 已自動處理）。

---

## 測試覆蓋

| 場景 | 結果 |
|------|------|
| 6 feeders + PRP 開啟 + STATCOM + enterprise | ✅ Green a_class=0 |
| validate_config 偵測無效 comm key | ✅ 輸出具體錯誤訊息 |
| connected_to=null 跳過連線 | ✅ 無多餘連線宣告 |
| hmi_count=2 主備 HMI | ✅ HMI_A/B 正確展開 |

---

_由 OT 架構圖自動化工具鏈 Executor Agent 產生，版本 v1.0.0，日期 2026-03-04。_
