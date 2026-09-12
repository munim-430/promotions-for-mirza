# Comprehensive Survey Report: Test Suite, Compilation Pipeline & Transmittals Scope
**Prepared by:** Pipeline & Test Explorer (`survey_explorer_3`)  
**Date:** September 6, 2026 (2026-09-06)  
**Target Milestone:** Full System Mapping for DB Insurance Re-Targeting & Compilation Pipeline Integration  
**Working Directory:** `d:/promotion`  

---

## 1. Executive Summary

This investigation conducted a comprehensive code-level audit of:
1. The **Automated Test Suite** located in `d:/promotion/tests/` (`run_all_tests.py`, `test_adversarial_suite.py`, `test_adversarial_deep_dive.py`, `test_harness_challenger_r3_1.py`, and `stress_test_results.json`).
2. The **Master Compilation Script** `d:/promotion/assemble_dossier.py` and the historical Markdown $\rightarrow$ DOCX $\rightarrow$ PDF generation engine (`.agents/worker_r3_4/compile_all_dossier.py`).
3. The **Executive Legal & Institutional Email Transmittals Suite** in `d:/promotion/legal_claim_package/12_lawyer_and_insurer_filing_email_transmittals.md`.
4. The **Packaging Workflows & Dispatch Guides**, including `01_SEND_TO_BANGLADESH_PRINT_PACK/`, `02_EVIDENCE_AND_IDENTITY_EXHIBITS/`, `03_KOREAN_LAWYERS_AND_INSURERS_FILING_PACK/`, `06_direct_filing_dispatch_package.md`, and `11_dhaka_to_seoul_dhl_dispatch_and_10day_tracking_guide.md`.

### Core Findings at a Glance
- **Test Suite Status:** The existing test runner executes 11 tests across `test_adversarial_suite.py` and `test_adversarial_deep_dive.py` with 100% pass status against the current Samsung Fire files. However, `test_adversarial_suite.py` hardcodes Samsung Fire policy `2026-SF-AUTO-28M1390`, agent `심기철 (010-8969-0440)`, and stem `01_samsung_fire_claim_notice_and_legal_brief`. Furthermore, it omits `12_lawyer_and_insurer_filing_email_transmittals.md` from its 13-stem validation list. The challenger harness (`test_harness_challenger_r3_1.py`) is decoupled from `run_all_tests.py`.
- **Architectural Disconnect in `assemble_dossier.py`:** Currently, `assemble_dossier.py` is a 636-line script that solely outputs `CASE_MASTER_KNOWLEDGE_DOSSIER.md`. It does **not** compile markdown to DOCX or PDF. The DOCX/PDF generation pipeline previously existed in `.agents/worker_r3_4/compile_all_dossier.py` using `python-docx` and Windows COM automation (`win32com.client.Dispatch('Word.Application')`). Requirement R3 and Acceptance Criteria explicitly mandate that `python assemble_dossier.py` must regenerate all `.md`, `.docx`, and `.pdf` deliverables. Thus, `assemble_dossier.py` must be upgraded into a unified compiler.
- **Vehicle vs. Insurer Entity Boundary:** The subject vehicle is a `Kia Morning` (`기아 모닝 경승용`, plate `28모1390`). Any automated grep audit asserting "zero stale Samsung Fire references" must strictly differentiate between the vehicle make (`Renault Samsung / 기아`) and the target insurer (`Samsung Fire / 삼성화재 / SFMI`), avoiding false-positive test breaks.
- **Environment Capabilities:** Microsoft Word 16.0 COM automation is verified operational on the host system. `docx`, `fitz` (PyMuPDF), and `pypdf` are installed and functioning. `pandoc` is not installed on PATH, confirming that the `python-docx` + Word COM pipeline is the canonical build toolchain.

---

## 2. Test Suite Deep Dive (`d:/promotion/tests/`)

### 2.1 Inventory of Test Files
| File Name | Size (Bytes) | Role & Architecture | Test Framework | Execution Status |
|---|---|---|---|---|
| `run_all_tests.py` | 1,356 | Master Test Runner; aggregates suites and reports summary | `unittest.TextTestRunner` | Active (Runs 11 tests) |
| `test_adversarial_suite.py` | 10,745 | High-level adversarial verification of files, XML, PDF, gateway limits, entities, and citations | `unittest.TestCase` (7 tests) | Active (All PASS) |
| `test_adversarial_deep_dive.py` | 6,701 | Deep-dive cross-referencing of 37 exhibits, banking coordinates, arithmetic shares, and format parity | `unittest.TestCase` (4 tests) | Active (All PASS) |
| `test_harness_challenger_r3_1.py` | 22,136 | Mathematical simulation of 6%/12% delay interest, KLAC indigence (4.678%), service dates, and 4 scenarios | Standalone Class | Active (All PASS, standalone) |
| `stress_test_results.json` | 6,090 | Machine-readable output produced by `test_harness_challenger_r3_1.py` | JSON Artifact | Up to date |

---

### 2.2 Existing Assertions & Hardcoded Elements

#### A. In `test_adversarial_suite.py`
1. **Stem List (`EXPECTED_MD_STEMS` - Lines 25–39):**
   ```python
   EXPECTED_MD_STEMS = [
       "00_master_dossier_index_and_executive_summary",
       "01_samsung_fire_claim_notice_and_legal_brief",  # HARDCODED SFI STEM
       "02_fss_dispute_mediation_petition",
       "03_seojeong_university_group_insurance_claim",
       "04_bilingual_special_power_of_attorney",
       "04_cross_border_heirship_and_legalization_guide",
       "05_evidence_inventory_and_exhibits_catalog",
       "06_direct_filing_dispatch_package",
       "07_legal_aid_and_consular_escalation_roster",
       "08_attorney_in_fact_execution_checklist",
       "09_direct_international_claim_and_10day_statutory_notice",
       "10_parallel_pro_bono_and_consular_intake_packets",
       "11_dhaka_to_seoul_dhl_dispatch_and_10day_tracking_guide",
   ]
   ```
   *Defect:* Only 13 stems are listed. `12_lawyer_and_insurer_filing_email_transmittals` is completely absent from the stem list, despite existing as Deliverable 12.
2. **Key Entities Assertion (`test_06_policy_number_and_agent_contact_integrity` - Lines 165–175):**
   ```python
   key_entities = {
       "vehicle_number": r"28모\s*1390",
       "policy_number": r"2026-SF-AUTO-28M1390",      # HARDCODED SFI POLICY
       "agent_name": r"심기철|Shim\s+Ki-cheol",         # HARDCODED SFI AGENT
       "agent_phone": r"010-8969-0440",                # HARDCODED SFI PHONE
       "swift_mtb": r"MTBLBDDH",
       "deceased_name": r"MAHADI\s+MONOAR\s+HOSSAIN",
       "deceased_arc": r"010530-7660021",
       "father_name": r"BELAL\s+HOSSAIN",
       "mother_name": r"MONOARA\s+BEGUM",
   }
   ```
   *Defect:* Asserts `policy_number` with Samsung Fire prefix `2026-SF-AUTO-28M1390`, agent `심기철`, and phone `010-8969-0440`. These will instantly break once files are retargeted to DB Insurance.
3. **Statutory Articles & Precedents (`test_07_statutory_articles_and_precedents` - Lines 193–202):**
   - Asserts: `Art_732_2_provisional_payment` (150 occurrences), `Art_739_accidental_death` (77 occurrences), `Art_663_prohibition_disadvantage` (64 occurrences), `PIL_Art_49_heirship` (69 occurrences), `Civil_Act_Art_118_poa` (20 occurrences), `Precedent_98Da48963` (82 occurrences), `Precedent_97Da27039` (33 occurrences), `Precedent_98Da26910` (27 occurrences).
   - *Status:* Valid and must be 100% preserved during the DB Insurance migration.
4. **Renewal Date:**
   - Currently, the renewal date (whether March 13, 2026 or January 21, 2026) is **not** asserted at all in `test_adversarial_suite.py`.

#### B. In `test_adversarial_deep_dive.py`
1. **Stem List (`STEMS` - Lines 20–34):** Same hardcoded `01_samsung_fire_claim_notice_and_legal_brief` and omits `12_`.
2. **Financial Arithmetic Consistency (`test_03` - Line 104):**
   - Specifically parses `01_samsung_fire_claim_notice_and_legal_brief.md` for KRW 100M and KRW 50M.
3. **Exhibit Cross-References (`test_01` - Line 47):**
   - Asserts exactly 37 exhibits in `05_evidence_inventory_and_exhibits_catalog.md` and 0 undefined references across all 13 documents. Exhibit G-1 is currently "Samsung Fire Formal Demand & Legal Brief".

#### C. In `test_harness_challenger_r3_1.py`
1. Line 261: `samsung_auto_principal = Decimal("100000000")`
2. Line 270: `print(f"  * Policy 1 (Samsung Fire Auto): KRW {samsung_auto_principal:,}...")`
3. Scenario descriptions in `test_decision_trees_and_scenarios` (Lines 304–352) contain references to Policy `28모1390` under insurer response timelines.

---

### 2.3 Required Test Suite Updates & New Tests for DB Insurance

To validate the DB Insurance migration and meet Acceptance Criteria R4, the test suite requires targeted refactoring:

```
+---------------------------------------------------------------------------------------------------+
|                                TEST SUITE REFACTORING SPECIFICATION                               |
+------------------------------------+--------------------------------------------------------------+
| File / Module                      | Required Modifications & New Capabilities                    |
+------------------------------------+--------------------------------------------------------------+
| tests/test_adversarial_suite.py    | 1. Update EXPECTED_MD_STEMS: replace '01_samsung_fire...'    |
|                                    |    with '01_db_insurance_claim_notice_and_legal_brief' and  |
|                                    |    append '12_lawyer_and_insurer_filing_email_transmittals'  |
|                                    |    (total 14 deliverable stems).                             |
|                                    | 2. Refactor test_06:                                         |
|                                    |    - Add 'db_insurer': r'DB손해보험|DB\s+Insurance'          |
|                                    |    - Add 'db_call_center': r'1588-0100'                      |
|                                    |    - Add 'db_address': r'DB금융센터|432\s+Teheran-ro|테헤란로' |
|                                    |    - Add 'renewal_date': r'2026-01-21|2026년\s*1월\s*21일'    |
|                                    |    - Replace 'policy_number' with DB reference.              |
|                                    |    - Remove Samsung agent Shim Ki-cheol / 010-8969-0440.     |
|                                    | 3. Add NEW test_08_zero_stale_samsung_fire_references:      |
|                                    |    Grep audit across all MD/txt files ensuring 0 residual    |
|                                    |    Samsung Fire insurer mentions (excluding Renault SM5).    |
+------------------------------------+--------------------------------------------------------------+
| tests/test_adversarial_deep_dive.py| 1. Update STEMS to match 14 deliverables (DB Insurance).     |
|                                    | 2. Update test_03 to check 01_db_insurance...                |
|                                    | 3. Ensure Exhibit G-1 catalog update preserves 37 exhibits.  |
+------------------------------------+--------------------------------------------------------------+
| tests/test_harness_challenger_r3_1 | 1. Rename variables: samsung_auto_principal -> db_principal. |
|                                    | 2. Update scenario texts from Samsung Fire to DB Insurance.  |
|                                    | 3. Maintain 100% precision on 6% commercial & 12% lit int.   |
+------------------------------------+--------------------------------------------------------------+
| tests/run_all_tests.py             | 1. Import AdversarialStressTester from test_harness...       |
|                                    | 2. Execute all 3 suites in a single unified run with         |
|                                    |    comprehensive summary output and pass/fail exit code.     |
+------------------------------------+--------------------------------------------------------------+
```

---

## 3. Compilation Pipeline & `assemble_dossier.py` Analysis

### 3.1 What `assemble_dossier.py` Currently Does
- **Target File:** `d:/promotion/CASE_MASTER_KNOWLEDGE_DOSSIER.md` (52,684 bytes).
- **Architecture:** Pure Python sequential writer script (`w(line)`).
- **Hardcoded Content:**
  - Case metadata (Lines 32–68): Declares Samsung Fire as primary insurer, vehicle `28모1390`, policy renewal date March 13, 2026, agent Shim Ki-cheol (`010-8969-0440`).
  - Section 1.3 (Lines 104–106): Objectives specifically name Samsung Fire.
  - Section 2 (Lines 124–125): Timeline places policy renewal at `March 13, 2026 (24:00)`.
  - Section 5.1 (Lines 303–308): "Samsung Fire Claim Specifics".
  - Section 6 Track 1 (Lines 337–340): "Direct Content-Certified Demand to Samsung Fire".
  - Section 7 File Inventory (Line 408): Lists `01_Samsung_Fire_Insurance_Claim_Notice_and_Legal_Brief.pdf`.
  - Section 8 Exhibit G-1 (Line 457): Lists `Samsung Fire Formal Demand & Legal Brief`.
  - Section 9 Transmittal 4 (Lines 489–495): "Transmittal 4 -> Samsung Fire & Marine Insurance Co., Ltd.".
  - Section 13 Playbook (Line 615): Step 2 sends notice to Samsung Fire.

### 3.2 The Existing Compilation Pipeline (`.agents/worker_r3_4/compile_all_dossier.py`)
In the previous milestone, full Markdown $\rightarrow$ DOCX $\rightarrow$ PDF compilation was executed by `compile_all_dossier.py`:

```
Markdown Source Files (14 files in legal_claim_package/)
        │
        ▼ (python-docx Custom Parser)
Word Documents (.docx in legal_claim_package/docx/)
        │
        ▼ (Windows COM: win32com.client.Dispatch('Word.Application'))
Print-Ready PDFs (.pdf in legal_claim_package/pdf/)
        │
        ▼ (PyMuPDF / fitz Verification)
Integrity Verification (Non-empty pages, >200 total pages, zero XML errors)
```

#### Detailed Toolchain & Dependencies:
1. **`python-docx` (v1.x):**
   - Generates `.docx` from scratch with custom styling:
     - Font: `Malgun Gothic` (맑은 고딕), line spacing 1.15, margins 0.7 in.
     - Color Palette: Deep Navy (`#002060`), Charcoal (`#3C3C3C`), Soft Slate (`#F4F6F9`), Accent Navy (`#E8ECF2`).
     - Running headers ("LEGAL RECOVERY DOSSIER | CASE: 2026-DB-AUTO-28M1390") and footers ("Confidential Litigation Document").
     - Custom AST parser supporting headings (`#` to `####`), tables with alternating shading (`#FAFAFA`), code callouts (`Consolas`), blockquotes, bullet lists, and bold/inline code spans.
2. **`win32com.client` (Microsoft Word COM Automation):**
   - Connects to host Microsoft Word 16.0 via `win32com.client.Dispatch('Word.Application')`.
   - Opens `.docx` in headless mode (`word.Visible = False`).
   - Executes native high-fidelity PDF export via `wb.SaveAs2(abs_pdf, FileFormat=17)` (`wdFormatPDF`).
   - Handles font embedding, East Asian typography, table pagination, and vector layout without requiring external utilities like `pandoc` or `wkhtmltopdf`.
3. **`fitz` (PyMuPDF) & `pypdf`:**
   - Validates generated PDFs: opens document, iterates through all pages, extracts text, asserts page count $> 0$ and non-blank page rendering.
4. **`pandoc` Assessment:**
   - Command `where.exe pandoc` returned exit code 1 (not installed).
   - Therefore, the pipeline relies 100% on the native Python + Microsoft Word COM automation stack.

### 3.3 Proposed Architectural Unification in `assemble_dossier.py`
To satisfy the user requirement:
> *"Run `assemble_dossier.py` to regenerate all markdown, Word (.docx), and PDF deliverables with zero formatting errors."*

`assemble_dossier.py` must be upgraded to serve as the single, all-in-one build command:
1. **Phase 1: Knowledge Base Generation** — Regenerates `CASE_MASTER_KNOWLEDGE_DOSSIER.md` with all DB Insurance facts.
2. **Phase 2: DOCX Compilation** — Parses all 14 markdown files in `legal_claim_package/` into `legal_claim_package/docx/` using the styled `python-docx` builder. Also creates `Lawyer_and_Insurer_Filing_Emails.docx`.
3. **Phase 3: PDF Export via Word COM** — Converts all `.docx` files to `.pdf` in `legal_claim_package/pdf/` and creates `Lawyer_and_Insurer_Filing_Emails.pdf`.
4. **Phase 4: Pack Synchronization** — Synchronizes compiled files to `03_KOREAN_LAWYERS_AND_INSURERS_FILING_PACK/` and `01_SEND_TO_BANGLADESH_PRINT_PACK/`.
5. **Phase 5: Post-Build Validation** — Runs `fitz` page checks and reports total page count and file sizes.

---

## 4. Transmittals Suite Inventory (`12_lawyer_and_insurer_filing_email_transmittals.md`)

`12_lawyer_and_insurer_filing_email_transmittals.md` contains 6 institutional email transmittals. Below is the granular change matrix required for DB Insurance re-targeting:

```
+---------------------------------------------------------------------------------------------------+
|                        TRANSMITTALS SUITE AUDIT & RETARGETING MATRIX                              |
+-------------------+-----------------------------+--------------------+----------------------------+
| Transmittal #     | Current Samsung Fire Content| Required DB Retargeting   | Impacted Lines / Elements  |
+-------------------+-----------------------------+--------------------+----------------------------+
| Transmittal 1     | • Attachment 4: 01_samsung_ | • Attachment 4:    | Lines 39, 54, 55, 61, 76   |
| (KLAC)            |   fire_claim_notice...pdf   |   01_db_insurance...|                            |
|                   | • Policy: 삼성화재 애니카   | • Policy: DB손해보험|                            |
|                   |   (2026-SF-AUTO-28M1390)    |   (2026-DB-AUTO...) |                            |
|                   | • Body text: 삼성화재       | • Body text: DB손보|                            |
|                   | • Eng text: Samsung Fire    | • Eng: DB Insurance|                            |
+-------------------+-----------------------------+--------------------+----------------------------+
| Transmittal 2     | • Attachment 2: 01_samsung_ | • Attachment 2:    | Lines 94, 106              |
| (Gong-Gam / DURO) |   fire_claim_notice...pdf   |   01_db_insurance...|                            |
|                   | • Body: 대형 손해보험사     | • Body: 대형 손보사|                            |
|                   |   (삼성화재해상보험)        |   (DB손해보험주식회 |                            |
|                   |                             |    사)              |                            |
+-------------------+-----------------------------+--------------------+----------------------------+
| Transmittal 3     | • "대형 금융기관"           | • Maintain context;| Lines 130–158              |
| (Seoul Bar Assoc) |                             |   ensure consistent |                            |
|                   |                             |   cross-references |                            |
+-------------------+-----------------------------+--------------------+----------------------------+
| Transmittal 4     | • Heading: SAMSUNG FIRE &   | • Heading: DB      | Lines 161–204              |
| (PRIMARY INSURER) |   MARINE INSURANCE          |   INSURANCE CO.,   | (ENTIRE SECTION REWRITTEN) |
|                   | • To: claim_auto@samsungfire|   LTD.             |                            |
|                   | • Cc: shim_kc@samsungfire   | • To: DB Claims HQ |                            |
|                   | • Subj: 삼성화재 자동차보험 | • Subj: DB손해보험 |                            |
|                   | • Attach: 01_samsung_fire...| • Attach: 01_db... |                            |
|                   | • Recipient: 삼성화재 대표  | • Recipient: DB손보|                            |
|                   |   및 강원보상본부, 심기철   |   대표이사 및 보상 |                            |
|                   | • Policy: 애니카 2026-SF... |   총괄본부         |                            |
|                   | • Call Center: 1588-5114    | • Call: 1588-0100  |                            |
+-------------------+-----------------------------+--------------------+----------------------------+
| Transmittal 5     | • Seojeong University D-2   | • Retain group     | Lines 208–246              |
| (Seojeong Univ)   |   Group accident insurance  |   claim context;   | (Note: DB was already in   |
|                   |   consortium (DB/KB/Hyundai)|   confirm no clash |  consortium list)          |
|                   |                             |   with individual  |                            |
+-------------------+-----------------------------+--------------------+----------------------------+
| Transmittal 6     | • Line 284: "Samsung Fire   | • Line 284: replace| Lines 250–300 (Line 284)   |
| (Bangladesh       |   & Marine Insurance Co."   |   with "DB Insur-  |                            |
|  Embassy)         |   in Note Verbale prayer    |   ance Co., Ltd."  |                            |
+-------------------+-----------------------------+--------------------+----------------------------+
```

---

## 5. Packaging Workflows & Dispatch Manifests

### 5.1 Directory-by-Directory Packaging Inventory

#### 1. `01_SEND_TO_BANGLADESH_PRINT_PACK/` (Print-Ready Files for Parents in Cumilla)
- `01_Bilingual_Special_Power_of_Attorney_TO_PRINT_AND_SIGN.pdf` (345,647 B)
- `02_Cross_Border_Heirship_and_Legalization_Guide.pdf` (270,001 B)
- `03_Korean_Hospital_Death_Certificate_GangNeung_Asan.pdf` (552,225 B)
- `04_Korean_Hospital_Post_Mortem_Certificate_GangNeung_Asan.pdf` (623,691 B)
- `05_Sokcho_Police_Station_Body_Release_and_Accident_Order.pdf` (320,227 B)
- `06_Embalming_and_Non_Contagious_Disease_Certificate.pdf` (423,880 B)
- `07_Bangladesh_Embassy_Seoul_Mortuary_Certificate.pdf` (325,107 B)
- `README_BANGLADESH_INSTRUCTIONS_বাংলা.txt` (4,979 B)
*Status:* All files are valid. Contains no direct Samsung Fire references.

#### 2. `02_EVIDENCE_AND_IDENTITY_EXHIBITS/` (Numbered Exhibits Repository)
- Exhibits A1, B1, B2, C1, C2, C3, D1, D3, E3 (NID & Passport), F3 (MTB Bank statement), F4 (repatriation receipts).
- `README_EVIDENCE_LIST_বাংলা.txt` (3,325 B)
*Status:* Conclusive evidentiary scans. Preserved intact.

#### 3. `03_KOREAN_LAWYERS_AND_INSURERS_FILING_PACK/` (Lawyer & Insurer Filing Pack)
- `00_Lawyer_and_Insurer_Filing_Emails_COPY_PASTE_WORD_FILE.docx` (47,638 B)
- `00_Lawyer_and_Insurer_Filing_Emails_REFERENCE.pdf` (405,489 B)
- `01_Samsung_Fire_Insurance_Claim_Notice_and_Legal_Brief.pdf` (380,006 B) $\rightarrow$ **Must be replaced with `01_DB_Insurance_Claim_Notice_and_Legal_Brief.pdf`**
- Exhibits and guides 02 through 12.
- `README_KOREAN_FILING_GUIDE_বাংলা.txt` (4,702 B) $\rightarrow$ **Must be updated in lines 7, 18, 20, 21, 23 to reference DB Insurance and Call Center 1588-0100 instead of Samsung Fire / Agent Shim Ki-cheol.**

---

### 5.2 Dispatch Guides: Courier & Postal Manifests

#### A. In `06_direct_filing_dispatch_package.md`:
- **Routing Table 3.1 (Lines 415–445):**
  - Current: Samsung Fire HQ, Seocho Tower, 14 Seocho-daero 74-gil, Seocho-gu, Seoul 06620 / Gangwon regional / Agent Shim Ki-cheol.
  - Required DB Replacement:
    - Company: DB손해보험주식회사 (DB Insurance Co., Ltd.)
    - Headquarters Address: 서울특별시 강남구 테헤란로 432 DB금융센터 (DB Financial Center, 432 Teheran-ro, Gangnam-gu, Seoul 06193)
    - Call Center: `1588-0100` / Auto Claims Hotline: `1588-0100`
    - Portal: `directdb.co.kr`, `idbins.com`
- **Electronic Intake & Content-Certified Mail Sections (Lines 487–560, 689–729):** Update recipient addresses, CEO name, and postal validation instructions.

#### B. In `11_dhaka_to_seoul_dhl_dispatch_and_10day_tracking_guide.md`:
- **DHL AWB & Pro-Forma Invoice Declarations (Lines 149–199, 289):** Update recipient to DB Insurance Headquarters (DB Financial Center, 432 Teheran-ro).
- **Email Gateway Limits & Template 1 (Lines 330–415):** Retarget Template 1 from Samsung Fire to DB Insurance.
- **10-Day Statutory Response Tracker (Lines 702–824):** Update Day-by-Day actions from Samsung Fire hotline (1588-5114) to DB Insurance Claims Center (1588-0100).

---

## 6. Grep Audit Strategy & Stale Reference Prevention

### 6.1 Crucial Distinction: Vehicle Make vs. Insurance Company
The deceased was driving a **Kia Morning** (`기아 모닝 경승용`).
- The phrase `Kia Morning`, `Renault Samsung`, `기아`, `기아 모닝` refers to the **motor vehicle manufacturer/model**.
- The phrases `Samsung Fire`, `Samsung Fire & Marine`, `삼성화재`, `삼성화재해상보험`, `SFMI`, `2026-SF` refer to the **insurance company**.

**Rule for Grep Audits:** The automated audit regex must use negative lookbehinds or context boundary matching to avoid false positives on the vehicle model name:
- Prohibited: `(?<!Renault\s)(?<!르노)삼성화재`, `(?<!Renault\s)Samsung\s+Fire`, `SFMI`, `2026-SF`, `심기철`, `010-8969-0440`, `1588-5114`, `samsungfire\.com`, `Seocho\s+Tower`, `서초대로74길`.

### 6.2 Prohibited Patterns & Stale Reference Checklist
```python
STALE_SAMSUNG_PATTERNS = [
    (r'(?<!Renault\s)(?<!르노)삼성화재', "Samsung Fire in Korean (삼성화재)"),
    (r'(?<!Renault\s)Samsung\s+Fire', "Samsung Fire in English"),
    (r'2026-SF-AUTO', "Samsung Fire Policy ID (2026-SF-AUTO)"),
    (r'심기철|Shim\s+Ki-ch[ue]l', "Samsung Fire Agent Shim Ki-cheol"),
    (r'010-8969-0440', "Samsung Fire Agent Phone"),
    (r'1588-5114', "Samsung Fire Customer Call Center"),
    (r'samsungfire\.com', "Samsung Fire Domain / Email"),
    (r'Seocho\s+Tower|서초대로\s*74길|14\s+Seocho-daero', "Samsung Fire Seocho HQ Address"),
    (r'19\s+Okcheon-ro|옥천로\s*19', "Samsung Fire Gangwon Office Address"),
    (r'March\s+13,?\s+2026|2026년\s*3월\s*13일', "Old Stale Renewal Date (March 13, 2026)"),
]
```

### 6.3 Required DB Insurance Target Assertions
```python
DB_REQUIRED_PATTERNS = [
    (r'DB손해보험|DB\s+Insurance', "DB Insurance Corporate Identity"),
    (r'1588-0100', "DB Insurance Representative Call Center"),
    (r'DB금융센터|432\s+Teheran-ro|테헤란로\s*432', "DB Financial Center HQ Address"),
    (r'2026-01-21|2026년\s*1월\s*21일|January\s+21,?\s+2026', "Verified Policy Renewal Date (2026-01-21)"),
    (r'28모\s*1390', "Subject Vehicle Number (28모1390)"),
    (r'732-2|732조의\s*2', "Commercial Code Art. 732-2"),
    (r'663조|Art(?:icle|\.)?\s*663', "Commercial Code Art. 663"),
    (r'98다48963|98Da48963', "Supreme Court En Banc Decision 98Da48963"),
]
```

---

## 7. Actionable Implementation & Verification Plan

### Phase 1: Test Suite Upgrades (`tests/`)
1. Refactor `test_adversarial_suite.py`:
   - Update `EXPECTED_MD_STEMS` with the DB Insurance deliverable name and add `12_lawyer_and_insurer_filing_email_transmittals`.
   - Update `test_06_policy_number_and_agent_contact_integrity` to assert DB Insurance corporate entities, address, call center `1588-0100`, and renewal date `2026-01-21`.
   - Implement `test_08_zero_stale_samsung_fire_references` using the regex checklist above.
2. Refactor `test_adversarial_deep_dive.py`:
   - Update `STEMS` list and `test_03` deliverable path.
3. Update `test_harness_challenger_r3_1.py`:
   - Retarget scenario descriptions and variable names to DB Insurance.
4. Integrate into `run_all_tests.py`:
   - Add `AdversarialStressTester` execution to provide 100% test coverage under a single runner.

### Phase 2: Unify Master Compilation Engine in `assemble_dossier.py`
1. Update knowledge base generator in `assemble_dossier.py`:
   - Retarget all metadata, chronology, legal grounds, file inventory, transmittals, and playbook sections to DB Insurance and renewal date 2026-01-21.
2. Merge `compile_all_dossier.py` logic into `assemble_dossier.py`:
   - Embed the `python-docx` styled converter and Microsoft Word COM automation exporter.
   - Automatically compile all 14 markdown files in `d:/promotion/legal_claim_package/` into `.docx` and `.pdf`.
   - Synchronize output `.docx` and `.pdf` files into `03_KOREAN_LAWYERS_AND_INSURERS_FILING_PACK/` and `01_SEND_TO_BANGLADESH_PRINT_PACK/`.
   - Run post-build verification with `fitz` ensuring $>200$ pages and 0 empty pages.

### Phase 3: Transmittals & Packaging Execution
1. Refactor `12_lawyer_and_insurer_filing_email_transmittals.md` according to Section 4 matrix.
2. Update `03_KOREAN_LAWYERS_AND_INSURERS_FILING_PACK/README_KOREAN_FILING_GUIDE_বাংলা.txt`.
3. Update dispatch manifests in `06_direct_filing_dispatch_package.md` and `11_dhaka_to_seoul_dhl_dispatch_and_10day_tracking_guide.md`.

---

## 8. Conclusion

The pipeline, test suite, and transmittal assets in `d:/promotion` are fully mapped. The system has the necessary runtime dependencies (Python `docx`, Word 16.0 COM, PyMuPDF) to execute the complete build and test lifecycle locally. With the architectural integration of compilation into `assemble_dossier.py` and the test suite enhancements specified herein, the team will achieve 100% test validation and zero stale insurer references.
