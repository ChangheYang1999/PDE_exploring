#!/usr/bin/env python
"""Battery memory mitigation check (lead 2026-10-25T21:03Z: the mitigation must not change any stored value). Runs the holdout
spec_diagnostics battery item (extras=True) on a saved state twice, with the ray-check point chunk at its old value (200000) and
at the new default (RAY_CHUNK), and reports the largest relative difference of every stored scalar (shell ratios, maxima, origin
Taylor, Z/I integrals, ray check). Usage: compare_ray_chunk.py <start.pt> [--device cpu|cuda] [--old 200000]"""
import sys, os, json, time, argparse, math
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import torch
ap = argparse.ArgumentParser(); ap.add_argument("start"); ap.add_argument("--device", default="cpu"); ap.add_argument("--old", type=int, default=200000); ap.add_argument("--threads", type=int, default=2); ap.add_argument("--abs_floor", type=float, default=1e-14, help="absolute floor in the relative difference (values below it are compared against the floor)")
a = ap.parse_args(); torch.set_num_threads(a.threads); ABS_FLOOR = a.abs_floor
from scripts.worker import build
from src.validation import spec_diagnostics as sdm
from src.validation.holdout import HoldoutGrid
S = torch.load(a.start, map_location="cpu", weights_only=False); cfg = dict(S["config"]); cfg.pop("init_from", None)
model, prob = build(cfg, a.device); z = S["z"].to(a.device)
hold = HoldoutGrid(model, r_core=model.R0, n_per_shell=int(cfg.get("holdout_per_shell", 6)))
out = {}
for tag, ch in (("new", sdm.RAY_CHUNK), ("old", a.old)):
    sdm.RAY_CHUNK = ch; t = time.time()
    if a.device != "cpu":
        torch.cuda.reset_peak_memory_stats(); torch.cuda.empty_cache()
    d = sdm.spec_diagnostics(prob, z, holdout=hold, extras=True)
    pk = torch.cuda.max_memory_allocated() / 2**30 if a.device != "cpu" else None
    out[tag] = dict(chunk=ch, seconds=round(time.time() - t, 1), peak_GB=pk, d=d)
    print(f"{tag}: chunk {ch}, {time.time() - t:.0f} s, peak {pk} GB, ray check {d['pressure'].get('ray_check', {}).get('max_rel_diff')}, extras_memory {d.get('extras_memory')}", flush=True)
def flat(x, pre=""):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from flat(v, f"{pre}.{k}" if pre else str(k))
    elif isinstance(x, (list, tuple)):
        for i, v in enumerate(x):
            yield from flat(v, f"{pre}[{i}]")
    elif isinstance(x, (int, float)) and not isinstance(x, bool):
        yield pre, float(x)
A = dict(flat(out["new"]["d"])); B = dict(flat(out["old"]["d"]))
skip = ("extras_memory", "ray_check.chunk")
rows = []
for k in sorted(set(A) | set(B)):
    if any(s in k for s in skip):
        continue
    if k not in A or k not in B:
        rows.append((float("inf"), k, A.get(k), B.get(k))); continue
    x, y = A[k], B[k]
    if math.isnan(x) and math.isnan(y):
        continue
    if math.isnan(x) or math.isnan(y):                 # one-sided NaN is a difference (astra referee 23:20Z)
        rows.append((float("inf"), k, x, y)); continue
    rel = abs(x - y) / max(abs(x), abs(y), ABS_FLOOR)   # absolute floor near zero: differences below ABS_FLOOR count as zero relative to the floor
    rows.append((rel, k, x, y))
rows.sort(reverse=True)
print(f"\ncompared {len(rows)} stored scalars; largest relative differences (new chunk {out['new']['chunk']} vs old {a.old}):")
for rel, k, x, y in rows[:12]:
    print(f"  {rel:.3e}  {k}: {x!r} vs {y!r}")
nz = [r for r in rows if r[0] > 0]
print(f"nonzero numerical differences: {len(nz)} of {len(rows)} compared numeric scalars (booleans, strings and the memory/chunk metadata are not compared; this is a numerical comparison, not a bitwise one); max {rows[0][0]:.3e} at {rows[0][1]}; all ray-check-related: {all('ray' in r[1] for r in nz)}")
res = dict(start=a.start, device=a.device, chunks=dict(new=out["new"]["chunk"], old=a.old), seconds=dict(new=out["new"]["seconds"], old=out["old"]["seconds"]), peak_GB=dict(new=out["new"]["peak_GB"], old=out["old"]["peak_GB"]),
           compared=len(rows), nonzero=len(nz), max_rel=rows[0][0], max_rel_key=rows[0][1], top=[dict(rel=r[0], key=r[1], new=r[2], old=r[3]) for r in rows[:12]],
           extras_memory=dict(new=out["new"]["d"].get("extras_memory"), old=out["old"]["d"].get("extras_memory")), generated=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
os.makedirs(os.path.join(ROOT, "reports"), exist_ok=True)
fn = os.path.join(ROOT, "reports", f"ray_chunk_compare_{os.path.basename(os.path.dirname(os.path.dirname(a.start)))}_{a.device}.json")
json.dump(res, open(fn, "w"), indent=1, default=str); print("written", fn)
