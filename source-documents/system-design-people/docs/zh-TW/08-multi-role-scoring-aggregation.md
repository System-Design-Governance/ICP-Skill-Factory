# 多角色績效計分與公平聚合模型

## Multi-Role Performance Scoring and Fair Aggregation Model

**文件編號：** GOV-04-001
**文件版本：** 1.1
**生效日期：** 2026-02-09
**文件層級：** 多角色與公平性治理文件
**依據文件：** GOV-02-001 角色定義與職責說明、GOV-03-002 KPI 評分模型

---

## 文件目的

本文件定義當一人擔任多個功能性角色時，如何：
1. 公平、可稽核且保留當責精神地將各角色分數聚合為個人績效分數
2. 允許多角色高品質表現合法超越單一角色貢獻
3. 確保聚合過程完全透明且可重現

本文件**非**獎酬分配文件，獎酬映射請參閱 GOV-04-002 貢獻對獎酬映射。

---

## 設計理念與原則

### 組織意圖

本組織基於以下認知設計本模型：

| 認知 | 說明 |
|-----|------|
| 責任與產出須量化 | 個人貢獻透過角色當責與可驗證產出量化，非主觀評價 |
| 多角色不應處於劣勢 | 承擔更多責任不應在結構上產生負期望值 |
| 高品質多角色代表更高貢獻 | 於多角色皆維持高品質表現，合法創造超越單一角色之貢獻價值 |
| 可稽核性與公平性優先 | 所有機制皆為規則式、可重現、可稽核 |

### 設計目標

| 目標 | 實現機制 |
|-----|---------|
| 鼓勵角色承接 | Role Load Stabilizer (RLS) |
| 維持當責完整性 | Critical Role Failure Protection |
| 獎勵多角色卓越 | Multi-Role Excellence Multiplier (MREM) |
| 避免分數膨脹 | 嚴格啟動條件與上限控制 |
| 保持可稽核性 | 全流程紀錄與規則式計算 |

### 核心原則

| 原則 | 說明 |
|-----|------|
| 角色獨立評估 | 每個角色之 KPI 先獨立計算，再進行聚合 |
| 當責不稀釋 | 擔任多角色不得降低任一角色之當責標準 |
| 風險敏感性 | 高風險角色之失敗不得被低風險角色之成功掩蓋 |
| 品質一致性獎勵 | 多角色卓越乘數基於品質一致性，非角色數量 |
| 可稽核性 | 聚合過程須完全透明且可重現 |

### 禁止事項

| 禁止項目 | 理由 |
|---------|------|
| 簡單平均 | 忽略角色重要性差異，高風險角色失敗被稀釋 |
| 取最高分 | 鼓勵忽略低分角色，破壞當責完整性 |
| 取最低分 | 過度懲罰，抑制多角色承擔意願 |
| 角色數量加權 | 鼓勵角色膨脹，偏離實質貢獻 |
| 主管主觀裁量 | 破壞可稽核性，引入不公平風險 |
| 乘數掩蓋失敗 | 任何乘數皆不得覆蓋當責失敗 |
| 登記未參與計分 | 登記角色但未實質參與者不得計入激勵機制 |

---

## 術語定義

| 術語 | 定義 |
|-----|------|
| Role Final Score | 角色層級最終分數 = Base Score + Exception Bonus（上限 110） |
| Base Score | 角色基本 KPI 計分（滿分 100 分） |
| Exception Bonus | 例外加分（單一角色上限 +10 分） |
| RCW (Role Contribution Weight) | 角色貢獻權重，反映角色於治理中之相對重要性 |
| AF (Allocation Factor) | 配置係數，反映個人於該角色之投入比例 |
| Individual Score (Raw) | 聚合後之原始個人分數，尚未套用調整機制 |
| RLS (Role Load Stabilizer) | 角色負荷穩定器，抵消多角色評估波動性之結構調整 |
| MREM (Multi-Role Excellence Multiplier) | 多角色卓越乘數，獎勵多角色皆維持高品質表現 |
| Final Individual Score | 最終個人分數，套用所有調整後之分數（上限 100） |
| Critical Role Failure | 關鍵角色失敗，任一角色 Base Score < 60 之情形 |
| Governance Failure Flag | 治理失敗標記，觸發失敗保護時設定，獨立於分數 |

---

## 模型架構概覽

本模型整合三個層次：

| 層次 | 名稱 | 目的 | 性質 |
|-----|------|------|------|
| Layer 1 | Role Load Stabilizer (RLS) | 抵消多角色評估波動性 | 結構性穩定器 |
| Layer 2 | Multi-Role Excellence Multiplier (MREM) | 獎勵多角色高品質一致表現 | 品質卓越放大器 |
| Layer 3 | Governance Safeguards | 保護當責完整性 | 治理保護機制 |

### 計算順序（強制）

```
角色基本分 (Base Scores)
    ↓
角色例外加分 (Exception Bonuses, capped)
    ↓
角色聚合 (Role Aggregation)
    ↓
治理保護機制 (Governance Safeguards)
    ↓
Role Load Stabilizer (RLS)
    ↓
Multi-Role Excellence Multiplier (MREM)
    ↓
Final Individual Score (cap at 100)
```

---

## 角色貢獻權重 (RCW)

### 設計理念

角色貢獻權重（RCW）反映各角色於組織治理中之相對重要性，而非個人投入時間。權重設計須滿足：

1. **風險承擔對應**：高風險角色高權重
2. **當責範圍對應**：廣泛當責角色高權重
3. **可替代性對應**：難以替代之角色高權重
4. **組織依賴對應**：組織高度依賴之角色高權重

### 標準 RCW 定義

| 角色 | 標準 RCW | 權重理由 |
|:-----------------------------|:----------:|:-----------------------------------------------|
| Head of System Design | 1.00 | 最高當責、標準體系擁有權、最終裁決權 |
| System Design Governance Lead | 0.90 | Gate 1/3 核准權、治理框架擁有權、爭議仲裁 |
| System Architect | 0.85 | 設計文件當責、技術可行性當責、架構標準擁有權 |
| Security Engineering Role | 0.85 | IEC 62443 合規當責、風險評估當責、安全標準擁有權 |
| Design QA Role | 0.75 | 品質驗證當責、追溯性標準擁有權 |
| Pre-Gate Design Support | 0.75 / 0.50 | **條件式 RCW**：後續 Gate 驗證貢獻有效時 0.75，否則 0.50 |
| Design Governance Coordinator | 0.60 | 流程協調當責、執行支援角色 |

### Pre-Gate Design Support 條件式 RCW 機制

**設計意圖**：Pre-Gate Design Support 角色之較高 RCW（0.75）須以「後續 Gate 可驗證之貢獻」為依據，而非自我宣稱或商務成果。此設計確保 RCW 提高與實質治理貢獻直接連結。

#### RCW 生效條件

| 條件代號 | 條件說明 | 驗證時點 | 驗證方式 |
|:----------:|:----------------------------------|:-------------|:---------------------------|
| PGDS-1 | 預釐清需求於 Gate 0 被採用 | Gate 0 核准後 | Gate 0 核准紀錄引用預釐清文件 |
| PGDS-2 | 預揭露風險於後續 Gate 未重複識別 | Gate 3 完成後 | 殘餘風險清單交叉比對 |
| PGDS-3 | 後續設計階段無因「需求澄清不足」導致之返工 | Gate 1 後 30 日 | 設計變更紀錄分析 |

#### RCW 判定規則

```
If ALL conditions (PGDS-1 AND PGDS-2 AND PGDS-3) met:
    RCW = 0.75 (高貢獻權重)
Else:
    RCW = 0.50 (基礎貢獻權重)
```

#### RCW 判定時點

由於 Pre-Gate Design Support 之貢獻須待後續 Gate 驗證，其 RCW 判定時點如下：

| 情境 | RCW 判定時點 | 說明 |
|-----|-------------|------|
| 專案已完成 Gate 3 | Gate 3 完成後 30 日內 | 完整驗證所有條件 |
| 專案僅完成 Gate 1 | Gate 1 後 30 日 | 暫以 PGDS-1 + PGDS-3 判定，PGDS-2 待 Gate 3 補驗 |
| 專案尚未進入 Gate 0 | 評估週期結束時 | RCW = 0.50（未驗證） |

#### RCW 追溯調整

若於評估週期結束後，後續 Gate 結果顯示驗證條件變更，得追溯調整：

| 情境 | 追溯動作 |
|-----|---------|
| 原採用 RCW = 0.75，後續驗證失敗 | 追溯降為 0.50，調整最終分數 |
| 原採用 RCW = 0.50，後續驗證通過 | 追溯升為 0.75，調整最終分數 |

追溯調整期限：Gate 3 完成後 60 日內。

---

## 後驗修正因子 (Post-Verification Factor, PVF)

### 設計目的

強化後驗驗證對績效權重的影響。當後續 Gate 結果顯示設計階段決策或交付存在可歸責瑕疵時，該角色之聚合權重須向下調整。

### 適用範圍

| 角色 | 適用 PVF | 理由 |
|-----|---------|------|
| System Architect | 是 | 設計基線品質須經後續 Gate 驗證 |
| Security Engineering Role | 是 | 風險評估有效性須經後續 Gate 驗證 |
| Pre-Gate Design Support | 否（已有條件式 RCW） | 條件式 RCW 已涵蓋後驗調整 |
| 其他角色 | 否 | 標準維護類 KPI 無需後驗 |

### PVF 觸發條件

| 條件代號 | 條件說明 | 驗證時點 | 適用角色 |
|---------|---------|---------|---------|
| PVF-SA-1 | Gate 1 後設計變更中「設計基線錯誤」類變更比例 ≥ 20% | Gate 1 後 30 日 | System Architect |
| PVF-SA-2 | Gate 3 最終文件包存在因「技術可行性誤判」導致之重大修訂 | Gate 3 完成後 | System Architect |
| PVF-SE-1 | Gate 3 殘餘風險中包含「威脅情境遺漏」類風險 | Gate 3 完成後 | Security Engineering Role |
| PVF-SE-2 | SL Decision 於 Gate 2 後發生非計畫性變更 | Gate 2 後 | Security Engineering Role |

### PVF 計算

```
若觸發任一 PVF 條件：
    PVF = 0.95（該角色聚合權重乘以 0.95）
若觸發兩項以上 PVF 條件：
    PVF = 0.90
若無觸發：
    PVF = 1.00
```

### PVF 套用位置

PVF 於聚合計算時套用於該角色之 RCW：

```
Effective RCW = RCW × PVF

Individual Score (Raw) = Σ(Role Final Score_i × Effective RCW_i × AF_i) / Σ(Effective RCW_i × AF_i)
```

### PVF 與條件式 RCW 之區分

| 項目 | 條件式 RCW（Pre-Gate Design Support） | PVF（System Architect / Security Engineering Role） |
|-----|-------------------------------------|---------------------------------------------------|
| 觸發邏輯 | 貢獻驗證失敗 → RCW 降級 | 後驗瑕疵 → 權重折減 |
| 調整幅度 | 0.75 → 0.50（33% 降幅） | × 0.95 或 × 0.90（5-10% 折減） |
| 設計意圖 | 獎勵須以驗證為前提 | 責任須以結果為依據 |

### RCW 調整機制

組織可依實際狀況調整 RCW，但須遵守以下限制：

| 限制 | 說明 |
|-----|------|
| 調整幅度 | 任一角色 RCW 調整不得超過 ±0.15 |
| 層級維持 | Head of System Design 須維持最高 RCW |
| 核准權限 | RCW 調整須經高階管理層核准 |
| 有效期間 | 調整後之 RCW 至少適用一個完整評估週期 |
| Pre-Gate Design Support 限制 | 條件式 RCW 機制不得調整為固定 RCW |

---

## 角色配置係數 (Allocation Factor)

### 標準配置係數

| 配置狀態 | Allocation Factor | 適用情境 |
|---------|-------------------|---------|
| 完全擔任 | 1.0 | 該角色由單人完全負責 |
| 主要擔任 | 0.7 | 該角色由多人共同負責，本人為主要負責人 |
| 次要擔任 | 0.3 | 該角色由多人共同負責，本人為次要負責人 |
| 備援擔任 | 0.1 | 僅於主要負責人不在時代理 |

### 配置係數限制

- 同一角色之所有擔任者 Allocation Factor 總和須 ≤ 1.2（容許適度重疊）
- 個人 Allocation Factor 總和無上限（可完全擔任多個角色）

### Allocation Factor 客觀判定依據

**設計目的**：確保 Allocation Factor 之判定具備客觀、可稽核、可重現之基礎，避免主觀認定導致之公平性爭議。

#### 判定維度

Allocation Factor 之判定須綜合考量以下三個維度：

| 維度 | 權重 | 說明 |
|:--------------------------------------|:-------:|:-------------------------------|
| 文件當責 (Documentation Accountability) | 40% | 該角色產出文件之實際負責比例 |
| RACI 登記 (RACI Matrix Registration) | 30% | 組織 RACI 矩陣中之正式登記狀態 |
| Gate 參與 (Gate Participation) | 30% | 各 Gate 審查中之實際參與與簽核 |

#### 文件當責判定標準

| 指標 | AF = 1.0（完全） | AF = 0.7（主要） | AF = 0.3（次要） | AF = 0.1（備援） |
|:------------|:------------------:|:------------------:|:------------------:|:------------------:|
| 文件版本控制者 | 唯一控制者 | 主要控制者 | 協作者 | 不涉及 |
| 文件審核簽署 | 唯一簽署者 | 主要簽署者 | 會簽者 | 備援簽署者 |
| 文件發布權限 | 唯一發布權 | 主要發布權 | 無發布權 | 無發布權 |
| 文件修訂當責 | 唯一修訂者 | 主要修訂者 | 協助修訂 | 不涉及 |

**證據來源**：版本控制紀錄、文件簽核紀錄、發布權限設定

#### RACI 矩陣判定標準

| RACI 登記狀態 | 對應 AF | 說明 |
|--------------|---------|------|
| Accountable（A）且唯一 | 1.0 | 該角色之 A 僅登記一人 |
| Accountable（A）且為主要 | 0.7 | 該角色之 A 登記多人，本人為主要 |
| Responsible（R）或 Consulted（C） | 0.3 | 非當責者但有實質參與 |
| Informed（I）或備援登記 | 0.1 | 僅接收資訊或備援 |

**證據來源**：組織 RACI 矩陣、角色指派紀錄

#### Gate 參與判定標準

| Gate 參與程度 | 對應 AF | 判定標準 |
|-------------|---------|---------|
| 完全參與 | 1.0 | 所有相關 Gate 皆以該角色身分參與並簽核 |
| 主要參與 | 0.7 | ≥ 70% 相關 Gate 以該角色身分參與並簽核 |
| 次要參與 | 0.3 | 30-70% 相關 Gate 以該角色身分參與 |
| 備援參與 | 0.1 | < 30% 相關 Gate 參與（通常為代理情形） |

**證據來源**：Gate 審查紀錄、會議簽到紀錄、核准簽核紀錄

#### 綜合判定流程

```
Step 1: 蒐集各維度證據
        - 文件控制紀錄
        - RACI 矩陣登記
        - Gate 參與紀錄

Step 2: 依各維度標準判定分項 AF
        - AF_文件 = 文件當責判定結果
        - AF_RACI = RACI 登記判定結果
        - AF_Gate = Gate 參與判定結果

Step 3: 計算加權 AF
        AF_計算 = AF_文件 × 0.4 + AF_RACI × 0.3 + AF_Gate × 0.3

Step 4: 對應至標準 AF 層級
        - AF_計算 ≥ 0.85 → AF = 1.0（完全擔任）
        - 0.55 ≤ AF_計算 < 0.85 → AF = 0.7（主要擔任）
        - 0.25 ≤ AF_計算 < 0.55 → AF = 0.3（次要擔任）
        - AF_計算 < 0.25 → AF = 0.1（備援擔任）

Step 5: Head of System Design 核定最終 AF
```

#### 判定紀錄要求

| 紀錄項目 | 內容要求 |
|---------|---------|
| 判定日期 | 評估週期開始日期 |
| 被判定者 | 人員姓名與工號 |
| 判定角色 | 角色名稱 |
| 各維度證據 | 文件、RACI、Gate 證據引用 |
| 各維度分項 AF | AF_文件、AF_RACI、AF_Gate |
| 計算過程 | AF_計算 數值 |
| 最終 AF | 對應之標準 AF 層級 |
| 核定者 | Head of System Design 簽核 |

#### 爭議處理

| 爭議類型 | 處理方式 |
|---------|---------|
| 證據不足 | 依現有證據判定，無法證明者視為較低層級 |
| 證據矛盾 | 以最近期且最正式之紀錄為準 |
| 判定結果爭議 | 由 Head of System Design 依證據裁決，裁決為最終決定 |

---

## 實質參與驗證 (Substantive Participation Verification, SPV)

### 設計目的

防止策略性承擔角色卻未產生實質價值。登記角色但未實際參與者，不應獲得 RLS 與 MREM 之激勵效果。

### SPV 驗證條件

每角色須通過 SPV 方可計入 RLS 與 MREM 之有效角色數（N_effective）：

| 條件代號 | 條件說明 | 驗證方式 |
|---------|---------|---------|
| SPV-1 | AF ≥ 0.5 | 依 AF 判定結果 |
| SPV-2 | Gate 簽核參與率 ≥ 50% | Gate 簽核紀錄 |

**判定規則**：

```
If SPV-1 OR SPV-2 met:
    角色通過 SPV → 計入 N_effective
Else:
    角色未通過 SPV → 不計入 N_effective（但仍納入分數聚合）
```

### SPV 對 RLS / MREM 之影響

| 情境 | N_total | N_effective | RLS 適用 N | MREM 適用 N |
|-----|---------|-------------|-----------|-------------|
| 2 角色皆通過 SPV | 2 | 2 | 2 | 2 |
| 2 角色僅 1 通過 SPV | 2 | 1 | 1 | 不適用（< 2） |
| 3 角色僅 2 通過 SPV | 3 | 2 | 2 | 2 |
| 3 角色僅 1 通過 SPV | 3 | 1 | 1 | 不適用（< 2） |

### SPV 未通過之角色處理

| 處理項目 | 說明 |
|---------|------|
| 分數聚合 | 仍納入聚合計算（依 RCW × AF） |
| RLS / MREM 計算 | 不計入有效角色數 |
| 連續未通過警示 | 連續 2 個評估週期未通過 SPV，須重新評估角色指派 |

---

## 個人分數聚合公式

### 基本聚合公式

當一人擔任 n 個角色時，個人綜合分數計算如下：

```
Individual Score (Raw) = Σ(Role Final Score_i × Effective RCW_i × AF_i) / Σ(Effective RCW_i × AF_i)
```

其中：
- **Role Final Score_i**：第 i 個角色之最終分數
- **Effective RCW_i**：第 i 個角色之有效角色貢獻權重 = RCW_i × PVF_i
- **RCW_i**：第 i 個角色之角色貢獻權重（含條件式 RCW 判定結果）
- **PVF_i**：第 i 個角色之後驗修正因子（適用角色為 0.90-1.00，其他角色為 1.00）
- **AF_i**：第 i 個角色之配置係數

### 聚合公式範例

**情境**：某人擔任 System Architect（完全）及 Security Engineering Role（主要）

```
計算步驟：
1. System Architect:
   - Role Final Score = 92
   - RCW = 0.85, AF = 1.0
   - 貢獻 = 92 × 0.85 × 1.0 = 78.2

2. Security Engineering Role:
   - Role Final Score = 88
   - RCW = 0.85, AF = 0.7
   - 貢獻 = 88 × 0.85 × 0.7 = 52.36

3. 權重總和 = (0.85 × 1.0) + (0.85 × 0.7) = 1.445

4. Individual Score (Raw) = (78.2 + 52.36) / 1.445 = 90.32
```

---

## Role Load Stabilizer (RLS)

### 定義與目的

**目的**：抵消多角色擔任者因評估面向增加而產生之結構性波動風險，使多角色擔任不成為負期望值選擇。

**重要說明**：RLS 為結構性穩定器，非努力獎勵、非績效加分、非角色數量獎金。RLS 存在之理由為移除結構性劣勢，而非創造優勢。

### RLS 公式

```
RLS = min(1 + 0.02 × (N_effective - 1), 1.05)
```

其中：
- **N_effective**：本評估週期內通過 SPV 驗證之有效角色數量
- **RLS 上限**：1.05（最多 5% 調整）

| 有效角色數量 (N_effective) | RLS 值 |
|--------------------------|--------|
| 1 | 1.00（無調整） |
| 2 | 1.02 |
| 3 | 1.04 |
| 4+ | 1.05（上限） |

**重要說明**：未通過 SPV 驗證之角色不計入 N_effective，但其分數仍納入聚合計算。

### RLS 治理合理性

| 特性 | 說明 |
|-----|------|
| 不掩蓋失敗 | Critical Role Failure Protection 仍優先適用 |
| 不創造白吃分數 | 須先有合格基本分才有調整空間 |
| 有上限 | 最多 5%，不因角色無限增加而無限膨脹 |
| 非獎勵 | 目的為移除劣勢，非創造優勢 |

### RLS 濫用防範

| 防範措施 | 說明 |
|---------|------|
| 上限控制 | RLS 最高 1.05，無法無限膨脹 |
| 角色數量中立 | 5% 調整不足以扭轉實質績效差異 |
| 不救失敗 | RLS 不能覆蓋失敗保護結果 |
| 年度驗證 | 若多角色溢價率 > 5%，須調降 RLS 係數 |

---

## Multi-Role Excellence Multiplier (MREM)

### 定義與目的

**目的**：允許多角色高品質一致表現合法超越單一角色貢獻。

**設計理念**：
- 於多個角色皆維持高品質表現，代表個人承擔更多責任並持續創造價值
- 此貢獻應被量化並允許合法獲得更高評價
- MREM 非角色數量獎勵，而是品質一致性獎勵

**重要說明**：MREM 為全有或全無（All-or-Nothing）機制。任一條件不滿足，MREM 即不適用。

### MREM 啟動條件

**所有條件皆須滿足**：

| 條件代號 | 條件說明 | 理由 |
|---------|---------|------|
| MREM-1 | 角色數量 N ≥ 2 | 單一角色無需卓越乘數 |
| MREM-2 | 每個角色之 Base Score ≥ 85 | 確保高品質一致性 |
| MREM-3 | 未觸發 Critical Role Failure Protection | 失敗不可被放大 |
| MREM-4 | 無角色以例外加分彌補基本 KPI 失敗 | 例外加分不得掩蓋缺陷 |
| MREM-5 | 每個角色之 Allocation Factor ≥ 0.3 | 排除備援角色 |
| MREM-6 | Pre-Gate Design Support 不得為唯一額外角色 | 詳見下方說明 |
| MREM-7 | 每個角色須通過 SPV 驗證 | 實質參與方可觸發卓越獎勵 |
| MREM-8 | 依賴後驗之角色須後驗完成且 PVF ≥ 0.95 | 後驗瑕疵角色不觸發 MREM |

### Pre-Gate Design Support 與 MREM 限制

**設計意圖**：Pre-Gate Design Support 角色之貢獻已透過條件式 RCW 機制獎勵。為避免貢獻重複計算，且維持 MREM 作為「核心設計角色卓越表現」之定位，設定以下限制：

#### MREM-6 條件說明

```
Pre-Gate Design Support 角色不得單獨觸發 MREM。

即：若個人擔任 N 個角色，且其中包含 Pre-Gate Design Support，
則 MREM 之 N 值計算須排除 Pre-Gate Design Support。

MREM 適用判定之 N_effective = N_total - N_PGDS
```

**範例**：

| 擔任角色組合 | N_total | N_effective | MREM 適用？ |
|-------------|---------|-------------|-------------|
| System Architect + Pre-Gate Design Support | 2 | 1 | 否（N_effective < 2） |
| System Architect + Security Engineering Role | 2 | 2 | 是（若其他條件滿足） |
| System Architect + Security Engineering Role + Pre-Gate Design Support | 3 | 2 | 是（若其他條件滿足） |
| Pre-Gate Design Support（單一角色） | 1 | 0 | 否 |

#### 限制理由

| 理由 | 說明 |
|-----|------|
| 避免貢獻重複計算 | 條件式 RCW 已獎勵 Pre-Gate Design Support 之高貢獻 |
| 維持 MREM 定位 | MREM 定位為「核心設計角色卓越表現」獎勵 |
| 責任對應 | Pre-Gate Design Support 不承擔設計責任，不應觸發設計卓越乘數 |
| 公平性 | 確保承擔設計責任之角色獲得適當獎勵優先權 |

### MREM 公式

```
MREM = min(1 + 0.03 × (N - 1), 1.10)
```

其中：
- **N**：本評估週期內擔任之角色數量
- **MREM 上限**：1.10（最多 10% 放大）

| 角色數量 (N) | MREM 值（若啟動） |
|-------------|------------------|
| 1 | 不適用（N < 2） |
| 2 | 1.03 |
| 3 | 1.06 |
| 4+ | 1.10（上限） |

### MREM 適用規則

```
If ALL MREM conditions met:
    MREM Adjusted Score = min(RLS Adjusted Score × MREM, 100)
    MREM Status = "Activated"
Else:
    MREM Adjusted Score = RLS Adjusted Score
    MREM Status = "Not Qualified" (列出未滿足之條件)
```

### MREM 治理說明

| 特性 | 說明 |
|-----|------|
| 不救失敗 | 失敗保護觸發時 MREM 自動不適用 |
| 全有或全無 | 任一條件不滿足即完全不適用 |
| 品質一致性基礎 | 基於每角色皆高品質，非角色數量 |
| 有上限 | 最多 10%，避免過度放大 |
| 最終分數仍有上限 | MREM 調整後仍不得超過 100 |

### MREM 濫用防範

| 防範措施 | 說明 |
|---------|------|
| 高門檻 | 每角色 Base Score ≥ 85 為嚴格要求 |
| 例外加分不救 | MREM-4 確保例外加分未掩蓋缺陷 |
| AF 下限 | 備援角色（AF < 0.3）不計入 |
| 上限控制 | 最多 10%，無法無限膨脹 |
| 全有或全無 | 無部分啟動，防止邊緣案例爭議 |

---

## 治理保護機制

### Critical Role Failure Protection

**目的**：防止關鍵角色之重大失敗被其他角色之成功掩蓋

**機制**：

```
若任一角色之 Base Score < 60，則：
Individual Score = min(Individual Score, 該角色 Base Score + 10)
Governance Failure Flag = TRUE
MREM 自動不適用
```

### Role Acceptance Threshold (RAT) 豁免

**目的**：避免因新接角色之過渡期表現而立即觸發失敗保護。

**RAT 豁免條件（全數滿足）**：

| 條件代號 | 條件說明 |
|---------|---------|
| RAT-1 | 該角色為新指派角色（本評估週期內首次指派） |
| RAT-2 | 該角色之 Allocation Factor ≤ 0.7（非完全擔任） |
| RAT-3 | 該角色之 Base Score ≥ 70（未達嚴重失敗程度） |

**RAT 豁免效果**：
- 符合條件之新指派角色不觸發 Critical Role Failure Protection
- 該角色分數仍納入聚合計算
- 豁免僅適用一個評估週期

### Minimum Weight Protection

**目的**：防止低配置角色被忽略

**機制**：

```
任一角色於 Individual Score 計算中之實際權重貢獻不得低於 15%
即：(RCW_i × AF_i) / Σ(RCW_j × AF_j) ≥ 0.15
```

### Exception Bonus Aggregation Cap

**目的**：防止多角色例外加分累積過高

**機制**：

```
Individual Exception Bonus Contribution =
    Σ(Role Exception Bonus_i × RCW_i × AF_i) / Σ(RCW_i × AF_i)

Individual Exception Bonus Cap = 10 分（與單一角色上限相同）
```

### 乘數不覆蓋失敗保護

**強制規則**：

```
If Critical Role Failure Protection triggered:
    Protected Score = min(Individual Score Raw, Failure Cap)
    RLS Score = min(Protected Score × RLS, 100)
    MREM = 1.00 (不適用)
    Final Score = RLS Score
    Governance Failure Flag = TRUE
```

---

## 完整計分流程

```
Step 1: 各角色 KPI 獨立評估
        ↓
Step 2: 各角色基本分計算
        ↓
Step 3: 各角色例外加分資格判定與計算
        ↓
Step 4: 各角色最終分數確定（Role Final Score ≤ 110）
        ↓
Step 5: 角色配置係數確認（依 AF 客觀判定標準）
        ↓
Step 6: 實質參與驗證（SPV）判定
        ↓
Step 7: 後驗修正因子（PVF）判定（適用角色）
        ↓
Step 8: 條件式 RCW 判定（Pre-Gate Design Support）
        ↓
Step 9: 計算 Effective RCW = RCW × PVF
        ↓
Step 10: 聚合公式計算 Individual Score (Raw)
        ↓
Step 11: Critical Role Failure Protection 檢查（含 RAT 豁免判定）
        ↓
Step 12: Minimum Weight Protection 檢查
        ↓
Step 13: Exception Bonus Aggregation Cap 檢查
        ↓
Step 14: Protected Score 確定
        ↓
Step 15: 計算 N_effective（通過 SPV 之角色數）
        ↓
Step 16: RLS 係數計算與套用（依 N_effective）
        ↓
Step 17: MREM 資格檢查（八項條件）
        ↓
Step 18: MREM 係數計算與套用（若適用）
        ↓
Step 19: Final Score 確定（上限 100）
        ↓
Step 20: Governance Failure Flag 設定
```

---

## 角色配置係數決定程序

| 步驟 | 說明 | 當責者 |
|-----|------|-------|
| 1 | 角色指派紀錄更新 | Head of System Design |
| 2 | 各維度證據蒐集 | 績效評估執行者 |
| 3 | 配置狀態判定（依 6.3 標準） | 績效評估執行者 |
| 4 | Allocation Factor 核定 | Head of System Design |
| 5 | 新指派角色標記 | Head of System Design |
| 6 | 每評估週期開始前確認 | 績效評估執行者 |

---

## 跨角色公平性驗證

### 公平性驗證指標

| 指標 | 定義 | 目標 |
|-----|------|-----|
| 多角色溢價率 | (多角色平均分 - 單角色平均分) / 單角色平均分 | ≤ 10% |
| MREM 啟動率 | MREM 啟動人次 / 多角色人次 | 監控（無目標） |
| 卓越層達成率差異 | 多角色卓越達成率 - 單角色卓越達成率 | 監控（無目標） |
| 治理保護觸發率 | 觸發失敗保護之人次 / 總人次 | 監控（無目標） |

### 年度公平性審查

每年度結束後須執行公平性審查，內容包含：

1. **統計分析**：多角色與單角色擔任者之分數分布比較
2. **MREM 分析**：MREM 啟動之案例分析，確認品質一致性
3. **異常檢視**：個案分析分數極端值
4. **係數適切性**：RLS、MREM 係數是否需調整

---

## 爭議處理

| 爭議類型 | 處理程序 |
|---------|---------|
| 角色配置係數爭議 | 依 6.3 客觀判定標準重新評估，由 Head of System Design 裁決 |
| 例外加分歸屬爭議 | 由審查委員會裁決 |
| 聚合公式適用爭議 | 由高階管理層裁決 |
| 治理保護觸發爭議 | 不得爭議（機制為強制性） |
| RLS 適用爭議 | 依角色數量客觀計算，不得爭議 |
| MREM 資格爭議 | 依八項條件客觀判定，不得主觀裁量 |

---

## 稽核紀錄要求

### 必要紀錄

| 紀錄項目 | 保存期限 |
|---------|---------|
| 各角色 KPI 原始數據 | 3 年 |
| 各角色例外加分申請與核准文件 | 3 年 |
| 角色配置係數判定紀錄（含各維度證據） | 3 年 |
| 聚合計算工作底稿 | 3 年 |
| 治理保護觸發紀錄 | 3 年 |
| RLS 計算紀錄 | 3 年 |
| MREM 資格判定紀錄 | 3 年 |
| 最終績效報告 | 永久 |

### 稽核查核點

| 查核點 | 查核內容 |
|-------|---------|
| 角色評估獨立性 | 確認各角色分數係獨立計算 |
| AF 判定客觀性 | 確認 AF 判定依循 6.3 客觀標準 |
| 聚合公式正確性 | 確認公式套用無誤 |
| 治理保護適用性 | 確認保護機制正確觸發 |
| RLS 計算正確性 | 確認 N 值與 RLS 係數正確 |
| MREM 資格判定正確性 | 確認八項條件皆經驗證 |
| MREM 不覆蓋失敗 | 確認觸發失敗保護時 MREM 未套用 |

---

## 附錄 A：快速參照表

### A.1 角色貢獻權重（RCW）

| 角色 | RCW | 備註 |
|-----|-----|------|
| Head of System Design | 1.00 | 固定 |
| System Design Governance Lead | 0.90 | 固定 |
| System Architect | 0.85 | 固定 |
| Security Engineering Role | 0.85 | 固定 |
| Design QA Role | 0.75 | 固定 |
| Pre-Gate Design Support | 0.75 / 0.50 | 條件式（驗證通過 0.75，否則 0.50） |
| Design Governance Coordinator | 0.60 | 固定 |

### A.2 配置係數（Allocation Factor）

| 配置狀態 | AF |
|---------|-----|
| 完全擔任 | 1.0 |
| 主要擔任 | 0.7 |
| 次要擔任 | 0.3 |
| 備援擔任 | 0.1 |

### A.3 Role Load Stabilizer (RLS)

| 有效角色數量 (N_effective) | RLS |
|--------------------------|-----|
| 1 | 1.00 |
| 2 | 1.02 |
| 3 | 1.04 |
| 4+ | 1.05 |

**公式**：`RLS = min(1 + 0.02 × (N_effective - 1), 1.05)`

**N_effective 判定**：僅通過 SPV 驗證（AF ≥ 0.5 或 Gate 簽核 ≥ 50%）之角色計入

### A.4 Multi-Role Excellence Multiplier (MREM)

| 角色數量 (N) | MREM（若啟動） |
|-------------|---------------|
| 1 | 不適用 |
| 2 | 1.03 |
| 3 | 1.06 |
| 4+ | 1.10 |

**公式**：`MREM = min(1 + 0.03 × (N - 1), 1.10)`

**啟動條件（全部須滿足）**：
- MREM-1: N_effective ≥ 2
- MREM-2: 每角色 Base Score ≥ 85
- MREM-3: 未觸發 Critical Role Failure Protection
- MREM-4: 無以例外加分彌補基本 KPI 失敗
- MREM-5: 每角色 AF ≥ 0.3
- MREM-6: Pre-Gate Design Support 不得為唯一額外角色
- MREM-7: 每角色須通過 SPV 驗證
- MREM-8: 依賴後驗之角色須後驗完成且 PVF ≥ 0.95

### A.5 完整計分公式

```
Step 1: Effective RCW = RCW × PVF
        （條件式 RCW 角色：先判定 RCW 再乘以 PVF）

Step 2: Individual Score (Raw) = Σ(Role Final Score × Effective RCW × AF) / Σ(Effective RCW × AF)

Step 3: Protected Score =
        If Critical Role Failure (not RAT exempted):
            min(Raw Score, min(Failing Role Base Score) + 10)
        Else:
            Raw Score

Step 4: N_effective = 通過 SPV 驗證之角色數

Step 5: RLS Score = min(Protected Score × RLS(N_effective), 100)

Step 6: Final Score =
        If MREM Qualified (含 MREM-7/MREM-8):
            min(RLS Score × MREM(N_effective), 100)
        Else:
            RLS Score
```

---

## 假設條件

1. **角色穩定性**：假設角色指派於評估週期內維持穩定；期中變更需特殊處理
2. **RCW 一致性**：假設 RCW 於評估週期內不變；調整須於週期開始前完成
3. **系統支援**：假設組織具備支援聚合計算之績效管理系統
4. **獨立評估**：假設各角色之 KPI 評估者具備獨立性
5. **係數穩定性**：假設 RLS、MREM 公式於評估週期內不變
6. **證據可及性**：假設 AF 判定所需之文件、RACI、Gate 紀錄皆可取得
7. **Pre-Gate Design Support 驗證可及性**：假設後續 Gate 紀錄可於追溯調整期限內取得
8. **SPV 驗證可及性**：假設 Gate 簽核紀錄可於評估週期內取得
9. **PVF 驗證可及性**：假設設計變更紀錄與殘餘風險清單可於驗證時點取得
10. **後驗時程對齊**：假設多數專案可於評估週期內完成至少 Gate 1，使後驗機制可適用

---

## 附錄 B：Pre-Gate Design Support 條件式 RCW 快速參照

### B.1 RCW 判定流程

```
Step 1: 確認專案進度
        - 已完成 Gate 3 → 進入 Step 2
        - 僅完成 Gate 1 → 進入 Step 2（PGDS-2 暫緩）
        - 未進入 Gate 0 → RCW = 0.50

Step 2: 驗證 PGDS-1（需求採用）
        - Gate 0 核准紀錄引用預釐清文件？
        - 是 → 繼續；否 → RCW = 0.50

Step 3: 驗證 PGDS-3（無返工）
        - 設計變更紀錄無「需求澄清不足」類別？
        - 是 → 繼續；否 → RCW = 0.50

Step 4: 驗證 PGDS-2（風險未重複）
        - 殘餘風險清單無預揭露風險重複識別？
        - 是 → RCW = 0.75；否 → RCW = 0.50
```

### B.2 MREM 計算調整

```
N_effective = N_total - N_PGDS

其中：
- N_total = 個人擔任之總角色數
- N_PGDS = 個人擔任之 Pre-Gate Design Support 角色數（通常為 0 或 1）
- N_effective = MREM 計算適用之有效角色數
```

### B.3 貢獻驗證時程

| 驗證項目 | 觸發事件 | 驗證期限 |
|---------|---------|---------|
| PGDS-1（需求採用） | Gate 0 核准 | Gate 0 核准後 15 日 |
| PGDS-3（無返工） | Gate 1 完成 | Gate 1 後 30 日 |
| PGDS-2（風險未重複） | Gate 3 完成 | Gate 3 後 30 日 |
| 追溯調整截止 | Gate 3 完成 | Gate 3 後 60 日 |

---

## 附錄 C：後驗修正因子 (PVF) 快速參照

### C.1 PVF 適用角色

| 角色 | 適用 PVF | 觸發條件數 |
|-----|---------|-----------|
| System Architect | 是 | 2 項 |
| Security Engineering Role | 是 | 2 項 |
| Pre-Gate Design Support | 否（條件式 RCW） | - |
| 其他角色 | 否 | - |

### C.2 PVF 值對照

| 觸發條件數 | PVF 值 | Effective RCW 影響 |
|-----------|-------|-------------------|
| 0 | 1.00 | 無折減 |
| 1 | 0.95 | 折減 5% |
| 2+ | 0.90 | 折減 10% |

### C.3 PVF 驗證時程

| 條件 | 適用角色 | 驗證時點 |
|-----|---------|---------|
| PVF-SA-1（設計基線錯誤） | System Architect | Gate 1 後 30 日 |
| PVF-SA-2（技術可行性誤判） | System Architect | Gate 3 完成後 |
| PVF-SE-1（威脅情境遺漏） | Security Engineering Role | Gate 3 完成後 |
| PVF-SE-2（SL 非計畫性變更） | Security Engineering Role | Gate 2 後 |

---

## 附錄 D：實質參與驗證 (SPV) 快速參照

### D.1 SPV 驗證條件

```
SPV 通過 = (AF ≥ 0.5) OR (Gate 簽核參與率 ≥ 50%)
```

### D.2 SPV 對激勵機制之影響

| 項目 | SPV 通過 | SPV 未通過 |
|-----|---------|-----------|
| 分數聚合 | 納入 | 納入 |
| N_effective 計算 | 計入 | 不計入 |
| RLS 適用 | 依 N_effective | 依 N_effective |
| MREM 適用 | 依 N_effective 且須 MREM-7 | 不適用 |

### D.3 連續未通過 SPV 處理

| 連續週期數 | 處理方式 |
|-----------|---------|
| 1 | 記錄，無額外動作 |
| 2 | 須重新評估角色指派 |
| 3+ | 建議移除角色指派 |

---

## 附錄 E：最終校驗問題

### E.1 制度公平性校驗

本模型設計須通過以下校驗問題：

| 問題 | 預期答案 | 機制保障 |
|-----|---------|---------|
| 若該角色明年換人，此制度仍然公平嗎？ | 是 | 所有計分規則皆為規則式、可重現 |
| 若該角色做得不好，制度是否會自動壓縮其回饋？ | 是 | Critical Role Failure Protection、PVF 折減 |
| 若該角色做得非常好，制度是否能合理放大其價值？ | 是 | MREM（條件嚴格）、例外加分（有上限） |

### E.2 濫用風險校驗

| 潛在濫用 | 防範機制 |
|---------|---------|
| 策略性承擔多角色以觸發 MREM | SPV 驗證、MREM-7 條件 |
| 掛名但未實際參與 | SPV 驗證、AF 客觀判定 |
| 後驗失敗仍獲高分 | 條件式 RCW、PVF 折減 |
| 例外加分彌補基本缺失 | MREM-4、例外加分不救基本分 |

---

*文件結束*
