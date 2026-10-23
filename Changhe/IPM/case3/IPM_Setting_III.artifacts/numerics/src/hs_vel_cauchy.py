"""
hs_vel_cauchy.py -- do the hydrostatic velocities V = (V_1, V_2) of consecutive saved trial states approach each other? (external referee cauchy1, item 5:
convergence of g in the class norm does not by itself control the nonlocal inverse).  V is evaluated with the resolved inverse hs_layer.hydro_V_log on a common
set of points (log radii 1e-2 .. 1e4 x 9 quadrant angles incl. both axes) and max |V_a - V_b|/(1 + r)^p, max |V_a - V_b|/max|V_b| are tabulated by region,
together with the scale max |V_b|/(1 + r)^p.  Diagnostic of trial states only.
usage: python3 src/hs_vel_cauchy.py runs/a.pt runs/b.pt ...
"""
import sys, os, numpy as np, torch
NTAIL = int(os.environ.get('HS_NTAIL', '400')); QMAP = int(os.environ.get('HS_Q', '2'))
# tail rule of the resolved inverse: t = y + (1 + y) (u/(1-u))^QMAP with NTAIL Gauss points.  The first tables of 4P(b)(xvi) item 9 used q = 3, 400 points, which is
# converged to about 4e-7 absolute in V_1 (1e-5 relative at far x-axis points, verifier 277); with q = 3 MORE tail points make the far-node contributions
# unreliable (inner V_1 drifts by 3e-4 from 400 to 3200 points), while q = 2 is stable to 3e-8 for 400 .. 3200 points: q = 2, 400 points is the default since 19:50Z.
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import hs, hs_solve, hs_layer
torch.set_default_dtype(torch.float64)

def load(f):
    st = torch.load(f, weights_only=False); N, M, c = st['N'], st['M'], st['c']; P = st.get('map_exponent_P', st.get('p')); c_map = P / (P - 1)
    hsm = hs_solve.HSModel(N, M, c_map, n_in=4, n_tail=4); m = hsm.m; u = st['u'].to(m.dev)
    return dict(N=N, M=M, c=c, ge=hs.GEval(m, m.beta_full(u)))

def main(files):
    S = [load(f) for f in files]; c = S[0]['c']; p = 1.0 / c
    r = np.logspace(-2, 4, 25); th = np.linspace(0, np.pi / 2, 9); R, T = np.meshgrid(r, th, indexing='ij'); X = (R * np.cos(T)).reshape(-1); Y = (R * np.sin(T)).reshape(-1); R = R.reshape(-1)
    V = []
    for s in S:
        V1, V2 = hs_layer.hydro_V_log(s['ge'], X, Y, n0=32, per_decade=10, ngl=16, n_tail=NTAIL, q=QMAP); V.append((np.asarray(V1), np.asarray(V2)))
    regs = [(0.01, 0.1), (0.1, 1), (1, 100), (100, 1e4 + 1)]
    print(f"c = {c}: {len(R)} points (25 log radii 1e-2 .. 1e4 x 9 angles incl. both axes); resolved inverse (n0 32, 10 log panels/decade x 16, tail {NTAIL}, q = {QMAP})")
    print("pair                      " + "  ".join(f"[{lo:g},{hi:g})".ljust(34) for lo, hi in regs) + "   columns: max|dV1|/(1+r)^p  max|dV2|/(1+r)^p  max|dV|/max|V_b| (region)")
    for a, b in zip(range(len(S) - 1), range(1, len(S))):
        d1 = np.abs(V[a][0] - V[b][0]); d2 = np.abs(V[a][1] - V[b][1]); line = f"{S[a]['N']}x{S[a]['M']} -> {S[b]['N']}x{S[b]['M']}".ljust(26)
        for lo, hi in regs:
            m = (R >= lo) & (R < hi); vb = np.hypot(V[b][0][m], V[b][1][m]).max()
            line += f"{(d1[m] / (1 + R[m]) ** p).max():9.2e} {(d2[m] / (1 + R[m]) ** p).max():9.2e} {np.hypot(d1[m], d2[m]).max() / vb:9.2e}      "
        print(line)
    line = f"scale of last: max|V1|,|V2|/(1+r)^p".ljust(26)
    for lo, hi in regs:
        m = (R >= lo) & (R < hi); line += f"{(np.abs(V[-1][0][m]) / (1 + R[m]) ** p).max():9.2e} {(np.abs(V[-1][1][m]) / (1 + R[m]) ** p).max():9.2e}                "
    print(line)
    print("\nV_2(0, y)/y^p on the axis at y = 1e-2, 1e-1, 1, 10, 100, 1e3, 1e4 (leading far-field value Q/(p(1-p)) = 4 Q at c = 2; if Q were p K this would be K/(1-p) = 2 K; verifier 277 corrected an earlier 4 K here):")
    ys = np.array([1e-2, 1e-1, 1, 10, 100, 1e3, 1e4]); zs = np.zeros_like(ys)
    for s in S:
        _, v2 = hs_layer.hydro_V_log(s['ge'], zs, ys, n0=32, per_decade=10, ngl=16, n_tail=NTAIL, q=QMAP); print(f"  {s['N']}x{s['M']}: " + " ".join(f"{v:+.5f}" for v in np.asarray(v2) / ys ** p))
    print("V_1(xi, 0)/(1+xi)^p on the x-axis at xi = same:")
    for s in S:
        v1, _ = hs_layer.hydro_V_log(s['ge'], ys, zs, n0=32, per_decade=10, ngl=16, n_tail=NTAIL, q=QMAP); print(f"  {s['N']}x{s['M']}: " + " ".join(f"{v:+.5f}" for v in np.asarray(v1) / (1 + ys) ** p))

if __name__ == '__main__':
    main(sys.argv[1:])
