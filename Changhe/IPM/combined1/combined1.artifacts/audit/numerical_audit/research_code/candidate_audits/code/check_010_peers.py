"""Register the independent polar reproduction of the exact multiscale point."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import time
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "research/candidate_audits"
PEER = BASE / "peer_review/T4_010"
NAME = "C1-N1-010-d2w-j7-x3bal-legqs"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


start = time.monotonic()
ctx.prec = 1024
own_path = ROOT / f"research/generator_sector_audit/verification/{NAME}_direct.json"
peer_path = PEER / "verification/results.json"
own = json.loads(own_path.read_text())
peer = json.loads(peer_path.read_text())
assert own["candidate"] == peer["candidate"] == NAME
assert own["point"] == peer["point"]
assert digest(PEER / "source/N4_result.json") == digest(own_path)
assert digest(PEER / "data/candidate010.json") == own["generator_sha256"]
for relative, expected in peer["inputs"].items():
    assert digest(PEER / relative) == expected, relative

checks = {
    f"field:{key}": bool(arb(value).overlaps(arb(peer["fields"][key])))
    for key, value in own["fields"].items()
}
for key in ("uniform_graded_upper", "uniform_graded_gap"):
    checks[key] = bool(arb(own[key]).overlaps(arb(peer[key])))
checks["uniform_positive"] = bool(arb(peer["uniform_graded_gap"]) > 0)
for row, other in zip(own["ball_exclusions"], peer["ball_exclusions"], strict=True):
    assert all(row[k] == other[k] for k in ("framework", "s", "radius"))
    for key in ("upper", "gap"):
        checks[f"{row['framework']}:{key}"] = bool(
            arb(row[key]).overlaps(arb(other[key]))
        )
    checks[f"{row['framework']}:positive"] = bool(arb(other["gap"]) > 0)
assert all(checks.values()), checks
inputs = [
    own_path, peer_path, PEER / "PROOF.md", PEER / "code/check.py",
    PEER / "data/candidate010.json", PEER / "source/N4_result.json",
]
out = {
    "utc": datetime.now(timezone.utc).isoformat(),
    "candidate": NAME,
    "precision_bits": ctx.prec,
    "checks": checks,
    "inputs": {str(p.relative_to(ROOT)): digest(p) for p in inputs},
    "code_sha256": digest(Path(__file__)),
    "elapsed_seconds": time.monotonic() - start,
    "verdict": "CONFIRMED N4-123 exact multiscale point and named necessary exclusions",
}
target = BASE / "verification/010_peer_comparison.json"
assert not target.exists()
target.write_text(json.dumps(out, indent=2) + "\n")
print(out["verdict"], len(checks), "checks", out["elapsed_seconds"], flush=True)
