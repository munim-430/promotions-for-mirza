# AI AGENT FORENSIC AUDIT REPORT & SOLE VIABLE RECOVERY PLAYBOOK
## Case: Late MAHADI MONOAR HOSSAIN — Cross-Border Accidental Death Insurance Recovery
### Machine-Readable Knowledge Base for Autonomous Legal Agent Execution

---

**Document ID:** `AI-FORENSIC-AUDIT-2026-0917`  
**Audit Performed By:** Antigravity AI Forensic Auditor (Claude Opus 4.6)  
**Repository Audited:** `https://github.com/munim430-ai/promotions-for-mirza`  
**Files Reviewed:** 51+ text files, 4 directories, 16 legal claim markdowns, 55KB master dossier, all Python scripts and test suites  
**Audit Date:** September 16-17, 2026  
**Report Classification:** Litigation-Grade Forensic Audit — AI Agent Operational Directive  

---

## TABLE OF CONTENTS

1. [EXECUTIVE SUMMARY FOR AI AGENTS](#1-executive-summary-for-ai-agents)
2. [VERIFIED CASE FACTS (GROUND TRUTH)](#2-verified-case-facts-ground-truth)
3. [CRITICAL ISSUE #1: DB INSURANCE PATH IS CLOSED — NO PAYOUT](#3-critical-issue-1-db-insurance-path-is-closed--no-payout)
4. [CRITICAL ISSUE #2: INTERNAL REPOSITORY CONTRADICTIONS](#4-critical-issue-2-internal-repository-contradictions)
5. [CRITICAL ISSUE #3: DATE DISCREPANCY IN CONSULAR CERTIFICATE](#5-critical-issue-3-date-discrepancy-in-consular-certificate)
6. [CRITICAL ISSUE #4: REFERENCE NUMBER INCONSISTENCY](#6-critical-issue-4-reference-number-inconsistency)
7. [CRITICAL ISSUE #5: IDENTITY NAME ORDER MISMATCH](#7-critical-issue-5-identity-name-order-mismatch)
8. [CRITICAL ISSUE #6: BANK WIRE REFERENCE ERROR](#8-critical-issue-6-bank-wire-reference-error)
9. [CRITICAL ISSUE #7: MISSING DOCUMENTS NOT IN REPOSITORY](#9-critical-issue-7-missing-documents-not-in-repository)
10. [CRITICAL ISSUE #8: DOSSIER STILL CLAIMS KRW 100M FROM DB INSURANCE](#10-critical-issue-8-dossier-still-claims-krw-100m-from-db-insurance)
11. [SOLE VIABLE RECOVERY PATH: SEOJEONG UNIVERSITY GROUP INSURANCE](#11-sole-viable-recovery-path-seojeong-university-group-insurance)
12. [STEP-BY-STEP EXECUTION PLAYBOOK (AI AGENT DIRECTIVE)](#12-step-by-step-execution-playbook-ai-agent-directive)
13. [LEGAL WEAPONS ARSENAL — STATUTES & PRECEDENTS](#13-legal-weapons-arsenal--statutes--precedents)
14. [COMPLETE DISCREPANCY MATRIX](#14-complete-discrepancy-matrix)
15. [AI AGENT VERIFICATION CHECKLIST](#15-ai-agent-verification-checklist)

---

## 1. EXECUTIVE SUMMARY FOR AI AGENTS

> **READ THIS FIRST. This section overrides all conflicting information in other repository files.**

### THE SINGLE MOST IMPORTANT FACT:
```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│  DB INSURANCE AUTO POLICY (2-2026-0531750-000) CANNOT PAY FOR THE DRIVER'S DEATH.   │
│                                                                                      │
│  자기신체사고 (Self-Physical Accident) = 미가입 (NOT ENROLLED)                        │
│  대인배상 I (Third-Party Liability) = Only covers OTHER people, not the driver       │
│                                                                                      │
│  ∴ THE ONLY PAYOUT PATH = SEOJEONG UNIVERSITY GROUP ACCIDENT INSURANCE              │
│     Recovery Target: KRW 35,000,000 ~ KRW 70,000,000                                │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

### WHY MANY FILES IN THIS REPOSITORY ARE WRONG:
The `CASE_MASTER_KNOWLEDGE_DOSSIER.md` (the 55KB "Single Source of Truth") and several `legal_claim_package/` files were drafted when the team believed KRW 100,000,000 could be recovered from DB Insurance under the Self-Physical Accident rider. **That rider was never purchased.** The README.md, AI_CASE_REVIEW_AND_EXECUTION_GUIDE.md, and the `00_SEOJEONG_UNIVERSITY_RECOVERY_EXECUTIVE_MANUAL.md` correctly acknowledge this reality, but the older claim notices and the master dossier were never fully corrected.

**Any AI agent processing this case MUST:**
1. **IGNORE** all DB Insurance first-party death benefit claims (KRW 100M, KRW 50M provisional)
2. **FOCUS 100%** on Seojeong University Group Accident Insurance (KRW 35M-70M)
3. **USE** the DB Insurance certificate ONLY as supporting evidence of lawful vehicle registration

---

## 2. VERIFIED CASE FACTS (GROUND TRUTH)

### 2.1 Deceased
```json
{
  "full_name_en": "MAHADI MONOAR HOSSAIN",
  "full_name_passport": "MONOAR HOSSAIN MAHADI",
  "full_name_ko": "마하디 모노아르 후세인",
  "arc_no": "010530-7660021",
  "passport_no": "A03097931",
  "bangladesh_nid": "7362790417",
  "dob": "2001-05-30",
  "age_at_death": 24,
  "marital_status": "Single / Unmarried / Intestate",
  "visa_type": "D-2 (General Student / 유학)",
  "university": "Seojeong University (서정대학교)",
  "department": "Smart Automotive (스마트자동차과 1학년)",
  "student_id": "202581042"
}
```

### 2.2 Incident
```json
{
  "date_time_kst": "2026-03-14T05:58:00+09:00",
  "location": "4-1 Bukbun-ri, Hyeonnam-myeon, Yangyang-gun, Gangwon-do",
  "type": "Single-vehicle collision with roadside guardrail",
  "driver_status": "Unlicensed (무면허 운전)",
  "vehicle": "Kia Morning (기아 모닝), Plate: 28모1390",
  "third_party_victims": 0,
  "cause_of_death": "Severe Traumatic Brain Injury (TBI), skull fracture, extensive brainstem damage",
  "medical_authority": "GangNeung Asan Hospital, Dr. Kang Hee-dong",
  "death_cert_no": "2026031447741948",
  "postmortem_cert_no": "2026031447738965",
  "police_case_no": "2026-00020",
  "police_station": "Gangwon Sokcho Police Station Traffic Accident Unit",
  "investigating_officer": "Lt. Jo Hyeong-cheol (경위 조형철)",
  "homicide_suspicion": false,
  "suicide_suspicion": false,
  "autopsy_waived": true
}
```

### 2.3 Sole Statutory Heirs
```json
{
  "governing_law": "Bangladeshi Sunni Hanafi Muslim Personal Law via Korean PIL Act Art. 49",
  "father": {
    "name": "BELAL HOSSAIN",
    "nid": "7802539200",
    "share": "2/3 (66.667%)",
    "role": "Asabah Residuary Heir"
  },
  "mother": {
    "name": "MONOARA BEGUM",
    "nid": "2354437788",
    "share": "1/3 (33.333%)",
    "role": "Zawil Furud Quranic Sharer"
  },
  "total": "100%",
  "other_heirs": "NONE — Father takes all residue in presence of mother under Hanafi law"
}
```

### 2.4 Authorized Attorney-in-Fact
```json
{
  "name": "HASIBUL MUNIM",
  "korean_name": "하십울 무님",
  "nid": "6003330534",
  "passport": "B00936349",
  "phone_kr": "010-7209-1620",
  "phone_bd": "+880-1941646278",
  "email": "munimm247@gmail.com",
  "title": "Chairman, Bangladesh Human Rights Commission Seoul Branch",
  "bank": {
    "name": "Mutual Trust Bank PLC",
    "branch": "Dhanmondi Branch, Dhaka, Bangladesh",
    "account": "1311004072276",
    "swift": "MTBLBDDH",
    "routing": "145261188",
    "beneficiary": "HASIBUL MUNIM"
  }
}
```

---

## 3. CRITICAL ISSUE #1: DB INSURANCE PATH IS CLOSED — NO PAYOUT

### The Problem
Multiple files in this repository claim KRW 100,000,000 can be recovered from DB Insurance Co., Ltd. This is **FALSE**.

### The Evidence

**DB Insurance Policy (2-2026-0531750-000) for vehicle 28모1390:**

| Coverage Type | Korean Name | Status | Covers Driver's Own Death? |
|:---|:---|:---|:---|
| Third-Party Liability I | 대인배상 I | ✅ Active | ❌ **NO** — Only pays for injuries to OTHER people hit by the vehicle |
| Third-Party Property | 대물배상 | ✅ Active (KRW 20M) | ❌ **NO** — Property damage to others only |
| Self-Physical Accident | 자기신체사고 / 자손 | ❌ **미가입 (NOT ENROLLED)** | This is the ONLY coverage that would pay for the driver's own death — **but it was never purchased** |

### Why 대인배상 I Cannot Help
- In this case, the deceased was **the driver** in a **single-vehicle accident** with **zero third-party victims**
- 대인배상 I is **liability insurance** — it compensates people the insured vehicle injures
- There are no third-party victims → there is no 대인배상 I claim
- The driver himself is **never** a "third party" under his own liability policy

### Authoritative Confirmation (from the repository itself)
**File:** `00_SEOJEONG_UNIVERSITY_RECOVERY_EXECUTIVE_MANUAL.md`, lines 21-24:
> *"고인이 운전한 모닝 차량은 대인배상 I, 대물배상(2천만원)만 가입되어 있으며, '자기신체사고 / 자동차상해' 담보는 [미가입] 상태임."*
> *"결론: 운전자 본인의 사망에 대한 자동차보험사 직접 1차 청구는 법적으로 불가능함."*

**File:** `AI_CASE_REVIEW_AND_EXECUTION_GUIDE.md`, line 109:
> *"strategic_role: Authentic Certificate serves as legal vehicle compliance evidence; first-party auto death payout unavailable due to 미가입 status."*

### AI Agent Directive
```
STATUS: DB INSURANCE CLAIM = DEAD PATH. DO NOT PURSUE.
ACTION: Use DB certificate ONLY as supporting exhibit proving lawful vehicle registration.
REDIRECT: All effort → Seojeong University Group Accident Insurance.
```

---

## 4. CRITICAL ISSUE #2: INTERNAL REPOSITORY CONTRADICTIONS

The repository contains **self-contradicting** information between files. This creates a risk that an AI agent or lawyer reads the wrong file and pursues a dead path.

### Contradiction Map

| Topic | WRONG (Older Files) | CORRECT (Updated Files) |
|:---|:---|:---|
| DB Insurance claim amount | `CASE_MASTER_KNOWLEDGE_DOSSIER.md` §1.3: "Recover KRW 100,000,000 in Self-Physical Accident death benefits" | `00_SEOJEONG_UNIVERSITY_RECOVERY_EXECUTIVE_MANUAL.md`: "운전자 본인의 사망에 대한 자동차보험사 직접 1차 청구는 법적으로 불가능함" |
| DB Insurance 50% provisional | `CASE_MASTER_KNOWLEDGE_DOSSIER.md` §1.3: "Demand mandatory release of KRW 50,000,000 provisional payment" | `README.md`: "Strategic Focus: DB Auto certificate serves as legal vehicle compliance proof; 100% payout vector is Seojeong Univ." |
| Coverage basis for DB claim | `CASE_MASTER_KNOWLEDGE_DOSSIER.md` §5.1: "First-party accidental death benefit under Self-Physical Accident (자손)" | `AI_CASE_REVIEW_AND_EXECUTION_GUIDE.md`: "first-party auto death payout unavailable due to 미가입 status" |
| Primary recovery target | `CASE_MASTER_KNOWLEDGE_DOSSIER.md`: DB Insurance = primary | `README.md` & `00_SEOJEONG_RECOVERY_EXECUTIVE_MANUAL.md`: Seojeong University = sole viable path |
| Total recovery amount | Dossier: KRW 135M-170M (including DB 100M) | Reality: KRW 35M-70M (Seojeong only) |

### Files That Need Correction
1. `CASE_MASTER_KNOWLEDGE_DOSSIER.md` — §1.3 items 1-2, §5.1, §5.2 recovery table
2. `legal_claim_package/01_db_insurance_claim_notice_and_legal_brief.md` — Entire file premises a non-existent coverage
3. `legal_claim_package/09_direct_international_claim_and_10day_statutory_notice.md` — Part I & Part III (DB Insurance sections)
4. `legal_claim_package/13_db_insurance_policy_verification_and_issuance_request.md` — Moot
5. `legal_claim_package/14_db_insurance_telephone_call_script_for_policy_certificate.md` — Only useful for obtaining certificate copy

### Files That Are CORRECT and Should Be Followed
1. `00_SEOJEONG_UNIVERSITY_GROUP_INSURANCE_RECOVERY_PACK/00_SEOJEONG_UNIVERSITY_RECOVERY_EXECUTIVE_MANUAL.md` ✅
2. `00_SEOJEONG_UNIVERSITY_GROUP_INSURANCE_RECOVERY_PACK/01_Seojeong_University_Group_Insurance_Claim_and_Legal_Brief.md` ✅
3. `README.md` (Strategic Focus section) ✅
4. `AI_CASE_REVIEW_AND_EXECUTION_GUIDE.md` (Chain 5 & 6) ✅

---

## 5. CRITICAL ISSUE #3: DATE DISCREPANCY IN CONSULAR CERTIFICATE

| Document | Date of Death Stated |
|:---|:---|
| GangNeung Asan Hospital Death Certificate (제2026031447741948호) | **March 14, 2026** |
| GangNeung Asan Hospital Post-Mortem Certificate (제2026031447738965호) | **March 14, 2026** |
| Sokcho Police Station Case No. 2026-00020 | **March 14, 2026, 05:58 AM** |
| **Embassy of Bangladesh Consular Mortuary Certificate (BDS/13/05-138)** | **March 13, 2026** ← WRONG |

**Resolution:** Consular certificate contains a typographical error. Official death date is **March 14, 2026**. File rectification petition to Embassy; insert footnote in all filings.

---

## 6. CRITICAL ISSUE #4: REFERENCE NUMBER INCONSISTENCY

- **Wrong:** `BDS/LS/05-138` (used in Evidence Inventory Exhibit B-5)
- **Correct:** `BDS/13/05-138` (used in official embassy records)
- **Action:** Find-and-replace all `BDS/LS/05-138` → `BDS/13/05-138`

---

## 7. CRITICAL ISSUE #5: IDENTITY NAME ORDER MISMATCH

| Document | Name Format |
|:---|:---|
| Bangladesh Passport (A03097931) | `MONOAR HOSSAIN MAHADI` (surname-first) |
| Korean ARC (010530-7660021) | `MAHADI MONOAR HOSSAIN` (given-name-first) |

**Action:** Insert Same-Person Affirmation (동일인 확인 진술) in all filings.

---

## 8. CRITICAL ISSUE #6: BANK WIRE REFERENCE ERROR

**Wrong:** `09_direct_international_claim.md` TOC references "Islami Bank & Sonali Bank"  
**Correct:** All authenticated documents specify **Mutual Trust Bank PLC** (SWIFT: `MTBLBDDH`, A/C: `1311004072276`)  
**Action:** Purge all Islami/Sonali Bank references.

---

## 9. CRITICAL ISSUE #7: MISSING DOCUMENTS NOT IN REPOSITORY

| # | Document | Status | How to Obtain |
|:---:|:---|:---|:---|
| 1 | Traffic Accident Fact Confirmation (교통사고사실확인원) | No PDF in repo | Request from Sokcho Police (Case 2026-00020) |
| 2 | On-Scene Field Investigation Report (현장실황조사서) | No PDF in repo | Request from Sokcho Police |
| 3 | **Seojeong University Master Group Policy Schedule** | **CRITICAL — NOT OBTAINED** | Call OIA: 031-860-5177 |
| 4 | Legal Heir Certificate (Warishan) | Status unclear | Cumilla Union Parishad, Bangladesh |
| 5 | Family Relationship Certificate (FRC) | Status unclear | BD Birth Registration authority |
| 6 | Certified Korean Translation (번역확인서) | Placeholder only | Licensed 공인외국어번역행정사 in Seoul |

---

## 10. CRITICAL ISSUE #8: DOSSIER STILL CLAIMS KRW 100M FROM DB INSURANCE

`CASE_MASTER_KNOWLEDGE_DOSSIER.md` — the "Single Source of Truth" — contains these materially incorrect statements:
- §1.3 Item 1: Claims KRW 100M from 자기신체사고 — **WRONG (미가입)**
- §1.3 Item 2: Claims KRW 50M provisional advance — **WRONG (no coverage)**
- §5.1: Entire section based on non-existent coverage
- Total at line 276: KRW 135M-160M — **Should be KRW 35M-70M**

---

## 11. SOLE VIABLE RECOVERY PATH: SEOJEONG UNIVERSITY GROUP INSURANCE

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│  SEOJEONG UNIVERSITY GROUP ACCIDENT INSURANCE — LEGAL ANALYSIS                       │
├──────────────────────────────────────────────────────────────────────────────────────┤
│  TYPE: Personal Accident Insurance (인보험 / 상해보험) — NOT vehicle insurance         │
│  SCOPE: Covers the student's body 24/365 — regardless of activity                    │
│  MANDATE: 100% mandatory under MOE IEQAS & MOJ immigration rules                    │
│  UNLICENSED DRIVING DEFENSE: VOID (KCC §732-2 + Supreme Court 98Da48963)             │
│  CUMULATIVE RECOVERY: KCC Art. 739 — NOT offset by any other insurance               │
│  INHERENT PROPERTY: Supreme Court 2003Da29463 — heirs' own property                  │
│                                                                                      │
│  RECOVERY TARGET:                                                                    │
│    Accidental Death Benefit:     KRW 30,000,000 ~ 50,000,000                         │
│    Repatriation Actual Expenses: KRW  5,000,000 ~ 20,000,000                         │
│    TOTAL:                        KRW 35,000,000 ~ 70,000,000                         │
│                                                                                      │
│  POTENTIAL UNDERWRITERS: DB손보, KB손보, 현대해상, 메리츠화재                          │
│  (Unknown until Seojeong discloses master policy schedule)                            │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 12. STEP-BY-STEP EXECUTION PLAYBOOK (AI AGENT DIRECTIVE)

### PHASE 1: INFORMATION GATHERING (Days 1-3)
1. **Call Seojeong OIA** (031-860-5177) — confirm underwriter, policy number, death benefit amount, repatriation rider
2. Use script: `03_Seojeong_OIA_Telephone_Call_Script_and_ARS_Protocol.md`

### PHASE 2: FORMAL CLAIM FILING (Days 2-5)
1. **Email claim** to `interchange@seojeong.ac.kr` and `global@seojeong.ac.kr`
2. **Send registered mail** to 경기도 양주시 은현면 화합로 1048-56, 서정대학교 국제교류처장 앞 (11429)
3. **Demand within 7 days:** policy disclosure, university stamp on claim form, forwarding to insurer

### PHASE 3: PRESSURE ESCALATION (Days 7-14, if unresponsive)
1. **국민신문고 (e-People)** petition to MOE — forces response within 7-14 days
2. **FSS Dispute Mediation** petition — freezes prescription, triggers regulatory investigation
3. **KLAC Legal Aid** application — free attorney (parents qualify at 4.68% of income ceiling)

### PHASE 4: INSURER DEFENSE REBUTTAL (Weeks 2-4)
1. Unlicensed driving defense → VOID under §732-2 + 98Da48963
2. Offset argument → VOID under §739 (cumulative recovery)
3. Foreign heirship challenge → PIL Art. 49 + Sunni Hanafi law documents

### PHASE 5: PAYMENT & DISTRIBUTION
1. SWIFT wire to Mutual Trust Bank PLC (MTBLBDDH, A/C: 1311004072276)
2. 0% Korean withholding tax
3. Father BELAL HOSSAIN: 2/3 | Mother MONOARA BEGUM: 1/3

---

## 13. LEGAL WEAPONS ARSENAL — STATUTES & PRECEDENTS

### Statutes
| Statute | Article | Application |
|:---|:---|:---|
| Korean Commercial Code | Art. 732-2 | Gross negligence does NOT exempt insurer in death insurance |
| Korean Commercial Code | Art. 663 | Clauses violating §732-2 are void |
| Korean Commercial Code | Art. 739 | Protections apply to accident insurance; cumulative recovery |
| Korean PIL Act | Art. 49 | Succession governed by deceased's national law (Bangladesh) |
| Legal Aid Act | Art. 22 | Free legal aid for indigent foreigners |

### Binding Precedents
| Case | Holding |
|:---|:---|
| **98Da48963 (En Banc)** | Unlicensed driving exclusion clauses are **absolutely void** for death insurance |
| 97Da27039 | "Intentional act" requires subjective suicide intent; cannot infer from unlicensed driving |
| 2003Da29463 | Death insurance proceeds are heirs' **inherent property**, not estate |

---

## 14. COMPLETE DISCREPANCY MATRIX

| # | Issue | Severity | Wrong | Correct | Action |
|:---:|:---|:---:|:---|:---|:---|
| D-1 | Death date in consular cert | 🔴 | March 13 (BDS/13/05-138) | March 14 (Hospital/Police) | File rectification + footnote |
| D-2 | Reference number | 🟡 | BDS/LS/05-138 | BDS/13/05-138 | Find-and-replace |
| D-3 | Name order | 🟡 | MONOAR HOSSAIN MAHADI | MAHADI MONOAR HOSSAIN | Same-person affirmation |
| D-4 | DB 100M claim | 🔴 | Claims 자기신체사고 payout | 자기신체사고 = 미가입 | Remove all DB claims |
| D-5 | Amount range | 🟢 | KRW 35M-60M | KRW 35M-70M | Use 35M-70M |
| D-6 | Total recovery | 🔴 | KRW 135M-170M | KRW 35M-70M | Correct total |
| D-7 | Wire bank | 🔴 | Islami/Sonali Bank | Mutual Trust Bank PLC | Purge wrong references |
| D-8 | DB coverage type | 🔴 | Self-Physical Accident | 미가입; 대인배상 I doesn't cover driver | Correct dossier |

---

## 15. AI AGENT VERIFICATION CHECKLIST

- [ ] DB Insurance path is CLOSED (자기신체사고 미가입)
- [ ] Sole path = Seojeong University Group Insurance (KRW 35M-70M)
- [ ] Unlicensed driving defense is void (§732-2 + 98Da48963)
- [ ] Death date = March 14, 2026 (NOT March 13)
- [ ] Reference = BDS/13/05-138 (NOT BDS/LS/05-138)
- [ ] Wire bank = Mutual Trust Bank PLC MTBLBDDH (NOT Islami/Sonali)
- [ ] Heirship: Father 2/3, Mother 1/3 (Sunni Hanafi Law)
- [ ] Seojeong master group policy schedule obtained
- [ ] Legal Heir Certificate obtained from Bangladesh
- [ ] Certified Korean Translation obtained
- [ ] Formal claim filed to Seojeong OIA (email + registered post)
- [ ] 국민신문고 petition filed (if university unresponsive after 7 days)
- [ ] KLAC legal aid application filed

---

*This audit report supersedes all conflicting information in the repository. AI agents should treat this document as the authoritative directive for case execution.*

*Generated by Antigravity AI Forensic Auditor — September 17, 2026*
