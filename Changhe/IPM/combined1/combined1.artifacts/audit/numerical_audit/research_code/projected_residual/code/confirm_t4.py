"""Check the independent polar weak-probe results for the three snapshots."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import time
from flint import arb, ctx

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[1]
PEER = ROOT / "research/localized_weak_probe/peer_review"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def run():
    start = time.monotonic()
    ctx.prec = 1024
    rows = []
    for name in ["C1-N1-002-7branch-frf", "C1-N1-003-8branch-frf",
                 "C1-N1-004-4branch-l2fw"]:
        peer_path = BASE / f"peer_review/T4_{name}_2048.json"
        target_path = BASE / f"verification/{name}_probe_2048.json"
        peer = json.loads(peer_path.read_text())
        target = json.loads(target_path.read_text())
        source = ROOT / f"research/candidate_audits/data/{name}/canonical.json"
        checks = {
            "code": peer["code_sha256"] == digest(PEER / "T4_reproduce.py"),
            "helper": peer["helper_sha256"] == digest(PEER / "T4_helper.py"),
            "proof": peer["proof_sha256"] == digest(PEER / "T4_PROOF.md"),
            "canonical": peer["canonical_sha256"] == digest(source),
            "target": peer["peer_sha256"] == digest(target_path),
            "own_source": target["source_sha256"] == digest(source),
        }
        assert all(checks.values()), checks
        refs = {row["k"]: row for row in target["probes"]}
        comparisons = []
        for row in peer["rows"]:
            values = {
                key: bool(arb(row[key]).overlaps(arb(refs[row["k"]][key])))
                for key in ["pairing", "A", "B_weighted", "C", "D",
                            "gradient_sup_upper_ball", "L2_radius_lower"]
            }
            assert all(values.values()) and all(row["comparisons"].values())
            assert arb(row["L2_radius_lower"]) > 0
            comparisons.append({
                "k": row["k"], "checks": values,
                "L2_radius_lower": row["L2_radius_lower"],
            })
        rows.append({
            "candidate": name, "peer_result_sha256": digest(peer_path),
            "target_sha256": digest(target_path),
            "source_checks": checks, "comparisons": comparisons,
        })
    result = {
        "utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "rows": rows, "component_comparisons": sum(7*len(r["comparisons"]) for r in rows),
        "review_sha256": digest(ROOT / "research/localized_weak_probe/REVIEW_T4.md"),
        "code_sha256": digest(Path(__file__)),
        "elapsed_seconds": time.monotonic()-start,
        "scope": "The twelve tested necessary L2 radii; not an optimal radius or an existence claim.",
    }
    dest = BASE / "verification/T4_confirmation.json"
    assert not dest.exists()
    dest.write_text(json.dumps(result, indent=2)+"\n")
    print("confirmed", result["component_comparisons"], "components;",
          result["elapsed_seconds"], "seconds", flush=True)


if __name__ == "__main__":
    run()
