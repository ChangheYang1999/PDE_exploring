"""Supplementary exact finite checks for the handwritten Gevrey-one proof."""
from fractions import Fraction
from math import comb
from pathlib import Path
from datetime import datetime, timezone
import json
from flint import arb, ctx


def main():
    ctx.prec = 256
    checks = []
    for n in range(2, 501):
        t = Fraction(n * n, 2 * (n - 1)) * sum(
            (Fraction(1, comb(n, i)) for i in range(1, n)), Fraction()
        )
        assert t < 2
        if n == 2:
            assert t == 1
        else:
            assert t <= Fraction(2 * n * (n - 2), (n - 1) ** 2)
        if n <= 12 or n in [50, 100, 500]:
            checks.append({"n": n, "T_n": str(t), "T_n_decimal": float(t)})
    s = arb(5).sqrt()
    delta = 1 / s
    c = (5 + s) / 4
    K = 55 + s
    H = 3240 * s - 3000
    D = 2 * H
    assert H < 4300 and D < 8600
    radius = ((4 * D).log() / delta).exp()
    out = {
        "checked_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "scope": "Finite exact checks supplement the written all-order proof; they do not prove convergence.",
        "binomial_majorant_checked_n": [2, 500],
        "selected_values": checks,
        "quadratic_irrational_constants_for_L_19_sigma_0_F_1": {
            "delta": str(delta), "c": str(c), "K": str(K), "H": str(H), "D": str(D),
            "R_for_q_one_quarter": str(radius), "H_lt_4300": True, "D_lt_8600": True,
        },
    }
    output = Path("research/04_gevrey/verification/majorant_checks.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(out, indent=2) + "\n")


if __name__ == "__main__":
    main()
