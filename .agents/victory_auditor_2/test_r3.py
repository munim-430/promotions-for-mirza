import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

pkg_dir = 'd:/promotion/legal_claim_package'
f08_path = os.path.join(pkg_dir, '08_attorney_in_fact_execution_checklist.md')
with open(f08_path, 'r', encoding='utf-8') as fh:
    f08 = fh.read()

m1 = re.search(r'Notary Public.*Ministry of Law.*MOFA', f08, re.DOTALL | re.IGNORECASE)
print(f"Check 1 (DOTALL): {'PASS' if m1 else 'FAIL'}")

m2 = re.search(r'D\+1.*D\+10.*D\+11.*D\+15.*D\+31', f08, re.DOTALL)
print(f"Check 2 (DOTALL): {'PASS' if m2 else 'FAIL'}")
