#!/usr/bin/env python
"""Write reports/PARAMETER_SWEEP.csv (every start) and reports/CANDIDATE_LEADERBOARD.csv (ranked by the SPEC 7.3 key:
rho_u_max, then rho_nl_max) from the ledger."""
import sys, os, csv, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
from src.campaign import ledger
recs = ledger.read(os.path.join(ROOT, "status", "ledger.jsonl"))
rows = [r for r in ledger.merge_reevaluations(recs) if not ledger.is_disposable(r.get("job_id"))]
cols = ["ts", "job_id", "start", "family", "c_l", "omega", "L", "Nk", "m_parity", "formulation", "optimizer", "nl_weighting", "efrac", "status", "iterations", "seconds", "gpu",
        "rms0", "rms_final", "rho_u_max_holdout", "rho_u_max_holdout_half", "rho_u_max_holdout_both", "rho_nl_max_holdout", "rho_nl_max_holdout_half",
        "sphere_rho_u_max", "sphere_r_at_max", "pi_u_max_holdout", "N_core_holdout", "e_core_holdout", "tier_S_holdout", "tier_S_holdout_half",
        "source_rho_u", "max_U_start", "nl_denominator", "tail_constraints", "two_family_source",
        "sigma_u_max", "sigma_u_max_shell", "sigma_u_max_half", "sigma_u_max_r1", "sigma_Om", "a_max", "a_max_shell", "a_max_half", "rho_lin_max_holdout", "rho_sp_max_holdout",
        "rho_sp_max_r1_holdout", "origin_U_rms", "origin_B", "origin_L", "G_closure_rel", "G_carried_mismatch_rel", "G_carried_correlation", "v10_last_tenth_rel_decrease", "channels", "L_ext",
        "rho_u_max", "rho_u_bal", "rho_nl_max", "pi_u_max", "rho_Om_max", "A_u", "A_Om", "N_core", "e_core", "N_F", "e_F", "r_core", "r_tail", "max_U",
        "max_abs_Omega", "lambda_max_S", "strain_at_max", "rotation_content_rel", "tail_nonaxi", "top_k_fraction", "top_l_fraction", "tier_S", "zfile"]
os.makedirs(os.path.join(ROOT, "reports"), exist_ok=True)
with open(os.path.join(ROOT, "reports", "PARAMETER_SWEEP.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore"); w.writeheader()
    for r in sorted(rows, key=lambda r: r.get("ts", "")):
        w.writerow({k: r.get(k) for k in cols})
def key(r):
    return r["rho_u_max_holdout"] if r.get("rho_u_max_holdout") is not None else r["rho_u_max"]
def excluded(r):
    if r.get("failure"): return r["failure"]
    if r.get("max_U") is not None and r["max_U"] < 1e-6: return "max_U<1e-6"
    if r.get("gauge_defect") is not None and r["gauge_defect"] > 1e-3: return "gauge_defect>1e-3"
    if r.get("max_abs_Omega", 0) <= 1e-6: return "no_vorticity"
    if r.get("rotation_content_rel", 0) <= 1e-3 or (r.get("e_F") is not None and r["e_F"] < 1e-4): return "axisymmetric"
    if str(r.get("job_id", "")).endswith("_free") or "_free_" in str(r.get("job_id", "")): return "free_params_unranked_until_fixed_evaluation"
    return ""
cols = cols + ["excluded_reason", "solver_version", "gauge_version", "gauge_defect", "Sigma_Z", "located_strain_ratio", "rho_u_max_holdout"]
cols = list(dict.fromkeys(cols))
for r in rows:
    r["excluded_reason"] = excluded(r)
ranked = [r for r in rows if r.get("rho_u_max") is not None and not r["excluded_reason"]]
ranked.sort(key=lambda r: (key(r), r.get("rho_nl_max_holdout") or r.get("rho_nl_max") or 1e300))
with open(os.path.join(ROOT, "reports", "CANDIDATE_LEADERBOARD.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["rank"] + cols, extrasaction="ignore"); w.writeheader()
    for i, r in enumerate(ranked):
        d = {k: r.get(k) for k in cols}; d["rank"] = i + 1; w.writerow(d)
print(f"{len(rows)} starts written; {len(ranked)} ranked (nontrivial, not failed); excluded: {sum(1 for r in rows if r['excluded_reason'])}; best ranked rho_u_max {key(ranked[0]) if ranked else None}")
if ranked:
    print("top 5 by rho_u_max:")
    for r in ranked[:5]:
        def f(v, fmt="%.3e"):
            return (fmt % v) if isinstance(v, (int, float)) else "n/a"
        print(f"  holdout rho_u std={f(r.get('rho_u_max_holdout'))} half={f(r.get('rho_u_max_holdout_half'))} sphere={f(r.get('sphere_rho_u_max'))} rho_nl(all shells)={f(r.get('rho_nl_max_holdout'))} {r['job_id']}/{r['start']} {r['family']} c_l={r['c_l']} om={r['omega']} nl_den={r.get('nl_denominator')} e_F={f(r.get('e_F'), '%.2f')} maxU={f(r.get('max_U'))} tierS={r.get('tier_S_holdout')}")
    print("ranking key: holdout rho_u^max on the standard family (SPEC 7.3); SPEC 7.3a: an ordering claim needs the same order on the half-offset family (column rho_u_max_holdout_half); 'both' = max of the two families.")
    print("SPEC v1.20 7.3b: X ranks ahead of Y only if X is lower on both families and X's sigma_u_max, sigma_Om and a_max each exceed Y's by at most 10 per cent; a missing value makes the pair not ordered (columns sigma_u_max, sigma_Om, a_max).")
