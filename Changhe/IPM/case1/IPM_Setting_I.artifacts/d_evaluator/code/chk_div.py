import sys, warnings
warnings.simplefilter("ignore")
import numpy as np
from snap_axis import snap_axis
from vb3 import find_xstar, local_fit
from vpolar import LogGrid
d = np.load(sys.argv[1])
r, ms = d['r'], d['ms']
g = LogGrid(len(r), r[0], r[-1])
for i in [0, 1, 2, 4]:
    ax, cl = snap_axis(d['F'][i], r, ms)
    x, w, h = ax['x'], ax['w'], ax['h']
    wp = g.du(w[:, None])[:, 0] / x
    xs = find_xstar(x, w)
    j = np.searchsorted(x, xs)
    sl = slice(j - 6, j + 7)
    print('tau %.2f cl %.5f x* %.4f' % (d['tau'][i], cl, xs))
    print('  max|wp+h-2cl| on x<100: %.2e' % np.abs((wp + h - 2 * cl)[x < 100]).max())
    print('  w near x*:', ' '.join('%.4f' % v for v in w[sl]))
    print('  wp near x*:', ' '.join('%.4f' % v for v in wp[sl]))
    for half, deg in ((0.05, 4), (0.1, 4), (0.02, 2), (0.1, 6)):
        print('   fit half %.2f deg %d: mu1 %.4f  h %.4f' % (half, deg, local_fit(x, w, xs, half * xs, deg).deriv()(0.0), local_fit(x, h, xs, half * xs, deg)(0.0)))
    print('   interp wp(x*) %.4f h(x*) %.4f' % (np.interp(xs, x, wp), np.interp(xs, x, h)))
