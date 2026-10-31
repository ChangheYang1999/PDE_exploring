#!/usr/bin/env python
"""Gate I.4 G3 (lead 02:02Z item 3): ledger completeness. Counts start_result rows missing rng_seed, solver_version, the holdout vector
(rho_u_max_holdout) or a failure reason (rows without holdout and without 'failure'); rows before 2026-10-24T19:39Z (when rng_seed and
solver_version were introduced) are marked 'missing (pre-19:39Z, field did not exist)' explicitly. Writes reports/G3_LEDGER.md."""
import sys, os, json, time, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
from src.campaign import ledger
recs = ledger.read(os.path.join(ROOT, "status", "ledger.jsonl"))
rows = [r for r in recs if r.get("kind") == "start_result"]
CUT = "2026-10-24T19:39"
def pre(r):
    return str(r.get("ts", "")) < CUT
c = collections.Counter(); examples = collections.defaultdict(list)
for r in rows:
    tag = "pre" if pre(r) else "post"
    c[(tag, "rows")] += 1
    for field in ("rng_seed", "solver_version"):
        if r.get(field) is None:
            c[(tag, "missing " + field)] += 1
            if len(examples[(tag, field)]) < 3: examples[(tag, field)].append(f"{r.get('job_id')}/{r.get('start')}")
    if r.get("rho_u_max_holdout") is None and not r.get("failure"):
        c[(tag, "missing holdout vector and no failure reason")] += 1
        if len(examples[(tag, "holdout")]) < 3: examples[(tag, "holdout")].append(f"{r.get('job_id')}/{r.get('start')}")
    if r.get("rho_u_max_holdout") is None and r.get("failure"):
        c[(tag, "no holdout, failure reason recorded")] += 1
    if r.get("rho_u_max_holdout_half") is None and r.get("rho_u_max_holdout") is not None:
        c[(tag, "holdout present but half-offset family missing (pre-7.3a row; reevaluate_holdout.py fills it)")] += 1
kinds = collections.Counter(r.get("kind") for r in recs)
lines = [f"# G3 ledger completeness (generated {time.strftime('%Y-%m-%dT%H:%MZ', time.gmtime())})", "",
         f"Ledger status/ledger.jsonl: {len(recs)} records; kinds: " + ", ".join(f"{k} {v}" for k, v in sorted(kinds.items())), "",
         f"start_result rows: {len(rows)} ({c[('pre','rows')]} before {CUT}Z, {c[('post','rows')]} after).", "",
         "| period | field | rows missing | note | examples |", "|---|---|---|---|---|"]
for tag in ("pre", "post"):
    for key in sorted(k for k in c if k[0] == tag and k[1] != "rows"):
        note = "missing (pre-19:39Z, field did not exist in the ledger schema; marked explicitly, not blank)" if tag == "pre" and key[1].startswith("missing") else ("" if tag == "post" else "")
        ex = ", ".join(examples.get((tag, key[1].replace("missing ", "").split(" ")[0]), examples.get((tag, "holdout"), [])) [:3]) if key[1].startswith("missing") else ""
        lines.append(f"| {'before 19:39Z' if tag == 'pre' else 'after 19:39Z'} | {key[1]} | {c[key]} | {note} | {ex} |")
lines += ["", "Rules: every start_result after 19:39Z carries rng_seed and solver_version (worker.py); a start without holdout diagnostics carries a 'failure' string",
          "(collapse, gauge defect, NaN) with no ratios and no tier; disposable test jobs (smoke_*, resume_test) are excluded from leaderboards by name.",
          "Pre-19:39Z rows belong to the s1a/s1b sweeps (weak axisymmetric collapse states and the first reweighted momentum starts); they are kept for the record.",
          "Post-19:39Z rows missing rng_seed/solver_version come from worker processes launched before 19:39Z (s1c jobs; the worker code is loaded at launch) and from",
          "the disposable job wtest_free; they are marked here explicitly. Half-offset-family columns are filled for shortlisted states by reevaluate_holdout.py (ledger kind 'reevaluation')."]
os.makedirs(os.path.join(ROOT, "reports"), exist_ok=True)
open(os.path.join(ROOT, "reports", "G3_LEDGER.md"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
