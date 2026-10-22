"""beta = 2: along the small-|W| locus P -> Q+: Theta, Omega, det DW, tr DW; Theta at all zeros of W in the
closed quadrant (x-axis P, y-axis zeros, interior Q+); far-field decay exponent of Omega; kinetic energy vs R."""
import sys, numpy as np
sys.path.insert(0, 'code')
from lm_solve import load_state
from charcheck import build, evalW, find_xstar
from forward import gradW
from scipy.optimize import minimize, brentq
for path in sys.argv[1:]:
    d = load_state(path); B = build(d, rmin=1e-3, rmax=1e4, nr=4000); beta = B['beta']
    xs, lam = find_xstar(B)
    print(f"=== {path}: beta={beta} P=({xs:.5f},0) W1'(P)={lam:.5f}")
    # locus: for each rho, angle of minimal |W| on the circle around P (restricted to the up-left sector 60..180 deg)
    ang = np.linspace(60, 180, 481) * np.pi / 180
    print("   rho   x        y        |W|/(beta rho)  Theta       Omega      det DW     tr DW")
    pts = []
    for rho in np.concatenate([np.linspace(0.1, 2, 8), np.linspace(2.5, 5.0, 6)]):
        X = xs + rho * np.cos(ang); Y = rho * np.sin(ang); ok = (X > 1e-6) & (Y > 1e-6)
        o = evalW(B, X[ok], Y[ok], need_fields=True); mag = np.hypot(o['W1'], o['W2']) / (beta * rho); i = np.argmin(mag)
        x0, y0 = X[ok][i], Y[ok][i]
        J = gradW(B, np.array([x0]), np.array([y0])); det = J[0][0] * J[3][0] - J[1][0] * J[2][0]; tr = J[0][0] + J[3][0]
        pts.append((x0, y0)); print(f"  {rho:5.2f} {x0:8.4f} {y0:8.4f}   {mag[i]:.3e}   {o['Theta'][i]:+.4e} {o['Omega'][i]:+.4e} {det:+.4f} {tr:+.4f}")
    # P itself
    J = gradW(B, np.array([xs]), np.array([1e-7])); print(f"  at P: det DW = {J[0][0]*J[3][0]-J[1][0]*J[2][0]:+.4f}, tr DW = {J[0][0]+J[3][0]:+.4f} (exact beta=2 profile: 0 and 4)")
    # interior minimum of |W|
    f = lambda p: float(np.hypot(evalW(B, np.array([p[0]]), np.array([p[1]]))['W1'][0], evalW(B, np.array([p[0]]), np.array([p[1]]))['W2'][0]))
    best = None
    for x0, y0 in pts[-4:] + [(9.5, 2.9), (8.9, 3.8)]:
        r = minimize(f, [x0, y0], method='Nelder-Mead', options=dict(xatol=1e-9, fatol=1e-13))
        if best is None or r.fun < best.fun: best = r
    o = evalW(B, np.array([best.x[0]]), np.array([best.x[1]]), need_fields=True)
    J = gradW(B, np.array([best.x[0]]), np.array([best.x[1]]))
    print(f"  Q+ = ({best.x[0]:.5f},{best.x[1]:.5f}): |W|={best.fun:.2e}, Theta={o['Theta'][0]:+.5e}, Omega={o['Omega'][0]:+.5e}, det DW={J[0][0]*J[3][0]-J[1][0]*J[2][0]:+.4f}, tr DW={J[0][0]+J[3][0]:+.4f}, grad Theta=({o['Theta_x'][0]:+.3e}, ?)")
    # all axis zeros and their Theta (Theta = 0 on both axes by parity): list y-axis zeros
    yy = np.geomspace(0.1, 3000, 2000); w2 = np.array([evalW(B, np.array([1e-9]), np.array([y]))['W2'][0] / y for y in yy])
    iz = np.where(np.diff(np.sign(w2)) != 0)[0]
    print(f"  y-axis zeros of W2/y: {[round(float(yy[i]), 3) for i in iz]} (Theta = 0 there by parity). Theta(P) = 0. Theta(Q+) = {o['Theta'][0]:+.4e}: no other zero of W shares it unless an interior one exists.")
    # far-field decay exponent of Omega: log-log slope of max_phi |Omega| on [50, 1000]
    rr = np.geomspace(50, 1000, 13); th = np.linspace(0.02, np.pi / 2 - 0.02, 180)
    mx = []
    for r0 in rr:
        o = evalW(B, r0 * np.cos(th), r0 * np.sin(th), need_fields=True); mx.append(np.abs(o['Omega']).max())
    mx = np.array(mx); slope = np.polyfit(np.log(rr), np.log(mx), 1)[0]
    loc = np.diff(np.log(mx)) / np.diff(np.log(rr))
    print(f"  far-field: max_phi|Omega| at r = 50..1000: slope (global fit) = {slope:+.4f}; local slopes {np.array2string(loc, precision=2)}; -1/beta = {-1/beta:.3f}, -2/beta = {-2/beta:.3f}")
    mxT = []
    for r0 in rr:
        o = evalW(B, r0 * np.cos(th), r0 * np.sin(th), need_fields=True); mxT.append(np.abs(o['Theta']).max())
    print(f"  far-field: max_phi|Theta| slope = {np.polyfit(np.log(rr), np.log(mxT), 1)[0]:+.4f} (formal 1 - 2/beta = {1-2/beta:.3f})")
    # kinetic energy int_{r<R} |U|^2 dA (full plane = 4 x quadrant), trapezoid in log r and theta
    rg = np.geomspace(1e-3, 3000, 600); thg = np.linspace(1e-4, np.pi / 2 - 1e-4, 200)
    R, TH = np.meshgrid(rg, thg, indexing='ij')
    o = evalW(B, (R * np.cos(TH)).ravel(), (R * np.sin(TH)).ravel())
    U2 = (o['U1'] ** 2 + o['U2'] ** 2).reshape(R.shape)
    inner_th = np.trapz(U2, thg, axis=1)                 # int |U|^2 dtheta
    integrand = inner_th * rg ** 2                        # r dr = r^2 d(log r)
    cum = np.concatenate([[0], np.cumsum(0.5 * (integrand[1:] + integrand[:-1]) * np.diff(np.log(rg)))]) * 4
    print("  kinetic energy 4 int_Q,r<R |U|^2 dA vs R:")
    for R0 in [1, 3, 10, 30, 100, 300, 1000, 3000]:
        print(f"     R={R0:6.0f}: E(R) = {np.interp(np.log(R0), np.log(rg), cum):.4e}")
    print(f"  local slope dlogE/dlogR between R = 300 and 3000: {(np.log(cum[-1]) - np.log(np.interp(np.log(300), np.log(rg), cum))) / np.log(10):+.3f} (|U| ~ r^{{1-1/beta}} gives slope {2*(1-1/beta)+2:.2f})")
