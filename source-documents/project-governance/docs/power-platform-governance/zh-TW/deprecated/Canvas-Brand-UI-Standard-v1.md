# Canvas Brand UI Standard v1.0

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
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**文件版本**：v1.0 ❌ **已棄用**
**生效日期**：2026-02-11
**棄用日期**：2026-02-11
**替代文件**：Canvas-Brand-UI-Standard-v1.1.md
**文件擁有者**：System Design Governance Function
**核准單位**：Engineering Management
**文件性質**：品牌 UI 設計標準（Brand UI Design Standard）

---

## 文件宗旨

本標準為治理系統所有 Canvas App 表單之**唯一品牌視覺規範**。

所有新建或修改之表單必須遵循本標準，確保：
- 品牌一致性
- 專業視覺呈現
- 簡潔直觀操作
- 傻瓜可執行性

---

## 第一章：品牌色彩系統

### 1.1 核心色彩定義

| 色彩名稱 | 色碼 | RGB | 用途 |
|:---------|:------|:-----|:------|
| **Brand Primary** | #0C3467 | 12, 52, 103 | Header、主標題、Primary Button、目前 Gate |
| **Brand Accent** | #008EC3 | 0, 142, 195 | Focus 邊框、Hyperlink、輕量強調 |
| **Neutral Gray** | #999999 | 153, 153, 153 | Readonly、Disabled、輔助文字 |
| **Text Base** | #2D2D2D | 45, 45, 45 | 內文主字色 |
| **Danger** | #A4262C | 164, 38, 44 | 終止操作、錯誤訊息 |
| **Success** | #107C10 | 16, 124, 16 | 成功訊息、已完成狀態 |
| **Warning** | #FFB900 | 255, 185, 0 | 警告訊息 |
| **Background** | #F5F5F5 | 245, 245, 245 | 頁面背景 |
| **Card White** | #FFFFFF | 255, 255, 255 | Section 卡片背景 |
| **Flow-Only BG** | #EFEFEF | 239, 239, 239 | 系統欄位背景 |
| **Border Light** | #E1E1E1 | 225, 225, 225 | 卡片邊框、分隔線 |

### 1.2 App.OnStart 色彩變數

```
// ═══════════════════════════════════════════════════════════
// Brand Color Palette - Governance System v1.0
// ═══════════════════════════════════════════════════════════

// Brand Primary（品牌主色）
Set(varBrandPrimary, ColorValue("#0C3467"));
Set(varBrandPrimaryHover, ColorValue("#0A2D5A"));
Set(varBrandPrimaryPressed, ColorValue("#082548"));

// Brand Accent（互動強調色）
Set(varBrandAccent, ColorValue("#008EC3"));
Set(varBrandAccentLight, ColorValue("#E6F4FA"));

// Neutral（中性色系）
Set(varNeutralGray, ColorValue("#999999"));
Set(varNeutralLight, ColorValue("#E1E1E1"));
Set(varNeutralLighter, ColorValue("#F5F5F5"));

// Text（文字色系）
Set(varTextBase, ColorValue("#2D2D2D"));
Set(varTextSecondary, ColorValue("#666666"));
Set(varTextDisabled, ColorValue("#999999"));
Set(varTextOnPrimary, ColorValue("#FFFFFF"));

// Semantic（語義色系）
Set(varDanger, ColorValue("#A4262C"));
Set(varDangerLight, ColorValue("#FDE7E9"));
Set(varSuccess, ColorValue("#107C10"));
Set(varSuccessLight, ColorValue("#DFF6DD"));
Set(varWarning, ColorValue("#FFB900"));
Set(varWarningLight, ColorValue("#FFF4CE"));

// Surface（表面色系）
Set(varBackground, ColorValue("#F5F5F5"));
Set(varCardWhite, ColorValue("#FFFFFF"));
Set(varFlowOnlyBg, ColorValue("#EFEFEF"));
Set(varBorderLight, ColorValue("#E1E1E1"));
```

### 1.3 色彩使用規則

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  色彩使用規則                                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ✓ 允許：                                                                    │
│    • Header 背景使用 varBrandPrimary                                         │
│    • Primary Button 使用 varBrandPrimary                                     │
│    • Focus 狀態使用 varBrandAccent                                           │
│    • 成功訊息使用 varSuccess                                                 │
│    • 錯誤訊息使用 varDanger                                                  │
│                                                                             │
│  ✗ 禁止：                                                                    │
│    • 硬編碼色碼（必須使用變數）                                              │
│    • 使用純黑 #000000（使用 varTextBase）                                    │
│    • 自定義新色彩                                                            │
│    • 在非危險情境使用 varDanger                                              │
│    • 在 Header 以外區域大面積使用 varBrandPrimary                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 第二章：Layout 結構規範

### 2.1 標準畫面骨架

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ① HEADER                                                    Height: 80px  │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │ ████████████████████████████████████████████████████████████████████████││
│  │ █  [Logo]  表單名稱                    [Status Badge]    使用者名稱  █  ││
│  │ ████████████████████████████████████████████████████████████████████████││
│  └─────────────────────────────────────────────────────────────────────────┘│
│  Fill: varBrandPrimary | Text: varTextOnPrimary                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  ② GATE STEPPER                                              Height: 50px  │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │                                                                         ││
│  │   ●━━━━━●━━━━━◉━━━━━○━━━━━○━━━━━○                                       ││
│  │ Pending Gate0  Gate1  Gate2  Gate3  Closed                              ││
│  │                                                                         ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│  Fill: varNeutralLighter                                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│  ③ MAIN BODY                                            Height: 動態填充   │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  ┌───────────────────────────────────────────────────────────────────┐  ││
│  │  │  Section 1: Basic Information                                     │  ││
│  │  │  RequestID, Title, Status                                         │  ││
│  │  └───────────────────────────────────────────────────────────────────┘  ││
│  │                                                                         ││
│  │  ┌───────────────────────────────────────────────────────────────────┐  ││
│  │  │  Section 2: Responsibility                                        │  ││
│  │  │  System Architect, Project Manager                                │  ││
│  │  └───────────────────────────────────────────────────────────────────┘  ││
│  │                                                                         ││
│  │  ┌───────────────────────────────────────────────────────────────────┐  ││
│  │  │  Section 3: Details                                               │  ││
│  │  │  可編輯欄位、系統欄位                                              │  ││
│  │  └───────────────────────────────────────────────────────────────────┘  ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│  Fill: varBackground                                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│  ④ FOOTER                                                    Height: 72px  │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │                                                                         ││
│  │  [Cancel]                                              [Primary Submit] ││
│  │     左側                                                        右側    ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│  Fill: varCardWhite | Border-top: varBorderLight                            │
├─────────────────────────────────────────────────────────────────────────────┤
│  ⑤ MESSAGE AREA（固定位置，覆蓋於頂部）                     Height: 0-60px  │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  [✓ Success] 或 [✗ Error] 訊息                                    [X]  ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│  位置：Y = 80（Header 下方） | 寬度：Parent.Width                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 區塊高度與座標

| 區塊 | 高度 | Y 座標 | 說明 |
|:------|:------|:--------|:------|
| Header | 80px | 0 | 固定不變 |
| Gate Stepper | 50px | 80 | 可隱藏（Visible: false） |
| Main Body | 動態 | `If(rectGateStepper.Visible, 130, 80)` | 填充剩餘空間 |
| Footer | 72px | `Parent.Height - 72` | 固定於底部 |
| Message Area | 60px | 80 | 覆蓋於 Gate Stepper / Body 上方 |

### 2.3 Section 卡片規格

| 屬性 | 值 |
|:------|:-----|
| Fill | varCardWhite |
| BorderColor | varBorderLight |
| BorderThickness | 1 |
| BorderRadius | 8 |
| Margin（距離邊界） | 20px |
| Padding（內部間距） | 16px |
| Section 間距 | 16px |

---

## 第三章：控制項命名標準

### 3.1 命名前綴規範

| 控制項類型 | 前綴 | 範例 |
|:-----------|:------|:------|
| Label | lbl | lblTitle, lblSection1 |
| Text input | txt | txtTitle, txtDescription |
| Dropdown | dd | ddProjectType, ddTargetSL |
| ComboBox | cmb | cmbProjectManager |
| Button | btn | btnSubmit, btnCancel |
| Rectangle | rect | rectHeader, rectSection1 |
| Icon | ico | icoClose, icoSuccess |
| Gallery | gal | galProjects |
| Image | img | imgLogo |
| Screen | scr | scrCreateProject |

### 3.2 區塊專用命名

| 區塊 | 容器命名 | 內部控制項前綴 |
|:------|:---------|:---------------|
| Header | rectHeader | lblHeader*, btnHeader* |
| Gate Stepper | rectGateStepper | icoStep*, lblStep*, lineStep* |
| Section 1 | rectSection1 | lblS1*, txtS1*, ddS1* |
| Section 2 | rectSection2 | lblS2*, txtS2*, cmbS2* |
| Section 3 | rectSection3 | lblS3*, txtS3*, ddS3* |
| Footer | rectFooter | btnCancel, btnSubmit |
| Message | rectMessage | icoMessage, lblMessageTitle, lblMessageText |

### 3.3 命名範例

```
scrCreateProject
├── rectHeader
│   ├── imgLogo
│   ├── lblHeaderTitle           "建立新專案"
│   ├── badgeStatus              Status Badge
│   └── lblHeaderUserName        使用者名稱
├── rectGateStepper
│   ├── icoStep_Pending
│   ├── lblStep_Pending
│   ├── lineStep_0to1
│   └── ...
├── rectSection1
│   ├── lblS1_Title              "Basic Information"
│   ├── lblS1_RequestIDLabel
│   ├── lblS1_RequestIDValue     (Flow-only)
│   └── ...
├── rectSection2
│   ├── lblS2_Title              "Responsibility"
│   ├── lblS2_ArchitectLabel
│   ├── lblS2_ArchitectValue     (Flow-only)
│   └── ...
├── rectSection3
│   ├── lblS3_Title              "Details"
│   ├── lblS3_TitleLabel
│   ├── txtS3_Title
│   └── ...
├── rectFooter
│   ├── btnCancel
│   └── btnSubmit
└── rectMessage
    ├── icoMessage
    ├── lblMessageTitle
    ├── lblMessageText
    └── icoCloseMessage
```

---

## 第四章：Gate Stepper 設計規範

### 4.1 Stepper 視覺規格

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   ●━━━━━━●━━━━━━◉━━━━━━○━━━━━━○━━━━━━○                                       │
│   │      │      │      │      │      │                                      │
│ Pending Gate0  Gate1  Gate2  Gate3  Closed                                  │
│   完成   完成   當前    未達    未達    未達                                   │
│                                                                             │
│  圖例：                                                                      │
│  ● 已完成：Fill = varBrandPrimary, Opacity = 0.6                            │
│  ◉ 目前：Fill = varBrandPrimary, 放大 1.2x, 白色內圈                        │
│  ○ 未達：Fill = varNeutralGray, Opacity = 0.4                               │
│  ━ 已完成連線：Stroke = varBrandPrimary                                     │
│  ─ 未達連線：Stroke = varNeutralGray                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Stepper 控制項規格

**步驟圓點（Icon.Circle）**：

| 屬性 | 已完成 | 目前 | 未達 |
|:------|:--------|:------|:------|
| Width/Height | 20 | 24 | 20 |
| Fill | varBrandPrimary | varBrandPrimary | varNeutralGray |
| Opacity | 0.6 | 1 | 0.4 |
| 內圈 | 無 | 白色圓心 | 無 |

**步驟標籤（Label）**：

| 屬性 | 已完成 | 目前 | 未達 |
|:------|:--------|:------|:------|
| Color | varBrandPrimary | varBrandPrimary | varNeutralGray |
| Font | Segoe UI | Segoe UI Semibold | Segoe UI |
| Size | 11 | 12 | 11 |

**連接線（Rectangle）**：

| 屬性 | 已完成區段 | 未達區段 |
|:------|:-----------|:---------|
| Width | 40 | 40 |
| Height | 2 | 2 |
| Fill | varBrandPrimary | varNeutralGray |
| Opacity | 0.6 | 0.3 |

### 4.3 Stepper Fill 公式

```
// icoStep_Gate0.Fill
If(
    varCurrentGateIndex > 0,
    varBrandPrimary,
    If(
        varCurrentGateIndex = 0,
        varBrandPrimary,
        varNeutralGray
    )
)

// Gate Index 對照：
// Pending = 0, Gate0 = 1, Gate1 = 2, Gate2 = 3, Gate3 = 4, Closed = 5
```

---

## 第五章：Status Badge 樣式規範

### 5.1 Badge 類型

| Badge 類型 | 用途 | Fill | Color | 範例值 |
|:-----------|:------|:------|:-------|:--------|
| Primary | 目前狀態 | varBrandPrimary | White | Active, Gate1 |
| Success | 完成狀態 | varSuccess | White | Closed, Approved |
| Danger | 終止/失敗 | varDanger | White | Terminated, Rejected |
| Warning | 待處理 | varWarning | varTextBase | Pending, UnderReview |
| Neutral | 一般資訊 | varNeutralLight | varTextBase | None, Draft |

### 5.2 Badge 控制項規格

```
Badge 共用屬性：
├── Height: 24
├── MinWidth: 60
├── PaddingLeft: 12
├── PaddingRight: 12
├── BorderRadius: 12（膠囊形）
├── Font: Segoe UI Semibold
├── Size: 11
└── DisplayMode: DisplayMode.View
```

### 5.3 Badge Fill 公式

```
// badgeStatus.Fill
Switch(
    varSelectedProject.gov_projectstatus,
    "Active", varBrandPrimary,
    "OnHold", varWarning,
    "Closed", varSuccess,
    "Terminated", varDanger,
    varNeutralLight
)

// badgeStatus.Color
Switch(
    varSelectedProject.gov_projectstatus,
    "Active", varTextOnPrimary,
    "OnHold", varTextBase,
    "Closed", varTextOnPrimary,
    "Terminated", varTextOnPrimary,
    varTextBase
)
```

---

## 第六章：Flow-Only 欄位視覺規範

### 6.1 視覺識別規格

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Flow-Only 欄位視覺規格                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │  Request ID (System-controlled)                                        │ │
│  │  ┌──────────────────────────────────────────────────────────────────┐  │ │
│  │  │ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │  │ │
│  │  │ ░░  DR-2026-00001234                                          ░░ │  │ │
│  │  │ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │  │ │
│  │  └──────────────────────────────────────────────────────────────────┘  │ │
│  │        ↑ 灰色背景 varFlowOnlyBg                                        │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│  必須滿足：                                                                  │
│  1. 使用 Label 控制項（非 Text input）                                       │
│  2. 背景色：varFlowOnlyBg (#EFEFEF)                                         │
│  3. 邊框色：varBorderLight (#E1E1E1)                                        │
│  4. 標籤後綴：" (System-controlled)"                                        │
│  5. 文字色：varTextSecondary (#666666)                                      │
│  6. DisplayMode：DisplayMode.View（永久唯讀）                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Flow-Only 欄位清單

| 欄位 | Schema Name | 標籤顯示 |
|:------|:-------------|:---------|
| Request ID | gov_requestid | Request ID (System-controlled) |
| Current Gate | gov_currentgate | Current Gate (System-controlled) |
| Request Status | gov_requeststatus | Request Status (System-controlled) |
| Project Status | gov_projectstatus | Project Status (System-controlled) |
| Freeze Status | gov_documentfreezestatus | Freeze Status (System-controlled) |
| Created On | createdon | Created On (System-controlled) |
| Created By | createdby | Created By (System-controlled) |
| Owner | ownerid | Owner (System-controlled) |

### 6.3 Flow-Only Label 設定

```
lblS1_RequestIDValue:
├── Text: varSelectedProject.gov_requestid
├── Fill: varFlowOnlyBg
├── BorderColor: varBorderLight
├── BorderThickness: 1
├── BorderRadius: 4
├── Color: varTextSecondary
├── Height: 36
├── PaddingLeft: 12
└── DisplayMode: DisplayMode.View
```

---

## 第七章：Button 樣式規範

### 7.1 Button 類型

| 類型 | 用途 | Fill | Color | Border |
|:------|:------|:------|:-------|:--------|
| Primary | 主要操作（Submit） | varBrandPrimary | White | 無 |
| Secondary | 次要操作（Save Draft） | White | varBrandPrimary | varBrandPrimary |
| Danger | 危險操作（Terminate） | varDanger | White | 無 |
| Ghost | 輔助操作（Cancel） | Transparent | varTextSecondary | 無 |
| Disabled | 停用狀態 | varNeutralLight | varTextDisabled | varBorderLight |

### 7.2 Button 控制項規格

**Primary Button**：

```
btnSubmit:
├── Text: "提交"
├── Fill: If(Self.DisplayMode = DisplayMode.Edit, varBrandPrimary, varNeutralLight)
├── Color: If(Self.DisplayMode = DisplayMode.Edit, varTextOnPrimary, varTextDisabled)
├── HoverFill: varBrandPrimaryHover
├── PressedFill: varBrandPrimaryPressed
├── BorderRadius: 4
├── Height: 40
├── MinWidth: 120
├── PaddingLeft: 24
├── PaddingRight: 24
├── Font: Font.'Segoe UI Semibold'
└── Size: 14
```

**Ghost Button**：

```
btnCancel:
├── Text: "取消"
├── Fill: Transparent
├── Color: varTextSecondary
├── HoverFill: varNeutralLighter
├── BorderThickness: 0
├── BorderRadius: 4
├── Height: 40
├── MinWidth: 80
└── Font: Font.'Segoe UI'
```

### 7.3 Footer Button 排列

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   [Cancel]                                                      [Submit]    │
│      ↑                                                             ↑        │
│   左側對齊                                                      右側對齊    │
│   X: 20                                            X: Parent.Width - 140    │
│                                                                             │
│   規則：                                                                     │
│   • Ghost Button 固定於左側                                                 │
│   • Primary Button 固定於右側                                               │
│   • 禁止順序混亂                                                            │
│   • 禁止水平置中排列                                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 第八章：字體與間距規範

### 8.1 字體規格

| 用途 | 字體 | 大小 | 色彩 |
|:------|:------|:------|:------|
| Header 標題 | Segoe UI Semibold | 20 | varTextOnPrimary |
| Section 標題 | Segoe UI Semibold | 16 | varTextBase |
| 欄位標籤 | Segoe UI | 13 | varTextBase |
| 欄位內容 | Segoe UI | 14 | varTextBase |
| 輔助說明 | Segoe UI | 12 | varTextSecondary |
| 錯誤提示 | Segoe UI | 12 | varDanger |
| Badge 文字 | Segoe UI Semibold | 11 | 依類型 |

### 8.2 間距規格

| 間距類型 | 值 | 用途 |
|:---------|:-----|:------|
| xxs | 4px | 極小間距（圖示與文字） |
| xs | 8px | 欄位標籤與輸入框間距 |
| sm | 12px | 同組控制項間距 |
| md | 16px | Section 內部 Padding、Section 間距 |
| lg | 20px | 區塊邊界間距 |
| xl | 24px | 大區塊間距 |

### 8.3 間距應用

```
┌────────────────────────────────────────┐
│ ← 20px (lg)                    20px → │
│ ┌────────────────────────────────────┐ │
│ │ ← 16px (md)              16px → │ │ │
│ │                                    │ │
│ │  欄位標籤                          │ │
│ │     ↓ 8px (xs)                     │ │
│ │  ┌────────────────────────────────┐│ │
│ │  │  輸入框                        ││ │
│ │  └────────────────────────────────┘│ │
│ │     ↓ 16px (md)                    │ │
│ │  欄位標籤                          │ │
│ │     ↓ 8px (xs)                     │ │
│ │  ┌────────────────────────────────┐│ │
│ │  │  輸入框                        ││ │
│ │  └────────────────────────────────┘│ │
│ │                                    │ │
│ └────────────────────────────────────┘ │
│     ↓ 16px (md)                        │
│ ┌────────────────────────────────────┐ │
│ │  下一個 Section                    │ │
│ └────────────────────────────────────┘ │
└────────────────────────────────────────┘
```

---

## 第九章：Message Area 規範

### 9.1 訊息區塊位置

**固定位置規則**：
- Y 座標：80（Header 正下方）
- 寬度：Parent.Width
- 高度：60px
- 覆蓋於 Gate Stepper 上方
- 不使用浮動 Toast

### 9.2 Success Message

```
rectMessageSuccess:
├── Fill: varSuccessLight
├── Y: 80
├── Height: 60
├── Visible: varShowSuccess

icoMessageSuccess:
├── Icon: Icon.CheckMark
├── Color: varSuccess
├── X: 20
├── Y: rectMessageSuccess.Y + 18

lblMessageSuccessTitle:
├── Text: "操作成功"
├── Color: varSuccess
├── Font: Font.'Segoe UI Semibold'
├── Size: 14
├── X: icoMessageSuccess.X + 32

lblMessageSuccessText:
├── Text: varSuccessMessage
├── Color: varTextBase
├── Size: 13
├── X: lblMessageSuccessTitle.X

icoCloseSuccess:
├── Icon: Icon.Cancel
├── Color: varTextSecondary
├── X: Parent.Width - 40
├── OnSelect: Set(varShowSuccess, false)
```

### 9.3 Error Message

```
rectMessageError:
├── Fill: varDangerLight
├── Y: 80
├── Height: 60
├── Visible: varShowError

icoMessageError:
├── Icon: Icon.Warning
├── Color: varDanger

lblMessageErrorTitle:
├── Text: "操作失敗"
├── Color: varDanger
├── Font: Font.'Segoe UI Semibold'

lblMessageErrorText:
├── Text: varErrorMessage
├── Color: varTextBase

icoCloseError:
├── Icon: Icon.Cancel
├── OnSelect: Set(varShowError, false)
```

---

## 第十章：禁止事項清單

### 10.1 色彩禁止事項

| 禁止項目 | 原因 |
|:---------|:------|
| 硬編碼色碼（如 ColorValue("#0C3467")） | 必須使用變數 |
| 使用純黑 #000000 | 使用 varTextBase |
| 自定義新色彩變數 | 破壞品牌一致性 |
| 在 Body 區大面積使用品牌色 | Header 專用 |
| 隨意使用 Danger 色 | 僅限危險操作 |

### 10.2 結構禁止事項

| 禁止項目 | 原因 |
|:---------|:------|
| 跳過五區塊配置 | 破壞一致性 |
| Body 區不分三個 Section | 破壞資訊分類 |
| Footer Button 順序混亂 | Cancel 左、Submit 右 |
| 使用浮動 Toast | Message 固定於頂部 |
| 訊息區塊位置隨機 | 必須在 Y=80 |

### 10.3 控制項禁止事項

| 禁止項目 | 原因 |
|:---------|:------|
| 保留預設命名（TextInput1） | 必須重命名 |
| Flow-Only 欄位使用 Text input | 必須使用 Label |
| Flow-Only 欄位無 "(System-controlled)" 標註 | 使用者需識別 |
| DisplayMode 回傳字串 | 必須回傳列舉值 |

### 10.4 品牌禁止事項

| 禁止項目 | 原因 |
|:---------|:------|
| 更改品牌主色 | #0C3467 為品牌象徵 |
| 在 Header 使用非品牌色 | 品牌識別區域 |
| 修改 Button 語義色彩對應 | 破壞認知一致性 |
| 在非 Focus 情境使用 Accent 色 | 強調色專用 |

---

## 第十一章：UX 驗證 Checklist

### 11.1 結構驗證

- [ ] Header 高度為 80px
- [ ] Header 背景色為 varBrandPrimary
- [ ] Gate Stepper 高度為 50px（若顯示）
- [ ] Body 區包含三個 Section
- [ ] Footer 高度為 72px
- [ ] Cancel 按鈕在左側
- [ ] Submit 按鈕在右側
- [ ] Message Area 在 Y=80 位置

### 11.2 色彩驗證

- [ ] 所有色彩使用變數（無硬編碼）
- [ ] Header 使用 varBrandPrimary
- [ ] Section 背景使用 varCardWhite
- [ ] Flow-Only 欄位使用 varFlowOnlyBg
- [ ] 主按鈕使用 varBrandPrimary
- [ ] 成功訊息使用 varSuccess
- [ ] 錯誤訊息使用 varDanger

### 11.3 控制項驗證

- [ ] 所有控制項已重命名（無預設名稱）
- [ ] 命名前綴符合規範
- [ ] Flow-Only 欄位使用 Label
- [ ] Flow-Only 欄位有 "(System-controlled)" 標註
- [ ] DisplayMode 公式正確

### 11.4 品牌驗證

- [ ] Logo 顯示於 Header 左側
- [ ] 表單標題顯示於 Header
- [ ] Status Badge 樣式正確
- [ ] 字體使用 Segoe UI 系列

---

## 附錄 A：App.OnStart 完整模板

```
// ═══════════════════════════════════════════════════════════
// App.OnStart - Governance Canvas App Brand Template v1.0
// 依據：Canvas-Brand-UI-Standard-v1.md
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

// ─────────────────────────────────────────────────────────────
// Section 4: Brand Color Palette
// ─────────────────────────────────────────────────────────────
Set(varBrandPrimary, ColorValue("#0C3467"));
Set(varBrandPrimaryHover, ColorValue("#0A2D5A"));
Set(varBrandPrimaryPressed, ColorValue("#082548"));
Set(varBrandAccent, ColorValue("#008EC3"));
Set(varBrandAccentLight, ColorValue("#E6F4FA"));
Set(varNeutralGray, ColorValue("#999999"));
Set(varNeutralLight, ColorValue("#E1E1E1"));
Set(varNeutralLighter, ColorValue("#F5F5F5"));
Set(varTextBase, ColorValue("#2D2D2D"));
Set(varTextSecondary, ColorValue("#666666"));
Set(varTextDisabled, ColorValue("#999999"));
Set(varTextOnPrimary, ColorValue("#FFFFFF"));
Set(varDanger, ColorValue("#A4262C"));
Set(varDangerLight, ColorValue("#FDE7E9"));
Set(varSuccess, ColorValue("#107C10"));
Set(varSuccessLight, ColorValue("#DFF6DD"));
Set(varWarning, ColorValue("#FFB900"));
Set(varWarningLight, ColorValue("#FFF4CE"));
Set(varBackground, ColorValue("#F5F5F5"));
Set(varCardWhite, ColorValue("#FFFFFF"));
Set(varFlowOnlyBg, ColorValue("#EFEFEF"));
Set(varBorderLight, ColorValue("#E1E1E1"));

// ─────────────────────────────────────────────────────────────
// Section 5: 區塊高度常數
// ─────────────────────────────────────────────────────────────
Set(varHeaderHeight, 80);
Set(varGateStepperHeight, 50);
Set(varFooterHeight, 72);
Set(varMessageHeight, 60);

// ─────────────────────────────────────────────────────────────
// Section 6: 間距常數
// ─────────────────────────────────────────────────────────────
Set(varSpacingXXS, 4);
Set(varSpacingXS, 8);
Set(varSpacingSM, 12);
Set(varSpacingMD, 16);
Set(varSpacingLG, 20);
Set(varSpacingXL, 24);

// ─────────────────────────────────────────────────────────────
// Section 7: Flow 回傳結果
// ─────────────────────────────────────────────────────────────
Set(varResult, {Status: "", Message: "", RequestID: "", ErrorCode: ""})
```

---

## 版本歷史

| 版本 | 日期 | 變更說明 |
|:------|:------|:----------|
| v1.0 | 2026-02-11 | 初版建立 - 品牌 UI 設計標準 |

---

**文件結束**

**本標準為治理系統 Canvas App UI 設計之唯一品牌規範。**
**所有新建或修改之表單必須遵循本標準。**
