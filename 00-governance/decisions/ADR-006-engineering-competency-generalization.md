# ADR-006: 工程能力管理通用化（Engineering Competency Generalization）

**狀態：** 已接受（Accepted）
**日期：** 2026-03-13
**來源：** `phase1-formal-review-r3.md` DEF-002 / FIX-002

---

## 背景（Context）

R1 版本新增 D11.6「安全能力管理」（Security Competency Management），源自 ID03 §5.3.3 安全能力要求框架，涵蓋安全專業培訓、資格認定、能力追蹤。

R3 獨立審查中識別出命名過於狹隘的問題：D11.6 目前僅服務於安全領域（D01 OT-CYBERSECURITY），但 ICP 的工程能力管理需求不限於安全——電力系統工程（D03）、保護工程（D04）、控制系統工程（D05）等領域同樣存在能力認證、培訓計畫、資格追蹤的需求。若 D11.6 僅以「安全」命名，將限制治理框架的擴展性，或迫使未來為每個領域重複建立能力管理子領域。

## 決策（Decision）

將 D11.6 由「安全能力管理」（Security Competency Management）更名為「工程能力管理」（Engineering Competency Management），作為跨域通用的能力治理子領域。

安全能力框架（源自 ID03 §5.3.3 及 ID01 §6.3）作為 D11.6 的**首要實例化案例**——即第一個在此子領域下定義的具體技能集。其他領域的能力框架（電力、保護、控制等）可在後續 Phase 中逐步加入。

## 影響（Consequences）

**正面影響：**
- D11.6 成為統一的能力管理入口，避免在多個 Domain 中重複建立能力管理子領域
- 符合 D11 ENGINEERING-GOVERNANCE 作為通用治理域的定位——能力管理是治理的一環
- Phase 3 定義技能時，SC-D11-011（能力框架建立）和 SC-D11-012（培訓計畫管理）可從安全領域擴展至全域適用

**注意事項：**
- 原 SC-D11-011 更名為 Engineering Competency Framework Development（工程能力框架建立）
- 原 SC-D11-012 更名為 Engineering Training Program Management（工程培訓計畫管理）
- 兩項候選技能保留 ID01 §6.3 和 ID03 §5.3.3 的文件溯源，作為安全能力實例的規範性依據
- 未來擴展至其他領域時，PRAC 來源候選項須經領域專家驗證

## 替代方案（Alternatives Considered）

**方案 A（未採用）：保留「安全能力管理」不變**
- 優點：命名直接對應 ID03 文件
- 缺點：限制擴展性，未來需在 D03/D04/D05 等域重複建立能力管理子領域

**方案 B（已採用）：泛化為「工程能力管理」**
- 優點：統一入口，符合治理域定位，可擴展
- 缺點：與 ID03 原始命名略有偏離，需在技能定義中保留安全能力的溯源

---

*決策記錄結束*
