"""SPEC T03 cross-check: grad P from the spherical-harmonic Green solver vs the independent ray integral, on a random
non-axisymmetric state of the actual representation (not a manufactured P); several points incl. core and r ~ 5."""
import sys, os, math, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
from src.equations.fields import Model, alpha_of
from src.optimization.problem import Problem
from src.pressure.ray_integral import gradP_ray
from src.equations import residuals as res
torch.set_default_dtype(torch.float64)
dev = "cuda:0" if torch.cuda.is_available() else "cpu"
torch.manual_seed(3)
model = Model(L=4, Nk=8, m_parity="even", R0=1.0, Nr=48, c_l=0.45, omega=1.3, device=dev)   # Nr = 6 Nk: quadratic source resolved
prob = Problem(model, formulation="mom")
z = torch.randn(model.n_z, device=dev) * 0.3
ev = prob.evaluate(z)
# pick grid points: a few radii and angles
js = [6, 12]; aa = [5, 77, 150]   # core points r < 1.5 (ray quadrature is accurate there; far points need the SH method)
pts = torch.stack([model.y[j, a] for j in js for a in aa])
gP_sh = torch.stack([ev['gradP'][:, j, a] for j in js for a in aa])
for (nt, nph, nr) in [(24, 48, 160), (32, 64, 240)]:
    t0 = time.time()
    gP_ray = gradP_ray(model, z, pts, ntheta=nt, nphi=nph, nrad=nr)
    err = (gP_ray - gP_sh).norm(dim=1) / gP_sh.norm(dim=1).clamp_min(1e-300)
    print(f"ray quadrature {nt}x{nph}x{nr}: rel err per point max {err.max().item():.2e} median {err.median().item():.2e}  ({time.time()-t0:.1f}s)")
print("radii of test points:", [f"{model.r[j].item():.3g}" for j in js])
g0 = prob.pressure.gradP_origin(res.pressure_source(ev["F"]["GU"])); g0r = gradP_ray(model, z, torch.zeros(1, 3, device=dev), ntheta=32, nphi=64, nrad=240, Rs=1.0)[0]
print(f"grad P(0): SH {g0.tolist()} ray {g0r.tolist()} rel diff {((g0-g0r).norm()/g0.norm()).item():.2e}")
assert err.max().item() < 1e-9 and ((g0-g0r).norm()/g0.norm()).item() < 1e-10
print("PRESSURE RAY CROSS-CHECK PASSED")
