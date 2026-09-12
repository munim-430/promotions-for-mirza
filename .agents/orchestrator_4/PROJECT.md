# Project: Legal Analysis & Cross-Border Litigation Document Preparation Dossier (DB Insurance Transition)

## Architecture
- **Objective**: Execute an end-to-end refactoring of the entire cross-border legal recovery dossier, FSS dispute mediation petition, and multi-agency filing packages to target DB Insurance Co., Ltd. (DB손해보험주식회사) as the sole auto insurer of record for vehicle 28모1390 (renewed on January 21, 2026), and document the DB Insurance web portal policy verification pathways and official issuance request letter.
- **Corporate Profile**: DB손해보험주식회사 (DB Insurance Co., Ltd.), CEO Jeong Jong-pyo, DB Financial Center, 432 Teheran-ro, Gangnam-gu, Seoul 06194, Call Center: 1588-0100 (Direct: 1600-0100, Foreigner: 1566-0161), Claims Fax: 0505-181-4862.
- **Policy Identifier**: `2026-DB-AUTO-28M1390`, Product: DB손해보험 프로미카 개인용 자동차보험 (종합보험).
- **Vehicle Profile**: 28모1390 (Kia Morning / 기아 모닝 경승용) — make/model strictly preserved.
- **Output Directory**: `d:/promotion/legal_claim_package/`
- **Integrity Level**: Litigation-grade, fully compliant with Korean Commercial Code §732-2, §739, §663, Supreme Court En Banc Decision 98Da48963, and Financial Consumer Protection Act Art. 28.

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | DB Portal Verification Pathways & Analysis | Investigation of directdb.co.kr / idbins.com endpoints (FWMYCV0371, FWMYCV0383, FWMYCV0366, FWMYCV0216) and authentication barrier analysis for deceased foreign national | M1 | ORIGINAL_REQUEST §R1 |
| 2 | Official Policy Confirmation & Premium Receipt Request Letter | Korean formal request letter (보험가입증명서 및 보험료납입영수증 발급요청서) under FCPA Art. 28 & Commercial Code Arts. 638, 640 | M1 | ORIGINAL_REQUEST §R1 |
| 3 | Core Dossier Retargeting to DB Insurance | Refactor CASE_MASTER_KNOWLEDGE_DOSSIER.md and Files 00-05 in legal_claim_package/ targeting DB Insurance HQ, CEO Jeong Jong-pyo, renewal date 2026-01-21 | M2 | ORIGINAL_REQUEST §R2 |
| 4 | Statutory Defenses & Standard Terms Tailoring | Preserve KCC §732-2, §663, and Supreme Court 98Da48963, tailored to DB Insurance auto policy terms (자기신체사고 및 자동차상해) and single-vehicle accident rules | M2 | ORIGINAL_REQUEST §R2 |
| 5 | Filing Package Retargeting to DB Insurance | Refactor Files 06-10 (Content-Certified Mail, KLAC, Checklist, Direct International Claim, Pro Bono Packets) for DB Insurance | M2 | ORIGINAL_REQUEST §R2 |
| 6 | Transmittal Emails & Dispatch Guides Update | Refactor File 11 (DHL guide & AWB) and File 12 (Transmittal 4 & metadata) for DB Insurance | M3 | ORIGINAL_REQUEST §R3 |
| 7 | Compilation Suite Integration into assemble_dossier.py | Integrate DOCX and PDF generation via python-docx & Word COM into assemble_dossier.py, clean regeneration of all packages | M3 | ORIGINAL_REQUEST §R3 |
| 8 | Automated Test Suite Updates & Zero-Stale Grep Audit | Update tests/run_all_tests.py, test_adversarial_suite.py, deep dive, add test_08 zero-stale audit with negative lookbehind for Renault Samsung, 100% pass rate | M4 | ORIGINAL_REQUEST §R4 |

## Milestones
| # | Name | Scope | Dependencies | Status | Output Files |
|---|------|-------|-------------|--------|--------------|
| 1 | Milestone 1 (R1) | DB Insurance Web Portal & Policy Verification Investigation | Phase 0 Survey | IN_PROGRESS | `13_db_insurance_policy_verification_and_issuance_request.md` |
| 2 | Milestone 2 (R2) | Complete Dossier & Legal Packages Re-Targeting to DB Insurance | M1 | PLANNED | `CASE_MASTER_KNOWLEDGE_DOSSIER.md`, `00_`-`10_` in `legal_claim_package/` |
| 3 | Milestone 3 (R3) | Transmittal Emails, Dispatch Guides & Document Compilation Suite | M1, M2 | PLANNED | `11_`, `12_`, `assemble_dossier.py`, docx/pdf outputs, print packs |
| 4 | Milestone 4 (R4) | Test Suite & Integrity Validation | M1, M2, M3 | PLANNED | `tests/run_all_tests.py`, `tests/test_adversarial_suite.py`, test execution |

## Deliverables Layout (`d:/promotion/legal_claim_package/`)
- `00_master_dossier_index_and_executive_summary.md` (Master Index, Exec Summary, DB Insurance Targets)
- `01_samsung_fire_claim_notice_and_legal_brief.md` (Bilingual Claim Notice & Preemptive Legal Brief to DB Insurance)
- `02_fss_dispute_mediation_petition.md` (FSS Dispute Mediation Petition targeting DB Insurance)
- `03_seojeong_university_group_insurance_claim.md` (Seojeong University D-2 Group Claim Package & Checklist)
- `04_bilingual_special_power_of_attorney.md` (Bilingual Special POA with Direct SWIFT Mandate)
- `04_cross_border_heirship_and_legalization_guide.md` (PIL Art. 49 Heirship & Dual-Track Legalization Guide)
- `05_evidence_inventory_and_exhibits_catalog.md` (Master Evidence Inventory & Cross-Reference Matrix)
- `06_direct_filing_dispatch_package.md` (Content-Certified Mail Cover Letters to DB Insurance)
- `07_legal_aid_and_consular_escalation_roster.md` (KLAC Legal Aid Scheme & Consular Roster)
- `08_attorney_in_fact_execution_checklist.md` (Step-by-Step Counter Guide & 10-Day Statutory Calendar)
- `09_direct_international_claim_and_10day_statutory_notice.md` (Direct International Claim & 10-Day Notice to DB Insurance)
- `10_parallel_pro_bono_and_consular_intake_packets.md` (Parallel Pro Bono & Consular Intake Packets)
- `11_dhaka_to_seoul_dhl_dispatch_and_10day_tracking_guide.md` (Dhaka-to-Seoul DHL Courier & Tracking Guide)
- `12_lawyer_and_insurer_filing_email_transmittals.md` (Executive Legal & Institutional Email Transmittal Suite)
- `13_db_insurance_policy_verification_and_issuance_request.md` (DB Insurance Portal Pathways & Official Request Letter)
- `docx/` (Compiled Word document distribution for all 15 deliverables)
- `pdf/` (Print-ready PDF document distribution for all 15 deliverables)
