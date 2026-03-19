---
name: edge-computing-architecture
description: >
  Design edge computing deployment, author ADRs, evaluate technologies, and facilitate
  architecture reviews for OT/ICS edge-to-cloud solutions.
  MANDATORY TRIGGERS: 邊緣計算, edge computing, ADR, 架構決策, architecture decision record,
  技術選型, technology selection, 架構審查, architecture review, edge node, edge deployment,
  edge-to-cloud, 離線韌性, offline resilience.
  Use this skill for edge node placement, ADR authoring, tech evaluation, and architecture review.
---

# 邊緣計算架構 (Edge Computing Architecture)

整合 4 個 SK，涵蓋邊緣部署、ADR、技術選型與架構審查。

---

## 0. 初始化

1. 網路架構已完成 (含 Zone/Conduit)
2. 系統可用性需求已取得 (RTO/RPO)
3. 現場環境條件已調查 (溫度、空間、電力)

---

## 1. 工作流程

### Step 1: 邊緣部署設計 (SK-D02-008)

| 考量 | 內容 | 典型值 |
|------|------|--------|
| 節點位置 | 變電站/配電室/機房 | 靠近數據源 |
| 運算需求 | CPU/RAM/Storage | 4C/16GB/256GB SSD |
| 離線韌性 | 本地 buffer 時間 | 72 hr store-and-forward |
| Edge-Cloud 同步 | 協定/頻率 | MQTT/5min batch |

**步驟**：識別 edge workload → 選定 edge hardware → 設計 edge-cloud 通訊 (MQTT/AMQP) → 定義離線策略 (local buffer + sync) → 部署拓撲圖

**⚠️ 避坑**：edge 節點需 UPS 保護；離線 buffer 滿時的 data retention policy 要預先定義

### Step 2: ADR 撰寫 (SK-D02-009)

```markdown
# ADR-{nnn}: {決策標題}

## Status: Proposed | Accepted | Deprecated | Superseded
## Context: 為什麼需要這個決策？背景與限制。
## Decision: 我們決定 {方案}。
## Alternatives:
  - 方案 B: {描述} — 排除原因
  - 方案 C: {描述} — 排除原因
## Consequences:
  - 正面: {benefits}
  - 負面: {trade-offs}
```

**⚠️ 避坑**：ADR 必須記錄被排除方案；status 需隨專案更新

### Step 3: 技術選型 (SK-D02-010)

| 評估維度 | 權重 | 候選 A | 候選 B | 候選 C |
|----------|------|--------|--------|--------|
| OT 相容性 | 20% | — | — | — |
| 安全認證 | 15% | — | — | — |
| TCO (5yr) | 15% | — | — | — |
| 供應商支援 | 10% | — | — | — |
| 社群/生態 | 10% | — | — | — |

**要求**：至少 15 項評估準則、3+ 候選方案、5 年 TCO 估算

**⚠️ 避坑**：避免只看初始成本；OT 環境需考慮長期供應商支援 (10+ 年)

### Step 4: 架構審查 (SK-D02-012)

**審查清單**：功能完整性 → 非功能需求 (效能/可用/安全) → 相依風險 → 部署可行性 → 維運複雜度

**產出**：審查報告 (findings + severity + recommendations)

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | Edge 部署拓撲圖含所有節點 |
| 2 | 離線韌性策略已定義 (buffer + sync) |
| 3 | 每個重大決策有 ADR |
| 4 | 技術選型含 3+ 候選、15+ 準則 |
| 5 | 5 年 TCO 估算完成 |
| 6 | 架構審查報告已產出 |

---

## 3. 人類審核閘門

```
邊緣架構完成。節點數：{n} | ADR：{count} 份 | 技術選型：{選定方案}
👉 請 SA + SYS 審核。
```

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D02-008 | Edge Deployment | 節點配置、離線韌性、edge-cloud 通訊 |
| SK-D02-009 | ADR Writing | 決策文件結構、status 管理 |
| SK-D02-010 | Technology Selection | 多維評估、TCO、候選比較 |
| SK-D02-012 | Architecture Review | 審查流程、findings 報告 |

<!-- Phase 6: Enhanced 2026-03-19. -->
