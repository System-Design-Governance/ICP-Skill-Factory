---
name: ai-workflow-automation
description: >
  AI 與工作流自動化：AI 審查助手、CI/CD 管線、工作流程編排。
  MANDATORY TRIGGERS: AI 輔助, AI workflow, CI/CD, 工作流程自動化, workflow automation,
  AI review, 自動化管線, pipeline.
  Use this skill for AI-assisted review and workflow automation in OT/ICS projects.
---

# AI 與工作流自動化 (AI Workflow Automation)

整合 3 個 SK，涵蓋 AI 審查助手、CI/CD 管線、工作流程編排。

---

## 0. 初始化

1. 待自動化的工作流程已識別並文件化
2. AI/ML 工具與 API 已選定 (LLM API, rule engine)
3. CI/CD 平台已建立 (GitHub Actions / GitLab CI / Jenkins)
4. 團隊對 AI 輔助的期望與限制已對齊

---

## 1. 工作流程

### Step 1: AI 審查助手 (SK-D13-004)

**AI 審查能力層級**：

| 層級 | 能力 | 方法 | 準確率 |
|------|------|------|--------|
| L1 | 格式/命名規範檢查 | Rule-based | ~99% |
| L2 | 文件完整性檢查 | Checklist + NLP | ~95% |
| L3 | 技術一致性審查 | LLM + domain rules | ~85% |
| L4 | 設計品質評估 | LLM + expert prompt | ~70% |

**步驟**：
1. 定義審查規則 (命名、完整性、一致性)
2. L1-L2：實作 rule-based checker (regex, schema validation)
3. L3-L4：設計 LLM prompt + domain context injection
4. 建立審查報告格式 (finding ID, severity, location, suggestion)
5. 整合到文件審核流程 (PR review / document review)
6. 設定 human-in-the-loop：AI 建議 → 人類決定

**⚠️ 避坑**：
- AI 幻覺 → 建議修改正確的內容為錯誤的
- 過度信任 AI → 跳過人類審核，放行有問題的設計
- L3-L4 準確率不穩定 → 需持續監控 precision/recall

### Step 2: CI/CD 管線設計 (SK-D13-005)

**工程文件 CI/CD Pipeline**：

```
Commit → Lint/Format → Validation → Build → Test → Review → Deploy
  │         │            │           │       │       │        │
 Git    Naming check  SK-D13-003   Doc Gen  Unit   Human   Publish
        + schema      rules       render   test   gate    to DMS
```

**Pipeline 階段**：

| 階段 | 工具 | Fail 條件 |
|------|------|-----------|
| Lint | Custom linter | 命名違規 |
| Validate | SK-D13-003 validation tool | 規則 fail |
| Build | Doc generator (SK-D13-002) | 產出失敗 |
| Test | Unit test + integration test | Test fail |
| Security Scan | SAST / dependency check | CVE found |
| Review Gate | Human approval | Reviewer reject |

**步驟**：
1. 定義 pipeline 觸發條件 (push, PR, schedule)
2. 配置 lint + validation stage
3. 整合 doc generator 為 build stage
4. 配置 test stage (unit + integration)
5. 加入 security scan (依賴庫掃描)
6. 設定 human review gate (approval required)
7. 配置 deploy stage (publish to DMS/repository)

**⚠️ 避坑**：
- Pipeline 太慢 → 團隊繞過直接手動發布
- 無 human gate → 自動發布未審核文件
- Secret 硬編碼在 pipeline config → 洩漏

### Step 3: 工作流程編排 (SK-D13-006)

**編排模式**：

| 模式 | 適用場景 | 工具 |
|------|----------|------|
| Sequential | 線性流程 (A→B→C) | Any workflow engine |
| Parallel | 獨立任務同時執行 | Airflow, Prefect |
| Conditional | 依條件分支 | BPMN, Camunda |
| Event-driven | 外部事件觸發 | Kafka + workflow |
| Human-in-loop | 需人類決策 | Approval workflow |

**常見工程工作流程**：

| 工作流程 | 步驟 | 自動化程度 |
|----------|------|------------|
| 設計審核 | 提交→AI check→人類審核→核准 | 70% |
| 文件發行 | 撰寫→lint→build→review→publish | 80% |
| 測試執行 | 排程→執行→記錄→報告→追蹤 | 60% |
| 缺陷管理 | 登記→分派→修復→驗證→關閉 | 50% |

**步驟**：
1. 繪製現有流程 (as-is) 並識別瓶頸
2. 設計目標流程 (to-be) 含自動化節點
3. 選擇編排工具 (Airflow / Prefect / custom)
4. 實作 task definitions + dependencies
5. 設定 error handling (retry, fallback, notification)
6. 配置監控 (task duration, success rate, SLA)
7. 漸進部署：先一個流程 → 驗證 → 擴展

**⚠️ 避坑**：
- 一次自動化所有流程 → 太多變動，團隊無法適應
- 自動化壞掉的流程 → 壞得更快 (先修流程再自動化)
- 未設 SLA 監控 → 流程卡住數天無人知曉

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | AI 審查 L1-L2 準確率 ≥ 95% |
| 2 | CI/CD pipeline 端到端運作，含 human gate |
| 3 | Pipeline 執行時間 < 10 min (典型 commit) |
| 4 | 工作流程含 error handling + monitoring |
| 5 | Human-in-the-loop 節點已設定 (AI 不自動決策) |
| 6 | Secret 管理正確 (vault, 非 plaintext) |

---

## 3. 人類審核閘門

```
AI 與工作流自動化完成。
📋 範圍：3 個工程步驟 (SK-D13-004, 005, 006)
📊 交付物：AI 審查規則、CI/CD pipeline、工作流程配置
⚠️ 待確認：{TBD 項目}
👉 請 SYS + DevOps + QAM 審核。
```

---

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D13-004 | AI Review Assistant | 規則分層 L1-L4、LLM prompt、human-in-loop |
| SK-D13-005 | CI/CD Pipeline | Lint→Validate→Build→Test→Review→Deploy |
| SK-D13-006 | Workflow Orchestration | 編排模式、工具選型、漸進部署 |

<!-- Phase 6: Enhanced 2026-03-19. -->
