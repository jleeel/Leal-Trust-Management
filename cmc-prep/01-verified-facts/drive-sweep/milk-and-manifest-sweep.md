# ATTORNEY WORK PRODUCT — PRIVILEGED & CONFIDENTIAL
## Prepared in anticipation of litigation — Leal v. Garabedian (Tulare County Superior Court, Case No. VCU327028)
## Drive Sweep Report: Milk Statements + Master Manifest (Agent territory: milk statements folder; full-tree manifest; root-level orphans)

- Sweep date: 2026-08-18 (all Drive reads performed this date; live-state re-checks same date)
- Source Drive: jaceleal@gmail.com, tree rooted at folder "Leal Trust Administration Litigation" (drive_id `1OPEaGuRzWRj8tXC8qmeV4qbwWUMYpIVW`)
- Companion file: `master-manifest.csv` (this directory) — 1,650 rows: path, drive_id, mimeType, modifiedTime, sizeBytes
- Method: recursive enumeration via Drive API listing (`parentId` queries, paged); every folder listed to exhaustion; content reads limited to this agent's territory (milk statements + orphans outside the other three agents' territories)

---

# PART 1 — MILK STATEMENTS (folder `1y-xw9HRGCmHwvsCQSyWk8te6sXsBBlsQ`, 12 PDFs, all read)

## 1.1 Identification

All 12 PDFs are **Land O'Lakes, Inc. member milk settlement statements** for **Farm No. 43627, Payout No. 4362701**, addressed to **"MANUEL C. LEAL & SON, 7027 AVENUE 208, TULARE, CA 93274"** — i.e., issued to the **partnership**, not to any individual or trust. Coverage is a continuous 12-month run: **April 2025 through March 2026** (one statement per month). Statement anatomy: FMMO component pricing (butterfat/protein/other solids/PPD), CA quota SNF payment, premiums, then a two-column ADVANCE/SETTLEMENT deduction schedule, mailbox price, and YTD totals.

## 1.2 Monthly extract table

| Period | Milk (lbs) | Gross milk revenue | CAPITAL RETAINS | Net deposit | Payment # / notes |
|---|---:|---:|---:|---:|---|
| Apr 2025 | 4,093,676 | $782,136.03 | $4,093.68 | $314,448.18 | pmt 874127 (5/16/25) |
| May 2025 | 4,280,271 | $822,531.37 | $4,280.27 | $343,886.44 | pmt 876739 |
| Jun 2025 | 4,156,288 | $804,060.73 | $4,156.29 | $350,124.92 | pmt 880439 |
| Jul 2025 | 4,299,839 | $848,099.06 | $4,299.84 | $358,978.75 | pmt 885235 |
| Aug 2025 | 4,168,265 | $823,795.24 | $4,168.27 | $363,978.89 | pmt 888906 |
| Sep 2025 | 3,978,039 | $759,977.75 | $3,978.04 | $288,976.39 | pmt 892566 |
| Oct 2025 | 3,986,206 | $721,975.24 | $3,986.21 | $0.00 | pmt 896219; DEFERRING ADVANCE $243,748.88 + DEFERRING FINAL $315,637.62 (payment deferral election) |
| Nov 2025 | 3,920,527 | $691,939.26 | $3,920.53 | $0.00 | pmt 899135; DEFERRING $236,303.50 + $293,724.06 |
| Dec 2025 | 4,228,318 | $707,493.42 | $4,228.32 | $315,341.05 | pmt 902899; DEFERRING ADVANCE $226,427.28 |
| Jan 2026 | 4,136,611 | $616,890.54 | $4,136.61 | $239,038.38 | pmt 906168; BASE ASSESSMENT −$39,241.65; forward contract +$7,178.88 |
| Feb 2026 | 3,710,402 | $604,941.07 | $3,710.40 | $201,045.65 | pmt 909794; BASE ASSESSMENT −$31,560.30; forward contract +$4,105.42 |
| Mar 2026 | 4,141,177 | $767,696.65 | $4,141.18 | $351,073.18 | pmt 914059; forward contract +$1,132.91 |
| **TOTAL (12 mo.)** | **49,099,619** | **$8,951,536.36** | **$49,099.64** | — | — |

Notes: (a) Oct–Dec 2025 "DEFERRING" lines are LOL's milk-check deferral program (cash pushed into the next tax year); the deferred sums re-appear as January-cycle cash. (b) Jan–Feb 2026 "BASE ASSESSMENT" charges (−$39,241.65, −$31,560.30) are LOL base-program over-base assessments. (c) Net deposits are after ALL deductions including two recurring Farm Credit West assignments of **$61,914.90 + $52,500.00 every month** and the STANDARD ADVANCE offset.

## 1.3 Standard monthly deduction schedule (per cwt unless noted)

NDPO $0.05 · Hauling $0.53 · Variable hauling $0.0563 · **CAPITAL RETAINS $0.1000** · Milk & Dairy Food Safety $0.0013 · Quota assessment $0.0385–0.039 · Dairy Council $0.012 · CA Milk Advisory Board $0.10 · CA assessment $0.01 · plus fixed Farm Credit West assignments ($61,914.90 and $52,500.00 per month).

## 1.4 The retains question (defense claim of "unpaid retains"; Settlement ¶9's $3,000/yr "milk retentions" for Hazel)

1. **Every one of the 12 statements withholds CAPITAL RETAINS at $0.1000/cwt** — $49,099.64 total for Apr 2025–Mar 2026 (arithmetic check: 490,996.19 cwt × $0.10 = $49,099.62; the $0.02 delta is monthly rounding).
2. **Whose account the retains credit:** the statements themselves name no individual — retains are withheld at the **farm level (Farm 43627)** and post to the cooperative **patron equity account 2017201**, which LOL's own equity statements title **"Manuel C. Leal & Son"** (the partnership). Nothing in the milk statements creates or credits any separate account for Hazel or her trust.
3. **No ¶9 line item:** there is no line in any statement paying, or earmarking, $3,000/year (or any amount) of "milk retentions" to Hazel. If the Settlement ¶9 payments were made, they were made outside the milk check; no record of such payments was located anywhere in this agent's territory (see § 4, Referenced-but-not-located).

## 1.5 LOL equity corroboration (LOL Equity folder + adjacent orphans, read from the LEAL DAIRY copies)

| Document (drive_id, LEAL DAIRY copy) | Key content |
|---|---|
| Equity Ownership Statement.pdf (`17HMc7O5B17i7Faew-c4EO1Ad6MX13-Fc`, 11/20/2013) | 2012 allocation $53,721.42 (cash $10,744.28); total equity ownership 11/20/2013 **$368,041.28** |
| Estimated Equity Revolvement.pdf (`1gEZJRaICMHLVfb5VwnYzRXBAQtufUq48`, 11/20/2013) | Patron 2017201; equity $368,040.28; **projected revolvements** 2017 $9,553 · 2018 $12,847 · 2019 $12,472 · 2020 $52,350 · 2021 $55,789 · 2022 $53,021 · 2023 $53,294 · 2024 $56,105 · 2025 $61,197 (cum. $366,629); expressly discretionary with LOL Board |
| Dairy Foods Patronage Statement.pdf (`13VYg8x6nOpGVehCMgG-GZiRo3qE2jgKt`) | 2012 patronage $0.213258/cwt × 251,908.11 cwt; account NOT then eligible for 100% cash or revolvement |
| Ag Service Patronage Statement.pdf (`1HT-0Wj7fF_nLCOQkgXGJD3LewqBQoxR7`) | Ag-services 2012 patronage $345.71 ($121 cash); total ownership $368,178.68 |
| 2017201 - Equity Statement.pdf (Taxes 2020 folder, `1XjMbsQhu4PwWXrA7Lx0AAWYZaZIAjRLN`, 1/27/2021) | **YE 12/31/2020 total equity $914,942.34 with ZERO 2020 activity** — no revolvement, no patronage paid that year (contradicts the 2013 projection of ~$52K revolving in 2020) |
| 2017201 Equity Statement.pdf (`1tpNvkMPMZDFPaYPaOQsr4VJbt0eABbID`, 8/23/2024) | DF Equity Target opened 2024 at $807,718.51; 3/7/2024 patronage allocation $101,524.87 with **only 20% cash ($12,816.69), 80% retained**; ending balance 8/23/2024 $896,426.69 + non-target $3,467.94 + $1 stock = **TOTAL $899,895.63, titled "Manuel C. Leal & Son"** |
| equity statement explained.pdf (LOL Equity folder, `1rQb2RBV_Umdc6hXsqXQB0qLjguPTob9s`) | LOL's generic SAMPLE explaining equity-statement mechanics: $2.75/cwt equity target; 100% cash patronage only when current equity ≥ target; revolvement only when current AND averaged equity ≥ target; glossary of A–S line codes. Useful as an interpretive exhibit |
| **Leal age retirement payouts.pdf** (`1z0GK1mZCS-6yZqdUu0tu5rHgl5khGlep`) | LOL **age-75 100% equity retirement checks**: Manuel C. Leal — $86,534.70 (2/24/2005), $12,541.61 (4/7/2005, LOL #2041468), $5,800.81 (4/6/2006), $29,088.18 (2/22/2007), $14,732.93 (4/5/2007); **Hazel Leal — $137,197.24 (6/21/2007)**, letter stating her "equity ownership … is now redeemed in full." Total redeemed 2005–2007 ≈ $285,895.47. Also contains an image of Hazel's CA driver license (DOB 4/16/1932) — PII, handle accordingly |

**Synthesis for the retains defense:** (i) Hazel's personal LOL equity was redeemed **in full** by age-retirement check of $137,197.24 in June 2007; (ii) all post-2007 retains and retained patronage accrued to the **partnership's** patron account 2017201, which grew $368K (2013) → $914,942.34 (YE2020) → $899,895.63 (8/23/2024); (iii) the 2013 projection of ~$50K+/yr revolvements for 2020–2025 evidently did not occur (zero activity in 2020; balance still ~$900K in 2024; revolvement is Board-discretionary); (iv) patronage since at least 2024 pays only 20% cash. The client's own valuation models (below) carry "LOL Equity" as a partnership asset — $719,108 (2018–mid-2023 models), $982,000 (9/23/22 model), $899,895 (12/12/23 onward).

---

# PART 2 — MASTER MANIFEST (tree rooted at `1OPEaGuRzWRj8tXC8qmeV4qbwWUMYpIVW`)

## 2.1 Totals

- **1,650 Drive items**: **140 folders + 1,510 files**, aggregate reported size **1,599,177,594 bytes (~1.49 GB)**. CSV: `master-manifest.csv` (1,650 data rows + header; zero parse errors; **zero duplicate drive_ids**).
- Root contains exactly **5 folders and no loose files**: LEAL DAIRY · Trust Administration · Leal Trust/Partnership · milk statements · Land Acquisition.

| Top-level branch | Files | Folders | Size (MB) |
|---|---:|---:|---:|
| LEAL DAIRY (`18iKM4vcGn84IOuGl6qyGdJ0gSDRY87ih`, created 2026-08-18) | 760 | 67 | 768.0 |
| Trust Administration (`17dgZhyfw2JmHsgD41Fq7MeZ_yGOzgnx_`, 2026-08-02) | 712 | 67 | 756.2 |
| Leal Trust/Partnership (`1cggIfIJeCJTj3YY7WTXxQOxXoVfWBYF8`) | 23 | 1 | 0.1 |
| milk statements (`1y-xw9HRGCmHwvsCQSyWk8te6sXsBBlsQ`) | 12 | 0 | 0.8 |
| Land Acquisition (`1vwHwHrRvMxcpOCbyxeX1kGaABI4HzpCN`) | 3 | 0 | 0.0 |

- File types: 1,292 PDF · 120 XLSX · 36 DOCX · 23 Google Docs · 9 DOC · 8 XLS · 8 PNG · 6 octet-stream (QuickBooks/OFX) · 3 JPG · 2 Google Sheets · 2 CSV · 1 EXE.
- **Path caveat:** the folder titled `Leal Trust/Partnership` contains a **literal slash in its Drive title** — in the CSV `path` column it is ONE folder (drive_id `1cggIfIJeCJTj3YY7WTXxQOxXoVfWBYF8`), not two nested levels. `modifiedTime` is date-only for rows transcribed in later enumeration passes.

## 2.2 Duplicate-tree finding

**LEAL DAIRY is a same-day re-upload that duplicates the Trust Administration financial tree.** `LEAL DAIRY/LEAL TRUST PARTNERSHIP FINANCIALS/**` (folder created 2026-08-18, day of sweep) mirrors `Trust Administration/LEAL TRUST PARTNERSHIP FINANCIALS/**` (created 2026-07-31) file-for-file — identical names, byte sizes and content modifiedTimes, but **distinct drive_ids** (both copies fully manifested; 0 shared IDs). LEAL DAIRY additionally holds ~50 loose dairy-operations files at its root (budgets, permits, feed/silage calculators, SCC bonus, time cards) that have no Trust Administration counterpart, plus the three high-relevance root orphans read below.

## 2.3 ⚠ PRESERVATION FLAG — file deleted from Drive mid-sweep

**`important numbers.xlsx` (23,583 bytes, modifiedTime 2026-07-06T23:15:15Z) was present in BOTH trees at enumeration (~11:45–11:52 UTC today) and was GONE from Drive when read was attempted later the same session.** Both copies now return "not found" by ID (LEAL DAIRY copy `1vacOZpTJl2BCbl1IjKnjHSB-y5hkMGrr`; Trust Administration copy `1BPwL7RG9QmC0zsdbxnV3WPCIsTP4S9V0`), title search finds nothing, and a live re-listing of the LEAL DAIRY financials folder shows 22 files where 23 were manifested. Because a moved file keeps its drive_id, "not found" indicates trash/permanent deletion, not a move. Its contents were never read and are unknown. **Counsel should advise the client immediately regarding litigation-hold/preservation obligations and restore the file from Drive trash if possible.**

## 2.4 Orphans found and READ (high-relevance items outside the other agents' territories)

### A. Trust Administration root (loose PDFs)

**`2026-7-2 BMO Atty Cunningham Ltr.pdf`** (`1nnHz4PJtMz7wv-6b1GGwpV-0CT7Xq4we`) — Ormonde Rascon (Brandon M. Ormonde) to Niki Cunningham (Whitney Thompson & Jeffcoach), July 2, 2026, re *Manuel Stephen Leal v. Ashley Garabedian, et al.*, **TCSC Case No. VCU327028**. Monetary settlement offer delivered "concurrent with" a new CCP § 998 offer:
- **Total $5,705,257.43** to purchase the Hazel J. Leal Revocable Trust's interest in the Manuel C. Leal & Son Dairy Partnership + trust real property under the 2017 Settlement Agreement/TIC Agreement, with Civ. Code § 1542 release.
- Principal **$4,700,000** = **$1,046,587.50 partnership** (per Moss Adams appraisal) + **$3,653,412.50 real property** (applying the 90% contractual buyout discount + 25% minority-interest discount, "consistent with … Stan Xavier … 2017").
- **Bypass income $327,427.02** ("all earned but undistributed income from the Manuel C. Leal Bypass Trust through Hazel's date of death") + **accrued interest $677,830.41** (4%/yr "from the dissociation to present," offered "while legally not required").
- Material condition: immediate **termination of all partnership-funded personal expenses and draws** for defendants; post-acceptance payments credited dollar-for-dollar. Open 30 days. (Page-2 header misprints "January 2, 2024" — template artifact.)

**`998 offer FINAL.pdf`** (`11VQh2jHIMvTnhVQr2bcIVZjoXcwrudYB`, Drive mtime 2026-07-02) — CCP § 998 Offer to Allow Judgment, *Manuel Stephen Leal v. Ashley Garabedian and Hazel Susan Leal, Successor Co-Trustees of the Hazel J. Leal Revocable Trust dtd 11/3/2008* (caption's case no. OCR-garbled "VCU3627028" = VCU327028). Offer: judgment ordering both sides to employ (1) **Stanley Xavier / Correia-Xavier** within 30 days to appraise defendants' **Real Property** interest ("the 652.02 acres" under the 12/7/2017 Settlement Agreement & Mutual Release and the TIC Agreement) as of **Hazel Leal's date of death**, with discounts, for sale to plaintiff; and (2) **Moss Adams** within 30 days to appraise defendants' **Partnership** interest as of DOD under the Settlement and Partnership Agreements, with discounts, for sale to plaintiff. **Date anomaly to resolve with counsel:** the proof of service is executed "January 3, 2018" (Georgia Davidson), yet the caption names successor co-trustees (post-death posture) and the 7/2/2026 letter announces a concurrent 998; the PDF may be a re-used 2018 template or a misdated 2026 service copy. Drafting slips: "OMRMONDE," "TIMOHTY," and plaintiff rendered both "MANUEL STEPHEN LEAL" and "STEVEN MANUEL LEAL."

### B. LEAL DAIRY root (loose files)

**`STEVE.HAZEL ADJUSTMENT.xlsx`** (6/27/2017) and **`STEVE.HAZEL ADJUSTMENT complete.xlsx`** (7/31/2017) — the client-side capital/land reconciliation model, 12/31/2014 values:
- Parcel table: 574.02 assessed acres; land $13.2M gross / $9.75M net of improvements; land debt $3,360,121; land equity $6,389,879; **Hazel's 12.5% land interest $798,734.88**; long-term debt schedule (FCW herd $1,031,020, quota $303,624, etc.).
- Partnership appraisal: **Reddington 100% equity $6,642,573**; "debt-adjusted" (land debt removed) $10,002,694. The earlier file splits equity **Hazel 37.5% / Steve 55% / Trust 7.5%** ($3,751,010.25 / $5,501,481.70 / $750,202.05); the "complete" version uses Hazel 37.5% / Steve 62.5% of the $6.5M Reddington-based figure.
- Income adjustment 1997–2015: total partnership income $6,598,525; **12.5% allocated to Hazel = $824,815.63**; est. tax adjustment $22,572.
- 12/31/15 capital accounts: Manuel $2,365,810 vs Steve $3,115,071 — a **$749,261 discrepancy attributed to "personal expenses withdrawn from Manuel's account over the years."** After adjustments, **$52,982.63 owed by Steve to Hazel** to true up the accounts.
- Buyout scenario (12.5% LOC + 15% LOM per the 706): net partnership $1,813,642 + 12.5% land $798,734.88 + equity adjust $52,982.63 = **total price $2,665,359.50** (variant with ½ note: $3,105,332.00; 20-yr note @ 4.5% = $22,311.56/mo).

**`APN DESCRIPTIONS.xlsx`** (`1dbN7hiHHGU-ZRixVqMqRbGri9-8tl0sf`, mtime 8/21/2023) — refined successor to the above: **652.33 assessed acres (582.9 farmable)** matching the 998 offer's "652.02 acres" description; debt-adjusted equity Hazel 37.5% **$3,751,010.35** / Steve 62.5% $6,251,683.91 (total $10,002,694.26); "HAZEL BUYOUT" tab: 37.5% less 12.5% LOC less 15% LOM = net partnership $2,789,813.95 + 12.5% land $798,734.84 + $52,982.63 = **TOTAL PRICE $3,641,531.41**, 20-yr note @ 4.5% ($22,063.74/mo); Hazel's pre-discount total $4,655,710.44. Embedded 7/14/2014 letter to Central Valley RWQCB (parcels under the Dairy General Order), signed **Jace Leal, Manager**.

**`1773591.pdf`** (`1j9hGok-KE1e8pqP5l3LXL5Hk4Fvfpjxq`, 1.9 MB) — public LLNL technical report LLNL-TR-797179 (Esser & Deinhart, Nov 2020), "Anthropogenic Markers in Alta Irrigation District Water Supply Wells" (nitrate/groundwater study for Kings River Watershed Coalition). Read: title pages + Key Points + keyword scans; **zero mentions of Leal, the dairy, or its APNs** — background regulatory material (pairs with `well nitrate tests.xlsx` and the RWQCB letter). Balance of the 38-page public report not read (no case-specific content).

### C. LEAL DAIRY/LEAL TRUST PARTNERSHIP FINANCIALS (duplicate-tree copies read as orphans; identical files exist in the Trust Administration copy for the finance agent)

**`Partnership Income Summary.xlsx`** (`1vdNkNCnKlfT67LBsi6bpBWu4IpWZwj_3`, mtime 10/2/2025) — the accounting backbone of the 7/2/2026 offer:
- Bypass Trust (7.5%) income 2015–2022: **$327,427.02** — the exact "Bypass Income" figure in the offer letter. Hazel net income 2015–2022: **$706,290.12**. "Due to Hazel 2015–2022 … TOTAL $1,033,717.15."
- Full capital-account roll-forward 1/1/2015 → 12/31/2022: total capital $4,992,459 → **$9,201,369**; 3/25/2015 transfer out of Manuel/Hazel account −$1,925,995 (to Steve $1,540,796 + Bypass $385,199); 12/31/22 balances Manuel/Hazel $2,730,705 (29.68%) / Steve $5,678,038 (61.71%) / Bypass $792,626 (8.61%) vs. target 37.5/55/7.5 splits of $3,450,513 / $5,060,753 / $690,103; **"(Excess Draws)/Amounts Receivable": Manuel/Hazel −$719,809, Steve +$617,285, Bypass +$102,523**.
- **Hazel's income is tracked only through 9/22–9/23/2022 (2022 income split "1/1/22–9/22/22" vs "9/23/22–12/31/22") — corroborating a date of death of approximately September 22, 2022** (consistent with the Moss Adams/JHA "Sept 2022" DOD valuation reports manifested in the Hazel Trust Admin folders, and with ~3.8 yrs of 4% interest ≈ $677,830 in the offer).
- Later years: 2023 income −$888,608 (loss); 2024 +$2,026,658; 2015–2024 total $7,093,321.

**`equity estimate Current.xlsx`** (`1dwBLlvoyZ4UsdMkCFNSqObxZT66e83G6`, mtime 4/21/2026, 234 KB) — the client's running buyout-valuation model: **20 dated snapshots from 6/1/2018 to 4/1/2026** (6.1.18, 12.12.20, 12.20.20, 3.18.21, 2.16.22, 9.12.22, **9.23.22**, 6.23.23, 7.7.23, 12.12.23, 7.5.24, 8.27.24, 10.3.24, 1.22.25, 2.27.25, 4.25.25, 8.1.25, 10.1.25, 1.21.26, **4.1.26**). Read in detail: 6/1/18, 9/23/22, 4/1/26 sections + the LOL-equity line across all 20 (other snapshots share the same template; not separately transcribed).
- **9.23.22 snapshot (≈ DOD)**: assets $22,244,886 (incl. LOL Equity **$982,000**, quota 2,049 lb @ $349, 553.87 open acres @ $18K, pistachios/almonds, herd $3.99M); debt $3,893,835; adjusted net $13,533,900.11; **37.5% = $6,881,644.13**, less 12.5% LOC and 20% LOM → **discounted $4,817,150.89**; Hazel payment modeled $25,846–$30,535/mo; Hazel income $859,795; bypass income $356,049.
- **4.1.26 snapshot (current)**: assets $30,960,820 (adds **LOL BASE 17,500 @ $200 = $3,500,000**; LOL Equity $899,895; herd repriced $3,500/cow); debt $1,930,628; adjusted net $22,362,319.78; **37.5% = $10,886,322**, less 12.5% LOC and 30% LOM → **discounted $6,667,872.23**. Side "Appraisals" panel: Dairy $4.0M/Land $7.5M/Feedlot $1.7M/Partnership $6,642,573 → 37.5% with per-asset discounts (25/20/30/25%) = **$5,689,473.66** — tracking within ~$16K of the 7/2/2026 offer's $5,705,257.43 total. Loan-calculator tab models a $3,561,646.81 note against a $4,817,150.89 "Total Buyout."
- LOL equity carried as a partnership asset in every snapshot: $719,108 (2018–2023) → $982,000 (9.23.22 only) → $899,895 (12.12.23 onward).

**`Leal age retirement payouts.pdf`** and **LOL Equity folder** — see Part 1.5. (A second copy, `Leal age retirement payouts (1).pdf`, also exists deeper in both Trust Administration subtrees.)

### D. Land Acquisition folder (3 Google files, all read)

**`160-Acre Acquisition Strategy & Term Sheet`** (GDOC `1hx9lfKBHiyLEPpaW9_ewryiHuMMme1--9WvutTegnMc`) — "PART I: INTERNAL STRATEGY & OPERATIONAL WAR ROOM — CONFIDENTIAL: Leal Partners & Legal Counsel Only." Because of "the ongoing § 998 buyout litigation and active obstruction by minority stakeholders (H. Susan Leal and Ashley Anderson Garabedian)," the partnership "**cannot** take title"; plan is a **drop-down LLC ("Leal Land Holdings, LLC") capitalized by Jace, Steve, and Jordan Leal**, holding title and leasing back to the dairy; "Brandon" (Ormonde) to draft an aggressive buy-sell. Term sheet: 160 ac Tulare County @ $21,000/ac = **$3,360,000**; $1,176,000 (35%) cash down; **seller carry $2,184,000 @ 4.08% AFR**, 20-yr am, $160,000/yr payment, 5-yr balloon (~$1.79M) with 24-mo extension @ 6.08%; seller gets 1st DOT; companion 3–5 yr lease proposal on seller's adjacent 160 ac. Holding cost $204,960/yr; inputs $192,000/yr to be floated on an FSA direct operating loan; EQIP/REAP grants; FSA guaranteed loan for balloon refi. **Counsel note:** document contemplates acquiring an opportunity adjacent to partnership operations through an entity excluding the trust — evaluate partnership-opportunity/fiduciary exposure and privilege treatment (it is addressed to "Leal Partners & Legal Counsel Only").

**`Leal Land Holdings` P&L (GSHEET `1tWyCOpuB5ay5B2sw6nPrb9kgTvQG9VD8SmU1BC3lq4Y`)** — 4,800 t @ $75 = $360,000 revenue; inputs −$192,000; RE expenses −$216,960; rent +$12,000; **net −$36,960/yr**.
**`Leal Land Holdings - P&L (33 Tons…)` (GSHEET `1s05YngoS1vg0-jh4myWR4189-tQy1bsoXEZ8-1B2VM0`)** — 5,280 t @ $75 = $396,000; adds $40,000 feed-line interest ($500,000 draw @ 8% for the down payment); **net −$40,960/yr**.

### E. Orphans identified but NOT read (low relevance, manifested only)

~45 dairy-operations files loose in LEAL DAIRY root (hay/silage/feed calculators, SCC bonus, time card, vacation tracker, Edison/solar, 2008 annual report, Rio Blanco base transfer, well nitrate tests.xlsx, feed truck.jpg, LEAL Budget Current.xlsx (mtime 5/2/2026 — flag for later if operations spending becomes an issue), Leal Farms.xlsx, Wells to Fields DATA.xlsx). Cross-territory items (inner Trust Administration subfolders, Leal Trust/Partnership Google Docs — 23 buyout/998 drafts dated Jan–May 2026, tax/banking folders) were manifested but deliberately not read per territory assignments.

## 2.5 Cross-territory retains evidence flagged for the other agents (manifested, not read by this agent)

Equity Accounts 1997-2015.pdf; equity accounts.pdf; equity 1992-1993.pdf; equity 1997.pdf; Equity Accounts 1997-2015 with 1993.pdf; Manuel Leal & Son Dairy Capital Analysis 8-3-2017.pdf; LOL 1099-PATR (2015/2016/2020/2022/2024); LOL DPAD (2017/2018/2021); 2017.10.06 Hazel Leal Mediation Brief; 2026.01.21 Garabedian-Leal Mediation Brief; Hazel draws files; Moss Adams Adjustment Calcs; STEVE.HAZEL PERSONAL EXPENSES.xlsx; Business Valuation_MA_Sept 2022_FINAL.pdf; Real Property Appraisal_JHA_Sept 2022 (Prorata Allocation).

---

# 3 — REFERENCED-BUT-NOT-LOCATED

| Item | Referenced by | Search result |
|---|---|---|
| LOL equity statements for 2014–2019, 2021–2023, 2025–2026 | Statements exist only for 2013 (set), YE2020, and 8/23/2024; trajectory has gaps | Not in tree |
| Milk settlement statements before Apr 2025 / after Mar 2026 | Settlement ¶9 dispute spans earlier years; only 12 months present | Not in tree |
| Records of Settlement ¶9 $3,000/yr "milk retentions" payments to Hazel | Settlement Agreement ¶9 | No payment records found in this territory |
| LOL revolvement/non-revolvement records 2017–2025 | 2013 Estimated Equity Revolvement projected ~$50K+/yr from 2020; YE2020 shows zero activity | Only the projection + YE2020/2024 statements |
| 1099-PATR for 2023 and 2025 | 2015/2016/2020/2022/2024 copies exist in tax folders | Not located |
| CDFA quota certificates | Quota (2,049 lb SNF) valued in every equity model and assessed monthly on milk checks | No certificates in tree |
| `important numbers.xlsx` content | Manifested in both trees this morning | **Deleted from Drive mid-sweep** (see § 2.3) |
| Conformed/filed 2026 CCP § 998 offer | 7/2/2026 letter says a 998 was delivered "concurrent"; `998 offer FINAL.pdf` carries a Jan 3, 2018 proof of service | Only the anomalously-dated PDF + unsigned GDOC drafts |
| Fully signed dairy/land lease | Only `lease agreement unsigned.pdf` and `LEASE AGREEMENT 3.6.13.docx` in the financials folders | No executed copy |
| Seller identity/APN for the 160-acre acquisition | Term sheet names no seller or parcel | Not in tree |

# 4 — UNREADABLE / NOT-MACHINE-READABLE

| File (both tree copies where applicable) | Why |
|---|---|
| `LEAL DAIRY/dmbcalculator.exe` (28,672 B, 2011) | Windows executable |
| `…/LEAL TRUST PARTNERSHIP FINANCIALS/Manuel Leal AJEs.QBJ` (×2, 126,536 B) | QuickBooks journal binary (an XLSX sibling of the same AJEs exists for the finance agent) |
| `…/Taxes 2013/2013 Taxes/QB_Manuel_Leal_Dairy 10.5.2009 (…Acct Transfer…).QBX` (×2, 18.4 MB) | QuickBooks accountant-transfer binary |
| `…/Taxes 2025/2021_RAM_2500_Transactions_2023-08-01_2026-07-14.ofx` (×2) | OFX banking data (text-ish but connector-unsupported) |
| `important numbers.xlsx` (×2) | **Deleted from Drive between enumeration and read** — see preservation flag § 2.3 |
| `__MACOSX/Leal Dairy & Feedlot Appraisal_Valuation Reports_2022` (×2) | Zip-artifact folders, verified empty |
| Images (`feed truck.jpg`, Correia Xavier `dairy facility.png`/`Heifer Ranch.jpg`/`heifer ranch.png`/`LEAL APN MAP.png`, `Dustin Snyder Email.png`) | Readable as images but not read: low relevance or other agents' territory (Correia Xavier / Hazel Trust Admin folders) |

# 5 — Coverage disclosures

- All 12 milk statement PDFs: read in full.
- LOL Equity folder (5 PDFs) + Taxes 2020 equity statement + age-retirement PDF: read in full.
- `STEVE.HAZEL ADJUSTMENT` (both), `APN DESCRIPTIONS.xlsx`, `Partnership Income Summary.xlsx`, BMO letter, 998 offer, all 3 Land Acquisition files: read in full.
- `equity estimate Current.xlsx`: sectional read (3 of 20 snapshots verbatim + one tracked line across all 20; remaining snapshots are the same template at intermediate dates — not fully transcribed).
- `1773591.pdf`: identification read only (title/Key Points + keyword scans; no Leal content; 38-page public LLNL report not read in full).
- Enumeration: every folder in the tree listed to exhaustion (no pagination token left unfollowed); two `__MACOSX` folders verified empty; live re-verification performed only for the LEAL DAIRY financials folder (which surfaced the § 2.3 deletion). The manifest is a point-in-time snapshot of 2026-08-18 morning UTC.
