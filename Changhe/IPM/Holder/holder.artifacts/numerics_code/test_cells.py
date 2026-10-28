"""Containment test: enclosure of int_Q g from certify_lb (v2) vs brute-force float midpoint integration on a fine subgrid."""
import numpy as np, certify_lb as C
from flint import arb, fmpq
import structured_lb as S
C.setup(fmpq(1,2), fmpq(1,2)); alpha = 0.5; a = 0.5
Z = S.make_Z(a)
def g_float(px, py, cross_only):
    f = S.f_val(px, py, alpha, a, Z)
    return (-S.K(px, py)*f) if cross_only else (S.k_tot(px, py)*f)
def brute(center, r1, r2, th1, th2, cross_only, n=400):
    lr = np.linspace(np.log(r1), np.log(r2), n + 1); lrc = 0.5*(lr[1:] + lr[:-1]); dlr = lr[1] - lr[0]
    th = np.linspace(th1, th2, n + 1); thc = 0.5*(th[1:] + th[:-1]); dth = th[1] - th[0]
    RR, TT = np.meshgrid(np.exp(lrc), thc, indexing='ij')
    px = center[0] + RR*np.cos(TT); py = center[1] + RR*np.sin(TT)
    return np.sum(g_float(px, py, cross_only)*RR*RR)*dlr*dth
rng = np.random.default_rng(1)
fails = 0; tot = 0
for trial in range(60):
    kind = rng.choice(['near_full', 'near_cross', 'm'])
    if kind == 'near_full':
        center = (1.0, 0.0); r1 = rng.uniform(0.25, 0.45); dr = r1*rng.uniform(0.01, 0.05); cross = False
        th1 = rng.uniform(0, 2*np.pi); dth = rng.uniform(0.01, 0.05)
        dist_fn = C.near_dist_fn
    elif kind == 'near_cross':
        center = (1.0, 0.0); r1 = 10**rng.uniform(-5, -0.7); dr = r1*rng.uniform(0.02, 0.1); cross = True
        th1 = rng.uniform(0, 2*np.pi); dth = rng.uniform(0.02, 0.1)
        dist_fn = C.near_dist_fn
    else:
        center = (0.5, 0.0); r1 = 10**rng.uniform(0.05, 3); dr = r1*rng.uniform(0.01, 0.1); cross = False
        th1 = rng.uniform(0, 2*np.pi); dth = rng.uniform(0.01, 0.1)
        def dist_fn(cx_, cy_, rQ_, r1_, th1_, th2_):
            return C.lower_dist(cx_, cy_, rQ_, arb(1), arb(0)), C.lower_dist(cx_, cy_, rQ_, arb(0), arb(0))
    r2 = r1 + dr; th2 = th1 + dth
    cA = (arb(center[0]), arb(center[1]))
    try:
        val, n = C.polar_value(cA, arb(r1), arb(r2), arb(th1), arb(th2), 0, 2, cross, dist_fn)
    except ValueError as e:
        print("skip", kind, e); continue
    b = brute(center, r1, r2, th1, th2, cross)
    inside = val.contains(arb(b)) or abs(float(val.mid()) - b) <= float(val.rad())*1.0001 + 1e-12*abs(b)
    tot += 1
    if not inside:
        fails += 1
        print(f"FAIL {kind} r1={r1:.3e} dr={dr:.2e} th1={th1:.3f} dth={dth:.3f}: enclosure {val.str(8, radius=True)} brute {b:.8e}")
    elif trial < 12:
        print(f"ok   {kind:10s} enclosure {val.str(8, radius=True)}  brute {b:+.8e}  rel.width {float(val.rad())/max(abs(b),1e-300):.1e}")
print(f"containment failures: {fails}/{tot}")
