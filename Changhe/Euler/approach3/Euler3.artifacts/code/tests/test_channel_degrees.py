"""Channel-specific angular degrees (SPEC 4.4 angular closure; lead 2026-10-24T22:40Z (a)): LB = 2L+3, LD = 2L+2, LE = L, even m <= 2 M_max.
Checks: (1) default channels unchanged (same n_z, identical fields); (2) extended model: pack/unpack round trip, A/C columns restricted to
l <= L, B columns reach l = 2L+3, D l = 2L+2, m <= 2 M_max; (3) exact embedding of a plain state gives identical fields; (4) tail-constraint
reduce/expand round trip and constraint satisfaction; (5) LM manufactured recovery with the extended channels (Jacobian mechanics)."""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
from src.equations.fields import Model
from src.optimization.problem import Problem
from src.optimization.lm import lm_solve
from src.optimization.tail_constraints import TailConstraints
from src.optimization.transfer import embed_state
torch.set_default_dtype(torch.float64)

def run():
    torch.manual_seed(5)
    c_l, om, L, Nk = 0.45, 0.3, 3, 5
    plain = Model(L=L, Nk=Nk, R0=0.7, Nr=10, c_l=c_l, omega=om, channels=dict(NkB=2, NkD=2, NkE=2))
    plain0 = Model(L=L, Nk=Nk, R0=0.7, Nr=10, c_l=c_l, omega=om, channels=dict(NkB=2, NkD=2, NkE=2, LB=None, LD=None))
    assert plain.n_z == plain0.n_z and not plain.extended_channels and plain.L_ext == L
    z = torch.randn(plain.n_z)
    F1 = plain.fields_grid(z); F2 = plain0.fields_grid(z)
    assert (F1['U'] - F2['U']).abs().max().item() == 0.0
    print(f"(1) default channels unchanged: n_z {plain.n_z}, Nq {plain.Nq}, L_ext {plain.L_ext}")
    ext = Model(L=L, Nk=Nk, R0=0.7, Nr=10, c_l=c_l, omega=om, channels=dict(NkB=2, NkD=2, NkE=2, LB=2 * L + 3, LD=2 * L + 2))
    lA = [ext.modes[i][0] for i in ext.chan_cols["A"].tolist()]; lB = [ext.modes[i][0] for i in ext.chan_cols["B"].tolist()]
    lD = [ext.modes[i][0] for i in ext.chan_cols["D"].tolist()]; mB = [ext.modes[i][1] for i in ext.chan_cols["B"].tolist()]
    assert max(lA) == L and max(lB) == 2 * L + 3 and max(lD) == 2 * L + 2 and max(mB) == 2 * plain.Mmax and ext.L_ext == 2 * L + 3
    assert ext.ncols["A"] == plain.Nq and ext.ncols["E"] == plain.Nq
    print(f"(2) extended: Nq {ext.Nq} (leading {plain.Nq}), cols A {ext.ncols['A']} B {ext.ncols['B']} D {ext.ncols['D']} E {ext.ncols['E']}, n_z {ext.n_z}, grid {ext.ntheta}x{ext.nphi}, Lf {ext.Lf}")
    ze = torch.randn(ext.n_z)
    d = ext.unpack_all(ze)
    for nm in ("A", "C", "B", "D", "E"):
        mask = torch.ones(ext.Nq, dtype=torch.bool); mask[ext.chan_cols[nm]] = False
        assert d[nm][:, mask].abs().max().item() == 0.0 if mask.any() else True
    zr = ext.pack(d["A"], d["C"], extra=dict(B=d["B"], D=d["D"], E=d["E"]))
    assert (zr - ze).abs().max().item() == 0.0
    print("    pack/unpack round trip exact; non-carried columns zero")
    # (3) embedding of the plain state into the extended model: identical fields at random points
    zemb = embed_state(z, plain, ext)
    pts = torch.randn(40, 3) * 1.5
    Fa = plain.fields_points(z, pts); Fb = ext.fields_points(zemb, pts)
    err = max((Fa['U'] - Fb['U']).abs().max().item(), (Fa['GOm'] - Fb['GOm']).abs().max().item()) / Fa['U'].abs().max().item()
    print(f"(3) exact embedding plain -> extended: relative field difference {err:.1e}")
    assert err < 1e-13
    # (4) tail constraints on the extended model
    tc = TailConstraints(ext)
    zred = tc.reduce(ze); zfull = tc.expand(zred); zred2 = tc.reduce(zfull)
    assert zred.numel() == tc.n_red and (zred - zred2).abs().max().item() < 1e-12
    dd = ext.unpack_all(zfull); k2 = torch.arange(Nk, dtype=torch.float64) ** 2
    assert (k2 @ dd["A"]).abs().max().item() < 1e-10 and (k2 @ dd["C"]).abs().max().item() < 1e-10
    kB = torch.arange(2, dtype=torch.float64) ** 2
    assert (kB @ dd["B"]).abs().max().item() < 1e-12 and (kB @ dd["D"]).abs().max().item() < 1e-12
    print(f"(4) tail constraints: n_red {tc.n_red} of n_z {ext.n_z}; round trip and k^2 moments exact")
    # (5) LM manufactured recovery (Jacobian mechanics) with the extended channels, momentum formulation
    prob = Problem(ext, formulation="mom")
    zs = torch.randn(ext.n_z) * 0.3; prob.pivot = prob.choose_pivot(zs)
    Rs = prob.residual_vector(zs)
    fun = lambda zz: prob.residual_vector(zz) - Rs
    out = lm_solve(fun, zs + 0.05 * torch.randn_like(zs), max_iter=120, lam0=1e-3, verbose=False, chunk=64, scale_rows=prob.n_pde_residuals())
    print(f"(5) LM recovery with extended channels: final cost {out['cost']:.2e}, |z - z*| {(out['z'] - zs).norm().item():.2e}, status {out['status']}")
    assert out['cost'] < 1e-16
    print("test_channel_degrees PASS")

if __name__ == "__main__":
    run()
