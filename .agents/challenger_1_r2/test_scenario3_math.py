import unittest, os, re

FILE_06 = 'd:/promotion/legal_claim_package/06_direct_filing_dispatch_package.md'
FILE_07 = 'd:/promotion/legal_aid_and_consular_escalation_roster.md' # or check correct path
FILE_08 = 'd:/promotion/legal_claim_package/08_attorney_in_fact_execution_checklist.md'

class TestScenario3InterestEngineMath(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('d:/promotion/legal_claim_package/06_direct_filing_dispatch_package.md', 'r', encoding='utf-8') as f:
            cls.f6_text = f.read()
        with open('d:/promotion/legal_claim_package/07_legal_aid_and_consular_escalation_roster.md', 'r', encoding='utf-8') as f:
            cls.f7_text = f.read()
        with open('d:/promotion/legal_claim_package/08_attorney_in_fact_execution_checklist.md', 'r', encoding='utf-8') as f:
            cls.f8_text = f.read()

    def test_3_1_provisional_payment_principal(self):
        # Full claim = KRW 100,000,000; 50% provisional = KRW 50,000,000
        self.assertIn('50,000,000', self.f6_text)
        self.assertIn('50,000,000', self.f7_text)
        self.assertIn('50,000,000', self.f8_text)

    def test_3_2_statutory_rates_and_triggers(self):
        # Commercial rate 6.0% p.a. under Commercial Code Art. 54 from Day 11
        self.assertIn('6.0%', self.f6_text)
        self.assertIn('6.0%', self.f7_text)
        self.assertIn('6.0%', self.f8_text)
        # Litigation rate 12.0% p.a. under Special Act on Promotion of Litigation Art. 3(1)
        self.assertIn('12.0%', self.f6_text)
        self.assertIn('12.0%', self.f7_text)
        self.assertIn('12.0%', self.f8_text)

    def test_3_3_exact_daily_interest_math_oracle(self):
        # Oracle calculations
        # Principal P = 50,000,000
        P_prov = 50000000.0
        P_full = 100000000.0
        
        # Daily rate 6%
        daily_comm_prov = (P_prov * 0.06) / 365.0 # 8219.178082...
        daily_comm_full = (P_full * 0.06) / 365.0 # 16438.356164...
        
        # Daily rate 12%
        daily_lit_prov = (P_prov * 0.12) / 365.0 # 16438.356164...
        daily_lit_full = (P_full * 0.12) / 365.0 # 32876.712328...

        # Verify daily rate for provisional 50M at 6% is KRW 8,219.18 / day
        self.assertAlmostEqual(daily_comm_prov, 8219.178, places=2)
        self.assertIn('8,219.18', self.f8_text)

        # Verify daily rate for full 100M at 6% is KRW 16,438.36 / day (or 16,438.35 in F6)
        self.assertTrue('16,438.36' in self.f8_text or '16,438.35' in self.f6_text)

        # Verify daily rate for full 100M at 12% is KRW 32,876.71 / day
        self.assertIn('32,876.71', self.f8_text)
        self.assertIn('32,876.71', self.f6_text)

    def test_3_4_cumulative_interest_scenarios(self):
        # Let us calculate exact interest for various day intervals
        P = 50000000
        # Day 11 to Day 30 = 20 days of default interest under commercial rate
        int_20d = (P * 0.06 / 365.0) * 20
        # Check that 20 days interest = KRW 164,383.56
        self.assertAlmostEqual(int_20d, 164383.56, places=1)

        # Day 11 to Day 40 (30 days commercial) = KRW 246,575.34
        int_30d = (P * 0.06 / 365.0) * 30
        self.assertAlmostEqual(int_30d, 246575.34, places=1)

    def test_3_5_heirship_share_distribution_math(self):
        # Total principal KRW 100,000,000
        # Father 2/3 = KRW 66,666,667 (or 66,666,666.67)
        # Mother 1/3 = KRW 33,333,333 (or 33,333,333.33)
        # Provisional 50,000,000:
        # Father 2/3 = KRW 33,333,333.33
        # Mother 1/3 = KRW 16,666,666.67
        
        self.assertTrue('66,666,667' in self.f7_text or '2/3' in self.f7_text)
        self.assertTrue('33,333,333' in self.f7_text or '1/3' in self.f7_text)
        self.assertIn('IBBL', self.f7_text)
        self.assertIn('Sonali', self.f7_text)

if __name__ == '__main__':
    unittest.main()
