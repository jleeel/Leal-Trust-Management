# 07 — Attorney dashboard

**ATTORNEY WORK-PRODUCT SUPPORT — PRIVILEGED & CONFIDENTIAL.** Built for Brandon M. Ormonde (lead)
and Erika Rason (co-counsel), Ormonde Rascon. Counsel team per client, 10/3/2026.

## What is here

| File | What it is | Share with |
|---|---|---|
| `leal-case-dashboard.html` | The one-stop page. Tabs: overview (caption, key dates, posture, this week's tasks, people), issues (10 cards with sources and Drive links), discovery tracker (Demand for Production, Set One), open items, red team, timeline, documents (verified sources, the full Drive manifest, evidence images and the RFP PDF) and the full library of workspace memos. | Counsel only. It contains work product and AI-assisted analysis. |
| `leal-document-index.html` | The Drive folder index with no analysis: file names, folders, dates and Drive links. Client drafts are flagged for privilege review. | Counsel and staff preparing a production. |
| `rfp-tracker.csv` | Status of each of the 18 demands: To collect / Partly collected / Collected / Produced / Objection, plus produced Bates range. | Edit, then rebuild. |
| `build_dashboard.py` | Generates both pages from the workspace. | — |

## Opening the pages

Both pages are single, self-contained HTML files. They make no outside connections: no fonts,
scripts or trackers load from the internet.
- **From Drive:** Google Drive's preview shows HTML as code. Download the file, then open it in
  Chrome, Edge, Safari or Firefox.
- **Drive links inside the page** open only for someone the case folder ("Leal Trust
  Administration Litigation", owner jaceleal@gmail.com) is shared with. Share the folder with
  counsel only.
- **Gmail thread IDs** refer to the client's mailbox. Ask Jace for the message.

## Rebuilding (after every integration)

```
python3 cmc-prep/07-attorney-dashboard/build_dashboard.py
```

The script needs `markdown-it-py` and, for the reduced evidence images, `Pillow`
(`pip install markdown-it-py pillow`).

It reads:
- `05-for-brandon/open_items.md` and `04-adverse-analysis/adverse_analysis.md` (item numbers,
  titles, flags, updates);
- `03-chronology/chronology.csv` and `01-verified-facts/source-register.md`;
- `01-verified-facts/drive-sweep/master-manifest.csv`;
- `rfp-tracker.csv`;
- every memo listed in its `LIBRARY_GROUPS`.

**Curated content** (key dates, people, issue cards, this week's tasks) is in the CONFIG block at
the top of the script. Every line there carries its source. Update it when the posture changes.

The script exits non-zero and prints `WARN` if an issue card cites an A- or OI-number or a file
that does not exist.

## Cautions

- **Work product.** Do not attach the dashboard to anything sent to another party. Use the
  document index, and counsel's numbered production, for anything produced.
- **"Marked answered"** on an open item means one of its headings carries a check mark or says
  answered or resolved. Part of the item may still be open, so read the latest update.
- **The Drive manifest is from 8/18/2026.** Files added since appear under "Verified sources" if
  the workspace has read them.
