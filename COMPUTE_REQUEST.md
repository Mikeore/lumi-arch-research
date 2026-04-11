# Compute Support Request

This page is an email-ready summary for GPU providers, research supporters, and potential collaborators.

---

## Short request

I am seeking GPU compute support for LUMI-Arch, an independent compact-model architecture research project.

The project has public evidence of compression and transfer signals, but the next questions require controlled 100M+ and 1B+ runs. The goal is not a blind scale chase. The goal is to test whether the observed structural-transfer signal survives larger scale and broader capability evaluations.

Repository:

<https://github.com/Mikeore/lumi-arch-research>

---

## Why this may be worth supporting

| Signal | Public-safe evidence |
|---|---:|
| matched 300M compression result | LUMI-family **1.2341 BPB** vs Transformer **1.4220 BPB** |
| seed consistency | **4 / 4** seeds favored LUMI-family |
| near-1B feasibility | **996M** pilot reached stable early convergence |
| newer private diagnostic signal | 66.5M branch reached structural transfer **0.590** and text BPB **1.831** |
| external reality check | HellaSwag **0.292**, PIQA **0.529**, ARC-Challenge **0.227** |

The honest state is: promising diagnostics, not a finished assistant model.

---

## What compute would be used for

| Experiment | Purpose |
|---|---|
| 100M+ controlled continuation | test whether structural-transfer gains survive scale |
| 1B+ controlled run | test whether compression pressure improves general representation learning at larger scale |
| broader data-mixture branches | test whether text/code/math/reasoning improve together rather than overfitting one private task |
| instruction-tuning branch | test whether chat ability can be added without erasing base capabilities |
| external benchmark reruns | prevent private-metric overfitting |

The project is currently compute-limited. The next step is not more speculation; it is running controlled comparisons.

---

## Disclosure boundary

I can share:

- public-safe results
- experiment goals
- failure-mode analysis
- benchmark summaries
- compute reports

I am not currently sharing:

- source code
- checkpoints or weights
- training recipes
- private data mixtures
- reproduction-level architecture details

This boundary is intentional. The project is still early enough that full disclosure would create imitation risk before the research is mature.

---

## Suggested email

Subject: Compute support request for independent compact-model research

Hello,

I am working on LUMI-Arch, an independent AI architecture research project focused on compact language models, compression pressure, and structural transfer.

The public repository is here:

<https://github.com/Mikeore/lumi-arch-research>

The short version is that the project has produced public-safe evidence worth testing further: a 300M matched compression result where a LUMI-family model reached 1.2341 BPB versus 1.4220 BPB for a matched Transformer baseline, 4/4 seed consistency, a near-1B pilot showing stable early convergence, and newer private diagnostics showing stronger structural-transfer behavior.

I am not asking for support for a blind scale run. The immediate goal is a controlled set of 100M+ and 1B+ experiments to test whether the transfer signal survives scale, whether broader text/code/math data improves general ability, and whether instruction-style behavior can be added without damaging base capabilities.

At this stage I am intentionally not publishing source code, checkpoints, training recipes, or reproduction-level architecture details. I can provide public-safe experiment reports, benchmark summaries, failure analysis, and compute-use summaries.

If you support independent research or offer GPU credits for experimental model work, I would be grateful to discuss whether LUMI-Arch is a fit.

Thank you for considering it.
