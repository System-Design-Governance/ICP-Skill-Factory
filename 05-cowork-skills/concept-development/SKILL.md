---
name: concept-development
description: >
  Develop concept-level system architecture and preliminary security classification for
  Pre-Gate 0 OT/ICS cybersecurity projects. Produces non-binding concept Zone/Conduit
  architecture, preliminary SL-T proposals, and Gate 0 feasibility inputs.
  MANDATORY TRIGGERS: 概念架構, concept architecture, 概念設計, concept design,
  概念 Zone/Conduit, concept zone conduit, 初步安全分類, preliminary security classification,
  Pre-Gate 0, 可行性輸入, feasibility input, 概念 SL-T, concept SL-T,
  初步分區, preliminary zoning, 安全分類, security classification.
  Use this skill for pre-gate concept architecture and security classification work.
---

# 概念設計與初步安全分類 (Concept Design & Preliminary Security Classification)

本 Skill 整合 3 個工程技能定義，產出 Gate 0 所需的概念架構和初步安全分類——這些都是 advisory (非約束性)，Gate 0 核准後由 SYS/SAC 在 R1 正式化。

---

## 0. 初始化

1. **需求**：SK-D14-001 需求規格已產出 (或 SOW/RFP 可用)
2. **場勘**：site-assessment Skill 產出可用 (Brownfield)
3. **可行性**：SK-D14-003 可行性評估可用 (或同步進行)
4. **IEC 62443**：標準文件可參考

---

## 1. 工作流程

### Step 1: 概念 Zone/Conduit 架構 (SK-D14-013)

**目標**：建立概念級 (non-binding) 網路分段和通訊管道架構，作為 Gate 0 五大必要輸入之一。

**操作步驟**：

1. **辨識安全 Zone** (≥3 zones)：
   ```markdown
   | Zone | 功能 | 典型設備 | 概念 SL-T |
   |------|------|---------|----------|
   | Enterprise IT | 辦公/Email | PC, AD, File Server | SL-1 |
   | DMZ | 邊界隔離 | Firewall, Proxy | SL-2 |
   | OT Control | SCADA/HMI | HMI, Historian, Switch | SL-2~3 |
   | Field | 現場設備 | PLC, RTU, Sensor | SL-2 |
   | SIS (如有) | 安全系統 | SIS Controller | SL-3 |
   ```

   **IEC 61850 變電所標準 Zone 分層**（當專案涉及變電所時，使用以下進階分層）：
   ```markdown
   | Purdue | Zone | 功能 | 典型設備 | 概念 SL-T |
   |--------|------|------|---------|----------|
   | L4 | Enterprise | 公司 IT/ERP | ERP, ADCC, Remote WS | SL-1 |
   | L3.5 | DMZ | IT/OT 邊界 | Firewall, Jump Server, Data Diode | SL-2 |
   | L3 | Supervisory | SCADA 監控 | SCADA Server, HMI, Historian, NTP | SL-2~3 |
   | L2 | Station Bus | PRP 通訊骨幹 | PRP Switch LAN-A/B, Bay Switch | SL-2 |
   | L1 | Bay Level | 現場控制 | RTU, Gateway, IED 通訊介面 | SL-2 |
   | L0 | Process | 現場設備 | Protection Relay, Inverter, Meter | SL-1~2 |
   ```
   詳細參考架構見 `references/substation_zone_conduit.md`。

   **⚠️ PRP 成本預警**：當概念架構含 PRP 雙骨幹時，自動標註以下警告：
   > ⚠️ PRP 架構將使網路交換機數量增加 2-3 倍（F6 實績：15→27 台，+80%）。
   > 概念階段即應預留 PRP 三倍化的成本空間，避免 CBOM 低估。
   > 詳見 cbom-builder/references/epci_substation_patterns.md §3。

2. **定義 Conduit**：Zone 間通訊路徑（協定、頻寬、延遲、可靠性）

3. **初步安全控制配置**：每個 Zone 的概念級安全控制

4. **標註非約束性**：所有圖面和文件必須標示 `CONCEPT — NON-BINDING — ADVISORY`

5. **產出概念架構圖**：可使用 arch-diagram Skill 的 D2/Mermaid 規範

**多站點概念架構**（當 EPCI 含多個站點時）：
- 每站點獨立繪製 Zone/Conduit，標示站間通訊 Conduit
- 站間光纖 trunk 和備援（如 4G/microwave）為獨立 Conduit
- 每站點可有不同 SL-T（如 ONS = SL-3、OnSWST = SL-2）
- 共用設備（如集中 SIEM）標示為跨站共用 Zone

**⚠️ 避坑**：
- 概念架構**不是**詳細設計——不需要 IP 規劃或完整防火牆規則
- 必須標示 non-binding——否則客戶可能視為合約承諾
- 至少要有 3 個 Zone——少於 3 個表示分析不夠深入
- **PRP 概念架構必須明確標示 LAN-A/B 雙骨幹**——影響設備數量估算

---

### Step 2: 初步安全分類 (SK-D14-014)

**目標**：建立初步 SL-T 提案和專案安全風險分類。

**操作步驟**：

1. **專案安全風險分類**：High / Medium / Low

| 分類 | 判定標準 | 範圍影響 |
|------|---------|---------|
| High | 涉及 safety system、關鍵基礎設施 | 需更多安全投入、SL-3+ Zone |
| Medium | 標準 OT/ICS 系統 | 標準安全措施 |
| Low | 非關鍵 IT/OT 系統 | 基本安全措施 |

2. **Per-Zone SL-T 提案**：
   ```markdown
   | Zone | 概念 SL-T | 理由 | 信心等級 |
   |------|----------|------|---------|
   | Enterprise IT | SL-1 | 一般辦公 | High |
   | OT Control | SL-2 | 標準 SCADA | High |
   | SIS | SL-3 | Safety function | Medium |
   ```

3. **範圍影響評估**：SL-T 對工時/成本/時程的影響量化

4. **不確定性評估**：信心等級、關鍵假設、變動因素

5. **Security Ambition Summary**：一頁摘要給 Gate 0 決策者

**⚠️ 避坑**：
- 初步分類是 indicative，不是 final——R1 會正式評估
- 不要所有 Zone 都給 SL-3——會導致成本爆炸
- 信心等級要誠實——Presales 階段的資訊通常不完整

---

### Step 3: Pre-Gate 0 需求釐清與可行性輸入 (SK-D14-018)

**目標**：確保概念架構和安全分類可作為 Gate 0 輸入。

**操作步驟**：
1. 驗證概念架構與客戶需求的對齊
2. 整合到可行性評估 (SK-D14-003) 的技術可行性面向
3. 標註所有假設和依賴
4. 準備 Gate 0 概念架構簡報

---

## 2. 輸出

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Concept Zone/Conduit Architecture Diagram | D2/Mermaid |
| 2 | Zone-Requirement Mapping | Markdown |
| 3 | Preliminary Security Control Allocation | Markdown |
| 4 | Conduit Specifications | Markdown |
| 5 | Preliminary Security Classification Report | Markdown |
| 6 | Per-Zone SL-T Proposal | Markdown |
| 7 | Scope Impact Assessment | Markdown |
| 8 | Security Ambition Summary (1-page) | Markdown |

---

## 3. 驗收標準

| # | 項目 | 條件 |
|---|------|------|
| 1 | ≥3 security zones 已辨識 | ✓ |
| 2 | Zone-Requirement mapping 已建立 | ✓ |
| 3 | Conduit 有 protocol/bandwidth/latency | ✓ |
| 4 | NON-BINDING 標示已加註 | ✓ |
| 5 | 專案安全分類 (H/M/L) 已指定+理由 | ✓ |
| 6 | Per-zone SL-T 有信心等級 | ✓ |
| 7 | 範圍影響已量化 (工時/成本) | ✓ |

---

## 4. 工時

| 步驟 | Junior | Senior |
|------|--------|--------|
| 概念架構 | 5-8 pd | 3-5 pd |
| 安全分類 | 3-5 pd | 2-3 pd |
| Gate 0 輸入 | 1-2 pd | 1 pd |

---

## 5. 人類審核閘門

```
概念設計完成。Zones：{n}個 | SL-T：{分布} | 安全分類：{H/M/L}
⚠️ 所有產出為 ADVISORY / NON-BINDING
👉 請 PGS + SAC 審核後提交 Gate 0。
```

---

## 6. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D14-013 | Concept Zone/Conduit Architecture | 概念分區、Conduit 規格、non-binding |
| SK-D14-014 | Preliminary Security Classification | SL-T 提案、安全風險分類、範圍影響 |
| SK-D14-018 | Pre-Gate 0 Requirement Clarification | 需求對齊、Gate 0 可行性輸入 |

<!-- Phase 6: Enhanced 2026-03-19. -->
<!-- F6 Optimization: IEC 61850 Z/C patterns, PRP cost warning, multi-site concept -->
