# Canvas Brand UX 升級報告

## 04-Canvas-Brand-UX-Patch-Report

**報告類型**：Canvas UI/UX Brand Upgrade Report
**報告日期**：2026-02-11
**升級對象**：04-powerapps-forms.md 及所有 FORM-xxx
**升級版本**：v4.0 → v5.0
**品牌標準**：Canvas-Brand-UI-Standard-v1.md

---

## 執行摘要

| 項目 | 結果 |
|------|------|
| **套用品牌標準** | ✅ 完成 |
| **升級表單數量** | 11 個（FORM-001 至 FORM-011） |
| **新增文件** | 1 個（appendix/Canvas-Brand-UI-Standard-v1.md） |
| **治理核心影響** | ❌ 無影響 |
| **Dataverse 變更** | ❌ 無變更 |
| **Flow 變更** | ❌ 無變更 |

---

## A. 套用標準的表單清單

### 完整套用品牌標準

| 表單 | 對應 Flow | 結構合規 | 色彩合規 | Flow-Only 合規 |
|------|----------|:--------:|:--------:|:-------------:|
| FORM-001 | GOV-001-CreateProject | ✅ | ✅ | ✅ |
| FORM-002 | GOV-002-GateTransitionRequest | ✅ | ✅ | ✅ |
| FORM-003 | GOV-005-DocumentIntake | ✅ | ✅ | ✅ |
| FORM-004 | GOV-004-RiskItemCreate | ✅ | ✅ | ✅ |
| FORM-005 | GOV-006-RiskReassessment | ✅ | ✅ | ✅ |
| FORM-006 | GOV-006-GateCancellation | ✅ | ✅ | ✅ |
| FORM-007 | GOV-007-LiteUpgrade | ✅ | ✅ | ✅ |
| FORM-008 | GOV-008-DocumentUnfreeze | ✅ | ✅ | ✅ |
| FORM-009 | GOV-009-ProjectClosure | ✅ | ✅ | ✅ |
| FORM-010 | GOV-010-ProjectSuspension | ✅ | ✅ | ✅ |
| FORM-011 | GOV-011-EmergencyDocument | ✅ | ✅ | ✅ |

---

## B. 具體優化項目

### 1. 品牌色彩系統

| 優化項目 | 變更前 | 變更後 |
|---------|--------|--------|
| Header 背景 | #0078D4（通用藍） | #0C3467（品牌主色） |
| Primary Button | #0078D4 | #0C3467 |
| Focus 邊框 | 無定義 | #008EC3（品牌強調色） |
| 內文主色 | #323130 | #2D2D2D（Text Base） |
| Danger 色 | #D13438 | #A4262C（品牌 Danger） |

### 2. 結構統一化

| 優化項目 | 變更說明 |
|---------|---------|
| Header 高度 | 統一為 80px |
| Gate Stepper 高度 | 統一為 50px |
| Footer 高度 | 統一為 72px |
| Message Area 位置 | 固定於 Y=80（Header 下方） |
| Section 數量 | 統一為三個（Basic Info / Responsibility / Details） |

### 3. 控制項命名規範

| 優化項目 | 變更說明 |
|---------|---------|
| Section 控制項前綴 | 新增 lblS1_, lblS2_, lblS3_, txtS3_, ddS3_ 等 |
| 容器命名 | rectHeader, rectSection1, rectSection2, rectSection3, rectFooter |
| Message 命名 | rectMessageSuccess, rectMessageError, icoMessage*, lblMessage* |

### 4. Flow-Only 欄位視覺規範

| 優化項目 | 變更說明 |
|---------|---------|
| 背景色 | varFlowOnlyBg (#EFEFEF) |
| 標籤後綴 | 新增 "(System-controlled)" 標註 |
| 控制項類型 | 強制使用 Label（非 Text input） |
| 文字色 | varTextSecondary (#666666) |

### 5. Button 排列規範

| 優化項目 | 變更說明 |
|---------|---------|
| Cancel 位置 | 固定於 Footer 左側 |
| Submit 位置 | 固定於 Footer 右側 |
| Button 間距 | 使用 varSpacing* 變數 |
| Ghost Button 樣式 | 透明背景、varTextSecondary 文字 |

### 6. App.OnStart 升級

| 優化項目 | 變更說明 |
|---------|---------|
| 色彩變數 | 升級為品牌色彩系統（varBrand*, varNeutral*, varText*, varDanger, varSuccess, varWarning） |
| 間距變數 | 新增 varSpacingXXS, varSpacingXS, varSpacingSM, varSpacingMD, varSpacingLG, varSpacingXL |
| 高度常數 | 新增 varHeaderHeight, varGateStepperHeight, varFooterHeight, varMessageHeight |

### 7. UX 驗證 Checklist

| 優化項目 | 變更說明 |
|---------|---------|
| FORM-001 | 新增 15 項驗證檢查點 |
| FORM-002 | 新增 4 項驗證檢查點 |
| 全域 | 新增 16 項全域驗證檢查點 |

### 8. Gate Stepper 視覺規範

| 優化項目 | 變更說明 |
|---------|---------|
| 已完成 Gate | varBrandPrimary, Opacity 0.6 |
| 目前 Gate | varBrandPrimary, 放大 1.2x |
| 未達 Gate | varNeutralGray, Opacity 0.4 |
| 連接線 | 已完成區段使用品牌色，未達區段使用灰色 |

### 9. Status Badge 規範

| Badge 類型 | Fill | 使用情境 |
|-----------|------|---------|
| Primary | varBrandPrimary | Active, 目前 Gate |
| Success | varSuccess | Closed, Approved |
| Danger | varDanger | Terminated, Rejected |
| Warning | varWarning | Pending, UnderReview |
| Neutral | varNeutralLight | None, Draft |

### 10. 訊息區塊規範

| 優化項目 | 變更說明 |
|---------|---------|
| 位置 | 固定於 Y=80（不使用浮動 Toast） |
| Success | varSuccessLight 背景 + varSuccess 圖示/標題 |
| Error | varDangerLight 背景 + varDanger 圖示/標題 |
| 關閉按鈕 | 固定於右側 |

---

## C. 治理核心保證

### 未變更項目確認

| 項目 | 狀態 | 說明 |
|------|:----:|------|
| Dataverse Entity 結構 | ❌ 未變更 | Schema 完全保留 |
| Dataverse 欄位定義 | ❌ 未變更 | 所有欄位、Choice、OptionSet 保留 |
| Gate 狀態機設計 | ❌ 未變更 | Pending → Gate0 → Gate1 → Gate2 → Gate3 保留 |
| Flow 規格（GOV-xxx） | ❌ 未變更 | 所有 19 個 Flow 規格保留 |
| Flow-only 設計原則 | ❌ 未變更 | Power Apps 仍禁止直接寫入治理表 |
| Guardrails 機制 | ❌ 未變更 | GOV-017/018/019 機制保留 |
| 三道防線架構 | ❌ 未變更 | FLS → Guardrail → Reconciler 保留 |
| 治理核心模型 | ❌ 未變更 | 專案生命週期、審批流程保留 |

### 變更範圍聲明

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  變更範圍聲明                                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  本次升級僅涉及：                                                            │
│                                                                             │
│  ✓ UI 視覺設計（色彩、間距、排版）                                           │
│  ✓ 控制項命名規範                                                           │
│  ✓ 文件敘述補強                                                             │
│  ✓ UX 驗證檢查清單                                                          │
│                                                                             │
│  本次升級不涉及：                                                            │
│                                                                             │
│  ✗ 資料模型（Dataverse）                                                    │
│  ✗ 業務邏輯（Flow）                                                         │
│  ✗ 治理規則（Gate、狀態機）                                                  │
│  ✗ 安全機制（FLS、Guardrails）                                              │
│  ✗ 新增表單或功能                                                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## D. 風險評估

### 低風險項目

| 風險項目 | 風險等級 | 緩解措施 |
|---------|:--------:|---------|
| 色彩變數重命名 | 🟢 低 | App.OnStart 包含完整變數定義 |
| 控制項命名變更 | 🟢 低 | 提供明確命名規範表 |
| Section 結構調整 | 🟢 低 | 資訊分類更清晰 |

### 無風險項目

| 項目 | 說明 |
|------|------|
| 治理邏輯 | 完全未變更 |
| Flow 參數 | 完全保留 |
| 資料流向 | Power Apps → Flow → Dataverse 不變 |
| 權限模型 | 完全未變更 |

### 向後相容性

| 項目 | 相容性 | 說明 |
|------|:------:|------|
| 既有專案資料 | ✅ 完全相容 | Dataverse 未變更 |
| 既有 Flow | ✅ 完全相容 | Flow 規格未變更 |
| 既有使用者操作 | ✅ 完全相容 | 表單功能未變更，僅視覺調整 |

---

## E. 未來 UI 擴充規範建議

### 新增表單規範

任何新增表單必須：

1. **遵循品牌標準**：appendix/Canvas-Brand-UI-Standard-v1.md
2. **採用五區塊配置**：Header → Gate Stepper → Body → Footer → Message
3. **Body 分三個 Section**：Basic Information → Responsibility → Details
4. **使用品牌色彩變數**：禁止硬編碼色碼
5. **Flow-Only 欄位標註**：使用 "(System-controlled)" 後綴
6. **通過 UX 驗證 Checklist**：結構、色彩、控制項、品牌驗證

### 禁止事項

| 禁止項目 | 原因 |
|---------|------|
| 更改品牌主色 #0C3467 | 品牌象徵 |
| 自定義新色彩 | 破壞一致性 |
| 跳過五區塊配置 | 破壞結構一致性 |
| Button 順序混亂 | 破壞操作一致性 |
| 使用浮動 Toast | Message 固定於頂部 |

### 文件維護

| 項目 | 維護要求 |
|------|---------|
| Canvas-Brand-UI-Standard-v1.md | 品牌變更時更新 |
| 04-powerapps-forms.md | 表單功能變更時更新 |
| UX 驗證 Checklist | 新增表單時擴充 |

---

## F. 修改檔案清單

### 新增檔案

| 檔案 | 位置 | 用途 |
|------|------|------|
| Canvas-Brand-UI-Standard-v1.md | appendix/ | 品牌 UI 設計標準 |

### 修改檔案

| 檔案 | 版本變更 | 修改內容 |
|------|---------|---------|
| 04-powerapps-forms.md | v4.0 → v5.0 | 套用品牌標準、升級 App.OnStart、補強操作步驟 |

### 未修改檔案

| 檔案 | 說明 |
|------|------|
| 02-dataverse-data-model-and-security.md | Dataverse 未變更 |
| 05-core-flows-implementation-runbook.md | Flow 未變更 |
| 06-guardrails-and-anti-cheating.md | Guardrails 未變更 |
| 其他所有文件 | 未涉及本次升級 |

---

## G. 結論

### 升級成效

| 指標 | 結果 |
|------|------|
| 品牌一致性 | ✅ 達成 |
| 結構統一性 | ✅ 達成 |
| 傻瓜可操作性 | ✅ 達成 |
| 治理核心保護 | ✅ 達成 |

### 封版聲明

本次升級為 **Canvas UI 品牌標準 v1.0 封版**。

- 所有表單已套用統一品牌標準
- 品牌色彩系統已定義並鎖定
- 結構規範已確立並鎖定
- 禁止未經核准的視覺變更

---

**報告結束**

**升級執行人員**：Claude Opus 4.5
**升級日期**：2026-02-11
**品牌標準依據**：appendix/Canvas-Brand-UI-Standard-v1.md
