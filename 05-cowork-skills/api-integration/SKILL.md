---
name: api-integration
description: >
  API 與第三方集成。
  Integrate third-party APIs (weather services, market data feeds, grid operator interfaces, cloud platforms) with OT/ICS systems, enabling data exchang
  MANDATORY TRIGGERS: 第三方 API 串接, API 與第三方集成, rest-api, authentication, third-party-api, api integration, cloud-integration, soap-xml, Third-Party API Integration, data-encryption.
  Use this skill for api integration tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# API 與第三方集成

本 Skill 整合 1 個工程技能定義，提供API 與第三方集成的完整工作流程。
適用領域：System Integration（D07）。

---

## 0. 初始化

執行前確認：

1. **專案背景**：已取得專案範圍定義與系統邊界
2. **輸入文件**：下方§1 列出的輸入已備齊或已標註為 TBD
3. **適用標準**：已確認本專案適用的 IEC 62443 / ISO 標準版本
4. **前置依賴**：確認以下 SK 產出已可用：SK-D01-001, SK-D01-005, SK-D01-006, SK-D02-003, SK-D02-006, SK-D05-001

---

## 1. 輸入

- Third-party API technical documentation (REST/SOAP specification, authentication schemes, data models, rate limits)
- Network architecture and zone/conduit diagram (from SK-D01-001)
- Data requirements and information classification (from SK-D01-005, SK-D01-007)
- Security requirements and authentication policies (from SK-D01-002, SK-D01-003, SK-D01-006)
- Zone/conduit crossing approval documentation (per SK-D01-001 boundary)
- Redundancy and failover strategy (from SK-D02-006 ⏳)

---

## 2. 工作流程

### Step 1: 第三方 API 串接
**SK 來源**：SK-D07-007 — Third-Party API Integration

執行第三方 API 串接：Integrate third-party APIs (weather services, market data feeds, grid operator interfaces, cloud platforms) with OT/ICS systems, enabling data exchang

**本步驟交付物**：
- Third-Party API Integration Specification: API endpoint, authentication method, data format, rate limits, timeout behavior
- API Authentication and Credential Management Plan: credential storage, rotation schedule, access control (who can access credentials), audit trail req
- API Data Format Mapping Document: external API data format → internal system data format, including validation rules and type conversions for both RES

---

## 3. 輸出 / 交付物

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | Third-Party API Integration Specification: API endpoint, authentication method, data format, rate limits, timeout behavior | 依需求 |
| 2 | API Authentication and Credential Management Plan: credential storage, rotation schedule, access control (who can access credentials), audit trail req | 依需求 |
| 3 | API Data Format Mapping Document: external API data format → internal system data format, including validation rules and type conversions for both RES | 依需求 |
| 4 | Error Handling and Retry Logic Specification: timeout values, retry attempts, exponential backoff, fallback behavior, alert triggers | 依需求 |
| 5 | API Security Hardening Checklist: TLS/SSL version verification, certificate pinning (if applicable), API key encryption, data-in-transit encryption, s | Markdown |
| 6 | Zone/Conduit Crossing Configuration: explicit approval of inter-zone API traffic, firewall rule specifications (to be implemented in SK-D02-003 ⏳) | 依需求 |

---

## 4. 適用標準

- IEC 62443-2-4: Technical security measures for OT/ICS systems — API interface and data exchange security requirements
- OWASP Top 10 for API Security: guidance on API authentication, data validation, logging, and error handling
- NIST SP 800-82 Rev. 3: Guide to OT Security — guidance on third-party system integration and data exchange
- OWASP Secure Coding Practices: input validation, output encoding, credential management
- TLS 1.2 or TLS 1.3 (minimum): encryption standard for API data-in-transit
- IEC 62443-3-3: System Security Requirements and Security Levels — API integration security baselines

---

## 5. 驗收標準

| # | 驗收項目 | 通過條件 |
|---|---------|---------|
| 1 | API endpoint, authentication method, data format, and rate limits are explicitly | ✅ 已驗證 |
| 2 | API authentication plan specifies credential storage mechanism, rotation schedul | ✅ 已驗證 |
| 3 | Data format mapping is bidirectional (where applicable) and includes validation  | ✅ 已驗證 |
| 4 | Error handling specification covers all documented error codes; timeout values a | ✅ 已驗證 |
| 5 | Security hardening checklist is 100% complete: TLS version ≥ 1.2 is enforced, AP | ✅ 已驗證 |
| 6 | Zone/conduit crossing has been documented and approved by SAC/STC; firewall rule | ✅ 已驗證 |
| 7 | API integration test plan is complete; authentication, data validation, rate lim | ✅ 已驗證 |

---

## 6. 工時參考

| SK | 估算基準 |
|----|---------|
| SK-D07-007 | | Junior (< 2 yr) | 5–10 person-days | Assumes single API endpoint, straightforward REST/JSON data f |
| SK-D07-007 | | Senior (5+ yr) | 2–5 person-days | Same scope; senior can leverage prior API integration experienc |
| SK-D07-007 | Notes: APIs with complex authentication schemes (OAuth 2.0, certificate-based), multiple data format |

---

## 7. 品質檢查清單

| # | 檢查項目 | 通過條件 |
|---|---------|---------|
| 1 | 輸入完整性 | 所有必要輸入文件已讀取並摘要 |
| 2 | 流程覆蓋 | 1 個工作步驟皆已執行並有產出 |
| 3 | 輸出完整性 | 所有交付物已產出、格式正確、非空白 |
| 4 | 標準合規 | 產出引用的標準版本正確 |
| 5 | 術語一致 | 專案術語、縮寫與 glossary 一致 |
| 6 | 跨步驟一致 | 各步驟產出間無矛盾（如數量、SL等級） |

---

## 8. 人類審核閘門

完成所有工作步驟後，暫停並向使用者提交審核：

```
API 與第三方集成已完成。
📋 執行範圍：1 個工程步驟（SK-D07-007）
📊 交付物清單：
  - Third-Party API Integration Specification: API endpoint, authentication method, data format, rate limits, timeout behavior
  - API Authentication and Credential Management Plan: credential storage, rotation schedule, access control (who can access credentials), audit trail req
  - API Data Format Mapping Document: external API data format → internal system data format, including validation rules and type conversions for both RES
  - Error Handling and Retry Logic Specification: timeout values, retry attempts, exponential backoff, fallback behavior, alert triggers
  - API Security Hardening Checklist: TLS/SSL version verification, certificate pinning (if applicable), API key encryption, data-in-transit encryption, s
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
| Domain | D07 (System Integration) |
| SK 覆蓋 | SK-D07-007 |

---

## 10. Source Traceability

| SK 編號 | 英文名稱 | 中文名稱 | 核心知識 |
|--------|---------|---------|---------|
| SK-D07-007 | Third-Party API Integration | 第三方 API 串接 | Integrate third-party APIs (weather services, market data fe |

<!-- Phase 5 Wave 2 deepened: SK-D07-007 -->