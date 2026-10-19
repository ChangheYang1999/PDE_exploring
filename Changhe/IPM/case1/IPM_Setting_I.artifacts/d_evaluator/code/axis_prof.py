import sys, warnings
warnings.simplefilter("ignore")
import numpy as np
from snap_axis import snap_axis
from vb3 import find_xstar
d = np.load(sys.argv[1])
r, ms = d['r'], d['ms']
xs_list = [0.5, 1, 2, 3, 5, 8, 12, 20, 30, 50, 100, 300]
print('tau   x*    | G1 at x =', xs_list)
for i, tau in enumerate(d['tau']):
    ax, cl = snap_axis(d['F'][i], r, ms)
    x, G1, h, w = ax['x'], ax['G1'], ax['h'], ax['w']
    xs = find_xstar(x, w)
    sel = x < 1e3
    j = np.argmax(np.abs(G1[sel]))
    print('%.3f %6.2f | G1max %.3g at x=%.3g | h at max %.3f w %.3g | ' % (tau, xs or -1, G1[j], x[j], h[j], w[j]),
          ' '.join('%.3g' % np.interp(xx, x, G1) for xx in xs_list))
    print('      h:', ' '.join('%.3f' % np.interp(xx, x, h) for xx in xs_list))
