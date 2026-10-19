#!/usr/bin/env python3
"""R21 follow-up: is D_ax a jump of rho / x^2 across the WEAK axis as r -> 0?
For a saved exit-map state, K(r) = rho(r, theta just below the x-axis) / rho(r, theta just above) at theta = 0 and 180, for several
offsets (1, 2, 4, 8 cells and 5 degrees), as a function of r; compared with exp(D_ax) from the state's info (a_div form, D_ax = q(270) - q(90)).
Usage: python3 tests/pfwd_axis_kink.py state.npz
"""
import sys, json, math, numpy as np
d = np.load(sys.argv[1], allow_pickle=True)
g = d['g']; lr = d['lr']; th = d['th']; Nr, Nth = g.shape
args = json.loads(str(d['args'])); info = json.loads(str(d['info']))
p = float(args['p']); D = info.get('D_ax'); Ddir = info.get('D_ax_dir')
r = np.exp(lr); rho = (r[:, None] ** p) * g
thd = th * 180 / math.pi
dth = 360.0 / Nth
j0 = int(np.argmin(np.abs(thd))); j180 = int(np.argmin(np.abs(thd - 180)))
print(json.dumps(dict(file=sys.argv[1], Nth=Nth, p=p, D_ax=D, D_ax_dir=Ddir, expD=math.exp(D) if D is not None else None, theta0_grid=float(thd[j0]), dth_deg=dth)))
offs = [1, 2, 4, 8, int(round(5.0 / dth))]
print('ratio rho(below) / rho(above) across the weak axis; expected exp(D_ax) = %.4f if D_ax is the jump (sign convention: below = toward 270 side)' % (math.exp(D)))
print('lr      r         ' + ' '.join(['axis0 off%-3d' % o for o in offs]) + ' | ' + ' '.join(['axis180 off%-3d' % o for o in offs]))
for lrv in [-13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0]:
    i = int(np.argmin(np.abs(lr - lrv)))
    row = []
    for o in offs:
        above = rho[i, (j0 + o) % Nth]; below = rho[i, (j0 - o) % Nth]
        row.append(below / above if above != 0 else float('nan'))
    row2 = []
    for o in offs:
        above = rho[i, (j180 - o) % Nth]; below = rho[i, (j180 + o) % Nth]   # above the negative x-axis = theta slightly less than 180
        row2.append(below / above if above != 0 else float('nan'))
    print('%5.1f  %9.2e  ' % (lr[i], r[i]) + ' '.join(['%12.4f' % v for v in row]) + ' | ' + ' '.join(['%14.4f' % v for v in row2]))
# also the angular profile of rho / (r^2 cos^2 th) near the axis at lr = -12 and -6 (does it look like a step?)
for lrv in (-12, -9, -6):
    i = int(np.argmin(np.abs(lr - lrv)))
    js = [(j0 + k) % Nth for k in range(-6, 7)]
    vals = rho[i, js] / (r[i] ** 2 * np.cos(th[js]) ** 2)
    print('lr %5.1f  rho/(r^2 cos^2) at theta = %s deg:' % (lr[i], ', '.join(['%.2f' % thd[j] if thd[j] <= 180 else '%.2f' % (thd[j] - 360) for j in js])))
    print('          ' + ' '.join(['%.5g' % v for v in vals]))
