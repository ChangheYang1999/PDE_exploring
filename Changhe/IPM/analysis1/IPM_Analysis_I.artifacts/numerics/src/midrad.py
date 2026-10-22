"""Rigorous midpoint-radius arithmetic on numpy float64 arrays (round-to-nearest only, no directed rounding).

Model (IEEE binary64, gradual underflow, no overflow): RN(z) = z (1 + delta) + xi, |delta| <= u = 2^-53, |xi| <= eta/2,
eta = 2^-1074 (xi = 0 for +,-).  Rules (astra/plan1 answer, item 5; Rump 1999, Rump-Zimmermann-Boldo-Melquiond 2009):
  z = x + y:  m = RN(mx + my),  r >= rx + ry + beta |m|,                       beta = u/(1-u)
  z = x * y:  m = RN(mx my),    r >= |mx| ry + |my| rx + rx ry + beta |m| + eta
Radius formulas are themselves evaluated with outward rounding: every + and * of nonnegative quantities in them is
followed by nextafter(., +inf) ("succ"), which bounds the exact result from above.
Dot products / matrix products of K terms: |RN-sum - exact| <= gamma_{2K} sum |a_i b_i|, gamma_j = j u / (1 - j u),
plus the propagated input radii (sum |a_i| r_bi + |b_i| r_ai + r_ai r_bi) and the underflow allowance K eta.
Elementary functions are NOT provided here (use Arb for them and import the results as mid/rad pairs).
"""
import numpy as np

U = 2.0 ** -53
ETA = 2.0 ** -1074
BETA = np.nextafter(U / (1 - U), np.inf)          # upper enclosure of u/(1-u)
INF = np.inf


def succ(x):
    return np.nextafter(x, INF)


class MR:
    """Arrays of midpoints and radii (same shape; radii >= 0)."""
    __slots__ = ("m", "r")

    def __init__(self, m, r=None):
        self.m = np.asarray(m, float)
        self.r = np.zeros_like(self.m) if r is None else np.broadcast_to(np.asarray(r, float), self.m.shape).copy()
        assert np.all(self.r >= 0)

    @staticmethod
    def exact(m):
        return MR(m, 0.0)

    @staticmethod
    def from_arb(balls):
        """From a list/array of python-flint arb balls: midpoint rounded to double, radius = ball radius + conversion error."""
        from flint import arb
        mids = np.array([float(b.mid()) for b in balls]); rads = np.array([float(b.rad()) for b in balls])
        # conversion of mid to double: |float(mid) - mid| <= u |float(mid)| + eta/2 ; rad float rounding: succ
        rads = succ(succ(succ(rads) + succ(U * np.abs(mids))) + ETA)
        return MR(mids, rads)

    def __getitem__(self, k):
        return MR(self.m[k], self.r[k])

    @property
    def shape(self):
        return self.m.shape

    def __neg__(self):
        return MR(-self.m, self.r)

    def __add__(self, other):
        if not isinstance(other, MR): other = MR.exact(other)
        m = self.m + other.m
        r = succ(succ(succ(self.r + other.r) + succ(BETA * np.abs(m))))
        return MR(m, r)

    __radd__ = __add__

    def __sub__(self, other):
        if not isinstance(other, MR): other = MR.exact(other)
        return self + (-other)

    def __rsub__(self, other):
        return (-self) + other

    def __mul__(self, other):
        if not isinstance(other, MR): other = MR.exact(other)
        m = self.m * other.m
        r = succ(succ(succ(succ(succ(np.abs(self.m) * other.r) + succ(np.abs(other.m) * self.r)) + succ(self.r * other.r))
                      + succ(BETA * np.abs(m))) + ETA)
        return MR(m, r)

    __rmul__ = __mul__

    def mag(self):
        """Upper bound of |x| over the ball."""
        return succ(np.abs(self.m) + self.r)

    def mig(self):
        """Lower bound of |x| over the ball (0 if the ball contains 0): |m| - r rounded downward."""
        return np.maximum(np.nextafter(np.abs(self.m) - self.r, -INF), 0.0)
    
    def lower(self):
        return np.nextafter(self.m - self.r, -INF)

    def upper(self):
        return succ(self.m + self.r)

    def sum(self, axis=None):
        """Rigorous sum along axis: |RN-sum - exact| <= gamma_{K-1} sum |m_i| (any order), plus radii, plus underflow allowance."""
        K = self.m.shape[axis] if axis is not None else self.m.size
        mm = self.m.sum(axis=axis)
        g = succ((K - 1) * U / (1 - (K - 1) * U)) if K > 1 else 0.0
        r = succ(succ(self.r.sum(axis=axis) * succ(1 + K * U)) + succ(g * succ(np.abs(self.m).sum(axis=axis) * succ(1 + K * U))) + K * ETA)
        return MR(mm, r)

    def contains(self, x):
        """True only if x is provably inside: |x - m| rounded upward <= r."""
        return np.all(succ(np.abs(np.asarray(x) - self.m)) <= self.r)


def mr_matmul(A, B):
    """Rigorous product of MR matrices A (p,K) @ B (K,q) with float64 BLAS matmul for the midpoints.
    Error of RN inner products of K terms <= gamma_{2K} sum_i |a_i b_i| (covers any summation order, incl. blocked/FMA;
    see Rump 2011 'Verified bounds for least squares problems and underdetermined linear systems' and Higham ch. 3), plus
    propagated radii |A| rB + rA |B| + rA rB (each computed with the same outward safety factor) and underflow K eta."""
    K = A.m.shape[-1]
    assert 2 * K * U < 0.5
    gam = succ(2 * K * U / (1 - 2 * K * U))
    m = A.m @ B.m
    absAB = np.abs(A.m) @ np.abs(B.m)
    prop = np.abs(A.m) @ B.r + A.r @ np.abs(B.m) + A.r @ B.r
    # the three auxiliary products are themselves RN computations of nonnegative sums: inflate by (1 + gam) each
    # underflow: each of the K products of the midpoint sum and of the three propagated-radius sums may lose up to eta/2
    r = succ(succ(succ(absAB * gam) + succ(prop * succ(1 + gam))) + 4 * (K + 1) * ETA)
    return MR(m, r)


def _test():
    from flint import arb, ctx
    ctx.prec = 200
    rng = np.random.default_rng(0)
    x = rng.normal(size=1000) * 10.0 ** rng.integers(-5, 5, 1000); y = rng.normal(size=1000) * 10.0 ** rng.integers(-5, 5, 1000)
    X = MR(x, np.abs(x) * 1e-12); Y = MR(y, np.abs(y) * 1e-13)
    Z = X * Y + X - Y
    # exact check with arb balls
    ok = True
    for i in range(0, 1000, 37):
        a = arb(x[i], abs(x[i]) * 1e-12); b = arb(y[i], abs(y[i]) * 1e-13)
        z = a * b + a - b
        lo, hi = float(z.lower()), float(z.upper())
        if not (Z.lower()[i] <= lo and Z.upper()[i] >= hi):
            ok = False; print("FAIL", i)
    print("MR ops vs arb enclosure (sampled): ok =", ok, "; typical radius inflation factor", np.median(Z.r / (np.abs(x * y) * 1.1e-12 + np.abs(x) * 1e-12 + np.abs(y) * 1e-13)))
    # matmul test: products with exactly representable integers -> exact result; check containment
    A = MR(rng.integers(-50, 50, (30, 400)).astype(float)); B = MR(rng.integers(-50, 50, (400, 20)).astype(float))
    C = mr_matmul(A, B); Cex = A.m.astype(np.int64) @ B.m.astype(np.int64)
    print("matmul exact-integer containment:", C.contains(Cex.astype(float)), " max radius", C.r.max())
    # sum test with cancellation
    v = MR(np.array([1e16, 1.0, -1e16]))
    print("sum [1e16, 1, -1e16]: mid %.3f rad %.3f (true 1)" % (v.sum().m, v.sum().r), v.sum().contains(1.0))


if __name__ == "__main__":
    _test()
