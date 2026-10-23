#!/usr/bin/env python3
"""Campaign ledger utilities: non-overlapping CREDITED elapsed time, STATE.json.

Each ledger record is one worker interval with wall start/end and the credited seconds inside it. Records written
since 2026-10-23 07:12Z also carry "chunks": the credited elapsed pieces between accepted optimizer steps (closed at
gaps > 30 s or at checkpoints). Chunks include checkpoint I/O and pauses shorter than 30 s, omit the first step of each
interval, and have endpoints rounded to 1 ms, so their union bounds the credited elapsed time; it is not a certificate
of eligible numerical activity. The per-worker sum is reported too; it is NOT the campaign time (parallel workers overlap).
The density estimate of the first version is kept only as 'deprecated'.
Usage: python3 ledger.py [--state]  (prints a summary; --state also writes STATE.json)
"""
import json, os, sys, time
from datetime import datetime, timezone

PROJECT = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(PROJECT, "CAMPAIGN_LEDGER.jsonl")


def ts(s):
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp()


def load():
    recs = []
    if not os.path.exists(LEDGER):
        return recs
    with open(LEDGER) as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    recs.append(json.loads(line))
                except Exception:
                    pass
    return recs


def union_length(segs):
    """Exact length of the union of [a,b] segments."""
    segs = sorted((a, b) for a, b in segs if b > a)
    tot, cur_a, cur_b = 0.0, None, None
    for a, b in segs:
        if cur_b is None or a > cur_b:
            if cur_b is not None:
                tot += cur_b - cur_a
            cur_a, cur_b = a, b
        else:
            cur_b = max(cur_b, b)
    if cur_b is not None:
        tot += cur_b - cur_a
    return tot


def exact_and_bounds(recs):
    """Returns dict with: union_seconds of all credited chunks (records that have 'chunks'), legacy_lower /
    legacy_upper bounds for records without chunks (lower = |union I_i| - sum_i g_i with g_i the inactive measure
    inside I_i; upper = |union I_i|), and combined lower/upper bounds for the whole ledger
    (combined_lower = exact_union(chunks) + legacy_lower_of_the_part_not_covered ... computed conservatively as
    union of [chunks + legacy intervals] minus sum of legacy gaps; combined_upper = union of all)."""
    chunks = []
    legacy = []
    gaps = 0.0
    for r in recs:
        if "chunks" in r:
            chunks += [(float(a), float(b)) for a, b in r["chunks"]]
        else:
            a, b = ts(r["interval_start"]), ts(r["interval_end"])
            if b > a:
                legacy.append((a, b)); gaps += max(0.0, (b - a) - float(r.get("active_seconds", 0.0)))
    exact = union_length(chunks)
    leg_upper = union_length(legacy)
    leg_lower = max(0.0, leg_upper - gaps)
    all_upper = union_length(chunks + legacy)
    all_lower = max(0.0, all_upper - gaps)
    return {"exact_union_seconds_chunks": exact, "legacy_lower_seconds": leg_lower, "legacy_upper_seconds": leg_upper,
            "combined_lower_seconds": all_lower, "combined_upper_seconds": all_upper, "n_records_with_chunks": sum(1 for r in recs if "chunks" in r),
            "n_legacy_records": len(legacy)}


def union_seconds(recs):
    """Union of wall intervals; each record contributes with density active/wall so that paused fractions
    are not credited. Implemented as a sweep over sorted interval endpoints using max density per instant."""
    segs = []
    for r in recs:
        a, b = ts(r["interval_start"]), ts(r["interval_end"])
        if b <= a:
            continue
        dens = min(1.0, max(0.0, r.get("active_seconds", 0.0) / max(1e-9, b - a)))
        segs.append((a, b, dens))
    if not segs:
        return 0.0, 0.0
    pts = sorted(set([s[0] for s in segs] + [s[1] for s in segs]))
    total, plain = 0.0, 0.0
    for i in range(len(pts) - 1):
        lo, hi = pts[i], pts[i + 1]
        mid = 0.5 * (lo + hi)
        d = [s[2] for s in segs if s[0] <= mid < s[1]]
        if d:
            total += (hi - lo) * max(d)
            plain += (hi - lo)
    return total, plain


def summarize():
    recs = load()
    tot, plain = union_seconds(recs)
    per_exp = {}
    for r in recs:
        e = per_exp.setdefault(r["exp_id"], {"active_seconds_sum": 0.0, "records": 0, "last": None, "first": None})
        e["active_seconds_sum"] += r.get("active_seconds", 0.0); e["records"] += 1
        e["last"] = r["interval_end"]; e["first"] = e["first"] or r["interval_start"]
        for k in ("val_score", "nonaxi_ratio_core", "eps_m_D1", "cl", "step_end", "ckpt_sha256", "cfg_hash"):
            if k in r:
                e[k] = r[k]
    eb = exact_and_bounds(recs)
    return {"active_hours_union": eb["combined_lower_seconds"] / 3600.0,  # the quotable number: rigorous lower bound
            "active_hours_upper": eb["combined_upper_seconds"] / 3600.0, "active_hours_exact_chunks": eb["exact_union_seconds_chunks"] / 3600.0,
            "legacy_lower_hours": eb["legacy_lower_seconds"] / 3600.0, "legacy_upper_hours": eb["legacy_upper_seconds"] / 3600.0,
            "n_records_with_chunks": eb["n_records_with_chunks"], "n_legacy_records": eb["n_legacy_records"],
            "method": "active_hours_union = |union of all credited chunks and legacy intervals| - sum of legacy inactive measures (lower bound of the CREDITED elapsed time); "
                      "records with 'chunks' carry the trainer-credited elapsed pieces between accepted optimizer steps (they include checkpoint I/O and pauses shorter than 30 s, omit the first step of each interval, and have endpoints rounded to 1 ms); legacy records (before 2026-10-23 07:12Z) have only wall intervals + active_seconds. "
                      "These are bounds on credited elapsed intervals, not a certificate of eligible numerical activity.",
            "density_estimate_hours_deprecated": tot / 3600.0, "wall_hours_covered": plain / 3600.0,
            "worker_hours_sum": sum(r.get("active_seconds", 0.0) for r in recs) / 3600.0,
            "records": len(recs), "experiments": per_exp, "computed": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}


if __name__ == "__main__":
    s = summarize()
    print(json.dumps({k: v for k, v in s.items() if k != "experiments"}, indent=1))
    for e, v in sorted(s["experiments"].items()):
        print("%-36s active %7.2f h  recs %3d  last %s  step %s  val %s  nonaxi %s" % (e, v["active_seconds_sum"] / 3600, v["records"], v["last"], v.get("step_end"),
              ("%.3e" % v["val_score"]) if v.get("val_score") is not None else "-", ("%.3e" % v["nonaxi_ratio_core"]) if v.get("nonaxi_ratio_core") is not None else "-"))
    if "--state" in sys.argv:
        st = {"cumulative_active_hours_nonoverlapping": round(s["active_hours_union"], 3), "cumulative_active_hours_upper_bound": round(s["active_hours_upper"], 3),
              "exact_union_hours_from_chunks": round(s["active_hours_exact_chunks"], 3), "legacy_records_lower_upper_hours": [round(s["legacy_lower_hours"], 3), round(s["legacy_upper_hours"], 3)],
              "method": s["method"], "worker_hours_sum": round(s["worker_hours_sum"], 3),
              "ledger_records": s["records"], "updated": s["computed"], "experiments": {k: {kk: vv for kk, vv in v.items()} for k, v in s["experiments"].items()}}
        rs = os.path.join(PROJECT, "runner_status.json")
        if os.path.exists(rs):
            st["runner"] = json.load(open(rs))
        tmp = os.path.join(PROJECT, "STATE.json.tmp")
        json.dump(st, open(tmp, "w"), indent=1, default=str); os.replace(tmp, os.path.join(PROJECT, "STATE.json"))
        print("STATE.json written")
