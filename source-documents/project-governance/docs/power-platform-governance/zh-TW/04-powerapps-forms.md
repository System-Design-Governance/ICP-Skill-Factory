# Power Apps 治理表單建置指南

**文件版本**：v7.4（Anti-Fragile Edition — KPI Evidence Collection）
**建立日期**：2026-01-29
**最後更新**：2026-03-05
**版本類型**：Hardening Upgrade
**適用系統**：Design Governance System（Dataverse 架構）
**前置文件**：01-prerequisites-and-environment.md、02-dataverse-data-model-and-security.md、03-sharepoint-architecture.md
**後續文件**：05-core-flows-implementation-runbook.md
**品牌標準**：appendix/Canvas-Brand-UI-Standard-v1.2.md（Anti-Fragile Edition）

---

## 本章閱讀指南

### 品牌 UI 標準依據

**本章所有表單必須遵循 Canvas Brand UI Standard v1.2（Anti-Fragile Edition）**

→ [appendix/Canvas-Brand-UI-Standard-v1.2.md](appendix/Canvas-Brand-UI-Standard-v1.2.md)

> ⚠️ **注意**：v1.0 及 v1.1 已棄用。請使用 v1.2 作為唯一設計依據。

該標準定義：
- 品牌色彩系統（Brand Primary #0C3467）
- 五區塊畫面骨架（IMMUTABLE）
- 三 Section 資訊分類
- Flow-Only 欄位視覺規則
- Button 排列與色彩規範
- **模板強制化架構（Template Enforcement）**
- **人為錯誤防護機制（Human Error Containment）**
- **3 年穩定性藍圖（3-Year Stability Blueprint）**

### 品牌色彩速查

| 色彩 | 色碼 | 用途 |
|:----|:----|:----|
| **Brand Primary** | #0C3467 | Header、Primary Button、目前 Gate |
| **Brand Accent** | #008EC3 | Focus 邊框、Hyperlink |
| **Neutral Gray** | #999999 | Readonly、Disabled |
| **Text Base** | #2D2D2D | 內文主字色 |
| **Danger** | #A4262C | 終止操作、錯誤訊息 |

### 占位符參考

→ [00C-placeholder-reference.md](00C-placeholder-reference.md)

---

## 治理角色定位聲明

### Power Apps 之治理定位

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Power Apps 治理角色定位宣告                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Power Apps 為使用者介面（UI）層。                                           │
│                                                                             │
│  Power Apps 之職責：                                                         │
│  ✓ 呈現資料供使用者檢視                                                      │
│  ✓ 收集使用者輸入                                                           │
│  ✓ 提供基本輸入格式驗證（UX 層）                                            │
│  ✓ 呼叫 Power Automate Flow                                                 │
│  ✓ 顯示 Flow 回傳之結果                                                     │
│                                                                             │
│  Power Apps 不具備之職責：                                                   │
│  ✗ 寫入治理狀態欄位                                                         │
│  ✗ 決定治理結果                                                             │
│  ✗ 執行治理驗證                                                             │
│  ✗ 形成治理事實                                                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 不可違反之原則

| 原則 | 說明 |
|:----|:----|
| Power Apps 不得直接寫入治理表 | 所有寫入必須透過 Flow |
| Power Apps 驗證不具治理效力 | Flow 必須重新驗證所有輸入 |
| 使用者操作不構成治理事實 | 治理事實由 Flow 寫入 Dataverse 後成立 |
| 表單狀態不決定治理結果 | 治理結果由 Flow 判定並回傳 |

---

## 表單欄位分類矩陣

### 欄位分類定義

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  欄位分類判準                                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  判準原則：以【治理語義】為準，非以【技術實作】為準。                          │
│                                                                             │
│  類別 1：使用者輸入欄位（User Input）                                        │
│  定義：使用者在表單中主動填寫或選擇的資料                                     │
│  控制項：Text input、Dropdown、ComboBox、Date picker                        │
│  DisplayMode：DisplayMode.Edit                                              │
│  標籤：無特殊後綴                                                            │
│                                                                             │
│  類別 2：使用者指派欄位（User Assignment）                                   │
│  定義：使用者在表單中指定責任人或角色                                         │
│  控制項：ComboBox（搜尋人員）、Dropdown（選擇角色）                          │
│  DisplayMode：DisplayMode.Edit                                              │
│  標籤：無特殊後綴，但應標示為必填（*）                                       │
│  ⚠️ 注意：責任指派屬於【使用者決策】，不是 Flow-Only                         │
│                                                                             │
│  類別 3：系統產生欄位（System Generated / Flow-Only）                        │
│  定義：由 Flow 或系統自動產生，使用者無權編輯                                 │
│  控制項：Label（禁止使用 Text input）                                        │
│  DisplayMode：DisplayMode.View                                              │
│  標籤：後綴「(System-controlled)」                                           │
│  視覺：背景 varFlowOnlyBg、文字 varTextSecondary                             │
│                                                                             │
│  類別 4：審核決策欄位（Approval Decision）                                   │
│  定義：審核者在審批表單中做出的決策                                           │
│  控制項：Dropdown（Approve/Reject）、Text input（審核意見）                  │
│  DisplayMode：依權限動態判斷                                                 │
│  標籤：無特殊後綴，應標示決策性質                                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 欄位分類矩陣（所有表單適用）

| 欄位名稱 | Schema Name | 類別 | 控制項類型 | Flow-Only | 說明 |
|:--------|:-----------|:----|:---------|:---------:|:----|
| **基本資訊（Section 1）** |
| Request ID | gov_requestid | 系統產生 | Label | ✓ | 由 Flow 產生流水號 |
| Project Title | gov_title | 使用者輸入 | Text input | ❌ | 使用者輸入專案名稱 |
| Project Status | gov_projectstatus | 系統產生 | Label + Badge | ✓ | 由 Flow 控制狀態轉換 |
| Current Gate | gov_currentgate | 系統產生 | Label + Badge | ✓ | 由 Flow 控制 Gate 進度 |
| Request Status | gov_requeststatus | 系統產生 | Label + Badge | ✓ | 由 Flow 控制申請狀態 |
| **責任歸屬（Section 2）** |
| System Architect | gov_systemarchitect | 使用者輸入 | Label (自動帶入) | ❌ | 建立者，自動帶入 varCurrentUser（Lookup User，非 email 字串） |
| Project Manager | gov_projectmanager | **使用者指派** | ComboBox | ❌ | 由建立者指派 |
| Approver | gov_approver | 系統產生 | Label | ✓ | 由 Flow 依規則指派（顯示用，來自 Flow 回傳，非 Dataverse 綁定欄位） |
| **詳細資料（Section 3）** |
| Project Type | gov_projecttype | 使用者輸入 | Dropdown | ❌ | 使用者選擇專案類型 |
| Target Security Level | gov_targetsl | 使用者輸入 | Dropdown | ❌ | 使用者選擇目標 SL |
| Description | gov_projectdescription | 使用者輸入 | Text input (MultiLine) | ❌ | 使用者輸入說明 |
| **系統時間戳記** |
| Created On | createdon | 系統產生 | Label | ✓ | 系統自動記錄 |
| Modified On | modifiedon | 系統產生 | Label | ✓ | 系統自動記錄 |
| Created By | createdby | 系統產生 | Label | ✓ | 系統自動記錄 |

### 常見誤判修正

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ⚠️ 欄位分類常見誤判                                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  誤判 1：Project Manager 標為 Flow-Only                                     │
│  ├── 錯誤原因：誤以為責任欄位由系統決定                                      │
│  ├── 正確分類：使用者指派                                                    │
│  ├── 治理語義：專案經理由系統架構師在建立專案時指派                          │
│  └── 修正做法：使用 ComboBox，允許使用者搜尋並選擇                          │
│                                                                             │
│  誤判 2：System Architect 標為可編輯                                         │
│  ├── 錯誤原因：誤以為可以任意指定架構師                                      │
│  ├── 正確分類：使用者輸入（但自動帶入，非 Flow-Only）                        │
│  ├── 治理語義：系統架構師為建立者本人，不可指定他人                          │
│  ├── 資料類型：Lookup (User table)，非文字欄位                               │
│  ├── 顯示做法：Label 顯示 varCurrentUserName（人類可讀）                     │
│  └── 提交做法：傳送 varCurrentUser（User 記錄）至 Flow                       │
│                                                                             │
│  ⚠️ 常見錯誤：使用 varCurrentUserEmail（email 字串）                         │
│     → 錯誤原因：Dataverse Lookup 欄位需要 User 記錄，非 email 字串           │
│     → 正確做法：顯示用 varCurrentUserName，提交用 varCurrentUser             │
│                                                                             │
│  誤判 3：Approver 標為使用者指派                                             │
│  ├── 錯誤原因：誤以為申請者可以選擇審核者                                    │
│  ├── 正確分類：系統產生（Flow-Only）                                         │
│  ├── 治理語義：審核者由 Flow 依業務規則自動指派                              │
│  └── 修正做法：使用 Label，標註 (System-controlled)                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 通用表單模板

### 共用元件命名規範

**固定命名（所有表單一致）**：

| 區塊 | 容器控制項 | 標題控制項 | 說明 |
|:----|:----------|:----------|:----|
| Header | rectHeader | lblHeaderTitle | 固定高度 80px |
| Gate Stepper | rectGateStepper | galGateStepper | 固定高度 50px |
| Body | rectBody | - | 動態高度 |
| Section 1 | cntSection1 或 rectSection1 | lblS1_Title | 基本資訊 |
| Section 2 | cntSection2 或 rectSection2 | lblS2_Title | 責任歸屬 |
| Section 3 | cntSection3 或 rectSection3 | lblS3_Title | 詳細資料 |
| Footer | rectFooter | - | 固定高度 72px |
| Message Success | rectMessageSuccess | lblMessageSuccessText | Y=80 覆蓋層 |
| Message Error | rectMessageError | lblMessageErrorText | Y=80 覆蓋層 |

> **控制項類型說明**：
> - `cnt*`：Modern Container（支援 BorderRadius，推薦）
> - `rect*`：Classic Rectangle（直角設計，降級方案）
> - 詳見 [Canvas-Brand-UI-Standard-v1.2.md](appendix/Canvas-Brand-UI-Standard-v1.2.md) 第 2.3 節

**變數使用規範（App.OnStart 定義）**：

| 變數分類 | 變數名稱 | 類型 | 說明 |
|:--------|:--------|:----|:----|
| **區塊高度** | varHeaderHeight | Number | 80 |
| | varStepperHeight | Number | 50 |
| | varFooterHeight | Number | 72 |
| | varMessageHeight | Number | 60 |
| **間距** | varSectionMargin | Number | 20（Section 左右邊距） |
| | varSectionSpacing | Number | 16（Section 間距） |
| | varSpacingMD | Number | 16（控制項間距） |
| | varSpacingXS | Number | 8（標籤與輸入框間距） |
| **動態 Y** | varBodyY | Number | 動態計算，參考 Stepper 可見性 |
| **表單狀態** | varFormValid | Boolean | 表單驗證狀態 |
| | varIsLoading | Boolean | 載入中狀態 |
| | varShowSuccess | Boolean | 成功訊息可見性 |
| | varShowError | Boolean | 錯誤訊息可見性 |

### Flow-Only 欄位視覺規範

**唯一做法（禁止變體）**：

```
控制項類型：Label（禁止 Text input）

視覺規格：
├── Fill: varFlowOnlyBg (#EFEFEF)
├── Color: varTextSecondary (#666666)
├── BorderColor: varBorderLight (#E1E1E1)
├── BorderThickness: 1
├── Height: 36
├── PaddingLeft: 12

標籤規格：
├── 標籤文字：欄位名稱 + " (System-controlled)"
├── 標籤 Color: varTextBase
├── 標籤 Size: 13

範例：
┌────────────────────────────────────────────────────────────────────────────┐
│  Request ID (System-controlled)                  ← 標籤                    │
│  ┌──────────────────────────────────────────────────────────────────────┐ │
│  │  DR-2026-00001234                             ← Label 控制項          │ │
│  └──────────────────────────────────────────────────────────────────────┘ │
│        Fill: varFlowOnlyBg | Color: varTextSecondary                      │
└────────────────────────────────────────────────────────────────────────────┘
```

### 操作手冊參考

> **詳細操作步驟與故障排除**：
> - 屬性找不到時的兩條路徑
> - BorderRadius 不支援的替代方案
> - 控制項類型確認方法
>
> 請參閱 [appendix/Canvas-Editor-Operability-Playbook-v1.md](appendix/Canvas-Editor-Operability-Playbook-v1.md)

---

## App.OnStart 品牌設定

**操作路徑**：

```
1. 樹狀檢視 → 選取最頂層「App」
2. 公式列 → 屬性下拉 → 選擇「OnStart」
3. 貼上以下完整模板
```

**完整模板（依據 Canvas-Brand-UI-Standard-v1.2.md）**：

```
// ═══════════════════════════════════════════════════════════
// App.OnStart - Governance Canvas App Brand Template v1.0
// 依據：appendix/Canvas-Brand-UI-Standard-v1.2.md
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

**驗證**：按 F5 進入預覽，若無錯誤表示設定成功。

---

## 畫面骨架標準結構

### 標準五區塊配置

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ① HEADER（高度 80）                                                         │
│  ████████████████████████████████████████████████████████████████████████████│
│  █  表單名稱                                    [Badge]      使用者名稱    █│
│  ████████████████████████████████████████████████████████████████████████████│
│  Fill: varBrandPrimary (#0C3467) | Text: varTextOnPrimary                    │
├─────────────────────────────────────────────────────────────────────────────┤
│  ② GATE STEPPER（高度 50）                                                   │
│  ●━━━━●━━━━◉━━━━○━━━━○━━━━○                                                  │
│  Fill: varNeutralLighter                                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│  ③ MAIN BODY（動態高度）                                                     │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  Section 1: Basic Information                                           ││
│  │  RequestID (System-controlled), Title, Status                           ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  Section 2: Responsibility                                              ││
│  │  System Architect (System-controlled), Project Manager                  ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  Section 3: Details                                                     ││
│  │  可編輯欄位、說明資訊                                                    ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│  Fill: varBackground                                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│  ④ FOOTER（高度 72）                                                         │
│  [Cancel]                                                          [Submit] │
│  左側                                                                 右側  │
│  Fill: varCardWhite | Border-top: varBorderLight                            │
├─────────────────────────────────────────────────────────────────────────────┤
│  ⑤ MESSAGE AREA（高度 60，位於 Y=80）                                        │
│  [Success/Error 訊息]                                                 [X]   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## FORM-001：專案建立表單

### 表單概述

| 項目 | 內容 |
|:----|:----|
| **對應 Flow** | GOV-001-CreateProject |
| **使用角色** | System Architect |
| **對應畫面** | scrCreateProject |
| **Gate Stepper** | 隱藏（新專案無 Gate） |
| **品牌標準** | appendix/Canvas-Brand-UI-Standard-v1.2.md |

---

### Step 1：建立 Header

**操作路徑**：插入 → 圖形 → 矩形

**控制項設定**：

| 屬性 | 設定方式 | 值 |
|:----|:--------|:--|
| 名稱 | 樹狀檢視重命名 | `rectHeader` |
| X | 右側屬性面板 | `0` |
| Y | 右側屬性面板 | `0` |
| Width | 右側屬性面板 | `Parent.Width` |
| Height | 右側屬性面板 | `varHeaderHeight` |
| Fill | 公式列 | `varBrandPrimary` |
| BorderThickness | 右側屬性面板 | `0` |

**驗證**：Header 應顯示為深藍色（#0C3467）橫條。

---

### Step 2：建立 Header 標題

**操作路徑**：插入 → 顯示 → 標籤

**控制項設定**：

| 屬性 | 設定方式 | 值 |
|:----|:--------|:--|
| 名稱 | 樹狀檢視重命名 | `lblHeaderTitle` |
| Text | 公式列 | `"建立新專案"` |
| X | 公式列 | `varSpacingLG` |
| Y | 公式列 | `(varHeaderHeight - Self.Height) / 2` |
| Width | 右側屬性面板 | `300` |
| Height | 右側屬性面板 | `40` |
| Color | 公式列 | `varTextOnPrimary` |
| Size | 右側屬性面板 | `20` |
| Font | 公式列 | `Font.'Segoe UI Semibold'` |

---

### Step 3：建立 Header 使用者名稱

**操作路徑**：插入 → 顯示 → 標籤

**控制項設定**：

| 屬性 | 值 |
|:----|:--|
| 名稱 | `lblHeaderUserName` |
| Text | `varCurrentUserName` |
| X | `Parent.Width - Self.Width - varSpacingLG` |
| Y | `(varHeaderHeight - Self.Height) / 2` |
| Color | `varTextOnPrimary` |
| Size | `14` |
| Align | `Align.Right` |

---

### Step 4：建立 Body 容器

**操作路徑**：插入 → 圖形 → 矩形

**控制項設定**：

| 屬性 | 值 |
|:----|:--|
| 名稱 | `rectBody` |
| X | `0` |
| Y | `varHeaderHeight` |
| Width | `Parent.Width` |
| Height | `Parent.Height - varHeaderHeight - varFooterHeight` |
| Fill | `varBackground` |
| BorderThickness | `0` |

---

### Step 5：建立 Section 1 - Basic Information

**操作路徑**：
- 推薦：插入 → Modern → Container（支援圓角）
- 降級：插入 → 圖形 → 矩形（直角設計）

> ⚠️ **注意**：Classic Rectangle **不支援** BorderRadius。
> 若需圓角效果，請使用 Modern Container。
> 詳見 [Canvas-Editor-Operability-Playbook-v1.md](appendix/Canvas-Editor-Operability-Playbook-v1.md) 第三章。

**控制項設定（容器）**：

| 屬性 | Modern Container | Classic Rectangle |
|:----|:----------------|:-----------------|
| 名稱 | `cntSection1` | `rectSection1` |
| X | `varSpacingLG` | `varSpacingLG` |
| Y | `rectBody.Y + varSpacingLG` | `rectBody.Y + varSpacingLG` |
| Width | `Parent.Width - varSpacingLG * 2` | `Parent.Width - varSpacingLG * 2` |
| Height | `100` | `100` |
| Fill | `varCardWhite` | `varCardWhite` |
| BorderColor | `varBorderLight` | `varBorderLight` |
| BorderThickness | `1` | `1` |
| BorderRadius | `8` ✓ | ❌ 不支援 |
| LayoutMode | `"Manual"` | N/A |

**Section 標題**：

```
lblS1_Title:
├── 名稱: lblS1_Title
├── Text: "Basic Information"
├── X: rectSection1.X + varSpacingMD
├── Y: rectSection1.Y + varSpacingMD
├── Color: varTextBase
├── Size: 16
├── Font: Font.'Segoe UI Semibold'
```

**新專案提示**：

```
lblS1_NewProjectHint:
├── 名稱: lblS1_NewProjectHint
├── Text: "Request ID 將於提交後由系統產生"
├── X: lblS1_Title.X
├── Y: lblS1_Title.Y + lblS1_Title.Height + varSpacingXS
├── Color: varTextSecondary
├── Size: 13
```

---

### Step 6：建立 Section 2 - Responsibility

**操作路徑**：同 Step 5（Container 或 Rectangle）

**控制項設定（容器）**：

| 屬性 | Modern Container | Classic Rectangle |
|:----|:----------------|:-----------------|
| 名稱 | `cntSection2` | `rectSection2` |
| X | `varSpacingLG` | `varSpacingLG` |
| Y | `cntSection1.Y + cntSection1.Height + varSpacingMD` | `rectSection1.Y + rectSection1.Height + varSpacingMD` |
| Width | `Parent.Width - varSpacingLG * 2` | `Parent.Width - varSpacingLG * 2` |
| Height | `120` | `120` |
| Fill | `varCardWhite` | `varCardWhite` |
| BorderColor | `varBorderLight` | `varBorderLight` |
| BorderThickness | `1` | `1` |
| BorderRadius | `8` ✓ | ❌ 不支援 |

**Section 標題**：

```
lblS2_Title:
├── Text: "Responsibility"
├── Color: varTextBase
├── Size: 16
├── Font: Font.'Segoe UI Semibold'
```

**系統架構師（自動帶入，非 Flow-Only）**：

> ⚠️ **v1.1 修正**：gov_systemarchitect 為 Lookup (User table)，非 Flow-Only 欄位。
> 必須使用 User 記錄（varCurrentUser），而非 email 字串（varCurrentUserEmail）。

```
lblS2_ArchitectLabel:
├── 名稱: lblS2_ArchitectLabel
├── Text: "System Architect"                           // 無 (System-controlled) 後綴
├── Color: varTextBase
├── Size: 13

lblS2_ArchitectValue:
├── 名稱: lblS2_ArchitectValue
├── Text: varCurrentUserName                           // 顯示用：人類可讀名稱
├── Fill: varNeutralLighter                            // 非 Flow-Only，使用較淺背景
├── BorderColor: varBorderLight
├── BorderThickness: 1
├── BorderRadius: 4
├── Color: varTextBase                                 // 非 varTextSecondary
├── Height: 36
├── PaddingLeft: 12
├── DisplayMode: DisplayMode.View                      // 自動帶入，不可編輯

提交時資料綁定：
├── 欄位：SystemArchitect
├── 值：varCurrentUser                                 // User 記錄，非 email 字串
├── ⚠️ 禁止使用：varCurrentUserEmail（會導致 Lookup 失敗）
```

**SA 欄位語義說明**：

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  System Architect 欄位設計原理                                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  資料模型（Dataverse）：                                                     │
│  ├── Schema Name: gov_systemarchitect                                       │
│  ├── Data Type: Lookup (User table)                                         │
│  ├── Flow-Only: No ← 這不是 Flow-Only 欄位                                  │
│  └── Required: Yes                                                          │
│                                                                             │
│  表單行為：                                                                  │
│  ├── 自動帶入登入者（varCurrentUser）                                        │
│  ├── 使用者不可修改（DisplayMode.View）                                     │
│  └── 若需變更 SA，須使用 SA Handover 流程（見下方）                          │
│                                                                             │
│  常見誤解：                                                                  │
│  ├── ❌「自動帶入」不等於「Flow-Only」                                       │
│  ├── ❌ email 字串（varCurrentUserEmail）不等於 User 記錄                   │
│  └── ✓ Lookup 欄位必須傳送 User 記錄（varCurrentUser）                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### Step 7：建立 Section 3 - Details

**操作路徑**：同 Step 5（Container 或 Rectangle）

**控制項設定（容器）**：

| 屬性 | Modern Container | Classic Rectangle |
|:----|:----------------|:-----------------|
| 名稱 | `cntSection3` | `rectSection3` |
| X | `varSpacingLG` | `varSpacingLG` |
| Y | `cntSection2.Y + cntSection2.Height + varSpacingMD` | `rectSection2.Y + rectSection2.Height + varSpacingMD` |
| Width | `Parent.Width - varSpacingLG * 2` | `Parent.Width - varSpacingLG * 2` |
| Height | `360` | `360` |
| Fill | `varCardWhite` | `varCardWhite` |
| BorderColor | `varBorderLight` | `varBorderLight` |
| BorderThickness | `1` | `1` |
| BorderRadius | `8` ✓ | ❌ 不支援 |

**Section 標題**：

```
lblS3_Title:
├── Text: "Details"
├── Color: varTextBase
├── Size: 16
├── Font: Font.'Segoe UI Semibold'
```

**專案名稱**：

```
lblS3_TitleLabel:
├── 名稱: lblS3_TitleLabel
├── Text: "專案名稱 *"
├── X: rectSection3.X + varSpacingMD
├── Y: lblS3_Title.Y + lblS3_Title.Height + varSpacingMD
├── Color: varTextBase
├── Size: 13

txtS3_Title:
├── 名稱: txtS3_Title
├── X: lblS3_TitleLabel.X
├── Y: lblS3_TitleLabel.Y + lblS3_TitleLabel.Height + varSpacingXS
├── Width: 400
├── Height: 40
├── Default: ""
├── HintText: "輸入專案名稱（必填）"
├── MaxLength: 255
├── BorderColor: varBorderLight
├── FocusBorderColor: varBrandAccent
```

**專案類型**：

```
lblS3_ProjectTypeLabel:
├── Text: "專案類型 *"
├── Y: txtS3_Title.Y + txtS3_Title.Height + varSpacingMD

ddS3_ProjectType:
├── 名稱: ddS3_ProjectType
├── Items: ["NewSystem", "MajorArchChange", "SecurityCritical", "ComplianceChange"]
├── Width: 300
├── BorderColor: varBorderLight
├── FocusBorderColor: varBrandAccent
```

**專案經理**：

```
lblS3_ProjectManagerLabel:
├── Text: "專案經理 *"

cmbS3_ProjectManager:
├── 名稱: cmbS3_ProjectManager
├── Items: Office365Users.SearchUser({searchTerm: Self.SearchText, top: 15})
├── DisplayFields: ["DisplayName", "Mail"]
├── SearchFields: ["DisplayName", "Mail"]
├── SelectMultiple: false
├── Width: 400
├── BorderColor: varBorderLight
├── FocusBorderColor: varBrandAccent
```

**目標安全等級**：

```
lblS3_TargetSLLabel:
├── Text: "目標安全等級 *"

ddS3_TargetSL:
├── 名稱: ddS3_TargetSL
├── Items: ["SL1", "SL2", "SL3", "SL4"]
├── Width: 200
```

**專案說明**：

```
lblS3_DescriptionLabel:
├── Text: "專案說明"

txtS3_Description:
├── 名稱: txtS3_Description
├── Mode: TextMode.MultiLine
├── Width: 400
├── Height: 100
├── Default: ""
├── HintText: "輸入專案說明（選填）"
├── MaxLength: 2000
```

---

### Step 8：建立 Footer

**操作路徑**：插入 → 圖形 → 矩形

**控制項設定**：

| 屬性 | 值 |
|:----|:--|
| 名稱 | `rectFooter` |
| X | `0` |
| Y | `Parent.Height - varFooterHeight` |
| Width | `Parent.Width` |
| Height | `varFooterHeight` |
| Fill | `varCardWhite` |

**Cancel 按鈕（左側）**：

```
btnCancel:
├── 名稱: btnCancel
├── Text: "取消"
├── X: varSpacingLG
├── Y: rectFooter.Y + (varFooterHeight - 40) / 2
├── Width: 100
├── Height: 40
├── Fill: Transparent
├── Color: varTextSecondary
├── HoverFill: varNeutralLighter
├── BorderThickness: 0
├── BorderRadius: 4
├── Font: Font.'Segoe UI'
├── OnSelect: Back()
```

**Submit 按鈕（右側）**：

```
btnSubmit:
├── 名稱: btnSubmit
├── Text: "提交"
├── X: Parent.Width - Self.Width - varSpacingLG
├── Y: rectFooter.Y + (varFooterHeight - 40) / 2
├── Width: 120
├── Height: 40
├── Fill: If(Self.DisplayMode = DisplayMode.Edit, varBrandPrimary, varNeutralLight)
├── Color: If(Self.DisplayMode = DisplayMode.Edit, varTextOnPrimary, varTextDisabled)
├── HoverFill: varBrandPrimaryHover
├── PressedFill: varBrandPrimaryPressed
├── BorderRadius: 4
├── Font: Font.'Segoe UI Semibold'
├── Size: 14
```

---

### Step 9：設定 DisplayMode

**btnSubmit.DisplayMode**：

```
If(
    And(
        !IsBlank(txtS3_Title.Text),
        Len(txtS3_Title.Text) >= 1,
        Len(txtS3_Title.Text) <= 255,
        !IsBlank(cmbS3_ProjectManager.Selected),
        !IsBlank(ddS3_ProjectType.Selected),
        !IsBlank(ddS3_TargetSL.Selected),
        !varIsLoading
    ),
    DisplayMode.Edit,
    DisplayMode.Disabled
)
```

---

### Step 10：建立 Message Area

**成功訊息（位於 Y=80）**：

```
rectMessageSuccess:
├── 名稱: rectMessageSuccess
├── Fill: varSuccessLight
├── X: 0
├── Y: varHeaderHeight
├── Width: Parent.Width
├── Height: varMessageHeight
├── Visible: varShowSuccess

icoMessageSuccess:
├── Icon: Icon.CheckMark
├── Color: varSuccess
├── X: varSpacingLG
├── Width: 24
├── Height: 24
├── Visible: varShowSuccess

lblMessageSuccessTitle:
├── Text: "操作成功"
├── Color: varSuccess
├── Font: Font.'Segoe UI Semibold'
├── Size: 14
├── Visible: varShowSuccess

lblMessageSuccessText:
├── Text: varSuccessMessage
├── Color: varTextBase
├── Size: 13
├── Visible: varShowSuccess

icoCloseSuccess:
├── Icon: Icon.Cancel
├── Color: varTextSecondary
├── X: Parent.Width - 40
├── OnSelect: Set(varShowSuccess, false)
├── Visible: varShowSuccess
```

**錯誤訊息**：

```
rectMessageError:
├── Fill: varDangerLight
├── Visible: varShowError

icoMessageError:
├── Icon: Icon.Warning
├── Color: varDanger
├── Visible: varShowError

lblMessageErrorTitle:
├── Text: "操作失敗"
├── Color: varDanger
├── Visible: varShowError

lblMessageErrorText:
├── Text: varErrorMessage
├── Visible: varShowError

icoCloseError:
├── OnSelect: Set(varShowError, false)
├── Visible: varShowError
```

---

### Step 11：設定 btnSubmit.OnSelect

**暫時版本（測試用）**：

```
Set(varIsLoading, true);
Set(varShowError, false);
Set(varShowSuccess, false);

// 模擬處理
Set(varIsLoading, false);
Set(varShowSuccess, true);
Set(varSuccessMessage,
    "【測試模式】" & Char(10) &
    "專案名稱: " & txtS3_Title.Text
)
```

**正式版本（待第 05 章完成後使用）**：

```
Set(varIsLoading, true);
Set(varShowError, false);
Set(varShowSuccess, false);

// v1.1 修正：SystemArchitect 為 Lookup (User)，需傳送 User 記錄
Set(
    varResult,
    'GOV-001-CreateProject'.Run(
        txtS3_Title.Text,
        varCurrentUser,                                // ✓ User 記錄（非 email 字串）
        cmbS3_ProjectManager.Selected.Mail,            // PM 仍使用 email（Flow 內部處理 Lookup）
        ddS3_ProjectType.Selected.Value,
        ddS3_TargetSL.Selected.Value,
        txtS3_Description.Text
    )
);

Set(varIsLoading, false);

If(
    varResult.Status = "Success",
    Set(varShowSuccess, true);
    Set(varSuccessMessage,
        "專案建立成功" & Char(10) &
        "Request ID: " & varResult.RequestID
    );
    Reset(txtS3_Title);
    Reset(cmbS3_ProjectManager);
    Reset(txtS3_Description),

    Set(varShowError, true);
    Set(varErrorCode, varResult.ErrorCode);
    Set(varErrorMessage, varResult.Message)
)
```

---

### Step 12：調整控制項層級順序

**正確順序（從上到下）**：

```
scrCreateProject
├── rectMessageSuccess    ← 最上層（訊息覆蓋）
├── icoMessageSuccess
├── lblMessageSuccessTitle
├── lblMessageSuccessText
├── icoCloseSuccess
├── rectMessageError
├── icoMessageError
├── lblMessageErrorTitle
├── lblMessageErrorText
├── icoCloseError
├── rectHeader            ← 結構層
├── lblHeaderTitle
├── lblHeaderUserName
├── rectBody
├── rectSection1
├── lblS1_Title
├── lblS1_NewProjectHint
├── rectSection2
├── lblS2_Title
├── lblS2_ArchitectLabel
├── lblS2_ArchitectValue
├── rectSection3
├── lblS3_Title
├── ... (所有 Section 3 控制項)
├── rectFooter
├── btnCancel
└── btnSubmit
```

---

### FORM-001 UX 驗證 Checklist

**結構驗證**：

- [ ] Header 高度 = 80px
- [ ] Header 背景 = varBrandPrimary (#0C3467)
- [ ] Body 包含三個 Section
- [ ] Footer 高度 = 72px
- [ ] Cancel 按鈕在左側
- [ ] Submit 按鈕在右側
- [ ] Message Area 在 Y=80

**色彩驗證**：

- [ ] 所有色彩使用變數（無硬編碼）
- [ ] Header 使用 varBrandPrimary
- [ ] Section 背景使用 varCardWhite
- [ ] Flow-Only 欄位使用 varFlowOnlyBg
- [ ] Submit 按鈕使用 varBrandPrimary

**控制項驗證**：

- [ ] 所有控制項已重命名
- [ ] Flow-Only 欄位使用 Label
- [ ] Flow-Only 欄位有 "(System-controlled)" 標註
- [ ] DisplayMode 公式正確

---

## FORM-002：Gate 申請表單

### 表單概述

| 項目 | 內容 |
|:----|:----|
| **對應 Flow** | GOV-002-GateTransitionRequest |
| **使用角色** | System Architect |
| **Gate Stepper** | 顯示 |

### 結構說明

**Section 1: Basic Information**

| 欄位 | 控制項類型 | Flow-Only |
|:----|:---------|:---------:|
| Request ID | Label | ✓ |
| Project Title | Label | ✓ |
| Current Gate | Label + Badge | ✓ |

**Section 2: Responsibility**

| 欄位 | 控制項類型 | Flow-Only | 備註 |
|:----|:---------|:---------:|:----|
| System Architect | Label | ❌ | v1.1 修正：Lookup 欄位，非 Flow-Only |
| Request Status | Badge | ✓ | |

**Section 3: Details**

| 欄位 | 控制項類型 | 說明 |
|:----|:---------|:----|
| 專案選擇器 | ComboBox | cmbS3_Project |
| 申請 Gate | Dropdown | ddS3_RequestedGate |
| 備註 | Text input | txtS3_Comments |
| SL 決策層級 | Dropdown | ddS3_SLDecisionLevel — Choice：SL1/SL2/SL3/SL4（僅當 Gate 涉及 SL 判定時顯示） |
| SL 判定備註 | Text input | txtS3_SLApprovedNote — Multiline Text(2000)，選填（僅當 SL 決策層級已選擇時顯示） |
| Rework 原因分類 | Dropdown | ddS3_ReworkReasonCategory — Choice：RequirementClarificationDeficiency/DesignError/CustomerRequirementChange/Other（僅當 Rework 觸發時顯示） |

> **Visible 公式參考**：
> - `ddS3_SLDecisionLevel.Visible`：`ddS3_RequestedGate.Selected.Value = "Gate1" || ddS3_RequestedGate.Selected.Value = "Gate3"`
> - `txtS3_SLApprovedNote.Visible`：`!IsBlank(ddS3_SLDecisionLevel.Selected)`
> - `ddS3_ReworkReasonCategory.Visible`：`varFlowResult.Status = "Rework"`

### 專案選擇器公式

```
cmbS3_Project.Items:
// v1.1 修正：gov_systemarchitect 為 Lookup (User)，需使用 User 記錄比對
Filter(
    gov_projectregistry,
    gov_projectstatus = "Active" And
    gov_systemarchitect.'Primary Email' = varCurrentUserEmail And    // Lookup 展開比對
    gov_requeststatus = "None"
)

// 或使用 GUID 比對（更可靠）：
// gov_systemarchitect.User = varCurrentUser.User
```

> **實作提醒**：Dataverse Choice 欄位在 PowerFx 中應使用 Enum 語法（如 `ThisRecord.gov_projectstatus = gov_projectstatus.Active`）或 `.Value` 屬性進行比較，避免直接使用字串比較。

### Gate 選項公式

```
ddS3_RequestedGate.Items:
Switch(
    cmbS3_Project.Selected.gov_currentgate,
    "Pending", ["Gate0"],
    "Gate0", ["Gate1"],
    "Gate1", ["Gate2"],
    "Gate2", ["Gate3"],
    []
)
```

### PowerFx Submit

```
'GOV-002-GateTransitionRequest'.Run(
    cmbS3_Project.Selected.gov_projectregistryid,
    ddS3_RequestedGate.Selected.Value,
    txtS3_Comments.Text,
    If(!IsBlank(ddS3_SLDecisionLevel.Selected), Text(ddS3_SLDecisionLevel.Selected.Value), ""),
    txtS3_SLApprovedNote.Text,
    If(!IsBlank(ddS3_ReworkReasonCategory.Selected), Text(ddS3_ReworkReasonCategory.Selected.Value), ""),
    varCurrentUserEmail
)
```

### FORM-002 UX Checklist

- [ ] Gate Stepper 顯示（Visible: true）
- [ ] 專案選擇後自動顯示 Current Gate
- [ ] Gate 選項依 Current Gate 動態過濾
- [ ] Footer Button 排列正確

---

## FORM-003：文件上傳表單

### 表單概述

| 項目 | 內容 |
|:----|:----|
| **對應 Flow** | GOV-005-DocumentIntake |
| **使用角色** | System Architect |
| **Gate Stepper** | 顯示 |

### Section 3: Details 欄位

| 欄位 | 控制項 | 說明 |
|:----|:------|:----|
| 專案選擇器 | cmbS3_Project | ComboBox — 篩選 ProjectStatus = Active |
| 文件類型 | ddS3_DocumentType | Dropdown — 選項來源見下方 |
| 文件名稱 | txtS3_DocumentName | Text input |
| 版本號 | txtS3_DocumentVersion | Text input — 格式 v1.0 |
| 檔案上傳 | attS3_FileUpload | Attachment — 使用者選擇檔案（Base64 傳至 Flow） |
| 交付物層級 | ddS3_DeliverablePackage | Dropdown — CoreDeliverable / SupplementaryDeliverable / AdHoc |
| 備註 | txtS3_Comments | Text input (MultiLine) |

> **重要變更（v7.3）**：`txtS3_SharePointLink` 已移除。使用者不再需要手動貼上 SharePoint 連結。
> 改為 `attS3_FileUpload`（Attachment 控制項），檔案以 Base64 傳遞至 GOV-005 Flow，由 Flow 上傳至 SharePoint 並自動回寫 URL。

### 檔案上傳控制項設定

```
attS3_FileUpload 設定：
────────────────────
MaxAttachments: 1
MaxAttachmentSize: 52428800  // 50 MB

提交時傳遞至 Flow 的 JSON：
{
    "FileName": First(attS3_FileUpload.Attachments).Name,
    "FileContent": First(attS3_FileUpload.Attachments).Value,  // Base64
    "ParentProjectId": cmbS3_Project.Selected.gov_projectregistryid,
    "DocumentType": ddS3_DocumentType.Selected.Value,
    "DocumentName": txtS3_DocumentName.Text,
    "DocumentVersion": txtS3_DocumentVersion.Text,
    "DeliverablePackage": ddS3_DeliverablePackage.Selected.Value,
    "Comments": txtS3_Comments.Text
}
```

### 文件類型選項

```
ddS3_DocumentType.Items:
["TechnicalFeasibility", "InitialRiskList", "RiskAssessmentStrategy", "DesignBaseline", "RiskAssessment", "IEC62443Checklist", "ThreatModel", "RequirementTraceability", "DocumentRegister", "DesignObjectInventory", "ChangeImpact", "TestPlan", "TestReport", "HandoverMeeting", "ResidualRiskList", "Other"]
```

### 交付物層級選項

```
ddS3_DeliverablePackage.Items:
["CoreDeliverable", "SupplementaryDeliverable", "AdHoc"]

ddS3_DeliverablePackage.Default: "CoreDeliverable"
```

### 版本格式驗證

```
lblS3_VersionError.Visible:
And(
    !IsBlank(txtS3_DocumentVersion.Text),
    !IsMatch(txtS3_DocumentVersion.Text, "^v\d+\.\d+$")
)

lblS3_VersionError.Text: "版本格式應為 v1.0"
lblS3_VersionError.Color: varDanger
```

---

## FORM-004 至 FORM-011 規格

### 共用結構

所有表單遵循相同五區塊配置 + 三 Section 資訊分類。

| 表單 | 對應 Flow | Gate Stepper |
|:----|:---------|:------------:|
| FORM-004 | GOV-004-RiskItemCreate | 顯示 |
| FORM-005 | GOV-020-DocumentInventoryParser | 顯示 |
| FORM-006 | GOV-006-GateCancellation | 顯示 |
| FORM-007 | GOV-007-LiteUpgrade | 顯示 |
| FORM-008 | GOV-008-DocumentUnfreeze | 顯示 |
| FORM-009 | GOV-009-ProjectClosure | 顯示 |
| FORM-010 | GOV-010-ProjectSuspension | 顯示 |
| FORM-011 | GOV-011-EmergencyDocument | 顯示 |
| FORM-012 | GOV-022-StandardFeedbackHandler | 隱藏 |
| FORM-013 | GOV-023-DisputeHandler | 隱藏 |
| FORM-014 | GOV-024-ActionItemTracker | 顯示 |
| FORM-015 | （Dataverse Direct Submit） | 隱藏 |
| FORM-016 | （Dataverse Direct Submit） | 隱藏 |

### 每個表單必須包含

1. **Header**：varBrandPrimary 背景、表單標題、使用者名稱
2. **Gate Stepper**：顯示專案進度（若適用）
3. **Section 1**：Basic Information（Flow-Only 欄位）
4. **Section 2**：Responsibility（Flow-Only 欄位）
5. **Section 3**：Details（使用者輸入欄位）
6. **Footer**：Cancel 左側、Submit 右側
7. **Message Area**：固定於 Y=80

---

## Flow 連接設定（待第 05 章完成）

**操作路徑**：

```
1. 左側面板 → ⚡ Power Automate
2. + Add flow
3. 選擇目標 Flow
4. 完成連接
```

**連接清單**：

| Flow 名稱 | 對應表單 |
|:---------|:-------|
| GOV-001-CreateProject | FORM-001 |
| GOV-002-GateTransitionRequest | FORM-002 |
| GOV-004-RiskItemCreate | FORM-004 |
| GOV-005-DocumentIntake | FORM-003 |
| GOV-006-GateCancellation | FORM-006 |
| GOV-020-DocumentInventoryParser | FORM-005 |
| GOV-007-LiteUpgrade | FORM-007 |
| GOV-008-DocumentUnfreeze | FORM-008 |
| GOV-009-ProjectClosure | FORM-009 |
| GOV-010-ProjectSuspension | FORM-010 |
| GOV-011-EmergencyDocument | FORM-011 |
| GOV-022-StandardFeedbackHandler | FORM-012 |
| GOV-023-DisputeHandler | FORM-013 |
| GOV-024-ActionItemTracker | FORM-014 |
| GOV-001B-SAHandover | FORM-001B |
| （Dataverse Direct Submit） | FORM-015 |
| （Dataverse Direct Submit） | FORM-016 |

---

## 全域 UX 驗證 Checklist

### 品牌一致性

- [ ] 所有表單 Header 使用 varBrandPrimary
- [ ] 所有表單 Submit 按鈕使用 varBrandPrimary
- [ ] 所有表單 Focus 邊框使用 varBrandAccent
- [ ] 無硬編碼色碼

### 結構一致性

- [ ] 所有表單採用五區塊配置
- [ ] 所有表單 Body 分三個 Section
- [ ] 所有表單 Cancel 在左、Submit 在右
- [ ] 所有表單 Message 固定於 Y=80

### Flow-Only 一致性

- [ ] 所有 Flow-Only 欄位使用 Label
- [ ] 所有 Flow-Only 欄位背景 varFlowOnlyBg
- [ ] 所有 Flow-Only 欄位標註 "(System-controlled)"

### 治理一致性

- [ ] 無 SubmitForm() 直接寫入
- [ ] 無 Patch() 直接寫入
  - （FORM-015、FORM-016 除外：Reference 類型資料表由 Governance Lead 透過 Patch() 直接寫入）
- [ ] 無硬編碼 Flow URL
- [ ] 所有提交透過 Flow

---

## System Architect Handover 規格（v1.1 新增）

### 設計原理

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  SA Handover 設計原理                                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  問題背景：                                                                  │
│  ├── System Architect 在專案建立時自動帶入（建立者本人）                     │
│  ├── 專案生命週期中，SA 可能需要變更（離職、調動、專案移交）                  │
│  └── 直接修改 Lookup 欄位會繞過治理追溯                                      │
│                                                                             │
│  設計原則：                                                                  │
│  ├── SA 變更必須透過 Flow（GOV-001B-SAHandover）                            │
│  ├── 所有變更必須記錄於 Event Log（Append-Only）                            │
│  ├── 新 SA 必須明確接受移交（Acceptance Confirmation）                      │
│  └── Presales 階段專案須保留原始記錄（不可覆寫）                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### GOV-001B-SAHandover Flow 規格

| 項目 | 內容 |
|:----|:----|
| Flow Name | GOV-001B-SAHandover |
| 觸發方式 | Power Apps 呼叫 |
| 執行身份 | Flow Service Principal |
| 權限要求 | 僅原 SA 或 Governance Lead 可發起 |

**輸入參數**：

| 參數 | 型別 | 說明 |
|:----|:-----|:----|
| ProjectID | Text | 專案 RequestID |
| NewSystemArchitect | User | 新 SA（Lookup User） |
| HandoverReason | Text | 移交原因 |
| RequestedBy | User | 發起人（Lookup User） |

**處理邏輯**：

```
1. 驗證發起人權限
   ├── 原 SA（gov_systemarchitect = RequestedBy）
   └── 或 Governance Lead 角色

2. 建立 SA Handover Event 記錄（Append-Only）
   ├── EventType: "SAHandover"
   ├── OriginalSA: 原 gov_systemarchitect
   ├── NewSA: NewSystemArchitect
   ├── HandoverReason: HandoverReason
   ├── RequestedBy: RequestedBy
   ├── RequestedDate: utcNow()
   └── Status: "PendingAcceptance"

3. 發送通知給新 SA
   └── 要求確認接受移交

4. 新 SA 確認後
   ├── 更新 gov_systemarchitect = NewSA
   ├── 更新 Event 記錄 Status = "Completed"
   └── 記錄 AcceptedDate = utcNow()
```

### FORM-001B：SA Handover 表單

| 項目 | 內容 |
|:----|:----|
| 對應 Flow | GOV-001B-SAHandover |
| 使用角色 | System Architect / Governance Lead |
| Gate Stepper | 顯示 |

**Section 3: Handover Details**

| 欄位 | 控制項類型 | 說明 |
|:----|:---------|:----|
| 專案選擇器 | ComboBox | cmbS3_Project |
| 新系統架構師 | ComboBox | cmbS3_NewArchitect（搜尋 User） |
| 移交原因 | Dropdown | ddS3_HandoverReason |
| 備註 | Text input | txtS3_Comments |

**移交原因選項**：

```
ddS3_HandoverReason.Items:
["Resignation", "RoleChange", "ProjectTransfer", "WorkloadBalance", "Other"]
```

### Presales 專案保護規則

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Presales 專案特殊處理                                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  當 ProjectType = "Presales" 時：                                           │
│  ├── 原始 SA 記錄必須保留於 Event Log                                        │
│  ├── Handover 不可刪除歷史記錄                                              │
│  ├── 所有 SA 變更皆為 Append-Only                                           │
│  └── Presales 轉正式專案時，SA 歷史完整保留                                  │
│                                                                             │
│  資料模型（gov_sahandoverevent）：                                           │
│  ├── EventID (PK, Flow-Only)                                                │
│  ├── ParentProject (Lookup gov_projectregistry, Flow-Only)                  │
│  ├── OriginalSA (Lookup User, Flow-Only)                                    │
│  ├── NewSA (Lookup User, Flow-Only)                                         │
│  ├── HandoverReason (Choice, Flow-Only)                                     │
│  ├── RequestedBy (Lookup User, Flow-Only)                                   │
│  ├── RequestedDate (DateTime, Flow-Only)                                    │
│  ├── AcceptedDate (DateTime, Flow-Only)                                     │
│  └── Status (Choice: PendingAcceptance/Completed/Rejected, Flow-Only)       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## FORM-012：標準回饋表單

### 表單概述

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| **對應 Flow** | GOV-022-StandardFeedbackHandler |
| **使用角色** | System Architect, Project Manager, Reviewers |
| **對應畫面** | scrStandardFeedback |
| **Gate Stepper** | 隱藏（非 Gate 事件） |
| **品牌標準** | appendix/Canvas-Brand-UI-Standard-v1.2.md |

### 畫面欄位定義

| 欄位 | 控制項 | Schema Field | Data Type |
|:------------------------------|:------------------------------|:------------------------------|:----------------------------------------------|
| 回饋 ID | lblS1_FeedbackID | gov_feedbackid | Text（Flow-only，提交後顯示） |
| 提報人 | lblS1_ReportedBy | gov_reportedby | Lookup User（系統自動填入） |
| 提報日期 | lblS1_ReportedDate | gov_reporteddate | DateTime（系統自動填入） |
| 處理狀態 | lblS1_ResolutionStatus | gov_feedbackresolutionstatus | Choice（系統自動填入 Open） |
| 標準 ID | txtS3_StandardID | gov_standardid | Text(100)，必填 |
| 回饋類型 | ddS3_FeedbackType | gov_feedbacktype | Choice：CannotExecute / Conflict / Improvement |
| 回饋說明 | txtS3_Description | gov_description | Multiline Text(4000)，必填 |
| 相關標準名稱 | txtS3_RelatedStandard | gov_relatedstandard | Text(200)，選填 |
| 相關專案 | cmbS3_RelatedProject | gov_parentproject | Lookup (gov_projectregistry)，選填 |

### PowerFx Submit

```
'GOV-022-StandardFeedbackHandler'.Run(
    ddS3_FeedbackType.Selected.Value,
    txtS3_StandardID.Text,
    txtS3_Description.Text,
    txtS3_RelatedStandard.Text,
    If(!IsBlank(cmbS3_RelatedProject.Selected), cmbS3_RelatedProject.Selected.gov_projectregistryid, ""),
    varCurrentUserEmail
)
```

### 驗證規則

| 規則 | 條件 | 訊息 |
|:------------------------------|:----------------------------------------------|:----------------------------------------------|
| 標準 ID 必填 | IsBlank(txtS3_StandardID.Text) | 「請輸入標準 ID」 |
| 回饋類型必填 | IsBlank(ddS3_FeedbackType.Selected) | 「請選擇回饋類型」 |
| 說明必填 | IsBlank(txtS3_Description.Text) | 「請輸入回饋說明」 |

---

## FORM-013：爭議提報表單

### 表單概述

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| **對應 Flow** | GOV-023-DisputeHandler |
| **使用角色** | All governance roles |
| **對應畫面** | scrDisputeFiling |
| **Gate Stepper** | 隱藏（非 Gate 事件） |
| **品牌標準** | appendix/Canvas-Brand-UI-Standard-v1.2.md |

### 畫面欄位定義

| 欄位 | 控制項 | Schema Field | Data Type |
|:------------------------------|:------------------------------|:------------------------------|:----------------------------------------------|
| 爭議 ID | lblS1_DisputeID | gov_disputeid | Text（Flow-only，提交後顯示） |
| 提報人 | lblS1_RaisedBy | gov_raisedby | Lookup User（系統自動填入） |
| 提報日期 | lblS1_RaisedDate | gov_raiseddate | DateTime（系統自動填入） |
| 爭議層級 | ddS3_DisputeLevel | gov_disputelevel | Choice：Level2 / Level3，必填 |
| 爭議說明 | txtS3_Description | gov_description | Multiline Text(4000)，必填 |
| 相關專案 | cmbS3_RelatedProject | gov_parentproject | Lookup (gov_projectregistry)，必填 |

### PowerFx Submit

```
'GOV-023-DisputeHandler'.Run(
    ddS3_DisputeLevel.Selected.Value,
    txtS3_Description.Text,
    cmbS3_RelatedProject.Selected.gov_projectregistryid,
    varCurrentUserEmail
)
```

### 驗證規則

| 規則 | 條件 | 訊息 |
|:------------------------------|:----------------------------------------------|:----------------------------------------------|
| 爭議層級必填 | IsBlank(ddS3_DisputeLevel.Selected) | 「請選擇爭議層級」 |
| 說明必填 | IsBlank(txtS3_Description.Text) | 「請輸入爭議說明」 |
| 相關專案必填 | IsBlank(cmbS3_RelatedProject.Selected) | 「請選擇相關專案」 |

---

## FORM-014：行動項目表單

### 表單概述

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| **對應 Flow** | GOV-024-ActionItemTracker |
| **使用角色** | System Architect, Project Manager |
| **對應畫面** | scrActionItem |
| **Gate Stepper** | 顯示（與 Gate 審查關聯） |
| **品牌標準** | appendix/Canvas-Brand-UI-Standard-v1.2.md |

### 畫面欄位定義

| 欄位 | 控制項 | Schema Field | Data Type |
|:------------------------------|:------------------------------|:------------------------------|:----------------------------------------------|
| 行動項目 ID | lblS1_ActionItemID | gov_actionitemid | Text（Flow-only，提交後顯示） |
| 狀態 | lblS1_Status | gov_actionitemstatus | Choice（系統自動填入 Open） |
| 待辦描述 | txtS3_Description | gov_description | Multiline Text(4000)，必填 |
| 負責人 | cmbS3_AssignedTo | gov_assignedto | Lookup User，必填 |
| 截止日 | dpS3_DueDate | gov_duedate | Date，必填 |
| 相關專案 | cmbS3_RelatedProject | gov_parentproject | Lookup (gov_projectregistry)，自動帶入 |
| 相關 Gate 審查 | lblS3_RelatedGateReview | gov_relatedgatereview | Lookup (gov_reviewdecisionlog)，自動帶入 |

### PowerFx Submit

```
'GOV-024-ActionItemTracker'.Run(
    lblS3_RelatedGateReview.Text,
    txtS3_Description.Text,
    cmbS3_AssignedTo.Selected.Mail,
    Text(dpS3_DueDate.SelectedDate, "yyyy-MM-ddTHH:mm:ssZ"),
    cmbS3_RelatedProject.Selected.gov_projectregistryid,
    varCurrentUserEmail
)
```

### 驗證規則

| 規則 | 條件 | 訊息 |
|:------------------------------|:----------------------------------------------|:----------------------------------------------|
| 描述必填 | IsBlank(txtS3_Description.Text) | 「請輸入待辦描述」 |
| 負責人必填 | IsBlank(cmbS3_AssignedTo.Selected) | 「請選擇負責人」 |
| 截止日必填 | IsBlank(dpS3_DueDate.SelectedDate) | 「請選擇截止日」 |
| 截止日不可過去 | dpS3_DueDate.SelectedDate < Today() | 「截止日不可為過去日期」 |

---

## FORM-015：標準登錄冊表單

### 表單概述

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| **對應 Flow** | （手動輸入，無專屬 Flow） |
| **使用角色** | Governance Lead |
| **對應畫面** | scrStandardsRegistry |
| **Gate Stepper** | 隱藏（非 Gate 事件） |
| **品牌標準** | appendix/Canvas-Brand-UI-Standard-v1.2.md |

> **說明**：此表單透過 Dataverse Direct Submit（`SubmitForm()` 或 `Patch()`）直接寫入 `gov_standardsregistry`。因為此表為 Reference 類型且僅 Governance Lead 使用，不需 Flow 中介。

### 畫面欄位定義

| 欄位 | 控制項 | Schema Field | Data Type |
|:------------------------------|:------------------------------|:------------------------------|:----------------------------------------------|
| 標準 ID | txtS3_StandardID | gov_standardregistryid | Text(30)，必填 |
| 標準名稱 | txtS3_StandardName | gov_standardname | Text(200)，必填 |
| 文件分類 | ddS3_DocumentCategory | gov_documentcategory | Choice：Architecture / Security / QA / Governance |
| 擁有角色 | txtS3_OwnerRole | gov_ownerrole | Text(100)，必填 |
| 審查週期 | ddS3_ReviewCycle | gov_reviewcycle | Choice：Annual / SemiAnnual / Quarterly |
| 上次審查日 | dpS3_LastReviewDate | gov_lastreviewdate | Date，選填 |
| 下次審查日 | dpS3_NextReviewDate | gov_nextreviewdate | Date，選填 |
| 目前版本 | txtS3_CurrentVersion | gov_currentversion | Text(20)，選填 |
| 狀態 | ddS3_Status | gov_standardstatus | Choice：Active / UnderReview / Retired |
| SharePoint 連結 | txtS3_SharePointLink | gov_sharepointlink | URL(500)，選填 |

### PowerFx Submit

```
Patch(
    gov_standardsregistry,
    Defaults(gov_standardsregistry),
    {
        gov_standardregistryid: txtS3_StandardID.Text,
        gov_standardname: txtS3_StandardName.Text,
        gov_documentcategory: ddS3_DocumentCategory.Selected,
        gov_ownerrole: txtS3_OwnerRole.Text,
        gov_reviewcycle: ddS3_ReviewCycle.Selected,
        gov_lastreviewdate: dpS3_LastReviewDate.SelectedDate,
        gov_nextreviewdate: dpS3_NextReviewDate.SelectedDate,
        gov_currentversion: txtS3_CurrentVersion.Text,
        gov_standardstatus: ddS3_Status.Selected,
        gov_sharepointlink: txtS3_SharePointLink.Text
    }
)
```

### 驗證規則

| 規則 | 條件 | 訊息 |
|:------------------------------|:----------------------------------------------|:----------------------------------------------|
| 標準 ID 必填 | IsBlank(txtS3_StandardID.Text) | 「請輸入標準 ID」 |
| 標準名稱必填 | IsBlank(txtS3_StandardName.Text) | 「請輸入標準名稱」 |
| 擁有角色必填 | IsBlank(txtS3_OwnerRole.Text) | 「請輸入擁有角色」 |

---

## FORM-016：外部單位登錄表單

### 表單概述

| 項目 | 內容 |
|:------------------------------|:----------------------------------------------|
| **對應 Flow** | （手動輸入，無專屬 Flow） |
| **使用角色** | Governance Lead |
| **對應畫面** | scrExternalUnit |
| **Gate Stepper** | 隱藏（非 Gate 事件） |
| **品牌標準** | appendix/Canvas-Brand-UI-Standard-v1.2.md |

> **說明**：同 FORM-015，此表單透過 Dataverse Direct Submit 寫入 `gov_externalunit`。

### 畫面欄位定義

| 欄位 | 控制項 | Schema Field | Data Type |
|:------------------------------|:------------------------------|:------------------------------|:----------------------------------------------|
| 單位 ID | txtS3_UnitID | gov_externalunitid | Text(30)，必填 |
| 單位名稱 | txtS3_UnitName | gov_unitname | Text(200)，必填 |
| 介面類型 | ddS3_InterfaceType | gov_interfacetype | Choice：Upstream / Downstream / Peer / Regulatory |
| 評估狀態 | ddS3_AssessmentStatus | gov_assessmentstatus | Choice：NotAssessed / InProgress / Assessed / NeedsReassessment |
| 評估日期 | dpS3_AssessmentDate | gov_assessmentdate | Date，選填 |
| 評估人員 | cmbS3_Assessor | gov_assessor | Lookup User，選填 |
| 備註 | txtS3_Notes | gov_notes | Multiline Text(4000)，選填 |

### PowerFx Submit

```
Patch(
    gov_externalunit,
    Defaults(gov_externalunit),
    {
        gov_externalunitid: txtS3_UnitID.Text,
        gov_unitname: txtS3_UnitName.Text,
        gov_interfacetype: ddS3_InterfaceType.Selected,
        gov_assessmentstatus: ddS3_AssessmentStatus.Selected,
        gov_assessmentdate: dpS3_AssessmentDate.SelectedDate,
        gov_assessor: cmbS3_Assessor.Selected,
        gov_notes: txtS3_Notes.Text
    }
)
```

### 驗證規則

| 規則 | 條件 | 訊息 |
|:------------------------------|:----------------------------------------------|:----------------------------------------------|
| 單位 ID 必填 | IsBlank(txtS3_UnitID.Text) | 「請輸入單位 ID」 |
| 單位名稱必填 | IsBlank(txtS3_UnitName.Text) | 「請輸入單位名稱」 |

---

## 版本歷史

| 版本 | 日期 | 變更說明 |
|:----|:-----|:---------|
| v1.0 | 2026-01-29 | 初版建立 |
| v2.0 | 2026-02-08 | P0 修正 |
| v3.0 | 2026-02-11 | 傻瓜可執行版本 |
| v4.0 | 2026-02-11 | 重構為符合 Design Standard |
| v5.0 | 2026-02-11 | 套用 Canvas Brand UI Standard v1.0 |
| v6.0 | 2026-02-11 | 套用 Anti-Fragile v1.2 |
| v7.0 | 2026-02-11 | 可執行 SOP 修補：欄位分類矩陣、BorderRadius 替代方案、操作手冊整合 |
| v7.1 | 2026-02-11 | SA 欄位 v1.1 修正：修復 Lookup User 語義錯誤（varCurrentUserEmail → varCurrentUser）、新增 SA Handover 規格 |
| v7.2 | 2026-02-11 | 鑑識修訂：修正版本標頭（v6.0→v7.2）、消除 Flow ID 重複（FORM-005: GOV-006→GOV-020-DocumentInventoryParser） |
| v7.3 | 2026-02-11 | 日常流程修訂：(1) FORM-003 移除 txtS3_SharePointLink，新增 attS3_FileUpload（Base64 上傳）；(2) FORM-003 新增 ddS3_DeliverablePackage 下拉選單；(3) FORM-003 檔案上傳控制項完整 JSON Schema；(4) 文件類型選項新增 TestPlan/Other |
| v7.4 | 2026-03-05 | KPI 證據採集支援：新增 FORM-012（標準回饋）、FORM-013（爭議提報）、FORM-014（行動項目）、FORM-015（標準登錄冊）、FORM-016（外部單位登錄）；FORM-002 新增 SL Decision Level 及 Rework Reason Category 條件欄位 |

---

**文件結束**

**品牌標準依據**：[appendix/Canvas-Brand-UI-Standard-v1.2.md](appendix/Canvas-Brand-UI-Standard-v1.2.md)

**操作手冊參考**：[appendix/Canvas-Editor-Operability-Playbook-v1.md](appendix/Canvas-Editor-Operability-Playbook-v1.md)

**下一步**：通過 UX 驗證 Checklist 後，請繼續參閱 [05-core-flows-implementation-runbook.md](05-core-flows-implementation-runbook.md)
