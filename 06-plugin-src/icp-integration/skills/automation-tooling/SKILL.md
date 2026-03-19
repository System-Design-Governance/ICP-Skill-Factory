---
name: automation-tooling
description: >
  自動化工具開發：計算腳本、文件產生器、驗證工具。
  MANDATORY TRIGGERS: 自動化工具, automation tooling, 計算腳本, calculation script,
  文件產生器, document generator, 驗證工具, validation tool.
  Use this skill for engineering automation tool development in OT/ICS projects.
---

# 自動化工具開發 (Automation Tooling)

整合 3 個 SK，涵蓋計算腳本、文件產生器、驗證工具開發。

---

## 0. 初始化

1. 待自動化的手動流程已識別
2. 開發環境已建立 (Python/MATLAB/VBA)
3. 版本控制已配置 (Git)
4. 使用者需求已蒐集 (誰用、多常用、輸入/輸出)

---

## 1. 工作流程

### Step 1: 計算腳本開發 (SK-D13-001)

**常見自動化計算**：

| 計算類型 | 手動耗時 | 自動化後 | 工具 |
|----------|----------|----------|------|
| Cable sizing | 2-4 hr/cable | < 1 min | Python + IEC 60364 |
| Short circuit | 4-8 hr | 5 min | Python + ETAP API |
| Voltage drop | 1-2 hr/feeder | < 1 min | Excel VBA |
| Protection coordination | 8-16 hr | 30 min | MATLAB + relay lib |
| Battery sizing | 2-4 hr | 5 min | Python |

**開發規範**：

| 項目 | 要求 |
|------|------|
| Input validation | 所有輸入經範圍/格式檢查 |
| Unit handling | 明確標示單位、支援轉換 |
| Error handling | 有意義的錯誤訊息 (非 stack trace) |
| Logging | 計算過程可追蹤 (audit trail) |
| Testing | 至少 3 組已知答案驗證 |
| Documentation | README + usage example |

**步驟**：
1. 分析手動計算流程 → 識別可自動化部分
2. 定義輸入/輸出 spec (格式、範圍、單位)
3. 實作核心計算邏輯
4. 加入 input validation + error handling
5. 用已知答案驗證 (≥ 3 組 benchmark)
6. 撰寫使用說明 + 範例

**⚠️ 避坑**：
- 計算公式未標明來源標準 → 審計時無法追溯
- 未做 input validation → 使用者輸入錯誤單位，結果差 10 倍
- 只驗證一組資料 → 邊界條件錯誤未被發現

### Step 2: 文件產生器開發 (SK-D13-002)

**文件產生流程**：

```
Template + Data Source → Render Engine → Output (PDF/DOCX/HTML)
```

**常見文件產生場景**：

| 文件 | 資料來源 | 範本 | 輸出 |
|------|----------|------|------|
| Test Report | 測試結果 DB | FAT/SAT template | PDF |
| Equipment List | Asset DB | BOM template | Excel |
| SLD | 電力系統模型 | CAD template | DWG/PDF |
| Compliance Matrix | SR checklist | IEC 62443 template | DOCX |

**步驟**：
1. 分析文件結構 → 識別固定部分 vs. 動態部分
2. 設計範本 (Jinja2 / XSLT / mail merge)
3. 建立資料源連接
4. 實作 render engine
5. 加入格式控制 (分頁、頁首/尾、浮水印)
6. 驗證輸出 vs. 手動產出 (逐欄位比對)

**⚠️ 避坑**：
- 範本硬編碼 → 需求變更時改程式而非改範本
- 中文/特殊字元 → encoding 問題導致亂碼
- 未處理空值 → 輸出含 "None" 或空白區塊

### Step 3: 驗證工具開發 (SK-D13-003)

**驗證工具類型**：

| 類型 | 驗證內容 | 範例 |
|------|----------|------|
| 命名規範檢查 | 設備/點位 ID 格式 | SS01_TR01_TEMP_AI ✓ |
| 交叉一致性 | 文件間資料一致 | SLD ID = BOM ID |
| 完整性檢查 | 必要欄位非空 | 所有 SR 有 status |
| 合規檢查 | 符合標準要求 | IEC 62443 SR 覆蓋率 |
| 計算驗證 | 計算結果正確 | V_drop < 5% |

**步驟**：
1. 定義驗證規則 (從標準/規範提取)
2. 設計規則引擎 (rule-based / schema validation)
3. 實作驗證邏輯
4. 產出驗證報告 (pass/fail/warning per rule)
5. 支援批次驗證 (整個專案一次跑)
6. 整合到 CI/CD pipeline (自動觸發)

**⚠️ 避坑**：
- 規則太死板 → 合法例外也報錯，使用者不信任工具
- 驗證報告無定位資訊 → 只說 "fail" 不說哪裡 fail

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | 計算腳本用 ≥ 3 組 benchmark 驗證通過 |
| 2 | 文件產生器輸出與手動產出一致 |
| 3 | 驗證工具覆蓋所有定義的規則 |
| 4 | 所有工具有 README + usage example |
| 5 | Input validation 覆蓋所有使用者輸入 |
| 6 | 工具已整合版本控制 (Git) |

---

## 3. 人類審核閘門

```
自動化工具開發完成。
📋 範圍：3 個工程步驟 (SK-D13-001, 002, 003)
📊 交付物：計算腳本 ({n} 支)、文件產生器 ({m} 範本)、驗證工具
⚠️ 待確認：{TBD 項目}
👉 請 DES + QAM 審核。
```

---

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D13-001 | Calc Script Dev | 計算自動化、input validation、benchmark |
| SK-D13-002 | Doc Generator | 範本引擎、資料源、格式控制 |
| SK-D13-003 | Validation Tool | 規則引擎、交叉一致性、批次驗證 |

<!-- Phase 6: Enhanced 2026-03-19. -->
