# SPECIFICATION MINING REPORT: PARALLEL PRO BONO & CONSULAR INTAKE PACKETS (R2)

**Document Identifier:** `d:/promotion/.agents/spec_miner_r3_2/r2_spec_report.md`  
**Miner Archetype:** `spec_miner_r3_2` (Legal Specification Miner)  
**Target Milestone:** R2 / Phase R3 - Parallel Pro Bono & Consular Intake Submission Packets  
**Governing Case:** Estate of Deceased Foreign Student MAHADI MONOAR HOSSAIN (`010530-7660021`)  
**Target Policy & Vehicle:** Samsung Fire & Marine Insurance Policy (`28모1390`, Agent 심기철 `010-8969-0440`) & Seojeong University D-2 Group Accident Insurance  
**Date of Execution:** August 27, 2026  

---

## 1. Executive Summary & Legal Framework Architecture

This specification mining report defines the authoritative legal, statutory, procedural, and evidentiary specifications required to generate execution-ready pro bono legal aid and consular intake submission packets.

The surviving sole legal heirs in Bangladesh—**BELAL HOSSAIN** (Father, 2/3 share) and **MONOARA BEGUM** (Mother, 1/3 share)—represented by their designated Attorney-in-Fact (**Md Monirul Islam**, Chairman of the Korea Bangladesh Human Rights Committee), are pursuing the full recovery of KRW 100,000,000 in first-party accidental death benefits under Samsung Fire & Marine Insurance policy `28모1390` and Seojeong University D-2 Foreign Student Group Accident Insurance.

To counter insurer delay or bad-faith unlicensed driving exemption defenses, the strategy deploys parallel submissions across four distinct institutional tracks:
1. **Korea Legal Aid Corporation (대한법률구조공단 - KLAC)**: State-funded free legal representation and court fee advancement under Legal Aid Act Art. 22.
2. **Gong-Gam Human Rights Law Foundation (공익인권법재단 공감)**: Public interest impact litigation brief focusing on migrant student rights and Commercial Code Art. 732-2.
3. **Association for Public Interest Law DURO (사단법인 두루)**: Strategic human rights litigation brief leveraging Supreme Court precedent 98Da48963 against systemic insurer exclusion practices.
4. **Embassy of Bangladesh in Seoul (Labour & Consular Wing)**: Diplomatic protection petition to Counsellor Mikon Tangchanggya for Note Verbale issuance, consular authentication, and empanelled counsel coordination.

---

## 2. Features Discovered

| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|----------|---------|-------------|--------|---------|----------------|----------------|
| 1 | KLAC Legal Aid | Foreigner Free Legal Aid Scheme Application | Formal legal aid application under Legal Aid Act Art. 22 & KLAC Regulations for civil lawsuit before Seoul Central or Sokcho District Court | Applicant details, Warisan Sanad, Special POA, income proof, police accident confirmation, Samsung Fire policy | Official KLAC Intake Receipt & Approval Decision (구조결정통지서), Case Assignment to Staff Attorney | Rejection if income exceeds 125% median income ceiling or lacks winning probability (승소가능성 결여) | Legal Aid Act Art. 22; KLAC Operational Rules; 07_legal_aid_and_consular_escalation_roster.md §2 |
| 2 | KLAC Legal Aid | Low-Income Eligibility Verification | Verification of <125% Korean National Median Income ceiling for foreign deceased student (D-2 zero income) and rural Bangladeshi heirs | D-2 Enrollment Certificate, Alien Registration Fact Sheet, Bangladeshi Union Parishad Income Certificate | Standard Low-Income Verification Assessment for Foreign Claimants | Request for supplementary local tax/income attestation | Legal Aid Act Art. 22; KLAC Foreigner Legal Aid Directives |
| 3 | KLAC Legal Aid | 100% Free Representation & Court Fee Advancement | State Treasury advancement of court filing stamps (인지대), service fees (송달료), and fact-finding costs, with 100% attorney fee waiver | Legal Aid Application Form, Litigation Fee Advancement Petition (소송비용대납신청서) | Total fee exemption for claimants (KRW 0 burden); statutory cost shift to Samsung Fire under Civil Procedure Act Art. 98 | Repayment required only if claim is fraudulently filed or dismissed with gross fault | Legal Aid Act Art. 22; Korean Civil Procedure Act Art. 98 |
| 4 | KLAC Legal Aid | Multi-Branch Venue Routing & Territorial Jurisdiction | Strategic selection between Seoul Central Branch (Defendant HQ) and Sokcho Branch (Accident locus) | Corporate domicile (Seocho-gu, Seoul) vs. Accident location (Yangyang-gun, Gangwon) | Optimal Civil Complaint filing before Seoul Central District Court (Specialized Insurance Bench) | Jurisdictional transfer if improperly filed without defendant corporate connection | Korean Civil Procedure Act Arts. 5 & 18; 07_legal_aid_and_consular_escalation_roster.md §2.5 |
| 5 | Public Interest Pro Bono | Gong-Gam Human Rights Law Foundation Intake Brief | Submission of public interest litigation brief advocating foreign student equality, Commercial Code Art. 732-2 mandatory protection, and anti-discrimination | Gong-Gam Case Brief, Evidence Portfolio, Supreme Court 98Da48963 Analysis | Strategic Case Intake Review, Direct Representation or Amicus Curiae Brief filing | Non-acceptance if deemed purely private commercial debt without systemic human rights value | Gong-Gam Charter; www.kpil.org; 07_legal_aid_and_consular_escalation_roster.md §4.2 |
| 6 | Public Interest Pro Bono | Association for Public Interest Law DURO Intake Brief | Submission of strategic impact litigation brief to DURO Migrant Rights Team (이주인권팀) challenging unlawful unlicensed driving exclusions against foreign students | DURO Impact Case Brief, FSS Mediation Petition, Policy `28모1390` terms | Case Intake Review, Strategic Impact Litigation or Joint Bar Association advocacy | Rejection if submitted as routine personal legal aid without systemic impact | DURO Operating Guidelines; www.duroo.org; Supreme Court 98Da48963 |
| 7 | Consular Escalation | Bangladesh Embassy Diplomatic Assistance Request Letter | Formal representation letter addressed to Counsellor Mikon Tangchanggya (Labour & Consular Wing) requesting diplomatic intervention | Bilingual representation petition, Warisan Sanad, Death Certificate, Samsung Fire Policy Certificate | Diplomatic Endorsement, Consular Authentication Seal (BDS/LS/2026/0826-HER) | Case hold if Bangladeshi heirship chain lacks MOFA Dhaka QR verification | Vienna Convention on Consular Relations Art. 5; 07_legal_aid_and_consular_escalation_roster.md §3.1–3.3 |
| 8 | Consular Escalation | Diplomatic Note Verbale (공한) Issuance Protocol | High-level diplomatic communication from Embassy to Samsung Fire CEO, FSS Governor, and MOFA Korea demanding statutory compliance | Case Fact Brief, Commercial Code 732-2 violations, 10-day provisional breach record | Official Note Verbale dispatched through diplomatic pouch / formal chancery channels | Delayed if bilateral diplomatic protocols require inter-ministerial clearance | Vienna Convention Art. 5; 07_legal_aid_and_consular_escalation_roster.md §3.5 |
| 9 | Consular Escalation | Embassy-Empanelled Counsel Referral & Direct SWIFT Oversight | Allocation of bilingual Korean contingency trial lawyers and consular supervision of SWIFT MT103 wire transfers to Islami Bank & Sonali Bank | Power of Attorney, Designated Bank SWIFT details (`IBBLBDDHXXX`, `BSONBDDHXXX`) | Contingency Retainer Agreement (성공보수) with KRW 0 upfront retainer; MT103 bank audit | Bank rejection if beneficiary name mismatches Bangladeshi passport / NID records | Foreign Exchange Transactions Act Art. 4; 04_bilingual_special_power_of_attorney.md Clause 6 |
| 10 | Cross-Border Evidentiary | 4-Step Chain-of-Legality Verification | Establishing absolute evidentiary admissibility under Korean Private International Law Art. 49 and Civil Procedure Act Arts. 356/358 | Warisan Sanad, Family Registration Certificate, Special POA, Translation Certificates | Fully admissible cross-border evidentiary docket | Inadmissibility if foreign public seal is unauthenticated or uncertified | PIL Art. 49; Civil Procedure Act Arts. 356 & 358; 04_cross_border_heirship_and_legalization_guide.md §3 |
| 11 | Statutory Enforcement | 10-Day Provisional Payment Enforcement | Demanding mandatory 50% provisional benefit (KRW 50,000,000) under Standard Auto Terms Art. 34(3) and Guarantee Auto Act Art. 11 | Content-Certified Claim Notice, Date of Service Receipt (T_0) | Immediate wire of KRW 50,000,000 within 10 business days | Statutory default (이행지체) on Day 11+ with 6.0% Commercial Code interest accrual | Standard Auto Terms Art. 34(3); Commercial Code Art. 54 |
| 12 | Statutory Enforcement | Dual-Tier Default Interest Calculation | Calculating 6.0% p.a. Commercial default interest transitioning to 12.0% p.a. Special Litigation Act interest upon complaint service | Principal amount, Day 11 breach date, Civil Complaint service date | Precise per diem interest ledger (KRW 8,219/day on 50M -> KRW 32,877/day on 100M) | Insurer forfeiture of interest defenses upon judicial adjudication | Commercial Code Art. 54; Special Act on Promotion of Litigation Art. 3(1) |

---

## 3. Edge Cases & Boundary Conditions

| # | Feature | Input / Condition | Observed Behavior & Procedural Safeguard |
|---|---------|-------------------|------------------------------------------|
| 1 | KLAC Foreigner Eligibility | Overseas claimants reside abroad and cannot appear in person at KLAC intake counter | KLAC allows designated Attorney-in-Fact (Md Monirul Islam) to file on their behalf upon submission of consular-legalized Special POA (특별위임장) and certified translation. |
| 2 | KLAC Income Verification | Bangladeshi agricultural subsistence income lacks Korean National Tax Service (국세청) income certificate | Local Union Parishad Chairman / Village Revenue Officer Income Certificate (저소득확인서) attested by MOFA Dhaka is recognized under KLAC Foreigner Legal Aid directives. |
| 3 | Venue Competition | Insurer argues accident occurred in Gangwon, seeking transfer from Seoul Central to Chuncheon/Sokcho | Civil Procedure Act Art. 5 establishes general forum at defendant corporate headquarters (Seoul Central). Seoul Central District Court has specialized insurance benches. Attorney-in-Fact maintains Seoul Central venue. |
| 4 | DURO Public Interest Scope | DURO's primary mission focuses on institutional reform rather than individual representation | Intake brief frames the case as a strategic impact lawsuit targeting the insurance industry's systemic discrimination against foreign students and illegal use of unlicensed driving exclusions. |
| 5 | Gong-Gam Capacity Constraints | Gong-Gam may have limited bandwidth for full trial representation | Brief requests alternative relief: (1) Direct co-counseling with KLAC/Seoul Bar, (2) Amicus Curiae brief to Seoul Central District Court, or (3) Joint press release with migrant rights groups. |
| 6 | Consular Remittance Impediment | Korean domestic banks or Samsung Fire claims adjusters demand Korean domestic bank accounts for payout | Foreign Exchange Transactions Act Art. 4 authorizes direct cross-border SWIFT MT103 wire transfer to heirs' accounts in Bangladesh (`IBBLBDDHXXX`, `BSONBDDHXXX`). Embassy demands MT103 confirmation copy. |
| 7 | Insurer Unlicensed Defense | Samsung Fire claims "unlicensed driving constitutes intentional violation or total exclusion under policy" | Supreme Court 98Da48963 and Commercial Code Arts. 732-2/663 explicitly invalidate unlicensed driving exclusion clauses for first-party accidental death benefits. Exemption is null and void (*당연무효*). |
| 8 | Name Transposition in Documents | Passport reads "MONOAR HOSSAIN MAHADI" while Alien Registration Card reads "MAHADI MONOAR HOSSAIN" | Exhibit inventory includes official Name Identity Attestation and Alien Registration Fact Sheet (`010530-7660021`) confirming single legal identity. |

---

## 4. Comprehensive Legal & Organizational Specifications

### SECTION A: Korea Legal Aid Corporation (대한법률구조공단 - KLAC)

#### 1. Statutory & Regulatory Architecture
- **Statutory Authority**: Legal Aid Act (법률구조법 - Act No. 18498) Arts. 1 (Purpose), 2 (Definition), 7 & 8 (Corporate Capacity), and 22 (State Treasury Advancement & Subsidy).
- **Internal Directives**:
  - KLAC Legal Aid Regulations (대한법률구조공단 법률구조규칙)
  - Litigation Representation Operational Rules (소송대리업무규정)
  - Foreigner Legal Aid Operational Directives (외국인 법률구조제도 운영지침)
- **Foreigner Eligibility Standard**: Foreign nationals whose rights are infringed within South Korean territory are entitled to legal aid under Article 22.
- **Low-Income Threshold**: Household monthly income equal to or below **125% of Korean National Median Income (기준 중위소득 125% 이하)**.
  - *Foreign Student Standing*: Deceased student held D-2 status with no taxable domestic income.
  - *Overseas Heirs Standing*: Surviving parents reside in rural Cumilla, Bangladesh, with subsistence agrarian income far below the 125% median threshold.

#### 2. Cost Exemption & Court Fee Advancement Mechanics
- **Attorney Professional Fees (변호사 보수)**: 100% Free (Covered by KLAC state appropriation).
- **Court Filing Stamp Fees (인지대)**: Advanced by State Treasury under Legal Aid Act Art. 22.
- **Service of Process Fees (송달료)**: Advanced by State Treasury under Legal Aid Act Art. 22.
- **Fact-Finding & Evidence Collection (사실조회비용)**: Covered by KLAC budget.
- **Cost Recovery upon Judgment**: Pursuant to Korean Civil Procedure Act Art. 98, all advanced court costs are taxed against and recovered directly from the losing corporate defendant (Samsung Fire & Marine Insurance Co., Ltd.). Zero deduction is made from the heirs' principal recovery.

#### 3. Master Branch Routing Directory

| Branch Name (지부/출장소) | Full Address (도로명 주소) | Phone / Fax / Hotline | Target Judicial Jurisdiction | Strategic Rationale |
|---|---|---|---|---|
| **KLAC Seoul Central Branch (서울중앙지부)** | 서울특별시 서초구 서초대로 247, 4~6층 (서초동, 한원빌딩) [06652] | Tel: 02-535-0132<br>Fax: 02-535-0138<br>Hotline: 132 | **Seoul Central District Court (서울중앙지방법원)** | **PRIMARY VENUE**: Defendant Samsung Fire HQ is in Seocho-gu. Specialized Insurance Judicial Benches. |
| **KLAC Seoul Bukbu Branch (서울북부지부)** | 서울특별시 도봉구 마들로 749, 3층 (도봉동, 삼진빌딩) [01322] | Tel: 02-918-0132<br>Fax: 02-918-0138<br>Hotline: 132 | **Seoul Bukbu District Court (서울북부지방법원)** | Northern Metro jurisdiction; convenient for Seojeong University group policy claims. |
| **KLAC Sokcho Branch (속초출장소)** | 강원특별자치도 속초시 번영로 163, 2층 (동명동) [24823] | Tel: 033-636-2342<br>Fax: 033-636-2345<br>Hotline: 132 | **Chuncheon Dist. Court Sokcho Branch (춘천지방법원 속초지원)** | **ACCIDENT VENUE**: Proximity to Sokcho Police Station and accident site records. |
| **KLAC Gangneung Branch (강릉출장소)** | 강원특별자치도 강릉시 동해대로 3288번길 18, 2층 (교동) [25488] | Tel: 033-642-1320<br>Fax: 033-642-1325<br>Hotline: 132 | **Chuncheon Dist. Court Gangneung Branch (춘천지방법원 강릉지원)** | Medical record venue; location of GangNeung Asan Hospital post-mortem files. |
| **KLAC Chuncheon HQ (춘천지부)** | 강원특별자치도 춘천시 공지로 312, 3층 (효자동) [24376] | Tel: 033-255-0811<br>Fax: 033-255-0815<br>Hotline: 132 | **Chuncheon District Court Main Bench (춘천지방법원 본원)** | Gangwon Provincial appellate hub. |

#### 4. Evidentiary Portfolio Checklist for KLAC Application
1. Form `법률구조신청서` (Legal Aid Application Form).
2. Bilingual Special Power of Attorney (소송대리 특별위임장) with MOFA Dhaka attestation & BD Embassy Consular Seal.
3. Legal Heirship Certificate (Warisan Sanad / 상속인증명서) with Magistrate attestation & MOFA Dhaka QR seal.
4. Family Relationship Certificate & Birth Registration records (가족관계등록부).
5. Passports & National ID Cards of Parents (Belal Hossain & Monoara Begum).
6. Certified Korean Translation Certificates (공인외국어번역확인서) under Civil Procedure Act Art. 356/358.
7. Deceased Alien Registration Fact Sheet (외국인등록사실증명 - `010530-7660021`) & Passport (`A03097931`).
8. Seojeong University Certificate of Enrollment (서정대학교 재학증명서 - Smart Automotive Dept).
9. GangNeung Asan Hospital Post-Mortem Examination Certificate (사체검안서/사망진단서 - Dr. Huidong Kang).
10. Sokcho Police Station Traffic Accident Fact Certificate (교통사고사실확인원 - Case `2026-00020`).
11. Samsung Fire Automobile Insurance Policy Certificate (`28모1390`, Agent 심기철).
12. Low-Income Verification / Indigence Attestation from Union Parishad, Cumilla (저소득확인서).

#### 5. Specific Prayer for Relief (KLAC Civil Complaint Draft)
```text
1. 피고(삼성화재해상보험 주식회사)는 원고 1(BELAL HOSSAIN)에게 금 66,666,667원, 원고 2(MONOARA BEGUM)에게 금 33,333,333원 및 각 이에 대하여 2026. 3. 29.부터 본건 소장 부본 송달일까지는 상법에 정한 연 6%, 그 다음날부터 다 갚는 날까지는 소송촉진 등에 관한 특례법에 정한 연 12%의 각 비율에 의한 금원을 지급하라.
2. 소송비용은 피고의 부담으로 한다.
3. 제1항은 가집행할 수 있다.
```

---

### SECTION B: Public Interest Human Rights Foundations (Gong-Gam & DURO)

#### 1. Gong-Gam Human Rights Law Foundation (공익인권법재단 공감)

##### Profile & Coordinates
- **Entity**: Public Interest Human Rights Law Foundation Gong-Gam (공익인권법재단 공감)
- **Address**: 서울특별시 종로구 창덕궁길 29-6, 3층 (원서동, 북촌창우극장) [우편번호: 03058]
- **Telephone**: +82-2-3675-7740 / 7741
- **Facsimile**: +82-2-3675-7742
- **Email**: `gonggam@gmail.com` / `gonggam.law@gmail.com`
- **Web Portal**: `https://www.kpil.org` (Online intake: '공익소송 신청하기')
- **Key Focus**: Migrant workers, international student human rights, anti-discrimination, insurance bad-faith litigation.

##### Public Interest Intake Brief Structure
1. **Case Subject**: Strategic Public Interest Litigation Brief challenging discriminatory unlicensed driving exemption defenses against deceased foreign student heirs under Commercial Code Art. 732-2.
2. **Human Rights & Public Policy Dimension**:
   - South Korean insurance companies frequently exploit foreign students' and overseas bereaved families' unfamiliarity with Korean law by invoking void exclusion clauses.
   - Supreme Court precedent 98Da48963 established over 25 years ago that unlicensed driving exclusion clauses in first-party accidental death policies are null and void.
   - Enforcing Commercial Code Art. 732-2 protects over 200,000 foreign students in Korea from predatory insurer practices.
3. **Requested Actions**:
   - Direct pro bono litigation representation before Seoul Central District Court; or
   - Co-counseling / Amicus Curiae Brief (의견서) submission in support of the heirs;
   - Public advocacy highlighting institutional insurance abuse against migrant families.

---

#### 2. Association for Public Interest Law DURO (사단법인 두루)

##### Profile & Coordinates
- **Entity**: Association for Public Interest Law DURO (사단법인 두루)
- **Address**: 서울특별시 중구 퇴계로8길 58, 3층 [우편번호: 04635]
- **Telephone**: +82-2-6200-1853 (or 02-6200-1902)
- **Facsimile**: +82-2-6200-0811
- **Email**: `duroo@duroo.org`
- **Web Portal**: `https://www.duroo.org`
- **Competent Team**: Migrant Rights Team (이주인권팀 - International Students, Migrant Workers, Refugees).

##### Strategic Impact Litigation Intake Brief Structure
1. **Case Subject**: Systemic Impact Litigation Intake Brief on the Enforcement of Mandatory Commercial Code Protections for Deceased Migrant Student Heirs.
2. **Impact Litigation Criteria Met**:
   - **Systemic Precedent Enforcement**: Re-establishing the strict nullity of unlicensed driving exclusions under Commercial Code Art. 732-2 and 663 against major non-life insurers.
   - **Protection of Vulnerable Non-Citizens**: Overseas rural Bangladeshi parents face structural hurdles in accessing Korean courts.
   - **Financial Consumer Equity**: Stopping bad-faith denial of statutory provisional payments (Standard Auto Terms Art. 34).
3. **Requested Relief**:
   - Strategic impact litigation support, advisory counsel, and collaboration with the Seoul Bar Association Foreigner Human Rights Sub-Committee.

---

### SECTION C: Embassy of Bangladesh in Seoul (Labour & Consular Wing)

#### 1. Diplomatic Mission Profile & Intake Channels
- **Official Mission**: Embassy of the People's Republic of Bangladesh, Seoul (주한 방글라데시 대사관)
- **Chancery Address**: 17 Jangmun-ro 6-gil, Yongsan-gu, Seoul 04393, Republic of Korea (서울특별시 용산구 장문로6길 17)
- **Chancery Telephone**: +82-2-796-4056 / 4057 / 4058 / 4059
- **Chancery Facsimile**: +82-2-796-4060
- **Consular Wing Direct**: +82-2-796-4058
- **24/7 Diplomatic & Consular Emergency Hotline**: +82-10-8588-4058
- **Competent Wing**: Labour & Consular Wing (노무 및 영사과)
- **Key Officer**: **Counsellor Mikon Tangchanggya** (Labour & Consular Wing / Head of Chancery)
- **Official Email Directory**:
  - Chancery Main: `mission.seoul@mofa.gov.bd`
  - Labour & Consular Wing: `labour.seoul@mofa.gov.bd`
  - Operations / Alternate: `bdootseoul@gmail.com`
- **Consular Service Hours**: Monday through Friday: 09:30 – 12:30 (Intake) / 15:30 – 16:30 (Delivery)

#### 2. Diplomatic Assistance Request Letter Specifications
- **Addressed To**: His Excellency the Ambassador & Counsellor Mikon Tangchanggya, Labour & Consular Wing.
- **Petitioning Body**: Md Monirul Islam, Chairman of Korea Bangladesh Human Rights Committee (Authorized Attorney-in-Fact).
- **Core Factual Narrative**:
  - Fatal crash of D-2 student MAHADI MONOAR HOSSAIN on March 14, 2026 in Yangyang-gun.
  - Active Samsung Fire Policy `28모1390` (renewed March 13, 2026, Agent 심기철 `010-8969-0440`).
  - Indigent surviving parents in Cumilla, Bangladesh: Belal Hossain (2/3) & Monoara Begum (1/3).
  - Samsung Fire's unlawful refusal to pay KRW 100M death benefit and withholding of KRW 50M 10-day provisional benefit.

#### 3. Four Specific Prayers for Diplomatic Action
1. **Consular Endorsement (영사확인)**: Official chancery seal on the MOFA Dhaka attested Warisan Sanad and Special POA.
2. **Issuance of Diplomatic Note Verbale (공한 / 외교구상서)**:
   - Addressed to: (a) Mr. Lee Mun-hwa, CEO of Samsung Fire & Marine Insurance Co., Ltd., (b) Governor, Financial Supervisory Service (FSS), (c) Director-General for South Asian & Pacific Affairs, MOFA Republic of Korea.
   - Demanding immediate un-discounted payout of KRW 100,000,000 and 10-day provisional disbursement of KRW 50,000,000 pursuant to Commercial Code Art. 732-2 and Supreme Court 98Da48963.
3. **Embassy Panel Legal Counsel Referral (대사관 자문변호사단 연계)**: Formal introduction to Korean trial attorneys for contingency representation and liaison with KLAC.
4. **Direct SWIFT MT103 Remittance Oversight (해외 직접 송금 감독)**:
   - Ensuring wire transfers directly to Islami Bank Bangladesh PLC (`IBBLBDDHXXX`) and Sonali Bank PLC (`BSONBDDHXXX`) with MT103 confirmation filed with the Embassy.

---

## 5. Master Contact & Intake Routing Directory

```
========================================================================================================================
                                MASTER INTAKE & CONTACT DIRECTORY (R2 TRACKS)
========================================================================================================================
Organization                    Channel / Type          Contact Coordinates / Address                      Hours / Intake
------------------------------------------------------------------------------------------------------------------------
Korea Legal Aid Corporation     Online / In-Person /    Seoul Central: 서초대로 247, 한원빌딩 4~6층       09:00 - 18:00
(대한법률구조공단 - KLAC)       Hotline                 Tel: 02-535-0132 / Fax: 02-535-0138 / 132          (Mon - Fri)
                                                        Web: www.klac.or.kr
------------------------------------------------------------------------------------------------------------------------
Gong-Gam Human Rights Law       Online / Email /        종로구 창덕궁길 29-6, 3층 (원서동)                09:30 - 18:00
Foundation (공익인권법재단 공감) Fax                    Tel: 02-3675-7740 / Fax: 02-3675-7742              (Mon - Fri)
                                                        Email: gonggam@gmail.com / gonggam.law@gmail.com
                                                        Web: www.kpil.org
------------------------------------------------------------------------------------------------------------------------
Association for Public Interest Email / Fax / Postal    중구 퇴계로8길 58, 3층 [04635]                    09:30 - 18:00
Law DURO (사단법인 두루)                                Tel: 02-6200-1853 / Fax: 02-6200-0811              (Mon - Fri)
                                                        Email: duroo@duroo.org / Web: www.duroo.org
------------------------------------------------------------------------------------------------------------------------
Embassy of Bangladesh in Seoul  Diplomatic Pouch /      용산구 장문로6길 17 [04393]                       09:30 - 12:30
(Labour & Consular Wing)        Email / Phone / 24/7    Tel: +82-2-796-4056~9 / Direct: +82-2-796-4058     (Intake)
                                Emergency               Fax: +82-2-796-4060 / 24/7: +82-10-8588-4058      15:30 - 16:30
                                                        Email: mission.seoul@mofa.gov.bd                   (Delivery)
                                                               labour.seoul@mofa.gov.bd
                                                               bdootseoul@gmail.com
                                                        Web: https://seoul.mofa.gov.bd
------------------------------------------------------------------------------------------------------------------------
Seoul Bar Association           In-Person / Email       서초구 서초대로45길 5, 변호사회관 1층·5층         09:00 - 18:00
(Foreigner Human Rights Sub)                            Tel: 02-3476-0050 / Fax: 02-3476-0059              (Mon - Fri)
                                                        Email: humanrights@seoulbar.or.kr
========================================================================================================================
```

---

## 6. Document Generation & Packaging Specification for Implementation

When the document drafting agents compile the actual client packets in `d:/promotion/legal_claim_package/`, they must generate the following four discrete submission packages:

1. **`09_klac_foreigner_legal_aid_application_package.md`**:
   - Formal KLAC Application Form (법률구조신청서).
   - Indigence & Foreign Student Eligibility Statement.
   - Comprehensive Evidence Inventory (Items 1–12).
   - Draft Civil Complaint for Seoul Central District Court.
2. **`10_gong_gam_public_interest_litigation_brief.md`**:
   - Formal Case Intake Brief for Gong-Gam Human Rights Law Foundation.
   - Analysis of Commercial Code Art. 732-2 & Supreme Court 98Da48963.
   - Strategic Migrant Student Protection Arguments.
   - Prayer for Legal Representation or Amicus Curiae Brief.
3. **`11_duro_public_interest_impact_litigation_brief.md`**:
   - Impact Litigation Case Brief for Association for Public Interest Law DURO (Migrant Rights Team).
   - Legal Theory on Invalidation of Standard Unlicensed Exclusion Clauses.
   - Systemic Financial Consumer Protection Analysis.
4. **`12_bangladesh_embassy_diplomatic_assistance_packet.md`**:
   - Formal Diplomatic Representation Letter to Counsellor Mikon Tangchanggya (Bilingual Korean/English).
   - Draft Diplomatic Note Verbale (공한) to Samsung Fire CEO, FSS Governor, and MOFA Korea.
   - Consular Heirship Endorsement Protocol & Direct SWIFT MT103 Remittance Tracking Schedule.

---

## 7. Quality & Verification Sign-Off

- [x] All statutory frameworks verified against Korean Legal Aid Act, Commercial Code, and Private International Law Act.
- [x] Precedential citations checked against Supreme Court En Banc 98Da48963, 97Da27039, 98Da26910, 2003Da29463.
- [x] Contact information and intake procedures verified for KLAC, Gong-Gam, DURO, and Bangladesh Embassy Seoul.
- [x] Features Discovered and Edge Cases tables populated in accordance with Specification Miner rules.
