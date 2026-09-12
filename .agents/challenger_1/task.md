# Challenger Task: Statutory, Financial & Mathematical Stress Testing

## Objective
Empirically stress-test the refactored legal package and dossier for statutory interest math, heirship inheritance shares, KLAC poverty thresholds, and insurance claim calculations.

## Scope of Stress Testing
1. Read `d:/promotion/.agents/ORIGINAL_REQUEST.md` (specifically header `## 2026-09-06T09:53:43Z`).
2. Write and execute stress testing scripts verifying:
   - Total claim (KRW 100,000,000) and 50% provisional advance (KRW 50,000,000).
   - Bangladeshi Sunni Hanafi succession shares under PIL Art. 49: Father (BELAL HOSSAIN) 2/3 (KRW 66,666,667), Mother (MONOARA BEGUM) 1/3 (KRW 33,333,333), summing to exactly 100%.
   - Provisional advance distribution: Father KRW 33,333,333, Mother KRW 16,666,667, summing to exactly KRW 50,000,000.
   - Statutory delay interest under Commercial Code §54 (6.0% p.a.) and Special Act on Litigation Expediting §3(1) (12.0% p.a.).
   - KLAC indigence threshold calculation: family income BDT 20,000 ≈ KRW 230,000/mo vs 2-person median ceiling (KRW 4,916,035/mo) = 4.68% (strictly < 125%).
   - Guarantee Act §29-2 deductible non-applicability to single-vehicle first-party death benefits.
   - Run `python tests/run_all_tests.py`.
3. Document test outputs in `d:/promotion/.agents/challenger_1/report.md` and handoff report in `d:/promotion/.agents/challenger_1/handoff.md` with explicit verdict: `APPROVE` or `REQUEST_CHANGES`.
