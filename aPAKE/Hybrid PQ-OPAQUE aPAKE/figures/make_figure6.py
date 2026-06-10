#!/usr/bin/env python3
"""Styled regeneration of Figure 6 (runtime profile, log-scale).
Matches the Figure 1-5 series: same palette, sans type, dashed rounded frame.
Writes ../img/figure_6.png at 300 dpi. Values are the canonical Run 1 Criterion
means on the Linux/Xeon platform (microseconds).
Run:  python3 make_figure6.py   (needs matplotlib)."""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(HERE, '..', 'img', 'figure_6.png')

BLUE   = ('#dce8f7', '#1b4a8b')
ORANGE = ('#fbe6cc', '#d9881d')
GREEN  = ('#d8ece1', '#317d5c')
KE3    = ('#efd9d4', '#9c6b63')
RED    = ('#f6d9d4', '#ab4335')
GRAY   = ('white',   '#5a5a5a')

# (label, value_us, display, color)  -- top to bottom
BENCH = [
    ('4DH profile',     224.23,  r'224.23 $\mu$s', BLUE),
    ('ML-KEM round',    336.09,  r'336.09 $\mu$s', ORANGE),
    ('KE2 generation',  557.13,  r'557.13 $\mu$s', GREEN),
    ('KE3 generation',  784950.0, '784.95 ms',     KE3),
    ('Argon2id',        787030.0, '787.03 ms',     RED),
    ('End-to-end auth', 806130.0, '806.13 ms',     GRAY),
]

fig, ax = plt.subplots(figsize=(7.2, 3.9), dpi=300)
fig.patch.set_facecolor('white')
fig.subplots_adjust(left=0.205, right=0.93, top=0.85, bottom=0.16)

labels = [b[0] for b in BENCH][::-1]
vals   = [b[1] for b in BENCH][::-1]
disp   = [b[2] for b in BENCH][::-1]
cols   = [b[3] for b in BENCH][::-1]
y = range(len(labels))

ax.set_axisbelow(True)
ax.xaxis.grid(True, which='major', color='#ececec', lw=0.9, zorder=0)
for yi, v, c in zip(y, vals, cols):
    ax.barh(yi, v, color=c[0], edgecolor=c[1], height=0.62, lw=1.3, zorder=3)
for yi, v, d in zip(y, vals, disp):
    ax.text(v * 1.18, yi, d, va='center', fontsize=8.5, color='#333', zorder=4)

ax.set_xscale('log')
ax.set_xlim(1, 3_000_000)
ax.set_yticks(list(y)); ax.set_yticklabels(labels, fontsize=9.5, color='#222')
ax.tick_params(axis='y', length=0)
ax.set_xticks([1, 10, 100, 1000, 10000, 100000, 1000000])
ax.set_xticklabels([r'1 $\mu$s', r'10 $\mu$s', r'100 $\mu$s', '1 ms',
                    '10 ms', '100 ms', '1 s'], fontsize=8, color='#444')
ax.set_xlabel('time', fontsize=10.5, color='#222')
ax.set_title('Log-scale, Criterion mean on the Linux/Xeon benchmark platform',
             fontsize=9.5, color='#222', pad=9)

for s in ('top', 'right'):
    ax.spines[s].set_visible(False)
for s in ('left', 'bottom'):
    ax.spines[s].set_color('#999'); ax.spines[s].set_linewidth(1.0)

fig.add_artist(FancyBboxPatch((0.018, 0.03), 0.966, 0.94,
               boxstyle="round,pad=0,rounding_size=0.02",
               transform=fig.transFigure, fc='none', ec='#444',
               lw=1.3, ls=(0, (6, 4)), clip_on=False))

fig.savefig(OUT, dpi=300, facecolor='white')
plt.close(fig)
print('wrote', os.path.normpath(OUT))
