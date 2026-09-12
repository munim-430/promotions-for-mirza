import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'd:/promotion/legal_claim_package'

# Key entities to check across all documents:
entities = {
    'Insured Name': ['MAHADI MONOAR HOSSAIN', 'MONOAR HOSSAIN MAHADI', '마하디 모노아르 후세인'],
    'ARC': ['010530-7660021'],
    'Passport': ['A03097931'],
    'Vehicle Plate': ['28모1390'],
    'Policy No': ['2026-SF-AUTO-28M1390'],
    'Agent': ['심기철', '010-8969-0440'],
    'Accident Date': ['2026-03-14', '05:58'],
    'Accident Location': ['북분리 4-1', 'Bukbun-ri 4-1', '현남면', 'Hyeonnam-myeon', '양양군', 'Yangyang'],
    'Father': ['BELAL HOSSAIN', '벨랄 후세인', '19741913345000128'],
    'Mother': ['MONOARA BEGUM', '모노아라 베검', '19801913345000129'],
    'Father Share': ['2/3', '66.667', '66,666,667'],
    'Mother Share': ['1/3', '33.333', '33,333,333'],
    'Principal Death Benefit': ['100,000,000', '1억원', '100M'],
    'Provisional Benefit': ['50,000,000', '5천만원', '50M'],
    'Supreme Court Precedents': ['98다48963', '98Da48963', '97다27039', '97Da27039', '98다26910', '98Da26910'],
    'Commercial Code Arts': ['732조의2', '732-2', '739', '663', '54'],
    'Attorney-in-Fact': ['Md Monirul Islam', '몬지룰 이슬람', '주한 방글라데시 인권위원회', 'Korea Bangladesh Human Rights'],
}

md_files = sorted([f for f in os.listdir(base_dir) if f.endswith('.md')])

print('CROSS REFERENCE VERIFICATION MATRIX')
print('=' * 80)
for md_file in md_files:
    path = os.path.join(base_dir, md_file)
    content = open(path, 'r', encoding='utf-8').read()
    print(f'File: {md_file} ({len(content)} chars)')
    found_summary = {}
    for cat, terms in entities.items():
        found = any(term in content for term in terms)
        found_summary[cat] = found
    
    missing = [cat for cat, found in found_summary.items() if not found]
    if missing:
        print(f'  [INFO] Categories not mentioned in this file: {missing}')
    else:
        print('  [PASS] All core entity categories referenced!')
print('=' * 80)
