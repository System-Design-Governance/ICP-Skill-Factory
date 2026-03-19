# ICP Skill Factory — Claude Code 治理規則

本文件整合自 `00-governance/SCHEMA.md` (v1.2) 與 `00-governance/CONVENTIONS.md` (v1.1)，
供 Claude Code 在 PR Review 時自動遵循。

---

## 1. SK Schema 驗證清單

每個 `SK-Dnn-nnn.md` 檔案必須包含兩個部分：

### Part A: YAML Metadata（13 個必要欄位）

位於 ` ```yaml ` 區塊內，`## Metadata` 標題下：

| 欄位 | 類型 | 必填 | 驗證規則 |
|------|------|------|----------|
| `skill_id` | String | ✅ | 格式 `SK-D{nn}-{nnn}`，須符合 CONVENTIONS §1 |
| `skill_name_en` | String | ✅ | Title Case，僅允許標準縮寫 |
| `skill_name_zh` | String | ✅ | 繁體中文顯示名稱 |
| `domain_id` | FK | ✅ | `D01`–`D14` |
| `subdomain_id` | FK | ✅ | `D{nn}.{n}` 格式 |
| `skill_type` | Enum | ✅ | Analysis/Design/Engineering/Testing/Documentation/Management/Verification/Governance/Integration/Operations |
| `tier` | Enum | ✅ | T1-Domain/T2-CapabilityGroup/T3-Skill/T4-AtomicSubskill |
| `maturity` | Enum | ✅ | Draft/Active/Deprecated/Retired |
| `version` | SemVer | ✅ | 例：`1.0.0` |
| `created_date` | Date | ✅ | ISO 日期格式 |
| `confidence` | Enum | ✅ | H+/H/M/L |
| `owner` | String | ❌ | 負責人或團隊 |
| `tags` | Text[] | ❌ | 自由標籤 |

可選欄位：`composition_patterns`（FK[] → CP，目前所有 171 個 SK 檔案皆為空陣列）。

### Part B: Prose Sections（14 個章節）

以 `##` 標題呈現於 YAML 區塊之後：

| 章節 | 必填 | 驗證規則 |
|------|------|----------|
| `## Description` | ✅ | 2–4 句範圍描述 |
| `## Inputs` | ✅ | 列出消費的文件/資料/上游 SK 輸出 |
| `## Outputs` | ✅ | 列出產出的交付物/產出物 |
| `## Tools` | ❌ | 使用的工具/平台 |
| `## Standards` | ❌ | 適用標準（IEC 62443, IEEE, NIST, ISO） |
| `## IEC 62443 Lifecycle Stages` | ❌ | Pre-R0/R0/R1/R2/R3/R4/R5 |
| `## Roles` | ❌ | 執行此技能的 ICP 角色 |
| `## Dependencies` | ❌ | 硬性（必要）和軟性（增強）技能依賴 |
| `## Automation Potential` | ❌ | Full/Partial/Human-Only |
| `## Acceptance Criteria` | ✅ | 3–6 項可觀察且可驗證的條件 |
| `## Estimated Effort` | ❌ | Junior vs Senior 人天基線 |
| `## Composition Patterns` | ❌ | CP-nnn 交叉引用 |
| `## Source Traceability` | ✅ | 文件 ID + 章節引用 |
| `## Footer` | ✅ | 版本戳記行 |

**不應出現的章節**：`## Workflow`/`## Process`、`## Pitfalls`/`## Anti-patterns`（設計決策，見 ADR-007）。

---

## 2. SKILL.md 品質評估標準

SKILL.md 品質依行數分為四級：

| 等級 | 行數門檻 | 說明 | 審查要求 |
|------|----------|------|----------|
| **A+** | ≥ 500 行 | 操作手冊等級，含完整範例、模板、參考資料 | 確認深度足夠，無填充內容 |
| **A** | 250–499 行 | 深度增強，含詳細步驟與參考矩陣 | 確認結構完整，步驟可執行 |
| **B** | 100–249 行 | 標準增強，生產就緒 | 確認覆蓋所有 SK 引用 |
| **C** | < 100 行 | 內容完整但偏短 | 標記為需要增強，建議補充 |

### SKILL.md 審查重點

- 必須引用對應的 SK 定義（`## SK Traceability` 或內文引用）
- 必須包含可執行的工作流程步驟
- 模板檔案（`templates/`）與參考檔案（`references/`）須存在且非空
- 觸發詞（Trigger）不得與其他 SKILL.md 衝突（見第 4 節）

---

## 3. Skill ID 與命名規則

### ID 格式

| 實體 | 格式 | 範例 |
|------|------|------|
| Domain | `D{nn}` | `D01` |
| Subdomain | `D{nn}.{n}` | `D01.2` |
| Skill Candidate | `SC-D{nn}-{nnn}` | `SC-D01-017` |
| Skill (已驗證) | `SK-D{nn}-{nnn}` | `SK-D01-003` |
| Sub-skill | `SK-D{nn}-{nnn}.{a}` | `SK-D01-003.a` |
| Composition Pattern | `CP-{nnn}` | `CP-001` |
| Decision Record | `ADR-{nnn}` | `ADR-004` |

### 命名規則

1. **雙語要求**：每個 Skill 必須有英文正式名稱 + 中文顯示名稱
2. **英文 Title Case**，僅允許業界標準縮寫：SCADA, EMS, DERMS, VPP, HMI, PLC, RTU, SIEM, SBOM, TRA, FAT, SAT, OPC UA
3. **動作型技能**：動詞開頭（Perform TRA, Design Zone/Conduit Architecture）
4. **知識型技能**：名詞開頭（IEC 62443 Compliance Framework）
5. **名稱不重複 Domain 前綴**（ID 已編碼 Domain 資訊）

### 檔案命名

- 所有檔案使用 kebab-case：`phase1-domain-map-approved.md`
- 資料夾以 Phase 編號為前綴：`00-governance/`、`01-domain-map/`
- SK 定義檔：`SK-D{nn}-{nnn}.md`

---

## 4. 觸發詞衝突偵測規則

審查 SKILL.md 時，必須檢查觸發詞（Trigger Words）是否與其他已存在的 SKILL.md 發生衝突：

### 衝突偵測流程

1. 提取 PR 中 SKILL.md 的觸發詞清單
2. 掃描 `05-cowork-skills/*/SKILL.md` 中所有既有觸發詞
3. 比對是否有完全相同或高度相似的觸發詞
4. 若發現衝突，在 PR Review 中標記為 **blocking issue**

### 衝突處理原則

- **完全相同觸發詞**：必須修改其中一方，不允許重複
- **高度相似觸發詞**：建議區分或合併，標記為 warning
- **跨 Plugin 觸發詞**：需確認是否為同一 Skill 的不同面向，參照 Overlap Resolution Rules

---

## 5. Overlap Resolution Rules（領域重疊解決規則）

以下為已裁定的領域邊界規則，PR Review 時須據此判斷 Skill 歸屬：

### 5.1 協定子領域 (CHG-004)
- **D02.3** = 架構層級協定選擇與拓撲設計
- **D05.5** = 裝置層級協定配置與閘道設定
- **D07.2** = 跨系統協定轉譯

### 5.2 變更管理 (CHG-005)
- **D10.2** = 專案特定變更請求（執行層）
- **D11.2** = 標準作業程序，D10.2 實例所遵循的（治理層）

### 5.3 Pre-Gate / Post-Gate 邊界 (ADR-005)
- **D14** = Gate 0 之前（合約簽訂前的技術執行）
- **D10** = 合約啟動後至專案結束（R1–R5）
- Gate 0 核准 / 合約授予為生命週期邊界
- D14.1 範圍框架饋入 D10.1 需求基線

### 5.4 VPP 電力面 / 控制面邊界 (REC-002)
- **D03.4** = VPP 電力系統面：聚合策略、調度邏輯、市場參與規則
- **D05.2** = VPP 控制系統面：DERMS 軟體配置、通訊設定、即時控制迴路
- 區分原則：標的為「電力系統行為」歸 D03.4，標的為「控制軟體配置」歸 D05.2

### 5.5 資料分析 / AI 輔助工程邊界 (REC-001)
- **D12.3** = 以能源資料為標的的分析建模（含 AI/ML 工具）
- **D13.2** = 以工程流程為標的的 AI 輔助能力
- 區分原則：標的為「資料」歸 D12，標的為「工程流程」歸 D13

### 5.6 能力管理歸屬 (ADR-006)
- **D11.6** = 工程能力管理（通用），涵蓋所有領域的能力框架、培訓、資格追蹤
- 各領域專業能力認證統一於 D11.6 管理，不在各域重複建立

---

## 6. Skill Type 分類定義

| 類型 | 定義 | 範例 |
|------|------|------|
| Analysis | 檢視資料/系統以產出發現 | 風險評估、電力潮流分析 |
| Design | 建立規格、架構、計畫 | Zone/Conduit 架構設計 |
| Engineering | 實作/配置技術系統 | SCADA 資料庫配置 |
| Testing | 依需求驗證/確認 | FAT 執行、滲透測試 |
| Documentation | 產出書面交付物 | TRA 報告撰寫 |
| Management | 協調人員、流程、資源 | 專案安全規劃 |
| Verification | 獨立檢查流程/產出合規性 | 安全設計審查 |
| Governance | 定義/執行標準與政策 | 安全政策開發 |
| Integration | 連接異質系統/資料 | 協定閘道配置 |
| Operations | 持續監控、維護、回應 | 安全監控、事件回應 |

---

## 7. 依賴引用規則

- SC-ID 佔位符使用 `⏳` 標記未升級的引用
- 格式：`SC-D01-005 ⏳: Asset Inventory Development — provides the asset baseline`
- 當目標技能升級為 SK 時，所有佔位符引用須批次更新

---

## 8. PR Review 快速檢核表

審查 PR 時，依變更類型執行以下檢查：

### SK 定義變更 (`03-skill-definitions/**`)
- [ ] YAML Metadata 13 個必填欄位皆存在且格式正確
- [ ] `skill_id` 符合 `SK-D{nn}-{nnn}` 格式
- [ ] `skill_type` 為 10 種合法值之一
- [ ] `tier` 為 4 種合法值之一
- [ ] 6 個必填 Prose Section 皆存在
- [ ] Acceptance Criteria 3–6 項，可觀察且可驗證
- [ ] 無 `## Workflow` 或 `## Pitfalls` 章節
- [ ] Source Traceability 引用具體文件 ID + 章節

### SKILL.md 變更 (`05-cowork-skills/**`)
- [ ] 品質等級達 B 以上（≥ 100 行）
- [ ] 引用對應 SK 定義
- [ ] 觸發詞無衝突
- [ ] 模板與參考檔案存在且非空

### Plugin 變更 (`06-plugin-src/**`)
- [ ] `plugin.json` 格式正確（name, version, description, author）
- [ ] version 遵循 SemVer
- [ ] 所有 skills/ 子目錄包含有效 SKILL.md

### 治理文件變更 (`00-governance/**`)
- [ ] 版本號已遞增
- [ ] CHANGELOG.md 已更新
- [ ] 不違反既有 ADR 決策
