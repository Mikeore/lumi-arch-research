# LUMI-Arch Research Notes

![Status](https://img.shields.io/badge/Status-Active%20Research-brightgreen)
![Stage](https://img.shields.io/badge/Stage-Active%20Diagnostics-blue)
![License](https://img.shields.io/badge/License-Research%20Only-orange)

**Independent AI architecture research** focused on compact language models with strong structural bias.

![LUMI public snapshot](./assets/public_results_snapshot.png)

---

## At a glance

LUMI-Arch is an independent research program exploring whether a compact, compression-first sequence architecture can outperform a parameter-matched Transformer baseline through architectural bias rather than scale alone.

The public record is intentionally limited to:

- evaluation evidence
- benchmark interpretation
- research direction

It does **not** expose implementation details, training recipes, or enough architectural information to reproduce the system.

---

## Current public evidence

### Compact LM sanity evidence

On a controlled small-scale natural-language comparison, a LUMI-family mixer
showed competitive behavior against a parameter-matched Transformer baseline:

- LUMI-family sanity branch: **1.7411 val BPB**
- Transformer baseline: **1.6599 val BPB**
- delta: **+0.0812 BPB**
- verdict: **WEAK PASS within preset tolerance**

This does **not** claim state-of-the-art quality.  It supports a narrower point:
the compact sequence mechanism remains viable enough to justify continued
research rather than being ruled out immediately.

### Large-scale training feasibility

Recent private experiments indicate that the broader research program can be
trained at substantially larger scale, and that its failure modes are now
better understood:

- compact language modeling remains the strongest current signal
- ARC-style reasoning remains bottlenecked by supervision and curriculum design
- some regularized variants collapse into shallow shortcuts rather than genuine
  content generation

This repository intentionally summarizes those findings only at a high level.
It does **not** expose the implementation detail required to reproduce them.

### Structured generalization

Earlier experiments on symbolic and compositional tasks showed repeated wins on:

- `mod_arith`
- `bracket_structural_holdout`
- `dsl_distributive`

Those results motivated the scale-up program.

---

## Why this matters

The central question behind LUMI-Arch is simple:

> Can the right structural inductive bias let a smaller model do meaningfully more with less?

The project takes the working view that language modeling quality is not only a matter of parameter count, but also of how strongly the architecture biases the model toward useful compression and hierarchical structure.

The current evidence suggests that this hypothesis remains alive in language
modeling, not only in symbolic settings, but the project is still in a
diagnostic phase rather than a finished “proved at scale” state.

---

## Public materials

| Path | Description |
|---|---|
| [public_results_snapshot.md](./public_results_snapshot.md) | One-page public summary for compute / partner outreach |
| [sanity_check_note_public.md](./sanity_check_note_public.md) | Early small-scale natural-language sanity check |
| [results/300m_scale_comparison.md](./results/300m_scale_comparison.md) | 300M parameter-matched comparison |
| [results/1b_pilot_convergence.md](./results/1b_pilot_convergence.md) | 1B pilot convergence note |
| [results/structured_tasks.md](./results/structured_tasks.md) | Structured-task benchmark summary |
| [data/300m_comparison.json](./data/300m_comparison.json) | Machine-readable 300M result data |
| [data/1b_pilot_results.json](./data/1b_pilot_results.json) | Machine-readable 1B pilot data |

---

## What is intentionally not public

This repository does **not** contain:

- model source code
- architecture implementation
- training loop details
- hyperparameter sweeps
- optimizer / initialization specifics
- full recipes for reproducing the reported system
- checkpoints or weights

The goal of this repository is to establish **evidence and direction**, not to open-source the full internal research workflow at this stage.

---

## Compute support

This project is currently constrained much more by **compute budget** than by
the ability to generate new hypotheses.

Additional compute would be used for tightly scoped diagnostics, not for a
blind brute-force scale chase.  The highest-priority next experiments are:

1. compact LM sanity replications on larger and cleaner text corpora
2. broad-structure pretraining pilots that test math / puzzle / structured
   transfer without exposing private implementation details
3. multilingual compression pilots that probe whether language diversity helps
   abstraction formation

What is **not** being offered here:

- no weights
- no training recipe sufficient for reproduction
- no hidden implementation disclosure on request

What **is** being offered:

- a legible public research record
- concrete experiment plans
- negative-result analysis and failure-mode documentation
- a compact, unusual architecture direction with early evidence worth testing

If you're evaluating support, the best framing is:

> LUMI-Arch is an independent compact-model research program with promising
> efficiency signals, unusually clear failure analysis, and a compute bottleneck
> that is now more limiting than idea generation.

---

## Current status

- **compact LM sanity branch:** completed, weak-pass signal obtained
- **private scale diagnostics:** active
- **current research focus:** diagnosing supervision / curriculum bottlenecks,
  broad-structure training, and multilingual compression
- **next public milestone:** a cleaner public-facing summary of which hypotheses
  survived the latest diagnostics

---

## Contact

**Project:** LUMI-Arch  
**Author:** [@Mikeore](https://github.com/Mikeore)  
**Scope:** independent research, 2025–2026

If you're interested in compute support, collaboration, or benchmarking
discussion, feel free to reach out via GitHub.
