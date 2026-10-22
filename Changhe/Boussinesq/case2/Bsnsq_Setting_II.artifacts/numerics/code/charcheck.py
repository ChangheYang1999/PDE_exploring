"""Characteristics-based transport consistency check of a saved LM state.
Independent of the collocation residuals: integrate backward characteristics of W = beta X + U (U from the state's
Psi modes, interpolated on a fine radial grid) from target points to a small circle around the x-axis source (x*,0),
then transport Theta (dTheta/ds = (beta-2) Theta) and Omega (dOmega/ds = -Omega + Theta_x) forward along the
characteristic and compare with the state's own Theta, Omega at the targets. For an exact solution the relative
discrepancy vanishes (up to ODE/interpolation error, ~1e-6 here)."""
import sys, numpy as np, torch, json
sys.path.insert(0, 'code')
from a2core import DT
from lm_solve import load_state, dev, make_model, rad_of_r
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq

def build(d, rmin=1e-3, rmax=1e5, nr=6000):
    N, M, L = int(d['N']), int(d['M']), float(d['L'])
    beta = float(d['beta']); mapname = str(d['mapname']) if 'mapname' in d else 'xi'
    beta_map = float(d['beta_map']) if 'beta_map' in d else beta
    rg = np.geomspace(rmin, rmax, nr)
    th = (np.arange(M) + 0.5) * np.pi / (2 * M)
    m0 = make_model(mapname, N, M, L, beta_map, float(d['sigma_a']), float(d['sigma_G']), np.array([0.0]), np.array([0.5]))
    rad = rad_of_r(m0, mapname, rg)
    m = make_model(mapname, N, M, L, beta_map, float(d['sigma_a']), float(d['sigma_G']), rad, th)
    ca = torch.tensor(d['ca'], dtype=DT, device=dev); cG = torch.tensor(d['cG'], dtype=DT, device=dev)
    f = m.fields(ca, cG, beta)
    C = np.cos(np.outer(th, 2 * np.arange(M)))
    alpha = np.linalg.solve(C, f['a'].cpu().numpy().T)      # [l, i]
    gamma = np.linalg.solve(C, f['G'].cpu().numpy().T)
    h = f['h'].cpu().numpy(); hd = f['hd'].cpu().numpy()      # [l, i], modes k = 2(l+1)
    u = np.log(rg)
    S = dict(alpha=[CubicSpline(u, alpha[l]) for l in range(M)], gamma=[CubicSpline(u, gamma[l]) for l in range(M)],
             h=[CubicSpline(u, h[l]) for l in range(M)], hd=[CubicSpline(u, hd[l]) for l in range(M)])
    return dict(S=S, M=M, beta=beta, rmin=rmin, rmax=rmax)

def evalW(B, x, y, need_fields=False):
    r = np.sqrt(x * x + y * y); th = np.arctan2(y, x); u = np.log(np.clip(r, B['rmin'], B['rmax']))
    M, beta = B['M'], B['beta']
    Psi_r = np.zeros_like(r); Psi_th = np.zeros_like(r)
    for l in range(M):
        k = 2 * (l + 1)
        Psi_r += B['S']['hd'][l](u) * np.sin(k * th); Psi_th += k * B['S']['h'][l](u) * np.cos(k * th)
    c, s = np.cos(th), np.sin(th)
    U1 = -(s * Psi_r + c * Psi_th / r); U2 = c * Psi_r - s * Psi_th / r
    out = dict(W1=beta * x + U1, W2=beta * y + U2, U1=U1, U2=U2)
    if need_fields:
        a = np.zeros_like(r); a_r = np.zeros_like(r); a_th = np.zeros_like(r); G = np.zeros_like(r)
        for l in range(M):
            al = B['S']['alpha'][l](u); dal = B['S']['alpha'][l](u, 1) / r
            a += al * np.cos(2 * l * th); a_r += dal * np.cos(2 * l * th); a_th += -2 * l * al * np.sin(2 * l * th)
            G += B['S']['gamma'][l](u) * np.cos(2 * l * th)
        a_x = c * a_r - s * a_th / r
        out.update(a=a, G=G, Theta=x * x * y * a, Omega=x * y * G, Theta_x=x * y * (2 * a + x * a_x))
    return out

def find_xstar(B):
    w1 = lambda x: evalW(B, np.array([x]), np.array([1e-12]))['W1'][0] / x
    xs = np.geomspace(0.05, 500, 400); v = np.array([w1(x) for x in xs])
    i = np.where(np.diff(np.sign(v)) != 0)[0]
    if len(i) == 0: return None, None
    x0 = brentq(w1, xs[i[0]], xs[i[0] + 1], xtol=1e-12)
    lam = (evalW(B, np.array([x0 * (1 + 1e-6)]), np.array([1e-12]))['W1'][0] - evalW(B, np.array([x0 * (1 - 1e-6)]), np.array([1e-12]))['W1'][0]) / (2e-6 * x0)
    return x0, lam

def transport_check(B, xs, targets, eps=0.02, dt_max=0.02, max_steps=40000):
    X = targets[:, 0].copy(); Y = targets[:, 1].copy(); n = len(X)
    s_acc = np.zeros(n); J = np.zeros(n); active = np.ones(n, bool); steps = np.zeros(n, int)
    P = np.array([xs, 0.0])
    def rhs(x, y):
        o = evalW(B, x, y); return -o['W1'], -o['W2']
    for it in range(max_steps):
        if not active.any(): break
        ia = np.where(active)[0]
        x, y = X[ia], Y[ia]
        o = evalW(B, x, y, need_fields=True)
        dist = np.sqrt((x - xs) ** 2 + y ** 2); speed = np.sqrt(o['W1'] ** 2 + o['W2'] ** 2) + 1e-300
        dt = np.minimum(dt_max, 0.02 * dist / speed)
        # RK4 for the backward flow dX/ds = -W
        k1x, k1y = -o['W1'], -o['W2']
        k2x, k2y = rhs(x + 0.5 * dt * k1x, y + 0.5 * dt * k1y)
        k3x, k3y = rhs(x + 0.5 * dt * k2x, y + 0.5 * dt * k2y)
        k4x, k4y = rhs(x + dt * k3x, y + dt * k3y)
        xn = x + dt * (k1x + 2 * k2x + 2 * k3x + k4x) / 6; yn = y + dt * (k1y + 2 * k2y + 2 * k3y + k4y) / 6
        # forward time tau decreases along the backward path; accumulate J = int e^{tau} Theta_x dtau with tau = -s_acc (target at tau=0)
        on = evalW(B, xn, yn, need_fields=True)
        tau0 = -s_acc[ia]; tau1 = -(s_acc[ia] + dt)
        J[ia] += 0.5 * dt * (np.exp(tau0) * o['Theta_x'] + np.exp(tau1) * on['Theta_x'])   # trapezoid
        X[ia], Y[ia] = xn, yn; s_acc[ia] += dt; steps[ia] += 1
        done = (np.sqrt((xn - xs) ** 2 + yn ** 2) < eps) | (yn < 0) | (xn < 0)
        active[ia[done]] = False
    o_hit = evalW(B, X, Y, need_fields=True); o_t = evalW(B, targets[:, 0], targets[:, 1], need_fields=True)
    beta = B['beta']
    # Theta(target) = Theta(hit) e^{(beta-2) s};  Omega(target) = e^{-s} Omega(hit) + int_{-s}^{0} e^{tau} Theta_x dtau
    Theta_pred = o_hit['Theta'] * np.exp((beta - 2) * s_acc)
    Omega_pred = np.exp(-s_acc) * o_hit['Omega'] + J
    return dict(X=X, Y=Y, s=s_acc, steps=steps, finished=~active, Theta_pred=Theta_pred, Theta=o_t['Theta'],
                Omega_pred=Omega_pred, Omega=o_t['Omega'], Theta_hit=o_hit['Theta'])

def yaxis_exponent(B, xs, ys=(2.0, 5.0, 10.0), xvals=None, eps=None):
    """Transport Omega (given W, Theta of the state) to points (x, y) with small x and fit
    Omega_pred/(x y) = A + C x^q : the N6(c) prediction is q = p - 1 = (2 beta + 1)/(beta + 2) (= 1.4 at beta 3)."""
    beta = B['beta']; q_pred = (2 * beta + 1) / (beta + 2)
    xvals = np.geomspace(0.01, 1.0, 12) if xvals is None else xvals
    eps = eps or 0.02 * xs
    print(f"  y-axis exponent test: predicted q = (2beta+1)/(beta+2) = {q_pred:.4f}")
    for y0 in ys:
        tg = np.stack([xvals, np.full_like(xvals, y0)], 1)
        res = transport_check(B, xs, tg, eps=eps, max_steps=200000)
        Gp = res['Omega_pred'] / (xvals * y0); Gs = res['Omega'] / (xvals * y0)
        # fit Gp = A + C x^q by least squares over q grid
        best = None
        for q in np.linspace(0.5, 3.0, 251):
            Amat = np.stack([np.ones_like(xvals), xvals ** q], 1)
            coef, resid, *_ = np.linalg.lstsq(Amat, Gp, rcond=None)
            r2 = np.sum((Amat @ coef - Gp) ** 2)
            if best is None or r2 < best[0]: best = (r2, q, coef)
        # also fit with q=2 (smooth) for comparison
        Amat2 = np.stack([np.ones_like(xvals), xvals ** 2], 1); c2, *_ = np.linalg.lstsq(Amat2, Gp, rcond=None)
        r2_2 = np.sum((Amat2 @ c2 - Gp) ** 2)
        print(f"   y={y0:5.2f}: finished {res['finished'].sum()}/{len(xvals)}; G_pred(x->0) ~ {best[2][0]:+.5f} + {best[2][1]:+.5f} x^{best[1]:.3f} (rss {best[0]:.2e}); smooth fit A+Cx^2 rss {r2_2:.2e}; state G(0.01,y)={Gs[0]:+.5f}")
        print("     x:      " + " ".join(f"{v:9.4f}" for v in xvals[::2]))
        print("     G_pred: " + " ".join(f"{v:9.5f}" for v in Gp[::2]))
        print("     G_state:" + " ".join(f"{v:9.5f}" for v in Gs[::2]))

if __name__ == '__main__':
    d = load_state(sys.argv[1]); B = build(d)
    xs, lam = find_xstar(B)
    print(f"state {sys.argv[1]}: beta={B['beta']:.6f}  x*={xs:.6f}  W1'(x*)={lam:.6f}  beta+2={B['beta']+2:.6f}  ratio={lam/(B['beta']+2):.5f}")
    rt = np.geomspace(0.3, 60, 16); tt = np.linspace(0.08, np.pi / 2 - 0.08, 11)
    RR, TT = np.meshgrid(rt, tt, indexing='ij'); targets = np.stack([(RR * np.cos(TT)).ravel(), (RR * np.sin(TT)).ravel()], 1)
    eps = float(sys.argv[2]) if len(sys.argv) > 2 else 0.02 * xs
    res = transport_check(B, xs, targets, eps=eps)
    fin = res['finished']
    relT = np.abs(res['Theta_pred'] - res['Theta']) / np.abs(res['Theta']); relO = np.abs(res['Omega_pred'] - res['Omega']) / np.abs(res['Omega'])
    print(f"targets {len(targets)}, finished {fin.sum()}, eps={eps:.4f}, max steps {res['steps'].max()}, max s {res['s'].max():.3f}")
    rr = np.sqrt(targets[:, 0] ** 2 + targets[:, 1] ** 2)
    for lo, hi in [(0, 1), (1, 5), (5, 15), (15, 30), (30, 100)]:
        mk = fin & (rr >= lo) & (rr < hi)
        if mk.any():
            print(f"  {lo:3d}<=r<{hi:3d}: n={mk.sum():3d}  Theta rel err median {np.median(relT[mk]):.3e} max {relT[mk].max():.3e} | Omega rel err median {np.median(relO[mk]):.3e} max {relO[mk].max():.3e}")
    # print a few lines of the grid
    print("  sample (r, th, Theta, Theta_pred, Omega, Omega_pred, s):")
    for i in np.linspace(0, len(targets) - 1, 12).astype(int):
        print(f"   r={rr[i]:7.3f} th={np.arctan2(targets[i,1], targets[i,0]):.3f}  Th={res['Theta'][i]:+.5e} pred={res['Theta_pred'][i]:+.5e}  Om={res['Omega'][i]:+.5e} pred={res['Omega_pred'][i]:+.5e}  s={res['s'][i]:.3f} fin={fin[i]}")
    yaxis_exponent(B, xs, eps=eps)
