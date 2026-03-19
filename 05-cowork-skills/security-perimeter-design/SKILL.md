---
name: security-perimeter-design
description: >
  Design and document security perimeters for OT/ICS environments including detailed firewall
  rule planning and comprehensive network segmentation documentation for IEC 62443 compliance.
  MANDATORY TRIGGERS: 防火牆規則, firewall rules, ACL, 網路分段, network segmentation,
  安全邊界, security perimeter, 防火牆規劃, firewall planning, 分段文件,
  segmentation documentation, zone boundary, conduit enforcement,
  防火牆設計, firewall design, 存取控制清單.
  Use this skill for firewall rule design and network segmentation documentation in OT/ICS projects.
---

# 安全邊界設計 (Security Perimeter Design)

本 Skill 整合 2 個工程技能定義，將 Zone/Conduit 架構轉換為具體防火牆規則和完整的網路分段文件包。適用於 R2 (詳細設計) 到 R3 (實施驗證)。

---

## 0. 初始化

1. **Zone/Conduit 架構**：已完成 (SK-D01-001)，含 Conduit Spec Table
2. **資產清冊**：已完成 (SK-D01-005)，含 IP/MAC/Zone 對照
3. **SL-T 評估**：已完成 (SK-D01-010)
4. **資料流圖**：已完成 (SK-D02-004)

---

## 1. 輸入

| 類別 | 輸入項目 | 來源 |
|------|---------|------|
| 架構 | Zone/Conduit 架構圖 + Conduit Spec Table | SK-D01-001 |
| 資產 | 資產清冊 (IP, MAC, Zone) | SK-D01-005 |
| 架構 | 資料流圖 (DFD) | SK-D02-004 |
| 風險 | SL-T 指定表 | SK-D01-010 |
| 網路 | 實體網路拓撲 | SK-D02-001 |
| 標準 | FR/SR 對照表 | Plugin 共用 references/ |

---

## 2. 工作流程

### Step 1: 防火牆規則規劃 (SK-D01-003)

**目標**：將 Conduit Spec Table 轉換為詳細防火牆規則。

**操作步驟**：

1. **逐 Conduit 展開規則**：每條 Conduit 產生 ≥1 firewall rule

   ```markdown
   | Rule ID | 方向 | Source Zone/IP | Dest Zone/IP | Protocol | Port | Action | Logging | 理由 | Conduit Ref |
   |---------|------|---------------|-------------|----------|------|--------|---------|------|------------|
   | FW-001 | → | DMZ/10.0.0.1 | SRV/10.20.0.5 | TCP | 443 | ALLOW | Yes | SCADA Web UI | C2 |
   | FW-002 | → | OT/10.30.0.0/24 | SRV/10.20.0.10 | TCP | 514 | ALLOW | Yes | Syslog | C3 |
   | FW-003 | ← | SRV/10.20.0.5 | DMZ/10.0.0.1 | TCP | 443 | ALLOW | Yes | Response | C2 |
   | FW-999 | * | Any | Any | Any | Any | DENY | Yes | Default deny | — |
   ```

2. **規則排序**：具體→通用，default deny 在最後

3. **雙向處理**：每條 Conduit 的 request + response 方向

4. **Broadcast/Multicast**：明確處理（allow/deny + 安全理由）

5. **Denial/Exception Log**：被拒絕的合理流量記錄例外

**⚠️ 避坑**：
- 不要用 `Any` 做 source/destination——每條規則要具體
- 別忘記 return traffic 規則——stateful FW 可省略，stateless 需明確
- 規則衝突檢查：不應有兩條規則對同一流量給出不同 action

---

### Step 2: 網路分段文件 (SK-D01-004)

**目標**：編譯所有分段實施文件為 IEC 62443 合規的驗證包。

**操作步驟**：

1. **Network Segmentation FDS**：撰寫功能設計規格
   - Zone 定義敘述 (含 SL-T 理由)
   - Conduit 政策敘述
   - 防火牆策略
   - VLAN/ACL 架構

2. **Design Verification Package** (per ID02 Annex C.3)：
   ```markdown
   | Evidence ID | 驗證項目 | 證據類型 | 文件位置 | 狀態 |
   |------------|---------|---------|---------|------|
   | DV-001 | Zone 邊界防火牆規則 | 設計文件 | FW Rule Table §2.1 | ✅ |
   | DV-002 | VLAN 隔離設定 | 設備 Config | Switch-01 running-config | ✅ |
   | DV-003 | ACL 實施 | 設備 Config | Router-01 ACL dump | ✅ |
   ```

3. **Master Device Config Reference Table**：設備→VLAN→規則→Firmware

4. **變更管理程序**：分段架構的變更如何管控 (GOV-SD Gate 2)

5. **Operational Handover Package**：給營運團隊的簡化版

**⚠️ 避坑**：
- 驗證包不是只列文件——需有 evidence mapping 到具體設備 config
- 變更管理必須涵蓋 emergency change path
- GOV-SD Gate 2 是 R3 prerequisite——分段文件需在 Gate 2 前完成

---

## 3. 輸出 / 交付物

| # | 交付物 | 步驟 |
|---|--------|------|
| 1 | Firewall Rule Specification Table | 1 |
| 2 | Rule Priority/Order Documentation | 1 |
| 3 | Denial/Exception Log | 1 |
| 4 | Rule Testing Plan | 1 |
| 5 | Network Segmentation FDS | 2 |
| 6 | Design Verification Package | 2 |
| 7 | Zone/Conduit Diagram with VLAN overlay | 2 |
| 8 | Master Device Config Reference Table | 2 |
| 9 | Change Management Procedure | 2 |
| 10 | Operational Handover Package | 2 |

---

## 4. 適用標準

| 標準 | 用途 |
|------|------|
| IEC 62443-3-2 | Zone-based risk assessment |
| IEC 62443-3-3 FR5 (RDF) | 受限資料流 |
| ID01 §7.4.1.2 | 網路分段要求 |
| ID02 Annex A.9 §10.1 | 安全實施規格 |
| ID02 Annex C.3 | 設計驗證 |
| NIST SP 800-82 Rev. 3 | OT 安全 |
| GOV-SD | Gate 2 prerequisite |

---

## 5. 驗收標準

| # | 項目 | 條件 |
|---|------|------|
| 1 | 規則覆蓋 | Conduit Spec Table 每條 → ≥1 firewall rule |
| 2 | 規則完整 | 每條規則含 source/dest/protocol/port/action/logging/理由 |
| 3 | 無衝突 | 規則衝突已辨識並解決 |
| 4 | Default deny | 每個方向末端有 catch-all deny |
| 5 | 雙向追溯 | 防火牆規則↔Zone/Conduit 架構可雙向追溯 |
| 6 | 驗證包 | Design Verification Evidence Matrix 完整 |
| 7 | 設備 Config | Master Device Config Table 涵蓋所有分段設備 |

---

## 6. 工時參考

| 步驟 | Junior | Senior | 備註 |
|------|--------|--------|------|
| Step 1 FW 規則 | 6-10 pd | 3-5 pd | ~50 devices |
| Step 2 分段文件 | 10-16 pd | 5-8 pd | 含驗證包 |

---

## 7. 人類審核閘門

```
安全邊界設計已完成。
📋 範圍：防火牆規則規劃 + 網路分段文件
📊 數據：FW Rules {n} 條 | Conduits {c} 條 | VLANs {v} 個 | 驗證項 {dv} 個
⚠️ 待確認：{規則衝突/例外/待確認 IP}
👉 請 SAC + SYS 審核 PASS / FAIL / PASS with Conditions。
```

---

## 8. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D01-003 | Firewall Rule Planning | Conduit→FW rule 轉換、規則排序、default deny |
| SK-D01-004 | Network Segmentation Documentation | FDS、驗證包、VLAN overlay、變更管理 |

<!-- Phase 6: Deep enhancement from 2 SK definitions. Enhanced 2026-03-19. -->
