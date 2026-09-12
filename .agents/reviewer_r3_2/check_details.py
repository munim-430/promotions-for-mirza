import sys, os
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'd:/promotion/legal_claim_package'

# Let us verify the exact parameters across all 13 documents:
# 1. Deceased ARC: 010530-7660021
# 2. Deceased Passport: A03097931
# 3. Vehicle Plate: 28모1390
# 4. Father: BELAL HOSSAIN (NID: 19741913345000128)
# 5. Mother: MONOARA BEGUM (NID: 19801913345000129)
# 6. Precedents: 98다48963
# 7. Commercial Code: 732조의2, 739, 663, 54
# 8. SWIFT: IBBLBDDHXXX / BSONBDDHXXX

md_files = sorted([f for f in os.listdir(base_dir) if f.endswith('.md')])

for f in md_files:
    text = open(os.path.join(base_dir, f), 'r', encoding='utf-8').read()
    arc = '010530-7660021' in text
    ppt = 'A03097931' in text
    veh = '28모1390' in text
    fnid = '19741913345000128' in text
    mnid = '19801913345000129' in text
    p98 = ('98다48963' in text) or ('98Da48963' in text)
    swift = ('IBBL' in text) or ('IBBLBDDHXXX' in text)
    print(f'{f:<55} | ARC:{arc!s:<5} | PPT:{ppt!s:<5} | Veh:{veh!s:<5} | FNID:{fnid!s:<5} | MNID:{mnid!s:<5} | 98Da:{p98!s:<5} | SWIFT:{swift!s:<5}')
