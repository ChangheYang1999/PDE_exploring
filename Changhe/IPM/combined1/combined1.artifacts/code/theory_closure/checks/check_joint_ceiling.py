# c1-t1 R1-019: check of the c1-t2 joint ceiling (REVIEW_T4_146.md remark R1). Both actual-inverse floors hold for the
# same M: M >= 1/(c - 1 - s) (T4-146 (4), s < c - 1) and M >= 1/beta_inf(a) (T4-097). With :H6 this gives
#   Y(F) < beta_inf/(1 + a) * J(a),  J(a) = sup_(0 < s < c - 1) min(c - 1 - s, beta_inf) sqrt(4 pi s(1 + s)).
# Part 1 (exact, sympy): the case analysis of J. Part 2 (mpmath iv, 60 digits): switch point, directed table of the
# joint ceiling (rounded up), FLOAT ratios to the T4-097 ceiling sqrt(8 pi) beta_inf^2/(1 + a) and the a -> 1 + 1/c
# limit. Run from artifacts/checks: OMP_NUM_THREADS=1 python3 -B check_joint_ceiling.py > check_joint_ceiling.out
import math
import sympy as sp
from mpmath import mp, iv, mpf

ok = []
s, d, b = sp.symbols('s d b', positive=True)
g = sp.sqrt(4 * sp.pi * s * (1 + s))
# g increasing on s > 0; (d - s) g has derivative sign (d - s)(-4 s^2 + (2d - 3) s + d) (T4-146 (19)).
dg = sp.simplify(sp.diff(g ** 2, s))
ok.append(('g^2 increasing: d/ds g^2 = 4 pi (1 + 2 s)', sp.simplify(dg - 4 * sp.pi * (1 + 2 * s)) == 0))
ex = sp.expand(sp.diff((d - s) ** 2 * s * (1 + s), s) - (d - s) * (-4 * s ** 2 + (2 * d - 3) * s + d))
ok.append(('derivative identity of (d - s)^2 s (1 + s)', ex == 0))
# Case analysis. min(d - s, b) = b on (0, d - b] (if b < d) and d - s on [d - b, d). b g(s) increases on (0, d - b];
# (d - s) g(s) is unimodal on (0, d) with maximum at s*. So J = H(d) if d - b <= s*, else J = b g(d - b) (value at the
# junction, since (d - s) g decreases on [d - b, d) when d - b > s*). If b >= d, J = H(d).
ok.append(('junction continuity: (d - s) g = b g at s = d - b', sp.simplify(((d - s) * g - b * g).subs(s, d - b)) == 0))

mp.dps = 60
iv.dps = 60
C = iv.mpf(4076476460239181) / iv.mpf(2) ** 51
D = C - 1
sst = ((2 * D - 3) + iv.sqrt((2 * D - 3) ** 2 + 16 * D)) / 8
H = (D - sst) * iv.sqrt(4 * iv.pi * sst * (1 + sst))
asw = (1 + C - (D - sst)) / C  # beta_inf(a) = c - 1 - s*
print('switch beta_inf = c - 1 - s* = [%s, %s] at a = [%s, %s]' % (mp.nstr(mpf((D - sst).a), 12),
      mp.nstr(mpf((D - sst).b), 12), mp.nstr(mpf(asw.a), 12), mp.nstr(mpf(asw.b), 12)))
ok.append(('switch in (1.2757, 1.2758)', asw.a > mpf('1.2757') and asw.b < mpf('1.2758')))


def up(x, k=7):
    x = mpf(x.b)
    e = math.floor(math.log10(x)) - k + 1
    return mp.nstr(mp.ceil(x / mpf(10) ** e) * mpf(10) ** e, k + 2)


def joint(a):
    beta = 1 + C - C * a
    if (D - beta).b <= sst.a:      # d - b <= s*: J = H
        J = H
    elif (D - beta).a > sst.b:     # d - b > s*: J = b g(d - b)
        J = beta * iv.sqrt(4 * iv.pi * (D - beta) * (1 + D - beta))
    else:
        return None, None
    return beta * J / (1 + a), beta


print('a | joint Y ceiling (rounded up) | joint N_a ceiling 5^((2-a)/2) x joint (rounded up) | ratio to T4-097 (FLOAT)')
rat = {}
for num, den in [(0, 1), (1, 4), (1, 2), (3, 4), (4, 5), (1, 1), (6, 5), (5, 4), (13, 10), (7, 5), (3, 2),
                 (31, 20)]:
    a = iv.mpf(num) / den
    jc, beta = joint(a)
    bc = iv.sqrt(8 * iv.pi) * beta ** 2 / (1 + a)
    r = jc / bc
    rat[(num, den)] = mpf(r.a)
    print('%s/%s | %s | %s | %s' % (num, den, up(jc), up(iv.mpf(5) ** ((2 - a) / 2) * jc), mp.nstr(mpf(r.a), 6)))
ok.append(('c1-t2 FLOAT ratios 0.0802 (a=0), 0.2254 (a=1), 0.7834 (a=3/2), 0.8531 (a=31/20)',
           [round(float(rat[k]), 4) for k in [(0, 1), (1, 1), (3, 2), (31, 20)]] == [0.0802, 0.2254, 0.7834, 0.8531]))
lim = iv.sqrt(D * C / 2)
print('limit a -> 1 + 1/c of the ratio: sqrt((c - 1) c/2) = %s (FLOAT)' % mp.nstr(mpf(lim.a), 8))
ok.append(('limit 0.856', abs(float(mpf(lim.a)) - 0.856) < 5e-4))
for name, v in ok:
    print('%s: %s' % ('PASS' if v else 'FAIL', name))
print('%d of %d checks pass' % (sum(v for _, v in ok), len(ok)))
