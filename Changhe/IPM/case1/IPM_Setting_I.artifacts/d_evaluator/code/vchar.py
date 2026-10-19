"""Verifier's characteristic defect (lead analysis 13.4, notes 21:55Z), verifier.
  J(X0) = int_{-inf}^0 (R/rho)(X(s)) ds along the characteristic dX/ds = W(X) through X0 (backward to the source P),
  R = W.grad rho - rho, W = c_l X + U.
Independent of the lead's notes/char_defect/char_defect.py: R, U and c_l come from the verifier's evaluator (vcand.main on
the sampled rho only; the exporter's W, residual and axis data are not read). R/rho is formed on the half-shifted angular
grid by exact Fourier interpolation of the odd functions R and rho, so no axis point (0/0) is used; W on the regular grid.
Quintic tensor splines in (log r, theta) on theta in [-0.15, pi/2 + 0.15] (R/rho and W1 even/odd extensions are automatic
because the full circle is sampled). Backward integration in tau = -s by DOP853 with two tolerances; J is recorded when
|X - P| first reaches each of eps_P = 0.3, 0.1, 0.03, 0.01.
Usage: python3 vchar.py field.npz Mmax r_start n_theta out.json
"""
import sys, json, warnings
warnings.simplefilter("ignore")
import numpy as np
from scipy.interpolate import RectBivariateSpline
from scipy.integrate import solve_ivp
from vcand import main as vcand_main
from vb3 import find_xstar


def half_shift(f, Nt):
    G = np.fft.rfft(f, axis=1)
    k = np.arange(G.shape[1])
    ph = np.exp(1j * k * (np.pi / Nt))          # shift by half a step, dtheta/2 = pi/Nt
    if Nt % 2 == 0:
        G[:, -1] = 0.0                          # drop the Nyquist term (not representable after the shift)
    return np.fft.irfft(G * ph, n=Nt, axis=1)


def run(path, Mmax, r_start, nth, outp):
    out, ev, ax = vcand_main(path, {'Mmax': Mmax, 'b3': False})
    from vcand import load_modes
    d, g, ms, F = load_modes(path, Mmax)
    summ, rows = run_ev(out, ev, ax, g, ms, F, r_start, nth, verbose=True)
    summ.update(file=path, Mmax=Mmax)
    print(json.dumps(summ))
    json.dump(dict(summary=summ, rows=rows), open(outp, 'w'), indent=1, default=float)


def run_ev(out, ev, ax, g, ms, F, r_start, nth, verbose=False, epsl=(4.0, 2.0, 1.0, 0.3, 0.1, 0.03, 0.01)):
    """Characteristic defect from a finished evaluation (vcand.main output, its Evaluation and axis traces).
    J is recorded at the first inward crossing of each |X - P| = eps in epsl (decreasing); the summary also gives the
    increments of J per distance shell [eps_(i+1), eps_i) (first shell: d >= eps_0) and their spread over start angles,
    for all start angles and for the interior ones (first and last start angle, next to the axes, excluded)."""
    r = g.r
    Nt = out['Nt']
    th = 2 * np.pi * np.arange(Nt) / Nt
    cl = ev.c_l
    keep = r < max(3 * r_start, 60.0)
    rho = F @ np.sin(np.outer(ms, th))                # the evaluator's own synthesis of the sampled rho
    Rm = half_shift(ev.R, Nt)
    rm = half_shift(rho, Nt)
    q = Rm / rm
    thm = th + np.pi / Nt
    # W on the regular grid
    ct, st = np.cos(th)[None, :], np.sin(th)[None, :]
    U1 = ev.Ur * ct - ev.Ut * st
    U2 = ev.Ur * st + ev.Ut * ct
    X1, X2 = r[:, None] * ct, r[:, None] * st
    W1, W2 = cl * X1 + U1, cl * X2 + U2

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
    P = np.array([xs, 0.0])
    # R/rho next to P (from above) and the q range on the band around P
    qP = [float(sq.ev(np.log(np.hypot(xs, yy)), np.arctan2(yy, xs))) for yy in (1e-3, 1e-2, 0.1, 0.5, 1.0, 2.0)]

    def rhs(tau, Z):
        l, t = np.log(np.hypot(Z[0], Z[1])), np.arctan2(Z[1], Z[0])
        return [-float(sW1.ev(l, t)), -float(sW2.ev(l, t)), float(sq.ev(l, t))]
    evs = []
    for e in epsl:
        f = (lambda e_: (lambda tau, Z: np.hypot(Z[0] - xs, Z[1]) - e_))(e)
        f.terminal = (e == epsl[-1])
        f.direction = -1
        evs.append(f)
    rows = []
    for t0 in np.linspace(0.02, np.pi / 2 - 0.02, nth):
        Z0 = [r_start * np.cos(t0), r_start * np.sin(t0), 0.0]
        rec = {}
        for tol in (1e-9, 1e-11):
            sol = solve_ivp(rhs, (0, 300), Z0, method='DOP853', events=evs, rtol=tol, atol=tol * 1e-2, max_step=0.05)
            Js = [float(ye[0][2]) if len(ye) else float('nan') for ye in sol.y_events]
            taus = [float(te[0]) if len(te) else float('nan') for te in sol.t_events]
            # closest approach to the origin (characteristics passing by the stagnation point at 0)
            rmin = float(np.hypot(sol.y[0], sol.y[1]).min())
            rec[tol] = dict(J=Js, tau=taus, rmin=rmin, end=[float(sol.y[0, -1] - xs), float(sol.y[1, -1])])
        rows.append(dict(theta0=float(t0), J=rec[1e-11]['J'], tau=rec[1e-11]['tau'], rmin=rec[1e-11]['rmin'],
                         end=rec[1e-11]['end'], J_tol9_minus_tol11=[a - b for a, b in zip(rec[1e-9]['J'], rec[1e-11]['J'])]))
        if verbose:
            print('%.4f tau %7.3f rmin %.3g  J(eps .3, .1, .03, .01) %s  dtol %.1e' % (
                t0, rows[-1]['tau'][-1], rows[-1]['rmin'], ' '.join('%+.4e' % v for v in rows[-1]['J']),
                max(abs(v) for v in rows[-1]['J_tol9_minus_tol11'])), flush=True)
    J = np.array([rw['J'] for rw in rows])
    summ = dict(r_start=r_start, c_l=cl, x_star=xs, hP=out.get('hP'), q_above_P=qP,
                spread=[float(np.nanmax(J[:, i]) - np.nanmin(J[:, i])) for i in range(len(epsl))],
                Jmin=[float(np.nanmin(J[:, i])) for i in range(len(epsl))],
                Jmax=[float(np.nanmax(J[:, i])) for i in range(len(epsl))], eps_P=list(epsl))
    inc = np.diff(np.concatenate([np.zeros((J.shape[0], 1)), J], 1), axis=1)
    summ['shells'] = ['d>=%g' % epsl[0]] + ['[%g,%g)' % (epsl[i + 1], epsl[i]) for i in range(len(epsl) - 1)]
    summ['shell_spread_all'] = [float(np.nanmax(inc[:, i]) - np.nanmin(inc[:, i])) for i in range(len(epsl))]
    summ['shell_spread_interior'] = [float(np.nanmax(inc[1:-1, i]) - np.nanmin(inc[1:-1, i])) for i in range(len(epsl))]
    summ['shell_mean'] = [float(np.nanmean(inc[:, i])) for i in range(len(epsl))]
    summ['spread_interior'] = [float(np.nanmax(J[1:-1, i]) - np.nanmin(J[1:-1, i])) for i in range(len(epsl))]
    return summ, rows


if __name__ == '__main__':
    run(sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), sys.argv[5])
