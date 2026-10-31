"""D6FP far-anchor repair acceptance (lead 2026-10-28T22:39Z item 3 (a), (b)): at S01, S05, S09, S20 and the manufactured (0.42, 0.3) field:
the discrete monopole M_0 and dipole M_1 relative to the absolute sums; old and new P_00, d_r P_00 at the three anchor radii against M_0^disc / r and
M_0^disc / r^2; the change of O1 and of the far-anchor residual rows with the option on. Writes validation/exterior_monopole_regression.json."""
import sys, os, json, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
from validation.gates import Case, PAIRS, ROOT
from src.pressure.poisson_sh import PressureSolver
from src.equations.fields import alpha_of
from src.equations import residuals as res
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z; out = {}
cases = {"S01": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")), "S05": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt")),
         "S09": dict(start=os.path.join(ROOT, "starts", "S09_d6w_cl0.45_om0.3_R1.pt")), "S20_allmode": dict(start=os.path.join(ROOT, "starts", "S20_s4allm_cl0.45_om1.0.pt")), "manu_a": dict(pair=PAIRS["a"], seed=3)}
for cname, cdef in cases.items():
    case = Case(cname, dev, **cdef); prob, model = case.prob, case.model
    c_l, omega = case.pair; zf = case.z_full
    F = model.fields_grid(zf, need_vort=False); f = res.pressure_source(F["GU"])
    ps_old = prob.pressure
    ps_new = PressureSolver(model, p0=2 * alpha_of(c_l) + 2, omega=omega, c_l=c_l, exterior_monopole=True)
    mom = ps_old.discrete_moments(f, lmax=1)
    rep_anchor_rows = [int(i) for i in torch.nonzero(ps_new.anchor_rows).flatten().tolist()]
    P1, g1, Plm1, dPlm1 = ps_old.solve(f); P2, g2, Plm2, dPlm2 = ps_new.solve(f)
    q0 = [i for i, (l, m, t) in enumerate(ps_old.pmodes) if l == 0][0]
    anchors = list(range(model.Nr_src, model.Nr)); rr = model.r[anchors]
    M0 = mom["(0,0,0)"]["M"]; alpha = alpha_of(c_l)
    rep = dict(pair=case.pair, anchor_rows_used=rep_anchor_rows, moments={k: dict(ratio=v["ratio"], M=v["M"], abs_sum=v["abs_sum"]) for k, v in mom.items()},
               anchor_radii=[float(x) for x in rr], P00_old=[float(Plm1[j, q0]) for j in anchors], P00_new=[float(Plm2[j, q0]) for j in anchors],
               dP00_old=[float(dPlm1[j, q0]) for j in anchors], dP00_new=[float(dPlm2[j, q0]) for j in anchors],
               predicted_P00_change_minus_M0_over_r=[-M0 / float(x) for x in rr], predicted_dP00_change_plus_M0_over_r2=[M0 / float(x) ** 2 for x in rr],   # new - old = -M0/r (P), +M0/r^2 (d_r P): P_old = (1/r) int_0^r + ..., P_new = -(1/r) int_r^inf + ... and int_0^r = M0 - int_r^inf
               observed_P00_change=[float(Plm2[j, q0] - Plm1[j, q0]) for j in anchors], observed_dP00_change=[float(dPlm2[j, q0] - dPlm1[j, q0]) for j in anchors],
               gradP_anchor_rel_change=[float((g2[:, j] - g1[:, j]).norm() / max(float(g1[:, j].norm()), 1e-300)) for j in anchors],
               gradP_interior_rel_change=float((g2[:, :model.Nr_src] - g1[:, :model.Nr_src]).norm() / g1[:, :model.Nr_src].norm()),
               true_far_pressure_scale_r_pow_minus_2alpha=[float(x) ** (-2 * alpha) for x in rr])
    # O1 with the option on (same weights/closure state; tables rebuilt by objective_at on the new solver)
    r_old, _ = prob.objective_at(zf, need_aux=False); O_old = 0.5 * float(r_old @ r_old)
    prob.pressure = ps_new; prob.exterior_monopole = True
    r_new, _ = prob.objective_at(zf, need_aux=False); O_new = 0.5 * float(r_new @ r_new)
    far = case.row_group == 2
    rep.update(O1_old=O_old, O1_new=O_new, O1_rel_change=abs(O_new - O_old) / O_old, far_rows_rel_change=float((r_new[far] - r_old[far]).norm() / max(float(r_old[far].norm()), 1e-300)),
               far_rows_norm_old=float(r_old[far].norm()), residual_rel_change=float((r_new - r_old).norm() / r_old.norm()))
    out[cname] = rep
    print(cname, "M0 ratio", f"{mom['(0,0,0)']['ratio']:.2e}", "M1 ratios", {k: f"{v['ratio']:.2e}" for k, v in mom.items() if k.startswith('(1,')}, "O1 rel change", f"{rep['O1_rel_change']:.2e}", "far rows rel change", f"{rep['far_rows_rel_change']:.2e}", flush=True)
    rep["sign_and_value_check"] = dict(P00=[dict(observed=o, predicted=p, abs_diff=abs(o - p)) for o, p in zip(rep["observed_P00_change"], rep["predicted_P00_change_minus_M0_over_r"])],
                                       dP00=[dict(observed=o, predicted=p, abs_diff=abs(o - p)) for o, p in zip(rep["observed_dP00_change"], rep["predicted_dP00_change_plus_M0_over_r2"])])
    print("   P00 change observed/predicted (-M0/r):", [f"{o:.3e}/{p:.3e}" for o, p in zip(rep["observed_P00_change"], rep["predicted_P00_change_minus_M0_over_r"])], "dP00 (+M0/r^2):", [f"{o:.3e}/{p:.3e}" for o, p in zip(rep["observed_dP00_change"], rep["predicted_dP00_change_plus_M0_over_r2"])], flush=True)
    del case; torch.cuda.empty_cache()
json.dump(out, open(os.path.join(ROOT, "validation", "exterior_monopole_regression.json"), "w"), indent=1, default=str)
print("DONE")
