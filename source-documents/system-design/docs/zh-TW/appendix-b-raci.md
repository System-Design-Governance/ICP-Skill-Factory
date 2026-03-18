```{=latex}
\newpage
\begin{landscape}
\pagestyle{landscapepage}
\enableLandscapeHeaderFooter
```

# Appendix B: RACI Matrix

## Introduction {#appB-introduction}

本附錄定義 System Design Governance 流程中各角色的責任分配。

**RACI 代碼說明**：
- **R** (Responsible)：負責執行該活動
- **A** (Accountable)：最終負責人，對結果承擔責任
- **C** (Consulted)：需諮詢意見，提供輸入
- **I** (Informed)：需告知結果

### 治理定位 {#appB-governance-position}

本 RACI Matrix 為主文件《System Design Governance》之執行層責任映射表，用途如下：

- **Gate Review 責任判定**：明確各 Gate 之 Approver、Accountable 與參與者
- **設計交付責任移轉**：定義 Gate 3 交接時之責任邊界
- **風險接受與稽核佐證**：區分設計責任與風險承擔責任
- **爭議處理依據**：當責任歸屬有爭議時，以本附錄為判定基準

本附錄所有角色與活動定義，以主文件第 3 章（Design Gates）、第 4 章（Roles & Accountability）、第 5 章（Risk Acceptance）為準。

### Approver 唯一性原則 {#appB-approver-principle}

**每個 Gate 僅有一個 Approver**，此為本治理框架之核心原則。RACI 表格中標註為 **A** 之角色，即為該 Gate 之唯一 Approver，承擔最終放行決策之責任。

**關於授權與代行**：

1. **授權關係不出現於 RACI 表格**：若 Approver 依組織授權由他人代行審查，該授權關係屬組織內部安排，不改變 RACI 表格中之責任歸屬標示。

2. **責任不因代行而分散**：無論是否委任代行，Gate 放行之最終責任仍由 RACI 表格所標示之 Approver 承擔。

3. **表格標示原則**：RACI 表格僅標示「責任歸屬」，不標示「執行方式」或「授權安排」。

---

## Gate-based RACI Matrix {#appB-gate-raci}

### Gate 0：專案啟動審查（Project Initiation & Feasibility） {#appB-gate0}

```{=latex}
\begin{tabularx}{\linewidth}{|L{5.5cm}|Z|Z|Z|Z|Z|Z|Z|}
\hline
\textbf{Activity} & \textbf{System Architect} & \textbf{Security Team} & \textbf{QA Team} & \textbf{Project Manager} & \textbf{Design Requesting Function} & \textbf{Risk Acceptance Authority} & \textbf{Engineering Management} \\
\hline
設計需求提出與確認 & C & I & I & C & R/A & - & I \\
\hline
技術可行性評估 & R/A & C & I & C & C & - & I \\
\hline
初步風險清單建立 & R & R & I & C & I & - & I \\
\hline
風險評估策略定義 & R/A & C & I & I & I & - & I \\
\hline
目標 SL 等級提案 & R & R & I & I & I & - & I \\
\hline
\textbf{Gate 0 Review \& Approval} & R & C & I & C & C & - & \textbf{A} \\
\hline
\end{tabularx}
```

### Gate 1：設計基線建立（Design Baseline & Risk Identification） {#appB-gate1}

```{=latex}
\begin{tabularx}{\linewidth}{|L{5.5cm}|Z|Z|Z|Z|Z|Z|Z|}
\hline
\textbf{Activity} & \textbf{System Architect} & \textbf{Security Team} & \textbf{QA Team} & \textbf{Project Manager} & \textbf{Design Requesting Function} & \textbf{Risk Acceptance Authority} & \textbf{Engineering Management} \\
\hline
設計基線文件撰寫 & R/A & C & C & I & I & - & I \\
\hline
整合式風險評估（IEC 62443-3-2 + FMEA + HAZOP） & R/A & R & C & I & I & - & I \\
\hline
Zone \& Conduit Diagram & R/A & R & I & I & I & - & I \\
\hline
IEC 62443 對應檢查表 & R & R/A & C & I & I & - & I \\
\hline
需求追溯矩陣 & R/A & C & R & I & C & - & I \\
\hline
\textbf{Gate 1 Review \& Approval}$^{\dagger}$ & R & R & R & I & I & - & \textbf{A}$^{\dagger}$ \\
\hline
\end{tabularx}
```

### Gate 2：設計變更管理（Design Change & Deviation Control） {#appB-gate2}

```{=latex}
\begin{tabularx}{\linewidth}{|L{5.5cm}|Z|Z|Z|Z|Z|Z|Z|}
\hline
\textbf{Activity} & \textbf{System Architect} & \textbf{Security Team} & \textbf{QA Team} & \textbf{Project Manager} & \textbf{Design Requesting Function} & \textbf{Risk Acceptance Authority} & \textbf{Engineering Management} \\
\hline
需求變更確認 & C & I & I & C & R/A & - & I \\
\hline
變更描述與影響分析 & R/A & C & C & I & C & - & I \\
\hline
風險評估更新 & R/A & R & C & I & I & - & I \\
\hline
設計文件版本更新 & R/A & I & C & I & I & - & I \\
\hline
SL 等級影響評估 & R & R/A & I & I & I & - & C \\
\hline
\textbf{Gate 2 Review \& Approval} & R & C & C & I & I & - & \textbf{A} \\
\hline
\end{tabularx}
```

### Gate 3：設計交付與責任移轉（Design Handover & Risk Transfer） {#appB-gate3}

```{=latex}
\begin{tabularx}{\linewidth}{|L{5.5cm}|Z|Z|Z|Z|Z|Z|Z|}
\hline
\textbf{Activity} & \textbf{System Architect} & \textbf{Security Team} & \textbf{QA Team} & \textbf{Project Manager} & \textbf{Design Requesting Function} & \textbf{Risk Acceptance Authority} & \textbf{Engineering Management} \\
\hline
最終設計文件包整備 & R/A & C & R & I & I & I & I \\
\hline
殘餘風險清單編製 & R/A & R & C & I & I & C & I \\
\hline
殘餘風險追溯驗證（20\% 抽查） & C & C & R/A & I & I & I & I \\
\hline
\textbf{殘餘風險接受簽核} & I & C & I & R & I & \textbf{A} & C（Critical Risk） \\
\hline
交接會議召開與紀錄 & R & I & I & R & I & R & I \\
\hline
\textbf{Gate 3 Review \& Approval}$^{\dagger}$ & R & C & R & I & I & I & \textbf{A}$^{\dagger}$ \\
\hline
\end{tabularx}
```

$^{\dagger}$ **Gate 1 及 Gate 3 委任說明**：Engineering Management 保留最終責任（Accountable），但依主文件 3.3.2 節及 3.3.4 節，Gate 1 及 Gate 3 之審查執行與放行決策由 System Design Governance Function 代行。

---

## RACI Rules {#appB-rules}

### 唯一 Accountable 原則 {#appB-single-accountable}

- **每個 Gate 僅有一個 Approver（A）**：避免權責分散，確保有人對 Gate 放行負最終責任
- **可有多個 Responsible（R）與 Consulted（C）**：執行與諮詢可由多人分擔
- **R/A 合併標註**：表示該角色既執行又負最終責任（常見於 System Architect 之設計產出）

### Gate 3 特殊規則 {#appB-gate3-special}

- **Risk Acceptance 與 Gate Approval 必須分離**：
  - 殘餘風險接受：由 Risk Acceptance Authority（依主文件 5.2 節分級）
  - Gate 3 放行：由 System Design Governance Function
- **分離原因**：風險承擔者與設計審查者職責不同，不得由同一角色兼任

### QA Team 角色限制 {#appB-qa-constraints}

- QA Team 不得擔任任何 Gate 之 Approver
- QA Team 僅能擔任 Responsible（執行審查）或 Consulted（提供意見）
- QA Team 之追溯驗證為獨立審查，結果供 Approver 參考

---

## Role Definitions {#appB-role-definitions}

### System Architect {#appB-role-architect}

**職責範圍**：
- 對設計內容正確性與風險揭露完整性負責
- 負責所有設計文件之 Accountable
- 參與 Gate 0 至 Gate 3 所有審查

**責任邊界**：
- **不可**代表專案執行單位接受殘餘風險
- **不可**擔任 Gate Approver（僅為 Responsible）
- Gate 3 後，設計責任移轉至專案執行單位

### Security Team {#appB-role-security}

**職責範圍**：
- 負責安全需求定義、威脅建模、IEC 62443 對應檢查
- 執行整合式風險評估之資安威脅識別部分
- 審查安全控制措施有效性

**責任邊界**：
- **不可**單獨決定 SL 等級（須與 System Architect 協作）
- **不可**代替 Risk Acceptance Authority 接受風險

### QA Team {#appB-role-qa}

**職責範圍**：
- 負責設計文件完整性與追溯性審查
- 執行 Gate 3 殘餘風險追溯驗證（至少 20% 抽查）
- 驗證版本一致性

**責任邊界**：
- **不可**擔任任何 Gate 之 Approver
- **不可**接受風險或放行設計
- 審查結果為建議性質，最終決策由 Approver 負責

### Project Manager {#appB-role-pm}

**職責範圍**：
- 負責專案整體協調與治理流程遵循
- 管理利害關係人溝通與會議召集
- Gate 3 交接會議之共同簽核者

**責任邊界**：
- **不可**放行設計 Gate（除非主文件明確授權）
- **可**擔任 Low/Medium Risk 之 Risk Acceptance Authority（依主文件 5.2 節）
- 對流程遵循負責，對設計內容正確性不負責

### Design Requesting Function {#appB-role-drf}

**職責範圍**：
- 設計需求之唯一合法提出來源
- 對設計需求之商業目的、營運必要性或策略合理性負責
- 確認需求變更之合理性

**RACI 角色**：
- **Gate 0**：設計需求提出與確認（R/A）、技術可行性評估與審查（C）
- **Gate 1**：需求追溯矩陣審查（C）
- **Gate 2**：需求變更確認（R/A）、變更影響分析（C）
- **Gate 3**：不參與

**責任邊界**：
- **不可**擔任 Gate 1 至 Gate 3 之 Approver
- **不可**對設計解法、安全架構或風險控制負技術決策責任
- **不可**參與設計內容審查（僅就需求範圍與商業合理性提供確認）

**角色映射**：依組織實際情況，可由 Business Owner、Product Owner、Requirement Owner、或經授權之專案發起人擔任。

**與 Business Owner 之關係說明**：

- **Business Owner 作為 DRF**：當 Business Owner 擔任 Design Requesting Function 時，負責需求提出與商業合理性確認（Gate 0、Gate 2）
- **Business Owner 作為 RAA**：當 Business Owner 參與 Risk Acceptance Authority（High Risk 情境）時，負責殘餘風險接受簽核（Gate 3）
- **職責不混淆**：同一人於不同時點行使不同職責時，簽核紀錄須分別留存，且不得以 DRF 身分代行 RAA 職責

### Risk Acceptance Authority {#appB-role-raa}

**職責範圍**：
- 僅於 Gate 3 出現，負責殘餘風險接受簽核
- 依主文件 5.2 節分級：
  - Low Risk：Project Manager
  - Medium Risk：Project Manager + Security Lead
  - High Risk：Project Manager + Security Lead + Business Owner
  - Critical Risk：須升級至 Engineering Management

**責任邊界**：
- **不等同於** Gate Approver（Gate 放行與風險接受為不同決策）
- 風險接受後，該風險之後果由接受者承擔
- **不可**由 System Architect 或 System Design Governance Function 擔任

### Engineering Management {#appB-role-engmgmt}

**職責範圍**：
- Gate 0、Gate 2 之 Approver
- Gate 1、Gate 3 之最終責任者（操作上由 System Design Governance Function 執行審查與放行，依主文件 3.3.2/3.3.4 節）
- 爭議升級之最終決策者
- Critical Risk 之額外緩解計畫核准

**責任邊界**：
- 對資源分配與專案啟動決策負責
- 對設計技術內容不直接負責（由 System Architect 負責）
- Gate 1、Gate 3 之審查與放行由 System Design Governance Function 代行，惟最終責任不因代行而移轉

---

## Escalation Path {#appB-escalation}

當跨部門對責任歸屬有爭議時，遵循以下升級路徑（依主文件 4.3 節）：

| Level | 參與者 | 時限 | 說明 |
|-------|--------|------|------|
| Level 1 | System Architect + Project Manager + QA Team | 3 個工作日 | 團隊層級協商，嘗試技術手段解決 |
| Level 2 | System Design Governance Function | 5 個工作日 | 部門層級仲裁，基於主文件判定 |
| Level 3 | Engineering Management | 10 個工作日 | 管理層最終決策 |

**Gate 對應說明**：
- 爭議通常發生於 **Gate 1**（設計基線範圍）與 **Gate 3**（殘餘風險接受）
- 爭議期間，該 Gate 視為「未通過」，專案不得進入下一階段
- 例外情境：若涉及「緊急安全修補」（主文件 2.2.1），可同步啟動例外機制

---

## Communication Matrix {#appB-communication}

| Information | Frequency | Format | Owner | Recipients |
|-------------|-----------|--------|-------|-----------|
| Design Requirement Specification | Gate 0 | Requirement Document | Design Requesting Function | System Architect, Project Manager |
| Gate Review Record | Per Gate | Meeting minutes | System Design Governance Function | All roles |
| Integrated Risk Assessment Report | Gate 1 / Gate 2 | Report | System Architect | Security Team, QA Team, Engineering Management |
| Residual Risk Register | Gate 3 | Register（Appendix C 模板） | System Architect | Risk Acceptance Authority, QA Team |
| Design Handover Meeting Minutes | Gate 3 | Meeting minutes | Project Manager | System Architect, 專案執行單位 |
| Design Change Notice | As needed | Change Record | System Architect | Security Team, QA Team, Engineering Management, Design Requesting Function |
| Requirement Change Confirmation | As needed | Confirmation Record | Design Requesting Function | System Architect, Project Manager |

---

## Document Control {#appB-doc-control}

- **Version**: 1.0
- **Effective Date**: 2026-01-08
- **Owner**: System Design Governance Function
- **Review Cycle**: 與主文件同步

本附錄之修訂依主文件 6.2 節流程辦理。

---

**文件結束**

```{=latex}
\disableLandscapeHeaderFooter
\end{landscape}
\pagestyle{fancy}
```
