---
name: icd-interface-design
description: >
  Develop Interface Control Documents (ICD) with formal protocol specs, data formats, timing,
  and error handling; select industrial protocols (Modbus/IEC 61850/DNP3/OPC UA) per communication path.
  MANDATORY TRIGGERS: ICD, 介面控制文件, interface control, 工業協定, industrial protocol,
  Modbus, IEC 61850, DNP3, OPC UA, 介面設計, interface design, 通訊路徑, communication path.
  Use this skill for ICD authoring and industrial protocol architecture decisions.
---

# 介面控制文件設計 (ICD Interface Design)

整合 2 個 SK，產出正式介面規格與工業協定選型。

---

## 0. 初始化

1. 系統架構圖已完成 (含所有子系統邊界)
2. 通訊路徑清單已識別 (point-to-point)
3. 各子系統負責廠商/團隊已確認

---

## 1. 工作流程

### Step 1: ICD 開發 (SK-D02-003)

**ICD 文件結構**：

```markdown
## ICD-{nnn}: {SystemA} ↔ {SystemB}

| 欄位 | 內容 |
|------|------|
| Interface ID | ICD-001 |
| System A | SCADA Server |
| System B | RTU-01 |
| Protocol | Modbus TCP |
| Data Format | 16-bit register, big-endian |
| Refresh Rate | 1 s (Status), 5 s (Analog) |
| Timeout | 3 s, retry 2x |
| Error Handling | Fallback to last-known, alarm |
```

**步驟**：列舉所有介面對 → 定義每對的 protocol/port/format → 定義 timing (scan rate, timeout, retry) → 定義 error handling (fallback, alarm, degraded mode) → 版本控制與簽核

**⚠️ 避坑**：byte order (big/little-endian) 必須雙方確認；timeout 需考慮網路延遲最壞情況；ICD 版本須與系統版本同步管理

### Step 2: 工業協定選型 (SK-D02-005)

| 協定 | 適用場景 | 速度 | 互通性 | 注意 |
|------|---------|------|--------|------|
| Modbus RTU/TCP | 簡單 I/O、legacy | 低 | 高 | 無安全機制 |
| IEC 61850 | 變電站內 | 高 (GOOSE <4ms) | 中 | SCL 配置複雜 |
| DNP3 | 配電/SCADA WAN | 中 | 高 | 需 SAv5 for security |
| OPC UA | IT/OT 整合 | 高 | 高 | 證書管理開銷 |

**步驟**：依通訊路徑分類 (站內/站間/IT-OT) → 比對協定特性 → 考量 cybersecurity 需求 → 確認 legacy 相容 → 產出 Protocol Assignment Matrix

**⚠️ 避坑**：同一路徑避免混用多協定；IEC 61850 需全站 SCL 一致；DNP3 over IP 需加密通道

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | 每個子系統介面對皆有 ICD |
| 2 | Protocol/port/data format 雙方確認 |
| 3 | Timing (scan rate, timeout, retry) 已定義 |
| 4 | Error handling 策略已定義 |
| 5 | Protocol Assignment Matrix 完成 |
| 6 | 無單一路徑混用衝突協定 |
| 7 | ICD 版本管理機制已建立 |

---

## 3. 人類審核閘門

```
ICD 設計完成。介面數：{n} | 協定：{protocols} | 待確認：{pending}
👉 請 SYS + 各子系統負責人審核。
```

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D02-003 | ICD Development | 介面規格、timing、error handling |
| SK-D02-005 | Industrial Protocol Architecture | Modbus/IEC 61850/DNP3/OPC UA 選型 |

<!-- Phase 6: Enhanced 2026-03-19. -->
