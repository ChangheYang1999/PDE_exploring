"""Signed normalized residual along rays theta = const near the source column (lead diagnostic).
Usage: python3 line.py fields.npz"""
import sys
import numpy as np
d = np.load(sys.argv[1])
r, th = d['r'], d['theta']
R, den = d['residual'], d['denominator']
for t in (0.1, 0.2, 0.3, 0.4, 0.5):
    j = np.argmin(abs(th - t))
    m = (r > 7) & (r < 11)
    v = R[m, j] / den[m, j]
    rr = r[m]
    # print sampled every few points plus sign changes count
    sc = np.sum(np.diff(np.sign(v)) != 0)
    print(f'theta {th[j]:.4f}: {m.sum()} pts in 7<r<11, sign changes {sc}, max|v| {abs(v).max():.2e} at r {rr[np.argmax(abs(v))]:.3f}')
    idx = np.linspace(0, len(rr) - 1, 25).astype(int)
    print('   ', ' '.join(f'{rr[i]:.2f}:{v[i]*1e6:+.1f}' for i in idx))
