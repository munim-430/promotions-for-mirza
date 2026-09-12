# Task: Refactor Legal Claim Deliverables 00-05 and Generate Deliverable 13

## Objective
Implement DB Insurance Co., Ltd. (DB손해보험주식회사) re-targeting for Deliverables 00 through 05 in `d:/promotion/legal_claim_package/` and generate the new Deliverable 13 (`13_db_insurance_policy_verification_and_issuance_request.md`) containing DB Insurance portal inquiry pathways and the formal Korean legal request letter.

## Mandatory Inputs & Reports to Read
1. `d:/promotion/.agents/ORIGINAL_REQUEST.md` (specifically header `## 2026-09-06T09:53:43Z`)
2. `d:/promotion/.agents/survey_spec_miner_1/report.md` (portal endpoints, authentication analysis, and Korean request letter template)
3. `d:/promotion/.agents/survey_explorer_2/report.md` (exact before/after changes for files 00 to 05, corporate profile, renewal date 2026-01-21, legal defense tailoring)

## Exclusive File Ownership (Write ONLY to these files)
- `d:/promotion/legal_claim_package/13_db_insurance_policy_verification_and_issuance_request.md` (NEW)
- `d:/promotion/legal_claim_package/00_master_dossier_index_and_executive_summary.md`
- `d:/promotion/legal_claim_package/01_samsung_fire_claim_notice_and_legal_brief.md`
- `d:/promotion/legal_claim_package/02_fss_dispute_mediation_petition.md`
- `d:/promotion/legal_claim_package/03_seojeong_university_group_insurance_claim.md`
- `d:/promotion/legal_claim_package/04_bilingual_special_power_of_attorney.md`
- `d:/promotion/legal_claim_package/04_cross_border_heirship_and_legalization_guide.md`
- `d:/promotion/legal_claim_package/05_evidence_inventory_and_exhibits_catalog.md`

## Critical Rules & Guidelines
1. **Target Corporate Profile**:
   - Company: DB손해보험주식회사 (DB Insurance Co., Ltd.) / CRN: 110111-0007882
   - CEO: 대표이사 사장 정종표 (Representative Director Jeong Jong-pyo)
   - Headquarters: 서울특별시 강남구 테헤란로 432 (대치동, DB금융센터) [우편번호: 06194] / DB Financial Center, 432 Teheran-ro, Gangnam-gu, Seoul 06194
   - Customer Call Center: 1588-0100 (Direct: 1600-0100, Foreigner: 1566-0161)
   - Faxes: 02-3011-3339 (Corporate), 0505-181-4862 (Claims Intake)
   - Claims Subsidiary: DB자동차보험손해사정(주)
   - Product: DB손해보험 프로미카 개인용 자동차보험 (종합보험)
   - Policy Number: `2026-DB-AUTO-28M1390`
   - Renewal Date: January 21, 2026 (2026-01-21 24:00 KST ~ 2027-01-21 24:00 KST, active 52 days prior to accident on March 14, 2026)
   - Managing Channel: DB Insurance Direct / Customer Claims Center (1588-0100), replacing agent Shim Ki-cheol
2. **PRESERVE VEHICLE MAKE**:
   - `28모1390` is a Kia Morning (`기아 모닝 경승용` / `Kia Morning`).
   - DO NOT replace `기아` or `Renault Samsung` when referring to the vehicle! Only replace Samsung Fire as the insurance company.
3. **Legal Defenses**:
   - Strictly preserve Korean Commercial Code §732-2, §739, §663, and Supreme Court En Banc Decision 98Da48963.
   - Tailor defenses to DB Insurance auto policy terms (보통약관 자기신체사고 및 자동차상해 특별약관).
   - Clarify that Guarantee of Automobile Accident Compensation Act §29-2 unlicensed deductible does not apply to single-vehicle first-party death benefits.
4. **Deliverable 13**:
   - Incorporate the complete investigation of `directdb.co.kr` and `idbins.com` (`FWMYCV0371.do`, `FWMYCV0383.do`, `FWMYCV0366.do`, `FWMYCV0216.do`), authentication failure analysis for deceased foreign national, and the complete official Korean legal request letter ("보험가입증명서 및 보험료납입영수증 발급요청서") under FCPA Art. 28 and Commercial Code Arts. 638, 640.

## Deliverables & Handoff
- Make all edits cleanly to your assigned files.
- Write a complete handoff report to `d:/promotion/.agents/worker_1/handoff.md` and send a message when done.
