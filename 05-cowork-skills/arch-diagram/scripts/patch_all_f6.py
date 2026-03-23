#!/usr/bin/env python3
"""
F6 ONS — 統一 D2 patch 腳本
修正所有圖面的邏輯認知錯誤：
  1. Non-OT 圖面（CCTV/ACS/TEL/PWR）去除 PRP 標籤、修正協定
  2. OT 圖面（PROT/SCADA/TPC）保留 IEC 61850 MMS/GOOSE
  3. 共用修正：移除 RedBox class 定義、修正 L4 newline
"""
import re, sys

def fix_newline_in_labels(s):
    """修正 Python replace 產生的實際 newline → D2 literal \\n"""
    lines = s.split('\n')
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # 偵測 D2 雙引號字串被中斷的情況（行尾有開引號但沒關引號）
        if '"' in line and line.count('"') % 2 == 1 and '{ class:' not in line and '->' not in line:
            # 這行有未關閉的引號，合併下一行
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                line = line.rstrip() + '\\n' + next_line
                i += 2
                result.append(line)
                continue
        result.append(line)
        i += 1
    return '\n'.join(result)


def patch_common(s):
    """所有圖面共用修正"""
    # 移除 RedBox class 定義
    s = re.sub(r'  redbox: \{[^}]+\}\n', '', s)
    # 修正 L4 node newline 問題
    s = fix_newline_in_labels(s)
    # 統一移除中文殘留
    s = s.replace('輔助設備', 'Auxiliary')
    s = s.replace('HMI 及監控桌\\n', '')
    s = s.replace('HMI 及監控桌\n', '')
    # LAN 標籤：移除中文，但保留 LAN-A/LAN-B 標識（由各 patch 函式決定是否改名）
    # 不在 common 統一改——PRP 圖保留 LAN-A/B，非 PRP 圖由 patch_non_ot() 改為 Ethernet
    s = s.replace('LAN-A（IEC 62439-3 獨立實體網路）', 'LAN-A (IEC 62439-3)')
    s = s.replace('LAN-B（IEC 62439-3 獨立實體網路）', 'LAN-B (IEC 62439-3)')
    # 統一清理 MCC 前綴（patch 後殘留的）
    s = re.sub(r'MCC-OnSWST\s+', 'OnSWST ', s)
    s = re.sub(r'MCC-WiFi\s+', 'WiFi ', s)
    s = re.sub(r'MCC-VoIP\s+', 'VoIP ', s)
    s = re.sub(r'MCC-ONS\s+', 'ONS ', s)
    return s


def patch_l4_labels(s, nodes):
    """替換 L4 預設節點"""
    for old, new in nodes.items():
        s = s.replace(old, new)
    return s


def patch_non_ot(s):
    """Non-OT 圖面（CCTV/ACS/TEL/PWR）專用修正"""
    # LAN 標籤：去除 PRP/IEC 62439-3
    # 非 PRP 圖：移除所有 LAN-A/LAN-B/PRP 術語
    s = s.replace('LAN-A (IEC 62439-3)', 'Ethernet VLAN')
    s = s.replace('LAN-B (IEC 62439-3)', 'Ethernet VLAN-B')
    # Switch 節點名稱中的 "LAN-A" → 移除
    s = re.sub(r' LAN-A ', ' ', s)
    # Core Switch A → Core Switch（去掉 A，因為沒有 B）
    s = s.replace('Core Switch A', 'Core Switch')
    # 連線標籤中的 "PRP LAN-A" → 協定名稱由各 patch 覆蓋
    s = s.replace(': "PRP LAN-A"', ': "Ethernet"')
    s = s.replace(': "PRP LAN-B"', ': "Ethernet"')

    # L2→L1 連線協定：IEC 61850 MMS → Ethernet
    # 只修正 L2→L1 的連線（保留 L3→L2 的 OPC-UA）
    s = re.sub(
        r'(SW_\w+_A -> L1\.\w+\.RTU_\w+): "IEC 61850 MMS"',
        r'\1: "Ethernet"',
        s
    )
    s = re.sub(
        r'(SW_\w+_B -> L1\.\w+\.REDBOX_\w+): "PRP.*?"',
        r'\1: "Ethernet"',
        s
    )

    # MCC 連線協定：Modbus TCP → Ethernet（對 non-OT 設備）
    s = re.sub(
        r'(SW_\w+_A -> L1\.mcc\.MCC_\w+): "Modbus TCP"',
        r'\1: "Ethernet"',
        s
    )
    return s


def patch_cctv(path):
    s = open(path, encoding='utf-8').read()
    s = patch_common(s)

    # L4：CCTV 不需要 L4（已 disabled）
    s = re.sub(r'  ERP:.*\n', '', s)
    s = re.sub(r'  ADCC:.*\n', '', s)
    s = re.sub(r'  SCADA_WS:.*\n', '', s)

    # L3 子群組
    s = s.replace('SCADA 伺服器群', 'VMS / SCADA Integration')
    s = s.replace('輔助設備', 'Display')

    # L2/L1 協定修正
    s = patch_non_ot(s)

    # MCC → PoE Switch
    s = s.replace('MCC 群', 'PoE Switch')
    s = s.replace('MCC-ONS  ONS Building + Yard', 'PoE Switch ONS (14 ports)')
    s = s.replace('MCC-SWST  Switching Station', 'PoE Switch OnSWST (6 ports)')

    # DMZ→L3：OPC-UA → Ethernet（CCTV 不用 OPC-UA）
    s = s.replace('DMZ.FW -> L3.scada_grp.HMI_A: "OPC-UA', 'DMZ.FW -> L3.scada_grp.HMI_A: "Ethernet')
    s = s.replace('DMZ.FW -> L3.scada_grp.HMI_B: "OPC-UA', 'DMZ.FW -> L3.scada_grp.HMI_B: "Ethernet')

    # L3→L2：OPC-UA → Ethernet
    s = re.sub(r'(L3\.scada_grp\.\w+ -> L2\.lana\.SW_CORE_A): "OPC-UA.*?"', r'\1: "Ethernet"', s)
    s = re.sub(r'(L3\.scada_grp\.\w+ -> L2\.lanb\.SW_CORE_B): "OPC-UA.*?"', r'\1: "Ethernet"', s)
    s = re.sub(r'(L3\.scada_grp\.HIST -> L2\.lana\.SW_CORE_A): ""', r'\1: ""', s)
    s = re.sub(r'(L3\.scada_grp\.HIST -> L2\.lanb\.SW_CORE_B): ""', r'\1: ""', s)

    open(path, 'w', encoding='utf-8').write(s)


def patch_acs(path):
    s = open(path, encoding='utf-8').read()
    s = patch_common(s)

    s = re.sub(r'  ERP:.*\n', '', s)
    s = re.sub(r'  ADCC:.*\n', '', s)
    s = re.sub(r'  SCADA_WS:.*\n', '', s)

    s = s.replace('SCADA 伺服器群', 'ACS Management')
    s = s.replace('輔助設備', 'Alarm Integration')
    s = patch_non_ot(s)

    s = s.replace('MCC 群', 'Field Wiring')
    s = s.replace('MCC-ONS  ONS Building', 'Wiring Hub ONS')
    s = s.replace('MCC-SWST  Switching Station', 'Wiring Hub OnSWST')

    # DMZ→L3：OPC-UA → Ethernet
    s = s.replace(': "OPC-UA', ': "Ethernet')

    # L3→L2
    s = re.sub(r'(L3\.scada_grp\.\w+ -> L2\.lana\.SW_CORE_A): "OPC-UA.*?"', r'\1: "Ethernet"', s)
    s = re.sub(r'(L3\.scada_grp\.\w+ -> L2\.lanb\.SW_CORE_B): "OPC-UA.*?"', r'\1: "Ethernet"', s)

    open(path, 'w', encoding='utf-8').write(s)


def patch_telecom(path):
    s = open(path, encoding='utf-8').read()
    s = patch_common(s)

    # L4
    s = s.replace('ERP: "ERP 系統" { class: external_system }',
                   'TPC_LINE: "TPC Dispatch\\nDedicated Line" { class: external_system }')
    s = re.sub(r'  ADCC:.*\n', '', s)
    s = re.sub(r'  SCADA_WS:.*\n', '', s)
    s = s.replace('L4.ERP', 'L4.TPC_LINE')

    # 移除指向已刪除 L4 節點的連線
    s = re.sub(r'L4\.ADCC[^\n]*\n(?:[^\n]*\n){3,4}', '', s)
    s = re.sub(r'L4\.SCADA_WS[^\n]*\n(?:[^\n]*\n){3,4}', '', s)

    # L3
    s = s.replace('SCADA 伺服器群', 'PBX / WiFi Management')
    s = s.replace('輔助設備', 'Authentication')

    # L2/L1
    s = patch_non_ot(s)
    s = s.replace('MCC 群', 'PoE Distribution')
    s = s.replace('MCC-WIFI  FortiAP x 16 (ONS+OnSWST)', 'FortiAP x 16')
    s = s.replace('MCC-VOIP  PoE Switch  Voice', 'PoE VoIP Switch')

    # DMZ→L3：OPC-UA → SIP/Ethernet
    s = s.replace('DMZ.FW -> L3.scada_grp.HMI_A: "OPC-UA', 'DMZ.FW -> L3.scada_grp.HMI_A: "SIP Trunk')
    s = s.replace('DMZ.FW -> L3.scada_grp.HMI_B: "OPC-UA', 'DMZ.FW -> L3.scada_grp.HMI_B: "HTTPS/CAPWAP')

    # L2→L1 PBX：IEC 61850 → Ethernet（PBX 不用 IEC 61850）
    s = re.sub(r'(-> L1\.pbx\.RTU_PBX): "IEC 61850[^"]*"', r'\1: "Ethernet"', s)

    # L3→L2
    s = re.sub(r'(L3\.scada_grp\.\w+ -> L2\.lana\.SW_CORE_A): "OPC-UA.*?"', r'\1: "Ethernet"', s)
    s = re.sub(r'(L3\.scada_grp\.\w+ -> L2\.lanb\.SW_CORE_B): "OPC-UA.*?"', r'\1: "Ethernet"', s)

    # ENG_WS (FortiAuth) → L2 連線
    s = s.replace('L3.aux_grp.ENG_WS -> L2.lana.SW_CORE_A: "IEC 61850 Monitor"',
                   'L3.aux_grp.ENG_WS -> L2.lana.SW_CORE_A: "RADIUS / 802.1X"')

    open(path, 'w', encoding='utf-8').write(s)


def patch_power(path):
    s = open(path, encoding='utf-8').read()
    s = patch_common(s)

    s = re.sub(r'  ERP:.*\n', '', s)
    s = re.sub(r'  ADCC:.*\n', '', s)
    s = re.sub(r'  SCADA_WS:.*\n', '', s)

    s = s.replace('SCADA 伺服器群', 'SCADA Monitoring (Ref)')
    s = s.replace('輔助設備', '')
    s = s.replace('MCC 群', 'Power Distribution')
    s = s.replace('MCC-ONS  ONS Power', 'ONS Power Panel')

    # L2/L1：Power 用 Modbus TCP，不是 PRP — 移除所有 LAN-A 術語
    s = s.replace('LAN-A (IEC 62439-3)', 'Modbus TCP Network')
    s = re.sub(r' LAN-A ', ' ', s)
    s = s.replace('Core Switch A', 'Core Switch')
    s = s.replace(': "PRP LAN-A"', ': "Modbus TCP"')

    # L2→L1：RTU 用 Modbus TCP（不是 IEC 61850）
    s = re.sub(
        r'(SW_\w+_A -> L1\.\w+\.RTU_\w+): "IEC 61850 MMS"',
        r'\1: "Modbus TCP"',
        s
    )

    # DMZ→L3
    s = s.replace(': "OPC-UA', ': "Modbus TCP')

    # L3→L2
    s = re.sub(r'(L3\.scada_grp\.\w+ -> L2\.lana\.SW_CORE_A): "OPC-UA.*?"', r'\1: "Modbus TCP"', s)

    open(path, 'w', encoding='utf-8').write(s)


def patch_scada(path):
    s = open(path, encoding='utf-8').read()
    s = patch_common(s)

    # L4
    s = s.replace('ERP: "ERP 系統" { class: external_system }',
                   'OSS: "OSS SCADA\\n500MW + 300MW" { class: external_system }')
    s = s.replace('ADCC: "ADCC 電力調度" { class: external_system }',
                   'CLOUD: "Cloud DR Backup\\n5yr AWS/Azure" { class: external_system }')
    s = s.replace('SCADA_WS: "SCADA 工作站" { class: hmi_workstation }',
                   'OMC: "F6 O&M Centre" { class: hmi_workstation }')
    s = s.replace('L4.ERP', 'L4.OSS')
    s = s.replace('L4.ADCC', 'L4.CLOUD')
    s = s.replace('L4.SCADA_WS', 'L4.OMC')

    # 移除 CLOUD→MODEM 連線（不經 PSTN）— 5 行 block: 連線 + 3 style + closing }
    s = re.sub(r'L4\.CLOUD -> DMZ\.MODEM[^\n]*\n(?:[^\n]*\n){3,4}', '', s)

    # L3
    s = s.replace('SCADA 伺服器群', 'WinCC OA SCADA')
    s = s.replace('輔助設備', 'NMS + Time Sync')
    s = s.replace('Gateway 責任分界點', 'Offshore SCADA Client')

    # MCC → Fortinet 設備
    s = s.replace('MCC 群', 'Fortinet Access Layer')
    s = s.replace('MCC-ONS  ONS L2 Switch x 8', 'FortiSwitch 124F x 17 ONS')
    s = s.replace('MCC-SWST  OnSWST L2 Switch x 4 + FW', 'FortiSwitch 124F x 5 + FG 80F OnSWST')
    s = s.replace('MCC-WIFI  FortiAP x 16 + FortiAuth', 'FortiAP x 16 + FortiAuth')

    # L2 IT 網路不是 PRP — 移除所有 LAN-A/PRP 術語
    s = s.replace('LAN-A (IEC 62439-3)', 'Fortinet Managed Network')
    s = re.sub(r' LAN-A ', ' ', s)
    s = s.replace('Core Switch A', 'Core Switch')
    s = s.replace(': "PRP LAN-A"', ': "Ethernet"')

    # RTU LV 連線：IEC 61850 → Modbus TCP
    s = s.replace('SW_SWST_A -> L1.rtu_lv.RTU_RTU_LV: "IEC 61850 MMS"',
                   'SW_SWST_A -> L1.rtu_lv.RTU_RTU_LV: "Modbus TCP"')

    # WiFi MCC 連線：Modbus TCP → Ethernet
    s = s.replace('SW_WIFI_A -> L1.mcc.MCC_WIFI: "Modbus TCP"',
                   'SW_WIFI_A -> L1.mcc.MCC_WIFI: "Ethernet / CAPWAP"')

    open(path, 'w', encoding='utf-8').write(s)


def patch_prot(path):
    s = open(path, encoding='utf-8').read()
    s = patch_common(s)

    # L4
    s = s.replace('ERP: "ERP 系統" { class: external_system }',
                   'TPC: "TPC Grid\\nPCC1 + PCC2 Inter-trip" { class: external_system }')
    s = s.replace('ADCC: "ADCC 電力調度" { class: external_system }',
                   'OSS: "OSS + WTG\\n800MW Offshore" { class: external_system }')
    s = s.replace('L4.ERP', 'L4.TPC')
    s = s.replace('L4.ADCC', 'L4.OSS')

    # L3
    s = s.replace('SCADA 伺服器群', 'SCADA / HMI')
    s = s.replace('輔助設備', 'Engineering / Time Sync')

    # MCC → RCP Panel
    s = s.replace('MCC 群', 'RCP Panel (28 Faces)')
    s = s.replace('MCC-TR  Transformer Bay', 'RCP TR Bay × 3')
    s = s.replace('MCC-LINE  Line / Cable Bay', 'RCP LINE Bay × 3')
    s = s.replace('MCC-BUS  Busbar + VSR + HF', 'RCP BUS/VSR/HF × 7')
    s = s.replace('MCC-FDR  22.8kV Feeder', 'RCP FDR Bay × 15')

    # L2→L1：OT 保護系統正確使用 IEC 61850 MMS，不修改
    # MCC (RCP) 連線保持 Modbus TCP（RCP 盤的輔助信號用 Modbus）
    # 不需要額外修正

    open(path, 'w', encoding='utf-8').write(s)


def patch_tpc(path):
    s = open(path, encoding='utf-8').read()
    s = patch_common(s)

    # L4
    s = s.replace('ERP: "ERP 系統" { class: external_system }',
                   'TPC: "TPC SCADA\\nDNP3" { class: external_system }')
    s = re.sub(r'  ADCC:.*\n', '', s)
    s = re.sub(r'  SCADA_WS:.*\n', '', s)
    s = s.replace('L4.ERP', 'L4.TPC')
    s = re.sub(r'L4\.ADCC[^\n]*\n(?:[^\n]*\n){3,4}', '', s)
    s = re.sub(r'L4\.SCADA_WS[^\n]*\n(?:[^\n]*\n){3,4}', '', s)

    # L4→DMZ 連線：Ethernet → DNP3
    s = s.replace('L4.TPC -> DMZ.FW: "Ethernet"', 'L4.TPC -> DMZ.FW: "DNP3"')

    # L3
    s = s.replace('SCADA 伺服器群', 'SCADA / SPS')
    s = s.replace('輔助設備', '')

    # MCC
    s = s.replace('MCC 群', 'Interface Panel')
    s = s.replace('MCC-PCC  TPC PCC Bay', 'TPC Interface Panel PCC')
    s = s.replace('MCC-MON  SPS Curtailment', 'SPS Interface Panel')

    # OTU 從 DMZ 移到更合適的描述
    s = s.replace('L3 Switch\\nOTU x 2  Fiber Termination', 'OTU x 2\\nFiber Termination')

    open(path, 'w', encoding='utf-8').write(s)


def patch_overview(path):
    s = open(path, encoding='utf-8').read()
    s = patch_common(s)

    # L4
    s = s.replace('ERP: "ERP 系統" { class: external_system }',
                   'TPC: "TPC SCADA\\nPCC1 + PCC2" { class: external_system }')
    s = s.replace('ADCC: "ADCC 電力調度" { class: external_system }',
                   'ADCC: "ADCC / CDCC\\nDispatch" { class: external_system }')
    s = s.replace('SCADA_WS: "SCADA 工作站" { class: hmi_workstation }',
                   'OMC: "F6 O&M Centre" { class: hmi_workstation }')
    s = s.replace('L4.ERP', 'L4.TPC')
    s = s.replace('L4.SCADA_WS', 'L4.OMC')

    # L3
    s = s.replace('SCADA 伺服器群', 'SCADA + VMS')
    s = s.replace('輔助設備', 'Management + Time Sync')
    s = s.replace('Gateway 責任分界點', 'Offshore SCADA Client')

    # L2
    s = s.replace('MCC 群', 'Network Layer')
    s = s.replace('MCC-OT  PRP IEC 61850 (See DWG-PROT)', 'OT PRP Network (DWG-PROT)')
    s = s.replace('MCC-IT  FortiSwitch 124F x 22', 'IT/Safety Network (DWG-SCADA)')

    # L2 LAN 標籤：Overview 混合 OT+IT，移除 LAN-A/PRP 術語
    s = s.replace('LAN-A (IEC 62439-3)', 'OT + IT Network Infrastructure')
    s = re.sub(r' LAN-A ', ' ', s)
    s = s.replace('Core Switch A', 'Core Switch')
    s = s.replace(': "PRP LAN-A"', ': "Ethernet"')

    # L1→L0 的 IT 連線修正
    s = s.replace('L1.bop.RTU_BOP -> L0.solar.CCTV: "Ethernet"',
                   'L1.bop.RTU_BOP -> L0.solar.CCTV: "Ethernet PoE"')
    s = s.replace('L1.bop.RTU_BOP -> L0.solar.TEL: "Ethernet"',
                   'L1.bop.RTU_BOP -> L0.solar.TEL: "SIP / Ethernet"')

    # L1→L0 OT 連線保持 IEC 61850
    # (已正確)

    open(path, 'w', encoding='utf-8').write(s)


if __name__ == '__main__':
    import os
    base = os.path.dirname(os.path.abspath(__file__))

    configs = {
        'cctv': patch_cctv,
        'acs': patch_acs,
        'telecom': patch_telecom,
        'power': patch_power,
        'scada': patch_scada,
        'prot': patch_prot,
        'tpc': patch_tpc,
        'overview': patch_overview,
    }

    for name, fn in configs.items():
        path = os.path.join(base, f'f6_{name}.d2')
        if os.path.exists(path):
            fn(path)
            print(f'[OK] Patched f6_{name}.d2')
        else:
            print(f'[SKIP] f6_{name}.d2 not found')
