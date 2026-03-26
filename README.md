# LUMI-Arch Research Notes

Public-facing research notes from an independent compact architecture project.

This repository documents evaluation evidence as the project progresses.
It is intentionally scoped to results and interpretation — not implementation.

---

## What this project is exploring

The central question is whether compact models can achieve meaningful language
understanding through architectural choices rather than scale alone.

The working hypothesis is that the right structural bias can allow a small model
to do more with less — in terms of both parameters and compute.

This is not a finished system. It is an active research direction with growing
benchmark evidence across structured and natural-language settings.

---

## Current evidence

### Natural language modeling

→ [LM Sanity Check Note](./sanity_check_note_public.md)

A compact architecture variant was evaluated against a standard Transformer
baseline on autoregressive language modeling (WikiText-103, single consumer GPU).

Result: **WEAK PASS** — within tolerance of the baseline, with a gap that
narrowed consistently over training.

### Structured generalization

→ [lumi-golf](https://github.com/Mikeore/lumi-golf)

Earlier benchmark evidence from structured symbolic tasks, including grokking-style
generalization, structural out-of-distribution evaluation, and parameter-matched
baseline comparisons.

---

## What is not here

- Implementation details or architecture specifics
- Training recipes or hyperparameter sweeps
- Model weights or checkpoints

The internal research workflow remains non-public.
These notes exist to communicate direction and evidence, not to reproduce the system.

---

## Status

Active. Evaluation scope expanding toward larger-scale natural language settings.
