import os
import re
import sys
import glob

sys.stdout.reconfigure(encoding='utf-8')

PACKAGE_DIR = r"d:/promotion/legal_claim_package"
MD_FILES = sorted(glob.glob(os.path.join(PACKAGE_DIR, "*.md")))

print("=== SCANNING FOR ALL SQUARE BRACKETS [...] ACROSS ALL 13 MD FILES ===")

for mf in MD_FILES:
    fname = os.path.basename(mf)
    with open(mf, "r", encoding="utf-8") as f:
        content = f.read()
    
    # find bracketed tokens that might be placeholders
    # exclude standard markdown links [text](url) and markdown checkboxes [ ] or [x]
    lines = content.splitlines()
    bracket_tokens = []
    
    for lno, line in enumerate(lines, 1):
        # find [something]
        matches = re.findall(r'\[([^\]]+)\]', line)
        for m in matches:
            # ignore markdown links like [title](path)
            if f"[{m}](" in line:
                continue
            # ignore markdown checkboxes
            if m.strip() in ("", " ", "x", "X"):
                continue
            # ignore section tags like [Korean - 전문], [English], [FACTUAL BACKGROUND], etc.
            # let's see what is inside
            bracket_tokens.append((lno, m, line.strip()))
            
    print(f"\n--- {fname} (Total bracket tokens: {len(bracket_tokens)}) ---")
    suspicious = []
    for lno, tok, ltext in bracket_tokens:
        tok_lower = tok.lower()
        if any(k in tok_lower for k in ["passport number", "designated", "appointed", "office address", "telephone", "email address", "insert", "fill", "todo", "tbd", "your name", "date", "representative resident"]):
            suspicious.append((lno, tok, ltext))
            print(f"  SUSPICIOUS Line {lno}: [{tok}] -> {ltext}")
    if not suspicious:
        print("  No suspicious bracket placeholders.")
