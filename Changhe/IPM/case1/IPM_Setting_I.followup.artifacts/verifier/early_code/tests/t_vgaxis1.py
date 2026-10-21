"""GreenAxis (Green quadrature, direct jets) against AxisData (collocation + ODE recursion) on X3: M_1 vs 2 c_int,
x*, w'(x*) - A, jets at x in [0.3, 8], and roughness of the jets in the origin layer."""
import sys, math, time, json
sys.path.insert(0, 'verifier/early_code')
import numpy as np
from numpy.polynomial import chebyshev as Ch
from vgen import Trial
from vaxis import AxisData
from vgaxis import GreenAxis
tr = Trial('../IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz', 'cuda')
hmax = float(sys.argv[1]) if len(sys.argv) > 1 else 0.05
qf = int(sys.argv[2]) if len(sys.argv) > 2 else 14
Nth = int(sys.argv[3]) if len(sys.argv) > 3 else 2048
t0 = time.time()
ga = GreenAxis(tr, K=6, Nth=Nth, hmax=hmax, qf=qf, xstar=8.600063792591499)
print('GreenAxis built %.1fs; panels %d targets %d' % (time.time() - t0, ga.P, len(ga.x)), flush=True)
M = ga.info['M']
print('M_n[phi]:', M[0])
print('consistency M_n[phi^(j)]/((2n)^j M_n) - 1:')
for j in range(1, M.shape[0]):
    print('  j=%d' % j, (M[j] / ((2 * np.arange(1, M.shape[1] + 1)) ** j * M[0]) - 1))
summ = json.loads(str(np.load('../data/x3_p12_h25_n2048_eval.npz', allow_pickle=True)['summary']))
print('M_1/2 = c: %.15f   c_int (collocation eval) %.15f  diff %.2e' % (M[0, 0] / 2, summ['c_int'], M[0, 0] / 2 - summ['c_int']))
print('tail M_1:', ga.info['M_tail'][0, 0])
# x* from the Green jets
xs = 8.600063792591499
for _ in range(4):
    wj = ga.jets_at(np.array([xs]))['w']
    xs = xs - wj[0, 0] / wj[1, 0]
wj = ga.jets_at(np.array([xs]))['w']
A = 2 * tr.c_l - 1
print('x* green %.13f (collocation 8.600063792591499); w1-A %.3e; w2 %.7f' % (xs, wj[1, 0] - A, 2 * wj[2, 0]))
ad = AxisData(tr, '../data/x3_p12_h25_n2048_eval.npz', Nth=2048, K=6, xstar=8.600063792591499)
xx = np.geomspace(0.3, 8.0, 7)
Wg = ga.jets_at(xx)['w']
Wc = ad.jets_at(xx)['w']
for i, x in enumerate(xx):
    print('x %.3f: rel diff per jet order' % x, ' '.join('%.1e' % (abs(Wg[k, i] - Wc[k, i]) / (abs(Wc[k, i]) + 1e-300)) for k in range(7)))
x = np.geomspace(3e-3, 0.3, 500)
s = (x / 0.3) ** 2
Wg = ga.jets_at(x)['w']
Wc = ad.jets_at(x)['w']
def rough(arr, lo, hi, deg=20):
    ch = Ch.Chebyshev.fit(s, arr, deg)
    m = (x >= lo) & (x < hi)
    return np.abs(arr - ch(s))[m].max()
for k in range(1, 7):
    print('jet %d (scaled by x^%d): green rough <0.01 %.1e 0.01-0.05 %.1e >0.05 %.1e | colloc %.1e %.1e %.1e' % (
        k, k - 1, rough(Wg[k] * x ** (k - 1), 0, .01), rough(Wg[k] * x ** (k - 1), .01, .05), rough(Wg[k] * x ** (k - 1), .05, 1),
        rough(Wc[k] * x ** (k - 1), 0, .01), rough(Wc[k] * x ** (k - 1), .01, .05), rough(Wc[k] * x ** (k - 1), .05, 1)))
np.savez('../data/t_vgaxis1.npz', x=x, Wg=Wg, Wc=Wc)
