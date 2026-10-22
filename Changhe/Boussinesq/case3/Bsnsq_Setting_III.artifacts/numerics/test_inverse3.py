import sys, time, numpy as np, torch, sympy as sp
sys.path.insert(0, '.')
from bq3core import Basis, Geometry, Problem, DT
from test_inverse import make_case
x, y = sp.symbols('x y', real=True)
r2 = x**2 + y**2
dev='cuda'
def run(beta, L, Nt, deg, K, Nphi, hexpr, label, ng_quad=12, rmap='r'):
    t0 = time.time()
    b = Basis(Nt, deg, K, Nphi, ng_coll=3, ng_quad=ng_quad, m_reg=2, device=dev)
    g = Geometry(b, beta, L, rmap=rmap)
    xs, ys = g.x.cpu().numpy(), g.y.cpu().numpy()
    fG, fH, fHy, fU2, fU1, v0, c = make_case(hexpr)
    Gv = torch.tensor(fG(xs, ys), dtype=DT, device=dev)
    Dt = ((1 - b.t_coll_t) ** g.pG)[:, None].expand(b.Nc, b.Nphi).reshape(-1)
    w = 1.0 / Dt
    act = g.active
    sol = torch.linalg.lstsq((g.Phi0G * w[:, None])[:, act], (Gv * w)[:, None], driver='gels')
    cG = torch.zeros(g.Phi0G.shape[1], dtype=DT, device=dev); cG[act] = sol.solution[:, 0]
    Gfit = g.Phi0G @ cG
    errG = ((Gfit - Gv) / Dt).abs().max().item()
    H = (g.M_H @ cG).cpu().numpy(); Hy = (g.M_Hy @ cG).cpu().numpy()
    U2 = (g.M_U2 @ cG).cpu().numpy(); U1 = (g.M_U1 @ cG).cpu().numpy()
    Hex = fH(xs, ys) - v0; Hyex = fHy(xs, ys); U2ex = fU2(xs, ys) - v0; U1ex = fU1(xs, ys)
    rr = g.rr.cpu().numpy()
    scale = (1 + rr) ** (1 - 1 / beta)           # local velocity scale
    e = (np.abs(U2 - U2ex) + np.abs(U1 - U1ex)) / scale
    cnum = (g.c_op @ cG).item()
    print(f"[{label} rmap={rmap}] beta={beta} L={L} Nt={Nt} deg={deg} K={K} Nphi={Nphi} ngq={ng_quad} Nb={b.Nb} time {time.time()-t0:.1f}s")
    print(f"   weighted fit err G (rel to local scale) {errG:.2e}; max |U err|/(1+r)^(1-2/beta) {e.max():.2e}; "
          f"Hy abs err {np.abs(Hy-Hyex).max():.2e}; c err {cnum-c:.2e}")
    for lo, hi in [(0, 0.1), (0.1, 1), (1, 10), (10, 100), (100, 1e4), (1e4, 1e30)]:
        m = (rr >= lo) & (rr < hi)
        if m.any():
            print(f"      r in [{lo:g},{hi:g}): max scaled U err {e[m].max():.2e}  n={m.sum()}")
beta = 3.0
# h ~ r^{1-1/beta} = r^{2/3}: x^2 (1+r^2/4)^{-2/3} ~ r^{2/3}; Omega ~ r^{-1/3} (SPEC tail)
h2 = (1 + y / 2 + x**2 / 5) * (1 + r2 / 4) ** (-sp.Rational(2, 3))
for rmap in ['r', 'r2']:
    for (Nt, deg, K, Nphi) in [(40, 5, 16, 32), (80, 5, 24, 48), (120, 7, 32, 64)]:
        run(beta, 1.5, Nt, deg, K, Nphi, h2, 'slow2w', rmap=rmap)
