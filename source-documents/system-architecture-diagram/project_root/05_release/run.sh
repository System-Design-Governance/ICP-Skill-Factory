#!/usr/bin/env bash
# ============================================================
# run.sh — OT 架構圖自動化產圖 Pipeline（bash 版本）
# 版本：v1.0  |  2026-03-04
# 用法：bash run.sh [project.yaml] [output_name]
# 範例：bash run.sh project.yaml TPC_HSUEH_L1_R1.0
# ============================================================

set -euo pipefail

PROJECT="${1:-project.yaml}"
OUTPUT_BASE="${2:-diagram}"
D2_OUTPUT="${OUTPUT_BASE}.d2"
SVG_RAW="${OUTPUT_BASE}_raw.svg"
SVG_FINAL="${OUTPUT_BASE}_final.svg"
LIBRARY="${LIBRARY:-component_library.yaml}"

echo "=============================================="
echo "  OT 架構圖自動化產圖 Pipeline v1.0"
echo "  Project : $PROJECT"
echo "  Library : $LIBRARY"
echo "  Output  : $SVG_FINAL"
echo "=============================================="

# ── Step 3：產生 D2 源碼 ──────────────────────────────────
echo ""
echo "[Step 3] 產生 D2 源碼..."
python gen_d2.py "$PROJECT" --output "$D2_OUTPUT" --library "$LIBRARY"
echo "[OK] D2 源碼：$D2_OUTPUT"

# ── Step 4：D2 render ─────────────────────────────────────
echo ""
echo "[Step 4] D2 render..."
d2 "$D2_OUTPUT" "$SVG_RAW"
echo "[OK] SVG raw：$SVG_RAW"

# ── Step 5：SVG 後製 ──────────────────────────────────────
echo ""
echo "[Step 5] SVG 後製..."
python optimize_svg.py \
    --input  "$SVG_RAW"   \
    --output "$SVG_FINAL" \
    --project "$PROJECT"

# ── Step 6：碰撞檢查 ──────────────────────────────────────
echo ""
echo "[Step 6] 碰撞檢查..."
if python check_collision.py "$SVG_FINAL"; then
    echo "[OK] 碰撞檢查通過"
else
    STATUS=$?
    if [ $STATUS -eq 1 ]; then
        echo ""
        echo "[WARN] A 類碰撞 ≥ 5，建議調整 project.yaml 後重新執行"
        echo "  常見調整："
        echo "    1. 調整 feeder_groups 順序（影響 edge switch 位置）"
        echo "    2. 將特定設備的 connected_to 設為 null（省略長線）"
        echo ""
        echo "  重新執行：bash run.sh $PROJECT $OUTPUT_BASE"
        # 不中止（警告即可，供 Controller 決定是否修正）
    fi
fi

# ── 完成 ───────────────────────────────────────────────────
echo ""
echo "=============================================="
echo "  Pipeline 完成！"
echo "  最終輸出：$SVG_FINAL"
echo "  檔案大小：$(wc -c < "$SVG_FINAL") bytes"
echo "=============================================="
