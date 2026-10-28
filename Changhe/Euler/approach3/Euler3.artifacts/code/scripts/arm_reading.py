#!/usr/bin/env python
"""Standing-lines reading of finished jobs against their start states (RUN_STATUS item 6; R2 / R10-R13 inputs). For each job id: the newest
start_result ledger row, its source job (config.init_from) and the ratios end/start on both shell families. Prints markdown; --json writes
reports/arm_reading_<job>.json. Values are primary-reported and unvalidated; a lower holdout is not a candidate. Usage: arm_reading.py <job_id> [...]"""
import sys, os, json, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
from src.campaign import ledger
recs = ledger.read(os.path.join(ROOT, "status", "ledger.jsonl"))
rows = ledger.merge_reevaluations(recs)
by_job = {}
for r in rows:
    by_job.setdefault(r.get("job_id"), []).append(r)
by_zfile = {r.get("zfile"): r for r in rows if r.get("zfile")}
def job_json(j):
    for d in ("done", "running", "pending", "failed", "cancelled", "hold", "hold_lowprio"):
        p = os.path.join(ROOT, "queue", d, j + ".json")
        if os.path.exists(p):
            return json.load(open(p)), d
    return None, None
def f(v, fmt="%.4g"):
    if v is None: return "n/a"
    if isinstance(v, bool): return "yes" if v else "NO"
    if isinstance(v, (int, float)):
        try: return fmt % v
        except Exception: return str(v)
    return str(v)
METRICS = [("holdout rho_u^max std", "rho_u_max_holdout"), ("holdout rho_u^max half", "rho_u_max_holdout_half"), ("rho_nl^max (holdout, all shells)", "rho_nl_max_holdout"), ("single-sphere rho_u max", "sphere_rho_u_max"),
           ("rho_lin^max (holdout)", "rho_lin_max_holdout"), ("sigma_u^max std / half", ("sigma_u_max", "sigma_u_max_half")), ("sigma_u^max core sets", "sigma_u_max_core"), ("sigma_Om", "sigma_Om"), ("holdout rho_Om^max (vorticity ratio)", "rho_Om_max_holdout"), ("a_max std / half", ("a_max", "a_max_half")),
           ("a_max core sets", "a_max_core"), ("a_eff (core resolved)", ("a_eff", "core_resolved")), ("strain ratio at located max", "located_strain_ratio"), ("gradient scale", None), ("tau_F (2^8 R0)", "tau_F_R8"), ("delta_G core / max", ("delta_G_core", "delta_G_max")),
           ("sampled Q_sw", "Q_sw"), ("e_core (holdout) / e_F", ("e_core_holdout", "e_F")), ("N_core / N_F", ("N_core", "N_F")), ("E_ren", "E_ren"), ("max E_F (radius)", ("E_F_max", "r_at_E_F_max")), ("H_tot / int|h|", "H_tot_over_abs"), ("H_tot", "H_tot"), ("core alignment", "core_alignment"),
           ("K_E ratio (carried/required)", "K_ratio_direct"), ("K_H ratio", "K_H_ratio_direct"), ("carried mismatch m", "G_carried_mismatch_rel"), ("G defect F-comp / parallel frac", ("G_defect_F_component", "G_defect_parallel_fraction")), ("kappa finite radius", "kappa_far_finite_radius"),
           ("radial-lambda share", "radial_lambda_share"), ("f_sw tail", "f_sw_tail"), ("tau_0/1/2 floored", ("tau0_floored", "tau1_floored", "tau2_floored")), ("max|U| / max|Omega|", ("max_U", "max_abs_Omega")), ("rotation content", "rotation_content_rel"),
           ("V10 last-tenth decrease", "v10_last_tenth_rel_decrease"), ("terminal LM cost (cost_after_reweight)", "cost_final"), ("rms_mom (unnormalized weighted training momentum RMS)", "rms_mom"),
           ("iterations / status / seconds", ("iterations", "status", "seconds")), ("c_l / omega", ("c_l", "omega"))]
out_all = {}
for j in sys.argv[1:]:
    if j == "--json": continue
    rs = by_job.get(j)
    if not rs:
        print(f"## {j}: no start_result row (job not finished or failed)"); continue
    r = rs[-1]; jj, where = job_json(j); src = None; src_id = None
    if jj and jj.get("config", {}).get("init_from"):
        zrel = os.path.relpath(jj["config"]["init_from"], ROOT); src = by_zfile.get(zrel); src_id = zrel.split("/")[1] if "/" in zrel else zrel
    cfg = (jj or {}).get("config", {})
    print(f"## {j} (queue/{where}; start {r.get('start')}; ts {r.get('ts')}; GPU {r.get('gpu')}; L {r.get('L')} Nk {r.get('Nk')} {r.get('m_parity')} {r.get('formulation')} {r.get('nl_denominator')}; channels {cfg.get('channels')}; closure {cfg.get('closure_lambda')}; "
          f"extra cfg: " + ", ".join(f"{k}={cfg[k]}" for k in ("omega", "c_l", "both_weight", "radial_lambda_w", "balance_lambda", "nu", "core_pin", "nonaxi_pin", "boost_e_core", "perturb_m", "perturb_m_rel", "fsw") if cfg.get(k) is not None) + ")")
    print(f"source: {src_id} (ledger row {'found' if src else 'NOT found'}; meta source holdout {f(r.get('source_rho_u'))} / {f(r.get('source_rho_u_half'))})")
    print("| metric | start | end | end/start |"); print("|---|---|---|---|")
    rec = {}
    for name, key in METRICS:
        if key is None: continue
        keys = key if isinstance(key, tuple) else (key,)
        e = " / ".join(f(r.get(k)) for k in keys); s_ = " / ".join(f(src.get(k)) for k in keys) if src else "n/a"
        ratio = ""
        if len(keys) == 1 and src and isinstance(r.get(key), (int, float)) and isinstance(src.get(key), (int, float)) and src.get(key) not in (0, None) and not isinstance(r.get(key), bool):
            ratio = "%.3f" % (r[key] / src[key])
        elif len(keys) == 2 and src and all(isinstance(r.get(k), (int, float)) and isinstance(src.get(k), (int, float)) and not isinstance(r.get(k), bool) and src.get(k) for k in keys):
            ratio = " / ".join("%.3f" % (r[k] / src[k]) for k in keys)
        print(f"| {name} | {s_} | {e} | {ratio} |"); rec[name] = dict(start=[src.get(k) for k in keys] if src else None, end=[r.get(k) for k in keys])
    bm = r.get("battery_memory") or []
    if bm:
        pk = max(bm, key=lambda x: x.get("peak_GB", 0)); print(f"battery memory: heaviest item '{pk['item']}' {pk['peak_GB']} GB; items: " + ", ".join(f"{x['item']} {x['peak_GB']}" for x in bm))
    cv = r.get("code_versions") or {}
    print("code versions: " + ", ".join(f"{os.path.basename(k)} {v.get('sha256_12')}" for k, v in cv.items()) if cv else "code versions: n/a")
    print(f"zfile: {r.get('zfile')}; failure flag: {r.get('failure')}; tier S holdout std/half: {f(r.get('tier_S_holdout'))} / {f(r.get('tier_S_holdout_half'))}\n")
    out_all[j] = dict(row=r, source_job=src_id, source_row=src, metrics=rec)
if "--json" in sys.argv:
    for j, v in out_all.items():
        fn = os.path.join(ROOT, "reports", f"arm_reading_{j}.json"); json.dump(v, open(fn, "w"), indent=1, default=str); print("written", fn)
