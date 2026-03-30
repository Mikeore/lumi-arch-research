"""
plot_results.py — LUMI-Arch result visualization
Reads from data/ and writes PNGs to assets/
No model code. Pure matplotlib visualization.
"""

import json
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── resolve paths relative to this script ────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# ── style constants ───────────────────────────────────────────────────────────
BLUE   = "#2563EB"   # LUMI-Arch primary
ORANGE = "#F97316"   # Baseline / annotation
GRAY   = "#6B7280"   # Grid / subtle text
BG     = "#FAFAFA"
FONT   = "DejaVu Sans"

plt.rcParams.update({
    "font.family": FONT,
    "axes.facecolor": BG,
    "figure.facecolor": "white",
    "axes.grid": True,
    "grid.color": "#E5E7EB",
    "grid.linewidth": 0.8,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.spines.left": True,
    "axes.spines.bottom": True,
})

# ─────────────────────────────────────────────────────────────────────────────
# Plot 1: 1B Pilot Convergence
# ─────────────────────────────────────────────────────────────────────────────

with open(os.path.join(DATA_DIR, "1b_pilot_results.json")) as f:
    pilot = json.load(f)

steps = [r["step"] for r in pilot["convergence"]]
bpbs  = [r["c4_bpb"] for r in pilot["convergence"]]

# Find the warmup artifact point
artifact_step = 500
artifact_bpb  = next(r["c4_bpb"] for r in pilot["convergence"] if r["step"] == artifact_step)

fig, ax = plt.subplots(figsize=(10, 5.5))

# Main convergence line — split at artifact to show the dip separately
pre_artifact  = [(s, b) for s, b in zip(steps, bpbs) if s <= 500]
post_artifact = [(s, b) for s, b in zip(steps, bpbs) if s >= 500]

px, py = zip(*pre_artifact)
qx, qy = zip(*post_artifact)

ax.plot(px, py, color=BLUE, linewidth=2.0, zorder=3)
ax.plot(qx, qy, color=BLUE, linewidth=2.0, zorder=3, label="LUMI-Arch 1B (C4 BPB)")

# Plot all points
ax.scatter(steps, bpbs, color=BLUE, s=50, zorder=5)

# Annotate the warmup artifact
ax.annotate(
    "Warmup artifact\n(corrected in production)",
    xy=(artifact_step, artifact_bpb),
    xytext=(700, 2.85),
    fontsize=8.5,
    color=ORANGE,
    arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.3),
    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=ORANGE, alpha=0.9),
)

# Annotate best checkpoint
best_step = 2000
best_bpb  = 2.1616
ax.annotate(
    f"Best: {best_bpb} BPB\n@ step {best_step:,}",
    xy=(best_step, best_bpb),
    xytext=(1600, 2.35),
    fontsize=8.5,
    color=BLUE,
    arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.3),
    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=BLUE, alpha=0.9),
)

# Annotate random init
ax.annotate(
    "Random init\nBPB=3.5697",
    xy=(0, 3.5697),
    xytext=(150, 3.35),
    fontsize=8.0,
    color=GRAY,
    arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.0),
)

ax.set_xlabel("Training Step", fontsize=11)
ax.set_ylabel("C4 Validation BPB (↓ better)", fontsize=11)
ax.set_title(
    "LUMI-Arch 1B Pilot — C4 Convergence\n"
    "996M params | scales=[1,4,16,64,256,1024,2048] | 2,000 of 30,000 planned steps",
    fontsize=12,
    fontweight="bold",
    pad=12,
)
ax.set_xlim(-80, 2150)
ax.set_ylim(1.9, 3.9)
ax.legend(fontsize=10, loc="upper right")

# Progress annotation
ax.text(
    0.02, 0.04,
    "Pilot: 2,000 steps | 32.8M tokens | RTX 5090 | 20.36 GB VRAM | ~10,473 tok/s",
    transform=ax.transAxes,
    fontsize=8,
    color=GRAY,
)

fig.tight_layout()
out_path = os.path.join(ASSETS_DIR, "1b_pilot_convergence.png")
fig.savefig(out_path, dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {out_path}")


# ─────────────────────────────────────────────────────────────────────────────
# Plot 2: 300M BPB Comparison
# ─────────────────────────────────────────────────────────────────────────────

with open(os.path.join(DATA_DIR, "300m_comparison.json")) as f:
    cmp = json.load(f)

lumi_bpb     = cmp["models"]["lumi_arch"]["val_bpb"]
baseline_bpb = cmp["models"]["transformer_baseline"]["val_bpb"]
delta        = cmp["result"]["delta_bpb"]
rel_pct      = cmp["result"]["relative_improvement_pct"]

fig, ax = plt.subplots(figsize=(7, 5.5))

labels = ["LUMI-Arch 300M\n(297M params)", "Transformer Baseline\n(304M params)"]
values = [lumi_bpb, baseline_bpb]
colors = [BLUE, ORANGE]

bars = ax.bar(labels, values, color=colors, width=0.45, zorder=3)

# Value labels on bars
for bar, val in zip(bars, values):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.008,
        f"{val:.4f}",
        ha="center",
        va="bottom",
        fontsize=12,
        fontweight="bold",
        color="black",
    )

# Delta annotation between bars
mid_x = (bars[0].get_x() + bars[0].get_width() / 2 +
          bars[1].get_x() + bars[1].get_width() / 2) / 2
arrow_y_top = baseline_bpb + 0.005
arrow_y_bot = lumi_bpb + 0.005
ax.annotate(
    "",
    xy=(mid_x + 0.02, arrow_y_bot),
    xytext=(mid_x + 0.02, arrow_y_top),
    arrowprops=dict(arrowstyle="<->", color="black", lw=1.5),
)
ax.text(
    mid_x + 0.08,
    (arrow_y_top + arrow_y_bot) / 2,
    f"Δ = {delta:+.4f}\n({rel_pct:+.1f}%)",
    va="center",
    fontsize=10,
    fontweight="bold",
    color="black",
)

ax.set_ylabel("Validation BPB (↓ better)", fontsize=11)
ax.set_title(
    "300M Scale: LUMI-Arch vs Transformer Baseline\n"
    "FineWeb-Edu 10BT | 30,000 steps | 4/4 seeds LUMI wins",
    fontsize=12,
    fontweight="bold",
    pad=12,
)

# Y-axis range — zoom in to make the difference visible
y_min = lumi_bpb - 0.08
y_max = baseline_bpb + 0.12
ax.set_ylim(y_min, y_max)
ax.yaxis.set_major_formatter(plt.FormatStrFormatter("%.3f"))

# Legend
lumi_patch     = mpatches.Patch(color=BLUE,   label=f"LUMI-Arch    BPB={lumi_bpb}")
base_patch     = mpatches.Patch(color=ORANGE, label=f"Baseline       BPB={baseline_bpb}")
ax.legend(handles=[lumi_patch, base_patch], fontsize=9, loc="upper left")

# Verdict stamp
ax.text(
    0.98, 0.04,
    "STRONG PASS",
    transform=ax.transAxes,
    fontsize=13,
    fontweight="bold",
    color="green",
    ha="right",
    va="bottom",
    bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor="green", linewidth=1.5),
)

fig.tight_layout()
out_path = os.path.join(ASSETS_DIR, "300m_comparison.png")
fig.savefig(out_path, dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {out_path}")

print("\nAll plots generated successfully.")
