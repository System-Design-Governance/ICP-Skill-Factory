```{=latex}
\newpage
```

# Appendix C: Residual Risk Template

## Purpose {#appC-purpose}

本附錄提供殘餘風險評估與記錄的標準化模板，確保所有已識別風險都經過適當評估與接受流程。本模板用於 Gate 3 設計交付時之殘餘風險清單編製，並作為 IEC 62443 合規稽核之證據文件。

---

## Risk Assessment Process {#appC-process}

### 風險分析輸入來源 {#appC-input-sources}

本治理框架之殘餘風險，必須源自以下經核可之風險分析方法：

| 分析方法 | 識別範圍 | Risk Source ID 格式 |
|---------|---------|-------------------|
| **IEC 62443-3-2** | 資安威脅、Zone/Conduit 邊界風險 | T-XXX |
| **FMEA** | 系統/元件失效模式 | FM-XXX |
| **HAZOP** | 操作流程偏差 | HAZ-XXX |
| **Threat Modeling（如 STRIDE）** | 設計層級資安威脅 | TM-XXX |

**重要說明**：
- 每筆殘餘風險必須標註其 Risk Source ID，以利追溯至原始分析文件
- 無法追溯至上述來源之風險項目，視為風險紀錄不成立，Gate 3 不得放行
- 各分析方法之執行步驟、模板與評分規範，請參閱 **Appendix D: Integrated Risk Assessment Templates**

### 評估流程 {#appC-assessment-flow}

1. **識別威脅** (Threat Identification)：依上述分析方法產出
2. **評估固有風險** (Inherent Risk Assessment)
3. **定義控制措施** (Control Measures)
4. **計算殘餘風險** (Residual Risk Calculation)
5. **風險接受決策** (Risk Acceptance Decision)

---

## Residual Risk Register Template {#appC-register-template}

### Risk ID: [RR-001]

#### Basic Information

| 欄位 | 內容 |
|------|------|
| **Risk Title** | [簡短描述風險] |
| **Risk Source ID** | [T-XXX / FM-XXX / HAZ-XXX / TM-XXX] |
| **Analysis Method** | [IEC 62443-3-2 / FMEA / HAZOP / Threat Modeling] |
| **Risk Owner** | [負責人] |
| **Date Identified** | [YYYY-MM-DD] |
| **Last Updated** | [YYYY-MM-DD] |

#### Threat Description

[詳細描述威脅情境，包括攻擊向量、失效模式、操作偏差等，視 Analysis Method 而定]

#### Inherent Risk Assessment

| Factor | Rating | Justification |
|--------|--------|---------------|
| Likelihood | High / Medium / Low | [說明發生可能性的理由] |
| Impact | High / Medium / Low | [說明影響程度的理由] |
| **Inherent Risk Level** | **Critical / High / Medium / Low** | [綜合評估結果] |

#### Implemented Controls

1. **Control 1**: [控制措施描述]
   - Type: Preventive / Detective / Corrective
   - Effectiveness: High / Medium / Low

2. **Control 2**: [控制措施描述]
   - Type: Preventive / Detective / Corrective
   - Effectiveness: High / Medium / Low

#### Residual Risk Assessment

| Factor | Rating | Justification |
|--------|--------|---------------|
| Likelihood (after controls) | High / Medium / Low | [套用控制措施後的可能性] |
| Impact (after controls) | High / Medium / Low | [套用控制措施後的影響] |
| **Residual Risk Level** | **Critical / High / Medium / Low** | [最終殘餘風險等級] |

#### Risk Treatment Decision

- [ ] Accept: 接受殘餘風險
- [ ] Mitigate: 需額外緩解措施
- [ ] Transfer: 轉移風險（如保險）
- [ ] Avoid: 避免風險（變更設計）

**Decision Rationale**: [決策理由說明]

#### Acceptance Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Risk Owner | | | |
| Security Lead | | | |
| Project Manager | | | |
| Business Owner | | | |

---

## Risk Matrix {#appC-risk-matrix}

### Likelihood Scale {#appC-likelihood-scale}

- **High**: 預期會發生（機率 > 50%）
- **Medium**: 有可能發生（機率 10-50%）
- **Low**: 不太可能發生（機率 < 10%）

### Impact Scale {#appC-impact-scale}

- **High**: 嚴重影響系統可用性、資料完整性或機密性
- **Medium**: 中度影響，可透過備援或人工介入恢復
- **Low**: 輕微影響，不影響核心功能

### Risk Level Matrix {#appC-level-matrix}

|            | **Low Impact** | **Medium Impact** | **High Impact** |
|------------|----------------|-------------------|-----------------|
| **High Likelihood** | Medium | High | Critical |
| **Medium Likelihood** | Low | Medium | High |
| **Low Likelihood** | Low | Low | Medium |

---

## Risk Acceptance Criteria {#appC-acceptance-criteria}

依主文件 5.2 節規定：

| Risk Level | 接受權限 |
|------------|---------|
| **Low** | Project Manager |
| **Medium** | Project Manager + Security Lead |
| **High** | Project Manager + Security Lead + Business Owner |
| **Critical** | Engineering Management，並制定額外緩解計畫 |

---

## Example: Sample Risk Entry {#appC-example}

### Risk ID: RR-001

#### Basic Information

| 欄位 | 內容 |
|------|------|
| **Risk Title** | 未加密的內部 API 通訊 |
| **Risk Source ID** | T-012 |
| **Analysis Method** | IEC 62443-3-2 |
| **Risk Owner** | System Architect |
| **Date Identified** | 2026-01-08 |
| **Last Updated** | 2026-01-08 |

#### Threat Description

內部微服務間的 API 通訊未加密，若內網遭入侵，攻擊者可攔截敏感資料（如使用者認證 token）。此威脅於 IEC 62443-3-2 威脅情境分析中識別（Threat Scenario T-012）。

#### Inherent Risk Assessment

| Factor | Rating | Justification |
|--------|--------|---------------|
| Likelihood | Medium | 內網隔離但無法完全排除入侵風險 |
| Impact | High | 可能導致認證繞過與資料外洩 |
| **Inherent Risk Level** | **High** | 中等可能性 × 高影響 |

#### Implemented Controls

1. **Control 1**: 內網隔離與防火牆規則
   - Type: Preventive
   - Effectiveness: Medium

2. **Control 2**: API Gateway 層進行認證檢查
   - Type: Detective
   - Effectiveness: Medium

#### Residual Risk Assessment

| Factor | Rating | Justification |
|--------|--------|---------------|
| Likelihood (after controls) | Low | 內網隔離降低入侵可能性 |
| Impact (after controls) | Medium | API Gateway 可限制影響範圍 |
| **Residual Risk Level** | **Low** | 低可能性 × 中等影響 |

#### Risk Treatment Decision

- [x] Accept: 接受殘餘風險

**Decision Rationale**: 考量效能需求與內網已有隔離措施，接受此殘餘風險。未來若風險等級提升，將評估導入 mTLS。

---

## Document Control {#appC-doc-control}

- **Version**: 1.0
- **Effective Date**: 2026-01-08
- **Owner**: System Design Governance Function
- **Review Cycle**: 與主文件同步

本附錄之修訂依主文件 6.2 節流程辦理。

---

**文件結束**
