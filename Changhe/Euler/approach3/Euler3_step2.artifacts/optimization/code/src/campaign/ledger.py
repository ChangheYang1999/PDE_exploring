"""Append-only JSONL ledger with file locking, plus leaderboard helpers."""
from __future__ import annotations
import json, os, fcntl, time, hashlib


def append(path, record):
    record = dict(record); record.setdefault("ts", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    line = json.dumps(record, sort_keys=True) + "\n"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.write(line); f.flush(); os.fsync(f.fileno())
        fcntl.flock(f, fcntl.LOCK_UN)


def read(path):
    out = []
    if not os.path.exists(path):
        return out
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return out


def is_disposable(job_id):
    """Smoke jobs (3-iteration memory/time tests, 'smoke' anywhere in the id), resume tests and LM-only validation runs are never ranked
    (2026-10-25T20:20Z: the earlier startswith('smoke') filter missed nest8nk8smoke, nest10smoke_*, s10smoke, s9dsmoke)."""
    j = str(job_id or "")
    return ("smoke" in j) or j.startswith("resume_test") or ("lmonly" in j) or j.startswith(("val8", "wtest"))


def leaderboard(records, key="rank_key", n=20, require_nontrivial=True, solver_version="latest"):
    """Ranked start results. solver_version: 'latest' (rows of the newest solver_version only, SPEC note 18:54Z item 3),
    'all', or an explicit tag. Rows without the field count as version v1 (plain LS) / v2 (gauge_version 2 without tag)."""
    rows = []
    def ver(r):
        return r.get("solver_version") or ("v2-untagged" if r.get("gauge_version") == 2 else "v1")
    all_rows = [r for r in records if r.get("kind") == "start_result"]
    if solver_version == "latest":
        tags = sorted(set(ver(r) for r in all_rows))
        dated = [t for t in tags if "-" in t and t.split("-", 1)[1][:2] == "20"]        # tags are v<k>-<date>; the newest date wins (v3 was wrongly pinned before 2026-10-24T23:05Z); 2026-10-25T21:52Z: "v2-untagged" is not a dated tag (it sorted after every date and made status.py show the 18:53-19:09Z gauge-2 rows as "latest")
        solver_version = max(dated, key=lambda t: t.split("-", 1)[1]) if dated else (tags[-1] if tags else None)
    for r in records:
        if r.get("kind") != "start_result":
            continue
        if solver_version not in (None, "all") and ver(r) != solver_version:
            continue
        r = dict(r)
        if "lm_rms_per_entry" not in r:      # early records stored the per-entry LM rms; use the weighted RMS
            r["lm_rms_per_entry"] = r.get("rms_final"); r["rms_final"] = r.get("rms_vort", r.get("rms_mom", r.get("rms_final")))
        # ranking key (SPEC 7.3): rho_u_max when available, else the weighted RMS (early records)
        r["rank_key"] = r.get("rho_u_max_holdout") if r.get("rho_u_max_holdout") is not None else (r.get("rho_u_max") if r.get("rho_u_max") is not None else r.get("rms_final"))
        if r.get(key) is not None:
            rows.append(r)
    rows = [r for r in rows if not is_disposable(r.get("job_id"))]      # disposable test jobs (smokes anywhere in the id, resume tests, LM-only validations)
    if require_nontrivial:
        rows = [r for r in rows if r.get("max_abs_Omega", 0) > 1e-6 and r.get("rotation_content_rel", 0) > 1e-3 and not r.get("failure")
                and (r.get("max_U") is None or r.get("max_U") > 1e-6) and (r.get("gauge_defect") is None or r.get("gauge_defect") <= 1e-3)]
    rows.sort(key=lambda r: r[key])
    return rows[:n]


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def merge_reevaluations(records):
    """Fill rho_u_max_holdout_half, rho_nl_max_holdout_half, sphere_rho_u_max, sphere_r_at_max (and *_both) of start_result rows that
    predate the two-family worker code from the newest 'reevaluation' record with the same zfile. Returns the (copied) start rows."""
    latest = {}
    for r in records:
        if r.get("kind") == "reevaluation" and isinstance(r.get("new"), dict) and r["new"].get("rho_u_max_half") is not None:
            latest[r.get("zfile")] = r
    out = []
    for r in records:
        if r.get("kind") != "start_result":
            continue
        r = dict(r)
        rv = latest.get(r.get("zfile"))
        if rv is not None:                      # fill every missing key from the newest re-evaluation (since 2026-10-25T05:05Z: also rows that already had the two-family fields)
            n = rv["new"]
            MAP = dict(rho_u_max_half="rho_u_max_holdout_half", rho_u_max_both="rho_u_max_holdout_both", rho_nl_max_half="rho_nl_max_holdout_half", rho_nl_max_both="rho_nl_max_holdout_both",
                       sphere_rho_u_max="sphere_rho_u_max", sphere_r_at_max="sphere_r_at_max", sphere_rho_nl_max="sphere_rho_nl_max",
                       rho_lin_max_std="rho_lin_max_holdout", rho_lin_max_half="rho_lin_max_holdout_half", rho_sp_max_std="rho_sp_max_holdout", rho_sp_max_half="rho_sp_max_holdout_half",
                       rho_lin_max_r1_std="rho_lin_max_r1_holdout", rho_sp_max_r1_std="rho_sp_max_r1_holdout", d30_Ru_over_T1_r1="d30_Ru_over_T1_r1", d30_ROm_over_Om="d30_ROm_over_Om",
                       sigma_u_max_std="sigma_u_max", sigma_u_max_shell_std="sigma_u_max_shell", sigma_u_max_half="sigma_u_max_half", sigma_u_max_r1_std="sigma_u_max_r1", sigma_Om="sigma_Om",
                       a_max_std="a_max", a_max_shell_std="a_max_shell", a_max_half="a_max_half", origin_U_rms="origin_U_rms", origin_B="origin_B", origin_L="origin_L", gram_check_max="gram_check_max",
                       structure="structure", peak_max_std="peak_max_holdout", tau_F_R8="tau_F_R8", tau_F_R12="tau_F_R12", delta_G_core="delta_G_core", delta_G_max="delta_G_max", tau_F_by_m="tau_F_by_m",
                       Q_sw="Q_sw", Gamma0_max="Gamma0_max", S_max="S_max", E_swirl_max="E_swirl_max", swirl_identity_closure="swirl_identity_closure",
                       tau0_floored="tau0_floored", tau1_floored="tau1_floored", tau2_floored="tau2_floored", taylor_consistency="taylor_consistency",
                       a_eff="a_eff", y_star="y_star", r_star="r_star", core_ball_over_a_eff="core_ball_over_a_eff", sigma_u_ball_half="sigma_u_ball_half", sigma_u_ball_quarter="sigma_u_ball_quarter",
                       a_max_ball_half_centre="a_max_ball_half_centre", a_max_ball_half_upper="a_max_ball_half_upper", a_max_ball_quarter_centre="a_max_ball_quarter_centre",
                       a_max_ball_quarter_upper="a_max_ball_quarter_upper", sigma_Om_ball_half="sigma_Om_ball_half", inner_sigma_u_max="inner_sigma_u_max", inner_a_max="inner_a_max",
                       core_resolved="core_resolved", core_doubling_change_max="core_doubling_change_max", sigma_u_max_core="sigma_u_max_core", a_max_core="a_max_core", a_max_core_upper="a_max_core_upper",
                       E_ren="E_ren", H_tot="H_tot", H_abs="H_abs", H_tot_over_abs="H_tot_over_abs", core_alignment="core_alignment", E_ren_change_2oct="E_ren_change_2oct", H_tot_change_2oct="H_tot_change_2oct",
                       E_F_max="E_F_max", r_at_E_F_max="r_at_E_F_max", E_F_weighted_excess="E_F_weighted_excess", E_F_weighted_deficit="E_F_weighted_deficit", E_ren_two_forms_rel_diff="E_ren_two_forms_rel_diff", H_F_sign_change_radii="H_F_sign_change_radii", kappa_far_finite_radius="kappa_far_finite_radius", Phi_F_far_finite_radius="Phi_F_far_finite_radius",
                       K_ratio_direct="K_ratio_direct", carried_mismatch_rel="G_carried_mismatch_rel", carried_correlation="G_carried_correlation", K_H_required="K_H_required", K_H_carried="K_H_carried",
                       K_H_ratio_direct="K_H_ratio_direct", K_H_identity_rel_closure="K_H_identity_rel_closure", G_defect_F_component="G_defect_F_component", G_defect_cos_F="G_defect_cos_F",
                       G_defect_parallel_fraction="G_defect_parallel_fraction", G_defect_parallel_rel="G_defect_parallel_rel", G_defect_orth_rel="G_defect_orth_rel", d84_bound_energy_ratio="d84_bound_energy_ratio", H_F_tail="H_F_tail")
            for k, v in MAP.items():
                if n.get(k) is not None and r.get(v) is None:
                    r[v] = n[k]
            r["two_family_source"] = "reevaluation " + str(rv.get("ts", ""))
            if r.get("rho_u_max_holdout") is None and n.get("rho_u_max") is not None:
                r["rho_u_max_holdout"] = n["rho_u_max"]; r["rho_nl_max_holdout"] = n.get("rho_nl_max")
        out.append(r)
    return out
