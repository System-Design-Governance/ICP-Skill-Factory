---
name: large-doc-search
description: |
  將大型 PDF 文件（數百至數千頁）拆解為結構化知識庫，並支援精準查詢。
  涵蓋兩個階段：(1) 建檔——解析 PDF、按章節拆分、產生索引；
  (2) 查詢——讀取索引、定位相關章節、載入上下文後回答。

  MANDATORY TRIGGERS — 當使用者提到以下任何情境時使用此 Skill：
  大型文件搜尋、手冊查詢、PDF 知識庫、文件拆分、章節索引、
  產品手冊、技術手冊、規格書查詢、large document, manual search,
  PDF knowledge base, document indexing, chapter search,
  或使用者上傳超過 50 頁的 PDF 並詢問其中內容，
  或使用者提到已建立的知識庫目錄（含 index.json）並想查詢資料。
  也適用於：建立知識庫、ingest PDF、拆分文件、手冊搜尋、
  technical manual, product manual, specification document, 規格書,
  保護電驛手冊, equipment manual, 設備手冊。
  觸發關鍵詞：建檔、建索引、建知識庫、拆分PDF成章節、查詢知識庫、
  手冊太長想快速查、ingest, index a manual, split PDF into chapters,
  ABB, Siemens, IEC standards, 數百頁, 數千頁, 500-page, 1000-page。
  不要用於：小型 PDF 擷取、PDF 合併轉換、RAG pipeline、向量資料庫。
---

# Large Document Search Skill

本 Skill 讓你能對任何大型 PDF 文件進行結構化拆解與精準查詢，無需外部 API 或向量資料庫。

## 運作原理

整個流程分為兩個完全解耦的階段：

**Phase 1 — 建檔（Ingest）**：將一份大型 PDF 拆分成以章節為單位的 Markdown 檔案，並產生一份輕量級索引（index.json）。這是一次性的前置作業。

**Phase 2 — 查詢（Query）**：收到使用者提問時，先讀索引找到相關章節，再按需載入章節內容來回答。每次查詢只需讀取少量檔案，不需要把整份手冊塞進 context。

---

## Phase 1：建檔（Ingest）

### 什麼時候進入建檔模式

當使用者做了以下任何一件事：
- 上傳一份大型 PDF（通常 50 頁以上）
- 明確說「建立知識庫」「建檔」「ingest」「拆分這份 PDF」

### 建檔步驟

1. **確認輸入**：確認 PDF 檔案路徑，以及使用者想把知識庫存在哪裡。如果使用者沒指定，用 PDF 檔名（去掉副檔名）作為知識庫名稱，放在工作目錄下。

2. **執行 ingest 腳本**：
   ```bash
   python3 <skill-path>/scripts/ingest.py <input.pdf> --output <kb_directory>
   ```

   可用選項（通常用預設值即可）：

   | 參數 | 預設 | 說明 |
   |------|------|------|
   | `--method` | `auto` | 章節偵測：`bookmark` / `toc` / `heading` / `auto`（依序嘗試） |
   | `--lang` | `auto` | 語言，影響關鍵字提取（`zh` 時用 jieba） |
   | `--max-chapter-chars` | `80000` | 超過此字數的章節會自動拆分子章節 |
   | `--extract-tables` | `true` | 是否獨立抽取表格 |
   | `--summary-method` | `extractive` | `extractive`（自動擷取關鍵句）或 `none` |

3. **檢查輸出**：腳本完成後，驗證知識庫目錄結構：
   ```
   {kb_name}/
   ├── index.json          ← 總索引
   ├── chapters/           ← 分章節 Markdown
   │   ├── ch01_xxx.md
   │   └── ...
   ├── tables/             ← 獨立表格
   │   └── ...
   └── metadata.json       ← PDF 元資訊
   ```

4. **回報結果**：告訴使用者建檔完成，列出偵測到的章節數量與知識庫路徑。如果偵測到問題（如 PDF 加密、掃描式 PDF 無文字），主動告知並建議解決方案。

### 建檔的邊界情況

| 狀況 | 你應該怎麼做 |
|------|-------------|
| PDF 加密 | 請使用者提供密碼，用 `--password` 選項 |
| 掃描式 PDF（純圖片） | 告知需先 OCR 處理，可用 pdf skill 的 OCR 功能 |
| 偵測不到章節結構 | 腳本會 fallback 到固定頁數切分（每 30 頁），告知使用者結果可能不理想 |
| 知識庫已存在 | 詢問使用者要覆蓋還是建立新版本 |
| 安裝缺少依賴 | 執行 `pip install pypdf pdfplumber --break-system-packages` |

---

## Phase 2：查詢（Query）

### 什麼時候進入查詢模式

當同時滿足以下條件：
- 使用者提出一個問題
- 工作目錄中有知識庫目錄（含 index.json）

### 查詢步驟

#### Step 1：定位知識庫

- 用 Glob 搜尋 `**/index.json`（maxdepth 3）找出所有知識庫
- 如果有多個 KB，先列出所有 `kb_name` + `source_file` + `total_pages`，根據問題自動選擇
- 使用者提到品牌或產品名稱時，用 `kb_name` / `source_file` 匹配

#### Step 2：判斷查詢類型並分流

收到問題後，先判斷屬於哪種類型，不同類型用不同策略。這是本 skill 的核心價值——根據問題性質選擇最有效的查找路徑，而不是每次都走「讀索引 → 找章節 → 載入」的通用流程。

**類型 A — 規格查詢**（問數值、範圍、溫度、精度、扭力等）
識別訊號：問題含「多少」「範圍」「規格」「spec」「值」或具體單位詞（°C, V, Hz, ms, N-m, AWG）

→ **表格優先策略**：
1. 先用 Glob 列出 `tables/*.md` 所有檔案名稱
2. 從檔名和 index 的 `related_tables` 中挑出可能相關的表格（通常 <2K chars）
3. 直接載入這些表格——表格通常就能完整回答規格問題
4. 只有表格不夠時，才載入對應章節正文補充說明
5. 回答格式：表格 + 來源頁碼

**類型 B — 跨知識庫比較**（比較兩個產品、品牌、方案）
識別訊號：問題含「比較」「差異」「vs」「哪個好」或同時提到兩個產品/品牌名

→ **跨 KB 比較協議**：
1. 讀取雙方的 index.json
2. 建立功能維度對照表：將雙方章節按功能域配對（如 A 的「合閘控制」對 B 的「Closing Stage」）
3. 按維度逐一載入雙方對應章節（或表格），每次只比較一個維度
4. 比較表格中的具體參數值，不是只描述「有支援」
5. 回答格式必須是：
   - 結構化比較表（每個維度一張表）
   - 每格標註來源（KB名/章節/頁碼）
   - 最後一段「關鍵差異總結」

**類型 C — 存在性/模糊查詢**（「有沒有提到 X」「哪裡講到 Y」）
識別訊號：問題含「有沒有」「哪裡」「是否提到」或使用者只給了模糊的產品描述

→ **Grep 快篩策略**：
1. 先用 Grep 在 `chapters/` 和 `tables/` 目錄搜尋關鍵字，output_mode="count"
2. 根據匹配次數排序，找出真正有內容的章節
3. 再讀 index.json 確認章節的 title 和 summary
4. 只載入 Grep 確認有提及的章節（避免靠「語意猜測」載入不相關章節）

**類型 D — 概念/原理查詢**（問「怎麼運作」「原理」「流程」）
→ 讀 index → summary 語意比對 → 載入章節 → 回答（傳統流程）

**類型 E — 頁碼/定位查詢**（「在第幾章」「目錄」）
→ 直接從 index 回答，不需載入任何章節

#### Step 3：載入控制

- 單次載入的總字數不超過 **120,000 字元**（約 30K tokens）
- 表格檔案（通常 <2K chars）不計入主要額度，可以多載幾個
- 優先載入 `char_count` 較小的章節（同等相關度時）
- 超過上限時，先回答已載入的部分，告知使用者還有哪些未載入

#### Step 4：回答

- **必須標註來源**：格式為「根據 {KB名} 第 X 章 {章節名}（p.XXX-YYY）」
- 涉及數值時，優先用表格呈現，標註原始頁碼
- 比較類問題，每個表格格子都標註來源 KB
- 找不到答案就明確說找不到，不要猜測
- 如果無法判斷哪個章節相關，列出候選章節讓使用者選擇

---

## 疑難排解

### ingest.py 執行失敗

最常見的原因是缺少 Python 套件。執行：
```bash
pip install pypdf pdfplumber --break-system-packages
```

如果需要中文關鍵字提取（jieba），額外安裝：
```bash
pip install jieba --break-system-packages
```

### 章節偵測品質不佳

可以用 `--method` 參數強制指定偵測方式：
- 有書籤的 PDF → `--method bookmark`
- 有明確目錄頁的 → `--method toc`
- 只能靠標題字體大小判斷的 → `--method heading`

### 索引太大或章節太多

如果 index.json 超過 50 KB，可以考慮：
- 提高 `--max-chapter-chars` 來減少子章節拆分
- 在查詢時只讀取 index 的 `chapters[].title` 和 `chapters[].keywords` 做初步篩選

---

## 資源檔案說明

| 檔案 | 何時閱讀 |
|------|----------|
| `references/query_guide.md` | 需要更深入了解查詢階段的行為規則時 |
| `assets/index_schema.json` | 需要驗證 index.json 格式時 |
| `scripts/ingest.py` | 不需要閱讀，直接執行即可 |
