"""Directed conversions and exact comparisons for the final floats of certificates (s2-num)."""
import math
from flint import arb


def fup(x):
    """float >= the exact upper end of the ball x"""
    u = x.upper(); f = float(u)
    while arb(f) < arb(u): f = math.nextafter(f, math.inf)
    return f


def flo(x):
    """float <= the exact lower end of the ball x"""
    l = x.lower(); f = float(l)
    while arb(f) > arb(l): f = math.nextafter(f, -math.inf)
    return f


def max_upper(balls):
    """the ball whose exact upper end is largest (exact dyadic comparison, no float ties)"""
    best = None
    for b in balls:
        if best is None or arb(b.upper()) > arb(best.upper()): best = b
    return best


def finite_or_raise(f, what):
    if not math.isfinite(f): raise ValueError("non-finite certificate value: " + what)
    return f
