---
name: security-system-hardening
description: >
  Execute comprehensive system security hardening for OT/ICS environments covering six domains:
  endpoint hardening (Windows servers, ICS devices, network equipment), account and access control
  management (RBAC, AD/GPO), security patch management, backup and restore procedures,
  malware protection deployment, and remote access security configuration.
  MANDATORY TRIGGERS: 系統加固, system hardening, 安全加固, security hardening,
  端點加固, endpoint hardening, 帳號管理, account management, RBAC, 存取控制,
  access control, 補丁管理, patch management, 備份還原, backup restore,
  惡意程式防護, malware protection, antivirus, EDR, 遠端存取, remote access,
  VPN, jump server, bastion host, MFA, 多因子認證.
  Use this skill for any system hardening task in OT/ICS/SCADA cybersecurity projects.
---

# 系統安全加固 (System Security Hardening)

本 Skill 整合 6 個工程技能定義，提供 OT/ICS 環境全面安全加固的完整工作流程——從端點加固到遠端存取安全。適用於 IEC 62443 生命週期 R2–R4 各階段。

---

## 0. 初始化

執行前確認：

1. **資產清冊**：已完成 (SK-D01-005)，含所有設備的 Zone 指派和 Criticality
2. **Zone/Conduit 設計**：已完成 (SK-D01-001)，SL-T 已指定
3. **風險評估**：初步 TRA (SK-D01-006) 或 DTRA (SK-D01-007) 產出可用
4. **網路架構圖**：已完成 (SK-D02-001)
5. **工具備妥**：弱掃工具 (Nessus/Tenable)、AV/EDR (Cortex XDR)、備份工具 (Acronis)

---

## 1. 輸入

| 類別 | 輸入項目 | 來源 |
|------|---------|------|
| 資產 | 資產清冊 (含 criticality) | SK-D01-005 |
| 架構 | Zone/Conduit 架構圖 + SL-T | SK-D01-001 |
| 風險 | TRA/DTRA 風險登錄冊 | SK-D01-006/007 |
| 標準 | FR/SR 對照表 | Plugin 共用 references/ |
| 範本 | 加固檢查清單模板 | Plugin 共用 templates/ |
| 政策 | 安全政策與程序計畫 | SK-D01-030 |
| 設備 | 各設備廠商加固指南 | CIS Benchmarks / 廠商文件 |

---

## 2. 工作流程

### Step 1: 端點安全加固 (SK-D01-019)

**目標**：對 SuC 內所有端點實施系統化安全加固。

**操作步驟**：

1. **分類設備**：從資產清冊按三類分組
   - **Windows 伺服器** (SCADA HMI, Historian, AD)
   - **ICS 嵌入式設備** (PLC, RTU, IED)
   - **網路設備** (Managed Switch, WAP, Firewall)

2. **基線掃描**：對每類設備執行加固前弱點掃描
   ```bash
   # Nessus CLI — 掃描目標 Zone
   nessuscli scan --targets=10.10.0.0/24 --policy="ICS-OT-Baseline" --output=pre-hardening-scan.csv
   ```

3. **依類別執行加固**：

   **Windows 伺服器**：移除不必要服務/角色、停用未使用實體埠、套用 CIS Benchmark、安裝 AV/EDR、設定稽核日誌→SIEM

   **ICS 嵌入式設備**：停用遠端程式變更、更新 Firmware (hash 驗證)、停用未使用介面/協定、變更預設密碼、啟用 Logging

   **網路設備**：更新 Firmware (hash 驗證)、關閉未使用介面、啟用 Port Security/802.1X、SSH v2 only、限制管理 IP

4. **驗證掃描**：加固後重新掃描比對改善
5. **例外登錄**：無法加固設備記錄補償控制

**⚠️ 避坑**：ICS 設備加固前必須取得廠商確認；安排維護窗口；firmware 需 hash 驗證；保留維護所需最小介面

---

### Step 2: 帳號與存取控制管理 (SK-D01-020)

**目標**：設計並實施 RBAC 框架和帳號管理政策。

**4-tier 授權層級**：

| 層級 | 名稱 | 權限 |
|------|------|------|
| L1 | Viewer | 唯讀/瀏覽 HMI |
| L2 | Control | 有限控制操作 |
| L3 | Engineering | 完整權限（除帳號管理） |
| L4 | System Manager | 完整權限（含帳號管理） |

**權限矩陣範例**：
```markdown
| 角色 | SCADA HMI | IED Ctrl | IED Prot | Switch | WAP |
|------|-----------|----------|----------|--------|-----|
| Operator | L2 | L1 | — | — | — |
| Engineer | L3 | L3 | L2 | L2 | L2 |
| Admin | L4 | L4 | L4 | L4 | L4 |
```

AD/GPO 設定→OU 對應 Zone→GPO 密碼政策→禁止共用帳號→變更預設密碼→FAT/SAT 驗證

**⚠️ 避坑**：無 AD 環境工時 ×1.5；service account 易被遺漏；OT 觸控螢幕密碼複雜度需務實調整

---

### Step 3: 安全補丁管理 (SK-D01-021)

**目標**：建立補丁管理生命週期程序。

**補丁評估流程**：適用性判斷 (Applies/N/A/Deferred) → 風險評估 (Criticality×Exploitability×Impact) → 測試環境驗證 → 備份 (SK-D01-022) → 部署 → 驗證 → CCM Table 記錄

**GOV-SD 觸發**：影響架構/SL/合約的重大補丁 → Gate 2 正式審查

**緊急補丁**：零日/主動利用漏洞的加速流程，含最大容許修補時間目標

**⚠️ 避坑**：OT 不能自動推送補丁；部署前必須備份；廠商未認證的補丁不能在 ICS 上部署

---

### Step 4: 備份與還原程序 (SK-D01-022)

**備份策略**：

| 類別 | 方法 | 排程 | 保留 |
|------|------|------|------|
| Windows | Acronis Agent → NAS | 6 個月/系統映像 | 依政策 |
| ICS | Config 匯出 → File Server | 組態變更時 | 6 個月 |
| 網路設備 | Config 匯出 → File Server | 組態變更時 | 6 個月 |

**災難劇本** (≥3)：伺服器崩潰→惡意程式污染備份→損毀設定檔

**⚠️ 避坑**：Air-gapped 需離線備份機制；備份伺服器本身需加固；復原程序要實測

---

### Step 5: 惡意程式防護 (SK-D01-023)

**三場景部署**：常駐主機 (Agent)、臨時設備 (連接前驗證)、可攜式媒體 (掃描後使用)

**Agent 部署驗證清單** (per ID12)：
```
□ 安裝成功  □ 系統功能完整  □ Agent→Controller 連線  □ 防護啟用
```

**⚠️ 避坑**：AV 可能影響 OT real-time 性能；Air-gapped 需 sneakernet 更新；某些 IACS 無法安裝 AV→network-based 補償

---

### Step 6: 遠端存取安全 (SK-D01-028)

**四大控制**：
- **VPN**：TLS 1.2+/AES-256、Certificate auth
- **Jump Server**：硬化 OS、PAM 整合、允許協定限制
- **MFA**：≥2 因子 (Certificate+Password 或 Password+TOTP)
- **Session Recording**：SL-2+ Zone 全錄、回放功能測試

**Break-glass 緊急存取程序**：事先定義、測試、文件化

**⚠️ 避坑**：遠端存取是最高風險攻擊面；別只靠 IP whitelist；Break-glass 要事先定義

---

## 3. 輸出 / 交付物

| # | 交付物 | 步驟 | 格式 |
|---|--------|------|------|
| 1 | Hardening Report (per category) | 1 | Markdown/Excel |
| 2 | Pre/Post Vulnerability Scan | 1 | CSV/PDF |
| 3 | Exception Log | 1 | Markdown |
| 4 | Account Management Policy | 2 | Markdown |
| 5 | RBAC Rights Matrix | 2 | Markdown |
| 6 | Password Policy | 2 | Markdown |
| 7 | Patch Management Procedure | 3 | Markdown |
| 8 | CCM Table | 3 | Excel |
| 9 | Backup/Restore Procedure | 4 | Markdown |
| 10 | Disaster Playbooks (≥3) | 4 | Markdown |
| 11 | Malware Protection Document | 5 | Markdown |
| 12 | AV Deployment Verification | 5 | Markdown |
| 13 | VPN/Jump Server Config | 6 | Markdown |
| 14 | Remote Access Matrix | 6 | Markdown |
| 15 | Session Recording Policy | 6 | Markdown |

---

## 4. 適用標準

| 標準 | 用途 |
|------|------|
| IEC 62443-2-4 SP06.02BR | 資產基線與組態管理 |
| IEC 62443-3-3 | FR/SR (FR1-AC, FR2-UC, FR3-SI, FR7-RA) |
| IEC 62443-4-2 | 元件安全要求 |
| CIS Benchmarks | 平台專屬安全組態 |
| NIST SP 800-123/800-40/800-34 | 伺服器安全/補丁/應變 |
| ISO 27001 A.9/A.12 | 存取控制/備份/惡意程式 |

---

## 5. 驗收標準

| # | 項目 | 條件 |
|---|------|------|
| 1 | 加固覆蓋 | 100% 設備有檢查清單 Pass/Fail/Exception |
| 2 | 弱掃改善 | 加固後無 Critical/High (或有例外+補償) |
| 3 | 預設密碼 | 100% 已變更 |
| 4 | RBAC | ≥4 層級，矩陣涵蓋所有設備類型 |
| 5 | 補丁追蹤 | 每個補丁有決策+理由 |
| 6 | 備份覆蓋 | 100% 設備有備份方法/排程/保留期 |
| 7 | 復原測試 | 每類設備至少一次 |
| 8 | AV 覆蓋 | 100% capable 設備已部署 |
| 9 | MFA | 所有遠端存取需兩因子 |
| 10 | Recording | SL-2+ Zone 已啟用+回放測試 |

---

## 6. 工時參考

| 步驟 | Junior | Senior | 備註 |
|------|--------|--------|------|
| Step 1 端點加固 | 15-20 pd | 8-12 pd | ~50 devices |
| Step 2 帳號管理 | 8-12 pd | 4-6 pd | AD-based |
| Step 3 補丁管理 | 8-10 pd | 4-6 pd | 初始程序 |
| Step 4 備份還原 | 6-10 pd | 3-5 pd | 含復原測試 |
| Step 5 惡意程式 | 10-15 pd | 5-8 pd | Cortex XDR |
| Step 6 遠端存取 | 12-18 pd | 5-8 pd | VPN+Jump+MFA |

---

## 7. 人類審核閘門

```
系統安全加固已完成。
📋 範圍：6 步驟（加固→帳號→補丁→備份→AV→遠端）
📊 數據：設備 {n} 台 | 弱掃 Critical {c}→{c2} | RBAC {r} 角色 | AV {pct}% | 遠端 {ra} 條
⚠️ 待確認：{例外設備/假設}
👉 請 SAC 審核 PASS / FAIL / PASS with Conditions。
```

---

## 8. IEC 62443 生命週期

| Phase | 角色 | 步驟 |
|-------|------|------|
| R2 | 設計：加固規格、RBAC、遠端架構 | 1-6 設計 |
| R3 | 實施：加固、部署、測試 | 1-6 執行 |
| R4 | 營運：補丁週期、帳號審查 | 2-4 持續 |

---

## 9. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D01-019 | Endpoint Hardening | 三類設備加固、CIS Benchmark、弱掃比對 |
| SK-D01-020 | Account/Access Control | 4-tier RBAC、AD/GPO、權限矩陣 |
| SK-D01-021 | Patch Management | 補丁生命週期、CCM Table、Gate 2 觸發 |
| SK-D01-022 | Backup/Restore | Acronis、3 類備份、災難劇本 |
| SK-D01-023 | Malware Protection | Cortex XDR、3 場景防護、Agent 驗證 |
| SK-D01-028 | Remote Access Security | VPN/Jump Server/MFA/Recording/Break-glass |

<!-- Phase 6: Deep enhancement from 6 SK definitions. Enhanced 2026-03-18. -->
