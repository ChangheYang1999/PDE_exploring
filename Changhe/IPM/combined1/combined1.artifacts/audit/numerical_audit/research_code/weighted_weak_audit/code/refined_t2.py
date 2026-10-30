"""Directed checks for six peer-selected weighted weak probes."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
from fractions import Fraction
import json
import time
from flint import arb, arb_poly, ctx, fmpq as Q
from check import (candidate_source, Radial, read_projection, destination,
                   groups, ap, ar, U, maximum, integral)

BASE = Path(__file__).resolve().parents[1]
CASES = {
    "state131": [("1", 32768, "0.000517550"),
                 ("6/5", 32768, "0.0001980444")],
    "d2": [("1", 288, "0.007810675"), ("6/5", 192, "0.004928906")],
    "Mpen2": [("1", 96, "0.02242667"), ("6/5", 64, "0.01587303")],
}


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def run():
    start = time.monotonic()
    ctx.prec = 2048
    target = BASE / "verification/T2_refined_2048.json"
    assert not target.exists()
    out = {
        "utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "precision_bits": ctx.prec, "rows": [],
        "code_sha256": digest(Path(__file__)),
        "proof_sha256": digest(BASE / "PROOF_REFINED.md"),
        "peer_files": {p.name: digest(p) for p in sorted((BASE / "peer_review/T2_081").iterdir())},
    }
    for name, cases in CASES.items():
        source = candidate_source(name)
        model = Radial(source)
        projected, _ = read_projection(name)
        F = [(ell, ap(P(U))) for ell, P in projected.items()]
        bg = groups(model, ["u1", "u2"])
        cg = groups(model, ["rho_x", "rho_y"])
        for aa, k, bound in cases:
            a = Q(aa)
            CU = arb(2) if a == 1 else ar(Q(808233, 500000))
            weight = arb_poly([5, 2 * k - 4])
            ell = arb_poly([ar(1 - model.c), ar(2 * model.c * (k + 2))])
            A2 = arb.pi() / 2 * integral(ell * ell, 1 - a, 2 * k + 1)
            B2 = arb.pi() / 2 * sum(
                (integral(P * weight * weight, b - a, 2 * k + 1) for b, P in bg.items()), arb(0))
            C2 = arb.pi() / 2 * sum(
                (integral(P, b - a, 2 * k + 1) for b, P in cg.items()), arb(0))
            assert A2 > 0 and B2 > 0 and C2 > 0
            A, B, C = A2.sqrt(), B2.sqrt(), C2.sqrt()
            D = A + B + CU * C
            pair = arb.pi() / 2 * sum(
                (integral(P, ell * model.delta / 2 - 1, k + 1) for ell, P in F), arb(0))
            H = maximum(k, 2 - a) + 2 * k * maximum(k, 3 - a) + 4 * maximum(k + 1, 2 - a)
            I = abs(pair)
            assert I > 0
            radius = 2 * I / (D + (D * D + 4 * CU * H * I).sqrt())
            rational_bound = Fraction(bound)
            assert radius > ar(Q(rational_bound.numerator, rational_bound.denominator)), (name, aa, k, bound, radius)
            values = {"pairing": pair, "A": A, "B_upper": B, "C_upper": C,
                      "D": D, "gradient_sup_upper": H, "weighted_L2_radius_lower": radius}
            out["rows"].append({
                "candidate": name, "a": aa, "k": k,
                "source_sha256": digest(source), "projection_sha256": digest(destination(name)),
                "peer_claimed_decimal_lower_bound": bound,
                "strict_lower_bound_passes": True,
                **{key: value.str(85) for key, value in values.items()},
            })
            print(name, aa, k, radius.str(35), flush=True)
    out["elapsed_seconds"] = time.monotonic() - start
    target.write_text(json.dumps(out, indent=2) + "\n")


if __name__ == "__main__":
    run()
