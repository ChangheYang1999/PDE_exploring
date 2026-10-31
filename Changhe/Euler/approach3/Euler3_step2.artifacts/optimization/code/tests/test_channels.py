"""Extra radial channels (SPEC 4.4): regularity at the origin, far-field rates, linear-operator action
(L[r^-(2alpha+1) G] = -r^-(2alpha+1) G asymptotically), untwisted harmonic channel, and LM manufactured recovery."""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
from src.equations.fields import Model, alpha_of
from src.equations import residuals as res
from src.optimization.problem import Problem
from src.optimization.lm import lm_solve
torch.set_default_dtype(torch.float64)

def run():
    torch.manual_seed(21)
    c_l, om = 0.46, 1.4; alpha = alpha_of(c_l)
    ch = dict(NkB=3, NkD=3, NkE=3, core_damp=2)
    model = Model(L=4, Nk=4, m_parity="even", R0=1.0, Nr=8, c_l=c_l, omega=om, channels=ch)
    print("layout", model.layout, "n_z", model.n_z)
    d = model.unpack_all(torch.zeros(model.n_z))
    # (1) B channel alone: field decays like r^-(2alpha+1) and L U = -U asymptotically
    for name, rate, lin in [("B", 2 * alpha + 1, -1.0), ("D", 2 * alpha + 1, -1.0)]:
        extra = {name: torch.zeros(3, model.Nq)}; extra[name][0] = torch.randn(model.Nq)
        z = model.pack(torch.zeros(4, model.Nq), torch.zeros(4, model.Nq), extra=extra)
        from src.bases.solid_harmonics import AngularGrid
        g = AngularGrid(24, 48); n = g.n; wq = g.w / (4 * math.pi)
        vals = []
        for r in [1e2, 1e3, 1e4]:
            F = model.fields_points(z, r * n, need_vort=False)
            U, GU, yv = F['U'], F['GU'], (r * n).T
            W = c_l * yv - om * res.Jvec(yv)
            LU = (1 - c_l) * U + torch.einsum('m...,mi...->i...', W, GU) + om * res.Jvec(U)
            vals.append((((U ** 2).sum(0) * wq).sum().sqrt().item(), ((LU - lin * U).norm(dim=0) / U.norm(dim=0)).max().item()))
        slope = math.log(vals[0][0] / vals[2][0]) / math.log(1e2)
        print(f"channel {name}: decay exponent {slope:.4f} (expected {rate:.4f}); |L U + U|/|U| at r=1e2,1e3,1e4: " + " ".join(f"{v[1]:.1e}" for v in vals))
        assert abs(slope - rate) < 1e-3 and vals[-1][1] < 1e-5
        # regularity at origin: finite values at 0 and on axis
        F0 = model.fields_points(z, torch.tensor([[0.0, 0.0, 0.0], [0.0, 0.0, 0.3], [1e-3, 0, 0]]), need_vort=True)
        assert torch.isfinite(F0['GOm']).all() and F0['U'][:, 0].abs().max().item() < 1e-6   # damped core: U(0) ~ 0 for these channels
    # (2) E channel: curl curl(h y) = -l grad h for h = r^-(l+1) Y_l^m -> U is a harmonic gradient: curl U = 0 and div = 0 at large r
    extra = {"E": torch.zeros(3, model.Nq)}; extra["E"][0] = torch.randn(model.Nq)
    z = model.pack(torch.zeros(4, model.Nq), torch.zeros(4, model.Nq), extra=extra)
    n = torch.randn(30, 3); n = n / n.norm(dim=1, keepdim=True)
    for r in [1e2, 1e3]:
        F = model.fields_points(z, r * n, need_vort=True)
        print(f"channel E at r={r:.0e}: |Omega|/|DU| = {(F['Om'].norm(dim=0) / F['GU'].reshape(9, -1).norm(dim=0)).max().item():.1e} (expected -> 0, harmonic gradient); |U| ~ r^-4 check: {F['U'].norm(dim=0).mean().item():.3e}")
    assert (F['Om'].norm(dim=0) / F['GU'].reshape(9, -1).norm(dim=0)).max().item() < 1e-5
    # (3) LM manufactured recovery with all channels active
    prob = Problem(model, formulation="mom")
    zs = torch.randn(model.n_z) * 0.3
    prob.pivot = prob.choose_pivot(zs)
    Rs = prob.residual_vector(zs)
    fun = lambda z: prob.residual_vector(z) - Rs
    z0 = zs + 0.05 * torch.randn_like(zs)
    out = lm_solve(fun, z0, max_iter=150, lam0=1e-3, verbose=False, chunk=64, scale_rows=prob.n_pde_residuals())   # mechanics test: no phase projection (shifted target not rotation invariant); PDE-row Marquardt scaling
    print(f"LM recovery with channels: final cost {out['cost']:.2e}, |z - z*| {(out['z'] - zs).norm().item():.2e}, status {out['status']}")
    assert out['cost'] < 1e-16
    # (4) backward compatibility: model without channels gives identical fields for the same A, C
    m0 = Model(L=4, Nk=4, m_parity="even", R0=1.0, Nr=8, c_l=c_l, omega=om)
    zA = torch.randn(m0.n_z)
    aT, aS, _, _ = m0.unpack(zA)
    zB = model.pack(aT, aS)
    dU = (m0.fields_grid(zA)['U'] - model.fields_grid(zB)['U']).abs().max().item()
    print(f"backward compatibility (extra channels zero): {dU:.1e}")
    assert dU < 1e-14
    print("CHANNEL TESTS PASSED")

if __name__ == "__main__":
    run()
