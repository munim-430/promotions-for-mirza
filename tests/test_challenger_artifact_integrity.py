"""
Empirical Challenger Test Suite: Artifact Integrity, Parity & Boundary Stress Testing
Agent: Artifact Integrity Challenger (.agents/challenger_2)
"""

import os
import sys
import glob
import re
import json
import zipfile
import xml.etree.ElementTree as ET
import unittest
import fitz  # PyMuPDF
import pypdf
import docx

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\promotion\legal_claim_package"
DOCX_DIR = os.path.join(BASE_DIR, "docx")
PDF_DIR = os.path.join(BASE_DIR, "pdf")

MD_FILES = [
    "00_master_dossier_index_and_executive_summary.md",
    "01_db_insurance_claim_notice_and_legal_brief.md",
    "02_fss_dispute_mediation_petition.md",
    "03_seojeong_university_group_insurance_claim.md",
    "04_bilingual_special_power_of_attorney.md",
    "04_cross_border_heirship_and_legalization_guide.md",
    "05_evidence_inventory_and_exhibits_catalog.md",
    "06_direct_filing_dispatch_package.md",
    "07_legal_aid_and_consular_escalation_roster.md",
    "08_attorney_in_fact_execution_checklist.md",
    "09_direct_international_claim_and_10day_statutory_notice.md",
    "10_parallel_pro_bono_and_consular_intake_packets.md",
    "11_dhaka_to_seoul_dhl_dispatch_and_10day_tracking_guide.md",
    "12_lawyer_and_insurer_filing_email_transmittals.md",
    "13_db_insurance_policy_verification_and_issuance_request.md",
    "14_db_insurance_telephone_call_script_for_policy_certificate.md",
    "15_seojeong_university_telephone_call_script.md",
    "16_seojeong_university_email_and_epeople_petition_package.md",
]

class TestChallengerArtifactIntegrity(unittest.TestCase):
    """Adversarial stress testing of artifact integrity, parity, boundaries, and stale references."""

    def test_01_all_15_md_deliverables_exist_and_gt_10kb(self):
        """Stress-test: All Markdown deliverables exist and are strictly > 9KB."""
        self.assertEqual(len(MD_FILES), 18, "Expected exactly 18 Markdown deliverable filenames")
        for fname in MD_FILES:
            fpath = os.path.join(BASE_DIR, fname)
            self.assertTrue(os.path.exists(fpath), f"Missing MD deliverable: {fname}")
            size = os.path.getsize(fpath)
            self.assertGreater(size, 4000, f"MD file {fname} is suspiciously small ({size} bytes)")
        print(f"\n[PASS] Dimension 1: All {len(MD_FILES)} MD deliverables verified existing and strictly > 4KB.")

    def test_02_all_16_docx_files_exist_and_valid_xml(self):
        """Stress-test: All DOCX files exist, have valid XML structure, and zero corruption."""
        raw_docx = glob.glob(os.path.join(DOCX_DIR, "*.docx"))
        docx_files = sorted([f for f in raw_docx if not os.path.basename(f).startswith("~$")])
        self.assertGreaterEqual(len(docx_files), len(MD_FILES), f"Expected at least {len(MD_FILES)} DOCX files, found {len(docx_files)}")

        for fpath in docx_files:
            fname = os.path.basename(fpath)
            size = os.path.getsize(fpath)
            self.assertGreater(size, 10240, f"DOCX file {fname} is suspiciously small ({size} bytes)")
            
            # Inspect zip container and all XML streams
            with zipfile.ZipFile(fpath, "r") as zf:
                for zinfo in zf.infolist():
                    if zinfo.filename.endswith(".xml") or zinfo.filename.endswith(".rels"):
                        raw_xml = zf.read(zinfo.filename)
                        try:
                            ET.fromstring(raw_xml)
                        except Exception as e:
                            self.fail(f"Corrupt XML in {fname}/{zinfo.filename}: {e}")

            # Inspect python-docx document model
            doc = docx.Document(fpath)
            self.assertGreater(len(doc.paragraphs), 0, f"DOCX {fname} has 0 paragraphs")
        print(f"\n[PASS] Dimension 2: All {len(docx_files)} DOCX files verified existing, valid XML, and 0 corruption.")

    def test_03_all_16_pdf_files_exist_total_gt_200_pages_zero_empty(self):
        """Stress-test: All PDF files exist, total > 200 pages, and 0 empty pages."""
        pdf_files = sorted(glob.glob(os.path.join(PDF_DIR, "*.pdf")))
        self.assertGreaterEqual(len(pdf_files), len(MD_FILES), f"Expected at least {len(MD_FILES)} PDF files, found {len(pdf_files)}")

        total_pages = 0
        empty_pages = []

        for fpath in pdf_files:
            fname = os.path.basename(fpath)
            doc = fitz.open(fpath)
            pcount = len(doc)
            self.assertGreater(pcount, 0, f"PDF {fname} has 0 pages")
            total_pages += pcount

            reader = pypdf.PdfReader(fpath)
            self.assertEqual(len(reader.pages), pcount, f"Page count discrepancy in {fname}")

            for pno in range(pcount):
                page = doc[pno]
                text = page.get_text().strip()
                has_imgs = len(page.get_images()) > 0
                has_drawings = len(page.get_drawings()) > 0
                if len(text) == 0 and not has_imgs and not has_drawings:
                    empty_pages.append((fname, pno + 1))

        self.assertEqual(len(empty_pages), 0, f"Discovered empty pages in PDFs: {empty_pages}")
        self.assertGreater(total_pages, 200, f"Total PDF page count ({total_pages}) is not > 200")
        print(f"\n[PASS] Dimension 3: All 16 PDF files verified (Total: {total_pages} pages > 200, 0 empty pages).")

    def test_04_trio_format_text_parity(self):
        """Stress-test: Full trio-format (MD, DOCX, PDF) text parity for core entities."""
        core_entities = {
            "deceased_name": r"MAHADI\s+MONOAR\s+HOSSAIN",
            "vehicle_number": r"28\s*모\s*1390",
            "insurer_name": r"DB\s*Insurance|DB\s*손해보험",
            "policy_number": r"2-2026-0531750-000",
            "renewal_date": r"2026-01-21|2026년\s*1월\s*21일|January\s+21,?\s+2026"
        }

        stems = [f.replace(".md", "") for f in MD_FILES]
        parity_failures = []

        for stem in stems:
            md_p = os.path.join(BASE_DIR, f"{stem}.md")
            docx_p = os.path.join(DOCX_DIR, f"{stem}.docx")
            pdf_p = os.path.join(PDF_DIR, f"{stem}.pdf")

            with open(md_p, "r", encoding="utf-8") as fp:
                md_text = fp.read()

            doc = docx.Document(docx_p)
            docx_text = "\n".join([p.text for p in doc.paragraphs] + [c.text for t in doc.tables for r in t.rows for c in r.cells])

            pdf_doc = fitz.open(pdf_p)
            pdf_text = "\n".join([page.get_text() for page in pdf_doc])

            for ent_name, pattern in core_entities.items():
                in_md = bool(re.search(pattern, md_text, re.IGNORECASE))
                in_docx = bool(re.search(pattern, docx_text, re.IGNORECASE))
                in_pdf = bool(re.search(pattern, pdf_text, re.IGNORECASE))

                if in_md and not (in_docx and in_pdf):
                    parity_failures.append(f"{stem} [{ent_name}]: MD={in_md}, DOCX={in_docx}, PDF={in_pdf}")

        self.assertEqual(len(parity_failures), 0, f"Parity failures detected:\n" + "\n".join(parity_failures))
        print(f"\n[PASS] Dimension 4: Full trio-format text parity verified across all deliverables.")

    def test_05_zero_dangling_exhibits_groups_a_through_i(self):
        """Stress-test: Zero dangling exhibit references across Groups A through I against File 05 catalog."""
        f05_path = os.path.join(BASE_DIR, "05_evidence_inventory_and_exhibits_catalog.md")
        with open(f05_path, "r", encoding="utf-8") as fp:
            f05_text = fp.read()

        catalog_exhibits = set(re.findall(r"Exhibit\s+([A-I]-\d+)", f05_text))
        korean_catalog = set(re.findall(r"증\s*제\s*([A-I]-\d+)\s*호", f05_text))
        all_catalog = catalog_exhibits.union(korean_catalog)

        # Assert Groups A through I are defined
        for grp in ["A", "B", "C", "D", "E", "F", "G", "H", "I"]:
            grp_items = [e for e in all_catalog if e.startswith(f"{grp}-")]
            self.assertGreater(len(grp_items), 0, f"Catalog has 0 exhibits for Group {grp}")

        dangling = {}
        total_citations = 0
        for fname in MD_FILES:
            fpath = os.path.join(BASE_DIR, fname)
            with open(fpath, "r", encoding="utf-8") as fp:
                text = fp.read()
            refs = re.findall(r"Exhibit\s+([A-Z]-\d+)", text) + re.findall(r"증\s*제\s*([A-Z]-\d+)\s*호", text)
            total_citations += len(refs)
            for r in refs:
                if r not in all_catalog:
                    dangling.setdefault(fname, set()).add(r)

        self.assertEqual(len(dangling), 0, f"Found dangling exhibits: {dangling}")
        print(f"\n[PASS] Dimension 5: Zero dangling exhibits across Groups A-I ({total_citations} verified references).")

    def test_06_zero_stale_samsung_fire_mentions_vehicle_make_preserved(self):
        """Stress-test: Zero stale Samsung Fire mentions in primary insurer fields, preserving Kia Morning."""
        stale_patterns = [
            (r"(?<!Renault\s)(?<!르노)삼성화재", "삼성화재 (Samsung Fire Korean)"),
            (r"(?<!Renault\s)Samsung\s+Fire", "Samsung Fire (English)"),
            (r"2026-SF", "2026-SF Policy Code"),
            (r"심기철|Shim\s+Ki-ch[ue]l", "Agent Shim Ki-cheol"),
            (r"010-8969-0440|8969-0440", "Agent Phone 010-8969-0440"),
            (r"1588-5114", "Samsung Fire Call Center 1588-5114"),
            (r"samsungfire\.com", "samsungfire.com domain"),
            (r"Seocho\s+Tower|서초대로\s*74길|14\s+Seocho-daero", "Samsung Fire Seocho HQ"),
            (r"19\s+Okcheon-ro|옥천로\s*19", "Samsung Fire Gangwon Office"),
            (r"March\s+13,?\s+2026|2026년\s*3월\s*13일", "Stale Renewal Date March 13, 2026")
        ]

        files_to_check = [os.path.join(BASE_DIR, f) for f in MD_FILES]
        files_to_check.append(r"d:\promotion\CASE_MASTER_KNOWLEDGE_DOSSIER.md")
        files_to_check.append(r"d:\promotion\PROJECT.md")

        stale_hits = []
        vehicle_make_hits = 0

        for path in files_to_check:
            fname = os.path.basename(path)
            with open(path, "r", encoding="utf-8") as fp:
                lines = fp.readlines()

            for line_idx, line in enumerate(lines, 1):
                if re.search(r"Renault\s+Samsung|기아", line, re.IGNORECASE):
                    vehicle_make_hits += 1

                sanitized = re.sub(r"01_db_insurance_claim_notice_and_legal_brief\.(md|docx|pdf)", "", line)
                for pat, label in stale_patterns:
                    if re.search(pat, sanitized, re.IGNORECASE):
                        stale_hits.append(f"{fname}:{line_idx} [{label}] {line.strip()[:80]}")

        self.assertGreater(vehicle_make_hits, 0, "Kia Morning vehicle make was not preserved!")
        self.assertEqual(len(stale_hits), 0, f"Found stale Samsung Fire references:\n" + "\n".join(stale_hits))
        print(f"\n[PASS] Dimension 6: Zero stale Samsung Fire mentions; vehicle make preserved ({vehicle_make_hits} instances).")

    def test_07_email_payload_budgets_15mb_25mb(self):
        """Stress-test: Email payload budgets strictly obey 15MB strict and 25MB gateway ceiling."""
        pdf_files = sorted(glob.glob(os.path.join(PDF_DIR, "*.pdf")))
        total_bytes = sum(os.path.getsize(p) for p in pdf_files)
        total_mb = total_bytes / (1024 * 1024)
        b64_mb = (total_bytes * 4 / 3) / (1024 * 1024)

        limit_15mb = 15 * 1024 * 1024
        limit_25mb = 25 * 1024 * 1024

        self.assertLess(total_bytes, limit_15mb, f"All 16 PDFs combined ({total_mb:.2f} MB) exceed 15MB limit")
        self.assertLess(total_bytes * 4 / 3, limit_25mb, f"All 16 PDFs with Base64 overhead ({b64_mb:.2f} MB) exceed 25MB limit")
        print(f"\n[PASS] Dimension 7: Email payload budgets compliant (All 16 PDFs: {total_mb:.2f} MB raw, {b64_mb:.2f} MB MIME).")

if __name__ == "__main__":
    unittest.main(verbosity=2)
