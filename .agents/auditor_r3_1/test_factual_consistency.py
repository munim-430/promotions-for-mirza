import os
import re
import sys
import glob

sys.stdout.reconfigure(encoding='utf-8')

PACKAGE_DIR = r"d:/promotion/legal_claim_package"
MD_FILES = sorted(glob.glob(os.path.join(PACKAGE_DIR, "*.md")))

facts_to_check = {
    "Deceased Name": ["MAHADI MONOAR HOSSAIN", "MONOAR HOSSAIN MAHADI"],
    "Deceased ARC": ["010530-7660021"],
    "Date of Accident/Death": ["March 14, 2026", "2026. 3. 14", "2026년 3월 14일"],
    "Policy Vehicle": ["28모1390"],
    "Policy Renewal Date": ["March 13, 2026", "2026. 3. 13", "2026년 3월 13일"],
    "Insurance Agent Name": ["심기철", "Shim Ki-cheol"],
    "Insurance Agent Phone": ["010-8969-0440"],
    "Father Name": ["BELAL HOSSAIN", "벨랄"],
    "Mother Name": ["MONOARA BEGUM", "모노아라"],
    "Father Share": ["2/3", "66.667%", "66,666,667", "6,666만"],
    "Mother Share": ["1/3", "33.333%", "33,333,333", "3,333만"],
    "Attorney-in-Fact": ["Md Monirul Islam", "모니룰 이슬람"],
    "Bangladesh Counsellor": ["Mikon Tangchanggya", "미콘 탕창갸"],
    "University": ["서정대학교", "Seojeong University"],
    "Samsung Benefit Amount": ["100,000,000", "1억 원", "100M", "100 Million"],
    "Samsung Provisional (50%)": ["50,000,000", "5,000만", "50M", "50 Million"],
    "Seojeong Benefit Amount": ["30,000,000", "3,000만", "50,000,000", "5,000만", "20,000,000", "2,000만"],
}

print("=== DETAILED FACTUAL CONSISTENCY CHECK ===")
for fname in [os.path.basename(f) for f in MD_FILES]:
    fpath = os.path.join(PACKAGE_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        text = f.read()
    
    print(f"\n--- {fname} ---")
    for fact_key, patterns in facts_to_check.items():
        found = any(re.search(re.escape(p), text, re.IGNORECASE) for p in patterns)
        # also print match count
        count = sum(len(re.findall(re.escape(p), text, re.IGNORECASE)) for p in patterns)
        if count > 0:
            print(f"  [OK] {fact_key:<25}: {count:3d} matches")
        else:
            print(f"  [--] {fact_key:<25}: not referenced in this file")
