#!/usr/bin/env python
"""D6FP: sidecar labels for the GPU release-battery records (SPEC v1.13 3.6 (b): every record states "release battery: GPU (v1.13)", the device and the
snapshot). For every validation/gates_gpu_v1_*.json (and g3_addon_gpu_v1*.json, g8_*_gpu_v1 logs' json if present) writes <name>_label.json with the
release-battery label, SPEC version and sha256, snapshot gpu_v1 (table status/RELEASE_SNAPSHOT_gpu_v1.md, addendum status/GPU_V1_DIFF.md), the device and
GPU index (from the run's log: CUDA_VISIBLE_DEVICES recorded by run_gpu_battery.sh), host, torch version and the code hashes recorded inside the file.
The result files themselves are not modified. Usage: python scripts/label_gate_records.py"""
import json, glob, os, re, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SPEC = dict(spec_version="v1.13 (binding v1.14 from 05:22Z; no threshold change)", spec_sha256_v1_13="80bf8833be2a91ba6a1d45399d88a5c27934a7c5af565d18fdb19f0e5a339b59", spec_sha256_v1_14="1e01acbc8828545d7d8e351cd8b472f99aa2a5b9ac8f947cf8370b8eb3f38eca")
snap = dict(snapshot="gpu_v1", table="status/RELEASE_SNAPSHOT_gpu_v1.md (20261029T051311Z)", diff="status/GPU_V1_DIFF.md", gates_py="8cb1c9ce7f1b109e (section addendum, status/RELEASE_SNAPSHOT_cpu_v1_addendum_split.md)")
n = 0
for f in sorted(glob.glob(os.path.join(ROOT, "validation", "gates_gpu_v1_*.json")) + glob.glob(os.path.join(ROOT, "validation", "g3_addon_gpu_v1*.json"))):
    if f.endswith("_label.json") or f.endswith("_flags.json"):
        continue
    d = json.load(open(f)); tag = d.get("tag") or os.path.basename(f)[:-5]
    gpu = None
    for lg in (os.path.join(ROOT, "validation", "logs", f"gpu_battery_{tag}.log"),):
        if os.path.exists(lg):
            m = re.search(r"on GPU (\d)", open(lg).read()); gpu = int(m.group(1)) if m else None
    lab = dict(release_battery="GPU (v1.13)", **SPEC, **snap, device=d.get("gpu") or d.get("device"), cuda_visible=d.get("cuda_visible"), gpu_index_assigned=gpu, host=d.get("host"), torch=d.get("torch"),
               precision_mode=d.get("precision_mode"), jacobian_precision=d.get("jacobian_precision"), code_sha256_recorded=d.get("code_sha256"), cases=list((d.get("cases") or {}).keys()), partial=any(isinstance(v, dict) and v.get("partial") for k, v in d.items() if k != "cases"),
               written=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), source_file=os.path.relpath(f, ROOT))
    json.dump(lab, open(f[:-5] + "_label.json", "w"), indent=1); n += 1
print(f"{n} label sidecars written")
