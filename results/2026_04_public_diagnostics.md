# April 2026 Public-Safe Diagnostics

This note summarizes a newer private diagnostic branch without disclosing source code, recipes, checkpoints, exact data mixtures, or reproduction-critical architecture details.

Raw public-safe values are stored in [`data/2026_04_public_diagnostics.json`](../data/2026_04_public_diagnostics.json).

---

## Diagnostic branch

| Field | Public-safe value |
|---|---:|
| parameter count | **66.5M** |
| training budget | **20K-step diagnostic run** |
| disclosure level | public-safe summary |
| architecture details | withheld |

The branch is included because it reflects the newer direction of the private research program more accurately than older public summaries. It should not be read as a reproducible release.

---

## Internal structural diagnostics

| Metric | Result |
|---|---:|
| text BPB | **1.831** |
| content token accuracy | **0.694** |
| structure token accuracy | **0.995** |
| sequence accuracy | **0.163** |
| row accuracy | **0.376** |
| cross-format content accuracy | **0.590** |
| cross-format sequence accuracy | **0.333** |
| holdout content accuracy | **0.571** |
| holdout sequence accuracy | **0.067** |

Interpretation:

- The strongest signal is structural transfer, especially cross-format content accuracy.
- Structure prediction is much easier than exact content generation.
- Sequence-level exactness is still far from solved.
- Text compression is usable for diagnostics, but it does not by itself imply assistant-grade language ability.

---

## External language-model evaluation

| Benchmark | Metric | Result |
|---|---:|---:|
| HellaSwag | acc_norm | **0.292** |
| PIQA | acc_norm | **0.529** |
| ARC-Easy | acc_norm | **0.271** |
| ARC-Challenge | acc_norm | **0.227** |
| Winogrande | acc | **0.507** |
| LAMBADA | acc | **0.040** |

Interpretation:

- The branch is not random on every external task.
- HellaSwag is the cleanest positive external signal in this snapshot.
- PIQA and Winogrande are close enough to chance that they should be treated cautiously.
- LAMBADA remains weak, consistent with long-context limitations in the current public-safe diagnostic setup.

---

## What this suggests

The useful reading is not "LUMI is already a strong assistant." It is:

> A compact private branch shows meaningful structural-transfer behavior and non-random external signals, while still exposing clear gaps in broad language competence.

That is exactly the kind of result that justifies controlled scale-up and broader evaluation.

---

## What remains unresolved

| Question | Status |
|---|---|
| Does the structural-transfer signal scale to 100M+ and 1B+? | unresolved |
| Can broader text/code/math data improve external tasks without destroying transfer? | unresolved |
| Can instruction tuning improve conversation while preserving base capability? | unresolved |
| Are long-context failures mostly architectural, data-related, or compute-limited? | unresolved |

These questions require controlled compute. They cannot be answered from this public-safe snapshot alone.
