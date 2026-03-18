# Wave 2 Subdomain Aggregation Plan

## 統計

- Wave 1 已覆蓋 SK: 19
- Wave 2 待轉換 SK: 152
- 預計產出 SKILL.md: 47
- 總計: 171 SK 定義

## 聚合映射表

| # | 目標 SKILL.md name | 中文名 | 來源 SK 列表 | SK 數量 | Domain |
|---|-------------------|-------|-------------|--------|--------|
| 1 | security-perimeter-design | 安全邊界設計 | SK-D01-003, SK-D01-004 | 2 | D01 |
| 2 | threat-risk-assessment | 威脅與風險評估 | SK-D01-005, SK-D01-006, SK-D01-007, SK-D01-008, SK-D01-009, SK-D01-035, SK-D01-036 | 7 | D01 |
| 3 | security-level-assessment | 安全等級評估 | SK-D01-010 | 1 | D01 |
| 4 | security-monitoring-incident-response | 安全監控與事件回應 | SK-D01-014, SK-D01-015, SK-D01-016, SK-D01-017, SK-D01-018, SK-D01-032 | 6 | D01 |
| 5 | security-system-hardening | 系統安全加固 | SK-D01-019, SK-D01-020, SK-D01-021, SK-D01-022, SK-D01-023, SK-D01-028 | 6 | D01 |
| 6 | security-policies-governance | 安全政策與治理 | SK-D01-030, SK-D01-033, SK-D01-034 | 3 | D01 |
| 7 | supply-chain-security | 供應鏈安全管理 | SK-D01-024, SK-D01-025, SK-D01-026, SK-D01-031 | 4 | D01 |
| 8 | sis-security-control | 安全儀控系統實施 | SK-D01-027 | 1 | D01 |
| 9 | network-architecture-design | 網路架構設計 | SK-D02-002, SK-D02-006, SK-D02-007 | 3 | D02 |
| 10 | icd-interface-design | 介面控制文件與通訊協定 | SK-D02-003, SK-D02-005 | 2 | D02 |
| 11 | edge-computing-architecture | 邊緣計算與架構決策 | SK-D02-008, SK-D02-009, SK-D02-010, SK-D02-012 | 4 | D02 |
| 12 | power-system-base-analysis | 電力系統基礎分析 | SK-D03-001, SK-D03-002, SK-D03-003 | 3 | D03 |
| 13 | renewable-energy-integration | 可再生能源併網 | SK-D03-004, SK-D03-005, SK-D03-006, SK-D03-007 | 4 | D03 |
| 14 | advanced-power-analysis | 進階電力分析與模擬 | SK-D03-008, SK-D03-009, SK-D03-010 | 3 | D03 |
| 15 | protection-coordination | 保護協調與整定 | SK-D04-001, SK-D04-002, SK-D04-003, SK-D04-006 | 4 | D04 |
| 16 | protection-logic-documentation | 保護邏輯與故障分析 | SK-D04-004, SK-D04-005 | 2 | D04 |
| 17 | scada-foundation | SCADA 基礎構建 | SK-D05-001, SK-D05-002 | 2 | D05 |
| 18 | control-strategy-configuration | 控制策略與配置 | SK-D05-003, SK-D05-004, SK-D05-012, SK-D05-013, SK-D05-014 | 5 | D05 |
| 19 | hmi-alarm-design | 人機介面與告警設計 | SK-D05-005, SK-D05-006 | 2 | D05 |
| 20 | plc-programming | PLC 程式開發 | SK-D05-007, SK-D05-008 | 2 | D05 |
| 21 | industrial-protocols | 工業通訊協議配置 | SK-D05-009, SK-D05-010, SK-D05-011 | 3 | D05 |
| 22 | electrical-mechanical-design | 電氣機械設計 | SK-D06-001, SK-D06-002, SK-D06-003, SK-D06-005 | 4 | D06 |
| 23 | cad-documentation | CAD 與元件規範 | SK-D06-004, SK-D06-006 | 2 | D06 |
| 24 | integration-planning | 整合規劃與架構 | SK-D07-001, SK-D07-002 | 2 | D07 |
| 25 | protocol-data-conversion | 協議與資料轉換 | SK-D07-003, SK-D07-004, SK-D07-005, SK-D07-006 | 4 | D07 |
| 26 | api-integration | API 與第三方集成 | SK-D07-007 | 1 | D07 |
| 27 | factory-acceptance-testing | 工廠驗收測試 | SK-D08-001, SK-D08-002 | 2 | D08 |
| 28 | site-acceptance-testing | 現場驗收測試 | SK-D08-003, SK-D08-004, SK-D08-005, SK-D08-013 | 4 | D08 |
| 29 | security-testing | 安全性與性能測試 | SK-D08-007, SK-D08-008, SK-D08-009, SK-D08-010, SK-D08-014 | 5 | D08 |
| 30 | commissioning-defect-management | 試運行與缺陷管理 | SK-D08-006, SK-D08-011 | 2 | D08 |
| 31 | design-documentation | 設計文件撰寫 | SK-D09-001, SK-D09-002, SK-D09-003, SK-D09-009 | 4 | D09 |
| 32 | document-management | 文件與版本管理 | SK-D09-004, SK-D09-005 | 2 | D09 |
| 33 | operational-training-materials | 操作與培訓教材 | SK-D09-006, SK-D09-008 | 2 | D09 |
| 34 | requirements-traceability | 需求與變更管理 | SK-D10-001, SK-D10-002, SK-D10-003, SK-D10-007 | 4 | D10 |
| 35 | project-coordination | 專案協調與追蹤 | SK-D10-004, SK-D10-005 | 2 | D10 |
| 36 | system-decommissioning | 系統除役管理 | SK-D10-006 | 1 | D10 |
| 37 | design-review-governance | 設計審查與治理 | SK-D11-001, SK-D11-003, SK-D11-017, SK-D11-018, SK-D11-020 | 5 | D11 |
| 38 | process-development | 流程開發與優化 | SK-D11-004, SK-D11-005, SK-D11-015, SK-D11-016, SK-D11-019 | 5 | D11 |
| 39 | quality-assurance | 品質保證與管理 | SK-D11-006, SK-D11-007, SK-D11-013 | 3 | D11 |
| 40 | knowledge-management | 知識與能力管理 | SK-D11-008, SK-D11-009, SK-D11-010, SK-D11-011, SK-D11-012, SK-D11-014, SK-D11-021 | 7 | D11 |
| 41 | data-infrastructure | 資料採集與基礎設施 | SK-D12-001, SK-D12-002, SK-D12-003, SK-D12-004 | 4 | D12 |
| 42 | data-analysis-insights | 資料分析與應用 | SK-D12-005, SK-D12-006, SK-D12-007, SK-D12-008 | 4 | D12 |
| 43 | automation-tooling | 自動化工具開發 | SK-D13-001, SK-D13-002, SK-D13-005 | 3 | D13 |
| 44 | ai-workflow-automation | AI 與工作流自動化 | SK-D13-003, SK-D13-004, SK-D13-006 | 3 | D13 |
| 45 | site-assessment | 現場評估與基礎設施 | SK-D14-011, SK-D14-012, SK-D14-017 | 3 | D14 |
| 46 | concept-development | 概念設計與初步評估 | SK-D14-013, SK-D14-014, SK-D14-018 | 3 | D14 |
| 47 | gate0-decision-package | Gate 0 決策與成本分析 | SK-D14-015, SK-D14-016 | 2 | D14 |

## 按 Domain 分布

| Domain | SKILL.md 數 | SK 數 | 平均 SK/SKILL.md |
|--------|-----------|-------|-----------------|
| D01 | 8 | 30 | 3.8 |
| D02 | 3 | 9 | 3.0 |
| D03 | 3 | 10 | 3.3 |
| D04 | 2 | 6 | 3.0 |
| D05 | 5 | 14 | 2.8 |
| D06 | 2 | 6 | 3.0 |
| D07 | 3 | 7 | 2.3 |
| D08 | 4 | 13 | 3.2 |
| D09 | 3 | 8 | 2.7 |
| D10 | 3 | 7 | 2.3 |
| D11 | 4 | 20 | 5.0 |
| D12 | 2 | 8 | 4.0 |
| D13 | 2 | 6 | 3.0 |
| D14 | 3 | 8 | 2.7 |
| **Total** | **47** | **152** | **3.2** |

## 聚合策略說明

### Domain D01 - 安全設計與實施
- **security-perimeter-design**: 防火牆規則和網路分段，形成安全邊界
- **threat-risk-assessment**: 威脅與風險評估工作流，包括資產清冊、STRIDE建模、風險矩陣、IEC/FMEA/HAZOP
- **security-level-assessment**: 獨立的安全等級評估
- **security-monitoring-incident-response**: SIEM、告警、事件回應、鑑識和威脅情報
- **security-system-hardening**: 端點、帳號、補丁、備份、惡意程式防護、遠端存取配置
- **security-policies-governance**: 安全政策、資料分類、解決方案整合
- **supply-chain-security**: 供應商評估、SBOM、第三方驗證、供應商安全管理
- **sis-security-control**: 安全儀控系統控制實施

### Domain D02 - 系統架構
- **network-architecture-design**: 網路冗餘、HA架構、RTO/RPO規劃
- **icd-interface-design**: 介面控制文件和工業協定架構
- **edge-computing-architecture**: 邊緣計算、架構決策記錄、技術選型、架構審查

### Domain D03 - 電力系統分析
- **power-system-base-analysis**: 基礎電力流、短路電流、電壓穩定分析
- **renewable-energy-integration**: 光伏併網、電池儲能、虛擬電廠、DER聚合
- **advanced-power-analysis**: 諧波分析、暫態穩定度、系統建模

### Domain D04 - 保護與繼電器
- **protection-coordination**: 過電流協調、距離保護、繼電器選型、測試
- **protection-logic-documentation**: 保護邏輯圖和故障錄波分析

### Domain D05 - 控制系統
- **scada-foundation**: SCADA點位清單、資料庫結構
- **control-strategy-configuration**: EMS AGC、DERMS、PID調參、負載管理、頻率調節
- **hmi-alarm-design**: HMI畫面、告警層級設計
- **plc-programming**: PLC階梯圖和結構化文字編程
- **industrial-protocols**: Modbus、IEC 61850、OPC UA配置

### Domain D06 - 電氣設計
- **electrical-mechanical-design**: 盤面佈局、配線圖、端子排、線徑計算
- **cad-documentation**: CAD施工圖、元件選型規範

### Domain D07 - 系統整合
- **integration-planning**: 介面整合矩陣、整合架構圖
- **protocol-data-conversion**: 協議閘道、資料格式轉換、資料模型對齐、時間戳同步
- **api-integration**: 第三方API串接

### Domain D08 - 測試與試運行
- **factory-acceptance-testing**: FAT程序和安全FAT
- **site-acceptance-testing**: SAT程序、現場驗收、安全驗收、SIT
- **security-testing**: 性能基線、應用安全測試、滲透測試、漏洞掃描、安全檢驗
- **commissioning-defect-management**: 試運行計劃、缺陷報告

### Domain D09 - 文件
- **design-documentation**: 系統設計說明、安全功能規範、單線圖、加固建議
- **document-management**: 文件交付清單、版本控制
- **operational-training-materials**: 操作手冊、培訓教材

### Domain D10 - 專案管理
- **requirements-traceability**: 需求追溯、變更申請、MOC、工作許可
- **project-coordination**: 技術澄清會、合同範圍追蹤
- **system-decommissioning**: 系統除役

### Domain D11 - 流程治理與品質
- **design-review-governance**: 設計審查、安全審查、階段審查、品質驗證、SL重認證
- **process-development**: SOP開發、流程效率、採購安全需求、專案安全管理、標準歸屬
- **quality-assurance**: 品質計劃、不合格項、資訊資產分類
- **knowledge-management**: 經驗學習、知識庫、設計標準維護、工程能力框架、培訓計劃、人員資格、KPI評分

### Domain D12 - 資料管理
- **data-infrastructure**: 資料採集架構、協定解析器、時序DB、資料保留
- **data-analysis-insights**: 負載預測、監控儀表板、資料字典、資料存取政策

### Domain D13 - 自動化與AI
- **automation-tooling**: 自動化計算腳本、文件產生器、測試流程
- **ai-workflow-automation**: AI輔助設計審查、自動化技能調用、工作流自動化

### Domain D14 - 售前與Gate 0
- **site-assessment**: 現場勘查、基礎設施清冊、NDA管理
- **concept-development**: 概念Zone/Conduit架構、初步安全分類、需求釐清
- **gate0-decision-package**: Gate 0決策包、成本風險分析

## 設計原則

1. **功能聚合優於形式聚合**: 按照執行主題和工作流程分組，而不僅僅是按domain分組
2. **均衡規模**: 每個SKILL.md包含2-8個SK定義，便於管理和執行
3. **可執行性**: 每個SKILL.md代表一個可獨立執行的工程任務或流程
4. **追溯性**: 保持清晰的SK-to-SKILL映射，支持反向追蹤
5. **跨域協作**: 允許跨domain分組（如D01.4的告警與D05.5的協議配置可在同一整合流程中使用）

## 實施注意事項

### 規模分布
- 最小: 1 SK (API整合、安全等級評估、SIS安全控制、系統除役)
- 最大: 7 SK (威脅風險評估、知識與能力管理)
- 中位數: 3 SK
- 平均: 3.2 SK/SKILL.md

### 域內平衡
- **D11** (流程治理): 4 SKILL.md覆蓋20個SK，單個SKILL可達7個SK
- **D01** (安全): 8 SKILL.md覆蓋30個SK，細粒度分布
- **其他域**: 均衡分布，2-5個SKILL.md

### 執行順序建議
1. **基礎層** (D02, D03, D04, D06): 架構和硬體設計
2. **實現層** (D05, D07, D12): 控制、整合、資料
3. **驗證層** (D08, D09): 測試和文件
4. **治理層** (D01, D10, D11): 安全、項目、流程
5. **高級層** (D13, D14): 自動化和售前

### 相關性提示
- D01安全設計與D05控制配置、D08測試密切相關
- D02架構設計與D07整合配置相關
- D03電力分析與D04保護協調相依賴
- D11流程治理與所有技術域都相關
- D13自動化可加速D09文件和D08測試流程
