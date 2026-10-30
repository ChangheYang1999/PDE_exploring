"""Extract the generator shapes (j, m, spec; no coefficients) of C1-N1-016, C1-N1-017 and the old basis
(old_basis.json, the exact quotient basis of 013 used by c1-t4) for check_T4322.py.

Usage: python3 -B extract_T4322_shapes.py <dir with candidate016.json, candidate017.json and old_basis.json>
Writes data/T4322_shapes.json. Run at 07:44Z and, with old_basis.json added, at 07:46Z on 2026-10-29
with the c1-t4 copies R6/c1-t4/research/scaled_rank_audit/data (byte-identical to the c1-n1 exact
snapshots by sha256)."""
import hashlib
import json
import sys
from pathlib import Path

src = Path(sys.argv[1])
out = {"sources": {}, "shapes": {}}
for name in ["candidate016.json", "candidate017.json", "old_basis.json"]:
    b = (src / name).read_bytes()
    out["sources"][name] = hashlib.sha256(b).hexdigest()
    d = json.loads(b)
    out["shapes"][name] = {"cl_exact": d.get("cl_exact"),
                           "gens": [[int(g["j"]), int(g["m"]), list(g["spec"])] for g in d["generators"]]}
Path(__file__).with_name("data").joinpath("T4322_shapes.json").write_text(json.dumps(out))
print(out["sources"])
