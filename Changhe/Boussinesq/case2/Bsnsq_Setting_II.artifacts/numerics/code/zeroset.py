"""Zero-set, nodal-set and origin-exponent diagnostics of a saved state (analysis requests 14:37Z/14:52Z).
 (1) stagnation set of W in the closed first quadrant: grid search for |W| minima + fsolve refinement; axis zeros;
 (2) sign tables / nodal sets of Theta (via a) and Omega (via G) on r < 100;
 (3) K'_0 fit: G(x,0) - b0 = A x^2 + C x^q on 0 < x < 0.1 x*, q = (2 beta + 1)/(beta + 2); report C/b0 (state and transport)."""
import sys, numpy as np, torch
sys.path.insert(0, 'code')
from lm_solve import load_state, problem_from_state
from diag_state import eval_state
from scipy.optimize import fsolve, brentq

def main(path, do_transport=True):
    d = load_state(path); beta = float(d['beta']); N, M = int(d['N']), int(d['M'])
    print(f"=== {path}: N={N} M={M} beta={beta}", flush=True)
    from charcheck import build, evalW
    B = build(d, rmin=1e-3, rmax=1e4, nr=4000)
    # (1) stagnation set on a log-polar grid
    r = np.geomspace(0.05, 300, 260); th = np.linspace(0.0, np.pi / 2, 181)
    m, f = eval_state(d, r, th)
    W1 = f['W1'].cpu().numpy(); W2 = f['W2'].cpu().numpy(); X = f['x'].cpu().numpy(); Y = f['y'].cpu().numpy()
    a = f['a'].cpu().numpy(); G = f['G'].cpu().numpy()
    # axis zeros
    w1ax = f['w1'][:, 0].cpu().numpy(); w2ax = f['w2'][:, -1].cpu().numpy()
    zx = [float(brentq(lambda rr: np.interp(rr, r, w1ax), r[i], r[i + 1])) for i in np.where(np.diff(np.sign(w1ax)) != 0)[0]]
    zy = [float(brentq(lambda rr: np.interp(rr, r, w2ax), r[i], r[i + 1])) for i in np.where(np.diff(np.sign(w2ax)) != 0)[0]]
    print(f"  x-axis zeros of W1/x: {np.round(zx, 4)};  y-axis zeros of W2/y: {np.round(zy, 4)}")
    # interior candidates: cells where both W1 and W2 change sign
    s1 = np.sign(W1); s2 = np.sign(W2)
    cand = []
    for i in range(len(r) - 1):
        for j in range(1, len(th) - 2):
            c1 = (s1[i, j] != s1[i + 1, j]) or (s1[i, j] != s1[i, j + 1])
            c2 = (s2[i, j] != s2[i + 1, j]) or (s2[i, j] != s2[i, j + 1])
            if c1 and c2: cand.append((X[i, j], Y[i, j]))
    pts = []
    def Wfun(p):
        o = evalW(B, np.array([max(p[0], 1e-9)]), np.array([max(p[1], 1e-9)]))
        return [o['W1'][0], o['W2'][0]]
    for (x0, y0) in cand[:200]:
        sol, info, ier, msg = fsolve(Wfun, [x0, y0], full_output=True, xtol=1e-10)
        if ier == 1 and sol[0] > 1e-3 and sol[1] > 1e-3 and np.hypot(*Wfun(sol)) < 1e-8:
            if not any(np.hypot(sol[0] - p[0], sol[1] - p[1]) < 1e-3 for p in pts): pts.append((sol[0], sol[1]))
    print(f"  interior stagnation points (open quadrant, r<300): {[(round(p[0], 4), round(p[1], 4)) for p in pts]}  (candidate cells: {len(cand)})")
    for p in pts:
        o = evalW(B, np.array([p[0]]), np.array([p[1]]), need_fields=True)
        print(f"     at ({p[0]:.4f},{p[1]:.4f}): Theta={o['Theta'][0]:+.4e}  Omega={o['Omega'][0]:+.4e}  a={o['a'][0]:+.4e} G={o['G'][0]:+.4e}", flush=True)
    # (2) sign tables of a (= sign of Theta in Q) and G (= sign of Omega in Q)
    rs = np.geomspace(0.1, 100, 25); ths = np.linspace(0.05, np.pi / 2 - 0.05, 12)
    m2, f2 = eval_state(d, rs, ths)
    a2 = f2['a'].cpu().numpy(); G2 = f2['G'].cpu().numpy()
    def sgn(v): return '+' if v > 0 else '-'
    print("  sign of Theta (rows r, cols theta from 0.05 to pi/2-0.05):")
    for i in range(len(rs)): print(f"   r={rs[i]:8.3f} " + "".join(sgn(v) for v in a2[i]) + f"   min a={a2[i].min():+.2e}")
    print("  sign of Omega:")
    for i in range(len(rs)): print(f"   r={rs[i]:8.3f} " + "".join(sgn(v) for v in G2[i]) + f"   min G={G2[i].min():+.2e}")
    # innermost zero of Theta / Omega in Q
    neg_a = [(rs[i], ths[j]) for i in range(len(rs)) for j in range(len(ths)) if a2[i, j] < 0]
    neg_G = [(rs[i], ths[j]) for i in range(len(rs)) for j in range(len(ths)) if G2[i, j] < 0]
    print(f"  innermost negative Theta sample: {min(neg_a) if neg_a else None}; innermost negative Omega sample: {min(neg_G) if neg_G else None}")
    # (3) K'_0 fit on the x-axis: G(x,0) - b0 = A x^2 + C x^q
    xs = zx[0] if zx else 18.0
    q = (2 * beta + 1) / (beta + 2)
    xx = np.linspace(0.005 * xs, 0.1 * xs, 60)
    m3, f3 = eval_state(d, xx, np.array([1e-9]))
    Gx = f3['G'][:, 0].cpu().numpy(); b0 = float(f3['G0']) if 'G0' in f3 else Gx[0]
    m0, f0 = eval_state(d, np.array([1e-6]), np.array([1e-9])); b0 = f0['G'][0, 0].item()
    A = np.stack([xx ** 2, xx ** q], 1); coef = np.linalg.lstsq(A, Gx - b0, rcond=None)[0]
    A2 = np.stack([xx ** 2, xx ** 4], 1); coef2 = np.linalg.lstsq(A2, Gx - b0, rcond=None)[0]
    res1 = np.abs(A @ coef - (Gx - b0)).max(); res2 = np.abs(A2 @ coef2 - (Gx - b0)).max()
    print(f"  K'_0 fit (state G on the x-axis, 0.005x*<x<0.1x*, q={q:.4f}): C/b0 = {coef[1]/b0:+.4e} (A x^2 coeff {coef[0]:+.4e}; fit resid {res1:.1e}); smooth fit A x^2 + B x^4 resid {res2:.1e}")
    if do_transport:
        from charcheck import build, transport_check, find_xstar
        B = build(d); xsB, lam = find_xstar(B)
        tg = np.stack([xx, np.full_like(xx, 1e-6 * xs)], 1)
        res = transport_check(B, xsB, tg, eps=0.02 * xsB, max_steps=100000)
        Gp = res['Omega_pred'] / (tg[:, 0] * tg[:, 1])
        fin = res['finished']
        if fin.sum() > 10:
            coefp = np.linalg.lstsq(A[fin], Gp[fin] - b0, rcond=None)[0]
            print(f"  K'_0 fit (transported Omega along the x-axis, {fin.sum()} pts): C/b0 = {coefp[1]/b0:+.4e} (A x^2 coeff {coefp[0]:+.4e}); G_pred(x->0)={Gp[fin][0]:.5f} vs b0={b0:.5f}")
        else:
            print("  transport along the x-axis: too few finished characteristics")

if __name__ == '__main__':
    for p in sys.argv[1:]:
        main(p)
