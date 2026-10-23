"""Sensitivity of the between-node far-field residual of the saved hydrostatic trial states to the inner quadrature of the inverse (default hs.hydro_V inner rule
n_in Gauss points on [0, y], used by sampled_table with n_in = 32 and by the solver maps with n_in = 24, versus the core-resolving rule hs_layer.hydro_V_log).
Points: radial midpoints of the Radau grid with r >= 100 x (angular midpoints + axis angles), as in hs_solve.sampled_table.  Diagnostic of the evaluator, 12:xxZ."""
import sys, numpy as np, torch
sys.path.insert(0, 'src'); import hs_solve, hs, hs_layer
torch.set_default_dtype(torch.float64)
RMIN = [a.split('=')[1] for a in sys.argv[1:] if a.startswith('rmin=')]; RMIN = RMIN[0] if RMIN else '100'
for f in [a for a in sys.argv[1:] if not a.startswith('rmin=')]:
    st = torch.load(f, weights_only=False); N, M, c = st['N'], st['M'], st['c']; P = st.get('map_exponent_P', st.get('p')); c_map = P / (P - 1)
    hsm = hs_solve.HSModel(N, M, c_map, n_in=4, n_tail=4); m = hsm.m; u = st['u'].to(m.dev); tag = f.split('/')[-1][:-3]
    tR = m.rad.tR_np; tm = 0.5 * (tR[:-1] + tR[1:]); th = m.ang.theta_np; thm = 0.5 * (th[:-1] + th[1:]); thm = np.sort(np.concatenate([thm, [th[0] / 4, th[0] / 2, (th[-1] + np.pi / 2) / 2, np.pi / 2]]))
    rm = m.rad.rmap_np(torch.tensor(tm)).numpy(); rm = rm[rm >= float(RMIN)]; RR, TT = np.meshgrid(rm, thm, indexing='ij'); X = (RR * np.cos(TT)).reshape(-1); Y = (RR * np.sin(TT)).reshape(-1)
    ge = hs.GEval(m, m.beta_full(u)); g, gx, gy = ge(X, Y)
    out = {}
    for name, (V1, V2) in [('n_in32', hs.hydro_V(ge, X, Y, n_in=32, n_tail=100, hrel=1e-5, hstep='r')), ('n_in24_t80', hs.hydro_V(ge, X, Y, n_in=24, n_tail=80, hrel=1e-5, hstep='r')),
                           ('n_in1024', hs.hydro_V(ge, X, Y, n_in=1024, n_tail=400, hrel=1e-5, hstep='r')), ('log', hs_layer.hydro_V_log(ge, X, Y))]:
        R = (c * X + V1) * gx + (c * Y + V2) * gy - g; Nf = np.abs((c * X + V1) * gx) + np.abs((c * Y + V2) * gy) + np.abs(g); out[name] = (R, Nf, V2)
    Rl, Nfl, V2l = out['log']
    print(f"{tag} {N}x{M} c {c}: {len(X)} points with r >= {RMIN} (r up to {RR.max():.1e}); max |R|/N_f: " + ", ".join(f"{k} {np.abs(v[0] / v[1]).max():.3e}" for k, v in out.items())
          + ";  max |V2 - V2_log|: " + ", ".join(f"{k} {np.abs(v[2] - V2l).max():.2e}" for k, v in out.items() if k != 'log')
          + ";  max |R/N_f - (R/N_f)_log|: " + ", ".join(f"{k} {np.abs(v[0] / v[1] - Rl / Nfl).max():.2e}" for k, v in out.items() if k != 'log')
          + f";  by region (log rule / n_in32): " + ", ".join(f"[{lo:.0e},{hi:.0e}) {np.abs(Rl / Nfl)[(RR.reshape(-1) >= lo) & (RR.reshape(-1) < hi)].max():.2e} / {np.abs(out['n_in32'][0] / out['n_in32'][1])[(RR.reshape(-1) >= lo) & (RR.reshape(-1) < hi)].max():.2e}" for lo, hi in [(0.1, 1), (1, 100), (1e2, 1e3), (1e3, 1e4), (1e4, 1e5), (1e5, 1e300)] if ((RR.reshape(-1) >= lo) & (RR.reshape(-1) < hi)).any()), flush=True)
