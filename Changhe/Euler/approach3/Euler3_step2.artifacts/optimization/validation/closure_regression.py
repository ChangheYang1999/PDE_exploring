"""D6FP: batched homogeneous_velocity vs the frozen per-column loop (carried_patterns, first_correction) on the S01 state; timings."""
import sys, os, time, importlib.machinery, importlib.util
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model
from src.optimization.problem import Problem
from src.far_field import correction as new
_path = os.path.join(os.path.dirname(__file__), "..", "src", "far_field", "correction.py.frozen_e3")
_loader = importlib.machinery.SourceFileLoader("src.far_field.correction_frozen", _path); _spec = importlib.util.spec_from_loader(_loader.name, _loader)
old = importlib.util.module_from_spec(_spec); sys.modules[_spec.name] = old; _loader.exec_module(old)
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
S = torch.load("starts/S01_nest6_cl0.45_om1.0_p0.pt", map_location="cpu", weights_only=False); cfg = S["config"]
model = Model(L=6, Nk=16, Nr=48, m_parity="even", R0=0.3, c_l=0.45, omega=1.0, free_params=True, channels=cfg["channels"], device=dev, extra_r=cfg["far_radii"])
prob = Problem(model, formulation="mom", nl_weighting=True, nl_denominator="all5far", closure_lambda=1e-3, far_radii=cfg["far_radii"])
z = torch.cat([S["z"].to(dev), torch.tensor([0.45, 1.0], device=dev)])
y = model.R0 * prob.closure["grid"].n
for name, mod in (("frozen", old), ("batched", new)):
    (torch.cuda.synchronize() if torch.cuda.is_available() else None); t0 = time.time(); V, labels = mod.carried_patterns(model, 0.45, 1.0, y); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t1 = time.time() - t0
    t0 = time.time(); fc = mod.first_correction(prob, z); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t2 = time.time() - t0
    print(f"{name}: carried_patterns {t1:.2f}s (V {tuple(V.shape)}), first_correction {t2:.2f}s G_norm {fc['G_norm']:.12f}")
    if name == "frozen":
        V0, G0 = V, fc["G"]
    else:
        print(f"   max |V_new - V_frozen| / max|V| = {float((V - V0).abs().max() / V0.abs().max()):.2e}; max |G_new - G_frozen|/max|G| = {float((fc['G'] - G0).abs().max() / G0.abs().max()):.2e}")
