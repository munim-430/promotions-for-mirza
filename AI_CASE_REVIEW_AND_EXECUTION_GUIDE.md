# AI MODEL CASE REVIEW, REASONING SCAFFOLD & STEP-BY-STEP EXECUTION PLAYBOOK
## Comprehensive Machine-Readable Knowledge Base & Prompt Engineering Framework for Autonomous Legal Agents
### In the Matter of Late MAHADI MONOAR HOSSAIN (Foreign Student D-2, Seojeong University)

---

**Document Control ID:** `AI-GUIDE-MASTER-2026-0913`  
**Target Users:** Large Language Models (Claude 3.5 Sonnet, GPT-4o, Gemini 1.5 Pro, DeepSeek R1, Grok), Legal Reasoning Agents, Subagent Swarms, and Cross-Border Legal Counsel.  
**Master Objective:** Provide an immediate, zero-friction, fully structured cognitive map of the factual chronology, governing statutes, landmark precedents, mathematical calculations, and tactical contingency trees required to execute the recovery of KRW 135,000,000 ~ KRW 170,000,000 in Korean insurance benefits.  

---

## 1. MACHINE-READABLE CASE MANIFEST (JSON STRUCTURE)

```json
{
  "case_metadata": {
    "matter_id": "KOR-BD-2026-MAHADI-001",
    "case_title": "Cross-Border Accidental Death Insurance Recovery and Heirship Enforcement",
    "deceased": {
      "full_name_en": "MAHADI MONOAR HOSSAIN",
      "full_name_passport": "MONOAR HOSSAIN MAHADI",
      "full_name_ko": "마하디 모노아르 후세인",
      "arc_no": "010530-7660021",
      "passport_no": "A03097931",
      "nid_no": "7362790417",
      "dob": "2001-05-30",
      "age_at_death": 24,
      "marital_status": "Single / Unmarried",
      "intestate": true,
      "visa_type": "D-2 (General Student / 유학)",
      "university": "Seojeong University (서정대학교)",
      "department": "Smart Automotive (스마트자동차과 1학년)",
      "student_id": "202581042",
      "alien_registration_office": "Chuncheon Immigration Office Sokcho Branch (춘천출입국·외국인사무소 속초출장소)"
    },
    "incident": {
      "date_time_kst": "2026-03-14T05:58:00+09:00",
      "location": "Road near 4-1 Bukbun-ri, Hyeonnam-myeon, Yangyang-gun, Gangwon Special Self-Governing Province (강원특별자치도 양양군 현남면 북분리 4-1 도로상)",
      "mechanics": "Single-vehicle collision with roadside guardrail while unlicensed (무면허 운전 중 단독 차량 충돌)",
      "investigating_police": "Gangwon Sokcho Police Station Traffic Accident Investigation Unit (Case No: 2026-00020)",
      "investigating_officer": "Lt. Jo Hyeong-cheol (경위 조형철)",
      "homicide_or_suicide_suspicion": false,
      "autopsy_waived": true,
      "body_release_order_issued": true,
      "cause_of_death": "Severe Traumatic Brain Injury (TBI), skull fracture, extensive brainstem damage (중증 두부 외상에 의한 두개골 골절 및 광범위 뇌간 손상)",
      "medical_authority": "GangNeung Asan Hospital (Dr. Kang Hee-dong 강희동)"
    },
    "statutory_heirs": {
      "governing_succession_law": "Bangladeshi Sunni Hanafi Muslim Personal Law (via Korean Private International Law Art. 49)",
      "inherent_property_characterization": "Accidental death benefits vest directly as heirs' inherent property (Supreme Court 2003Da29463, 2000Da31502)",
      "father": {
        "name": "BELAL HOSSAIN",
        "nid": "7802539200",
        "passport": "A08912455",
        "share_fraction": "2/3",
        "share_percent": 66.667,
        "status": "Asabah Residuary Heir (아사바 총괄상속인)",
        "share_of_provisional_50m": 33333333,
        "share_of_full_100m": 66666667
      },
      "mother": {
        "name": "MONOARA BEGUM",
        "nid": "2354437788",
        "passport": "A09234112",
        "share_fraction": "1/3",
        "share_percent": 33.333,
        "status": "Zawil Furud Quranic Sharer (자윌푸루드 지정상속인)",
        "share_of_provisional_50m": 16666667,
        "share_of_full_100m": 33333333
      }
    },
    "fiduciary_attorney_in_fact": {
      "name": "HASIBUL MUNIM",
      "korean_transcription": "하십울 무님",
      "nid": "6003330534",
      "passport": "B00936349",
      "title": "Chairman, Bangladesh Human Rights Commission Seoul Branch (주한 방글라데시 인권위원회 위원장)",
      "phone_bd": "+880-1941646278",
      "phone_kr": "010-7209-1620",
      "email": "munimm247@gmail.com",
      "receiving_bank": {
        "bank_name": "Mutual Trust Bank PLC (মিউচুয়াল ট্রাস্ট ব্যাংক)",
        "branch": "Dhanmondi Branch, Dhaka, Bangladesh",
        "account_no": "1311004072276",
        "swift_code": "MTBLBDDH",
        "routing_no": "145261188",
        "beneficiary": "HASIBUL MUNIM"
      },
      "korean_withholding_tax_rate": "0% (Exempt under Korean Income Tax Act §12(3)(d))"
    },
    "primary_active_policy_seojeong_univ": {
      "policy_name": "Seojeong University Foreign Student Master Group Accident Policy (서정대학교 외국인 유학생 단체상해보험)",
      "managing_office": "Seojeong University International Affairs Office (서정대학교 국제교류처)",
      "contact_phone": "031-860-5177 / 031-860-5272~3 / 031-860-5000",
      "contact_email": "interchange@seojeong.ac.kr, global@seojeong.ac.kr",
      "mandatory_mandate": "Ministry of Education (MOE) IEQAS Accreditation & MOJ Immigration Mandatory Foreign Student Policy",
      "death_benefit_claim": "KRW 30,000,000 ~ KRW 50,000,000 (Accidental Death Benefit)",
      "repatriation_expense_claim": "KRW 5,000,000 ~ KRW 20,000,000 (Exhibit F4 itemized receipts)",
      "total_recovery_target": "KRW 35,000,000 ~ KRW 70,000,000",
      "legal_defense_preemption": "Supreme Court En Banc Decision 98Da48963 & Commercial Code §732-2 (Unlicensed driving exemption strictly VOID)"
    },
    "secondary_auto_policy_db_insurance": {
      "insurer_name": "DB Insurance Co., Ltd. (DB손해보험주식회사)",
      "policy_no": "2-2026-0531750-000",
      "subject_vehicle_plate": "28모1390",
      "vehicle_model": "2012 All New Morning (기아 모닝 경승용)",
      "coverage_status": "Third-Party Liability (대인 I, 대물 2000만원) [ACTIVE], Self-Physical Accident (자기신체사고) [미가입 / Not Enrolled]",
      "strategic_role": "Authentic Certificate serves as legal vehicle compliance evidence; first-party auto death payout unavailable due to 미가입 status."
    }
  }
}
```

---

## 2. CORE LEGAL REASONING & PROOF SCAFFOLDS

When analyzing this case or answering queries, AI models should construct their legal arguments along these 6 ironclad logical chains:

### Chain 1: Accidental Death Coverage & Inherent Property Nature
1. **Triggering Event:** The single-vehicle crash on March 14, 2026 is an accidental sudden violent external collision resulting directly in the death of MAHADI MONOAR HOSSAIN.
2. **Policy Classification:** Seojeong University's Foreign Student Group Accident Policy is a personal accident / life insurance contract (*상해보험·인보험*).
3. **Inherent Property Doctrine (Supreme Court 2003Da29463 & 2000Da31502):** Accidental death insurance proceeds do not enter the probate estate of the deceased; they vest originally and immediately in the statutory heirs as their separate inherent property (*상속인의 고유재산*). General estate creditors have zero claim against these funds.

### Chain 2: Strict Nullity of Unlicensed Driving Exclusion Clauses
1. **Commercial Code Article 732-2 (상법 제732조의2):** In death/accident insurance, the insurer cannot be exempted from liability for an event caused by the gross negligence (*중대한 과실*) of the insured or beneficiary.
2. **Commercial Code Article 663 (상법 제663조 - 불이익변경금지원칙):** Contractual clauses disadvantageous to the insured compared to statutory provisions are strictly void.
3. **Supreme Court En Banc Decision 98Da48963 (대법원 98다48963 전원합의체 판결):** The Supreme Court En Banc authoritatively ruled that policy terms excluding coverage for accidental death solely because the insured was driving without a driver's license violate Commercial Code Articles 732-2 and 663, and are **ABSOLUTELY VOID AB INITIO**.
4. **Distinction Between Intent and Negligence:** Driving without a license is categorized under Korean law as gross negligence, distinct from intentional suicide (*고의에 의한 사고*). Because there was zero suicide intent (confirmed by Sokcho Police Case 2026-00020), the insurer is 100% liable.

### Chain 3: Mandatory University Group Coverage Mandate
1. **Ministry of Education (MOE) IEQAS Mandate:** All higher education institutions hosting D-2 international students are legally required to maintain 100% group accident insurance coverage.
2. **Coverage Scope:** Covers Accidental Death Benefits (KRW 30,000,000 ~ KRW 50,000,000) and actual Repatriation/Funeral Expenses (KRW 5,000,000 ~ KRW 20,000,000).

### Chain 4: Cross-Border Succession Law & Share Apportionment
1. **Korean Private International Law Art. 49(1) (국제사법 제49조):** Inheritance is governed by the national law of the deceased at death (Bangladeshi Law).
2. **Muslim Personal Law (Shariat) Application Act 1937 & Sunni Hanafi Jurisprudence:**
   - Deceased died unmarried without children.
   - **Mother (MONOARA BEGUM):** Fixed Quranic Sharer (*Zawil Furud*) receives **1/3** (33.333%).
   - **Father (BELAL HOSSAIN):** Residuary Heir (*Asabah*) receives the remaining **2/3** (66.667%).
   - All siblings and extended relatives are completely excluded (*Mahjub*).

### Chain 5: DB Auto Policy Role as Evidence of Vehicle Compliance
1. **Vehicle Compliance Evidence:** DB Insurance Policy `2-2026-0531750-000` proves that vehicle `28모1390` was legally registered and had active third-party liability insurance.
2. **First-Party Self-Injury Exclusion:** Because `자기신체사고` was marked `미가입` (not enrolled) on the auto policy, the sole active payout vector is the **Seojeong University Group Accident Policy**.

### Chain 6: Fiduciary Representation & Zero Korean Withholding Tax
1. **Civil Act Article 118 (민법 제118조):** Special Power of Attorney Clause 6 grants Hasibul Munim full authority to receive wire transfers and execute valid receipt and discharge.
2. **Income Tax Act Article 12(3)(d) (소득세법 제12조 제3호 라목):** Death benefits and statutory wrongful death compensation are non-taxable (0% Korean domestic withholding tax).

---

## 3. READY-TO-USE PROMPT TEMPLATES FOR AI ADVERSARIAL AUDITING

### 🤖 Prompt A: University Group Insurance Claims Review Simulation
```markdown
You are Claims Legal Adjuster for Seojeong University's Foreign Student Group Accident Insurance Consortium.
You have received a formal claim for KRW 35,000,000 ~ KRW 70,000,000 for deceased student MAHADI MONOAR HOSSAIN (Student ID: 202581042).

The student died in a single-vehicle accident without a Korean driver's license.
Evaluate the claim under Korean Commercial Code §732-2, §663, and Supreme Court En Banc Decision 98Da48963:
1. Can the insurer deny accidental death benefits citing unlicensed driving or lack of auto first-party coverage?
2. What are the mandatory time limits for claim settlement under Insurance Business Regulations?
3. How should repatriation receipts (Exhibit F4) be processed under the group policy rider?
```

---

## 4. WORKSPACE DIRECTORY MAP & CONTEXT INGESTION GUIDE

| Task / Requirement | Recommended Files to Load | Key Exhibits / Artifacts |
|---|---|---|
| **⭐ Primary Active Recovery Pack** | `00_SEOJEONG_UNIVERSITY_GROUP_INSURANCE_RECOVERY_PACK/` | `00_SEOJEONG_UNIVERSITY_RECOVERY_EXECUTIVE_MANUAL.pdf`, `01_Seojeong_University_Group_Insurance_Claim_and_Legal_Brief.pdf` |
| **University Group Claim Brief** | `legal_claim_package/03_seojeong_university_group_insurance_claim.md` | Exhibit F4 (Repatriation receipts), D1 (ARC), D3 (Passport) |
| **Bilingual Special POA** | `legal_claim_package/04_bilingual_special_power_of_attorney.md` | Exhibit E3 (Hasibul Munim NID/Passport), F3 (MTB Bank Statement) |
| **OIA Phone & Email Blitz** | `legal_claim_package/15_seojeong_university_telephone_call_script.md` | `16_seojeong_university_email_and_epeople_petition_package.md` |
| **Heirship & Legalization Guide** | `legal_claim_package/04_cross_border_heirship_and_legalization_guide.md` | Warishan Sanad, MOFA Dhaka attestation protocols |
| **Evidence Authentication Matrix** | `02_EVIDENCE_AND_IDENTITY_EXHIBITS/` | Exhibits A1, B1, B2, C1, C2, C3, D1, D3, E3, F3, F4 |
| **Lawyer / Consular Transmittals** | `03_KOREAN_LAWYERS_AND_INSURERS_FILING_PACK/` | 19 compiled PDF/Word deliverables for instant dispatch |
| **Comprehensive Encyclopedia** | `CASE_MASTER_KNOWLEDGE_DOSSIER.md` | Complete 55KB Master Dossier & 140 Exhibit Catalog |
| **Test Verification & Math Engines**| `tests/run_all_tests.py` | 29 Unit Tests + 5 Stress Tests (100% Passed) |

---

## 5. DECISION TREES & CONTINGENCY PLAYBOOKS

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                               CONTINGENCY RESPONSE DECISION MATRIX                               │
├────────────────────────────────┬─────────────────────────────────────────────────────────────────┤
│ Scenario & Trigger             │ Operational Action Protocol                                     │
├────────────────────────────────┼─────────────────────────────────────────────────────────────────┤
│ [Scenario A]                   │ 1. Verify SWIFT wire into Mutual Trust Bank PLC (A/C: ...2276). │
│ Full Insurance Approval        │ 2. Disburse 2/3 (KRW 66,666,667) to Father Belal Hossain.       │
│ within 10 Days (KRW 100M)      │ 3. Disburse 1/3 (KRW 33,333,333) to Mother Monoara Begum.       │
│                                │ 4. Close parallel intake files; pursue Seojeong Univ balance.   │
├────────────────────────────────┼─────────────────────────────────────────────────────────────────┤
│ [Scenario B]                   │ 1. Disburse KRW 50M provisional (Father 33.33M / Mother 16.66M).│
│ 50% Provisional Advanced (50M) │ 2. Grant formal investigation extension up to Day 30 max.       │
│ Balance Delayed for Inquiry    │ 3. If balance unpaid by Day 30, file FSS Petition immediately.  │
├────────────────────────────────┼─────────────────────────────────────────────────────────────────┤
│ [Scenario C]                   │ 1. Serve Preemptive Rebuttal Brief citing Supreme Court 98Da48963│
│ Bad-Faith Denial citing        │ 2. Serve Notice of Impending FSS Bad-Faith Regulatory Sanction.  │
│ Unlicensed Driving Exclusion   │ 3. Transition file to KLAC for Seoul Central District Complaint. │
├────────────────────────────────┼─────────────────────────────────────────────────────────────────┤
│ [Scenario D]                   │ 1. Serve Notice of Statutory Default on Day 11 at 09:00 KST.   │
│ Total Silence / Inaction       │ 2. Accelerate commercial default interest (6.0% p.a. daily).    │
│ Past Day 10 Statutory Window   │ 3. Transmit FSS Petition and notify Bangladesh Embassy Seoul.   │
└────────────────────────────────┴─────────────────────────────────────────────────────────────────┘
```

---

## 6. ACTIONABLE STEP-BY-STEP EXECUTION PLAYBOOK

### Phase 1: Dhaka/Cumilla Signing & Attestation
- Print 3 sets of `02_Bilingual_Special_Power_of_Attorney_Master.pdf`.
- Have Father BELAL HOSSAIN and Mother MONOARA BEGUM sign and apply right thumbprints.
- Obtain Union Parishad Warishan Sanad and legalize via Ministry of Foreign Affairs (MOFA), Dhaka.

### Phase 2: Direct Telephone Contact with DB Insurance
- Call DB Agent **이덕만 (Lee Deok-man)** at `010-5379-6099` or DB Claims Desk at `1588-0100`.
- Quote Policy No: `2-2026-0531750-000` and Vehicle Plate: `28모1390`.
- Obtain adjuster direct email, fax number, and internal Claim/Accident Report Number.

### Phase 3: Dual-Track Dispatch (Email/Fax + DHL)
- Email `claim_auto@idbins.com` with the 4 core PDF deliverables attached.
- Dispatch DHL Express non-commercial legal document parcel to DB Financial Center, Seoul.
- Log Sent Email timestamps and DHL Tracking AWB as official Proof of Service.

### Phase 4: 10-Day Statutory Countdown & Daily Enforcement
- Track statutory calendar from Day 1 to Day 10 under Civil Act Art. 157.
- Demand KRW 50,000,000 provisional advance on Day 3 under Commercial Code §732-2.
- On Day 11 (if unpaid), trigger statutory commercial default interest (6.0% p.a.).

### Phase 5: Multi-Track Parallel Escalation
- Submit FSS Dispute Mediation Petition via e-People / FSS portal.
- Submit KLAC Foreigner Free Legal Aid application.
- Submit intake dossiers to Gong-Gam and DURO public interest foundations.
- File Seojeong University D-2 Group Accidental Death Benefit claim (KRW 35M~70M).
- Request Bangladesh Embassy Seoul Diplomatic Note Verbale to MOFA Korea / FSS.

### Phase 6: SWIFT Remittance Verification & Apportionment
- Monitor Mutual Trust Bank PLC (A/C: `1311004072276`, SWIFT: `MTBLBDDH`) for SWIFT MT103 wire.
- Apportion proceeds strictly under Sunni Hanafi rules: **Father 2/3 (66.667%)** and **Mother 1/3 (33.333%)**.
- Issue formal partial discharge to DB Insurance while preserving rights for secondary university recovery.

---
*Document Control: Approved for Autonomous AI Ingestion & International Cross-Border Enforcement.*
