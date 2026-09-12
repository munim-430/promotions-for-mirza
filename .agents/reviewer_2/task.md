# Review Task: Logistics, Compilation Suite, Trio-Format Parity & Zero-Stale Audit

## Objective
Independently review the compilation suite, trio-format (MD, DOCX, PDF) parity across all 15 deliverables, email transmittals, DHL manifests, print packs, and run zero-stale grep audits.

## Scope of Review
1. Read `d:/promotion/.agents/ORIGINAL_REQUEST.md` (specifically header `## 2026-09-06T09:53:43Z`).
2. Examine Deliverables 06 to 12, Print Packs, and `CASE_MASTER_KNOWLEDGE_DOSSIER.md`:
   - Content-Certified Mail cover letters, envelope addressing to DB Insurance HQ.
   - DHL courier logistics, commercial invoice, waybill declarations to DB Insurance HQ.
   - Email transmittals (`12_lawyer_and_insurer_filing_email_transmittals.md`), particularly Transmittal 4 to DB Insurance Claims Center (`claim@idbins.com`, `claim_auto@idbins.com`).
   - Bengali Print Pack README guides.
3. Verify compilation suite and trio-format parity:
   - Verify `python assemble_dossier.py` regenerates `CASE_MASTER_KNOWLEDGE_DOSSIER.md`, all DOCX files, and all PDF files cleanly.
   - Verify page counts, non-empty pages, and text parity across MD, DOCX, and PDF.
4. Execute audit checks:
   - Perform grep audit for residual stale Samsung Fire mentions (excluding vehicle make `Kia Morning` / `기아 모닝`).
   - Run `python tests/run_all_tests.py` and verify all tests pass.
5. Write your comprehensive review report to `d:/promotion/.agents/reviewer_2/report.md` and your handoff report to `d:/promotion/.agents/reviewer_2/handoff.md` with explicit verdict: `APPROVE` or `REQUEST_CHANGES`.
