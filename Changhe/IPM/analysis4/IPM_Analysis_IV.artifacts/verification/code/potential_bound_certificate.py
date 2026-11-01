"""Rational fixed-point certificate for a uniform potential inverse bound.

No floating-point arithmetic is used. Every interval endpoint is an integer
multiple of 2**(-256); operations round outward by exact integer division.
"""
from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json

BITS = 256
SCALE = 1 << BITS


def ceildiv(a, b):
    return -((-a) // b)


@dataclass(frozen=True)
class Interval:
    lo: int
    hi: int

    def __post_init__(self):
        assert self.lo <= self.hi

    @staticmethod
    def of(value):
        return value if isinstance(value, Interval) else Interval(value*SCALE, value*SCALE)

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __add__(self, other):
        other = self.of(other)
        return Interval(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __sub__(self, other):
        return self + (-self.of(other))

    def __rsub__(self, other):
        return self.of(other) + (-self)

    def __mul__(self, other):
        other = self.of(other)
        products = [a*b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return Interval(min(products)//SCALE, ceildiv(max(products), SCALE))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.of(other)
        assert other.lo > 0 or other.hi < 0, 'division interval contains zero'
        pairs = [(a*SCALE, b) for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return Interval(min(a//b for a, b in pairs), max(ceildiv(a,b) for a,b in pairs))

    def __rtruediv__(self, other):
        return self.of(other) / self

    def __abs__(self):
        if self.lo >= 0:
            return self
        if self.hi <= 0:
            return -self
        return Interval(0, max(-self.lo, self.hi))


def validate_rounding():
    from fractions import Fraction
    for a, b, c, d in [(-7, 13, 5, 9), (4, 7, -3, 11), (5, 17, 0, 1), (-11, 7, -8, 3)]:
        x, y = Interval.of(a)/b, Interval.of(c)/d
        xf, yf = Fraction(a,b), Fraction(c,d)
        tests = [(x+y, xf+yf), (x-y, xf-yf), (x*y, xf*yf), (abs(x), abs(xf))]
        if c:
            tests.append((x/y, xf/yf))
        for enclosure, exact in tests:
            assert Fraction(enclosure.lo,SCALE) <= exact <= Fraction(enclosure.hi,SCALE)


def main():
    validate_rounding()
    sqrt_lo = isqrt(5*SCALE*SCALE)
    assert sqrt_lo*sqrt_lo < 5*SCALE*SCALE < (sqrt_lo+1)*(sqrt_lo+1)
    sqrt5 = Interval(sqrt_lo, sqrt_lo+1)
    delta = 1/sqrt5
    assert (18*delta).lo >= 8*SCALE
    # The all-order tail estimate is 400*sqrt(5), strictly below 900.
    assert (400*sqrt5).hi < 900*SCALE
    rows = []
    for n in range(1,18):
        x = (n*delta-2)/2
        q = 4-n*delta
        K = 10*n-1
        largest_lo = largest_hi = 0
        upper_column = None
        for col in range(K+1):
            ds = [Interval.of(0) for _ in range(col+2)]
            for m in range(col,0,-1):
                ds[m] = ((1 if m==col else 0)-(m+1-x)*ds[m+1])/(m+x)
            ds[0] = ((1 if col==0 else 0)-(1-x)*ds[1])/(2*x)
            norm = sum((abs(ds[m]/(q*q-4*m*m)) for m in range(col+1)),Interval.of(0))
            assert norm.hi < 900*SCALE
            largest_lo = max(largest_lo, norm.lo)
            if norm.hi > largest_hi:
                largest_hi = norm.hi
                upper_column = col
        rows.append({
            'n':n, 'matrix_columns_checked':K+1,
            'operator_norm_lower_numerator':str(largest_lo),
            'operator_norm_upper_numerator':str(largest_hi),
            'denominator':str(SCALE),
            'strict_integer_upper_bound':ceildiv(largest_hi,SCALE),
            'largest_upper_bound_column':upper_column,
            'all_columns_below_900':True,
        })
    out = {
        'checked_at_utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'method':'Exact integer fixed-point interval arithmetic, outward rounding, 256 fractional bits',
        'delta':'1/sqrt(5)', 'density_bandwidth_bound':'20*n-1',
        'sqrt5_lower_numerator':str(sqrt_lo), 'sqrt5_upper_numerator':str(sqrt_lo+1),
        'sqrt5_denominator':str(SCALE), 'sqrt5_square_check':True,
        'first_tail_order':18, 'tail_bound':'400*sqrt(5)<900',
        'uniform_potential_inverse_bound':900,
        'finite_orders':rows,
    }
    path=Path('research/06_conditional_convergence/verification/potential_bound.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print('Certified all 1530 early matrix columns and the analytic tail bound below 900.')


if __name__=='__main__':
    main()
