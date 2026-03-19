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

# Legend 資料（元件類型 + 連線類型）
LEGEND_COMPONENTS = [
    ("矩形(深藍框)", "SCADA / Historian",  "#0C3467"),
    ("矩形(天藍框)", "HMI / NTP Server",   "#008EC3"),
    ("菱形(紅框)",   "防火牆 Firewall",     "#c0392b"),
    ("六角(天藍框)", "Switch PRP",          "#008EC3"),
    ("六角(琥珀框)", "Protocol Gateway",    "#F5A623"),
    ("矩形(琥珀框)", "RTU / IED",           "#F5A623"),
    ("矩形(灰框)",   "Field IED / ENG WS",  "#9B9B9B"),
    ("六角(深藍框)", "RedBox",              "#0C3467"),
    ("矩形(虛線框)", "外部系統",            "#9B9B9B"),
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
def inject_title_bar(svg_content: str, project: dict, canvas_width: float) -> str:
    """
    R-PP-02：注入固定規格的品牌 Title Bar。
    高度：110px，y=0~110
    背景：#0C3467（Navy Primary）
    左側裝飾條：x=0~6, height=110, fill=#008EC3（Sky Blue）
    三行文字：主標題(y=40)/副標題(y=66)/標準行(y=88)
    """
    name    = project.get("name", "OT Architecture Diagram")
    site    = project.get("site", "")
    rev     = project.get("rev", "1.0")
    date    = project.get("date", "")
    std     = project.get("standard", "IEC 62443")
    cx      = canvas_width / 2

    subtitle = f"{site}  Rev {rev}  {date}".strip()
    std_line = f"Purdue Model / ISA-95 / {std} Zone &amp; Conduit"

    title_bar = f"""
  <!-- R-PP-02: Title Bar -->
  <g id="title-bar">
    <rect x="0" y="0" width="{canvas_width}" height="{TITLE_HEIGHT}" fill="#0C3467"/>
    <rect x="0" y="0" width="6" height="{TITLE_HEIGHT}" fill="#008EC3"/>
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
                    y_start: int = 130) -> tuple[int, int]:
    """
    R-PP-06：以 100px 步進掃描，找第一個完全空白的矩形區域。
    收集所有元素 bounding box，判斷候選區域是否與任何元素重疊。
    找不到時 fallback 到左上角 (30, y_start)。
    """
    # 收集所有 rect 與 g transform 的座標（簡化版：提取所有 x/y 屬性）
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
            occupied.append((ox, oy, ox + ow, oy + oh))
        except (ValueError, AttributeError):
            pass

    def overlaps(cx, cy):
        """候選區域 (cx, cy, cx+legend_w, cy+legend_h) 是否與任何元素重疊"""
        for ox, oy, ox2, oy2 in occupied:
            if not (cx + legend_w <= ox or cx >= ox2 or
                    cy + legend_h <= oy or cy >= oy2):
                return True
        return False

    step = 100
    # 確保掃描範圍不超出畫布（Legend 右邊界不超出）
    max_x = int(canvas_width) - legend_w - 20
    max_y = int(canvas_height) - legend_h - 20
    for y in range(y_start, max(y_start + 1, max_y), step):
        for x in range(10, max(11, max_x), step):
            if not overlaps(x, y):
                return x, y

    # R-PP-06 fallback：靠左上角 Title Bar 下方
    return 30, y_start


# ─────────────────────────────────────────────────────────────
# Step 6b: inject_legend() — 注入 Legend 浮層（R-PP-03）
# ─────────────────────────────────────────────────────────────
def inject_legend(svg_content: str, lx: int, ly: int) -> str:
    """
    R-PP-03：Legend 嵌入浮層，雙欄設計。
    左欄：元件類型；右欄：連線類型。
    不硬編碼座標，由 find_empty_zone() 決定位置（R-PP-06）。
    """
    row_h   = 27
    header_h = 28
    n_rows  = max(len(LEGEND_COMPONENTS), len(LEGEND_CONNECTIONS))
    leg_w   = 490
    leg_h   = header_h + n_rows * row_h + 16
    col_sep = 244

    rows_svg = []
    for i in range(n_rows):
        ry = header_h + 8 + i * row_h

        # 左欄：元件
        if i < len(LEGEND_COMPONENTS):
            shape_label, comp_label, color = LEGEND_COMPONENTS[i]
            rows_svg.append(
                f'  <rect x="{lx+12}" y="{ly+ry-10}" width="18" height="14" '
                f'fill="white" stroke="{color}" stroke-width="1.5" rx="1"/>'
            )
            rows_svg.append(
                f'  <text x="{lx+36}" y="{ly+ry+2}" font-family="Arial,sans-serif" '
                f'font-size="11" fill="#1a1a1a">{comp_label}</text>'
            )

        # 右欄：連線
        if i < len(LEGEND_CONNECTIONS):
            line_label, conn_label, color, dashed = LEGEND_CONNECTIONS[i]
            lx2 = lx + col_sep + 12
            dash_attr = 'stroke-dasharray="5,3"' if dashed else ''
            rows_svg.append(
                f'  <line x1="{lx2}" y1="{ly+ry-4}" x2="{lx2+22}" y2="{ly+ry-4}" '
                f'stroke="{color}" stroke-width="2" {dash_attr}/>'
            )
            rows_svg.append(
                f'  <text x="{lx2+28}" y="{ly+ry+2}" font-family="Arial,sans-serif" '
                f'font-size="11" fill="#1a1a1a">{conn_label}</text>'
            )

    legend_svg = f"""
  <!-- R-PP-03: Legend 浮層（位置由 find_empty_zone() 決定，R-PP-06）-->
  <g id="legend-overlay">
    <rect x="{lx}" y="{ly}" width="{leg_w}" height="{leg_h}"
          fill="white" fill-opacity="0.93" stroke="#0C3467" stroke-width="1.5" rx="6"
          filter="drop-shadow(2px 2px 6px rgba(0,0,0,0.15))"/>
    <rect x="{lx}" y="{ly}" width="{leg_w}" height="{header_h}"
          fill="#0C3467" rx="6"/>
    <rect x="{lx}" y="{ly+header_h//2}" width="{leg_w}" height="{header_h//2}" fill="#0C3467"/>
    <text x="{lx + leg_w//2}" y="{ly+19}" font-family="Arial,sans-serif" font-size="11"
          font-weight="bold" fill="white" text-anchor="middle">圖例 / Legend</text>
    <line x1="{lx+col_sep}" y1="{ly+header_h+4}" x2="{lx+col_sep}" y2="{ly+leg_h-4}"
          stroke="#9B9B9B" stroke-width="0.5"/>
    {''.join(rows_svg)}
  </g>"""

    # 注入在 </svg> 前
    svg_content = re.sub(r'(</svg>)', legend_svg + r'\n\1', svg_content)
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
    R-PP-05（改進版）：使用逐行處理方式，更穩定地插入白底 rect。
    """
    lines = svg_content.split('\n')
    result = []
    for line in lines:
        # 檢查此行是否為含連線關鍵字的 text 元素
        if '<text' in line and any(f'>{kw}' in line or f' {kw}' in line
                                   for kw in CONN_KEYWORDS):
            x_m = re.search(r'\bx="([^"]+)"', line)
            y_m = re.search(r'\by="([^"]+)"', line)
            text_m = re.search(r'>([^<]+)<', line)
            if x_m and y_m and text_m:
                try:
                    tx = float(x_m.group(1))
                    ty = float(y_m.group(1))
                    text_content = text_m.group(1)
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
def update_canvas(svg_content: str, original_bbox: dict, extra_h: int = 0) -> str:
    """
    R-PP-01 Step 8：更新 viewBox 和 height。
    新 height = 原始 height + TITLE_HEIGHT + extra_h（Legend 區域等額外空間）
    避免使用可變寬度 lookbehind（Python re 不支援）。
    """
    orig_h = original_bbox["height"]
    orig_w = original_bbox["width"]
    new_h = orig_h + TITLE_HEIGHT + extra_h

    # 更新 viewBox
    svg_content = re.sub(
        r'viewBox="[^"]*"',
        f'viewBox="0 0 {orig_w:.0f} {new_h:.0f}"',
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

    # Step 3: shift_content（R-PP-01 Step 3，必須在 Step 5 之前）
    svg = shift_content(svg, TITLE_HEIGHT)
    print(f"[Step 3] 主圖元素向下位移 +{TITLE_HEIGHT}px")

    # Step 4: fix_dasharray（R-PP-04）
    before = svg.count("stroke-dasharray")
    svg = fix_dasharray(svg)
    print(f"[Step 4] fix_dasharray 完成（共處理 {before} 個 dasharray 屬性）")

    # Step 5: inject_title_bar（R-PP-02）
    svg = inject_title_bar(svg, project, canvas_w)
    print("[Step 5] Title Bar 注入完成")

    # Step 6: inject_legend（R-PP-03）
    # Legend 放在圖表內容下方，避免與圖層 rect 重疊（R-PP-06 修正）
    # 計算 legend 高度
    _legend_rows = max(len(LEGEND_COMPONENTS), len(LEGEND_CONNECTIONS))
    _legend_h = 28 + _legend_rows * 27 + 16   # header_h=28, row_h=27
    _legend_w = 490
    # 垂直：緊接圖表內容底部 + 20px 間距
    ly = int(canvas_h) + TITLE_HEIGHT + 20
    # 水平：居中，不超出畫布左右
    lx = max(10, int((canvas_w - _legend_w) // 2))
    svg = inject_legend(svg, lx, ly)
    print(f"[Step 6] Legend 浮層注入完成（位置：x={lx}, y={ly}）")

    # Step 7: add_label_backgrounds（R-PP-05）
    svg = add_label_backgrounds_v2(svg)
    print("[Step 7] 連線 label 白底遮罩完成")

    # Step 8: update_canvas + write（R-PP-01 Step 8）
    # 新高度 = 原始高度 + Title Bar + Legend 區域（含下邊距）
    svg = update_canvas(svg, bbox, extra_h=_legend_h + 40)

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
