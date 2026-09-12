import os
import sys
import re
import glob
import fitz # PyMuPDF
import docx

sys.stdout.reconfigure(encoding='utf-8')

PACKAGE_DIR = r"d:/promotion/legal_claim_package"
MD_FILES = sorted(glob.glob(os.path.join(PACKAGE_DIR, "*.md")))
DOCX_DIR = os.path.join(PACKAGE_DIR, "docx")
PDF_DIR = os.path.join(PACKAGE_DIR, "pdf")

print("=== CHECK 1: FILE INVENTORY & SYMMETRY ===")
md_basenames = [os.path.splitext(os.path.basename(f))[0] for f in MD_FILES]
print(f"Total Markdown files: {len(md_basenames)}")

docx_files = glob.glob(os.path.join(DOCX_DIR, "*.docx"))
docx_basenames = [os.path.splitext(os.path.basename(f))[0] for f in docx_files]
print(f"Total DOCX files: {len(docx_basenames)}")

pdf_files = glob.glob(os.path.join(PDF_DIR, "*.pdf"))
pdf_basenames = [os.path.splitext(os.path.basename(f))[0] for f in pdf_files]
print(f"Total PDF files: {len(pdf_basenames)}")

missing_docx = set(md_basenames) - set(docx_basenames)
missing_pdf = set(md_basenames) - set(pdf_basenames)

print(f"Missing DOCX: {missing_docx}")
print(f"Missing PDF: {missing_pdf}")

print("\n=== CHECK 2: MANDATORY ENTITY & FACT AUDIT ===")

required_entities = {
    "Deceased Name": [r"MAHADI MONOAR HOSSAIN", r"마하디 모노아르"],
    "Deceased ID/ARC": [r"010530-7660021"],
    "Policy / Vehicle": [r"28모1390"],
    "Insurance Agent": [r"심기철", r"Shim Ki-cheol", r"010-8969-0440"],
    "Father": [r"BELAL HOSSAIN", r"벨랄 호센", r"벨랄 호사인"],
    "Mother": [r"MONOARA BEGUM", r"모노아라 베검", r"모노아라 베굼"],
    "Attorney-in-Fact": [r"Md Monirul Islam", r"모니룰 이슬람", r"Monirul Islam"],
    "Consular Officer": [r"Mikon Tangchanggya", r"미콘 탕창갸"],
    "University": [r"서정대학교", r"Seojeong University"],
    "KLAC": [r"대한법률구조공단", r"Korea Legal Aid Corporation", r"KLAC"],
    "Gong-Gam": [r"공익인권법재단 공감", r"공감", r"Gong-Gam"],
    "DURO": [r"사단법인 두루", r"두루", r"DURO"],
    "FSS": [r"금융감독원", r"Financial Supervisory Service", r"FSS"],
}

matrix = {}
for mf in MD_FILES:
    bname = os.path.basename(mf)
    with open(mf, "r", encoding="utf-8") as f:
        text = f.read()
    
    matrix[bname] = {}
    for ent, patterns in required_entities.items():
        found = any(re.search(p, text, re.IGNORECASE) for p in patterns)
        matrix[bname][ent] = found

# Print entity matrix
print(f"{'Document':<45} | " + " | ".join([f"{k[:6]}" for k in required_entities.keys()]))
print("-" * 120)
for bname, results in matrix.items():
    row = [f"{'YES' if v else ' . '}" for v in results.values()]
    print(f"{bname:<45} | " + " | ".join([f"{r:^6}" for r in row]))

print("\n=== CHECK 3: STATUTORY & PRECEDENT CITATION AUDIT ===")
precedents = {
    "98Da48963 (En Banc)": [r"98다48963", r"98Da48963"],
    "97Da27039": [r"97다27039", r"97Da27039"],
    "98Da26910": [r"98다26910", r"98Da26910"],
    "2003Da29463": [r"2003다29463", r"2003Da29463"],
    "Comm. Code Art. 663": [r"663조", r"Art\.? 663", r"제663조"],
    "Comm. Code Art. 732-2": [r"732조의2", r"Art\.? 732-2", r"제732조의2"],
    "Comm. Code Art. 739": [r"739조", r"Art\.? 739", r"제739조"],
    "Legal Aid Act Art. 22": [r"법률구조법 제22조", r"Legal Aid Act Art\.? 22", r"제22조"],
}

prec_matrix = {}
for mf in MD_FILES:
    bname = os.path.basename(mf)
    with open(mf, "r", encoding="utf-8") as f:
        text = f.read()
    prec_matrix[bname] = {}
    for p_name, patterns in precedents.items():
        found = any(re.search(p, text, re.IGNORECASE) for p in patterns)
        prec_matrix[bname][p_name] = found

print(f"{'Document':<45} | " + " | ".join([f"{k[:7]}" for k in precedents.keys()]))
print("-" * 120)
for bname, results in prec_matrix.items():
    row = [f"{'YES' if v else ' . '}" for v in results.values()]
    print(f"{bname:<45} | " + " | ".join([f"{r:^7}" for r in row]))

