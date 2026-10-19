"""Verifier's independent evaluation of the lead's w-only B_3 functional (lead analysis 7.3, scripts/b3_wonly_export.py),
verifier. Only rho samples are read (a gen_shape field or an export); w = W_1(x,0) comes from the verifier's own inverse.

Steps:
  1. odd sine modes f_m (vcand.load_modes), tails as in vresid.evaluate (power law k = 1/c_l outside, f_m(r0)(r/r0)^beta
     inside), own c and c_l = (1 + c)/3 (identity), FastInverse for p_n, p_n' (n <= Mmax + 1);
  2. axis: w = c_l x - Psi1, w' = c_l - Psi1' (analytic p_n'), w'' two ways: 8th-order FD in u of w', and the mode ODE
     p_n'' = -p_n'/r + n^2 p_n/r^2 - F_n, F_n the sin(n t) mode of d_x rho;
  3. w-only traces: h_w = 2c_l - w', g_w'/g_w = (w' - A)/w with g_w ~ x^2; the simple pole of (w' - A)/w at x*, residue
     eps = (mu1 - A)/mu1 (zero iff h(P) = 1), is removed (g_w is then smooth through x*; the dropped factor is
     |1 - x/x*|^eps); a2_w = (g_w' - w'')/2, b3_w = -a2_w'/3, F3_w = -a2_w g_w' - b3_w g_w;
  4. B_3 = f.p. int_0^{x*} -F3/(w H) with vb3.b3 (verifier's tool, independent of the lead's b3_diag.py / b3_ls.py) for
     several fit windows, in physical and natural units (x*^(p3 - 2) B_3), for the w-only traces and for the density traces.
  5. second route, closed form B_3 = (1/(3N)) f.p. int_0^{x*} (a2/g^3)' m^beta dx, m = |w|/g, beta = 2/A - 1, N = A^(2/A),
     own quadrature: even-polynomial finite part near 0, Gauss-Legendre in u in the middle, x* - x = s^(1/(1+beta)) at x*.
Usage: python3 vb3w.py field.npz Mmax out.json [axis_out.npz]
"""
import sys, json, warnings
warnings.simplefilter("ignore")
import numpy as np
from scipy.interpolate import CubicSpline
from vcand import load_modes
from vfast import FastInverse
from vb3 import axis_traces, find_xstar, b3, local_fit


def inverse(g, F, Mmax):
    """F: (N, Mh). Returns c, c_l, k, p, dp (nn, N), ns."""
    r = g.r
    Ft = F.T
    beta = np.maximum(np.arange(1, Mmax + 1, 2), 3).astype(float)
    fi = FastInverse(g, Mmax + 1)
    k = 0.18
    for _ in range(3):
        p, dp, c = fi.solve(Ft, (Ft[:, -1] / r[-1] ** k, k), (Ft[:, 0], beta))
        cl = (1 + c) / 3
        k = 1 / cl
    p, dp, c = fi.solve(Ft, (Ft[:, -1] / r[-1] ** k, k), (Ft[:, 0], beta))
    return c, (1 + c) / 3, k, p, dp, fi.ns


def w_traces(g, F, ms, p, dp, ns, cl):
    x = g.r
    n = ns[:, None].astype(float)
    Psi1 = (n * p).sum(0) / x
    Psi1p = (n * (dp - p / x)).sum(0) / x
    w = cl * x - Psi1
    wp = cl - Psi1p
    du = lambda a: g.du(a[:, None])[:, 0]
    wpp_fd = du(wp) / x
    # mode ODE route for w'' = -Psi1''
    Fm = {m: F[:, i] for i, m in enumerate(ms)}
    dF = g.du(F) / x[:, None]
    dFm = {m: dF[:, i] for i, m in enumerate(ms)}
    z = np.zeros_like(x)
    Psi1pp = np.zeros_like(x)
    for a, nn in enumerate(ns):
        flo, fhi = Fm.get(nn - 1, z), Fm.get(nn + 1, z)
        dlo, dhi = dFm.get(nn - 1, z), dFm.get(nn + 1, z)
        Fn = 0.5 * (dlo - (nn - 1) * flo / x + dhi + (nn + 1) * fhi / x)
        ppp = -dp[a] / x + nn ** 2 * p[a] / x ** 2 - Fn
        Psi1pp += nn * (ppp * x ** 2 - 2 * x * dp[a] + 2 * p[a]) / x ** 3
    wpp_ode = -Psi1pp
    return dict(x=x, w=w, wp=wp, wpp_fd=wpp_fd, wpp_ode=wpp_ode)


def wonly(g, tr, cl, xs, mu1, wpp_key='wpp_fd'):
    x, w, wp, wpp = tr['x'], tr['w'], tr['wp'], tr[wpp_key]
    A = 2 * cl - 1
    eps = (mu1 - A) / mu1
    e = (wp - A) / w - 2 / x - eps / (x - xs)
    # cumulative int_0^x e dt = int e x du (from r0) + e(r0) r0 / 2 (e = O(x) at 0)
    cum = g.expcum_fwd(e * x, 0.0) + 0.5 * e[0] * x[0]
    gw = x ** 2 * np.exp(cum)
    gwp = gw * (e + 2 / x)
    a2 = (gwp - wpp) / 2
    a2p = g.du(a2[:, None])[:, 0] / x
    b3w = -a2p / 3
    F3 = -a2 * gwp - b3w * gw
    h = 2 * cl - wp
    return dict(x=x, w=w, h=h, F3=F3, G3=np.full_like(x, 1e-300), G1=gw, G1p=gwp, W1_2=a2, W2_3=b3w, eps=eps, a2p=a2p)


def closed_form(ax, cl, xs, t_lo_frac=0.01, t_c_frac=0.3, K=8, end_frac=0.04, nq=400):
    """(1/(3N)) f.p. int_0^{x*} (a2/g^3)' m^beta, m = |w|/g; own quadrature (route 2)."""
    x, w, gw, gwp, a2, a2p = ax['x'], ax['w'], ax['G1'], ax['G1p'], ax['W1_2'], ax['a2p']
    A = 2 * cl - 1
    be = 2 / A - 1
    Nn = A ** (2 / A)
    qd = a2p / gw ** 3 - 3 * a2 * gwp / gw ** 4          # (a2/g^3)'
    m = np.abs(w) / gw
    I = qd * m ** be
    u = np.log(x)
    p3 = 6 + 2 / A
    # near 0: I = x^{1 - p3} * even series
    t_lo, t_c = t_lo_frac * xs, t_c_frac * xs
    sel = (x >= t_lo) & (x <= t_c)
    tt = x[sel]
    q = I[sel] * tt ** (p3 - 1)
    M = np.stack([tt ** (2 * k) for k in range(K + 1)], 1)
    qk, *_ = np.linalg.lstsq(M, q, rcond=None)
    fit = float(np.abs(M @ qk - q).max() / np.abs(q).max())
    fp0 = float(sum(qk[k] * t_c ** (2 * k + 2 - p3) / (2 * k + 2 - p3) for k in range(K + 1)))
    # middle: Gauss-Legendre in u, spline of the smooth factors qd and m in u
    left = x < xs * (1 - 0.004)
    cq = CubicSpline(u[left], qd[left])
    # m = (x* - x) Mt(x), Mt smooth (w has a simple zero); spline Mt = m / (x* - x) through points away from x*
    cm = CubicSpline(u[left], m[left] / (xs - x[left]))
    Ifun = lambda xx: cq(np.log(xx)) * (cm(np.log(xx)) * (xs - xx)) ** be
    x_e = xs * (1 - end_frac)
    gx, gwt = np.polynomial.legendre.leggauss(nq)
    ua, ub = np.log(t_c), np.log(x_e)
    uq = 0.5 * (ua + ub) + 0.5 * (ub - ua) * gx
    xq = np.exp(uq)
    mid = float(np.sum(Ifun(xq) * xq * gwt) * 0.5 * (ub - ua))
    # end: I = (x* - x)^be * Q(x), Q = qd Mt^be smooth up to x*; fit Q by a polynomial on points left of x*, then
    # int_0^{d} s'^be Q(x* - s') ds' with s' = t^{1/(1+be)}
    selE = (x > xs * (1 - 2.5 * end_frac)) & left
    Qv = qd[selE] * (m[selE] / (xs - x[selE])) ** be
    pQ = np.poly1d(np.polyfit(x[selE] - xs, Qv, 5))
    dd = xs - x_e
    ta = dd ** (1 + be)
    ts = 0.5 * ta * (gx + 1)
    endp = float(np.sum(pQ(-(ts ** (1 / (1 + be)))) * gwt) * 0.5 * ta / (1 + be))
    B = (fp0 + mid + endp) / (3 * Nn)
    return dict(B3=B, fp0=fp0 / (3 * Nn), mid=mid / (3 * Nn), endp=endp / (3 * Nn), fit=fit)


def main(path, Mmax, outp, axp=None):
    d, g, ms, F = load_modes(path, Mmax)
    c, cl, k, p, dp, ns = inverse(g, F, Mmax)
    A = 2 * cl - 1
    p3 = 6 + 2 / A
    tr = w_traces(g, F, ms, p, dp, ns, cl)
    x, w = tr['x'], tr['w']
    xs = find_xstar(x, w)
    pw = local_fit(x, w, xs, 0.1 * xs)
    mu1 = float(pw.deriv()(0.0))
    nat = xs ** (p3 - 2)
    out = dict(file=path, Mmax=Mmax, N=len(x), r0=float(x[0]), R=float(x[-1]), c=c, c_l=cl, k=k, A=A, p3=p3,
               x_star=xs, mu1=mu1, hP_w=2 * cl - mu1, natural_unit_factor=nat)
    sel = (x > 0.05) & (x < 1.3 * xs)
    out['wpp_fd_vs_ode_max'] = float(np.abs(tr['wpp_fd'] - tr['wpp_ode'])[sel].max())
    out['wpp_scale'] = float(np.abs(tr['wpp_fd'])[sel].max())
    # density traces (vb3.axis_traces) for comparison
    du = lambda a: g.du(a)
    axd = axis_traces(F.T, ms, p, dp, ns, x, cl, du)
    res = {}
    for key in ('wpp_fd', 'wpp_ode'):
        ax = wonly(g, tr, cl, xs, mu1, key)
        if key == 'wpp_fd':
            out['eps_pole'] = ax['eps']
            jj = [int(np.argmin(np.abs(x - t))) for t in (0.01, 0.15, 0.5, 1.5, 4.0, 8.0, 8.5)]
            out['gw_over_G1_minus_1'] = {('%.3g' % x[j]): float(ax['G1'][j] / axd['G1'][j] - 1) for j in jj}
            out['a2w_minus_a2rho'] = {('%.3g' % x[j]): float(ax['W1_2'][j] - axd['W1_2'][j]) for j in jj}
            out['dropped_factor_at'] = {('%.3g' % t): float(abs(1 - t / xs) ** ax['eps']) for t in (1.0, 8.0, 8.5)}
            if axp:
                np.savez(axp, x=x, w=w, wp=tr['wp'], wpp_fd=tr['wpp_fd'], wpp_ode=tr['wpp_ode'], gw=ax['G1'],
                         a2w=ax['W1_2'], G1=axd['G1'], c_l=cl, x_star=xs)
        rows = []
        for (tlo, tc, K) in ((0.01, 0.3, 8), (0.02, 0.3, 8), (0.005, 0.4, 10), (0.01, 0.4, 8), (0.01, 0.2, 6),
                             (0.01, 0.3, 6), (0.01, 0.3, 10), (0.003, 0.25, 8)):
            o = b3(ax, t_lo_frac=tlo, t_c_frac=tc, K=K)
            cf = closed_form(ax, cl, xs, t_lo_frac=tlo, t_c_frac=tc, K=K)
            rows.append(dict(t_lo=tlo, t_c=tc, K=K, B3=o['B3'], B3_nat=o['B3'] * nat, fit=o['fit_err'],
                             B3_closed=cf['B3'], B3_closed_nat=cf['B3'] * nat, fit_closed=cf['fit'], p3_meas=o['p3']))
        res['wonly_' + key] = rows
    rows = []
    for (tlo, tc, K) in ((0.01, 0.3, 8), (0.02, 0.3, 8), (0.005, 0.4, 10), (0.01, 0.4, 8), (0.01, 0.2, 6)):
        o = b3(axd, t_lo_frac=tlo, t_c_frac=tc, K=K)
        rows.append(dict(t_lo=tlo, t_c=tc, K=K, B3=o['B3'], B3_nat=o['B3'] * nat, fit=o['fit_err'],
                         hybrid_nat=[v * nat for v in o['hybrid']]))
    res['density_traces'] = rows
    out['B3'] = res
    out['w_at'] = {('%.4g' % t): float(CubicSpline(np.log(x), w)(np.log(t))) for t in (0.15, 0.5, 1.5, 4.0, 8.0)}
    json.dump(out, open(outp, 'w'), indent=1, default=float)
    return out


if __name__ == '__main__':
    o = main(sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else None)
    print(json.dumps({k: v for k, v in o.items() if k != 'B3'}, indent=1, default=float))
    for key, rows in o['B3'].items():
        print(key)
        for rw in rows:
            print('  ', ' '.join('%s=%s' % (a, ('%.4g' % b) if isinstance(b, float) else b) for a, b in rw.items()))
