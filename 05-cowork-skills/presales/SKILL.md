---
name: presales
description: >
  Execute a complete Presales proposal preparation workflow for cybersecurity, network, and IT infrastructure projects.
  Takes client input documents (SOW, requirements specs, compliance standards) and produces 4 deliverables:
  feasibility assessment, system architecture, commercial BOM (CBOM), and document inventory.
  Includes automated cross-consistency review, defect fixing, and release packaging.
  MANDATORY TRIGGERS: presales, 提案, 提案準備, pre-sales, proposal preparation, bid preparation,
  feasibility study, 可行性評估, 投標準備, SOW analysis, SOW 分析, Gate 0, Pre-Gate 0,
  售前評估, technical proposal, 技術提案, tender response, 招標回應, 售前工作流程.
  Use this skill whenever the user wants to prepare a proposal, estimate costs for an IT/OT/cybersecurity project,
  assess feasibility, generate architecture + BOM from client requirements, or run any part of a presales pipeline.
  Also trigger when the user mentions SOW analysis, compliance gap assessment, or needs to produce
  a package of technical + commercial deliverables for a client bid.
---

# Presales 提案準備工作流程

本 Skill 將客戶原始文件（SOW、需求規範、合規標準）轉化為完整的 Presales 提案包，包含可行性評估、系統架構、商務物料清單(CBOM)與文件清冊，並經過交叉一致性審查。

## 適用範圍

資安、網路、IT 基礎設施、OT/ICS 安全、實體安全等系統整合專案的售前準備。精度定位為 Presales 高階估算級 (±20%)。

## 關聯 Skill

本 Skill 在執行過程中會引用以下獨立 Skill 的規範：

| Skill | 引用時機 | 職責 |
|-------|----------|------|
| **arch-diagram** | T05 系統架構設計 | 架構圖渲染規範：D2/Mermaid 工具選擇、圖層佈局、Zone 顏色體系、元件命名、Conduit 標註 |
| **cbom-builder** | T06 商務物料清單 | BOM 填表規範：公司模板欄位對應、定價邏輯、工時估算基準、幣別處理、公式規則 |

執行 T05 時，必須先讀取 arch-diagram Skill 的規範再開始繪圖。
執行 T06 時，必須先讀取 cbom-builder Skill 的規範再開始填表。

---

## Phase 0: 初始化

### 0.1 建立專案目錄

在工作目錄下建立以下結構（若不存在）：

```
presales_project/
├── 00_inbox/          ← 使用者放入客戶文件
├── 01_brief/          ← Planner 產出
├── 02_plan/           ← Planner 產出
├── 03_work/           ← Executor 產出
├── 04_review/         ← Reviewer 產出
└── 05_release/        ← 最終交付包
```

### 0.2 讀取客戶輸入

掃描 `00_inbox/` 中的所有文件。典型輸入包括：

- 業主需求書 / SOW (Scope of Work)
- 合規要求（如 IEC 62443、ISO 27001、業主 ER）
- 公司 BOM 模板（如有 .xlsx 模板則後續直接填入）
- 場勘紀錄、現況架構圖（如有）
- RFP / 招標文件

讀完後，向使用者確認以下決策點（使用 AskUserQuestion）：

1. **架構圖工具**：Mermaid（嵌入 markdown）或 D2（產出 .d2 原始碼）
2. **CBOM 輸出格式**：markdown 表格 或 填入公司 Excel BOM 模板
3. **報價幣別**：TWD / USD / EUR / other
4. **業主預算**：已知（金額）/ 未提供（自行估算）

---

## Phase 1: Planner — 需求結晶與任務規劃

以 Planner 角色執行。職責是**規劃**，不是撰寫正文。

### 產出清單

| 檔案 | 路徑 | 說明 |
|------|------|------|
| 需求結晶 | `01_brief/brief.md` | 1-2 頁，含系統邊界(In/Out Scope)、核心業務目標、主要限制、利害關係人 |
| 任務樹 | `02_plan/tasks.md` | 10 個標準任務 T01–T10（見下表） |
| 驗收標準 | `02_plan/acceptance.md` | 專案特化版 DoD |
| 假設登錄 | `02_plan/assumptions.md` | 假設(A)、風險(R)、阻塞(B)，影響報價者標 [$] |
| 術語表 | `02_plan/glossary.md` | 專案相關縮寫與術語 |

### 標準任務樹

```
T01 需求萃取 → T02 任務樹 → T03 假設登錄
  ↓
T04 可行性評估
  ↓
T05 系統架構設計
  ↓ ↘
T06 CBOM  T07 文件清冊
  ↓         ↑
  ├─→ T06a 精算回圈（觸發條件成立時回到 T06）
  ↓
T08 全域審查（含底層清帳）→ T09 修正缺陷 → T10 打包交付
```

### 隱性需求辨識

Planner 必須主動從客戶文件中辨識「客戶沒說但業界慣例需要」的項目，常見包括：
HLD/LLD 設計文件、IP 位址規劃、安全基線設定、維護窗口協議、教育訓練、備品策略、保固/維護合約、合規 Gap Analysis。

每項隱性需求給予 IR-XX 編號，登錄於 brief.md。

### 完成 Phase 1 後

向使用者報告 brief 摘要與假設清單，等待確認後再進入 Phase 2。

---

## Phase 2: Executor — 四大交付物

依序執行 T04–T07。每個任務完成後必須輸出 Self-Check，格式為：

```
| # | 檢查項目 | 結果 | 備註 |
|---|----------|------|------|
| 1 | [條件]   | ✅ PASS / ❌ FAIL | [說明] |
```

### T04: 可行性評估 (`03_work/feasibility.md`)

讀取 `templates/feasibility_template.md`（本 skill 附帶）作為結構指引。

**文件章節結構**：
```
§1 專案概述（1段）
§2 技術可行性（逐項評估表）
§3 商務可行性（成本分類表，含 ±20% 高低估）
§4 時程可行性（里程碑 + 關鍵路徑）
§5 綜合建議（Go / No-Go / Conditional Go）
§6 附錄：假設與風險
```

必須包含三面向評估：

1. **技術可行性**：逐項對照 SOW 需求，評估技術方案是否可行
2. **商務可行性**：成本效益概估，分類列出硬體/軟體/ISP/工程/合規/營運/PM/差旅/退場等成本項，給出金額範圍 (±20%)
3. **時程可行性**：主要里程碑、關鍵路徑、前置時間風險

成本分類表格式：
```
| 分類 | 低估 | 基準 | 高估 | 備註 |
|------|------|------|------|------|
```

最後給出 Go / No-Go / Conditional Go 建議。

### T05: 系統架構設計 (`03_work/architecture.md`)

讀取 `templates/architecture_template.md`（本 skill 附帶）作為結構指引。
**⚠️ 開始前必須先讀取 arch-diagram Skill 規範，依其定義的顏色/圖層/命名/圖例標準渲染架構圖。**

**文件章節結構**：
```
§1 系統邊界（In/Out Scope + 外部介面表）
§2 邏輯架構圖（D2 + Mermaid + 元件說明表）
§3 Zone/Conduit（Zone 定義表 + Conduit 定義表）
§4 資料流表
§5 關鍵技術選型表
§5A 補充設計：CCTV 整合（如適用）
§5B 補充設計：事件回應流程
§5C 補充設計：退場程序
§6 圖例
```

必須包含：
- **系統邊界與外部介面表**（In/Out Scope 明確標示）
- **架構圖**：依 arch-diagram Skill 規範渲染（D2/Mermaid 雙軌、Zone 顏色、元件命名）
- **元件說明表**：每個元件含功能描述、部署位置、**對應 CBOM 品項編號**
- **Zone/Conduit 定義**：Zone 表（安全等級、包含元件）+ Conduit 表（連接 Zone、協定、安全措施）
- **資料流表**：來源、目的、資料類型、頻率
- **技術選型表**：選型、理由、替代方案
- **補充設計**：CCTV 整合（如適用）、事件回應流程概要、退場程序概要

CBOM 品項編號規則：硬體 CBOM-H01~Hnn，軟體 CBOM-S01~Snn。

**元件說明表必備欄位**：
```
| 元件 | 功能描述 | 部署位置 | 對應 CBOM 品項 |
```
- 「對應 CBOM 品項」欄必填，格式為 `CBOM-H{nn}` 或 `CBOM-S{nn}`
- 不含於我方供貨的元件：填 `不含於我方供貨（{業主}自有）`

### T06: 商務物料清單 (`03_work/cbom.xlsx` 或 `cbom.md`)

**⚠️ 開始前必須先讀取 cbom-builder Skill 規範，依其定義的欄位對應、定價邏輯、工時基準填表。**

**如有公司 BOM 模板 (.xlsx)**：
1. 讀取模板結構（sheet 名稱、欄位、公式）
2. 複製模板為 `03_work/cbom.xlsx`
3. 填入專案資訊（01參數設定 sheet）
4. 填入 BOM 品項，依模板的 Group 分類（項目/工程安裝/規劃設計/現場任務/專案管理）
5. 確保 Total Cost 欄位使用公式 `=Qty*Cost`
6. 使用 `recalc.py` 重新計算公式
7. 針對 template 已有的分析 sheet（成本統計、報價分析等），保留原有公式不動

**如無公司模板**：
產出 `03_work/cbom.md`，依 cbom-builder Skill §9 的 Markdown BOM 格式。

CBOM 品項需完整涵蓋：
- architecture.md 中所有硬體元件（含線材、機櫃、配件）
- 所有軟體授權（含延長期間）
- ISP/通訊月費（依營運期間計算）
- 工程人天（安裝、設定、佈線、門禁）
- 規劃設計人天（HLD/LLD、Gap Analysis、偏差聲明、事件程序）
- 現場任務人天（場勘、FAT/SAT、訓練、竣工文件、營運文件編製、月維護、退場）
- 專案管理人天 + 差旅 + 保險 + 運輸
- 已知風險準備金（大型案 5%、中小型案 3%）+ 保固費（總額 2%/年）

**CBOM Excel 額外格式要求**：
- 每個 Group 之間空一行
- Group 標題行加粗
- 品項按邏輯順序排列（非字母排序）：先核心設備、再周邊、再線材配件

### T06a: 精算回圈（Iterative Refinement Loop）

**F6 經驗**：CBOM 通常需要多次迭代（F6 實績 12 版），不是線性一次完成。

**觸發條件**（任一成立即回到 T06 修正）：

| # | 觸發條件 | 典型案例 |
|---|---------|---------|
| 1 | Scope 變更 | 客戶追加/移除子系統（如 DGA 移除 -3.2M） |
| 2 | Port Budget 驗證失敗 | PRP 交換機數量需修正（如 15→27 台） |
| 3 | 報價單比對差異 >15% | 供應商正式報價與估價有顯著差異 |
| 4 | 架構變更連動 | T05 修正 Zone/Conduit 後影響設備清單 |
| 5 | 底層清帳發現差異 | Python 加總與 Excel 公式不符 |

**精算回圈流程**：
```
T06 CBOM 初版 → 交叉驗證（見 cbom-builder references/epci_substation_patterns.md §5）
  → 發現差異？ → 是 → 修正 CBOM → 更新版本號 → 重新驗證
                → 否 → 進入 T07
```

**注意**：每次修正須更新版本號（v0.1→v0.2→...），保留修正原因紀錄。

---

### T07: 文件清冊 (`03_work/doc_inventory.md`)

讀取 `templates/doc_inventory_template.md`（本 skill 附帶）作為結構指引。

**文件章節結構**：
```
§1 文件清冊表（D-/T-/O-/P-/C- 分類）
§2 需求追溯矩陣
§3 交付時程（T+0 ~ T+{n} 月）
§4 CBOM 對照表（100% 覆蓋率）
```

必須包含：
- **文件清冊表**：文件編號（D-/T-/O-/P-/C-分類）、名稱、對應需求、負責人、交付階段
- **需求追溯矩陣**：SOW 條目 + ER 條款 + 隱性需求 → 對應文件
- **交付時程**：各階段（設計/採購/FAT/安裝/SAT/移交/營運/退場）的文件交付
- **CBOM 對照表**：每份文件對應的 CBOM 人工品項（必須 100% 覆蓋）

**文件編號規則**：

| 前綴 | 分類 | 範例 |
|------|------|------|
| D-{nn} | 設計 (Design) | D-01 HLD, D-02 LLD |
| T-{nn} | 測試 (Test) | T-01 FAT Plan, T-02 SAT Report |
| O-{nn} | 營運 (Operations) | O-01 SOP, O-02 Backup Procedure |
| P-{nn} | 專案管理 (PM) | P-01 Project Plan, P-02 Progress Report |
| C-{nn} | 合規 (Compliance) | C-01 Gap Analysis, C-02 Deviation Statement |

---

## Phase 3: Reviewer — 全域審查

以 Reviewer 角色執行。職責是**找問題**，不是修問題。

### 審查維度

讀取 `references/review_checklist.md` 取得完整審查清單。核心維度：

| 維度 | 檢查重點 |
|------|---------|
| A. 交叉一致性 | arch 元件 vs CBOM 品項、feasibility 估計 vs CBOM 總額、doc_inventory vs CBOM 人天 |
| B. SOW 覆蓋度 | 每項 SOW 需求是否在 arch/CBOM/doc 中有對應 |
| C. 合規性 | ER/標準條款是否在 arch 或 doc 中有應對 |
| D. 數值一致性 | 元件數量、營運期間、成本範圍是否一致 |
| E. 品質問題 | TBD 項目、術語不一致、邏輯缺口 |
| **F. 底層清帳** | **Python 逐 Group 加總驗證、跨版本 diff 比對（必要步驟）** |
| **G. Component-CBOM Mapping** | **架構設備清冊每項設備都有對應 CBOM 行項目** |

### 產出格式

`04_review/review_report.md` 中每項缺陷需有：ID、嚴重度（🔴/🟡/🟢）、分類、檔案位置、問題描述、建議修正。

---

## Phase 4: 修正與交付

### T09: 修正缺陷

依 review_report.md 的優先級修正：
- 🔴 Critical：必須修正（如成本不符、覆蓋缺漏）
- 🟡 Major：盡量修正（如 ISP 定價、術語不一致）
- 🟢 Minor：選擇性修正
- 需外部輸入的缺陷標記為 ⏳ Deferred

### T09a: Open Items Register

Presales 階段識別但無法在 Pre-Gate 0 解決的待定項目，須編入 Open Items Register 確保傳遞至 Detailed Design：

```markdown
| OI-ID | 描述 | 來源 | 影響（成本/時程/範圍） | 負責人 | 目標解決階段 |
|-------|------|------|---------------------|--------|------------|
| OI-001 | Cybersecurity scope 待定 | T05 | ±30-38M | SAC | R1 |
| OI-002 | PAGA/Radio Mast 歸屬 | SOW | ±5M | PM | Gate 0 |
```

**傳遞規則**：
- 所有 Open Items 必須出現在 Gate 0 Decision Package 中
- 具成本影響的 OI 須在 CBOM 中預留對應金額或標記 `[TBD]`
- R1 啟動時，Open Items Register 移交給 SYS/SAC 負責人

---

### T10: 打包交付

產出 `05_release/RELEASE_NOTE.md`，包含：
- 交付物清單（檔案名 + 說明 + Self-Check 結果）
- 缺陷修正狀態表
- 關鍵數據摘要（CBOM 總額、feasibility 範圍、營運期間、品項數）
- **CBOM 版本演化摘要**（初版→定版的金額變化軌跡、主要修正原因）
- **Open Items Register**（待後續解決的待定項目）
- 待後續確認事項

---

## 檢查點協定

每個 Phase 完成後必須向使用者報告並等待確認：

| 檢查點 | 時機 | 報告內容 |
|--------|------|---------|
| CP1 | Phase 1 完成 | brief 摘要 + 假設清單 + 隱性需求 |
| CP2 | T04 完成 | Go/No-Go 結論 + 成本範圍 |
| CP3 | T05 完成 | 架構圖 + 元件數 + Zone/Conduit 數 |
| CP4 | T06 完成 | CBOM 總額 + 品項數 |
| CP5 | T07 完成 | 文件數 + 追溯覆蓋率 |
| CP6 | T08 完成 | 缺陷數量（Critical/Major/Minor） |
| CP7 | T10 完成 | Release Note 連結 |

使用者說「繼續」或類似確認語時，才進入下一 Phase/Task。

---

## 文件格式通則

所有 Presales 交付物（Markdown 文件）遵循以下格式規則：

### 通用文件結構

```markdown
# {文件標題} — {專案名稱}

版本：v{X.Y}
更新日期：{YYYY-MM-DD}
{其他元資訊（如對應圖檔路徑）}

---

## 1. {第一章節}
### 1.1 {子章節}

[正文內容]

---

## 2. {第二章節}
...
```

### 標題層級

| 層級 | 用途 | 範例 |
|------|------|------|
| H1 `#` | 文件標題（每份文件僅一個） | `# 高階系統架構 — DFO 臨時設施` |
| H2 `##` | 主章節（帶編號） | `## 3. 網路拓撲 / Zone-Conduit` |
| H3 `###` | 子章節 | `### 3.1 Zone 定義` |
| H4 `####` | 細項（較少使用） | `#### 3.1.1 Office IT Zone 詳述` |

編號格式：`{H2序號}.{H3序號}`，不跳號。H2 之間用 `---` 分隔。

### 表格規則

- 空值用 `—` 或 `N/A`，不留空白
- 欄寬讓內容自然延伸
- Markdown 不支援跨列，改用備註欄

### 版本控制

| 欄位 | 格式 | 規則 |
|------|------|------|
| 版本號 | `v{主版本}.{修訂}` | Executor 產出為 v0.1；Reviewer 修正後為 v1.0 |
| 更新日期 | `YYYY-MM-DD` | 最後修改日期 |
| 變更紀錄 | Release Note 中統一列出 | 不在各文件內設獨立 changelog |

### 語言規範

| 元素 | 語言 | 範例 |
|------|------|------|
| 章節標題 | 中文 | `系統邊界`、`技術選型` |
| 表格欄位名 | 中文 | `元件`、`功能描述` |
| 技術術語 | 英文原文（不翻譯） | `Firewall`、`EDR`、`VLAN` |
| 品牌/型號 | 英文原文 | `FortiGate 60F`、`Cisco CBS350` |
| 縮寫首次出現 | 全稱 + 縮寫 | `端點偵測與回應 (EDR)` |
| CBOM 品名 | 中文為主，括號附英文型號 | `邊界防火牆 (FortiGate 60F)` |

---

## 附帶模板

本 skill 的 `templates/` 目錄包含以下模板，執行對應任務前讀取：

- `feasibility_template.md` — 可行性評估結構
- `architecture_template.md` — 系統架構文件結構
- `doc_inventory_template.md` — 文件清冊結構

`references/` 目錄包含：

- `review_checklist.md` — 審查檢查清單詳細版
- `epci_workflow_pattern.md` — EPCI 變電所提案工作流模式（基於 F6 實績）


<!-- optimization-v3: trimmed 2026-03-16 | removed 904 redundant lines | condensed to 230-line core sections -->

---

## IEC 62443 Lifecycle 對應

| Lifecycle | Presales 角色 | 關鍵交付物 |
|-----------|-------------|-----------|
| Pre-R0 | 需求萃取、可行性評估、風險矩陣、CBOM、技術提案 | brief, feasibility, architecture, CBOM, proposal |
| R0 (Gate 0) | 提供 5 項必要輸入供決策 | Gate 0 Decision Package |
| R1 | Presales 輸出作為設計基線 | 交接至設計團隊 |

**Pre-Gate 0 邊界**：所有 Presales 產出皆為 advisory（非約束性），直到 Gate 0 核准後方具約束力（依 GOV-SD）。

---

## 域知識整合參考（SK-D14 系列）

以下為 T01-T10 各任務需參考的 SK 定義知識。執行各任務時應遵循其指引。

### 需求規格書 (SK-D14-001)
- 四類需求分類：Functional (FR)、Security (SR)、Operational (OR)、Interface (IF)
- 需求 ID：REQ-{nnn}，每項需有 priority + acceptance criterion + verification method
- Security 需求必須包含 IEC 62443 SL target 參考
- 產出：Requirements Traceability Matrix (RTM) + Open Issues Register

### 利害關係人分析 (SK-D14-002)
- Stakeholder Register：含 influence/interest 分類 + engagement strategy
- 四種策略：Manage Closely / Keep Satisfied / Keep Informed / Monitor
- Communication Plan：每組頻率、管道、內容、負責人
- Interface Register：正式組織介面

### 可行性評估強化 (SK-D14-003)
- 四維度評估：Technical / Commercial / Schedule / Operational
- 每個需求區域需有 verdict：Feasible / Feasible-with-Conditions / Not-Feasible
- 必須產出：Risk Pre-Disclosure List（業務語言，供 Gate 0 決策者）
- 最少 5 項技術風險，含 likelihood/impact + mitigation strategy
- One-page Feasibility Summary：overall verdict + top-3 risks

### 技術風險矩陣 (SK-D14-004)
- 五類風險：Technology (TEC) / Integration (INT) / Delivery (DEL) / Resource (RES) / External (EXT)
- Risk ID：TR-{nnn}，含 description, category, likelihood, impact, score, mitigation, owner
- Risk Pre-Disclosure List 需用業務語言（非技術語言）

### 技術提案 (SK-D14-008)
- 10 章結構：Executive Summary → 需求理解 → 方案說明 → 交付方法 → 安全方法 → 團隊資歷 → 風險管理 → 假設排除 → 合規矩陣 → 附錄
- Compliance Matrix 100% 覆蓋率（逐項回應招標需求）
- 標註為 Pre-Gate 0 advisory

### POC 規劃 (SK-D14-009)
- POC Charter：objectives, scope, success criteria, timeline
- 驗證報告含量化指標（latency, throughput, detection rates）
- 客戶環境零非預期停機
- 經驗教訓回饋至可行性評估與風險矩陣

### 安全需求定義 (SK-D14-010)
- 客戶安全需求 → IEC 62443 SP/SR category 對應
- 每 Zone 提出 SL-T 建議（含依據）
- Security deliverable inventory（依 IEC 62443-2-4 SP 類別）
- Gate 0 quality thresholds：comprehensible, evaluable, owner assigned, scope stable

---

## 品質檢查清單 (Quality Checklist)

### Phase 1 (Planner)
- [ ] Brief 含明確 In/Out Scope boundary
- [ ] 隱性需求已辨識（IR-XX 編號）
- [ ] 假設已登錄，影響報價者標 [$]
- [ ] 需求按 FR/SR/OR/IF 四類分類

### Phase 2 (Executor: T04-T07)
- [ ] T04：可行性含 3+ 維度評估，有 Go/No-Go/Conditional Go 結論
- [ ] T04：Risk Pre-Disclosure List 含 ≥5 項風險
- [ ] T05：架構遵循 arch-diagram SKILL 規範
- [ ] T05：元件表含 CBOM 品項對照（CBOM-H/S 編號）
- [ ] T06：CBOM 遵循 cbom-builder SKILL 規範
- [ ] T06：品項覆蓋架構中所有硬體/軟體
- [ ] T07：需求追溯 100% 覆蓋（SOW + ER + 隱性需求）
- [ ] T07：CBOM 對照表 100% 覆蓋

### Phase 3 (Reviewer: T08-T10)
- [ ] T08：跨檔一致性通過（arch ↔ CBOM ↔ doc）
- [ ] T08：所有 🔴 Critical 缺陷已修正
- [ ] T10：Release Note 含關鍵數據摘要

---

## 人類審核閘門 (Human Review Gate)

本 Skill 在每個 Phase 完成後暫停，等待使用者確認。

**審核標準**：
- **PASS**：使用者確認或僅有 Minor 修正
- **FAIL**：發現重大缺漏，必須返工後重審
- **PASS with Conditions**：使用者接受但要求補充項目

**CP 審核提示範本**：
```
Phase {N} 已完成。
📋 摘要：{1-3 句關鍵發現}
📊 數據：{品項數/金額/覆蓋率等量化指標}
⚠️ 風險：{待確認假設或 TBD 項目}
👉 請確認是否可進入下一 Phase，或指出需調整的部分。
```

每個 CP 的專屬審核焦點：
| CP | 時機 | 核心審核焦點 |
|----|------|-------------|
| CP1 | Phase 1 完成 | Brief 完整性 + 假設合理性 + 隱性需求識別 |
| CP2 | T04 完成 | Go/No-Go + 成本範圍 ±20% + 風險揭露清單 |
| CP3 | T05 完成 | 架構圖 + Zone/Conduit + 元件表 + CBOM 對照 |
| CP4 | T06 完成 | CBOM 總額 + 品項覆蓋率 + 工時合理性 |
| CP5 | T07 完成 | 文件數 + 追溯覆蓋率 + CBOM 人天對照 |
| CP6 | T08 完成 | 缺陷統計 (🔴/🟡/🟢) + 跨檔一致性 |
| CP7 | T10 完成 | Release Note + 待確認事項 |

---

## Source Traceability

| 整合來源 | SK 編號 | 核心知識 |
|---------|--------|---------|
| Requirements Specification Development | SK-D14-001 | 四類需求、REQ-nnn、RTM |
| Stakeholder Analysis | SK-D14-002 | 利害關係人矩陣、溝通計畫 |
| Technical Feasibility Assessment | SK-D14-003 | 四維度評估、風險揭露 |
| Technical Risk Matrix Development | SK-D14-004 | 五類風險、TR-nnn、RPN |
| Technical Proposal Writing | SK-D14-008 | 提案結構、合規矩陣 |
| POC Planning and Execution | SK-D14-009 | POC Charter、驗證報告 |
| Tender Security Requirements | SK-D14-010 | SL-T 提案、安全交付物清單 |

<!-- Phase 5 Wave 1: SK knowledge integrated from SK-D14-001~004, 008~010 -->
<!-- F6 Optimization: iterative refinement loop, bottom-up reconciliation, Open Items Register -->
