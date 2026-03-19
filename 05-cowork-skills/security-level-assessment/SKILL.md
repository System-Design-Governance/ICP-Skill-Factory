---
name: security-level-assessment
description: >
  Assess and assign Security Level Targets (SL-T) to each zone and conduit in OT/ICS
  architecture per IEC 62443-3-3. Covers SL-T methodology, stakeholder alignment,
  SL Decision Lifecycle, and SL-T baseline documentation.
  MANDATORY TRIGGERS: 安全等級, security level, SL-T, SL target, 安全等級評估,
  security level assessment, SL 指定, SL assignment, 安全等級目標,
  SL decision, zone security level, SL-1, SL-2, SL-3, SL-4.
  Use this skill for SL-T assessment and assignment in IEC 62443 OT/ICS projects.
---

# 安全等級目標評估 (Security Level Target Assessment)

本 Skill 評估並指定 IEC 62443-3-3 SL-T 至每個 Zone/Conduit。SL-T 決定每個 Zone 所需的安全能力和控制深度。

---

## 0. 初始化

1. **Zone/Conduit 架構**：已完成 (SK-D01-001)
2. **風險評估**：初步 TRA (SK-D01-006) 產出可用
3. **IEC 62443-3-3**：標準文件可參考

---

## 1. 輸入

| 類別 | 輸入 | 來源 |
|------|------|------|
| 架構 | Zone/Conduit 架構圖 | SK-D01-001 |
| 風險 | 初步 TRA (風險等級 per zone) | SK-D01-006 |
| 需求 | 客戶安全需求 / 法規要求 | SOW / 合約 |
| 標準 | FR/SR 對照表 | Plugin 共用 references/ |

---

## 2. 工作流程

### Step 1: SL-T 評估方法論 (SK-D01-010)

**SL-T 定義速查**：

| SL | 防護目標 | 典型 Zone | 控制深度 |
|----|---------|----------|---------|
| SL-0 | 無特定安全要求 | 非關鍵顯示 | — |
| SL-1 | 防止意外違規 | Office IT | 基本 AC + logging |
| SL-2 | 防止簡單蓄意攻擊 | Server Room, 一般 OT | AC + monitoring + encryption |
| SL-3 | 防止精密蓄意攻擊 | 關鍵 SCADA, EMS | 深度 AC + IDS + MFA + encryption |
| SL-4 | 防止國家級攻擊 | 核設施, 關鍵基礎設施 | 全面控制 + 持續監控 |

**操作步驟**：

1. **風險驅動評估**：每個 Zone 的 SL-T 由以下因素決定
   - 資產 criticality (High/Medium/Low)
   - 威脅可能性 (from TRA)
   - 後果嚴重度 (Safety / Business / Operational / Compliance)
   - 法規要求 (客戶指定 or 產業標準)

2. **SL-T 指定模板**：
   ```markdown
   | Zone ID | Zone 名稱 | Criticality | 威脅等級 | 後果 | 法規 | SL-T | 理由 |
   |---------|----------|------------|---------|------|------|------|------|
   | Z-01 | DMZ | High | High | 邊界突破→全域影響 | — | SL-2 | 邊界防護需防蓄意攻擊 |
   | Z-02 | Office IT | Medium | Medium | 資料外洩 | — | SL-1 | 一般辦公，無 safety 影響 |
   | Z-03 | OT Control | Critical | High | 控制中斷→safety | IEC 62443 | SL-3 | 關鍵控制，需防精密攻擊 |
   | Z-04 | SIS | Critical | Medium | Safety function 失效 | IEC 61511 | SL-3 | 安全系統，需最高防護 |
   ```

3. **SL Decision Lifecycle** (GOV-SD)：
   ```
   Initial Assignment → Stakeholder Verified → Risk-Updated → Finalized
   ```
   - 每階段需 stakeholder 簽核
   - SL-T 升級/降級需文件化理由+核准

4. **Stakeholder Alignment Workshop**：
   - 呈現每個 Zone 的 SL-T 建議
   - 討論 cost-benefit (高 SL = 更多控制 = 更高成本)
   - 取得 SAC + Zone Owner 共識

5. **產出 SL-T Baseline Document**

**⚠️ 避坑**：
- SL-T 不是隨意指定——每個需有明確理由 (risk + consequence)
- 不要所有 Zone 都給 SL-3——over-engineering 浪費成本
- SL-T 升級容易降級難——需在初始就審慎評估
- 相鄰 Zone SL 差異 ≥2 時需在 Conduit 加入額外安全機制

---

## 3. 輸出

| # | 交付物 | 格式 |
|---|--------|------|
| 1 | SL-T Baseline Document | Markdown |
| 2 | SL-T Assignment Matrix (Zone→SL) | Markdown |
| 3 | SL-T Justification (per zone) | Markdown |
| 4 | SL Decision Lifecycle Audit Trail | Markdown |
| 5 | Stakeholder Sign-off Records | Markdown |

---

## 4. 驗收標準

| # | 項目 | 條件 |
|---|------|------|
| 1 | 覆蓋 | 每個 Zone 有指定 SL-T (0-4) |
| 2 | 理由 | 每個 SL-T 有明確理由 (risk + consequence + 法規) |
| 3 | Lifecycle | SL Decision Lifecycle 已記錄 (Initial→Verified→Final) |
| 4 | 簽核 | SAC + Zone Owner 已簽核 |
| 5 | IEC 62443 對齊 | SL-T 選擇依 IEC 62443-3-3 指引 |
| 6 | 相鄰差異 | SL 差異 ≥2 的 Conduit 有額外安全機制 |

---

## 5. 工時參考

| 角色 | Junior | Senior | 備註 |
|------|--------|--------|------|
| SAC | 20 hr | 10 hr | Lead assessment |
| Risk Manager | 8 hr | 4 hr | Risk input |
| Zone Owner | 12 hr | 8 hr | Per zone |
| 合計 | ~46 hr | ~26 hr | 依 Zone 數量 |

---

## 6. 人類審核閘門

```
SL-T 評估已完成。
📋 Zone 數：{n} 個
📊 SL-T 分布：SL-1: {s1} | SL-2: {s2} | SL-3: {s3} | SL-4: {s4}
⚠️ 待確認：{SL-T 爭議/成本影響/相鄰 Zone 差異}
👉 請 SAC + Zone Owner 審核 SL-T Baseline。
```

---

## 7. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D01-010 | Security Level Target Assessment | SL-T 方法論、SL Decision Lifecycle、Stakeholder alignment |

<!-- Phase 6: Deep enhancement from 1 SK definition. Enhanced 2026-03-19. -->
