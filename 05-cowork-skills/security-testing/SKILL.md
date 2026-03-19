---
name: security-testing
description: >
  Execute security and performance testing for OT/ICS environments including performance
  baseline establishment, application security testing, penetration testing, vulnerability
  scanning, and security inspection/test protocol development.
  MANDATORY TRIGGERS: 安全測試, security testing, 滲透測試, penetration testing,
  弱點掃描, vulnerability scanning, 效能基線, performance baseline,
  應用安全測試, application security testing, 安全檢驗, security inspection,
  pentest, 弱掃, vuln scan, OT 安全測試, 安全驗證, security verification.
  Use this skill for security testing, pentesting, vulnerability scanning, and performance
  baseline tasks in OT/ICS projects.
---

# 安全性與效能測試 (Security & Performance Testing)

本 Skill 整合 5 個工程技能定義，提供 OT/ICS 環境安全測試的完整框架——從效能基線到滲透測試到安全檢驗協定。適用於 R3 (驗證) 階段。

---

## 0. 初始化

1. **加固完成**：系統加固 (SK-D01-019) 已完成
2. **DTRA 可用**：詳細風險評估 (SK-D01-007) 驅動測試範圍
3. **Rules of Engagement**：已取得測試授權 (PtW)
4. **測試環境**：已辨識測試 vs 生產環境邊界

---

## 1. 輸入

| 類別 | 輸入 | 來源 |
|------|------|------|
| 風險 | DTRA 風險登錄冊 | SK-D01-007 |
| 架構 | Zone/Conduit + 防火牆規則 | SK-D01-001/003 |
| 加固 | 加固報告 | SK-D01-019 |
| 資產 | 資產清冊 | SK-D01-005 |
| 標準 | ID14 安全檢驗測試協定 exemplar | source-documents/ |
| 授權 | Rules of Engagement / PtW | 專案管理 |

---

## 2. 工作流程

### Step 1: 效能基線建立 (SK-D08-007)

**目標**：在 commissioning 期間建立系統效能基線，作為異常偵測參考。

**操作步驟**：

1. **定義基線指標**：

| 指標類別 | 量測項目 | 典型基線值 |
|---------|---------|-----------|
| 網路 | Throughput, Latency, Packet loss | <1ms latency, <0.01% loss |
| 主機 | CPU, Memory, Disk I/O | <30% CPU, <60% Memory |
| 應用 | Response time, Transaction rate | <2s response |
| 控制 | Scan cycle time, Control loop timing | Per design spec |

2. **量測方法**：72 hr 穩態量測→統計 mean/std/p95/p99
3. **基線文件化**：每個指標的 acceptable range
4. **異常閾值設定**：mean ± 3σ 或 domain-specific rules

**⚠️ 避坑**：基線量測需在正常營運條件下——startup transient 不算

---

### Step 2: 應用安全測試 (SK-D08-008)

**目標**：測試 OT/ICS 軟體元件的應用層安全。

**測試範圍**：SCADA server, HMI web UI, historian, EMS/DERMS

**測試類別**：

| 類別 | 測試項目 | 工具 |
|------|---------|------|
| 認證 | 暴力登入、預設帳號、session hijack | Burp Suite, OWASP ZAP |
| 授權 | 越權存取、角色繞過 | Manual + Burp |
| 輸入驗證 | SQL injection, XSS, command injection | OWASP ZAP, sqlmap |
| Session | Session fixation, timeout, CSRF | Burp Suite |
| 加密 | TLS 版本、cipher suite、certificate | testssl.sh, nmap |

```bash
# testssl.sh — 檢查 SCADA Web UI 的 TLS 設定
./testssl.sh --severity HIGH --color 0 https://scada-hmi.local:443
```

**⚠️ 避坑**：OT 應用測試不能使用 fuzzing——可能導致 PLC crash；read-only 測試優先

---

### Step 3: 滲透測試 (SK-D08-009)

**目標**：依 Rules of Engagement 對 OT/ICS 執行滲透測試。

**OT 滲透測試特殊規則**：

| 規則 | 原因 |
|------|------|
| **禁止** fuzzing 控制協定 (Modbus, DNP3) | 可能導致設備異常 |
| **禁止** DoS 測試 on live systems | 可能影響 safety |
| **要求** 即時回報 critical findings | 不能等報告 |
| **要求** Safety engineer standby | 以防影響 safety function |
| **限制** 測試時段 | 維護窗口內 |

**測試階段**：
1. **Reconnaissance**：被動掃描、OSINT、architecture review
2. **Vulnerability Assessment**：弱掃 (Step 4)
3. **Exploitation** (受控)：僅對授權目標，non-destructive
4. **Post-Exploitation**：lateral movement 評估
5. **Reporting**：findings + remediation + evidence

**⚠️ 避坑**：OT pentest 不是 IT pentest——破壞性測試可能導致人身安全事故；需 safety engineer 在場

---

### Step 4: 弱點掃描與報告 (SK-D08-010)

**目標**：使用 OT-aware 弱掃工具執行系統化弱點掃描。

**操作步驟**：

1. **工具選擇**：OT-aware scanner (Tenable.ot, Claroty, Nozomi)——不用純 IT scanner
2. **掃描配置**：
   ```bash
   # Nessus — OT-safe scan policy
   nessuscli scan --targets=10.30.0.0/24 \
     --policy="ICS-Safe-Scan" \
     --exclude-checks="dos,brute-force,fuzzing" \
     --output=ot-zone-scan.csv
   ```
3. **結果分析**：
   ```markdown
   | Vuln ID | CVE | Severity | Asset | Zone | CVSS | Remediation | Status |
   |---------|-----|----------|-------|------|------|-------------|--------|
   | V-001 | CVE-2024-xxxx | Critical | PLC-01 | OT | 9.8 | Patch v2.1 | Open |
   | V-002 | CVE-2024-yyyy | High | HMI-01 | OT | 7.5 | Config change | Fixed |
   ```
4. **補救計畫**：每個 Critical/High 弱點有 remediation + timeline
5. **排除 false positive**：OT 設備常有 FP——需人工驗證

**⚠️ 避坑**：純 IT 弱掃工具可能 crash OT 設備——必須用 OT-aware 工具；某些 legacy PLC 無法掃描

---

### Step 5: 安全檢驗測試協定 (SK-D08-014)

**目標**：開發涵蓋 14 個安全類別的完整檢驗測試協定 (per ID14 exemplar)。

**14 個測試類別** (per ID14)：

| # | 類別 | 驗證內容 |
|---|------|---------|
| 1 | Access Control | 帳號、RBAC、密碼政策 |
| 2 | Use Control | 授權、session 管理 |
| 3 | Data Integrity | 通訊完整性、防竄改 |
| 4 | Data Confidentiality | 加密、資料保護 |
| 5 | Restricted Data Flow | 防火牆、分段、ACL |
| 6 | Timely Response | 告警、事件回應 |
| 7 | Resource Availability | DoS 防護、備份、復原 |
| 8 | System Hardening | CIS Benchmark 合規 |
| 9 | Malware Protection | AV/EDR 部署驗證 |
| 10 | Patch Management | 補丁程序驗證 |
| 11 | Backup/Restore | 備份完整性+復原測試 |
| 12 | Remote Access | VPN/MFA/Recording |
| 13 | Physical Security | 實體存取控制 |
| 14 | SIS Security | SIS 隔離+SIL 保護 |

**產出**：每個類別的 test case + expected result + actual result + pass/fail

**⚠️ 避坑**：測試協定需在 FAT 階段開發——不能等到 SAT 才開始設計

---

## 3. 輸出

| # | 交付物 | 步驟 |
|---|--------|------|
| 1 | Performance Baseline Report | 1 |
| 2 | Application Security Test Report | 2 |
| 3 | Penetration Test Report | 3 |
| 4 | Vulnerability Scan Report + Remediation Plan | 4 |
| 5 | Security Inspection & Test Protocol | 5 |
| 6 | Test Evidence Package (screenshots, logs) | All |

---

## 4. 驗收標準

| # | 項目 | 條件 |
|---|------|------|
| 1 | 基線 | 效能基線已建立，含 mean/std/p95 |
| 2 | 應用測試 | OWASP Top 10 測試完成 (OT-adapted) |
| 3 | Pentest | 依 RoE 完成，critical findings 即時回報 |
| 4 | 弱掃 | OT-aware 工具，每個 Critical/High 有 remediation |
| 5 | 測試協定 | 14 類別全覆蓋，每類有 test case |
| 6 | 零事故 | 測試期間無非預期 OT 系統中斷 |
| 7 | 證據 | 所有測試有 evidence (截圖/日誌) |

---

## 5. 工時參考

| 步驟 | Junior | Senior | 備註 |
|------|--------|--------|------|
| Step 1 效能基線 | 3-5 pd | 2-3 pd | 72hr 量測+分析 |
| Step 2 應用測試 | 5-8 pd | 3-5 pd | SCADA/HMI/Historian |
| Step 3 滲透測試 | 8-12 pd | 5-8 pd | 含報告 |
| Step 4 弱點掃描 | 3-5 pd | 2-3 pd | OT-aware tool |
| Step 5 測試協定 | 5-8 pd | 3-5 pd | 14 類別 |

---

## 6. 人類審核閘門

```
安全測試已完成。
📋 範圍：效能基線 + 應用測試 + Pentest + 弱掃 + 14 類檢驗協定
📊 弱點：Critical {c} | High {h} | Medium {m} | FP 排除 {fp}
📊 Pentest：findings {f} 個 | 已 remediate {r} 個
⚠️ 測試期間非預期中斷：{0/N}
👉 請 SAC + STC 審核 PASS / FAIL / PASS with Conditions。
```

---

## 7. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D08-007 | Performance Baseline | 效能指標、72hr 量測、異常閾值 |
| SK-D08-008 | Application Security Testing | OWASP、Burp Suite、OT 適配 |
| SK-D08-009 | Penetration Testing | OT pentest 規則、非破壞性、RoE |
| SK-D08-010 | Vulnerability Scanning | OT-aware tools、CVE 比對、FP 排除 |
| SK-D08-014 | Security Inspection Protocol | 14 類別測試協定、ID14 exemplar |

<!-- Phase 6: Deep enhancement from 5 SK definitions. Enhanced 2026-03-19. -->
