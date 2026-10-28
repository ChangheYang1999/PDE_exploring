"""VT-5 reading helper (lead QD item 3): compare the numbers of the clean-process validation run (validate_candidate.py --full JSON)
with the SAVED nest10 values, naming the source of every saved value. Read-only on every input; writes one markdown table and one JSON
next to the VT output. Nothing here is a threshold or a verdict: a match shows that the saved diagnostics reproduce from a clean process.
Usage: compare_vt_nest10.py <vt_json> <out_md> <out_json>
Saved sources: (S1) runs/nest10_L10_cl0.45_om+1.0_fixed_p0/results.jsonl, the start 0 row written by the worker at 2026-10-26T14:23:30Z;
(S2) status/ledger.jsonl, the start_result row of the same job and start (checked equal to S1 on every compared key);
(S3) candidates/nest10_L10_cl0.45_om1.0_p0/meta.json 'diagnostics' (the SPEC 10 export), where a key of the same name exists.
The mapping saved key -> validation JSON path is the worker's own mapping (scripts/worker.py lines 765 to 790 of v2.4 2edbd00c)."""
import sys, json, math, os
ROOT = os.environ.get("CAMPAIGN_ROOT", os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))  # campaign root; default: the published artifacts folder (runs/ is not included there)
vt_path, out_md, out_json = sys.argv[1:4]
VT = json.load(open(vt_path))
JOB = "nest10_L10_cl0.45_om+1.0_fixed_p0"
S1 = [json.loads(l) for l in open(f"{ROOT}/runs/{JOB}/results.jsonl")]
S1 = [r for r in S1 if r.get("start", 0) == 0][-1]
S2 = None
for l in open(f"{ROOT}/status/ledger.jsonl"):
    if JOB in l and '"start_result"' in l:
        d = json.loads(l)
        if d.get("job_id") == JOB and d.get("start", 0) == 0: S2 = d
S3 = (json.load(open(f"{ROOT}/candidates/nest10_L10_cl0.45_om1.0_p0/meta.json")).get("diagnostics") or {})
def get(d, path):
    cur = d
    for p in path:
        if isinstance(cur, dict) and p in cur: cur = cur[p]
        elif isinstance(cur, (list, tuple)) and isinstance(p, int) and len(cur) > p: cur = cur[p]
        else: return None
    return cur
sd, sdh = ("spec_training",), ("spec_holdout",)
MAP = {}
for k in ["rho_u_max", "rho_u_bal", "rho_nl_max", "pi_u_max", "rho_Om_max", "A_u", "A_Om"]: MAP[k] = sd + ("global_", k)
for k in ["N_core", "e_core", "N_F", "e_F"]: MAP[k] = sd + ("nonaxi", k)
MAP.update(r_core=sd + ("guards", "N4_r_core"), r_tail=sd + ("guards", "N5_r_tail"), max_U=sd + ("guards", "N4_max_U"), lambda_max_S=sd + ("guards", "N2_lambda_max_S"))
for k in ["rho_u_max", "rho_u_bal", "rho_nl_max", "pi_u_max", "rho_Om_max", "A_u"]: MAP[k + "_holdout"] = sdh + ("global_", k)
for k in ["N_core", "e_core"]: MAP[k + "_holdout"] = sdh + ("nonaxi", k)
MAP.update(r_core_holdout=sdh + ("guards", "N4_r_core"), r_tail_holdout=sdh + ("guards", "N5_r_tail"), pressure_ray_check=sdh + ("pressure", "ray_check", "max_rel_diff"),
           tier_S_holdout=("tier_S_holdout", 0), tier_S_holdout_half=("tier_S_holdout_half", 0))
tf = ("two_family",)
for saved, key in [("rho_u_max_holdout_half", "rho_u_max_half"), ("rho_u_max_holdout_both", "rho_u_max_both"), ("rho_nl_max_holdout_half", "rho_nl_max_half"), ("rho_nl_max_holdout_both", "rho_nl_max_both"),
                   ("sphere_rho_u_max", "sphere_rho_u_max"), ("sphere_r_at_max", "sphere_r_at_max"), ("sphere_rho_nl_max", "sphere_rho_nl_max"), ("sphere_r_at_nl_max", "sphere_r_at_nl_max"),
                   ("rho_lin_max_holdout", "rho_lin_max_std"), ("rho_lin_max_holdout_half", "rho_lin_max_half"), ("rho_sp_max_holdout", "rho_sp_max_std"), ("rho_sp_max_holdout_half", "rho_sp_max_half"),
                   ("rho_lin_max_r1_holdout", "rho_lin_max_r1_std"), ("rho_sp_max_r1_holdout", "rho_sp_max_r1_std"), ("d30_Ru_over_T1_r1", "d30_Ru_over_T1_r1"), ("d30_ROm_over_Om", "d30_ROm_over_Om"),
                   ("gram_check_max", "gram_check_max"), ("sigma_u_max", "sigma_u_max_std"), ("sigma_u_max_shell", "sigma_u_max_shell_std"), ("sigma_u_max_half", "sigma_u_max_half"), ("sigma_u_max_r1", "sigma_u_max_r1_std"),
                   ("sigma_Om", "sigma_Om"), ("a_max", "a_max_std"), ("a_max_half", "a_max_half"), ("origin_U_rms", "origin_U_rms"), ("origin_B", "origin_B"), ("origin_L", "origin_L"), ("peak_max_holdout", "peak_max_std"),
                   ("gram_gamma_shells", "gram_gamma_std"), ("gram_a_shells", "gram_a_std"), ("gram_b_shells", "gram_b_std")]:
    MAP[saved] = tf + (key,)
gc = ("G_closure",)
for saved, key in [("G_norm", "G_norm"), ("G_closure_rel", "dist_rel"), ("G_span_rank", "rank"), ("G_span_columns", "n_columns"), ("G_carried_mismatch_rel", "carried_mismatch_rel"), ("G_carried_correlation", "carried_correlation"),
                   ("G_carried_norm", "G_carried_norm"), ("K_ratio_direct", "K_ratio_direct"), ("K_H_required", "K_H_required"), ("K_H_carried", "K_H_carried"), ("K_H_ratio_direct", "K_H_ratio_direct"),
                   ("K_H_identity_rel_closure", "K_H_identity_rel_closure"), ("G_defect_F_component", "G_defect_F_component"), ("G_defect_cos_F", "G_defect_cos_F"), ("G_defect_parallel_fraction", "G_defect_parallel_fraction"),
                   ("d84_bound_energy_ratio", "d84_bound_energy_ratio")]:
    MAP[saved] = gc + (key,)
st = ("strength",)
for k in ["R_trap", "lambda_max_S_inside_Rtrap", "B_u", "KU_ratio", "KOmega_L2_ratio"]: MAP[k] = st + (k,)
def num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)
def flat(x):
    if num(x): return [float(x)]
    if isinstance(x, (list, tuple)): return [v for e in x for v in flat(e)]
    return None
rows, n_match, n_diff, n_missing_vt, n_missing_saved = [], 0, 0, 0, 0
for saved_key, path in MAP.items():
    v_vt = get(VT, path); v1 = S1.get(saved_key); v2 = S2.get(saved_key) if S2 else None; v3 = S3.get(saved_key)
    src = []
    if saved_key in S1: src.append("S1")
    if S2 and saved_key in S2: src.append("S2" + ("" if v2 == v1 else " (DIFFERS from S1)"))
    if saved_key in S3: src.append("S3" + ("" if v3 == v1 else " (DIFFERS from S1)"))
    if v_vt is None and v1 is None: continue
    if v_vt is None:
        n_missing_vt += 1; rows.append((saved_key, "/".join(str(p) for p in path), "MISSING in the VT output", repr(v1)[:40], ", ".join(src), "n/a", "saved only")); continue
    if v1 is None:
        n_missing_saved += 1; rows.append((saved_key, "/".join(str(p) for p in path), repr(v_vt)[:40], "no saved counterpart", "", "n/a", "NEW, unreviewed")); continue
    a, b = flat(v_vt), flat(v1)
    if a is None or b is None or len(a) != len(b):
        same = (v_vt == v1); rows.append((saved_key, "/".join(str(p) for p in path), repr(v_vt)[:40], repr(v1)[:40], ", ".join(src), "n/a", "equal" if same else "DIFFERENT (non-numeric or shape)")); n_match += same; n_diff += (not same); continue
    rel = max((abs(x - y) / max(abs(x), abs(y), 1e-300)) for x, y in zip(a, b)) if a else 0.0
    verdict = "equal" if rel == 0.0 else ("agree to rounding (rel <= 1e-12)" if rel <= 1e-12 else ("close (rel <= 1e-6)" if rel <= 1e-6 else "DIFFERENT (rel > 1e-6)"))
    n_match += rel <= 1e-6; n_diff += rel > 1e-6
    fmt = lambda v: (f"{v:.10g}" if num(v) else repr(v)[:40])
    rows.append((saved_key, "/".join(str(p) for p in path), fmt(v_vt), fmt(v1), ", ".join(src), f"{rel:.2e}", verdict))
new_sections = [k for k in ("training_grid", "refined_grid", "holdout", "X5_vorticity", "orbit_averages", "orbit_checks_7_14", "critical") if k in VT]
L = [f"# VT-5 reading: clean-process validation of {JOB} start 0 against the saved values (helper compare_vt_nest10.py; written {__import__('time').strftime('%Y-%m-%dT%H:%M:%SZ', __import__('time').gmtime())})", "",
     "Saved sources: S1 runs/.../results.jsonl (worker row 2026-10-26T14:23:30Z); S2 status/ledger.jsonl start_result row; S3 candidates/nest10_L10_cl0.45_om1.0_p0/meta.json diagnostics. 'equal' is bitwise; 'agree to rounding' rel <= 1e-12; 'close' rel <= 1e-6; anything above 1e-6 is listed as DIFFERENT and is read by hand. A match reproduces saved diagnostics from a clean process; it is not new evidence about the state.", "",
     f"Summary: {len(rows)} compared keys; {n_match} within 1e-6 relative; {n_diff} different; {n_missing_vt} saved keys missing in the VT output; {n_missing_saved} VT values without a saved counterpart (new, unreviewed).", "",
     "| saved key | VT JSON path | VT value | saved value | saved sources | max rel diff | verdict |", "|---|---|---|---|---|---|---|"]
for r in rows: L.append("| " + " | ".join(r) + " |")
L += ["", "## VT output sections without a saved counterpart (new, unreviewed; not compared): " + ", ".join(new_sections) + ".",
      "- critical.local_maxima[0] (abs_Omega, r, strain_ratio, transport_ratio) is compared BY HAND with the worker's CRITICAL stdout line of 2026-10-26T13:58:28Z (located |Omega| max 13.4820 at r=0.264, strain ratio 0.9114, transport 2.9e-10); the values are printed below.",
      "- VT critical.local_maxima[0]: " + json.dumps({k: get(VT, ("critical", "local_maxima", 0, k)) for k in ("abs_Omega", "r", "strain_ratio", "transport_ratio", "lambda_max_S")}),
      "- VT holdout random points (4003): " + json.dumps({k: get(VT, ("holdout", k)) for k in ("rms_scaled_R_Omega", "max_scaled_R_Omega", "rms_scaled_Omega")}),
      "- Not computed by the validation script and therefore not compared: V10 (an optimizer-history quantity), the LM cost, the SPECTRUM, RADIAL LAMBDA and ORIGIN battery lines, the core-set a_max variants, E_ren / H_tot balances (BALANCE line), FAR RATE, RAY by |m|."]
open(out_md, "w").write("\n".join(L) + "\n")
json.dump(dict(rows=[dict(zip(("saved_key", "vt_path", "vt_value", "saved_value", "sources", "max_rel_diff", "verdict"), r)) for r in rows], n_match=n_match, n_diff=n_diff, n_missing_vt=n_missing_vt, n_new=n_missing_saved, new_sections=new_sections), open(out_json, "w"), indent=1)
print(L[4]); print("wrote", out_md, out_json)
