"""Spectral resolvedness and local regularity of the softest exact-action Ritz directions (18:50Z).
For the k softest Ritz vectors of runs/ritz_<tag>.pt (columns of Wv, softest last) at their state:
 (1) the 2D spectral coefficients of delta b (Chebyshev in q, index n = 0..N; cos(2 m s) in the mapped angle, m = 0..M-1): energy fractions in
     the upper third of the radial and of the angular index ranges, and the decay rate (least-squares slope of log shell energy against index
     over the upper half) -- compared with the state's own b - 1 (a resolved function on this grid) and with a random vector (unresolved);
 (2) the same for the physical relative variation delta b / b (nodal) and for the weighted variation (1 - q) delta b / b;
 (3) local behaviour near P = (x*, 0): energy fraction of delta b within |X - P| < 2 and < 0.5 (node weights: plain node count), the
     axis profile delta b(x, theta = 0) for x in x* + [-3, 3], second differences along the axis at h = 1, 0.5, 0.25 (interpolant level),
     the transverse profile at x = x*, and the location of max |delta b|.
Usage: python3 src/soft_smoothness.py runs/ritz_<tag>.pt tag [k=6] [xstar]"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn

LANE = '.'


def cheb_vander(q):
    x = np.clip(2.0 * np.asarray(q) - 1.0, -1, 1); N = len(q) - 1
    return np.cos(np.outer(np.arccos(x), np.arange(N + 1)))


def spectrum(V, Tinv, A):
    """V (N+1, M) nodal values -> coefficients a[n, m] (Chebyshev n in q, cos(2 m s) m)."""
    Cang = V @ A.T          # (N+1, M) angular coefficients at each radius
    return Tinv @ Cang      # (N+1, M)


def decay_stats(a):
    N1, M = a.shape; e = a ** 2; tot = e.sum() + 1e-300
    en = e.sum(1); em = e.sum(0)
    n_hi = int(np.ceil(2 * (N1 - 1) / 3)); m_hi = int(np.ceil(2 * M / 3))
    fr_n = en[n_hi:].sum() / tot; fr_m = em[m_hi:].sum() / tot
    # slopes over the upper half (log10 energy per index)
    def slope(ev):
        k = np.arange(len(ev)); sel = k >= len(ev) // 2; y = np.log10(ev[sel] + 1e-300); x = k[sel]
        return float(np.polyfit(x, y, 1)[0])
    # last-third to first-third ratio of mean shell energy
    r_n = en[n_hi:].mean() / (en[:N1 // 3].mean() + 1e-300); r_m = em[m_hi:].mean() / (em[:M // 3].mean() + 1e-300)
    return dict(frac_radial_upper_third=float(fr_n), frac_angular_upper_third=float(fr_m), slope_radial=slope(en), slope_angular=slope(em),
                ratio_radial_hi_lo=float(r_n), ratio_angular_hi_lo=float(r_m), last_radial_shell=float(en[-1] / tot), last_angular_shell=float(em[-1] / tot))


def main():
    rpath, tag = sys.argv[1], sys.argv[2]; k = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    R = torch.load(rpath); Wv = R['Wv'].double().cpu().numpy(); kk = Wv.shape[1]; spath = R['state']
    model, x, d = ipn.load_state(spath, device='cpu'); N, M = model.N, model.M
    b, cl = model.unpack(x); b = b.numpy(); cl = float(cl)
    xstar = float(sys.argv[4]) if len(sys.argv) > 4 else None
    if xstar is None:
        s4 = f'{LANE}/runs/s4e_{os.path.basename(spath).replace(".npz", "")}.json'
        xstar = float(json.load(open(s4))['xstar']) if os.path.exists(s4) else 8.5774
    q = model.q_np; T = cheb_vander(q); Tinv = np.linalg.inv(T); A = model.ang.A['EE'].cpu().numpy()
    r, w, v = model.radii(cl); th = model.ang.theta_np
    rr = np.repeat(r[1:], M); tt = np.tile(th, N); X = rr * np.cos(tt); Y = rr * np.sin(tt); dP = np.hypot(X - xstar, Y)
    out = dict(tag=tag, state=spath, N=N, M=M, L=model.L, c_l=cl, xstar=xstar, modes=[], refs={})

    def analyse(V, name, dcl=0.0, dC=0.0):
        V = np.asarray(V, float); V0 = V.copy(); V0[0, :] = 0.0
        res = dict(name=name, dcl=dcl, dC=dC)
        res['delta_b'] = decay_stats(spectrum(V0, Tinv, A))
        with np.errstate(divide='ignore', invalid='ignore'):
            rel = np.where(np.abs(b) > 1e-300, V0 / b, 0.0)
        res['delta_b_over_b'] = decay_stats(spectrum(rel, Tinv, A))
        res['weighted_(1-q)_delta_b_over_b'] = decay_stats(spectrum((1.0 - q)[:, None] * rel, Tinv, A))
        vv = V0[1:].ravel(); tot = (vv ** 2).sum() + 1e-300
        res['energy_frac_near_P'] = dict(d_lt_2=float((vv[dP < 2] ** 2).sum() / tot), d_lt_0p5=float((vv[dP < 0.5] ** 2).sum() / tot),
                                         r_lt_1=float((vv[rr < 1] ** 2).sum() / tot), r_1_100=float((vv[(rr >= 1) & (rr < 100)] ** 2).sum() / tot), r_ge_100=float((vv[rr >= 100] ** 2).sum() / tot))
        imax = int(np.argmax(np.abs(vv))); res['argmax'] = dict(r=float(rr[imax]), theta_deg=float(np.degrees(tt[imax])), value=float(vv[imax]))
        # axis profile and second differences at P
        xs = xstar + np.linspace(-3, 3, 61); qq = model.q_of_r(xs, cl)
        prof = model.eval_EE(V0, qq, np.zeros_like(qq)); res['axis_profile_x'] = xs.tolist(); res['axis_profile'] = prof.tolist()
        f = lambda xx: model.eval_EE(V0, model.q_of_r(np.atleast_1d(xx), cl), np.zeros(np.size(xx)))
        sup = np.abs(prof).max() + 1e-300; d2 = {}
        for h in (1.0, 0.5, 0.25, 0.125):
            d2[str(h)] = float((f(xstar + h) - 2 * f(xstar) + f(xstar - h))[0] / h ** 2 / sup)
        res['axis_second_diff_over_sup'] = d2
        # transverse profile at x = x*
        ths = np.linspace(0, 0.3, 13); rs = xstar / np.cos(ths)
        res['transverse_theta'] = ths.tolist(); res['transverse_profile'] = model.eval_EE(V0, model.q_of_r(rs, cl), ths).tolist()
        # also the state's own b second differences for comparison are in refs
        return res

    def line(res):
        s1 = res['delta_b']; s2 = res['delta_b_over_b']; e = res['energy_frac_near_P']
        return (f"{res['name']:>14s} dc_l {res['dcl']:+.2e} dC {res['dC']:+.2e} | delta b: hi-third radial {s1['frac_radial_upper_third']:.3f} angular {s1['frac_angular_upper_third']:.3f} "
                f"slopes {s1['slope_radial']:+.3f} {s1['slope_angular']:+.3f} last shells {s1['last_radial_shell']:.1e} {s1['last_angular_shell']:.1e} | delta b/b: hi-third {s2['frac_radial_upper_third']:.3f} {s2['frac_angular_upper_third']:.3f} "
                f"| near P: d<2 {e['d_lt_2']:.3f} d<0.5 {e['d_lt_0p5']:.3f}; r<1 {e['r_lt_1']:.2f} 1..100 {e['r_1_100']:.2f} >100 {e['r_ge_100']:.2f} | argmax r {res['argmax']['r']:.2f} th {res['argmax']['theta_deg']:.1f} "
                f"| axis d2/sup h=1,.5,.25,.125: " + ' '.join(f"{res['axis_second_diff_over_sup'][h]:+.2f}" for h in ('1.0', '0.5', '0.25', '0.125')))

    print(f'{tag}: state {spath} (N,M,L) = ({N},{M},{model.L}) c_l {cl:.10f} x* {xstar:.6f}; Ritz file {rpath} ({kk} columns)')
    for i in range(min(k, kk)):
        vfull = Wv[:, kk - 1 - i]; vfull = vfull / np.linalg.norm(vfull)
        V = np.zeros((N + 1, M)); V[1:] = vfull[:N * M].reshape(N, M)
        res = analyse(V, f'ritz{i}', float(vfull[-2]), float(vfull[-1])); out['modes'].append(res); print(line(res), flush=True)
    # references: the state b - 1 (resolved), a random vector (unresolved), the smooth generic direction used by ritz_subspace is not stored
    Vb = b.copy(); Vb[0, :] = 0.0; Vb[1:] -= 1.0
    rb = analyse(Vb, 'state b-1'); out['refs']['state_b_minus_1'] = rb; print(line(rb))
    rng = np.random.default_rng(0); Vr = np.zeros((N + 1, M)); Vr[1:] = rng.standard_normal((N, M))
    rr_ = analyse(Vr, 'random'); out['refs']['random'] = rr_; print(line(rr_))
    # a smooth test direction: delta b = (1 - q) q cos(2 s) * b  (resolved by construction)
    sj = model.ang.s_np; Vs = np.outer((1 - q) * q, np.cos(2 * sj)) * b; Vs[0, :] = 0.0
    rs_ = analyse(Vs, 'smooth test'); out['refs']['smooth_test'] = rs_; print(line(rs_))
    json.dump(out, open(f'{LANE}/runs/smooth_{tag}.json', 'w'), indent=1); print(f'saved runs/smooth_{tag}.json')


if __name__ == '__main__':
    main()
