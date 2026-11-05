# Methodology

Verified on 2026-11-05. This pass used the public web, PhysioNet project pages,
file indexes, one EDF header range read, Zenodo records, OpenNeuro metadata,
NSRR dataset pages, and the MASS and ISRUC project sites. No credentialed
file tree was opened. No patient file was stored in this repository.

## Where the search started

The seed list was Sleep-EDF Expanded, CAP Sleep Database, HMC Sleep Staging,
PSG-IPA, MIT-BIH Polysomnographic Database, ISRUC-Sleep, MASS, the Sleep Heart
Health Study, and MESA Sleep. None of those names was treated as open until
the current access statement was read.

The search then covered:

- the PhysioNet database index and the sleep topic page
- NSRR dataset pages and the public data-request description
- Zenodo records linked from official code repositories
- OpenNeuro dataset `ds005555` and its `dataset_description.json`
- OSF and GitHub pages for MODA
- citation chasing from Guillot et al. 2020, Alvarez-Estevez et al., and the
  NSRR resource papers

PhysioNet entries that appeared in the index but were not given a full page
review are listed in [the verification report](access-and-licensing.md#not-reviewed-in-this-pass).
They are not catalog rows.

## What counted as a source

A fact is tied to one of these:

1. The owner's project page or versioned deposit.
2. A license or data-use page linked from that deposit.
3. A file that was actually read: `RECORDS`, an EDF header, or a
   `dataset_description.json`.
4. The dataset paper, used for design details when the deposit points to it.

A training repository is evidence that code is open. It is evidence about the
data only when it points at a deposit and the deposit was opened. Reuploads on
Kaggle and Hugging Face were not catalogued.

## Counts

Subjects, recordings, and epochs are different fields. When one official page
prints two sample sizes, both are kept. Filename-derived counts say so.
Header-derived sampling rates name the file and say that other records were
not scanned.

Epoch totals are usually absent from the project pages, so this catalog does
not invent them.

## Access tiers

| Tier | Rule used in this pass |
| --- | --- |
| A | The project page says anyone can access the files under the license, or the deposit exposes a direct download, and no approval step was found. |
| B | A free account or click-through would be sufficient, with no human approval. No resource met that description without also being a mirror or an unverified page. |
| C | The page requires a data-access request, an ethics packet, credentialing, or a restricted data-use agreement. |
| Unverified | Used when the gate cannot be judged. This pass left those candidates out of the machine-readable catalog and listed them in the verification notes. |

Open download is not a statement about the user's institutional ethics review.
Licenses still apply. ODC-By and CC BY require attribution. CC BY-NC-ND and
"research purposes" wording are narrower.

## Evidence grounding

Four questions are answered separately for every row:

1. Are raw, time-addressable signals present?
2. Are human events already timed, and do any of them name a channel?
3. Does any label connect a model or clinical claim to a source span?
4. Would a new annotation pass be required to build `e_k = (claim_k, source_k, pointer_k)`?

A positive answer to (1) is never recorded as a positive answer to (3).

## Versions

Sleep-EDF Expanded absorbs the older Sleep-EDF subset. HMC is catalogued only
as version 1.1. DOD-H and DOD-O are one deposit with two cohorts. DREAMS
subsets stay in one row. SHHS Visit 1 and Visit 2 stay in one NSRR entry.
Challenge 2018 was checked at version 1.0.0 even though the page advertises a
later DOI.

## Reproducibility

`scripts/validate_catalog.py` checks required fields, ids, tiers, URL shape,
and JSON/CSV equality. It does not fetch the web. The weekly link workflow
reports failures and has no permission to edit the catalog.
