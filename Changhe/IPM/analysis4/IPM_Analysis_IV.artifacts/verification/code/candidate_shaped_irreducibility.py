"""Replay the Candidate-shaped degree-nine irreducibility certificate."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import sys
import time

sys.dont_write_bytecode = True
sys.set_int_max_str_digits(0)
from exact_polynomial_certificates import irreducibility_certificate

root = Path("research/156_candidate_shaped_compatibility")
start = time.monotonic()
source = root / "verification/polynomial.json"
data = json.loads(source.read_text())
coefficients = list(map(int, data["primitive_coefficients_ascending"]))
assert len(coefficients) == 10
assert coefficients[-1] % 229
certificate = irreducibility_certificate(coefficients, 229)
assert certificate["monic_coefficients_ascending"] == [
    92, 87, 130, 11, 207, 30, 127, 32, 131, 1
]
result = dict(
    checked_at_utc=datetime.now(timezone.utc).isoformat(timespec="seconds"),
    all_checks_pass=True,
    irreducible_over_Q=True,
    source_sha256=sha256(source.read_bytes()).hexdigest(),
    prime=229,
    modular_certificate=certificate,
    actual_elapsed_s=time.monotonic() - start,
)
(root / "verification/modular_irreducibility_replay.json").write_text(
    json.dumps(result, indent=2) + "\n"
)
(root / "sources/candidate_shaped_irreducibility.py").write_bytes(
    Path(__file__).read_bytes()
)
print(json.dumps(result), flush=True)
