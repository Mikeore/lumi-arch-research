# LUMI-Arch Methodology: Causal Multi-Scale Averaging (CMSA)

*A conceptual account of the architecture and its theoretical grounding.*
*This document contains no implementation code.*

---

## 1. Why Self-Attention Is Suboptimal from an MDL Perspective

The standard Transformer architecture uses self-attention as its primary mixing mechanism. Self-attention allows every token to attend to every other token in the context window, producing a weighted combination of all past token representations at each layer. This is elegant and expressive — but from the standpoint of Minimum Description Length (MDL), it has two structural problems.

**Problem 1: Quadratic cost.**
Self-attention is O(n²) in sequence length. At long contexts, this is not merely expensive — it is a structural statement about the model's inductive bias. The model is spending equal "attention budget" on every possible token pair, including pairs that carry no meaningful information. From an MDL perspective, a good model should focus its capacity where it matters most. A mechanism that scales quadratically with context length is spending that capacity diffusely.

**Problem 2: No temporal prior.**
Standard self-attention has no built-in assumption about the structure of time. It can, in principle, attend equally to a token one position back and a token 10,000 positions back. Language, however, has a strongly hierarchical temporal structure: characters form tokens, tokens form phrases, phrases form sentences, sentences form paragraphs. A mechanism with no temporal prior must learn this structure entirely from data — increasing the effective description length of the model class.

MDL says: the model class with the most appropriate inductive bias will converge to good solutions with fewer bits. A model whose architecture already encodes "close tokens matter most, but distant tokens sometimes matter too" should learn faster and generalize better than one that starts from scratch.

---

## 2. What CMSA Does: Hierarchical Temporal Aggregation

**Causal Multi-Scale Averaging (CMSA)** replaces self-attention with a mechanism that aggregates token information at multiple temporal resolutions simultaneously.

The intuition is straightforward. Instead of asking "which past tokens should I attend to?", CMSA asks: "what is the average state of the context at each of several pre-defined temporal scales?"

At each CMSA layer, the model maintains several parallel information streams, each operating at a different temporal resolution:

- **Scale = 1:** The most recent single token. Pure local context.
- **Scale = 4:** An average over the last ~4 tokens. Word-level context.
- **Scale = 16:** An average over the last ~16 tokens. Phrase-level context.
- **Scale = 64:** An average over the last ~64 tokens. Sentence-level context.
- **Scale = 256:** An average over the last ~256 tokens. Paragraph-level context. *(1B only)*
- **Scale = 1024:** An average over the last ~1024 tokens. Section-level context. *(1B only)*
- **Scale = 2048:** An average over the last ~2048 tokens. Document-level context. *(1B only)*

These scales are exponentially spaced — each is roughly 4× larger than the previous. This is not arbitrary. Exponential spacing means the model covers a large dynamic range (from 1 token to 2048 tokens) with only 7 scales, and that each scale is meaningfully different from its neighbors.

The outputs of all scale streams are then fused using learned scale weights, allowing the model to discover which temporal resolutions are most informative for a given prediction task.

**The result is sub-quadratic.** The core computation no longer grows as O(n²) with sequence length. CMSA imposes a strong, linguistically motivated prior on temporal structure, while remaining learnable and expressive.

### Scale Hierarchy at Each Model Size

**300M model:** scales = `[1, 4, 16, 64]`
Covers local-to-sentence context. Sufficient for S1 validation.

**1B model:** scales = `[1, 4, 16, 64, 256, 1024, 2048]`
Extends to document-level context. Matches the 2048-token sequence length used in 1B training.

---

## 3. Why Interleaved Sparse Attention?

Pure CMSA, without any form of global attention, would lose the ability to form long-range associations that do not fit the fixed exponential scale grid. Some language tasks require this: coreference resolution, long-range logical entailment, structural consistency across a document.

LUMI-Arch addresses this with a hybrid design: **sparse FlashAttention interleaved every 4th layer**.

The rationale is frequency decomposition. Most of the model's computation — the high-frequency work of predicting the next token given local context — is handled by CMSA at every layer. The low-frequency work of maintaining global coherence is handled by sparse attention at a fraction of layers. This mirrors how signal processing separates high- and low-frequency components: different mechanisms for different frequency bands.

**FlashAttention** is used for memory efficiency, and the attention pattern is sparse (not full O(n²)) to maintain the sub-quadratic overall cost profile.

The ratio (1 attention layer per 4 CMSA layers) is a design choice balancing global expressiveness against computational budget. At 300M scale, this corresponds to 5 attention layers in a 26-layer network. At 1B scale, this corresponds to approximately 5–6 attention layers in a 22-layer network.

---

## 4. NoPE Design Rationale

LUMI-Arch uses a **NoPE (No Position Encoding)** design: no explicit positional embeddings (sinusoidal, learned, or rotary) are added to token representations.

This is motivated by the observation that CMSA already encodes position implicitly. The scale hierarchy provides a natural positional signal: a token that falls within the scale=4 window but not within scale=1 is, by definition, 2–4 positions back. The model learns from this structural information rather than from a separate positional signal.

NoPE also connects to the MDL philosophy: adding positional encodings increases the description length of the model. If position information is already available through the scale hierarchy, adding explicit encodings is redundant — and redundancy is compression inefficiency.

Empirically, NoPE models have shown competitive or superior performance on tasks requiring structural generalization, as they are forced to learn positional relationships from data rather than relying on a fixed encoding scheme that may not generalize to novel structural patterns.

---

## 5. MDL Principle and Its Connection to Generalization

Minimum Description Length (MDL) is a formal principle from algorithmic information theory. The central claim is:

> **The best model is the one that, together with its predictions, minimizes the total description length of the data.**

This is the Occam's Razor of machine learning, made precise. A model that memorizes training data achieves low training loss but requires a long description (many bits to specify). A model that has learned the underlying rules achieves similar training loss with a shorter description. MDL says the second model is better — and this preference is not arbitrary, it is a statement about expected generalization.

In practice, MDL manifests in LUMI-Arch in several ways:

1. **Architecture selection:** CMSA is chosen because it imposes a prior that reduces the effective description length of the model class over self-attention.

2. **Scale selection:** Exponentially spaced scales are parsimonious. They cover the same dynamic range as linearly spaced scales with far fewer components.

3. **Training objective:** The standard cross-entropy loss on next-token prediction is equivalent to minimizing a code length under the model's predicted distribution. Lower BPB = shorter description = better compression.

4. **Evaluation philosophy:** The project uses BPB (bits per byte) as the primary metric because it has a direct information-theoretic interpretation: it measures how many bits the model needs, on average, to encode each byte of held-out text.

---

## 6. Connection to Information Theory: Compression as Causal Understanding

The deeper theoretical motivation for LUMI-Arch draws on a line of work arguing that compression is not merely correlated with intelligence — it *is* intelligence, in a formal sense.

The relevant insight, sometimes called the ITI hypothesis, is that an agent capable of compressing its observations to short descriptions has, by necessity, learned something about the causal structure of the world that generated those observations. You cannot efficiently compress a sequence without understanding the process that produced it.

This has a strong implication for language modeling: **a model that achieves lower BPB on held-out text has, by the compression-intelligence equivalence, learned more about the causal structure of language**. It is not enough to fit training data. The compression must generalize — and generalization is the test.

LUMI-Arch's 300M result — a −13.2% BPB improvement over a parameter-matched Transformer baseline, consistent across 4 seeds — is therefore not merely a benchmark win. It is evidence that the architectural prior imposed by CMSA is better aligned with the causal structure of language than unconstrained self-attention.

---

## 7. Why This Might Matter for AGI

This section is speculative, but it is the motivation behind the research.

If intelligence is compression, and if current large language models are limited by their architectural inability to efficiently compress structured information, then architectural improvements like CMSA could represent a path toward more general intelligence that does not depend purely on scale.

The standard scaling paradigm says: more parameters, more data, more compute → better performance. This is empirically true. But it leaves open the question of whether the current architectural family (Transformers with full self-attention) is the right one to scale, or merely the one that happened to be available when compute became cheap.

LUMI-Arch's hypothesis is that architecture matters — that the right structural inductive bias can allow a smaller model to compress and generalize better than a larger model with the wrong bias. The 300M results are early evidence. The 1B training, and the ablation studies planned for S3, are designed to test whether this hypothesis holds at scale.

The ultimate goal is not a better language model. It is a research direction: **understanding what architectural properties are necessary and sufficient for a system to learn general causal structure from sequential data.** The answer to that question is, we believe, deeply connected to the MDL principle — and LUMI-Arch is an attempt to make that connection empirically concrete.

---

*For experimental results, see the `results/` directory.*
*For raw data, see the `data/` directory.*
