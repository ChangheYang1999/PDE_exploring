"""Map of the normalized residual near the source P on an export (lead diagnostic).
Usage: python3 map.py fields.npz"""
import sys
import numpy as np
d = np.load(sys.argv[1])
r, th = d['r'], d['theta']
sel = (r > 0.5) & (r < 30)
x, y = d['x'][sel], d['y'][sel]
R, den, rho = d['residual'][sel], d['denominator'][sel], d['rho'][sel]
ax, aw = d['axis_x'], d['axis_w']
from scipy.optimize import brentq
xs = brentq(lambda t: np.interp(t, ax, aw), 1.0, 30.0)
q = np.abs(R / den)
print('x*', xs, 'max |R/den| on 0.5<r<30:', q.max())
i = np.unravel_index(np.argmax(q), q.shape)
print('at x, y =', x[i], y[i], ' x-x* =', x[i] - xs)
# coarse cell table in (x - x*, y)
xe = np.array([-8.6, -6, -4, -2, -1, -0.5, -0.2, 0, 0.2, 0.5, 1, 2, 4, 8, 20])
ye = np.array([0, 0.05, 0.1, 0.2, 0.5, 1, 2, 4, 8, 20])
print('rows: y bins; cols: x - x* bins; entries max |R/den| x 1e6')
print('        ' + ' '.join(f'{a:>6.1f}' for a in xe[:-1]))
for j in range(len(ye) - 1):
    row = []
    for k in range(len(xe) - 1):
        m = (x - xs >= xe[k]) & (x - xs < xe[k + 1]) & (y >= ye[j]) & (y < ye[j + 1])
        row.append(q[m].max() * 1e6 if m.any() else np.nan)
    print(f'{ye[j]:5.2f}-{ye[j+1]:<5.2f}' + ' '.join(f'{v:6.1f}' for v in row))
qr = np.abs(R / np.where(np.abs(rho) > 0, rho, np.nan))
print('R/rho (relative) cell table x 1e6')
for j in range(len(ye) - 1):
    row = []
    for k in range(len(xe) - 1):
        m = (x - xs >= xe[k]) & (x - xs < xe[k + 1]) & (y >= ye[j]) & (y < ye[j + 1]) & np.isfinite(qr)
        row.append(np.nanmax(qr[m]) * 1e6 if m.any() else np.nan)
    print(f'{ye[j]:5.2f}-{ye[j+1]:<5.2f}' + ' '.join(f'{v:6.1f}' for v in row))
