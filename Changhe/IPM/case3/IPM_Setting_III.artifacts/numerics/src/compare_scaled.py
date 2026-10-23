"""compare_scaled.py -- compare saved Q states with a reference state modulo the exact scaling symmetry rho_lam(X) = lam rho(X/lam)
(a_0 and c_l invariant, K -> lam^(1-1/c_l) K, b, e -> lam^-2 b, e; so b K^(2 c_l/(c_l-1)) ... at c_l = 3: b K^3 invariant).
For each state S: lam = (K_S/K_ref)^(1/(1-gamma)); report the invariants a_0, b K^3, e K^3 (generally b K^(2/(1-gamma))), and the pointwise
comparison q_S(r) against q_ref(r/lam) on both axes (relative differences of 1 - q in the core and of q outside).
usage: python3 src/compare_scaled.py ref.pt state1.pt [state2.pt ...]"""
import sys, math, numpy as np
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import qdiag
from local_exponent import jets
files = [a for a in sys.argv[1:] if '=' not in a]
S = [qdiag.State(f) for f in files]; ref = S[0]; g = ref.gamma; ex = 2 / (1 - g)
rr = np.array([1e-3, 3e-3, 1e-2, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 100.0, 1e4, 1e6])
def qax(s, r, th): o = s.ev(r, np.full_like(r, th)); return o['w'] * o['b'] / s.a0
print(f"reference {files[0]}: N={ref.N} L={ref.L} a0={ref.a0:.6f} K={ref.K:.6f}; invariant exponent b K^{ex:.4g}")
rows = []
for f, s in zip(files, S):
    a0, b, e, c, q1, q2 = jets(s); lam = (s.K / ref.K) ** (1 / (1 - g))
    rows.append((f, s, lam, a0, b, e))
    print(f"{f.split('/')[-1]:>24s}: N={s.N:3d} L={s.L:4g} K={s.K:9.5f} lam={lam:8.5f} a0={a0:.6f} ({a0/ref.a0-1:+.4%} vs ref)  b K^ex={b*s.K**ex:+.6e}  e K^ex={e*s.K**ex:+.6e}  lam^2 b={lam*lam*b:+.4f}  lam^2 e={lam*lam*e:+.4f}")
a0r, br, er = rows[0][3], rows[0][4], rows[0][5]
for f, s, lam, a0, b, e in rows[1:]:
    print(f"   invariant changes vs ref: a0 {a0/a0r-1:+.4%}, b K^ex {b*s.K**ex/(br*ref.K**ex)-1:+.4%}, e K^ex {e*s.K**ex/(er*ref.K**ex)-1:+.4%}")
print("pointwise, modulo scaling: q_S(r) vs q_ref(r/lam) on the y-axis [and x-axis]; columns per state: rel diff of (1-q) | rel diff of q")
hdr = f"{'r':>8s} " + " ".join(f"{f.split('/')[-1].replace('r1C_cl3.0_',''):>22s}" for f, *_ in rows[1:]); print(hdr)
qy_ref = {}; qx_ref = {}
for f, s, lam, *_ in rows[1:]:
    qy_ref[f] = qax(ref, rr / lam, math.pi / 2); qx_ref[f] = qax(ref, rr / lam, 0.0)
qy = {f: qax(s, rr, math.pi / 2) for f, s, *_ in rows[1:]}; qx = {f: qax(s, rr, 0.0) for f, s, *_ in rows[1:]}
for i, r in enumerate(rr):
    line = f"{r:8.0e} "
    for f, *_ in rows[1:]:
        d1 = (1 - qy[f][i]) / (1 - qy_ref[f][i]) - 1; d2 = qy[f][i] / qy_ref[f][i] - 1
        d3 = (1 - qx[f][i]) / (1 - qx_ref[f][i]) - 1; d4 = qx[f][i] / qx_ref[f][i] - 1
        line += f" y:{d1:+8.4f}|{d2:+8.4f} x:{d3:+8.4f}|{d4:+8.4f}"
    print(line)
