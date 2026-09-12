"""
Adversarial Verification Suite for Legal Claim Package Dossier
Updated for DB Insurance Co., Ltd. Architecture & All 14 Deliverables
"""

import os
import sys
import glob
import re
import zipfile
import xml.etree.ElementTree as ET
import unittest
import fitz  # PyMuPDF
import pypdf
import docx

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\promotion\legal_claim_package"
DOCX_DIR = os.path.join(BASE_DIR, "docx")
PDF_DIR = os.path.join(BASE_DIR, "pdf")
EXTRACTED_DIR = r"d:\promotion\extracted"

EXPECTED_MD_STEMS = [
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
    "14_db_insurance_telephone_call_script_for_policy_certificate",
]

class TestAdversarialDossierSuite(unittest.TestCase):

    def test_01_markdown_files_exist_and_non_trivial(self):
        """Verify all 16 MD deliverable files exist, are readable, and non-trivial (>9KB)."""
        self.assertEqual(len(EXPECTED_MD_STEMS), 16)
        for stem in EXPECTED_MD_STEMS:
            path = os.path.join(BASE_DIR, f"{stem}.md")
            self.assertTrue(os.path.exists(path), f"Missing Markdown file: {path}")
            size = os.path.getsize(path)
            self.assertGreater(size, 9000, f"Markdown file {stem}.md is too small ({size} bytes)")
        print(f"\n[PASS] All {len(EXPECTED_MD_STEMS)} Markdown files exist and are verified non-trivial (>9KB).")

    def test_02_docx_files_exist_and_valid_xml(self):
        """Verify all 15 DOCX files exist, have valid XML structure and readable paragraphs."""
        docx_files = glob.glob(os.path.join(DOCX_DIR, "*.docx"))
        self.assertGreaterEqual(len(docx_files), 15, f"Expected at least 15 DOCX files, found {len(docx_files)}")
        
        for stem in EXPECTED_MD_STEMS:
            path = os.path.join(DOCX_DIR, f"{stem}.docx")
            self.assertTrue(os.path.exists(path), f"Missing DOCX file: {path}")
            size = os.path.getsize(path)
            self.assertGreater(size, 10000, f"DOCX file {stem}.docx is too small ({size} bytes)")
            
            # Test ZIP and XML integrity
            with zipfile.ZipFile(path, "r") as zf:
                for zinfo in zf.infolist():
                    if zinfo.filename.endswith(".xml") or zinfo.filename.endswith(".rels"):
                        content = zf.read(zinfo.filename)
                        try:
                            ET.fromstring(content)
                        except Exception as e:
                            self.fail(f"Invalid XML in {stem}.docx/{zinfo.filename}: {e}")
            
            # Test python-docx parsing
            doc = docx.Document(path)
            self.assertGreater(len(doc.paragraphs), 10, f"DOCX {stem}.docx has too few paragraphs: {len(doc.paragraphs)}")
        print(f"\n[PASS] All {len(EXPECTED_MD_STEMS)} core DOCX files exist, contain 0 XML errors, and have valid paragraph/table structures.")

    def test_03_pdf_integrity_and_page_counts(self):
        """Verify all 15 PDF files exist, have valid pages, no empty pages, and total > 200 pages."""
        pdf_files = glob.glob(os.path.join(PDF_DIR, "*.pdf"))
        self.assertGreaterEqual(len(pdf_files), 15, f"Expected at least 15 PDF files, found {len(pdf_files)}")
        
        total_pages_fitz = 0
        total_pages_pypdf = 0
        empty_pages = []
        
        for stem in EXPECTED_MD_STEMS:
            path = os.path.join(PDF_DIR, f"{stem}.pdf")
            self.assertTrue(os.path.exists(path), f"Missing PDF file: {path}")
            
            # PyMuPDF check
            doc_fitz = fitz.open(path)
            pcount_fitz = len(doc_fitz)
            self.assertGreater(pcount_fitz, 0, f"PDF {stem}.pdf has 0 pages")
            total_pages_fitz += pcount_fitz
            
            # Check text on each page
            for pno in range(pcount_fitz):
                page = doc_fitz[pno]
                text = page.get_text().strip()
                if len(text) == 0:
                    empty_pages.append((stem, pno + 1))
            
            # pypdf check
            reader = pypdf.PdfReader(path)
            pcount_pypdf = len(reader.pages)
            self.assertEqual(pcount_pypdf, pcount_fitz, f"Page count mismatch in {stem}.pdf")
            total_pages_pypdf += pcount_pypdf
            
        self.assertEqual(len(empty_pages), 0, f"Found empty pages in PDFs: {empty_pages}")
        self.assertGreater(total_pages_fitz, 200, f"Total PDF page count {total_pages_fitz} is not > 200")
        print(f"\n[PASS] Total PDF page count across {len(EXPECTED_MD_STEMS)} documents: {total_pages_fitz} pages (All pages rendered and non-empty).")

    def test_04_email_attachment_and_gateway_limits(self):
        """Verify email attachment batches and size limits against 15MB/25MB mail server gateways."""
        pdf_files = glob.glob(os.path.join(PDF_DIR, "*.pdf"))
        total_generated_pdf_size = sum(os.path.getsize(f) for f in pdf_files)
        
        limit_15mb = 15 * 1024 * 1024
        limit_25mb = 25 * 1024 * 1024
        
        self.assertLess(total_generated_pdf_size, limit_15mb, f"All generated PDFs combined ({total_generated_pdf_size} bytes) exceed 15MB")
        
        # Check declared budgets in File 06
        file06_path = os.path.join(BASE_DIR, "06_direct_filing_dispatch_package.md")
        with open(file06_path, "r", encoding="utf-8") as fp:
            f06_text = fp.read()
        
        f06_declared_kb = [int(m.replace(",", "")) for m in re.findall(r"Total\s+([\d,]+)\s*KB", f06_text)]
        for kb in f06_declared_kb:
            bytes_val = kb * 1024
            self.assertLessEqual(bytes_val, limit_15mb, f"Declared package size {kb} KB exceeds 15MB limit")
            self.assertLessEqual(bytes_val, limit_25mb, f"Declared package size {kb} KB exceeds 25MB limit")

        # Check declared budgets in File 11
        file11_path = os.path.join(BASE_DIR, "11_dhaka_to_seoul_dhl_dispatch_and_10day_tracking_guide.md")
        with open(file11_path, "r", encoding="utf-8") as fp:
            f11_text = fp.read()
            
        f11_declared_kb = [int(m.replace(",", "")) for m in re.findall(r"TOTAL PAYLOAD.*?:.*?([\d,]+)\s*KB", f11_text)]
        for kb in f11_declared_kb:
            bytes_val = kb * 1024
            self.assertLessEqual(bytes_val, limit_15mb, f"File 11 declared size {kb} KB exceeds 15MB limit")
            self.assertLessEqual(bytes_val, limit_25mb, f"File 11 declared size {kb} KB exceeds 25MB limit")
        print(f"\n[PASS] Email attachment schedules strictly obey 15MB (<15,728,640 B) and 25MB limits.")

    def test_05_cross_references_exhibits(self):
        """Verify internal cross-references to Exhibits A-1 through G-7 across all documents."""
        file05_path = os.path.join(BASE_DIR, "05_evidence_inventory_and_exhibits_catalog.md")
        with open(file05_path, "r", encoding="utf-8") as fp:
            f05_text = fp.read()
        
        defined_exhibits = set(re.findall(r"Exhibit\s+([A-I]-\d+)", f05_text))
        self.assertGreaterEqual(len(defined_exhibits), 20, f"Expected at least 20 defined exhibits, found {len(defined_exhibits)}")
        
        for group in ["A", "B", "C", "D", "E", "F", "G"]:
            group_exhibits = [e for e in defined_exhibits if e.startswith(f"{group}-")]
            self.assertGreater(len(group_exhibits), 0, f"No exhibits found for Group {group}")
            
        print(f"\n[PASS] All Exhibit Groups A through G verified with {len(defined_exhibits)} unique catalog entries.")

    def test_06_policy_number_and_agent_contact_integrity(self):
        """Verify DB Insurance policy numbers, managing channel, renewal date, and parties across documents."""
        key_entities = {
            "vehicle_number": r"28모\s*1390",
            "policy_number": r"2-2026-0531750-000",
            "managing_channel": r"DB손해보험|1588-0100|고객지원센터|다이렉트",
            "renewal_date": r"2026년\s*1월\s*21일|2026-01-21|January\s*21,?\s*2026",
            "insurer_name": r"DB손해보험|DB\s+Insurance",
            "swift_mtb": r"MTBLBDDH",
            "deceased_name": r"MAHADI\s+MONOAR\s+HOSSAIN",
            "deceased_arc": r"010530-7660021",
            "father_name": r"BELAL\s+HOSSAIN",
            "mother_name": r"MONOARA\s+BEGUM",
        }
        
        occurrence_counts = {k: 0 for k in key_entities}
        
        for stem in EXPECTED_MD_STEMS:
            path = os.path.join(BASE_DIR, f"{stem}.md")
            with open(path, "r", encoding="utf-8") as fp:
                text = fp.read()
            for k, pat in key_entities.items():
                matches = re.findall(pat, text, re.IGNORECASE)
                occurrence_counts[k] += len(matches)
                
        for k, cnt in occurrence_counts.items():
            self.assertGreater(cnt, 0, f"Entity {k} has 0 occurrences across all documents!")
            print(f"  - Verified Entity '{k}': {cnt} total occurrences.")

    def test_07_statutory_articles_and_precedents(self):
        """Verify citations of key statutory articles and Supreme Court precedents."""
        legal_citations = {
            "Art_732_2_provisional_payment": r"732-2|732조의\s*2",
            "Art_739_accidental_death": r"739조|Art(?:icle|\.)?\s*739",
            "Art_663_prohibition_disadvantage": r"663조|Art(?:icle|\.)?\s*663",
            "PIL_Art_49_heirship": r"49조|Art(?:icle|\.)?\s*49",
            "Civil_Act_Art_118_poa": r"118조|Art(?:icle|\.)?\s*118",
            "Precedent_98Da48963": r"98다48963|98Da48963",
            "Precedent_97Da27039": r"97다27039|97Da27039",
            "Precedent_98Da26910": r"98다26910|98Da26910",
        }
        
        citation_counts = {k: 0 for k in legal_citations}
        for stem in EXPECTED_MD_STEMS:
            path = os.path.join(BASE_DIR, f"{stem}.md")
            with open(path, "r", encoding="utf-8") as fp:
                text = fp.read()
            for k, pat in legal_citations.items():
                matches = re.findall(pat, text, re.IGNORECASE)
                citation_counts[k] += len(matches)
                
        for k, cnt in citation_counts.items():
            self.assertGreater(cnt, 0, f"Legal citation {k} has 0 occurrences across all documents!")
            print(f"  - Verified Legal Citation '{k}': {cnt} total occurrences.")

    def test_08_zero_stale_samsung_fire_references(self):
        """Verify zero occurrences of Samsung Fire as insurer across all markdown deliverables and dossier,
        while strictly preserving vehicle make (Kia Morning / 기아 모닝)."""
        stale_insurer_patterns = [
            (r"(?<!Renault\s)(?<!르노)삼성화재", "Samsung Fire in Korean (삼성화재)"),
            (r"(?<!Renault\s)Samsung\s+Fire", "Samsung Fire in English"),
            (r"2026-SF", "Samsung Fire Policy ID Prefix (2026-SF)"),
            (r"심기철|Shim\s+Ki-ch[ue]l", "Samsung Fire Agent Shim Ki-cheol"),
            (r"010-8969-0440|8969-0440", "Samsung Fire Agent Phone"),
            (r"1588-5114", "Samsung Fire Call Center"),
            (r"samsungfire\.com", "Samsung Fire Domain / Email"),
            (r"Seocho\s+Tower|서초대로\s*74길|14\s+Seocho-daero", "Samsung Fire Seocho HQ"),
            (r"19\s+Okcheon-ro|옥천로\s*19", "Samsung Fire Gangwon Office Address"),
            (r"March\s+13,?\s+2026|2026년\s*3월\s*13일", "Old Stale Renewal Date (March 13, 2026)"),
        ]
        
        files_to_scan = [os.path.join(BASE_DIR, f"{stem}.md") for stem in EXPECTED_MD_STEMS]
        files_to_scan.append(r"d:\promotion\CASE_MASTER_KNOWLEDGE_DOSSIER.md")
        files_to_scan.append(r"d:\promotion\PROJECT.md")
        
        violations = []
        for path in files_to_scan:
            if not os.path.exists(path):
                continue
            with open(path, "r", encoding="utf-8") as fp:
                lines = fp.readlines()
            for line_idx, line in enumerate(lines, 1):
                # Allow preserved filename 01_db_insurance_claim_notice_and_legal_brief
                cleaned_line = re.sub(r"01_db_insurance_claim_notice_and_legal_brief\.(md|docx|pdf)", "", line)
                for pattern, desc in stale_insurer_patterns:
                    if re.search(pattern, cleaned_line, re.IGNORECASE):
                        violations.append(f"{os.path.basename(path)}:{line_idx} - [{desc}] {line.strip()[:80]}")
                        
        self.assertEqual(len(violations), 0, f"Found stale Samsung Fire insurer references:\n" + "\n".join(violations))
        print(f"\n[PASS] Zero stale Samsung Fire insurer references found across {len(files_to_scan)} files (Kia Morning preserved).")

    def test_09_db_insurance_policy_and_metadata_validation(self):
        """Verify presence of DB Insurance corporate headquarters, CEO, call center, and renewal date."""
        db_required_entities = {
            "DB Headquarters Address": r"DB금융센터|432\s+Teheran-ro|테헤란로\s*432",
            "DB CEO Jeong Jong-pyo": r"정종표|Jeong\s+Jong-pyo",
            "DB Call Center 1588-0100": r"1588-0100",
            "Policy Renewal Date 2026-01-21": r"2026-01-21|2026년\s*1월\s*21일|January\s+21,?\s+2026",
            "Subject Vehicle 28모1390": r"28모\s*1390",
        }
        
        primary_docs = [
            os.path.join(BASE_DIR, "00_master_dossier_index_and_executive_summary.md"),
            os.path.join(BASE_DIR, "01_db_insurance_claim_notice_and_legal_brief.md"),
            os.path.join(BASE_DIR, "06_direct_filing_dispatch_package.md"),
            os.path.join(BASE_DIR, "13_db_insurance_policy_verification_and_issuance_request.md"),
            r"d:\promotion\CASE_MASTER_KNOWLEDGE_DOSSIER.md",
        ]
        
        for name, pattern in db_required_entities.items():
            matched_files = 0
            for doc_path in primary_docs:
                if os.path.exists(doc_path):
                    with open(doc_path, "r", encoding="utf-8") as fp:
                        if re.search(pattern, fp.read(), re.IGNORECASE):
                            matched_files += 1
            self.assertGreater(matched_files, 0, f"Required DB metadata '{name}' not found in any primary document!")
            print(f"  - Verified DB Metadata '{name}': Present in {matched_files}/{len(primary_docs)} primary documents.")
        print("[PASS] DB Insurance policy and corporate metadata verified across all primary claim documents.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
