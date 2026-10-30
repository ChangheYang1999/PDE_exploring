"""Exact partial fractions and outward real radial moments."""
from math import comb
from flint import fmpq as Q, fmpq_poly as Poly, arb

V = Poly([0, 1])


def ar(value):
    value = Q(value)
    return arb(value.numerator) / arb(value.denominator)


def normalize(factors):
    merged = {}
    for a, m in factors:
        a = Q(a)
        assert isinstance(m, int) and m > 0 and a > 0
        merged[a] = merged.get(a, 0) + m
    return sorted(merged.items())


def truncate(P, size):
    return Poly(list(P)[:size])


def decompose(numerator, raw_factors):
    """Return Q and principal parts; replay their full exact identity."""
    N = Poly([Q(c) for c in numerator])
    factors = normalize(raw_factors)
    D = Poly([1])
    for a, m in factors:
        D *= (1 + a*V)**m
    polynomial, remainder = divmod(N, D)
    parts = []
    for a, m in factors:
        shift = Poly([-1/a, 1/a])
        local = truncate(remainder(shift), m)
        for other, power in factors:
            if other == a:
                continue
            constant = 1 - other/a
            ratio = (other/a) / constant
            assert constant != 0
            expansion = Poly([
                Q((-1)**k * comb(power+k-1, k)) * ratio**k / constant**power
                for k in range(m)
            ])
            local = truncate(local * expansion, m)
        for k, coefficient in enumerate(local):
            if coefficient:
                parts.append((a, m-k, coefficient))
    replay = polynomial * D
    for a, k, coefficient in parts:
        quotient, residue = divmod(D, (1+a*V)**k)
        assert not residue
        replay += coefficient * quotient
    assert replay == N
    return polynomial, parts, factors, D.degree()


def pole_moments(b, a, maximum):
    b, a = Q(b), Q(a)
    assert b > -1 and a > 0 and maximum >= 0
    values = [ar(1/(b+1))]
    if maximum:
        first = (-ar(a)).hypgeom_2f1(
            arb(1), ar(b+1), ar(b+2), bc=True, abc=True
        ) / ar(b+1)
        assert first.is_finite()
        values.append(first)
    for k in range(2, maximum+1):
        values.append((ar((1+a)**(1-k)) - ar(b-k+2)*values[-1])/(k-1))
    return values


def integral(b, numerator, factors):
    b = Q(b)
    assert b > -1
    polynomial, parts, merged, degree = decompose(numerator, factors)
    total = sum((ar(c/(b+j+1)) for j, c in enumerate(polynomial)), arb(0))
    cache = {a: pole_moments(b, a, m) for a, m in merged}
    for a, k, coefficient in parts:
        total += ar(coefficient) * cache[a][k]
    assert total.is_finite()
    return total, {
        "b": str(b),
        "factors": [[str(a), m] for a, m in merged],
        "denominator_degree": degree,
        "polynomial_degree": polynomial.degree(),
        "principal_parts": len(parts),
        "exact_reconstruction": True,
        "relative_accuracy_bits": total.rel_accuracy_bits(),
    }
