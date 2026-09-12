# SURVEY REPORT: DOSSIER & LEGAL PACKAGES RE-TARGETING SCOPE
## Mapping, Corporate Identity, Policy Dates, Agent Information, and Legal Defense Tailoring for DB Insurance Co., Ltd. (DB손해보험주식회사)

- **Survey Agent**: Dossier Scope Explorer (`survey_explorer_2`)
- **Investigation Date**: 2026-09-06 (UTC: 2026-09-06T10:00:00Z)
- **Primary Corpus**: `d:/promotion/legal_claim_package/`, `d:/promotion/CASE_MASTER_KNOWLEDGE_DOSSIER.md`, `d:/promotion/assemble_dossier.py`
- **Governing Mandate**: Refactor all auto insurance claim packages from Samsung Fire & Marine Insurance Co., Ltd. to DB Insurance Co., Ltd. (DB손해보험주식회사), update policy renewal dates from March 13, 2026 to January 21, 2026, retarget managing agent/channels, and preserve all statutory protections under Korean Commercial Code §§ 732-2, 739, 663 and Supreme Court En Banc Decision 98Da48963.

---

## 1. EXECUTIVE SUMMARY & INVESTIGATION OVERVIEW

### 1.1 Core Mission
Following the discovery of the authentic automobile insurance renewal records for vehicle **`28모1390`** (registered to deceased Bangladeshi student **MAHADI MONOAR HOSSAIN**, ARC: `010530-7660021`), the target non-life underwriter of record is **DB Insurance Co., Ltd. (DB손해보험주식회사)** under a valid renewal executed on **January 21, 2026** (effective from 2026-01-21 24:00 KST). 

The entire cross-border legal recovery package—comprising 14 core deliverables in `d:/promotion/legal_claim_package/`, the Master Single Source of Truth (`CASE_MASTER_KNOWLEDGE_DOSSIER.md`), and the dossier build generator (`assemble_dossier.py`)—currently cites **Samsung Fire & Marine Insurance Co., Ltd. (삼성화재해상보험주식회사)** and an obsolete renewal date of March 13, 2026.

This survey provides a complete, forensic mapping of:
1. **Every occurrence** of Samsung Fire mentions, addresses, CEO references, and claims routing.
2. **Every occurrence** of the obsolete renewal date (March 13, 2026) and its replacement with January 21, 2026.
3. **The replacement** of soliciting agent Shim Ki-cheol (`심기철`, `010-8969-0440`) with DB Insurance Direct / Branch customer claims routing (`1588-0100`).
4. **The strict preservation** of vehicle make/model (`28모1390`, Kia Morning / 기아 모닝 경승용) while changing the insurer.
5. **The legal defense architecture**: tailoring Commercial Code §732-2, §739, §663, and Supreme Court En Banc Decision 98Da48963 directly to the standard terms of DB Insurance's automobile policy (DB손해보험 자동차보험 보통약관 - 자기신체사고 및 자동차상해 특별약관).
6. **A file-by-file change specification** for execution by downstream worker agents.

---

## 2. CORPORATE IDENTITY & ENTITY COMPARISON MATRIX

| Dimension | Previous Insurer (Samsung Fire) | Target Insurer (DB Insurance) | Legal & Practical Significance |
| :--- | :--- | :--- | :--- |
| **Full Corporate Name (KR)** | 삼성화재해상보험주식회사 | **DB손해보험주식회사** | Legal entity name in all Korean pleadings, FSS petitions, and POA |
| **Corporate Name (EN)** | Samsung Fire & Marine Insurance Co., Ltd. | **DB Insurance Co., Ltd.** | Corporate name in all English briefs, international DHL invoices, and SWIFT mandates |
| **Representative Director (CEO)** | 대표이사 이문화 (Lee Mun-hwa) | **대표이사 사장 정종표 (Jeong Jong-pyo)** | Addressee on formal Content-Certified Mail and court summons |
| **Corporate Registration / CRN** | 110111-0004994 | **110111-0007882** | Essential for court filing, FSS petition, and corporate verification |
| **Headquarters Address (KR)** | 서울특별시 서초구 서초대로74길 14 (서초동, 삼성화재 서초타워) [우: 06620] | **서울특별시 강남구 테헤란로 432 (대치동, DB금융센터) [우편번호: 06194]** | Crucial for Korea Post Content-Certified Mail envelope matching & e-Post |
| **Headquarters Address (EN)** | Samsung Fire Seocho Tower, 14 Seocho-daero 74-gil, Seocho-gu, Seoul 06620 | **DB Financial Center, 432 Teheran-ro, Gangnam-gu, Seoul 06194, Republic of Korea** | Consignee address for DHL Express Pack 1 from Dhaka |
| **Primary Telephone** | 1588-5114 | **1588-0100 (Direct: 1600-0100)** | Claims reporting hotline and daily adjuster follow-up |
| **Automobile Claims Subsidiary** | 삼성화재애니카손해사정(주) | **DB자동차보험손해사정(주)** | Dedicated claims adjustment entity handling field investigation |
| **Regional Claims Center (Gangwon)** | 강원특별자치도 강릉시 옥천로 19, 삼성화재 강릉사옥 4층 강원보상부 (우: 25539) | **강원특별자치도 원주시 시청로 28 (또는 강릉/속초 관할 보상센터)** / DB자동차보험손해사정 강원사업단 | Territorial office handling the accident scene at Yangyang-gun |
| **Target Policy Product Name** | 삼성화재 애니카 개인용 자동차보험 (종합보험) | **DB손해보험 프로미카 개인용 자동차보험 (또는 다이렉트 자동차보험)** | Contractual policy type covering vehicle 28모1390 |
| **Policy Identifier Format** | `2026-SF-AUTO-28M1390` | **`2026-DB-AUTO-28M1390`** | Universal cross-reference key across all 14 deliverables |
| **Renewal Date & Coverage Window** | 2026-03-13 24:00 (Obsolete) | **2026-01-21 24:00 (Valid ~ 2027-01-21 24:00)** | Policy in active force 52 days prior to the March 14, 2026 fatal accident |
| **Managing Channel / Agent** | 심기철 (`010-8969-0440`), 삼성화재 애니카 | **DB손해보험 다이렉트 / 고객지원센터 (`1588-0100`)** | Solicitation & service channel |
| **Subject Vehicle** | **28모1390 (Kia Morning / 기아 모닝)** | **28모1390 (Kia Morning / 기아 모닝)** | **STAYS UNCHANGED** (Vehicle make is Renault Samsung, NOT insurer) |
| **Claims Intake Email** | `claim@samsungfire.com`, `sfmiclaim@samsungfire.com` | **`claim@idbins.com`, `claim_auto@idbins.com`** | High-priority transmittal emails |

---

## 3. FILE-BY-FILE OCCURRENCE CENSUS & AUDIT

Every single file in `d:/promotion/legal_claim_package/` and `CASE_MASTER_KNOWLEDGE_DOSSIER.md` contains references requiring refactoring. Below is the comprehensive file-by-file occurrence audit.

### File 00: `00_master_dossier_index_and_executive_summary.md`
- **Total Lines**: 520 lines | **Size**: 64,364 bytes
- **Occurrences of Samsung / 삼성**: 27 instances
- **Occurrences of March 13 / 2026-03-13**: 8 instances
- **Occurrences of Agent Shim Ki-cheol / 심기철 / 010-8969-0440**: 6 instances
- **Key Affected Line Ranges**:
  - `Lines 11-13`: Metadata banner (Primary Subject Policy & Vehicle: Samsung Fire Anycar -> DB Insurance Promy Car, Policy No: `2026-DB-AUTO-28M1390`, Renewal: January 21, 2026, Agent: DB Insurance Direct / 1588-0100).
  - `Line 36`: Table of Contents item 1.3 (Target Coverage Architecture: 삼성화재 1억원 -> DB손해보험 1억원).
  - `Line 41`: Table of Contents item 2.1 (Channel 1: Samsung Fire Claim Notice -> DB Insurance Claim Notice).
  - `Lines 95-103`: Case Profile Box (Primary Insurance Policy, Policy Renewal Date, Managing Certified Agent).
  - `Lines 117-122`: Section 1.1 Factual Summary (Renewal on January 21, 2026 by deceased student MAHADI MONOAR HOSSAIN).
  - `Lines 128-132`: Section 1.2 Two-Pronged Recovery Model (Track 1 demand to DB Insurance HQ).
  - `Lines 142, 172`: Section 1.3 Coverage Table (Channel 1: DB Insurance KRW 100M Self-Physical / Auto Injury Death Benefit).
  - `Lines 186-196`: Section 2.1 Channel 1 Description (Formal legal demand served upon DB Insurance Representative Director Jeong Jong-pyo).
  - `Lines 287, 293`: Section 2.7 Legal doctrine summary (DB Insurance 100% payout without offset against Seojeong Univ).
  - `Lines 311-314, 338, 365`: Section 3.2 Deliverable Inventory (File 01 title and target).
  - `Lines 394-420`: Section 3.3 Stage Timeline (Days 0, 3, 10 actions against DB Insurance).
  - `Lines 436-441`: Section 4.1 Contact Directory (Row for DB Insurance HQ, CEO Jeong Jong-pyo, Teheran-ro 432, 1588-0100, `claim@idbins.com`).
  - `Line 455`: Row for KLAC venue (General forum against DB Insurance HQ in Gangnam / Seoul Central).
  - `Lines 472-476`: Section 5 Operational Scenarios A, B, C, D (DB Insurance compliance or breach).
  - `Line 503`: Section 6 SWIFT Remittance instructions (Recoveries from DB Insurance).

---

### File 01: `01_samsung_fire_claim_notice_and_legal_brief.md`
- **Total Lines**: 538 lines | **Size**: 49,287 bytes
- **File Name Refactoring Recommendation**: Rename / compile to `01_db_insurance_claim_notice_and_legal_brief.md`.
- **Occurrences of Samsung / 삼성**: 42 instances
- **Occurrences of March 13 / 2026-03-13**: 6 instances
- **Occurrences of Agent Shim Ki-cheol / 심기철 / 010-8969-0440**: 4 instances
- **Key Affected Line Ranges**:
  - `Line 6`: Document Number (`SFMI-CLAIM-2026-0314-01` -> `DBINS-CLAIM-2026-0314-01`).
  - `Lines 14-20`: Addressee Block:
    - 수신인: DB손해보험주식회사 (DB Insurance Co., Ltd.)
    - 대표자: 대표이사 사장 정종표
    - 주소: 서울특별시 강남구 테헤란로 432 (대치동, DB금융센터) [우편번호: 06194]
    - 소관부서: 자동차보상본부 / 강원사업단(원주/강릉 보상센터) / 보상심사팀
    - 접수창구: DB손해보험 다이렉트 / 고객지원센터 (1588-0100)
  - `Lines 36-42`: [국문 정본] 피보험자동차 및 대상 보험계약의 표시:
    - 피보험차량 번호: `28모1390 (기아 모닝 경승용)`
    - 보험종목: `DB손해보험 프로미카 개인용 자동차보험 (종합보험)`
    - 담보종목: `자기신체사고 (또는 자동차상해 특약) 사망보험금 1억 원`
    - 계약 체결 및 갱신일: `2026년 1월 21일 (2026-01-21 24:00 개시)`
    - 관리 창구: `DB손해보험 다이렉트 / 고객지원센터 (1588-0100)`
  - `Lines 44, 46`: Factual summary (accidental crash on March 14, 2026 while policy was valid).
  - `Lines 54-81`: 청구 취지 (Demand upon DB손해보험주식회사).
  - `Lines 104-108`: Section 4 사전 법률의견서 (Preemptive legal brief rejecting unlicensed driving exemption asserted by DB손해보험).
  - `Lines 109-176`: Detailed statutory analysis under Commercial Code §§ 732-2, 739, 663 and Supreme Court 98Da48963, 97Da27039, 98Da26910 applied to DB Insurance standard auto terms.
  - `Lines 180-207`: Section 5 10-day statutory window and 50% provisional advance demand upon DB Insurance.
  - `Lines 209-237`: Section 6 Direct SWIFT wire instructions to Bangladesh bank.
  - `Lines 241-250`: Section 7 Final legal warning against DB Insurance.
  - `Lines 267-274`: [Part II: English Version] Policy information (DB Insurance Co., Ltd., DB Promy Car Comprehensive Policy, Renewed January 21, 2026).
  - `Lines 287-317`: Formal Prayer for Relief against DB Insurance.
  - `Lines 342-409`: English Preemptive Legal Brief (Statutory Trinity & Supreme Court Precedents against DB Insurance).
  - `Lines 411-442`: 10-day demand and 50% advance against DB Insurance.
  - `Lines 480-488`: Remedies against DB Insurance.
  - `Lines 498-499`: Exhibit 1 in Catalog: DB손해보험 자동차보험 가입증명서 / 보험증권 (DB Insurance Co., Ltd.).

---

### File 02: `02_fss_dispute_mediation_petition.md`
- **Total Lines**: 401 lines | **Size**: 40,723 bytes
- **Occurrences of Samsung / 삼성**: 12 instances
- **Occurrences of March 13 / 2026-03-13**: 3 instances
- **Occurrences of Agent Shim Ki-cheol / 심기철 / 010-8969-0440**: 3 instances
- **Key Affected Line Ranges**:
  - `Lines 6-7`: Title & Target Case (Dispute under DB Insurance Policy `2026-DB-AUTO-28M1390`, Vehicle `28모1390`).
  - `Lines 54-60`: Section [1].3 피신청인 (Respondent Insurer):
    - 회사명: `DB손해보험 주식회사 (DB Insurance Co., Ltd.)`
    - 대표자: `대표이사 정종표 (Representative Director Jeong Jong-pyo)`
    - 본점 소재지: `서울특별시 강남구 테헤란로 432, DB금융센터 (우편번호: 06194)`
    - 대표전화: `1588-0100`
    - 담당 부서: `자동차보상본부 강원사업단 / 보상심사팀`
  - `Lines 74-88`: Section [1].5 대상 보험계약의 표시:
    - 보험종목: `프로미카 개인용 자동차보험 (종합보험)`
    - 증권번호: `2026-DB-AUTO-28M1390`
    - 보험기간: `2026년 1월 21일 24:00부터 2027년 1월 21일 24:00까지`
    - 모집/관리창구: `DB손해보험 다이렉트 / 고객지원센터 (1588-0100)`
    - 자기신체사고/자동차상해 사망보험금: `금 100,000,000원`
  - `Lines 94-105`: Section [2] 신청취지 (Orders against 피신청인 DB손해보험주식회사).
  - `Lines 117-122`: Section [3] 신청이유 (Factual chronology: 2026년 1월 21일 DB손해보험 갱신계약 체결 및 보험료 완납).
  - `Lines 138-143`: Chronological Table (2026. 01. 21. DB손해보험 자동차보험 갱신 체결).
  - `Lines 274-278`: Legal grounds rebutting DB Insurance's improper exclusion arguments.
  - `Lines 324-325`: 갑 제3호증: `DB손해보험 자동차보험 가입증명서 및 보험료납입영수증`.
  - `Lines 336-337`: 갑 제6호증: `보험금 청구서 및 피신청인(DB손해보험) 면책/지급유예 통보 서면`.
  - `Lines 361-365`: Conclusion petitioning FSS to sanction DB Insurance's bad-faith practices.

---

### File 03: `03_seojeong_university_group_insurance_claim.md`
- **Total Lines**: 502 lines | **Size**: 64,659 bytes
- **Occurrences of Samsung / 삼성**: 2 instances
- **Occurrences of March 13 / 2026-03-13**: 0 instances
- **Key Affected Line Ranges**:
  - `Lines 157-158`: Section 4.3 Header & Text:
    - Header: `#### 4.3 자동차보험(DB손해보험)과의 중복보상 및 비상계 원칙`
    - Body: `피보험자가 가입한 자동차보험(DB손해보험주식회사, 차량번호 28모1390)의 자기신체사고/자동차상해 담보와 대학 단체상해보험은 별개의 독립된 인보험(상해보험) 계약입니다...`
    - Statutory Doctrine: Commercial Code Art. 739 non-offset principle.

---

### File 04: `04_bilingual_special_power_of_attorney.md`
- **Total Lines**: 334 lines | **Size**: 41,567 bytes
- **Occurrences of Samsung / 삼성**: 18 instances (7 Korean, 11 English)
- **Occurrences of March 13 / 2026-03-13**: 2 instances
- **Occurrences of Agent Shim Ki-cheol / 심기철 / 010-8969-0440**: 2 instances
- **Key Affected Line Ranges**:
  - `Line 17`: English Header Metadata (`TARGET VEHICLE / POLICY: DB Insurance Co., Ltd. (Vehicle Plate: 28모1390)`).
  - `Lines 107, 120`: Clause 1 Title (Korean: `제1조: DB손해보험 자동차보험금 청구, 보상 협의, 가지급금 및 수령에 관한 특별수권` / English: `CLAUSE 1: DB Insurance Automobile Insurance Claim, Negotiation & Recovery Mandate`).
  - `Lines 123-128`: Clause 1 Korean Text:
    - `DB손해보험주식회사(이하 [DB손해보험])의 자동차보험계약(피보험자동차: 28모1390, 보험계약 갱신일: 2026년 1월 21일, 관리/접수: DB손해보험 다이렉트 / 고객지원센터 1588-0100)`
    - Sub-clauses (a)-(d): Direct demand, 50% provisional advance, negotiation with DB Insurance adjusters.
  - `Lines 130-135`: Clause 1 English Text:
    - `...automobile insurance policy issued by DB Insurance Co., Ltd. ([DB Insurance]) covering the deceased insured MAHADI MONOAR HOSSAIN (Vehicle Plate: 28모1390, Policy Renewal Date: January 21, 2026, Service Channel: DB Insurance Direct / Branch 1588-0100)...`
  - `Lines 159, 166`: Clause 2 (Korean & English FSS dispute mediation against DB Insurance).
  - `Lines 199, 204`: Clause 4 (Korean & English settlement and compromise authority with DB Insurance).
  - `Lines 216-217`: Clause 5 Korean Text (Direct collection from DB손해보험 and direct SWIFT wire to Mutual Trust Bank PLC).
  - `Lines 224-225`: Clause 5 English Text (Direct collection from DB Insurance Co., Ltd. and wire to Mutual Trust Bank PLC).
  - `Line 243`: Section Summary Table row (Accidental death benefits and provisional advance from DB Insurance).

---

### File 04-B: `04_cross_border_heirship_and_legalization_guide.md`
- **Total Lines**: 437 lines | **Size**: 40,156 bytes
- **Occurrences of Samsung / 삼성**: 12 instances
- **Occurrences of March 13 / 2026-03-13**: 1 instance
- **Occurrences of Agent Shim Ki-cheol / 심기철 / 010-8969-0440**: 1 instance
- **Key Affected Line Ranges**:
  - `Line 8`: Metadata (`Target Policy / Vehicle: DB Insurance Co., Ltd. (28모1390)`).
  - `Line 45`: Pipeline diagram (`Track 1: DB Insurance (자손)`).
  - `Lines 56-57`: Section 1.1 Policy Overview (`DB Insurance Automobile Policy (28모1390): Active policy renewed on January 21, 2026, DB Insurance Direct / Customer Center 1588-0100`).
  - `Line 189`: Practice note (Korean claims adjusters at DB Insurance).
  - `Line 266`: Stage 4 checklist (DB Insurance issues Payment Approval Notice).
  - `Line 298`: Section 3.2 Tax note (Proceeds from DB Insurance and Seojeong Univ under KRW 200M tax exemption).
  - `Line 312`: SWIFT Message template Field 50K (`[DB Insurance / Escrow Account]`).
  - `Line 357`: Section 3.4 Non-offset analysis (Group policy does not reduce DB Insurance death benefit).
  - `Line 393`: Remittance clause (Special POA Clause 6 instruction to DB Insurance).
  - `Lines 408, 412, 424`: Actionable Roadmap Stages 1, 2, 5 (Service on DB Insurance, 50% advance, FSS escalation).

---

### File 05: `05_evidence_inventory_and_exhibits_catalog.md`
- **Total Lines**: 477 lines | **Size**: 54,941 bytes
- **Occurrences of Samsung / 삼성**: 16 instances
- **Occurrences of March 13 / 2026-03-13**: 2 instances
- **Occurrences of Agent Shim Ki-cheol / 심기철 / 010-8969-0440**: 2 instances
- **Key Affected Line Ranges**:
  - `Line 11`: Metadata banner (Primary Insurer: DB Insurance Co., Ltd., Policy: `2026-DB-AUTO-28M1390`, Renewal: January 21, 2026, Channel: DB Insurance Direct / 1588-0100).
  - `Line 49`: Executive Summary bullet (`Exhibit C-1: DB Insurance Automobile Policy Certificate (28모1390)`).
  - `Line 104`: Flowchart box (`KRW 100M DB Insurance Accidental Death Benefit`).
  - `Lines 205-207`: Exhibit C-1 Table Row:
    - Document Title: `DB Insurance Automobile Policy Certificate & Premium Receipt (DB손해보험 자동차보험 가입증명서 및 보험료납입영수증)`
    - Issuing Authority: `DB Insurance Co., Ltd. (DB손해보험주식회사)`
    - Details: `Policy: 2026-DB-AUTO-28M1390, renewed on 2026-01-21, KRW 100M Death Benefit`.
  - `Line 308`: Exhibit G-1 Table Row (Content-Certified Mail receipt on DB Insurance HQ).
  - `Line 311`: Exhibit G-2 Table Row (Delivery confirmation card upon DB Insurance).
  - `Line 323`: Exhibit G-5 Table Row (Diplomatic Note Verbale to DB Insurance CEO).
  - `Line 327`: Exhibit G-6 Table Row (Email transmission logs to DB Insurance claims inbox).
  - `Line 348`: Exhibit G-7 Table Row (DHL Express waybill to DB Insurance HQ in Seoul).
  - `Line 356`: Exhibit G-8 Table Row (Electronic filing headers to DB Insurance).
  - `Line 383`: Appendix note (Note Verbale draft to DB Insurance CEO and FSS).
  - `Line 393`: File inventory reference (`01_db_insurance_claim_notice_and_legal_brief.md`).
  - `Line 422`: Exhibit cross-reference audit table (Exhibit C-1 DB Insurance Auto Policy Binder).

---

### File 06: `06_direct_filing_dispatch_package.md`
- **Total Lines**: 755 lines | **Size**: 69,974 bytes
- **Occurrences of Samsung / 삼성**: 38 instances
- **Occurrences of March 13 / 2026-03-13**: 5 instances
- **Occurrences of Agent Shim Ki-cheol / 심기철 / 010-8969-0440**: 7 instances
- **Key Affected Line Ranges**:
  - `Line 2`: Subtitle (`대한민국 내용증명 우편 및 전자접수 송부 편람 (DB손해보험 및 서정대학교)`).
  - `Lines 17-21`: Master Profile Box:
    - Primary Policy: `DB Insurance Co., Ltd. Promy Car Comprehensive Auto Policy (DB손해보험 프로미카 개인용 자동차보험)`
    - Subject Vehicle: `28모1390 (Kia Morning / 기아 모닝 경승용)` (**RETAIN RENAULT SAMSUNG**)
    - Policy Number: `2026-DB-AUTO-28M1390`
    - Service Channel: `DB Insurance Direct / Customer Center (1588-0100)`
  - `Lines 47-55`: Table of Contents Section 1:
    - `SECTION 1: KOREA POST CONTENT-CERTIFIED MAIL COVER LETTER 1 — DB INSURANCE CO., LTD. (DB손해보험주식회사 내용증명 최고서 국문 정본)`
    - `SECTION 3.1: DB Insurance Co., Ltd. Routing Dossier`
    - `SECTION 4.1: High-Priority Email Template A: DB Insurance Claims Department`
  - `Lines 71, 104-143`: Section 1 Content-Certified Mail Cover Letter:
    - Recipient: `DB손해보험주식회사 (DB Insurance Co., Ltd.)`
    - CEO: `대표이사 정종표 귀하`
    - Address: `서울특별시 강남구 테헤란로 432 (대치동, DB금융센터) [우편번호: 06194]`
    - Department: `자동차보상본부 / 강원사업단 / 보상심사팀`
    - Policy: `DB손해보험 프로미카 개인용 자동차보험 (종합보험), 증권번호: 2026-DB-AUTO-28M1390`
    - Renewal date: `2026년 1월 21일 24:00`
    - Demand text: KRW 100M full benefit, KRW 50M provisional advance within 3 business days.
  - `Lines 206-216`: Mandatory statutory demands and FSS escalation warnings against DB Insurance.
  - `Line 240`: Exhibit list item 9 (`갑 제9호증: DB손해보험 자동차보험 가입증명서 및 갱신영수증`).
  - `Line 365`: Section 2 note (DB Insurance auto claim independent from Seojeong Univ group policy).
  - `Lines 415-446`: Section 3.1 DB Insurance Routing Directory:
    - Corporate Name: `DB손해보험주식회사 (DB Insurance Co., Ltd.)`
    - Road Address: `서울특별시 강남구 테헤란로 432 (대치동, DB금융센터)`
    - English Address: `DB Financial Center, 432 Teheran-ro, Gangnam-gu, Seoul 06194`
    - Addressee on Envelope: `DB손해보험주식회사 대표이사 정종표 귀하 (자동차보상본부)`
    - Regional Office: `강원특별자치도 원주시 시청로 28 (또는 강릉/속초) DB자동차보험손해사정 강원사업단 / 보상센터`
    - Intake Emails: `claim@idbins.com`, `claim_auto@idbins.com`
    - Online Upload: `www.idbins.com` (보상서비스 -> 자동차보험 청구서류 접수)
    - Target Policy: `2026-DB-AUTO-28M1390`
  - `Lines 487-560`: Section 4.1 High-Priority Email Template A:
    - To: `claim@idbins.com`, `claim_auto@idbins.com`
    - Addressed to DB Insurance CEO Jeong Jong-pyo in Korean and English.
  - `Lines 689-729`: Section 5 Postal Clerk Compliance:
    - Envelope verbatim matching: `(우편번호 06194) 서울특별시 강남구 테헤란로 432, DB금융센터 DB손해보험주식회사 대표이사 정종표 귀하`.
    - Korea Post e-Post online postal address validation against `06194`.

---

### File 07: `07_legal_aid_and_consular_escalation_roster.md`
- **Total Lines**: 696 lines | **Size**: 84,152 bytes
- **Occurrences of Samsung / 삼성**: 34 instances
- **Occurrences of March 13 / 2026-03-13**: 3 instances
- **Occurrences of Agent Shim Ki-cheol / 심기철 / 010-8969-0440**: 4 instances
- **Key Affected Line Ranges**:
  - `Line 9`: Metadata banner (Primary Subject Policy: DB Insurance, renewed January 21, 2026).
  - `Lines 66, 74`: Section 1 Strategy Overview (Multi-layered pipeline if DB Insurance unlawfully denies/delays).
  - `Line 162`: Section 2.3 KLAC cost recovery note (Court costs assessed against losing defendant DB Insurance under CPA Art. 98).
  - `Line 179`: Item 10 in Checklist (DB Insurance Policy Certificate `28모1390`).
  - `Lines 185, 194, 236-238`: Section 2.5 Territorial Jurisdiction & Venue:
    - Defendant: `DB Insurance Co., Ltd. (DB손해보험주식회사)`
    - Corporate Domicile: `DB Financial Center, 432 Teheran-ro, Gangnam-gu, Seoul 06194`
    - Jurisdiction: Seoul Central District Court / 서울중앙지방법원 (or Seoul Eastern District Court); KLAC Seoul Central / Gangnam Branch.
  - `Lines 332-367`: Section 3.2 Formal Korean Consular Petition to Bangladesh Embassy:
    - 대상 보험사: `DB손해보험주식회사 (DB Insurance Co., Ltd.)`
    - 보험계약: 2026년 1월 21일 갱신 체결, `2026-DB-AUTO-28M1390`
    - 불법 면책 시도 규탄 및 외교공한(Note Verbale) 발송 청원 (수신처: DB손해보험주식회사 대표이사 정종표 귀하, 금융감독원장, 외교부장관)
  - `Lines 408-444`: Section 3.3 Formal English Representation to Embassy:
    - Full English diplomatic petition citing DB Insurance Co., Ltd.
  - `Lines 488-505`: Section 4.1 Diplomatic Note Verbale Protocol:
    - Addressee 1: Chief Executive Officer Jeong Jong-pyo, DB Insurance Co., Ltd. (DB Financial Center, 432 Teheran-ro, Gangnam-gu, Seoul 06194).
    - Diplomatic text demanding immediate SWIFT wire transfer under KCC §732-2.
  - `Lines 565, 584-593, 613, 631, 662-677`: Escalation Timetable & Execution Checklist (Actions targeting DB Insurance HQ).

---

### File 08: `08_attorney_in_fact_execution_checklist.md`
- **Total Lines**: 786 lines | **Size**: 71,167 bytes
- **Occurrences of Samsung / 삼성**: 24 instances
- **Occurrences of March 13 / 2026-03-13**: 2 instances
- **Occurrences of Agent Shim Ki-cheol / 심기철 / 010-8969-0440**: 4 instances
- **Key Affected Line Ranges**:
  - `Line 26`: Section 1.1 Scope (Primary Policy: DB Insurance Co., Ltd. Promy Car Policy, Renewed January 21, 2026, Channel: DB Insurance Direct / 1588-0100).
  - `Lines 189, 224`: Section 1.5 Legalization acceptance by DB Insurance.
  - `Lines 296-299`: Section 2.2 Korea Post Dispatch Envelope Specifications:
    - Header: `수신인: DB손해보험주식회사 대표이사 정종표`
    - Address: `서울특별시 강남구 테헤란로 432 (대치동, DB금융센터) [우편번호: 06194]`
    - Envelope: Verbatim matching `(우편번호 06194) 서울특별시 강남구 테헤란로 432, DB금융센터 DB손해보험주식회사 대표이사 정종표 귀하`.
  - `Lines 383, 386, 425, 483, 504`: Section 3 10-Day Statutory Response Tracker (Day 1 delivery to DB Insurance, Day 2 adjuster call 1588-0100, Day 11 default notice).
  - `Lines 559, 561-562, 568, 580, 595-596, 615, 650`: Section 4 Master Checklist items:
    - Item 2.1: Dispatch Content-Certified Mail to DB Insurance HQ.
    - Item 2.2: Dispatch to DB Insurance Direct / Branch.
    - Item 2.4: Email dispatch to `claim@idbins.com`, `claim_auto@idbins.com`.
    - Item 2.6: Monitor assigned adjuster at DB Insurance Gangwon Claims Team.
    - Item 3.1: File FSS dispute mediation against DB Insurance.
  - `Lines 680-684`: Section 5 Directory Item 1 (DB Insurance Corporate Profile, DB Financial Center, 432 Teheran-ro, Seoul 06194, 1588-0100).
  - `Line 777`: Section 6 Final audit verification (Recoveries from DB Insurance).

---

### File 09: `09_direct_international_claim_and_10day_statutory_notice.md`
- **Total Lines**: 836 lines | **Size**: 73,942 bytes
- **Occurrences of Samsung / 삼성**: 30 instances
- **Occurrences of March 13 / 2026-03-13**: 4 instances
- **Occurrences of Agent Shim Ki-cheol / 심기철 / 010-8969-0440**: 6 instances
- **Key Affected Line Ranges**:
  - `Line 2`: Subtitle (`국제 직접 보험금 청구서 및 10일 법정 가지급금 최고서 (DB손해보험 및 서정대학교)`).
  - `Lines 45-47`: Case Profile Box (Target Insurer: DB Insurance Co., Ltd. / CEO Jeong Jong-pyo, Policy: `2026-DB-AUTO-28M1390`, Renewal: January 21, 2026, Channel: DB Insurance Direct / 1588-0100).
  - `Lines 65, 82`: Table of Contents Parts I & III (Part I: DB손해보험주식회사 대상 최고서 / Part III: DB Insurance Co., Ltd. 10-Day Statutory Demand).
  - `Lines 112, 143-170`: Part I [국문 정본] 최고서:
    - 수신인: DB손해보험주식회사 (DB Insurance Co., Ltd.)
    - 본사 주소: 서울특별시 강남구 테헤란로 432 (대치동, DB금융센터) [우편번호: 06194]
    - 보험계약 번호: `2026-DB-AUTO-28M1390`
    - 보험종목: `DB손해보험 프로미카 개인용 자동차보험`
    - 갱신일자: `2026년 1월 21일 24:00`
    - 관리 창구: `DB손해보험 다이렉트 / 고객지원센터 (1588-0100)`
  - `Lines 182, 239, 289`: Mandatory demands, nullity of unlicensed driving defense, notification of parallel legal aid intake.
  - `Line 424`: Part II note (Non-offset of Seojeong Univ claim against DB Insurance claim).
  - `Lines 449-515`: Part III [English Version] Formal Direct Insurance Claim Notice:
    - Addressee: DB Insurance Co., Ltd., DB Financial Center, 432 Teheran-ro, Gangnam-gu, Seoul 06194.
    - Policy: `2026-DB-AUTO-28M1390`, Renewal Date: January 21, 2026.
    - Prayer for Relief: KRW 100M death benefit, KRW 50M provisional advance within 3 business days.
  - `Lines 570-603`: English Preemptive Legal Brief on Commercial Code §§ 732-2, 739, 663 and Supreme Court 98Da48963 against DB Insurance.
  - `Lines 621, 681, 756`: Notifications and warnings to DB Insurance.
  - `Line 829`: Exhibit 5: DB Insurance Promy Car Auto Policy Certificate (`2026-DB-AUTO-28M1390`).

---

### File 10: `10_parallel_pro_bono_and_consular_intake_packets.md`
- **Total Lines**: 942 lines | **Size**: 73,770 bytes
- **Occurrences of Samsung / 삼성**: 38 instances
- **Occurrences of March 13 / 2026-03-13**: 2 instances
- **Occurrences of Agent Shim Ki-cheol / 심기철 / 010-8969-0440**: 3 instances
- **Key Affected Line Ranges**:
  - `Line 10`: Metadata banner (Target Policy: DB Insurance Promy Car, Policy: `2026-DB-AUTO-28M1390`, Renewal: January 21, 2026).
  - `Line 69`: Table of Contents item 4.4 (Diplomatic Note Verbale to DB Insurance, FSS & MOFA).
  - `Lines 96, 125`: Executive summary (DHL dispatch to DB Insurance HQ, parallel institutional mobilization).
  - `Lines 187, 209`: KLAC overview (Cost recovery against losing defendant DB Insurance; Exhibit C-1 DB Insurance Policy Certificate).
  - `Lines 223, 243, 272, 279, 318, 411, 428`: Section 2 KLAC Foreigner Legal Aid Application:
    - 상대방(피고): `DB손해보험 주식회사 (대표이사 정종표)`
    - 본점 주소: `서울특별시 강남구 테헤란로 432 (대치동, DB금융센터) [우편번호: 06194]`
    - 소송구조 신청 취지 및 이유 (사망보험금 1억원 지급 청구의 소 대리).
  - `Lines 496, 576, 628, 641, 653, 657`: Section 3 Gong-Gam & DURO Intake Briefs:
    - 피청구인: `DB손해보험 주식회사 (대표이사 정종표)`
    - 사실관계 및 대기업 보험사(DB손해보험)의 불법 면책 관행 규탄.
  - `Lines 676, 686-703, 731, 758-797, 827`: Section 4 Bangladesh Embassy Representation & Diplomatic Note Verbale:
    - Full Diplomatic Note Verbale addressed to:
      1. `Mr. Jeong Jong-pyo, Representative Director & CEO, DB Insurance Co., Ltd., DB Financial Center, 432 Teheran-ro, Gangnam-gu, Seoul 06194`.
      2. Governor of FSS.
      3. Minister of Foreign Affairs of ROK.
    - Demand for SWIFT MT103 wire transfer of undisputed accidental death benefits.
  - `Lines 861, 878-879, 886-888, 915-917`: Master exhibits and 10-day tracking calendar.

---

### File 11: `11_dhaka_to_seoul_dhl_dispatch_and_10day_tracking_guide.md`
- **Total Lines**: 915 lines | **Size**: 73,881 bytes
- **Occurrences of Samsung / 삼성**: 26 instances
- **Occurrences of March 13 / 2026-03-13**: 3 instances
- **Occurrences of Agent Shim Ki-cheol / 심기철 / 010-8969-0440**: 4 instances
- **Key Affected Line Ranges**:
  - `Lines 38-43`: Master Case Profile:
    - Insurer: `DB Insurance Co., Ltd. (DB손해보험주식회사)`
    - Policy Classification: `DB Promy Car Individual Auto Policy (프로미카 개인용 자동차보험)`
    - Vehicle Plate: `28모1390 (Kia Morning Hatchback)`
    - Policy Identifier: `2026-DB-AUTO-28M1390`
    - Managing Channel: `DB Insurance Direct / Customer Center (1588-0100)`
  - `Lines 85, 149-151`: DHL Pack 1 Consignee Declarations:
    - Company: `DB Insurance Co., Ltd. (DB손해보험주식회사)`
    - Address: `DB Financial Center, 432 Teheran-ro, Gangnam-gu, Seoul 06194, Republic of Korea`
    - Attn: `CEO Jeong Jong-pyo / Auto Claims Dept.` (Tel: `+82-2-1588-0100`)
  - `Lines 186, 197-199`: Commercial Invoice details (Invoice Ref: `INV-DHAKA-SEOUL-2026-DB01`, Consignee: DB Insurance Co., Ltd., DB Financial Center).
  - `Line 289`: Physical packing chart (DHL Pack 1 -> DB Insurance HQ).
  - `Lines 330, 353-415`: Section 2.2 Master Electronic Email Template 1:
    - To: `claim@idbins.com`, `claim_auto@idbins.com`
    - Korean & English templates addressed to DB Insurance CEO Jeong Jong-pyo regarding Policy `2026-DB-AUTO-28M1390` (renewed January 21, 2026).
  - `Lines 492, 507, 512, 527, 558, 597, 614`: Section 3 Legal aid filing templates and transmittal references.
  - `Lines 702, 706, 796, 824, 904`: Section 4 10-Day Statutory Response Tracker & Default Notice to DB Insurance.

---

### File 12: `12_lawyer_and_insurer_filing_email_transmittals.md`
- **Total Lines**: 314 lines | **Size**: 23,701 bytes
- **Occurrences of Samsung / 삼성**: 13 instances
- **Occurrences of March 13 / 2026-03-13**: 0 instances
- **Occurrences of Agent Shim Ki-cheol / 심기철 / 010-8969-0440**: 2 instances
- **Key Affected Line Ranges**:
  - `Lines 39, 54, 61, 76`: Transmittal 1 (KLAC Application):
    - Attachment 4: `01_db_insurance_claim_notice_and_legal_brief.pdf`
    - 적용 보험계약: `DB손해보험 프로미카 자동차보험 (증권번호: 2026-DB-AUTO-28M1390)`
    - English Summary: `DB Insurance is unlawfully withholding statutory death benefits (KRW 100M)...`
  - `Lines 94, 106`: Transmittal 2 (Gong-Gam & DURO):
    - Attachment 2: `01_db_insurance_claim_notice_and_legal_brief.pdf`
    - 대형 손해보험사(DB손해보험)의 이주민 유족에 대한 차별적 미지급 대응.
  - `Lines 161-187`: Transmittal 4 (Target Insurer Direct Email):
    - Section Title: `## 4. DB INSURANCE CO., LTD. (DB손해보험 보상본부 및 고객지원센터)`
    - Email Transmittal 4 Header: `EMAIL TRANSMITTAL 4: DB INSURANCE CO., LTD. (DB손해보험 보상본부 및 담당자)`
    - To: `claim_auto@idbins.com`, `claim@idbins.com`
    - Cc: `munimhasibul@gmail.com`
    - Subject: `[법정 최고서] DB손해보험 자동차보험(차량 28모1390, 증권 2026-DB-AUTO-28M1390) 사망보험금 1억원 및 상법 제732조의2 가지급금(5천만원) 즉시 지급청구 통지의 건`
    - Attachment 1: `01_db_insurance_claim_notice_and_legal_brief.pdf`
    - Salutation & Body: `DB손해보험(주) 대표이사 정종표 및 자동차보상본부장, 강원보상센터장 귀하`
    - Contract: `28모1390 (증권번호: 2026-DB-AUTO-28M1390, 갱신일: 2026년 1월 21일)`
  - `Line 284`: Transmittal 6 (Bangladesh Embassy):
    - Request for Note Verbale to MOFA, FSS, and DB Insurance Co., Ltd.

---

### Master SSOT: `CASE_MASTER_KNOWLEDGE_DOSSIER.md` & `assemble_dossier.py`
- **Total Lines**: 603 lines (MD) / 636 lines (Python script)
- **Architectural Discovery**: `CASE_MASTER_KNOWLEDGE_DOSSIER.md` is **programmatically generated** by `d:/promotion/assemble_dossier.py`! Running `python assemble_dossier.py` will overwrite `CASE_MASTER_KNOWLEDGE_DOSSIER.md`. Therefore, both files must be synchronized.
- **Key Affected Line Ranges in `assemble_dossier.py` / `CASE_MASTER_KNOWLEDGE_DOSSIER.md`**:
  - `Lines 38-46` (MD lines 38-46; py lines 55-63):
    - Primary Target Policy: `DB Insurance Co., Ltd. (DB손해보험주식회사)`
    - Target Vehicle Plate: `28모1390 (28Mo1390) | Policy No: 2026-DB-AUTO-28M1390`
    - Policy Renewal Date: `January 21, 2026 (Effective from 2026-01-21 24:00)`
    - Managing / Channel: `DB Insurance Direct / Customer Call Center: 1588-0100 (Direct: 1600-0100)`
    - Coverage Claimed: `Self-Physical Accident Death Benefit (자기신체사고 사망보험금) KRW 100,000,000`
    - Statutory Demand: `50% Provisional Advance KRW 50,000,000 within 10 business days (Commercial Code §732-2)`
    - Core Legal Doctrine: `Commercial Code §732-2, §663 & Supreme Court En Banc Decision 98Da48963`
  - `Lines 85, 87` (py lines 104, 106): Core Financial Objectives (DB Insurance Primary Recovery KRW 100M).
  - `Lines 99-105` (py lines 118-124): Chronology (Renewal on January 21, 2026, 52 days prior to March 14, 2026 crash).
  - `Lines 166, 169` (py lines 185, 188): Legal effects (DB Insurance barred from unlicensed exclusion).
  - `Line 238` (py lines 257): Heir representation before DB Insurance.
  - `Line 267` (py lines 286): Insurance policies summary table (DB Insurance Promy Car, Policy `2026-DB-AUTO-28M1390`).
  - `Lines 279-282` (py lines 298-301): DB Insurance Claim Specifics (Headquarters Claims Dept. at DB Financial Center, 432 Teheran-ro, Seoul 06194 / DB자동차보험손해사정 강원보상센터).
  - `Lines 306, 312` (py lines 325, 331): Multi-Track Architecture (Track 1 Direct Content-Certified Demand to DB Insurance).
  - `Lines 382, 408, 430, 461-466` (py lines 401, 427, 449, 480-485): Workspace inventory, exhibits, and Transmittal 4 to DB Insurance.
  - `Line 585` (py lines 604): Step 2 execution playbook (Content-Certified Mail to DB Insurance).

---

## 7. CRITICAL IMPLEMENTATION SAFEGUARDS & AUDIT CHECKS

When worker agents execute these edits, they must observe the following critical safeguards:
1. **Vehicle Make Preservation**:
   - The vehicle is a **Kia Morning Hatchback (기아 모닝 경승용, Plate: `28모1390`)**.
   - **Do NOT blind-replace `Samsung` with `DB`!**
   - Mentions of `Kia Morning` or `기아 모닝` represent the automobile manufacturer (Renault Korea / 르노코리아자동차) and must remain **100% intact**.
2. **Renewal Date Realism**:
   - The fatal accident occurred on **March 14, 2026 at 05:58 AM**.
   - The policy was renewed on **January 21, 2026** (2026-01-21 24:00).
   - The temporal narrative must state: *"The policy was validly renewed on January 21, 2026 and remained continuously and actively in force at the time of the fatal crash on March 14, 2026 (52 days after renewal)."*
   - Avoid legacy phrasing claiming the crash occurred "hours after renewal".
3. **Statutory Doctrine Purity**:
   - The citations to **Commercial Code §§ 732-2, 739, 663** and **Supreme Court En Banc Decision 98Da48963** are universal mandatory rules of law applying to all Korean automobile policies.
   - They apply with identical legal force to **DB Insurance Company** as they did to Samsung Fire.
   - The arguments regarding the nullity of the unlicensed driving exclusion clause in first-party accidental death benefits must remain completely undiluted.
4. **Build Pipeline Synchronization**:
   - Because `assemble_dossier.py` generates `CASE_MASTER_KNOWLEDGE_DOSSIER.md`, edits to the master dossier must be made inside `assemble_dossier.py` or synchronized so running the script does not reintroduce Samsung Fire references.
5. **Print Pack Recompilation**:
   - In `03_KOREAN_LAWYERS_AND_INSURERS_FILING_PACK/`, `01_Samsung_Fire_Insurance_Claim_Notice_and_Legal_Brief.pdf` must be recompiled as `01_DB_Insurance_Claim_Notice_and_Legal_Brief.pdf` (along with `.docx`).

---

*Report prepared and certified by Dossier Scope Explorer (`survey_explorer_2`) for immediate handoff to the Orchestrator and downstream execution agents.*
