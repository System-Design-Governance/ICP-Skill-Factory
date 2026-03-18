---
name: security-system-hardening
description: >
  系統安全加固。
  Implement systematic security hardening across all endpoint categories within the SuC — including Windows-based host servers (SCADA HMI), ICS embedded。Design and implement the account management policy and Role-Based Access Control (RBAC) framework f
  MANDATORY TRIGGERS: 帳號與存取控制管理, 備份與還原程序設計, 安全補丁管理, 端點安全加固實施, 遠端存取安全配置, 系統安全加固, 惡意程式防護實施, vpn, configuration, Endpoint Hardening Implementation, session-recording, multi-factor-authentication, antivirus, least-privilege, endpoint-security.
  Use this skill for security system hardening tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 系統安全加固

本 Skill 整合 6 個工程技能定義，提供系統安全加固的完整工作流程。
適用領域：OT Cybersecurity（D01）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D01-005, SK-D01-007, SK-D01-009, SK-D01-011, SK-D01-014

---

## 1. 輸入

- Asset inventory with device specifications (from SK-D01-005: Asset Inventory Development)
- Zone/Conduit architecture with SL-T assignments per zone (from SK-D01-001)
- FR/SR requirements mapping per device type (from SK-D01-007: Detailed Risk Assessment — countermeasure specifications)
- Vendor hardening guides and CIS Security Configuration Benchmarks per device category
- Vulnerability scanning results (Nessus or equivalent) — baseline state before hardening
- Equipment baseline with firmware/software versions and serial numbers (from ID12 exemplar: SP06.02BR asset baselining)
- Asset inventory with device types and OS platforms (from SK-D01-005)
- Zone/Conduit architecture with SL-T assignments (from SK-D01-001) — SL drives access control rigor
- FR/SR mapping for access control requirements (from SK-D01-007: SR 1.x Human User Identification/Authentication, SR 2.x Use Control)
- Customer requirements for least privilege and mutual authentication
- Organizational Active Directory structure and Group Policy baseline
- Existing account inventory (for brownfield: current user accounts across all devices)

---

## 2. 工作流程

### Step 1: 端點安全加固實施
**SK 來源**：SK-D01-019 — Endpoint Hardening Implementation

執行端點安全加固實施：Implement systematic security hardening across all endpoint categories within the SuC — including Windows-based host servers (SCADA HMI), ICS embedded

**本步驟交付物**：
- Hardening Implementation Report per device category:
- Server Hardening Checklist** (per ID13 exemplar): OS patched, unnecessary services removed, user authentication configured, access controls set, secur
- Network Device Hardening Checklist**: firmware updated with hash verification, unused physical interfaces shut down, switch port access control, encry

### Step 2: 帳號與存取控制管理
**SK 來源**：SK-D01-020 — Account and Access Control Management

執行帳號與存取控制管理：Design and implement the account management policy and Role-Based Access Control (RBAC) framework for all systems within the SuC, covering centralized

**本步驟交付物**：
- Account Management Policy Document (per ID07 §4.0 exemplar):
- Centralized account management approach (AD + GPO for Windows-based hosts)
- Local account management rules (one local account per host, least privilege, encrypted transit)

### Step 3: 安全補丁管理
**SK 來源**：SK-D01-021 — Security Patch Management

執行安全補丁管理：Design and implement the security patch management procedure for all system categories within the SuC — covering Windows-based host servers (WBHS), IC

**本步驟交付物**：
- Patch Management Procedure Document (per ID07 §8.0 exemplar):
- Patch acquisition channels identification (vendor portals, ICS-CERT, security feeds)
- Applicability assessment methodology (Applies / N/A / Deferred with justification)

### Step 4: 備份與還原程序設計
**SK 來源**：SK-D01-022 — Backup and Restore Procedure Design

執行備份與還原程序設計：Design the comprehensive backup and restore procedure covering all device categories within the SuC, including backup targets, methods, schedules, ret

**本步驟交付物**：
- Backup and Restore Procedure Document (per ID07 §6.0 exemplar):
- Backup target definitions for 3 device categories:
- Windows-based host servers (SCADA HMI): Acronis Agent, centralized scheduling, system image + configuration

### Step 5: 惡意程式防護實施
**SK 來源**：SK-D01-023 — Malware Protection Implementation

執行惡意程式防護實施：Design and implement the malware protection framework for all endpoint categories within the SuC, covering three deployment scenarios: on-site host co

**本步驟交付物**：
- Malware Protection Implementation Document (per ID07 §7.0 exemplar):
- General rules: systematic approach to malware protection in OT environments with risk assessment of antivirus impact
- Central management architecture: centralized console deployment, policy enforcement, real-time threat visibility

### Step 6: 遠端存取安全配置
**SK 來源**：SK-D01-028 — Remote Access Security Configuration

執行遠端存取安全配置：Configure secure remote access mechanisms for OT/ICS environments including VPN setup, jump server configuration, multi-factor authentication (MFA), s

**本步驟交付物**：
- VPN Configuration Baseline: VPN technology selection, tunnel encryption algorithm, authentication method (certificate, PSK), key exchange parameters, 
- VPN Authentication Configuration: certificates and certificate authority (CA) hierarchy for site-to-site VPN, or client certificate distribution and e
- Jump Server (Bastion Host) Configuration: hardened OS baseline, firewall rules, allowed protocols, user account provisioning procedure, privileged acc

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Hardening Implementation Report per device category: | Markdown |
| 2 | Server Hardening Checklist** (per ID13 exemplar): OS patched, unnecessary services removed, user authentication configured, access controls set, secur | Markdown |
| 3 | Network Device Hardening Checklist**: firmware updated with hash verification, unused physical interfaces shut down, switch port access control, encry | Markdown |
| 4 | IACS Embedded Device Hardening Checklist**: remote program changes disabled, firmware updated with hash verification, unused network interfaces disabl | Markdown |
| 5 | Physical Hardening Documentation: port/interface disable strategy per device (e.g., VGA/DVI/USB/RS232 disabled; RJ45/PS2 enabled for operations) | 依需求 |
| 6 | Protocol Hardening Tables: enabled vs. disabled protocols per device with justification | 依需求 |
| 7 | Account Management Policy Document (per ID07 §4.0 exemplar): | 依需求 |
| 8 | Centralized account management approach (AD + GPO for Windows-based hosts) | 依需求 |
| 9 | Local account management rules (one local account per host, least privilege, encrypted transit) | 依需求 |
| 10 | Account naming conventions and prohibited practices (no hidden accounts, no unchangeable passwords) | 依需求 |
| 11 | User identity validity rules (configurable expiry, immediate deletion of invalid accounts) | 依需求 |
| 12 | Default account handling (rename default admin, change default passwords post-installation) | 依需求 |

---

## 4. 適用標準

- IEC 62443-2-4 SP06.02BR: Asset baselining and configuration management
- IEC 62443-3-3: System security requirements — SR mapping drives hardening scope per SL
- IEC 62443-4-2: Technical security requirements for IACS components — device-level requirements
- CIS Benchmarks: Platform-specific security configuration standards
- NIST SP 800-123: Guide to General Server Security (supplementary)
- GOV-SD: Gate 3 countermeasure evidence — hardened configuration must have design evidence reference
- IEC 62443-2-4 SP06.02BR: Account and access management requirements
- IEC 62443-3-3 SR 1.1–1.13: Human User Identification and Authentication
- IEC 62443-3-3 SR 2.1–2.12: Use Control (authorization, least privilege, session management)
- IEC 62443-4-2: Component-level authentication and authorization requirements

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | Hardening checklists completed for 100% of devices in the asset inventory, with  | ✅ 已驗證 |
| 2 | Post-hardening vulnerability scan shows no Critical or High findings that existe | ✅ 已驗證 |
| 3 | Physical hardening documented: all unused ports/interfaces disabled with per-dev | ✅ 已驗證 |
| 4 | No default passwords remain on any device; all credentials changed and documente | ✅ 已驗證 |
| 5 | Secure remote management enforced: SSH v2 only (no Telnet), encrypted passwords, | ✅ 已驗證 |
| 6 | Exception log documents all devices where full hardening is infeasible, with com | ✅ 已驗證 |
| 7 | RBAC framework defines at least 4 authorization levels with clear separation of  | ✅ 已驗證 |
| 8 | Rights matrix covers all device types in the asset inventory with explicit role  | ✅ 已驗證 |
| 9 | No default passwords remain on any device post-implementation; all default admin | ✅ 已驗證 |
| 10 | Password policies enforced: complexity meeting customer/employer standards, rota | ✅ 已驗證 |
| 11 | All accounts reviewed and approved by employer/customer as documented in account | ✅ 已驗證 |
| 12 | Exception register documents all deviations from standard policy with compensati | ✅ 已驗證 |
| 13 | Patch management procedure covers all three device categories (WBHS, ICS, networ | ✅ 已驗證 |
| 14 | Patch applicability register maintained: every vendor patch release has a docume | ✅ 已驗證 |
| 15 | Configuration Revision Control table is current: every patched device has pre-pa | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D01-019 | | Junior (< 2 yr) | 15–20 person-days | Assumes ~50 devices across 3 categories (server, network, IA |
| SK-D01-019 | | Senior (5+ yr) | 8–12 person-days | Same scope; senior leverages scripted hardening templates and  |
| SK-D01-020 | | Junior (< 2 yr) | 8–12 person-days | Assumes ~50 devices, 5 user roles, AD-based environment; incl |
| SK-D01-020 | | Senior (5+ yr) | 4–6 person-days | Same scope; senior leverages RBAC templates and AD scripting | |
| SK-D01-020 | Notes: Environments without Active Directory (pure local accounts) require 1.5× effort due to per-de |
| SK-D01-021 | | Junior (< 2 yr) | 8–10 person-days | Initial procedure design and configuration baseline for ~50 d |
| SK-D01-021 | | Senior (5+ yr) | 4–6 person-days | Same scope; senior leverages existing CCM templates and vendor- |
| SK-D01-021 | Notes: ID07 §8.0 baseline indicates substantial documentation effort across WBHS and ICS/network dev |

---

## 7. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 輸入完整性 | 所有必要輸入文件已讀取並摘要 |
| 2 | 流程覆蓋 | 6 個工作步驟皆已執行並有產出 |
| 3 | 輸出完整性 | 所有交付物已產出、格式正確、非空白 |
| 4 | 標準合規 | 產出引用的標準版本正確 |
| 5 | 術語一致 | 專案術語、縮寫與 glossary 一致 |
| 6 | 跨步驟一致 | 各步驟產出間無矛盾（如數量、SL等級） |
| 7 | 依賴追溯 | 外部依賴 SK 的輸入已驗證可用 |

---

## 8. 人類審核閘門

完成所有工作步驟後，暫停並向使用者提交審核：

```
系統安全加固已完成。
📋 執行範圍：6 個工程步驟（SK-D01-019, SK-D01-020, SK-D01-021, SK-D01-022, SK-D01-023, SK-D01-028）
📊 交付物清單：
  - Hardening Implementation Report per device category:
  - Server Hardening Checklist** (per ID13 exemplar): OS patched, unnecessary services removed, user authentication configured, access controls set, secur
  - Network Device Hardening Checklist**: firmware updated with hash verification, unused physical interfaces shut down, switch port access control, encry
  - IACS Embedded Device Hardening Checklist**: remote program changes disabled, firmware updated with hash verification, unused network interfaces disabl
  - Physical Hardening Documentation: port/interface disable strategy per device (e.g., VGA/DVI/USB/RS232 disabled; RJ45/PS2 enabled for operations)
⚠️ 待確認事項：{列出 TBD 項目或需人工判斷的假設}
👉 請審核以上成果，確認 PASS / FAIL / PASS with Conditions。
```

**判定標準**：
- **PASS**：成果完整且正確，可進入下一階段或歸檔
- **FAIL**：發現重大缺漏或錯誤，需返工後重新提交
- **PASS with Conditions**：整體接受，但需補充特定項目後完成

---

## 9. IEC 62443 生命週期對應

| 項目 | 值 |
|------|---|
| 主要生命週期階段 | 依專案階段 |
| Domain | D01 (OT Cybersecurity) |
| SK 覆蓋 | SK-D01-019, SK-D01-020, SK-D01-021, SK-D01-022, SK-D01-023, SK-D01-028 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D01-019 | Endpoint Hardening Implementation | 端點安全加固實施 | Implement systematic security hardening across all endpoint  |
| SK-D01-020 | Account and Access Control Management | 帳號與存取控制管理 | Design and implement the account management policy and Role- |
| SK-D01-021 | Security Patch Management | 安全補丁管理 | Design and implement the security patch management procedure |
| SK-D01-022 | Backup and Restore Procedure Design | 備份與還原程序設計 | Design the comprehensive backup and restore procedure coveri |
| SK-D01-023 | Malware Protection Implementation | 惡意程式防護實施 | Design and implement the malware protection framework for al |
| SK-D01-028 | Remote Access Security Configuration | 遠端存取安全配置 | Configure secure remote access mechanisms for OT/ICS environ |

<!-- Phase 5 Wave 2 deepened: SK-D01-019, SK-D01-020, SK-D01-021, SK-D01-022, SK-D01-023, SK-D01-028 -->