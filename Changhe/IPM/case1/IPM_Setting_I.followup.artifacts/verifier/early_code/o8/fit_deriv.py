# Own quadrature (bnat.py, form (II), default panels) of b0 = B(e = 0), B_e = (B - b0)/e (B is affine in e), and the
# fixed-shape B_A, B_AA (central differences in A with w = (A/A0) w0, i.e. q -> (A/A0) q) on the fitted reference;
# compared with the fred23 certify.py enclosures.
import sys, json, time
from fractions import Fraction as Fr
sys.path.insert(0, 'verifier/early_code/xref_ver')
import mpmath as mp
from bnat import Ref, B_value
d = json.load(open('fred23/01-obstruction/data/fitted_reference.json'))
A0s = d['A0_exact']; qs = d['q_power_coefficients_exact_decimal']
mp.mp.dps = 40
e = 1/mp.mpf(d['L0_exact'])**2
def B(As, ee):
    sc = Fr(As)/Fr(A0s)
    q = ['%d/%d' % ((Fr(c)*sc).numerator, (Fr(c)*sc).denominator) for c in qs]
    t0 = time.time()
    R = Ref(As, ee, q, dps=40); R.series0(80)
    v, _ = B_value(R, 'II', mp.mpf('0.25'))
    print('  B(A = %s, e = %s) = %s (%.0fs)' % (As, mp.nstr(ee, 8), mp.nstr(v, 22), time.time() - t0), flush=True)
    return v
B0 = B(A0s, e); b0 = B(A0s, 0)
print('B = %s, b0 = %s, B_e = %s, mu0 = 1 - B/b0 = %s' % (mp.nstr(B0, 20), mp.nstr(b0, 20), mp.nstr((B0 - b0)/e, 16), mp.nstr(1 - B0/b0, 10)), flush=True)
h = mp.mpf('0.0001')
Bp = B('10.150825', e); Bm = B('10.150625', e)
print('B_A (central, h 1e-4) = %s; B_AA = %s; certify base enclosures B_A [-0.006701853437, -0.006171669738], B_e [-7.0946356, -6.9550237], B_AA [-0.0029305439, -0.0027685102]'
      % (mp.nstr((Bp - Bm)/(2*h), 12), mp.nstr((Bp - 2*B0 + Bm)/h**2, 8)), flush=True)
