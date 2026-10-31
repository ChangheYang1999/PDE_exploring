"""Manufactured test of the field assembly: the same potentials built symbolically in sympy (twist, envelopes,
Chebyshev map), U = curl(T y) + curl curl(S y), Omega = curl U, and all first derivatives, compared with
Model.fields_points (arbitrary points incl. axis and origin) and Model.fields_grid (product grid)."""
import sys, os, math, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch, sympy as sp
from src.equations.fields import Model, alpha_of
torch.set_default_dtype(torch.float64)

def sympy_solid(modes, L):
    """Real solid harmonics as exact sympy polynomials via the same recurrences (exact rational arithmetic)."""
    x, y, z = sp.symbols('x y z', real=True)
    rho = x**2 + y**2 + z**2
    R = {}
    R[(0, 0)] = sp.Integer(1)
    for m in range(1, L + 1):
        R[(m, m)] = sp.expand((x + sp.I * y) * R[(m - 1, m - 1)] / (2 * m))
    for m in range(0, L):
        R[(m + 1, m)] = sp.expand(z * R[(m, m)])
    for m in range(0, L + 1):
        for l in range(m + 2, L + 1):
            R[(l, m)] = sp.expand(((2 * l - 1) * z * R[(l - 1, m)] - rho * R[(l - 2, m)]) / ((l - m) * (l + m)))
    out = []
    for (l, m, t) in modes:
        N = sp.sqrt(sp.Rational(2 * l + 1, 4) / sp.pi * sp.factorial(l - m) / sp.factorial(l + m))
        if m == 0:
            out.append(N * sp.factorial(l) * R[(l, 0)])
        else:
            f = sp.sqrt(2) * N * sp.factorial(l + m)
            out.append(f * (sp.re(sp.expand(R[(l, m)])) if t == 0 else sp.im(sp.expand(R[(l, m)]))))
    return out

def sympy_fields(model, z):
    x, y, zz = sp.symbols('x y z', real=True)
    aT, aS, c_l, omega = model.unpack(z)
    c_l = sp.Float(float(c_l), 30); omega = sp.Float(float(omega), 30)
    alpha = (1 - c_l) / c_l
    R0 = sp.Float(model.R0, 30)
    rho = x**2 + y**2 + zz**2
    s = sp.sqrt(rho + R0**2)
    X = (s - R0) / (s + R0)
    beta = omega / (2 * c_l) * sp.log(1 + rho / R0**2)
    polys = sympy_solid(model.modes, model.L)
    def cheb(k):
        return sp.chebyshevt(k, 2 * X - 1)
    T = 0; S = 0
    # twist: pair (c, s) -> gc cos(m beta) + gs sin(m beta) on the cos mode, -gc sin(m beta) + gs cos(m beta) on the sin mode
    gT = lambda qq: sum(float(aT[k, qq]) * cheb(k) for k in range(model.Nk))
    gS = lambda qq: sum(float(aS[k, qq]) * cheb(k) for k in range(model.Nk))
    for q, (l, m, t) in enumerate(model.modes):
        envT = (s / R0) ** (-(alpha + l)); envS = (s / R0) ** (-(alpha + l - 1))
        if m == 0:
            T += envT * gT(q) * polys[q]; S += envS * gS(q) * polys[q]
        elif t == 0:
            T += envT * (gT(q) * sp.cos(m * beta) + gT(q + 1) * sp.sin(m * beta)) * polys[q]
            S += envS * (gS(q) * sp.cos(m * beta) + gS(q + 1) * sp.sin(m * beta)) * polys[q]
        else:
            T += envT * (-gT(q - 1) * sp.sin(m * beta) + gT(q) * sp.cos(m * beta)) * polys[q]
            S += envS * (-gS(q - 1) * sp.sin(m * beta) + gS(q) * sp.cos(m * beta)) * polys[q]
    Y = sp.Matrix([x, y, zz])
    def curl(V):
        return sp.Matrix([sp.diff(V[2], y) - sp.diff(V[1], zz), sp.diff(V[0], zz) - sp.diff(V[2], x), sp.diff(V[1], x) - sp.diff(V[0], y)])
    U = curl(T * Y) + curl(curl(S * Y))
    Om = curl(U)
    GU = sp.Matrix(3, 3, lambda mm, i: sp.diff(U[i], [x, y, zz][mm]))
    GOm = sp.Matrix(3, 3, lambda mm, i: sp.diff(Om[i], [x, y, zz][mm]))
    divU = sum(sp.diff(U[i], v) for i, v in enumerate([x, y, zz]))
    f = sp.lambdify((x, y, zz), [U, Om, GU, GOm, divU], "mpmath")
    return f

MPAR = sys.argv[1] if len(sys.argv) > 1 else "all"

def run():
    torch.manual_seed(0)
    model = Model(L=2, Nk=2, m_parity=MPAR, R0=1.3, Nr=6, ntheta=5, nphi=8, c_l=0.45, omega=0.7, free_params=True)
    z = torch.randn(model.n_z) * 0.5
    z[-2] = 0.45; z[-1] = 0.7
    t0 = time.time()
    f = sympy_fields(model, z)
    print(f"sympy build {time.time()-t0:.1f}s")
    import mpmath
    mpmath.mp.dps = 30
    pts = np.array([[0.3, -0.7, 0.5], [1.9, 0.2, -1.1], [0.0, 0.0, 0.8], [0.0, 0.0, -2.5], [1e-3, 2e-3, -1e-3]])
    out = model.fields_points(z, torch.tensor(pts))
    maxerr = {'U': 0, 'Om': 0, 'GU': 0, 'GOm': 0, 'divU_sympy': 0}
    for p in range(pts.shape[0]):
        Uref, Omref, GUref, GOmref, dv = f(*[mpmath.mpf(float(v)) for v in pts[p]])
        Uref = np.array(Uref.tolist(), dtype=float).reshape(3); Omref = np.array(Omref.tolist(), dtype=float).reshape(3)
        GUref = np.array(GUref.tolist(), dtype=float); GOmref = np.array(GOmref.tolist(), dtype=float)
        maxerr['U'] = max(maxerr['U'], np.max(np.abs(out['U'][:, p].numpy() - Uref)) / (1 + np.abs(Uref).max()))
        maxerr['Om'] = max(maxerr['Om'], np.max(np.abs(out['Om'][:, p].numpy() - Omref)) / (1 + np.abs(Omref).max()))
        maxerr['GU'] = max(maxerr['GU'], np.max(np.abs(out['GU'][:, :, p].numpy() - GUref)) / (1 + np.abs(GUref).max()))
        maxerr['GOm'] = max(maxerr['GOm'], np.max(np.abs(out['GOm'][:, :, p].numpy() - GOmref)) / (1 + np.abs(GOmref).max()))
        maxerr['divU_sympy'] = max(maxerr['divU_sympy'], abs(float(dv)))
    print("points (incl. axis, near origin) vs sympy, relative errors:", {k: f"{v:.2e}" for k, v in maxerr.items()})
    assert all(v < 1e-10 for v in maxerr.values())
    # grid evaluation vs sympy at a few grid points
    og = model.fields_grid(z)
    yg = og['y']
    errg = 0.0
    for (j, a) in [(0, 0), (2, 7), (5, 13), (3, 39), (5, 0)]:
        P = yg[j, a].numpy()
        Uref, Omref, GUref, GOmref, dv = f(*[mpmath.mpf(float(v)) for v in P])
        Uref = np.array(Uref.tolist(), dtype=float).reshape(3); Omref = np.array(Omref.tolist(), dtype=float).reshape(3)
        GUref = np.array(GUref.tolist(), dtype=float); GOmref = np.array(GOmref.tolist(), dtype=float)
        errg = max(errg, np.max(np.abs(og['U'][:, j, a].numpy() - Uref)) / (1 + np.abs(Uref).max()),
                   np.max(np.abs(og['Om'][:, j, a].numpy() - Omref)) / (1 + np.abs(Omref).max()),
                   np.max(np.abs(og['GU'][:, :, j, a].numpy() - GUref)) / (1 + np.abs(GUref).max()),
                   np.max(np.abs(og['GOm'][:, :, j, a].numpy() - GOmref)) / (1 + np.abs(GOmref).max()))
    print(f"grid evaluation vs sympy (r up to {yg[5,0].norm():.1f}): max rel err {errg:.2e}")
    assert errg < 1e-10
    # divergence of the torch field
    divU = og['GU'][0, 0] + og['GU'][1, 1] + og['GU'][2, 2]
    print(f"div U on grid (torch): {divU.abs().max().item():.2e} relative to |GU| max {og['GU'].abs().max().item():.2e}")
    assert divU.abs().max().item() < 1e-11 * og['GU'].abs().max().item()
    # points vs grid consistency at all grid points
    op = model.fields_points(z, yg.reshape(-1, 3))
    d = max((op['U'].reshape(3, model.Nr, model.Na) - og['U']).abs().max().item(), (op['GOm'].reshape(3, 3, model.Nr, model.Na) - og['GOm']).abs().max().item())
    print(f"points-evaluator vs grid-evaluator at all grid points: {d:.2e}")
    assert d < 1e-10
    print("ALL FIELD TESTS PASSED")

if __name__ == "__main__":
    run()
