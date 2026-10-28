"""Lead evaluation, for independent audit: the exact exterior tail (V222), the sharp deficiencies (V205) at the fixed V209
radii, and the full even-moment reflection saving (V223) on the optimal outer-tangent axis disks (V224).

Disks. sigma is isolated in (0,1/3) by exact rational signs of p(s)=2s^4-3s^2+4s-1. H(s)=(1-2s^2)^2/(2(1-2s+2s^3)) is
evaluated in ball arithmetic on the whole isolating interval; a rational c >= the upper endpoint satisfies c >= H(sigma) =
max H, so the disk with centre c and radius a=1-c is contained (V224: c >= H(s) for all s is the containment condition);
also 2/3 < c < 3/4, so a < c/2 and the exact radial minorant holds. c is used exactly (rational) below.

Moments. B_m(c)=int_0^a t^m/(c+t)^2 dt = int_c^1 (u-c)^m u^-2 du, expanded exactly: a rational part plus m(-c)^(m-1)(-log c).
A_n(alpha)=2 alpha prod_(k=1)^(2n-1)(k-alpha)/(n!)^2 (exact rational). Savings use finite partial sums of positive terms
(lower bounds); NT terms. Unperturbed local rows: s=1/2. Retained cutoff rows: s=rho and B^rho_m=B_m-rho^2 a^(m+1)/((m+1)(1-rho)^2).
Uniform D envelope: saving/alpha >= sum_n [A_n(eps)/eps] rho^(2n) B^rho_(2n+1), since A_n(alpha)/alpha decreases in alpha.

Exterior tail. T(alpha)=2^(alpha+1) alpha S(alpha)/pi with S <= S_N^+ (N=64), exact rational at rational alpha.

Bases for the ten table rows: previous_upper_D (exact rationals, before any reflection saving) of the V220 manifest.
Precision 512 bits (and 768 bits as a check). Upper results: exact dyadic upper endpoints rounded up to 10 places.
Single-threaded, a few seconds."""
import json, sys, hashlib
from fractions import Fraction as Fr
from math import comb, factorial
from flint import arb, ctx, fmpq

R = ''
V209F = R + '08_improved_upper_bounds/explicit_second_term/sharp_deficiency/numerical_values/accepted.json'
V220F = R + '08_improved_upper_bounds/local_projection/strict_increment/larger_disks/exact_radial_density/cross4096_values/accepted.json'
NT = 30; NTAIL = 64

def q2a(f): return arb(fmpq(f.numerator, f.denominator))
def exact(x): m, e = x.man_exp(); m = int(m); e = int(e); return Fr(m * 2 ** e) if e >= 0 else Fr(m, 2 ** (-e))
def hi(x): return exact(x.upper())
def lo(x): return exact(x.lower())
def ceil10(f): n = -((-f.numerator * 10 ** 10) // f.denominator); return Fr(n, 10 ** 10)
def dec10(f): n = f * 10 ** 10; assert n.denominator == 1; n = int(n); return '%d.%010d' % (n // 10 ** 10, n % 10 ** 10)

def p_(s): return 2 * s ** 4 - 3 * s ** 2 + 4 * s - 1
def isolate():
    l, h = Fr(0), Fr(1, 3); assert p_(l) < 0 < p_(h)
    for _ in range(300):
        m = (l + h) / 2
        if p_(m) < 0: l = m
        else: h = m
    return l, h

def run(prec):
    ctx.prec = prec
    pi = arb.pi(); log2 = arb(2).log()
    # Catalan's constant: the library ball (the 384-bit V209 run used the exact rational enclosure; here only a check)
    G = arb.const_catalan()
    sl, sh = isolate()
    S0 = q2a(sl).union(q2a(sh))
    Hb = (1 - 2 * S0 * S0) ** 2 / (2 * (1 - 2 * S0 + 2 * S0 ** 3))
    cH = hi(Hb)
    c = Fr(-((-cH.numerator * 10 ** 40) // cH.denominator), 10 ** 40)   # rational c >= max H, rounded up at 1e-40
    assert Fr(2, 3) < c < Fr(3, 4) and c >= cH
    a = 1 - c
    cb = q2a(c); logc = cb.log()
    def Bm(m, cc=c, lg=None):
        cc = Fr(cc); lg = q2a(cc).log() if lg is None else lg
        rat = (-cc) ** m * (1 / cc - 1)
        for j in range(2, m + 1): rat += comb(m, j) * (-cc) ** (m - j) * (1 - cc ** (j - 1)) / (j - 1)
        return q2a(rat) - m * q2a((-cc) ** (m - 1)) * lg
    # sanity: closed forms at c=3/4 and elementary bounds at c
    J34 = -arb(31) / 32 + arb(27) / 8 * (arb(4) / 3).log(); K34 = -arb(233) / 1024 + arb(405) / 512 * (arb(4) / 3).log()
    assert (2 * Bm(3, Fr(3, 4)) - J34).contains(0) and (Bm(5, Fr(3, 4)) / 2 - K34).contains(0)
    B = {}
    for m in range(1, 2 * NT + 3):
        B[m] = Bm(m, c, logc)
        assert lo(B[m]) >= a ** (m + 1) / (m + 1) and hi(B[m]) <= a ** (m + 1) / ((m + 1) * c * c), m
    def An(al, n):
        p = Fr(1)
        for k in range(1, 2 * n): p *= (k - al)
        return 2 * al * p / factorial(n) ** 2
    def sav_local(al, s=Fr(1, 2)):
        assert 2 * a * s < 1
        return sum((q2a(An(al, n) * s ** (2 * n)) * B[2 * n + 1] for n in range(1, NT + 1)), arb(0))
    def Brho(m, rho): return B[m] - q2a(rho ** 2 * a ** (m + 1) / ((m + 1) * (1 - rho) ** 2))
    def sav_cut(al, rho):
        assert 2 * a * rho < 1 and rho < Fr(1, 2)
        tot = arb(0)
        for n in range(1, NT + 1):
            b = Brho(2 * n + 1, rho); assert lo(b) > 0
            tot += q2a(An(al, n) * rho ** (2 * n)) * b
        return tot
    def sav_env(eps, rho):
        tot = arb(0)
        for n in range(1, NT + 1):
            b = Brho(2 * n + 1, rho); assert lo(b) > 0
            tot += q2a(An(eps, n) / eps * rho ** (2 * n)) * b
        return tot
    # two-term saving at c=3/4 (V206), to reproduce the V220 gains
    def eta34(al):
        p = al * (1 - al); q = p * (2 - al) * (3 - al)
        return q2a(p) * J34 / 4 + q2a(q) * K34 / 16
    # exterior tail, exact rational upper bound S_N^+
    def Splus(al, N=NTAIL):
        s = Fr(0)
        for n in range(N): s += Fr(n + 1, 4 ** n) / ((2 * n + 1 - al) * (2 * n + 1))
        return s + Fr(4, 3) * Fr(1, 4 ** N) * (N + 1) / ((2 * N + 1 - al) * (2 * N + 1))
    def A_(al): return ((al + 2) / 2).gamma() / (2 * pi.sqrt() * ((al + 3) / 2).gamma())
    def a2(al): return arb(2) ** (1 + al / 2) / (pi * (2 + al))
    def E(r): return -(1 - r * r).log() / 2
    def N0(r): return arb(1) / 2 - 2 / pi * r.log()
    def Lr(r): return (-(1 - 2 * r).log()).max((1 + 2 * r) * (1 + 2 * r).log())
    def BC(r): return r * r / (2 * (1 - r) ** 2) * (-r.log() + arb(1) / 2 + 2 * G / pi)
    def BD(r): return r * r / (2 * (1 - r) ** 2) * (-r.log() + arb(1) / 2 + log2)
    def T(al, Sx): return arb(2) ** (al + 1) / pi * al * Sx
    def JC(al, r, Sx): return 2 * a2(al) * r ** al / al + arb(2) ** al * N0(r) + (arb(2) ** al - 1) * E(r) + T(al, Sx) + al * (BC(r) + E(r) * Lr(r))
    def JD(al, r, Sx): return 2 * A_(al) * r ** al / al + arb(1) / 2 + arb(2) ** al * N0(r) + (arb(2) ** al - 1) * E(r) + T(al, Sx) + al * (BD(r) + 3 * E(r) * Lr(r))
    out = {'precision_bits': prec, 'sigma_interval': [str(sl), str(sh)], 'H_on_sigma_interval_upper': float(cH),
           'c': str(c), 'a': str(a), 'terms': NT, 'tail_terms': NTAIL}
    # finite rows at the V209 radii
    V209 = json.load(open(V209F)); assert V209['verdict'] == 'CONFIRMED'
    fin = []
    for x in V209['rows']:
        if x['mode'] != 'finite' or x['retained_reflection']: continue
        al = Fr(x['alpha_or_epsilon']); rho = Fr(x['rho']); alb = q2a(al); rb = q2a(rho)
        Sx = q2a(Splus(al))
        if x['operator'] == 'C':
            v = JC(alb, rb, Sx); fin.append({'operator': 'C', 'alpha': x['alpha_or_epsilon'], 'rho': x['rho'],
                                             'upper': dec10(ceil10(hi(v))), 'V209': x['safe_upper']})
        else:
            v = JD(alb, rb, Sx); w = v - sav_cut(al, rho)
            fin.append({'operator': 'D', 'alpha': x['alpha_or_epsilon'], 'rho': x['rho'], 'upper_no_reflection': dec10(ceil10(hi(v))),
                        'upper_with_reflection': dec10(ceil10(hi(w))), 'V209_no_reflection': x['safe_upper'],
                        'saving_lower': float(lo(sav_cut(al, rho)))})
    out['finite'] = fin
    # uniform envelope, eps = 1/100, at the V209 radii
    eps = Fr(1, 100); eb = q2a(eps)
    def Z(r): return (N0(r) + E(r)) * ((arb(2) ** eb - 1) / eb) + arb(2) ** (eb + 1) / pi * q2a(Splus(eps))
    def KC(r): l = r.log() + log2 / 2 - arb(1) / 2; return (l ** 2 + arb(1) / 4) / pi + Z(r) + BC(r) + E(r) * Lr(r)
    def KD(r): l = r.log() + log2 - 1; return (l ** 2 + 1 - pi ** 2 / 12) / pi + Z(r) + BD(r) + 3 * E(r) * Lr(r)
    rC, rD = Fr(34891, 100000), Fr(15993, 50000)
    out['envelope'] = {'K_C': dec10(ceil10(hi(KC(q2a(rC))))), 'K_D': dec10(ceil10(hi(KD(q2a(rD))))),
                       'K_D_with_reflection': dec10(ceil10(hi(KD(q2a(rD)) - sav_env(eps, rD)))), 'rho_C': str(rC), 'rho_D': str(rD)}
    # ten table rows: V220 bases minus the full saving at c (unperturbed local rows only)
    V220 = json.load(open(V220F)); assert V220['verdict'] == 'CONFIRMED'
    tab = []
    for x in V220['rows']:
        if x['kind'] != 'unperturbed local': continue
        al = Fr(x['alpha']); base = Fr(x['previous_upper_D'])
        g34 = eta34(al); gs = sav_local(al)
        chk = ceil10(hi(q2a(base) - g34))
        tab.append({'alpha': x['alpha'], 'V220_safe_upper_D': x['safe_upper_D'], 'recomputed_c34_two_terms': dec10(chk),
                    'upper_D': dec10(ceil10(hi(q2a(base) - gs))), 'saving_c34_lower': float(lo(g34)), 'saving_lower': float(lo(gs)),
                    'extra_saving_lower': float(lo(gs - g34))})
        assert dec10(chk) == x['safe_upper_D'] or abs(chk - Fr(x['safe_upper_D'])) <= Fr(1, 10 ** 10), (x['alpha'], dec10(chk))
    out['table_rows'] = tab
    return out

res = {p: run(p) for p in (512, 768)}
a, b = res[512], res[768]
for k in ('finite', 'table_rows'):
    for x, y in zip(a[k], b[k]):
        for f in x:
            if f.startswith('upper') or f == 'upper': assert x[f] == y[f], (k, f, x[f], y[f])
assert a['envelope'] == b['envelope'] and a['c'] == b['c']
src = {f: hashlib.sha256(open(f, 'rb').read()).hexdigest() for f in (V209F, V220F, __file__)}
json.dump({'runs': res, 'sha256': src}, open(sys.argv[1] if len(sys.argv) > 1 else 'eval_all.json', 'w'), indent=1)
print(json.dumps(a, indent=1))
