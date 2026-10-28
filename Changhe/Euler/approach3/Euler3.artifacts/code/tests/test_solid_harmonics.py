"""Solid harmonics: values vs scipy sph_harm, derivative ladders vs sympy (low degree) and finite differences,
orthonormality on the Gauss grid, harmonicity (trace of Hessian = 0), on-axis regularity."""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch, sympy as sp
from scipy.special import sph_harm
from src.bases.solid_harmonics import mode_list, eval_solid, AngularGrid, angular_matrices
torch.set_default_dtype(torch.float64)

def test_values_vs_scipy(L=20):
    modes = mode_list(L, "all", l_min=0)
    rng = np.random.default_rng(0)
    y = rng.normal(size=(50, 3))
    A0, _, _ = eval_solid(torch.tensor(y), modes, L, nderiv=0)
    r = np.linalg.norm(y, axis=1); th = np.arccos(y[:, 2] / r); ph = np.arctan2(y[:, 1], y[:, 0])
    err = 0.0
    for q, (l, m, t) in enumerate(modes):
        Ylm = sph_harm(m, l, ph, th)  # scipy: sph_harm(m, l, azimuth, polar), includes (-1)^m CS phase
        cs = (-1) ** m
        if m == 0:
            ref = (r ** l) * Ylm.real
        elif t == 0:
            ref = (r ** l) * math.sqrt(2) * cs * Ylm.real
        else:
            ref = (r ** l) * math.sqrt(2) * cs * Ylm.imag
        err = max(err, np.max(np.abs(A0[:, q].numpy() - ref)) / (1 + np.max(np.abs(ref))))
    print(f"values vs scipy L={L}: max rel err {err:.2e}")
    assert err < 1e-12

def test_ladders_vs_sympy(L=5):
    modes = mode_list(L, "all", l_min=0)
    x, y, z = sp.symbols("x y z", real=True)
    r = sp.sqrt(x**2 + y**2 + z**2)
    th = sp.acos(z / r); ph = sp.atan2(y, x)
    pts = np.random.default_rng(1).normal(size=(6, 3))
    A0, A1, A2 = eval_solid(torch.tensor(pts), modes, L, nderiv=2)
    maxerr = 0.0
    for q, (l, m, t) in enumerate(modes):
        N = sp.sqrt(sp.Rational(2*l+1, 4) / sp.pi * sp.factorial(l-m) / sp.factorial(l+m))
        Plm = (1 - sp.Symbol('u')**2)**sp.Rational(m, 2) * sp.diff(sp.legendre(l, sp.Symbol('u')), sp.Symbol('u'), m)
        Plm = Plm.subs(sp.Symbol('u'), sp.cos(th))
        if m == 0:
            expr = N * Plm * r**l
        else:
            expr = sp.sqrt(2) * N * Plm * (sp.cos(m*ph) if t == 0 else sp.sin(m*ph)) * r**l
        f = sp.lambdify((x, y, z), expr, "numpy")
        g = [sp.lambdify((x, y, z), sp.diff(expr, v), "numpy") for v in (x, y, z)]
        h = [[sp.lambdify((x, y, z), sp.diff(expr, v, w), "numpy") for w in (x, y, z)] for v in (x, y, z)]
        for p in range(pts.shape[0]):
            X = pts[p]
            maxerr = max(maxerr, abs(float(f(*X)) - A0[p, q].item()))
            for i in range(3):
                maxerr = max(maxerr, abs(float(g[i](*X)) - A1[i, p, q].item()))
                for j in range(3):
                    maxerr = max(maxerr, abs(float(h[i][j](*X)) - A2[i, j, p, q].item()))
    print(f"ladders vs sympy L={L}: max abs err {maxerr:.2e}")
    assert maxerr < 1e-10

def test_ladders_vs_fd(L=16):
    modes = mode_list(L, "all", l_min=0)
    pts = torch.tensor(np.random.default_rng(2).normal(size=(8, 3)) * 0.3)
    A0, A1, A2 = eval_solid(pts, modes, L, nderiv=2)
    h = 1e-3
    err1 = err2 = 0.0
    for i in range(3):
        e = torch.zeros(3); e[i] = h
        Ap, _, _ = eval_solid(pts + e, modes, L, 0); Am, _, _ = eval_solid(pts - e, modes, L, 0)
        A2p, A2m = eval_solid(pts + e, modes, L, 1)[1], eval_solid(pts - e, modes, L, 1)[1]
        # fourth-order central differences
        Ap2, _, _ = eval_solid(pts + 2*e, modes, L, 0); Am2, _, _ = eval_solid(pts - 2*e, modes, L, 0)
        fd1 = (8*(Ap - Am) - (Ap2 - Am2)) / (12*h)
        err1 = max(err1, ((fd1 - A1[i]).abs() / (1 + A1[i].abs())).max().item())
        A2p2, A2m2 = eval_solid(pts + 2*e, modes, L, 1)[1], eval_solid(pts - 2*e, modes, L, 1)[1]
        fd2 = (8*(A2p - A2m) - (A2p2 - A2m2)) / (12*h)
        err2 = max(err2, ((fd2 - A2[:, i]).abs() / (1 + A2[:, i].abs())).max().item())
    print(f"ladders vs 4th-order central FD (h={h}) L={L}: grad rel err {err1:.2e}, hess rel err {err2:.2e}")
    assert err1 < 1e-7 and err2 < 1e-7

def test_orthonormality_and_harmonicity(L=14):
    modes = mode_list(L, "all", l_min=0)
    g = AngularGrid(L + 2, 2*L + 3)
    A0, A1, A2 = angular_matrices(g, modes, L, 2)
    G = (A0 * g.w[:, None]).T @ A0
    err = (G - torch.eye(len(modes))).abs().max().item()
    lap = (A2[0, 0] + A2[1, 1] + A2[2, 2]).abs().max().item()
    # Euler homogeneity: n . grad P = l P on the unit sphere
    l_arr = torch.tensor([float(l) for (l, m, t) in modes])
    eul = (torch.einsum('ia,iaq->aq', g.n.T, A1) - l_arr[None, :] * A0).abs().max().item()
    print(f"orthonormality L={L}: {err:.2e}; harmonicity: {lap:.2e}; Euler identity: {eul:.2e}")
    assert err < 1e-12 and lap < 1e-11 and eul < 1e-11

def test_axis_regularity(L=12):
    modes = mode_list(L, "all", l_min=0)
    # points exactly on the axis and approaching it
    zs = torch.tensor([[0.0, 0.0, 0.8], [0.0, 0.0, -0.5], [0.0, 0.0, 0.0]])
    A0, A1, A2 = eval_solid(zs, modes, L, 2)
    assert torch.isfinite(A0).all() and torch.isfinite(A1).all() and torch.isfinite(A2).all()
    eps = 1e-7
    near = torch.tensor([[eps, 0.0, 0.8], [0.0, eps, -0.5], [eps, eps, 0.0]])
    B0, B1, B2 = eval_solid(near, modes, L, 2)
    d = max((A0-B0).abs().max().item(), (A1-B1).abs().max().item(), (A2-B2).abs().max().item())
    print(f"axis regularity L={L}: on-axis vs eps-offset difference {d:.2e} (expect O(eps))")
    assert d < 1e-3

if __name__ == "__main__":
    test_values_vs_scipy(); test_ladders_vs_sympy(); test_ladders_vs_fd(); test_orthonormality_and_harmonicity(); test_axis_regularity()
    print("ALL SOLID HARMONIC TESTS PASSED")
