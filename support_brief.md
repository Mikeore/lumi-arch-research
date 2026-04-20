# LUMI-Arch Support Brief

## What this project is

LUMI-Arch is an independent AI architecture research project focused on compact language models, compression pressure, and structural transfer.

The central question is:

> Can a smaller model become more capable by learning under stronger structural constraints, rather than depending mostly on brute-force scale?

This is not a product pitch. It is a technical research program looking for evidence that a different architecture/training pressure can improve capability per unit of compute.

---

## Why it matters

Most serious model research now depends on very large compute budgets. That makes it easier to scale known recipes and harder to test alternative architecture ideas.

LUMI-Arch is trying to keep one of those alternative paths alive: compact models that learn stronger abstractions from compression and transfer pressure.

The project is also deliberately failure-aware. A result is not considered meaningful just because one internal metric improves. The research tracks whether gains survive external checks and whether they destroy other abilities.

---

## What has already been shown

The project has moved beyond idea stage.

| Evidence | Public-safe result |
|---|---:|
| 300M matched compression comparison | LUMI-family **1.2341 BPB** vs Transformer **1.4220 BPB** |
| seed consistency | **4 / 4** seeds favored LUMI-family |
| 1B pilot feasibility | **996M** parameter pilot reached stable early convergence |
| 2026 private diagnostic branch | internal structural transfer **0.590**, text BPB **1.831** |
| external reality check | HellaSwag **0.292**, PIQA **0.529**, ARC-Challenge **0.227** |
| current private track | context-efficiency diagnostics for compact byte-level models |

The honest interpretation is:

- compression and structural-transfer signals are real enough to justify more compute
- a newer private track is testing context efficiency without exposing the mechanism
- broad assistant-grade capability is not yet established
- the next stage must test scale, data breadth, and instruction behavior without losing base capability

---

## Why the public repo is intentionally limited

The public repository is here:

<https://github.com/Mikeore/lumi-arch-research>

It is designed to show evidence, not to expose a build recipe.

Public:

- results summaries
- machine-readable public-safe data
- failure-mode analysis
- compute needs

Not public:

- source implementation
- checkpoints or weights
- private data mixture
- training recipes
- reproduction-level architecture internals

This boundary is important. The project is early enough that premature full disclosure would create imitation risk without yet producing the scientific benefit of a mature open release.

---

## What support would unlock

The immediate bottleneck is controlled GPU time.

Useful support would fund targeted experiments, not a blind scale chase:

1. 100M+ runs to test whether structural-transfer gains survive scale.
2. 1B+ runs to test whether compression pressure continues to improve general representation learning.
3. context-efficiency diagnostics for compact byte-level models.
4. broader text/code/math/reasoning data tests to avoid building a narrow puzzle machine.
5. instruction-tuning branches that must preserve base ability rather than merely sounding conversational.
6. external benchmark reruns after every important branch.

Even modest compute support would matter because the project is already set up around controlled comparisons and negative-result analysis.

---

## What makes this worth supporting

LUMI-Arch is unusual in a useful way:

- It has public controlled evidence, not only speculation.
- It has a clear disclosure boundary, so support does not require immediate IP exposure.
- It is compute-limited more than hypothesis-limited.
- It is testing an architecture direction that is different from simply scaling the standard recipe.
- It can provide public-safe reports without publishing source, weights, recipes, or reproduction-critical internals.

The best framing is:

> LUMI-Arch is an independent compact-model research program with promising compression and transfer signals, clear failure analysis, and a compute bottleneck that now limits the quality of the evidence.

Support would help answer whether the signal scales.
