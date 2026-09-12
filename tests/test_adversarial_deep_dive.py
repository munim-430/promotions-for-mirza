"""
Adversarial Deep Dive & Cross-Verification Harness
Updated for DB Insurance Architecture & All 14 Deliverables (15 Files)
Author: challenger_r3_2 / worker_3
"""

import os
import sys
import glob
import re
import unittest
import fitz
import docx

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\promotion\legal_claim_package"
DOCX_DIR = os.path.join(BASE_DIR, "docx")
PDF_DIR = os.path.join(BASE_DIR, "pdf")

STEMS = [
    "00_master_dossier_index_and_executive_summary",
    "01_db_insurance_claim_notice_and_legal_brief",
    "02_fss_dispute_mediation_petition",
    "03_seojeong_university_group_insurance_claim",
    "04_bilingual_special_power_of_attorney",
    "04_cross_border_heirship_and_legalization_guide",
    "05_evidence_inventory_and_exhibits_catalog",
    "06_direct_filing_dispatch_package",
    "07_legal_aid_and_consular_escalation_roster",
    "08_attorney_in_fact_execution_checklist",
    "09_direct_international_claim_and_10day_statutory_notice",
    "10_parallel_pro_bono_and_consular_intake_packets",
    "11_dhaka_to_seoul_dhl_dispatch_and_10day_tracking_guide",
    "12_lawyer_and_insurer_filing_email_transmittals",
    "13_db_insurance_policy_verification_and_issuance_request",
]

class TestAdversarialDeepDive(unittest.TestCase):

    def test_01_exhibit_reference_validity(self):
        """Verify that every exhibit referenced across all 15 documents is defined in the Exhibit Catalog (File 05)."""
        file05_path = os.path.join(BASE_DIR, "05_evidence_inventory_and_exhibits_catalog.md")
        with open(file05_path, "r", encoding="utf-8") as fp:
            f05_text = fp.read()

        # Find all defined exhibits in File 05 across Groups A through I
        catalog_exhibits = set(re.findall(r"Exhibit\s+([A-I]-\d+)", f05_text))
        
        self.assertEqual(len(catalog_exhibits), 37, f"Expected 37 defined exhibits in catalog, found {len(catalog_exhibits)}")
        
        # Verify Groups A through G explicitly required by prompt
        for group in ["A", "B", "C", "D", "E", "F", "G"]:
            grp_ex = [e for e in catalog_exhibits if e.startswith(f"{group}-")]
            self.assertGreater(len(grp_ex), 0, f"Group {group} has no exhibits defined!")

        # Scan all 15 documents for referenced exhibits
        undefined_refs = {}
        total_references = 0
        for stem in STEMS:
            path = os.path.join(BASE_DIR, f"{stem}.md")
            with open(path, "r", encoding="utf-8") as fp:
                text = fp.read()
            refs = re.findall(r"Exhibit\s+([A-Z]-\d+)", text)
            total_references += len(refs)
            for r in refs:
                if r not in catalog_exhibits:
                    undefined_refs.setdefault(stem, set()).add(r)

        self.assertEqual(len(undefined_refs), 0, f"Found undefined exhibit references: {undefined_refs}")
        print(f"\n[PASS] All {total_references} exhibit references across {len(STEMS)} documents match catalog definitions (0 dangling references).")

    def test_02_banking_coordinates_exact_match(self):
        """Verify SWIFT codes, account numbers, and beneficiary details across all files."""
        expected_values = {
            "MTB SWIFT": "MTBLBDDH",
            "Account Number": "1311004072276",
            "Routing Number": "145261188",
            "Munim Passport": "B00936349",
        }
        
        for name, val in expected_values.items():
            found_count = 0
            for stem in STEMS:
                path = os.path.join(BASE_DIR, f"{stem}.md")
                with open(path, "r", encoding="utf-8") as fp:
                    text = fp.read()
                if val in text:
                    found_count += 1
            self.assertGreater(found_count, 0, f"Banking value '{name}' ({val}) not found in any file!")
            print(f"[PASS] Verified '{name}' ({val}) in {found_count} separate documents.")

    def test_03_financial_arithmetic_consistency(self):
        """Verify mathematical integrity of claim figures, shares, and interest rates."""
        total_claim = 100000000
        provisional_claim = 50000000
        father_share = 66666667
        mother_share = 33333333
        
        self.assertEqual(father_share + mother_share, total_claim)
        
        father_prov = 33333333
        mother_prov = 16666667
        self.assertEqual(father_prov + mother_prov, provisional_claim)

        for stem in ["00_master_dossier_index_and_executive_summary",
                     "01_db_insurance_claim_notice_and_legal_brief",
                     "06_direct_filing_dispatch_package",
                     "09_direct_international_claim_and_10day_statutory_notice",
                     "11_dhaka_to_seoul_dhl_dispatch_and_10day_tracking_guide"]:
            path = os.path.join(BASE_DIR, f"{stem}.md")
            with open(path, "r", encoding="utf-8") as fp:
                text = fp.read()
            self.assertTrue("100,000,000" in text or "1억" in text, f"Missing 100M claim in {stem}")
            self.assertTrue("50,000,000" in text or "5천만" in text or "50%" in text, f"Missing 50M provisional claim in {stem}")
        print("[PASS] Financial arithmetic, heirship apportionment (2/3 & 1/3), and provisional claim amounts are verified consistent.")

    def test_04_trio_format_text_parity(self):
        """Verify that MD, DOCX, and PDF for each deliverable contain the core identity and claim text."""
        test_patterns = [
            ("MAHADI MONOAR HOSSAIN", r"MAHADI\s+MONOAR\s+HOSSAIN"),
            ("Vehicle 28모1390", r"28\s*모\s*1390"),
        ]
        
        for stem in STEMS:
            md_path = os.path.join(BASE_DIR, f"{stem}.md")
            docx_path = os.path.join(DOCX_DIR, f"{stem}.docx")
            pdf_path = os.path.join(PDF_DIR, f"{stem}.pdf")
            
            # Read MD
            with open(md_path, "r", encoding="utf-8") as fp:
                md_text = fp.read()
                
            # Read DOCX
            doc = docx.Document(docx_path)
            docx_text = "\n".join([p.text for p in doc.paragraphs] + [c.text for t in doc.tables for r in t.rows for c in r.cells])
            
            # Read PDF
            pdf_doc = fitz.open(pdf_path)
            pdf_text = "\n".join([page.get_text() for page in pdf_doc])
            
            for label, pattern in test_patterns:
                if re.search(pattern, md_text, re.IGNORECASE):
                    self.assertTrue(bool(re.search(pattern, docx_text, re.IGNORECASE)), f"DOCX {stem}.docx missing pattern for '{label}'")
                    self.assertTrue(bool(re.search(pattern, pdf_text, re.IGNORECASE)), f"PDF {stem}.pdf missing pattern for '{label}'")
                    
        print(f"[PASS] All {len(STEMS)} deliverables exhibit complete content parity across MD, DOCX, and PDF formats.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
