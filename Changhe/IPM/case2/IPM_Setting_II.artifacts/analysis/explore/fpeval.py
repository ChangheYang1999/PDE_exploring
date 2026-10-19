# Lead exploration (2026-10-17): evaluator for the forward fixed-point problem of Setting II.
# For a datum A(theta) = cos^2(theta) exp(F(theta)), F = sum_j a_j phi_j(theta), and p = 1/l, run the forward
# self-similar evolution d_s g = V.grad g + p (W_r/r) g (rho = r^p g, inflow g = A at r_max; same scheme as
# pforward.py) to a stationary state, then
#   m1     = weak eigenvalue of M = DV(0) (ring fit),
#   G(th)  = A(th) / A_new(th), A_new = |xi(r_max, th)|^(1/m1) / r_max^p from backward orbits (as in gfix.py).
# A Setting II profile (x-even exploration: F built from x-even modes) is a zero of
#   R(a, p) = ( m1 - 1/2 , <log G - mean, phi_j>_w , j = 1..N ),   w = cos^4(theta)
# (G constant and quadratic angular zeros force m1 = 1/2). Exploratory; nothing here is verified.
import sys, json, time
import numpy as np
from scipy.interpolate import RectBivariateSpline
sys.path.insert(0, 'explore')
import pforward as PF
import p0_forward2 as P2


def basis(th, N, kind='xeven'):
    """x-even modes (f(pi - th) = f(th)): sin th, cos 2th, sin 3th, cos 4th, ...; kind='full' adds the x-odd ones."""
    out = []
    for j in range(1, N + 1):
        out.append(np.sin(j * th) if j % 2 == 1 else np.cos(j * th))
    if kind == 'full':
        for j in range(1, N + 1):
            out.append(np.cos(j * th) if j % 2 == 1 else np.sin(j * th))
    return np.array(out)


def datum_fn(a, N, kind='xeven'):
    a = np.asarray(a, float)
    def A(th):
        return np.cos(th) ** 2 * np.exp(a @ basis(th, N, kind))
    return A


def evolve(p, Afun, g, lr, th, nsteps, ds=0.02, kring=20, tol=None):
    l = 1.0 / p
    Nr, Nth = g.shape
    drho = lr[1] - lr[0]; r = np.exp(lr); dth = 2 * np.pi / Nth
    dgn = np.nan
    for n in range(nsteps):
        rhoD = (r ** p)[:, None] * g
        wr, wt = PF.velocity_p(rhoD, lr, th, p)
        ar = l + wr / r[:, None]; at = wt / r[:, None]; src = p * wr / r[:, None]
        ci0 = np.arange(Nr)[:, None] + 0.5 * ds * ar / drho
        cj0 = np.arange(Nth)[None, :] + 0.5 * ds * at / dth
        arm = P2.interp_qm(ar, ci0, cj0, Nth); atm = P2.interp_qm(at, ci0, cj0, Nth)
        srm = P2.interp_qm(src, ci0, cj0, Nth)
        ci = np.arange(Nr)[:, None] + ds * arm / drho
        cj = np.arange(Nth)[None, :] + ds * atm / dth
        gn = P2.interp_qm(g, ci, cj, Nth) * np.exp(ds * srm)
        out = ci > Nr - 1
        if out.any():
            gn[out] = Afun(cj[out] * dth)
        dgn = np.max(np.abs(gn - g)) / ds
        g = gn
        if tol is not None and dgn < tol and n > 50:
            break
    return g, dict(steps=n + 1, dgds=float(dgn))


def node_and_G(p, Afun, g, lr, th, nA=1024, lr0=-9.0, dt=0.01, kring=20):
    l = 1.0 / p
    r = np.exp(lr)
    rhoD = (r ** p)[:, None] * g
    wr, wt = PF.velocity_p(rhoD, lr, th, p)
    ar = l + wr / r[:, None]; at = wt / r[:, None]
    M = PF.node_matrix(ar[kring], at[kring], th)
    ev, evec = np.linalg.eigh(0.5 * (M + M.T)); m1, m2 = ev
    e1 = evec[:, 0] * np.sign(evec[0, 0] if abs(evec[0, 0]) > 1e-12 else 1.0)
    pad = 8
    thx = np.concatenate([th[-pad:] - 2 * np.pi, th, th[:pad] + 2 * np.pi])
    ext = lambda F: np.concatenate([F[:, -pad:], F, F[:, :pad]], axis=1)
    Sr = RectBivariateSpline(lr, thx, ext(ar), kx=3, ky=3)
    St = RectBivariateSpline(lr, thx, ext(at), kx=3, ky=3)
    def rhs(x, t):
        tt = np.mod(t, 2 * np.pi)
        return -Sr.ev(x, tt), -St.ev(x, tt)
    thA = 2 * np.pi * np.arange(nA) / nA
    x = np.full(nA, lr[-1]); t = thA.copy(); T = np.zeros(nA); live = np.ones(nA, bool); it = 0
    while live.any() and it < 200000:
        xi, ti = x[live], t[live]
        k1 = rhs(xi, ti); k2 = rhs(xi + 0.5 * dt * k1[0], ti + 0.5 * dt * k1[1])
        k3 = rhs(xi + 0.5 * dt * k2[0], ti + 0.5 * dt * k2[1]); k4 = rhs(xi + dt * k3[0], ti + dt * k3[1])
        x[live] = xi + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        t[live] = ti + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        T[live] += dt
        live = live & (x > lr0); it += 1
    if live.any():
        print('node_and_G: WARNING %d orbits did not reach lr0 = %g (cap %d steps)' % (int(live.sum()), lr0, it), file=sys.stderr)
    X0 = np.exp(x)[:, None] * np.stack([np.cos(t), np.sin(t)], 1)
    u0 = X0 @ e1
    logAn = np.log(np.maximum(np.abs(u0), 1e-300)) / m1 + T - p * lr[-1]
    A_old = Afun(thA)
    logG = np.log(np.maximum(A_old, 1e-300)) - logAn
    return dict(m1=float(m1), m2=float(m2), e1=e1.tolist(), M=M.ravel().tolist(), thA=thA, logG=logG, A=A_old,
                logAn=logAn, Tmax=float(T.max()), sgn=np.sign(u0), nlive=int(live.sum()))


def residual(p, a, N, kind, ng, wpow=4, gmode='g'):
    # gmode 'g': log G = log A - log A_new (singular like (2 - 1/m1) log|Xi| at the zeros unless m1 = 1/2);
    # gmode 'gt': log Gt = log A - 2 log|Xi| = log A - 2 m1 log A_new (bounded at quadratic zeros; same zeros of R).
    thA = ng['thA']
    w = np.cos(thA) ** wpow
    lg = ng['logG'] if gmode == 'g' else np.log(np.maximum(ng['A'], 1e-300)) - 2 * ng['m1'] * ng['logAn']
    ok = np.isfinite(lg)
    w = np.where(ok, w, 0.0); lg = np.where(ok, lg, 0.0)
    mean = np.sum(w * lg) / np.sum(w)
    B = basis(thA, N, kind)
    proj = (B * (w * (lg - mean))[None, :]).sum(1) / np.sum(w)
    Gw = np.exp(lg - mean)
    sel = w > 1e-3
    return np.concatenate([[ng['m1'] - 0.5], proj]), dict(mean_logG=float(mean),
            G_ratio=float(Gw[sel].max() / Gw[sel].min()), wstd_logG=float(np.sqrt(np.sum(w * (lg - mean) ** 2) / np.sum(w))))


if __name__ == '__main__':
    # quick single evaluation: python3 fpeval.py restart.npz p N a1,a2,... [nsteps]
    st = np.load(sys.argv[1]); p = float(sys.argv[2]); N = int(sys.argv[3])
    a = np.array([float(v) for v in sys.argv[4].split(',')]) if len(sys.argv) > 4 and sys.argv[4] != '0' else np.zeros(N)
    nsteps = int(sys.argv[5]) if len(sys.argv) > 5 else 600
    Af = datum_fn(a, N)
    t0 = time.time()
    g, info = evolve(p, Af, st['g'], st['lr'], st['th'], nsteps)
    ng = node_and_G(p, Af, g, st['lr'], st['th'])
    R, diag = residual(p, a, N, 'xeven', ng)
    print(json.dumps(dict(p=p, a=a.tolist(), m1=ng['m1'], m2=ng['m2'], R=R.tolist(), diag=diag, info=info,
                          wall=round(time.time() - t0, 1))))
