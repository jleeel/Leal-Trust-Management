# Steve's "temporary loans" to the partnership, and the $100,000 (tested 10/1/2026)

**ATTORNEY WORK-PRODUCT SUPPORT — PRIVILEGED & CONFIDENTIAL.** This tests a client explanation
against the documents. It is not a finding, and it states no legal conclusion.

**The client explanation** (Jace, 10/1/2026; CLIENT-ATTESTED): "The 100,000 was a repayment of a
temporary loan to the partnership to maintain ability to pay bills. Robyn Esraelian was stalling
our ability to pull funds from our operating line with farm credit. You can see evidence of this
in emails."

The explanation answered A-60's question about "the $100,000 check to Steve on 9/30/2014."
**That description was wrong** (§1).

## 1. Correction: there was no $100,000 check on 9/30/2014

The workspace stated in five places that "check #23074 to Steve Leal, 9/30/2014" was for
$100,000. Those places were:
- A-60;
- the A-60 10/1 update;
- gmail-extract §2;
- trust-admin-sweep §2.6;
- chronology row 2014-09-30 (repeated in delay-ledger line 260).

The error came from a text extraction that misaligned the register's columns. I re-parsed
"personal steve.pdf" (Drive `1wVz1Won1T_ovfpqPGhBB71qOKGoEkPTA`, account 515000 Personal-Steve,
1999–11/1/2016) with each row tied to its amount. The running balance ties out on every one of
the 230 rows (0 breaks). It shows:

| Date | Type | Memo / split | Amount | Balance |
|---|---|---|---|---|
| 9/30/2014 | Check 23074 | Steve Leal | **−$126.00** | −16,336.04 |
| 12/31/2014 | General Journal, FRAZE | "TO CLOSE OUT ACCOUNT" / 102000 | −$3,657.36 | −21,627.37 |
| 12/31/2014 | General Journal, FRAZE | "TO RECLASS STEVE LEAL WI…" / 512000 · Capital Contribution | **−$100,000.00** | −121,627.37 |

**Frazer's own adjusting-entry report confirms the third line.** "Accountant Changes
12.31.14.pdf" (Drive `1f5JGW5GYY4weVMoBqbfqETX3Llgz_VNp`; duplicate
`1RgKBfuN2P0JTGiiwYf0aP2lBMlA1Qzpa`), p. 36 of 37, entry 202:

> "Added Journal Entry FRAZE 12/31/2014 · Adjusting Entry yes · Capital Cont. - Steve 100000.00
> TO RECLASS STEVE LEAL WITHDRAWALS · Personal - Steve 100000.00 TO RECLASS STEVE LEAL
> WITHDRAWALS"

**What it means (calc).** The −$100,000 in 515000 is a debit to Personal-Steve, so the
offsetting credit went to 512000 Capital Cont.-Steve. Before year-end, therefore, a $100,000
payment to Steve was booked *against his capital-contribution account*: that is how a
contribution or loan is returned. Frazer's adjustment moved it to "withdrawals." Steve's total
capital is the same either way. Only the label changed, and the label is what puts $100,000
into FY2014 "Personal" withdrawals (Steve $120,155 vs. Manuel $7,333; A-1).

**Not yet located:**
- The 2014 bank transaction itself: its date, the check or transfer, and the payee account.
- The 512000 ledger for 2012–2014.

**Grade:** the reclass is **SUPPORTED**. The underlying 2014 payment is **INDETERMINATE**.

## 2. How the dairy booked Steve's loans, in Frazer's words, sent to the other side

On 2/22/2018, Mike Edwards (Frazer) wrote to Aaron Garabedian, cc'ing Robyn Esraelian, Brandon
Esraelian, Tim Thompson, Niki Cunningham and Michael Johnson. This was **not privileged**; it went
to opposing counsel. Gmail `1602be0a88bae639`, quoted in Edwards's 8/2/2018 forward to Jace:

> "3. Steve's capital contributions are for money Steve loaned the business to cover bills. Jace
> uses this account to post the money Steve put in and when Steve is reimbursed the payments are
> also ran through this account. I think the current balance owed to Steve is ~$70,000. When we
> prepare the F/S I will pull the detail together for the loan activity."

This matches the 2014 entry exactly: a reimbursement run through 512000, then reclassed by
Frazer. **Grade:** the *practice* (loans booked in 512000, repayments run through the same
account) is **SUPPORTED** by the accountant's contemporaneous statement. That **this particular
2014 payment** repaid a loan is **NOT ESTABLISHED**. No 2014 inflow has been tied to it.

**Where the 2014 repayment's inflow might be** (from the printed statements, S-4
`1O7OGL798JcaTXginVNMIUgKtNV-ckK0l`):
- FY2014: no capital-contribution line.
- FY2013: none.
- **FY2012: "Capital contribution 126,028," of which Steve $125,987.**

The FY2012 contribution is the nearest documented inflow large enough to cover a $100,000 return.
**The link is an inference, not a finding** (INDETERMINATE). The 512000 detail for 2012–2014
would settle it.

## 3. The Esraelian "stalling" evidence is real, but it is from 2017–2018, not 2014

Every document found on Hazel's side withholding or conditioning operating-line draws dates
from **September 2017 to June 2018** (all read in full, 10/1/2026):

| Date | Event | Source (Gmail thread) | Privilege |
|---|---|---|---|
| 9/18–19/2017 | FCW renewal documents await Hazel's signature, due 10/1/2017. Esraelian: "The form is incorrect. I have notified Ryan." | `15ea026a2587b8a5` | non-priv (Esraelian msg) |
| 10/20/2017 | Griswold drafts a "Partnership Loan Approval Agreement" for Esraelian | `15f3bc24ecfe3e5e` (att. "2017.10.20 Partnership Loan Approval Agreement.pdf", not opened) | [PRIV] |
| 11/2/2017 | Jace: "We need to make a loan advance of $50,000 for November." 11/3: "Robyn sent a form to Ryan Camara at Farm Credit… we will use that for now." | `15f3bc24ecfe3e5e` | [PRIV] |
| 11/3/2017 | Esraelian: "I have received a withdrawal request from Ryan Camara… for $100,000. Ryan has asked for Hazel's signature. I cannot advise Hazel to sign without more information." Jace answers the same day: A&M Livestock cows $46,430, property taxes ~$28,000, TID ~$10,000; "~$96000 of principal is paid toward these loans each month"; "home care nurse expenses for Hazel have totaled ~$138,000 for this year to date." | `15f9daabdb9b5d4f` | non-priv |
| 11/8/2017 | Aaron Garabedian's accounting requests, item 1: "Narrative of GL account # 512000 - Capital Contribution Steve… two entries with a memo of 'Temp Loan to Partner'. One transaction is for $70,000 and the other is for $100,000. Source of funds and use of funds." | quoted in `15fa1ce3b9f72277` | non-priv |
| 11/9/2017 | Esraelian: Hazel "will agree to sign this request at this time" but "will not sign future requests… in the event Steve fails to provide the information requested." Signature conditioned on written confirmation of answers by 11/17. Johnson: "The bills for the dairy cannot be paid until we receive the funds from the advance." Esraelian (later): "Your continued threats to take away or to stop paying Hazel's caregivers is causing Hazel severe emotional distress." | `15fa1ce3b9f72277` (att. "Steve Temp Loan to Partner.pdf", not opened) | mixed (Esraelian/Johnson-to-Esraelian msgs non-priv; Johnson↔Jace [PRIV]) |
| 11/9/2017, 9:44 AM PT | **The message behind the "threats" accusation** (lealdairy@gmail.com; seen 10/1/2026 in a client screenshot, not yet read natively). Leal Dairy to Esraelian, cc Johnson, Thompson, Cunningham, Brandon Esraelian, Aaron and Dale Garabedian: "When can we expect the signed authorization to arrive at Farm Credit? **I will not be able to make checks for the home care nurses until the funds are in the business checking account.**" Esraelian's 1:09 PM "continued threats" reply quotes this message. | screenshot `01-verified-facts/2017-11-09_lealdairy-to-esraelian-nurse-checks-email.png` | non-priv (sent to opposing counsel) |
| 11/9/2017 (draft) | "Response 11.9.17.docx": "Steve has made a temporary loan to the partnership for $170,000. The source is personal funds. If you remove the Frazer Journal Entries from the account the balance would show zero. The current total of temporary loans from Steve is $170,000." | Drive `1--NBmBDOT7CgW02vsECpqAdzJjm3bZN2` | client draft; whether sent is NOT ESTABLISHED |
| 12/27/2017 | Esraelian: "I'm not sure we are ready to give up the loan authorization issue yet… we will still want to have the loan authorization in place for Hazel's security." | `16099bc4ac9deb75` | non-priv |
| 2/22/2018 | Jace to Edwards (cc Johnson): "That is where I put the temporary loans that Steve made to the partnership. **Last month he paid himself back most of it and is currently owed $70,000.** He doesn't plan on doing that again in the future for obvious reasons." Edwards to Garabedian: §2 above. | `1602be0a88bae639` | Jace→Edwards: counsel to assess (Johnson cc'd); Edwards→Garabedian: non-priv |
| 6/15/2018 | Johnson: "Robyn is trying to reach out to Hazel on the $100,000 lending." Esraelian: "I'm trying to contact Hazel… I believe she is out of town." | `164047e526301ab2` | mixed |
| 6/19/2018 | Johnson to Esraelian: "The dairy is having severe cash flow issues right now… We really need to get the Morgan Stanley reimbursement or the loan approved today." Also: Steve "took a draw to pay the taxes and since the taxes turned out to be less he has returned the money", $50,000 deposited back so far. | `16418f57c7b5daa4` | [PRIV] forward; the quoted Johnson→Esraelian message is non-priv |
| 8/4/2018 | Jace to Ryan Camara invokes Settlement p. 4: "Steve's authorization to borrow $100k per month." | `1650688693ff6180` (chronology) | non-priv |

**Dates matter here.** Manuel was alive until 3/25/2015. In the targeted Gmail searches run
10/1/2026, no document gives Esraelian any role in partnership borrowing before September 2017.
The earliest Esraelian-related threads found are 2016 trust-administration letters (Gin).
**The 12/31/2014 reclass cannot be explained by Esraelian's 2017–2018 conduct.**

The client's account does fit a *different* $100,000. Per Jace's 2/22/2018 email, Steve repaid
himself "most of" the $170,000 in **January 2018**, leaving $70,000. That implies roughly a
$100,000 repayment (calc: $170,000 − $70,000). **The client may be describing the January 2018
repayment, not the 2014 reclass.** OI-80 asks the client to say which.

**Same-day sequence, 11/9/2017 (Pacific time; reconstructed from Gmail timestamps and the
screenshot):**

| Time | Who | What |
|---|---|---|
| 9:13 | Esraelian | Conditional approval |
| 9:23–9:32 | Johnson | Commits to answers by 11/17 and thanks her "for approving the credit request" |
| **9:44** | Leal Dairy | "nurses" message |
| 10:44 | Johnson to Jace, [PRIV] | "Remember Judge Broadman wants your hands clean… Let me be the bad guy on these communications" |
| 10:46 | Johnson to all | Restates it neutrally: "The bills for the dairy cannot be paid until we receive the funds from the advance" |
| 11:45 | Jace to Johnson, [PRIV] | "My Dad just isn't too excited about loaning the partnership to pay for nurses" |
| 1:09 PM | Esraelian | Will take the document to Hazel Friday, plus the "continued threats" sentence |

The approval had already been given 12 minutes before the "nurses" message was sent.

## 4. What does not reconcile yet (adverse rigor)

1. **Amounts by year.** The emails say $170,000 was outstanding in 11/2017, about $100,000 was
   repaid in 1/2018, and $70,000 was owed in 2/2018. The statements show contributions of
   $60,000 (2017) and $93,630 (2018), and a $60,000 *debit* to 512000 in 2019 (sweep §6). If
   all $170,000 came in during 2017 and nothing was repaid that year, FY2017 should show
   $170,000, not $60,000. One possible explanation: Garabedian's "$100,000 Temp Loan" entry may
   itself be the 2014 item still sitting in 512000. That would fit the draft's "If you remove
   the Frazer Journal Entries… the balance would show zero." But it cannot be squared with "the
   current total… is $170,000." **INDETERMINATE until the 512000 ledger is read.**
2. **Loan or capital?** No note, no interest, and the reviewed statements call these "capital
   contributions." The other side can say every repayment was a draw (kit Item 6 caution, and
   A-72).
3. **Self-repayment after the Settlement.** The January 2018 repayment came after the 12/7/2017
   effective date. Settlement ¶11 governs borrowing and partner loans, though its signature
   blocks are dated 2018 (memo §5.1). Whether repaying a pre-Settlement partner loan needed
   Hazel's approval is **for counsel (UNVERIFIED)**. Partly mitigating: Frazer disclosed the
   loan-and-repayment practice and the ~$70,000 balance to opposing counsel on 2/22/2018.
4. **Tone evidence cuts against us.**
   - [PRIV] Jace, 11/9/2017: "My Dad just isn't too excited about loaning the partnership to pay
     for nurses."
   - Non-privileged and in their file: Esraelian's "continued threats to take away or to stop
     paying Hazel's caregivers," and Jace's own 11/3/2017 tie between the advance and "home care
     nurse expenses for Hazel… ~$138,000."
   - Expect this used for a control or leverage narrative.
   - **Updated 10/1/2026:** the "threats" sentence answered a specific non-privileged message
     (11/9/2017, 9:44 AM, see the sequence above). Read both ways:
     - **Helps:** it states a cash-timing fact, not a refusal. The nurses were paid from
       partnership funds, and the partnership was waiting on a signature Hazel's side controlled.
     - **Hurts:** of all the dairy's bills, it singled out Hazel's caregivers. It was sent after
       the approval was already given. Johnson moved within the hour to take over the
       communications and restate it neutrally.
     - The same-day [PRIV] line shows Steve was able to bridge but unwilling to do it for the
       nurses. That would matter if privilege were ever lost, and it shapes deposition answers to
       "Could Steve have covered those checks?"
     - Esraelian's word "continued" implies other instances. Search lealdairy before any
       deposition (OI-81).

## 5. What helps

- **Contemporaneous, non-privileged disclosure.** The other side's CPA asked about the
  temporary loans in 11/2017. Frazer answered in writing on 2/22/2018 to Garabedian, Esraelian,
  Thompson and Cunningham. "Concealment" is hard to argue for a practice opposing counsel was
  told about eight years ago.
- **Hazel's side conditioned partnership borrowing on information demands** (11/3–11/9/2017,
  12/27/2017, 6/15–19/2018). The other side's own emails show why Steve's bridge money was
  needed.
- **A-1 symmetry (calc, from printed S-4 figures).** If FY2014 counts a $100,000 return of
  Steve's money as a withdrawal, a fair comparison counts the money Steve put in.
  - Over FY2012–FY2014, withdrawals were Steve $280,587 and Manuel $282,700.
  - Contributions were Steve $125,987 and Manuel $41.
  - **Net of contributions: Steve $154,600, Manuel $282,659.**
  - Excluding only the reclassed $100,000, Steve's FY2014 withdrawals were $67,503 against
    Manuel's $110,081.
  - These are arithmetic on printed figures. Whether the 2014 payment *was* a loan repayment is
    INDETERMINATE (§2).

## 6. To close it out (OI-80)

1. The **512000 Capital Cont.-Steve GL detail, 2012–2019**. Two copies already exist as Gmail
   attachments that the connector cannot open:
   - "512000 - Capital Cont. - Steve.pdf" (Edwards, 12/6/2017, thread `1602be0a88bae639`);
   - "Steve Temp Loan to Partner.pdf" (Esraelian, 11/9/2017, thread `15fa1ce3b9f72277`).
   Save both to Drive.
2. The 2014 payment's check image or transfer record (Citizens), and Steve's bank deposit of it.
3. Steve's bank records for the inflows: the 2012 $125,987, and the 2017 $70,000 and $100,000.
4. Whether "Response 11.9.17" was sent, and in what final form (Griswold file / Jace's sent
   mail).
5. The client's answer: is "the $100,000" the January 2018 repayment, the 2014 reclass, or
   both?

---

## 7. UPDATE 10/1/2026 (later the same day): the 512000 ledger and the Citizens register settle most of this

**New sources, each read in full:**
- **"Steve Temp Loan to Partner.pdf"** (Drive `1sf5rKftJWQsrm95oLqAaQxRVmjvaNzLB`; client-saved Gmail
  attachment from Esraelian's 11/9/2017 email). One page: QuickBooks "Transactions by Account,
  All Transactions," **512000 · Capital Cont. - Steve**, printed **10:27 AM 08/18/17**.
  - Someone has written "Send to Tim" on it and highlighted it; the writer is not identified.
  - **Defendants' side has had this ledger since at least 11/9/2017.**
- **"quickbooks citizens checking transactions since 2009.xlsx"** (Drive
  `1XhazEklYhxAH27FlpuY6IqHSMEZ1muvR`).
  - QuickBooks Account QuickReport, 102001 · Citizens Checking, 12/31/2009–9/30/2026, exported
    10/1/2026.
  - 33,364 transaction lines. The running balance ties on every line (0 breaks, calc).
  - **Limit:** a deposit with several offsetting accounts shows only "-SPLIT-". A Steve deposit
    inside a split deposit is invisible here. The 512000 ledger fills that gap through 8/18/2017.

### 7.1 The 512000 ledger, transcribed (debit = money to Steve; credit = money from Steve)

| Date | Type / No. | Memo | Debit | Credit | Balance |
|---|---|---|---|---|---|
| 5/31/2004, 1/31/2005 | GJ (MSW) | Transactions… | 5,936.00 | 5,936.00 | 0.00 |
| 2/1/2012 | Deposit | **LOAN** | | 25,000.00 | 25,000.00 |
| 2/16/2012 | Check 19538 | | 25,000.00 | | 0.00 |
| 8/23/2012 | Deposit | **Temporary Lo[an]** | | 50,000.00 | 50,000.00 |
| 8/29/2012 | Deposit 5293 | Deposit | | 40,000.00 | 90,000.00 |
| 10/3/2012 | Deposit | Deposit | | 10,000.00 | 100,000.00 |
| 1/1/2013 | GJ FRAZE | To tie out cap… (500000 Capital) | 125,987.00 | | −25,987.00 |
| 3/4/2013 | Check 21027 | Hay loan | 75,000.00 | | −100,987.00 |
| 4/11/2013 | Deposit | Deposit | | 80,000.00 | −20,987.00 |
| 5/1/2013 | Deposit | **temp loan** | | 50,000.00 | 29,013.00 |
| 5/16/2013 | Check 21283 | | 50,000.00 | | −20,987.00 |
| 5/22/2013 | Check 21288 | | 25,000.00 | | −45,987.00 |
| 8/12/2013 | Deposit | Deposit | | 20,000.00 | −25,987.00 |
| 10/17/2013 | Check 21844 | | 50,000.00 | | −75,987.00 |
| 10/31/2013 | Deposit | Deposit | | 50,000.00 | −25,987.00 |
| 12/31/2013 | GJ FRAZ | To tie to FRA… | | 25,987.00 | 0.00 |
| 2/13/2014 | Check 22327 | | 50,000.00 | | −50,000.00 |
| 3/15/2014 | Check 22468 | | 50,000.00 | | −100,000.00 |
| 7/2/2014 | Deposit | Deposit | | 50,000.00 | −50,000.00 |
| 10/2/2014 | Check 23248 | **Pay back Loan** | 50,000.00 | | −100,000.00 |
| 12/31/2014 | GJ FRAZE | TO RECLAS… (515000 Pers…) | | 100,000.00 | 0.00 |
| 6/30/2015 | Deposit 5686 | **TEMP LOAN** | | 100,000.00 | 100,000.00 |
| 7/9/2015 | Deposit 5692 | Deposit | | 50,000.00 | 150,000.00 |
| 10/6/2015 | Deposit 5371 | Deposit | | 20,000.00 | 170,000.00 |
| 12/31/2015 | GJ Frazer | RECLASS IN… (689000 Proc…) | | 88,025.87 | 258,025.87 |
| 1/1/2016 | GJ FZR-Y… | To close capit… (502000) | 258,025.87 | | 0.00 |
| **3/2/2017** | **Check 27872** | **Temp Loan P[ayback]** | **100,000.00** | | −100,000.00 |
| **4/25/2017** | **Check 28235** | **Temp Loan P[ayback]** | **70,000.00** | | **−170,000.00** |

Totals as printed: debits 934,948.87, credits 764,948.87, balance −170,000.00. Every check and
non-split deposit in the table matches the Citizens register by date, number and amount. The
8/29/2012, 7/2/2014 and 7/9/2015 deposits fall inside same-day "-SPLIT-" deposits there.

### 7.2 What it proves

**(a) The 2014 "$100,000" was the return of Steve's 2012 loans. SUPPORTED** (partnership GL plus
bank register).
- 2012: Steve put in $125,000 and took back $25,000, net **+$100,000**. Memos: "LOAN,"
  "Temporary Loan."
- 2013: $200,000 in and $200,000 out, net 0. Memo "temp loan."
- 2014: $50,000 in and $150,000 out, net **−$100,000**. Memo "Pay back Loan."
- Over 2012–2014, cash in equals cash out: **$375,000 each way** (calc).
- Frazer's 12/31/2014 entry moved exactly that net $100,000 into "withdrawals."
- **The FY2014 "Personal" excess in A-1 is Steve being repaid his own 2012 money.**
- Minor wrinkle: Frazer closed **$125,987** to capital at 1/1/2013 when the account held
  $100,000, then reversed the $25,987 difference at 12/31/2013. So the FY2012 statement's
  "capital contribution $125,987" overstates Steve's 2012 cash by $25,987.

**(b) The 2017 $170,000 were repayments TO Steve of his 2015 loans, not loans outstanding.
SUPPORTED.**
- 2015 in: 6/30 "TEMP LOAN" $100,000 + 7/9 $50,000 + 10/6 $20,000 = $170,000.
- 2017 out: 3/2 $100,000 + 4/25 $70,000 = $170,000.
- Frazer closed the 2015 loans to capital at year-end. That is why the account shows −$170,000
  in 8/2017. Jace's draft ("If you remove the Frazer Journal Entries from the account the
  balance would show zero") is **accurate**.
- **Correction to §3–§5:**
  - Garabedian's "Temp Loan to Partner" entries are these two 2017 *repayment* checks. Their
    memo is "Temp Loan P…," which the bank register gives in full as "Temp Loan **Payback**."
  - My reading that $170,000 was still owed in 11/2017 was wrong.
- **The client's "$100,000 repayment of a temporary loan" most directly matches check #27872,
  3/2/2017, "Temp Loan Payback," $100,000.** It repaid the 6/30/2015 "TEMP LOAN" of $100,000.

**(c) Esraelian cannot explain the $100,000 items. NOT SUPPORTED for 2012–2017.**
- 2012–2014 was Manuel's lifetime.
- On 6/30/2015, the day of the $100,000 "TEMP LOAN," the register also shows a **$150,000 Farm
  Credit feed-line advance**. Feed-line advances posted throughout 2015: 4/29, 6/5, 6/30, 8/3,
  8/11, 9/1, 9/12, 10/6, 11/2, 11/13 and 12/1. The line was being drawn.
- **What does fit the Esraelian account:**
  - **10/6/2017, $50,000 from Steve.** It came while the FCW renewal documents sat with
    Esraelian (due 10/1/2017; 9/19 "The form is incorrect").
  - **11/17/2017, $20,000 back to Steve ("Repay loan")** four days after a **$100,000
    deposit on 11/13/2017**. The amount and date are consistent with the advance Hazel signed
    for on 11/10.
  - The book balance was **−$111,560.43 just before that deposit** and **−$258,204.46 on
    11/28/2017** (calc from register). The cash squeeze was real.

**(d) The nurses were paid every week (OI-81 item 1). SUPPORTED at register level.**
- Weekly caregiver checks (504000 Medical-Hazel) went to Jennifer Sousa, Brailee Scoggin,
  Maria Trovao, Maria Cardosa, Brittany McGarrah, Rebecca Sousa and Carrie Alvarado.
- Check dates: 10/6, 10/9, 10/19, 10/25, 11/2, **11/9**, 11/16, 11/24, 11/30, 12/7, 12/14,
  12/15 and 12/28/2017. Checks #29306–29311 are **dated 11/9/2017**, the day of the "I will not
  be able to make checks for the home care nurses" email. They were written against a book
  balance of about −$155,000.
- Both ways:
  - No week was skipped, so the statement never stopped Hazel's care.
  - But the checks were written anyway, so the email overstated the constraint.
  - Clearing dates need the bank statements.

**(e) 🔴 New, adverse: $220,000 to Steve in 2018, coded as personal draws (A-73).**
- **1/13/2018, check #29635, $150,000**, 515000 · Personal-Steve.
- **6/1/2018, check #30321, $70,000**, 515000 · Personal-Steve. The balance afterward was
  $4,493.98.
- Jace's 2/22/2018 email calls the January check repayment of "most of" the temporary loans,
  with "$70,000" still owed. The June check matches that $70,000.
- **But the ledger and register show only about $30,000 of Steve loans outstanding at the
  time:** 10/6/2017 +$50,000, less 11/17/2017 −$20,000. The 2015 loans were already repaid in
  2017.
- So about **$190,000 of the $220,000 is not supported as loan repayment** by either record
  (calc). It is booked as Steve's draws. A loan that came in through some other channel is not
  ruled out (INDETERMINATE).
- Steve's 515000 checks through Citizens in 2018 total **$236,286.53** (26 items, calc).
- **On 6/19/2018, 18 days after the $70,000 check, Johnson told Esraelian "There is not
  enough money to meet current operating needs"** and pressed for loan approval. He mentioned
  Steve returning a $50,000 tax refund but not the $70,000.

### 7.3 Regrades

| Item | Was | Now |
|---|---|---|
| 2014 $100,000 = loan repayment | INDETERMINATE | **SUPPORTED** (GL + register; 2012–14 nets to zero) |
| 2017 $100,000 (3/2) = loan repayment | — | **SUPPORTED** ("Temp Loan Payback"; repays 6/30/2015 "TEMP LOAN") |
| Esraelian stalling caused the $100,000 loans | CLIENT-ATTESTED | **NOT SUPPORTED** for 2012–15 loans; **fits** only the 10/2017 $50,000 |
| "$170,000 outstanding 11/2017" (my §3–§5 reading) | — | **WITHDRAWN.** Repaid 3–4/2017 |
| 2018 $220,000 = loan repayment (client 2/22/2018 email) | — | **UNSUPPORTED** for ~$190,000 on the ledger; INDETERMINATE pending other channels |
| Nurses paid on schedule in 11/2017 | open | **SUPPORTED** (register) |

---

## 8. UPDATE 10/1/2026 (latest): the complete 512000 ledger, 2004–2026, reverses §7.2(e)

**Source:** "steve capital contributions.xlsx" (Drive `1K8BSGBlDp8p-Bkd4trxMzynhOsckBZqX`; client
export 10/1/2026, QuickBooks Account QuickReport, 512000 Capital Cont.-Steve, all transactions;
read in full).
- It matches the 8/18/2017 printout line for line through 4/25/2017.
- It shows the full memos ("Temp Loan Payback"; "RECLASS INSURANCE SETTLEMENT TO CAPITAL
  CONTRIBUTION").
- **It adds entries the Citizens register could not show, because they sit inside split
  deposits.**

### 8.1 Entries after 4/25/2017

| Date | Type / No. | Memo | Amount | Balance |
|---|---|---|---|---|
| 8/29/2017 | Deposit 6020 | **temp loan** | +100,000.00 | −70,000.00 |
| 10/6/2017 | Deposit 6042 | **Temporary Loan** | +50,000.00 | −20,000.00 |
| **11/9/2017** | Deposit 6064 | **temp loan** | **+20,000.00** | 0.00 |
| 11/17/2017 | Check 29338 | Temp Loan Payback | −20,000.00 | −20,000.00 |
| 11/29/2017 | Deposit 6074 | temporary loan | +40,000.00 | 20,000.00 |
| 12/5/2017 | Deposit 6077 | temp loan | +40,000.00 | 60,000.00 |
| 1/1/2018 | GJ Frazer 18-8 | close out 12/31/17 capital | −60,000.00 | 0.00 (= FY2017 "contribution" $60,000) |
| 6/8/2018 | Deposit 6154 | Deposit | +10,000.00 | 10,000.00 |
| 7/11/2018 | Deposit 6164 | Temp Loan | +15,000.00 | 25,000.00 |
| 7/16/2018 | Deposit | **2013 2014 FTB refund** | +43,630.24 | 68,630.24 |
| 9/11/2018 | Deposit 6193 | TEMP LOAN | +25,000.00 | 93,630.24 |
| 1/1/2019 | GJ Frazer 49- | TO CLOSE CAPITAL | −93,630.24 | 0.00 (= FY2018 "contribution" $93,630) |
| 4/22/2019 | Check 31962 | | −60,000.00 | −60,000.00 |
| 1/1/2020 | GJ Frazer 1 | To close capital | +60,000.00 | 0.00 |
| 6/24/2023 | Deposit 6881 | Deposit | +155,000.00 | 155,000.00 |
| 6/24/2023 | Deposit ("Cash") | Deposit | +5,000.00 | 160,000.00 |
| 7/20/2023 | Deposit | Deposit | +100,000.00 | 260,000.00 |
| 8/14/2023 | Deposit 6900 | Deposit | +100,000.00 | 360,000.00 |
| 1/1/2024 | GJ FrzrTXP-01 | To close capital | −360,000.00 | 0.00 (= FY2023 "contribution" $360,000) |

**Also:** 12/31/2015, Frazer, "RECLASS INSURANCE SETTLEMENT TO CAPITAL CONTRIBUTION," from 689000
"Proceeds from Home Fire Claims," +$88,025.87. The FY2015 statements show the same $88,026
credited to Manuel's column. That implies $176,051.74 of home-fire insurance proceeds split to
the partners' capital (calc). **Whose home, and why it went to capital: open (OI-87).**

### 8.2 What changes

**§7.2(e) and A-73 were wrong on the key point. Corrected:**
- Between 8/29 and 12/5/2017, Steve lent the partnership **$250,000**, every deposit memo'd
  "temp loan" or "temporary loan." He was repaid $20,000 on 11/17.
- **About $230,000 was owed to him at 12/31/2017** (calc).
- The **$150,000 (1/13/2018) and $70,000 (6/1/2018)** checks therefore repaid documented loans.
- **Grade: SUPPORTED** as loan repayments in substance. They were *coded* to 515000
  Personal-Steve rather than 512000, the same presentation problem as 2014. So Steve's FY2018
  "Personal" withdrawals are overstated by about $220,000 of loan repayment (calc).
- Jace's 2/22/2018 "currently owed $70,000" is close to the ledger's $230,000 − $150,000 =
  $80,000. A **$10,000 difference** is unexplained.

**Esraelian. The client's explanation fits this loan series. PARTLY SUPPORTED:**
- The $250,000 came in exactly while Hazel's sign-off on Farm Credit draws was being withheld or
  conditioned (documented 9/18–12/27/2017).
- The 8/29/2017 $100,000 "temp loan" precedes the first Esraelian email found (9/18/2017) by
  three weeks. Ryan Camara had already sent her the renewal documents by then (date NOT
  ESTABLISHED).
- **On 11/9/2017, the day of the authorization fight and the "nurses" email, Steve lent
  $20,000.** That answers the same-day "[PRIV] My Dad just isn't too excited about loaning the
  partnership to pay for nurses": he lent anyway, and lent $80,000 more by 12/5.

**The client's "$100,000 repayment of a temporary loan"** now has three candidates, all supported
as loan repayments:
- the 2014 net $100,000 (Frazer reclass);
- 3/2/2017 "Temp Loan Payback" $100,000;
- the 1/13/2018 $150,000, which repaid the 8/29/2017 $100,000 plus the 10/6 $50,000.

Only the last one fits the Esraelian explanation.

**6/19/2018 "not enough money" (A-73):**
- Steve had been repaid $70,000 on 6/1 for late-2017 loans.
- He then lent again: $10,000 (6/8), $15,000 (7/11) and $43,630.24 (7/16, his FTB refund).
- That is consistent with Johnson's "he has deposited it back."
- The timing still reads poorly, but it is explicable as a revolving bridge.

**2023:** $360,000 in (6/24–8/14/2023), "Deposit" memos, no repayment through 512000 since.
Jace's 7/16/2026 "bridge loans" description therefore has **no repayment yet** for the 2023
money. If it is a loan, it is still outstanding.
