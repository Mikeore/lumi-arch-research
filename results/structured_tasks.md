# Structured-Task Results

**Status:** archived motivation evidence
**Disclosure level:** public-safe summary

Before the larger language-model experiments, LUMI-Arch was tested on small structured-generalization tasks. These tasks were used to probe whether the model family could learn rules rather than only memorize examples.

This page preserves the public-safe interpretation. Implementation details and reproduction-level task recipes are intentionally omitted.

---

## Summary

| Task family | Public-safe result | Interpretation |
|---|---|---|
| modular arithmetic style generalization | LUMI-family won against matched baseline | Early evidence of rule transfer rather than memorization. |
| structural bracket holdout | LUMI-family won against matched baseline | Early evidence of out-of-distribution structural generalization. |
| symbolic rewrite transfer | LUMI-family won against matched baseline | Early evidence that compact structural bias can help compositional transfer. |

These results motivated the later compression and scale-up experiments. They are not the main current evidence.

---

## What "won" means here

In this archived suite, "won" means:

- higher held-out accuracy than a matched baseline
- consistent direction across multiple seeds
- better behavior on held-out structural cases, not just training examples

The important distinction was memorization vs transfer.

---

## Current interpretation

The structured-task results are useful because they pointed toward a real research direction:

> the architecture family may encourage representations that transfer across structural forms.

However, small structured tasks are not enough. The later public record therefore moved to:

- 300M matched language-model compression
- near-1B convergence
- private 2026 diagnostics with external language-model checks

---

## Disclosure boundary

This page intentionally omits:

- exact task-generation recipes
- source implementation
- architecture mechanics
- hyperparameter choices
- full reproduction instructions

The public goal is to document the evidence trail, not to publish a cloneable benchmark package.
