---
name: gate0-decision-package
description: >
  Assemble and verify Gate 0 decision package consolidating all Pre-Gate 0 deliverables,
  and perform cost risk contingency analysis for project budget risk adjustment.
  MANDATORY TRIGGERS: Gate 0, 決策包, decision package, Gate 0 組裝,
  Gate 0 assembly, 成本風險, cost risk, contingency, 風險餘裕,
  risk contingency, Gate 0 package, 決策包組裝, gate review package,
  風險調整預算, risk-adjusted budget, 成本敏感度.
  Use this skill for Gate 0 decision package assembly and cost risk contingency analysis.
---

# Gate 0 決策包組裝與成本風險分析 (Gate 0 Decision Package & Cost Risk)

本 Skill 整合 2 個工程技能定義，將所有 Pre-Gate 0 產出整合為 Gate 0 決策包，並執行成本風險餘裕分析。

---

## 0. 初始化

1. **5 大 Gate 0 必要輸入**已產出 (或明確標示 gap)：
   - (1) 需求釐清記錄 (SK-D14-001)
   - (2) 風險預先揭露清單 (SK-D14-004)
   - (3) 可行性評估 (SK-D14-003)
   - (4) CBOM (SK-D14-005)
   - (5) 概念架構 (SK-D14-013)
2. **CBOM 已完成**：成本數據可用於風險餘裕計算

---

## 1. 工作流程

### Step 1: Gate 0 決策包組裝 (SK-D14-015)

**目標**：驗證完整性、評估品質閾值、組裝為正式決策包。

**GOV-SD Gate 0 四大品質閾值**：

| 閾值 | 定義 | 驗證方式 |
|------|------|---------|
| Comprehensibility | 決策者能理解內容 | 非技術人員 review |
| Evaluability | 內容足以做 Go/No-Go 決策 | 檢查 cost/risk/feasibility 數據 |
| Accountable Owner | 每項交付物有負責人 | 責任矩陣檢查 |
| Scope Stability | 範圍不會在評審中大幅變動 | 假設清單 + 風險清單穩定性 |

**操作步驟**：

1. **完整性檢查**：5 大必要輸入逐項驗證
   ```markdown
   | # | 必要輸入 | 來源 SK | 文件位置 | 版本 | 狀態 |
   |---|---------|--------|---------|------|------|
   | 1 | 需求釐清記錄 | SK-D14-001 | 01_brief/brief.md | v1.0 | ✅ |
   | 2 | 風險預先揭露 | SK-D14-004 | 03_work/risk_matrix.md | v1.0 | ✅ |
   | 3 | 可行性評估 | SK-D14-003 | 03_work/feasibility.md | v1.0 | ✅ |
   | 4 | CBOM | SK-D14-005 | 03_work/cbom.xlsx | v1.0 | ✅ |
   | 5 | 概念架構 | SK-D14-013 | 03_work/architecture.md | v1.0 | ✅ |
   ```

2. **品質閾值評估**：每個閾值 Pass/Fail
3. **交叉引用矩陣**：確保 5 大輸入間的數據一致
4. **已知缺口文件化**：未解決的 gap 記錄 owner + 解決路徑
5. **Gate 0 簡報摘要**：2-3 頁 executive summary
6. **責任移交備忘**：Pre-Gate → Post-Gate 的責任移交

**⚠️ 避坑**：
- 不要在缺少任何必要輸入的情況下提交 Gate 0——即使有 gap 也要文件化
- 品質閾值不是 checkbox——需實質評估 (Comprehensibility 需要非技術人員確認)
- 交叉引用不一致 (如 CBOM 金額 ≠ 可行性成本範圍) 會直接導致 Gate 0 fail

---

### Step 2: 成本風險餘裕分析 (SK-D14-016)

**目標**：計算風險調整後的 contingency reserve。

**操作步驟**：

1. **辨識成本風險驅動因素** (≥5 項)：
   ```markdown
   | Risk ID | 風險描述 | 機率 | 影響 (TWD) | 風險暴露 | 類別 |
   |---------|---------|------|-----------|---------|------|
   | CR-001 | 供應商漲價 | 30% | 500,000 | 150,000 | Supply |
   | CR-002 | 場域限制增加工時 | 40% | 300,000 | 120,000 | Schedule |
   | CR-003 | 匯率波動 (USD) | 20% | 200,000 | 40,000 | Financial |
   | CR-004 | 額外安全控制需求 | 25% | 400,000 | 100,000 | Scope |
   | CR-005 | Legacy 整合困難 | 35% | 350,000 | 122,500 | Technical |
   ```

2. **三情境模型**：
   ```markdown
   | 情境 | 基礎成本 | 風險調整 | Contingency % | 總計 |
   |------|---------|---------|-------------|------|
   | Low (Optimistic) | 5,000,000 | +200,000 | 4% | 5,200,000 |
   | Baseline (Expected) | 5,000,000 | +500,000 | 10% | 5,500,000 |
   | High (Pessimistic) | 5,000,000 | +1,200,000 | 24% | 6,200,000 |
   ```

3. **Contingency 分配**：按風險類別分配
4. **成本敏感度分析**：辨識對總成本影響最大的 ≥3 個風險
5. **緩解策略**：每個高風險有觸發條件+緩解措施
6. **Finance/PM 核准**：contingency 需正式核准
7. **Contingency 在預算中正式分離**：不混入基礎成本

**⚠️ 避坑**：
- Contingency 不是「加 10% 了事」——需有 risk-based 計算基礎
- 三情境差異太小 → 低估風險；差異太大 → 不可信
- 敏感度分析至少 3 個風險——識別哪些風險對預算影響最大

---

## 2. 輸出

| # | 交付物 | 步驟 |
|---|--------|------|
| 1 | Gate 0 Decision Package | 1 |
| 2 | Completeness Checklist (5 大輸入) | 1 |
| 3 | Quality Threshold Assessment | 1 |
| 4 | Cross-Reference Matrix | 1 |
| 5 | Gate 0 Briefing Summary (2-3 page) | 1 |
| 6 | Cost Risk Assessment Report | 2 |
| 7 | Contingency Reserve Calculation | 2 |
| 8 | Risk-Adjusted Budget (3 scenarios) | 2 |
| 9 | Cost Sensitivity Analysis | 2 |

---

## 3. 驗收標準

| # | 項目 | 條件 |
|---|------|------|
| 1 | 5 大輸入全部存在+驗證 current | ✓ |
| 2 | 4 品質閾值每項有 Pass/Fail | ✓ |
| 3 | 交叉引用一致 (成本/風險/範圍) | ✓ |
| 4 | 已知缺口有 owner+解決路徑 | ✓ |
| 5 | ≥5 成本風險驅動因素 | ✓ |
| 6 | 三情境 (Low/Base/High) 已計算 | ✓ |
| 7 | 敏感度分析 ≥3 個風險 | ✓ |
| 8 | Contingency 在預算中正式分離 | ✓ |

---

## 4. 工時

| 步驟 | Junior | Senior |
|------|--------|--------|
| Gate 0 組裝 | 3-5 pd | 2-3 pd |
| 成本風險分析 | 5-8 pd | 3-5 pd |

---

## 5. 人類審核閘門

```
Gate 0 決策包已組裝。
📋 5 大輸入：{pass}/{total} 通過 | 品質閾值：{qt_pass}/4
📊 成本：基礎 {base} | Contingency {pct}% | 風險調整 {adj}
⚠️ 缺口：{gaps} 項待解決
👉 請 HEAD (系統設計主管) 審核並決策 Gate 0 Go/No-Go/Conditional。
```

---

## 6. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D14-015 | Gate 0 Decision Package Assembly | 5 大輸入、4 品質閾值、交叉引用、責任移交 |
| SK-D14-016 | Cost Risk Contingency Analysis | 成本風險驅動、三情境、敏感度、Contingency 分離 |

<!-- Phase 6: Enhanced 2026-03-19. -->
