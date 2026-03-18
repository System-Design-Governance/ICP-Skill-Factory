#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
05 文件修正工具
根據 02 文件的權威定義，修正所有 cr_ 前綴和 OptionSet 值
"""

import re
from collections import defaultdict
from typing import Dict, List, Tuple

# 從 02 文件定義的 OptionSet 值（權威來源）
OPTIONSET_MAPPINGS = {
    # gov_currentgate
    'gov_currentgate': {
        '900000000': ('100000000', 'Pending'),
        '900000001': ('100000001', 'Gate0'),
        '900000002': ('100000002', 'Gate1'),
        '900000003': ('100000003', 'Gate2'),
        '900000004': ('100000004', 'Gate3'),
    },
    # gov_requeststatus
    'gov_requeststatus': {
        '900000000': ('100000000', 'None'),
        '900000001': ('100000001', 'Pending'),
        '900000002': ('100000002', 'UnderReview'),
        '900000003': ('100000003', 'Approved'),
        '900000004': ('100000004', 'Rejected'),
    },
    # gov_projectstatus
    'gov_projectstatus': {
        '900000000': ('100000000', 'Active'),  # 注意：Draft 不存在於 02，需標記
        '900000001': ('100000000', 'Active'),  # 位置對應調整
        '900000002': ('100000001', 'OnHold'),
        '900000003': ('100000002', 'Closed'),  # Completed -> Closed
        '900000004': ('100000003', 'Terminated'),  # Cancelled -> Terminated
    },
    # gov_documentfreezestatus
    'gov_documentfreezestatus': {
        '900000000': ('100000000', 'NotFrozen'),
        '900000001': ('100000001', 'Frozen'),
    },
    # gov_decision
    'gov_decision': {
        '900000000': ('100000000', 'Pending'),
        '900000001': ('100000001', 'Approved'),
        '900000002': ('100000002', 'Rejected'),
        '900000003': ('100000003', 'Executed'),
    },
    # gov_reviewtype
    'gov_reviewtype': {
        '900000000': ('100000000', 'ProjectCreation'),
        '900000001': ('100000001', 'Gate0Request'),
        '900000002': ('100000002', 'Gate1Request'),
        '900000003': ('100000003', 'Gate2Request'),
        '900000004': ('100000004', 'Gate3Request'),
        '900000005': ('100000005', 'RiskInitialAssessment'),
        '900000006': ('100000006', 'RiskReassessment'),
        '900000007': ('100000007', 'RiskAcceptance'),
        '900000008': ('100000008', 'DocumentFreeze'),
        '900000009': ('100000009', 'LiteToFullUpgrade'),
        '900000010': ('100000010', 'ExceptionWaiverRequest'),
        '900000011': ('100000011', 'ExceptionWaiverApproval'),
        '900000012': ('100000012', 'ProjectClosure'),
    },
    # gov_risklevel
    'gov_risklevel': {
        '900000000': ('100000000', 'Low'),
        '900000001': ('100000001', 'Medium'),
        '900000002': ('100000002', 'High'),
    },
    # gov_layerreviewstatus
    'gov_layerreviewstatus': {
        '900000000': ('100000000', 'Pending'),
        '900000001': ('100000001', 'Approved'),
        '900000002': ('100000002', 'Rejected'),
        '900000003': ('100000003', 'Skipped'),
    },
}

# 02 文件中定義的所有 Table Schema Names
DEFINED_TABLES = [
    'gov_projectregistry',
    'gov_reviewdecisionlog',
    'gov_riskassessmenttable',
    'gov_exceptionwaiverlog',
    'gov_documentregister',
    'gov_governanceviolationlog',
    'gov_counterlist',
]

def fix_document(file_path: str, output_path: str) -> Dict:
    """修正文件"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    modifications = []
    todos = []

    # 統計資料
    prefix_replacements = defaultdict(int)
    optionset_replacements = defaultdict(int)

    # Step 1: Replace Publisher Prefix (cr_ -> gov_)
    print("[1/4] Replacing Publisher Prefix...")

    # Replace Table names
    for table in DEFINED_TABLES:
        cr_table = table.replace('gov_', 'cr_')
        pattern = r'\b' + re.escape(cr_table) + r'\b'
        matches = len(re.findall(pattern, content))
        if matches > 0:
            content = re.sub(pattern, table, content)
            prefix_replacements[f'{cr_table} -> {table}'] = matches
            modifications.append(f"Table: {cr_table} -> {table} ({matches} occurrences)")

    # Replace field names (cr_xxx -> gov_xxx)
    cr_pattern = r'\bcr_([a-z][a-z0-9_]*)\b'
    cr_matches = re.findall(cr_pattern, content)
    unique_fields = set(cr_matches)

    for field in unique_fields:
        old_name = f'cr_{field}'
        new_name = f'gov_{field}'
        pattern = r'\b' + re.escape(old_name) + r'\b'
        matches = len(re.findall(pattern, content))
        if matches > 0:
            content = re.sub(pattern, new_name, content)
            prefix_replacements[f'{old_name} -> {new_name}'] = matches

    print(f"  - Replaced {len(prefix_replacements)} prefixes")

    # Step 2: Replace OptionSet values (900000000 -> 100000000 series)
    print("[2/4] Replacing OptionSet values...")

    # Global replace 900000xxx -> 100000xxx
    for old_val in range(900000000, 900000020):
        new_val = old_val - 800000000  # 900000000 -> 100000000
        pattern = r'\b' + str(old_val) + r'\b'
        matches = len(re.findall(pattern, content))
        if matches > 0:
            content = re.sub(pattern, str(new_val), content)
            optionset_replacements[f'{old_val} -> {new_val}'] = matches

    print(f"  - Replaced {len(optionset_replacements)} OptionSet values")

    # Step 3: Detect undefined states
    print("[3/4] Detecting undefined states...")

    # 檢測 Draft 狀態（02 文件中不存在）
    draft_pattern = r'Draft|900000000.*Draft|100000000.*Draft'
    draft_matches = re.finditer(draft_pattern, content, re.IGNORECASE)
    for match in draft_matches:
        line_num = content[:match.start()].count('\n') + 1
        todos.append({
            'line': line_num,
            'issue': 'gov_projectstatus 的「Draft」狀態未在 02 文件定義',
            'context': match.group(),
            'recommendation': '需決策：1) 在 02 新增 Draft 狀態，2) 移除 Draft 邏輯，專案建立即為 Active'
        })

    # 檢測 Completed 狀態（應對應為 Closed）
    completed_pattern = r'Completed|900000003.*Completed'
    completed_matches = re.finditer(completed_pattern, content, re.IGNORECASE)
    for match in completed_matches:
        line_num = content[:match.start()].count('\n') + 1
        todos.append({
            'line': line_num,
            'issue': 'gov_projectstatus 的「Completed」應對應為 02 文件的「Closed」',
            'context': match.group(),
            'recommendation': '已自動替換 OptionSet 值，但需確認業務語意是否一致'
        })

    # 檢測 Cancelled 狀態（應對應為 Terminated）
    cancelled_pattern = r'Cancelled|900000004.*Cancelled'
    cancelled_matches = re.finditer(cancelled_pattern, content, re.IGNORECASE)
    for match in cancelled_matches:
        line_num = content[:match.start()].count('\n') + 1
        todos.append({
            'line': line_num,
            'issue': 'gov_projectstatus 的「Cancelled」應對應為 02 文件的「Terminated」',
            'context': match.group(),
            'recommendation': '已自動替換 OptionSet 值，但需確認業務語意是否一致'
        })

    print(f"  - Found {len(todos)} items requiring decision")

    # Step 4: Generate fix report
    print("[4/4] Generating fix report...")

    # 在文件末尾新增修正總覽
    report = generate_report(modifications, prefix_replacements, optionset_replacements, todos)

    # 不直接附加報告到文件，而是寫入 content（文件本身已修正）
    # 報告單獨產出

    # 寫入修正後的文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return {
        'prefix_replacements': prefix_replacements,
        'optionset_replacements': optionset_replacements,
        'todos': todos,
        'report': report,
        'changes_made': len(prefix_replacements) + len(optionset_replacements) > 0
    }

def generate_report(modifications, prefix_replacements, optionset_replacements, todos) -> str:
    """產生修正報告"""

    report = []
    report.append("\n" + "="*80)
    report.append("05 文件修正報告")
    report.append("="*80)
    report.append("")
    report.append("## 修正摘要")
    report.append("")
    report.append(f"- Publisher Prefix 替換：{len(prefix_replacements)} 項")
    report.append(f"- OptionSet 值替換：{len(optionset_replacements)} 項")
    report.append(f"- 待決策項目：{len(todos)} 項")
    report.append("")

    # Publisher Prefix 替換總覽
    if prefix_replacements:
        report.append("## Publisher Prefix 替換總覽")
        report.append("")
        report.append("| 原引用 | 新引用 | 替換次數 |")
        report.append("|--------|--------|---------|")
        for old_new, count in sorted(prefix_replacements.items(), key=lambda x: -x[1])[:20]:
            old, new = old_new.split(' -> ')
            report.append(f"| `{old}` | `{new}` | {count} |")
        if len(prefix_replacements) > 20:
            report.append(f"| ... | ... | ... |")
            report.append(f"| 共 {len(prefix_replacements)} 項 | | |")
        report.append("")

    # OptionSet 值替換總覽
    if optionset_replacements:
        report.append("## OptionSet 值替換總覽")
        report.append("")
        report.append("| 原值（05 文件） | 新值（02 文件） | 替換次數 |")
        report.append("|----------------|----------------|---------|")
        for old_new, count in sorted(optionset_replacements.items(), key=lambda x: int(x[0].split(' -> ')[0]))[:20]:
            old, new = old_new.split(' -> ')
            report.append(f"| `{old}` | `{new}` | {count} |")
        if len(optionset_replacements) > 20:
            report.append(f"| ... | ... | ... |")
            report.append(f"| 共 {len(optionset_replacements)} 項 | | |")
        report.append("")

    # TODO 清單
    if todos:
        report.append("## 待決策項目清單（TODO）")
        report.append("")
        report.append("以下項目需要架構決策，無法自動修正：")
        report.append("")
        for i, todo in enumerate(todos, 1):
            report.append(f"### TODO-{i:03d}")
            report.append("")
            report.append(f"**位置**：行 {todo['line']}")
            report.append(f"**問題**：{todo['issue']}")
            report.append(f"**上下文**：`{todo['context']}`")
            report.append(f"**建議**：{todo['recommendation']}")
            report.append("")

    report.append("="*80)
    report.append("修正完成時間：2026-02-08")
    report.append("修正依據：02-dataverse-data-model-and-security.md (權威來源)")
    report.append("="*80)

    return "\n".join(report)

def main():
    file_path = r"c:\Users\victo\OneDrive\文件\開發\治理系統\System-Design-Governance\docs\power-platform-governance\zh-TW\05-core-flows-implementation-runbook.md"
    output_path = file_path  # 直接覆蓋原文件
    report_path = r"c:\Users\victo\OneDrive\文件\開發\治理系統\System-Design-Governance\docs\05-Fix-Report.md"

    print("="*80)
    print("05 Document Systematic Fix Tool")
    print("="*80)
    print()
    print(f"Source: {file_path}")
    print(f"Output: {output_path}")
    print()

    result = fix_document(file_path, output_path)

    if result['changes_made']:
        print()
        print("[OK] Fix completed!")
        print()
        print(f"Statistics:")
        print(f"  - Prefix replacements: {len(result['prefix_replacements'])} items")
        print(f"  - OptionSet replacements: {len(result['optionset_replacements'])} items")
        print(f"  - TODO items: {len(result['todos'])} items")
        print()

        # Write report
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(result['report'])

        print(f"Fix report generated: {report_path}")
    else:
        print()
        print("[OK] Document is up-to-date, no fix needed")

    print()
    print("="*80)

if __name__ == "__main__":
    main()
