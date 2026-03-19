---
name: hmi-alarm-design
description: >
  Design HMI screens following ISA-101 standards and alarm hierarchy systems
  following ISA-18.2 with alarm rationalization.
  MANDATORY TRIGGERS: HMI, 人機介面, 畫面設計, screen design, 告警, alarm,
  告警層級, alarm hierarchy, ISA-101, ISA-18.2, alarm rationalization,
  告警合理化, color coding, 色彩規範, screen hierarchy, 畫面層級.
  Use this skill for HMI screen design and alarm management system design.
---

# HMI 與告警設計 (HMI & Alarm Design)

整合 2 個 SK，涵蓋 HMI 畫面設計與告警層級管理。

---

## 0. 初始化

1. SCADA 點位清單已完成
2. 操作流程已確認 (SOP)
3. 使用者角色已定義 (operator/engineer/manager)

---

## 1. 工作流程

### Step 1: HMI 畫面設計 (SK-D05-005)

**畫面層級 (ISA-101)**：

| Level | 名稱 | 內容 | 操作 |
|-------|------|------|------|
| L1 | Overview | 全廠/全系統總覽 | KPI、關鍵狀態 |
| L2 | Area | 區域/子系統 | 設備群組操作 |
| L3 | Detail | 單一設備 | 參數/控制 |
| L4 | Diagnostic | 診斷/趨勢 | 歷史、波形 |

**色彩規範**：

| 顏色 | 用途 | 說明 |
|------|------|------|
| 灰色 | 背景/靜態元件 | 降低視覺疲勞 |
| 綠色 | 正常/運轉中 | 設備正常狀態 |
| 紅色 | 跳脫/停止/告警 | 需注意 |
| 黃色 | 警告/手動模式 | 非正常但非緊急 |
| 藍色 | 資訊/選擇 | 輔助資訊 |
| 動畫閃爍 | 僅限未確認告警 | 避免過度使用 |

**步驟**：定義畫面層級架構 → 設計 L1 Overview (不超過 5 個 KPI) → 設計 L2/L3 模板 → 套用色彩規範 → Navigation 設計 (3 click rule) → 操作員 review

**⚠️ 避坑**：色彩過多造成「聖誕樹效應」；避免在正常狀態使用鮮豔色彩

### Step 2: 告警層級設計 (SK-D05-006)

**ISA-18.2 告警分級**：

| 等級 | 回應時間 | 後果 | 範例 |
|------|---------|------|------|
| Critical | <5 min | 人員安全/設備損壞 | 變壓器過溫跳脫 |
| High | <10 min | 製程中斷 | 饋線過電流 |
| Medium | <30 min | 效能降低 | 電壓偏移 |
| Low | <60 min | 維護提醒 | 設備預防保養 |

**告警合理化**：

```
每個告警必須回答：
1. 告警的原因是什麼？
2. 操作員需要做什麼？
3. 多少時間內必須回應？
4. 不回應的後果？
5. 是否為獨立告警 (非重複/非衍生)？

目標: ≤10 告警/操作員/10min (ISA-18.2 benchmark)
```

**步驟**：從點位清單匯出所有告警 → 分級 (Critical/High/Medium/Low) → 合理化審查 (消除 nuisance alarm) → 設定 shelving/suppression 規則 → KPI 監控 (alarm rate)

**⚠️ 避坑**：告警氾濫 (alarm flood) 導致操作員忽視；standing alarm 必須處理或抑制

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | 畫面層級符合 ISA-101 |
| 2 | 3-click rule 可達任何設備 |
| 3 | 色彩規範統一且文件化 |
| 4 | 告警分級符合 ISA-18.2 |
| 5 | Alarm rate ≤10/operator/10min |
| 6 | 每個告警通過合理化審查 |
| 7 | 操作員 review 完成 |

---

## 3. 人類審核閘門

```
HMI/告警設計完成。畫面數：{n} | 告警數：{total} | Critical：{count}
👉 請 SYS + 操作員代表審核。
```

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D05-005 | HMI Screen Design | ISA-101、畫面層級、色彩規範 |
| SK-D05-006 | Alarm Hierarchy | ISA-18.2、告警分級、合理化 |

<!-- Phase 6: Enhanced 2026-03-19. -->
