"""SPEC v1.24 7.8 far-helicity coefficients (lead 2026-10-25T09:58Z item 1; d78, FINAL_REPORT section 2 item 34; verifier 09:56Z independent values).
H1: K_H(required) = (1 - 3 alpha) Psi_F equals the identity form 2 int G_req.H - (1 - 3 alpha) int n.(F x G_req) to 1e-10 (identity (I) of d78 on the
    exact homogeneous tail fields), while the negative control (Q + |F|^2/2) differs at order one.
H2: the two forms of K_H(carried) (sphere form and direct exact curl of the carried homogeneous field) agree to 1e-10; the carried field rebuilt from
    the combined potentials reproduces G_carried to 1e-12.
H3: K_H required / carried / ratio and the energy ratio reproduce the independent route's values (verifier 2026-10-25T09:56Z, 272 Decimal80 checks)
    to 1e-9 relative on nest6 (0.45, 1) p0, d6w3_L6 and S9b (carried 0 by construction: no B/D channels).
H4: the second exterior helicity term enters H_tot as K_H R^(1 - 3 alpha)/(3 alpha - 1) (checked against a direct evaluation at R_end) and is below
    1e-12 at R_end = 2^20 R0, so H_tot and the S9 rows are unchanged to that precision."""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model, alpha_of
from src.optimization.problem import Problem
from src.far_field.correction import closure_distance
ROOT = os.path.join(os.path.dirname(__file__), "..")
REF = {  # verifier 2026-10-25T09:56Z: K_H required, K_H carried, helicity ratio, energy ratio
    "runs/nest6_L6_cl0.45_om+1.0_fixed_p0_om+1.0s43s0/starts/start_000.pt": (-0.388799366389, -0.490845706358, 1.2624652939, -32.6281126771),
    "runs/d6w3_L6_cl0.45_om+0.3_fixed/starts/start_000.pt": (-1.04436929693, -1.12169120534, 1.07403694137, -3.25360597442),
    "runs/s9b_L4_cl0.45_om+1.0_fixed_bal10_naxpin_from_bal1/starts/start_000.pt": (0.392702299466, 0.0, 0.0, 0.0),
}

def load(zf, dev):
    S = torch.load(os.path.join(ROOT, zf), map_location="cpu", weights_only=False); cfg = S["config"]; z = S["z"].to(dev)
    model = Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), Nr=cfg.get("Nr"), c_l=cfg["c_l"], omega=cfg["omega"], free_params=False, channels=cfg.get("channels"), device=dev)
    return model, z, S

def run(device=None):
    device = device or ("cuda:0" if torch.cuda.is_available() else "cpu")
    ok = True
    for zf, (kreq, kcar, krat, erat) in REF.items():
        model, z, S = load(zf, device)
        g = closure_distance(Problem(model, formulation="mom"), z)
        name = os.path.basename(os.path.dirname(os.path.dirname(zf)))
        h1 = g["K_H_identity_rel_closure"] < 1e-10 and g["K_H_negative_control_rel"] > 0.1
        print(f"H1 {name}: identity closure {g['K_H_identity_rel_closure']:.1e} (< 1e-10), negative control {g['K_H_negative_control_rel']:.2f} (> 0.1): {'PASS' if h1 else 'FAIL'}")
        if g.get("K_H_carried_two_forms_rel") is not None:
            h2 = g["K_H_carried_two_forms_rel"] < 1e-10 and g["G_carried_rebuild_rel"] < 1e-12
            print(f"H2 {name}: carried two forms {g['K_H_carried_two_forms_rel']:.1e} (< 1e-10), rebuild {g['G_carried_rebuild_rel']:.1e} (< 1e-12): {'PASS' if h2 else 'FAIL'}")
        else:
            h2 = g.get("K_H_carried") == 0.0 and model.channels.get("NkB", 0) == 0
            print(f"H2 {name}: no carried channels, K_H carried {g.get('K_H_carried')} (0 by construction): {'PASS' if h2 else 'FAIL'}")
        e_req = abs(g["K_H_required"] - kreq) / abs(kreq)
        e_car = abs(g["K_H_carried"] - kcar) / max(abs(kcar), 1e-3)
        e_rat = abs((g["K_H_ratio_direct"] or 0.0) - krat) / max(abs(krat), 1e-3)
        e_en = abs((g["K_ratio_direct"] or 0.0) - erat) / max(abs(erat), 1e-3)
        h3 = max(e_req, e_car, e_rat, e_en) < 1e-9
        print(f"H3 {name}: K_H required {g['K_H_required']:.12f} (verifier {kreq}; rel {e_req:.1e}), carried {g['K_H_carried']:.12f} ({kcar}; {e_car:.1e}), ratio {g['K_H_ratio_direct']} ({krat}; {e_rat:.1e}), energy ratio {g['K_ratio_direct']} ({erat}; {e_en:.1e}): {'PASS' if h3 else 'FAIL'}")
        ok = ok and h1 and h2 and h3
        if name.startswith("nest6"):
            from src.validation.global_balances import GlobalBalances
            gb = GlobalBalances(model)
            with torch.no_grad():
                b0 = gb.integrals(z); b1 = gb.integrals(z, K_H=g["K_H_carried"])
            alpha = alpha_of(float(model.c_l0)); R = float(b1["R_end"])
            direct = g["K_H_carried"] * R ** (1 - 3 * alpha) / (3 * alpha - 1)
            t2 = float(b1["H_tot_exterior_second_term"])
            h4 = abs(t2 - direct) <= 1e-12 * max(abs(direct), 1e-300) + 1e-300 and abs(t2) < 1e-12 and abs(float(b1["H_tot"]) - float(b0["H_tot"])) < 1e-12 and abs(float(b1["H_tot_one_term"]) - float(b0["H_tot"])) == 0.0
            print(f"H4 {name}: second exterior term {t2:.3e} (direct {direct:.3e}) at R_end {R:.3e}; H_tot one term {float(b0['H_tot']):.6f} both terms {float(b1['H_tot']):.6f}: {'PASS' if h4 else 'FAIL'}")
            ok = ok and h4
        del model; torch.cuda.empty_cache()
    print("test_far_helicity:", "PASS" if ok else "FAIL")
    return ok

if __name__ == "__main__":
    sys.exit(0 if run() else 1)
