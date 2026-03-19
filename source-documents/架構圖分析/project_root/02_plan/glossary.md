# Glossary — OT 架構圖自動化工具鏈

版本：v1.0
更新日期：2026-03-04

---

## 術語表

| 術語 | 縮寫 | 定義 | 參考來源 |
|------|------|------|----------|
| Purdue Model | — | 工業控制系統網路分層架構模型，分為 L0（現場設備）至 L4（企業層） | ISA-95 |
| Zone | — | 具有共同安全需求的一組資產集合；本框架中對應 Purdue 各層 | IEC 62443-3-2 |
| Conduit | — | 連接兩個 Zone 之間的通訊路徑，含防火牆/跳板機/資料二極體等管控機制 | IEC 62443-3-2 |
| Security Level | SL | 安全等級，分為 SL 1–4，定義系統應抵抗的攻擊能力等級 | IEC 62443-1-1 |
| PRP | Parallel Redundancy Protocol | 雙網冗餘協定，兩條路徑同時傳送封包，任一路徑斷線不影響通訊（零切換時間） | IEC 62439-3 |
| HSR | High-availability Seamless Redundancy | 環形冗餘協定，為 IED 提供無縫備援 | IEC 62439-3 |
| IED | Intelligent Electronic Device | 智能電子裝置，如保護電驛；具備通訊介面，支援 IEC 61850 等協定 | IEC 61850 |
| RTU | Remote Terminal Unit | 遠端終端單元，負責現場 I/O 採集與通訊轉換 | 工業通用 |
| SCADA | Supervisory Control and Data Acquisition | 監控與資料採集系統，位於 Purdue L3 | 工業通用 |
| HMI | Human-Machine Interface | 人機介面工作站，位於 Purdue L3 | 工業通用 |
| DMZ | Demilitarized Zone | 非軍事區，位於 IT 與 OT 網路之間，放置防火牆/跳板機等邊界裝置 | 資安通用 |
| dagre | — | D2 使用的圖形排版引擎；`direction: down` 時依子群組宣告順序從左到右排列 | D2 文件 |
| D2 | — | 本框架使用的圖形描述語言（文字轉 SVG），由 Terrastruct 開發 | D2 官方 |
| CLASSES_BLOCK | — | gen_d2.py 中定義所有設備視覺樣式（顏色、形狀）的常數區塊 | Framework §4, §8 |
| gen_d2.py | — | 讀取 project.yaml + component_library.yaml，套用 Rulebook，輸出 .d2 源碼的 Python 腳本 | Framework §5.1 |
| optimize_svg.py | — | 對 D2 render 輸出的 SVG 執行八步驟後製（Title Bar/Legend/白底遮罩）的 Python 腳本 | Framework §5.2 |
| check_collision.py | — | 檢查 SVG 中 A 類碰撞（連線穿越節點文字）數量的 Python 腳本 | Framework §5.3 |
| A 類碰撞 | — | 連線路徑穿越節點文字的碰撞；合格標準：< 5 為 Yellow，= 0 為 Green，≥ 5 為 Red | Framework §5.3 |
| Rulebook | — | 本框架收錄的所有已驗證規則集合；分為 T 系列（拓撲）、R-D2 系列（D2 語法）、R-PP 系列（SVG後製）、R-BR 系列（品牌色） | Framework §6~§8 |
| Title Bar | — | optimize_svg.py 注入的品牌頂欄，高度 110px，顯示專案名稱/日期/標準 | Framework §7 R-PP-02 |
| Legend | — | 圖面右上角或空白區的浮層圖例，以雙欄顯示元件類型與連線類型 | Framework §7 R-PP-03 |
| feeder_group | — | project.yaml 中的饋線迴路定義單元，每個 group 對應 L2 一對 edge switch + L1 一個 MCC 節點 | Framework §4.2 |
| comm_style | — | project.yaml 中通訊方式的樣式定義（線色、線寬、虛線），以 key 名稱在各設備中引用 | Framework §4.2 |
