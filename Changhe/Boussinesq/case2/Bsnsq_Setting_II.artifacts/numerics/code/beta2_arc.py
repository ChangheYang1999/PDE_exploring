"""beta = 2: trace the locus of minimal |W|/(beta rho) on circles around P (fine), to see where the approximate
stagnation arc goes and ends."""
import sys, numpy as np
sys.path.insert(0, 'code')
from lm_solve import load_state
from charcheck import build, evalW, find_xstar
for path in sys.argv[1:]:
    d = load_state(path); B = build(d, rmin=1e-3, rmax=1e4, nr=4000); beta = B['beta']
    xs, lam = find_xstar(B)
    print(f"=== {path}: beta={beta} x*={xs:.5f} W1'(x*)={lam:.5f}")
    ang = np.linspace(60, 180, 481) * np.pi / 180
    print("   rho    angle(deg)   x        y        |W|/(beta rho)   Theta       Omega      a         G")
    for rho in np.concatenate([np.linspace(0.1, 2, 11), np.linspace(2.5, 10, 16)]):
        X = xs + rho * np.cos(ang); Y = rho * np.sin(ang); ok = (X > 1e-6) & (Y > 1e-6)
        o = evalW(B, X[ok], Y[ok], need_fields=True)
        mag = np.hypot(o['W1'], o['W2']) / (beta * rho); i = np.argmin(mag)
        print(f"  {rho:5.2f}  {ang[ok][i]*180/np.pi:8.2f}  {X[ok][i]:8.4f} {Y[ok][i]:8.4f}   {mag[i]:.3e}   {o['Theta'][i]:+.3e} {o['Omega'][i]:+.3e} {o['a'][i]:+.3e} {o['G'][i]:+.3e}")
    # local refinement of the interior near-stagnation point
    from scipy.optimize import minimize
    f = lambda p: float(np.hypot(*[v[0] for v in (evalW(B, np.array([p[0]]), np.array([p[1]]))[k] for k in ('W1', 'W2'))]))
    best = None
    for x0, y0 in [(9.5, 2.9), (10, 2.5), (9, 3.5)]:
        r = minimize(f, [x0, y0], method='Nelder-Mead', options=dict(xatol=1e-8, fatol=1e-12))
        if best is None or r.fun < best.fun: best = r
    o = evalW(B, np.array([best.x[0]]), np.array([best.x[1]]), need_fields=True)
    print(f"  interior minimum of |W|: at ({best.x[0]:.5f},{best.x[1]:.5f}) |W|={best.fun:.3e} (|W|/(beta r)={best.fun/(beta*np.hypot(*best.x)):.2e}); Theta={o['Theta'][0]:+.4e} Omega={o['Omega'][0]:+.4e}")
