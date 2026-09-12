import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:/promotion/legal_claim_package/04_bilingual_special_power_of_attorney.md", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.splitlines()
for i, l in enumerate(lines[:100]):
    print(f"{i+1:3d}: {l}")
