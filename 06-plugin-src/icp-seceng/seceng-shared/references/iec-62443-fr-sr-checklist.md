# IEC 62443-3-3 FR/SR Quick Reference Checklist

**用途**：icp-seceng Plugin 各 Skill 共用。用於 DTRA、SL-T 評估、設計審查。

---

## Foundational Requirements (FR) 與 System Requirements (SR) 對照表

| FR | FR Name | Key SRs | SL-1 | SL-2 | SL-3 | SL-4 |
|----|---------|---------|------|------|------|------|
| FR1 | Identification & Authentication (IAC) | SR 1.1 Human user ID, SR 1.2 SW process ID, SR 1.3 HW asset ID, SR 1.5 Authenticator mgmt, SR 1.7 Password strength, SR 1.9 Public key auth, SR 1.10 Authenticator feedback, SR 1.13 Access via untrusted networks | ● | ●● | ●●● | ●●●● |
| FR2 | Use Control (UC) | SR 2.1 Authorization enforcement, SR 2.2 Wireless use control, SR 2.4 Mobile code, SR 2.5 Session lock, SR 2.6 Remote session termination, SR 2.8 Auditable events, SR 2.9 Audit storage, SR 2.12 Non-repudiation | ● | ●● | ●●● | ●●●● |
| FR3 | System Integrity (SI) | SR 3.1 Communication integrity, SR 3.2 Malicious code protection, SR 3.3 Security functionality verification, SR 3.4 SW/info integrity, SR 3.5 Input validation, SR 3.8 Session integrity | ● | ●● | ●●● | ●●●● |
| FR4 | Data Confidentiality (DC) | SR 4.1 Info confidentiality, SR 4.2 Info persistence, SR 4.3 Use of cryptography | ○ | ● | ●● | ●●● |
| FR5 | Restricted Data Flow (RDF) | SR 5.1 Network segmentation, SR 5.2 Zone boundary protection, SR 5.3 General-purpose person-to-person comm restrictions, SR 5.4 Application partitioning | ● | ●● | ●●● | ●●●● |
| FR6 | Timely Response to Events (TRE) | SR 6.1 Audit log accessibility, SR 6.2 Continuous monitoring | ○ | ● | ●● | ●●● |
| FR7 | Resource Availability (RA) | SR 7.1 DoS protection, SR 7.2 Resource management, SR 7.3 Control system backup, SR 7.4 Control system recovery, SR 7.6 Network/security config settings, SR 7.7 Least functionality, SR 7.8 Control system component inventory | ● | ●● | ●●● | ●●●● |

**圖例**: ○ = Optional, ● = Minimal, ●● = Moderate, ●●● = Substantial, ●●●● = Comprehensive

---

## SL-T 對照速查

| SL | 防護對象 | 典型場景 |
|----|---------|---------|
| SL-0 | 無特定安全要求 | 非關鍵資訊顯示 |
| SL-1 | 防止意外違規 | 一般辦公 IT Zone |
| SL-2 | 防止使用簡單手段的蓄意攻擊 | Server Room、一般 OT Zone |
| SL-3 | 防止使用精密手段的蓄意攻擊 | 關鍵控制系統、SCADA |
| SL-4 | 防止國家級攻擊者 | 核設施、關鍵基礎設施 |

---

## Gate 3 FR/SR 驗證規則 (GOV-SD)

- Gate 3 時所有 applicable SR 狀態必須為 **Implemented** (不接受 Planned)
- 每個 SR 需有 design evidence reference
- 殘餘風險需按 GOV-SD 權限層級簽核
