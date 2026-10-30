"""Exact first sine mode, retaining all background-frequency interactions."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse
import gzip
import json
import sys
import time
from flint import fmpq as Q, fmpq_poly as Poly

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/"research/projected_residual"
sys.path.insert(0, str(ROOT/"research/radial_fourier/code"))
sys.path.insert(0, str(ROOT/"research/whole_plane_norms/code"))
from radial import Radial, T, pshift, put
from pipeline import source, load, DATA


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def candidate_source(name):
    if name.startswith("C1-N1-"):
        return ROOT/f"research/candidate_audits/data/{name}/canonical.json"
    return source(name)


def project(model):
    result = {}
    for (j, n), P in model.rho.items():
        if n != 1:
            continue
        TP = T*P.derivative()
        L = model.c*(2*TP-3*P+2*T*(model.p[j]*P-TP))-P
        put(result, j+1, pshift(L, 2))
    quadratic = {}
    counts = []
    for C, S in [(model.u1, model.rx), (model.ry, model.u2)]:
        count = 0
        for (i, n), P in C.items():
            for (j, m), QQ in S.items():
                twice_weight = int(m+n == 1)+int(m-n == 1)-int(m-n == -1)
                if twice_weight:
                    put(quadratic, i+j+2, P*QQ*Q(twice_weight, 2))
                    count += 1
        counts.append(count)
    for ell, P in quadratic.items():
        put(result, ell, pshift(P, 4))
    return {ell: P for ell, P in result.items() if P}, counts


def destination(name):
    return BASE/f"data/{name}_first_mode.json.gz"


def read_projection(name):
    path = destination(name)
    with gzip.open(path, "rt") as f:
        data = json.load(f)
    assert data["source_sha256"] == digest(candidate_source(name))
    result = {
        row["ell"]: Poly([int(x) for x in row["numerator"]])/Q(row["denominator"])
        for row in data["rows"]
    }
    return result, data


def run(name, compare):
    start = time.monotonic()
    path = candidate_source(name)
    model = Radial(path)
    projected, counts = project(model)
    elapsed_build = time.monotonic()-start
    print("built", name, "branches", len(projected), "pairs", counts,
          "seconds", elapsed_build, flush=True)
    comparison = {}
    if compare:
        full = load(name, 0)[0, 0]
        expected = {ell: P for (ell, kind, n), P in full.items() if kind == "s" and n == 1}
        assert projected == expected
        comparison = {
            "exact_full_residual_projection_match": True,
            "full_residual_sha256": digest(DATA/f"{name}_D0.json.gz"),
            "branches_compared": len(expected),
        }
    rows = [
        {"ell": ell, "numerator": [str(v) for v in P.numer()], "denominator": str(P.denom())}
        for ell, P in sorted(projected.items())
    ]
    output = {
        "schema": "N4-first-sine-residual-v1",
        "utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "candidate": name,
        "source_sha256": digest(path),
        "code_sha256": digest(Path(__file__)),
        "proof_sha256": digest(BASE/"PROOF.md"),
        "radial_code_sha256": digest(ROOT/"research/radial_fourier/code/radial.py"),
        "cl": str(model.c),
        "delta": str(model.delta),
        "nonzero_frequency_pairs": counts,
        "build_seconds": elapsed_build,
        **comparison,
        "rows": rows,
    }
    dest = destination(name)
    dest.parent.mkdir(parents=True, exist_ok=True)
    assert not dest.exists(), f"Refuse to replace existing projection {dest}"
    with gzip.open(dest, "wt", compresslevel=2) as f:
        json.dump(output, f, separators=(",", ":"))
    summary = {key: value for key, value in output.items() if key != "rows"}
    summary.update({
        "projection_sha256": digest(dest),
        "projection_bytes": dest.stat().st_size,
        "total_elapsed_seconds": time.monotonic()-start,
    })
    (BASE/"verification").mkdir(exist_ok=True)
    (BASE/f"verification/{name}_build.json").write_text(json.dumps(summary, indent=2)+"\n")
    print("saved", dest.name, "bytes", dest.stat().st_size,
          "comparison", bool(comparison), "seconds", summary["total_elapsed_seconds"], flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate")
    parser.add_argument("--compare-full", action="store_true")
    args = parser.parse_args()
    run(args.candidate, args.compare_full)
