# LUMI-Arch: Causal Multi-Scale Averaging

![Status](https://img.shields.io/badge/Status-Active%20Research-brightgreen)
![Stage](https://img.shields.io/badge/Stage-S2%20In%20Progress-blue)
![License](https://img.shields.io/badge/License-Research%20Only-orange)

**Independent AI Architecture Research** | [@Mikeore](https://github.com/Mikeore) | 2025–2026

---

## Abstract

LUMI-Arch is an independent research project investigating whether self-attention — the dominant mechanism in modern language models — is a principled choice from an information-theoretic standpoint, or merely a historical accident that became entrenched through scale. We propose **Causal Multi-Scale Averaging (CMSA)**, a replacement for self-attention grounded in the **Minimum Description Length (MDL)** principle: the hypothesis that intelligence is compression, and that a better learning machine should find shorter, more general descriptions of data. CMSA aggregates token information at multiple temporal resolutions simultaneously, forming a hierarchy from local context (scale=1) to document-level context (scale=2048), with sparse FlashAttention interleaved at low frequency for global coherence. At 300M parameters, LUMI-Arch achieves a validation BPB of **1.2341** versus the Transformer baseline's **1.4220** — a **−0.1879 BPB improvement (−13.2% relative)**, consistent across all 4 independent seeds. A 996M-parameter pilot run confirms convergence behavior holds at 1B scale.

---

## Architecture Concept

```
Input Tokens
     |
     v
 ┌─────────────────────────────────────────────────────┐
 │                  CMSA Layer (×N)                    │
 │                                                     │
 │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ...     │
 │  │ Scale=1  │  │ Scale=4  │  │ Scale=16 │  ...     │
 │  │  Local   │  │  Token   │  │  Phrase  │          │
 │  │ Context  │  │  Group   │  │  Level   │          │
 │  └────┬─────┘  └────┬─────┘  └────┬─────┘          │
 │       └─────────────┴─────────────┘                 │
 │                      │                              │
 │             ┌─────────────────┐                     │
 │             │  Scale Fusion   │                     │
 │             │ (learned blend) │                     │
 │             └────────┬────────┘                     │
 └──────────────────────┼──────────────────────────────┘
                        │
          [Every 4th layer: Sparse FlashAttention]
          (Global context injection, NoPE design)
                        │
                        v
               Next-layer representation
```

**Scale hierarchy (1B model):** `[1, 4, 16, 64, 256, 1024, 2048]`

Each scale corresponds to a different level of linguistic structure — from single tokens to full document context — without the quadratic cost of full attention.

---

## Key Results

> **300M scale: LUMI val_bpb 1.2341 vs Transformer baseline 1.4220**
> **Δ = −0.1879 BPB | −13.2% relative improvement | 4/4 seeds confirm**

### Results Summary

| Task | Scale | LUMI-Arch | Baseline | Delta | Result |
|------|-------|-----------|----------|-------|--------|
| Language Modeling | 300M | 1.2341 BPB | 1.4220 BPB | −0.1879 | **STRONG PASS** |
| Language Modeling | 1B pilot | 2.1616 BPB | — | — | Converging |
| mod_arith (grokking) | tiny | wins | — | — | **PASS** |
| bracket_structural_holdout | tiny | wins | — | — | **PASS** |
| dsl_distributive | tiny | wins | — | — | **PASS** |
| boolean_logic | tiny | ongoing | — | — | in progress |

### 1B Pilot Convergence (C4, 2,000 of 30,000 planned steps)

| Step | C4 BPB | Note |
|------|--------|------|
| 0 | 3.5697 | Random initialization |
| 250 | 2.5076 | — |
| 500 | 2.9706 | Warmup schedule artifact (corrected in production) |
| 750 | 2.3249 | — |
| 1,000 | 2.2808 | — |
| 1,250 | 2.2199 | — |
| 1,500 | 2.1754 | — |
| **2,000** | **2.1616** | **Pilot end — best checkpoint** |

*Training ongoing. ~32.8M of 3.93B target tokens processed.*
*Hardware: NVIDIA RTX 5090 | 20.36 GB peak VRAM | ~10,473 tok/s*

---

## Research Philosophy

### Compression as the Core of Intelligence

LUMI-Arch is built on the conviction that the MDL principle — *the best model is the one that compresses data most efficiently* — is not merely a training heuristic but a statement about the nature of intelligence itself.

The theoretical anchor is the ITI (Inductive Bias of Transformers) line of work, which suggests that efficient compression mechanically selects for models that have internalized causal structure. A model that genuinely understands language should be able to compress it — not by memorizing surface patterns, but by learning the underlying generative rules.

Self-attention, from this perspective, has a structural inefficiency: it is quadratic in sequence length and unconstrained in what it attends to. It can in principle learn arbitrary token-to-token relationships, but this expressiveness comes at the cost of imposing no prior toward compression. CMSA is designed to impose that prior structurally, by forcing the model to aggregate information at discrete, exponentially spaced temporal scales — a design that mirrors how linguistic meaning actually accumulates across levels of structure.

**The core claim:** A model with the right structural inductive bias should be able to learn more from less data, generalize more reliably out-of-distribution, and do so with lower computational cost. The 300M results are early evidence that this claim is empirically grounded.

---

## Roadmap

| Stage | Description | Status |
|-------|-------------|--------|
| **S0** | Architecture design & MDL theoretical grounding | Done |
| **S1** | 300M scale validation vs Transformer baseline | **Done — STRONG PASS** |
| **S1.5** | Tiny structured task suite (G2–G4) | Done |
| **S2** | 1B scale full training (30K steps, 3.93B tokens) | **In progress** |
| **S3** | Ablation study: scale hierarchy, attention frequency | Planned |
| **S4** | Benchmark suite: MMLU, GSM8K, HumanEval | Planned |
| **S5** | Paper writeup and public release | Planned |

---

## What This Repository Contains

| Path | Contents |
|------|----------|
| `METHODOLOGY.md` | Conceptual explanation of CMSA and the MDL framework (no code) |
| `results/300m_scale_comparison.md` | Full 300M experimental results |
| `results/1b_pilot_convergence.md` | 1B pilot convergence data and analysis |
| `results/structured_tasks.md` | G2–G4 structured task results |
| `data/300m_comparison.json` | Machine-readable 300M result data |
| `data/1b_pilot_results.json` | Machine-readable 1B pilot data |
| `assets/` | Visualizations and convergence plots |
| `plot_results.py` | Visualization script (reads from `data/`, outputs to `assets/`) |

## What This Repository Does NOT Contain

This repository deliberately omits all implementation details. Specifically absent:

- Model source code (`.py` files with architecture logic)
- Training loop implementation
- Optimizer configuration and initialization details
- The internal mechanics of scale aggregation
- Gate mechanism design
- Any information sufficient to reproduce the architecture from this repository alone

The results reported here are real and reproducible — but only with access to the full codebase, which is not public at this stage of research.

---

## Contact & Citation

**Project:** LUMI-Arch (independent research, 2025–2026)
**Repository:** https://github.com/Mikeore/lumi-arch-research

If you reference this work, please cite:

```
Mikeore. "LUMI-Arch: Causal Multi-Scale Averaging for
Sub-Quadratic Language Modeling." Independent research report, 2026.
https://github.com/Mikeore/lumi-arch-research
```

*This is independent research. No institutional affiliation.*
