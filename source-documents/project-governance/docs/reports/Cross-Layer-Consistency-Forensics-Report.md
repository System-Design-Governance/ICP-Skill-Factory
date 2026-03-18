# Cross-Layer Consistency Forensics Report

> **Audit Date**: 2026-03-05
> **Remediation Date**: 2026-03-05
> **Scope**: 49 files, 53,588 lines across 4 governance layers
> **Method**: Exhaustive cross-layer comparison with line-level evidence
> **Remediation**: 30/54 findings fixed across 17 files (~125 lines changed)

---

## Executive Summary

本鑑識級審計對治理文件體系四層架構進行窮舉式交叉比對，發現 **54 項問題**，分布如下：

| 嚴重度 | 數量 | 已修復 | 不修復（含理由） | 說明 |
|:-------|:----:|:------:|:---------------:|:-----|
| **CRITICAL** | 7 | 6 | 1 | 跨層定義衝突、編號碰撞、數值不相容 |
| **HIGH** | 11 | 8 | 3 | 角色越權、懸空引用、結構缺口 |
| **MEDIUM** | 18 | 11 | 7 | 命名漂移、語意不一致、時序風險 |
| **LOW** | 10 | 5 | 5 | 過時引用、缺失文件、格式問題 |
| **INFO** | 8 | 0 | 8 | 一致性確認（合規項，無需修復） |
| **Total** | **54** | **30** | **24** | — |

> **修復摘要**：30 項已修復（跨 17 個文件，~125 行變更）。24 項不修復含 8 項 INFO 合規確認、7 項屬開發任務（非文件勘誤）、5 項屬治理委員會決議範疇、4 項為設計預期或未來規劃。

**Top 5 Must-Fix Issues（修復狀態）**:

1. ~~**OptionSet 前綴衝突**（CRITICAL）~~ — **FIXED** ✅ Ch.07 全部 36 處 `100000xxx` → `807660xxx`
2. ~~**GOV-020 三重身分**（CRITICAL）~~ — **FIXED** ✅ L2 SOP-04-part3 更新為 Document Inventory Parser，原 Document Unfreeze 延至 GOV-021；L3 Ch.04 映射修正
3. ~~**GOV-013/014 編號漂移**（CRITICAL）~~ — **FIXED** ✅ SOP-03-part1 Flow 表全面重編對齊 SOP-04
4. **7 條 Flow 無 L3 施工規格**（HIGH）— **NOT FIXED** — GOV-006~012 為 Phase 3 開發任務，非文件勘誤
5. ~~**風險接受權責衝突**（HIGH）~~ — **FIXED** ✅ SOP-01/SOP-05 全部對齊 L1 分級 RAA 定義

---

## Section 1: Role Definition Consistency Scan

### 1.1 L1 Canonical Role Registry

L1 共定義 **21 個角色**，來源為 `system-design-governance.md` 與 `appendix-b-raci.md`：

| # | 角色名稱 | 定義來源 | RACI 出現 |
|:-:|:---------|:---------|:---------:|
| 1 | System Architect | governance:165, raci:162-172 | R/A (Gate 0-3) |
| 2 | Security Team | governance:424, raci:174-183 | R (Gate 0-1), C (Gate 2-3) |
| 3 | QA Team | governance:232, raci:185-195 | R (Gate 1,3), C (Gate 2) |
| 4 | Project Manager | governance:91, raci:197-207 | C (Gate 0), R (Gate 3 簽核/交接) |
| 5 | Design Requesting Function | governance:249-267, raci:209-233 | R/A (Gate 0 需求), C (Gate 1) |
| 6 | Risk Acceptance Authority | governance:577-586, raci:235-248 | A (Gate 3 風險簽核) |
| 7 | Engineering Management | governance:119, raci:250-260 | **A** (Gate 0/1/2/3 per RACI table) |
| 8 | System Design Governance Function | governance:240, 423, 470 | (未列為 RACI 獨立欄) |
| 9 | Security Lead | governance:580-581 | (RAA 組成成員) |
| 10 | Business Owner | governance:267, 278-283 | (DRF/RAA 映射) |
| 11-21 | Product Owner, Requirement Owner, Owner, Approver, Required Reviewers, Co-signers, 系統設計部門, 專案執行部門, 營運維護部門, Risk Owner, Accountable Role | (各出處見下文) | — |

#### L1 RACI Approver 矛盾（Finding L1-RACI-01） — ✅ FIXED

> **嚴重度：CRITICAL** | **修復方式**：RACI 表 Gate 1/3 行加註腳標（†），Engineering Management 角色描述更新為 Gate 0/2 Approver + Gate 1/3 delegation

| Gate | 主文件 Approver | RACI 表 A 欄 |
|:----:|:----------------|:-------------|
| Gate 0 | Engineering Management | Engineering Management |
| **Gate 1** | **System Design Governance Function** (line 423) | **Engineering Management** (raci line 86) |
| Gate 2 | Engineering Management | Engineering Management |
| **Gate 3** | **System Design Governance Function** (line 470) | **Engineering Management** (raci line 130) |

- 主文件 `system-design-governance.md` 明確指定 Gate 1/3 Approver 為 System Design Governance Function
- RACI 表 `appendix-b-raci.md` 所有 Gate Review & Approval 行的 A 欄均為 Engineering Management
- Appendix A 檢查表同樣宣告 Gate 1 Approver = System Design Governance Function（line 298）、Gate 3 Approver = System Design Governance Function（line 331）
- RACI 表文字敘述補充「Gate 3 放行：由 System Design Governance Function」（raci line 149）

**影響**：L2 SOP 與 L3 均依照主文件（Gate 1/3 → Governance Function），但 RACI 表若被直接引用將產生相反結論。

---

### 1.2 L2 SOP Role Comparison

L2 SOP 共定義 **11 個角色**，跨 13 個文件出現以下角色定義衝突：

#### Finding SOP-ROLE-01: 風險接受權責衝突（HIGH） — ✅ FIXED

| 文件 | 風險接受者 | 行號 |
|:-----|:-----------|:----:|
| SOP-01 | Risk Owner (Low)=部門主管, (Med)=事業單位主管, (High)=CTO | 386-388 |
| SOP-05 ch1 | R1 System Architect 接受 Low/Medium | 221, 243 |
| SOP-05 ch1 | R7 Executive Management 接受 High | 227 |
| L1 | RAA: Low=PM, Med=PM+Security Lead, High=PM+Security Lead+Business Owner, Critical=Engineering Management | governance:579-582 |

**三套互不相容的風險接受矩陣**。SOP-05 允許 System Architect 接受 Low/Medium 風險，但 L1 明確禁止 System Architect 擔任 RAA（`appendix-b-raci.md` line 248：「不可由 System Architect 或 System Design Governance Function 擔任」）。

#### Finding SOP-ROLE-02: 治理角色命名漂移（HIGH） — ⚠️ PARTIAL FIX

| 文件 | 角色名 | Gate 職責 |
|:-----|:-------|:---------|
| SOP-01 line 385 | Governance Function | Gate 1 放行 |
| SOP-01 line 389 | Governance Owner | Gate 3 最終核准、例外豁免 |
| SOP-04-part1 line 41 | Governance Lead | Gate 0/3 Final Approval |
| SOP-05 ch1 line 226 | 治理負責人 | Gate 1/3 Governance Approval |

SOP-01 將 Governance Function 與 Governance Owner 分為**兩個角色**，SOP-04/05 合併為**一個 Governance Lead**。SOP-04-part1 更錯誤地將 Gate 0 指派給 Governance Lead（所有其他來源均為 Engineering Management）。

#### Finding SOP-ROLE-03: Security Reviewer Gate 範圍矛盾（MEDIUM） — ✅ FIXED

- SOP-04-part1 line 39：Security Reviewer 負責 `Gate 1/2 Security Review`
- SOP-01 line 382、SOP-05 ch1 line 223、SOP-04-part3 line 44：Security Reviewer 僅參與 **Gate 1**
- Gate 2 為 Engineering Management 單層審批，無 Security 層

#### Finding SOP-ROLE-04: QA Gate 3 職責遺漏（MEDIUM） — ✅ FIXED

- SOP-01 line 383：QA Team 僅列 Gate 1
- SOP-04-part3 line 45、SOP-05 ch1 line 224：QA 為 Gate 3 Layer 1 審查者
- SOP-01 **遺漏** QA 的 Gate 3 職責

#### Finding SOP-ROLE-05: Flow Service Principal 範圍過時（LOW） — ✅ FIXED

- SOP-01 line 391：`GOV-001~GOV-010`
- SOP-04-part1 line 44：`All Flows`
- 實際範圍已擴展至 GOV-019/020，SOP-01 未更新

---

### 1.3 L2 People Role Comparison

L2 People（`system-design-people`）定義 **7 個角色** JD，與 L1 比對結果：

| L2 People 角色 | L1 對應角色 | 匹配度 |
|:--------------|:-----------|:------:|
| Head of System Design | Engineering Management | 部分（L2 增加標準體系擁有者職責） |
| System Design Governance Lead | System Design Governance Function | 一致 |
| System Architect | System Architect | 一致 |
| Security Engineering Role | Security Team | 一致（更精細的 JD） |
| Design QA Role | QA Team | 一致 |
| Design Governance Coordinator | — | **L2 新增角色，L1 無定義** |
| Pre-Gate Design Support | — | **L2 新增角色，L1 無定義** |

#### Finding PEOPLE-ROLE-01: L2 角色越權擴展（MEDIUM） — NOT FIXED（L2 有權在 L1 框架內擴展角色定義）

- **Design Governance Coordinator**：L1 未提及此角色，L2 自行定義為非標準擁有的協調支援角色（`03-role-definitions-jd.md` lines 347-392）
- **Pre-Gate Design Support**：L1 僅在 `system-design-governance.md` lines 37-70 簡述 Pre-Gate0 釐清階段，L2 People 擴展為完整正式角色，附帶 7 項 KPI 與明確的責任邊界（`03-role-definitions-jd.md` lines 395-555）

#### Finding PEOPLE-ROLE-02: Coordinator 缺席 Gate 責任矩陣（LOW） — NOT FIXED（結構缺口，屬未來文件規劃）

- `02-role-responsibility-boundary.md` Gate 責任矩陣（lines 383-391）未包含 Design Governance Coordinator
- 但 JD 明確列出 Gate 相關職責（安排會議、記錄紀要）

---

### 1.4 L3 Role Usage Audit

L3 定義 **7 個安全群組**，映射至 L1/L2 角色：

| L3 安全群組 | L1/L2 角色 | 來源 |
|:-----------|:-----------|:-----|
| GOV-Architects | System Architect | Ch.01 line 366 |
| GOV-SecurityReviewers | Security Reviewer | Ch.01 line 367 |
| GOV-QAReviewers | QA Reviewer | Ch.01 line 368 |
| GOV-EngineeringManagement | Engineering Management | Ch.01 line 369 |
| GOV-GovernanceLead | Governance Lead | Ch.01 line 370 |
| GOV-ExecutiveManagement | Executive Management | Ch.01 line 371 |
| GOV-FlowServicePrincipal | (Service Account) | Ch.01 line 372 |

#### Finding L3-ROLE-01: 未映射角色（MEDIUM） — NOT FIXED（PM/DRF/RAA 在 Power Platform 無對應安全群組需求）

以下 L1 角色無 L3 對應安全群組：
- Project Manager
- Design Requesting Function
- Risk Acceptance Authority（分級）
- Pre-Gate Design Support
- Design Governance Coordinator

#### Finding L3-ROLE-02: 幽靈群組（LOW） — ✅ FIXED

- `GOV-AllStakeholders` 出現在 Ch.07 部署清單（line 1722）但從未在 Ch.01 或 00B 定義

---

## Section 2: Gate Flow Integrity Tracking

### 2.1 L1 Gate Criteria Registry

| Gate | 目的 | 觸發時機 | Approver | 來源行號 |
|:----:|:-----|:---------|:---------|:--------:|
| 0 | 受理決策 | 專案概念提出後、啟動前 | Engineering Management | governance:354-399 |
| 1 | 設計基線建立 | 初步設計完成後 | System Design Governance Function | governance:401-424 |
| 2 | 設計變更管理 | 設計基線後發生變更 | Engineering Management | governance:426-448 |
| 3 | 設計交付與責任移轉 | 詳細設計完成後 | System Design Governance Function | governance:450-493 |

**Gate 0 Entry Criteria** (4 項品質門檻)：
1. 可理解性（Comprehensibility）— governance:371
2. 可評估性（Evaluability）— governance:373
3. 需求擁有者明確性 — governance:375
4. 範圍穩定性 — governance:377

**Gate 1 Exit Criteria** (6 項最低產出)：設計基線文件、整合式風險評估報告、IEC 62443 檢查表、需求追溯矩陣、文件清冊、設計標的清冊

**Gate 2 Exit Criteria** (4 項)：變更描述與理由、影響分析、風險重新評估、更新後設計文件

**Gate 3 Exit Criteria** (4 項)：最終設計文件包、殘餘風險清單、設計交付檢查表、交接會議紀錄

---

### 2.2 SOP Coverage Matrix

| Gate | L2 審批層數 | L2 審批者 | L2 必要文件數 | 來源 |
|:----:|:----------:|:---------|:------------:|:-----|
| 0 | 1 | Engineering Management | 3 | sop-04-part2:834-858, sop-04-part3:42 |
| 1 | 3 | Security → QA → Governance Lead | 7 | sop-04-part2:862-883, sop-04-part3:43 |
| 2 | 1 | Engineering Management | 2 | sop-04-part2:887-905, sop-04-part3:44 |
| 3 | 2 | QA → Governance Lead | 3 | sop-04-part2:909-935, sop-04-part3:45 |

#### Finding GATE-SOP-01: Gate 0 Approver 矛盾（MEDIUM） — ✅ FIXED

SOP-04-part1 line 41 將 Gate 0 指派給 Governance Lead，但 sop-01 line 384、sop-04-part3 line 42、sop-05-ch1 line 225 均指派給 Engineering Management。**SOP-04-part1 角色表有誤**。

---

### 2.3 L3 Flow Coverage

| Gate | L3 實作 Flow | L3 審批層數 | 一致性 |
|:----:|:------------|:----------:|:------:|
| 0 | GOV-003 | 1 (GOV-GovernanceLead) | **待確認** — 見下方 |
| 1 | GOV-003 | 3 (Security → QA → Governance) | 一致 |
| 2 | GOV-003 | 1 (Engineering Management) | 一致 |
| 3 | GOV-003 + GOV-014 | 2 (QA → Governance) | 一致 |

#### Finding GATE-L3-01: Gate 0 Approver L3 實作（INFO — 合規確認）

L3 Ch.05 GOV-003 Gate 0 使用 `GOV-GovernanceLead` 群組（與 SOP-04-part3 主流來源一致，但 SOP-04-part1 角色表有誤）。此處 L3 遵循正確的 SOP-04-part3 規格。

---

## Section 3: Terminology & Definition Drift

### 3.1 Core Glossary

L1 定義 **46 個核心術語**（無獨立詞彙表文件，Appendix A 為 IEC 62443 Alignment）。關鍵術語摘錄：

| 術語 | L1 定義 | 來源 |
|:-----|:--------|:-----|
| 設計基線 | Gate 1 建立，含架構圖、介面定義、資料流圖 | governance:401-414 |
| 殘餘風險 | 設計階段無法完全消除之風險，Gate 3 揭露並移轉 | governance:562 |
| 重大變更 | 影響核心架構/外部介面、改變 SL、增移安全控制、影響已簽約承諾 | governance:448 |
| 整合式風險評估 | 必須結合 IEC 62443-3-2 + FMEA + HAZOP，三者不可互代 | governance:169-175 |
| 受理決策 | Gate 0 判定是否接受設計需求 | governance:363 |

### 3.2 Drift Inventory

#### Finding TERM-01: RequestStatus vs GateStatus 混淆（MEDIUM） — NOT FIXED（語意設計議題，非文件勘誤）

| 文件 | 欄位名 | 值集合 |
|:-----|:-------|:-------|
| SOP-02 lines 463-477 | RequestStatus | {Pending, UnderReview, Approved, Rejected} |
| SOP-05-ch3-4 lines 1228-1268 | GateStatus | {Approved, UnderReview, Rework, OnHold} |

SOP-02 定義 `RequestStatus`，SOP-05 引入 `GateStatus`，兩者值集合不同且未說明關係。

#### Finding TERM-02: Form-Only vs Form-First 命名漂移（LOW） — NOT FIXED（語意差異微小，各 SOP 內部一致）

- SOP-01：`Form-Only Interaction`
- SOP-05-ch5-6：`Form-First Principle`
- 同一概念，不同名稱

#### Finding TERM-03: MGL 要素數量不一致（MEDIUM） — NOT FIXED（不同粒度呈現屬設計選擇）

- SOP-01 定義 MGL 含 12 個事件
- SOP-05-ch1 使用「5 verification elements」框架
- 同一概念以不同粒度呈現，可能造成混淆

#### Finding TERM-04: Governance Lead 簡稱（LOW） — NOT FIXED（慣用簡稱，非錯誤）

- GOV-05-001（`09-annual-governance-cycle.md`）使用「Governance Lead」簡稱
- 正式全名為「System Design Governance Lead」
- 非錯誤但可能在脫離語境時造成歧義

---

## Section 4: KPI & JD Authorization Tracking

### 4.1 Role Match

L2 People 定義 7 個角色 JD（GOV-02-001），每角色含 4-7 個 KPI。與 L1 角色匹配：

| L2 JD 角色 | L1 匹配 | 差異 |
|:-----------|:--------|:-----|
| Head of System Design | Engineering Management | L2 擴展：標準體系擁有者、例外裁定 |
| System Design Governance Lead | Governance Function | 一致 |
| System Architect | System Architect | 一致 |
| Security Engineering Role | Security Team | L2 更精細化 |
| Design QA Role | QA Team | 一致 |
| Design Governance Coordinator | **無 L1 對應** | L2 新增 |
| Pre-Gate Design Support | **L1 僅簡述** | L2 大幅擴展 |

### 4.2 KPI Traceability

L2 People 共定義 **40 個 KPI**（7 角色），每個 KPI 均有 SMART 目標值。

#### Finding KPI-01: Pre-Gate Design Support KPI 數量不一致（HIGH） — ✅ FIXED

| 文件 | KPI 數量 | 細節 |
|:-----|:--------:|:-----|
| GOV-02-002（`04-role-kpi-evidence-model.md` lines 193-201） | **7** | 含 CBOM Completeness + Concept Architecture Completeness |
| GOV-03-001（`05-smart-kpi-definitions.md` lines 479-539） | **6** | 將上述兩項合併為 Concept Output Labeling Compliance Rate |

Evidence Model 承諾 7 項可觀察 KPI，SMART 定義僅操作化 6 項。1:1 對應關係被打破。

#### Finding KPI-02: MREM 條件數量錯誤（HIGH） — ✅ FIXED

- `08-multi-role-scoring-aggregation.md` lines 509-520：定義 **8** 項條件（MREM-1 ~ MREM-8）
- 同文件 line 766 爭議處理段落：宣稱「依**五**項條件客觀判定」
- Appendix A.4（line 846）：列出 **8** 項條件
- **Line 766 為事實錯誤**，應為「八項」

#### Finding KPI-03: KPI 弱追溯項（LOW） — NOT FIXED（設計選擇，非勘誤）

- Design Governance Coordinator「Process Reminder Timeliness」（GOV-03-001 line 456）：衡量行政流程時效，非直接治理目標
- Pre-Gate Design Support「Rework Reduction Rate」（GOV-03-001 line 501）：事後歸因指標，需主觀判斷

### 4.3 Cycle Rule Conflicts

L2 People 定義 **29 條週期規則**（`09-annual-governance-cycle.md`）。

#### Finding CYCLE-01: 十二月排程密度風險（MEDIUM） — NOT FIXED（流程設計議題，需治理委員會決議）

December 必須容納：Week 1 角色確認、Week 2 AF 判定 + RCW 調整 + 治理活動截止、Week 3 治理文件年審 + 數據凍結 + 6 項年度審查、Week 4 年度目標溝通。任一審查延遲將影響整條瀑布。

#### Finding CYCLE-02: Pre-Gate Design Support 事後調整缺口（MEDIUM） — NOT FIXED（流程設計議題，需治理委員會決議）

- 數據凍結：Dec Week 3（line 132）
- RCW 回溯調整期限：Gate 3 + 60 天（line 282）
- 年度績效結算：Jan Week 4（line 157）
- 若 Gate 3 在 Dec 完成，RCW 調整可能在**結算後**才到期，但無事後修正程序

#### Finding CYCLE-03: Gate 紀錄截止衝突（LOW） — NOT FIXED（流程設計議題，需治理委員會決議）

- Gate 審查紀錄完成期限：5 個工作日（line 233）
- Gate 審查截止：Dec Week 2（line 234）
- 若 Dec Week 2 進行最後一次 Gate 審查，紀錄完成期將落入 Dec Week 3 數據凍結區

---

## Section 5: Layer 3 Compliance

### 5.1 Precondition Compliance Matrix

#### Finding L3-COMP-01: OptionSet 前綴不相容（CRITICAL） — ✅ FIXED

| 文件 | OptionSet 前綴 | 範例 |
|:-----|:--------------|:-----|
| Ch.02（Dataverse 模型） | `807660xxx` | Active=807660000 |
| Ch.05（Flow 實作） | `807660xxx` | Active=807660000, Gate3=807660004 |
| **Ch.07（測試案例）** | **`100000xxx`** | Active=100000000, Gate3=100000004 |

Ch.07 所有測試案例（E2E-001~018、AC-001~008、SA-001~005）均使用 `100000xxx` 前綴。依 Ch.05 建置的系統無法通過 Ch.07 測試。

**證據**：
- `05-core-flows-implementation-runbook.md` lines 7051-7059：OptionSet 表使用 `807660xxx`
- `07-testing-and-acceptance.md` line 656：`gov_currentgate: 100000000`
- `07-testing-and-acceptance.md` line 1234：`100000002 代表 Gate1`
- `07-testing-and-acceptance.md` line 1091：`Planned (100000000)`

#### Finding L3-COMP-02: Counter List 命名不一致（HIGH） — ✅ FIXED

| 文件 | CounterName | 行號 |
|:-----|:-----------|:----:|
| 00B 初始化清單 | `RequestID` | 61 |
| Ch.05 GOV-001 | `ProjectRequest` | 1927 |

依照 00B 初始化建立的 Counter 命名為 `RequestID`，但 GOV-001 查詢 `ProjectRequest`，將因找不到 Counter 而失敗。

#### Finding L3-COMP-03: Flow 數量不一致（MEDIUM） — ✅ FIXED

- Ch.05 Go-live 清單（line 8046）：宣稱「12 條 Flow」
- Ch.05 實際實作：**14 條**（GOV-001, 002, 003, 004, 005, 013A, 013B, 014, 015, 016, 017, 018, 019, 020）

#### Finding L3-COMP-04: 00A 範圍排除 GOV-020（MEDIUM） — ✅ FIXED

- 00A Phase 2 範圍（line 36）：`GOV-001 至 GOV-019`
- Ch.05 實際包含 GOV-020 實作（line 7530）

---

### 5.2 Flow Spec Contradiction Analysis

#### Finding L3-FLOW-01: GOV-020 三重身分（CRITICAL — Layer Violation） — ✅ FIXED

| 層 / 文件 | GOV-020 身分 | 來源 |
|:----------|:------------|:-----|
| L2 SOP-04-part3 | Document Unfreeze Flow（未來開發） | line 2321 |
| L2 SOP-05-ch1 | Document Unfreeze Flow（需另行開發） | line 1475 |
| **L3 Ch.05** | **Document Inventory Parser**（已實作 ~500 行） | line 7530 |
| **L3 Ch.04** | **GOV-020-RiskReassessment**（FORM-005 映射） | line 1222 |

L3 未經 L2 授權即重新定義 GOV-020 用途，構成**層次越權**。若 L2 日後實作原計畫的 Document Unfreeze Flow，將與 L3 現有實作碰撞。

#### Finding L3-FLOW-02: 7 條 Flow 無施工規格（HIGH） — NOT FIXED（Phase 3 開發任務，非文件勘誤）

| Flow ID | L2 定義名稱 | L2 來源 | L3 Ch.05 狀態 |
|:--------|:-----------|:--------|:-------------|
| GOV-006 | Gate Request Cancellation | sop-04-part1:99 | **未實作** |
| GOV-007 | Lite to Full Upgrade | sop-04-part1:101 | **未實作** |
| GOV-008 | Document Unfreeze Exception | sop-04-part1:103 | **未實作** |
| GOV-009 | Project Closure | sop-04-part1:105 | **未實作** |
| GOV-010 | Project Suspension/Resume | sop-04-part1:107 | **未實作** |
| GOV-011 | Gate Rollback Exception | sop-04-part1:109 | **未實作** |
| GOV-012 | Project Archival | sop-04-part1:111 | **未實作** |

Appendix A 將這 7 條列為 Phase 3 建置範圍（lines 85-91），但未提供實作細節。

#### Finding L3-FLOW-03: 測試引用未實作 Flow（CRITICAL） — ✅ FIXED

- Ch.07 E2E-009（line 780）：測試案例引用 `GOV-009`（Project Closure）
- GOV-009 在 Ch.05 中**完全不存在**
- 測試案例指向一個無法建置的 Flow

#### Finding L3-FLOW-04: Appendix A vs Ch.05 矛盾彙總（MEDIUM） — NOT FIXED（Appendix A 已標註「僅供參考」，矛盾屬預期設計）

| 項目 | Appendix A | Ch.05 | 影響 |
|:-----|:----------|:------|:-----|
| RequestID 格式 | GUID-based（line 219） | Counter-based DR-{YYYY}-{####}（line 2009） | 實質差異 |
| GOV-001 並行控制 | Off（line 817） | Required, Parallelism=1（line 229） | 關鍵差異 |
| GOV-005 觸發器 | HTTP Request（line 655） | Power Apps (V2) | 整合方式不同 |
| GOV-004 Risk Owner | 靜態群組 GOV-RiskOwnerHigh/Medium/Low（lines 588-592） | 動態讀取 gov_riskowner 欄位 | 架構差異 |

Appendix A 已標註「僅供參考 — 禁止作為施工依據」（line 1-6），`00-index.md` lines 105-121 確認 Ch.05 為唯一權威。但 Appendix A 的重複內容已與 Ch.05 產生漂移。

---

### 5.3 Appendix/A Warning Audit

#### Finding L3-APPX-01: 警示機制完備（INFO — COMPLIANT）

- Appendix A 標題含「僅供參考 — 禁止作為施工依據」
- Line 16 有明確警示框
- `00-index.md` lines 105-121 建立 Ch.05 為唯一施工權威
- **警示機制正常運作**

#### Finding L3-APPX-02: 重複內容漂移風險（MEDIUM） — NOT FIXED（已有警示機制，風險可接受）

Appendix A 重複了 Ch.05 的以下內容：Gate 審批矩陣、GOV-001~005 I/O Schema、Error Code 定義、OptionSet 值表。已有 4 項實質矛盾（見 L3-FLOW-04）。

---

## Section 6: Cross-File Reference Integrity

### 6.1 Reference Inventory

全體 49 個文件共掃描到以下引用模式：

| 引用類型 | 總數 | 分布 |
|:---------|:----:|:-----|
| GOV-xxx Flow ID | 200+ | 集中在 L2 SOP 與 L3 |
| FORM-xxx 表單 | 80+ | L2 SOP-03/04、L3 Ch.04 |
| ERR-xxx 錯誤碼 | 150+ | L2 SOP-04-part2、L3 Ch.05 |
| Gate 0/1/2/3 | 300+ | 全體 |
| Appendix A-E | 50+ | L1 主文件、L2 SOP |
| 參見/詳見/依據 | 40+ | L2 SOP、L3 |
| SOP-0x | 30+ | L2 SOP 內部互引 |

### 6.2 Dangling References

#### Finding REF-01: GOV-014 身分衝突（CRITICAL） — ✅ FIXED

| 文件 | GOV-014 = | 行號 |
|:-----|:----------|:----:|
| SOP-03-part1 | **Notification Handler** | 64, 88, 100 |
| SOP-04-part1 | **Document Freeze** | 125 |
| SOP-04-part3 | **Document Freeze** | 23 |
| L3 Ch.05 | **Document Freeze** | 610 |

SOP-03-part1 使用**草稿版編號**（GOV-014=Notification Handler），SOP-04 重新編號後 GOV-014=Document Freeze、GOV-015=Notification Handler。SOP-03-part1 **從未更新**。

#### Finding REF-02: FORM-006 身分衝突（CRITICAL） — ✅ FIXED

| 文件 | FORM-006 = | 對應 Flow |
|:-----|:----------|:---------|
| SOP-02 line 560 | **Exception Waiver Request** | GOV-009 |
| SOP-03-part1 line 78 | **Gate Cancellation** | GOV-006 |
| SOP-04-part1 line 165 | **Gate Cancellation** | GOV-006 |
| L3 Ch.04 line 1183 | **GOV-006-GateCancellation** | GOV-006 |

SOP-02 的 FORM-006 映射已過時，其他所有文件一致為 Gate Cancellation。

#### Finding REF-03: MGL 編號對映嚴重分歧（CRITICAL） — ✅ FIXED

| MGL | SOP-01 事件 | SOP-01 GOV | SOP-02 事件 | SOP-02 GOV |
|:---:|:-----------|:-----------|:-----------|:-----------|
| MGL-06 | Gate 3 Risk Acceptance | — | Risk Initial Assessment | — |
| MGL-07 | Gate 3 Approval | — | Document Freeze | — |
| MGL-08 | Document Freeze | GOV-005 | Lite to Full Upgrade | — |
| MGL-09 | Risk Item Creation | GOV-008 | Risk Reassessment | — |
| MGL-10 | Lite to Full Upgrade | GOV-009 | Risk Acceptance | — |
| MGL-12 | Guardrail Monitor | GOV-007 | — | — |

SOP-01 與 SOP-02 的 MGL 編號對映**完全不同**，且 SOP-01 使用 v3.0 Flow 編號（如 GOV-007=Guardrail，應為 GOV-017）。

#### Finding REF-04: SOP-06 懸空引用（HIGH） — ✅ FIXED

- SOP-01 lines 9, 126：引用「SOP-02~06」
- SOP-06 **不存在**

#### Finding REF-05: 「SOP-05 Operational Usage Guide」懸空引用（HIGH） — ✅ FIXED

- SOP-05-ch3-4 lines 1741, 1754：引用「SOP-05 Operational Usage Guide」作為日常操作快速參考
- 此文件**不存在**

#### Finding REF-06: SOP-02 GOV-008 錯誤引用（MEDIUM） — ✅ FIXED

- SOP-02 line 507：`GOV-008 每日自動檢查` 用於 Document Freeze
- GOV-008 = Document Unfreeze Exception（SOP-03/04）
- 正確引用應為 GOV-014（Document Freeze）或 GOV-018（Compliance Reconciler）

#### Finding REF-07: FORM-003 vs FORM-005 編號衝突（MEDIUM） — ✅ FIXED

- SOP-04-part1 line 164：`FORM-005` = Document Upload → GOV-005
- SOP-05-ch2、SOP-01 line 380：`FORM-003` = Document Upload
- 同一表單兩個不同編號

#### Finding REF-08: FORM-008/009 語意漂移（LOW） — NOT FIXED（SOP-05-ch5-6 為 hypothetical scenario，非規範性定義）

- SOP-03/04：FORM-008 = Document Unfreeze、FORM-009 = Project Closure
- SOP-05-ch5-6 line 893：FORM-008 = Add Project Note
- SOP-05-ch5-6 line 1507：FORM-009 = Critical Exception Request
- 表單用途在不同 SOP 中不同

#### Finding REF-09: APPROVAL-003/004 語意漂移（MEDIUM） — NOT FIXED（SOP-01 與 SOP-04 使用不同語意範疇，屬設計選擇）

- SOP-01：APPROVAL-003 = Gate 1 QA Review、APPROVAL-004 = Gate 2 Approval
- SOP-04-part1：APPROVAL-003 = Gate Approval (通用)、APPROVAL-004 = Risk Acceptance
- 語意映射不同

#### Finding REF-10: 04-powerapps-forms.md 引用已棄用文件（MEDIUM） — ✅ FIXED

- Ch.04 lines 279, 284 引用 `appendix/Canvas-Brand-UI-Standard-v1.md`
- Ch.04 line 22 自己宣告 v1.0/v1.1 已棄用，應使用 v1.2
- 引用指向 `deprecated/` 目錄中的文件

### 6.3 Orphan Documents

| 文件 | 層 | 狀態 |
|:-----|:--|:-----|
| `internal-design-request-intake-criteria.md` | L1 | 未被任何其他 L1 文件引用 |
| `appendix/Canvas-Brand-UI-Standard-v1.1.md` | L3 | 已棄用，未被活躍文件引用 |
| `deprecated/Canvas-UI-Governance-Standard-v1.md` | L3 | 已棄用，自包含 |
| `deprecated/Canvas-Brand-UI-Standard-v1.md` | L3 | 已棄用，被 Ch.04 錯誤引用 |

### 6.4 Layer Direction Analysis

| 引用方向 | 偵測結果 |
|:---------|:---------|
| L3 → L2 SOP（正常） | ✅ 發現多處「authority source: SOP-04-v2-Part3」等正向引用 |
| L3 → L1（應透過 L2） | ✅ 未發現直接引用 L1，正確透過 L2 間接引用 |
| L2 → L3（反向依賴） | ✅ 未發現，引用方向正確 |
| L2 People → L2 SOP | ✅ 未發現跨 L2 domain 引用，設計獨立 |

---

## Section 7: Structural Gaps（L2 People）

### 7.1 Missing Artifacts

| 預期文件 | 實際狀態 | 影響 |
|:---------|:---------|:-----|
| RACI 矩陣（獨立文件） | **不存在** | GOV-04-001 AF 判定需 RACI 矩陣作為 30% 輸入來源（`08-multi-role-scoring-aggregation.md` lines 294-303） |
| 獨立詞彙表 | **不存在** | 術語散佈於多個文件，PVF/SPV/RAT 僅在單一文件定義 |
| 升級矩陣 | **不存在** | — |
| 職能矩陣 | **不存在** | — |
| Onboarding 清單 | **不存在** | — |

### 7.2 Terminology Inconsistency

#### Finding PEOPLE-TERM-01: Presales 標籤矛盾（MEDIUM） — ✅ FIXED

- `02-role-responsibility-boundary.md` line 214：BOM 表中 Pre-Gate Design Support 附加「(Presales)」標籤
- 同文件 line 116：明確宣告此角色為「非商務角色、非顧問角色」
- 「Presales」標籤與角色定位矛盾

---

## Remediation Summary

### 修復統計

| Phase | 修改檔案數 | 修復項數 | 說明 |
|:-----:|:---------:|:-------:|:-----|
| 1 | 1 | 1 | L1 RACI 表 Gate 1/3 Approver 腳標 + Engineering Management 角色描述 |
| 2 | 7 | 16 | L2 SOP 層：SOP-01~05 角色/引用/編號全面對齊 |
| 3 | 3 | 3 | L2 People 層：MREM 條件數、Presales 標籤、KPI 數量 |
| 4 | 6 | 8 | L3 落地層：OptionSet 前綴、Counter 名稱、Flow 數量、GOV-020 映射 |
| 5 | 2 | 2 | 補充：SOP-04-part3 GOV-020 預留、SOP-05-ch3-4 懸空引用 |
| **Total** | **17** | **30** | — |

### 不修復項清單（含理由）

| Finding ID | 嚴重度 | 理由 |
|:-----------|:------:|:-----|
| L3-FLOW-02 | HIGH | GOV-006~012 為 Phase 3 開發任務，非文件勘誤 |
| PEOPLE-ROLE-01 | MEDIUM | L2 有權在 L1 框架內擴展角色定義，非越權 |
| L3-ROLE-01 | MEDIUM | PM/DRF/RAA 在 Power Platform 無對應安全群組需求 |
| TERM-01 | MEDIUM | RequestStatus vs GateStatus 屬語意設計議題 |
| TERM-03 | MEDIUM | MGL 不同粒度呈現屬設計選擇 |
| CYCLE-01/02 | MEDIUM | 排程密度/事後調整為流程設計議題，需治理委員會決議 |
| L3-FLOW-04 | MEDIUM | Appendix A 已標註「僅供參考」 |
| L3-APPX-02 | MEDIUM | 已有警示機制，風險可接受 |
| REF-09 | MEDIUM | SOP-01 與 SOP-04 使用不同語意範疇 |
| PEOPLE-ROLE-02 | LOW | 結構缺口，屬未來文件規劃 |
| CYCLE-03 | LOW | 流程設計議題，需治理委員會決議 |
| KPI-03 | LOW | 指標設計選擇，非勘誤 |
| TERM-02 | LOW | Form-Only/First 語意差異微小 |
| TERM-04 | LOW | Governance Lead 慣用簡稱，非錯誤 |
| REF-08 | LOW | SOP-05-ch5-6 為 hypothetical scenario |
| G-01~G-04 | INFO | RACI/Glossary/Escalation/Onboarding 為未來規劃 |
| GATE-L3-01 | INFO | 合規確認 |
| L3-APPX-01 | INFO | 合規確認 |

### 關鍵設計決策

1. **GOV-020 身分**：保留 L3 Ch.05 的 Document Inventory Parser（已實作 ~500 行），L2 SOP-04-part3 更新對齊，原 Document Unfreeze 延至 GOV-021 預留
2. **RACI 表 Approver**：Engineering Management 保留 RACI 表 A 欄（因表格無 Governance Function 獨立欄位），透過腳標註明 Gate 1/3 執行審查權限委任予 System Design Governance Function
3. **風險接受權責**：以 L1 憲法為準（RAA 分級制），SOP-01/SOP-05 全部對齊，System Architect 不再擔任風險接受者

---

## Appendix: Methodology

### Audit Approach

1. **Wave 1（4 parallel agents）**：
   - Agent A：L1 全部 7 個文件（2,257 行）→ 角色/Gate/術語登記表
   - Agent B：L2 SOP 全部 13 個文件（19,450 行）→ 角色/Gate/術語比對
   - Agent C：L2 People 全部 12 個文件（5,259 行）→ KPI/JD/週期審計
   - Agent D：全部 49 個文件跨引用 Grep 掃描

2. **Wave 2（1 sequential agent）**：
   - Agent E：L3 全部 17 個文件（26,622 行）→ 消費 Wave 1 產出執行合規審計

### Evidence Standard

- 每項發現均附帶**文件路徑與行號**
- 行號基於審計當時的文件版本（commit `2f4febb`）
- 引用文字為原文直接引述，未經修改

### Severity Classification

| 級別 | 定義 |
|:-----|:-----|
| CRITICAL | 跨層定義衝突，可能導致系統建置錯誤或合規失敗 |
| HIGH | 單層內重大不一致或懸空引用，影響文件可信度 |
| MEDIUM | 命名漂移或語意不一致，可能造成誤解但不直接導致系統故障 |
| LOW | 過時引用或缺失文件，影響完整性但不影響正確性 |
| INFO | 一致性確認或合規紀錄 |

### File Inventory

**L1 system-design（7 files, 2,257 lines）**:
`system-design-governance.md`, `appendix-a-iec62443-alignment.md`, `appendix-b-raci.md`, `appendix-c-residual-risk-template.md`, `appendix-d-integrated-risk-assessment-templates.md`, `appendix-e-design-request-readiness-guideline.md`, `internal-design-request-intake-criteria.md`

**L2 governance-sop-dataverse（13 files, 19,450 lines）**:
`sop-01-governance-system-overview.md` ~ `sop-05-chapter5-6-exceptions-finality.md`

**L2 system-design-people（12 files, 5,259 lines）**:
`00-index.md` ~ `10-score-usage-rules.md` + `appendix/A-decision-summary-appendix.md`

**L3 project-governance（17 files, 26,622 lines）**:
`00-index.md` ~ `07-testing-and-acceptance.md` + `appendix/` + `deprecated/`
