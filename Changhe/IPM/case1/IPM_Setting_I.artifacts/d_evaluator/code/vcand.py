"""Verifier's independent evaluation of a sampled candidate field (verifier).

Input: npz with r (uniform in log r), theta (uniform on [0, pi/2], endpoints included) and rho[i, j] = rho(r_i, theta_j)
in the closed first quadrant (the construct1 export format of the lead lane). Only rho is used; the exporter's psi, U,
c_l and residual are read only for comparison.
Steps (all verifier code):
  1. odd sine modes f_m(r), m <= Mmax, by the trapezoid rule on the reflected periodic function (exact DST);
  2. vresid.evaluate on the full circle: own inverse (vpolar), c from formula C3 with own tails, c_l = (1 + c)/3
     (identity, not the exporter's c_l), R = W.grad rho - rho with own derivatives, E = -Lap psi - d_x rho;
  3. regional residuals sup|R| / sup(|rho| + |X.grad rho| + |U.grad rho|) on radial bands, pointwise maxima;
  4. axis diagnostics with vb3 (x*, mu1, h(P), div check, B_3).
Usage: python3 vcand.py file.npz '{"Mmax": 255, "k_far": null}'
"""
import sys, json, warnings
warnings.simplefilter("ignore")
import numpy as np
from scipy.interpolate import CubicSpline
from vpolar import LogGrid
from vresid import evaluate
from vb3 import axis_traces, find_xstar, b3


def load_modes(path, Mmax):
    d = np.load(path, allow_pickle=True)
    r, th, rq = d['r'], d['theta'], d['rho']
    g = LogGrid(len(r), r[0], r[-1])
    assert np.allclose(g.r, r, rtol=1e-12), 'radial grid is not uniform in log r'
    dth = np.diff(th)
    assert np.allclose(dth, dth[0]) and abs(th[0]) < 1e-14 and abs(th[-1] - np.pi / 2) < 1e-12
    wq = np.full(len(th), dth[0])
    wq[0] = wq[-1] = 0.5 * dth[0]
    ms = np.arange(1, Mmax + 1, 2)
    F = (4 / np.pi) * rq @ (np.sin(np.outer(ms, th)) * wq).T     # (N, Mh)
    return d, g, ms, F


def d10(ev, g, th, rho):
    """SPEC D10: Q3 = int rho U.grad(phi) dX, phi = sin(3 theta) r^-3 (harmonic), must equal (c_l - 1) pi c, i.e.
    q = Q3/c^2 = (pi/3)(1 - 2/c). Derivation: multiply W.grad rho = rho by phi, integrate by parts (div W = 2 c_l,
    X.grad phi = -3 phi, boundary terms O(r0^2) and O(R^(k-1))), int phi rho dX = pi int f_3 r^-2 dr = pi c.
    U.grad phi = 3 r^-4 (-U_r sin 3t + U_t cos 3t); dX = r^2 du dt. Outer tail: power-law extrapolation of the radial profile."""
    r = g.r
    integrand = 3 * rho * (-ev.Ur * np.sin(3 * th)[None, :] + ev.Ut * np.cos(3 * th)[None, :]) / r[:, None] ** 2
    prof = integrand.sum(1) * (2 * np.pi / len(th))          # periodic trapezoid in theta
    from scipy.integrate import simpson
    Q3 = simpson(prof, x=np.log(r))
    # tail beyond R: prof ~ C e^{s u}, s < 0 fitted on the last decade
    sel = r > r[-1] / 10
    s = np.polyfit(np.log(r[sel]), np.log(np.abs(prof[sel]) + 1e-300), 1)[0]
    tail = prof[-1] / (-s) if s < 0 else float('nan')
    Q3t = Q3 + tail
    c, cl = ev.c, ev.c_l
    target = (cl - 1) * np.pi * c
    return dict(Q3=float(Q3t), Q3_tail=float(tail), tail_slope=float(s), Q3_target=float(target),
                q=float(Q3t / c ** 2), q_target=float(np.pi / 3 * (1 - 2 / c)), rel_defect=float((Q3t - target) / target))


def main(path, cfg):
    Mmax = cfg.get('Mmax', 255)
    d, g, ms, F = load_modes(path, Mmax)
    r = g.r
    Nt = cfg.get('Nt', 4 * (Mmax + 1))
    th = 2 * np.pi * np.arange(Nt) / Nt
    rho = F @ np.sin(np.outer(ms, th))
    out = dict(file=path, Mmax=Mmax, Nt=Nt, N=len(r), r0=float(r[0]), R=float(r[-1]))
    # reconstruction on the exporter's quarter-circle points (they coincide with ours if Nt = 4 * (len(theta) - 1))
    nq = d['rho'].shape[1]
    if Nt == 4 * (nq - 1):
        out['recon_err_rel'] = float(np.abs(rho[:, :nq] - d['rho']).max() / np.abs(d['rho']).max())
    out['top_mode_share'] = float(np.abs(F[:, -8:]).max() / np.abs(F).max())
    ev = evaluate(rho, g, th, c_l=None, nmax=Mmax + 1, k_far=cfg.get('k_far'), k_self=cfg.get('k_self', False))
    out.update(c=float(ev.c), c_notail=float(ev.c_notail), c_l=float(ev.c_l), k_far=ev.k_far,
               c_exporter=float(d['c']) if 'c' in d.files else None,
               cl_exporter=float(d['c_l']) if 'c_l' in d.files else None,
               parity_bad=float(ev.parity_bad))
    # regional residuals
    bands = cfg.get('bands', [[r[0], 1e-2], [1e-2, 1], [1, 10], [10, 100], [100, 1e3], [1e3, r[-1]]])
    trim = 8
    reg = []
    for a, b in bands:
        sel = (r >= a) & (r <= b)
        sel[:trim] = False
        sel[-trim:] = False
        if sel.sum() == 0 or ev.Rnorm[sel].max() == 0:
            continue
        R, Nn = ev.R[sel], ev.Rnorm[sel]
        mask = Nn > 1e-8 * Nn.max()
        reg.append(dict(band=[float(a), float(b)], relsup=float(np.abs(R).max() / Nn.max()),
                        relpt=float((np.abs(R[mask]) / Nn[mask]).max()),
                        relE=float(np.abs(ev.E[sel]).max() / np.abs(ev.dxrho[sel]).max())))
    out['regions'] = reg
    out['D10'] = d10(ev, g, th, rho)
    # velocity comparison with the exporter (first quadrant points)
    if 'U1' in d.files and Nt == 4 * (nq - 1):
        ct, st = np.cos(th[:nq])[None, :], np.sin(th[:nq])[None, :]
        Ur, Ut = ev.Ur[:, :nq], ev.Ut[:, :nq]
        U1, U2 = Ur * ct - Ut * st, Ur * st + Ut * ct
        scale = np.sqrt(d['U1'] ** 2 + d['U2'] ** 2).max(axis=1)[:, None] + 1e-300
        dU = np.sqrt((U1 - d['U1']) ** 2 + (U2 - d['U2']) ** 2) / scale
        out['U_diff_rel_by_band'] = [float(dU[(r >= a) & (r <= b)].max()) for a, b in bands]
        if 'residual' in d.files:
            # the exporter's residual sign convention is unknown: compare magnitudes
            out['exporter_res_rel'] = float(np.abs(d['residual']).max() / d['denominator'].max())
    # axis
    ns = np.array(sorted(ev.pm))
    P = np.array([ev.pm[n][0] for n in ns])
    dP = np.array([ev.pm[n][1] for n in ns])
    Fm = F.T
    du = lambda A: g.du(A)
    ax = axis_traces(Fm, ms, P, dP, ns, r, ev.c_l, du)
    x, w, h = ax['x'], ax['w'], ax['h']
    xs = find_xstar(x, w)
    out['x_star'] = xs
    if xs is not None:
        wp = g.du(w[:, None])[:, 0] / x
        mu1 = float(CubicSpline(np.log(x), wp)(np.log(xs)))
        hP = float(CubicSpline(np.log(x), h)(np.log(xs)))
        out.update(mu1=mu1, hP=hP, div_chk=mu1 + hP - 2 * ev.c_l, A=2 * ev.c_l - 1)
        zs = np.where(np.diff(np.sign(w[x > 1.5 * xs])) != 0)[0]
        out['other_axis_zeros'] = [float(x[x > 1.5 * xs][j]) for j in zs]
        if cfg.get('b3', True):
            try:
                o = b3(ax)
                out['B3'] = {k: o[k] for k in ('B3', 'fp0', 'mid', 'endp', 'fit_err', 'hybrid', 'B3_hat', 'kappa', 'p3',
                                                'lambda1m', 'lambda2m') if k in o}
            except Exception as e:
                out['B3'] = 'failed: %r' % e
    # W_2/y on the y-axis and min over the quadrant (sign checks)
    return out, ev, ax


if __name__ == '__main__':
    cfg = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    out, ev, ax = main(sys.argv[1], cfg)
    print(json.dumps(out, indent=1, default=float))
