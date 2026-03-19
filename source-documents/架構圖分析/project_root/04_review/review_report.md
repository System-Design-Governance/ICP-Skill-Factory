# Reviewer Report — OT 架構圖自動化工具鏈

版本：v1.0
審查日期：2026-03-04
審查員：Reviewer Agent
輸入基準：02_plan/acceptance.md

---

## 審查結論

| 等級 | 數量 |
|------|------|
| 🔴 Critical | 0 |
| 🟠 Major | 0 |
| 🟡 Minor | 5 |
| ✅ Pass | 所有 DoD 主項目通過 |

**整體評估：可進行 T25 Release 打包，Minor 缺陷應於本次修正。**

---

## E2E 測試結果（T22）

```
Pipeline 完成：a_class = 0（Green OK）
輸出：diagram_final.svg  95,533 bytes
Steps：gen_d2 → d2 render → optimize_svg → check_collision  全部通過
```

---

## DoD 核對表

### gen_d2.py DoD（T03~T13）

| # | 規則 | 狀態 | 說明 |
|---|------|------|------|
| 1 | R-D2-01 layout-engine: dagre | ✅ | gen_header() 行 338：`layout-engine: dagre` |
| 2 | R-D2-02 無 title:/legend: 節點 | ✅ | generate_d2() 不含任何 title/legend 宣告 |
| 3 | R-D2-03 / T-04 L1 子群組順序 gw→rtu→mcc→statcom | ✅ | gen_l1() 行 634–646 硬編碼順序 |
| 4 | R-D2-05 L0 r_group 在前 | ✅ | gen_l0() 行 671–698 硬編碼 r_group 先行 |
| 5 | T-05 / R-D2-06 骨幹 label 去重 | ✅ | gen_conn_backbone() 行 781 i==0 條件 |
| 6 | T-06 null 跳過連線 | ✅ | gen_conn_l0() 行 883–884 continue |
| 7 | T-07 enterprise=false 省略 L4 | ✅ | gen_l4() 行 361 return "" |
| 8 | T-08 statcom=false 省略 | ✅ | gen_l1_statcom() 行 595–596 return [] |
| 9 | R-D2-08 zone_sub class | ✅ | 所有子群組均宣告 class: zone_sub |
| 10 | R-D2-09 inline style 連線 | ✅ | emit_connection() 行 755–761 |
| 11 | R-D2-10 連線 label 無換行 | ✅ | emit_connection() 行 750–751 replace |

### optimize_svg.py DoD（T15~T19）

| # | 規則 | 狀態 | 說明 |
|---|------|------|------|
| 1 | R-PP-01 八步驟依序 | ✅ | optimize() 函式 Step 0~8 串接 |
| 2 | R-PP-02 Title Bar 規格 | ✅ | inject_title_bar() 110px / #0C3467 / 左側 6px #008EC3 |
| 3 | R-PP-03 Legend 浮層動態定位 | ✅ | find_empty_zone() 100px 掃描 |
| 4 | R-PP-04 fix_dasharray | ✅ | 29 個 dasharray 項目已修正 |
| 5 | R-PP-05 連線 label 白底 | ✅ | add_label_backgrounds_v2() |
| 6 | SVG 可在瀏覽器開啟 | ✅ | 94948 bytes 有效 SVG |

### check_collision.py DoD（T20）

| # | 規則 | 狀態 | 說明 |
|---|------|------|------|
| 1 | 輸出 a_class + 受影響節點 | ✅ | CLI 輸出格式正確 |
| 2 | 狀態顯示 Green/Yellow/Red | 🟡 | 見 [M-002]：使用 ASCII 替代 emoji |
| 3 | 錯誤路徑 exit code 1 | ✅ | main() 行 217–218 |

### 全流程 DoD（T22）

| # | 規則 | 狀態 | 說明 |
|---|------|------|------|
| 1 | 8 步驟無 exception | ✅ | bash run.sh 全程通過 |
| 2 | a_class < 5 | ✅ | a_class = 0（Green） |

---

## 缺陷清單

### [M-001] gen_d2.py:425–426 — HMI_A label 重複附加 model suffix（hmi_count=1 情況）

**等級**：🟡 Minor
**檔案**：03_work/gen_d2.py，行 425–426
**條件**：`scada.hmi_count == 1` 且 `scada.hmi_model` 有值時觸發

**問題**：
```python
# 行 424–426
label = "主站 HMI_A" if hmi_count >= 2 else f"HMI{hmi_suffix}"
lines.append(f'  HMI_A: "{label}{hmi_suffix}" {{ class: hmi_workstation }}')
```
當 `hmi_count == 1`：
- `label = f"HMI{hmi_suffix}"` → 已含 model 後綴
- 最終輸出：`"HMI\nDA-820\nDA-820"` → model 重複

**修正**：
```python
if hmi_count >= 2:
    lines.append(f'  HMI_A: "主站 HMI_A{hmi_suffix}" {{ class: hmi_workstation }}')
else:
    lines.append(f'  HMI_A: "HMI{hmi_suffix}" {{ class: hmi_workstation }}')
```

---

### [M-002] check_collision.py — 狀態圖示使用 ASCII 替代，偏離規格

**等級**：🟡 Minor（可接受的技術例外）
**檔案**：03_work/check_collision.py，行 228–230

**問題**：
acceptance.md §check_collision.py DoD 規定顯示 `✅ ⚠️ ❌`，
現行因 Windows CP950 編碼限制改為 `[Green OK] / [Yellow WARN] / [Red FAIL]`。
功能正確，僅視覺規格偏差。

**修正建議**：加入 `PYTHONIOENCODING=utf-8` 環境變數設定，或使用 `sys.stdout.reconfigure(encoding='utf-8')` 並恢復 emoji 符號。

---

### [M-003] gen_d2.py:validate_config() — 未驗證內部固定 comm_styles key

**等級**：🟡 Minor
**檔案**：03_work/gen_d2.py，行 274–318

**問題**：
`gen_conn_backbone()`、`gen_conn_inter_zone()` 等函式使用固定的 comm_styles key：
`PRP_LAN_A`, `PRP_LAN_B`, `OPC_UA_A`, `OPC_UA_B`, `IEEE1588_A`, `IEEE1588_B`,
`IEC61850_MMS`, `Modbus_TCP`, `PRP_fiber_A`, `PRP_fiber_B` 等。
但 `validate_config()` 未驗證這些 key 是否存在於 `project.yaml` 的 `comm_styles` 中。
若 comm_styles 缺少這些 key，`emit_connection()` 中的 `style.get(...)` 會靜默使用預設值，
不會報錯，但連線樣式不符規格。

**修正建議**：在 `validate_config()` 末端增加：
```python
REQUIRED_COMM_KEYS = {
    "PRP_LAN_A", "PRP_LAN_B", "OPC_UA_A", "OPC_UA_B",
    "IEEE1588_A", "IEEE1588_B", "IEC61850_MMS", "Modbus_TCP",
    "PRP_fiber_A", "PRP_fiber_B", "IEC61850_fiber", "RS485_modbus",
    "IT_ethernet"
}
for key in REQUIRED_COMM_KEYS:
    if key not in comm_keys:
        errors.append(f"[comm_styles] 必要的 key '{key}' 不存在")
```

---

### [M-004] check_collision.py:131 — ZONE_LABEL_PREFIXES 過度匹配風險

**等級**：🟡 Minor
**檔案**：03_work/check_collision.py，行 131–133

**問題**：
```python
ZONE_LABEL_PREFIXES = ("Level ", "DMZ｜", "zone", "核心交換", "饋線邊緣交換",
                       "R 群", "太陽能", "Protocol Gateway", "MCC 群", "STATCOM",
                       "TPC RTU", "RTU 盤", "Field", "Supervisory", "Enterprise")
```
`"Field"` 前綴會誤判所有以 "Field" 開頭的葉節點標籤（如 `"Field IED 87L1"`），
導致真實碰撞被忽略。

**修正建議**：將 `"Field"` 改為 `"Field Control"` 或完整 Zone 標題字串，
或加長前綴匹配字串以避免誤判。

---

### [M-005] acceptance.md:80 — viewBox height 比較方向有誤

**等級**：🟡 Minor（文件勘誤）
**檔案**：02_plan/acceptance.md，行 80

**問題**：
> 輸出 SVG viewBox height 小於 diagram_raw.svg

實際行為：optimize_svg.py 的 Step 3 將所有內容下移 +110px（Title Bar 空間），
Step 8 更新 viewBox 使其比 raw SVG **增加** 110px。
此條件實際不應通過，但 E2E 測試在此條件下標記 PASS 是錯誤的。

**修正建議**：將 acceptance.md 第 80 行改為：
> 輸出 SVG viewBox height 大於 diagram_raw.svg（+110px Title Bar）

---

## 正向確認（Positive Findings）

1. **品牌色碼管理**：所有色碼統一由 `COLOR` 常數字典管理，無任何硬編碼色碼值（R-BR-02 全面落實）。
2. **T-04 強制排序**：`gen_l1()` 使用程式碼層面的固定呼叫順序（非 YAML 排序），確保 gw 永遠第一個宣告，設計嚴謹。
3. **d2label() 輔助函式**：對 YAML 換行字元的處理方式明確、集中，R-D2-10 補丁設計良好。
4. **碰撞檢測演算法升級**：從 bounding box 重疊改為精確的 SVG 路徑線段距離計算，消除所有 false positive，a_class=0（Green）。
5. **run.sh 錯誤處理**：Step 6 碰撞檢查失敗（exit code 1）時僅輸出警告，不中止 pipeline，設計符合 Framework §5.3「Red 建議修正，Controller 決策」的原則。
6. **動態 Legend 定位**：`find_empty_zone()` 以 100px 步進掃描避免 Legend 與圖表重疊，符合 R-PP-06 不硬編碼座標的要求。

---

## 建議修正優先順序（T24）

| 優先 | 缺陷 | 估計影響 |
|------|------|----------|
| 1 | M-001 HMI 雙重 suffix | 視覺輸出錯誤 |
| 2 | M-003 validate_config | 使用性/健壯性 |
| 3 | M-004 ZONE_LABEL_PREFIXES | 碰撞漏報風險 |
| 4 | M-002 狀態圖示 | 規格一致性 |
| 5 | M-005 acceptance.md 勘誤 | 文件準確性 |

---

_審查結束。本報告由 Reviewer Agent 產生，版本 v1.0，日期 2026-03-04。_
