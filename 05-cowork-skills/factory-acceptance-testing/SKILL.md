---
name: factory-acceptance-testing
description: >
  工廠驗收測試。
  Develop the Factory Acceptance Test (FAT) procedure document that defines the test protocol for verifying security and functional requirements at the 。Design security-specific FAT (Factory Acceptance Test) test cases that comprehensively validate the
  MANDATORY TRIGGERS: FAT 程序撰寫, 安全 FAT 測試案例設計, 工廠驗收測試, access-control, security-testing, test-procedure, factory acceptance testing, IEC-62443, network-segmentation, factory-acceptance-testing, pre-shipment.
  Use this skill for factory acceptance testing tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 工廠驗收測試

本 Skill 整合 2 個工程技能定義，提供工廠驗收測試的完整工作流程。
適用領域：Testing & Commissioning（D08）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D01-002, SK-D01-003, SK-D01-006, SK-D01-007, SK-D01-019

---

## 1. 輸入

- Security Functional Description Specification (from SK-D09-002 ⏳) — SR requirements that must be verified
- FR/SR mapping matrix (from SK-D01-007) — specifies which SRs apply per zone/device
- Zone/Conduit architecture (from SK-D01-001) — defines the security topology to be tested
- Endpoint hardening specifications (from SK-D01-019) — hardening configurations to verify during FAT
- Account and access control policy (from SK-D01-020) — RBAC implementation to verify
- Malware protection deployment plan (from SK-D01-023) — antivirus configuration to verify
- Security Functional Specification (from SK-D09-002)
- Security Requirements specification including FR-SR mapping (from SK-D01-006, SK-D01-007)
- System architecture and zone/conduit diagram (from SK-D01-001)
- Access control matrix and RBAC policies (from SK-D01-003)
- Encryption and key management specification (from SK-D05-001 ⏳)
- System hardening checklist and baseline standards (from SK-D01-002)

---

## 2. 工作流程

### Step 1: FAT 程序撰寫
**SK 來源**：SK-D08-001 — FAT Procedure Development

執行FAT 程序撰寫：Develop the Factory Acceptance Test (FAT) procedure document that defines the test protocol for verifying security and functional requirements at the 

**本步驟交付物**：
- FAT Procedure Document (per ID14 exemplar format):
- Test scope and objectives: what is being verified, what is out of scope
- Test environment requirements: lab setup, network configuration, simulated loads

### Step 2: 安全 FAT 測試案例設計
**SK 來源**：SK-D08-002 — Security FAT Test Case Design

執行安全 FAT 測試案例設計：Design security-specific FAT (Factory Acceptance Test) test cases that comprehensively validate the security controls and hardening of the OT/ICS syst

**本步驟交付物**：
- Security FAT Test Plan: overview of security testing scope, test environment setup requirements, safety considerations, and test execution schedule
- Security FAT Test Case Catalog: prioritized list of all security test cases with test ID, description, preconditions, test steps, expected results, an
- Access Control Test Cases: user authentication (valid/invalid credentials, multi-factor), authorization (role-based access, zone boundaries, conduit r

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | FAT Procedure Document (per ID14 exemplar format): | 依需求 |
| 2 | Test scope and objectives: what is being verified, what is out of scope | 依需求 |
| 3 | Test environment requirements: lab setup, network configuration, simulated loads | 依需求 |
| 4 | Test categories (per ID14 14-category structure): | 依需求 |
| 5 | Physical security inspection | 依需求 |
| 6 | Network architecture verification | 依需求 |
| 7 | Security FAT Test Plan: overview of security testing scope, test environment setup requirements, safety considerations, and test execution schedule | 依需求 |
| 8 | Security FAT Test Case Catalog: prioritized list of all security test cases with test ID, description, preconditions, test steps, expected results, an | Markdown |
| 9 | Access Control Test Cases: user authentication (valid/invalid credentials, multi-factor), authorization (role-based access, zone boundaries, conduit r | 依需求 |
| 10 | Network Segmentation Test Cases: inter-zone communication validation (allowed vs. blocked traffic), conduit rule enforcement, zone boundary crossing v | 依需求 |
| 11 | Encryption and Cryptography Test Cases: encryption validation (TLS version, cipher strength), key exchange verification, data-in-transit encryption, c | 依需求 |
| 12 | Logging and Audit Trail Test Cases: log generation on security events, audit trail completeness, timestamp validation, log integrity verification (tam | 依需求 |

---

## 4. 適用標準

- IEC 62443-2-4 SP.09.01–SP.09.04: Verification and validation requirements
- IEC 62443-3-3: System Security Requirements — SR verification drives FAT test categories
- IEC 62443-4-2: Component Security Requirements — device-level verification requirements
- ISO 17025: General requirements for the competence of testing and calibration laboratories (supplementary, for test envi
- GOV-SD: Gate 3 delivery checklist — FAT completion evidence required; testing results serve as SR verification evidence
- IEC 62443-3-3: System Security Requirements and Security Levels — Functional Security Requirements (FR) and Security Lev
- IEC 62443-2-4: Technical security measures for OT/ICS systems — security control implementation guidance
- NIST SP 800-115: Technical Security Testing and Assessment — security testing methodology and best practices
- OWASP Testing Guide: guidance on access control testing, encryption validation, and security testing in general
- IEC 62443-1-1: Terminology, concepts and models — foundational security concepts

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | FAT procedure covers all 14 test categories (per ID14 exemplar) or documents exp | ✅ 已驗證 |
| 2 | Every applicable SR in the FR/SR mapping matrix has at least one corresponding F | ✅ 已驗證 |
| 3 | Each test case includes: unique ID, clear steps, expected result, and unambiguou | ✅ 已驗證 |
| 4 | Test environment specification is sufficient to reproduce the test: lab configur | ✅ 已驗證 |
| 5 | Re-test criteria defined: conditions for re-execution of failed tests, maximum r | ✅ 已驗證 |
| 6 | FAT procedure reviewed and approved by Security Engineering Role and Design QA R | ✅ 已驗證 |
| 7 | Every Functional Security Requirement (FR) in SK-D09-002 has at least one corres | ✅ 已驗證 |
| 8 | Access control test cases cover: valid authentication, invalid credentials, role | ✅ 已驗證 |
| 9 | Network segmentation test cases cover: allowed inter-zone communication, blocked | ✅ 已驗證 |
| 10 | Encryption test cases cover: TLS version and cipher strength validation, certifi | ✅ 已驗證 |
| 11 | Logging and audit trail test cases cover: event logging completeness, timestamp  | ✅ 已驗證 |
| 12 | Security alarm test cases cover: alarm triggering on policy violations, alarm de | ✅ 已驗證 |
| 13 | Hardening compliance test cases cover: firmware version, disabled services, remo | ✅ 已驗證 |
| 14 | Test cases are documented in a consistent format with clear preconditions, test  | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D08-001 | | Junior (< 2 yr) | 10–15 person-days | Assumes ~30 applicable SRs, 14 test categories, ~100 individ |
| SK-D08-001 | | Senior (5+ yr) | 5–8 person-days | Same scope; senior leverages reusable test case templates and S |
| SK-D08-002 | | Junior (< 2 yr) | 8–15 person-days | Assumes moderate system complexity (~5 zones, ~3 user roles,  |
| SK-D08-002 | | Senior (5+ yr) | 4–8 person-days | Same scope; senior can leverage prior security testing experien |
| SK-D08-002 | Notes: Complex systems with multi-zone architectures, many user roles, or stringent encryption requi |

---

## 7. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 輸入完整性 | 所有必要輸入文件已讀取並摘要 |
| 2 | 流程覆蓋 | 2 個工作步驟皆已執行並有產出 |
| 3 | 輸出完整性 | 所有交付物已產出、格式正確、非空白 |
| 4 | 標準合規 | 產出引用的標準版本正確 |
| 5 | 術語一致 | 專案術語、縮寫與 glossary 一致 |
| 6 | 跨步驟一致 | 各步驟產出間無矛盾（如數量、SL等級） |

---

## 8. 人類審核閘門

完成所有工作步驟後，暫停並向使用者提交審核：

```
工廠驗收測試已完成。
📋 執行範圍：2 個工程步驟（SK-D08-001, SK-D08-002）
📊 交付物清單：
  - FAT Procedure Document (per ID14 exemplar format):
  - Test scope and objectives: what is being verified, what is out of scope
  - Test environment requirements: lab setup, network configuration, simulated loads
  - Test categories (per ID14 14-category structure):
  - Physical security inspection
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
| Domain | D08 (Testing & Commissioning) |
| SK 覆蓋 | SK-D08-001, SK-D08-002 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D08-001 | FAT Procedure Development | FAT 程序撰寫 | Develop the Factory Acceptance Test (FAT) procedure document |
| SK-D08-002 | Security FAT Test Case Design | 安全 FAT 測試案例設計 | Design security-specific FAT (Factory Acceptance Test) test  |

<!-- Phase 5 Wave 2 deepened: SK-D08-001, SK-D08-002 -->