# ==============================================================================
# SCRIPT: compile_all_dossier.py
# PURPOSE: Compiles all 13 Legal Claim Package Markdown files to DOCX and PDF
# ==============================================================================

import os
import re
import sys
import time
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
import win32com.client
import fitz

sys.stdout.reconfigure(encoding='utf-8')

COLOR_PRIMARY = RGBColor(0, 32, 96)       # Deep Navy
COLOR_SECONDARY = RGBColor(60, 60, 60)    # Charcoal Gray
COLOR_BODY = RGBColor(30, 30, 30)         # Off Black
COLOR_CALLOUT_BG = "F4F6F9"               # Soft Slate
COLOR_HEADER_BG = "E8ECF2"                # Light Navy Accent

def set_cell_background(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=80, bottom=80, left=100, right=100):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def create_styled_document(doc_title=""):
    doc = Document()
    for section in doc.sections:
        section.top_margin = Inches(0.7)
        section.bottom_margin = Inches(0.7)
        section.left_margin = Inches(0.7)
        section.right_margin = Inches(0.7)
        
        # Header
        header = section.header
        h_p = header.paragraphs[0]
        h_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        h_run = h_p.add_run("LEGAL RECOVERY DOSSIER | CASE: 2026-SF-AUTO-28M1390")
        h_run.font.name = "Malgun Gothic"
        h_run.font.size = Pt(8.0)
        h_run.font.color.rgb = RGBColor(140, 140, 140)
        
        # Footer
        footer = section.footer
        f_p = footer.paragraphs[0]
        f_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        f_run = f_p.add_run(f"Confidential Litigation Document — {doc_title[:45]}")
        f_run.font.name = "Malgun Gothic"
        f_run.font.size = Pt(8.0)
        f_run.font.color.rgb = RGBColor(140, 140, 140)

    style_normal = doc.styles['Normal']
    style_normal.font.name = 'Malgun Gothic'
    style_normal.font.size = Pt(9.5)
    style_normal.font.color.rgb = COLOR_BODY
    style_normal.paragraph_format.line_spacing = 1.15
    style_normal.paragraph_format.space_after = Pt(2.5)
    
    return doc

def add_formatted_runs(paragraph, text, default_font="Malgun Gothic", default_size=9.5, default_color=COLOR_BODY):
    # Process bold **text** and inline code `code`
    tokens = re.split(r'(\*\*.*?\*\*|`.*?`)', text)
    for token in tokens:
        if not token:
            continue
        if token.startswith('**') and token.endswith('**') and len(token) >= 4:
            run = paragraph.add_run(token[2:-2])
            run.font.name = default_font
            run.font.size = Pt(default_size)
            run.font.bold = True
            run.font.color.rgb = default_color
        elif token.startswith('`') and token.endswith('`') and len(token) >= 2:
            run = paragraph.add_run(token[1:-1])
            run.font.name = 'Consolas'
            run.font.size = Pt(default_size * 0.95)
            run.font.color.rgb = RGBColor(180, 0, 0)
        else:
            run = paragraph.add_run(token)
            run.font.name = default_font
            run.font.size = Pt(default_size)
            run.font.color.rgb = default_color

def parse_markdown_to_docx(md_path, output_docx_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    base_name = os.path.splitext(os.path.basename(md_path))[0]
    doc = create_styled_document(base_name)
    
    in_code_block = False
    code_buffer = []
    in_table = False
    table_buffer = []
    
    for line in lines:
        raw_line = line.rstrip('\r\n')
        
        # Code block handling
        if raw_line.startswith('```'):
            if in_code_block:
                in_code_block = False
                tbl = doc.add_table(rows=1, cols=1)
                tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
                cell = tbl.cell(0, 0)
                set_cell_background(cell, COLOR_CALLOUT_BG)
                set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
                
                cp = cell.paragraphs[0]
                cp.paragraph_format.space_after = Pt(0)
                cp.paragraph_format.line_spacing = 1.05
                crun = cp.add_run('\n'.join(code_buffer))
                crun.font.name = 'Consolas'
                crun.font.size = Pt(7.5)
                crun.font.color.rgb = RGBColor(30, 30, 30)
                
                doc.add_paragraph()
                code_buffer = []
            else:
                in_code_block = True
                code_buffer = []
            continue
            
        if in_code_block:
            code_buffer.append(raw_line)
            continue
            
        # Table handling
        if '|' in raw_line and not raw_line.startswith('#'):
            if not in_table:
                in_table = True
                table_buffer = []
            table_buffer.append(raw_line)
            continue
        else:
            if in_table:
                in_table = False
                rows_data = []
                for tline in table_buffer:
                    if re.match(r'^\s*\|?[\s\-:|]+\|?\s*$', tline):
                        continue
                    cells = [c.strip() for c in tline.strip('|').split('|')]
                    if cells:
                        rows_data.append(cells)
                
                if rows_data:
                    num_cols = max(len(r) for r in rows_data)
                    table = doc.add_table(rows=len(rows_data), cols=num_cols)
                    table.alignment = WD_TABLE_ALIGNMENT.CENTER
                    
                    for r_idx, row in enumerate(rows_data):
                        for c_idx, val in enumerate(row):
                            if c_idx < num_cols:
                                c = table.cell(r_idx, c_idx)
                                c.text = ""
                                cp = c.paragraphs[0]
                                cp.paragraph_format.space_after = Pt(1.5)
                                cp.paragraph_format.line_spacing = 1.05
                                
                                if r_idx == 0:
                                    set_cell_background(c, COLOR_HEADER_BG)
                                    add_formatted_runs(cp, val, default_font="Malgun Gothic", default_size=8.5, default_color=COLOR_PRIMARY)
                                    for run in cp.runs:
                                        run.font.bold = True
                                else:
                                    if r_idx % 2 == 1:
                                        set_cell_background(c, "FAFAFA")
                                    add_formatted_runs(cp, val, default_font="Malgun Gothic", default_size=8.0, default_color=COLOR_BODY)
                                set_cell_margins(c, top=50, bottom=50, left=70, right=70)
                    doc.add_paragraph()
                table_buffer = []
                
        if not raw_line.strip():
            continue
            
        # Headings and Paragraphs
        if raw_line.startswith('# '):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(4)
            run = p.add_run(raw_line[2:].strip())
            run.font.name = 'Malgun Gothic'
            run.font.size = Pt(14)
            run.font.bold = True
            run.font.color.rgb = COLOR_PRIMARY
        elif raw_line.startswith('## '):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(9)
            p.paragraph_format.space_after = Pt(3)
            run = p.add_run(raw_line[3:].strip())
            run.font.name = 'Malgun Gothic'
            run.font.size = Pt(11.5)
            run.font.bold = True
            run.font.color.rgb = COLOR_PRIMARY
        elif raw_line.startswith('### '):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(2)
            run = p.add_run(raw_line[4:].strip())
            run.font.name = 'Malgun Gothic'
            run.font.size = Pt(10)
            run.font.bold = True
            run.font.color.rgb = COLOR_SECONDARY
        elif raw_line.startswith('#### '):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(1.5)
            run = p.add_run(raw_line[5:].strip())
            run.font.name = 'Malgun Gothic'
            run.font.size = Pt(9.5)
            run.font.bold = True
            run.font.color.rgb = COLOR_SECONDARY
        elif raw_line.startswith('---'):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            run = p.add_run('―' * 45)
            run.font.color.rgb = RGBColor(190, 190, 190)
        elif raw_line.startswith('> '):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.25)
            p.paragraph_format.space_after = Pt(3)
            add_formatted_runs(p, raw_line[2:].strip(), default_font="Malgun Gothic", default_size=9.0, default_color=RGBColor(60, 60, 60))
            for run in p.runs:
                run.font.italic = True
        elif raw_line.startswith('- ') or raw_line.startswith('* '):
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            add_formatted_runs(p, raw_line[2:].strip())
        elif re.match(r'^\d+\.\s', raw_line):
            match = re.match(r'^(\d+\.)\s(.*)$', raw_line)
            p = doc.add_paragraph(style='List Number')
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            add_formatted_runs(p, match.group(2))
        else:
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(2.5)
            p.paragraph_format.line_spacing = 1.15
            add_formatted_runs(p, raw_line)

    doc.save(output_docx_path)
    print(f"[OK] Generated DOCX: {os.path.basename(output_docx_path)} ({os.path.getsize(output_docx_path):,} bytes)")

def convert_all_docx_to_pdf(docx_files, pdf_dir):
    os.makedirs(pdf_dir, exist_ok=True)
    word = win32com.client.Dispatch('Word.Application')
    word.Visible = False
    
    results = []
    try:
        for docx_path in docx_files:
            file_name = os.path.splitext(os.path.basename(docx_path))[0]
            pdf_path = os.path.join(pdf_dir, f"{file_name}.pdf")
            abs_docx = os.path.abspath(docx_path)
            abs_pdf = os.path.abspath(pdf_path)
            
            try:
                wb = word.Documents.Open(abs_docx)
                wb.SaveAs2(abs_pdf, FileFormat=17) # 17 = wdFormatPDF
                wb.Close(SaveChanges=False)
                
                # Verify PDF with fitz
                pdf_doc = fitz.open(abs_pdf)
                pages = len(pdf_doc)
                size = os.path.getsize(abs_pdf)
                pdf_doc.close()
                
                print(f"[OK] Exported PDF: {os.path.basename(pdf_path)} ({pages} pages, {size:,} bytes)")
                results.append((file_name, True, pages, size))
            except Exception as ex:
                print(f"[ERROR] Failed PDF export for {file_name}: {ex}")
                results.append((file_name, False, 0, 0))
    finally:
        word.Quit()
        
    return results

def main():
    pkg_dir = 'd:/promotion/legal_claim_package'
    docx_dir = os.path.join(pkg_dir, 'docx')
    pdf_dir = os.path.join(pkg_dir, 'pdf')
    
    os.makedirs(docx_dir, exist_ok=True)
    os.makedirs(pdf_dir, exist_ok=True)
    
    # Remove any temp lock files
    for root, dirs, files in os.walk(docx_dir):
        for f in files:
            if f.startswith('~$'):
                try:
                    os.remove(os.path.join(root, f))
                except Exception:
                    pass

    md_files = [
        "00_master_dossier_index_and_executive_summary.md",
        "01_samsung_fire_claim_notice_and_legal_brief.md",
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
        "12_lawyer_and_insurer_filing_email_transmittals.md"
    ]
    
    generated_docx = []
    print(f"=== Compiling {len(md_files)} Markdown Files to DOCX ===")
    for mf in md_files:
        in_path = os.path.join(pkg_dir, mf)
        out_base = os.path.splitext(mf)[0] + ".docx"
        out_path = os.path.join(docx_dir, out_base)
        parse_markdown_to_docx(in_path, out_path)
        generated_docx.append(out_path)

    # Also create the friendly named copy for the user: Lawyer_and_Insurer_Filing_Emails.docx
    friendly_docx = os.path.join(docx_dir, "Lawyer_and_Insurer_Filing_Emails.docx")
    parse_markdown_to_docx(os.path.join(pkg_dir, "12_lawyer_and_insurer_filing_email_transmittals.md"), friendly_docx)
    generated_docx.append(friendly_docx)
        
    print(f"\n=== Converting {len(generated_docx)} DOCX Files to PDF via Word COM ===")
    pdf_results = convert_all_docx_to_pdf(generated_docx, pdf_dir)
    
    print("\n=== COMPILATION & VERIFICATION SUMMARY ===")
    all_success = True
    for fname, success, pages, size in pdf_results:
        status = "PASSED" if (success and pages > 0 and size > 1000) else "FAILED"
        if status == "FAILED":
            all_success = False
        print(f"  {fname:<65} | Pages: {pages:>3} | Size: {size:>9,} B | {status}")
        
    if all_success:
        print("\n>>> ALL 13 DELIVERABLES COMPILED & VERIFIED PERFECTLY! <<<")
    else:
        print("\n>>> SOME FILES FAILED COMPILATION OR VERIFICATION! <<<")

if __name__ == '__main__':
    main()
