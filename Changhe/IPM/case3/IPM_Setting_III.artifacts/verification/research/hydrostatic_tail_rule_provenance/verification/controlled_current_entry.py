"""
hs_node_check.py -- residual of a saved hydrostatic trial state AT ITS OWN COLLOCATION NODES, evaluated with the independent resolved evaluator
(hs.GEval for g, grad g; hs_layer.hydro_V_log for V_1, V_2: n0 32, 10 log panels per decade x 16 Gauss points, tail 400), i.e. the evaluator of the
between-node tables, compared with the solver's own node residual |F|max (computed from its precomputed quadrature maps: n0 24 Gauss on [0, min(1, y)],
log panels with 4 per decade x 8 points, tail 80 points, q = 3).  Referee referee cauchy2 claim 6: a node/between-node gap is only meaningful if the nodes
and the between-node points are evaluated with the same evaluator.  If the evaluator gives |R_h|/N_f ~ 1e-5 at the nodes where the maps give 1e-7, the
'between-node floor' is largely the quadrature error of the solver's maps, and the states are accurate solutions of a quadrature-perturbed discrete problem.
usage: python3 src/hs_node_check.py runs/state.pt [...]
"""
import sys, json, numpy as np, torch
sys.path.insert(0, 'numerics/src')
import hs, hs_solve, hs_layer
torch.set_default_dtype(torch.float64)

def main(files):
    for f in files:
        st = torch.load(f, weights_only=False); N, M, c = st['N'], st['M'], st['c']; P = st.get('map_exponent_P', st.get('p')); c_map = P / (P - 1)
        res0 = st.get('result') or {}; fine = bool(res0.get('fine', False)) or bool((st.get('inverse_options') or {}).get('fine', False))
        hsm = hs_solve.HSModel(N, M, c_map, n_in=4, n_tail=4, fine=fine); m = hsm.m; u = st['u'].to(m.dev)   # fine=True: the 3M oversampled angles are the solve rows (referee alias1)
        q_ref = int(__import__('os').environ.get('HS_Q', '2'))                                        # tail exponent of the reference evaluator (default 2 since 02:5xZ; the accurate maps use q = 2)
        X, Y = hsm.X, hsm.Y; R = np.hypot(X, Y); ge = hs.GEval(m, m.beta_full(u))
        V1 = np.zeros_like(X); V2 = np.zeros_like(X); CH = int(__import__("os").environ.get("HS_CH", "1500"))   # chunk of nodes per evaluator call (GPU memory; HS_CH=100 when the card is nearly full)
        for k0 in range(0, len(X), CH):
            sl = slice(k0, min(len(X), k0 + CH))
            if __import__('os').environ.get('HS_RULE', 'ref') == 'std':   # the solver's STANDARD map rule (24 Gauss on [0, min(1,y)], 4 log panels/decade x 8, 80-point tail, q = 3)
                v1, v2 = hs_layer.hydro_V_log(ge, X[sl], Y[sl], n0=24, per_decade=4, ngl=8, n_tail=80, q=3, hrel=1e-5, ymax_dec=np.log10(max(Y.max(), 10.0)))
            else:
                v1, v2 = hs_layer.hydro_V_log(ge, X[sl], Y[sl], n0=32, per_decade=10, ngl=16, n_tail=400, q=q_ref, hrel=1e-5, ymax_dec=np.log10(max(Y.max(), 10.0)))
            V1[sl] = np.asarray(v1).reshape(-1); V2[sl] = np.asarray(v2).reshape(-1)
        g, gx, gy = ge(X, Y)
        Rh = (c * X + V1) * gx + (c * Y + V2) * gy - g; Nf = np.abs((c * X + V1) * gx) + np.abs((c * Y + V2) * gy) + np.abs(g)
        res = st.get('result') or {}; nodeF = res.get('nodes_Fmax', float('nan'))
        rule = 'STANDARD-map rule (24, 4x8, 80, q=3)' if __import__('os').environ.get('HS_RULE', 'ref') == 'std' else f'resolved evaluator (32, 10x16, 400, q={q_ref})'
        rule += f"; rows: {'3M oversampled angles (fine)' if fine else 'M collocation angles'}" 
        print(f"{f.split('/')[-1]} {N}x{M} c={c}: solver node |F|max (maps) {nodeF:.3e};  {rule} AT THE SAME NODES ({len(X)} points):")
        for lo, hi in [(0, 0.1), (0.1, 1), (1, 100), (100, 1e300)]:
            msk = (R >= lo) & (R < hi)
            if msk.any(): print(f"   r in [{lo:g}, {hi:g}): max |R_h| {np.abs(Rh[msk]).max():.3e}   max |R_h|/N_f {(np.abs(Rh) / Nf)[msk].max():.3e}   max N_f {Nf[msk].max():.3e}   median |R_h|/N_f {np.median((np.abs(Rh) / Nf)[msk]):.2e}")
        # where is the maximum
        i = int(np.argmax(np.abs(Rh) / Nf)); print(f"   argmax |R_h|/N_f at (x, y) = ({X[i]:.4g}, {Y[i]:.4g}), r = {R[i]:.4g}, theta = {np.degrees(np.arctan2(Y[i], X[i])):.2f} deg; R_h {Rh[i]:.3e}, N_f {Nf[i]:.3e}")
        sv = __import__('os').environ.get('HS_SAVE', '')                                               # optional node-level export (added 2026-10-22T05:5xZ for the checker): all arrays at the evaluated nodes
        if sv:
            import hashlib
            np.savez(sv, x=np.asarray(X, float), y=np.asarray(Y, float), V1=V1, V2=V2, g=np.asarray(g, float), g_xi=np.asarray(gx, float), g_y=np.asarray(gy, float), R_h=Rh, N_f=Nf,
                     c=float(c), N=int(N), M=int(M), fine=bool(fine), rule=rule, state_file=f, state_sha256=hashlib.sha256(open(f, 'rb').read()).hexdigest(), solver_nodes_Fmax=float(nodeF))
            print(f"   node arrays saved to {sv} (x, y, V1, V2, g, g_xi, g_y, R_h, N_f at all {len(X)} evaluated nodes; sha256 of the state recorded)")

if __name__ == '__main__':
    main(sys.argv[1:])
