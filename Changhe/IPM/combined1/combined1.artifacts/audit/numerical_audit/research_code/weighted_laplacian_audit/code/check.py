"""Cartesian-trace reproduction and coarse all-parameter comparison."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import gzip
import json
import sys
import time
from flint import arb, ctx, fmpq as Q, fmpq_poly as P

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "research/weighted_laplacian_audit"
sys.path.insert(0, str(ROOT / "research/whole_plane_norms/code"))
from pipeline import load, source
from norms import derivative, ar, T, U, ZERO


def digest(p):
    h = sha256()
    with Path(p).open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def run():
    start = time.monotonic()
    ctx.prec = 2048
    peerfile = BASE / "source/T4_d2_2048.json"
    peer = json.loads(peerfile.read_text())
    src = source("d2")
    assert peer["source_sha256"] == digest(src) == digest(BASE / "source/T4_d2.json")
    assert peer["code_sha256"] == digest(BASE / "source/T4_evaluate.py")
    assert peer["helper_sha256"] == digest(BASE / "source/T4_reproduce.py")
    assert peer["proof_sha256"] == digest(BASE / "source/T4_PROOF.md")
    c = Q(json.loads(src.read_text())["cl"])
    delta = 1 - 1 / c
    F = load("d2", 0)[0, 0]
    print("loaded", len(F), "seconds", time.monotonic() - start, flush=True)
    dx = derivative(F, 0, "x", delta)
    dy = derivative(F, 0, "y", delta)
    assert derivative(dx, 1, "y", delta) == derivative(dy, 1, "x", delta)
    dxx = derivative(dx, 1, "x", delta)
    dyy = derivative(dy, 1, "y", delta)
    lap = {key: dxx.get(key, ZERO) + dyy.get(key, ZERO) for key in set(dxx) | set(dyy)}
    lap = {key: V for key, V in lap.items() if V}
    td = lambda V, d: (1 - 2 * d * T) * V + 2 * T * U * V.derivative()
    polar = {key: td(td(V, key[0] * delta / 2), key[0] * delta / 2) - key[2]**2 * V
             for key, V in F.items()}
    polar = {key: V for key, V in polar.items() if V}
    assert set(polar) == set(lap)
    assert all(T * V == polar[key] for key, V in lap.items())
    print("Cartesian trace and polar identity", len(lap), time.monotonic() - start, flush=True)
    modes, diagonals = {}, []
    for (ell, kind, n), V in lap.items():
        assert kind == "s" and n > 0
        W = V(U)
        q = next(i for i, x in enumerate(W) if x)
        diagonals.append((ell, n, q))
        modes.setdefault(n, []).append((ell, W))
    groups = {}
    for terms in modes.values():
        for i, (ell, V) in enumerate(terms):
            for j in range(i, len(terms)):
                ell2, W = terms[j]
                b = (ell + ell2) * delta / 2 - 3
                groups[b] = groups.get(b, ZERO) + (1 if i == j else 2) * U * V * W
    terms = [(b + j + 1, ar(v)) for b, V in groups.items() for j, v in enumerate(V) if v]
    assert len(groups) == peer["square_power_groups"]
    assert len(terms) == peer["nonzero_monomials"]
    groupfile = BASE / "verification/d2_exact_power_groups.json.gz"
    assert not groupfile.exists()
    with gzip.open(groupfile, "wt", compresslevel=2) as f:
        json.dump({str(b): [str(v) for v in V] for b, V in sorted(groups.items())},
                  f, separators=(",", ":"))
        f.write("\n")
    print("grouped", len(groups), len(terms), time.monotonic() - start, flush=True)
    rows, norm_values = [], {}
    peerrows = {Q(row["a"]): row for row in peer["weights"]}
    A = 1 + 1 / c
    endpoints = [Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1), Q(5, 4), Q(3, 2), A]
    for a in endpoints:
        assert all(a + ell * delta + 2 * q - 2 > 0 for ell, n, q in diagonals)
        assert all(a + b > 0 for b, x in terms)
        E = sum((x / ar(a + b) for b, x in terms), arb(0))
        assert E > 0
        norm = (arb.pi() * E / 2).sqrt()
        lower = arb(5)**ar((a - 2) / 2) * norm
        ceiling = (8 * arb.pi()).sqrt() * ar((1 + c - c * a)**2 / (1 + a))
        values = {"weighted_laplacian_norm": norm, "Y_lower_bound": lower,
                  "necessary_residual_ceiling": ceiling}
        matches = {k: bool(v.overlaps(arb(peerrows[a][k]))) for k, v in values.items()} if a in peerrows else {}
        assert all(matches.values())
        rows.append({"a": str(a), **{k: v.str(100) for k, v in values.items()},
                     "peer_comparisons": matches})
        norm_values[a] = norm
        print("a", a, "J", norm.str(35), flush=True)
    cells = []
    for l, h in zip(endpoints[:-1], endpoints[1:]):
        lower = arb(5)**ar((l - 2) / 2) * norm_values[h]
        ceiling = (8 * arb.pi()).sqrt() * ar((1 + c - c * l)**2 / (1 + l))
        gap, ratio = lower - ceiling, lower / ceiling
        assert gap > 0 and ratio > 1
        cells.append({"left": str(l), "right": str(h), "lower_bound": lower.str(100),
                      "ceiling": ceiling.str(100), "positive_gap": gap.str(100),
                      "ratio_lower": ratio.str(100)})
    out = {
        "utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "candidate": "d2",
        "c": str(c), "a_upper": str(A), "precision_bits": ctx.prec,
        "source_sha256": digest(src), "peer_result_sha256": digest(peerfile),
        "code_sha256": digest(Path(__file__)), "proof_sha256": digest(BASE / "PROOF.md"),
        "derivative_code_sha256": digest(ROOT / "research/whole_plane_norms/code/norms.py"),
        "cache_sha256": digest(ROOT / "research/whole_plane_norms/data/d2_D0.json.gz"),
        "exact_power_groups_sha256": digest(groupfile),
        "residual_components": len(F), "laplacian_components": len(lap),
        "mixed_derivative_agreement": True, "cartesian_polar_exact_agreements": len(lap),
        "power_groups": len(groups), "nonzero_moments": len(terms),
        "weights": rows, "cover_cells": cells,
        "elapsed_seconds": time.monotonic() - start,
        "scope": "Peer point values reproduced; new scalar cover awaits peer. Scheme exclusion conditional on T4-097.",
    }
    target = BASE / "verification/d2.json"
    assert not target.exists()
    target.write_text(json.dumps(out, indent=2) + "\n")
    print("DONE", len(cells), "cells", time.monotonic() - start, flush=True)


if __name__ == "__main__":
    run()
