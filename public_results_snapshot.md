# LUMI-Arch Public Results Snapshot

**Status:** active independent research  
**Focus:** compact architecture exploration for efficient language modeling and structural generalization

---

## Core claim

LUMI-Arch is testing whether a compact, compression-first architecture can beat a parameter-matched Transformer baseline through architectural bias rather than brute-force scale.

This repository exposes **evidence**, not implementation.

---

## Public evidence so far

### 300M scale language modeling

- Dataset: FineWeb-Edu 10BT
- Metric: validation BPB
- Setting: parameter-matched comparison against a standard Transformer baseline

**Result**

- LUMI-Arch: **1.2341**
- Transformer baseline: **1.4220**
- Delta: **-0.1879 BPB**
- Relative improvement: **-13.2%**
- Seed consistency: **4/4 seeds**
- Verdict: **STRONG PASS**

### 1B pilot

- Model size: **996M parameters**
- Run length: **2,000 steps**
- Device: **single RTX 5090**

**Observed**

- C4 BPB at step 2,000: **2.1616**
- Throughput: **~10.5k tok/s**
- Peak VRAM: **20.36 GB**

Interpretation: the recipe converges at 1B scale and can be piloted on accessible hardware, but full validation still requires longer runs.

### Structured-task record

Earlier stages showed repeated wins on:

- `mod_arith`
- `bracket_structural_holdout`
- `dsl_distributive`

These experiments motivated the current language-model scale-up.

---

## What this snapshot does and does not claim

### It supports

- the architecture is not just a toy symbolic result
- the 300M natural-language result is meaningful
- the 1B recipe is trainable in practice

### It does not yet prove

- superiority at 1B full-run scale
- broad downstream superiority over major open models
- instruction tuning or agent capability

---

## Why this project is interesting

Most modern LMs rely on scale plus standard attention. LUMI-Arch asks whether a stronger structural bias can deliver:

- better compression
- better data efficiency
- better structural generalization
- competitive scaling behavior at smaller model sizes

That is the research bet.

---

## Repository policy

This public repository intentionally omits:

- source implementation
- detailed architecture mechanics
- training recipes
- checkpoints and weights

The goal is to make the evidence legible without making the internal research workflow reproducible.
