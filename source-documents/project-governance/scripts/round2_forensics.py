#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第二輪一致性鑑識工具
檢查語意一致性問題（Draft/Completed/Cancelled）
"""

import re
from typing import Dict, List, Tuple
from collections import defaultdict

# 權威來源定義的正確狀態
VALID_PROJECT_STATES = ['Active', 'OnHold', 'Closed', 'Terminated']
DEPRECATED_STATES = {
    'Draft': {
        'correct': 'PreGate0 (Active + Pending)',
        'reason': '專案一旦建立即進入治理範圍，不存在草稿狀態',
        'optionset': 'N/A (使用 Active + currentgate = Pending 組合)'
    },
    'Completed': {
        'correct': 'Closed',
        'reason': '術語一致性，對齊 02 文件權威定義',
        'optionset': '100000002'
    },
    'Cancelled': {
        'correct': 'Terminated',
        'reason': '明確區分正常結案與異常終止',
        'optionset': '100000003'
    }
}

def scan_file_for_deprecated_states(file_path: str) -> List[Dict]:
    """掃描文件中已淘汰的狀態"""
    issues = []

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for deprecated, info in DEPRECATED_STATES.items():
        pattern = r'\b' + deprecated + r'\b'
        matches = re.finditer(pattern, content, re.IGNORECASE)

        for match in matches:
            line_num = content[:match.start()].count('\n') + 1
            # 取得上下文（前後 30 字元）
            start = max(0, match.start() - 30)
            end = min(len(content), match.end() + 30)
            context = content[start:end].replace('\n', ' ')

            issues.append({
                'file': file_path.split('\\')[-1],
                'line': line_num,
                'deprecated': deprecated,
                'correct': info['correct'],
                'context': context,
                'reason': info['reason'],
                'optionset': info['optionset']
            })

    return issues

def scan_for_old_prefix(file_path: str) -> List[Dict]:
    """掃描仍使用 cr_ prefix 的地方"""
    issues = []

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 搜尋 cr_ pattern
    pattern = r'\bcr_([a-z][a-z0-9_]*)\b'
    matches = re.finditer(pattern, content)

    for match in matches:
        line_num = content[:match.start()].count('\n') + 1
        start = max(0, match.start() - 30)
        end = min(len(content), match.end() + 30)
        context = content[start:end].replace('\n', ' ')

        issues.append({
            'file': file_path.split('\\')[-1],
            'line': line_num,
            'old_prefix': match.group(0),
            'correct': match.group(0).replace('cr_', 'gov_'),
            'context': context
        })

    return issues

def scan_for_old_optionset(file_path: str) -> List[Dict]:
    """掃描仍使用 900000000 系列的 OptionSet 值"""
    issues = []

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 搜尋 900000xxx pattern
    pattern = r'\b(90000000\d)\b'
    matches = re.finditer(pattern, content)

    for match in matches:
        line_num = content[:match.start()].count('\n') + 1
        old_val = match.group(1)
        new_val = str(int(old_val) - 800000000)

        start = max(0, match.start() - 30)
        end = min(len(content), match.end() + 30)
        context = content[start:end].replace('\n', ' ')

        issues.append({
            'file': file_path.split('\\')[-1],
            'line': line_num,
            'old_value': old_val,
            'correct': new_val,
            'context': context
        })

    return issues

def check_test_coverage(file_path: str) -> Dict:
    """檢查測試案例涵蓋範圍"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    coverage = {
        'pregate0': False,
        'gate0_transition': False,
        'terminated': False,
        'closed': False
    }

    # PreGate0 測試（專案建立後但未提交 Gate 0）
    if re.search(r'PreGate0|專案建立後.*未提交.*Gate.*0', content, re.IGNORECASE):
        coverage['pregate0'] = True

    # Gate 0 轉換測試
    if re.search(r'Gate.*0.*轉換|Gate.*0.*審批|提交.*Gate.*0', content, re.IGNORECASE):
        coverage['gate0_transition'] = True

    # Terminated 測試
    if re.search(r'\bTerminated\b|專案終止|異常終止', content, re.IGNORECASE):
        coverage['terminated'] = True

    # Closed 測試
    if re.search(r'\bClosed\b|專案結案|正常結案', content, re.IGNORECASE):
        coverage['closed'] = True

    return coverage

def check_sharepoint_pregate0(file_path: str) -> Dict:
    """檢查 SharePoint 資料夾結構是否能容納 PreGate0 專案"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    result = {
        'folder_creation_timing': None,
        'supports_pregate0': False,
        'issues': []
    }

    # 檢查資料夾建立時機
    if re.search(r'GOV-001.*建立.*資料夾|專案建立.*時.*建立.*資料夾', content, re.IGNORECASE):
        result['folder_creation_timing'] = 'GOV-001 (專案建立時)'
        result['supports_pregate0'] = True

    # 檢查是否有狀態限制
    if re.search(r'Gate.*0.*通過.*後.*建立.*資料夾', content, re.IGNORECASE):
        result['supports_pregate0'] = False
        result['issues'].append('資料夾建立時機設定為 Gate 0 通過後，無法容納 PreGate0 專案')

    return result

def generate_report(all_issues: Dict) -> str:
    """產生第二輪鑑識報告"""

    report = []
    report.append("# 第二輪一致性鑑識報告")
    report.append("")
    report.append("**報告日期**：2026-02-08")
    report.append("**鑑識範圍**：語意一致性檢查（Phase 1 & 2 已完成）")
    report.append("**權威來源**：02-dataverse-data-model-and-security.md、05-core-flows-implementation-runbook.md")
    report.append("")
    report.append("---")
    report.append("")

    # 執行摘要
    report.append("## 執行摘要")
    report.append("")

    total_issues = sum([
        len(all_issues['deprecated_states']),
        len(all_issues['old_prefix']),
        len(all_issues['old_optionset']),
        len([k for k, v in all_issues['test_coverage'].items() if not v])
    ])

    p0_count = len([i for i in all_issues['deprecated_states'] if i['file'] == '04-powerapps-forms.md'])
    p1_count = len(all_issues['old_prefix']) + len(all_issues['old_optionset'])
    p2_count = len([k for k, v in all_issues['test_coverage'].items() if not v])

    report.append(f"- **總問題數**：{total_issues}")
    report.append(f"- **P0（阻斷上線）**：{p0_count}")
    report.append(f"- **P1（高風險）**：{p1_count}")
    report.append(f"- **P2（中風險）**：{p2_count}")
    report.append("")

    # 問題詳情
    report.append("---")
    report.append("")
    report.append("## 問題清單")
    report.append("")

    issue_num = 1

    # Section 1: 已淘汰狀態
    if all_issues['deprecated_states']:
        report.append(f"### ISSUE-R2-{issue_num:03d}: 使用已淘汰的專案狀態")
        report.append("")
        report.append("**風險等級**：P0（阻斷上線）")
        report.append("")
        report.append("**問題描述**：")
        report.append("以下文件仍使用已被淘汰的專案狀態（Draft/Completed/Cancelled），與治理決策不一致。")
        report.append("")
        report.append("**影響範圍**：")
        report.append("")

        by_file = defaultdict(list)
        for issue in all_issues['deprecated_states']:
            by_file[issue['file']].append(issue)

        for file_name, issues in by_file.items():
            report.append(f"#### {file_name}")
            report.append("")
            report.append("| 行號 | 已淘汰狀態 | 正確狀態 | 上下文 |")
            report.append("|-----|----------|---------|--------|")
            for issue in issues:
                context = issue['context'][:50] + "..." if len(issue['context']) > 50 else issue['context']
                report.append(f"| {issue['line']} | `{issue['deprecated']}` | `{issue['correct']}` | {context} |")
            report.append("")
            report.append("**修正建議**：")
            report.append("")
            for deprecated in set([i['deprecated'] for i in issues]):
                info = DEPRECATED_STATES[deprecated]
                report.append(f"- **{deprecated}** → `{info['correct']}`")
                report.append(f"  - 原因：{info['reason']}")
                report.append(f"  - OptionSet 值：{info['optionset']}")
            report.append("")

        issue_num += 1

    # Section 2: 舊 Prefix
    if all_issues['old_prefix']:
        report.append(f"### ISSUE-R2-{issue_num:03d}: 仍使用 cr_ Prefix")
        report.append("")
        report.append("**風險等級**：P1（高風險）")
        report.append("")
        report.append("**問題描述**：")
        report.append("以下文件仍使用 cr_ prefix，應替換為 gov_。")
        report.append("")

        by_file = defaultdict(list)
        for issue in all_issues['old_prefix']:
            by_file[issue['file']].append(issue)

        for file_name, issues in by_file.items():
            report.append(f"#### {file_name}")
            report.append("")
            report.append(f"- **總計**：{len(issues)} 處")
            report.append("")
            # 只列出前 5 個範例
            report.append("**範例**（前 5 處）：")
            report.append("")
            report.append("| 行號 | 舊引用 | 正確引用 |")
            report.append("|-----|--------|---------|")
            for issue in issues[:5]:
                report.append(f"| {issue['line']} | `{issue['old_prefix']}` | `{issue['correct']}` |")
            if len(issues) > 5:
                report.append(f"| ... | ... | ... |")
            report.append("")

        report.append("**修正方式**：執行 `fix_05_document.py` 腳本進行批次替換")
        report.append("")

        issue_num += 1

    # Section 3: 舊 OptionSet 值
    if all_issues['old_optionset']:
        report.append(f"### ISSUE-R2-{issue_num:03d}: 仍使用 900000000 系列 OptionSet 值")
        report.append("")
        report.append("**風險等級**：P1（高風險）")
        report.append("")
        report.append("**問題描述**：")
        report.append("以下文件仍使用 900000000 系列 OptionSet 值，應替換為 100000000 系列。")
        report.append("")

        by_file = defaultdict(list)
        for issue in all_issues['old_optionset']:
            by_file[issue['file']].append(issue)

        for file_name, issues in by_file.items():
            report.append(f"#### {file_name}")
            report.append("")
            report.append(f"- **總計**：{len(issues)} 處")
            report.append("")
            report.append("**範例**（前 5 處）：")
            report.append("")
            report.append("| 行號 | 舊值 | 新值 |")
            report.append("|-----|------|------|")
            for issue in issues[:5]:
                report.append(f"| {issue['line']} | `{issue['old_value']}` | `{issue['correct']}` |")
            if len(issues) > 5:
                report.append(f"| ... | ... | ... |")
            report.append("")

        report.append("**修正方式**：執行 `fix_05_document.py` 腳本進行批次替換")
        report.append("")

        issue_num += 1

    # Section 4: 測試涵蓋範圍缺口
    missing_coverage = [k for k, v in all_issues['test_coverage'].items() if not v]
    if missing_coverage:
        report.append(f"### ISSUE-R2-{issue_num:03d}: 測試案例涵蓋範圍不足")
        report.append("")
        report.append("**風險等級**：P2（中風險）")
        report.append("")
        report.append("**問題描述**：")
        report.append("測試文件缺少以下關鍵狀態轉換的測試案例。")
        report.append("")
        report.append("**缺少的測試案例**：")
        report.append("")

        coverage_map = {
            'pregate0': {
                'name': 'PreGate0 階段測試',
                'desc': '專案建立後但尚未提交 Gate 0 申請的狀態',
                'test_scenario': '建立專案 → 驗證 currentgate = Pending, projectstatus = Active'
            },
            'gate0_transition': {
                'name': 'Gate 0 轉換測試',
                'desc': '從 PreGate0 轉換到 Active (Gate0) 的流程',
                'test_scenario': '提交 Gate 0 → 審批通過 → 驗證 currentgate = Gate0'
            },
            'terminated': {
                'name': 'Terminated 流程測試',
                'desc': '專案異常終止的完整流程',
                'test_scenario': '專案任意階段 → 終止決策 → 驗證 projectstatus = Terminated'
            },
            'closed': {
                'name': 'Closed 流程測試',
                'desc': '專案正常結案的完整流程',
                'test_scenario': 'Gate 3 通過 → 結案流程 → 驗證 projectstatus = Closed, documentfreezestatus = Frozen'
            }
        }

        for missing in missing_coverage:
            info = coverage_map[missing]
            report.append(f"#### {info['name']}")
            report.append("")
            report.append(f"- **描述**：{info['desc']}")
            report.append(f"- **測試情境**：{info['test_scenario']}")
            report.append("")

        report.append("**修正建議**：在 07-testing-and-acceptance.md 新增對應測試案例")
        report.append("")

        issue_num += 1

    # Section 5: SharePoint 架構檢查
    if not all_issues['sharepoint']['supports_pregate0']:
        report.append(f"### ISSUE-R2-{issue_num:03d}: SharePoint 資料夾結構與 PreGate0 不一致")
        report.append("")
        report.append("**風險等級**：P1（高風險）")
        report.append("")
        report.append("**問題描述**：")
        for issue in all_issues['sharepoint']['issues']:
            report.append(f"- {issue}")
        report.append("")
        report.append("**修正建議**：確認 GOV-001 在專案建立時即建立 SharePoint 資料夾，不等待 Gate 0 通過")
        report.append("")

        issue_num += 1

    # 修正優先級建議
    report.append("---")
    report.append("")
    report.append("## 修正優先級建議")
    report.append("")
    report.append("### P0 - 立即修正（阻斷上線）")
    report.append("")
    report.append("1. **ISSUE-R2-001**：修正 04-powerapps-forms.md 中的已淘汰狀態")
    report.append("   - 影響：使用者介面會顯示錯誤的狀態選項")
    report.append("   - 預估工時：0.5 小時")
    report.append("")
    report.append("### P1 - 高優先級（1 週內完成）")
    report.append("")
    report.append("2. **ISSUE-R2-002/003**：修正 07 文件中的 cr_ prefix 和 900000000 值")
    report.append("   - 影響：測試案例會使用錯誤的欄位名稱和值")
    report.append("   - 預估工時：1 小時（可使用腳本自動修正）")
    report.append("")
    report.append("### P2 - 中優先級（2 週內完成）")
    report.append("")
    report.append("3. **ISSUE-R2-004**：補充缺失的測試案例")
    report.append("   - 影響：關鍵狀態轉換未經測試")
    report.append("   - 預估工時：4 小時")
    report.append("")

    # 附錄：治理狀態對照表
    report.append("---")
    report.append("")
    report.append("## 附錄：治理狀態權威定義")
    report.append("")
    report.append("### gov_projectstatus（專案狀態）")
    report.append("")
    report.append("| OptionSet 值 | 狀態名稱 | 說明 | 觸發條件 |")
    report.append("|------------|---------|------|---------|")
    report.append("| 100000000 | Active | 專案進行中 | GOV-001 建立專案 |")
    report.append("| 100000001 | OnHold | 專案暫停 | 業務決策暫停 |")
    report.append("| 100000002 | Closed | 正常結案 | GOV-012 結案流程 |")
    report.append("| 100000003 | Terminated | 異常終止 | 業務決策或違規終止 |")
    report.append("")
    report.append("### 已淘汰狀態")
    report.append("")
    report.append("| 已淘汰 | 正確狀態 | 原因 |")
    report.append("|-------|---------|------|")
    for deprecated, info in DEPRECATED_STATES.items():
        report.append(f"| {deprecated} | {info['correct']} | {info['reason']} |")
    report.append("")

    report.append("---")
    report.append("")
    report.append("**報告產生工具**：round2_forensics.py")
    report.append("**後續文件**：各文件的修正執行計畫")

    return "\n".join(report)

def main():
    base_path = r"c:\Users\victo\OneDrive\文件\開發\治理系統\System-Design-Governance\docs\power-platform-governance\zh-TW"

    files_to_check = [
        f"{base_path}\\03-sharepoint-architecture.md",
        f"{base_path}\\04-powerapps-forms.md",
        f"{base_path}\\07-testing-and-acceptance.md"
    ]

    print("="*80)
    print("Round 2 Consistency Forensics Tool")
    print("="*80)
    print()

    all_issues = {
        'deprecated_states': [],
        'old_prefix': [],
        'old_optionset': [],
        'test_coverage': {},
        'sharepoint': {}
    }

    # Scan deprecated states
    print("[1/5] Scanning deprecated states...")
    for file_path in files_to_check:
        issues = scan_file_for_deprecated_states(file_path)
        all_issues['deprecated_states'].extend(issues)
    print(f"  - Found {len(all_issues['deprecated_states'])} issues")

    # Scan old prefix
    print("[2/5] Scanning old cr_ prefix...")
    for file_path in files_to_check:
        issues = scan_for_old_prefix(file_path)
        all_issues['old_prefix'].extend(issues)
    print(f"  - Found {len(all_issues['old_prefix'])} issues")

    # Scan old OptionSet values
    print("[3/5] Scanning old OptionSet values...")
    for file_path in files_to_check:
        issues = scan_for_old_optionset(file_path)
        all_issues['old_optionset'].extend(issues)
    print(f"  - Found {len(all_issues['old_optionset'])} issues")

    # Check test coverage
    print("[4/5] Checking test coverage...")
    test_file = f"{base_path}\\07-testing-and-acceptance.md"
    all_issues['test_coverage'] = check_test_coverage(test_file)
    missing = [k for k, v in all_issues['test_coverage'].items() if not v]
    print(f"  - Missing {len(missing)} test cases")

    # Check SharePoint architecture
    print("[5/5] Checking SharePoint architecture...")
    sp_file = f"{base_path}\\03-sharepoint-architecture.md"
    all_issues['sharepoint'] = check_sharepoint_pregate0(sp_file)
    if all_issues['sharepoint']['supports_pregate0']:
        print(f"  - SharePoint supports PreGate0")
    else:
        print(f"  - SharePoint does NOT support PreGate0")

    # Generate report
    print()
    print("Generating report...")
    report = generate_report(all_issues)

    output_path = r"c:\Users\victo\OneDrive\文件\開發\治理系統\System-Design-Governance\docs\Consistency-Forensics-Report-Round2.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print()
    print("="*80)
    print("[OK] Round 2 forensics completed!")
    print("="*80)
    print()
    print(f"Report generated: {output_path}")
    print()
    print("Summary:")
    print(f"  - Deprecated states: {len(all_issues['deprecated_states'])} issues")
    print(f"  - Old prefix: {len(all_issues['old_prefix'])} issues")
    print(f"  - Old OptionSet values: {len(all_issues['old_optionset'])} issues")
    print(f"  - Missing test cases: {len([k for k, v in all_issues['test_coverage'].items() if not v])} cases")
    print()

if __name__ == "__main__":
    main()
