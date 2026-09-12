# -*- coding: utf-8 -*-
import base64

spa_path = 'd:/promotion/legal_claim_package/04_bilingual_special_power_of_attorney.md'

with open(spa_path, 'w', encoding='utf-8') as f:
    f.write('')

def write_b64(b64_str):
    decoded = base64.b64decode(b64_str.encode('ascii')).decode('utf-8')
    with open(spa_path, 'a', encoding='utf-8') as f:
        f.write(decoded)
