# Dispatch Assignment: Evidence & Case File Fact Extraction

## Working Directory
d:/promotion/.agents/spec_miner_1

## Objective
Thoroughly inspect all files in `d:/promotion/extracted` and `d:/promotion/images` to extract and catalog all factual case data, including:
1. Deceased details: Full legal name, Alien Registration Number (010530-7660021), date of birth, nationality, passport number, visa type (D-2), university/program (Seojeong University).
2. Vehicle and Insurance details: Vehicle plate `28모1390`, Samsung Fire & Marine Insurance policy number, renewal date (March 13, 2026), coverage limits (자손/자상 Self-Injury / Accidental Death, Liability, etc.), insurance agent details (`심기철`, `010-8969-0440`).
3. Accident & Death details: Date, time, location, accident report/police traffic accident report details, cause of death / autopsy / post-mortem certificate findings, single-vehicle collision facts.
4. Heir & Family details: Father (BELAL HOSSAIN), Mother (MONOARA BEGUM), Bangladeshi national IDs, passports, address, bank details for SWIFT wire transfer.
5. University records: Seojeong University enrollment certificate, student ID, tuition/insurance fee payment, group accident policy records.

## Instructions
- Read `d:/promotion/.agents/ORIGINAL_REQUEST.md` before starting.
- Inspect the PDFs in `d:/promotion/extracted` and images in `d:/promotion/images` (you may use python scripts, pdftotext, tesseract/ocr or image inspection if available, or view files).
- Compile a comprehensive, highly detailed Fact & Evidence Inventory report and write it to `d:/promotion/.agents/spec_miner_1/fact_inventory.md` and `d:/promotion/.agents/spec_miner_1/handoff.md`.
- Send a completion message back to the orchestrator when finished.

## 2026-08-22T23:05:56Z
<USER_REQUEST>
You are the Case Evidence Spec Miner.
Your working directory is: d:/promotion/.agents/spec_miner_1
You MUST read:
1. d:/promotion/.agents/ORIGINAL_REQUEST.md
2. d:/promotion/.agents/spec_miner_1/DISPATCH.md

Inspect all PDF documents in d:/promotion/extracted and image files in d:/promotion/images. Extract every piece of factual evidence:
- Deceased identity, alien registration number, passport, student status at Seojeong University
- Vehicle plate 28모1390, Samsung Fire policy details, policy period, renewal date March 13, 2026, agent 심기철 (010-8969-0440), coverage line items
- Police report/accident summary, time, date, location, single-vehicle collision facts, cause of death
- Surviving parents (BELAL HOSSAIN & MONOARA BEGUM), Bangladeshi identification, addresses, banking details
- Seojeong University student records and group insurance details

Write your comprehensive findings to:
- d:/promotion/.agents/spec_miner_1/fact_inventory.md
- d:/promotion/.agents/spec_miner_1/handoff.md

Send a completion message back to the orchestrator with your findings.
</USER_REQUEST>
