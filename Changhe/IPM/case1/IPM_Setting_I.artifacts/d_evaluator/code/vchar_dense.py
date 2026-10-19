"""Characteristic defect J on a prescribed set of start angles (VERIFY_REPORT G69 (e)), verifier.
Same evaluation, splines and integrator as vchar.run_ev (code/vchar.py); only the start set differs. Start points on
|X| = r_start at
  A: theta0 uniform in [0.02, pi/2 - 0.02], n_uni points;
  B: theta0 = pi/2 - delta, delta geometric in [dmin, 0.02), n_geo points (these pass the stagnation point at 0 and reach P
     along the x-axis from the left; the y-axis is the separatrix);
  C: theta0 = delta, delta geometric in [dmin, 0.02), n_geo points (next to the x-axis right of P).
Optional theta window [t_lo, t_hi] restricts A to that window (resolution check of J(theta0)).
Usage: python3 vchar_dense.py field.npz Mmax r_start n_uni n_geo dmin out.json [t_lo t_hi]
"""
import sys, os, json, warnings
warnings.simplefilter("ignore")
import numpy as np
from scipy.interpolate import RectBivariateSpline
from scipy.integrate import solve_ivp
from vcand import main as vcand_main, load_modes
from vb3 import find_xstar
from vchar import half_shift


def run(path, Mmax, r_start, n_uni, n_geo, dmin, outp, win=None, epsl=(4.0, 2.0, 1.0, 0.3, 0.1, 0.03, 0.01)):
    out, ev, ax = vcand_main(path, dict({'Mmax': Mmax, 'b3': False}, **json.loads(os.environ.get('VCHAR_CFG', '{}'))))  # VCHAR_CFG: extra vcand cfg, e.g. {"k_self": true}
    d, g, ms, F = load_modes(path, Mmax)
    r = g.r
    Nt = out['Nt']
    th = 2 * np.pi * np.arange(Nt) / Nt
    cl = ev.c_l
    keep = r < max(3 * r_start, 60.0)
    rho = F @ np.sin(np.outer(ms, th))
    q = half_shift(ev.R, Nt) / half_shift(rho, Nt)
    thm = th + np.pi / Nt
    ct, st = np.cos(th)[None, :], np.sin(th)[None, :]
    U1 = ev.Ur * ct - ev.Ut * st
    U2 = ev.Ur * st + ev.Ut * ct
    W1, W2 = cl * r[:, None] * ct + U1, cl * r[:, None] * st + U2

    def window(tt, A):
        tt = np.where(tt > np.pi, tt - 2 * np.pi, tt)
        o = np.argsort(tt)
        tt, A = tt[o], A[:, o]
        s = (tt > -0.15) & (tt < np.pi / 2 + 0.15)
        return tt[s], A[keep][:, s]
    lr = np.log(r[keep])
    t1, W1w = window(th, W1)
    _, W2w = window(th, W2)
    t2, qw = window(thm, q)
    sW1 = RectBivariateSpline(lr, t1, W1w, kx=5, ky=5)
    sW2 = RectBivariateSpline(lr, t1, W2w, kx=5, ky=5)
    sq = RectBivariateSpline(lr, t2, qw, kx=5, ky=5)
    xs = find_xstar(np.asarray(ax['x']), np.asarray(ax['w']))

    def rhs(tau, Z):
        l, t = np.log(np.hypot(Z[0], Z[1])), np.arctan2(Z[1], Z[0])
        return [-float(sW1.ev(l, t)), -float(sW2.ev(l, t)), float(sq.ev(l, t))]
    evs = []
    for e in epsl:
        f = (lambda e_: (lambda tau, Z: np.hypot(Z[0] - xs, Z[1]) - e_))(e)
        f.terminal = (e == epsl[-1])
        f.direction = -1
        evs.append(f)
    if win is None:
        A = np.linspace(0.02, np.pi / 2 - 0.02, n_uni)
    else:
        A = np.linspace(win[0], win[1], n_uni)
    geo = np.geomspace(dmin, 0.02, n_geo + 1)[:-1] if n_geo > 0 else np.zeros(0)
    starts = [('A', t) for t in A] + [('B', np.pi / 2 - dl) for dl in geo] + [('C', dl) for dl in geo]
    rows = []
    for fam, t0 in starts:
        Z0 = [r_start * np.cos(t0), r_start * np.sin(t0), 0.0]
        rec = {}
        for tol in (1e-9, 1e-11):
            sol = solve_ivp(rhs, (0, 300), Z0, method='DOP853', events=evs, rtol=tol, atol=tol * 1e-2, max_step=0.05)
            Js = [float(ye[0][2]) if len(ye) else float('nan') for ye in sol.y_events]
            taus = [float(te[0]) if len(te) else float('nan') for te in sol.t_events]
            # heights at which the characteristic crosses x = x* - 1 (left of P), if it does
            xx, yy = sol.y[0], sol.y[1]
            k = np.nonzero((xx[:-1] - (xs - 1)) * (xx[1:] - (xs - 1)) < 0)[0]
            ycross = float(yy[k[-1]]) if len(k) else float('nan')
            rec[tol] = dict(J=Js, tau=taus, rmin=float(np.hypot(xx, yy).min()), ycross=ycross)
        rows.append(dict(fam=fam, theta0=float(t0), J=rec[1e-11]['J'], tau=rec[1e-11]['tau'], rmin=rec[1e-11]['rmin'],
                         ycross=rec[1e-11]['ycross'],
                         dtol=float(np.nanmax(np.abs(np.array(rec[1e-9]['J']) - np.array(rec[1e-11]['J']))))))
        rw = rows[-1]
        print('%s %.7f rmin %.3g ycross %.3g J %s dtol %.1e' % (fam, t0, rw['rmin'], rw['ycross'],
              ' '.join('%+.4e' % v for v in rw['J']), rw['dtol']), flush=True)
    J = np.array([rw['J'] for rw in rows])
    summ = dict(file=path, Mmax=Mmax, r_start=r_start, c_l=cl, x_star=xs, eps_P=list(epsl), n=len(rows),
                spread=[float(np.nanmax(J[:, i]) - np.nanmin(J[:, i])) for i in range(len(epsl))])
    print(json.dumps(summ))
    json.dump(dict(summary=summ, rows=rows), open(outp, 'w'), indent=1, default=float)


if __name__ == '__main__':
    a = sys.argv
    win = (float(a[8]), float(a[9])) if len(a) > 9 else None
    run(a[1], int(a[2]), float(a[3]), int(a[4]), int(a[5]), float(a[6]), a[7], win)
