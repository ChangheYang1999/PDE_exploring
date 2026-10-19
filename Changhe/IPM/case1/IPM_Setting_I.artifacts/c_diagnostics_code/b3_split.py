"""Check of the SPEC v4 D12 identity on an export (lead):
  f.p. B_3 from (w, h, a2, b3, g)  =  B_3 of the trial's own G3  +  f.p. int_0^{x*} D/(wH) dx,  D = T3 of the export.
Computes the left side and f.p. int D/(wH) with the b3_ls machinery (F3 replaced by -D), prints natural units, and the
difference (the trial's own B_3 implied by the exported G3), to compare with B3_ansatz from the export diagnostics.
Usage: python b3_split.py fields.npz"""
import sys, json
import numpy as np
sys.argv_saved = list(sys.argv)
import importlib.util
here = __file__.rsplit('/', 1)[0]
sys.path.insert(0, here)
from b3_diag import AxisData
spec = importlib.util.spec_from_file_location('b3ls', here + '/b3_ls.py')
# reuse helpers without running the b3_ls main loop: exec only the definitions
src = open(here + '/b3_ls.py').read().split("wf = odd(z['axis_w'])")[0]
ns = {'__file__': here + '/b3_ls.py'}
exec(src, ns)
z, odd, even, fp_ls, cl = ns['z'], ns['odd'], ns['even'], ns['fp_ls'], ns['cl']
from scipy.optimize import brentq
wf = odd(z['axis_w']); xs = brentq(wf, 1.0, 30.0)
hf, g1, g1p = even(z['axis_h']), even(z['axis_G1'], 2), odd(z['axis_G1_prime'])
G3, G3p = even(z['axis_G3'], 2), odd(z['axis_G3_prime'])
try:
    diag = json.loads(str(z['diagnostics']))
    b3a = diag.get('B3_ansatz')
except Exception:
    b3a = None
nat = xs ** (-4 - 2 / (2 * cl - 1))
print(f'{sys.argv[1]}: c_l {cl:.8f} x* {xs:.6f}; B3_ansatz (export) {b3a} -> natural {b3a / nat if b3a else float("nan"):.4f}')
for nm in ('', '_finite_difference'):
    a2, b3 = odd(z['axis_A2' + nm]), even(z['axis_B3W' + nm])
    d = AxisData(wf, hf, a2, b3, g1, g1p, cl, xs, ncheb=96)
    dD = AxisData(wf, hf, a2, b3, g1, g1p, cl, xs, ncheb=96)
    D = lambda t: wf(t) * G3p(t) + (3 * hf(t) - 1) * G3(t) + a2(t) * g1p(t) + b3(t) * g1(t)
    dD.F3 = lambda t: -D(t)
    tt = np.array([0.5, 2.0, 5.0, 8.0])
    scale = np.abs(wf(tt) * G3p(tt)) + np.abs((3 * hf(tt) - 1) * G3(tt)) + np.abs(a2(tt) * g1p(tt)) + np.abs(b3(tt) * g1(tt))
    print(f'  a2/b3 {nm or "solver"}: D/scale at x = 0.5, 2, 5, 8:', ' '.join(f'{v:.2e}' for v in D(tt) / scale))
    for delta in (0.4, 0.5):
        for deg in (10, 12, 14):
            tot = fp_ls(d, delta, deg)[0]
            dw = fp_ls(dD, delta, deg)[0]
            print(f'    delta {delta} deg {deg}: f.p. B_3 {tot: .4f}   f.p. int D/(wH) {dw: .4f}   difference (own B_3) {tot - dw: .4f}')
