#!/usr/bin/env python
"""v11 (08:2xZ, V205): a (k) add-on file that is present but rejected (hash, case, harness, completeness) makes the (k) and (k)+(j) outcomes INVALID with the reason; only a missing file leaves (k) equal to the registered outcome.
v10 (08:1xZ, V202 items 1-5): (1) a salvage record whose pair dictionary is present but invalid is INVALID (no fallback to the scalar); (2) provenance
(_source_gates_py) is set by the checker from the file each record came from, overwriting anything in the input; (3) an add-on marked complete=false, or whose
per-Jacobian count disagrees with its columns, is rejected; (4) pair witness scale must equal the record's step scale (add-on and registered records);
(5) add-on whole-column errors must equal per_group[step]['all'] at both steps.
v9 (08:0xZ, V198 items 1-5): (1) the (k) decision is recomputed from the add-on's own column_test witnesses (two fresh steps 1e-2 s_j, 1e-3 s_j: finite
error ladders, five-point and second-order rules at both steps, the pair Richardson from the witness norms with eligibility, active sets at the base and all
eight stencil points for J_cw/J_c); the add-on must name the case, derive from the record (hash), be built on the record's gates.py, and cover every column
that fails the registered rule in that Jacobian; otherwise the (k) outcome is INVALID; (2) with (k) requires exactly twenty distinct coefficient records that
are the drawn columns; len(ids) != 20 is INVALID in the registered outcome; (3) INVALID pair evidence stays INVALID in every outcome (no small-amplitude
exclusion of invalid records); (4) salvage records use complete pair witnesses first when present, the saved pair must be adjacent and eligible, and the
convention is decided by the source gates.py hash of the file the record came from (companion records carry _source_gates_py), not by the convention string
alone; (5) negative or non-finite physical-omega F0 Richardson witnesses (whole or group) are INVALID before any re-judgement.
v8 (07:5xZ): a coefficient-only record (gates.py --sections G1_coef / G1_Jc_coef, no parameter columns) is combined with the parameter columns of the companion
G1 record of the same case in the same directory (gates_gpu_v1_<case>_G1v4.json, then gates_gpu_v1_<case>.json): the parameter decisions come from that record
(its file and gates.py hash are stated as parameter_source); the coefficient decisions from the coefficient-only record. Both files are named in the output.
v7 (07:5xZ, SPEC v1.18 3.6 (k), lead 07:41Z): three outcomes per case and Jacobian: registered; with the post-result step rule (k) (a column or group that fails
the registered ladder passes under (k) when the add-on validation/g1_step_addon_<case>.json shows the pair (1e-2 s_j, 1e-3 s_j) passing: both steps within tau,
second order and five point, and the pair Richardson within tau; label "pass under the post-result step rule (k)", with the per-decade error ratio); with (k)
and the small-amplitude rule (j). The add-on record must be on the same case and come from the same v5c coefficient record (input hash recorded).
v6 (07:4xZ, V195): (1) a record whose convention is v5c must carry full pair witnesses for all four nominal pairs (no fallback to a scalar summary); salvage of
older records is allowed only through an explicit allowlist of recorded conventions (v4 and earlier), separately labelled, with the witnesses actually present
(a recorded Richardson scalar must be finite and non-negative); missing fields never make a record "old"; (2) each of the six registered group decisions
(group_pass) must exist on every record, iterated from REQUIRED_GROUPS; (3) non-finite, missing or negative pair evidence is INVALID (not FAIL); discrepancies
between recomputed decisions and stored summaries are reported.
v5 (07:3xZ, V193): (1) ids_match is part of the amended aggregate too; (2) the closure, gauge and far-anchor-block groups are required for every battery case
in addition to the three radial groups; (3) the raw active-set records must carry the exact base label and the twenty stencil labels (+-h s, +-2h s for the
five nominal steps at the recorded step scale) and their signatures must agree; (4) every Richardson error is recomputed from the witness norms
(norm_diff_scaled, norm_d_scaled, norm_R_scaled, floor, scale) for the four adjacent nominal pairs and each pair's eligibility from the errors at those steps;
stored values are comparisons only; (5) the whole-column ladders must be complete, finite, non-negative and equal to per_group[step][kind]['all'].
v4 (07:2xZ, V192): (1) the twenty coefficient ids are matched against the case's drawn columns (G1_coefficient_columns_drawn) and the per-Jacobian column lists;
(2) the registered row groups (near_origin, core_intermediate, far, far_anchor_block) and the whole-column 'all' witnesses are required, with the five nominal
step labels, finite non-negative norms and errors and valid scales; (3) the raw base and stencil active records are validated (all equal) before
active_sets_identical is trusted (J_f: frozen convention); (4) the second-order, five-point and Richardson decisions are RECOMPUTED from the recorded errors and
pair witnesses and compared with the stored flags, which are reported but not authoritative; (5) REJUDGED_PASS counts as a registered pass.
v3 (07:0xZ, V190): completeness schema before any classification: every record must have the five ladder steps, every required group, finite d, D, D4 and whole-column norms;
exactly the registered number of distinct coefficient columns per Jacobian (20); explicit active-set validity for J_cw and J_c (the frozen-weight J_f has no changing
weight active set: declared frozen convention); the registered outcome distinguishes INVALID (missing or incomplete evidence) from FAIL (numerical); a separate
resolved-coverage count (>= 5) is kept. Physical-omega parameter records written by harness v3/v4 (derivative scaled by omega < 0.5 against the fixed floor,
V190 item 2) are re-judged in physical units from the saved witnesses: per-step second-order and five-point errors are recomputed exactly from the stored
scaled norms and errors; the F = 0 Richardson is scale-free; a floored-only Richardson pass is marked RECOMPUTE_NEEDED (not a pass).
v2 (06:4xZ, V187): per-group norms divided by s_j before the comparison; records with non-identical active sets or missing decisions are invalid (fail closed).
SPEC v1.17 3.6 (j) "small-amplitude group, post-result rule" (lead 06:22Z; V180, V183): per battery case and Jacobian (J_f, J_cw, J_c harness) the checker
writes the REGISTERED outcome and the AMENDED outcome side by side. Fails closed: missing or non-finite records count as failures, never as small-amplitude.
Registered outcome (3.0 (b'), (d)): every parameter column passes (whole column and every group) and every coefficient column passes (whole column and every group).
Amended outcome: (i) the whole-column test is retained for every column; (ii) parameter columns are never classified: both parameters, in both coordinate systems,
must pass every group with complete valid records (active sets identical); (iii) a coefficient-column group is small-amplitude when max(||d_g||, ||D_g,h|| second-order and five-point) < 1e-6 ||column|| at EVERY
valid step (any absent or non-finite norm: not small-amplitude); it is reported as "not tested on that column"; (iv) a group counts only if, in the same case and
Jacobian, it passes on all parameter columns and on at least five DISTINCT coefficient columns where it is not small-amplitude, and fails on none where it is
not small-amplitude; otherwise OPEN. Usage: python validation/g1_coverage_check.py validation/gates_gpu_v1_<case>*.json -> prints markdown; writes <file>_coverage.json."""
import json, sys, glob, os, math
JACS = (("Jf", "G1_Jf_param_columns", "G1_Jf_coefficient_columns"), ("Jcw", "G1_Jcw_param_columns", "G1_Jcw_coefficient_columns"), ("Jc", "G1_Jc_param_columns", "G1_Jc_coefficient_columns"))
THRESH = 1e-6; MIN_COEF = 5; LABEL = "small-amplitude group, post-result rule (SPEC v1.17 3.6 (j))"
def fin(x):
    return isinstance(x, (int, float)) and math.isfinite(x)
def col_record(entry, jac):
    return entry.get("Jf") if (jac == "Jf" and isinstance(entry.get("Jf"), dict)) else entry
def col_id(entry, jac):
    return entry.get("column", col_record(entry, jac).get("column"))
N_STEPS = 5; N_COEF = 20; TAU_ALL = 1e-6; TAU_GROUP = 1e-5
STEP_LABELS = ["1e-03", "1e-04", "1e-05", "1e-06", "1e-07"]
REQUIRED_GROUPS = ["near_origin(r<=0.1R0)", "core_intermediate", "far(r>256R0)", "far_anchor_block", "closure", "gauge"]      # every registered battery case has anchors, closure rows and the gauge row (V193 item 2)
PAIR_LABELS = [f"{STEP_LABELS[i]}->{STEP_LABELS[i + 1]}" for i in range(len(STEP_LABELS) - 1)]
def expected_stencil_labels(scale):
    """The labels column_test writes: f'{t:+.1e}' for t = 0 and t = +-h s, +-2h s over the five nominal steps (V193 item 3)."""
    labs = {f"{0.0:+.1e}"}
    for l in STEP_LABELS:
        h = float(l) * scale
        for t in (h, -h, 2 * h, -2 * h):
            labs.add(f"{t:+.1e}")
    return labs
def active_sets_valid(rec, needs_active):
    """V192 item 3 / V193 item 3: the raw base and the twenty stencil active records (exact labels for the recorded step scale) must exist and agree (recomputed);
    the base flag must be set; J_f uses the declared frozen convention."""
    if not needs_active:
        return True, "frozen-weight convention (no changing active set)"
    a = rec.get("active_sets"); sc = rec.get("step_scale", 1.0)
    if not isinstance(a, dict) or not rec.get("active_set_base_recorded"):
        return False, "raw active-set records or the base record missing"
    exp = expected_stencil_labels(sc)
    if set(a.keys()) != exp:
        return False, f"active-set labels do not match the stencil of the recorded step scale (have {len(a)}, expected {len(exp)}; missing {sorted(exp - set(a.keys()))[:4]})"
    keys = set(json.dumps(v, sort_keys=True) for v in a.values())
    if len(keys) != 1:
        return False, "active sets differ among the stencil points and the base"
    if rec.get("active_sets_identical") is not True:
        return False, "stored active_sets_identical not True"
    return True, ""
def recompute_richardson_from_witnesses(allp, errs_by_label, tau, expected_scale=None):
    """V193 item 4: every one of the four adjacent nominal pairs must be present with finite non-negative norm_diff_scaled, norm_d_scaled, norm_R_scaled, floor and
    a positive scale; the error is recomputed as norm_diff / max(norm_d, norm_R, floor); eligibility from the errors at the two steps. Returns (best, pair, ok, detail)."""
    if not isinstance(allp, dict) or sorted(allp.keys()) != sorted(PAIR_LABELS):
        return None, None, False, "pair witnesses missing or mislabelled"
    best = None; best_pair = None; detail = {}
    for pl in PAIR_LABELS:
        w = allp[pl]; a, b = pl.split("->")
        vals = [w.get(k) for k in ("norm_diff_scaled", "norm_d_scaled", "norm_R_scaled", "floor")]
        if any(not fin(x) or x < 0 for x in vals) or not fin(w.get("scale")) or w.get("scale") <= 0:
            return None, None, False, f"pair {pl}: witness norms missing, non-finite, negative or scale invalid"
        if expected_scale is not None and fin(expected_scale) and abs(w["scale"] - expected_scale) > 1e-12 * max(1.0, abs(expected_scale)):   # V202 item 4
            return None, None, False, f"pair {pl}: witness scale {w['scale']} differs from the record's step scale {expected_scale}"
        nd_, nd, nR, F = vals
        r = nd_ / max(nd, nR, F, 1e-300)
        elig = fin(errs_by_label.get(a)) and fin(errs_by_label.get(b)) and errs_by_label[a] <= tau and errs_by_label[b] <= tau
        detail[pl] = dict(recomputed=r, stored=w.get("richardson_error"), eligible=elig, stored_eligible=w.get("pair_passes_second_order"))
        if elig and (best is None or r < best):
            best, best_pair = r, pl
    return best, best_pair, True, detail
def consecutive_pass(errs_by_label, tau):
    labs = [l for l in STEP_LABELS if l in errs_by_label]
    return any(fin(errs_by_label[labs[i]]) and fin(errs_by_label[labs[i + 1]]) and errs_by_label[labs[i]] <= tau and errs_by_label[labs[i + 1]] <= tau for i in range(len(labs) - 1))
def ladder_ok(errs):
    return isinstance(errs, dict) and sorted(errs.keys()) == sorted(STEP_LABELS) and all(fin(v) and v >= 0 for v in errs.values())
SALVAGE_CONVENTIONS = ("v4 (", "v3 (")      # recorded scaling_convention prefixes of pre-v5c harness versions whose records may be judged from the witnesses they have (separately labelled)
SALVAGE_HARNESS_HASHES = {"918c2e06ba2bae2f": "gates.py v4", "549c21b0fac9ecfa": "gates.py v3"}   # explicit source-hash allowlist (V195 item 1): the record file's recorded gates.py hash
CURRENT_HARNESS = {"hash": None}
V5C_HASHES = {"5f4079926f1c757b"}                                        # gates.py v5c (frozen harness; full pair witnesses)
K_STEPS = ["1e-02", "1e-03"]; K_PAIR = "1e-02->1e-03"
def record_convention(rec):
    """V198 item 4: the convention is decided by the gates.py hash of the file the record came from (the record file, or the companion file for copied
    parameter records); a convention string that contradicts the source is 'unknown' (INVALID)."""
    src = str(rec.get("_source_gates_py") or CURRENT_HARNESS["hash"] or "")[:16]; conv = str(rec.get("scaling_convention") or "")
    if src in SALVAGE_HARNESS_HASHES:
        return "salvage" if (not conv or any(conv.startswith(pfx) for pfx in SALVAGE_CONVENTIONS)) else "unknown"
    if src in V5C_HASHES:
        return "v5c" if conv.startswith("v5c") else "unknown"
    return "unknown"
def richardson_evidence(container, errs_by_label, tau, rec):
    """V195 items 1 and 3: v5c records need the full pair witnesses (INVALID otherwise); salvage records use the recorded finite non-negative scalar, labelled;
    unknown conventions are INVALID. Returns (rich, pair, status, detail): status in PASS_EVIDENCE / INVALID."""
    conv = record_convention(rec); allp = container.get("richardson_all_pairs")
    if conv == "v5c":
        rich, pair, okw, detail = recompute_richardson_from_witnesses(allp, errs_by_label, tau, expected_scale=rec.get("derivative_scale", rec.get("step_scale", 1.0)))
        return (rich, pair, "witnesses", detail) if okw else (None, None, "INVALID", detail)
    if conv == "salvage":
        if isinstance(allp, dict):                                      # V198 item 4: complete norm witnesses first; V202 item 1: invalid witnesses are INVALID, no fallback
            rich, pair, okw, detail = recompute_richardson_from_witnesses(allp, errs_by_label, tau, expected_scale=rec.get("derivative_scale", rec.get("step_scale", 1.0)))
            if okw:
                return rich, pair, "witnesses (salvage record with complete pair witnesses)", detail
            return None, None, "INVALID", f"salvage record with a pair dictionary that is not valid evidence: {detail}"
        r = container.get("richardson", container.get("richardson_error"))
        if r is None:                                                   # the harness stores no Richardson value when no adjacent pair passes the second-order rule:
            return None, None, "salvage (no passing pair: numerical failure, no Richardson value)", None   # a numerical FAIL, not missing evidence
        if not fin(r) or r < 0:
            return None, None, "INVALID", "salvage record with a non-finite or negative Richardson value"
        pair = container.get("richardson_pair")
        if pair is not None:                                            # V198 item 4: a saved pair must be adjacent and both of its steps must pass the second-order rule
            pl = pair if isinstance(pair, str) else "->".join(str(x) for x in pair)
            if pl not in PAIR_LABELS:
                return None, None, "INVALID", f"salvage record names a non-adjacent Richardson pair {pl}"
            a, b = pl.split("->")
            if not (fin(errs_by_label.get(a)) and fin(errs_by_label.get(b)) and errs_by_label[a] <= tau and errs_by_label[b] <= tau):
                return None, None, "INVALID", f"salvage record names a Richardson pair {pl} whose steps do not both pass the second-order rule"
            return r, pl, "salvage (recorded Richardson scalar of an adjacent eligible pair; pre-v5c harness)", None
        return r, None, "salvage (recorded Richardson scalar; pre-v5c harness)", None
    return None, None, "INVALID", f"unknown recording convention '{rec.get('scaling_convention')}'"
def recompute_whole(rec, tau=TAU_ALL):
    """V192/V193 item 4-5: whole-column decision recomputed from complete, finite, non-negative error ladders (equal to per_group[step][kind]['all']) and from the
    Richardson pair witnesses (v5c records: witness norms; v4 records: the recorded value, labelled as such). Missing data -> not a pass (INVALID at the schema)."""
    e2 = rec.get("errors") or rec.get("errors_second_order") or {}; e4 = rec.get("errors_five_point") or {}
    if not (ladder_ok(e2) and ladder_ok(e4)):
        return dict(PASS=False, reason="whole-column error ladder incomplete or non-finite", stored_PASS=rec.get("PASS"), agrees_with_stored=False)
    pg = rec.get("per_group") or {}
    for l in STEP_LABELS:
        if l in pg and (abs((pg[l].get("second_order") or {}).get("all", float("nan")) - e2[l]) > 1e-12 * max(1.0, e2[l]) or abs((pg[l].get("five_point") or {}).get("all", float("nan")) - e4[l]) > 1e-12 * max(1.0, e4[l])):
            return dict(PASS=False, reason=f"whole-column errors contradict per_group['all'] at step {l}", stored_PASS=rec.get("PASS"), agrees_with_stored=False)
    p2 = consecutive_pass(e2, tau); p4 = consecutive_pass(e4, tau)
    rich, pair, source, detail = richardson_evidence(rec, e2, tau, rec)
    if source == "INVALID":
        return dict(PASS=False, INVALID=True, reason=detail, stored_PASS=rec.get("PASS"), agrees_with_stored=False)
    ok = bool(p2 and p4 and fin(rich) and rich <= tau)
    return dict(pass_second_order=p2, pass_five_point=p4, richardson=rich, richardson_pair=pair, richardson_source=source, pairs=detail, PASS=ok, stored_PASS=rec.get("PASS"), agrees_with_stored=(ok == bool(rec.get("PASS"))))
def recompute_group(rec, g, tau=TAU_GROUP):
    pg = rec.get("per_group") or {}
    e2 = {h: (v.get("second_order") or {}).get(g) for h, v in pg.items()}; e4 = {h: (v.get("five_point") or {}).get(g) for h, v in pg.items()}
    if not (ladder_ok(e2) and ladder_ok(e4)):
        return dict(PASS=False, reason="group error ladder incomplete or non-finite", stored_PASS=((rec.get("group_pass") or {}).get(g) or {}).get("PASS"), agrees_with_stored=False)
    p2 = consecutive_pass(e2, tau); p4 = consecutive_pass(e4, tau)
    gp = (rec.get("group_pass") or {}).get(g)
    if not isinstance(gp, dict) or "PASS" not in gp:
        return dict(PASS=False, INVALID=True, reason=f"group decision for {g} missing", stored_PASS=None, agrees_with_stored=False)
    rich, pair, source, detail = richardson_evidence(gp, e2, tau, rec)
    if source == "INVALID":
        return dict(PASS=False, INVALID=True, reason=detail, stored_PASS=gp.get("PASS"), agrees_with_stored=False)
    ok = bool(p2 and p4 and fin(rich) and rich <= tau)
    return dict(pass_second_order=p2, pass_five_point=p4, richardson=rich, richardson_pair=pair, richardson_source=source, PASS=ok, stored_PASS=gp.get("PASS"), agrees_with_stored=(ok == bool(gp.get("PASS"))))
def record_complete(rec, groups, needs_active):
    """Completeness schema (V190, V192): the five nominal steps, the registered groups and the whole column with finite non-negative norms and errors, valid scales,
    decisions present, and (for J_cw / J_c) validated identical active sets including the base. Returns (ok, reason)."""
    if not isinstance(rec, dict) or "PASS" not in rec or not isinstance(rec.get("group_pass"), dict):
        return False, "decision or group decisions missing"
    pg = rec.get("per_group")
    if not isinstance(pg, dict) or sorted(pg.keys()) != sorted(STEP_LABELS):
        return False, f"ladder step labels {sorted(pg.keys()) if isinstance(pg, dict) else None} (need {STEP_LABELS})"
    pg0 = pg[STEP_LABELS[0]] if isinstance(pg, dict) and STEP_LABELS[0] in pg else {}
    present = set((pg0.get("second_order") or {}).keys())
    for g in REQUIRED_GROUPS + ["all"]:
        if g not in present:
            return False, f"registered group {g} absent from the record"
    gpd = rec.get("group_pass") or {}
    for g in REQUIRED_GROUPS:                                               # V195 item 2: each registered group DECISION must exist
        if not (isinstance(gpd.get(g), dict) and "PASS" in gpd[g]):
            return False, f"group decision for {g} missing"
    if record_convention(rec) == "unknown":
        return False, f"unknown recording convention '{rec.get('scaling_convention')}' (neither v5c nor an allowlisted older harness)"
    sc = rec.get("step_scale", 1.0); dsc = rec.get("derivative_scale", sc)
    if not (fin(sc) and sc > 0 and fin(dsc) and dsc > 0):
        return False, "invalid step or derivative scale"
    okA, whyA = active_sets_valid(rec, needs_active)
    if not okA:
        return False, whyA
    cn = rec.get("norm", rec.get("column_norm"))            # coefficient records store 'norm', parameter records (column_test output) 'column_norm'
    if not fin(cn) or cn <= 0:
        return False, "whole-column norm missing or non-finite"
    for h, v in pg.items():
        for g in list(groups) + ["all"]:
            for k in ("norm_d", "norm_fd", "norm_fd_five_point"):
                x = (v.get(k) or {}).get(g)
                if not fin(x) or x < 0:
                    return False, f"group {g} step {h}: {k} missing, non-finite or negative"
        for k in ("second_order", "five_point", "second_order_F0", "five_point_F0"):
            for g in list(groups) + ["all"]:
                x = (v.get(k) or {}).get(g)
                if not fin(x) or x < 0:
                    return False, f"group {g} step {h}: {k} missing, non-finite or negative"
    for k in ("errors", "errors_second_order"):
        if k in rec and (not isinstance(rec[k], dict) or sorted(rec[k].keys()) != sorted(STEP_LABELS)):
            return False, "whole-column error ladder incomplete"
    return True, ""
def record_valid(rec):
    """Validity for the decision functions: complete decisions and active sets not reported as different (the completeness schema is checked separately)."""
    return isinstance(rec, dict) and rec.get("active_sets_identical") is not False and isinstance(rec.get("group_pass"), dict) and "PASS" in rec
def rejudge_physical_omega(rec, tau=1e-6, tau_group=1e-5):
    """V190 item 2: a physical-omega record of harness v3/v4 (step_scale omega < 0.5, no derivative_scale field) scaled d and D_h by omega against the fixed floor.
    From the stored scaled norms and errors the unscaled per-step errors are recomputed exactly: |d - D| s = e * max(|d| s, |D| s, F), so
    e' = (e * den / s) / max(|d|, |D|, F). Whole-column decision: two consecutive passing steps (second order and five point) in e'; the Richardson
    with F = 0 is scale-free (richardson_F0 <= tau suffices); otherwise RECOMPUTE_NEEDED. Returns dict(status, ...)."""
    s_ = rec.get("step_scale", 1.0); conv = str(rec.get("scaling_convention") or "")
    if not (fin(s_) and 0 < s_ < 1.0) or rec.get("derivative_scale") is not None or not (conv.startswith("v3") or conv.startswith("v4")) or record_convention(rec) != "salvage":
        return dict(status="NOT_APPLICABLE")               # only harness v3/v4 records scaled the physical derivative; v1/v2 and v5 records are in physical units
    pg = rec.get("per_group") or {}; hs = sorted(pg.keys(), key=lambda x: -float(x))
    def unscaled(h, g, kind):
        v = pg[h]; nd = v["norm_d"][g]; e = v["second_order"][g] if kind == "2" else v["five_point"][g]; F = (v.get("floor") or {}).get(g, 0.0)
        nf = v["norm_fd"][g] if kind == "2" else v["norm_fd_five_point"][g]
        den = max(nd, nf, F); diff = e * den / s_
        return diff / max(nd / s_, nf / s_, F, 1e-300)
    out = dict(status=None, per_group={})
    ok_all = True
    for g in ["all"] + [g for g in pg[hs[0]]["second_order"] if g != "all"]:
        t = tau if g == "all" else tau_group
        e2 = [unscaled(h, g, "2") for h in hs]; e4 = [unscaled(h, g, "4") for h in hs]
        p2 = any(e2[i] <= t and e2[i + 1] <= t for i in range(len(hs) - 1)); p4 = any(e4[i] <= t and e4[i + 1] <= t for i in range(len(hs) - 1))
        r0 = rec.get("richardson_error_F0") if g == "all" else ((rec.get("group_pass") or {}).get(g) or {}).get("richardson_error_F0")
        if r0 is not None and (not fin(r0) or r0 < 0):                   # V198 item 5: negative or non-finite witnesses are INVALID before any re-judgement
            st = "INVALID"; rich_ok = False
        else:
            rich_ok = fin(r0) and r0 <= t
            st = "PASS" if (p2 and p4 and rich_ok) else ("RECOMPUTE_NEEDED" if (p2 and p4) else "FAIL")
        out["per_group"][g] = dict(e2_physical_units=e2, e4_physical_units=e4, pass_second_order=p2, pass_five_point=p4, richardson_F0=r0, status=st)
        ok_all = ok_all and st == "PASS"
    if any(v["status"] == "INVALID" for v in out["per_group"].values()):
        out["status"] = "INVALID"
    else:
        out["status"] = "PASS" if ok_all else ("RECOMPUTE_NEEDED" if all(v["status"] in ("PASS", "RECOMPUTE_NEEDED") for v in out["per_group"].values()) else "FAIL")
    return out
def small_amplitude(rec, g):
    """v1.17 (iii), with the normalization of V187: the per-group norms stored by column_test v3 are SCALED by the step scale s_j, the whole-column norm
    (rec['norm']) is not; the group norms are divided by s_j before the comparison with 1e-6 of the column norm. Fails closed on anything missing or
    non-finite (then not small-amplitude, and the record counts as tested)."""
    pg = rec.get("per_group"); cn = rec.get("norm", rec.get("column_norm")); sj = rec.get("step_scale", 1.0)
    if not record_valid(rec) or not isinstance(pg, dict) or not pg or not fin(cn) or cn <= 0 or not fin(sj) or sj <= 0:
        return False
    for h, v in pg.items():
        vals = [(v.get(k) or {}).get(g) for k in ("norm_d", "norm_fd", "norm_fd_five_point")]
        if any(not fin(x) for x in vals):
            return False
        if max(vals) / sj >= THRESH * cn:
            return False
    return True
def group_pass(rec, g):
    """The per-group decision RECOMPUTED from the recorded errors and Richardson witnesses (V192 item 4); the stored flag is only compared. Fails closed."""
    if not record_valid(rec):
        return False
    gp = (rec.get("group_pass") or {}).get(g)
    if not (isinstance(gp, dict) and "PASS" in gp):
        return False
    pg = rec.get("per_group") or {}
    for h, v in pg.items():
        vals = [(v.get(k) or {}).get(g) for k in ("norm_d", "norm_fd")]
        if any(not fin(x) for x in vals):
            return False
    return recompute_group(rec, g)["PASS"]
def load_addon(cname, record_path):
    """The (k) add-on record for the case, if present, derived from this record (input_record_sha256), naming the case and built on the record's gates.py (V198 item 1)."""
    ap = os.path.join(os.path.dirname(record_path), f"g1_step_addon_{cname}.json")
    if not os.path.exists(ap):
        return None, "no (k) add-on record"
    a = json.load(open(ap))
    import hashlib
    if a.get("input_record_sha256") != hashlib.sha256(open(record_path, "rb").read()).hexdigest():
        return None, f"add-on record {os.path.basename(ap)} was derived from another input record (hash mismatch)"
    if a.get("case") != cname:
        return None, f"add-on record names case {a.get('case')!r}, not {cname!r}"
    ah = str((a.get("code_sha256") or {}).get("validation/gates.py", ""))[:16]
    if not ah or ah != CURRENT_HARNESS["hash"] or ah not in V5C_HASHES:
        return None, f"add-on gates.py hash {ah!r} is not the record's v5c harness {CURRENT_HARNESS['hash']!r}"
    if not isinstance(a.get("jacobians"), dict):
        return None, "add-on record has no jacobians"
    if a.get("complete") is False or a.get("partial") is True:         # V202 item 3
        return None, "add-on record marked incomplete"
    for jn, jv in a["jacobians"].items():
        cols = (jv or {}).get("columns")
        if not isinstance(cols, dict) or (jv.get("n_columns_reevaluated") is not None and jv.get("n_columns_reevaluated") != len(cols)):
            return None, f"add-on jacobian {jn}: column count disagrees with its records"
        for ck, cr in cols.items():
            if not isinstance(cr, dict) or str(cr.get("column")) != str(ck) or cr.get("complete") is False:
                return None, f"add-on jacobian {jn}: column record {ck} missing, mislabelled or incomplete"
    return a, ""
def expected_k_labels(scale):
    labs = {f"{0.0:+.1e}"}
    for l in K_STEPS:
        h = float(l) * scale
        for t in (h, -h, 2 * h, -2 * h):
            labs.add(f"{t:+.1e}")
    return labs
def k_decision(addon, jac, col, g, needs_active):
    """V198 item 1: the (k) decision RECOMPUTED from the add-on's column_test witnesses at the two fresh steps; the stored PASS_k is only compared.
    Returns dict(PASS, INVALID, reason, ratio, richardson, agrees_with_stored)."""
    rec = ((addon.get("jacobians") or {}).get(jac) or {}).get("columns", {}).get(str(col)) if addon else None
    if not isinstance(rec, dict):
        return dict(PASS=False, INVALID=True, reason="column not re-evaluated in the add-on")
    t = rec.get("column_test")
    if not isinstance(t, dict) or rec.get("column") != col:
        return dict(PASS=False, INVALID=True, reason="add-on column record without column_test witnesses or with a different column id")
    sc = t.get("step_scale", 1.0)
    if not fin(sc) or sc <= 0 or abs(sc - float(rec.get("step_scale", sc))) > 1e-12 * max(1.0, sc):
        return dict(PASS=False, INVALID=True, reason="invalid or inconsistent step scale")
    if g is None:
        e2 = t.get("errors_second_order") or {}; e4 = t.get("errors_five_point") or {}; container = t; tau = TAU_ALL; stored = (rec.get("whole") or {}).get("PASS_k")
    else:
        pg = t.get("per_group") or {}
        e2 = {h: (v.get("second_order") or {}).get(g) for h, v in pg.items()}; e4 = {h: (v.get("five_point") or {}).get(g) for h, v in pg.items()}
        container = (t.get("group_pass") or {}).get(g); tau = TAU_GROUP; stored = ((rec.get("groups") or {}).get(g) or {}).get("PASS_k")
        if not isinstance(container, dict):
            return dict(PASS=False, INVALID=True, reason=f"group {g} absent from the add-on witnesses")
    if sorted(e2.keys()) != sorted(K_STEPS) or sorted(e4.keys()) != sorted(K_STEPS) or any(not fin(v) or v < 0 for v in list(e2.values()) + list(e4.values())):
        return dict(PASS=False, INVALID=True, reason="two-step error ladders incomplete or non-finite")
    if g is None:                                                      # V202 item 5: whole-column errors must equal per_group[step]['all']
        pg = t.get("per_group") or {}
        for l in K_STEPS:
            a2 = ((pg.get(l) or {}).get("second_order") or {}).get("all"); a4 = ((pg.get(l) or {}).get("five_point") or {}).get("all")
            if not fin(a2) or not fin(a4) or abs(a2 - e2[l]) > 1e-12 * max(1.0, e2[l]) or abs(a4 - e4[l]) > 1e-12 * max(1.0, e4[l]):
                return dict(PASS=False, INVALID=True, reason=f"add-on whole-column errors contradict per_group['all'] at step {l}")
    if needs_active:
        a = t.get("active_sets")
        if not isinstance(a, dict) or not t.get("active_set_base_recorded") or set(a.keys()) != expected_k_labels(sc):
            return dict(PASS=False, INVALID=True, reason="add-on active-set records (base and eight stencil points) missing or mislabelled")
        if len(set(json.dumps(v, sort_keys=True) for v in a.values())) != 1 or t.get("active_sets_identical") is not True:
            return dict(PASS=False, INVALID=True, reason="add-on active sets differ among the base and the stencil points")
    allp = container.get("richardson_all_pairs")
    if not isinstance(allp, dict) or list(allp.keys()) != [K_PAIR]:
        return dict(PASS=False, INVALID=True, reason="pair witness for 1e-02->1e-03 missing or mislabelled")
    w = allp[K_PAIR]; vals = [w.get(k) for k in ("norm_diff_scaled", "norm_d_scaled", "norm_R_scaled", "floor")]
    if any(not fin(x) or x < 0 for x in vals) or not fin(w.get("scale")) or w.get("scale") <= 0:
        return dict(PASS=False, INVALID=True, reason="pair witness norms missing, non-finite, negative or scale invalid")
    if abs(w["scale"] - sc) > 1e-12 * max(1.0, sc):                      # V202 item 4
        return dict(PASS=False, INVALID=True, reason=f"pair witness scale {w['scale']} differs from the column step scale {sc}")
    r = vals[0] / max(vals[1], vals[2], vals[3], 1e-300)
    both2 = all(e2[l] <= tau for l in K_STEPS); both4 = all(e4[l] <= tau for l in K_STEPS)
    ok = bool(both2 and both4 and r <= tau)
    ratio = (e2["1e-02"] / e2["1e-03"]) if e2["1e-03"] > 0 else None
    return dict(PASS=ok, INVALID=False, richardson=r, ratio=ratio, both_steps_second_order=both2, both_steps_five_point=both4, stored_PASS_k=stored, agrees_with_stored=(ok == bool(stored)))
K_CTX = {"needs_active": False, "invalid": []}
def k_pass(addon, jac, col, g=None):
    """(pass, ratio) of the recomputed (k) decision (k_decision); INVALID evidence counts as not passing and is collected in K_CTX['invalid']."""
    if not addon:
        return False, None
    d = k_decision(addon, jac, col, g, K_CTX["needs_active"])
    if d.get("INVALID"):
        K_CTX["invalid"].append(f"{col}:{g or 'all'}: {d.get('reason')}")
        return False, None
    return bool(d["PASS"]), d.get("ratio")
def main(files):
    for f in files:
        d = json.load(open(f)); entries = dict(d.get("cases", {}))
        CURRENT_HARNESS["hash"] = str((d.get("code_sha256") or {}).get("validation/gates.py", ""))[:16]
        for k, v in d.items():
            if isinstance(v, dict) and v.get("partial") and k not in entries:
                entries[k] = v
        report = dict(source=os.path.relpath(f), label=LABEL, threshold_small_amplitude=THRESH, min_coefficient_coverage=MIN_COEF, harness_gates_py=CURRENT_HARNESS["hash"],
                      harness_salvage=SALVAGE_HARNESS_HASHES.get(CURRENT_HARNESS["hash"], "v5c or later" if CURRENT_HARNESS["hash"] else "unknown"), cases={}, parameter_source={})
        # V202 item 2: provenance is set here from the record file itself; any _source_gates_py in the input is overwritten
        for cname, c in list(entries.items()):
            for jac, pkey, ckey in JACS:
                for v in (c.get(pkey) or {}).values():
                    if isinstance(v, dict):
                        v["_source_gates_py"] = CURRENT_HARNESS["hash"]
                for e in ((c.get(ckey) or {}).get("results") or []):
                    r = col_record(e, jac)
                    if isinstance(r, dict):
                        r["_source_gates_py"] = CURRENT_HARNESS["hash"]
        # v8: coefficient-only records take their parameter columns from the companion G1 record of the case
        for cname, c in list(entries.items()):
            if any(k in c for k in ("G1_Jf_param_columns", "G1_Jcw_param_columns", "G1_Jc_param_columns")):
                continue
            for cand in (f"gates_gpu_v1_{cname}_G1v4.json", f"gates_gpu_v1_{cname}.json"):
                cp = os.path.join(os.path.dirname(f), cand)
                if os.path.exists(cp) and os.path.abspath(cp) != os.path.abspath(f):
                    dd = json.load(open(cp)); ce = dict(dd.get("cases", {}))
                    for k, v in dd.items():
                        if isinstance(v, dict) and v.get("partial") and k not in ce:
                            ce[k] = v
                    comp = ce.get(cname)
                    if comp and "G1_Jf_param_columns" in comp:
                        src_hash = str((dd.get("code_sha256") or {}).get("validation/gates.py", ""))[:16]
                        for key in ("G1_Jf_param_columns", "G1_Jcw_param_columns", "G1_Jc_param_columns", "G1_coefficient_columns_drawn"):
                            if key in comp and key not in c:
                                c[key] = comp[key]
                                if key != "G1_coefficient_columns_drawn":
                                    for v in c[key].values():                       # the companion file's gates.py hash governs its records (V198 item 4)
                                        if isinstance(v, dict):
                                            v["_source_gates_py"] = src_hash
                        import hashlib as _hl
                        report["parameter_source"][cname] = dict(file=cand, file_sha256=_hl.sha256(open(cp, "rb").read()).hexdigest(), gates_py=src_hash, note="parameter columns taken from the companion G1 record (harness v4 parameter records decide; lead 07:18Z)")
                        break
        for cname, c in entries.items():
            cres = {}
            for jac, pkey, ckey in JACS:
                pc = c.get(pkey) or {}; cc = (c.get(ckey) or {}).get("results") or []
                expected_params = ["optimizer:z_c", "optimizer:z_w", "physical:c_l", "physical:omega"]
                missing_params = [k for k in expected_params if k not in pc]
                groups = set()
                for v in pc.values():
                    groups |= set((v.get("group_pass") or {}).keys())
                for e in cc:
                    groups |= set((col_record(e, jac).get("group_pass") or {}).keys())
                groups.discard("all")
                # completeness schema (V190) and the registered outcome, distinguishing INVALID evidence from a numerical FAIL
                needs_active = jac in ("Jcw", "Jc")                     # J_f: frozen weights, no changing active set (declared frozen convention)
                groups_req = sorted(groups)
                comp_param = {k: record_complete(v, groups_req, needs_active) for k, v in pc.items()}
                comp_coef = {col_id(e, jac): record_complete(col_record(e, jac), groups_req, needs_active) for e in cc}
                ids = [col_id(e, jac) for e in cc]; distinct = len(set(ids))
                drawn = c.get("G1_coefficient_columns_drawn"); listed = (c.get(ckey) or {}).get("columns")
                ids_match = (drawn is not None and sorted(set(ids)) == sorted(drawn)) and (listed is None or sorted(listed) == sorted(drawn))
                rejudge = {k: rejudge_physical_omega(v) for k, v in pc.items() if k == "physical:omega"}
                recomputed = {}
                def reg_state(k, v, comp):
                    ok, why = comp
                    if not ok:
                        return "INVALID: " + why
                    if k == "physical:omega" and rejudge.get(k, {}).get("status") not in (None, "NOT_APPLICABLE"):
                        return "REJUDGED_" + rejudge[k]["status"] + " (harness v3/v4 scaled the physical derivative by omega; physical-unit decision from witnesses)"
                    rw = recompute_whole(v); rg = {g: recompute_group(v, g) for g in REQUIRED_GROUPS}
                    recomputed[k if k is not None else v.get("column")] = dict(whole=rw, groups=rg)
                    if rw.get("INVALID") or any(x.get("INVALID") for x in rg.values()):
                        return "INVALID: " + str(rw.get("reason") or next((x.get("reason") for x in rg.values() if x.get("INVALID")), "pair evidence"))
                    allok = rw["PASS"] and all(x["PASS"] for x in rg.values())
                    return "PASS" if allok else "FAIL"
                reg_param = {k: reg_state(k, v, comp_param[k]) for k, v in pc.items()}
                reg_coef = {col_id(e, jac): reg_state(None, col_record(e, jac), comp_coef[col_id(e, jac)]) for e in cc}
                registered = dict(parameter_columns=reg_param, coefficient_columns=reg_coef, n_coefficient_records=len(cc), n_distinct_coefficient_columns=distinct,
                                  coefficient_count_as_registered=(distinct == N_COEF and len(ids) == N_COEF), ids_match_drawn=ids_match, drawn_columns=drawn, missing_parameter_columns=missing_params, recomputed_decisions=recomputed,
                                  physical_omega_rejudgement=rejudge.get("physical:omega"),
                                  PASS=(not missing_params) and distinct == N_COEF and len(ids) == N_COEF and bool(ids_match) and all(v in ("PASS",) or str(v).startswith("REJUDGED_PASS") for v in reg_param.values()) and all(v == "PASS" for v in reg_coef.values()),
                                  INVALID=any(str(v).startswith("INVALID") or str(v).startswith("REJUDGED_RECOMPUTE") or str(v).startswith("REJUDGED_INVALID") for v in list(reg_param.values()) + list(reg_coef.values())) or bool(missing_params) or distinct != N_COEF or len(ids) != N_COEF or not ids_match)
                records_v2 = bool(cc) and all(isinstance(col_record(e, jac).get("per_group"), dict) for e in cc)
                if not records_v2:
                    cres[jac] = dict(registered=registered, amended=dict(status="RECORDS_INSUFFICIENT", reason="compact v1 coefficient records: per-group norms absent"), label=LABEL)
                    continue
                # amended outcome
                whole_param = {k: bool(record_valid(v) and comp_param[k][0] and (recompute_whole(v)["PASS"] or str(reg_param.get(k, "")).startswith("REJUDGED_PASS")) and all(recompute_group(v, g)["PASS"] for g in REQUIRED_GROUPS)) for k, v in pc.items()}   # recomputed (V192 item 4)
                whole_coef = {}
                for e in cc:
                    r = col_record(e, jac)
                    whole_coef[col_id(e, jac)] = bool(record_valid(r) and comp_coef[col_id(e, jac)][0] and recompute_whole(r)["PASS"])
                gres = {}
                for g in sorted(groups):
                    par_fail = [k for k in expected_params if k in pc and not group_pass(pc[k], g)] + [k for k in missing_params]
                    sa, pass_cols, fail_cols, inv_cols = [], [], [], []
                    seen = set()
                    for e in cc:
                        r = col_record(e, jac); k = col_id(e, jac)
                        if k in seen:
                            continue
                        seen.add(k)
                        if not comp_coef[k][0] or recompute_group(r, g).get("INVALID") or recompute_whole(r).get("INVALID"):   # V198 item 3: invalid evidence is never excluded as small-amplitude
                            inv_cols.append(k); continue
                        if small_amplitude(r, g):
                            sa.append(k); continue
                        (pass_cols if group_pass(r, g) else fail_cols).append(k)
                    par_inv = [k for k in expected_params if k in pc and (not comp_param[k][0] or recompute_group(pc[k], g).get("INVALID") or str(reg_param.get(k, "")).startswith("INVALID") or str(reg_param.get(k, "")).startswith("REJUDGED_INVALID"))]
                    status = "INVALID" if (inv_cols or par_inv) else ("PASS" if (not par_fail and not fail_cols and len(set(pass_cols)) >= MIN_COEF) else "OPEN")
                    gres[g] = dict(status=status, parameter_columns_failing_or_missing=par_fail, coefficient_columns_invalid_evidence=inv_cols, parameter_columns_invalid_evidence=par_inv, coefficient_columns_passing=pass_cols, coefficient_columns_failing_not_small_amplitude=fail_cols,
                                   coefficient_columns_small_amplitude_not_tested=sa, n_coverage_distinct=len(set(pass_cols)))
                complete_all = all(c[0] for c in comp_param.values()) and all(c[0] for c in comp_coef.values()) and not missing_params and distinct == N_COEF and len(ids) == N_COEF
                incomplete = {k: c[1] for k, c in list(comp_param.items()) + list(comp_coef.items()) if not c[0]}
                phys_ok = all(v.get("status") in (None, "NOT_APPLICABLE", "PASS") for v in rejudge.values())
                amended_pass = complete_all and bool(ids_match) and phys_ok and all(whole_param.values()) and all(whole_coef.values()) and bool(gres) and all(v["status"] == "PASS" for v in gres.values())
                evidence_invalid = any(str(v).startswith("INVALID") or str(v).startswith("REJUDGED_INVALID") or str(v).startswith("REJUDGED_RECOMPUTE") for v in list(reg_param.values()) + list(reg_coef.values())) or any(v["status"] == "INVALID" for v in gres.values())
                amended_pass = amended_pass and not evidence_invalid
                amended_status = "PASS" if amended_pass else ("INVALID (incomplete, ids not the drawn columns, invalid pair evidence, or re-judgement pending)" if (not complete_all or not phys_ok or not ids_match or evidence_invalid) else "OPEN")
                # ---- SPEC v1.18 3.6 (k): registered outcome with the post-result step rule, and with (k) and (j) together
                addon, addon_note = load_addon(cname, f)
                K_CTX["needs_active"] = needs_active; K_CTX["invalid"] = []
                if addon is None and addon_note != "no (k) add-on record":        # V205: a present but rejected add-on makes the (k) outcomes INVALID, never "as absent"
                    K_CTX["invalid"].append("add-on present but rejected: " + addon_note)
                k_cols = {}; k_fail = []; k_ratios = {}; reg_failing_cols = []
                for e in cc:
                    r = col_record(e, jac); k = col_id(e, jac)
                    rw = recompute_whole(r); rg = {g: recompute_group(r, g) for g in REQUIRED_GROUPS}
                    if not (rw.get("PASS") and all(x.get("PASS") for x in rg.values())):
                        reg_failing_cols.append(k)
                    if rw.get("INVALID") or any(x.get("INVALID") for x in rg.values()):
                        K_CTX["invalid"].append(f"{k}: invalid registered pair evidence")
                    ok_whole = rw.get("PASS") or (k_pass(addon, jac, k)[0] if comp_coef.get(k, (False, ""))[0] else False)
                    groups_ok = {}
                    for g in REQUIRED_GROUPS:
                        if rg[g].get("PASS"):
                            groups_ok[g] = "registered"
                        else:
                            pk, ratio = k_pass(addon, jac, k, g)
                            groups_ok[g] = "pass under the post-result step rule (k)" if pk else "FAIL"
                            if pk:
                                k_ratios[f"{k}:{g}"] = ratio
                    passed = bool(comp_coef.get(k, (False, ""))[0]) and ok_whole and all(v != "FAIL" for v in groups_ok.values())
                    k_cols[k] = dict(PASS=passed, whole="registered" if rw.get("PASS") else ("pass under the post-result step rule (k)" if ok_whole else "FAIL"), groups=groups_ok)
                    if not passed:
                        k_fail.append(k)
                params_ok = (not missing_params) and all(v in ("PASS",) or str(v).startswith("REJUDGED_PASS") for v in reg_param.values())
                addon_cols = set(int(x) for x in (((addon or {}).get("jacobians") or {}).get(jac) or {}).get("columns", {}).keys()) if addon else set()
                addon_incomplete = bool(reg_failing_cols) and addon is not None and not set(reg_failing_cols) <= addon_cols
                if addon_incomplete:
                    K_CTX["invalid"].append(f"add-on does not cover the registered failing columns {sorted(set(reg_failing_cols) - addon_cols)}")
                k_invalid = bool(K_CTX["invalid"]) or registered["INVALID"] or distinct != N_COEF or len(ids) != N_COEF or not ids_match
                with_k = dict(status=("PASS" if (params_ok and ids_match and distinct == N_COEF and len(ids) == N_COEF and not k_fail and not k_invalid and all(c[0] for c in comp_coef.values())) else ("INVALID" if k_invalid else "FAIL")),
                              invalid_evidence=list(K_CTX["invalid"]), registered_failing_columns=sorted(set(reg_failing_cols)), addon_columns=sorted(addon_cols),
                              failing_columns=k_fail, columns=k_cols, error_ratios_1e2_over_1e3=k_ratios, addon=(None if addon is None else os.path.basename(os.path.join(os.path.dirname(f), f"g1_step_addon_{cname}.json"))), addon_note=addon_note,
                              label="registered rule with the post-result step rule (k) (SPEC v1.18 3.6 (k))")
                # (k) and (j): small-amplitude groups excluded as in the amended outcome, the remaining failures may pass under (k)
                kj_groups = {}
                for g, gv in gres.items():
                    fails = [k for k in gv["coefficient_columns_failing_not_small_amplitude"] if not k_pass(addon, jac, k, g)[0]]
                    passes_k = [k for k in gv["coefficient_columns_failing_not_small_amplitude"] if k_pass(addon, jac, k, g)[0]]
                    cov = len(set(gv["coefficient_columns_passing"]) | set(passes_k))
                    kj_groups[g] = dict(status=("INVALID" if gv["status"] == "INVALID" else ("PASS" if (not gv["parameter_columns_failing_or_missing"] and not fails and cov >= MIN_COEF) else "OPEN")), failing=fails, pass_under_k=passes_k, coverage=cov, small_amplitude_not_tested=gv["coefficient_columns_small_amplitude_not_tested"])
                with_kj = dict(status=("PASS" if (complete_all and ids_match and phys_ok and not evidence_invalid and not k_invalid and all(whole_param.values()) and all((whole_coef[k] or k_pass(addon, jac, k)[0]) for k in whole_coef) and bool(kj_groups) and all(v["status"] == "PASS" for v in kj_groups.values())) else ("INVALID" if (not (complete_all and ids_match and phys_ok) or evidence_invalid or k_invalid or any(v["status"] == "INVALID" for v in kj_groups.values())) else "OPEN")),
                               invalid_evidence=list(K_CTX["invalid"]), groups=kj_groups, label="post-result rules (k) and (j) together (SPEC v1.18 3.6 (k) (7))")
                cres[jac] = dict(registered=registered, with_k=with_k, with_k_and_j=with_kj, amended=dict(status=amended_status, incomplete_records=incomplete, whole_column_parameter=whole_param, whole_column_coefficient=whole_coef, missing_parameter_columns=missing_params, groups=gres,
                                                                     resolved_coverage_counts={g: v["n_coverage_distinct"] for g, v in gres.items()}), label=LABEL)
            report["cases"][cname] = cres
        outp = f[:-5] + "_coverage.json"; json.dump(report, open(outp, "w"), indent=1)
        print(f"\n### {os.path.basename(f)} -> {os.path.basename(outp)} ({LABEL})")
        for cname, cres in report["cases"].items():
            for jac, v in cres.items():
                am = v["amended"]
                rg = v["registered"]; npass = sum(1 for x in rg["coefficient_columns"].values() if x == "PASS")
                wk = v.get("with_k") or {}; wkj = v.get("with_k_and_j") or {}
                print(f"- {cname} {jac}: registered {'PASS' if rg['PASS'] else ('INVALID' if rg.get('INVALID') else 'FAIL')} ({npass}/{rg['n_distinct_coefficient_columns']} distinct coefficient columns PASS; parameters {rg['parameter_columns']}); with (k): {wk.get('status')} (failing {wk.get('failing_columns')}; {wk.get('addon_note') or wk.get('addon')}); with (k)+(j): {wkj.get('status')}; amended (j) only: {am.get('status')}" + (f" ({am.get('reason')})" if am.get("reason") else "") + (f"; incomplete: {am.get('incomplete_records')}" if am.get("incomplete_records") else ""))
                for g, gv in (am.get("groups") or {}).items():
                    print(f"    - {g}: {gv['status']}; coverage {gv['n_coverage_distinct']} distinct columns {gv['coefficient_columns_passing']}; failing (not small-amplitude) {gv['coefficient_columns_failing_not_small_amplitude']}; small-amplitude (not tested) {gv['coefficient_columns_small_amplitude_not_tested']}; parameter columns failing or missing {gv['parameter_columns_failing_or_missing']}")
if __name__ == "__main__":
    main([f for a in sys.argv[1:] for f in glob.glob(a) if not (f.endswith("_label.json") or f.endswith("_coverage.json") or f.endswith("_flags.json"))])
