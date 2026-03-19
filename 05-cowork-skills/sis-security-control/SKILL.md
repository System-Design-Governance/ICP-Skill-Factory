---
name: sis-security-control
description: >
  Design and implement cybersecurity controls for Safety Instrumented Systems (SIS) that
  enforce IEC 62443 security while preserving SIL certification and IEC 61511 functional safety.
  MANDATORY TRIGGERS: SIS, safety instrumented system, 安全儀控, SIL, 安全完整性,
  safety integrity level, SIS 安全, SIS security, 安全系統隔離,
  safety system isolation, 功能安全, functional safety, IEC 61511,
  安全控制系統, safety control system, SIS 網路隔離.
  Use this skill when cybersecurity controls must coexist with functional safety requirements.
---

# SIS 安全控制 (Safety Instrumented System Security Controls)

本 Skill 處理 OT/ICS 環境中安全控制與功能安全的特殊衝突域——在實施 IEC 62443 安全要求的同時，確保不影響 IEC 61511 安全系統的 SIL 認證和功能安全保障。

---

## 0. 初始化

1. **SIS 識別**：資產清冊中已標記 SIS 設備
2. **Zone/Conduit**：SIS 已被指定為獨立高 SL Zone
3. **功能安全工程師**：已指定並可參與 dual sign-off
4. **SIL 認證**：現有 SIL 認證文件可參考

---

## 1. 輸入

| 類別 | 輸入 | 來源 |
|------|------|------|
| 資產 | SIS 設備清冊 | SK-D01-005 |
| 架構 | Zone/Conduit (SIS Zone) | SK-D01-001 |
| 安全 | SL-T for SIS Zone | SK-D01-010 |
| 功能安全 | SIL 認證文件 | 功能安全團隊 |
| 標準 | IEC 61511 Annex B | 標準文庫 |

---

## 2. 工作流程

### Step 1: SIS 安全控制設計 (SK-D01-027)

**核心衝突**：安全措施可能影響 safety 系統回應時間、可用性或測試程序。

**操作步驟**：

1. **SIS 網路隔離設計**：

| 隔離機制 | 適用場景 | 優點 | 限制 |
|---------|---------|------|------|
| Air Gap | 最高 SIL | 完全隔離 | 無法遠端監控 |
| DMZ + App Gateway | SIL-2/3 | 可監控+隔離 | 需驗證延遲 |
| Dedicated Firewall | SIL-1/2 | 靈活 | 需嚴格規則管理 |

2. **SIS 存取控制**：
   - 僅允許透過定義的認證路徑進行管理存取
   - **不得**影響手動安全覆寫 (manual safety override)
   - 測試方式：模擬認證失敗→驗證手動覆寫仍可用

3. **SIS Conduit 規格**：
   ```markdown
   | Conduit | 來源 | 目標 | 協定 | 延遲上限 | 可靠性 | 安全措施 |
   |---------|------|------|------|---------|--------|---------|
   | C-SIS-01 | SIS Zone | DCS Zone | OPC UA | <100ms | 99.99% | App Gateway + 加密 |
   | C-SIS-02 | SIS Zone | HMI | Modbus TCP | <50ms | 99.99% | Dedicated FW |
   ```
   **關鍵**：每條 Conduit 需文件化延遲和可靠性保證，並驗證安全控制不會降低這些指標。

4. **SIS 變更管理程序**：
   - **Dual Sign-off**：每個 SIS 安全控制變更需 Security Architect + Functional Safety Engineer 雙簽
   - SIL 再驗證觸發條件：安全控制變更是否影響 safety function
   - 需 PtW (Permit to Work) 核准

5. **Security-Safety 衝突解決**：
   ```markdown
   | 衝突 ID | 安全要求 | Safety 要求 | 解決方案 | 取捨 | 核准人 |
   |---------|---------|-----------|---------|------|--------|
   | SC-001 | 加密 SIS↔DCS | <50ms 延遲 | 硬體加速加密 | 成本增加 | PM+SAC+FSE |
   | SC-002 | 強制 MFA 登入 | 緊急手動覆寫 | MFA bypass for safety override | 安全降級 | Engineering Mgmt |
   ```

6. **SIS 資安評估報告**：
   - IEC 62443 安全要求→SIS 控制映射
   - SIL 認證不受影響的確認聲明
   - 功能安全工程師書面確認

**⚠️ 避坑**：
- **絕對不要**在 SIS 上部署可能影響 real-time 回應的安全控制（如 deep packet inspection on safety bus）
- 加密可能增加延遲——需硬體加速或驗證延遲在 tolerance 內
- SIS firmware 更新需 SIL 再驗證——不能像一般 OT 設備一樣 patch
- 每個 SIS 安全控制決策都需 FSE 書面確認——口頭同意不夠
- 既有 SIL 認證系統的安全升級工時可能是新建的 1.5-2 倍

---

## 3. 輸出

| # | 交付物 |
|---|--------|
| 1 | SIS Security Architecture Specification |
| 2 | SIS Network Isolation Design |
| 3 | SIS Conduit Specification (含延遲/可靠性保證) |
| 4 | SIS Change Management Procedure (dual sign-off) |
| 5 | Security-Safety Conflict Resolution Log |
| 6 | SIS Cybersecurity Assessment Report |
| 7 | Functional Safety Engineer 書面確認 |

---

## 4. 驗收標準

| # | 項目 | 條件 |
|---|------|------|
| 1 | SIS 隔離 | SIS 為獨立高 SL Zone，與 non-safety 網路有明確隔離 |
| 2 | 存取控制 | 管理存取僅透過認證路徑，手動覆寫不受影響 (已測試) |
| 3 | Conduit 保證 | 延遲/可靠性指標已文件化，安全控制不降低指標 |
| 4 | Dual Sign-off | 變更管理需 SAC + FSE 雙簽 |
| 5 | 衝突記錄 | ≥1 衝突已辨識 (如有)，含解決方案+核准 |
| 6 | SIL 確認 | FSE 已書面確認 SIL 認證不受影響 |

---

## 5. 工時參考

| 場景 | Junior | Senior | 備註 |
|------|--------|--------|------|
| Greenfield SIS | 12-18 pd | 8-12 pd | 含衝突分析+雙簽流程 |
| 既有 SIL 系統升級 | 18-27 pd | 12-18 pd | ×1.5 due to SIL re-validation |

---

## 6. 人類審核閘門

```
SIS 安全控制已完成。
📋 SIS 設備數：{n} 台 | 隔離方式：{type}
📊 衝突：{c} 個已辨識+已解決 | Conduit 延遲驗證：{pass/fail}
⚠️ 關鍵：FSE 書面確認 SIL 認證不受影響？{是/否}
👉 請 SAC + FSE 審核 PASS / FAIL / PASS with Conditions。
```

---

## 7. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D01-027 | SIS Security Control Implementation | SIS 隔離、安全-安全衝突、dual sign-off、SIL 保護 |

<!-- Phase 6: Deep enhancement from 1 SK definition. Enhanced 2026-03-19. -->
