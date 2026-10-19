"""Compare the axis velocity w/A of an export with a reference export (lead). Usage: python w_compare.py fields.npz ref.npz"""
import sys
import numpy as np
from scipy.interpolate import CubicSpline
out = []
for f in sys.argv[1:3]:
    z = np.load(f); x = z['axis_x']; sel = x < 40; cl = float(z['c_l']); A = 2 * cl - 1
    out.append((CubicSpline(x[sel] ** 2, z['axis_w'][sel] / x[sel] / A), cl))
(S, cl), (Sr, clr) = out
print(f'c_l {cl:.8f} vs ref {clr:.8f} (diff {cl - clr:.2e}); relative change of w/A at x = 0.01 0.05 0.15 0.5 1.5 4 8:')
print('  ' + ' '.join(f'{S(t * t) / Sr(t * t) - 1: .2e}' for t in (0.01, 0.05, 0.15, 0.5, 1.5, 4, 8)))
