# Access, licensing, and verification

Last catalog review: 2026-11-05.

## Result of this pass

| Group | Count | Meaning |
| --- | ---: | --- |
| Rows with a primary source | 23 | Machine-readable catalog |
| Tier A | 14 | Direct download under the stated license |
| Tier A with waveforms | 13 | MODA is the annotations-only exception |
| Tier B | 0 | No registration-only original dataset cleared the bar |
| Tier C | 9 | Request, ethics packet, credentialing, or restricted agreement |
| Unverified rows | 0 | Incomplete candidates were left out rather than given a soft "open" label |

Tier C is documented so that readers do not mistake a famous cohort for a
direct download. It is not part of the open tables in the README.

## What Tier A does and does not allow

PhysioNet open projects checked here use either the Open Data Commons
Attribution License v1.0 or CC BY 4.0, and the page says anyone can access the
files if they follow the license. `wget` and anonymous S3 sync are documented
for those projects.

That is a data-access fact. It is not:

- a waiver of institutional review for a new human-subjects study
- permission to ignore attribution
- permission to treat a derived mirror as the canonical copy
- evidence that test-set labels exist, when the challenge page does not say so

Special cases:

- **Dreem Open Datasets.** The Zenodo record states MIT. The paper is still
  the citation to use for the cohort.
- **BOAS.** `dataset_description.json` on the OpenNeuro mirror says CC0. The
  GitLab code is CC BY-NC 4.0. Those are different objects.
- **DREAMS.** The bundled license matches CC BY-NC-ND 3.0. Direct download,
  non-commercial terms, and a no-adaptations clause.
- **ISRUC-Sleep.** Download links are public. No standard license text was
  found. The site says "research purposes." Commercial use is not granted by
  any text reviewed here.
- **MODA.** Annotation files are public. The EEG they refer to is MASS, which
  is Tier C.

## Tier C gates, as written by the owners

| Dataset | Gate found on the official page |
| --- | --- |
| SHHS, MESA, MrOS | NSRR account, request, and data-access agreement. A public forum reply says IRB review is preferred for SHHS but not a firm requirement; an internal review option exists. A person still approves the request. |
| CFS | NSRR request, and the page limits use to non-commercial research. |
| STAGES | NSRR request even though the about text also says the data will be publicly available. Commercial and non-commercial use are both named as allowed after approval. |
| MASS biosignals | Project description plus proof of approval from the requester's own ethics board. The site says PSG files will not be offered as a direct download. |
| DREAMT | PhysioNet restricted-health-data license. Qualified requestors, no sharing of access. |
| NCH Sleep DataBank and CPS | PhysioNet credentialing, CITI training, and a signed data-use agreement. CPS also limits use to the original study aims. |

NSRR pages for SHHS and MESA carried a banner that the repository is under
review for possible changes tied to administration directives. Re-read the
live page before starting an application.

## Conflicts left unresolved

These are disagreements inside official sources, not catalog errors.

- **SHHS.** The page header says 5,804 adults. The about text says 6,441 people
  were enrolled in Visit 1, and 3,295 received a Visit 2 PSG.
- **MrOS.** The header says 2,911 men. The about text says 3,135 were recruited
  to the sleep study. The dataset introduction says 2,911 Visit 1 rows had a
  successful PSG, and 1,026 subjects had repeated sleep measures.
- **ISRUC-Sleep.** The homepage's three groups match the 2016 paper's structure:
  100 single sessions, 8 subjects with two sessions, and 10 healthy subjects.
  The download page currently calls cohort II healthy. Cohort counts match;
  the clinical label does not.
- **DOD-O.** The 2020 paper reports 55 patients. The official code README says
  the 2025 Zenodo archive has 56 HDF5 files and names one file with no
  consensus score.
- **Challenge 2018.** Version 1.0.0 documents 1,985 subjects. The same page
  shows a later DOI (`10.13026/1q9b-ge17`) that this pass did not re-read.
- **BOAS.** The mirror metadata cites OpenNeuro `v1.1.3`. A DataCite record for
  `v1.2.0` was seen in search and was not file-diffed.
- **MESA file count.** The about page says 2,237 participants enrolled in the
  sleep exam. This pass did not count EDF files. Third-party tools should not
  be cited as the official inventory.
- **MIT-BIH Polysomnographic Database.** The current narrative says 16 subjects.
  `RECORDS` lists 18 waveform files because some recordings are split.
- **Apnea-ECG.** Seventy records are listed, but the page itself says `c05` and
  `c06` come from one original recording.

## Sampling rates that were measured

| File | What was read on 2026-11-05 |
| --- | --- |
| `capslpdb/1.0.0/n1.edf` | EEG and EOG channels 512 Hz; the first EMG channel in that header was 256 Hz |
| `ucddb/1.0.0/ucddb002.rec` | EEG 128 Hz; EOG and EMG 64 Hz; ECG 128 Hz; airflow, effort, SpO2, and sound 8 Hz |

Other records in those databases were not scanned. Sleep-EDF, HMC, PSG-IPA,
and Challenge 2018 rates in the catalog are taken from the project text, which
states them directly.

## Not reviewed in this pass

Seen on an index, in a review article, or in search, and deliberately not
given a row:

- Wisconsin Sleep Cohort, Study of Osteoporotic Fractures, CHAT, and CCSHS are
  named in the NSRR literature. Their live access pages were not opened.
- PhysioNet index titles for the Sleep Bioradiolocation Database, MMASH, the
  multi-night Apple Watch heart-rate set, and the original unexpanded
  Sleep-EDF page. The expanded Sleep-EDF release is catalogued; the older
  release is a subset, not a second cohort.
- OpenNeuro ear-EEG set `ds005178` and the UCSD forehead-patch set `ds006695`.
- TRACE-PSG. The MICCAI 2026 paper describes a retrospective report corpus.
  No public waveform or report deposit was found. Absence from this catalog is
  the finding.
- Synthetic PSG-report sets on Kaggle. They are not clinical recordings.

## Link checking

`.github/workflows/check-links.yml` runs `lychee` on pull requests, on manual
dispatch, and every Monday. A failure is a report. The workflow cannot push,
and it does not remove a dataset. A human has to open the primary page before
changing a URL.

## Repository license versus dataset licenses

The catalog, docs, and scripts are CC BY 4.0. See `LICENSE`. That grant stops
at the boundary of this repository. If you download a dataset, the dataset
license is the one in its row.
