"""Pressure solver tests (PROMPT.md section 7 item 7 and section 3 item 7): manufactured P with -Delta P = f computed by
sympy; Gaussian (compact) and power-law (algebraic tail) cases; P, grad P at random points, and the l=0 normalization.
Run: python3 tests/test_pressure.py"""
import os, sys, math, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np
import sympy as sp
from axi.pressure import PressureSolver

FAILS = []
def check(name, err, tol):
    ok = err <= tol
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: err={err:.3e} tol={tol:.1e}")
    if not ok: FAILS.append(name)

r, z = sp.symbols("r z", real=True)
R2 = r**2 + z**2
def lap3(P):   # axisymmetric 3D Laplacian
    return sp.diff(P, r, 2) + sp.diff(P, r) / r + sp.diff(P, z, 2)
rng = np.random.default_rng(3)

def run_case(name, Pexpr, edges, R_far, lmax, tolP, tolG, order=32):
    f = -lap3(Pexpr)      # not simplified: sympy may otherwise split exp(-R^2) into overflowing factors
    fl = sp.lambdify((r, z), f, "numpy"); Pl = sp.lambdify((r, z), Pexpr, "numpy")
    Prl = sp.lambdify((r, z), sp.diff(Pexpr, r), "numpy"); Pzl = sp.lambdify((r, z), sp.diff(Pexpr, z), "numpy")
    def f_func(R, mu):
        rr = R * np.sqrt(np.clip(1 - mu**2, 0, None)); zz = R * mu
        return np.asarray(fl(rr, zz), float) + 0 * R
    t0 = time.time()
    ps = PressureSolver(f_func, edges, R_far, lmax, n_mu=2 * lmax + 12, order=order)
    Rt = np.concatenate([rng.uniform(0.02, 3, 40), 10 ** rng.uniform(0.5, 3, 30)]); mut = rng.uniform(-1, 1, len(Rt))
    ev = ps.evaluate(Rt, mut)
    rr = Rt * np.sqrt(1 - mut**2); zz = Rt * mut
    Pe = np.asarray(Pl(rr, zz), float) + 0 * Rt; Pre = np.asarray(Prl(rr, zz), float) + 0 * Rt; Pze = np.asarray(Pzl(rr, zz), float) + 0 * Rt
    sc = np.max(np.abs(Pe)); scg = max(np.max(np.abs(Pre)), np.max(np.abs(Pze)))
    eP = np.max(np.abs(ev["P"] - Pe)) / sc
    eG = max(np.max(np.abs(ev["P_r"] - Pre)), np.max(np.abs(ev["P_z"] - Pze))) / scg
    print(f"  {name}: build {time.time()-t0:.1f}s, |P|max {sc:.3e}, tail_p[0:3] {ps.tail_p[:3]}, tail_rem[0] {ps.tail_rem[0]:.2e}")
    check(f"{name}: P at random points (relative to max |P|)", eP, tolP)
    check(f"{name}: grad P at random points (relative)", eG, tolG)
    # axis values (mu = +-1) are finite and match
    Ra = np.array([0.5, 1.0, 2.5, 20.0]); mua = np.array([1.0, -1.0, 1.0, -1.0])
    eva = ps.evaluate(Ra, mua)
    Pa = np.asarray(Pl(0 * Ra, Ra * mua), float)
    check(f"{name}: P on the axis", np.max(np.abs(eva["P"] - Pa)) / sc, tolP)

if __name__ == "__main__":
    t0 = time.time()
    # 1. Gaussian, odd + even parts, no symmetry
    P1 = sp.exp(-R2) * (1 + sp.Rational(3, 10) * z + sp.Rational(1, 5) * r**2) + sp.Rational(1, 10) * z * sp.exp(-R2 / 2)
    run_case("gaussian", P1, [0.0, 0.5, 2.0, 10.0], 1e6 * 10.0, 16, 1e-9, 1e-8)
    # 2. algebraic tail: P ~ R^-(2 beta) with angular dependence; f ~ R^-(2 beta + 2): tests the exterior integration and the analytic remainder
    beta = sp.Rational(7, 10)   # P ~ R^-1.4, f ~ R^-3.4 (like 2 alpha + 2 at c_l ~ 0.59)
    P2 = (1 + R2) ** (-beta) * (1 + sp.Rational(1, 2) * z / sp.sqrt(1 + R2) + sp.Rational(1, 4) * r**2 / (1 + R2))
    run_case("algebraic", P2, [0.0, 0.5, 2.0, 10.0], 1e6 * 10.0, 12, 1e-7, 1e-6)
    # 3. l = 0 normalization: f = 3 exp(-R^2) -> P = ... check against the direct radial formula with the solver (Gaussian monopole)
    P3 = sp.exp(-R2)
    run_case("monopole", P3, [0.0, 1.0, 4.0, 8.0], 1e5 * 8.0, 4, 1e-10, 1e-9)   # exterior panels start where the Gaussian is negligible
    print(f"\n{len(FAILS)} failures; total {time.time()-t0:.1f}s")
    if FAILS:
        print("FAILED:", FAILS); sys.exit(1)


def run_case_5d(name, phi_expr, edges, R_far, lmax, tol):
    """-Delta_5 phi = eta manufactured: the 5D Green inverse must reproduce phi and its gradient."""
    eta = -(sp.diff(phi_expr, r, 2) + 3 * sp.diff(phi_expr, r) / r + sp.diff(phi_expr, z, 2))
    el = sp.lambdify((r, z), eta, "numpy"); pl = sp.lambdify((r, z), phi_expr, "numpy")
    prl = sp.lambdify((r, z), sp.diff(phi_expr, r), "numpy"); pzl = sp.lambdify((r, z), sp.diff(phi_expr, z), "numpy")
    def f_func(R, mu):
        rr = R * np.sqrt(np.clip(1 - mu**2, 0, None)); zz = R * mu
        return np.asarray(el(rr, zz), float) + 0 * R
    ps = PressureSolver(f_func, edges, R_far, lmax, n_mu=2 * lmax + 12, dim=5)
    Rt = np.concatenate([rng.uniform(0.02, 3, 40), 10 ** rng.uniform(0.5, 3, 30)]); mut = rng.uniform(-1, 1, len(Rt))
    ev = ps.evaluate(Rt, mut)
    rr = Rt * np.sqrt(1 - mut**2); zz = Rt * mut
    Pe = np.asarray(pl(rr, zz), float) + 0 * Rt; Pre = np.asarray(prl(rr, zz), float) + 0 * Rt; Pze = np.asarray(pzl(rr, zz), float) + 0 * Rt
    sc = np.max(np.abs(Pe)); scg = max(np.max(np.abs(Pre)), np.max(np.abs(Pze)))
    check(f"5D {name}: phi at random points (relative)", np.max(np.abs(ev["P"] - Pe)) / sc, tol)
    check(f"5D {name}: grad phi at random points (relative)", max(np.max(np.abs(ev["P_r"] - Pre)), np.max(np.abs(ev["P_z"] - Pze))) / scg, 10 * tol)


if __name__ == "__main__" and "--5d" in sys.argv or __name__ == "__main__":
    t1 = time.time()
    phi1 = sp.exp(-R2) * (z + sp.Rational(1, 3) * r**2 * z + sp.Rational(1, 5)) + sp.Rational(1, 4) * z * sp.exp(-R2 / 3)
    run_case_5d("gaussian", phi1, [0.0, 0.5, 2.0, 10.0], 1e6 * 10.0, 14, 1e-9)
    beta = sp.Rational(7, 10)    # phi ~ R^-1.4 (like R^-alpha): eta ~ R^-3.4
    phi2 = (1 + R2) ** (-beta) * (z / sp.sqrt(1 + R2) + sp.Rational(1, 3) + sp.Rational(1, 4) * r**2 / (1 + R2))
    run_case_5d("algebraic", phi2, [0.0, 0.5, 2.0, 10.0], 1e6 * 10.0, 12, 1e-7)
    print(f"5D cases {time.time()-t1:.1f}s; total failures {len(FAILS)}")
    if FAILS:
        print("FAILED:", FAILS); sys.exit(1)
