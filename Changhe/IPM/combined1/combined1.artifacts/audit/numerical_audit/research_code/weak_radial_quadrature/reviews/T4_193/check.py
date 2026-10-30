"""Reconstruct the first residual mode, then audit frozen finite radial sums."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import gzip
import importlib.util
import json
import sys
import time
from flint import fmpq as Q, fmpq_poly as P, arb, arb_poly, ctx

sys.set_int_max_str_digits(0)
BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parent
HELPER = ROOT / "localized_probe_audit/code/reproduce.py"
spec = importlib.util.spec_from_file_location("t4_own_polar", HELPER)
f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)
ctx.prec = 2048
T, W, ZERO = f.T, f.W, f.ZERO


def digest(path):
    return sha256(Path(path).read_bytes()).hexdigest()


def ap(poly):
    return arb_poly([f.ar(v) for v in poly])


def primitive(poly, b, x):
    # Exact rational division of each coefficient, before Arb evaluation.
    coeff = P([v / (b + j + 1) for j, v in enumerate(poly)])
    return f.ar(x) ** f.ar(b + 1) * ap(coeff)(f.ar(x))


def main():
    start = time.monotonic()
    source = ROOT / "projected_laplacian/data/candidate007_canonical.json"
    projection = ROOT / "projected_laplacian/data/candidate007_mode1.json.gz"
    peerfile = BASE / "source/candidate007.json"
    assert digest(source) == "153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316"
    c, delta, rho, stream = f.fields(json.loads(source.read_text()))
    residual = {}
    drho = {key: f.td(v, (key[0]+1)*delta/2, 1) for key, v in rho.items()}
    ds = {key: f.td(v, (key[0]+1)*delta/2, 2) for key, v in stream.items()}

    def add(ell, poly):
        residual[ell] = residual.get(ell, ZERO) + poly

    for (j, n), v in rho.items():
        if n == 1:
            add(j+1, c*drho[j, n]-v)
    pairs = 0
    for (j, m), s in stream.items():
        for (i, n), r in rho.items():
            if abs(n-m) == 1:
                add(i+j+2, Q(1 if n > m else -1, 2) *
                    (-n*r*ds[j, m]-m*s*drho[i, n]))
                pairs += 1
    residual = {ell: p for ell, p in residual.items() if p}
    old = json.loads(gzip.decompress(projection.read_bytes()))
    expected = {row["ell"]: P([Q(int(v), int(row["denominator"]))
                for v in row["numerator"]]) for row in old["rows"]}
    assert residual == expected
    print("reconstructed", len(residual), "branches", pairs, "pairs",
          time.monotonic()-start, flush=True)
    peer = json.loads(peerfile.read_text())
    ks = [row["k"] for row in peer["rules"][0]["values"]]
    assert len(set(ks)) == len(ks)
    exact = {k: arb.pi()/2 * sum(
        (f.integral(p, ell*delta/2-1, k+1) for ell, p in residual.items()),
        arb(0)) for k in ks}
    split = {}
    for k in [0, 1, 2, 4, 8]:
        exterior = []
        for radius in [Q(1, 50), Q(10000)]:
            x = 1/(1+radius*radius)
            exterior.append(arb.pi()/2 * sum(
                (primitive(W**(k+1)*p(W), ell*delta/2-1, x)
                 for ell, p in residual.items()), arb(0)))
        split[k] = {"inside": exact[k]-exterior[0],
                    "middle": exterior[0]-exterior[1],
                    "outside": exterior[1]}
        for name, v in split[k].items():
            assert v.overlaps(arb(peer["exact_splits"][str(k)][name]))
    parts = [(ell, ap(p)) for ell, p in residual.items()]
    rows = []
    paths = [source, projection, peerfile, HELPER, Path(__file__), BASE/"PROOF.md"]
    for rule in peer["rules"]:
        tick = time.monotonic()
        order = rule["middle_order"]
        nodefile = BASE / f"source/nodes_mid{order}.json"
        paths.append(nodefile)
        nodes = json.loads(nodefile.read_text())["rational_radii_weights"]
        assert len(nodes) == rule["nodes"]
        sums = {k: arb(0) for k in ks}
        accuracy = []
        for rs, ws in nodes:
            r, weight = Q(rs), Q(ws)
            assert r > 0 and weight > 0
            tq = r*r/(1+r*r)
            wq = 1-tq
            t, w = f.ar(tq), f.ar(wq)
            val = sum((w**f.ar(ell*delta/2) * p(t)
                       for ell, p in parts), arb(0))
            accuracy.append(val.rel_accuracy_bits())
            assert accuracy[-1] > 100
            for k in ks:
                sums[k] += f.ar(weight) * t**(k+2) * val
        vals = []
        for row in rule["values"]:
            k = row["k"]
            finite = arb.pi()*sums[k]
            error = finite-exact[k]
            checks = {
                "finite_sum": finite.overlaps(arb(row["quadrature_ball"])),
                "whole_plane": exact[k].overlaps(arb(row["whole_plane_ball"])),
                "total_error": error.overlaps(arb(row["error_vs_whole_plane"])),
            }
            if k in split:
                checks["middle_error"] = (finite-split[k]["middle"]).overlaps(
                    arb(row["error_vs_exact_middle"]))
            assert all(checks.values()), (order, k, checks)
            vals.append({"k": k, "quadrature": finite.str(90),
                         "whole_plane": exact[k].str(90),
                         "error": error.str(90), "checks": checks})
        rows.append({"order": order, "nodes": len(nodes),
                     "minimum_accuracy_bits": min(accuracy),
                     "values": vals, "elapsed_seconds": time.monotonic()-tick})
        print("MID", order, "all checks passed",
              "seconds", time.monotonic()-tick, flush=True)
    output = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "precision_bits": ctx.prec,
        "field_projection_exact_equality": True,
        "nonlinear_frequency_pairs": pairs,
        "rows": rows,
        "splits": {str(k): {name: v.str(90) for name, v in row.items()}
                   for k, row in split.items()},
        "inputs": {str(p): digest(p) for p in paths},
        "elapsed_seconds": time.monotonic()-start,
        "scope": "Exact candidate, exact recorded finite node lists only."
    }
    dest = BASE / "verification/candidate007.json"
    with dest.open("x") as handle:
        json.dump(output, handle, indent=2)
        handle.write("\n")
    print("DONE", output["elapsed_seconds"], flush=True)


if __name__ == "__main__":
    main()
