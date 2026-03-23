#!/usr/bin/env python3
"""
check_collision.py — OT 架構圖 A 類碰撞快速檢查
版本：v1.0  |  2026-03-04
用法：python check_collision.py diagram_final.svg

依據 OT_Architecture_Framework_v1.0.md §5.3 實作：
  a_class == 0    → Green  ✅ 優秀
  a_class 1~4    → Yellow ⚠️ 可接受
  a_class >= 5   → Red    ❌ 必須修正，更新 Rulebook
"""

import sys
import re
import argparse
from pathlib import Path

# Windows CP950 環境下強制 UTF-8 輸出，以支援 emoji 狀態符號（M-002 修正）
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


# ─────────────────────────────────────────────────────────────
# 連線路徑關鍵字（用於識別連線元素）
# ─────────────────────────────────────────────────────────────
CONN_KEYWORDS = {
    'PRP', 'IEC', 'IEEE', 'Modbus', 'RS-485', 'RS485', 'Ethernet',
    'OPC', 'IRIG', 'GOOSE', 'MMS', 'Fiber', 'RF', 'PSTN', 'VPN',
    'LAN', 'PTP', 'DNP', 'Wireless'
}


def parse_text_elements(svg_content: str) -> list[dict]:
    """
    提取所有 <text> 元素的位置與內容。
    回傳 list of {x, y, text, is_conn_label}
    """
    elements = []
    # 匹配 <text x="..." y="...">content</text>
    pattern = re.compile(
        r'<text[^>]*\bx="([^"]+)"[^>]*\by="([^"]+)"[^>]*>([^<]*)</text>',
        re.DOTALL
    )
    for m in pattern.finditer(svg_content):
        try:
            x = float(m.group(1))
            y = float(m.group(2))
            text = m.group(3).strip()
            is_conn = any(kw.lower() in text.lower() for kw in CONN_KEYWORDS)
            elements.append({"x": x, "y": y, "text": text, "is_conn": is_conn})
        except ValueError:
            pass
    return elements


def parse_path_segments(svg_content: str) -> list[list[tuple]]:
    """
    提取所有 <path> 元素的線段列表。
    每個 path 回傳 [(x1,y1,x2,y2), ...] 線段列表。
    支援 M/L/H/V/C/Q 命令，忽略 Z。
    """
    paths = []
    pattern = re.compile(r'<path\b[^>]+\bd="([^"]+)"', re.DOTALL)

    def parse_d(d: str):
        """將 SVG path d 屬性解析為線段列表"""
        segments = []
        # 分割指令
        tokens = re.findall(r'[MLHVCSQTAZmlhvcsqtaz]|[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?', d)
        cx, cy = 0.0, 0.0
        sx, sy = 0.0, 0.0  # 起始點（for Z）
        i, cmd = 0, 'M'
        while i < len(tokens):
            t = tokens[i]
            if t.isalpha():
                cmd = t
                i += 1
                continue
            try:
                if cmd in ('M', 'm'):
                    x, y = float(tokens[i]), float(tokens[i+1])
                    if cmd == 'm': x, y = cx + x, cy + y
                    cx, cy = x, y; sx, sy = x, y; i += 2; cmd = 'L' if cmd == 'M' else 'l'
                elif cmd in ('L', 'l'):
                    x, y = float(tokens[i]), float(tokens[i+1])
                    if cmd == 'l': x, y = cx + x, cy + y
                    segments.append((cx, cy, x, y)); cx, cy = x, y; i += 2
                elif cmd in ('H', 'h'):
                    x = float(tokens[i]); x = (cx + x) if cmd == 'h' else x
                    segments.append((cx, cy, x, cy)); cx = x; i += 1
                elif cmd in ('V', 'v'):
                    y = float(tokens[i]); y = (cy + y) if cmd == 'v' else y
                    segments.append((cx, cy, cx, y)); cy = y; i += 1
                elif cmd in ('C', 'c'):
                    x1,y1,x2,y2,x,y = [float(tokens[i+j]) for j in range(6)]
                    if cmd == 'c': x1,y1,x2,y2,x,y = cx+x1,cy+y1,cx+x2,cy+y2,cx+x,cy+y
                    segments.append((cx, cy, x, y)); cx, cy = x, y; i += 6
                elif cmd in ('Q', 'q'):
                    x1,y1,x,y = [float(tokens[i+j]) for j in range(4)]
                    if cmd == 'q': x1,y1,x,y = cx+x1,cy+y1,cx+x,cy+y
                    segments.append((cx, cy, x, y)); cx, cy = x, y; i += 4
                elif cmd in ('S', 's'):
                    x2,y2,x,y = [float(tokens[i+j]) for j in range(4)]
                    if cmd == 's': x2,y2,x,y = cx+x2,cy+y2,cx+x,cy+y
                    segments.append((cx, cy, x, y)); cx, cy = x, y; i += 4
                elif cmd in ('Z', 'z'):
                    segments.append((cx, cy, sx, sy)); cx, cy = sx, sy; i += 0; cmd = 'M'
                    continue
                else:
                    i += 1
            except (IndexError, ValueError):
                i += 1
        return segments

    for m in pattern.finditer(svg_content):
        segs = parse_d(m.group(1))
        if segs:
            total_len = sum(((x2-x1)**2 + (y2-y1)**2)**0.5 for x1,y1,x2,y2 in segs)
            if total_len > 200:  # 只保留足夠長的連線
                paths.append(segs)
    return paths


def point_to_segment_dist(px, py, x1, y1, x2, y2) -> float:
    """計算點 (px,py) 到線段 (x1,y1)-(x2,y2) 的最短距離"""
    dx, dy = x2 - x1, y2 - y1
    if dx == 0 and dy == 0:
        return ((px-x1)**2 + (py-y1)**2) ** 0.5
    t = max(0, min(1, ((px-x1)*dx + (py-y1)*dy) / (dx*dx + dy*dy)))
    return ((px - (x1 + t*dx))**2 + (py - (y1 + t*dy))**2) ** 0.5


# Zone 容器標題的識別前綴（排除在碰撞計算之外）
# Zone 標題本身不是節點，與穿越的連線不算真正碰撞
ZONE_LABEL_PREFIXES = ("Level ", "DMZ｜", "zone", "核心交換", "饋線邊緣交換",
                       "R 群", "太陽能", "Protocol Gateway", "MCC 群", "STATCOM",
                       "TPC RTU", "RTU 盤",
                       "Field Control", "Field Devices",  # M-004：精確前綴，避免誤判 "Field IED"
                       "Supervisory Control", "Enterprise")


def quick_collision_check(svg_path: str) -> dict:
    """
    A 類碰撞檢查：連線路徑穿越「葉節點」文字（R-D2-04）。

    演算法：
    1. 提取所有文字元素，排除 Zone 容器標題與連線 label
    2. 提取所有足夠長的連線路徑（> 200px）的實際線段
    3. 計算每條線段到葉節點文字中心的精確距離
    4. 距離 < DIST_THRESHOLD 且非路徑端點處 → 真正穿越，計為碰撞

    回傳：{
      'a_class': int,      # A 類碰撞數（葉節點文字被穿越）
      'affected': list,    # 受影響的節點名稱
      'status': str,       # 'green' / 'yellow' / 'red'
    }
    """
    content = Path(svg_path).read_text(encoding="utf-8")
    texts = parse_text_elements(content)
    all_path_segs = parse_path_segments(content)

    # 葉節點文字：排除連線 label 與 Zone 容器標題
    def is_zone_label(t: dict) -> bool:
        text = t["text"]
        return (text.startswith(ZONE_LABEL_PREFIXES) or
                len(text) > 35 or          # 長字串通常是 Zone/sub-zone 標題
                "｜" in text)              # 含全形｜的是 Zone 主標題

    leaf_texts = [t for t in texts if not t["is_conn"] and not is_zone_label(t)]

    affected = []
    DIST_THRESHOLD = 10   # px：文字中心到線段的距離閾值（小於此值視為穿越）
    ENDPOINT_MARGIN = 25  # px：路徑整體端點附近，視為合理連線端點，不算穿越

    for segs in all_path_segs:
        if not segs:
            continue
        # 整條路徑的起點與終點（用於排除合理的連線端點接觸）
        path_x0, path_y0 = segs[0][0], segs[0][1]
        path_xn, path_yn = segs[-1][2], segs[-1][3]

        for txt in leaf_texts:
            tx = txt["x"] + max(len(txt["text"]) * 3, 20)  # 文字中心 x（估算）
            ty = txt["y"] - 4                               # 文字中心 y

            name = txt["text"][:35].strip() if txt["text"] else "(無標籤)"
            if name in affected:
                continue

            for x1, y1, x2, y2 in segs:
                d = point_to_segment_dist(tx, ty, x1, y1, x2, y2)
                if d < DIST_THRESHOLD:
                    # 排除路徑整體端點附近（連線端點合理接觸節點）
                    d_start = ((tx - path_x0)**2 + (ty - path_y0)**2) ** 0.5
                    d_end   = ((tx - path_xn)**2 + (ty - path_yn)**2) ** 0.5
                    if d_start > ENDPOINT_MARGIN and d_end > ENDPOINT_MARGIN:
                        affected.append(name)
                        break

    a_class = len(affected)

    if a_class == 0:
        status = "green"
    elif a_class <= 4:
        status = "yellow"
    else:
        status = "red"

    return {
        "a_class": a_class,
        "affected": affected,
        "status": status,
    }


def main():
    parser = argparse.ArgumentParser(
        description="OT 架構圖 A 類碰撞快速檢查 v1.0"
    )
    parser.add_argument("svg_path", help="待檢查的 SVG 檔案路徑")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="顯示所有受影響節點的詳細列表")
    args = parser.parse_args()

    p = Path(args.svg_path)
    if not p.exists():
        print(f"[ERROR] 找不到 SVG 檔案：{p}", file=sys.stderr)
        sys.exit(1)

    print(f"[INFO] 正在檢查：{p}")
    result = quick_collision_check(str(p))

    a = result["a_class"]
    s = result["status"]
    affected = result["affected"]

    # 狀態顯示（M-002：使用 emoji，stdout 已切換為 UTF-8）
    STATUS_ICON = {"green": "Green \u2705", "yellow": "Yellow \u26a0\ufe0f", "red": "Red \u274c"}
    STATUS_MSG = {
        "green":  "優秀（無 A 類碰撞）",
        "yellow": "可接受（建議調整拓撲以改善）",
        "red":    "必須修正！請調整子群組宣告順序或設 connected_to: null",
    }

    print(f"\n{'='*50}")
    print(f"  A 類碰撞數：{a}  →  {STATUS_ICON[s]}")
    print(f"  狀態：{STATUS_MSG[s]}")
    print(f"{'='*50}")

    if affected:
        print(f"\n  受影響節點（{len(affected)} 個）：")
        for i, name in enumerate(affected[:20], 1):   # 最多顯示 20 個
            print(f"    {i:2d}. {name}")
        if len(affected) > 20:
            print(f"    ... 共 {len(affected)} 個（使用 --verbose 查看全部）")
    elif args.verbose:
        print("\n  受影響節點：無")

    if args.verbose and affected:
        print(f"\n  完整受影響節點列表：")
        for i, name in enumerate(affected, 1):
            print(f"    {i:2d}. {name}")

    # exit code：red = 1，否則 0
    sys.exit(1 if s == "red" else 0)


if __name__ == "__main__":
    main()
