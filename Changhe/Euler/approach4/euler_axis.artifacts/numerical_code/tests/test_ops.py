"""Operator and manufactured-field tests (PROMPT.md section 3). Run: python3 tests/test_ops.py

All reference values come from sympy in cylindrical (r, z) or Cartesian (x, y, z) coordinates; the code
under test works from (R, mu) derivatives. Tolerances are float64 round-off level.
"""
import os, sys, math, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np
import sympy as sp
import torch
from axi import ops, basis

torch.set_default_dtype(torch.float64)
rng = np.random.default_rng(1234)
FAILS = []


def check(name, err, tol):
    ok = err <= tol
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: err={err:.3e} tol={tol:.1e}")
    if not ok:
        FAILS.append(name)


# ------------------------------------------------------------------ symbolic manufactured fields
r, z, R, mu = sp.symbols("r z R mu", positive=True)
cl_s = sp.Symbol("c_l", positive=True)


def manufactured(a, b, c):
    phi = sp.exp(-(r**2 + z**2)) * (1 + a * z)
    q = sp.exp(-(r**2 + z**2)) * (b + c * z)
    return phi, q


def to_Rmu(expr):
    return sp.simplify(expr.subs({r: R * sp.sqrt(1 - mu**2), z: R * mu}))


def deriv_dict(expr_rz, pts_R, pts_mu, maxord=3):
    """Numeric dict of d^i_R d^j_mu of expr at points, computed symbolically from the (r,z) expression."""
    e = expr_rz.subs({r: R * sp.sqrt(1 - mu**2), z: R * mu})
    out = {}
    for i in range(maxord + 1):
        for j in range(maxord + 1 - i):
            d = sp.diff(e, R, i, mu, j) if (i + j) > 0 else e
            f = sp.lambdify((R, mu), d, "numpy")
            out[(i, j)] = torch.tensor(np.asarray(f(pts_R, pts_mu), dtype=np.float64))
    return out


def sym_reduced(phi, q, cl):
    Ur = -r * sp.diff(phi, z)
    Uz = 2 * phi + r * sp.diff(phi, r)
    eta = -(sp.diff(phi, r, 2) + 3 * sp.diff(phi, r) / r + sp.diff(phi, z, 2))
    Wr = cl * r + Ur
    Wz = cl * z + Uz
    Rq = q + Wr * sp.diff(q, r) + Wz * sp.diff(q, z) + 2 * (Ur / r) * q
    Reta = (1 + cl) * eta + Wr * sp.diff(eta, r) + Wz * sp.diff(eta, z) - sp.diff(q**2, z)
    Ut = r * q
    Mr = (1 - cl) * Ur + Wr * sp.diff(Ur, r) + Wz * sp.diff(Ur, z) - Ut**2 / r
    Mt = (1 - cl) * Ut + Wr * sp.diff(Ut, r) + Wz * sp.diff(Ut, z) + Ur * Ut / r
    Mz = (1 - cl) * Uz + Wr * sp.diff(Uz, r) + Wz * sp.diff(Uz, z)
    div = sp.diff(Ur, r) + Ur / r + sp.diff(Uz, z)
    Om = sp.diff(Ur, z) - sp.diff(Uz, r)
    G = r * Ut
    RG = (1 - 2 * cl) * G + Wr * sp.diff(G, r) + Wz * sp.diff(G, z)
    return dict(Ur=Ur, Uz=Uz, Ut=Ut, eta=eta, Rq=Rq, Reta=Reta, Mr=Mr, Mt=Mt, Mz=Mz, div=div, Om=Om, RG=RG, G=G)


def lam(expr, pr, pz_):
    f = sp.lambdify((r, z), expr, "numpy")
    return np.asarray(f(pr, pz_), dtype=np.float64)


def test_manufactured():
    t0 = time.time()
    npts = 40
    pts_R = rng.uniform(0.05, 2.5, npts)
    pts_mu = rng.uniform(-0.999, 0.999, npts)
    pr = pts_R * np.sqrt(1 - pts_mu**2)
    pz_ = pts_R * pts_mu
    for (a, b, c, cl) in [(0.7, 1.3, -0.4, 0.6), (-1.1, 0.5, 0.9, 0.52), (0.3, -0.8, 0.6, 0.7)]:
        phi, q = manufactured(a, b, c)
        S = sym_reduced(phi, q, cl)
        g = ops.geom(torch.tensor(pts_R), torch.tensor(pts_mu))
        phid = deriv_dict(phi, pts_R, pts_mu, 3)
        qd = deriv_dict(q, pts_R, pts_mu, 1)
        Rq, Reta, aux = ops.reduced_residuals(phid, qd, g, cl)
        scale = lambda arr: max(1.0, np.max(np.abs(arr)))
        ref = lam(S["Rq"], pr, pz_); check(f"R_q vs sympy (a,b,c,cl)={(a,b,c,cl)}", np.max(np.abs(Rq.numpy() - ref)) / scale(ref), 1e-12)
        ref = lam(S["Reta"], pr, pz_); check(f"R_eta vs sympy {(a,b,c,cl)}", np.max(np.abs(Reta.numpy() - ref)) / scale(ref), 1e-11)
        ref = lam(S["eta"], pr, pz_); check(f"eta=-Delta_5 phi vs Omega^theta/r {(a,b,c,cl)}", np.max(np.abs(aux["eta"].numpy() - ref)) / scale(ref), 1e-12)
        ref = lam(S["Om"] / r, pr, pz_); check(f"Omega^theta/r (sympy curl) vs -Delta_5 phi {(a,b,c,cl)}", np.max(np.abs(aux["eta"].numpy() - ref)) / scale(ref), 1e-12)
        ref = lam(S["Ur"], pr, pz_); check(f"U^r {(a,b,c,cl)}", np.max(np.abs(aux["Ur"].numpy() - ref)) / scale(ref), 1e-13)
        ref = lam(S["Uz"], pr, pz_); check(f"U^z {(a,b,c,cl)}", np.max(np.abs(aux["Uz"].numpy() - ref)) / scale(ref), 1e-13)
        # Gamma-equation equivalence: (1-2cl)Gamma + W.grad Gamma = r^2 R_q  (exact identity)
        RG, G = ops.gamma_residual(phid, qd, g, cl)
        check(f"Gamma eq = r^2 R_q {(a,b,c,cl)}", np.max(np.abs(RG.numpy() - (pr**2) * Rq.numpy())) / scale(RG.numpy()), 1e-12)
        ref = lam(S["RG"], pr, pz_); check(f"Gamma eq vs sympy {(a,b,c,cl)}", np.max(np.abs(RG.numpy() - ref)) / scale(ref), 1e-12)
        # primitive pieces
        P = ops.primitive_terms(phid, qd, g, cl)
        check(f"divergence identically zero {(a,b,c,cl)}", np.max(np.abs(P["div"].numpy())), 1e-13)
        ref = lam(S["div"], pr, pz_); check(f"sympy divergence zero {(a,b,c,cl)}", np.max(np.abs(ref)), 1e-13)
        ref = lam(S["Mt"], pr, pz_); check(f"M_theta vs sympy {(a,b,c,cl)}", np.max(np.abs(P["Mt"].numpy() - ref)) / scale(ref), 1e-12)
        check(f"M_theta = r R_q {(a,b,c,cl)}", np.max(np.abs(P["Mt"].numpy() - pr * Rq.numpy())) / scale(ref), 1e-12)
        ref = lam(S["Mr"], pr, pz_); check(f"M_r vs sympy {(a,b,c,cl)}", np.max(np.abs(P["Mr"].numpy() - ref)) / scale(ref), 1e-12)
        ref = lam(S["Mz"], pr, pz_); check(f"M_z vs sympy {(a,b,c,cl)}", np.max(np.abs(P["Mz"].numpy() - ref)) / scale(ref), 1e-12)
        # curl of meridional momentum equals r R_eta (exact identity, derived in NUMERICAL_METHODS.md)
        curlM = sp.diff(S["Mr"], z) - sp.diff(S["Mz"], r)
        ref = lam(curlM, pr, pz_); check(f"d_z M_r - d_r M_z = r R_eta {(a,b,c,cl)}", np.max(np.abs(ref - pr * Reta.numpy())) / scale(ref), 1e-11)
        # Omega^theta from primitive pieces
        ref = lam(S["Om"], pr, pz_); check(f"Omega^theta primitive {(a,b,c,cl)}", np.max(np.abs(P["Om_theta"].numpy() - ref)) / scale(ref), 1e-12)
    print(f"  manufactured tests done in {time.time()-t0:.1f}s")


def test_cartesian_source_and_momentum():
    """Pressure Poisson source and momentum: cylindrical formulas vs a fully Cartesian sympy calculation."""
    x, y, zz = sp.symbols("x y z", real=True)
    a, b, c, cl = 0.6, 1.1, -0.7, 0.62
    rr = sp.sqrt(x**2 + y**2)
    phi = sp.exp(-(rr**2 + zz**2)) * (1 + a * zz)
    q = sp.exp(-(rr**2 + zz**2)) * (b + c * zz)
    Ur = -rr * sp.diff(phi, zz)
    Uz = 2 * phi + rr * sp.diff(phi, rr) if False else 2 * phi + (x * sp.diff(phi, x) + y * sp.diff(phi, y))  # r d_r = x d_x + y d_y
    Ut = rr * q
    Ux = Ur * x / rr - Ut * y / rr
    Uy = Ur * y / rr + Ut * x / rr
    U = [Ux, Uy, Uz]
    X = [x, y, zz]
    Ssym = sum(sp.diff(U[j], X[i]) * sp.diff(U[i], X[j]) for i in range(3) for j in range(3))
    Mom = [(1 - cl) * U[k] + sum((cl * X[i] + U[i]) * sp.diff(U[k], X[i]) for i in range(3)) for k in range(3)]
    divc = sum(sp.diff(U[i], X[i]) for i in range(3))
    npts = 12
    px = rng.uniform(-1.5, 1.5, npts); py = rng.uniform(-1.5, 1.5, npts); pzz = rng.uniform(-1.5, 1.5, npts)
    fS = sp.lambdify((x, y, zz), Ssym, "numpy"); fM = [sp.lambdify((x, y, zz), m, "numpy") for m in Mom]
    fdiv = sp.lambdify((x, y, zz), divc, "numpy")
    pr = np.sqrt(px**2 + py**2); pR = np.sqrt(pr**2 + pzz**2); pmu = pzz / pR
    g = ops.geom(torch.tensor(pR), torch.tensor(pmu))
    phi_rz = sp.exp(-(r**2 + z**2)) * (1 + a * z); q_rz = sp.exp(-(r**2 + z**2)) * (b + c * z)
    phid = deriv_dict(phi_rz, pR, pmu, 3); qd = deriv_dict(q_rz, pR, pmu, 1)
    P = ops.primitive_terms(phid, qd, g, cl)
    refS = np.asarray(fS(px, py, pzz), float)
    check("pressure source S cylindrical vs Cartesian", np.max(np.abs(P["S"].numpy() - refS)) / max(1, np.max(np.abs(refS))), 1e-12)
    check("Cartesian divergence zero", np.max(np.abs(np.asarray(fdiv(px, py, pzz), float))), 1e-12)
    Mx, My, Mz = [np.asarray(f(px, py, pzz), float) for f in fM]
    cth, sth = px / pr, py / pr
    Mr_c = Mx * cth + My * sth; Mt_c = -Mx * sth + My * cth
    sc = max(1, np.max(np.abs(Mr_c)))
    check("M_r cylindrical vs Cartesian (swirl curvature term)", np.max(np.abs(P["Mr"].numpy() - Mr_c)) / sc, 1e-12)
    check("M_theta cylindrical vs Cartesian", np.max(np.abs(P["Mt"].numpy() - Mt_c)) / sc, 1e-12)
    check("M_z cylindrical vs Cartesian", np.max(np.abs(P["Mz"].numpy() - Mz)) / sc, 1e-12)


def test_dilation_covariance():
    """phi_L(y) = L phi(y/L), q_L(y) = q(y/L): R_q,L(y) = R_q(y/L), R_eta,L(y) = L^-1 R_eta(y/L)."""
    a, b, c, cl, L = 0.4, 0.9, 0.5, 0.58, 1.7
    phi, q = manufactured(a, b, c)
    phiL = L * phi.subs({r: r / L, z: z / L}, simultaneous=True)
    qL = q.subs({r: r / L, z: z / L}, simultaneous=True)
    npts = 20
    pts_R = rng.uniform(0.1, 2.0, npts); pts_mu = rng.uniform(-0.99, 0.99, npts)
    g = ops.geom(torch.tensor(pts_R), torch.tensor(pts_mu))
    gL = ops.geom(torch.tensor(pts_R / L), torch.tensor(pts_mu))
    RqL, RetaL, _ = ops.reduced_residuals(deriv_dict(phiL, pts_R, pts_mu), deriv_dict(qL, pts_R, pts_mu, 1), g, cl)
    Rq, Reta, _ = ops.reduced_residuals(deriv_dict(phi, pts_R / L, pts_mu), deriv_dict(q, pts_R / L, pts_mu, 1), gL, cl)
    check("dilation covariance R_q", np.max(np.abs(RqL.numpy() - Rq.numpy())) / max(1, np.max(np.abs(Rq.numpy()))), 1e-12)
    check("dilation covariance R_eta (L^-1)", np.max(np.abs(RetaL.numpy() - Reta.numpy() / L)) / max(1, np.max(np.abs(Reta.numpy()))), 1e-12)


def test_axis_limits():
    """Axis regularity: at mu -> +-1 (r=0) the code must give finite, correct values with no NaN."""
    a, b, c, cl = 0.7, 1.3, -0.4, 0.6
    phi, q = manufactured(a, b, c)
    pts_R = np.array([0.3, 0.9, 1.7, 0.3, 0.9]); pts_mu = np.array([1.0, 1.0, 1.0, -1.0, -1.0])
    g = ops.geom(torch.tensor(pts_R), torch.tensor(pts_mu))
    Rq, Reta, aux = ops.reduced_residuals(deriv_dict(phi, pts_R, pts_mu), deriv_dict(q, pts_R, pts_mu, 1), g, cl)
    S = sym_reduced(phi, q, cl)
    # reference on the axis by symbolic limit r->0
    refRq = np.array([float(sp.limit(S["Rq"].subs(z, zz), r, 0)) for zz in pts_R * pts_mu])
    refReta = np.array([float(sp.limit(S["Reta"].subs(z, zz), r, 0)) for zz in pts_R * pts_mu])
    check("axis limit R_q finite and correct", np.max(np.abs(Rq.numpy() - refRq)), 1e-12)
    check("axis limit R_eta finite and correct", np.max(np.abs(Reta.numpy() - refReta)), 1e-11)
    P = ops.primitive_terms(deriv_dict(phi, pts_R, pts_mu), deriv_dict(q, pts_R, pts_mu, 1), g, cl)
    check("axis: U^r = 0", np.max(np.abs(P["Ur"].numpy())), 1e-14)
    check("axis: U^theta = 0", np.max(np.abs(P["Ut"].numpy())), 1e-14)
    check("axis: no NaN in primitive pieces", float(sum(np.isnan(v.numpy()).sum() for v in P.values())), 0)


def test_basis_reproduction():
    """Ball basis reproduces an axisymmetric Cartesian polynomial exactly; exterior reproduces its ansatz."""
    # ball
    R1, nmax, D = 2.0, 8, 12
    el = basis.make_element("ball", 0.0, R1, nmax, {"D": D}, nR=14, nmu=12)
    f = (r**2 + z)**3 + z * r**4 + 0.3 * z**5 * r**2 - r**6   # degree 7 axisymmetric polynomial
    fd = deriv_dict(f, el.R, el.mu, 3)
    coef, *_ = np.linalg.lstsq(el.B[(0, 0)], fd[(0, 0)].numpy(), rcond=None)
    # check all derivatives at fresh points
    Rt = rng.uniform(0.01, R1, 30); mut = rng.uniform(-1, 1, 30)
    Bt = el.eval_at(Rt, mut)
    ft = deriv_dict(f, Rt, mut, 3)
    err = max(np.max(np.abs(Bt[k] @ coef - ft[k].numpy())) / max(1, np.max(np.abs(ft[k].numpy()))) for k in basis.DERIV_KEYS)
    check("ball basis exact for degree-7 polynomial (all derivatives to order 3)", err, 1e-10)
    el_j = basis.make_element("ball", 0.0, R1, nmax, {"D": D, "radial": "jacobi"}, nR=14, nmu=12)
    coef_j, *_ = np.linalg.lstsq(el_j.B[(0, 0)], fd[(0, 0)].numpy(), rcond=None)
    Btj = el_j.eval_at(Rt, mut)
    err = max(np.max(np.abs(Btj[k] @ coef_j - ft[k].numpy())) / max(1, np.max(np.abs(ft[k].numpy()))) for k in basis.DERIV_KEYS)
    check("ball basis (jacobi radial) exact for degree-7 polynomial (all derivatives to order 3)", err, 1e-10)
    # Jacobi derivative formula vs finite differences
    xq = np.linspace(-0.9, 0.9, 7)
    Pd = basis.jacobi_derivs_x(xq, 6, 0.0, 3.5)
    h = 1e-5
    fd1 = (basis.jacobi_values(xq + h, 6, 0.0, 3.5) - basis.jacobi_values(xq - h, 6, 0.0, 3.5)) / (2 * h)
    check("jacobi first derivative vs central FD", np.max(np.abs(Pd[1] - fd1)) / np.max(np.abs(fd1)), 1e-8)
    fd2 = (basis.jacobi_values(xq + h, 6, 0.0, 3.5) - 2 * basis.jacobi_values(xq, 6, 0.0, 3.5) + basis.jacobi_values(xq - h, 6, 0.0, 3.5)) / h**2
    check("jacobi second derivative vs FD", np.max(np.abs(Pd[2] - fd2)) / np.max(np.abs(fd2)), 1e-5)
    cj = np.linalg.cond(el_j.B[(0, 0)] / np.max(np.abs(el_j.B[(0, 0)]), axis=0)); cc = np.linalg.cond(el.B[(0, 0)] / np.max(np.abs(el.B[(0, 0)]), axis=0))
    print(f"  ball value-matrix condition (column-scaled): chebyshev {cc:.2e}, jacobi {cj:.2e}")
    # a function odd in z (no parity imposed): z*exp(-R^2) should be approximated spectrally
    el2 = basis.make_element("ball", 0.0, 1.5, 20, {"D": 40}, nR=30, nmu=24)
    fo = z * sp.exp(-(r**2 + z**2)) + r**2 * sp.cos(z)
    fd = deriv_dict(fo, el2.R, el2.mu, 0)
    coef, *_ = np.linalg.lstsq(el2.B[(0, 0)], fd[(0, 0)].numpy(), rcond=None)
    Rt = rng.uniform(0.01, 1.5, 50); mut = rng.uniform(-1, 1, 50)
    Bt = el2.eval_at(Rt, mut); ft = deriv_dict(fo, Rt, mut, 2)
    err = max(np.max(np.abs(Bt[k] @ coef - ft[k].numpy())) for k in [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)])
    check("ball basis spectral approximation of smooth non-symmetric field (D=40), derivs to order 2", err, 1e-9)
    # shell
    el3 = basis.make_element("shell", 1.0, 8.0, 10, {"K": 24, "map": "log"}, nR=30, nmu=14)
    fs = (1 + 0.3 * z) / (1 + r**2 + z**2) + z / (4 + r**2 + z**2)**2 + 0.2 * r**2 * z / (1 + r**2 + z**2)**sp.Rational(5, 2)
    fd = deriv_dict(fs, el3.R, el3.mu, 0)
    coef, *_ = np.linalg.lstsq(el3.B[(0, 0)], fd[(0, 0)].numpy(), rcond=None)
    Rt = rng.uniform(1.0, 8.0, 50); mut = rng.uniform(-1, 1, 50)
    Bt = el3.eval_at(Rt, mut); ft = deriv_dict(fs, Rt, mut, 2)
    err = max(np.max(np.abs(Bt[k] @ coef - ft[k].numpy())) for k in [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)])
    check("shell basis (log map, K=24, nmax=10) smooth field, derivs to order 2", err, 1e-6)
    # exterior
    alpha = 0.55
    exps = basis.exterior_exponents(alpha, 6.0, "phi")
    el4 = basis.make_element("exterior", 6.0, math.inf, 6, {"exponents": exps}, nR=2 * len(exps) + 4, nmu=8)   # >= 2 nodes per exponent over the six-decade node range (conditioning)
    Rs = sp.Symbol("Rs", positive=True)
    fe = (r**2 + z**2)**(-alpha / 2) * (1 + 0.5 * z**2 / (r**2 + z**2)) + 0.7 * (r**2 + z**2)**(-(2 * alpha + 1) / 2) * z / sp.sqrt(r**2 + z**2) - 0.2 * (r**2 + z**2)**(-sp.Rational(3, 2))
    fd = deriv_dict(fe, el4.R, el4.mu, 0)
    # nodes span six decades (R up to 1e6 Rm), so the plain lstsq matrix has columns ranging over ~36 orders of
    # magnitude; scale columns to unit max before the fit (the solver's LM scaling does the equivalent).
    A0 = el4.B[(0, 0)]; cs = np.max(np.abs(A0), axis=0)
    coef, *_ = np.linalg.lstsq(A0 / cs, fd[(0, 0)].numpy(), rcond=None); coef = coef / cs
    Rt = 6.0 / rng.uniform(0.01, 1.0, 40); mut = rng.uniform(-1, 1, 40)
    Bt = el4.eval_at(Rt, mut); ft = deriv_dict(fe, Rt, mut, 3)
    err = max(np.max(np.abs(Bt[k] @ coef - ft[k].numpy())) / max(1e-3, np.max(np.abs(ft[k].numpy()))) for k in basis.DERIV_KEYS)
    check(f"exterior basis exact for its ansatz (alpha={alpha}, {len(exps)} exponents), relative, derivs to order 3", err, 1e-9)
    print("  exterior exponents phi:", [round(e, 4) for e in exps])
    print("  exterior exponents q  :", [round(e, 4) for e in basis.exterior_exponents(alpha, 6.0, 'q')])


def test_dtype():
    el = basis.make_element("ball", 0.0, 1.0, 4, {"D": 6}, nR=6, nmu=6)
    assert all(v.dtype == np.float64 for v in el.B.values())
    t = torch.tensor(el.B[(0, 0)])
    check("float64 dtype of basis matrices and torch tensors", 0.0 if t.dtype == torch.float64 else 1.0, 0)


if __name__ == "__main__":
    t0 = time.time()
    test_dtype()
    test_basis_reproduction()
    test_manufactured()
    test_cartesian_source_and_momentum()
    test_dilation_covariance()
    test_axis_limits()
    print(f"\n{len(FAILS)} failures; total time {time.time()-t0:.1f}s")
    if FAILS:
        print("FAILED:", FAILS)
        sys.exit(1)
