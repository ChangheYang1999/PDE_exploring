"""Sharper certified far-field bound of sup_{r>=R} sup_theta |F| r^{-p_2}.
f(r, theta) := F r^{-p2} = sum_{(h,q), q<=Q} r^{alpha_hq - p2} E_hq(theta) + tail(r, theta), |tail| <= T(R) r^{...} (from farfield_F_cert pieces).
On s = log r in [log R, log R2] use a grid with step ds; at each grid point bound sup_theta |f| rigorously (grid + Bernstein in theta);
between grid points use |d f/ds| <= sum |alpha - p2| r^{alpha - p2} sup|E| (monotone decreasing in r) evaluated at the left end.
For r >= R2 use the crude additive bound (all sectors in absolute value), which is sharp as R2 -> infinity.
"""
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import numpy as np
from flint import arb, ctx
from farfield_bounds import sup_trig, A
import farfield_exact as FE

def sup_sum_trig(terms, M=20000):
    """terms: list of (coef arb, sine dict {k: Fraction}); rigorous sup_theta |sum coef * series| (arb).
    Float evaluation on M equispaced angles with an ADDITIVE proved rounding margin (as in farfield_bounds.sup_trig; repaired 14:38Z after the verifier's V211:
    the earlier multiplicative inflation did not control cancellation between large coefficients): with n float terms c_i = float(coef_i) float(v_ik),
    |float sum - exact sum| <= (2n + 4) 2^-53 sum|c_i| (products and additions, glibc sin within 1 ulp) + deg sum|c_i| 2^-50 (float angle error)
    + 2 * 2^-53 sum|c_i| (the two float conversions) + sum_i rad(coef_i) sum_k |v_ik| (the coefficient balls). Then the Bernstein inequality
    |T'| <= deg sup|T| gives sup <= (grid max + margin) / (1 - spacing deg / 2) with the spacing bound 2 pi / M (1 + 2^-40)."""
    th = np.linspace(0, 2*math.pi, M, endpoint=False)
    vals = np.zeros(M); deg = 0; csum = 0.0; ball = arb(0); n = 0
    for coef, S in terms:
        c = float(coef.mid()); rad = float(coef.rad())
        for k, v in S.items():
            cv = c*float(v); vals += cv*np.sin(k*th); deg = max(deg, k); csum += abs(cv); n += 1
        ball += arb(rad)*sum(abs(float(v)) for v in S.values())
    margin = arb((2*n + 4)*2.0**-53*csum + deg*csum*2.0**-50 + 2*2.0**-53*csum) + ball
    gmax = arb(float(np.abs(vals).max())) + margin
    spacing = 2*arb.pi()/M*(1 + arb(2)**-40)
    fac = 1 - spacing*deg/2
    assert fac > 0
    return gmax/fac

if __name__ == '__main__':
    d = json.load(open(sys.argv[1])); cl = Fr(d['cl']); a = [Fr(s) for s in d['a_canonical']]
    ctx.prec = 128
    Q = int(sys.argv[2]); R = float(sys.argv[3]); R2 = float(sys.argv[4]); ds = float(sys.argv[5])
    cert = json.load(open(os.environ.get('FARFIELD_F_CERT', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'farfield_F_cert_088.json'))))
    g = Fr(1)/cl; lam = 1-g; p2 = 2*g-1
    def alpha(h, q): return g - h*lam - 2*q
    X = FE.expand(cl, a, qmax=Q, hmax=7)
    secs = [((h, q), alpha(h, q) - p2, S) for (h, q), S in X['E'].items() if S]
    sups = {hq: sup_trig({('s', k): v for k, v in S.items()}) for (hq, e, S) in secs}
    # non-sector remainder at R (linear tail + cross + nonlinear tails from the cert file, which are decreasing in r)
    key = str(R) if str(R) in cert else None
    if key is None: raise SystemExit('run farfield_F_cert.py with this R first')
    rem = arb(cert[key]['linear_tail']) + arb(cert[key]['cross']) + arb(cert[key]['nonlinear_tails'])
    svals = np.arange(math.log(R), math.log(R2) + ds/2, ds)
    best = arb(0); argbest = None
    for s in svals:
        r = arb(s).exp()
        terms = [(r**A(e), S) for (hq, e, S) in secs]
        sup_here = sup_sum_trig(terms)
        # Lipschitz in s over [s, s+ds]: f' = sum e r^e E(theta) is itself a trig polynomial in theta for each r; bound sup|f'| at both
        # ends of the interval and add ds * (sum of sups of f'' terms) for the variation of f' in between (f'' = sum e^2 r^e E).
        r2 = (arb(s) + ds).exp()
        lip1 = sup_sum_trig([(A(e)*r**A(e), S) for (hq, e, S) in secs if e != 0])
        lip2 = sup_sum_trig([(A(e)*r2**A(e), S) for (hq, e, S) in secs if e != 0])
        curv = sum((A(e)*A(e)*r**A(e)*sups[hq] for (hq, e, S) in secs if e != 0), arb(0))
        lip = (lip1 if lip1 > lip2 else lip2) + curv*ds
        bound = sup_here + lip*ds + rem
        if bound > best: best = bound; argbest = float(s)
    # r >= R2: additive bound
    add = sum((sups[hq]*arb(R2)**A(e) for (hq, e, S) in secs), arb(0)) + rem
    final = best if best > add else add
    print('Q=%d, R=%g, R2=%g, ds=%g: sup_{r>=R} |F| r^-p2 <= %.6f  (grid part %.6f at log r = %.2f; r>=R2 additive %.6f; remainder %.2e; sup|E_1| = %.6f)' % (Q, R, R2, ds, float(final.upper()), float(best.upper()), argbest, float(add.upper()), float(rem), float(sups[(1, 0)])))
    out = json.load(open(os.environ.get('FARFIELD_F_CERT', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'farfield_F_cert_088.json'))))
    out['sharp_' + str(R)] = {'bound': float(final.upper()), 'R2': R2, 'ds': ds, 'Q': Q}
    json.dump(out, open(os.environ.get('FARFIELD_F_OUT', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'farfield_F_cert_088.json')), 'w'), indent=1)
