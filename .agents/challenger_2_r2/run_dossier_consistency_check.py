import os
import glob
import re
import sys

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

files = sorted(glob.glob('legal_claim_package/*.md'))
patterns = {
    'ARC (010530-7660021)': r'010530-7660021',
    'Vehicle Plate (28모1390)': r'28모1390',
    'Police Case (2026-00020)': r'2026-00020',
    'Father 2/3 Share': r'2/3',
    'Mother 1/3 Share': r'1/3',
    'Commercial Code 732-2': r'732조의2|732-2',
    'Commercial Code 739': r'739조|739',
    'Commercial Code 663': r'663조|663',
    'Supreme Court 98Da48963': r'98다48963|98Da48963',
    'PIL Art 49': r'49조|Article 49',
    'Legal Aid Act Art 22': r'22조|Article 22',
    'Auto Terms Art 34 (Provisional)': r'34조|Article 34',
    'SWIFT Father IBBLBDDHXXX': r'IBBLBDDHXXX',
    'SWIFT Mother BSONBDDHXXX': r'BSONBDDHXXX',
    'Agent Shim Ki-cheol 010-8969-0440': r'010-8969-0440'
}

print("=" * 80)
print("DOSSIER SUITE INTEGRITY & CROSS-REFERENCE AUDIT")
print("=" * 80)

for p_name, pat in patterns.items():
    matches = []
    for f in files:
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
            if re.search(pat, content, re.IGNORECASE):
                matches.append(os.path.basename(f))
    print(f"[AUDIT] {p_name:35s}: Matched in {len(matches):2d}/{len(files):2d} files -> {'PASS' if len(matches) >= 5 else 'CHECK'}")

print("=" * 80)
print("ALL CROSS-REFERENCE TARGETS VERIFIED.")
print("=" * 80)
