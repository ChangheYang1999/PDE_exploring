"""
hs_angular_scan.py -- signed residual R_h/N_f of a saved hydrostatic state along the angle at fixed radii, on a fine angular grid (the collocation angles are
theta_j = pi (j + 1/2)/(2M)? -- printed from the model), with the resolved evaluator.  Shows whether a node-exact state oscillates between the collocation angles
(aliasing) and at which angular frequency.  usage: python3 src/hs_angular_scan.py state.pt r1 r2 ...
"""
import sys, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import hs, hs_solve, hs_layer
torch.set_default_dtype(torch.float64)
f = sys.argv[1]; radii = [float(a) for a in sys.argv[2:]] or [3.0, 30.0, 300.0, 3000.0]
st = torch.load(f, weights_only=False); N, M, c = st['N'], st['M'], st['c']; P = st.get('map_exponent_P', st.get('p')); c_map = P / (P - 1)
hsm = hs_solve.HSModel(N, M, c_map, n_in=4, n_tail=4); m = hsm.m; u = st['u'].to(m.dev); ge = hs.GEval(m, m.beta_full(u))
th_c = np.sort(np.unique(np.round(np.arctan2(hsm.Y, hsm.X), 10)))
print(f"{f.split('/')[-1]} {N}x{M}: collocation angles (deg): " + " ".join(f"{np.degrees(t):.2f}" for t in th_c[:6]) + " ... " + " ".join(f"{np.degrees(t):.2f}" for t in th_c[-3:]))
nth = int(__import__('os').environ.get('HS_NTH', 8 * M + 1)); th = np.linspace(0, np.pi / 2, nth)[1:-1]   # HS_NTH: number of angles over the quadrant (default 8M + 1; added 2026-10-22T07:5xZ to test the sample dependence of the sign-change count)
print(f'  angular sample: {nth} points over the quadrant ({nth - 2} interior angles)')
for r in radii:
    X = r * np.cos(th); Y = r * np.sin(th); g, gx, gy = ge(X, Y)
    _os = __import__('os'); _q = int(_os.environ.get('HS_QS', '2')); _nt = int(_os.environ.get('HS_NTAIL', '400')); _hr = float(_os.environ.get('HS_HREL', '1e-5'))   # evaluator variants (added 2026-10-22T08:0xZ for the sensitivity test of the r = 3 scan)
    V1, V2 = hs_layer.hydro_V_log(ge, X, Y, n0=32, per_decade=10, ngl=16, n_tail=_nt, q=_q, hrel=_hr, ymax_dec=np.log10(max(Y.max(), 10.0)))
    V1 = np.asarray(V1); V2 = np.asarray(V2); R = (c * X + V1) * gx + (c * Y + V2) * gy - g; Nf = np.abs((c * X + V1) * gx) + np.abs((c * Y + V2) * gy) + np.abs(g)
    q = R / Nf; sgn = np.sign(q); nzero = int((sgn[1:] * sgn[:-1] < 0).sum())
    # residual at the collocation angles (interpolated) vs the maxima between them
    qc = np.interp(th_c, th, q)
    # dominant angular frequency of q (cos 2k theta content)
    k = np.arange(0, 3 * M); C = np.cos(2 * k[None, :] * th[:, None]); coef = np.linalg.lstsq(C, q, rcond=None)[0]; kd = int(np.argmax(np.abs(coef[1:])) + 1)
    _sv = _os.environ.get('HS_SAVE', '')
    if _sv:
        np.savez(_sv.replace('.npz', '') + f'_r{r:g}.npz', theta=th, q=q, R_h=R, N_f=Nf, V1=V1, V2=V2, g=np.asarray(g, float), g_xi=np.asarray(gx, float), g_y=np.asarray(gy, float), x=X, y=Y, r=r, q_tail=_q, n_tail=_nt, hrel=_hr, state_file=f)
        print(f"  pointwise arrays saved to {_sv.replace('.npz', '')}_r{r:g}.npz (theta, q = R_h/N_f, R_h, N_f, V1, V2, g, g_xi, g_y, x, y; evaluator q_tail {_q}, n_tail {_nt}, hrel {_hr})")
    print(f"  r = {r:8g}: max |R_h|/N_f {np.abs(q).max():.3e} (at theta = {np.degrees(th[np.argmax(np.abs(q))]):.2f} deg), at the collocation angles max {np.abs(qc).max():.3e}; sign changes over the quadrant {nzero} (M = {M}); dominant cos 2k theta mode k = {kd} (|coef| {abs(coef[kd]):.2e}; k <= 3 total {np.abs(coef[:4]).sum():.2e})")
