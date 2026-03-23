# OT/IT/BoP Protocol Usage Map

> Cross-diagram protocol consistency reference

---

## 1. OT Devices (IEC 61850 PRP Network)

| Device | Protocol | Diagram |
|--------|----------|---------|
| Protection Relay (7SJ82/7UT86/7SL86/7SS85) | IEC 61850 GOOSE/MMS | PROT |
| BCU (6MD85) | IEC 61850 GOOSE/MMS | PROT |
| P850 Power Meter | IEC 61850 MMS | PROT |
| SCADA Server (WinCC OA) | OPC-UA / IEC 104 | SCADA |
| GPS/PTP Clock | IEEE 1588 PTP | PROT, SCADA |

## 2. IT Devices (Ethernet, NOT PRP)

| Device | Protocol | Diagram |
|--------|----------|---------|
| IP Camera / NVR | Ethernet PoE | CCTV |
| ACS Panel / Card Reader | RS-485 / Ethernet | ACS |
| IP-PBX / IP Phone | SIP / Ethernet PoE | TEL |
| FortiAP WiFi | Ethernet / CAPWAP | TEL, SCADA |
| FortiAuthenticator | RADIUS / 802.1X | TEL |

## 3. BoP Devices (Modbus TCP)

| Device | Protocol | Diagram |
|--------|----------|---------|
| SICAM A8000 RTU | Modbus TCP | SCADA, PWR |
| FAS / HVAC / EDG Status | Modbus TCP (via RTU) | SCADA, PWR |
| DC/UPS/Battery Status | Modbus TCP (via RTU) | PWR |

## 4. External Interfaces

| Target | Protocol | Notes |
|--------|----------|-------|
| TPC Dispatch Center | **DNP3** | NOT IEC 104 |
| TPC PSTN Backup | DNP3 PSTN | Dial-up dedicated line |
| OSS/WTG Offshore SCADA | IEC 60870-5-104 | We are Client |
| Cloud DR Backup | HTTPS / VPN | AWS/Azure |

## 5. comm_styles Required Keys (13 mandatory)

`PRP_LAN_A`, `PRP_LAN_B`, `OPC_UA_A`, `OPC_UA_B`, `IEEE1588_A`, `IEEE1588_B`,
`IEC61850_MMS`, `IEC61850_fiber`, `PRP_fiber_A`, `PRP_fiber_B`,
`Modbus_TCP`, `RS485_modbus`, `IT_ethernet`

Optional: `VPN_PSTN`, `RF_wireless`, `RS485`, `IRIG_B`, `DNP3_PSTN`, `DNP3_IEC104`
