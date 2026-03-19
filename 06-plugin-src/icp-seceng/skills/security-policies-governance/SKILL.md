---
name: security-policies-governance
description: >
  Develop security policy framework for OT/ICS environments covering security policies and
  procedures plan (account/hardening/backup/AV/patch/monitoring), data classification policy,
  and security solution integration planning.
  MANDATORY TRIGGERS: 安全政策, security policy, 安全程序, security procedures,
  資料分類, data classification, 安全整合計畫, security integration plan,
  政策撰寫, policy development, 安全管理計畫, security management plan,
  政策框架, policy framework, 安全治理, security governance.
  Use this skill for security policy development and governance planning in OT/ICS projects.
---

# 安全政策與治理 (Security Policies & Governance)

本 Skill 整合 3 個工程技能定義，建立 OT/ICS 安全政策框架——從安全程序計畫到資料分類政策到安全解決方案整合規劃。

---

## 0. 初始化

1. **組織 ISMS 框架**：已了解組織既有的資安管理體系
2. **Zone/Conduit 架構**：已完成 (SK-D01-001)
3. **風險評估**：TRA 產出可用 (SK-D01-006/007)
4. **ID07 範本**：Security Policies and Procedures Plan exemplar 可參考

---

## 1. 輸入

| 類別 | 輸入 | 來源 |
|------|------|------|
| 架構 | Zone/Conduit + SL-T | SK-D01-001, SK-D01-010 |
| 風險 | TRA/DTRA 風險登錄冊 | SK-D01-006/007 |
| 範本 | ID07 安全政策程序計畫 exemplar | source-documents/ |
| 組織 | ISMS 政策、ISO 27001 體系 | 組織文件 |
| 法規 | GDPR/HIPAA/PCI-DSS 要求 | 適用法規 |

---

## 2. 工作流程

### Step 1: 安全政策與程序計畫 (SK-D01-030)

**目標**：建立 6 大安全政策領域的完整程序計畫 (per ID07 format)。

**6 大政策領域**：

| § | 領域 | 涵蓋範圍 | 對應實施 SK |
|---|------|---------|-----------|
| §4.0 | 帳號管理 | RBAC、AD/GPO、密碼政策、帳號生命週期 | SK-D01-020 |
| §5.0 | 系統加固 | CIS Benchmark、實體/邏輯/軟體加固 | SK-D01-019 |
| §6.0 | 備份還原 | 備份目標、方法、排程、保留、復原 | SK-D01-022 |
| §7.0 | 惡意程式防護 | AV 部署、USB 管控、更新機制 | SK-D01-023 |
| §8.0 | 補丁管理 | 補丁取得、評估、測試、部署、緊急流程 | SK-D01-021 |
| §9.0 | 安全監控 | SIEM、告警、事件回應、日誌保留 | SK-D01-014~018 |

**政策撰寫原則**：
- 每項政策包含**具體可量化要求** (非模糊指令如「確保適當安全」)
- 明確連結 IEC 62443-3-3 FR/SR
- 考慮 OT 操作限制 (availability > confidentiality)
- 定義例外審批流程和權限層級
- 交叉引用對應的實施 SK

**⚠️ 避坑**：
- 政策太嚴與 OT 操作實務脫節 → 需與 OT 操作員和 SYS 驗證
- 政策沒有執行機制 → 每項政策要指定負責角色和檢查頻率
- 直接照抄 IT 政策 → OT 有其特殊限制 (legacy 設備、availability 優先)

---

### Step 2: 資料分類政策 (SK-D01-033)

**目標**：定義資料分類等級、標記要求和處理規則。

**分類等級** (≥3 級)：

| 等級 | 範例 | 加密 | 存取控制 | 保留 | 銷毀 |
|------|------|------|---------|------|------|
| Public | 公開技術文件 | — | — | 無限制 | 一般刪除 |
| Internal | 營運數據、設定檔 | Transit 加密 | RBAC | 依政策 | 安全刪除 |
| Confidential | 安全評估、弱掃報告 | 全程加密 | Need-to-know | 依法規 | 驗證銷毀 |
| Restricted | 密碼、金鑰、SIS 設定 | 全程加密+HSM | 雙因子+審核 | 最小必要 | 多次覆寫+驗證 |

**資料類型對照** (per ID07/ID23)：

| 資料類型 | 分類 | OT 特殊考量 |
|---------|------|-----------|
| 法規/合規文件 | Confidential | 稽核時需可存取 |
| 營運/過程數據 | Internal | 即時性優先於機密性 |
| 安全組態 | Restricted | 變更需 dual sign-off |
| 稽核日誌 | Confidential | 不可竄改，保留≥1年 |
| 備份資料 | 同原始分類 | 備份媒體需同等保護 |

**⚠️ 避坑**：
- 分類過細 → 執行困難；分類過粗 → 保護不足
- 忘記 OT 即時數據 → 過程控制數據的 availability 優先於 confidentiality

---

### Step 3: 安全解決方案整合計畫 (SK-D01-034)

**目標**：規劃如何將個別安全控制整合為一致的安全架構。

**整合範圍**：
- Firewall / Network segmentation
- SIEM / Log aggregation
- Endpoint protection (AV/EDR)
- Access control (AD/RBAC)
- Backup / DR
- VPN / Remote access

**整合順序規劃**：
```
Phase 1: 基礎 (FW + Network segmentation + Logging)
    ↓
Phase 2: 偵測 (SIEM + Alarm rules + Monitoring)
    ↓
Phase 3: 防護 (AV/EDR + Access control + MFA)
    ↓
Phase 4: 韌性 (Backup/DR + Remote access + IR)
```

**依賴矩陣**：功能、操作、時間依賴的交叉分析

**Rollback 程序**：每個 phase 有可測試的 rollback 路徑

**⚠️ 避坑**：
- 不考慮控制間的依賴 → SIEM 需在 logging 啟用後才有效
- 沒有 rollback 計畫 → 整合失敗時可能影響 OT 營運
- Phasing 不合理 → 基礎控制 (FW/logging) 必須先於偵測控制 (SIEM)

---

## 3. 輸出

| # | 交付物 | 步驟 |
|---|--------|------|
| 1 | Security Policies and Procedures Plan (§4-§9) | 1 |
| 2 | RACI Matrix (政策職責) | 1 |
| 3 | Policy Implementation Roadmap | 1 |
| 4 | Data Classification Policy | 2 |
| 5 | Data Handling Guidelines | 2 |
| 6 | Security Solution Integration Plan | 3 |
| 7 | Integration Dependency Matrix | 3 |
| 8 | Rollback Procedures (per phase) | 3 |
| 9 | Integration Testing Strategy | 3 |

---

## 4. 驗收標準

| # | 項目 | 條件 |
|---|------|------|
| 1 | 政策覆蓋 | 6 大領域 (§4-§9) 全部涵蓋 |
| 2 | 可量化 | 每項政策有具體可量化要求 (非模糊指令) |
| 3 | FR/SR 連結 | 政策連結 IEC 62443-3-3 FR/SR |
| 4 | OT 可行 | 已考慮 OT 操作限制 |
| 5 | 資料分類 | ≥3 等級，含處理/保留/銷毀規則 |
| 6 | 整合順序 | 有依賴分析+phasing+rollback |
| 7 | 職責 | RACI 定義清楚 |

---

## 5. 人類審核閘門

```
安全政策與治理文件已完成。
📋 範圍：安全程序計畫 (§4-§9) + 資料分類 + 安全整合計畫
📊 政策數：{n} 項 | 分類等級：{c} 級 | 整合 Phase：{p} 個
⚠️ 待確認：{政策與 OT 操作衝突項/例外}
👉 請 SAC + GOV-Lead 審核。
```

---

## 6. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D01-030 | Security Policies & Procedures Plan | 6 大政策領域 (§4-§9)、RACI、OT 適配 |
| SK-D01-033 | Data Classification Policy | 分類等級、標記、處理規則、OT 數據特殊性 |
| SK-D01-034 | Security Solution Integration Plan | 整合排序、依賴矩陣、Rollback、測試策略 |

<!-- Phase 6: Deep enhancement from 3 SK definitions. Enhanced 2026-03-19. -->
