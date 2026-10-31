#!/usr/bin/env python
"""Summarize g3_addon records: per case, per estimator and ladder, the pass counts with flags.

Usage: python validation/g3_addon_summary.py validation/g3_addon_gpu_v1_<case>.json [...]
Flags per direction and estimator/ladder: PASS (relative rule), PASS_rel, absolute_only, FAIL, OPEN.
"""
import json, sys, os

def flag(o):
    if o.get("OPEN"):
        return "OPEN"
    if o.get("PASS"):
        return "PASS(abs_only)" if o.get("absolute_only") else "PASS"
    if o.get("PASS_rel"):
        return "PASS_rel"
    return "FAIL"

def main(paths):
    for p in paths:
        d = json.load(open(p))
        case = d.get("case")
        dirs = d.get("directions", {})
        keys = None
        print(f"== {case}  ({os.path.basename(p)}; n_opt {d.get('n_opt')}, cost {d.get('cost'):.4e}, directions {len(dirs)})")
        totals = {}
        for name, rec in dirs.items():
            outs = rec.get("outcomes", {})
            if keys is None:
                keys = list(outs.keys())
            row = []
            for k in keys:
                o = outs.get(k, {})
                f = flag(o)
                t = totals.setdefault(k, {"PASS": 0, "PASS(abs_only)": 0, "PASS_rel": 0, "FAIL": 0, "OPEN": 0, "n": 0})
                t[f] += 1; t["n"] += 1
                re = o.get("richardson_error")
                row.append(f"{k}: {f}" + (f" R={re:.1e}" if isinstance(re, (int, float)) and re is not None else ""))
            print(f"  {name:24s} valid_steps {rec.get('n_valid_steps')} | " + " | ".join(row))
        print("  totals (passing = PASS + PASS(abs_only) + PASS_rel):")
        for k, t in totals.items():
            npass = t["PASS"] + t["PASS(abs_only)"] + t["PASS_rel"]
            print(f"    {k:42s} {npass}/{t['n']} pass; relative-rule PASS {t['PASS']}, absolute_only {t['PASS(abs_only)']}, PASS_rel {t['PASS_rel']}, FAIL {t['FAIL']}, OPEN {t['OPEN']}")
        print()


def label_for(reg, step, est):
    """Release label per direction (SPEC 3.0 (b'), (b''); lead 08:27Z item 2): registered five-step O1 pass -> 'registered';
    seven-step O1 pass -> 'pass under the post-result step rule'; only the gauge-subtracted estimator passes -> 'pass under the
    post-result gauge-subtracted estimator'; nothing passes -> 'FAIL'."""
    ok = lambda f: f.startswith("PASS")
    if ok(reg):
        return "registered PASS" + (" (absolute-only)" if "abs" in reg else "")
    if ok(step):
        return "pass under the post-result step rule" + (" (absolute-only)" if "abs" in step else "")
    if ok(est):
        return "pass under the post-result gauge-subtracted estimator" + (" (absolute-only)" if "abs" in est else "")
    return "FAIL under every rule"


def markdown(paths):
    out = []
    K_REG, K_STEP, K_EST, K_EST5 = "O1:v1.4_ladder", "O1:seven_step_ladder", "O_tilde_gauge_subtracted:seven_step_ladder", "O_tilde_gauge_subtracted:v1.4_ladder"
    for p in paths:
        d = json.load(open(p)); case = d.get("case"); dirs = d.get("directions", {})
        out.append(f"### G3 at {case} (record {os.path.basename(p)}; cost {d.get('cost'):.4e}; nine directions, seven valid steps each)\n")
        out.append("| direction | registered five-step O1 (SPEC 3.5) | seven-step O1 (post-result step rule, 3.0 (b') (2)) | seven-step gauge-subtracted estimator (3.0 (b') (3)) | five-step gauge-subtracted | release label |")
        out.append("|---|---|---|---|---|---|")
        cnt = {"reg": 0, "step": 0, "est": 0, "est5": 0}
        for name, rec in dirs.items():
            o = rec.get("outcomes", {})
            fr, fs, fe, fe5 = (flag(o.get(k, {})) for k in (K_REG, K_STEP, K_EST, K_EST5))
            def cell(f, k):
                re_ = o.get(k, {}).get("richardson_error")
                return f + (f" (R {re_:.1e})" if isinstance(re_, (int, float)) and re_ is not None and f.startswith("PASS") else "")
            for key, f in (("reg", fr), ("step", fs), ("est", fe), ("est5", fe5)):
                cnt[key] += f.startswith("PASS")
            out.append(f"| {name} | {cell(fr, K_REG)} | {cell(fs, K_STEP)} | {cell(fe, K_EST)} | {cell(fe5, K_EST5)} | {label_for(fr, fs, fe)} |")
        n = len(dirs)
        out.append(f"\nCounts: registered five-step O1 {cnt['reg']} of {n}; seven-step O1 {cnt['step']} of {n}; seven-step gauge-subtracted {cnt['est']} of {n}; five-step gauge-subtracted {cnt['est5']} of {n}. "
                   "PASS = relative rule with two consecutive passing steps and Richardson; PASS(abs_only) = passes only against the absolute floor; FAIL = no two consecutive passing steps.\n")
    return "\n".join(out)


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--md":
        print(markdown(args[1:]))
    else:
        main(args)
