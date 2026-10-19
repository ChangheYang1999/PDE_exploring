"""
Manufactured-solution tests of the per-mode full-plane inverse and of the transport residual.

rho = P(d_x, d_y) exp(-r^2) for a polynomial operator P.  With Phi the radial potential of exp(-r^2),
  -Lap Phi = exp(-r^2),  Phi'(r) = -(1 - exp(-r^2))/(2r),  Phi = -(1/4)(log r^2 + E_1(r^2)),
the exact stream function is psi = d_x P(d) Phi and U = (-psi_y, psi_x).  The code computes the
renormalized quantities psi - psi(0) - X.grad psi(0) (modes 0 and 1 fixed at the origin) and
V = U - U(0).  Decaying data => the Robin condition with zero tail is exact once exp(-R^2) ~ 0.
"""
import sys, math, time
import numpy as np
import sympy as sp
import torch
from scipy.special import exp1
sys.path.insert(0, "code")
from ipm2polar import Disc

torch.set_default_dtype(torch.float64)
x, y = sp.symbols("x y", real=True)
r2 = x ** 2 + y ** 2
Phi = -sp.Rational(1, 4) * (sp.log(r2) + sp.expint(1, r2))
G = sp.exp(-r2)


def make_case(coeffs):
    """coeffs: dict {(a,b): c} meaning rho = sum c d_x^a d_y^b exp(-r^2)."""
    rho = 0
    psi = 0
    for (a, b), c in coeffs.items():
        rho += c * sp.diff(G, x, a, y, b)
        psi += c * sp.diff(Phi, x, a + 1, y, b)
    U1 = -sp.diff(psi, y)
    U2 = sp.diff(psi, x)
    return rho, psi, U1, U2


def eval_np(expr, X, Y):
    """Evaluate a sympy expression (possibly containing expint(1,.)) on numpy arrays."""
    f = sp.lambdify((x, y), expr, modules=[{"expint": lambda n, z: exp1(z)}, "numpy"])
    return f(X, Y) * np.ones_like(X)


def taylor_coeffs(expr, nmax):
    """Return dict {(a,b): d_x^a d_y^b expr(0,0)} for a+b <= nmax, via a polar series in t."""
    t, w = sp.symbols("t w", positive=True)
    e = expr.subs({x: t * sp.cos(w), y: t * sp.sin(w)})
    ser = sp.series(e, t, 0, nmax + 1).removeO()
    out = {}
    for n in range(nmax + 1):
        coeff = sp.expand(ser.coeff(t, n))
        angs = [sp.Rational(k, n + 1) * sp.pi / 2 + sp.pi / 7 for k in range(n + 1)]
        A = sp.Matrix([[sp.cos(ww) ** (n - j) * sp.sin(ww) ** j for j in range(n + 1)] for ww in angs])
        rhs = sp.Matrix([coeff.subs(w, ww) for ww in angs])
        sol = A.LUsolve(rhs)
        for j in range(n + 1):
            a, b = n - j, j
            out[(a, b)] = float(sp.N(sol[j] * sp.factorial(a) * sp.factorial(b), 20))
    return out


def run_case(name, coeffs, Nr, Ntheta, R, L=1.0, K=2, cl=0.7, dev="cuda", verbose=True):
    rho_e, psi_e, U1_e, U2_e = make_case(coeffs)
    d = Disc(Nr, Ntheta, R, L=L, K=K, device=dev)
    th = d.theta_p.cpu().numpy()
    r = d.r_np
    TH, RR = np.meshgrid(th, r, indexing="ij")
    X, Y = RR * np.cos(TH), RR * np.sin(TH)
    rho_g = eval_np(rho_e, X, Y)
    psi_g = eval_np(psi_e, X, Y)
    U1_g = eval_np(U1_e, X, Y)
    U2_g = eval_np(U2_e, X, Y)
    tp = taylor_coeffs(psi_e, 2)
    tr = taylor_coeffs(rho_e, 2)
    psi0, psix0, psiy0 = tp[(0, 0)], tp[(1, 0)], tp[(0, 1)]
    U0 = (-psiy0, psix0)
    psi_ren_g = psi_g - psi0 - X * psix0 - Y * psiy0
    V1_g, V2_g = U1_g - U0[0], U2_g - U0[1]
    rx_g = eval_np(sp.diff(rho_e, x), X, Y)
    ry_g = eval_np(sp.diff(rho_e, y), X, Y)
    R_g = (cl * X + V1_g) * rx_g + (cl * Y + V2_g) * ry_g - rho_g
    # ---- code path
    rho_t = torch.tensor(rho_g, device=d.dev)
    rho_m = d.to_modes(rho_t)
    q = rho_m / d.rk
    out = d.residual_modes(q, cl, return_all=True)
    psi_c = d.to_phys(out["psi_m"]).cpu().numpy()
    Ur_c, Ut_c = out["Ur"].cpu().numpy(), out["Ut"].cpu().numpy()
    V1_c = Ur_c * np.cos(TH) - Ut_c * np.sin(TH)
    V2_c = Ur_c * np.sin(TH) + Ut_c * np.cos(TH)
    R_c = out["Rphys"].cpu().numpy()
    rho_c = out["rho"].cpu().numpy()
    f_c = d.to_phys(out["f_m"]).cpu().numpy()
    e = {}
    e["rho_interp"] = np.abs(rho_c - rho_g).max()
    e["dxrho"] = np.abs(f_c - rx_g).max() / np.abs(rx_g).max()
    e["psi"] = np.abs(psi_c - psi_ren_g).max() / np.abs(psi_ren_g).max()
    e["V1"] = np.abs(V1_c - V1_g).max() / max(np.abs(V1_g).max(), 1e-300)
    e["V2"] = np.abs(V2_c - V2_g).max() / max(np.abs(V2_g).max(), 1e-300)
    e["R"] = np.abs(R_c - R_g).max() / np.abs(rho_g).max()
    t_rho = [float(v) for v in d.taylor_rho(q)]
    t_rho_e = [tr[(0, 0)], tr[(1, 0)], tr[(0, 1)], tr[(2, 0)], tr[(1, 1)], tr[(0, 2)]]
    e["jet"] = max(abs(a - b) for a, b in zip(t_rho, t_rho_e))
    U0c, pxx, pxy, pyy = d.taylor_psi(out["p"])
    e["psiHess"] = max(abs(float(pxx) - tp[(2, 0)]), abs(float(pxy) - tp[(1, 1)]), abs(float(pyy) - tp[(0, 2)]))
    e["U0_code"] = max(abs(float(U0c[0])), abs(float(U0c[1])))
    if verbose:
        print("%-8s Nr=%3d Nth=%3d R=%5.1f K=%d | " % (name, Nr, Ntheta, R, K)
              + " ".join("%s=%.1e" % (k, v) for k, v in e.items()), flush=True)
    return e


CASES = {
    "T1_rad": {(0, 0): 1.0},
    "T2_dy": {(0, 1): 1.0},
    "T3_dxdy": {(1, 1): 1.0},
    "T4_asym": {(0, 0): 1.0, (1, 0): 0.3, (0, 1): 0.7, (1, 1): 0.2, (0, 2): -0.4, (3, 0): 0.1, (0, 3): 0.05,
                (2, 1): -0.15},
}

if __name__ == "__main__":
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    for name, co in CASES.items():
        for Nr in (32, 48, 64, 96):
            run_case(name, co, Nr, 32, 10.0, K=2, dev=dev)
    print("--- K dependence and R dependence for T4")
    for K in (0, 1, 2, 4, 6):
        run_case("T4_asym", CASES["T4_asym"], 64, 32, 10.0, K=K, dev=dev)
    for R in (6.0, 10.0, 20.0, 50.0):
        run_case("T4_asym", CASES["T4_asym"], 64, 32, R, K=2, dev=dev)
    for Nth in (16, 24, 48):
        run_case("T4_asym", CASES["T4_asym"], 64, Nth, 10.0, K=2, dev=dev)
