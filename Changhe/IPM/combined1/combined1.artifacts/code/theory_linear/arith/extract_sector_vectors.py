"""Extract the exact leading residual sine vectors of the 4-, 6-, 7- and 8-branch stationary families.

Source (read only, another lane): R6/c1-n4/research/sector_audit/verification/stationary_principal.json
(c1-n4 exact principal stationary recursion; sha256 b80ec60e...ae363 when extracted). Output:
data/n4_forcing_sin_6_8.json (branch index j: residual exponent gamma - j delta and exact sine coefficients) and
data/n4_forcing_sin_4.json (the same for j = 4, used by arith/b4_family_cutoffs.py).
Run from artifacts/:  python3 -B arith/extract_sector_vectors.py   (only needed to regenerate the data files)
"""
import hashlib
import json
from pathlib import Path

SRC = Path("RUN_ROOT/numerics_audit_N4/research/sector_audit/verification/stationary_principal.json")
raw = SRC.read_bytes()
d = json.loads(raw)
here = Path(__file__).resolve().parents[1]
for idx, name in (((6, 7, 8), "data/n4_forcing_sin_6_8.json"), ((4,), "data/n4_forcing_sin_4.json")):
    out = {"source": str(SRC), "source_sha256": hashlib.sha256(raw).hexdigest(), "cl": d["cl"], "branches": {}}
    for b in d["branches"]:
        if int(b["index"]) in idx:
            out["branches"][str(b["index"])] = {"residual_exponent": b["residual_exponent"],
                                                "forcing_full_circle_norm": b["forcing_full_circle_norm"],
                                                "forcing_sin": b["forcing_sin"]}
    (here / name).write_text(json.dumps(out, indent=1) + "\n")
    print(name, ": source sha256", out["source_sha256"], "; branches", list(out["branches"]))
