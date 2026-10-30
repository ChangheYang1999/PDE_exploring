"""Bind the independent T4 quotient-map reproduction to N4's exact files."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import time

BASE = Path(__file__).resolve().parents[1]
D = BASE / "reviews/T4_230"
H = lambda p: sha256(Path(p).read_bytes()).hexdigest()
start = time.monotonic()
manifest = json.loads((D / "MANIFEST.json").read_text())
for name, row in manifest["files"].items():
    assert H(D / name) == row["sha256"]
peer = json.loads((D / "map_result.json").read_text())
ownpath = BASE / "verification/007_legendre/result.json"
own = json.loads(ownpath.read_text())
assert H(D / "PROOF.md") == peer["proof_sha256"]
assert H(D / "check_map.py") == peer["code_sha256"]
checks = {
    "original007.json": own["source_sha256"],
    "canonical007.json": own["canonical_sha256"],
    "reduced_exact.json": H(BASE / "verification/007_legendre/reduced_exact.json"),
    "coordinate_map.json": H(BASE / "verification/007_legendre/coordinate_map.json"),
    "N4_QUOTIENT_result.json": H(ownpath),
}
assert checks == peer["inputs"]
assert checks["reduced_exact.json"] == own["reduced_sha256"]
assert checks["coordinate_map.json"] == own["map_sha256"]
assert peer["original_columns"] == own["generator_count"] == 2982
assert peer["selected_columns"] == own["reduced_dimension"] == 1922
assert peer["verified_unit_nonpivot_relations"] == own["zero_potential_dimension"] == 1060
for key in ["selected_shapes_equal", "transformed_coefficients_equal", "whole_canonical_maps_equal"]:
    assert peer[key] is True
assert peer["rank_dependency"] == "T4-195 independent exact rank1922"
for key in ["all_kernel_relations_exact", "all_potential_coefficients_preserved",
            "canonical_check_passed", "second_reduction_identical"]:
    assert own[key] is True
out = {
    "utc": datetime.now(timezone.utc).isoformat(),
    "verdict": "CONFIRMED N4-175 concrete exact quotient map by independent T4-230",
    "peer_result_sha256": H(D / "map_result.json"),
    "own_result_sha256": H(ownpath),
    "manifest_sha256": H(D / "MANIFEST.json"),
    "proof_sha256": H(D / "ACCEPTANCE_PROOF.md"),
    "code_sha256": H(__file__),
    "checked_input_hashes": checks,
    "original_columns": 2982,
    "selected_columns": 1922,
    "unit_nonpivot_relations": 1060,
    "peer_elapsed_seconds": peer["elapsed_seconds"],
    "local_acceptance_elapsed_seconds": time.monotonic() - start,
}
with (D / "ACCEPTANCE.json").open("x") as stream:
    json.dump(out, stream, indent=2)
    stream.write("\n")
print(json.dumps(out, indent=2))
