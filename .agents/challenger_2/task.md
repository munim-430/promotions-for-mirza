# Challenger Task: Artifact Integrity, Parity & Boundary Stress Testing

## Objective
Adversarially challenge and stress-test artifact integrity, trio-format (MD, DOCX, PDF) parity, zero-stale references, and boundary constraints.

## Scope of Stress Testing
1. Read `d:/promotion/.agents/ORIGINAL_REQUEST.md` (specifically header `## 2026-09-06T09:53:43Z`).
2. Write and execute stress testing scripts verifying:
   - All 15 Markdown deliverables exist and are > 10KB.
   - All 16 DOCX files exist, have valid XML structure, and contain 0 corruption errors.
   - All 16 PDF files exist, total > 200 pages, and contain 0 empty pages.
   - Full trio-format text parity for core entities (`MAHADI MONOAR HOSSAIN`, `28모1390`, `DB Insurance`, `2026-DB-AUTO-28M1390`, `2026-01-21`).
   - Zero dangling exhibit references across Groups A-I (all match catalog entries in File 05).
   - Zero stale Samsung Fire references across all deliverables, with `Kia Morning` / `기아 모닝` strictly preserved.
   - Email payload budgets strictly comply with 15MB/25MB limits.
   - Run `python tests/run_all_tests.py`.
3. Document test outputs in `d:/promotion/.agents/challenger_2/report.md` and handoff report in `d:/promotion/.agents/challenger_2/handoff.md` with explicit verdict: `APPROVE` or `REQUEST_CHANGES`.
