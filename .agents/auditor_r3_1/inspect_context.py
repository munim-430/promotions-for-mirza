import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

def show_context(filepath, line_nums):
    fname = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"\n==================== {fname} ====================")
    for lno in line_nums:
        start = max(0, lno - 5)
        end = min(len(lines), lno + 5)
        print(f"--- Around Line {lno} ---")
        for i in range(start, end):
            prefix = ">>>" if i + 1 == lno else "   "
            print(f"{prefix} {i+1:4d}: {lines[i].rstrip()}")

show_context(r"d:/promotion/legal_claim_package/03_seojeong_university_group_insurance_claim.md", [628, 630])
show_context(r"d:/promotion/legal_claim_package/07_legal_aid_and_consular_escalation_roster.md", [319, 392, 700])
show_context(r"d:/promotion/legal_claim_package/10_parallel_pro_bono_and_consular_intake_packets.md", [395, 409, 413, 434, 713, 958])
show_context(r"d:/promotion/legal_claim_package/11_dhaka_to_seoul_dhl_dispatch_and_10day_tracking_guide.md", [146, 162, 193, 238, 951])
