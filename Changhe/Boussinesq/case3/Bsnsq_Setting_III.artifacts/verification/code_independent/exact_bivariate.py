"""Own elementary rational polynomial ring with total-degree truncation.

This module does not use any stream center or tail formulas. It is used to
check those formulas by direct expansion, differentiation, and multiplication.
"""
from fractions import Fraction as Q


def clean(p):
    return {k: Q(v) for k, v in p.items() if v}


def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, Q(0))+v
    return clean(out)


def scale(p, a):
    return clean({k: a*v for k, v in p.items()})


def mul(p, q, degree):
    out = {}
    for (i, j), a in p.items():
        for (k, l), b in q.items():
            if i+j+k+l <= degree:
                key = (i+k, j+l)
                out[key] = out.get(key, Q(0))+a*b
    return clean(out)


def trunc(p, degree):
    return {k: v for k, v in p.items() if sum(k) <= degree and v}


def homogeneous(p, degree):
    return {k: v for k, v in p.items() if sum(k) == degree and v}


def diff(p, axis):
    out = {}
    for k, v in p.items():
        if k[axis]:
            key = list(k)
            key[axis] -= 1
            out[tuple(key)] = v*k[axis]
    return clean(out)


def lap(p):
    return add(diff(diff(p, 0), 0), diff(diff(p, 1), 1))


def power(p, n, degree):
    if type(n) is not int or n < 0:
        raise ValueError('nonnegative integer exponent required')
    out = {(0, 0): Q(1)}
    while n:
        if n % 2:
            out = mul(out, p, degree)
        p = mul(p, p, degree)
        n //= 2
    return out


def unit_power(p, exponent, degree):
    """Taylor polynomial of (1+p)^exponent, requiring p(0)=0."""
    if p.get((0, 0), 0):
        raise ValueError('nonzero constant in perturbation')
    out = {(0, 0): Q(1)}
    term = {(0, 0): Q(1)}
    coefficient = Q(1)
    for j in range(1, degree+1):
        term = mul(term, p, degree)
        if not term:
            break
        coefficient *= (Q(exponent)-j+1)/j
        out = add(out, scale(term, coefficient))
    return out


def cheb(p, n, degree):
    a, b = {(0, 0): Q(1)}, p
    if n == 0:
        return a
    for j in range(1, n):
        a, b = b, add(scale(mul(p, b, degree), 2), scale(a, -1))
    return b


def dot_grad(v, p, degree):
    return add(mul(v[0], diff(p, 0), degree), mul(v[1], diff(p, 1), degree))


def pde(beta, psi, theta, degree):
    omega = scale(lap(psi), -1)
    W = (add({(1, 0): beta}, scale(diff(psi, 1), -1)),
         add({(0, 1): beta}, diff(psi, 0)))
    ft = add(dot_grad(W, theta, degree), scale(theta, -(beta-2)))
    go = add(dot_grad(W, omega, degree), omega, scale(diff(theta, 0), -1))
    return ft, go


def ordinary_stream_jet(beta, labels, C, D, degree):
    """Expand elementary expressions directly, without center moment identities."""
    s = 1/Q(beta)
    r2 = {(2, 0): Q(1), (0, 2): Q(1)}
    x, x2, y = {(1, 0): Q(1)}, {(2, 0): Q(1)}, {(0, 1): Q(1)}
    rpower = lambda q: unit_power(r2, Q(q)/2, degree)
    u = add(scale(rpower(-s), 2), {(0, 0): Q(-1)})
    z = mul(y, rpower(-1), degree)
    us = {i: cheb(u, i, degree) for i, j, d in labels}
    zs = {j: cheb(z, j, degree) for i, j, d in labels}
    raws = {}
    psi, theta = {}, {}
    for (i, j, d), c, a in zip(labels, C, D):
        uv = mul(us[i], zs[j], degree)
        for kind, q, pre, coeff in [('C', 1-s-d, x, c),
                                    ('D', -1-2*s-d, x2, a)]:
            if not coeff:
                continue
            if q not in raws:
                raws[q] = rpower(q)
            term = scale(mul(pre, mul(raws[q], uv, degree), degree), coeff)
            if kind == 'C':
                psi = add(psi, term)
            else:
                theta = add(theta, term)
    psi.pop((1, 0), None)
    return psi, theta


def serialize(p):
    return [{'x_power': i, 'y_power': j, 'coefficient': str(v)}
            for (i, j), v in sorted(p.items(), key=lambda kv: (sum(kv[0]), kv[0]))]
