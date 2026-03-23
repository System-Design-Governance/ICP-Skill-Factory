# ICP Skill Management Agent — Architecture Plan v2

**Version:** v2.0 (2026-03-19)
**Owner:** Victor Liu, ICP System Design Dept
**Team:** 4–6 人，混合技術背景
**Core Engine:** Claude Code (via `claude-code-action` + `CLAUDE.md`)
**Approach:** Hybrid — GitHub Actions + Claude Code (CI/CD) + Cowork Scheduled Tasks (監控報告)

---

## 1. Problem Statement

（同 v1.0，略）

---

## 2. v1 vs v2 Architecture Comparison

### v1 的問題：自己寫所有腳本

```
v1 需要維護的自建代碼：
├── scripts/validate-skills.py       ~300 行 Python  ← 要自己寫
├── scripts/quality-gate.py          ~200 行 Python  ← 要自己寫 + 串 Claude API
├── scripts/build-plugins.py         ~150 行 Python  ← 要自己寫
├── scripts/health-monitor.py        ~200 行 Python  ← 要自己寫
├── scripts/coverage-report.py       ~200 行 Python  ← 要自己寫
└── scripts/schemas/*.schema.json    ~150 行 JSON    ← 要自己寫
                                    ─────────────────
                                    ~1200 行自建代碼需要長期維護
```

v1 的核心問題是：你要寫一堆 Python 去**模仿 Claude 本來就能做的事**。
Schema 驗證用 Python 寫可以，但品質判斷、語意衝突偵測、改善建議這些，
Claude Code 本身就是最好的引擎。

### v2 的方案：讓 Claude Code 成為引擎

```
v2 需要維護的：
├── CLAUDE.md                          ~150 行   ← 治理規則（已有 80%）
├── .github/workflows/claude.yml       ~30 行    ← 標準模板
├── .github/workflows/build-plugins.yml ~40 行   ← 打包腳本（機械性工作）
└── scripts/build-plugins.sh           ~80 行    ← 純 ZIP 打包
                                      ───────────
                                      ~300 行，且 CLAUDE.md 幾乎不需要寫新內容
```

**關鍵洞察：** 你的 `SCHEMA.md`、`CONVENTIONS.md`、ADR 文件已經用自然語言
描述了所有治理規則。Claude Code 直接讀這些文件就能做驗證，不需要你再把
這些規則翻譯成 Python 代碼。

---

## 3. v2 Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                    GitHub Repository                              │
│            System-Design-Governance/ICP-Skill-Factory             │
│                                                                   │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │  CLAUDE.md  ← 治理規則的單一事實來源 (Single Source of Truth) │  │
│  │  引用：SCHEMA.md + CONVENTIONS.md + ADR-001~007            │  │
│  └────────────────────────────────────────────────────────────┘  │
│                              │                                    │
│               Claude Code 讀取後自動遵循                          │
│                              │                                    │
│  ┌───────────────────────────┼────────────────────────────────┐  │
│  │          GitHub Actions (Event-Driven)                      │  │
│  │                           │                                 │  │
│  │   PR 事件 ───────────────▶│                                 │  │
│  │   @claude 指令 ──────────▶│                                 │  │
│  │                           ▼                                 │  │
│  │   ┌─────────────────────────────────────┐                  │  │
│  │   │   claude-code-action@v1             │                  │  │
│  │   │                                     │                  │  │
│  │   │   能力：                             │                  │  │
│  │   │   • 讀取 CLAUDE.md 治理規則          │                  │  │
│  │   │   • 解析 SK YAML + prose sections   │                  │  │
│  │   │   • 語意品質評估 + 改善建議          │                  │  │
│  │   │   • 觸發詞衝突偵測                   │                  │  │
│  │   │   • 直接在 PR comment 回覆          │                  │  │
│  │   │   • 可由 @claude 互動呼叫           │                  │  │
│  │   └─────────────────────────────────────┘                  │  │
│  │                                                             │  │
│  │   Merge 事件 ──▶ build-plugins.yml ──▶ Release             │  │
│  │                  (純機械性打包，不需要 Claude)               │  │
│  └─────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
                               │
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────┐
│               Cowork Scheduled Tasks (Periodic)                   │
│                                                                   │
│  ┌────────────────┐  ┌──────────────────┐                        │
│  │ Health Monitor  │  │ Coverage Report   │                        │
│  │ (Daily 09:00)   │  │ (Weekly Mon 09:00)│                        │
│  │                 │  │                   │                        │
│  │ 用 gh CLI 讀取  │  │ 用 gh CLI 讀取    │                        │
│  │ Repo 最新狀態   │  │ Repo + git log    │                        │
│  │ 產生健康報告    │  │ 產生覆蓋率週報     │                        │
│  └────────────────┘  └──────────────────┘                        │
└──────────────────────────────────────────────────────────────────┘
```

---

## 4. CLAUDE.md — 治理規則的核心

這是整個 Agent 系統的大腦。Claude Code 在每次 PR review 和 @claude 互動時
都會自動載入這個檔案。你已有的 `SCHEMA.md` 和 `CONVENTIONS.md` 覆蓋了 80%
的規則，CLAUDE.md 只需要把它們串起來並補充 review 流程。

```markdown
# CLAUDE.md

## Repository Overview

This is the ICP Skill Factory — a governance system for 171 engineering
skill definitions (SK) and 51 executable Cowork skills (SKILL.md) across
5 role-based plugins for OT/ICS energy infrastructure.

## Governance Documents (MUST READ before any review)

- `00-governance/SCHEMA.md` — SK definition schema (13 YAML + 14 prose fields)
- `00-governance/CONVENTIONS.md` — Naming, ID patterns, overlap resolution rules
- `00-governance/decisions/ADR-*.md` — Architecture decision records

## When reviewing PRs that modify SK definitions (03-skill-definitions/)

### Validation Checklist
1. YAML metadata block has all 11 required fields (per SCHEMA.md Part A)
2. skill_id format matches filename: SK-D{nn}-{nnn}.md
3. domain_id is valid (D01–D14); subdomain_id matches domain
4. skill_type is one of: Analysis, Design, Engineering, Testing,
   Documentation, Management, Verification, Governance, Integration, Operations
5. tier is one of: T1-Domain, T2-CapabilityGroup, T3-Skill, T4-AtomicSubskill
6. maturity is one of: Draft, Active, Deprecated, Retired
7. version follows SemVer
8. Required prose sections exist: Description, Inputs, Outputs,
   Acceptance Criteria, Source Traceability, Footer
9. Acceptance Criteria are observable and verifiable (not vague like "adequate")
10. Dependencies reference existing SK-IDs (or SC-IDs with ⏳ marker)

### Overlap Detection (per CONVENTIONS.md §4)
- D02.3 vs D05.5 vs D07.2 (protocol subdomains)
- D10.2 vs D11.2 (change management)
- D14 vs D10 (pre-gate vs post-gate)
- D03.4 vs D05.2 (VPP power vs control)
- D12.3 vs D13.2 (data analysis vs AI-assisted engineering)

## When reviewing PRs that modify SKILL.md files (05-cowork-skills/, 06-plugin-src/)

### Structure Check
1. YAML frontmatter has `name` and `description`
2. description contains MANDATORY TRIGGERS (bilingual: English + Chinese)
3. Skill directory has SKILL.md at root
4. Referenced files in scripts/, references/, templates/ actually exist
5. SKILL.md follows progressive disclosure pattern (Layer 1: description,
   Layer 2: body <500 lines, Layer 3: bundled resources)

### Quality Assessment (rate A/B/C)
- **A (Production)**: >400 lines, complete sections, has scripts/references/
  templates, acceptance criteria are verifiable, description is comprehensive
- **B (Skeleton)**: 150-400 lines, structure complete but needs deep content
- **C (Draft)**: <150 lines, missing sections, needs significant work

### Trigger Conflict Detection
Compare the new/modified skill's MANDATORY TRIGGERS against ALL other skills
in the same plugin. Flag if >30% keyword overlap with another skill.

## When someone uses @claude

Respond helpfully in Traditional Chinese (繁體中文). You can:
- Validate specific files on request
- Suggest improvements to skill content
- Help resolve merge conflicts
- Explain governance rules
- Help with skill creation following CONVENTIONS.md patterns

## Plugin Structure (06-plugin-src/)
- icp-seceng: OT Cybersecurity (10 skills)
- icp-sysarch: System Architecture (16 skills)
- icp-integration: Integration & Verification (13 skills)
- icp-governance: Engineering Governance (7 skills)
- icp-presales: Pre-Gate Support (5 skills)

## Build Process
After merge to main, .plugin files are built by zipping each plugin directory
in 06-plugin-src/ with its .claude-plugin/plugin.json manifest.
```

---

## 5. GitHub Actions Workflows

### 5.1 Claude Code PR Review (取代 v1 的 validate + quality-gate)

**一個 workflow 取代 v1 的兩個 workflow + 兩個 Python 腳本。**

```yaml
# .github/workflows/claude.yml
name: Claude Code Skill Review

on:
  pull_request:
    types: [opened, synchronize]
    paths:
      - '03-skill-definitions/**'
      - '05-cowork-skills/**'
      - '06-plugin-src/**/skills/**'
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]

jobs:
  review:
    # 自動 review 每個 PR；也響應 @claude 互動
    if: |
      github.event_name == 'pull_request' ||
      (github.event_name == 'issue_comment' && contains(github.event.comment.body, '@claude')) ||
      (github.event_name == 'pull_request_review_comment' && contains(github.event.comment.body, '@claude'))
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          prompt: |
            Review this PR against ICP Skill Factory governance rules.

            Steps:
            1. Read CLAUDE.md for full governance context
            2. Identify which files were changed (SK definitions, SKILL.md, or plugin files)
            3. Run the appropriate validation checklist from CLAUDE.md
            4. For SKILL.md changes: provide a quality rating (A/B/C) with justification
            5. Check for trigger keyword conflicts with existing skills
            6. Post a structured review comment with:
               - ✅ Passed checks
               - ❌ Failed checks (blocking)
               - ⚠️ Warnings (non-blocking)
               - 💡 Improvement suggestions

            Respond in Traditional Chinese (繁體中文).
          claude_args: "--model claude-sonnet-4-6 --max-turns 10"
```

**與 v1 對比：**

| 面向 | v1（自建 Python） | v2（Claude Code） |
|------|-------------------|-------------------|
| Schema 驗證 | validate-skills.py 逐欄位檢查 | Claude 直接讀 SCHEMA.md 理解規則 |
| 品質評估 | quality-gate.py 串 Claude API | Claude Code 原生能力 |
| 觸發詞衝突 | 需自己寫 tokenizer + 相似度比對 | Claude 語意理解，直接偵測 |
| 改善建議 | 要自己寫 prompt template | Claude 讀完治理文件後自然產出 |
| 互動能力 | 無（只能看 CI 結果） | @claude 即時問答 |
| 維護成本 | ~500 行 Python + JSON Schema | ~150 行 CLAUDE.md |
| 新增規則 | 修改 Python 代碼 + Schema | 修改 CLAUDE.md 自然語言 |

### 5.2 @claude 互動場景

PR 中 @claude 的典型用法（團隊成員直接在 PR comment 裡打字）：

```
@claude 這個 SKILL.md 的 MANDATORY TRIGGERS 夠完整嗎？
@claude 幫我檢查 SK-D01-015 的 Acceptance Criteria 是否可驗證
@claude 這個 skill 跟 compliance-gap-assessor 會不會衝突？
@claude 幫我把這個 Tier B skill 升級到 Tier A，給我改善建議
@claude 這個 PR 有哪些地方不符合 CONVENTIONS.md？
```

Claude Code 會讀取 CLAUDE.md 和相關治理文件後回答，而且回答會**帶著完整的
repo context**（它能看到所有其他 skills 來做衝突比對）。

### 5.3 Plugin Builder（保持不變）

打包是純機械性工作，不需要 Claude：

```yaml
# .github/workflows/build-plugins.yml
name: Build & Release Plugins
on:
  push:
    branches: [main]
    paths:
      - '05-cowork-skills/**'
      - '06-plugin-src/**'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build .plugin packages
        run: |
          mkdir -p dist
          for plugin_dir in 06-plugin-src/icp-*; do
            plugin_name=$(basename "$plugin_dir")
            # Read version from plugin.json
            version=$(jq -r '.version' "$plugin_dir/.claude-plugin/plugin.json")
            # Create ZIP with .plugin extension
            cd "$plugin_dir" && zip -r "../../dist/${plugin_name}.plugin" . && cd ../..
          done

      - name: Bump patch version
        run: |
          for plugin_dir in 06-plugin-src/icp-*; do
            jq '.version |= (split(".") | .[2] = (.[2]|tonumber+1|tostring) | join("."))' \
              "$plugin_dir/.claude-plugin/plugin.json" > tmp.json
            mv tmp.json "$plugin_dir/.claude-plugin/plugin.json"
          done

      - name: Create GitHub Release
        uses: softprops/action-gh-release@v2
        with:
          files: dist/*.plugin
          tag_name: v${{ github.run_number }}
          generate_release_notes: true
```

---

## 6. Cowork Scheduled Tasks

### 6.1 Health Monitor (Daily)

```
Task ID:     skill-health-monitor
Schedule:    0 9 * * 1-5  (Weekdays 09:00)
```

**Prompt:**

```
你是 ICP Skill Factory 的健康監控 Agent。請執行以下檢查：

1. 使用 gh CLI clone ICP-Skill-Factory repo 的最新版本
2. 掃描 03-skill-definitions/registry/ 下所有 SK-D*.md，統計總數
3. 掃描 05-cowork-skills/ 下所有 SKILL.md，統計總數
4. 比對：哪些 SK 定義沒有對應的 SKILL.md？
5. 檢查 06-plugin-src/ 下每個 plugin 的 skills/ 是否與 05-cowork-skills/ 一致
6. 用 git log --since="30 days ago" 找出超過 30 天未更新的 SKILL.md
7. 掃描所有 SKILL.md 中引用的 scripts/、references/、templates/ 路徑是否存在

產出一份繁體中文的每日健康報告（markdown 格式），包含：
- 摘要（SK 總數、SKILL.md 總數、Tier A/B 比例）
- 缺失清單（有 SK 但無 SKILL.md 的項目）
- 過期清單（>30 天未更新的 Tier B skills）
- Broken References（引用不存在的檔案）
- 建議的優先行動項目
```

### 6.2 Coverage Report (Weekly)

```
Task ID:     skill-coverage-report
Schedule:    0 9 * * 1  (Monday 09:00)
```

**Prompt:**

```
你是 ICP Skill Factory 的覆蓋率報告 Agent。請產出本週覆蓋率報告：

1. Clone repo，讀取 01-domain-map/ 取得 14 個 Domain 的定義
2. 對每個 Domain (D01-D14)，統計：
   - SK 定義數量
   - SKILL.md 數量
   - Tier A 數量（>400 行、有 scripts/references/templates）
   - 覆蓋率 = SKILL.md / SK 定義
3. 用 git log --since="7 days ago" 統計本週變更：
   - 新增的 skills
   - 修改的 skills
   - 每位 contributor 的提交數
4. 檢查本週 merged PRs 的 Claude review 結果

產出繁體中文週報（markdown 格式），包含：
- Domain Coverage Matrix（表格）
- 本週亮點（新增 / 升級的 skills）
- Team Contribution 排行
- 下週建議優先項目（覆蓋率最低的 Domain）

同時產出 Excel 版本的 Domain Coverage Matrix。
```

---

## 7. Developer Workflow (v2)

### 7.1 Git-Proficient Developer

```
1. git checkout -b feat/seceng-new-skill-name
2. 建立/修改 skill 檔案
3. git push → 建立 PR
4. Claude Code 自動 review：
   - Schema 驗證 ✓/✗
   - 品質評分 A/B/C
   - 觸發詞衝突檢查
   - 改善建議
5. 如有問題 → 在 PR 中 @claude 討論
6. 修正後 → 團隊 Review → Approve
7. Merge → 自動打包 → GitHub Release
```

### 7.2 Cowork-Primary Developer

```
1. 在 Cowork 中使用 skill-creator 建立/修改 skill
2. 告訴 Cowork：「幫我把這個 skill 提交到 Repo」
   → Cowork Agent 自動建立 branch + push + 建立 PR
3. Claude Code 在 PR 上自動 review
4. 收到 review 結果 → 在 PR 中 @claude 詢問改善方式
5. 修正 → 團隊 Approve → Merge → Release
```

### 7.3 核心差異：@claude 互動

v1 的流程是單向的：CI 跑完你只能看結果。
v2 的流程是互動的：你可以直接跟 Claude 討論，問它為什麼給 B 級，
怎麼改才能到 A 級，甚至請它幫你改。

```
Developer: @claude 為什麼 security-testing 這個 SKILL.md 只得到 B？

Claude:    security-testing 目前是 B 級，主要有三個原因：
           1. 缺少 scripts/ 目錄（Tier A 需要可執行的輔助腳本）
           2. references/ 只有 2 個檔案（建議至少包含 OWASP + IEC 62443-4-2）
           3. Acceptance Criteria 第 3 項「測試結果符合要求」太模糊
              建議改為「所有 High/Critical 弱點在報告中包含 CVSS v3.1 評分和
              修復建議，且修復優先級與 SL-T 等級一致」

Developer: @claude 幫我加上建議的 Acceptance Criteria 修改

Claude:    [直接提交修改到 PR branch]
```

---

## 8. Repository Structure (v2)

```
icp-skill-factory/
├── CLAUDE.md                          # ★ 治理規則核心 (新增)
├── .github/
│   ├── workflows/
│   │   ├── claude.yml                 # Claude Code PR Review + @claude 互動
│   │   └── build-plugins.yml          # 自動打包 + Release
│   └── PULL_REQUEST_TEMPLATE.md       # PR 模板 (新增)
├── 00-governance/
│   ├── SCHEMA.md                      # (既有) SK Schema v1.2
│   ├── CONVENTIONS.md                 # (既有) 命名與 ID 規範
│   ├── skill-governance-workplan.md   # (既有) 治理工作計畫
│   └── decisions/
│       └── ADR-008-claude-code-agent.md  # (新增) 本文件的 ADR 版本
├── 04-review/
│   ├── daily-health/                  # Health Monitor 輸出 (新增)
│   └── weekly-reports/                # Coverage Report 輸出 (新增)
└── ... (all existing directories unchanged)
```

**新增/修改的檔案只有 4 個：**
1. `CLAUDE.md` (~150 行)
2. `.github/workflows/claude.yml` (~30 行)
3. `.github/workflows/build-plugins.yml` (~40 行)
4. `.github/PULL_REQUEST_TEMPLATE.md` (~20 行)

---

## 9. Implementation Roadmap (v2)

### Phase 1：Claude Code 上線（Week 1）— 3 天可完成

| # | Task | Effort |
|---|------|--------|
| 1.1 | 撰寫 CLAUDE.md（整合 SCHEMA.md + CONVENTIONS.md 規則） | 2 hr |
| 1.2 | 安裝 Claude GitHub App (`/install-github-app`) | 15 min |
| 1.3 | 設定 ANTHROPIC_API_KEY secret | 5 min |
| 1.4 | 建立 `.github/workflows/claude.yml` | 30 min |
| 1.5 | 設定 main branch protection (require PR + 1 approval) | 15 min |
| 1.6 | 用現有 PR 測試 Claude Code review | 1 hr |

**Milestone：** 所有 PR 自動獲得 Claude Code review + @claude 互動可用

### Phase 2：自動打包 + Release（Week 2）

| # | Task | Effort |
|---|------|--------|
| 2.1 | 撰寫 `build-plugins.yml` workflow | 2 hr |
| 2.2 | 建立 PR template | 30 min |
| 2.3 | 撰寫 ADR-008 (Claude Code Agent Architecture) | 1 hr |
| 2.4 | 端到端測試：PR → Review → Merge → Release | 2 hr |

**Milestone：** 完整 CI/CD pipeline 上線

### Phase 3：Scheduled Monitoring（Week 3）

| # | Task | Effort |
|---|------|--------|
| 3.1 | 建立 Cowork Scheduled Task — Health Monitor | 1 hr |
| 3.2 | 建立 Cowork Scheduled Task — Coverage Report | 1 hr |
| 3.3 | 驗證報告品質並調整 prompt | 2 hr |

**Milestone：** 自動化監控與報告機制運作

### Phase 4：Team Onboarding（Week 4）

| # | Task | Effort |
|---|------|--------|
| 4.1 | 撰寫 Contributor Guide（如何在 PR 中使用 @claude） | 1 hr |
| 4.2 | 團隊工作坊（Demo @claude review + 互動流程） | 2 hr |
| 4.3 | 開發 submit-skill-to-repo Cowork Skill（for 非 Git 用戶）| 3 hr |
| 4.4 | 收集回饋並迭代 CLAUDE.md 規則 | 持續 |

**Milestone：** 全團隊上線使用

### 總時程對比

| | v1 (自建 Python) | v2 (Claude Code) |
|--|-------------------|-------------------|
| 總時程 | 8 週 | 4 週 |
| 自建代碼量 | ~1200 行 | ~300 行 |
| 維護複雜度 | 高（Python + Schema + API 串接） | 低（主要維護 CLAUDE.md 自然語言） |
| 新增治理規則 | 修改 Python 代碼 | 修改 CLAUDE.md 文字 |
| 互動能力 | 無 | @claude 即時互動 |

---

## 10. Cost Analysis

### GitHub Actions 費用

- Claude Code action 使用 GitHub-hosted runner（ubuntu-latest）
- 每次 PR review 約 2-5 分鐘 runner 時間
- GitHub Free plan: 2000 分鐘/月
- 預估使用：20 PRs/月 × 5 min = 100 分鐘 ← 遠低於免費額度

### Claude API 費用

- 每次 PR review: Claude Sonnet ~5K input + 2K output tokens
- 每次 @claude 互動: ~3K input + 1K output tokens
- 月預估: 20 PRs + 40 互動 = ~$5-10/月

### Cowork Scheduled Tasks

- Health Monitor: 每日 1 次 × 22 工作日 = 22 sessions/月
- Coverage Report: 每週 1 次 = 4 sessions/月
- 總計 ~26 sessions/月

---

## 11. Security Considerations

- `ANTHROPIC_API_KEY` 存放在 GitHub repository secrets，不暴露在 logs 中
- Claude Code action 只在 GitHub-hosted runner 上執行，不接觸本地環境
- Claude Code 對 repo 的存取權限透過 GitHub App 管理（Contents + Issues + PRs）
- `CLAUDE.md` 中不包含任何敏感資訊（純治理規則）
- Branch protection 確保所有變更必須經過 PR review

---

## 12. Future Extensions

### Phase 5+（當需求出現時再啟動）

- **Auto-Fix PRs**：Claude Code 不只 review，還能自動修復並 push 到 PR branch
- **Eval-as-a-Service**：整合 skill-creator eval 到 CI，每個 SKILL.md 變更自動跑 eval
- **Tier Auto-Upgrade**：Claude Code 偵測 Tier B skills 並自動產生升級 PR
- **Cross-Plugin Dedup**：跨 5 個 plugins 的觸發詞去重（定期排程）
- **Issue → Skill**：在 GitHub Issue 中描述需求 → @claude 自動產生 skill 初稿 PR

---

## Appendix A：CLAUDE.md 完整初稿

（見上方 Section 4）

## Appendix B：PR Template

```markdown
## 變更類型
- [ ] 新增 SK 定義 (03-skill-definitions/)
- [ ] 新增/修改 SKILL.md (05-cowork-skills/)
- [ ] 修改 Plugin 結構 (06-plugin-src/)
- [ ] 治理文件更新 (00-governance/)

## 變更摘要
<!-- 簡述這個 PR 做了什麼 -->

## 對應的 Skill ID
<!-- 例如 SK-D01-015 或 threat-risk-assessment -->

## Plugin 歸屬
<!-- icp-seceng / icp-sysarch / icp-integration / icp-governance / icp-presales -->

## 自檢清單
- [ ] SK YAML metadata 完整（13 個欄位）
- [ ] SKILL.md frontmatter 包含 name + description
- [ ] Description 包含 MANDATORY TRIGGERS（中英文）
- [ ] 引用的 scripts/references/templates 檔案存在
- [ ] 已確認不與現有 skills 的觸發詞衝突
```
