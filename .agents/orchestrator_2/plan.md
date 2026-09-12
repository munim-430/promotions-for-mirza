# Execution Plan — Direct-Filing Dispatch Package & Legal Aid Escalation Protocol

## 1. Survey Phase
- Spawn 3 parallel survey subagents:
  1. `explorer_r1`: Survey existing dossier files (00_master_dossier through 05_evidence_inventory) in `d:/promotion/legal_claim_package` to catalog all specific identifiers, deceased data, parents, attorneys-in-fact, claim amounts, exhibit references, and dates.
  2. `spec_miner_r1`: Mine Korean postal content-certified mail (내용증명) formatting, e-filing/email templates, and exact routing data for Samsung Fire HQ (Claim/Customer Dispute resolution dept, Gangnam-gu, Seoul) & Agent Shim Ki-cheol, plus Seojeong University International Affairs Office (Yangju-si, Gyeonggi-do).
  3. `spec_miner_r2`: Mine KLAC Foreigner Legal Aid Scheme rules (Gangwon/Seoul branch routing, eligibility criteria, required documents under Foreigner Legal Aid guidelines), Bangladesh Embassy (Labour & Consular Wing, Itaewon/Dongbinggo-dong, Seoul) diplomatic representation requirements, and Bar Association Foreigner Centers (Seoul Bar Association Foreigner Human Rights Sub-committee, Gong-Gam Foundation).

## 2. Decomposition & Implementation Phase
- Produce `PROJECT.md` with full feature inventory and file boundaries.
- Spawn Workers:
  - `worker_m1`: Generate `06_direct_filing_dispatch_package.md` containing content-certified mail cover letters (Samsung Fire HQ & Agent Shim, Seojeong University), recipient routing tables, and bilingual email dispatch templates.
  - `worker_m2`: Generate `07_legal_aid_and_consular_escalation_roster.md` containing KLAC Foreigner Scheme dossier, Bangladesh Embassy formal diplomatic petition cover letter, and Bar Association Foreigner Support intake roster.
  - `worker_m3`: Generate `08_attorney_in_fact_execution_checklist.md` containing chronological execution checklist (Consular legalization/Apostille in Bangladesh, Korea Post content-certified mail dispatch, 10-day provisional payment tracking under Commercial Code Art. 732-2).
  - `worker_m4`: Update and harmonize `00_master_dossier_index_and_executive_summary.md` and `05_evidence_inventory_and_exhibits_catalog.md` with new dispatch files and exhibits.

## 3. Verification & Gating Phase
- Spawn 2 Reviewers independently (`reviewer_1`, `reviewer_2`) to verify completeness, Korean postal formatting compliance, factual consistency with existing files, and legal citation validity.
- Spawn 2 Challengers (`challenger_1`, `challenger_2`) to test contingency trigger thresholds, postal execution feasibility, and emergency escalation paths.
- Spawn 1 Forensic Auditor (`auditor_1`) to perform integrity verification.
- Complete Gate evaluation and report to Sentinel.
