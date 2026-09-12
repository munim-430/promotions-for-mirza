import unittest, os, re

FILES = [
    'd:/promotion/legal_claim_package/01_samsung_fire_claim_notice_and_legal_brief.md',
    'd:/promotion/legal_claim_package/02_fss_dispute_mediation_petition.md',
    'd:/promotion/legal_claim_package/06_direct_filing_dispatch_package.md',
    'd:/promotion/legal_claim_package/07_legal_aid_and_consular_escalation_roster.md',
    'd:/promotion/legal_claim_package/08_attorney_in_fact_execution_checklist.md',
]

class TestScenario2LegalStatutoryBar(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dossier = {}
        for fpath in FILES:
            fname = os.path.basename(fpath)
            with open(fpath, 'r', encoding='utf-8') as f:
                cls.dossier[fname] = f.read()

    def test_2_1_commercial_code_statutory_trinity(self):
        for fname in ['01_samsung_fire_claim_notice_and_legal_brief.md', 
                      '02_fss_dispute_mediation_petition.md', 
                      '06_direct_filing_dispatch_package.md', 
                      '07_legal_aid_and_consular_escalation_roster.md', 
                      '08_attorney_in_fact_execution_checklist.md']:
            text = self.dossier[fname]
            self.assertTrue('732조의2' in text or '732-2' in text, f'{fname} must cite Commercial Code 732-2')
            self.assertTrue('663' in text, f'{fname} must cite Commercial Code 663')
            self.assertTrue('739' in text, f'{fname} must cite Commercial Code 739')

    def test_2_2_supreme_court_98da48963_en_banc_precedent(self):
        for fname in ['01_samsung_fire_claim_notice_and_legal_brief.md',
                      '02_fss_dispute_mediation_petition.md',
                      '06_direct_filing_dispatch_package.md',
                      '07_legal_aid_and_consular_escalation_roster.md',
                      '08_attorney_in_fact_execution_checklist.md']:
            text = self.dossier[fname]
            self.assertTrue('98다48963' in text or '98Da48963' in text, f'{fname} must cite 98Da48963 En Banc')

    def test_2_3_unlicensed_driving_exclusion_invalidation_doctrine(self):
        f1_text = self.dossier['01_samsung_fire_claim_notice_and_legal_brief.md']
        f6_text = self.dossier['06_direct_filing_dispatch_package.md']
        f8_text = self.dossier['08_attorney_in_fact_execution_checklist.md']
        
        for text in [f1_text, f6_text, f8_text]:
            self.assertTrue('무면허' in text or 'unlicensed' in text.lower(), 'Must address unlicensed driving')
            self.assertTrue('중과실' in text or 'gross negligence' in text.lower(), 'Must establish gross negligence')
            self.assertTrue('무효' in text or 'null and void' in text.lower(), 'Must establish clause invalidity / nullity')

    def test_2_4_intent_vs_gross_negligence_rebuttal(self):
        f1_text = self.dossier['01_samsung_fire_claim_notice_and_legal_brief.md']
        f6_text = self.dossier['06_direct_filing_dispatch_package.md']
        f7_text = self.dossier['07_legal_aid_and_consular_escalation_roster.md']
        
        self.assertTrue('단독' in f1_text or '단독' in f6_text, 'Must state single-vehicle accident')
        self.assertTrue('가드레일' in f1_text or '가드레일' in f6_text, 'Must state guardrail collision')
        self.assertTrue('고의' in f1_text and '중과실' in f1_text, 'Must contrast intent vs gross negligence')

    def test_2_5_heirship_inherent_property_doctrine(self):
        f1_text = self.dossier['01_samsung_fire_claim_notice_and_legal_brief.md']
        f8_text = self.dossier['08_attorney_in_fact_execution_checklist.md']
        self.assertTrue('2003다29463' in f1_text or '2003다29463' in f8_text, 'Must cite 2003Da29463')
        self.assertTrue('고유재산' in f1_text or '고유재산' in f8_text, 'Must establish inherent property right')

if __name__ == '__main__':
    unittest.main()
