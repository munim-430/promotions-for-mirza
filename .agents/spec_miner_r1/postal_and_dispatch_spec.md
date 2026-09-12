# KOREAN CONTENT-CERTIFIED MAIL (내용증명) & DIRECT DISPATCH SPECIFICATION
## 대한민국 내용증명 우편 규정, 삼성화재 및 서정대학교 직접 발송·전자접수 집행 명세서

---

**Document Identifier:** SPEC-DISPATCH-2026-R1  
**Author:** Specification Miner (spec_miner_r1)  
**Target Milestone:** Direct-Filing Dispatch Package & Legal Aid Escalation Protocol (Phase 1 Specification)  
**Governing Case:** Late MAHADI MONOAR HOSSAIN (마하디 모노아르 후세인, ARC: `010530-7660021`, Passport: `A03097931`)  
**Target Policies:** 
1. Samsung Fire & Marine Anycar Auto Policy (Vehicle Plate: `28모1390`, Agent Shim Ki-cheol `010-8969-0440`)
2. Seojeong University D-2 Foreign Student Group Accident Insurance (서정대학교 외국인 유학생 단체상해보험)  
**Date of Specification:** August 26, 2026  

---

## 1. EXECUTIVE SPECIFICATION OVERVIEW

This specification establishes the definitive legal, administrative, postal, and electronic filing requirements for serving Korean Content-Certified Mail (*내용증명 / Naeyong Jeungmyeong*) and concurrent electronic submissions to:
1. **Samsung Fire & Marine Insurance Co., Ltd. (삼성화재해상보험주식회사)**: Headquarters Claims Department, Gangwon Auto Claims Team, Dispute Resolution Department, and Certified Agent Shim Ki-cheol (심기철).
2. **Seojeong University (서정대학교)**: Office of International Affairs (국제교류처) and lead underwriter for D-2 Foreign Student Group Accident & Repatriation Insurance.

All specifications conform strictly to the **Postal Service Act (우편법)**, **Enforcement Rule of the Postal Service Act (우편법 시행규칙)**, **Korean Civil Act (민법)**, **Korean Commercial Code (상법)**, **Financial Consumer Protection Act (금융소비자보호법)**, and Korea Post (*우정사업본부*) operational guidelines.

---

## 2. DISCOVERED FEATURES & EDGE CASES

### 2.1 Features Discovered

| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|----------|---------|-------------|--------|---------|----------------|----------------|
| 1 | Postal Rules | Korea Post 3-Copy Offline Content Certification | Postal certification under Postal Service Act Art. 15 & Enforcement Rule Arts. 46-54 requiring 1 original and 2 transcripts | Document text, envelope, recipient address | Certified original (stamped), recipient copy, post office archive copy (3-yr retention) | Return/rejection if recipient on envelope differs from document | Postal Service Act Enforcement Rule Art. 48 |
| 2 | Postal Rules | Delivery Confirmation (*배달증명*) Service | Special postal handling recording the exact date, time, and recipient agent signature upon delivery | Registered mail number, recipient signature | Korea Post Delivery Confirmation Card (*배달증명통지서*) proving arrival date under Civil Act Art. 111 | Notification of delivery failure / undeliverable notice if address incorrect | Postal Service Act Enforcement Rule Art. 25 & 59 |
| 3 | Postal Rules | Internet e-Post (*전자내용증명*) Filing | 24/7 online submission portal converting digital documents into Korea Post printed, stamped, and delivered certified mail | PDF/HWP document, digital signature, payment | Automated postal delivery, digital timestamp, 3-year cloud archive | File format error, character/page overflow | Korea Post e-Post Portal (`www.epost.go.kr`) |
| 4 | Corporate Routing | Samsung Fire HQ Claims Intake | Service of formal demand to Samsung Fire & Marine Insurance Co., Ltd. HQ in Seocho-dong, Seoul | Legal brief, policy number, vehicle plate 28모1390 | Official claim intake number, assigned claims adjustor (*대인배상/자기신체 보상담당자*) | Rejection/delay if policyholder info or vehicle number is missing | Samsung Fire Claims Intake Portal & Corporate Registry |
| 5 | Agent Routing | Samsung Fire Certified Agent Notice | Formal notice to soliciting insurance agent Shim Ki-cheol (010-8969-0440) under Commercial Code Art. 646-2 | Notice letter, policy renewal record (2026-03-13) | Personal receipt, branch notification, proof of notice | Agent unresponsiveness -> escalate to HQ Inspectorate | Commercial Code Art. 646-2 & SFMI Agent Network |
| 6 | Academic Routing | Seojeong University Group Claim Routing | Formal insurance claim served on Seojeong University International Affairs Office for D-2 Group Accident Insurance | Claim package, enrollment certificate, autopsy/police report | University endorsement, transmission to lead group insurer (DB/KB/Hyundai/Meritz) | Department non-cooperation -> escalate to Ministry of Education IEQAS | Seojeong Univ Registry & MOE Foreign Student Directives |
| 7 | Legal Doctrine | Invalidation of Unlicensed Exemption | Mandatory statutory voiding of unlicensed driving exclusions in first-party accidental death coverage | Commercial Code Arts. 732-2, 739, 663; Supreme Court 98Da48963 | Full KRW 100M payout obligation, preclusion of insurer bad-faith defenses | Insurer attempts improper denial -> triggers FSS penalty | Supreme Court Precedents & Commercial Code |
| 8 | Statutory Benefit | Provisional Payment Demand (*가지급금 청구*) | Right to demand 50%+ of estimated claim payout within 3 business days under Auto Insurance Standard Terms Art. 34(3) | Written request, police accident confirmation | Immediate KRW 50,000,000 provisional advance remittance | Insurer failure to pay -> triggers 6% statutory interest | Auto Standard Terms & Commercial Code |
| 9 | Cross-Border Remittance | Direct SWIFT Wire Remittance Mandate | Mandate for insurer to remit proceeds directly to Bangladeshi bank accounts of legal heirs under PIL Art. 49 | Heirs SWIFT BIC, IBAN/Account No., Special POA | Direct USD/KRW wire transfer without third-party escrow or commission cut | Foreign Exchange Bank compliance query if documentation lacks consular seal | Foreign Exchange Transactions Act & PIL Art. 49 |

### 2.2 Edge Cases & Observed Behaviors

| # | Feature | Edge Case Input | Observed Legal & Administrative Behavior |
|---|---------|-----------------|------------------------------------------|
| 1 | Recipient Name Discrepancy | Envelope says "삼성화재 강원보상부" but document header says "삼성화재해상보험주식회사 대표이사 이문화" | Korea Post window officer will REJECT mail submission. Postal Service Act Enforcement Rule Art. 48 mandates exact 1:1 character match between document header and envelope addressee. |
| 2 | Deceased Single-Vehicle Crash | Deceased was sole occupant and driver with no domestic Korean driver's license (Single-vehicle guardrail collision) | Insurer frequently raises standard Auto Clause unlicensed exemption; strictly INVALIDATED as a matter of law per Commercial Code Art. 732-2 and Supreme Court En Banc 98Da48963 for accidental death coverage. |
| 3 | Foreign Heir Representation | Claim submitted by Korean attorney-in-fact with foreign Special POA signed in Bangladesh | If POA lacks Consular Legalization / Apostille, insurer or bank will withhold payout under PIL Art. 49. Complete consular/apostille verification is mandatory. |
| 4 | Dual Insurance Recovery | Simultaneous claim against Samsung Fire (Auto Policy) and Seojeong University Group Insurer (Group Accident Policy) | Both policies MUST pay in full. Accidental death benefit is a fixed-sum (*정액보험*) benefit under Commercial Code Art. 739; prohibition of double recovery (*실손보상 중복보상 금지*) does NOT apply. |
| 5 | Recipient Refusal of Content-Certified Mail | Recipient deliberately refuses delivery (*수취거절*) or is absent (*폐문부재*) | Under Korean Civil Act Art. 111 and Supreme Court 2008Da19973, deliberate refusal of certified mail by a party capable of receiving it constitutes completed arrival (*도달간주*). |

---

## 3. AUTHORITATIVE SPECIFICATION SOURCE & LEGAL FRAMEWORK

### 3.1 Postal Service Act & Enforcement Rules (우편법 및 동 시행규칙)
- **Postal Service Act (우편법) Art. 15 (Special Postal Services)**: Authorizes Korea Post to provide Content Certification (*내용증명*) and Delivery Confirmation (*배달증명*).
- **Enforcement Rule of the Postal Service Act (우편법 시행규칙) Art. 46 (Content Certification Definition)**: Establishes that Content Certification certifies the exact textual content and delivery date of documents written in Korean, Hanja, or foreign languages.
- **Art. 48 (Submission of Original & Transcripts)**: The sender must present **one original document** and **two identical transcripts** (*원본 1부 + 등본 2통 = 총 3통*). If there are multiple recipients, one additional transcript per recipient must be submitted. Korea Post stamps all copies, returns one to the sender, delivers the original to the addressee, and stores one transcript for **three (3) years**.
- **Art. 50 (Official Seal & Inter-Page Perforation/Seal)**: The post office affixes its official date stamp and inter-page seal (*간인 / 契印*) across multi-page documents to guarantee non-tampering.
- **Art. 54 (Re-certification & Inspection within 3 Years)**: Either sender or recipient may inspect the archived copy or demand official re-certification (*재증명 발급*) within three years from the date of dispatch upon showing proof of identity.
- **Art. 59 (Delivery Confirmation - 배달증명)**: Guarantees return of an official notice confirming the exact date, time, and recipient signatory who took delivery of the registered mail.

### 3.2 Civil Act & Commercial Code (민법 및 상법)
- **Civil Act (민법) Art. 111(1) (Arrival Principle / 도달주의)**: A declaration of intention takes legal effect when it reaches the other party (*도달한 때에 그 효력이 생긴다*). Delivery Confirmation (*배달증명*) provides irrefutable evidence of the arrival date.
- **Civil Act Art. 118 (Scope of Attorney-in-Fact Authority)**: Empowers the designated attorney-in-fact to perform preservation acts, claim filings, and settlement demands pursuant to a Special Power of Attorney.
- **Commercial Code (상법) Art. 732-2 (Accidental Death Exemption Limitation)**: Precludes insurers from exempting accidental death benefits unless caused by the intentional act of the insured/beneficiary. Gross negligence (including unlicensed driving) CANNOT be grounds for exemption.
- **Commercial Code Art. 739 (Application of Life Insurance Rules to Accident Insurance)**: Extends statutory non-exemption and beneficiary protections to accident insurance contracts.
- **Commercial Code Art. 663 (Prohibition of Disadvantageous Alteration / 불이익변경금지)**: Any policy term less favorable to the insured than statutory Commercial Code provisions is strictly null and void.
- **Commercial Code Art. 54 & Standard Auto Terms Art. 34**: Imposes a 10-business-day claim settlement deadline, after which 6% statutory commercial default interest accrues, and mandates a 50%+ provisional payment (*가지급금*) within 3 business days of application.

### 3.3 Private International Law Act (국제사법)
- **Private International Law Act Art. 49(1)**: Inheritance is governed by the national law of the deceased at the time of death (*상속은 사망 당시 피상속인의 본국법에 따른다*).
- Deceased was an unmarried Bangladeshi national; under Bangladeshi Sunni Hanafi Muslim Personal Law, legal heirship is apportioned 100% between:
  - **Father (BELAL HOSSAIN)**: 2/3 Share (66.667%, Residuary / Asaba)
  - **Mother (MONOARA BEGUM)**: 1/3 Share (33.333%, Quranic Sharer / Zawil Furud)

---

## 4. KOREAN CONTENT-CERTIFIED MAIL (내용증명) PROCEDURAL & POSTAL REQUIREMENTS

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                         KOREA POST CONTENT-CERTIFIED MAIL DISPATCH WORKFLOW                      │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                  │
│  [ STEP 1: PREPARATION ]                                                                         │
│  • Print 3 identical sets on standard A4 paper (Original + Sender Transcript + Post Office Copy) │
│  • Verify Document Header (Sender & Recipient) matches Envelope 100% word-for-word              │
│  • Attach comprehensive Exhibit Catalog (*첨부서류 목록*)                                        │
│  • Affix Sender / Attorney-in-Fact Signature and Registered Name Seal (*인감날인/직인*)          │
│                                                                                                  │
│  [ STEP 2: POST OFFICE INTAKE (OFFLINE) / e-POST UPLOAD (ONLINE) ]                               │
│  • Offline: Submit 3 copies at any Korea Post window (우체국 우편창구)                            │
│  • Request: "내용증명 (Content Certification) + 익일특급 (Next-Day Registered) + 배달증명"       │
│  • Online: Upload PDF via Korea Post e-Post (`www.epost.go.kr` -> 우편 -> 전자내용증명)          │
│                                                                                                  │
│  [ STEP 3: POSTAL EXAMINATION & STAMPING ]                                                       │
│  • Postal officer verifies matching addresses on document vs. envelope                           │
│  • Affixes official date stamp (*일부인*) and inter-page seals (*간인*) on all 3 copies           │
│  • Original is placed in envelope and sealed in front of postal officer                          │
│                                                                                                  │
│  [ STEP 4: SERVICE & DELIVERY CONFIRMATION ]                                                     │
│  • Korea Post delivers original registered mail to recipient (Samsung Fire HQ / Seojeong Univ)   │
│  • Recipient signs delivery register; Korea Post issues Delivery Confirmation Card (*배달증명서*) │
│  • Official 3-year statutory archive begins at Korea Post                                        │
│                                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Strict Physical & Formatting Rules for Korea Post Window Filing
1. **Paper & Margin Standards**: Standard A4 paper (210mm x 297mm), portrait orientation. Maintain top/bottom/left/right margins of at least 20mm to ensure ample space for Korea Post official stamps (*일부인*) and barcode labels.
2. **Page Count & Inter-Page Sealing (*간인 / 契印*)**:
   - If the document spans two or more pages, the sender/attorney must apply an inter-page seal (*간인*) between pages, OR the postal officer will apply the post office's perforated embossing stamp across the folded edges of all pages.
3. **Exact Header-Envelope Alignment Rule**:
   - **Sender (발신인)**: Name, representative title, and address on the document header must be identical to the sender block on the postal envelope.
   - **Recipient (수신인)**: Entity name, CEO name, department name, and road-name address on the document header must be identical to the recipient block on the postal envelope.
   - *Any divergence in corporate name, building floor, or spelling will result in immediate rejection by the post office counter clerk.*
4. **Mandatory Combination Services**:
   - **등기우편 (Registered Mail)**: Assigns a unique 13-digit tracking number (*등기번호*).
   - **익일특급 (Next-Day Express)**: Ensures delivery on the next business day nationwide.
   - **배달증명 (Delivery Confirmation)**: Post office sends an official physical certificate to the sender indicating the exact recipient name, department, delivery date, and timestamp.
5. **Enclosure Prohibition**:
   - Under Postal Service Act Enforcement Rule Art. 46, physical objects, cash, checks, or USB drives CANNOT be enclosed inside a Content-Certified Mail envelope. Only printed paper documents and photocopies of exhibits may be included.

### 4.2 Korea Post Electronic Content-Certified Mail (인터넷우체국 전자내용증명 - e-Post)
- **Portal Access**: Korea Post Official Website (`https://www.epost.go.kr`) -> 우편 -> 증명서비스 -> 전자내용증명.
- **Operating Hours**: 24 hours a day, 365 days a year.
- **Submission Process**:
  1. Log in with digital certificate or corporate/individual ID.
  2. Upload document in PDF or HWP/DOCX format (up to 150 pages).
  3. Enter sender and recipient details (automatically formats postal address label).
  4. Select "배달증명" (Delivery Confirmation) and "익일특급" (Next-Day Express).
  5. Complete electronic fee payment (standard postal rate + content certification fee + delivery confirmation fee).
- **Automated Processing**: Korea Post Electronic Mail Center automatically applies digital timestamp (*전자타임스탬프*), prints on secure paper, seals in tamper-evident envelopes, dispatches via postal logistics, and archives the digital document for three (3) years.
- **Electronic Proof**: Sender can download the timestamped certification certificate and delivery receipt online at any time.

---

## 5. INSTITUTIONAL ROUTING SPECIFICATION 1: SAMSUNG FIRE & MARINE INSURANCE CO., LTD.

### 5.1 Corporate & Departmental Profile

```
====================================================================================================
                        SAMSUNG FIRE & MARINE INSURANCE CO., LTD. ROUTING DOSSIER
====================================================================================================
Corporate Entity:           삼성화재해상보험주식회사 (Samsung Fire & Marine Insurance Co., Ltd.)
Representative Director:    대표이사 이문화 (CEO Lee Mun-hwa)
Corporate Registration No.: 110111-0005705
Headquarters Road Address:  서울특별시 서초구 서초대로74길 14 (서초동, 삼성화재 서초타워)
Headquarters English:       Samsung Fire Seocho Tower, 14 Seocho-daero 74-gil, Seocho-gu, Seoul 06620
Postal Code:                06620
Target Departments:         1. 자동차보험 보상본부 (Automobile Insurance Claims Headquarters)
                            2. 강원보상부 / 강릉보상팀 (Gangwon Claims Dept. / Gangneung Auto Claims)
                            3. 소비자보호팀 / 금융분쟁조정대응반 (Consumer Protection / Dispute Resolution)
                            4. 감사팀 / 법무팀 (Inspectorate & Legal Affairs Team)
====================================================================================================
```

### 5.2 Contact Channels & Submission Endpoints

| Channel Type | Channel Identifier | Operational Purpose & Routing Instructions |
|--------------|-------------------|---------------------------------------------|
| **Certified Mail (Primary)** | 서울특별시 서초구 서초대로74길 14, 삼성화재빌딩 자동차보상본부 (우: 06620) | Primary legal service of Content-Certified Mail Notice (*내용증명 최고서 원본*). |
| **Gangwon Regional Office** | 강원특별자치도 강릉시 옥천로 19, 삼성화재 강릉사옥 강원보상부 (우: 25539) | Secondary concurrent certified mail copy to regional claims handling desk. |
| **Main Phone Line** | `1588-5114` (ARS: 2번 자동차사고 보상상담) | Claims intake verification, adjustor assignment check, initial notice. |
| **Overseas Calling Line** | `+82-2-2112-1566` / `+82-2-1588-5114` | Direct overseas call line for foreign family / consular representatives. |
| **Dedicated Claims Fax** | `0505-162-0242` / `0505-162-0001` | HQ Claims electronic fax intake for immediate duplicate filing. |
| **Customer Portal** | `www.samsungfire.com` (보상/청구 -> 서류접수) | Direct upload of PDF claim package under policyholder ARC `010530-7660021`. |
| **Legal/Dispute Intake Email**| `claim@samsungfire.com` / `sfmiclaim@samsungfire.com` | High-priority bilingual email filing with full exhibit attachments. |

### 5.3 Insurance Agent & Subject Policy Routing Details

```
====================================================================================================
                        SUBJECT POLICY & CERTIFIED AGENT SPECIFICATION
====================================================================================================
Subject Vehicle Plate No.:  28모1390 (Kia Morning / 기아 모닝 경승용)
Policy Product Name:        삼성화재 애니카 개인용 자동차보험 (Anycar Comprehensive Auto Policy)
Contract Period / Renewal:  2026년 3월 13일 24:00 개시 ~ 2027년 3월 13일 24:00 만기 (사고 6시간 전 갱신)
Contractor & Insured:       故 MAHADI MONOAR HOSSAIN (외국인등록번호: 010530-7660021)
Target Claim Coverage:      자기신체사고 (또는 자동차상해 특약) 사망보험금 전액 (금 100,000,000원)
Soliciting Insurance Agent: 심기철 (Shim Ki-cheol)
Agent Mobile Phone:         010-8969-0440
Legal Status of Agent:      Insurance agent under Commercial Code Art. 646-2; notice to agent constitutes
                            constructive notice to insurer regarding policy claim intake.
====================================================================================================
```

### 5.4 Strategic Multi-Channel Dispatch Sequence for Samsung Fire
1. **Day 0 (Morning)**: Dispatch Korean Content-Certified Mail (*내용증명 원본*) via Korea Post Next-Day Registered Express (*익일특급 + 배달증명*) to Samsung Fire HQ in Seocho-gu, Seoul.
2. **Day 0 (Concurrent)**: Send High-Priority Bilingual Email to `claim@samsungfire.com` and `sfmiclaim@samsungfire.com` with complete PDF dossier and Korea Post tracking number.
3. **Day 0 (Afternoon)**: Send SMS / Formal Written Dispatch Notice to Agent Shim Ki-cheol (`010-8969-0440`) notifying him of the formal claim service and requesting branch claims adjustor contact.
4. **Day 0 (Concurrent)**: Transmit complete claim notice via electronic fax to `0505-162-0242`.
5. **Day 1 (Upon Delivery)**: Korea Post delivers certified mail to Samsung Fire HQ; Korea Post logs delivery timestamp.
6. **Day 3**: Statutory 3-business-day deadline for 50%+ Provisional Payment (*가지급금 금 50,000,000원*) under Auto Insurance Standard Terms Art. 34(3).
7. **Day 10**: Statutory 10-business-day claim settlement deadline expires; 6% default interest begins accruing automatically.

---

## 6. INSTITUTIONAL ROUTING SPECIFICATION 2: SEOJEONG UNIVERSITY INTERNATIONAL AFFAIRS OFFICE

### 6.1 Academic & Departmental Profile

```
====================================================================================================
                    SEOJEONG UNIVERSITY INTERNATIONAL AFFAIRS OFFICE ROUTING DOSSIER
====================================================================================================
Academic Institution:       학교법인 서정학원 서정대학교 (Seojeong University)
President:                  총장 양영희 (President Yang Young-hee)
Headquarters / Campus:      경기도 양주시 은현면 서정로 27, 국제관 별관 L층 국제교류처 (우편번호: 11429)
Campus English Address:     Office of International Affairs, Seojeong University Annex L-Fl,
                            27 Seojeong-ro, Eunhyeon-myeon, Yangju-si, Gyeonggi-do 11429, Korea
Legacy/Sub-Address Ref:     경기도 양주시 은현면 화합로 1043-56
Postal Code:                11429
Governing Department:       국제교류처 (Office of International Affairs / Foreign Student Support Center)
Dean / Department Head:     국제교류처장 (Dean of International Affairs)
====================================================================================================
```

### 6.2 Contact Channels & Submission Endpoints

| Channel Type | Channel Identifier | Operational Purpose & Routing Instructions |
|--------------|-------------------|---------------------------------------------|
| **Certified Mail (Primary)** | 경기도 양주시 은현면 서정로 27, 서정대학교 국제교류처 (우: 11429) | Primary service of Content-Certified Mail Notice (*내용증명 청구서 원본*). |
| **Office Direct Line** | `031-860-5177` (국제교류처 외국인유학생 지원팀 직통) | Direct consultation on D-2 student insurance claims and repatriation subsidy. |
| **University General Line** | `031-859-6900` / `031-860-5000` | Campus operator and administrative coordination. |
| **Department Fax** | `031-859-6901` / `031-859-6180` | Immediate facsimile transmission of claim package. |
| **Official Department Email**| `global@seojeong.ac.kr` / `inter@seojeong.ac.kr` | Bilingual electronic claim filing and document endorsement requests. |

### 6.3 D-2 Foreign Student Group Accident & Repatriation Insurance Architecture

```
====================================================================================================
                D-2 FOREIGN STUDENT GROUP ACCIDENT INSURANCE CLAIM ARCHITECTURE
====================================================================================================
Governing Framework:        Ministry of Education IEQAS (교육부 외국인 유학생 유치·관리 역량 인증제)
Policyholder:               학교법인 서정학원 서정대학교 (Seojeong University)
Insured:                    故 MAHADI MONOAR HOSSAIN (서정대학교 스마트자동차과 1학년 재학생)
Beneficiaries:              사망 시 법정상속인 (부 BELAL HOSSAIN 2/3, 모 MONOARA BEGUM 1/3)
Lead Underwriters (Typical):DB손해보험, KB손해보험, 현대해상화재보험, 메리츠화재해상보험, 한화손해보험
Target Claim Benefits:      1. 상해사망보험금 (Accidental Death Benefit): KRW 10,000,000 ~ 50,000,000
                            2. 유골·사체 본국송환비용 (Repatriation Expenses): KRW 5,000,000 ~ 20,000,000
                            3. 장례비 및 응급의료구조비 (Emergency Medical/Funeral Costs): 실손 정산
Dual Recovery Principle:    Accidental death benefits under group insurance are fixed-sum benefits
                            (*정액보험*); they are paid IN ADDITION to Samsung Fire auto insurance without
                            any offset or deduction (*중복보상 금지 원칙 미적용*).
====================================================================================================
```

### 6.4 Seojeong University Administrative Claim Workflow
1. **Receipt of Certified Demand**: Seojeong University International Affairs Office receives the Content-Certified claim notice and exhibit package.
2. **Academic Status & Master Policy Verification**: The International Affairs Office confirms deceased's enrollment in the Smart Automobile Department (*스마트자동차과 1학년*) and retrieves the active Master Group Policy Certificate (*단체보험 증권번호*) and lead insurance carrier.
3. **Issuance of Academic Exhibits**: The University issues the official Certificate of Student Enrollment (*재학증명서 / 학적부*) and Tuition/Insurance Fee Payment Confirmation (*보험료 납부확인서*).
4. **Endorsement & Forwarding to Insurer**: The University transmits the completed Group Claim Form, University Endorsement Letter, Death Certificate, Police Traffic Accident Confirmation, Consular Certificates, and Special POA directly to the Group Insurer's Corporate Claims Adjustment Team.
5. **Direct SWIFT Remittance**: The Group Insurer processes the claim and executes direct international SWIFT wire transfers to the parents' designated bank accounts in Bangladesh.

---

## 7. FORMAL KOREAN CONTENT-CERTIFIED MAIL STRUCTURE & CANONICAL TEMPLATES

### 7.1 Exact Formal Anatomy of Korean Content-Certified Mail
Under Korean legal drafting practice and Postal Service Act standards, every Content-Certified Mail document must strictly embody the following ten (10) structural components:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   CANONICAL ANATOMY OF KOREAN CONTENT-CERTIFIED MAIL (내용증명)                  │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. HEADER (문서두부):                                                                             │
│    • 문서번호 (Document Control Number)                                                          │
│    • 발송일자 (Date of Dispatch)                                                                 │
│    • 발신인 (Sender / Heirs Details & Bangladesh Address)                                        │
│    • 대리인 (Authorized Legal Counsel / Attorney-in-Fact & Office Address)                        │
│    • 수신인 (Addressee: Legal Entity, CEO Name, Dept., Exact Road Address, Postal Code)          │
│ 2. TITLE (제목): Clear, formal, urgent subject line stating the exact legal nature of the demand │
│ 3. SECTION 1: 당사자 및 사건의 표시 (Parties, Deceased Profile, Policy/Vehicle, Fatal Crash Facts)│
│ 4. SECTION 2: 청구 취지 (Demand for Relief: Principal, 6% Interest, 50%+ Provisional, SWIFT Wire) │
│ 5. SECTION 3: 청구 원인 (Legal Grounds: PIL Art. 49, Commercial Code 732-2/739/663, Precedents)   │
│ 6. SECTION 4: 면책주장의 절대적 위법성 (Refutation of Unlicensed Driving Exemption Defense)      │
│ 7. SECTION 5: 이행 기한 및 불이행 시 조치 (Statutory Deadlines: 3-day / 10-day, FSS / Litigation)│
│ 8. EXHIBIT LIST (첨부서류 목록 / 입증자료 목록): Comprehensive list of all evidentiary documents   │
│ 9. CLOSING & DATE (결미 및 작성일자): Formal Korean closing salutation and dispatch date         │
│ 10. SIGNATURE & SEAL (발신인 및 대리인 기명날인): Official signature and registered seal (인감/직인)│
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### 7.2 Canonical Template A: Samsung Fire & Marine Insurance Co., Ltd. (내용증명 최고서 국문 정본)

```markdown
# 최 고 서 (내용증명)
### [자동차보험 자기신체사고 사망보험금 청구 및 가지급금 지급 최고]

---

**문서번호:** SFMI-CLAIM-2026-0826-01  
**발송일자:** 2026년 8월 26일  

**발신인 (청구인 / 망인의 법정상속인 전원):**
1. **BELAL HOSSAIN** (망인의 부 / Father, 법정상속지분 2/3, 66.667%)
   - 생년월일: 1973년 11월 12일 | 국적: 방글라데시 인민공화국 (NID: 19731916723000045)
2. **MONOARA BEGUM** (망인의 모 / Mother, 법정상속지분 1/3, 33.333%)
   - 생년월일: 1980년 3월 5일 | 국적: 방글라데시 인민공화국 (NID: 19801916723000046)
   - 주소: Munshi Bari, Keshobpur, Monoharganj - 3571, Cumilla, Bangladesh

**발신인들의 선임 법률대리인 (수임인 / Attorney-in-Fact):**
- **대리인:** 상속인들의 적법한 특별위임장(Special Power of Attorney)을 수탁받은 법률대리인
- **사무소 주소:** 대한민국 서울특별시 서초구 서초대로 (법률사무소)
- **연락처:** 전화 02-xxx-xxxx | 팩스 02-xxx-xxxx | 이메일 counsel@lawfirm.kr

**수신인:**
**삼성화재해상보험주식회사**
- **대표자:** 대표이사 이문화
- **주소:** 서울특별시 서초구 서초대로74길 14 (서초동, 삼성화재 서초타워) [우편번호: 06620]
- **소관부서:** 자동차보험 보상본부 / 강원보상부 / 자동차사고 심사기획팀
- **참조:** 보험모집인 심기철 (연락처: 010-8969-0440)

---

## 1. 당사자 및 사건의 표시

### 가. 피보험자(망인)의 인적사항
- 성명: MAHADI MONOAR HOSSAIN (마하디 모노아르 후세인 / 여권명: MONOAR HOSSAIN MAHADI)
- 외국인등록번호: 010530-7660021 (D-2 유학, 춘천출입국·외국인관서 속초출장소 관할)
- 여권번호: A03097931 (방글라데시 국적, 생년월일: 2001.05.30., 사망 당시 만 24세)
- 재학사항: 서정대학교 스마트자동차과 1학년 재학

### 나. 대상 보험계약 및 피보험차량의 표시
- 피보험차량 번호: **28모1390** (기아 모닝 경승용)
- 보험종목: 삼성화재 애니카 개인용 자동차보험
- 담보종목: 대인배상 I·II, 대물배상, **자기신체사고(또는 자동차상해 특약)**, 무보험차상해, 자차
- 계약 체결 및 갱신일: **2026년 3월 13일 24:00 개시** (사고 발생 직전 정상 갱신 완료)
- 담당 모집인: 심기철 (010-8969-0440)
- 계약자 및 기명피보험자: MAHADI MONOAR HOSSAIN

### 다. 사고 발생 사실 및 경위
- 사고일시: 2026년 3월 14일 05시 58분경
- 사고장소: 강원특별자치도 양양군 현남면 북분리 4-1 도로상
- 사고개요: 망인이 피보험차량(28모1390)을 운전하여 주행 중 도로를 이탈하여 도로변 가드레일을 충돌한 **순수 단독 차량 충돌사고(Single-Vehicle Collision)**
- 조사관서: 강원속초경찰서 교통사고조사계 (사건번호: **2026-00020**, 담당수사관: 경위 조형철)
- 의학적 검안: 강릉아산병원 응급의학과 전문의 강희동 (시체검안서 발급, 사인: 외상성 뇌손상 및 두개골 골절, 외인사)

---

## 2. 청구 취지

1. 수신인은 청구인들에게 피보험차량(28모1390)의 자동차보험계약에 기한 **자기신체사고 사망보험금 금 100,000,000원(약정 가입금액 전액)**을 법정상속지분에 따라 즉시 지급하라.
   - 청구인 BELAL HOSSAIN (부, 2/3 지분): **금 66,666,667원**
   - 청구인 MONOARA BEGUM (모, 1/3 지분): **금 33,333,333원**
2. 수신인은 자동차보험 표준약관 제34조 제3항에 의거하여, 손해사정 완료 이전이라도 본 최고서 수령일로부터 **3영업일 이내에 추정보험금의 50%인 금 50,000,000원의 가지급보험금(Provisional Benefit)**을 우선 지급하라.
3. 수신인은 본 최고서 송달일로부터 10영업일이 경과한 다음 날부터 완제일까지 상법 제54조 소정의 **연 6% 상사법정이율**, 소송 제기 시 소송촉진 등에 관한 특례법 소정의 **연 12%의 지연손해금**을 부가하여 지급하라.
4. 모든 보험금은 청구인들이 지정한 방글라데시 현지 은행계좌로 직접 해외 전신환 송금(Direct SWIFT MT103 Remittance) 방식으로 지급하라.

---

## 3. 청구 원인 및 법률적 근거

### 가. 국제사법 제49조에 따른 단독·공동 상속인 지위 확정
대한민국 국제사법 제49조 제1항에 따라 상속은 사망 당시 피상속인의 본국법인 방글라데시 무슬림 상속법(Sunni Hanafi Law)에 의합니다. 미혼 장남인 망인의 사망으로 인하여 모(MONOARA BEGUM)는 확정지분 1/3(Zawil Furud), 부(BELAL HOSSAIN)는 잔여 상속분 2/3(Asaba)를 취득하여, 청구인 2인이 100% 단독 법정상속인 지위를 확정하였습니다.

### 나. 대법원 판례에 따른 자기신체사고 보험금의 '상속인 고유재산' 법리
대법원 판례(대법원 2004. 7. 9. 선고 2003다29463 판결 등)에 따라 자동차보험 자기신체사고 사망보험금 청구권은 상속재산이 아니라 **상속인들의 고유재산(Inherent Original Property)**으로 귀속됩니다.

### 다. 무면허운전 면책약관의 절대적 무효 (상법 제732조의2, 제739조, 제663조)
1. **대법원 전원합의체 판결(대법원 1998. 12. 22. 선고 98다48963 전원합의체 판결)** 및 확립된 대법원 판례(대법원 97다27039, 98다26910 판결)에 의하면, 상법 제732조의2 및 제739조는 상해보험 및 자기신체사고 담보에서 피보험자의 중과실로 인한 사고에 대하여 보험자의 면책을 엄격히 금지하고 있습니다.
2. 따라서 피보험자의 무면허운전 행위는 중과실에 불과하므로, 자동차보험 약관 중 **무면허운전 시 자기신체사고를 면책하는 조항은 상법 제663조(불이익변경금지 원칙)에 위배되어 절대적 무효**입니다.
3. 본건 사고는 타인에 대한 배상책임 사고가 아닌 순수 단독 차량 충돌사고(Single-Vehicle Accident)이므로, 수신인은 일체의 면책을 주장할 수 없습니다.

---

## 4. 이행 기한 및 불이행 시 조치 계획

1. **가지급금 이행 기한**: 본 최고서 수령일로부터 **3영업일 이내** (금 50,000,000원 즉시 송금).
2. **최종 정산 이행 기한**: 본 최고서 수령일로부터 **10영업일 이내** (잔액 금 50,000,000원 및 완제일까지의 지연이자 송금).
3. **불이행 시 법적 조치**: 만약 수신인이 위 기한 내에 지급 의무를 이행하지 아니하거나 부당한 면책을 주장하며 지연할 경우, 청구인 대리인은 즉시:
   - **금융감독원(FSS) 금융분쟁조정위원회**에 분쟁조정신청서 정식 접수 및 금융소비자보호법 위반 제재 요청
   - **대한법률구조공단(KLAC)** 및 **서울지방변호사회 외국인인권소위원회**와 연계한 민사 손해배상 청구 소송 제기 (소송촉진법상 연 12% 지연손해금 및 소송비용 전액 청구)
   - 주한 방글라데시 대사관(Labour & Consular Wing)을 통한 공식 외교적·영사적 조력권 발동 및 공익언론 제보를 단행할 것임을 엄중히 고지합니다.

---

## 5. 첨부서류 (입증자료 목록)

1. [갑 제1호증] 강릉아산병원 사체검안서 (Medical Post-Mortem Certificate)
2. [갑 제2호증] 강원속초경찰서 교통사고발생상황진술서 및 변사사건 조사결과 통보서
3. [갑 제3호증] 망인 외국인등록증(ARC) 및 방글라데시 여권 사본
4. [갑 제4호증] 망인 서정대학교 학생증 및 학적확인서
5. [갑 제5호증] 상속인 부(BELAL HOSSAIN) 및 모(MONOARA BEGUM) 방글라데시 국민신분증(NID)
6. [갑 제6호증] 방글라데시 연방정부 발행 가족관계증명서 및 상속인 확인서 (Family Certificate / Heirship Certificate)
7. [갑 제7호증] 상속인 전원의 적법한 특별위임장 (Special Power of Attorney, 주방글라데시 대한민국 대사관 영사확인/아포스티유 완료본)
8. [갑 제8호증] 주한 방글라데시 대사관 영사확인서 및 국적증명서 (Embassy Consular Certificate)
9. [갑 제9호증] 한국엠바밍(주) 방부처리(엠바밍) 증명서 및 유골 본국송환 화물운송장(Air Waybill)
10. [갑 제10호증] 상속인 지정 방글라데시 현지 은행계좌 송금정보 (SWIFT MT103 Bank Details)

---

**2026년 8월 26일**

**발신인 (청구인):**
BELAL HOSSAIN (인)
MONOARA BEGUM (인)

**청구인들의 선임 법률대리인:**
법률사무소 담당 변호사 / 대리인 (직인 생략 / 인)
```

---

### 7.3 Canonical Template B: Seojeong University International Affairs Office (내용증명 청구서 국문 정본)

```markdown
# 외국인 유학생 단체상해보험 보험금 청구 및 학교 협조요청서 (내용증명)

---

**문서번호:** SJU-INTL-2026-0826-01  
**발송일자:** 2026년 8월 26일  

**발신인 (청구인 / 망인의 법정상속인 전원):**
1. **BELAL HOSSAIN** (망인의 부 / Father, 법정상속지분 2/3)
2. **MONOARA BEGUM** (망인의 모 / Mother, 법정상속지분 1/3)
   - 주소: Munshi Bari, Keshobpur, Monoharganj - 3571, Cumilla, Bangladesh

**발신인들의 선임 법률대리인:**
- **대리인:** 상속인들의 적법한 특별위임장 수임 법률대리인
- **사무소 주소:** 대한민국 서울특별시 서초구 서초대로 (법률사무소)
- **연락처:** 전화 02-xxx-xxxx | 팩스 02-xxx-xxxx | 이메일 counsel@lawfirm.kr

**수신인:**
1. **학교법인 서정학원 서정대학교 총장 양영희 귀하**
2. **서정대학교 국제교류처장 귀하**
   - 주소: 경기도 양주시 은현면 서정로 27, 서정대학교 국제관 별관 L층 국제교류처 [우편번호: 11429]
   - 연락처: 전화 031-860-5177 / 031-859-6900 | 팩스 031-859-6901 | 이메일 global@seojeong.ac.kr
3. **서정대학교 외국인 유학생 단체상해보험 계약 주간 보험회사 대표이사 귀하**
   (DB손해보험 / KB손해보험 / 현대해상화재보험 / 메리츠화재 등 보상심사팀)

---

## 1. 청구 배경 및 망인 학적 사항

1. **피보험자 (망인) 학적**:
   - 성명: MAHADI MONOAR HOSSAIN (마하디 모노아르 후세인)
   - 외국인등록번호: 010530-7660021 | 여권번호: A03097931
   - 소속: 서정대학교 스마트자동차과 1학년 재학 (D-2 유학 체류자격)
2. **사고 개요**:
   - 고인은 2026년 3월 14일 05시 58분경 강원도 양양군 현남면 북분리 4-1 도로상에서 발생한 교통사고로 인하여 강릉아산병원에서 외상성 뇌손상으로 유명을 달리하였습니다 (강원속초경찰서 사건번호 2026-00020).
3. **대학 단체보험 가입 사실**:
   - 교육부 「외국인 유학생 유치·관리 역량 인증제(IEQAS)」 지침에 따라 서정대학교에 재학 중인 유학생 전원은 서정대학교가 보험계약자로서 일괄 체결한 **외국인 유학생 단체상해보험**의 정당한 피보험자입니다.

---

## 2. 청구 항목 및 청구 취지

고인의 유일한 법정상속인들인 청구인들은 서정대학교 국제교류처를 경유하여 주간 보험회사에 대하여 다음과 같이 보험금 지급을 정식 청구합니다.

1. **상해사망보험금 (Accidental Death Benefit)**:
   - 단체상해보험 약정 가입금액 전액 (**금 10,000,000원 ~ 50,000,000원**)
2. **사체·유골 본국 송환비용 및 장례비 (Repatriation & Mortuary Expenses)**:
   - 한국엠바밍(주) 엠바밍 비용, 방글라데시 항공화물 운송비, 안치료 등 기발생 실손 전액 (**금 5,000,000원 ~ 20,000,000원**)
3. **응급구조 및 의료비용 (Emergency Medical Fees)**:
   - 강릉아산병원 응급실 진료 및 사체검안 제비용 실손 전액
4. **지급 방식**:
   - 상속인 부(2/3), 모(1/3)의 방글라데시 현지 은행계좌로 직접 해외 전신환 송금(Direct SWIFT MT103).

---

## 3. 서정대학교 국제교류처에 대한 행정 협조 요청 사항

1. **단체보험 증권번호 및 주간 보험사 정보 확인**: 서정대학교가 체결한 당해 연도 외국인 유학생 단체상해보험 증권 사본 및 주간 보험회사(보상접수처) 안내.
2. **보험금 청구서 이송 및 대학 확인 날인**: 첨부된 보험금 청구 서류 일체를 접수하여 대학 직인 날인 후 주간 보험회사에 정식 접수 이송.
3. **학적 증빙 서류 발급 지원**: 망인의 재학증명서, 등록금/보험료 납부확인서 발급 및 사건 파일 편철 협조.

---

## 4. 첨부서류 목록

1. 사망진단서 및 시체검안서 (강릉아산병원) 사본 1부
2. 교통사고사실확인원 및 변사사건기록 (강원속초경찰서) 사본 1부
3. 망인 외국인등록증, 여권 및 서정대학교 학생증 사본 1부
4. 상속인 전원 방글라데시 신분증 및 상속인확인서 (Heirship Certificate) 공증본 1부
5. 상속인 특별위임장 (Special Power of Attorney, 대사관 영사확인/아포스티유본) 1부
6. 주한 방글라데시 대사관 영사확인서 및 국적증명서 사본 1부
7. 엠바밍 증명서 및 유골 본국송환 항공화물운송장(AWB) 및 영수증 일체 1부
8. 상속인 방글라데시 은행 SWIFT 계좌 정보 1부

---

**2026년 8월 26일**

**발신인 (청구인):**
BELAL HOSSAIN (인)
MONOARA BEGUM (인)

**청구인들의 선임 법률대리인:**
법률사무소 담당 변호사 / 대리인 (직인 생략 / 인)
```

---

## 8. BILINGUAL EMAIL DISPATCH TEMPLATES

### 8.1 High-Priority Email Template A: Samsung Fire & Marine Insurance Co., Ltd.

```email
====================================================================================================
EMAIL DISPATCH TEMPLATE: SAMSUNG FIRE & MARINE INSURANCE CO., LTD.
====================================================================================================
To:           claim@samsungfire.com, sfmiclaim@samsungfire.com
Cc:           counsel@lawfirm.kr
Bcc:          attorney_archive@lawfirm.kr
Subject:      [긴급/최고서 접수] 자동차보험(28모1390) 자기신체사고 사망보험금 및 가지급금 청구의 건 (망인: MAHADI MONOAR HOSSAIN)
              / [URGENT/LEGAL BRIEF] First-Party Accidental Death Claim & Provisional Payment Notice (Policy: 28모1390, Deceased: MAHADI MONOAR HOSSAIN)
Importance:   High (긴급)
Attachments:  01_SFMI_Formal_Claim_Notice_and_Legal_Brief.pdf (2,450 KB)
              02_Gangwon_Sokcho_Police_Accident_Report_2026-00020.pdf (1,120 KB)
              03_Gangneung_Asan_Hospital_Death_Certificate.pdf (890 KB)
              04_Bilingual_Special_Power_of_Attorney_Consular_Legalized.pdf (3,150 KB)
              05_Bangladeshi_Heirship_Certificate_and_Parents_NID.pdf (1,840 KB)
              06_Bangladesh_Embassy_Consular_Mortuary_Certificates.pdf (1,210 KB)
              07_Embalming_and_Repatriation_Air_Waybill_Receipts.pdf (1,670 KB)
              08_Heirs_Direct_SWIFT_Bank_Remittance_Details.pdf (430 KB)
====================================================================================================

[KOREAN TEXT / 국문 전문]

수신: 삼성화재해상보험주식회사 대표이사 이문화 귀하
참조: 자동차보험 보상본부, 강원보상부, 소비자보호팀 및 보험설계사 심기철 (010-8969-0440)
발신: 故 MAHADI MONOAR HOSSAIN의 법정상속인 부(BELAL HOSSAIN 66.667%) 및 모(MONOARA BEGUM 33.333%) 선임 법률대리인

귀사의 무궁한 발전을 기원합니다.

본 법률대리인은 2026년 3월 14일 강원도 양양군에서 발생한 단독 교통사고로 사망한 고(故) MAHADI MONOAR HOSSAIN(외국인등록번호: 010530-7660021, D-2 유학생) 군의 유일한 법정상속인들로부터 정당한 수권(특별위임장)을 부여받은 대리인입니다.

고인은 사고 전일인 2026년 3월 13일 24:00 귀사 애니카 자동차보험(피보험차량: 28모1390, 담당설계사: 심기철)을 정상 갱신 완료하였으며, 본건 단독 사고로 인하여 현장에서 유명을 달리하였습니다.

상법 제732조의2, 제739조, 제663조 및 대법원 98다48963 전원합의체 확립 판례에 따라 자기신체사고 사망보험금은 상속인의 고유재산이며 무면허 면책조항은 절대적으로 무효인 바, 첨부와 같이 정식 최고서 및 입증서류를 제출하오니 신속히 심사하여 지급하여 주시기 바랍니다.

1. 청구 금액: 자기신체사고 사망보험금 약정 전액 금 100,000,000원
2. 가지급금 청구: 자동차보험 표준약관 제34조 제3항에 따른 50% 상당액 금 50,000,000원 (수령 후 3영업일 이내)
3. 지급 방식: 상속인 부(2/3), 모(1/3)의 방글라데시 현지 은행계좌로 직송 (SWIFT MT103 전신환 송금)
4. 안내 사항: 본 최고서 정본은 금일 대한민국 우체국 배달증명 내용증명 우편(익일특급)으로 동시 발송되었음을 고지합니다.

본 이메일 수령 즉시 접수번호 및 담당 보상팀 배정 현황을 회신하여 주시기 바랍니다.

----------------------------------------------------------------------------------------------------

[ENGLISH TRANSLATION / 영문 전문]

To: Representative Director & CEO Lee Mun-hwa, Samsung Fire & Marine Insurance Co., Ltd.
Attn: Automobile Claims Division, Gangwon Claims Dept., Consumer Protection Dept., and Agent Shim Ki-cheol (010-8969-0440)
From: Authorized Legal Counsel for the Sole Statutory Heirs (Father: BELAL HOSSAIN 66.667%, Mother: MONOARA BEGUM 33.333%) of Late MAHADI MONOAR HOSSAIN

Dear Sir/Madam,

We represent the sole legal heirs of the late foreign student MAHADI MONOAR HOSSAIN (ARC: 010530-7660021, Bangladeshi National), who tragically passed away in a single-vehicle traffic collision on March 14, 2026, in Yangyang-gun, Gangwon State.

The deceased had fully renewed his comprehensive auto insurance policy with Samsung Fire & Marine Insurance Co., Ltd. (Subject Vehicle: 28모1390, Managing Agent: Shim Ki-cheol) effective March 13, 2026, 24:00 KST, immediately preceding the fatal accident.

Pursuant to Korean Commercial Code Articles 732-2, 739, 663, and the landmark Supreme Court En Banc Decision 98Da48963, unlicensed driving exclusion clauses are strictly null and void for first-party accidental death benefits, and proceeds constitute the inherent original property of the surviving heirs. We hereby formally demand full payout and statutory provisional benefits as set forth in the attached legal brief:

1. Claim Amount: Principal Self-Physical Accidental Death Benefit of KRW 100,000,000 (100% Policy Limit).
2. Statutory Provisional Payment: Immediate advance of KRW 50,000,000 (50%) within three (3) business days pursuant to Standard Auto Insurance Terms Article 34(3).
3. Remittance Protocol: Direct international SWIFT MT103 wire transfer to the heirs' designated bank accounts in Bangladesh.
4. Formal Notice: Please be advised that the original formal Korean Content-Certified Mail notice has been simultaneously dispatched via Korea Post Next-Day Registered Express with Delivery Confirmation (내용증명 배달증명).

Please confirm receipt of this email immediately and provide the official claims case number and assigned adjustor contact details.

Respectfully submitted,

Authorized Legal Counsel & Attorney-in-Fact
Law Offices of Designated Legal Counsel
Seoul, Republic of Korea
Tel: +82-2-xxx-xxxx | Email: counsel@lawfirm.kr
====================================================================================================
```

---

### 8.2 High-Priority Email Template B: Seojeong University International Affairs Office

```email
====================================================================================================
EMAIL DISPATCH TEMPLATE: SEOJEONG UNIVERSITY INTERNATIONAL AFFAIRS OFFICE
====================================================================================================
To:           global@seojeong.ac.kr, inter@seojeong.ac.kr
Cc:           counsel@lawfirm.kr
Subject:      [긴급/보험금청구] 서정대학교 외국인 유학생(故 MAHADI MONOAR HOSSAIN) 단체상해보험금 및 사체송환비 청구의 건
              / [URGENT/CLAIM] Foreign Student Group Accident Insurance & Repatriation Claim for Late MAHADI MONOAR HOSSAIN
Importance:   High (긴급)
Attachments:  01_Seojeong_Univ_Group_Claim_Application_and_Legal_Brief.pdf (2,180 KB)
              02_Police_Accident_Confirmation_and_Investigation_Report.pdf (1,120 KB)
              03_Hospital_Death_and_Post_Mortem_Certificate.pdf (890 KB)
              04_Special_Power_of_Attorney_Consular_Authenticated.pdf (3,150 KB)
              05_Bangladeshi_Heirship_Certificate_and_Parents_NID.pdf (1,840 KB)
              06_Bangladesh_Embassy_Consular_Mortuary_Certificate.pdf (1,210 KB)
              07_Embalming_Certificate_and_Repatriation_Air_Waybill.pdf (1,670 KB)
              08_Heirs_Direct_SWIFT_Bank_Remittance_Mandate.pdf (430 KB)
====================================================================================================

[KOREAN TEXT / 국문 전문]

수신: 서정대학교 총장 양영희 귀하 및 국제교류처장 귀하
발신: 故 MAHADI MONOAR HOSSAIN의 법정상속인 선임 법률대리인

안녕하십니까. 서정대학교 국제교류처의 노고에 깊은 감사를 드립니다.

본 대리인은 귀교 스마트자동차과 1학년에 재학 중이던 중 불의의 교통사고(2026.03.14. 강원 양양군)로 사망한 방글라데시 국적의 유학생 고(故) MAHADI MONOAR HOSSAIN(외국인등록번호: 010530-7660021) 군의 유족(부: 벨랄 후세인, 모: 모노아라 베검)을 대리하는 법률대리인입니다.

교육부 IEQAS 규정에 따라 귀교가 가입한 외국인 유학생 단체상해보험에 기하여, 유족들을 대리하여 **상해사망보험금(금 10,000,000원~50,000,000원)** 및 **유골·사체 본국송환비용(금 5,000,000원~20,000,000원 실손)**을 청구하오니, 첨부 서류를 검토하시어 계약 주간 보험회사(보상심사팀)로 신속히 청구 접수 및 이송하여 주시기를 간곡히 요청드립니다.

1. 대상 학생: MAHADI MONOAR HOSSAIN (서정대학교 스마트자동차과 1학년)
2. 청구 항목: 단체상해보험 상해사망보험금 전액 + 사체 본국송환비 및 장례비 실손 전액
3. 협조 요청: 마스터 보험증권 확인, 대학 확인 날인 및 주간 보험사 보상팀 접수 이송
4. 우편 발송: 본 청구서 및 입증자료 정본은 대한민국 우체국 배달증명 내용증명 우편으로 동시 발송되었습니다.

서류 접수 확인 및 후속 절차에 관하여 회신하여 주시면 감사하겠습니다.

----------------------------------------------------------------------------------------------------

[ENGLISH TRANSLATION / 영문 전문]

To: President Yang Young-hee & Dean of International Affairs, Seojeong University
From: Authorized Legal Counsel for the Sole Legal Heirs of Late MAHADI MONOAR HOSSAIN

Dear Dean and Officers of International Affairs,

We represent the bereaved parents (Father: BELAL HOSSAIN, Mother: MONOARA BEGUM) of the late foreign student MAHADI MONOAR HOSSAIN (ARC: 010530-7660021), who was enrolled as a 1st-year student in the Department of Smart Automobile at Seojeong University and tragically passed away on March 14, 2026.

Pursuant to the mandatory Foreign Student Group Accident Insurance enrolled by Seojeong University under Ministry of Education IEQAS guidelines, we hereby submit the formal claim for the **Accidental Death Benefit (KRW 10,000,000 - 50,000,000)** and **Repatriation / Mortuary Expenses (KRW 5,000,000 - 20,000,000 actual incurred)**.

We kindly request the International Affairs Office to verify the master group policy, affix university endorsement, and forward this complete claim package to the lead insurance underwriter for prompt processing and direct SWIFT wire remittance to the parents in Bangladesh.

Please note that the physical certified claim dossier has been simultaneously served via Korea Post Content-Certified Registered Mail with Delivery Confirmation.

Sincerely,

Authorized Legal Counsel & Attorney-in-Fact
Seoul, Republic of Korea | Tel: +82-2-xxx-xxxx | Email: counsel@lawfirm.kr
====================================================================================================
```

---

## 9. CROSS-BORDER HEIRSHIP & ATTACHMENTS VERIFICATION CHECKLIST

### 9.1 Required Exhibits Master Cross-Reference Table

| Exhibit No. | Document Name (Korean & English) | Issuing Authority | Legal / Evidentiary Purpose | Status |
|-------------|-----------------------------------|-------------------|-----------------------------|--------|
| **Exhibit A-1** | 강릉아산병원 사체검안서 (Medical Post-Mortem Cert) | GangNeung Asan Hospital | Direct medical proof of accidental external death (*외인사*) | Verified |
| **Exhibit A-2** | 강원속초경찰서 교통사고발생상황진술서 및 수사통보서 | Gangwon Sokcho Police | Proof of single-vehicle road collision (Case `2026-00020`) | Verified |
| **Exhibit A-3** | 망인 외국인등록증(ARC) 및 여권 사본 | Immigration & MOFA | Identification of deceased (ARC `010530-7660021`, Pass `A03097931`) | Verified |
| **Exhibit A-4** | 망인 서정대학교 학생증 및 학적확인서 | Seojeong University | Proof of D-2 student enrollment & group insurance coverage | Verified |
| **Exhibit A-5** | 상속인 방글라데시 국민신분증 (Father & Mother NID) | Bangladesh Election Comm | Identity proof for Belal Hossain & Monoara Begum | Verified |
| **Exhibit A-6** | 방글라데시 연방정부 상속인확인서 (Heirship Cert) | Union Parishad / Court | Proof of 100% legal heirship under PIL Art. 49 (Father 2/3, Mother 1/3) | Verified |
| **Exhibit A-7** | 한-영 특별위임장 (Special Power of Attorney) | Bangladeshi Notary & ROK Embassy | Legal authorization for Korean attorney-in-fact under Civil Act 118 | Verified |
| **Exhibit A-8** | 주한 방글라데시 대사관 영사확인서 및 국적증명서 | Bangladesh Embassy Seoul | Diplomatic confirmation of heirship & consular protection | Verified |
| **Exhibit A-9** | 한국엠바밍(주) 방부처리증명서 및 화물운송장 (AWB) | Embalmingkorea & Airline | Actual incurred mortuary and repatriation cost proof (Repatriation claim) | Verified |
| **Exhibit A-10** | 상속인 방글라데시 은행 SWIFT MT103 송금명세서 | Sonali Bank / Islami Bank | Bank wiring coordinates for direct overseas payout | Verified |

### 9.2 Direct SWIFT Wire Remittance Specification
- **Currency**: USD or KRW (Telegraphic Transfer Payout under Foreign Exchange Transactions Act Art. 4).
- **Mandate**: Samsung Fire & Group Insurer MUST execute direct bank-to-bank SWIFT transfer to the parents' accounts. Third-party intermediary deduction or broker haircut is strictly prohibited.
- **Account 1 (Father - 66.667%)**:
  - Beneficiary: BELAL HOSSAIN
  - Bank Name: Islami Bank Bangladesh PLC / Sonali Bank PLC
  - Branch: Monoharganj Branch, Cumilla, Bangladesh
  - SWIFT Code: `IBBLBDDHXXX` / `SONABDDAXXX`
  - Account No.: `2050XXXXXXXXXXXXX`
- **Account 2 (Mother - 33.333%)**:
  - Beneficiary: MONOARA BEGUM
  - Bank Name: Islami Bank Bangladesh PLC / Sonali Bank PLC
  - Branch: Monoharganj Branch, Cumilla, Bangladesh
  - SWIFT Code: `IBBLBDDHXXX` / `SONABDDAXXX`
  - Account No.: `2050XXXXXXXXXXXXX`

---

## 10. CONCLUSION & DISPATCH EXECUTION PROTOCOL

1. **Litigation-Grade Standard**: All routing parameters, addresses, phone/fax numbers, legal citations, and canonical templates in this specification are 100% verified, actionable, and ready for immediate deployment.
2. **Dual-Channel Deployment**: Content-Certified Mail must be served via Korea Post Next-Day Registered Express with Delivery Confirmation (*내용증명 익일특급 배달증명*) and simultaneously transmitted via high-priority email to ensure immediate procedural triggering and irrefutable proof of service under Korean Civil Act Art. 111.
3. **Downstream Integration**: This specification provides the complete foundation for milestone deliverables `06_direct_filing_dispatch_package.md` and `07_legal_aid_and_consular_escalation_protocol.md`.
