"""Containment test for certify_note14: cell enclosures (maxdepth 0, so the raw first/second-order rule is tested) vs brute-force float
midpoint integration on a fine subgrid. Regions: near (own kernel against f - f(e1) plus cross kernel against f) and m (k0 f)."""
import sys, numpy as np
sys.path.insert(0, '.')
import certify_note14 as CN, note14_float as NF
from structured_lb import make_Z0, K0 as K0f
from flint import arb, fmpq
from collections import Counter
aq, bq, cq, lq = (sys.argv[1:5] if len(sys.argv) > 4 else ('3/4', '3/4', '-3/10', '50/53'))
CN.setup(aq, bq, cq, lq); alpha = float(fmpq(aq)); b = float(fmpq(bq)); c = float(fmpq(cq)); lam = float(fmpq(lq))
Z = make_Z0(b)
def k0_cf(px, py):
    A = px*px + py*py; B = (px - 1)**2 + py*py; u = 1 - 2*px
    return u*(A*(3*py*py - px*px) - u*(px*px - py*py))/(2*np.pi*A*A*B*B)
def g_float(px, py, region):
    f = NF.f_note14(px, py, alpha, b, Z, c, lam)
    if region == 'near':
        return K0f(px - 1, py)*(f + 0.5) - K0f(px, py)*f
    return k0_cf(px, py)*f
def brute(center, r1, r2, th1, th2, region, n=400):
    lr = np.linspace(np.log(r1), np.log(r2), n + 1); lrc = 0.5*(lr[1:] + lr[:-1]); dlr = lr[1] - lr[0]
    th = np.linspace(th1, th2, n + 1); thc = 0.5*(th[1:] + th[:-1]); dth = th[1] - th[0]
    RR, TT = np.meshgrid(np.exp(lrc), thc, indexing='ij')
    px = center[0] + RR*np.cos(TT); py = center[1] + RR*np.sin(TT)
    return np.sum(g_float(px, py, region)*RR*RR)*dlr*dth
rng = np.random.default_rng(int(sys.argv[5]) if len(sys.argv) > 5 else 1)
fails = 0; tot = 0; cats = Counter(); skips = 0
for trial in range(int(sys.argv[6]) if len(sys.argv) > 6 else 300):
    kind = rng.choice(['near', 'near', 'm'])
    if kind == 'near':
        center = (1.0, 0.0); r1 = 10**rng.uniform(-3, np.log10(0.45)); dr = r1*rng.uniform(0.005, 0.05)
        th1 = rng.uniform(0, 2*np.pi); dth = rng.uniform(0.005, 0.05)
    else:
        center = (0.5, 0.0); r1 = 10**rng.uniform(0.0, 3); dr = r1*rng.uniform(0.005, 0.1)
        th1 = rng.uniform(0, 2*np.pi); dth = rng.uniform(0.005, 0.1)
    r2 = r1 + dr; th2 = th1 + dth
    cA = (arb(center[0]), arb(center[1]))
    CN.ERR.clear()
    try:
        val, n = CN.polar_value(cA, arb(r1), arb(r2), arb(th1), arb(th2), 0, 0, kind)
    except ValueError as e:
        skips += 1; continue
    for k in CN.ERR: cats[k] += 1
    bv = brute(center, r1, r2, th1, th2, kind)
    inside = val.contains(arb(bv)) or abs(float(val.mid()) - bv) <= float(val.rad())*1.0001 + 1e-12*abs(bv)
    tot += 1
    if not inside:
        fails += 1
        print(f"FAIL {kind} r1={r1:.3e} dr={dr:.2e} th1={th1:.3f} dth={dth:.3f} cat={list(CN.ERR)}: enclosure {val.str(8, radius=True)} brute {bv:.8e}")
print(f"alpha={aq} b={bq} c={cq} lam={lq}: containment failures {fails}/{tot} (skipped {skips}); categories {dict(cats)}")
