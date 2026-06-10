#!/usr/bin/env python3
"""Styled regeneration of Figure 3 (authentication-message wire sizes).
Matches the hand-drawn Figure 1/2 aesthetic: same palette, sans type, dashed
rounded frame. Writes ../img/figure_3.png at 300 dpi. Exact byte counts below.
Run:  python3 make_figure3.py   (needs matplotlib + numpy)."""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(HERE, '..', 'img', 'figure_3.png')
BLUE   = ('#dce8f7', '#1b4a8b')   # classical
ORANGE = ('#fbe6cc', '#d9881d')   # hybrid

groups    = ['KE1', 'KE2', 'KE3']
classical = [88, 288, 64]
hybrid    = [1273, 1377, 65]

fig, ax = plt.subplots(figsize=(7.1, 3.8), dpi=300)
fig.patch.set_facecolor('white')
fig.subplots_adjust(left=0.11, right=0.95, top=0.82, bottom=0.17)
x = np.arange(3); w = 0.38

bc = ax.bar(x - w/2, classical, w, color=BLUE[0],   edgecolor=BLUE[1],
            lw=1.4, label='Classical payload', zorder=3)
bh = ax.bar(x + w/2, hybrid,    w, color=ORANGE[0], edgecolor=ORANGE[1],
            lw=1.4, label='Hybrid wire format', zorder=3)

for i in range(3):
    ax.text(x[i] - w/2, classical[i] + 22, str(classical[i]),
            ha='center', va='bottom', fontsize=8.5, color=BLUE[1], zorder=4)
    ax.text(x[i] + w/2, hybrid[i] + 22, str(hybrid[i]),
            ha='center', va='bottom', fontsize=8.5, color=ORANGE[1], zorder=4)

ax.set_ylim(0, 1550)
ax.set_ylabel('Bytes', fontsize=11, color='#222')
ax.set_xlabel('Message', fontsize=11, color='#222')
ax.set_xticks(x); ax.set_xticklabels(groups, fontsize=11, color='#222')
ax.tick_params(axis='y', labelsize=9, colors='#444')
ax.tick_params(axis='x', length=0)

ax.set_axisbelow(True)
ax.yaxis.grid(True, color='#ececec', lw=0.9, zorder=0)
for s in ('top', 'right'):
    ax.spines[s].set_visible(False)
for s in ('left', 'bottom'):
    ax.spines[s].set_color('#999'); ax.spines[s].set_linewidth(1.0)

ax.legend(frameon=False, fontsize=10, loc='lower center',
          bbox_to_anchor=(0.5, 1.01), ncol=2, handlelength=1.3,
          columnspacing=2.0, handletextpad=0.6)

# dashed rounded figure-level frame, matching the box-diagram figures
fig.add_artist(FancyBboxPatch((0.018, 0.03), 0.966, 0.94,
               boxstyle="round,pad=0,rounding_size=0.02",
               transform=fig.transFigure, fc='none', ec='#444',
               lw=1.3, ls=(0, (6, 4)), clip_on=False))

fig.savefig(OUT, dpi=300, facecolor='white')
plt.close(fig)
print('wrote', os.path.normpath(OUT))
