#!/usr/bin/env python3
"""Add experiments to the queue. Usage: enqueue.py file1.json [file2.json ...]
Each file: {"exp_id":..., "priority": int, "config": {...}, ["gpu": "2"]}. Refuses duplicates of ids already
in any queue directory or with an existing run directory unless --force (then the run dir is resumed)."""
import json, os, sys, glob, shutil
P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
force = "--force" in sys.argv
for f in [a for a in sys.argv[1:] if not a.startswith("--")]:
    ent = json.load(open(f))
    eid = ent["exp_id"]
    existing = glob.glob(os.path.join(P, "queue", "*", eid + ".json"))
    if existing and not force:
        print("skip", eid, "already in", existing[0]); continue
    if os.path.exists(os.path.join(P, "runs", eid)) and not force:
        print("skip", eid, "run dir exists (use --force to resume it)"); continue
    dst = os.path.join(P, "queue", "pending", eid + ".json")
    json.dump(ent, open(dst + ".tmp", "w"), indent=1); os.replace(dst + ".tmp", dst)
    print("queued", eid, "priority", ent.get("priority", 0))
