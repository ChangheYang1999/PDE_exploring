"""Independent polar fields and direct factored hypergeometric moments."""
from pathlib import Path
from datetime import datetime, timezone
from functools import lru_cache
import argparse
import hashlib
import importlib.util
import json
import sys
import time
from flint import fmpq as Q, arb, ctx

sys.set_int_max_str_digits(0)
B = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("t4_polar026", B / "code/polar.py")
f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)
Rat, TR, VR, ar = f.Rat, f.TR, f.VR, f.ar
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


@lru_cache(None)
def beta(btext, L):
    b = Q(btext)
    assert b > -1 and isinstance(L, int) and L >= 0
    return ar(b + 1).gamma() * arb(L + 1).gamma() / ar(b + L + 2).gamma()


@lru_cache(None)
def pole(btext, L, atext, k):
    b, a = Q(btext), Q(atext)
    assert b > -1 and a > 0 and k > 0
    return beta(str(b), L) * (-ar(a)).hypgeom_2f1(
        arb(k), ar(b + 1), ar(b + L + 2), bc=True, abc=True
    )


def integrate(A, b, L, label):
    tick = time.monotonic()
    assert b > -1
    if not A:
        return arb(0), {"label": label, "exact_zero": True, "b": str(b), "L": L}
    numerator = f.V * A.numerator_v()
    denominator, rows = f.crt_data(A.powers)
    polynomial, remainder = divmod(numerator, denominator)
    moment = beta(str(b), L)
    value = arb(0)
    for j, coefficient in enumerate(polynomial):
        value += ar(coefficient) * moment
        moment *= ar((b + j + 1) / (b + j + L + 2))
    replay = polynomial * denominator
    count = 0
    for a, k, Di, Ei, inverse in rows:
        Ri = divmod(remainder * inverse, Di)[1]
        local = Ri(f.Poly([-1 / a, 1 / a]))
        for j, coefficient in enumerate(local):
            if coefficient:
                assert k - j > 0
                value += ar(coefficient) * pole(str(b), L, str(a), k - j)
                count += 1
        replay += Ri * Ei
    assert replay == numerator
    assert value.is_finite() and value.rel_accuracy_bits() > 150, (
        label, value.rel_accuracy_bits()
    )
    record = {
        "label": label, "b": str(b), "L": L,
        "denominator_powers": list(A.powers),
        "polynomial_degree": polynomial.degree(), "principal_parts": count,
        "exact_CRT_replay": True, "accuracy_bits": value.rel_accuracy_bits(),
        "value": value.str(100), "elapsed_seconds": time.monotonic() - tick,
    }
    print(label, "bits", value.rel_accuracy_bits(),
          "seconds", record["elapsed_seconds"], flush=True)
    return value, record


def groups_integral(groups, delta, offset, L, label):
    total, records = arb(0), []
    for ell, A in sorted(groups.items()):
        value, record = integrate(A, offset + ell * delta / 2, L, f"{label}:{ell}")
        total += value
        records.append(record)
    return total, records


def gradient(K, n, H):
    A, D = 2 * K + 1, 2 * K + 4
    aa, bb, cc = D * (K + 3), (K + 2) * A + (K + 1) * D, K * A
    discriminant = bb * bb - 4 * aa * cc
    assert discriminant > 0
    roots = [(bb - arb(discriminant).sqrt()) / (2 * aa),
             (bb + arb(discriminant).sqrt()) / (2 * aa)]
    assert all(0 < t and t < 1 for t in roots)
    values = [abs(t**K * (1 - t)**2 * (A - D * t)) for t in roots]
    t = ar(Q(K, K + 2))
    values.append(n * t**K * (1 - t)**2)
    assert all(value < ar(H) for value in values)
    return {
        "quadratic_coefficients": [aa, -bb, cc],
        "discriminant": discriminant, "H_upper_exact": str(H),
        "roots": [t.str(100) for t in roots],
        "amplitude_caps": [value.str(100) for value in values],
        "complete_critical_point_check": True,
    }


def fixtures():
    result = []
    for i, (powers, L, b) in enumerate([
        ((0, 0), 3, Q(-1, 3)), ((1, 0), 2, Q(1, 5)),
        ((3, 0), 5, Q(-3, 7)), ((0, 2), 4, Q(2, 7)),
        ((2, 1), 3, Q(7, 3)), ((2, 3), 6, Q(-2, 5)),
    ]):
        A = Rat(3 + f.T - 2 * f.T**2, powers)
        value, record = integrate(A, b, L, f"fixture:{i}")
        expanded, _ = f.integrate(A * TR**L, b, f"expanded:{i}")
        assert value.overlaps(expanded)
        result.append({**record, "expanded_localization_overlap": True})
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=int, default=23)
    parser.add_argument("--power", type=int, default=2400)
    parser.add_argument("--bits", type=int, default=2048)
    parser.add_argument("--skip-fixtures", action="store_true")
    args = parser.parse_args()
    for relative in ['PROOF.md', 'code/polar.py', 'code/rational.py',
                     'code/C_SYMMETRY.md', 'source/N4_PROOF.md',
                     'source/N4_moments_PROOF.md', 'source/N4_weak.py']:
        assert (B / relative).is_file(), relative
    ctx.prec = args.bits
    start = time.monotonic()
    n, K = args.mode, args.power
    assert n > 0 and n % 2 and K > 0 and K >= (n - 1) // 2
    fixture_records = [] if args.skip_fixtures else fixtures()
    source = B / "data/candidate026.json"
    point_path = B / "source/T4_point.json"
    probe_path = B / f"data/probe_n{n}_K{K}.json"
    peer_path = B / f"source/N4_n{n}_K{K}.json"
    data, reference, probe, peer = [
        json.loads(p.read_text()) for p in [source, point_path, probe_path, peer_path]
    ]
    assert sha(source) == peer["raw_sha256"] == (
        "2978faab0e8b4a1da1ec06991ebaf03eb9bfa7ed388b0dbbae9d955ca3a095f3"
    )
    assert (peer["n"], peer["K"]) == (probe["n"], probe["K"]) == (n, K)
    canonical007 = B.parent / "taylor_projection/source/canonical007.json"
    data007 = json.loads(canonical007.read_text())
    c0, d0, r0, s0 = f.fields(data007)
    co, do, ro, so = f.Old.fields(data007)
    assert c0 == co and d0 == do and set(r0) == set(ro) and set(s0) == set(so)
    assert all(A == Rat(ro[k]) for k, A in r0.items())
    assert all(A == Rat(so[k]) for k, A in s0.items())
    c, delta, rho, stream = f.fields(data)
    values = f.evaluation(c, delta, rho, stream, *reference["point"])
    point_checks = {k: bool(v.overlaps(arb(reference["fields"][k])))
                    for k, v in values.items()}
    assert all(point_checks.values()), point_checks
    assert any(A.powers[0] > 0 for A in list(rho.values()) + list(stream.values()))
    assert all(A.powers[1] == 0 for A in list(rho.values()) + list(stream.values()))
    print("fields", len(rho), len(stream), "point checks", point_checks,
          "seconds", time.monotonic() - start, flush=True)
    H = Q(probe["H_upper_exact"])
    sup = gradient(K, n, H)
    radial = (2 * K + 1) - (2 * K + 4) * TR
    A0 = (2 * c + 1) + c * radial
    Ds = {k: f.td(A, (k[0] + 1) * delta / 2, 2) for k, A in stream.items()}
    Dr = {k: f.td(A, (k[0] + 1) * delta / 2, 1) for k, A in rho.items()}
    modes = {(0, n): A0}
    for (j, m), S in stream.items():
        f.put(modes, j + 1, n + m, (n * Ds[j, m] - m * S * radial) / 2)
        f.put(modes, j + 1, n - m, (-n * Ds[j, m] - m * S * radial) / 2)
    modes = {k: A for k, A in modes.items() if A}
    by_mode = {}
    for (ell, m), A in modes.items():
        by_mode.setdefault(m, []).append((ell, A))
    mgroups, mpairs = {}, 0
    for rows in by_mode.values():
        for i, (ell, A) in enumerate(rows):
            for k, (ell2, C) in enumerate(rows[i:], i):
                f.add(mgroups, ell + ell2, A * C * (1 if i == k else 2))
                mpairs += 1
    print("M assembled", mpairs, "seconds", time.monotonic() - start, flush=True)
    mraw, mr = groups_integral(mgroups, delta, Q(1), 2 * K, "M2")
    M2 = arb.pi() / 2 * mraw
    cgroups, cpairs = {}, 0
    rr = list(rho.items())
    for ix, ((j, m), A) in enumerate(rr):
        for iy in range(ix, len(rr)):
            (k, l), C = rr[iy]
            multiplicity = 1 if ix == iy else 2
            ac = 2 * (m == l) - (abs(m - l) == 2 * n) + (m + l == 2 * n)
            bc = 2 * (m == l) - (abs(m - l) == 2 * n) - (m + l == 2 * n)
            if ac or bc:
                f.add(cgroups, j + k + 2, multiplicity *
                      (ac * Dr[j, m] * Dr[k, l] + bc * m * l * A * C))
                cpairs += multiplicity
    print("C assembled", cpairs, "seconds", time.monotonic() - start, flush=True)
    craw, cr = groups_integral(cgroups, delta, Q(1), 2 * K, "C2")
    C2 = arb.pi() / 8 * craw
    direct = {}
    for (j, m), R in rho.items():
        if m == n:
            f.add(direct, j + 1, c * Dr[j, m] - R)
    for (j, m), S in stream.items():
        for (k, l), R in rho.items():
            term = Rat()
            if l + m == n:
                term += (-m * S * Dr[k, l] + l * Ds[j, m] * R) / 2
            if abs(l - m) == n:
                term += (1 if l > m else -1) * (
                    -m * S * Dr[k, l] - l * Ds[j, m] * R
                ) / 2
            if term:
                f.add(direct, j + k + 2, term)
    iraw, ir = groups_integral(direct, delta, Q(-1), K, "I_direct")
    I = arb.pi() / 2 * iraw
    parts = {}
    for (j, m), R in rho.items():
        for (ell, l), A in modes.items():
            if l == m:
                f.add(parts, j + 1 + ell, R * A)
    praw, pr = groups_integral(parts, delta, Q(-1), K, "I_parts")
    Ip = -arb.pi() / 2 * praw
    assert I.overlaps(Ip) and M2 > 0 and C2 > 0
    M, C = M2.sqrt(), C2.sqrt()
    D = M + C
    radius = 2 * abs(I) / (D + (D * D + 4 * ar(H) * abs(I)).sqrt())
    results = {"pairing": I, "pairing_by_parts": Ip, "M2": M2, "C2": C2,
               "M": M, "C": C, "D": D, "radius": radius}
    comparisons = {k: bool(v.overlaps(arb(peer[k]))) for k, v in results.items()}
    assert all(comparisons.values()), comparisons
    floor = Q(peer["strict_lower_exact"])
    assert ar(floor) < radius and floor > Q(25, 54684)
    paths = [source, point_path, probe_path, peer_path, canonical007, Path(__file__),
             B / "PROOF.md", B / "code/polar.py", B / "code/rational.py",
             B / "code/C_SYMMETRY.md", B / "source/N4_PROOF.md",
             B / "source/N4_moments_PROOF.md", B / "source/N4_weak.py",
             B.parent / "weak_probe_audit/code/reproduce.py"]
    output = {
        "utc": datetime.now(timezone.utc).isoformat(), "candidate": peer["candidate"],
        "n": n, "K": K, "precision_bits": ctx.prec, "source_sha256": sha(source),
        "inputs": {str(p): sha(p) for p in paths},
        "fixtures": fixture_records, "R1_full_fields_exact": True,
        "actual_candidate_point_checks": point_checks,
        "density_terms": len(rho), "stream_terms": len(stream),
        "M_pairs": mpairs, "C_ordered_pairs": cpairs,
        "M_moments": mr, "C_moments": cr, "direct_moments": ir, "parts_moments": pr,
        "gradient_certificate": sup, "H_upper_exact": str(H),
        **{k: v.str(100) for k, v in results.items()},
        "comparisons": comparisons, "strict_lower_exact": str(floor),
        "exceeds_original_graded_ceiling": True,
        "elapsed_seconds": time.monotonic() - start,
        "verdict": "CONFIRMED independent polar and direct hypergeometric reproduction",
    }
    target = B / f"verification/n{n}_K{K}.json"
    with target.open("x") as stream_out:
        json.dump(output, stream_out, indent=2)
        stream_out.write("\n")
    print("DONE", output["utc"], "radius", radius.str(45),
          "seconds", output["elapsed_seconds"], flush=True)


if __name__ == "__main__":
    main()
