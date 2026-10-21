"""Check of vaxis.AxisData on X3: jets of w against nodal w and its derivative; w'(x*) = A; smoothness of the
integrands near 0."""
import sys, math, time
sys.path.insert(0, 'verifier/early_code')
import numpy as np, torch
from vgen import Trial
from vaxis import AxisData, B3
t0 = time.time()
tr = Trial('../IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz', 'cuda')
ad = AxisData(tr, 'verifier/early_data/x3_p12_h25_n2048_eval.npz', Nth=2048, K=4)
print('axis panels', ad.P, 'points', len(ad.x), 'x*', ad.xs, 'time %.1f' % (time.time() - t0))
# compare w with panel interpolation of S1
S1n = (2 * ad.ns[None, :] * ad.psi).sum(1)
x = ad.x
S1 = ad.pan.interp(S1n, np.log(x), 0)
S1t = ad.pan.interp(S1n, np.log(x), 1)
w_direct = ad.c_l * x - S1 / x
wp_direct = ad.c_l - (S1t - S1) / x ** 2
W = ad.wj['w']
print('max |w_jet - w_direct| / max|w|', np.abs(W[0] - w_direct).max() / np.abs(w_direct).max())
print('max |w1_jet - w1_direct|', np.abs(W[1] - wp_direct).max())
# finite-difference check of w'' and w''' on the interpolant of w1 jets
for i in [0, len(x) // 3, len(x) // 2, len(x) - 30]:
    xi = x[i]; hh = 1e-4 * xi
    w1p = ad.interp('w', [xi + hh])[1]; w1m = ad.interp('w', [xi - hh])[1]
    w2p = ad.interp('w', [xi + hh])[2]; w2m = ad.interp('w', [xi - hh])[2]
    print('x %.4g: 2*w2 %.10e  fd(w1) %.10e ; 6*w3 %.8e fd(2 w2) %.8e' % (xi, 2 * W[2][i], (w1p - w1m)[0] / (2 * hh),
          6 * W[3][i], 2 * (w2p - w2m)[0] / (2 * hh)))
A = 2 * ad.c_l - 1
ws = ad.interp('w', [ad.xs])
print('w(x*)', ws[0], " w'(x*) - A", ws[1] - A, "  h(P)-1 =", 2 * ad.c_l - ws[1] - 1)
# near 0: w ~ -A x
for xi in [1e-4, 1e-3, 1e-2, 0.1, 1.0]:
    wi = ad.interp('w', [xi * 1.0001])
    print('x %.0e  w/x + A = %.3e   w1 + A = %.3e  w2 = %.3e' % (xi, wi[0][0] / (xi * 1.0001) + A, wi[1][0] + A, wi[2][0]))
b = B3(ad)
print('B3 init time %.1f' % (time.time() - t0))
xs = np.geomspace(2e-4, ad.xs * 0.999, 40)
I = b.integrands(xs)
for key in ['F1', 'F2b', 'F2a', 'ident']:
    print(key, ' '.join('%.3e' % v for v in (I[key] * xs ** (5 + b.be))[::3]))
print('T1', ' '.join('%.2e' % v for v in I['T1'][::3]))
print('gw/g -1', ' '.join('%.2e' % v for v in (I['gw'] / I['g'] - 1)[::3]))
np.save('verifier/early_data/t_vaxis1_xs.npy', xs)
