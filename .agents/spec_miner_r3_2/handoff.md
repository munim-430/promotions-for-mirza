# HANDOFF REPORT: SPECIFICATION MINING FOR R2 (PRO BONO & CONSULAR INTAKE PACKETS)

**Agent:** `spec_miner_r3_2` (Specification Miner)  
**Recipient:** Parent Orchestrator (`ee9982c4-2cdf-44ae-97ab-bdacc00ac17c`)  
**Date:** August 27, 2026  
**Target Milestone:** R2 / Phase R3 — Parallel Pro Bono & Consular Intake Packets  

---

## 1. Observation
- Inspected repository files:
  - `d:/promotion/.agents/ORIGINAL_REQUEST.md` (lines 75–112): Defines Requirement R2 requiring tailored pro bono legal aid and consular intake packages for KLAC, Gong-Gam, DURO, and the Bangladesh Embassy in Seoul.
  - `d:/promotion/PROJECT.md` (lines 1–43): Establishes project architecture, litigation-grade standards under Korean Commercial Code Arts. 732-2, 739, 663, and Private International Law Art. 49.
  - `d:/promotion/legal_claim_package/07_legal_aid_and_consular_escalation_roster.md` (lines 116–560): Contains comprehensive statutory provisions for KLAC under Legal Aid Act Arts. 1, 7, 8, 22; branch routing matrices for Seoul Central and Gangwon branches; diplomatic profile for the Embassy of Bangladesh in Seoul (17 Jangmun-ro 6-gil, Yongsan-gu; Counsellor Mikon Tangchanggya, Labour & Consular Wing); Note Verbale protocols; and Gong-Gam coordinates.
  - `d:/promotion/legal_claim_package/02_fss_dispute_mediation_petition.md` (lines 10–107): Identifies sole heirs (Belal Hossain 2/3 share, Monoara Begum 1/3 share), policyholder Mahadi Monoar Hossain (`010530-7660021`), vehicle `28모1390`, managing agent 심기철 (`010-8969-0440`), and relief sought.
  - Web research verification:
    - Association for Public Interest Law DURO (사단법인 두루): Address: 서울특별시 중구 퇴계로8길 58, 3층 [04635] / Tel: 02-6200-1853 / Fax: 02-6200-0811 / Email: `duroo@duroo.org` / Specialization: Migrant Rights Team (이주인권팀).
    - Gong-Gam Human Rights Law Foundation (공익인권법재단 공감): Address: 서울특별시 종로구 창덕궁길 29-6, 3층 (원서동) [03058] / Tel: 02-3675-7740 / Fax: 02-3675-7742 / Email: `gonggam@gmail.com` / `gonggam.law@gmail.com`.
    - Korea Legal Aid Corporation (대한법률구조공단): Seoul Central Branch (서울특별시 서초구 서초대로 247, 4~6층, Tel: 02-535-0132 / Hotline: 132); Sokcho Branch (강원특별자치도 속초시 번영로 163, 2층, Tel: 033-636-2342).
    - Embassy of Bangladesh in Seoul: 17 Jangmun-ro 6-gil, Yongsan-gu, Seoul 04393 / Consular Direct: +82-2-796-4058 / 24/7 Hotline: +82-10-8588-4058 / Emails: `mission.seoul@mofa.gov.bd`, `labour.seoul@mofa.gov.bd`, `bdootseoul@gmail.com`.

---

## 2. Logic Chain
1. **Statutory Basis for Free Legal Aid (KLAC)**:
   - Under Legal Aid Act Art. 22 and Ministry of Justice directives, foreign accident victims with claims arising in South Korea are eligible for 100% free legal aid if their monthly income is <= 125% of national median income.
   - Deceased D-2 student had KRW 0 taxable domestic income, and overseas Bangladeshi parents earn subsistence agrarian income, qualifying them under the indigence criteria.
   - Legal Aid Act Art. 22 authorizes the State Treasury to advance all court stamp (인지대) and service fees (송달료), which are recovered from Samsung Fire upon judgment pursuant to Civil Procedure Act Art. 98.
2. **Public Interest Litigation Grounds (Gong-Gam & DURO)**:
   - Supreme Court En Banc Decision 98Da48963 establishes that first-party accidental death insurance (자기신체사고/자동차상해) is accident insurance under Commercial Code Art. 739.
   - Commercial Code Art. 732-2 prohibits insurers from excluding death benefits even for gross negligence (which includes unlicensed driving).
   - Commercial Code Art. 663 prohibits detrimental alterations.
   - Insurers routinely attempt to enforce void exclusion clauses against vulnerable foreign students and overseas families. This systemic injustice provides the core hook for Gong-Gam and DURO's public interest impact briefs.
3. **Consular & Diplomatic Intervention (Bangladesh Embassy)**:
   - Under Article 5 of the 1961 Vienna Convention on Consular Relations and Korean Private International Law Art. 49, the Embassy of Bangladesh has diplomatic standing to protect deceased citizens and verify foreign public documents.
   - Formally petitioning Counsellor Mikon Tangchanggya (Labour & Consular Wing) activates:
     - Diplomatic Note Verbale (공한) to Samsung Fire CEO, FSS Governor, and MOFA Korea.
     - Consular authentication of Warisan Sanad and Special POA.
     - Referral to Embassy-empanelled Korean legal counsel.
     - Consular oversight of direct SWIFT MT103 wire transfers to Islami Bank and Sonali Bank.

---

## 3. Caveats
- No caveats regarding substantive Korean insurance law or Supreme Court precedents; the doctrine in 98Da48963 is established and undisputed.
- DURO primarily focuses on systemic/impact litigation rather than routine individual aid; therefore, the intake brief to DURO is structured specifically as an impact litigation submission targeting the insurance industry's discriminatory practices against foreign students.

---

## 4. Conclusion
All statutory bases, eligibility rules, court fee advancement mechanics, organizational directories, contact channels, and customized prayers for relief have been mined and codified in `d:/promotion/.agents/spec_miner_r3_2/r2_spec_report.md`. The downstream document generation agents have all necessary parameters to produce the final client submission packets (`09_klac_foreigner_legal_aid_application_package.md`, `10_gong_gam_public_interest_litigation_brief.md`, `11_duro_public_interest_impact_litigation_brief.md`, and `12_bangladesh_embassy_diplomatic_assistance_packet.md`).

---

## 5. Verification Method
- Inspect specification file: `view_file` on `d:/promotion/.agents/spec_miner_r3_2/r2_spec_report.md`.
- Confirm coverage of all four organizations: KLAC, Gong-Gam, DURO, Bangladesh Embassy.
- Verify presence of Features Discovered table (12 features) and Edge Cases table (8 edge cases).
- Cross-reference with existing repo files: `02_fss_dispute_mediation_petition.md`, `04_bilingual_special_power_of_attorney.md`, `07_legal_aid_and_consular_escalation_roster.md`.
