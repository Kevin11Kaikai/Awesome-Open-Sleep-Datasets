# Awesome Open Sleep Datasets

[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-blue.svg)](LICENSE)
[![Catalog verified](https://img.shields.io/badge/catalog%20verified-2026--11--05-2ea44f.svg)](docs/methodology.md)
[![Tier A / B / C](https://img.shields.io/badge/access-A%20%7C%20B%20%7C%20C-lightgrey.svg)](docs/access-and-licensing.md)

[中文](README_zh-CN.md)

A curated catalog of sleep datasets whose access path, license, and cohort
size were checked against a primary source. The aim is a map for sleep
staging, polysomnography, respiratory events, wearable validation, inter-rater
disagreement, and signal-level evidence work.

It is not a dump of every paper that mentions EEG. Code repositories and
reuploads are not treated as data releases. Controlled cohorts stay in their
own section.

Reviewed on **2026-11-05**: **23** datasets with a primary source,
**14** Tier A (13 with waveforms, 1 annotations-only), **0** Tier B, and
**9** Tier C. Details and unresolved conflicts are in
[Access and licensing](docs/access-and-licensing.md).

## Why this list exists

Open EEG staging benchmarks are easy to name and easy to over-read. A file of
raw EEG does not contain expert disagreement, a timed micro-event, or a
clinical report that points back at a channel. Those are separate annotations.

This catalog started from a concrete need: find data that can support a second
stage of explainable sleep analysis, where a judgment can be traced to a
channel and a time span. The working form of that trace is
`e_k = (claim_k, source_k, pointer_k)`. TRACE-PSG develops that idea on
PSG reports. Its report corpus was not found as a public waveform release.
The open datasets below are therefore graded by which piece of the trace they
actually contain.

## Inclusion rules

A dataset is listed when a project page, deposit, or license page could be
opened and the access rule was explicit.

- **Tier A.** Direct download. No account and no approval. A license still applies.
- **Tier B.** Free registration or a standard click-through, with no human approval. None cleared this pass.
- **Tier C.** A request, ethics packet, credentialing course, or restricted data-use agreement. Listed separately.
- **Unverified.** Not given a catalog row. Named in the [verification notes](docs/access-and-licensing.md#not-reviewed-in-this-pass).

Direct download does not exempt a new study from institutional review, and it
does not transfer the dataset owner's license to this repository. Numbers that
disagree across official sections are reported as disagreements.

Machine-readable copies: [`datasets/datasets.csv`](datasets/datasets.csv) and
[`datasets/datasets.json`](datasets/datasets.json).

## Contents

- [Sleep staging and PSG](#sleep-staging-and-psg)
- [Inter-rater and microstructure](#inter-rater-and-microstructure)
- [Apnea and other events](#apnea-and-other-events)
- [Wearables](#wearables)
- [Annotations without waveforms](#annotations-without-waveforms)
- [How the open sets compare](#how-the-open-sets-compare)
- [COVER Stage 2](#cover-stage-2)
- [Controlled access](#controlled-access)
- [License and ethics](#license-and-ethics)
- [Contributing](#contributing)
- [References](#references)

## Sleep staging and PSG

Tier A resources with raw signals and stage labels. "Recordings" are nights or
files, not epochs.

| Dataset | Subjects / recordings | Signals and rate | Stages | License |
| --- | --- | --- | --- | --- |
| [Sleep-EDF Expanded](https://physionet.org/content/sleep-edfx/1.0.0/) | 100 subjects, 197 PSGs | EEG, EOG, chin EMG at 100 Hz; cassette EMG envelope and airflow at 1 Hz | R&K, one hypnogram | ODC-By 1.0 |
| [CAP Sleep Database](https://physionet.org/content/capslpdb/1.0.0/) | 108 recordings (16 controls, 92 pathological recordings) | Multi-channel EEG, EOG, EMG, respiration, SpO2, ECG. `n1.edf` EEG/EOG is 512 Hz | R&K plus CAP A phases | ODC-By 1.0 |
| [HMC v1.1](https://physionet.org/content/hmc-sleep-staging/1.1/) | 151 recordings (85 male, 66 female) | 4 EEG, 2 EOG, chin EMG, ECG at 256 Hz | AASM v2.4, one scorer | CC BY 4.0 |
| [Challenge 2018](https://physionet.org/content/challenge-2018/1.0.0/) | 1,985 subjects; 994 training / 989 test | Six EEG, EOG, EMG, ECG, respiration, SaO2 at 200 Hz | AASM 30 s stages on the training description | ODC-By 1.0 |
| [ISRUC-Sleep](https://sleeptight.isr.uc.pt/) | 118 subjects, 126 recordings | Full-night PSG. Rate not restated on the pages reviewed | Two experts | Research-purpose statement; no standard license found |
| [Dreem DOD-H / DOD-O](https://zenodo.org/records/15900394) | Paper: 25 healthy and 55 OSA. Archive note: 56 DOD-O files | PSG in HDF5, including EEG and EOG | Five technologists; consensus documented in the files | MIT on the Zenodo record |
| [BOAS](https://openneuro.org/datasets/ds005555) | 100 adults, 128 nights | Simultaneous clinical PSG and forehead EEG. Code assumes 256 Hz | Three experts, consensus, and AI labels | Data CC0; code CC BY-NC 4.0 |
| [DREAMS](https://zenodo.org/records/2650142) | 20 healthy and 27 patient whole nights, plus smaller subsets | PSG or channel excerpts | R&K and AASM on the whole-night subsets | CC BY-NC-ND 3.0 |

The 2002 Sleep-EDF release is an earlier subset of Sleep-EDF Expanded, not a
second cohort. HMC version 1.0 is superseded; 1.1 dropped three corrupt
recordings.

## Inter-rater and microstructure

| Dataset | What is independently labeled | Scale | Waveform in the download |
| --- | --- | --- | --- |
| [PSG-IPA](https://physionet.org/content/psg-ipa/1.0.0/) | 12 technologists, manual and computer-assisted. Staging on 5 recordings; arousals, leg movements, and respiratory events on 5 each | 20 PSGs | Yes |
| [Dreem Open Datasets](https://zenodo.org/records/15900394) | Five technologists in the paper. Confirm the per-scorer arrays inside the HDF5 | 25 + 55, with one extra DOD-O file called out by the code README | Yes |
| [ISRUC-Sleep](https://sleeptight.isr.uc.pt/?page_id=48) | Two experts on the recordings | 126 recordings, including 8 people with two nights | Yes |
| [BOAS](https://openneuro.org/datasets/ds005555) | Three experts are described. The public events were not opened, so consensus-only remains possible | 128 nights | Yes |
| [DREAMS spindles / K-complexes](https://zenodo.org/records/2650142) | Two experts on 30-minute excerpts. Expert 1 spindles were cut off after 1000 s | 8 spindle excerpts, 5 K-complex excerpts | Yes, excerpts only |
| [CAP](https://physionet.org/content/capslpdb/1.0.0/) | One scoring team. Phase A rows include duration and a channel location | 108 recordings | Yes |
| [MODA](https://osf.io/8bma7/wiki/home/) | Crowd and expert spindle marks | 180 MASS recordings | No. MASS EEG is Tier C |

PSG-IPA event tasks include a prefilled hypnogram that scorers were not
allowed to change. That hypnogram is not a second staging opinion.

## Apnea and other events

| Dataset | Event timing | Also staged? | Limit |
| --- | --- | --- | --- |
| [Challenge 2018 training](https://physionet.org/content/challenge-2018/1.0.0/) | Sample-level arousals and respiratory classes | Yes, 30 s | Test-partition labels were not confirmed in version 1.0.0 |
| [UCD / St Vincent's](https://physionet.org/content/ucddb/1.0.0/) | Apnea, hypopnea, and periodic breathing with time of occurrence | Yes, plus artifact and indeterminate | 25 nights, one technologist |
| [MIT-BIH Polysomnographic](https://physionet.org/content/slpdb/1.0.0/) | QRS reviewed; apnea and CPAP timing described | R&K | 16 subjects in the current text, 18 files, 2-7 h |
| [Apnea-ECG](https://physionet.org/content/apnea-ecg/1.0.0/) | Minute apnea labels on 35 learning records | No | ECG, not PSG. Eight records add respiration and SpO2. `c05` and `c06` are one source recording |
| [CAP](https://physionet.org/content/capslpdb/1.0.0/) | CAP A phase onset, duration, location | Yes | Not a respiratory-event database; only 4 SDB recordings are in the named groups |

## Wearables

| Dataset | What was released | PSG waveform | Access |
| --- | --- | --- | --- |
| [BOAS](https://openneuro.org/datasets/ds005555) | Headband EEG recorded at the same time as clinical PSG | Yes | A, CC0 |
| [Sleep-Accel](https://physionet.org/content/sleep-accel/1.0.0/) | Apple Watch acceleration, heart rate, steps, and PSG stage labels for 31 subjects | No | A, ODC-By 1.0 |
| [DREAMT v2.2.0](https://physionet.org/content/dreamt/2.2.0/) | Smartwatch signals aligned with PSG and technician stages, 100 participants | Yes | C, restricted agreement |

Sleep-Accel cannot support a pointer into EEG. The people excluded before
release included sleep apnea and REM sleep behavior disorder.

## Annotations without waveforms

[MODA](https://osf.io/8bma7/wiki/home/) (Lacourse et al., Scientific Data 2020)
distributes spindle annotations for 180 MASS recordings. The
[MODA_GC instructions](https://github.com/klacourse/MODA_GC) send readers to
MASS for the PSG, and MASS requires an ethics-approved project. MASS subset
SS2 also has public spindle and K-complex files on Borealis; the EEG for those
files is still restricted.

## How the open sets compare

| Question | Best current open answer | Missing piece |
| --- | --- | --- |
| Train a modern AASM stager on clinical PSG | Challenge 2018 training (994) and HMC v1.1 (151) | A shared second scorer |
| Compare with the classic low-rate benchmark | Sleep-EDF Expanded | Disorder diversity and AASM labels |
| Measure expert disagreement | PSG-IPA, then ISRUC and DOD after a file check | PSG-IPA has only five staged nights |
| Point at a channel and a time | CAP location field; Challenge 2018 and PSG-IPA event spans | A label that ties a claim to that span |
| Compare wearable EEG with PSG | BOAS | Confirmation that all three human tracks are in the events |
| Pair a report with the waveform | None in Tier A or B | TRACE-PSG was not found as open data |

Full field-level notes, including sampling-rate caveats, are in the CSV.

## COVER Stage 2

The short version: start with PSG-IPA for disagreement, Challenge 2018 and CAP
for timed evidence, HMC and Sleep-EDF for external staging, and BOAS for
wearable EEG. Read the designs, the negative findings, and the 90-day sequence
in [COVER Stage 2 recommendations](docs/cover-stage2-recommendations.md).

No open dataset in this catalog contains supervised pointer-grounded evidence.
Event times are raw material for a pointer. They are not the pointer-claim link.

## Controlled access

These are real PSG resources. They are not open downloads. Do not cite them as
Tier A or B.

| Dataset | Who is described | Gate |
| --- | --- | --- |
| [SHHS](https://sleepdata.org/datasets/shhs) | Header 5,804 adults; about text 6,441 enrolled and 3,295 Visit 2 PSGs | NSRR request and agreement |
| [MESA Sleep](https://sleepdata.org/datasets/mesa) | 2,237 enrolled in the sleep exam; parent study 6,814 | NSRR request. Other MESA exams are separate |
| [MrOS Sleep](https://sleepdata.org/datasets/mros) | 2,911 with a successful Visit 1 PSG; 3,135 recruited; 1,026 with repeat sleep measures | NSRR request. Actigraphy raw data are not in this copy |
| [Cleveland Family Study](https://sleepdata.org/datasets/cfs) | 2,284 people in 361 families. Visit 5 PSG posted first | NSRR request, non-commercial only |
| [STAGES](https://www.sleepdata.org/datasets/stages) | 1,500 adult and adolescent patients. Mayo PSGs removed in 2023 | NSRR request |
| [MASS](https://ceams-carsm.ca/mass/) | Laboratory PSG. SS1 and SS2 public descriptions list 53 and 19 subjects | Ethics approval for biosignals |
| [DREAMT](https://physionet.org/content/dreamt/2.2.0/) | 100 participants | PhysioNet restricted license |
| [NCH Sleep DataBank](https://physionet.org/content/nch-sleep/3.1.0/) | 3,984 pediatric studies, 3,673 patients, plus EHR tables | PhysioNet credentialing and CITI training |
| [CPS](https://physionet.org/content/cps-dataset-sleep/1.0.0/) | 113 diagnostic PSGs, 81 event types | Credentialing, and use aligned with the original trial |

SHHS and MESA pages displayed a banner that the repository is under review for
administrative changes. Pediatric studies (NCH, and adolescents within STAGES)
need extra governance even after a data agreement.

## License and ethics

This repository is [CC BY 4.0](LICENSE). The license covers the catalog,
documentation, and scripts. It does not cover any dataset you download.

Each row names the dataset license that was visible on 2026-11-05. ODC-By and
CC BY require attribution. DREAMS is non-commercial and no-derivatives.
ISRUC states research use and does not publish a standard license. NSRR and
PhysioNet credentialed agreements add their own conditions, including, for
CFS and for CPS, limits that are stricter than "any research."

Being allowed to download a de-identified file is not a determination that
your protocol is exempt from ethics review.

## Contributing

Corrections need a primary URL and the date it was opened. The link checker
reports broken links; it does not delete rows. Read
[CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

```bash
python scripts/export_csv.py
python scripts/validate_catalog.py
```

## References

The comparison method and the tier rules are in
[methodology](docs/methodology.md). Access conflicts are in
[access and licensing](docs/access-and-licensing.md).

Dataset papers and deposits cited from the rows include Kemp et al., IEEE TBME
2000; Mourtazaev et al., Sleep 1995; Terzano et al., Sleep Medicine 2001;
Alvarez-Estevez and Rijsman, PLoS ONE 2021 and 2022; Ichimaru and Moody,
Psychiatry and Clinical Neurosciences 1999; Penzel et al., Computers in
Cardiology 2000; Ghassemi et al., Computing in Cardiology 2018; Walch et al.,
Sleep 2019; Guillot et al., IEEE TNSRE 2020; O'Reilly et al., Journal of Sleep
Research 2014; Lacourse et al., Scientific Data 2020; Quan et al., Sleep 1997;
Zhang et al., JAMIA 2018; Khalighi et al., Computer Methods and Programs in
Biomedicine 2016.

PhysioNet, NSRR, Zenodo, OpenNeuro, Borealis, OSF, and the ISRUC project site
are the data sources. This list does not redistribute their recordings.
