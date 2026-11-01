"""Check independent residual coefficients and print directed decimal bounds."""
from read_evidence_bytes import read_bytes as read_evidence_bytes
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json
import pickle
import time
from flint import arb, ctx, fmpq, fmpz


def dyadic(m, e):
    x = arb(fmpz(int(m))) * arb(2) ** int(e)
    assert x.is_exact()
    return x


def own_ball(v):
    return arb(dyadic(v[0], v[1]), dyadic(v[2], v[3]))


def peer_ball(v):
    m, e, r = v
    if "*2^" in r:
        a, b = r.split("*2^")
        radius = dyadic(a, b)
    else:
        radius = arb(r)
    return arb(dyadic(m, e), radius)


def qdyadic(m, e):
    return Fraction(int(m)) * Fraction(2) ** int(e)


def endpoint(v, upper):
    return qdyadic(v[0], v[1]) + (1 if upper else -1) * qdyadic(v[2], v[3])


def decimal_bound(q, upper, digits=6):
    assert q > 0
    e = len(str(q.numerator)) - len(str(q.denominator))
    while q < Fraction(10) ** e:
        e -= 1
    while q >= Fraction(10) ** (e + 1):
        e += 1
    scale = Fraction(10) ** (digits - 1 - e)
    z = q * scale
    n = z.numerator // z.denominator
    if upper and z.denominator != 1:
        n += 1
    s = str(n)
    out = s[0] + "." + s[1:] + "e" + str(e + len(s) - digits)
    assert Fraction(out) >= q if upper else Fraction(out) <= q
    return out


def main():
    start = time.monotonic()
    ctx.prec = 1152
    root = Path("research/56_sqrt5_residuals")
    own_path = root / "verification/coefficients.json"
    result_path = root / "verification/checks.json"
    peer_path = Path("../a4-num/ckpt/sqrt5_sin1_p1024.pkl")
    eval_path = Path("../a4-num/notes/eval_sqrt5_sin1_p1024.json")
    exact_path = Path("research/01_recurrence/verification/quadratic_field_comparison.json")
    raw = {str(p): read_evidence_bytes(p) for p in (own_path, result_path, peer_path, eval_path, exact_path)}
    own = json.loads(raw[str(own_path)])
    result = json.loads(raw[str(result_path)])
    peer = pickle.loads(raw[str(peer_path)])
    evaluation = json.loads(raw[str(eval_path)])
    exact = json.loads(raw[str(exact_path)])
    assert own["completed_order"] == result["completed_order"] == 161
    assert peer["N"] == 700 and peer["prec"] == 1024
    maximum_relative_difference = arb(0)
    comparisons = 0
    overlaps = 0
    legacy_radii = 0
    for name, short in (("density", "f"), ("stream", "g")):
        for ns, field in own[name].items():
            n = int(ns)
            amplitudes = {int(m): 2 * own_ball(v) for m, v in field["positive_coefficients"].items()}
            norm = sum(map(abs, amplitudes.values()), arb(0))
            assert norm > 0
            for index, v in enumerate(peer[short][n]):
                m = 2 * index + 1 if name == "density" else 2 * index
                x = amplitudes.get(m, arb(0))
                y = peer_ball(v)
                if v[2] != "0" and "*2^" not in v[2]:
                    legacy_radii += 1
                comparisons += 1
                overlaps += int(x.overlaps(y))
                relative = abs(x.mid() - y.mid()) / norm
                maximum_relative_difference = maximum_relative_difference.max(relative)
                assert relative < arb("1e-180"), (name, n, m, relative)
    assert overlaps == comparisons
    exact_checks = 0
    for row in exact["cases"][0]["recursion"]["rows"]:
        n = str(row["n"])
        for name in ("density", "stream"):
            for ms, encoded in row[name].items():
                a, b = encoded.split("|")
                q = arb(fmpq(a)) + arb(fmpq(b)) * arb(5).sqrt()
                x = 2 * own_ball(own[name][n]["positive_coefficients"][ms])
                assert x.overlaps(q), (name, n, ms)
                exact_checks += 1
    decimal_rows = []
    comparisons_eval = []
    for row in result["rows"]:
        ev = next(r for r in evaluation["rows"] if r["N"] == row["N"] and r["R"] == float(row["R"]))
        bounds = {}
        for name, b in row["bounds"].items():
            lo = endpoint(b["lower_ball"], False)
            hi = endpoint(b["upper_ball"], True)
            bounds[name] = [decimal_bound(lo, False), decimal_bound(hi, True)]
        for name, key in (("residual", "resid_k0"), ("theta", "resid_k1"),
                          ("theta2", "resid_k2"), ("increment", "tail_k0")):
            value = Fraction.from_float(ev[key])
            b = row["bounds"][name]
            assert endpoint(b["lower_ball"], False) <= value <= endpoint(b["upper_ball"], True)
            comparisons_eval.append(dict(N=row["N"], R=row["R"], quantity=name, peer_value=ev[key], enclosed=True))
        decimal_rows.append(dict(N=row["N"], R=row["R"], bounds=bounds))
    (root / "verification/outward_decimal_bounds.json").write_text(json.dumps(decimal_rows, indent=2) + "\n")
    retained = dict(source_checkpoint=str(peer_path), N=peer["N"], prec=peer["prec"],
                    c_l_pack=peer["c_l_pack"], delta_pack=peer["delta_pack"],
                    f={str(n): peer["f"][n] for n in range(1, 162)},
                    g={str(n): peer["g"][n] for n in range(1, 162)})
    (root / "sources/peer_prefix.json").write_text(json.dumps(retained) + "\n")
    (root / "sources/peer_evaluation.json").write_bytes(raw[str(eval_path)])
    out = dict(checked_at_utc=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
               hashes={p: sha256(b).hexdigest() for p, b in raw.items()},
               independent_coefficient_comparisons=comparisons, interval_overlaps=overlaps,
               peer_legacy_decimal_radius_count=legacy_radii,
               legacy_radius_scope="Peer decimal radii are not assumed to be directed enclosures. Independent exact-dyadic coefficient balls certify the residual bounds.",
               largest_norm_scaled_midpoint_difference=maximum_relative_difference.str(20),
               exact_quadratic_field_checks=exact_checks,
               peer_sampled_evaluation_checks=comparisons_eval,
               actual_elapsed_s=time.monotonic() - start)
    (root / "verification/cross_checks.json").write_text(json.dumps(out, indent=2) + "\n")
    (root / "sources/sqrt5_residual_certificate_audit.py.txt").write_bytes(Path(__file__).read_bytes())
    print(json.dumps({k: v for k, v in out.items() if k not in ("hashes", "peer_sampled_evaluation_checks")}, indent=2))
    for row in decimal_rows:
        print(row["N"], row["R"], row["bounds"]["residual"])


if __name__ == "__main__":
    main()
