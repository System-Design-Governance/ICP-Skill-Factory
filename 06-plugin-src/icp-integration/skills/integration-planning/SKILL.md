---
name: integration-planning
description: >
  整合規劃：建立介面整合矩陣與系統整合測試計畫。
  MANDATORY TRIGGERS: 整合規劃, integration planning, 介面矩陣, interface matrix, SIT,
  整合測試, system integration test, integration matrix.
  Use this skill for integration planning tasks in OT/ICS/SCADA cybersecurity and energy infrastructure projects.
---

# 整合規劃 (Integration Planning)

整合 2 個 SK，涵蓋介面整合矩陣建立與系統整合測試計畫。

---

## 0. 初始化

1. 專案功能架構與系統分解已完成 (SK-D01-002, SK-D01-011)
2. Zone/Conduit 架構已定義 (SK-D01-001)
3. 網路拓撲圖已產出或同步進行中 (SK-D02-001)
4. 資料流圖已產出 (SK-D02-004)

---

## 1. 工作流程

### Step 1: 介面整合矩陣建立 (SK-D07-001)

**矩陣欄位定義**：

| 欄位 | 說明 | 範例 |
|------|------|------|
| Interface ID | 唯一識別碼 | INT-SCADA-RTU-01 |
| Source System | 來源系統 | SCADA Master |
| Destination System | 目標系統 | RTU-001 |
| Protocol | 通訊協定 | IEC 60870-5-104 |
| Direction | 方向 | Bidirectional |
| Data Payload | 資料描述 | Real-time measurements, 500 B/s |
| Latency Req | 延遲需求 | < 500 ms |
| Availability | 可用性 | 99.5% |
| Source Zone | 來源安全區 | Zone-L3 (Control) |
| Dest Zone | 目標安全區 | Zone-L1 (Field) |
| Auth Method | 認證方式 | X.509 certificates |
| Encryption | 加密需求 | TLS 1.2+ |
| Conduit Ref | 管道參考 | CDT-L3-L1-01 |

**步驟**：
1. 從功能架構識別所有子系統對 (SCADA↔RTU, EMS↔DERMS, SCADA↔Historian 等)
2. 逐一填寫矩陣欄位：協定、延遲、頻寬、安全區跨越
3. 標記所有跨安全區介面，對應 SK-D01-001 conduit 表
4. 對跨區介面指定認證/加密機制
5. 執行相容性分析：識別協定衝突或資料模型不匹配
6. 產出系統對系統連接圖 (節點=系統, 邊=介面)

**⚠️ 避坑**：
- 遺漏 legacy 系統介面 → 上線後發現不相容，需緊急加 protocol gateway
- 未記錄「無加密」介面的補償控制 → 審計不通過
- 延遲需求與加密開銷衝突未事先分析 → 即時控制迴路失效

### Step 2: 系統整合測試計畫 (SK-D07-002)

**測試計畫架構**：

| 區段 | 內容 |
|------|------|
| 範圍定義 | 測試涵蓋的子系統與介面清單 |
| 測試環境 | 硬體/軟體/網路配置、模擬器需求 |
| 測試案例 | 功能測試、效能測試、安全測試、故障切換測試 |
| 通過標準 | 每案例的 pass/fail 判定條件 |
| 時程與資源 | 人員、設備、場地、天數 |
| 風險與應變 | 測試失敗的升級與重測程序 |

**步驟**：
1. 從介面矩陣提取所有待測介面
2. 為每個介面設計至少：正常流程、異常流程、邊界條件 各一案例
3. 設計跨系統端對端場景 (e.g., 事件從 field device → RTU → SCADA → Historian 全程驗證)
4. 定義效能基準：延遲、吞吐量、並行連線數
5. 定義安全測試：認證失敗、未授權存取、加密降級偵測
6. 建立測試追蹤矩陣：測試案例 ↔ 介面 ID ↔ 需求 ID

**⚠️ 避坑**：
- 測試環境與生產環境差異過大 → SIT 結果不可信
- 未涵蓋故障切換場景 → redundancy 設計未被驗證
- 安全測試僅測「應通過」場景，未測「應拒絕」→ 漏洞未被發現

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | 資料流圖中每個子系統間交換均有對應矩陣條目 |
| 2 | 每條目含：來源、目標、協定、延遲、安全分類 |
| 3 | 100% 跨安全區介面已標記並連結 conduit 設計 |
| 4 | 跨區介面已指定認證/加密方法並說明理由 |
| 5 | Legacy 介面已識別並記錄安全限制與補償控制 |
| 6 | SIT 計畫涵蓋功能、效能、安全、故障切換測試 |
| 7 | 測試追蹤矩陣完整：案例↔介面↔需求 |
| 8 | SYS + Security Engineer + Network Engineer 已審核簽核 |

---

## 3. 人類審核閘門

```
整合規劃完成。
📋 範圍：2 個工程步驟 (SK-D07-001, SK-D07-002)
📊 交付物：介面整合矩陣 ({n} 筆介面)、SIT 計畫 ({m} 筆測試案例)
⚠️ 待確認：{TBD 項目}
👉 請 SYS + SEC + NET 審核，確認 PASS / FAIL / PASS with Conditions。
```

---

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D07-001 | Interface Integration Matrix | 介面識別、協定映射、安全區跨越、相容性分析 |
| SK-D07-002 | System Integration Test Plan | 測試架構、案例設計、效能基準、追蹤矩陣 |

<!-- Phase 6: Enhanced 2026-03-19. -->
