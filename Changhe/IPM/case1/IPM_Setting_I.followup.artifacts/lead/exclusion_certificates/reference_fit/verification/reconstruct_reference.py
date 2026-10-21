"""Numerical reconstruction from the exact frozen reference, not interval proof."""
import json
import resource
from fractions import Fraction as F
from pathlib import Path

resource.setrlimit(resource.RLIMIT_AS, (1_900_000_000, 1_900_000_000))
import mpmath as mp

ROOT = Path(__file__).resolve().parent.parent / "data"
mp.mp.dps = 65


def real(x):
    return mp.mpf(x.numerator) / x.denominator


if __name__ == "__main__":
    data = json.loads((ROOT / "fitted_reference.json").read_text())
    qr = [F(c) for c in data["q_power_coefficients_exact_decimal"]]
    coeff = list(map(real, qr))
    A = mp.mpf(data["A0_exact"])
    L = mp.mpf(data["L0_exact"])

    def q(t):
        return mp.polyval(list(reversed(coeff)), t)

    def H(t):
        return A - t * (1 - t*t) * q(t)

    integral = mp.quad(lambda t: (1+t)**2*q(t)/H(t),
                       [0, mp.mpf("0.25"), mp.mpf("0.5"),
                        mp.mpf("0.75"), 1])
    gs = mp.exp(integral/2)/2
    q1 = sum(qr)
    w2 = F(data["A0_exact"]) + 8*q1
    result = {
        "status": "numerical quadrature; no certified error bound",
        "working_decimal_digits": mp.mp.dps,
        "g_star_normalized_numerical": mp.nstr(gs, 40),
        "g_star_physical_numerical": mp.nstr(L*L*gs, 40),
        "q_at_1": mp.nstr(real(q1), 40),
        "q_at_1_exact_fraction": str(q1),
        "w_second_derivative_at_1": mp.nstr(real(w2), 40),
        "w_second_derivative_at_1_exact_fraction": str(w2),
        "log_integral": mp.nstr(integral, 40),
    }
    (ROOT / "reconstruction_numerical.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
