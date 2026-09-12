import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

PACKAGE_DIR = r"d:/promotion/legal_claim_package"

def verify_legal_text(fname, keywords):
    fpath = os.path.join(PACKAGE_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        text = f.read()
    print(f"\n==========================================")
    print(f"VERIFYING LEGAL DOCTRINE IN: {fname}")
    print(f"==========================================")
    for kw in keywords:
        matches = [m.start() for m in re.finditer(re.escape(kw), text, re.IGNORECASE)]
        print(f" - Keyword '{kw}': {len(matches)} occurrence(s)")
        if matches:
            idx = matches[0]
            start = max(0, idx - 150)
            end = min(len(text), idx + 250)
            snippet = text[start:end].replace("\n", " ")
            print(f"   Snippet: ...{snippet}...")

verify_legal_text("01_samsung_fire_claim_notice_and_legal_brief.md", [
    "98다48963",
    "97다27039",
    "98다26910",
    "732조의2",
    "663조",
    "739조",
    "가지급금",
    "무면허"
])

verify_legal_text("02_fss_dispute_mediation_petition.md", [
    "98다48963",
    "금융소비자 보호에 관한 법률",
    "분쟁조정",
    "732조의2"
])

verify_legal_text("09_direct_international_claim_and_10day_statutory_notice.md", [
    "98다48963",
    "732-2",
    "가지급금",
    "50,000,000"
])

verify_legal_text("10_parallel_pro_bono_and_consular_intake_packets.md", [
    "법률구조법 제22조",
    "98다48963",
    "공감",
    "두루",
    "Mikon Tangchanggya"
])
