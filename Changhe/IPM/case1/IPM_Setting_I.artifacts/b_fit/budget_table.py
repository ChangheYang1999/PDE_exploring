"""Table of the fixed-density budget runs NAME_quadrature_*.json (run_budget.sh). Differences are relative to the
8192 x 480, R 10000, two-term run. Residual columns: pointwise maximum of |R|/den (construct4 normalization) per fixed
region (inner r <= 2, annulus 2 <= r <= 10, x_strip, y_strip, whole). Usage: python3 budget_table.py NAME"""
import json, sys
from pathlib import Path
import numpy as np
N = sys.argv[1]
runs = {}
for p in sorted(Path('.').glob(N + '_quadrature_*.json')):
    d = json.loads(p.read_text()); runs[(d['nr'], d['nt'], int(d['R_shape']), d['tail'])] = d
base = runs.get((8192, 480, 10000, 'two-term'))
regs = ('inner', 'annulus', 'x_strip', 'y_strip', 'whole')
print(f'# Fixed-density budget for {N}_shape.npz (no refit; L fixed)\n')
print('| nr | nt | R shape | tail | c_l (identity) | d c_l | x* | d x* | h(P) - 1 | max dw (5 axis samples) | '
      + ' | '.join(f'{r} pw' for r in regs) + ' |')
print('|' + '---|' * (10 + len(regs)))
for key in sorted(runs):
    d = runs[key]; q = d['roots_xaxis'][0]
    w = np.array(d['axis_velocity_samples']['w']) if 'axis_velocity_samples' in d else None
    if base is not None:
        qb = base['roots_xaxis'][0]; dcl = d['cl'] - base['cl']; dx = q['x'] - qb['x']
        dw = np.max(np.abs(w - np.array(base['axis_velocity_samples']['w']))) if w is not None else float('nan')
    else:
        dcl = dx = dw = float('nan')
    print(f"| {key[0]} | {key[1]} | {key[2]} | {key[3]} | {d['cl']:.9f} | {dcl:.2e} | {q['x']:.8f} | {dx:.2e} | "
          f"{q['mu2'] - 1:.2e} | {dw:.2e} | " + ' | '.join(f"{d['residuals'][r]['pointwise']:.3e}" for r in regs) + ' |')
