# Component Evaluation Matrix

**Project:** {Project Name}
**Component Type:** {e.g., Managed Ethernet Switch / PLC CPU / RTU / HMI Panel}
**Author:** {Author}
**Date:** {YYYY-MM-DD}
**Revision:** {Rev}

## 1. Purpose

Provide a structured, weighted comparison of candidate components to support
objective selection decisions. Scoring criteria include technical fit,
cybersecurity compliance, supply chain resilience, lifecycle support, and cost.

## 2. Evaluation Criteria and Weights

| # | Criterion | Weight (%) | Description |
|---|---|---|---|
| 1 | Technical Score | {30} | Performance, features, environmental ratings, form factor |
| 2 | IEC 62443 Score | {20} | Security certification level, secure-by-design features |
| 3 | Supply Chain Score | {15} | Lead time, multi-source availability, regional stock |
| 4 | Lifecycle Score | {15} | Product lifecycle stage, warranty, long-term support commitment |
| 5 | Cost Score | {20} | Unit cost, volume pricing, total cost of ownership |
| | **Total** | **100** | |

## 3. Candidate Comparison

### 3.1 Technical Evaluation

| Technical Attribute | Requirement | Candidate A: {Model} | Candidate B: {Model} | Candidate C: {Model} |
|---|---|---|---|---|
| {Operating Temp Range} | {-40 to +70 deg C} | {-40 to +75 deg C} | {-20 to +60 deg C} | {-40 to +70 deg C} |
| {Protection Rating} | {IP67} | {IP67} | {IP65} | {IP67} |
| {Port Count / I/O Count} | {8x GbE + 2x SFP} | {8+2} | {8+2} | {16+4} |
| {Protocol Support} | {Modbus TCP, OPC UA} | {Yes, Yes} | {Yes, No} | {Yes, Yes} |
| {Redundancy Support} | {MRP / RSTP} | {MRP, RSTP, PRP} | {RSTP only} | {MRP, RSTP} |
| {Power Consumption} | {< 30 W} | {18 W} | {22 W} | {35 W} |
| {Certifications} | {IEC 61850-3, IEEE 1613} | {Both} | {IEC 61850-3 only} | {Both} |
| **Technical Score (1-10)** | | **{8}** | **{5}** | **{7}** |

### 3.2 IEC 62443 Security Evaluation

| Security Attribute | Requirement | Candidate A | Candidate B | Candidate C |
|---|---|---|---|---|
| {IEC 62443-4-1 Certified (SDLC)} | {Required} | {Yes, TUV certified} | {No} | {Yes, self-declared} |
| {IEC 62443-4-2 SL Capability} | {SL-2 minimum} | {SL-2 certified} | {SL-1} | {SL-2 capable} |
| {Secure Boot} | {Required} | {Yes} | {No} | {Yes} |
| {Encrypted Communication} | {TLS 1.2+} | {TLS 1.3} | {TLS 1.2} | {TLS 1.2} |
| {Role-Based Access Control} | {Required} | {Yes, granular} | {Basic user/admin} | {Yes} |
| {Audit Logging} | {Required} | {Syslog + local} | {Local only} | {Syslog + local} |
| {Firmware Signing} | {Required} | {Yes} | {No} | {Yes} |
| {Vulnerability Disclosure Program} | {Preferred} | {Yes, PSIRT active} | {No formal program} | {Yes} |
| **IEC 62443 Score (1-10)** | | **{9}** | **{3}** | **{7}** |

### 3.3 Supply Chain Evaluation

| Supply Chain Attribute | Candidate A | Candidate B | Candidate C |
|---|---|---|---|
| {Current Lead Time} | {4 weeks} | {2 weeks} | {8 weeks} |
| {Regional Distributor (Taiwan)} | {Yes, 2 distributors} | {Yes, 1 distributor} | {No, import only} |
| {Alternate Sources} | {2 compatible models} | {None} | {1 compatible model} |
| {Country of Origin Risk} | {Low} | {Medium} | {Low} |
| **Supply Chain Score (1-10)** | | **{8}** | **{6}** | **{5}** |

### 3.4 Lifecycle Evaluation

| Lifecycle Attribute | Candidate A | Candidate B | Candidate C |
|---|---|---|---|
| {Product Lifecycle Stage} | {Active, launched 2023} | {Mature, launched 2018} | {Active, launched 2024} |
| {Stated Product Availability} | {10+ years} | {EOL announced 2027} | {10+ years} |
| {Warranty} | {5 years} | {2 years} | {3 years} |
| {Firmware Update Commitment} | {Quarterly security patches} | {Annual} | {Quarterly} |
| {Migration Path} | {In-place upgrade to next gen} | {Forklift replacement} | {Pin-compatible successor} |
| **Lifecycle Score (1-10)** | | **{9}** | **{3}** | **{8}** |

### 3.5 Cost Evaluation

| Cost Attribute | Candidate A | Candidate B | Candidate C |
|---|---|---|---|
| {Unit Price (list)} | {USD {X}} | {USD {Y}} | {USD {Z}} |
| {Volume Price (10+ units)} | {USD {X}} | {USD {Y}} | {USD {Z}} |
| {Annual Maintenance / License} | {USD {X}} | {USD {Y}} | {USD {Z}} |
| {Training Cost (one-time)} | {included} | {USD {Y}} | {USD {Z}} |
| {5-Year TCO per Unit} | {USD {X}} | {USD {Y}} | {USD {Z}} |
| **Cost Score (1-10)** | | **{6}** | **{9}** | **{5}** |

## 4. Weighted Total

| Criterion | Weight | Candidate A Score | Weighted A | Candidate B Score | Weighted B | Candidate C Score | Weighted C |
|---|---|---|---|---|---|---|---|
| Technical | {0.30} | {8} | {2.40} | {5} | {1.50} | {7} | {2.10} |
| IEC 62443 | {0.20} | {9} | {1.80} | {3} | {0.60} | {7} | {1.40} |
| Supply Chain | {0.15} | {8} | {1.20} | {6} | {0.90} | {5} | {0.75} |
| Lifecycle | {0.15} | {9} | {1.35} | {3} | {0.45} | {8} | {1.20} |
| Cost | {0.20} | {6} | {1.20} | {9} | {1.80} | {5} | {1.00} |
| **Total** | **1.00** | | **{7.95}** | | **{5.25}** | | **{6.45}** |

## 5. Recommendation

**Selected:** {Candidate A -- {Model Name}}

**Justification:** {e.g., "Candidate A achieves the highest weighted score driven by
superior security certification, longest lifecycle commitment, and strong regional
supply chain. Although unit cost is higher than Candidate B, the 5-year TCO is
competitive when factoring maintenance and migration costs."}

## 6. Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Engineering Lead | {name} | | {date} |
| Procurement | {name} | | {date} |
| Security Lead | {name} | | {date} |
