"""Independent lower-bound cell arithmetic and an upper-bound misuse fixture."""
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import contextlib
import importlib.util
import io
import json
import time
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "research/dyadic_complete_cover"


def digest(p):
    return sha256(Path(p).read_bytes()).hexdigest()


def aq(q):
    q = Q(q)
    return arb(q.numerator) / q.denominator


def write(name, value):
    with (BASE / "verification" / name).open("x") as f:
        json.dump(value, f, indent=2)
        f.write("\n")


def main():
    tick = time.monotonic()
    manifest_path = BASE / "source/MANIFEST.json"
    manifest = json.loads(manifest_path.read_text())
    for name, value in manifest["files"].items():
        assert digest(ROOT / name) == value
    path = BASE / "source/N3_dyadic_lap_test.py"
    spec = importlib.util.spec_from_file_location("frozen_n3_dyadic", path)
    peer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(peer)
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        rows = peer.run(str(BASE / "source/zero_norm_fixture.json"))
    assert len(rows) == 1 and rows[0][3]
    write("upper_bound_counterexample.json", {
        "utc": datetime.now(timezone.utc).isoformat(),
        "actual_norm_at_every_weight": "0",
        "input_enclosure": ["0", "1000"],
        "frozen_checker_excludes_zero_residual": True,
        "stdout": output.getvalue(),
        "peer_rows": rows,
        "checker_sha256": digest(path),
        "manifest_sha256": digest(manifest_path),
        "status": "REFUTED generic exclusion logic: upper bounds do not prove a necessary-test failure",
    })
    ctx.prec = 768
    c = Q(4076476460239181, 2251799813685248)
    assert Q(3, 2) < 1 + 1/c
    src = ROOT / "research/candidate007_laplacian_fast/verification/N3_comparison_v01.json"
    data = json.loads(src.read_text())
    assert data["candidate"] == "C1-N1-007-d2w-j7-e2bal"
    assert data["complete_modes"] == 160 and data["weights_compared"] == 11
    assert data["source_sha256"] == "ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21"
    grid = [Q(x) for x in ("0", "1/5", "1/4", "2/5", "1/2", "3/5", "3/4", "4/5", "1", "5/4", "3/2")]
    norms = {Q(row["a"]): arb(row["own_norm"]) for row in data["rows"]}
    assert sorted(norms) == grid

    def bound(a):
        return (8*arb.pi()).sqrt()*aq(1+c-c*a)**2/aq(1+a)

    point_rows = []
    for a in grid:
        z = 1+c-c*a
        assert z > 0 and 2*c*(1+a)+z > 0
        r = arb(5)**aq((a-2)/2)*norms[a]/bound(a)
        assert r > 1
        point_rows.append({"a": str(a), "ratio_ball": r.str(70)})
    cells = []
    floors = []
    for l, h in zip(grid[:-1], grid[1:]):
        ratio = arb(5)**aq((l-2)/2)*norms[h]/bound(l)
        assert ratio > 1
        # Integer comparisons establish a safe floor; no floating cast is used.
        scale = 10**8
        lo, hi = 0, 10**14
        while hi-lo > 1:
            mid = (lo+hi)//2
            if ratio > aq(Q(mid, scale)):
                lo = mid
            else:
                hi = mid
        floor = Q(lo, scale)
        assert ratio > aq(floor)
        floors.append(floor)
        cells.append({"l": str(l), "h": str(h), "ratio_ball": ratio.str(70),
                      "strict_rational_floor": str(floor), "excludes_entire_cell": True})
    assert min(floors) > Q(1386, 1000)
    result = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "candidate": data["candidate"],
        "complete_interval": ["0", "3/2"],
        "admissible_scope": "0<a<=3/2, with all NC-T-DYADIC-LAP hypotheses",
        "point_rows": point_rows,
        "cells": cells,
        "minimum_strict_floor": str(min(floors)),
        "all_ten_cells_excluded": True,
        "norm_input_sha256": digest(src),
        "code_sha256": digest(__file__),
        "proof_sha256": digest(BASE / "PROOF.md"),
        "manifest_sha256": digest(manifest_path),
        "elapsed_seconds": time.monotonic()-tick,
        "status": "CONFIRMED candidate007 ten-cell arithmetic using actual containing norm balls",
    }
    write("candidate007.json", result)
    print(json.dumps({"utc": result["utc"], "minimum_strict_floor": str(min(floors)),
                      "cells": len(cells), "elapsed_seconds": result["elapsed_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
