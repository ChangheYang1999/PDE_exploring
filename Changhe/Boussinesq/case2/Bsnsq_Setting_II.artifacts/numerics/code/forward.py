"""Forward (characteristics) formulation for Setting A2, beta > 2.
Given a velocity evaluator W(X) = beta X + U(X) (U from Psi modes on a fine radial grid, see charcheck.build/evalW),
the source P = (x*, 0) is the first zero of W1 on the x-axis. Theta and Omega are determined by their Taylor data at P:
  Theta = g* y + (higher orders fixed by the recursion),  Omega = (unique bounded local solution), 
and transported along characteristics:  dX/ds = W,  dTheta/ds = (beta-2) Theta,  d(grad Theta)/ds = -(grad W)^T grad Theta
+ (beta-2) grad Theta,  dOmega/ds = -Omega + Theta_x.  Backward integration from targets to a circle |X-P| = eps.
This is independent of any spectral basis and makes no far-field assumption.
"""
import sys, math, numpy as np
sys.path.insert(0, 'code')
from charcheck import build, evalW, find_xstar


def gradW(B, x, y, h=1e-6):
    """finite-difference Jacobian of W at points (x,y): returns W1x, W1y, W2x, W2y"""
    hx = h * np.maximum(1.0, np.abs(x) + np.abs(y))
    op = evalW(B, x + hx, y); om = evalW(B, x - hx, y)
    W1x = (op['W1'] - om['W1']) / (2 * hx); W2x = (op['W2'] - om['W2']) / (2 * hx)
    op = evalW(B, x, y + hx); om = evalW(B, x, y - hx)
    W1y = (op['W1'] - om['W1']) / (2 * hx); W2y = (op['W2'] - om['W2']) / (2 * hx)
    return W1x, W1y, W2x, W2y


def taylor_W(B, xs, order=3, h=None):
    """Taylor coefficients of W1, W2 at P=(xs,0) up to total degree `order` by least-squares fit on a stencil.
    Returns dict {(m,n): (c1, c2)} with W_i ~ sum c_i[m,n] (x-xs)^m y^n."""
    h = h or 0.02 * xs
    pts = []
    for i in range(-3, 4):
        for j in range(-3, 4):
            pts.append((xs + i * h / 3, j * h / 3))
    pts = np.array(pts); x, y = pts[:, 0], pts[:, 1]
    o = evalW(B, x, y)
    mons = [(m, n) for m in range(order + 1) for n in range(order + 1) if m + n <= order]
    A = np.stack([(x - xs) ** m * y ** n for m, n in mons], 1)
    c1 = np.linalg.lstsq(A, o['W1'], rcond=None)[0]; c2 = np.linalg.lstsq(A, o['W2'], rcond=None)[0]
    return {mn: (c1[i], c2[i]) for i, mn in enumerate(mons)}


def local_solution(B, xs, gstar, order=3):
    """Taylor coefficients of Theta and Omega at P solving (T),(V) order by order, Theta_1 = g* y.
    Returns dicts theta[(m,n)], omega[(m,n)] for m+n <= order (Theta) and m+n <= order-1 (Omega)."""
    beta = B['beta']
    cW = taylor_W(B, xs, order)
    # polynomial helpers: dict (m,n)->coef
    def mul(p, q):
        r = {}
        for (a, b), u in p.items():
            for (c, d), v in q.items():
                r[(a + c, b + d)] = r.get((a + c, b + d), 0.0) + u * v
        return r
    def dx(p): return {(m - 1, n): m * u for (m, n), u in p.items() if m > 0}
    def dy(p): return {(m, n - 1): n * u for (m, n), u in p.items() if n > 0}
    def deg(p, d): return {mn: u for mn, u in p.items() if sum(mn) == d}
    W1 = {mn: c[0] for mn, c in cW.items() if abs(c[0]) > 0}; W2 = {mn: c[1] for mn, c in cW.items() if abs(c[1]) > 0}
    lam = cW[(1, 0)][0]; mu2 = cW[(0, 1)][1]
    theta = {(0, 1): gstar}
    for d in range(2, order + 1):
        # (A xi).grad Theta_d - (beta-2) Theta_d = -[ (W - A xi).grad Theta ]_d
        rhs = {}
        full = mul(W1, dx(theta)); full2 = mul(W2, dy(theta))
        for p in (full, full2):
            for mn, u in deg(p, d).items(): rhs[mn] = rhs.get(mn, 0.0) + u
        # subtract the linear-part contribution of degree d, which involves Theta_d itself (unknown): handle by solving
        # diagonal system: coefficient of x^m y^n in (A xi).grad Theta_d is (m lam + n mu2) theta_mn
        for (m, n) in [(m, d - m) for m in range(d + 1)]:
            lin = (m * lam + n * mu2) - (beta - 2)
            r = -(rhs.get((m, n), 0.0))      # rhs contains only lower-order theta (theta_d not yet in dict)
            if abs(lin) < 1e-10:
                theta[(m, n)] = 0.0
            else:
                theta[(m, n)] = r / lin
    # Omega: (A xi).grad Omega_d + Omega_d = [Theta_x]_d - [(W - A xi).grad Omega]_d
    omega = {}
    Tx = dx(theta)
    for d in range(0, order):
        rhs = {}
        full = mul(W1, dx(omega)); full2 = mul(W2, dy(omega))
        for p in (full, full2):
            for mn, u in deg(p, d).items(): rhs[mn] = rhs.get(mn, 0.0) + u
        for (m, n) in [(m, d - m) for m in range(d + 1)]:
            lin = (m * lam + n * mu2) + 1.0
            omega[(m, n)] = (Tx.get((m, n), 0.0) - rhs.get((m, n), 0.0)) / lin
    return theta, omega, cW


def eval_poly(p, X, Y):
    out = np.zeros_like(X)
    for (m, n), u in p.items(): out = out + u * X ** m * Y ** n
    return out


def transport_from_source(B, xs, gstar, targets, eps=None, order=3, dt_max=0.02, max_steps=6000, loc=None,
                          need_grad=True):
    """Backward characteristics from targets to the circle |X-P| = eps (RK4, vectorized over targets), storing
    position, step and grad W per step; then Theta, grad Theta and Omega are integrated forward along the stored
    path (midpoint rule for the linear system). Returns Theta, Theta_x, Theta_y, Omega at the targets."""
    beta = B['beta']; eps = eps or 0.01 * xs
    theta_c, omega_c, cW = loc if loc is not None else local_solution(B, xs, gstar, order)
    X = targets[:, 0].copy(); Y = targets[:, 1].copy(); n = len(X)
    s_acc = np.zeros(n); active = np.ones(n, bool); steps = np.zeros(n, int)
    # per-step records: arrays over all targets (inactive ones get dt = 0)
    rec_x, rec_y, rec_dt, rec_J = [], [], [], []
    def rhs(x, y):
        o = evalW(B, x, y); return -o['W1'], -o['W2']
    for it in range(max_steps):
        if not active.any(): break
        ia = np.where(active)[0]; x, y = X[ia], Y[ia]
        o = evalW(B, x, y)
        dist = np.sqrt((x - xs) ** 2 + y ** 2); speed = np.hypot(o['W1'], o['W2']) + 1e-300
        dt = np.minimum(dt_max, 0.02 * dist / speed)
        k1x, k1y = -o['W1'], -o['W2']
        k2x, k2y = rhs(x + 0.5 * dt * k1x, y + 0.5 * dt * k1y)
        k3x, k3y = rhs(x + 0.5 * dt * k2x, y + 0.5 * dt * k2y)
        k4x, k4y = rhs(x + dt * k3x, y + dt * k3y)
        xn = x + dt * (k1x + 2 * k2x + 2 * k3x + k4x) / 6; yn = y + dt * (k1y + 2 * k2y + 2 * k3y + k4y) / 6
        # record midpoint position and grad W there (for the forward linear integration)
        xm, ym = 0.5 * (x + xn), 0.5 * (y + yn)
        J = gradW(B, xm, ym) if need_grad else (0, 0, 0, 0)
        fx = np.zeros(n); fy = np.zeros(n); fdt = np.zeros(n); fJ = np.zeros((4, n))
        fx[ia] = xm; fy[ia] = ym; fdt[ia] = dt
        if need_grad:
            for q in range(4): fJ[q, ia] = J[q]
        rec_x.append(fx); rec_y.append(fy); rec_dt.append(fdt); rec_J.append(fJ)
        X[ia], Y[ia] = xn, yn; s_acc[ia] += dt; steps[ia] += 1
        done = (np.sqrt((xn - xs) ** 2 + yn ** 2) < eps) | (yn < 0) | (xn < 0)
        active[ia[done]] = False
    # forward integration along stored paths (reverse order), vectorized over targets
    Xh, Yh = X - xs, Y
    th = eval_poly(theta_c, Xh, Yh)
    tx = eval_poly({(m - 1, k): m * u for (m, k), u in theta_c.items() if m > 0}, Xh, Yh)
    ty = eval_poly({(m, k - 1): k * u for (m, k), u in theta_c.items() if k > 0}, Xh, Yh)
    om = eval_poly(omega_c, Xh, Yh)
    for i in range(len(rec_dt) - 1, -1, -1):
        dt = rec_dt[i]; J = rec_J[i]
        # exact integration of dTheta/ds = (beta-2) Theta over dt; midpoint (RK2) for the gradient and Omega
        def f(tx, ty, om, th):
            dtx = -(J[0] * tx + J[2] * ty) + (beta - 2) * tx
            dty = -(J[1] * tx + J[3] * ty) + (beta - 2) * ty
            dom = -om + tx
            return dtx, dty, dom
        d1 = f(tx, ty, om, th)
        txm, tym, omm = tx + 0.5 * dt * d1[0], ty + 0.5 * dt * d1[1], om + 0.5 * dt * d1[2]
        d2 = f(txm, tym, omm, th)
        tx, ty, om = tx + dt * d2[0], ty + dt * d2[1], om + dt * d2[2]
        th = th * np.exp((beta - 2) * dt)
    return dict(Theta=th, Theta_x=tx, Theta_y=ty, Omega=om, s=s_acc, finished=~active, steps=steps)


if __name__ == '__main__':
    from lm_solve import load_state
    d = load_state(sys.argv[1]); B = build(d)
    xs, lam = find_xstar(B)
    beta = B['beta']
    # g* from the state: Theta_y(x*,0) = x*^2 a(x*,0)
    o = evalW(B, np.array([xs]), np.array([1e-9]), need_fields=True); gstar = xs ** 2 * o['a'][0]
    theta_c, omega_c, cW = local_solution(B, xs, gstar, order=3)
    print(f"beta={beta} x*={xs:.6f} lambda={lam:.6f} (beta+2={beta+2}) g*={gstar:.6f}")
    print("W Taylor at P (m,n): W1, W2:", {k: (round(v[0], 5), round(v[1], 5)) for k, v in cW.items() if sum(k) <= 2})
    print("Theta local coefficients:", {k: round(v, 6) for k, v in theta_c.items() if abs(v) > 1e-12})
    print("Omega local coefficients:", {k: round(v, 6) for k, v in omega_c.items() if abs(v) > 1e-12})
    # compare with the state on a circle of radius 0.3 x* around P and at interior targets
    rt = np.geomspace(0.3, 30, 12); tt = np.linspace(0.1, np.pi / 2 - 0.1, 7)
    RR, TT = np.meshgrid(rt, tt, indexing='ij'); targets = np.stack([(RR * np.cos(TT)).ravel(), (RR * np.sin(TT)).ravel()], 1)
    res = transport_from_source(B, xs, gstar, targets, eps=0.01 * xs, order=3)
    ot = evalW(B, targets[:, 0], targets[:, 1], need_fields=True)
    rr = np.hypot(targets[:, 0], targets[:, 1]); fin = res['finished']
    relT = np.abs(res['Theta'] - ot['Theta']) / np.abs(ot['Theta']); relO = np.abs(res['Omega'] - ot['Omega']) / np.abs(ot['Omega'])
    relTx = np.abs(res['Theta_x'] - ot['Theta_x']) / (np.abs(ot['Theta_x']) + 1e-300)
    print(f"finished {fin.sum()}/{len(targets)}; max steps {res['steps'].max()}")
    for lo, hi in [(0, 1), (1, 5), (5, 15), (15, 40)]:
        mk = fin & (rr >= lo) & (rr < hi)
        if mk.any():
            print(f"  {lo:3d}<=r<{hi:3d}: Theta rel err med {np.median(relT[mk]):.2e} max {relT[mk].max():.2e} | Theta_x med {np.median(relTx[mk]):.2e} | Omega med {np.median(relO[mk]):.2e} max {relO[mk].max():.2e}")
