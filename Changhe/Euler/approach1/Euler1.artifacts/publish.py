#!/usr/bin/env python3
"""Publish a checkpoint for independent validation: copies ckpt, exports NPZ + manifest, runs evaluate.py, writes
artifacts/candidates/<exp_id>/{ckpt.pt, weights.npz, manifest.json, audit.json, val_last.json, NOTE.md}. Atomic copies.
Usage: python3 publish.py runs/<exp_id>/ckpt_best.pt [--label preliminary|baseline|negative] [--device cuda:0]"""
import argparse, json, os, shutil, subprocess, sys, hashlib
P = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser(); ap.add_argument("ckpt"); ap.add_argument("--label", default="preliminary"); ap.add_argument("--device", default="cuda:0"); ap.add_argument("--note", default="")
a = ap.parse_args()
import torch
ck = torch.load(a.ckpt, map_location="cpu", weights_only=False)
eid = ck["exp_id"]; d = os.path.join(P, "artifacts", "candidates", eid); os.makedirs(d, exist_ok=True)
tmp = os.path.join(d, "ckpt.pt.tmp"); shutil.copy2(a.ckpt, tmp); os.replace(tmp, os.path.join(d, "ckpt.pt"))
subprocess.run([sys.executable, os.path.join(P, "export_npz.py"), os.path.join(d, "ckpt.pt"), os.path.join(d, "weights")], check=True)
os.replace(os.path.join(d, "weights.json"), os.path.join(d, "manifest.json"))
subprocess.run([sys.executable, os.path.join(P, "evaluate.py"), os.path.join(d, "ckpt.pt"), "--device", a.device, "--out", os.path.join(d, "audit.json")], check=True)
vl = os.path.join(P, "runs", eid, "val.jsonl")
if os.path.exists(vl):
    lines = open(vl).read().strip().splitlines()
    if lines:
        json.dump(json.loads(lines[-1]), open(os.path.join(d, "val_last.json"), "w"), indent=1)
sha = hashlib.sha256(open(os.path.join(d, "ckpt.pt"), "rb").read()).hexdigest()
with open(os.path.join(d, "NOTE.md"), "w") as f:
    f.write("# %s\n\nlabel: %s\nsource: %s\nckpt sha256: %s\nc_l (fixed input unless cl_trainable): %s\nstate: %s\n\n%s\n" % (eid, a.label, a.ckpt, sha, ck["cfg"].get("cl"), json.dumps({k: v for k, v in ck.get("state", {}).items() if k != "interruptions"}), a.note))
print("published", d, "sha256", sha[:16])
