# LUMI-Arch: Natural Language LM Sanity Check
**Date:** 2026-03-26
**Status:** WEAK PASS

---

## What was tested

A compact architecture research direction (LUMI-Arch) was evaluated against a
standard causal Transformer baseline on autoregressive language modeling.

The core hypothesis: *an alternative compact sequence mechanism can match
standard self-attention in next-token prediction quality at small scale.*

---

## Setup

| | LUMI-Arch | Baseline |
|---|---|---|
| Sequence mechanism | compact structure-aware mixer | causal multi-head attention |
| Core parameter budget | smaller | standard |
| Layers | 4 | 4 |
| Model width | matched | matched |
| Per-layer complexity | sub-quadratic | O(n²) |

- Dataset: WikiText-103 (GPT-2 tokenizer)
- Steps: 5,000
- Hardware: single consumer GPU (8 GB VRAM)

---

## Results

### Final val BPB (bits per byte, lower = better)

| Model | val BPB |
|---|---|
| LUMI-Arch | **1.741** |
| Baseline | 1.660 |
| Δ | **+0.081** |

**Pass threshold:** ±0.10 BPB
**Verdict: WEAK PASS**

---

## Learning curve

| Step | LUMI BPB | BASE BPB | Gap |
|---|---|---|---|
| 500 | 2.286 | 1.970 | +0.316 |
| 1,000 | 2.031 | 1.867 | +0.164 |
| 2,000 | 1.858 | 1.760 | +0.098 |
| 3,000 | 1.794 | 1.715 | +0.079 |
| 5,000 | **1.741** | **1.660** | **+0.081** |

Gap narrows from **+0.32 → +0.08** over training and stabilizes.

---

## Key observations

- The architecture runs efficiently on the tested hardware
- The gap reduction trend is consistent with the hypothesis that the mechanism
  adapts to corpus statistics over training
- LUMI-Arch achieves this with a smaller core parameter budget than the baseline

---

## What this does not show

- Performance at scale (>1B parameters)
- Instruction-following or reasoning capability
- Long-context behavior (seq=256 only)
- Comparison against other efficient sequence architectures

This is a **proof-of-concept** at toy scale.
The hypothesis remains viable at this scale. Full validation requires further scale-up.

---

## Relation to prior results

This natural-language LM result extends the earlier structured-task benchmark
record (mod_arith, bracket_structural_holdout, dsl_distributive) to a standard
language modeling setting.

The same research direction that showed consistent structural OOD generalization
on symbolic tasks also passes the natural-language sanity gate within tolerance.
