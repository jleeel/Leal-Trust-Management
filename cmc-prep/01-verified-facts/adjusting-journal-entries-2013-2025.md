# QuickBooks Adjusting Journal Entries, 2013–2025 (S-45)

**ATTORNEY WORK-PRODUCT SUPPORT — PRIVILEGED & CONFIDENTIAL.** This is an analysis of a QuickBooks
report. It is not an accounting opinion.

**Source (S-45):**
- "YTD Journal Entries Excel.xlsx" (Drive `1MZSFT1KTsD5N_P7QluI0-J60VOjRp9q-`), with a PDF copy
  "YTD Journal Entries.pdf" (`1GNNmGhxvyvlfSg7141vtk5SkdeZGshd4`), uploaded by the client
  10/8/2026.
- Report title: **"Adjusting Journal Entries", "January 2000 through December 2025", accrual,
  run 10/5/2026 10:51 AM.** The file name says "YTD", but the report covers 2000–2025.
- **Read in full:** 395 entries, 1,725 lines. Debits equal credits ($60,375,044.41) and every
  entry balances.

**What it is and is not:**
- **The earliest entry is 1/1/2013.** That confirms Frazer's adjustments before 2013 were never
  entered in QuickBooks; the books were plugged to Frazer's balances in 2013.
- It lists entries **flagged as adjusting.** One closing entry seen in the draw exports
  (1/1/2017, "To close out prior years draws") is absent, so non-adjusting general-journal
  entries may be missing.
- It has **no entered/modified dates or user names.** The Audit Trail report is still needed
  (OI-98).
- **2026 entries are not included.**

## 1. The books changed between 10/3 and 10/5/2026

The same Frazer entry appears differently in two client exports two days apart:

| Entry | 505000 QuickReport, run 10/3/2026 8:48 AM (S-41) | Adjusting entries report, run 10/5/2026 10:51 AM (S-45) |
|---|---|---|
| 7/31/2025, "To reclass Hazel salary to draws" | No. **FrazerTXP7**, $42,000 | No. **Frazer7**, $42,000 |
| 12/31/2025, "To move Hazel salary to draw" | No. **FrazerTXP16**, **$6,000** | No. **Frazer16**, **$30,000** |

**Not established:**
- who made the change, and when;
- whether it was Frazer finalizing FY2025, an accountant's-copy import, or an edit in the file.

The Audit Trail shows who and when. Both versions are preserved in Drive (S-41, S-45).

**Effect:**
- 2025 salary-to-draw is now **$72,000**, all twelve $6,000 payments, against $48,000 before.
- 2025 Hazel "Personal" on the ledger becomes $9,284.67 + $72,000 = **$81,284.67**, against the
  FY2025 draft's $75,285 (calc). That is now $6,000 over the draft, where it was $18,000.33
  under.

See A-86.

## 2. "TIE TO 12.31.15" ($17,148.24 to Hazel's draws) is Manuel's funeral and memorial costs

Entry dated 12/31/2015 (num "Frazer"):

| Account | Debit | Credit |
|---|---|---|
| 505000 Personal–Hazel | $17,148.24 | |
| 799000 Miscellaneous (dairy expense) | $11,570.00 | |
| 515000 Personal–Steve | | $4,757.11 |
| 518000 Appraisal Fees / Trust Admin | | $23,961.13 |

**$23,961.13 is exactly the 2015 charges to 518000** (register, S-29):

| Payee | Amount |
|---|---|
| Millers Tulare Funeral Home | $10,330.76 |
| Barnes Memorial | $5,579.25 |
| Happy Cookers Catering | $3,750.00 |
| Peter Perkins Flowers | $2,127.67 |
| Tulare Cemetery | $1,626.25 |
| International Agri-Center | $547.20 |

So the entry allocated Manuel's 2015 funeral and memorial costs: $17,148.24 to Hazel's draws and
$11,570 to dairy expense. It also **credited Steve's draws $4,757.11.** No reason is stated for
the split or for the credit to Steve (no source). Frazer's FY2015 workpapers would explain it.

## 3. Entries that resolve earlier open points

- **2012 income taxes, symmetric:** the entry dated 11/30/2013 has four lines:
  - 505000 debit $18,913.00 / 755000 credit;
  - 515000 debit $23,302.81 / 755000 credit.
- **2013 Pismo and cable:** "city of pismo utilities" $651.11 and "charter communications"
  $930.40 both move out of 751000 Utilities into 505000. The "split" seen in S-41 was a display
  artifact.
- **United of Omaha:**
  - 12/31/2016: $4,126.20, 760000 → **515000** Personal–Steve, in the same entry as Anthem
    {STEVE} health insurance $15,832.08 → 514000. S-42's "514000" split was the other line.
  - **12/31/2017: $2,063.10, 760000 → 514000** Medical–Steve.
  - **2019–2022 are not reclassified.** Steve's yearly insurance reclasses in those years equal
    his Blue Shield premiums to the cent: 2019 $27,714.86, 2020 $20,099.14, 2021 $13,020.48,
    2022 $10,146.87. They exclude United of Omaha.
- **2015 personal income taxes:** an entry reclassed them into the partners' tax accounts and a
  second entry ("TO RECLASS PERSONAL TAX EXPENSES", FZR-YE16-03) reversed it. The net effect on
  the partner accounts is about zero (Hazel $0; Steve +$34.07).
- **Built Wright:** 12/31/2025 "To reclass CIP for new freestall barn" moves $430,508.43 out of
  230000 Leasehold Improvements into construction in progress. That corroborates "the new
  freestall" (S-40, A-82).
- **The 2018 $150,000 and $70,000 checks to Steve:** no adjusting entry. They stay as personal
  draws in the books (A-73).

## 4. Expense-to-draw reclasses by partner, 2013–2025 (calc; closing and tie-out entries excluded)

| | Hazel side (503–506) | Steve side (513–516) |
|---|---|---|
| Total moved from dairy expense into draws | **$176,124.39** | **$232,050.10** |
| of which post-death "salary" to draws | $129,000 (2022 $3,000; 2024 $54,000; 2025 $72,000) | — |
| **Excluding salary** | **$47,124.39** | **$232,050.10** |

**Main items:**
- **Hazel side:**
  - 2012 income tax $18,913;
  - Manuel's funeral allocation $17,148.24;
  - 2017 health insurance $6,519.87;
  - Pismo house tax and utilities and cable $5,401.91.
- **Steve side:**
  - health insurance 2016–2022 $103,136.00;
  - Ram 2500 financing $55,085;
  - Jacobsma "personal home repairs" $49,352.87;
  - 2012 income tax $23,302.81;
  - United of Omaha 2016–17 $6,189.30;
  - less the 2015 funeral credit, −$4,757.11.

## 5. Health insurance: what was left in dairy expense, by partner

Register coding by year (S-29), with this report's reclasses applied (calc, rounded):

| | Coded to dairy insurance, never reclassified | Reclassified or coded to the partner |
|---|---|---|
| **Hazel** (Anthem, unlabeled) | 2014 $9,287; 2015 $9,565; 2016 $6,052: **about $24,900**. Plus 2010–11 $3,545 (pre-2013, INDETERMINATE) | 2010–13 and 2018–23 coded to 504000; 2017 $6,520 reclassed |
| **Steve** (Anthem {STEVE}, Blue Shield) | 2015 $11,815; 2018 $20,129: **about $31,900** | 2016–17 and 2019–22 reclassed ($103,136); 2018 partial and 2020–26 coded to 514000 |

**Both partners had health insurance left in dairy expense in some years, and Steve's
uncorrected amount is larger.** That cuts against a one-sided reading of A-76. It also confirms
the books were corrected inconsistently, year to year.

## 6. United of Omaha, corrected

- **Treated as Steve's:**
  - reclassified 2016 ($4,126.20) and 2017 ($2,063.10);
  - coded to him 2018 ($4,126.20);
  - that is **$10,315.50**.
- **Left in dairy expense:** 2013, 2015, 2019, 2020, 2021 (×2) and 2022. That is **7 × $2,063.10 =
  $14,441.70**. 2012 is INDETERMINATE.
- **All three Demand-13 checks (2019, 2020, 2022) are in the uncorrected group.** This corrects
  "8 × $2,063.10 = $16,504.80" in the partner-draw memo §6 and A-84.
