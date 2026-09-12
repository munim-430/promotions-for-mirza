import os
import fitz
import docx

pkg_dir = 'd:/promotion/legal_claim_package'
docx_dir = os.path.join(pkg_dir, 'docx')
pdf_dir = os.path.join(pkg_dir, 'pdf')

files_13 = [
    "00_master_dossier_index_and_executive_summary",
    "01_samsung_fire_claim_notice_and_legal_brief",
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
    "11_dhaka_to_seoul_dhl_dispatch_and_10day_tracking_guide"
]

print("=== FINAL DOSSIER VERIFICATION AUDIT ===")
all_passed = True
total_pdf_pages = 0
total_docx_size = 0
total_pdf_size = 0
total_md_size = 0

for base in files_13:
    md_p = os.path.join(pkg_dir, f"{base}.md")
    docx_p = os.path.join(docx_dir, f"{base}.docx")
    pdf_p = os.path.join(pdf_dir, f"{base}.pdf")
    
    # Check MD
    if not os.path.exists(md_p):
        print(f"[FAIL] Missing MD: {md_p}")
        all_passed = False
        continue
    md_size = os.path.getsize(md_p)
    total_md_size += md_size
    
    # Check DOCX
    if not os.path.exists(docx_p):
        print(f"[FAIL] Missing DOCX: {docx_p}")
        all_passed = False
        continue
    docx_size = os.path.getsize(docx_p)
    total_docx_size += docx_size
    doc = docx.Document(docx_p)
    p_count = len(doc.paragraphs)
    tbl_count = len(doc.tables)
    
    # Check PDF
    if not os.path.exists(pdf_p):
        print(f"[FAIL] Missing PDF: {pdf_p}")
        all_passed = False
        continue
    pdf_size = os.path.getsize(pdf_p)
    total_pdf_size += pdf_size
    pdf_doc = fitz.open(pdf_p)
    pages = len(pdf_doc)
    total_pdf_pages += pages
    pdf_doc.close()
    
    print(f"[PASS] {base:<55} | MD: {md_size:>6,} B | DOCX: {docx_size:>6,} B ({p_count} p, {tbl_count} t) | PDF: {pdf_size:>7,} B ({pages:>2} pgs)")

print("\n=== AGGREGATE METRICS ===")
print(f"Total Markdown Files: {len(files_13)} ({total_md_size:,} bytes)")
print(f"Total DOCX Files:     {len(files_13)} ({total_docx_size:,} bytes)")
print(f"Total PDF Files:      {len(files_13)} ({total_pdf_size:,} bytes, {total_pdf_pages} total printed pages)")

if all_passed:
    print("\n>>> ALL VERIFICATION CHECKS PASSED (100% SUITE COMPLETION) <<<")
else:
    print("\n>>> VERIFICATION FAILED <<<")
