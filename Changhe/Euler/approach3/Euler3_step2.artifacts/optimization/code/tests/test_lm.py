"""(a) AD Jacobian (forward-mode under vmap) vs central differences at several step sizes.
(b) Manufactured recovery: fun(z) = R(z) - R(z*) vanishes at z*; LM from a perturbed start must recover a zero."""
import sys, os, math, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
from src.equations.fields import Model
from src.optimization.problem import Problem
from src.optimization.lm import jacobian_fwd, jacobian_fd, lm_solve
torch.set_default_dtype(torch.float64)

def test_jacobian(formulation):
    torch.manual_seed(5)
    model = Model(L=2, Nk=4, m_parity="even", R0=1.0, Nr=8, c_l=0.45, omega=0.8, free_params=True)
    prob = Problem(model, formulation=formulation)   # production gauge weight; Marquardt scaling from the PDE rows only
    z = torch.randn(model.n_z) * 0.3; z[-2] = 0.45; z[-1] = 0.8
    prob.pivot = prob.choose_pivot(z)
    fun = prob.residual_vector
    t0 = time.time(); J = jacobian_fwd(fun, z, chunk=64); tj = time.time() - t0
    for h in [1e-4, 1e-5, 1e-6, 1e-7]:
        Jfd = jacobian_fd(fun, z, h=h)
        err = (J - Jfd).abs().max().item() / J.abs().max().item()
        print(f"  [{formulation}] AD vs FD(h={h:.0e}) Jacobian rel err {err:.2e}  (J max {J.abs().max().item():.2e}, {J.shape}, AD {tj:.2f}s)")
    # directional check with Richardson on the parameter directions (c_l, omega)
    for k, name in [(model.n_z - 2, "c_l"), (model.n_z - 1, "omega")]:
        e = torch.zeros_like(z); e[k] = 1.0
        h = 1e-4
        d = (8 * (fun(z + h * e) - fun(z - h * e)) - (fun(z + 2 * h * e) - fun(z - 2 * h * e))) / (12 * h)
        err = (J[:, k] - d).abs().max().item() / (1 + J[:, k].abs().max().item())
        print(f"  [{formulation}] d/d{name}: AD vs 4th-order FD rel err {err:.2e}")
        assert err < 1e-7
    Jfd = jacobian_fd(fun, z, h=1e-6)
    assert (J - Jfd).abs().max().item() / J.abs().max().item() < 1e-7

def test_recovery(formulation):
    torch.manual_seed(6)
    model = Model(L=2, Nk=4, m_parity="even", R0=1.0, Nr=8, c_l=0.45, omega=0.8, free_params=False)
    prob = Problem(model, formulation=formulation)   # production gauge weight; Marquardt scaling from the PDE rows only
    zs = torch.randn(model.n_z) * 0.3
    prob.pivot = prob.choose_pivot(zs)
    Rs = prob.residual_vector(zs)
    fun = lambda z: prob.residual_vector(z) - Rs
    z0 = zs + 0.05 * torch.randn_like(zs)
    r0 = fun(z0)
    out = lm_solve(fun, z0, max_iter=60, lam0=1e-3, verbose=False, scale_rows=prob.n_pde_residuals())   # mechanics test: no phase projection (shifted target not rotation invariant); PDE-row Marquardt scaling
    print(f"  [{formulation}] recovery: start cost {0.5*(r0@r0).item():.3e} -> final {out['cost']:.3e} in {len(out['history'])} its, status {out['status']}, |z-z*| {(out['z']-zs).norm().item():.2e}")
    assert out['cost'] < 1e-20

def test_jtj_split(formulation):
    """(c) Split-column J^T J accumulation (jtj_split, 2026-10-25T16:10Z) against the dense J^T J and J^T r: blocks 1, 2, 3, 5 with a
    chunk that does not align with the block edges; then the first LM step of lm_solve(jtj_blocks=2) against the dense LM step from the
    same start (the lead's validation criterion: first-step relative difference <= 1e-6, cost decrease within 1 per cent), and a recovery run."""
    from src.optimization.lm import jtj_split
    torch.manual_seed(7)
    model = Model(L=2, Nk=4, m_parity="even", R0=1.0, Nr=8, c_l=0.45, omega=0.8, free_params=False)
    prob = Problem(model, formulation=formulation)
    z = torch.randn(model.n_z) * 0.3
    prob.pivot = prob.choose_pivot(z)
    fun = prob.residual_vector
    r = fun(z)
    J = jacobian_fwd(fun, z, chunk=64); A0 = J.T @ J; g0 = J.T @ r
    for nb in [1, 2, 3, 5]:
        A, g = jtj_split(fun, z, r, chunk=7, n_blocks=nb)
        ea = (A - A0).abs().max().item() / A0.abs().max().item(); eg = (g - g0).abs().max().item() / g0.abs().max().item()
        print(f"  [{formulation}] jtj_split blocks {nb}: rel err A {ea:.2e}, g {eg:.2e}  (N {z.numel()}, Nres {r.numel()})")
        assert ea < 1e-13 and eg < 1e-13
    # scalar rows path
    sc = [lambda zz: (zz * zz).sum() - 1.0, lambda zz: zz.sum()]
    Jsc = torch.stack([torch.autograd.grad(f(z.clone().requires_grad_(True)), [z.clone().requires_grad_(True)])[0] if False else torch.func.grad(f)(z) for f in sc], 0)
    rfull = torch.cat([r, torch.stack([f(z) for f in sc])])
    Jfull = torch.cat([J, Jsc], 0); A1 = Jfull.T @ Jfull; g1 = Jfull.T @ rfull
    A, g = jtj_split(fun, z, r, chunk=7, n_blocks=3, scalar_rows=sc, r_scalar=rfull[r.numel():])
    ea = (A - A1).abs().max().item() / A1.abs().max().item(); eg = (g - g1).abs().max().item() / g1.abs().max().item()
    print(f"  [{formulation}] jtj_split with 2 scalar rows: rel err A {ea:.2e}, g {eg:.2e}")
    assert ea < 1e-13 and eg < 1e-13
    # first LM step: dense vs split from the same start (manufactured zero problem, PDE-row scaling off: full-diagonal scaling as in the worker)
    zs = torch.randn(model.n_z) * 0.3
    prob.pivot = prob.choose_pivot(zs)
    Rs = prob.residual_vector(zs)
    f2 = lambda zz: prob.residual_vector(zz) - Rs
    z0 = zs + 0.05 * torch.randn_like(zs)
    c0 = 0.5 * float(f2(z0) @ f2(z0))
    od = lm_solve(f2, z0, max_iter=1, lam0=1e-3, verbose=False, chunk=64)
    osp = lm_solve(f2, z0, max_iter=1, lam0=1e-3, verbose=False, chunk=7, jtj_blocks=2)
    dzd = od["z"] - z0; dzs = osp["z"] - z0
    rel = (dzd - dzs).norm().item() / dzd.norm().item()
    dec_d = (c0 - od["cost"]) / c0; dec_s = (c0 - osp["cost"]) / c0
    print(f"  [{formulation}] first LM step dense vs split(2): relative step difference {rel:.2e}; cost decrease {dec_d:.6f} vs {dec_s:.6f} (relative difference {abs(dec_d - dec_s) / dec_d:.2e})")
    assert rel < 1e-6 and abs(dec_d - dec_s) / dec_d < 1e-2
    out = lm_solve(f2, z0, max_iter=60, lam0=1e-3, verbose=False, chunk=7, jtj_blocks=3, scale_rows=prob.n_pde_residuals())
    outd = lm_solve(f2, z0, max_iter=60, lam0=1e-3, verbose=False, chunk=64, scale_rows=prob.n_pde_residuals())
    print(f"  [{formulation}] recovery with jtj_blocks 3 (PDE-row scaling): final cost {out['cost']:.3e} in {len(out['history'])} its, status {out['status']}, |z-z*| {(out['z']-zs).norm().item():.2e}; dense {outd['cost']:.3e} in {len(outd['history'])} its")
    assert out['cost'] < 1e-20 and outd['cost'] < 1e-20

if __name__ == "__main__":
    for f in ["vort", "mom"]:
        test_jacobian(f); test_recovery(f); test_jtj_split(f)
    print("ALL LM TESTS PASSED")
