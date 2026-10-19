"""B_3 with the verifier's integrator (vb3.b3) applied to the axis arrays exported by construct1, compared with the
coefficient of the singular basis term (diagnostics B3_ansatz). Also the closed-form w-only value (analysis 7.3) and the
hybrid function B3(x) = f.p. int_0^x J + G3(x)/H(x), which is constant iff the y^3 axis equation holds."""
import sys, json, numpy as np
from vb3 import b3
d = np.load(sys.argv[1])
dg = json.loads(str(d['diagnostics']))
x = d['axis_x']
ax = dict(x=x, w=d['axis_w'], h=d['axis_h'], G1=d['axis_G1'], G1p=d['axis_G1_prime'], G3=d['axis_G3'],
          W1_2=d['axis_A2'], W2_3=d['axis_B3W'])
ax['F3'] = -ax['W1_2'] * ax['G1p'] - ax['W2_3'] * ax['G1']
out = dict(file=sys.argv[1], B3_ansatz=dg['B3_ansatz'], p3_export=dg['p3'])
for tl, tc in ((0.01, 0.3), (0.02, 0.3), (0.01, 0.2), (0.005, 0.4)):
    o = b3(ax, t_lo_frac=tl, t_c_frac=tc)
    out['b3_%g_%g' % (tl, tc)] = dict(B3=o['B3'], hybrid=o['hybrid'], fit_err=o['fit_err'], p3=o['p3'])
# with finite-difference A2, B3W
ax2 = dict(ax)
ax2['W1_2'] = d['axis_A2_finite_difference']; ax2['W2_3'] = d['axis_B3W_finite_difference']
ax2['F3'] = -ax2['W1_2'] * ax2['G1p'] - ax2['W2_3'] * ax2['G1']
o = b3(ax2)
out['b3_fdA2'] = dict(B3=o['B3'], hybrid=o['hybrid'])
# H from h_eff = 1 - w G1'/G1 (the y-linear axis equation solved for h): differs from the h-based H by the y-linear defect
ax3 = dict(ax)
ax3['h'] = 1 - ax['w'] * ax['G1p'] / ax['G1']
o = b3(ax3)
out['b3_heff'] = dict(B3=o['B3'], hybrid=o['hybrid'], p3=o['p3'], kappa=o['kappa'])
# compatibility of the exported jets: a2 = (g' - w'')/2, a2' + 3 b3 = 0
from scipy.interpolate import CubicSpline
u = np.log(x)
wpp = CubicSpline(u, d['axis_w_prime'])(u, 1) / x
a2c = 0.5 * (ax['G1p'] - wpp)
sel = (x > 0.05) & (x < 0.95 * 8.6)
out['a2_compat_rel'] = float(np.abs(a2c - ax['W1_2'])[sel].max() / np.abs(ax['W1_2'][sel]).max())
a2p = CubicSpline(u, ax['W1_2'])(u, 1) / x
out['b3_compat_rel'] = float(np.abs(a2p + 3 * ax['W2_3'])[sel].max() / np.abs(3 * ax['W2_3'][sel]).max())
print(json.dumps(out, indent=1, default=float))
