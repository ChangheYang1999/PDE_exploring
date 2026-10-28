"""S9b (lead 2026-10-25T07:26Z item 6) implementation tests: the guard rows reproduce the SPEC 7.4 values e_core and e_F of two exports to 1e-3
(against the stored training-grid spec_diag of the start files, same r_tail), and their Jacobian rows (reverse-mode gradients) agree with central
differences to 1e-6."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model
from src.optimization.problem import Problem
ROOT = os.path.join(os.path.dirname(__file__), "..")
FILES = ["runs/d6w3_L6_cl0.45_om+0.3_fixed/starts/start_000.pt", "runs/nest4_L4_cl0.45_om+1.0_fixed_p0_om+1.0s31/starts/start_000.pt"]

def run(device=None):
    device = device or ("cuda:0" if torch.cuda.is_available() else "cpu")
    ok = True
    for zf in FILES:
        S = torch.load(os.path.join(ROOT, zf), map_location="cpu", weights_only=False); cfg = S["config"]; z = S["z"].to(device)
        model = Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg["R0"], Nr=cfg["Nr"], c_l=cfg["c_l"], omega=cfg["omega"], channels=cfg.get("channels"), device=device,
                      extra_r=cfg.get("far_radii") if cfg.get("far_merged", True) else None)
        prob = Problem(model, formulation="mom")
        sd = S["spec_diag"]; r_tail = sd["guards"]["N5_r_tail"]
        F = model.fields_grid(z, need_vort=False); aT, aS, c_l, om = model.unpack(z)
        ec = float(prob.e_core_training(F, r_tail=r_tail)); ef = float(prob.e_F_tail(aT, aS, c_l, om))
        e1 = abs(ec - sd["nonaxi"]["e_core"]) / sd["nonaxi"]["e_core"]; e2 = abs(ef - sd["nonaxi"]["e_F"]) / sd["nonaxi"]["e_F"]
        print(f"S9b rows on {zf.split('/')[1]}: e_core {ec:.6e} vs SPEC 7.4 {sd['nonaxi']['e_core']:.6e} (rel {e1:.1e}); e_F {ef:.6e} vs {sd['nonaxi']['e_F']:.6e} (rel {e2:.1e})")
        ok = ok and e1 < 1e-3 and e2 < 1e-3
        # Jacobian rows vs central differences
        prob.nonaxi_r_tail = r_tail
        def rows(zz):
            F_ = model.fields_grid(zz, need_vort=False); a_, s_, c_, o_ = model.unpack(zz)
            return torch.stack([prob.e_core_training(F_), prob.e_F_tail(a_, s_, c_, o_)])
        zz = z.clone().requires_grad_(True); r0 = rows(zz)
        g = torch.stack([torch.autograd.grad(r0[i], zz, retain_graph=True)[0] for i in range(2)], 0)
        torch.manual_seed(1); worst = 0.0
        for _ in range(4):
            v = torch.randn_like(z); v /= v.norm(); h = 1e-5
            with torch.no_grad():
                fd = (rows(z + h * v) - rows(z - h * v)) / (2 * h)
            worst = max(worst, float((g @ v - fd).abs().max() / (g @ v).abs().max()))
        print(f"   Jacobian rows vs central differences (4 directions): worst relative {worst:.1e}")
        ok = ok and worst < 1e-6
    print("S9b tests PASS" if ok else "S9b tests FAIL")
    return ok

if __name__ == "__main__":
    sys.exit(0 if run() else 1)
