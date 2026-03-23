# OT 架構圖工具鏈 — 開發經驗值與 Skill 優化素材

> **用途**：本文件彙整 F6 ONS 專案開發過程中累積的所有架構規則、教訓、程式碼修正、
> 命名規範。供 Skill Agent 製作/優化 Skill 時參考。

---

## 一、架構圖產出標準流程

### 1.1 Pipeline

```
project.yaml → gen_d2.py → .d2 → patch_all.py → d2 render → _raw.svg → optimize_svg.py → _final.svg → check_collision.py
```

### 1.2 多圖專案流程（如 F6 的 8 張圖）

```
1. 每個子系統建立獨立 project_f6_{name}.yaml
2. gen_d2.py 產出 f6_{name}.d2
3. patch_all_f6.py 統一修正所有 D2（協定標籤、中文清除、L4 節點替換）
4. d2 render → SVG
5. optimize_svg.py 後製（Title Bar + Legend + 白底遮罩）
6. check_collision.py 驗證（Yellow 以下可接受）
7. gen_pdf.py 合併為 PDF 提案書
```

---

## 二、IEC 62439-3 PRP 架構規則（最關鍵的教訓）

### 2.1 PRP 正確拓撲

```
         LAN-A (獨立實體網路)          LAN-B (獨立實體網路)
     ┌──────────────────────┐    ┌──────────────────────┐
     │ Core-A  Bay-A1  ...  │    │ Core-B  Bay-B1  ...  │
     └───┬───────┬──────────┘    └───┬───────┬──────────┘
         │       │                    │       │
         │    Port-A              Port-B      │
         │    ┌──┴──────────────────┴──┐      │
         │    │   DANP (7SJ82/6MD85)   │      │
         │    │   單一 MAC + 單一 IP    │      │
         │    └────────────────────────┘      │
```

### 2.2 關鍵規則

| 規則 | 說明 |
|------|------|
| **DANP 雙網** | 每個 PRP 設備有 2 個 Ethernet port，分別連 LAN-A 和 LAN-B 的 Bay Switch |
| **LAN 完全隔離** | LAN-A 和 LAN-B 之間**沒有任何** switch-to-switch 連線 |
| **RedBox vs DANP** | RedBox 是給非 PRP 設備的橋接器；SIPROTEC 5 是 DANP（原生 PRP），不需要 RedBox |
| **Switch 不需 PRP 感知** | PRP 的智慧在端點（DANP），Switch 是標準 Ethernet Switch |
| **SCADA Server 也是 DANP** | SCADA Server 需要雙 NIC + PRP driver，呈現單一邏輯介面 |
| **同一 MAC/IP** | DANP 的兩個 port 共用同一個 MAC 和 IP |

### 2.3 gen_d2.py 的 PRP 實作

```python
# gen_conn_inter_zone() — L2→L1 連線
# 當 prp=true 時，每個 Bay 產生 LAN-A + LAN-B 兩條連線
lines.append(emit_connection(f"L2.lana.SW_{feeder}_A", target_node, ...))
if prp:
    lines.append(emit_connection(f"L2.lanb.SW_{feeder}_B", target_node, ..., label=""))
```

### 2.4 常見錯誤

| 錯誤 | 正確 |
|------|------|
| ❌ L2→L1 只連 LAN-A | ✅ 必須同時連 LAN-A 和 LAN-B |
| ❌ IED 透過 BCU 上行 | ✅ IED 和 BCU 平行掛在 PRP Station Bus |
| ❌ IED 透過 RedBox 上行 | ✅ SIPROTEC 5 是 DANP，直接走 PRP |
| ❌ LAN-B 只顯示簡短名稱 | ✅ LAN-A 和 LAN-B 的 Bay Switch 描述必須一致 |
| ❌ 非 OT 設備掛 PRP 網路 | ✅ CCTV/ACS/TEL/PWR 走 Ethernet VLAN |

---

## 三、協定使用規範

### 3.1 OT 設備（走 IEC 61850 PRP）

| 設備 | 協定 | 出現圖面 |
|------|------|---------|
| Protection Relay (7SJ82/7UT86/7SL86/7SS85) | IEC 61850 GOOSE/MMS | PROT |
| BCU (6MD85) | IEC 61850 GOOSE/MMS | PROT |
| P850 電錶 | IEC 61850 MMS | PROT |
| SCADA Server (WinCC OA) | OPC-UA / IEC 104 | SCADA |
| GPS/PTP | IEEE 1588 PTP | PROT, SCADA |

### 3.2 IT 設備（走 Ethernet，不走 PRP）

| 設備 | 協定 | 出現圖面 |
|------|------|---------|
| IP Camera / NVR | Ethernet PoE | CCTV |
| ACS Panel / Card Reader | RS-485 / Ethernet | ACS |
| IP-PBX / IP Phone | SIP / Ethernet PoE | TEL |
| FortiAP WiFi | Ethernet / CAPWAP | TEL, SCADA |
| FortiAuthenticator | RADIUS / 802.1X | TEL |

### 3.3 BoP 設備（走 Modbus TCP）

| 設備 | 協定 | 出現圖面 |
|------|------|---------|
| SICAM A8000 RTU | Modbus TCP | SCADA, PWR |
| FAS / HVAC / EDG 狀態 | Modbus TCP (via RTU) | SCADA, PWR |
| DC/UPS/Battery 狀態 | Modbus TCP (via RTU) | PWR |

### 3.4 外部介面

| 連接對象 | 協定 | 說明 |
|---------|------|------|
| TPC 調度中心 | **DNP3** | 不是 IEC 104 |
| TPC PSTN 備援 | DNP3 PSTN | 撥接專線 |
| OSS/WTG 離岸 SCADA | IEC 60870-5-104 | 我方是 Client |
| Cloud DR 備份 | HTTPS / VPN | AWS/Azure |

---

## 四、設備命名規範（跨圖一致性）

### 4.1 gen_d2.py 的 `node_label` 欄位

| 圖面 | `node_label` 值 | 實際設備 |
|------|-----------------|---------|
| PROT | `"BCU"` | 6MD85 Bay Controller |
| CCTV | `"NVR"` | Network Video Recorder |
| ACS | `"ACS Panel"` | Access Control Panel |
| TEL | `"PBX"` | IP-PBX System |
| TPC | `"BCU"` + `"SPS"` | Bay Controller + SPS Controller |
| PWR | `"RTU"` | SICAM A8000（正確） |
| SCADA | `"RTU"` | SICAM A8000（正確） |
| Overview | `"BCU"` + `"RTU"` | 分別標示 |

### 4.2 跨圖標籤統一規則

| 設備 | 統一標籤 | 不要用 |
|------|---------|-------|
| WinCC OA SCADA Server | "WinCC OA Server x 2" | ❌ "SCADA Server x 2"（太通用） |
| FortiGate 防火牆 | 主圖："FortiGate 80F HA x 3" / 副圖："FortiGate (See DWG-SCADA)" | ❌ "OT Firewall"（缺型號） |
| FortiSwitch Core | "FortiSwitch 448E x 5" | ❌ "L3 Core Switch"（缺型號） |
| GPS 時間同步 | "GPS/PTP x 2 IRIG-B" | ❌ "NTP Server"（太通用） |
| Legend 中的 RTU 圖示 | "BCU / RTU / IED" | ❌ "RTU / IED"（缺 BCU） |
| Legend 中的 RedBox 圖示 | "DANP (PRP Dual-NIC)" | ❌ "RedBox" |

### 4.3 中文清除規則

所有圖面標籤必須為英文。以下中文需在 patch 階段清除：

| 原文 | 替換為 |
|------|--------|
| `輔助設備` | `Auxiliary` |
| `SCADA 伺服器群` | 依圖面語境（`SCADA / HMI`、`VMS / SCADA Integration` 等） |
| `HMI 及監控桌` | 移除 |
| `MCC 群` | 依語境（`RCP Panel`、`PoE Switch`、`Bay LV Panel` 等） |
| `Gateway 責任分界點` | `Offshore SCADA Client` |
| `LAN-A（IEC 62439-3 獨立實體網路）` | `LAN-A (IEC 62439-3)` |

---

## 五、Purdue Model 分層規則

### 5.1 設備歸屬

| Purdue Level | 設備類型 | 注意事項 |
|-------------|---------|---------|
| **L4** | TPC SCADA、ADCC、OSS/WTG、O&M Centre、Cloud DR | 外部系統，用虛線框 |
| **DMZ** | FortiGate、FortiNDR、FortiAnalyzer、VPN Gateway | IEC 62443-3-2 |
| **L3** | WinCC OA Server、HMI OWS、Historian、NMS、ENG WS、GPS/PTP、UPS、SCADA Client | 所有 SCADA 級設備 |
| **L2** | FortiSwitch Core/Edge、PRP LAN-A/LAN-B | 網路基礎設施 |
| **L1** | BCU (6MD85)、Protection Relay、P850 Meter、RCP Panel、RTU、NVR、ACS Panel | **平行掛 PRP**，不是階層關係 |
| **L0** | GIS、Main TR、VSR、HF、CT/VT、Switchgear | 一次設備（Process I/O） |

### 5.2 L0 佈局規則

- L0 設備必須有 `connected_to` 連線到 L1，否則 dagre 會把 L0 排到圖面最上方
- 安防/電信/電源設備若不走 OT 網路，仍需連到對應的 L1 節點（NVR、ACS Panel、PBX、RTU）

### 5.3 SPS 特殊規則

- SPS 是 **Curtailment（降載）**控制器，不是 UFLS/UVLS（那是負載端概念）
- SPS 的降載對象是 **WTG SCADA + ONS PCC CB**（我方設備），不是 TPC 的 CB/DS/ES
- SPS 降載目標放在 **L1**（和 SPS Controller 平行），不是 L0（TPC-side Equipment）

---

## 六、optimize_svg.py 後製規則

### 6.1 Legend 位置策略

| 畫布寬度 | 策略 | Legend 位置 |
|---------|------|-----------|
| ≥ 6000px | 嵌入圖內空白 | `find_empty_zone()` 掃描 |
| < 6000px | 右側延伸 | `x = canvas_w + 30, y = TITLE_HEIGHT//2 + 30` |

### 6.2 Title Bar 延伸條

- 右側延伸時，畫一條 `TITLE_HEIGHT // 2` (55px) 高的深藍色條銜接 Legend
- 不要和 Title Bar 一樣高（110px），會看起來太粗
- 不要太細（4px），會看起來不協調

### 6.3 SVG `&` 跳脫

- YAML 中 project name 含 `&` 時，`inject_title_bar()` 會產生無效 XML
- 解法：YAML 中用 `+` 取代 `&`，或在 inject 時用 `&amp;`

---

## 七、gen_pdf.py PDF 提案書規則

### 7.1 架構

```
Stage 1: reportlab → 文字頁面 PDF（封面、目錄、Legend 頁、章節標題、附錄）
Stage 2: d2 CLI → 架構圖 PDF（向量圖，不經 optimize_svg.py）
Stage 3: pypdf → 合併（文字頁 + 架構圖交錯，架構圖上疊加 Title Bar overlay）
```

### 7.2 Legend 策略

- ❌ 不要疊加在架構圖頁面上（會和圖面內容重疊，z-order 問題）
- ✅ Legend 作為獨立頁面，放在 TOC 之後、第一章之前

### 7.3 架構圖頁面

- 使用 d2 CLI 直接產 PDF（向量圖，不跑版）
- 用 reportlab canvas overlay 疊加 Title Bar（章節名稱 + 文件資訊）
- d2 產的 PDF 頁面尺寸不固定，由圖面內容決定

### 7.4 不可行方案記錄

| 方案 | 問題 |
|------|------|
| svglib 解析 SVG | D2 的 CSS selector 太複雜，解析失敗 |
| cairosvg 轉 PNG | Windows 缺 Cairo 系統庫 |
| Chrome headless print-to-pdf | 頁面跑版、加日期浮水印 |
| Legend 疊加在 d2 PDF 上 | 不同頁面尺寸導致 Legend 位置不一致 |

---

## 八、patch_all_f6.py 設計模式

### 8.1 架構

```python
patch_common(s)      # 所有圖面共用（中文清除、LAN 標籤、MCC 前綴）
patch_non_ot(s)      # CCTV/ACS/TEL/PWR 專用（去 PRP、去 IEC 61850）
patch_{name}(path)   # 每張圖的專屬修正（L4 節點、協定標籤、MCC 命名）
```

### 8.2 L4 節點替換模式

gen_d2.py 固定產生 `ERP`、`ADCC`、`SCADA_WS` 三個 L4 節點。
每張圖的 patch 函式替換為實際的外部系統：

| gen_d2.py 預設 | PROT | SCADA | TPC | Overview |
|---------------|------|-------|-----|---------|
| ERP | TPC Grid | OSS SCADA | TPC SCADA DNP3 | TPC SCADA |
| ADCC | OSS+WTG | Cloud DR | (刪除) | ADCC/CDCC |
| SCADA_WS | (刪除) | F6 O&M Centre | (刪除) | F6 O&M Centre |

### 8.3 連線刪除 regex

刪除 L4 節點的連線時，必須匹配 4-5 行（連線宣告 + 3 style 行 + closing `}`）：
```python
s = re.sub(r'L4\.ADCC[^\n]*\n(?:[^\n]*\n){3,4}', '', s)
```
不能只匹配 4 行，否則會留下 orphan `}` 導致 D2 compile error。

---

## 九、check_collision.py 品質標準

| 碰撞等級 | a_class | 可接受？ | 說明 |
|---------|---------|---------|------|
| Green | 0 | ✅ 最佳 | 無碰撞 |
| Yellow | 1-4 | ✅ 可接受 | 通常是子群組標題被穿越 |
| Red | ≥5 | ❌ 必須修正 | 需要調整拓撲結構 |

### 碰撞修正策略

1. 減少 L0 PRP 直連線（改為 L1→L0）
2. 合併 feeder_groups（減少 L2 edge switch 數量）
3. 設定 `connected_to: null`（省略長線）
4. 調整子群組宣告順序（影響 dagre 水平排列）

---

## 十、CBOM 對齊規則

### 10.1 設備數量必須可追溯

每個架構圖的設備節點標籤必須包含 **型號 + 數量**，可直接對照 CBOM：

```
"7SL86 x 8\n87L Line Diff (M+B)"  →  CBOM-H101 (7SL86, Qty 8)
"FortiSwitch 124F x 22"           →  CBOM-H401 (8) + H402 (5) + ... = 22
```

### 10.2 CBOM 進版時的更新流程

1. 讀取新版 CBOM，和目前圖面數量比對
2. 修改 YAML 中的設備數量標籤
3. 修改 patch_all.py 中的 MCC/設備名稱標籤
4. 重建全部圖面
5. 驗證碰撞 + 名詞一致性

---

## 十一、工具鏈修正歷程（治本修正清單）

| 修正項 | 檔案 | 原因 | 修正內容 |
|--------|------|------|---------|
| PRP LAN-B 連線 | gen_d2.py L1000-1020 | L2→L1 只連 LAN-A | 新增 LAN-B→L1 連線 |
| LAN-B 描述一致 | gen_d2.py L564-568 | LAN-B Bay Switch 缺描述 | 加上和 LAN-A 一致的 description |
| node_label 支援 | gen_d2.py L625-631 | 所有 L1 節點都叫 RTU | 新增 `node_label` 欄位 |
| DANP 標籤 | gen_d2.py L636 | RedBox 不適用 SIPROTEC 5 | 改為 "DANP Interface" |
| Legend DANP | optimize_svg.py L53 | Legend 寫 RedBox | 改為 "DANP (PRP Dual-NIC)" |
| Legend BCU/RTU/IED | optimize_svg.py L51 | Legend 寫 RTU/IED | 改為 "BCU / RTU / IED" |
| Legend 右側延伸 | optimize_svg.py L744-766 | 窄圖面 Legend 重疊 | 畫布右側延伸 |
| Title Bar 延伸條 | optimize_svg.py L176-180 | 延伸區域沒有 Title Bar | 55px 高深藍色銜接條 |
| find_empty_zone 閾值 | optimize_svg.py L744 | 中等寬度圖面 Legend 誤嵌入 | 閾值提高到 6000px |
| SVG & 跳脫 | 各 YAML | project name 含 & | 改用 + |

---

## 十二、關鍵檔案路徑

| 檔案 | 路徑 | 用途 |
|------|------|------|
| gen_d2.py | project_root/03_work/ | D2 源碼產生器（核心工具） |
| optimize_svg.py | project_root/03_work/ | SVG 後製（Title Bar + Legend） |
| check_collision.py | project_root/03_work/ | 碰撞檢查 |
| patch_all_f6.py | project_root/03_work/ | F6 專案 D2 patch |
| gen_pdf.py | project_root/03_work/ | PDF 提案書產生器 |
| component_library.yaml | project_root/03_work/ | 設備元件庫 |
| project_template.yaml | project_root/03_work/ | YAML 模板 |
| SKILL_PACKAGE.md | project_root/ | 初版 Skill 素材包 |
| F6_CBOM_v1.1.md | project_root/00_inbox/ | 最新 CBOM |

---

*本文件產生於 2026-03-23，基於 F6 ONS 專案完整開發經驗。*
