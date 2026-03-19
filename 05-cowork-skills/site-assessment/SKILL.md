---
name: site-assessment
description: >
  Conduct comprehensive site assessment for OT/ICS cybersecurity projects covering physical
  site survey, constraint documentation, existing infrastructure inventory, and NDA management.
  MANDATORY TRIGGERS: 現場勘查, site survey, 場勘, site assessment, 現場評估,
  基礎設施盤點, infrastructure inventory, 限制條件, constraint documentation,
  brownfield assessment, 既有設備, existing equipment, 場域調查,
  site visit, physical assessment, 現況調查.
  Use this skill for site surveys, infrastructure discovery, and constraint documentation
  in pre-gate OT/ICS projects.
---

# 現場評估與基礎設施盤點 (Site Assessment & Infrastructure Inventory)

本 Skill 整合 3 個工程技能定義，提供 Pre-Gate 0 / Presales 的完整現場評估流程。

---

## 0. 初始化

1. **專案範圍**：SOW/RFP 已取得
2. **場勘排程**：已安排現場訪問
3. **NDA**：已確認是否需要保密協議
4. **工具**：相機、量測工具、筆電、網路掃描工具 (如授權)

---

## 1. 工作流程

### Step 1: 現場勘查 (SK-D14-011)

**6 大評估面向**：

| 面向 | 評估項目 | 記錄方式 |
|------|---------|---------|
| 實體環境 | 建物結構、空間、通道、承重 | 照片+測量 |
| 環境條件 | 溫度、濕度、灰塵、振動、EMI | 量測值 |
| 電力 | 電源容量、接地、UPS、配電盤 | 量測+照片 |
| 網路 | 佈線、機櫃、光纖、ISP | 照片+拓撲 |
| 實體安全 | 門禁、CCTV、圍欄、照明 | 照片+清單 |
| HSE | 危險區域、PPE、緊急出口 | 照片+標示 |

**Constraint Register**：
```markdown
| ID | 類別 | 描述 | 嚴重度 | 影響設計 | 緩解方式 |
|----|------|------|--------|---------|---------|
| C-001 | 電力 | 機房剩餘僅 2kW | Hard | 設備選型 | 增迴路/低功耗設備 |
| C-002 | 環境 | 35-42°C 無空調 | Hard | 耐溫規格 | 工業級設備+散熱 |
| C-003 | 網路 | 僅 Cat5e | Soft | 頻寬 | 評估 Cat6 升級 |
```

- **Hard**：必須解決，否則方案不可行
- **Soft**：有替代方案

**⚠️ 避坑**：環境需實測 (夏冬差異大)；Hard constraint 需照片；未文件化設備需實體場勘

---

### Step 2: 既有基礎設施清冊 (SK-D14-012)

**6 大盤點類別**：自動化、網路、伺服器、通訊、安全、實體設施

```markdown
| Item ID | 類別 | 名稱 | 廠牌 | 型號 | FW | 位置 | 狀態 | EOL |
|---------|------|------|------|------|-----|------|------|-----|
| INV-001 | 網路 | Core Switch | Cisco | 2960X | 15.2 | 機房 | Active | 2027 |
| INV-002 | 自動化 | PLC | Siemens | S7-300 | v5.6 | 現場 | Active | 2025⚠️ |
```

**產出**：EOL Risk Register + Gap Summary + Integration Impact Assessment

**⚠️ 避坑**：被動掃描需 PtW；legacy 設備需人工讀銘牌；別漏非網路化設備

---

### Step 3: NDA 管理 (SK-D14-017)

NDA 需求評估→文件準備 (ID25 模板)→簽署追蹤→團隊保密告知

---

## 2. 輸出

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Site Survey Report (6 面向) | Markdown+照片 |
| 2 | Constraint Register | Markdown |
| 3 | Infrastructure Inventory | Markdown/Excel |
| 4 | EOL Risk Register | Markdown |
| 5 | Gap Summary | Markdown |
| 6 | NDA Tracking Register | Markdown |

---

## 3. 驗收標準

| # | 項目 | 條件 |
|---|------|------|
| 1 | 場勘 6 面向全覆蓋 | ✓ |
| 2 | ≥10 限制條件，Hard 有照片 | ✓ |
| 3 | 環境數據為實測值 | ✓ |
| 4 | 6 類基礎設施全盤點 | ✓ |
| 5 | EOL 設備已標記+風險記錄 | ✓ |
| 6 | 清冊格式與 SK-D01-005 相容 | ✓ |

---

## 4. 工時

| 步驟 | Junior | Senior |
|------|--------|--------|
| 場勘 | 3-5 pd | 2-3 pd |
| 清冊 | 3-5 pd | 2-3 pd |
| NDA | 1-2 pd | 0.5-1 pd |

---

## 5. 人類審核閘門

```
現場評估完成。場域：{name} | 限制：{n}項 (Hard:{h}) | 設備：{inv}項 | EOL：{eol}項
👉 請 PGS 審核。
```

---

## 6. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D14-011 | Site Survey | 6 面向場勘、Constraint Register |
| SK-D14-012 | Infrastructure Inventory | 6 類盤點、EOL、Gap Summary |
| SK-D14-017 | NDA Management | 保密協議追蹤 |

<!-- Phase 6: Enhanced 2026-03-19. -->
