"""Stage II S8 implementation tests I1-I4 (lead reports/stage2_plan_draft.md, 2026-10-25T05:14:51Z).
I1: Delta U from the potentials (Model.laplacian_points) against the exact AD Laplacian (sum_m d_m of DU by forward-mode AD in the point),
    on a random L4 state with channels, at random points incl. axis points; also laplacian_grid against laplacian_points on the grid nodes.
I2: the rate alpha+2 viscous coefficient: Delta[r^-P e^(-i m kappa log r) P_q] = B r^(-P-2) e^(-i m kappa log r) P_q with
    B = (-P - i m kappa)(1 + 2 l - P - i m kappa) by sympy (exact), and end to end: with the inhomogeneous tail constraints the far field
    of R^nu = R_u - nu Delta U decays faster than r^-(alpha+2) (the rate alpha+2 part is balanced), while with the homogeneous constraints
    r^(alpha+2) RMS(R^nu) tends to a nonzero constant.
I3: ball identity int_B U.R^nu = beta_0 E(R) + (c_l R/2) E'(R) + int_S (P + |U|^2/2) U.n + nu int_B |DU|^2 - nu int_S U.(n.grad)U on a
    random state (quadrature accuracy).
I4: at nu = 0 the viscous residual vector equals the Stage I residual vector exactly."""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model, alpha_of
from src.optimization.problem import Problem

def test_I1(device):
    torch.manual_seed(3)
    model = Model(L=4, Nk=8, m_parity="even", R0=0.5, Nr=24, c_l=0.45, omega=0.7, channels=dict(NkB=2, NkD=2, NkE=2), device=device)
    z = torch.randn(model.n_z, device=device) * 0.3
    pts = torch.cat([torch.randn(30, 3, device=device) * 0.6, torch.tensor([[0.0, 0.0, 0.3], [0.0, 0.0, -1.2], [0.0, 0.0, 0.0]], device=device)], 0)
    lap = model.laplacian_points(z, pts)                                    # (3, Np)
    ad = torch.zeros_like(lap)
    for m in range(3):
        e = torch.zeros_like(pts); e[:, m] = 1.0
        _, jg = torch.func.jvp(lambda q: model.fields_points(z, q, need_vort=False)["GU"], (pts,), (e,))   # d_m (d_m' U_i) -> take m' = m
        ad = ad + jg[m]
    e1 = float((lap - ad).norm() / ad.norm())
    lg = model.laplacian_grid(z); lp = model.laplacian_points(z, model.y.reshape(-1, 3)).reshape(3, model.Nr, model.Na)
    e2 = float((lg - lp).norm() / lg.norm())
    print(f"I1 Delta U: potentials vs AD Laplacian {e1:.2e} (33 points incl. axis and origin); grid vs points {e2:.2e}")
    return e1 < 1e-10 and e2 < 1e-12

def test_I2_sympy():
    """Delta[r^-P e^(-i m kappa log r) P_q(y)] = B r^(-P-2) e^(-i m kappa log r) P_q with B = (-P - i m kappa)(1 + 2 l - P - i m kappa): exact check with
    sympy for the degree-2 solid harmonics P = x^2 - y^2 (l = 2, m = 2 cos) and P = xz (l = 2, m = 1), P = 2 z^2 - x^2 - y^2 (l = 2, m = 0)."""
    import sympy as sp
    x, y, z = sp.symbols('x y z', real=True); P_, kap = sp.symbols('P kappa', positive=True)
    r = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
    worst = 0.0
    for Pq, l, m in ((x ** 2 - y ** 2, 2, 2), (x * z, 2, 1), (2 * z ** 2 - x ** 2 - y ** 2, 2, 0), (x, 1, 1)):
        f = r ** (-P_) * sp.exp(-sp.I * m * kap * sp.log(r)) * Pq
        lap = sp.diff(f, x, 2) + sp.diff(f, y, 2) + sp.diff(f, z, 2)
        B = (-P_ - sp.I * m * kap) * (1 + 2 * l - P_ - sp.I * m * kap)
        ratio = sp.simplify(lap / (B * r ** (-P_ - 2) * sp.exp(-sp.I * m * kap * sp.log(r)) * Pq))
        val = complex(ratio.subs({x: 0.3, y: -0.7, z: 0.4, P_: 2.37, kap: 0.8}))
        worst = max(worst, abs(val - 1.0))
    print(f"I2 (sympy): Delta of the twisted power mode equals B times the next power, worst |ratio - 1| = {worst:.1e}")
    return worst < 1e-12


def _far_terms(model, z, c_l, omega, radii, nu, device):
    from src.pressure.poisson_sh import PressureSolver
    from src.equations import residuals as res
    from src.validation.spec_diagnostics import five_term_split
    Lx = getattr(model, "L_ext", model.L)
    em = Model(L=model.L, Nk=model.Nk, m_parity=model.m_parity, R0=model.R0, r_nodes=radii, ntheta=2 * Lx + 12, nphi=4 * Lx + 18, c_l=model.c_l0, omega=model.omega0,
               free_params=model.free_params, channels=model.channels, device=device, phi0=0.123)
    F = em.fields_grid(z, need_vort=False)
    ps = PressureSolver(model, p0=2 * alpha_of(c_l) + 2, omega=omega, c_l=c_l, eval_model=em)
    P, gradP, _, _ = ps.solve(res.pressure_source(model.fields_grid(z, need_vort=False)["GU"]))
    T = five_term_split(F, gradP); lap = em.laplacian_grid(z)
    Rnu = sum(T) - nu * lap
    w = em.grid.w / (4 * math.pi)
    rms = lambda X: ((X ** 2).sum(0) * w[None, :]).sum(1).sqrt()          # per radius
    return rms(Rnu), rms(F["U"]), rms(lap), P, F, gradP, em, T, lap


def test_I2_farfield(device):
    """With the inhomogeneous tail constraints the rate alpha+2 part of R^nu is balanced: r^(alpha+2) RMS(R^nu) on far spheres decays,
    while with the homogeneous constraints it tends to a nonzero constant (the viscous forcing of the leading tail)."""
    from src.optimization.tail_constraints import TailConstraints
    torch.manual_seed(5)
    c_l, omega, nu = 0.45, 0.7, 0.02
    model = Model(L=4, Nk=10, m_parity="even", R0=0.5, Nr=30, c_l=c_l, omega=omega, device=device)
    zr = torch.randn(TailConstraints(model).n_red, device=device) * 0.3
    z_h = TailConstraints(model, nu=0.0).expand(zr); z_v = TailConstraints(model, nu=nu).expand(zr)
    alpha = alpha_of(c_l)
    radii = model.R0 * 2.0 ** np.array([14.0, 16.0, 18.0, 20.0])     # beyond 2^14 R0 the rate alpha+3 term of a random state (coefficient ~ sum k^6 a_k) has decayed; beyond 2^20 R0 the K = 6 Chebyshev derivatives are roundoff-limited
    out = {}
    w_ang = None
    for name, zz in (("homogeneous", z_h), ("inhomogeneous", z_v)):
        rR, rU, rL, P, F, gradP, em, T, lap = _far_terms(model, zz, c_l, omega, radii, nu, device)
        # the rate alpha+2 balance is a statement about the LINEAR viscous operator L U - nu Delta U (the nonlinear terms decay like
        # r^-(2 alpha + 1), only r^-(alpha - 1) faster than rate alpha + 2, and dominate the full residual of a random state at these radii)
        w = em.grid.w / (4 * math.pi)
        Rlin = T[0] + T[1] + T[2] - nu * lap
        rms = ((Rlin ** 2).sum(0) * w[None, :]).sum(1).sqrt()
        scaled = (torch.tensor(radii, device=device) ** (alpha + 2) * rms).cpu().numpy()
        out[name] = scaled
    ratio_last = out["inhomogeneous"][-1] / out["homogeneous"][-1]
    decay = out["inhomogeneous"][-1] / out["inhomogeneous"][0]
    const = out["homogeneous"][-1] / out["homogeneous"][-2]
    print("I2 (far field): r^(alpha+2) RMS(L U - nu Delta U) at r/R0 = 2^14..2^20: homogeneous constraints", ["%.3e" % v for v in out["homogeneous"]],
          "| inhomogeneous", ["%.3e" % v for v in out["inhomogeneous"]], f"| ratio at 2^20: {ratio_last:.1e} (homogeneous -> the viscous constant nu |Delta U_0|, inhomogeneous -> rate alpha+3 decay)")
    return ratio_last < 3e-2 and 0.9 < const < 1.1 and decay < 0.05


def test_I3(device):
    """Ball identity int_B U.R^nu = beta_0 E + (c_l R/2) E' + R^2 int (P + |U|^2/2) U.n + nu int_B |DU|^2 - nu R^2 int U.(n.grad)U."""
    from src.pressure.poisson_sh import PressureSolver
    from src.equations import residuals as res
    from src.validation.spec_diagnostics import five_term_split
    torch.manual_seed(8)
    c_l, omega, nu = 0.45, 0.7, 0.03
    model = Model(L=4, Nk=8, m_parity="even", R0=0.5, Nr=24, c_l=c_l, omega=omega, channels=dict(NkB=2, NkD=2, NkE=2), device=device)
    z = torch.randn(model.n_z, device=device) * 0.3
    R = 1.3; nq = 64
    xg, wg = np.polynomial.legendre.leggauss(nq); rq = 0.5 * R * (xg + 1); wq = 0.5 * R * wg * rq ** 2
    radii = np.concatenate([rq, [R]])
    rR, rU, rL, P, F, gradP, em, T, lap = _far_terms(model, z, c_l, omega, radii, nu, device)
    U, GU = F["U"], F["GU"]; Rnu = sum(T) - nu * lap
    w = em.grid.w                                                       # sum 4 pi
    def ball(fn):                                                       # fn (Nr, Na) -> int_B
        per_r = (fn[:nq] * w[None, :]).sum(1)
        return float((per_r * torch.tensor(wq, device=device)).sum())
    def sphere(fn):                                                     # at the last radius R
        return float((fn[nq] * w).sum()) * R ** 2
    n = em.grid.n.T                                                     # (3, Na)
    lhs = ball((U * Rnu).sum(0))
    E = ball((U ** 2).sum(0)); Ep = sphere((U ** 2).sum(0))
    Un = (U[:, nq, :] * n).sum(0)
    flux = float((((P[nq] + 0.5 * (U[:, nq, :] ** 2).sum(0)) * Un) * w).sum()) * R ** 2
    D = ball((GU ** 2).sum((0, 1)))
    dnU = torch.einsum('m a,m i a->i a', n, GU[:, :, nq, :])              # (n.grad) U
    bvisc = float((((U[:, nq, :] * dnU).sum(0)) * w).sum()) * R ** 2
    beta0 = 1 - 2.5 * c_l
    rhs = beta0 * E + 0.5 * c_l * R * Ep + flux + nu * D - nu * bvisc
    err = abs(lhs - rhs) / max(abs(lhs), abs(rhs))
    print(f"I3 ball identity on B(0, {R}): lhs {lhs:.10e} rhs {rhs:.10e} rel diff {err:.1e} (nu D = {nu * D:.3e}, beta0 E = {beta0 * E:.3e})")
    return err < 1e-9


def test_I4(device):
    torch.manual_seed(2)
    model = Model(L=4, Nk=8, m_parity="even", R0=0.5, Nr=24, c_l=0.45, omega=0.7, channels=dict(NkB=2, NkD=2, NkE=2), device=device)
    z = torch.randn(model.n_z, device=device) * 0.3
    p0 = Problem(model, formulation="mom", nl_weighting=True, nl_denominator="all5"); p1 = Problem(model, formulation="mom", nl_weighting=True, nl_denominator="all5", nu=0.0)
    p0.update_nl_weights(z); p1.update_nl_weights(z)
    r0 = p0.residual_vector(z); r1 = p1.residual_vector(z)
    e = float((r0 - r1).abs().max() / r0.abs().max())
    p2 = Problem(model, formulation="mom", nl_weighting=True, nl_denominator="all5", nu=1e-3); p2.update_nl_weights(z); r2 = p2.residual_vector(z)
    e2 = float((r0 - r2).abs().max() / r0.abs().max())
    print(f"I4: nu = 0 reproduces the Stage I residual vector to {e:.1e}; nu = 1e-3 changes it by {e2:.1e} (must be > 0)")
    return e < 1e-13 and e2 > 1e-8


if __name__ == "__main__":
    dev = "cuda:0" if torch.cuda.is_available() else "cpu"
    res_ = dict(I1=test_I1(dev), I2_sympy=test_I2_sympy(), I2_far=test_I2_farfield(dev), I3=test_I3(dev), I4=test_I4(dev))
    print("S8 implementation tests:", res_)
    print("S8 PASS" if all(res_.values()) else "S8 FAIL")
    sys.exit(0 if all(res_.values()) else 1)
