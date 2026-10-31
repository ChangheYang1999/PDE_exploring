#!/usr/bin/env python3
"""v2 (shift 7): rows for the Phase III segments, the perturbation repeat and the V662/V682 values.
Interim deliverable-A table (report section 3) from the numerics records, the lead's ranking candidates
(independent values) and the GPU-hours ledger.
Usage: python3 tools/table_a.py <tag>   -> notes/table_a_<tag>.md and .json
Optimizer values: worker end records (validation/summary_runs.json) or, where a segment is not yet listed there, the
admitted 6.3 (a) end record (validation/records_63a/<tag>.json, battery). Independent values: notes/ranking_candidates.json
(verifier V-numbers). GPU-hours: status/gpu_hours.json rows summed over the lineage's jobs up to the row's segment."""
import json, sys, os, hashlib, time

NUM = "<optimization tree>"
tag = sys.argv[1]


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


src = {
    "summary": NUM + "/validation/summary_runs.json",
    "gpu": NUM + "/status/gpu_hours.json",
    "cand": "notes/ranking_candidates.json",
}
S = json.load(open(src["summary"]))
G = json.load(open(src["gpu"]))
C = json.load(open(src["cand"]))

seg_by_run = {}
for lname, L in S["lineages"].items():
    for seg in L["segments"]:
        seg_by_run[seg["run"]] = seg
cand_by_run = {c["run"]: c for c in C}
EXTRA = {  # independent development values recorded after notes/ranking_candidates.json (06:00Z)
    "f1_S05_m3_L6_cl0.4500_om0.3000_free": {"rho_std": 0.0466343871225642, "rho_half": 0.0498839803695604,
                                             "source": "V662 (two pressure levels, development grids)"},
    "f2_S01_k0_keep_m3_L6_cl0.4597_om1.3389_free": {"rho_std": 0.037916249316753525, "rho_half": 0.03760911737235851,
                                                     "source": "V682 (one completed coarse pressure level; fine level OPEN)"},
}
for k, v in EXTRA.items():
    cand_by_run.setdefault(k, {"run": k})
    if not cand_by_run[k].get("independent"):
        cand_by_run[k]["independent"] = v
gpu_by_job = {}
for r in G["rows"]:
    gpu_by_job[r["job_id"]] = gpu_by_job.get(r["job_id"], 0.0) + r["gpu_hours_charged"]

# (row name, run id, start record tag, jobs of the lineage up to this segment, stationarity label)
P1 = ["p1_s1_S01_L6_cl0.4500_om1.0000_free", "p1_s2_S01_L6_cl0.4500_om1.0000_free",
      "cont1_s3_S01_L6_cl0.4500_om1.0000_free", "cont1_s4_S01_L6_cl0.4500_om1.0000_free"]
P1c = ["p1c_s1_S01_L6_cl0.4500_om1.0000_fixed", "p1c_s2_S01_L6_cl0.4500_om1.0000_fixed"]
P2 = ["p2_s1_S09_L6_cl0.4500_om0.3000_free", "p2_s2_S09_L6_cl0.4500_om0.3000_free"] + \
     ["cont2_s%d_S09_L6_cl0.4500_om0.3000_free" % k for k in (3, 4, 5, 6)]
P2c = ["p2c_s1_S09_L6_cl0.4500_om0.3000_fixed", "p2c_s2_S09_L6_cl0.4500_om0.3000_fixed"]
F1 = ["f1_s1_S05_L6_cl0.4500_om0.3000_free"] + ["f1_S05_m%d_L6_cl0.4500_om0.3000_free" % k for k in (1, 2, 3, 4)]
F2 = ["f2_S01_k0_keep_L6_cl0.4597_om1.3389_free"] + ["f2_S01_k0_keep_m%d_L6_cl0.4597_om1.3389_free" % k for k in (1, 2, 3, 4, 5)]
P3 = ["p3_s1b_S20_L6_cl0.4500_om1.0000_free", "p3_s2b_S20_L6_cl0.4500_om1.0000_free",
      "cont3free_S20_L6_cl0.4500_om1.0000_free", "cont4free_S20_L6_cl0.4500_om1.0000_free",
      "cont5free_S20_L6_cl0.4500_om1.0000_free", "cont6free_S20_L6_cl0.4500_om1.0000_free"]
PERT = "f3_P1s4_pert_s7_L6_cl0.4481_om1.4083_free"
P3c = ["p3c_s1b_S20_L6_cl0.4500_om1.0000_fixed", "p3c_s2b_S20_L6_cl0.4500_om1.0000_fixed"]
ROWS = [
    ("P1 FREE (S01), segment 4, frozen P1 state", P1[3], "P1_start_v10", P1, "incomplete (checked)"),
    ("P1 FREE (S01), segment 5, excluded (6.3 (g)), diagnostic", "cont1_s5_S01_L6_cl0.4500_om1.0000_free",
     "P1_start_v10", P1 + ["cont1_s5_S01_L6_cl0.4500_om1.0000_free"], "incomplete (lead value)"),
    ("P1 FIXED-CONTROL (S01)", P1c[1], "P1_start_v10", P1c, "incomplete (checked)"),
    ("P1 perturbation repeat (from P1 segment 4, size 1e-3)", PERT, "P1_start_v10", P1 + [PERT], "pending"),
    ("P2 FREE (S09), segment 6, 12-hour budget used", P2[5], "P2_start_v10", P2, "incomplete (checked)"),
    ("P2 FIXED-CONTROL (S09)", P2c[1], "P2_start_v10", P2c, "incomplete (checked)"),
    ("F1 FREE (S05), segment 3", F1[2], "f1_start", F1[:3], "incomplete (checked)"),
    ("F1 FREE (S05), segment 4", F1[3], "f1_start", F1[:4], "incomplete (criterion (a), lead value)"),
    ("F1 FREE (S05), segment 5", F1[4], "f1_start", F1[:5], "pending"),
    ("F2 FREE (S01 kept at moved parameters), segment 3", F2[2], "f2_start_v10", F2[:3], "incomplete (lead value)"),
    ("F2 FREE (S01 kept at moved parameters), segment 4", F2[3], "f2_start_v10", F2[:4], "incomplete (checked)"),
    ("F2 FREE (S01 kept at moved parameters), segment 5", F2[4], "f2_start_v10", F2[:5], "pending"),
    ("F2 FREE (S01 kept at moved parameters), segment 6", F2[5], "f2_start_v10", F2[:6], "pending"),
    ("P3 FREE (S20, all-m), segment 2", P3[1], "P3_start", P3[:2], "incomplete (lead value)"),
    ("P3 FIXED-CONTROL (S20, all-m), segment 2", P3c[1], "P3_start", P3c, "incomplete (independent value)"),
    ("P3 FREE (S20, all-m), segment 3", P3[2], "P3_start", P3[:3], "incomplete (lead value)"),
    ("P3 FREE (S20, all-m), segment 4", P3[3], "P3_start", P3[:4], "pending"),
    ("P3 FREE (S20, all-m), segment 5", P3[4], "P3_start", P3[:5], "pending"),
    ("P3 FREE (S20, all-m), segment 6", P3[5], "P3_start", P3[:6], "pending"),
    ("Approach from above (P1 s4 coefficients kept at omega 1.80), excluded (6.3 (g)) against S01",
     "f2_P1s4_om1p80_L6_cl0.4481_om1.8000_free", "f2P1s4_start", ["f2_P1s4_om1p80_L6_cl0.4481_om1.8000_free"],
     "incomplete (checked)"),
]


def endvals(run):
    """optimizer end values: summary_runs segment, else the 6.3 (a) end record battery"""
    s = seg_by_run.get(run)
    if s is not None and "params_final" not in s:   # a running segment: no end values yet
        return None
    if s is not None:
        return dict(src="summary_runs", c_l=s["params_final"]["c_l"], omega=s["params_final"]["omega"],
                    rho_std=s["rho_u_max_holdout"], rho_half=s.get("rho_u_max_holdout_half"),
                    a_core=s.get("a_max_core"), a_core_up=s.get("a_max_core_upper"), it=s.get("iterations"),
                    O1=s.get("cost_final"))
    rp = NUM + "/runs/%s/results.jsonl" % run
    if os.path.exists(rp):   # the worker's own end battery (start_result), as read by tools/ranking.py
        recs = [json.loads(l) for l in open(rp) if l.strip()]
        recs = [r for r in recs if r.get("kind") == "start_result"]
        if recs:
            r = recs[-1]
            return dict(src="results.jsonl", c_l=r.get("c_l"), omega=r.get("omega"), rho_std=r.get("rho_u_max_holdout"),
                        rho_half=r.get("rho_u_max_holdout_half"), a_core=r.get("a_max_core"),
                        a_core_up=r.get("a_max_core_upper"), it=r.get("n_accepted"), O1=r.get("cost_final"))
    stem = run.split("_L6_")[0]
    for t in (stem + "_end_v10", stem + "_end"):
        p = NUM + "/validation/records_63a/%s.json" % t
        if os.path.exists(p):
            d = json.load(open(p))
            b = d["battery"]
            return dict(src="records_63a/" + t, c_l=b["c_l"], omega=b["omega"], rho_std=b["rho_u_max_holdout"],
                        rho_half=None, a_core=b.get("a_max_core"), a_core_up=b.get("a_max_core_upper"),
                        it=d["state"].get("iterations"), O1=None)
    return None


def startvals(t):
    d = json.load(open(NUM + "/validation/records_63a/%s.json" % t))
    b = d["battery"]
    im = d["state"].get("init_meta", {})
    # the source half-offset value describes the source state at its own parameters; not used for moved starts
    same = abs(im.get("source_c_l", b["c_l"]) - b["c_l"]) < 1e-12 and abs(im.get("source_omega", b["omega"]) - b["omega"]) < 1e-12
    return dict(c_l=b["c_l"], omega=b["omega"], rho_std=b["rho_u_max_holdout"],
                rho_half=im.get("source_rho_u_half") if (same and t != "f2_start_v10") else None,
                a_core=b.get("a_max_core"), a_core_up=b.get("a_max_core_upper"))


def f(x, n=4):
    return "-" if x is None else ("%.*f" % (n, x))


out = []
lines = ["| Run | initial (c_l, omega) | final (c_l, omega) | accepted iterations | initial residual: holdout rho_u^max standard / half-offset [opt] | final holdout rho_u^max standard / half-offset | core residual: a_max core (centre / outer weight) [opt]; core-ball RMS [ind] | stationarity (7.4) | GPU-hours (ledger) |",
         "|---|---|---|---|---|---|---|---|---|"]
for name, run, st, jobs, lab in ROWS:
    e = endvals(run)
    s0 = startvals(st)
    if e is None:
        continue
    c = cand_by_run.get(run) or {}
    ind = c.get("independent")
    if ind:
        fin = "%s / %s [ind, %s]" % (f(ind["rho_std"], 5), f(ind["rho_half"], 5), ind["source"].split(" ")[0])
    else:
        fin = "%s / %s [opt]" % (f(e["rho_std"], 5), f(e["rho_half"], 5))
    cb = (c.get("core_ball_rms") or {}).get("value")
    gh = sum(gpu_by_job.get(j, 0.0) for j in jobs)
    row = dict(name=name, run=run, start=s0, end=e, independent=ind, core_ball_rms=c.get("core_ball_rms"),
               gpu_hours=gh, jobs=jobs, label=lab)
    out.append(row)
    lines.append("| %s | (%s, %s) | (%s, %s) | %s | %s / %s | %s | %s / %s; %s | %s | %.2f |" % (
        name, f(s0["c_l"], 6), f(s0["omega"], 6), f(e["c_l"], 6), f(e["omega"], 6), e["it"],
        f(s0["rho_std"], 5), f(s0["rho_half"], 5), fin, f(e["a_core"], 3), f(e["a_core_up"], 3),
        f(cb, 3) if cb is not None else "-", lab, gh))
meta = dict(written=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), sources={k: [v, sha(v)] for k, v in src.items()},
            summary_ts=S["ts"], gpu_written=G["written"])
json.dump(dict(meta=meta, rows=out), open("notes/table_a_%s.json" % tag, "w"), indent=1)
open("notes/table_a_%s.md" % tag, "w").write("\n".join(lines) + "\n\nsources: " + json.dumps(meta) + "\n")
print("\n".join(lines))
