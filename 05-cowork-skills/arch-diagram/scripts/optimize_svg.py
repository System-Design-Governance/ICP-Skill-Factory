#!/usr/bin/env python3
"""
optimize_svg.py — OT 架構圖 SVG 後製優化腳本
版本：v1.0  |  2026-03-04
用法：python optimize_svg.py --input diagram_raw.svg [--project project.yaml]

依據 OT_Architecture_Framework_v1.0.md §7 實作：
  R-PP-01：八步驟固定流程，順序不可改變
  R-PP-02：Title Bar 規格
  R-PP-03：Legend 嵌入浮層
  R-PP-04：stroke-dasharray 補正
  R-PP-05：連線 label 白底遮罩
  R-PP-06：動態掃描空白區域
"""

import sys
import re
import yaml
import argparse
from pathlib import Path
from xml.etree import ElementTree as ET

# SVG namespace
SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")

TITLE_HEIGHT = 110  # R-PP-02：Title Bar 高度

# 連線 label 識別關鍵字（R-PP-05）
CONN_KEYWORDS = {
    'PRP', 'IEC', 'IEEE', 'Modbus', 'RS-485', 'Ethernet',
    'OPC', 'SQL', 'IRIG', 'Control', 'Serial', 'GOOSE',
    'MMS', 'Fiber', 'RF', 'PSTN', 'VPN', 'Wireless', 'PTP',
    'ICCP', 'RS485', 'DNP', 'LAN'
}

# Zone Title 識別：使用全形分隔符 "｜" 精確匹配 Zone 容器標題
# 所有 Zone 容器標題格式為 "Zone XX｜描述"，此字元不出現在其他元素中
ZONE_TITLE_SEPARATOR = '\uff5c'  # ｜ fullwidth vertical bar U+FF5C

# Legend 資料（元件類型 + 連線類型）
# LEGEND_COMPONENTS 格式：(shape, label, stroke_color, fill_color, dashed)
# shape: "rect" | "diamond" | "hexagon"
LEGEND_COMPONENTS = [
    ("rect",    "SCADA / Historian",  "#0C3467", "#e0f4fb", False),
    ("rect",    "HMI / NTP Server",   "#008EC3", "#e0f4fb", False),
    ("diamond", "防火牆 Firewall",     "#c0392b", "#fdecea", False),
    ("hexagon", "Switch PRP",          "#008EC3", "#e0f4fb", False),
    ("hexagon", "Protocol Gateway",    "#F5A623", "#fff8e1", False),
    ("rect",    "BCU / RTU / IED",      "#F5A623", "#fff8e1", False),
    ("rect",    "Field IED / ENG WS",  "#9B9B9B", "#f5f5f5", False),
    ("hexagon", "DANP (PRP Dual-NIC)", "#0C3467", "#e0f4fb", False),
    ("rect",    "外部系統",            "#9B9B9B", "white",   True),
]

LEGEND_CONNECTIONS = [
    ("實線(深藍粗)",  "IEC 61850 GOOSE Fiber", "#0C3467", False),
    ("實線(天藍)",    "PRP LAN-A / OPC-UA A",  "#008EC3", False),
    ("虛線(深藍)",    "PRP LAN-B / OPC-UA B",  "#0C3467", True),
    ("虛線(灰細)",    "RS-485 / IT Ethernet",  "#9B9B9B", True),
    ("虛線(琥珀)",    "VPN / RF Wireless",      "#F5A623", True),
    ("實線(天藍細)",  "Modbus TCP",             "#008EC3", False),
    ("實線(深藍)",    "IRIG-B / IEEE 1588",     "#0C3467", False),
]


# ─────────────────────────────────────────────────────────────
# Step 1: parse_svg() — 解析 SVG，取得主圖 bounding box
# ─────────────────────────────────────────────────────────────
def parse_svg(svg_content: str) -> tuple[ET.Element, dict]:
    """
    解析 SVG，回傳 (root_element, bounding_box)。
    bounding_box = {x, y, width, height}
    """
    root = ET.fromstring(svg_content)
    vb = root.get("viewBox", "0 0 1000 1000")
    parts = vb.split()
    bbox = {
        "x": float(parts[0]) if len(parts) > 0 else 0,
        "y": float(parts[1]) if len(parts) > 1 else 0,
        "width": float(parts[2]) if len(parts) > 2 else 1000,
        "height": float(parts[3]) if len(parts) > 3 else 1000,
    }
    return root, bbox


# ─────────────────────────────────────────────────────────────
# Step 2: remove_d2_artifacts() — 移除 D2 殘留的 title/legend（R-PP-01）
# ─────────────────────────────────────────────────────────────
def remove_d2_artifacts(svg_content: str) -> str:
    """
    R-D2-02 / R-PP-01：移除 D2 自動產生的 title/legend 節點。
    使用正則表達式處理，避免 namespace 問題。
    """
    # 移除 D2 title group（通常 id 含 "title" 或 "d2-title"）
    svg_content = re.sub(
        r'<g[^>]*id="[^"]*title[^"]*"[^>]*>.*?</g>',
        '', svg_content, flags=re.DOTALL | re.IGNORECASE
    )
    # 移除 D2 legend group
    svg_content = re.sub(
        r'<g[^>]*id="[^"]*legend[^"]*"[^>]*>.*?</g>',
        '', svg_content, flags=re.DOTALL | re.IGNORECASE
    )
    return svg_content


# ─────────────────────────────────────────────────────────────
# Step 3: shift_content() — 主圖元素向下位移（R-PP-01）
# ─────────────────────────────────────────────────────────────
def shift_content(svg_content: str, dy: int = TITLE_HEIGHT) -> str:
    """
    R-PP-01 Step 3：所有主圖元素向下位移 dy px，為 Title Bar 保留空間。
    注意：此步驟必須在 inject_title_bar 之前（R-PP-01 Step 3 < Step 5）。
    透過在主要 <g> 群組加上 transform="translate(0, {dy})" 實現。
    """
    # 找到第一個 <g> 或包裹所有內容的主群組，加入位移
    # D2 輸出的 SVG 通常有一個根 <g> 包裹所有內容
    svg_content = re.sub(
        r'(<svg[^>]*>)\s*(<g(?:\s[^>]*)?>)',
        lambda m: m.group(1) + f'\n<g transform="translate(0, {dy})">\n<!-- shift_content wrapper -->\n' + m.group(2),
        svg_content, count=1
    )
    # 對應補上閉合標籤（在 </svg> 前插入 </g>）
    svg_content = re.sub(
        r'(</g>\s*</svg>)',
        r'</g>\n<!-- end shift_content wrapper -->\n\1',
        svg_content
    )
    return svg_content


# ─────────────────────────────────────────────────────────────
# Step 4: fix_dasharray() — 修正過大的 stroke-dasharray（R-PP-04）
# ─────────────────────────────────────────────────────────────
def fix_dasharray(svg_content: str) -> str:
    """
    R-PP-04：D2(dagre) 將 stroke-dash 值乘以 stroke-width 輸出至 SVG。
    任何值超過 8 的 dasharray 都是被放大的，一律修正為 6,4。
    """
    def replacer(m):
        vals = [float(v) for v in re.split(r'[,\s]+', m.group(1).strip()) if v]
        if any(v > 8 for v in vals):
            return 'stroke-dasharray:6,4'
        return m.group(0)
    return re.sub(r'stroke-dasharray:\s*([\d.,\s]+)', replacer, svg_content)


# ─────────────────────────────────────────────────────────────
# Step 5: inject_title_bar() — 注入品牌 Title Bar（R-PP-02）
# ─────────────────────────────────────────────────────────────
def inject_title_bar(svg_content: str, project: dict,
                     canvas_width: float, bar_width: float = 0,
                     extend_w: float = 0) -> str:
    """
    R-PP-02：注入固定規格的品牌 Title Bar。
    canvas_width：原始圖面寬度（文字置中基準）
    bar_width：Title Bar 背景寬度，預設 = canvas_width
    extend_w：右側延伸寬度（Legend 區域），產生 8px 高的細窄色帶銜接
    """
    if bar_width <= 0:
        bar_width = canvas_width
    name    = project.get("name", "OT Architecture Diagram")
    site    = project.get("site", "")
    rev     = project.get("rev", "1.0")
    date    = project.get("date", "")
    std     = project.get("standard", "IEC 62443")
    cx      = canvas_width / 2

    subtitle = f"{site}  Rev {rev}  {date}".strip()
    std_line = f"Purdue Model / ISA-95 / {std} Zone &amp; Conduit"

    # 右側延伸：只畫一條 4px 的色帶作為視覺銜接（不複製完整 Title Bar）
    ext_strip = ""
    if extend_w > 0:
        ext_strip = (
            f'\n    <rect x="{canvas_width}" y="0" '
            f'width="{extend_w}" height="{TITLE_HEIGHT // 2}" fill="#0C3467"/>'
        )

    title_bar = f"""
  <!-- R-PP-02: Title Bar -->
  <g id="title-bar">
    <rect x="0" y="0" width="{bar_width}" height="{TITLE_HEIGHT}" fill="#0C3467"/>
    <rect x="0" y="0" width="6" height="{TITLE_HEIGHT}" fill="#008EC3"/>{ext_strip}
    <text x="{cx}" y="40" font-family="Arial,sans-serif" font-size="21"
          font-weight="bold" fill="white" text-anchor="middle">{name}</text>
    <text x="{cx}" y="66" font-family="Arial,sans-serif" font-size="12"
          fill="#93c5fd" text-anchor="middle">{subtitle}</text>
    <text x="{cx}" y="88" font-family="Arial,sans-serif" font-size="10"
          fill="#94a3b8" text-anchor="middle">{std_line}</text>
  </g>"""

    # 注入在 <svg ...> 標籤之後
    svg_content = re.sub(
        r'(<svg[^>]*>)',
        r'\1' + title_bar,
        svg_content, count=1
    )
    return svg_content


# ─────────────────────────────────────────────────────────────
# Step 6a: find_empty_zone() — 動態掃描空白區域（R-PP-06）
# ─────────────────────────────────────────────────────────────
def find_empty_zone(svg_content: str,
                    canvas_width: float,
                    canvas_height: float,
                    legend_w: int = 490,
                    legend_h: int = 340,
                    y_start: int = 0) -> tuple[int, int]:
    """
    R-PP-06：尋找圖中沒有節點的水平空白帶來放置 Legend。
    只收集「節點大小」的矩形作為障礙物（過濾 Zone 背景大矩形）。
    掃描策略：優先找 x 最右側、從各 y 層掃描，找到可放入 Legend 的空白位置。
    傳入的 svg_content 應為 shift_content() 之前的原始座標空間。
    找不到時回傳 (-1, -1)（由呼叫方決定 fallback）。
    """
    # 收集所有可見矩形作為障礙物（排除全畫布背景，但保留 Zone 容器）
    occupied = []
    for m in re.finditer(r'<(?:rect|ellipse|circle|polygon)[^>]+>', svg_content):
        tag = m.group(0)
        x_m = re.search(r'\bx="([^"]+)"', tag)
        y_m = re.search(r'\by="([^"]+)"', tag)
        w_m = re.search(r'\bwidth="([^"]+)"', tag)
        h_m = re.search(r'\bheight="([^"]+)"', tag)
        try:
            ox = float(x_m.group(1)) if x_m else 0
            oy = float(y_m.group(1)) if y_m else 0
            ow = float(w_m.group(1)) if w_m else 0
            oh = float(h_m.group(1)) if h_m else 0
            # 只排除全畫布背景（寬度 > 90% 且高度 > 90%）
            if ow > canvas_width * 0.9 and oh > canvas_height * 0.9:
                continue
            occupied.append((ox, oy, ox + ow, oy + oh))
        except (ValueError, AttributeError):
            pass

    # 同時收集連線路徑的 bounding box 作為障礙物
    for m in re.finditer(r'<path[^>]+d="([^"]+)"[^>]*>', svg_content):
        d_attr = m.group(1)
        nums = [float(n) for n in re.findall(r'[-]?\d+(?:\.\d+)?', d_attr)]
        if len(nums) >= 4:
            xs = nums[0::2]
            ys = nums[1::2]
            occupied.append((min(xs), min(ys), max(xs), max(ys)))

    MARGIN = 20  # 節點與 Legend 之間的最小間距

    def overlaps(cx, cy):
        """候選矩形 (cx,cy) ~ (cx+legend_w, cy+legend_h) 是否與任何障礙物重疊"""
        for ox, oy, ox2, oy2 in occupied:
            if not (cx + legend_w + MARGIN <= ox or cx - MARGIN >= ox2 or
                    cy + legend_h + MARGIN <= oy or cy - MARGIN >= oy2):
                return True
        return False

    step = 30
    right_margin = 20
    max_x = int(canvas_width) - legend_w - right_margin
    max_y = int(canvas_height) - legend_h - 20
    if max_x < 10 or max_y < y_start:
        return -1, -1

    # 掃描策略：從右上角往左下掃描
    # dagre 佈局通常將節點置中，右上角較容易有空白
    for y in range(y_start, max_y + 1, step):
        for x in range(max_x, 9, -step):
            if not overlaps(x, y):
                return x, y

    # 左上角 fallback
    for y in range(y_start, max_y + 1, step):
        for x in range(10, max_x + 1, step):
            if not overlaps(x, y):
                return x, y

    return -1, -1  # 找不到空白位置


# ─────────────────────────────────────────────────────────────
# Step 6b: inject_legend() — 注入 Legend 浮層（R-PP-03）
# ─────────────────────────────────────────────────────────────
def _legend_shape_svg(shape: str, sx: int, sy: int,
                       stroke: str, fill: str, dashed: bool) -> str:
    """
    繪製 Legend 元件圖示（22×16 bounding box）。
    shape: "rect" | "diamond" | "hexagon"
    """
    sw = 1.5
    dash = 'stroke-dasharray="4,2"' if dashed else ''
    common = f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {dash}'
    if shape == "diamond":
        # 菱形：以中心點 (sx+11, sy+8) 展開
        pts = f"{sx+11},{sy} {sx+22},{sy+8} {sx+11},{sy+16} {sx},{sy+8}"
        return f'<polygon points="{pts}" {common}/>'
    elif shape == "hexagon":
        # 扁六角形（flat-top）
        pts = f"{sx+5},{sy} {sx+17},{sy} {sx+22},{sy+8} {sx+17},{sy+16} {sx+5},{sy+16} {sx},{sy+8}"
        return f'<polygon points="{pts}" {common}/>'
    else:
        # 矩形（含 rx=2 圓角）
        return (f'<rect x="{sx}" y="{sy}" width="22" height="16" rx="2" {common}/>')


def inject_legend(svg_content: str, lx: int, ly: int) -> str:
    """
    R-PP-03：Legend 嵌入浮層，雙欄設計。
    左欄：元件類型（正確形狀 + 填色）；右欄：連線類型。
    不硬編碼座標，由 find_empty_zone() 決定位置（R-PP-06）。
    """
    row_h    = 27
    header_h = 30
    top_pad  = 16   # header 底部到第一行 icon 頂部的最小間距
    n_rows   = max(len(LEGEND_COMPONENTS), len(LEGEND_CONNECTIONS))
    leg_w    = 500
    leg_h    = header_h + top_pad + n_rows * row_h + 14
    col_sep  = 250   # 左欄寬度（含 icon + 文字）

    rows_svg = []
    for i in range(n_rows):
        # icon 頂部偏移 = header_h + top_pad + i * row_h
        # icon 高度 16px，icon 中心在頂部偏移 + 8
        icon_top_offset = header_h + top_pad + i * row_h
        cy = ly + icon_top_offset + 8   # 行圖示垂直中心 = 文字 baseline 參考

        # 左欄：元件圖示 + 名稱
        if i < len(LEGEND_COMPONENTS):
            shape, comp_label, stroke, fill, dashed = LEGEND_COMPONENTS[i]
            sx, sy_icon = lx + 10, ly + icon_top_offset   # icon 左上角
            rows_svg.append('  ' + _legend_shape_svg(shape, sx, sy_icon, stroke, fill, dashed))
            rows_svg.append(
                f'  <text x="{lx+38}" y="{cy+2}" font-family="Arial,sans-serif" '
                f'font-size="11" fill="#1a1a1a">{comp_label}</text>'
            )

        # 右欄：連線樣式線段 + 名稱
        if i < len(LEGEND_CONNECTIONS):
            _, conn_label, color, dashed = LEGEND_CONNECTIONS[i]
            lx2 = lx + col_sep + 10
            dash_attr = 'stroke-dasharray="5,3"' if dashed else ''
            rows_svg.append(
                f'  <line x1="{lx2}" y1="{cy-4}" x2="{lx2+26}" y2="{cy-4}" '
                f'stroke="{color}" stroke-width="2" {dash_attr}/>'
            )
            rows_svg.append(
                f'  <text x="{lx2+32}" y="{cy+2}" font-family="Arial,sans-serif" '
                f'font-size="11" fill="#1a1a1a">{conn_label}</text>'
            )

    legend_svg = f"""
  <!-- R-PP-03: Legend 浮層（位置由 find_empty_zone() 決定，R-PP-06）-->
  <g id="legend-overlay">
    <rect x="{lx}" y="{ly}" width="{leg_w}" height="{leg_h}"
          fill="white" fill-opacity="0.95" stroke="#0C3467" stroke-width="1.5" rx="6"
          filter="drop-shadow(2px 3px 8px rgba(0,0,0,0.18))"/>
    <rect x="{lx}" y="{ly}" width="{leg_w}" height="{header_h}"
          fill="#0C3467" rx="6"/>
    <rect x="{lx}" y="{ly+header_h//2}" width="{leg_w}" height="{header_h//2}" fill="#0C3467"/>
    <text x="{lx + leg_w//2}" y="{ly + header_h*2//3 + 4}" font-family="Arial,sans-serif" font-size="12"
          font-weight="bold" fill="white" text-anchor="middle">圖例 / Legend</text>
    <line x1="{lx+col_sep}" y1="{ly+header_h+4}" x2="{lx+col_sep}" y2="{ly+leg_h-4}"
          stroke="#cccccc" stroke-width="1"/>
    {''.join(rows_svg)}
  </g>"""

    # 注入在最後一個 </svg>（根元素）前，避免注入到 D2 內嵌 <svg> 元素
    last_idx = svg_content.rfind('</svg>')
    if last_idx >= 0:
        svg_content = svg_content[:last_idx] + legend_svg + '\n</svg>' + svg_content[last_idx + 6:]
    return svg_content


# ─────────────────────────────────────────────────────────────
# Step 7: add_label_backgrounds() — 連線 label 加白底遮罩（R-PP-05）
# ─────────────────────────────────────────────────────────────
def estimate_width(text: str) -> int:
    """估算文字像素寬度（R-PP-05）"""
    ascii_w = sum(7 for c in text if ord(c) < 128)
    cjk_w   = sum(13 for c in text if ord(c) >= 0x4E00)
    return ascii_w + cjk_w + 8


def add_label_backgrounds(svg_content: str, font_size: int = 11) -> str:
    """
    R-PP-05：識別含 CONN_KEYWORDS 的連線 label，在其前一行插入白底 rect。
    rect 規格：fill=white, fill-opacity=0.85, rx=2
    必須先插入 rect 再繪製 text（SVG 繪製順序）。
    """
    def replacer(m):
        full_tag = m.group(0)
        text_content = m.group(1)

        # 判斷是否為連線 label（含 CONN_KEYWORDS）
        if not any(kw.lower() in text_content.lower() for kw in CONN_KEYWORDS):
            return full_tag

        # 提取 x, y 座標
        x_m = re.search(r'\bx="([^"]+)"', full_tag)
        y_m = re.search(r'\by="([^"]+)"', full_tag)
        if not x_m or not y_m:
            return full_tag

        try:
            tx = float(x_m.group(1))
            ty = float(y_m.group(1))
        except ValueError:
            return full_tag

        w = estimate_width(text_content)
        rect = (
            f'<rect x="{tx - 4:.1f}" y="{ty - font_size:.1f}" '
            f'width="{w}" height="{font_size + 4}" '
            f'fill="white" fill-opacity="0.85" rx="2"/>\n'
        )
        return rect + full_tag

    # 匹配 SVG text 元素（單行）
    return re.sub(
        r'(<text[^>]*>)([^<]+)(</text>)',
        lambda m: replacer(m.group(0).replace(m.group(0),
            m.group(0))) if any(kw.lower() in m.group(2).lower() for kw in CONN_KEYWORDS)
            else m.group(0),
        svg_content
    )


def add_label_backgrounds_v2(svg_content: str, font_size: int = 11) -> str:
    """
    R-PP-05（改進版）：使用逐行處理方式，為連線 label 插入白底 rect。
    注意：Zone title 的白底遮罩由 elevate_zone_titles() 負責（z-order 問題）。
    """
    lines = svg_content.split('\n')
    result = []
    for line in lines:
        if '<text' not in line:
            result.append(line)
            continue

        text_m = re.search(r'>([^<]+)<', line)
        if not text_m:
            result.append(line)
            continue

        text_content = text_m.group(1)
        is_conn = any(f'>{kw}' in line or f' {kw}' in line for kw in CONN_KEYWORDS)

        if is_conn:
            x_m = re.search(r'\bx="([^"]+)"', line)
            y_m = re.search(r'\by="([^"]+)"', line)
            if x_m and y_m:
                try:
                    tx = float(x_m.group(1))
                    ty = float(y_m.group(1))
                    w = estimate_width(text_content)
                    rect = (
                        f'<rect x="{tx - 4:.1f}" y="{ty - font_size:.1f}" '
                        f'width="{w}" height="{font_size + 4}" '
                        f'fill="white" fill-opacity="0.85" rx="2"/>'
                    )
                    result.append(rect)
                except (ValueError, AttributeError):
                    pass
        result.append(line)
    return '\n'.join(result)


# ─────────────────────────────────────────────────────────────
# Step 7b: elevate_container_titles() — 所有容器標題 halo + z-order 提升
# ─────────────────────────────────────────────────────────────
def _collect_container_titles(svg_content: str) -> list:
    """
    掃描 SVG 中所有容器標題（Zone 標題 + 子群組標題），回傳清單。

    D2 的 SVG 結構中，容器標題緊接在 shape group 的 </g> 之後：
      <g class="shape"><rect .../></g><text ...>TITLE</text>

    識別方式：
      - Zone 容器標題：class="text-bold fill-N1"，含 ｜ 分隔符
      - 子群組標題：class="text fill-N1"（非 bold、非 italic）

    排除：
      - 節點名稱：class="text-bold fill-N1"，不含 ｜（在 shape 內部）
      - 連線 label：class="text-italic fill-N2"
    """
    titles = []

    # 匹配 D2 結構：</g> 後緊接的 <text>（容器標題）
    pattern = r'</g>\s*(<text\b([^>]*)>([^<]+)</text>)'
    for m in re.finditer(pattern, svg_content):
        full_tag = m.group(1)
        attrs = m.group(2)
        text_content = m.group(3)

        # 排除連線 label（italic）
        if 'text-italic' in attrs:
            continue

        # 區分容器標題 vs 節點名稱：
        # - Zone 容器標題：text-bold + 含 ｜
        # - 子群組標題：text fill-N1（非 bold）
        # - 節點名稱：text-bold + 不含 ｜ → 排除
        is_zone = ZONE_TITLE_SEPARATOR in text_content
        is_subgroup = 'class="text fill-N1"' in full_tag
        if not is_zone and not is_subgroup:
            continue

        x_m = re.search(r'\bx="([^"]+)"', full_tag)
        y_m = re.search(r'\by="([^"]+)"', full_tag)
        if not x_m or not y_m:
            continue

        titles.append({"tag": full_tag})
    return titles


def elevate_zone_titles(svg_content: str) -> str:
    """
    為所有容器標題（Zone + 子群組）加上 text halo 光暈效果。
    使用地圖學標準技法 paint-order: stroke fill，
    讓文字帶白色描邊輪廓，從交叉的連線中浮起。
    線條保持完整不斷開。
    """
    titles = _collect_container_titles(svg_content)
    if not titles:
        return svg_content

    # ── Text Halo：文字描邊光暈 ──
    halo_zone = 5     # Zone 標題（16px 字體）較粗的 halo
    halo_sub = 4      # 子群組標題（13px 字體）較細的 halo
    overlay_parts = ['  <!-- Container Title Halo Overlay (cartographic technique) -->',
                     '  <g id="zone-title-overlay">']
    for t in titles:
        tag = t["tag"]
        is_zone = ZONE_TITLE_SEPARATOR in tag
        hw = halo_zone if is_zone else halo_sub
        halo_style = (f'stroke:white;stroke-width:{hw};'
                      f'stroke-linejoin:round;paint-order:stroke fill;')
        halo_tag = tag.replace('style="', f'style="{halo_style}')
        overlay_parts.append(f'    {halo_tag}')
    overlay_parts.append('  </g>')
    overlay_svg = '\n'.join(overlay_parts)

    # 注入到內層 D2 SVG 的第一個 </svg> 前（座標系一致）
    first_close = svg_content.find('</svg>')
    if first_close >= 0:
        svg_content = svg_content[:first_close] + overlay_svg + '\n' + svg_content[first_close:]

    return svg_content


# ─────────────────────────────────────────────────────────────
# Step 7c: displace_overlapping_labels() — 連線 label 與容器標題重疊位移
# ─────────────────────────────────────────────────────────────
def displace_overlapping_labels(svg_content: str) -> str:
    """
    偵測連線 label (text-italic) 與容器標題 (text-bold/text fill-N1) 的
    垂直重疊，將重疊的連線 label 向上或向下位移，同時同步調整 D2 mask
    中對應的黑色遮罩 rect。
    """
    # 收集容器標題位置
    title_zones = []  # [(y, x, half_w)]
    for m in re.finditer(r'</g>\s*<text\b([^>]*)>([^<]+)</text>', svg_content):
        attrs, txt = m.group(1), m.group(2)
        if 'text-italic' in attrs:
            continue
        is_zone = ZONE_TITLE_SEPARATOR in txt
        is_sub = 'class="text fill-N1"' in attrs
        if not is_zone and not is_sub:
            continue
        x = float(re.search(r'x="([^"]+)"', attrs).group(1))
        y = float(re.search(r'y="([^"]+)"', attrs).group(1))
        fs = int(re.search(r'font-size:(\d+)', attrs).group(1)) if re.search(r'font-size:(\d+)', attrs) else 16
        w_est = estimate_width(txt)
        w_est = int(w_est * (1.5 if is_zone else 1.0))
        title_zones.append((y, x, w_est / 2, fs))

    if not title_zones:
        return svg_content

    # 掃描連線 label，檢查是否與任何標題重疊
    shift_amount = 28  # 位移量（px）
    shifts = {}  # { original_y: new_y }

    def check_overlap(label_tag_match):
        tag = label_tag_match.group(0)
        attrs = label_tag_match.group(0)
        if 'text-italic' not in attrs:
            return tag

        lx_m = re.search(r'\bx="([^"]+)"', tag)
        ly_m = re.search(r'\by="([^"]+)"', tag)
        if not lx_m or not ly_m:
            return tag
        lx = float(lx_m.group(1))
        ly = float(ly_m.group(1))

        for (ty, tx, thw, tfs) in title_zones:
            dy = abs(ly - ty)
            dx = abs(lx - tx)
            # 垂直接近（< tfs+8）且水平有交集（dx < 半寬之和）
            if dy < tfs + 8 and dx < thw + 200:
                # 向上或向下位移，選離標題更遠的方向
                new_y = ly - shift_amount if ly <= ty else ly + shift_amount
                shifts[ly] = new_y
                return tag.replace(f'y="{ly_m.group(1)}"', f'y="{new_y:.6f}"')
        return tag

    svg_content = re.sub(
        r'<text\b[^>]*class="text-italic[^>]*>[^<]+</text>',
        check_overlap, svg_content
    )

    # 同步調整 mask 中對應的黑色 rect（D2 的 label gap）
    if shifts:
        mask_start = svg_content.find('<mask ')
        mask_end = svg_content.find('</mask>')
        if mask_start >= 0 and mask_end >= 0:
            mask_section = svg_content[mask_start:mask_end]

            def shift_mask_rect(rect_match):
                rect = rect_match.group(0)
                ry = float(rect_match.group(1))
                # mask rect y 通常 = label y - ~16 (font offset)
                for orig_y, new_y in shifts.items():
                    if abs(ry - (orig_y - 16)) < 8:
                        delta = new_y - orig_y
                        new_ry = ry + delta
                        return rect.replace(
                            f'y="{rect_match.group(1)}"',
                            f'y="{new_ry:.1f}"'
                        )
                return rect

            new_mask = re.sub(
                r'<rect x="[^"]+" y="([^"]+)" width="\d+" height="\d+" fill="black"></rect>',
                shift_mask_rect, mask_section
            )
            svg_content = svg_content[:mask_start] + new_mask + svg_content[mask_end:]

    return svg_content


# ─────────────────────────────────────────────────────────────
# Step 8b: set_paper_size() — 設定 A1 圖紙物理尺寸
# ─────────────────────────────────────────────────────────────
def set_paper_size(svg_content: str, width_mm: str = "841mm", height_mm: str = "594mm") -> str:
    """
    將 SVG 根元素的 width/height 設為實體圖紙尺寸（A1 橫向：841mm × 594mm）。
    viewBox 保持像素座標不變，瀏覽器/印表機據此將圖縮放至 A1 紙面。
    以 xmlns 識別根元素，避免誤改 SVG 內部嵌套的 <svg> 子元素。
    """
    def replace_root_svg(m: re.Match) -> str:
        tag = m.group(0)
        # 移除既有 width/height（如有）
        tag = re.sub(r'\s+width="[^"]*"', '', tag)
        tag = re.sub(r'\s+height="[^"]*"', '', tag)
        # 在結尾 > 前插入 width height
        return tag[:-1] + f' width="{width_mm}" height="{height_mm}">'

    svg_content = re.sub(
        r'<svg\b[^>]*xmlns="http://www\.w3\.org/2000/svg"[^>]*>',
        replace_root_svg,
        svg_content, count=1, flags=re.DOTALL
    )
    return svg_content


# ─────────────────────────────────────────────────────────────
# Step 8: update_canvas() — 更新 viewBox/height（R-PP-01）
# ─────────────────────────────────────────────────────────────
def update_canvas(svg_content: str, original_bbox: dict, extra_h: int = 0, extra_w: int = 0) -> str:
    """
    R-PP-01 Step 8：更新 viewBox 的 width 和 height。
    新 height = 原始 height + TITLE_HEIGHT + extra_h
    新 width  = 原始 width + extra_w（右側延伸放 Legend 時使用）
    """
    orig_h = original_bbox["height"]
    orig_w = original_bbox["width"]
    new_h = orig_h + TITLE_HEIGHT + extra_h
    new_w = orig_w + extra_w

    # 更新 viewBox
    svg_content = re.sub(
        r'viewBox="[^"]*"',
        f'viewBox="0 0 {new_w:.0f} {new_h:.0f}"',
        svg_content, count=1
    )
    # 更新 <svg ...> 標籤內的 height 屬性（用 callback 避免 lookbehind）
    svg_content = re.sub(
        r'(<svg\b[^>]*?\s)height="[^"]*"',
        lambda m: m.group(1) + f'height="{new_h:.0f}"',
        svg_content, count=1, flags=re.DOTALL
    )
    return svg_content


# ─────────────────────────────────────────────────────────────
# 主流程：八步驟（R-PP-01）
# ─────────────────────────────────────────────────────────────
def optimize(input_path: str, output_path: str, project_yaml: str = None):
    """
    R-PP-01：八步驟後製流程，順序不可改變。
    Step 1  parse_svg()
    Step 2  remove_d2_artifacts()
    Step 3  shift_content(+110px)
    Step 4  fix_dasharray()
    Step 5  inject_title_bar()
    Step 6  find_empty_zone() + inject_legend()
    Step 7  add_label_backgrounds()
    Step 8  update_canvas() + write()
    """
    # 載入 project.yaml（如果有）
    project = {}
    if project_yaml and Path(project_yaml).exists():
        with open(project_yaml, encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        project = cfg.get("project", {})
    else:
        print("[WARN] 未指定 project.yaml，Title Bar 將使用預設文字。")

    # 讀取原始 SVG
    raw = Path(input_path).read_text(encoding="utf-8")
    print(f"[Step 0] 讀入：{input_path}  ({len(raw)} bytes)")

    # Step 1: parse_svg
    _, bbox = parse_svg(raw)
    canvas_w = bbox["width"]
    canvas_h = bbox["height"]
    print(f"[Step 1] 畫布尺寸：{canvas_w:.0f} × {canvas_h:.0f}")

    # Step 2: remove_d2_artifacts（R-PP-01 Step 2）
    svg = remove_d2_artifacts(raw)
    print("[Step 2] 移除 D2 殘留 title/legend")

    # 計算 legend 尺寸（Step 6 用）
    _legend_rows = max(len(LEGEND_COMPONENTS), len(LEGEND_CONNECTIONS))
    _legend_h = 30 + 16 + _legend_rows * 27 + 14   # header_h=30, top_pad=16, row_h=27
    _legend_w = 500

    # Step 6 預掃描：在 shift 之前（原始座標空間）找空白區域
    # 畫布寬度不足 Legend 3 倍時，跳過嵌入掃描（避免窄圖面 Legend 重疊）
    _min_w_for_inline = max(_legend_w * 12, 6000)  # 至少 6000px 寬才嘗試嵌入（只有 PROT 等超寬圖才嵌入）
    if canvas_w >= _min_w_for_inline:
        _raw_lx, _raw_ly = find_empty_zone(
            svg, canvas_w, canvas_h,
            legend_w=_legend_w, legend_h=_legend_h, y_start=20
        )
    else:
        _raw_lx, _raw_ly = -1, -1
    _extra_w = 0  # 額外畫布寬度（右側延伸）
    if _raw_lx >= 0:
        # 找到圖內空白：換算到 shift 後座標（加 TITLE_HEIGHT）
        lx = _raw_lx
        ly = _raw_ly + TITLE_HEIGHT
        _extra_h = 0
        _legend_placement = "圖內空白"
    else:
        # 找不到空白：Legend 放在圖面右側延伸區域
        # Legend 頂部在 Title Bar 下方留足間距，避免深藍色視覺融合
        lx = int(canvas_w) + 30
        ly = TITLE_HEIGHT // 2 + 30
        _extra_h = max(0, _legend_h + 40 - int(canvas_h))  # 只在 Legend 超出高度時延伸
        _extra_w = _legend_w + 60  # 畫布右側延伸
        _legend_placement = "右側延伸"

    # Step 3: shift_content（R-PP-01 Step 3，必須在 Step 5 之前）
    svg = shift_content(svg, TITLE_HEIGHT)
    print(f"[Step 3] 主圖元素向下位移 +{TITLE_HEIGHT}px")

    # Step 4: fix_dasharray（R-PP-04）
    before = svg.count("stroke-dasharray")
    svg = fix_dasharray(svg)
    print(f"[Step 4] fix_dasharray 完成（共處理 {before} 個 dasharray 屬性）")

    # Step 5: inject_title_bar（R-PP-02）
    # 主 Title Bar 覆蓋原始圖面寬度；右側延伸一條細窄色帶銜接 Legend
    svg = inject_title_bar(svg, project, canvas_w,
                           bar_width=canvas_w, extend_w=_extra_w)
    print("[Step 5] Title Bar 注入完成")

    # Step 6: inject_legend（R-PP-03）
    svg = inject_legend(svg, lx, ly)
    print(f"[Step 6] Legend 浮層注入完成（位置：x={lx}, y={ly}，{_legend_placement}）")

    # Step 7: add_label_backgrounds（R-PP-05）
    svg = add_label_backgrounds_v2(svg)
    print("[Step 7] 連線 label 白底遮罩完成")

    # Step 7b: elevate_zone_titles — 容器標題 halo 提升至最頂層
    svg = elevate_zone_titles(svg)
    print("[Step 7b] 容器標題 halo 提升完成")

    # Step 7c: displace_overlapping_labels — 連線 label 避讓容器標題
    svg = displace_overlapping_labels(svg)
    print("[Step 7c] 連線 label 重疊位移完成")

    # Step 8: update_canvas + write（R-PP-01 Step 8）
    svg = update_canvas(svg, bbox, extra_h=_extra_h, extra_w=_extra_w)

    # Step 8b: 設定 A1 圖紙物理尺寸（橫向 841mm × 594mm）
    svg = set_paper_size(svg, "841mm", "594mm")
    print("[Step 8b] A1 圖紙尺寸設定完成（841mm × 594mm 橫向）")

    out = Path(output_path)
    out.write_text(svg, encoding="utf-8")
    new_size = len(svg)
    print(f"[Step 8] 輸出：{out}  ({new_size} bytes)")
    print("[OK] 後製完成")


def main():
    parser = argparse.ArgumentParser(
        description="OT 架構圖 SVG 後製優化腳本 v1.0"
    )
    parser.add_argument("--input", "-i", required=True,
                        help="輸入 SVG 路徑（D2 render 輸出的 _raw.svg）")
    parser.add_argument("--output", "-o", default=None,
                        help="輸出 SVG 路徑（預設：輸入檔名去掉 _raw 後綴）")
    parser.add_argument("--project", "-p", default="project.yaml",
                        help="project.yaml 路徑（用於讀取 Title Bar 文字）")
    args = parser.parse_args()

    inp = Path(args.input)
    if not inp.exists():
        print(f"[ERROR] 找不到輸入檔案：{inp}", file=sys.stderr)
        sys.exit(1)

    # 預設輸出路徑：移除 _raw 後綴或加上 _final
    if args.output:
        out = args.output
    else:
        stem = inp.stem.replace("_raw", "")
        out = str(inp.parent / f"{stem}_final.svg")

    optimize(str(inp), out, args.project)


if __name__ == "__main__":
    main()
