---
name: factory-acceptance-testing
description: >
  工廠驗收測試：FAT 程序撰寫與安全 FAT 測試案例設計。
  MANDATORY TRIGGERS: FAT, 工廠驗收, factory acceptance, 出廠測試,
  factory test, pre-shipment test.
  Use this skill for factory acceptance testing in OT/ICS cybersecurity projects.
---

# 工廠驗收測試 (Factory Acceptance Testing)

整合 2 個 SK，涵蓋 FAT 程序開發與安全測試案例設計。

---

## 0. 初始化

1. 安全功能描述規範 (SFDS) 已完成 (SK-D09-002)
2. FR/SR 映射矩陣已就緒 (SK-D01-007)
3. 端點加固規格已定義 (SK-D01-019)
4. 帳號/存取控制策略已定義 (SK-D01-020)
5. 確認 FAT = 工廠測試 (pre-shipment)，區別於 SAT (site) 和 SIT (integration)

---

## 1. 工作流程

### Step 1: FAT 程序撰寫 (SK-D08-001)

**FAT 文件架構**：

| 章節 | 內容 |
|------|------|
| 1. 範圍 | 受測系統/元件、測試邊界 |
| 2. 測試環境 | 硬體配置、網路拓撲、模擬器 |
| 3. 前置條件 | 系統狀態、資料準備、人員 |
| 4. 測試類別 | 功能、安全、效能、故障恢復 |
| 5. 測試案例 | ID、步驟、預期結果、pass/fail |
| 6. 通過標準 | 整體 pass 門檻 |
| 7. 文件標準 | 紀錄格式、證據要求 |

**步驟**：
1. 從 FR/SR 矩陣提取所有可在工廠驗證的需求
2. 分類為功能測試、安全測試、效能測試、故障恢復測試
3. 撰寫每個測試案例：前置條件 → 步驟 → 預期結果 → pass/fail 判定
4. 定義測試環境需求 (可能需要模擬現場設備)
5. 建立測試執行順序 (dependency-aware)
6. 定義文件化標準：截圖、log、簽核

**⚠️ 避坑**：
- 測試環境缺少模擬器 → 關鍵介面測試被 skip，到 SAT 才發現問題
- Pass/fail 標準模糊 → 客戶與整合商對結果各說各話
- 未列出排除項 → 客戶期望所有功能都在 FAT 完成

### Step 2: 安全 FAT 測試案例設計 (SK-D08-002)

**安全測試類別**：

| 類別 | 測試內容 | 工具 |
|------|----------|------|
| 帳號管理 | RBAC、密碼策略、lockout | 手動 + script |
| 網路安全 | Firewall rules、port scan、VLAN isolation | Nmap, Nessus |
| 加密驗證 | TLS 版本、憑證鏈、cipher suite | Wireshark, OpenSSL |
| 加固驗證 | 不必要服務關閉、預設帳號移除 | CIS-CAT, custom script |
| 日誌/稽核 | 事件記錄完整性、syslog 輸出 | Log parser |
| 惡意程式防護 | AV/EDR 安裝、更新機制 | 產品管理介面 |

**步驟**：
1. 從 SR 清單建立測試案例：每個 SR 至少一個正向 + 一個負向測試
2. 正向測試：驗證安全功能正常運作 (e.g., 正確帳號可登入)
3. 負向測試：驗證安全功能正確拒絕 (e.g., 錯誤密碼被鎖定)
4. 邊界測試：極端情況 (e.g., 密碼長度剛好 = 最低要求)
5. 對應每案例到 SR ID，建立追蹤矩陣
6. 定義證據要求：截圖、scan report、config export

**⚠️ 避坑**：
- 僅測正向案例 → 安全功能「存在」但「不生效」未被發現
- 未測 default password → 出廠即存在已知弱點
- 掃描工具 false positive 未人工確認 → 報告不可信

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | FAT 程序涵蓋所有可工廠驗證的 FR/SR |
| 2 | 每個測試案例含：前置條件、步驟、預期結果、pass/fail |
| 3 | 安全測試含正向 + 負向案例 |
| 4 | 測試案例 ↔ SR ID 追蹤矩陣完整 |
| 5 | 測試環境需求已明確定義 |
| 6 | FAT 排除項已列出並經客戶同意 |
| 7 | 文件符合 Gate 3 delivery checklist 要求 |

---

## 3. 人類審核閘門

```
FAT 程序完成。
📋 範圍：2 個工程步驟 (SK-D08-001, SK-D08-002)
📊 交付物：FAT 程序文件 ({n} 案例)、安全測試案例 ({m} SR 覆蓋)
⚠️ 待確認：{TBD 項目}
👉 請 STC + SAC + 客戶代表審核。
```

---

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D08-001 | FAT Procedure Development | 程序架構、案例撰寫、環境需求、文件標準 |
| SK-D08-002 | FAT Execution (Security) | 安全測試類別、正/負向測試、SR 追蹤 |

<!-- Phase 6: Enhanced 2026-03-19. -->
