# LUMI-Arch Public Results Snapshot

**Status:** active independent research  
**Focus:** compact architectures, compression pressure, structural transfer, and public-safe diagnostics

---

## Core claim

LUMI-Arch is testing whether stronger compression and structural training pressure can improve capability per unit of compute in compact language models.

This public repository exposes evidence and interpretation. It does not expose implementation details, recipes, checkpoints, or enough architecture detail to reproduce the internal system.

---

## Evidence table

| Track | Public-safe result | Why it matters |
|---|---:|---|
| 300M matched compression test | LUMI-family **1.2341 BPB** vs Transformer **1.4220 BPB** | Strong controlled signal that the architecture family can compress better than a matched baseline. |
| Seed consistency | **4 / 4** seeds favored LUMI-family | Reduces the chance that the 300M result is a lucky seed. |
| 1B pilot | **996M** parameter pilot reached **2.1616 C4 BPB** at 2K steps | Shows near-1B training is operationally feasible, but not a full-run quality claim. |
| 66.5M 2026 private diagnostic branch | structural transfer **0.590**, text BPB **1.831** | Indicates newer internal diagnostics improved transfer while preserving language-modeling signal. |
| External reality check | HellaSwag **0.292**, PIQA **0.529**, ARC-Challenge **0.227** | Shows non-random behavior, while making clear that broad assistant-grade competence is not yet established. |

---

## What the evidence supports

- The research direction has moved beyond a toy symbolic result.
- The 300M compression result is a meaningful public signal.
- The newer private diagnostics suggest structural transfer is improving.
- The project has enough instrumentation to distinguish progress from several shortcut failures.

## What the evidence does not yet prove

- It does not prove state-of-the-art language-model quality.
- It does not prove assistant/chat capability.
- It does not prove broad downstream superiority over open baselines.
- It does not make the internal system reproducible from public materials.

---

## Current interpretation

The strongest current working hypothesis is:

> LUMI's compression mechanism is valuable as a training pressure that improves internal representations and transfer, even when the compressed state is not exposed as a standalone public artifact.

This is an empirical hypothesis, not a settled claim. The next stage is to test whether the signal survives larger scale and broader data mixtures.

---

## Why compute support matters

The main bottleneck is controlled GPU time for comparison work.

The important next experiments are not blind scale runs. They are separated tests of:

| Question | Required evidence |
|---|---|
| Does structural transfer scale? | 100M+ and 1B+ runs with the same public-safe metrics. |
| Does broader data improve general ability? | External benchmarks and chat/code/math diagnostics, not only internal structural tasks. |
| Does instruction tuning preserve base capability? | Mixed continuation SFT branches with internal and external retention gates. |
| Are failures architectural or curricular? | Controlled ablations with one major variable changed at a time. |

---

## Disclosure policy

Shared:

- public-safe result summaries
- benchmark interpretation
- failure-mode notes
- compute needs

Withheld:

- source code
- checkpoints and weights
- exact architecture internals
- training recipes
- private data mixtures
- hyperparameter sweeps

This boundary is intentional. The goal is to make the research credible without making it easy to clone prematurely.
