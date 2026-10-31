import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model
from src.optimization.problem import Problem
from src.far_field import correction as C
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
S = torch.load("starts/S01_nest6_cl0.45_om1.0_p0.pt", map_location="cpu", weights_only=False); cfg = S["config"]
model = Model(L=6, Nk=16, Nr=48, m_parity="even", R0=0.3, c_l=0.45, omega=1.0, free_params=True, channels=cfg["channels"], device=dev, extra_r=cfg["far_radii"])
prob = Problem(model, formulation="mom", nl_weighting=True, nl_denominator="all5far", closure_lambda=1e-3, far_radii=cfg["far_radii"])
z = torch.cat([S["z"].to(dev), torch.tensor([0.45, 1.0], device=dev)])
def T(f, n=3):
    f(); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t0 = time.time()
    for _ in range(n): f()
    (torch.cuda.synchronize() if torch.cuda.is_available() else None); return (time.time() - t0) / n
grid = prob.closure["grid"]; n = grid.n; y = model.R0 * n
aT, aS, c_l, omega = model.unpack(z); alpha = (1 - 0.45) / 0.45; kappa = 1.0 / 0.45
t, s = prob.tail_amplitudes(aT.detach(), aS.detach(), torch.tensor(0.45, device=dev))
print("first_correction total", T(lambda: C.first_correction(prob, z)))
print("  homogeneous_velocity J=1", T(lambda: C.homogeneous_velocity(y, t[:, None], s[:, None], alpha, alpha - 1.0, model.modes, model.L_ext, kappa, model.R0)))
pmodes = C.mode_list(18, "even", l_min=0)
print("  eval_solid pmodes deg 18", T(lambda: C.eval_solid(n, pmodes, 18, 0)))
print("  eval_Y L_ext", T(lambda: C.eval_Y(C._rotate_z(n, kappa * torch.log(y.norm(dim=-1) / model.R0)), model.modes, model.L_ext)))
print("  tail_amplitudes", T(lambda: prob.tail_amplitudes(aT, aS, c_l)))
print("first_correction_graph", T(lambda: C.first_correction_graph(prob, z)))
print("closure_state_at", T(lambda: prob.closure_state_at(z)))
print("objective_at", T(lambda: prob.objective_at(z)))
zz = z.clone().requires_grad_(True)
def cg():
    r = prob.objective_graph(zz); c = 0.5 * (r @ r); g, = torch.autograd.grad(c, zz); return g
print("objective_graph+backward", T(cg, 2))
print("complete_gradient", T(lambda: prob.complete_gradient(z), 2))
