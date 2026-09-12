import json

with open(r'd:/promotion/.agents/auditor_r3_1/findings_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for fname in ["00_master_dossier_index_and_executive_summary.md",
              "01_samsung_fire_claim_notice_and_legal_brief.md",
              "02_fss_dispute_mediation_petition.md",
              "03_seojeong_university_group_insurance_claim.md",
              "04_bilingual_special_power_of_attorney.md",
              "04_cross_border_heirship_and_legalization_guide.md",
              "05_evidence_inventory_and_exhibits_catalog.md",
              "06_direct_filing_dispatch_package.md",
              "07_legal_aid_and_consular_escalation_roster.md"]:
    findings = data.get(fname, [])
    print(f"\n==========================================")
    print(f"FILE: {fname} (Total matches: {len(findings)})")
    print(f"==========================================")
    for item in findings:
        lno = item['line_no']
        lbl = item['label']
        mtc = item['match']
        txt = item['line']
        print(f"  Line {lno:4d} [{lbl:25s}] : {mtc} -> {txt}")
