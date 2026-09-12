# -*- coding: utf-8 -*-
import os

files = [
    'd:/promotion/legal_claim_package/04_bilingual_special_power_of_attorney.md',
    'd:/promotion/legal_claim_package/04_cross_border_heirship_and_legalization_guide.md'
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    text = text.replace(chr(92) + 'x60', chr(96))
    text = text.replace(chr(92) + 'x22', chr(34))
    text = text.replace(chr(92) + 'x27', chr(39))
    
    lines = text.split(chr(10))
    fixed_lines = []
    for line in lines:
        s = line.strip()
        if s == chr(96) or s == chr(96)*2:
            fixed_lines.append(chr(96)*3)
        else:
            fixed_lines.append(line)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(chr(10).join(fixed_lines))

print('Cleaned files successfully')
