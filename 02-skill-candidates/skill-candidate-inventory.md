# ICP Skill Factory — Skill Candidate Inventory (Phase 2)

**Version:** R5 (2026-03-13)
**Total Candidates:** 173 pre-normalization / 171 post-normalization
**Domains Covered:** 14 (D01–D14)
**Source:** Extracted from ID01–ID14, ID21–ID25, GOV-SD, GOV-SDP, and practical engineering knowledge (PRAC)

### Legend

- **Source**: ID01–ID14 = document source (Tier 2 exemplar); ID21–ID25 = org procedures (Tier 3 contextual); GOV-SD/GOV-SDP = governance framework (Tier 1 authoritative); PRAC = practical engineering knowledge
- **Confidence**: H = High (directly stated in source), H+ = High with deliverable exemplar + governance confirmation, M = Medium (strongly implied), L = Low (inferred from context)
- **Type**: ANA=Analysis, DES=Design, ENG=Engineering, TST=Testing, DOC=Documentation, MGT=Management, VER=Verification, GOV=Governance, INT=Integration, OPS=Operations
- **R5 markers**: ▲ = new in R5 from governance (Tier 1); △ = new in R5 from exemplars (Tier 2/3)

---

### D01 — OT Cybersecurity (36 candidates; +8 in R5)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D01-001 | Zone/Conduit Architecture Design | Zone/Conduit 架構設計 | D01.1 | DES | R1,R2 | ID01 §7.4.1.2; ID02 A.9 §10.2 | H |
| SC-D01-002 | Defense-in-Depth Strategy Design | 縱深防禦策略設計 | D01.1 | DES | R1,R2 | ID01 §6.5.1.3; ID02 A.9 §2 | H |
| SC-D01-003 | Firewall Rule Planning | 防火牆規則規劃 | D01.1 | ENG | R2,R3 | ID02 A.9 §10.1 | H |
| SC-D01-004 | Network Segmentation Documentation | 網路分段文件 | D01.1 | DOC | R2,R3 | ID01 §7.4.1.2; ID02 C.3 | H |
| SC-D01-005 | Asset Inventory Development | 資產清冊建立 | D01.2 | ANA | R0,R1 | ID01 §7.2.1; ID02 A.6; ID02 C.4 | H |
| SC-D01-006 | Threat and Risk Assessment (Preliminary) | 初步威脅風險評估 | D01.2 | ANA | R1 | ID01 §7.2; ID02 A.8 | H |
| SC-D01-007 | Detailed Risk Assessment | 詳細風險評估 | D01.2 | ANA | R2 | ID01 §7.3; ID03 §5.6.4 | H |
| SC-D01-008 | STRIDE/DREAD Threat Modeling | STRIDE/DREAD 威脅建模 | D01.2 | ANA | R1,R2 | ID01 §5.0 ref[32]; PRAC | M |
| SC-D01-009 | Risk Classification Matrix Development | 風險分類矩陣建立 | D01.2 | ANA | R1 | ID03 §5.4.1 | H |
| SC-D01-010 | Security Level Target (SL-T) Assessment | 安全等級目標評估 | D01.3 | ANA | R1 | ID01 §6.5.1.2; ID03 §5.4.2 | H |
| SC-D01-011 | IEC 62443 Compliance Gap Analysis | IEC 62443 合規差距分析 | D01.3 | ANA | R1,R4 | ID01 §6.6.3; ID02 C.1-C.8 | H |
| SC-D01-012 | Security Audit Execution | 安全稽核執行 | D01.3 | VER | R4 | ID01 §7.8.3.1 | H |
| SC-D01-013 | Gate Review Preparation and Execution | 閘門審查準備與執行 | D01.3 | GOV | R0-R5 | ID01 §6.5.1.1.3, §6.5.1.2.4 | H |
| SC-D01-014 | SIEM Configuration and Tuning | SIEM 配置與調校 | D01.4 | ENG | R3,R4 | ID01 §7.8.4.2; ID02 A.4 §9 | H |
| SC-D01-015 | Security Alarm Rule Design | 安全告警規則設計 | D01.4 | DES | R3 | ID01 §7.8.4.1 | H |
| SC-D01-016 | Incident Response Procedure Development | 事件回應程序撰寫 | D01.4 | DOC | R3,R4 | ID01 §7.8.5; ID03 §5.5.2 | H |
| SC-D01-017 | Security Incident Investigation and Forensics | 安全事件調查與鑑識 | D01.4 | ANA | R4 | ID01 §6.5.2.5 | M |
| SC-D01-018 | Continuous Security Monitoring | 持續安全監控 | D01.4 | OPS | R4 | ID01 §6.5.2.6; §7.8.4.2 | H |
| SC-D01-019 | Endpoint Hardening Implementation | 端點安全加固實施 | D01.5 | ENG | R3 | ID01 §7.4.1.5; ID02 A.10 | H |
| SC-D01-020 | Account and Access Control Management | 帳號與存取控制管理 | D01.5 | ENG | R3,R4 | ID01 §7.4.1.3; ID02 A.4 §4 | H |
| SC-D01-021 | Security Patch Management | 安全補丁管理 | D01.5 | OPS | R3,R4 | ID01 §7.4.1.11; ID02 A.4 §8.5 | H |
| SC-D01-022 | Backup and Restore Procedure Design | 備份與還原程序設計 | D01.5 | DES | R3 | ID01 §7.4.1.12; ID02 A.4 §6 | H |
| SC-D01-023 | Malware Protection Implementation | 惡意程式防護實施 | D01.5 | ENG | R3 | ID01 §7.4.1.10; ID02 A.4 §7 | H |
| SC-D01-024 | Vendor Security Risk Assessment | 供應商安全風險評估 | D01.6 | ANA | R0,R1 | ID01 §7.1.1.2; ID02 A.2 | H |
| SC-D01-025 | SBOM Analysis and Management | SBOM 分析與管理 | D01.6 | ANA | R3,R4 | ID03 §5.3.1; PRAC | M |
| SC-D01-026 | Third-Party Component Security Verification | 第三方元件安全驗證 | D01.6 | VER | R2,R3 | ID01 §6.4; ID02 B.3 | M |
| SC-D01-027 | SIS Security Control Implementation | SIS 安全控制實施 | D01.7★ | ENG | R2,R3 | ID01 §7.4.1.7; ID02 A.9 §12 | H |
| SC-D01-028 | Remote Access Security Configuration | 遠端存取安全配置 | D01.5 | ENG | R3 | ID01 §7.4.1.8; ID02 A.9 §9 | H |
| SC-D01-029 △ | Security Management Plan Development | 安全管理計畫撰寫 | D01.3 | DOC | R0,R1 | ID04 (Tier 2 format example) | H |
| SC-D01-030 △ | Security Policies and Procedures Plan Development | 安全政策與程序計畫撰寫 | D01.5 | DOC | R1,R2 | ID07 (Tier 2); ID01 §7.1.1.4 | H |
| SC-D01-031 △ | Vendor Security Management Plan Development | 供應商安全管理計畫撰寫 | D01.6 | DOC | R0,R1 | ID05 (Tier 2); ID01 §7.1.1.2 | H |
| SC-D01-032 △ | Threat Intelligence Collection and Analysis | 威脅情資蒐集與分析 | D01.4 | ANA | R4 | ID24 §5.3–5.4 (Tier 3) | H |
| SC-D01-033 △ | Data Classification Policy Development | 資料分類政策制定 | D01.5 | GOV | R1 | ID23 (Tier 3); GOV-SD BOUNDARY-008 | H |
| SC-D01-034 △ | Security Solution Integration Plan Development | 安全解決方案整合計畫撰寫 | D01.5 | DOC | R3 | ID04 §5.0 (Tier 2) | M |
| SC-D01-035 ▲ | Integrated Risk Assessment Execution (IEC+FMEA+HAZOP) | 整合風險評估執行 | D01.2 | ANA | R1,R2 | GOV-SD (triple-method mandatory) | H |
| SC-D01-036 ▲ | Risk Source Traceability & Residual Risk Register | 風險溯源與殘餘風險登錄 | D01.2 | ANA | R1–R3 | GOV-SD (T-XXX/FM-XXX/HAZ-XXX; Gate 3 20% sampling) | H |

---

### D02 — System Architecture (12 candidates)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D02-001 | OT Network Topology Design | OT 網路拓撲設計 | D02.1 | DES | R1,R2 | ID02 A.7; ID01 §7.4.1.2 | H |
| SC-D02-002 | Network Redundancy Design (RSTP/Ring) | 網路冗餘設計 | D02.1 | DES | R2 | PRAC | M |
| SC-D02-003 | Interface Control Document (ICD) Development | 介面控制文件撰寫 | D02.2 | DOC | R2 | PRAC | M |
| SC-D02-004 | Data Flow Diagram Development | 資料流圖繪製 | D02.2 | DOC | R1,R2 | ID02 A.5; ID01 §7.2.1 | H |
| SC-D02-005 | Industrial Protocol Architecture Design | 工業協定架構設計 | D02.3 | DES | R1,R2 | PRAC | M |
| SC-D02-006 | High-Availability Architecture Design | 高可用架構設計 | D02.4 | DES | R2 | PRAC | M |
| SC-D02-007 | RTO/RPO Planning | RTO/RPO 規劃 | D02.4 | DES | R2 | PRAC | M |
| SC-D02-008 | Edge Computing Deployment Design | 邊緣計算部署設計 | D02.5 | DES | R2 | PRAC | L |
| SC-D02-009 | Architecture Decision Record (ADR) Writing | 架構決策記錄撰寫 | D02.6 | DOC | R1,R2 | PRAC | M |
| SC-D02-010 | Technology Selection Evaluation | 技術選型評估 | D02.6 | ANA | R0,R1 | PRAC | M |
| SC-D02-011 | Simple Network Diagram Development | 簡易網路圖繪製 | D02.1 | DOC | R1 | ID02 A.7; ID03 Table 2 Doc 1.05 | H |
| SC-D02-012 | Architecture Review Facilitation | 架構審查主持 | D02.6 | GOV | R2 | ID01 §7.3.2 | H |

---

### D03 — Power System Engineering (10 candidates)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D03-001 | Power Flow Analysis | 潮流分析 | D03.1 | ANA | R1,R2 | PRAC | H |
| SC-D03-002 | Short Circuit Current Analysis | 短路電流分析 | D03.1 | ANA | R1,R2 | PRAC | H |
| SC-D03-003 | Voltage Stability Assessment | 電壓穩定度評估 | D03.1 | ANA | R2 | PRAC | M |
| SC-D03-004 | PV System Grid Integration Design | PV 系統併網設計 | D03.2 | DES | R1,R2 | PRAC | M |
| SC-D03-005 | BESS Capacity Planning | BESS 容量規劃 | D03.3 | DES | R1,R2 | PRAC | M |
| SC-D03-006 | VPP Dispatch Algorithm Design | VPP 調度演算法設計 | D03.4 | DES | R2 | PRAC | M |
| SC-D03-007 | DER Aggregation Strategy Design | DER 聚合策略設計 | D03.4 | DES | R1,R2 | PRAC | M |
| SC-D03-008 | Harmonic Analysis and Filter Design | 諧波分析與濾波器設計 | D03.5 | ANA | R2 | PRAC | M |
| SC-D03-009 | Transient Stability Simulation | 暫態穩定度模擬 | D03.6 | ANA | R2 | PRAC | M |
| SC-D03-010 | Power System Modeling (ETAP/PSS/E) | 電力系統建模 | D03.6 | ENG | R2 | PRAC | M |

---

### D04 — Protection Engineering (6 candidates)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D04-001 | Overcurrent Protection Coordination | 過電流保護協調 | D04.1 | DES | R2 | PRAC | H |
| SC-D04-002 | Distance Protection Setting Calculation | 距離保護整定計算 | D04.1 | ANA | R2 | PRAC | M |
| SC-D04-003 | Relay Selection and Parameter Setting | 繼電器選型與參數設定 | D04.2 | ENG | R2,R3 | PRAC | H |
| SC-D04-004 | Protection Logic Diagram Development | 保護邏輯圖繪製 | D04.3 | DES | R2 | PRAC | M |
| SC-D04-005 | Fault Recording Analysis | 故障錄波分析 | D04.4 | ANA | R4 | PRAC | M |
| SC-D04-006 | Protection Relay Testing | 保護繼電器測試 | D04.2 | TST | R3 | PRAC | H |

---

### D05 — Control System Engineering (14 candidates)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D05-001 | SCADA Point List Development | SCADA 點位清單建立 | D05.1 | ENG | R2 | PRAC | H |
| SC-D05-002 | SCADA Database Structure Design | SCADA 資料庫結構設計 | D05.1 | DES | R2 | PRAC | H |
| SC-D05-003 | EMS AGC Configuration | EMS AGC 配置 | D05.2 | ENG | R2,R3 | PRAC | M |
| SC-D05-004 | DERMS DER Management Strategy Setting | DERMS DER 管理策略設定 | D05.2 | ENG | R2,R3 | PRAC | M |
| SC-D05-005 | HMI Screen Design | HMI 畫面設計 | D05.3 | DES | R2,R3 | PRAC | H |
| SC-D05-006 | Alarm Hierarchy and Configuration Design | 告警層級配置設計 | D05.3 | DES | R2,R3 | PRAC | H |
| SC-D05-007 | PLC Ladder Logic Programming | PLC 階梯圖程式撰寫 | D05.4 | ENG | R2,R3 | PRAC | H |
| SC-D05-008 | Structured Text Programming | 結構化文字程式開發 | D05.4 | ENG | R2,R3 | PRAC | M |
| SC-D05-009 | Modbus Mapping Configuration | Modbus 映射配置 | D05.5 | ENG | R3 | PRAC | H |
| SC-D05-010 | IEC 61850 SCL Configuration | IEC 61850 SCL 配置 | D05.5 | ENG | R3 | PRAC | M |
| SC-D05-011 | OPC UA Server/Client Configuration | OPC UA 伺服器/客戶端配置 | D05.5 | ENG | R3 | PRAC | M |
| SC-D05-012 | PID Control Tuning | PID 控制調參 | D05.6 | ENG | R3 | PRAC | M |
| SC-D05-013 | Load Management Strategy Design | 負載管理策略設計 | D05.6 | DES | R2 | PRAC | M |
| SC-D05-014 | Frequency Regulation Control Design | 頻率調節控制設計 | D05.6 | DES | R2 | PRAC | M |

---

### D06 — Panel Engineering (6 candidates)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D06-001 | Panel Layout Design and Thermal Calculation | 盤面佈局設計與散熱計算 | D06.1 | DES | R2 | PRAC | H |
| SC-D06-002 | Wiring Diagram Development | 配線圖繪製 | D06.2 | DES | R2 | PRAC | H |
| SC-D06-003 | Terminal Block Schedule Development | 端子排表建立 | D06.2 | DOC | R2 | PRAC | H |
| SC-D06-004 | Fabrication Drawing Production (CAD) | 施工圖 CAD 出圖 | D06.3 | ENG | R2 | PRAC | H |
| SC-D06-005 | Wire Sizing Calculation | 線徑選用計算 | D06.2 | ANA | R2 | PRAC | M |
| SC-D06-006 | Component Selection and Specification Writing | 元件選型與規範書撰寫 | D06.4 | DES | R1,R2 | PRAC | H |

---

### D07 — Integration Engineering (7 candidates)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D07-001 | Interface Integration Matrix Development | 介面整合矩陣建立 | D07.1 | DOC | R2 | PRAC | M |
| SC-D07-002 | System Integration Architecture Diagram | 系統整合架構圖繪製 | D07.1 | DES | R2 | PRAC | M |
| SC-D07-003 | Protocol Gateway Configuration | 協定閘道配置 | D07.2 | ENG | R3 | PRAC | H |
| SC-D07-004 | Data Format Conversion Design | 資料格式轉換設計 | D07.2 | DES | R2,R3 | PRAC | M |
| SC-D07-005 | Cross-System Data Model Alignment | 跨系統資料模型對齊 | D07.3 | DES | R2 | PRAC | M |
| SC-D07-006 | Timestamp Synchronization Design | 時間戳同步設計 | D07.3 | DES | R2,R3 | PRAC | M |
| SC-D07-007 | Third-Party API Integration | 第三方 API 串接 | D07.4 | INT | R3 | PRAC | M |

---

### D08 — Testing & Commissioning (13 candidates; +2 in R5) ◆ SC-D08-012 遷移至 D10

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D08-001 | FAT Procedure Development | FAT 程序撰寫 | D08.1 | DOC | R3 | ID01 §6.5.1.4; ID02 A.11 | H |
| SC-D08-002 | Security FAT Test Case Design | 安全 FAT 測試案例設計 | D08.1 | TST | R3 | ID02 A.11; ID03 Table 2 Doc 3.07 | H |
| SC-D08-003 | SAT Procedure Development | SAT 程序撰寫 | D08.2 | DOC | R3 | ID02 A.11; ID03 Table 2 Doc 3.12 | H |
| SC-D08-004 | Site Acceptance Testing Execution | 現場驗收測試執行 | D08.2 | TST | R3 | ID01 §7.6; ID02 C.7 | H |
| SC-D08-005 | System Security Acceptance Testing | 系統安全驗收測試 | D08.2 | TST | R3 | ID01 §6.5.1.4.3; §7.6 | H |
| SC-D08-006 | Commissioning Plan Development | 試車計畫撰寫 | D08.3 | DOC | R3 | PRAC | H |
| SC-D08-007 | Performance Baseline Establishment | 性能基線建立 | D08.4 | TST | R3 | PRAC | M |
| SC-D08-008 | Application Security Testing Execution | 應用安全測試執行 | D08.4 | TST | R3 | ID01 §6.5.1.4.2; §7.5 | H |
| SC-D08-009 | Penetration Testing Execution | 滲透測試執行 | D08.4 | TST | R3 | ID01 §6.5.1.4.4; ID03 Table 2 Doc 3.17 | H |
| SC-D08-010 | Vulnerability Scanning and Reporting | 弱點掃描與報告 | D08.4 | TST | R3,R4 | ID02 A.12 | H |
| SC-D08-011 | Defect Report Writing and Severity Classification | 缺陷報告撰寫與分級 | D08.5 | DOC | R3 | PRAC | H |
| ~~SC-D08-012~~ | ~~System Decommissioning Execution~~ | ~~系統除役執行~~ | ~~D08.6~~ | — | — | — | — | ◆ 遷移至 D10, 見 SC-D10-006 |
| SC-D08-013 △ | Site Integration Test (SIT) Protocol Development | SIT 測試協定撰寫 | D08.2 | DOC | R3 | ID14 (Tier 2 SIT as distinct phase) | H |
| SC-D08-014 △ | Security Inspection and Test Protocol Development | 安全檢驗測試協定撰寫 | D08.4 | DOC | R3 | ID14 (Tier 2; 14-category example) | H |

---

### D09 — Engineering Documentation (9 candidates; +1 in R5)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D09-001 | System Design Description Writing | 系統設計說明書撰寫 | D09.1 | DOC | R2 | PRAC | H |
| SC-D09-002 | Security Functional Description Specification | 安全功能描述規範撰寫 | D09.1 | DOC | R3 | ID02 A.9; ID03 Table 2 Doc 3.02 | H |
| SC-D09-003 | Single-Line Diagram (SLD) Development | 單線圖繪製 | D09.2 | DES | R2 | PRAC | H |
| SC-D09-004 | Document Delivery Checklist Management | 文件交付清單管理 | D09.4 | MGT | R3 | ID03 §5.5.3 | H |
| SC-D09-005 | Version Control and Archiving | 版本控制與歸檔 | D09.4 | MGT | R0-R5 | PRAC | M |
| SC-D09-006 | Operation Manual Writing | 操作手冊撰寫 | D09.5 | DOC | R3 | PRAC | H |
| SC-D09-007 | SOP Development | SOP 編撰 | D09.5 | DOC | R3,R4 | PRAC | H |
| SC-D09-008 | Training Material Development | 培訓教材製作 | D09.5 | DOC | R3,R4 | ID01 §6.3; ID03 §5.3.3 | M |
| SC-D09-009 △ | Hardening Recommended Practices Document | 加固建議實踐文件撰寫 | D09.1 | DOC | R3 | ID13 (Tier 2 format example) | H |

---

### D10 — Project Engineering (7 candidates; +1 in R5) ★◆ RE-SCOPED to post-acceptance + decommissioning

8 candidates migrated to D14. 1 new candidate added. See `phase1-revision-r2.md` for migration table.

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D10-001 | Requirements Traceability Matrix Management | 需求追溯矩陣管理 | D10.1 | DOC | R1,R2 | PRAC | M |
| SC-D10-002 | Change Request Evaluation and Impact Analysis | 變更申請評估與影響分析 | D10.2 | ANA | R1-R4 | ID01 §6.5.2.3; §7.8.7 | H |
| SC-D10-003 | Management of Change (MOC) Execution | 變更管理執行 | D10.2 | MGT | R1-R4 | ID01 §7.8.7.1; ID03 §5.7.1 | H |
| SC-D10-004 | Technical Clarification Meeting Facilitation | 技術澄清會議主持 | D10.3 | MGT | R1-R3 | PRAC | M |
| SC-D10-005 | Contract Technical Scope Tracking | 合約技術範圍追蹤 | D10.4 | MGT | R1-R4 | PRAC | H |
| SC-D10-006 ◆ | System Decommissioning Execution | 系統除役執行 | D10.5 | OPS | R5 | ID01 §6.5.3 | H | ◆ 由 SC-D08-012 遷入 |
| SC-D10-007 △ | Permit to Work (PtW) Process Management | 工作許可流程管理 | D10.2 | MGT | R3,R4 | ID04 §12.0 (Tier 2) | M |

---

### D14 — Pre-Gate Engineering (18 candidates; +2 in R5) ★ NEW DOMAIN

10 candidates migrated from former D10 + 6 new candidates.

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D14-001 | Requirements Specification Development | 需求規格書撰寫 | D14.1 | DOC | Pre-R0 | ID03 §5.1.1; Table 2 Doc 0.01 | H |
| SC-D14-002 ◆ | Stakeholder Analysis | 利害關係人分析 | D14.5 | ANA | Pre-R0 | PRAC | M | ◆ 由 D14.1 遷至 D14.5（利害關係人分析與介面清冊） |
| SC-D14-003 | Technical Feasibility Assessment | 技術可行性評估 | D14.3 | ANA | Pre-R0 | PRAC | H |
| SC-D14-004 | Technical Risk Matrix Development | 技術風險矩陣建立 | D14.6 | ANA | Pre-R0 | PRAC | M |
| SC-D14-005 | CBOM Development | CBOM 編制 | D14.4 | ENG | Pre-R0 | PRAC | H |
| SC-D14-006 | Labor Hour Estimation | 工時估算 | D14.4 | ANA | Pre-R0 | PRAC | H |
| SC-D14-007 | RFI Response Preparation | RFI 回覆準備 | D14.1 | DOC | Pre-R0 | PRAC | M |
| SC-D14-008 | Technical Proposal Writing | 技術提案撰寫 | D14.3 | DOC | Pre-R0 | PRAC | H |
| SC-D14-009 | POC Planning and Execution | POC 規劃與執行 | D14.3 | MGT | Pre-R0 | PRAC | M |
| SC-D14-010 | Tender Security Requirements Definition | 投標安全需求定義 | D14.6 | DOC | Pre-R0 | ID01 §6.5.1.1.1; ID03 Table 1 SSA-PRO-001 | H |
| SC-D14-011 | Site Survey and Constraint Documentation | 現場勘查與限制條件文件 | D14.2 | ANA | Pre-R0 | PRAC | H |
| SC-D14-012 | Existing Infrastructure Inventory | 既有基礎設施清冊 | D14.2 | DOC | Pre-R0 | PRAC | H |
| SC-D14-013 | Concept Zone/Conduit Architecture | 概念 Zone/Conduit 架構 | D14.3 | DES | Pre-R0 | PRAC; ID01 §6.5.1.1 | M |
| SC-D14-014 | Preliminary Security Classification | 初步安全分類 | D14.6 | ANA | Pre-R0 | ID03 §5.4.1; ID01 §6.5.1.2 | H |
| SC-D14-015 | Gate 0 Decision Package Assembly | Gate 0 決策包組裝 | D14.6 | DOC | Pre-R0 | ID01 §6.5.1.1.3; ID03 §5.5.2 | H |
| SC-D14-016 | Cost Risk Contingency Analysis | 成本風險餘裕分析 | D14.4 | ANA | Pre-R0 | PRAC | M |
| SC-D14-017 △ | NDA and Confidentiality Agreement Management | NDA 與保密協議管理 | D14.1 | MGT | Pre-R0 | ID25 (Tier 3 template) | H |
| SC-D14-018 ▲ | Pre-Gate 0 Requirement Clarification & Feasibility Input | Pre-Gate 0 需求釐清與可行性輸入 | D14.3 | ANA | Pre-R0 | GOV-SD (5 Gate 0 inputs; non-binding boundary) | H |

---

### D11 — Engineering Governance (21 candidates; +9 in R5, SC-D11-002 superseded by SC-D11-017)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D11-001 | Design Review Checklist Development | 設計審查清單建立 | D11.1 | GOV | R2 | PRAC | H |
| ~~SC-D11-002~~ | ~~Stage-Gate Review Facilitation~~ | ~~階段閘門審查主持~~ | ~~D11.1~~ | — | — | — | — | ▲ R5: Superseded by SC-D11-017 (governance-authoritative gate review) |
| SC-D11-003 | Critical Security Design Review | 關鍵安全設計審查 | D11.1 | VER | R2 | ID01 §7.3.2 | H |
| SC-D11-004 | Engineering SOP Development | 工程 SOP 制定 | D11.2 | GOV | R0-R5 | PRAC | H |
| SC-D11-005 | Process Efficiency Analysis | 流程效率分析 | D11.2 | ANA | R4 | PRAC | L |
| SC-D11-006 | Quality Plan Development | 品質計畫撰寫 | D11.3 | DOC | R1 | PRAC | H |
| SC-D11-007 | Nonconformance Management | 不合格項管理 | D11.3 | MGT | R3,R4 | ID01 §6.6.4 | M |
| SC-D11-008 | Lessons Learned Management | 經驗學習管理 | D11.4 | MGT | R4,R5 | PRAC | M |
| SC-D11-009 | Technical Knowledge Base Development | 技術知識庫建置 | D11.4 | ENG | R4 | PRAC | L |
| SC-D11-010 | Internal Design Standards Maintenance | 內部設計標準維護 | D11.5 | GOV | R0-R5 | PRAC | M |
| SC-D11-011 | Engineering Competency Framework Development | 工程能力框架建立 | D11.6★◆ | GOV | R0 | ID01 §6.3; ID03 §5.3.3 | H | ◆ 由安全能力泛化為工程能力（ADR-006），安全能力為首要實例 |
| SC-D11-012 | Engineering Training Program Management | 工程培訓計畫管理 | D11.6★◆ | MGT | R0-R5 | ID01 §6.3; ID03 §5.3.3 | H | ◆ 由安全培訓泛化為工程培訓（ADR-006） |
| SC-D11-013 △ | Information Asset Classification and Grading | 資訊資產分類分級 | D11.3 | GOV | R0,R4 | ID23 (Tier 3 procedure) | H |
| SC-D11-014 △ | Personnel Security Qualification Management | 人員安全資格管理 | D11.6 | MGT | R0–R5 | ID21 (Tier 3); ID06 §5.4 | H |
| SC-D11-015 △ | Procurement Security Requirements Integration | 採購安全需求整合 | D11.2 | GOV | R0,R1 | ID22 (Tier 3 procedure) | H |
| SC-D11-016 △ | SI/SM Project Security Management Plan Development | SI/SM 專案安全管理計畫撰寫 | D11.2 | DOC | R0 | ID06 (Tier 2; 45+ pages) | H |
| SC-D11-017 ▲ | Gate Review Governance & Blocking Condition Verification | 階段審查治理與阻斷條件驗證 | D11.1 | GOV | R0–R3 | GOV-SD (4-gate blocking conditions; 12-item Gate 3 checklist) | H |
| SC-D11-018 ▲ | Design Quality & Traceability Verification | 設計品質與追溯性驗證 | D11.3 | VER | R1,R3 | GOV-SD (Design QA role; traceability matrix; document register) | H |
| SC-D11-019 ▲ | Standards Ownership & Exception Arbitration | 標準歸屬與例外裁定 | D11.2 | GOV | R0–R5 | GOV-SDP (standards ownership; exception ruling; L1-L2-L3 escalation) | H |
| SC-D11-020 ▲ | Design Change Impact Analysis & SL Recertification | 設計變更影響分析與SL重認證 | D11.2 | ANA | R2 | GOV-SD (Gate 2 triggers; SL Decision Record update) | H |
| SC-D11-021 ▲ | Role KPI Evidence Collection & Scoring | 角色KPI證據收集與評分 | D11.6 | MGT | R0–R5 | GOV-SDP (SMART KPIs; RCW/AF/PVF formula; bonus mechanism) | M |

---

### D12 — Energy Data Platform (8 candidates)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D12-001 | Data Acquisition Architecture Design | 資料採集架構設計 | D12.1 | DES | R2 | PRAC | M |
| SC-D12-002 | Protocol Parser Development | 協定解析器開發 | D12.1 | ENG | R2,R3 | PRAC | M |
| SC-D12-003 | Time-Series Database Selection and Configuration | 時序資料庫選型與配置 | D12.2 | ENG | R2 | PRAC | M |
| SC-D12-004 | Data Retention Policy Design | 資料保留策略設計 | D12.2 | DES | R2 | PRAC | M |
| SC-D12-005 | Load Forecasting Model Development | 負載預測模型開發 | D12.3 | ENG | R2,R3 | PRAC | M |
| SC-D12-006 | Monitoring Dashboard Design | 監控儀表板設計 | D12.4 | DES | R3 | PRAC | M |
| SC-D12-007 | Data Dictionary Development | 資料字典建立 | D12.5 | DOC | R2 | PRAC | M |
| SC-D12-008 | Data Access Policy Design | 資料存取政策設計 | D12.5 | GOV | R2 | PRAC | M |

---

### D13 — Engineering Automation (6 candidates)

| SC ID | Skill Name (EN) | 技能名稱 (ZH) | Subdomain | Type | Lifecycle | Source | Confidence |
|-------|----------------|------------|-----------|------|-----------|--------|------------|
| SC-D13-001 | Automated Calculation Script Development | 自動化計算腳本開發 | D13.1 | ENG | R2,R3 | PRAC | M |
| SC-D13-002 | Document Generator Development | 文件產生器開發 | D13.1 | ENG | R3 | PRAC | M |
| SC-D13-003 | AI-Assisted Design Review | AI 輔助設計審查 | D13.2 | ENG | R2 | PRAC | L |
| SC-D13-004 | Automated Skill Invocation | 自動化技能調用 | D13.2 | ENG | R2-R4 | PRAC | L |
| SC-D13-005 | Automated Test Pipeline Development | 自動化測試管線開發 | D13.3 | ENG | R3 | PRAC | M |
| SC-D13-006 | Review Workflow Automation | 審查工作流程自動化 | D13.4 | ENG | R2-R4 | PRAC | L |

### Inventory Statistics (R5)

| Domain | R3 Count | R5 Count | From ID01-03 | From ID04-25/GOV | From PRAC | H/H+ Conf. | M Conf. | L Conf. |
|--------|---------|---------|-------------|-------------------|-----------|-----------|---------|---------|
| D01 | 28 | 36 | 24 | 8 △▲ | 4 | 31 | 5 | 0 |
| D02 | 12 | 12 | 4 | 0 | 8 | 4 | 7 | 1 |
| D03 | 10 | 10 | 0 | 0 | 10 | 2 | 7 | 1 |
| D04 | 6 | 6 | 0 | 0 | 6 | 3 | 3 | 0 |
| D05 | 14 | 14 | 0 | 0 | 14 | 5 | 9 | 0 |
| D06 | 6 | 6 | 0 | 0 | 6 | 4 | 2 | 0 |
| D07 | 7 | 7 | 0 | 0 | 7 | 1 | 6 | 0 |
| D08 ◆ | 11 | 13 | 8 | 2 △ | 3 | 11 | 1 | 1 |
| D09 | 8 | 9 | 3 | 1 △ | 5 | 6 | 3 | 0 |
| D10 ★◆ | 6 | 7 | 3 | 1 △ | 3 | 3 | 3 | 1 |
| D11 | 12 | 21 | 5 | 9 △▲ | 7 | 14 | 4 | 3 |
| D12 | 8 | 8 | 0 | 0 | 8 | 0 | 8 | 0 |
| D13 | 6 | 6 | 0 | 0 | 6 | 0 | 3 | 3 |
| D14 ★ | 16 | 18 | 4 | 2 △▲ | 12 | 10 | 5 | 3 |
| **Total** | **150** | **173** | **51** | **23** | **99** | **94** | **66** | **13** |

**R5 Normalization notes:**
- R3 post-normalization: 149 (SC-D09-007 merged into SC-D11-004)
- R5 post-normalization: **171** (SC-D09-007 merge + SC-D11-002 superseded by SC-D11-017)
- H+ confidence subset: 19 candidates with both Tier 2 exemplar and Tier 1 governance confirmation (see R5 analysis for details)
- Source tier breakdown: 51 from Tier 2 originals (ID01-03), 15 from Tier 2 exemplars (ID04-14), 5 from Tier 3 org procedures (ID21-25), 8 from Tier 1 governance (GOV-SD/SDP), 99 from PRAC
