---
name: api-integration
description: >
  API 與第三方系統整合：REST/SOAP API 設計、認證、錯誤處理、速率限制。
  MANDATORY TRIGGERS: API, 第三方整合, third-party integration, REST, API 整合,
  web service, API integration.
  Use this skill for third-party API integration tasks in OT/ICS projects.
---

# API 與第三方整合 (API Integration)

整合 1 個 SK，涵蓋第三方 API 整合設計與實作。

---

## 0. 初始化

1. 待整合的第三方服務已識別 (天氣、市場、電網調度、雲平台)
2. API 文件 / Swagger spec 已取得
3. 安全策略已確定 (認證方式、資料分級)
4. 網路連線方案已確認 (DMZ、proxy、VPN)

---

## 1. 工作流程

### Step 1: 第三方 API 整合設計 (SK-D07-007)

**整合架構模式**：

| 模式 | 適用場景 | 優點 | 風險 |
|------|----------|------|------|
| Direct Call | 低頻、非關鍵 | 簡單 | 耦合高 |
| API Gateway | 多 API 聚合 | 統一認證/限流 | 增加延遲 |
| Message Queue | 非同步、高可靠 | 解耦、重試 | 複雜度高 |
| Polling + Cache | 外部限流嚴格 | 減少呼叫數 | 資料延遲 |

**認證方式比較**：

| 方式 | 安全等級 | 適用場景 |
|------|----------|----------|
| API Key | 低 | 公開資料 (天氣 API) |
| OAuth 2.0 | 中-高 | 雲平台、SaaS |
| mTLS | 高 | OT-IT 邊界、關鍵資料 |
| HMAC Signature | 中 | 交易/市場資料 |

**步驟**：
1. 分析 API spec：endpoints, rate limits, pagination, error codes
2. 設計整合架構 (選擇上述模式)
3. 實作認證流程 (token 更新、密鑰輪替)
4. 設計資料映射：API 回應 → 內部資料模型
5. 實作錯誤處理：retry (exponential backoff)、circuit breaker、fallback
6. 設定 rate limiting：遵守第三方限制、內部保護
7. 實作日誌與監控：呼叫次數、延遲、錯誤率
8. 安全設計：API key 存於 vault (非 source code)、傳輸加密、輸入驗證

**⚠️ 避坑**：
- API key 硬編碼在 source code → 洩漏至 Git repo
- 未實作 circuit breaker → 第三方掛掉拖垮整個系統
- 未處理 rate limit 429 回應 → 被封鎖 IP
- 未做輸入驗證 → API injection 攻擊風險
- 時區處理不一致 → 天氣/市場資料對不上時間

**測試策略**：

| 測試類型 | 內容 |
|----------|------|
| Contract Test | 驗證 API 回應符合 spec |
| Integration Test | 實際呼叫 sandbox/staging API |
| Failure Test | 模擬 timeout、500、rate limit |
| Security Test | 無效 token、過期 token、injection |
| Performance Test | 並行呼叫數、延遲分布 |

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | 所有 API endpoints 已整合並通過 contract test |
| 2 | 認證 token 自動更新，密鑰存於 vault (非 source code) |
| 3 | 錯誤處理覆蓋 timeout、5xx、rate limit (429) |
| 4 | Circuit breaker 已配置並測試 |
| 5 | 監控儀表板含呼叫量、錯誤率、P95 延遲 |
| 6 | 安全測試通過：無 injection、token 洩漏風險 |

---

## 3. 人類審核閘門

```
API 整合完成。
📋 範圍：1 個工程步驟 (SK-D07-007)
📊 交付物：整合設計文件、API 映射表、錯誤處理規範、監控配置
⚠️ 待確認：{TBD 項目}
👉 請 SYS + SEC 審核。
```

---

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D07-007 | Third-Party API Integration | 架構模式、認證、錯誤處理、rate limit、安全 |

<!-- Phase 6: Enhanced 2026-03-19. -->
