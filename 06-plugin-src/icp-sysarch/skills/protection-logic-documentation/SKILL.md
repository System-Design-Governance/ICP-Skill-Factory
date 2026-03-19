---
name: protection-logic-documentation
description: >
  Document protection logic diagrams (Boolean logic, trip matrix, interlocking) and
  perform fault recording analysis (waveform, SOE timeline).
  MANDATORY TRIGGERS: 保護邏輯, protection logic, 跳脫矩陣, trip matrix, 故障錄波,
  fault recording, 邏輯圖, logic diagram, SOE, sequence of events, 布林邏輯,
  Boolean logic, interlocking, 聯鎖, waveform analysis, 波形分析.
  Use this skill for protection logic documentation and fault recording analysis.
---

# 保護邏輯文件 (Protection Logic Documentation)

整合 2 個 SK，涵蓋邏輯圖/跳脫矩陣與故障錄波分析。

---

## 0. 初始化

1. 保護協調設計已完成 (TCC/距離)
2. 繼電器選型已確認 (含 I/O 配置)
3. 保護設定值已計算

---

## 1. 工作流程

### Step 1: 保護邏輯圖 (SK-D04-004)

**跳脫矩陣範例**：

```
Trip Matrix — Bay: Feeder-01
┌──────────┬─────┬─────┬─────┬──────┐
│ 保護功能  │ CB1 │ CB2 │ Alarm│ SOE  │
├──────────┼─────┼─────┼─────┼──────┤
│ 50/51    │  ●  │     │  ●  │  ●   │
│ 50N/51N  │  ●  │     │  ●  │  ●   │
│ 27 (UV)  │     │     │  ●  │  ●   │
│ 59 (OV)  │  ●  │     │  ●  │  ●   │
│ 79 (AR)  │  ●  │  ●  │  ●  │  ●   │
│ 86 (LOR) │  ●  │  ●  │  ●  │  ●   │
└──────────┴─────┴─────┴─────┴──────┘
```

**Boolean Logic 表示**：

```
TRIP_CB1 = (50 OR 51) OR (50N OR 51N) OR 59 OR 79_TRIP OR 86
BLOCK_AR = 86 OR Manual_Block
AR_INITIATE = 79_ENABLE AND TRIP_CB1 AND NOT BLOCK_AR
```

**步驟**：列舉所有保護功能 → 定義 trip assignment (哪個功能跳哪個 CB) → 設計 interlocking 邏輯 → 繪製 Boolean logic diagram → 建立跳脫矩陣 → 交叉檢查一致性

**⚠️ 避坑**：interlocking 邏輯錯誤可能導致拒跳或誤跳；86 (lockout) 重置必須手動

### Step 2: 故障錄波分析 (SK-D04-005)

**分析流程**：

| 步驟 | 內容 | 工具 |
|------|------|------|
| 1. 資料擷取 | COMTRADE 檔案 (.cfg/.dat) | Relay 下載 |
| 2. 波形檢視 | V/I 波形、相量圖 | SIGRA/TopView |
| 3. SOE 排列 | 事件時序 (ms 精度) | SOE 報表 |
| 4. 故障辨識 | 故障類型/位置/阻抗 | 計算 Z_fault |
| 5. 保護動作驗證 | 跳脫時間/正確性 | 比對設定值 |

**SOE 時序範例**：

```
T+0.000s  故障發生 (A 相接地)
T+0.025s  50N pickup
T+0.045s  51N 動作
T+0.065s  CB1 跳脫命令發出
T+0.115s  CB1 開極 (CB 動作時間 50ms)
T+0.215s  79 自動復閉 (dead time 100ms)
T+0.265s  復閉成功，故障消失
```

**⚠️ 避坑**：時鐘同步不準導致 SOE 排序錯誤 (需 GPS/IEEE 1588)；COMTRADE 取樣率需足夠

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | 每個 Bay 有跳脫矩陣 |
| 2 | Boolean logic 與矩陣一致 |
| 3 | Interlocking 邏輯已驗證 |
| 4 | 故障錄波分析流程已建立 |
| 5 | SOE 時鐘同步機制已確認 |

---

## 3. 人類審核閘門

```
保護邏輯文件完成。Bay 數：{n} | 矩陣：{done}/{total} | 錄波工具：{tool}
👉 請 PE + Protection Engineer 審核。
```

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D04-004 | Logic Diagram | Boolean logic、trip matrix、interlocking |
| SK-D04-005 | Fault Recording | COMTRADE、波形分析、SOE 時序 |

<!-- Phase 6: Enhanced 2026-03-19. -->
