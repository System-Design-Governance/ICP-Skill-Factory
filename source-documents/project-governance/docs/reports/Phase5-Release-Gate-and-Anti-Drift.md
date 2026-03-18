# PHASE 5：Release Gate 與防漂移機制（v1.1）

**產出日期**：2026-02-11
**執行者**：治理系統鑑識與重構總工程師
**適用範圍**：本文件為治理文件集部署前最終閘門與日常維護防漂移規則

---

## Part A：部署前置檢查清單（Release Gate Checklist）

> **任何文件修訂或新版本部署前，必須通過以下所有檢查項目。**

### A-1：Dataverse 欄位存在性驗證

| # | 檢查項目 | 驗證方法 | 通過標準 |
|:-:|---------|---------|---------|
| A-1.1 | 所有 Flow-only 欄位存在於 Dataverse | 逐表比對 Doc 02 欄位定義與實際環境 | 零差異 |
| A-1.2 | 所有 Flow-only 欄位已啟用 Column Security | 每欄位 Advanced → Enable column security = On | 100% |
| A-1.3 | gov_isfrozen 與 gov_frozendate 存在於 Document Register | Tables → gov_documentregister → Columns | 欄位可見 |
| A-1.4 | gov_sahandoverevent 資料表存在 | Tables 列表搜尋 | 資料表可見 |
| A-1.5 | Counter List 有 7 筆種子記錄 | 查詢 gov_counterlist 記錄數 | 7 筆 |
| A-1.6 | 所有 Choice Set 值與 Doc 02 一致（含 gov_documentrole, gov_deliverablepackage） | 逐 Choice 比對 | 零差異，22 個 Choice Set |
| A-1.7 | gov_documentregister 包含 gov_documentrole, gov_deliverablepackage, gov_supersededby 欄位 | Columns 標籤檢查 | 3 欄位可見 |
| A-1.8 | gov_projectregistry 包含 15 個 Link 欄位（含 RequirementTraceability, DesignObjectInventory, DocumentRegister, ChangeImpact） | Columns 標籤計算 URL 型別欄位 | 15 欄位 |
| A-1.9 | Document Baseline Matrix 存在於 Doc 02 | 搜尋 Doc 02「Document Baseline Matrix」章節 | 存在 16 列映射 |

### A-2：Flow 寫入白名單驗證

| # | 檢查項目 | 驗證方法 | 通過標準 |
|:-:|---------|---------|---------|
| A-2.1 | Doc 05 每個 Flow 的 Dataverse 寫入欄位皆存在於 Doc 02 | 交叉比對 Flow 步驟中的欄位與 Doc 02 定義 | 零孤兒欄位 |
| A-2.2 | Doc 06 GOV-017 監控清單涵蓋 Doc 02 所有 Flow-only 欄位 | 比對 FlowOnlyFields JSON 與 Doc 02 Flow-only 標記 | 零遺漏 |
| A-2.3 | Doc 06 Schema 名稱全部使用 gov_ 前綴 | 全文搜尋 `cr_` | 零命中 |
| A-2.4 | Doc 06 OData Entity Set 名稱對應表完整 | 比對 Doc 02 資料表清單 | 零缺漏 |

### A-3：Form → Flow 映射完整性驗證

| # | 檢查項目 | 驗證方法 | 通過標準 |
|:-:|---------|---------|---------|
| A-3.1 | Doc 04 每個 Form 映射的 Flow ID 唯一 | 掃描 Form-Flow 映射表 | 零重複 |
| A-3.2 | Doc 04 每個 Flow ID 在 Doc 05 有對應施工步驟 | 交叉比對 | 零遺漏（或有明確「待補」標記） |
| A-3.3 | Doc 04 System Architect 欄位使用 Lookup (User) 而非 Email 字串 | 檢查欄位分類矩陣 | Lookup (User) |

### A-4：Guardrail 可驗證性

| # | 檢查項目 | 驗證方法 | 通過標準 |
|:-:|---------|---------|---------|
| A-4.1 | GOV-017 Checkpoint 機制已描述 | 搜尋 Doc 06 `GOV017_LastCheckpoint` | 存在 |
| A-4.2 | GOV-018 HTTP 認證已設定 | 搜尋 Doc 06 `Active Directory OAuth` | 存在 |
| A-4.3 | Doc 06 升級規則（Level 1-4）完整定義 | 檢查通知與升級規則章節 | 4 層級完整 |

### A-5：測試覆蓋率

| # | 檢查項目 | 驗證方法 | 通過標準 |
|:-:|---------|---------|---------|
| A-5.1 | Doc 07 每個 E2E 測試場景有對應的 Form + Flow | 比對 Phase 2 一致性矩陣 | ≥ 80% 覆蓋 |
| A-5.2 | Doc 07 所有 Flow ID 引用與 Doc 04/05 一致 | 交叉比對 | 零矛盾 |
| A-5.3 | Doc 07 反作弊測試涵蓋所有 Flow-only 欄位類別 | 檢查測試案例 | ≥ 3 個 Entity 覆蓋 |
| A-5.4 | Doc 07 包含 Baseline Seeding 測試（E2E-014） | 檢查 E2E-014 存在 | 存在 |
| A-5.5 | Doc 07 包含 Version Progression 測試（E2E-015, E2E-016） | 檢查 E2E-015/016 存在 | 存在 |
| A-5.6 | Doc 07 包含 Link 目標規則測試（E2E-017） | 檢查 E2E-017 存在 | 存在 |

### A-6：文件版本一致性

| # | 檢查項目 | 驗證方法 | 通過標準 |
|:-:|---------|---------|---------|
| A-6.1 | 所有文件標頭版本號與版本歷史最新條目一致 | 逐文件比對 | 零矛盾 |
| A-6.2 | 所有版本歷史有日期與變更說明 | 逐文件檢查 | 無空白條目 |
| A-6.3 | manifest.json 中的文件清單與實際文件一致 | 比對 | 零差異 |

### Release Gate 通過判定

```
Release Gate 簽核記錄
=====================
檢查日期：____年____月____日
檢查者：________________（姓名 + 職稱）

A-1 Dataverse 欄位存在性：____ / 9 項通過
A-2 Flow 寫入白名單：      ____ / 4 項通過
A-3 Form→Flow 映射：       ____ / 3 項通過
A-4 Guardrail 可驗證性：   ____ / 3 項通過
A-5 測試覆蓋率：           ____ / 6 項通過
A-6 文件版本一致性：       ____ / 3 項通過

總計：____ / 28 項通過

Gate 判定：[ ] 通過 — 可部署
           [ ] 未通過 — 禁止部署

未通過項目清單：
1. ________________
2. ________________

簽核者簽名：________________
```

---

## Part B：防漂移規則（Anti-Drift Rules）

> **以下規則為日常維護的強制約束。違反任何規則需觸發 Governance Function 審查。**

### B-1：文件修訂防漂移規則

| Rule ID | 規則 | 觸發條件 | 必要動作 |
|---------|------|---------|---------|
| ADR-001 | **新增/修改 Flow 必須同步更新一致性矩陣** | 任何 GOV Flow 的新增或修改 | 更新 Phase 2 一致性矩陣對應列，確認 Form→Flow→Dataverse→SharePoint→Guardrail→Test 鏈完整 |
| ADR-002 | **新增 Dataverse 欄位必須更新 Flow-only 白名單** | 新增任何標記為 Flow-only 的欄位 | (1) Doc 02 新增欄位定義 (2) Doc 06 GOV-017 FlowOnlyFields JSON 新增 (3) FLS Profile 新增欄位 |
| ADR-003 | **新增治理場景必須更新測試案例** | 新增任何 Form/Flow 治理場景 | (1) Doc 07 新增對應 E2E 測試案例 (2) 更新一致性矩陣 |
| ADR-004 | **修改 Choice Set 必須同步所有引用文件** | 新增/修改/刪除 Choice 值 | (1) Doc 02 更新定義 (2) Doc 04 更新 Dropdown 選項 (3) Doc 06 更新偵測條件（若適用） |
| ADR-005 | **修改 SharePoint 結構必須同步 Doc 01 + Doc 03 + Doc 00B** | 修改資料夾結構或權限設計 | 三份文件必須同步更新，不得出現矛盾 |
| ADR-006 | **文件版本號必須遞增** | 任何文件內容修改 | (1) 標頭版本 +0.1 (2) 版本歷史新增條目 (3) Changelog 記錄 |
| ADR-007 | **修改 DocumentType→Folder 映射必須從 Doc 02 Baseline Matrix 開始** | 新增/修改 DocumentType 或 SharePoint 資料夾對應 | (1) Doc 02 Baseline Matrix 為唯一修改點 (2) Doc 03/05/Appendix A 的對應表自動跟隨，不得獨立修改 |
| ADR-008 | **新增 DocumentType 必須同步 Baseline Seeding 邏輯** | 新增 RequiredForGate ≠ '-' 的 DocumentType | (1) Doc 02 Baseline Matrix 新增映射 (2) Doc 05 GOV-001 Baseline Seeding Array 新增條目 (3) Doc 07 E2E-014 更新預期記錄數 |
| ADR-009 | **Version Progression 規則不可繞過** | 任何 Document Register 寫入 | GOV-005 必須執行版本推進：新上傳 = Draft，舊版 = Superseded，Link 回寫遵循 Approved > Draft 規則 |
| ADR-010 | **Link 回寫必須遵循 Doc 02 Baseline Matrix 的 ProjectRegistryLinkField** | GOV-005 更新 Project Registry Link | 不得使用硬編碼映射，必須依據 Baseline Matrix 的 ProjectRegistryLinkField 欄位 |

### B-2：Schema 防漂移規則

| Rule ID | 規則 | 自動化檢查方式 |
|---------|------|--------------|
| ADR-S01 | **禁止使用 cr_ 前綴** | 全文搜尋所有 .md 文件，`cr_` 命中數必須為 0 |
| ADR-S02 | **所有 Dataverse Schema Name 必須使用 gov_ 前綴** | 正則搜尋 `[^g]ov_` + `cr_` + `new_` 等非標準前綴 |
| ADR-S03 | **OData Entity Set Name 必須使用複數形式** | 比對 Doc 06 Entity Set 對應表 |

### B-3：權威文件防漂移規則

| Rule ID | 規則 | 說明 |
|---------|------|------|
| ADR-A01 | **Dataverse 資料模型以 Doc 02 為唯一真相** | 其他文件引用的欄位型別、名稱必須與 Doc 02 一致 |
| ADR-A02 | **SharePoint 架構以 Doc 03 為唯一真相** | 資料夾結構、權限矩陣以 Doc 03 為準 |
| ADR-A03 | **Flow 施工步驟以 Doc 05 為唯一實作依據** | Appendix A 僅供參考，不得作為實作依據 |
| ADR-A04 | **Guardrail 語意以 Doc 06 為唯一權威** | 違規判定標準、偵測邏輯以 Doc 06 為準 |
| ADR-A05 | **Doc 01 SharePoint 權限必須與 Doc 03 保持一致** | 任何權限修改需同步兩份文件 |
| ADR-A06 | **DocumentType→Folder→LinkField 映射以 Doc 02 Baseline Matrix 為唯一權威** | Doc 03/05/Appendix A 的對應表為快速參考副本，不得獨立維護 |

### B-4：跨文件一致性自動檢查腳本（建議）

```bash
#!/bin/bash
# governance-consistency-check.sh
# 每次文件修改後執行，或納入 CI/CD Pipeline

echo "=== 治理文件一致性檢查 ==="

# 檢查 1：cr_ 前綴殘留
echo "[CHECK 1] Schema 前綴檢查..."
CR_COUNT=$(grep -r "cr_" docs/power-platform-governance/zh-TW/*.md | grep -v "Changelog" | wc -l)
if [ "$CR_COUNT" -gt 0 ]; then
  echo "  FAIL: 發現 $CR_COUNT 處 cr_ 前綴殘留"
  grep -rn "cr_" docs/power-platform-governance/zh-TW/*.md | grep -v "Changelog"
else
  echo "  PASS: 無 cr_ 前綴殘留"
fi

# 檢查 2：版本標頭一致性
echo "[CHECK 2] 版本標頭一致性..."
for f in docs/power-platform-governance/zh-TW/0[1-7]*.md; do
  HEADER_VER=$(grep -m1 "文件版本" "$f" | grep -oP 'v[\d.]+')
  LATEST_VER=$(grep -oP 'v[\d.]+' "$f" | tail -1)
  if [ "$HEADER_VER" != "$LATEST_VER" ]; then
    echo "  WARN: $f 標頭 $HEADER_VER ≠ 最新歷史 $LATEST_VER"
  fi
done

# 檢查 3：Flow ID 唯一性
echo "[CHECK 3] Flow ID 唯一性..."
DUPES=$(grep -oP 'GOV-\d+' docs/power-platform-governance/zh-TW/04*.md | sort | uniq -d)
if [ -n "$DUPES" ]; then
  echo "  FAIL: 發現重複 Flow ID: $DUPES"
else
  echo "  PASS: 無重複 Flow ID"
fi

# 檢查 4：GOV-017 監控欄位覆蓋率
echo "[CHECK 4] GOV-017 監控欄位覆蓋率..."
FLOW_ONLY_COUNT=$(grep -c "Flow-only.*Yes\|**Yes**" docs/power-platform-governance/zh-TW/02*.md)
MONITOR_COUNT=$(grep -c "gov_" docs/power-platform-governance/zh-TW/06*.md | head -1)
echo "  INFO: Doc 02 Flow-only 欄位約 $FLOW_ONLY_COUNT 個，Doc 06 監控引用約 $MONITOR_COUNT 處"

echo "=== 檢查完成 ==="
```

---

## Part C：變更管理流程

### C-1：文件修改標準流程

```
Step 1: 提出修改需求
    │
    ├── 描述修改原因
    ├── 識別影響的文件清單
    └── 識別影響的 ADR 規則
    │
Step 2: 執行跨文件影響分析
    │
    ├── 使用一致性矩陣確認影響範圍
    ├── 列出所有需同步修改的文件
    └── 列出需更新的 Choice Set / Schema
    │
Step 3: 執行修改
    │
    ├── 修改所有受影響文件
    ├── 更新所有版本號
    └── 更新所有版本歷史
    │
Step 4: 執行 Release Gate Checklist
    │
    ├── 完成 Part A 所有 22 項檢查
    └── 簽核 Release Gate
    │
Step 5: 執行防漂移自動檢查
    │
    └── 執行 governance-consistency-check.sh
    │
Step 6: 核准與發布
    │
    ├── Governance Function 審核
    ├── make 重新建置 PDF/DOCX
    └── 發布新版本
```

### C-2：禁止行為

| 禁止行為 | 原因 | 後果 |
|---------|------|------|
| 單獨修改一份文件而不檢查跨文件影響 | 造成文件間矛盾 | 觸發鑑識審查 |
| 跳過 Release Gate 直接部署 | 無法確保一致性 | 部署無效 |
| 修改內容但不遞增版本號 | 版本追溯斷裂 | 觸發稽核警報 |
| 新增 Flow 但不更新一致性矩陣 | 治理覆蓋缺口 | 場景鏈斷裂 |
| 新增 Flow-only 欄位但不更新 GOV-017 | Guardrail 盲區 | 安全漏洞 |

---

## Part D：本次鑑識修訂後之系統健康狀態

### D-1：修訂前後對比

| 指標 | 修訂前 | 修訂後 | 改善 |
|------|--------|--------|------|
| FATAL 級別缺陷 | 6 | **0** | -6 |
| GOV BREACH 缺陷 | 9 | **4**（殘留需另案） | -5 |
| AUDIT CHAIN 斷裂 | 3 | **0** | -3 |
| DRIFT 缺陷 | 8 | **2**（殘留需另案） | -6 |
| 場景鏈斷裂率 | 41%（9/22） | **18%**（4/22，均為 Flow 缺失場景） | -23pp |
| Schema 前綴正確率 | ~50%（Doc 06 全錯） | **100%** | +50pp |
| 版本標頭一致率 | 71%（5/7 正確） | **100%** | +29pp |

### D-2：殘留項目（需另案處理）

| 項目 | 類型 | 影響 | 建議時程 |
|------|------|------|---------|
| GOV-006~012 施工規格缺失 | GOV BREACH | 7 個場景無法建置 | 下一輪迭代 |
| BOM Registry Form/Flow 缺失 | GOV BREACH | BOM 場景無法操作 | 下一輪迭代 |
| Escalation 自動化 Flow | GOV BREACH | 升級規則僅手動執行 | 下一輪迭代 |
| OnHold 解除機制 | DRIFT | 狀態凍結無法恢復 | 下一輪迭代 |

### D-3：部署就緒判定

```
╔═══════════════════════════════════════════════════════════════╗
║                     部署就緒判定                               ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  ✅ FATAL 缺陷：全部消除（6/6）                                ║
║  ✅ Schema 一致性：100%                                        ║
║  ✅ 版本追溯：完整                                             ║
║  ✅ 權威文件衝突：已解決                                       ║
║  ✅ Release Gate Checklist：已建立                             ║
║  ✅ 防漂移規則：已定義（10 條文件規則 + 3 條 Schema 規則 + 6 條權威文件規則） ║
║                                                               ║
║  ⚠️ 殘留項目：4 項（均為功能缺口，非結構性錯誤）               ║
║     不影響已覆蓋場景之部署                                      ║
║                                                               ║
║  判定：可部署已覆蓋之 15/22 場景                                ║
║        另 7 場景待 GOV-006~012 補齊後啟用                       ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

**PHASE 5 v1.1 更新完成。新增 Baseline Seeding / Version Progression / Link Target 相關 Release Gate 項目與 Anti-Drift 規則。**
