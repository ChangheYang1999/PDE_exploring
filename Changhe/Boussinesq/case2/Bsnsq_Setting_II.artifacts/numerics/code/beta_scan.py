"""Fixed-coefficient beta scan of a saved least-squares state : rebuild the state's objective from its saved settings (as in
stationarity.py: beta_map, Rw, w_origin, tail rows and t1; states with ypen/pres/patch rows are refused) with beta as an explicit variable,
hold the Chebyshev-Fourier coefficients ca, cG fixed at their stored values, and evaluate the residual vector F(ca, cG, beta) for beta on a grid
around the stored value. The t-map basis and its prefactors use beta_map (the stored map exponent), so only the equations change with beta:
the standard rows (weighted R_a, R_G at the collocation nodes), the three origin rows w_origin (2 beta - c + 2) a_0, w_origin ((2 beta + 1) G_0
- 2 a_0), w_origin (a_0 - target) and the tail rows (first-tail matching at t1, evaluated with the current beta). The origin rows depend on
beta explicitly (d/dbeta = 2 w_origin a_0 and 2 w_origin G_0 at fixed coefficients), so they dominate any fixed-coefficient scan; the groups
are therefore reported separately, and the central-difference derivative d|F_group|^2/dbeta at the stored beta is printed per group.
This is a model quantity of the fitted objective at fixed coefficients (no re-optimization); nothing here concerns profiles.
Usage: python3 -u code/beta_scan.py state1.npz [state2.npz ...]"""
import sys, json, ast, numpy as np, torch
sys.path.insert(0, 'code')
import lm_solve as L

DELTAS = [-0.10, -0.06, -0.04, -0.02, -0.01, -0.005, -0.001, 0.0, 0.001, 0.005, 0.01, 0.02, 0.04, 0.06, 0.10]

def build(d):
    extra = d['extra'].item() if 'extra' in d else {}
    if isinstance(extra, bytes): extra = extra.decode()
    if isinstance(extra, str):
        try: extra = json.loads(extra)
        except Exception:
            try: extra = ast.literal_eval(extra)
            except Exception: extra = {}
    if not isinstance(extra, dict): extra = {}
    if extra.get('ypen') or extra.get('pres'): raise SystemExit('state fitted with ypen/pres rows: not handled')
    patch = np.array(d['patch']).tolist() if 'patch' in d else extra.get('patch')
    if patch is not None and len(patch) == 4 and any(float(v) != 0.0 for v in patch): raise SystemExit('state fitted with patch rows: not handled')
    mapname = str(d['mapname']) if 'mapname' in d else 'xi'
    N, M, Ld = int(d['N']), int(d['M']), float(d['L']); ov = float(d['Ne']) / N
    beta = float(d['beta']); beta_map = float(d['beta_map']) if 'beta_map' in d else beta
    tail = float(d['tail']) if 'tail' in d else float(extra.get('tail') or 0.0); tail = tail if tail > 0 else None
    t1 = float(d['t1']) if 't1' in d else float(extra.get('t1', 1e-5))
    wmax = float(d['wmax']) if ('wmax' in d and float(d['wmax']) > 0) else None
    prob = L.LMProblem(N, M, Ld, beta_map, float(d['sigma_a']), float(d['sigma_G']), float(d['a0_target']),
                       float(d['w_origin']) if 'w_origin' in d else 3.0, None, ov=ov, mapname=mapname,
                       Rw=float(d['Rw']) if 'Rw' in d else 30.0, wmax=wmax, tail=tail, t1=t1)
    z = prob.pack(torch.tensor(d['ca'], dtype=L.DT, device=L.dev), torch.tensor(d['cG'], dtype=L.DT, device=L.dev), beta)
    return prob, z, beta, beta_map, tail, t1

def groups(prob, F):
    n_std = 2 * prob.Ne * prob.Me
    g = {'std': F[:n_std], 'origin': F[n_std:n_std + 3]}
    if prob.tail is not None: g['tail'] = F[n_std + 3:n_std + 3 + 2 * prob.Me]
    g['all'] = F; g['all_minus_origin'] = torch.cat([F[:n_std], F[n_std + 3:]])
    return {k: float(v.norm()) for k, v in g.items()}

def main(paths):
    for p in paths:
        d = L.load_state(p); name = p.split('/')[-1].replace('.npz', '')
        prob, z, beta, beta_map, tail, t1 = build(d)
        hist = json.loads(str(d['hist'])) if 'hist' in d else []
        Fst = hist[-1]['Fnorm'] if hist else float('nan')
        with torch.no_grad():
            F0 = prob.F(z); g0 = groups(prob, F0)
        print(f"state {name}: N={prob.N} M={prob.M} beta_stored={beta:.6f} beta_map={beta_map:.6f} tail={tail} t1={t1} rows={F0.numel()} (std {2*prob.Ne*prob.Me}, origin 3, tail {2*prob.Me if tail else 0})")
        print(f"  |F| rebuilt {g0['all']:.6e} stored {Fst:.6e}; group norms at stored beta: std {g0['std']:.6e} origin {g0['origin']:.3e} tail {g0.get('tail', float('nan')):.6e} all_minus_origin {g0['all_minus_origin']:.6e}")
        print(f"  {'beta':>10s} {'delta':>8s} {'|F_all|':>12s} {'|F_std|':>12s} {'|F_origin|':>12s} {'|F_tail|':>12s} {'|F_all-orig|':>12s}  ratios to stored-beta values: std, tail, all_minus_origin")
        rows = {}
        for dl in DELTAS:
            zz = z.clone(); zz[-1] = beta + dl
            with torch.no_grad():
                g = groups(prob, prob.F(zz))
            rows[dl] = g
            print(f"  {beta+dl:10.6f} {dl:+8.3f} {g['all']:12.6e} {g['std']:12.6e} {g['origin']:12.3e} {g.get('tail', float('nan')):12.6e} {g['all_minus_origin']:12.6e}  {g['std']/g0['std']:.6f} {g.get('tail', float('nan'))/g0.get('tail', 1.0):.6f} {g['all_minus_origin']/g0['all_minus_origin']:.6f}")
        for h in (0.001, 0.005, 0.01):
            gp, gm = rows[h], rows[-h]
            der = {k: (gp[k] ** 2 - gm[k] ** 2) / (2 * h) for k in gp}
            print(f"  central-difference d|F_group|^2/dbeta at beta={beta:.6f} (h={h}): all {der['all']:+.4e} std {der['std']:+.4e} origin {der['origin']:+.4e} tail {der.get('tail', float('nan')):+.4e} all_minus_origin {der['all_minus_origin']:+.4e}")
        # minimizer of the quadratic fit of |F_all_minus_origin|^2 over the three central points (model quantity)
        f = lambda dl: rows[dl]['all_minus_origin'] ** 2
        a2 = (f(0.01) - 2 * f(0.0) + f(-0.01)) / (0.01 ** 2); a1 = (f(0.01) - f(-0.01)) / 0.02
        if a2 > 0: print(f"  quadratic model of |F_all_minus_origin|^2 through delta = -0.01, 0, 0.01: curvature {a2:.4e} > 0, stationary point at delta = {-a1/a2:+.5f} (beta = {beta - a1/a2:.6f}); fixed-coefficient model only")
        else: print(f"  quadratic model of |F_all_minus_origin|^2 through delta = -0.01, 0, 0.01: curvature {a2:.4e} <= 0 (no interior minimum of the model on this stencil)")
        sys.stdout.flush()

if __name__ == '__main__':
    main(sys.argv[1:])
