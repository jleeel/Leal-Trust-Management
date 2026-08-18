# ⛔ READ THIS BEFORE OPENING R1–R4
# THE LEGAL RESEARCH IN THIS FOLDER IS **NOT VERIFIED AUTHORITY**

**ATTORNEY WORK-PRODUCT SUPPORT — PREPARED FOR COUNSEL — NOT LEGAL ADVICE**
Prepared August 18, 2026

---

## What happened

Memos R1–R4 were scoped to be researched using a **CourtListener MCP server**, with every
citation verified by retrieving the source.

**That was not possible in this environment, and counsel needs to know exactly why.**

1. **No CourtListener MCP server was available.** It is not connected to this session.
2. **The network egress proxy blocked every legal-research domain.** Verified directly:
   `leginfo.legislature.ca.gov`, `courtlistener.com`, `storage.courtlistener.com`,
   `courts.ca.gov`, `cite.case.law`, `justia.com`, `casetext.com`, `scholar.google.com`,
   `findlaw.com`, `leagle.com`, `casemine.com`, `law.resource.org`, `public.law`,
   `archive.org` — all returned **HTTP 403 / EGRESS_BLOCKED** at the gateway.

**Consequence: not a single judicial opinion was read in its native source.** Case names,
years, reporter citations and holdings in R1–R4 come from **web-search result summaries**.

---

## What this means, stated plainly

| | Status |
|---|---|
| **Statutory text** | **Partially verified.** R2 located the California Legislative Counsel's own PUBINFO database export (a July 9, 2026 snapshot, mirrored publicly) and read **verbatim text for 22 code sections**. R1, R3 and R4 obtained statutory text through search extraction only. |
| **Case law** | **NONE VERIFIED.** No opinion was retrieved. No holding was read in the original. |
| **Pin cites** | **NONE CONFIRMED, ANYWHERE, IN ANY MEMO.** |

**Treat R1–R4 as a research roadmap, not as research.** They are useful for issue-spotting,
for the statutory framework, and as a list of authorities to look up. **They are not a basis
for advising a client, drafting a brief, or making a representation to the court.**

---

## Mandatory before any use

1. **Re-run every issue in Westlaw or CoCounsel.** Confirm each case exists, says what the
   memo says, and remains good law. **Shepardize / KeyCite everything.**
2. **Confirm every statutory quotation against leginfo**, including the verbatim-sourced
   sections — the PUBINFO snapshot's completeness could not be independently confirmed.
3. **Do not cite anything from these memos in any filing without doing 1 and 2 first.**

---

## Specific traps flagged by the researchers — check these first

- **R1 — `M. Lowenstein & Sons, Inc. v. Superior Court` (1978) 80 Cal.App.3d 762: DO NOT CITE.**
  Name, citation and holding all unconfirmed; a differently-named case surfaced instead. This
  was the intended support for the **fact-of-service vs. proof-of-service** distinction — our
  best non-prejudice argument on the § 998 POS defect. **That argument currently rests on no
  verified citation.**
- **R1 — `Gorobets`**, reported as a California Supreme Court decision of **August 6, 2026**
  (twelve days before this memo). A very recent decision found only through search summaries
  is exactly the kind of item most likely to be misdescribed. **Verify its existence, holding
  and citation before relying on it for anything.** Same for `Madrigal` — reporter cites
  unconfirmed for both.
- **R1 — `Poster v. So. Cal. RTD` (1990) 52 Cal.3d 266**: the search record contains **directly
  contradictory** statements about whether CCP § 1013 extends the § 998 acceptance window to
  35 days. The memo adopts 35 days **but flags it**. **Counsel must read the opinion.** This
  drives the expiration-date computation in the chronology.
- **R1 — `Katz v. El Paseo Collection Elegante`** is reported **unpublished** — presumptively
  non-citable under **CRC 8.1115**.
- **R1 — Open Question #1, potentially dispositive:** whether **§ 998 applies to a Probate Code
  proceeding at all** was not researched.
- **R1 — subdivision error in the original tasking:** § 998(c)(1) governs a **defendant's**
  offer. Ours is a **plaintiff's** offer, so **§ 998(d)** likely controls — *discretionary
  expert fees*, not automatic cost-shifting. **If correct, the § 998 upside is much smaller
  than assumed.** Verify.
- **R2 — `Estate of Silveira`** is **unpublished and not citable** (CRC 8.1115), though the
  trigger question it raises is worth counsel's attention.
- **R2 — no published California case was found** holding a partnership/LLC interest "unique"
  for specific-performance purposes, or applying **appraisal-as-arbitration outside first-party
  insurance**. Both gaps are material to our theory.
- **R3 — citation trap:** **Probate Code § 16403** (successor-trustee liability) and
  **Corporations Code § 16403** (partnership books and records) are *different statutes with
  the same number*. Also: `Estate of McCabe` appears at **two** different citations.
- **R3 — no case is cited** for the surcharge elements or burden allocation; **laches was not
  researched at all.**
- **R4 — no California authority was located** on the effect of a general release on the
  temporal scope of discovery. That analysis is first-principles inference only.
- **R4 — a search summary directly contradicted the statutory text it purported to quote**
  (CCP § 2031.280(e)). Documented in that memo as evidence the summaries are unreliable unaided.

---

## ⚠️ A premise in R4 has since been disproved by the documents

R4's proportionality analysis leans on the **December 7, 2017 Settlement Agreement and Mutual
Release** operating as a cutoff for pre-2017 claims and therefore limiting discovery.

**The Settlement Agreement has now been read** (see
`../01-verified-facts/governing-instruments-extract.md`). **The release is narrow.** ¶13
releases only claims relating to "**the division of the real property**," and ¶15 states that
"**the only issues resolved by this Settlement Agreement is [sic] the division of identified
real property and the valuation of the improvements identified in the Agreement.**"

**Accounting, draw, distribution and fiduciary claims appear to fall outside it.** Counsel
should read R4's release-based arguments with that correction in mind.

---

## One finding worth counsel's early attention (still unverified)

R2 flags **Civ. Code § 3390(b)** — barring specific enforcement of "an obligation to employ
another in personal service" — and **§ 3390(d)** — barring an order compelling a party "to
procure the act or consent of… any other third person."

**Our § 998 offer and the Complaint's prayer both ask the court to order defendants to
*employ* Stanley Xavier and Moss Adams**, neither of whom is before the court. R2 reads
§ 3390 as aimed squarely at that form of relief, and suggests an alternative framing:
**judicial valuation, or appointment under CCP § 1281.6** (court "shall appoint the
arbitrator" where the agreed method "fails or for any reason cannot be followed") or
**Evid. Code § 730**.

**This is potentially a structural problem with the relief we have pleaded, and it deserves
counsel's attention early — but § 3390's text and its case-law gloss must be confirmed
before anyone acts on it.**


---

# ⚡ UPDATE — AUGUST 18, 2026: COURTLISTENER VERIFICATION PASS COMPLETED

The client connected a **CourtListener MCP server** mid-session. A verification agent re-checked
the critical authorities against **actual opinion text**. Full report:
`verification-report-courtlistener.md`. **The warnings above still apply to everything NOT listed
there, and CourtListener cannot check subsequent history — KeyCite/Shepard's remains mandatory.**

## Status changes

| Item | Old status | New status |
|---|---|---|
| *Poster v. So. Cal. RTD* (1990) 52 Cal.3d 266 | conflicting summaries | **VERIFIED (read)** — § 1013 extends the § 998 acceptance period to **35 days** for mailed offers (p. 275). The contrary statement was the reversed Court of Appeal. The chronology's **8/13/2026** expiration is the operative computation for a 7/9/2026 mailed offer. |
| *Gorobets v. Jaguar Land Rover*, S287946 (Cal. Aug. 6, 2026) | unverified recency flag | **VERIFIED (read)** — alternative-choice § 998 offers are valid **if clearly structured and one alternative is certain when made; offeror bears the validity burden.** CoA below: 105 Cal.App.5th 913. No reporter cite yet. |
| *M. Lowenstein & Sons* (1978) 80 Cal.App.3d 762 | **DO NOT CITE — possibly nonexistent** | **VERIFIED (read full) — the case is REAL.** It is a **service-of-summons** case: jurisdiction depends on the **fact** of service, and POS defects are **amendable nunc pro tunc**. Useful by analogy for our misdated proof of service; it is **not** § 998 authority. |
| *Puerta*, *Mostafavi*, *Barella*, *Licudine* | search summaries | **All VERIFIED (read)** with quotes. Note **Mostafavi fn. 6: the offer's terms must be in the offer itself** — adverse to our cover-letter-only monetary alternative. *Barella*: strict construction against the offeror; a non-valuable term invalidates. |
| *Bewick v. Mecham* (1945) 26 Cal.2d 92 (Traynor, J.) | search summary | **VERIFIED (read full)** — where a party's refusal breaks the agreed appraisal mechanism, **the court fixes the price itself (Civ. Code § 1613) and decrees specific performance**; appraisal ≠ arbitration. |
| *Petrolink v. Lantel* (2018) 21 Cal.App.5th 375 | search summary | **VERIFIED** — the appraiser there was a **court-appointed Evid. Code § 730 expert**, not § 1281.6; no one was ordered to "employ" anyone. |
| *Woolley* (1991) 227 Cal.App.3d 1520 | not previously found | **VERIFIED-operative** — § 3390 bars specific performance of personal-services contracts. **Adverse to our "order defendants to employ two named appraisers" prayer.** |
| *Rappaport v. Gelfand* (2011) 197 Cal.App.4th 1213 | statute unverified | **VERIFIED** — quotes § 16701(b) verbatim: "**Interest shall be paid from the date of dissociation to the date of payment**," and affirms a judgment carrying interest from the dissociation date. Also quotes the § 16103(a) default rule. |
| *Han v. Hallberg* (2019) 35 Cal.App.5th 621 | § 16601 unverified | **VERIFIED — with a landmine.** Holds substitution of a successor trustee is NOT dissociation, per § 16601, subd. **(8)** (the memos said (7) — corrected). **BUT the Supreme Court GRANTED REVIEW (S256659). Its current status and any Supreme Court disposition are unknown to this workspace. This is the single most important KeyCite in the case.** |
| *Corrales v. Corrales* (2011) 198 Cal.App.4th 221 | not previously found | **VERIFIED** — "the buyout rule of section 16701 does not apply to a **two-person** partnership when one partner leaves" (dissolution/winding-up instead). **Our partnership has FOUR named partners (Art. I.B), so Corrales appears distinguishable — but counsel should be ready for arguments about the effective partner count after the Bypass Trust's 1/1/2023 dissolution.** |
| Corp. Code § 16603 | unverified | **NOT FOUND quoted in any California opinion** — still needs Westlaw for its text. |
| *Purdy*, *Uzyel*, *Levin v. Winston-Levin*, *Estate of Kraus*, *Calcor*, *Obregon*, *Williams* | search summaries | **All VERIFIED** with quotes in the report. |

## What this means for the case theory (counsel's calls, stated as considerations)

1. **The relief reframe now has verified support.** *Bewick* (court fixes the price when a party's
   refusal breaks the mechanism) + *Petrolink* (§ 730 court-appointed appraiser) supply exactly
   the alternative R2 proposed — while *Woolley* verifies the § 3390 exposure of the current
   "employ Correia-Xavier / employ Moss Adams" prayer. **The amendment decision (OI-22 / A-19)
   should now assume the § 3390 risk is real and the fix is available.**
2. **The interest-not-profits position has verified statutory text behind it** (*Rappaport*
   quoting § 16701(b)) — **conditioned entirely on dissociation having occurred**, which is where
   *Han* sits. **If the Supreme Court affirmed Han, the contract's express "Dissociating Events"
   definition (Art. XIII.B.1) has to carry the argument against the statutory default alone; if
   review was dismissed or the CoA reversed, the landscape shifts. One Westlaw lookup resolves
   this.**
3. **The § 998 posture worsened on verification.** *Mostafavi* fn. 6 (terms in the offer itself)
   and *Gorobets* (alternatives must be clearly structured **in the offer**, offeror's burden)
   both cut against the July 2026 package, whose only monetary term lives in the cover letter.
   **The serve-a-fresh-corrected-998 option (OI-1) looks stronger than defending the old one.**
   *Poster* being verified at 35 days means the old offer expired **8/13/2026** if mailed 7/9.

---

## STATUS UPDATE — 8/18/2026 (second CourtListener pass, drafts-sweep trigger)

**Martinez v. Brownco Construction Co. (2013) 56 Cal.4th 1014 — moved from "not researched"
to VERIFIED (read in full, CourtListener cluster 899532).** Holding quoted verbatim in R1
Addendum 2. Trigger: the drafts sweep surfaced four 5/18/2026 cover letters for a possible
EARLIER $5,750,000 § 998 offer (service unestablished — OI-41). If two successive offers
exist, Martinez/Wilson/T. M. Cobb govern the baseline analysis; R1 Addendum 2 frames the
briefing question. Still Westlaw-only: subsequent history/citing treatment of all four
successive-offer cases, and whether Martinez extends to a LOWER second offer by the offeror.
