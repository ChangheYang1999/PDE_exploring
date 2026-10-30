"""Exact Green split at a prescribed rational circle."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
import argparse
import json
import sys
import time
from flint import arb, arb_poly, fmpq as Q, fmpq_poly as Poly, ctx

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/"research/negative_norm_split"
sys.path.insert(0, str(ROOT/"research/radial_fourier/code"))
sys.path.insert(0, str(ROOT/"research/whole_plane_norms/code"))
from radial import pshift, U, ar
from pipeline import load, source, DATA


def sha(path):
    return sha256(path.read_bytes()).hexdigest()


def ap(P):
    return arb_poly([ar(v) for v in P])


def mode(n, rows, endpoint):
    m = (n-1)//2
    logarithm = endpoint.log()
    inner_moment = arb(0)
    outer_moment = arb(0)
    As, Ds = [], []
    for b, P in rows:
        A = ap(U**n)*ap(P)
        D = arb_poly([ar(q)/ar(b+m-1+l) for l, q in enumerate(P)])
        As.append((b, A))
        Ds.append((b, D))
        for k, coefficient in enumerate(A):
            alpha = b-m-2+k
            integral = -(ar(alpha)*logarithm).expm1()/ar(alpha) if alpha else -logarithm
            inner_moment += coefficient*integral/2
        outer_moment += (ar(b+m-1)*logarithm).exp()*D(endpoint)/2
    groups = {}
    for b, A in As:
        for c, D in Ds:
            groups[b+c] = groups.get(b+c, arb_poly([]))+A*D
    full, outside = arb(0), arb(0)
    for bc, P in groups.items():
        power = (ar(bc-3)*logarithm).exp()
        for k, coefficient in enumerate(P):
            denominator = ar(bc-3+k)
            assert denominator > 0
            full += coefficient/denominator
            outside += coefficient*power/denominator
            power *= endpoint
    factor = arb.pi()/(4*n)
    full *= factor
    outside *= factor
    cross = arb.pi()/n*inner_moment*outer_moment
    inside = full-outside-cross
    assert full > 0 and outside > 0 and inside > 0, (n, full, outside, inside)
    return full, inside, cross, outside


def sanity():
    values = mode(1, [(Q(2), Poly([1]))], arb(1)/2)
    p = arb.pi()
    expected = [p/8, p*(3-4*arb(2).log())/32, p*(arb(2).log()-arb(1)/2)/8, 3*p/32]
    assert all(a.overlaps(b) for a, b in zip(values, expected))
    return {name: value.str(60) for name, value in zip(["full", "inner", "cross", "outer"], values)}


def run(name, radius, binary, bits):
    start = time.monotonic()
    ctx.prec = bits
    check = sanity()
    rational = Fraction(float(radius)) if binary else Fraction(radius)
    R = Q(rational.numerator, rational.denominator)
    assert R > 0
    endpoint = ar(1/(1+R*R))
    data = load(name, 0)[0, 0]
    raw = json.loads(source(name).read_text())
    delta = 1-1/Q(raw["cl"])
    modes = {}
    for (ell, kind, n), P in data.items():
        assert kind == "s" and n > 0 and n % 2 == 1
        normalized = pshift(P, (n-1)//2)(U)
        order = 0
        while order < len(normalized) and not normalized[order]:
            order += 1
        normalized = pshift(normalized, order)
        assert normalized
        b = ell*delta/2+order
        assert b > Q(3, 2)
        modes.setdefault(n, []).append((b, normalized))
    del data
    previous_path = ROOT/f"research/whole_plane_norms/verification/{name}_Hminus1_ball_{bits}.json"
    previous = json.loads(previous_path.read_text())
    refs = {row["n"]: arb.pi()*arb(row["squared_norm_div_pi"]) for row in previous["mode_contributions"]}
    totals = [arb(0) for _ in range(4)]
    records = []
    print("prepared", name, "R", radius, "modes", len(modes), "seconds", time.monotonic()-start, flush=True)
    for n, rows in sorted(modes.items()):
        values = mode(n, rows, endpoint)
        assert values[0].overlaps(refs[n]), (n, values[0], refs[n])
        for i, value in enumerate(values):
            totals[i] += value
        records.append({
            "n": n,
            **{key: value.str(80) for key, value in zip(["full", "inner", "cross", "outer"], values)},
            "prior_full_norm_overlap": True,
        })
        if n < 10 or n % 20 == 1:
            print("mode", n, "seconds", time.monotonic()-start, flush=True)
    out = {
        "utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "candidate": name,
        "radius_input": radius,
        "radius_exact": str(R),
        "radius_parser": "exact value of supplied binary64" if binary else "exact decimal rational",
        "precision_bits": bits,
        "source_sha256": sha(source(name)),
        "residual_sha256": sha(DATA/f"{name}_D0.json.gz"),
        "prior_full_norm_sha256": sha(previous_path),
        "code_sha256": sha(Path(__file__)),
        "proof_sha256": sha(BASE/"PROOF.md"),
        "synthetic_check": check,
        "squared_norm_contributions": {
            key: value.str(80) for key, value in zip(["full", "inner", "cross", "outer"], totals)
        },
        "mode_contributions": records,
        "elapsed_seconds": time.monotonic()-start,
        "scope": "Exact radial Green split; N4-ORIGIN pending independent reproduction.",
    }
    (BASE/"verification").mkdir(exist_ok=True)
    dest = BASE/f"verification/{name}_R{radius}_{bits}.json"
    assert not dest.exists(), f"Refuse to replace {dest}"
    dest.write_text(json.dumps(out, indent=2)+"\n")
    print(out["squared_norm_contributions"], "seconds", out["elapsed_seconds"], flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate")
    parser.add_argument("radius")
    parser.add_argument("--binary64-radius", action="store_true")
    parser.add_argument("--bits", type=int, default=2048)
    args = parser.parse_args()
    run(args.candidate, args.radius, args.binary64_radius, args.bits)
