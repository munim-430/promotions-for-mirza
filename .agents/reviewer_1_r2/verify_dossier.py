import os
import sys
import re
import glob

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

pkg_dir = "d:/promotion/legal_claim_package"
files = sorted(glob.glob(os.path.join(pkg_dir, "*.md")))

print(f"Total files in legal_claim_package: {len(files)}")

key_patterns = {
    "Deceased Name": r"MAHADI MONOAR HOSSAIN",
    "Alien Registration No": r"010530-7660021",
    "Passport No": r"A03097931",
    "Vehicle Plate": r"28모1390",
    "Policy Number": r"2026-SF-AUTO-28M1390",
    "Agent Shim": r"심기철|010-8969-0440",
    "Father Belal": r"BELAL HOSSAIN",
    "Mother Monoara": r"MONOARA BEGUM",
    "Father NID": r"19741913345000128",
    "Mother NID": r"19801913345000129",
    "IBBL SWIFT": r"IBBLBDDHXXX",
    "Sonali SWIFT": r"BSONBDDHXXX",
    "Comm Code 732-2": r"732조의2|732-2",
    "Comm Code 739": r"739",
    "Comm Code 663": r"663",
    "Comm Code 54": r"54조|Art\. 54|제54조",
    "Supreme Court 98Da48963": r"98다48963|98Da48963",
    "Supreme Court 97Da27039": r"97다27039|97Da27039",
    "Supreme Court 98Da26910": r"98다26910|98Da26910",
    "Supreme Court 2003Da29463": r"2003다29463|2003Da29463",
    "PIL Art 49": r"국제사법.*49|Private International Law.*49|PIL.*49",
    "Special Act Lit 3(1)": r"소송촉진|소촉|Special Act on Promotion",
    "Seojeong Univ": r"서정대학교|Seojeong University",
    "Seojeong Postal 11429": r"11429",
    "Samsung Fire Postal 06620": r"06620",
    "BD Embassy Postal 04393": r"04393",
    "KLAC": r"대한법률구조공단|KLAC|Korea Legal Aid",
    "Attorney-in-Fact": r"Md Monirul Islam|모니룰 이슬람",
}

report = []
for fpath in files:
    fname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    file_res = {"file": fname, "size": len(content), "lines": len(content.splitlines())}
    matches = {}
    for label, pat in key_patterns.items():
        found = re.findall(pat, content, re.IGNORECASE)
        matches[label] = len(found)
    file_res["matches"] = matches
    report.append(file_res)

for r in report:
    print(f"\n==========================================")
    print(f"File: {r['file']} ({r['lines']} lines, {r['size']} chars)")
    print(f"==========================================")
    for k, v in r["matches"].items():
        if v > 0:
            print(f"  [OK] {k:26}: {v:3d} matches")
        else:
            print(f"  [--] {k:26}:   0 matches")
