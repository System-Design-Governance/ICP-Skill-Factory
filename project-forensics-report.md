# ICP Skill Factory 鑑識報告

**日期:** 2026-03-13  
**範圍:** `icp-skill-factory` 根目錄與主要治理/技能文件  
**分析方式:** 目錄盤點、關鍵文件交叉比對、實體產物計數、一致性檢查

---

## 1. 執行摘要

本目錄目前不是一般軟體程式碼庫，而是一個以治理文件、技能分類、技能定義與來源證據為核心的知識工程專案。專案名稱為 **ICP Skill Factory**，目的是建立能源系統工程領域的權威技能治理系統，供人員治理、技能盤點、AI agent 技能選擇與後續自動化編排使用。

就目前狀態判斷：

- **Phase 1 Domain Map** 已完成
- **Phase 2 Skill Candidates** 已完成
- **Phase 3 Skill Definitions** 已進入執行，但仍屬早中期
- **Phase 4~7** 尚未真正啟動，仍停留在 TODO 規劃階段

本次鑑識也發現數個重要現象：

- 根目錄 **不是 git repository**，缺少版本歷史可供時間序追溯
- `README.md`、`repo-bootstrap-summary.md`、`phase3-execution-plan.md` 與實際檔案狀態 **存在同步落差**
- Phase 3 的實際產物數量 **高於 README 與執行計畫中的敘述**
- 已 authored skill definitions 整體品質良好，但已出現 **欄位完整性、placeholder 殘留、批次追蹤不同步** 等治理問題
- 來源治理層級已從單純 PDF 抽取，升級為 **Tier 1 Governance > Tier 2 Exemplar > Tier 3 Contextual** 的權威體系
- 終端讀取時出現明顯 **中文亂碼/編碼顯示問題**

---

## 2. 專案目的判讀

根據 `README.md`、`00-governance/skill-governance-workplan.md`、`00-governance/SCHEMA.md` 與各 phase 文件，本專案的核心目的如下：

1. 建立能源系統工程領域的完整技能架構
2. 將技能以可治理的方式定義為標準化物件
3. 為每個技能建立結構化 metadata、邊界、依賴、可驗收條件與來源追溯
4. 支援 AI agent 在未來進行技能選擇、鏈接、依賴推理與自動化協作
5. 為組織後續的能力治理、訓練規劃、職能分工與演進管理建立單一真實來源

換句話說，這不是單純的文件整理專案，而是 **Skill Governance System** 的建模與實作專案。

---

## 3. 目錄結構鑑識

### 3.1 根目錄主體

根目錄主要由以下區塊構成：

- `00-governance/`：命名規範、schema、決策紀錄、工作計畫、變更紀錄
- `01-domain-map/`：Phase 1 領域分類與正式核准版本
- `02-skill-candidates/`：Phase 2 候選技能清單與抽取方法
- `03-skill-definitions/`：Phase 3 技能定義模板、執行計畫與 registry
- `04-dependency-map/`：Phase 4 依賴映射 TODO
- `05-conflict-analysis/`：Phase 5 衝突分析 TODO
- `06-refactoring/`：Phase 6 重構 TODO
- `07-evolution/`：Phase 7 演進治理 TODO
- `source-documents/`：來源 PDF、治理文庫與參考材料

### 3.2 結構特徵

此結構具有典型的「分 phase 治理型知識工廠」特徵：

- 先定義 taxonomy，再抽取 candidate，再逐步 authoring
- 後續將以 dependency、conflict、refactoring、evolution 完成全生命周期治理
- `00-governance/` 扮演 cross-cutting governance layer

### 3.3 根目錄附帶歷史與快照文件

根目錄尚保留多個 legacy / bootstrap / summary 類文件，例如：

- `repo-bootstrap-summary.md`
- `skill-factory-deliverable.md`
- `phase1-skill-domain-map.md`
- `phase1-revision-r2.md`
- `skill-governance-workplan.md`
- `skill-governance-workplan-zh.md`

這代表此目錄同時保存了：

- 初始拆包成果
- 後續 phase 化治理成果
- 部分尚未完全清理的歷史快照

---

## 4. 來源資料與權威層級

### 4.1 主要來源類型

`source-documents/` 內同時存在三種來源：

1. **Dummy Project / Exemplar PDF**
   - ID04 ~ ID14
   - 主要提供 deliverable 格式、樣板與工程實例

2. **組織程序與政策文件**
   - ID21 ~ ID25
   - 提供訓練、採購、資產、事件管理等程序脈絡

3. **治理文庫**
   - `system-design/`
   - `system-design-people/`
   - `project-governance/`

### 4.2 R5 的關鍵升級

`00-governance/CHANGELOG.md` 顯示專案在 R5 已建立明確的來源權威順序：

- Tier 1: Governance
- Tier 2: Exemplar
- Tier 3: Contextual

這是本專案的重要成熟訊號。它表示：

- skill factory 不再只是從 PDF 做 capability extraction
- 而是開始以治理制度作為最高優先來源
- 當 dummy exemplar 與治理文件衝突時，以治理文件為準

### 4.3 治理來源的角色

觀察 manifest 可知：

- `system-design/` 是 System Design Governance 主文庫
- `system-design-people/` 是角色、JD、KPI、責任邊界文庫
- `project-governance/` 看起來是一個成熟治理案例與鑑識參考來源

其中 `system-design/` 與 `system-design-people/` 對本 skill factory 的直接影響最強，因為它們被明確標記為治理權威來源。

---

## 5. 當前進度判讀

### 5.1 Phase 1: Domain Map

狀態：**完成**

依據：

- `01-domain-map/phase1-domain-map-approved.md`
- `00-governance/CHANGELOG.md`

目前基線：

- 14 個 domains
- 73 個 subdomains
- 10 條 boundary rules
- 已納入 R5 治理補強

### 5.2 Phase 2: Skill Candidate Extraction

狀態：**完成**

依據：

- `02-skill-candidates/skill-candidate-inventory.md`
- `00-governance/CHANGELOG.md`

目前基線：

- 173 pre-normalization
- 171 post-normalization
- 已含 H / H+ / M / L confidence 分級
- 已納入 Tier 1/Tier 2/Tier 3 來源標註

### 5.3 Phase 3: Skill Definition Authoring

狀態：**進行中**

依據：

- `03-skill-definitions/phase3-execution-plan.md`
- `03-skill-definitions/registry/`
- `00-governance/SCHEMA.md`

目前觀察到：

- schema 已升為 **27 fields**
- template 已升級至 v1.1.0
- 存在 golden example：`SK-D01-001.md`
- registry 目前實際已有 **18 份** skill definition

實際存在的 skill 檔案包括：

- D01: `001, 005, 006, 007, 013, 016, 019, 020, 021, 022, 023, 024`
- D02: `004, 011`
- D08: `001, 004, 005`
- D09: `002`

### 5.4 Phase 4~7

狀態：**尚未啟動**

依據：

- `04-dependency-map/TODO.md`
- `05-conflict-analysis/TODO.md`
- `06-refactoring/TODO.md`
- `07-evolution/TODO.md`

目前尚未發現正式 deliverable，仍停留在規劃與待辦層。

---

## 6. 已 Authored Skills 鑑識級審查

### 6.1 審查範圍

本次針對 `03-skill-definitions/registry/` 內目前所有已 authored skill files 進行結構與品質審查。

實際檔案數量：**18**

涵蓋 domain：

- D01：12 份
- D02：2 份
- D08：3 份
- D09：1 份

未見已落地 skill 的 domain：

- D03, D04, D05, D06, D07, D10, D11, D12, D13, D14

此結果代表目前 registry 明顯偏向：

- OT cybersecurity
- architecture input / documentation
- acceptance testing

也就是優先建了「安全治理主線」上的前置與關鍵 gate skills。

### 6.2 覆蓋率判讀

根據 Phase 2 inventory，候選 skill 總數為 **171**。目前已 authored **18** 份，約為：

- **10.5%** 的整體覆蓋率

若以 `phase3-execution-plan.md` 的 Stage 1 H+ 路徑判斷，目前進度為：

- Batch 0 完成：Golden Example
- Batch 1 完成
- Batch 2 完成
- Batch 3 完成
- Batch 4 部分完成

Batch 4 計畫中原列 4 項：

- `SK-D08-005`
- `SK-D09-002`
- `SK-D11-011`
- `SK-D11-012`

其中目前實際只看得到前兩項，`SK-D11-011` 與 `SK-D11-012` 尚未出現在 registry。這表示 Batch 4 應標示為 **PARTIAL / IN PROGRESS**，而非 pending。

### 6.3 結構完整性審查

依 template，完整 skill definition 應包含：

- Metadata
- Description
- Inputs
- Outputs
- Tools
- Standards
- IEC 62443 Lifecycle Stages
- Roles
- Dependencies
- Automation Potential
- Acceptance Criteria
- Estimated Effort
- Composition Patterns
- Source Traceability

本次檢查結果：

- **17/18** 份 skill 檔案具有 `Automation Potential` 章節
- **1/18** 缺少該章節：`SK-D01-001.md`
- **18/18** 份 skill 檔案都有 `Dependencies`
- **18/18** 份 skill 檔案都有 `Acceptance Criteria`
- **18/18** 份 skill 檔案都有 `Composition Patterns`
- **18/18** 份 skill 檔案都有 `Source Traceability`
- **18/18** 份 skill 檔案都具備 6 條 acceptance criteria

這裡最值得注意的是：

- `SK-D01-001.md` 被標示為 golden example
- 但 golden example 自身卻缺少 `Automation Potential`

這是高優先的治理問題，因為它會直接削弱 template benchmark 的可信度。

### 6.4 Placeholder / Promotion 一致性審查

依 `00-governance/CONVENTIONS.md`，Phase 3 允許先用 `SC-*` placeholder，待 skill promotion 後再回填為 `SK-*`。

本次檢查到：

- **17/18** 份 skill 檔含有 `SC-*` placeholder
- 總 placeholder 引用次數：**86**

這本身不一定是錯，因為很多依賴目標尚未 authoring。

但其中有一部分是 **已經 promotion 成功，卻仍未回填的陳舊 placeholder**。已確認的例子包括：

- `SK-D01-001.md` 仍引用 `SC-D01-005`, `SC-D01-006`, `SC-D02-004`
- `SK-D08-001.md` 仍引用 `SC-D09-002`
- `SK-D08-004.md` 仍引用 `SC-D08-005`
- `SK-D08-005.md` 仍引用 `SC-D09-002`
- `SK-D01-019.md`、`SK-D01-020.md`、`SK-D01-021.md`、`SK-D01-022.md`、`SK-D01-023.md` 之間存在多個已 authored skill 仍以 `SC-*` 互相引用的情況

已確認至少有以下 promotion 後未回填的配對：

- `SC-D01-001` -> `SK-D01-001`
- `SC-D01-005` -> `SK-D01-005`
- `SC-D01-006` -> `SK-D01-006`
- `SC-D01-019` -> `SK-D01-019`
- `SC-D01-020` -> `SK-D01-020`
- `SC-D01-021` -> `SK-D01-021`
- `SC-D01-022` -> `SK-D01-022`
- `SC-D01-023` -> `SK-D01-023`
- `SC-D02-004` -> `SK-D02-004`
- `SC-D08-005` -> `SK-D08-005`
- `SC-D09-002` -> `SK-D09-002`

這代表目前 registry 的 cross-reference 尚未完成批次 promotion 清理。若現在直接進入 Phase 4，自動抽 dependency graph 時很容易把同一 skill 當成兩個節點。

### 6.5 品質成熟度判讀

從抽樣閱讀 `SK-D01-001.md`、`SK-D01-005.md`、`SK-D01-024.md`、`SK-D02-004.md`、`SK-D08-005.md`、`SK-D09-002.md` 的內容來看，目前 skill files 有以下優點：

- scope boundary 寫得相對清楚
- inputs / outputs 與 gate 產物有實質連結
- acceptance criteria 具可觀察性
- estimated effort 已能支援後續估工或 CBOM 類用途
- source traceability 不只是列文件名，而是有 section / exemplar / governance 層級交叉引用
- role assignment 已開始納入 GOV-SDP 角色體系

這表示目前的 authored skills 不是簡短詞條，而是接近可執行規格的 skill definition。

### 6.6 主要缺陷與風險

本次 skill 層審查的主要發現如下：

1. **Golden Example 缺欄位**
   - `SK-D01-001.md` 缺少 `Automation Potential`
   - 影響模板 benchmark 的權威性

2. **Promotion 後交叉引用未回填**
   - 多份 skill 仍引用已 promotion 的 `SC-*`
   - 會污染未來 dependency mapping 與 graph 分析

3. **Batch 追蹤落後實況**
   - execution plan 未如實反映 registry 現況
   - 容易造成人工作業與自動化統計錯位

4. **Domain 覆蓋高度集中**
   - 18 份 skill 幾乎集中在 D01/D02/D08/D09
   - 其餘 domain 尚未形成最小代表集
   - 這會讓後續 dependency mapping 偏向資安主線，而缺少跨領域平衡

5. **中文內容顯示層不穩**
   - skill 檔中 `skill_name_zh` 等內容在不同讀取方式下有時正常、有時亂碼
   - 代表目前編碼處理不夠穩定，對審閱與後續處理不利

### 6.7 Skill Registry 綜合判斷

目前 skill registry 的品質判讀可以概括為：

- **內容深度：高**
- **結構完整度：中高**
- **治理一致性：中**
- **覆蓋率：低**

也就是說，單一 skill 的寫作品質已經具備良好基礎，但 registry 作為「整體治理系統」仍處於 early-scale 階段，尤其需要補上：

- promotion 後 cross-reference 清理
- 單一進度板
- 最小跨 domain 覆蓋
- golden example 修正

### 6.8 四大能力分類審查

本次額外針對你關心的四種分類進行審查：

1. 執行能力
2. 設計能力
3. 治理能力
4. 文件化能力

#### 結論摘要

**目前 repo 尚未正式做到這四大類的制度化分類，但已有部分能力可被對應到這四類。**

也就是說：

- **不是完全沒有**
- **但也不是已經明確建成**

目前真正被制度化的分類，不是四大類，而是 `00-governance/CONVENTIONS.md` 中定義的 **10 種 skill type taxonomy**：

- Analysis
- Design
- Engineering
- Testing
- Documentation
- Management
- Verification
- Governance
- Integration
- Operations

這代表現在的分類粒度，比四大類更細，也更偏向工程作業語意。

#### 是否有明文化四大類

在本 repo 主治理規範中，並**沒有**找到以下四類被明確列為正式 taxonomy：

- 執行能力
- 設計能力
- 治理能力
- 文件化能力

唯一接近的訊號，是在 `source-documents/system-design-people/docs/zh-TW/01-department-mandate.md` 中出現「治理流程執行能力」字樣，但它屬於來源治理文件中的描述語句，**不是** skill factory 目前已採用的正式 skill classification framework。

#### 目前已 authored skills 的實際型別分布

從目前 18 份已 authored skills 的 `skill_type` 來看，實際分布如下：

- Analysis: 4
- Design: 2
- Documentation: 5
- Engineering: 3
- Governance: 1
- Operations: 1
- Testing: 2

目前尚未在已 authored skills 中出現的型別：

- Management
- Verification
- Integration

#### 與四大類的對應判讀

若硬要將現有 taxonomy 對應到四大類，較合理的推導方式如下：

- **執行能力**
  - 可對應：Engineering、Testing、Operations
  - 目前已 authored 數量：6

- **設計能力**
  - 可對應：Design
  - 目前已 authored 數量：2

- **治理能力**
  - 可對應：Governance
  - 目前已 authored 數量：1

- **文件化能力**
  - 可對應：Documentation
  - 目前已 authored 數量：5

但這樣對應後，會立刻出現一個結構問題：

- **Analysis** 這一類目前沒有自然歸屬

已 authored 的 4 份 Analysis skills 包括風險評估、資產清冊、供應商風險評估等，這些在工程上非常重要，但若只用四大類，會出現以下歧義：

- 它們是設計前置？
- 還是執行能力的一部分？
- 還是應該獨立成第五類「分析能力」？

這表示四大類目前**不足以完整覆蓋** repo 已有的 skill_type 現況。

#### 審查判斷

就目前狀態而言，可做如下判斷：

1. **文件化能力：有做到，且最明確**
   - `Documentation` 已是正式 skill_type
   - 已 authored skills 中也佔比最高之一

2. **設計能力：有做到**
   - `Design` 已是正式 skill_type
   - 但目前已 authored 數量仍偏少

3. **治理能力：有做到，但覆蓋不足**
   - `Governance` 已是正式 skill_type
   - 目前只有 `SK-D01-013`
   - 真正屬於治理主線的 D11 skills 尚未落地

4. **執行能力：有部分做到，但不是以單一類別存在**
   - 它被拆散在 `Engineering`、`Testing`、`Operations`
   - 也就是 conceptually 有，但 schema 上沒有叫做「Execution」

5. **四分類整體：尚未正式落地**
   - 現有系統採用的是 10 類 skill taxonomy
   - 四分類目前只能視為高階管理視角的再分群，不是現行主分類

#### 對 skill factory 的影響

這件事的影響不小，因為它涉及：

- skill dashboard 怎麼做彙總
- 後續依賴圖是否要顯示 macro category
- 管理層是否能快速理解目前 registry 的能力分布
- 未來 AI agent 是否要用粗粒度或細粒度做 skill routing

若未明確決定四大類與 10-type taxonomy 的關係，後續很容易出現：

- 文件用四大類講
- registry 用十類寫
- 報表與自動化用不同映射

最後造成治理層與執行層語言不一致。

#### 鑑識結論

截至 2026-03-13，本 repo 對這四類的落地程度可總結為：

- **文件化能力：已正式落地**
- **設計能力：已正式落地**
- **治理能力：已正式落地，但落地深度不足**
- **執行能力：僅以多個 skill_type 分散落地，尚未作為單一正式類別存在**

因此，若以嚴格治理標準判斷：

**目前尚未正式完成「四大能力分類」建模；現況比較接近「十類 skill type taxonomy 已落地，四類 macro view 尚未定義」。**

---

## 7. 關鍵不一致與治理漂移

### 6.1 `README.md` 已非最新狀態

`README.md` 說明：

- Phase 3: `16/171 authored`

但實際 registry 檔案數量為 **18**。因此 README 至少在 skill authored count 上落後。

### 6.2 `repo-bootstrap-summary.md` 屬於過時快照

此文件仍描述：

- 24-field schema
- 149 candidates
- 初始 bootstrap 階段的目錄與統計

但實際專案已進入：

- 27-field schema
- 171 candidates
- R5 source authority hierarchy

因此這份文件應視為 **歷史快照**，不應作為現況依據。

### 6.3 `phase3-execution-plan.md` 與實體檔案不完全一致

計畫文件顯示：

- Batch 4: `PENDING`

但實際上 registry 內已存在：

- `SK-D08-005.md`
- `SK-D09-002.md`

代表 Batch 4 不是完全 pending，而是至少 **部分完成**。此為目前最明顯的治理同步落差之一。

### 6.4 統計與治理文件存在多版本並存現象

目錄內同時存在：

- bootstrap summary
- README current view
- changelog rolling history
- phase execution plan
- approved map baseline

這些文件不是全部同步更新，已出現「同一專案多個真相版本」的治理風險。若未持續整併，未來會影響：

- 新成員 onboarding
- 自動化讀取與報表
- Phase 4 依賴抽取的可信度

---

## 8. 實際成熟度判讀

### 7.1 已成熟部分

以下部分已相當成熟：

- 領域 taxonomy 已定型
- ID 規範已定型
- skill schema 已定型到 27 fields
- golden example 已建立
- source authority hierarchy 已明確
- 部分高優先技能已達可複用的定義品質

這表示專案的核心治理骨架已建立完成。

### 7.2 尚未成熟部分

以下部分仍未完成：

- 大規模 skill authoring 覆蓋率仍低
- dependencies 尚未系統化
- composition patterns 尚未產出
- conflict analysis 尚未啟動
- refactoring/evolution 尚未展開
- 多份摘要文件未同步，治理狀態板不夠穩定

### 7.3 目前所處階段

綜合判斷，本專案目前位於：

**Phase 3 早中期**

理由：

- 架構已穩定，不再是探索期
- 核心模板與規則已定型
- 已開始批次 authoring
- 但覆蓋率尚未高到可進入 Phase 4 的全面依賴建模

---

## 9. 技術與流程風險

### 8.1 無 git 歷史

目前根目錄不是 git repository，造成：

- 無法追溯各版本差異來源
- 無法確認誰在何時更新 README、CHANGELOG、execution plan
- 無法做正式的 forensics timeline reconstruction

若要做更高可信度的鑑識，需取得原始 git 倉或其他版本紀錄。

### 8.2 編碼/顯示風險

在 PowerShell 讀取時，多份中文文件出現亂碼。這不一定代表檔案內容毀損，但表示至少存在以下一種問題：

- 檔案編碼與終端顯示編碼不一致
- PowerShell output encoding 與檔案實際編碼不一致
- 字型/locale 設定與內容不相容

此問題會直接影響：

- 人工審閱
- 文字抽取
- diff 判讀
- 後續自動化報表與轉檔流程

### 8.3 治理同步風險

目前最實際的風險不是 taxonomy 設計，而是治理同步：

- 實際 skill 檔案數量增加後，摘要文件沒有同步更新
- 執行計畫與 registry 之間已出現落差
- 若未建立單一 progress ledger，後續 Phase 4 很容易吃到錯誤前提

### 9.4 Skill Graph 污染風險

由於目前多份已 authored skill 仍保留 promotion 後未回填的 `SC-*` 依賴參照，若直接進入 Phase 4 做 dependency extraction，會有以下風險：

- 同一 skill 被拆成 `SC-*` 與 `SK-*` 兩個節點
- dependency count 被高估
- cycle detection 產生假陽性
- composition pattern 分析結果失真

因此在進入 Phase 4 前，建議先做一次 registry cross-reference normalization。

---

## 10. 當前最可信的現況基線

若要選出目前最可信、最能代表「專案真實狀態」的文件組合，建議以以下優先順序判讀：

1. `03-skill-definitions/registry/`  
   原因：直接反映實際已落地產物

2. `00-governance/CHANGELOG.md`  
   原因：記錄 R1~R5 演進脈絡與統計變化

3. `01-domain-map/phase1-domain-map-approved.md`  
   原因：Phase 1 的正式核准基線

4. `02-skill-candidates/skill-candidate-inventory.md`  
   原因：Phase 2 的候選清單基線

5. `00-governance/SCHEMA.md`  
   原因：Phase 3 authoring 的現行 schema 規則

以下文件不建議單獨用來描述當前狀態：

- `repo-bootstrap-summary.md`
- `README.md`
- `03-skill-definitions/phase3-execution-plan.md`

原因不是它們無效，而是它們目前存在 **部分過時或未完全同步** 的問題。

---

## 11. 建議的近期修復順序

### P0

1. 更新 `README.md`
2. 更新 `03-skill-definitions/phase3-execution-plan.md`
3. 明確標記 `repo-bootstrap-summary.md` 為歷史快照
4. 修正 `SK-D01-001.md` 缺少 `Automation Potential` 的問題
5. 對已 promotion 的 skill 執行一次 `SC-*` -> `SK-*` cross-reference 回填

### P1

6. 建立一份單一的 Phase 3 進度表
7. 將 registry 實際數量與 batch 狀態自動化對齊
8. 為 Phase 4 準備可抽取的 dependency ledger
9. 補齊 D11 的最小 authored set，完成 Stage 1 Batch 4

### P2

10. 統一 Markdown 編碼策略為 UTF-8
11. 固定終端/轉檔輸出編碼
12. 規範哪些 summary 文件需要同步更新，哪些只保留歷史用途
13. 建立 registry 品質檢查規則，至少涵蓋欄位完整性與 stale placeholder 檢測

---

## 12. 最終判斷

本專案不是空架構，也不是初期草稿，而是已經完成技能治理骨架設計、完成候選技能抽取、並開始高品質 skill definition authoring 的知識工程專案。

它目前最大的問題不是「不知道要做什麼」，而是：

- 現況文件沒有完全同步
- Phase 3 的執行狀態需要更清楚的單一進度來源
- 後續 Phase 4~7 尚未接續啟動

如果後續目標是讓這個 skill factory 成為真正可持續維護、可供 AI 與人共同使用的權威技能登錄系統，那麼接下來最關鍵的工作是：

- 把 Phase 3 進度治理收斂成單一真實來源
- 盡快建立 dependency mapping 的可執行基線
- 先修正文檔同步問題，再擴大 authoring 覆蓋率

---

## 13. 附錄：本次鑑識直接參考的關鍵文件

- `README.md`
- `repo-bootstrap-summary.md`
- `00-governance/skill-governance-workplan.md`
- `00-governance/CHANGELOG.md`
- `00-governance/SCHEMA.md`
- `00-governance/CONVENTIONS.md`
- `01-domain-map/phase1-domain-map-approved.md`
- `02-skill-candidates/skill-candidate-inventory.md`
- `03-skill-definitions/phase3-execution-plan.md`
- `03-skill-definitions/registry/*.md`
- `04-dependency-map/TODO.md`
- `05-conflict-analysis/TODO.md`
- `06-refactoring/TODO.md`
- `07-evolution/TODO.md`
- `source-documents/system-design/manifest.json`
- `source-documents/system-design-people/manifest.json`
- `source-documents/project-governance/docs/reports/Cross-Layer-Consistency-Forensics-Report.md`
- `source-documents/project-governance/docs/Domain-Contamination-Assessment.md`
