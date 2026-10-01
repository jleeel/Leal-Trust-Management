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
