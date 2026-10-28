"""Stage II S9 implementation tests (lead 2026-10-25T05:36Z, stage2_plan_draft S9): J1 the E_ren row reproduces the lead's d64 values on the two
exports to 1e-3 relative (d6w3_L6 -1.0377, nest4 (0.45, 1) -2.1003); J2 the H_tot / int |h| row reproduces d64 to 1e-3 (-0.8337, -0.8291);
J3 the row Jacobians (reverse-mode gradients of E_ren and H_tot/int|h| with respect to the coefficients) agree with central differences to 1e-6."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model
from src.validation.global_balances import GlobalBalances
ROOT = os.path.join(os.path.dirname(__file__), "..")
# d64 lead values (E_ren; H_tot / int|h| with the FINITE-BALL denominator, the lead's d64 omitted the exterior term of int|h|, verifier 2026-10-25T05:54Z) and
# the verifier's independent full-denominator ratio for nest4 (-0.826893; d6w3_L6 not yet published: None)
# full-denominator references: the lead's corrected d64 (2026-10-25T06:01Z): d6w3_L6 -0.8323, nest4 (0.45, 1) -0.8270 (the verifier's independent nest4 value -0.826893 agrees to 5e-4)
REF = {"runs/d6w3_L6_cl0.45_om+0.3_fixed/starts/start_000.pt": (-1.0377, -0.8337, -0.8323), "runs/nest4_L4_cl0.45_om+1.0_fixed_p0_om+1.0s31/starts/start_000.pt": (-2.1003, -0.8291, -0.8270)}

def load(zf, dev):
    S = torch.load(os.path.join(ROOT, zf), map_location="cpu", weights_only=False); cfg = S["config"]; z = S["z"].to(dev)
    model = Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), Nr=cfg.get("Nr"), c_l=cfg["c_l"], omega=cfg["omega"], free_params=False, channels=cfg.get("channels"), device=dev)
    return model, z, S

def run(device=None):
    device = device or ("cuda:0" if torch.cuda.is_available() else "cpu")
    ok = True
    for zf, (Eref, Href_finite, Href_full) in REF.items():
        model, z, S = load(zf, device)
        gb = GlobalBalances(model)
        rc = ((S.get("spec_diag_holdout") or {}).get("guards") or {}).get("N4_r_core")
        with torch.no_grad():
            b = gb.integrals(z, r_core=rc)
        e1 = abs(float(b["E_ren"]) - Eref) / abs(Eref); e2 = abs(float(b["H_tot_over_abs_finite_denominator"]) - Href_finite) / abs(Href_finite)
        e3 = (abs(float(b["H_tot_over_abs"]) - Href_full) / abs(Href_full)) if Href_full is not None else None
        print(f"J1/J2 {os.path.basename(os.path.dirname(os.path.dirname(zf)))}: E_ren {float(b['E_ren']):.5f} vs d64 {Eref} (rel {e1:.1e}); H_tot/int|h| finite-ball denominator {float(b['H_tot_over_abs_finite_denominator']):.5f} vs d64 {Href_finite} (rel {e2:.1e}); "
              f"full denominator (exterior term included) {float(b['H_tot_over_abs']):.6f}" + (f" vs corrected d64 {Href_full} (rel {e3:.1e})" if e3 is not None else ""))
        ok = ok and e1 < 1e-3 and e2 < 1e-3 and (e3 is None or e3 < 1e-3)
        # J4 two forms of E_ren at an intermediate radius where E_F(R) - 1 is not negligible (verifier 05:54Z: manufactured nonzero endpoint difference)
        with torch.no_grad():
            F = gb.em.fields_grid(z, need_vort=False); Ae = ((F['U'] ** 2).sum(0) * gb.w_ang[None, :]).sum(1); r = gb.r; alpha = b["alpha"]; p = b["p"]
            Ec = gb.W @ (Ae * r ** 3) + Ae[0] * r[0] ** 3 / 3.0; EF = r ** (2 * alpha) * Ae
            k = int(torch.argmin((r - 4.0 * float(rc or model.R0)).abs()).item())            # R = 4 r_core: E_F(R) - 1 is order one there
            row = Ec[k] - EF[k] * r[k] ** p / p
            gq = r ** (p - 1) * (EF - 1.0); radial = (gb.W[k] * (r * gq)).sum() - r[0] ** p / p - (EF[k] - 1.0) * r[k] ** p / p
            e4 = float((row - radial).abs() / row.abs())
        print(f"J4 two forms of E_ren at R = {float(r[k]):.3g} (E_F(R) = {float(EF[k]):.4f}): finite-radius row {float(row):.6f}, radial integral minus (E_F(R) - 1) R^p/p {float(radial):.6f}, rel diff {e4:.1e}")
        ok = ok and e4 < 1e-6
    # J3 on the (cheaper) nest4 state: gradients of the two rows vs central differences in 6 random directions
    model, z, S = load(list(REF)[1], device); gb = GlobalBalances(model)
    def rows(zz):
        b = gb.integrals(zz); return torch.stack([b["E_ren"], b["H_tot_over_abs"]])
    zz = z.clone().requires_grad_(True); r0 = rows(zz)
    g = torch.stack([torch.autograd.grad(r0[i], zz, retain_graph=True)[0] for i in range(2)], 0)       # (2, n)
    torch.manual_seed(0); worst = 0.0
    for _ in range(6):
        v = torch.randn_like(z); v /= v.norm(); h = 1e-5
        with torch.no_grad():
            fd = (rows(z + h * v) - rows(z - h * v)) / (2 * h)
        worst = max(worst, float((g @ v - fd).abs().max() / (g @ v).abs().max()))
    print(f"J3 row Jacobians (reverse mode) vs central differences, 6 directions: worst relative {worst:.1e}")
    ok = ok and worst < 1e-6
    print("S9 tests PASS" if ok else "S9 tests FAIL")
    return ok

if __name__ == "__main__":
    sys.exit(0 if run() else 1)
