import unittest, os, re

FILE_06 = 'd:/promotion/legal_claim_package/06_direct_filing_dispatch_package.md'
FILE_07 = 'd:/promotion/legal_claim_package/07_legal_aid_and_consular_escalation_roster.md'
FILE_08 = 'd:/promotion/legal_claim_package/08_attorney_in_fact_execution_checklist.md'

class TestScenario1PostalCounterIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(FILE_06, 'r', encoding='utf-8') as f:
            cls.f6_text = f.read()
        with open(FILE_07, 'r', encoding='utf-8') as f:
            cls.f7_text = f.read()
        with open(FILE_08, 'r', encoding='utf-8') as f:
            cls.f8_text = f.read()

    def test_1_1_content_certified_mail_structure(self):
        elements = ['발신인', '수신인', '청구 취지', '청구 원인', '첨부서류']
        for elem in elements:
            self.assertIn(elem, self.f6_text, f'Missing required structural element: {elem}')

    def test_1_2_samsung_fire_recipient_and_routing(self):
        self.assertIn('삼성화재해상보험주식회사', self.f6_text)
        self.assertIn('이문화', self.f6_text)
        self.assertIn('06620', self.f6_text)
        self.assertIn('서초대로74길 14', self.f6_text)
        self.assertIn('심기철', self.f6_text)
        self.assertIn('010-8969-0440', self.f6_text)
        self.assertIn('2026-SF-AUTO-28M1390', self.f6_text)
        self.assertIn('28모1390', self.f6_text)

    def test_1_3_seojeong_univ_recipient_and_routing(self):
        self.assertIn('서정대학교', self.f6_text)
        self.assertIn('양영희', self.f6_text)
        self.assertIn('11429', self.f6_text)
        self.assertIn('서정로 27', self.f6_text)
        self.assertIn('국제교류처', self.f6_text)
        self.assertIn('202581042', self.f6_text)

    def test_1_4_korea_post_postal_rules(self):
        self.assertIn('우편법 시행규칙', self.f6_text)
        self.assertIn('원본 1부', self.f6_text)
        self.assertIn('등본 2부', self.f6_text)
        self.assertTrue('간인' in self.f6_text or '契印' in self.f6_text)
        self.assertTrue('간인' in self.f8_text or '契印' in self.f8_text)
        self.assertIn('배달증명', self.f6_text)
        self.assertIn('익일특급', self.f6_text)
        self.assertIn('3년', self.f6_text)

    def test_1_5_overseas_sender_representation_edge_case(self):
        self.assertIn('BELAL HOSSAIN', self.f6_text)
        self.assertIn('MONOARA BEGUM', self.f6_text)
        self.assertIn('19741913345000128', self.f6_text)
        self.assertIn('19801913345000129', self.f6_text)
        self.assertIn('Md Monirul Islam', self.f6_text)
        self.assertIn('주한 방글라데시 인권위원회', self.f6_text)
        self.assertIn('특별위임장', self.f6_text)

    def test_1_6_internet_epost_backup_workflow(self):
        self.assertIn('epost.go.kr', self.f6_text)
        self.assertIn('전자내용증명', self.f6_text)
        self.assertIn('전자타임스탬프', self.f6_text)
        self.assertIn('전자내용증명', self.f8_text)

if __name__ == '__main__':
    unittest.main()
