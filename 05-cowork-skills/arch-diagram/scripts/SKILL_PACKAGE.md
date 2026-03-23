# OT 架構圖自動化產圖 — Skill 整合包

> **用途**：本文件為 Skill Agent 製作 Claude Code Skill 的完整素材包。
> 包含工具鏈全貌、所有規則、程式碼、YAML 結構、使用範例。
> Skill Agent 應根據本文件內容建立一個可被使用者透過 `/ot-diagram-gen` 叫用的 Skill。

---

## 一、專案概覽

### 1.1 解決的問題

OT（營運科技）工程師需要繪製符合 IEC 62443 / Purdue Model 的系統架構圖。
傳統方式需要手動修改 D2 源碼，耗時且容易出錯。

本工具鏈讓工程師只需填寫一份 `project.yaml`（不需要懂 D2 語法），
執行 4 個指令即可得到一份完整的 SVG 架構圖。

### 1.2 三層分離架構

```
Layer 1  PROJECT CONFIG (project.yaml)        ← 工程師只填這份
Layer 2  COMPONENT LIBRARY (component_library.yaml)  ← 設備標準定義
Layer 3  CODE GENERATOR (gen_d2.py)           ← 套用 Rulebook，輸出 D2
Layer 4  RENDER (d2 CLI, dagre layout)        ← D2 官方渲染
Layer 5  POSTPROCESS (optimize_svg.py)        ← Title Bar / Legend / 遮罩
```

### 1.3 版本資訊

- 版本：v1.0.2（2026-03-04 發布）
- 狀態：全 25 個任務完成，0 Critical / 0 Major 缺陷
- 已驗證專案：3 個（project_test / project_substation / project_icp_lab）

---

## 二、工具鏈檔案位置

### 正式發布目錄（優先使用）
```
c:/Users/victor.liu/OneDrive - Intelligent Cloud Plus Corp/文件/工作區/TEST/架構圖分析/project_root/05_release/
```

### 開發工作目錄（備用）
```
c:/Users/victor.liu/OneDrive - Intelligent Cloud Plus Corp/文件/工作區/TEST/架構圖分析/project_root/03_work/
```

### 規格文件
```
c:/Users/victor.liu/OneDrive - Intelligent Cloud Plus Corp/文件/工作區/TEST/架構圖分析/project_root/00_inbox/OT_Architecture_Framework_v1.0.md
```

### 核心檔案清單

| 檔案 | 行數 | 用途 |
|------|------|------|
| `gen_d2.py` | 1,152 | YAML → D2 源碼產生器（CLI） |
| `optimize_svg.py` | 820 | SVG 8 步驟後製腳本（CLI） |
| `check_collision.py` | 270 | A 類碰撞快速檢查（CLI） |
| `component_library.yaml` | 541 | 設備元件庫（34 個標準設備） |
| `project_template.yaml` | 272 | 空白專案模板（含 inline 中文說明） |
| `run.sh` | 71 | 一鍵 pipeline（bash 版） |
| `Makefile` | — | 一鍵 pipeline（make 版） |

### 系統需求

| 項目 | 最低版本 |
|------|---------|
| Python | 3.9+ |
| d2 CLI | 0.6.0+ |
| PyYAML | 5.0+ (`pip install pyyaml`) |

---

## 三、Pipeline 完整流程

### 3.1 一鍵執行

```bash
cd "$TOOLCHAIN_DIR"
bash run.sh <project.yaml> <output_name>
# 輸出: <output_name>_final.svg
```

### 3.2 分步驟執行

```bash
cd "$TOOLCHAIN_DIR"

# Step 1: 產生 D2 源碼
python gen_d2.py project.yaml --output diagram.d2 --library component_library.yaml

# Step 2: D2 render
d2 diagram.d2 diagram_raw.svg

# Step 3: SVG 後製
python optimize_svg.py --input diagram_raw.svg --output diagram_final.svg --project project.yaml

# Step 4: 碰撞檢查
python check_collision.py diagram_final.svg
```

### 3.3 其他指令

```bash
# 僅驗證 YAML（不產圖）
python gen_d2.py project.yaml --dry-run

# 使用 Makefile
make all PROJECT=project.yaml SVG_FINAL=diagram_final.svg
make validate PROJECT=project.yaml   # 僅驗證
make clean                            # 清除產出物
```

---

## 四、project.yaml 完整欄位規格

### 4.1 頂層結構

```yaml
project:           # 專案基本資訊（Title Bar 文字來源）
scada:             # L3 SCADA 監控站（HMI, Historian, NTP, UPS）
dmz:               # DMZ 邊界防護（防火牆, 遠端存取）
enterprise:        # L4 企業層（可選，enabled: true/false）
network:           # L2 控制網路（PRP 開關, feeder_groups 動態展開）
field_control:     # L1 現場控制（gateways, rtu_panels, statcom）
field_devices:     # L0 現場設備（protection_ieds, solar_storage）
comm_styles:       # 通訊方式樣式庫（集中定義，設備只引用 key）
```

### 4.2 project 區塊

```yaml
project:
  name: "專案名稱"           # Title Bar 主標題
  site: "場站名稱"           # Title Bar 副標題
  client: "客戶代碼"         # 檔案命名用，例：TPC
  site_code: "場站代碼"      # 檔案命名用，例：HSUEH
  rev: "1.0"                # 圖面版次
  date: "2026-03-04"        # 圖面日期
  standard: "IEC 62443"     # Title Bar 適用標準
  zone_labels:              # 可選：自訂 Zone 容器標籤
    l4: "Level 4 — Enterprise Zone"
    dmz: "DMZ｜非軍事化區"
    l3: "Level 3 — Supervisory Zone"
    l2: "Level 2 — Control Network"
    l1: "Level 1 — Field Control"
    l0: "Level 0 — Field Devices"
```

### 4.3 scada 區塊（L3）

```yaml
scada:
  hmi_count: 2              # 1=單機, 2=主備（T-02）
  hmi_model: "DA-820"       # 空字串=不顯示型號
  hmi_redundancy: true
  hmi_labels:               # 可選：自訂 HMI 顯示標籤
    hmi_a: "主站 HMI_A"
    hmi_b: "備援 HMI_B"
  historian: true
  historian_model: ""
  hmi_ws: false             # 可選：HMI 監控桌
  hmi_ws_model: ""
  engineering_ws: true
  engineering_ws_model: ""
  ntp: true
  ntp_model: "IEEE 1588 PTP"
  gnss: true                # GNSS 天線（ntp=true 時有效）
  ups_l3: true
  ups_l3_capacity: "10kVA"
```

### 4.4 dmz 區塊

```yaml
dmz:
  firewall_model: "EDR-GN010"
  l3_switch_model: "PT-G7728"
  remote_access: true
  remote_type: "PSTN+4G"   # "PSTN+4G" | "4G" | "PSTN" | "RF"
  modem_model: ""           # 空白=依 remote_type 自動填寫
```

### 4.5 enterprise 區塊（L4，可選）

```yaml
enterprise:
  enabled: true             # false=省略整個 L4（T-07）
  erp: true
  adcc: true
  scada_ws: true
```

### 4.6 network 區塊（L2）

```yaml
network:
  prp_enabled: true         # false=單網（T-01）
  core_switch_model: ""
  feeder_groups:            # 每個 block 產生 L2 edge switch 對 + L1 MCC
    - id: "F1"             # 唯一 ID
      label: "F1"          # 圖面標籤
      description: "161kV TR"
      mcc_panels: "16/17"
    - id: "F2"
      label: "F2"
      description: "69kV TR"
      mcc_panels: "18/19"
```

### 4.7 field_control 區塊（L1）

```yaml
field_control:
  gateways:
    enabled: true
    count: 2                # 1=單 GW, 2=雙 GW（T-03）
    model: "IEC-7442"
    zone: "l1"              # "l1"（預設）或 "l3"（GW 在 L3 層）
    gw_labels:              # 可選：自訂 GW 顯示標籤
      gw_a: "GW_A"
      gw_b: "GW_B"
    protocol_conversion:
      - "IEC61850 → Modbus RTU"

  rtu_panels:               # 可多個 RTU 盤
    - id: "TPC"
      label: "TPC RTU 盤"
      rtu_model: "RSG-007R"
      redbox: true          # PRP 橋接器（prp_enabled=false 時忽略）
      ieds:                 # 掛在此 RTU 盤下的 IED
        - id: "IED_87L1"
          label: "87L1\n線路保護"
          protocol: "IEC61850"
      connected_to_feeder: "F1"   # 對應 feeder_groups id

  statcom:
    enabled: false          # T-08
    osc_model: "BPX-B1"
    module_count: 3
    protocol: "Modbus TCP"
```

### 4.8 field_devices 區塊（L0）

```yaml
field_devices:
  protection_ieds:
    enabled: true
    group_label: "R 群（保護電驛 IED）"
    ieds:
      - id: "IED_87T"
        label: "87T1\n變壓器差動保護"
        comm: "IEC61850_fiber"       # 引用 comm_styles key
        connected_to: "gw_A"        # "gw_A"|"gw_B"|"rtu_[id]"|null（T-06）

  pmcc_ieds:                         # 可選：PMCC IED 群
    enabled: false
    group_label: "PMCC IED 群"
    ieds: []

  solar_storage:
    enabled: false
    group_label: "太陽能 / 儲能設備"
    devices:
      - id: "INV1"
        label: "逆變器 #1"
        type: "inverter"             # "inverter"|"plc"|"gateway"|"ups"
        comm: "Modbus_TCP"
        connected_to: "mcc_F1"      # "gw_A"|"gw_B"|"mcc_[id]"|null
```

### 4.9 comm_styles 區塊

```yaml
comm_styles:
  PRP_LAN_A:
    label: "PRP LAN-A"
    stroke: "#008EC3"       # R-BR-01 色碼
    stroke_width: 2
    stroke_dash: 0          # 0=實線, >0=虛線（D2 會乘以 stroke_width）
```

**必要的 13 個 keys**（validate_config 會驗證）：
`PRP_LAN_A`, `PRP_LAN_B`, `OPC_UA_A`, `OPC_UA_B`, `IEEE1588_A`, `IEEE1588_B`,
`IEC61850_MMS`, `IEC61850_fiber`, `PRP_fiber_A`, `PRP_fiber_B`,
`Modbus_TCP`, `RS485_modbus`, `IT_ethernet`

**可選 keys**（依專案需求）：
`VPN_PSTN`, `RF_wireless`, `RS485`, `IRIG_B`, `DNP3_PSTN`, `DNP3_IEC104`

### 4.10 欄位快速對照

| 我想要的效果 | 改哪個欄位 | 設定值 |
|------------|-----------|--------|
| 只有單台 HMI | `scada.hmi_count` | `1` |
| 不做 PRP 雙網 | `network.prp_enabled` | `false` |
| 增加饋線迴路 | `network.feeder_groups` | 加一個 block |
| 新增保護電驛 | `field_devices.protection_ieds.ieds` | 加一個 block |
| 省略某條長線 | 該設備的 `connected_to` | `null` |
| 不畫 L4 | `enterprise.enabled` | `false` |
| 去掉 STATCOM | `field_control.statcom.enabled` | `false` |
| Gateway 改單台 | `field_control.gateways.count` | `1` |
| 新增通訊方式 | `comm_styles` | 加新 key |

---

## 五、Rulebook 完整規則

### 5.1 拓撲規則（T-01 ~ T-08）

| ID | 名稱 | 觸發條件 | 行為 |
|----|------|---------|------|
| T-01 | PRP 備援開關 | `prp_enabled: false` | 單網，每個 feeder 只有 SW_A，RTU 盤無 REDBOX |
| T-02 | HMI 備援 | `hmi_count: 1` | 只產生 HMI_A |
| T-03 | Gateway 備援 | `gateways.count: 1` | 只有 GW_A |
| T-04 | **L1 子群組順序（最關鍵）** | 永遠套用 | 宣告順序強制：**gw → rtu_panels → mcc → statcom** |
| T-05 | 骨幹 label 去重 | 永遠套用 | LAN-A/LAN-B 各自只有第一條保留 label |
| T-06 | null 跳過連線 | `connected_to: null` | 完全不產生連線宣告 |
| T-07 | L4 可選 | `enterprise.enabled: false` | 省略 L4 Zone + 所有 L4↔DMZ 連線 |
| T-08 | STATCOM 可選 | `statcom.enabled: false` | 省略 STATCOM 子群組 |

**T-04 為何最關鍵**：dagre 在 `direction: down` 下依宣告順序從左到右排列子群組。
`gw` 必須第一個（最左側）才能靠近 `L0.r_group`，否則 3 條光纖線會橫穿整個 L0 區域（1700px 長線穿越所有 IED 節點）。

### 5.2 D2 語法規則（R-D2-01 ~ R-D2-11）

| ID | 等級 | 規則 |
|----|------|------|
| R-D2-01 | 🔴 | 永遠使用 dagre layout，禁止 ELK |
| R-D2-02 | 🔴 | 禁止在 D2 中宣告 title:/legend: 節點 |
| R-D2-03 | 🔴 | 子群組宣告順序決定水平排列 |
| R-D2-04 | 🔴 | 跨 Zone 長線兩端須宣告在同一側 |
| R-D2-05 | 🔴 | L0 r_group 在前（左），solar 在後（右） |
| R-D2-06 | 🟠 | 骨幹連線重複 label 除第一條外全部置空 |
| R-D2-07 | 🟠 | 省略語意上不必要的長線（connected_to: null） |
| R-D2-08 | 🔴 | 所有子群組使用 class: zone_sub，禁止硬編碼顏色 |
| R-D2-09 | 🔴 | 連線使用 inline style，禁止 connection class |
| R-D2-10 | 🔴 | 連線 label 禁止 `\n`，用兩空格替代 |
| R-D2-11 | 🟠 | stroke-dash 設定值 × stroke-width = SVG 實際 dasharray |

### 5.3 SVG 後製規則（R-PP-01 ~ R-PP-06）

| ID | 等級 | 規則 |
|----|------|------|
| R-PP-01 | 🔴 | 8 步驟固定順序：parse → remove_artifacts → shift(+110) → fix_dash → title_bar → legend → label_bg → update_canvas |
| R-PP-02 | 🔴 | Title Bar：110px 高, #0C3467 背景, 左側 6px #008EC3 裝飾條, 三行文字 |
| R-PP-03 | 🔴 | Legend 為浮層（非頁尾），雙欄設計，動態定位 |
| R-PP-04 | 🔴 | stroke-dasharray > 8 修正為 6,4 |
| R-PP-05 | 🔴 | 所有連線 label 必須有白底遮罩 (fill-opacity=0.85) |
| R-PP-06 | 🟠 | Legend 位置以 30px 步進掃描空白區域，不硬編碼座標 |

### 5.4 品牌色碼（R-BR-01）

| 色名 | HEX | 用途 |
|------|-----|------|
| Navy Primary | `#0C3467` | L4/L2 Zone、LAN-B、IEC 61850 光纖、Title Bar 背景 |
| Sky Blue | `#008EC3` | L3 Zone、HMI/Switch PRP、LAN-A、Title Bar 裝飾條 |
| Amber | `#F5A623` | L1 Zone、Gateway/RTU/IED、VPN/RF |
| Gray | `#9B9B9B` | L0 Zone、Field IED、IT/RS-485 |
| Red | `#c0392b` | 防火牆（固定色） |
| Green | `#2e7d32` | L2 Control Network Zone |

**Zone 背景淡色**：L4=#e8eef5, DMZ=#fdecea, L3=#e0f4fb, L2=#e8f5e9, L1=#fff8e1, L0=#f5f5f5

### 5.5 已知缺陷（KB-01 ~ KB-06）

| ID | 問題 | 因應 |
|----|------|------|
| KB-01 | D2 的 title/legend 節點位置不可控 | 禁用 D2 title/legend，改由 optimize_svg.py 後製注入 |
| KB-02 | stroke-dash 值被乘以 stroke-width | optimize_svg.py 的 fix_dasharray() 修正 |
| KB-03 | ELK 產生 SVG S-curves | 禁用 ELK，強制 dagre |
| KB-04 | dagre > 3 層嵌套不穩定 | 限制嵌套層數 |
| KB-05 | 連線 label 中 \n 在 SVG 被忽略 | 改用兩空格分隔 |
| KB-06 | dagre 長線穿越節點 bounding box | check_collision.py 檢測 + 調整拓撲 |

---

## 六、gen_d2.py 函式架構

### 6.1 函式對照表

| 函式 | 職責 | 關聯規則 |
|------|------|---------|
| `zone_label(config, key, default)` | 自訂 Zone 標籤（向後相容） | — |
| `d2label(s)` | YAML → D2 字串安全轉換（\n 處理） | R-D2-10 |
| `build_classes_block()` | 19 個 D2 class 定義（色碼集中管理） | R-D2-08, R-BR-01 |
| `load_config(yaml, lib)` | 載入 project.yaml + 元件庫 | — |
| `validate_config(config)` | 驗證 connected_to / comm_styles 引用 | R-D2-04 |
| `gen_header(config)` | vars / direction / classes 區塊 | R-D2-01 |
| `gen_l4(config)` | L4 Enterprise Zone | T-07 |
| `gen_dmz(config)` | DMZ Zone | — |
| `gen_l3(config)` | L3 Supervisory Zone（3 子群組） | T-02 |
| `gen_l2(config)` | L2 Control Network（PRP 雙網） | T-01 |
| `gen_l1(config)` | L1 Zone（**強制排序**） | T-04 |
| `gen_l1_gw(config)` | Gateway 子群組 | T-03 |
| `gen_l1_rtu_panel(panel, prp)` | RTU 盤子群組 | T-01 |
| `gen_l1_mcc(feeders)` | MCC 群子群組 | — |
| `gen_l1_statcom(config)` | STATCOM 子群組 | T-08 |
| `gen_l0(config)` | L0 Zone（r_group 在前） | R-D2-05 |
| `resolve_target(target, config)` | YAML key → D2 節點路徑 | — |
| `emit_connection(src, dst, comm_key, styles)` | 輸出連線 D2 語法 | R-D2-09, R-D2-10 |
| `gen_conn_backbone(config)` | L2 骨幹 PRP 連線 | T-05, R-D2-06 |
| `gen_conn_inter_zone(config)` | 跨 Zone 骨幹連線 | — |
| `gen_conn_l0(config)` | L0 連線 | T-06 |
| `generate_d2(config)` | 組合完整 D2 源碼 | — |

### 6.2 D2 輸出順序

```
header → L4 → DMZ → L3 → L2 → L1 → L0 → conn_backbone → conn_inter_zone → conn_l0
```

### 6.3 D2 Classes 完整列表（19 個）

**Zone 容器**：zone_l4, zone_dmz, zone_l3, zone_l2, zone_l1, zone_l0, zone_sub

**L3 設備**：scada_server, hmi_workstation, historian, engineering_ws, ntp_server

**DMZ 設備**：firewall, data_diode, jump_server

**L2 設備**：switch_prp

**L1 設備**：gateway, redbox, rtu_ied, plc

**L0 設備**：field_ied, inverter, ups

**外部系統**：external_system

---

## 七、optimize_svg.py 函式架構

### 7.1 八步驟流程

| Step | 函式 | 職責 |
|------|------|------|
| 0 | — | 讀入原始 SVG |
| 1 | `parse_svg()` | 解析 viewBox bounding box |
| 2 | `remove_d2_artifacts()` | 正則移除 D2 殘留 title/legend group |
| 3 | `shift_content(+110px)` | 主圖元素向下位移（Title Bar 空間） |
| 4 | `fix_dasharray()` | dasharray > 8 → 6,4 |
| 5 | `inject_title_bar()` | 110px Navy 背景 + 3 行文字 |
| 6 | `find_empty_zone() + inject_legend()` | 動態掃描 + 雙欄 Legend 浮層 |
| 7 | `add_label_backgrounds_v2()` | 連線 label 白底遮罩 |
| 7b | `elevate_zone_titles()` | 容器標題 text halo（地圖學技法） |
| 7c | `displace_overlapping_labels()` | 連線 label 避讓容器標題 |
| 8 | `update_canvas()` | 更新 viewBox height |
| 8b | `set_paper_size()` | A1 橫向 841mm × 594mm |

### 7.2 Title Bar 規格（R-PP-02）

```
高度：110px，橫跨全畫布
背景：#0C3467（Navy）
左側裝飾條：x=0~6, height=110, fill=#008EC3（Sky Blue）
行 1：y=40, font-size=21, bold, white → 主標題
行 2：y=66, font-size=12, #93c5fd → 場站/版本/日期
行 3：y=88, font-size=10, #94a3b8 → "Purdue Model / ISA-95 / IEC 62443..."
```

### 7.3 Legend 規格（R-PP-03）

```
外框：white bg, opacity=0.95, stroke=#0C3467, rx=6, drop-shadow
標題列：height=30, fill=#0C3467, "圖例 / Legend"
雙欄：左=元件類型（9 種），右=連線類型（7 種）
每行：27px, font-size=11
位置：find_empty_zone() 30px 步進掃描，找不到則放底部
```

**Legend 元件類型**：
1. SCADA/Historian (rect, #0C3467)
2. HMI/NTP Server (rect, #008EC3)
3. 防火牆 Firewall (diamond, #c0392b)
4. Switch PRP (hexagon, #008EC3)
5. Protocol Gateway (hexagon, #F5A623)
6. RTU/IED (rect, #F5A623)
7. Field IED/ENG WS (rect, #9B9B9B)
8. RedBox (hexagon, #0C3467)
9. 外部系統 (rect, #9B9B9B, dashed)

**Legend 連線類型**：
1. IEC 61850 GOOSE Fiber (深藍粗實線)
2. PRP LAN-A / OPC-UA A (天藍實線)
3. PRP LAN-B / OPC-UA B (深藍虛線)
4. RS-485 / IT Ethernet (灰細虛線)
5. VPN / RF Wireless (琥珀虛線)
6. Modbus TCP (天藍細實線)
7. IRIG-B / IEEE 1588 (深藍實線)

---

## 八、check_collision.py 規格

### 8.1 碰撞定義

**A 類碰撞**：連線路徑穿越「葉節點」文字。

排除項目：
- Zone 容器標題（含 ｜ 分隔符或特定前綴）
- 連線 label（含 CONN_KEYWORDS）
- 路徑端點附近（25px 範圍內，視為合理連接）
- 路徑總長度 < 200px 的短連線

### 8.2 合格標準

| a_class | 狀態 | 圖示 | 說明 |
|---------|------|------|------|
| 0 | Green | ✅ | 優秀 |
| 1~4 | Yellow | ⚠️ | 可接受（建議調整） |
| ≥ 5 | Red | ❌ | 必須修正 |

### 8.3 碰撞修正策略

1. 調整 `feeder_groups` 順序（影響 L2 edge switch 水平位置）
2. 設定 `connected_to: null`（省略跨 Zone 長線）
3. 減少單一 RTU 盤下的 IED 數量，分散到多個盤

---

## 九、元件庫結構

### 9.1 YAML 結構

```yaml
components:
  - id: "SW-MOXA-EDS-408A"     # 格式：{類型}-{廠商}-{型號}
    category: SWITCH_PRP        # 設備類別
    vendor: "Moxa"
    model: "EDS-408A"
    display_name: "EDS-408A\nPRP Switch"
    d2_class: switch_prp        # 對應 gen_d2.py 的 CLASSES_BLOCK
    protocols: [PRP, RSTP, IEC61850, SNMP]
    ports:                      # 選填
      ETH_100M: 8
    redundancy: true            # 選填
    certifications: [IEC 62443-4-2]  # 選填
    notes: ""                   # 選填
    deprecated: false           # 選填
    superseded_by: ""           # deprecated=true 時必填
```

### 9.2 目前元件庫統計（v2.0，34 個設備）

| Purdue 層 | 數量 | 設備類別 |
|-----------|------|---------|
| L4 Enterprise | 3 | IT Switch, IT Firewall, ERP Server |
| DMZ | 5 | Firewall×2, Data Diode, VPN Router, Switch |
| L3 Supervisory | 6 | HMI, SCADA, Historian, NTP, ENG WS, UPS |
| L2 Control | 4 | Switch PRP×3, RedBox |
| L1 Field Control | 6 | Gateway×2, RTU×2, PLC, STATCOM |
| L0 Field Devices | 10 | IED×7, Meter, PMU, Inverter×2, UPS |

### 9.3 設備類別 → D2 Class 對照

| category | d2_class | 圖形 | 框線色 |
|----------|----------|------|--------|
| SCADA_SERVER | scada_server | 矩形 | Navy |
| HMI | hmi_workstation | 矩形 | Sky Blue |
| HISTORIAN | historian | 圓柱 | Navy |
| ENG_WS | engineering_ws | 矩形 | Gray |
| NTP_SERVER | ntp_server | 矩形 | Sky Blue |
| FIREWALL | firewall | 菱形 | Red |
| SWITCH_PRP | switch_prp | 六角形 | Sky Blue |
| DATA_DIODE | data_diode | 菱形 | Amber |
| GATEWAY | gateway | 六角形 | Amber |
| REDBOX | redbox | 六角形 | Navy |
| RTU | rtu_ied | 矩形 | Amber |
| PLC | plc | 矩形 | Sky Blue |
| IED_PROTECTION | field_ied | 矩形 | Gray |
| INVERTER | inverter | 矩形 | Amber 細框 |
| UPS | ups | 矩形 | Amber 細框 |
| EXTERNAL_SYS | external_system | 矩形 | Gray 虛線 |

---

## 十、Skill 建議結構

### 10.1 建議的 Skill 目錄

```
~/.claude/skills/ot-diagram-gen/
├── SKILL.md                    # 主指令檔
└── references/
    └── (可選參考檔)
```

### 10.2 建議的 SKILL.md frontmatter

```yaml
---
name: ot-diagram-gen
description: "OT 架構圖自動化產圖 — 從 YAML 產生 IEC 62443 / Purdue Model 架構 SVG 圖"
user-invocable: true
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Agent
---
```

### 10.3 Skill 應支援的使用情境

| 情境 | 觸發語 | 行為 |
|------|--------|------|
| 建立新專案 | "建新的 OT 架構圖" | 複製 template，引導填寫 YAML |
| 執行產圖 | "產圖" / "generate" | 執行完整 4 步驟 pipeline |
| 碰撞修正 | "碰撞太多" / "Red" | 引導調整 feeder_groups / connected_to |
| 查詢元件庫 | "有什麼設備" / "查元件" | 搜尋 component_library.yaml |
| YAML 驗證 | "驗證" / "validate" | 執行 --dry-run |
| 解釋架構 | "什麼是 Purdue" | 說明框架概念 |

### 10.4 互動流程建議

1. 先確認工具鏈目錄存在且檔案完整
2. 確認 d2 CLI 已安裝（`d2 --version`）
3. 詢問使用者想做什麼
4. 逐步執行，每步確認結果
5. 碰撞修正是迭代過程（可能多次 YAML→產圖）

---

## 十一、完整範例 project.yaml（變電所）

```yaml
project:
  name: "學甲 161kV 變電所 OT 系統架構圖"
  site: "學甲 Hsueh-Chia S/S"
  client: "TPC"
  site_code: "HSUEH"
  rev: "1.0"
  date: "2026-03-04"
  standard: "IEC 62443"

scada:
  hmi_count: 2
  hmi_model: "DA-820"
  hmi_redundancy: true
  historian: true
  historian_model: ""
  engineering_ws: true
  engineering_ws_model: "DHI6C400 / OMCRON"
  ntp: true
  ntp_model: "IEEE 1588 PTP"
  gnss: true
  ups_l3: true
  ups_l3_capacity: "10kVA"

dmz:
  firewall_model: "EDR-GN010"
  l3_switch_model: "PT-G7728"
  remote_access: true
  remote_type: "PSTN+4G"

enterprise:
  enabled: true
  erp: true
  adcc: true
  scada_ws: true

network:
  prp_enabled: true
  core_switch_model: ""
  feeder_groups:
    - { id: "M1", label: "M1", description: "161kV TR", mcc_panels: "16/17" }
    - { id: "M2", label: "M2", description: "161kV BPT / General", mcc_panels: "01/02/03" }
    - { id: "M3", label: "M3", description: "161kV LINE / TR", mcc_panels: "04/05/06" }
    - { id: "M4", label: "M4", description: "53.4kV MAIN / BPT", mcc_panels: "07/08/09/10" }
    - { id: "M5", label: "M5", description: "53.4kV STATCOM", mcc_panels: "11/12/13" }
    - { id: "M6", label: "M6", description: "23kV", mcc_panels: "14/15" }

field_control:
  gateways:
    enabled: true
    count: 2
    model: "IEC-7442 / Advantech"
    protocol_conversion:
      - "IEC61850 → Modbus RTU"
      - "IEC61850 → RS-485"
  rtu_panels:
    - id: "TPC"
      label: "TPC RTU 盤"
      rtu_model: "RSG-007R"
      redbox: true
      ieds:
        - { id: "IED_87L1", label: "87L1\n線路保護", protocol: "IEC61850" }
        - { id: "IED_87L2", label: "87L2\n線路保護", protocol: "IEC61850" }
        - { id: "IED_60BF", label: "60BF\n斷路器失效", protocol: "IEC61850" }
      connected_to_feeder: "M1"
  statcom:
    enabled: true
    osc_model: "BPX-B1"
    module_count: 3
    protocol: "Modbus TCP"

field_devices:
  protection_ieds:
    enabled: true
    group_label: "R 群（保護電驛 IED）"
    ieds:
      - { id: "IED_87T", label: "87T1 / 87T2\n變壓器差動保護", comm: "IEC61850_fiber", connected_to: "gw_A" }
      - { id: "IED_87B", label: "87B\n匯流排保護", comm: "IEC61850_fiber", connected_to: "gw_A" }
      - { id: "IED_87L", label: "87L\n線路差動保護", comm: "IEC61850_fiber", connected_to: "gw_B" }
      - { id: "IED_50BF", label: "50BF-1/2\n斷路器失效保護", comm: "RS485_modbus", connected_to: "rtu_TPC" }
      - { id: "IED_50S", label: "50/51-1/2\n過電流保護", comm: "RS485_modbus", connected_to: "rtu_TPC" }
      - { id: "IED_D7", label: "87D / 87D2\n其他差動保護", comm: "IEC61850_fiber", connected_to: "gw_A" }
  solar_storage:
    enabled: true
    group_label: "太陽能 / 儲能設備"
    devices:
      - { id: "INV_A", label: "Inverter 群 A\nDC → AC", type: "inverter", comm: "RS485_modbus", connected_to: "mcc_M4" }
      - { id: "INV_B", label: "Inverter 群 B\nDC → AC", type: "inverter", comm: "RS485_modbus", connected_to: "mcc_M5" }
      - { id: "DC_CHG", label: "DC CHARGE\n充放電系統", type: "plc", comm: "RS485", connected_to: "gw_B" }
      - { id: "RF_MOD", label: "RF Solar Module\n無線監測", type: "gateway", comm: "RF_wireless", connected_to: "gw_B" }
      - { id: "UPS_FIELD", label: "UPS（現場）\nSerial RS485", type: "ups", comm: "RS485_modbus", connected_to: null }

comm_styles:
  PRP_LAN_A:      { label: "PRP LAN-A",                stroke: "#008EC3", stroke_width: 2, stroke_dash: 0 }
  PRP_LAN_B:      { label: "PRP LAN-B",                stroke: "#0C3467", stroke_width: 2, stroke_dash: 3 }
  IEC61850_fiber:  { label: "IEC 61850 GOOSE  Fiber SM", stroke: "#0C3467", stroke_width: 3, stroke_dash: 0 }
  IEC61850_MMS:    { label: "IEC 61850 MMS",             stroke: "#008EC3", stroke_width: 2, stroke_dash: 0 }
  PRP_fiber_A:     { label: "PRP LAN-A  Fiber MM",       stroke: "#008EC3", stroke_width: 2, stroke_dash: 0 }
  PRP_fiber_B:     { label: "PRP LAN-B  Fiber MM",       stroke: "#0C3467", stroke_width: 2, stroke_dash: 3 }
  OPC_UA_A:        { label: "OPC-UA / ICCP  LAN-A",      stroke: "#008EC3", stroke_width: 2, stroke_dash: 0 }
  OPC_UA_B:        { label: "OPC-UA / ICCP  LAN-B",      stroke: "#0C3467", stroke_width: 2, stroke_dash: 3 }
  IT_ethernet:     { label: "Ethernet / OPC-UA",          stroke: "#9B9B9B", stroke_width: 1, stroke_dash: 3 }
  RS485_modbus:    { label: "RS-485  Modbus RTU",         stroke: "#9B9B9B", stroke_width: 1, stroke_dash: 3 }
  RS485:           { label: "RS-485",                     stroke: "#9B9B9B", stroke_width: 1, stroke_dash: 3 }
  Modbus_TCP:      { label: "Modbus TCP",                 stroke: "#008EC3", stroke_width: 1, stroke_dash: 0 }
  VPN_PSTN:        { label: "PSTN 備援 / RF",             stroke: "#F5A623", stroke_width: 1, stroke_dash: 4 }
  RF_wireless:     { label: "RF Wireless",                stroke: "#F5A623", stroke_width: 1, stroke_dash: 4 }
  IRIG_B:          { label: "IRIG-B / PPS  Fiber",        stroke: "#0C3467", stroke_width: 3, stroke_dash: 0 }
  IEEE1588_A:      { label: "IEEE 1588 PTP  LAN-A",      stroke: "#008EC3", stroke_width: 2, stroke_dash: 0 }
  IEEE1588_B:      { label: "IEEE 1588 PTP  LAN-B",      stroke: "#0C3467", stroke_width: 2, stroke_dash: 3 }
```

---

## 十二、已知限制

1. **SVG 後製依賴正規表達式解析**：不使用完整 XML 解析器，複雜嵌套可能有邊界情況
2. **碰撞檢查為靜態分析**：基於文字座標與 path 線段距離，不模擬 dagre 碰撞解算
3. **Legend 位置演算法**：極度密集的圖表可能 fallback 至底部
4. **僅支援 dagre layout**：ELK 禁用（KB-01, KB-03）
5. **D2 版本需 ≥ 0.6.0**
6. **Windows 環境需確保 UTF-8**（check_collision.py 已自動處理）

---

_本整合包產生於 2026-03-20，基於 OT 架構圖自動化工具鏈 v1.0.2。_
