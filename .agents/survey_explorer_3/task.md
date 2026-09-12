# Survey Task: Test Suite, Compilation Pipeline & Transmittals Scope

## Objective
Map the test suite in `d:/promotion/tests/`, the compilation script `d:/promotion/assemble_dossier.py`, transmittals in `d:/promotion/legal_claim_package/12_lawyer_and_insurer_filing_email_transmittals.md`, and packaging workflows.

## Scope & Instructions
1. Read `d:/promotion/.agents/ORIGINAL_REQUEST.md` (specifically header `## 2026-09-06T09:53:43Z`).
2. Examine `d:/promotion/assemble_dossier.py` and understand how markdown files are compiled to docx/pdf, how TOC/metadata/manifests are built, and what external dependencies (e.g. pandoc, python-docx, reportlab, etc.) are used.
3. Examine all test files in `d:/promotion/tests/`:
   - Identify existing test assertions checking Samsung Fire, policy renewal date (March 13, 2026), corporate addresses, calculation engines, and exhibit cross-references.
   - Map out what test updates and new tests are needed for DB Insurance (DB손해보험주식회사, Headquarters: DB Financial Center, 432 Teheran-ro, Gangnam-gu, Seoul, Call Center 1588-0100), renewal date January 21, 2026, and grep audits for residual stale Samsung Fire references.
4. Inventory `12_lawyer_and_insurer_filing_email_transmittals.md`, DHL manifests, and related dispatch files.
5. Write your detailed survey findings report to:
   `d:/promotion/.agents/survey_explorer_3/report.md` and your `handoff.md`.
