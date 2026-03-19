---
name: security-monitoring-incident-response
description: >
  Execute comprehensive security monitoring and incident response for OT/ICS environments.
  Covers SIEM configuration and tuning, security alarm rule design, incident response procedure
  development, security incident investigation and forensics, continuous security monitoring,
  and threat intelligence collection and analysis.
  MANDATORY TRIGGERS: 安全監控, security monitoring, SIEM, 事件回應, incident response,
  告警規則, alarm rules, correlation rules, 事件調查, incident investigation,
  數位鑑識, digital forensics, 持續監控, continuous monitoring, 威脅情資,
  threat intelligence, SOC, 安全事件, security event, 日誌分析, log analysis,
  IDS, anomaly detection, 異常偵測.
  Use this skill for security monitoring, SIEM, incident response, forensics, and threat
  intelligence tasks in OT/ICS/SCADA cybersecurity projects.
---

# 安全監控與事件回應 (Security Monitoring & Incident Response)

本 Skill 整合 6 個工程技能定義，提供 OT/ICS 環境安全監控與事件回應的完整工作流程——從 SIEM 建置到威脅情資持續運營。適用於 IEC 62443 生命週期 R3–R4。

---

## 0. 初始化

執行前確認：

1. **Zone/Conduit 架構**：已完成 (SK-D01-001)，SL-T 已指定
2. **資產清冊**：已完成 (SK-D01-005)，含所有 log source 設備
3. **風險評估**：DTRA (SK-D01-007) 產出可用——驅動監控優先級
4. **加固完成**：端點加固 (SK-D01-019) 已啟用 logging
5. **SIEM 平台**：已選定並部署 (Splunk/Graylog/QRadar/等)

---

## 1. 輸入

| 類別 | 輸入項目 | 來源 |
|------|---------|------|
| 架構 | Zone/Conduit 圖 + SL-T | SK-D01-001 |
| 資產 | 資產清冊 (log source 對照) | SK-D01-005 |
| 風險 | DTRA 風險登錄冊 | SK-D01-007 |
| 威脅 | STRIDE Threat Catalog | SK-D01-008 |
| 組態 | 加固後設備 logging 設定 | SK-D01-019 |
| 政策 | 安全政策與程序計畫 | SK-D01-030 |
| 標準 | FR/SR 對照表 | Plugin 共用 references/ |

---

## 2. 工作流程

### Step 1: SIEM 配置與調校 (SK-D01-014)

**目標**：設定 SIEM 系統，整合所有 log source，建立基線。

**操作步驟**：

1. **Log Source 盤點與整合**：
   ```markdown
   | Log Source | 類型 | 協定 | 頻率 | Zone | 優先級 |
   |-----------|------|------|------|------|--------|
   | Edge Firewall | FW | Syslog/TLS | Real-time | DMZ | High |
   | Windows AD | Auth | WEF/WinRM | Real-time | Server | High |
   | SCADA HMI | App | Syslog | 5-min | OT | Critical |
   | ICS PLC | Device | OPC UA audit | Event-driven | OT | Critical |
   | Switch/WAP | Network | SNMP/Syslog | Real-time | All | Medium |
   ```

2. **SIEM 基線配置**：
   - Log parsing rules (per OT protocol: Modbus, DNP3, IEC 61850, OPC UA)
   - Log normalization and field mapping
   - Storage and retention policy (最少 1 年 per IEC 62443-2-1 §7.8.4.2)
   - Dashboard 建立：事件趨勢、告警分布、false positive 追蹤

3. **初始調校**：收集 2-4 週基線數據後調整閾值

**⚠️ 避坑**：OT 協定 (Modbus/DNP3) 缺少 native logging——需 network tap + protocol-aware parser；不要將 IT SIEM rules 直接套用到 OT

---

### Step 2: 安全告警規則設計 (SK-D01-015)

**目標**：設計偵測 OT/ICS 威脅的告警規則與關聯邏輯。

**操作步驟**：

1. **告警分類框架** (5 類)：

| 類別 | 範例場景 | 嚴重度 |
|------|---------|--------|
| Authentication | 暴力登入、異常時段登入、預設帳號使用 | High |
| Network | 未授權跨 Zone 流量、新設備出現、協定異常 | Critical |
| Configuration | 組態變更、firmware 更新、服務啟停 | High |
| Malware | AV 告警、異常 process、C2 通訊 | Critical |
| Operational | 效能異常、資源耗盡、通訊中斷 | Medium |

2. **關聯規則設計**：
   - 單一事件規則 (threshold-based)
   - 多事件關聯 (sequence-based)
   - 異常偵測 (baseline deviation)

3. **與 SK-D05-006 整合**：安全告警層級需與 OT alarm hierarchy 對齊——避免 alarm flooding

**⚠️ 避坑**：規則太嚴會造成 alert fatigue (false positive flood)；規則太鬆會漏掉真正威脅——需持續 tuning

---

### Step 3: 事件回應程序 (SK-D01-016)

**目標**：建立端到端事件回應程序。

**事件嚴重度分類** (4 級 per ID24)：

| Level | 標準 | RTO 目標 |
|-------|------|---------|
| L1 | 低影響，單一系統 | 72 hr |
| L2 | 中影響，局部功能 | 72 hr |
| L3 | 高影響，多系統 | 36 hr |
| L4 | 關鍵影響，全面中斷 | 36 hr 或依合約 |

**事件回應流程**：
```
偵測 → 分類 (L1-L4) → 通報 → 圍堵 → 調查 → 根因分析 → 修復 → 復原 → 事後檢討
```

**損害控制任務** (A-G per ID24)：
- A: 停止未授權存取
- B: 隔離受影響系統
- C: 保全證據
- D: 通知利害關係人
- E: 啟動備份復原
- F: 修復弱點
- G: 驗證系統完整性

**事後改善**：1 個月內完成改善措施 (per ID24 §5.7.8)

**⚠️ 避坑**：OT 環境的圍堵不能隨意斷網——可能影響 safety system；需 safety engineer 確認

---

### Step 4: 安全事件調查與鑑識 (SK-D01-017)

**目標**：使用數位鑑識方法調查 OT/ICS 安全事件。

**六階段方法論**：

1. **調查授權**：取得正式授權、定義範圍
2. **Volatile Data 保全**：記憶體、執行中 process、網路連線
   ```bash
   # Linux volatile data collection
   date > /tmp/forensics/timestamp.txt
   ps auxww > /tmp/forensics/processes.txt
   netstat -anp > /tmp/forensics/netstat.txt
   cat /proc/meminfo > /tmp/forensics/meminfo.txt
   ```
3. **系統穩定 + Non-Volatile 取得**：磁碟映像、日誌備份
4. **證據分析 + 時間線重建**：Master Timeline 建構
5. **根因判定**：攻擊向量、影響範圍
6. **調查報告 + 證據歸檔**：Chain of Custody 維護

**⚠️ 避坑**：OT 設備的 volatile data 取得需考慮 real-time 控制影響；不要在 live PLC 上執行深度鑑識

---

### Step 5: 持續安全監控 (SK-D01-018)

**目標**：建立並運營 R4 階段的持續安全監控。

**六階段運營模式**：
1. 監控基礎設施部署與設定
2. 基線建立與異常偵測規則開發
3. 告警產生與初始分類 (Triage)
4. 事件關聯與模式分析
5. 威脅情資整合與規則精煉
6. 營運報告與持續改善

**關鍵報告週期**：
- **月報**：安全事件趨勢、告警分布、false positive rate
- **季報**：威脅情資更新、控制效能、改善建議
- **年報**：監控效能總評、SL-A 驗證

**⚠️ 避坑**：監控不是 set-and-forget——需持續 tuning 和 rule 更新

---

### Step 6: 威脅情資蒐集與分析 (SK-D01-032)

**目標**：建立 OT/ICS 威脅情資持續蒐集與分析能力。

**情資來源**：
- ICS-CERT / CISA advisories
- 廠商安全公告 (Siemens ProductCERT, ABB, Schneider)
- MITRE ATT&CK for ICS
- 商用威脅情資 feed
- OSINT 平台

**情資分析流程**：CVE 分析 → 威脅演員 profiling → 攻擊模式分析 → IOC enrichment → 與組織 OT 環境的相關性評估

**情資發布**：
- SOC/工程團隊：月報
- 管理層：季報
- 零日/緊急：即時告警

**⚠️ 避坑**：未過濾的威脅情資會造成資訊過載——必須按組織 OT 環境相關性篩選

---

## 3. 輸出 / 交付物

| # | 交付物 | 步驟 | 格式 |
|---|--------|------|------|
| 1 | SIEM Configuration Baseline | 1 | Markdown |
| 2 | Log Source Integration Checklist | 1 | Markdown |
| 3 | Alarm Category Specification | 2 | Markdown |
| 4 | Correlation Rule Library | 2 | Markdown/SIEM export |
| 5 | Incident Response Procedure | 3 | Markdown/Word |
| 6 | Incident Reporting Templates | 3 | Markdown |
| 7 | Investigation Authorization Template | 4 | Markdown |
| 8 | Forensic Evidence Chain of Custody | 4 | Markdown |
| 9 | Investigation Report Template | 4 | Markdown |
| 10 | Monthly Security Event Report | 5 | Markdown |
| 11 | Threat Intelligence Program Charter | 6 | Markdown |
| 12 | Monthly Threat Intelligence Report | 6 | Markdown |

---

## 4. 適用標準

| 標準 | 用途 |
|------|------|
| IEC 62443-2-1 §6.5.2.5-6 | 事件調查與鑑識 |
| IEC 62443-2-1 §7.8.4.2 | 日誌保留 (最少 1 年) |
| IEC 62443-3-3 FR6 (TRE) | 及時事件回應 |
| IEC 62443-2-4 | 安全服務提供者要求 |
| NIST SP 800-61 Rev. 3 | 事件回應指南 |
| NIST SP 800-82 Rev. 3 | OT 安全 |
| NIST SP 800-86 | 數位鑑識指南 |
| NIST SP 800-150 | 威脅情資共享 |
| ISO/IEC 27035 | 資安事件管理 |
| MITRE ATT&CK for ICS | 威脅分類框架 |

---

## 5. 驗收標準

| # | 項目 | 條件 |
|---|------|------|
| 1 | Log Source 覆蓋 | 100% 資產清冊設備已整合至 SIEM |
| 2 | 日誌保留 | ≥1 年保留，符合 IEC 62443-2-1 §7.8.4.2 |
| 3 | 告警分類 | ≥5 告警類別，每類有嚴重度定義 |
| 4 | 關聯規則 | ≥10 條 correlation rules，涵蓋 STRIDE 6 類 |
| 5 | 事件回應 | 4 級嚴重度+RTO 目標+損害控制任務 A-G |
| 6 | 鑑識程序 | 6 階段方法論+Chain of Custody+Master Timeline |
| 7 | 持續監控 | 月/季/年報週期已定義 |
| 8 | 威脅情資 | ≥3 情資來源已整合+月報產出 |
| 9 | False Positive | 追蹤機制建立，目標 <20% FP rate |
| 10 | 演練 | 至少 1 次 tabletop exercise 已完成 |

---

## 6. 工時參考

| 步驟 | Junior | Senior | 備註 |
|------|--------|--------|------|
| Step 1 SIEM 配置 | 12-18 pd | 5-8 pd | 含 OT protocol parser |
| Step 2 告警規則 | 8-12 pd | 3-5 pd | 含 tuning |
| Step 3 事件回應 | 8-12 pd | 4-6 pd | 含演練 |
| Step 4 鑑識程序 | 6-10 pd | 3-5 pd | 程序設計 |
| Step 5 持續監控 | 8-12 pd | 4-6 pd | 初始建置 |
| Step 6 威脅情資 | 6-10 pd | 3-5 pd | 程序+首次報告 |

---

## 7. 人類審核閘門

```
安全監控與事件回應已完成。
📋 範圍：6 步驟（SIEM→告警→IR→鑑識→持續監控→威脅情資）
📊 數據：Log Sources {n} | Rules {r} | IR Level L1-L4 | 情資源 {s}
⚠️ 待確認：{SIEM tuning 週期/演練排程}
👉 請 SAC 審核 PASS / FAIL / PASS with Conditions。
```

---

## 8. IEC 62443 生命週期

| Phase | 角色 | 步驟 |
|-------|------|------|
| R3 | 部署：SIEM 配置、規則建立、程序撰寫 | 1-4, 6 |
| R4 | 營運：持續監控、事件回應、情資更新 | 3-6 持續 |

---

## 9. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D01-014 | SIEM Configuration and Tuning | Log source 整合、correlation rules、dashboard |
| SK-D01-015 | Security Alarm Rule Design | 告警分類、關聯邏輯、anomaly detection |
| SK-D01-016 | Incident Response Procedure | 4 級嚴重度、RTO、損害控制 A-G |
| SK-D01-017 | Incident Investigation & Forensics | 6 階段鑑識、Chain of Custody、Timeline |
| SK-D01-018 | Continuous Security Monitoring | 6 階段運營、月/季/年報 |
| SK-D01-032 | Threat Intelligence Collection | 情資來源、CVE 分析、IOC、月報 |

<!-- Phase 6: Deep enhancement from 6 SK definitions. Enhanced 2026-03-19. -->
