#!/usr/bin/env python3
"""Build the attorney dashboard and the document index from the workspace.

    python3 cmc-prep/07-attorney-dashboard/build_dashboard.py

Outputs (self-contained HTML, no external requests):
    leal-case-dashboard.html   work product: status, issues, discovery, open items,
                               red team, timeline, documents, library of memos
    leal-document-index.html   Drive document list only, no analysis

Inputs are the workspace files themselves, so rebuild after every integration.
Curated content (key dates, people, issue cards) lives in the CONFIG section below;
every statement there carries its source.
"""
from __future__ import annotations

import base64
import csv
import html
import io
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from markdown_it import MarkdownIt

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent                      # cmc-prep/
OUT_DASH = HERE / "leal-case-dashboard.html"
OUT_INDEX = HERE / "leal-document-index.html"

DRIVE = "https://drive.google.com/open?id={}"
DRIVE_ID = re.compile(r"^1[A-Za-z0-9_-]{24,48}$")
GMAIL_ID = re.compile(r"^1[0-9a-f]{15}$")

# ---------------------------------------------------------------------------
# CONFIG — curated, cited content
# ---------------------------------------------------------------------------

CAPTION = {
    "court": "Superior Court of the State of California · County of Tulare, Visalia Division",
    "plaintiff": "MANUEL STEPHEN LEAL, Plaintiff,",
    "defendants": ("ASHLEY GARABEDIAN and HAZEL SUSAN LEAL, Successor Co-Trustees of the "
                   "HAZEL J. LEAL REVOCABLE TRUST dated November 3, 2008; and DOES 1–10, Defendants."),
    "right": [("Case No.", "VCU327028"), ("Judge", "Hon. David C. Mathias, Dept. 1"),
              ("Action filed", "October 16, 2025"), ("Trial date", "None set")],
    "source": "S-38, caption p.1",
}

KEY_DATES = [
    # (date, label, state, source)
    ("2026-10-13", "Case management conference", "confirm",
     "Workspace tasking; confirm on the docket (OI-9, OI-19)"),
    ("2026-10-14", "Client documents due to Brandon (his working date, not a court deadline)", "soon",
     "Ormonde email 9/29/2026: “within 15 days from today” (S-39)"),
    ("", "Formal response to Demand for Production, Set One", "counsel",
     "Served 9/28/2026 by mail and email (S-38 POS). Counsel calendars the date."),
    ("2026-09-28", "Defendants served Demand for Production, Set One (18 demands)", "done", "S-38"),
    ("2026-01-28", "Mediation (Volkmann, JAMS); did not resolve", "done", "Incoming-counsel briefing §2"),
    ("2025-10-16", "Complaint filed", "done", "S-38 caption"),
    ("2022-09-23", "Hazel J. Leal died (the buyout trigger)", "done",
     "S-3 (a brief); death certificate not located (OI-11)"),
]

PEOPLE = [
    # (group, name, role, source)
    ("Our side", "Brandon M. Ormonde", "Lead counsel, Ormonde Rascon, Tulare", "S-38 POS; client 10/3/2026"),
    ("Our side", "Erika Rason", "Co-counsel, Ormonde Rascon (litigation)", "Client 10/3/2026 (spelling as given by client)"),
    ("Our side", "Steve Leal (Manuel Stephen Leal)", "Plaintiff; managing partner of the dairy", "S-38"),
    ("Our side", "Jace Leal", "Client-side contact; keeps the books", "Workspace"),
    ("Our side", "Frazer LLP (Dan Vos, Mike Edwards)", "Partnership CPA", "S-40; kit §0"),
    ("Their side", "Ashley Garabedian; Hazel Susan Leal", "Defendants, successor co-trustees", "S-38"),
    ("Their side", "Timothy L. Thompson; Nikole E. Cunningham", "Defense counsel, Whitney, Thompson & Jeffcoach LLP, Fresno", "S-38"),
    ("Their side", "Edwards & Barber (Will Shannon, Tad Edwards)", "Defendants' CPAs; hold the full QuickBooks backup since 2/12/2026", "Kit §0 (Gmail 19c5247709a41389)"),
    ("Their side", "Robyn L. Esraelian", "Trust attorney (prior firm); percipient witness", "Briefing §6.8; A-79"),
    ("Court", "Hon. David C. Mathias", "Assigned for all purposes, Dept. 1", "S-38"),
    ("Witness", "Mary (surname possibly Pacheco; confirm)", "Hazel's sister, about 90; willing to testify per client; account of Hazel's banker/stockbroker request and a facility incident (2020-22)", "Client 10/4/2026; S-43, S-44; A-85"),
]

THIS_WEEK_CLIENT = [
    ("OI-92", "Pull the documents for Demand for Production, Set One, by source; deliver to Brandon by about 10/14."),
    ("OI-98", "Export the QuickBooks Journal report and Audit Trail, plus the remaining draw accounts."),
    ("OI-93", "Answer the mobile-home questions (rent, cash, who lives there) for counsel only."),
    ("OI-94", "Built Wright: building permit, contract, invoices #1500–#1636, site."),
    ("OI-95", "Insurance schedules (CIG, Nationwide) and the United of Omaha policy."),
    ("OI-96", "Vendor account histories with job sites: Morris Levin, Phelps, Saltzman, Turnupseed, Israel Rivas."),
    ("OI-100", "Mary (Hazel's sister): consent to the recording, her details, transcript; no more case talk until counsel speaks to her."),
]
THIS_WEEK_COUNSEL = [
    ("S-38", "Calendar the response date; objections (demands 4–5 have no date limit; “affiliated accounts”; YOU and DAIRY definitions)."),
    ("A-81", "Privilege log approach (CPA Rebuttal drafts, analysis files) and rolling production."),
    ("A-68", "Demand 6: reconcile the draft's “third-party cash rent” with the client's “employee housing.”"),
    ("A-83", "Characterization of the partnership-paid legal fees (LEA-0648, “Jace Bill”)."),
    ("OI-72", "Unconditional tender of the undisputed amount, weighed against title and structuring."),
    ("OI-30", "Westlaw: whether § 16601(8) can be varied by agreement under § 16103(b) (largest dollar issue)."),
]

STANDING = [
    ("Formal discovery has started.", "Defendants served Demand for Production, Set One on 9/28/2026. It formalizes 8 of Cunningham's 9 informal requests and adds 9 vendor and insurance demands.", "S-38; A-81"),
    ("The informal requests were rated insufficient.", "Cunningham, 9/2026: items 1–3 and 5 insufficient, 6–9 no response, 4 resolved; no second mediation day before the CMC; they plan to file an answer and cross-complaint.", "Kit §0 (Gmail 1a0e8bb75c0a0a1c)"),
    ("Defendants have not answered the Complaint, as far as the record shows.", "As of 8/18/2026 there was an open-ended extension. No answer or cross-complaint has been located since.", "Briefing §2; no later source"),
    ("Settlement positions are far apart.", "Ours $5,705,257.43 (7/2/2026). Theirs $7,359,766 plus 2025 profit and lease credits (6/19/2025). The partnership value itself is agreed at $1,162,612.50 before the 90% factor.", "Briefing §§2–3; S-2"),
    ("The biggest dollar question is legal.", "Post-death profit share (theirs) vs. the contract's 4% interest (ours). Han v. Hallberg stands; whether § 16601(8) can be varied by agreement is the open question.", "OI-30; briefing §5"),
]

ISSUES = [
    {
        "title": "Mandatory buyout and the price",
        "tag": "Core dispute",
        "points": [
            ("Hazel's death is a defined “Dissociating Event.” The 7/2018 Amended and Restated Partnership Agreement requires a buyout at 90% of appraised value on a 20-year, 4% note (Art. XIII.B).", "governing-instruments-extract, addendum"),
            ("Four levers decide the number: real-property basis, minority discount, post-death compensation, offsets. Ours $5,705,257.43 vs. theirs $7,359,766 + 2025 profit + leases.", "Briefing §§2–3; S-2"),
            ("Their counsel (Esraelian) proposed and engaged Stan Xavier for the buyout in 2023; Moss Adams found “no obvious errors or omissions in either report.”", "Briefing §4 (Ex. G, Ex. Q)"),
        ],
        "docs": [("Amended & Restated Partnership Agreement (7/24/2018)", "14gtepTK9rtCjDHXjvmLok69Lzm9AeE_E"),
                 ("Tenants-in-Common Agreement (6/2018)", "1m88PUeUj1PPR5DGwAV8K3oQEF56J9C0-"),
                 ("Correia-Xavier real property appraisal", "1kpW6FmVWvfiALeYiiENeBYfLSa8fFzKd"),
                 ("J. Hower real property appraisal", "1l1tts-BOgCRgnHrfmU9HbVNK6bOGjBOX"),
                 ("Moss Adams appraisal review", "1nGWM6PKf5AH9MM7SOey0PagCahXxAInC"),
                 ("Moss Adams business valuation", "1eIWBle06AeRRPoDKbvA_ND2Xj8IDArZF"),
                 ("Edwards, Lien & Toso personal property appraisal", "1j8YCVJRHiwfY51A8r998aHVTGUqugzQi"),
                 ("Ormonde to Cunningham, 7/2/2026 (our offer)", "1nnHz4PJtMz7wv-6b1GGwpV-0CT7Xq4we"),
                 ("Esraelian letter, 6/19/2025 (their position)", "17nW4-KFFOg3LWZfXkdOiPaM8JxlxZgKQ"),
                 ("Ormonde to Esraelian, 3/3/2025 (first priced offer)", "1ZjR_PqMiJ1Zz77MtrSIOoXJ_N4y-_Syt")],
        "library": ["06-counsel-transition/incoming-counsel-briefing.md", "01-verified-facts/governing-instruments-extract.md",
                    "01-verified-facts/drive-sweep/valuations-instruments-sweep.md"],
        "a": [15, 20], "oi": [23, 72],
    },
    {
        "title": "Post-death profits vs. 4% interest",
        "tag": "Largest dollar issue",
        "points": [
            ("Theirs: 37.5% of profits after death ($1,617,761 incl. interest, plus 2025 and leases). Ours: the contract's 4% interest ($677,830).", "Briefing §3"),
            ("Our own 2022 and 2024 Forms 1065 issue K-1s to the Hazel Revocable Trust at 37.5%. Argue election, waiver, contract; never “no such right exists.”", "Briefing §6.1; A-30, A-40"),
            ("The trustees received the $6,000 monthly payments: $288,000, 10/2022–9/2026 (client says trustees received them; ACH proof pending).", "A-70; OI-88"),
        ],
        "docs": [("FY2024/2023 reviewed financial statements (Frazer)", "1cqN3Cp2t9pMFiql2mXOYYZFZTxsSVZRm"),
                 ("Frazer capital through Hazel's DOD, rev. 2/13/2025 (DRAFT)", "1NTKDNbrv6pbcsNtp7yvR-9s0StvESndK"),
                 ("Hazel Draws 9.22.22–1.31.25", "1HMjBSPjcexZxjwoyXSBKkOALzWY4UkH1"),
                 ("Hazel's draws 1-15-25 thru 5-7-26", "1bBIP8sSpjtbTXcDlD-6BDpjNUEccc2bT"),
                 ("505000 Personal–Hazel 2009–2026 (S-41)", "15NgOh-wM6-JIzTUvtgZIUw9aPq-2wPG0")],
        "library": ["01-verified-facts/post-death-profits-issue.md", "02-legal-research/han-v-hallberg-explainer.md",
                    "02-legal-research/00-READ-FIRST-research-reliability.md"],
        "a": [30, 40, 70], "oi": [30, 38, 48, 88],
    },
    {
        "title": "Offsets and capital accounts",
        "tag": "$262,592 offset",
        "points": [
            ("Every offer nets $262,592: Hazel's excess draws $591,965 less $329,373 of Bypass income (Frazer reconciliation, rev. 2/13/2025, marked DRAFT).", "Briefing §4.5; S-8"),
            ("Hoof-trimmer “Cash” checks charged to Hazel's draws feed that figure. The ledgers show both partners were charged: Hazel $49,300.10, Steve $67,710, 2009–1/2018; the 2017–18 splits were 50/50.", "A-69 update; S-41, S-42"),
            ("Bypass double count: $329,373 − $1,945 = $327,427.02, the same figure used twice.", "Briefing §6.5; A-55; OI-60"),
        ],
        "docs": [("Frazer capital through Hazel's DOD (DRAFT)", "1NTKDNbrv6pbcsNtp7yvR-9s0StvESndK"),
                 ("Equity Accounts 1997–2015 (S-4)", "1O7OGL798JcaTXginVNMIUgKtNV-ckK0l"),
                 ("STEVE.HAZEL PERSONAL EXPENSES.xlsx (S-6)", "1o5Re3q_6wZTRu_Mhh4yrtNqVrgFuKmBo"),
                 ("505000 Personal–Hazel (S-41)", "15NgOh-wM6-JIzTUvtgZIUw9aPq-2wPG0"),
                 ("515000 Personal–Steve (S-42)", "1wDIt4i7kJHM66KanNOTH08PocKIDW_E7")],
        "library": ["01-verified-facts/partner-draw-accounts-505000-515000.md", "01-verified-facts/verified_facts_memo.md"],
        "a": [1, 55, 69, 76, 84], "oi": [39, 60, 75],
    },
    {
        "title": "Steve's loans and the 2023 $360,000",
        "tag": "Characterization",
        "points": [
            ("512000 ledger: 2012–14 lent and repaid $375,000; 2015 $170,000 lent, repaid 3–4/2017; 8–12/2017 $250,000 of temporary loans, repaid by the 2018 $150,000 and $70,000 checks.", "steve-temp-loans-512000.md §§7–8; S-30, S-32"),
            ("Frazer told their side on 2/22/2018 that Steve's capital contributions “are for money Steve loaned the business to cover bills.”", "Gmail 1602be0a88bae639 (kit item 6)"),
            ("2023 $360,000: the books call it a capital contribution; the client says Steve expected to be sole owner. Loan vs. contribution is undecided.", "A-77; OI-80"),
        ],
        "docs": [("512000 Capital Cont.–Steve 2004–2026 (S-32)", "1K8BSGBlDp8p-Bkd4trxMzynhOsckBZqX"),
                 ("512000 ledger printed 8/18/2017 (S-30)", "1sf5rKftJWQsrm95oLqAaQxRVmjvaNzLB"),
                 ("Citizens register 2009–2026 (S-29)", "1XhazEklYhxAH27FlpuY6IqHSMEZ1muvR"),
                 ("Frazer FY2014 adjusting entries (S-25)", "1f5JGW5GYY4weVMoBqbfqETX3Llgz_VNp"),
                 ("Response 11.9.17 (client draft answers, S-26)", "1--NBmBDOT7CgW02vsECpqAdzJjm3bZN2")],
        "library": ["01-verified-facts/steve-temp-loans-512000.md"],
        "a": [1, 72, 73, 77], "oi": [80],
    },
    {
        "title": "Settlement ¶8 accounting and ¶11 borrowing",
        "tag": "Their theory",
        "points": [
            ("Settlement ¶8 requires a monthly accounting; ¶11 sets spending and borrowing approvals.", "governing-instruments-extract §1"),
            ("Partly documented: online access 9/10/2020; a June 2021 packet; May–Aug 2022 statements sent to the trust's CPA before the 15th.", "A-13 update; S-35"),
            ("Esraelian held the credit line 9/2017–6/2018; the 11/9/2017 nurse-checks email.", "steve-temp-loans-512000.md §3; S-28"),
        ],
        "docs": [("Settlement Agreement (eff. 12/7/2017)", "1XyW7LqeH2j3t93ESBFRco2GFmfW4XHoE")],
        "library": ["01-verified-facts/governing-instruments-extract.md", "04-adverse-analysis/adverse_analysis.md"],
        "a": [13], "oi": [14, 40],
    },
    {
        "title": "Trust-side benefits and Hazel's checks",
        "tag": "Both ways",
        "points": [
            ("Charged to Hazel's draws: Mercury {Danielle} insurance $18,999.45, Fly Girl $15,325, Culligan $10,413.80, a grave payment and the memorial.", "S-41; A-75"),
            ("Hazel's handwritten checks (below #4477) coded as dairy expense: $98,774.70 personal on its face; at least $4,284.51 later reclassified into her draws; 2010–2012 indeterminate.", "A-76 update"),
            ("Water to the three houses and the Danielle card incident are CLIENT-ATTESTED.", "trust-side-benefits memo"),
        ],
        "docs": [("Cancelled checks Feb 2013 (S-33)", "1ILfq7Zz37BYLQHnGFysOIO1X8C8eGa14"),
                 ("505000 Personal–Hazel (S-41)", "15NgOh-wM6-JIzTUvtgZIUw9aPq-2wPG0"),
                 ("Grant deed APN 158-160-006, Bypass → Hazel trust 50% (S-34)", "1qfthXjyoAuJR73MGGUVDFMxt4lGhOjp1")],
        "library": ["01-verified-facts/trust-side-benefits-water-insurance-card.md", "01-verified-facts/hazel-checkbook-series-2010-2019.md"],
        "a": [75, 76], "oi": [83, 86],
    },
    {
        "title": "The “funneling” theory and the RFP vendors",
        "tag": "Discovery",
        "points": [
            ("The Demand for Production targets off-book income, personal expenses and capital-account entries, with check numbers.", "S-38; A-81"),
            ("Built Wright “new freestall”: $1,479,054.85 (9/2024–9/2026), $1,040,414.94 after the Complaint; site not established.", "A-82; S-40"),
            ("Frazer reclassified $49,352.87 of Jacobsma “personal home repairs - Steve” out of dairy repairs (2022). The partnership pays Ormonde & Rascon fees, expensed since 5/2025.", "A-84; A-83"),
        ],
        "docs": [("Citizens register 2009–2026 (S-29)", "1XhazEklYhxAH27FlpuY6IqHSMEZ1muvR"),
                 ("515000 Personal–Steve (S-42)", "1wDIt4i7kJHM66KanNOTH08PocKIDW_E7"),
                 ("FY2024/2023 reviewed FS", "1cqN3Cp2t9pMFiql2mXOYYZFZTxsSVZRm")],
        "library": ["05-for-brandon/rfp-set-one-response-map.md", "03-chronology/delay-attribution-ledger.md"],
        "a": [68, 81, 82, 83, 84], "oi": [92, 93, 94, 95, 96, 97, 98],
    },
    {
        "title": "Heifer ranch note and the 2026 balloon",
        "tag": "Answered",
        "points": [
            ("The Orozco note's makers were the three trusts, including Hazel's; the partnership is not a maker.", "A-71 (Chicago Title escrow file)"),
            ("Paid 3/4/2026: $637,853.98 final payment, funded by a $600,000 Cow Line advance deposited to Citizens the same day.", "S-29; kit addendum"),
            ("The partnership also paid $600,000 to Borges Dairy for Land O'Lakes base on 3/18/2026, coded Miscellaneous.", "A-59; S-29"),
        ],
        "docs": [("Rodrigues Ranch Escrow (2/23/2011)", "10ZCnjymzZ2nTAHSwPnCw9Do7m6YvDnqU"),
                 ("Rodrigues Ranch Note (amortization schedule)", "1b_jf6r-yY-nkYbKzZl6VcfDwP40n1g7l"),
                 ("Orozco.Rodrigues Deed (image-only)", "1ATNLIoV4I0xe-9ajJz8IGJeYno625Gvl")],
        "library": ["05-for-brandon/nikki-9-requests-kit.md"],
        "a": [59, 71], "oi": [67, 68],
    },
    {
        "title": "§ 998 offer and settlement posture",
        "tag": "Procedure",
        "points": [
            ("The July 2026 § 998 package has facial defects: proof of service dated January 3, 2018; no monetary term in the offer itself.", "A-2, A-3; S-1, S-14"),
            ("The 5/18/2026 $5,750,000 letters were client drafts, not served (strong inference).", "OI-41 (resolved)"),
            ("Conditional offers do not stop interest (Mission, verified); the unconditional-tender decision is open.", "A-66, A-67; OI-72"),
        ],
        "docs": [("998 offer FINAL.pdf (S-1)", "11VQh2jHIMvTnhVQr2bcIVZjoXcwrudYB"),
                 ("Ormonde to Cunningham, 7/2/2026 (S-2)", "1nnHz4PJtMz7wv-6b1GGwpV-0CT7Xq4we")],
        "library": ["01-verified-facts/998-as-served-extract.md", "02-legal-research/R1-ccp-998-validity.md"],
        "a": [2, 3, 66, 67], "oi": [1, 41, 72],
    },
    {
        "title": "Relationships on the trust side",
        "tag": "Bias and knowledge",
        "points": [
            ("Aaron J. Garabedian, CPA, was the trust side's accountant in 2017–18 and is a named contingent remainder beneficiary of Hazel's trust; Lauren Garabedian Ruff was Hazel's CPA 2020–22.", "A-78"),
            ("Robyn Esraelian (née Garabedian) is Dale Garabedian's sister; Dale is Aaron's and Lauren's father; Ashley and Aaron married 11/11/2018 and divorced in 2026.", "A-79 (CLIENT-ATTESTED family ties); S-36"),
            ("9/28/2017: Ashley and Aaron proposed making Jace CEO of a new LLC (CLIENT-ATTESTED).", "A-80; S-37"),
        ],
        "docs": [],
        "library": ["04-adverse-analysis/adverse_analysis.md", "05-for-brandon/deposition-outline-draft.md"],
        "a": [78, 79, 80], "oi": [89, 90, 91],
    },
]

LIBRARY_GROUPS = [
    ("Start here", ["05-for-brandon/00-COVER-NOTE.md", "06-counsel-transition/incoming-counsel-briefing.md",
                    "05-for-brandon/action_plan.md", "05-for-brandon/open_items.md"]),
    ("Discovery", ["05-for-brandon/rfp-set-one-response-map.md", "05-for-brandon/nikki-9-requests-kit.md",
                   "05-for-brandon/document-retrieval-list.md", "05-for-brandon/deposition-outline-draft.md"]),
    ("Red team and delay", ["04-adverse-analysis/adverse_analysis.md", "03-chronology/delay-attribution-ledger.md"]),
    ("Facts and extracts", "01-verified-facts/*.md"),
    ("Legal research (UNVERIFIED unless marked)", "02-legal-research/*.md"),
    ("Drive sweeps", "01-verified-facts/drive-sweep/*.md"),
    ("Counsel transition", ["06-counsel-transition/transition-checklist-and-counsel-selection.md"]),
]
LIBRARY_FIRST = ["verified_facts_memo.md", "source-register.md", "governing-instruments-extract.md",
                 "trust-instruments-extract.md", "complaint-extract.md"]

EVIDENCE = [  # workspace files received by chat upload, not in Drive
    ("2017-09-28_jace-ashley-text-after-meeting.png", "Text thread with Ashley, 9/28/2017 (S-37)"),
    ("2018-10-06_ashley-text-wedding-11-11-2018.png", "Text thread with Ashley, 10/6/2018 (S-36)"),
    ("2017-11-09_lealdairy-to-esraelian-nurse-checks-email.png", "Esraelian reply quoting the 11/9/2017 nurse-checks email (S-28)"),
    ("2026-10-01_lealdairy-sent-to-lauren-ruff-monthly-statements-2022.png", "Monthly statements sent to Lauren Ruff, 2022 (S-35)"),
    ("2026-09_susan-leal-final-payment-email.png", "Susan Leal final-payment email, 9/2026"),
]
EVIDENCE_PDF = ("2026-09-28_defendants-RFP-set-one-to-manuel-stephen-leal.pdf",
                "Defendants' Demand for Production, Set One (S-38)")

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def esc(s) -> str:
    return html.escape(str(s or ""), quote=True)


def slugify(path: str) -> str:
    s = re.sub(r"\.md$", "", path)
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def strip_tags(s: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def drive_link(label: str, did: str) -> str:
    return (f'<a class="doc" href="{DRIVE.format(esc(did))}" target="_blank" rel="noopener">'
            f'{esc(label)}</a>')


def git_rev() -> str:
    try:
        return subprocess.check_output(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"],
                                       text=True).strip()
    except Exception:
        return "unknown"


def json_script(id_: str, data) -> str:
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return f'<script type="application/json" id="{id_}">{payload}</script>'


SEVERITY = {"🔴": "crit", "🟠": "high", "🟡": "med", "🟢": "low"}


def severity_of(text: str) -> str:
    for k, v in SEVERITY.items():
        if k in text:
            return v
    return ""


EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐️]")


def clean_title(t: str) -> str:
    t = EMOJI.sub("", t)
    t = re.sub(r"\*\*|__|`", "", t)
    return re.sub(r"\s+", " ", t).strip()

# ---------------------------------------------------------------------------
# markdown library
# ---------------------------------------------------------------------------

MD = MarkdownIt("commonmark", {"html": False, "linkify": False, "typographer": False}) \
    .enable("table").enable("strikethrough")


def collect_library():
    docs, seen = [], set()
    for group, spec in LIBRARY_GROUPS:
        paths = []
        if isinstance(spec, str):
            found = sorted(ROOT.glob(spec))
            order = {n: i for i, n in enumerate(LIBRARY_FIRST)}
            found.sort(key=lambda p: (order.get(p.name, 99), p.name))
            paths = [str(p.relative_to(ROOT)) for p in found]
        else:
            paths = spec
        for rel in paths:
            p = ROOT / rel
            if not p.exists() or p.name in seen:
                continue
            seen.add(p.name)
            docs.append({"group": group, "path": rel, "name": p.name, "slug": slugify(rel)})
    return docs


def render_library(docs):
    name_to_slug = {}
    for d in docs:
        name_to_slug[d["name"]] = d["slug"]
        name_to_slug[d["path"]] = d["slug"]
        name_to_slug["cmc-prep/" + d["path"]] = d["slug"]
        if d["path"].startswith("05-for-brandon/"):
            pass
    # mirrors: 05-for-brandon/<name> resolves to the canonical copy
    headings = []
    for d in docs:
        text = (ROOT / d["path"]).read_text(encoding="utf-8")
        body = MD.render(text)
        n = 0

        def h_sub(m):
            nonlocal n
            n += 1
            level, inner = m.group(1), m.group(2)
            hid = f'{d["slug"]}--{n}'
            plain = strip_tags(inner).strip()
            headings.append({"doc": d["slug"], "id": hid, "level": int(level), "text": plain})
            return f'<h{level} id="{hid}">{inner}</h{level}>'

        body = re.sub(r"<h([1-6])>(.*?)</h\1>", h_sub, body, flags=re.S)

        def code_sub(m):
            inner = m.group(1)
            raw = html.unescape(inner).strip()
            if DRIVE_ID.match(raw) and not GMAIL_ID.match(raw):
                return (f'<a class="drive" href="{DRIVE.format(esc(raw))}" target="_blank" '
                        f'rel="noopener" title="Open in Google Drive"><code>{inner}</code></a>')
            if GMAIL_ID.match(raw):
                return f'<code class="gmail" title="Gmail thread ID (client mailbox)">{inner}</code>'
            key = raw.split("#")[0]
            base = key.split("/")[-1]
            slug = name_to_slug.get(key) or (name_to_slug.get(base) if base.endswith(".md") else None)
            if slug:
                return f'<a class="xref" href="#doc-{slug}"><code>{inner}</code></a>'
            return m.group(0)

        body = re.sub(r"<code>(.*?)</code>", code_sub, body, flags=re.S)
        body = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', body)
        d["html"] = body
        d["title"] = next((h["text"] for h in headings if h["doc"] == d["slug"]), d["name"])
        d["bytes"] = len(text)
    return headings

# ---------------------------------------------------------------------------
# structured sources
# ---------------------------------------------------------------------------

def parse_items(headings, doc_slug, prefix):
    """Group headings that name OI-n / A-n into items (file order)."""
    items = {}
    pat = re.compile(rf"\b{prefix}-(\d+)\b")
    for h in headings:
        if h["doc"] != doc_slug or h["level"] > 3:
            continue
        nums = [int(x) for x in pat.findall(h["text"])]
        if not nums:
            continue
        lead = re.match(rf"^\W*{prefix}-(\d+)", clean_title(h["text"]))
        for num in nums:
            it = items.setdefault(num, {"num": num, "title": "", "sev": "", "headings": [], "raw": [],
                                        "first": h["id"]})
            it["headings"].append({"id": h["id"], "text": clean_title(h["text"])})
            it["raw"].append(h["text"])
            if not it["title"] and lead and int(lead.group(1)) == num:
                t = re.sub(rf"^{prefix}-\d+\s*[.—–:-]*\s*", "", clean_title(h["text"]))
                it["title"], it["sev"], it["first"] = t, severity_of(h["text"]), h["id"]
    for it in items.values():
        if not it["title"]:
            it["title"] = re.sub(rf"^.*?{prefix}-\d+\s*[.—–:-]*\s*", "", it["headings"][0]["text"])
            it["sev"] = severity_of(it["raw"][0])
        # "marked": some heading for the item carries a check mark or says RESOLVED/ANSWERED
        it["resolved"] = any("✅" in r or re.search(r"\b(RESOLVED|ANSWERED)\b", r) for r in it["raw"])
        it["updates"] = len(it["headings"]) - 1
        it["latest"] = it["headings"][-1]["text"]
    return items


def load_chronology():
    with open(ROOT / "03-chronology" / "chronology.csv", newline="", encoding="utf-8") as f:
        return [r for r in csv.DictReader(f)]


def load_manifest():
    with open(ROOT / "01-verified-facts" / "drive-sweep" / "master-manifest.csv", newline="",
              encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    out = []
    for r in rows:
        parts = r["path"].split("/")
        folder = parts[1] if len(parts) > 2 else "(root)"
        is_folder = r["mimeType"] == "application/vnd.google-apps.folder"
        name = parts[-1]
        flag = ""
        if re.search(r"/Leal Trust/Partnership/|/Land Acquisition/", r["path"]) or \
                re.search(r"rebuttal|refutation|\bdraft\b|copy of", name, re.I):
            flag = "draft"
        out.append({"n": name, "p": "/".join(parts[1:-1]), "f": folder, "id": r["drive_id"],
                    "t": "folder" if is_folder else (r["mimeType"].split("/")[-1].split(".")[-1][:18]),
                    "m": r["modifiedTime"], "s": r["sizeBytes"], "x": flag})
    return out


def load_sources():
    text = (ROOT / "01-verified-facts" / "source-register.md").read_text(encoding="utf-8")
    out = []
    for line in text.splitlines():
        m = re.match(r"^\|\s*(S-\d+)\s*\|(.*)\|\s*$", line)
        if not m:
            continue
        cells = [c.strip() for c in m.group(2).split("|")]
        title = re.sub(r"\*\*|`", "", cells[0])
        ids = [i for i in re.findall(r"\b1[A-Za-z0-9_-]{24,48}\b", " ".join(cells[1:2]) + " " + cells[0])
               if DRIVE_ID.match(i) and not GMAIL_ID.match(i)]
        gm = re.findall(r"\b1[0-9a-f]{15}\b", " ".join(cells))
        local = re.findall(r"01-verified-facts/[\w./-]+\.(?:png|pdf)", " ".join(cells))
        nature = re.sub(r"\*\*|`", "", cells[-1]) if len(cells) > 1 else ""
        date = cells[2] if len(cells) >= 4 else ""
        out.append({"id": m.group(1), "title": title, "drive": ids[:2], "gmail": gm[:8],
                    "local": local[:2], "date": re.sub(r"\*\*|`", "", date), "nature": nature})
    out.sort(key=lambda s: int(s["id"].split("-")[1]))
    return out


def load_tracker():
    with open(HERE / "rfp-tracker.csv", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def evidence_assets():
    out = []
    try:
        from PIL import Image
    except Exception:
        Image = None
    for fname, label in EVIDENCE:
        p = ROOT / "01-verified-facts" / fname
        if not p.exists():
            continue
        data, mime = p.read_bytes(), "image/png"
        if Image is not None:
            im = Image.open(p).convert("RGB")
            im.thumbnail((900, 2400))
            buf = io.BytesIO()
            im.save(buf, "JPEG", quality=72, optimize=True)
            data, mime = buf.getvalue(), "image/jpeg"
        out.append({"label": label, "file": fname,
                    "src": f"data:{mime};base64,{base64.b64encode(data).decode()}"})
    pdf = None
    p = ROOT / "01-verified-facts" / EVIDENCE_PDF[0]
    if p.exists():
        pdf = {"label": EVIDENCE_PDF[1], "file": EVIDENCE_PDF[0],
               "b64": base64.b64encode(p.read_bytes()).decode()}
    return out, pdf

# ---------------------------------------------------------------------------
# page pieces
# ---------------------------------------------------------------------------

CSS = r"""
/* Layout: a court-file binder. Caption block on top, tabbed dividers, dense tables. */
:root{
  --bg:#f3f5f8; --surface:#ffffff; --sunk:#eaeef3; --ink:#18212c; --muted:#5a6676; --line:#d6dce4;
  --accent:#23527c; --accent-ink:#ffffff; --accent-soft:#e3ecf5; --priv:#8f1f1f; --priv-soft:#f8e9e7;
  --crit:#b42318; --crit-soft:#fbe9e7; --high:#a8510a; --high-soft:#fdf0e1; --med:#7a6300; --med-soft:#fbf5d9;
  --ok:#1e7448; --ok-soft:#e5f4ec; --link:#1f5f99;
  --font-display:"Iowan Old Style","Palatino Linotype","Book Antiqua",Palatino,Georgia,serif;
  --font-body:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  --font-mono:ui-monospace,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace;
  --radius:6px; color-scheme:light;
}
@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){
  --bg:#0f141a; --surface:#161d26; --sunk:#1b2430; --ink:#e5eaf0; --muted:#9aa6b4; --line:#2a3441;
  --accent:#7fb0e0; --accent-ink:#0f141a; --accent-soft:#1b2b3c; --priv:#e59a94; --priv-soft:#2a1716;
  --crit:#f08a7e; --crit-soft:#2c1715; --high:#f0a862; --high-soft:#2a1d10; --med:#e2c75c; --med-soft:#26220f;
  --ok:#72cf9c; --ok-soft:#12261b; --link:#8cbcf0; color-scheme:dark; } }
:root[data-theme="dark"]{
  --bg:#0f141a; --surface:#161d26; --sunk:#1b2430; --ink:#e5eaf0; --muted:#9aa6b4; --line:#2a3441;
  --accent:#7fb0e0; --accent-ink:#0f141a; --accent-soft:#1b2b3c; --priv:#e59a94; --priv-soft:#2a1716;
  --crit:#f08a7e; --crit-soft:#2c1715; --high:#f0a862; --high-soft:#2a1d10; --med:#e2c75c; --med-soft:#26220f;
  --ok:#72cf9c; --ok-soft:#12261b; --link:#8cbcf0; color-scheme:dark; }
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 var(--font-body)}
a{color:var(--link)} a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.privband{background:var(--priv-soft);color:var(--priv);font:600 11px/1.4 var(--font-body);letter-spacing:.08em;text-transform:uppercase;text-align:center;padding:6px 16px;border-bottom:1px solid var(--line)}
header.top{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--surface);border-bottom:1px solid var(--line)}
.topin{max-width:1240px;margin:0 auto;padding-inline:16px;display:flex;flex-wrap:wrap;align-items:center;gap:8px 20px;padding-block:10px 0}
.brand{font:600 19px/1.2 var(--font-display);letter-spacing:.01em;margin:0}
.brand small{display:block;font:500 12px/1.3 var(--font-body);color:var(--muted);letter-spacing:0}
.tools{margin-left:auto;display:flex;gap:8px;align-items:center}
nav.tabs{max-width:1240px;margin:0 auto;padding-inline:16px;display:flex;gap:2px;overflow-x:auto;scrollbar-width:thin}
nav.tabs a{flex:none;text-decoration:none;color:var(--muted);font:600 13px/1 var(--font-body);padding:12px 12px 11px;border-bottom:3px solid transparent;white-space:nowrap}
nav.tabs a[aria-current="page"]{color:var(--ink);border-bottom-color:var(--accent)}
nav.tabs a .ct{font:500 11px var(--font-mono);color:var(--muted);margin-left:4px}
main{max-width:1240px;margin:0 auto;padding-inline:16px;padding-block:20px 60px}
section.tab{display:block} section.tab[hidden]{display:none!important}
h2.sec{font:600 22px/1.25 var(--font-display);margin:0 0 4px;text-wrap:balance}
p.lede{margin:0 0 18px;color:var(--muted);max-width:75ch}
h3.sub{font:600 13px/1.3 var(--font-body);text-transform:uppercase;letter-spacing:.07em;color:var(--muted);margin:26px 0 10px}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,460px),1fr));gap:16px}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,330px),1fr));gap:16px}
.panel{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:16px;min-width:0}
.caption{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);display:grid;grid-template-columns:minmax(0,1.6fr) minmax(0,1fr)}
.caption .court{grid-column:1/-1;text-align:center;font:600 12px/1.4 var(--font-body);letter-spacing:.09em;text-transform:uppercase;color:var(--muted);padding:10px 16px;border-bottom:1px solid var(--line)}
.caption .parties{padding:14px 16px;border-right:1px solid var(--line);font:15px/1.5 var(--font-display)}
.caption .parties .v{margin:6px 0;color:var(--muted);font-style:italic}
.caption dl{margin:0;padding:14px 16px;display:grid;grid-template-columns:auto 1fr;gap:6px 12px;font-size:14px}
.caption dt{color:var(--muted)} .caption dd{margin:0;font-weight:600}
.caption .src{grid-column:1/-1;border-top:1px solid var(--line);padding:6px 16px;font-size:12px;color:var(--muted)}
@media (max-width:640px){.caption{grid-template-columns:1fr}.caption .parties{border-right:0;border-bottom:1px solid var(--line)}}
.dates{list-style:none;margin:0;padding:0;display:grid;gap:0}
.dates li{display:grid;grid-template-columns:96px 1fr;gap:4px 12px;padding:10px 0;border-top:1px solid var(--line)}
.dates li:first-child{border-top:0}
.dates .d{font:600 13px var(--font-mono);font-variant-numeric:tabular-nums}
.dates .s{grid-column:2;font-size:12px;color:var(--muted)}
.chip{display:inline-flex;align-items:center;gap:4px;font:600 11px/1 var(--font-body);letter-spacing:.03em;padding:4px 7px;border-radius:999px;background:var(--sunk);color:var(--muted);white-space:nowrap;vertical-align:1px}
.chip.crit{background:var(--crit-soft);color:var(--crit)} .chip.high{background:var(--high-soft);color:var(--high)}
.chip.med{background:var(--med-soft);color:var(--med)} .chip.low,.chip.ok,.chip.done{background:var(--ok-soft);color:var(--ok)}
.chip.soon,.chip.confirm{background:var(--high-soft);color:var(--high)} .chip.counsel{background:var(--accent-soft);color:var(--accent)}
.chip.accent{background:var(--accent-soft);color:var(--accent)}
.stats{display:flex;flex-wrap:wrap;gap:10px;margin:14px 0 0}
.stat{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:10px 14px;min-width:120px;text-decoration:none;color:inherit}
.stat b{display:block;font:600 22px/1.1 var(--font-display);font-variant-numeric:tabular-nums}
.stat span{font-size:12px;color:var(--muted)}
ul.plain{margin:0;padding-left:18px} ul.plain li{margin:6px 0}
.todo{list-style:none;margin:0;padding:0} .todo li{display:grid;grid-template-columns:62px 1fr;gap:10px;padding:8px 0;border-top:1px solid var(--line)} .todo li:first-child{border-top:0}
.ref{font:600 12px var(--font-mono);color:var(--accent);text-decoration:none;white-space:nowrap}
.cite{font-size:12px;color:var(--muted)}
.standing{display:grid;gap:12px}
.standing div b{display:block}
table.data{width:100%;border-collapse:collapse;font-size:13.5px;background:var(--surface)}
table.data th{text-align:left;font:600 11px/1.3 var(--font-body);text-transform:uppercase;letter-spacing:.06em;color:var(--muted);background:var(--sunk);padding:8px 10px;border-bottom:1px solid var(--line);position:sticky;top:0}
table.data td{padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}
table.data td.num,table.data td.mono{font-family:var(--font-mono);font-size:12.5px;font-variant-numeric:tabular-nums;white-space:nowrap}
.tablewrap{overflow-x:auto;border:1px solid var(--line);border-radius:var(--radius);max-height:72vh}
.filters{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 12px;align-items:center}
.filters input[type=search],.filters select{font:14px var(--font-body);padding:8px 10px;border:1px solid var(--line);border-radius:var(--radius);background:var(--surface);color:var(--ink);min-width:0}
.filters input[type=search]{flex:1 1 260px}
.filters .count{font-size:12px;color:var(--muted);font-variant-numeric:tabular-nums}
button.btn{font:600 13px var(--font-body);padding:8px 12px;border-radius:var(--radius);border:1px solid var(--line);background:var(--surface);color:var(--ink);cursor:pointer}
button.btn:hover{border-color:var(--accent)}
.issue h3{font:600 18px/1.3 var(--font-display);margin:0 0 6px;text-wrap:balance}
.issue ul.pts{margin:10px 0;padding-left:18px} .issue ul.pts li{margin:6px 0}
.issue .docs{margin:10px 0 0;padding:10px 0 0;border-top:1px solid var(--line);display:grid;gap:4px;font-size:13.5px}
.issue .refs{margin-top:10px;display:flex;flex-wrap:wrap;gap:6px}
a.doc::before{content:"↗ ";color:var(--muted)}
.refs a{text-decoration:none}
.lib{display:grid;grid-template-columns:280px minmax(0,1fr);gap:20px;align-items:start}
@media (max-width:860px){.lib{grid-template-columns:1fr}}
.libnav{position:sticky;top:110px;max-height:calc(100vh - 130px);overflow:auto;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:10px}
@media (max-width:860px){.libnav{position:static;max-height:300px}}
.libnav h4{font:600 11px/1.3 var(--font-body);text-transform:uppercase;letter-spacing:.07em;color:var(--muted);margin:12px 6px 4px}
.libnav a{display:block;padding:5px 6px;border-radius:4px;text-decoration:none;color:var(--ink);font-size:13px;line-height:1.35}
.libnav a[aria-current="true"]{background:var(--accent-soft);color:var(--accent);font-weight:600}
.doc-body{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:22px clamp(16px,3vw,36px);min-width:0}
.doc-body .path{font:12px var(--font-mono);color:var(--muted);margin-bottom:10px;word-break:break-all}
.md{max-width:82ch;font-size:15px}
.md h1,.md h2,.md h3,.md h4{font-family:var(--font-display);line-height:1.3;text-wrap:balance;scroll-margin-top:120px}
.md h1{font-size:24px;margin:.2em 0 .6em} .md h2{font-size:20px;margin:1.6em 0 .5em;padding-top:.6em;border-top:1px solid var(--line)} .md h3{font-size:17px;margin:1.3em 0 .4em} .md h4{font-size:15px}
.md table{border-collapse:collapse;font-size:13.5px;margin:12px 0;display:block;overflow-x:auto;max-width:100%}
.md th,.md td{border:1px solid var(--line);padding:6px 8px;vertical-align:top;text-align:left}
.md th{background:var(--sunk)}
.md blockquote{margin:12px 0;padding:8px 14px;border-left:3px solid var(--accent);background:var(--accent-soft);color:var(--ink)}
.md code{font:13px var(--font-mono);background:var(--sunk);padding:1px 4px;border-radius:3px;word-break:break-all}
.md pre{overflow-x:auto;background:var(--sunk);padding:10px;border-radius:var(--radius)}
.md a.drive code{border-bottom:1px dotted var(--link);color:var(--link)}
.md code.gmail{color:var(--muted)}
.hit{background:var(--med-soft);outline:2px solid var(--med);border-radius:2px}
.results{display:grid;gap:6px;margin:0 0 14px}
.results a{display:block;padding:8px 10px;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);text-decoration:none;color:var(--ink)}
.results a small{display:block;color:var(--muted);font-size:12px}
.gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,220px),1fr));gap:14px}
.gallery figure{margin:0;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:8px}
.gallery img{width:100%;height:220px;object-fit:cover;object-position:top;border-radius:4px;cursor:zoom-in;background:var(--sunk)}
.gallery figcaption{font-size:12.5px;margin-top:6px}
dialog#viewer{max-width:min(96vw,980px);width:100%;border:1px solid var(--line);border-radius:var(--radius);background:var(--surface);color:var(--ink);padding:0}
dialog#viewer::backdrop{background:rgba(10,14,20,.6)}
dialog#viewer .bar{display:flex;justify-content:space-between;align-items:center;padding:8px 12px;border-bottom:1px solid var(--line);font-size:13px}
dialog#viewer .scroll{max-height:82vh;overflow:auto;padding:10px;text-align:center}
dialog#viewer img{max-width:100%}
.note{font-size:13px;color:var(--muted);background:var(--sunk);border-radius:var(--radius);padding:10px 12px;margin:0 0 14px}
footer{max-width:1240px;margin:0 auto;padding-inline:16px;padding-block:0 30px;font-size:12px;color:var(--muted)}
@media (prefers-reduced-motion:reduce){*{scroll-behavior:auto!important}}
@media print{header.top,nav.tabs,.filters,.libnav{display:none} section.tab[hidden]{display:block!important}}
"""

JS = r"""
(function(){
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>Array.from(r.querySelectorAll(s));
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const DRIVE=id=>'https://drive.google.com/open?id='+encodeURIComponent(id);
const data=id=>{const el=document.getElementById(id);return el?JSON.parse(el.textContent):null};
const store={get(k){try{return localStorage.getItem(k)}catch(e){return null}},set(k,v){try{localStorage.setItem(k,v)}catch(e){}}};

/* theme */
const themeBtn=$('#theme');
function applyTheme(t){ if(t==='light'||t==='dark'){document.documentElement.setAttribute('data-theme',t)}else{document.documentElement.removeAttribute('data-theme')} if(themeBtn) themeBtn.textContent='Theme: '+(t||'system'); }
applyTheme(store.get('leal-theme'));
if(themeBtn) themeBtn.addEventListener('click',()=>{const cur=store.get('leal-theme')||'system';const nx=cur==='system'?'light':cur==='light'?'dark':'system';store.set('leal-theme',nx==='system'?'':nx);applyTheme(nx==='system'?'':nx)});

/* tabs and deep links */
const tabs=$$('section.tab');
function showTab(name){ let hit=false; tabs.forEach(t=>{const on=t.id===name; t.hidden=!on; hit=hit||on}); if(!hit&&tabs[0]){tabs[0].hidden=false; name=tabs[0].id}
  $$('nav.tabs a').forEach(a=>a.setAttribute('aria-current',a.getAttribute('href')==='#'+name?'page':'false')); }
function route(){ const h=decodeURIComponent(location.hash.slice(1));
  if(!h){showTab(tabs[0]?tabs[0].id:'');return}
  if(h.startsWith('doc-')){showTab('library'); openDoc(h.slice(4)); window.scrollTo(0,0); return}
  const el=document.getElementById(h);
  if(el && el.closest('.doc-body')){ showTab('library'); const d=el.closest('article.libdoc'); if(d) openDoc(d.dataset.slug,true); requestAnimationFrame(()=>el.scrollIntoView({block:'start'})); return }
  if(document.getElementById(h) && document.getElementById(h).classList.contains('tab')){showTab(h); window.scrollTo(0,0); return}
  showTab(tabs[0].id);
}
window.addEventListener('hashchange',route);

/* library */
function openDoc(slug,keep){ $$('article.libdoc').forEach(a=>a.hidden=a.dataset.slug!==slug); $$('.libnav a').forEach(a=>a.setAttribute('aria-current',a.dataset.slug===slug?'true':'false')); store.set('leal-doc',slug); }
const libq=$('#libq');
if(libq){ let t; libq.addEventListener('input',()=>{clearTimeout(t); t=setTimeout(libSearch,220)}); }
function libSearch(){ const q=libq.value.trim().toLowerCase(); const out=$('#libresults'); out.innerHTML='';
  if(q.length<3){ out.hidden=true; return }
  const hits=[]; for(const art of $$('article.libdoc')){ const title=art.dataset.title; let lastH=null;
    for(const el of art.querySelectorAll('h1,h2,h3,h4,p,li,td,blockquote')){ if(/^H[1-4]$/.test(el.tagName)) lastH=el;
      const tx=el.textContent; const i=tx.toLowerCase().indexOf(q); if(i<0) continue;
      const anchor=(/^H/.test(el.tagName)?el:lastH); hits.push({title, sec:anchor?anchor.textContent:'', id:anchor?anchor.id:'doc-'+art.dataset.slug, snip:tx.slice(Math.max(0,i-70),i+110)});
      if(hits.length>=80) break; }
    if(hits.length>=80) break; }
  out.hidden=false; out.innerHTML='<p class="cite">'+hits.length+(hits.length>=80?'+':'')+' matches</p>'+hits.map(h=>'<a href="#'+esc(h.id)+'"><b>'+esc(h.title)+'</b><small>'+esc(h.sec)+'</small><small>…'+esc(h.snip)+'…</small></a>').join('');
}

/* generic row filter for server-rendered tables */
$$('[data-filter-for]').forEach(inp=>{ const tbl=document.getElementById(inp.dataset.filterFor); const cnt=document.getElementById(inp.dataset.count);
  const sel=inp.dataset.select?document.getElementById(inp.dataset.select):null;
  const run=()=>{ const q=inp.value.trim().toLowerCase(); const sv=sel?sel.value:''; let n=0;
    $$('tbody tr',tbl).forEach(tr=>{ const ok=(!q||tr.dataset.s.includes(q))&&(!sv||tr.dataset.k===sv||(tr.dataset.k||'').split(' ').includes(sv)); tr.hidden=!ok; if(ok)n++ }); if(cnt) cnt.textContent=n+' shown'; };
  inp.addEventListener('input',run); if(sel) sel.addEventListener('change',run); run(); });

/* timeline */
const chron=data('chron-data');
if(chron){ const body=$('#tl-body'), q=$('#tlq'), cat=$('#tlcat'), cnt=$('#tlcount');
  const cats=[...new Set(chron.map(r=>r.category))].sort(); cat.innerHTML='<option value="">All categories</option>'+cats.map(c=>'<option>'+esc(c)+'</option>').join('');
  const run=()=>{ const s=q.value.trim().toLowerCase(), c=cat.value; const rows=chron.filter(r=>(!c||r.category===c)&&(!s||(r.date+' '+r.event+' '+r.source+' '+r.citation).toLowerCase().includes(s)));
    cnt.textContent=rows.length+' of '+chron.length;
    body.innerHTML=rows.map(r=>'<tr><td class="mono">'+esc(r.date)+'<br><span class="cite">'+esc(r.date_certainty)+'</span></td><td>'+esc(r.event)+(r.source_is_brief_only==='TRUE'?' <span class="chip high">brief only</span>':'')+'</td><td><span class="chip">'+esc(r.category)+'</span></td><td class="cite">'+esc(r.source)+'<br>'+esc(r.citation)+'</td></tr>').join(''); };
  q.addEventListener('input',run); cat.addEventListener('change',run); run(); }

/* drive manifest */
const man=data('manifest-data');
if(man){ const body=$('#mf-body'), q=$('#mfq'), fol=$('#mffolder'), typ=$('#mftype'), cnt=$('#mfcount'), more=$('#mfmore'); let limit=250;
  const fols=[...new Set(man.map(r=>r.f))].sort(); fol.innerHTML='<option value="">All folders</option>'+fols.map(c=>'<option>'+esc(c)+'</option>').join('');
  const run=()=>{ const s=q.value.trim().toLowerCase(), f=fol.value, t=typ.value; const rows=man.filter(r=>(!f||r.f===f)&&(!t||(t==='folder'?r.t==='folder':t==='draft'?r.x==='draft':r.t!=='folder'))&&(!s||(r.n+' '+r.p).toLowerCase().includes(s)));
    cnt.textContent=rows.length+' of '+man.length;
    body.innerHTML=rows.slice(0,limit).map(r=>'<tr><td><a href="'+DRIVE(r.id)+'" target="_blank" rel="noopener">'+esc(r.n)+'</a>'+(r.x==='draft'?' <span class="chip high">client draft: privilege review</span>':'')+'<div class="cite">'+esc(r.p)+'</div></td><td class="mono">'+esc(r.t)+'</td><td class="mono">'+esc(r.m)+'</td></tr>').join('');
    more.hidden=rows.length<=limit; };
  more.addEventListener('click',()=>{limit+=500;run()}); [q,fol,typ].forEach(e=>e.addEventListener(e.tagName==='INPUT'?'input':'change',()=>{limit=250;run()})); run(); }

/* evidence viewer */
const dlg=$('#viewer');
$$('.gallery img').forEach(img=>img.addEventListener('click',()=>{ if(!dlg) return; $('#viewer .ttl').textContent=img.alt; $('#viewer img').src=img.src; dlg.showModal(); }));
const vclose=$('#viewer .close'); if(vclose) vclose.addEventListener('click',()=>dlg.close());
const pdfBtn=$('#openpdf'); if(pdfBtn){ pdfBtn.addEventListener('click',()=>{ const b64=data('pdf-data'); const bin=atob(b64); const u8=new Uint8Array(bin.length); for(let i=0;i<bin.length;i++) u8[i]=bin.charCodeAt(i);
  const url=URL.createObjectURL(new Blob([u8],{type:'application/pdf'})); const w=window.open(url,'_blank'); if(!w){ location.href=url; } }); }

const last=store.get('leal-doc'); const first=$('article.libdoc'); openDoc(last && document.querySelector('article.libdoc[data-slug="'+CSS.escape(last)+'"]')?last:(first?first.dataset.slug:''));
route();
})();
"""


def chip(cls, text):
    return f'<span class="chip {esc(cls)}">{esc(text)}</span>'


def fmt_date(d):
    if not d:
        return "—"
    try:
        return datetime.strptime(d, "%Y-%m-%d").strftime("%-m/%-d/%Y")
    except ValueError:
        return d


def ref_link(ref, oi_items, a_items, oi_doc, a_doc):
    m = re.match(r"^(OI|A)-(\d+)$", ref)
    if m:
        kind, num = m.group(1), int(m.group(2))
        items = oi_items if kind == "OI" else a_items
        it = items.get(num)
        if it:
            return f'<a class="ref" href="#{esc(it["first"])}" title="{esc(it["title"])}">{esc(ref)}</a>'
    return f'<span class="ref">{esc(ref)}</span>'


def page_head(title, desc):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
            f'<meta name="robots" content="noindex,nofollow"><meta name="description" content="{esc(desc)}">'
            f'<title>{esc(title)}</title><style>{CSS}</style></head><body>')


def build():
    warnings = []
    docs = collect_library()
    headings = render_library(docs)
    oi_doc = slugify("05-for-brandon/open_items.md")
    a_doc = slugify("04-adverse-analysis/adverse_analysis.md")
    oi_items = parse_items(headings, oi_doc, "OI")
    a_items = parse_items(headings, a_doc, "A")
    chron = load_chronology()
    manifest = load_manifest()
    sources = load_sources()
    tracker = load_tracker()
    images, pdf = evidence_assets()
    rev = git_rev()
    built = datetime.now().strftime("%-m/%-d/%Y %H:%M")

    for iss in ISSUES:
        for n in iss["a"]:
            if n not in a_items:
                warnings.append(f"issue '{iss['title']}': A-{n} not found")
        for n in iss["oi"]:
            if n not in oi_items:
                warnings.append(f"issue '{iss['title']}': OI-{n} not found")
        for lib in iss["library"]:
            if not (ROOT / lib).exists():
                warnings.append(f"issue '{iss['title']}': library file {lib} missing")

    R = lambda ref: ref_link(ref, oi_items, a_items, oi_doc, a_doc)
    open_oi = [i for i in oi_items.values() if not i["resolved"]]
    crit_open = [i for i in open_oi if i["sev"] == "crit"]

    # ---------------- overview
    cap = CAPTION
    caption = (f'<div class="caption"><div class="court">{esc(cap["court"])}</div>'
               f'<div class="parties">{esc(cap["plaintiff"])}<div class="v">v.</div>{esc(cap["defendants"])}</div>'
               '<dl>' + "".join(f"<dt>{esc(k)}</dt><dd>{esc(v)}</dd>" for k, v in cap["right"]) +
               f'</dl><div class="src">Source: {esc(cap["source"])}</div></div>')
    state_label = {"confirm": "confirm on docket", "soon": "client action", "counsel": "counsel calendars",
                   "done": "past"}
    dates = '<ul class="dates">' + "".join(
        f'<li><span class="d">{esc(fmt_date(d))}</span><span>{esc(lbl)} {chip(st, state_label[st])}</span>'
        f'<span class="s">{esc(src)}</span></li>' for d, lbl, st, src in KEY_DATES) + "</ul>"
    people = ('<div class="tablewrap" style="max-height:none"><table class="data"><thead><tr><th>Side</th><th>Who</th><th>Role</th><th>Source</th></tr></thead><tbody>' +
              "".join(f"<tr><td>{esc(g)}</td><td><b>{esc(n)}</b></td><td>{esc(r)}</td><td class='cite'>{esc(s)}</td></tr>"
                      for g, n, r, s in PEOPLE) + "</tbody></table></div>")
    todo_c = '<ul class="todo">' + "".join(f"<li>{R(r)}<span>{esc(t)}</span></li>" for r, t in THIS_WEEK_CLIENT) + "</ul>"
    todo_l = '<ul class="todo">' + "".join(f"<li>{R(r)}<span>{esc(t)}</span></li>" for r, t in THIS_WEEK_COUNSEL) + "</ul>"
    standing = '<div class="standing">' + "".join(
        f'<div><b>{esc(h)}</b>{esc(t)} <span class="cite">({esc(s)})</span></div>' for h, t, s in STANDING) + "</div>"
    stats = ('<div class="stats">'
             f'<a class="stat" href="#open-items"><b>{len(open_oi)}</b><span>open items, not marked answered ({len(crit_open)} red)</span></a>'
             f'<a class="stat" href="#red-team"><b>{len(a_items)}</b><span>red-team items</span></a>'
             f'<a class="stat" href="#discovery"><b>{len(tracker)}</b><span>demands to answer</span></a>'
             f'<a class="stat" href="#timeline"><b>{len(chron)}</b><span>dated events</span></a>'
             f'<a class="stat" href="#documents"><b>{len(manifest):,}</b><span>Drive items indexed</span></a>'
             f'<a class="stat" href="#library"><b>{len(docs)}</b><span>memos in the library</span></a></div>')
    overview = (f'<section class="tab" id="overview"><h2 class="sec">Where the case stands</h2>'
                f'<p class="lede">Built {esc(built)} from the case workspace (revision {esc(rev)}). Every line carries its source; '
                'S-numbers are the source register, A-numbers the red-team file, OI-numbers the open-items register.</p>'
                f'{caption}{stats}'
                f'<div class="grid2" style="margin-top:16px"><div class="panel"><h3 class="sub" style="margin-top:0">Key dates</h3>{dates}</div>'
                f'<div class="panel"><h3 class="sub" style="margin-top:0">Posture</h3>{standing}</div></div>'
                f'<div class="grid2" style="margin-top:16px"><div class="panel"><h3 class="sub" style="margin-top:0">This week: client</h3>{todo_c}</div>'
                f'<div class="panel"><h3 class="sub" style="margin-top:0">This week: counsel decisions</h3>{todo_l}</div></div>'
                f'<h3 class="sub">People</h3>{people}'
                '<h3 class="sub">Using this page</h3><div class="note">Document links open Google Drive and work only if the case folder '
                '(“Leal Trust Administration Litigation”, owner jaceleal@gmail.com) is shared with you. Gmail thread IDs refer to the '
                'client\'s mailbox; ask Jace for the message. Memos are in the Library tab. Everything here is attorney work product '
                'and includes AI-assisted analysis; use the separate Document Index page for production planning.</div></section>')

    # ---------------- issues
    cards = []
    for iss in ISSUES:
        pts = "".join(f'<li>{esc(t)} <span class="cite">({esc(s)})</span></li>' for t, s in iss["points"])
        dl = "".join(drive_link(l, i) for l, i in iss["docs"]) or '<span class="cite">No Drive documents; see the library and evidence.</span>'
        libs = " ".join(f'<a class="chip accent" href="#doc-{slugify(p)}">{esc(Path(p).stem)}</a>' for p in iss["library"])
        refs = " ".join(R(f"A-{n}") for n in iss["a"]) + " " + " ".join(R(f"OI-{n}") for n in iss["oi"])
        cards.append(f'<article class="panel issue"><h3>{esc(iss["title"])}</h3>{chip("accent", iss["tag"])}'
                     f'<ul class="pts">{pts}</ul><div class="docs"><span class="cite">Key documents</span>{dl}</div>'
                     f'<div class="refs">{libs}</div><div class="refs">{refs}</div></article>')
    issues = ('<section class="tab" id="issues" hidden><h2 class="sec">Issues</h2><p class="lede">Each card gives the short version with sources, '
              'the documents that matter (one click to Drive), our memos, and the red-team and open-item numbers.</p>'
              f'<div class="grid2">{"".join(cards)}</div></section>')

    # ---------------- discovery
    status_cls = {"To collect": "high", "Partly collected": "med", "Collected": "ok", "Produced": "done",
                  "Objection": "counsel"}
    rows = []
    for t in tracker:
        inhand = []
        for part in [p for p in t["in_hand"].split(";") if p.strip()]:
            lbl, _, did = part.partition("|")
            inhand.append(drive_link(lbl.strip(), did.strip()) if did.strip() else esc(lbl))
        refs = " ".join(R(r.strip()) if re.match(r"^(OI|A)-\d+$", r.strip()) else f'<span class="cite">{esc(r.strip())}</span>'
                        for r in t["refs"].split(";") if r.strip())
        s = " ".join([t["demand"], t["topic"], t["to_pull"], t["notes"], t["in_hand"]]).lower()
        rows.append(f'<tr data-s="{esc(s)}" data-k="{esc(t["status"])}"><td class="num">{esc(t["demand"])}</td>'
                    f'<td><b>{esc(t["topic"])}</b><div class="cite" style="margin-top:4px">{esc(t["notes"])}</div></td>'
                    f'<td>{chip(status_cls.get(t["status"], ""), t["status"])}{("<div class=cite>Produced: " + esc(t["produced_ref"]) + "</div>") if t["produced_ref"] else ""}</td>'
                    f'<td><div style="display:grid;gap:3px">{"".join(inhand) or "<span class=cite>None yet</span>"}</div></td>'
                    f'<td>{esc(t["to_pull"])}</td><td>{refs}</td></tr>')
    statuses = sorted({t["status"] for t in tracker})
    discovery = ('<section class="tab" id="discovery" hidden><h2 class="sec">Demand for Production, Set One</h2>'
                 '<p class="lede">Served 9/28/2026 by mail and email on Ormonde (S-38). Status comes from '
                 '<code>07-attorney-dashboard/rfp-tracker.csv</code> and is updated when documents are collected or produced. '
                 'Objections, privilege and the response date are counsel\'s calls. Full analysis: '
                 f'<a href="#doc-{slugify("05-for-brandon/rfp-set-one-response-map.md")}">response map</a>.</p>'
                 '<div class="filters"><input type="search" id="dq" placeholder="Filter demands" aria-label="Filter demands" '
                 'data-filter-for="dtable" data-count="dcount" data-select="dstatus">'
                 '<select id="dstatus" aria-label="Status"><option value="">All statuses</option>' +
                 "".join(f"<option>{esc(s)}</option>" for s in statuses) + '</select><span class="count" id="dcount"></span></div>'
                 '<div class="tablewrap"><table class="data" id="dtable"><thead><tr><th>#</th><th>Demand</th><th>Status</th>'
                 '<th>Already in Drive</th><th>Still to pull</th><th>Refs</th></tr></thead><tbody>' + "".join(rows) +
                 '</tbody></table></div></section>')

    # ---------------- open items / red team
    def item_table(items, kind, tid):
        rows = []
        for it in sorted(items.values(), key=lambda x: x["num"]):
            sev = it["sev"]
            sevtxt = {"crit": "red", "high": "orange", "med": "yellow", "low": "green"}.get(sev, "")
            state = "marked" if (kind == "OI" and it["resolved"]) else ("open" if kind == "OI" else "")
            k = " ".join(x for x in [sevtxt, state] if x)
            upd = it["headings"][1:]
            latest = (f'<div class="cite">Latest: <a href="#{esc(upd[-1]["id"])}">{esc(upd[-1]["text"][:150])}</a>'
                      f'{" (+" + str(len(upd) - 1) + " earlier)" if len(upd) > 1 else ""}</div>') if upd else ""
            s = (f'{kind}-{it["num"]} ' + it["title"] + " " + " ".join(h["text"] for h in it["headings"])).lower()
            badges = (chip(sev, sevtxt) if sevtxt else "") + (" " + chip("done", "marked answered") if state == "marked" else "")
            rows.append(f'<tr data-s="{esc(s)}" data-k="{esc(k)}"><td class="num"><a class="ref" href="#{esc(it["first"])}">{kind}-{it["num"]}</a></td>'
                        f'<td><a href="#{esc(it["first"])}" style="color:inherit;text-decoration:none"><b>{esc(it["title"])}</b></a>{latest}</td>'
                        f'<td>{badges}</td><td class="num">{it["updates"]}</td></tr>')
        sel = '<option value="">All</option><option value="red">Red</option><option value="orange">Orange</option><option value="yellow">Yellow</option>'
        if kind == "OI":
            sel += '<option value="open">Open</option><option value="marked">Marked answered</option>'
        return ('<div class="filters">'
                f'<input type="search" id="{tid}q" placeholder="Filter by number or words" aria-label="Filter" data-filter-for="{tid}" data-count="{tid}c" data-select="{tid}s">'
                f'<select id="{tid}s" aria-label="Severity or status">{sel}</select><span class="count" id="{tid}c"></span></div>'
                f'<div class="tablewrap"><table class="data" id="{tid}"><thead><tr><th>No.</th><th>Item</th><th>Flag</th><th>Updates</th></tr></thead><tbody>'
                + "".join(rows) + "</tbody></table></div>")

    openitems = ('<section class="tab" id="open-items" hidden><h2 class="sec">Open items</h2>'
                 '<p class="lede">From the open-items register (OI-1 onward). Flags come from the item headings. “Marked answered” means a heading '
                 'for the item carries a check mark or says answered or resolved; part of the item may still be open, so read the latest update. '
                 'Newer updates are appended at the end of the register. Click any item to read it in full.</p>'
                 + item_table(oi_items, "OI", "oit") + "</section>")
    redteam = ('<section class="tab" id="red-team" hidden><h2 class="sec">Red team</h2>'
               '<p class="lede">The case against us, item by item (A-1 onward), with both-ways analysis and dated corrections. '
               'Red flags mark items the file treats as most serious.</p>' + item_table(a_items, "A", "att") + "</section>")

    # ---------------- timeline
    timeline = ('<section class="tab" id="timeline" hidden><h2 class="sec">Timeline</h2>'
                '<p class="lede">The master chronology. Each row carries its source and how certain the date is; '
                '“brief only” marks facts sourced only to a party\'s brief.</p>'
                '<div class="filters"><input type="search" id="tlq" placeholder="Search events, sources, citations" aria-label="Search timeline">'
                '<select id="tlcat" aria-label="Category"></select><span class="count" id="tlcount"></span></div>'
                '<div class="tablewrap"><table class="data"><thead><tr><th>Date</th><th>Event</th><th>Category</th><th>Source</th></tr></thead>'
                '<tbody id="tl-body"></tbody></table></div></section>')

    # ---------------- documents
    src_rows = []
    for s in sources:
        links = [drive_link("Drive", d) for d in s["drive"]]
        links += [f'<span class="cite" title="Gmail thread ID, client mailbox">Gmail {esc(g)}</span>' for g in s["gmail"][:3]]
        links += [f'<span class="cite">workspace: {esc(Path(l).name)}</span>' for l in s["local"]]
        srch = (s["id"] + " " + s["title"] + " " + s["nature"]).lower()
        src_rows.append(f'<tr data-s="{esc(srch)}"><td class="num">{esc(s["id"])}</td><td><b>{esc(s["title"])}</b>'
                        f'<div class="cite">{esc(s["nature"][:360])}{"…" if len(s["nature"]) > 360 else ""}</div></td>'
                        f'<td class="mono">{esc(s["date"][:40])}</td><td><div style="display:grid;gap:3px">{"".join(links) or "<span class=cite>—</span>"}</div></td></tr>')
    gallery = "".join(f'<figure><img src="{im["src"]}" alt="{esc(im["label"])}" loading="lazy"><figcaption>{esc(im["label"])}'
                      f'<div class="cite">{esc(im["file"])}</div></figcaption></figure>' for im in images)
    pdfbtn = (f'<p><button class="btn" id="openpdf">Open: {esc(pdf["label"])}</button> '
              f'<span class="cite">{esc(pdf["file"])}</span></p>') if pdf else ""
    documents = ('<section class="tab" id="documents" hidden><h2 class="sec">Documents</h2>'
                 '<p class="lede">Verified sources first (the documents this workspace actually read, S-1 onward), then every item in the '
                 'case Drive folder as manifested on 8/18/2026, then evidence that arrived by chat and is not in Drive.</p>'
                 '<h3 class="sub">Verified sources</h3><div class="filters"><input type="search" id="sq" placeholder="Filter sources" '
                 'aria-label="Filter sources" data-filter-for="stable" data-count="scount"><span class="count" id="scount"></span></div>'
                 '<div class="tablewrap"><table class="data" id="stable"><thead><tr><th>No.</th><th>Document</th><th>Date</th><th>Open</th></tr></thead><tbody>'
                 + "".join(src_rows) + '</tbody></table></div>'
                 '<h3 class="sub">Case Drive folder (manifest of 8/18/2026)</h3>'
                 '<div class="note">Files added to Drive after 8/18/2026 (for example the 10/2026 QuickBooks exports) appear under Verified sources, '
                 'not here. Items flagged “client draft” sit in the drafts folders or are named as drafts; review for privilege before any production.</div>'
                 '<div class="filters"><input type="search" id="mfq" placeholder="Search file names and folders" aria-label="Search Drive files">'
                 '<select id="mffolder" aria-label="Folder"></select><select id="mftype" aria-label="Type"><option value="">Files and folders</option>'
                 '<option value="file">Files only</option><option value="folder">Folders only</option><option value="draft">Client drafts only</option></select>'
                 '<span class="count" id="mfcount"></span></div><div class="tablewrap"><table class="data"><thead><tr><th>Name</th><th>Type</th>'
                 '<th>Modified</th></tr></thead><tbody id="mf-body"></tbody></table></div><p><button class="btn" id="mfmore" hidden>Show more</button></p>'
                 '<h3 class="sub">Evidence received by chat (not in Drive)</h3>'
                 '<div class="note">These came in as uploads and live in the workspace. Images are reduced copies; ask Jace for the originals. '
                 'They should also be saved to the Drive case folder.</div>'
                 f'{pdfbtn}<div class="gallery">{gallery}</div></section>')

    # ---------------- library
    nav, arts, cur = [], [], None
    for d in docs:
        if d["group"] != cur:
            cur = d["group"]
            nav.append(f"<h4>{esc(cur)}</h4>")
        nav.append(f'<a href="#doc-{d["slug"]}" data-slug="{d["slug"]}">{esc(clean_title(d["title"])[:90])}</a>')
        arts.append(f'<article class="libdoc" data-slug="{d["slug"]}" data-title="{esc(clean_title(d["title"]))}" id="doc-{d["slug"]}" hidden>'
                    f'<div class="path">{esc(d["path"])} · {d["bytes"]:,} characters</div><div class="md">{d["html"]}</div></article>')
    library = ('<section class="tab" id="library" hidden><h2 class="sec">Library</h2>'
               '<p class="lede">Every memo, extract and research file in the workspace, rendered in full. Drive IDs in the text are links. '
               'Legal research is UNVERIFIED unless marked; nothing is filing-ready without KeyCite.</p>'
               '<div class="filters"><input type="search" id="libq" placeholder="Search all memos (3+ letters)" aria-label="Search the library"></div>'
               '<div class="results" id="libresults" hidden></div>'
               f'<div class="lib"><nav class="libnav" aria-label="Library documents">{"".join(nav)}</nav>'
               f'<div class="doc-body">{"".join(arts)}</div></div></section>')

    tabs = [("overview", "Overview", ""), ("issues", "Issues", len(ISSUES)), ("discovery", "Discovery", len(tracker)),
            ("open-items", "Open items", len(open_oi)), ("red-team", "Red team", len(a_items)),
            ("timeline", "Timeline", len(chron)), ("documents", "Documents", len(sources)), ("library", "Library", len(docs))]
    nav_html = "".join(f'<a href="#{t}">{esc(l)}{f"<span class=ct>{c}</span>" if c != "" else ""}</a>' for t, l, c in tabs)

    page = (page_head("Leal Case Dashboard",
                      "Attorney work product: status, issues, discovery, open items, red team, timeline, documents and memos for Leal v. Garabedian.")
            + '<div class="privband">Attorney work product · Privileged and confidential · Prepared for counsel · Not for production</div>'
            + '<header class="top"><div class="topin"><h1 class="brand">Leal v. Garabedian<small>Case dashboard for counsel · Tulare County No. VCU327028</small></h1>'
            + '<div class="tools"><button class="btn" id="theme" type="button">Theme</button></div></div>'
            + f'<nav class="tabs" aria-label="Sections">{nav_html}</nav></header>'
            + f"<main>{overview}{issues}{discovery}{openitems}{redteam}{timeline}{documents}{library}</main>"
            + f'<footer>Generated {esc(built)} from workspace revision {esc(rev)} by 07-attorney-dashboard/build_dashboard.py. '
              'Rebuild after each update; do not edit this file by hand.</footer>'
            + '<dialog id="viewer"><div class="bar"><span class="ttl"></span><button class="btn close" type="button">Close</button></div>'
              '<div class="scroll"><img alt=""></div></dialog>'
            + json_script("chron-data", chron) + json_script("manifest-data", manifest)
            + (json_script("pdf-data", pdf["b64"]) if pdf else "")
            + f"<script>{JS}</script></body></html>")
    OUT_DASH.write_text(page, encoding="utf-8")

    # ---------------- document index (no analysis)
    src_plain = []
    for s in sources:
        if not s["drive"]:
            continue
        src_plain.append(f'<tr data-s="{esc((s["id"] + " " + s["title"]).lower())}"><td class="num">{esc(s["id"])}</td>'
                         f'<td>{drive_link(s["title"][:160], s["drive"][0])}</td><td class="mono">{esc(s["date"][:40])}</td></tr>')
    idx = (page_head("Leal Document Index", "Index of the case Drive folder for Leal v. Garabedian, without analysis.")
           + '<div class="privband">Confidential · Index only, no analysis · Production decisions are counsel\'s</div>'
           + '<header class="top"><div class="topin"><h1 class="brand">Leal v. Garabedian<small>Document index · Tulare County No. VCU327028</small></h1>'
           + '<div class="tools"><button class="btn" id="theme" type="button">Theme</button></div></div>'
           + '<nav class="tabs" aria-label="Sections"><a href="#drive">Drive folder</a><a href="#later">Added after 8/18/2026</a></nav></header><main>'
           + '<section class="tab" id="drive"><h2 class="sec">Case Drive folder</h2><p class="lede">Every item in “Leal Trust Administration Litigation” '
             'as manifested on 8/18/2026. Links open Google Drive and need access to the folder. Items flagged “client draft” are drafts; review for privilege '
             'before producing anything. Bates numbers are applied at production, not here.</p>'
             '<div class="filters"><input type="search" id="mfq" placeholder="Search file names and folders" aria-label="Search Drive files">'
             '<select id="mffolder" aria-label="Folder"></select><select id="mftype" aria-label="Type"><option value="">Files and folders</option>'
             '<option value="file">Files only</option><option value="folder">Folders only</option><option value="draft">Client drafts only</option></select>'
             '<span class="count" id="mfcount"></span></div><div class="tablewrap"><table class="data"><thead><tr><th>Name</th><th>Type</th>'
             '<th>Modified</th></tr></thead><tbody id="mf-body"></tbody></table></div><p><button class="btn" id="mfmore" hidden>Show more</button></p></section>'
           + '<section class="tab" id="later" hidden><h2 class="sec">Added or identified after 8/18/2026</h2><p class="lede">Drive documents in the source '
             'register, by register number. Titles only.</p><div class="filters"><input type="search" id="sq" placeholder="Filter" aria-label="Filter" '
             'data-filter-for="stable" data-count="scount"><span class="count" id="scount"></span></div><div class="tablewrap"><table class="data" id="stable">'
             '<thead><tr><th>No.</th><th>Document</th><th>Date</th></tr></thead><tbody>' + "".join(src_plain) + '</tbody></table></div></section>'
           + f'</main><footer>Generated {esc(built)} from workspace revision {esc(rev)}.</footer>'
           + json_script("manifest-data", manifest) + f"<script>{JS}</script></body></html>")
    OUT_INDEX.write_text(idx, encoding="utf-8")

    print(f"dashboard: {OUT_DASH.stat().st_size/1e6:.2f} MB; index: {OUT_INDEX.stat().st_size/1e6:.2f} MB")
    print(f"library docs {len(docs)}, headings {len(headings)}, OI {len(oi_items)} ({len(open_oi)} open), A {len(a_items)}, "
          f"chron {len(chron)}, manifest {len(manifest)}, sources {len(sources)}, images {len(images)}, pdf {'yes' if pdf else 'no'}")
    for w in warnings:
        print("WARN", w)
    return 0 if not warnings else 1


if __name__ == "__main__":
    sys.exit(build())
