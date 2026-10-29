"""Counts and minima of the Stage I main sweep (1/2 < c_l < 3/4) from the primary failure map, with explicit filters.
Usage: python3 stage1_counts.py FAILURE_MAP.csv [cutoff_iso]
Swirl retention filter: s_core >= 0.05 and s_far >= 0.05 (the magnitude part of SPEC B2)."""
import csv, json, sys, collections, os
path = sys.argv[1]
cutoff = sys.argv[2] if len(sys.argv) > 2 else None
rows = list(csv.DictReader(open(path)))
def f(x):
    try: return float(x)
    except Exception: return None
out = {"source_rows": len(rows), "cutoff": cutoff, "by_stage": dict(collections.Counter(r["stage"] for r in rows))}
main = [r for r in rows if r["stage"] == "I" and (cutoff is None or r["finished"] <= cutoff)]
out["stage_I_runs"] = len(main)
out["stage_I_failure_class"] = dict(collections.Counter(r["failure_class"] for r in main))
out["stage_I_last_finished"] = max(r["finished"] for r in main) if main else None
keep = [r for r in main if (f(r["s_core"]) or 0) >= 0.05 and (f(r["s_far"]) or 0) >= 0.05 and f(r["rho_max"]) is not None]
out["stage_I_swirl_retaining"] = len(keep)
per = {}
for r in keep:
    c = r["cl_start"]
    if c not in per or f(r["rho_max"]) < f(per[c]["rho_max"]):
        per[c] = r
out["min_rho_swirl_retaining_by_cl_start"] = {c: {"rho_max": f(per[c]["rho_max"]), "job_id": per[c]["job_id"],
    "dominant_eq": per[c]["dominant_eq"], "s_core": f(per[c]["s_core"]), "s_far": f(per[c]["s_far"])} for c in sorted(per, key=float)}
free = [r for r in main if r["free_cl"] == "True"]
out["stage_I_free_cl"] = [{"job_id": r["job_id"], "cl_start": f(r["cl_start"]), "cl_final": f(r["cl_final"]), "rho_max": f(r["rho_max"])} for r in sorted(free, key=lambda r: (float(r["cl_start"]), r["job_id"]))]
o = os.path.join(os.path.dirname(os.path.abspath(__file__)), "stage1_counts_output.json")
json.dump(out, open(o, "w"), indent=1)
print(json.dumps({k: v for k, v in out.items() if k != "stage_I_free_cl"}, indent=1)); print(len(free), "free-c_l runs")
