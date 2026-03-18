# Canvas Brand UI Standard v1.1

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ⚠️ 已棄用（DEPRECATED）                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  本文件已於 2026-02-11 棄用。                                                │
│                                                                             │
│  請改用：appendix/Canvas-Brand-UI-Standard-v1.2.md                          │
│                                                                             │
│  v1.2 為 Anti-Fragile Canvas Governance Edition                             │
│  包含模板強制化、人為錯誤防護、3 年穩定架構                                   │
│                                                                             │
│  禁止引用本文件作為設計依據。                                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**文件版本**：v1.1 ❌ **已棄用**
**生效日期**：2026-02-11
**棄用日期**：2026-02-11
**替代文件**：Canvas-Brand-UI-Standard-v1.2.md
**文件擁有者**：System Design Governance Function
**核准單位**：Engineering Management
**文件性質**：品牌 UI 設計標準（Brand UI Design Standard）
**文件權威**：**已由 v1.2 取代**

---

## 重要聲明（歷史記錄）

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ⚠️ 權威聲明（AUTHORITY STATEMENT）- 歷史記錄                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [已棄用] 本文件曾為治理系統 Canvas App 之色彩與 UI 設計權威                  │
│                                                                             │
│  現已由 Canvas-Brand-UI-Standard-v1.2.md 取代                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 第一章：統一色彩系統

### 1.1 唯一色彩定義

**本章節為所有 Canvas App 色彩之唯一來源。禁止在任何其他文件定義色彩。**

| 變數名稱 | 色碼 | RGB | 用途 | 語義 |
|:---------|:------|:-----|:------|:------|
| varBrandPrimary | #0C3467 | 12, 52, 103 | Header、主標題、Primary Button | 品牌主色 |
| varBrandPrimaryHover | #0A2D5A | 10, 45, 90 | Primary Button Hover | 品牌互動 |
| varBrandPrimaryPressed | #082548 | 8, 37, 72 | Primary Button Pressed | 品牌互動 |
| varBrandAccent | #008EC3 | 0, 142, 195 | Focus 邊框、強調連結 | 強調色 |
| varNeutralDark | #605E5C | 96, 94, 92 | 次要文字、標籤 | 中性深 |
| varNeutralGray | #999999 | 153, 153, 153 | Disabled、未達 Gate | 中性中 |
| varNeutralLight | #E1E1E1 | 225, 225, 225 | 邊框、分隔線 | 中性淺 |
| varNeutralLighter | #F5F5F5 | 245, 245, 245 | 頁面背景 | 中性極淺 |
| varTextBase | #2D2D2D | 45, 45, 45 | 主要文字 | 文字主色 |
| varTextSecondary | #666666 | 102, 102, 102 | 輔助文字 | 文字次色 |
| varTextDisabled | #999999 | 153, 153, 153 | 停用文字 | 文字停用 |
| varTextOnPrimary | #FFFFFF | 255, 255, 255 | 品牌色上文字 | 反白文字 |
| varDanger | #A4262C | 164, 38, 44 | 錯誤、刪除、Terminated | 危險 |
| varDangerLight | #FDE7E9 | 253, 231, 233 | 錯誤訊息背景 | 危險淺 |
| varSuccess | #107C10 | 16, 124, 16 | 成功、Closed、已完成 | 成功 |
| varSuccessLight | #DFF6DD | 223, 246, 221 | 成功訊息背景 | 成功淺 |
| varWarning | #FFB900 | 255, 185, 0 | 警告、Pending | 警告 |
| varWarningLight | #FFF4CE | 255, 244, 206 | 警告訊息背景 | 警告淺 |
| varCardWhite | #FFFFFF | 255, 255, 255 | Section 卡片背景 | 白色 |
| varFlowOnlyBg | #EFEFEF | 239, 239, 239 | 系統欄位背景 | 唯讀背景 |
| varBorderLight | #E1E1E1 | 225, 225, 225 | 卡片邊框 | 邊框 |

### 1.2 已棄用變數對照表

**以下變數已棄用，禁止使用。若既有程式碼使用這些變數，必須遷移至新變數。**

| 棄用變數 | 替代變數 | 說明 |
|:---------|:---------|:------|
| varColorPrimary | varBrandPrimary | 品牌主色統一 |
| varColorPrimaryHover | varBrandPrimaryHover | 互動色統一 |
| varColorPrimaryPressed | varBrandPrimaryPressed | 互動色統一 |
| varColorSuccess | varSuccess | 移除 Color 前綴 |
| varColorSuccessLight | varSuccessLight | 移除 Color 前綴 |
| varColorDanger | varDanger | 移除 Color 前綴 |
| varColorDangerLight | varDangerLight | 移除 Color 前綴 |
| varColorWarning | varWarning | 移除 Color 前綴 |
| varColorWarningLight | varWarningLight | 移除 Color 前綴 |
| varColorNeutral | varNeutralDark | 語義明確化 |
| varColorNeutralLight | varNeutralLighter | 語義明確化 |
| varColorNeutralBorder | varBorderLight | 語義明確化 |
| varColorBackground | varNeutralLighter | 統一背景色 |
| varColorFlowOnlyBg | varFlowOnlyBg | 移除 Color 前綴 |
| varColorFlowOnlyBorder | varBorderLight | 統一邊框色 |
| varColorTextPrimary | varTextBase | 語義明確化 |
| varColorTextSecondary | varTextSecondary | 移除 Color 前綴 |
| varColorTextDisabled | varTextDisabled | 移除 Color 前綴 |
| varColorTextOnPrimary | varTextOnPrimary | 移除 Color 前綴 |
| varBrandAccentLight | 移除 | 簡化色彩系統 |

### 1.3 App.OnStart 唯一色彩模板

```
// ═══════════════════════════════════════════════════════════
// Canvas Brand UI Standard v1.1 - 唯一色彩定義
// 生效日期：2026-02-11
// 權威：本區塊為唯一官方色彩來源
// ═══════════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────────────
// Brand（品牌色系）
// ─────────────────────────────────────────────────────────────
Set(varBrandPrimary, ColorValue("#0C3467"));
Set(varBrandPrimaryHover, ColorValue("#0A2D5A"));
Set(varBrandPrimaryPressed, ColorValue("#082548"));
Set(varBrandAccent, ColorValue("#008EC3"));

// ─────────────────────────────────────────────────────────────
// Neutral（中性色系）- 極簡四階
// ─────────────────────────────────────────────────────────────
Set(varNeutralDark, ColorValue("#605E5C"));
Set(varNeutralGray, ColorValue("#999999"));
Set(varNeutralLight, ColorValue("#E1E1E1"));
Set(varNeutralLighter, ColorValue("#F5F5F5"));

// ─────────────────────────────────────────────────────────────
// Text（文字色系）
// ─────────────────────────────────────────────────────────────
Set(varTextBase, ColorValue("#2D2D2D"));
Set(varTextSecondary, ColorValue("#666666"));
Set(varTextDisabled, ColorValue("#999999"));
Set(varTextOnPrimary, ColorValue("#FFFFFF"));

// ─────────────────────────────────────────────────────────────
// Semantic（語義色系）- 極簡三色
// ─────────────────────────────────────────────────────────────
Set(varDanger, ColorValue("#A4262C"));
Set(varDangerLight, ColorValue("#FDE7E9"));
Set(varSuccess, ColorValue("#107C10"));
Set(varSuccessLight, ColorValue("#DFF6DD"));
Set(varWarning, ColorValue("#FFB900"));
Set(varWarningLight, ColorValue("#FFF4CE"));

// ─────────────────────────────────────────────────────────────
// Surface（表面色系）
// ─────────────────────────────────────────────────────────────
Set(varCardWhite, ColorValue("#FFFFFF"));
Set(varFlowOnlyBg, ColorValue("#EFEFEF"));
Set(varBorderLight, ColorValue("#E1E1E1"));
```

### 1.4 色彩使用絕對規則

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  色彩使用絕對規則                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ✓ 允許：                                                                    │
│    • Header 背景：varBrandPrimary                                           │
│    • Primary Button：varBrandPrimary                                        │
│    • Focus 邊框：varBrandAccent                                             │
│    • 成功訊息：varSuccess / varSuccessLight                                 │
│    • 錯誤訊息：varDanger / varDangerLight                                   │
│    • 警告訊息：varWarning / varWarningLight                                 │
│    • 頁面背景：varNeutralLighter                                            │
│    • Section 背景：varCardWhite                                             │
│    • Flow-Only 欄位：varFlowOnlyBg                                          │
│                                                                             │
│  ✗ 禁止：                                                                    │
│    • 硬編碼色碼（如 ColorValue("#0C3467")）                                  │
│    • 使用任何 varColor* 變數                                                 │
│    • 自定義新色彩變數                                                        │
│    • 使用純黑 #000000                                                        │
│    • 在非錯誤情境使用 varDanger                                              │
│    • 在非成功情境使用 varSuccess                                             │
│    • 在 Body 區大面積使用 varBrandPrimary                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 第二章：Layout 結構規範

### 2.1 五區塊配置（不可變更）

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ① HEADER                                                    Height: 80px  │
│  Fill: varBrandPrimary | Text: varTextOnPrimary                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  ② GATE STEPPER                                              Height: 50px  │
│  Fill: varNeutralLighter                                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│  ③ MAIN BODY                                            Height: 動態填充   │
│  Fill: varNeutralLighter                                                    │
│  ┌─Section 1: Basic Information──────────────────────────────────────────┐  │
│  │  Fill: varCardWhite                                                   │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│  ┌─Section 2: Responsibility─────────────────────────────────────────────┐  │
│  │  Fill: varCardWhite                                                   │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│  ┌─Section 3: Details────────────────────────────────────────────────────┐  │
│  │  Fill: varCardWhite                                                   │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────────────────────┤
│  ④ FOOTER                                                    Height: 72px  │
│  Fill: varCardWhite | Border-top: varBorderLight                            │
│  [Cancel] 左側                                          [Submit] 右側       │
├─────────────────────────────────────────────────────────────────────────────┤
│  ⑤ MESSAGE AREA（覆蓋於頂部）                              Height: 0-60px  │
│  位置：Y = 80（Header 下方）                                                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 區塊固定尺寸

| 區塊 | 高度 | Y 座標 | 可變更 |
|------|------|--------|:------:|
| Header | 80px | 0 | ❌ |
| Gate Stepper | 50px | 80 | ❌ |
| Body | 動態 | `If(rectGateStepper.Visible, 130, 80)` | 動態 |
| Footer | 72px | `Parent.Height - 72` | ❌ |
| Message | 60px | 80 | ❌ |

### 2.3 Section 卡片規格

| 屬性 | 值 |
|:------|:-----|
| Fill | varCardWhite |
| BorderColor | varBorderLight |
| BorderThickness | 1 |
| BorderRadius | 8 |
| Margin | 20px |
| Padding | 16px |
| Section 間距 | 16px |

---

## 第三章：Gate Stepper 極簡設計

### 3.1 Stepper 視覺規格（極簡版）

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   ●━━━━━━●━━━━━━◉━━━━━━○━━━━━━○━━━━━━○                                       │
│  Pending Gate0  Gate1  Gate2  Gate3  Closed                                 │
│   完成   完成    當前    未達    未達    未達                                  │
│                                                                             │
│  極簡設計規格：                                                               │
│  ● 已完成：varBrandPrimary, Opacity 0.5                                     │
│  ◉ 目前：varBrandPrimary, Opacity 1.0                                       │
│  ○ 未達：varNeutralGray, Opacity 0.4                                        │
│  ━ 連線：統一使用 varNeutralLight                                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Stepper 控制項規格

**步驟圓點**：

| 屬性 | 已完成 | 目前 | 未達 |
|:------|:--------|:------|:------|
| Width/Height | 16 | 20 | 16 |
| Fill | varBrandPrimary | varBrandPrimary | varNeutralGray |
| Opacity | 0.5 | 1.0 | 0.4 |

**步驟標籤**：

| 屬性 | 已完成 | 目前 | 未達 |
|:------|:--------|:------|:------|
| Color | varBrandPrimary | varBrandPrimary | varNeutralGray |
| Font | Segoe UI | Segoe UI Semibold | Segoe UI |
| Size | 10 | 11 | 10 |

**連接線**：統一 Height: 2px, Fill: varNeutralLight

---

## 第四章：Status Badge 極簡規格

### 4.1 Badge 僅四種類型

| Badge | 用途 | Fill | Color |
|:-------|:------|:------|:-------|
| Primary | Active, 目前 Gate | varBrandPrimary | varTextOnPrimary |
| Success | Closed, Approved | varSuccess | varTextOnPrimary |
| Danger | Terminated, Rejected | varDanger | varTextOnPrimary |
| Neutral | Pending, Draft, None | varNeutralLight | varTextBase |

**移除 Warning Badge**：Pending 狀態使用 Neutral，減少視覺情緒。

### 4.2 Badge 控制項規格

```
Height: 22
PaddingLeft: 10
PaddingRight: 10
BorderRadius: 11（膠囊形）
Font: Segoe UI Semibold
Size: 10
```

---

## 第五章：Flow-Only 欄位規範

### 5.1 視覺識別

```
┌────────────────────────────────────────────────────────────────────────┐
│  Request ID (System-controlled)                                        │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  DR-2026-00001234                                                │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│        Fill: varFlowOnlyBg | Color: varTextSecondary                   │
└────────────────────────────────────────────────────────────────────────┘
```

### 5.2 強制規則

1. 使用 **Label** 控制項（禁止 Text input）
2. 背景色：**varFlowOnlyBg**
3. 邊框色：**varBorderLight**
4. 標籤後綴：**" (System-controlled)"**
5. 文字色：**varTextSecondary**

---

## 第六章：Button 語義規範

### 6.1 Button 僅三種類型

| 類型 | 用途 | Fill | Color |
|:------|:------|:------|:-------|
| Primary | 主要操作 | varBrandPrimary | varTextOnPrimary |
| Ghost | 取消/返回 | Transparent | varTextSecondary |
| Danger | 危險操作 | varDanger | varTextOnPrimary |

**移除 Secondary Button**：簡化為 Primary + Ghost 雙按鈕模式。

### 6.2 Footer Button 排列

```
┌─────────────────────────────────────────────────────────────────────────────┐
│   [Cancel]                                                      [Submit]    │
│      ↑                                                             ↑        │
│   Ghost                                                        Primary      │
│   X: 20                                            X: Parent.Width - 140    │
└─────────────────────────────────────────────────────────────────────────────┘

規則：
• Ghost Button 固定左側
• Primary Button 固定右側
• 禁止三按鈕以上
• 禁止水平置中
```

---

## 第七章：訊息區塊極簡規範

### 7.1 訊息僅兩種類型

| 類型 | 用途 | Fill | Icon Color |
|:------|:------|:------|:------------|
| Success | 操作成功 | varSuccessLight | varSuccess |
| Error | 操作失敗 | varDangerLight | varDanger |

**移除 Warning Message**：警告資訊使用對話框或 inline 提示。

### 7.2 訊息區塊規格

```
Y: 80（Header 下方）
Height: 60px
Width: Parent.Width
位置：覆蓋於 Gate Stepper 上方
關閉按鈕：右側 X 圖示
```

---

## 第八章：字體與間距極簡規範

### 8.1 字體僅三級

| 級別 | 用途 | 字體 | 大小 |
|:------|:------|:------|:------|
| Title | Header、Section 標題 | Segoe UI Semibold | 16 |
| Body | 欄位內容、按鈕 | Segoe UI | 14 |
| Caption | 標籤、說明 | Segoe UI | 12 |

### 8.2 間距僅四級

| 級別 | 值 | 用途 |
|:------|:-----|:------|
| XS | 8px | 標籤與輸入框 |
| SM | 12px | 同組控制項 |
| MD | 16px | Section 內部 |
| LG | 20px | Section 間距 |

---

## 第九章：控制項命名標準

### 9.1 命名前綴

| 控制項 | 前綴 | 範例 |
|:--------|:------|:------|
| Label | lbl | lblTitle |
| Text input | txt | txtTitle |
| Dropdown | dd | ddType |
| ComboBox | cmb | cmbManager |
| Button | btn | btnSubmit |
| Rectangle | rect | rectHeader |
| Icon | ico | icoClose |

### 9.2 區塊命名

| 區塊 | 容器 | 內部控制項前綴 |
|:------|:------|:---------------|
| Header | rectHeader | lblH_, btnH_ |
| Section 1 | rectSection1 | lblS1_, txtS1_ |
| Section 2 | rectSection2 | lblS2_, cmbS2_ |
| Section 3 | rectSection3 | lblS3_, ddS3_ |
| Footer | rectFooter | btnCancel, btnSubmit |

---

## 第十章：UI Governance Stability Guardrails

### 10.1 不可逆警告條款（FREEZE）

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  🔒 不可逆警告條款（IMMUTABLE FREEZE ITEMS）                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ❌ 條款 1：禁止修改核心布局骨架                                             │
│     • 五區塊配置（Header/Stepper/Body/Footer/Message）不可變更              │
│     • 區塊高度（80/50/動態/72/60）不可變更                                   │
│     • 三 Section 結構（Basic/Responsibility/Details）不可變更               │
│                                                                             │
│  ❌ 條款 2：禁止新增未授權色彩                                               │
│     • 本標準定義之 21 個色彩變數為唯一來源                                   │
│     • 禁止在任何文件新增 HEX 色碼定義                                        │
│     • 禁止使用 varColor* 系列變數（已棄用）                                  │
│                                                                             │
│  ❌ 條款 3：禁止個人風格自由發揮                                             │
│     • 新表單必須沿用本標準模板                                               │
│     • 禁止自定義動畫、陰影、漸層                                             │
│     • 禁止變更 Button 排列規則（Ghost 左/Primary 右）                        │
│                                                                             │
│  違反上述條款之表單將被視為不合規，禁止上線。                                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 10.2 允許的擴充方式（Overlay 模式）

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ✓ 允許的擴充方式（OVERLAY EXTENSION）                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ✓ 擴充 1：Section 內欄位擴充                                                │
│     • 可在既有 Section 內新增欄位                                            │
│     • 必須遵循控制項命名規範                                                 │
│     • 必須使用標準色彩變數                                                   │
│                                                                             │
│  ✓ 擴充 2：訊息文案客製                                                      │
│     • 可自定義成功/錯誤訊息文案                                              │
│     • 禁止變更訊息區塊結構與色彩                                             │
│                                                                             │
│  ✓ 擴充 3：Stepper 顯示控制                                                  │
│     • 可透過 Visible 屬性隱藏 Gate Stepper                                   │
│     • 禁止變更 Stepper 視覺設計                                              │
│                                                                             │
│  擴充申請流程：                                                              │
│  1. 提出書面申請說明擴充需求                                                 │
│  2. 確認擴充符合 Overlay 模式                                                │
│  3. UX Governance Specialist 審核                                           │
│  4. 更新本標準文件（若為通用擴充）                                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 10.3 技術債預防機制

| 機制 | 說明 |
|:------|:------|
| 單一權威文件 | 本標準為唯一 UI 設計權威，禁止多頭馬車 |
| 變數前綴鎖定 | 僅允許 varBrand*, varNeutral*, varText*, var[Semantic]* |
| 版本凍結 | v1.1 為穩定版，下次大版本升級需全系統評估 |
| 禁止向後相容層 | 不提供 varColor* → varBrand* 自動映射 |

---

## 附錄 A：Canvas 施工步驟完整教學

### A.1 從零開始建立 Canvas App

**Step 1：進入 Power Apps**

```
操作路徑：
1. 開啟瀏覽器 → 前往 https://make.powerapps.com
2. 確認右上角環境為正確環境（如 Production、Dev）
3. 點擊左側選單「+ 建立」

驗證點：
✓ 頁面顯示「建立」選項
```

**Step 2：建立空白 Canvas App**

```
操作路徑：
1. 選擇「空白應用程式」
2. 選擇「空白畫布應用程式」
3. 輸入應用程式名稱（如 GOV-FormTemplate）
4. 選擇「平板電腦」格式
5. 點擊「建立」

驗證點：
✓ Power Apps Studio 開啟
✓ 畫面顯示空白畫布
```

**Step 3：設定 App.OnStart**

```
操作路徑：
1. 點擊左上角「Tree view」圖示
2. 點擊「App」節點
3. 在右側屬性面板找到「OnStart」屬性
4. 點擊「OnStart」旁的「編輯」按鈕（fx 圖示）
5. 在公式列中貼上本標準第 1.3 節的完整色彩模板
6. 按下 Ctrl+S 儲存

驗證點：
✓ 公式列無紅色錯誤
✓ 無語法警告
```

**Step 4：執行 Run OnStart**

```
操作路徑：
1. 點擊頂部選單「App」
2. 點擊「Run OnStart」

驗證點：
✓ 無錯誤訊息
✓ 變數已初始化（可在「變數」面板確認）
```

### A.2 五區塊畫面建置步驟

**Step 1：建立 Header Rectangle**

```
操作路徑：
1. 點擊頂部「插入」選單
2. 點擊「形狀」→「矩形」
3. 在畫布上繪製矩形

重命名控制項：
1. 在左側 Tree view 找到「Rectangle1」
2. 點擊兩下或右鍵「重新命名」
3. 輸入：rectHeader

設定屬性（在公式列或右側面板）：
├── X: 0
├── Y: 0
├── Width: Parent.Width
├── Height: 80
├── Fill: varBrandPrimary
└── BorderThickness: 0

驗證點：
✓ 矩形位於畫面頂部
✓ 高度為 80px
✓ 顏色為深藍色（#0C3467）
```

**Step 2：建立 Gate Stepper**

```
操作路徑：
1. 插入 → 形狀 → 矩形
2. 重命名為：rectGateStepper

設定屬性：
├── X: 0
├── Y: 80
├── Width: Parent.Width
├── Height: 50
├── Fill: varNeutralLighter
└── BorderThickness: 0

驗證點：
✓ 矩形位於 Header 下方
✓ 高度為 50px
✓ 顏色為淺灰色（#F5F5F5）
```

**Step 3：建立 Section 1（Basic Information）**

```
操作路徑：
1. 插入 → 形狀 → 矩形
2. 重命名為：rectSection1

設定屬性：
├── X: 20
├── Y: 150
├── Width: Parent.Width - 40
├── Height: 120
├── Fill: varCardWhite
├── BorderColor: varBorderLight
├── BorderThickness: 1
└── BorderRadius: 8

新增 Section 標題：
1. 插入 → 文字 → 標籤
2. 重命名為：lblS1_Title
3. 設定 Text: "Basic Information"
4. 設定 X: rectSection1.X + 16
5. 設定 Y: rectSection1.Y + 12
6. 設定 Font: Font.'Segoe UI Semibold'
7. 設定 Size: 16
8. 設定 Color: varTextBase

驗證點：
✓ 白色卡片位於 Stepper 下方
✓ 有 8px 圓角
✓ 標題顯示 "Basic Information"
```

**Step 4：建立 Section 2（Responsibility）**

```
操作路徑：
1. 插入 → 形狀 → 矩形
2. 重命名為：rectSection2

設定屬性：
├── X: 20
├── Y: rectSection1.Y + rectSection1.Height + 16
├── Width: Parent.Width - 40
├── Height: 100
├── Fill: varCardWhite
├── BorderColor: varBorderLight
├── BorderThickness: 1
└── BorderRadius: 8

新增 Section 標題：
1. 插入 → 文字 → 標籤
2. 重命名為：lblS2_Title
3. 設定 Text: "Responsibility"

驗證點：
✓ 第二個白色卡片位於 Section 1 下方
✓ 間距為 16px
```

**Step 5：建立 Section 3（Details）**

```
操作路徑：
1. 複製 Section 2 的方法
2. 重命名為：rectSection3
3. Y: rectSection2.Y + rectSection2.Height + 16
4. 標題標籤：lblS3_Title，Text: "Details"

驗證點：
✓ 三個 Section 垂直排列
✓ 間距一致（16px）
```

**Step 6：建立 Footer**

```
操作路徑：
1. 插入 → 形狀 → 矩形
2. 重命名為：rectFooter

設定屬性：
├── X: 0
├── Y: Parent.Height - 72
├── Width: Parent.Width
├── Height: 72
├── Fill: varCardWhite
├── BorderColor: varBorderLight
└── BorderThickness: 1（僅頂部，可用巢狀元素實現）

驗證點：
✓ Footer 固定於畫面底部
✓ 高度為 72px
```

**Step 7：建立 Cancel Button（Ghost）**

```
操作路徑：
1. 插入 → 輸入 → 按鈕
2. 重命名為：btnCancel

設定屬性：
├── Text: "取消"
├── X: 20
├── Y: rectFooter.Y + (rectFooter.Height - 40) / 2
├── Width: 80
├── Height: 40
├── Fill: Transparent
├── Color: varTextSecondary
├── BorderThickness: 0
├── HoverFill: varNeutralLighter
└── Font: Font.'Segoe UI'

驗證點：
✓ 按鈕位於 Footer 左側
✓ 透明背景
✓ 灰色文字
```

**Step 8：建立 Submit Button（Primary）**

```
操作路徑：
1. 插入 → 輸入 → 按鈕
2. 重命名為：btnSubmit

設定屬性：
├── Text: "提交"
├── X: Parent.Width - 120 - 20
├── Y: rectFooter.Y + (rectFooter.Height - 40) / 2
├── Width: 120
├── Height: 40
├── Fill: varBrandPrimary
├── Color: varTextOnPrimary
├── HoverFill: varBrandPrimaryHover
├── PressedFill: varBrandPrimaryPressed
├── BorderRadius: 4
└── Font: Font.'Segoe UI Semibold'

驗證點：
✓ 按鈕位於 Footer 右側
✓ 深藍色背景
✓ 白色文字
```

**Step 9：調整控制項層級順序**

```
操作路徑：
1. 在左側 Tree view 中
2. 將 rectFooter 拖曳至最底部（最先渲染）
3. 將 rectSection3 拖曳至 rectFooter 上方
4. 依序排列（從下到上）：
   └── rectFooter
   └── rectSection3
   └── rectSection2
   └── rectSection1
   └── rectGateStepper
   └── rectHeader
   └── btnCancel
   └── btnSubmit
   └── 標籤控制項

驗證點：
✓ 預覽時所有元素正確顯示
✓ Button 可點擊
```

**Step 10：最終驗證**

```
驗證項目：
☐ Header 高度 80px，背景 varBrandPrimary
☐ Gate Stepper 高度 50px，背景 varNeutralLighter
☐ 三個 Section 卡片，白底、圓角、邊框
☐ Footer 高度 72px，固定於底部
☐ Cancel 按鈕左側，Ghost 樣式
☐ Submit 按鈕右側，Primary 樣式
☐ 所有控制項已正確命名

常見錯誤：
1. 忘記執行 Run OnStart → 色彩變數未定義
2. 使用 Color.Blue 而非 varBrandPrimary → 色彩不一致
3. Section Y 座標寫死 → 響應式失效
4. 控制項使用預設名稱 → 維護困難
```

---

## 附錄 B：常見錯誤與排除

### B.1 色彩相關錯誤

| 錯誤現象 | 原因 | 解決方式 |
|:---------|:------|:---------|
| 「varBrandPrimary 未定義」 | 未執行 Run OnStart | 執行 App → Run OnStart |
| 色彩與標準不符 | 使用舊版 varColor* 變數 | 遷移至 varBrand* 變數 |
| 硬編碼色碼警告 | 使用 ColorValue("#xxx") | 改用變數引用 |

### B.2 Layout 相關錯誤

| 錯誤現象 | 原因 | 解決方式 |
|:---------|:------|:---------|
| Section 重疊 | Y 座標計算錯誤 | 使用相對座標公式 |
| Footer 不在底部 | Y 寫死數值 | 改用 Parent.Height - 72 |
| 響應式失效 | Width 寫死數值 | 改用 Parent.Width - 40 |

### B.3 控制項相關錯誤

| 錯誤現象 | 原因 | 解決方式 |
|:---------|:------|:---------|
| 公式引用錯誤 | 控制項使用預設名稱 | 依規範重命名 |
| DisplayMode 無效 | 回傳字串而非列舉 | 使用 DisplayMode.Edit |
| Flow-Only 欄位可編輯 | 使用 Text input | 改用 Label 控制項 |

---

## 版本歷史

| 版本 | 日期 | 變更說明 |
|:------|:------|:----------|
| v1.0 | 2026-02-11 | 初版建立 - 品牌 UI 設計標準 |
| v1.1 | 2026-02-11 | 統一雙權威、新增施工教學、極簡優化、穩定性 Guardrails |

### v1.1 變更摘要

| 變更項目 | 說明 |
|:---------|:------|
| 統一色彩系統 | 棄用 varColor*，統一使用 varBrand* |
| 極簡視覺 | 移除 Secondary Button、Warning Message、部分色階 |
| 施工教學 | 新增 Appendix A 完整建置步驟 |
| Stability Guardrails | 新增不可逆條款與擴充模式 |

---

## 棄用文件聲明

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  已棄用文件（DEPRECATED DOCUMENTS）                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  以下文件自 v1.1 生效後標記為【已棄用】：                                     │
│                                                                             │
│  1. appendix/Canvas-Brand-UI-Standard-v1.md                                 │
│  2. Canvas-UI-Governance-Standard-v1.md                                     │
│                                                                             │
│  禁止引用上述文件作為設計依據。                                               │
│  本文件（Canvas-Brand-UI-Standard-v1.1.md）為唯一權威。                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

**文件結束**

**本標準為治理系統 Canvas App UI 設計之唯一權威規範。**
**v1.1 為穩定版，禁止未經授權之變更。**
