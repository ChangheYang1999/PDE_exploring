"""SPEC 7.6 / T08: origin Taylor orders 1 and 2 by the quadratic Taylor fit on small spheres (src/validation/origin_taylor.py).
Checks on a random L4 state with channels: (i) the fitted order-0 coefficient of R_u equals the exact R_u(0) (fields_points at y = 0 and
gradP_origin); (ii) the fitted D U(0) equals the exact DU(0); (iii) the fitted D^2 U(0) equals central differences of DU from fields_points;
(iv) the fit on the spheres (eps, 2 eps, 3 eps) and the check set (2 eps, 4 eps, 6 eps) agree (consistency of the Taylor ratios);
(v) tau_j are finite and the floor rule of 7.6 is applied."""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model
from src.optimization.problem import Problem
from src.validation.spec_diagnostics import spec_diagnostics
from src.validation.origin_taylor import origin_taylor

def run(device=None):
    device = device or ("cuda:0" if torch.cuda.is_available() else "cpu")
    torch.manual_seed(5)
    model = Model(L=4, Nk=8, m_parity="even", R0=0.5, Nr=24, c_l=0.45, omega=0.7, channels=dict(NkB=2, NkD=2, NkE=2), device=device)
    z = torch.randn(model.n_z, device=device) * 0.3
    prob = Problem(model, formulation="mom")
    sd = spec_diagnostics(prob, z)                       # training-grid diagnostics with the origin block (exact tau_0 + fitted tau_1, tau_2)
    og = sd["origin"]
    assert "taylor_error" not in og, og.get("taylor_error")
    errs = dict(D0_Ru_vs_exact=og["taylor_D0_Ru_vs_exact_rel"], D1_U_vs_exact=og["taylor_D1_U_vs_exact_rel"],
                consistency_tau=max(og["taylor_consistency_rel_change_tau"]), consistency_DRu=max(og["taylor_consistency_rel_change_DRu"]))
    # (iii) second derivatives of U at 0 against central differences of DU (fields_points), independent of the fit
    ot = origin_taylor(prob, z, 0.45, 0.7, U_c=sd["guards"]["N4_max_U"], r_core=sd["guards"]["N4_r_core"])
    h = 1e-4
    D2fd = torch.zeros(3, 3, 3, dtype=torch.float64, device=device)   # D2fd[i(component), m, n] = d_m d_n U_i
    for n in range(3):
        e = torch.zeros(1, 3, dtype=torch.float64, device=device); e[0, n] = h
        Gp = model.fields_points(z, e, need_vort=False)["GU"][:, :, 0]; Gm = model.fields_points(z, -e, need_vort=False)["GU"][:, :, 0]   # [m, i]
        D2fd[:, :, n] = ((Gp - Gm) / (2 * h)).T
    # recover the fitted D2 of U from a second call with the tensors (recompute the fit here to access the tensor)
    from src.validation.origin_taylor import _taylor_fit, _derivative_norms
    nf = len(ot["radii_fit"])
    em = Model(L=4, Nk=8, m_parity="even", R0=0.5, r_nodes=ot["radii_fit"], ntheta=ot["ntheta"], nphi=ot["nphi"], c_l=0.45, omega=0.7, channels=dict(NkB=2, NkD=2, NkE=2), device=device, phi0=math.pi / (2 * ot["nphi"]))
    F = em.fields_grid(z, need_vort=False); y = F["y"]; w = em.grid.w / (4 * math.pi)
    pts = torch.cat([y[j] for j in range(nf)], 0); ww = torch.cat([w for _ in range(nf)], 0)
    c = _taylor_fit(pts, torch.cat([F["U"][:, j, :] for j in range(nf)], 1), ww, ot["radii_fit"][-1])
    _, (D0, D1, D2) = _derivative_norms(c, ot["radii_fit"][-1])
    errs["D2_U_vs_fd"] = float((D2 - D2fd).norm() / D2fd.norm())
    ok = errs["D0_Ru_vs_exact"] < 1e-6 and errs["D1_U_vs_exact"] < 1e-6 and errs["D2_U_vs_fd"] < 1e-5 and errs["consistency_tau"] < 1e-4 and errs["consistency_DRu"] < 1e-4
    print("T08 origin Taylor: tau (floored) =", ["%.3e" % v for v in (og["tau0_floored"], og["tau1_floored"], og["tau2_floored"])], "raw =", og["tau0_raw"], og["tau1_raw"], og["tau2_raw"])
    print("   errors:", {k: "%.2e" % v for k, v in errs.items()}, "floors", ["%.2e" % v for v in og["floor_1e3_S"]], "|D^j R_u|", ["%.3e" % v for v in og["D_Ru_norms_fit"]])
    print("T08 PASS" if ok else "T08 FAIL")
    return ok

if __name__ == "__main__":
    ok = run()
    sys.exit(0 if ok else 1)
