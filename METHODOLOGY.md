# LUMI-Arch Public Methodology

*A public-safe account of the research method and evidence standard. This document intentionally omits implementation details.*

---

## 1. Research bet

LUMI-Arch investigates a compact-model hypothesis:

> Better compression pressure and structural transfer can make a smaller model learn more useful representations per unit of compute.

The project is not trying to publish a cloneable architecture recipe at this stage. It is trying to produce a credible public record of whether the hypothesis deserves larger controlled runs.

---

## 2. What is being measured

The public record separates three kinds of evidence.

| Evidence type | Example metric | What it answers |
|---|---|---|
| Compression | BPB on held-out text | Can the model encode language efficiently? |
| Structural transfer | held-out structural / format-transfer diagnostics | Does structure learned in one form transfer to another? |
| Context efficiency | private long-dependency diagnostics | Can a compact byte-level model make better use of limited raw context? |
| External reality checks | HellaSwag, PIQA, ARC-style LM evals | Is the model learning anything beyond private diagnostics? |

No single metric is treated as decisive. A result is interesting only if it improves one axis without obviously destroying the others.

---

## 3. Evidence-first rule

LUMI-Arch uses a deliberately conservative reporting standard:

- public numbers must be tied to a recorded run or machine-readable data file
- internal diagnostics are labeled as internal diagnostics
- pilot runs are labeled as pilots
- external benchmarks are used to check for overfitting to private tasks
- negative results are treated as useful evidence, not hidden failures

This matters because architecture research can easily become story-driven. The project tries to keep the story subordinate to measurements.

---

## 4. Compression as training pressure

The current working interpretation is that the compression mechanism may be valuable as a training pressure.

In simple terms: forcing a model to pass information through a constrained internal representation can make the rest of the network organize features more usefully. Even if that compressed state is not presented publicly as a standalone module, the pressure can still change what the model learns.

This is why the project tracks both:

- direct performance numbers
- transfer and stability diagnostics

The goal is not to make a model that scores well on one private task. The goal is to test whether compression-oriented structure improves general representation learning.

---

## 5. Public-safe abstraction level

Some earlier public documents described architecture mechanics more concretely. The public boundary has now been tightened.

This repository intentionally avoids:

- implementation diagrams detailed enough to rebuild the system
- layer-by-layer architecture recipes
- private training schedules
- internal hyperparameter choices
- data-mixture details
- checkpoints and weights
- mechanism names or ablation labels when those would reveal the private approach

Instead, it shares:

- what was tested
- what moved
- what failed
- what still needs compute

That tradeoff is deliberate. The project benefits from public credibility, but premature disclosure would make the core work too easy to imitate before the research program is mature.

---

## 6. Current public evidence standard

A public result is treated as stronger when it satisfies more of the following:

| Criterion | Why it matters |
|---|---|
| matched baseline | separates architecture effect from scale effect |
| multiple seeds | reduces lucky-run risk |
| external benchmark check | reduces private-metric overfitting risk |
| machine-readable data | makes the public record auditable |
| caveats included | prevents overclaiming |

The 300M matched comparison is currently the strongest public compression result. The 1B pilot is a feasibility signal, not a completed benchmark claim. The 2026 diagnostic branch is public-safe evidence of newer internal progress, not a reproduction release.

A newer private context-efficiency track is reported only at the level of
motivation and evaluation categories. The mechanism is intentionally withheld.

---

## 7. What would count as stronger evidence

The next evidence tier would require:

| Target | Evidence needed |
|---|---|
| 100M+ scale confirmation | same diagnostics, larger model, controlled comparison |
| 1B+ full run | full training curve and external benchmark suite |
| context-efficiency confirmation | aggregate longer-dependency gains without base BPB regression |
| general capability claim | text, code, math, reasoning, and conversation evaluations |
| instruction-tuned branch | chat improvement while preserving base internal and external metrics |

This is why compute support matters. The remaining questions are empirical and require controlled runs.

---

## 8. Summary

LUMI-Arch is a compression-first architecture research program. The public record is designed to show that the direction has real signal while keeping reproduction-critical details private.

The current claim is intentionally narrow:

> There is enough public and private-safe evidence to justify larger controlled experiments.

It is not a claim that the architecture is finished, open, or already competitive with major frontier systems.
