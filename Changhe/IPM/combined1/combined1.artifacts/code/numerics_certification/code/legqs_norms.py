"""Exact whole-plane residual norms and weak pairings for candidates with multi-scale (legqs) functions (lane c1-n3, N3).
Extends e2norms (Beta-integral method) to generators carrying (R0^2 + r^2)^(-N) factors. Plan: notes/LEGQS_EXTENSION_PLAN.md.

Representation (tuple keys): a degree-d compactified component is a dict (ell, kind, n, scales) -> fmpq_poly in t, where the term is
   even d:  r (1-t)^(d/2)      w^ell P(t) T_(kind,n)(theta) prod_(a,N) in scales (1 + a v)^(-N)
   odd d:   (1-t)^((d-1)/2)    w^ell P(t) T_(kind,n)(theta) prod_(a,N) in scales (1 + a v)^(-N)
with v = 1 - t = 1/(1+r^2), a = R0^2 - 1 (K convention of legqs_e2norms: the v^N of (R0^2+r^2)^(-N) = v^N (1+a v)^(-N) is already
inside the standard (1-t) exponent). Canonical form (canon_t): one key per (ell, kind, n), all scale powers raised to their maximum by
multiplying with (1 + a (1-t))^(Nmax - N); exact, and harmless because the integration below is exact.

Radial integrals: int_0^1 P(t) (1-t)^b prod_R (1 + a_R (1-t))^(-M_R) dt = int_0^1 P(1-v) v^b prod_R (1 + a_R v)^(-M_R) dv.
Partial fractions in v (exact) reduce the product to single factors (1 + a v)^(-i). With b = b0 + m (b0 in (-1, 0], m >= 0 integer) the
contiguous recurrences
   (1) J(b+1, 1) = (1/a) (1/(b+1) - J(b, 1)),
   (2) J(b+1, i+1) = ((b+1) J(b, i) - (1+a)^(-i)) / (i a)        (integration by parts; b > -1),
   (3) J(b, i) = J(b, i-1) - a J(b+1, i),
express every J(b0 + m, i) = int_0^1 v^(b0+m) (1+a v)^(-i) dv as R1 + R2 I0 with exact rationals R1, R2 and the single transcendental
I0(a, b0) = int_0^1 v^b0 / (1 + a v) dv = (1+a)^(-1) 2F1(1, 1; b0+2; a/(1+a)) / (b0+1) (Pfaff form; arb ball at 1024 bits, checked
against the direct 2F1 and the Beta x 2F1 form of legqs_integrals.J). The cancellation between the rational parts (coefficients up to 1e40 times (1+a)^Nmax against results of order 1e-10) therefore
happens in exact rational arithmetic; the balls enter only through the products R2 * I0 (one per scale and exponent class), whose
radii |R2| rad(I0) are reported (S_ball_radius) and must be checked against the result. All exponents are rational (c is rational).
With no scales present every integral is the exact Beta rational of e2norms (validation: identical S sums on state 131 and on R0 = 1 legqs tests).
"""
from fractions import Fraction as Q
from math import comb, floor
from pathlib import Path
from datetime import datetime, timezone
import json, sys, time, hashlib, argparse
from flint import fmpq, fmpq_poly, fmpz, arb, ctx
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import e2norms as E
import legqs_e2norms as LS
from legqs_integrals import partial_fractions, J as J2F1
from e2norms import fq, Z, OM, ONE, endpoint

def fq2arb(x):
    x = fq(x) if not isinstance(x, fmpq) else x
    return arb(x.p) / arb(x.q)

# ---------------------------------------------------------------- tuple-key field algebra
def add_t(D, key, p):
    ell, kind, n, sc = key
    if n < 0:
        n = -n
        if kind == 's': p = -p
    if not p or (kind == 's' and n == 0): return
    key = (ell, kind, n, sc)
    D[key] = D.get(key, fmpq_poly([])) + p
    if not D[key]: del D[key]

def plus_t(*terms):
    out = {}
    for scale, D in terms:
        for key, p in D.items(): add_t(out, key, p * fq(scale))
    return out

def to_tuple(D):
    """Single-scale keys (ell, kind, n, N, a) -> tuple keys; a = 0 (R0 = 1) or N = 0 carry no factor and are dropped from the tuple."""
    out = {}
    for (ell, kind, n, N, a), p in D.items():
        sc = ((Q(a), N),) if (N and Q(a) != 0) else ()
        add_t(out, (ell, kind, n, sc), p)
    return out

def from_plain(D):
    """e2norms keys (ell, kind, n) -> tuple keys with no scales."""
    return {(ell, kind, n, ()): p for (ell, kind, n), p in D.items()}

def to_plain(D):
    """Tuple keys with no scales -> e2norms keys (asserts that no scale factor is present)."""
    out = {}
    for (ell, kind, n, sc), p in D.items():
        assert not sc, ('scale factor present', ell, kind, n, sc)
        out[(ell, kind, n)] = p
    return out

def merge_scales(s1, s2):
    d = {}
    for a, N in tuple(s1) + tuple(s2): d[a] = d.get(a, 0) + N
    return tuple(sorted((a, N) for a, N in d.items() if N))

mul_t = LS.mul_s

def canon_t(D):
    """One key per (ell, kind, n): every scale power raised to its maximum over the group by (1 + a (1-t))^(Nmax - N). Exact."""
    groups = {}
    for (ell, kind, n, sc), p in D.items(): groups.setdefault((ell, kind, n), []).append((dict(sc), p))
    out = {}
    for (ell, kind, n), rows in groups.items():
        Nmax = {}
        for sc, p in rows:
            for a, N in sc.items(): Nmax[a] = max(Nmax.get(a, 0), N)
        tot = fmpq_poly([])
        for sc, p in rows:
            f = p
            for a, M in Nmax.items():
                e = M - sc.get(a, 0)
                if e: f = f * (ONE + fq(a) * OM) ** e
            tot += f
        if tot: out[(ell, kind, n, tuple(sorted(Nmax.items())))] = tot
    return out

def equal_t(D1, D2):
    """Equality of two fields as functions (joint canonical form)."""
    C1 = canon_t(D1); C2 = canon_t(D2)
    g1 = {(ell, kind, n): (dict(sc), p) for (ell, kind, n, sc), p in C1.items()}
    g2 = {(ell, kind, n): (dict(sc), p) for (ell, kind, n, sc), p in C2.items()}
    if set(g1) != set(g2): return False
    for key in g1:
        s1, p1 = g1[key]; s2, p2 = g2[key]
        for a in set(s1) | set(s2):
            e1 = max(s1.get(a, 0), s2.get(a, 0)) - s1.get(a, 0); e2 = max(s1.get(a, 0), s2.get(a, 0)) - s2.get(a, 0)
            if e1: p1 = p1 * (ONE + fq(a) * OM) ** e1
            if e2: p2 = p2 * (ONE + fq(a) * OM) ** e2
        if p1 != p2: return False
    return True

def diff_t(D, d, axis, delta):
    """One Cartesian derivative of a degree-d component with tuple keys (rules of e2norms.diff plus, per scale (a, N) in the key,
    the piece 2 N a t (1-t) P (even d) or 2 N a (1-t) P (odd d) times cos(theta) (x) or sin(theta) (y) with N -> N+1 for that scale)."""
    out = {}
    for (ell, kind, n, sc), p in D.items():
        if d % 2 == 0:
            rad = (ONE - Z * fq(d + ell * delta)) * p + 2 * Z * OM * p.derivative(); ang = p
            radK = [(a, 2 * fq(N * a) * Z * OM * p) for a, N in sc]
        else:
            rad = -fq(d - 1 + ell * delta) * p + 2 * OM * p.derivative()
            if n:
                ang, rem = divmod(p, Z); assert not rem, ('origin pole', d, ell, kind, n)
            else: ang = fmpq_poly([])
            radK = [(a, 2 * fq(N * a) * OM * p) for a, N in sc]
        rk = 'c' if axis == 'x' else 's'
        for kk, nn, factor in E.trigprod(rk, 1, kind, n):
            add_t(out, (ell, kk, nn, sc), rad * fq(factor))
            for a, pk in radK:
                sc2 = tuple(sorted((aa, NN + 1 if aa == a else NN) for aa, NN in sc))
                add_t(out, (ell, kk, nn, sc2), pk * fq(factor))
        if n:
            ak = 's' if axis == 'x' else 'c'; dk = 's' if kind == 'c' else 'c'
            sign = (-1 if kind == 'c' else 1) * (-1 if axis == 'x' else 1)
            for kk, nn, factor in E.trigprod(ak, 1, dk, n): add_t(out, (ell, kk, nn, sc), ang * fq(sign * n * factor))
    return out

# ---------------------------------------------------------------- residual assembly
def fields_t(A, A_s, c, log=print):
    t0 = time.monotonic(); j3 = {}; j4 = {}
    for d, save in [(3, j3), (4, j4)]:
        for nx in range(d): save[nx] = canon_t(to_tuple(LS.chi_compact_s(A, A_s, c, d, nx)))
    rho = canon_t(plus_t((-1, j3[0]), (-1, j3[2]))); u1 = canon_t(plus_t((-1, j3[1]))); u2 = j3[2]
    rx = canon_t(plus_t((-1, j4[1]), (-1, j4[3]))); ry = canon_t(plus_t((-1, j4[0]), (-1, j4[2])))
    log(f'fields from chi derivatives ({time.monotonic()-t0:.0f}s): rho {len(rho)} u1 {len(u1)} u2 {len(u2)} rho_x {len(rx)} rho_y {len(ry)} keys')
    return {'rho': rho, 'u1': u1, 'u2': u2, 'rho_x': rx, 'rho_y': ry}

CX = {(0, 'c', 1, ()): ONE}; SY = {(0, 's', 1, ()): ONE}

def residual_t(A, A_s, c, max_order=2, log=print, check_mixed=True):
    """D[(d, nx)] = canonical tuple-key components of d_x^nx d_y^(d-nx) F, F = (c X + U).grad rho - rho, for d <= max_order."""
    delta = 1 - 1 / c; start = time.monotonic()
    fields = fields_t(A, A_s, c, log)
    rho, u1, u2, rx, ry = (fields[k] for k in ('rho', 'u1', 'u2', 'rho_x', 'rho_y'))
    F = canon_t(plus_t((c, mul_t(CX, rx)), (c, mul_t(SY, ry)), (-1, rho), (1, mul_t(u1, rx)), (1, mul_t(u2, ry))))
    log(f'F assembled {time.monotonic()-start:.1f}s, components {len(F)}, max degree {max(p.degree() for p in F.values())}, '
        f'scales {sorted({sc for (ell, kind, n, sc) in F})[-1] if F else None}')
    D = {(0, 0): F}
    for d in range(max_order):
        for nx in range(d + 2):
            D[d + 1, nx] = canon_t(diff_t(D[d, 0], d, 'y', delta) if nx == 0 else diff_t(D[d, nx - 1], d, 'x', delta))
        if check_mixed:
            for nx in range(1, d + 1):
                assert equal_t(D[d + 1, nx], diff_t(D[d, nx], d, 'y', delta)), ('mixed derivative mismatch', d, nx)
        log(f'derivative order {d+1} done {time.monotonic()-start:.1f}s')
    return D, fields

# ---------------------------------------------------------------- exact integration: J tables and accumulators
class ScaleTables:
    """J(b0 + m, i; a) = int_0^1 v^(b0+m) (1+a v)^(-i) dv = R1 + R2 I0(a, b0) as exact rational pairs, memoized on demand along the
    recurrence diagonals (J(m, i) <- J(m-1, i-1)), so that a probe with t^K, K ~ 2400, only costs the entries it needs."""
    def __init__(self): self.J = {}; self.i0 = {}; self.pf_cache = {}; self.beta_cache = {}
    def entry(self, a, b0, m, i):
        key = (Q(a), Q(b0)); tab = self.J.setdefault(key, {})
        if (m, i) in tab: return tab[(m, i)]
        A = fq(a); b0q = fq(b0)
        if i == 0:
            val = (1 / (b0q + m + 1), fmpq(0)); tab[(m, i)] = val; return val
        if i == 1:
            if (0, 1) not in tab: tab[(0, 1)] = (fmpq(0), fmpq(1))
            mm = m
            while (mm, 1) not in tab: mm -= 1
            for k in range(mm + 1, m + 1):                       # (1) J(b+1, 1) = (1/a) (1/(b+1) - J(b, 1)), b = b0 + k - 1
                R1, R2 = tab[(k - 1, 1)]; bb = b0q + k - 1
                tab[(k, 1)] = ((1 / (bb + 1) - R1) / A, -R2 / A)
            return tab[(m, 1)]
        if m == 0:                                                # (3) J(b0, i) = J(b0, i-1) - a J(b0+1, i)
            P1, P2 = self.entry(a, b0, 0, i - 1); S1, S2 = self.entry(a, b0, 1, i)
            val = (P1 - A * S1, P2 - A * S2); tab[(0, i)] = val; return val
        path = []; mm, ii = m, i                                  # (2) along the diagonal: J(b+1, i) = ((b+1) J(b, i-1) - (1+a)^(1-i)) / ((i-1) a)
        while ii >= 2 and mm >= 1 and (mm, ii) not in tab: path.append((mm, ii)); mm -= 1; ii -= 1
        base = self.entry(a, b0, mm, ii)
        inv1a = 1 / (1 + A)
        for (m2, i2) in reversed(path):
            R1, R2 = base; bb = b0q + m2 - 1; den = (i2 - 1) * A
            base = (((bb + 1) * R1 - inv1a ** (i2 - 1)) / den, (bb + 1) * R2 / den); tab[(m2, i2)] = base
        return base
    def pack(self, a, b0, m0, deg, i):
        """(den, [R1 numerators], [R2 numerators]) for J(b0 + m0 + n, i), n = 0..deg, over one common denominator (fmpz)."""
        ents = [self.entry(a, b0, m0 + n, i) for n in range(deg + 1)]
        den = fmpz(1)
        for R1, R2 in ents: den = _lcm(_lcm(den, R1.q), R2.q)
        return den, [R1.p * (den // R1.q) for R1, R2 in ents], [R2.p * (den // R2.q) for R1, R2 in ents]
    def beta_column(self, b, nmax):
        """(den, [numerators]) for int_0^1 v^(b+n) dv = 1/(b+n+1), n <= nmax, over one common denominator."""
        key = (Q(b)); z = self.beta_cache.get(key)
        if z is None or len(z[1]) <= nmax:
            bq = Q(b); pb, qb = fmpz(bq.numerator), fmpz(bq.denominator)
            facs = [pb + (n + 1) * qb for n in range(nmax + 1)]
            den = fmpz(1)
            for f in facs: den = _lcm(den, f)
            z = (den, [qb * (den // f) for f in facs]); self.beta_cache[key] = z
        return z
    def pf(self, Ms):
        key = tuple(Ms)
        if key not in self.pf_cache: self.pf_cache[key] = partial_fractions([M for a, M in Ms], [a for a, M in Ms])
        return self.pf_cache[key]
    def I0(self, a, b0, prec=1024):
        key = (Q(a), Q(b0), prec)
        if key not in self.i0:
            old = ctx.prec; ctx.prec = prec
            A = fq2arb(fq(a)); b1 = fq2arb(fq(b0)) + 1; z = A / (1 + A)
            v1 = z.hypgeom_2f1(arb(1), arb(1), b1 + 1) / ((1 + A) * b1)           # Pfaff form
            v2 = (-A).hypgeom_2f1(arb(1), b1, b1 + 1) / b1                          # direct 2F1 at z = -a
            assert v1.is_finite() and v2.is_finite() and v1.overlaps(v2), ('I0 forms disagree or not finite', v1, v2)
            self.i0[key] = v1
            ctx.prec = old
        return self.i0[key]

def _lcm(x, y):
    x = fmpz(x); y = fmpz(y); return x * y // x.gcd(y)

class Accumulator:
    """Sum of integrals int_0^1 P(t) (1-t)^b prod_R (1 + a_R (1-t))^(-M_R) dt kept as (exact rational) + sum_classes (R1 + R2 I0).
    Integer dot products over common denominators (the rational version was 500 times slower on 10^4-digit coefficients)."""
    BALL_DEGREE = 400          # groups of higher degree (probe polynomials t^K ...) take the t-monomial ball route
    BALL_PREC = 1536
    def __init__(self, tables):
        self.tables = tables; self.rational = fmpq(0); self.cls = {}; self.n_terms = 0; self.ball = arb(0); self.n_ball = 0
    def add_ball(self, P_t, b, Ms):
        """High-degree groups: int_0^1 t^n (1-t)^b prod_R (1 + a_R (1-t))^(-M_R) dt = sum_pf c_pf J(b, n, a_r, i) with
        J(b, n, a, i) = int_0^1 v^b (1-v)^n (1+a v)^(-i) dv = B(b+1, n+1) 2F1(i, b+1; b+n+2; -a) (legqs_integrals.J, arb balls at BALL_PREC
        bits; no composition, so only the intrinsic cancellation of the coefficients appears; the radius is reported)."""
        old = ctx.prec; ctx.prec = self.BALL_PREC
        coeffs = P_t.coeffs(); pf = self.tables.pf(Ms) if any(M for a, M in Ms) else {(-1, 0): Q(1)}
        tot = arb(0)
        for (r, i), cpf in pf.items():
            a = Ms[r][0] if r >= 0 else Q(0); s = arb(0)
            for n, cn in enumerate(coeffs):
                if cn: s += fq2arb(cn) * J2F1(b, n, a, i, self.BALL_PREC)
            tot += fq2arb(fq(cpf)) * s
        assert tot.is_finite()
        self.ball += tot; self.n_ball += 1
        ctx.prec = old
    def add(self, P_t, b, Ms):
        b = Q(b); assert b > -1, b
        if P_t.degree() > self.BALL_DEGREE: return self.add_ball(P_t, b, Ms)
        Pv = P_t(ONE - Z); self.n_terms += 1
        if not Pv: return
        Nv = Pv.numer().coeffs(); denP = Pv.denom(); deg = len(Nv) - 1
        if not any(M for a, M in Ms):
            den, nums = self.tables.beta_column(b, deg)
            s = fmpz(0)
            for cn, bn in zip(Nv, nums): s += cn * bn
            self.rational += fmpq(s, denP * den); return
        frac = b - floor(b); b0 = frac - 1 if frac > 0 else Q(0); m0 = int(b - b0); assert m0 >= 0 and b0 > -1
        for (r, i), cpf in self.tables.pf(Ms).items():
            a = Ms[r][0]; den, n1, n2 = self.tables.pack(a, b0, m0, deg, i)
            s1 = fmpz(0); s2 = fmpz(0)
            for n, cn in enumerate(Nv):
                if cn: s1 += cn * n1[n]; s2 += cn * n2[n]
            acc = self.cls.setdefault((Q(a), b0), [fmpq(0), fmpq(0)]); D = denP * den
            acc[0] += fq(cpf) * fmpq(s1, D); acc[1] += fq(cpf) * fmpq(s2, D)
    def value(self, prec=1024):
        """Ball enclosure: all rational parts (the scale-free integrals and every R1) are summed exactly first; the only ball
        operations are the products R2 * I0 (one per scale and exponent class) and their sum."""
        old = ctx.prec; ctx.prec = prec
        exact = self.rational
        for (a, b0), (R1, R2) in self.cls.items(): exact += R1
        total = fq2arb(exact)
        for (a, b0), (R1, R2) in self.cls.items(): total += fq2arb(R2) * self.tables.I0(a, b0, prec)
        if self.n_ball: total += self.ball
        assert total.is_finite(), 'non-finite enclosure'
        ctx.prec = old
        return total
    def is_rational(self): return not self.cls and not self.n_ball

def normsq_t(comps, d, delta, a_shift=Q(0), t_power=0, series=(), N=56, tables=None, prec=1024):
    """Squared weighted L^2 norm sum_(mult, D) mult ||W D||_2^2 of degree-d tuple-key components (canonical), W^2 = (1-t)^a_shift t^t_power
    prod (1+c t)^alpha (series: rigorous binomial enclosure as in e2norms). Returns dict(lo, hi: arb balls containing the bounds; the true
    value lies in [lo.lower(), hi.upper()]), or dict(status INFINITE, bad_sectors) if an exact nonzero endpoint sector diverges."""
    tables = tables or ScaleTables(); a_shift = Q(a_shift); groups = {}; bad = []; facts = []
    for mult, comp in comps:
        modes = {}
        for (ell, kind, n, sc), p in comp.items():
            q, p2 = endpoint(p)
            modes.setdefault((kind, n), []).append((ell, q, p2, sc))
            b = Q(d - 3) + ell * delta + 2 * q + a_shift
            facts.append({'ell': ell, 'kind': kind, 'mode': n, 'order': q, 'scales': [[str(a), M] for a, M in sc], 'diagonal_exponent': str(b)})
            if b <= -1: bad.append(facts[-1])
        ells = {ell for rows in modes.values() for ell, q, p, sc in rows}
        for l in ells:
            for m in ells:
                if l != m: assert ((l - m) * delta / 2).denominator != 1, 'resonant branches'
        if bad: continue
        for (kind, n), rows in modes.items():
            for i, (ell, q, p, sc) in enumerate(rows):
                for j in range(i, len(rows)):
                    ell2, q2, p2, sc2 = rows[j]
                    b = Q(d - 3) + (ell + ell2) * delta / 2 + q + q2 + a_shift
                    factor = Q(mult) * (2 if n == 0 and kind == 'c' else 1) * (1 if i == j else 2) * Q(1, 2)
                    v = p * p2 * fq(factor)
                    if d % 2 == 0: v *= Z
                    if t_power: v *= Z ** t_power
                    key = (b, merge_scales(sc, sc2)); groups[key] = groups.get(key, fmpq_poly([])) + v
    if bad: return {'status': 'INFINITE', 'bad_sectors': bad[:20], 'n_bad': len(bad)}
    S = Accumulator(tables); T = Accumulator(tables)
    wp = ONE; eps_total = fmpq(0); pref = arb(1); sdesc = []
    old = ctx.prec; ctx.prec = prec
    for cc, alpha in series:
        mid, al, p, eps = E.series_factor(cc, alpha, N)
        wp = wp * p; eps_total = eps_total + eps
        pref *= fq2arb(fq(mid)) ** fq2arb(fq(al)); sdesc.append({'c': str(cc), 'alpha': str(alpha), 'N': N, 'eps': str(eps)})
    assert len(series) <= 1
    for (b, Ms), p in sorted(groups.items()):
        S.add(p, b, Ms)
        if series: T.add(p * wp, b, Ms)
    Sv = S.value(prec); Tv = T.value(prec) if series else Sv
    lo = Tv - fq2arb(eps_total) * Sv; hi = Tv + fq2arb(eps_total) * Sv
    assert lo.is_finite() and hi.is_finite(), 'non-finite enclosure'
    res = {'status': 'FINITE', 'lo': arb.pi() * pref * lo, 'hi': arb.pi() * pref * hi, 'n_groups': len(groups), 'series': sdesc,
           'S_exact_rational': str(S.rational) if S.is_rational() else None, 'S_ball': Sv.str(40), 'T_ball': Tv.str(40),
           'S_ball_radius': Sv.rad().str(5), 'T_ball_radius': Tv.rad().str(5), 'n_classes': len(S.cls), 'n_ball_groups': S.n_ball}
    ctx.prec = old
    return res

def norm_t(D, d, delta, a_shift=Q(0), t_power=0, series=(), N=56, label='', tables=None, prec=1024):
    """Enclosure of || W D^d F ||_2 (sum over the comb(d, nx) components), record format of e2norms.norm."""
    start = time.monotonic()
    r = normsq_t([(comb(d, nx), D[d, nx]) for nx in range(d + 1)], d, delta, a_shift, t_power, series, N, tables, prec)
    if r['status'] != 'FINITE':
        return {'label': label, 'status': 'INFINITE', 'bad_sectors': r['bad_sectors'], 'n_bad': r['n_bad'],
                'scope': 'exact nonzero endpoint sector (canonical form over all scales) with square exponent <= -1 (nonresonant branches)'}
    old = ctx.prec; ctx.prec = prec
    lo = r['lo']; hi = r['hi']
    lo_b = max(lo.lower(), arb(0)); nl = arb(lo_b).sqrt(); nh = arb(hi.upper()).sqrt()
    out = {'label': label, 'status': 'FINITE', 'norm_lower': str(nl.lower()), 'norm_upper': str(nh.upper()),
           'norm_lower_ball': nl.str(40), 'norm_upper_ball': nh.str(40), 'square_lo_ball': lo.str(40), 'square_hi_ball': hi.str(40),
           'S_exact_rational': r['S_exact_rational'], 'S_ball': r['S_ball'], 'T_ball': r['T_ball'], 'S_ball_radius': r['S_ball_radius'],
           'T_ball_radius': r['T_ball_radius'], 'n_classes': r['n_classes'], 'series': r['series'],
           'a_shift': str(Q(a_shift)), 't_power': t_power, 'n_groups': r['n_groups'], 'precision_bits': prec,
           'method': 'exact rational reduction to R1 + R2 I0 per (scale, exponent class); I0 ball', 'elapsed_seconds': time.monotonic() - start}
    ctx.prec = old
    return out

def pair_t(F, G, delta, tables=None, prec=1024):
    """int F G dX for two degree-0 tuple-key fields (canonical): arb ball, or None if a diagonal exponent is <= -1."""
    tables = tables or ScaleTables(); idx = {}
    for (ell, kind, n, sc), p in G.items(): idx.setdefault((kind, n), []).append((ell, sc, p))
    groups = {}
    for (ell, kind, n, sc), p in F.items():
        q1, p1 = endpoint(p)
        for ell2, sc2, p2raw in idx.get((kind, n), []):
            q2, p2 = endpoint(p2raw)
            b = Q(-3) + (ell + ell2) * delta / 2 + q1 + q2
            if b <= -1: return None
            factor = Q(1, 2) * (2 if (kind == 'c' and n == 0) else 1)
            key = (b, merge_scales(sc, sc2)); groups[key] = groups.get(key, fmpq_poly([])) + p1 * p2 * Z * fq(factor)
    acc = Accumulator(tables)
    for (b, Ms), v in sorted(groups.items()): acc.add(v, b, Ms)
    old = ctx.prec; ctx.prec = prec; val = arb.pi() * acc.value(prec); ctx.prec = old
    assert val.is_finite()
    return val

# ---------------------------------------------------------------- records
def save_F(F, path, meta):
    rows = [{'ell': ell, 'kind': kind, 'mode': n, 'scales': [[str(a), N] for a, N in sc], 'coeff': [str(v) for v in p.coeffs()]}
            for (ell, kind, n, sc), p in sorted(F.items(), key=lambda kv: (kv[0][0], kv[0][1], kv[0][2]))]
    Path(path).write_text(json.dumps(dict(meta, polynomials={'0,0': rows}), separators=(',', ':')) + '\n')

def load_F(path):
    raw = json.loads(Path(path).read_text())
    F = {(r['ell'], r['kind'], r['mode'], tuple((Q(a), N) for a, N in r.get('scales', []))): fmpq_poly([fmpq(v) for v in r['coeff']]) for r in raw['polynomials']['0,0']}
    return F, raw

STANDARD = [('G0', 0, Q(0), 0, ()), ('rF', 0, Q(-1), 1, ()), ('G1', 1, Q(0), 0, ()), ('P2', 2, Q(-4, 5), 0, E.OMEGA),
            ('Pw1', 1, Q(1, 5), 0, ()), ('D2', 2, Q(0), 0, ()), ('rD2', 2, Q(-1), 1, ())]

def run(path, name, outdir, norms=('G0', 'rF', 'G1', 'P2'), max_order=2, prec=1024, N=56):
    outdir = Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
    logf = open(outdir / f'{name}_legqs.log', 'a')
    def log(*a):
        msg = ' '.join(str(x) for x in a); print(msg, flush=True); logf.write(msg + '\n'); logf.flush()
    t0 = time.monotonic()
    c, A, A_s, src_sha, meta = LS.load_reference_legqs(path); delta = 1 - 1 / c
    log(f'[{datetime.now(timezone.utc).isoformat(timespec="seconds")}] {name}: {meta} source_sha256={src_sha}')
    rec = {'utc_start': datetime.now(timezone.utc).isoformat(timespec='seconds'), 'name': name, 'source_path': str(path), 'source_sha256': src_sha,
           'reference_meta': meta, 'cl': str(c), 'delta': str(delta), 'precision_bits': prec, 'series_degree': N,
           'code_sha256': {f: hashlib.sha256((Path(__file__).parent / f).read_bytes()).hexdigest() for f in ('legqs_norms.py', 'legqs_e2norms.py', 'legqs_integrals.py', 'e2norms.py')},
           'norms': {}, 'status': 'RUNNING'}
    dest = outdir / f'{name}_legqs_norms.json'
    def save():
        rec['utc_updated'] = datetime.now(timezone.utc).isoformat(timespec='seconds'); rec['elapsed_seconds'] = time.monotonic() - t0
        dest.write_text(json.dumps(rec, indent=1) + '\n')
    save()
    D, fields = residual_t(A, A_s, c, max_order, log)
    Fpath = outdir / f'{name}_legqs_Fpoly.json'
    save_F(D[0, 0], Fpath, {'name': name, 'source_sha256': src_sha, 'delta': str(delta), 'cl': str(c), 'format': 'tuple keys; K convention'})
    log(f'F record saved {Fpath} ({Fpath.stat().st_size/1e6:.1f} MB)')
    tables = ScaleTables()
    for label, d, a, tp, ser in STANDARD:
        if label not in norms or (d, 0) not in D: continue
        r = norm_t(D, d, delta, a, tp, ser, N, label, tables, prec); rec['norms'][label] = r; save()
        log(f"{label}: {r['status']} {r.get('norm_lower_ball','')} {r.get('norm_upper_ball','')} ({r.get('elapsed_seconds',0):.1f}s)")
    rec['assembly'] = E.e2_assembly(rec['norms']); rec['status'] = 'COMPLETE'; save()
    log(json.dumps(rec['assembly'], indent=1)); log(f'DONE {name} {time.monotonic()-t0:.1f}s')
    return rec

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('path'); ap.add_argument('name'); ap.add_argument('outdir')
    ap.add_argument('--norms', default='G0,rF,G1,P2'); ap.add_argument('--order', type=int, default=2); ap.add_argument('--prec', type=int, default=1024)
    args = ap.parse_args()
    run(args.path, args.name, args.outdir, tuple(args.norms.split(',')), args.order, args.prec)
