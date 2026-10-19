"""Verifier's combined audit of one field export (verifier). One evaluation (vcand.main: own inverse, own c and c_l from
the identity, own derivatives; only the sampled rho is read), then
  1. transport residual R in two normalizations, first quadrant, axis points excluded:
       N_v = |rho| + |X.grad rho| + |U.grad rho|        (vcand, vresid)
       N_f = |W_1 rho_x| + |W_2 rho_y| + |rho|          (Cartesian flux, lead construct4 REPORT)
     max and plain sample RMS of |R|/N by physical band and in regions around P = (x*, 0);
  2. the characteristic defect J (vchar.run_ev);
  3. x-axis traces from the same inverse (vb3w.w_traces with the evaluation's p_n, p_n') and the integrated-by-parts
     B_3 (vb3ibp), both w'' routes.
Usage: python3 vaudit.py field.npz Mmax out.json [r_start n_theta [vcand cfg json, e.g. '{"k_far": 0.189}']]
(2026-10-18 03:4xZ: optional vcand cfg added; default behaviour unchanged, backup vaudit_pre_kfar.py)
"""
import sys, json, time, warnings
warnings.simplefilter("ignore")
import numpy as np
from vcand import main as vcand_main, load_modes
import vchar
import vb3w
import vb3ibp


def residual_tables(ev, g, th, rho, xs, cl):
    r = g.r
    R2 = r[:, None]
    ct, st = np.cos(th)[None, :], np.sin(th)[None, :]
    rx = ct * ev.rho_r - st * ev.rho_t / R2
    ry = st * ev.rho_r + ct * ev.rho_t / R2
    U1 = ev.Ur * ct - ev.Ut * st
    U2 = ev.Ur * st + ev.Ut * ct
    X1, X2 = R2 * ct, R2 * st
    W1, W2 = cl * X1 + U1, cl * X2 + U2
    Nf = np.abs(W1 * rx) + np.abs(W2 * ry) + np.abs(rho)
    Nv = ev.Rnorm
    Nt = len(th)
    q = np.zeros(Nt, bool)
    q[1:Nt // 4] = True                                   # open first quadrant: no axis point
    trim = 8
    rr = np.zeros(len(r), bool)
    rr[trim:-trim] = True
    dist = np.hypot(X1 - xs, X2)
    regs = [('r<=0.1', (R2 <= 0.1)), ('0.1<=r<=2', (R2 >= 0.1) & (R2 <= 2)), ('2<=r<=10', (R2 >= 2) & (R2 <= 10)),
            ('10<=r<=100', (R2 >= 10) & (R2 <= 100)), ('100<=r<=1000', (R2 >= 100) & (R2 <= 1000)),
            ('1000<=r<=R', R2 >= 1000), ('|X-P|<0.5', dist < 0.5), ('|X-P|<2', dist < 2), ('|X-P|<4', dist < 4),
            ('|xi|<=3,y<=4', (np.abs(X1 - xs) <= 3) & (X2 <= 4)), ('all', R2 > 0)]
    ya = (np.pi / 2 - th)[None, :] >= 0.006               # 2026-10-18T14:51Z: A5 of G67 (g), the y-axis floor columns excluded
    regs += [('all,ya>=0.006', (R2 > 0) & ya), ('r<=1000,ya>=0.006', (R2 <= 1000) & ya), ('r>1000,ya>=0.006', (R2 > 1000) & ya)]
    import os
    if os.environ.get('VAUDIT_RFIT'):                     # fit radius (physical) of a bounded-domain fit, e.g. construct5
        Rf = float(os.environ['VAUDIT_RFIT'])
        regs += [('10<=r<=Rfit', (R2 >= 10) & (R2 <= Rf)), ('r<=Rfit', R2 <= Rf), ('r>Rfit', R2 > Rf)]
        if Rf > 1000:                                     # 2026-10-18T13:56Z: far band inside the fit radius (lead r >= 1000 scan band)
            regs += [('1000<=r<=Rfit', (R2 >= 1000) & (R2 <= Rf)),
                     ('1000<=r<=Rfit,ya>=0.006', (R2 >= 1000) & (R2 <= Rf) & ya), ('r>Rfit,ya>=0.006', (R2 > Rf) & ya)]
    out = []
    for name, m in regs:
        m = np.broadcast_to(m, rho.shape) & q[None, :] & rr[:, None]
        if m.sum() == 0:
            continue
        a = np.abs(ev.R[m])
        ef = a / Nf[m]
        evv = a / Nv[m]
        i = int(np.argmax(ef)); iv = int(np.argmax(evv))
        ii, jj = np.nonzero(m)
        out.append(dict(region=name, n=int(m.sum()), flux_max=float(ef.max()), flux_rms=float(np.sqrt(np.mean(ef ** 2))),
                        Nv_max=float(evv.max()), Nv_rms=float(np.sqrt(np.mean(evv ** 2))),
                        flux_argmax_r=float(r[ii[i]]), flux_argmax_theta=float(th[jj[i]]),
                        abs_max=float(a.max()), Nv_argmax_r=float(r[ii[iv]]), Nv_argmax_theta=float(th[jj[iv]])))
    return out


def main(path, Mmax, outp, r_start=20.0, nth=24, extra=None):
    t0 = time.time()
    cfg = {'Mmax': Mmax, 'b3': False}
    cfg.update(extra or {})
    out, ev, ax = vcand_main(path, cfg)
    d, g, ms, F = load_modes(path, Mmax)
    Nt = out['Nt']
    th = 2 * np.pi * np.arange(Nt) / Nt
    rho = F @ np.sin(np.outer(ms, th))
    res = dict(vcand=out, t_eval=time.time() - t0)
    xs, cl = out['x_star'], ev.c_l
    res['residual'] = residual_tables(ev, g, th, rho, xs, cl)
    print(json.dumps(dict(file=path, Mmax=Mmax, c_l=cl, x_star=xs, hP=out.get('hP'), regions=out['regions'])), flush=True)
    for rw in res['residual']:
        print('  %-14s flux max %.3e rms %.3e | N_v max %.3e rms %.3e | at r %.4g th %.4f' % (
            rw['region'], rw['flux_max'], rw['flux_rms'], rw['Nv_max'], rw['Nv_rms'], rw['flux_argmax_r'],
            rw['flux_argmax_theta']), flush=True)
    # axis traces from the same inverse, IBP B_3
    ns = np.array(sorted(ev.pm))
    P = np.array([ev.pm[n][0] for n in ns])
    dP = np.array([ev.pm[n][1] for n in ns])
    tr = vb3w.w_traces(g, F, ms, P, dP, ns, cl)
    sel = tr['x'] < 60
    res['B3'] = {}
    for key in ('wpp_ode', 'wpp_fd'):
        try:
            bd = vb3ibp.build(tr['x'][sel], tr['w'][sel], tr['wp'][sel], tr[key][sel], cl)
            s, rows = vb3ibp.b3_variants(bd, path + ' ' + key)
            res['B3'][key] = dict(summary=s, rows=rows)
            print('B3 %s ibp %.4f [%.4f, %.4f] orig %.4f [%.4f, %.4f] fit %.1e x* %.6f' % (
                key, s['ibp_median'], s['ibp_min'], s['ibp_max'], s['orig_median'], s['orig_min'], s['orig_max'],
                s['worst_fit'], s['x_star']), flush=True)
        except Exception as e:
            res['B3'][key] = 'failed: %r' % e
            print('B3 %s failed %r' % (key, e), flush=True)
    # characteristic defect
    summ, rows = vchar.run_ev(out, ev, ax, g, ms, F, r_start, nth)
    res['char'] = dict(summary=summ, rows=rows)
    print('J at |X - P| = %s: spread %s  Jmin %s  Jmax %s' % (
        ' '.join('%g' % v for v in summ['eps_P']), ' '.join('%.3e' % v for v in summ['spread']),
        ' '.join('%+.3e' % v for v in summ['Jmin']), ' '.join('%+.3e' % v for v in summ['Jmax'])), flush=True)
    print('J spread, interior start angles: ' + ' '.join('%.3e' % v for v in summ['spread_interior']), flush=True)
    print('J increments per shell %s: mean %s | spread all %s | spread interior %s' % (
        ' '.join(summ['shells']), ' '.join('%+.2e' % v for v in summ['shell_mean']),
        ' '.join('%.2e' % v for v in summ['shell_spread_all']),
        ' '.join('%.2e' % v for v in summ['shell_spread_interior'])), flush=True)
    print('q above P (y = 1e-3, 1e-2, .1, .5, 1, 2): ' + ' '.join('%+.2e' % v for v in summ['q_above_P']), flush=True)
    res['t_total'] = time.time() - t0
    json.dump(res, open(outp, 'w'), indent=1, default=float)
    print('done in %.0f s' % res['t_total'], flush=True)


if __name__ == '__main__':
    a = sys.argv
    main(a[1], int(a[2]), a[3], float(a[4]) if len(a) > 4 else 20.0, int(a[5]) if len(a) > 5 else 24,
         json.loads(a[6]) if len(a) > 6 else None)
