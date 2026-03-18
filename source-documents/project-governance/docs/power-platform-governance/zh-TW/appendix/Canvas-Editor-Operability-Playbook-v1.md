# Canvas 編輯器操作手冊 v1.0

**文件版本**：v1.0
**生效日期**：2026-02-11
**文件擁有者**：System Design Governance Function
**核准單位**：Engineering Management
**文件性質**：Canvas 編輯器故障排除與操作指南
**前置文件**：appendix/Canvas-Brand-UI-Standard-v1.2.md

---

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Canvas 編輯器操作手冊                                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  本手冊解決以下問題：                                                        │
│  • 屬性面板找不到 X/Y/Width/Height                                           │
│  • BorderRadius 在 Rectangle 不支援                                         │
│  • Modern Controls 與 Classic Controls 差異                                 │
│  • 控制項類型確認方法                                                        │
│                                                                             │
│  閱讀對象：                                                                  │
│  新手開發者、Canvas 建置人員、UI 維護人員                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 第一章：屬性設定的兩條路徑

### 1.1 Power Apps Studio 介面概覽

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Power Apps Studio 介面                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────┬────────────────────────────────────┬──────────────────────┐   │
│  │ 樹狀檢視 │  設計畫布（中央）                   │  屬性面板（右側）    │   │
│  │ (左側)   │                                    │                      │   │
│  │          │  ┌──────────────────────────────┐  │  ┌────────────────┐  │   │
│  │ App      │  │                              │  │  │ 屬性           │  │   │
│  │ ├ Screen │  │                              │  │  │ 進階           │  │   │
│  │ │ ├ rect │  │        你的控制項            │  │  ├────────────────┤  │   │
│  │ │ ├ lbl  │  │                              │  │  │ X: [輸入框]    │  │   │
│  │ │ └ btn  │  │                              │  │  │ Y: [輸入框]    │  │   │
│  │          │  └──────────────────────────────┘  │  │ Width: [...]   │  │   │
│  │          │                                    │  │ Height: [...]  │  │   │
│  │          │  ┌──────────────────────────────┐  │  │                │  │   │
│  │          │  │ 公式列（頂部）                │  │  └────────────────┘  │   │
│  │          │  │ 屬性下拉 ▼ │ [公式輸入區]   │  │                      │   │
│  │          │  └──────────────────────────────┘  │                      │   │
│  └──────────┴────────────────────────────────────┴──────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 路徑 A：右側屬性面板（推薦）

**操作步驟**：

```
步驟 1：選取控制項
├── 方法 1：在設計畫布上點選控制項
├── 方法 2：在左側樹狀檢視中點選控制項名稱
└── 驗證點：控制項周圍出現選取框（藍色邊框）

步驟 2：開啟右側屬性面板
├── 若面板已顯示：直接操作
├── 若面板隱藏：點擊右上角「屬性」圖示（齒輪或面板圖示）
└── 驗證點：右側出現「屬性」標籤頁

步驟 3：找到位置與尺寸屬性
├── 基本模式：X、Y、Width、Height 通常在「屬性」標籤頁的下半部
├── 若找不到：
│   ├── 點擊「進階」標籤頁
│   ├── 或展開「位置與大小」區塊
│   └── 或使用搜尋框輸入屬性名稱
└── 驗證點：看到 X、Y 輸入框且可以輸入數值或公式

步驟 4：設定數值
├── 直接輸入數值：例如 80
├── 輸入公式：例如 Parent.Width
├── 按 Enter 確認
└── 驗證點：畫布上控制項位置或大小改變
```

**常見問題排除**：

| 問題 | 原因 | 解決方式 |
|:------|:------|:---------|
| 右側面板完全不見 | 面板被關閉 | 點擊頂部選單「檢視」→「屬性」 |
| 只有少數屬性顯示 | 在「屬性」標籤頁 | 切換到「進階」標籤頁 |
| 屬性為灰色不可編輯 | 控制項被鎖定或為子控制項 | 選取正確的父控制項 |

---

### 1.3 路徑 B：公式列（屬性下拉選單）

**適用情境**：
- 右側面板找不到屬性
- 需要輸入複雜公式
- 精確設定特定屬性

**操作步驟**：

```
步驟 1：選取控制項
└── 確認控制項已選取（有藍色選取框）

步驟 2：找到公式列
├── 位置：設計畫布正上方
├── 結構：[屬性下拉選單 ▼] [公式輸入區]
└── 驗證點：看到類似 fx 的圖示或公式輸入框

步驟 3：展開屬性下拉選單
├── 點擊下拉箭頭 ▼
├── 出現完整屬性清單（按字母排序）
└── 常見屬性：
    ├── BorderColor
    ├── BorderRadius（僅部分控制項支援）
    ├── Fill
    ├── Height
    ├── Visible
    ├── Width
    ├── X
    └── Y

步驟 4：選取目標屬性
├── 點擊屬性名稱（如 X）
├── 公式列顯示目前該屬性的值
└── 驗證點：公式列左側顯示 "X" 或選定的屬性名稱

步驟 5：輸入公式或值
├── 直接輸入：0、80、Parent.Width - 40
├── 按 Enter 或點擊外部確認
└── 驗證點：畫布上控制項反映變更
```

**公式列屬性下拉選單示意**：

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  公式列                                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐  ┌────────────────────────────────────────────────────┐    │
│  │ X         ▼│  │ Parent.Width - 40                                  │    │
│  └─────────────┘  └────────────────────────────────────────────────────┘    │
│        ↑                        ↑                                           │
│    屬性下拉選單            公式輸入區                                        │
│                                                                             │
│  點擊 ▼ 後展開：                                                            │
│  ┌─────────────┐                                                            │
│  │ AutoHeight  │                                                            │
│  │ BorderColor │                                                            │
│  │ BorderRadius│ ← 若控制項支援                                             │
│  │ BorderStyle │                                                            │
│  │ ...         │                                                            │
│  │ Fill        │                                                            │
│  │ FocusedBord│                                                            │
│  │ Font        │                                                            │
│  │ Height      │ ← 尺寸                                                     │
│  │ ...         │                                                            │
│  │ Visible     │                                                            │
│  │ Width       │ ← 尺寸                                                     │
│  │ X           │ ← 位置                                                     │
│  │ Y           │ ← 位置                                                     │
│  └─────────────┘                                                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 第二章：控制項類型確認方法

### 2.1 為什麼需要確認控制項類型

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  控制項類型影響可用屬性                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  問題情境：                                                                  │
│  你以為選到的是 Rectangle，但實際上是：                                      │
│  • Container（有 BorderRadius 但佈局不同）                                  │
│  • Button（有 BorderRadius 但有點擊行為）                                   │
│  • Image（沒有 Fill 屬性）                                                  │
│  • Group（控制項群組，非獨立控制項）                                        │
│                                                                             │
│  後果：                                                                      │
│  • 找不到預期的屬性                                                          │
│  • 設定無效                                                                  │
│  • 運行時行為異常                                                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 確認控制項類型的三種方法

**方法 1：樹狀檢視圖示識別**

```
步驟 1：開啟左側樹狀檢視
├── 點擊左上角「樹狀檢視」圖示
└── 展開畫面節點

步驟 2：觀察控制項圖示
├── 矩形圖示 □ → Rectangle
├── 文字圖示 A → Label
├── 框線圖示 ⬜ → Container
├── 按鈕圖示 → Button
├── 輸入框圖示 → Text input
└── 下拉圖示 → Dropdown

步驟 3：驗證
└── 滑鼠懸停在控制項名稱上，出現 tooltip 顯示完整類型
```

**方法 2：屬性面板標題確認**

```
步驟 1：選取控制項

步驟 2：查看右側屬性面板標題
├── 面板頂部顯示控制項類型
├── 例如："Rectangle1" 下方顯示 "Classic/Rectangle"
└── 或顯示 "Modern/Container"

步驟 3：驗證點
└── 標題區域明確顯示控制項類型名稱
```

**方法 3：公式列檢查特徵屬性**

```
步驟 1：選取控制項

步驟 2：在公式列展開屬性下拉選單

步驟 3：根據可用屬性判斷類型

Rectangle 特徵屬性：
├── Fill ✓
├── BorderColor ✓
├── BorderThickness ✓
├── BorderRadius ❌（Classic Rectangle 不支援）
└── OnSelect ❌

Container 特徵屬性：
├── Fill ✓
├── BorderColor ✓
├── BorderRadius ✓（Modern Container 支援）
├── LayoutMode ✓
└── LayoutDirection ✓

Button 特徵屬性：
├── Fill ✓
├── BorderRadius ✓
├── OnSelect ✓
├── Text ✓
└── Pressed* 屬性 ✓
```

### 2.3 控制項類型識別速查表

| 控制項類型 | 支援 Fill | 支援 BorderRadius | 支援 OnSelect | 支援 LayoutMode |
|-----------|:---------:|:----------------:|:-------------:|:---------------:|
| Rectangle (Classic) | ✓ | ❌ | ❌ | ❌ |
| Container (Modern) | ✓ | ✓ | ❌ | ✓ |
| Button (Classic) | ✓ | ✓ | ✓ | ❌ |
| Button (Modern) | ✓ | ✓ | ✓ | ❌ |
| Label | ❌ | ❌ | ✓ | ❌ |
| Image | ❌ | ✓ | ✓ | ❌ |

---

## 第三章：BorderRadius 不支援的處理

### 3.1 問題說明

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ⚠️ BorderRadius 不支援問題                                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  問題：                                                                      │
│  治理文件要求 Section 容器使用 BorderRadius: 8（圓角卡片）                   │
│  但 Power Apps Canvas 中的 Classic Rectangle 不支援 BorderRadius            │
│                                                                             │
│  影響範圍：                                                                  │
│  • rectSection1、rectSection2、rectSection3                                 │
│  • Flow-Only 欄位容器                                                       │
│  • Badge 容器                                                               │
│                                                                             │
│  解決方案：                                                                  │
│  方案 A：使用 Modern Container（推薦，若環境支援）                           │
│  方案 B：使用 Button (DisplayMode: View) 作為容器                           │
│  方案 C：接受直角設計（降級方案）                                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 方案 A：使用 Modern Container（推薦）

**前置條件**：

```
步驟 1：確認 Modern Controls 已啟用
├── 前往 Settings → Upcoming features → Experimental
├── 確認 "Modern controls and themes" 已開啟
└── 驗證點：Insert 選單中出現 "Modern" 分類

步驟 2：若未開啟
├── 開啟設定
├── 啟用 Modern controls
├── 儲存並重新載入 App
└── 驗證點：Insert → Modern → Container 可用
```

**建立 Modern Container 步驟**：

```
步驟 1：插入 Modern Container
├── 點擊頂部「Insert」選單
├── 選擇「Modern」分類
├── 點擊「Container」
└── 在畫布上繪製或點選放置

步驟 2：重新命名
├── 在樹狀檢視中找到新控制項
├── 雙擊或右鍵「重新命名」
├── 輸入：cntSection1（使用 cnt 前綴表示 Container）
└── 驗證點：樹狀檢視顯示新名稱

步驟 3：設定屬性
├── X: varSectionMargin（或 20）
├── Y: rectGateStepper.Y + rectGateStepper.Height + varSectionSpacing
├── Width: Parent.Width - varSectionMargin * 2
├── Height: [依內容調整]
├── Fill: varCardWhite
├── BorderColor: varBorderLight
├── BorderThickness: 1
├── BorderRadius: 8 ← Container 支援此屬性
└── LayoutMode: "Manual"（若不需自動佈局）

步驟 4：驗證
├── 預覽模式：容器顯示圓角
└── 邊框平滑無銳角
```

### 3.3 方案 B：使用 Button (DisplayMode: View)

**適用情境**：環境不支援 Modern Container

```
步驟 1：插入 Button
├── Insert → Input → Button
└── 放置於目標位置

步驟 2：重新命名
└── 命名為：btnSection1_Container（明確標示用途）

步驟 3：設定屬性
├── X、Y、Width、Height：同 Container 設定
├── Fill: varCardWhite
├── BorderColor: varBorderLight
├── BorderThickness: 1
├── BorderRadius: 8 ← Button 支援此屬性
├── Text: ""（留空）
├── DisplayMode: DisplayMode.View ← 關鍵：禁用點擊
├── HoverFill: varCardWhite（避免 hover 效果）
├── PressedFill: varCardWhite
└── FocusBorderColor: varCardWhite（避免 focus 邊框）

步驟 4：放置子控制項
├── 在 Button 上方放置 Label、Input 等控制項
├── 子控制項的 Y 值需參考 Button 位置
└── 注意：子控制項不會成為 Button 的子項，僅視覺上覆蓋

步驟 5：驗證
├── Button 不可點擊
├── 圓角正確顯示
└── 子控制項可正常互動
```

### 3.4 方案 C：接受直角設計（降級方案）

**適用情境**：
- 環境限制無法使用 Modern Controls
- 專案時程緊迫
- 圓角非必要需求

```
步驟 1：使用 Classic Rectangle
├── Insert → Icons & shapes → Rectangle
└── 保留直角設計

步驟 2：設定屬性
├── 所有屬性同標準規格
├── 移除 BorderRadius 設定（不適用）
└── BorderThickness: 1（保留邊框強調卡片邊界）

步驟 3：視覺補償
├── 適當增加 BorderThickness（1 → 2）可增強卡片感
├── 或使用稍深的 BorderColor
└── 確保視覺一致性

步驟 4：文件註記
└── 在表單說明中註記：「本環境使用直角卡片設計」
```

### 3.5 方案選擇決策樹

```
開始
  │
  ▼
┌─────────────────────────┐
│ Modern Controls 可用？ │
└───────────┬─────────────┘
            │
    ┌───────┴───────┐
    │               │
   是              否
    │               │
    ▼               ▼
┌─────────┐   ┌─────────────────────────┐
│ 方案 A  │   │ 需要圓角視覺？         │
│ Container│   └───────────┬─────────────┘
└─────────┘               │
                  ┌───────┴───────┐
                  │               │
                 是              否
                  │               │
                  ▼               ▼
            ┌─────────┐     ┌─────────┐
            │ 方案 B  │     │ 方案 C  │
            │ Button  │     │ Rectangle│
            │ (View)  │     │ 直角    │
            └─────────┘     └─────────┘
```

---

## 第四章：版本差異與環境適應

### 4.1 Power Apps 編輯器版本差異

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  編輯器版本差異對照                                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Classic Experience（傳統體驗）：                                            │
│  • Insert 選單分類：Icons & shapes、Input、Display、Media                   │
│  • Rectangle 在 "Icons & shapes" 分類                                       │
│  • 屬性面板：簡易模式 + 進階模式                                             │
│  • Modern Controls 需手動啟用                                               │
│                                                                             │
│  New Experience（新體驗）：                                                  │
│  • Insert 選單分類：Classic、Modern、Layout                                 │
│  • Rectangle 在 "Classic" 分類                                              │
│  • Container 在 "Layout" 或 "Modern" 分類                                   │
│  • 屬性面板：統一設計，無進階切換                                            │
│  • Modern Controls 預設可用                                                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 屬性位置差異對照

| 屬性 | Classic 面板位置 | New 面板位置 | 公式列可用 |
|------|-----------------|-------------|:----------:|
| X | 進階 → 位置 | 屬性 → 尺寸與位置 | ✓ |
| Y | 進階 → 位置 | 屬性 → 尺寸與位置 | ✓ |
| Width | 進階 → 位置 | 屬性 → 尺寸與位置 | ✓ |
| Height | 進階 → 位置 | 屬性 → 尺寸與位置 | ✓ |
| Fill | 屬性 → 填滿 | 屬性 → 樣式 | ✓ |
| BorderRadius | 進階 → 設計 | 屬性 → 樣式 | ✓ |
| Visible | 進階 → 核心 | 屬性 → 顯示 | ✓ |

### 4.3 「找不到屬性」萬用解法

**當右側面板找不到任何屬性時**：

```
步驟 1：確認控制項已選取
└── 左側樹狀檢視中，控制項名稱應為高亮顯示

步驟 2：使用公式列設定（保證可用）
├── 確認公式列可見（畫布上方）
├── 展開屬性下拉選單
├── 找到目標屬性
├── 輸入值或公式
└── Enter 確認

步驟 3：若公式列也不見
├── 點擊頂部選單「檢視」(View)
├── 勾選「公式列」(Formula bar)
└── 公式列應出現在畫布上方

步驟 4：若屬性完全不存在於下拉選單
└── 該控制項類型不支援此屬性（參見第二章確認類型）
```

---

## 第五章：常見錯誤與排除

### 5.1 錯誤速查表

| 錯誤現象 | 可能原因 | 排除步驟 |
|:---------|:---------|:---------|
| 「varBrandPrimary 名稱無法辨識」 | 未執行 Run OnStart | App → Run OnStart |
| 屬性設定後無變化 | 選錯控制項 | 確認樹狀檢視選取正確 |
| BorderRadius 不在下拉選單 | 控制項類型不支援 | 改用 Container 或 Button |
| X/Y 為灰色不可編輯 | 控制項在 Container 內且為自動佈局 | 切換 Container 為 Manual 模式 |
| 公式顯示紅色錯誤 | 語法錯誤或引用不存在的控制項 | 檢查拼字與控制項名稱 |
| 控制項重疊無法選取 | 層級順序問題 | 使用樹狀檢視選取 |

### 5.2 層級順序調整

```
問題：控制項被其他控制項覆蓋，無法在畫布上選取

解決方案：

步驟 1：使用樹狀檢視選取
├── 左側樹狀檢視顯示所有控制項
├── 直接點擊目標控制項名稱
└── 即使被覆蓋也能選取

步驟 2：調整層級順序
├── 在樹狀檢視中拖曳控制項
├── 向上拖曳 = 更上層（覆蓋其他）
├── 向下拖曳 = 更下層（被覆蓋）
└── 或右鍵 → 移至最上層/最下層

步驟 3：正確的層級順序
├── 最上層：訊息區塊（覆蓋所有）
├── 中間層：輸入控制項、Label
├── 底層：背景 Rectangle、Container
└── 最底層：畫面背景
```

### 5.3 執行 Run OnStart

```
問題：變數未定義（如 varBrandPrimary）

解決方案：

步驟 1：確認 App.OnStart 已設定
├── 左側樹狀檢視 → 選取「App」節點
├── 公式列選擇「OnStart」屬性
└── 確認包含色彩變數定義

步驟 2：執行 Run OnStart
├── 方法 1：點擊「App」節點 → 三點選單 → Run OnStart
├── 方法 2：頂部選單 → App → Run OnStart
└── 方法 3：點擊 OnStart 旁的「▶」按鈕（若可見）

步驟 3：驗證
├── 無錯誤訊息
├── 左側「變數」面板顯示所有已定義變數
└── 在公式中輸入 varBrandPrimary，無紅色錯誤
```

---

## 第六章：驗證點檢查清單

### 6.1 每步操作後的驗證點

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  操作 → 驗證點對照                                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  插入控制項 → 驗證：                                                         │
│  ☐ 控制項出現在畫布上                                                        │
│  ☐ 控制項出現在樹狀檢視中                                                    │
│  ☐ 選取時有藍色邊框                                                          │
│                                                                             │
│  設定 X/Y → 驗證：                                                           │
│  ☐ 控制項在畫布上移動到正確位置                                              │
│  ☐ 公式列顯示設定值（無紅色錯誤）                                            │
│                                                                             │
│  設定 Fill → 驗證：                                                          │
│  ☐ 控制項顏色改變                                                            │
│  ☐ 顏色符合預期（如深藍色 for varBrandPrimary）                              │
│                                                                             │
│  設定 BorderRadius → 驗證：                                                  │
│  ☐ 控制項角落變為圓角                                                        │
│  ☐ 若無變化，確認控制項類型是否支援                                          │
│                                                                             │
│  設定 Visible → 驗證：                                                       │
│  ☐ false：控制項在設計模式顯示透明框線，預覽模式不可見                       │
│  ☐ true：控制項正常顯示                                                      │
│                                                                             │
│  設定 DisplayMode → 驗證：                                                   │
│  ☐ Disabled：預覽模式中控制項灰色且不可互動                                  │
│  ☐ Edit：預覽模式中控制項可互動                                              │
│  ☐ View：控制項可見但不可互動                                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 6.2 最終檢查清單

```
建置完成前檢查：

結構完整性：
☐ Header 存在且高度 80px
☐ Gate Stepper 存在（或 Visible: false）
☐ 三個 Section 容器存在
☐ Footer 存在且高度 72px
☐ 訊息區塊存在

屬性正確性：
☐ 所有控制項已重命名（無預設名稱）
☐ 所有色彩使用變數（無硬編碼）
☐ 所有位置使用變數或相對公式
☐ DisplayMode 使用列舉值

功能驗證：
☐ Run OnStart 成功執行
☐ 預覽模式：所有元素正確顯示
☐ 預覽模式：必填欄位驗證正確
☐ 預覽模式：按鈕互動正確
```

---

## 第七章：User Lookup 欄位正確處理（v1.1 新增）

### 7.1 問題背景

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  User Lookup 欄位常見錯誤                                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  問題描述：                                                                  │
│  Dataverse 中的 Lookup (User table) 欄位常被錯誤處理為純文字欄位。           │
│                                                                             │
│  典型錯誤範例：                                                              │
│  ├── 顯示：使用 varCurrentUserEmail（email 字串）                           │
│  ├── 提交：傳送 varCurrentUserEmail 給 Flow                                │
│  └── 比對：gov_systemarchitect = varCurrentUserEmail                        │
│                                                                             │
│  正確做法：                                                                  │
│  ├── 顯示：使用 varCurrentUserName（人類可讀）                               │
│  ├── 提交：傳送 varCurrentUser（User 記錄）給 Flow                          │
│  └── 比對：gov_systemarchitect.'Primary Email' = varCurrentUserEmail       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 7.2 User() 函數回傳值

```
User() 函數在 App.OnStart 中的完整設定：

Set(varCurrentUser, User());                    // ← User 記錄（Lookup 用）
Set(varCurrentUserEmail, User().Email);         // ← Email 字串（顯示/比對用）
Set(varCurrentUserName, User().FullName);       // ← 名稱字串（顯示用）

三個變數用途對照：

| 變數 | 型別 | 用途 | 範例 |
|:------|:------|:------|:------|
| varCurrentUser | User Record | 傳送給 Lookup 欄位 | Flow 輸入參數 |
| varCurrentUserEmail | Text | 顯示、文字比對 | Filter 條件 |
| varCurrentUserName | Text | UI 顯示 | Label.Text |
```

### 7.3 顯示 User Lookup 欄位

**錯誤做法**：
```
lblArchitectValue.Text: varCurrentUserEmail

問題：
├── 僅顯示 email，不夠友善
├── 與 Lookup 欄位語義不一致
└── 若 email 變更會導致不一致
```

**正確做法**：
```
lblArchitectValue.Text: varCurrentUserName

優點：
├── 顯示人類可讀的名稱
├── 與 Dataverse 記錄一致
└── 更友善的 UX
```

### 7.4 提交 User Lookup 欄位給 Flow

**錯誤做法**：
```
'GOV-001-CreateProject'.Run(
    txtTitle.Text,
    varCurrentUserEmail,           // ❌ 錯誤：email 字串
    ...
)

問題：
├── Flow 收到的是 email 字串
├── Dataverse 的 Lookup 欄位無法直接接受 email 字串
└── 需要 Flow 額外做 Lookup 解析
```

**正確做法**：
```
'GOV-001-CreateProject'.Run(
    txtTitle.Text,
    varCurrentUser,                // ✓ 正確：User 記錄
    ...
)

優點：
├── Flow 直接收到 User 記錄
├── Dataverse Lookup 欄位可直接寫入
└── 減少 Flow 處理邏輯
```

### 7.5 Filter 中比對 User Lookup 欄位

**錯誤做法**：
```
Filter(
    gov_projectregistry,
    gov_systemarchitect = varCurrentUserEmail      // ❌ 錯誤：型別不匹配
)

問題：
├── gov_systemarchitect 是 Lookup (User)
├── varCurrentUserEmail 是 Text
└── 型別不匹配，可能無結果或錯誤
```

**正確做法**：
```
// 方法 A：展開 Lookup 欄位比對 email
Filter(
    gov_projectregistry,
    gov_systemarchitect.'Primary Email' = varCurrentUserEmail
)

// 方法 B：使用 User GUID 比對（更可靠）
Filter(
    gov_projectregistry,
    gov_systemarchitect.User = varCurrentUser.User
)
```

### 7.6 User Lookup 欄位檢查清單

```
開發前檢查：

☐ 確認 Dataverse 欄位類型
   └── 若為 Lookup (User table)，必須使用 User 記錄

☐ 確認 App.OnStart 設定
   ├── Set(varCurrentUser, User())              ✓ 必須有
   ├── Set(varCurrentUserEmail, User().Email)   ✓ 必須有
   └── Set(varCurrentUserName, User().FullName) ✓ 必須有

☐ 確認顯示用變數
   └── Label.Text: varCurrentUserName（非 varCurrentUserEmail）

☐ 確認提交用變數
   └── Flow 輸入：varCurrentUser（非 varCurrentUserEmail）

☐ 確認 Filter 比對
   └── gov_systemarchitect.'Primary Email' = varCurrentUserEmail
```

### 7.7 常見錯誤訊息與排除

| 錯誤訊息 | 原因 | 解決方式 |
|:---------|:------|:---------|
| "Invalid argument type" | Lookup 欄位收到 Text | 改用 varCurrentUser |
| "The value cannot be found" | email 字串無法 Lookup | 使用展開欄位比對 |
| Filter 無結果 | 型別不匹配 | 使用 'Primary Email' 展開 |
| Flow 寫入失敗 | Lookup 欄位型別錯誤 | Flow 內使用 Lookup action |

---

## 版本歷史

| 版本 | 日期 | 變更說明 |
|:------|:------|:---------|
| v1.0 | 2026-02-11 | 初版建立 - 故障排除與操作指南 |
| v1.1 | 2026-02-11 | 新增第七章：User Lookup 欄位正確處理 |

---

**文件結束**

**本手冊為 Canvas 編輯器操作之故障排除指南。**
**配合 Canvas Brand UI Standard v1.2 使用。**
