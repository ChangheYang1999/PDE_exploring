"""Tight rigorous range enclosures of exponential polynomials on a finite cell (s2-num, 04:10Z; resonance merging 04:35Z).

f(sigma) = sum_e e^{e sigma} p_e(sigma), sigma in [0, h].  Two defects of the coefficient-sum bound of tailbound.sup_bound:
 (a) it is loose by 1e2..1e5 on the spline cells, whose Green representation has large cancelling coefficients (logs/dbg_range.log);
 (b) near-resonant exponent pairs (|e_1 - e_2| = lambda tiny, e.g. the inner mode 27 with lambda = 1.07e-12, verifier V054) carry
     cancelling coefficients of size lambda^{-7}; every bound that treats the terms separately (coefficient sums, also the Taylor
     remainder below) is then useless, whatever the precision.

Method.
 1. Resonance merging (exact up to a rigorous remainder): exponents are clustered so that |e - e_0| h <= 1 within a cluster
    (e_0 the member closest to 0). Each member e^{e sigma} p(sigma) = e^{e_0 sigma} e^{lambda sigma} p(sigma), lambda = e - e_0, is
    replaced by e^{e_0 sigma} [sum_{j<=J} (lambda sigma)^j/j!] p(sigma) (J = 40, polynomial arithmetic in balls at >= 512 bits so
    that the lambda^{-7} cancellations leave radii ~ 2^{-512} lambda^{-7}); the dropped part is bounded by
    |R| <= e^{max(e_0,0) h} (sum_a |c_a| h^a) (|lambda| h)^{J+1}/(J+1)! e^{|lambda| h}   and added as a symmetric radius at the end.
 2. Taylor enclosure about the midpoint m = h/2 of order K = 8 with the rigorous remainder
       f(m + x) in sum_{k<=K} f^(k)(m) x^k/k! + R,  |R| <= sup_{[0,h]} |f^(K+1)| (h/2)^{K+1}/(K+1)!,
    sup by the coefficient-sum bound of the (K+1)-th derivative (now applied to the merged representation).
 3. When |e|_max h > SPLIT (= 6) the cell is split into sub-intervals (ExpPoly.shift of the merged polynomial), each enclosed as in 2;
    the union is returned. With SPLIT = 6 the Taylor remainder of a term c e^{e sigma} is at most 3^9/9! e^6 |c| = 22 |c|, i.e. 5% of
    the maximal size of that term on the sub-interval.
Returned: a ball whose [lower, upper] contains the exact range (ball arithmetic, outward floats via directed conversions).
"""
import math
from flint import arb, fmpq, ctx
from exact_trial import ExpPoly, q2arb
from tailbound import sup_bound
from outward import fup

MERGE_PREC = 512
J_MERGE = 40
SPLIT = 6.0
K_TAYLOR = 8


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


def merge_resonant(ep, h, J=J_MERGE):
    """(merged ExpPoly, remainder radius arb): clusters of exponents with |e - e_0| h <= 1 are merged into the base exponent e_0
    by the truncated expansion of e^{(e - e_0) sigma}; computed at >= MERGE_PREC bits."""
    if len(ep.terms) <= 1: return ep, arb(0)
    saved = ctx.prec; ctx.prec = max(saved, MERGE_PREC)
    try:
        exps = sorted(ep.terms.keys(), key=lambda e: float(q2arb(e)))
        hf = float(h.upper())
        clusters = []; cur = [exps[0]]
        for e in exps[1:]:
            if float(q2arb(e - cur[0])) * hf <= 1.0: cur.append(e)
            else: clusters.append(cur); cur = [e]
        clusters.append(cur)
        out = ExpPoly(); rem = arb(0)
        for cl in clusters:
            if len(cl) == 1:
                out.add(cl[0], ep.terms[cl[0]]); continue
            e0 = min(cl, key=lambda e: abs(float(q2arb(e))))
            e0a = q2arb(e0); emax0 = arb(1) if e0a <= 0 else (e0a * h).exp()
            for e in cl:
                cs = ep.terms[e]
                if e == e0:
                    out.add(e0, cs); continue
                lam = q2arb(e - e0)
                # (sum_{j<=J} lam^j sigma^j / j!) * p(sigma)
                poly = [arb(0)] * (len(cs) + J)
                lj = arb(1); fact = arb(1)
                for j in range(J + 1):
                    if j > 0: lj *= lam; fact *= j
                    coef = lj / fact
                    for a, c in enumerate(cs):
                        if c != 0: poly[a + j] += coef * c
                out.add(e0, poly)
                # remainder of the truncated exponential: |lam sigma|^{J+1}/(J+1)! e^{|lam sigma|} times |p|
                lh = abs(lam) * h
                rj = lh ** (J + 1) / arb.fac_ui(J + 1) * lh.exp()
                ps = arb(0)
                for a, c in enumerate(cs):
                    if c != 0: ps += abs(c) * h ** a
                rem += emax0 * ps * rj
        return out, rem
    finally:
        ctx.prec = saved


def taylor_range(ep, h, K=K_TAYLOR):
    """ball enclosing the range of ep on [0, h] (h arb) by a Taylor expansion of order K about h/2 with rigorous remainder"""
    if not ep.terms: return arb(0)
    m = h / 2; r = h / 2
    d = ep; val = d(m); rad = arb(0); fact = arb(1); rp = arb(1)
    for k in range(1, K + 1):
        d = d.deriv(); fact *= k; rp *= r
        rad += abs(d(m)) * rp / fact
    d = d.deriv(); fact *= (K + 1); rp *= r
    rem = _sup_coeff(d, h) * rp / fact
    return val + arb(0, fup(rad + rem))


def max_abs_exponent(ep):
    return max((abs(float(q2arb(e))) for e in ep.terms), default=0.0)


def range_finite(ep, cl, K=K_TAYLOR, split=SPLIT):
    """ball enclosing the range of ep on the finite cell cl (keys h (arb), hq (fmpq)); resonance merging, sub-intervals when |e|_max h > split"""
    if not ep.terms: return arb(0)
    h = cl["h"]
    epm, rem = merge_resonant(ep, h)
    emax = max_abs_exponent(epm)
    hf = float(h.upper())
    nsub = max(1, int(math.ceil(emax * hf / split)))
    if nsub == 1:
        b = taylor_range(epm, h, K)
    else:
        hq = cl["hq"]; lo = None; hi = None
        for i in range(nsub):
            s_q = hq * i / nsub; w_q = hq / nsub
            sub = epm.shift(q2arb(s_q)); w = q2arb(w_q)
            bb = taylor_range(sub, w, K)
            l = bb.lower(); u = bb.upper()
            lo = l if (lo is None or l < lo) else lo; hi = u if (hi is None or u > hi) else hi
        b = (arb(lo) + arb(hi)) / 2 + arb(0, fup((arb(hi) - arb(lo)) / 2))
    if rem != 0: b = b + arb(0, fup(rem))
    return b


def range_on_cell(ep, cl, K=K_TAYLOR, split=SPLIT):
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
        return const + arb(0, fup(s0))
    return range_finite(ep, cl, K, split)
