#!/usr/bin/env python
"""Stage I gate shortlist (SPEC 11b G4): ranked, nontrivial states grouped into structurally different branches
((c_l, omega) region, dominant tail azimuthal order, toroidal fraction, core radius class); for each branch the best
state by holdout rho_u_max with pointers to its full residual vector (start file: spec_diag, spec_diag_holdout, critical)
and resource cost. Writes reports/STAGE1_SHORTLIST.md and reports/STAGE1_SHORTLIST.json."""
import sys, os, json, math, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import torch
from src.campaign import ledger

recs = ledger.read(os.path.join(ROOT, "status", "ledger.jsonl"))
ver = sys.argv[1] if len(sys.argv) > 1 else "latest"
rows = ledger.leaderboard(ledger.merge_reevaluations(recs) + [r for r in recs if r.get("kind") != "start_result"], n=10**6, solver_version=ver)
rows = [r for r in rows if not ledger.is_disposable(r.get("job_id")) and not (str(r.get("job_id", "")).endswith("_free") or "_free_" in str(r.get("job_id", "")))]
def branch_key(r):
    zf = os.path.join(ROOT, r["zfile"])
    dom_m, tor = None, None
    try:
        S = torch.load(zf, map_location="cpu", weights_only=False)
        by_m = S["diag"]["tail"]["by_m"]; dom_m = max(by_m, key=lambda k: by_m[k]); tor = S["diag"]["tail"]["toroidal_fraction"]
    except Exception:
        pass
    rc = r.get("r_core_holdout") or r.get("r_core") or 0
    rc_class = "core<1" if rc < 1 else ("core1-3" if rc < 3 else "core>3")
    j = str(r.get("job_id", ""))                                        # lineage (2026-10-25T12:58Z): the D6 transfer lineage and the route's own nest ladder are
    lin = "D6" if j.startswith(("d6", "c1c", "c1b", "c1_")) else ("nest" if j.startswith("nest") else ("balance" if j.startswith("s9") else "other"))   # structurally different branches at the same (c_l, omega)
    return (round(r["c_l"], 2), r["omega"], dom_m, ("toroidal" if (tor or 0) > 0.5 else "poloidal"), rc_class, lin)
branches = {}
for r in rows:
    k = branch_key(r)
    if k not in branches or r["rank_key"] < branches[k]["rank_key"]:
        branches[k] = r
items = sorted(branches.values(), key=lambda r: r["rank_key"])
def fmt(v, f):
    return (f % v) if isinstance(v, (int, float)) and v is not None and not (isinstance(v, float) and math.isnan(v)) else "n/a"
lines = [f"# Stage I shortlist (generated {time.strftime('%Y-%m-%dT%H:%MZ', time.gmtime())}; ranking key holdout rho_u_max, SPEC 7.3)", "",
         f"{len(rows)} ranked nontrivial states (solver version {ver}), {len(items)} structurally distinct branches. No state reaches Tier S.", "",
         "SPEC v1.20 7.3b: a state ranks ahead of another only if its holdout rho_u^max is lower on BOTH shell families and its sigma_u^max, sigma_Om and a_max each exceed the other's by at most 10 per cent; since SPEC v1.21 the sigma_u^max and a_max comparisons also use the core-resolved sets (balls B(y_*, a_eff/2), B(y_*, a_eff/4) and the inner shells to a_eff/16; columns 'all sets'), and a state that is core unresolved or lacks these values is not ordered;",
         "a missing value makes the pair not ordered. The rank column is the standard-family order only; rows with n/a in the 7.3b columns are not ordered against anything.",
         "CONDITION (lead d128 HA item 3, 2026-10-26): SPEC 7.3b asks for the same radius and quadrature for both states in its sigma_Om leg. The holdout shell edges (23 shells on both families, 138 radii) are shared by every state, but the holdout angular count depends on the degree (6380 at L10, 4700 at L8, 3276 at L6; the column 'holdout angles / radii' states each state's count from its saved spec_diag_holdout). Every '>' or '<' relation between states of different degree is therefore conditional on this leg; the core-resolved flags that enter the core-set comparisons are primary-reported, not independently verified.", "",
         "| rank | rho_u_max (holdout, std) | rho_u_max (half) | rho_nl_max (all shells) | sigma_u_max (std / half) | sigma_Om | a_max (std / half) | rho_sp_max (r<1) | V10 last-tenth decrease | c_l | omega | dominant m | tail type | r_core | e_F | N_core | lambda_max(S) | strain ratio at located max | Sigma_Z | iterations | seconds | job/start | dom m core/tail | helicity r<1 / 1-8 | r_core(half) | axial/planar | grad scale (origin, sh1, sh2) | near-linear (b/a core min-max) | max U / max Omega | GPU h | reproducible | tau_F (2^8 R0) | delta_G core / max | Q_sw (exact <= 1) | e_core (eddy energy fraction, holdout) | tau_0 / tau_1 / tau_2 (floored) | a_eff | sigma_u B(y_*, a_eff/2) / B(y_*, a_eff/4) | a_max ball centre / upper | sigma_u^max all sets | a_max all sets | core resolved | E_ren | max E_F (radius) | H_tot (with exterior term) | H_tot / int abs(h) | core alignment int h / int abs(U) abs(Omega) | K_E ratio carried/required (direct, exact 1) | K_H ratio carried/required (v1.24, exact 1) | G defect m (rel) / along F / orthogonal | holdout angles / radii (spec_diag_holdout n_eval_angles / n_eval_radii) |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
out = []
for i, r in enumerate(items[:12]):
    k = branch_key(r)
    lines.append(f"| {i+1} | {fmt(r['rank_key'], '%.3e')} | {fmt(r.get('rho_u_max_holdout_half'), '%.3e')} | {fmt(r.get('rho_nl_max_holdout') or r.get('rho_nl_max'), '%.2e')} | {fmt(r.get('sigma_u_max'), '%.3f')} / {fmt(r.get('sigma_u_max_half'), '%.3f')} | {fmt(r.get('sigma_Om'), '%.3f')} | {fmt(r.get('a_max'), '%.3f')} / {fmt(r.get('a_max_half'), '%.3f')} | {fmt(r.get('rho_sp_max_r1_holdout'), '%.3f')} | {fmt(r.get('v10_last_tenth_rel_decrease'), '%.1e')} | {r['c_l']} | {r['omega']} | {k[2]} | {k[3]} | {fmt(r.get('r_core_holdout') or r.get('r_core'), '%.2f')} | {fmt(r.get('e_F'), '%.2f')} | {fmt(r.get('N_core'), '%.2e')} | {fmt(r.get('lambda_max_S'), '%.2f')} | {fmt(r.get('located_strain_ratio'), '%.3f')} | {fmt(r.get('Sigma_Z'), '%.3f')} | {r.get('iterations')} | {fmt(r.get('seconds'), '%.0f')} | {r['job_id']}/{r['start']} |")
    st = r.get("structure") or {}
    gs = st.get("grad_scale_T4_over_U") or []
    lines[-1] = lines[-1] + (f" {st.get('core_dominant_m')} / {st.get('tail_dominant_m')} | {fmt(st.get('helicity_r_lt_1'), '%+.2e')} / {fmt(st.get('helicity_1_8'), '%+.2e')} | {fmt(st.get('r_core_half'), '%.3g')} | {fmt(st.get('axial_to_planar_vorticity'), '%.2f')} | "
                             + " ".join(fmt(v, '%.2f') for v in gs) + f" | {st.get('near_linear')} ({fmt(st.get('b_over_a_core_min'), '%.2f')}-{fmt(st.get('b_over_a_core_max'), '%.2f')}) | {fmt(r.get('max_U'), '%.2f')} / {fmt(r.get('max_abs_Omega'), '%.1f')} | {fmt((r.get('seconds') or 0) / 3600.0, '%.2f')} | {'yes' if (str(r.get('ts', '')) >= '2026-10-24T19:39' and r.get('rng_seed') is not None and r.get('solver_version')) else 'no (pre-19:39Z row or missing seed/version)'} | {fmt(r.get('tau_F_R8'), '%.3f')} | {fmt(r.get('delta_G_core'), '%.3f')} / {fmt(r.get('delta_G_max'), '%.3f')} | {fmt(r.get('Q_sw'), '%.3f')} | {fmt(r.get('e_core_holdout') if r.get('e_core_holdout') is not None else r.get('e_core'), '%.4f')} | {fmt(r.get('tau0_floored'), '%.2e')} / {fmt(r.get('tau1_floored'), '%.2e')} / {fmt(r.get('tau2_floored'), '%.2e')} | {fmt(r.get('a_eff'), '%.4f')} | {fmt(r.get('sigma_u_ball_half'), '%.3f')} / {fmt(r.get('sigma_u_ball_quarter'), '%.3f')} | {fmt(r.get('a_max_ball_half_centre'), '%.3f')} / {fmt(r.get('a_max_ball_half_upper'), '%.3f')} | {fmt(r.get('sigma_u_max_core'), '%.3f')} | {fmt(r.get('a_max_core'), '%.3f')} | {('yes' if r.get('core_resolved') else 'NO (core unresolved)') if r.get('core_resolved') is not None else 'n/a (not ordered)'} | {fmt(r.get('E_ren'), '%.3f')} | {fmt(r.get('E_F_max'), '%.5f')} ({fmt(r.get('r_at_E_F_max'), '%.3g')}) | {fmt(r.get('H_tot'), '%.3f')} | {fmt(r.get('H_tot_over_abs'), '%.3f')} | {fmt(r.get('core_alignment'), '%.3f')} | {fmt(r.get('K_ratio_direct'), '%.3f')} | {fmt(r.get('K_H_ratio_direct'), '%.3f')} | {fmt(r.get('carried_mismatch_rel') if r.get('carried_mismatch_rel') is not None else r.get('G_carried_mismatch_rel'), '%.3f')} / {fmt(r.get('G_defect_parallel_rel'), '%.3f')} / {fmt(r.get('G_defect_orth_rel'), '%.3f')} |")
    try:
        import torch as _torch
        _z = _torch.load(os.path.join(ROOT, r["zfile"]), map_location="cpu", weights_only=False)
        _sdh = _z.get("spec_diag_holdout") or {}
        _na, _nr = _sdh.get("n_eval_angles"), _sdh.get("n_eval_radii")
    except Exception:
        _na, _nr = None, None
    lines[-1] = lines[-1] + f" {_na if _na is not None else 'n/a'} / {_nr if _nr is not None else 'n/a'} |"
    out.append(dict(rank=i + 1, branch=list(k), lineage=("D6-lineage" if r["job_id"].startswith("d6") else "nest ladder" if r["job_id"].startswith("nest") else "from-scratch L6 sweeps"), record=r))
# SPEC v1.20 7.3b pairwise order relations among the shortlisted representatives
def ahead(x, y):
    """x ranks ahead of y: lower holdout rho_u^max on BOTH families, and sigma_u^max (both families), sigma_Om, a_max (both families) each at most
    10 per cent above y's; any missing value -> not ordered."""
    need = ("rho_u_max_holdout", "rho_u_max_holdout_half", "sigma_u_max", "sigma_u_max_half", "sigma_Om", "a_max", "a_max_half", "sigma_u_max_core", "a_max_core", "a_max_core_upper", "core_resolved")
    if any(x.get(k) is None or y.get(k) is None for k in need):
        return None
    if not (x["core_resolved"] and y["core_resolved"]):     # SPEC v1.21 (c): a core-unresolved state is not ordered
        return None
    if not (x["rho_u_max_holdout"] < y["rho_u_max_holdout"] and x["rho_u_max_holdout_half"] < y["rho_u_max_holdout_half"]):
        return False
    return all(x[k] <= 1.1 * y[k] for k in ("sigma_u_max", "sigma_u_max_half", "sigma_Om", "a_max", "a_max_half", "sigma_u_max_core", "a_max_core", "a_max_core_upper"))
reps = items[:12]
lines += ["", "## SPEC v1.20 7.3b order relations (rows X, columns Y; '>' X ahead of Y, '<' Y ahead of X, '-' not ordered, '?' a value is missing)", "",
          "| X \\ Y | " + " | ".join(str(j + 1) for j in range(len(reps))) + " |", "|---|" + "---|" * len(reps)]
rel = {}
for i, x in enumerate(reps):
    row = []
    for j, y in enumerate(reps):
        if i == j:
            row.append("."); continue
        a = ahead(x, y); b = ahead(y, x)
        if a is None or b is None: row.append("?")
        elif a: row.append(">")
        elif b: row.append("<")
        else: row.append("-")
        rel[(i + 1, j + 1)] = row[-1]
    lines.append(f"| {i + 1} | " + " | ".join(row) + " |")
n_ord = sum(1 for v in rel.values() if v in (">", "<")) // 2; n_pairs = len(reps) * (len(reps) - 1) // 2
lines += ["", "Relations between representatives of different degree are conditional on the 7.3b sigma_Om same-radius-and-quadrature leg (holdout angular counts differ by degree; see the CONDITION line above); the core-resolved flags are primary-reported.", "", f"{n_ord} of {n_pairs} pairs are ordered under 7.3b; the rest are not ordered (both stay on the shortlist). Branch lineage: job id prefix (d6*: D6-lineage descendants; nest*: route's own random-start ladder; s1*/c2x2*: from-scratch L6 sweeps and their continuations)."]
# G4: branch grouping and GPU hours per branch (lead 2026-10-25T02:02Z item 3; start_result seconds summed per lineage prefix over the whole ledger)
def lineage_of(job_id):
    j = str(job_id)
    if j.startswith("d6"): return "D6-lineage descendants (warm starts from the verifier's released degree-6 state; c_l 0.45-0.48, omega 0.3)"
    if j.startswith("nest"): return "nest ladder (route's own random L2 starts promoted L2 -> L4 -> L6; (0.45, 0.3), (0.45, 1), (0.42, 0.3))"
    if j.startswith("s7"): return "S7 mean-swirl probes (Stage II structural arm, started early)"
    if j.startswith(("s1", "c2x2")): return "from-scratch L6 sweeps and continuations (s1*, c2x2*; 5 c_l x 5 |omega| grid, floor states 0.25-0.5)"
    return "other (smoke, tests, controls)"
hours = {}; nstarts = {}
for r_ in recs:
    if r_.get("kind") == "start_result" and r_.get("seconds"):
        k = lineage_of(r_.get("job_id")); hours[k] = hours.get(k, 0.0) + r_["seconds"] / 3600.0; nstarts[k] = nstarts.get(k, 0) + 1
lines += ["", "## Branches (G4 grouping) and GPU hours per branch", "", "| branch | starts in the ledger | GPU hours (start wall time, 1-3 processes per GPU) | best holdout rho_u^max (std / half) | Q_sw of the representative | note |", "|---|---|---|---|---|---|"]
for k in sorted(hours, key=lambda k: -hours[k]):
    reps_k = [r for r in items if lineage_of(r["job_id"]) == k]
    best = reps_k[0] if reps_k else None
    note = ""
    if best is not None and best.get("Q_sw") is not None and best["Q_sw"] > 1:
        note = "Q_sw > 1 (sampled maxima): by the residual form of the mean-swirl identity, its mean azimuthal residual is at least about max|S| (Q_sw - 1); not an enclosed bound (FINAL_REPORT section 2 item 28 (d))"
    lines.append(f"| {k} | {nstarts[k]} | {hours[k]:.1f} | {fmt(best['rank_key'], '%.4f') if best else 'n/a'} / {fmt(best.get('rho_u_max_holdout_half'), '%.4f') if best else 'n/a'} | {fmt(best.get('Q_sw'), '%.2f') if best else 'n/a'} | {note} |")
lines += ["", "Structurally different branches on the shortlist: (i) D6-lineage descendants (core gradient scale 12-14, sigma_u^max 1.8-2.1, Q_sw 0.15-0.44, tail 82-84 per cent mean swirl);",
          "(ii) nest ladder (0.45, 1) and (0.42, 0.3): balanced cores (gradient scale about 1, sigma_u^max 0.5-0.6, GRAM gamma -1 on every core shell) but Q_sw 2.0-2.6 (mean swirl not eddy-generated; near-axisymmetric swirl states);",
          "(iii) nest2 L2 states with dominant m = 2 tails and core eddy fractions 0.7-0.96 (rho_u^max 0.12-0.16); (iv) from-scratch L6 floor states (not on the top-12 list; rho_u^max 0.25-0.5). None approaches Tier S; no pair across (i)-(iii) is ordered under 7.3b except where listed above."]
lines += ["", "Full residual vectors: each start file (zfile) holds diag, spec_diag (training grid), spec_diag_holdout, critical (located maxima, W zeros).",
          "Resource cost: seconds per start as recorded; GPU type A100 80GB, two to three processes per GPU."]
os.makedirs(os.path.join(ROOT, "reports"), exist_ok=True)
open(os.path.join(ROOT, "reports", "STAGE1_SHORTLIST.md"), "w").write("\n".join(lines) + "\n")
json.dump(out, open(os.path.join(ROOT, "reports", "STAGE1_SHORTLIST.json"), "w"), indent=1)
print("\n".join(lines[:4 + min(12, len(items))]))
