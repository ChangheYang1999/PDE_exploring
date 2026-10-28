"""Third computation, in bivariate interval Taylor arithmetic, of the necessary local distance tests (verification
topics 38, 40, 41, 42 and 45) and of the b6 derivative values (topic 36).

For an exact reference potential chi = sum b_(j,m,k) Re(z^(2m)) t^(k-m) w^(p_j-m), z = x + iy, w = 1 + x^2 + y^2,
t = (x^2 + y^2)/w, p_j = (3 + gamma - j delta)/2, the normalized Taylor coefficients chi_(a,b)/(a! b!) up to total
order N are computed in mpmath interval arithmetic (outward rounding), with power jets from the Euler-operator
recurrence u E v = alpha v E u. Evaluated at a point interval this encloses the jet at that point; evaluated at a box
it encloses the coefficients at every point of the box. The fields are rho = -chi_xxy - chi_yyy,
V = (c x - chi_xyy, c y + chi_xxy) and F = V.D rho - rho, by differentiation and multiplication of jets.

Point tests (topics 38, 40, 42), s = 3 * 2^-31: a = 4 s^(-1/2), g = max(1, r)^(1/5), H = min(a|y|, 16 g),
B = min(a r, 104 g), A = a|V| + H + B|D rho|, Q = a B; the largest q = 2^-k with |F| > A q + Q q^2 is found.
At every point the residual lower bound N(F) >= 12 |F(X)|/g(X) of topic 45 is also formed and compared exactly with
the recorded lower bound.
Square tests (topic 41): on the square of center X0 and half side delta, Taylor's formula of order K = 6 with the box
enclosure of the order-K coefficients bounds inf |F|, sup |V| and sup |D rho|; with H = 16 g, B = 104 g, d = 15/(4 delta),
A = H (V d + |2c + 1|) + B D and Q = H B d, the largest q = 2^-k with inf |F| > A q + Q q^2 is found; the same is
done with the amplitude constants H = g/12, B = 3 g/16 of topics 44 and 45.
Every comparison is made on interval endpoints with outward rounding.

Usage: python3 check_jet_distance.py VERIFICATION_RESEARCH_DIR [OUTPUT_JSON] [--only NAME,...] [--squares-only]
"""
import json, sys, time, hashlib
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
from mpmath import iv
sys.set_int_max_str_digits(0)
iv.prec = 320

ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 and not sys.argv[2].startswith('--') else Path(__file__).with_suffix('.json')
ONLY = None
if '--only' in sys.argv:
    ONLY = sys.argv[sys.argv.index('--only') + 1].split(',')
NAMES = ['state131', 'nb_stableA2_exact', 'nb_stableA3_exact', 'nb_stableA4_exact', 'nb_stableA5_exact',
         'nb_Mpen_exact', 'nb_A6dpen_exact', 'nb_Mpen2_exact', 'nb_b6_exact', 'nb_d2_exact']
POINTS = [('0', '1/10'), ('0', '1/5'), ('0', '2/5'), ('0', '4/5'), ('0', '1'), ('0', '2'), ('1', '1'), ('3', '4'), ('6', '8')]
EXTRA_POINTS = {'state131': [('12', '16'), ('30', '40'), ('60', '80')]}
SQUARES = {'nb_Mpen2_exact': [('0', '4/5', 10), ('0', '2/5', 10)], 'nb_d2_exact': [('0', '2/5', 10)]}
K = 6                                   # order of the box remainder in the square tests


def fr(t):
    """exact value of a raw mpf tuple (sign, mantissa, exponent, bitcount); to_man_exp alone drops the sign."""
    sign, man, e, bc = t
    if not man:
        assert not e, 'infinite or undefined endpoint'
        return Q(0)
    v = Q(int(man)) * Q(2) ** int(e)
    return -v if sign else v


lo = lambda x: fr(x._mpi_[0]); hi = lambda x: fr(x._mpi_[1])
I = lambda q: iv.mpf(Q(q).numerator) / Q(q).denominator
mag = lambda x: max(abs(lo(x)), abs(hi(x)))     # exact upper bound of |x|


def mig(x):                                     # exact lower bound of |x|
    a, b = lo(x), hi(x)
    return a if a > 0 else (-b if b < 0 else Q(0))


class Jets:
    def __init__(self, N):
        self.N = N
        self.idx = [(i, n - i) for n in range(N + 1) for i in range(n, -1, -1)]
        self.pos = {ij: k for k, ij in enumerate(self.idx)}
        self.L = len(self.idx)
        self.mt = [[(self.pos[a, b], self.pos[i - a, j - b]) for a in range(i + 1) for b in range(j + 1)]
                   for i, j in self.idx]
        self.pt = [[(self.pos[a, b], self.pos[i - a, j - b], a + b) for a in range(i + 1) for b in range(j + 1)
                    if (a, b) != (0, 0)] for i, j in self.idx]

    def zero(self): return [iv.mpf(0)] * self.L
    def const(self, v): return [v] + [iv.mpf(0)] * (self.L - 1)

    def var(self, v, which):
        u = self.const(v); u[self.pos[(1, 0) if which == 0 else (0, 1)]] = iv.mpf(1); return u

    def mul(self, u, v):
        return [iv.fsum(u[p] * v[q] for p, q in pairs) if pairs else iv.mpf(0) for pairs in self.mt]

    def power(self, u, alpha):
        v = [None] * self.L
        v[0] = iv.exp(alpha * iv.log(u[0]))
        for k in range(1, self.L):
            n = self.idx[k][0] + self.idx[k][1]
            v[k] = iv.fsum(u[p] * v[q] * (alpha * s - (n - s)) for p, q, s in self.pt[k]) / (n * u[0])
        return v

    def add(self, u, v, a=1): return [x + a * y for x, y in zip(u, v)]

    def shift(self, u, a, b, M):
        """jet of order M of d^(a,b) f."""
        return [u[self.pos[i + a, j + b]] * (factorial(i + a) // factorial(i)) * (factorial(j + b) // factorial(j))
                for n in range(M + 1) for i in range(n, -1, -1) for j in [n - i]]


def source(name):
    if name == 'state131':
        p = ROOT / 'source_audit/state131_exact.json'
    elif name == 'nb_b6_exact':
        p = ROOT / '36_b6_candidates/verification/nb_b6_exact.audit.json'
    else:
        p = ROOT / f'19_nb_candidates/verification/{name}.audit.json'
    raw = p.read_bytes(); d = json.loads(raw)
    cl, a0 = (d['exact_parameters']['cl'], d['exact_parameters']['a0']) if name == 'state131' else (d['cl'], d['origin_slope'])
    terms = [(tuple(k), Q(v)) for k, v in zip(d['canonical_order'], d['canonical_coefficients'])]
    return p, hashlib.sha256(raw).hexdigest(), Q(cl), a0, terms


def chi_jet(J, terms, c, X, Y, t0=Q(0)):
    """chi = sum_j w^(p_j) sum_m Re(zeta^m) P_jm(t) with zeta = z^2/w (|zeta| = t), so that the growth of z^(2m) and the
    decay of w^(-m) never appear separately; the polynomials P_jm are re-expanded exactly in powers of tau = t - t0
    (no cancellation over a box near t0)."""
    g = 1 / c; dl = 1 - g
    groups = {}
    for (j, m, k), v in terms:
        groups.setdefault((j, m), {})
        groups[j, m][k - m] = groups[j, m].get(k - m, Q(0)) + v
    for key, P in groups.items():
        top = max(P)
        groups[key] = [(n, sum((P.get(e, Q(0)) * comb(e, n) * t0 ** (e - n) for e in range(n, top + 1)), Q(0)))
                       for n in range(top + 1)]
    x = J.var(X, 0); y = J.var(Y, 1)
    r2 = J.add(J.mul(x, x), J.mul(y, y)); w = J.add(J.const(iv.mpf(1)), r2); wi = J.power(w, iv.mpf(-1))
    t = J.mul(r2, wi); t[0] -= I(t0)
    emax = max(e for gr in groups.values() for e, _ in gr)
    tp = [J.const(iv.mpf(1))]
    for _ in range(emax): tp.append(J.mul(tp[-1], t))
    mmax = max(m for _, m in groups)
    zeta = (J.mul(J.add(J.mul(x, x), J.mul(y, y), -1), wi), J.mul([2 * a for a in J.mul(x, y)], wi))
    zp = [(J.const(iv.mpf(1)), J.zero())]
    for _ in range(mmax):
        a, b = zp[-1]
        zp.append((J.add(J.mul(a, zeta[0]), J.mul(b, zeta[1]), -1), J.add(J.mul(a, zeta[1]), J.mul(b, zeta[0]))))
    chi = J.zero()
    for j in sorted({j for j, _ in groups}):
        S = J.zero()
        for (jj, m), gr in sorted(groups.items()):
            if jj != j: continue
            P = J.zero()
            for e, v in gr:
                P = J.add(P, tp[e], I(v))
            S = J.add(S, J.mul(zp[m][0], P))
        chi = J.add(chi, J.mul(J.power(w, I((3 + g - j * dl) / 2)), S))
    return chi


def fields(J, chi, c, X, Y):
    N = J.N; M = N - 3
    JM = Jets(M)
    rho = [-(a + b) for a, b in zip(J.shift(chi, 2, 1, M), J.shift(chi, 0, 3, M))]
    V1 = [-a for a in J.shift(chi, 1, 2, M)]; V2 = J.shift(chi, 2, 1, M)
    V1[0] += I(c) * X; V2[0] += I(c) * Y
    V1[JM.pos[1, 0]] += I(c); V2[JM.pos[0, 1]] += I(c)
    rx, ry = JM.shift(rho, 1, 0, M - 1), JM.shift(rho, 0, 1, M - 1)
    J1 = Jets(M - 1)
    cut = lambda u: u[:J1.L]
    F = J1.add(J1.add(J1.mul(cut(V1), rx), J1.mul(cut(V2), ry)), cut(rho), -1)
    return {'J': JM, 'rho': rho, 'V1': V1, 'V2': V2, 'J1': J1, 'rx': rx, 'ry': ry, 'F': F}


def deriv_norm(Jx, comps, n):
    """exact upper bound of the Frobenius norm of the n-th derivative tensor of the field with these jets."""
    s = iv.mpf(0)
    for u in comps:
        for i in range(n + 1):
            dv = mag(u[Jx.pos[i, n - i]]) * factorial(i) * factorial(n - i)
            s += comb(n, i) * I(dv * dv)
    return iv.sqrt(s)


def point_test(name, c, terms, xs, ys):
    X, Y = I(Q(xs)), I(Q(ys))
    J = Jets(4); chi = chi_jet(J, terms, c, X, Y); f = fields(J, chi, c, X, Y)
    F = f['F'][0]; V = iv.sqrt(f['V1'][0] ** 2 + f['V2'][0] ** 2); D = iv.sqrt(f['rx'][0] ** 2 + f['ry'][0] ** 2)
    s = Q(3, 2 ** 31); a = 4 / iv.sqrt(I(s)); x, y = Q(xs), Q(ys)
    r = iv.sqrt(I(x * x + y * y)); g = iv.mpf(1) if x * x + y * y <= 1 else r ** (iv.mpf(1) / 5)
    H = min(hi(a * abs(I(y))), hi(16 * g)); B = min(hi(a * r), hi(104 * g))
    A = hi(a * V + I(H) + I(B) * D); Qc = hi(a * I(B)); Fm = mig(F)
    k = next((k for k in range(90) if Fm > A * Q(1, 2 ** k) + Qc * Q(1, 4 ** k)), None)
    Nl = 12 * Fm / hi(g)                                   # N(F) >= 12 |F(X)| / g(X) (amplitude constant 1/12)
    gap = max(k for k in range(-40, 90) if Nl > Q(2) ** (k - 30))
    return {'point': [xs, ys], 'F_lo': float(lo(F)), 'F_hi': float(hi(F)), 'V_hi': float(hi(V)), 'Drho_hi': float(hi(D)),
            'dyadic_power_t0': k, 'N_lower_amp44': float(Nl), 'gap_power_over_2^-30': gap}, Nl


def square_test(name, c, terms, xs, ys, dpow):
    X0, Y0 = Q(xs), Q(ys); dl = Q(1, 2 ** dpow); N = K + 4
    t0 = (X0 * X0 + Y0 * Y0) / (1 + X0 * X0 + Y0 * Y0)
    Jt = Jets(N); ft = fields(Jt, chi_jet(Jt, terms, c, I(X0), I(Y0), t0), c, I(X0), I(Y0))
    BX = iv.mpf([I(X0 - dl), I(X0 + dl)]); BY = iv.mpf([I(Y0 - dl), I(Y0 + dl)])   # outward hulls
    Jb = Jets(N); fb = fields(Jb, chi_jet(Jb, terms, c, BX, BY, t0), c, BX, BY)
    def sup_dev(Jx, uc, ub, order):
        """sum over 1 <= |alpha| < order of |T_alpha(X0)| dl^|alpha| plus sum over |alpha| = order of sup |T_alpha| dl^order."""
        tot = Q(0)
        for n in range(1, order + 1):
            for i in range(n + 1):
                k = Jx.pos[i, n - i]
                tot += (mag(uc[k]) if n < order else mag(ub[k])) * dl ** n
        return tot
    J1 = ft['J1']; JM = ft['J']
    Fc = ft['F'][0]
    f_low = mig(Fc) - sup_dev(J1, ft['F'], fb['F'], K)
    assert J1.N >= K and JM.N >= K
    Vsup = [mag(ft[v][0]) + sup_dev(JM, ft[v], fb[v], K) for v in ('V1', 'V2')]
    Dsup = [mag(ft[v][0]) + sup_dev(J1, ft[v], fb[v], K) for v in ('rx', 'ry')]
    V = hi(iv.sqrt(I(Vsup[0] ** 2 + Vsup[1] ** 2))); D = hi(iv.sqrt(I(Dsup[0] ** 2 + Dsup[1] ** 2)))
    rmax = hi(iv.sqrt(I(X0 * X0 + Y0 * Y0)) + iv.sqrt(2) * I(dl))
    g = Q(1) if rmax <= 1 else hi(I(rmax) ** (iv.mpf(1) / 5))
    d = Q(15) / (4 * dl); ks = []
    for H, B in [(16 * g, 104 * g), (g / 12, 3 * g / 16)]:   # amplitude constants of topic 18 and of topic 44
        A = H * (V * d + abs(2 * c + 1)) + B * D; Qc = H * B * d
        ks.append(next((k for k in range(90) if f_low > A * Q(1, 2 ** k) + Qc * Q(1, 4 ** k)), None))
    k = ks[0]
    return {'center': [xs, ys], 'half_side_power': dpow, 'K': K, 'F_center': [float(lo(Fc)), float(hi(Fc))],
            'inf_absF_lower': float(f_low), 'remainder_part_F': float(sum(mag(fb['F'][J1.pos[i, K - i]]) for i in range(K + 1)) * dl ** K),
            'sup_V_upper': float(V), 'sup_Drho_upper': float(D), 'dyadic_power': k, 'dyadic_power_amp44': ks[1]}


def run(name, squares_only):
    t0 = time.monotonic()
    p, sha, c, a0rec, terms = source(name)
    out = {'source': str(p.relative_to(ROOT)), 'source_sha256': sha, 'terms': len(terms)}
    J = Jets(4); chi0 = chi_jet(J, terms, c, iv.mpf(0), iv.mpf(0)); f0 = fields(J, chi0, c, iv.mpf(0), iv.mpf(0))
    norm = I(c) + 4 * chi0[J.pos[2, 2]]                       # c + chi_xxyy(0)
    slope = f0['ry'][0]
    out['normalization_c_plus_chi_xxyy0'] = [float(lo(norm)), float(hi(norm))]
    out['slope'] = [float(lo(slope)), float(hi(slope))]
    out['slope_record'] = str(a0rec)[:40]
    assert lo(norm) <= 1 <= hi(norm)
    out['slope_contains_record'] = lo(slope) <= Q(a0rec) <= hi(slope)
    assert out['slope_contains_record']
    if not squares_only:
        out['points'] = []
        rec45 = json.loads((ROOT / '45_improved_distances/verification/audit_rational.json').read_text())
        rec45 = {tuple(t['point']): Q(t['N_strict_lower_exact']) for r in rec45['residual'] if r['name'] == name for t in r['tests']}
        agree = 0
        for xs, ys in POINTS + EXTRA_POINTS.get(name, []):
            row, Nl = point_test(name, c, terms, xs, ys); out['points'].append(row)
            row['exceeds_recorded_topic45_lower_bound'] = Nl > rec45[xs, ys]; agree += row['exceeds_recorded_topic45_lower_bound']
            print(name, row, flush=True)
        out['topic45_point_bounds_confirmed'] = f'{agree}/{len(rec45)}'
        out['best_gap_power_over_2^-30'] = max(r['gap_power_over_2^-30'] for r in out['points'])
    if name == 'nb_b6_exact' and not squares_only:
        J7 = Jets(7)
        for (xs, ys), n, key in [(('0', '1/5'), 2, 'D2rho_at_0_1/5'), (('3', '4'), 4, 'D4rho_at_3_4')]:
            f7 = fields(J7, chi_jet(J7, terms, c, I(Q(xs)), I(Q(ys))), c, I(Q(xs)), I(Q(ys)))
            s = iv.mpf(0)
            for i in range(n + 1):
                v = f7['rho'][f7['J'].pos[i, n - i]] * factorial(i) * factorial(n - i)
                s += comb(n, i) * I(mig(v)) ** 2
            low = lo(iv.sqrt(s))
            if n == 4: low *= 26
            out[key + ('' if n == 2 else '_times_<r>^2') + '_lower'] = float(low)
            print(name, key, float(low), flush=True)
    if name in SQUARES:
        out['squares'] = []
        for xs, ys, dp in SQUARES[name]:
            row = square_test(name, c, terms, xs, ys, dp); out['squares'].append(row)
            print(name, row, flush=True)
    out['seconds'] = round(time.monotonic() - t0, 1)
    return out


if __name__ == '__main__':
    res = {'method': 'bivariate interval Taylor arithmetic (mpmath iv, 320 bits)', 'candidates': {}}
    for name in (ONLY or NAMES):
        res['candidates'][name] = run(name, '--squares-only' in sys.argv)
    res['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.write_text(json.dumps(res, indent=2) + '\n'); print('DONE')
