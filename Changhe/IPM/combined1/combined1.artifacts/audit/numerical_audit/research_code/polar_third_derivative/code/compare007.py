"""Check the complete polar Q3 record against the frozen Cartesian result."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import sys
import time
from flint import arb, ctx, fmpq as Q

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "research/polar_third_derivative"
NAME = "C1-N1-007-d2w-j7-e2bal"
ctx.prec = 2048


def digest(path):
    h = sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def main():
    tick = time.monotonic()
    folder = BASE / "verification" / NAME
    full_path, manifest_path = folder / "full.json", folder / "manifest.json"
    full = json.loads(full_path.read_text())
    manifest = json.loads(manifest_path.read_text())
    assert full["candidate"] == NAME and full["complete"]
    assert full["completed_modes"] == manifest["modes"] == list(range(1, 320, 2))
    assert not full["missing_modes"]
    assert full["manifest_sha256"] == digest(manifest_path)
    assert all(digest(ROOT / name) == value for name, value in manifest["inputs"].items())
    assert full["code_sha256"] == digest(BASE / "code/check.py")
    assert manifest["components"] == 1360 and manifest["precision_bits"] == 2048
    assert manifest["weight_degree"] == 112
    peer_path = BASE / "source/N3_norms007_v03.json"
    peer_code = BASE / "source/N3_e2norms_v03.py"
    peer = json.loads(peer_path.read_text())
    assert digest(peer_path) == full["reference_sha256"]
    assert digest(peer_code) == peer["code_sha256"]
    canonical_path = ROOT / f"research/candidate_audits/data/{NAME}/canonical.json"
    canonical = json.loads(canonical_path.read_text())
    entries = {tuple(k): Q(v) for k, v in zip(canonical["order"], canonical["coefficients"]) if Q(v)}
    serial = "\n".join(",".join(map(str, k)) + ":" + str(v) for k, v in sorted(entries.items())) + "\n"
    semantic = sha256(serial.encode()).hexdigest()
    assert semantic == canonical["canonical_serialization_sha256"] == peer["canonical_sha256"]
    assert canonical["source_sha256"] == peer["source_sha256"]
    assert Q(canonical["cl"]) == Q(peer["cl"]) == Q(4076476460239181, 2251799813685248)
    previous_path = ROOT / "research/polar_derivative_norms/verification/candidate007_N3_comparison.json"
    previous = json.loads(previous_path.read_text())
    assert previous["source_sha256"] == peer["source_sha256"]
    assert previous["canonical_semantic_sha256"] == semantic
    mode_records = []
    for n in manifest["modes"]:
        path = folder / f"modes/mode_{n:03d}.json"
        rec = json.loads(path.read_text())
        assert digest(path) == full["mode_sha256"][str(n)]
        assert rec["manifest_sha256"] == digest(manifest_path) and rec["mode"] == n
        assert rec["symmetry_identities"] > 0
        for side in ("lower", "upper"):
            energy = arb(rec[f"energy_{side}_ball"])
            assert energy > 0 and energy.rel_accuracy_bits() > 150
        for endpoint in rec["endpoints"]:
            assert Q(endpoint["diagonal_exponent"]) > -1
        mode_records.append(rec)
    assert sum(r["symmetry_identities"] for r in mode_records) == full["symmetry_identities"] == 2720
    assert len(full["fixtures"]) == 12
    totals = {}
    for side in ("lower", "upper"):
        value = sum((arb(r[f"energy_{side}_ball"]) for r in mode_records), arb(0)).sqrt()
        assert value.overlaps(arb(full[f"norm_{side}_ball"]))
        totals[side] = value.str(80)
    other = peer["norms"]["Q3"]
    assert other["status"] == "FINITE"
    ol, ou = arb(full["norm_lower_ball"]), arb(full["norm_upper_ball"])
    pl, pu = arb(other["norm_lower_ball"]), arb(other["norm_upper_ball"])
    assert ol < ou and pl < pu and ol < pu and pl < ou
    result = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "candidate": NAME,
        "canonical_entries": len(entries),
        "canonical_semantic_sha256": semantic,
        "source_sha256": peer["source_sha256"],
        "modes": len(mode_records),
        "symmetry_identities": 2720,
        "fixture_count": 12,
        "own_lower_ball": full["norm_lower_ball"],
        "own_upper_ball": full["norm_upper_ball"],
        "peer_lower_ball": other["norm_lower_ball"],
        "peer_upper_ball": other["norm_upper_ball"],
        "intervals_overlap": True,
        "reassembled_total_balls": totals,
        "inputs": {
            str(p.relative_to(ROOT)): digest(p)
            for p in (full_path, manifest_path, peer_path, peer_code,
                      canonical_path, previous_path, Path(__file__))
        },
        "elapsed_seconds": time.monotonic() - tick,
        "status": "CONFIRMED complete candidate007 Q3; general formula peer review separate",
    }
    with (BASE / "verification/candidate007_N3_comparison.json").open("x") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
