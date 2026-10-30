"""Exact binomial panel approximants with rigorous integral remainder bounds."""
from math import comb
from flint import arb, fmpq as Q, fmpq_poly as Poly


def ar(x):
    x = Q(x)
    return arb(x.numerator) / x.denominator


def partition(factors):
    maximum = max((a for a, m in factors), default=Q(0))
    if maximum <= 1:
        return [(Q(0), Q(1))]
    left, right = Q(0), 1 / maximum
    panels = []
    while left < 1:
        panels.append((left, right))
        left, right = right, min(2 * right, Q(1))
    return panels


def tail_order(m, q, tolerance):
    if not q:
        return 0, Q(0)
    k = 0
    omitted = m * q
    while True:
        ratio = q * Q(m + k + 1, k + 2)
        if ratio < 1:
            error = omitted / (1 - ratio)
            if error <= tolerance:
                return k, error
        omitted *= ratio
        k += 1
        if k > 10000:
            raise RuntimeError("Binomial truncation exceeds declared work limit")


def factor_approximation(a, m, left, right, tolerance):
    center = (left + right) / 2
    d = 1 + a * center
    q = a * (right - left) / (2 * d)
    assert 0 <= q <= Q(1, 3)
    order, error = tail_order(m, q, tolerance)
    z = Poly([-a * center / d, a / d])
    coefficients = [Q((-1) ** k * comb(m + k - 1, k)) for k in range(order + 1)]
    approximation = Poly(coefficients)(z) / d**m
    error /= d**m
    bound = (1 + a * left) ** (-m)
    return approximation, error, bound, order, q


def power_integral(polynomial, exponent, left, right):
    upper = ar(right) ** ar(exponent + 1)
    lower = ar(left) ** ar(exponent + 1) if left else arb(0)
    result = arb(0)
    for k, coefficient in enumerate(polynomial):
        if coefficient:
            result += ar(coefficient) * (upper - lower) / ar(exponent + k + 1)
        upper *= ar(right)
        lower *= ar(left)
    return result


def integral(exponent, numerator, raw_factors, tolerance=Q(1, 2**120)):
    exponent = Q(exponent)
    numerator = Poly([Q(x) for x in numerator])
    factors = [(Q(a), int(m)) for a, m in raw_factors]
    assert exponent > -1 and tolerance > 0
    assert all(a >= 0 and m >= 1 for a, m in factors)
    records = []
    total = arb(0)
    total_error = arb(0)
    for left, right in partition(factors):
        polynomial = Poly([1])
        approximations = []
        for a, m in factors:
            A, E, B, order, q = factor_approximation(a, m, left, right, tolerance)
            polynomial *= A
            approximations.append((E, B, order, q))
        error = Q(0)
        for i, (E, B, order, q) in enumerate(approximations):
            term = E
            for j, (Ej, Bj, kj, qj) in enumerate(approximations):
                if j < i:
                    term *= Bj + Ej
                elif j > i:
                    term *= Bj
            error += term
        numerator_bound = sum(
            (abs(value) * right**k for k, value in enumerate(numerator)), Q(0)
        )
        value = power_integral(numerator * polynomial, exponent, left, right)
        remainder = ar(error * numerator_bound) * power_integral(
            Poly([1]), exponent, left, right
        )
        assert remainder >= 0
        total += value
        total_error += remainder
        records.append({
            "left": str(left), "right": str(right),
            "orders": [entry[2] for entry in approximations],
            "q_exact": [str(entry[3]) for entry in approximations],
            "factor_errors_exact": [str(entry[0]) for entry in approximations],
            "product_error_exact": str(error),
            "numerator_bound_exact": str(numerator_bound),
            "approximant_integral": value.str(90),
            "remainder_upper_ball": remainder.str(90),
        })
    lower = (total - total_error).lower()
    upper = (total + total_error).upper()
    return {
        "lower": lower, "upper": upper,
        "approximant": total, "remainder": total_error,
        "panels": records,
    }
