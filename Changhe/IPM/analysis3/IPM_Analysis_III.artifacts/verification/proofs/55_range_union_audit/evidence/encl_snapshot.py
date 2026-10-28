"""Tight rigorous range enclosures of exponential polynomials on a finite cell (s2-num, 04:10Z).

f(sigma) = sum_e e^{e sigma} p_e(sigma), sigma in [0, h].  The coefficient-sum bound of tailbound.sup_bound is rigorous but loose when
the representation has large cancelling coefficients (the Green data of the trial on spline cells), see logs/dbg_range.log.

Method (Taylor enclosure about the midpoint, rigorous remainder):
  f(m + x) = sum_{k<=K} f^(k)(m) x^k/k! + R,  |R| <= sup_{[0,h]} |f^(K+1)| (h/2)^{K+1}/(K+1)!,
with f^(k)(m) balls from the exact derivative ExpPolys, and the remainder sup by the coefficient-sum bound of the (K+1)-th derivative.
The range over |x| <= h/2 is enclosed by f(m) + sum_{k=1..K} |f^(k)(m)| (h/2)^k/k! [-1,1] + |R| [-1,1].
When e_max h is large (half-line-like sub-cells, |e| up to 2*260), the cell is split into sub-intervals of width <= SPLIT/|e|_max so
that the Taylor remainder converges; each sub-interval is shifted (ExpPoly.shift) and enclosed; the union is returned.
Returned: a ball whose [lower, upper] contains the exact range (ball arithmetic, outward).
"""
import math
from flint import arb, fmpq, ctx
from exact_trial import ExpPoly, q2arb
from tailbound import sup_bound


def _sup_coeff(ep, h):
    """coefficient-sum upper bound of sup_{[0,h]} |ep| (finite interval), same rule as tailbound.sup_bound"""
    tot = arb(0)
    for e, cs in ep.terms.items():
        ea = q2arb(e); emax = arb(1) if ea <= 0 else (ea * h).exp()
        s = arb(0)
        for a, c in enumerate(cs):
            if c != 0: s += abs(c) * h ** a
        tot += emax * s
    return tot


def taylor_range(ep, h, K=8):
    """ball enclosing the range of ep on [0, h] (h arb) by a Taylor expansion of order K about h/2 with rigorous remainder"""
    if not ep.terms: return arb(0)
    m = h / 2; r = h / 2
    d = ep; val = d(m); rad = arb(0); fact = arb(1); rp = arb(1)
    for k in range(1, K + 1):
        d = d.deriv(); fact *= k; rp *= r
        rad += abs(d(m)) * rp / fact
    d = d.deriv(); fact *= (K + 1); rp *= r
    rem = _sup_coeff(d, h) * rp / fact
    tot = rad + rem
    return val + arb(0, float(tot.upper()) * (1 + 1e-15) + 1e-300)


def max_abs_exponent(ep):
    return max((abs(float(q2arb(e))) for e in ep.terms), default=0.0)


def range_finite(ep, cl, K=8, split=6.0):
    """ball enclosing the range of ep on the finite cell cl (keys h (arb), hq (fmpq)); sub-intervals when |e|_max h > split"""
    if not ep.terms: return arb(0)
    h = cl["h"]; emax = max_abs_exponent(ep)
    hf = float(h.upper())
    nsub = max(1, int(math.ceil(emax * hf / split)))
    if nsub == 1: return taylor_range(ep, h, K)
    hq = cl["hq"]; lo = None; hi = None
    for i in range(nsub):
        s_q = hq * i / nsub; w_q = hq / nsub
        sub = ep.shift(q2arb(s_q)); w = q2arb(w_q)
        b = taylor_range(sub, w, K)
        l = float(b.lower()); u = float(b.upper())
        lo = l if lo is None else min(lo, l); hi = u if hi is None else max(hi, u)
    mid = (lo + hi) / 2
    return arb(mid) + arb(0, (hi - lo) / 2 * (1 + 1e-15) + 1e-300)


def range_on_cell(ep, cl, K=8, split=6.0):
    """general: half-lines keep the exact constant and bound the rest by sup_bound; finite cells use range_finite"""
    if not ep.terms: return arb(0)
    if cl["kind"] in ("minf", "pinf"):
        const = arb(0); rest = ExpPoly()
        for e, cs in ep.terms.items():
            if e == 0:
                assert all(x == 0 for x in cs[1:]), "polynomial constant term on a half-line"
                const += cs[0]
            else: rest.add(e, cs)
        s0 = sup_bound(rest, cl)[0] if rest.terms else arb(0)
        return const + arb(0, float(s0.upper()) * (1 + 1e-15) + 1e-300)
    return range_finite(ep, cl, K, split)
