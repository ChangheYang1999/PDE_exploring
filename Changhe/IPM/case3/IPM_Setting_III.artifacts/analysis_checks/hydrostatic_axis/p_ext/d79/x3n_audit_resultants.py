"""Independent exact recomputation from A.3.80, using Newton identities.

Run with one CPU thread and a memory limit:
timeout 540 /bin/sh -c 'ulimit -v 1900000;
  export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1;
  /usr/bin/python3 -B audit_resultants.py'
"""
import json
import time
from pathlib import Path

import sympy as s

eta, x, v, shift = s.symbols("eta x v shift")


def reduced(expr):
    return s.cancel(expr)


def numerator(expr):
    """Numerator in lowest terms, then remove only its integer content."""
    num, den = s.fraction(reduced(expr))
    poly = s.Poly(num, x, eta, domain=s.ZZ).primitive()[1]
    return poly.as_expr(), den


def powers(coefficients, count):
    """Power sums for v^r + c_1 v^(r-1) + ... + c_r."""
    degree = len(coefficients)
    result = [s.Integer(degree)]
    for k in range(1, count + 1):
        value = sum(
            coefficients[j - 1] * result[k - j]
            for j in range(1, min(k, degree + 1))
        )
        if k <= degree:
            value += k * coefficients[k - 1]
        result.append(reduced(-value))
    return result


def type_i(a0, theta1, theta2, m):
    d = a0 + 2 * theta1 + m * theta2
    T = a0 * eta - d
    delta = theta1 - theta2
    b2 = reduced(((T + delta) * x * eta - (T + 2 * delta) * eta**2) / T)
    p1 = powers([-x, b2], m + 1)
    c = list(s.symbols("c1:" + str(m + 1)))
    for k in range(1, m):
        pk = powers(c, k)[k]
        moment = a0 * (eta - 1)**k + theta1 * p1[k] + theta2 * pk
        pivot = s.diff(moment, c[k - 1])
        assert reduced(pivot + k * theta2) == 0
        c[k - 1] = reduced(-moment.subs(c[k - 1], 0) / pivot)
    poly2 = v**m + sum(c[j - 1] * v**(m - j) for j in range(1, m + 1))
    relation = delta * eta * s.diff(poly2, v).subs(v, eta) - T * poly2.subs(v, eta)
    assert reduced(s.diff(relation, c[-1]) + T) == 0
    c[-1] = reduced(relation.subs(c[-1], 0) / T)
    p2 = powers(c, m + 1)
    for k in range(1, m):
        assert reduced(a0 * (eta - 1)**k + theta1 * p1[k] + theta2 * p2[k]) == 0
    moments = [a0 * (eta - 1)**k + theta1 * p1[k] + theta2 * p2[k]
               for k in (m, m + 1)]
    return d, [numerator(q) for q in moments]


def type_ii(a0, a1, a2, b):
    d = a0 + a1 + a2 + 2 * b
    T = a0 * eta - d
    S = (T + a1 - b) * eta - T * x
    y = reduced(eta * ((T + a1 + a2 - 2 * b) * eta - (T + a2 - b) * x) / S)
    assert reduced(
        eta * ((a1 - b) * (eta - y) + (a2 - b) * (eta - x))
        + T * (eta - x) * (eta - y)
    ) == 0
    b3 = reduced(-(a0 * (eta - 1) + a1 * x + a2 * y) / b)
    b4 = reduced((a0 * (eta - 1)**2 + a1 * x**2 + a2 * y**2 + b * b3**2) / (2 * b))
    p2 = powers([-b3, b4], 3)
    for k in (1, 2):
        assert reduced(a0 * (eta - 1)**k + a1 * x**k + a2 * y**k + b * p2[k]) == 0
    M3 = a0 * (eta - 1)**3 + a1 * x**3 + a2 * y**3 + b * p2[3]
    poly = (v - x) * (v - y) * (v**2 - b3 * v + b4)
    derivative = s.diff(poly, v).subs(v, eta)
    return d, [numerator(q) for q in (M3, derivative)]


CASES = [
    ("(1; 3, 2, 1, 1)", "II", (1, 6, 4, 2)),
    ("(1; 2, 2, 1, 1, 1)", "I", (1, 4, 2, 3)),
    ("(1; 4, 2, 1, 1)", "II", (1, 8, 4, 2)),
    ("(1; 3, 2, 2, 1)", "II", (1, 6, 2, 4)),
    ("(3; 3, 2, 1, 1)", "II", (3, 6, 4, 2)),
    ("(1; 2, 2, 2, 1, 1)", "I", (1, 2, 4, 3)),
    ("(3; 2, 2, 1, 1, 1)", "I", (3, 4, 2, 3)),
    ("(1; 2, 2, 1, 1, 1, 1)", "I", (1, 4, 2, 4)),
]


def compute_case(label, kind, params):
    start = time.monotonic()
    print("START", label, kind, params, flush=True)
    d, equations = (type_i if kind == "I" else type_ii)(*params)
    n1, n2 = [a for a, _ in equations]
    print("NUMERATORS",
          [(s.degree(q, x), s.degree(q, eta), len(s.Poly(q, x, eta).terms())) for q in (n1, n2)],
          "seconds", round(time.monotonic() - start, 2), flush=True)
    R = s.Poly(s.resultant(n1, n2, x), eta, domain=s.ZZ)
    assert not R.is_zero
    lam = R.primitive()[1]
    if lam.LC() < 0:
        lam = -lam
    # Horner composition gives exact integer shifted coefficients.
    shifted = s.Poly(lam.as_expr().subs(eta, shift + d + 2).expand(), shift, domain=s.ZZ)
    cs = shifted.all_coeffs()
    least = min(cs)
    factors = s.factor_list(lam.as_expr(), eta)
    record = {
        "pattern": label, "type": kind, "parameters": params, "d": d,
        "N1": str(n1), "N2": str(n2),
        "denominators": [str(s.factor(b)) for _, b in equations],
        "numerator_degrees_x": [int(s.degree(q, x)) for q in (n1, n2)],
        "degree": lam.degree(), "least_shifted_coefficient": str(least),
        "least_coefficient_powers": [len(cs)-1-i for i, a in enumerate(cs) if a == least],
        "all_positive": all(a > 0 for a in cs),
        "coefficients_descending": [str(a) for a in lam.all_coeffs()],
        "shifted_coefficients_descending": [str(a) for a in cs],
        "factorization": str(factors),
        "elapsed_seconds": round(time.monotonic() - start, 3),
    }
    print("RESULT", label, "degree", record["degree"], "least", least,
          "powers", record["least_coefficient_powers"],
          "positive", record["all_positive"], "seconds", record["elapsed_seconds"], flush=True)
    print("FACTORS", factors, flush=True)
    return record


if __name__ == "__main__":
    records = []
    for case in CASES:
        records.append(compute_case(*case))
        Path("resultants.json").write_text(json.dumps(records, indent=2) + "\n")
