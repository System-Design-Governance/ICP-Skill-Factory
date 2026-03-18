# 治理角色與責任邊界

## Governance Role and Responsibility Boundary

**文件編號：** GOV-01-002
**文件版本：** 1.1
**生效日期：** 2026-02-09
**文件層級：** 公司級治理文件
**依據文件：** GOV-01-001 部門使命與組織定位

---

## 職責範圍

系統設計部門**必須擁有**以下職責：

### 標準定義與維護職責

- **標準框架擁有權**：定義、發布、維護並強制執行所有設計相關標準
- **標準審查與更新**：每年審查標準時效性，依需要更新
- **標準詮釋權**：作為標準詮釋之最終權威
- **標準合規驗證**：驗證受治理專案與單位之標準合規狀態

### 設計治理職責

- **治理框架執行**：執行《System Design Governance》文件及所有規範性附錄
- **Gate 審查權責**：擔任 Gate 1 及 Gate 3 之 Approver；由 Head of System Design 進行 Gate 0 及 Gate 2 核准
- **設計變更治理**：透過正式 Gate 2 流程控制 Gate 1 後之所有設計修改
- **設計交接執行**：透過書面交接會議促進設計責任正式移轉至執行單位
- **介面相容性驗證**：驗證與本治理框架銜接之外部單位符合最低相容性要求
- **爭議仲裁**：擔任專案團隊間責任爭議之第二級仲裁者（5 個工作日內）
- **例外管理**：處理標準偏離之例外申請，並維護例外紀錄供年度稽核檢視

### 系統架構職責

- **技術基線定義**：定義全公司系統設計之技術基線標準
- **技術可行性評估**：針對所有通過 Gate 0 之設計需求，執行並記錄技術可行性與初步風險識別
- **設計基線建立**：確保所有受治理之設計皆具備經正式核准之基線文件集，並納入版本控制
- **架構設計產出**：產出系統架構圖、介面定義、資料流圖及 Zone & Conduit 圖
- **設計文件擁有**：作為所有設計文件之當責擁有者，確保文件準確性與完整性

### 安全工程職責（設計階段）

- **安全標準執行**：執行設計階段安全工程標準
- **整合式風險評估**：執行並驗證所有適用專案之 IEC 62443-3-2 威脅分析、FMEA 及 HAZOP
- **IEC 62443 合規驗證**：維護主要對應表（FR-SR），並確保所有適用之系統要求（SR）皆已處理
- **安全等級（SL）判定**：於 Gate 0 提出目標 SL、於 Gate 1 確認 SL 對齊、於 Gate 3 驗證殘餘風險不影響所宣告之 SL
- **安全需求定義**：定義設計階段安全需求並執行威脅建模

### 設計品質保證職責

- **品質標準執行**：執行設計品質標準
- **文件完整性驗證**：驗證設計文件符合完整性要求
- **追溯性稽核**：執行需求追溯矩陣之建立與抽查驗證
- **符合性審查**：於 Gate 審查前執行設計符合性審查
- **殘餘風險清冊維護**：確保所有殘餘風險皆使用標準化模板記錄，並具備適當簽核鏈

### 設計工程管理職責

- **標準擁有權裁決**：作為標準詮釋與例外核准之最終權責
- **Gate 0/Gate 2 核准**：作為 Gate 0（需求受理）及 Gate 2（重大變更）之核准權責
- **例外裁決**：裁決標準偏離之例外申請
- **爭議升級決策**：處理 Level 3 爭議升級
- **技術方向決策**：決定部門技術方向與標準演進方向
- **設計資源配置決策**：決定設計階段資源配置優先順序

---

## 明確排除之職責

以下職責**不屬於**本部門：

| 職責 | 權責單位 | 邊界說明 |
|:--------------------------|:--------------------------------|:-------------------------------|
| 業務需求蒐集與商務承諾 | 業務部門 | 商業決策非設計範圍 |
| 設計需求之正當性與商業合理性確認 | Design Requesting Function | 業務合理性由需求方負責 |
| 實作、施工或部署 | 執行部門／專案執行單位 | 設計責任於 Gate 3 移轉；本部門提供標準，不執行實作 |
| 運行期間風險管理與事件回應 | 營運維護部門 | 運行階段非本部門範圍 |
| 殘餘風險接受決策（簽核權限） | Risk Acceptance Authority | 風險接受為業務決策；本部門提供風險清單，不接受風險 |
| 專案執行階段資源配置與時程安排 | Project Manager | 執行階段管理非本部門範圍 |
| 實作階段安全測試與滲透測試 | Security Operations Team | 本部門提供設計階段安全標準，不執行實作階段測試 |
| 生產環境品質檢驗 | Production QA Team | 本部門提供設計品質標準，不執行生產品質檢驗 |

### 邊界澄清

- 本部門**定義標準**，其他單位**遵循標準執行**
- 若執行偏離核准設計，本部門**不**對執行結果負責
- 本部門**不**代替執行單位接受殘餘風險
- 對於設計階段無法合理識別之風險，本部門**不**追溯承擔設計責任
- 本部門之安全工程職責**僅限於**設計階段標準與執行
- 本部門之品質保證職責**僅限於**設計文件與設計產出

### 賦能而非代勞

本部門透過以下方式賦能其他單位正確執行，而非代替其執行：

| 賦能方式 | 說明 | 受益單位 |
|:----------|:--------------------------------------|:----------------|
| 標準提供 | 提供可遵循之標準框架 | 所有受治理單位 |
| 範本提供 | 提供可直接使用之標準範本 | 設計執行人員 |
| 流程定義 | 定義可預期之決策流程 | 專案團隊 |
| 品質基線 | 定義可量測之品質標準 | 交付單位 |
| 技術基線 | 定義可參照之技術標準 | 架構設計人員 |

### 內部角色與外部單位區分

| 功能 | 本部門內部角色（標準擁有者） | 部門外部對應單位（標準遵循者） |
|:----------|:-------------------------------|:-------------------------------|
| 安全工程 | Security Engineering Role（設計階段標準） | Security Operations Team（實作/運行階段執行） |
| 品質保證 | Design QA Role（設計品質標準） | Production QA Team（生產品質執行） |
| 工程管理 | Head of System Design（設計決策標準） | Project Manager（執行管理） |
| 前置需求釐清 | Pre-Gate Design Support（技術預釐清） | 業務部門（商務需求蒐集） |

### Pre-Gate Design Support 角色定位與責任邊界

**角色性質**：Pre-Gate Design Support 定義為 **Concept System Architect / Feasibility Owner**，為 Pre-Gate 0 與 Gate 0 階段之正式執行角色。本角色**非商務角色、非諮詢角色**，而是承擔 Gate 0 輸入品質當責之技術角色。

#### 角色定位

| 定位項目 | 說明 |
|---------|------|
| **角色正式名稱** | Concept System Architect / Feasibility Owner |
| **職責階段** | Pre-Gate 0 至 Gate 0 核准 |
| **角色性質** | 技術執行角色，非商務角色 |
| **與業務區分** | 提供技術可行性判斷，非商務承諾 |

#### 責任邊界

| 邊界項目 | 說明 |
|---------|------|
| **承擔 Gate 0 輸入文件當責** | Gate 0 所需之需求釐清、風險預揭露、可行性判斷由本角色負責產出 |
| **不承擔 Gate 0 核准決策責任** | Gate 0 核准/拒絕決策當責歸屬於 Head of System Design |
| **不承擔 Gate 1 後設計責任** | Gate 0 核准後，設計責任正式移轉至 System Architect |
| **不承擔風險評估最終責任** | 正式風險評估與 SL 判定當責歸屬於 Security Engineering Role |
| **不因概念產出錯誤承擔設計後果** | 概念產出明確標註為 Non-binding，正式設計責任歸屬 System Architect |

#### Gate 0 輸入文件當責

**Pre-Gate Design Support 負責產出 Gate 0 所有輸入文件**：

| 輸入文件 | 當責 | 文件性質 |
|---------|------|---------|
| 需求釐清紀錄 | Pre-Gate Design Support | 正式文件 |
| 風險預揭露清單 | Pre-Gate Design Support | 正式文件 |
| 技術可行性初評 | Pre-Gate Design Support | 建議性質（供 System Architect 參考） |
| **初階 BOM List（Feasibility BOM）** | Pre-Gate Design Support | **Commercially Usable / Design Non-binding** |
| **概念系統架構圖（Concept Architecture）** | Pre-Gate Design Support | **Conceptual / Design Non-binding** |

#### 概念產出之性質與用途

##### BOM 使用性與拘束力定義

**Feasibility BOM 之「Commercially Usable / Design Non-binding」定義**：

| 層面 | 說明 |
|-----|------|
| **Commercially Usable（商務可用）** | 可作為報價、成案、合約估算之商務依據 |
| **Design Non-binding（設計不拘束）** | 不構成技術實作承諾、不自動成為設計基線、System Architect 得於 Gate 1 調整或否定 |

**關鍵區分**：

| 項目 | Feasibility BOM（Gate 0） | Design BOM（Gate 1） |
|:----------|:--------------------------|:--------------------|
| 商務報價使用 | ✔ 可使用 | ✔ 可使用 |
| 設計基線地位 | ✖ 非設計基線 | ✔ 正式設計基線 |
| 技術實作承諾 | ✖ 不構成承諾 | ✔ 構成承諾 |
| 可調整性 | ✔ Gate 1 可調整或否定 | 須經 Gate 2 變更程序 |
| 當責角色 | Pre-Gate Design Support | System Architect |

##### 初階 BOM List（Feasibility BOM）之用途

**允許用途**：

1. 報價與成案之商務依據
2. Gate 0 可行性判斷依據
3. 風險識別與預揭露支持
4. 資源估算與時程初估參考
5. 合約金額估算參考

**明確限制**：

- Feasibility BOM **不**自動成為設計基線（Design Baseline）
- Feasibility BOM **不**構成技術實作承諾
- System Architect 於 Gate 1 **得**調整、修正或否定 Feasibility BOM 內容而不構成違約
- Feasibility BOM **不得**直接作為施工或執行依據
- 正式設計基線須由 System Architect 於 Gate 1 重新確認或產出

##### 概念系統架構圖（Concept Architecture）之用途

**允許用途**：

1. Gate 0 可行性判斷依據
2. 風險識別與預揭露支持
3. 溝通與說明用途

**明確限制**：

- Concept Architecture **不**自動成為設計基線
- Concept Architecture **不得**直接作為施工或執行依據
- 正式系統架構須由 System Architect 於 Gate 1 重新設計並產出

---

## BOM 分層語義定義

### BOM 類型定義

本治理框架定義兩種 BOM 類型，各有明確之用途、當責與拘束力：

| 屬性 | Commercial BOM (CBOM) | Engineering BOM (EBOM) |
|:--------------|:----------------------|:----------------------|
| **定義** | 可供報價與合約範圍引用之 BOM | 設計基線與工程交付用之 BOM |
| **產生階段** | Pre-Gate 0 至 Gate 0 | Gate 1 之後 |
| **當責角色** | Pre-Gate Design Support | System Architect |
| **商務可用性** | ✔ 可用於報價、成案、合約估算 | ✔ 可用於報價與合約 |
| **設計基線地位** | ✖ 非設計基線 | ✔ 正式設計基線 |
| **技術實作承諾** | ✖ 不構成技術實作承諾 | ✔ 構成技術實作承諾 |
| **凍結與變更管理** | 無凍結機制（Gate 0 前可自由更新） | 受變更管理程序控制 |
| **版本控制** | 報價後須保留版本紀錄 | 納入設計基線版本控制 |

### CBOM 與 EBOM 之關係

```
Pre-Gate 0          Gate 0           Gate 1            Gate 2/3
    │                 │                │                  │
    │  CBOM 產出      │                │                  │
    │ ─────────────► │                │                  │
    │                 │ Gate 0 核准    │                  │
    │                 │ CBOM 定版      │                  │
    │                 │                │                  │
    │                 │                │  EBOM 產出       │
    │                 │                │ ◄─────────────── │
    │                 │                │                  │
    │                 │                │  EBOM 與 CBOM    │
    │                 │                │  差異紀錄        │
    │                 │                │ ─────────────────│
```

### CBOM 詳細規範

#### 定義與用途

**Commercial BOM (CBOM)** 為 Pre-Gate Design Support 於 Gate 0 前產出之初階設備清單，具備以下特性：

| 特性 | 說明 |
|-----|------|
| **商務可用** | 可作為報價、成案、合約金額估算之依據 |
| **設計不拘束** | 不構成技術實作承諾，System Architect 於 Gate 1 得調整 |
| **版本追溯** | 報價後須保留版本，供後續差異比對 |

#### CBOM 狀態流轉

| 狀態 | 說明 | 觸發時點 |
|-----|------|---------|
| Draft | 初稿，可自由修改 | CBOM 建立時 |
| Quoted | 已用於報價，版本須保留 | 報價提交時 |
| Gate0 Approved | Gate 0 核准定版 | Gate 0 核准時 |

#### CBOM 允許用途

1. 報價與成案之商務依據
2. 合約金額估算參考
3. Gate 0 可行性判斷依據
4. 資源估算與時程初估參考
5. 風險識別與預揭露支持

#### CBOM 明確限制

- CBOM **不**自動成為設計基線（Design Baseline）
- CBOM **不**構成技術實作承諾
- System Architect 於 Gate 1 **得**調整、修正或否定 CBOM 內容而不構成對商務承諾之違約
- CBOM **不得**直接作為施工或執行依據
- 正式設計基線須由 System Architect 於 Gate 1 確認或重新產出為 EBOM

### EBOM 詳細規範

#### 定義與用途

**Engineering BOM (EBOM)** 為 System Architect 於 Gate 1 後產出之設計基線 BOM，具備以下特性：

| 特性 | 說明 |
|-----|------|
| **設計基線** | 構成正式設計基線，納入版本控制 |
| **技術承諾** | 構成技術實作承諾 |
| **變更管理** | 變更須經 Gate 2 程序 |

#### EBOM 狀態流轉

| 狀態 | 說明 | 觸發時點 |
|-----|------|---------|
| Draft | System Architect 編製中 | EBOM 建立時 |
| Baseline | 已納入設計基線 | Gate 1 核准時 |
| Frozen | 凍結，變更須經 Gate 2 | Gate 3 前凍結 |

#### EBOM 與 CBOM 差異處理

| 情境 | 處理方式 | 當責角色 |
|-----|---------|---------|
| EBOM 與 CBOM 完全一致 | 無需額外處理 | System Architect |
| EBOM 與 CBOM 存在差異 | 記錄差異原因，觸發評估 | System Architect |
| 差異導致商務影響 | 通知業務部門處理合約調整 | 業務部門 |

### Gate 0 之商務轉折語義

**Gate 0 核准代表**：

| 項目 | 說明 |
|-----|------|
| 商務可承諾範圍定版 | CBOM 於 Gate 0 核准後定版，構成商務可用基準 |
| 設計責任移轉起點 | 設計責任正式移轉至 System Architect |
| **非**工程基線成立 | 工程基線（EBOM）於 Gate 1 方成立 |

**重要說明**：

1. Gate 0 核准**不**等於技術實作承諾
2. 商務合約應明確說明 CBOM 之「Commercially Usable / Design Non-binding」性質
3. System Architect 於 Gate 1 調整 CBOM 為其正當職權，不構成對商務承諾之違約
4. 商務調整（如合約變更）之處理責任歸屬於業務部門，非設計部門

### BOM 責任追溯矩陣

| 責任追溯路徑 | 說明 |
|-------------|------|
| 商務依據 → CBOM → Pre-Gate Design Support | CBOM 內容當責歸屬 Pre-Gate Design Support |
| 設計基線 → EBOM → System Architect | EBOM 內容當責歸屬 System Architect |
| 差異處理 → 業務部門 | 商務合約調整當責歸屬業務部門 |

#### 責任移轉機制

```
Pre-Gate 0 → Gate 0 核准 → 責任移轉
     ↓              ↓           ↓
Pre-Gate Design   Head of    System Architect
Support 產出     System     承接設計責任
Gate 0 輸入    Design 核准
```

**責任移轉時點**：Gate 0 核准後，設計責任正式移轉至 System Architect。移轉後：

- System Architect 對設計基線負完全當責
- Pre-Gate Design Support 之概念產出僅供參考
- 後續設計變更由 System Architect 負責

#### Gate 1 對 Feasibility BOM 之承接與驗證

**承接機制**：

| 步驟 | 說明 | 當責角色 |
|-----|------|---------|
| 1. 承接檢視 | System Architect 檢視 Feasibility BOM 內容 | System Architect |
| 2. 技術評估 | 評估 Feasibility BOM 之技術可行性與完整性 | System Architect |
| 3. 調整決策 | 決定沿用、調整或重新產出 | System Architect |
| 4. Design BOM 產出 | 產出正式 Design BOM 作為設計基線 | System Architect |
| 5. 差異記錄 | 若有調整，記錄差異原因 | System Architect |

**調整權限說明**：

| 情境 | System Architect 權限 | 對商務合約之影響 |
|-----|---------------------|-----------------|
| Feasibility BOM 完全可行 | 沿用並確認為設計基線 | 無 |
| 部分規格需調整 | 調整後產出 Design BOM | 依合約條款處理（非設計責任） |
| 技術不可行需重大修正 | 否定並提出替代方案 | 依合約條款處理（非設計責任） |

**重要說明**：

1. System Architect 於 Gate 1 調整 Feasibility BOM 為其正當職權，**不**構成對商務承諾之違約
2. 商務合約條款應明確說明 Feasibility BOM 之「Commercially Usable / Design Non-binding」性質
3. 商務調整（如合約變更）之處理責任歸屬於業務部門，**非**設計部門
4. 責任可清楚回溯：商務依據 → Feasibility BOM → Pre-Gate Design Support；設計基線 → Design BOM → System Architect

#### RCW 與責任對應

```
高 RCW（0.75）= 對 Gate 0 輸入品質之貢獻獎勵
高 RCW ≠ 承擔設計責任
責任歸屬 = 依階段移轉（Gate 0 前：Pre-Gate Design Support；Gate 0 後：System Architect）
```

---

## Gate 與角色當責對應

### Gate 當責矩陣

| Gate | 核准者 (Approver) | 當責執行角色 | 必要輸入 |
|:-----:|:---------------------------|:--------------------------------------|:--------------------------------------|
| **Gate 0** | Head of System Design | **Pre-Gate Design Support（Gate 0 輸入文件）**、System Architect（技術可行性審核）、Security Engineering Role（SL 提案） | **需求釐清紀錄、風險預揭露清單、Feasibility BOM、Concept Architecture**、技術可行性評估、目標 SL 提案 |
| Gate 1 | System Design Governance Lead | System Architect（設計基線）、Security Engineering Role（風險評估）、Design QA Role（追溯矩陣） | 設計基線文件集、整合式風險評估報告、SR 檢查表、需求追溯矩陣 |
| Gate 2 | Head of System Design（重大）/ System Architect（次要） | System Architect（變更紀錄）、Security Engineering Role（影響分析） | 設計變更紀錄、影響分析文件、更新之 SL Decision Record（若適用） |
| Gate 3 | System Design Governance Lead | System Architect（最終文件包）、Security Engineering Role（殘餘風險清單）、Design QA Role（交付檢查表） | 最終設計文件包、殘餘風險清單、設計交付檢查表、交接會議紀錄 |

### Pre-Gate 0 階段職責

| 階段 | Pre-Gate Design Support 職責 | 產出文件 | 文件性質 |
|:----------:|:---------------------------|:-----------------|:--------------------------------------|
| Pre-Gate 0 | 需求技術釐清 | 需求釐清紀錄 | 正式文件 |
| Pre-Gate 0 | 技術風險預揭露 | 風險預揭露清單 | 正式文件 |
| Pre-Gate 0 | 可行性評估初判 | 技術可行性初評 | 建議性質 |
| Pre-Gate 0 | 初階 BOM 估算 | Feasibility BOM | Commercially Usable / Design Non-binding |
| Pre-Gate 0 | 概念架構產出 | Concept Architecture | Conceptual / Design Non-binding |
| Gate 0 | 提交 Gate 0 輸入文件 | Gate 0 文件包 | 正式提交 |
| Gate 0 後 | 責任移轉至 System Architect | 交接紀錄 | 正式文件 |

### Gate 0 後責任移轉

| 階段 | Pre-Gate Design Support | System Architect |
|-----|------------------------|------------------|
| Gate 0 核准前 | 負責所有 Gate 0 輸入文件 | 審核可行性初評、提供標準指導 |
| Gate 0 核准後 | 責任終止，概念產出僅供參考 | 承接設計責任，重新產出正式設計文件 |
| Gate 1 | 無直接參與 | 負責設計基線產出 |
| Gate 2/3 | 無直接參與 | 負責後續設計當責 |

### 標準與角色對應

| 標準類別 | 擁有角色 |
|---------|---------|
| 治理框架標準 | System Design Governance Lead |
| 設計流程標準 | System Architect + System Design Governance Lead |
| 安全工程標準 | Security Engineering Role |
| 設計品質標準 | Design QA Role |
| 例外管理標準 | Head of System Design |
| 需求預釐清標準 | 無正式標準擁有權（Pre-Gate Design Support 執行，System Architect 指導） |

---

## 內外部介面

### 部門內部角色介面矩陣

| 角色 A | 角色 B | 介面內容 |
|-------|-------|---------|
| Head of System Design | System Design Governance Lead | 標準核准、Gate 審查包、例外申請、升級案件 |
| Head of System Design | System Architect | 技術基線標準核准、技術可行性評估 |
| Head of System Design | Security Engineering Role | 安全標準核准、SL Decision Record 核准 |
| Head of System Design | Design QA Role | 品質標準核准 |
| System Design Governance Lead | System Architect | Gate 審查、設計交接、標準合規驗證 |
| System Design Governance Lead | Security Engineering Role | 安全分析結果供 Gate 審查 |
| System Design Governance Lead | Design QA Role | QA 審查結果供 Gate 決策 |
| System Design Governance Lead | Design Governance Coordinator | 流程執行指派 |
| System Architect | Security Engineering Role | 架構資訊↔安全要求 |
| System Architect | Design QA Role | 設計文件 QA 審查 |
| System Architect | Pre-Gate Design Support | 預釐清方向指導、技術標準一致性確認 |
| Security Engineering Role | Design QA Role | 風險追溯性驗證 |
| Security Engineering Role | Pre-Gate Design Support | 風險預揭露資訊銜接 |
| Pre-Gate Design Support | Design Requesting Function（外部） | 需求預釐清、技術限制溝通 |

### 外部介面

| 介面對象 | 資訊流入（Inbound） | 資訊流出（Outbound） | 治理接觸點 |
|:-----------------------------|:------------------|:------------------------------|:---------|
| **Design Requesting Function** | 設計需求規格、範圍變更確認 | 標準要求、技術可行性回饋、Gate 0 受理／拒絕 | Gate 0、Gate 2 |
| **Risk Acceptance Authority** | 殘餘風險接受決策 | 殘餘風險清單供簽核 | Gate 3 |
| **執行部門** | 偏差回報 | 設計文件包、標準合規要求、交接確認 | Gate 3 交接 |
| **營運維護部門** | 運行回饋 | 設計限制說明 | 交接後 |
| **Project Manager** | 專案時程限制 | Gate 時程、標準遵循要求 | Gate 3 |

### 外部稽核介面

| 介面對象 | 介面目的 | 治理要求 |
|--------|--------|--------|
| **外部稽核員** | IEC 62443 合規稽核、ISO 9001 流程稽核 | 提供 Gate 紀錄、風險清冊、合規檢查表、標準文件作為稽核證據 |
| **驗證機構** | 需設計證據之產品驗證 | 提供與驗證範圍對齊之設計文件包 |
| **客戶（透過業務部門）** | 設計交付物驗收 | 與業務部門協調；本部門不直接與客戶介接 |

### 外部單位介面相容性要求

任何與本部門治理框架銜接之外部組織單位須展現：

1. **標準認知**：理解並承諾遵循本部門所定義之標準
2. **角色映射**：能夠識別 Design Requesting Function、Risk Acceptance Authority 及 Accountable Role 之對等角色
3. **決策點映射**：具備至少兩個可稽核決策點，等效於 Gate 0 及 Gate 3
4. **可稽核性**：能夠提供文件清冊、決策紀錄及責任歸屬紀錄

不相容之單位於補救措施協議完成前，不得被承認為有效之需求來源或責任承接方。

---

## Responsibility Density Indicators（責任密度指標）

### 定義與目的

**責任密度指標（Responsibility Density Indicators）** 為描述性指標，用於說明特定角色於特定時期內所承擔之責任集中程度。此指標**非計分用途**，僅供以下目的使用：

1. **工作負荷可視化**：協助管理層理解角色負荷分布
2. **資源配置參考**：作為人力規劃之參考依據
3. **風險識別**：識別責任過度集中之潛在風險
4. **組織設計改善**：支持角色架構之持續優化

### 責任密度構成要素

| 要素 | 說明 | 量測方式 |
|-----|------|---------|
| **Gate 參與密度** | 於評估週期內參與之 Gate 審查次數 | 計數（Gate 0/1/2/3 分別計算） |
| **標準擁有範圍** | 所擁有之標準數量與複雜度 | 標準數量 × 複雜度係數 |
| **決策當責密度** | 須做出之核准/裁決決策數量 | 計數（依決策類型分類） |
| **介面複雜度** | 須協調之內外部介面數量 | 介面角色數量 |
| **角色重疊係數** | 同時擔任之角色數量 | 角色數量（依 Allocation Factor 加權） |

### 責任密度解讀

| 密度水準 | 描述 | 管理意涵 |
|---------|------|---------|
| **低密度** | 責任分散，負荷輕 | 可考慮增加角色承擔 |
| **適中密度** | 責任適度集中 | 正常運作狀態 |
| **高密度** | 責任高度集中 | 需關注burnout 風險，考慮分擔 |
| **過載密度** | 責任過度集中 | 須立即處理，可能影響治理品質 |

### 使用限制

**責任密度指標之使用限制**：

| 禁止事項 | 理由 |
|---------|------|
| 不得用於績效計分 | 密度為描述性指標，非績效指標 |
| 不得用於比較個人表現 | 密度反映配置狀況，非個人能力 |
| 不得作為薪酬決策依據 | 薪酬應基於績效，非工作負荷 |
| 不得替代 KPI 評估 | KPI 評估當責履行，密度僅描述負荷 |

---

## 治理完整性自我驗證

### 標準擁有權驗證

- [x] 所有標準皆有擁有角色
- [x] 每個標準擁有角色皆有明確之標準範圍
- [x] 無孤立標準（無擁有角色之標準）

### Gate 當責驗證

- [x] Gate 0：Head of System Design（核准）、System Architect（技術可行性）、Security Engineering Role（SL 提案）
- [x] Gate 1：System Design Governance Lead（核准）、System Architect（設計基線）、Security Engineering Role（風險評估）、Design QA Role（追溯矩陣）
- [x] Gate 2：Head of System Design / System Architect（核准）、System Architect（變更紀錄）、Security Engineering Role（影響分析）
- [x] Gate 3：System Design Governance Lead（核准）、System Architect（最終文件包）、Security Engineering Role（殘餘風險清單）、Design QA Role（交付檢查表）

### 責任無空白驗證

- [x] 所有職責範圍皆可對應至至少一個角色
- [x] 所有成功標準皆有當責角色
- [x] 所有標準皆有擁有角色

---

## 假設條件

本文件之適用基於以下假設：

1. **角色配置**：本說明書所定義之角色代表功能性職責；一人可擔任多個角色，一個角色亦可由多人共同擔任；無論配置方式為何，當責與標準擁有權仍歸屬於角色
2. **設計階段邊界**：本部門之權限範圍僅限於設計階段；實作階段、運行階段之對應功能仍由部門外部單位負責，但須遵循本部門於設計階段定義之標準
3. **Head of System Design 權限**：Head of System Design 具有組織權限核准標準發布、Gate 0、Gate 2（重大變更）、例外及最終升級決策
4. **外部單位區分**：本部門內部角色為標準擁有者，部門外部對應單位為標準遵循者；設計階段與實作/運行階段之責任邊界以 Gate 3 為分界

---

*文件結束*
