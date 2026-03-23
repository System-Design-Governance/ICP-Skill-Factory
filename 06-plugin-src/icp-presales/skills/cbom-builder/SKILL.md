---
name: cbom-builder
description: >
  Build Commercial Bill of Materials (CBOM) for IT/OT/cybersecurity infrastructure projects.
  Fills company BOM Excel templates (CF-SR-03-01 or similar) with standardized pricing logic,
  labor estimation baselines, and currency handling rules. Also supports standalone markdown BOM
  when no company template is available.
  MANDATORY TRIGGERS: BOM, CBOM, 物料清單, bill of materials, 成本估算, cost estimation,
  BOM估算, 報價, quotation, 填BOM, BOM template, 設備清單, equipment list, 估價,
  pricing estimate, 工時估算, labor estimation, 工時估算基準, labor hour estimation, 人天估算,
  person-day estimation, IEC 62543 安全設備, security equipment cost, Gate 0 CBOM,
  安全成本, security cost breakdown, RFI response cost.
  Use this skill whenever the user wants to create, update, or review a commercial BOM for
  an infrastructure project. Also trigger when the user needs to fill a company BOM template,
  estimate project costs, or produce an equipment/labor pricing breakdown.
---

# CBOM 填表規範

本 Skill 定義商務物料清單的欄位對應、定價邏輯、工時估算基準與幣別處理規則。適用於資安、網路、IT/OT 基礎設施、實體安全等系統整合專案的成本估算。

精度定位：Presales 高階估算級 (±20%)。

---

## 1. 初始化

使用前先確認：

1. **是否有公司 BOM 模板**：優先檢查本 Skill 附帶的 `templates/CF-SR-03-01.xlsx`；若使用者另外提供了模板，則使用使用者版本
2. **報價幣別**：TWD / USD / EUR / other（向使用者確認）
3. **業主預算**：已知（金額）/ 未提供（自行估算）
4. **營運期間**：合約月數（影響月費類品項的數量計算）

---

## 2. 公司 BOM 模板欄位對應

以 CF-SR-03-01 模板為基準。若使用其他模板，需先分析其 sheet 結構再對應。

### 2.1 參數設定 sheet

| 欄位 | 對應來源 | 格式要求 |
|------|----------|----------|
| 專案代號 | 專案名稱縮寫 | `{客戶}-{年份}`（如 `DFO-2026`） |
| 版本 | 執行批次 | `v{主版本}.{修訂}`（如 `v1.0`） |
| 營運期間 | 合約期間 | 月份數（如 `12`） |
| 幣別 | 使用者選擇 | `TWD` / `USD` / `EUR` |
| 業主預算 | 已知則填入；未知填 `N/A` | 數值或 `N/A` |

### 2.2 BOM sheet — Group 分類規則

| Group | 包含品項 | CBOM 編號前綴 |
|-------|----------|---------------|
| 項目 | 硬體設備 + 軟體授權 + ISP/通訊 | CBOM-H01~Hnn, CBOM-S01~Snn |
| 工程安裝 | 設備安裝、佈線、系統設定、門禁安裝 | 無前綴，用描述 |
| 規劃設計 | HLD/LLD、Gap Analysis、偏差聲明、事件程序設計 | 無前綴，用描述 |
| 現場任務 | 場勘、FAT/SAT、訓練、竣工/營運文件、月維護、退場 | 無前綴，用描述 |
| 專案管理 | PM 人天、差旅交通、風險準備金、保固費、保險 | 無前綴，用描述 |

**品項排列順序**（每個 Group 內）：先核心設備、再周邊、再線材配件。非字母排序。

---

## 3. 欄位填寫規則

| 欄位名稱 | 模板欄位 | 填寫規則 |
|----------|----------|----------|
| 品項名稱 | Column B (品名) | 中文為主，括號內附英文型號（如有） |
| 品項描述 | Column C (規格描述) | 1-2 行，含關鍵規格 |
| 數量 | Column J (數量) | 整數；月費類用月份數作為數量 |
| 單位 | Column K (單位) | `台` / `套` / `組` / `月` / `天` / `式` / `趟` |
| 單價 | Column L (單價) | 不含稅原幣金額 |
| 小計 | Column M (小計) | 公式 `=J{n}*L{n}`（非手動填入） |
| 備註 | Column N (備註) | 選填，說明假設或替代品 |

**格式要求**：
- 每個 Group 之間空一行
- Group 標題行加粗
- 空值欄位不留空白，填 `—` 或 `N/A`

---

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

**價格匹配流程**：
1. 使用者提供設備型號（如 "FortiGate 60F"）
2. 在 price_lookup.json 中搜尋：
   a. `product_name` 包含型號 → 精確匹配
   b. `brand_name` 包含品牌名 → 品牌匹配，列出該品牌所有產品供選擇
   c. `product_spec` 包含關鍵字 → 規格匹配
3. 若找到多筆，取 `confidence` 最高、`latest_date` 最近的一筆
4. 若完全找不到，退回市場估價模式

### 4.2 其他品項定價

| 品項類型 | 定價策略 | 資料來源 |
|----------|----------|----------|
| 軟體授權 | 年訂閱 or 永久授權；依授權數計算 | 原廠公開定價 |
| ISP 月費 | 商用固定 IP 光纖月租 | 台灣 ISP 商用方案（中華電信/遠傳等） |
| 工程人天 | `每天 = 8 小時` | 單日費率見 §5 |
| 差旅 | 高鐵/住宿/日支 | 公司差旅標準 |
| 風險準備金 | 設備+軟體+ISP 小計 × 5% | 固定比率（F6 EPCI 實績校正：大型案 5%，中小型案可維持 3%） |
| 保固費 | 總設備金額 × 2% × 年數 | 固定比率（F6 EPCI 實績校正：含 OT 設備維護溢價） |

**注意**：
- ISP 月費必須使用商用方案價格，不可用家用方案（差異可達 5-10 倍）
- 軟體授權若為年訂閱制，數量 = 授權數 × 年數
- 風險準備金和保固費放在「專案管理」Group

---

## 5. 工時估算基準

以下為 Presales 階段（±20% 精度）的標準工時參考值：

| 工作項目 | 估算基準 | 典型範圍 |
|----------|----------|----------|
| 現場場勘 | 每次 1 天 + 交通 | 1-2 趟 |
| 設備安裝 (網路) | 每 10 台設備 ≈ 1 天 | 1-3 天 |
| 設備安裝 (門禁) | 每 2 門 ≈ 1 天 | 1-3 天 |
| 佈線工程 | 每 20 點 ≈ 1 天 | 2-5 天 |
| 系統設定 (FW/SW/AP) | 全套 ≈ 2-4 天 | 含測試 |
| HLD/LLD 設計 | 中型案 ≈ 5-8 天 | 依複雜度 |
| Gap Analysis | 每份標準 ≈ 3-5 天 | IEC 62443 / ISO 27001 |
| FAT/SAT | FAT 2天 + SAT 2天 | 含文件 |
| 訓練 | 每場 0.5-1 天 | 1-3 場 |
| 營運文件編製 | 中型案 ≈ 3-5 天 | SOP/維護手冊等 |
| PM/合規文件 | 中型案 ≈ 2-3 天 | 合規報告/驗收文件 |
| 月維護 | 每月 0.5-1 天 | 依合約 |
| 退場 | 2-3 天 | 含資料銷毀 |

**每日費率參考（台灣市場）**：
- 資深工程師：TWD 8,000-12,000/天
- 專案經理：TWD 10,000-15,000/天
- 資安顧問：TWD 12,000-18,000/天

**案型規模參考**：
- 小型案（< 20 設備）：總工時 30-60 天
- 中型案（20-100 設備）：總工時 60-150 天
- 大型案（> 100 設備）：總工時 150+ 天

---

## 6. 幣別處理

| 場景 | 處理規則 |
|------|----------|
| 全案 TWD | 所有品項直接以 TWD 填入 |
| 全案 USD | 所有品項以 USD 填入，匯率寫在參數設定 sheet |
| 混合幣別 | BOM 統一以一種幣別填入（使用者決策幣別），外幣品項在備註註明原幣金額與匯率 |
| ISP 月費 | 台灣 ISP 一律用 TWD，即使主幣別為 USD |

---

## 7. 公式與計算規則

- 新增行一律使用簡單公式 `=J{n}*L{n}`（不使用 Structured Table Reference）
- 模板既有的結構化表格公式（如 `=[@數量]*[@單價]`）保留不動
- 分析 sheet（計算、標案分析等）保留原有公式，不手動修改
- 使用 openpyxl 操作 Excel 時，注意：
  - 新增行插入在 BOM 表格的末尾（最後一個 Group 之後）或各 Group 末尾
  - 避免修改模板既有的 ArrayFormula 和命名範圍
  - 公式使用 A1 格式（如 `=J5*L5`），不用 R1C1
- 最終交付時註明「請以 Microsoft Excel 開啟以確保所有公式正確計算」

---

## 8. Excel 格式規範（CF-SR-03-01 模板專用）

本章定義使用 openpyxl 操作公司 BOM 模板時的格式規則，確保產出檔案在 Excel 中開啟時與原始模板視覺一致。

### 8.1 模板結構（原始 BOM sheet）

```
Row 1-3: 標題區（專案代號、版本等，由參數設定 sheet 連結）
Row 4:   欄位標題列（NO, Classification, Group, Type, ... Total Cost）
Row 5:   **** 項目 ****         ← Group Header（黃底）
Row 6-7: 項目 data rows（模板預留 2 行）
Row 8:   **** 工程安裝 ****     ← Group Header（黃底）
Row 9-10: 工程安裝 data rows
Row 11:  **** 規劃設計 ****     ← Group Header（黃底）
Row 12-13: 規劃設計 data rows
Row 14:  **** 現場任務 ****     ← Group Header（黃底）
Row 15-16: 現場任務 data rows
Row 17:  **** 專案管理 ****     ← Group Header（黃底）
Row 18-26: 專案管理 data rows（模板預留 9 行）
Row 27:  **** 追加 ****         ← 紅底（變更單用）
Row 35:  **** 追減 ****         ← 紅底（變更單用）
Row 41:  **** 臨櫃採購 ****     ← 特殊色
```

### 8.2 Group Header 格式規則

**⚠️ 所有「本案」Group（項目/工程安裝/規劃設計/現場任務/專案管理）的標題行必須使用黃底，不可使用紅底。紅底僅用於「追加/追減」變更單區域。**

| 屬性 | 值 |
|------|------|
| 文字格式 | `**** {Group名} ****`（前後各 4 個星號 + 空格） |
| 文字位置 | Column G (第 7 欄) |
| 填充顏色 | `PatternFill(start_color='FFFFFF00', fill_type='solid')` （黃色） |
| 填充範圍 | Column D 至 Column M（第 4-13 欄） |
| 字型 | `Font(name='微軟正黑體', size=10, bold=True)` |

**Python 範例**：
```python
from openpyxl.styles import PatternFill, Font

YELLOW_FILL = PatternFill(start_color='FFFFFF00', fill_type='solid')
GROUP_FONT = Font(name='微軟正黑體', size=10, bold=True)

def format_group_header(ws, row, group_name):
    """設定 Group 標題行格式"""
    ws.cell(row=row, column=7).value = f'**** {group_name} ****'
    for col in range(4, 14):  # D(4) to M(13)
        cell = ws.cell(row=row, column=col)
        cell.fill = YELLOW_FILL
        cell.font = GROUP_FONT
```

### 8.3 資料行格式規則

**⚠️ 所有新增的資料行必須明確設定字型與對齊方式，不可依賴系統預設（Linux 環境下預設字型為 DejaVu Sans，對齊為 None）。`insert_rows()` 產生的新行不會繼承任何格式，必須逐欄手動設定。**

#### 8.3.1 字型規則（依欄位區分粗細）

原始模板的資料行**並非統一字型**，各欄粗細不同：

| 欄位 | Column | 字型 | 說明 |
|------|--------|------|------|
| NO | C (3) | `Font(name='微軟正黑體', size=9, bold=True)` | 較小字，粗體 |
| Classification ~ Qty | D-J (4-10) | `Font(name='微軟正黑體', size=10, bold=True)` | 標準粗體 |
| Unit | K (11) | `Font(name='微軟正黑體', size=10, bold=False)` | 非粗體 |
| Cost / Total Cost | L-M (12-13) | `Font(name='微軟正黑體', size=10, bold=False)` | 非粗體 |
| 其餘欄 (N-S) | N-S (14-19) | `Font(name='微軟正黑體', size=10, bold=True)` | 延伸欄粗體 |

#### 8.3.2 對齊規則（必須明確設定）

| 欄位 | Column | 水平 | 垂直 | wrap_text |
|------|--------|------|------|-----------|
| NO | C (3) | center | center | False |
| Classification | D (4) | center | center | False |
| Group | E (5) | center | center | False |
| 本案_追加 | F (6) | center | center | False |
| Type | G (7) | left | center | **True** |
| Description | H (8) | left | center | **True** |
| Manufacture | I (9) | center | center | False |
| Qty | J (10) | center | center | False |
| Unit | K (11) | center | center | False |
| Cost(未稅) | L (12) | left | center | False |
| Total Cost | M (13) | left | center | False |

#### 8.3.3 數字格式

| 欄位 | Column | number_format |
|------|--------|---------------|
| Cost(未稅) | L (12) | `"NT$"#,##0` |
| Total Cost | M (13) | `"NT$"#,##0` |

⚠️ 格式必須含 `NT$` 前綴，不可使用簡化的 `#,##0`。

#### 8.3.4 背景色

所有資料行**無填充**（透明），不可套用任何背景顏色。

**Python 範例**：
```python
from openpyxl.styles import Font, Alignment

# 依欄位粗細分三種字型
FONT_NO   = Font(name='微軟正黑體', size=9, bold=True)    # Col C
FONT_BOLD = Font(name='微軟正黑體', size=10, bold=True)   # Col D-J, N-S
FONT_THIN = Font(name='微軟正黑體', size=10, bold=False)  # Col K-M

# 各欄對齊方式
ALIGN_CC  = Alignment(horizontal='center', vertical='center')
ALIGN_LC  = Alignment(horizontal='left', vertical='center')
ALIGN_LCW = Alignment(horizontal='left', vertical='center', wrap_text=True)

def format_data_row(ws, row):
    """設定資料行格式（字型+對齊+數字格式，完整覆蓋模板規則）"""
    # Col C: NO
    ws.cell(row=row, column=3).font = FONT_NO
    ws.cell(row=row, column=3).alignment = ALIGN_CC
    # Col D-F: Classification, Group, 本案
    for col in [4, 5, 6]:
        ws.cell(row=row, column=col).font = FONT_BOLD
        ws.cell(row=row, column=col).alignment = ALIGN_CC
    # Col G-H: Type, Description (left + wrap)
    for col in [7, 8]:
        ws.cell(row=row, column=col).font = FONT_BOLD
        ws.cell(row=row, column=col).alignment = ALIGN_LCW
    # Col I-J: Manufacture, Qty
    for col in [9, 10]:
        ws.cell(row=row, column=col).font = FONT_BOLD
        ws.cell(row=row, column=col).alignment = ALIGN_CC
    # Col K: Unit (non-bold)
    ws.cell(row=row, column=11).font = FONT_THIN
    ws.cell(row=row, column=11).alignment = ALIGN_CC
    # Col L-M: Cost, Total Cost (non-bold, NT$ format)
    for col in [12, 13]:
        ws.cell(row=row, column=col).font = FONT_THIN
        ws.cell(row=row, column=col).alignment = ALIGN_LC
        ws.cell(row=row, column=col).number_format = '"NT$"#,##0'
    # Col N-S: 延伸欄（bold）
    for col in range(14, 20):
        ws.cell(row=row, column=col).font = FONT_BOLD
        ws.cell(row=row, column=col).alignment = ALIGN_LC
```

### 8.4 行插入策略

原始模板每個 Group 只預留 2 行（專案管理預留 9 行），實際品項通常遠多於此。插入策略：

1. **定位 Group Header 行**：掃描 Column G 找 `****` 標記
2. **計算需要插入的行數**：`所需行數 - 模板預留行數`
3. **在 Group 的最後一個預留行之後插入新行**：使用 `ws.insert_rows(row, count)`
4. **插入後重新設定格式**：`insert_rows` 不會自動複製格式，必須手動設定每個新行的字型
5. **更新後續 Group Header 位置**：插入行後下方所有行的 row index 會偏移

**⚠️ 插入行的順序：由下往上**。先處理最下方的 Group（專案管理），最後處理最上方的 Group（項目），這樣不會影響尚未處理的 Group 的 row index。

**Python 範例**：
```python
def insert_data_rows(ws, after_row, count):
    """在指定行之後插入 count 行，並設定格式"""
    ws.insert_rows(after_row + 1, count)
    for i in range(count):
        row = after_row + 1 + i
        format_data_row(ws, row)
```

### 8.4.1 ⚠️ 關鍵：更新結構化表格範圍（防止 Excel 開檔錯誤）

**問題根因**：BOM sheet 包含一個 Excel 結構化表格（Structured Table）名為 `表格_BOM`，原始範圍為 `B4:X44`。當 openpyxl 用 `insert_rows()` 插入新行後，工作表的儲存格確實增加了，但 `表格_BOM` 的 `ref` 屬性（定義表格範圍）和 `autoFilter.ref` 不會自動更新。Excel 開檔時偵測到「表格定義的範圍」與「實際資料行數」不符，就會彈出「我們發現內容有問題，是否嘗試復原」的錯誤提示。

**修復方法**：在所有行插入和資料填寫完成後，必須手動更新 `表格_BOM` 的範圍。

**Python 修復程式碼**：
```python
def fix_table_range(ws, table_name='表格_BOM'):
    """
    修正結構化表格範圍，使其與實際資料行數一致。
    必須在所有 insert_rows() 和資料填寫完成之後呼叫。
    """
    # 找到表格物件（注意：迭代 ws.tables 回傳的是 str 名稱，不是 Table 物件）
    table = None
    if table_name in ws.tables:
        table = ws.tables[table_name]

    if table is None:
        print(f"Warning: Table '{table_name}' not found")
        return

    # 計算實際最後一行（含 totals row）
    last_data_row = ws.max_row

    # 更新 table ref（保持起始欄位不變，只更新結束行號）
    # 原始格式：B4:X44 → B4:X{new_last_row}
    import re
    old_ref = table.ref
    match = re.match(r'([A-Z]+\d+):([A-Z]+)(\d+)', old_ref)
    if match:
        start = match.group(1)       # B4
        end_col = match.group(2)     # X
        new_ref = f'{start}:{end_col}{last_data_row}'
        table.ref = new_ref

        # 更新 autoFilter 範圍（排除 totals row）
        if table.autoFilter:
            if table.totalsRowCount:
                filter_last = last_data_row - table.totalsRowCount
            else:
                filter_last = last_data_row
            table.autoFilter.ref = f'{start}:{end_col}{filter_last}'

        print(f"Table '{table_name}' range updated: {old_ref} → {new_ref}")
```

**呼叫時機**：在 `wb.save()` 之前呼叫一次即可。

```python
# ... 所有行插入和資料填寫完成 ...

# 修正表格範圍（必須在 save 之前）
fix_table_range(ws, '表格_BOM')

wb.save('03_work/cbom.xlsx')
```

**其他 sheet 的表格**：模板中共有 8 個結構化表格。BOM sheet 的 `表格_BOM` 是唯一會因插入行而受影響的表格。其他 sheet（01參數設定、03成本統計表、報價分析等）的表格範圍是固定的，不需要修改。

### 8.5 欄位標題列參考

| 欄 | 字母 | 欄位名稱 | 填入內容 |
|----|------|----------|----------|
| 2 | B | (checkbox) | 保留空白，模板公式控制 |
| 3 | C | NO | 流水號（整數） |
| 4 | D | Classification | `工程材料（硬體）`/`工程材料（軟體）`/`施工_外包費`/`人工`/`差旅費`/`運輸費`/`保險費` |
| 5 | E | Group | `項目`/`工程安裝`/`規劃設計`/`現場任務`/`專案管理` |
| 6 | F | 本案_追加 | `本案`（固定值） |
| 7 | G | Type | 品項英文短名（如 `Edge Firewall`） |
| 8 | H | Functional Description | 品項中文描述（如 `FortiGate 60F UTM防火牆`） |
| 9 | I | Manufacture | 廠牌（如 `Fortinet`） |
| 10 | J | Qty | 數量（整數） |
| 11 | K | Unit | 單位：`台`/`套`/`組`/`月`/`天`/`式`/`趟`/`年`/`箱`/`組`/`端點` |
| 12 | L | Cost(未稅) | 單價（NT$ 整數） |
| 13 | M | Total Cost | 公式 `=J{n}*L{n}` |

### 8.6 Classification 對應規則

| Group | Classification 值 | 說明 |
|-------|-------------------|------|
| 項目（硬體） | `工程材料（硬體）` | 含設備、線材、機櫃、配件 |
| 項目（軟體） | `工程材料（軟體）` | 含授權、訂閱 |
| 項目（ISP） | `施工_外包費` | ISP 月費、安裝費 |
| 工程安裝 | `人工` | 安裝、佈線、設定工時 |
| 規劃設計 | `人工` | 設計、分析工時 |
| 現場任務 | `人工` / `差旅費` | 人工 or 差旅依性質 |
| 專案管理 | `人工` / `運輸費` / `保險費` / `差旅費` / `工程材料（硬體）` | 依品項性質 |

### 8.7 Manufacture 欄填寫規則

| 品項類型 | Manufacture 值 | 範例 |
|----------|---------------|------|
| 硬體設備 | 設備廠牌 | `Fortinet`, `Cisco`, `Synology` |
| 軟體授權 | 軟體廠牌 | `CrowdStrike/Sophos`, `Graylog` |
| ISP | `TBD ISP` | 待定 ISP 供應商 |
| 人工（自有） | `ICPSI`（公司名稱縮寫） | 自有人力 |
| 人工（外包） | 外包商名稱 or `TBD` | 待定外包商 |
| 差旅/運輸/保險 | 供應商 or `ICPSI` | 視性質 |
| 未定品項 | `TBD` | 待決定 |

---

## 9. CBOM 品項完整性檢查

填表完成後，執行以下 Self-Check：

| # | 檢查項目 | 通過條件 |
|---|----------|----------|
| 1 | 硬體覆蓋率 | 架構文件中每個硬體元件都有對應 CBOM 行 |
| 2 | 軟體覆蓋率 | 每個軟體授權都有對應 CBOM 行 |
| 3 | ISP 月費 | 使用商用方案價格，數量 = 營運月數 |
| 4 | 人天合理性 | 總工時在案型規模參考範圍內 |
| 5 | 風險準備金 | 已編列（大型案 5%、中小型案 3%） |
| 6 | 保固費 | 已編列（設備 × 2% × 年） |
| 7 | 差旅 | 已編列（場勘+安裝+驗收的交通/住宿） |
| 8 | 文件人天 | 營運文件、PM/合規文件皆有編列 |
| 9 | 退場 | 已編列退場工時 |
| 10 | 公式正確 | 小計欄皆為公式，非手動值 |
| 11 | Group Header 顏色 | 五個本案 Group 標題行皆為黃底（FFFFFF00），無紅底 |
| 12 | 字型一致性 | Col C = `微軟正黑體 9pt bold`；Col D-J = `微軟正黑體 10pt bold`；Col K-M = `微軟正黑體 10pt non-bold` |
| 13 | 資料行無背景色 | 資料行背景透明，無意外填色 |
| 14 | 表格範圍正確 | `表格_BOM` 的 `ref` 涵蓋所有資料行（非原始模板的 `B4:X44`） |
| 15 | 對齊一致性 | C,D,E,F,I,J,K = center/center；G,H = left/center + wrap_text；L,M = left/center |
| 16 | 數字格式 | L,M 欄 number_format = `"NT$"#,##0`（含貨幣前綴） |
| 17 | 價格來源標示 | 每筆硬體單價備註欄標明來源：`[歷史]` / `[市場]` / `[TBD]` |

---

## 10. 無模板時的 Markdown BOM 格式

若無公司 Excel 模板，產出 `cbom.md`，使用以下結構：

```markdown
# 商務物料清單 (CBOM) — {專案名稱}

版本：v{X.Y}
更新日期：{YYYY-MM-DD}
幣別：{TWD/USD/EUR}
營運期間：{N} 個月

---

## 1. 項目（硬體 + 軟體 + ISP）

| # | CBOM 編號 | 品名 | 規格描述 | 數量 | 單位 | 單價 | 小計 | 備註 |
|---|-----------|------|----------|------|------|------|------|------|

## 2. 工程安裝
...（同上表格格式）

## 3. 規劃設計
...

## 4. 現場任務
...

## 5. 專案管理
...

---

## 總計

| 分類 | 小計 |
|------|------|
| 項目 | {金額} |
| 工程安裝 | {金額} |
| 規劃設計 | {金額} |
| 現場任務 | {金額} |
| 專案管理 | {金額} |
| **總計（成本基礎）** | **{金額}** |
```

---

## 11. 語言規範

| 元素 | 語言 | 範例 |
|------|------|------|
| 品項名稱 | 中文為主，括號附英文型號 | `邊界防火牆 (FortiGate 60F)` |
| 規格描述 | 中英混用 | `UTM 整合 IPS/AV/Web Filter` |
| Group 名稱 | 中文 | `項目`、`工程安裝` |
| 單位 | 中文 | `台`、`天`、`月` |
| 備註 | 中文 | `含 3 年訂閱` |

---

## 12. IEC 62443 安全設備成本估算（SK-D14-005 整合）

安全相關設備依以下四大類別估算：

| 類別 | 涵蓋品項範例 | 定價考量 |
|------|------------|---------|
| Hardware | 防火牆、IDS/IPS、Data Diode、安全交換器 | 歷史成交價優先（見 §4.1），無資料時台灣代理商市場價 ±10% |
| Software | EDR/XDR、SIEM、OT 監控、漏洞管理 | 年訂閱 × 授權數 × 年數 |
| Services | 安全評估、合規稽核、滲透測試、SL 驗證 | 人天費率 × 估算天數 |
| Maintenance | 安全設備維護、訂閱續約、安全更新 | 設備金額 × 年維護比率 |

**CBOM 狀態流**：Draft → Quoted → Gate 0 Approved
**GOV-SD 邊界**：Pre-Gate 0 CBOM 為 advisory（±20% 精度），Gate 0 核准後方具約束力。

---

## 13. 工時估算方法論（SK-D14-006 整合）

### 13.1 三點估算法
每項工作估算 3 個值：Optimistic (O)、Most Likely (M)、Pessimistic (P)
加權平均：`E = (O + 4M + P) / 6`

### 13.2 按資歷等級分配
| 等級 | 日費率 (TWD) | 適用工作 |
|------|-------------|---------|
| Junior | 6,000-8,000 | 文件整理、資料蒐集、測試執行 |
| Senior | 8,000-12,000 | 設計、設定、整合、稽核 |
| Consultant | 12,000-18,000 | Gap Analysis、風險評估、SL 驗證 |
| PM | 10,000-15,000 | 專案管理、協調、報告 |

### 13.3 IEC 62443 生命週期工時對應
| 階段 | 典型活動 | 工時佔比 |
|------|---------|---------|
| Pre-R0 | 需求萃取、可行性、CBOM | 10-15% |
| R1 Design | HLD/LLD、SL allocation | 15-20% |
| R2 Implementation | 設備安裝、設定、佈線 | 25-35% |
| R3 Verification | FAT/SAT、SL verification | 15-20% |
| R4 Operation | 月維護、監控 | 10-15% |
| R5 Decommission | 退場、資料銷毀 | 3-5% |

---

## 14. 品質檢查清單（Quality Checklist）

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 硬體覆蓋率 | 架構文件每個硬體元件都有 CBOM 行 |
| 2 | 軟體覆蓋率 | 每個軟體授權都有 CBOM 行 |
| 3 | ISP 月費 | 商用方案價格，數量 = 營運月數 |
| 4 | 人天合理性 | 總工時在案型規模參考範圍內 |
| 5 | 風險準備金 | 大型案 5%、中小型案 3% |
| 6 | 保固費 | 設備 × 2% × 年 |
| 7 | 差旅 | 場勘+安裝+驗收交通/住宿已編列 |
| 8 | 安全設備覆蓋 | 四大安全類別（HW/SW/Svc/Maint）齊全 |
| 9 | 三點估算 | 關鍵工作項已用三點法估算 |
| 10 | CBOM 狀態 | 明確標示 Draft/Quoted/Gate 0 |
| 11 | Excel 格式 | Group Header 黃底、字型一致、表格範圍正確 |
| 12 | 公式正確 | 小計欄皆為公式，非手動值 |
| 13 | 價格來源標示 | 每筆硬體單價備註欄標明來源：`[歷史]` / `[市場]` / `[TBD]` |

---

## 15. 人類審核閘門（Human Review Gate）

**審核時機**：CBOM 初稿完成後，提交人類審核。

**審核提示範本**：
```
CBOM 初稿已完成。
📊 品項數：{N} 項（硬體 {h}、軟體 {s}、服務 {svc}）
💰 總額：{currency} {amount}（±20% 精度）
⚠️ 待確認：{TBD 品項數} 項待定、{假設數} 項假設
👉 請審核品項覆蓋率、定價合理性與工時估算，確認後進入下一步。
```

**審核標準**：
- **PASS**：品項覆蓋完整、定價合理、工時在參考範圍
- **FAIL**：缺漏關鍵品項、定價偏差 >30%、工時明顯不合理
- **PASS with Conditions**：接受但需補充特定品項或調整估算

---

## 16. Source Traceability

| SK 編號 | 名稱 | 整合內容 |
|--------|------|---------|
| SK-D14-005 | CBOM Development | 四大安全成本分類、CBOM 狀態流、GOV-SD 邊界 |
| SK-D14-006 | Labor Estimation | 三點估算法、資歷分配、生命週期工時佔比 |
| SK-D14-007 | RFI Response Prep | RFI 成本加項意識（透過協作引用） |

<!-- Phase 5 Wave 1: SK knowledge integrated from SK-D14-005/006/007 -->
<!-- F6 Optimization: EPCI substation patterns integrated from Formosa 6 ONS project -->

---

## 附帶檔案

本 Skill 的 `templates/` 目錄包含：

- `CF-SR-03-01.xlsx` — 公司 BOM 成本預估表模板（空白版），作為預設模板使用

本 Skill 的 `references/` 目錄包含：

- `price_lookup.json` — 產品歷史成交價摘要表（1,829 筆），涵蓋 199 品牌，時間跨度 2024-01 ~ 2026-03
- `deprecated_products.json` — 廢棄產品替代關係（38 筆）
- `brand_map.json` — 品牌代碼對照表（199 筆）
- `epci_substation_patterns.md` — 大型 EPCI 變電所專案 CBOM 模式（基於 F6 ONS 實績）

> 價格資料建議每季更新。97.2% 為 TWD，少量 EUR/USD 品項需按匯率換算。
> EPCI 模式適用於 NT$100M+ 的變電所/電力系統整合專案。
