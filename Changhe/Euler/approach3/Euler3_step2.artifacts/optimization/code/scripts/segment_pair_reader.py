#!/usr/bin/env python
"""scripts/segment_pair_reader.py v1.1 (2026-10-30T07:3xZ; V681: named k above both lengths emitted as unavailable, beyond-wall rows null; v1 07:2xZ; V670, lead 06:52:15Z item 1 and 07:11:58Z item 4 (a)): SEGMENT-LOCAL matched readings of two runs A and B from their
saved checkpoint histories (no field evaluation):
  - each run's history is split into inherited rows (from earlier segments of a resumed lineage) and the segment's OWN accepted rows: for a resumed segment the own rows
    are those with cumulative index it_cum >= the segment start (job segment_source.it_end, or the checkpoint's own first row for a fresh start); cumulative indices are preserved
    and the segment-local accepted count k = 1..n is rebased on the own rows; k beyond the shorter segment is marked unavailable;
  - the segment-local elapsed (the own rows' elapsed field, which restarts at the segment start) is used for wall matching: at wall w the last own row of each run at or before w;
  - readings: O1 and (c_l, omega) of both runs at equal segment-local accepted counts (every k up to the common n, plus named ks) and at equal segment-local elapsed times
    (every 600 s up to the common wall, plus the full wall of the shorter), with the ratios A/B;
  - the checkpoint used may be a periodic checkpoint (--a-checkpoint / --b-checkpoint), named in the record (a periodic checkpoint is not an end).
These are stored objective values of two runs that ran at different times on a shared host; not physical-residual comparisons (lead 07:11:58Z item 4 (a)).
Usage: python scripts/segment_pair_reader.py <tag> <run A dir> <run B dir> [--a-checkpoint FILE] [--b-checkpoint FILE] [--ks 12,29,44] [--walls 1800,3600,7200] [--flag TEXT]
Writes validation/segpair_<tag>.json (exclusive create) and prints the readings."""
import os, sys, json, time, hashlib, argparse, bisect
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import torch
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()


def load(run, ckfile=None):
    run = os.path.abspath(run)
    ck_path = ckfile or (os.path.join(run, "checkpoint_segment_end.pt") if os.path.exists(os.path.join(run, "checkpoint_segment_end.pt")) else os.path.join(run, "checkpoint.pt"))
    ck = torch.load(ck_path, map_location="cpu", weights_only=False); cur = ck["current"]; hist = cur["history"]
    jid = ck.get("job_id"); jobf = None
    for d in ("done", "running", "cancelled", "failed"):
        p = os.path.join(ROOT, "queue", d, f"{jid}.json")
        if os.path.exists(p):
            jobf = p; break
    if jobf is None:
        for p in (os.path.join(ROOT, "status", "s2_prod", f"{jid}.json"),):
            if os.path.exists(p):
                jobf = p
    job = json.load(open(jobf)) if jobf else {}
    seg_src = job.get("segment_source") or {}
    it_start = seg_src.get("it_end")                       # cumulative index of the resumed end (own rows have it_cum >= it_start); None for a fresh start
    rows = [h for h in hist if h.get("accepted", True)]
    cum = [int(h.get("it_cum", h["it"])) for h in rows]
    if it_start is None:
        own = list(range(len(rows))); inherited = 0
    else:
        own = [i for i, c in enumerate(cum) if c >= int(it_start)]; inherited = len(rows) - len(own)
    own_rows = [rows[i] for i in own]
    k_tab = [dict(k=k + 1, it_cum=int(h.get("it_cum", h["it"])), elapsed=float(h["elapsed"]), cost=float(h["cost"]), c_l=(h.get("params") or {}).get("c_l"), omega=(h.get("params") or {}).get("omega")) for k, h in enumerate(own_rows)]
    # segment-local elapsed sanity: it must be non-decreasing within the own rows
    el = [r["elapsed"] for r in k_tab]; monotone = all(b >= a for a, b in zip(el, el[1:]))
    return dict(run=run, job_id=jid, checkpoint=ck_path, checkpoint_sha256=sha(ck_path), checkpoint_kind=("segment end" if ck_path.endswith("checkpoint_segment_end.pt") else "periodic checkpoint (NOT an end)"), it_checkpoint=int(cur["it"]), lm_status=cur.get("lm_status"),
                job_file=jobf, segment_start_it_cum=it_start, inherited_rows=inherited, own_accepted=len(own_rows), own_elapsed_monotone=monotone, own_wall_s=(el[-1] if el else None), params_end=(k_tab[-1]["c_l"], k_tab[-1]["omega"]) if k_tab else None, table=k_tab)


def at_wall(tab, w):
    c = [r for r in tab if r["elapsed"] <= w]
    return c[-1] if c else None


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("tag"); ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("--a-checkpoint"); ap.add_argument("--b-checkpoint"); ap.add_argument("--ks", default=""); ap.add_argument("--walls", default=""); ap.add_argument("--flag", default="")
    a = ap.parse_args()
    A = load(a.a, a.a_checkpoint); B = load(a.b, a.b_checkpoint)
    n = min(A["own_accepted"], B["own_accepted"])
    ks = sorted(set([int(x) for x in a.ks.split(",") if x] + [n]))
    by_k = []
    for k in range(1, max(A["own_accepted"], B["own_accepted"], max(ks) if ks else 0) + 1):          # v1.1 (V681): a named k above BOTH lengths is emitted as an unavailable entry, not omitted
        ra = A["table"][k - 1] if k <= A["own_accepted"] else None; rb = B["table"][k - 1] if k <= B["own_accepted"] else None
        by_k.append(dict(k=k, A=ra, B=rb, ratio=(ra["cost"] / rb["cost"] if ra and rb else None), available=(ra is not None and rb is not None)))
    wmax = min(A["own_wall_s"], B["own_wall_s"]); walls = sorted(set([float(x) for x in a.walls.split(",") if x] + [600.0 * i for i in range(1, int(wmax // 600) + 1)] + [wmax]))
    by_w = []
    for w in walls:
        ra = at_wall(A["table"], w); rb = at_wall(B["table"], w)
        avail = (w <= wmax and ra is not None and rb is not None)
        by_w.append(dict(wall_s=w, A=(ra if avail else None), B=(rb if avail else None), ratio=((ra["cost"] / rb["cost"]) if avail else None), available=avail, note=(None if w <= wmax else "beyond the shorter segment's wall: unavailable (no ratio)")))   # v1.1 (V681): beyond-wall rows carry null values
    rec = dict(tag=a.tag, tool="scripts/segment_pair_reader.py v1.1", tool_sha256=sha(os.path.abspath(__file__)), ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), flag=a.flag,
               A={k: v for k, v in A.items() if k != "table"}, B={k: v for k, v in B.items() if k != "table"}, common_accepted=n, common_wall_s=wmax,
               named_k=[r for r in by_k if r["k"] in ks], by_k=by_k, by_wall=by_w,
               note="segment-local readings (own rows of each segment; cumulative indices preserved; k rebased; segment-local elapsed for wall matching); stored objective values of runs on a shared host at different times, not physical-residual comparisons; a periodic checkpoint is not an end")
    out = os.path.join(ROOT, "validation", f"segpair_{a.tag}.json")
    with open(out, "x") as fh:
        json.dump(rec, fh, indent=1, default=str)
    print(f"{a.tag}: A {A['job_id']} ({A['checkpoint_kind']}, own accepted {A['own_accepted']}, inherited {A['inherited_rows']}, wall {A['own_wall_s']:.0f} s) vs B {B['job_id']} ({B['checkpoint_kind']}, own {B['own_accepted']}, inherited {B['inherited_rows']}, wall {B['own_wall_s']:.0f} s); common k {n}, common wall {wmax:.0f} s")
    for r in rec["named_k"]:
        print(f"  k={r['k']}: " + (f"A {r['A']['cost']:.6e} ({r['A']['c_l']:.6f}, {r['A']['omega']:.6f}) | B {r['B']['cost']:.6e} ({r['B']['c_l']:.6f}, {r['B']['omega']:.6f}) | ratio {r['ratio']:.5f}" if r["available"] else "unavailable (beyond the shorter segment)"))
    for r in by_w:
        if r["available"] and (r["wall_s"] % 1800 == 0 or r["wall_s"] == wmax):
            print(f"  wall {r['wall_s']:.0f} s: A {r['A']['cost']:.6e} (k {r['A']['k']}) | B {r['B']['cost']:.6e} (k {r['B']['k']}) | ratio {r['ratio']:.5f}")
    print("written", out)


if __name__ == "__main__":
    main()
