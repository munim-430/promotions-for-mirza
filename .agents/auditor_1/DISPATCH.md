# Dispatch Assignment: Forensic Integrity Auditor

## Working Directory
d:/promotion/.agents/auditor_1

## Objective
Perform an independent, exhaustive forensic integrity audit across all generated deliverables in `d:/promotion/legal_claim_package/`:
1. `00_master_dossier_index_and_executive_summary.md`
2. `01_samsung_fire_claim_notice_and_legal_brief.md`
3. `02_fss_dispute_mediation_petition.md`
4. `03_seojeong_university_group_insurance_claim.md`
5. `04_bilingual_special_power_of_attorney.md`
6. `04_cross_border_heirship_and_legalization_guide.md`
7. `05_evidence_inventory_and_exhibits_catalog.md`

## Audit Criteria
1. **Authenticity & Substantive Logic**: Verify that all legal arguments, statutory citations (Commercial Code Arts. 732-2, 739, 663; PIL Art. 49), and Supreme Court case holdings (98Da48963, 97Da27039, 98Da26910) are authentic, rigorous, and accurately interpreted.
2. **Zero Dummy/Facade Check**: Confirm that no dummy placeholders, truncated stubs, or fake citations exist.
3. **Factual Accuracy**: Confirm exact match of policyholder (`MAHADI MONOAR HOSSAIN`, `010530-7660021`), vehicle `28모1390`, renewal date March 13, 2026, agent reference (`심기철`, `010-8969-0440`), parents (`BELAL HOSSAIN`, `MONOARA BEGUM`), share ratios (2/3 & 1/3), and banking/SWIFT coordinates.
4. **Mandatory Binary Verdict**:
   - If ANY cheating, dummy code, or fabricated facts are found -> report `INTEGRITY VIOLATION`.
   - If all implementations are genuine, authentic, and litigation-grade -> report `CLEAN`.

## Output
Write your full forensic audit report to `d:/promotion/.agents/auditor_1/audit_report.md` and `d:/promotion/.agents/auditor_1/handoff.md`. Send a completion message back to the orchestrator.

## 2026-08-23T05:33:35Z
Dispatch received from parent (3af4573e-bcc2-4c8b-a875-df9dd0b7b603) requesting forensic integrity audit of all 7 deliverables in `d:/promotion/legal_claim_package/`.

## 2026-09-06T10:39:25Z
You are Forensic Integrity Auditor. Your working directory is d:/promotion/.agents/auditor_1.
You MUST read d:/promotion/.agents/ORIGINAL_REQUEST.md (specifically header '## 2026-09-06T09:53:43Z') and d:/promotion/.agents/auditor_1/task.md before starting work.

Objective:
Conduct an independent forensic integrity audit across legal_claim_package/, CASE_MASTER_KNOWLEDGE_DOSSIER.md, assemble_dossier.py, and tests/.
Check for:
1. Genuine implementations vs hardcoded test facades / stubs.
2. Authentic DB Insurance metadata (CEO Jeong Jong-pyo, 432 Teheran-ro, 1588-0100, 2026-DB-AUTO-28M1390, 2026-01-21).
3. Strict preservation of vehicle make: 28모1390 (Kia Morning / 기아 모닝 경승용).
4. Genuine legal analysis of KCC §732-2, §739, §663, and Supreme Court 98Da48963 En Banc tailored to DB Promy Car terms.
5. Deliverable 13 portal verification analysis and authentic Korean request letter under FCPA Art. 28 and KCC Arts. 638, 640.
6. Execution of tests and test validity.

Output binary verdict: CLEAN or INTEGRITY VIOLATION.
Write your report to d:/promotion/.agents/auditor_1/report.md and your handoff to d:/promotion/.agents/auditor_1/handoff.md.
Then send a message back with your verdict and summary.

