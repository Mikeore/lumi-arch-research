# Near-1B Pilot Convergence

**Status:** feasibility signal
**Disclosure level:** public-safe summary

This note reports an early near-1B convergence pilot. It is a training-feasibility result, not a completed benchmark claim.

Exact architecture internals, sequence configuration, training recipes, and reproduction-critical details are intentionally withheld.

Raw public-safe values: [`data/1b_pilot_results.json`](../data/1b_pilot_results.json)

---

## Setup summary

| Property | Public-safe value |
|---|---:|
| parameter class | near-1B |
| public parameter count | **996M** |
| run type | early convergence pilot |
| steps reported | **2,000** |
| hardware class | single high-end consumer GPU |
| peak VRAM | **20.36 GB** |
| observed throughput | **10,473 tok/s** |

This pilot was run to check whether the larger branch trains stably before committing to more expensive controlled runs.

---

## Convergence table

| Step | C4 BPB | Note |
|---:|---:|---|
| 0 | 3.5697 | random initialization |
| 250 | 2.5076 | early learning |
| 500 | 2.9706 | warmup artifact |
| 750 | 2.3249 | recovery after warmup |
| 1,000 | 2.2808 | stable improvement |
| 1,250 | 2.2199 | stable improvement |
| 1,500 | 2.1754 | stable improvement |
| 2,000 | **2.1616** | best pilot checkpoint |

The step-500 spike is treated as a warmup artifact. After that point, the curve improved smoothly through the end of the pilot window.

---

## Early external checks

| Benchmark | Result |
|---|---:|
| WikiText-103 BPB | **2.4047** |
| HellaSwag 0-shot | **0.226** |
| ARC-Easy 0-shot | **0.273** |
| LAMBADA accuracy | **0.000** |

These values are expected to be weak because the pilot is very early in training. They are included as a baseline, not as a capability claim.

---

## Interpretation

What this result supports:

- near-1B training is operationally feasible
- early convergence is stable after warmup
- memory use is within reach of high-end local hardware
- the project has a path to larger controlled tests

What this result does not support:

- completed 1B quality claims
- assistant capability
- benchmark competitiveness
- public reproduction

The useful conclusion is narrow but important:

> The larger branch is trainable enough to justify controlled 1B-scale experiments if compute is available.
