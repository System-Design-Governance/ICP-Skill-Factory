# Phase 1 Domain Map — 正式獨立審查報告

**審查版本：** R3-REVIEW
**審查日期：** 2026-03-13
**審查對象：** `phase1-domain-map-approved.md` (R2 baseline, 14 domains, 73 subdomains — R2 原誤報 75)
**審查角色：** AI Skill 開發顧問、工程能力架構審查顧問、治理型 Skill Taxonomy Reviewer
**審查依據：** ID01 v1.0、ID02 v1.1、ID03 v1.0、CONVENTIONS.md、SCHEMA.md、ADR-001–005、Phase 2 skill-candidate-inventory.md

---

## 第 1 節｜審查總結

本報告針對 ICP Skill Factory Phase 1 Domain Map（R2 版本）進行獨立正式審查，涵蓋七項結構性檢驗、D14 獨立判定、D10 重新界定、角色治理映射、以及 Phase 2 提取就緒度評估。

R2 版本的核心架構決策——將前置技術工程（D14）從專案工程（D10）中獨立——經交叉比對 ID01 §6.5.1.1（Tendering/Acquisition 階段）、ID03 Table 1（R0 階段正式任務 SSA-PRO-001/002/003）、以及 ICP 組織治理文件中「Pre-Gate Design Support」角色的制度化定位，確認為正確且必要的結構決策。

本審查識別出 3 項結構性缺陷需修正、5 項改善建議、以及 2 項 Phase 2 提取風險。整體判定為：**有條件通過，附帶指定修正項（CONDITIONAL PASS with mandated fixes）**。

R2 版本在修正指定項目後，可作為 Phase 3 Skill Definition 之正式基線。

---

## 第 2 節｜優點

**2.1 生命週期邊界切分精準**

R2 版本以 Gate 0 / 合約簽訂作為 D14 與 D10 的生命週期分界，此決策直接對應 IEC 62443 安全生命週期中 Pre-R0（概念）與 R0–R5（執行）的階段轉換。ID01 §6.5.1.1 明確定義 Tendering/Acquisition 為獨立階段，ID03 Table 1 中 R0 階段指定三項正式任務（SSA-PRO-001 定義招標安全需求、SSA-PRO-002 評估安全規格、SSA-PRO-003 R0 閘門審查），均為 D14 範圍內的技術執行活動。以 Gate 0 作為切分點，避免了「同一 Domain 跨越不同合約狀態」的治理模糊問題。

**2.2 MECE 原則總體遵循度高**

14 個 Level 1 Domain 在功能面基本滿足互斥性：技術執行域（D01–D08）各有明確的工程標的，管理支撐域（D09–D11）功能互補，新興能力域（D12–D13）定位清晰。R2 增加的三條 Boundary Rule（D02.3/D05.5/D07.2 協定分層、D10.2/D11.2 變更管理分層、D10/D14 生命週期分界）有效化解了已識別的重疊風險。

**2.3 四層架構一致性**

Domain → Capability Group → Skill → Atomic Sub-skill 的四層結構在命名規則（CONVENTIONS.md）、Schema 定義（SCHEMA.md §24 fields）、ID 編碼（ADR-004 SK-D{nn}-{nnn}）三方面保持一致，為 Phase 3 Skill Definition 提供穩固的架構基礎。

**2.4 雙語命名與產業對齊**

所有 75 個 Level 2 子領域均具備中英雙語名稱，且專有名詞（SCADA、EMS、DERMS、VPP、HMI、Zone/Conduit 等）保留業界慣用寫法，符合 CONVENTIONS.md §2 命名規範。

**2.5 依賴關係預建**

D14 的正向依賴（D14→D01, D02, D09, D10, D11）與反向依賴（D01, D09, D11→D14）已在 R2 文件中完整記錄，為 Phase 4 Dependency Mapping 預建了結構基礎。此為多數 taxonomy 專案在 Phase 1 不會涵蓋的超前佈局。

---

## 第 3 節｜缺口與風險

### 缺陷 DEF-001：D08.6「系統除役」歸屬不當（嚴重度：中）

**問題描述：** D08.6 系統除役（System Decommissioning）目前歸屬於 D08 TESTING-COMMISSIONING，但系統除役並非測試或試車活動。ID01 §6.5.3 明確將 Decommissioning 定義為生命週期 R5 階段的獨立活動，涵蓋資料保存、媒體消毒、硬體處置等，其性質為營運結束階段的工程管理行為，與 FAT/SAT/Commissioning 的 R3 階段活動本質不同。

**影響：** 若不修正，Phase 3 在 D08 下撰寫除役技能定義時，將面臨生命週期標註矛盾（D08 為 R3 活動，除役為 R5 活動），且 Skill 的 prerequisite 和 dependency 將無法正確連結。

**建議方案：**
- 方案 A（推薦）：將 D08.6 遷移至 D10，新增 D10.5「系統除役與資產處置」，因除役是專案執行後期的技術管理活動，屬 D10 post-contract 範疇。
- 方案 B：保留 D08.6 但重新命名 D08 為 TESTING-COMMISSIONING-DECOMMISSIONING，並更新 Domain Description 以涵蓋完整 R3–R5 範圍。

### 缺陷 DEF-002：D11.6「安全能力管理」歸屬待釐清（嚴重度：低）

**問題描述：** D11.6 安全能力管理（Security Competency Management）目前歸屬 D11 ENGINEERING-GOVERNANCE。此子領域源自 ID03 §5.3.3 之安全能力要求框架，涉及安全專業培訓、資格認定、能力追蹤。問題在於：「安全」能力管理是 D01 OT-CYBERSECURITY 的人員面向，還是 D11 ENGINEERING-GOVERNANCE 的通用治理機制？

**分析：** 若 ICP 未來在 D01 之外還有其他領域需要能力管理（如 D03 電力系統能力認證、D04 保護工程能力認證），則 D11.6 應泛化為「工程能力管理」（Engineering Competency Management），涵蓋所有領域的能力框架。若 D11.6 僅服務於安全領域，則應遷移至 D01。

**建議：** 保留於 D11 但更名為「工程能力管理」，將安全能力作為其第一個實例化案例。此決定應記錄為 ADR-006。

### 缺陷 DEF-003：D12/D13 邊界模糊區域（嚴重度：低）

**問題描述：** D12.3「資料分析與建模」與 D13.2「AI 輔助工程」存在功能重疊的潛在風險。當 AI/ML 技術應用於能源資料分析（如電力負載預測、DER 出力預測），該技能歸屬 D12.3 還是 D13.2？

**建議：** 新增 Boundary Rule 明確切分：D12.3 涵蓋以能源資料為標的的分析建模（含使用 AI/ML 作為工具），D13.2 涵蓋以工程流程為標的的 AI 輔助能力（如 AI 輔助設計審查、自動化文件生成）。標的物不同：D12 的標的是「資料」，D13 的標的是「工程流程」。

### 缺口 GAP-001：缺少「維運工程」能力域（嚴重度：中）

**問題描述：** IEC 62443 R4 階段（Operation & Maintenance）包含大量持續性工程活動：安全監控（已由 D01.4 覆蓋）、補丁管理（D01.5）、安全稽核（D01.3）、變更管理（D10.2），但非安全面的維運工程能力（如系統健康監控、效能優化、預防性維護策略、SLA 管理）目前未有明確歸屬。

**風險評估：** ID01 §6.5.2（R4 階段 O&M Practice）中描述的持續監控、效能基線比對、週期性審查等活動，目前分散於 D01（安全面）、D05（控制系統面）、D08（測試面）。若維運工程能力需求顯著，建議在 Phase 5（Overlap Analysis）中評估是否需新增 D15 OPERATIONS-ENGINEERING，或在 D10 中新增維運技術管理子領域。

**本次處理：** 記錄為 Phase 5 評估項目，不於本次修正中新增 Domain。理由：目前 source documents 的 O&M 內容已由 D01.4/D01.5 和 D08 部分覆蓋，新增 Domain 需更多實務驗證。

### 缺口 GAP-002：D03.4 虛擬電廠與 D05.2 EMS/DERMS 的分界不夠嚴謹（嚴重度：低）

**問題描述：** VPP 架構設計（D03.4）與 DERMS 配置（D05.2）在實務中高度耦合——DERMS 是 VPP 的核心控制平台。目前 D03.4 定位為「電力系統」視角的 VPP 架構，D05.2 定位為「控制系統」視角的 DERMS 配置，但此分界在 Phase 3 定義具體技能時可能產生歸屬爭議。

**建議：** 新增 Boundary Rule：D03.4 涵蓋 VPP 的電力系統面（聚合策略、調度邏輯、市場參與規則），D05.2 涵蓋 VPP 的控制系統面（DERMS 軟體配置、通訊設定、即時控制迴路）。

### 風險 RISK-001：PRAC 來源候選技能缺乏文件驗證（嚴重度：中）

**問題描述：** Phase 2 候選清冊中，99 項（66%）候選技能的 Source 為 PRAC（Practical Engineering Knowledge），意味著缺乏 ID01–ID03 的直接文件依據。其中 D03（全部 10 項）、D04（全部 4 項）、D05（大部分）、D06（全部 6 項）、D12（全部）、D13（全部）完全依賴 PRAC。

**風險評估：** PRAC 候選技能的合理性在概念層面無疑（這些確實是 ICP 工程師的日常工作），但在治理層面缺乏可追溯的文件錨點，可能導致 Phase 3 定義時無法引用規範性依據。

**建議：** Phase 3 優先處理具有 ID01–ID03 文件依據的高信心候選項，同時為 PRAC 候選項建立「領域專家驗證」流程——每項 PRAC 技能須至少獲得一位 ICP 領域工程師的確認簽名。

### 風險 RISK-002：D05 子領域粒度可能不足（嚴重度：低）

**問題描述：** D05 控制系統工程目前有 6 個子領域，但 D05.6「控制策略設計」涵蓋範圍極廣——從 AGC 自動發電控制、VPP 調度策略、到 DERMS 優化演算法，每一項都可能構成獨立子領域。Phase 2 已產生 14 項候選技能，若 Phase 3 展開至 atomic sub-skill 層級，D05.6 可能產生大量細粒度技能。

**建議：** 此為觀察性風險，不需於 Phase 1 修正。建議在 Phase 3 處理 D05 時，評估是否需將 D05.6 拆分為「基礎控制策略」與「進階優化策略」兩個子領域。

---

## 第 4 節｜角色治理影響

### 4.1 ID03 角色定義與 Domain 映射

ID03 §5.3.1–§5.3.2 定義了 18 個專案安全保證角色。以下分析各角色的主要 Domain 映射：

| 角色代碼 | 角色名稱 | 主要 Domain | 次要 Domain | 分析說明 |
|---------|---------|-----------|-----------|---------|
| PM | Project Manager | D10 | D11 | 專案技術管理，變更管理、技術協調 |
| PQM | Project Quality Manager | D11 | D08 | 品質管控（D11.3）、設計審查（D11.1） |
| PJSC | Project Security Coordinator | D01 | D11 | 安全架構、合規稽核、安全治理 |
| PJS | Project Security Specialist | D01 | — | 安全技術執行專責 |
| PCM | Configuration Manager | D01 | D09 | 安全加固與組態管理（D01.5）、文件版控（D09.4） |
| RQM | Requirements Manager | D10, D14 | D09 | D14.1（前置需求釐清）→ D10.1（專案需求管理） |
| SYS | System Engineer | D02 | D01, D07, D14 | 系統架構設計主責，同時涉及前置概念架構（D14.3） |
| DES | Designer | D02, D05 | D06 | 系統設計與控制系統設計 |
| DEV | Developer | D05 | D13 | 控制系統程式設計、工程工具開發 |
| TL | Test Leader | D08 | D01 | 測試規劃與執行 |
| AN | Analyst | D01 | D03 | 風險評估、威脅建模 |
| PR | Peer Reviewer | D11 | ALL | 設計審查、品質驗證（跨域角色） |
| IMP | Implementer | D05, D06, D07 | — | 系統實作、盤櫃安裝、整合 |
| INT | Integrator | D07 | D05, D02 | 系統整合主責 |
| TST | Tester | D08 | D01 | FAT/SAT 執行 |
| VER | Verifier | D08, D11 | D01 | 獨立驗證 |
| VAL | Validator | D08, D11 | — | 確認驗證 |
| CSA | Cybersecurity Advisor | D01 | D14, D11 | 安全顧問，提供前置安全分類輸入（D14.6） |

### 4.2 關鍵發現

**發現 RF-001：RQM 角色橫跨 D14/D10 邊界**

Requirements Manager（RQM）在 ID03 Table 1 中同時出現於 R0 階段（需求定義）和 R1–R4 階段（需求追蹤）。R2 版本的 D14/D10 切分正確反映了 RQM 角色的跨階段特性：D14.1 需求釐清（Pre-Gate 0）→ D10.1 專案需求管理（Post-Contract）。這強化了 D14 獨立的合理性——RQM 的前置工作產出成為後續專案的輸入基線。

**發現 RF-002：SYS 角色自然跨越 D02/D14 邊界**

System Engineer（SYS）在 ID01 Table.1 中負責系統架構設計（D02 主責），但同時在 ID01 §6.5.1.1 的 Tendering/Acquisition 階段承擔概念架構工作。D14.3（可行性評估與概念架構）正確捕捉了 SYS 在前置階段的技術執行角色。

**發現 RF-003：CSA 角色支持 D14.6 的設立**

Cybersecurity Advisor（CSA）在 ID03 §5.3.1 中被定義為提供安全分類輸入的諮詢角色，其主要活動包括初步安全等級評估——這正是 D14.6 前置風險評估的核心技能之一。CSA→D14.6 的映射為 D14.6 子領域的設立提供了角色治理層面的獨立證據。

**發現 RF-004：缺少「Pre-Gate Design Support」的正式角色對應**

ID01–ID03 中未出現「Pre-Gate Design Support」或「Concept System Architect」的正式角色名稱。R2 版本在 D14 描述中使用的「Concept System Architect / Feasibility Owner」為推導性角色標籤。此角色在 ICP 內部治理文件中已制度化，但在 ID01–ID03 source documents 中，對應的最接近角色是 SYS（System Engineer）在 R0 階段的職責範圍。

**建議：** Phase 3 在定義 D14 技能時，應在 SCHEMA.md 的 `primary_roles` 欄位中使用 ID03 的角色代碼（SYS, RQM, CSA, AN），並在 `notes` 欄位中註記 ICP 內部的對應角色名稱。這確保了可追溯性同時保留了實務對齊。

---

## 第 5 節｜D14 判定

### 5.1 選項比較

| 評估面向 | 選項 A：保留在 D10 | 選項 B：獨立為 D14 |
|---------|------------------|------------------|
| 生命週期對齊 | ✗ D10 橫跨 Pre-Gate 到 Post-Project，合約狀態不一致 | ✓ D14 = Pre-Gate 0 → Gate 0，D10 = Post-Contract → Closure，各自完整 |
| 角色對齊 | ✗ Pre-Gate 的 Concept Architect 與 Post-Contract 的 Project Engineer 是不同角色定位 | ✓ D14 的主要角色（SYS@R0, RQM@R0, CSA）與 D10 的主要角色（PM, RQM@R1+）明確區分 |
| 交付物性質 | ✗ 可行性報告、概念架構 vs. 變更請求、專案追蹤——混在同一 Domain 降低治理精度 | ✓ D14 交付物為決策支援文件（Gate 0 package），D10 交付物為專案執行文件 |
| 文件證據 | — ID01 §6.5.1.1 定義 Tendering/Acquisition 為獨立階段 | ✓ ID03 Table 1 R0 有三項正式任務，ID01 §6.5.1.1 明確獨立 |
| 技能規模 | 選項 A 下 D10 有 14+ 候選項跨越兩個生命週期階段 | ✓ 分拆後 D14 = 16 項、D10 = 5 項，各自聚焦 |
| MECE 影響 | ✗ D10 內部不互斥（Pre-Gate 需求分析 vs. Post-Contract 需求管理 功能重疊） | ✓ 互斥性通過 Gate 0 邊界保證 |
| 組織治理對齊 | ✗ ICP 已將 Pre-Gate Design Support 制度化為獨立角色，放入 D10 與治理實務矛盾 | ✓ D14 直接對應 ICP 內部已制度化的 Pre-Gate 技術執行角色 |
| 遷移成本 | ✓ 零遷移成本 | △ 需遷移 8 項候選技能、重新編號、更新依賴 |

### 5.2 判定結論

**判定：選項 B — 獨立為 D14，確認 R2 決策正確。**

理由摘要：

第一，生命週期證據充分。ID01 §6.5.1.1 將 Tendering/Acquisition 定義為 Secure Development Lifecycle 的獨立階段（Pre-R0 / R0 前段）。ID03 Table 1 在 R0 階段指定三項正式安全保證任務（SSA-PRO-001/002/003），證明 Pre-Gate 階段並非臨時性活動，而是具有正式任務編號、指定角色、明確交付物的制度化工程階段。

第二，角色治理證據充分。ICP 內部治理文件已將「Pre-Gate Design Support」制度化為技術執行角色（非銷售支援角色）。在 ID03 的角色框架中，SYS（System Engineer）在 R0 階段的職責與 D14.3 可行性評估與概念架構直接對應；RQM 在 R0 階段的職責與 D14.1 需求釐清直接對應；CSA 的安全分類輸入與 D14.6 前置風險評估直接對應。

第三，若 Pre-Gate Design Support 已在組織治理中被制度化為獨立的技術執行角色，則不能僅以「D10 部分覆蓋」為由拒絕 D14 獨立。此角色的制度化意味著它具有獨立的能力發展路徑、績效指標、與訓練需求，這些都需要獨立 Domain 層級的技能分類來支撐。

---

## 第 6 節｜D14 定義與子領域

### 6.1 R2 版本 D14 子領域品質評估

| D14 子領域 | 品質評分 | 評語 |
|-----------|---------|------|
| D14.1 需求釐清與範圍框定 | ★★★★☆ | 定義清楚，與 D10.1 的邊界明確。缺少對「需求衝突解決」的明確提及。 |
| D14.2 現場勘查與技術探勘 | ★★★★★ | 定義完整，涵蓋實體勘查、既有設施盤點、環境限制、棕地整合。 |
| D14.3 可行性評估與概念架構 | ★★★★☆ | 涵蓋技術可行性、概念架構、技術選型、POC 設計。建議補充「方案比較分析」能力。 |
| D14.4 成本基礎與 BOM 工程 | ★★★★★ | 定義精確，涵蓋工程級成本估算、初步 CBOM、人時基線、供應商報價、成本風險。 |
| D14.5 基線清冊準備 | ★★★☆☆ | 與 D01.5（安全加固與組態管理的資產清冊面向）和 D14.2（既有設施盤點）有重疊疑慮。需進一步區分。 |
| D14.6 前置風險評估與 Gate 0 輸入包 | ★★★★★ | 整合性子領域，將 D14.1–D14.5 的產出彙整為 Gate 0 決策包。定義清晰。 |

### 6.2 D14.5 調整建議

D14.5「基線清冊準備」與 D14.2「現場勘查與技術探勘」存在功能重疊：D14.2 已包含「existing infrastructure inventory」，D14.5 再定義「preliminary asset inventory, existing system baseline documentation」造成冗餘。

**建議方案：**
- 將 D14.5 重新定位為「利害關係人分析與介面點清冊」（Stakeholder Analysis & Interface Enumeration），涵蓋：利害關係人識別與期望對齊、跨系統介面點列舉、既有系統能力評估（legacy capability assessment）、整合限制條件匯總。
- 此調整將 D14.5 從「資產清冊」（與 D14.2 重疊）轉為「人與系統介面」的整理，補充了原 D14 缺少的利害關係人管理面向。
- 原 D14.5 中的「既有系統基線文件」併入 D14.2。

### 6.3 建議修正後的 D14 子領域

| ID | 子領域名稱 | 說明 |
|----|----------|------|
| D14.1 | 需求釐清與範圍框定 | 客戶/利害關係人需求提取、範圍邊界定義、需求衝突解決、初步需求追溯 |
| D14.2 | 現場勘查與技術探勘 | 實體場址評估、既有基礎設施盤點（含資產基線）、環境限制、棕地整合評估 |
| D14.3 | 可行性評估與概念架構 | 技術可行性分析、概念架構設計、方案比較分析、技術選型、POC 設計、初步 Zone/Conduit 概念 |
| D14.4 | 成本基礎與 BOM 工程 | 工程級成本估算、初步 CBOM、人時基線、供應商報價協調、成本風險餘裕分析 |
| D14.5 | 利害關係人分析與介面清冊 | 利害關係人識別與期望對齊、跨系統介面點列舉、既有系統能力評估、整合限制條件匯總 |
| D14.6 | 前置風險評估與 Gate 0 輸入包 | 初步 HLCRA、安全分類輸入、風險導向範圍建議、Gate 0 決策包組裝 |

---

## 第 7 節｜D10 重新界定

### 7.1 R2 版本 D10 評估

R2 將 D10 重新界定為「post-acceptance project technical management」，保留 4 個子領域：D10.1 專案需求管理、D10.2 變更管理、D10.3 技術協調、D10.4 合約技術管理。此結構清晰且聚焦。

### 7.2 DEF-001 修正方案：D08.6 遷移至 D10

如第 3 節 DEF-001 所述，系統除役（D08.6）應遷移至 D10。實施後，D10 結構調整為：

| ID | 子領域名稱 | 說明 |
|----|----------|------|
| D10.1 | 專案需求管理 | 合約後需求追蹤、分解、追溯、範圍基線維護 |
| D10.2 | 變更管理 | 設計變更評估、影響分析、核准流程 |
| D10.3 | 技術協調 | 跨部門/供應商技術協調、RFI 管理 |
| D10.4 | 合約技術管理 | 技術範圍追蹤、交付物驗收標準、技術爭議解決 |
| D10.5 | 系統除役與資產處置 | 系統退役規劃、資料保存、媒體消毒、硬體處置、R5 生命週期管理 |

**影響：** D08 縮減為 5 個子領域（D08.1–D08.5），D10 擴充為 5 個子領域。對應的候選技能遷移：原 D08.6 相關候選技能（若有）應重新編號至 SC-D10-006+。

### 7.3 D10 Boundary Rule 更新

修正後的 D10/D14 邊界規則：
- D14 操作範圍：Pre-Gate 0 → Gate 0（合約簽訂前的技術執行）
- D10 操作範圍：Post-Contract Kickoff → Project Closure including Decommissioning（合約後專案技術管理，含系統除役）
- 生命週期覆蓋：D14 = Pre-R0, R0 / D10 = R1–R5

---

## 第 8 節｜修正版 Domain Map

以下為整合本審查所有建議修正後的 Domain Map（R3 Candidate）。標記 ★ 為本次新增修正，標記 ▲ 為 R2 已有修正。

### Level 1 — 14 Engineering Skill Domains

| # | Domain ID | Domain Name | 說明 |
|---|-----------|-------------|------|
| D01 | OT-CYBERSECURITY | OT 資訊安全 | OT/ICS 安全架構、風險評估、合規、防護 |
| D02 | SYSTEM-ARCHITECTURE | 系統架構設計 | OT/IT 系統架構、網路拓撲、介面設計 |
| D03 | POWER-SYSTEM | 電力系統工程 | 電力系統分析、設計、模擬、再生能源整合 |
| D04 | PROTECTION | 保護工程 | 保護協調、繼電器工程、故障分析 |
| D05 | CONTROL-SYSTEM | 控制系統工程 | SCADA、EMS、DERMS、VPP 設計配置與調校 |
| D06 | PANEL-ENGINEERING | 盤櫃工程 | 電氣盤面設計、配線、端子規劃 |
| D07 | INTEGRATION | 系統整合工程 | 跨系統介面整合、協定橋接、資料交換 |
| D08 | TESTING-COMMISSIONING | 測試與試車 | ★ FAT、SAT、試車、效能測試（D08.6 除役遷出至 D10） |
| D09 | ENGINEERING-DOCS | 工程文件管理 | 技術文件、設計報告、文件治理 |
| D10 | PROJECT-ENGINEERING | 專案工程 | ▲★ 合約後專案技術管理：需求追蹤、變更管理、技術協調、合約技術管理、系統除役 |
| D11 | ENGINEERING-GOVERNANCE | 工程治理 | 流程標準化、品質管控、設計審查、知識管理 |
| D12 | DATA-PLATFORM | 能源資料平台 | 能源資料擷取、儲存、分析、視覺化 |
| D13 | ENGINEERING-AUTOMATION | 工程自動化 | 工程自動化工具、AI 輔助設計、CI/CD |
| D14 | PRE-GATE-ENGINEERING | 前置技術工程 | ▲ Pre-Gate 0 → Gate 0 技術執行 |

### Level 2 子領域修正摘要

| 修正項目 | 修正內容 | 來源 |
|---------|---------|------|
| D08.6 遷移 | D08.6 系統除役 → D10.5 系統除役與資產處置 | DEF-001 |
| D11.6 更名 | 安全能力管理 → 工程能力管理 | DEF-002 |
| D14.1 補充 | 新增「需求衝突解決」 | §6.2 |
| D14.3 補充 | 新增「方案比較分析」 | §6.2 |
| D14.5 重定位 | 基線清冊準備 → 利害關係人分析與介面清冊 | §6.2 |
| 新增 Boundary Rule | D12.3/D13.2 邊界：標的物原則（資料 vs. 流程） | DEF-003 |
| 新增 Boundary Rule | D03.4/D05.2 邊界：VPP 電力面 vs. 控制面 | GAP-002 |

### 修正後統計

| 指標 | R2 | R3 Candidate | 變動 |
|------|-----|-------------|------|
| Level 1 Domains | 14 | 14 | — |
| Level 2 Subdomains | ~~75~~ 73 | 73 | ±0 net（D08 −1, D10 +1, D14.5 重定位）；R2 原誤報 75 |
| Boundary Rules | 4 | 6 | +2 |
| ADRs | 5 | 6 (+ ADR-006 工程能力管理) | +1 |

---

## 第 9 節｜前置修正清單

以下為本審查報告所產出之修正事項，分為「必須修正」（Phase 3 進入前完成）和「建議修正」（Phase 3 中完成或在後續 Phase 處理）。

### 必須修正（Mandatory Fixes）

| 修正 ID | 對應缺陷 | 修正內容 | 影響範圍 | 修正檔案 |
|---------|---------|---------|---------|---------|
| FIX-001 | DEF-001 | D08.6 遷移至 D10.5，D08 更新為 5 個子領域，D10 更新為 5 個子領域 | phase1-domain-map-approved.md, skill-candidate-inventory.md | 結構變更 |
| FIX-002 | DEF-002 | D11.6 更名為「工程能力管理」，新增 ADR-006 記錄決策 | phase1-domain-map-approved.md, CHANGELOG.md, ADR-006 | 命名變更 |
| FIX-003 | §6.2 | D14.5 重定位為「利害關係人分析與介面清冊」，合併原資產基線功能至 D14.2 | phase1-domain-map-approved.md, skill-candidate-inventory.md | 子領域定義變更 |

### 建議修正（Recommended Fixes）

| 修正 ID | 對應缺陷 | 修正內容 | 建議時間點 |
|---------|---------|---------|----------|
| REC-001 | DEF-003 | 新增 D12.3/D13.2 Boundary Rule（標的物原則：資料 vs. 流程） | Phase 3 啟動前 |
| REC-002 | GAP-002 | 新增 D03.4/D05.2 Boundary Rule（VPP 電力面 vs. 控制面） | Phase 3 啟動前 |
| REC-003 | GAP-001 | 在 Phase 5 評估維運工程能力域需求 | Phase 5 |
| REC-004 | RISK-001 | 建立 PRAC 候選技能專家驗證流程 | Phase 3 |
| REC-005 | RISK-002 | 在 Phase 3 評估 D05.6 是否需拆分 | Phase 3 |
| REC-006 | §6.2 | D14.1 補充「需求衝突解決」、D14.3 補充「方案比較分析」 | Phase 3 啟動前 |
| REC-007 | RF-004 | Phase 3 D14 技能定義中 primary_roles 使用 ID03 角色代碼 | Phase 3 |

---

## 第 10 節｜最終判定

### 判定結論

**有條件通過，附帶指定修正項（CONDITIONAL PASS with mandated fixes）**

### 判定理由

R2 版本的 Domain Map 在核心架構層面是正確的：14 個 Level 1 Domain 覆蓋了 ICP 工程能力的完整範圍，D14 的獨立設立有充分的生命週期證據和角色治理證據支持，四層架構的一致性良好，ID 編碼系統穩健。

然而，審查識別出三項必須修正的結構缺陷（FIX-001 至 FIX-003），若不修正將導致 Phase 3 產出不一致：D08.6 系統除役的歸屬錯誤會造成生命週期標註矛盾，D11.6 的命名過於狹隘將限制能力管理框架的擴展，D14.5 與 D14.2 的重疊將在候選技能歸屬時產生爭議。

### 執行要求

三項必須修正（FIX-001, FIX-002, FIX-003）應於 Phase 3 Skill Definition 啟動前完成，並更新以下檔案：

1. `01-domain-map/phase1-domain-map-approved.md` — 反映 D08、D10、D11、D14 子領域修正
2. `02-skill-candidates/skill-candidate-inventory.md` — 反映候選技能遷移（D08.6 → D10.5 相關項）
3. `00-governance/CHANGELOG.md` — 記錄 CHG-011 至 CHG-014
4. `00-governance/decisions/ADR-006.md` — 工程能力管理通用化決策
5. `00-governance/CONVENTIONS.md` — 新增 D12.3/D13.2 和 D03.4/D05.2 Boundary Rules

完成上述修正後，R3 版本即可作為 Phase 3 Skill Definition 之正式基線，無需再次全面審查。

---

*審查報告結束 — 2026-03-13*
*審查者：AI Skill 開發顧問 / 工程能力架構審查顧問 / 治理型 Skill Taxonomy Reviewer*
