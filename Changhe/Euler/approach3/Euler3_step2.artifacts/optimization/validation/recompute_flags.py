"""D6FP (lead 23:24Z item 3): recompute the absolute-only flag of EXISTING gate and add-on files from their saved values as PASS (with the
floor F, the registered decision) and not PASS_rel (F = 0, same rule including Richardson). Scalar tests (gates G3 entries, g3_addon outcomes):
second-order values D_h are saved, five-point values are not in the old files, so |D4 - d| is backed out from e4 * max(|d|, |D4|, F) with |D4|
bounded by |d| +- |D4 - d| (conservative, as in the lead's analysis/g3_relative_recheck.py). Column tests: the old files saved only e and a
per-step 'absolute_only' = (F > max(||d||, ||D_h||)); when that is False at both steps of the passing pair, the F = 0 error equals the saved
error and PASS_rel is determined; otherwise it is undetermined (rerun on the frozen snapshot decides). Files written: <name>_flags.json."""
import sys, os, json, glob
TAU = 1e-6
def rule_scalar(e2, e4, D2, d, hs, valid, F, tau):
    hs = sorted(hs, reverse=True)
    pairs = [(hs[i], hs[i + 1]) for i in range(len(hs) - 1) if valid.get(hs[i], True) and valid.get(hs[i + 1], True)]
    ok2 = any(e2[a] <= tau and e2[b] <= tau for a, b in pairs); ok4 = any(e4[a] <= tau and e4[b] <= tau for a, b in pairs)
    rich = None
    for a, b in pairs:
        if e2[a] <= tau and e2[b] <= tau:
            R = D2[b] + (D2[b] - D2[a]) / 99.0; rich = abs(R - d) / max(abs(d), abs(R), F); break
    return dict(pass2=ok2, pass4=ok4, rich=rich, PASS=bool(pairs) and ok2 and ok4 and rich is not None and rich <= tau)
def e4_F0_conservative(e4F, d, F):
    cand = []
    for s_ in (+1, -1):
        x = e4F * max(abs(d), F)
        for _ in range(60):
            x = e4F * max(abs(d), abs(d) + s_ * x, F)
        den = max(abs(d), abs(d) + s_ * x) if abs(d) + s_ * x > 0 else abs(d)
        cand.append(x / max(den, 1e-300))
    return max(cand)
def scalar_entry(ov, d, F, tau=TAU):
    keys = list(ov["fd_values"].keys()); hs = [float(k) for k in keys]
    D2 = {float(k): ov["fd_values"][k] for k in keys}
    valid = {float(k): ov["step_valid"][k] for k in keys} if "step_valid" in ov else {h: True for h in hs}
    e2F = {float(k): ov["errors_second_order"][k] for k in keys}; e4F = {float(k): ov["errors_five_point"][k] for k in keys}
    e2_0 = {h: abs(D2[h] - d) / max(abs(d), abs(D2[h]), 1e-300) for h in hs}
    if "fd_values_five_point" in ov:
        D4 = {float(k): ov["fd_values_five_point"][k] for k in keys}; e4_0 = {h: abs(D4[h] - d) / max(abs(d), abs(D4[h]), 1e-300) for h in hs}; cons = False
    else:
        e4_0 = {h: e4_F0_conservative(e4F[h], d, F) for h in hs}; cons = True
    rF = rule_scalar(e2F, e4F, D2, d, hs, valid, F, tau); r0 = rule_scalar(e2_0, e4_0, D2, d, hs, valid, 0.0, tau)
    return dict(PASS_with_floor=rF["PASS"], PASS_rel_F0=r0["PASS"], absolute_only_SPEC=bool(rF["PASS"] and not r0["PASS"]), flag_in_file=ov.get("absolute_only"), PASS_in_file=ov.get("PASS"),
                richardson_F0=r0["rich"], five_point_F0_conservative=cons)
def column_entry(t):
    """t: a column_test record. PASS_rel determinable when the floor was below the norms at the steps of the passing pair of every group."""
    if "PASS_rel" in t:
        return dict(PASS=t["PASS"], PASS_rel=t["PASS_rel"], absolute_only_SPEC=t["absolute_only"], determined=True, source="file (new format)")
    pg = t.get("per_group") or {}
    hs = sorted(pg.keys(), key=lambda k: -float(k))
    undetermined = []
    for g, gp in (t.get("group_pass") or {}).items():
        e = [pg[h]["second_order"].get(g) for h in hs]; flags = [(pg[h].get("absolute_only") or {}).get(g) for h in hs]
        for i in range(len(hs) - 1):
            if e[i] is not None and e[i + 1] is not None and e[i] <= (1e-6 if g == "all" else 1e-5) and e[i + 1] <= (1e-6 if g == "all" else 1e-5):
                if flags[i] or flags[i + 1]:
                    undetermined.append(g)
                break
    if undetermined:
        return dict(PASS=t["PASS"], PASS_rel=None, absolute_only_SPEC=None, determined=False, groups_floor_active_at_passing_pair=undetermined)
    return dict(PASS=t["PASS"], PASS_rel=t["PASS"], absolute_only_SPEC=False, determined=True, source="floor below the norms at the passing pair of every group (F = 0 errors equal the saved errors)")
def process_gates(path):
    d = json.load(open(path)); out = dict(source=path, cases={})
    for cname, case in (d.get("cases") or d).items() if isinstance(d.get("cases"), dict) else [(d.get("name", "case"), d)]:
        if not isinstance(case, dict):
            continue
        rec = dict(G3={}, columns={})
        for k, v in (case.get("G3") or {}).items():
            if isinstance(v, dict) and "fd_values" in v:
                rec["G3"][k] = scalar_entry(v, v["derivative_complete"], v.get("floor", 0.0))
        for sect in ("G1_Jf_param_columns", "G1_Jcw_param_columns", "G1_Jc_param_columns"):
            for k, v in (case.get(sect) or {}).items():
                if isinstance(v, dict) and "per_group" in v:
                    rec["columns"][f"{sect}:{k}"] = column_entry(v)
        out["cases"][cname] = rec
    return out
def process_addon(path):
    src = json.load(open(path)); out = dict(source=path, cases={})
    cases = src.get("cases") or ({src.get("name", os.path.basename(path)): src} if "directions" in src else {})
    for cname, cv in cases.items():
        od = {}
        for dn, dv in (cv.get("directions") or {}).items():
            d = dv["derivative_complete"]; F = dv["floor"]
            od[dn] = {on: scalar_entry(ov, d, F) for on, ov in dv["outcomes"].items()}
        out["cases"][cname] = od
    return out
if __name__ == "__main__":
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    files = sys.argv[1:] or (glob.glob(os.path.join(root, "gates_*.json")) + glob.glob(os.path.join(root, "g3_addon_*.json")))
    for f in files:
        if f.endswith("_flags.json"):
            continue
        try:
            res = process_addon(f) if os.path.basename(f).startswith("g3_addon") else process_gates(f)
        except Exception as e:
            print(f"{os.path.basename(f)}: FAILED {e!r}"); continue
        outp = f[:-5] + "_flags.json"; json.dump(res, open(outp, "w"), indent=1)
        n_abs = 0; n_tot = 0; n_und = 0
        for cv in res["cases"].values():
            for sect in cv.values() if isinstance(cv, dict) else []:
                for v in (sect.values() if isinstance(sect, dict) else []):
                    if isinstance(v, dict) and "absolute_only_SPEC" in v:
                        n_tot += 1; n_abs += bool(v["absolute_only_SPEC"]); n_und += (v["absolute_only_SPEC"] is None)
                    elif isinstance(v, dict):
                        for vv in v.values():
                            if isinstance(vv, dict) and "absolute_only_SPEC" in vv:
                                n_tot += 1; n_abs += bool(vv["absolute_only_SPEC"]); n_und += (vv["absolute_only_SPEC"] is None)
        print(f"{os.path.basename(f)}: {n_tot} outcomes, absolute-only (SPEC) {n_abs}, undetermined {n_und} -> {os.path.basename(outp)}")
