# 角色定義與職責說明

## Role Definitions and Job Descriptions

**文件編號：** GOV-02-001
**文件版本：** 1.1
**生效日期：** 2026-02-09
**文件層級：** 角色治理文件
**依據文件：** GOV-01-001 部門使命與組織定位

---

## 角色架構原則

### 基本原則

1. **功能性角色定義**：本文件定義之角色為**功能性系統角色（Functional System Role）**，非職位名稱
2. **角色與人員分離**：一人可擔任多個角色，一個角色亦可由多人共同擔任
3. **當責隨角色**：當責歸屬於角色，非歸屬於個人
4. **標準擁有權映射**：每個角色對應特定標準之擁有權，角色共同構成部門之標準擁有能力
5. **角色邊界明確**：每個角色之決策權限、當責範圍及產出物須明確定義且不重疊

### 角色清單

| 角色 | 功能領域 | 標準擁有權 |
|-----|---------|-----------|
| Head of System Design | 設計工程管理 | 標準體系整體擁有權、例外管理標準 |
| System Design Governance Lead | 設計治理 | 治理框架標準、Gate 機制標準 |
| System Architect | 系統架構 | 架構設計標準、技術基線標準 |
| Security Engineering Role | 安全工程 | 安全工程標準、風險評估標準 |
| Design QA Role | 設計品質保證 | 文件品質標準、追溯性標準 |
| Design Governance Coordinator | 治理協調 | 無（執行支援角色） |
| Pre-Gate Design Support | **概念設計與可行性（Concept System Architect / Feasibility Owner）** | 無（Gate 0 執行角色，非標準擁有者） |

---

## Head of System Design

### Role Purpose

作為系統設計部門之最高權責者，擁有部門標準體系之整體擁有權，確保本部門作為公司級技術權責單位之定位得以實現。本角色負責標準方向決策、例外裁決及跨部門技術爭議之最終裁決。

### Accountabilities

- 部門標準體系之整體完整性與一致性
- 標準偏離例外之最終裁決當責
- Gate 0（需求受理）及 Gate 2（重大變更）之核准當責
- Level 3 爭議升級之最終裁決當責
- 部門技術方向之決策當責

### Decision Authority

| 決策類型 | 權限 |
|---------|-----|
| 標準發布與重大修訂 | 核准 |
| 標準偏離例外申請 | 最終裁決 |
| Gate 0 核准 | 核准或拒絕 |
| Gate 2 重大變更核准 | 核准或拒絕 |
| Level 3 爭議 | 最終裁決 |
| 部門技術方向 | 決定 |
| SL Decision Record | 核准 |

### Key Responsibilities

- 核准標準發布與重大修訂
- 裁決標準偏離例外申請，維護例外紀錄
- 審核並核准 Gate 0 需求受理決策
- 審核並核准 Gate 2 重大設計變更
- 處理 Level 3 爭議升級
- 決定部門技術方向與標準演進方向
- 核准安全等級（SL）決策紀錄

### Key Deliverables and Evidence

| 交付物/證據 | 說明 |
|-----------|-----|
| 標準發布核准紀錄 | 含標準名稱、版本、核准日期 |
| 例外裁決紀錄 | 含例外理由、裁決結果、附加條件、有效期限 |
| Gate 0 核准紀錄 | 含核准決策、日期、簽核 |
| Gate 2 重大變更核准紀錄 | 含變更範圍、影響評估、核准決策 |
| Level 3 爭議裁決紀錄 | 含爭議內容、裁決結果、執行要求 |
| SL Decision Record 核准簽核 | 於 SL Decision Record 上之核准簽核 |

### Role Interfaces

| 介面角色 | 介面目的 |
|---------|---------|
| System Design Governance Lead | 接收標準修訂提案、Gate 審查包、例外申請、升級案件 |
| System Architect | 接收技術可行性評估、技術基線標準提案 |
| Security Engineering Role | 接收 SL Decision Record 供核准、安全標準修訂提案 |
| Design Requesting Function（外部） | 溝通 Gate 0 核准/拒絕決策 |
| 高階管理層（外部） | 報告部門績效、技術方向建議 |

---

## System Design Governance Lead

### Role Purpose

作為治理框架標準之擁有者，確保本部門之治理原則、Gate 機制及合規要求成為全公司系統設計之強制遵循標準。本角色負責治理標準之定義、發布、執行監督及合規驗證。

### Accountabilities

- 治理框架標準（System Design Governance 主文件及附錄）之完整性與時效性
- 治理標準於全公司之一致執行
- Gate 1 及 Gate 3 之核准當責
- 爭議仲裁（Level 2）之處理當責
- 外部單位介面相容性之驗證當責

### Decision Authority

| 決策類型 | 權限 |
|---------|-----|
| 治理框架標準修訂 | 提案（需 Head of System Design 核准） |
| Gate 1 核准 | 核准或拒絕 |
| Gate 3 核准 | 核准或拒絕 |
| Level 2 爭議 | 仲裁（5 個工作日內） |
| 外部單位相容性 | 承認或不承認 |
| 標準合規判定 | 判定（合規/不合規/條件合規） |

### Key Responsibilities

- 定義、發布並維護《System Design Governance》文件及附錄
- 監督治理標準於系統部門內之執行狀況
- 執行 Gate 1 及 Gate 3 審查並作成核准決策
- 驗證受治理專案之標準合規狀態
- 於 5 個工作日內仲裁 Level 2 責任爭議
- 驗證外部單位之介面相容性
- 維護 Gate 審查紀錄及例外紀錄
- 協調設計交接會議並記錄交接結果

### Key Deliverables and Evidence

| 交付物/證據 | 說明 |
|-----------|-----|
| System Design Governance 主文件 | 含版本號、生效日期、年度審查紀錄 |
| Appendix B: RACI Matrix | Gate-based 責任分配矩陣 |
| Gate 1/Gate 3 審查紀錄 | 含審查結果、核准/拒絕決策、簽核 |
| 標準合規驗證紀錄 | 含驗證範圍、合規狀態、發現事項 |
| Level 2 爭議仲裁紀錄 | 含爭議內容、仲裁結果、解決日期 |
| 外部單位相容性評估紀錄 | 含角色映射、決策點映射、可稽核性評估 |
| 交接會議紀錄 | 含交接事項、簽核、確認聲明 |

### Role Interfaces

| 介面角色 | 介面目的 |
|---------|---------|
| Head of System Design | 提交標準修訂提案、Gate 審查包、例外申請、升級案件 |
| System Architect | 接收設計文件供 Gate 審查；協調設計交接 |
| Security Engineering Role | 接收安全分析結果供 Gate 審查 |
| Design QA Role | 接收 QA 審查結果供 Gate 決策 |
| Design Governance Coordinator | 指派 Gate 流程執行任務 |
| 執行部門（外部） | 執行設計交接、接收偏差回報 |

---

## System Architect

### Role Purpose

作為架構設計標準與技術基線標準之擁有者，確保全公司系統設計具備一致之技術基礎與架構方法。本角色負責定義架構設計之標準方法、維護技術基線，並作為專案層級設計內容之當責擁有者。

### Accountabilities

- 架構設計標準之完整性與可執行性
- 技術基線標準之維護與更新
- 系統架構決策之技術正確性
- 設計文件（設計基線、架構圖、介面定義）之準確性與完整性
- 技術可行性評估之當責

### Decision Authority

| 決策類型 | 權限 |
|---------|-----|
| 架構設計標準修訂 | 提案（需 Head of System Design 核准） |
| 技術基線更新 | 提案（需 Head of System Design 核准） |
| 架構設計決策 | 決定（重大變更需 Gate 2 核准） |
| 技術可行性判定 | 建議（Gate 0 核准由 Head of System Design） |
| 設計變更分類 | 判定（Minor/Major 分類） |
| 設計文件版本發布 | 核准（Minor 版本） |

### Key Responsibilities

- 定義並維護架構設計標準
- 定義並維護技術基線標準
- 執行技術可行性評估並記錄評估結果
- 產出系統架構設計，包含架構圖、介面定義、資料流圖
- 產出 Zone & Conduit Diagram
- 建立並維護設計基線文件集
- 建立並維護設計標的清冊
- 執行設計變更影響分析
- 編製最終設計文件包供 Gate 3 交付

### Key Deliverables and Evidence

| 交付物/證據 | 說明 |
|-----------|-----|
| 架構設計標準文件 | 含標準方法、範本、範例 |
| 技術基線標準文件 | 含技術規格、相容性要求 |
| 技術可行性評估紀錄 | 含評估範圍、技術分析、結論 |
| 設計基線文件集 | 經版本控制之完整設計文件 |
| 系統架構圖 | 含元件、介面、資料流 |
| Zone & Conduit Diagram | 符合 IEC 62443-3-2 之分區圖 |
| 設計標的清冊 | 含所有設計標的、版本、狀態 |
| 設計變更紀錄 | 含變更內容、分類、影響分析 |
| 最終設計文件包 | Gate 3 交付之完整文件包 |

### Role Interfaces

| 介面角色 | 介面目的 |
|---------|---------|
| Head of System Design | 提交標準修訂提案、技術可行性評估供 Gate 0 決策 |
| System Design Governance Lead | 提交設計文件供 Gate 審查；參與交接會議 |
| Security Engineering Role | 提供架構資訊供安全分析；接收安全要求納入設計 |
| Design QA Role | 提交設計文件供 QA 審查；回應 QA 發現 |
| Design Requesting Function（外部） | 接收設計需求規格；溝通技術限制 |
| 執行部門（外部） | 交付設計文件包；回應設計澄清請求 |

---

## Security Engineering Role

### Role Purpose

作為設計階段安全工程標準與風險評估標準之擁有者，確保全公司系統設計於設計階段即納入適當之安全考量，並與 IEC 62443 標準對齊。本角色負責定義安全工程之標準方法，並作為專案層級安全分析之當責執行者。

### Accountabilities

- 安全工程標準（IEC 62443 對應、威脅建模、SL 判定）之完整性與可執行性
- 風險評估標準（威脅情境、FMEA、HAZOP、殘餘風險管理）之完整性與可執行性
- 設計階段威脅分析之完整性與正確性
- IEC 62443 合規驗證之當責
- 安全等級（SL）判定之當責
- 殘餘風險清單編製之當責

### Decision Authority

| 決策類型 | 權限 |
|---------|-----|
| 安全工程標準修訂 | 提案（需 Head of System Design 核准） |
| 風險評估標準修訂 | 提案（需 Head of System Design 核准） |
| 目標 SL 提案 | 提案（Gate 0） |
| SL 對齊確認 | 確認（Gate 1） |
| SL 驗證 | 驗證（Gate 3） |
| 風險評估方法選擇 | 決定（Lite/Full Assessment） |
| SR 對應狀態判定 | 判定（Implemented/Partial/Not Applicable） |

### Key Responsibilities

- 定義並維護安全工程標準（Appendix A）
- 定義並維護風險評估標準（Appendix C, D）
- 於 Gate 0 提出目標安全等級（SL）建議
- 執行 IEC 62443-3-2 威脅情境分析
- 執行或監督 FMEA 及 HAZOP 分析
- 維護 FR-SR 對應表及 SR 檢查表
- 於 Gate 1 確認 SL 對齊
- 於 Gate 3 驗證殘餘風險不影響所宣告之 SL
- 編製殘餘風險清單供 Risk Acceptance Authority 簽核

### Key Deliverables and Evidence

| 交付物/證據 | 說明 |
|-----------|-----|
| 安全工程標準文件（Appendix A） | 含 IEC 62443 對應方法、SL 判定程序 |
| 風險評估標準文件（Appendix C, D） | 含風險評估方法、範本、範例 |
| SL Decision Record | 含目標 SL、判定理由、各 Gate 更新紀錄 |
| 整合式風險評估報告 | 含威脅情境、FMEA、HAZOP 分析結果 |
| IEC 62443 SR 檢查表 | 含所有適用 SR 之處理狀態與證據引用 |
| Zone & Conduit 分析工作表 | 威脅情境分析之工作紀錄 |
| 殘餘風險清單 | 含風險 ID、來源追溯、風險等級、建議處置 |

### Role Interfaces

| 介面角色 | 介面目的 |
|---------|---------|
| Head of System Design | 提交標準修訂提案、SL Decision Record 供核准 |
| System Design Governance Lead | 提交安全分析結果供 Gate 審查 |
| System Architect | 接收架構資訊進行安全分析；提供安全要求納入設計 |
| Design QA Role | 協調風險追溯性驗證 |
| Risk Acceptance Authority（外部） | 提交殘餘風險清單供簽核 |

---

## Design QA Role

### Role Purpose

作為設計品質標準與追溯性標準之擁有者，確保全公司設計產出具備一致之品質水準與可追溯性。本角色負責定義設計品質之標準方法，並作為專案層級品質驗證之當責執行者。

### Accountabilities

- 文件品質標準之完整性與可執行性
- 追溯性標準之完整性與可執行性
- 設計文件完整性驗證之當責
- 需求追溯矩陣之建立與維護當責
- 文件清冊之維護當責
- Gate 審查前符合性審查之當責

### Decision Authority

| 決策類型 | 權限 |
|---------|-----|
| 文件品質標準修訂 | 提案（需 Head of System Design 核准） |
| 追溯性標準修訂 | 提案（需 Head of System Design 核准） |
| 文件完整性判定 | 判定（通過/不通過/條件通過） |
| 追溯性抽查結果 | 判定（通過/不通過） |
| 文件清冊更新 | 維護 |
| QA 審查報告發布 | 發布（建議性質） |

### Key Responsibilities

- 定義並維護文件品質標準
- 定義並維護追溯性標準
- 建立並維護需求追溯矩陣
- 建立並維護文件清冊（Document Register）
- 於 Gate 審查前執行設計文件完整性審查
- 於 Gate 3 執行殘餘風險可追溯性抽查（20% 抽查）
- 編製設計交付檢查表
- 編製設計 QA 審查報告
- 驗證文件版本一致性

### Key Deliverables and Evidence

| 交付物/證據 | 說明 |
|-----------|-----|
| 文件品質標準文件 | 含格式要求、元資料要求、版本控制要求 |
| 追溯性標準文件 | 含追溯方法、驗證程序、抽查標準 |
| 需求追溯矩陣 | 含需求 ID、設計對應、驗證狀態 |
| 文件清冊 | 含文件 ID、版本、狀態、擁有者 |
| 設計 QA 審查報告 | 含審查範圍、發現、建議 |
| 設計交付檢查表 | Gate 3 之 12 項檢查結果 |
| 追溯性抽查紀錄 | 含抽查樣本、追溯驗證結果 |
| 版本一致性驗證紀錄 | Gate 3 文件包版本一致性驗證 |

### Role Interfaces

| 介面角色 | 介面目的 |
|---------|---------|
| Head of System Design | 提交標準修訂提案 |
| System Design Governance Lead | 提交 QA 審查報告供 Gate 決策 |
| System Architect | 接收設計文件進行 QA 審查；回饋 QA 發現 |
| Security Engineering Role | 協調風險追溯性驗證 |
| Design Governance Coordinator | 協調文件清冊維護 |

---

## Design Governance Coordinator

### Role Purpose

作為治理流程執行與文件管理之協調者，確保 Gate 流程順利執行、文件管理有序、會議紀錄完整。本角色為執行支援角色，不擁有標準，但確保標準流程之日常運作順暢。

### Accountabilities

- Gate 流程執行之協調當責
- Gate 審查會議之安排與紀錄當責
- 治理文件版本控制之維護當責

### Decision Authority

| 決策類型 | 權限 |
|---------|-----|
| Gate 會議安排 | 安排 |
| 文件版本發布 | 協調（需 Document Owner 核准） |
| 流程提醒發送 | 發送 |

### Key Responsibilities

- 協調 Gate 審查會議之安排與執行
- 記錄 Gate 審查會議紀錄
- 維護治理文件之版本控制
- 追蹤 Gate 審查待辦事項
- 協調文件收集與分發
- 發送流程提醒與時程通知

### Key Deliverables and Evidence

| 交付物/證據 | 說明 |
|-----------|-----|
| Gate 會議紀錄 | 含議程、決議、待辦事項 |
| 版本控制紀錄 | 文件版本變更紀錄 |
| 流程追蹤表 | Gate 流程進度追蹤 |

### Role Interfaces

| 介面角色 | 介面目的 |
|---------|---------|
| System Design Governance Lead | 接收指派、回報執行狀態 |
| System Architect | 協調文件提交、會議安排 |
| Security Engineering Role | 協調安全文件提交 |
| Design QA Role | 協調 QA 審查排程 |

---

## Pre-Gate Design Support

### Role Purpose

作為 **Concept System Architect / Feasibility Owner**，本角色為 Pre-Gate 0 與 Gate 0 階段之**正式執行角色**。本角色**非商務角色、非諮詢角色**，而是承擔 Gate 0 輸入品質當責之技術角色。

本角色負責：
1. 產出 Gate 0 所需之所有輸入文件
2. 執行技術需求釐清與可行性初判
3. 識別並預揭露潛在技術風險
4. 產出 Feasibility BOM（Commercially Usable / Design Non-binding）
5. 產出 Concept Architecture（Conceptual / Design Non-binding）

Gate 0 核准後，設計責任正式移轉至 System Architect。System Architect 於 Gate 1 得依技術評估結果調整 Feasibility BOM，此為正當職權行使。

### Role Positioning

| 定位項目 | 說明 |
|---------|------|
| **角色正式名稱** | Concept System Architect / Feasibility Owner |
| **職責階段** | Pre-Gate 0 至 Gate 0 核准 |
| **角色性質** | 技術執行角色，非商務角色、非諮詢角色 |
| **Gate 0 當責** | 負責 Gate 0 所有輸入文件之產出 |
| **與 System Architect 區分** | Gate 0 前：本角色負責；Gate 0 後：責任移轉至 System Architect |
| **與業務區分** | 提供技術可行性判斷，非商務承諾或需求蒐集 |

### Accountabilities

- **Gate 0 輸入文件產出當責**：所有 Gate 0 所需之輸入文件由本角色負責產出
- 需求技術釐清之完整性與品質
- 技術風險與設計限制之預先揭露
- 初階 BOM（Feasibility BOM）之產出
- 概念系統架構圖（Concept Architecture）之產出
- Gate 0 準備度之初步評估

### Non-Accountabilities（明確排除）

**本角色明確不承擔以下當責**：

| 排除項目 | 理由 |
|---------|------|
| Gate 0 核准決策 | 核准當責歸屬於 Head of System Design |
| Gate 1/2/3 核准決策 | 核准當責歸屬於 System Design Governance Lead 或 Head of System Design |
| 設計基線文件產出 | Gate 0 後設計當責移轉至 System Architect |
| 正式 Design BOM 產出 | Gate 1 設計基線當責歸屬於 System Architect |
| 風險評估執行與 SL 判定 | 安全當責歸屬於 Security Engineering Role |
| 設計品質驗證 | 品質當責歸屬於 Design QA Role |
| 商務承諾與成交責任 | 商務當責歸屬於業務部門 |
| 執行階段問題解決 | 執行當責歸屬於執行部門 |
| Gate 1 調整 Feasibility BOM 之後果 | System Architect 調整 BOM 為正當職權，商務調整由業務部門處理 |
| 商務合約條款設計 | 商務當責歸屬於業務部門 |

### Decision Authority

| 決策類型 | 權限 |
|---------|-----|
| Gate 0 輸入文件內容 | 決定（文件產出當責） |
| 技術可行性初評 | 初步判定（供 System Architect 與 Head of System Design 參考） |
| 風險預揭露內容 | 決定（文件產出當責） |
| Feasibility BOM 內容 | 決定（標註為 Commercially Usable / Design Non-binding） |
| Concept Architecture 內容 | 決定（標註為 Conceptual / Design Non-binding） |
| Gate 0 核准決策 | **無**（由 Head of System Design 決定） |
| 正式設計方向決策 | **無**（由 System Architect 決定） |
| 正式 Design BOM 決定 | **無**（由 System Architect 於 Gate 1 決定） |

### Key Responsibilities

- 產出 Gate 0 所需之需求釐清紀錄
- 產出風險預揭露清單，識別潛在技術風險與設計限制
- 產出初階 BOM List（Feasibility BOM），標註為 Commercially Usable / Design Non-binding
- 產出概念系統架構圖（Concept Architecture），標註為 Conceptual / Design Non-binding
- 執行技術可行性初評，供 System Architect 審核
- 與 System Architect 協調，確保概念產出與設計標準一致
- 於 Gate 0 核准後，完成責任移轉交接

### Key Deliverables and Evidence

| 交付物/證據 | 性質 | 說明 |
|-----------|------|-----|
| 需求釐清紀錄 | 正式文件 | 含釐清項目、結果、日期、Design Requesting Function 確認 |
| 風險預揭露清單 | 正式文件 | 含風險 ID、風險描述、揭露日期、後續 Gate 追溯 ID |
| **初階 BOM List（Feasibility BOM）** | **Commercially Usable / Design Non-binding** | **含設備清單、規格初估、明確標註商務可用性與設計不拘束性** |
| **概念系統架構圖（Concept Architecture）** | **Conceptual / Design Non-binding** | **含系統架構初步規劃、明確標註概念性質與設計不拘束性** |
| 技術可行性初評 | 建議性質 | 供 System Architect 與 Head of System Design 參考 |
| 技術釐清會議紀錄 | 正式文件 | 含會議日期、參與者、釐清結論 |
| Gate 0 責任移轉紀錄 | 正式文件 | Gate 0 核准後，記錄責任移轉至 System Architect |

### 概念產出標註要求

**Commercial BOM (CBOM)** 須包含以下標註：

```
【文件性質：Commercial BOM (CBOM)】
【商務可用 / 設計不拘束】

本文件為 Gate 0 階段產出之 Commercial BOM。

▶ 文件類型說明：
  - BOM Type: Commercial BOM (CBOM)
  - Binding Scope: Commercial binding only（商務拘束，設計不拘束）
  - BOM Owner: Pre-Gate Design Support / Presales

▶ 商務可用性說明：
  本文件可作為報價、成案及合約估算之商務依據。
  報價後之版本須保留，供後續與 Engineering BOM (EBOM) 差異比對。

▶ 設計不拘束性說明：
  本文件不構成技術實作承諾，不自動成為設計基線（Design Baseline）。
  System Architect 於 Gate 1 得依技術評估結果調整、修正或重新產出正式
  Engineering BOM (EBOM)，此為正當職權行使，不構成對商務承諾之違約。

▶ 責任歸屬：
  - CBOM 內容當責：Pre-Gate Design Support（Concept System Architect）
  - EBOM / 設計基線當責：System Architect（Gate 1 起）
  - CBOM 與 EBOM 差異之商務處理：業務部門
```

**概念系統架構圖（Concept Architecture）**須包含以下標註：

```
【文件性質：Conceptual / Design Non-binding】
【概念性質 / 設計不拘束】

本圖為 Gate 0 階段產出之概念系統架構。

▶ 用途說明：
  本圖供 Gate 0 可行性評估、風險識別及技術溝通使用。

▶ 設計不拘束性說明：
  本圖不構成正式設計基線（Design Baseline）。
  正式系統架構須由 System Architect 於 Gate 1 重新設計並產出。
  本圖不得作為施工或執行依據。

▶ 責任歸屬：
  - 本圖內容當責：Pre-Gate Design Support（Concept System Architect）
  - 正式系統架構當責：System Architect（Gate 1 起）
```

### Role Interfaces

| 介面角色 | 介面目的 |
|---------|---------|
| Design Requesting Function（外部） | 接收需求草案、執行技術釐清 |
| System Architect | 協調概念產出方向、確認技術標準一致性、Gate 0 後責任交接 |
| Security Engineering Role | 風險預揭露資訊銜接、SL 提案協調 |
| Head of System Design | 提交 Gate 0 輸入文件、接收 Gate 0 核准決策 |

### Contribution Validation Mechanism

**本角色之貢獻權重（RCW）生效條件**：

高 RCW（0.75）僅在以下條件皆滿足時生效：

| 驗證條件 | 驗證時點 | 驗證方式 |
|---------|---------|---------|
| Gate 0 輸入文件被採用 | Gate 0 核准後 | Gate 0 核准紀錄引用本角色產出文件 |
| 預揭露風險於後續 Gate 未重複出現 | Gate 1/Gate 3 | 殘餘風險清單無預揭露風險之重複識別 |
| 後續設計階段無因需求釐清不足導致返工 | Gate 1 後 | 設計變更紀錄無「需求澄清不足」類別變更 |

若驗證條件未滿足，該評估週期之 RCW 降為 0.50。

---

## 主要交付物與文件

### 標準與框架文件（持續性）

| 文件 | 說明 | 當責角色 | 審查週期 |
|-----|------|---------|---------|
| System Design Governance（主文件） | 治理憲章文件 | System Design Governance Lead | 年度 |
| Appendix A：IEC 62443 Alignment | FR-SR 對應表、SL 模板、檢查表 | Security Engineering Role | 與主文件同步 |
| Appendix B：RACI Matrix | Gate-based 責任分配 | System Design Governance Lead | 與主文件同步 |
| Appendix C：Residual Risk Template | 風險清冊標準格式 | Security Engineering Role | 與主文件同步 |
| Appendix D：Integrated Risk Assessment Templates | 風險評估工作表 | Security Engineering Role | 與主文件同步 |
| Appendix E：Design Request Readiness Guideline | 需求準備指南 | System Design Governance Lead | 與主文件同步 |

### 專案交付物

| 文件 | 適用 Gate | 當責角色 |
|-----|----------|---------|
| 需求預釐清紀錄 | Pre-Gate 0 產出 | Pre-Gate Design Support |
| 風險預揭露清單 | Pre-Gate 0 產出 | Pre-Gate Design Support |
| 技術可行性評估紀錄 | Gate 0 產出 | System Architect |
| 風險評估策略文件 | Gate 0 產出 | Security Engineering Role |
| SL Decision Record | Gate 0、Gate 1、Gate 2（若變更）、Gate 3 | Security Engineering Role（編製）、Head of System Design（核准） |
| 設計基線文件集 | Gate 1 產出 | System Architect |
| Zone & Conduit Diagram | Gate 1（必要）、Gate 2（若更新） | System Architect |
| 整合式風險評估報告 | Gate 1 產出 | Security Engineering Role |
| IEC 62443 SR 檢查表 | Gate 1、Gate 3 | Security Engineering Role |
| 需求追溯矩陣 | Gate 1 產出 | Design QA Role |
| 文件清冊 | Gate 1（必要）、維護至 Gate 3 | Design QA Role |
| 設計標的清冊 | Gate 1（必要）、Gate 3 定版 | System Architect |
| 設計變更紀錄 | Gate 2（每次變更） | System Architect |
| 影響分析文件 | Gate 2（每次變更） | System Architect + Security Engineering Role |
| 最終設計文件包 | Gate 3 產出 | System Architect |
| 殘餘風險清單 | Gate 3 產出 | Security Engineering Role（編製）、Risk Acceptance Authority（接受） |
| 設計交付檢查表 | Gate 3 產出 | Design QA Role |
| 交接會議紀錄 | Gate 3 產出 | System Design Governance Lead |
| Gate 審查紀錄 | 每個 Gate | System Design Governance Lead |
| 設計 QA 審查報告 | Gate 1、Gate 3 | Design QA Role |

### 文件品質要求

所有交付物須符合本部門文件品質標準：
- 包含 Major.Minor 格式之版本號
- 包含 ISO 格式日期（YYYY-MM-DD）
- 包含文件擁有者識別
- 包含審查／核准簽核紀錄
- Gate 3 時文件包內所有引用版本須一致

---

## 假設條件

本文件之適用基於以下假設：

1. **角色配置**：本說明書所定義之角色代表功能性職責；一人可擔任多個角色，一個角色亦可由多人共同擔任；無論配置方式為何，當責與標準擁有權仍歸屬於角色
2. **Head of System Design 權限**：Head of System Design 具有組織權限核准標準發布、Gate 0、Gate 2（重大變更）、例外及最終升級決策

---

*文件結束*
