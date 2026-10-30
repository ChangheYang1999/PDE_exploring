# Uniform necessary bound of T4-007 for a general base rate mu0 (rate mu0 - 4800 s - 5 r/sqrt(s) > 0).
# Exact rational upper bounds for C1 r, C0 r using pi > 333/106, then applied to T4's saved Arb point triples.
import json
from fractions import Fraction as Fr
from flint import arb, ctx
ctx.prec = 256
PI_LO = Fr(333, 106)
def sqrt_up(q, n=60):
    # rational upper bound for sqrt(q) via Newton from above
    x = Fr(max(1, int(q) + 1))
    for _ in range(n):
        x = (x + q / x) / 2
        x = Fr(x.numerator * 10**30 // x.denominator + 1, 10**30)
    assert x * x >= q
    return x
def sqrt_lo(q):
    u = sqrt_up(q); l = q / u
    assert l * l <= q
    return l
def consts(mu0):
    smax = mu0 / 4800           # s < smax
    # r < mu0 sqrt(s)/5 ; C1 r < mu0/(5 sqrt(8 pi (1+s))) <= mu0/(5 sqrt(8 pi))
    c1r = mu0 / (5 * sqrt_lo(8 * PI_LO))
    # C0 r < mu0 sqrt(s)/(5*2 sqrt(pi)) <= mu0 sqrt(smax)/(10 sqrt(pi))
    c0r = mu0 * sqrt_up(smax) / (10 * sqrt_lo(PI_LO))
    return c1r, c0r, c1r * c0r
import os, sys
src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 't4_point_witnesses.json')
d = json.load(open(src))
for mu0 in (Fr(1, 10), Fr(297, 1000)):
    c1r, c0r, b = consts(mu0)
    print(f"mu0={mu0}: C1 r < {float(c1r):.6e} (1/{float(1/c1r):.2f}), C0 r < {float(c0r):.6e}, C0C1r^2 < {float(b):.3e}")
    for p in d['results']:
        f = arb(p['F_abs']); v = arb(p['V_norm']); g = arb(p['gradient_norm'])
        up = v * arb(c1r.numerator) / c1r.denominator + arb(c0r.numerator) / c0r.denominator * (1 + g) + arb(b.numerator) / b.denominator
        gap = f - up
        print(f"  {p['candidate']:12s} {str(p['point']):8s} |F|={float(f.mid()):.5f} |V|={float(v.mid()):.4f} |Drho|={float(g.mid()):.4f} gap={float(gap.mid()):+.5f} excl={bool(gap > 0)}")

# Specific closure ball of FW-T-TB-rebal-v1: s = 2^-16, r = 3*2^-15 (C1 r = 3*2^-7/sqrt(8 pi (1+s)), C0 r = r/(2 sqrt(pi(1+s))))
s = Fr(1, 2**16); r = Fr(3, 2**15)
c1r = r / sqrt_lo(8 * PI_LO * s * (1 + s)); c0r = r / (2 * sqrt_lo(PI_LO * (1 + s)))
print(f"FW-T-TB-rebal-v1 ball: C1 r < {float(c1r):.6e}, C0 r < {float(c0r):.6e}")
for p in d['results']:
    f = arb(p['F_abs']); v = arb(p['V_norm']); g = arb(p['gradient_norm'])
    up = v * arb(c1r.numerator) / c1r.denominator + arb(c0r.numerator) / c0r.denominator * (1 + g) + arb((c1r * c0r).numerator) / (c1r * c0r).denominator
    if f - up > 0:
        print(f"  excluded: {p['candidate']:12s} {str(p['point']):8s} gap={float((f - up).mid()):+.5f}")
# Largest mu0 (to 1e-3) for which each candidate keeps at least one uniform witness
for cand in ('C1-A2-d2', 'C1-A2-Mpen2', 'C1-A2-b6'):
    best = None
    for k in range(1, 1001):
        mu0 = Fr(k, 1000); c1r, c0r, b = consts(mu0)
        ok = False
        for p in d['results']:
            if p['candidate'] != cand: continue
            f = arb(p['F_abs']); v = arb(p['V_norm']); g = arb(p['gradient_norm'])
            up = v * arb(c1r.numerator) / c1r.denominator + arb(c0r.numerator) / c0r.denominator * (1 + g) + arb(b.numerator) / b.denominator
            if f - up > 0: ok = True; break
        if ok: best = mu0
        else: break
    print(f"{cand}: uniform witness survives for every base rate mu0 <= {best} (first failure at {float(best)+0.001:.3f})" if best else f"{cand}: none")
