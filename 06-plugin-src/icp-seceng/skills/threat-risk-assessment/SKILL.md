---
name: threat-risk-assessment
description: >
  Execute comprehensive threat and risk assessment for OT/ICS/SCADA cybersecurity projects.
  Covers the full TRA lifecycle: asset inventory, preliminary HLCRA, detailed risk assessment (DTRA),
  STRIDE/DREAD threat modeling, risk classification matrix, integrated assessment (IEC+FMEA+HAZOP),
  and risk source traceability with residual risk register.
  MANDATORY TRIGGERS: 威脅與風險評估, threat risk assessment, 風險評估, risk assessment,
  資產清冊, asset inventory, HLCRA, 初步風險評估, preliminary TRA, 詳細風險評估, DTRA,
  detailed risk assessment, STRIDE, DREAD, 威脅建模, threat modeling, 風險矩陣,
  risk classification matrix, FMEA, HAZOP, 整合風險評估, integrated risk assessment,
  殘餘風險, residual risk, 風險登錄冊, risk register, 風險溯源, risk traceability,
  zone mapping, 風險分類矩陣建立.
  Use this skill for any threat/risk assessment task in OT/ICS/SCADA cybersecurity and
  energy infrastructure projects. Covers Pre-Gate through R3 lifecycle.
---

# 威脅與風險評估 (Threat & Risk Assessment)

本 Skill 整合 7 個工程技能定義，提供 OT/ICS 資安威脅與風險評估的完整工作流程——從資產清冊建立到殘餘風險登錄。適用於 IEC 62443 生命週期 R0–R3 各階段。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得 SuC (System under Consideration) 範圍定義與系統邊界
2. **輸入文件**：§1 輸入清單已備齊或已標註 TBD
3. **適用標準**：確認本專案 IEC 62443 / ISO 標準版本
4. **前置 SK 產出**：確認以下可用
   - SK-D01-001 (Zone/Conduit Design)
   - SK-D01-002 (Defense-in-Depth)
   - SK-D02-001 (OT Network Topology)
   - SK-D02-004 (Data Flow Diagram)
   - SK-D14-001 (Requirements)

**⚠️ 若為 Presales 階段 (Pre-R0)**：步驟 1-2 為最小可行範圍，步驟 3-7 可在 R1/R2 階段執行。

---

## 1. 輸入

| 類別 | 輸入項目 | 來源 |
|------|---------|------|
| 範圍 | SuC 範圍定義 | SOW / 合約 |
| 架構 | 初步網路架構圖 | SK-D02-001 |
| 架構 | 資料流圖 (DFD) | SK-D02-004 |
| 資產 | 設備清單、SLD、CMDB 匯出 | 客戶提供 |
| 場勘 | 場勘紀錄 (brownfield) | SK-D14-011 |
| 場勘 | 既有基礎設施清冊 (brownfield) | SK-D14-012 |
| 標準 | IEC 62443-3-2 Zone/Conduit 指引 | 標準文庫 |
| 威脅 | 威脅來源目錄 (ICS-CERT, MITRE ATT&CK for ICS) | 公開資料 |
| 需求 | RPO/RTO 目標 | 客戶需求 |

---

## 2. 工作流程

### Step 1: 資產清冊建立 (SK-D01-005)

**目標**：建立 SuC 內所有實體與邏輯資產的完整清冊，含 criticality 分級。

**操作步驟**：

1. **定義範圍**：從 SOW/合約確認 SuC 邊界，列出 In-Scope / Out-of-Scope
2. **資產發現**：
   - Greenfield：從設計圖面、BOQ 提取
   - Brownfield：實體場勘 + 被動網路掃描（需 PtW 核准）
3. **資產分類**：按類型登錄——HMI, IED, PLC/RTU, Switch, WAP, IT infra, Software
4. **指定唯一 ID**：格式 `A-{Zone}-{nnn}` (如 `A-DMZ-001`)
5. **Zone 指派**：每個資產指派所屬 Zone，對照 Zone/Conduit 設計 (SK-D01-001)
6. **Criticality 分級**：High / Medium / Low，附書面理由
7. **Conduit 映射**：記錄跨 Zone 通訊路徑（協定、方向、頻率）
8. **假設登錄**：無法直接觀察的資產（廠商管理、雲端服務等）記錄假設與信心等級

**交付物**：

```markdown
# 資產清冊 (Asset Inventory Register) — {專案名稱}

| Asset ID | 資產名稱 | 類型 | 廠牌/型號 | FW/SW 版本 | IP/MAC | 位置 | Zone | Conduit | Criticality | 資料分類 | 備註 |
|----------|---------|------|----------|-----------|--------|------|------|---------|------------|---------|------|
| A-DMZ-001 | Edge Firewall | FW | FortiGate 60F | v7.4.1 | 10.0.0.1 | 機房-R1 | DMZ | C1,C2 | High | — | — |
| A-OFC-001 | Core Switch | SW | Cisco CBS350 | — | 10.10.0.1 | 機房-R1 | Office IT | C1,C3 | Medium | — | — |
```

```markdown
# Zone 指派摘要表

| Zone ID | Zone 名稱 | SL-T | 資產數 | 包含資產 | 指派理由 |
|---------|----------|------|--------|---------|---------|
| Z-01 | DMZ | SL-2 | 3 | A-DMZ-001~003 | 邊界隔離 |
```

**⚠️ 避坑指引**：
- Brownfield 環境常有未文件化的 legacy 設備，工時可能需 2-3 倍
- 非網路化資產（實體門禁、手動開關）容易遺漏——需場勘+訪談
- 不要省略 firmware 版本——這是供應鏈風險的關鍵欄位
- 假設未記錄會在 Gate 3 驗證時產生 traceability 缺口

---

### Step 2: 初步威脅風險評估 / HLCRA (SK-D01-006)

**目標**：基於資產清冊和初步架構，進行高階網路風險評估 (HLCRA)。

**操作步驟**：

1. **威脅來源辨識**：使用 ICS-CERT top threats + MITRE ATT&CK for ICS
2. **威脅-弱點矩陣**：每個威脅 × 每個 Zone/資產，初步 impact scoring
3. **資料保護需求**：辨識所有受保護資料類型（法規、商業機密、組態、營運、稽核）
4. **風險分類**：使用核准的 Likelihood × Impact 矩陣 (見 Step 5)
5. **風險編碼**：每筆風險指定 `T-{nnn}` 識別碼 (依 GOV-SD traceability 要求)
6. **初步處置方向**：Mitigate / Accept / Transfer / Avoid
7. **編寫 TRA 報告**：依 ID11 範本格式

**TRA 報告結構** (依 ID11 exemplar)：

```markdown
# 初步威脅風險評估報告 (Preliminary TRA) — {專案名稱}

## §1 Introduction
- 目的、範圍、評估方法論

## §2 Security Context
- SuC 描述、資產摘要、網路架構、資料流、威脅來源

## §3 Risk Assessment Results
- HLCRA proforma：威脅-弱點矩陣、衝擊分析、風險分類

## §4 Preliminary Risk Register
| Risk ID | 威脅描述 | 影響 Zone/資產 | Likelihood | Impact | Risk Level | 處置方向 |
|---------|---------|--------------|-----------|--------|-----------|---------|
| T-001 | Unauthorized remote access via VPN | DMZ | Medium | High | High | Mitigate |
| T-002 | Malware propagation via USB | OT Zone | Low | Critical | High | Mitigate |

## §5 Data Safeguarding Requirements
| 資料類型 | 分類 | 保護方式 |
|---------|------|---------|
| 法規/合規 | Confidential | 加密存儲+存取控制 |
| 營運數據 | Internal | 備份+完整性校驗 |

## §6 Security Profile Summary
- 整體風險態勢、下游設計建議
```

**⚠️ 避坑指引**：
- 使用通用威脅庫但未針對 OT/ICS 客製化 → 漏掉 safety-critical 威脅
- 風險描述使用模糊語言 ("may", "could") → 改用具體攻擊場景描述
- 未涵蓋資料保護需求 → Gate 1 Lite 審查不通過
- 不同評估人員的風險矩陣 scoring 不一致 → 需建立 scoring guideline

---

### Step 3: 詳細風險評估 / DTRA (SK-D01-007)

**目標**：將初步 TRA 深化為具體安全控制需求，推導 FR/SR mapping。

**前提**：需已完成 Zone/Conduit 設計 (SK-D01-001) 和 SL-T 指定 (SK-D01-010)。

**操作步驟**：

1. **審閱初步 TRA**：確認所有 T-xxx 風險均需深化
2. **盤點現有控制**：記錄 current-state security controls
3. **FR/SR 推導**：對每個 Zone，依 IEC 62443-3-3 推導 Functional Requirements (FR) 和 System Requirements (SR)
4. **對策規格**：按五大功能區域指定具體對策：
   - Data Protection（儲存點+資料流保護）
   - Hardware Protection（實體存取、防竄改）
   - System Administration（帳號管理、稽核日誌）
   - Application Security（輸入驗證、Session 管理）
   - Network Security（分段強化、協定過濾）
5. **殘餘風險**：計算 countermeasure 實施後的殘餘風險等級
6. **風險接受簽核**：依 GOV-SD 層級路由

**FR/SR Mapping 模板**：

```markdown
| Zone | FR | SR | 狀態 | 設計證據 | 備註 |
|------|----|----|------|---------|------|
| DMZ | FR1 (AC) | SR 1.1 | Implemented | arch-doc §3.2 | — |
| DMZ | FR2 (UC) | SR 2.1 | Planned | — | Gate 3 前完成 |
| OT Zone | FR5 (RDF) | SR 5.1 | Implemented | DFD §4 | Data Diode |
```

**殘餘風險接受層級** (GOV-SD)：

| 殘餘嚴重度 | 接受權限 |
|-----------|---------|
| Low | PM only |
| Medium | PM + Security (SAC/ISM) |
| High | PM + Security + Business (Executive) |
| Critical | Engineering Management + All Above (需 RCA + 替代控制) |

**⚠️ 避坑指引**：
- 在 Zone/Conduit 設計定案前進行 DTRA → 需重做，建立 design stability checkpoint
- FR/SR mapping 用通用目錄未考慮 Zone-specific SL-T → 需 zone-specific selection
- 殘餘風險未附 control effectiveness 證據 → Gate 3 驗證不通過
- Gate 3 要求「Implemented」，不接受「Planned」狀態的 SR

---

### Step 4: STRIDE/DREAD 威脅建模 (SK-D01-008)

**目標**：系統性列舉 OT/ICS 威脅並量化風險排序。

**Phase 1 — System Decomposition**：
- 將 OT/ICS 架構分解為 threat-modeling units (assets, processes, data flows, actors)
- 對齊 Zone/Conduit 設計，辨識 trust boundaries

**Phase 2 — STRIDE 威脅列舉**：
對每個系統元件，按六類威脅系統性列舉：

| STRIDE | OT/ICS 情境範例 |
|--------|---------------|
| **S**poofing | 偽造 SCADA 伺服器身份、spoofed sensor readings |
| **T**ampering | 竄改 safety-critical setpoints、修改 historian 日誌 |
| **R**epudiation | 停用稽核日誌、否認控制操作 |
| **I**nfo Disclosure | 竊聽即時數據、提取 credential |
| **D**enial of Service | 網路洪泛、崩潰主機 |
| **E**levation of Privilege | Operator→Admin、利用漏洞提權 |

**Phase 3 — DREAD 評分**：
每個威脅按五維度打分 (1=Low, 2=Medium, 3=High)：

| 維度 | 評分指引 |
|------|---------|
| **D**amage | 1: 輕微 / 2: 設施營運受影響 / 3: 安全事故或環境危害 |
| **R**eproducibility | 1: 極難重現 / 2: 需特定條件 / 3: 隨時可重現 |
| **E**xploitability | 1: 需專家+特殊工具 / 2: 中等技能 / 3: 腳本即可 |
| **A**ffected Users | 1: 單一設備 / 2: 一個場域 / 3: 全企業 |
| **D**iscoverability | 1: 極隱蔽 / 2: 需主動探索 / 3: 公開已知 |

**Overall Score** = (D+R+E+A+D) / 5，≥2.4 為 High-risk，優先設計控制。

**威脅目錄模板**：

```markdown
| Threat ID | STRIDE | 威脅描述 | D | R | E | A | D | Score | Zone | IEC 62443 FR |
|-----------|--------|---------|---|---|---|---|---|-------|------|-------------|
| T-001 | S | 偽造 HMI 登入憑證 | 2 | 2 | 3 | 2 | 3 | 2.4 | OT | FR1 (AC) |
| T-002 | T | 竄改 PLC setpoint | 3 | 1 | 2 | 1 | 2 | 1.8 | OT | FR3 (SI) |
| T-003 | D | Modbus flood 導致 RTU 停擺 | 3 | 3 | 3 | 2 | 3 | 2.8 | OT | FR7 (RA) |
```

**⚠️ 避坑指引**：
- 使用通用 STRIDE 清單未適配 OT → Tampering 應聚焦 safety setpoints 而非一般 data
- DREAD 打分無共識 → 需多方參與 consensus scoring session
- 威脅目錄與 FMEA/HAZOP 脫鉤 → 確保 T-XXX 與 FM-XXX/HAZ-XXX 有交叉引用
- 高估理論攻擊路徑 → 用 Exploitability/Discoverability 反映實際可行性

---

### Step 5: 風險分類矩陣 (SK-D01-009)

**目標**：建立專案的 Likelihood × Impact 風險分類矩陣。

**操作步驟**：

1. 定義 **Likelihood 量表** (含定性描述+定量區間)：

| 等級 | 描述 | 量化 (年) |
|------|------|----------|
| 1-Rare | 幾乎不可能 | < 0.01 |
| 2-Unlikely | 不太可能 | 0.01 - 0.1 |
| 3-Possible | 可能發生 | 0.1 - 1.0 |
| 4-Likely | 很可能 | 1.0 - 10 |
| 5-Almost Certain | 幾乎確定 | > 10 |

2. 定義 **Impact 量表** (四維度最低要求)：

| 等級 | 營運/可用性 | 安全/人身 | 財務/商業 | 聲譽/合規 |
|------|-----------|----------|----------|----------|
| 1-Negligible | 無感 | 無 | < 10萬 | 無 |
| 2-Minor | 短暫中斷 (<1hr) | 輕傷可能 | 10-100萬 | 媒體關注 |
| 3-Moderate | 局部中斷 (<8hr) | 可能受傷 | 100-500萬 | 監管關注 |
| 4-Major | 全面中斷 (<24hr) | 嚴重傷害 | 500-2000萬 | 裁罰 |
| 5-Catastrophic | 長期中斷 (>24hr) | 死亡可能 | > 2000萬 | 執照撤銷 |

3. 建立 **5×5 風險矩陣**：

```
        Impact →   1    2    3    4    5
Likelihood ↓
    5            M    H    H    C    C
    4            M    M    H    H    C
    3            L    M    M    H    H
    2            L    L    M    M    H
    1            L    L    L    M    M

L=Low(綠) M=Medium(黃) H=High(橙) C=Critical(紅)
```

4. 定義 **容忍閾值**：
   - **Acceptable (L)**：無需額外行動
   - **Tolerable (M)**：需控制措施，PM 核准
   - **Unacceptable (H/C)**：必須降低至 M 以下，或經指定權限接受

**⚠️ 避坑指引**：
- 量表與組織風險偏好不一致 → 需 stakeholder alignment workshop
- 缺少維度專屬評分指引 → 每個維度需附範例情境
- 僅 SAC 核准 → 需 Risk Manager + Stakeholder 三方簽核

---

### Step 6: 整合風險評估 IEC+FMEA+HAZOP (SK-D01-035)

**目標**：三方法整合評估——IEC 62443 (cyber) + FMEA (reliability) + HAZOP (safety)。

**FMEA 工作表**：

```markdown
| FM ID | 元件/功能 | 失效模式 | 後果 | L | S | D | RPN | 建議措施 |
|-------|---------|---------|------|---|---|---|-----|---------|
| FM-001 | PLC CPU | Firmware crash | 控制迴路中斷 | 2 | 3 | 2 | 12 | Redundant PLC |
| FM-002 | HMI 顯示 | 顯示凍結 | 操作員誤判 | 2 | 2 | 3 | 12 | Watchdog alarm |
```
RPN = Likelihood × Severity × Detection (1-3 scale each, max 27)

**HAZOP 引導詞**：

| 引導詞 | 偏差類型 | OT 範例 |
|--------|---------|--------|
| NO | 完全無 | 無通訊 → 控制迴路失效 |
| MORE | 過多 | 過高電壓 → 設備損壞 |
| LESS | 不足 | 採樣率不足 → 事件偵測延遲 |
| REVERSE | 反向 | 電流反灌 → 變壓器損壞 |
| AS WELL AS | 額外 | 正常流量+惡意流量 → 資料外洩 |

**Cross-Method Mapping**：

```markdown
| 整合 Risk ID | T-XXX (Cyber) | FM-XXX (FMEA) | HAZ-XXX (HAZOP) | 統一評分 | 建議控制 |
|-------------|--------------|--------------|----------------|---------|---------|
| IR-001 | T-003 | FM-001 | HAZ-005 | High | Redundant PLC + Network segmentation |
| IR-002 | T-001 | — | HAZ-002 | Medium | MFA + Access logging |
```

**Gate 3 驗證抽樣**：
- 抽樣 ≥20% 整合風險 (最少 10 項)
- 三種佐證類型：
  - **Type 1**：≥2 方法識別相同風險，嚴重度一致
  - **Type 2**：一方法識別，另一方法調查確認
  - **Type 3**：專家審查確認為真實可信風險

**⚠️ 避坑指引**：
- 三方法各自獨立不整合 → 需同一團隊 concurrent 執行+cross-reference
- 統一評分偏重 cyber 忽略 safety → 需平衡三維度
- Gate 3 抽樣不足 20% → 自動 fail

---

### Step 7: 風險溯源與殘餘風險登錄 (SK-D01-036)

**目標**：建立風險 traceability chain 和版本控制的殘餘風險登錄冊。

**Risk Identifier System**：

| 前綴 | 來源方法 | 範例 |
|------|---------|------|
| T-XXX | IEC 62443 Threat Catalog | T-001 ~ T-NNN |
| FM-XXX | FMEA Failure Modes | FM-001 ~ FM-NNN |
| HAZ-XXX | HAZOP Deviations | HAZ-001 ~ HAZ-NNN |

**Traceability Chain**：
```
Risk Source → Risk Characteristics (L, I, Severity)
  → Assigned Countermeasures → Implementation Status
    → Residual Risk Assessment → Acceptance Decision
```

**殘餘風險登錄冊模板**：

```markdown
# 殘餘風險登錄冊 (Residual Risk Register) — {專案名稱}

| Risk ID | 原始描述 | 原始等級 | 實施控制 | 殘餘 L | 殘餘 I | 殘餘等級 | 接受權限 | 接受日期 | Risk Owner | 監控頻率 |
|---------|---------|---------|---------|-------|-------|---------|---------|---------|-----------|---------|
| T-001 | Unauthorized remote access | High | MFA + VPN + Logging | 2 | 3 | Medium | PM+SAC | 2026-04-15 | SAC | Quarterly |
| FM-001 | PLC firmware crash | High | Redundant PLC + Watchdog | 1 | 3 | Medium | PM+SAC | — | SYS | Monthly |
```

**Risk Owner 職責**：
- 監控殘餘風險狀態
- 觸發升級時通報 (escalation triggers 需事先定義)
- 季度 review 報告

---

## 3. 輸出 / 交付物總覽

| # | 交付物 | 對應步驟 | 格式 |
|---|--------|---------|------|
| 1 | Asset Inventory Register | Step 1 | Excel/Markdown |
| 2 | Zone Assignment Summary | Step 1 | Markdown |
| 3 | Asset-to-Conduit Mapping | Step 1 | Markdown |
| 4 | Preliminary TRA Report (HLCRA) | Step 2 | Markdown/Word |
| 5 | Threat-Vulnerability Matrix | Step 2 | Markdown |
| 6 | Preliminary Risk Register (T-XXX) | Step 2 | Markdown/Excel |
| 7 | Detailed Risk Assessment (DTRA) | Step 3 | Markdown/Word |
| 8 | FR/SR Mapping Matrix | Step 3 | Markdown/Excel |
| 9 | Risk Treatment Plan | Step 3 | Markdown |
| 10 | STRIDE Threat Catalog | Step 4 | Markdown |
| 11 | DREAD Risk Ranking | Step 4 | Markdown |
| 12 | Risk Classification Matrix | Step 5 | Markdown |
| 13 | Integrated Risk Assessment Report | Step 6 | Markdown/Word |
| 14 | FMEA Summary (FM-XXX) | Step 6 | Markdown/Excel |
| 15 | HAZOP Study Report (HAZ-XXX) | Step 6 | Markdown |
| 16 | Cross-Method Traceability Matrix | Step 6 | Markdown |
| 17 | Gate 3 Verification Report | Step 6 | Markdown |
| 18 | Residual Risk Register | Step 7 | Markdown/Excel |
| 19 | Risk Traceability Matrices | Step 7 | Markdown |

---

## 4. 適用標準

| 標準 | 用途 |
|------|------|
| IEC 62443-3-2 | 主方法論：Zone-based risk assessment |
| IEC 62443-3-3 | FR/SR 要求推導 |
| IEC 62443-1-1 | 術語、概念、模型 |
| IEC 62443-2-1 | 安全管理系統、資產管理 |
| IEC 62443-4-2 | 元件安全要求 |
| ISO 27005 | 資訊安全風險管理框架 (補充) |
| ISO 31000 | 風險管理原則 (補充) |
| NIST SP 800-82 Rev. 3 | OT Security 威脅脈絡 (補充) |
| NIST SP 800-30 Rev. 1 | Risk Assessment Framework |
| IEC 61508 / ISA-84 | FMEA/HAZOP 功能安全基礎 |

---

## 5. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 資產覆蓋率 | 清冊涵蓋 SuC 100% 資產，無未文件化遺漏 |
| 2 | Zone 指派 | 每個資產有唯一 ID + 已指派 Zone + Criticality + 書面理由 |
| 3 | 威脅覆蓋 | 威脅目錄含 ICS-CERT top threats 且已適配 OT/ICS |
| 4 | 風險編碼 | 每筆風險有 T-XXX / FM-XXX / HAZ-XXX 唯一編碼 |
| 5 | FR/SR 完整 | 所有 Zone 的每個 applicable SR 狀態為 Implemented (非 Planned) |
| 6 | DREAD 完整 | 每個威脅有五維度 numeric 分數 (非區間或定性) |
| 7 | Gate 3 抽樣 | ≥20% 整合風險完成佐證驗證 |
| 8 | 殘餘風險簽核 | 依 GOV-SD 權限層級簽核 (Low→PM; Medium→PM+SAC; High→Executive) |
| 9 | 資料保護 | 所有受保護資料類型已辨識並指定保護方式 |
| 10 | Traceability Chain | 每筆風險可追溯：來源→特徵→對策→實施→殘餘→接受 |

---

## 6. 工時參考

| 步驟 | Junior (< 2yr) | Senior (5+ yr) | 備註 |
|------|---------------|----------------|------|
| Step 1 資產清冊 | 8-12 pd | 4-6 pd | 單站 ~50 資產 greenfield |
| Step 2 初步 TRA | 10-15 pd | 5-8 pd | ID04 §9.0 基準 ~10 pd |
| Step 3 DTRA | 18-25 pd | 10-15 pd | ~20 risk entries + FR/SR |
| Step 4 STRIDE/DREAD | 5-8 pd | 3-5 pd | 需 workshop 共識 |
| Step 5 風險矩陣 | 2-3 pd | 1-2 pd | 含 stakeholder alignment |
| Step 6 IEC+FMEA+HAZOP | 15-20 pd | 8-12 pd | 三方法整合 |
| Step 7 Traceability | 5-8 pd | 3-5 pd | 含 Gate 3 準備 |

Brownfield + legacy：× 2-3 倍。複雜多站：按站數線性增加。

---

## 7. 工具指引

| 工具 | 用途 | 備註 |
|------|------|------|
| Excel | 資產清冊、風險登錄冊、FR/SR matrix | 主要作業工具 |
| MITRE ATT&CK Navigator | ICS 威脅辨識 | 免費線上工具 |
| ICP TRA Report Template | 報告格式 | 依 ID11 exemplar |
| STRIDE/DREAD Worksheet | 威脅列舉+評分 | 本 Skill 模板 |
| FMEA Worksheet | 失效模式分析 | RPN 計算 |
| HAZOP Study Guide | 引導詞+偏差分析 | 搭配 process flow |
| GOV-SD Appendix C | 殘餘風險登錄格式 | 版本控制 |

---

## 8. 人類審核閘門 (Human Review Gate)

完成所有步驟後暫停，提交 SAC 審核：

```
威脅與風險評估已完成。
📋 執行範圍：7 步驟（資產清冊→HLCRA→DTRA→STRIDE/DREAD→風險矩陣→IEC+FMEA+HAZOP→風險溯源）
📊 關鍵數據：
  - 資產數：{n} 項（High: {h}, Medium: {m}, Low: {l}）
  - 威脅數：{t} 項（DREAD ≥2.4 High-risk: {hr} 項）
  - 殘餘風險：{rr} 項（Critical: {c}, High: {h}, Medium: {m}）
  - FR/SR 覆蓋：{fr_pct}% Implemented
⚠️ 待確認：{TBD 項目/假設/需權限簽核的殘餘風險}
👉 請 SAC 審核以上成果，確認 PASS / FAIL / PASS with Conditions。
```

**審核焦點**：
- 資產清冊覆蓋率是否 100%
- 威脅目錄是否已適配 OT/ICS 場景
- DREAD 評分是否有共識基礎
- FR/SR mapping 是否 zone-specific
- 殘餘風險接受權限是否正確路由

---

## 9. IEC 62443 生命週期對應

| Lifecycle | 本 Skill 角色 | 執行步驟 |
|-----------|-------------|---------|
| Pre-R0 | 初步範圍界定 | Step 1 (基本), Step 2 (概略) |
| R0/R1 | Gate 0/1 風險基線 | Step 1-2 完整, Step 5 |
| R1/R2 | 設計基線風險評估 | Step 3-4, Step 6 |
| R2/R3 | 實施驗證 | Step 6 (Gate 3), Step 7 |

---

## 10. Source Traceability

| SK 編號 | 名稱 | 核心知識 |
|--------|------|---------|
| SK-D01-005 | Asset Inventory Development | 資產發現、分類、criticality、Zone 指派、Conduit 映射 |
| SK-D01-006 | Preliminary TRA (HLCRA) | 威脅來源辨識、威脅-弱點矩陣、資料保護、T-XXX 編碼 |
| SK-D01-007 | Detailed Risk Assessment (DTRA) | FR/SR 推導、五區域對策、殘餘風險、GOV-SD 接受層級 |
| SK-D01-008 | STRIDE/DREAD Threat Modeling | 六類威脅列舉、五維度 DREAD 評分、OT/ICS 適配 |
| SK-D01-009 | Risk Classification Matrix | Likelihood/Impact 量表、5×5 矩陣、容忍閾值 |
| SK-D01-035 | Integrated Assessment (IEC+FMEA+HAZOP) | 三方法整合、FMEA RPN、HAZOP 引導詞、Gate 3 抽樣 |
| SK-D01-036 | Risk Traceability & Residual Register | T/FM/HAZ 編碼系統、traceability chain、季度 review |

<!-- Phase 6: Deep enhancement from 7 SK definitions. Enhanced 2026-03-18. -->
