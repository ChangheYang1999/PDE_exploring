"""Lead 15:48Z/16:00Z diagnostics.
 (AXQ) at each y-axis zero y1 of W2: nu = d_y W2(0,y1) vs -(3beta+2)/n; log-log slope of |Theta_xx(0,y)| = |2 y a(0,y)|
       against |y - y1| on both sides (exact smooth profile: integer n+2); second x-axis zeros: w'(x2) vs -(beta+2)/m.
 (T25) beta = 2: sup_{|X|=r} |U| against r (formal tail r^{1/2})."""
import sys, numpy as np
sys.path.insert(0, 'code')
from lm_solve import load_state
from charcheck import build, evalW
from scipy.optimize import brentq
for path in sys.argv[1:]:
    d = load_state(path); B = build(d, rmin=1e-3, rmax=1e5, nr=6000); beta = B['beta']
    print(f"=== {path}: beta={beta}")
    yy = np.geomspace(0.2, 3000, 4000); w2 = np.array([evalW(B, np.array([1e-10]), np.array([y]))['W2'][0] / y for y in yy])
    iz = np.where(np.diff(np.sign(w2)) != 0)[0]
    W2y = lambda y: evalW(B, np.array([1e-10]), np.array([y]))['W2'][0]
    for i in iz:
        y1 = brentq(lambda y: W2y(y) / y, yy[i], yy[i + 1], xtol=1e-12)
        h = 1e-5 * y1; nu = (W2y(y1 + h) - W2y(y1 - h)) / (2 * h)
        ns = np.arange(1, 13); allowed = -(3 * beta + 2) / ns
        n_best = ns[np.argmin(np.abs(allowed - nu))]
        # Theta_xx(0,y) = 2 y a(0,y): fit |Theta_xx| ~ |y-y1|^s on each side over |y-y1| in [1e-3, 3e-2] * y1
        out = [f"  y-axis zero y1={y1:.5f}: nu=d_yW2={nu:+.5f}; nearest allowed -(3beta+2)/n: n={n_best} -> {allowed[n_best-1]:+.4f} (others: " + ", ".join(f"{v:+.3f}" for v in allowed[:6]) + ")"]
        for side, sg in [('below', -1), ('above', +1)]:
            dy = y1 * np.geomspace(1e-3, 3e-2, 25); ys = y1 + sg * dy
            o = evalW(B, np.full_like(ys, 1e-10), ys, need_fields=True); Txx = np.abs(2 * ys * o['a'])
            sl = np.polyfit(np.log(dy), np.log(Txx + 1e-300), 1)[0]
            out.append(f"     |Theta_xx(0,y)| log-log slope vs |y-y1| ({side}): {sl:+.3f}  (exact smooth: integer n+2 = {n_best+2}); Theta_xx at |y-y1|=1e-3 y1: {Txx[0]:.3e}, at 3e-2 y1: {Txx[-1]:.3e}")
        print("\n".join(out))
    if len(iz) == 0: print("  no y-axis zero of W2")
    # second x-axis zeros
    xx = np.geomspace(0.2, 3000, 4000); w1 = np.array([evalW(B, np.array([x]), np.array([1e-10]))['W1'][0] / x for x in xx])
    ix = np.where(np.diff(np.sign(w1)) != 0)[0]
    W1x = lambda x: evalW(B, np.array([x]), np.array([1e-10]))['W1'][0]
    xz = [brentq(lambda x: W1x(x) / x, xx[i], xx[i + 1], xtol=1e-12) for i in ix]
    for k, x2 in enumerate(xz):
        h = 1e-5 * x2; wp = (W1x(x2 + h) - W1x(x2 - h)) / (2 * h)
        tag = "first root (exact: beta+2)" if k == 0 else f"later root (exact: beta+2 or -(beta+2)/m: " + ", ".join(f"{-(beta+2)/m:+.3f}" for m in range(1, 6)) + ")"
        print(f"  x-axis zero x{k+1}={x2:.5f}: W1'={wp:+.5f}  [{tag}]")
    if beta == 2.0:
        rr = np.geomspace(1, 3000, 25); th = np.linspace(1e-4, np.pi / 2 - 1e-4, 361)
        sup = []
        for r0 in rr:
            o = evalW(B, r0 * np.cos(th), r0 * np.sin(th)); sup.append(np.hypot(o['U1'], o['U2']).max())
        sup = np.array(sup); sl = np.diff(np.log(sup)) / np.diff(np.log(rr))
        print("  (T25) sup_{|X|=r}|U| vs r:  " + "  ".join(f"r={r0:.0f}:{s:.3e}" for r0, s in zip(rr[::3], sup[::3])))
        print(f"        local log-log slopes: {np.array2string(sl[::3], precision=2)}  (formal tail 1/2); global slope on r in [100,3000]: {np.polyfit(np.log(rr[rr>=100]), np.log(sup[rr>=100]), 1)[0]:+.3f}")
