# Task: Master Dossier Compilation Pipeline & Test Suite Integrity Verification

## Objective
1. Refactor `assemble_dossier.py` to generate `CASE_MASTER_KNOWLEDGE_DOSSIER.md` with 100% authentic DB Insurance metadata and integrate the complete Markdown -> DOCX -> PDF compilation pipeline (incorporating all 15 deliverables: `00_` through `13_` plus friendly transmittal copies).
2. Run `python assemble_dossier.py` to regenerate all deliverables across Markdown, DOCX, and PDF with zero errors.
3. Update `tests/run_all_tests.py`, `tests/test_adversarial_suite.py`, and `tests/test_adversarial_deep_dive.py` to validate DB Insurance metadata, renewal date (2026-01-21), correct corporate addresses, statutory interest engines, and a zero-stale regex audit ensuring zero residual Samsung Fire insurer references (while strictly preserving `Kia Morning` / `기아 모닝`).
4. Update `d:/promotion/PROJECT.md` at root to reflect current DB Insurance architecture and deliverables.
5. Run the full automated test suite (`python tests/run_all_tests.py`) and ensure a 100% test pass rate.

## Mandatory Inputs & Reports to Read
1. `d:/promotion/.agents/ORIGINAL_REQUEST.md` (specifically header `## 2026-09-06T09:53:43Z`)
2. `d:/promotion/.agents/survey_explorer_3/report.md` (pipeline disconnect analysis, test mapping, and COM automation details)
3. `d:/promotion/.agents/worker_1/handoff.md` (details of files 00-05 and 13)
4. `d:/promotion/.agents/worker_2/handoff.md` (details of files 06-12)
5. `d:/promotion/.agents/worker_r3_4/compile_all_dossier.py` (reference DOCX/PDF styling and Word COM automation)

## Exclusive File Ownership
- `d:/promotion/assemble_dossier.py`
- `d:/promotion/CASE_MASTER_KNOWLEDGE_DOSSIER.md`
- `d:/promotion/tests/run_all_tests.py`
- `d:/promotion/tests/test_adversarial_suite.py`
- `d:/promotion/tests/test_adversarial_deep_dive.py`
- `d:/promotion/PROJECT.md`
- `d:/promotion/legal_claim_package/docx/*`
- `d:/promotion/legal_claim_package/pdf/*`
- `d:/promotion/03_KOREAN_LAWYERS_AND_INSURERS_FILING_PACK/*` (compiled PDFs)

## Key Technical Specifications
1. **`assemble_dossier.py`**:
   - Update header metadata: DB Insurance Co., Ltd. (DB손해보험주식회사), CEO Jeong Jong-pyo, DB Financial Center, 432 Teheran-ro, Gangnam-gu, Seoul 06194, Call Center 1588-0100, Policy No `2026-DB-AUTO-28M1390`, Renewal Date 2026-01-21 24:00 KST, active 52 days prior to accident.
   - Strictly preserve `28모1390 (Kia Morning / 기아 모닝 경승용)`.
   - Update Section 1, 2, 5, 6, 7, 8, 9, 11, 13 to reflect DB Insurance. Include Deliverable 13 in the inventory and table of contents.
   - Incorporate the `parse_markdown_to_docx` and `convert_all_docx_to_pdf` logic so running `python assemble_dossier.py` compiles all 14 MD files:
     - `00_master_dossier_index_and_executive_summary.md`
     - `01_samsung_fire_claim_notice_and_legal_brief.md`
     - `02_fss_dispute_mediation_petition.md`
     - `03_seojeong_university_group_insurance_claim.md`
     - `04_bilingual_special_power_of_attorney.md`
     - `04_cross_border_heirship_and_legalization_guide.md`
     - `05_evidence_inventory_and_exhibits_catalog.md`
     - `06_direct_filing_dispatch_package.md`
     - `07_legal_aid_and_consular_escalation_roster.md`
     - `08_attorney_in_fact_execution_checklist.md`
     - `09_direct_international_claim_and_10day_statutory_notice.md`
     - `10_parallel_pro_bono_and_consular_intake_packets.md`
     - `11_dhaka_to_seoul_dhl_dispatch_and_10day_tracking_guide.md`
     - `12_lawyer_and_insurer_filing_email_transmittals.md`
     - `13_db_insurance_policy_verification_and_issuance_request.md`
     Plus friendly transmittal copies (`Lawyer_and_Insurer_Filing_Emails.docx` and `.pdf`).
   - Copy/update the compiled PDF into `03_KOREAN_LAWYERS_AND_INSURERS_FILING_PACK/` where appropriate.
   - Run `python assemble_dossier.py` and verify all files compile cleanly.
2. **`tests/test_adversarial_suite.py`**:
   - Update `EXPECTED_MD_STEMS` to include all 14 deliverable stems (including `12_` and `13_`).
   - In `test_06_policy_number_and_agent_contact_integrity`, assert:
     - `"policy_number": r"2026-DB-AUTO-28M1390"`
     - `"managing_channel": r"DB손해보험|1588-0100|고객지원센터|다이렉트"`
     - `"renewal_date": r"2026년\s*1월\s*21일|2026-01-21|January\s*21,?\s*2026"`
     - `"insurer_name": r"DB손해보험|DB\s+Insurance"`
     - `"vehicle_number": r"28모\s*1390"`
     - `"deceased_name": r"MAHADI\s+MONOAR\s+HOSSAIN"`
     - `"deceased_arc": r"010530-7660021"`
     - `"swift_mtb": r"MTBLBDDH"`
   - Add `test_08_zero_stale_samsung_fire_references`:
     - Scan all MD, DOCX, and PDF files.
     - Ensure 0 occurrences of Samsung Fire as insurer (`삼성화재`, `Samsung Fire`, `2026-SF`, `심기철`, `8969-0440`, `1588-5114`, `samsungfire.com`, `서초대로74길`).
     - Allow `기아` and `Renault Samsung` ONLY for vehicle make.
   - Add `test_09_db_insurance_policy_and_metadata_validation`:
     - Assert presence of DB Financial Center (테헤란로 432 / Teheran-ro 432), CEO Jeong Jong-pyo (정종표), 1588-0100 across primary claim documents.
3. **`tests/test_adversarial_deep_dive.py`**:
   - Update `STEMS` to include `12_` and `13_`.
   - Ensure all exhibit references, banking coordinates, and financial arithmetic pass.
4. **Execution & Validation**:
   - Execute `python assemble_dossier.py`.
   - Execute `python tests/run_all_tests.py`.
   - Ensure 100% tests pass.

## Deliverables & Handoff
- Document all actions and test outputs in `d:/promotion/.agents/worker_3/handoff.md`.
- Send completion message to parent.
