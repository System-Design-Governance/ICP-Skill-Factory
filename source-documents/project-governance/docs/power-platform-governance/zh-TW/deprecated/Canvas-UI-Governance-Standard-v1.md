# Canvas UI Governance Design Standard v1.0

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ⚠️ 已棄用（DEPRECATED）                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  本文件已於 2026-02-11 棄用。                                                │
│                                                                             │
│  請改用：appendix/Canvas-Brand-UI-Standard-v1.1.md                          │
│                                                                             │
│  禁止引用本文件作為設計依據。                                                │
│  本文件使用之 varColor* 變數已全部棄用。                                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**文件版本**：v1.0 ❌ **已棄用**
**生效日期**：2026-02-11
**棄用日期**：2026-02-11
**替代文件**：appendix/Canvas-Brand-UI-Standard-v1.1.md
**文件擁有者**：System Design Governance Function
**核准單位**：Engineering Management
**文件性質**：設計標準（Design Standard）

---

## 文件宗旨與適用範圍

### 設計理念

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Canvas UI Governance Design Standard                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  本標準之核心原則：                                                          │
│                                                                             │
│  1. 一致性優先（Consistency First）                                          │
│     所有治理表單必須遵循統一視覺與操作規範                                    │
│                                                                             │
│  2. 治理語義可視化（Governance Semantics Visibility）                        │
│     使用者必須能從視覺設計中辨識治理限制                                      │
│                                                                             │
│  3. 防呆優先於效率（Fool-proof Over Efficiency）                             │
│     設計必須防止使用者誤操作，即使犧牲部分便利性                              │
│                                                                             │
│  4. Flow-Only 欄位明確標示（Flow-Only Field Marking）                        │
│     所有由 Flow 控制的欄位必須視覺上不可編輯                                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 適用範圍

| 適用對象 | 說明 |
|:---------|:------|
| 所有治理表單 | FORM-001 至 FORM-011 |
| 所有狀態顯示畫面 | 專案清單、詳情、審批記錄 |
| 未來新增表單 | 必須遵循本標準 |
| 第三方整合畫面 | 若顯示治理資料，必須遵循 |

### 不適用範圍

| 不適用對象 | 原因 |
|:-----------|:------|
| 非治理系統之 Canvas App | 超出本標準範疇 |
| Model-driven App | 使用不同設計模式 |
| Portal / Power Pages | 使用不同設計模式 |

---

## 不可變更條款（Freeze Items）

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ⛔ 不可變更條款（FREEZE ITEMS）                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  以下項目於 v1.0 封版後不可變更：                                            │
│                                                                             │
│  1. 畫面骨架結構（五區塊配置）                                               │
│  2. 控制項命名前綴規則                                                       │
│  3. 顏色語義定義                                                             │
│  4. Flow-Only 欄位視覺標識規則                                               │
│  5. 訊息區塊樣式                                                             │
│  6. Gate 視覺條配置                                                          │
│                                                                             │
│  任何對上述項目的變更請求必須：                                              │
│  - 提出書面變更申請                                                          │
│  - 經 Governance Lead 核准                                                   │
│  - 同步更新所有既有表單                                                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 第一章：全域 Form Layout Template

### 1.1 畫面骨架結構

所有治理表單必須採用以下五區塊配置：

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ① HEADER 區（headerContainer）                            Height: 80px    │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │ [Logo] [表單標題]                              [使用者資訊] [登出按鈕] ││
│  └─────────────────────────────────────────────────────────────────────────┘│
├─────────────────────────────────────────────────────────────────────────────┤
│  ② GATE 視覺條（gateStepperContainer）                      Height: 60px    │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │ ○ Pending ─── ○ Gate0 ─── ○ Gate1 ─── ○ Gate2 ─── ○ Gate3 ─── ○ Closed ││
│  └─────────────────────────────────────────────────────────────────────────┘│
├─────────────────────────────────────────────────────────────────────────────┤
│  ③ BODY 主體區（bodyContainer）                    Height: 動態（彈性填充） │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │  │
│  │  │  Section A：專案識別區（sectionProjectIdentity）                 │  │  │
│  │  │  RequestID、Title、Status 等識別資訊                            │  │  │
│  │  └─────────────────────────────────────────────────────────────────┘  │  │
│  │                                                                       │  │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │  │
│  │  │  Section B：使用者輸入區（sectionUserInput）                     │  │  │
│  │  │  可編輯欄位、選擇器                                              │  │  │
│  │  └─────────────────────────────────────────────────────────────────┘  │  │
│  │                                                                       │  │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │  │
│  │  │  Section C：系統資訊區（sectionSystemInfo）                      │  │  │
│  │  │  Flow-Only 欄位、唯讀狀態、時間戳記                              │  │  │
│  │  └─────────────────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────────────────────┤
│  ④ FOOTER 操作區（footerContainer）                         Height: 70px    │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │                                      [取消] [儲存草稿] [提交]         ││
│  └─────────────────────────────────────────────────────────────────────────┘│
├─────────────────────────────────────────────────────────────────────────────┤
│  ⑤ MESSAGE 訊息區（messageContainer）                       Height: 0-80px  │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │ [Success/Error/Warning Message Banner]                   [X 關閉]      ││
│  └─────────────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 區塊高度規範

| 區塊 | 高度 | 說明 |
|:------|:------|:------|
| Header | 80px | 固定高度，不可變更 |
| Gate Stepper | 60px | 固定高度；若表單不顯示 Gate 可隱藏（Visible: false） |
| Body | 動態 | `Parent.Height - 80 - 60 - 70` 或根據 Gate 顯示狀態調整 |
| Footer | 70px | 固定高度，不可變更 |
| Message | 0-80px | 預設隱藏，觸發時展開 80px |

### 1.3 區塊 Y 座標計算

| 區塊 | Y 座標公式 |
|:------|:-----------|
| Header | `0` |
| Gate Stepper | `80` |
| Body | `If(gateStepperContainer.Visible, 140, 80)` |
| Footer | `Parent.Height - 70` |
| Message | `0`（覆蓋於最上層） |

### 1.4 容器控制項設定

**headerContainer**：

```
控制項類型：Rectangle
名稱：headerContainer

屬性設定：
├── X: 0
├── Y: 0
├── Width: Parent.Width
├── Height: 80
├── Fill: varColorPrimary
└── BorderThickness: 0
```

**gateStepperContainer**：

```
控制項類型：Rectangle
名稱：gateStepperContainer

屬性設定：
├── X: 0
├── Y: 80
├── Width: Parent.Width
├── Height: 60
├── Fill: varColorNeutralLight
├── BorderThickness: 0
└── Visible: varShowGateStepper
```

**bodyContainer**：

```
控制項類型：Rectangle
名稱：bodyContainer

屬性設定：
├── X: 0
├── Y: If(gateStepperContainer.Visible, 140, 80)
├── Width: Parent.Width
├── Height: Parent.Height - Self.Y - 70
├── Fill: varColorBackground
└── BorderThickness: 0
```

**footerContainer**：

```
控制項類型：Rectangle
名稱：footerContainer

屬性設定：
├── X: 0
├── Y: Parent.Height - 70
├── Width: Parent.Width
├── Height: 70
├── Fill: Color.White
├── BorderColor: varColorNeutralBorder
└── BorderThickness: 1 (top only via nested element)
```

---

## 第二章：Gate 視覺條設計（Stepper）

### 2.1 Stepper 結構

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   ●──────●──────●──────○──────○──────○                                      │
│   │      │      │      │      │      │                                      │
│ Pending Gate0  Gate1  Gate2  Gate3  Closed                                  │
│                  ▲                                                          │
│              目前位置                                                        │
│                                                                             │
│  圖例：                                                                      │
│  ● 已完成（Completed）：Fill = varColorSuccess                              │
│  ◉ 目前位置（Current）：Fill = varColorPrimary, 放大 1.2x                   │
│  ○ 未達（Pending）：Fill = varColorNeutral                                  │
│  ━ 已完成連線：Stroke = varColorSuccess                                     │
│  ─ 未達連線：Stroke = varColorNeutral                                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Stepper 控制項命名

| 控制項 | 名稱 | 類型 |
|:--------|:------|:------|
| 步驟圓點 | `icoStep_Pending`, `icoStep_Gate0`, ... | Icon (Circle) |
| 步驟標籤 | `lblStep_Pending`, `lblStep_Gate0`, ... | Label |
| 連接線 | `lineStep_0to1`, `lineStep_1to2`, ... | Rectangle |

### 2.3 Stepper Icon Fill 公式

```
// icoStep_Gate0.Fill
Switch(
    varCurrentGate,
    "Pending", varColorNeutral,
    "Gate0", varColorPrimary,
    varColorSuccess
)

// icoStep_Gate1.Fill
Switch(
    varCurrentGate,
    "Pending", varColorNeutral,
    "Gate0", varColorNeutral,
    "Gate1", varColorPrimary,
    varColorSuccess
)

// 通用公式模式
If(
    gateIndex < currentGateIndex,
    varColorSuccess,                    // 已完成
    If(
        gateIndex = currentGateIndex,
        varColorPrimary,                // 目前
        varColorNeutral                 // 未達
    )
)
```

### 2.4 Gate Index 對照表

| Gate 名稱 | Index | 說明 |
|:----------|:-------|:------|
| Pending | 0 | 初始狀態（PreGate0） |
| Gate0 | 1 | 可行性評估完成 |
| Gate1 | 2 | 設計基線完成 |
| Gate2 | 3 | 實作驗證完成 |
| Gate3 | 4 | 交付完成 |
| Closed | 5 | 專案關閉 |

---

## 第三章：Body 主體區三區塊分組

### 3.1 三區塊強制分組

所有表單的 Body 區必須包含以下三個 Section：

| Section | 名稱 | 用途 | 背景色 |
|:---------|:------|:------|:--------|
| Section A | sectionProjectIdentity | 專案識別資訊（RequestID、Title、Status） | `varColorNeutralLight` |
| Section B | sectionUserInput | 使用者可編輯欄位 | `Color.White` |
| Section C | sectionSystemInfo | Flow-Only 欄位、系統資訊 | `varColorFlowOnlyBg` |

### 3.2 Section 容器設定

**sectionProjectIdentity**：

```
控制項類型：Rectangle
名稱：sectionProjectIdentity

屬性設定：
├── X: 20
├── Y: bodyContainer.Y + 20
├── Width: Parent.Width - 40
├── Height: 100
├── Fill: varColorNeutralLight
├── BorderRadius: 8
└── BorderThickness: 0

內含控制項：
├── lblSectionA_Title: "專案識別"
├── lblRequestID: RequestID 顯示
├── lblProjectTitle: 專案名稱顯示
└── lblProjectStatus: 專案狀態 Badge
```

**sectionUserInput**：

```
控制項類型：Rectangle
名稱：sectionUserInput

屬性設定：
├── X: 20
├── Y: sectionProjectIdentity.Y + sectionProjectIdentity.Height + 20
├── Width: Parent.Width - 40
├── Height: 動態計算（依欄位數量）
├── Fill: Color.White
├── BorderRadius: 8
├── BorderColor: varColorNeutralBorder
└── BorderThickness: 1

內含控制項：
├── lblSectionB_Title: "表單資料"
├── 所有使用者可編輯欄位
└── 欄位標籤與輸入控制項
```

**sectionSystemInfo**：

```
控制項類型：Rectangle
名稱：sectionSystemInfo

屬性設定：
├── X: 20
├── Y: sectionUserInput.Y + sectionUserInput.Height + 20
├── Width: Parent.Width - 40
├── Height: 動態計算
├── Fill: varColorFlowOnlyBg
├── BorderRadius: 8
└── BorderThickness: 0

內含控制項：
├── lblSectionC_Title: "系統資訊（唯讀）"
├── Flow-Only 欄位（灰底顯示）
├── 時間戳記
└── 建立者/修改者
```

### 3.3 Section 標題樣式

```
// Section 標題統一樣式
lblSection_Title 共用屬性：
├── Font: Segoe UI Semibold
├── Size: 14
├── Color: varColorNeutral
├── Height: 24
├── PaddingLeft: 12
└── PaddingTop: 8
```

---

## 第四章：顏色與語義規範

### 4.1 核心色彩定義

**App.OnStart 必須包含以下色彩定義**：

```
// ═══════════════════════════════════════════════════════════
// 核心色彩定義（Governance Color Palette）
// ═══════════════════════════════════════════════════════════

// Primary（主色）- Microsoft Fluent Blue
Set(varColorPrimary, ColorValue("#0078D4"));
Set(varColorPrimaryHover, ColorValue("#106EBE"));
Set(varColorPrimaryPressed, ColorValue("#005A9E"));

// Success（成功）- Microsoft Fluent Green
Set(varColorSuccess, ColorValue("#107C10"));
Set(varColorSuccessLight, ColorValue("#DFF6DD"));

// Danger（危險/錯誤）- Microsoft Fluent Red
Set(varColorDanger, ColorValue("#D13438"));
Set(varColorDangerLight, ColorValue("#FDE7E9"));

// Warning（警告）- Microsoft Fluent Yellow
Set(varColorWarning, ColorValue("#FFB900"));
Set(varColorWarningLight, ColorValue("#FFF4CE"));

// Neutral（中性）- Microsoft Fluent Gray
Set(varColorNeutral, ColorValue("#605E5C"));
Set(varColorNeutralLight, ColorValue("#F3F2F1"));
Set(varColorNeutralBorder, ColorValue("#EDEBE9"));

// Background（背景）
Set(varColorBackground, ColorValue("#FAF9F8"));

// Flow-Only 欄位背景（強調不可編輯）
Set(varColorFlowOnlyBg, ColorValue("#F0F0F0"));
Set(varColorFlowOnlyBorder, ColorValue("#D2D0CE"));

// Text（文字）
Set(varColorTextPrimary, ColorValue("#323130"));
Set(varColorTextSecondary, ColorValue("#605E5C"));
Set(varColorTextDisabled, ColorValue("#A19F9D"));
Set(varColorTextOnPrimary, ColorValue("#FFFFFF"));
```

### 4.2 顏色語義對照表

| 語義 | 變數名稱 | 色碼 | 使用情境 |
|:------|:---------|:------|:---------|
| 主要操作 | varColorPrimary | #0078D4 | 提交按鈕、主要連結、目前 Gate |
| 成功狀態 | varColorSuccess | #107C10 | 成功訊息、已完成 Gate |
| 錯誤狀態 | varColorDanger | #D13438 | 錯誤訊息、必填警告、刪除按鈕 |
| 警告狀態 | varColorWarning | #FFB900 | 警告訊息、待處理項目 |
| 中性資訊 | varColorNeutral | #605E5C | 標籤、說明文字、未達 Gate |
| Flow-Only | varColorFlowOnlyBg | #F0F0F0 | 系統欄位背景、唯讀區塊 |

### 4.3 顏色使用禁止事項

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ⛔ 顏色使用禁止事項                                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ✗ 禁止使用硬編碼色碼                                                        │
│    錯誤：Fill: ColorValue("#0078D4")                                        │
│    正確：Fill: varColorPrimary                                              │
│                                                                             │
│  ✗ 禁止在非錯誤情境使用 Danger 色                                            │
│    錯誤：將一般按鈕設為紅色                                                  │
│    正確：僅刪除、取消、錯誤訊息使用紅色                                      │
│                                                                             │
│  ✗ 禁止在非成功情境使用 Success 色                                           │
│    錯誤：將主要按鈕設為綠色                                                  │
│    正確：僅成功訊息、已完成狀態使用綠色                                      │
│                                                                             │
│  ✗ 禁止自定義新色彩                                                          │
│    錯誤：Set(varMyCustomColor, ColorValue("#123456"))                       │
│    正確：使用本標準定義之色彩變數                                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 第五章：Badge 樣式規則

### 5.1 Badge 類型定義

| Badge 類型 | 用途 | 背景色 | 文字色 | 邊框 |
|:-----------|:------|:--------|:--------|:------|
| Primary | 目前狀態、主要標籤 | varColorPrimary | White | 無 |
| Success | 已完成、通過 | varColorSuccess | White | 無 |
| Danger | 失敗、違規 | varColorDanger | White | 無 |
| Warning | 待審核、注意 | varColorWarning | Black | 無 |
| Neutral | 一般資訊 | varColorNeutralLight | varColorTextPrimary | varColorNeutralBorder |
| Outline | 次要資訊 | Transparent | varColorPrimary | varColorPrimary |

### 5.2 Badge 控制項設定

**Badge 容器**：

```
控制項類型：Button（DisplayMode: View）
名稱前綴：badge[狀態名稱]

共用屬性：
├── Height: 24
├── PaddingLeft: 12
├── PaddingRight: 12
├── BorderRadius: 12（圓角膠囊形）
├── Font: Segoe UI Semibold
├── Size: 12
└── DisplayMode: DisplayMode.View（不可點擊）
```

**Badge 樣式公式**：

```
// 狀態 Badge 動態樣式
// badgeStatus.Fill
Switch(
    varSelectedProject.gov_projectstatus,
    "Active", varColorSuccess,
    "OnHold", varColorWarning,
    "Closed", varColorNeutral,
    "Terminated", varColorDanger,
    varColorNeutralLight
)

// badgeStatus.Color（文字色）
Switch(
    varSelectedProject.gov_projectstatus,
    "Active", Color.White,
    "OnHold", varColorTextPrimary,
    "Closed", Color.White,
    "Terminated", Color.White,
    varColorTextPrimary
)
```

### 5.3 Gate Badge 樣式

| Gate | Badge Fill | Badge Color |
|:------|:-----------|:-------------|
| Pending | varColorNeutralLight | varColorTextPrimary |
| Gate0 | varColorPrimary | White |
| Gate1 | varColorPrimary | White |
| Gate2 | varColorPrimary | White |
| Gate3 | varColorSuccess | White |
| Closed | varColorNeutral | White |
| Terminated | varColorDanger | White |

---

## 第六章：Button 樣式語義

### 6.1 Button 類型定義

| Button 類型 | 用途 | Fill | Color | BorderColor |
|:------------|:------|:------|:-------|:-------------|
| Primary | 主要操作（提交） | varColorPrimary | White | 無 |
| Secondary | 次要操作（儲存草稿） | White | varColorPrimary | varColorPrimary |
| Danger | 危險操作（刪除、取消申請） | varColorDanger | White | 無 |
| Ghost | 輔助操作（取消、返回） | Transparent | varColorNeutral | 無 |
| Disabled | 停用狀態 | varColorNeutralLight | varColorTextDisabled | varColorNeutralBorder |

### 6.2 Button 控制項設定

**Primary Button**：

```
控制項名稱：btnSubmit

屬性設定：
├── Fill: If(Self.DisplayMode = DisplayMode.Edit, varColorPrimary, varColorNeutralLight)
├── Color: If(Self.DisplayMode = DisplayMode.Edit, Color.White, varColorTextDisabled)
├── HoverFill: varColorPrimaryHover
├── PressedFill: varColorPrimaryPressed
├── BorderRadius: 4
├── Height: 40
├── PaddingLeft: 24
├── PaddingRight: 24
├── Font: Segoe UI Semibold
└── Size: 14
```

**Secondary Button**：

```
控制項名稱：btnSaveDraft

屬性設定：
├── Fill: Color.White
├── Color: varColorPrimary
├── BorderColor: varColorPrimary
├── BorderThickness: 1
├── HoverFill: varColorNeutralLight
├── BorderRadius: 4
├── Height: 40
└── Font: Segoe UI Semibold
```

**Ghost Button**：

```
控制項名稱：btnCancel

屬性設定：
├── Fill: Transparent
├── Color: varColorNeutral
├── BorderThickness: 0
├── HoverFill: varColorNeutralLight
├── Height: 40
└── Font: Segoe UI
```

### 6.3 Button 排列規則

```
Footer 區 Button 排列（由右至左）：

┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│                          [Ghost]  [Secondary]  [Primary]                    │
│                          取消      儲存草稿      提交                         │
│                                                                             │
│  間距規範：                                                                   │
│  ├── Button 間距：12px                                                       │
│  ├── 最右側 Button 距離右邊界：20px                                           │
│  └── 最左側 Button 距離左邊界：不限（靠右對齊）                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 第七章：控制項操作標準

### 7.1 Flow-Only 欄位視覺規則

**定義**：Flow-Only 欄位指僅能由 Power Automate Flow 寫入的欄位，使用者不可編輯。

**視覺標識**：

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Flow-Only 欄位視覺規格                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  必須符合以下規格：                                                          │
│                                                                             │
│  1. 背景色：varColorFlowOnlyBg（#F0F0F0）                                    │
│  2. 邊框色：varColorFlowOnlyBorder（#D2D0CE）                                │
│  3. 控制項類型：Label（不使用 Text input）                                   │
│  4. 標籤後綴：加註「（系統產生）」或「（唯讀）」                              │
│  5. 群組位置：統一放置於 sectionSystemInfo                                   │
│                                                                             │
│  ┌────────────────────────────────────────────┐                             │
│  │  系統資訊（唯讀）                           │ ← Section 標題              │
│  │  ┌────────────────────────────────────────┐│                             │
│  │  │  Request ID（系統產生）                ││ ← 欄位標籤                  │
│  │  │  ┌────────────────────────────────────┐││                             │
│  │  │  │  DR-2026-00001234                  │││ ← 灰底 Label                │
│  │  │  └────────────────────────────────────┘││                             │
│  │  └────────────────────────────────────────┘│                             │
│  └────────────────────────────────────────────┘                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Flow-Only 欄位清單**：

| 欄位 | Schema Name | 說明 |
|:------|:-------------|:------|
| Request ID | gov_requestid | 流水號 |
| Current Gate | gov_currentgate | 目前 Gate |
| Request Status | gov_requeststatus | 申請狀態 |
| Project Status | gov_projectstatus | 專案狀態 |
| Document Freeze Status | gov_documentfreezestatus | 文件凍結狀態 |
| Created On | createdon | 建立時間 |
| Modified On | modifiedon | 修改時間 |
| Created By | createdby | 建立者 |
| Owner | ownerid | 擁有者（必須為 Flow SP） |

### 7.2 DisplayMode 標準寫法

**Pattern A：必填欄位驗證**

```
// btnSubmit.DisplayMode
// 所有必填欄位皆已填寫時啟用

If(
    And(
        !IsBlank(txtField1.Text),
        !IsBlank(txtField2.Text),
        !IsBlank(cmbField3.Selected),
        !IsBlank(ddField4.Selected),
        !varIsLoading
    ),
    DisplayMode.Edit,
    DisplayMode.Disabled
)
```

**Pattern B：狀態條件驗證**

```
// btnGateRequest.DisplayMode
// 專案狀態為 Active 且無進行中申請時啟用

If(
    And(
        varSelectedProject.gov_projectstatus = "Active",
        varSelectedProject.gov_requeststatus = "None",
        !varIsLoading
    ),
    DisplayMode.Edit,
    DisplayMode.Disabled
)
```

**Pattern C：角色條件驗證**

```
// btnApprove.DisplayMode
// 僅審批者可操作

If(
    And(
        varCurrentUserEmail in varApproverList,
        varSelectedRequest.gov_requeststatus = "UnderReview",
        !varIsLoading
    ),
    DisplayMode.Edit,
    DisplayMode.Disabled
)
```

### 7.3 DisplayMode 禁止寫法

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ⛔ DisplayMode 禁止寫法                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ✗ 禁止：回傳字串而非列舉值                                                  │
│    錯誤：If(條件, "Edit", "Disabled")                                        │
│    正確：If(條件, DisplayMode.Edit, DisplayMode.Disabled)                   │
│                                                                             │
│  ✗ 禁止：回傳布林值                                                          │
│    錯誤：If(條件, true, false)                                               │
│    正確：If(條件, DisplayMode.Edit, DisplayMode.Disabled)                   │
│                                                                             │
│  ✗ 禁止：缺少 else 分支                                                      │
│    錯誤：If(條件, DisplayMode.Edit)                                          │
│    正確：If(條件, DisplayMode.Edit, DisplayMode.Disabled)                   │
│                                                                             │
│  ✗ 禁止：硬編碼 DisplayMode.View                                             │
│    錯誤：DisplayMode.View（永久唯讀）                                        │
│    正確：使用 Label 控制項替代唯讀 Text input                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 第八章：訊息區塊標準

### 8.1 Success Message 標準組件

**結構**：

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ✓ 操作成功                                                            [X]  │
│   Request ID: DR-2026-00001234                                              │
└─────────────────────────────────────────────────────────────────────────────┘

控制項組成：
├── rectSuccessBanner（背景）
├── icoSuccessIcon（勾選圖示）
├── lblSuccessTitle（標題）
├── lblSuccessMessage（詳細訊息）
└── icoCloseSuccess（關閉按鈕）
```

**控制項設定**：

```
rectSuccessBanner:
├── Fill: varColorSuccessLight
├── Height: 80
├── Visible: varShowSuccess

icoSuccessIcon:
├── Icon: Icon.CheckMark
├── Color: varColorSuccess
├── Width: 24
├── Height: 24

lblSuccessTitle:
├── Text: "操作成功"
├── Font: Segoe UI Semibold
├── Size: 16
├── Color: varColorSuccess

lblSuccessMessage:
├── Text: varSuccessMessage
├── Font: Segoe UI
├── Size: 14
├── Color: varColorTextPrimary

icoCloseSuccess:
├── Icon: Icon.Cancel
├── Color: varColorNeutral
├── OnSelect: Set(varShowSuccess, false)
```

### 8.2 Error Message 標準區塊

**結構**：

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ✗ 操作失敗                                                            [X]  │
│   錯誤代碼: ERR-001-002                                                     │
│   錯誤訊息: 您沒有執行此操作的權限                                           │
└─────────────────────────────────────────────────────────────────────────────┘

控制項組成：
├── rectErrorBanner（背景）
├── icoErrorIcon（錯誤圖示）
├── lblErrorTitle（標題）
├── lblErrorCode（錯誤代碼）
├── lblErrorMessage（詳細訊息）
└── icoCloseError（關閉按鈕）
```

**控制項設定**：

```
rectErrorBanner:
├── Fill: varColorDangerLight
├── Height: 100
├── Visible: varShowError

icoErrorIcon:
├── Icon: Icon.Warning
├── Color: varColorDanger
├── Width: 24
├── Height: 24

lblErrorTitle:
├── Text: "操作失敗"
├── Font: Segoe UI Semibold
├── Size: 16
├── Color: varColorDanger

lblErrorCode:
├── Text: "錯誤代碼: " & varErrorCode
├── Font: Segoe UI
├── Size: 12
├── Color: varColorTextSecondary

lblErrorMessage:
├── Text: varErrorMessage
├── Font: Segoe UI
├── Size: 14
├── Color: varColorTextPrimary
```

### 8.3 Warning Message 標準區塊

**結構**：

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ⚠ 注意事項                                                            [X]  │
│   此操作將進入審批流程，提交後無法自行撤銷                                   │
└─────────────────────────────────────────────────────────────────────────────┘

控制項組成：
├── rectWarningBanner（背景）
├── icoWarningIcon（警告圖示）
├── lblWarningTitle（標題）
├── lblWarningMessage（詳細訊息）
└── icoCloseWarning（關閉按鈕）
```

**控制項設定**：

```
rectWarningBanner:
├── Fill: varColorWarningLight
├── Height: 80
├── Visible: varShowWarning

icoWarningIcon:
├── Icon: Icon.Warning
├── Color: varColorWarning
├── Width: 24
├── Height: 24

lblWarningTitle:
├── Text: varWarningTitle
├── Font: Segoe UI Semibold
├── Size: 16
├── Color: varColorTextPrimary
```

### 8.4 訊息區塊層級順序

```
訊息區塊必須位於最上層：

控制項層級（從上到下）：
├── rectLoadingOverlay    ← 最上層（載入遮罩）
├── lblLoadingText
├── rectSuccessBanner     ← 訊息區塊層
├── rectErrorBanner
├── rectWarningBanner
├── icoClose* 系列
├── lbl*Message 系列
├── headerContainer       ← 畫面結構層
├── gateStepperContainer
├── bodyContainer
├── footerContainer
└── 其他控制項
```

---

## 第九章：控制項命名規則

### 9.1 命名前綴規範

| 控制項類型 | 前綴 | 範例 |
|:-----------|:------|:------|
| Label | lbl | lblTitle, lblErrorMessage |
| Text input | txt | txtTitle, txtDescription |
| Dropdown | dd | ddProjectType, ddTargetSL |
| ComboBox | cmb | cmbProjectManager, cmbProject |
| Button | btn | btnSubmit, btnCancel |
| Rectangle | rect | rectHeader, rectErrorBanner |
| Icon | ico | icoClose, icoSuccess |
| Gallery | gal | galProjects, galAuditLog |
| Date picker | dt | dtExpectedDate |
| Toggle | tgl | tglEnableNotification |
| Checkbox | chk | chkAgreeTerms |
| Radio | rdo | rdoOption1 |
| Image | img | imgLogo |
| Screen | scr | scrHome, scrCreateProject |

### 9.2 命名結構規範

**格式**：`[前綴][區塊][功能描述]`

| 組成部分 | 說明 | 範例 |
|:---------|:------|:------|
| 前綴 | 控制項類型識別 | lbl, txt, btn |
| 區塊 | 所屬區塊識別（選用） | Header, SectionA, Footer |
| 功能描述 | 功能說明（PascalCase） | Title, ProjectManager, Submit |

**範例**：

```
lblHeaderTitle          ← Header 區的標題 Label
txtSectionB_Title       ← Section B 的標題輸入框
btnFooterSubmit         ← Footer 區的提交按鈕
rectSectionA            ← Section A 的背景矩形
```

### 9.3 禁止命名

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ⛔ 禁止命名                                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ✗ 禁止：使用預設名稱                                                        │
│    錯誤：TextInput1, Button2, Label3                                        │
│    正確：txtTitle, btnSubmit, lblStatus                                     │
│                                                                             │
│  ✗ 禁止：使用空格                                                            │
│    錯誤：btn Submit, lbl Project Title                                      │
│    正確：btnSubmit, lblProjectTitle                                         │
│                                                                             │
│  ✗ 禁止：使用特殊字元                                                        │
│    錯誤：btn-submit, lbl_title                                              │
│    正確：btnSubmit, lblTitle                                                │
│                                                                             │
│  ✗ 禁止：使用純數字開頭                                                      │
│    錯誤：1stButton, 2ndLabel                                                │
│    正確：btnFirst, lblSecond                                                │
│                                                                             │
│  ✗ 禁止：使用中文命名                                                        │
│    錯誤：btn提交, lbl標題                                                    │
│    正確：btnSubmit, lblTitle                                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 第十章：間距規範

### 10.1 間距定義

| 間距類型 | 值 | 使用情境 |
|:---------|:-----|:---------|
| xs | 4px | 圖示與文字間距 |
| sm | 8px | 同組控制項間距 |
| md | 12px | Button 間距、欄位內部間距 |
| lg | 20px | Section 間距、邊界間距 |
| xl | 32px | 大區塊間距 |

### 10.2 間距應用規則

**欄位標籤與輸入框**：

```
┌────────────────────────────────────────┐
│  專案名稱 *                   ← Label  │
│           ↓ 4px (xs)                   │
│  ┌────────────────────────────────────┐│
│  │  [輸入框]                          ││
│  └────────────────────────────────────┘│
│           ↓ 20px (lg)                  │
│  專案類型 *                   ← Label  │
│           ↓ 4px (xs)                   │
│  ┌────────────────────────────────────┐│
│  │  [下拉選單]                        ││
│  └────────────────────────────────────┘│
└────────────────────────────────────────┘
```

**Section 間距**：

```
┌────────────────────────────────────────┐
│  ↑ 20px (lg) 距離 Body 頂部            │
│  ┌────────────────────────────────────┐│
│  │  Section A                         ││
│  └────────────────────────────────────┘│
│  ↓ 20px (lg)                           │
│  ┌────────────────────────────────────┐│
│  │  Section B                         ││
│  └────────────────────────────────────┘│
│  ↓ 20px (lg)                           │
│  ┌────────────────────────────────────┐│
│  │  Section C                         ││
│  └────────────────────────────────────┘│
│  ↓ 20px (lg) 距離 Footer               │
└────────────────────────────────────────┘
```

**Button 間距**：

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                    [取消]  [儲存草稿]  [提交]               │
│                        ↑       ↑       ↑                    │
│                        └──12px─┴──12px─┘                    │
│                                         ↑                   │
│                                    20px 距離右邊界           │
└─────────────────────────────────────────────────────────────┘
```

---

## 第十一章：未來新增表單必須遵守原則

### 11.1 新增表單檢查清單

任何新增表單必須通過以下檢查：

**結構檢查**：

- [ ] 畫面採用五區塊配置（Header, Gate Stepper, Body, Footer, Message）
- [ ] Body 區包含三個 Section（ProjectIdentity, UserInput, SystemInfo）
- [ ] 所有容器命名符合規範
- [ ] 控制項層級順序正確

**顏色檢查**：

- [ ] 僅使用本標準定義之顏色變數
- [ ] 無硬編碼色碼
- [ ] 顏色語義正確（Success 僅用於成功、Danger 僅用於錯誤）

**控制項檢查**：

- [ ] 所有控制項已重命名（無 TextInput1 等預設名稱）
- [ ] 命名前綴正確
- [ ] Flow-Only 欄位使用 Label 並放置於 sectionSystemInfo
- [ ] DisplayMode 公式符合標準寫法

**訊息區塊檢查**：

- [ ] 包含 Success Message 區塊
- [ ] 包含 Error Message 區塊
- [ ] 訊息區塊位於最上層

**Button 檢查**：

- [ ] Primary Button 用於主要操作
- [ ] Secondary Button 用於次要操作
- [ ] Ghost Button 用於取消/返回
- [ ] Button 排列符合規範（靠右對齊）

### 11.2 新增表單審核流程

```
新增表單審核流程：

┌─────────────────┐
│ 1. 開發表單      │
└────────┬────────┘
         ↓
┌─────────────────┐
│ 2. 自我檢查     │ ← 使用 11.1 檢查清單
└────────┬────────┘
         ↓
┌─────────────────┐
│ 3. 同儕審查     │ ← 另一位開發者審核
└────────┬────────┘
         ↓
┌─────────────────┐
│ 4. UI 標準審核  │ ← UX Governance Specialist 審核
└────────┬────────┘
         ↓
┌─────────────────┐
│ 5. 合併至 App   │
└─────────────────┘
```

---

## 第十二章：禁止事項總覽

### 12.1 結構禁止事項

| 禁止項目 | 原因 |
|:---------|:------|
| 跳過五區塊配置 | 破壞一致性 |
| Body 區不分三個 Section | 破壞資訊分類 |
| 將 Flow-Only 欄位放入 UserInput 區 | 誤導使用者 |
| 使用非標準容器命名 | 增加維護難度 |

### 12.2 顏色禁止事項

| 禁止項目 | 原因 |
|:---------|:------|
| 硬編碼色碼 | 無法統一變更 |
| 自定義新顏色 | 破壞設計系統 |
| 錯誤使用顏色語義 | 誤導使用者 |

### 12.3 控制項禁止事項

| 禁止項目 | 原因 |
|:---------|:------|
| 保留預設控制項名稱 | 公式難以維護 |
| 使用 Text input 顯示 Flow-Only 欄位 | 可能誤導使用者嘗試編輯 |
| DisplayMode 回傳非列舉值 | 導致錯誤 |

### 12.4 治理禁止事項

| 禁止項目 | 原因 |
|:---------|:------|
| SubmitForm() 寫入治理表 | 繞過 Flow 驗證 |
| Patch() 寫入治理表 | 繞過 Flow 驗證 |
| 硬編碼 Flow URL | 破壞環境隔離 |
| 直接修改狀態欄位 | 破壞治理完整性 |

---

## 附錄 A：App.OnStart 完整模板

```
// ═══════════════════════════════════════════════════════════
// App.OnStart - Governance Canvas App 標準模板
// 版本：v1.0
// 最後更新：2026-02-11
// ═══════════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────────────
// Section 1: 使用者資訊
// ─────────────────────────────────────────────────────────────
Set(varCurrentUser, User());
Set(varCurrentUserEmail, User().Email);
Set(varCurrentUserName, User().FullName);

// ─────────────────────────────────────────────────────────────
// Section 2: 顯示控制變數
// ─────────────────────────────────────────────────────────────
Set(varIsLoading, false);
Set(varShowSuccess, false);
Set(varShowError, false);
Set(varShowWarning, false);
Set(varShowGateStepper, true);

// ─────────────────────────────────────────────────────────────
// Section 3: 訊息內容變數
// ─────────────────────────────────────────────────────────────
Set(varSuccessMessage, "");
Set(varErrorMessage, "");
Set(varErrorCode, "");
Set(varWarningTitle, "");
Set(varWarningMessage, "");

// ─────────────────────────────────────────────────────────────
// Section 4: 核心色彩定義（Governance Color Palette）
// ─────────────────────────────────────────────────────────────

// Primary（主色）
Set(varColorPrimary, ColorValue("#0078D4"));
Set(varColorPrimaryHover, ColorValue("#106EBE"));
Set(varColorPrimaryPressed, ColorValue("#005A9E"));

// Success（成功）
Set(varColorSuccess, ColorValue("#107C10"));
Set(varColorSuccessLight, ColorValue("#DFF6DD"));

// Danger（危險/錯誤）
Set(varColorDanger, ColorValue("#D13438"));
Set(varColorDangerLight, ColorValue("#FDE7E9"));

// Warning（警告）
Set(varColorWarning, ColorValue("#FFB900"));
Set(varColorWarningLight, ColorValue("#FFF4CE"));

// Neutral（中性）
Set(varColorNeutral, ColorValue("#605E5C"));
Set(varColorNeutralLight, ColorValue("#F3F2F1"));
Set(varColorNeutralBorder, ColorValue("#EDEBE9"));

// Background（背景）
Set(varColorBackground, ColorValue("#FAF9F8"));

// Flow-Only 欄位
Set(varColorFlowOnlyBg, ColorValue("#F0F0F0"));
Set(varColorFlowOnlyBorder, ColorValue("#D2D0CE"));

// Text（文字）
Set(varColorTextPrimary, ColorValue("#323130"));
Set(varColorTextSecondary, ColorValue("#605E5C"));
Set(varColorTextDisabled, ColorValue("#A19F9D"));
Set(varColorTextOnPrimary, ColorValue("#FFFFFF"));

// ─────────────────────────────────────────────────────────────
// Section 5: 間距變數
// ─────────────────────────────────────────────────────────────
Set(varSpacingXS, 4);
Set(varSpacingSM, 8);
Set(varSpacingMD, 12);
Set(varSpacingLG, 20);
Set(varSpacingXL, 32);

// ─────────────────────────────────────────────────────────────
// Section 6: 區塊高度常數
// ─────────────────────────────────────────────────────────────
Set(varHeaderHeight, 80);
Set(varGateStepperHeight, 60);
Set(varFooterHeight, 70);
Set(varMessageHeight, 80);

// ─────────────────────────────────────────────────────────────
// Section 7: Flow 回傳結果預設值
// ─────────────────────────────────────────────────────────────
Set(varResult, {Status: "", Message: "", RequestID: "", ErrorCode: ""})
```

---

## 附錄 B：表單畫面模板

### B.1 完整畫面結構模板

```
Screen: scrFormTemplate

控制項結構：
│
├── 訊息層（最上層）
│   ├── rectLoadingOverlay
│   ├── lblLoadingText
│   ├── rectSuccessBanner
│   ├── icoSuccessIcon
│   ├── lblSuccessTitle
│   ├── lblSuccessMessage
│   ├── icoCloseSuccess
│   ├── rectErrorBanner
│   ├── icoErrorIcon
│   ├── lblErrorTitle
│   ├── lblErrorCode
│   ├── lblErrorMessage
│   ├── icoCloseError
│   ├── rectWarningBanner
│   ├── icoWarningIcon
│   ├── lblWarningTitle
│   ├── lblWarningMessage
│   └── icoCloseWarning
│
├── 結構層
│   ├── headerContainer
│   │   ├── imgLogo
│   │   ├── lblHeaderTitle
│   │   ├── lblUserName
│   │   └── btnLogout
│   │
│   ├── gateStepperContainer
│   │   ├── icoStep_Pending
│   │   ├── lblStep_Pending
│   │   ├── lineStep_0to1
│   │   ├── icoStep_Gate0
│   │   ├── lblStep_Gate0
│   │   ├── ... (其他 Gate 步驟)
│   │   └── lblStep_Closed
│   │
│   ├── bodyContainer
│   │   ├── sectionProjectIdentity
│   │   │   ├── lblSectionA_Title
│   │   │   ├── lblRequestID
│   │   │   ├── lblProjectTitle
│   │   │   └── badgeProjectStatus
│   │   │
│   │   ├── sectionUserInput
│   │   │   ├── lblSectionB_Title
│   │   │   ├── lblField1Label
│   │   │   ├── txtField1
│   │   │   ├── ... (其他輸入欄位)
│   │   │   └── txtLastField
│   │   │
│   │   └── sectionSystemInfo
│   │       ├── lblSectionC_Title
│   │       ├── lblCreatedOnLabel
│   │       ├── lblCreatedOnValue
│   │       ├── lblCreatedByLabel
│   │       └── lblCreatedByValue
│   │
│   └── footerContainer
│       ├── btnCancel
│       ├── btnSaveDraft
│       └── btnSubmit
```

---

## 版本歷史

| 版本 | 日期 | 變更說明 |
|:------|:------|:----------|
| v1.0 | 2026-02-11 | 初版建立 |

---

**文件結束**

**本標準為治理系統 UI 設計之唯一依據。**
**未經核准，不得變更不可變更條款（Freeze Items）。**
