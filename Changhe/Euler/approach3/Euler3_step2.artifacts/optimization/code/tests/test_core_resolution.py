"""SPEC v1.21 core-resolution code (src/validation/core_resolution.py): (i) gradP_points (Chebyshev-interpolated Green solution synthesized at
arbitrary points) agrees with PressureSolver.solve on the points of a product grid; (ii) the ball RMS of a smooth field converges under node
doubling (random L4 state with channels); (iii) core_resolution runs end to end and reports a_eff, the two balls and the inner shells."""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model
from src.optimization.problem import Problem
from src.equations import residuals as res
from src.pressure.poisson_sh import PressureSolver
from src.validation.core_resolution import gradP_points, core_resolution, core_text, ball_points

def run(device=None):
    device = device or ("cuda:0" if torch.cuda.is_available() else "cpu")
    torch.manual_seed(7)
    model = Model(L=4, Nk=8, m_parity="even", R0=0.5, Nr=24, c_l=0.45, omega=0.7, channels=dict(NkB=2, NkD=2, NkE=2), device=device)
    z = torch.randn(model.n_z, device=device) * 0.3
    prob = Problem(model, formulation="mom")
    # (i) product-grid reference: eval model with 5 radii and the default angular grid
    radii = np.array([0.03, 0.07, 0.12, 0.2, 0.31])
    em = Model(L=4, Nk=8, m_parity="even", R0=0.5, r_nodes=radii, ntheta=10, nphi=16, c_l=0.45, omega=0.7, channels=dict(NkB=2, NkD=2, NkE=2), device=device, phi0=0.1)
    ps = PressureSolver(model, p0=2 * (0.55 / 0.45) + 2, omega=0.7, c_l=0.45, eval_model=em)
    f = res.pressure_source(model.fields_grid(z, need_vort=False)['GU'])
    P_ref, gP_ref, _, _ = ps.solve(f)                                     # (Nr, Na), (3, Nr, Na)
    pts = em.y.reshape(-1, 3)
    P_pt, gP_pt, info = gradP_points(prob, z, 0.45, 0.7, pts)
    e_P = float((P_pt - P_ref.reshape(-1)).abs().max() / P_ref.abs().max()); e_g = float((gP_pt - gP_ref.reshape(3, -1)).abs().max() / gP_ref.abs().max())
    # (ii) and (iii): end to end on the state's own maxima
    from src.validation.critical_points import local_maxima_omega
    mx = local_maxima_omega(model, z, 0.45, 0.7, n_starts=60, iters=25)
    F = model.fields_grid(z, need_vort=True)
    maxU = float(F['U'].norm(dim=0).max()); maxOm = max(float(F['Om'].norm(dim=0).max()), mx[0]['abs_Omega'] if mx else 0.0)
    ystar = mx[0]['y'] if mx else [0.1, 0.0, 0.05]
    cr = core_resolution(prob, z, 0.45, 0.7, ystar, maxU, maxOm, core_ball_radius=2.0 ** math.floor(math.log2(0.5 / 32)))
    print(core_text(cr))
    print(f"gradP_points vs product-grid solve: P {e_P:.2e} gradP {e_g:.2e} (interp cond {info['interp_cond']:.1e}); max doubling change {cr['max_doubling_rel_change']:.2e}")
    ok = e_P < 1e-9 and e_g < 1e-9 and cr["max_doubling_rel_change"] < 0.1 and cr["a_eff"] > 0
    print("core_resolution PASS" if ok else "core_resolution FAIL")
    return ok

if __name__ == "__main__":
    sys.exit(0 if run() else 1)
