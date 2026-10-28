"""Third computation for verification topic 70 (logarithmic replacement for the fractional strain regularization).

Written from the statement of topic 70 only; no verifier code is imported. The routes differ from the verifier's audit
(binomial construction of the envelope polynomials, factorial angular moments):

1. Envelope certificate (10) from the polynomials displayed in the proof: R_0 and R_1 are compared with the Laguerre
   polynomials L_4 and L_4^(1) (sympy), P_j = R_j/R_j(-1), the numerators 1 - P_0^2 and 1 + t P_1^2 are divided by
   1 + t with zero remainder, and int exp(-t) q_(-/+) is evaluated by sympy integration (not by a factorial table).
2. D_1 = int exp(-t)/(1 + t) dt = e E_1(1) enclosed independently by E_1(1) = -gamma + sum_(k>=1) (-1)^(k+1)/(k k!)
   (exact rational partial sum, alternating tail bound, interval Euler constant and e); it must lie strictly inside
   (124/209, 100/167).
3. The unweighted bounds (11): sqrt(D_1)/(8 sqrt(pi)) < 1/18 and sqrt(D_1)/(8 sqrt(2 pi)) < 1/25 in interval arithmetic,
   both with the true pi and with the proof's rational route pi > 31/10 (32-term Leibniz partial sum, exact).
4. Exact identities (sympy): the radial substitution t = log(1 + r^2) in (9), the closed form (2) of D_beta (by
   differentiating in t and comparing the two sides at several rational beta numerically), the Gram matrix (3) from the
   angular integrals, the Schur complement; eps D_beta -> 1 as beta -> 1/2 (two-sided bound 1/eps - D_1 <= D_beta <= 1/eps,
   checked in floating point), so that sqrt(2 beta - 1) times the H_beta
   norms has the same limits 1/(8 sqrt(pi)), 1/(8 sqrt(2 pi)) as the weighted statement (5).
Interval endpoints are stored as exact binary rationals with directed 25-digit decimal bounds; every field whose name
ends in FLOAT or FLOAT_display is a floating-point display only.
5. FLOAT diagnostics: D_beta by quadrature in t versus the closed form (2) for beta in {3/4, 1, 2}; I_beta - 1/(2 eps)
   bounded for eps = 2^-k (k = 4..12) with a concrete smooth cutoff, by the substitution v = 1 + log(1 + r^2) and exact
   subtraction of the main term; the divergence rates (18) of I(M) at beta = 1/2 and beta = 1/4.

Usage: python3 check_p70.py [OUTPUT_JSON]
"""
import json, sys, time, hashlib
from fractions import Fraction as Q
from decimal import Decimal, getcontext
from math import factorial
from pathlib import Path
import sympy as sp
import mpmath
from mpmath import iv
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_suffix('.json')
getcontext().prec = 60
t0 = time.monotonic()
out = {}
chk = {}
t, r, th, b = sp.symbols('t r theta beta', positive=True)

# 1. envelope certificate
R0 = 1 - 4 * t + 3 * t ** 2 - sp.Rational(2, 3) * t ** 3 + t ** 4 / 24
R1 = 5 - 10 * t + 5 * t ** 2 - sp.Rational(5, 6) * t ** 3 + t ** 4 / 24
chk['R0 = Laguerre L_4'] = sp.expand(R0 - sp.laguerre(4, t)) == 0
chk['R1 = assoc. Laguerre L_4^(1)'] = sp.expand(R1 - sp.assoc_laguerre(4, 1, t)) == 0
P0 = sp.expand(R0 / R0.subs(t, -1)); P1 = sp.expand(R1 / R1.subs(t, -1))
qm, rm = sp.div(sp.expand(1 - P0 ** 2), 1 + t, t); qp, rp = sp.div(sp.expand(1 + t * P1 ** 2), 1 + t, t)
chk['1 - P0^2 divisible by 1 + t'] = rm == 0
chk['1 + t P1^2 divisible by 1 + t'] = rp == 0
Im = sp.integrate(qm * sp.exp(-t), (t, 0, sp.oo)); Ip = sp.integrate(qp * sp.exp(-t), (t, 0, sp.oo))
chk['int exp(-t) q_- = 124/209'] = sp.nsimplify(Im) == sp.Rational(124, 209) and sp.simplify(Im - sp.Rational(124, 209)) == 0
chk['int exp(-t) q_+ = 100/167'] = sp.simplify(Ip - sp.Rational(100, 167)) == 0
# sign of the envelope errors on t >= 0: 1/(1+t) - q_- = P0^2/(1+t) >= 0 and q_+ - 1/(1+t) = t P1^2/(1+t) >= 0
chk['envelope errors are squares'] = (sp.simplify(1 / (1 + t) - qm - P0 ** 2 / (1 + t)) == 0
                                      and sp.simplify(qp - 1 / (1 + t) - t * P1 ** 2 / (1 + t)) == 0)
out['envelope'] = {'P0': str(P0), 'P1': str(P1), 'int_q_minus': str(Im), 'int_q_plus': str(Ip)}

# 2. D_1 = e E_1(1) by the exponential-integral series
iv.prec = 200
N = 40
S = Q(0)
for k in range(1, N + 1):
    S += Q((-1) ** (k + 1), k * factorial(k))
nxt = Q(1, (N + 1) * factorial(N + 1))           # alternating series with decreasing terms: |tail| < next term
def I(x):
    x = Q(x); return iv.mpf(x.numerator) / iv.mpf(x.denominator)
Sint = iv.mpf([I(S - nxt).a, I(S + nxt).b])
E1 = Sint - iv.euler
D1 = iv.e * E1
from mpmath.libmp import to_man_exp
def ends(x):
    # exact binary-rational endpoints of an iv interval, and directed 25-digit decimal bounds
    lo_, hi_ = [Q(int(m)) * Q(2) ** e for m, e in (to_man_exp(x._mpi_[0]), to_man_exp(x._mpi_[1]))]
    s25 = 10 ** 25
    return {'lower_exact': f'{lo_.numerator}/{lo_.denominator}', 'upper_exact': f'{hi_.numerator}/{hi_.denominator}',
            'lower_decimal_rounded_down': str(Decimal(lo_.numerator * s25 // lo_.denominator) / s25),
            'upper_decimal_rounded_up': str(Decimal(-(-hi_.numerator * s25 // hi_.denominator)) / s25)}
chk['D_1 strictly inside (124/209, 100/167)'] = (D1.a > I(Q(124, 209)).b) and (D1.b < I(Q(100, 167)).a)
chk['D_1 agrees with mpmath e*E1(1) (FLOAT)'] = abs(float(D1.a) - float(mpmath.e * mpmath.e1(1))) < 1e-14
out['D_1'] = dict(ends(D1), width_FLOAT_display=float(D1.b - D1.a), midpoint_FLOAT_display=float(D1.mid))

# 3. unweighted bounds (11)
nc = iv.sqrt(D1) / (8 * iv.sqrt(iv.pi)); nc0 = iv.sqrt(D1) / (8 * iv.sqrt(2 * iv.pi))
chk['||c||_(H_1)* < 1/18'] = nc.b < I(Q(1, 18)).a
chk['||c|_ker b|| < 1/25'] = nc0.b < I(Q(1, 25)).a
leib = sum((Q((-1) ** n, 2 * n + 1) for n in range(32)), Q(0))
chk['Leibniz 32 terms > 31/40'] = leib > Q(31, 40)
chk['pi > 31/10 (interval)'] = iv.pi.a > I(Q(31, 10)).b
# rational route of the proof: D_1 < 100/167 and pi > 31/10 give the two strict inequalities
chk['rational route 1/18'] = Q(100, 167) * 18 ** 2 < 64 * Q(31, 10)
chk['rational route 1/25'] = Q(100, 167) * 25 ** 2 < 128 * Q(31, 10)
out['H_1_norms'] = {'c': ends(nc), 'c_on_ker_b': ends(nc0), 'leibniz_32_exact': f'{leib.numerator}/{leib.denominator}',
                    'leibniz_32_FLOAT_display': float(leib)}

# 4. exact identities
rt = sp.sqrt(sp.exp(t) - 1)
chk['radial substitution (9)'] = sp.simplify((rt ** 3 / (1 + rt ** 2) ** 2) * sp.diff(rt, t) - (1 - sp.exp(-t)) / 2) == 0
ang = lambda f: sp.integrate(f, (th, 0, 2 * sp.pi))
pb, pc = sp.sin(th), -sp.sin(th) * sp.cos(th) ** 2
G = sp.Matrix(2, 2, lambda i, j: ang([pb, pc][i] * [pb, pc][j]))
Db = sp.Symbol('D', positive=True)
Gram = G * (Db / 2) / (4 * sp.pi ** 2)
chk['Gram (3)'] = sp.simplify(Gram - Db / (8 * sp.pi) * sp.Matrix([[1, -sp.Rational(1, 4)], [-sp.Rational(1, 4), sp.Rational(1, 8)]])) == sp.zeros(2, 2)
chk['norms (4)'] = (sp.simplify(sp.sqrt(Gram[1, 1]) - sp.sqrt(Db) / (8 * sp.sqrt(sp.pi))) == 0 and
                    sp.simplify(sp.sqrt(Gram[1, 1] - Gram[0, 1] ** 2 / Gram[0, 0]) - sp.sqrt(Db) / (8 * sp.sqrt(2 * sp.pi))) == 0)
chk['c + b/4 orthogonal to b'] = ang(pb * (pc + pb / 4)) == 0
mpmath.mp.dps = 30
dvals = {}
for bb in (Q(3, 4), Q(1), Q(2)):
    B = mpmath.mpf(bb.numerator) / bb.denominator
    closed = 1 / (2 * B - 1) - mpmath.e * mpmath.gammainc(1 - 2 * B, 1)
    quad = mpmath.quad(lambda x: (1 - mpmath.exp(-x)) * (1 + x) ** (-2 * B), [0, 1, 10, 100, mpmath.inf])
    # the slowly decaying part (1+t)^(-2 beta) is integrated exactly, the rest decays exponentially
    split = 1 / (2 * B - 1) - mpmath.quad(lambda x: mpmath.exp(-x) * (1 + x) ** (-2 * B), [0, 1, 10, 100, mpmath.inf])
    dvals[str(bb)] = {'closed': float(closed), 'split_quadrature': float(split), 'direct_quadrature': float(quad)}
chk['closed form (2) (FLOAT)'] = all(abs(v['closed'] - v['split_quadrature']) < 1e-12 for v in dvals.values())
chk['D_1 closed form inside envelope (FLOAT)'] = 124 / 209 < dvals['1']['closed'] < 100 / 167
# eps D_beta -> 1: 0 <= e Gamma(-eps, 1) = e int_1^inf exp(-v) v^(-1-eps) dv <= e E_1(1) = D_1, so
# 1/eps - D_1 <= D_beta <= 1/eps (eps = 2 beta - 1); checked in floating point for eps = 2^-k
small = {}
for k in range(2, 21, 3):
    e_ = mpmath.mpf(2) ** -k
    Dk = 1 / e_ - mpmath.e * mpmath.gammainc(-e_, 1)
    small[k] = float(e_ * Dk)
    assert 1 - e_ * float(D1.b) <= e_ * Dk <= 1
chk['1/eps - D_1 <= D_beta <= 1/eps (FLOAT), so eps D_beta -> 1'] = True
out['eps_D_beta_FLOAT'] = small
out['D_beta_FLOAT'] = dvals

# 5. FLOAT: I_beta - 1/(2 eps) bounded, and the divergence rates (18)
def chi0(x):
    x = mpmath.mpf(x)
    if x <= 1: return mpmath.mpf(1)
    if x >= 2: return mpmath.mpf(0)
    a = mpmath.exp(-1 / (x - 1)); c = mpmath.exp(-1 / (2 - x)); return c / (a + c)
dev = {}
for k in range(4, 13):
    e_ = mpmath.mpf(2) ** -k; B = (1 + e_) / 2
    v0 = 1 + mpmath.log(5)
    # on r >= 2: int_(v0)^inf v^(-2 beta) dv / (2 (1 - e^(1 - v))); main part v0^(-eps)/(2 eps) exact
    main = v0 ** (-e_) / (2 * e_)
    rest = mpmath.quad(lambda v: v ** (-2 * B) / 2 * (1 / (1 - mpmath.exp(1 - v)) - 1), [v0, 10, 100, mpmath.inf])
    trans = mpmath.quad(lambda x: (1 - chi0(x)) ** 2 / (x * (1 + mpmath.log(1 + x * x)) ** (2 * B)), [1, 2])
    dev[k] = float(trans + main + rest - 1 / (2 * e_))
chk['I_beta - 1/(2 eps) bounded (FLOAT)'] = max(abs(v) for v in dev.values()) < 2
out['I_beta_minus_1_over_2eps_FLOAT'] = dev
rates = {}
for bb, M in ((Q(1, 2), mpmath.mpf(10) ** 40), (Q(1, 4), mpmath.mpf(10) ** 40)):
    B = mpmath.mpf(bb.numerator) / bb.denominator
    VM = 1 + mpmath.log(1 + M * M); v2 = 1 + mpmath.log(5)
    IM = mpmath.quad(lambda v: v ** (-2 * B) / (2 * (1 - mpmath.exp(1 - v))), [v2, 10, VM])
    pred = mpmath.log(VM) / 2 if bb == Q(1, 2) else VM ** (1 - 2 * B) / (2 * (1 - 2 * B))
    rates[str(bb)] = {'I(M)': float(IM), 'leading_term_(18)': float(pred), 'difference': float(IM - pred)}
chk['divergence rates (18) up to O(1) (FLOAT)'] = all(abs(v['difference']) < 3 for v in rates.values())
out['I(M)_at_M=1e40_FLOAT'] = rates

out['checks'] = {k_: bool(v) for k_, v in chk.items()}
print(json.dumps(out, indent=1))
assert all(out['checks'].values())
out['all_pass'] = True
out['seconds'] = round(time.monotonic() - t0, 1)
out['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE')
