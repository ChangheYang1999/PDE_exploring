"""
hs.py -- HYDROSTATIC profile problem (lead 08:04Z task HS; FINAL_REPORT 3.72, eps = 0 limit of large slopes).  Variables x = sqrt(a0) xi, rho = a0 g,
psi = sqrt(a0) Phi; the eps = 0 system is
    (c xi + V_1) g_xi + (c y + V_2) g_y = g,   -Phi_yy = g_xi,   g_y(0) = 1,   V = (-Phi_y, Phi_xi) sublinear,
with the explicit vertical-line inverse (y >= 0; V_1 even in y, V_2 odd in y):
    V_1(xi, y) = -int_y^inf g_xi(xi, t) dt,     V_2(xi, y) = int_0^y t g_xixi(xi, t) dt + y int_y^inf g_xixi(xi, t) dt.
This module: (1) a lean Cartesian evaluator of a Q-basis function g = y w(r) b(r, theta) (g, g_xi, g_y) with the parities, g_xixi by central differences;
(2) the hydrostatic inverse hydro_V for any callable (quadrature: Gauss-Legendre on [0, y]; tail t = y + Lt (u/(1-u))^q, q = 3, Lt = 1 + y, Gauss-Legendre
in u); (3) the manufactured test g = exp(-xi^2) y exp(-tau y^2): V_1 = xi exp(-xi^2) exp(-tau y^2)/tau, V_2 = -(1 - 2 xi^2) exp(-xi^2) sqrt(pi) erf(sqrt(tau) y)/(2 tau^(3/2)),
Phi_xiy(0) = -1/tau, div V = 0, d_y V_1 = g_xi.
"""
import sys, math, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import ipm3, ipm3s, ipm3q, ipm3ql
from ipm3 import interp_matrix
torch.set_default_dtype(torch.float64)


class GEval:
    """lean Cartesian evaluator of g = y w(t) sum_k b_k(t) cos 2k theta (Q basis, mode values b_k = sigma^k beta_k) at arbitrary points, with parities."""
    def __init__(self, mdl, beta):
        self.m = mdl; self.beta = beta; rad = mdl.rad
        self.bkR = (rad.sigR[:, None] ** mdl.kk[None, :]) * beta                      # mode values at the Radau nodes
        self.bkR_t = rad.DR @ self.bkR                                                 # exact t-derivative of the degree-N mode functions
    def __call__(self, X, Y):
        """returns g, g_x, g_y at Cartesian points (numpy arrays, any quadrant)."""
        X = np.asarray(X, dtype=np.float64); Y = np.asarray(Y, dtype=np.float64); shp = X.shape
        ax, ay = np.abs(X).reshape(-1), np.abs(Y).reshape(-1); sx = np.where(X.reshape(-1) < 0, -1.0, 1.0); sy = np.where(Y.reshape(-1) < 0, -1.0, 1.0)
        r = np.hypot(ax, ay); th = np.arctan2(ay, ax); rad, dev = self.m.rad, self.m.dev
        t = rad.t_of_r(np.maximum(r, 1e-300)); PR = torch.tensor(interp_matrix(rad.tR_np, t, rad.wR_np), device=dev)
        tt = torch.tensor(t, device=dev); tht = torch.tensor(th, device=dev); rr = torch.tensor(r, device=dev)
        Q = rad.Q(tt); g = (1 - tt ** 2) / Q; om = -(1 + tt) / Q; w = (1 - tt) / 2
        bk = PR @ self.bkR; bk_t = PR @ self.bkR_t; n = 2 * self.m.kk
        C = torch.cos(tht[:, None] * n[None, :]); S = torch.sin(tht[:, None] * n[None, :])
        b = (bk * C).sum(1); rb_r = g * (bk_t * C).sum(1); b_th = -(bk * n[None, :] * S).sum(1)
        cos, sin = torch.cos(tht), torch.sin(tht)
        P = sin * b; rP_r = sin * rb_r; P_th = cos * b + sin * b_th
        rho = rr * w * P; rho_r = w * ((1 + om) * P + rP_r); rho_th_r = w * P_th
        gx = cos * rho_r - sin * rho_th_r; gy = sin * rho_r + cos * rho_th_r
        rho = rho.cpu().numpy() * sy; gx = gx.cpu().numpy() * sx * sy; gy = gy.cpu().numpy()
        return rho.reshape(shp), gx.reshape(shp), gy.reshape(shp)


def hydro_V(gfun, X, Y, n_in=64, n_tail=200, q=3, hrel=1e-5, hstep='x'):
    """V_1, V_2 of the hydrostatic inverse at points (X, Y) for a callable gfun(X, Y) -> (g, g_x, g_y); g_xx by central differences in x with step
    hrel (1 + |x|) (hstep='x', the setting of all hsA..hsD runs) or hrel (1 + sqrt(x^2 + t^2)) (hstep='r': the step scales with the local length scale r, which
    removes the round-off floor of the fixed step where g is large, i.e. in the far field of the small-c states).  Returns V1, V2 (numpy, shape of X); V_1 even in y, V_2 odd in y."""
    X = np.asarray(X, dtype=np.float64); Y = np.asarray(Y, dtype=np.float64); shp = X.shape; x = X.reshape(-1); y = np.abs(Y.reshape(-1)); sy = np.where(Y.reshape(-1) < 0, -1.0, 1.0)
    npts = len(x)
    def gx_gxx(xx, tt):
        h = hrel * (1 + (np.hypot(xx, tt) if hstep == 'r' else np.abs(xx))); _, gxp, _ = gfun(xx + h, tt); _, gxm, _ = gfun(xx - h, tt); _, gx0, _ = gfun(xx, tt)
        return gx0, (gxp - gxm) / (2 * h)
    # inner integral int_0^y t g_xx dt (Gauss-Legendre on [0, y])
    ug, wg = np.polynomial.legendre.leggauss(n_in); ug = 0.5 * (ug + 1); wg = 0.5 * wg
    T_in = y[:, None] * ug[None, :]; W_in = y[:, None] * wg[None, :]
    _, gxx_in = gx_gxx(np.repeat(x[:, None], n_in, 1).reshape(-1), T_in.reshape(-1)); gxx_in = gxx_in.reshape(npts, n_in)
    I_in = (W_in * T_in * gxx_in).sum(1)
    # tail integrals int_y^inf g_x dt and int_y^inf g_xx dt with t = y + Lt (u/(1-u))^q
    ut, wt = np.polynomial.legendre.leggauss(n_tail); ut = 0.5 * (ut + 1); wt = 0.5 * wt
    Lt = 1.0 + y; s = (ut / (1 - ut)) ** q; ds = q * ut ** (q - 1) / (1 - ut) ** (q + 1)
    T_t = y[:, None] + Lt[:, None] * s[None, :]; W_t = Lt[:, None] * (wt * ds)[None, :]
    gx_t, gxx_t = gx_gxx(np.repeat(x[:, None], n_tail, 1).reshape(-1), T_t.reshape(-1)); gx_t = gx_t.reshape(npts, n_tail); gxx_t = gxx_t.reshape(npts, n_tail)
    J1 = (W_t * gx_t).sum(1); J2 = (W_t * gxx_t).sum(1)
    V1 = -J1; V2 = I_in + y * J2
    return V1.reshape(shp), (V2 * sy).reshape(shp)


def manufactured_test(tau=1.0, n_in=64, n_tail=200, q=3):
    from scipy.special import erf
    def gfun(X, Y):
        X = np.asarray(X, dtype=np.float64); Y = np.asarray(Y, dtype=np.float64)
        e = np.exp(-X ** 2) * np.exp(-tau * Y ** 2); g = e * Y; gx = -2 * X * g; gy = e * (1 - 2 * tau * Y ** 2)
        return g, gx, gy
    xs = np.array([0.0, 0.3, 0.7, 1.0, 1.5, 2.5]); ys = np.array([0.0, 0.2, 0.6, 1.0, 1.7, 3.0, 6.0]); XX, YY = np.meshgrid(xs, ys, indexing='ij')
    V1, V2 = hydro_V(gfun, XX, YY, n_in=n_in, n_tail=n_tail, q=q)
    V1e = XX * np.exp(-XX ** 2) * np.exp(-tau * YY ** 2) / tau
    V2e = -(1 - 2 * XX ** 2) * np.exp(-XX ** 2) * math.sqrt(math.pi) * erf(math.sqrt(tau) * YY) / (2 * tau ** 1.5)
    e1 = np.abs(V1 - V1e).max(); e2 = np.abs(V2 - V2e).max()
    # Phi_xiy(0) = d_xi(-V_1)(0,0) = -1/tau: central difference in xi at the origin
    h = 1e-4; V1p, _ = hydro_V(gfun, np.array([h]), np.array([0.0]), n_in, n_tail, q); V1m, _ = hydro_V(gfun, np.array([-h]), np.array([0.0]), n_in, n_tail, q)
    phixy = -(V1p[0] - V1m[0]) / (2 * h)
    # divergence and -Phi_yy = g_xi at a few points by central differences
    pts = [(0.3, 0.6), (1.0, 1.0), (0.7, 2.0)]; divs = []; poiss = []
    for (x0, y0) in pts:
        hh = 1e-4
        a, _ = hydro_V(gfun, np.array([x0 + hh, x0 - hh]), np.array([y0, y0]), n_in, n_tail, q); _, b2 = hydro_V(gfun, np.array([x0, x0]), np.array([y0 + hh, y0 - hh]), n_in, n_tail, q)
        c1, _ = hydro_V(gfun, np.array([x0, x0]), np.array([y0 + hh, y0 - hh]), n_in, n_tail, q); gxe = gfun(np.array([x0]), np.array([y0]))[1][0]
        divs.append((a[0] - a[1]) / (2 * hh) + (b2[0] - b2[1]) / (2 * hh)); poiss.append((c1[0] - c1[1]) / (2 * hh) - gxe)
    return dict(maxerr_V1=e1, maxerr_V2=e2, maxV1=np.abs(V1e).max(), maxV2=np.abs(V2e).max(), phixy=phixy, phixy_exact=-1 / tau, div=max(abs(d) for d in divs), poisson_defect=max(abs(p) for p in poiss))


if __name__ == '__main__':
    for (n_in, n_tail, q) in [(32, 100, 3), (64, 200, 3), (128, 400, 3), (64, 200, 2), (64, 200, 4)]:
        r = manufactured_test(1.0, n_in, n_tail, q)
        print(f"manufactured (tau = 1): n_in {n_in} n_tail {n_tail} q {q}: max|V1 - exact| {r['maxerr_V1']:.2e} (max|V1| {r['maxV1']:.2e}), max|V2 - exact| {r['maxerr_V2']:.2e} (max|V2| {r['maxV2']:.2e}); "
              f"Phi_xiy(0) = {r['phixy']:+.8f} (exact {r['phixy_exact']:+.3f}); max|div V| {r['div']:.1e}; max|d_y V1 - g_xi| {r['poisson_defect']:.1e}", flush=True)
    r = manufactured_test(0.25, 64, 200, 3); print(f"manufactured (tau = 0.25): errors V1 {r['maxerr_V1']:.2e} V2 {r['maxerr_V2']:.2e}; Phi_xiy(0) {r['phixy']:+.8f} (exact {r['phixy_exact']:+.3f})")
