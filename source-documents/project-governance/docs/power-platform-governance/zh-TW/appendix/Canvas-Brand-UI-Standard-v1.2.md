# Canvas 品牌 UI 標準 v1.2

**文件版本**：v1.2
**生效日期**：2026-02-11
**文件擁有者**：系統設計治理部門
**核准單位**：工程管理層
**文件性質**：反脆弱 Canvas 治理標準
**文件權威**：**唯一官方 UI 設計與模板架構標準**
**版本類型**：強化升級 – 3 年穩定架構

---

```
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║           設計部門治理系統 v1.2                                               ║
║                                                                             ║
║           反脆弱 CANVAS 治理版本                                              ║
║                                                                             ║
║           版本類型：強化升級                                                  ║
║           狀態：穩定架構                                                      ║
║           穩定期限：3 年 (2026-2029)                                         ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
```

---

## 權威聲明

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ⚠️ 權威聲明                                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  本文件為以下項目之【唯一權威】：                                             │
│  • Canvas App 色彩定義                                                       │
│  • 畫面模板架構                                                              │
│  • 組件庫規格                                                                │
│  • 佈局強制規則                                                              │
│  • 人為錯誤防護機制                                                          │
│                                                                             │
│  所有其他 UI 相關文件均【從屬】於本標準。                                      │
│                                                                             │
│  已取代：                                                                    │
│  ✗ Canvas-Brand-UI-Standard-v1.0.md                                         │
│  ✗ Canvas-Brand-UI-Standard-v1.1.md                                         │
│  ✗ Canvas-UI-Governance-Standard-v1.md                                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

# 第一部分：基礎治理

## 第一章：統一色彩系統

### 1.1 色彩權威宣告

**本章節為色彩定義之【唯一來源】。任何其他文件、檔案或程式碼區塊【禁止】定義色彩。**

### 1.2 官方色彩調色盤

| 變數名稱 | 色碼 | RGB | 語義用途 |
|:---------|:------|:-----|:---------|
| varBrandPrimary | #0C3467 | 12, 52, 103 | Header、主按鈕、目前 Gate |
| varBrandPrimaryHover | #0A2D5A | 10, 45, 90 | 主按鈕懸停 |
| varBrandPrimaryPressed | #082548 | 8, 37, 72 | 主按鈕按下 |
| varBrandAccent | #008EC3 | 0, 142, 195 | 焦點邊框、超連結 |
| varNeutralDark | #605E5C | 96, 94, 92 | 次要文字、標籤 |
| varNeutralGray | #999999 | 153, 153, 153 | 停用、未達 Gate |
| varNeutralLight | #E1E1E1 | 225, 225, 225 | 邊框、分隔線 |
| varNeutralLighter | #F5F5F5 | 245, 245, 245 | 頁面背景 |
| varTextBase | #2D2D2D | 45, 45, 45 | 主要文字 |
| varTextSecondary | #666666 | 102, 102, 102 | 次要文字 |
| varTextDisabled | #999999 | 153, 153, 153 | 停用文字 |
| varTextOnPrimary | #FFFFFF | 255, 255, 255 | 品牌色上文字 |
| varDanger | #A4262C | 164, 38, 44 | 錯誤、刪除、已終止 |
| varDangerLight | #FDE7E9 | 253, 231, 233 | 錯誤訊息背景 |
| varSuccess | #107C10 | 16, 124, 16 | 成功、已關閉、已完成 |
| varSuccessLight | #DFF6DD | 223, 246, 221 | 成功訊息背景 |
| varWarning | #FFB900 | 255, 185, 0 | 警告、待處理 |
| varWarningLight | #FFF4CE | 255, 244, 206 | 警告訊息背景 |
| varCardWhite | #FFFFFF | 255, 255, 255 | Section 卡片背景 |
| varFlowOnlyBg | #EFEFEF | 239, 239, 239 | 系統欄位背景 |
| varBorderLight | #E1E1E1 | 225, 225, 225 | 卡片邊框 |

### 1.3 色彩強制規則

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  色彩強制規則                                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  規則 C-001：所有色彩值【必須】透過變數引用。                                  │
│              行內 ColorValue("#XXXXXX")【禁止】使用。                        │
│                                                                             │
│  規則 C-002：所有色彩變數【必須】定義於 App.OnStart。                         │
│              畫面層級的色彩定義【禁止】使用。                                  │
│                                                                             │
│  規則 C-003：色彩變數名稱【必須】完全符合本規格。                              │
│              自訂色彩變數名稱【禁止】使用。                                    │
│                                                                             │
│  規則 C-004：色彩使用【必須】遵循語義對應。                                    │
│              在非錯誤情境使用 varDanger【禁止】。                              │
│                                                                             │
│  規則 C-005：varBrandPrimary【僅限】用於：                                    │
│              • Header 背景                                                   │
│              • 主按鈕填充                                                    │
│              • 目前 Gate 指示器                                               │
│              其他用途【禁止】。                                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.4 App.OnStart 色彩模板

```
// ═══════════════════════════════════════════════════════════════════════════
// CANVAS 品牌 UI 標準 v1.2 - 官方色彩調色盤
// 這是色彩定義的【唯一來源】。
// 禁止在其他地方定義色彩。
// ═══════════════════════════════════════════════════════════════════════════

// ─── 品牌色彩 ──────────────────────────────────────────────────────────────
Set(varBrandPrimary, ColorValue("#0C3467"));
Set(varBrandPrimaryHover, ColorValue("#0A2D5A"));
Set(varBrandPrimaryPressed, ColorValue("#082548"));
Set(varBrandAccent, ColorValue("#008EC3"));

// ─── 中性色彩 ──────────────────────────────────────────────────────────────
Set(varNeutralDark, ColorValue("#605E5C"));
Set(varNeutralGray, ColorValue("#999999"));
Set(varNeutralLight, ColorValue("#E1E1E1"));
Set(varNeutralLighter, ColorValue("#F5F5F5"));

// ─── 文字色彩 ──────────────────────────────────────────────────────────────
Set(varTextBase, ColorValue("#2D2D2D"));
Set(varTextSecondary, ColorValue("#666666"));
Set(varTextDisabled, ColorValue("#999999"));
Set(varTextOnPrimary, ColorValue("#FFFFFF"));

// ─── 語義色彩 ──────────────────────────────────────────────────────────────
Set(varDanger, ColorValue("#A4262C"));
Set(varDangerLight, ColorValue("#FDE7E9"));
Set(varSuccess, ColorValue("#107C10"));
Set(varSuccessLight, ColorValue("#DFF6DD"));
Set(varWarning, ColorValue("#FFB900"));
Set(varWarningLight, ColorValue("#FFF4CE"));

// ─── 表面色彩 ──────────────────────────────────────────────────────────────
Set(varCardWhite, ColorValue("#FFFFFF"));
Set(varFlowOnlyBg, ColorValue("#EFEFEF"));
Set(varBorderLight, ColorValue("#E1E1E1"));
```

---

## 第二章：佈局結構規格

### 2.1 五區塊架構（不可變更）

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  區塊 1：HEADER                                            高度：80px       │
│  Y: 0 | Fill: varBrandPrimary                                               │
├─────────────────────────────────────────────────────────────────────────────┤
│  區塊 2：GATE STEPPER                                      高度：50px       │
│  Y: 80 | Fill: varNeutralLighter                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│  區塊 3：BODY                                              高度：動態       │
│  Y: 130（若 Stepper 隱藏則 80）| Fill: varNeutralLighter                    │
│  ┌─Section 1：基本資訊─────────────────────────────────────────────────┐    │
│  │  Fill: varCardWhite | BorderRadius: 8                               │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│  ┌─Section 2：責任歸屬─────────────────────────────────────────────────┐    │
│  │  Fill: varCardWhite | BorderRadius: 8                               │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│  ┌─Section 3：詳細資料─────────────────────────────────────────────────┐    │
│  │  Fill: varCardWhite | BorderRadius: 8                               │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
├─────────────────────────────────────────────────────────────────────────────┤
│  區塊 4：FOOTER                                            高度：72px       │
│  Y: Parent.Height - 72 | Fill: varCardWhite                                 │
│  [Ghost: 取消] ←─────────────────────────────────→ [Primary: 提交]          │
├─────────────────────────────────────────────────────────────────────────────┤
│  區塊 5：MESSAGE（覆蓋層）                                  高度：60px       │
│  Y: 80 | Visible: varShowSuccess OR varShowError                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 區塊高度常數

| 區塊 | 高度 | Y 座標 | 可修改 |
|------|------|--------|:------:|
| Header | 80px | 0 | ❌ 禁止 |
| Gate Stepper | 50px | 80 | ❌ 禁止 |
| Body | 動態 | `varBodyY` | ✓（透過變數） |
| Footer | 72px | `Parent.Height - 72` | ❌ 禁止 |
| Message | 60px | 80 | ❌ 禁止 |

### 2.3 Section 卡片控制項規格

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ⚠️ 重要：控制項類型與 BorderRadius 支援                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Classic Rectangle 【不支援】BorderRadius。                                  │
│  若需圓角卡片效果，【必須】使用以下替代方案。                                │
│                                                                             │
│  方案優先順序：                                                              │
│  1. Modern Container（推薦，支援 BorderRadius）                              │
│  2. Button (DisplayMode: View)（備選，支援 BorderRadius）                   │
│  3. Classic Rectangle（降級，直角設計）                                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**控制項能力對照表**：

| 控制項類型 | 支援 Fill | 支援 BorderRadius | 支援子控制項 | 建議用途 |
|-----------|:---------:|:----------------:|:------------:|---------|
| Rectangle (Classic) | ✓ | ❌ | ❌ | 背景、分隔線 |
| Container (Modern) | ✓ | ✓ | ✓ | **Section 卡片（推薦）** |
| Button (DisplayMode: View) | ✓ | ✓ | ❌ | Section 卡片（備選） |

**Modern Container Section 規格**：

```
控制項類型：Modern Container
命名前綴：cnt（如 cntSection1、cntSection2）

屬性設定：
├── X: varSectionMargin
├── Y: [動態計算，參考上一個區塊]
├── Width: Parent.Width - varSectionMargin * 2
├── Height: [依內容調整]
├── Fill: varCardWhite
├── BorderColor: varBorderLight
├── BorderThickness: 1
├── BorderRadius: 8
└── LayoutMode: "Manual"（手動佈局子控制項）

驗證點：
☐ 容器顯示圓角
☐ 子控制項可在容器內正確定位
☐ 邊框平滑無銳角
```

**降級方案（Classic Rectangle）**：

```
當環境不支援 Modern Container 時：

控制項類型：Classic Rectangle
命名前綴：rect（如 rectSection1）

屬性設定：
├── X: varSectionMargin
├── Y: [動態計算]
├── Width: Parent.Width - varSectionMargin * 2
├── Height: [依內容調整]
├── Fill: varCardWhite
├── BorderColor: varBorderLight
├── BorderThickness: 1
└── [BorderRadius 不適用，保持直角]

視覺補償：
├── 增加 BorderThickness 至 2 可強化卡片感
└── 確保所有 Section 風格一致（皆為直角）
```

> **操作手冊參考**：詳細操作步驟與故障排除請參閱
> [appendix/Canvas-Editor-Operability-Playbook-v1.md](Canvas-Editor-Operability-Playbook-v1.md)

### 2.4 動態 Y 座標系統

**所有 Y 座標【必須】使用變數。直接數值【禁止】使用。**

```
// ─── 佈局常數（設定於 App.OnStart）─────────────────────────────────────────
Set(varHeaderHeight, 80);
Set(varStepperHeight, 50);
Set(varFooterHeight, 72);
Set(varMessageHeight, 60);
Set(varSectionSpacing, 16);
Set(varSectionMargin, 20);

// ─── 動態 Y 座標 ───────────────────────────────────────────────────────────
Set(varStepperY, varHeaderHeight);
Set(varBodyY, If(varShowGateStepper, varHeaderHeight + varStepperHeight, varHeaderHeight));
Set(varMessageY, varHeaderHeight);
```

---

# 第二部分：CANVAS 模板強制架構

## 第三章：畫面模板強制機制

### 3.1 模板強制宣告

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ⛔ 畫面模板強制機制                                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  規則 T-001：直接建立新畫面【禁止】。                                         │
│              所有畫面【必須】透過複製官方畫面模板                              │
│              (scrTemplate_Governance) 來建立。                               │
│                                                                             │
│  規則 T-002：以下組件複製後【不可變更】：                                     │
│              • rectHeader（Header 容器）                                     │
│              • rectGateStepper（Gate Stepper 容器）                          │
│              • rectFooter（Footer 容器）                                     │
│              • rectMessage（訊息覆蓋層容器）                                  │
│                                                                             │
│  規則 T-003：僅【允許】以下修改：                                             │
│              • 在 rectSection1、rectSection2、rectSection3 內新增控制項      │
│              • 修改 lblHeaderTitle.Text                                      │
│              • 修改 btnSubmit.Text                                           │
│              • 修改 btnSubmit.OnSelect 中的表單特定邏輯                       │
│                                                                             │
│  規則 T-004：畫面命名【必須】遵循模式：                                        │
│              scr[表單名稱]（例：scrCreateProject、scrGateRequest）            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 官方畫面模板結構

> **注意**：Section 容器建議使用 Modern Container（支援 BorderRadius）。
> 若環境不支援，可改用 Classic Rectangle（直角設計）。
> 詳見 2.3 節「Section 卡片控制項規格」。

```
scrTemplate_Governance
│
├── rectHeader ────────────────────────────────────────── [不可變更]
│   ├── imgLogo
│   ├── lblHeaderTitle
│   ├── badgeHeaderStatus
│   └── lblHeaderUserName
│
├── rectGateStepper ───────────────────────────────────── [不可變更]
│   ├── galGateStepper（Gallery 形式，資料驅動）
│   └── 從 colGateSteps 集合產生的控制項
│
├── rectBody ──────────────────────────────────────────── [容器不可變更]
│   ├── cntSection1 (或 rectSection1) ──────────────── [內部可修改]
│   │   ├── lblS1_Title: "基本資訊"
│   │   └── [此處新增表單特定控制項]
│   │
│   ├── cntSection2 (或 rectSection2) ──────────────── [內部可修改]
│   │   ├── lblS2_Title: "責任歸屬"
│   │   └── [此處新增表單特定控制項]
│   │
│   └── cntSection3 (或 rectSection3) ──────────────── [內部可修改]
│       ├── lblS3_Title: "詳細資料"
│       └── [此處新增表單特定控制項]
│
├── rectFooter ────────────────────────────────────────── [不可變更]
│   ├── btnCancel
│   └── btnSubmit
│
├── rectMessageSuccess ────────────────────────────────── [不可變更]
│   ├── icoMessageSuccess
│   ├── lblMessageSuccessTitle
│   ├── lblMessageSuccessText
│   └── icoCloseSuccess
│
├── rectMessageError ──────────────────────────────────── [不可變更]
│   ├── icoMessageError
│   ├── lblMessageErrorTitle
│   ├── lblMessageErrorText
│   └── icoCloseError
│
└── rectLoadingOverlay ────────────────────────────────── [不可變更]
    └── lblLoadingText
```

### 3.3 組件不可變性規則

| 組件 | 不可變更屬性 | 可修改屬性 |
|:------|:-------------|:-----------|
| rectHeader | X、Y、Width、Height、Fill | 無 |
| rectGateStepper | X、Y、Width、Height、Fill、結構 | Visible（透過 varShowGateStepper） |
| rectFooter | X、Y、Width、Height、Fill、按鈕位置 | btnSubmit.Text、btnSubmit.OnSelect |
| cntSection* / rectSection* | X、Y、Width、Height、Fill | 內部控制項（BorderRadius 依控制項類型） |
| rectMessage* | X、Y、Width、Height、Fill、結構 | Visible（透過 varShowSuccess/Error） |

> **控制項命名說明**：
> - `cntSection*`：使用 Modern Container 時（支援 BorderRadius）
> - `rectSection*`：使用 Classic Rectangle 時（直角設計）

---

## 第四章：組件庫架構

### 4.1 組件庫宣告

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  組件庫架構                                                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  以下組件【應】建立為可重用的 Canvas 組件：                                   │
│                                                                             │
│  1. cmpBrandColorProvider                                                   │
│     用途：集中式色彩分發                                                     │
│     使用：【必須】存在於 App 層級                                            │
│                                                                             │
│  2. cmpGovHeader                                                            │
│     用途：標準化 Header                                                      │
│     輸入：Title、ShowStatus、StatusValue、UserName                          │
│                                                                             │
│  3. cmpGateStepper                                                          │
│     用途：Gate 進度視覺化                                                    │
│     輸入：CurrentGateIndex、GateSteps（集合）                                │
│                                                                             │
│  4. cmpMessageBlock                                                         │
│     用途：成功/錯誤訊息顯示                                                  │
│     輸入：MessageType、Title、Message、ShowClose                            │
│                                                                             │
│  5. cmpGovFooter                                                            │
│     用途：標準化 Footer 含按鈕                                               │
│     輸入：CancelText、SubmitText、SubmitEnabled、OnSubmit                   │
│                                                                             │
│  6. cmpFlowOnlyField                                                        │
│     用途：系統控制欄位顯示                                                   │
│     輸入：Label、Value                                                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 BrandColorProvider 組件規格

```
組件：cmpBrandColorProvider
類型：非視覺（資料組件）
範圍：App 層級單例

用途：
- 集中分發品牌色彩
- 防止重複色彩定義
- 強制單一真實來源

輸出屬性：
├── BrandPrimary: Color
├── BrandPrimaryHover: Color
├── BrandPrimaryPressed: Color
├── BrandAccent: Color
├── NeutralDark: Color
├── NeutralGray: Color
├── NeutralLight: Color
├── NeutralLighter: Color
├── TextBase: Color
├── TextSecondary: Color
├── TextDisabled: Color
├── TextOnPrimary: Color
├── Danger: Color
├── DangerLight: Color
├── Success: Color
├── SuccessLight: Color
├── Warning: Color
├── WarningLight: Color
├── CardWhite: Color
├── FlowOnlyBg: Color
└── BorderLight: Color

使用模式：
// 取代：Fill: varBrandPrimary
// 使用：Fill: cmpBrandColorProvider.BrandPrimary
```

### 4.3 MessageBlock 組件規格

```
組件：cmpMessageBlock
類型：視覺組件

輸入屬性：
├── MessageType: Text（"Success" | "Error"）
├── Title: Text
├── Message: Text
├── ShowClose: Boolean
└── OnClose: Behavior

內部結構：
├── rectBackground
│   Fill: If(MessageType = "Success", SuccessLight, DangerLight)
├── icoMessage
│   Icon: If(MessageType = "Success", CheckMark, Warning)
│   Color: If(MessageType = "Success", Success, Danger)
├── lblTitle
│   Text: Title
│   Color: If(MessageType = "Success", Success, Danger)
├── lblMessage
│   Text: Message
└── icoClose
    Visible: ShowClose
    OnSelect: OnClose

尺寸：
├── Width: Parent.Width
├── Height: 60
└── Y: 80（固定於 Header 下方）
```

### 4.4 GateStepper 組件規格

```
組件：cmpGateStepper
類型：視覺組件

輸入屬性：
├── CurrentGateIndex: Number（0-5）
├── ShowStepper: Boolean
└── GateLabels: Table（選擇性覆寫）

預設 Gate 標籤：
ClearCollect(colDefaultGateLabels,
    {Index: 0, Label: "Pending"},
    {Index: 1, Label: "Gate0"},
    {Index: 2, Label: "Gate1"},
    {Index: 3, Label: "Gate2"},
    {Index: 4, Label: "Gate3"},
    {Index: 5, Label: "Closed"}
)

內部結構：
├── galSteps（水平 Gallery）
│   Items: If(IsEmpty(GateLabels), colDefaultGateLabels, GateLabels)
│   Template:
│   ├── cirStep
│   │   Fill: If(ThisItem.Index < CurrentGateIndex, varBrandPrimary,
│   │         If(ThisItem.Index = CurrentGateIndex, varBrandPrimary, varNeutralGray))
│   │   Opacity: If(ThisItem.Index < CurrentGateIndex, 0.5,
│   │            If(ThisItem.Index = CurrentGateIndex, 1, 0.4))
│   │   Width: If(ThisItem.Index = CurrentGateIndex, 20, 16)
│   │   Height: If(ThisItem.Index = CurrentGateIndex, 20, 16)
│   ├── lblStepLabel
│   │   Text: ThisItem.Label
│   │   Color: If(ThisItem.Index <= CurrentGateIndex, varBrandPrimary, varNeutralGray)
│   └── lineConnector
│       Visible: ThisItem.Index < CountRows(GateLabels) - 1
│       Fill: varNeutralLight

尺寸：
├── Width: Parent.Width
├── Height: 50
├── Y: 80
└── Visible: ShowStepper
```

---

## 第五章：佈局強制規則

### 5.1 位置強制機制

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ⛔ 位置強制規則                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  規則 P-001：直接 X/Y 數值【禁止】使用。                                      │
│              所有位置【必須】使用佈局變數或相對公式。                          │
│                                                                             │
│              ❌ 禁止：Y: 80                                                  │
│              ✅ 必須：Y: varHeaderHeight                                     │
│                                                                             │
│  規則 P-002：Width【必須】使用 Parent.Width 或相對計算。                      │
│                                                                             │
│              ❌ 禁止：Width: 1366                                            │
│              ✅ 必須：Width: Parent.Width                                    │
│              ✅ 必須：Width: Parent.Width - varSectionMargin * 2             │
│                                                                             │
│  規則 P-003：響應式佈局【必須】使用 Layout Container。                        │
│              表單控制項的絕對定位【禁止】。                                    │
│                                                                             │
│  規則 P-004：Section Y 座標【必須】動態計算。                                 │
│                                                                             │
│              ✅ 必須：rectSection2.Y =                                       │
│                      rectSection1.Y + rectSection1.Height +                  │
│                      varSectionSpacing                                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 DisplayMode 強制機制

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ⛔ DISPLAYMODE 強制規則                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  規則 D-001：DisplayMode 中使用行內 And()【禁止】。                           │
│              DisplayMode【必須】引用集中驗證變數。                            │
│                                                                             │
│              ❌ 禁止：                                                       │
│              DisplayMode: If(And(!IsBlank(txt1.Text), !IsBlank(txt2.Text),  │
│                            !IsBlank(dd3.Selected)), DisplayMode.Edit,       │
│                            DisplayMode.Disabled)                            │
│                                                                             │
│              ✅ 必須：                                                       │
│              DisplayMode: If(varFormValid, DisplayMode.Edit,                │
│                            DisplayMode.Disabled)                            │
│                                                                             │
│  規則 D-002：表單驗證【必須】集中於單一變數。                                  │
│                                                                             │
│              // 在 App.OnStart 或 Screen.OnVisible 中：                      │
│              Set(varFormValid,                                              │
│                  And(                                                       │
│                      !IsBlank(txtTitle.Text),                               │
│                      !IsBlank(ddType.Selected),                             │
│                      !IsBlank(cmbManager.Selected),                         │
│                      !varIsLoading                                          │
│                  )                                                          │
│              );                                                             │
│                                                                             │
│  規則 D-003：DisplayMode【必須】回傳列舉值，非字串。                          │
│                                                                             │
│              ❌ 禁止：If(condition, "Edit", "Disabled")                      │
│              ✅ 必須：If(condition, DisplayMode.Edit,                        │
│                                    DisplayMode.Disabled)                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

# 第三部分：人為錯誤防護機制

## 第六章：反人為錯誤設計

### 6.1 錯誤防護宣告

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  人為錯誤防護機制                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  本章節定義在 Canvas App 開發與維護期間                                       │
│  預防、偵測與控制人為錯誤的機制。                                             │
│                                                                             │
│  錯誤類別：                                                                  │
│  • E1：色彩定義錯誤（重複、行內、錯誤變數）                                   │
│  • E2：佈局錯誤（硬編碼位置、響應式失效）                                     │
│  • E3：邏輯錯誤（行內驗證、錯誤 DisplayMode）                                │
│  • E4：模板錯誤（修改不可變組件）                                            │
│  • E5：命名錯誤（預設名稱、錯誤前綴）                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 6.2 表單變數集中化

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  表單變數集中化規則                                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  規則 V-001：每個表單【必須】只有一個驗證變數。                               │
│              變數名稱：varFormValid                                          │
│                                                                             │
│  規則 V-002：所有表單狀態【必須】透過標準變數管理：                            │
│                                                                             │
│              varIsLoading      : Boolean - 載入狀態                         │
│              varFormValid      : Boolean - 表單驗證狀態                      │
│              varShowSuccess    : Boolean - 成功訊息可見性                    │
│              varShowError      : Boolean - 錯誤訊息可見性                    │
│              varSuccessMessage : Text    - 成功訊息內容                      │
│              varErrorMessage   : Text    - 錯誤訊息內容                      │
│              varErrorCode      : Text    - Flow 回傳的錯誤代碼               │
│                                                                             │
│  規則 V-003：表單特定變數【必須】使用前綴 varForm_                            │
│              範例：varForm_SelectedProject、varForm_ApprovalComment          │
│                                                                             │
│  規則 V-004：varFormValid【必須】在 Screen.OnVisible                         │
│              以及任何輸入控制項值變更後重新計算。                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 6.3 標準驗證模式

```
// ═══════════════════════════════════════════════════════════════════════════
// 標準表單驗證模式
// 此模式【必須】用於所有治理表單。
// ═══════════════════════════════════════════════════════════════════════════

// ─── 步驟 1：在 Screen.OnVisible 定義驗證 ──────────────────────────────────
UpdateContext({
    locFormValid: And(
        // 必填欄位檢查
        !IsBlank(txtTitle.Text),
        Len(txtTitle.Text) >= 3,
        !IsBlank(ddType.Selected),
        !IsBlank(cmbManager.Selected),

        // 載入狀態檢查
        !varIsLoading
    )
});
Set(varFormValid, locFormValid);

// ─── 步驟 2：在輸入變更時更新驗證 ───────────────────────────────────────────
// 新增到每個輸入控制項的 OnChange 屬性：
Set(varFormValid,
    And(
        !IsBlank(txtTitle.Text),
        Len(txtTitle.Text) >= 3,
        !IsBlank(ddType.Selected),
        !IsBlank(cmbManager.Selected),
        !varIsLoading
    )
);

// ─── 步驟 3：在 DisplayMode 中引用 ─────────────────────────────────────────
// btnSubmit.DisplayMode:
If(varFormValid, DisplayMode.Edit, DisplayMode.Disabled)
```

### 6.4 訊息區塊統一化

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  訊息區塊統一化規則                                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  規則 M-001：僅【允許】兩種訊息類型：成功與錯誤。                              │
│              訊息區塊中的警告訊息【禁止】。                                   │
│                                                                             │
│  規則 M-002：訊息區塊【必須】使用標準化結構：                                  │
│              • rectMessage[Type]（容器）                                    │
│              • icoMessage[Type]（圖示）                                     │
│              • lblMessage[Type]Title（標題標籤）                             │
│              • lblMessage[Type]Text（訊息標籤）                              │
│              • icoClose[Type]（關閉按鈕）                                   │
│                                                                             │
│  規則 M-003：訊息位置【固定】於 Y: varHeaderHeight（80）。                    │
│              浮動 Toast【禁止】。                                            │
│                                                                             │
│  規則 M-004：成功與錯誤訊息【互斥】。                                         │
│              同時只能顯示一個訊息區塊。                                       │
│                                                                             │
│  規則 M-005：訊息顯示邏輯：                                                   │
│              Set(varShowSuccess, true); Set(varShowError, false);           │
│              或                                                              │
│              Set(varShowError, true); Set(varShowSuccess, false);           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 6.5 Stepper 重複防護

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  STEPPER 重複防護                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  規則 S-001：每個畫面【必須】只有零個或一個 Gate Stepper。                    │
│              單一畫面上的多個 Stepper【禁止】。                               │
│                                                                             │
│  規則 S-002：Gate Stepper【必須】使用集合進行資料驅動。                       │
│              硬編碼的個別步驟控制項【禁止】。                                  │
│                                                                             │
│              ❌ 禁止：                                                       │
│              icoStep_Pending、icoStep_Gate0、icoStep_Gate1、...             │
│              （每個步驟的個別控制項）                                        │
│                                                                             │
│              ✅ 必須：                                                       │
│              galGateStepper with Items: colGateSteps                        │
│              （Gallery 形式，資料驅動）                                      │
│                                                                             │
│  規則 S-003：Gate 步驟資料【必須】定義於 App.OnStart：                        │
│                                                                             │
│              ClearCollect(colGateSteps,                                     │
│                  {Index: 0, Label: "Pending", Value: "Pending"},            │
│                  {Index: 1, Label: "Gate0", Value: "Gate0"},                │
│                  {Index: 2, Label: "Gate1", Value: "Gate1"},                │
│                  {Index: 3, Label: "Gate2", Value: "Gate2"},                │
│                  {Index: 4, Label: "Gate3", Value: "Gate3"},                │
│                  {Index: 5, Label: "Closed", Value: "Closed"}               │
│              );                                                             │
│                                                                             │
│  規則 S-004：目前 Gate【必須】透過 varCurrentGateIndex 指示。                 │
│              直接與 Gate 字串比對【禁止】。                                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

# 第四部分：3 年 UI 穩定性藍圖

## 第七章：未來防護架構

### 7.1 穩定期限宣告

```
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║  3 年 UI 穩定性藍圖（2026-2029）                                             ║
║                                                                             ║
║  本架構設計可容納以下變更                                                     ║
║  【無需】重構既有表單：                                                       ║
║                                                                             ║
║  ✓ 新增 Flow                                                                ║
║  ✓ 新增 Gate                                                                ║
║  ✓ 更改品牌色彩                                                              ║
║  ✓ 新增 KPI 覆蓋層                                                           ║
║  ✓ 新增表單類型                                                              ║
║  ✓ 修改驗證規則                                                              ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
```

### 7.2 新增 Flow（零 UI 影響）

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  情境：新增 Flow（例：GOV-020-NewFeature）                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  架構透過以下方式實現：                                                       │
│                                                                             │
│  1. HEADER 獨立性                                                            │
│     • Header 透過 lblHeaderTitle.Text 顯示表單標題                           │
│     • 標題為表單特定，非 Flow 特定                                            │
│     • Header 結構中無 Flow 引用                                              │
│                                                                             │
│  2. FOOTER 抽象化                                                            │
│     • btnSubmit.OnSelect 呼叫通用模式：                                      │
│                                                                             │
│       Set(varIsLoading, true);                                              │
│       Set(varResult, [FlowName].Run(                                        │
│           [Parameters]                                                      │
│       ));                                                                   │
│       Set(varIsLoading, false);                                             │
│       If(varResult.Status = "Success",                                      │
│           Set(varSuccessMessage, varResult.Message);                        │
│           Set(varShowSuccess, true),                                        │
│           Set(varErrorMessage, varResult.Message);                          │
│           Set(varErrorCode, varResult.ErrorCode);                           │
│           Set(varShowError, true)                                           │
│       );                                                                    │
│                                                                             │
│     • 每個表單僅變更 Flow 名稱與參數                                          │
│     • 結果處理模式在所有表單中【相同】                                        │
│                                                                             │
│  3. 訊息區塊標準化                                                           │
│     • 訊息區塊透過變數接收文字                                               │
│     • Flow 回應解析為標準變數                                                │
│     • 無 Flow 特定訊息處理                                                   │
│                                                                             │
│  需要變更：複製模板、修改 Section 內容、變更 Flow                              │
│  禁止變更：Header、Footer、訊息區塊結構                                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 7.3 新增 Gate（零 Stepper 重建）

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  情境：新增 Gate4 或移除 Gate2                                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  架構透過以下方式實現：                                                       │
│                                                                             │
│  1. 資料驅動 STEPPER                                                         │
│     • Gate 步驟定義於 colGateSteps 集合                                      │
│     • Stepper 從集合動態渲染                                                 │
│     • 無硬編碼步驟控制項                                                     │
│                                                                             │
│  2. 單點變更                                                                 │
│     • 修改 App.OnStart 中的 colGateSteps：                                   │
│                                                                             │
│       // 新增 Gate4：                                                        │
│       ClearCollect(colGateSteps,                                            │
│           {Index: 0, Label: "Pending", Value: "Pending"},                   │
│           {Index: 1, Label: "Gate0", Value: "Gate0"},                       │
│           {Index: 2, Label: "Gate1", Value: "Gate1"},                       │
│           {Index: 3, Label: "Gate2", Value: "Gate2"},                       │
│           {Index: 4, Label: "Gate3", Value: "Gate3"},                       │
│           {Index: 5, Label: "Gate4", Value: "Gate4"},    // 新增            │
│           {Index: 6, Label: "Closed", Value: "Closed"}                      │
│       );                                                                    │
│                                                                             │
│  3. 基於索引的目前狀態                                                       │
│     • varCurrentGateIndex 控制高亮顯示                                       │
│     • Gallery 模板使用 ThisItem.Index 比對                                   │
│     • UI 中無基於字串的 Gate 比對                                            │
│                                                                             │
│  需要變更：在【一個位置】修改 colGateSteps 集合                               │
│  禁止變更：個別畫面的 Stepper 修改                                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 7.4 更改品牌色彩（零表單修改）

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  情境：品牌重塑，從 #0C3467 改為新色彩                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  架構透過以下方式實現：                                                       │
│                                                                             │
│  1. 集中式色彩定義                                                           │
│     • 所有色彩【僅】定義於 App.OnStart                                       │
│     • 所有控制項引用變數，非硬編碼值                                          │
│                                                                             │
│  2. 單點變更                                                                 │
│     • 修改 App.OnStart 中的【一行】：                                        │
│                                                                             │
│       // 變更前：                                                            │
│       Set(varBrandPrimary, ColorValue("#0C3467"));                          │
│                                                                             │
│       // 變更後：                                                            │
│       Set(varBrandPrimary, ColorValue("#新色碼"));                           │
│                                                                             │
│  3. 自動傳播                                                                 │
│     • 所有 Header、Button、Stepper、Badge 控制項自動更新                     │
│     • 無需修改個別控制項                                                     │
│                                                                             │
│  4. 組件庫增強                                                               │
│     • 若使用 cmpBrandColorProvider 組件：                                    │
│     • 組件中的變更自動更新所有使用該組件的畫面                                │
│                                                                             │
│  需要變更：App.OnStart 中的【一行】                                          │
│  禁止變更：任何個別控制項色彩屬性                                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 7.5 新增 KPI 覆蓋層（零 UI 干擾）

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  情境：在表單上新增 KPI 儀表板覆蓋層                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  架構透過以下方式實現：                                                       │
│                                                                             │
│  1. 覆蓋層架構                                                               │
│     • Z-index 分層允許非破壞性覆蓋層                                         │
│     • KPI 面板可從右側滑入                                                   │
│     • 不影響既有五區塊結構                                                   │
│                                                                             │
│  2. 保留覆蓋區域                                                             │
│     • rectKPIOverlay（選用，預設隱藏）                                       │
│     • 位置：右側邊緣，全高度                                                 │
│     • Visible: varShowKPIPanel                                              │
│                                                                             │
│     含 KPI 的畫面結構：                                                       │
│     ┌────────────────────────────────────┬──────────────────┐               │
│     │  [既有 5 區塊佈局]                  │  [KPI 覆蓋層]    │               │
│     │                                    │  （滑入式）      │               │
│     │  Header                            │                  │               │
│     │  Stepper                           │  儀表板          │               │
│     │  Body                              │  圖表            │               │
│     │  Footer                            │  指標            │               │
│     │                                    │                  │               │
│     └────────────────────────────────────┴──────────────────┘               │
│                                                                             │
│  3. 實作模式                                                                 │
│     • 將 rectKPIOverlay 新增至模板（預設 Visible: false）                    │
│     • 在 Header 新增 btnShowKPI（選用）                                      │
│     • KPI 內容獨立於表單邏輯                                                 │
│                                                                             │
│  需要變更：將覆蓋層容器新增至模板                                             │
│  禁止變更：既有區塊的修改                                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 7.6 穩定性保證矩陣

| 變更類型 | 修改檔案數 | 變更行數 | 影響既有表單 |
|---------|-----------|---------|:------------:|
| 新增 Flow | 0 個既有 | 0 | ❌ 無 |
| 新增 Gate | 1（App.OnStart） | ~2 | ❌ 無 |
| 更改品牌色彩 | 1（App.OnStart） | 1 | ❌ 無（自動更新） |
| 新增 KPI 覆蓋層 | 1（模板） | ~50 | ❌ 無（選用） |
| 新增表單類型 | 1（新畫面） | ~100 | ❌ 無 |
| 修改驗證規則 | 1（目標畫面） | ~10 | ❌ 無 |

---

# 第五部分：附錄

## 附錄 X：Canvas 模板架構圖

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    CANVAS 模板架構圖                                           ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  ┌─────────────────────────────────────────────────────────────────────────┐  ║
║  │                           APP 層級                                       │  ║
║  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐          │  ║
║  │  │ App.OnStart     │  │ cmpBrandColor   │  │ colGateSteps    │          │  ║
║  │  │                 │  │ Provider        │  │（集合）         │          │  ║
║  │  │ • 色彩變數      │  │                 │  │                 │          │  ║
║  │  │ • 佈局變數      │  │ 分發色彩至      │  │ 定義 Gate       │          │  ║
║  │  │ • 狀態變數      │  │ 所有組件        │  │ 序列            │          │  ║
║  │  │ • 集合          │  │                 │  │ 資料驅動        │          │  ║
║  │  └─────────────────┘  └─────────────────┘  └─────────────────┘          │  ║
║  └─────────────────────────────────────────────────────────────────────────┘  ║
║                                    │                                          ║
║                                    ▼                                          ║
║  ┌─────────────────────────────────────────────────────────────────────────┐  ║
║  │                      畫面模板                                            │  ║
║  │                 (scrTemplate_Governance)                                 │  ║
║  │                                                                          │  ║
║  │  ┌───────────────────────────────────────────────────────────────────┐   │  ║
║  │  │  區塊 1：HEADER (rectHeader)                   [不可變更]         │   │  ║
║  │  │  ├── imgLogo                                                      │   │  ║
║  │  │  ├── lblHeaderTitle                                               │   │  ║
║  │  │  ├── badgeHeaderStatus                                            │   │  ║
║  │  │  └── lblHeaderUserName                                            │   │  ║
║  │  ├───────────────────────────────────────────────────────────────────┤   │  ║
║  │  │  區塊 2：GATE STEPPER (rectGateStepper)        [不可變更]         │   │  ║
║  │  │  └── galGateStepper (Items: colGateSteps)                         │   │  ║
║  │  │      └── 模板：cirStep、lblStepLabel、lineConnector               │   │  ║
║  │  ├───────────────────────────────────────────────────────────────────┤   │  ║
║  │  │  區塊 3：BODY (rectBody)                                          │   │  ║
║  │  │  ├── rectSection1 ─────────────────────────── [可修改]            │   │  ║
║  │  │  │   └── [表單特定控制項]                                         │   │  ║
║  │  │  ├── rectSection2 ─────────────────────────── [可修改]            │   │  ║
║  │  │  │   └── [表單特定控制項]                                         │   │  ║
║  │  │  └── rectSection3 ─────────────────────────── [可修改]            │   │  ║
║  │  │      └── [表單特定控制項]                                         │   │  ║
║  │  ├───────────────────────────────────────────────────────────────────┤   │  ║
║  │  │  區塊 4：FOOTER (rectFooter)                   [不可變更]         │   │  ║
║  │  │  ├── btnCancel（Ghost，左側）                                     │   │  ║
║  │  │  └── btnSubmit（Primary，右側）                                   │   │  ║
║  │  ├───────────────────────────────────────────────────────────────────┤   │  ║
║  │  │  區塊 5：訊息覆蓋層                            [不可變更]         │   │  ║
║  │  │  ├── rectMessageSuccess                                           │   │  ║
║  │  │  └── rectMessageError                                             │   │  ║
║  │  └───────────────────────────────────────────────────────────────────┘   │  ║
║  │                                                                          │  ║
║  │  ┌───────────────────────────────────────────────────────────────────┐   │  ║
║  │  │  選用：KPI 覆蓋層 (rectKPIOverlay)             [可擴充]           │   │  ║
║  │  │  └── 未來 KPI 儀表板的滑入面板                                    │   │  ║
║  │  └───────────────────────────────────────────────────────────────────┘   │  ║
║  │                                                                          │  ║
║  └─────────────────────────────────────────────────────────────────────────┘  ║
║                                    │                                          ║
║                    ┌───────────────┼───────────────┐                          ║
║                    ▼               ▼               ▼                          ║
║  ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐               ║
║  │ scrCreateProject │ │ scrGateRequest   │ │ scrDocumentIntake│               ║
║  │                  │ │                  │ │                  │               ║
║  │ 從模板複製      │ │ 從模板複製      │ │ 從模板複製      │               ║
║  │                  │ │                  │ │                  │               ║
║  │ 已修改：        │ │ 已修改：        │ │ 已修改：        │               ║
║  │ • Section 內容  │ │ • Section 內容  │ │ • Section 內容  │               ║
║  │ • Header 標題   │ │ • Header 標題   │ │ • Header 標題   │               ║
║  │ • 提交邏輯      │ │ • 提交邏輯      │ │ • 提交邏輯      │               ║
║  └──────────────────┘ └──────────────────┘ └──────────────────┘               ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## 附錄 Y：反脆弱 UI 強制規則

### Y.1 完整規則參照

| 規則 ID | 類別 | 規則敘述 | 嚴重程度 |
|---------|------|---------|:--------:|
| C-001 | 色彩 | 所有色彩值【必須】透過變數引用 | 嚴重 |
| C-002 | 色彩 | 所有色彩變數【必須】定義於 App.OnStart | 嚴重 |
| C-003 | 色彩 | 色彩變數名稱【必須】完全符合規格 | 高 |
| C-004 | 色彩 | 色彩使用【必須】遵循語義對應 | 高 |
| C-005 | 色彩 | varBrandPrimary【僅限】用於 Header/Button/Gate | 高 |
| T-001 | 模板 | 直接建立新畫面【禁止】 | 嚴重 |
| T-002 | 模板 | 不可變組件【禁止】修改 | 嚴重 |
| T-003 | 模板 | 僅允許經許可的修改 | 高 |
| T-004 | 模板 | 畫面命名【必須】遵循模式 | 中 |
| P-001 | 位置 | 直接 X/Y 數值【禁止】 | 高 |
| P-002 | 位置 | Width【必須】使用 Parent.Width 或相對計算 | 高 |
| P-003 | 位置 | 響應式佈局【必須】使用 Layout Container | 中 |
| P-004 | 位置 | Section Y 座標【必須】動態計算 | 高 |
| D-001 | DisplayMode | DisplayMode 中行內 And()【禁止】 | 嚴重 |
| D-002 | DisplayMode | 表單驗證【必須】集中化 | 高 |
| D-003 | DisplayMode | DisplayMode【必須】回傳列舉值 | 高 |
| V-001 | 變數 | 每個表單【必須】只有一個驗證變數 | 高 |
| V-002 | 變數 | 表單狀態【必須】透過標準變數管理 | 高 |
| V-003 | 變數 | 表單特定變數【必須】使用前綴 varForm_ | 中 |
| V-004 | 變數 | varFormValid【必須】適當重新計算 | 高 |
| M-001 | 訊息 | 僅【允許】成功與錯誤訊息類型 | 中 |
| M-002 | 訊息 | 訊息區塊【必須】使用標準化結構 | 高 |
| M-003 | 訊息 | 訊息位置【固定】於 Y: varHeaderHeight | 高 |
| M-004 | 訊息 | 成功與錯誤訊息【互斥】 | 中 |
| M-005 | 訊息 | 訊息顯示邏輯【必須】遵循標準模式 | 中 |
| S-001 | Stepper | 每個畫面【必須】只有零個或一個 Gate Stepper | 高 |
| S-002 | Stepper | Gate Stepper【必須】資料驅動 | 嚴重 |
| S-003 | Stepper | Gate 步驟資料【必須】定義於 App.OnStart | 高 |
| S-004 | Stepper | 目前 Gate【必須】透過 varCurrentGateIndex 指示 | 高 |

### Y.2 嚴重程度定義

| 嚴重程度 | 影響 | 必要行動 |
|:---------|:------|:---------|
| 嚴重 | 系統崩潰、安全風險或治理繞過 | 立即修復，阻擋部署 |
| 高 | 顯著維護性或一致性影響 | 程式碼審查核准前修復 |
| 中 | 輕微不一致、最佳實踐違規 | 下次維護週期修復 |

---

## 附錄 Z：人為錯誤預防檢查清單

### Z.1 開發前檢查清單

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  開發前檢查清單                                                              │
│  在開始任何新表單開發前完成                                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ☐ 確認 App.OnStart 包含完整色彩調色盤（21 個變數）                          │
│  ☐ 確認 App.OnStart 包含佈局常數                                            │
│  ☐ 確認 colGateSteps 集合已定義                                             │
│  ☐ 確認 scrTemplate_Governance 存在且為最新版本                              │
│  ☐ 確認所有必要的資料連線已新增                                              │
│  ☐ 複製模板（禁止建立空白畫面）                                              │
│  ☐ 依模式重新命名畫面：scr[表單名稱]                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Z.2 開發中檢查清單

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  開發中檢查清單                                                              │
│  開發期間持續驗證                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  色彩檢查：                                                                  │
│  ☐ 所有 Fill 屬性使用色彩變數                                               │
│  ☐ 任何公式中無 ColorValue("#XXXXXX")                                       │
│  ☐ 無 Color.Blue、Color.Red 等硬編碼色彩                                    │
│                                                                             │
│  位置檢查：                                                                  │
│  ☐ 無硬編碼 X 值（除了 0）                                                   │
│  ☐ 無硬編碼 Y 值（使用變數）                                                 │
│  ☐ Width 使用 Parent.Width 或相對計算                                       │
│  ☐ Section Y 使用上一個 Section 位置 + 高度 + 間距                          │
│                                                                             │
│  模板檢查：                                                                  │
│  ☐ rectHeader 未修改（除了 lblHeaderTitle.Text）                            │
│  ☐ rectGateStepper 未修改（除了 Visible）                                   │
│  ☐ rectFooter 未修改（除了 btnSubmit.Text 與 OnSelect）                     │
│  ☐ rectMessage* 未修改                                                      │
│                                                                             │
│  DisplayMode 檢查：                                                          │
│  ☐ btnSubmit.DisplayMode 引用 varFormValid                                  │
│  ☐ 任何 DisplayMode 屬性中無行內 And()                                      │
│  ☐ 所有 DisplayMode 回傳 DisplayMode.Edit 或 DisplayMode.Disabled           │
│                                                                             │
│  命名檢查：                                                                  │
│  ☐ 無預設名稱（TextInput1、Button2 等）                                     │
│  ☐ 所有控制項使用正確前綴（lbl、txt、dd、cmb、btn、rect、ico）              │
│  ☐ Section 控制項使用 S1_、S2_、S3_ 前綴                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Z.3 部署前檢查清單

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  部署前檢查清單                                                              │
│  在發佈或匯出前完成                                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  結構驗證：                                                                  │
│  ☐ Header 高度為 80px                                                       │
│  ☐ Gate Stepper 高度為 50px（若可見）                                       │
│  ☐ Footer 高度為 72px                                                       │
│  ☐ Footer Y 為 Parent.Height - 72                                          │
│  ☐ 三個 Section 存在（基本資訊、責任歸屬、詳細資料）                         │
│                                                                             │
│  色彩驗證：                                                                  │
│  ☐ Header Fill 為 varBrandPrimary                                          │
│  ☐ Header 文字為 varTextOnPrimary                                          │
│  ☐ Section Fill 為 varCardWhite                                            │
│  ☐ btnSubmit Fill 為 varBrandPrimary                                       │
│  ☐ btnCancel 為透明（Ghost 樣式）                                           │
│                                                                             │
│  功能驗證：                                                                  │
│  ☐ 預覽模式：所有欄位正確渲染                                               │
│  ☐ 預覽模式：必填欄位為空時停用提交                                         │
│  ☐ 預覽模式：所有必填欄位填寫後啟用提交                                     │
│  ☐ 訊息區塊在成功/錯誤時正確顯示                                            │
│  ☐ 載入覆蓋層在提交時顯示                                                   │
│                                                                             │
│  Flow 整合：                                                                 │
│  ☐ Flow 連線已新增                                                          │
│  ☐ Flow.Run() 參數符合 Flow 定義                                            │
│  ☐ 結果解析處理 Status、Message、ErrorCode                                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Z.4 錯誤偵測模式

| 錯誤類型 | 偵測方法 | 預防方法 |
|:---------|:---------|:---------|
| 行內色彩 | 搜尋 `ColorValue("#` | 使用尋找取代為變數 |
| 硬編碼位置 | 搜尋 `Y: [0-9]`（除了 Y: 0） | 使用佈局變數 |
| 預設命名 | 搜尋 `TextInput`、`Button`、`Label` + 數字 | 建立後立即重新命名 |
| DisplayMode 行內 And() | 搜尋 `DisplayMode: If(And(` | 提取至 varFormValid |
| 重複 Stepper | 計算 `icoStep_` 控制項數量 | 使用 Gallery 形式 Stepper |
| 模板修改 | 與 scrTemplate_Governance 比對 | 還原未授權變更 |

---

## 版本歷史

| 版本 | 日期 | 變更說明 |
|:------|:------|:---------|
| v1.0 | 2026-02-11 | 初版品牌 UI 標準 |
| v1.1 | 2026-02-11 | 統一雙權威、新增施工指南 |
| v1.2 | 2026-02-11 | 反脆弱強化、模板強制、3 年穩定性 |
| v1.2.1 | 2026-02-11 | 修正 BorderRadius 規格、新增控制項能力對照表、新增操作手冊參考 |

---

## 已取代文件

以下文件已被本標準【取代】，【禁止】引用：

| 文件 | 狀態 | 取代日期 |
|:------|:------|:---------|
| Canvas-Brand-UI-Standard-v1.md | ❌ 已棄用 | 2026-02-11 |
| Canvas-Brand-UI-Standard-v1.1.md | ❌ 已棄用 | 2026-02-11 |
| Canvas-UI-Governance-Standard-v1.md | ❌ 已棄用 | 2026-02-11 |

---

**文件結束**

**本標準為 Canvas App UI 治理之【唯一權威】。**
**v1.2 版建立 3 年穩定架構（2026-2029）。**
**未經授權之修改【禁止】。**
