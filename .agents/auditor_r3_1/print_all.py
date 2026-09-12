import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:/promotion/.agents/auditor_r3_1/findings_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for fname in sorted(data.keys()):
    findings = data[fname]
    print(f"\n==========================================")
    print(f"FILE: {fname} (Total matches: {len(findings)})")
    print(f"==========================================")
    for item in findings:
        lno = item['line_no']
        lbl = item['label']
        mtc = item['match']
        txt = item['line']
        print(f"  Line {lno:4d} [{lbl:25s}] : {mtc} -> {txt[:100]}")
