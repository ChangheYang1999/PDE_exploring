#!/usr/bin/env python
"""Pair result (SPEC v1.19 3.6 (h); lead 11:54:29Z item 1, 11:56:57Z item 4): for a FREE/FIXED pair, the cumulative optimizer history over the finished
segments (checkpoint_segment_end.pt of each run directory; the history entries carry it_cum, elapsed, cost, params, cost_blocks) and the two readings:
iteration-matched (O1 at the largest cumulative accepted iteration both members reached, and at a named iteration if both reached it) and wall-matched
(O1 of each member at the largest cumulative wall time both reached, and at a named budget if both reached it); c_l and omega of the FREE member at the
reading points; sharing-condition flags are passed as text and copied into the record. No production change. Usage:
python scripts/pair_result.py <pair tag> <FREE run dirs comma-separated, segment order> <FIXED run dirs comma-separated> [--it 360] [--wall 10800] [--flag "text"]
Writes validation/pair_result_<pair tag>.json (exclusive create) and prints the readings."""
import sys, os, json, time, bisect
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import torch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def series(run_dirs):
    """cumulative (it_cum, wall, cost, c_l, omega, blocks) over the segments; wall = sum of previous segments' total elapsed + this segment's elapsed."""
    out = []; wall0 = 0.0; last_it = -1; segs = []
    for rd in run_dirs:
        rd = rd if os.path.isabs(rd) else os.path.join(ROOT, rd)
        ck = torch.load(os.path.join(rd, "checkpoint_segment_end.pt"), map_location="cpu", weights_only=False)
        cur = ck["current"]; hist = cur["history"]
        seg_entries = [h for h in hist if h.get("it_cum", h["it"]) > last_it]      # a segment-2 history may repeat the earlier entries: keep the new ones only
        for h in seg_entries:
            if not h.get("accepted", True):
                continue
            out.append(dict(it_cum=h.get("it_cum", h["it"]), wall=wall0 + h["elapsed"], cost=h["cost"], c_l=h.get("params", {}).get("c_l"), omega=h.get("params", {}).get("omega"), blocks=h.get("cost_blocks"), segment=os.path.basename(rd)))
        seg_elapsed = max(h["elapsed"] for h in seg_entries) if seg_entries else 0.0
        segs.append(dict(run=os.path.basename(rd), job_id=ck["job_id"], label=ck.get("label"), entries=len(seg_entries), it_end=cur["it"], lm_status=cur.get("lm_status"), seg_elapsed=seg_elapsed, ts=cur.get("ts"), gpu=ck.get("gpu"), counters=cur.get("counters")))
        wall0 += seg_elapsed; last_it = max(last_it, cur["it"] - 1 if seg_entries == [] else max(h.get("it_cum", h["it"]) for h in seg_entries))
    return out, segs


def at_iteration(s, it):
    c = [e for e in s if e["it_cum"] <= it]
    return c[-1] if c else None


def at_wall(s, w):
    c = [e for e in s if e["wall"] <= w]
    return c[-1] if c else None


def main():
    tag, free_dirs, fixed_dirs = sys.argv[1], sys.argv[2].split(","), sys.argv[3].split(",")
    args = sys.argv[4:]; it_named = int(args[args.index("--it") + 1]) if "--it" in args else None; wall_named = float(args[args.index("--wall") + 1]) if "--wall" in args else None
    flag = args[args.index("--flag") + 1] if "--flag" in args else None
    out_path = os.path.join(ROOT, "validation", f"pair_result_{tag}.json")
    if os.path.exists(out_path):
        raise FileExistsError(out_path)
    sF, segF = series(free_dirs); sX, segX = series(fixed_dirs)
    it_common = min(sF[-1]["it_cum"], sX[-1]["it_cum"]); wall_common = min(sF[-1]["wall"], sX[-1]["wall"])
    def reading(kind, value):
        f = at_iteration(sF, value) if kind == "iteration" else at_wall(sF, value); x = at_iteration(sX, value) if kind == "iteration" else at_wall(sX, value)
        if f is None or x is None:
            return dict(kind=kind, at=value, available=False)
        notes = []
        if kind == "iteration":
            matched = (f["it_cum"] == x["it_cum"])     # both members at the same cumulative accepted iteration (it_cum 0-based; the named count is 1-based)
            for nm, e, fin in (("FREE", f, sF[-1]), ("FIXED", x, sX[-1])):
                if fin["it_cum"] + 1 < value:          # it_cum is 0-based: it_cum = 359 is the 360th accepted iteration
                    notes.append(f"{nm} reached only {fin['it_cum'] + 1} cumulative accepted iterations (< {value + 1}): its final state is used; the reading is NOT iteration-matched")
        else:
            matched = True
            for nm, e, fin, segs in (("FREE", f, sF[-1], segF), ("FIXED", x, sX[-1], segX)):
                if fin["wall"] < value:
                    notes.append(f"{nm} ended at cumulative wall {fin['wall']:.0f} s (< {value:.0f} s; last segment lm_status {segs[-1]['lm_status']}): its final state is used (no further change within the wall budget)")
        return dict(kind=kind, at=value, available=True, matched=bool(matched), notes=notes, FREE=dict(O1=f["cost"], it_cum=f["it_cum"], wall=f["wall"], c_l=f["c_l"], omega=f["omega"], blocks=f["blocks"]),
                    FIXED=dict(O1=x["cost"], it_cum=x["it_cum"], wall=x["wall"], blocks=x["blocks"]), ratio_FREE_over_FIXED=(f["cost"] / x["cost"] if x["cost"] else None))
    readings = dict(iteration_matched_common=reading("iteration", it_common), wall_matched_common=reading("wall", wall_common))
    if it_named is not None:
        readings[f"iteration_matched_{it_named}"] = reading("iteration", it_named - 1)       # the named count is 1-based; it_cum is 0-based
        readings[f"iteration_matched_{it_named}"]["at"] = it_named; readings[f"iteration_matched_{it_named}"]["at_it_cum_index"] = it_named - 1
    if wall_named is not None:
        readings[f"wall_matched_{wall_named:.0f}s"] = reading("wall", wall_named)
    rec = dict(pair=tag, FREE=dict(runs=free_dirs, segments=segF, final=sF[-1]), FIXED=dict(runs=fixed_dirs, segments=segX, final=sX[-1]), readings=readings, sharing_condition_flag=flag,
               definitions="O1 = history cost at the accepted iterate (self-consistent objective of the worker); it_cum is the 0-based index of the accepted iteration over the segments (it_cum = 359 is the 360th); the named iteration count is 1-based; wall = cumulative LM elapsed over the segments (segment checkpoints and restarts excluded); the iteration-matched reading compares both members at the same cumulative accepted iteration, the wall-matched at the same cumulative wall time",
               ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    with open(out_path, "x") as fh:
        json.dump(rec, fh, indent=1, default=str)
    for k, r in readings.items():
        if r.get("available"):
            print(f"{k}: FREE O1 {r['FREE']['O1']:.6e} (it {r['FREE']['it_cum']}, wall {r['FREE']['wall']:.0f} s, c_l {r['FREE']['c_l']}, omega {r['FREE']['omega']}) | FIXED O1 {r['FIXED']['O1']:.6e} (it {r['FIXED']['it_cum']}, wall {r['FIXED']['wall']:.0f} s) | ratio {r['ratio_FREE_over_FIXED']:.4f} | matched {r['matched']} {'; '.join(r['notes'])}")
        else:
            print(f"{k}: not available (at {r['at']})")
    print("DONE", out_path)


if __name__ == "__main__":
    main()
