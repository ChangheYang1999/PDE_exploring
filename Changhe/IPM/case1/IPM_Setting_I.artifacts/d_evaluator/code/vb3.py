"""Verifier's independent axis diagnostics (D3/D7) and B_3 evaluation, verifier.

Axis traces from polar modes (rho = sum_m f_m sin m t, m odd; psi = sum_n p_n sin n t, n even), x = r on theta = 0:
  G1 = d_y rho(x,0)        = sum m f_m / x
  G3 = d_y^3 rho(x,0)/6    = x^-3 sum [ -f_m (m/3 + m^3/6) + x f_m' m/2 ]
  Psi1, Psi3: the same formulas for psi.
  w = W_1(x,0) = c_l x - Psi1,  h = d_y W_2(x,0) = c_l + Psi1',
  W1_2 = (1/2) d_y^2 W_1(x,0) = -3 Psi3,  W2_3 = (1/6) d_y^3 W_2(x,0) = Psi3'.
Axis ODEs (lead analysis 3.1): w G1' = (1 - h) G1,  w G3' + (3h - 1) G3 = F3 := -W1_2 G1' - W2_3 G1.
B_3 = f.p. int_0^{x*} J,  J = -F3/(w H),  H = exp(int (1 - 3h)/w) normalized by H ~ x^{p3} at 0.

Numerics (independent of the lead's scripts/b3_diag.py):
 - near 0: q(t) = J t^{p3-1} is fitted by an even polynomial on [t_lo, t_c]; f.p. int_0^{t_c} J = sum q_k t_c^{2k+2-p3}/(2k+2-p3);
 - middle: Gauss-Legendre on [t_c, x_e] with J from a cubic spline in u = log x of the smooth factors;
 - near x*: J = (x* - x)^{kap-1} Q(x), Q smooth, kap = (3 mu2 - 1)/mu1; substitution x* - x = s^{1/kap}.
"""
import numpy as np
from scipy.interpolate import CubicSpline


def axis_traces(F, ms, P, dP, ns, r, cl, du):
    """F: (Mh, N) modes f_m; P, dP: (nn, N) modes p_n and dp_n/dr; du: function computing d/du along axis 0 of (N, k) arrays."""
    x = r
    m = ms[:, None].astype(float)
    n = ns[:, None].astype(float)
    dF = du(F.T).T / r          # f_m'
    G1 = (m * F).sum(0) / x
    G3 = (-(F * (m / 3 + m ** 3 / 6)).sum(0) + x * (dF * m / 2).sum(0)) / x ** 3
    Psi1 = (n * P).sum(0) / x
    Psi3 = (-(P * (n / 3 + n ** 3 / 6)).sum(0) + x * (dP * n / 2).sum(0)) / x ** 3
    d = du(np.stack([Psi1, Psi3, G1], 1)) / r[:, None]
    Psi1p, Psi3p, G1p = d[:, 0], d[:, 1], d[:, 2]
    w = cl * x - Psi1
    h = cl + Psi1p
    W1_2 = -3 * Psi3
    W2_3 = Psi3p
    F3 = -W1_2 * G1p - W2_3 * G1
    return dict(x=x, G1=G1, G1p=G1p, G3=G3, w=w, h=h, W1_2=W1_2, W2_3=W2_3, F3=F3)


def find_xstar(x, w):
    """First positive zero of w with w < 0 before it; refined by a local cubic in x."""
    s = np.where((w[:-1] < 0) & (w[1:] >= 0))[0]
    if not len(s):
        return None
    j = s[0]
    st = np.arange(max(j - 2, 0), min(j + 4, len(x)))
    c = np.polyfit(x[st] - x[j], w[st], 3)
    rts = np.roots(c)
    rts = rts[np.isreal(rts)].real + x[j]
    return float(rts[np.argmin(np.abs(rts - x[j]))])


def local_fit(x, f, x0, half, deg=6):
    # the window is widened until it holds at least 3 (deg + 1) grid points (a narrower window makes polyfit unreliable)
    sel = np.abs(x - x0) <= half
    while sel.sum() < 3 * (deg + 1):
        half *= 1.25
        sel = np.abs(x - x0) <= half
    c = np.polyfit(x[sel] - x0, f[sel], deg)
    return np.poly1d(c)


def b3(ax, t_lo_frac=0.01, t_c_frac=0.3, end_frac=0.04, K=8, nq=400, excl=0.004):
    """Returns dict with x*, mu1, mu2, lambda1m, lambda2m, p3, B3 and its pieces."""
    x, w, h, F3 = ax['x'], ax['w'], ax['h'], ax['F3']
    xs = find_xstar(x, w)
    out = dict(x_star=xs)
    if xs is None:
        return out
    pw = local_fit(x, w, xs, 0.1 * xs)
    ph = local_fit(x, h, xs, 0.1 * xs)
    mu1 = float(pw.deriv()(0.0))
    mu2 = float(ph(0.0))
    kap = (3 * mu2 - 1) / mu1
    # exponents at 0, measured from the traces on [t_lo, 4 t_lo]
    sel0 = (x > t_lo_frac * xs * 0.1) & (x < t_lo_frac * xs)
    lam1 = float(np.polyfit(x[sel0] ** 2, w[sel0] / x[sel0], 2)[-1])
    lam2 = float(np.polyfit(x[sel0] ** 2, h[sel0], 2)[-1])
    p3 = (3 * lam2 - 1) / abs(lam1)
    out.update(mu1=mu1, mu2=mu2, kappa=kap, lambda1m=lam1, lambda2m=lam2, p3=p3)
    u = np.log(x)
    # log H = p3 log x - kap log(1 - x/x*) - kap x/x* + S0(x), S0(x) = int_0^x g0,
    # g0 = (1-3h)/w - p3/t - kap t/(x*(x*-t)): both poles removed and g0 = O(t) at 0, so the spline is accurate up to x* - excl.
    g0 = (1 - 3 * h) / w - p3 / x - kap * x / (xs * (xs - x))
    left = x < xs * (1 - excl)
    i0 = np.searchsorted(x, t_lo_frac * xs * 0.1)
    cs = CubicSpline(u[i0:left.sum()], (g0 * x)[i0:left.sum()])   # integrand in u: g0 dt = g0 x du
    S00 = 0.5 * g0[i0] * x[i0]   # int_0^{x[i0]} g0 dt, with g0 = O(t) near 0
    def S0(xx):
        return cs.integrate(u[i0], np.log(xx)) + S00
    def logH(xx):
        return p3 * np.log(xx) - kap * np.log(1 - xx / xs) - kap * xx / xs + np.vectorize(S0)(xx)
    # J on the middle range via splines of smooth factors
    csF = CubicSpline(u, F3)
    csw = CubicSpline(u, w)
    def J(xx):
        return -csF(np.log(xx)) / (csw(np.log(xx)) * np.exp(logH(xx)))
    # near 0: fit q(t) = J t^{p3-1} as an even polynomial
    t_lo, t_c = t_lo_frac * xs, t_c_frac * xs
    sel = (x >= t_lo) & (x <= t_c)
    tt = x[sel]
    q = -F3[sel] / (w[sel] * np.exp(logH(tt))) * tt ** (p3 - 1)
    A = np.stack([tt ** (2 * k) for k in range(K + 1)], 1)
    qk, *_ = np.linalg.lstsq(A, q, rcond=None)
    fit_err = float(np.abs(A @ qk - q).max() / np.abs(q).max())
    fp0 = float(sum(qk[k] * t_c ** (2 * k + 2 - p3) / (2 * k + 2 - p3) for k in range(K + 1)))
    # middle: Gauss-Legendre in u on [t_c, x_e]
    x_e = xs * (1 - end_frac)
    gx, gw = np.polynomial.legendre.leggauss(nq)
    ua, ub = np.log(t_c), np.log(x_e)
    uq = 0.5 * (ua + ub) + 0.5 * (ub - ua) * gx
    xq = np.exp(uq)
    mid = float(np.sum(J(xq) * xq * gw) * 0.5 * (ub - ua))
    # end piece: J = (x* - x)^{kap-1} Q, Q = -F3 e^{-S}/w * (x*-x) ... computed at grid points away from x*, fitted, then
    # integrated with x* - x = s^{1/kap}.
    # log H(x) = -kap log(x* - x) + L(x), L smooth on both sides; we only need x < x*.
    selE = (x > xs * (1 - 2.5 * end_frac)) & (x < xs * (1 - excl))
    xe_pts = x[selE]
    LH = logH(xe_pts) + kap * np.log(xs - xe_pts)
    Qv = -F3[selE] * np.exp(-LH) * (xs - xe_pts) / w[selE]     # J (x*-x)^{1-kap}... see below
    # J = -F3/(w H) = -F3 exp(-LH) (x*-x)^kap / w = (x*-x)^{kap-1} * [ -F3 exp(-LH) (x*-x) / w ]
    pQ = np.poly1d(np.polyfit(xe_pts - xs, Qv, 5))
    sa = (xs - x_e) ** kap
    gs = 0.5 * sa * (gx + 1)
    endp = float(np.sum(pQ(-(gs ** (1 / kap))) * gw) * 0.5 * sa / kap)
    B3 = fp0 + mid + endp
    # hybrid check: B3(x) = f.p. int_0^x J + G3(x)/H(x) at a few x in the middle
    hyb = []
    for fr in (0.3, 0.5, 0.7):
        xm = fr * xs
        ub2 = np.log(xm)
        uq2 = 0.5 * (ua + ub2) + 0.5 * (ub2 - ua) * gx
        xq2 = np.exp(uq2)
        m2 = float(np.sum(J(xq2) * xq2 * gw) * 0.5 * (ub2 - ua))
        G3m = float(CubicSpline(u, ax['G3'])(ub2))
        hyb.append(fp0 + m2 + G3m / np.exp(logH(np.array([xm]))[0]))
    G3max = float(np.abs(ax['G3'][x <= xs]).max())
    out.update(B3=B3, fp0=fp0, mid=mid, endp=endp, fit_err=fit_err, qk=qk.tolist(), hybrid=hyb,
               B3_hat=B3 * xs ** p3 / G3max, G3max=G3max)
    return out
