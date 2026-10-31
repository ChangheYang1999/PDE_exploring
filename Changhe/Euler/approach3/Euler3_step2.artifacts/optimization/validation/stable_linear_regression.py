"""D6FP: the stable linear operator vs the original sum on saved states and a manufactured field: per-group differences relative to the residual
and to the term sizes, O1 change, jvp compatibility of the parameter columns, and the far-group G1 ladder with the stable evaluation."""
import sys, os, json, time, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
from validation.gates import Case, PAIRS, column_test, ROOT
from src.optimization.lm import param_columns
from src.equations import residuals as res
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
out = {}
for cname, cdef in {"S01_own": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")), "S05_own": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt")), "manu_a": dict(pair=PAIRS["a"], seed=3)}.items():
    case = Case(cname, dev, **cdef); prob, model = case.prob, case.model
    zf = case.z_full
    ev = prob.evaluate(zf)
    mt = ev["mom_terms"]
    Rs, Ro = mt["sum"], mt["sum_original"]
    terms = mt["lin"].abs() + mt["adv"].abs() + mt["rot"].abs() + mt["gradP"].abs()
    groups = torch.where(model.r <= 0.1 * model.R0, 0, torch.where(model.r <= 2.0 ** 8 * model.R0, 1, 2))
    rep = {}
    for gi, g in enumerate(case.group_names[:3]):
        m = groups == gi
        d = (Rs[:, m] - Ro[:, m]).norm(); rep[g] = dict(diff_over_residual=float(d / Ro[:, m].norm()), diff_over_terms=float(d / terms[:, m].norm()), residual_over_terms=float(Ro[:, m].norm() / terms[:, m].norm()))
    # O1 with and without
    r_s, _ = prob.objective_at(zf); c_s = 0.5 * float(r_s @ r_s)
    prob.stable_linear = False; r_o, _ = prob.objective_at(zf); c_o = 0.5 * float(r_o @ r_o); prob.stable_linear = True
    rep["O1_stable"] = c_s; rep["O1_original"] = c_o; rep["O1_rel_change"] = abs(c_s - c_o) / c_o
    # far-group G1 ladder (physical coordinates) with the stable evaluation, frozen-weight residual
    n = case.z_phys.numel(); zp = case.z_phys
    pfun = lambda q: prob.residual_vector(case.to_full_phys(q), differentiable_pressure=True); ref = lambda q: prob.residual_vector_rebuild(case.to_full_phys(q))
    t0 = time.time(); Jp = param_columns(pfun, zp, [n - 2, n - 1]); (torch.cuda.synchronize() if torch.cuda.is_available() else None); rep["t_param_columns"] = time.time() - t0
    for j, pname in enumerate(("c_l", "omega")):
        e = torch.zeros_like(zp); e[n - 2 + j] = 1.0
        scale = case.pair[1] if (pname == "omega" and case.pair[1] < 0.5) else 1.0
        t = column_test(case, f"stable G1 {pname}", Jp[:, j], ref, zp, e, [1e-3, 1e-4, 1e-5, 1e-6, 1e-7], ref=case.r, scale=scale)
        rep[f"G1_{pname}"] = dict(all=t["errors_second_order"], far={h: v["second_order"]["far(r>256R0)"] for h, v in t["per_group"].items()}, core={h: v["second_order"]["core_intermediate"] for h, v in t["per_group"].items()}, PASS=t["PASS"], group_pass={g: v["pass_second_order"] and v["pass_five_point"] for g, v in t["group_pass"].items()}, richardson=t["richardson_error"])
    # vmap compatibility: 3 coefficient columns
    fun = lambda q: prob.residual_vector_wd(case.to_full_opt(q)); zo = case.z_opt
    E = torch.zeros(3, zo.numel(), device=dev); E[0, 5] = 1; E[1, 700] = 1; E[2, 1400] = 1
    Jc = torch.func.vmap(lambda ee: torch.func.jvp(fun, (zo,), (ee,))[1])(E); rep["vmap_ok"] = bool(torch.isfinite(Jc).all())
    out[cname] = rep
    print(cname, json.dumps({k: v for k, v in rep.items() if k.startswith("O1") or k in ("t_param_columns", "vmap_ok")}), flush=True)
    for g in case.group_names[:3]:
        print("   ", g, {k: f"{v:.2e}" for k, v in rep[g].items()}, flush=True)
    for pn in ("c_l", "omega"):
        print(f"   G1 {pn}: all", {h: f"{v:.1e}" for h, v in rep[f'G1_{pn}']['all'].items()}, "far", {h: f"{v:.1e}" for h, v in rep[f'G1_{pn}']['far'].items()}, "PASS", rep[f"G1_{pn}"]["PASS"], rep[f"G1_{pn}"]["group_pass"], flush=True)
    del case; torch.cuda.empty_cache()
json.dump(out, open(os.path.join(ROOT, "validation", "stable_linear_regression.json"), "w"), indent=1, default=str)
print("DONE")
