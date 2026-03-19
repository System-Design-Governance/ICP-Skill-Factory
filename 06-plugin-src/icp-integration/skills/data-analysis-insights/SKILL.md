---
name: data-analysis-insights
description: >
  資料分析與洞察：能源分析、儀表板設計、ML 模型、資料視覺化。
  MANDATORY TRIGGERS: 資料分析, data analysis, 儀表板, dashboard, 能源分析,
  energy analytics, ML, 機器學習, 資料視覺化, data visualization.
  Use this skill for data analytics and dashboard design in energy/OT/ICS projects.
---

# 資料分析與洞察 (Data Analysis & Insights)

整合 4 個 SK，涵蓋能源分析、儀表板設計、ML 模型、資料視覺化。

---

## 0. 初始化

1. 資料基礎設施已就緒 (TSDB + pipeline)
2. 分析需求已從業務端蒐集
3. 歷史資料已累積足夠量 (ML 需 ≥ 6 個月)
4. 視覺化工具已選定 (Grafana/PowerBI/custom)

---

## 1. 工作流程

### Step 1: 能源分析 (SK-D12-003)

**分析類型**：

| 類型 | 方法 | 輸出 | 典型用途 |
|------|------|------|----------|
| 負載預測 | ARIMA, LSTM, Prophet | 未來 24h/7d 負載曲線 | 排程最佳化 |
| 損耗分析 | 能量平衡計算 | 線損率、變壓器損耗 | 節能措施 |
| 功率品質 | FFT、THD 分析 | 諧波含量、電壓偏差 | 改善電能品質 |
| 設備健康 | 趨勢分析、異常偵測 | 劣化趨勢、RUL 預估 | 預防性維護 |

**步驟**：
1. 定義分析目標與 KPI
2. 資料準備：清洗、對齊、特徵工程
3. 選擇分析方法 (統計 vs. ML)
4. 建立分析模型 + 驗證 (train/test split)
5. 輸出分析結果 + 可行動建議
6. 設定自動化排程 (daily/weekly report)

**⚠️ 避坑**：
- 資料品質不足 → 模型輸出不可信 (garbage in, garbage out)
- 過度擬合 → 歷史表現好但預測失準
- 分析結果無行動建議 → 看了報告不知道該做什麼

### Step 2: 儀表板設計 (SK-D12-004)

**儀表板層級**：

| 層級 | 受眾 | 內容 | 更新頻率 |
|------|------|------|----------|
| Executive | 管理層 | KPI 摘要、趨勢 | 日/週 |
| Operational | 操作員 | 即時狀態、告警 | 秒級 |
| Analytical | 分析師 | 互動圖表、drill-down | 依需求 |
| Engineering | 工程師 | 詳細參數、歷史比對 | 依需求 |

**設計原則**：

| 原則 | 說明 |
|------|------|
| 5 秒規則 | 關鍵資訊 5 秒內可辨識 |
| 資訊密度 | 不過多也不過少，依受眾需求 |
| 色彩語義 | 紅=異常 黃=警告 綠=正常 (一致) |
| 互動性 | 支持 drill-down、時間範圍選擇、篩選 |

**步驟**：
1. 依受眾定義儀表板層級
2. 設計 wireframe (先畫草圖再實作)
3. 選擇視覺化元件 (gauge、trend、bar、map)
4. 連接資料源 (TSDB query)
5. 配置告警整合 (threshold → 變色/通知)
6. 使用者測試 → 迭代修改

**⚠️ 避坑**：
- 全部放一頁 → 資訊過載，什麼都看不到
- 即時儀表板查詢 raw data → TSDB 被拖垮

### Step 3: ML 模型開發 (SK-D12-007)

**OT/能源 ML 應用**：

| 應用 | 演算法 | 輸入 | 輸出 |
|------|--------|------|------|
| 負載預測 | LSTM, XGBoost | 歷史負載+天氣+日曆 | 未來負載 |
| 異常偵測 | Isolation Forest, AutoEncoder | 感測器多維資料 | 異常分數 |
| 設備 RUL | Survival Analysis, CNN | 振動+溫度+電流 | 剩餘壽命 |
| 分類/辨識 | Random Forest, SVM | 事件特徵 | 故障類型 |

**步驟**：
1. 問題定義 → 選擇 ML 類型 (regression/classification/anomaly)
2. 資料收集 + EDA (Exploratory Data Analysis)
3. 特徵工程：lag features、rolling stats、domain features
4. 模型訓練 + 超參數調優
5. 驗證：cross-validation、holdout test
6. 部署：batch prediction 或 online inference
7. 監控：model drift detection、retraining trigger

**⚠️ 避坑**：
- Data leakage (用了未來資料) → 測試指標虛高
- 未監控 model drift → 模型隨時間退化但無人知曉
- OT 資料不平衡 (故障極少) → accuracy 高但 recall 低

### Step 4: 資料視覺化 (SK-D12-008)

**圖表選擇指引**：

| 目的 | 推薦圖表 | 不適合 |
|------|----------|--------|
| 趨勢 | Line chart, Area | Pie chart |
| 比較 | Bar chart, Grouped bar | 3D chart |
| 分布 | Histogram, Box plot | Line chart |
| 比例 | Stacked bar, Treemap | Scatter |
| 相關 | Scatter, Heatmap | Pie chart |
| 地理 | Map, Choropleth | Bar chart |

**步驟**：
1. 確定溝通目標 (展示什麼 insight)
2. 選擇適合的圖表類型
3. 設計：標題、軸標、單位、圖例
4. 控制資料墨水比 (Data-Ink Ratio)
5. 確保色彩可及性 (色盲友善)
6. 靜態報告 vs. 互動 dashboard 選擇

**⚠️ 避坑**：3D 圓餅圖 → 視覺扭曲，定量比較不準確

---

## 2. 驗收標準

| # | 條件 |
|---|------|
| 1 | 能源分析模型通過驗證 (MAPE < 目標值) |
| 2 | 儀表板依受眾分層且符合 5 秒規則 |
| 3 | ML 模型含 drift 監控與 retraining 機制 |
| 4 | 視覺化符合色彩一致性與可及性標準 |
| 5 | 所有 dashboard query 效能 < 3s |
| 6 | 分析結果含可行動建議 |

---

## 3. 人類審核閘門

```
資料分析與洞察完成。
📋 範圍：4 個工程步驟 (SK-D12-003, 004, 007, 008)
📊 交付物：分析模型、儀表板、ML pipeline、視覺化規範
⚠️ 待確認：{TBD 項目}
👉 請 Data Engineer + 業務端 + OPS 審核。
```

---

## 4. Source Traceability

| SK | 名稱 | 核心知識 |
|----|------|---------|
| SK-D12-003 | Energy Analytics | 負載預測、損耗分析、功率品質 |
| SK-D12-004 | Dashboard Design | 層級設計、5 秒規則、告警整合 |
| SK-D12-007 | ML Model | 演算法選擇、特徵工程、drift 監控 |
| SK-D12-008 | Data Visualization | 圖表選擇、Data-Ink Ratio、色彩可及性 |

<!-- Phase 6: Enhanced 2026-03-19. -->
