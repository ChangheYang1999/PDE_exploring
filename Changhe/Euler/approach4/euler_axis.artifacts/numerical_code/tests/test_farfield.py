"""Far-field first correction (axi.farfield): for random low-degree (A, B), the two-term tails phi0 + phi1, q0 + q1 must make the scaled
residuals R^(2 alpha + 2) R_q and R^(2 alpha + 3) R_eta decay like R^-(1/c) (the next order), whereas the leading tail alone leaves them
constant in R.  Also checks the algebraic identities 1 - c(2 alpha + 2) = -1 and 1 + c - c(2 alpha + 3) = -1 by construction."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np, torch
from axi import basis, ops
from axi.farfield import first_correction
torch.set_default_dtype(torch.float64)
FAILS = []
def check(name, err, tol):
    ok = err <= tol; print(f"[{'PASS' if ok else 'FAIL'}] {name}: err={err:.3e} tol={tol:.1e}")
    if not ok: FAILS.append(name)

def tail_fields(coefs_exps, mu, R):
    """phi (or q) = sum_k R^-e_k sum_n c_kn P_n(mu): derivative dict to third order."""
    nmax = max(len(c) for c, e in coefs_exps) - 1
    Pm = basis.legendre_derivs(mu, nmax, 3)
    out = {k: np.zeros_like(R) for k in basis.DERIV_KEYS}
    for c, e in coefs_exps:
        pw = basis.power_derivs(R, -e)
        cc = np.zeros(nmax + 1); cc[:len(c)] = c
        for (i, j) in basis.DERIV_KEYS:
            out[(i, j)] += pw[i] * (Pm[j] @ cc)
    return {k: torch.tensor(v) for k, v in out.items()}

rng = np.random.default_rng(1)
for cl in (0.56, 0.6, 0.68, 0.74):
    alpha = (1 - cl) / cl
    a = np.zeros(7); b = np.zeros(7); a[:4] = rng.normal(size=4); b[:3] = rng.normal(size=3)
    a1, b1, info = first_correction(a, b, alpha, nmax_out=14)
    mu = np.linspace(-0.95, 0.95, 41)
    def scaled_res(with_corr, R):
        Rv = np.full_like(mu, R)
        phi = tail_fields([(a, alpha)] + ([(a1, 2 * alpha + 1)] if with_corr else []), mu, Rv)
        q = tail_fields([(b, alpha + 1)] + ([(b1, 2 * alpha + 2)] if with_corr else []), mu, Rv)
        g = ops.geom(torch.tensor(Rv), torch.tensor(mu))
        Rq, Reta, _ = ops.reduced_residuals(phi, q, g, cl)
        return float(np.sqrt(np.mean((R ** (2 * alpha + 2) * Rq.numpy()) ** 2))), float(np.sqrt(np.mean((R ** (2 * alpha + 3) * Reta.numpy()) ** 2)))
    r0 = [scaled_res(False, R) for R in (1e2, 1e3, 1e4)]
    r1 = [scaled_res(True, R) for R in (1e2, 1e3, 1e4)]
    print(f"c_l={cl}: leading only  scaled (R_q, R_eta) at R=1e2,1e3,1e4: " + " ".join(f"({q:.2e},{e:.2e})" for q, e in r0))
    print(f"         with correction                              : " + " ".join(f"({q:.2e},{e:.2e})" for q, e in r1) + f"   trunc {info}")
    # leading only: constant in R (ratio ~1); with correction: decays like R^-(1/c) per decade = 10^-(1/c)
    check(f"c_l={cl}: leading-only scaled residuals are R-independent", abs(r0[2][1] / r0[0][1] - 1) + abs(r0[2][0] / r0[0][0] - 1), 1e-6)
    expected = 10.0 ** (-2 / cl)      # two decades
    check(f"c_l={cl}: corrected scaled R_q decays like R^-(1/c) (ratio 1e4/1e2 vs 10^(-2/c))", abs(r1[2][0] / r1[0][0] / expected - 1), 0.3)
    check(f"c_l={cl}: corrected scaled R_eta decays like R^-(1/c)", abs(r1[2][1] / r1[0][1] / expected - 1), 0.3)
    check(f"c_l={cl}: corrected residual at R=1e3 is far below leading-only", (r1[1][0] + r1[1][1]) / (r0[1][0] + r0[1][1]), 1e-2)
print(f"\n{len(FAILS)} failures")
if FAILS: print("FAILED:", FAILS); sys.exit(1)
