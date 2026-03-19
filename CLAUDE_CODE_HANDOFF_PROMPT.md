# ICP Skill Factory — Phase 5 修正與深化執行 Prompt

> **Git Repo**: https://github.com/System-Design-Governance/ICP-Skill-Factory.git
> **前置文件**: `04-review/full-forensic-review.md` (鑑識報告) + `04-review/remediation-plan.md` (修正計畫)
> **模式**: 先讀取上述兩份文件，然後按本 Prompt 的修訂版任務表執行

---

## 背景

鑑識報告已完成（13 個缺口：5 Critical、5 Major、3 Minor）。本 Prompt 是基於鑑識報告的**修訂版執行計畫**，補充了原始 remediation-plan.md 遺漏的 5 個問題：

**重大發現：原始 7-Phase 計畫與實際執行嚴重偏離。**

原始計畫的 7 Phase 為：①領域發現 → ②架構設計 → ③技能定義 → ④依賴對應 → ⑤衝突分析 → ⑥分類重構 → ⑦演進規劃。實際執行完成了 Phase 1-3，但 **Phase 4-7 全部未執行**（僅有 TODO.md），取而代之的是直接進入 Cowork SKILL.md 轉換和 Plugin 打包（不在原始計畫中）。這導致：
- `04-dependency-map/` 和 `04-review/` 編號衝突
- `05-conflict-analysis/` 和 `05-cowork-skills/` 編號衝突
- `06-refactoring/` 和 `07-evolution/` 空殼佔位
- 依賴圖、衝突矩陣、重構提案、演進路線圖均未產出

此偏差是 Victor 有意識的決策（優先讓 Skills 可用於生產），不是失誤。但目錄結構需要清理以反映真實狀態。

## ⚠️ 核心原則（貫穿所有任務）

### 原則 1：以 Plugin 為單位思考，不是以獨立 Skill 為單位

每個 Skill 都是 Plugin 的一部分。開發時必須考慮：

- **共用資源先行**：深化某 Plugin 前，先建立 Plugin 層級的 `references/` 和 `templates/`，再讓各 Skill 引用
- **跨 Skill 引用**：同 Plugin 內的 Skills 用相對路徑引用共用資源（如 `../../references/iec-62443-sr-checklist.md`）
- **Plugin README.md**：每個 Plugin 根目錄需有 README.md，說明角色職責、Skill 清單、協作關係
- **TRIGGERS 不衝突**：同 Plugin 內 Skills 的 MANDATORY TRIGGERS 不應過度重疊

### 原則 2：SK 定義是「知識規格書」，不是「操作手冊」

鑑識報告確認 0/171 SK 有 Workflow 和 Pitfalls 章節。深化時：
- **Workflow**：從 SK 的 Description + Outputs + Acceptance Criteria 推導，結合 Tier A 範例風格自行建構
- **Pitfalls**：從領域知識 + source-documents (ID01~ID14) + IEC 62443 標準推導，不是從 SK 提取
- **可執行性**：產出的 SKILL.md 必須是操作手冊級，讓 Claude 讀了就能執行

### 原則 3：Tier A 是品質標竿

深化前必須先讀取至少 2 個 Tier A SKILL.md 理解目標品質：
- `05-cowork-skills/arch-diagram/SKILL.md` (619L, 25 code blocks)
- `05-cowork-skills/cbom-builder/SKILL.md` (607L, 16 code blocks)
- `05-cowork-skills/presales/SKILL.md` (518L, 有 templates/ + references/)
- `05-cowork-skills/compliance-gap-assessor/SKILL.md` (261L, 12 code blocks)

---

## 修訂版任務表

原始 remediation-plan.md 的 R-001~R-013 加上 4 個補充任務（R-014~R-017）。

### Phase 0 (P0): 目錄重整 + 治理修正 + Git 初始化

#### R-018 [新增] — 目錄結構重整（最優先）

**問題**：原始 7-Phase 計畫使用 `01-07` 編號目錄，但 Phase 4-7 未執行（僅有 TODO.md），實際工作建立了 `04-review/` 和 `05-cowork-skills/` 與原始目錄**編號衝突**。

**原始結構 → 實際狀態**：
```
01-domain-map/           ✅ Phase 1 完成（保留）
02-skill-candidates/     ✅ Phase 2 完成（保留）
03-skill-definitions/    ✅ Phase 3 完成（保留）
04-dependency-map/       ❌ Phase 4 未執行（僅 TODO.md）
04-review/               ✅ 實際 Phase 3-5 Review（與上方衝突）
05-conflict-analysis/    ❌ Phase 5 未執行（僅 TODO.md）
05-cowork-skills/        ✅ 實際 Phase 5 Cowork（與上方衝突）
06-refactoring/          ❌ Phase 6 未執行（僅 TODO.md）
07-evolution/            ❌ Phase 7 未執行（僅 TODO.md）
```

**修正方案**：將原始未執行的 Phase 4-7 TODO 目錄歸檔為 `_archive/`，消除編號衝突，同時建立 Plugin 原始碼目錄 `06-plugin-src/`。

```bash
# 1. 歸檔未執行的 Phase 目錄
mkdir -p _archive/original-plan
mv 04-dependency-map _archive/original-plan/
mv 05-conflict-analysis _archive/original-plan/
mv 06-refactoring _archive/original-plan/
mv 07-evolution _archive/original-plan/

# 2. 建立 Plugin 開發目錄（從 05-cowork-skills/plugins/ 的建構來源搬入）
mkdir -p 06-plugin-src

# 3. 重整後的乾淨結構：
# 00-governance/           ← 治理文件
# 01-domain-map/           ← Phase 1 (完成)
# 02-skill-candidates/     ← Phase 2 (完成)
# 03-skill-definitions/    ← Phase 3 (完成，凍結)
# 04-review/               ← Phase 3-5 Review 報告
# 05-cowork-skills/        ← 51 個 SKILL.md 開發工作區
# 06-plugin-src/           ← 5 個 Plugin 原始碼（打包來源）
# source-documents/        ← 治理+範例+程序文件
# _archive/original-plan/  ← 未執行的 Phase 4-7 TODO（保留可追溯）
```

**注意**：`_archive/original-plan/` 中的 TODO.md 保留了原始 Phase 4-7 的規劃意圖，未來如需執行依賴對應、衝突分析、分類重構或演進規劃，可從此處恢復。

| ID | 任務 | 對應缺口 | 說明 |
|----|------|---------|------|
| **R-018** | 目錄結構重整 | G-014 (新) | 歸檔 Phase 4-7 空目錄，消除編號衝突，建立 06-plugin-src |
| **R-001** | 更新 SCHEMA.md | G-003 | 明確區分 YAML fields (~13) vs prose sections (~14)，新增 ADR 記錄此設計決策 |
| **R-002** | git init + push to GitHub | G-013 | `git remote add origin https://github.com/System-Design-Governance/ICP-Skill-Factory.git && git add -A && git commit && git push -u origin main`（repo 已有 .git） |
| **R-010** | forensic report supersession note | G-008 | 在 `04-review/forensic-review-report.md` 頂部加入指向 phase4-review-report.md 的 supersession note |
| **R-011** | SCHEMA.md 標註 composition_patterns Optional | G-007 | 將此欄位標為 `Optional / Deferred (原始 Phase 4 未執行)` |
| **R-013** | README.md 更新 | G-002 | 建立 repo 根目錄 README.md，含專案概述、目錄說明、Phase 狀態、偏差記錄 |

### Phase 1 (P1): 核心 Plugin 深化

**重要：每個 Plugin 深化的第一步是建立 Plugin 級共用資源，然後才逐一深化 Skills。**

#### R-014 [新增] — Plugin 級共用資源建立

在深化 Skills 之前，先為每個 Plugin 建立共用 references/ 和 templates/：

| Plugin | 共用 references/ | 共用 templates/ |
|--------|-----------------|-----------------|
| icp-seceng | `iec-62443-sr-checklist.md` (FR/SR 完整對照表), `stride-dread-scoring-guide.md` | `risk-register.md`, `tra-report.md`, `asset-inventory.md`, `hardening-checklist.md` |
| icp-sysarch | `purdue-model-mapping.md`, `zone-color-spec.md` (從 arch-diagram 提取) | `architecture-doc.md`, `vlan-plan.md`, `icd-template.md` |
| icp-integration | `protocol-comparison.md`, `test-severity-classification.md` | `fat-plan.md`, `sat-plan.md`, `interface-matrix.md`, `commissioning-plan.md` |
| icp-governance | `gate-0-3-checklists.md`, `gov-sd-appendix-c.md` | `design-review-checklist.md`, `rtm.md`, `sop-template.md` |
| icp-presales | (已有 review_checklist.md) | (已有 feasibility/architecture/doc_inventory) — 補充 `gate0-package.md` |

每個共用資源檔案應從以下來源建立：
1. source-documents/ 中的 Tier 1-3 文件
2. SK 定義中的 Standards + Acceptance Criteria 段落
3. Tier A SKILL.md 中已有的範例（如 arch-diagram 的 Zone 顏色表）

#### R-004 — 深化 icp-seceng (9 個 Tier B)

依序：security-system-hardening(6 SKs) → security-monitoring-incident-response(6) → security-perimeter-design(2) → security-level-assessment(1) → security-policies-governance(3) → supply-chain-security(4) → sis-security-control(1) → security-testing(5) → 重新打包 plugin

#### R-005 — 深化 icp-presales (2 個 Tier B)

site-assessment(3 SKs) → concept-development(3) → gate0-decision-package(2) → 重新打包 plugin

### Phase 2 (P2): 全面深化

#### R-006 — 深化 icp-sysarch (15 個 Tier B)

優先：network-architecture-design → scada-foundation → control-strategy-configuration → 其餘 12 個 → 重新打包

#### R-007 — 深化 icp-integration (13 個 Tier B)

優先：factory-acceptance-testing → site-acceptance-testing → design-documentation → 其餘 10 個 → 重新打包

#### R-008 — 深化 icp-governance (7 個 Tier B)

優先：design-review-governance → process-development → 其餘 5 個 → 重新打包

#### R-015 [新增] — MANDATORY TRIGGERS 衝突檢查

每個 Plugin 深化完成後，執行 TRIGGERS 衝突檢查：
```bash
# 檢查同 Plugin 內 Skills 的 trigger 重疊度
for plugin_dir in icp-seceng icp-sysarch icp-integration icp-governance icp-presales; do
  echo "=== $plugin_dir ==="
  for f in $plugin_dir/skills/*/SKILL.md; do
    grep "MANDATORY TRIGGERS:" "$f" | sed 's/.*MANDATORY TRIGGERS://' | tr ',' '\n' | sed 's/^ *//'
  done | sort | uniq -c | sort -rn | head -20
done
```
重疊度 >3 的 trigger 需要調整，確保 Claude 能精確區分該觸發哪個 Skill。

### Phase 3 (P3): 收尾

| ID | 任務 |
|----|------|
| **R-012** | 確認 5 個 standalone skills (ciso-advisor, senior-security, sales-engineer, dept-timesheet-analyzer, protocol-integrator) 的位置和處理方式。這些目前僅在使用者的 Cowork `.skills/` 中，不在 repo 內。與使用者確認是否需要納入 Plugin 或保持獨立。 |
| **R-016** [新增] | 將 5 個 standalone skills 從 Cowork `.skills/` 匯出到 repo，建立第 6 個 Plugin `icp-tools`（工具類 Skills：ciso-advisor, senior-security, sales-engineer, dept-timesheet-analyzer, protocol-integrator）或整合到現有 Plugin |
| **R-017** [新增] | 全域 Review：所有 5 Plugin 重新打包後，執行 51 SKILL.md 的結構驗證 + TRIGGERS 衝突檢查 + Plugin 內部一致性審查，產出 `04-review/phase5-final-review.md` |

---

## 深化 SOP（每個 Skill）

```
0. 確認 Plugin 級共用資源已建立（R-014）
1. 讀取 05-cowork-skills/{skill-name}/SKILL.md（現有骨架）
2. 讀取 SKILL.md 末尾 Source Traceability 表，找對應 SK 編號
3. 逐一讀取 03-skill-definitions/registry/SK-D{nn}-{nnn}.md
4. 從 SK 定義推導（注意：SK 沒有 Workflow 和 Pitfalls 章節）：
   a. Description + Outputs + Acceptance Criteria → 建構具體步驟操作指引
   b. Outputs → markdown 交付物模板（code blocks），適合的放入 templates/
   c. Acceptance Criteria → 強化品質檢查清單（≥5 可量化項）
   d. 領域知識 + source-documents → ⚠️ Pitfalls/Anti-patterns 段落
   e. Tools section → 工具使用指引（含 code blocks）
   f. Standards → 引用 Plugin 共用 references/ 中的對照表
5. 參考 Tier A 風格（必須有 code blocks、表格、具體範例）
6. 寫入增強版 SKILL.md（目標 300-500 行）
7. 如需要建立 Skill 專屬的 templates/ 和 references/ 子目錄
8. 確認引用 Plugin 共用資源的相對路徑正確
```

---

## 每個 SKILL.md 的驗收標準 (DoD)

| # | 驗收項 | 通過條件 |
|---|--------|---------|
| 1 | 行數 | 250-500 行（精煉，不求最長） |
| 2 | Code blocks | ≥1 個程式碼或模板區塊 |
| 3 | Workflow | 具體操作步驟（可執行手冊，非 SK Description 複製貼上） |
| 4 | Quality Checklist | ≥5 個可量化驗收項 |
| 5 | Pitfalls | 含 ⚠️ 避坑指引段落（從領域知識建構） |
| 6 | Human Review Gate | 有角色專屬審核提示（對應 Plugin 角色） |
| 7 | Source Traceability | 正確對應 SK 編號 |
| 8 | YAML Triggers | description 含中英文 MANDATORY TRIGGERS，與同 Plugin 內其他 Skills 不衝突 |
| 9 | 共用資源引用 | 適當引用 Plugin 級 references/templates/ |
| 10 | 結構完整 | §0 初始化 → §1 輸入 → §2 工作流程 → §3 輸出 → §4 標準 → §5 驗收 → §6 工時 → §7 Pitfalls → §8 品質檢查 → §9 審核閘門 → §10 生命週期 → §11 Source Traceability |

---

## Plugin 打包指令

```bash
# 每完成一個 Plugin 的全部 Skills 深化後：
cd plugin-build/{plugin-name}
# 確認結構：
# {plugin-name}/
# ├── .claude-plugin/plugin.json
# ├── README.md                    ← Plugin 級說明
# ├── references/                  ← Plugin 級共用參考
# ├── templates/                   ← Plugin 級共用模板
# └── skills/
#     ├── {skill-1}/
#     │   ├── SKILL.md
#     │   ├── templates/           ← Skill 專屬模板（如有）
#     │   └── references/          ← Skill 專屬參考（如有）
#     └── ...

zip -r /tmp/{plugin-name}.plugin . -x "*.DS_Store"
```

---

## Plugin 級共用資源 vs Skill 專屬資源判斷規則

- **≥2 個 Skills 共用** → 放 Plugin 根目錄 `references/` 或 `templates/`
- **僅 1 個 Skill 使用** → 放該 Skill 子目錄 `{skill-name}/references/` 或 `{skill-name}/templates/`
- **跨 Plugin 共用**（如 IEC 62443 SR checklist 被 seceng 和 sysarch 都用）→ 各 Plugin 各放一份，不做跨 Plugin 引用

---

## Tier A 品質標竿速查

| Skill | 行數 | Code Blocks | 關鍵特色 |
|-------|------|-------------|---------|
| arch-diagram | 619 | 25 | D2/Mermaid 完整範例、Zone 顏色 hex、正確/錯誤範例對比 |
| cbom-builder | 607 | 16 | openpyxl Python 程式碼、Excel 欄位對應表、16 項品項檢查清單 |
| presales | 518 | 20 | 4-Phase 工作流、T01-T10 任務樹、CP1-CP7 Checkpoint |
| compliance-gap-assessor | 261 | 12 | 5-Phase 差距評估、Annex C 稽核矩陣模板、Gate Review 合規包 |
| threat-risk-assessment | 528 | 12 | Claude Code 已深化為 Tier A+ |

---

## 執行順序總覽

```
P0 (Day 1-2)
├── R-018: 目錄結構重整（歸檔 Phase 4-7 空目錄 + 建立 06-plugin-src）  ← 最優先
├── R-001: SCHEMA.md 更新
├── R-002: git commit + push（目錄重整後 commit）
├── R-010: forensic report supersession
├── R-011: composition_patterns Optional
└── R-013: README.md（含專案偏差記錄）

P1 (Day 3-20)
├── R-014: 5 Plugin 共用資源建立     ← 新增，最優先
├── R-004: icp-seceng 深化 (9 skills)
├── R-005: icp-presales 補齊 (3 skills)
└── R-015: TRIGGERS 衝突檢查          ← 新增

P2 (Day 21-50)
├── R-006: icp-sysarch 深化 (15 skills)
├── R-007: icp-integration 深化 (13 skills)
├── R-008: icp-governance 深化 (7 skills)
└── R-015: 每 Plugin 完成後 TRIGGERS 檢查

P3 (Day 51-55)
├── R-012: standalone skills 確認
├── R-016: standalone skills 歸檔/Plugin 化    ← 新增
└── R-017: 全域 Final Review                    ← 新增
```

---

**開始前請先：**
1. 讀取 `04-review/full-forensic-review.md` 和 `04-review/remediation-plan.md` 了解鑑識結果
2. 讀取 2 個 Tier A SKILL.md（建議 `arch-diagram` + `presales`）了解目標品質
3. 讀取 1 個 Tier B SKILL.md（建議 `security-system-hardening`）了解現有骨架
4. 從 R-001 開始依序執行
