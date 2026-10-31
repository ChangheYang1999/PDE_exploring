"""70-digit normalized solid harmonics with literal product derivatives.

The recurrence is the independent normalized complex convention, including
Condon-Shortley phase. No production tables or derivative ladders are used.
Exact rational polynomial checks qualify this faster reference separately.
"""
from decimal import Decimal, localcontext
from functools import lru_cache
from itertools import combinations_with_replacement
import math
import mpmath as mp


@lru_cache(None)
def derivative_axes(order):
    return tuple(ax for k in range(order + 1) for ax in combinations_with_replacement(range(3), k))


class AngularReference:
    def __init__(self, lmax, order=1, digits=70):
        self.lmax, self.order, self.digits = int(lmax), int(order), int(digits)
        self.axes = derivative_axes(order)
        self.counts = [tuple(ax.count(i) for i in range(3)) for ax in self.axes]
        lookup = {a: i for i, a in enumerate(self.counts)}
        self.lower = [[lookup.get(tuple(n - int(j == k) for j, n in enumerate(a))) for k in range(3)] for a in self.counts]
        self.lower2 = [[lookup.get(tuple(n - 2 * int(j == k) for j, n in enumerate(a))) for k in range(3)] for a in self.counts]
        with mp.workdps(digits + 20):
            cv = lambda x: Decimal(mp.nstr(x, digits + 15))
            self.h00 = cv(1 / mp.sqrt(4 * mp.pi))
            self.sqrt2 = cv(mp.sqrt(2))
            self.diag = {m: cv(-mp.sqrt(mp.mpf(2 * m + 1) / (2 * m))) for m in range(1, lmax + 1)}
            self.vert = {m: cv(mp.sqrt(2 * m + 3)) for m in range(lmax)}
            self.ab = {(l, m): (cv(mp.sqrt(mp.mpf(4 * l * l - 1) / (l * l - m * m))),
                                     cv(mp.sqrt(mp.mpf((2 * l + 1) * ((l - 1) ** 2 - m * m)) / ((2 * l - 3) * (l * l - m * m)))))
                       for m in range(lmax + 1) for l in range(m + 2, lmax + 1)}

    def values(self, point, modes):
        with localcontext() as ctx:
            ctx.prec = self.digits
            xyz = [Decimal.from_float(float(x)) for x in point]
            r2 = sum(x * x for x in xyz)
            z0 = Decimal(0)
            nderiv = len(self.axes)

            def linear(h, k):
                result = []
                for i, a in enumerate(self.counts):
                    v = xyz[k] * h[i]
                    if a[k]: v += a[k] * h[self.lower[i][k]]
                    result.append(v)
                return result

            def quadratic(h):
                result = []
                for i, a in enumerate(self.counts):
                    v = r2 * h[i]
                    for k in range(3):
                        if a[k]: v += 2 * a[k] * xyz[k] * h[self.lower[i][k]]
                        if a[k] > 1: v += a[k] * (a[k] - 1) * h[self.lower2[i][k]]
                    result.append(v)
                return result

            data = {(0, 0): ([self.h00] + [z0] * (nderiv - 1), [z0] * nderiv)}
            for m in range(self.lmax + 1):
                if m:
                    hr, hi = data[m - 1, m - 1]
                    xr, xi, yr, yi = linear(hr, 0), linear(hi, 0), linear(hr, 1), linear(hi, 1)
                    c = self.diag[m]
                    data[m, m] = ([c * (x - y) for x, y in zip(xr, yi)], [c * (x + y) for x, y in zip(xi, yr)])
                if m < self.lmax:
                    data[m + 1, m] = tuple([self.vert[m] * v for v in linear(h, 2)] for h in data[m, m])
                for l in range(m + 2, self.lmax + 1):
                    a, b = self.ab[l, m]
                    data[l, m] = tuple([a * x - b * y for x, y in zip(linear(h1, 2), quadratic(h2))]
                                           for h1, h2 in zip(data[l - 1, m], data[l - 2, m]))
            out = []
            for l, m, kind in modes:
                factor = (self.sqrt2 * (-1 if m % 2 else 1)) if m else Decimal(1)
                out.append([factor * v for v in data[int(l), int(m)][int(kind)]])
            return out
