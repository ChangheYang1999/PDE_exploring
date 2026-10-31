#!/usr/bin/env python
"""S14 stage (ii) reading (reports/S14_ENQUEUE_20261026.md; lead d128 KK items 1, 4 and message 23:13Z): for one finished L6 all-m promotion job
(single start, init_from = a stage (i) L4 start), report (1) the end state's holdout rho_u^max on both shell families, V10, LM status / iterations /
seconds, whole-job seconds from the stdout.log START and JOB DONE stamps; (2) the S14R-1 collapse check: N_core, N_F, e_core, e_F of the L6 end state
against the same four values of the L4 promoted start (looked up in the stage (i) results.jsonl by the init_from path), ratios L6 / L4, and the SPEC 7.4
flag 'collapsing' if any of the four decreased by more than a factor 2 across the level, 'warning' if any L6 value is below its guard (N 1e-2, e 1e-4);
(3) the odd-m content of the L6 end state from reports/oddm/oddm_<job>_0.json (scripts/odd_m_fraction.py; amplitude and energy) beside the L4 start's
(reports/oddm/oddm_<L4 job>_<k>.json); (4) the holdout against the even-class L6 comparator at the same (c_l, omega) (ledger row named on the command line
with --comparator, e.g. nest6_L6_cl0.45_om+1.0_fixed_p0_om+1.0s43s0; its budget max_iter stated beside this job's: 600 against 300), the ratios on both
families, and the SPEC 7.3b relation through scripts/order_73b.py (which writes reports/arm_reading_<id>.json for both ids); 'no even-class L6 comparator
at this point: coverage reading only' when --comparator is absent. HB item 4 wording is applied by the writer, not by this tool. CPU only; reads saved files.
Usage: .venv/bin/python scripts/s14_stage2_reading.py <L6 job_id> [--comparator <job_id>] [--json]"""
import sys, os, json, re, subprocess, argparse, datetime
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PY = os.path.join(ROOT, ".venv", "bin", "python")
ap = argparse.ArgumentParser(); ap.add_argument("job"); ap.add_argument("--comparator", default=None); ap.add_argument("--json", action="store_true"); a = ap.parse_args()
job = a.job; rdir = os.path.join(ROOT, "runs", job)
rows = [json.loads(l) for l in open(os.path.join(rdir, "results.jsonl")) if l.strip()]
rows = [r for r in rows if r.get("kind") == "start_result"]
assert len(rows) == 1, ("expected one start result", len(rows))
r = rows[0]
def ts(s):
    return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")
log = open(os.path.join(rdir, "stdout.log")).read().splitlines()
start_line = next(l for l in log if " START job " in l)
cfg = json.loads(re.search(r"cfg=(\{.*\})\s*$", start_line).group(1))
t0 = ts(start_line[:20]); t1 = next((ts(l[:20]) for l in log if "JOB DONE" in l), None)
whole = (t1 - t0).total_seconds() if t1 else None
# the L4 promoted start: init_from -> runs/<L4 job>/starts/start_00k.pt -> its results.jsonl row
src = cfg["init_from"]; m = re.search(r"runs/([^/]+)/starts/start_(\d+)\.pt$", src)
l4_job, l4_k = m.group(1), int(m.group(2))
l4_rows = [json.loads(l) for l in open(os.path.join(ROOT, "runs", l4_job, "results.jsonl")) if l.strip()]
l4 = next(x for x in l4_rows if x.get("kind") == "start_result" and x.get("start") == l4_k)
assert os.path.abspath(os.path.join(ROOT, l4["zfile"])) == os.path.abspath(src), (l4["zfile"], src)
GU = dict(N_core=1e-2, N_F=1e-2, e_core=1e-4, e_F=1e-4)
coll = {}
for n in GU:
    v6, v4 = r.get(n), l4.get(n)
    ratio = (v6 / v4) if (v6 is not None and v4 not in (None, 0)) else None
    coll[n] = dict(L4=v4, L6=v6, ratio_L6_over_L4=ratio, collapsing=(ratio is not None and ratio < 0.5), warning=(v6 is not None and v6 < GU[n]))
collapsing = any(c["collapsing"] for c in coll.values()); warning = any(c["warning"] for c in coll.values())
def oddm(path):
    return json.load(open(path)) if os.path.exists(path) else None
od6 = oddm(os.path.join(ROOT, "reports", "oddm", f"oddm_{job}_0.json")); od4 = oddm(os.path.join(ROOT, "reports", "oddm", f"oddm_{l4_job}_{l4_k}.json"))
def ofrac(od):
    return dict(energy_all=od["energy_fraction_odd"]["all"], energy_core=od["energy_fraction_odd"]["core_r_lt_0p125"], energy_tail=od["energy_fraction_odd"]["tail_r_ge_8"], amp_U=od["ratio_all"]["U"], amp_Omega=od["ratio_all"]["Omega"], amp_DU=od["ratio_all"]["DU"], coef_norm_fraction=od["coef_norm_fraction_odd"]) if od else None
comp = None
if a.comparator:
    cj = a.comparator; cfn = os.path.join(ROOT, "reports", f"arm_reading_{cj}.json")
    out = subprocess.run([PY, os.path.join(ROOT, "scripts", "order_73b.py"), job, cj, "--json", os.path.join(ROOT, "reports", f"order_73b_{job}_vs_comparator.json")], cwd=ROOT, env=dict(os.environ, CUDA_VISIBLE_DEVICES="-1"), capture_output=True, text=True)
    crow = json.load(open(cfn))["row"]
    ccfg = None
    for d in ("done", "running", "pending", "failed", "hold"):
        pth = os.path.join(ROOT, "queue", d, cj + ".json")
        if os.path.exists(pth):
            ccfg = json.load(open(pth)).get("config", {}); break
    rel = [l for l in out.stdout.splitlines() if l.startswith("| " + job) or l.startswith("| " + cj)]
    comp = dict(comparator=cj, holdout_std=crow.get("rho_u_max_holdout"), holdout_half=crow.get("rho_u_max_holdout_half"), ratio_std=(r["rho_u_max_holdout"] / crow["rho_u_max_holdout"]) if crow.get("rho_u_max_holdout") else None,
                ratio_half=(r.get("rho_u_max_holdout_half") / crow["rho_u_max_holdout_half"]) if (crow.get("rho_u_max_holdout_half") and r.get("rho_u_max_holdout_half")) else None,
                comparator_max_iter=(ccfg or {}).get("max_iter"), comparator_iterations=crow.get("iterations"), comparator_status=crow.get("status"), this_max_iter=cfg.get("max_iter"),
                order_73b_lines=rel, order_73b_json=f"reports/order_73b_{job}_vs_comparator.json", order_73b_stdout_tail=out.stdout.splitlines()[-3:])
cv = r.get("code_versions") or {}
res = dict(job=job, c_l=cfg.get("c_l"), omega=cfg.get("omega"), config=dict(L=cfg.get("L"), Nk=cfg.get("Nk"), Nr=cfg.get("Nr"), m_parity=cfg.get("m_parity"), channels=cfg.get("channels"), closure_lambda=cfg.get("closure_lambda"), chunk=cfg.get("chunk"), max_iter=cfg.get("max_iter"), time_limit_per_start=cfg.get("time_limit_per_start"), nl_denominator=cfg.get("nl_denominator")),
           init_from=src, l4_job=l4_job, l4_start=l4_k, l4_family=l4.get("family"), l4_rng_seed=l4.get("rng_seed"),
           status=r.get("status"), iterations=r.get("iterations"), lm_seconds=r.get("seconds"), job_start=t0.strftime("%Y-%m-%dT%H:%M:%SZ"), job_done=(t1.strftime("%Y-%m-%dT%H:%M:%SZ") if t1 else None), whole_job_seconds=whole,
           holdout_std=r.get("rho_u_max_holdout"), holdout_half=r.get("rho_u_max_holdout_half"), l4_holdout_std=l4.get("rho_u_max_holdout"), l4_holdout_half=l4.get("rho_u_max_holdout_half"),
           v10=r.get("v10_last_tenth_rel_decrease"), rms_mom=r.get("rms_mom"), cost_final=r.get("cost_final"), rho_nl_max_holdout=r.get("rho_nl_max_holdout"), max_U=r.get("max_U"), max_abs_Omega=r.get("max_abs_Omega"),
           core_resolved=r.get("core_resolved"), a_max_core=r.get("a_max_core"), sigma_u_max_core=r.get("sigma_u_max_core"), sigma_Om=r.get("sigma_Om"), a_eff=r.get("a_eff"), E_ren=r.get("E_ren"), H_tot_over_abs=r.get("H_tot_over_abs"),
           K_E_ratio=r.get("K_ratio_direct"), K_H_ratio=r.get("K_H_ratio_direct"), G_carried_mismatch_rel=r.get("G_carried_mismatch_rel"), Q_sw=r.get("Q_sw"), tau_F_R8=r.get("tau_F_R8"), rotation_content_rel=r.get("rotation_content_rel"),
           collapse_check=dict(values=coll, collapsing=collapsing, warning=warning, rule="SPEC 7.4: warning if N_core < 1e-2, N_F < 1e-2, e_core < 1e-4 or e_F < 1e-4; collapsing if any decreases by more than 2x per refinement level (L4 -> L6)"),
           odd_m_L6=ofrac(od6), odd_m_L4=ofrac(od4), comparator=comp, failure=r.get("failure"), code_versions={k: v.get("sha256_12") for k, v in cv.items()} if isinstance(cv, dict) else cv)
def f(v, fmt="%.4f"):
    return (fmt % v) if isinstance(v, (int, float)) and v is not None else "n/a"
print(f"# S14 stage (ii) reading: {job} (c_l {res['c_l']}, omega {res['omega']}; L6 Nk16 all-m from {l4_job} start {l4_k} ({l4.get('family')}, seed {l4.get('rng_seed')}); status {r.get('status')} after {r.get('iterations')} iterations, LM {f(r.get('seconds'), '%.0f')} s, whole job {f(whole, '%.0f')} s = {f((whole or 0) / 3600, '%.2f')} GPU-h)")
print(f"HOLDOUT rho_u^max std / half: L6 {f(res['holdout_std'])} / {f(res['holdout_half'])}; L4 start {f(res['l4_holdout_std'])} / {f(res['l4_holdout_half'])} (ratio L6/L4 {f(res['holdout_std'] / res['l4_holdout_std'] if res['l4_holdout_std'] else None, '%.3f')} / {f(res['holdout_half'] / res['l4_holdout_half'] if (res['l4_holdout_half'] and res['holdout_half']) else None, '%.3f')}); V10 {f(res['v10'], '%.2e')}; rms_mom {f(res['rms_mom'], '%.4g')}; rho_nl^max {f(res['rho_nl_max_holdout'], '%.3g')}")
print("COLLAPSE CHECK (S14R-1): " + "; ".join(f"{n} L4 {f(c['L4'], '%.3g')} -> L6 {f(c['L6'], '%.3g')} (x{f(c['ratio_L6_over_L4'], '%.2f')})" for n, c in coll.items()) + f" -> {'COLLAPSING' if collapsing else 'not collapsing'}{'; WARNING (below a guard value)' if warning else ''}")
print(f"ODD-M L6: " + (f"energy all / core / tail {f(res['odd_m_L6']['energy_all'], '%.3f')} / {f(res['odd_m_L6']['energy_core'], '%.3f')} / {f(res['odd_m_L6']['energy_tail'], '%.3f')}; amplitude U / Omega / DU {f(res['odd_m_L6']['amp_U'], '%.3f')} / {f(res['odd_m_L6']['amp_Omega'], '%.3f')} / {f(res['odd_m_L6']['amp_DU'], '%.3f')}" if od6 else "not computed (run scripts/odd_m_fraction.py on the L6 start)") + "; L4 start: " + (f"energy all {f(res['odd_m_L4']['energy_all'], '%.3f')}, amplitude U {f(res['odd_m_L4']['amp_U'], '%.3f')}" if od4 else "n/a"))
print(f"CORE / BALANCES: core resolved {res['core_resolved']}; core-set a_max {f(res['a_max_core'], '%.3g')}, sigma_u {f(res['sigma_u_max_core'], '%.3g')}, sigma_Om {f(res['sigma_Om'], '%.3g')}, a_eff {f(res['a_eff'], '%.3g')}; max|U| {f(res['max_U'], '%.3f')}, max|Omega| {f(res['max_abs_Omega'], '%.3g')}; E_ren {f(res['E_ren'], '%.3g')}, H_tot/int|h| {f(res['H_tot_over_abs'], '%.3g')}; K_E / K_H ratio {f(res['K_E_ratio'], '%.3g')} / {f(res['K_H_ratio'], '%.3g')}, carried mismatch m {f(res['G_carried_mismatch_rel'], '%.3g')}; Q_sw {f(res['Q_sw'], '%.3g')}; tau_F {f(res['tau_F_R8'], '%.3g')}; rotation content {f(res['rotation_content_rel'], '%.3g')}")
if comp:
    print(f"COMPARATOR {comp['comparator']}: holdout {f(comp['holdout_std'])} / {f(comp['holdout_half'])} (its budget max_iter {comp['comparator_max_iter']}, {comp['comparator_status']} after {comp['comparator_iterations']} iterations; this job max_iter {comp['this_max_iter']}); ratios this / comparator {f(comp['ratio_std'], '%.3f')} / {f(comp['ratio_half'], '%.3f')}")
    for l in comp["order_73b_lines"]: print("ORDER 7.3b " + l)
else:
    print("COMPARATOR: none given: no even-class L6 comparator at this point, coverage reading only")
print("CODE VERSIONS: " + json.dumps(res["code_versions"], sort_keys=True))
if a.json:
    fn = os.path.join(ROOT, "reports", f"s14_stage2_reading_{job}.json"); json.dump(res, open(fn, "w"), indent=1); print("written", fn)
