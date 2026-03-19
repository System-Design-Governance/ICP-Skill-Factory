---
name: supply-chain-security
description: >
  Manage supply chain security for OT/ICS projects covering vendor security risk assessment,
  SBOM analysis and management, third-party component security verification, and vendor
  security management plan development.
  MANDATORY TRIGGERS: 供應鏈安全, supply chain security, 供應商評估, vendor assessment,
  SBOM, software bill of materials, 第三方元件, third-party component,
  供應商管理, vendor management, 供應商風險, vendor risk, CVE,
  元件驗證, component verification, 軟體物料清單.
  Use this skill for supply chain security, vendor assessment, SBOM, and component
  verification tasks in OT/ICS projects.
---

# 供應鏈安全管理 (Supply Chain Security)

本 Skill 整合 4 個工程技能定義，提供 OT/ICS 供應鏈安全的完整管理流程——從供應商評估到元件驗證到持續管理。

---

## 0. 初始化

1. **供應商清單**：已辨識參與 SuC 交付的所有供應商
2. **採購程序**：已了解組織 ID22 採購管理程序
3. **資產清冊**：已完成 (SK-D01-005)，含第三方元件
4. **CVE 資料庫**：可存取 NIST NVD / 廠商安全公告

---

## 1. 輸入

| 類別 | 輸入 | 來源 |
|------|------|------|
| 供應商 | 供應商/外包商清單 | 專案團隊 |
| 採購 | ID22 採購管理程序 | 組織 QMS |
| 資產 | 資產清冊 (含第三方元件) | SK-D01-005 |
| 標準 | IEC 62443-2-4 SP.01 供應商要求 | 標準文庫 |
| 情資 | CVE/NVD 資料庫 | NIST / 廠商 |

---

## 2. 工作流程

### Step 1: 供應商安全風險評估 (SK-D01-024)

**目標**：評估所有供應商的資安風險態勢。

**操作步驟**：

1. **供應商盤點**：辨識所有供應硬體/軟體/服務的供應商
2. **安全能力評估**：
   - 認證狀態 (ISO 27001, IEC 62443-4-1 等)
   - 安全開發生命週期成熟度
   - 弱點揭露流程
   - 補丁支援承諾

3. **評分** (per ID22 criteria)：
   ```markdown
   | 供應商 | 品質系統 | 交付能力 | 技術能力 | 安全態勢 | 加權總分 | Risk Rating |
   |--------|---------|---------|---------|---------|---------|------------|
   | Vendor A | 8/10 | 7/10 | 9/10 | 6/10 | 7.5 | Medium |
   | Vendor B | 9/10 | 8/10 | 8/10 | 9/10 | 8.5 | Low |
   ```

4. **風險登錄**：High→季度 review, Medium→年度, Low→雙年度
5. **合約安全條款**：為高風險供應商制定額外安全要求
6. **Gate 0 供應鏈風險摘要**：匯入 Gate 0 決策包

**⚠️ 避坑**：COTS-heavy 架構需 product-level 安全分析 (工時 ×1.5)

---

### Step 2: SBOM 分析與管理 (SK-D01-025)

**目標**：蒐集、分析和管理軟體物料清單。

**操作步驟**：

1. **SBOM 蒐集**：向供應商索取 CycloneDX / SPDX 格式 SBOM
2. **SBOM 整合**：
   ```markdown
   | Component | Version | Vendor | Type | Zone | Criticality | SBOM Source |
   |-----------|---------|--------|------|------|-------------|-------------|
   | OpenSSL | 3.0.12 | OSS | Library | All | High | CycloneDX |
   | Node.js | 18.19.0 | OSS | Runtime | Server | Medium | SPDX |
   ```
3. **CVE 比對**：與 NIST NVD 比對已知弱點
4. **授權合規**：檢查 OSS 授權與組織政策相容性
5. **元件生命週期追蹤**：版本歷史、EOL 狀態
6. **持續監控計畫**：定義 CVE 檢查頻率 (至少每季)

**⚠️ 避坑**：Legacy 硬體可能無 SBOM→需手動元件辨識 (工時 ×2)；不是所有供應商都能提供 SBOM

---

### Step 3: 第三方元件安全驗證 (SK-D01-026)

**目標**：在整合前驗證第三方元件的安全性。

**操作步驟**：

1. **弱點掃描**：每個元件執行 CVE 掃描
2. **安全組態審查**：加密、認證、logging 能力
3. **合規評估**：元件安全屬性 vs 專案要求
4. **核准分類**：
   - **Approved**：符合所有要求
   - **Conditional**：有已知弱點但有 patch timeline
   - **Rejected**：不符合要求，需替代方案
5. **再驗證排程**：穩定元件年度，重大更新後立即

**⚠️ 避坑**：別忘了 firmware 也需要驗證 (不只軟體)；供應商 EOL 宣告需立即觸發再評估

---

### Step 4: 供應商安全管理計畫 (SK-D01-031)

**目標**：建立供應商安全管理的長期治理框架 (per ID05)。

**操作步驟**：

1. **供應商分類框架**：依 criticality + risk 分 ≥3 級
2. **評估流程**：定義評估權限、時程、核准鏈
3. **持續監控**：供應商績效 KPIs (安全合規)
4. **第三方事件回應**：供應商安全事件的通報和處理流程
5. **與專案 Security Management Plan (SK-D01-029) 整合**

**⚠️ 避坑**：計畫不能只做一次→需定義年度 review 週期；供應商停業/EOL 需要觸發再評估

---

## 3. 輸出

| # | 交付物 | 步驟 |
|---|--------|------|
| 1 | Vendor Security Risk Assessment Report | 1 |
| 2 | Vendor Risk Register | 1 |
| 3 | Approved Vendor List | 1 |
| 4 | Vendor Security Requirements Spec | 1 |
| 5 | Consolidated SBOM | 2 |
| 6 | CVE Matching Report | 2 |
| 7 | License Compliance Inventory | 2 |
| 8 | Component Verification Reports | 3 |
| 9 | Approved Components List | 3 |
| 10 | Vendor Security Management Plan | 4 |
| 11 | Gate 0 Supply Chain Risk Summary | 1 |

---

## 4. 驗收標準

| # | 項目 | 條件 |
|---|------|------|
| 1 | 供應商覆蓋 | 100% 供應商有安全評估+風險分級 |
| 2 | 評分完成 | 加權評分 per ID22 criteria |
| 3 | SBOM 覆蓋 | 100% 軟體 + 80%+ 硬體元件有 SBOM |
| 4 | CVE 比對 | 所有 Critical/High CVE 已辨識+文件化 |
| 5 | 授權合規 | 無未核准的 OSS 授權 |
| 6 | 元件核准 | 每個元件有 Approved/Conditional/Rejected |
| 7 | 管理計畫 | ≥3 級供應商分類+review 排程 |
| 8 | Gate 0 | 供應鏈風險摘要已交付 |

---

## 5. 人類審核閘門

```
供應鏈安全管理已完成。
📋 範圍：供應商評估 + SBOM + 元件驗證 + 管理計畫
📊 數據：供應商 {v} 家 (H:{h}/M:{m}/L:{l}) | SBOM 元件 {c} 個 | CVE {cve} 個
⚠️ 待確認：{High-risk 供應商/Conditional 元件/缺 SBOM 的 legacy 設備}
👉 請 SAC 審核 PASS / FAIL / PASS with Conditions。
```

---

## 6. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D01-024 | Vendor Security Risk Assessment | 供應商安全能力評估、ID22 評分、風險登錄 |
| SK-D01-025 | SBOM Analysis and Management | CycloneDX/SPDX、CVE 比對、授權合規 |
| SK-D01-026 | Third-Party Component Verification | 元件弱掃、核准分類、再驗證排程 |
| SK-D01-031 | Vendor Security Management Plan | 供應商分類、持續監控、第三方 IR |

<!-- Phase 6: Deep enhancement from 4 SK definitions. Enhanced 2026-03-19. -->
