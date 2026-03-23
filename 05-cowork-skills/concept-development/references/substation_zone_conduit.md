# 變電所標準 Zone/Conduit 參考架構

> 適用於 IEC 61850 / PRP 架構的變電所 OT 系統概念設計

---

## 1. 標準 Zone 分層（Purdue Model）

```
L4 Enterprise  ─── ERP, ADCC, Remote Access WS
       │
   [Firewall]  ─── DMZ (L3.5)
       │
L3 Supervisory ─── SCADA Server, HMI, Historian, Eng WS, NTP
       │
   [PRP LAN-A / LAN-B]  ─── L2 Station Bus
       │
L1 Bay Level   ─── RTU, Gateway, IED Comm Interface
       │
L0 Process     ─── Protection Relay, Inverter, Meter, Sensor
```

---

## 2. Zone 定義表

| Zone ID | Zone 名稱 | Purdue | SL-T | 典型設備 | VLAN |
|---------|----------|--------|------|---------|------|
| Z-ENT | Enterprise | L4 | SL-1 | ERP Server, ADCC WS, Remote WS | VLAN 100 |
| Z-DMZ | DMZ | L3.5 | SL-2 | Edge Firewall, Jump Server, VPN Gateway | VLAN 999 |
| Z-SUP | Supervisory | L3 | SL-2~3 | SCADA Server, HMI ×n, Historian, Eng WS, NTP | VLAN 30 |
| Z-STB | Station Bus | L2 | SL-2 | PRP Switch LAN-A ×n, PRP Switch LAN-B ×n | VLAN 20 |
| Z-BAY | Bay Level | L1 | SL-2 | RTU, Protocol Gateway, Bay Switch, RedBox | VLAN 10 |
| Z-PRO | Process | L0 | SL-1~2 | Protection Relay, Inverter, Power Meter | — |

---

## 3. Conduit 定義表

| Conduit ID | 來源 Zone | 目標 Zone | 協定 | 安全措施 | 方向 |
|-----------|----------|----------|------|---------|------|
| CD-01 | Z-ENT | Z-DMZ | HTTPS, SSH | Firewall ACL, NAT | 雙向 |
| CD-02 | Z-DMZ | Z-SUP | OPC-UA, ICCP | Firewall DPI, Data Diode (選配) | 主要北向 |
| CD-03 | Z-SUP | Z-STB | IEC 61850 MMS | PRP 冗餘, VLAN ACL | 雙向 |
| CD-04 | Z-STB | Z-BAY | IEC 61850 GOOSE, Modbus TCP | PRP 冗餘, Port Security | 雙向 |
| CD-05 | Z-BAY | Z-PRO | IEC 61850 GOOSE (Fiber), RS-485 | 實體隔離, 光纖 | 主要北向 |
| CD-06 | Z-SUP | Z-SUP (NTP) | IEEE 1588 PTP, NTP | 時間同步專用 VLAN | 單向 |

---

## 4. PRP 雙骨幹拓撲

### 4.1 架構概念

```
SCADA ──┬── LAN-A (Primary) ──┬── Bay SW-A1 ── RTU/GW
        │                      ├── Bay SW-A2 ── RTU/GW
        │                      └── Bay SW-An ── RTU/GW
        │
        └── LAN-B (Backup)  ──┬── Bay SW-B1 ── RTU/GW
                               ├── Bay SW-B2 ── RTU/GW
                               └── Bay SW-Bn ── RTU/GW
```

### 4.2 設備→Zone 映射

| 設備類別 | 單站數量 (6 饋線) | PRP 影響 | Zone |
|---------|-----------------|---------|------|
| Station Switch (L2) | 4 (2×LAN-A + 2×LAN-B) | ×2 | Z-STB |
| Bay Switch | 24 (6 Bay × 2 × 2 LAN) | ×4 | Z-BAY |
| RedBox | 依非 PRP 設備數 | 新增 | Z-BAY |
| SCADA Server | 2 (主/備) | 不變 | Z-SUP |
| HMI | 2-4 | 不變 | Z-SUP |
| Historian | 1 | 不變 | Z-SUP |
| Firewall | 2 (HA pair) | 不變 | Z-DMZ |

### 4.3 成本影響估算

| 項目 | 無 PRP | 有 PRP | 倍率 |
|------|--------|--------|------|
| L2 交換機 | 2 | 4 | ×2 |
| Bay 交換機 | 6 | 24 | ×4 |
| RedBox | 0 | 10-20 | 新增 |
| 光纖 | 基礎 | ×2 | ×2 |
| **總網路設備** | ~8 | ~48+ | **×3~6** |

---

## 5. 多站點設計原則

| 原則 | 說明 |
|------|------|
| 獨立 Zone 體系 | 每站點有獨立的 Z-SUP/Z-STB/Z-BAY/Z-PRO |
| 共用 Enterprise | L4 Enterprise Zone 可跨站共用（透過 WAN） |
| 站間 Conduit | 專用光纖 trunk + 4G/microwave 備援 |
| 獨立防火牆 | 每站點獨立 Edge Firewall，不共用 |
| SL-T 可不同 | 主站（ONS）可能 SL-3，輔站（OnSWST）可能 SL-2 |

---

## 6. IEC 62439-3 PRP 對資安的影響

| 面向 | 影響 | 概念設計考量 |
|------|------|------------|
| 攻擊面增加 | 雙網路 = 雙倍攻擊面 | 兩條 LAN 皆需安全監控 |
| 韌體管理 | 交換機數量 ×3 = 韌體更新工作量 ×3 | 納入維護工時估算 |
| 網路監控 | 需監控兩條獨立骨幹 | SIEM/IDS 需雙倍流量處理 |
| 失效模式 | LAN-A 失效時 LAN-B 接管，但安全策略需同步 | Firewall rule 同步機制 |
