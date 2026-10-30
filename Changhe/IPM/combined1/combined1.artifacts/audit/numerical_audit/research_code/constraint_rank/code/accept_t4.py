"""Hash-linked acceptance of T4's independent squared-coordinate rank audit."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from fractions import Fraction as Q
import json
import sys
import time

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/"research/constraint_rank"
REVIEW = BASE/"reviews/T4_209"
digest = lambda p: sha256(Path(p).read_bytes()).hexdigest()
start = time.monotonic()
manifest = json.loads((REVIEW/"MANIFEST.json").read_text())
for name, entry in manifest["files"].items():
    assert digest(REVIEW/name) == entry["sha256"]
peer = json.loads((REVIEW/"result.json").read_text())
own_path = BASE/"verification/candidate007.json"
assert digest(own_path) == "ca06f0aeeb4dff484e4628c838954030425347b4377f0c50cfbaf2d84630580a"
own = json.loads(own_path.read_text())
assert peer["proof_sha256"] == digest(REVIEW/"PROOF.md")
assert peer["code_sha256"] == digest(REVIEW/"check.py")
checks = {
    "tail_rank": peer["tail_rank"] == 420,
    "linear_rank": peer["linear_rank"] == own["linear_constraint_rank"] == 421,
    "full_rank": peer["full_differential_rank"] == own["full_constraint_rank"] == 426,
    "potential_tangent": peer["potential_tangent_dimension"] == own["constrained_potential_tangent_dimension"] == 1496,
    "coefficient_tangent": peer["coefficient_tangent_dimension"] == own["constrained_generator_tangent_dimension"] == 2556,
    "a0": Q(peer["a0_exact"]) == Q(own["a0_exact"]),
    "Taylor_coefficients": list(map(Q, peer["Taylor_coefficients_exact"])) == list(map(Q, own["Taylor_residual_exact"])),
    "determinant": Q(peer["determinant_exact"]) == Q(own["determinant_exact"]) != 0,
    "Taylor_nonfeasibility": peer["Taylor_constant_exact_zero"] and peer["five_other_Taylor_coefficients_exact_nonzero"],
}
for direction in peer["directions"]:
    a, b = direction["a"], direction["b"]
    other = next(d for d in own["directions"] if d["a"] == a and d["b"] == b)
    checks[f"direction_{a}_{b}"] = (
        list(map(Q, direction["column"]))
        == [Q(other["strain"])] + list(map(Q, other["Taylor_differential"])))
assert len(peer["tail_minor_witnesses"]) == 360
assert sum(row["rank"] for row in peer["tail_minor_witnesses"]) == 420
assert all(Q(row["minor"]) != 0 for row in peer["tail_minor_witnesses"])
checks["all_tail_minors_nonzero"] = True
assert all(checks.values()), checks
out = {
    "utc": datetime.now(timezone.utc).isoformat(),
    "checks": checks, "count": len(checks),
    "manifest_sha256": digest(REVIEW/"MANIFEST.json"),
    "peer_result_sha256": digest(REVIEW/"result.json"),
    "own_result_sha256": digest(own_path),
    "code_sha256": digest(__file__),
    "elapsed_seconds": time.monotonic()-start,
    "verdict": "CONFIRMED exact ranks420/421/426 and Taylor non-feasibility; no PDE conditioning conclusion",
    "method_scope": "Peer proof/code reviewed. Compare independent exact arithmetic output; do not reexecute peer code.",
}
with (REVIEW/"ACCEPTANCE.json").open("x") as f:
    json.dump(out, f, indent=2)
    f.write("\n")
print(out["verdict"], out["count"], "checks", out["elapsed_seconds"])
