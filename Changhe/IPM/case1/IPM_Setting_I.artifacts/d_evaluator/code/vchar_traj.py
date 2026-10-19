"""Where along a characteristic J accumulates (VERIFY_REPORT G69 (e)), verifier. Same evaluation, splines and
integrator as vchar.run_ev / vchar_dense.run; records (x, y, tau, J) on a dense tau grid for given start angles on
|X| = r_start, and J accumulated in named regions: y-axis strip (x < 0.5, y > 0.5), origin disk (r < 0.5), x-axis strip
(y < 0.5, 0.5 <= x, |X - P| >= 0.5), disk |X - P| < 0.5, and the rest.
Usage: python3 vchar_traj.py field.npz Mmax r_start theta0[,theta0...] out.json
"""
import sys, json, warnings
warnings.simplefilter("ignore")
import numpy as np
from scipy.interpolate import RectBivariateSpline
from scipy.integrate import solve_ivp
from vcand import main as vcand_main, load_modes
from vb3 import find_xstar
from vchar import half_shift


def main(path, Mmax, r_start, t0s, outp):
    out, ev, ax = vcand_main(path, {'Mmax': Mmax, 'b3': False})
    d, g, ms, F = load_modes(path, Mmax)
    r = g.r; Nt = out['Nt']; th = 2 * np.pi * np.arange(Nt) / Nt; cl = ev.c_l
    keep = r < max(3 * r_start, 60.0)
    rho = F @ np.sin(np.outer(ms, th))
    q = half_shift(ev.R, Nt) / half_shift(rho, Nt)
    thm = th + np.pi / Nt
    ct, st = np.cos(th)[None, :], np.sin(th)[None, :]
    W1 = cl * r[:, None] * ct + ev.Ur * ct - ev.Ut * st
    W2 = cl * r[:, None] * st + ev.Ur * st + ev.Ut * ct

    def window(tt, A):
        tt = np.where(tt > np.pi, tt - 2 * np.pi, tt); o = np.argsort(tt); tt, A = tt[o], A[:, o]
        s = (tt > -0.15) & (tt < np.pi / 2 + 0.15)
        return tt[s], A[keep][:, s]
    lr = np.log(r[keep])
    t1, W1w = window(th, W1); _, W2w = window(th, W2); t2, qw = window(thm, q)
    sW1 = RectBivariateSpline(lr, t1, W1w, kx=5, ky=5); sW2 = RectBivariateSpline(lr, t1, W2w, kx=5, ky=5)
    sq = RectBivariateSpline(lr, t2, qw, kx=5, ky=5)
    xs = find_xstar(np.asarray(ax['x']), np.asarray(ax['w']))

    def rhs(tau, Z):
        l, t = np.log(np.hypot(Z[0], Z[1])), np.arctan2(Z[1], Z[0])
        return [-float(sW1.ev(l, t)), -float(sW2.ev(l, t)), float(sq.ev(l, t))]
    stop = lambda tau, Z: np.hypot(Z[0] - xs, Z[1]) - 0.03
    stop.terminal = True; stop.direction = -1
    res = []
    for t0 in t0s:
        Z0 = [r_start * np.cos(t0), r_start * np.sin(t0), 0.0]
        sol = solve_ivp(rhs, (0, 300), Z0, method='DOP853', events=[stop], rtol=1e-11, atol=1e-13, max_step=0.01,
                        dense_output=True)
        T = sol.t[-1]; tt = np.linspace(0, T, 20001); Y = sol.sol(tt)
        x, y, J = Y
        dJ = np.diff(J); xm, ym = 0.5 * (x[1:] + x[:-1]), 0.5 * (y[1:] + y[:-1])
        rm = np.hypot(xm, ym); dP = np.hypot(xm - xs, ym)
        regs = dict(yaxis=(xm < 0.5) & (ym > 0.5), origin=rm < 0.5, xaxis=(ym < 0.5) & (xm >= 0.5) & (dP >= 0.5), Pdisk=dP < 0.5)
        regs['rest'] = ~(regs['yaxis'] | regs['origin'] | regs['xaxis'] | regs['Pdisk'])
        acc = {k: float(dJ[m].sum()) for k, m in regs.items()}
        # J accumulated along the y-axis strip by height band
        yb = {}
        for lo, hi in ((0.5, 2), (2, 5), (5, 10), (10, 21)):
            m = regs['yaxis'] & (ym >= lo) & (ym < hi); yb['%g-%g' % (lo, hi)] = float(dJ[m].sum())
        xb = {}
        for lo, hi in ((0.5, 2), (2, 4), (4, 6), (6, 7.6), (7.6, 9)):
            m = regs['xaxis'] & (xm >= lo) & (xm < hi); xb['%g-%g' % (lo, hi)] = float(dJ[m].sum())
        res.append(dict(theta0=float(t0), J_end=float(J[-1]), tau_end=float(T), regions=acc, yaxis_bands=yb, xaxis_bands=xb,
                        x_at_y=[float(np.interp(v, y[::-1], x[::-1])) if y.min() < v < y.max() else None for v in (10, 5, 2, 1)]))
        print(json.dumps(res[-1]), flush=True)
    json.dump(res, open(outp, 'w'), indent=1)


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), [float(v) for v in sys.argv[4].split(',')], sys.argv[5])
