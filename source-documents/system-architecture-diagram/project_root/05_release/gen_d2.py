#!/usr/bin/env python3
"""
gen_d2.py — OT 架構圖 D2 源碼產生器
版本：v1.0  |  2026-03-04
用法：python gen_d2.py project.yaml [--output output.d2] [--dry-run]

依據 OT_Architecture_Framework_v1.0.md 實作：
  T-01~T-08 拓撲規則
  R-D2-01~R-D2-11 D2 語法規則
  R-BR-01 品牌色碼規範
"""

import sys
import yaml
import argparse
from pathlib import Path


def d2label(s: str) -> str:
    """
    將 YAML 字串安全轉換為 D2 double-quoted 字串內容。
    YAML 解析後的 \n（實際換行符）轉為字面 \n（R-D2-10 補丁）。
    D2 接受字面 \n，但不接受實際換行符在 double-quoted string 內。
    """
    return s.replace('\n', '\\n') if s else s

# ─────────────────────────────────────────────────────────────
# 品牌色碼常數（R-BR-01）— 唯一合法顏色集合
# 禁止在此以外的地方硬編碼任何顏色值（R-BR-02）
# ─────────────────────────────────────────────────────────────
COLOR = {
    "navy":   "#0C3467",   # Navy Primary
    "sky":    "#008EC3",   # Sky Blue
    "amber":  "#F5A623",   # Amber
    "gray":   "#9B9B9B",   # Gray
    "red":    "#c0392b",   # Red（防火牆固定色）
    "green":  "#2e7d32",   # Green（L2 Control Network）
    # Zone 背景淡色
    "bg_l4":  "#e8eef5",
    "bg_dmz": "#fdecea",
    "bg_l3":  "#e0f4fb",
    "bg_l2":  "#e8f5e9",
    "bg_l1":  "#fff8e1",
    "bg_l0":  "#f5f5f5",
}

# ─────────────────────────────────────────────────────────────
# CLASSES_BLOCK — 所有設備 D2 class 定義（R-D2-08）
# 色碼全部引用 COLOR 常數，禁止硬編碼
# ─────────────────────────────────────────────────────────────
def build_classes_block() -> str:
    """產生 D2 的 classes: {} 區塊（R-D2-08）"""
    n  = COLOR["navy"]
    s  = COLOR["sky"]
    a  = COLOR["amber"]
    g  = COLOR["gray"]
    r  = COLOR["red"]
    gr = COLOR["green"]
    return f"""classes: {{
  # ── Zone 容器 ──────────────────────────────────────────────
  zone_l4: {{
    style.fill: "{COLOR['bg_l4']}"
    style.stroke: "{n}"
    style.stroke-width: 2
    style.font-size: 16
    style.bold: true
  }}
  zone_dmz: {{
    style.fill: "{COLOR['bg_dmz']}"
    style.stroke: "{r}"
    style.stroke-width: 2
    style.font-size: 16
    style.bold: true
  }}
  zone_l3: {{
    style.fill: "{COLOR['bg_l3']}"
    style.stroke: "{s}"
    style.stroke-width: 2
    style.font-size: 16
    style.bold: true
  }}
  zone_l2: {{
    style.fill: "{COLOR['bg_l2']}"
    style.stroke: "{gr}"
    style.stroke-width: 2
    style.font-size: 16
    style.bold: true
  }}
  zone_l1: {{
    style.fill: "{COLOR['bg_l1']}"
    style.stroke: "{a}"
    style.stroke-width: 2
    style.font-size: 16
    style.bold: true
  }}
  zone_l0: {{
    style.fill: "{COLOR['bg_l0']}"
    style.stroke: "{g}"
    style.stroke-width: 2
    style.font-size: 16
    style.bold: true
  }}
  zone_sub: {{
    style.fill: "transparent"
    style.stroke: "{g}"
    style.stroke-width: 1
    style.stroke-dash: 3
    style.font-size: 13
  }}
  # ── L3 設備 ──────────────────────────────────────────────
  scada_server: {{
    shape: rectangle
    style.fill: "{COLOR['bg_l3']}"
    style.stroke: "{n}"
    style.stroke-width: 2
    style.font-size: 13
  }}
  hmi_workstation: {{
    shape: rectangle
    style.fill: "{COLOR['bg_l3']}"
    style.stroke: "{s}"
    style.stroke-width: 2
    style.font-size: 13
  }}
  historian: {{
    shape: cylinder
    style.fill: "{COLOR['bg_l3']}"
    style.stroke: "{n}"
    style.stroke-width: 2
    style.font-size: 13
  }}
  engineering_ws: {{
    shape: rectangle
    style.fill: "{COLOR['bg_l0']}"
    style.stroke: "{g}"
    style.stroke-width: 2
    style.font-size: 13
  }}
  ntp_server: {{
    shape: rectangle
    style.fill: "{COLOR['bg_l3']}"
    style.stroke: "{s}"
    style.stroke-width: 2
    style.font-size: 13
  }}
  # ── DMZ 設備 ───────────────────────────────────────────────
  firewall: {{
    shape: diamond
    style.fill: "{COLOR['bg_dmz']}"
    style.stroke: "{r}"
    style.stroke-width: 2
    style.font-size: 13
  }}
  data_diode: {{
    shape: diamond
    style.fill: "{COLOR['bg_l1']}"
    style.stroke: "{a}"
    style.stroke-width: 2
    style.font-size: 13
  }}
  jump_server: {{
    shape: rectangle
    style.fill: "white"
    style.stroke: "{r}"
    style.stroke-width: 1
    style.stroke-dash: 3
    style.font-size: 13
  }}
  # ── L2 設備 ──────────────────────────────────────────────
  switch_prp: {{
    shape: hexagon
    style.fill: "{COLOR['bg_l3']}"
    style.stroke: "{s}"
    style.stroke-width: 2
    style.font-size: 12
  }}
  # ── L1 設備 ──────────────────────────────────────────────
  gateway: {{
    shape: hexagon
    style.fill: "{COLOR['bg_l1']}"
    style.stroke: "{a}"
    style.stroke-width: 2
    style.font-size: 13
  }}
  redbox: {{
    shape: hexagon
    style.fill: "{COLOR['bg_l3']}"
    style.stroke: "{n}"
    style.stroke-width: 2
    style.font-size: 12
  }}
  rtu_ied: {{
    shape: rectangle
    style.fill: "{COLOR['bg_l1']}"
    style.stroke: "{a}"
    style.stroke-width: 2
    style.font-size: 13
  }}
  plc: {{
    shape: rectangle
    style.fill: "{COLOR['bg_l3']}"
    style.stroke: "{s}"
    style.stroke-width: 2
    style.font-size: 13
  }}
  # ── L0 設備 ──────────────────────────────────────────────
  field_ied: {{
    shape: rectangle
    style.fill: "{COLOR['bg_l0']}"
    style.stroke: "{g}"
    style.stroke-width: 2
    style.font-size: 12
  }}
  inverter: {{
    shape: rectangle
    style.fill: "{COLOR['bg_l1']}"
    style.stroke: "{a}"
    style.stroke-width: 1
    style.font-size: 12
  }}
  ups: {{
    shape: rectangle
    style.fill: "{COLOR['bg_l1']}"
    style.stroke: "{a}"
    style.stroke-width: 1
    style.font-size: 12
  }}
  # ── 外部系統 ────────────────────────────────────────────
  external_system: {{
    shape: rectangle
    style.fill: "white"
    style.stroke: "{g}"
    style.stroke-width: 1
    style.stroke-dash: 3
    style.font-size: 13
  }}
}}"""


# ─────────────────────────────────────────────────────────────
# T03: load_config() — 載入 YAML 設定
# ─────────────────────────────────────────────────────────────
def load_config(project_yaml: str, library_yaml: str = "component_library.yaml") -> tuple[dict, dict]:
    """
    載入 project.yaml 與 component_library.yaml。
    回傳 (config, library)，任一檔案不存在則中止。
    """
    p = Path(project_yaml)
    if not p.exists():
        print(f"[ERROR] 找不到 project.yaml：{project_yaml}", file=sys.stderr)
        sys.exit(1)

    lib_path = Path(library_yaml)
    if not lib_path.exists():
        # 嘗試同目錄下的 component_library.yaml
        lib_path = p.parent / "component_library.yaml"
    if not lib_path.exists():
        print(f"[ERROR] 找不到 component_library.yaml：{library_yaml}", file=sys.stderr)
        sys.exit(1)

    with open(p, encoding="utf-8") as f:
        config = yaml.safe_load(f)
    with open(lib_path, encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    # 將 library 轉為 dict，key = component id
    library = {c["id"]: c for c in raw.get("components", [])}
    return config, library


# ─────────────────────────────────────────────────────────────
# T03: validate_config() — 驗證設定完整性（R-D2-04）
# ─────────────────────────────────────────────────────────────
def validate_config(config: dict) -> list[str]:
    """
    驗證 config 中的引用是否合法：
    - connected_to 引用的 key 必須存在
    - comm_styles key 必須存在
    回傳 error message list，空 list = 驗證通過
    """
    errors = []
    comm_keys = set(config.get("comm_styles", {}).keys())
    feeder_ids = {f["id"] for f in config.get("network", {}).get("feeder_groups", [])}
    rtu_ids = {p["id"] for p in config.get("field_control", {}).get("rtu_panels", [])}

    # 合法的 connected_to 值
    gw_count = config.get("field_control", {}).get("gateways", {}).get("count", 2)
    valid_targets = {"gw_A"}
    if gw_count >= 2:
        valid_targets.add("gw_B")
    for rid in rtu_ids:
        valid_targets.add(f"rtu_{rid}")
    for fid in feeder_ids:
        valid_targets.add(f"mcc_{fid}")

    def check_device(dev: dict, context: str):
        comm = dev.get("comm")
        if comm and comm not in comm_keys:
            errors.append(f"[{context}] comm '{comm}' 不在 comm_styles 中（合法值：{sorted(comm_keys)}）")
        target = dev.get("connected_to")
        if target and target not in valid_targets:
            errors.append(f"[{context}] connected_to '{target}' 無效（合法值：{sorted(valid_targets)}）")

    # 驗證 L0 保護電驛
    for ied in config.get("field_devices", {}).get("protection_ieds", {}).get("ieds", []):
        check_device(ied, f"protection_ieds/{ied.get('id','?')}")

    # 驗證 L0 太陽能/儲能
    for dev in config.get("field_devices", {}).get("solar_storage", {}).get("devices", []):
        check_device(dev, f"solar_storage/{dev.get('id','?')}")

    # 驗證 RTU 盤的 connected_to_feeder
    for panel in config.get("field_control", {}).get("rtu_panels", []):
        feeder = panel.get("connected_to_feeder")
        if feeder and feeder not in feeder_ids:
            errors.append(f"[rtu_panels/{panel['id']}] connected_to_feeder '{feeder}' 不在 feeder_groups 中（{sorted(feeder_ids)}）")

    # M-003：驗證 gen_conn_*() 內部固定使用的 comm_styles key 均存在
    REQUIRED_COMM_KEYS = {
        "PRP_LAN_A", "PRP_LAN_B", "OPC_UA_A", "OPC_UA_B",
        "IEEE1588_A", "IEEE1588_B", "IEC61850_MMS", "Modbus_TCP",
        "PRP_fiber_A", "PRP_fiber_B", "IEC61850_fiber", "RS485_modbus",
        "IT_ethernet",
    }
    for key in sorted(REQUIRED_COMM_KEYS):
        if key not in comm_keys:
            errors.append(f"[comm_styles] 必要的 key '{key}' 不存在（內部連線生成所需）")

    return errors


# ─────────────────────────────────────────────────────────────
# T04: gen_header() — vars / direction / classes 區塊（R-D2-01）
# ─────────────────────────────────────────────────────────────
def gen_header(config: dict) -> str:
    """
    輸出 D2 檔案開頭的 vars / direction / classes 區塊。
    R-D2-01：強制使用 dagre layout，禁止 elk。
    R-D2-02：禁止在此宣告 title: 或 legend: 節點。
    """
    proj = config.get("project", {})
    lines = [
        f"# OT Architecture Diagram — {proj.get('name', '')} {proj.get('site', '')}",
        f"# Rev: {proj.get('rev', '1.0')}  |  {proj.get('date', '')}",
        f"# Generated by gen_d2.py v1.0",
        "",
        "# R-D2-01: 強制使用 dagre，禁止 elk",
        "vars: {",
        "  d2-config: {",
        "    layout-engine: dagre",
        "    theme-id: 0",
        "  }",
        "}",
        "",
        "direction: down",
        "",
    ]
    lines.append(build_classes_block())
    lines.append("")
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────
# T05: gen_l4() — L4 Enterprise Zone（T-07）
# ─────────────────────────────────────────────────────────────
def gen_l4(config: dict) -> str:
    """
    T-07：enterprise.enabled=false 時完全省略 L4 Zone。
    """
    ent = config.get("enterprise", {})
    if not ent.get("enabled", True):
        return ""   # T-07：省略整個 L4

    lines = [
        'L4: "Level 4｜企業層  Enterprise Zone" {',
        "  class: zone_l4",
    ]
    if ent.get("erp"):
        lines.append('  ERP: "ERP 系統" { class: external_system }')
    if ent.get("adcc"):
        lines.append('  ADCC: "ADCC 電力調度" { class: external_system }')
    if ent.get("scada_ws"):
        lines.append('  SCADA_WS: "SCADA 工作站" { class: hmi_workstation }')
    lines.append("}")
    lines.append("")
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────
# T05: gen_dmz() — DMZ Zone
# ─────────────────────────────────────────────────────────────
def gen_dmz(config: dict) -> str:
    dmz = config.get("dmz", {})
    fw_model  = dmz.get("firewall_model", "")
    sw_model  = dmz.get("l3_switch_model", "")
    fw_label  = f"FIREWALL\\n{fw_model}" if fw_model else "FIREWALL"
    sw_label  = f"L3 Switch\\n{sw_model}" if sw_model else "L3 Switch"

    lines = [
        'DMZ: "DMZ｜邊界防護  Demilitarized Zone" {',
        "  class: zone_dmz",
        f'  FW: "{fw_label}" {{ class: firewall }}',
        f'  SW_DMZ: "{sw_label}" {{ class: switch_prp }}',
    ]

    # 遠端存取（PSTN/4G）
    if dmz.get("remote_access"):
        rt = dmz.get("remote_type", "PSTN+4G")
        modem_model = dmz.get("modem_model") or rt
        lines.append(f'  MODEM: "Modem\\n{modem_model}" {{ class: gateway }}')

    lines.append("}")
    lines.append("")
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────
# T06: gen_l3() — L3 Supervisory Zone（T-02）
# ─────────────────────────────────────────────────────────────
def gen_l3(config: dict) -> str:
    """
    T-02：hmi_count=1 只產生 HMI_A；hmi_count=2 產生 HMI_A + HMI_B。
    """
    scada = config.get("scada", {})
    hmi_model = scada.get("hmi_model", "")
    hmi_suffix = f"\\n{hmi_model}" if hmi_model else ""

    lines = [
        'L3: "Level 3｜監控站  Supervisory Control Zone" {',
        "  class: zone_l3",
    ]

    # HMI：T-02
    hmi_count = scada.get("hmi_count", 1)
    if hmi_count >= 1:
        if hmi_count >= 2:
            lines.append(f'  HMI_A: "主站 HMI_A{hmi_suffix}" {{ class: hmi_workstation }}')
        else:
            lines.append(f'  HMI_A: "HMI{hmi_suffix}" {{ class: hmi_workstation }}')
    if hmi_count >= 2:
        lines.append(f'  HMI_B: "備援 HMI_B{hmi_suffix}" {{ class: hmi_workstation }}')

    # Historian
    if scada.get("historian"):
        hist_m = scada.get("historian_model", "")
        hist_suffix = f"\\n{hist_m}" if hist_m else ""
        lines.append(f'  HIST: "Historian{hist_suffix}" {{ class: historian }}')

    # 工程師工作站
    if scada.get("engineering_ws"):
        ews_m = scada.get("engineering_ws_model", "")
        ews_suffix = f"\\n{ews_m}" if ews_m else ""
        lines.append(f'  ENG_WS: "Engineering WS{ews_suffix}" {{ class: engineering_ws }}')

    # NTP / GPS 時間伺服器
    if scada.get("ntp"):
        ntp_m = scada.get("ntp_model", "")
        ntp_suffix = f"\\n{ntp_m}" if ntp_m else ""
        lines.append(f'  NTP: "NTP Server{ntp_suffix}" {{ class: ntp_server }}')
        if scada.get("gnss"):
            lines.append('  GNSS: "GNSS Antenna" { class: ntp_server }')

    # UPS L3
    if scada.get("ups_l3"):
        cap = scada.get("ups_l3_capacity", "")
        cap_suffix = f"\\n{cap}" if cap else ""
        lines.append(f'  UPS_L3: "UPS{cap_suffix}" {{ class: ups }}')

    lines.append("}")
    lines.append("")
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────
# T07: gen_l2() — L2 Control Network（T-01：PRP 開關）
# ─────────────────────────────────────────────────────────────
def gen_l2(config: dict) -> str:
    """
    T-01：prp_enabled=false 時每個 feeder 只產生一個 edge switch（LAN-A）。
    T-01：prp_enabled=true  時每個 feeder 產生一對 edge switch（LAN-A + LAN-B）。
    """
    net = config.get("network", {})
    prp = net.get("prp_enabled", True)
    core_m = net.get("core_switch_model", "")
    core_suffix = f"\\n{core_m}" if core_m else ""
    feeders = net.get("feeder_groups", [])

    lines = [
        'L2: "Level 2｜控制網路  Control Network Zone" {',
        "  class: zone_l2",
        '  core: "核心交換（雙網 PRP 冗餘）" {',
        "    class: zone_sub",
        f'    SW_CORE_A: "Core Switch A{core_suffix}" {{ class: switch_prp }}',
    ]
    if prp:
        lines.append(f'    SW_CORE_B: "Core Switch B{core_suffix}" {{ class: switch_prp }}')
    lines.append("  }")
    lines.append('  edge: "饋線邊緣交換" {')
    lines.append("    class: zone_sub")
    for f in feeders:
        fid = f["id"]
        flabel = f.get("label", fid)
        fdesc  = f.get("description", "")
        fpanels = f.get("mcc_panels", "")
        desc_part = f"  {fdesc}" if fdesc else ""
        panels_part = f"  MCC {fpanels}" if fpanels else ""
        lines.append(f'    SW_{fid}_A: "SW-{flabel} LAN-A{desc_part}{panels_part}" {{ class: switch_prp }}')
        if prp:
            lines.append(f'    SW_{fid}_B: "SW-{flabel} LAN-B" {{ class: switch_prp }}')
    lines.append("  }")
    lines.append("}")
    lines.append("")
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────
# T08: gen_l1_gw() — Protocol Gateway 子群組（T-03）
# ─────────────────────────────────────────────────────────────
def gen_l1_gw(config: dict) -> list[str]:
    """
    T-03：gateways.count=1 只有 GW_A；count=2 有 GW_A + GW_B。
    T-04：此函式輸出的 gw 子群組必須是 L1 第一個（由 gen_l1 保證）。
    """
    gw_conf = config.get("field_control", {}).get("gateways", {})
    if not gw_conf.get("enabled", True):
        return []

    count = gw_conf.get("count", 2)
    model = gw_conf.get("model", "")
    model_suffix = f"\\n{model}" if model else ""
    protos = gw_conf.get("protocol_conversion", [])

    lines = [
        '  gw: "Protocol Gateway" {',
        "    class: zone_sub",
        f'    GW_A: "GW_A{model_suffix}" {{ class: gateway }}',
    ]
    if count >= 2:
        lines.append(f'    GW_B: "GW_B{model_suffix}" {{ class: gateway }}')
    if protos:
        proto_str = "  ".join(p for p in protos if p)
        lines.append(f'    # 協定轉換：{proto_str}')
    lines.append("  }")
    return lines


# ─────────────────────────────────────────────────────────────
# T09: gen_l1_rtu_panel() — RTU 盤子群組（含 IED + REDBOX）
# ─────────────────────────────────────────────────────────────
def gen_l1_rtu_panel(panel: dict, prp_enabled: bool) -> list[str]:
    """
    每個 RTU 盤輸出一個子群組。
    T-01：prp_enabled=false 時 REDBOX 省略。
    """
    pid    = panel["id"]
    plabel = panel.get("label", f"RTU 盤 {pid}")
    rtu_m  = panel.get("rtu_model", "")
    rtu_suffix = f"\\n{rtu_m}" if rtu_m else ""

    lines = [
        f'  {pid.lower()}: "{plabel}" {{',
        "    class: zone_sub",
        f'    RTU_{pid}: "RTU{rtu_suffix}" {{ class: rtu_ied }}',
    ]

    # REDBOX：T-01
    if panel.get("redbox") and prp_enabled:
        lines.append(f'    REDBOX_{pid}: "RedBox" {{ class: redbox }}')

    # L1 層 IED
    for ied in panel.get("ieds", []):
        iid = ied["id"]
        ilabel = d2label(ied.get("label", iid))
        lines.append(f'    {iid}: "{ilabel}" {{ class: field_ied }}')

    lines.append("  }")
    return lines


# ─────────────────────────────────────────────────────────────
# T09: gen_l1_mcc() — MCC 群子群組
# ─────────────────────────────────────────────────────────────
def gen_l1_mcc(feeders: list) -> list[str]:
    lines = [
        '  mcc: "MCC 群" {',
        "    class: zone_sub",
    ]
    for f in feeders:
        fid = f["id"]
        flabel = f.get("label", fid)
        fdesc = f.get("description", "")
        fpanels = f.get("mcc_panels", "")
        desc_str = f"  {fdesc}" if fdesc else ""
        panels_str = f"  盤{fpanels}" if fpanels else ""
        lines.append(f'    MCC_{fid}: "MCC-{flabel}{desc_str}{panels_str}" {{ class: plc }}')
    lines.append("  }")
    return lines


# ─────────────────────────────────────────────────────────────
# T09: gen_l1_statcom() — STATCOM 子群組（T-08）
# ─────────────────────────────────────────────────────────────
def gen_l1_statcom(config: dict) -> list[str]:
    """
    T-08：statcom.enabled=false 時完全省略。
    """
    sc = config.get("field_control", {}).get("statcom", {})
    if not sc.get("enabled", False):
        return []  # T-08：省略

    osc_m = sc.get("osc_model", "")
    osc_suffix = f"\\n{osc_m}" if osc_m else ""
    mod_count = sc.get("module_count", 3)
    proto = sc.get("protocol", "Modbus TCP")

    lines = [
        '  statcom: "STATCOM 系統" {',
        "    class: zone_sub",
        f'    OSC: "OSC 控制器{osc_suffix}" {{ class: plc }}',
    ]
    mod_labels = ["A", "B", "C", "D", "E", "F"]
    for i in range(mod_count):
        lbl = mod_labels[i] if i < len(mod_labels) else str(i + 1)
        lines.append(f'    LNK_{lbl}: "LNK-{lbl}  {proto}" {{ class: gateway }}')
    lines.append("  }")
    return lines


# ─────────────────────────────────────────────────────────────
# T08: gen_l1() — L1 Zone（T-04：強制 gw 第一）
# ─────────────────────────────────────────────────────────────
def gen_l1(config: dict) -> str:
    """
    T-04：L1 Zone 子群組宣告順序強制為 gw → rtu_panels → mcc → statcom。
    不論 project.yaml 中的順序如何，此處強制排列。
    """
    net = config.get("network", {})
    prp = net.get("prp_enabled", True)
    feeders = net.get("feeder_groups", [])

    lines = [
        'L1: "Level 1｜現場控制層  Field Control Zone" {',
        "  class: zone_l1",
        "  # T-04: 子群組宣告順序強制為 gw → rtu_panels → mcc → statcom",
    ]

    # 1. GW（必須第一個，T-04 / R-D2-03）
    lines += gen_l1_gw(config)

    # 2. RTU 盤
    for panel in config.get("field_control", {}).get("rtu_panels", []):
        lines += gen_l1_rtu_panel(panel, prp)

    # 3. MCC
    if feeders:
        lines += gen_l1_mcc(feeders)

    # 4. STATCOM（最後，T-08）
    lines += gen_l1_statcom(config)

    lines.append("}")
    lines.append("")
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────
# T10: gen_l0() — L0 Zone（R-D2-05：r_group 在前）
# ─────────────────────────────────────────────────────────────
def gen_l0(config: dict) -> str:
    """
    R-D2-05：r_group 永遠第一個宣告（左側），solar 第二個（右側）。
    r_group 靠近 L1.gw，solar 靠近 L1.mcc，縮短跨 Zone 連線長度。
    """
    fd = config.get("field_devices", {})
    prot = fd.get("protection_ieds", {})
    solar = fd.get("solar_storage", {})

    lines = [
        'L0: "Level 0｜現場設備  Field Devices" {',
        "  class: zone_l0",
        "  # R-D2-05: r_group 在前（左），solar 在後（右）",
    ]

    # R 群（保護電驛）— 永遠第一個
    if prot.get("enabled", True):
        grp_label = prot.get("group_label", "R 群（保護電驛 IED）")
        lines.append(f'  r_group: "{grp_label}" {{')
        lines.append("    class: zone_sub")
        for ied in prot.get("ieds", []):
            iid = ied["id"]
            ilabel = d2label(ied.get("label", iid))
            lines.append(f'    {iid}: "{ilabel}" {{ class: field_ied }}')
        lines.append("  }")

    # 太陽能/儲能 — 第二個（右側）
    if solar.get("enabled", False):
        grp_label = solar.get("group_label", "太陽能 / 儲能設備")
        lines.append(f'  solar: "{grp_label}" {{')
        lines.append("    class: zone_sub")
        type_map = {
            "inverter": "inverter",
            "plc": "plc",
            "gateway": "gateway",
            "ups": "ups",
        }
        for dev in solar.get("devices", []):
            did = dev["id"]
            dlabel = d2label(dev.get("label", did))
            dclass = type_map.get(dev.get("type", ""), "field_ied")
            lines.append(f'    {did}: "{dlabel}" {{ class: {dclass} }}')
        lines.append("  }")

    lines.append("}")
    lines.append("")
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────
# T12: resolve_target() — YAML 語意 key → D2 節點路徑
# ─────────────────────────────────────────────────────────────
def resolve_target(target: str, config: dict) -> str | None:
    """
    將 project.yaml 中的語意 key 轉換為 D2 節點路徑。
    gw_A  → L1.gw.GW_A
    gw_B  → L1.gw.GW_B
    rtu_TPC → L1.tpc.RTU_TPC
    mcc_M1  → L1.mcc.MCC_M1
    返回 None 表示 target=null，應跳過此連線（T-06）
    """
    if target is None:
        return None
    if target == "gw_A":
        return "L1.gw.GW_A"
    if target == "gw_B":
        return "L1.gw.GW_B"
    if target.startswith("rtu_"):
        rid = target[4:]
        return f"L1.{rid.lower()}.RTU_{rid}"
    if target.startswith("mcc_"):
        fid = target[4:]
        return f"L1.mcc.MCC_{fid}"
    return target  # 直接使用（fallback）


# ─────────────────────────────────────────────────────────────
# T12: emit_connection() — 輸出單一連線的 D2 語法
# R-D2-09：inline style；R-D2-10：label 禁止 \n
# ─────────────────────────────────────────────────────────────
def emit_connection(src: str, dst: str, comm_key: str,
                    comm_styles: dict, label: str | None = None) -> str:
    """
    R-D2-09：使用 inline style，禁止 class 引用。
    R-D2-10：label 中 \n 替換為兩空格。
    label=None 時使用 comm_styles 中的 label；label="" 時置空（T-05）。
    """
    style = comm_styles.get(comm_key, {})
    stroke = style.get("stroke", COLOR["gray"])
    sw = style.get("stroke_width", 1)
    sd = style.get("stroke_dash", 0)

    if label is None:
        # R-D2-10：將 \n 替換為兩空格
        raw_label = style.get("label", comm_key)
        conn_label = raw_label.replace("\\n", "  ").replace("\n", "  ")
    else:
        conn_label = label  # 可為 "" (T-05 去重)

    style_block = f'style.stroke: "{stroke}"\n    style.stroke-width: {sw}'
    if sd > 0:
        style_block += f'\n    style.stroke-dash: {sd}'

    return (f'{src} -> {dst}: "{conn_label}" {{\n'
            f'    {style_block}\n'
            f'  }}')


# ─────────────────────────────────────────────────────────────
# T11: gen_conn_backbone() — L2 骨幹 PRP 連線（T-05：label 去重）
# ─────────────────────────────────────────────────────────────
def gen_conn_backbone(config: dict) -> str:
    """
    T-05 / R-D2-06：LAN-A 骨幹只有第一條保留 label，其餘置空 ""。
    LAN-B 同理。
    """
    net = config.get("network", {})
    prp = net.get("prp_enabled", True)
    feeders = net.get("feeder_groups", [])
    comm = config.get("comm_styles", {})
    lines = ["# ── L2 骨幹連線（T-05：只有第一條保留 label）──"]

    for i, f in enumerate(feeders):
        fid = f["id"]
        # LAN-A 骨幹
        lbl_a = None if i == 0 else ""   # T-05：只有第一條保留 label
        lines.append(emit_connection(
            "L2.core.SW_CORE_A", f"L2.edge.SW_{fid}_A",
            "PRP_LAN_A", comm, label=lbl_a
        ))
        if prp:
            lbl_b = None if i == 0 else ""
            lines.append(emit_connection(
                "L2.core.SW_CORE_B", f"L2.edge.SW_{fid}_B",
                "PRP_LAN_B", comm, label=lbl_b
            ))

    lines.append("")
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────
# 骨幹連線：L3 ↔ DMZ ↔ L2 ↔ L1
# ─────────────────────────────────────────────────────────────
def gen_conn_inter_zone(config: dict) -> str:
    """L3 → DMZ → L2 → L1 的跨 Zone 骨幹連線"""
    comm = config.get("comm_styles", {})
    prp = config.get("network", {}).get("prp_enabled", True)
    ent = config.get("enterprise", {})
    lines = ["# ── 跨 Zone 骨幹連線 ──────────────────────────"]

    # L4 → DMZ（T-07：enterprise.enabled=false 時省略）
    if ent.get("enabled", True):
        if ent.get("erp"):
            lines.append(emit_connection("L4.ERP", "DMZ.FW", "IT_ethernet", comm))
        if ent.get("adcc"):
            lines.append(emit_connection("L4.ADCC", "DMZ.FW", "IT_ethernet", comm))
        if ent.get("scada_ws"):
            lines.append(emit_connection("L4.SCADA_WS", "DMZ.FW", "IT_ethernet", comm))

    # DMZ → L3
    lines.append(emit_connection("DMZ.FW", "L3.HMI_A", "OPC_UA_A", comm))
    scada = config.get("scada", {})
    if scada.get("hmi_count", 1) >= 2:
        lines.append(emit_connection("DMZ.FW", "L3.HMI_B", "OPC_UA_B", comm))

    # L3 → L2
    lines.append(emit_connection("L3.HMI_A", "L2.core.SW_CORE_A", "OPC_UA_A", comm))
    if scada.get("hmi_count", 1) >= 2 and prp:
        lines.append(emit_connection("L3.HMI_B", "L2.core.SW_CORE_B", "OPC_UA_B", comm))
    if scada.get("historian"):
        lines.append(emit_connection("L3.HIST", "L2.core.SW_CORE_A", "OPC_UA_A", comm))
    if scada.get("ntp"):
        lines.append(emit_connection("L3.NTP", "L2.core.SW_CORE_A", "IEEE1588_A", comm))
        if prp:
            lines.append(emit_connection("L3.NTP", "L2.core.SW_CORE_B", "IEEE1588_B", comm))

    # L2 edge → L1 RTU 盤
    for panel in config.get("field_control", {}).get("rtu_panels", []):
        pid = panel["id"]
        feeder = panel.get("connected_to_feeder")
        if feeder:
            pid_lower = pid.lower()
            if panel.get("redbox") and prp:
                lines.append(emit_connection(
                    f"L2.edge.SW_{feeder}_A", f"L1.{pid_lower}.REDBOX_{pid}",
                    "PRP_fiber_A", comm))
                lines.append(emit_connection(
                    f"L2.edge.SW_{feeder}_B", f"L1.{pid_lower}.REDBOX_{pid}",
                    "PRP_fiber_B", comm))
            else:
                lines.append(emit_connection(
                    f"L2.edge.SW_{feeder}_A", f"L1.{pid_lower}.RTU_{pid}",
                    "IEC61850_MMS", comm))

    # L2 edge → MCC
    for f in config.get("network", {}).get("feeder_groups", []):
        fid = f["id"]
        lines.append(emit_connection(
            f"L2.edge.SW_{fid}_A", f"L1.mcc.MCC_{fid}", "Modbus_TCP", comm))

    # STATCOM
    sc = config.get("field_control", {}).get("statcom", {})
    if sc.get("enabled"):
        feeders = config.get("network", {}).get("feeder_groups", [])
        if feeders:
            last_fid = feeders[-1]["id"]
            lines.append(emit_connection(
                f"L2.edge.SW_{last_fid}_A", "L1.statcom.OSC", "Modbus_TCP", comm))

    lines.append("")
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────
# T12: gen_conn_l0() — L0 連線（T-06：null 跳過）
# ─────────────────────────────────────────────────────────────
def gen_conn_l0(config: dict) -> str:
    """
    T-06：connected_to=null 時完全跳過，不產生連線宣告。
    連線方向：L1.gw → L0.IED（GW 為 IEC 61850 MMS Client，主動下行連線至 IED Server）。
    方向由上往下符合 dagre direction:down，確保 L0 Zone 被排在 L1 下方（layout 修正）。
    """
    comm = config.get("comm_styles", {})
    lines = ["# ── L0 連線（T-06：connected_to=null 跳過；方向 L1→L0 確保 dagre 由上往下）──"]

    # 保護電驛 IED
    for ied in config.get("field_devices", {}).get("protection_ieds", {}).get("ieds", []):
        gw_target = resolve_target(ied.get("connected_to"), config)
        if gw_target is None:
            continue   # T-06：跳過 null 連線
        ied_node = f"L0.r_group.{ied['id']}"
        comm_key = ied.get("comm", "IEC61850_fiber")
        # 方向：L1.GW → L0.IED（向下，讓 dagre 將 L0 排在 L1 下方）
        lines.append(emit_connection(gw_target, ied_node, comm_key, comm))

    # 太陽能/儲能設備
    if config.get("field_devices", {}).get("solar_storage", {}).get("enabled"):
        for dev in config["field_devices"]["solar_storage"].get("devices", []):
            ctrl_target = resolve_target(dev.get("connected_to"), config)
            if ctrl_target is None:
                continue   # T-06：跳過 null 連線
            dev_node = f"L0.solar.{dev['id']}"
            comm_key = dev.get("comm", "RS485_modbus")
            # 方向：L1.controller → L0.device（向下）
            lines.append(emit_connection(ctrl_target, dev_node, comm_key, comm))

    lines.append("")
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────
# T13: main() — 整合所有 gen_* 函式，輸出完整 D2 源碼
# ─────────────────────────────────────────────────────────────
def generate_d2(config: dict) -> str:
    """
    依照 Framework §5.1 的模組設計，組合完整 D2 源碼。
    輸出順序：header → L4 → DMZ → L3 → L2 → L1 → L0 → connections
    """
    parts = [
        gen_header(config),
        gen_l4(config),
        gen_dmz(config),
        gen_l3(config),
        gen_l2(config),
        gen_l1(config),   # T-04：gw 第一
        gen_l0(config),   # R-D2-05：r_group 在前
        gen_conn_backbone(config),   # T-05
        gen_conn_inter_zone(config),
        gen_conn_l0(config),         # T-06
    ]
    return "\n".join(p for p in parts if p)


def main():
    parser = argparse.ArgumentParser(
        description="OT 架構圖 D2 源碼產生器 v1.0"
    )
    parser.add_argument("project_yaml", help="project.yaml 路徑")
    parser.add_argument("--output", "-o", default="output.d2",
                        help="輸出 .d2 檔案路徑（預設：output.d2）")
    parser.add_argument("--library", "-l", default="component_library.yaml",
                        help="component_library.yaml 路徑")
    parser.add_argument("--dry-run", action="store_true",
                        help="只驗證設定，不輸出檔案")
    args = parser.parse_args()

    # T03: 載入設定
    config, library = load_config(args.project_yaml, args.library)

    # T03: 驗證設定
    errors = validate_config(config)
    if errors:
        print("[ERROR] 設定驗證失敗：", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        sys.exit(1)
    print(f"[OK] 設定驗證通過（{args.project_yaml}）")

    if args.dry_run:
        print("[OK] Dry-run 完成，未輸出檔案。")
        return

    # T13: 產生 D2 源碼
    d2_content = generate_d2(config)

    # 輸出
    out_path = Path(args.output)
    out_path.write_text(d2_content, encoding="utf-8")
    print(f"[OK] 輸出：{out_path}  ({len(d2_content)} bytes)")


if __name__ == "__main__":
    main()
