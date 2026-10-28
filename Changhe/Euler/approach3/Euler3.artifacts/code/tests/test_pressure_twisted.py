"""T03 with twist: manufactured P built as a twisted potential of the actual representation (decay r^-alpha, m != 0 with
phase m beta(r)); f = -Lap P from the exact Hessian trace; solver must recover P and grad P. Also grad P(0)."""
import sys, os, math, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
from src.equations.fields import Model, alpha_of
from src.pressure.poisson_sh import PressureSolver
torch.set_default_dtype(torch.float64)

def run(L=4, Nk=8, Nr=30, c_l=0.45, omega=3.0):
    torch.manual_seed(4)
    # the "pressure modes" include l = 0 and all even m; use a Model with l_min=1 modes for the potential and add nothing for l=0
    model = Model(L=L, Nk=Nk, m_parity="even", R0=1.0, Nr=Nr, c_l=c_l, omega=omega)
    alpha = alpha_of(c_l)
    aT = torch.randn(Nk, model.Nq) * torch.exp(-0.4 * torch.arange(Nk))[:, None]; aS = torch.zeros_like(aT)
    gT, gS = model.radial_derivs(aT, aS, torch.tensor(c_l), torch.tensor(omega), K=4)
    P_ref, gP_ref, H_ref = model.scalar_grid((gT[0], gT[1], gT[2]), True)        # P := twisted potential T (decays like r^-alpha)
    f = -(H_ref[0, 0] + H_ref[1, 1] + H_ref[2, 2])
    for p0 in [alpha + 2]:
        t0 = time.time(); ps = PressureSolver(model, p0=p0); tb = time.time() - t0
        P, gP, Plm, dPlm = ps.solve(f)
        errP = (P - P_ref).abs().max().item() / P_ref.abs().max().item()
        errG = (gP - gP_ref).abs().max().item() / gP_ref.abs().max().item()
        wr = (1 + model.r ** 2) ** (alpha / 2)
        errPw = ((P - P_ref).abs() * wr[:, None]).max().item() / (P_ref.abs() * wr[:, None]).max().item()
        g0 = ps.gradP_origin(f); g0_ref = model.fields_points(model.pack(aT, aS), torch.zeros(1, 3), need_vort=False)
        print(f"omega={omega} c_l={c_l} p0={p0:.3f}: build {tb:.1f}s ({ps.n_quad} quad pts), rel err P {errP:.2e}, grad P {errG:.2e}, r^alpha-weighted P {errPw:.2e}; grad P(0) = {g0.tolist()}")
        assert errP < 1e-9 and errG < 1e-8
    print("TWISTED PRESSURE TEST PASSED")

if __name__ == "__main__":
    run(omega=3.0); run(omega=0.3, c_l=0.49); run(L=6, Nk=10, Nr=36, omega=10.0, c_l=0.41)
