#!/usr/bin/env python
"""S12 / R13 helper: print the worker's 'RADIAL LAMBDA (d93, training grid)' battery line (share of the weighted squared momentum residual along
lambda(r) U, lambda max and its radius, octaves with lambda < 0, lambda by octave of r/R0) for a job and for the job it started from (config.init_from),
so that lambda(r) by octave at the start and at the end of an arm can be recorded (stage2_plan_draft.md S12: 'Record lambda(r) by octave and the
radial-lambda share at the start and at the end'). Reads runs/<job>/stdout.log only; values are primary-reported diagnostics, never acceptance criteria.
Usage: radial_lambda_octaves.py <job_id> [...]"""
import sys, os, json, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
def lam_line(job):
    p = os.path.join(ROOT, "runs", job, "stdout.log")
    if not os.path.exists(p):
        return None
    lines = [l.rstrip("\n") for l in open(p, errors="replace") if "RADIAL LAMBDA" in l]
    return lines[-1] if lines else None
def source_of(job):
    for d in ("done", "running", "pending", "failed", "cancelled", "hold", "hold_lowprio"):
        p = os.path.join(ROOT, "queue", d, job + ".json")
        if os.path.exists(p):
            src = json.load(open(p)).get("config", {}).get("init_from")
            if src:
                parts = os.path.relpath(src, ROOT).split(os.sep)
                return parts[1] if len(parts) > 1 and parts[0] == "runs" else src
    return None
def parse(line):
    m = re.search(r"\(lambda by octave of r/R0: (.*)\)", line)
    octs = {}
    if m:
        for tok in m.group(1).split():
            k, v = tok.rsplit(":", 1); octs[k] = float(v)
    share = re.search(r"lambda\(r\) U = ([0-9.eE+-]+)", line); lmax = re.search(r"lambda max ([0-9.eE+-]+) at r ([0-9.eE+-]+)", line)
    neg = re.search(r"octaves with lambda < 0: (\d+) of (\d+)", line)
    return dict(share=float(share.group(1)) if share else None, lambda_max=float(lmax.group(1)) if lmax else None, r_at_max=float(lmax.group(2)) if lmax else None,
                n_negative=int(neg.group(1)) if neg else None, n_octaves=int(neg.group(2)) if neg else None, by_octave=octs)
for job in sys.argv[1:]:
    src = source_of(job)
    print(f"## {job} (source {src})")
    for tag, j in (("start", src), ("end", job)):
        line = lam_line(j) if j else None
        if not line:
            print(f"  {tag} ({j}): no RADIAL LAMBDA line"); continue
        d = parse(line)
        print(f"  {tag} ({j}): share {d['share']}, lambda max {d['lambda_max']} at r {d['r_at_max']}, octaves with lambda < 0: {d['n_negative']} of {d['n_octaves']}")
        print("    lambda by octave of r/R0: " + " ".join(f"{k}:{v:+.3f}" for k, v in d["by_octave"].items()))
