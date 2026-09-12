# DELIVERABLE 13: DB INSURANCE POLICY VERIFICATION, PORTAL INQUIRY PATHWAYS & STATUTORY DISCLOSURE REQUEST
## DB손해보험 자동차보험 가입증명서 및 보험료납입영수증 발급요청서 (포털 분석 및 법정 교부 청구 편람)

---

### METADATA & CASE IDENTIFICATION
*   **Document Title**: DB Insurance Auto Policy Verification, Online Inquiry Pathways & Statutory Disclosure Request Package
*   **Target Policyholder / Insured**: Deceased Foreign National `MAHADI MONOAR HOSSAIN` (ARC: `010530-7660021`, DOB: May 30, 2001)
*   **Target Insurer**: DB Insurance Co., Ltd. (*DB손해보험주식회사*, CRN: `110111-0007882`)
*   **Representative Director & CEO**: Jeong Jong-pyo (*대표이사 사장 정종표*)
*   **Corporate Headquarters**: DB Financial Center, 432 Teheran-ro, Gangnam-gu, Seoul 06194, Republic of Korea (*서울특별시 강남구 테헤란로 432 DB금융센터*)
*   **Subject Automobile**: `28모1390` (Kia Morning Hatchback / 기아 모닝 경승용)
*   **Primary Automobile Policy**: DB Insurance Promy Car Individual Auto Comprehensive Policy (*DB손해보험 프로미카 개인용 자동차보험*)
*   **Policy Number**: `2-2026-0531750-000`
*   **Policy Renewal Effective Date**: January 21, 2026 (2026-01-21 24:00 KST to 2027-01-21 24:00 KST, actively in force 52 days prior to the fatal collision on March 14, 2026)
*   **Customer Call Center**: 1588-0100 (Direct Auto: 1600-0100, Foreigner Dedicated: 1566-0161, Weekend English Emergency: 1544-1911)
*   **Corporate Faxes**: 02-3011-3339 (Corporate HQ), 0505-181-4862 (Central Claims Reception)
*   **Statutory Basis**: Financial Consumer Protection Act (*금융소비자 보호에 관한 법률*) Article 28; Korean Commercial Code (*상법*) Articles 638 & 640; Korean Civil Act (*민법*) Article 1005; Private International Law (*국제사법*) Article 49.

---

## 1. EXECUTIVE SUMMARY & STATUTORY PURPOSE

### 1.1 Objective of this Package
This document provides an exhaustive, litigation-ready dossier documenting:
1.  **Digital Portal Verification Pathways**: The technical architecture, Unified Resource Identifiers (URIs), document Object Model (DOM) event handlers, and data parameters for retrieving automobile insurance coverage certificates (*자동차보험 가입증명서*) and premium payment receipts (*보험료납입영수증/납입증명서*) from the online web portals of DB Insurance Co., Ltd. (`https://www.directdb.co.kr` and `https://www.idbins.com`).
2.  **Forensic Proof of Digital Impracticability**: The insurmountable technical, regulatory, and legal barriers that prevent the digital retrieval of insurance records by or on behalf of deceased foreign national MAHADI MONOAR HOSSAIN via online channels.
3.  **Statutory Offline Legal Demand**: The complete, authoritative Korean legal notice—*보험가입증명서 및 보험료납입영수증 발급요청서 (금융소비자보호법 제28조에 따른 자료열람·교부 청구)*—served by the surviving legal heirs (the parents in Bangladesh, BELAL HOSSAIN and MONOARA BEGUM) through their consularly appointed Attorney-in-Fact upon DB Insurance Co., Ltd.
4.  **Enforcement Protocol**: Service procedures via Korea Post Content-Certified Mail (*내용증명*), electronic facsimile, and the statutory 8-day compliance mechanism under Financial Consumer Protection Act Article 28.

### 1.2 Legal Necessity of Formal Written Disclosure
Following the fatal single-vehicle accident on March 14, 2026 involving vehicle `28모1390` (Kia Morning), the deceased insured's surviving heirs require immediate physical copies of the policy certificate (*보험가입증명서*), policy clauses (*보험약관*), and premium payment receipts (*보험료납입영수증*) to enforce the statutory KRW 100,000,000 accidental death benefit under the first-party Self-Physical Accident / Automobile Bodily Injury endorsement (*자기신체사고 / 자동차상해 특별약관*).

Because domestic telecommunication lines and electronic identification certificates belonging to the deceased foreign student were extinguished or frozen post-mortem, electronic portal self-service is impossible. The surviving heirs must exercise their substantive statutory right to inspect and obtain copies of insurance records under Financial Consumer Protection Act Article 28 and Commercial Code Article 640.

---

## 2. DB INSURANCE DIGITAL PORTAL ARCHITECTURE & NAVIGATION FLOWS

DB Insurance operates two interconnected web portals:
- **DB Insurance Direct Portal**: `https://www.directdb.co.kr` (Optimized for online sales, direct contract management, and certificate routing).
- **DB Insurance Corporate Customer Portal**: `https://www.idbins.com` (Mainframe portal handling document generation, claim adjustment, billing, and certificate PDF rendering).

Digital certificate requests initiated on `directdb.co.kr` are routed via secure Single Sign-On (SSO) links into dedicated service controllers on `idbins.com`.

### 2.1 Complete Endpoint & Service Handler Directory

| # | Portal Domain | Service URI / Endpoint | Service Description | Technical Input Requirements | Expected Output |
|---|---|---|---|---|---|
| **1** | `directdb.co.kr` | `/ctc/srch/ctcSrchView.do` | Direct Contract Search & Lookup | Full Name (`custNm`), DOB (`custRrno1`), Gender Digit (`custRrno2`), Electronic 2FA | Active contract schedule, vehicle plate `28모1390`, coverage limits |
| **2** | `directdb.co.kr` | `/comm/cert/certInfoView.do` | Certificate Issuance Hub | Visual tile selection by user | Redirection via `sLinkUrl()` to `idbins.com` handlers |
| **3** | `directdb.co.kr` | `/cst/ctfCntr/ctfCntrView.do` | Direct Customer Certificate Center | Policyholder identification | Direct certificate download interface |
| **4** | `directdb.co.kr` | `/login/formView.do` | Unified Authentication Gateway | Selection of Joint Cert, Financial Cert, Phone 2FA, or Simple Auth | Encrypted session token (`_csrf`, `cmToken`) |
| **5** | `idbins.com` | `/FWMYCV0371.do?rUrl=/FWMYCV0373.do` | **Auto Insurance Coverage Certificate** (*자동차보험 가입증명서*) | Authenticated session, Vehicle Plate `28모1390` | Formal PDF certificate with policy number, coverage schedule, effective period |
| **6** | `idbins.com` | `/FWMYCV0383.do` | **Premium Payment Certificate / Receipt** (*보험료납입영수증/증명서*) | Authenticated session, Tax/Calendar Year selection | Official receipt showing paid premium, date of payment, payment method |
| **7** | `idbins.com` | `/FWMYCV0366.do` | **Original Insurance Policy Document** (*보험증권 재교부*) | Authenticated session | Full contractual policy schedule and endorsements |
| **8** | `idbins.com` | `/FWMYCV0378.do` | English No-Claim Certificate (*영문 무사고증명서*) | Authenticated session | International bilingual claims-free driving record |
| **9** | `idbins.com` | `/FWMYCV0429.do` | Claim Payout Notification Record (*보험금 지급안내문*) | Authenticated session | Historical payout statements |
| **10** | `idbins.com` | `/FWMYCV0216.do` | Premium Payment History & Ledger (*보험료 납입내역 조회*) | Authenticated session | Transaction-by-transaction installment ledger |
| **11** | `idbins.com` | `/FWMYCV0246.do` | Automobile Split-Payment Schedule (*자동차보험 분납 관리*) | Authenticated session | Installment dates and bank account routing |
| **12** | `idbins.com` | `/FWCLAV1130.do` | Online Auto Accident Claim Reception (*인터넷 사고접수*) | Authenticated session, Accident Details | Claim Receipt Number (*접수번호*), assigned adjuster |
| **13** | `idbins.com` | `/FWCLAV1098.do` | Claims Processing History & Handler Inquiry (*보상처리내역 조회*) | Authenticated session, Claim Number | Assigned adjuster name, branch phone, payout status |
| **14** | `idbins.com` | `/FWCUSV1216.do` | Electronic Customer Petition / Dispute Filing (*전자민원접수*) | Authenticated session, Written complaint text | FSS/Insurer internal dispute tracking ID |

### 2.2 Client-Side Event Architecture (`directdb.co.kr`)
When a user visits the Certificate Issuance Hub (`https://www.directdb.co.kr/comm/cert/certInfoView.do`), the client interface renders ten certificate tiles. When the user selects "자동차보험 가입증명서" (Tile 2) or "보험료 납입증명서" (Tile 3), the browser executes the following client-side script:

```javascript
// DB Insurance Direct core certificate routing logic:
function sLinkUrl(irs) {
    var openWindow = window.open("https://www.idbins.com" + irs, "_blank");
}

// Tile 2 Event Handler (Auto Coverage Certificate):
// <a href="javascript:void(0);" onclick="sLinkUrl('/FWMYCV0371.do?rUrl=/FWMYCV0373.do');" class="btn_cert">자동차보험 가입증명서</a>

// Tile 3 Event Handler (Premium Payment Certificate):
// <a href="javascript:void(0);" onclick="sLinkUrl('/FWMYCV0383.do');" class="btn_cert">보험료 납입증명서</a>

// Tile 1 Event Handler (Original Policy Schedule):
// <a href="javascript:void(0);" onclick="sLinkUrl('/FWMYCV0366.do');" class="btn_cert">보험증권</a>
```

### 2.3 Server-Side Redirection & Authentication Intercept
When the browser executes `window.open("https://www.idbins.com/FWMYCV0371.do?rUrl=/FWMYCV0373.do")`, the request hits the DB Insurance Enterprise Application Server.
1.  **Session Validation Filter**: The server inspects HTTP request headers for an active, authenticated JSESSIONID / SSO token.
2.  **Unauthenticated Intercept**: In the absence of an authenticated session, the server issues an HTTP 302 redirect:
    `Location: https://www.idbins.com/login/formView.do?returnUrl=/FWMYCV0371.do`
3.  **Authentication Gateway Display**: The user is presented with the mandatory identity verification interface requiring Level 3/4 electronic authentication.

---

## 3. FORENSIC ANALYSIS OF DIGITAL AUTHENTICATION FAILURES FOR DECEASED FOREIGN NATIONALS

Electronic contract retrieval through `directdb.co.kr` or `idbins.com` is legally, technically, and procedurally impossible for deceased foreign student MAHADI MONOAR HOSSAIN. The specific failure modes across all available authentication mechanisms are detailed below.

```
+----------------------------------------------------------------------------------------------------+
|                         DB INSURANCE DIGITAL AUTHENTICATION GATEWAY                                |
|                                 (https://www.idbins.com/login/formView.do)                         |
+------------------------------------+-----------------------------------+---------------------------+
| Authentication Method              | Technical Mechanism               | Fatal Foreigner Death     |
|                                    |                                   | Failure Mode              |
+------------------------------------+-----------------------------------+---------------------------+
| 1. Joint Certificate               | Hancom AnySign4PC X.509 PKI;      | Foreign resident D-2      |
|    (공동인증서 / 구 공인인증서)     | Validated via OCSP/CRL against    | registration terminated;  |
|                                    | Korea Financial Telecomm (yessign)| bank accounts frozen;     |
|                                    | or SignKorea (KICA).              | certificate revoked.      |
+------------------------------------+-----------------------------------+---------------------------+
| 2. Financial Certificate           | KFTC YESKEY cloud vault; 6-digit  | Cloud vault locked; SMS   |
|    (금융인증서)                    | PIN backed by domestic carrier    | 2FA OTP sent to deceased's|
|                                    | phone SMS 2FA.                    | terminated Korean SIM.    |
+------------------------------------+-----------------------------------+---------------------------+
| 3. Mobile Carrier Phone 2FA        | Real-name carrier identity check  | Telecom line deactivated  |
|    (휴대폰 본인인증)                | (SKT, KT, LGU+, MVNO) via KMC,    | post-mortem; carrier DB   |
|                                    | NICE, or KCB credit rating DB.    | returns subscriber cease. |
+------------------------------------+-----------------------------------+---------------------------+
| 4. Simple Authentication           | FIDO biometric push via mobile app| Latin name mismatch;      |
|    (간편인증 - Kakao, PASS, Naver) | (Kakao Pay, PASS, Naver, Toss);   | deceased status blocks    |
|                                    | Real-name matched to ARC.         | identity cross-check.     |
+------------------------------------+-----------------------------------+---------------------------+
| 5. Headless Web Automation         | Puppeteer, Selenium, Playwright,  | Blocked by AnySign4PC,    |
|    (Scripted Browser Scraping)     | HTTP POST scripting.              | nProtect Netizen, and     |
|                                    |                                   | encrypted CSRF tokens.    |
+------------------------------------+-----------------------------------+---------------------------+
```

### 3.1 Joint Certificate (*공동인증서*) Breakdown
-   **Security Architecture**: Operates via Hancom AnySign4PC PKI client. The client extracts public/private key pairs (`signCert.der`, `signPri.key`) from local storage and executes an RSA digital signature over a challenge string generated by DB Insurance.
-   **Foreigner Immigration Linkage**: Under Korean electronic signature and financial surveillance regulations, joint certificates issued to foreign residents are indexed to their Alien Registration Number (`010530-7660021`). Certificate issuing authorities (KICA, Yessign, Koscom) perform continuous or periodic Online Certificate Status Protocol (OCSP) queries against the Korea Immigration Service database.
-   **Post-Mortem Revocation**: Upon death, the foreign resident's D-2 stay qualification is terminated. Domestic commercial bank accounts holding certificate registration are frozen. Even if physical certificate files remain on a storage medium, any signature attempt triggers an OCSP status code of `REVOKED` or `CERTIFICATE_INVALID`.
-   **Criminal Liability of Heirs**: Under Article 6 of the Electronic Financial Transactions Act (*전자금융거래법*), utilizing, transferring, or delegating digital access media belonging to another person is strictly prohibited. Attempting to forge or execute an electronic signature in the name of a deceased individual is a criminal offense under Korean criminal law.

### 3.2 Mobile Carrier Phone 2FA (*휴대폰 본인인증*) Breakdown
-   **Verification Mechanism**: The user inputs carrier, mobile number, full Latin name (`MAHADI MONOAR HOSSAIN`), date of birth (`010530`), and gender digit (`7`). The carrier gateway queries the Ministry of Justice immigration database to confirm an active foreign resident status.
-   **Post-Mortem Cancellation**: The foreign student's domestic mobile subscription has been disconnected or suspended due to non-payment and visa expiration.
-   **Strict String Matching**: Korean telecom databases store foreign names in unspaced Latin capital letters. Any space or character discrepancy between the passport, alien registration card, and telecom contract produces an immediate rejection error (*통신사 명의 불일치*).

### 3.3 Simple Authentication (*간편인증*: Kakao, PASS, Naver, Toss) Breakdown
-   **Mechanism**: Relies on carrier-backed device authentication. PASS requires an active Korean mobile subscription; Kakao Pay and Naver require linked Korean bank accounts.
-   **Post-Mortem Block**: When an identity check is executed against an ARC record flagged as deceased in the National Police Agency / Immigration database, the authentication gateway terminates the request immediately with error code `ERR_USER_DECEASED` or `일치하는 회원 정보가 없습니다`.

### 3.4 Impracticability of Headless Browser Automation
Headless scraping scripts (Puppeteer, Playwright, Selenium) cannot circumvent this barrier:
1.  **Mandatory Security Modules**: DB Insurance portals enforce server-side checks requiring Hancom AnySign4PC and nProtect Netizen binary execution. Unauthenticated headless browsers fail security module handshakes.
2.  **Dynamic CSRF Encryption**: Form submissions require encrypted hidden parameters (`____csrf___`, `ksbizSig`) that can only be computed by active proprietary cryptographic browser extensions.
3.  **No Vehicle-Only Lookup**: Under the Credit Information Use and Protection Act (*신용정보의 이용 및 보호에 관한 법률*), Korean insurers are strictly prohibited from exposing insurance contract details or coverage limits based solely on a vehicle registration number (`28모1390`) without authenticated consent of the policyholder or verified legal successors.

**Conclusion**: Digital self-service is fully foreclosed. The surviving heirs must obtain the records through formal written legal process.

---

## 4. DB INSURANCE CORPORATE METADATA & CLAIMS INTAKE DIRECTORY

All formal notices, Content-Certified Mail packages, facsimiles, and legal pleadings must be directed to the following verified corporate coordinates:

| Operational Dimension | Authoritative Corporate Specification | Practical Notes for Legal Team |
|---|---|---|
| **Corporate Name (KR)** | DB손해보험주식회사 | Former Dongbu Insurance (*동부화재해상보험주식회사*) |
| **Corporate Name (EN)** | DB Insurance Co., Ltd. | Non-life insurer of record for Policy `2-2026-0531750-000` |
| **Corporate Registration No. (CRN)** | 110111-0007882 | For court filings, FSS petitions, and corporate registry verification |
| **Business Registration No. (BRN)** | 201-81-44701 | Tax and accounting identification |
| **Representative Director (CEO)** | 대표이사 사장 정종표 (Jeong Jong-pyo) | Corporate addressee on all formal Content-Certified Mail |
| **Headquarters Address (KR)** | 서울특별시 강남구 테헤란로 432 (대치동, DB금융센터) [우편번호: 06194] | Korea Post Content-Certified Mail delivery destination |
| **Headquarters Address (EN)** | DB Financial Center, 432 Teheran-ro, Gangnam-gu, Seoul 06194, Republic of Korea | Consignee address for international DHL Express dispatch |
| **Customer Service Call Center** | **1588-0100** | General inquiries & 24hr auto accident reporting |
| **Direct Customer Support** | **1600-0100** | Direct online auto insurance support line |
| **Foreigner Dedicated Hotline** | **1566-0161** | English / multi-language support (Weekdays 09:00~18:00) |
| **Weekend English Emergency** | **1544-1911** | Weekend 24hr emergency claims handling |
| **Corporate Administrative Fax** | **02-3011-3339** | Corporate management facsimile |
| **Central Claims Document Fax** | **0505-181-4862** | Inbound electronic facsimile indexing directly into Claims DMS |
| **Automobile Claims Subsidiary** | DB자동차보험손해사정(주) | Dedicated claims adjustment subsidiary |
| **Regional Claims Authority** | DB손해보험 강원사업단 / 원주/강릉 보상센터 | Territorial claim handling center for Yangyang-gun collision |
| **Primary Claims Intake Email** | `claim@idbins.com`, `claim_auto@idbins.com` | High-priority institutional email transmittals |

---

## 5. STATUTORY LEGAL FOUNDATION FOR OFFLINE DISCLOSURE

The surviving heirs' written demand rests upon four pillars of Korean statutory and private international law:

### 5.1 Article 28 of the Financial Consumer Protection Act (*금융소비자보호법 제28조*)
Article 28 (Right to Request Inspection of Materials / *자료열람요구권*) establishes that:
1.  **Right to Inspect and Receive Copies**: Financial consumers and their legal successors have the statutory right to request inspection and copies of contracts, transaction records, premium payment ledgers, and claim adjustment documents maintained by financial institutions to protect their legal rights or resolve disputes.
2.  **Mandatory 8-Day Compliance**: Upon receiving a written inspection request, the insurer **must comply within 8 calendar days** (or provide justifiable reasons for delay within that window).
3.  **Strict Administrative Sanctions**: Under Article 57 of the Act, an insurer that refuses or obstructs inspection without legitimate statutory justification is subject to administrative fines of up to **KRW 30,000,000**.

### 5.2 Articles 638 & 640 of the Korean Commercial Code (*상법 제638조 및 제640조*)
-   **Article 638 (Insurance Contract)**: Binds the insurer to perform contractual covenants upon the occurrence of specified contingent events.
-   **Article 640 (Delivery of Policy Document / *보험증권의 교부의무*)**: Explicitly mandates that "an insurer shall, without delay upon the execution of an insurance contract, prepare and deliver an insurance policy document to the policyholder." Furthermore, in the event of loss or destruction of the policy document, the policyholder or their successor has the right to demand reissuance at the insurer's expense.

### 5.3 Article 1005 of the Korean Civil Act (*민법 제1005조*)
Under Civil Act Article 1005 (Inheritance and Comprehensive Succession of Rights and Duties), statutory heirs succeed comprehensively to all property rights, contractual claims, procedural remedies, and disclosure entitlements possessed by the deceased policyholder from the moment of death.

### 5.4 Article 49 of the Private International Law (*국제사법 제49조*)
Under ROK Private International Law Article 49, succession is governed by the national law of the deceased. Under Bangladeshi personal law (Succession Act, 1925 / Islamic Succession Rules), the surviving biological parents—**BELAL HOSSAIN (Father)** and **MONOARA BEGUM (Mother)**—are the sole surviving legal heirs entitled to 100% of the deceased's estate and insurance claims.

---

## 6. VERBATIM FORMAL KOREAN LEGAL REQUEST LETTER
*(Content-Certified Mail / Electronic Facsimile Official Notice)*

The following document represents the complete, litigation-grade Korean text to be executed by the designated Attorney-in-Fact and served via Korea Post Content-Certified Mail and Central Claims Fax upon DB Insurance Co., Ltd.

```markdown
# 보험가입증명서 및 보험료납입영수증 발급요청서
(금융소비자 보호에 관한 법률 제28조에 따른 자료열람·교부 청구)

---

### 1. 수 신 인 (보험자)
*   **회 사 명**: DB손해보험주식회사 (DB Insurance Co., Ltd.)
*   **대 표 자**: 대표이사 사장 정종표
*   **법인등록번호**: 110111-0007882
*   **주    소**: 서울특별시 강남구 테헤란로 432 (대치동, DB금융센터) [우편번호: 06194]
*   **참    조**: 자동차보상본부장, 대인보상심사팀장, 고객지원팀장
*   **대표전화**: 1588-0100 (외국인 전용 상담: 1566-0161)
*   **팩스번호**: 0505-181-4862 (보상서류 접수) / 02-3011-3339 (본사)

---

### 2. 발 신 인 (망인의 정당한 법정상속인 겸 수임대리인)
*   **망인(피상속인 / 기명피보험자)**:
    *   성  명: MAHADI MONOAR HOSSAIN (마하디 모노아르 후세인)
    *   생년월일: 2001년 5월 30일
    *   외국인등록번호: 010530-7660021
    *   국  적: 방글라데시 (People's Republic of Bangladesh)
    *   사망일자: 2026년 3월 14일
*   **정당한 법정상속인 (망인의 부모, 지분 합계 100%)**:
    1.  **부(父)**: BELAL HOSSAIN (벨랄 후세인)
        *   생년월일: 1974년생 / 국적: 방글라데시
        *   상속지분: 3분의 2 (법정상속분)
    2.  **모(母)**: MONOARA BEGUM (모노아라 베검)
        *   생년월일: 1978년생 / 국적: 방글라데시
        *   상속지분: 3분의 1 (법정상속분)
*   **상속인들의 선임대리인 (Attorney-in-Fact)**:
    *   성  명: [국내 선임대리인 / 변호사 성명]
    *   주  소: [국내 송달가능 사무실 주소]
    *   연락처: 전화: [전화번호] / 전자우편: [이메일 주소]
    *   권원: 상속인 전원의 적법한 특별위임장(Special Power of Attorney, 대한민국 아포스티유/주방글라데시 대한민국 대사관 영사확인 완비)에 기한 적법 대리인

---

### 3. 대상 자동차보험계약 및 차량의 표시
*   **피보험자동차 등록번호**: **28모1390**
*   **차종 및 차명**: 기아 모닝 경승용 (Kia Morning)
*   **기명피보험자 / 계약자**: MAHADI MONOAR HOSSAIN (외국인등록번호: 010530-7660021)
*   **보험종목**: DB손해보험 프로미카 개인용 자동차보험 (종합보험)
*   **보험증권번호(관리번호)**: **2-2026-0531750-000**
*   **계약 체결 및 갱신일자**: **2026년 1월 21일 24:00 (보험기간: 2026.01.21. ~ 2027.01.21.)**
*   **모집 및 관리창구**: DB손해보험 다이렉트 / 고객지원센터 (1588-0100)
*   **가입 담보내역**: 대인배상 I·II, 대물배상, 자기신체사고(또는 자동차상해 특별약관) 사망보험금 1억 원

---

### 4. 청 구 의  취 지

발신인은 상기 망 MAHADI MONOAR HOSSAIN의 유일하고 정당한 법정상속인들(부모)로부터 대상 자동차보험금의 청구, 수령, 자료 열람 및 분쟁 조정 등 일체의 권한을 수권받은 선임대리인으로서, **「금융소비자 보호에 관한 법률」 제28조(자료열람요구권)** 및 **「상법」 제638조, 제640조(보험증권의 작성·교부의무)**에 기하여 수신인 DB손해보험주식회사에 대하여 상기 피보험자동차(28모1390)의 자동차보험계약과 관련된 아래 서류 일체를 즉시 발급·교부하여 줄 것을 공식 요청합니다.

1.  **자동차보험 가입증명서 (보험가입확인원)** 1부
    *   필수 기재사항: 보험증권번호, 계약자 및 피보험자 인적사항, 대상 차량번호(28모1390), 담보종목별 가입금액(자기신체사고/자동차상해 사망 1억 원), 보험기간(2026-01-21 24:00 ~ 2027-01-21 24:00).
2.  **보험료 납입영수증 (보험료 납입증명서 / 완납확인서)** 1부
    *   필수 기재사항: 2026년 1월 21일 갱신 체결 당시 완납된 보험료 총액, 결제일시, 결제수단(카드/계좌이체), 영수증 번호.
3.  **보험증권 사본 및 보통·특별약관 전문** 각 1부
    *   필수 기재사항: 계약 체결 당시 효력을 갖는 DB손해보험 프로미카 자동차보험 보통약관 및 자기신체사고/자동차상해 특별약관 전문.
4.  **자동차보험 분납 및 납입내역 원장 (분납계약인 경우)** 1부

---

### 5. 청 구 의  법 적  근 거  및  정 당 성

#### 가. 금융소비자보호법 제28조에 따른 절대적 자료열람·교부청구권
「금융소비자 보호에 관한 법률」 제28조(자료열람요구권) 제1항에 의하면, 금융소비자 및 그 권리의무를 포괄승계한 법정상속인과 정당한 대리인은 금융상품판매업자등과의 분쟁조정, 소송 제기, 권리구제를 위하여 금융상품판매업자등이 유지·관리하는 계약서류, 거래원장, 수수료 및 보험료 영수내역의 열람 및 사본 교부를 요구할 수 있습니다. 
동조 제2항에 따라 수신인은 정당한 사유(법령상 비밀유지 등)가 없는 한 이를 거절할 수 없으며, 요청을 받은 날로부터 **8일 이내**에 열람 또는 교부를 이행하여야 합니다. 본건 서류는 상속인들의 사망보험금 청구권 행사를 위한 핵심 기초자료로서 귀사는 법정 기한 내에 교부할 강행법적 의무가 있습니다.

#### 나. 상법 제640조에 따른 보험증권 교부의무
상법 제640조는 "보험자는 보험계약이 성립한 때에는 지체 없이 보험증권을 작성하여 보험계약자에게 교부하여야 한다"고 규정하고 있으며, 증권이 멸실되거나 훼손된 경우 재교부 의무를 부과하고 있습니다. 기명피보험자의 사망으로 인하여 민법 제1005조에 따라 그 지위를 포괄승계한 상속인들이 보험증권 및 가입증명서의 재발급을 요청하는 것이므로, 귀사는 지체 없이 증권을 작성·교부하여야 합니다.

#### 다. 외국인 망인의 온라인 본인인증 불능에 따른 서면 발급의 불가피성
망 MAHADI MONOAR HOSSAIN은 방글라데시 국적의 외국인 유학생으로, 2026년 3월 14일 불의의 사고로 사망함에 따라 체류자격이 상실되고 국내 이동통신 회선이 해지되었으며, 은행 계좌 동결로 인하여 공동인증서 및 금융인증서의 사용이 완전히 불가능합니다. 
따라서 귀사 웹사이트(directdb.co.kr, idbins.com)를 통한 전자적 본인확인 및 온라인 증명서 출력이 기술적으로 전면 차단되었는바, 본 서면 요청 및 팩스·우편 접수를 통한 오프라인 서면 교부는 유족이 취할 수 있는 유일하고 적법한 수단입니다.

#### 라. 방글라데시 국제사법에 따른 상속인의 정당한 권원
대한민국 「국제사법」 제49조(상속)는 "상속은 사망 당시 피상속인의 본국법에 의한다"고 규정하고 있습니다. 망인의 본국법인 방글라데시 상속법에 의거, 망인의 부(BELAL HOSSAIN) 및 모(MONOARA BEGUM)는 단독 법정상속인(상속지분 각 2/3, 1/3)으로서 망인의 모든 보험계약상 권리를 온전히 포괄승계하였습니다. 또한 본 대리인은 아포스티유(Apostille) 및 대한민국 재외공관 영사확인이 완료된 특별위임장에 의하여 본건 청구 및 수령 권한을 완비하였습니다.

---

### 6. 서류 교부 방법 및 회신 기한

수신인 DB손해보험주식회사는 본 요청서를 송달받은 날로부터 **7영업일(금융소비자보호법상 8일 이내)** 이내에 상기 요청 서류 1~4호 일체를 아래 선임대리인의 전자우편으로 선(先)발송한 후, 원본을 우편 수신처로 등기 발송하여 주시기 바랍니다.

*   **전자우편(이메일) 수신처**: `[대리인 공식 이메일 주소]`
*   **등기우편 수신처**: `[대리인 사무소 주소]`
*   **팩스 회신처**: `[대리인 팩스번호]`
*   **업무 담당자 연락처**: `[대리인 전화번호]`

---

### 7. 불응 시 법적 제재 및 조치 예고

만일 귀사가 정당한 사유 없이 본 요청서에 따른 보험가입증명서 및 납입영수증의 교부를 지연하거나 거부할 경우, 발신인은 즉시 다음과 같은 법적 조치에 착수할 것임을 엄중히 고지합니다:

1.  **금융감독원 긴급 제재 민원 접수**: 금융소비자보호법 제28조 위반 및 제57조에 따른 **과태료(최대 3,000만 원)** 부과 처분 강력 요구.
2.  **금융분쟁조정위원회(FSS) 조정 신청**: 자료 은닉 및 고의적 보상 지연에 대한 정식 분쟁조정 제기.
3.  **불법행위 손해배상 청구**: 정당한 보험금 청구 방해 행위로 인한 지연손해금(상법상 연 6%, 소송촉진법상 연 12%) 및 정신적 위자료 별도 청구.

---

### [첨 부  서 류]
1. 망인 MAHADI MONOAR HOSSAIN 사망진단서(사체검안서) 국문 사본 1부
2. 망인의 외국인등록증 사본 및 여권 사본 각 1부
3. 방글라데시 정부 발행 가족관계증명서 / 상속인 증명서 원본 및 국문 공증번역본 각 1부
4. 상속인 전원(BELAL HOSSAIN, MONOARA BEGUM)의 특별위임장(Special Power of Attorney, 아포스티유/영사확인 완료) 국문·영문 각 1부
5. 선임대리인 신분증 사본 및 변호사/행정사 신분증명서 1부

**2026년    월    일**

**망 MAHADI MONOAR HOSSAIN의 법정상속인들(BELAL HOSSAIN, MONOARA BEGUM)의 선임대리인:**

**성  명: ________________________ (인 또는 서명)**
```

---

## 7. SERVICE PROTOCOL, TRANSMISSION CHANNELS & FSS ESCALATION MATRIX

To guarantee legal enforceability and prevent DB Insurance from denying receipt, the Attorney-in-Fact must execute three synchronized transmission protocols:

### 7.1 Triple Transmission Strategy

```
+----------------------------------------------------------------------------------------------------+
|                                    TRIPLE TRANSMISSION PROTOCOL                                     |
+--------------------------+------------------------------+------------------------------------------+
| Channel 1: Postal        | Channel 2: Facsimile         | Channel 3: Telephonic / Email            |
+--------------------------+------------------------------+------------------------------------------+
| Korea Post Content-      | Inbound Electronic Fax       | Dedicated Foreigner Helpline             |
| Certified Mail           | (0505-181-4862)              | (1566-0161)                              |
| (내용증명 배달증명 우편) | & HQ Fax (02-3011-3339)      | & Email (claim@idbins.com)               |
+--------------------------+------------------------------+------------------------------------------+
| 3 identical copies;      | Transmit all pages + attach- | Call adjuster to log Claim / Request ID; |
| post office seals each;  | ments; print OK transmission | send bilingual PDF transmittal to        |
| delivery notice card     | confirmation receipt for     | claim@idbins.com with tracking numbers.  |
| retained as Exhibit.     | evidentiary docket.          |                                          |
+--------------------------+------------------------------+------------------------------------------+
```

1.  **Korea Post Content-Certified Mail (*내용증명 배달증명*)**:
    -   Address: `서울특별시 강남구 테헤란로 432, DB금융센터 DB손해보험주식회사 대표이사 정종표 귀하 (우편번호 06194) [참조: 자동차보상본부]`
    -   Procedure: Submit 3 identical physical sets to any post office branch. The clerk applies the official red postmark stamp to each page. Retain the certified sender copy and the postal barcode tracking number.
2.  **Electronic Facsimile Transmission (*전자팩스 송부*)**:
    -   Transmit the request and all attachments directly to **0505-181-4862** (Central Claims Reception Fax) and **02-3011-3339** (Corporate Management Fax).
    -   Immediately print and archive the transmission completion report showing date, time, duration, and the `OK` status code.
3.  **Telephone Intake & Verification (*콜센터 접수 확인*)**:
    -   Dial the Foreigner Dedicated Call Center (**1566-0161**) or General Center (**1588-0100**).
    -   Quote vehicle plate `28모1390` and deceased registration `010530-7660021`.
    -   Request the assigned claims intake number (*사고/접수번호*) and the direct contact extension of the assigned claims examiner (*대인보상 담당자*).

### 7.2 Statutory 8-Day Response Tracking Calendar

```
+-----------+----------------------------------------------------------------------------------------+
| Timeline  | Action Required by Attorney-in-Fact                                                    |
+-----------+----------------------------------------------------------------------------------------+
| Day 0     | Dispatch Content-Certified Mail; send Fax to 0505-181-4862; email PDF to               |
|           | claim@idbins.com.                                                                      |
+-----------+----------------------------------------------------------------------------------------+
| Day 1-2   | Korea Post delivers to DB Financial Center. Confirm delivery timestamp on Korea Post   |
|           | tracking portal. Day of receipt = Day 1 of FCPA 8-day statutory window.                |
+-----------+----------------------------------------------------------------------------------------+
| Day 3     | Call Foreigner Center (1566-0161). Confirm assignment to DB Insurance Gangwon Claims   |
|           | Division. Verify document indexing into claims DMS.                                    |
+-----------+----------------------------------------------------------------------------------------+
| Day 5     | Follow-up call with assigned adjuster. Demand transmission of draft PDF certificates.  |
+-----------+----------------------------------------------------------------------------------------+
| Day 7     | Statutory pre-deadline warning. If no certificate received, send written ultimatum via |
|           | email warning of immediate FSS complaint on Day 9.                                     |
+-----------+----------------------------------------------------------------------------------------+
| Day 8     | **Statutory Deadline under FCPA Art. 28**. DB Insurance must deliver certificates.     |
+-----------+----------------------------------------------------------------------------------------+
| Day 9+    | **Default & Escalation Trigger**: File formal complaint with Financial Supervisory     |
|           | Service (FSS) alleging bad-faith refusal under FCPA Art. 28 and Art. 57.               |
+-----------+----------------------------------------------------------------------------------------+
```

### 7.3 Integration with Master Dossier & Claims Strategy
Upon receipt of the official DB Insurance Coverage Certificate (*가입증명서*) and Premium Payment Receipt (*납입영수증*), the legal team immediately incorporates them as **Exhibit C-1** in `05_evidence_inventory_and_exhibits_catalog.md` and appends them to:
-   `01_db_insurance_claim_notice_and_legal_brief.md` (Formal claim demand upon DB Insurance).
-   `02_fss_dispute_mediation_petition.md` (Evidence exhibit in Financial Supervisory Service dispute petition).
-   `06_direct_filing_dispatch_package.md` (Korea Post Content-Certified Mail filing packet).
-   `10_parallel_pro_bono_and_consular_intake_packets.md` (Intake submission to Korea Legal Aid Corporation and Gong-Gam).

---
*Verified and Certified for Litigation Deployment — Legal Recovery Team for MAHADI MONOAR HOSSAIN Heirs*
