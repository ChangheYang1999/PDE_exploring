"""
hs_common_res.py -- between-node residuals of saved hydrostatic trial states on ONE common point set with ONE evaluator (external referee cauchy1, item 6):
g, g_x, g_y from hs.GEval and V = (V_1, V_2) from the resolved inverse hs_layer.hydro_V_log (n0 32, 10 log panels per decade x 16 Gauss points, tail 400) at
37 log radii 1e-3 .. 1e6 x 9 quadrant angles (both axes included; the angles are NOT the collocation angles of any state).  R_h = (c x + V_1) g_x + (c y + V_2) g_y - g,
N_f = |(c x + V_1) g_x| + |(c y + V_2) g_y| + |g|.  Reports max |R_h| and max |R_h|/N_f by region, and the quadrature sensitivity of the evaluator on the last state
(per_decade 10 -> 20, tail 400 -> 800).  Diagnostic of trial states only; sampled maxima are not bounds.
usage: python3 src/hs_common_res.py runs/a.pt ...
"""
import sys, os, numpy as np, torch
QMAP = int(os.environ.get('HS_Q', '2')); NTAIL = int(os.environ.get('HS_NTAIL', '400'))   # tail map exponent / points of the resolved inverse; the first tables (21:0xZ) used q = 3 (see hs_layer.hydro_V_log NOTE); q = 2 since 21:45Z
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import hs, hs_solve, hs_layer
torch.set_default_dtype(torch.float64)

def load(f):
    st = torch.load(f, weights_only=False); N, M, c = st['N'], st['M'], st['c']; P = st.get('map_exponent_P', st.get('p')); c_map = P / (P - 1)
    hsm = hs_solve.HSModel(N, M, c_map, n_in=4, n_tail=4); m = hsm.m; u = st['u'].to(m.dev)
    return dict(tag=f.split('/')[-1][:-3], N=N, M=M, c=c, ge=hs.GEval(m, m.beta_full(u)))

def resid(s, X, Y, **kw):
    g, gx, gy = s['ge'](X, Y); V1, V2 = hs_layer.hydro_V_log(s['ge'], X, Y, **kw); V1 = np.asarray(V1); V2 = np.asarray(V2); c = s['c']
    R = (c * X + V1) * gx + (c * Y + V2) * gy - g; Nf = np.abs((c * X + V1) * gx) + np.abs((c * Y + V2) * gy) + np.abs(g)
    return R, Nf

def main(files):
    S = [load(f) for f in files]
    r = np.logspace(-3, 6, 37); th = np.linspace(0, np.pi / 2, 9); Rg, T = np.meshgrid(r, th, indexing='ij'); X = (Rg * np.cos(T)).reshape(-1); Y = (Rg * np.sin(T)).reshape(-1); Rr = Rg.reshape(-1)
    regs = [(0, 0.1), (0.1, 1), (1, 100), (100, 1e4), (1e4, 1e6 + 1)]
    kw = dict(n0=32, per_decade=10, ngl=16, n_tail=NTAIL, q=QMAP)
    print(f"c = {S[0]['c']}: {len(Rr)} common points (37 log radii 1e-3 .. 1e6 x 9 angles 0 .. pi/2), resolved inverse (n0 32, 10 log panels/decade x 16, tail {NTAIL} points, q = {QMAP}); per region: max |R_h| / max |R_h|/N_f")
    print("state                     " + "  ".join(f"[{lo:g},{hi:g})".ljust(22) for lo, hi in regs))
    for s in S:
        R, Nf = resid(s, X, Y, **kw); line = f"{s['N']}x{s['M']}".ljust(26)
        for lo, hi in regs:
            m = (Rr >= lo) & (Rr < hi); mm = m & (Nf > 0); line += f"{np.abs(R[m]).max():9.2e} {(np.abs(R[mm]) / Nf[mm]).max():9.2e}    "   # on the x-axis g = g_x = V_2 = 0 so R_h = N_f = 0: excluded from the ratio
        print(line)
    s = S[-1]; R0, Nf0 = resid(s, X, Y, **kw); R1, Nf1 = resid(s, X, Y, n0=32, per_decade=20, ngl=16, n_tail=2 * NTAIL, q=QMAP)
    line = f"evaluator sensitivity ({s['N']}x{s['M']}): max |R_h(fine) - R_h(std)|/N_f by region: "
    for lo, hi in regs:
        m = (Rr >= lo) & (Rr < hi) & (Nf0 > 0); line += f"{(np.abs(R1[m] - R0[m]) / Nf0[m]).max():9.2e}  "
    print(line)

if __name__ == '__main__':
    main(sys.argv[1:])
