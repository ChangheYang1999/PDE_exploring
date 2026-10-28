"""VT-5 reading helper, v2 (lead review of v1 fcf7306e, 2026-10-27T16:58:27Z, items R1 to R6): compare the numbers of the clean-process validation run
(validate_candidate.py --full JSON) with the SAVED nest10 values, naming the source of every saved value. Read-only on every input; writes one markdown
table and one JSON next to the VT output. Nothing here is a threshold or a verdict: a match shows that the saved diagnostics reproduce from a clean process.
Usage: compare_vt_nest10_v2.py <vt_json> <out_md> <out_json>
Saved sources: (S1) runs/nest10_L10_cl0.45_om+1.0_fixed_p0/results.jsonl, the start 0 row written by the worker at 2026-10-26T14:23:30Z;
(S2) status/ledger.jsonl, the start_result row of the same job and start (checked equal to S1 on every compared key);
(S3) candidates/nest10_L10_cl0.45_om1.0_p0/meta.json 'diagnostics' (the SPEC 10 export), where a key of the same name exists.
The mapping saved key -> validation JSON path is the worker's own mapping (scripts/worker.py lines 763 to 795 and 856 to 860 of v2.4 2edbd00c).
v2 changes against v1: R1 explicit non-finite handling and the row-count identity; R2 no silent skip ('absent in both' rows); R3 the nine extra
comparisons (critical maxima, W zeros, global integrals); R4 tier_S_holdout as 'definition differs (worker.py 679)'; R5 every numeric S1 key not
compared is listed, plus two_family.structure; R6 docstring citation and '|' escaping in table cells."""
import sys, json, math, os, time
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
# R3: the nine extra comparisons of worker.py 856 to 860 (critical maxima, W zeros) and the global integrals
MAP.update(located_max_abs_Omega=("critical", "local_maxima", 0, "abs_Omega"), located_max_r=("critical", "local_maxima", 0, "r"),
           located_strain_ratio=("critical", "local_maxima", 0, "strain_ratio"), located_transport_ratio=("critical", "local_maxima", 0, "transport_ratio"),
           n_W_zeros=("DERIVED", "n_W_zeros"), min_W_eigvec_defect=("DERIVED", "min_W_eigvec_defect"),
           Z=sd + ("global_integrals", "Z"), Sigma_Z=sd + ("global_integrals", "Sigma_Z"), F_norm2=sd + ("global_integrals", "F_norm2"))
def derived(name):
    wz = get(VT, ("critical", "W_zeros"))
    if wz is None: return None
    if name == "n_W_zeros": return len(wz)
    vals = [q.get("eigvec_defect") for q in wz if isinstance(q, dict) and q.get("eigvec_defect") is not None]
    return (min(vals) if vals else None) if wz else None
DEFINITIONAL = {"tier_S_holdout": "definition differs (worker.py 679 recomputes tier_S with located_lambda_max; validate_candidate.py does not)"}
def num(x): return isinstance(x, (int, float)) and not isinstance(x, bool)
def flat(x):
    if num(x): return [float(x)]
    if isinstance(x, (list, tuple)):
        out = []
        for e in x:
            f = flat(e)
            if f is None: return None
            out += f
        return out
    return None
def esc(s): return str(s).replace("|", "\\|")
def fmt(v): return f"{v:.10g}" if num(v) else repr(v)[:40]
rows = []; counts = dict(n_match=0, n_diff=0, n_missing_vt=0, n_new=0, n_definitional=0, n_absent_both=0)
for saved_key, path in MAP.items():
    v_vt = derived(saved_key) if path[0] == "DERIVED" else get(VT, path)
    in1, in2, in3 = (saved_key in S1), (S2 is not None and saved_key in S2), (saved_key in S3)
    v1 = S1.get(saved_key)
    src = []
    if in1: src.append("S1")
    if in2: src.append("S2" + ("" if S2.get(saved_key) == v1 else " (DIFFERS from S1)"))
    if in3: src.append("S3" + ("" if S3.get(saved_key) == v1 else " (DIFFERS from S1)"))
    pth = "/".join(str(p) for p in path)
    if saved_key in DEFINITIONAL:
        counts["n_definitional"] += 1; rows.append((saved_key, pth, fmt(v_vt) if v_vt is not None else "MISSING", fmt(v1) if in1 else "absent", ", ".join(src), "n/a", DEFINITIONAL[saved_key])); continue
    if v_vt is None and not in1:
        if in2 or in3:
            counts["n_missing_vt"] += 1; rows.append((saved_key, pth, "MISSING in the VT output", fmt((S2 or {}).get(saved_key, S3.get(saved_key))), ", ".join(src), "n/a", "saved only (S2/S3)")); continue
        counts["n_absent_both"] += 1; rows.append((saved_key, pth, "absent", "absent", "none", "n/a", "absent in both")); continue
    if v_vt is None:
        counts["n_missing_vt"] += 1; rows.append((saved_key, pth, "MISSING in the VT output", fmt(v1), ", ".join(src), "n/a", "saved only")); continue
    if not in1:
        counts["n_new"] += 1; rows.append((saved_key, pth, fmt(v_vt), "no saved counterpart", ", ".join(src), "n/a", "NEW, unreviewed")); continue
    a, b = flat(v_vt), flat(v1)
    if a is None or b is None or len(a) != len(b):
        same = (v_vt == v1); counts["n_match" if same else "n_diff"] += 1
        rows.append((saved_key, pth, fmt(v_vt), fmt(v1), ", ".join(src), "n/a", "equal" if same else "DIFFERENT (non-numeric or shape)")); continue
    nonfinite = [(x, y) for x, y in zip(a, b) if not (math.isfinite(x) and math.isfinite(y))]
    if nonfinite:
        ident = all((math.isnan(x) and math.isnan(y)) or (x == y) for x, y in nonfinite) and all((x == y) for x, y in zip(a, b) if math.isfinite(x) and math.isfinite(y))
        counts["n_match" if ident else "n_diff"] += 1
        rows.append((saved_key, pth, fmt(v_vt), fmt(v1), ", ".join(src), "non-finite", "equal (identical non-finite values)" if ident else "DIFFERENT (non-finite value on one side or unequal)")); continue
    rel = max([abs(x - y) / max(abs(x), abs(y), 1e-300) for x, y in zip(a, b)] or [0.0])
    verdict = "equal" if rel == 0.0 else ("agree to rounding (rel <= 1e-12)" if rel <= 1e-12 else ("close (rel <= 1e-6)" if rel <= 1e-6 else "DIFFERENT (rel > 1e-6)"))
    counts["n_match" if rel <= 1e-6 else "n_diff"] += 1
    rows.append((saved_key, pth, fmt(v_vt), fmt(v1), ", ".join(src), f"{rel:.2e}", verdict))
total = sum(counts.values()); assert total == len(rows), (counts, len(rows))
# R5: every numeric S1 key not compared, plus two_family.structure
compared = set(MAP) | set(DEFINITIONAL)
not_compared = sorted(k for k, v in S1.items() if k not in compared and (num(v) or (isinstance(v, list) and flat(v) is not None and len(flat(v)) > 0)))
new_sections = [k for k in ("training_grid", "refined_grid", "holdout", "X5_vorticity", "orbit_averages", "orbit_checks_7_14", "critical") if k in VT]
TS = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
L = [f"# VT-5 reading: clean-process validation of {JOB} start 0 against the saved values (helper compare_vt_nest10_v2.py; written {TS})", "",
     "Saved sources: S1 runs/.../results.jsonl (worker row 2026-10-26T14:23:30Z); S2 status/ledger.jsonl start_result row; S3 candidates/nest10_L10_cl0.45_om1.0_p0/meta.json diagnostics. 'equal' is bitwise; 'agree to rounding' rel <= 1e-12; 'close' rel <= 1e-6; anything above 1e-6 is listed as DIFFERENT and is read by hand. These labels are reading aids, not thresholds. A match reproduces saved diagnostics from a clean process; it is not new evidence about the state.", "",
     f"Summary: {len(rows)} rows; n_match {counts['n_match']} (within 1e-6 relative or identical), n_diff {counts['n_diff']}, n_missing_vt {counts['n_missing_vt']} (saved keys missing in the VT output), n_new {counts['n_new']} (VT values without a saved counterpart; unreviewed), n_definitional {counts['n_definitional']}, n_absent_both {counts['n_absent_both']}; identity n_match + n_diff + n_missing_vt + n_new + n_definitional + n_absent_both = {total} = row count (asserted).", "",
     "| saved key | VT JSON path | VT value | saved value | saved sources | max rel diff | verdict |", "|---|---|---|---|---|---|---|"]
for r in rows: L.append("| " + " | ".join(esc(c) for c in r) + " |")
L += ["", f"## Numeric S1 keys NOT compared ({len(not_compared)}; R5), plus two_family.structure (unmapped): " + ", ".join(not_compared) + "; two_family.structure.",
      "## VT output sections without a saved counterpart (new, unreviewed; not compared): " + ", ".join(new_sections) + ".",
      "- The worker's CRITICAL stdout line of 2026-10-26T13:58:28Z (worker.log line 148) reads: located |Omega| max 13.4820 at r=0.264, strain ratio 0.9114 (exact 1), transport 2.9e-10; the located_* rows above compare the saved full-precision values.",
      "- VT critical.local_maxima[0]: " + esc(json.dumps({k: get(VT, ("critical", "local_maxima", 0, k)) for k in ("abs_Omega", "r", "strain_ratio", "transport_ratio", "lambda_max_S")})),
      "- VT holdout random points: " + esc(json.dumps({k: get(VT, ("holdout", k)) for k in ("n_points", "rms_scaled_R_Omega", "max_scaled_R_Omega", "rms_scaled_Omega")})),
      "- Not computed by the validation script and therefore not compared: V10 (an optimizer-history quantity), the LM cost, the SPECTRUM, RADIAL LAMBDA and ORIGIN battery lines, the core-set a_max variants, E_ren / H_tot balances (BALANCE line), FAR RATE, RAY by |m|."]
open(out_md, "w").write("\n".join(L) + "\n")
json.dump(dict(rows=[dict(zip(("saved_key", "vt_path", "vt_value", "saved_value", "sources", "max_rel_diff", "verdict"), r)) for r in rows], counts=counts, total_rows=len(rows), not_compared_numeric_S1_keys=not_compared, new_sections=new_sections, written=TS), open(out_json, "w"), indent=1)
print(L[4]); print("wrote", out_md, out_json)
