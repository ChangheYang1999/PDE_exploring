"""Exact transcription and logical-scope checks of frozen numerics_v11."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from hashlib import sha256
import json
import re
import time

R = Path(__file__).resolve().parents[3]
B = R / "research/numerics_v11_audit"


def main():
    start = time.monotonic()
    inputs = {}
    checks = {}

    def bind(path, expected=None):
        path = Path(path)
        digest = sha256(path.read_bytes()).hexdigest()
        assert expected is None or digest == expected, path
        inputs[str(path.relative_to(R))] = digest
        return path

    def read(path):
        return json.loads(bind(path).read_text())

    manifest = read(B / "source/MANIFEST_v01.json")
    bind(B / "PROOF.md", manifest["proof_sha256"])
    bind(Path(__file__))
    for name, entry in manifest["files"].items():
        bind(B / "source" / name, entry["sha256"])
    report = (B / "source/numerics_v11.md").read_text()
    assert sha256(report.encode()).hexdigest() == (
        "700e76e9f13556033bfa2ea2dbbe0b6e93ed56a35e895b897ee718f629e11536"
    )
    assert report.count("RUN_1. Reading of the 016 family") == 2
    assert report.count("The 14 mid-field pairing rows of 021 were inert") == 3
    assert "020 is OPEN." in report
    checks["two_corrupted_header_references"] = True
    checks["three_unsupported_inert_attributions"] = True

    def ball(text):
        match = re.fullmatch(r"\[([^\s]+) \+/- ([^\]]+)\]", text)
        assert match, text
        center, radius = map(Q, match.groups())
        assert radius >= 0
        return center - radius, center + radius

    rounded = {
        16: "1.4704e-3",
        17: "1.6718e-3",
        18: "1.6558e-3",
        19: "1.6618e-3",
    }
    floor_rows = []
    for n, printed in rounded.items():
        topic = f"candidate{n:03d}_weak{'19' if n == 17 else ''}_peer"
        record = read(R / "research" / topic / "verification/result.json")
        assert record["verdict"].startswith("CONFIRMED")
        rows = [r for r in record["rows"] if (r["n"], r["K"]) == (19, 1800)]
        assert len(rows) == 1
        row = rows[0]
        floor = Q(row["strict_floor"])
        lower, upper = ball(row["radius_recomputed"])
        assert 0 < floor < lower <= upper
        assert f"{n:03d} > {printed}" in report
        display = Q(printed)
        safe = Q((floor * 10**7).__floor__(), 10**7)
        assert 0 < safe <= floor
        if n == 16:
            assert display > upper and safe == Q("0.0014703")
        else:
            assert display <= floor
        floor_rows.append({
            "candidate": n,
            "printed": printed,
            "accepted_strict_floor": str(floor),
            "root_lower": str(lower),
            "root_upper": str(upper),
            "display_licensed_by_accepted_floor": display <= floor,
            "display_above_root_upper": display > upper,
            "safe_7decimal_floor": str(safe),
        })
    checks["all_four_printed_floor_directions_checked"] = True
    checks["016_printed_floor_is_above_certified_root"] = True
    checks["017_018_019_printed_floors_are_safe"] = True

    statuses = []
    publication = datetime.fromisoformat("2026-10-29T10:45:46+00:00")
    for n in [20, 21]:
        record = read(R / f"research/candidate{n:03d}_weak_peer/verification/result.json")
        assert record["verdict"].startswith("CONFIRMED")
        assert datetime.fromisoformat(record["utc"]) < publication
        row = next(r for r in record["rows"] if (r["n"], r["K"]) == (19, 1800))
        assert Q(row["strict_floor"]) > Q(25, 54684)
        statuses.append({
            "candidate": n,
            "acceptance_utc": record["utc"],
            "accepted_strict_floor": row["strict_floor"],
            "accepted_before_v11": True,
        })
    checks["020_and_021_accepted_before_publication"] = True

    w = Q(10**12)
    a = Q(1, 200000)
    assert w * a * a == 25
    xstar = Q(25, 26)
    assert 2 * xstar + 50 * (xstar - 1) == 0
    assert 2 + 50 > 0
    assert 25 * (xstar - 1)**2 == Q(25, 676)
    fixtures = []
    for base in [10**7, 10**12, 10**20]:
        penalty = 25 * (xstar - 1)**2
        fraction = penalty / (base + xstar**2 + penalty)
        assert 0 < fraction < Q(1, base)
        fixtures.append({
            "constant": base,
            "minimizer_shift": str(xstar),
            "relative_penalty_at_minimum": str(fraction),
            "initial_relative_penalty": str(Q(25, base)),
        })
    checks["exact_penalty_counterexample"] = True
    assert all(checks.values())
    out = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "publication_utc": publication.isoformat(),
        "inputs": inputs,
        "checks": checks,
        "floor_rows": floor_rows,
        "accepted_statuses": statuses,
        "quadratic_fixtures": fixtures,
        "foreign_code_executed": False,
        "elapsed_seconds": time.monotonic() - start,
        "verdict": (
            "CONFIRMED transcription defects and three safe floor roundings; "
            "REFUTED 016 displayed number as a floor supplied by the cited certificate, "
            "020 OPEN as current accepted status, and inactivity inferred from value fraction; "
            "OPEN actual causal effect and unverified FLOAT trial values"
        ),
    }
    dest = B / "verification/result.json"
    with dest.open("x") as stream:
        json.dump(out, stream, indent=2)
        stream.write("\n")
    print(out["utc"], len(checks), "checks", sha256(dest.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
