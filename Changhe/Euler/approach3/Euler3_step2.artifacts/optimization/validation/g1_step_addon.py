"""SPEC v1.18 3.6 (k) (lead 07:41Z): G1 coefficient-column step add-on on the deciding harness (gates.py v5c recording). For a battery case, read its v5c G1_coef record
(validation/gates_gpu_v1_<case>_G1coef_v5.json), find every coefficient column and Jacobian (J_f, J_cw, J_c harness) whose whole column or any group FAILS the
registered rule (stored decisions of the v5c record), and evaluate afresh the two steps 1e-2 s_j and 1e-3 s_j for those columns with column_test (every witness:
per-group norms and errors, active sets with the base, Richardson witnesses of the pair), using the same column constructions as gates.py (J_f: jvp of
residual_vector; J_cw: jvp of residual_vector_wd; J_c: tables and weights differentiable with the closure block by five-point differences at 1e-4 s_j).
Decision under (k) per column and group: both steps of the pair within tau (second order and five point) and the pair's Richardson within tau; the per-decade
error ratio e(1e-2 s_j)/e(1e-3 s_j) is recorded. Only the comparison of this pair is new; nothing of the registered ladder is changed.
Usage: CUDA_VISIBLE_DEVICES=<gpu> python validation/g1_step_addon.py <case> [record json]  -> validation/g1_step_addon_<case>.json (label "pass under the post-result step rule (k)")"""
import sys, os, json, time, hashlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from validation.gates import Case, ROOT, PAIRS, column_test, code_hashes
dev = "cuda:0" if torch.cuda.is_available() else "cpu"
cname = sys.argv[1]; rec_path = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, "validation", f"gates_gpu_v1_{cname}_G1coef_v5.json")
for _ in range(180):                                                       # the input record may still be in the making (queue order): wait up to 30 min
    if os.path.exists(rec_path):
        break
    time.sleep(10)
if not os.path.exists(rec_path):
    print("input record missing:", rec_path); sys.exit(3)
D = json.load(open(rec_path)); entries = dict(D.get("cases", {}))
for k, v in D.items():
    if isinstance(v, dict) and v.get("partial") and k not in entries:
        entries[k] = v
C = entries[cname]
defs = {"S01_own": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")), "S09_own": dict(start=os.path.join(ROOT, "starts", "S09_d6w_cl0.45_om0.3_R1.pt")),
        "S05_own": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt")), "S11_own": dict(start=os.path.join(ROOT, "starts", "S11_nest6_cl0.42_om0.3_p0.pt")),
        "S20_own": dict(start=os.path.join(ROOT, "starts", "S20_s4allm_cl0.45_om1.0.pt")),
        "S01_shift_a": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt"), pair=PAIRS["a"]), "S05_shift_c": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt"), pair=PAIRS["c"]),
        "manu_a": dict(pair=PAIRS["a"], seed=3), "manu_small_omega": dict(pair=PAIRS["small_omega"], seed=5), "manu_large_omega": dict(pair=PAIRS["large_omega"], seed=6),
        "manu_near_edge": dict(pair=PAIRS["near_edge"], seed=7), "manu_allm_c": dict(pair=PAIRS["c"], seed=8, m_parity="all")}
t_all = time.time()
case = Case(cname, dev, **defs[cname]); prob = case.prob; zo = case.z_opt; n = zo.numel()
fun = lambda q: prob.residual_vector(case.to_full_opt(q)); fun_w = lambda q: prob.residual_vector_wd(case.to_full_opt(q))
sc_fun_o = lambda q: prob.objective_at(case.to_full_opt(q), need_aux=False)[0]
def act(zz_full):
    ev = prob.evaluate(zz_full, tables=prob.pressure_tables_at(zz_full))
    return prob.nl_active_set(ev) | dict(geometry=prob.pressure.geometry_id)
def jc_coef_column(k, scale):
    def fun_wd(q):
        zz = case.to_full_opt(q); tabs = prob.pressure_tables_at(zz, differentiable=True); ev = prob.evaluate(zz, tables=tabs)
        return prob.residual_vector(zz, tables=tabs, nl_w=prob.nl_weights_from_ev(ev, differentiable=True), closure=prob.closure, ev=ev)
    e = torch.zeros_like(zo); e[k] = 1.0
    col = torch.func.jvp(fun_wd, (zo,), (e,))[1].clone()
    if "closure" in case.block_slices:
        a0, a1 = case.block_slices["closure"]; h = 1e-4 * scale
        crow = lambda q: prob.closure_rows(case.to_full_opt(q), closure=prob.closure_state_at(case.to_full_opt(q)))
        col[a0:a1] = (8 * (crow(zo + h * e) - crow(zo - h * e)) - (crow(zo + 2 * h * e) - crow(zo - 2 * h * e))) / (12 * h)
    return col
JAC = {"Jf": ("G1_Jf_coefficient_columns", lambda k, s: torch.func.jvp(fun, (zo,), (torch.eye(n, device=dev)[k],))[1], fun, None),
       "Jcw": ("G1_Jcw_coefficient_columns", lambda k, s: torch.func.jvp(fun_w, (zo,), (torch.eye(n, device=dev)[k],))[1], fun_w, lambda q: act(case.to_full_opt(q))),
       "Jc": ("G1_Jc_coefficient_columns", jc_coef_column, sc_fun_o, lambda q: act(case.to_full_opt(q)))}
STEPS = [1e-2, 1e-3]; TAU_ALL = 1e-6; TAU_GROUP = 1e-5
out = dict(ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), case=cname, device=dev, input_record=os.path.relpath(rec_path, ROOT), input_record_sha256=hashlib.sha256(open(rec_path, "rb").read()).hexdigest(),
           code_sha256=code_hashes(), steps_nominal=STEPS, rule="SPEC v1.18 3.6 (k): pair (1e-2 s_j, 1e-3 s_j); pass if both steps within tau (second order and five point) and the pair Richardson within tau; label 'pass under the post-result step rule (k)'", jacobians={})
for jac, (key, colfun, reffun, rec_act) in JAC.items():
    res = (C.get(key) or {}).get("results") or []; jres = {}
    for e_ in res:
        r = e_.get("Jf", e_) if jac == "Jf" else e_; k = e_.get("column", r.get("column"))
        failing_groups = [g for g, gp in (r.get("group_pass") or {}).items() if isinstance(gp, dict) and not gp.get("PASS")]
        if r.get("PASS") and not failing_groups:
            continue
        s_j = float(r.get("step_scale", 1.0))
        e = torch.zeros_like(zo); e[k] = 1.0
        col = colfun(k, s_j)
        t = column_test(case, f"G1 (k) add-on {jac} column {k}", col, reffun, zo, e, STEPS, ref=case.r, record_active=rec_act, scale=s_j)
        def pair_decision(e2, e4, rich):
            l2, l3 = f"{1e-2:.0e}", f"{1e-3:.0e}"
            both2 = e2.get(l2) is not None and e2.get(l3) is not None and e2[l2] <= TAU_ALL and e2[l3] <= TAU_ALL
            both4 = e4.get(l2) is not None and e4.get(l3) is not None and e4[l2] <= TAU_ALL and e4[l3] <= TAU_ALL
            ratio = (e2[l2] / e2[l3]) if (e2.get(l3) not in (None, 0.0) and e2.get(l2) is not None) else None
            return dict(both_steps_second_order=both2, both_steps_five_point=both4, richardson=rich, PASS_k=bool(both2 and both4 and rich is not None and rich <= TAU_ALL), error_ratio_1e2_over_1e3=ratio)
        whole = pair_decision(t["errors_second_order"], t["errors_five_point"], t["richardson_error"])
        groups = {}
        for g, gp in t["group_pass"].items():
            if g == "all":
                continue
            e2 = {h: t["per_group"][h]["second_order"].get(g) for h in t["per_group"]}; e4 = {h: t["per_group"][h]["five_point"].get(g) for h in t["per_group"]}
            tau = TAU_GROUP
            l2, l3 = f"{1e-2:.0e}", f"{1e-3:.0e}"
            both2 = e2.get(l2) is not None and e2.get(l3) is not None and e2[l2] <= tau and e2[l3] <= tau
            both4 = e4.get(l2) is not None and e4.get(l3) is not None and e4[l2] <= tau and e4[l3] <= tau
            rich = gp.get("richardson_error")
            groups[g] = dict(both_steps_second_order=both2, both_steps_five_point=both4, richardson=rich, PASS_k=bool(both2 and both4 and rich is not None and rich <= tau),
                             error_ratio_1e2_over_1e3=((e2[l2] / e2[l3]) if (e2.get(l3) not in (None, 0.0) and e2.get(l2) is not None) else None), registered_failing=(g in failing_groups))
        jres[str(k)] = dict(column=k, step_scale=s_j, registered_PASS=r.get("PASS"), registered_failing_groups=failing_groups, whole=whole, groups=groups, column_test=t)
        print(f"{jac} col {k} (s_j {s_j:.3g}): whole PASS_k {whole['PASS_k']} (ratio {whole['error_ratio_1e2_over_1e3']}); groups: " + ", ".join(f"{g}:{'P' if v['PASS_k'] else 'F'}" + ("*" if v["registered_failing"] else "") for g, v in groups.items()), flush=True)
    out["jacobians"][jac] = dict(record_key=key, n_columns_reevaluated=len(jres), columns=jres)
out["seconds"] = time.time() - t_all
json.dump(out, open(os.path.join(ROOT, "validation", f"g1_step_addon_{cname}.json"), "w"), indent=1, default=str)
print("DONE", cname, {j: v["n_columns_reevaluated"] for j, v in out["jacobians"].items()}, f"{out['seconds']:.0f}s")
