"""Lead request 20:39Z item 1(b): manufactured TWISTED source (decay r^-alpha potential, m != 0, phase m beta(r)) with the
Green solution evaluated at OFF-GRID radii: random radii, radii just inside/outside source nodes (near panel edges), radii
beyond the last source node, and the origin neighbourhood; error <= 1e-12 required."""
import sys, os, math, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
from src.equations.fields import Model, alpha_of
from src.pressure.poisson_sh import PressureSolver
torch.set_default_dtype(torch.float64)

def run(L=4, Nk=8, Nr=30, c_l=0.45, omega=3.0):
    torch.manual_seed(4)
    model = Model(L=L, Nk=Nk, m_parity="even", R0=1.0, Nr=Nr, c_l=c_l, omega=omega)
    alpha = alpha_of(c_l)
    aT = torch.randn(Nk, model.Nq) * torch.exp(-0.4 * torch.arange(Nk))[:, None]; aS = torch.zeros_like(aT)
    rs = model.r.numpy()
    rng = np.random.default_rng(1)
    off = np.concatenate([np.exp(rng.uniform(np.log(rs[0] / 3), np.log(rs[-1] * 30), 60)),      # random, incl. beyond the last node
                          rs[5:25] * (1 + 1e-6), rs[5:25] * (1 - 1e-6),                             # just outside / inside nodes
                          0.5 * (rs[:-1] + rs[1:])[::3], [rs[0] / 50, rs[0] / 5]])                  # panel midpoints, near the origin
    off = np.unique(off)
    hold = Model(L=L, Nk=Nk, m_parity="even", R0=1.0, r_nodes=off, ntheta=model.ntheta, nphi=model.nphi, c_l=c_l, omega=omega)
    # manufactured P := twisted potential T on both grids; source f = -Lap T on the training grid
    gT, _ = model.radial_derivs(aT, aS, torch.tensor(c_l), torch.tensor(omega), K=4)
    P_tr, gP_tr, H_tr = model.scalar_grid((gT[0], gT[1], gT[2]), True); f = -(H_tr[0, 0] + H_tr[1, 1] + H_tr[2, 2])
    gTh, _ = hold.radial_derivs(aT, aS, torch.tensor(c_l), torch.tensor(omega), K=4)
    P_ref, gP_ref, _ = hold.scalar_grid((gTh[0], gTh[1], gTh[2]), True)
    ps = PressureSolver(model, p0=alpha + 2, eval_model=hold)
    P, gP, _, _ = ps.solve(f)
    errP = ((P - P_ref).abs().max() / P_ref.abs().max()).item(); errG = ((gP - gP_ref).abs().max() / gP_ref.abs().max()).item()
    # pointwise relative error of the gradient where the gradient is not tiny
    big = gP_ref.norm(dim=0) > 1e-3 * gP_ref.norm(dim=0).max()
    errGp = ((gP - gP_ref).norm(dim=0)[big] / gP_ref.norm(dim=0)[big]).max().item()
    print(f"off-grid radii: {len(off)} (r from {off.min():.3g} to {off.max():.3g}); rel err P {errP:.2e}, grad P {errG:.2e} (normalized), pointwise max {errGp:.2e}; quad pts {ps.n_quad}")
    assert errP < 1e-12 and errG < 1e-12 and errGp < 1e-10
    print("OFF-GRID TWISTED PRESSURE TEST PASSED")

if __name__ == "__main__":
    run()
