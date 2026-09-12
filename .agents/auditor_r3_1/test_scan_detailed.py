import os
import re
import sys
import glob
import json

sys.stdout.reconfigure(encoding='utf-8')

PACKAGE_DIR = r"d:/promotion/legal_claim_package"
MD_FILES = sorted(glob.glob(os.path.join(PACKAGE_DIR, "*.md")))

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

all_findings = {}

for filepath in MD_FILES:
    fname = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as fp:
        content = fp.read()
    
    lines = content.splitlines()
    file_findings = []
    
    for pat, label in suspicious_patterns:
        for m in re.finditer(pat, content, re.IGNORECASE):
            lno = content[:m.start()].count("\n") + 1
            line = lines[lno - 1]
            file_findings.append({
                "label": label,
                "line_no": lno,
                "match": m.group(0),
                "line": line.strip()
            })
    
    all_findings[fname] = file_findings

print("SUMMARY OF PLACEHOLDER SCAN:")
for fname, findings in all_findings.items():
    print(f"{fname}: {len(findings)} matches")
    for f in findings:
        print(f"  Line {f['line_no']} [{f['label']}]: '{f['match']}' -> {f['line']}")

with open(r"d:/promotion/.agents/auditor_r3_1/findings_raw.json", "w", encoding="utf-8") as fp:
    json.dump(all_findings, fp, indent=2, ensure_ascii=False)
