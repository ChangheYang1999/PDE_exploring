"""J split by angular frequency band of R (VERIFY_REPORT G70 (b)), verifier.
Same evaluation, splines and integrator as vchar_dense.run (code/vchar_dense.py). J is linear in R along a fixed path,
so with R = sum_b R_b (R_b: the part of the sine series of R(r, .) with k in band b, by FFT on the evaluation circle)
J = sum_b J_b, J_b = int (R_b / rho)(Phi_t X0) dt, integrated on the same characteristic (the paths use W only).
Bands relative to Ktop = twice the largest angular index of the shape basis, as code/vq0band.py:
  low [1, Ktop/2), mid [Ktop/2, Ktop - 40), top [Ktop - 40, Ktop + 40), high [Ktop + 40, Nt/2].
Start set: n_win angles uniform in [t_lo, t_hi] (family A window) and n_geo angles pi/2 - delta, delta geometric in
[1e-4, 0.02) (family B). One tolerance (rtol 1e-10); J at eps 0.03 and 0.01; check sum_b J_b - J.
Usage: python3 vjband.py field.npz Mmax Ktop r_start n_win t_lo t_hi n_geo out.json
"""
import sys, os, json, warnings
warnings.simplefilter("ignore")
import numpy as np
from scipy.interpolate import RectBivariateSpline
from scipy.integrate import solve_ivp
from vcand import main as vcand_main, load_modes
from vb3 import find_xstar
from vchar import half_shift

BANDS = ('low', 'mid', 'top', 'high')


def run(path, Mmax, Ktop, r_start, n_win, t_lo, t_hi, n_geo, outp, epsl=(0.03, 0.01)):
    out, ev, ax = vcand_main(path, dict({'Mmax': Mmax, 'b3': False}, **json.loads(os.environ.get('VCHAR_CFG', '{}'))))
    d, g, ms, F = load_modes(path, Mmax)
    r = g.r
    Nt = out['Nt']
    th = 2 * np.pi * np.arange(Nt) / Nt
    cl = ev.c_l
    keep = r < max(3 * r_start, 60.0)
    rho = F @ np.sin(np.outer(ms, th))
    hr = half_shift(rho, Nt)
    Rhat = np.fft.rfft(ev.R, axis=1)
    kk = np.arange(Rhat.shape[1])
    lims = dict(low=(1, Ktop // 2), mid=(Ktop // 2, Ktop - 40), top=(Ktop - 40, Ktop + 40), high=(Ktop + 40, Nt // 2 + 1))
    qs = [half_shift(ev.R, Nt) / hr]
    for b in BANDS:
        lo, hi = lims[b]
        Rb = np.fft.irfft(Rhat * ((kk >= lo) & (kk < hi))[None, :], n=Nt, axis=1)
        qs.append(half_shift(Rb, Nt) / hr)
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
    sW1 = RectBivariateSpline(lr, t1, W1w, kx=5, ky=5)
    sW2 = RectBivariateSpline(lr, t1, W2w, kx=5, ky=5)
    sq = []
    for qq in qs:
        t2, qw = window(thm, qq)
        sq.append(RectBivariateSpline(lr, t2, qw, kx=5, ky=5))
    xs = find_xstar(np.asarray(ax['x']), np.asarray(ax['w']))

    def rhs(tau, Z):
        l, t = np.log(np.hypot(Z[0], Z[1])), np.arctan2(Z[1], Z[0])
        return [-float(sW1.ev(l, t)), -float(sW2.ev(l, t))] + [float(s.ev(l, t)) for s in sq]
    evs = []
    for e in epsl:
        f = (lambda e_: (lambda tau, Z: np.hypot(Z[0] - xs, Z[1]) - e_))(e)
        f.terminal = (e == epsl[-1])
        f.direction = -1
        evs.append(f)
    A = np.linspace(t_lo, t_hi, n_win)
    geo = np.geomspace(1e-4, 0.02, n_geo + 1)[:-1] if n_geo > 0 else np.zeros(0)
    starts = [('A', t) for t in A] + [('B', np.pi / 2 - dl) for dl in geo]
    rows = []
    for fam, t0 in starts:
        Z0 = [r_start * np.cos(t0), r_start * np.sin(t0)] + [0.0] * len(sq)
        sol = solve_ivp(rhs, (0, 300), Z0, method='DOP853', events=evs, rtol=1e-10, atol=1e-12, max_step=0.05)
        Jv = [[float(v) for v in ye[0][2:]] if len(ye) else [float('nan')] * len(sq) for ye in sol.y_events]
        xx, yy = sol.y[0], sol.y[1]
        k = np.nonzero((xx[:-1] - (xs - 1)) * (xx[1:] - (xs - 1)) < 0)[0]
        ycross = float(yy[k[-1]]) if len(k) else float('nan')
        rw = dict(fam=fam, theta0=float(t0), ycross=ycross, rmin=float(np.hypot(xx, yy).min()))
        for i, e in enumerate(epsl):
            rw['%g' % e] = dict(J=Jv[i][0], **{b: Jv[i][1 + j] for j, b in enumerate(BANDS)},
                                sumcheck=float(sum(Jv[i][1:]) - Jv[i][0]))
        rows.append(rw)
        e0 = rw['%g' % epsl[0]]
        print('%s %.7f rmin %.3g ycross %.3g | J %+.4e = low %+.3e mid %+.3e top %+.3e high %+.2e (sum-J %.1e)'
              % (fam, t0, rw['rmin'], ycross, e0['J'], e0['low'], e0['mid'], e0['top'], e0['high'], e0['sumcheck']), flush=True)
    summ = dict(file=path, Mmax=Mmax, Ktop=Ktop, bands={b: list(lims[b]) for b in BANDS}, r_start=r_start, c_l=cl, x_star=xs,
                window=[t_lo, t_hi, n_win], n_geo=n_geo, ranges={})
    for e in epsl:
        for fam in ('A', 'B', 'all'):
            sel = [rw for rw in rows if fam == 'all' or rw['fam'] == fam]
            summ['ranges']['%s_%g' % (fam, e)] = {c: [float(np.nanmin([rw['%g' % e][c] for rw in sel])),
                                                      float(np.nanmax([rw['%g' % e][c] for rw in sel]))]
                                                  for c in ('J',) + BANDS}
    print(json.dumps(summ, indent=1))
    json.dump(dict(summary=summ, rows=rows), open(outp, 'w'), indent=1, default=float)


if __name__ == '__main__':
    a = sys.argv
    run(a[1], int(a[2]), int(a[3]), float(a[4]), int(a[5]), float(a[6]), float(a[7]), int(a[8]), a[9])
