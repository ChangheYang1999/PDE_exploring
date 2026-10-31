#!/usr/bin/env python3
"""8.6 ranking table for the Phase III branch selection (lead tool, plain Python, reads only). v2: candidates without an end battery are listed as pending.
v3 (after V672): the 7.3b condition (ii) uses the core-resolved sets of v1.21 (b), as the registered text requires:
  sigma_u_max_core (max over both shell families and the added core sets), sigma_Om (global, unchanged by v1.21 (b)),
  a_max_core and a_max_core_upper (max over both shell families and the added core sets, centre and upper weight; both
  must pass). A pair is not ordered if either state lacks a quantity or has core_resolved not true (the quadrature
  doubling part of v1.21 (c)). The L2 to L3 part of v1.21 (c) is OPEN in this campaign (SPEC 6.2); every "ahead" is
  conditional on it.

Input: a JSON list of candidate ends (default notes/ranking_candidates.json), each
  {"name": ..., "run": <run directory under the numerics runs/>, "record": <validation/records_63a tag or null>,
   "independent": {"rho_std": x, "rho_half": y, "source": "V..."} or null,
   "core_ball_rms": {"value": v, "source": "V..."} or null, "lineage": ..., "branch_pair_results": [...]}
Per candidate, from the run's last start_result in results.jsonl (the worker's end battery):
  holdout rho_u^max on the standard and the half-offset shell family, sigma_u^max, sigma_Om, a_max (dyadic shells),
  a_max_core and a_max_core_upper, O1, parameters, iterations; from the 6.3 (a) record: any_exclusion, the raised (b)
  flags, the record version and whether the tool is admitted (ADMITTED_TOOL.txt present).
Ranking quantity: holdout rho_u^max, the independent value where one exists (verifier), else the primary value.
Ordering rule (previous campaign 7.3b, SPEC 8.6): X is ahead of Y only if X has the lower ranking rho_u^max on both
families and each of X's sigma_u^max, sigma_Om and a_max exceeds Y's by at most 10 per cent; otherwise the pair is not
ordered. States with a raised 6.3 (a) exclusion are excluded (lead 20:22:14Z item 3 (c)); open 6.3 (b) flags are shown.
Rank order: by the ranking rho_u^max on the standard family (consistent with the rule: X ahead of Y implies a lower value).
Output: artifacts/ranking/<tag>.json and <tag>.md. Numerics, not a proof."""
import json, os, sys, time, hashlib, argparse

NUM = "<optimization tree>"
OUT = "<analysis tree>/artifacts/ranking"


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def end_result(run):
    p = os.path.join(NUM, "runs", run, "results.jsonl")
    recs = [json.loads(l) for l in open(p) if l.strip()]
    recs = [r for r in recs if r.get("kind") == "start_result"]
    if not recs:
        raise SystemExit(f"no start_result in {p}")
    return recs[-1], sha(p)


def record_info(tag):
    if not tag:
        return dict(status="no 6.3 (a) record")
    p = os.path.join(NUM, "validation", "records_63a", tag + ".json")
    if not os.path.isfile(p):
        return dict(status="record missing", path=p)
    d = json.load(open(p))
    def raised(lst):   # one entry per item; a record can evaluate an item against several start references
        out = {}
        for f in lst:
            if f.get("raised"):
                out.setdefault(f["item"], []).append(str(f.get("reference")))
        return [it + " [ref " + ", ".join(refs) + "]" for it, refs in out.items()]
    flags = raised(d.get("flags_6_3b", []))
    excl = raised(d.get("exclusions_6_3a", []))
    adm_p = os.path.join(NUM, "validation", "records_63a", "ADMITTED_TOOL.txt")
    adm = [l.split()[0] for l in open(adm_p) if l.strip()] if os.path.isfile(adm_p) else []
    admitted = d.get("script_sha256") in adm   # the record was written by the admitted producer (not the wrapper's answer)
    refs = d.get("start_reference")
    refs = refs if isinstance(refs, list) else [refs]
    ref_versions = []
    for r in refs:
        t = r.get("tag") if isinstance(r, dict) else r
        rp = os.path.join(NUM, "validation", "records_63a", f"{t}.json") if t else None
        ref_versions.append(f"{t}:{json.load(open(rp)).get('version')}" if rp and os.path.isfile(rp) else f"{t}:?")
    return dict(status="read", tag=tag, version=d.get("version"), sha256=sha(p), any_exclusion=d.get("any_exclusion"), exclusions=excl,
                open=d.get("open"), flags=flags, registered_clearance_6_3a=d.get("registered_clearance_6_3a"), tool_admitted=admitted,
                producer_sha256=d.get("script_sha256"), start_reference_versions=ref_versions)


def ahead(x, y, tol=0.10):
    """(bool, reason): x ahead of y under the 7.3b ordering."""
    if not (x["rho_std"] < y["rho_std"] and x["rho_half"] < y["rho_half"]):
        return False, "rho_u^max not lower on both families"
    for s in (x, y):
        if s.get("core_resolved") is not True:
            return False, f"core resolution not recorded as true for {s['name']}"
    for k in ("sigma_u_max_core", "sigma_Om", "a_max_core", "a_max_core_upper"):
        if x.get(k) is None or y.get(k) is None:
            return False, f"{k} missing"
        if x[k] > (1.0 + tol) * y[k]:
            return False, f"{k} {x[k]:.4g} exceeds {(1 + tol):.2f} x {y[k]:.4g}"
    return True, "ahead"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidates", default="<analysis tree>/notes/ranking_candidates.json")
    ap.add_argument("--tag", required=True)
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    C = json.load(open(a.candidates))
    rows = []
    pending = []
    for c in C:
        try:
            r, rsha = end_result(c["run"])
        except (SystemExit, FileNotFoundError) as e:   # v2: a run without an end battery yet is listed as pending, not ranked
            pending.append(dict(name=c["name"], run=c["run"], reason=str(e)))
            continue
        ind = c.get("independent") or None
        row = dict(name=c["name"], lineage=c.get("lineage"), run=c["run"], results_sha256=rsha, it=r.get("n_accepted"), it_cum=len(r.get("trajectory") or []),
                   c_l=r.get("c_l"), omega=r.get("omega"), O1=r.get("cost_final"),
                   rho_std_primary=r.get("rho_u_max_holdout"), rho_half_primary=r.get("rho_u_max_holdout_half"),
                   sigma_u_max=r.get("sigma_u_max"), sigma_Om=r.get("sigma_Om"), a_max=r.get("a_max"),
                   a_max_core=r.get("a_max_core"), a_max_core_upper=r.get("a_max_core_upper"),
                   sigma_u_max_core=r.get("sigma_u_max_core"), core_resolved=r.get("core_resolved"), core_doubling_change_max=r.get("core_doubling_change_max"),
                   core_ball_rms=(c.get("core_ball_rms") or {}).get("value"), core_ball_rms_source=(c.get("core_ball_rms") or {}).get("source"),
                   independent=ind, record=record_info(c.get("record")))
        if ind and ind.get("rho_std") is not None and ind.get("rho_half") is not None:
            row["rho_std"], row["rho_half"], row["rho_source"] = float(ind["rho_std"]), float(ind["rho_half"]), "independent (" + str(ind.get("source")) + ")"
        else:
            row["rho_std"], row["rho_half"], row["rho_source"] = row["rho_std_primary"], row["rho_half_primary"], "primary (worker end battery)"
        rec = row["record"]
        row["excluded"] = bool(rec.get("any_exclusion")) if rec.get("status") == "read" else None
        rows.append(row)
    ranked = sorted([x for x in rows if x["excluded"] is not True], key=lambda x: x["rho_std"])
    excluded = [x for x in rows if x["excluded"] is True]
    pairs = []
    for i, x in enumerate(ranked):
        for y in ranked[i + 1:]:
            f, why = ahead(x, y); b, whyb = ahead(y, x)
            pairs.append(dict(x=x["name"], y=y["name"], x_ahead=f, reason=why, y_ahead=b, reason_reverse=whyb,
                              relation=("x ahead of y" if f else ("y ahead of x" if b else "not ordered"))))
    rec = dict(kind="8.6 ranking table (lead tool)", tag=a.tag, candidates_file=a.candidates, candidates_sha256=sha(a.candidates),
               rule="7.3b of the previous campaign (SPEC 8.6) with the core-resolved sets of v1.21 (b): lower rho_u^max on both families and sigma_u^max (core-resolved), sigma_Om, a_max (core-resolved, centre and upper weight) within +10 per cent; core_resolved true for both; L2 to L3 part of v1.21 (c) OPEN",
               ranked=ranked, excluded=excluded, pending=pending, pairs=pairs, script_sha256=sha(os.path.abspath(__file__)),
               ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    jp = os.path.join(OUT, a.tag + ".json")
    if os.path.exists(jp):
        raise FileExistsError(jp)
    json.dump(rec, open(jp, "x"), indent=1)
    L = [f"# Ranking table {a.tag} ({rec['ts']})", "",
         "| rank | state | (c_l, omega) | it | rho std | rho half | source | sigma_u^max dyadic / core-resolved | sigma_Om | a_max dyadic | a_max core-resolved centre / upper | core resolved (doubling change) | 6.3 record | open 6.3 (b) flags |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for k, x in enumerate(ranked, 1):
        r_ = x["record"]
        rs = (f"{r_.get('version')} ({'admitted producer' if r_.get('tool_admitted') else 'producer not admitted'}; refs {', '.join(r_.get('start_reference_versions') or [])}), exclusion {r_.get('any_exclusion')}" if r_.get("status") == "read" else r_.get("status"))
        fl = "; ".join(f.replace("top two radial coefficients of block ", "top2 ").replace(" above 0.1 of the block maximum", "") for f in (r_.get("flags") or [])) or "none"
        cb = (f"{x['core_ball_rms']:.4g} ({x['core_ball_rms_source']})" if x["core_ball_rms"] is not None else "not computed")
        L.append(f"| {k} | {x['name']} | ({x['c_l']:.6f}, {x['omega']:.6f}) | {x['it']} | {x['rho_std']:.5f} | {x['rho_half']:.5f} | {x['rho_source']} | "
                 f"{x['sigma_u_max']:.4f} / {x['sigma_u_max_core']:.4f} | {x['sigma_Om']:.4f} | {x['a_max']:.4f} | {x['a_max_core']:.4f} / {x['a_max_core_upper']:.4f} | {x['core_resolved']} ({x['core_doubling_change_max']:.2g}) | {rs} | {fl} |")
    if excluded:
        L += ["", "Excluded (raised 6.3 (a)): " + ", ".join(f"{x['name']} ({'; '.join(x['record']['exclusions'])})" for x in excluded)]
    if pending:
        L += ["", "Pending (no end battery yet): " + ", ".join(x["name"] for x in pending)]
    L += ["", "Pairs (7.3b ordering with the core-resolved sets; conditional on the OPEN L2 to L3 part of v1.21 (c)):", ""] + [f"- {p['x']} vs {p['y']}: {p['relation']} ({p['reason'] if p['relation'] != 'y ahead of x' else p['reason_reverse']})" for p in pairs]
    open(os.path.join(OUT, a.tag + ".md"), "x").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
