# LUMI-Arch Research Notes

![Status](https://img.shields.io/badge/Status-Active%20Research-brightgreen)
![Stage](https://img.shields.io/badge/Stage-Public%20Safe%20Diagnostics-blue)
![License](https://img.shields.io/badge/License-Research%20Only-orange)

**Independent AI architecture research focused on compact language models, compression pressure, and structural transfer.**

This repository is a public research record. It is designed to make the evidence legible without exposing implementation details, training recipes, checkpoints, or reproduction-critical architecture internals.

---

## Short version

LUMI-Arch asks whether a compact model can learn more useful structure per unit of compute by adding stronger compression pressure and structure-aware training signals, rather than relying only on brute-force scale.

The current public record supports three claims:

| Claim | Public status | What it means |
|---|---:|---|
| The direction is not just a symbolic toy | Supported | Earlier structured-task wins motivated scale-up. |
| The architecture family can beat a matched Transformer on a controlled 300M compression test | Supported | 300M LUMI-family run reached **1.2341 BPB** vs **1.4220 BPB** for the matched Transformer baseline. |
| Larger training is feasible, but the program is still diagnostic | Supported | A 996M pilot reached stable early convergence, but it was not a full benchmark run. |

The current public record does **not** claim state-of-the-art assistant ability, open reproduction, or a solved general-reasoning system.

---

## Current public evidence

### Compression and scale diagnostics

| Experiment | Public-safe result | Interpretation |
|---|---:|---|
| 300M matched comparison | LUMI-family: **1.2341 BPB** / Transformer: **1.4220 BPB** | A controlled compression win at matched scale. |
| 300M seed consistency | **4 / 4** seeds favored LUMI-family | The result was not a single lucky run. |
| 1B pilot | **996M** parameters, early C4 BPB **2.1616** at 2K steps | Training at near-1B scale is operationally feasible, but not yet a final-quality claim. |
| 66.5M private diagnostic branch | internal structural transfer **0.590**, text BPB **1.831** | Newer private diagnostics show stronger transfer behavior, but implementation details are intentionally withheld. |

### Public-safe external evaluation snapshot

The 66.5M private diagnostic branch was also checked with standard language-model evaluation tasks. These are useful as a reality check: LUMI is showing non-random behavior on several tasks, but it is not yet a broadly strong assistant model.

| Benchmark | Metric used | Result |
|---|---:|---:|
| HellaSwag | acc_norm | **0.292** |
| PIQA | acc_norm | **0.529** |
| ARC-Easy | acc_norm | **0.271** |
| ARC-Challenge | acc_norm | **0.227** |
| Winogrande | acc | **0.507** |
| LAMBADA | acc | **0.040** |

These numbers are included to avoid cherry-picking internal metrics. They show the current gap clearly: structural transfer is improving faster than broad natural-language competence.

---

## Why this is interesting

Most compact-model projects improve by changing data, scale, or training duration. LUMI-Arch is testing a different bet:

> Can compression pressure and structural transfer act as a training pressure that improves the model's internal representations across domains?

The strongest current hypothesis is that the concept/compression mechanism is useful less as a direct inference-time module and more as a training constraint: it forces the model to organize representations in ways that transfer better.

That hypothesis is still being tested. The public evidence says the direction is worth testing further; it does not say the problem is solved.

---

## Disclosure boundary

To reduce imitation risk, this repository intentionally shares:

| Shared publicly | Not shared publicly |
|---|---|
| benchmark summaries | source code |
| public-safe data tables | checkpoints or weights |
| failure-mode interpretation | exact architecture internals |
| compute needs and experiment goals | training recipes and hyperparameter sweeps |
| high-level research direction | private data mixtures or curriculum details |

If you are evaluating the project for compute support or collaboration, the intended signal is the research trajectory and evidence quality, not a recipe for reproducing the system.

---

## Public materials

| Path | Description |
|---|---|
| [public_results_snapshot.md](./public_results_snapshot.md) | One-page public summary for compute / partner outreach |
| [support_brief.md](./support_brief.md) | Short compute-support brief |
| [COMPUTE_REQUEST.md](./COMPUTE_REQUEST.md) | Email-ready compute support framing |
| [METHODOLOGY.md](./METHODOLOGY.md) | Public-safe methodology and disclosure boundary |
| [results/300m_scale_comparison.md](./results/300m_scale_comparison.md) | 300M parameter-matched comparison |
| [results/1b_pilot_convergence.md](./results/1b_pilot_convergence.md) | 1B pilot convergence note |
| [results/2026_04_public_diagnostics.md](./results/2026_04_public_diagnostics.md) | April 2026 public-safe diagnostic snapshot |
| [results/structured_tasks.md](./results/structured_tasks.md) | Structured-task benchmark summary |
| [data/300m_comparison.json](./data/300m_comparison.json) | Machine-readable 300M result data |
| [data/1b_pilot_results.json](./data/1b_pilot_results.json) | Machine-readable 1B pilot data |
| [data/2026_04_public_diagnostics.json](./data/2026_04_public_diagnostics.json) | Machine-readable April 2026 public-safe diagnostics |

Tables are treated as canonical. Images and plots, when present, are auxiliary only.

---

## Compute support

The bottleneck is controlled compute, not idea generation.

The highest-value next step is not one huge blind scale run. It is a set of carefully separated experiments that test:

| Question | Why it matters |
|---|---|
| Does the structural-transfer signal survive at 100M+ and 1B+? | This tests whether the current 66.5M signal is a scaling direction or a small-model artifact. |
| Do broader text/code/math mixtures improve external tasks without destroying structured transfer? | This tests whether LUMI is becoming more general, not merely better at one diagnostic domain. |
| Can instruction-style behavior be added without erasing base capability? | This tests whether conversation ability is a conversion of base capability or just superficial tuning. |
| Which failures are architecture failures vs data/curriculum failures? | This determines whether scaling is justified. |

What is being offered:

- a clear public research record
- controlled experiment plans
- negative-result analysis
- public-safe benchmark reporting
- an unusual architecture direction with enough signal to justify more compute

What is not being offered:

- weights
- full implementation disclosure
- reproduction-level recipes
- private training data mixtures

---

## Current status

| Area | Status |
|---|---|
| 300M controlled compression comparison | Public result available |
| 1B pilot | Public convergence note available |
| 66.5M 2026 diagnostics | Public-safe summary available |
| broad assistant/chat capability | Not yet established |
| next major need | controlled 100M+ and 1B+ compute |

---

## Contact

**Project:** LUMI-Arch  
**Author:** [@Mikeore](https://github.com/Mikeore)  
**Scope:** independent research, 2025-2026

If you are interested in compute support, collaboration, or benchmarking discussion, feel free to reach out via GitHub.
