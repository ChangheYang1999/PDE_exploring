"""Exact arithmetic on the recorded candidate005 diagnostic table."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from hashlib import sha256
import json
import time

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "research/radial_mass"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def run():
    start = time.monotonic()
    name = "C1-N1-005-d2w-j7-x3"
    source = ROOT / f"research/candidate_audits/data/{name}/d2w_j7_n4_X3_mid180_diag2.json"
    data = json.loads(source.read_text())
    rows = data["dyadic"]
    exact = lambda x: Q(x) if isinstance(x, float) else Q(str(x))
    regions = {"near_0p25_to_2": (-2, 1), "middle_8_to_256": (3, 8),
               "middle_16_to_256": (4, 8)}
    results = {}
    for field, exterior in [("L2", exact(data["F2_far"])), ("gradF", Q(0)),
                            ("omD2F", Q(0))]:
        mass = {r["j"]: exact(r[field])**2 for r in rows}
        total = sum(mass.values(), exterior)
        assert total > 0
        results[field] = {
            "recorded_total_squared_mass": str(total),
            "fractions": {
                label: {"exact": str(sum(v for j, v in mass.items() if lo <= j < hi)/total),
                        "decimal": float(sum(v for j, v in mass.items() if lo <= j < hi)/total)}
                for label, (lo, hi) in regions.items()
            },
            "largest_recorded_annulus_index": max(mass, key=mass.get),
            "exterior_squared_mass_included": str(exterior),
        }
    result = {
        "utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source_sha256": digest(source), "candidate": name,
        "code_sha256": digest(Path(__file__)),
        "proof_sha256": digest(BASE / "DIAGNOSTIC_TABLE_AUDIT.md"),
        "results": results, "elapsed_seconds": time.monotonic()-start,
        "scope": "Exact arithmetic on recorded FLOAT diagnostics only; no quadrature certification.",
    }
    dest = BASE / "verification/candidate005_diagnostic_table.json"
    assert not dest.exists()
    dest.write_text(json.dumps(result, indent=2)+"\n")
    for field, row in results.items():
        print(field, {label: v["decimal"] for label, v in row["fractions"].items()},
              "largest j", row["largest_recorded_annulus_index"], flush=True)


if __name__ == "__main__":
    run()
