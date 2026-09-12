# Project: Direct-Filing Dispatch Package & Legal Aid Escalation Protocol

## Architecture
This project produces an execution-ready, litigation-grade direct-filing dispatch package, contingency legal aid escalation roster, and step-by-step attorney-in-fact operational checklist for the foreign heirs of deceased student MAHADI MONOAR HOSSAIN in `d:/promotion/legal_claim_package/`.

### Core Data & Case Identifiers
- **Deceased Insured**: MAHADI MONOAR HOSSAIN (마하디 모노아르 호세인)
  - Alien Registration No.: 010530-7660021
  - Passport No.: A03097931
  - Nationality: Bangladesh
  - Student Status: Enrolled D-2 Foreign Student, Seojeong University (서정대학교, Student ID: 202581042)
- **Accident**: Single-vehicle collision with guardrail on March 14, 2026 at 05:58 AM KST, National Road 7, Hyeonnam-myeon, Yangyang-gun, Gangwon State. Gangwon Sokcho Police Station Traffic Accident Case No. `2026-00020`. Post-Mortem Certificate No. `2026031447738965` (GangNeung Asan Hospital).
- **Subject Vehicle & Policy**: Vehicle No. `28모1390` (Hyundai Sonata), Anycar Individual Auto Policy `2026-SF-AUTO-28M1390`, validly renewed March 13, 2026 24:00 KST through March 13, 2027 24:00 KST. Managing Certified Agent: Shim Ki-cheol (심기철, 010-8969-0440).
- **Sole Legal Heirs**:
  - Father: BELAL HOSSAIN (NID: 19741913345000128) — 2/3 share (66.667%)
  - Mother: MONOARA BEGUM (NID: 19801913345000129) — 1/3 share (33.333%)
  - Domicile: Village: Chandpur, P.O.: Chandpur, Thana: Debidwar, District: Cumilla, Bangladesh.
- **Designated Attorney-in-Fact**: Md Monirul Islam, Chairman of the Korea Bangladesh Human Rights Committee (수임인 겸 대리인).
- **Direct Wire Remittance Coordinates**:
  - Father (Belal Hossain): Islami Bank Bangladesh PLC, Debidwar Branch, Account No. 20501230100456789, SWIFT: `IBBLBDDHXXX`
  - Mother (Monoara Begum): Sonali Bank PLC, Debidwar Branch, Account No. 20501230100789012, SWIFT: `BSONBDDHXXX`

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| F1 | Samsung Fire Content-Certified Mail Notice | Canonical Korean 내용증명 cover letter to Samsung Fire HQ CEO Lee Mun-hwa & Agent Shim Ki-cheol demanding KRW 100M + KRW 50M provisional payment | M1 | ORIGINAL_REQUEST R1 |
| F2 | Seojeong University Content-Certified Mail Notice | Canonical Korean 내용증명 cover letter to Seojeong Univ President Yang Young-hee & Dean of International Affairs for D-2 Group Insurance & Repatriation benefits | M1 | ORIGINAL_REQUEST R1 |
| F3 | Recipient Routing Tables | Full physical addresses, zip codes, direct phone, fax, emails for Samsung Fire HQ, Agent Shim, and Seojeong Univ OIA | M1 | ORIGINAL_REQUEST R1 |
| F4 | Bilingual Email Submission Templates | Production-ready Korean/English email templates with attachment schedules and SWIFT wire coordinates for electronic filing | M1 | ORIGINAL_REQUEST R1 |
| F5 | Korea Post Postal Guidelines | Detailed operational rules for 3-copy offline Content-Certified Mail (등본 날인/간인) and 24/7 Internet e-Post (전자내용증명) | M1 | spec_miner_r1 |
| F6 | KLAC Foreigner Legal Aid Scheme Guide | Income/resident criteria (125% median income), required Bangladeshi/Korean documents, and procedural roadmap | M2 | ORIGINAL_REQUEST R2 |
| F7 | KLAC Branch Routing Network | Complete routing matrix for 4 Gangwon branches and 5 Seoul branches (addresses, phone, jurisdiction) | M2 | ORIGINAL_REQUEST R2 |
| F8 | Bangladesh Embassy Diplomatic Representation | Formal English/Korean diplomatic petition to Labour & Consular Wing requesting Note Verbale, Legal Heirship verification, and panel attorney referral | M2 | ORIGINAL_REQUEST R2 |
| F9 | Bar Association & Pro Bono Intake Roster | Contact details, intake channels, and submission guidelines for Seoul Bar Foreigner Human Rights Sub-committee & Gong-Gam Foundation | M2 | ORIGINAL_REQUEST R2 |
| F10 | Contingency Escalation Matrix | Explicit trigger thresholds and decision trees (Direct Filing -> Day 10 Provisional -> FSS Dispute Mediation -> KLAC/Pro Bono Litigation) | M2 | ORIGINAL_REQUEST R2 |
| F11 | Special POA Legalization Roadmap | Step-by-step instructions for Dhaka Notary -> Law Ministry -> MOFA Dhaka -> Korean Embassy Dhaka (Track B) / Apostille (Track A) -> Korean Certified Translation | M3 | ORIGINAL_REQUEST R3 |
| F12 | Korea Post Counter Dispatch Protocol | Step-by-step execution protocol for Attorney-in-Fact at post office window (document inspection, inter-page seals, delivery confirmation, receipt management) | M3 | ORIGINAL_REQUEST R3 |
| F13 | Statutory 10-Day Provisional Payment Tracker | Chronological tracking ledger, default interest calculator (6% p.a. commercial -> 12% p.a. litigation), and enforcement workflow under Commercial Code Art. 732-2 | M3 | ORIGINAL_REQUEST R3 |
| F14 | Master Dossier Index & Exhibits Synchronization | Integration of Files 06, 07, 08 and new dispatch evidence into `00_master_dossier_index_and_executive_summary.md` and `05_evidence_inventory_and_exhibits_catalog.md` | M4 | System Harmony |

## Milestones
| # | Name | Target File | Scope & Key Deliverables | Dependencies | Status |
|---|------|-------------|--------------------------|--------------|--------|
| M1 | Direct Postal & Electronic Filing Dispatch Package | `06_direct_filing_dispatch_package.md` | Samsung Fire HQ & Agent Shim 내용증명, Seojeong Univ 내용증명, Recipient Routing Tables, Bilingual Email Templates, Korea Post Guidelines | Survey Reports | PLANNED |
| M2 | Legal Aid (KLAC) & Consular Escalation Contingency Roster | `07_legal_aid_and_consular_escalation_roster.md` | KLAC Foreigner Scheme rules, Gangwon/Seoul KLAC branch network, BD Embassy Diplomatic Petition, Seoul Bar/Gong-Gam intake roster, Escalation Trigger Matrix | Survey Reports | PLANNED |
| M3 | Step-by-Step Attorney-in-Fact Execution Checklist | `08_attorney_in_fact_execution_checklist.md` | Special POA Legalization Guide (Dhaka to Seoul), Post Office Counter Dispatch Protocol, 10-Day Provisional Payment Tracking & Default Interest Ledger | M1, M2 | PLANNED |
| M4 | Master Dossier & Exhibits Catalog Synchronization | `00_master_dossier_...md`, `05_evidence_...md` | Update Master Index, executive summaries, cross-reference matrices, and exhibit catalog to fully incorporate Files 06, 07, 08 | M1, M2, M3 | PLANNED |

## Code & Artifact Layout
```
d:/promotion/legal_claim_package/
├── 00_master_dossier_index_and_executive_summary.md (Updated in M4)
├── 01_samsung_fire_claim_notice_and_legal_brief.md (Existing)
├── 02_fss_dispute_mediation_petition.md (Existing)
├── 03_seojeong_university_group_insurance_claim.md (Existing)
├── 04_bilingual_special_power_of_attorney.md (Existing)
├── 04_cross_border_heirship_and_legalization_guide.md (Existing)
├── 05_evidence_inventory_and_exhibits_catalog.md (Updated in M4)
├── 06_direct_filing_dispatch_package.md (Authored in M1)
├── 07_legal_aid_and_consular_escalation_roster.md (Authored in M2)
└── 08_attorney_in_fact_execution_checklist.md (Authored in M3)
```

## Interface Contracts
- **File 06 (Dispatch Package)** references all exhibit codes from File 05 (Exhibits A-1 to F-4) and cross-references Claim Brief File 01 and Group Claim File 03.
- **File 07 (Legal Aid Roster)** integrates Special POA File 04, FSS Petition File 02, and Heirship Guide File 04-Guide into KLAC/Embassy/Bar submissions.
- **File 08 (Execution Checklist)** binds Files 01 through 07 into an operational, chronological execution sequence for the attorney-in-fact.
- **Files 00 & 05** provide master indexation and cataloging for the entire 9-file suite.
