"""Atomic checkpoints (tmp file + os.replace) and immutable accepted checkpoints with a hash manifest."""
from __future__ import annotations
import os, json, time, stat, torch
from .ledger import sha256_file


def atomic_save(obj, path):
    tmp = path + ".tmp"
    torch.save(obj, tmp)
    with open(tmp, "rb") as f:
        os.fsync(f.fileno())
    os.replace(tmp, path)


def atomic_write_text(text, path):
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        f.write(text); f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)


def promote_accepted(src_path, accepted_dir, name, note=""):
    """Copy a checkpoint into the immutable accepted area (read-only) and record its hash in MANIFEST.json."""
    os.makedirs(accepted_dir, exist_ok=True)
    dst = os.path.join(accepted_dir, name)
    if os.path.exists(dst):
        raise FileExistsError(f"accepted checkpoint {dst} exists; accepted checkpoints are immutable")
    with open(src_path, "rb") as fi, open(dst + ".tmp", "wb") as fo:
        fo.write(fi.read()); fo.flush(); os.fsync(fo.fileno())
    os.replace(dst + ".tmp", dst)
    os.chmod(dst, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    man_path = os.path.join(accepted_dir, "MANIFEST.json")
    man = json.load(open(man_path)) if os.path.exists(man_path) else {}
    man[name] = dict(sha256=sha256_file(dst), ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), note=note, source=src_path)
    atomic_write_text(json.dumps(man, indent=1, sort_keys=True), man_path)
    return dst
