import sys, os, time, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
from validation.gates import Case, ROOT
from src.far_field import correction as C
from src.equations.fields import alpha_of
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
case = Case("S01", dev, start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")); prob, model = case.prob, case.model
c_l, omega = case.pair; alpha = alpha_of(c_l); kappa = omega / c_l; R0 = model.R0; n = prob.closure["grid"].n; y = R0 * n
mB, mD, allm, Lmax = C.carried_mode_sets(model, None, None)
E = torch.zeros(len(allm), len(mB), dtype=torch.float64, device=dev)
for j, q in enumerate(mB):
    E[allm.index(q), j] = 1.0
(torch.cuda.synchronize() if torch.cuda.is_available() else None); t0 = time.time(); VB1, _ = C.homogeneous_velocity_exact(y, E, None, 2 * alpha + 1, 2 * alpha, allm, Lmax, kappa, R0, need_grad=False); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t1 = time.time() - t0
t0 = time.time(); VB2 = C.homogeneous_patterns_exact(y, E, None, 2 * alpha + 1, 2 * alpha, allm, Lmax, kappa, R0); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t2 = time.time() - t0
print(f"B patterns: per-column exact {t1:.2f}s, batched {t2:.3f}s, rel diff {float((VB1 - VB2).norm() / VB1.norm()):.2e}")
E = torch.zeros(len(allm), len(mD), dtype=torch.float64, device=dev)
for j, q in enumerate(mD):
    E[allm.index(q), j] = 1.0
t0 = time.time(); VD1, _ = C.homogeneous_velocity_exact(y, None, E, 2 * alpha + 1, 2 * alpha, allm, Lmax, kappa, R0, need_grad=False); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t1 = time.time() - t0
t0 = time.time(); VD2 = C.homogeneous_patterns_exact(y, None, E, 2 * alpha + 1, 2 * alpha, allm, Lmax, kappa, R0); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t2 = time.time() - t0
print(f"D patterns: per-column exact {t1:.2f}s, batched {t2:.3f}s, rel diff {float((VD1 - VD2).norm() / VD1.norm()):.2e}")
# off-sphere check with twist (r = 2 R0) on a few columns
y2 = 2 * R0 * n; E3 = E[:, :5]
V1, _ = C.homogeneous_velocity_exact(y2, None, E3, 2 * alpha + 1, 2 * alpha, allm, Lmax, kappa, R0, need_grad=False); V2 = C.homogeneous_patterns_exact(y2, None, E3, 2 * alpha + 1, 2 * alpha, allm, Lmax, kappa, R0)
print(f"off-sphere (twist) rel diff {float((V1 - V2).norm() / V1.norm()):.2e}")
