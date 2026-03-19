---
name: plc-programming
description: >
  Develop PLC programs using ladder logic and structured text per IEC 61131-3,
  covering motor control, interlocking, state machines, and complex algorithms.
  MANDATORY TRIGGERS: PLC, 程式設計, programming, 階梯圖, ladder logic,
  結構化文字, structured text, IEC 61131-3, motor control, 馬達控制,
  interlocking, 聯鎖, state machine, 狀態機, PLC programming.
  Use this skill for PLC ladder logic and structured text programming.
---

# PLC 程式設計 (PLC Programming)

整合 2 個 SK，涵蓋階梯圖與結構化文字程式開發。

---

## 0. 初始化

1. I/O 清單已完成 (含 address mapping)
2. 控制策略/邏輯已確認
3. PLC 硬體型號與 CPU 已選定
4. 程式設計規範已建立 (命名/結構)

---

## 1. 工作流程

### Step 1: 階梯圖程式 (SK-D05-007)

**典型馬達控制迴路**：

```
(Ladder Logic — Motor Start/Stop with Interlock)

|  START   STOP    OL    INTERLOCK        MOTOR  |
|--[ ]--+--[/]---[/]------[ ]--------( )--------|
|       |                                        |
|  MOTOR|                                        |
|--[ ]--+                                        |
|                                                |
|  MOTOR                            RUN_IND      |
|--[ ]------------------------------------( )----|
|                                                |
|  OL                               FAULT_ALM    |
|--[ ]------------------------------------( )----|
```

**IEC 61131-3 規範重點**：

| 項目 | 規範 |
|------|------|
| 命名 | 描述性名稱 (非 I:0/1) |
| 註解 | 每個 rung 標題 + 說明 |
| 結構 | Function Block 重用 |
| Scan Time | 監控最壞情況 |
| 保留記憶體 | Retain 變數定義 |

**步驟**：定義 I/O mapping → 建立 FB library (motor/valve/analog) → 撰寫主程式 → 加入 interlock 邏輯 → 加入 alarm 處理 → 模擬測試 → 現場調試

**⚠️ 避坑**：latch 迴路缺少 reset 條件會卡住；scan time 過長影響安全迴路

### Step 2: 結構化文字程式 (SK-D05-008)

**狀態機範例**：

```pascal
CASE state OF
  ST_IDLE:
    IF startCmd AND NOT fault THEN
      state := ST_STARTING;
      timer(IN:=TRUE, PT:=T#10s);
    END_IF;

  ST_STARTING:
    motorCmd := TRUE;
    IF runFeedback THEN
      state := ST_RUNNING;
      timer(IN:=FALSE);
    ELSIF timer.Q THEN
      state := ST_FAULT;
      faultCode := 1; (* Start timeout *)
    END_IF;

  ST_RUNNING:
    IF stopCmd OR fault THEN
      state := ST_STOPPING;
      motorCmd := FALSE;
    END_IF;

  ST_STOPPING:
    motorCmd := FALSE;
    IF NOT runFeedback THEN
      state := ST_IDLE;
    END_IF;

  ST_FAULT:
    motorCmd := FALSE;
    IF resetCmd THEN
      state := ST_IDLE;
      faultCode := 0;
    END_IF;
END_CASE;
```

**適用場景**：複雜演算法 (PID, 排程)、狀態機、數學計算、通訊處理

**步驟**：定義狀態/事件 → 繪製狀態遷移圖 → 撰寫 ST 程式 → 單元測試 → 整合測試 → 文件化

**⚠️ 避坑**：ST 缺少 watchdog 可能無限迴圈；所有狀態必須有退出路徑

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | 程式符合 IEC 61131-3 |
| 2 | 命名與註解完整 |
| 3 | Interlock 邏輯經確認 |
| 4 | 模擬測試 100% 通過 |
| 5 | Scan time 在允許範圍內 |
| 6 | Retain 變數正確定義 |
| 7 | 狀態機所有路徑已測試 |

---

## 3. 人類審核閘門

```
PLC 程式完成。Ladder rung：{n} | ST module：{n} | FB：{count}
👉 請 Control Engineer + 現場工程師審核。
```

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D05-007 | Ladder Logic | IEC 61131-3、馬達控制、interlock |
| SK-D05-008 | Structured Text | 狀態機、複雜演算法 |

<!-- Phase 6: Enhanced 2026-03-19. -->
