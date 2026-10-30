"""Accept T4's general tensor and full retained-record audit without regeneration."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import time
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/"research/polar_third_derivative"
REVIEW = BASE/"reviews/T4_207"
digest = lambda p: sha256(Path(p).read_bytes()).hexdigest()
start = time.monotonic()
ctx.prec = 1024
manifest = json.loads((REVIEW/"MANIFEST.json").read_text())
for name, entry in manifest["files"].items():
    assert digest(REVIEW/name) == entry["sha256"]
peer = json.loads((REVIEW/"result.json").read_text())
own_path = BASE/"verification/C1-N1-007-d2w-j7-e2bal/full.json"
assert digest(own_path) == "ccecb46f06398c1883065e68c2141607f430ff7f5edc903d3341b9b49aa2543a"
own = json.loads(own_path.read_text())
checks = {
    "proof_hash": peer["proof_sha256"] == digest(REVIEW/"PROOF.md"),
    "code_hash": peer["code_sha256"] == digest(REVIEW/"check.py"),
    "complex_tensor_identity": peer["symbolic_complex_tensor_identity"],
    "connection_identities": peer["symbolic_degree6_connection_identities"],
    "complete_modes": own["complete"] and not own["missing_modes"]
        and own["completed_modes"] == list(range(1, 320, 2)) and peer["modes"] == 160,
    "symmetry_identities": peer["symmetry_identities"] == own["symmetry_identities"] == 2720,
    "endpoint_checks": peer["exact_endpoint_checks"] == 5440,
    "weight_degree": peer["weight_degree"] == 112,
    "canonical_semantic_hash": peer["canonical_semantic_sha256"] == "9845434c23b7f6d0791850586a307397d8de748c6ade666a472244f9626186f9",
    "source_hash": peer["source_sha256"] == "ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21",
    "N3_comparison": peer["N3_overlap"],
}
for key in ["norm_lower_ball", "norm_upper_ball"]:
    checks[key] = arb(own[key]).overlaps(arb(peer[key]))
assert all(checks.values()), checks
out = {
    "utc": datetime.now(timezone.utc).isoformat(),
    "checks": checks, "count": len(checks),
    "manifest_sha256": digest(REVIEW/"MANIFEST.json"),
    "peer_result_sha256": digest(REVIEW/"result.json"),
    "own_result_sha256": digest(own_path),
    "code_sha256": digest(__file__),
    "elapsed_seconds": time.monotonic()-start,
    "verdict": "CONFIRMED general polar third-tensor method and complete007 retained norm record",
    "method_scope": "Independent complex-derivative theorem/code audit and retained-record reassembly; two full arithmetic paths remain N3 Cartesian and N4 polar.",
}
with (REVIEW/"ACCEPTANCE.json").open("x") as f:
    json.dump(out, f, indent=2)
    f.write("\n")
print(out["verdict"], out["count"], "checks", out["elapsed_seconds"])
