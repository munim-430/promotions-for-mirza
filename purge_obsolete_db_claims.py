# -*- coding: utf-8 -*-
"""
Deep Cleanup Script: Purge Obsolete DB 100M/50M Claims and Align Dossier Exclusively to Seojeong University
"""

import os, sys, shutil, glob

sys.stdout.reconfigure(encoding='utf-8')

# 1. Remove obsolete 00_DB_50M_KRW_FIRST_PAYOUT_BANGLADESH_DIRECT_FILING_PACK
db_pack_dir = r"d:\promotion\00_DB_50M_KRW_FIRST_PAYOUT_BANGLADESH_DIRECT_FILING_PACK"
if os.path.exists(db_pack_dir):
    shutil.rmtree(db_pack_dir)
    print(f"Removed obsolete directory: {db_pack_dir}")

# 2. Update CASE_MASTER_KNOWLEDGE_DOSSIER.md
dossier_path = r"d:\promotion\CASE_MASTER_KNOWLEDGE_DOSSIER.md"
with open(dossier_path, 'r', encoding='utf-8') as f:
    dossier_text = f.read()

# Replace DB 100M primary claims with Seojeong University Group Insurance primary recovery
dossier_updated = dossier_text.replace(
"""Primary Target Policy: DB Insurance Co., Ltd. (DB손해보험주식회사)
Target Vehicle Plate : 28모1390 (Kia Morning / 기아 모닝 경승용) | Policy No: 2-2026-0531750-000
Product Name         : DB손해보험 프로미카 개인용 자동차보험 (종합보험)
Policy Period/Renewal: January 21, 2026 24:00 KST ~ January 21, 2027 24:00 KST (Active 52 days prior to crash)
Corporate Profile    : Representative Director & CEO Jeong Jong-pyo (대표이사 정종표) | CRN: 110111-0007882
Headquarters Address : DB Financial Center, 432 Teheran-ro, Gangnam-gu, Seoul 06194 (서울특별시 강남구 테헤란로 432 DB금융센터)
Managing Channel     : DB Insurance Customer Support & Claims Center (콜센터: 1588-0100 / 다이렉트: 1600-0100 / 외국인: 1566-0161)
Claims Communication : Fax: 02-3011-3339 (HQ), 0505-181-4862 (Claims) | Email: claim_auto@idbins.com, claim@idbins.com
Coverage Claimed     : Self-Physical Accident Death Benefit (자기신체사고 사망보험금) KRW 100,000,000
Statutory Demand     : 50% Provisional Advance KRW 50,000,000 within 10 business days (Commercial Code §732-2)
Core Legal Doctrine  : Unlicensed driving exemption strictly VOID under Commercial Code §732-2, §663 &
                       Supreme Court En Banc Decision 98Da48963 (대법원 98다48963 전원합의체 판결)

Secondary Policy     : Seojeong University D-2 International Student Master Group Accident Insurance
Coverage Claimed     : Accidental Death Benefit (KRW 30M~50M) + Repatriation/Embalming Costs (KRW 5M~10M)""",
"""Primary Target Policy: Seojeong University Foreign Student Master Group Accident Insurance
Managing Entity      : Seojeong University Office of International Affairs (서정대학교 국제교류처)
Coverage & Payout    : KRW 35,000,000 ~ KRW 70,000,000 (Death Benefit KRW 30M~50M + Repatriation KRW 5M~20M)
Mandatory Legal Basis: Ministry of Education (MOE) IEQAS Accreditation & MOJ Immigration Foreign Student Mandate
Core Legal Doctrine  : Unlicensed driving exemption strictly VOID under Commercial Code §732-2, §663 &
                       Supreme Court En Banc Decision 98Da48963 (대법원 98다48963 전원합의체 판결)

Secondary Evidence   : DB Insurance Co., Ltd. Auto Policy (Policy No: 2-2026-0531750-000, Vehicle: 28모1390)
Policy Facts & Role  : Third-Party Liability Active; Self-Physical Accident [미가입 / Not Enrolled].
                       Certificate serves as conclusive evidence of lawful vehicle registration and academic driving."""
)

with open(dossier_path, 'w', encoding='utf-8') as f:
    f.write(dossier_updated)
print("Updated CASE_MASTER_KNOWLEDGE_DOSSIER.md")

print("Cleanup complete.")
