```{=latex}
\newpage
\begin{landscape}
\pagestyle{landscapepage}
\enableLandscapeHeaderFooter
```

# Appendix A: IEC 62443 Alignment

---

## Purpose and Scope {#appA-purpose}

本附錄提供 System Design Governance 主文件與 IEC 62443 標準系列之對應關係，作為 Gate 審查時驗證合規性之依據。本附錄為實施細節，不新增治理流程或角色；所有強制性要求以主文件為準。

---

## How to Use This Appendix During Gate Reviews {#appA-usage}

- **Gate 0**：使用「SL Decision Record Template」模板，記錄目標 SL 等級提案與假設依據
- **Gate 1**：使用「Primary Mapping Table」SR 檢查表驗證設計是否涵蓋目標 SL 之必要安全要求；使用「Gate 1 Compliance Checklist」確認所有必要產出
- **Gate 2**：當設計變更影響 Zone/Conduit 或 SL 等級時，重新檢視「Primary Mapping Table」受影響之 SR 項目；使用「Gate 2 Compliance Checklist」
- **Gate 3**：使用「Primary Mapping Table」驗證殘餘風險是否已對應至相關 SR；使用「Gate 3 Compliance Checklist」確認合規交付完整性
- **稽核準備**：「Secondary Mapping」提供 IEC 62443-2-4（程序要求）與 IEC 62443-3-2（風險評估）之證據對應，供稽核時快速索引
- **SL 變更管理**：任何 SL 等級調整必須更新「SL Decision Record Template」，並經主文件定義之核准流程

---

## IEC 62443 Reference Model Summary {#appA-reference-model}

IEC 62443 標準系列結構如下，本治理框架主要對應 2-4、3-2、3-3：

| 標準編號 | 標準名稱 | 與本治理框架之關係 |
|---------|---------|------------------|
| IEC 62443-1-1 | Concepts and Models | 術語定義參考 |
| IEC 62443-2-4 | Security Program Requirements for IACS Service Providers | 程序與流程要求，對應 Gate 機制與文件管理 |
| IEC 62443-3-2 | Security Risk Assessment for System Design | 風險評估方法，對應主文件 3.2 節整合式風險評估 |
| IEC 62443-3-3 | System Security Requirements and Security Levels | 系統安全要求，對應設計基線與 SR 檢查表 |
| IEC 62443-4-2 | Technical Security Requirements for IACS Components | 元件安全要求，由元件供應商負責，本框架於採購規格中引用 |

**Security Level (SL) 定義**：
- **SL 1**：防護偶發或意外違規
- **SL 2**：防護使用簡單手段之蓄意違規
- **SL 3**：防護使用複雜手段之蓄意違規
- **SL 4**：防護使用複雜手段且具備大量資源之蓄意違規

**重要說明**：目標 SL 為專案特定，依 Gate 0 提案、Gate 1 確認；本框架不預設特定 SL 等級。

---

## Primary Mapping Table: IEC 62443-3-3 Foundational Requirements {#appA-primary-mapping}

### Coverage Rule {#appA-coverage-rule}

所有 IEC 62443-3-3 System Requirements (SR) 必須於專案特定 SR 檢查表中涵蓋。本節提供規範性模板與對應方法；專案須依目標 SL 等級填寫實際對應狀態。

**Status 定義**：
| Status | 定義 | 證據要求 |
|--------|------|---------|
| Implemented | 設計已包含對應控制措施 | 設計文件明確描述控制措施，可追溯至 SR |
| Planned | 設計將包含但尚未完成 | Gate 1 Lite 可接受；Gate 3 前必須升級為 Implemented |
| N/A | 經評估不適用於本專案 | 必須記錄不適用理由並經 Approver 簽核 |

### FR-SR Mapping Template {#appA-fr-sr-mapping}

以下為 IEC 62443-3-3 七大 Foundational Requirements (FR) 之 SR 對應模板。專案應複製此模板並填寫實際狀態。

#### FR1: Identification and Authentication Control (IAC)

| SR ID | SR 簡述 | 治理控制點 | 預期證據 | Gate 1 Lite 最低要求 | Gate 3 完整要求 | Status |
|-------|--------|-----------|---------|---------------------|----------------|--------|
| SR 1.1 | Human User Identification and Authentication | Gate 1: 設計基線文件 | 認證機制設計說明 | 識別認證需求 | 完整認證設計與測試計畫 | |
| SR 1.2 | Software Process and Device Identification | Gate 1: 設計基線文件 | 軟體/設備識別機制 | 識別需識別之軟體與設備 | 完整識別機制設計 | |
| SR 1.3 | Account Management | Gate 1: 設計基線文件 | 帳號管理流程設計 | 帳號生命週期定義 | 完整帳號管理設計 | |
| SR 1.4 | Identifier Management | Gate 1: 設計基線文件 | 識別碼管理規則 | 識別碼命名規則 | 完整識別碼管理設計 | |
| SR 1.5 | Authenticator Management | Gate 1: 設計基線文件 | 驗證器管理機制 | 密碼/憑證策略 | 完整驗證器管理設計 | |
| SR 1.6 | Wireless Access Management | Gate 1: 設計基線文件 | 無線存取控制設計 | 識別無線存取點 | 完整無線安全設計（若適用） | |
| SR 1.7 | Strength of Password-based Authentication | Gate 1: 設計基線文件 | 密碼強度規則 | 密碼策略定義 | 密碼強度實作驗證 | |
| SR 1.8 | PKI Certificates | Gate 1: 設計基線文件 | PKI 設計文件 | PKI 需求識別 | 完整 PKI 設計（若適用） | |
| SR 1.9 | Strength of Public Key Authentication | Gate 1: 設計基線文件 | 公鑰認證設計 | 公鑰認證需求 | 公鑰強度驗證 | |
| SR 1.10 | Authenticator Feedback | Gate 1: 設計基線文件 | 認證回饋設計 | UI 認證回饋需求 | 認證回饋實作 | |
| SR 1.11 | Unsuccessful Login Attempts | Gate 1: 設計基線文件 | 登入失敗處理 | 失敗處理策略 | 失敗處理實作 | |
| SR 1.12 | System Use Notification | Gate 1: 設計基線文件 | 系統使用通知 | 通知需求定義 | 通知實作 | |
| SR 1.13 | Access via Untrusted Networks | Gate 1: Zone & Conduit Diagram | 非信任網路存取控制 | Zone 邊界識別 | 完整邊界控制設計 | |

#### FR2: Use Control (UC)

| SR ID | SR 簡述 | 治理控制點 | 預期證據 | Gate 1 Lite 最低要求 | Gate 3 完整要求 | Status |
|-------|--------|-----------|---------|---------------------|----------------|--------|
| SR 2.1 | Authorization Enforcement | Gate 1: 設計基線文件 | 授權機制設計 | 授權模型定義 | 完整授權實作設計 | |
| SR 2.2 | Wireless Use Control | Gate 1: 設計基線文件 | 無線使用控制 | 無線使用策略 | 無線控制實作（若適用） | |
| SR 2.3 | Use Control for Portable/Mobile Devices | Gate 1: 設計基線文件 | 行動裝置控制 | 行動裝置策略 | 行動裝置控制實作 | |
| SR 2.4 | Mobile Code | Gate 1: 設計基線文件 | 行動程式碼控制 | 行動程式碼策略 | 行動程式碼控制實作 | |
| SR 2.5 | Session Lock | Gate 1: 設計基線文件 | 工作階段鎖定 | 鎖定策略定義 | 鎖定機制實作 | |
| SR 2.6 | Remote Session Termination | Gate 1: 設計基線文件 | 遠端工作階段終止 | 終止策略定義 | 終止機制實作 | |
| SR 2.7 | Concurrent Session Control | Gate 1: 設計基線文件 | 並行工作階段控制 | 並行策略定義 | 並行控制實作 | |
| SR 2.8 | Auditable Events | Gate 1: 設計基線文件 | 可稽核事件定義 | 稽核事件清單 | 完整稽核設計 | |
| SR 2.9 | Audit Storage Capacity | Gate 1: 設計基線文件 | 稽核儲存容量 | 儲存需求評估 | 儲存設計與保護 | |
| SR 2.10 | Response to Audit Processing Failures | Gate 1: 設計基線文件 | 稽核失敗回應 | 失敗處理策略 | 失敗處理實作 | |
| SR 2.11 | Timestamps | Gate 1: 設計基線文件 | 時間戳記機制 | 時間同步需求 | 時間戳記實作 | |
| SR 2.12 | Non-repudiation | Gate 1: 設計基線文件 | 不可否認性機制 | 不可否認性需求 | 不可否認性實作（依 SL） | |

#### FR3: System Integrity (SI)

| SR ID | SR 簡述 | 治理控制點 | 預期證據 | Gate 1 Lite 最低要求 | Gate 3 完整要求 | Status |
|-------|--------|-----------|---------|---------------------|----------------|--------|
| SR 3.1 | Communication Integrity | Gate 1: 設計基線文件 | 通訊完整性機制 | 完整性需求識別 | 完整性機制設計 | |
| SR 3.2 | Malicious Code Protection | Gate 1: 設計基線文件 | 惡意程式碼防護 | 防護策略定義 | 防護機制設計 | |
| SR 3.3 | Security Functionality Verification | Gate 1: 設計基線文件 | 安全功能驗證 | 驗證需求定義 | 驗證程序設計 | |
| SR 3.4 | Software and Information Integrity | Gate 1: 設計基線文件 | 軟體/資訊完整性 | 完整性需求 | 完整性保護設計 | |
| SR 3.5 | Input Validation | Gate 1: 設計基線文件 | 輸入驗證機制 | 驗證需求識別 | 驗證機制設計 | |
| SR 3.6 | Deterministic Output | Gate 1: 設計基線文件 | 確定性輸出 | 輸出需求定義 | 輸出機制設計 | |
| SR 3.7 | Error Handling | Gate 1: 設計基線文件 | 錯誤處理機制 | 錯誤處理策略 | 錯誤處理設計 | |
| SR 3.8 | Session Integrity | Gate 1: 設計基線文件 | 工作階段完整性 | 完整性需求 | 完整性機制設計 | |
| SR 3.9 | Protection of Audit Information | Gate 1: 設計基線文件 | 稽核資訊保護 | 保護需求定義 | 保護機制設計 | |

#### FR4: Data Confidentiality (DC)

| SR ID | SR 簡述 | 治理控制點 | 預期證據 | Gate 1 Lite 最低要求 | Gate 3 完整要求 | Status |
|-------|--------|-----------|---------|---------------------|----------------|--------|
| SR 4.1 | Information Confidentiality | Gate 1: 設計基線文件 | 資訊機密性設計 | 機密性需求識別 | 機密性控制設計 | |
| SR 4.2 | Information Persistence | Gate 1: 設計基線文件 | 資訊持久性控制 | 資料保留需求 | 資料清除設計 | |
| SR 4.3 | Use of Cryptography | Gate 1: 設計基線文件 | 加密機制設計 | 加密需求識別 | 加密實作設計 | |

#### FR5: Restricted Data Flow (RDF)

| SR ID | SR 簡述 | 治理控制點 | 預期證據 | Gate 1 Lite 最低要求 | Gate 3 完整要求 | Status |
|-------|--------|-----------|---------|---------------------|----------------|--------|
| SR 5.1 | Network Segmentation | Gate 1: Zone & Conduit Diagram | 網路分割設計 | Zone 邊界定義 | 完整分割設計 | |
| SR 5.2 | Zone Boundary Protection | Gate 1: Zone & Conduit Diagram | Zone 邊界保護 | 邊界控制識別 | 邊界保護設計 | |
| SR 5.3 | General Purpose Person-to-Person Communication Restrictions | Gate 1: 設計基線文件 | 通訊限制設計 | 限制需求識別 | 限制機制設計 | |
| SR 5.4 | Application Partitioning | Gate 1: 設計基線文件 | 應用程式分割 | 分割需求識別 | 分割設計 | |

#### FR6: Timely Response to Events (TRE)

| SR ID | SR 簡述 | 治理控制點 | 預期證據 | Gate 1 Lite 最低要求 | Gate 3 完整要求 | Status |
|-------|--------|-----------|---------|---------------------|----------------|--------|
| SR 6.1 | Audit Log Accessibility | Gate 1: 設計基線文件 | 稽核日誌存取 | 存取需求定義 | 存取機制設計 | |
| SR 6.2 | Continuous Monitoring | Gate 1: 設計基線文件 | 持續監控設計 | 監控需求識別 | 監控機制設計 | |

#### FR7: Resource Availability (RA)

| SR ID | SR 簡述 | 治理控制點 | 預期證據 | Gate 1 Lite 最低要求 | Gate 3 完整要求 | Status |
|-------|--------|-----------|---------|---------------------|----------------|--------|
| SR 7.1 | Denial of Service Protection | Gate 1: 設計基線文件 | DoS 防護設計 | 防護需求識別 | 防護機制設計 | |
| SR 7.2 | Resource Management | Gate 1: 設計基線文件 | 資源管理設計 | 資源需求識別 | 資源管理設計 | |
| SR 7.3 | Control System Backup | Gate 1: 設計基線文件 | 備份設計 | 備份需求定義 | 備份機制設計 | |
| SR 7.4 | Control System Recovery and Reconstitution | Gate 1: 設計基線文件 | 復原設計 | 復原需求定義 | 復原機制設計 | |
| SR 7.5 | Emergency Power | Gate 1: 設計基線文件 | 緊急電源設計 | 電源需求識別 | 電源設計（若適用） | |
| SR 7.6 | Network and Security Configuration Settings | Gate 1: 設計基線文件 | 組態管理設計 | 組態需求定義 | 組態管理設計 | |
| SR 7.7 | Least Functionality | Gate 1: 設計基線文件 | 最小功能設計 | 功能精簡策略 | 功能精簡設計 | |
| SR 7.8 | Control System Component Inventory | Gate 1: 設計基線文件 | 元件清單管理 | 元件清單需求 | 元件清單設計 | |

### SR Checklist Usage Notes {#appA-sr-checklist-notes}

- **Gate 1 Lite**：Status 可為 Planned，但必須記錄預計完成時程
- **Gate 3**：所有適用 SR 之 Status 必須為 Implemented 或 N/A；N/A 必須有簽核理由
- **SR 與殘餘風險關聯**：Gate 3 殘餘風險清單中若有安全相關風險，必須標註對應之 SR ID
- **SL 等級對應**：不同 SL 等級對 SR 有不同強度要求（如 SR 1.7 密碼強度，SL 2 與 SL 3 要求不同），專案須依目標 SL 填寫對應要求

---

## Secondary Mapping: IEC 62443-2-4 and 62443-3-2 Linkage {#appA-secondary-mapping}

### IEC 62443-2-4 Program Requirements Mapping {#appA-2-4-mapping}

IEC 62443-2-4 定義服務提供者之安全程序要求。本治理框架之 Gate 機制提供以下證據對應：

| 62443-2-4 Requirement Area | 治理控制點 | 預期證據 | 責任角色 |
|---------------------------|-----------|---------|---------|
| SP.01 Security Management | Gate 0 至 Gate 3 完整執行 | Gate 審查紀錄、核准文件 | System Design Governance Function |
| SP.02 Configuration Management | Gate 2: 設計變更管理 | 變更紀錄、版本管理文件 | System Architect |
| SP.03 Remote Access | Gate 1: 設計基線文件 | 遠端存取設計、Zone & Conduit Diagram | System Architect |
| SP.04 Event Management | Gate 1: 設計基線文件 | 事件管理設計、稽核設計 | System Architect |
| SP.05 Account Management | Gate 1: 設計基線文件 | 帳號管理設計（對應 FR1） | System Architect |
| SP.06 Patch Management | Gate 2: 設計變更管理 | 修補程序設計、變更控制 | System Architect |
| SP.07 Backup/Restore | Gate 1: 設計基線文件 | 備份/復原設計（對應 FR7） | System Architect |
| SP.08 Malware Protection | Gate 1: 設計基線文件 | 惡意程式防護設計（對應 FR3） | System Architect |

### IEC 62443-3-2 Risk Assessment Mapping {#appA-3-2-mapping}

IEC 62443-3-2 定義系統設計之風險評估方法。本治理框架之整合式風險評估（主文件 3.2 節）提供以下對應：

| 62443-3-2 Requirement | 治理控制點 | 預期證據 | 責任角色 |
|----------------------|-----------|---------|---------|
| ZCR 1: Asset Identification | Gate 0: 風險評估策略 | 資產清單、Zone 定義 | System Architect |
| ZCR 2: Zone and Conduit Model | Gate 1: Zone & Conduit Diagram | Zone & Conduit Diagram（Lite 或完整版） | System Architect |
| ZCR 3: Risk Assessment | Gate 1: 整合式風險評估報告 | IEC 62443-3-2 + FMEA + HAZOP 報告 | System Architect |
| ZCR 4: Security Requirements | Gate 1: IEC 62443 對應檢查表 | 本附錄「Primary Mapping Table」SR 檢查表 | System Architect |
| ZCR 5: Security Countermeasures | Gate 1: 設計基線文件 | 控制措施設計對應至 SR | System Architect |
| ZCR 6: Documentation | Gate 3: 最終設計文件包 | 所有設計文件、版本一致 | System Architect |
| ZCR 7: Risk Acceptance | Gate 3: 殘餘風險清單 | 殘餘風險清單（使用 Appendix C 模板） | Risk Acceptance Authority |

### Role of FMEA and HAZOP in Integrated Risk Assessment {#appA-fmea-hazop-role}

本治理框架之整合式風險評估（Integrated Risk Assessment）要求 IEC 62443-3-2、FMEA、HAZOP 三種方法並行執行（見主文件 3.2 節）。FMEA 與 HAZOP 並非 IEC 62443 合規框架，而是作為 IEC 62443-3-2 威脅識別之補充輸入，確保風險識別涵蓋資安威脅以外之失效模式與操作偏差。

**稽核證據追溯說明**：

- **IEC 62443-3-2 Threat Scenario**：識別資安威脅，產出 Threat Scenario ID（如 T-001）
- **FMEA Failure Mode**：識別系統失效模式，產出 Failure Mode ID（如 FM-SYS-001）
- **HAZOP Deviation**：識別操作流程偏差，產出 Deviation ID（如 HAZ-P001-D01）

Gate 3 殘餘風險清單中每個風險項目之 Risk Source ID，必須可追溯至上述三種來源之至少一種。此追溯機制確保所有殘餘風險皆有明確分析依據，而非憑空產生。FMEA 與 HAZOP 之模板與評分方法，請參閱 Appendix D。

---

## Security Level (SL) Determination Guidance {#appA-sl-guidance}

### SL Determination Process {#appA-sl-process}

依主文件 5.1 節規定：

1. **Gate 0**：System Architect 提出目標 SL 等級提案，基於系統用途、威脅環境、客戶要求
2. **Gate 1**：完成 SL 等級判定，驗證設計是否滿足目標 SL 之安全要求
3. **Gate 2**：設計變更若影響 SL 等級，必須重新評估並經核准
4. **Gate 3**：確認殘餘風險不影響目標 SL 等級之宣告

**SL 變更須經核准**：SL 等級降級必須由 Stakeholders 簽核接受（見主文件 5.1 節）。

### SL Decision Record Template {#appA-sl-template}

專案應於每個 Gate 使用以下模板記錄 SL 決策，並附於 Gate 審查文件：

```{=latex}
\begin{center}
\begin{tabular}{|p{12cm}|}
\hline
\multicolumn{1}{|c|}{\textbf{SL DECISION RECORD}} \\
\hline
\textbf{Project ID:} \underline{\hspace{4cm}} \\[0.3em]
\textbf{Gate:} $\square$ Gate 0 \quad $\square$ Gate 1 \quad $\square$ Gate 2 \quad $\square$ Gate 3 \\[0.3em]
\textbf{Date:} \underline{\hspace{3cm}} (YYYY-MM-DD) \\
\hline
\textbf{Target SL:} $\square$ SL 1 \quad $\square$ SL 2 \quad $\square$ SL 3 \quad $\square$ SL 4 \\[0.3em]
\textbf{SL Rationale:} \underline{\hspace{8cm}} \\[0.3em]
\underline{\hspace{11cm}} \\
\hline
\textbf{SL Changed from Previous Gate?} $\square$ Yes \quad $\square$ No \\[0.3em]
If Yes, Previous SL: \underline{\hspace{1.5cm}} Change Reason: \underline{\hspace{4cm}} \\[0.3em]
Change Approved By: \underline{\hspace{3cm}} Date: \underline{\hspace{2.5cm}} \\
\hline
\textbf{Applicable Zones} (if multiple SL): \\[0.3em]
\quad Zone Name: \underline{\hspace{3cm}} Target SL: \underline{\hspace{1.5cm}} \\[0.3em]
\quad Zone Name: \underline{\hspace{3cm}} Target SL: \underline{\hspace{1.5cm}} \\
\hline
\textbf{Prepared By:} \underline{\hspace{3cm}} (System Architect) \\[0.3em]
\textbf{Reviewed By:} \underline{\hspace{3cm}} (Security Team) \\[0.3em]
\textbf{Approved By:} \underline{\hspace{3cm}} (Gate Approver) \\[0.3em]
\textbf{Approval Date:} \underline{\hspace{3cm}} \\
\hline
\end{tabular}
\end{center}
```

---

## Gate-Ready Compliance Checklists {#appA-gate-checklists}

以下檢查表供各 Gate 審查時使用。每個檢查項目必須標註通過標準與證據來源。

### Gate 0 Compliance Checklist {#appA-gate0-checklist}

**重要說明**：Gate 0 為受理決策（Acceptance Decision），本檢查表用於驗證需求是否達到主文件所定義之品質門檻。本檢查表**不構成 Design Requesting Function 之強制提交清單**，而是系統設計部門內部評估工具。

| # | 品質門檻檢查 | 通過標準 | 判定依據 | 通過 |
|---|-------------|---------|---------|------|
| 1 | 可理解性 | 需求目標、範圍與預期成果可被理解，足以進行技術可行性評估 | 審查者判定 | [ ] |
| 2 | 可評估性 | 資訊足以評估技術可行性與識別基本風險假設 | 審查者判定 | [ ] |
| 3 | 需求擁有者明確性 | 存在明確之 Design Requesting Function | DRF 確認紀錄 | [ ] |
| 4 | 範圍穩定性 | 需求目標與範圍足夠穩定，可作為設計基線基礎 | 審查者判定 | [ ] |

**Gate 0 核准後之輸出驗證**（若 Gate 0 核准，須確認以下輸出存在）：

| # | 輸出項目 | 通過標準 | 證據來源 | 通過 |
|---|---------|---------|---------|------|
| 1 | 技術可行性初步判定 | 有書面或紀錄形式之可行性評估結論 | 可稽核紀錄 | [ ] |
| 2 | 目標 SL 等級初步提案 | SL Decision Record 或等效紀錄已填寫 | SL Decision Record | [ ] |
| 3 | 風險評估策略 | 明確後續將採用之風險分析方法及其範圍深度 | 風險評估策略紀錄 | [ ] |
| 4 | 初步風險識別 | 至少識別主要風險類別（安全、合規、技術） | 初步風險紀錄 | [ ] |

**Gate 0 Approver**: Engineering Management

### Gate 1 Compliance Checklist {#appA-gate1-checklist}

| # | 檢查項目 | 通過標準 | 證據來源 | 通過 |
|---|---------|---------|---------|------|
| 1 | 設計基線文件完整 | 包含系統架構圖、介面定義、資料流圖 | 設計基線文件 | [ ] |
| 2 | 整合式風險評估已完成 | IEC 62443-3-2、FMEA、HAZOP 三種方法皆有產出（Lite 或完整版） | 整合式風險評估報告 | [ ] |
| 3 | Zone & Conduit Diagram 已建立 | 至少識別關鍵信任邊界 | Zone & Conduit Diagram | [ ] |
| 4 | IEC 62443 對應檢查表已完成 | 「Primary Mapping Table」SR 檢查表已填寫，適用 SR 皆有 Status | IEC 62443 對應檢查表 | [ ] |
| 5 | 需求追溯矩陣已建立 | 關鍵設計決策可追溯至需求 | 需求追溯矩陣 | [ ] |
| 6 | 目標 SL 等級已確認 | SL Decision Record 已更新 | SL Decision Record | [ ] |
| 7 | 安全控制措施已定義 | 高風險項目皆有對應控制措施 | 設計基線文件、風險評估報告 | [ ] |
| 8 | 文件版本號已標註 | 所有文件有版本號、日期、擁有者 | 各文件標頭 | [ ] |
| 9 | 審查簽核已完成 | Security Team、QA Team 已完成審查 | 審查簽核紀錄 | [ ] |

**Gate 1 Approver**: System Design Governance Function

### Gate 2 Compliance Checklist {#appA-gate2-checklist}

| # | 檢查項目 | 通過標準 | 證據來源 | 通過 |
|---|---------|---------|---------|------|
| 1 | 變更描述與理由已記錄 | 變更內容與理由明確 | 變更申請文件 | [ ] |
| 2 | 影響分析已完成 | 識別受影響之模組、介面、需求 | 影響分析文件 | [ ] |
| 3 | 風險評估已更新 | 依 3.2.5 節觸發條件更新受影響之分析 | 更新後之風險評估文件 | [ ] |
| 4 | IEC 62443 對應已檢視 | 若變更影響 SR 對應，「Primary Mapping Table」檢查表已更新 | 更新後之 SR 檢查表 | [ ] |
| 5 | SL 等級影響已評估 | 若 SL 受影響，SL Decision Record 已更新並經核准 | SL Decision Record | [ ] |
| 6 | 設計文件版本號已遞增 | 變更後文件版本號一致遞增 | 更新後之設計文件 | [ ] |
| 7 | 重大變更已經核准 | 若符合重大變更定義，Engineering Management 已核准 | 核准紀錄 | [ ] |

**Gate 2 Approver**: Engineering Management

### Gate 3 Compliance Checklist {#appA-gate3-checklist}

| # | 檢查項目 | 通過標準 | 證據來源 | 通過 |
|---|---------|---------|---------|------|
| 1 | 最終設計文件包完整 | 所有文件標註版本號、發布日期、文件擁有者 | 最終設計文件包 | [ ] |
| 2 | 文件版本一致 | 所有文件引用相同基準版本號 | 版本一致性檢查 | [ ] |
| 3 | 整合式風險評估為完整版 | Gate 1 Lite 已升級為完整版 | 完整版風險評估報告 | [ ] |
| 4 | IEC 62443 對應檢查表完成 | 所有適用 SR 之 Status 為 Implemented 或 N/A（有簽核理由） | 完成之 SR 檢查表 | [ ] |
| 5 | 殘餘風險清單完整 | 使用 Appendix C 模板，每個風險有 Risk Source ID | 殘餘風險清單 | [ ] |
| 6 | 殘餘風險追溯有效 | QA Team 已抽查至少 20% 高風險項目之追溯 | QA 抽查紀錄 | [ ] |
| 7 | 殘餘風險已獲簽核接受 | 依主文件 5.2 節權限分級簽核 | 風險接受簽核紀錄 | [ ] |
| 8 | SL 等級宣告有效 | 殘餘風險不影響目標 SL 等級 | SL Decision Record | [ ] |
| 9 | 設計交付檢查表完成 | Gate 1、Gate 2 要求皆已滿足 | 設計交付檢查表 | [ ] |
| 10 | 交接會議已召開 | 設計團隊與執行團隊已召開交接會議 | 交接會議紀錄 | [ ] |
| 11 | 交接確認已記載 | 交接會議紀錄記載「專案執行單位已完成交接確認」 | 交接會議紀錄 | [ ] |
| 12 | 雙方簽核已完成 | System Architect + Project Manager 已簽核 | 交接會議紀錄簽核 | [ ] |

**Gate 3 Approver**: System Design Governance Function

---

## Document Control {#appA-doc-control}

- **Version**: 1.0
- **Effective Date**: 2026-01-08
- **Owner**: System Design Governance Function
- **Approved By**: Engineering Management
- **Review Cycle**: 與主文件同步，每年至少一次

本附錄之修訂依主文件 6.2 節流程辦理。附錄內容調整屬次要修訂，通知即可。

---

## CHANGELOG

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-09 | Initial release aligned with System Design Governance v1.0 |

**主要變更說明（相對於原版本）**：

1. **結構重組**：從簡單 Mapping Table 改為完整結構，涵蓋使用指引、FR1-FR7 完整 SR 對應、Gate 檢查表
2. **移除不正確引用**：刪除「Design Review Phase 2」等不存在於主文件之術語，改用正確 Gate 名稱
3. **移除預設 SL 2 聲明**：原版本宣稱「預設以 SL 2 為基準」，但主文件無此規定，已修正為「目標 SL 為專案特定」
4. **新增 FR1-FR7 完整 SR 對應模板**：提供可複製之 SR 檢查表模板，涵蓋所有 IEC 62443-3-3 SR
5. **新增 Status 定義**：明確定義 Implemented/Planned/N/A 之意義與證據要求
6. **新增 IEC 62443-2-4 與 3-2 對應表**：補充程序要求與風險評估方法之 Gate 證據對應
7. **新增 SL Decision Record 模板**：提供可附於 Gate 文件之 SL 決策紀錄模板
8. **新增 Gate 0-3 完整檢查表**：每個 Gate 提供具體檢查項目、通過標準、證據來源
9. **對齊主文件術語**：統一使用 System Design Governance Function、System Architect、交接會議紀錄等術語
10. **新增文件版本控制**：依主文件 6.2 節要求新增版本資訊

---

**文件結束**

```{=latex}
\disableLandscapeHeaderFooter
\end{landscape}
\pagestyle{fancy}
```
