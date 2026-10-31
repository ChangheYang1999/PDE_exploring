#!/usr/bin/env python3
"""scripts/lineage_status.py v1 (2026-10-30T08:3xZ; lead 08:20:06Z item 2: the final status of every lineage with state hashes, for the published artifacts).
Reads configs/lineage_status.txt (hand-maintained lines 'LINEAGE | RUN | STATUS | NOTE'; '#' comments) and, for each run, the worker's end record
runs/RUN/results.jsonl (start_result row: final c_l, omega, O1, accepted iterations, holdout rho_u^max standard / half-offset, stop) and the sha256 of the
end-state file runs/RUN/checkpoint_segment_end.pt (or checkpoint.pt when the segment has no end yet). Prints markdown; no field evaluation. Status words are
the lead's decisions as recorded in NOTES/WORKLOG at the time of writing (frozen = Phase IV frozen state; excluded = 6.3 (a) exclusion raised; diagnostic =
Phase III diagnostic end, never a candidate; control = FIXED-CONTROL; pilot = breadth pilot; running = not ended at generation time).
Usage: python3 scripts/lineage_status.py [configs/lineage_status.txt]"""
import os, sys, json, hashlib, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
cfg = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "configs", "lineage_status.txt")
def sha16(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()[:16]
def fmt(x, f="{:.6f}"):
    try: return f.format(float(x))
    except Exception: return "-"
rows = []; listed = set(); header_note = []
for line in open(cfg):
    line = line.strip()
    if not line: continue
    if line.startswith("#"): header_note.append(line[1:].strip()); continue
    parts = [p.strip() for p in line.split("|")]
    if len(parts) < 3: continue
    lin, run, status = parts[0], parts[1], parts[2]; note = parts[3] if len(parts) > 3 else ""
    listed.add(run); d = os.path.join(ROOT, "runs", run)
    end = os.path.join(d, "checkpoint_segment_end.pt"); ck = os.path.join(d, "checkpoint.pt")
    if os.path.exists(end): hs = "end " + sha16(end)
    elif os.path.exists(ck): hs = "ckpt " + sha16(ck)
    elif os.path.isdir(os.path.join(ROOT, "status", "s2_prod", run)): 
        e2 = os.path.join(ROOT, "status", "s2_prod", run, "checkpoint.pt"); hs = ("ckpt " + sha16(e2)) if os.path.exists(e2) else "-"; d = os.path.join(ROOT, "status", "s2_prod", run)
    else: hs = "-"
    sr = {}
    rp = os.path.join(d, "results.jsonl")
    if os.path.exists(rp):
        for l in open(rp):
            try: r = json.loads(l)
            except Exception: continue
            if r.get("kind") == "start_result": sr = r
    rows.append((lin, run, status, hs, sr, note))
print("# Lineage status of the degree-6 free-parameter campaign (generated %s by scripts/lineage_status.py v1)" % time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
print()
for n in header_note: print(n)
print()
print("Values are the worker's own end-record values (optimizer); independently checked values are in the verifier's report. 'hash' is the first 16 hex digits of the sha256 of the run's end-state file (end = checkpoint_segment_end.pt; ckpt = the last periodic checkpoint of a segment without an end).")
print()
print("| lineage | run | status | final (c_l, omega) | O1 final | accepted (cum.) | holdout rho_u^max std / half | stop | end state hash | note |")
print("|---|---|---|---|---|---|---|---|---|---|")
for lin, run, status, hs, sr, note in rows:
    par = "(%s, %s)" % (fmt(sr.get("c_l")), fmt(sr.get("omega"))) if sr else "-"
    print("| %s | %s | %s | %s | %s | %s | %s / %s | %s | %s | %s |" % (lin, run, status, par, fmt(sr.get("cost_final"), "{:.4e}") if sr else "-", sr.get("n_accepted", "-") if sr else "-",
          fmt(sr.get("rho_u_max_holdout"), "{:.5f}") if sr else "-", fmt(sr.get("rho_u_max_holdout_half"), "{:.5f}") if sr else "-", sr.get("stop_reason", "-") if sr else "-", hs, note))
others = sorted(x for x in os.listdir(os.path.join(ROOT, "runs")) if x not in listed and not x.startswith("INVALID"))
print()
print("Runs not listed above (smoke tests, resume tests, pilots and refits; their end records are in the deliverable-A table of NUM_REPORT.md and in the ledger): " + ", ".join(others))
