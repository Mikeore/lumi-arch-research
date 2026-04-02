# LUMI-Arch Public Results Snapshot

**Status:** active independent research  
**Focus:** compact architecture exploration for efficient language modeling and structural generalization

---

## Core claim

LUMI-Arch is testing whether a compact, compression-first architecture can
remain competitive enough to justify continued scale-up and structured-data
experiments through architectural bias rather than brute-force scale alone.

This repository exposes **evidence**, not implementation.

---

## Public evidence so far

### Public compact-LM sanity result

- Dataset: WikiText-103
- Metric: validation BPB
- Setting: compact LUMI-family mixer vs parameter-matched Transformer baseline

**Result**

- LUMI-family branch: **1.7411**
- Transformer baseline: **1.6599**
- Delta: **+0.0812 BPB**
- Verdict: **WEAK PASS** under the branch's preset tolerance criterion

Interpretation: this is a proof that the sequence mechanism is plausible enough
to keep investing in, not a claim of broad superiority.

### Current private diagnostics (high level only)

Private runs at larger scale have already made two things clearer:

- natural-language compression remains the cleanest public-positive signal
- ARC-style reasoning is currently bottlenecked more by supervision and
  curriculum design than by raw willingness to scale

Those diagnostics are intentionally summarized without recipe detail or
reproduction-enabling implementation.

### Structured-task record

Earlier stages showed repeated wins on:

- `mod_arith`
- `bracket_structural_holdout`
- `dsl_distributive`

These experiments motivated the current language-model scale-up.

---

## What this snapshot does and does not claim

### It supports

- the architecture direction is not only a toy symbolic result
- the compact LM sanity result is meaningful enough to justify more testing
- the project has moved from vague idea stage into evidence-backed diagnostics

### It does not yet prove

- superiority at larger full-run scale
- broad downstream superiority over major open models
- instruction tuning or agent capability
- reproducibility of the internal system from public materials alone

---

## Why this project is interesting

Most modern LMs rely on scale plus standard attention. LUMI-Arch asks whether a stronger structural bias can deliver:

- better compression
- better data efficiency
- better structural generalization
- competitive scaling behavior at smaller model sizes

That is the research bet.

---

## Why compute support matters

The main bottleneck right now is not a shortage of hypotheses.  It is the cost
of running enough carefully chosen experiments to separate:

- architecture effects
- curriculum / supervision effects
- data-mixture effects
- language-diversity effects

Additional compute would go into:

1. compact LM replications on stronger corpora
2. broad-structure training pilots
3. multilingual compression pilots

This snapshot is designed to help potential supporters judge whether the
research direction is interesting enough to warrant those experiments, without
making the underlying system reproducible.

---

## Repository policy

This public repository intentionally omits:

- source implementation
- detailed architecture mechanics
- training recipes
- checkpoints and weights

The goal is to make the evidence legible without making the internal research workflow reproducible.
