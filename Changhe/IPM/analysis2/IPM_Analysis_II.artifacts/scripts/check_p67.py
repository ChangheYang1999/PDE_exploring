"""Third computation for verification topic 67 (fractional Gaussian kernels from integer kernels; ordinary frozen
C^(1/2) inverse constant 87 for checkpoints 88 and 131).

Written from the statement of topic 67 only; no verifier code is imported. The routes differ from the verifier's
primary (Arb incomplete gamma and beta) and audit (alternating Taylor series, binomial beta series) routes:

1. Kernel polynomials. P_3 and P_4 from the closed Laguerre form P_j(u) = j! L_j(u) = sum_l binom(j, l) (j!/l!) (-u)^l,
   compared with the recursion (7) P_(j+1) = (1 - u) P_j + (2u - 1) P_j' - u P_j'' and with the record. Root count by
   exact Sturm sequences: all roots of P_j are real, positive and simple, and each unit interval of the record holds
   exactly one. Exact rational bisection to width 2^-300.
2. A_j = 2^alpha int_0^inf u^(alpha/2) exp(-u) |P_j(u)| du by exact reduction of every gamma_lower(5/4 + l, z) to
   gamma_lower(5/4, z) with the recurrence gamma_lower(a + 1, z) = a gamma_lower(a, z) - z^a exp(-z), so that
   F_j(z) = C_j gamma_lower(5/4, z) - exp(-z) z^(5/4) S_j(z) with exact rational C_j and polynomial S_j; the single
   function gamma_lower(5/4, z) is the positive Kummer series z^(5/4) exp(-z) sum z^n/((5/4)(9/4)...(5/4 + n)) with a
   geometric tail, evaluated on the root interval.
3. J0 = B_x(1 - eps, q + eps), x = T/(1 + T), by the positive hypergeometric series
   B_x(a, b) = x^a (1 - x)^b / a * sum_n (a + b)_n/(a + 1)_n x^n with a geometric tail; Jtot by gamma functions.
4. The forward bound (1) at the recorded T, the reverse constant B_(theta, z) of topic 66 recomputed (Kummer series for
   erf and gamma_lower(1/4, z^2), as in check_p66) and compared with the imported rationals 359/50 and 361/50, and the
   ordinary bound 2 B C < 87 for both checkpoints. A few other grid values of T are compared with the record.
5. FLOAT sanity check (not a certificate): the actual weighted kernel integral int |X|^alpha |k_sigma| dX, with
   k_sigma(r) = Gamma(sigma/2 + 1)/(4 pi) 1F1(sigma/2 + 1; 1; -r^2/4), by mpmath quadrature; it must lie below the forward
   bound C and below the topic 66 forward factor sqrt(A_P^2).

Usage: python3 check_p67.py VERIFICATION_RESEARCH_DIR [OUTPUT_JSON]
"""
import json, sys, hashlib, time, re
from fractions import Fraction as Q
from decimal import Decimal
from math import comb, factorial
from pathlib import Path
import mpmath
from mpmath import iv
sys.set_int_max_str_digits(0)
ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).with_suffix('.json')
iv.prec = 500
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
t_start = time.monotonic()
out = {'inputs': {}}


def I(x):
    x = Q(x); return iv.mpf(x.numerator) / iv.mpf(x.denominator)


def fr(t):
    """exact value of a raw mpf tuple (sign, mantissa, exponent, bitcount)."""
    sign, man, e, bc = t
    if not man:
        assert not e, 'infinite or undefined endpoint'
        return Q(0)
    v = Q(int(man)) * Q(2) ** int(e)
    return -v if sign else v


lo = lambda x: fr(x._mpi_[0]); hi = lambda x: fr(x._mpi_[1])


def ball(s):
    m = re.fullmatch(r'\[(.*?) \+/- (.*?)\]', s.strip()); assert m, s
    mid, rad = Q(Decimal(m.group(1))), Q(Decimal(m.group(2)))
    return mid - rad, mid + rad


overlap = lambda x, b: max(lo(x), b[0]) <= min(hi(x), b[1])
rec_path = ROOT / '67_fractional_gaussian/verification/compute.json'
rec = json.loads(rec_path.read_text()); out['inputs'][str(rec_path.relative_to(ROOT))] = sha(rec_path)
p66 = ROOT / '66_gaussian_holder/verification/compute.json'
rec66 = json.loads(p66.read_text()); out['inputs'][str(p66.relative_to(ROOT))] = sha(p66)


# ---------- 1. polynomials and roots ----------
def pev(co, x):
    v = Q(0)
    for c in reversed(co): v = v * x + c
    return v


def pder(co): return [l * co[l] for l in range(1, len(co))]


def padd(*ps):
    n = max(len(p) for p in ps); r = [Q(0)] * n
    for p in ps:
        for i, c in enumerate(p): r[i] += c
    while len(r) > 1 and r[-1] == 0: r.pop()
    return r


def pmulx(p, k=1): return [Q(0)] * k + list(p)


def pscale(p, s): return [s * c for c in p]


def prem(a, b):
    a = list(a)
    while len(a) >= len(b) and any(a):
        f = a[-1] / b[-1]; sh = len(a) - len(b)
        for i, c in enumerate(b): a[sh + i] -= f * c
        a.pop()
        while len(a) > 1 and a[-1] == 0: a.pop()
    return a


def sturm_count(co, a, b):
    seq = [list(map(Q, co)), list(map(Q, pder(co)))]
    while len(seq[-1]) > 1 or seq[-1][0] != 0:
        r = prem(seq[-2], seq[-1])
        if not any(r): break
        seq.append([-c for c in r])
    def V(x):
        s = [pev(p, x) for p in seq]; s = [v for v in s if v != 0]
        return sum(1 for i in range(len(s) - 1) if (s[i] > 0) != (s[i + 1] > 0))
    return V(a) - V(b), len(seq)


polys, roots = {}, {}
P = [Q(1)]
rec_polys = {k['n']: k for k in rec['kernels']}
for j in range(1, 5):
    P = padd(pscale(P, 1), pscale(pmulx(P), -1), pscale(pmulx(pder(P)), 2), pscale(pder(P), -1), pscale(pmulx(pder(pder(P))), -1))
    lag = [Q(comb(j, l) * factorial(j) // factorial(l) * (-1) ** l) for l in range(j + 1)]
    assert P == lag, (j, P, lag)
    if j in (3, 4):
        polys[j] = P
        assert [int(c) for c in P] == rec_polys[j]['polynomial']
total_roots = {}
for j, co in polys.items():
    big = Q(100)
    nall, _ = sturm_count(co, Q(0), big); assert nall == j            # all j roots lie in (0, 100]; degree j, so all real
    assert sturm_count(co, Q(-1, 10**6), Q(0))[0] == 0 and pev(co, 0) > 0
    boxes = []
    for a, b in rec_polys[j]['root_intervals_exact']:
        a, b = Q(a), Q(b)
        # one root in the record box, and the same root in the unit interval [floor(a), floor(a) + 1]
        assert sturm_count(co, a, b)[0] == 1 and pev(co, a) * pev(co, b) < 0
        ua = Q(int(a)); assert sturm_count(co, ua, ua + 1)[0] == 1 and pev(co, ua) * pev(co, ua + 1) < 0
        l_, h_ = ua, ua + 1
        for _ in range(310):
            m = (l_ + h_) / 2
            if pev(co, l_) * pev(co, m) <= 0: h_ = m
            else: l_ = m
        assert pev(co, l_) * pev(co, h_) <= 0 and h_ - l_ < Q(1, 2 ** 300)
        assert max(l_, a) <= min(h_, b)     # overlaps the record root box
        boxes.append((l_, h_))
    assert all(boxes[k][1] < boxes[k + 1][0] for k in range(j - 1))
    roots[j] = boxes
    out[f'P{j}'] = {'coefficients': [int(c) for c in co], 'roots_float': [float(a) for a, _ in boxes],
                    'sturm_roots_in_(0,100]': nall}
    print('P', j, [int(c) for c in co], [float(a) for a, _ in boxes], flush=True)


# ---------- 2. A_j by reduction to gamma_lower(5/4, z) ----------
def g54(z, N=200):
    """gamma_lower(5/4, z) for an interval 0 < z < 20 (positive Kummer series with geometric tail)."""
    s = Q(5, 4); term = 1 / I(s); tot = iv.mpf(0)
    for n in range(N):
        tot += term; term = term * z / I(s + n + 1)
    rho = hi(z) / (s + N + 1); assert rho < Q(1, 2)
    tail = term / (1 - I(rho))
    tot = tot + iv.mpf([0, tail.b])
    return iv.exp(I(s) * iv.log(z)) * iv.exp(-z) * tot


al = Q(1, 2)
A = {}
for j, co in polys.items():
    # gamma_lower(5/4 + l, z) = c_l gamma_lower(5/4, z) - exp(-z) z^(5/4) S_l(z)
    cl, Sl = [Q(1)], [[Q(0)]]
    for l in range(j):
        a = Q(5, 4) + l
        cl.append(a * cl[-1]); Sl.append(padd(pscale(Sl[-1], a), pmulx([Q(1)], l)))
    Cj = sum(co[l] * cl[l] for l in range(j + 1)); Sj = padd(*[pscale(Sl[l], co[l]) for l in range(j + 1)])
    Finf = I(Cj) * iv.gamma(I(Q(5, 4)))
    val = (-1) ** j * Finf
    for k, (a, b) in enumerate(roots[j], 1):
        z = iv.mpf([I(a).a, I(b).b])
        Sz = iv.mpf(0)
        for c in reversed(Sj): Sz = Sz * z + I(c)
        F = I(Cj) * g54(z) - iv.exp(-z) * iv.exp(I(Q(5, 4)) * iv.log(z)) * Sz
        val += 2 * (-1) ** (k - 1) * F
    val = iv.sqrt(iv.mpf(2)) * val
    A[j] = val
    ok = overlap(val, ball(rec_polys[j]['A']))
    out[f'A_{2 * j}'] = {'value': float(lo(val)), 'width': float(hi(val) - lo(val)), 'C_j': str(Cj),
                         'S_j': [str(c) for c in Sj], 'overlap_record': ok}
    print('A', 2 * j, float(lo(val)), float(hi(val) - lo(val)), ok, flush=True)
    assert ok and lo(val) > 0


# ---------- 3. incomplete beta ----------
def beta_lower(a, b, x, N=400):
    """B_x(a, b) for rational a > 0, b > 1, 0 < x < 1 by the positive series x^a (1-x)^b/a sum (a+b)_n/(a+1)_n x^n."""
    assert a > 0 and b > 1 and 0 < x < 1
    Ia, Ib, Ix = I(a), I(b), I(x)
    term = iv.mpf(1); tot = iv.mpf(0)
    for n in range(N):
        tot += term; term = term * (Ia + Ib + n) / (Ia + 1 + n) * Ix
    rho = (a + b + N) / (a + 1 + N) * x; assert rho < 1
    tot = tot + iv.mpf([0, (term / (1 - I(rho))).b])
    return iv.exp(Ia * iv.log(Ix)) * iv.exp(Ib * iv.log(1 - Ix)) / Ia * tot


# ---------- 4. reverse constant B_(theta, z) of topic 66 ----------
def kummer(x, s, N=160):
    tot, term = Q(0), 1 / s
    for n in range(N):
        tot += term; term = term * x / (s + n + 1)
    ratio = x / (s + N + 1); assert ratio < Q(1, 2)
    return iv.mpf([I(tot).a, I(tot + term / (1 - ratio)).b])


def reverse_B(sg, th, z):
    x = z * z
    erf = iv.exp(-I(x)) * I(z) * kummer(x, Q(1, 2)) / iv.sqrt(iv.pi)
    gl = iv.exp(I(Q(1, 4)) * iv.log(I(x))) * iv.exp(-I(x)) * kummer(x, Q(1, 4))
    S = I(sg); a_ = I(al); b = S - a_
    Aa = iv.exp(-b / 2 * iv.log(1 - I(th))); k = 1 / (4 * iv.sqrt(I(th)))
    return 4 * iv.exp(a_ * iv.log(k)) / (a_ * iv.gamma(S / 2)) * (iv.exp(-a_ * iv.log(I(z))) * (1 - Aa * erf) + Aa * gl / iv.sqrt(iv.pi))


rec66s = {r['state']: r for r in rec66['states']}
grid = {(g['state'], g['T']): g for g in rec['grid']}
q = Q(11, 4); Iq = I(q)
for r in rec['states']:
    st = r['state']
    p = ROOT / f'source_audit/state{st:03d}_exact.json'; out['inputs'][str(p.relative_to(ROOT))] = sha(p)
    d = json.loads(p.read_text()); sg = Q(d['exact_parameters']['sigma']); eps = (sg - 6) / 2
    folder = 'state088_handoff' if st == 88 else 'state131_last_unverified'
    src = ROOT.parent.parent / f'source/case4/IPM_case4.artifacts/checkpoints/{folder}/accepted_{st:08d}.json'
    chk = {'sigma_record': str(sg) == r['sigma'], 'eps_record': str(eps) == r['epsilon'], '0<eps<1': 0 < eps < 1,
           'q=n-alpha/2>0': q == 3 - al / 2 > 0, 'source_sha256': sha(src) == r['source_sha256'] == d['source_json_sha256'],
           'n=3,alpha=1/2': r['n'] == 3 and r['alpha'] == '1/2'}
    Ie = I(eps)
    Jtot = iv.gamma(1 - Ie) * iv.gamma(Iq + Ie) / iv.gamma(Iq + 1)

    def forward(T):
        x = T / (1 + T); J0 = beta_lower(1 - eps, q + eps, x)
        IT = I(T); v = iv.exp(-Iq * iv.log(1 + IT)); Tm = iv.exp(-Ie * iv.log(IT))
        first = -Tm * (1 - v) + Iq * J0; second = Tm * (1 + v) - Iq * (Jtot - J0)
        C = (A[4] / Iq * first + A[3] * second) / iv.gamma(1 - Ie)
        return J0, first, second, C

    T = Q(r['T']); J0, first, second, C = forward(T)
    B66 = reverse_B(sg, Q(rec66s[st]['theta']), Q(rec66s[st]['z']))
    Brev = Q(r['B_reverse_rational']); ordinary = 2 * I(Brev) * C; ordinary_direct = 2 * B66 * C
    chk.update({'J0': overlap(J0, ball(r['J0'])), 'Jtot': overlap(Jtot, ball(r['Jtot'])),
                'first_bracket_positive': lo(first) > 0, 'second_bracket_positive': lo(second) > 0,
                'first_bracket': overlap(first, ball(r['first_bracket'])), 'second_bracket': overlap(second, ball(r['second_bracket'])),
                'forward': overlap(C, ball(r['forward_bound'])), 'B66_record': overlap(B66, ball(rec66s[st]['B'])),
                'B66<B_reverse_rational': hi(B66) < Brev, 'ordinary': overlap(ordinary, ball(r['ordinary_bound'])),
                'ordinary<87': hi(ordinary) < 87 == r['safe_integer'], 'direct_ordinary<87': hi(ordinary_direct) < 87})
    other = {}
    for Ts in ('1/2', '3/4', '5/4', '2'):
        _, f1, f2, Cg = forward(Q(Ts)); g = grid[(st, Ts)]
        other[Ts] = {'forward': float(lo(Cg)), 'overlap_record': overlap(Cg, ball(g['forward_bound'])), 'brackets_positive': lo(f1) > 0 and lo(f2) > 0}
        chk[f'grid_T={Ts}'] = other[Ts]['overlap_record'] and other[Ts]['brackets_positive']
    out[f'state{st}'] = {'sigma_float': float(sg), 'eps_float': float(eps), 'T': str(T), 'J0': float(lo(J0)), 'Jtot': float(lo(Jtot)),
                         'first': float(lo(first)), 'second': float(lo(second)), 'forward_upper': float(hi(C)),
                         'B66_upper': float(hi(B66)), 'ordinary_upper': float(hi(ordinary)),
                         'ordinary_direct_upper': float(hi(ordinary_direct)), 'margin_below_87': float(87 - hi(ordinary)),
                         'other_T': other, 'checks': chk}
    print(st, {k: v for k, v in out[f'state{st}'].items() if k not in ('checks', 'other_T')}, flush=True)
    print(chk, flush=True)
    assert all(chk.values())

# ---------- 5. FLOAT sanity check of the true kernel integral ----------
mpmath.mp.dps = 30
flt = {}
for r in rec['states']:
    st = r['state']; sg = mpmath.mpf(Q(r['sigma']).numerator) / Q(r['sigma']).denominator
    k = lambda rr: mpmath.gamma(sg / 2 + 1) / (4 * mpmath.pi) * mpmath.hyp1f1(sg / 2 + 1, 1, -rr * rr / 4)
    zeros = []
    grid_r = [mpmath.mpf(i) / 20 for i in range(1, 400)]
    vals = [k(x) for x in grid_r]
    for i in range(len(vals) - 1):
        if vals[i] * vals[i + 1] < 0: zeros.append(mpmath.findroot(k, (grid_r[i], grid_r[i + 1]), solver='anderson'))
    pts = [0] + zeros + [mpmath.inf]
    tot = sum(mpmath.quad(lambda rr: 2 * mpmath.pi * rr ** 1.5 * abs(k(rr)), [pts[i], pts[i + 1]]) for i in range(len(pts) - 1))
    integral0 = mpmath.quad(lambda rr: 2 * mpmath.pi * rr * k(rr), pts)
    Cup = out[f'state{st}']['forward_upper']
    ap66 = next(x for x in rec66['records'] if x['state'] == st and x['degree'] == 5 and x['family'] == 'binomial')
    sqrtAP = float(mpmath.sqrt(mpmath.mpf(ball(ap66['A_squared'])[1].numerator) / ball(ap66['A_squared'])[1].denominator))
    flt[st] = {'zeros_r': [float(z) for z in zeros], 'weighted_L1_FLOAT': float(tot), 'kernel_integral_FLOAT': float(integral0),
               'forward_bound_C': Cup, 'topic66_sqrtA_P': sqrtAP, 'below_C': float(tot) < Cup, 'below_topic66': float(tot) < sqrtAP}
    print(st, 'FLOAT', flt[st], flush=True)
    assert flt[st]['below_C'] and flt[st]['below_topic66']
out['float_sanity'] = flt
out['all_pass'] = True
out['seconds'] = round(time.monotonic() - t_start, 1)
out['code_sha256'] = sha(Path(__file__))
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE')
