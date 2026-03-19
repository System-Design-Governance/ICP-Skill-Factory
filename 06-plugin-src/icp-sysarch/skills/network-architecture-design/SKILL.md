---
name: network-architecture-design
description: >
  Design OT/ICS network architecture covering network redundancy (RSTP/ring/dual-homing),
  high-availability architecture (hot/warm/cold standby), and RTO/RPO planning.
  MANDATORY TRIGGERS: 網路架構, network architecture, 冗餘設計, redundancy design,
  高可用, high availability, HA, RTO, RPO, 備援, failover, 網路冗餘,
  network redundancy, RSTP, ring topology, dual-homing, 復原時間, recovery time.
  Use this skill for OT network redundancy, HA architecture, and RTO/RPO planning.
---

# OT 網路架構設計 (Network Architecture Design)

整合 3 個 SK，設計 OT/ICS 網路的冗餘、高可用和復原架構。

---

## 0. 初始化

1. Zone/Conduit 架構已完成 (SK-D01-001)
2. 資產清冊已完成 (SK-D01-005)
3. 客戶 RTO/RPO 需求已取得

---

## 1. 工作流程

### Step 1: 網路冗餘設計 (SK-D02-002)

| 機制 | 切換時間 | 適用場景 | 注意 |
|------|---------|---------|------|
| RSTP | 1-30s | 中型乙太網路 | 確認 VLAN 隔離 |
| Ring (MRP/HSR/PRP) | <50ms/0ms | 高可用工控 | 最佳 OT 方案 |
| Dual-Homing | <1s | Server 冗餘 | 需防 loop |
| LACP | Active-active | 高頻寬 | 注意 STP 互動 |

**步驟**：辨識 SPOF → 選冗餘機制 → 設計拓撲 (含 link cost) → 定義 failover timing → 驗證不跨 Zone boundary

**⚠️ 避坑**：冗餘路徑不可跨 security zone；RSTP 對某些 OT 太慢；Ring 需全設備支援

### Step 2: 高可用架構 (SK-D02-006)

| 配置 | RTO | 成本 | 適用 |
|------|-----|------|------|
| Hot Standby | <1 min | 高 | SCADA, Historian |
| Warm Standby | 1-30 min | 中 | App Server |
| Cold Standby | >30 min | 低 | 非關鍵 |

**重點**：Server 冗餘 (Active/Passive) → DB replication (同步/非同步) → Auto-failover 觸發 → Zone 安全整合

**⚠️ 避坑**：HA failover 不可繞過 security zone；DB replication lag 影響 RPO

### Step 3: RTO/RPO 規劃 (SK-D02-007)

```markdown
| 系統 | Criticality | RTO | RPO | 備份策略 |
|------|------------|-----|-----|---------|
| SCADA | Critical | 5 min | 0 (同步) | Hot standby |
| Historian | High | 30 min | 5 min | Warm + DB repl |
| HMI | High | 15 min | 30 min | VM snapshot |
| File Server | Medium | 4 hr | 24 hr | Daily backup |
```

**步驟**：定義 per-system RTO/RPO → 備份策略選擇 → Storage 需求 → Recovery procedure → 驗證測試 → Backup security classification

**⚠️ 避坑**：RTO/RPO 必須客戶確認；backup repository 需與 source 同等 SL 保護

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | SPOF 已消除或文件化例外 |
| 2 | 冗餘路徑不跨 Zone boundary |
| 3 | Failover 符合 RTO |
| 4 | HA failover 已測試驗證 |
| 5 | 每系統有 RTO/RPO + 客戶確認 |
| 6 | Recovery 每 tier 至少測試一次 |

---

## 3. 人類審核閘門

```
網路架構完成。冗餘：{type} | HA：{n} 系統 | RTO 最嚴：{min}
👉 請 SYS + SAC 審核。
```

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D02-002 | Network Redundancy | RSTP/Ring/Dual-homing、failover |
| SK-D02-006 | HA Architecture | Hot/Warm/Cold、DB replication |
| SK-D02-007 | RTO/RPO Planning | Target matrix、backup、recovery |

<!-- Phase 6: Enhanced 2026-03-19. -->
