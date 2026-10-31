#!/usr/bin/env python
"""S14 stage (i) reading (reports/S14_ENQUEUE_20261026.md, lead d128 HE item 5): per start of one S14 job, the holdout rho_u^max on both shell
families, the SPEC 7.4 guards used as the R10 (e) guards (N_core >= 1e-2, N_F >= 1e-2, e_core >= 1e-4, e_F >= 1e-4; no failure flag; max|Omega| > 1e-6
and rotation content > 1e-3 as in promote_nest.py), the odd-m fractions in amplitude and energy (reports/oddm/oddm_<job>_<k>.json written by
scripts/odd_m_fraction.py), V10, the LM status and seconds, and the promotion decision fixed before the data: the lowest holdout (the larger of the two
families; ties by the standard family) among the starts that pass the guards and keep an odd-m energy fraction (all radii) >= 1e-2; none qualifying =
'fresh all-m starts at L4 failed the guards or lost their odd-m content'. Whole-job seconds from the stdout.log START and JOB DONE stamps; bytes
written = du -sb runs/<job>. CPU only; reads saved files. Usage: .venv/bin/python scripts/s14_reading.py <job_id> [--json]"""
import sys, os, json, re, subprocess, argparse, datetime
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ap = argparse.ArgumentParser(); ap.add_argument("job"); ap.add_argument("--json", action="store_true"); a = ap.parse_args()
job = a.job; rdir = os.path.join(ROOT, "runs", job)
rows = [json.loads(l) for l in open(os.path.join(rdir, "results.jsonl")) if l.strip()]
rows = [r for r in rows if r.get("kind") == "start_result"]
def ts(s):
    return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")
log = open(os.path.join(rdir, "stdout.log")).read().splitlines()
t_start = next((ts(l[:20]) for l in log if " START job " in l), None)
t_done = next((ts(l[:20]) for l in log if "JOB DONE" in l), None)
whole = (t_done - t_start).total_seconds() if (t_start and t_done) else None
nbytes = int(subprocess.run(["du", "-sb", rdir], capture_output=True, text=True).stdout.split()[0])
GU = dict(N_core=1e-2, N_F=1e-2, e_core=1e-4, e_F=1e-4)
out = []
for r in sorted(rows, key=lambda r: r["start"]):
    k = r["start"]
    om = os.path.join(ROOT, "reports", "oddm", f"oddm_{job}_{k}.json")
    od = json.load(open(om)) if os.path.exists(om) else None
    g = {n: (r.get(n) is not None and r[n] >= GU[n]) for n in GU}
    g["no_failure"] = not r.get("failure"); g["nontrivial"] = (r.get("max_abs_Omega", 0) > 1e-6) and (r.get("rotation_content_rel", 0) > 1e-3)
    passes = all(g.values())
    std, half = r.get("rho_u_max_holdout"), r.get("rho_u_max_holdout_half")
    key = max(v for v in (std, half) if v is not None) if std is not None else None
    e_odd = od["energy_fraction_odd"]["all"] if od else None
    cv = r.get("code_versions") or {}
    out.append(dict(start=k, family=r.get("family"), rng_seed=r.get("rng_seed"), status=r.get("status"), iterations=r.get("iterations"), lm_seconds=r.get("seconds"),
                    holdout_std=std, holdout_half=half, holdout_key=key, rho_nl_max_holdout=r.get("rho_nl_max_holdout"), rms_mom=r.get("rms_mom"), cost_final=r.get("cost_final"),
                    v10=r.get("v10_last_tenth_rel_decrease"), e_core=r.get("e_core"), N_core=r.get("N_core"), e_F=r.get("e_F"), N_F=r.get("N_F"), guards=g, guards_pass=passes,
                    odd_energy_all=e_odd, odd_energy_core=(od["energy_fraction_odd"]["core_r_lt_0p125"] if od else None), odd_energy_tail=(od["energy_fraction_odd"]["tail_r_ge_8"] if od else None),
                    odd_amp_U=(od["ratio_all"]["U"] if od else None), odd_amp_Omega=(od["ratio_all"]["Omega"] if od else None), odd_amp_DU=(od["ratio_all"]["DU"] if od else None),
                    odd_coef_norm_fraction=(od["coef_norm_fraction_odd"] if od else None), max_U=r.get("max_U"), max_abs_Omega=r.get("max_abs_Omega"), r_core=r.get("r_core_holdout") or r.get("r_core"),
                    r_tail=r.get("r_tail_holdout") or r.get("r_tail"), core_resolved=r.get("core_resolved"), a_max_core=r.get("a_max_core"), sigma_u_max_core=r.get("sigma_u_max_core"), sigma_Om=r.get("sigma_Om"),
                    E_ren=r.get("E_ren"), H_tot_over_abs=r.get("H_tot_over_abs"), Q_sw=r.get("Q_sw"), tau_F_R8=r.get("tau_F_R8"), K_E_ratio=r.get("K_ratio_direct"), K_H_ratio=r.get("K_H_ratio_direct"),
                    core_dominant_m=(r.get("structure") or {}).get("core_dominant_m"), tail_dominant_m=(r.get("structure") or {}).get("tail_dominant_m"), lambda_max_S=r.get("lambda_max_S"),
                    located_strain_ratio=r.get("located_strain_ratio"), zfile=r.get("zfile"), failure=r.get("failure"),
                    code_versions={k2: v.get("sha256_12") for k2, v in cv.items()} if isinstance(cv, dict) else cv, qualifies=(passes and e_odd is not None and e_odd >= 1e-2 and key is not None)))
qual = [o for o in out if o["qualifies"]]
best = min(qual, key=lambda o: (o["holdout_key"], o["holdout_std"])) if qual else None
cfg = json.loads(re.search(r"cfg=(\{.*\})\s*$", next(l for l in log if " START job " in l)).group(1)) if any(" START job " in l for l in log) else {}
res = dict(job=job, c_l=cfg.get("c_l"), omega=cfg.get("omega"), n_starts_cfg=cfg.get("n_starts"), n_done=len(out), job_start=t_start.strftime("%Y-%m-%dT%H:%M:%SZ") if t_start else None,
           job_done=t_done.strftime("%Y-%m-%dT%H:%M:%SZ") if t_done else None, whole_job_seconds=whole, whole_job_gpu_hours=(whole / 3600.0 if whole else None), lm_seconds_total=sum((o["lm_seconds"] or 0) for o in out),
           bytes_written=nbytes, guards=GU, promotion=(dict(start=best["start"], family=best["family"], rng_seed=best["rng_seed"], holdout_std=best["holdout_std"], holdout_half=best["holdout_half"], odd_energy_all=best["odd_energy_all"], zfile=best["zfile"]) if best else None),
           promotion_reading=("promote start %d (%s)" % (best["start"], best["family"]) if best else "fresh all-m starts at L4 failed the guards or lost their odd-m content"), starts=out)
def f(v, fmt="%.4f"):
    return (fmt % v) if isinstance(v, (int, float)) and v is not None else "n/a"
print(f"# S14 stage (i) reading: {job} (c_l {res['c_l']}, omega {res['omega']}; {len(out)} of {res['n_starts_cfg']} starts; job {res['job_start']} -> {res['job_done']}, whole-job {f(whole, '%.0f')} s = {f(res['whole_job_gpu_hours'], '%.2f')} GPU-h, LM {res['lm_seconds_total']:.0f} s; {nbytes/1e6:.1f} MB written)")
print("| start | family | seed | status / its / LM s | holdout std / half | rho_nl^max | V10 | e_core / N_core / e_F / N_F | guards | odd energy all / core / tail | odd amp U / Omega / DU | max U / max Omega | r_core / r_tail | core resolved; core a_max / sigma_u / sigma_Om | E_ren; H_tot/int|h| | Q_sw; tau_F | K_E / K_H ratio | dom m core / tail | qualifies |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for o in out:
    print(f"| {o['start']} | {o['family']} | {o['rng_seed']} | {o['status']} / {o['iterations']} / {f(o['lm_seconds'], '%.0f')} | {f(o['holdout_std'])} / {f(o['holdout_half'])} | {f(o['rho_nl_max_holdout'], '%.3g')} | {f(o['v10'], '%.2e')} | {f(o['e_core'], '%.3g')} / {f(o['N_core'], '%.3g')} / {f(o['e_F'], '%.3g')} / {f(o['N_F'], '%.3g')} | {'pass' if o['guards_pass'] else 'FAIL ' + ','.join(k for k, v in o['guards'].items() if not v)} | {f(o['odd_energy_all'], '%.3f')} / {f(o['odd_energy_core'], '%.3f')} / {f(o['odd_energy_tail'], '%.3f')} | {f(o['odd_amp_U'], '%.3f')} / {f(o['odd_amp_Omega'], '%.3f')} / {f(o['odd_amp_DU'], '%.3f')} | {f(o['max_U'], '%.3f')} / {f(o['max_abs_Omega'], '%.3g')} | {f(o['r_core'], '%.3g')} / {f(o['r_tail'], '%.3g')} | {o['core_resolved']}; {f(o['a_max_core'], '%.3g')} / {f(o['sigma_u_max_core'], '%.3g')} / {f(o['sigma_Om'], '%.3g')} | {f(o['E_ren'], '%.3g')}; {f(o['H_tot_over_abs'], '%.3g')} | {f(o['Q_sw'], '%.3g')}; {f(o['tau_F_R8'], '%.3g')} | {f(o['K_E_ratio'], '%.3g')} / {f(o['K_H_ratio'], '%.3g')} | {o['core_dominant_m']} / {o['tail_dominant_m']} | {'yes' if o['qualifies'] else 'no'} |")
print(f"PROMOTION: {res['promotion_reading']}" + (f" holdout {f(best['holdout_std'])} / {f(best['holdout_half'])}, odd-m energy fraction {f(best['odd_energy_all'], '%.3f')}, file {best['zfile']}" if best else ""))
cvs = sorted({json.dumps(o['code_versions'], sort_keys=True) for o in out}); print("CODE VERSIONS: " + "; ".join(cvs))
if a.json:
    fn = os.path.join(ROOT, "reports", f"s14_reading_{job}.json"); json.dump(res, open(fn, "w"), indent=1); print("written", fn)
