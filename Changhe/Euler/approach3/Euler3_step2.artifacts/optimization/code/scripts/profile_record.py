#!/usr/bin/env python
"""scripts/profile_record.py v2.2 (2026-10-30T10:4xZ; V727 wording: gD is the pre-step frozen-model scaled gradient; the holdouts are the normalized-state battery values). v2.1 (2026-10-30T10:2xZ: the equal-count reading also without the gauge row, from the stored block split of the k*-th accepted iterate of both runs). v2 (2026-10-30T09:0xZ; lead 08:54:48Z item 4 after V697: holdout values from the flat keys of results.jsonl (rho_u_max_holdout, rho_u_max_holdout_half, ...), battery_set and the sha256 of results.jsonl recorded, "after the same budget" only when same_budget is true, otherwise "after k and k' accepted iterations"; the equal-count reading k* = min(accepted counts) added (lead 07:24:37Z item 4)). v1 (2026-10-30T05:5xZ; lead 02:59:34Z item 2, 05:16:32Z item (4)): the record of ONE PROFILE run (or of the reference run) from the worker's own
saved outputs, no field evaluation: from runs/<job>/checkpoint_segment_end.pt (history: accepted iterations with cost, elapsed, cost_blocks incl. the gauge block, the
complete gradient of O1 at the new iterate, the scaled gradient) and runs/<job>/results.jsonl (iteration-0 O1 = cost0 and its block split cost_blocks_projected of the
start state after the worker's entry path; the end battery holdouts; stop status; v10 last-tenth decrease):
  - the O1 trajectory (it_cum, cost, elapsed) and the parameters (fixed);
  - O1 without the gauge row at iteration 0 (start blocks: total - gauge) and at the end (last accepted iterate's blocks);
  - the relative fall of O1 over the last 10 accepted iterations (and over the last tenth, as the worker records);
  - the stop reason (lm_status: max_iter / time_limit / ...), accepted and rejected counts, LM seconds;
  - the SPEC 7.4 quantities the worker writes at its end: the PRE-STEP frozen-model scaled gradient ||g_D||_inf / ||r|| of the last accepted iteration (gD_inf_over_r; V727: not a complete scaled gradient), the complete
    gradient at the NEW iterate without column scaling (g_inf, g_inf_over_r), the last-50 relative fall where available; the holdout values are the worker end battery's, computed on the F-normalized end state, not on the raw optimizer endpoint that carries O1 (V727); parameter gradients are empty for FIXED runs (no parameter columns);
  - the end-battery holdout rho_u^max (standard / half-offset) and the core diagnostics from results.jsonl where present.
With --reference <run dir> the same quantities of the reference run (the base state's own PROFILE run) are put beside them and the point is called "lower" only if its
end value after the same budget is below the reference's (lead 02:59:34Z item 2); a higher value at a soft point is "possibly budget-limited", not a minimum.
Usage: python scripts/profile_record.py <run dir> [--reference <run dir>] [--out validation/profile_records/<job>.json]"""
import os, sys, json, time, hashlib, argparse
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import torch
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()


def read_run(run):
    run = os.path.abspath(run); ck_path = os.path.join(run, "checkpoint_segment_end.pt")
    if not os.path.exists(ck_path):
        ck_path = os.path.join(run, "checkpoint.pt")
    ck = torch.load(ck_path, map_location="cpu", weights_only=False); cur = ck["current"]; hist = [h for h in cur["history"] if h.get("accepted", True)]
    res_path = os.path.join(run, "results.jsonl"); res = [json.loads(l) for l in open(res_path)] if os.path.exists(res_path) else []
    sr = next((r for r in res if r.get("kind") == "start_result"), res[-1] if res else {})
    traj = [dict(it=int(h.get("it_cum", h["it"])), cost=float(h["cost"]), elapsed=float(h["elapsed"]), gauge=float((h.get("cost_blocks") or {}).get("gauge", float("nan")))) for h in hist]
    cost0 = float(cur["meta"].get("cost0", float("nan"))); blocks0 = sr.get("cost_blocks_projected") or sr.get("cost_blocks_parent") or {}
    gauge0 = float(blocks0.get("gauge", float("nan"))) if blocks0 else float("nan")
    last = hist[-1] if hist else {}; blocks_end = last.get("cost_blocks") or {}
    def rel_fall(n):
        if len(traj) <= n:
            return None
        a, b = traj[-1 - n]["cost"], traj[-1]["cost"]; return (a - b) / a if a > 0 else None
    cg = last.get("complete_gradient") or {}
    # iteration-0 block split: the worker does not record the start's blocks (cost_blocks_projected is empty); for the P1 s4 PROFILE points the kept start's entry O1 and its
    # gauge part were measured by the linear-response tool at the same parameters (validation/lrs/P1s4_profile_<name>.json, tool v1; P1s4_dp0.json for the reference):
    # the same state through the same entry path, so cost0 must agree with it (relative difference recorded as a consistency check)
    lrs = None; jid = str(ck.get("job_id", ""))
    if jid.startswith("prof_P1s4_"):
        nm = jid[len("prof_P1s4_"):].split("_L6")[0]
        lp = os.path.join(ROOT, "validation", "lrs", "P1s4_dp0.json" if nm == "reference" else f"P1s4_profile_{nm}.json")
        if os.path.exists(lp):
            L = json.load(open(lp)); ke = L["objective"]["kept"]["entry"]
            lrs = dict(file=lp, sha256=sha(lp), kept_entry_O1=ke["O1"], kept_entry_gauge_part=ke["gauge_part"], kept_entry_O1_without_gauge=ke["O1_without_gauge"], params=L["params_after"],
                       rel_diff_cost0_vs_lrs=((cost0 - ke["O1"]) / ke["O1"] if ke["O1"] else None), note="measured by scripts/linear_response_start.py v1 for the kept start at the same parameters through the worker's entry path (the same state as this PROFILE run's start)")
            if gauge0 != gauge0:
                gauge0 = float(ke["gauge_part"])
    out = dict(run=run, job_id=ck.get("job_id"), label=ck.get("label"), iteration0_blocks_source=("worker start_result cost_blocks_projected" if blocks0 else ("linear-response tool record (same state)" if lrs else "not available")), lrs_iteration0=lrs, checkpoint=ck_path, checkpoint_sha256=sha(ck_path), params=dict(c_l=float(ck["config"]["c_l"]), omega=float(ck["config"]["omega"])), free_params=bool(ck["config"].get("free_params", False)),
               max_iter=ck["config"].get("max_iter"), time_limit_s=ck["config"].get("time_limit_per_start"), stop_reason=cur.get("lm_status"), counters=cur.get("counters"), accepted_iterations=len(traj), lm_seconds=(traj[-1]["elapsed"] if traj else None),
               O1_iteration0=cost0, O1_iteration0_without_gauge=(cost0 - gauge0 if gauge0 == gauge0 else None), gauge_iteration0=(gauge0 if gauge0 == gauge0 else None), start_blocks=blocks0,
               O1_end=(traj[-1]["cost"] if traj else None), O1_end_without_gauge=((traj[-1]["cost"] - float(blocks_end.get("gauge"))) if traj and "gauge" in blocks_end else None), end_blocks=blocks_end,
               rel_fall_last10=rel_fall(10), rel_fall_last50=rel_fall(50), v10_last_tenth_rel_decrease=sr.get("v10_last_tenth_rel_decrease"), v10_iterations=sr.get("v10_iterations"),
               spec74=dict(gD_inf_over_r_last=last.get("gD_inf_over_r"), gD_2_over_r_last=last.get("gD_2_over_r"), gD_note="pre-step frozen-model scaled gradient of the last accepted iteration (V727), not a complete scaled gradient", complete_gradient_new_iterate=dict(g_inf=cg.get("g_inf"), g_2=cg.get("g_2"), g_inf_over_r=cg.get("g_inf_over_r"), g_2_over_r=cg.get("g_2_over_r"), note="complete gradient at the new iterate without column scaling"), g_param_scaled=last.get("g_param_scaled"), note="FIXED runs have no parameter columns: parameter gradients empty; (b) eta and the reduced model need the J_c EVAL (lead tool), not written by the worker"),
               holdout=dict(basis="worker end battery of the F-normalized end state (V727: not the raw optimizer endpoint)", rho_u_max_holdout=sr.get("rho_u_max_holdout"), rho_u_max_holdout_half=sr.get("rho_u_max_holdout_half"), rho_u_max_holdout_both=sr.get("rho_u_max_holdout_both"), rho_u_max_train=sr.get("rho_u_max"),
                            tier_S_holdout=sr.get("tier_S_holdout"), tier_S_holdout_half=sr.get("tier_S_holdout_half"), sigma_u_max=sr.get("sigma_u_max"), a_max_core=sr.get("a_max_core"), a_max_core_upper=sr.get("a_max_core_upper"),
                            N_core=sr.get("N_core"), N_core_holdout=sr.get("N_core_holdout"), r_core_holdout=sr.get("r_core_holdout"), core_resolved=sr.get("core_resolved"), rho_Om_max_holdout=sr.get("rho_Om_max_holdout"),
                            rms_final=sr.get("rms_final"), cost_final=sr.get("cost_final"), status=sr.get("status"), gauge_defect=sr.get("gauge_defect"), note="flat keys of the worker's start_result row (v2); None = not in the record"),
               battery_set=sr.get("battery_set"), results_jsonl=(res_path if os.path.exists(res_path) else None), results_jsonl_sha256=(sha(res_path) if os.path.exists(res_path) else None), t_battery_s=sr.get("t_battery_s"), t_lm_s=sr.get("t_lm_s"),
               trajectory=traj)
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("run"); ap.add_argument("--reference"); ap.add_argument("--out"); a = ap.parse_args()
    rec = read_run(a.run); rec["tool"] = "scripts/profile_record.py v2.2"; rec["tool_sha256"] = sha(os.path.abspath(__file__)); rec["ts"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    if a.reference:
        ref = read_run(a.reference); rec["reference"] = {k: ref[k] for k in ref if k != "trajectory"}
        if rec["O1_end"] is not None and ref["O1_end"] is not None:
            same_budget = (rec["max_iter"] == ref["max_iter"] and rec["time_limit_s"] == ref["time_limit_s"])
            kp, kr = rec["accepted_iterations"], ref["accepted_iterations"]; kstar = min(kp, kr)
            tp, tr = rec["trajectory"], ref["trajectory"]
            o_p = tp[kstar - 1]["cost"] if kstar >= 1 and len(tp) >= kstar else None; o_r = tr[kstar - 1]["cost"] if kstar >= 1 and len(tr) >= kstar else None
            # v2.1: the same readings without the gauge row (the worker stores the block split of every accepted iterate; the kept entry at a moved parameter point carries a large gauge-row violation)
            g_p = tp[kstar - 1].get("gauge") if kstar >= 1 and len(tp) >= kstar else None; g_r = tr[kstar - 1].get("gauge") if kstar >= 1 and len(tr) >= kstar else None
            ng_p = (o_p - g_p) if (o_p is not None and g_p is not None and g_p == g_p) else None; ng_r = (o_r - g_r) if (o_r is not None and g_r is not None and g_r == g_r) else None
            if same_budget:
                reading = ("lower than the reference after the same budget (max_iter %s, time limit %s s; %d and %d accepted iterations)" % (rec["max_iter"], rec["time_limit_s"], kp, kr)) if rec["O1_end"] < ref["O1_end"] else \
                          ("not lower than the reference after the same budget (max_iter %s, time limit %s s; %d and %d accepted iterations): possibly budget-limited, not evidence of a minimum (lead 02:59:34Z item 2)" % (rec["max_iter"], rec["time_limit_s"], kp, kr))
            else:
                reading = "budgets differ (point max_iter %s / %s s, reference %s / %s s): end values after %d and %d accepted iterations; no matched 'lower' verdict (V697); use the equal-count reading at k*" % (rec["max_iter"], rec["time_limit_s"], ref["max_iter"], ref["time_limit_s"], kp, kr)
            rec["comparison"] = dict(point_O1_end=rec["O1_end"], reference_O1_end=ref["O1_end"], ratio=rec["O1_end"] / ref["O1_end"], lower_than_reference=((rec["O1_end"] < ref["O1_end"]) if same_budget else None),
                                     point_O1_end_without_gauge=rec["O1_end_without_gauge"], reference_O1_end_without_gauge=ref["O1_end_without_gauge"], same_budget=same_budget, accepted_point=kp, accepted_reference=kr,
                                     equal_count=dict(k_star=kstar, point_O1_at_k_star=o_p, reference_O1_at_k_star=o_r, ratio_at_k_star=((o_p / o_r) if (o_p and o_r) else None),
                                                      point_gauge_at_k_star=g_p, reference_gauge_at_k_star=g_r, point_O1_without_gauge_at_k_star=ng_p, reference_O1_without_gauge_at_k_star=ng_r,
                                                      ratio_without_gauge_at_k_star=((ng_p / ng_r) if (ng_p and ng_r) else None),
                                                      lower_at_k_star=((o_p < o_r) if (o_p is not None and o_r is not None) else None), note="O1 after the same number k* = min(k, k') of accepted iterations (lead 07:24:37Z item 4); wall times differ under the host load"),
                                     holdout_point=dict(std=rec["holdout"]["rho_u_max_holdout"], half=rec["holdout"]["rho_u_max_holdout_half"], battery_set=rec["battery_set"]), holdout_reference=dict(std=ref["holdout"]["rho_u_max_holdout"], half=ref["holdout"]["rho_u_max_holdout_half"], battery_set=ref["battery_set"]),
                                     reading=reading)
    out = a.out or os.path.join(ROOT, "validation", "profile_records", os.path.basename(os.path.abspath(a.run)) + ".json"); os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(rec, open(out, "w"), indent=1, default=str)
    print(f"{rec['job_id']}: ({rec['params']['c_l']:.6f}, {rec['params']['omega']:.6f}) it0 O1 {rec['O1_iteration0']:.6e} (without gauge {rec['O1_iteration0_without_gauge']}) -> end {rec['O1_end']} (without gauge {rec['O1_end_without_gauge']}); {rec['accepted_iterations']} accepted, stop {rec['stop_reason']}, last-10 fall {rec['rel_fall_last10']}; gD_inf/r {rec['spec74']['gD_inf_over_r_last']}; written {out}")


if __name__ == "__main__":
    main()
