#!/usr/bin/env python3
"""Independently recompute the signed exterior M bound at radius30000."""
import hashlib
import json
import sys
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path
from flint import arb, ctx

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "coercivity_residual"))
from fields013 import C, SOURCE_HASHES, Evaluator, rational_arb
from asymptotics013 import Expansion


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    ctx.prec = 512
    price_path = HERE / "operator_theory/signed_matrix_far_price_v01.json"
    price = json.loads(price_path.read_text())
    assert price["source_hashes"] == SOURCE_HASHES
    for name, h in price["bindings"].items():
        assert sha(HERE / name) == h
    L2 = json.loads((HERE / "coercivity_residual/L2_signed_far_v05/result.json").read_text())
    assert price["signed_theta_origin"] == L2["far_theta"]
    e = Evaluator(512, 1, 1)
    ex = Expansion(e, "far", 12)
    radius = arb(30000)

    def scaled_field(name, i, j, shift):
        total = arb(0)
        for (_, _, p), a in ex.field(name, i, j).items():
            assert p + shift < 0
            total += arb(abs(a)) * radius ** rational_arb(p + shift)
        for a, p in ex.remainder_terms(name, i, j, radius):
            assert p + shift < 0
            assert a >= 0
            total += a * radius ** rational_arb(p + shift)
        return total

    u1 = scaled_field("u1", 0, 0, -1)
    u2 = scaled_field("u2", 0, 0, -1)
    ur = (u1*u1 + u2*u2).sqrt()
    strain = scaled_field("u1", 1, 0, 0) + (
        scaled_field("u1", 0, 1, 0) + scaled_field("u2", 1, 0, 0)) / 2
    theta = L2["far_theta"]
    assert radius > arb(theta["endpoint"])
    power = F(theta["common_gradient_power"])
    assert power < 0
    theta_bound = arb(theta["normalized_theta_upper"]).abs_upper() * radius ** (
        arb(power.numerator) / arb(power.denominator))
    c = rational_arb(C)
    lower = 1 - c/10 - c/(1+4*radius*radius) - ur - arb(21)/10*strain - theta_bound
    assert lower > arb(7)/10
    row = next(r for r in price["rows"] if r["radius"] == 30000)
    for value, key in [(ur, "u_over_r_upper"), (strain, "strain_upper"),
                       (theta_bound, "signed_K_loss_upper"), (lower, "matrix_lower")]:
        assert arb(row[key]).contains(value), (key, str(value), row[key])
    out = {
        "status": "ROOT_SIGNED_MATRIX_FAR_REPLAY_PASS",
        "finished_utc": datetime.now(timezone.utc).isoformat(),
        "source_hashes": SOURCE_HASHES,
        "price_result_sha256": sha(price_path),
        "program_sha256": sha(Path(__file__)),
        "radius": "30000", "precision_bits": ctx.prec,
        "recomputed_matrix_lower": lower.str(100),
        "all_required_field_and_remainder_powers_strictly_negative": True,
        "published_containment_checks": True,
        "scope": "Independent endpoint replay only; core coverage is a separate obligation.",
    }
    (HERE / "ROOT_SIGNED_MATRIX_FAR_REPLAY.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
