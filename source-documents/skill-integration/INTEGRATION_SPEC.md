# cbom-builder Skill 價格資料庫整合規格

> 本文件供 Skill 管理 Agent 使用，說明如何將歷史成交價資料整合至 cbom-builder Skill。

---

## 交付檔案清單

```
references/
├── price_lookup.json         # 產品價格摘要表 (1,829 筆) — 主查詢表
├── deprecated_products.json  # 廢棄產品替代關係 (38 筆)
└── brand_map.json            # 品牌代碼對照表 (199 筆)
```

### price_lookup.json 欄位說明

| 欄位 | 型態 | 說明 |
|------|------|------|
| `product_code` | string | 產品代碼 (ERP 料號) |
| `product_name` | string | 產品名稱（含型號） |
| `product_spec` | string | 規格描述 |
| `product_code_type` | string | `product` / `consumable` / `panel_material` |
| `brand_code` | string | 品牌代碼 |
| `brand_name` | string | 品牌全名（如「西門子 SIEMENS」） |
| `currency` | string | 幣別（TWD / EUR / USD / GBP / CHF） |
| `primary_supplier_name` | string | 主要供應商名稱 |
| `latest_unit_price` | float | 最近一次成交單價 |
| `latest_date` | string | 最近成交日期 (YYYY-MM-DD) |
| `avg_unit_price` | float | 歷史平均單價 |
| `median_unit_price` | float | 歷史中位單價 |
| `min_unit_price` | float | 歷史最低單價 |
| `max_unit_price` | float | 歷史最高單價 |
| `price_trend` | string | `rising` / `stable` / `falling` / `insufficient_data` |
| `confidence` | string | `high` / `medium` / `low` / `deprecated` |
| `total_transactions` | int | 歷史交易筆數 |
| `unique_suppliers` | int | 供應過的供應商數 |
| `is_deprecated` | bool | 是否已標記不再使用 |
| `replacement_code` | string | 替代產品代碼（若已廢棄） |

---

## SKILL.md 修改建議

### §4 定價邏輯 — 替換原有表格

將原有的 §4 表格替換為以下三層瀑布式定價邏輯：

```markdown
## 4. 定價邏輯

### 4.1 硬體設備定價（三層瀑布）

填入 CBOM 單價時，依以下優先順序查詢：

| 優先序 | 定價來源 | 使用條件 | 取價方式 | 精度 |
|--------|----------|----------|----------|------|
| 1 | 歷史成交價 (高信心) | `confidence` = `high` 或 `medium` | 取 `median_unit_price` | ±10% |
| 2 | 歷史成交價 (低信心) | `confidence` = `low` | 取 `median_unit_price`，備註標註「歷史價，僅供參考」 | ±20% |
| 3 | 市場估價 | 無歷史資料 | 台灣代理商市場價 ±10%（品牌官方建議售價 / 經銷報價） | ±20% |

**查詢方式**：在 `references/price_lookup.json` 中以產品型號或品牌名稱模糊比對。

**廢棄產品處理**：若查到的產品 `is_deprecated` = true，改用 `replacement_code` 指向的替代品價格。替代關係詳見 `references/deprecated_products.json`。

**價格趨勢提示**：
- `price_trend` = `rising`：備註「近期漲價趨勢，建議預留 5-10% 漲幅」
- `price_trend` = `falling`：備註「近期降價趨勢」
- `price_trend` = `stable`：無需額外備註

### 4.2 其他品項定價（不變）

| 品項類型 | 定價策略 | 資料來源 |
|----------|----------|----------|
| 軟體授權 | 年訂閱 or 永久授權；依授權數計算 | 原廠公開定價 |
| ISP 月費 | 商用固定 IP 光纖月租 | 台灣 ISP 商用方案（中華電信/遠傳等） |
| 工程人天 | `每天 = 8 小時` | 單日費率見 §5 |
| 差旅 | 高鐵/住宿/日支 | 公司差旅標準 |
| 風險準備金 | 設備+軟體+ISP 小計 × 3% | 固定比率 |
| 保固費 | 總設備金額 × 1% × 年數 | 固定比率 |
```

### §12 安全設備成本估算 — Hardware 列更新

將第 516 行的 Hardware 定價考量從：
```
| Hardware | 防火牆、IDS/IPS、Data Diode、安全交換器 | 台灣代理商市場價 ±10% |
```
改為：
```
| Hardware | 防火牆、IDS/IPS、Data Diode、安全交換器 | 歷史成交價優先（見 §4.1），無資料時台灣代理商市場價 ±10% |
```

### §9 / §14 品質檢查清單 — 新增價格來源追溯

在 Self-Check 表格末尾新增一行：

```
| 17 | 價格來源標示 | 每筆硬體單價備註欄標明來源：`[歷史]` / `[市場]` / `[TBD]` |
```

---

## 價格匹配建議邏輯

Skill 在填 BOM 時，建議的匹配流程：

```
1. 使用者提供設備型號（如 "FortiGate 60F"）
2. 在 price_lookup.json 中搜尋：
   a. product_name 包含型號 → 精確匹配
   b. brand_name 包含品牌名 → 品牌匹配，列出該品牌所有產品供選擇
   c. product_spec 包含關鍵字 → 規格匹配
3. 若找到多筆，取 confidence 最高、latest_date 最近的一筆
4. 若完全找不到，退回市場估價模式
```

---

## 資料涵蓋範圍

| 屬性 | 值 |
|------|------|
| 時間跨度 | 2024-01-01 ~ 2026-03-18 |
| 產品數量 | 1,829（排除費用類） |
| 品牌數 | 199 |
| 幣別 | TWD (97.2%), EUR, USD, GBP, CHF |
| 信心分布 | high: 96, medium: 1,079, low: 616, deprecated: 38 |
| 資料來源 | ERP 牌價表匯出（含詢價與實際成交價） |
| 建議更新頻率 | 每季 |

---

## 注意事項

1. **幣別轉換**：price_lookup.json 中 97.2% 為 TWD，少量 EUR/USD 品項需在 BOM 中按匯率換算
2. **C 開頭代碼是費用類**（運費、折扣等），已排除在 price_lookup.json 之外
3. **B 開頭代碼是耗材**（如點工外包費），`product_code_type` = `consumable`
4. **盤廠物料碼**（英文長碼如 `TT132P04P2KS01`），`product_code_type` = `panel_material`，為策略供應鏈管理處專用
5. **price_lookup.json 體積**：約 1.5 MB，可直接打包進 .skill 檔
