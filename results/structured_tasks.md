# Structured Task Results: G2–G4 Suite

**Stage S1.5 — Complete**
*Tiny-scale structured generalization evaluation*

---

## Overview

Before committing to large-scale language modeling experiments, LUMI-Arch was evaluated on a suite of structured generalization tasks designed to probe whether the architectural prior imposed by CMSA leads to qualitatively different — and better — generalization behavior than a standard Transformer baseline.

These tasks are intentionally small (the "tiny" scale): they do not require large compute, but they are specifically designed so that a model that memorizes training data will fail, while a model that learns the underlying rule will succeed. This makes them a sensitive test of inductive bias.

All tasks use:
- **Multi-seed evaluation** (multiple independent random seeds)
- **Canonical train/test splits** (fixed, not shuffled)
- **Non-training holdout sets** (test examples that were never seen during training)
- **Parameter-matched baselines** (same parameter count, different architecture)

---

## Task Results

### G2: mod_arith — Grokking-Style Generalization

**Task:** Modular arithmetic. Learn the mapping `(a + b) mod p = c` from a training subset of all possible (a, b) pairs.

**What "winning" means:** The task is designed in the spirit of the "grokking" phenomenon — models can appear to memorize training data and plateau, but then suddenly generalize (often after significant additional training). A model that wins this task shows genuine generalization to held-out (a, b) pairs, not just memorization.

**Result: LUMI-Arch wins.**

LUMI-Arch generalizes to the held-out test set where the Transformer baseline memorizes. The CMSA scale hierarchy appears to promote the internalization of the modular structure rather than surface-level pattern matching.

---

### G3: bracket_structural_holdout — OOD Structural Generalization

**Task:** Bracket matching / structural parsing. The model must correctly identify whether a bracket sequence is valid. The test set contains structural patterns that were systematically held out from training — not just unseen examples from the same distribution, but examples that exercise structural properties not present in the training distribution.

**What "winning" means:** The model must generalize the rule (matching brackets form a valid sequence) to novel structural configurations. A model that has learned the rule succeeds on OOD examples; a model that has learned surface statistics fails.

**Result: LUMI-Arch wins.**

LUMI-Arch generalizes to OOD structural configurations where the baseline fails to transfer. This is consistent with the hypothesis that CMSA's scale hierarchy encourages the model to learn hierarchical structural rules, which are by definition portable across structural contexts.

---

### G4: dsl_distributive — Symbolic Reasoning Transfer

**Task:** A domain-specific language (DSL) task involving distributive law application. The model must learn to apply a symbolic rewriting rule (distributivity) and transfer this knowledge to novel symbolic expressions.

**What "winning" means:** The model must transfer the symbolic rule to new expression forms not seen during training. This tests whether the model has learned the rule as a rule, or merely as a pattern that happens to work on the training distribution.

**Result: LUMI-Arch wins.**

LUMI-Arch demonstrates symbolic reasoning transfer where the baseline fails to generalize. This is the most demanding of the three completed tasks, as it requires the model to apply an abstract operation (distribution) across a novel compositional structure.

---

### boolean_logic — Status: Ongoing / Frozen

**Task:** Boolean logic evaluation. The model must correctly evaluate boolean expressions of increasing complexity.

**Status:** This task is currently ongoing and partially frozen pending further investigation. Results will be published when the evaluation is complete.

---

## What "Winning" Means: A Precise Statement

In each of the above tasks, "LUMI-Arch wins" means the following:

1. **LUMI-Arch achieves higher accuracy on the held-out non-training test set** than the parameter-matched Transformer baseline.
2. **The difference is consistent across multiple random seeds.** It is not a single lucky run.
3. **The Transformer baseline's failure mode is memorization.** The baseline achieves good training accuracy but fails to generalize to the OOD or held-out test conditions. LUMI-Arch does not exhibit this memorization failure, or exhibits it to a significantly lesser degree.

The key distinction is between **memorization** and **structural generalization**. A model that memorizes training data can achieve high training accuracy but will fail whenever the test distribution differs from the training distribution. A model that has internalized the underlying rule will generalize.

The G2–G4 results suggest that CMSA's architectural prior — forcing the model to aggregate information across multiple temporal scales rather than attending to arbitrary token pairs — systematically promotes structural rule learning over surface-level memorization.

---

## Connection to the 300M Results

The structured task results came before the 300M scale experiments and provided early evidence that the CMSA architectural prior leads to qualitatively better generalization behavior. The 300M result (−13.2% BPB, 4/4 seeds) can be seen as a scaled-up version of the same signal: at language modeling scale, the architectural prior leads to better compression of held-out text, which is the natural language analog of structural generalization on toy tasks.

---

## Methodology Notes

- All tasks are drawn from or inspired by the `lumi-golf` benchmark suite (see [lumi-golf repository](https://github.com/Mikeore/lumi-golf))
- Baselines are parameter-matched: same number of total parameters as the corresponding LUMI-Arch model, with full self-attention replacing CMSA
- "Multi-seed" means a minimum of 3 independent random seeds per task per model
- Train/test splits are fixed and published; they do not change between seeds
- No data augmentation or test-time adaptation is used

---

*For the 300M scale results, see `results/300m_scale_comparison.md`*
*For the 1B pilot, see `results/1b_pilot_convergence.md`*
