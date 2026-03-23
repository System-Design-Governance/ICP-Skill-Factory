# icp-general — ICP 通用工具包 Plugin

## 定位

跨角色通用工具，不綁定特定 IEC 62443 工程職責。所有 ICP 工程角色（SYS / SAC / INT / GOV / PGS）皆可使用。

## Skills

| Skill | 用途 | 觸發情境 |
|-------|------|---------|
| **large-doc-search** | 大型 PDF 拆解為結構化知識庫，支援精準查詢 | 上傳 >50 頁 PDF、手冊查詢、規格比較 |

## 未來擴充候選

以下 standalone skills 評估後可納入：

| Skill | 行數 | 說明 |
|-------|------|------|
| ciso-advisor | 145L | CISO 層級資安建議 |
| senior-security | 445L | 資深資安工程師輔助 |
| sales-engineer | 242L | 售前工程師輔助 |
| dept-timesheet-analyzer | 305L | 部門工時分析 |
| protocol-integrator | 162L | 協定整合輔助 |

## 安裝

```bash
# Claude Cowork 安裝
# 將 icp-general.plugin 拖入 Cowork 或使用 CLI 安裝
```

## 目錄結構

```
icp-general/
├── .claude-plugin/plugin.json
├── README.md
└── skills/
    └── large-doc-search/
        ├── SKILL.md              ← 操作指引
        ├── scripts/ingest.py     ← PDF 拆解腳本 (847L)
        ├── references/query_guide.md  ← 查詢行為規範
        └── assets/index_schema.json   ← index.json schema
```
