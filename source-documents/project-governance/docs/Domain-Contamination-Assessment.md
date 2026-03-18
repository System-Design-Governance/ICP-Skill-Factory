# Domain 汙染鑑識報告
# Domain Contamination Assessment

**鑑識日期**：2026-02-08
**鑑識範圍**：整個 System-Design-Governance Repository
**鑑識目的**：識別 Global 層級檔案與 Domain-specific 檔案（Project Governance domain）
**執行者**：Claude Sonnet 4.5
**鑑識模式**：Dry-run（僅報告，不移動或刪除任何檔案）

---

## 執行摘要

### 鑑識結果統計

| 分類 | 數量 | 位置 |
|------|------|------|
| **Global 檔案** | 8 項 | Repository 根目錄 |
| **Domain-specific 檔案** | 13 項 | 分散於 docs/、docs/power-platform-governance/、scripts/ |
| **汙染程度** | **高** | 13/21 檔案 (61.9%) 為 Domain-specific |
| **需移動檔案** | 13 項 | 建議移至 `/domains/project-governance/` |

### 關鍵發現

1. **docs/power-platform-governance/zh-TW/** 目錄下所有 8 個核心文件均為 **Project Governance domain**，包含 **834 處** Domain-specific 關鍵字（PreGate0, Gate0-3, projectstatus, currentgate, GOV-XXX）

2. **所有 3 個 Python 腳本** 均為 Domain-specific，硬編碼 Project Governance 相關欄位與 Flow 編號

3. **docs/ 目錄下 2 個報告** 均為 Domain-specific，專門針對 Project Governance 文件的鑑識與清理報告

4. **全域基礎設施檔案** (Makefile, README.md, ChangeGovernance.md, glossary.yml) 保持乾淨，未被 Domain 汙染

---

## Global 檔案清單（可安全留在根目錄）

### 1. README.md
**判定理由**：Global
- 說明整個 multi-domain governance documentation pipeline
- 列舉 5 個 domains（含 power-platform-governance）
- 描述通用 Makefile 建置流程
- **無 Domain-specific 內容**

**保留位置**：`/README.md`

---

### 2. Makefile
**判定理由**：Global
- 提供所有 domains 通用的建置邏輯
- 使用 `DOMAIN` 與 `LANG` 參數化變數
- 可處理任意 domain 的文件建置
- **無 Domain-specific 內容**

**保留位置**：`/Makefile`

---

### 3. ChangeGovernance.md
**判定理由**：Global
- 定義治理型文件變更控管政策
- 適用於所有 domains 的文件變更流程
- 描述 Git PR 審核原則、RACI 角色、版本控制
- **無 Domain-specific 內容**

**保留位置**：`/ChangeGovernance.md`

---

### 4. glossary.yml
**判定理由**：Global
- 提供通用治理術語映射表（RACI、Gate、Risk、Audit 等）
- 適用於所有 domains 的術語一致性需求
- **關鍵字檢測結果**：0 處 Domain-specific 關鍵字
- **無 Domain-specific 內容**

**保留位置**：`/glossary.yml`

---

### 5. build/
**判定理由**：Global
- Pandoc 輸出目錄（PDF、DOCX）
- 由 Makefile 自動管理
- **無 Domain-specific 內容**

**保留位置**：`/build/`

---

### 6. fonts/
**判定理由**：Global
- 字型檔案目錄（用於 PDF 產生）
- 供所有 domains 共用
- **無 Domain-specific 內容**

**保留位置**：`/fonts/`

---

### 7. styles/
**判定理由**：Global
- CSS 樣式檔案目錄
- 供所有 domains 共用
- **無 Domain-specific 內容**

**保留位置**：`/styles/`

---

### 8. templates/
**判定理由**：Global
- Pandoc 模板目錄（reference.docx, template.tex 等）
- 供所有 domains 共用
- **無 Domain-specific 內容**

**保留位置**：`/templates/`

---

## Domain-specific 檔案清單（需移至 /domains/project-governance/）

### A. Core Documentation Files（核心文件）

#### 1. docs/power-platform-governance/zh-TW/00-index.md
**判定理由**：Domain-specific (Project Governance)
- 標題：「Power Platform 治理系統建置手冊」
- 描述 Project Governance System 實作流程
- 引用 Gate0-3 審查流程
- **Domain-specific 關鍵字**：建置手冊主索引（間接引用所有 Domain-specific 文件）

**建議目標位置**：`/domains/project-governance/docs/power-platform-governance/zh-TW/00-index.md`

---

#### 2. docs/power-platform-governance/zh-TW/01-prerequisites-and-environment.md
**判定理由**：Domain-specific (Project Governance)
- 建立 GOV-Architects、GOV-EngineeringManagement 等 **Project Governance 專用** Security Groups
- 建立 Service Principal 用於 **GOV-XXX Flows**
- **Domain-specific 關鍵字數量**：10 處

**建議目標位置**：`/domains/project-governance/docs/power-platform-governance/zh-TW/01-prerequisites-and-environment.md`

---

#### 3. docs/power-platform-governance/zh-TW/02-dataverse-data-model-and-security.md
**判定理由**：Domain-specific (Project Governance)
- 定義 **gov_projectstatus**、**gov_currentgate** Choice Sets
- 定義 **PreGate0 概念**（projectstatus = Active + currentgate = Pending）
- 定義 **Gate0、Gate1、Gate2、Gate3** OptionSet 值
- 定義 **GOV-XXX Flow-only 欄位** Field-Level Security
- **Domain-specific 關鍵字數量**：112 處

**建議目標位置**：`/domains/project-governance/docs/power-platform-governance/zh-TW/02-dataverse-data-model-and-security.md`

**關鍵證據**：
```markdown
gov_currentgate (Current Gate)：Choice
- 100000000 = Pending (PreGate0 狀態)
- 100000001 = Gate0
- 100000002 = Gate1
- 100000003 = Gate2
- 100000004 = Gate3

gov_projectstatus (Project Status)：Choice
- 100000000 = Active
- 100000001 = OnHold
- 100000002 = Closed
- 100000003 = Terminated
```

---

#### 4. docs/power-platform-governance/zh-TW/03-sharepoint-architecture.md
**判定理由**：Domain-specific (Project Governance)
- 描述 **Gate0、Gate1、Gate2、Gate3** SharePoint 資料夾結構
- 描述 Project Governance 專用文件管理流程
- **Domain-specific 關鍵字數量**：21 處

**建議目標位置**：`/domains/project-governance/docs/power-platform-governance/zh-TW/03-sharepoint-architecture.md`

**關鍵證據**：
```
PRJ-{RequestID}/
├── Gate0/
├── Gate1/
├── Gate2/
└── Gate3/
```

---

#### 5. docs/power-platform-governance/zh-TW/04-powerapps-forms.md
**判定理由**：Domain-specific (Project Governance)
- 實作 Project Governance Canvas App
- 使用 **gov_projectstatus**、**gov_currentgate** 欄位
- 包含 PreGate0、Gate0-3 相關表單邏輯
- **Domain-specific 關鍵字數量**：74 處

**建議目標位置**：`/domains/project-governance/docs/power-platform-governance/zh-TW/04-powerapps-forms.md`

---

#### 6. docs/power-platform-governance/zh-TW/05-core-flows-implementation-runbook.md
**判定理由**：Domain-specific (Project Governance)
- **所有 GOV-XXX Flows 實作手冊**（GOV-001 至 GOV-018）
- 包含 **PreGate0、Gate0、Gate1、Gate2、Gate3** 狀態轉換邏輯
- 包含 **gov_projectstatus**、**gov_currentgate** 欄位操作
- 包含 Appendix D「Project Status Semantics」說明 PreGate0 概念
- **Domain-specific 關鍵字數量**：228 處（最高）

**建議目標位置**：`/domains/project-governance/docs/power-platform-governance/zh-TW/05-core-flows-implementation-runbook.md`

**關鍵證據**：
```markdown
GOV-001：Create Project and Initialize Folder Structure
GOV-013：Gate Approval Request Submission
GOV-015：Gate Approval Decision Processing
...
```

---

#### 7. docs/power-platform-governance/zh-TW/06-guardrails-and-anti-cheating.md
**判定理由**：Domain-specific (Project Governance)
- 描述 **GOV-017** 違規偵測 Flow
- 描述 **GOV-018** 不一致偵測 Flow
- 監控 **gov_currentgate**、**gov_projectstatus** 欄位的非法修改
- **Domain-specific 關鍵字數量**：61 處

**建議目標位置**：`/domains/project-governance/docs/power-platform-governance/zh-TW/06-guardrails-and-anti-cheating.md`

---

#### 8. docs/power-platform-governance/zh-TW/07-testing-and-acceptance.md
**判定理由**：Domain-specific (Project Governance)
- 包含 **E2E-007: PreGate0 狀態驗證** 測試案例
- 包含 **E2E-008: Terminated 異常終止流程** 測試案例
- 包含 **E2E-009: Closed 正常結案流程** 測試案例
- 包含 **Gate0、Gate1、Gate2、Gate3** 測試案例
- **Domain-specific 關鍵字數量**：174 處

**建議目標位置**：`/domains/project-governance/docs/power-platform-governance/zh-TW/07-testing-and-acceptance.md`

---

#### 9. docs/power-platform-governance/zh-TW/appendix/A-core-flows-specification.md
**判定理由**：Domain-specific (Project Governance)
- **GOV-XXX Flows 設計規格**（附錄文件）
- 包含所有 Gate0-3 相關 Flow 規格
- **Domain-specific 關鍵字數量**：154 處

**建議目標位置**：`/domains/project-governance/docs/power-platform-governance/zh-TW/appendix/A-core-flows-specification.md`

---

### B. Forensics and Cleanup Reports（鑑識與清理報告）

#### 10. docs/Consistency-Forensics-Report-Round2.md
**判定理由**：Domain-specific (Project Governance)
- 第二輪一致性鑑識報告
- 專門鑑識 **02、03、04、05、07** 等 Project Governance 文件
- 檢查 **PreGate0、Draft、Completed、Cancelled** 狀態汙染
- 檢查 **cr_ prefix** 與 **900000000 OptionSet 值** 汙染
- **影響範圍**：僅 Project Governance domain

**建議目標位置**：`/domains/project-governance/docs/Consistency-Forensics-Report-Round2.md`

**關鍵證據**（報告內容摘錄）：
```markdown
**鑑識範圍**：語意一致性檢查（Phase 1 & 2 已完成）
**權威來源**：02-dataverse-data-model-and-security.md、05-core-flows-implementation-runbook.md

### ISSUE-R2-001: 使用已淘汰的專案狀態
- Draft → PreGate0 (Active + Pending)
- Completed → Closed
- Cancelled → Terminated
```

---

#### 11. docs/Deleted-Files-Summary.md
**判定理由**：Domain-specific (Project Governance)
- Project Governance 專案清理報告
- 記錄刪除的 **05-Fix-Report.md**、**07-Fix-Report.md** 等 Project Governance 工具報告
- 記錄刪除的 **analyze_choice_fields.py**、**fix_07_document.py** 等 Project Governance 工具腳本
- **影響範圍**：僅 Project Governance domain

**建議目標位置**：`/domains/project-governance/docs/Deleted-Files-Summary.md`

**關鍵證據**（報告內容摘錄）：
```markdown
## 核心交付文件（docs/power-platform-governance/zh-TW/）
1. 00-index.md - 系統概覽與文件索引
2. 01-prerequisites-and-environment.md - 環境建置指南
3. 02-dataverse-data-model-and-security.md - 資料模型與安全（權威來源）
...
```

---

### C. Automation Scripts（自動化腳本）

#### 12. scripts/fix_05_document.py
**判定理由**：Domain-specific (Project Governance)
- 硬編碼 **Project Governance 專用 OptionSet 映射**
- 硬編碼 **gov_currentgate**（Pending, Gate0, Gate1, Gate2, Gate3）
- 硬編碼 **gov_projectstatus**（Active, OnHold, Closed, Terminated）
- 硬編碼 **gov_requeststatus**、**gov_reviewtype** 等 Project Governance 欄位
- **專用於修正 05-core-flows-implementation-runbook.md**
- **無法適用於其他 domains**

**建議目標位置**：`/domains/project-governance/scripts/fix_05_document.py`

**關鍵證據**（程式碼摘錄）：
```python
OPTIONSET_MAPPINGS = {
    'gov_currentgate': {
        '900000000': ('100000000', 'Pending'),
        '900000001': ('100000001', 'Gate0'),
        '900000002': ('100000002', 'Gate1'),
        '900000003': ('100000003', 'Gate2'),
        '900000004': ('100000004', 'Gate3'),
    },
    'gov_projectstatus': {
        '900000000': ('100000000', 'Active'),
        '900000002': ('100000001', 'OnHold'),
        '900000003': ('100000002', 'Closed'),
        '900000004': ('100000003', 'Terminated'),
    },
    ...
}
```

---

#### 13. scripts/enhance_05_operability.py
**判定理由**：Domain-specific (Project Governance)
- 硬編碼 **GOV-001**、**GOV-013**、**GOV-015** Flow 補強內容
- 專用於增強 **05-core-flows-implementation-runbook.md** 操作性
- 包含 Project Governance 專用 Trigger 條件、Preconditions、I/O 定義
- **無法適用於其他 domains**

**建議目標位置**：`/domains/project-governance/scripts/enhance_05_operability.py`

**關鍵證據**（程式碼摘錄）：
```python
FLOW_ENHANCEMENTS = {
    'GOV-001': {
        'trigger': """### Trigger 條件
        **觸發時機**：使用者透過 Power Apps 提交專案建立表單時
        **觸發者**：System Architect
        ...
        """,
        ...
    },
    'GOV-013': { ... },
    'GOV-015': { ... },
}
```

---

#### 14. scripts/round2_forensics.py
**判定理由**：Domain-specific (Project Governance)
- 硬編碼檢查 **03-sharepoint-architecture.md**、**04-powerapps-forms.md**、**07-testing-and-acceptance.md**
- 硬編碼檢查 **Draft、Completed、Cancelled** 已淘汰狀態
- 硬編碼檢查 **PreGate0、Terminated、Closed** 測試覆蓋率
- 專用於產生 **Consistency-Forensics-Report-Round2.md**
- **無法適用於其他 domains**

**建議目標位置**：`/domains/project-governance/scripts/round2_forensics.py`

**關鍵證據**（程式碼摘錄）：
```python
DEPRECATED_STATES = {
    'Draft': {'correct': 'PreGate0 (Active + Pending)', 'optionset': 'N/A'},
    'Completed': {'correct': 'Closed', 'optionset': '100000002'},
    'Cancelled': {'correct': 'Terminated', 'optionset': '100000003'}
}
```

---

## 建議目錄結構重組方案

### 當前結構（存在汙染）

```
System-Design-Governance/
├── README.md (Global)
├── Makefile (Global)
├── ChangeGovernance.md (Global)
├── glossary.yml (Global)
├── build/ (Global)
├── fonts/ (Global)
├── styles/ (Global)
├── templates/ (Global)
├── docs/
│   ├── Consistency-Forensics-Report-Round2.md (Domain-specific - CONTAMINATION!)
│   ├── Deleted-Files-Summary.md (Domain-specific - CONTAMINATION!)
│   └── power-platform-governance/ (Domain-specific - CONTAMINATION!)
│       └── zh-TW/
│           ├── 00-index.md
│           ├── 01-prerequisites-and-environment.md
│           ├── 02-dataverse-data-model-and-security.md
│           ├── 03-sharepoint-architecture.md
│           ├── 04-powerapps-forms.md
│           ├── 05-core-flows-implementation-runbook.md
│           ├── 06-guardrails-and-anti-cheating.md
│           ├── 07-testing-and-acceptance.md
│           └── appendix/
│               └── A-core-flows-specification.md
└── scripts/
    ├── fix_05_document.py (Domain-specific - CONTAMINATION!)
    ├── enhance_05_operability.py (Domain-specific - CONTAMINATION!)
    └── round2_forensics.py (Domain-specific - CONTAMINATION!)
```

---

### 建議結構（乾淨分離）

```
System-Design-Governance/
├── README.md (Global)
├── Makefile (Global)
├── ChangeGovernance.md (Global)
├── glossary.yml (Global)
├── build/ (Global)
├── fonts/ (Global)
├── styles/ (Global)
├── templates/ (Global)
└── domains/  ← NEW: Domain-specific 檔案移至此處
    └── project-governance/  ← NEW: Project Governance domain
        ├── docs/
        │   ├── power-platform-governance/
        │   │   └── zh-TW/
        │   │       ├── 00-index.md
        │   │       ├── 01-prerequisites-and-environment.md
        │   │       ├── 02-dataverse-data-model-and-security.md
        │   │       ├── 03-sharepoint-architecture.md
        │   │       ├── 04-powerapps-forms.md
        │   │       ├── 05-core-flows-implementation-runbook.md
        │   │       ├── 06-guardrails-and-anti-cheating.md
        │   │       ├── 07-testing-and-acceptance.md
        │   │       └── appendix/
        │   │           └── A-core-flows-specification.md
        │   ├── Consistency-Forensics-Report-Round2.md
        │   └── Deleted-Files-Summary.md
        └── scripts/
            ├── fix_05_document.py
            ├── enhance_05_operability.py
            └── round2_forensics.py
```

---

### 檔案移動對照表

| 當前路徑 | 建議目標路徑 | 移動原因 |
|---------|------------|---------|
| `docs/power-platform-governance/` | `domains/project-governance/docs/power-platform-governance/` | 所有 8 個文件包含 834 處 Domain-specific 關鍵字 |
| `docs/Consistency-Forensics-Report-Round2.md` | `domains/project-governance/docs/Consistency-Forensics-Report-Round2.md` | 專門鑑識 Project Governance 文件 |
| `docs/Deleted-Files-Summary.md` | `domains/project-governance/docs/Deleted-Files-Summary.md` | 專門清理 Project Governance 工具 |
| `scripts/fix_05_document.py` | `domains/project-governance/scripts/fix_05_document.py` | 硬編碼 Project Governance OptionSet |
| `scripts/enhance_05_operability.py` | `domains/project-governance/scripts/enhance_05_operability.py` | 硬編碼 GOV-001/013/015 Flows |
| `scripts/round2_forensics.py` | `domains/project-governance/scripts/round2_forensics.py` | 硬編碼 Project Governance 鑑識邏輯 |

---

## 後續影響評估

### Makefile 相容性

**當前 Makefile 使用方式**：
```bash
make DOMAIN=power-platform-governance LANG=zh-TW all
```

**移動後需修改為**：
```bash
make DOMAIN=domains/project-governance/docs/power-platform-governance LANG=zh-TW all
```

**或修改 Makefile 支援新路徑結構**：
```makefile
DOMAIN_DIR := domains/$(DOMAIN)/docs
SRC_DIR := $(DOMAIN_DIR)/$(LANG)
```

---

### 既有 CI/CD Pipeline 影響

如有既有 CI/CD Pipeline（GitHub Actions, Azure DevOps, etc.），需檢查以下項目：

1. **文件路徑引用**
   - 是否硬編碼 `docs/power-platform-governance/zh-TW/` 路徑？
   - 是否需要更新為 `domains/project-governance/docs/power-platform-governance/zh-TW/`？

2. **腳本路徑引用**
   - 是否硬編碼 `scripts/*.py` 路徑？
   - 是否需要更新為 `domains/project-governance/scripts/*.py`？

3. **Pandoc 建置邏輯**
   - 是否依賴固定路徑？
   - 是否需要更新 `DOMAIN` 參數傳遞方式？

---

### Git 歷史保留建議

為保留檔案歷史記錄（Git blame, Git log），建議使用以下方式移動檔案：

```bash
# 保留 Git 歷史的移動方式
git mv docs/power-platform-governance domains/project-governance/docs/power-platform-governance
git mv docs/Consistency-Forensics-Report-Round2.md domains/project-governance/docs/
git mv docs/Deleted-Files-Summary.md domains/project-governance/docs/
git mv scripts/fix_05_document.py domains/project-governance/scripts/
git mv scripts/enhance_05_operability.py domains/project-governance/scripts/
git mv scripts/round2_forensics.py domains/project-governance/scripts/
```

---

## 風險評估與緩解措施

### 風險 1：Makefile 失效

**風險等級**：高
**影響範圍**：所有 PDF/DOCX 建置流程

**緩解措施**：
1. 更新 Makefile，支援 `domains/*/docs/` 路徑結構
2. 保留舊路徑相容模式（透過 symlinks 或條件判斷）
3. 完整測試建置流程後再移動檔案

---

### 風險 2：現有文件內部交叉引用失效

**風險等級**：中
**影響範圍**：00-index.md 等文件內部連結

**緩解措施**：
1. 移動後執行全文搜尋，檢查是否有 `../` 相對路徑引用
2. 更新所有交叉引用連結
3. 測試 Pandoc 轉換後的 PDF/DOCX 連結

---

### 風險 3：Python 腳本路徑硬編碼失效

**風險等級**：中
**影響範圍**：3 個 Python 腳本

**緩解措施**：
1. 檢查腳本內部是否有 `docs/power-platform-governance/` 硬編碼路徑
2. 更新為相對路徑或環境變數
3. 測試腳本在新路徑下是否正常執行

---

## 建議執行步驟（Dry-run 結束後）

### Phase 1：前置作業（估計 30 分鐘）

1. **建立 Git 分支**
   ```bash
   git checkout -b refactor/domain-separation
   ```

2. **建立目標目錄**
   ```bash
   mkdir -p domains/project-governance/docs
   mkdir -p domains/project-governance/scripts
   ```

3. **備份當前 Makefile**
   ```bash
   cp Makefile Makefile.backup
   ```

---

### Phase 2：檔案移動（估計 15 分鐘）

4. **移動文件目錄**
   ```bash
   git mv docs/power-platform-governance domains/project-governance/docs/
   git mv docs/Consistency-Forensics-Report-Round2.md domains/project-governance/docs/
   git mv docs/Deleted-Files-Summary.md domains/project-governance/docs/
   ```

5. **移動腳本目錄**
   ```bash
   git mv scripts/fix_05_document.py domains/project-governance/scripts/
   git mv scripts/enhance_05_operability.py domains/project-governance/scripts/
   git mv scripts/round2_forensics.py domains/project-governance/scripts/
   ```

6. **確認 docs/ 與 scripts/ 目錄清空**
   ```bash
   ls docs/     # 應為空（或僅剩其他 domains）
   ls scripts/  # 應為空（或僅剩 Global 腳本）
   ```

---

### Phase 3：更新 Makefile（估計 30 分鐘）

7. **更新 Makefile 路徑邏輯**
   ```makefile
   # 修改前
   SRC_DIR := docs/$(DOMAIN)/$(LANG)

   # 修改後
   SRC_DIR := domains/$(DOMAIN)/docs/power-platform-governance/$(LANG)
   ```

8. **測試建置流程**
   ```bash
   make DOMAIN=project-governance LANG=zh-TW pdf
   ```

9. **驗證輸出檔案**
   ```bash
   ls build/project-governance/zh-TW/*.pdf
   ```

---

### Phase 4：更新 Python 腳本（估計 20 分鐘）

10. **檢查腳本內部路徑**
    ```bash
    grep -r "docs/power-platform-governance" domains/project-governance/scripts/
    grep -r "../docs" domains/project-governance/scripts/
    ```

11. **更新腳本路徑（如需要）**
    - 將硬編碼路徑改為相對路徑或參數化

12. **測試腳本執行**
    ```bash
    cd domains/project-governance/scripts
    python fix_05_document.py --dry-run
    ```

---

### Phase 5：更新 README.md（估計 15 分鐘）

13. **更新文件路徑說明**
    ```markdown
    # 修改前
    docs/power-platform-governance/zh-TW/

    # 修改後
    domains/project-governance/docs/power-platform-governance/zh-TW/
    ```

14. **更新建置指令範例**
    ```markdown
    # 修改前
    make DOMAIN=power-platform-governance LANG=zh-TW all

    # 修改後
    make DOMAIN=project-governance LANG=zh-TW all
    ```

---

### Phase 6：驗證與提交（估計 30 分鐘）

15. **全文搜尋檢查遺漏**
    ```bash
    grep -r "docs/power-platform-governance" .
    grep -r "scripts/fix_05_document" .
    ```

16. **完整建置測試**
    ```bash
    make DOMAIN=project-governance LANG=zh-TW all
    make DOMAIN=project-governance LANG=zh-TW clean
    ```

17. **提交變更**
    ```bash
    git add -A
    git commit -m "refactor: Separate Project Governance domain from Global layer

    - Move docs/power-platform-governance/ to domains/project-governance/docs/
    - Move Project Governance scripts to domains/project-governance/scripts/
    - Move Project Governance reports to domains/project-governance/docs/
    - Update Makefile to support new domain structure
    - Update README.md with new paths

    This separation ensures Global layer remains clean and reusable across all domains.

    Refs: Domain-Contamination-Assessment.md"
    ```

18. **建立 Pull Request**
    ```bash
    git push origin refactor/domain-separation
    # 在 GitHub/GitLab 建立 PR，請相關人員 Review
    ```

---

## 品質檢查清單

在執行實際移動前，請確認以下項目：

- [ ] **Makefile 已更新且測試通過**
- [ ] **Python 腳本路徑已檢查且測試通過**
- [ ] **README.md 已更新**
- [ ] **全文搜尋無遺漏的硬編碼路徑**
- [ ] **PDF/DOCX 建置流程測試通過**
- [ ] **Git 歷史保留（使用 `git mv` 而非 `mv`）**
- [ ] **所有交叉引用連結已驗證**
- [ ] **CI/CD Pipeline 已更新（如有）**

---

## 附錄 A：Domain-specific 關鍵字統計

### 統計方法

使用 `grep` 工具統計以下關鍵字出現次數：
- `PreGate0`（不區分大小寫）
- `Gate0`、`Gate1`、`Gate2`、`Gate3`（不區分大小寫）
- `projectstatus`（不區分大小寫）
- `currentgate`（不區分大小寫）
- `GOV-XXX`（使用正則表達式 `GOV-\d{3}`）

### 統計結果

| 檔案 | 關鍵字數量 |
|------|-----------|
| 01-prerequisites-and-environment.md | 10 |
| 02-dataverse-data-model-and-security.md | 112 |
| 03-sharepoint-architecture.md | 21 |
| 04-powerapps-forms.md | 74 |
| 05-core-flows-implementation-runbook.md | 228 |
| 06-guardrails-and-anti-cheating.md | 61 |
| 07-testing-and-acceptance.md | 174 |
| appendix/A-core-flows-specification.md | 154 |
| **總計** | **834** |

### 關鍵結論

**834 處 Domain-specific 關鍵字** 出現在所有 8 個核心文件中，證明這些文件 **100% 屬於 Project Governance domain**，不適合留在 Global 層級。

---

## 附錄 B：無需移動的檔案（保留在根目錄）

以下檔案已確認為 Global，**無需移動**：

| 檔案 | 檔案類型 | Global 理由 |
|------|---------|-----------|
| README.md | Markdown | Multi-domain 平台說明，不含 Domain-specific 內容 |
| Makefile | Makefile | 通用建置邏輯，支援所有 domains |
| ChangeGovernance.md | Markdown | 通用文件變更治理政策 |
| glossary.yml | YAML | 通用治理術語表，0 處 Domain-specific 關鍵字 |
| build/ | Directory | Pandoc 輸出目錄，由 Makefile 管理 |
| fonts/ | Directory | 字型檔案，供所有 domains 共用 |
| styles/ | Directory | CSS 樣式檔案，供所有 domains 共用 |
| templates/ | Directory | Pandoc 模板，供所有 domains 共用 |

---

## 附錄 C：其他 Domains 狀況

根據 README.md，此 repository 包含以下 5 個 domains：

1. **system-design** - （未在此次鑑識範圍，需後續檢查）
2. **cross-department** - （未在此次鑑識範圍，需後續檢查）
3. **iec61850-substation** - （未在此次鑑識範圍，需後續檢查）
4. **governance-sop-dataverse** - （未在此次鑑識範圍，需後續檢查）
5. **power-platform-governance** - ✅ **已完成鑑識（本報告）**

### 建議後續行動

對其他 4 個 domains 執行相同的 Domain Contamination Assessment，確保所有 Domain-specific 檔案均移至 `domains/*/` 目錄下。

---

## 簽核

| 角色 | 簽核人 | 日期 | 狀態 |
|-----|-------|------|---------|
| 鑑識執行者 | Claude Sonnet 4.5 | 2026-02-08 | ✅ 完成 |
| 架構審核者 | - | - | 待簽核 |
| 執行核准者 | - | - | 待簽核 |

---

**鑑識結論**：

1. **Global 層級乾淨度**：✅ 優良（8/8 個根目錄檔案為 Global）

2. **Domain 汙染程度**：❌ 嚴重（13 個 Domain-specific 檔案分散於 docs/ 與 scripts/）

3. **建議行動**：**立即執行檔案移動**，將 13 個 Project Governance domain 檔案移至 `domains/project-governance/` 目錄

4. **預期效益**：
   - Global 層級完全乾淨，可供所有 domains 共用
   - Domain-specific 檔案隔離，避免交叉汙染
   - 新增 domains 時，架構更清晰、更易維護

---

**報告結束**
