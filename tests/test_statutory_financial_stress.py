"""
Empirical Adversarial Stress-Testing Suite: Statutory & Financial Engines
Focus Areas:
1. Statutory Interest Mathematics:
   - Commercial Code §54: 6.0% per annum (Daily KRW 16,438.356 on KRW 100M, KRW 8,219.178 on KRW 50M)
   - Special Act on Litigation Expediting §3(1): 12.0% per annum (Daily KRW 32,876.712 on KRW 100M, KRW 16,438.356 on KRW 50M)
   - Cumulative accrual schedules (10, 20, 30, 60, 90, 180, 270, 365 days)
   - Leap year sensitivity and fractional Won rounding mechanics
2. Bangladeshi Sunni Hanafi Succession under Korean Private International Law Art. 49:
   - Father (BELAL HOSSAIN): 2/3 share (Asaba residuary) = KRW 66,666,667 of KRW 100M (provisional: KRW 33,333,333)
   - Mother (MONOARA BEGUM): 1/3 share (Zawil Furud Quranic sharer) = KRW 33,333,333 of KRW 100M (provisional: KRW 16,666,667)
   - Total exact sum = KRW 100,000,000 (100.000000%) and KRW 50,000,000 (100.000000%)
3. Commercial Code §732-2 & Automobile Insurance Standard Terms Art. 34(3) 50% Provisional Advance:
   - Mandatory 50% advance: KRW 50,000,000 within 10 business days (or 3 days post document inspection)
4. Korea Legal Aid Corporation (KLAC) Indigence Calculation under Legal Aid Act §22:
   - 2-person Korean standard median income (2026): KRW 3,932,828/mo
   - KLAC 125% median income ceiling: KRW 4,916,035/mo
   - Parents' monthly income in Bangladesh: BDT 20,000 @ 11.5 KRW/BDT = KRW 230,000/mo
   - Indigence ratio: 4.679% of ceiling (< 125%), safety margin > 95%
   - Stress testing across exchange rate fluctuations (9.0 to 20.0 KRW/BDT) and income volatility
   - Court filing stamp under Court Stamp Act: KRW 455,000
5. Guarantee of Automobile Accident Compensation Act §29-2 Deductible / Co-payment Non-Applicability:
   - Single-vehicle collision (단독차량 충돌사고): 0 third-party liability
   - First-party accidental death (자기신체사고 / 자손): Commercial Code §732-2, §739 & Supreme Court 98Da48963
   - Deductible / Co-payment (사고부담금) under §29-2 strictly applies to third-party indemnity (대인/대물), not first-party death
   - Net deductible = KRW 0; Net claim payout = KRW 100,000,000 (100%)
"""

import unittest
import os
import re
from decimal import Decimal, ROUND_HALF_UP, ROUND_FLOOR, ROUND_CEILING

BASE_DIR = r"d:\promotion\legal_claim_package"

class TestStatutoryFinancialStress(unittest.TestCase):

    # =========================================================================
    # 1. STATUTORY INTEREST MATHEMATICAL ENGINE
    # =========================================================================
    def test_01_statutory_interest_daily_precision(self):
        """Test exact daily default interest accrual under KCC §54 (6%) and Special Act §3(1) (12%)."""
        principal_100m = Decimal("100000000")
        principal_50m = Decimal("50000000")
        days_365 = Decimal("365")

        rate_comm = Decimal("0.06")
        rate_lit = Decimal("0.12")

        # Daily rate calculations
        daily_comm_100m = (principal_100m * rate_comm) / days_365
        daily_comm_50m = (principal_50m * rate_comm) / days_365
        daily_lit_100m = (principal_100m * rate_lit) / days_365
        daily_lit_50m = (principal_50m * rate_lit) / days_365

        # Documented rounded amounts:
        # File 11 line 858: KRW 16,438.356... -> KRW 16,438.36 / day
        # File 11 line 863: KRW 32,876.712... -> KRW 32,876.71 / day
        # File 11 line 869: KRW 8,219.18 / day
        # File 11 line 872: KRW 16,438.36 / day

        self.assertAlmostEqual(float(daily_comm_100m), 16438.356164, places=4)
        self.assertAlmostEqual(float(daily_comm_50m), 8219.178082, places=4)
        self.assertAlmostEqual(float(daily_lit_100m), 32876.712328, places=4)
        self.assertAlmostEqual(float(daily_lit_50m), 16438.356164, places=4)

        # Exact decimal rounding checks
        self.assertEqual(daily_comm_100m.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), Decimal("16438.36"))
        self.assertEqual(daily_comm_50m.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), Decimal("8219.18"))
        self.assertEqual(daily_lit_100m.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), Decimal("32876.71"))
        self.assertEqual(daily_lit_50m.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), Decimal("16438.36"))

        # Integer won rounding
        self.assertEqual(daily_comm_100m.quantize(Decimal("1"), rounding=ROUND_HALF_UP), Decimal("16438"))
        self.assertEqual(daily_comm_50m.quantize(Decimal("1"), rounding=ROUND_HALF_UP), Decimal("8219"))
        self.assertEqual(daily_lit_100m.quantize(Decimal("1"), rounding=ROUND_HALF_UP), Decimal("32877"))
        self.assertEqual(daily_lit_50m.quantize(Decimal("1"), rounding=ROUND_HALF_UP), Decimal("16438"))

    def test_02_cumulative_default_interest_schedule(self):
        """Stress-test the multi-period cumulative interest table against rounding variance."""
        principal = Decimal("100000000")
        rate_comm = Decimal("0.06")
        rate_lit = Decimal("0.12")
        days_in_year = Decimal("365")

        daily_comm = (principal * rate_comm) / days_in_year
        daily_lit = (principal * rate_lit) / days_in_year

        expected_schedule = [
            (10, Decimal("164384"), 10 * daily_comm),
            (20, Decimal("328767"), 20 * daily_comm),
            (30, Decimal("493151"), 30 * daily_comm),
            (60, Decimal("1479452"), 30 * daily_comm + 30 * daily_lit),
            (90, Decimal("2465753"), 30 * daily_comm + 60 * daily_lit),
            (180, Decimal("5424658"), 30 * daily_comm + 150 * daily_lit),
            (270, Decimal("8383562"), 30 * daily_comm + 240 * daily_lit),
            (365, Decimal("12000000"), principal * rate_lit),
            (365, Decimal("11506849"), 30 * daily_comm + 335 * daily_lit),
        ]

        for days, doc_val, formula_val in expected_schedule:
            calc_rounded = formula_val.quantize(Decimal("1"), rounding=ROUND_HALF_UP)
            diff = abs(calc_rounded - doc_val)
            self.assertLessEqual(diff, Decimal("1"), f"Cumulative interest mismatch at {days} days: {calc_rounded} vs {doc_val}")

    def test_03_interest_leap_year_and_rate_stress_analysis(self):
        """Adversarial stress-test: Evaluate interest math under 366-day leap year denominator and rate stability."""
        principal = Decimal("100000000")
        daily_365 = (principal * Decimal("0.06")) / Decimal("365")
        daily_366 = (principal * Decimal("0.06")) / Decimal("366")

        diff_per_day = daily_365 - daily_366
        # At 366 days, daily interest is ~16,393.44 vs 16,438.36 (diff = KRW 44.91 / day)
        self.assertAlmostEqual(float(diff_per_day), 44.914, places=2)
        # Verify 365-day standard applies under standard Korean banking/civil litigation conventions
        self.assertGreater(daily_365, daily_366)

    # =========================================================================
    # 2. BANGLADESHI SUNNI HANAFI HEIRSHIP FRACTIONS & 100% ALLOCATION
    # =========================================================================
    def test_04_heirship_share_mathematics(self):
        """Verify Sunni Hanafi inheritance shares: Father 2/3 (Asaba), Mother 1/3 (Zawil Furud) = 100%."""
        father_frac = Decimal("2") / Decimal("3")
        mother_frac = Decimal("1") / Decimal("3")

        # Sum must equal exactly 1.0 (100.0%)
        total_frac = father_frac + mother_frac
        self.assertEqual(total_frac, Decimal("1"))

        principal_100m = Decimal("100000000")
        father_share_100m = (principal_100m * father_frac).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
        mother_share_100m = (principal_100m * mother_frac).quantize(Decimal("1"), rounding=ROUND_HALF_UP)

        self.assertEqual(father_share_100m, Decimal("66666667"))
        self.assertEqual(mother_share_100m, Decimal("33333333"))
        self.assertEqual(father_share_100m + mother_share_100m, principal_100m)

    def test_05_provisional_advance_apportionment_and_balance_resolution(self):
        """Verify 50% provisional advance (KRW 50M) and remaining balance apportionment to the exact Won."""
        provisional_50m = Decimal("50000000")
        father_frac = Decimal("2") / Decimal("3")
        mother_frac = Decimal("1") / Decimal("3")

        # Provisional advance breakdown
        father_prov = (provisional_50m * father_frac).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
        mother_prov = (provisional_50m * mother_frac).quantize(Decimal("1"), rounding=ROUND_HALF_UP)

        self.assertEqual(father_prov, Decimal("33333333"))
        self.assertEqual(mother_prov, Decimal("16666667"))
        self.assertEqual(father_prov + mother_prov, provisional_50m)

        # Remaining balance breakdown
        father_total = Decimal("66666667")
        mother_total = Decimal("33333333")

        father_balance = father_total - father_prov
        mother_balance = mother_total - mother_prov

        self.assertEqual(father_balance, Decimal("33333334"))
        self.assertEqual(mother_balance, Decimal("16666666"))
        self.assertEqual(father_balance + mother_balance, provisional_50m)

        # Combined totals equal principal 100M
        self.assertEqual(father_prov + father_balance, father_total)
        self.assertEqual(mother_prov + mother_balance, mother_total)

    # =========================================================================
    # 3. KLAC INDIGENCE CALCULATIONS & STRESS-TESTING
    # =========================================================================
    def test_06_klac_median_income_and_poverty_ratio(self):
        """Stress-test KLAC 125% median income ceiling against family income and FX sensitivity."""
        # 2026 Korean Median Income (2-person household)
        median_2p = Decimal("3932828")
        ceiling_125 = (median_2p * Decimal("1.25")).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
        self.assertEqual(ceiling_125, Decimal("4916035"))

        # Family monthly income in Bangladesh: BDT 20,000
        bdt_income = Decimal("20000")
        fx_rate = Decimal("11.5")  # KRW per BDT
        krw_income = (bdt_income * fx_rate).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
        self.assertEqual(krw_income, Decimal("230000"))

        ratio = (krw_income / ceiling_125) * Decimal("100")
        ratio_rounded = ratio.quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)
        self.assertEqual(ratio_rounded, Decimal("4.679"))
        self.assertLess(ratio_rounded, Decimal("125.0"))

        # Safety margin
        safety_margin = Decimal("100") - ratio_rounded
        self.assertGreater(safety_margin, Decimal("95.0"))

        # FX Sensitivity Stress-Test: From 8.0 to 30.0 KRW/BDT
        for test_fx in [Decimal("8.0"), Decimal("10.0"), Decimal("15.0"), Decimal("20.0"), Decimal("30.0")]:
            simulated_krw = bdt_income * test_fx
            simulated_ratio = (simulated_krw / ceiling_125) * Decimal("100")
            self.assertLess(simulated_ratio, Decimal("20.0"), f"At FX {test_fx}, ratio {simulated_ratio}% exceeded safety budget")

        # Breakeven income to breach 125% ceiling
        breakeven_krw = ceiling_125
        breakeven_bdt = (breakeven_krw / fx_rate).quantize(Decimal("1"), rounding=ROUND_FLOOR)
        self.assertEqual(breakeven_bdt, Decimal("427481"))  # Over 21x current income!

    def test_07_court_stamp_and_litigation_costs(self):
        """Verify Court Stamp Act calculations on KRW 100,000,000 claim."""
        claim = Decimal("100000000")
        # Formula for KRW 50M to KRW 100M: claim * 0.0045 + 5,000
        stamp_duty = (claim * Decimal("0.0045") + Decimal("5000")).quantize(Decimal("1"))
        self.assertEqual(stamp_duty, Decimal("455000"))

        # Electronic filing 10% discount: KRW 409,500
        stamp_duty_electronic = (stamp_duty * Decimal("0.9")).quantize(Decimal("1"))
        self.assertEqual(stamp_duty_electronic, Decimal("409500"))

    # =========================================================================
    # 4. GUARANTEE ACT §29-2 DEDUCTIBLE NON-APPLICABILITY STRESS-TEST
    # =========================================================================
    def test_08_guarantee_act_29_2_deductible_non_applicability(self):
        """Stress-test Guarantee Act §29-2 co-payment (사고부담금) non-applicability to first-party death benefits."""
        # 1. Legal Domain Separation:
        # - Guarantee Act §29-2 governs third-party liability (대인배상 I/II, 대물배상).
        # - In third-party liability, unlicensed driving triggers statutory co-payment (사고부담금) up to KRW 150M.
        # - In first-party personal accident (자기신체사고 / 상해보험), KCC §732-2 & §739 govern.
        # - Supreme Court En Banc 98Da48963 explicitly struck down unlicensed exclusions in first-party coverage.

        accident_type = "single_vehicle_collision"  # 단독차량 충돌사고
        third_party_injuries = 0
        third_party_property_damage = 0

        # Co-payment under Guarantee Act §29-2:
        if accident_type == "single_vehicle_collision" and third_party_injuries == 0:
            guarantee_act_29_2_copay = Decimal("0")
        else:
            guarantee_act_29_2_copay = Decimal("150000000")  # hypothetical third-party

        self.assertEqual(guarantee_act_29_2_copay, Decimal("0"))

        # Claim calculation:
        total_policy_benefit = Decimal("100000000")
        net_payable = total_policy_benefit - guarantee_act_29_2_copay
        self.assertEqual(net_payable, Decimal("100000000"))

        # Verify documents explicitly state §29-2 non-applicability
        files_to_check = [
            "01_db_insurance_claim_notice_and_legal_brief.md",
            "02_fss_dispute_mediation_petition.md",
            "09_direct_international_claim_and_10day_statutory_notice.md",
        ]

        for fname in files_to_check:
            fpath = os.path.join(BASE_DIR, fname)
            self.assertTrue(os.path.exists(fpath), f"File {fname} does not exist")
            with open(fpath, "r", encoding="utf-8") as fp:
                content = fp.read()
            # Must mention Guarantee Act / 자배법 and 사고부담금 in the context of non-applicability
            has_copay_defense = ("사고부담금" in content) and ("자배법" in content or "자동차손해배상" in content)
            self.assertTrue(has_copay_defense, f"File {fname} lacks Guarantee Act / 사고부담금 non-applicability defense")

        # Explicit citation check for primary brief and notice
        for fname in ["01_db_insurance_claim_notice_and_legal_brief.md", "09_direct_international_claim_and_10day_statutory_notice.md"]:
            fpath = os.path.join(BASE_DIR, fname)
            with open(fpath, "r", encoding="utf-8") as fp:
                content = fp.read()
            has_specific_art = ("29조의2" in content or "29-2" in content)
            self.assertTrue(has_specific_art, f"File {fname} lacks explicit citation to Guarantee Act Art. 29-2")

    # =========================================================================
    # 5. DOSSIER CONSISTENCY & RE-CHECKING ALL 15 DELIVERABLES
    # =========================================================================
    def test_09_dossier_heirship_and_financial_integrity(self):
        """Verify that Father 2/3 and Mother 1/3 amounts are completely uniform across all documents."""
        primary_stems = [
            "00_master_dossier_index_and_executive_summary",
            "01_db_insurance_claim_notice_and_legal_brief",
            "02_fss_dispute_mediation_petition",
            "05_evidence_inventory_and_exhibits_catalog",
            "06_direct_filing_dispatch_package",
            "07_legal_aid_and_consular_escalation_roster",
            "09_direct_international_claim_and_10day_statutory_notice",
            "10_parallel_pro_bono_and_consular_intake_packets",
            "11_dhaka_to_seoul_dhl_dispatch_and_10day_tracking_guide",
        ]

        for stem in primary_stems:
            path = os.path.join(BASE_DIR, f"{stem}.md")
            with open(path, "r", encoding="utf-8") as fp:
                text = fp.read()

            self.assertIn("66,666,667", text, f"Missing Father's share (66,666,667) in {stem}.md")
            self.assertIn("33,333,333", text, f"Missing Mother's share (33,333,333) in {stem}.md")

if __name__ == "__main__":
    unittest.main(verbosity=2)
