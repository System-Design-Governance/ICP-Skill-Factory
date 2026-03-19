---
name: industrial-protocols
description: >
  Configure industrial communication protocols including Modbus register mapping,
  IEC 61850 SCL configuration, and OPC UA information modeling.
  MANDATORY TRIGGERS: Modbus, IEC 61850, OPC UA, 通訊協定, protocol configuration,
  SCL, GOOSE, MMS, SV, sampled values, Modbus mapping, register mapping,
  OPC UA server, information model, ICD file, SCD file.
  Use this skill for Modbus, IEC 61850, and OPC UA protocol configuration.
---

# 工業通訊協定配置 (Industrial Protocols)

整合 3 個 SK，涵蓋 Modbus、IEC 61850 SCL 與 OPC UA 配置。

---

## 0. 初始化

1. 通訊架構已設計 (ICD 介面文件)
2. 設備清單與通訊介面已確認
3. 網路拓撲已完成

---

## 1. 工作流程

### Step 1: Modbus 映射配置 (SK-D05-009)

**Register 規劃**：

| Register Type | Address Range | 存取 | 用途 |
|--------------|---------------|------|------|
| Coil (0x) | 00001-09999 | R/W | DO 控制 |
| Discrete Input (1x) | 10001-19999 | R | DI 狀態 |
| Input Register (3x) | 30001-39999 | R | AI 量測 |
| Holding Register (4x) | 40001-49999 | R/W | AO/設定值 |

**Modbus Mapping Table 範例**：

```
| Register | Data Type | Description      | Unit | Scale |
|----------|-----------|------------------|------|-------|
| 40001    | UINT16    | Bus Voltage      | V    | ×0.1  |
| 40002    | INT16     | Bus Current      | A    | ×0.01 |
| 40003-04 | FLOAT32   | Active Power     | kW   | 1.0   |
| 40005-06 | FLOAT32   | Reactive Power   | kVAr | 1.0   |
| 00001    | BOOL      | CB Close Command | -    | -     |
| 10001    | BOOL      | CB Status        | -    | -     |
```

**步驟**：定義 register block 分區 → 填寫 mapping table → 設定 polling 週期 → RTU/TCP 選擇 → Slave ID 規劃 → 通訊測試

**⚠️ 避坑**：byte order (ABCD/CDAB) 必須確認；FLOAT32 佔 2 registers；polling 過頻影響設備

### Step 2: IEC 61850 SCL 配置 (SK-D05-010)

**SCL 檔案層級**：

| 檔案 | 用途 | 產出者 |
|------|------|--------|
| ICD | 設備能力描述 | 設備廠商 |
| SSD | 系統規格描述 | 系統整合商 |
| SCD | 全站配置描述 | 系統整合商 |
| CID | 設備實例配置 | 配置工具 |

**關鍵服務**：

| 服務 | 用途 | 效能 |
|------|------|------|
| GOOSE | 保護跳脫訊號 | <4ms |
| SV (Sampled Values) | 量測值串流 | 4000 samples/s |
| MMS | 監控/設定 | 一般 |
| Reports | 事件報告 | 依配置 |

**步驟**：收集 ICD 檔案 → 建立 SSD → 配置 GOOSE/SV dataset → 產出 SCD → 匯出 CID → 下載至 IED → GOOSE 通訊測試

**⚠️ 避坑**：GOOSE APPID 全站唯一；SV 需精確時鐘同步 (IEEE 1588)；SCL 版本相容性

### Step 3: OPC UA 配置 (SK-D05-011)

**Information Model 設計**：

```
Objects/
├── Station/
│   ├── Transformer_01/
│   │   ├── WindingTemp (AnalogItem, °C)
│   │   ├── TapPosition (DiscreteItem)
│   │   └── Status (TwoStateDiscrete)
│   └── Feeder_01/
│       ├── Current (AnalogItem, A)
│       ├── Voltage (AnalogItem, V)
│       └── CB_Control (Method)
```

**Security Policy**：

| Policy | 安全等級 | 適用 |
|--------|---------|------|
| None | 無 | 測試環境 |
| Basic256Sha256 | 中 | 內部 OT 網路 |
| Aes128_Sha256_RsaOaep | 高 | IT/OT 邊界 |

**步驟**：設計 information model (namespace) → 配置 security policy → 設定 endpoint → 憑證管理 (CA/self-signed) → client 連線測試 → subscription 配置

**⚠️ 避坑**：Security None 不可用於 production；憑證過期需自動告警

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | Modbus mapping table 完整且測試通過 |
| 2 | Byte order / data type 雙方確認 |
| 3 | IEC 61850 SCD 產出且 GOOSE 測試通過 |
| 4 | SV 時鐘同步精度符合要求 |
| 5 | OPC UA information model 完成 |
| 6 | OPC UA security policy 非 None |
| 7 | 所有協定通訊測試報告完成 |

---

## 3. 人類審核閘門

```
協定配置完成。Modbus 設備：{n} | IEC 61850 IED：{n} | OPC UA node：{n}
👉 請 SYS + 通訊工程師審核。
```

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D05-009 | Modbus Configuration | Register mapping、polling、RTU/TCP |
| SK-D05-010 | IEC 61850 SCL | ICD/SCD、GOOSE/SV/MMS |
| SK-D05-011 | OPC UA | Information model、security policy |

<!-- Phase 6: Enhanced 2026-03-19. -->
