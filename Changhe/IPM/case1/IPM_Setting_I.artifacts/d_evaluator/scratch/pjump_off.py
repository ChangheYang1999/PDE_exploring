"""H_xxx(x, y) profiles across the vertical through P at fixed heights y (verifier H evaluator, pjump.H_pts), physical units.
Prints H_xxx at xi = x - x* for each y, and the circle offset sqrt(x*^2 - y^2) - x* (where the radial knot cluster at r* sits).
Usage: python3 pjump_off.py shape.npz x_star y1,y2,..."""
import sys
import numpy as np
from pjump import H_pts, d3
d = np.load(sys.argv[1], allow_pickle=True); xs = float(sys.argv[2]); ys = [float(v) for v in sys.argv[3].split(',')]
h = 1e-3
XI = [-0.5, -0.3, -0.2, -0.13, -0.1, -0.06, -0.03, -0.02, -0.01, 0, 0.01, 0.02, 0.03, 0.06, 0.1, 0.13, 0.2, 0.3, 0.5]
print('xi      ' + ' '.join('%+7.3f' % v for v in XI))
for y in ys:
    x = xs + np.arange(-0.8, 0.8 + h / 2, h)
    H = H_pts(d, x, np.full(len(x), y)); g = d3(H, h); xg = x[3:-3]
    print('y %.2f  ' % y + ' '.join('%+7.3f' % np.interp(xs + v, xg, g) for v in XI) + '   circle %+.4f' % (np.sqrt(xs ** 2 - y ** 2) - xs))
