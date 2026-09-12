# Auditor Task: Forensic Integrity & Anti-Deception Audit

## Objective
Conduct an independent, objective forensic audit of the entire codebase, deliverables, and test suite to detect any cheating, hardcoded test facades, stubs, dummy implementations, or integrity violations.

## Scope of Forensic Audit
1. Read `d:/promotion/.agents/ORIGINAL_REQUEST.md` (specifically header `## 2026-09-06T09:53:43Z`).
2. Examine `legal_claim_package/`, `CASE_MASTER_KNOWLEDGE_DOSSIER.md`, `assemble_dossier.py`, and `tests/`:
   - Verify that all legal arguments, factual timelines, and statutory analyses are genuine and authentically authored (not dummy placeholders).
   - Verify that test assertions are genuine and execute real file reading, XML parsing, PyMuPDF page checks, and regex evaluations (no test bypassing, no hardcoded return True).
   - Verify that Deliverable 13 genuinely analyzes DB Insurance portal endpoints (`directdb.co.kr`, `idbins.com`), post-mortem 2FA failure modes, and drafts an authentic Korean legal request letter under FCPA Art. 28 and Commercial Code Arts. 638, 640.
   - Verify that Commercial Code §732-2, §739, §663, and Supreme Court 98Da48963 En Banc are genuinely applied to DB Promy Car terms.
   - Verify zero residual stale Samsung Fire mentions in target insurer fields, and strict preservation of Kia Morning vehicle make.
3. Binary Veto:
   - If any cheating, hardcoded facades, fabricated authorities, or integrity violations are found: verdict is `INTEGRITY VIOLATION`.
   - If work product implements functionality authentically and cleanly: verdict is `CLEAN`.
4. Write your comprehensive forensic audit report to `d:/promotion/.agents/auditor_1/report.md` and handoff report to `d:/promotion/.agents/auditor_1/handoff.md`.
