# Archived Natural-Language Sanity Check

**Date:** 2026-03-26
**Status:** archived early sanity result
**Disclosure level:** public-safe summary

This was an early compact language-model sanity check. It is preserved for historical continuity, but it is no longer the headline public result.

The newer public-facing evidence is summarized in:

- [`README.md`](./README.md)
- [`public_results_snapshot.md`](./public_results_snapshot.md)
- [`results/300m_scale_comparison.md`](./results/300m_scale_comparison.md)
- [`results/2026_04_public_diagnostics.md`](./results/2026_04_public_diagnostics.md)

---

## What was tested

A compact LUMI-family branch was compared with a parameter-matched Transformer-style baseline on a small natural-language language-modeling sanity check.

The purpose was simple:

> Rule out the possibility that the architecture direction immediately fails at basic next-token prediction.

---

## Public result

| Model family | Validation BPB |
|---|---:|
| LUMI-family early branch | **1.741** |
| matched baseline | **1.660** |
| delta | **+0.081** |
| archived verdict | viability-only historical result |

This was not a win over the baseline. It was a viability check.

---

## Current interpretation

This result should be read as historical context only.

It showed that the early branch was not immediately disqualified for basic language modeling, but the project has since moved to stronger public evidence:

- a 300M matched compression result
- a near-1B convergence pilot
- newer private structural-transfer diagnostics

---

## What remains intentionally omitted

This archived note omits implementation details, exact architecture mechanics, training recipes, and reproduction-level configuration.
