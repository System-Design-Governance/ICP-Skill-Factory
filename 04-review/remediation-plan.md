# ICP Skill Factory — 修正與開發計畫

**Date:** 2026-03-18
**Based on:** full-forensic-review.md (同日)
**Author:** Claude Opus 4.6

---

## 修正任務表

| ID | 優先級 | 任務 | 對應缺口 | 影響檔案數 | 估計工時 | 依賴 |
|----|--------|------|---------|-----------|---------|------|
| R-001 | P0 | 更新 SCHEMA.md：明確區分 YAML fields (~13) vs prose sections (~12) | G-003 | 1 | 0.5 pd | — |
| R-002 | P0 | git init + 初始 commit | G-013 | 全 repo | 0.5 pd | — |
| R-003 | P0 | 使用者手動刪除 Cowork manifest 中 9 個重複 standalone Skills | G-012 | manifest.json | 0.5 pd | 使用者操作 |
| R-004 | P1 | 深化 icp-seceng 9 個 Tier B Skills (threat-risk-assessment 已完成) | G-009, G-010 | 9 SKILL.md + plugin | 8-12 pd | R-001 |
| R-005 | P1 | 深化 icp-presales 2 個 Tier B Skills (site-assessment, concept-development) | G-009, G-010 | 2 SKILL.md + plugin | 2-3 pd | R-001 |
| R-006 | P2 | 深化 icp-sysarch 15 個 Tier B Skills | G-009, G-010 | 15 SKILL.md + plugin | 12-18 pd | R-004 |
| R-007 | P2 | 深化 icp-integration 13 個 Tier B Skills | G-009, G-010 | 13 SKILL.md + plugin | 10-15 pd | R-004 |
| R-008 | P2 | 深化 icp-governance 7 個 Tier B Skills | G-009, G-010 | 7 SKILL.md + plugin | 5-8 pd | R-004 |
| R-009 | P2 | 深化 icp-presales 剩餘 1 個 (gate0-decision-package) | G-009 | 1 SKILL.md | 1-2 pd | R-005 |
| R-010 | P3 | Phase 3 forensic report 加 supersession note | G-008 | 1 | 0.1 pd | — |
| R-011 | P3 | SCHEMA.md 標註 composition_patterns 為 Optional/Deferred | G-007 | 1 | 0.1 pd | — |
| R-012 | P3 | 確認 5 個 standalone skills 位置並歸檔 | G-011 | 5 | 0.5 pd | 使用者確認 |
| R-013 | P3 | README.md 標註 project-governance/ 定位 | G-002 | 1 | 0.1 pd | — |

**總估計工時：41-61 person-days** (其中 P0: 1.5 pd, P1: 10-15 pd, P2: 28-43 pd, P3: 0.8 pd)

---

## 執行順序

```
Phase 0 (P0): 治理修正                   ← Day 1-2
├── R-001: 更新 SCHEMA.md
├── R-002: git init
└── R-003: 清除重複 Skills (使用者操作)

Phase 1 (P1): 核心 Plugin 深化            ← Day 3-17
├── R-004: icp-seceng 深化 (9 skills)
│   ├── security-system-hardening (6 SKs) ← 優先
│   ├── security-monitoring-incident-response (6 SKs)
│   ├── security-perimeter-design (2 SKs)
│   ├── security-level-assessment (1 SK)
│   ├── security-policies-governance (3 SKs)
│   ├── supply-chain-security (4 SKs)
│   ├── sis-security-control (1 SK)
│   ├── security-testing (5 SKs)
│   └── → 重新打包 icp-seceng.plugin
│
└── R-005: icp-presales 補齊 (2 skills)
    ├── site-assessment (3 SKs)
    ├── concept-development (3 SKs)
    └── → 重新打包 icp-presales.plugin

Phase 2 (P2): 全面深化                    ← Day 18-60
├── R-006: icp-sysarch (15 skills)
│   ├── network-architecture-design (3 SKs) ← 優先
│   ├── scada-foundation (2 SKs)
│   ├── control-strategy-configuration (5 SKs)
│   ├── ...（其餘 12 skills）
│   └── → 重新打包 icp-sysarch.plugin
│
├── R-007: icp-integration (13 skills)
│   ├── factory-acceptance-testing (2 SKs) ← 優先
│   ├── site-acceptance-testing (4 SKs)
│   ├── design-documentation (4 SKs)
│   ├── ...（其餘 10 skills）
│   └── → 重新打包 icp-integration.plugin
│
├── R-008: icp-governance (7 skills)
│   ├── design-review-governance (5 SKs) ← 優先
│   ├── process-development (5 SKs)
│   ├── ...（其餘 5 skills）
│   └── → 重新打包 icp-governance.plugin
│
└── R-009: icp-presales gate0-decision-package

Phase 3 (P3): 收尾                        ← Day 61-62
├── R-010: forensic report supersession note
├── R-011: SCHEMA composition_patterns 標註
├── R-012: standalone skills 歸檔
└── R-013: README 更新
```

---

## 深化 SOP (每個 Skill)

```
1. 讀取 05-cowork-skills/{skill-name}/SKILL.md（現有骨架）
2. 讀取 SKILL.md 末尾 Source Traceability，找對應 SK 編號
3. 逐一讀取 03-skill-definitions/registry/SK-D{nn}-{nnn}.md
4. 從 SK 提取並展開：
   a. Description → 具體步驟操作指引（可執行手冊，非摘要）
   b. Outputs → markdown 交付物模板 (code blocks)
   c. Acceptance Criteria → 強化品質檢查清單 (≥5 可量化項)
   d. 領域知識 → ⚠️ Pitfalls/Anti-patterns 段落
   e. Tools → 工具指引 (含 code blocks if applicable)
5. 參考 Tier A 風格（arch-diagram, cbom-builder, presales, compliance-gap-assessor）
6. 寫入增強版 SKILL.md（目標 300-500 行）
7. 如需要建立 templates/ 和 references/ 子目錄
8. 完成一整個 Plugin 的全部 Skills 後重新打包 .plugin
```

---

## 每個 SKILL.md 的驗收標準 (DoD)

| # | 驗收項 | 通過條件 |
|---|--------|---------|
| 1 | 行數 | 250-500 行（精煉，不求最長） |
| 2 | Code blocks | ≥1 個程式碼或模板區塊 |
| 3 | Workflow | 具體操作步驟（可執行手冊，非 SK 摘要） |
| 4 | Quality Checklist | ≥5 個可量化驗收項 |
| 5 | Pitfalls | 含 ⚠️ 避坑指引段落 |
| 6 | Human Review Gate | 有角色專屬審核提示 |
| 7 | Source Traceability | 正確對應 SK 編號 |
| 8 | YAML Triggers | description 含中英文 MANDATORY TRIGGERS |
| 9 | 結構完整 | YAML + §0 初始化 + §1 輸入 + §2 工作流程 + §3 輸出 + §4 標準 + §5 品質檢查 + §6 工時 + §7 工具 + §8 審核閘門 + §9 生命週期 + §10 Source Traceability |

---

## Plugin 重新打包指令

```bash
# 以 icp-seceng 為例
cd /path/to/plugin-build/icp-seceng
# 結構：
# icp-seceng/
# ├── .claude-plugin/
# │   └── plugin.json
# └── skills/
#     ├── threat-risk-assessment/
#     │   └── SKILL.md
#     ├── security-system-hardening/
#     │   ├── SKILL.md
#     │   └── templates/  (if needed)
#     └── ...

zip -r /tmp/icp-seceng.plugin . -x "*.DS_Store"
```

---

## Plugin 級共用資源規劃

| Plugin | 建議共用 references/ | 建議共用 templates/ |
|--------|---------------------|---------------------|
| icp-seceng | IEC 62443-3-3 FR/SR 對照表, STRIDE/DREAD 評分指引 | 風險登錄冊模板, TRA 報告模板, 資產清冊模板 |
| icp-sysarch | Purdue Model 映射表, Zone 顏色規範 | 架構文件模板, VLAN 規劃表模板 |
| icp-integration | 協定對照表, API 規格模板 | FAT/SAT 計畫模板, 介面矩陣模板 |
| icp-governance | Gate 0-3 檢查清單, GOV-SD 附錄 C | Design Review Checklist 模板, RTM 模板 |
| icp-presales | (已有) review_checklist.md | (已有) feasibility/architecture/doc_inventory |

---

## 風險評估

| 風險 | 可能性 | 影響 | 緩解策略 |
|------|--------|------|---------|
| SK 定義內容不足以支撐深化 | Medium | High | 結合 Tier A 範例 + 領域知識 + source documents |
| 深化品質不一致 | Medium | Medium | 每 Plugin 完成後執行 Wave Review (T06+T07) |
| Plugin 重新打包格式錯誤 | Low | High | 建立標準打包腳本 + 安裝測試 |
| MANDATORY TRIGGERS 同 Plugin 內衝突 | Medium | Medium | 深化前先盤查 trigger 覆蓋度 |

---

*計畫日期：2026-03-18*
