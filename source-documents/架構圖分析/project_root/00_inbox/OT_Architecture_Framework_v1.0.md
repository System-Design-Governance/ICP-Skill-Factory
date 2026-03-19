# OT 架構圖標準化框架
**OT Architecture Diagram Standardization Framework**

版本 v1.0 ｜ 2026-03-04 ｜ 適用標準：Purdue Model / ISA-95 / IEC 62443

---

## 目錄

1. [框架設計原則](#1-框架設計原則)
2. [文件制度](#2-文件制度)
3. [元件庫（Component Library）](#3-元件庫component-library)
4. [專案設定檔（project.yaml）](#4-專案設定檔projectyaml)
5. [自動化工具鏈](#5-自動化工具鏈)
6. [Rulebook：拓撲規則](#6-rulebook拓撲規則)
7. [Rulebook：SVG 後製規則](#7-rulebook-svg-後製規則)
8. [Rulebook：品牌色碼](#8-rulebook品牌色碼)
9. [Rulebook：已知缺陷](#9-rulebook已知缺陷)
10. [SOP：新專案操作流程](#10-sop新專案操作流程)
11. [Claude Code Prompt 庫](#11-claude-code-prompt-庫)
12. [版本歷史與更新機制](#12-版本歷史與更新機制)

---

## 1. 框架設計原則

### 1.1 要解決的問題

每個新專案都需要手動修改 D2 源碼：改設備數量、連線方式、備援結構。耗時，且容易引入錯誤——特別是拓撲宣告順序會影響 dagre 佈局，這個副作用不直觀，換個工程師就會忘記。

更大的問題是：設備型號、通訊協定、顏色規範都分散在不同地方，沒有單一可信的來源。

### 1.2 三層分離架構

本框架將「要什麼」和「怎麼畫」完全分開：

```
┌─────────────────────────────────────────────────────────────┐
│  Layer 1  PROJECT CONFIG（project.yaml）                     │
│           工程師只需要填這份，不需要懂 D2 語法               │
├─────────────────────────────────────────────────────────────┤
│  Layer 2  COMPONENT LIBRARY（component_library.yaml）        │
│           所有設備的標準定義：型號、協定、D2 class、品牌色   │
├─────────────────────────────────────────────────────────────┤
│  Layer 3  CODE GENERATOR（gen_d2.py）                        │
│           讀取 project.yaml + 元件庫，套用 Rulebook，         │
│           輸出合法的 D2 源碼                                  │
├─────────────────────────────────────────────────────────────┤
│  Layer 4  RENDER（d2 CLI）                                   │
│           D2 官方渲染引擎（dagre layout）                     │
├─────────────────────────────────────────────────────────────┤
│  Layer 5  POSTPROCESS（optimize_svg.py）                     │
│           Title Bar 注入、Legend 浮層、遮罩、畫布縮減        │
└─────────────────────────────────────────────────────────────┘
```

工程師的完整工作流程：

```bash
# 1. 填寫設定檔（選設備、填數量、選通訊方式）
vim project.yaml

# 2. 產生 D2 源碼（自動套用所有 Rulebook 規則）
python gen_d2.py project.yaml

# 3. D2 渲染
d2 output.d2 diagram_raw.svg

# 4. SVG 後製
python optimize_svg.py --input diagram_raw.svg

# 5. 碰撞檢查
python check_collision.py diagram_final.svg
```

### 1.3 圖層分類

每個專案依用途產出四個層次的架構圖，各有不同的受眾和詳細程度：

| 圖層 ID | 名稱 | 主要受眾 | 包含內容 | 不包含 |
|---------|------|---------|---------|--------|
| DWG-L1 | Level 1 全景圖（System Context） | 客戶 / 業主 | Purdue 分層、Zone 邊界、主要系統名稱 | 設備型號、IP 位址 |
| DWG-L2 | Level 2 網路安全圖（Security View） | 資安審查 | Zone & Conduit、防火牆、通訊協定 | 設備品牌、施工細節 |
| DWG-L3 | Level 3 拓撲圖（Engineering View） | 整合商 / 施工 | 設備型號、IP、連線媒介、線號 | 一次設備細節 |
| DWG-L4 | Level 4 細節圖（Maintenance View） | 工程師維護 | 單設備介面、Port 對應、接線細節 | 系統整體架構 |

### 1.4 檔案命名規則

```
{客戶代碼}_{場站代碼}_{圖層}_{Rev}.{副檔名}

範例：
  TPC_HSUEH_L1_R1.0.d2           ← D2 源碼
  TPC_HSUEH_L1_R1.0_raw.svg      ← render 原始檔（未後製）
  TPC_HSUEH_L1_R1.0.svg          ← 最終交付檔
```

---

## 2. 文件制度

### 2.1 七份核心文件

| 文件 ID | 文件名稱 | 格式 | 更新觸發條件 |
|---------|---------|------|-------------|
| DOC-01 | OT 架構圖標準化框架（本文件） | `.md` | 框架架構變更 / 年度審查 |
| DOC-02 | Rulebook（拓撲與渲染規則手冊） | `.md` | 每次發現新問題或根治後 |
| DOC-03 | 元件庫（Component Library） | `.yaml` | 新設備採購 / 規格異動 |
| DOC-04 | 品牌規範（Brand Guidelines） | `.md` | 品牌識別更新時 |
| DOC-05 | 專案設定模板（project_template.yaml） | `.yaml` | DOC-03 異動後同步更新 |
| DOC-06 | Claude Code Prompt 庫 | `.md` | 每次迭代後補充新版本 |
| DOC-07 | 已知問題記錄（Known Issues） | `.md` | 每次 render 後更新 |

### 2.2 版本號規則

```
MAJOR（X.0.0）  框架架構調整，或現有 RULE 被修改
MINOR（x.Y.0）  新增 RULE、新增設備類型、新增工具模組
PATCH（x.x.Z）  說明補充、PATTERN 新增、錯字修正
```

文件之間的版本號相互獨立。DOC-03（元件庫）更新時，同步更新 DOC-05（模板）的版本號，但不需要更新 DOC-01。

---

## 3. 元件庫（Component Library）

### 3.1 設計目標

元件庫是本框架的核心資產，解決四個問題：

- 不同工程師使用不一致的設備命名、顏色、形狀
- 新設備採購後需要手動更新所有既有圖面
- 廠商型號更迭時，無法快速識別哪些圖面受影響
- 無法統計跨專案的設備使用頻率

### 3.2 YAML 結構定義

每個元件定義包含以下欄位：

```yaml
components:
  - id: string          # 唯一識別碼，格式：{類型前綴}-{廠商}-{型號}
                        # 例：SW-MOXA-EDS-408A、GW-ADV-IEC7442、RTU-TPRI-RSG007R
    category: enum      # 設備類別（見 3.3）
    vendor: string      # 廠商名稱，例：Moxa、Advantech、Siemens
    model: string       # 型號，例：EDS-408A
    display_name: string  # 圖面上顯示的名稱，可含 \n 換行
    d2_class: string    # D2 class 名稱，對應品牌 class 庫（見 3.4）
    protocols: list     # 支援的通訊協定
                        # 合法值：IEC61850、Modbus_TCP、Modbus_RTU、RS485、
                        #         DNP3、PRP、HSR、RSTP、SNMP、OPC_UA、IEC104
    ports:              # Port 定義（選填）
      ETH: int
      RS485: int
      RS232: int
      DI: int
      DO: int
    redundancy: bool    # 是否支援備援（PRP/HSR）（選填）
    certifications: list  # 認證清單（選填）
                          # 例：[IEC 62443-4-2, UL 61010-2, DNV GL]
    notes: string       # 已知問題或使用限制備注（選填）
    deprecated: bool    # true = 停產，禁止用於新專案（選填）
    superseded_by: string  # 替代型號 id，deprecated=true 時必填（選填）
```

**欄位必填規則：** `id`、`category`、`vendor`、`model`、`display_name`、`d2_class`、`protocols` 為必填。`deprecated=true` 時 `superseded_by` 也為必填。

### 3.3 設備類別清單（category 合法值）

| category | 中文名稱 | D2 Class | 圖形 | Purdue 層 |
|----------|---------|---------|------|---------|
| `SCADA_SERVER` | SCADA / DCS 伺服器 | `scada_server` | 矩形（深藍框） | L3 |
| `HMI` | HMI 操作站 / 工作站 | `hmi_workstation` | 矩形（天藍框） | L3 |
| `HISTORIAN` | 歷史資料庫 | `historian` | 圓柱（深藍框） | L3 |
| `ENG_WS` | 工程師工作站 | `engineering_ws` | 矩形（灰框） | L3 |
| `NTP_SERVER` | NTP / GPS 時間伺服器 | `ntp_server` | 矩形（天藍框） | L3 |
| `FIREWALL` | 防火牆 | `firewall` | 菱形（紅框） | DMZ |
| `SWITCH_PRP` | 工業級 PRP/HSR 交換機 | `switch_prp` | 六角形（天藍框） | L2 |
| `SWITCH_MANAGED` | 工業級 Managed 交換機 | `switch_prp` | 六角形（天藍框） | L2 |
| `DATA_DIODE` | 資料單向閘 | `data_diode` | 菱形（琥珀框） | DMZ |
| `JUMP_SERVER` | Jump Server | `jump_server` | 矩形（紅虛線框） | DMZ |
| `GATEWAY` | Protocol Gateway | `gateway` | 六角形（琥珀框） | L1 |
| `REDBOX` | RedBox（PRP 橋接器） | `redbox` | 六角形（深藍框） | L1 |
| `RTU` | RTU 遠端終端單元 | `rtu_ied` | 矩形（琥珀框） | L1 |
| `IED_PROTECTION` | 保護電驛 IED | `field_ied` | 矩形（灰框） | L0 |
| `IED_MEASUREMENT` | 量測 IED | `field_ied` | 矩形（灰框） | L0 |
| `PLC` | PLC 可程式控制器 | `plc` | 矩形（天藍框） | L1 |
| `INVERTER` | 逆變器 | `inverter` | 矩形（琥珀細框） | L0 |
| `UPS` | 不斷電系統 | `ups` | 矩形（琥珀細框） | L0/L1 |
| `MODEM` | 數據機（PSTN/4G） | `gateway` | 六角形（琥珀框） | DMZ |
| `EXTERNAL_SYS` | 外部系統（ERP/ADCC） | `external_system` | 矩形（灰虛線框） | L4 |

### 3.4 元件庫範例

```yaml
components:

  - id: SW-MOXA-EDS-408A
    category: SWITCH_PRP
    vendor: Moxa
    model: EDS-408A
    display_name: "EDS-408A\nPRP Switch"
    d2_class: switch_prp
    protocols: [PRP, RSTP, IEC61850, SNMP]
    ports:
      ETH_100M: 8
    redundancy: true
    certifications: [IEC 62443-4-2, DNV GL]

  - id: GW-ADV-IEC7442
    category: GATEWAY
    vendor: Advantech
    model: IEC-7442
    display_name: "IEC-7442\nProtocol Gateway"
    d2_class: gateway
    protocols: [IEC61850, Modbus_TCP, Modbus_RTU, RS485, DNP3]
    ports:
      ETH: 2
      RS485: 4
      RS232: 2
    redundancy: false

  - id: RTU-TPRI-RSG007R
    category: RTU
    vendor: TPRI
    model: RSG-007R
    display_name: "RTU\nRSG-007R"
    d2_class: rtu_ied
    protocols: [IEC61850, Modbus_RTU, RS485, DNP3]
    ports:
      ETH: 2
      RS485: 8
      DI: 32
      DO: 16
    redundancy: false
    certifications: [CNS, TPC-approved]

  - id: FW-MOXA-EDR-GN010
    category: FIREWALL
    vendor: Moxa
    model: EDR-GN010
    display_name: "FIREWALL\nEDR-GN010"
    d2_class: firewall
    protocols: [Ethernet, IPSec, OpenVPN]
    certifications: [IEC 62443-4-2]

  - id: IED-SEL-487E
    category: IED_PROTECTION
    vendor: SEL
    model: SEL-487E
    display_name: "SEL-487E\n變壓器差動保護"
    d2_class: field_ied
    protocols: [IEC61850, Modbus_RTU, RS485, DNP3]
    ports:
      ETH: 2
      RS485: 1
    certifications: [IEEE C37.90]

  - id: HMI-ADV-DA820
    category: HMI
    vendor: Advantech
    model: DA-820
    display_name: "SCADA-HMI\nDA-820"
    d2_class: hmi_workstation
    protocols: [OPC_UA, IEC61850, Modbus_TCP]
    notes: "主站與備援使用同型號，以 display_name 區分主站/備援標記"
```

### 3.5 元件庫維護流程

| 事件 | 觸發動作 | 必須更新的欄位 |
|------|---------|--------------|
| 新設備採購確認 | 新增元件 block，填寫全部必填欄位 | id, category, vendor, model, display_name, d2_class, protocols |
| 設備停產通知 | 設定 `deprecated: true`，填寫 `superseded_by` | deprecated, superseded_by |
| 協定支援異動 | 更新 protocols 欄位，在 notes 記錄版本 | protocols, notes |
| 發現渲染問題 | 在 notes 記錄問題描述與對應 Rulebook ID | notes |
| 新認證取得 | 更新 certifications 清單 | certifications |
| 元件庫更新後 | 同步更新 project_template.yaml 版本號 | — |

---

## 4. 專案設定檔（project.yaml）

### 4.1 設計原則

`project.yaml` 是工程師填寫的唯一輸入。它只描述「這個專案有什麼」，完全不涉及 D2 語法。`gen_d2.py` 負責把它翻譯成合規的 D2 源碼。

設備不是填「台數」，而是每台各填一個 block，因為每台的通訊方式和連接對象可能不同。

### 4.2 完整欄位規格

```yaml
# ============================================================
# OT 系統架構圖專案設定檔
# 填完後執行：python gen_d2.py this_file.yaml
# ============================================================

project:
  name: "[專案名稱]"             # 顯示在 Title Bar 第一行
  site: "[場站名稱]"             # 顯示在 Title Bar 第二行
  rev: "1.0"
  date: "2026-03-04"
  standard: "IEC 62443"         # 顯示在 Title Bar 第三行


# ══════════════════════════════════════════════════
# LEVEL 3：SCADA 監控站
# ══════════════════════════════════════════════════
scada:
  hmi_count: 2                  # 1=只有主站  2=主站+備援
  hmi_model: "DA-820"           # 對應 component_library.yaml 的 model
  hmi_redundancy: true          # true=顯示「主站/備援」標記

  historian: true               # 是否包含 Historian
  historian_model: ""           # 空白=不顯示型號

  engineering_ws: true          # 是否有工程師工作站
  engineering_ws_model: "DHI6C400 / OMCRON"

  ntp: true                     # 是否有 NTP/GPS 時間伺服器
  ntp_model: "IEEE 1588 PTP"
  gnss: true                    # 是否有 GNSS 天線

  ups_l3: true                  # L3 是否有 UPS
  ups_l3_capacity: "10kVA"


# ══════════════════════════════════════════════════
# DMZ / 防火牆
# ══════════════════════════════════════════════════
dmz:
  firewall_model: "EDR-GN010"   # 對應元件庫 model
  l3_switch_model: "PT-G7728"

  remote_access: true           # 是否有遠端通訊備援
  remote_type: "PSTN+4G"        # "PSTN+4G" | "4G" | "PSTN" | "RF"
  modem_model: ""               # 空白=依 remote_type 自動填寫


# ══════════════════════════════════════════════════
# LEVEL 4：企業層（可選）
# ══════════════════════════════════════════════════
enterprise:
  enabled: true                 # false = 完全省略 L4 Zone 及所有 L4 連線
  erp: true
  adcc: true
  scada_ws: true


# ══════════════════════════════════════════════════
# LEVEL 2：交換路由層
# ══════════════════════════════════════════════════
network:
  prp_enabled: true             # false = 單網，不畫 LAN-B 節點和 REDBOX
  core_switch_model: ""         # 空白=不顯示型號

  # 每個 feeder_group 對應：
  #   L2 一對邊緣 switch（LAN-A + LAN-B）
  #   L1 一個 MCC 節點
  # 新增饋線：在這裡加一個 block，gen_d2.py 自動展開
  feeder_groups:
    - id: "M1"
      label: "M1"
      description: "161kV TR"
      mcc_panels: "16/17"
    - id: "M2"
      label: "M2"
      description: "161kV BPT / General"
      mcc_panels: "01/02/03"
    - id: "M3"
      label: "M3"
      description: "161kV LINE / TR"
      mcc_panels: "04/05/06"
    - id: "M4"
      label: "M4"
      description: "53.4kV MAIN / BPT"
      mcc_panels: "07/08/09/10"
    - id: "M5"
      label: "M5"
      description: "53.4kV STATCOM"
      mcc_panels: "11/12/13"
    - id: "M6"
      label: "M6"
      description: "23kV"
      mcc_panels: "14/15"


# ══════════════════════════════════════════════════
# LEVEL 1：現場控制層
# ══════════════════════════════════════════════════
field_control:

  # Protocol Gateway
  gateways:
    enabled: true
    count: 2                    # 1=單 GW  2=雙 GW（A/B 備援）
    model: "IEC-7442 / Advantech"
    protocol_conversion:        # 僅用於 DWG-L3 標注，不影響拓撲
      - "IEC61850 → Modbus RTU"
      - "IEC61850 → RS-485"

  # RTU 盤（可多個，每個 block 對應一個實體盤）
  rtu_panels:
    - id: "TPC"                 # 唯一 ID，用於 connected_to 引用
      label: "TPC RTU 盤"
      rtu_model: "RSG-007R"

      redbox: true              # 是否有 REDBOX（prp_enabled=false 時自動忽略）

      # L1 層掛在此 RTU 盤裡的 IED
      ieds:
        - id: "IED_87L1"
          label: "87L1\n線路保護"
          protocol: "IEC61850"  # "IEC61850" | "Modbus_RTU" | "Modbus_TCP" | "RS485"
        - id: "IED_87L2"
          label: "87L2\n線路保護"
          protocol: "IEC61850"
        - id: "IED_60BF"
          label: "60BF\n斷路器失效"
          protocol: "IEC61850"

      connected_to_feeder: "M1" # 對應 network.feeder_groups 的 id

  # STATCOM 系統（可選）
  statcom:
    enabled: true
    osc_model: "BPX-B1"
    module_count: 3             # OSC Module 數量（LNK-A/B/C）
    protocol: "Modbus TCP"


# ══════════════════════════════════════════════════
# LEVEL 0：現場設備層
# ══════════════════════════════════════════════════
field_devices:

  # 保護電驛 IED 群（R 群）
  protection_ieds:
    enabled: true
    group_label: "R 群（保護電驛 IED）"
    ieds:
      - id: "IED_87T"
        label: "87T1 / 87T2\n變壓器差動保護"
        comm: "IEC61850_fiber"  # 引用下方 comm_styles 的 key
        connected_to: "gw_A"   # "gw_A" | "gw_B" | "rtu_{panel_id}" | null
                                # null = 省略此連線（避免長線穿圖）
      - id: "IED_87B"
        label: "87B\n匯流排保護"
        comm: "IEC61850_fiber"
        connected_to: "gw_A"
      - id: "IED_87L"
        label: "87L\n線路差動保護"
        comm: "IEC61850_fiber"
        connected_to: "gw_B"
      - id: "IED_50BF"
        label: "50BF-1/2\n斷路器失效保護"
        comm: "RS485_modbus"
        connected_to: "rtu_TPC"
      - id: "IED_50S"
        label: "50/51-1/2\n過電流保護"
        comm: "RS485_modbus"
        connected_to: "rtu_TPC"
      - id: "IED_D7"
        label: "87D / 87D2\n其他差動保護"
        comm: "IEC61850_fiber"
        connected_to: "gw_A"

  # 太陽能 / 儲能設備（可選）
  solar_storage:
    enabled: true
    group_label: "太陽能 / 儲能設備"
    devices:
      - id: "INV_A"
        label: "Inverter 群 A\nDC → AC"
        type: "inverter"
        comm: "RS485_modbus"
        connected_to: "mcc_M4"
      - id: "INV_B"
        label: "Inverter 群 B\nDC → AC"
        type: "inverter"
        comm: "RS485_modbus"
        connected_to: "mcc_M5"
      - id: "DC_CHG"
        label: "DC CHARGE\n充放電系統"
        type: "plc"
        comm: "RS485"
        connected_to: "gw_B"
      - id: "RF_MOD"
        label: "RF Solar Module\n無線監測"
        type: "gateway"
        comm: "RF_wireless"
        connected_to: "gw_B"
      - id: "UPS_FIELD"
        label: "UPS（現場）\nSerial RS485"
        type: "ups"
        comm: "RS485_modbus"
        connected_to: null      # null = 省略此連線，避免 2812px 長線穿越 13 個節點


# ══════════════════════════════════════════════════
# 通訊方式樣式庫
# 在這裡集中定義，其他地方只用 key 引用
# 新增通訊方式：加一個 block，補充 label/stroke/stroke_width/stroke_dash
# ══════════════════════════════════════════════════
comm_styles:

  PRP_LAN_A:
    label: "PRP LAN-A"
    stroke: "#008EC3"
    stroke_width: 2
    stroke_dash: 0              # 0 = 實線

  PRP_LAN_B:
    label: "PRP LAN-B"
    stroke: "#0C3467"
    stroke_width: 2
    stroke_dash: 3

  IEC61850_fiber:
    label: "IEC 61850 GOOSE  Fiber SM"
    stroke: "#0C3467"
    stroke_width: 3
    stroke_dash: 0

  IEC61850_MMS:
    label: "IEC 61850 MMS"
    stroke: "#008EC3"
    stroke_width: 2
    stroke_dash: 0

  PRP_fiber_A:
    label: "PRP LAN-A  Fiber MM"
    stroke: "#008EC3"
    stroke_width: 2
    stroke_dash: 0

  PRP_fiber_B:
    label: "PRP LAN-B  Fiber MM"
    stroke: "#0C3467"
    stroke_width: 2
    stroke_dash: 3

  OPC_UA_A:
    label: "OPC-UA / ICCP  LAN-A"
    stroke: "#008EC3"
    stroke_width: 2
    stroke_dash: 0

  OPC_UA_B:
    label: "OPC-UA / ICCP  LAN-B"
    stroke: "#0C3467"
    stroke_width: 2
    stroke_dash: 3

  IT_ethernet:
    label: "Ethernet / OPC-UA"
    stroke: "#9B9B9B"
    stroke_width: 1
    stroke_dash: 3

  RS485_modbus:
    label: "RS-485  Modbus RTU"
    stroke: "#9B9B9B"
    stroke_width: 1
    stroke_dash: 3

  RS485:
    label: "RS-485"
    stroke: "#9B9B9B"
    stroke_width: 1
    stroke_dash: 3

  Modbus_TCP:
    label: "Modbus TCP"
    stroke: "#008EC3"
    stroke_width: 1
    stroke_dash: 0

  VPN_PSTN:
    label: "PSTN 備援 / RF"
    stroke: "#F5A623"
    stroke_width: 1
    stroke_dash: 4

  RF_wireless:
    label: "RF Wireless"
    stroke: "#F5A623"
    stroke_width: 1
    stroke_dash: 4

  IRIG_B:
    label: "IRIG-B / PPS  Fiber"
    stroke: "#0C3467"
    stroke_width: 3
    stroke_dash: 0

  IEEE1588_A:
    label: "IEEE 1588 PTP  LAN-A"
    stroke: "#008EC3"
    stroke_width: 2
    stroke_dash: 0

  IEEE1588_B:
    label: "IEEE 1588 PTP  LAN-B"
    stroke: "#0C3467"
    stroke_width: 2
    stroke_dash: 3
```

### 4.3 欄位快速對照

| 我想要的效果 | 改哪個欄位 | 設定值 |
|------------|-----------|--------|
| 只有單台 HMI，無備援 | `scada.hmi_count` | `1` |
| 不做 PRP 雙網冗餘 | `network.prp_enabled` | `false` |
| 增加一個饋線迴路 | `network.feeder_groups` | 加一個 block（id/label/description/mcc_panels） |
| 新增保護電驛 IED | `field_devices.protection_ieds.ieds` | 加一個 block（id/label/comm/connected_to） |
| 某設備改用 Modbus TCP | 該設備的 `comm` | `"Modbus_TCP"` |
| 省略某條長線（避免穿圖） | 該設備的 `connected_to` | `null` |
| 不畫 L4 企業層 | `enterprise.enabled` | `false` |
| 去掉 STATCOM | `field_control.statcom.enabled` | `false` |
| 去掉遠端備援 | `dmz.remote_access` | `false` |
| 增加 RTU 盤 | `field_control.rtu_panels` | 加一個 panel block |
| Gateway 改為單台 | `field_control.gateways.count` | `1` |
| 新增通訊方式 | `comm_styles` | 加一個新 key，定義 label/stroke/stroke_width/stroke_dash |

---

## 5. 自動化工具鏈

### 5.1 gen_d2.py 模組設計

gen_d2.py 讀取 `project.yaml` 和 `component_library.yaml`，套用所有 Rulebook 規則，輸出合法的 D2 源碼。

每個函式對應一個 Purdue 層次或連線群組：

| 函式 | 職責 | 關聯 Rulebook |
|------|------|--------------|
| `load_config()` | 載入 project.yaml + 元件庫，驗證必填欄位 | — |
| `validate_config()` | 驗證 connected_to 引用存在、comm_styles key 合法 | R-D2-04 |
| `gen_header()` | 輸出 vars: / direction: / classes: 區塊 | R-D2-01, R-BR-01 |
| `gen_l4()` | L4 Zone（enterprise.enabled 開關） | T-07 |
| `gen_dmz()` | DMZ Zone | — |
| `gen_l3()` | L3 Zone（hmi/historian/ntp 開關） | T-02 |
| `gen_l2()` | L2 Zone（feeder_groups 動態展開 edge switch） | T-01 |
| `gen_l1()` | L1 Zone，**gw 子群組永遠第一個宣告** | T-04, R-D2-03 |
| `gen_l1_gw()` | Protocol Gateway 子群組（count 開關） | T-03 |
| `gen_l1_rtu_panel()` | RTU 盤子群組（含 REDBOX PRP 開關） | T-01 |
| `gen_l1_mcc()` | MCC 群子群組（從 feeder_groups 展開） | — |
| `gen_l1_statcom()` | STATCOM 子群組（enabled 開關） | T-08 |
| `gen_l0()` | L0 Zone（r_group 在前、solar 在後） | R-D2-05 |
| `gen_conn_backbone()` | L2 骨幹 PRP 連線，**第一條保留 label，其餘置空** | T-05, R-D2-06 |
| `gen_conn_l0()` | L0 連線，**connected_to=null 跳過** | T-06, R-D2-07 |
| `resolve_target()` | YAML 語意 key → D2 節點路徑轉換 | — |
| `emit_connection()` | 輸出單一連線的 D2 語法（查 comm_styles） | R-D2-09, R-D2-10 |

**拓撲 Rulebook（T 系列）完整清單：**

| 規則 ID | 名稱 | 觸發條件 | 行為 |
|---------|------|---------|------|
| T-01 | PRP 備援開關 | `network.prp_enabled: false` | 每個 feeder 只產生一個 edge switch，RTU 盤不產生 REDBOX，連線只用 LAN-A |
| T-02 | HMI 備援開關 | `scada.hmi_count: 1` | 只產生 HMI_A，連接 LAN-A |
| T-03 | Gateway 備援 | `gateways.count: 1` | 只有 GW_A，所有設備連 GW_A |
| T-04 | L1 子群組排列順序 | 永遠套用 | L1 Zone 內宣告順序必須是：**gw → rtu_panels → mcc → statcom** |
| T-05 | 骨幹 label 去重 | 永遠套用 | LAN-A 骨幹只有**第一條**保留 label，後續全部設為 `""`；LAN-B 同理 |
| T-06 | 跳過 null 連線 | `connected_to: null` | 完全不產生該設備的連線宣告 |
| T-07 | L4 可選 | `enterprise.enabled: false` | 省略整個 L4 Zone 和 L4↔DMZ 所有連線 |
| T-08 | STATCOM 可選 | `statcom.enabled: false` | 省略 statcom 子群組和 L2.SW_09→statcom 連線 |

T-04 是最關鍵的規則：dagre 在 `direction: down` 下依宣告順序從左到右排列子群組，`gw` 必須第一個才能排在左側靠近 `L0.r_group`，否則 3 條光纖線會橫穿整個 L0 區域（1700px 長線，穿越所有 IED 節點文字）。

### 5.2 optimize_svg.py 模組設計

optimize_svg.py 執行固定的八步驟後製流程：

| 步驟 | 函式 | 職責 | 關聯 Rulebook |
|------|------|------|--------------|
| 1 | `parse_svg()` | 解析 SVG，取得主圖 bounding box | — |
| 2 | `remove_d2_artifacts()` | 移除 D2 殘留的 title/legend 節點 | R-PP-01 |
| 3 | `shift_content()` | 所有主圖元素向下位移 110px（TITLE_HEIGHT） | R-PP-01 |
| 4 | `fix_dasharray()` | 修正過大的 stroke-dasharray 值（> 8 → 6,4） | R-PP-04 |
| 5 | `inject_title_bar()` | 注入品牌 Title Bar（從 project.yaml 讀標題） | R-PP-02 |
| 6 | `find_empty_zone()` + `inject_legend()` | 掃描空白區域，注入嵌入式 Legend 浮層 | R-PP-03, R-PP-06 |
| 7 | `add_label_backgrounds()` | 所有連線 label 加白底遮罩 | R-PP-05 |
| 8 | `update_canvas()` + `write()` | 更新 viewBox / height，輸出最終 SVG | R-PP-01 |

步驟順序不可改變。特別是步驟 3（位移）必須在步驟 5（注入 Title Bar）之前，否則 Title Bar 也會被位移。

### 5.3 check_collision.py 設計

每次 render 後執行，輸出碰撞檢查報告：

```python
def quick_collision_check(svg_path: str) -> dict:
    """
    回傳：{
      'a_class': int,   # A 類碰撞數（連線路徑穿越節點文字）
      'affected': list  # 受影響的節點名稱
    }
    """

# 合格標準：
# a_class == 0   優秀（Green）
# a_class 1~4   可接受（Yellow）
# a_class >= 5   必須修正（Red），更新 Rulebook
```

---

## 6. Rulebook：拓撲規則

本章所有規則來自實測確認。每條規則有唯一 ID，可在 Prompt 中直接引用。

### R-D2-01 🔴 永遠使用 dagre，禁止使用 elk

```d2
vars: {
  d2-config: {
    layout-engine: dagre    # 強制
    theme-id: 0
  }
}
```

ELK 的 `near: top-center` / `near: bottom-right` 在實測中，前者讓 title 渲染在 y = -31（畫布外），後者讓 legend 延伸至畫布右側 4000px+。ELK 的 orthogonal routing 也在長連線轉折處插入 SVG `S` 指令，產生不自然曲線。

### R-D2-02 🔴 禁止在 D2 中宣告 title: 和 legend: 節點

D2 的 title/legend 位置在 dagre 下完全不可控。改由 `optimize_svg.py` 的後製步驟 5 和步驟 6 注入。

### R-D2-03 🔴 子群組的宣告順序決定 dagre 的水平排列

dagre 在 `direction: down` 下，同一容器內的子群組**依宣告順序從左到右排列**。這是控制節點位置的唯一可靠方式。

```d2
# 讓 gw 排在最左側（靠近 L0.r_group）：
L1: "Level 1｜現場控制層  Field Control Zone" {
  gw:      "Protocol Gateway"       { ... }  # 第一個 = 最左
  tpc:     "TPC RTU 盤"             { ... }
  mcc:     "MCC 群"                 { ... }
  statcom: "STATCOM 系統"           { ... }  # 最後 = 最右
}
```

### R-D2-04 🔴 跨 Zone 長線的兩端必須宣告在同一側

長線判斷方式：兩個節點所在子群組的宣告順序差距 > 2，連線將橫跨超過 1000px，必然穿越中間節點文字。

```
實際案例（diagram_final.svg 碰撞 G4）：
  問題：L1.gw（x≈2100）→ L0.r_group IED（x≈200~1100）
        GW 在 L1 第四個子群組（右側），L0 R 群在最左
  結果：3 條光纖線橫穿 1700px，穿越所有 IED 節點文字
  修正：把 L1.gw 移到 L1 的第一個子群組宣告
        → dagre 將 GW 排在左側 → 連線垂直向下，不再橫跨
```

### R-D2-05 🔴 L0 子群組必須對應其連接的 L1 子群組位置

```d2
# 正確：r_group 靠近 gw（都在左側），solar 靠近 mcc（都在右側）
L0: "Level 0｜現場設備  Field Devices" {
  r_group: "R 群（保護電驛 IED）" { ... }  # 第一個（左）= 靠近 L1.gw
  solar:   "太陽能 / 儲能設備"    { ... }  # 第二個（右）= 靠近 L1.mcc
}
```

違反此規則時，L1→L0 的連線會橫穿整個 L0 區域，產生跨度 3000px+ 的斜線穿越 10 個以上的節點（碰撞分類 G5，為所有問題中最嚴重的）。

### R-D2-06 🟠 一對多骨幹連線，重複 label 除第一條外全部置空

```d2
# 正確：8 條骨幹，LAN-A 只有第一條保留 label
L2.core.SW_01 -> L2.edge.SW_03: "PRP LAN-A" { style.stroke: "#008EC3"; style.stroke-width: 2 }
L2.core.SW_01 -> L2.edge.SW_05: ""          { style.stroke: "#008EC3"; style.stroke-width: 2 }
L2.core.SW_01 -> L2.edge.SW_07: ""          { style.stroke: "#008EC3"; style.stroke-width: 2 }
L2.core.SW_01 -> L2.edge.SW_09: ""          { style.stroke: "#008EC3"; style.stroke-width: 2 }
# LAN-B 同理
```

8 條線全部有 label 時，label 堆疊在同一 y 帶（y≈1300~1600），互相遮蓋，且加重碰撞。

### R-D2-07 🟠 省略語意上不必要的長線

連線保留條件：**同時滿足以下兩點**

1. 技術上代表真實的通訊路徑（不只是供電或物理安裝關係）
2. 讀圖者需要這條線才能理解系統邏輯

```
實際案例：L0.solar.UPS_FIELD -> L1.tpc.RTU
分析：UPS 為 RTU 提供備用電源，不是通訊連線
     在 Purdue Model 圖中不顯示電源線
     此連線跨度 2812px，穿越 13 個節點文字
結論：設 connected_to: null，省略此連線
```

### R-D2-08 🔴 所有子群組必須使用 class: zone_sub，禁止硬編碼顏色

```d2
# 正確
core: "核心交換（雙網 PRP 冗餘）" {
  class: zone_sub               # 使用標準 class
  SW_01: "Switch-01" { class: switch_prp }
}

# 禁止
core: "核心交換" {
  style: { fill: "#dcfce7"; stroke: "#15803d" }   # 硬編碼非品牌色
}
```

### R-D2-09 🔴 每條連線必須直接 inline style，禁止使用連線 class

連線 class 的 `stroke-dash` 值在 SVG 輸出中不可預測，必須用 inline style 才能確保顏色和線型正確。

```d2
# 正確：inline style
NodeA -> NodeB: "PRP LAN-A  Fiber MM" {
  style.stroke: "#008EC3"
  style.stroke-width: 2
}

# 禁止：連線 class
NodeA -> NodeB: "PRP LAN-A" { class: link_lan_a }
```

### R-D2-10 🔴 連線 label 禁止使用 \n，改用兩空格分隔

```d2
# 正確
NodeA -> NodeB: "IEC 61850 GOOSE  Fiber SM"    # 兩空格分隔協定與媒介

# 禁止
NodeA -> NodeB: "IEC 61850 GOOSE\nFiber SM"    # \n 在 SVG 中被忽略
```

### R-D2-11 🟠 stroke-dash 設定值速查表

D2 在 dagre 下將 `stroke-dash` 值乘以 `stroke-width`，SVG 實際值 = D2設定值 × stroke-width。

| 連線類型 | stroke-width | D2 設定值 | SVG 實際 dasharray |
|---------|-------------|----------|-------------------|
| Zone 容器虛線框 | 2 | 3 | 6 |
| PRP LAN-B 備援 | 2 | 3 | 6 |
| IT / 企業網路 | 1 | 5 | 5 |
| VPN / 遠端存取 | 1 | 4 | 4 |
| RS-485 串列 | 1 | 3 | 3 |
| RF 無線 | 1 | 4 | 4 |

---

## 7. Rulebook：SVG 後製規則

### R-PP-01 🔴 後製流程固定八步驟，順序不可改變

```
Step 1  parse_svg()              解析 bounding box
Step 2  remove_d2_artifacts()    移除殘留 title/legend
Step 3  shift_content(+110px)    保留 Title Bar 空間
Step 4  fix_dasharray()          修正過大 dasharray
Step 5  inject_title_bar()       注入品牌 Title Bar
Step 6  inject_legend()          注入 Legend 浮層
Step 7  add_label_backgrounds()  連線 label 加白底
Step 8  update_canvas()          更新 viewBox，輸出
```

### R-PP-02 🔴 Title Bar 規格（固定，不得修改）

```
高度：110px，橫跨全畫布寬度，y = 0~110
背景：#0C3467（Navy Primary）
左側裝飾條：x = 0~6, height = 110, fill = #008EC3（Sky Blue）

文字三行：
  行 1  y=40   font-size=21  bold  fill=white   text-anchor=middle  → 主標題
  行 2  y=66   font-size=12  fill=#93c5fd                           → 專案/場站/版本/日期
  行 3  y=88   font-size=10  fill=#94a3b8                           → "Purdue Model / ISA-95 / IEC 62443 Zone & Conduit"
```

### R-PP-03 🔴 Legend 必須以嵌入浮層形式放置，禁止頁尾全寬設計

頁尾全寬 Legend 佔總畫布高度的 9.7%，視覺上如附錄表格，且字體因縮放不可讀。

```
位置：x=30, y=130（title bar 正下方左上角）
尺寸：width=480, height=28（標題列）+ max(左欄項目數, 右欄項目數) × 27 + 16
     以目前 10 項元件 + 7 種連線為例：28 + 10×27 + 16 = 314px

落點選擇原則：
  每次 render 後自動掃描，選擇圖面左上角第一個「完全空白」的矩形區域
  浮層與任何節點/容器的間距 ≥ 20px

外框樣式：
  fill=white, fill-opacity=0.93
  stroke=#0C3467, stroke-width=1.5, rx=6
  filter: drop-shadow(2px 2px 6px rgba(0,0,0,0.15))

標題列：
  height=28, fill=#0C3467
  text: "圖例 / Legend"  fill=white  font-size=11  bold

雙欄佈局：
  左欄：元件類型（含圖示 + 標籤）
  右欄：連線類型（含線段範例 + 標籤）
  垂直分隔線：x=244, stroke=#9B9B9B, stroke-width=0.5
  每行高 27px，font-size=11
```

### R-PP-04 🔴 stroke-dasharray 補正函式

```python
def fix_dasharray(svg_content: str) -> str:
    """
    D2 (dagre) 將 stroke-dash 值乘以 stroke-width 輸出至 SVG。
    任何值超過 8 的 dasharray 都是被放大過的，一律修正為 6,4。
    """
    def replacer(m):
        vals = [float(v) for v in re.split(r'[,\s]+', m.group(1).strip()) if v]
        if any(v > 8 for v in vals):
            return 'stroke-dasharray:6,4'
        return m.group(0)
    return re.sub(r'stroke-dasharray:\s*([\d.,\s]+)', replacer, svg_content)
```

### R-PP-05 🔴 所有連線 label 必須加白底遮罩

連線 label 因 dagre 路由會穿越其他節點文字或線條，白底遮罩確保可讀性。

```python
CONN_KEYWORDS = {
    'PRP', 'IEC', 'IEEE', 'Modbus', 'RS-485', 'Ethernet',
    'OPC', 'SQL', 'IRIG', 'Control', 'Serial', 'GOOSE',
    'MMS', 'Fiber', 'RF', 'PSTN', 'VPN', 'Wireless'
}

def add_label_background(svg_content: str, font_size: int = 11) -> str:
    """
    識別條件：text 內容包含 CONN_KEYWORDS 中任一關鍵字
    遮罩規格：
      fill=white, fill-opacity=0.85, rx=2
      x = text_x - 4
      y = text_y - font_size
      width = estimate_width(text) + 8
      height = font_size + 4
    必須在對應 text 的前一行插入 rect（SVG 繪製順序，rect 先繪製才能墊底）
    """
    def estimate_width(text: str) -> int:
        ascii_w = sum(7 for c in text if ord(c) < 128)
        cjk_w   = sum(13 for c in text if ord(c) >= 0x4E00)
        return ascii_w + cjk_w + 8
    ...
```

### R-PP-06 🟠 每次 render 後自動掃描空白區域，動態決定 Legend 位置

```python
def find_empty_zone(svg_content: str,
                    min_w: int = 500, min_h: int = 300,
                    y_start: int = 130) -> tuple[int, int] | None:
    """
    收集所有元素的座標，以 100px 步進掃描，
    回傳第一個符合尺寸的空白區域左上角座標 (x, y)
    找不到時：fallback 到右下角
    """
```

不硬編碼 Legend 座標的原因：不同拓撲的空白區域位置不同。當前這份圖的空白區在左上角 `x=0~2369, y=110~578`，但 feeder_groups 數量改變後，空白區可能移動。

---

## 8. Rulebook：品牌色碼

### R-BR-01 🔴 品牌色碼完整表（唯一合法顏色集合）

| 色名 | HEX | 用途 |
|------|-----|------|
| Navy Primary | `#0C3467` | L4/L2 Zone 框線、SCADA Server、LAN-B 連線、IEC 61850 光纖、Title Bar 背景 |
| Sky Blue | `#008EC3` | L3 Zone 框線、HMI/Switch PRP、LAN-A 連線、PTP 時間同步、Title Bar 裝飾條 |
| Amber | `#F5A623` | L1 Zone 框線、Gateway/RTU/IED、VPN/RF 連線 |
| Gray | `#9B9B9B` | L0 Zone 框線、Field IED、IT 連線、RS-485 串列 |
| Red（固定） | `#c0392b` | 防火牆（資安辨識色，不隨品牌變動） |
| Green（L2） | `#2e7d32` | L2 Control Network Zone 框線 |

**Zone 背景淡色：**

| Zone | 背景色 | 框線色 |
|------|--------|--------|
| L4 Enterprise | `#e8eef5` | `#0C3467` |
| DMZ | `#fdecea` | `#c0392b` |
| L3 Supervisory | `#e0f4fb` | `#008EC3` |
| L2 Control Network | `#e8f5e9` | `#2e7d32` |
| L1 Field Control | `#fff8e1` | `#F5A623` |
| L0 Physical | `#f5f5f5` | `#9B9B9B` |
| 子群組（zone_sub） | transparent | `#9B9B9B` |

### R-BR-02 🔴 禁止使用以下色碼（從舊版 class 庫移除）

```
#dbeafe / #1d4ed8  ← 舊版 scada_server（通用藍，非品牌色）
#fef9c3 / #a16207  ← 舊版 hmi_workstation（黃色）
#f0fdf4 / #15803d  ← 舊版 historian（薄荷綠）
#c026d3            ← 舊版 zone_enterprise（紫色）
#d97706            ← 舊版 zone_dmz（橘色）
#ede9fe / #6d28d9  ← 舊版子群組硬編碼紫色
#ecfdf5 / #059669  ← 舊版 switch_prp（薄荷綠）
#7c3aed            ← 舊版 zone_field / rtu_ied（深紫）
```

---

## 9. Rulebook：已知缺陷

每個 Known Bug 記錄症狀、影響版本和防禦方式。

### KB-01：title/legend 節點位置不可控

- **症狀：** `near: top-center` → title 渲染在 y = -31（畫布外）；`near: bottom-right` → legend 延伸至畫布右側 4000px+
- **影響版本：** D2 所有目前測試過的版本（ELK 和 dagre 均有）
- **防禦：** 永遠不在 D2 中宣告 title/legend 節點，改用後製腳本注入（R-D2-02）

### KB-02：stroke-dash 值自動乘以 stroke-width

- **症狀：** D2 `stroke-dash: 5` + `stroke-width: 2` → SVG 輸出 `stroke-dasharray: 10, 9.8`
- **影響版本：** D2 所有版本
- **防禦：** 按 R-D2-11 表格設定值；後製腳本執行 R-PP-04 補正

### KB-03：ELK 連線路由產生 SVG S 曲線

- **症狀：** ELK 的 orthogonal routing 在轉折點插入 SVG `S` 曲線指令，長連線出現不自然 S 形彎折
- **影響版本：** ELK layout（改用 dagre 後不存在）
- **防禦：** 永遠使用 dagre（R-D2-01）

### KB-04：dagre 子群組排列順序不穩定（超過 3 層巢狀）

- **症狀：** 容器巢狀超過 3 層時，dagre 可能忽略宣告順序，自行決定排列
- **影響版本：** dagre，深層巢狀場景
- **防禦：** 容器巢狀最多 2 層；超過 3 層考慮展平結構

### KB-05：連線 label 換行在 SVG 中被忽略

- **症狀：** D2 連線 label 中的 `\n` 在 SVG 輸出中被替換為空格，不換行
- **影響版本：** D2 所有版本
- **防禦：** 使用兩空格分隔（R-D2-10）

### KB-06：dagre 長線路由穿越中間節點（無法自動繞開）

- **症狀：** 兩端距離 > 1000px 時，dagre 路由直線穿越所有中間節點的 bounding box
- **影響版本：** dagre
- **防禦：** 調整子群組宣告順序縮短連線（R-D2-03/04/05）；設 `connected_to: null` 省略不必要長線（T-06）；後製加 label 白底遮罩（R-PP-05）

---

## 10. SOP：新專案操作流程

### 10.1 新專案 8 步驟

**Step 1：建立設定檔**

複製 `project_template.yaml` → `project_{客戶代碼}.yaml`，填寫：專案名稱、場站名稱、feeder_groups 清單、保護電驛 IED 清單、通訊方式。

驗證：所有必填欄位非空，feeder_groups ≥ 1。

**Step 2：從元件庫選設備**

確認所有 `ieds[].comm` 和 `devices[].comm` 的 key 存在於 `comm_styles`。確認設備型號在 `component_library.yaml` 有對應記錄（deprecated 不可用於新專案）。

**Step 3：產生 D2 源碼**

```bash
python gen_d2.py project.yaml
```

肉眼確認輸出 .d2 的節點數量符合 yaml 設定。特別確認 `L1` 容器內子群組的宣告順序：`gw` 必須第一個。

**Step 4：執行 D2 render**

```bash
d2 output.d2 diagram_raw.svg
```

確認 diagram_raw.svg 存在且可在瀏覽器開啟，無 XML 錯誤。

**Step 5：執行 SVG 後製**

```bash
python optimize_svg.py --input diagram_raw.svg
```

確認：Title Bar 存在（y=0~110）；Legend 在左上角空白區域；連線 label 有白底。

**Step 6：執行碰撞檢查**

```bash
python check_collision.py diagram_final.svg
```

a_class < 5 為可接受，= 0 為優秀。

**Step 7：（如需）調整並重新產圖**

如果 a_class ≥ 5，根據碰撞報告調整 yaml，重回 Step 3。常見調整：
- 調整 feeder_groups 順序（影響 edge switch 水平位置）
- 將特定設備的 `connected_to` 設為 `null`（省略長線）

**Step 8：存檔歸檔**

依命名規則存入專案資料夾。更新 `project.yaml` 的 `project.rev`。

### 10.2 元件庫更新流程

1. 收到新設備資訊（採購確認書 / 型錄）
2. 在 `component_library.yaml` 新增元件 block，填寫全部欄位
3. 確認 `d2_class` 對應正確（查 3.3 類別清單）
4. 確認 `protocols` 在 `project_template.yaml` 的 `comm_styles` 有對應定義
5. 測試：以最近一個專案的 `project.yaml` 重新執行 `gen_d2.py`，確認無報錯
6. 更新 DOC-03 版本號（至少 PATCH）
7. 同步更新 DOC-05（project_template.yaml）版本號

### 10.3 Rulebook 更新流程

觸發條件：a_class ≥ 5；發現新的 D2/dagre 行為限制；找到更好的拓撲排列方式。

1. 在已知缺陷章節（第 9 章）記錄問題症狀、影響版本、防禦方式
2. 如已找到根本原因，新增對應的 RULE
3. 更新版本號（新增 RULE → MINOR；新增 PATTERN/KB → PATCH）
4. 在本文件的版本歷史（第 12 章）新增一行記錄

---

## 11. Claude Code Prompt 庫

### 11.1 工具建立 Prompt（首次使用）

用此 Prompt 讓 Claude Code 建立完整工具鏈（三個檔案）：

```
你的任務是建立 OT 架構圖自動產生工具鏈，輸出以下三個檔案：

【gen_d2.py】
完整實作所有 gen_* 函式，嵌入完整的 CLASSES_BLOCK 常數（從 scada_level1_template_v2.d2
的 classes: {} 區塊直接複製）。

必須實作以下 Rulebook 規則：
  T-01 PRP 備援開關      T-02 HMI 備援開關     T-03 Gateway 備援
  T-04 L1 子群組 gw 第一 T-05 骨幹 label 去重  T-06 null 連線跳過
  T-07 L4 可選           T-08 STATCOM 可選

關鍵規則 T-04：L1 Zone 內子群組宣告順序永遠是 gw → rtu_panels → mcc → statcom，
不論 project.yaml 中的順序如何，gen_d2.py 輸出時必須強制此順序。

【optimize_svg.py】
實作 R-PP-01 的八步驟後製流程，包含：
  fix_dasharray()  inject_title_bar()  find_empty_zone()  inject_legend()
  add_label_backgrounds()

Legend 位置必須動態偵測（find_empty_zone），不得硬編碼座標。

【project_template.yaml】
完整的空白專案模板，所有欄位保留，加入中文 inline 說明。

完成後以附件的 project.yaml 執行完整測試，
確認 T-04（gw 在 L1 第一）、T-05（骨幹 label 只有第一條）均正確。
```

### 11.2 新架構圖生成 Prompt

有現成工具後，用此 Prompt 產出新專案架構圖：

```
你是 OT 架構圖生成工程師，工具鏈已就位（gen_d2.py / optimize_svg.py）。

作業流程：
1. 驗證附件 project.yaml 的必填欄位完整性（validate_config）
2. python gen_d2.py project.yaml
3. d2 output.d2 diagram_raw.svg
4. python optimize_svg.py --input diagram_raw.svg
5. python check_collision.py diagram_final.svg
6. 若 a_class >= 5，根據碰撞報告調整 yaml，重新執行 Step 2
7. 輸出 diagram_final.svg 並附上碰撞報告（a_class 數量 + 受影響節點列表）

違反任何 🔴 RULE 時，必須在輸出前修正，不可跳過。
特別注意：
  R-D2-03（L1.gw 必須是第一個子群組）
  R-D2-05（L0 子群組順序必須對應 L1）
  R-D2-06（骨幹 label 只保留第一條）
```

### 11.3 SVG 獨立後製 Prompt

已有 diagram_raw.svg，僅執行後製優化時使用：

```
執行 diagram_raw.svg 的 SVG 後製優化（八步驟，依序執行）：

Step 1  P1-A：連線 label 白底遮罩
        識別條件：text 包含通訊協定關鍵字（PRP/IEC/IEEE/Modbus/RS-485/Fiber 等）
        遮罩規格：fill=white, fill-opacity=0.85, rx=2
Step 2  P1-B：Zone 標題白底遮罩
        識別條件：開頭為 "Level N｜" 的 text
Step 3  P2：骨幹 PRP label 去重
        範圍：y=1300~1730，每種文字只保留 x 值最大的一個（最右側）
Step 4  P3：Legend 移至左上角空白區域
        自動掃描落點（不硬編碼座標）
        規格：480×314px，雙欄，標題列深藍，font-size=11
Step 5  P4：移除頁尾 Legend，更新 viewBox height

輸出 diagram_optimized.svg，驗證 checklist：
□ Legend 完整可讀（10 項元件 + 7 種連線）
□ 連線 label 有白底遮罩，不被線條壓蓋
□ viewBox height 已縮減
□ SVG 為有效 UTF-8 XML，瀏覽器可直接開啟
```

### 11.4 Prompt 版本歷史

| 版本 | 日期 | 主要變更 |
|------|------|---------|
| v1.0 | 2026-03-04 | 品牌色第一版，ELK layout，title/legend 使用 D2 節點 |
| v2.0 | 2026-03-04 | 改為 dagre layout，移除 D2 title/legend，後製腳本加入 |
| v3.0 | 2026-03-04 | 加入碰撞鑑識結果，Legend 改為嵌入浮層，加入白底遮罩 |
| v3.1 | 2026-03-04 | 加入拓撲 Rulebook（T-01~T-08），gen_d2.py 設計規格 |

---

## 12. 版本歷史與更新機制

### 12.1 框架版本歷史

| 版本 | 日期 | 類型 | 主要變更 | 觸發事件 |
|------|------|------|---------|---------|
| v1.0 | 2026-03-04 | MAJOR | 框架初版建立，整合以下所有既有文件：OT架構圖標準說明\_v1.0、OT\_Diagram\_Rulebook\_v1.0、OT\_Diagram\_Generator\_Design、ANALYSIS\_diagram\_optimization\_v2；建立五層架構（文件制度 / 元件庫 / 工具鏈 / Rulebook / SOP） | diagram\_final.svg 鑑識分析完成，24 A 類 + 44 B 類碰撞問題全部歸類 |

### 12.2 下一版預定更新項目

| 優先級 | 項目 | 類型 | 預期版本 |
|--------|------|------|---------|
| 🔴 P1 | gen_d2.py 完整實作（所有 gen_* 函式） | 工具 | v1.1 |
| 🔴 P1 | optimize_svg.py 完整實作（八步驟後製） | 工具 | v1.1 |
| 🟠 P2 | check_collision.py 實作（A 類碰撞快速檢查） | 工具 | v1.1 |
| 🟠 P2 | component_library.yaml 初始資料填充（現有設備清單） | 資料 | v1.2 |
| 🟡 P3 | Makefile / pipeline 腳本 | 工具 | v1.2 |
| 🟡 P3 | DWG-L2 網路安全圖模板 | 模板 | v1.3 |
| 🟢 P4 | DWG-L3 拓撲圖模板（含 IP/Port 欄位） | 模板 | v2.0 |
| 🟢 P4 | 多專案批次產圖腳本 | 工具 | v2.0 |

### 12.3 自我檢驗 Checklist

每次產出新架構圖後，逐項確認：

**D2 源碼自我檢查**
- [ ] vars.d2-config.layout-engine 設為 dagre
- [ ] 沒有 title: 節點，沒有 legend: 節點
- [ ] 所有子群組使用 class: zone_sub（無硬編碼色）
- [ ] 所有連線使用 inline style，無 class 引用
- [ ] 所有連線 label 無 \n 換行字元
- [ ] 扇形骨幹連線（一對多）：同方向只有第一條保留 label
- [ ] L1 子群組宣告順序：gw → rtu_panels → mcc → statcom
- [ ] L0 子群組宣告順序：r_group 在前（左）、solar 在後（右）
- [ ] 長線檢查：兩端子群組宣告順序差距 ≤ 2

**SVG 後製自我檢查**
- [ ] Title Bar 存在於 y=0~110，背景 #0C3467，左側 6px 天藍條
- [ ] Legend 為浮層（非頁尾），位於圖面空白區域
- [ ] Legend 文字可讀（font-size ≥ 11px，無縮放）
- [ ] 頁尾 Legend 已移除，畫布高度已縮減
- [ ] 所有 stroke-dasharray 無超過 8 的值
- [ ] 所有連線 label 有白底遮罩
- [ ] 畫布寬度合理（≤ 7000px）
- [ ] 輸出為 UTF-8 編碼 SVG，瀏覽器可直接開啟

---

*本文件維護於：DOC-01*
*對應工具：gen\_d2.py / optimize\_svg.py / check\_collision.py*
*對應資料：component\_library.yaml / project\_template.yaml*
