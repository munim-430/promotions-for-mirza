import os
import re
import glob
import fitz # PyMuPDF
import docx

PACKAGE_DIR = r"d:/promotion/legal_claim_package"
MD_FILES = sorted(glob.glob(os.path.join(PACKAGE_DIR, "*.md")))

print(f"Found {len(MD_FILES)} markdown files:")
for f in MD_FILES:
    print(" -", os.path.basename(f), f"({os.path.getsize(f):,} bytes)")

print("\n--- CHECK 1: SCANNING MARKDOWN FOR SUSPICIOUS PLACEHOLDERS ---")
suspicious_patterns = [
    (r"\[TODO.*?\]", "TODO placeholder"),
    (r"\[TBD.*?\]", "TBD placeholder"),
    (r"\[Insert.*?\]", "Insert placeholder"),
    (r"\[Fill.*?\]", "Fill placeholder"),
    (r"\[Your Name.*?\]", "Your Name placeholder"),
    (r"\[Date\]", "Date placeholder"),
    (r"Lorem ipsum", "Lorem ipsum dummy text"),
    (r"PLACEHOLDER", "PLACEHOLDER string"),
    (r"__+", "Underscore blanks (_____)"),
    (r"\[\s*\]", "Empty brackets []"),
    (r"\bXXX+\b", "XXX dummy placeholder"),
]

for filepath in MD_FILES:
    fname = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as fp:
        content = fp.read()
    
    findings = []
    for pat, label in suspicious_patterns:
        matches = re.finditer(pat, content, re.IGNORECASE)
        for m in matches:
            # find line number
            line_no = content[:m.start()].count("\n") + 1
            line = content.splitlines()[line_no - 1]
            findings.append((label, line_no, m.group(0), line.strip()))
    
    if findings:
        print(f"\n[FLAG] {fname}: {len(findings)} potential placeholder(s) found:")
        for label, lno, match_text, line_text in findings:
            print(f"  Line {lno} ({label}): '{match_text}' in: {line_text[:100]}")
    else:
        print(f"[OK] {fname}: No suspicious placeholders found.")

print("\n--- CHECK 2: STATUTORY AND PRECEDENT CITATIONS ---")
statutes = [
    "732-2", "732조의2",
    "739", "739조",
    "663", "663조",
    "98다48963", "98Da48963",
    "97다27039", "97Da27039",
    "98다26910", "98Da26910",
    "2003다29463", "2003Da29463",
    "법률구조법 제22조", "Legal Aid Act Art. 22", "Legal Aid Act",
]

for filepath in MD_FILES:
    fname = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as fp:
        content = fp.read()
    found = [s for s in statutes if s in content]
    print(f"{fname}: Found {len(found)} legal references -> {', '.join(found[:5])}...")

