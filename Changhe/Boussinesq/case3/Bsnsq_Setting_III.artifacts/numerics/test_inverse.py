import sys, time, numpy as np, torch, sympy as sp
sys.path.insert(0, '.')
from bq3core import Basis, Geometry, Problem, DT

torch.set_default_dtype(DT)
dev = 'cuda'
x, y = sp.symbols('x y', real=True)
r2 = x**2 + y**2

def make_case(hexpr):
    Psi = x * hexpr
    Om = -(sp.diff(Psi, x, 2) + sp.diff(Psi, y, 2))
    G = sp.simplify(Om / x)
    fG = sp.lambdify((x, y), G, 'numpy')
    fH = sp.lambdify((x, y), hexpr, 'numpy')
    fHy = sp.lambdify((x, y), sp.diff(hexpr, y), 'numpy')
    fU2 = sp.lambdify((x, y), sp.diff(Psi, x), 'numpy')
    fU1 = sp.lambdify((x, y), -sp.diff(Psi, y), 'numpy')
    v0 = float(sp.diff(Psi, x).subs({x: 0, y: 0}))
    c = float(sp.diff(Psi, x, y).subs({x: 0, y: 0}))
    return fG, fH, fHy, fU2, fU1, v0, c

def run(beta, L, Nt, deg, K, Nphi, hexpr, label):
    t0 = time.time()
    b = Basis(Nt, deg, K, Nphi, ng_coll=3, ng_quad=12, m_reg=2, device=dev)
    g = Geometry(b, beta, L)
    xs, ys = g.x.cpu().numpy(), g.y.cpu().numpy()
    fG, fH, fHy, fU2, fU1, v0, c = make_case(hexpr)
    Gv = torch.tensor(fG(xs, ys), dtype=DT, device=dev)
    # least-squares fit of G on the basis
    sol = torch.linalg.lstsq(g.Phi0, Gv[:, None], driver='gels')
    cG = sol.solution[:, 0]
    Gfit = g.Phi0 @ cG
    errG = (Gfit - Gv).abs().max().item() / Gv.abs().max().item()
    H = (g.M_H @ cG).cpu().numpy()
    Hy = (g.M_Hy @ cG).cpu().numpy()
    U2 = (g.M_U2 @ cG).cpu().numpy()
    U1 = (g.M_U1 @ cG).cpu().numpy()
    Hex = fH(xs, ys) - v0            # subtracted uniform vertical velocity
    Hyex = fHy(xs, ys)
    U2ex = fU2(xs, ys) - v0
    U1ex = fU1(xs, ys)
    def rel(a, bb):
        return np.max(np.abs(a - bb)) / np.max(np.abs(bb))
    cnum = (g.c_op @ cG).item()
    v0num = (g.v0_op @ cG).item()
    print(f"[{label}] beta={beta} L={L} Nt={Nt} deg={deg} K={K} Nphi={Nphi} Nb={b.Nb} Npts={len(xs)} "
          f"time {time.time()-t0:.1f}s")
    print(f"   fit err G rel {errG:.2e}; H rel {rel(H,Hex):.2e}; Hy rel {rel(Hy,Hyex):.2e}; "
          f"U2 rel {rel(U2,U2ex):.2e}; U1 rel {rel(U1,U1ex):.2e}; c num {cnum:.8f} exact {c:.8f} (err {cnum-c:.2e}); "
          f"v0 num {v0num:.8f} exact {v0:.8f}")
    # error by radius
    rr = g.rr.cpu().numpy()
    e = np.abs(U2 - U2ex) + np.abs(U1 - U1ex)
    for lo, hi in [(0, 0.1), (0.1, 1), (1, 10), (10, 100), (100, 1e4), (1e4, 1e30)]:
        m = (rr >= lo) & (rr < hi)
        if m.any():
            print(f"      r in [{lo:g},{hi:g}): max|U err| {e[m].max():.2e}  max|U ex| {(np.abs(U2ex)+np.abs(U1ex))[m].max():.2e}  n={m.sum()}")

if __name__ == '__main__':
    # case 1: Gaussian decay, no y parity
    h1 = (1 + y / 2 + x**2 / 5) * sp.exp(-r2 / 4)
    for (Nt, deg, K, Nphi) in [(40, 5, 16, 32), (80, 5, 24, 48), (120, 7, 32, 64)]:
        run(3.0, 1.5, Nt, deg, K, Nphi, h1, 'gauss')
    # case 2: slow algebraic decay matching the beta tail: Omega ~ r^{-2/beta}
    beta = 3.0
    h2 = (1 + y / 2 + x**2 / 5) * (1 + r2 / 4) ** (-sp.Rational(1, 3) - 1) * (1 + r2/4)  # ~ r^{-2/beta}, beta=3
    # Psi = x h ~ r^{1-2/3} = r^{1/3}: Omega ~ r^{-2/3} ok
    for (Nt, deg, K, Nphi) in [(40, 5, 16, 32), (80, 5, 24, 48), (120, 7, 32, 64)]:
        run(beta, 1.5, Nt, deg, K, Nphi, h2, 'slow')
