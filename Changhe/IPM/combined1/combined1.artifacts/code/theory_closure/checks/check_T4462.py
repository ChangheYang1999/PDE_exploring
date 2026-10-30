# R1-047 (REVIEWS_v45): reciprocal review of the exact weight elimination of c1-t4 T4-462
# (research/weight_uniform_gram_audit/PROOF.md, sha256 3c871d7f...2f3030c), written from the PROOF text only;
# no c1-t4 or c1-t2 code is run. Checks, exactly (sympy) unless stated:
#  (A) the determinant formula (4) of the 3x3 matrix G(mu) of (1), the numerator identity (5) after w1 = (z+E)/(p a),
#      the AM-GM step to (6) and its equality point, and the sign facts p, q, z, c > 0 under positive semidefiniteness;
#  (B) the s-elimination (7) to (8): sup over s > 0 of s (mu - C s)^2 is 4 mu^3/(27 C);
#  (C) the constants K and v of (10), (11) against the lower values 39068/100 and 15871/10000 (mpmath interval
#      arithmetic at 200 bits);
#  (D) for each of the seven rows of the PROOF, the degree-7 polynomial Q_b of (9) has no root on [0, m2] and is positive
#      there (Sturm root count, exact), so ||h||_2 < b; the supremum of the bound (8) over mu (FLOAT, mpmath) is printed
#      to show how close b is; the gains over the sharpw and TB-sharp ceilings and the 007 factors are exact rational
#      comparisons with the printed displays;
#  (E) the beta monotonicity used in the bL extension.
# Usage: python3 check_T4462.py (from artifacts/checks). No input files.
import sympy as sp
from fractions import Fraction as Fr
from mpmath import iv, mp, mpf
n_ok = 0


def ok(cond, msg):
    global n_ok
    assert cond, msg
    n_ok += 1


# ---- (A) exact algebra
# p = m2 - mu, a = m1 - mu, c = beta - mu are independent positive symbols here (identities in p, a, c)
mu, w1, w2, z, beta, O = sp.symbols('mu w1 w2 z beta O', positive=True)
p, a, c = sp.symbols('p a c', positive=True)
G = sp.Matrix([[p, -O, -5], [-O, w1 * a - 40, -3 * w1], [-5, -3 * w1, w2 * c]])
E = 40 * p + O**2
zz = p * a * w1 - E
det4 = w2 * c * zz - (9 * p * w1**2 + (30 * O + 25 * a) * w1 - 1000)
ok(sp.expand(G.det() - det4) == 0, 'determinant formula (4)')
bracket = 9 * p * w1**2 + (30 * O + 25 * a) * w1 - 1000
num = sp.cancel(sp.expand((bracket * p * a**2).subs(w1, (z + E) / (p * a))))
S = 3 * E + 5 * O * a
ok(sp.expand(num - (9 * z**2 + (18 * E + 30 * O * a + 25 * a**2) * z + S**2)) == 0, 'numerator identity (5)')
Oval = sp.Rational(347, 10)
ok(30 * Oval == 1041, 'cross coefficient 30 O = 1041')
# AM-GM: 9z + S^2/z - 6S = (3z - S)^2/z >= 0, equality at z = S/3; then w2 >= [ (6S + 18E + 30Oa + 25a^2) ]/(c p a^2)
ok(sp.expand((9 * z + S**2 / z - 6 * S) * z - (3 * z - S)**2) == 0, 'AM-GM identity')
W6 = (1440 * p + (6 * O + 5 * a)**2) / (c * p * a**2)
ok(sp.simplify((6 * S + 18 * E + 30 * O * a + 25 * a**2) - (1440 * p + (6 * O + 5 * a)**2)) == 0,
   '6S + 18E + 30 O a + 25 a^2 = 1440 p + (6O + 5a)^2')
# det >= 0 with z > 0 gives w2 c z p a^2 >= num = 9z^2 + B z + S^2, i.e. w2 >= (9z + B + S^2/z)/(c p a^2) >= W6
# equality point: z = S/3, w1 = (z + E)/(p a) = (2E + 5 O a/3)/(p a)?  (S/3 + E = 2E + 5Oa/3)
ok(sp.expand(S / 3 + E - (2 * E + 5 * O * a / 3)) == 0, 'equality point w1 = (2E + 5Oa/3)/(pa)')
B = 18 * E + 30 * O * a + 25 * a**2
at_eq = sp.simplify((9 * z + B + S**2 / z).subs(z, S / 3) - (6 * S + B))
ok(at_eq == 0, 'equality value at z = S/3')
# at the equality point det G = 0 with the leading 2x2 block positive definite: check det = 0 symbolically
w1e = (2 * E + 5 * O * a / 3) / (p * a)
ok(sp.cancel(sp.together(det4.subs({w1: w1e, w2: W6}))) == 0, 'det G = 0 at the equality point')
# leading 2x2 minor p q - O^2 = z with q = a w1 - 40
ok(sp.expand(p * (a * w1 - 40) - O**2 - zz) == 0, 'p q - O^2 = z')
# if p q = O^2 (z = 0), det = -(9 p w1^2 + 30 O w1 + 25 q) after using 25 a w1 - 1000 = 25 q
q = a * w1 - 40
ok(sp.expand((det4 - w2 * c * zz) + (9 * p * w1**2 + 30 * O * w1 + 25 * q)) == 0,
   'z = 0 gives det = -(9 p w1^2 + 30 O w1 + 25 q) < 0')
print('(A) determinant, numerator identity, AM-GM step, equality point: exact')

# ---- (B) s-elimination: f(t) = t (mu - C t^2) with t = sqrt(s); max at t^2 = mu/(3C); f_max^2 = 4 mu^3/(27 C)
t, C = sp.symbols('t C', positive=True)
f = t * (mu - C * t**2)
tm = sp.sqrt(mu / (3 * C))
ok(sp.simplify(sp.diff(f, t).subs(t, tm)) == 0, 'critical point t^2 = mu/(3C)')
ok(sp.simplify(f.subs(t, tm)**2 - 4 * mu**3 / (27 * C)) == 0, 'f_max^2 = 4 mu^3/(27 C)')
ok(sp.simplify(sp.diff(f, t, 2) + 6 * C * t) == 0, 'f is concave on t > 0 (f\'\' = -6 C t), so the critical point is the maximum')
print('(B) sup over s of s (mu - C s)^2 = 4 mu^3/(27 C): exact')

# ---- (C) constants with interval arithmetic
iv.prec = 200
sig = iv.mpf(1) / 1024
pi = iv.pi
M = iv.sqrt(pi) * iv.gamma((1 - sig) / 2) / 2
W = 8 * iv.sqrt(5) * iv.exp(-iv.mpf(3) / 5 * iv.log(6)) / 5
k1 = M + iv.mpf(8) / 5
cr = 3 * M / 2 + iv.mpf(32) / 15
c8 = 1 + 3 * pi * W / 4
dtop = 1 + pi * W / 2
K = 2 * dtop + 6 * c8 + 24 * (cr + 2 * k1) + 32 * k1
q0 = 1 / (2 * iv.sqrt(pi))
ps = iv.exp(sig * iv.log(2)) * iv.sqrt(1 + sig) / (2 * iv.sqrt(pi))
P0 = ps * (1 + W * M * sig) + W * M * sig / (2 * iv.sqrt(pi))
v = iv.mpf(4) / 5 * q0 + q0 * (1 + 4 * W * M * sig) + iv.mpf(19) / 5 * P0
ok(K.a > iv.mpf(39068) / 100, 'K > 39068/100')
ok(v.a > iv.mpf(15871) / 10000, 'v > 15871/10000')
print('(C) K =', iv.nstr(K, 15), '; v =', iv.nstr(v, 15), '(interval enclosures)')

# ---- (D) rows: Q_b(mu) = 27 k u^2 b^2 (1440 p + (6O + 5a)^2) - 4 mu^3 c p a^2 > 0 on [0, m2]
R = sp.Rational
k, u = R(39068, 100), R(15871, 10000)
d007 = sp.Rational(4769166867, 10**12)
H18min = sp.Rational(1232449584, 10**12)
# exact registered family ceilings b_fam^2 = 4 mu0^3/(27 C cU^2 W2) (registered tuples: sharpw mu0 = 97/250, C = 397,
# cU = 8/5, sqrt(W2) = 1024; TB-sharp mu0 = 297/1000, C = 402, cU = 8/5, sqrt(W2) = 512)
ceil2 = {'sharpw': 4 * R(97, 250)**3 / (27 * 397 * R(8, 5)**2 * 1024**2),
         'TB-sharp': 4 * R(297, 1000)**3 / (27 * 402 * R(8, 5)**2 * 512**2)}
ok(R(28495, 10**10)**2 < ceil2['sharpw'] < R(28496, 10**10)**2, 'sharpw ceiling in (2.8495e-6, 2.8496e-6)')
ok(R(37929, 10**10)**2 < ceil2['TB-sharp'] < R(37930, 10**10)**2, 'TB-sharp ceiling in (3.7929e-6, 3.7930e-6)')
rows = [('R3', R(1, 2), R(9, 10), R(2), R(33469, 10**10), 'sharpw', '1.1746', '1424.9'),
        ('TB', R(1, 2), R(9, 10), R(11, 4), R(40249, 10**10), 'TB-sharp', '1.0612', '1184.9'),
        ('hyp_R3_2', R(61151, 10**5), R(99116, 10**5), R(2), R(50757, 10**10), 'sharpw', '1.7813', '939.6'),
        ('hyp_TB', R(61151, 10**5), R(99116, 10**5), R(11, 4), R(61373, 10**10), 'TB-sharp', '1.6181', '777.0'),
        ('hyp_R3_4', R(61151, 10**5), R(99116, 10**5), R(4), R(37927, 5 * 10**9), 'sharpw', '2.6620', '628.7'),
        ('bL_c0', R(1, 2), R(9, 10), R(6328276273924429, 2251799813685248), R(20373, 5 * 10**9), 'sharpw', '1.4299',
         '1170.4'),
        ('bL_all_A', R(1, 2), R(9, 10), R(57, 20), R(41069, 10**10), 'sharpw', '1.4413', '1161.2')]
x = sp.symbols('x')
mp.prec = 120
for (lab, M2, M1, BE, b, fam, gain, fac) in rows:
    P_, A_, C_ = M2 - x, M1 - x, BE - x
    Q = sp.Poly(sp.expand(27 * k * u**2 * b**2 * (1440 * P_ + (6 * Oval + 5 * A_)**2) - 4 * x**3 * C_ * P_ * A_**2), x)
    ok(Q.degree() == 7, 'degree 7')
    ok(Q.count_roots(0, M2) == 0 and Q.eval(0) > 0, '%s: Q_b > 0 on [0, m2]' % lab)
    # FLOAT: supremum of the bound (8)
    g = lambda m: mp.sqrt(4 * m**3 * (mpf(BE.p) / BE.q - m) * (mpf(M2.p) / M2.q - m) * (mpf(M1.p) / M1.q - m)**2 /
                          (27 * mpf(k.p) / k.q * (mpf(u.p) / u.q)**2 *
                           (1440 * (mpf(M2.p) / M2.q - m) + (6 * mpf(347) / 10 + 5 * (mpf(M1.p) / M1.q - m))**2)))
    best = max(g(mpf(M2.p) / M2.q * i / 20000) for i in range(1, 20000))
    # displayed gain and 007 factor: gain is an upper factor b/ceiling <= gain + 1e-4 rounding up; factor is a lower one
    gu, fl = Fr(gain), Fr(fac)
    ok(b**2 / ceil2[fam] <= R(gu.numerator, gu.denominator)**2, '%s: gain upper display (exact ceiling)' % lab)
    ok(Fr(int(d007.p), int(d007.q)) / Fr(int(b.p), int(b.q)) > fl, '%s: 007 factor lower display' % lab)
    print('(D) %-9s b = %s; sup of (8) over mu (FLOAT) = %s; b/sup = %s; gain <= %s; 007 factor > %s; '
          'H18 factor > %s' % (lab, mp.nstr(mpf(b.p) / b.q, 6), mp.nstr(best, 8), mp.nstr((mpf(b.p) / b.q) / best, 8),
                               gain, fac, mp.nstr(mpf(H18min.p) / H18min.q / (mpf(b.p) / b.q), 6)))
ok(H18min / R(41069, 10**10) > 300 and H18min / R(20373, 5 * 10**9) > R(3024, 10), 'H18 factors 300.0 and 302.4')

# ---- (E) beta monotonicity: G(beta_new) - G(beta_old) = w2 (beta_new - beta_old) e3 e3^T, PSD for w2 >= 0
b2 = sp.symbols('b2', positive=True)
Gb = G.subs(c, beta - mu)
D = sp.simplify(Gb.subs(beta, b2) - Gb)
ok(D == sp.Matrix([[0, 0, 0], [0, 0, 0], [0, 0, w2 * (b2 - beta)]]), 'beta enters only G33 = w2 (beta - mu)')
ok(R(6328276273924429, 2251799813685248) == 1 + R(4076476460239181, 2251799813685248) and 1 + R(37, 20) == R(57, 20),
   '1 + c0 and 1 + 37/20 = 57/20')
print('checks passed', n_ok)
print('RESULT PASS')
