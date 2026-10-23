"""
hs_cauchy.py -- are the saved hydrostatic trial states of a refinement sequence a Cauchy sequence AS FUNCTIONS?
For consecutive saved states (same c, same map) evaluate g, g_x, g_y with the lean evaluator hs.GEval on a common set of points
(log-spaced radii, quadrant angles including both axes) and report, by radial region, the maximum of
    |g_a - g_b| / (1 + r)^p          (p = 1/c; the far-field growth of g is r^p, so this is a scale-free difference),
    |g_a - g_b| / (|g_b| + 1e-300)   (relative, where g_b is not tiny),
    |grad(g_a - g_b)| / (1 + r)^(p-1),
and the same for the axis trace G(y) = g(0, y) and the x-axis slope k(xi) = g_y(xi, 0).  Diagnostic of trial states only.
usage: python3 src/hs_cauchy.py runs/a.pt runs/b.pt runs/c.pt ...   (consecutive pairs are compared)
"""
import sys, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import hs, hs_solve
torch.set_default_dtype(torch.float64)

def load(f):
    st = torch.load(f, weights_only=False); N, M, c = st['N'], st['M'], st['c']; P = st.get('map_exponent_P', st.get('p')); c_map = P / (P - 1)
    hsm = hs_solve.HSModel(N, M, c_map, n_in=4, n_tail=4); m = hsm.m; u = st['u'].to(m.dev)
    return dict(tag=f.split('/')[-1][:-3], N=N, M=M, c=c, ge=hs.GEval(m, m.beta_full(u)))

def points():
    r = np.logspace(-3, 7, 401); th = np.concatenate([[0.0], np.linspace(0, np.pi / 2, 49)[1:-1], [np.pi / 2]])
    R, T = np.meshgrid(r, th, indexing='ij'); return (R * np.cos(T)).reshape(-1), (R * np.sin(T)).reshape(-1), R.reshape(-1)

def main(files):
    S = [load(f) for f in files]; X, Y, R = points(); c = S[0]['c']; p = 1.0 / c
    vals = []
    for s in S:
        g, gx, gy = s['ge'](X, Y); vals.append((g, gx, gy))
    regs = [(0, 0.1), (0.1, 1), (1, 100), (100, 1e4), (1e4, 1e7)]
    print(f"c = {c}, p = {p:.4f}; {len(R)} points (401 log radii 1e-3..1e7 x 49 angles incl. both axes); columns per region: max|dg|/(1+r)^p, max|dg|/|g_b|, max|d grad g|/(1+r)^(p-1)")
    print("pair                                    " + "  ".join(f"[{lo:g},{hi:g})".ljust(30) for lo, hi in regs))
    for a, b in zip(S[:-1], S[1:]):
        ga, gxa, gya = vals[S.index(a)]; gb, gxb, gyb = vals[S.index(b)]
        dg = np.abs(ga - gb); dgr = np.hypot(gxa - gxb, gya - gyb); line = f"{a['N']}x{a['M']} -> {b['N']}x{b['M']}".ljust(40)
        for lo, hi in regs:
            m = (R >= lo) & (R < hi)
            line += f"{(dg[m] / (1 + R[m]) ** p).max():9.2e} {(dg[m] / (np.abs(gb[m]) + 1e-300)).max():9.2e} {(dgr[m] / (1 + R[m]) ** (p - 1)).max():9.2e}   "
        print(line)
    # scale of the states themselves (for reference): max |g|/(1+r)^p and max |grad g|/(1+r)^(p-1) per region for the last state
    gb, gxb, gyb = vals[-1]; line = f"scale of {S[-1]['N']}x{S[-1]['M']}: max|g|/(1+r)^p, max|grad g|/(1+r)^(p-1)".ljust(40)
    for lo, hi in regs:
        m = (R >= lo) & (R < hi); line += f"{(np.abs(gb[m]) / (1 + R[m]) ** p).max():9.2e}           {(np.hypot(gxb[m], gyb[m]) / (1 + R[m]) ** (p - 1)).max():9.2e}   "
    print(line)
    # axis traces
    y = np.logspace(-3, 7, 1001); z = np.zeros_like(y)
    print("\naxis trace G(y) = g(0, y): max |G_a - G_b| / (1 + y)^p by region; x-axis slope k(xi) = g_y(xi, 0): max |k_a - k_b| / (1 + xi)^(p-1)")
    for a, b in zip(S[:-1], S[1:]):
        Ga = a['ge'](z, y)[0]; Gb = b['ge'](z, y)[0]; ka = a['ge'](y, z)[2]; kb = b['ge'](y, z)[2]
        line = f"{a['N']}x{a['M']} -> {b['N']}x{b['M']}".ljust(40)
        for lo, hi in regs:
            m = (y >= lo) & (y < hi); line += f"G {np.abs(Ga - Gb)[m].max() / 1:9.2e}/(1+y)^p-> {(np.abs(Ga - Gb)[m] / (1 + y[m]) ** p).max():9.2e}  k {(np.abs(ka - kb)[m] / (1 + y[m]) ** (p - 1)).max():9.2e} | "
        print(line)
    # a few pointwise values of G and k for the eye
    ys = np.array([1e-2, 1e-1, 1.0, 10.0, 100.0, 1e3, 1e4, 1e6]); zs = np.zeros_like(ys)
    print("\nG(0, y) / y^p at y = " + ", ".join(f"{v:g}" for v in ys))
    for s in S: print(f"  {s['N']}x{s['M']}: " + " ".join(f"{v:+.6f}" for v in s['ge'](zs, ys)[0] / ys ** p))
    print("g_y(xi, 0) / (1+xi)^(p-1) at xi = " + ", ".join(f"{v:g}" for v in ys))
    for s in S: print(f"  {s['N']}x{s['M']}: " + " ".join(f"{v:+.6f}" for v in s['ge'](ys, zs)[2] / (1 + ys) ** (p - 1)))
    print("g(xi, xi) / r^p at xi = " + ", ".join(f"{v:g}" for v in ys))
    for s in S: print(f"  {s['N']}x{s['M']}: " + " ".join(f"{v:+.6f}" for v in s['ge'](ys, ys)[0] / (np.sqrt(2) * ys) ** p))

if __name__ == '__main__':
    main(sys.argv[1:])
