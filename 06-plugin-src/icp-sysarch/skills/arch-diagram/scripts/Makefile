# ============================================================
# Makefile — OT 架構圖自動化產圖 Pipeline
# 版本：v1.0  |  2026-03-04
# 用法：make PROJECT=project.yaml [all|gen|render|optimize|check|clean]
# ============================================================

PROJECT     ?= project.yaml
D2_OUTPUT   ?= output.d2
SVG_RAW     ?= diagram_raw.svg
SVG_FINAL   ?= diagram_final.svg
LIBRARY     ?= component_library.yaml

PYTHON      ?= python
D2          ?= d2

.PHONY: all gen render optimize check clean help

## 預設目標：完整流程（SOP Step 1~6）
all: gen render optimize check
	@echo ""
	@echo "=============================="
	@echo "  Pipeline 完成！"
	@echo "  最終輸出：$(SVG_FINAL)"
	@echo "=============================="

## Step 3：產生 D2 源碼
gen:
	@echo "[Step 3] 產生 D2 源碼..."
	$(PYTHON) gen_d2.py $(PROJECT) --output $(D2_OUTPUT) --library $(LIBRARY)

## Step 4：D2 render
render:
	@echo "[Step 4] D2 render..."
	$(D2) $(D2_OUTPUT) $(SVG_RAW)

## Step 5：SVG 後製
optimize:
	@echo "[Step 5] SVG 後製..."
	$(PYTHON) optimize_svg.py --input $(SVG_RAW) --output $(SVG_FINAL) --project $(PROJECT)

## Step 6：碰撞檢查
check:
	@echo "[Step 6] 碰撞檢查..."
	$(PYTHON) check_collision.py $(SVG_FINAL)

## 清除產出物
clean:
	@echo "[Clean] 移除產出檔案..."
	rm -f $(D2_OUTPUT) $(SVG_RAW) $(SVG_FINAL)

## 只驗證設定（不輸出檔案）
validate:
	@echo "[Validate] 驗證 project.yaml..."
	$(PYTHON) gen_d2.py $(PROJECT) --library $(LIBRARY) --dry-run

## 顯示說明
help:
	@echo "OT 架構圖自動化產圖 Pipeline v1.0"
	@echo ""
	@echo "用法："
	@echo "  make all        完整流程（gen + render + optimize + check）"
	@echo "  make gen        只產生 D2 源碼"
	@echo "  make render     只執行 D2 render"
	@echo "  make optimize   只執行 SVG 後製"
	@echo "  make check      只執行碰撞檢查"
	@echo "  make validate   只驗證 project.yaml（不輸出）"
	@echo "  make clean      清除所有產出物"
	@echo ""
	@echo "自訂參數："
	@echo "  make all PROJECT=my_project.yaml"
	@echo "  make all SVG_FINAL=my_diagram.svg"
