# Snapshot gpu_v1 addendum 9 (test-only, specification v1.18 3.6 (k), lead 07:41Z): G1 step add-on and checker v7; written 2026-10-29T07:45:43Z

validation/g1_step_addon.py e8ea779cf9a84710 (new): on the deciding harness v5c (column_test with every witness, active sets with the base, Richardson witnesses), for a case's v5c G1_coef record, every coefficient column and Jacobian whose whole column or any group fails the registered rule is re-evaluated afresh at the two steps 1e-2 s_j and 1e-3 s_j with the same column constructions as gates.py (J_f, J_cw, harness J_c with the closure block at 1e-4 s_j); decision under (k) per column and group: both steps within tau (second order and five point) and the pair Richardson within tau; the per-decade error ratio e(1e-2 s_j)/e(1e-3 s_j) is recorded; output validation/g1_step_addon_<case>.json with the input record's sha256 and the code hashes. validation/g1_coverage_check.py d4a78f1339a5ebf6 (v6, kept as .v6_d4a78f13) -> e53bd772d7b7dfaa (v7): three outcomes per case and Jacobian: registered; with (k) (label 'pass under the post-result step rule (k)', failing columns, per-decade ratios; the add-on record must derive from the same v5c record, checked by hash); with (k) and (j) together (small-amplitude groups excluded, remaining failures may pass under (k), coverage recomputed). The queue runs the add-on for S09_own, S01_own, S05_own and manu_large_omega after the v5c G1_coef reruns and ahead of g8_tables.

## g1_step_addon.py (full text)
```
"""specification v1.18 3.6 (k) (lead 07:41Z): G1 coefficient-column step add-on on the deciding harness (gates.py v5c recording). For a battery case, read its v5c G1_coef record
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
           code_sha256=code_hashes(), steps_nominal=STEPS, rule="specification v1.18 3.6 (k): pair (1e-2 s_j, 1e-3 s_j); pass if both steps within tau (second order and five point) and the pair Richardson within tau; label 'pass under the post-result step rule (k)'", jacobians={})
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
```

## diff checker v6 -> v7
```
--- validation/g1_coverage_check.py.v6_d4a78f13	2026-10-29 07:45:06.018131505 +0000
+++ validation/g1_coverage_check.py	2026-10-29 07:45:06.078131633 +0000
@@ -1,5 +1,9 @@
 #!/usr/bin/env python
-"""v6 (07:4xZ, V195): (1) a record whose convention is v5c must carry full pair witnesses for all four nominal pairs (no fallback to a scalar summary); salvage of
+"""v7 (07:5xZ, specification v1.18 3.6 (k), lead 07:41Z): three outcomes per case and Jacobian: registered; with the post-result step rule (k) (a column or group that fails
+the registered ladder passes under (k) when the add-on validation/g1_step_addon_<case>.json shows the pair (1e-2 s_j, 1e-3 s_j) passing: both steps within tau,
+second order and five point, and the pair Richardson within tau; label "pass under the post-result step rule (k)", with the per-decade error ratio); with (k)
+and the small-amplitude rule (j). The add-on record must be on the same case and come from the same v5c coefficient record (input hash recorded).
+v6 (07:4xZ, V195): (1) a record whose convention is v5c must carry full pair witnesses for all four nominal pairs (no fallback to a scalar summary); salvage of
 older records is allowed only through an explicit allowlist of recorded conventions (v4 and earlier), separately labelled, with the witnesses actually present
 (a recorded Richardson scalar must be finite and non-negative); missing fields never make a record "old"; (2) each of the six registered group decisions
 (group_pass) must exist on every record, iterated from REQUIRED_GROUPS; (3) non-finite, missing or negative pair evidence is INVALID (not FAIL); discrepancies
@@ -247,6 +251,27 @@
         if any(not fin(x) for x in vals):
             return False
     return recompute_group(rec, g)["PASS"]
+def load_addon(cname, record_path):
+    """The (k) add-on record for the case, if present and derived from this record (input_record_sha256)."""
+    ap = os.path.join(os.path.dirname(record_path), f"g1_step_addon_{cname}.json")
+    if not os.path.exists(ap):
+        return None, "no (k) add-on record"
+    a = json.load(open(ap))
+    import hashlib
+    if a.get("input_record_sha256") != hashlib.sha256(open(record_path, "rb").read()).hexdigest():
+        return None, f"add-on record {os.path.basename(ap)} was derived from another input record (hash mismatch)"
+    return a, ""
+def k_pass(addon, jac, col, g=None):
+    """True if the add-on shows the pair (1e-2 s_j, 1e-3 s_j) passing for this column (whole column when g is None, else the group); returns (pass, ratio)."""
+    if not addon:
+        return False, None
+    rec = ((addon.get("jacobians") or {}).get(jac) or {}).get("columns", {}).get(str(col))
+    if not rec:
+        return False, None
+    dec = rec["whole"] if g is None else (rec.get("groups") or {}).get(g)
+    if not isinstance(dec, dict):
+        return False, None
+    return bool(dec.get("PASS_k")), dec.get("error_ratio_1e2_over_1e3")
 def main(files):
     for f in files:
         d = json.load(open(f)); entries = dict(d.get("cases", {}))
@@ -328,7 +353,40 @@
                 phys_ok = all(v.get("status") in (None, "NOT_APPLICABLE", "PASS") for v in rejudge.values())
                 amended_pass = complete_all and bool(ids_match) and phys_ok and all(whole_param.values()) and all(whole_coef.values()) and bool(gres) and all(v["status"] == "PASS" for v in gres.values())
                 amended_status = "PASS" if amended_pass else ("INVALID (incomplete, ids not the drawn columns, or re-judgement pending)" if (not complete_all or not phys_ok or not ids_match) else "OPEN")
-                cres[jac] = dict(registered=registered, amended=dict(status=amended_status, incomplete_records=incomplete, whole_column_parameter=whole_param, whole_column_coefficient=whole_coef, missing_parameter_columns=missing_params, groups=gres,
+                # ---- specification v1.18 3.6 (k): registered outcome with the post-result step rule, and with (k) and (j) together
+                addon, addon_note = load_addon(cname, f)
+                k_cols = {}; k_fail = []; k_ratios = {}
+                for e in cc:
+                    r = col_record(e, jac); k = col_id(e, jac)
+                    rw = recompute_whole(r); rg = {g: recompute_group(r, g) for g in REQUIRED_GROUPS}
+                    ok_whole = rw.get("PASS") or (k_pass(addon, jac, k)[0] if comp_coef.get(k, (False, ""))[0] else False)
+                    groups_ok = {}
+                    for g in REQUIRED_GROUPS:
+                        if rg[g].get("PASS"):
+                            groups_ok[g] = "registered"
+                        else:
+                            pk, ratio = k_pass(addon, jac, k, g)
+                            groups_ok[g] = "pass under the post-result step rule (k)" if pk else "FAIL"
+                            if pk:
+                                k_ratios[f"{k}:{g}"] = ratio
+                    passed = bool(comp_coef.get(k, (False, ""))[0]) and ok_whole and all(v != "FAIL" for v in groups_ok.values())
+                    k_cols[k] = dict(PASS=passed, whole="registered" if rw.get("PASS") else ("pass under the post-result step rule (k)" if ok_whole else "FAIL"), groups=groups_ok)
+                    if not passed:
+                        k_fail.append(k)
+                params_ok = (not missing_params) and all(v in ("PASS",) or str(v).startswith("REJUDGED_PASS") for v in reg_param.values())
+                with_k = dict(status=("PASS" if (params_ok and ids_match and bool(cc) and not k_fail and all(c[0] for c in comp_coef.values())) else ("INVALID" if registered["INVALID"] else "FAIL")),
+                              failing_columns=k_fail, columns=k_cols, error_ratios_1e2_over_1e3=k_ratios, addon=(None if addon is None else os.path.basename(os.path.join(os.path.dirname(f), f"g1_step_addon_{cname}.json"))), addon_note=addon_note,
+                              label="registered rule with the post-result step rule (k) (specification v1.18 3.6 (k))")
+                # (k) and (j): small-amplitude groups excluded as in the amended outcome, the remaining failures may pass under (k)
+                kj_groups = {}
+                for g, gv in gres.items():
+                    fails = [k for k in gv["coefficient_columns_failing_not_small_amplitude"] if not k_pass(addon, jac, k, g)[0]]
+                    passes_k = [k for k in gv["coefficient_columns_failing_not_small_amplitude"] if k_pass(addon, jac, k, g)[0]]
+                    cov = len(set(gv["coefficient_columns_passing"]) | set(passes_k))
+                    kj_groups[g] = dict(status=("PASS" if (not gv["parameter_columns_failing_or_missing"] and not fails and cov >= MIN_COEF) else "OPEN"), failing=fails, pass_under_k=passes_k, coverage=cov, small_amplitude_not_tested=gv["coefficient_columns_small_amplitude_not_tested"])
+                with_kj = dict(status=("PASS" if (complete_all and ids_match and phys_ok and all(whole_param.values()) and all((whole_coef[k] or k_pass(addon, jac, k)[0]) for k in whole_coef) and bool(kj_groups) and all(v["status"] == "PASS" for v in kj_groups.values())) else ("INVALID" if not (complete_all and ids_match and phys_ok) else "OPEN")),
+                               groups=kj_groups, label="post-result rules (k) and (j) together (specification v1.18 3.6 (k) (7))")
+                cres[jac] = dict(registered=registered, with_k=with_k, with_k_and_j=with_kj, amended=dict(status=amended_status, incomplete_records=incomplete, whole_column_parameter=whole_param, whole_column_coefficient=whole_coef, missing_parameter_columns=missing_params, groups=gres,
                                                                      resolved_coverage_counts={g: v["n_coverage_distinct"] for g, v in gres.items()}), label=LABEL)
             report["cases"][cname] = cres
         outp = f[:-5] + "_coverage.json"; json.dump(report, open(outp, "w"), indent=1)
@@ -337,7 +395,8 @@
             for jac, v in cres.items():
                 am = v["amended"]
                 rg = v["registered"]; npass = sum(1 for x in rg["coefficient_columns"].values() if x == "PASS")
-                print(f"- {cname} {jac}: registered {'PASS' if rg['PASS'] else ('INVALID' if rg.get('INVALID') else 'FAIL')} ({npass}/{rg['n_distinct_coefficient_columns']} distinct coefficient columns PASS; parameters {rg['parameter_columns']}); amended {am.get('status')}" + (f" ({am.get('reason')})" if am.get("reason") else "") + (f"; incomplete: {am.get('incomplete_records')}" if am.get("incomplete_records") else ""))
+                wk = v.get("with_k") or {}; wkj = v.get("with_k_and_j") or {}
+                print(f"- {cname} {jac}: registered {'PASS' if rg['PASS'] else ('INVALID' if rg.get('INVALID') else 'FAIL')} ({npass}/{rg['n_distinct_coefficient_columns']} distinct coefficient columns PASS; parameters {rg['parameter_columns']}); with (k): {wk.get('status')} (failing {wk.get('failing_columns')}; {wk.get('addon_note') or wk.get('addon')}); with (k)+(j): {wkj.get('status')}; amended (j) only: {am.get('status')}" + (f" ({am.get('reason')})" if am.get("reason") else "") + (f"; incomplete: {am.get('incomplete_records')}" if am.get("incomplete_records") else ""))
                 for g, gv in (am.get("groups") or {}).items():
                     print(f"    - {g}: {gv['status']}; coverage {gv['n_coverage_distinct']} distinct columns {gv['coefficient_columns_passing']}; failing (not small-amplitude) {gv['coefficient_columns_failing_not_small_amplitude']}; small-amplitude (not tested) {gv['coefficient_columns_small_amplitude_not_tested']}; parameter columns failing or missing {gv['parameter_columns_failing_or_missing']}")
 if __name__ == "__main__":
```
