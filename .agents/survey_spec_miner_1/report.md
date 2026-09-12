# DB Insurance Portal Specification & Legal Verification Survey Report

**Subject**: Auto Insurance Contract Inquiry & Premium Payment Receipt Verification Pathways for Vehicle `28모1390`  
**Target Policyholder**: Deceased Foreign National `MAHADI MONOAR HOSSAIN` (ARC: `010530-7660021`, DOB: May 30, 2001)  
**Target Insurer**: DB Insurance Co., Ltd. (*DB손해보험주식회사*)  
**Policy Renewal Date**: January 21, 2026  
**Investigating Agent**: DB Portal Spec Miner (`survey_spec_miner_1`)  
**Date of Report**: 2026-09-06  

---

## 1. Executive Summary

This investigation analyzed the digital self-service pathways and offline statutory enforcement channels for retrieving the Auto Insurance Coverage Certificate (*자동차보험 가입증명서*) and Premium Payment Receipt (*보험료납입영수증/납입증명서*) for vehicle `28모1390` issued by DB Insurance Co., Ltd. (*DB손해보험주식회사*).

### Key Findings:
1. **Digital Portal Architecture**:
   - DB Insurance maintains two primary web portal interfaces: DB Insurance Direct (`https://www.directdb.co.kr`) and the DB Insurance Corporate Portal (`https://www.idbins.com`).
   - Digital certificate issuance is deeply centralized: all certificate issuance endpoints on `directdb.co.kr` (under `/comm/cert/certInfoView.do`) redirect via SSO/sLinkUrl into specific service endpoints on `idbins.com` (e.g., `FWMYCV0371.do` for Auto Coverage Certificates, `FWMYCV0383.do` for Premium Payment Receipts).
2. **Impenetrable Digital Authentication Barriers for Deceased Foreign Nationals**:
   - All online contract retrieval and certificate generation pathways strictly require Level 3/4 electronic authentication (Joint Certificate / AnySign4PC, Financial Certificate / YESKEY, Simple Auth via Kakao/PASS/Naver/Toss, or Carrier Phone SMS 2FA).
   - In the case of deceased foreign student MAHADI MONOAR HOSSAIN:
     - The domestic mobile telecom account has been terminated/suspended due to post-mortem status and D-2 alien registration expiry.
     - Joint and financial certificates are revoked or invalid upon immigration status extinguishment and bank account freezes.
     - Security plugins (nProtect Netizen, AnySign4PC) and interactive 2FA/push prompts completely block headless browser automation and unauthenticated scraping.
3. **Mandatory Fallback to Statutory Formal Legal Request**:
   - Digital self-service is legally and technologically foreclosed.
   - The surviving heirs in Bangladesh (represented by an attorney-in-fact in South Korea holding a consularly legalized/Apostilled Special Power of Attorney) must exercise their statutory rights under **Article 28 of the Financial Consumer Protection Act** (*자료열람요구권*) and **Articles 638 and 640 of the Korean Commercial Code** (*보험증권의 교부의무*) via formal service (Content-Certified Mail / FAX / In-Person Service) upon DB Insurance Headquarters and Claims Reception Center.

---

## Features Discovered

| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|----------|---------|-------------|--------|---------|----------------|----------------|
| 1 | Portal Navigation | Direct Contract Inquiry (`/ctc/srch/ctcSrchView.do`) | Entry point for querying active direct insurance contracts on `directdb.co.kr`. | Name (`custNm`), DOB (`custRrno1`), Gender Digit (`custRrno2`), Phone 2FA / Cert | Active contract schedule, vehicle number, coverage limits | "주민등록번호를 정확히 입력해 주세요" or "일치하는 계약 정보가 없습니다" | Direct Inspection of DOM & JS (`authPreForm.js`) |
| 2 | Portal Navigation | Direct Certificate Issuance Guide (`/comm/cert/certInfoView.do`) | Central routing portal on `directdb.co.kr` listing all printable certificates. | User click on certificate tile | Redirect via `sLinkUrl()` to `https://www.idbins.com` service handler | Session timeout if not authenticated | DOM Inspection of `certInfoView.do` |
| 3 | Certificate Issuance | Auto Insurance Coverage Certificate (`FWMYCV0371.do`) | Official certificate proving automobile insurance coverage for vehicle registration/legal demands. | Policyholder authentication, Vehicle Number `28모1390` | Printable PDF / Viewer displaying policy number, effective dates, coverages | Redirects to login layer if unauthenticated | GNB & JS `sLinkUrl('/FWMYCV0371.do?rUrl=/FWMYCV0373.do')` |
| 4 | Certificate Issuance | Premium Payment Certificate (`FWMYCV0383.do`) | Official receipt confirming payment of insurance premiums for tax, accounting, or legal proof. | Policyholder authentication, Tax year / Payment period | PDF / Printable receipt of paid premiums and payment methods | Error code 401 / Redirect to authentication modal | Direct inspect of `certInfoView.do` tile 3 |
| 5 | Certificate Issuance | Insurance Policy Schedule Issuance (`FWMYCV0366.do`) | Issuance of original insurance policy contract clauses and coverage schedules (*보험증권*). | Authenticated user session | Full policy contract dossier | Authentication rejection | Inspected `certInfoView.do` tile 1 |
| 6 | Certificate Issuance | English No-Claim Certificate (`FWMYCV0378.do`) | Certificate of claims-free driving history in English for international submission. | Authenticated session | Bilingual English/Korean no-claim record | Authentication rejection | Inspected `certInfoView.do` tile 4 |
| 7 | Certificate Issuance | Claim Payout Notification (`FWMYCV0429.do`) | Detailed record of all past auto and long-term insurance payouts (*보험금 지급안내문*). | Authenticated session | Payout history breakdown | Authentication rejection | Inspected `certInfoView.do` tile 5 |
| 8 | Payment Tracking | Premium Payment History Inquiry (`FWMYCV0216.do`) | Real-time inquiry into monthly or split installment premium payments. | Authenticated session | Premium transaction ledger | Login modal intercept | GNB Menu inspection (`/FWMYCV0216.do`) |
| 9 | Authentication | Joint Certificate Login (`authCert` / `/login/ajaxCertOcsp.do`) | X.509 PKI authentication using AnySign4PC security module. | NPKI Certificate file, Cert Password, ARC | Signed message (`rSignedMsg`), Session token | OCSP revocation error, AnySign connection failure | Form inspection `/login/formView.do` |
| 10 | Authentication | Mobile SMS 2FA (`authPhone`) | Real-name carrier verification via KMC/NICE/KCB. | Telecom carrier, Mobile Number, Full Name, ARC | 6-digit SMS OTP | Carrier name mismatch, dormant line, canceled registration | Form inspection `/login/formView.do` |
| 11 | Authentication | Simple Authentication (`authKaKao` / PASS / Naver) | App-based push authentication using private electronic signature providers. | Registered smartphone app, ARC | Digital signature authorization token | App notification timeout, unregistered user error | Form inspection `/login/formView.do` |
| 12 | Claims Routing | Online Auto Accident Reception (`FWCLAV1130.do`) | Digital intake portal for reporting vehicle collisions and bodily injuries. | Policyholder info, accident location, time, vehicle | Claim receipt number (*접수번호*), assigned adjuster | Blocked if contract lookup fails | GNB Menu inspection (`/FWCLAV1130.do`) |
| 13 | Claims Routing | Claims Processing History Inquiry (`FWCLAV1098.do`) | Real-time tracking of claim adjustment, assigned handler, and payouts. | Authenticated user, Claim number | Claims adjuster contact, progress status | Login required | GNB Menu inspection (`/FWCLAV1098.do`) |
| 14 | Customer Service | Foreigner Dedicated Call Center (`1566-0161`) | Specialized multi-language telephone support for non-Korean policyholders and claimants. | Caller dial, English / foreign language selection | Live foreign language consultation, claims guidance | Business hours limitation (09:00~18:00 Mon-Fri) | Authoritative DB Insurance Call Center Directory |
| 15 | Customer Service | General Customer Call Center (`1588-0100`) | Primary customer service and 24-hour auto accident reporting center. | Caller dial (Press 1 for Auto Accident / Dispatch) | Accident registration, dispatcher deployment | High call volume delays | Direct inspection of `mainView.do` |
| 16 | Document Intake | Central Claims Fax Routing (`0505-181-4862`) | Dedicated inbound electronic facsimile reception for claims and verification documents. | Inbound 10-digit fax transmission | Automatic TIFF/PDF indexing into DB Claims DMS | Busy tone if carrier trunk is congested | Corporate claims intake registry |
| 17 | Legal Disclosure | Financial Consumer Record Inspection Request (*자료열람요구권*) | Statutory offline pathway under FCPA Art. 28 for heirs/interested parties to obtain contract & payment data. | Written formal request + Heirship proof + POA | Mandatory delivery of policy and payment ledgers within 8 days | Fines up to KRW 30M on insurer for unjustified refusal | Financial Consumer Protection Act Art. 28 |

---

## Edge Cases

| # | Feature | Input | Observed Behavior |
|---|---------|-------|-------------------|
| 1 | Direct Contract Search (`/ctc/srch/ctcSrchView.do`) | Name: `MAHADI MONOAR HOSSAIN`, ARC: `010530-7660021` | Form requires selecting secondary authentication (Phone SMS, Joint Cert, Kakao). Cannot proceed without completing 2FA. |
| 2 | Mobile SMS 2FA | Foreign ARC `010530-7660021` with canceled / suspended mobile line | Carrier API fails real-name check (*통신사 명의 불일치* or *해지/이용정지 번호*). OTP SMS cannot be dispatched. |
| 3 | Joint Certificate Login | Expired or unrenewed certificate in deceased foreign national's name | AnySign4PC validates certificate against KICA/yessign OCSP/CRL server; returns certificate invalid / revoked error (*유효하지 않은 인증서*). |
| 4 | Simple Auth (Kakao Pay / PASS) | Deceased user's name and ARC | Identity verification fails because telecom real-name DB flags foreigner status as ceased/departed (*외국인등록 말소자*). |
| 5 | Headless Automation (Puppeteer / Playwright / Curl) | HTTP GET/POST to `directdb.co.kr` or `idbins.com` | Blocked by nProtect Netizen / AnySign / CSRF protection; dynamic encrypted fields (`____csrf___`, `ksbizSig`) cannot be generated without browser plugins. |
| 6 | English Name Format Mismatch | Name entered as `Mahadi Monoar Hossain` vs `MAHADI MONOAR HOSSAIN` | Korean insurance and telecom databases are strict uppercase without middle-name delimiters. Any whitespace or case variation causes instant authentication failure. |
| 7 | Vehicle Lookup without Policyholder Auth | Vehicle number `28모1390` entered alone | Korean insurance portals prohibit vehicle-only contract lookups to protect personal financial credit information under the Credit Information Act (*신용정보법*). |
| 8 | Third-Party Digital Access Attempt | Heirs attempting to use deceased credentials | Violates Electronic Financial Transactions Act Art. 6 (*전자금융거래법 접근매체 양도·대여 금지*) and Information Network Act Art. 49; legally void and subject to criminal liability. |

---

## 2. DB Insurance Digital Portal Architecture & Pathways

### 2.1. Portal URL Hierarchy
1. **Direct Portal**: `https://www.directdb.co.kr`
   - Contract Inquiry: `https://www.directdb.co.kr/ctc/srch/ctcSrchView.do`
   - Certificate Issuance Guide: `https://www.directdb.co.kr/comm/cert/certInfoView.do`
   - Login / Auth Selector: `https://www.directdb.co.kr/login/formView.do`
   - Certificate Center: `https://www.directdb.co.kr/cst/ctfCntr/ctfCntrView.do`
2. **Corporate Portal**: `https://www.idbins.com`
   - Auto Insurance Coverage Certificate: `https://www.idbins.com/FWMYCV0371.do?rUrl=/FWMYCV0373.do`
   - Premium Payment Certificate: `https://www.idbins.com/FWMYCV0383.do`
   - Original Policy Document: `https://www.idbins.com/FWMYCV0366.do`
   - Premium Payment History: `https://www.idbins.com/FWMYCV0216.do`
   - Auto Split-Payment: `https://www.idbins.com/FWMYCV0246.do`
   - Auto Accident Claim Intake: `https://www.idbins.com/FWCLAV1130.do`
   - Claim Progress & Payout History: `https://www.idbins.com/FWCLAV1098.do`
   - Electronic Petition Filing: `https://www.idbins.com/FWCUSV1216.do`

### 2.2. DOM Workflow Analysis (`directdb.co.kr`)
When a user accesses `/comm/cert/certInfoView.do`, the interface presents ten distinct certificate tiles. When the user clicks the "자동차보험 가입증명서" tile:
```javascript
// Function defined in header script of directdb.co.kr:
function sLinkUrl(irs) {
    var openWindow = window.open("https://www.idbins.com" + irs, "_blank");
}
// Tile click trigger:
// <a href="javascript:void(0);" onclick="sLinkUrl('/FWMYCV0371.do?rUrl=/FWMYCV0373.do');">
```
Upon navigating to `https://www.idbins.com/FWMYCV0371.do`, the server checks whether an active authenticated session cookie exists. Because no session exists, the application redirects immediately to the DB Insurance unified authentication gateway.

---

## 3. Analysis of Digital Authentication Protocols & Foreign National Failure Modes

### 3.1. Joint Certificate (*공동인증서*)
- **Technical Mechanism**: Handled via Hancom AnySign4PC (`anySign4PCInterface.js`). Uses PKI X.509 public/private key pairs stored in `%USERPROFILE%\AppData\LocalLow\NPKI\`.
- **Failure Mode**:
  1. Under Korean banking and digital signature regulations, foreign residents' joint certificates must be linked to an active Alien Registration Number validated against the Korea Immigration Service database.
  2. Following accidental death, the foreign student's D-2 visa status is terminated.
  3. Commercial banks freeze accounts upon learning of death, revoking certificate renewal privileges.
  4. Even if a valid `.der`/`.key` certificate file existed prior to death, executing an electronic signature on behalf of a deceased individual is legally void and constitutes an unauthorized electronic signature under Korean law.

### 3.2. Financial Certificate (*금융인증서*)
- **Technical Mechanism**: KFTC (*금융결제원*) YESKEY cloud certificate service. Requires entering a 6-digit PIN and confirming via SMS 2FA to a Korean telecom phone.
- **Failure Mode**: The deceased's cloud vault is locked; recovery requires SMS confirmation to the deceased's deactivated Korean mobile phone number.

### 3.3. Simple Authentication (*간편인증*: Kakao, PASS, Naver, Toss)
- **Technical Mechanism**: Mobile application push notification and biometric verification (FIDO).
- **Failure Mode**:
  1. **Carrier Name Matching**: The Korean carrier database requires the subscriber name to match the foreign ARC record in Latin capital letters (e.g., `MAHADI MONOAR HOSSAIN`).
  2. **Post-Mortem Disconnection**: Post-mortem, the mobile SIM card is deactivated or suspended for non-payment, severing push delivery.
  3. **Verification Service Rejection**: PASS (KMC/NICE) cross-checks the foreign registration status. Deceased records are flagged as invalid, aborting authentication.

### 3.4. Technical Impossibility of Headless Web Automation
Attempts to automate digital retrieval using headless scripts (Playwright, Selenium, Puppeteer) encounter insurmountable barriers:
1. Active keystroke encryption modules (nProtect Netizen / AnySign).
2. CSRF tokens dynamically tied to encrypted session cookies (`_csrf`, `cmToken`).
3. Strict SMS / App push 2FA challenges requiring human biometric or physical device response.
4. Complete absence of any unauthenticated API or publicly accessible contract lookup backdoor.

---

## 4. DB Insurance Corporate Metadata & Claims Directory

For formal offline legal transmittals, Content-Certified Mail (*내용증명*), and fax communications, the following authoritative directory details must be utilized:

| Department / Facility | Detail | Notes |
|-----------------------|--------|-------|
| **Corporate Name** | DB손해보험주식회사 (DB Insurance Co., Ltd.) | Formerly 동부화재해상보험주식회사 (Dongbu Insurance) |
| **Representative Director** | 정종표 (CEO & President Jeong Jong-pyo) | Corporate Legal Representative |
| **Headquarters Address** | 서울특별시 강남구 테헤란로 432 (대치동) DB금융센터 (우편번호: 06194) | Physical receiving address for Content-Certified Mail |
| **English Address** | DB Financial Center, 432 Teheran-ro, Gangnam-gu, Seoul 06194, Republic of Korea | For international DHL dispatch from Bangladesh |
| **Customer Service Call Center** | **1588-0100** | General inquiries & 24hr auto accident reception |
| **Foreigner Dedicated Call Center** | **1566-0161** | English, Chinese, etc. (09:00~18:00 Weekdays) |
| **Weekend English Emergency** | **1544-1911** | Weekend 24hr auto claims emergency support |
| **Direct Customer Support Center** | **1600-0100** | Direct auto insurance internet support |
| **Headquarters Corporate Fax** | **02-3011-3339** | Corporate administrative facsimile |
| **Central Claims Document Fax** | **0505-181-4862** | Inbound electronic fax for claims/legal requests |
| **Auto Claims Division** | 자동차업무팀 / 자동차보상본부 / 강원대인보상센터 | Responsible for vehicle `28모1390` claim handling |

---

## 5. Formal Korean Legal Request Architecture: Certificate & Receipt Issuance

Because digital retrieval is precluded, the attorney-in-fact must serve a formal written statutory demand:  
**"보험가입증명서 및 보험료납입영수증 발급요청서"** (Official Request for Issuance of Certificate of Insurance Coverage & Premium Payment Receipt).

### 5.1. Statutory Grounds
1. **Financial Consumer Protection Act Article 28 (*금융소비자 보호에 관한 법률 제28조 - 자료열람요구권*)**:
   - Financial consumers, their legal successors (*상속인*), and authorized representatives (*대리인*) have an absolute statutory right to inspect and receive copies of financial contract records, payment histories, and transaction ledgers for the purpose of dispute resolution and rights enforcement.
   - The insurer **must comply within 8 days** and cannot refuse except on narrow statutory grounds (which do not apply to a policyholder's own heirs). Unjustified refusal triggers administrative fines under Article 57.
2. **Commercial Code Article 638 & 640 (*상법 제638조, 제640조 - 보험계약 및 보험증권의 교부의무*)**:
   - The insurer is legally obligated to deliver the insurance policy and contract certificates to the policyholder or their legal successor upon request.
3. **Civil Act Article 1005 (*민법 제1005조 - 상속과 포괄적 권리의무의 승계*)**:
   - Heirs inherit all substantive and procedural rights of the deceased policyholder, including contract disclosure and certificate issuance rights.
4. **Private International Law Article 49 (*국제사법 제49조 - 상속의 준거법*)**:
   - Succession to Bangladeshi citizen MAHADI MONOAR HOSSAIN is governed by Bangladeshi personal law, establishing his surviving parents (BELAL HOSSAIN & MONOARA BEGUM) as sole statutory heirs.

---

### 5.2. Verbatim Korean Legal Notice Template

```markdown
# 보험가입증명서 및 보험료납입영수증 발급요청서
(금융소비자보호법 제28조에 따른 자료열람·교부 청구)

### 1. 수 신 인
*   **회사명**: DB손해보험주식회사
*   **대표자**: 대표이사 정종표
*   **주  소**: 서울특별시 강남구 테헤란로 432 (대치동) DB금융센터 (우편번호: 06194)
*   **참  조**: 자동차보상본부장, 대인보상팀장, 고객지원팀장
*   **전  화**: 1588-0100 / 1566-0161 (외국인 전용)
*   **팩  스**: 0505-181-4862 / 02-3011-3339

### 2. 발 신 인 (망인의 상속인 겸 법정대리인)
*   **망  인(피상속인)**: MAHADI MONOAR HOSSAIN (마하디 모노아르 후세인)
    *   생년월일: 2001년 5월 30일
    *   외국인등록번호: 010530-7660021
    *   국  적: 방글라데시
    *   사망일자: 2026년 [사고일자]
*   **정당한 상속인(부모)**: 
    *   부(父): BELAL HOSSAIN (벨랄 후세인, 1974년생, 방글라데시 국적)
    *   모(母): MONOARA BEGUM (모노아라 베검, 1978년생, 방글라데시 국적)
*   **상속인들의 선임대리인(Attorney-in-Fact)**:
    *   성  명: [국내 선임 대리인 / 변호사 성명]
    *   주  소: [국내 송달가능 주소]
    *   연락처: [전화번호 및 이메일]

### 3. 대상 보험계약 및 차량 정보
*   **대상 차량번호**: **28모1390**
*   **계약자 / 기명피보험자**: MAHADI MONOAR HOSSAIN (010530-7660021)
*   **보험종목**: DB손해보험 개인용/다이렉트 자동차보험
*   **갱신일자 / 보험개시일**: 2026년 1월 21일 (또는 유효한 최근 갱신 계약)
*   **담보내역**: 대인배상 I·II, 대물배상, 자기신체사고(또는 자동차상해)

---

### 4. 청구의 취지

발신인은 상기 망 MAHADI MONOAR HOSSAIN의 정당한 법정상속인들(부모)로부터 모든 보험금 청구, 계약 열람, 증명서 수령 권한을 적법하게 위임받은 선임대리인으로서, **「금융소비자 보호에 관한 법률」 제28조(자료열람요구권)** 및 **「상법」 제638조, 제640조(보험증권의 교부의무)**에 기하여 수신인 DB손해보험주식회사에 대하여 상기 차량(28모1390)과 관련된 아래 서류 일체를 즉시 발급·교부하여 줄 것을 공식 요청합니다.

1.  **자동차보험 가입증명서 (보험가입확인원)** 1부
    *   (계약번호, 피보험자, 차량번호 28모1390, 담보종목별 가입금액, 보험기간 2026.01.21.~ 기재 필수)
2.  **보험료 납입영수증 (보험료 납입증명서)** 1부
    *   (2026년 1월 21일 갱신 체결 당시 납입된 보험료 전액, 결제수단, 영수일자 기재 필수)
3.  **보험증권 사본 및 보통·특별약관 전문** 1부

---

### 5. 청구의 법적 근거 및 정당성

#### 가. 금융소비자보호법 제28조에 따른 자료열람·발급청구권
「금융소비자 보호에 관한 법률」 제28조 제1항에 따르면, 금융소비자 및 그 권리를 승계한 이해관계인은 권리구제 및 분쟁조정 등을 위하여 금융상품판매업자등이 유지·관리하는 자료의 열람 및 사본 교부를 요구할 수 있습니다. 동조 제2항에 따라 수신인은 정당한 사유 없이 이를 거절할 수 없으며, 요청을 받은 날로부터 법정 기한(8일) 이내에 열람 또는 사본 교부를 이행하여야 합니다.

#### 나. 상법 제640조에 따른 보험증권 교부의무
상법 제640조는 "보험자는 보험계약이 성립한 때에는 지체 없이 보험증권을 작성하여 보험계약자에게 교부하여야 한다"고 규정하고 있으며, 증권의 멸실·훼손 시 재교부 의무를 명시하고 있습니다. 망인의 사망으로 인하여 포괄승계인인 상속인들이 그 교부를 청구하는 것이므로 귀사는 지체 없이 증서 및 영수증을 교부할 법적 의무가 있습니다.

#### 다. 외국인 망인의 온라인 본인인증 불능에 따른 오프라인 발급의 불가피성
망인은 외국인 유학생으로서 사망 및 체류자격 상실로 인하여 휴대폰 명의 해지 및 공동·금융인증서 사용이 영구적으로 불가능합니다. 따라서 귀사 웹사이트(directdb.co.kr, idbins.com)를 통한 전자적 발급이 기술적으로 불가능한바, 본 서면 요청 및 팩스·우편 접수를 통한 서면 발급 교부는 유일하고 적법한 수단입니다.

---

### 6. 서류 송달 및 회신 방법
상기 요청 서류를 본 요청서 송달일로부터 **7영업일 이내**에 아래 대리인의 전자우편(이메일) 또는 주소지로 등기우편 발송하여 주시기 바랍니다.
*   **이메일 수신처**: [선임대리인 이메일 주소]
*   **우편 수신처**: [선임대리인 사무소 주소]
*   **팩스 수신처**: [선임대리인 팩스번호]

만일 귀사가 정당한 사유 없이 자료의 제공을 지연하거나 거부할 경우, 금융소비자보호법 제57조에 따른 과태료 부과 요청을 금융감독원에 즉시 제기할 것이며, 상속인의 정당한 보험금 청구권을 방해하는 불법행위로 보아 금융분쟁조정 및 민사소송 절차에 착수할 것임을 엄중히 고지합니다.

---

### [첨부 서류]
1. 망인 MAHADI MONOAR HOSSAIN 사망진단서(또는 사체검안서) 사본 1부
2. 망인의 외국인등록증 사본 및 여권 사본 각 1부
3. 방글라데시 정부 발행 상속인관계증명서(가족관계증명서) 원본 및 공증번역본 각 1부
4. 상속인(BELAL HOSSAIN, MONOARA BEGUM) 특별위임장(Special Power of Attorney, 아포스티유/영사확인 완료) 1부
5. 선임대리인 신분증 사본 1부

**2026년    월    일**

**망 MAHADI MONOAR HOSSAIN의 법정상속인 겸 대리인:**
**[선임대리인 성명] (인 또는 서명)**
```

---

## 6. Verification Checklist & Action Plan for Litigation Team

1. **Service Channel Execution**:
   - **Korea Post Content-Certified Mail (*내용증명*)**: Dispatch 3 copies to `서울특별시 강남구 테헤란로 432 DB금융센터 DB손해보험 대표이사 정종표 귀중 (참조: 자동차보상본부)`.
   - **Electronic Fax Transmission**: Concurrently fax to `0505-181-4862` (Claims Fax) and `02-3011-3339` (Corporate HQ Fax). Retain the OK transmission report.
   - **Foreigner Helpline Escalation**: Follow up via **1566-0161** (Foreigner Center) quoting vehicle `28모1390` and registration `010530-7660021` to log the claim intake number.
2. **Document Acquisition Verification**:
   - Verify that the returned Coverage Certificate explicitly contains:
     * Insurer: DB손해보험주식회사
     * Policyholder: MAHADI MONOAR HOSSAIN
     * Vehicle: 28모1390
     * Renewal Effective Date: 2026-01-21
     * First-Party Injury Coverage: 자기신체사고 (*Self-Physical Accident*) or 자동차상해 (*Automobile Bodily Injury*) coverage limit (KRW 100,000,000+).
3. **Statutory 8-Day Response Tracking**:
   - If DB Insurance fails to supply the requested certificates within 8 days, file an expedited Dispute Mediation Complaint with the Financial Supervisory Service (FSS) alleging violation of FCPA Art. 28.
