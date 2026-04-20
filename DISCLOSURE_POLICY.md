# LUMI-Arch Disclosure Policy

**Status:** active public-safe boundary  
**Last updated:** 2026-04-20

This repository is meant to make the research direction and evidence legible
without publishing a reproduction path. The boundary is intentional: LUMI-Arch is
still early enough that full release would create imitation risk before the
scientific value of a mature open release is clear.

---

## Public by default

These materials can be shared publicly:

- high-level research questions
- public-safe result summaries
- machine-readable aggregate result tables
- external benchmark summaries
- failure-mode interpretation
- compute needs and experiment goals
- negative-result analysis

Public results should be caveated and tied to a recorded run or data file when
possible.

---

## Private discussion only

These may be discussed selectively with serious collaborators or compute
supporters, but are not published in the repository:

- planned evaluation categories
- approximate compute requirements
- public-safe experiment roadmaps
- benchmark interpretation details
- risk analysis and failure gates
- project status beyond the latest public snapshot

The goal is to help supporters understand the research program without making
the system easy to clone.

---

## NDA or trusted-review only

These are not public, but may be considered for trusted technical due diligence
under an explicit private-review agreement:

- limited architecture rationale
- selected internal logs or diagnostic summaries
- controlled experiment plans
- non-reproduction-level code walkthroughs
- compute-use reports

Even under private review, the default is to share the minimum needed to assess
the seriousness of the work.

---

## Not shared at this stage

These are withheld:

- source implementation
- checkpoints or weights
- exact architecture internals
- reproduction-level diagrams
- training recipes
- optimizer and initialization details
- private data mixtures
- hyperparameter sweeps
- prompt/SFT recipes or instruction-tuning data details

This boundary may change later if the research matures enough for a deliberate
open release. Until then, the public repository documents evidence and direction,
not a build recipe.

---

## Current private track boundary

A newer private track studies context efficiency in compact byte-level models.
The public repository may describe:

- the motivation
- the evaluation categories
- whether aggregate results are positive, mixed, or negative
- whether base language modeling is preserved

It will not disclose:

- the mechanism
- the implementation
- the internal state representation
- the exact training setup
- model configuration details
- data mixture details
- ablation names or reproduction-critical metrics

Public wording should describe the research problem, not the solution.
