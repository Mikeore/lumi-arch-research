# 300M Matched Compression Comparison

**Status:** public positive compression signal
**Disclosure level:** public-safe summary

This note reports the public-safe result of a controlled 300M-scale comparison between a LUMI-family model and a parameter-matched Transformer baseline.

Exact architecture internals, training recipes, and reproduction-critical details are intentionally withheld.

Raw public-safe values: [`data/300m_comparison.json`](../data/300m_comparison.json)

---

## Setup summary

| Property | Public-safe value |
|---|---|
| comparison type | matched architecture comparison |
| scale class | 300M |
| dataset family | public educational web text |
| primary metric | validation BPB, lower is better |
| seeds | 4 independent seeds |

The key independent variable was architecture family, not parameter class.

---

## Main result

| Model | Validation BPB |
|---|---:|
| LUMI-family model | **1.2341** |
| matched Transformer baseline | **1.4220** |
| delta | **-0.1879 BPB** |
| relative change | **-13.2%** |

Lower BPB means the model requires fewer bits to encode held-out text. In this controlled setup, the LUMI-family model compressed the validation data more efficiently than the matched Transformer baseline.

---

## Seed consistency

| Check | Result |
|---|---:|
| seeds run | **4** |
| seeds favoring LUMI-family | **4** |

The important point is not just the best score. The direction held across all tested seeds.

---

## Interpretation

This is currently the strongest public compression result in the repository.

It supports the claim that the LUMI-Arch direction has a real architecture-level signal at compact scale.

It does not prove:

- state-of-the-art performance
- assistant capability
- broad downstream superiority
- full-scale convergence
- reproducibility from public materials

---

## Why the details are limited

This public repository is meant to make the evidence auditable without making the internal system easy to clone.

For that reason, this page omits:

- exact model configuration
- source implementation
- private training recipe
- optimizer and initialization details
- reproduction-level architecture mechanics

The public claim is intentionally narrower:

> At matched 300M scale, a LUMI-family model produced a strong and seed-consistent compression result against a Transformer baseline.
