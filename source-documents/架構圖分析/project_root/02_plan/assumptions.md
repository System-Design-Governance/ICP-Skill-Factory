# Assumptions & Risks — OT 架構圖自動化工具鏈

版本：v1.0
更新日期：2026-03-04

---

## 當前登錄

| ID | 類型 | 描述 | 影響 | 行動 | 狀態 |
|----|------|------|------|------|------|
| A01 | 假設 | 執行環境已安裝 Python 3.9+、d2 CLI（最新版） | 若未安裝，T13 以後所有測試任務均 BLOCKED | Controller 在 Step 0 前確認環境；若未安裝，T21 前需補充 requirements.txt / setup 文件 | OPEN |
| A02 | 假設 | Framework §4.2 的 project.yaml 範例是本次整合測試的唯一測試用例 | 若有其他拓撲變化（如 prp_enabled=false），覆蓋率不足 | 接受此限制；若需更多測試案例，Controller 補充至 00_inbox/ | OPEN |
| A03 | 假設 | D2 CLI 版本的 dagre 行為與 Framework §6/§9 Rulebook 描述一致 | 若 D2 新版改變 dagre 行為，Rulebook 中的 T-04/R-D2-03 可能失效 | Executor 在 T14 測試時確認 D2 版本號並記錄至 test_report | OPEN |
| A04 | 假設 | `scada_level1_template_v2.d2` 的 classes 區塊已存在於開發環境，或可從 Framework §8 品牌色碼反推完整 CLASSES_BLOCK | 若不存在，T04 需要從頭設計 CLASSES_BLOCK，工作量增加 | Executor 執行 T04 前先確認是否有 template 檔案；若無，依 §8 R-BR-01 重建 | OPEN |
| A05 | 假設 | Framework 中的 HMI-ADV-DA820 是 component_library.yaml 的第 6 個初始設備（T02 DoD 要求 ≥ 5，已由 5 個確認，第 6 個為加值） | 不影響 T02 通過，僅影響測試覆蓋率 | 不需要行動 | ACCEPTED |
| R01 | 風險 | dagre 在特定拓撲下（如 feeder_groups > 8）可能出現新的碰撞問題，導致 T22 E2E 測試 a_class ≥ 5 | M（中等）— 需額外迭代調整 project.yaml 或新增 Rulebook | T22 若 a_class ≥ 5，Executor 根據碰撞報告調整 connected_to=null，並更新 Framework §9（KB 新增） | OPEN |
| R02 | 風險 | optimize_svg.py 的 find_empty_zone() 在某些拓撲找不到空白區域，Legend fallback 到右下角，可能超出畫布 | M — 視覺品質問題，不影響功能 | T17 實作時加入 fallback 邊界保護（right-bottom 座標 ≤ 畫布寬-50px） | OPEN |
| R03 | 風險 | 開發過程中 Framework Rulebook 可能需要新增規則（如發現新的 dagre 行為限制） | L（低）— 只影響對應任務，不影響整體架構 | 新規則由 Controller 登錄並補充至 Framework DOC-02，對應任務加入新 DoD 條件 | OPEN |
| R04 | 風險 | project.yaml 的 feeder_groups 動態展開（T07）可能在 feeder 數量為 1 或 > 10 的邊界情況出現錯誤 | L — 影響 T14 測試通過率 | T14 補充邊界測試：feeder_groups=1 和 feeder_groups=9 | OPEN |
| B01 | 阻塞 | 無 `scada_level1_template_v2.d2` 原始檔案 — CLASSES_BLOCK 需要從 Framework §8 + §3.3 重建 | 影響 T04 工作量（估計增加 20~30 分鐘） | Executor 執行 T04 前確認；若無原始檔，從 R-BR-01 + §3.3 D2 class 清單重建 CLASSES_BLOCK | OPEN（不影響進行） |

---

## 類型定義

- **假設**：視為真實但未經驗證的前提
- **風險**：可能發生的不利事件
- **阻塞**：缺少必要資訊，但不影響任務推進（已有替代方案）

## 狀態定義

- **OPEN**：尚未解決
- **RESOLVED**：已確認或消除
- **ACCEPTED**：接受此限制，不採取行動
- **BLOCKED**：需要外部輸入才能繼續（目前無此狀態）
