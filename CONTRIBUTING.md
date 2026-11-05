# Contributing

Add or correct a dataset only when a primary source supports the change.
Primary sources are the data owner's project page, the versioned deposit, the
license or data-use agreement, and the dataset paper. A methods paper that
used a private cohort, a GitHub training script, or a reupload is not enough.

## What to include

For a new row, update both `datasets/datasets.json` and `datasets/datasets.csv`,
then run:

```bash
python scripts/export_csv.py
python scripts/validate_catalog.py
```

`export_csv.py` rewrites the CSV from the JSON. Edit the JSON first.

Required facts:

- Official name and the version you actually opened.
- Official URL and the download or request URL.
- Subjects and recordings as separate numbers. Use `Unknown` rather than a
  blog's round number.
- Modalities, sampling rate, and annotations, each tied to a page or a file
  header you inspected.
- Access tier: `A`, `B`, `C`, or `Unverified`.
- License or the statement that no license was found.
- `last_verified` as `YYYY-MM-DD`.
- At least one verification URL.

## Access tiers

| Tier | Meaning |
| --- | --- |
| A | The files can be downloaded without an account, an approval email, or a data-use agreement. A license can still apply. |
| B | A free account or a standard click-through is enough, and no person approves the request. |
| C | A human review, institutional approval, ethics-board packet, data-use agreement, or credentialing course stands between the visitor and the files. |
| Unverified | The access path was not confirmed. Do not call it open. |

Tier C rows stay in the catalog and out of the open comparison tables.

## Do not

- Upload PSG, EEG, clinical text, or any derived patient-level file.
- Add a Kaggle, Hugging Face, or GitHub mirror as the official source.
- Copy another catalog's prose. Summarize the primary source in new words.
- Delete a row because the link checker failed. Fix the URL after checking it,
  or mark the entry unverified and explain why.

## Pull requests

Explain what you opened, the date, and which field changed. If two official
pages disagree, quote both and leave the disagreement in `notes`.
