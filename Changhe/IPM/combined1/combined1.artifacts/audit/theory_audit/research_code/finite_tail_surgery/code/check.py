"""Exact third-tail construction and finite-order arithmetic."""
from pathlib import Path
from datetime import datetime, timezone
from math import gcd
import hashlib
import json
import sys
import time
from flint import fmpq as Q, arb, ctx

sys.set_int_max_str_digits(0)
ctx.prec = 768
BASE = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()


def decode(d):
    return {int(n): Q(v) for n, v in d.items() if Q(v)}


def encode(d):
    return {str(n): str(v) for n, v in sorted(d.items()) if v}


def put(out, n, value):
    if n < 0:
        n, value = -n, -value
    if n and value:
        out[n] = out.get(n, Q(0)) + value
        if not out[n]:
            del out[n]


def product(out, stream, density, ep, et):
    for m, a in stream.items():
        for n, b in density.items():
            z = a * b / 2
            put(out, n + m, z * (-et * m + (ep + 1) * n))
            put(out, n - m, z * (-et * m - (ep + 1) * n))


def residual(key, densities, streams, expo, c):
    k, l = key
    out = {n: (c * expo(key) - 1) * v
           for n, v in densities.get(key, {}).items()
           if (c * expo(key) - 1) * v}
    for k1 in range(1, k):
        for l1 in range(l + 1):
            p, t = (k1, l1), (k - k1, l - l1)
            product(out, streams.get(p, {}), densities.get(t, {}),
                    expo(p), expo(t))
    return out


def potential(a, target):
    mtop = (max(target) - 1) // 2
    assert a < 2 and all(a not in (2 * m, -2 * m)
                         for m in range(mtop + 1))

    def hm(m):
        return (-a * a * (a - 2) if m == 0 else
                -(a * a - 4 * m * m) * (a - 2 - 2 * m) / 2)

    def jm(m):
        return (a * a - 4 * m * m) * (a - 2 + 2 * m) / 2

    out, nxt = {}, Q(0)
    for m in range(mtop, -1, -1):
        out[m] = (target.get(2 * m + 1, Q(0)) - jm(m + 1) * nxt) / hm(m)
        nxt = out[m]
    return out


def fields(a, pot):
    density, stream = {}, {}
    for m, p in pot.items():
        n = 2 * m
        put(density, n + 1, -p * (a * a - n * n) * (a - 2 - n) / 2)
        put(density, n - 1, p * (a * a - n * n) * (a - 2 + n) / 2)
        put(stream, n + 2, p * (a - n) * (a - n - 2) / 4)
        put(stream, n - 2, -p * (a + n) * (a + n - 2) / 4)
    return density, stream


def norm(d):
    return (arb.pi() * arb(sum((v * v for v in d.values()), Q(0)))).sqrt()


def main():
    tick = time.monotonic()
    c = Q(4076476460239181, 2251799813685248)
    gamma, delta = 1 / c, 1 - 1 / c
    q1, q2, q3, qs = -1 - 4 * delta, 1 - 9 * delta, -1 - 5 * delta, gamma - 4
    expo = lambda k: 1 - k[0] * delta - 2 * k[1]
    assert q1 - delta == q3 < q2
    assert q2 - delta < qs < q3 < q2 < -3 < q1 < -2
    assert q3 - delta < qs and 2 * q3 - 1 < qs
    assert 2 * q2 - 1 < qs
    aa, bb = int(delta.numerator), int(delta.denominator)
    assert gcd(aa, bb) == 1 and aa % 2 == 1 and bb % 2 == 1
    bound = 1 - 2 * aa
    assert bound == -3649353293107865
    prefix = [(k, l) for k in range(1, 16) for l in range(4)
              if expo((k, l)) >= qs]
    through_minus5 = [(k, l) for k in range(1, 16) for l in range(4)
                      if expo((k, l)) > -5]
    assert all((expo(k) + 3).denominator != 1 or
               int(expo(k) + 3) % 2 for k in through_minus5)
    inputs = [BASE / "PROOF.md", Path(__file__)]
    manifest = json.loads((BASE / "source/MANIFEST.json").read_text())
    for record in manifest["files"]:
        assert sha(BASE / "source" / record["path"]) == record["sha256"]
    rows, previous = [], None
    for label in ("007", "013", "014"):
        sp, ep = (BASE / f"source/{label}_sectors.json",
                  BASE / f"source/{label}_endpoint.json")
        inputs.extend((sp, ep))
        sectors, end = json.loads(sp.read_text()), json.loads(ep.read_text())
        assert Q(sectors["c_exact"]) == c == Q(end["c"])
        th = {(r["K"], r["L"]): decode(r["density"]) for r in sectors["sectors"]}
        ps = {(r["K"], r["L"]): decode(r["stream"]) for r in sectors["sectors"]}
        for r in sectors["sectors"]:
            key = r["K"], r["L"]
            assert residual(key, th, ps, expo, c) == decode(r["residual"])
        assert th[(1, 0)] == decode(end["Theta0"])
        th[(1, 2)] = decode(end["Theta12"])
        astar = decode(end["F12"])
        assert residual((1, 2), th, ps, expo, c) == astar
        assert astar == {n: -4 * c * v for n, v in th[(1, 2)].items()}
        olda3 = residual((5, 1), th, ps, expo, c)
        th[(4, 1)], ps[(4, 1)] = {}, {}
        a3 = residual((5, 1), th, ps, expo, c)
        assert a3 and a3 != olda3
        assert residual((1, 2), th, ps, expo, c) == astar
        a2 = residual((9, 0), th, ps, expo, c)
        b2 = {n: v / (1 - c * q2) for n, v in a2.items()}
        p2 = potential(q2 + 3, b2)
        d2, s2 = fields(q2 + 3, p2)
        assert d2 == b2
        for n, v in d2.items():
            put(th[(9, 0)], n, v)
        for n, v in s2.items():
            put(ps[(9, 0)], n, v)
        assert not residual((9, 0), th, ps, expo, c)
        assert residual((5, 1), th, ps, expo, c) == a3
        assert residual((1, 2), th, ps, expo, c) == astar
        b3 = {n: v / (1 - c * q3) for n, v in a3.items()}
        p3 = potential(q3 + 3, b3)
        d3, s3 = fields(q3 + 3, p3)
        assert d3 == b3
        for n, v in d3.items():
            put(th[(5, 1)], n, v)
        for n, v in s3.items():
            put(ps[(5, 1)], n, v)
        remaining = {}
        for key in prefix:
            f = residual(key, th, ps, expo, c)
            if f:
                remaining[str(key)] = encode(f)
                assert key == (1, 2) and f == astar
        assert list(remaining) == ["(1, 2)"]
        assert previous is None or a3 == previous
        previous = a3
        na, nb = norm(a3), norm(b3)
        assert na > arb(191042) and na < arb(191043)
        assert nb > arb(27840) and nb < arb(27842)
        dst = BASE / f"data/{label}_third_repair.json"
        dst.write_text(json.dumps({
            "candidate": label, "q3": str(q3), "c": str(c),
            "residual_A3": encode(a3), "density_B3": encode(b3),
            "potential_cosine_coefficients": encode(p3),
            "stream_coefficients": encode(s3),
            "endpoint_residual_unchanged": encode(astar),
            "source_sector_sha256": sha(sp), "source_endpoint_sha256": sha(ep)
        }, indent=2) + "\n")
        rows.append({
            "candidate": label, "original_sector_maps_reproduced": len(sectors["sectors"]),
            "A3_changed_by_first_cutoff": True, "A3_preserved_by_second_cutoff": True,
            "A3_circle_norm": na.str(65), "B3_circle_norm": nb.str(65),
            "potential_modes": len(p3), "top_density_mode": max(b3),
            "third_density_reproduced": True,
            "only_nonzero_prefix_sector_after_third_cutoff": [1, 2],
            "endpoint_unchanged": True, "data_sha256": sha(dst)
        })
    result = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": time.monotonic() - tick,
        "inputs": {str(p): sha(p) for p in inputs},
        "exponents": {k: str(v) for k, v in zip(("q1", "q2", "q3", "qstar"), (q1, q2, q3, qs))},
        "nonresonance_threshold": bound,
        "lattice_prefix_count": len(prefix),
        "nonresonant_sectors_above_minus5": len(through_minus5),
        "rows": rows,
        "scope": "Finite-order audit; endpoint consequence remains conditional on OPEN T4-335."
    }
    (BASE / "verification/result.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "inputs"}, indent=2))


if __name__ == "__main__":
    main()
