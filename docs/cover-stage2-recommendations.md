# COVER Stage 2: what the open data can actually support

Verified 2026-11-05. COVER Stage 2, as framed for this catalog, needs five
things that are easy to conflate:

1. Raw EEG or PSG that can be addressed by channel and time.
2. A way to find 30-second epochs that are hard, not only epochs that are
   numerous.
3. More than one expert on the same epoch or event, when the question is
   disagreement rather than a proxy for it.
4. A path from a judgment back to a signal span.
5. A clinical text that is actually paired with those signals.

The pointer the work is aiming at is:

```text
e_k = (claim_k, source_k, pointer_k)
```

No dataset in the open tier ships that triple as a supervised label. Several
ship the ingredients of `source_k` and a usable `pointer_k` for physiological
events. The claim, and the link from claim to pointer, still has to be built.

## Recommendation order

| Order | Dataset | Use it for | Do not pretend it already has |
| --- | --- | --- | --- |
| 1 | PSG-IPA | Twelve-scorer disagreement and onset/offset uncertainty | A training corpus. Only five recordings are independently staged |
| 2 | Dreem DOD-H / DOD-O | Five-scorer staging in healthy sleep and OSA, if the per-scorer arrays are in the HDF5 | A confirmed per-scorer layout. The README documents one consensus hypnogram. Open a file before locking the design |
| 3 | ISRUC-Sleep | Two-expert labels on 126 nights, plus eight people recorded twice | A standard open license, or a settled diagnosis for cohort II |
| 4 | Challenge 2018 training (994) | Timed arousals and respiratory events on raw clinical PSG | A second scorer, or confirmed test-set labels |
| 5 | CAP Sleep Database | Phase A intervals that name a channel | Multi-rater stage labels or diagnostic-report pointers |
| 6 | BOAS | Simultaneous clinical PSG and wearable EEG, consensus versus AI | Proof, until the events are opened, that three raw scorer tracks are public |
| 7 | UCD Sleep Apnea Database | Respiratory-event times aligned to stages, including artifact and indeterminate | Scale. There are 25 nights and one scorer |
| 8 | DREAMS spindle and K-complex excerpts | Two-expert microstructure on short EEG excerpts | Whole-night context, and unrestricted commercial training. The license is CC BY-NC-ND 3.0, and expert 1 spindles stop at 1000 s |
| 9 | HMC v1.1 and Sleep-EDF Expanded | External staging distributions at 256 Hz and 100 Hz | Disagreement labels or event pointers |

MODA's spindle gold standard is real and public, and the matching EEG is not.
It becomes useful after MASS access, which requires the requester's own ethics
approval. It is not step one of an open-data experiment.

## Designs that can start now

### 1. Disagreement, at the right sample size

Treat PSG-IPA as the measurement study, not the training set.

- On the five staging recordings, compute epoch-wise agreement across the 12
  manual scorers. Define difficulty as one minus the majority fraction.
  Keep the computer-assisted pass separate, because it is not an independent
  reading.
- On the arousal, limb, and respiratory recordings, score boundary
  disagreement: how far onset and offset move across scorers. The prefilled
  hypnogram is context, not a second staging opinion.
- Train any stager on HMC v1.1, Sleep-EDF Expanded, or the Challenge 2018
  training set. Test only whether high predictive entropy lands on the
  low-agreement PSG-IPA epochs. With five staged nights, this is a pilot
  calibration, not a performance claim.

Then scale the same definition to ISRUC-Sleep, where two experts labeled 126
recordings, and to DOD if the individual vectors are present. Report N1 and
stage transitions separately from stable N2 and N3. The eight ISRUC subjects
with two nights separate within-person change from between-expert change.

### 2. Difficult epochs when only one label exists

Challenge 2018 does not provide a second technologist. It does provide
sample-level arousals and respiratory events. A pre-registered proxy, which
must be called a proxy, is:

- epochs that contain a target arousal
- epochs labeled undefined, or that sit on a stage transition
- epochs with no such event, matched on stage, as controls

Sleep-EDF's unscored (`?`) and movement epochs, and UCD's artifact and
indeterminate epochs, are additional negative-quality labels. They are not
inter-rater disagreement.

### 3. Building pointers without inventing a claim label

Construct pointers only from annotations a human already timed.

| Source annotation | Pointer you can form | What it supervises |
| --- | --- | --- |
| CAP phase A: onset, duration, location string | `(channel, t0, t1)` for that phase | CAP detection, not "why this epoch is N2" |
| Challenge 2018 arousal and respiratory regions | sample span, then the channels AASM scoring would consult | Event detection and epoch difficulty proxies |
| PSG-IPA event edits | distribution of human onsets and offsets | Boundary uncertainty |
| UCD respiratory-event file | event time and type, joined to the stage file | Which stages contain scored respiratory events |
| DREAMS spindle and K-complex excerpts | two-expert intervals on a short central EEG | Microstructure agreement, inside the license |

None of these rows is a `(claim, source, pointer)` example. A later annotation
layer can add the claim: for a disagreed epoch, a reviewer states the stage
call and selects one of these spans, or rejects all of them. Until that layer
exists, a model that highlights a spindle has produced a candidate pointer,
not a verified one.

### 4. Cross-dataset generalization

A honest open staging suite is:

- Sleep-EDF Expanded: mostly healthy or mild sleep-onset difficulty, R&K, 100 Hz, two EEG derivations
- HMC v1.1: mixed referrals, AASM v2.4, 256 Hz, four EEG derivations
- CAP: disorder-enriched, R&K, higher-rate EEG, many channels
- Challenge 2018 training: large clinical AASM PSG at 200 Hz
- UCD: suspected sleep-disordered breathing, one scorer, 25 nights

Pool them only after resampling and after mapping R&K stages 3 and 4 onto N3
explicitly. Leave PSG-IPA out of training so the twelve-scorer nights stay
untouched as a disagreement probe. Leave DOD-O's extra unscored file out of
any paper replication.

### 5. Wearable signals versus EEG evidence

BOAS records clinical PSG and a forehead EEG headband on the same night. It is
the open place to ask whether uncertainty on the headband tracks uncertainty
on the PSG. Sleep-Accel is the complementary negative control: watch motion
and heart rate with PSG labels, and no PSG waveform. A pointer cannot land on
an EEG channel that was never released.

DREAMT is the restricted version of the wearable-plus-PSG question. It is not
needed to start.

## The gap that open data does not close

Clinical text aligned to signals is missing from Tier A and Tier B.

- TRACE-PSG's reports were not found as a public deposit.
- NCH Sleep DataBank links pediatric PSGs to structured EHR tables, under
  PhysioNet credentialing. That is not an open narrative report, and it is not
  an adult cohort.
- STAGES has questionnaires and clinical PSGs behind an NSRR request. The
  public page does not describe free-text interpretations tied to time spans.
- CPS has questionnaires and 81 event types, also credentialed, and use is
  limited to the original study aims.

A text-signal experiment on open data would be synthetic or would use coded
variables. Neither is pointer-grounded evidence in the TRACE-PSG sense. The
honest Stage 2 path is signal and event pointers first, and a new text
annotation protocol only if a data owner releases reports under terms that
allow it.

## Suggested first 90 days

1. Download PSG-IPA, HMC v1.1, and the Challenge 2018 training records.
2. Inspect one DOD HDF5 and one BOAS events file. Record whether individual
   scorers are columns or only a consensus. Update this catalog either way.
3. Freeze an epoch-agreement definition on PSG-IPA manual staging before
   looking at model entropy.
4. Build CAP location strings into channel-time pointers and count how often
   the named channel is actually present.
5. Write the license check for DREAMS and ISRUC before any training run that
   might be commercial or redistributed.

Do not start with SHHS, MESA, or MASS unless the access packet is already
approved. They answer different questions, at a different governance cost.
