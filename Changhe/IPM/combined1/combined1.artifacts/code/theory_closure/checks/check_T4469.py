# R1-049 (REVIEWS_v46): independent review of T4-469 (c1-t4 research/divergence_free_negative_norm_upper, PROOF sha256
# efabe956...377c2cbf, ERRATA_v01 sha256 45e743dd...10840037, TEAM_NOTE_v247), written from the PROOF and ERRATA texts
# only. No c1-t4 code is run. Domains and signs of the angular right inverse, the divergence-free correction and the
# residual identity H(F)^2 = 2p - d + H(g)^2.
# Part A, exact sympy: div A_F = F for A_F = -e_theta r f(r) cos(n theta)/n; the sign identity <A_F, grad psi> = -p
#   (angular integration by parts, no radial term); M2 = pi n^-2 int r^3 f^2 dr; orthogonality of Z for different n.
# Part B, exact sympy: the one-mode formulas (7) and (8) from (2) and (6) in polar form, for symbolic u, f and n;
#   the log-variable operator (9) u_y = r w^b D_b P for symbolic b and a generic cubic P; the measure change behind
#   (10) and (11) (r f u_yy dr = (1/2) t w^(e+b-3) A D_b^2 P dt), and the pole factor R0^2 + r^2 = (1 + 624 w)/w at R0 = 25.
# Part C, exact rationals and sympy integrals: the manufactured fixtures u_1 = r/(1+r^2)^(3/2) (n = 1) and
#   u_3 = r^3/(1+r^2)^3 (n = 3): d/pi, M2/pi, a/pi computed three ways (direct r integrals, formula (7) in y, formula (10)
#   with exact Beta moments), b = -a for F = -Delta psi, the two-mode value 153/280, the one-test upper 1457/2520 and its
#   gap 2/63; the residual identity at psi = psi_1 equals the t = 1 case of (3).
# Part D, mpmath quadrature at 40 digits (FLOAT, not interval): (10) and (11) against (7) and (8) for a two-group trial
#   (b = 3/4 and 13/10, k = -1 to 2) and a source with the positive pole (1 + 624 w)^(-3), modes 1 and 3.
# Part E, application to candidate 016 (exact rationals, then Arb balls): the trial energies a_n/pi of N4-398 for c1-n3's
#   exact vectors (modes 1 and 3) by a separate method (log-derivative operator on r^(3+2k) (1+r^2)^(-beta-k) and
#   rational Beta values in r), compared exactly with c1-n4's a_over_pi_exact; with N4-398's 4096-bit cross balls b_n:
#   a_n + b_n, the improvement floors, and (CONDITIONAL on c1-n3's 30-digit mode Hardy displays, not an accepted M2) the
#   difference M2_n - b_n^2/a_n - LB_n^2 of the T4-469 upper and the N4-396 lower in each tested mode.
# Usage: python3 check_T4469.py (from artifacts/checks). Inputs for Part E in data/: N3_016_hdual_m13deep.json,
#   N4398_mode_001.json, N4398_mode_003.json, N4398_result.json (copies of c1-n4
#   research/candidate016_solenoidal_upper/verification/{mode_001,mode_003,result}.json), sha256 checked.
import hashlib, json, os, sys, time
from fractions import Fraction as Fr
from math import factorial
import sympy as sp
import mpmath as mp
import flint

sys.set_int_max_str_digits(0)
t0 = time.time()
n_ok = 0


def ok(cond, msg):
    global n_ok
    assert cond, msg
    n_ok += 1


r, th, y, T = sp.symbols('r theta y t', positive=True)
n = sp.symbols('n', positive=True, integer=True)
f = sp.Function('f')
u = sp.Function('u')

# ---- Part A
# A_F in polar components (A_r, A_theta) = (0, -r f cos(n theta)/n); div = (1/r) d_r(r A_r) + (1/r) d_theta A_theta
Ath = -r * f(r) * sp.cos(n * th) / n
ok(sp.simplify(sp.diff(Ath, th) / r - f(r) * sp.sin(n * th)) == 0, 'div A_F = f sin(n theta)')
# <A_F, grad psi> on one circle: grad psi theta component is (1/r) d_theta psi; times r dtheta
psi = u(r) * sp.sin(n * th)
for nn in (1, 2, 3, 5):
    lhs = sp.integrate((Ath * sp.diff(psi, th) / r * r).subs(n, nn), (th, 0, 2 * sp.pi))
    pF = sp.integrate((f(r) * sp.sin(nn * th) * psi.subs(n, nn) * r), (th, 0, 2 * sp.pi))
    ok(sp.simplify(lhs + pF) == 0, '<A_F, grad psi> = -p on every circle, n=%d' % nn)
    m2 = sp.integrate((Ath.subs(n, nn)) ** 2 * r, (th, 0, 2 * sp.pi))
    ok(sp.simplify(m2 - sp.pi * r ** 3 * f(r) ** 2 / nn ** 2) == 0, 'M2 density pi n^-2 r^3 f^2, n=%d' % nn)
# Z = A_(Delta psi) - grad psi: radial part ~ sin(n theta), tangential part ~ cos(n theta); different n orthogonal
for (n1, n2) in [(1, 3), (1, 5), (3, 5), (2, 4)]:
    ok(sp.integrate(sp.sin(n1 * th) * sp.sin(n2 * th), (th, 0, 2 * sp.pi)) == 0 and
       sp.integrate(sp.cos(n1 * th) * sp.cos(n2 * th), (th, 0, 2 * sp.pi)) == 0, 'Z orthogonal %d %d' % (n1, n2))
print('Part A: div A_F = F, <A_F, grad psi> = -p with no radial term, M2 density, Z orthogonality;', n_ok, 'checks')

# ---- Part B
U, Up, Upp, Fv = sp.symbols('U Up Upp Fv')
nn = sp.symbols('nn', positive=True)
g = Upp + Up / r - nn ** 2 * U / r ** 2                      # radial part of Delta psi
# b = <A_F, A_(Delta psi)> + p (6): densities pi n^-2 r^3 f g + pi r f u; (8): pi n^-2 r f (r^2 u'' + r u')
ok(sp.expand(sp.pi / nn ** 2 * r ** 3 * Fv * g + sp.pi * r * Fv * U - sp.pi / nn ** 2 * r * Fv * (r ** 2 * Upp + r * Up))
   == 0, 'formula (8): p cancels exactly')
# (7): with v(y) = u(e^y): v' = r u', v'' = r^2 u'' + r u'; dr/r = dy
v = sp.Function('v')
vv = v(y)
V1, V2 = sp.diff(vv, y), sp.diff(vv, y, 2)
# ||A_(Delta psi)||^2/pi = n^-2 int (v'' - n^2 v)^2 dy, d/pi = int (v'^2 + n^2 v^2) dy; a = difference after
# int v v'' = -int v'^2 (v v' -> 0 at both ends)
Vs, V1s, V2s = sp.symbols('Vs V1s V2s')
lhs = sp.expand((V2s - nn ** 2 * Vs) ** 2 / nn ** 2 - (V1s ** 2 + nn ** 2 * Vs ** 2))
# replace the cross term -2 v v'' by +2 v'^2 (integration by parts)
lhs_ibp = lhs.coeff(Vs * V2s) * (-V1s ** 2) + (lhs - lhs.coeff(Vs * V2s) * Vs * V2s)
ok(sp.expand(lhs_ibp - (V2s ** 2 / nn ** 2 + V1s ** 2)) == 0, 'formula (7): a/pi = n^-2 int v^2 + int v^2')
# polar form of Delta psi radial part in y: r^2 g = v'' - n^2 v
uu = sp.Function('uu')
expr = r ** 2 * (sp.diff(uu(r), r, 2) + sp.diff(uu(r), r) / r) - (r ** 2 * sp.diff(uu(r), r, 2) + r * sp.diff(uu(r), r))
ok(sp.simplify(expr) == 0, 'r^2 (u_rr + u_r/r) = v_yy')
# (9): t = r^2/(1+r^2), w = 1 - t; u = r w^b P(t); u_y = r d/dr u
bsym = sp.symbols('b', positive=True)
c = sp.symbols('c0:4')
Pt = sum(c[i] * T ** (i + 1) for i in range(4)) + sp.Symbol('cm') * 1   # k = -1 gives the constant t^0 term
tr = r ** 2 / (1 + r ** 2)
ur = r * (1 - tr) ** bsym * Pt.subs(T, tr)


def Dop(P, b):
    return sp.expand((1 - 2 * b * T) * P + 2 * T * (1 - T) * sp.diff(P, T))


uy = r * sp.diff(ur, r)
ok(sp.simplify((uy - r * (1 - tr) ** bsym * Dop(Pt, bsym).subs(T, tr)) / (r * (1 - tr) ** bsym)) == 0, '(9) first')
uyy = r * sp.diff(uy, r)
ok(sp.simplify((uyy - r * (1 - tr) ** bsym * Dop(Dop(Pt, bsym), bsym).subs(T, tr)) / (r * (1 - tr) ** bsym)) == 0,
   '(9) second')
# measure: dt/dr = 2 r w^2, r^2 = t/w, dy = dt/(2 t w)
ok(sp.simplify(sp.diff(tr, r) - 2 * r * (1 - tr) ** 2) == 0, 'dt/dr = 2 r w^2')
ok(sp.simplify(r ** 2 - tr / (1 - tr)) == 0, 'r^2 = t/w')
# (11): r f_n u_yy dr with f_n = r w^e A(t), u_yy = r w^b D^2P: r^3 w^(e+b) A D^2P dr = (1/2) t w^(e+b-3) A D^2P dt
e = sp.symbols('e')
ok(sp.simplify(r ** 3 * (1 - tr) ** (e + bsym) / sp.diff(tr, r) - tr * (1 - tr) ** (e + bsym - 3) / 2) == 0,
   '(11) measure')
# (10): v'^2 dy = r^2 w^(b+c) Db Dc dt/(2 t w) = (1/2) w^(b+c-2) Db Dc dt
cs = sp.symbols('cs', positive=True)
ok(sp.simplify(r ** 2 * (1 - tr) ** (bsym + cs) / (2 * tr * (1 - tr)) - (1 - tr) ** (bsym + cs - 2) / 2) == 0,
   '(10) measure')
# pole factor of the legqs variables at R0 = 25: R0^2 + r^2 = (1 + 624 w)/w, positive on [0, 1]
ok(sp.simplify(625 + r ** 2 - (1 + 624 * (1 - tr)) / (1 - tr)) == 0, 'R0^2 + r^2 = (1 + 624 w)/w')
# r^2 Delta_n maps r^a (1+r^2)^(-s) (label (beta, k), a = 3+2k, s = beta+k) into labels (beta, k), (beta, k+1), (beta, k+2):
# r^2 Delta_n m(a, s) = (a^2 - n^2) m(a, s) - 4 s (a+1) m(a+2, s+1) + 4 s (s+1) m(a+4, s+2)
asym, ssym = sp.symbols('a s', positive=True)
mm = lambda A_, S_: r ** A_ * (1 + r ** 2) ** (-S_)
lhs = r ** 2 * (sp.diff(mm(asym, ssym), r, 2) + sp.diff(mm(asym, ssym), r) / r - nn ** 2 * mm(asym, ssym) / r ** 2)
rhs = ((asym ** 2 - nn ** 2) * mm(asym, ssym) - 4 * ssym * (asym + 1) * mm(asym + 2, ssym + 1)
       + 4 * ssym * (ssym + 1) * mm(asym + 4, ssym + 2))
ok(sp.simplify((lhs - rhs) / mm(asym, ssym)) == 0, 'r^2 Delta_n closure on labels (beta, k..k+2)')
print('Part B: (7), (8), (9), the (10) and (11) measures, the 1 + 624 w pole factor and the r^2 Delta_n label shift;',
      n_ok, 'checks')

# ---- Part C: manufactured fixtures, exact


def direct(uexpr, nv):
    up, upp = sp.diff(uexpr, r), sp.diff(uexpr, r, 2)
    d = sp.integrate(sp.simplify(r * up ** 2 + nv ** 2 * uexpr ** 2 / r), (r, 0, sp.oo))
    gg = upp + up / r - nv ** 2 * uexpr / r ** 2
    M2 = sp.integrate(sp.simplify(r ** 3 * gg ** 2 / nv ** 2), (r, 0, sp.oo))
    # (7) in y, written back in r: v' = r u', v'' = r^2 u'' + r u', dy = dr/r
    v1, v2 = r * up, r ** 2 * upp + r * up
    a7 = sp.integrate(sp.simplify((v2 ** 2 / nv ** 2 + v1 ** 2) / r), (r, 0, sp.oo))
    # (8) for F = -Delta psi: f = -gg
    b8 = sp.integrate(sp.simplify(r * (-gg) * v2 / nv ** 2), (r, 0, sp.oo))
    return [sp.nsimplify(z) for z in (d, M2, a7, b8)]


def beta_mom(j, q):
    # int_0^1 t^j (1-t)^q dt = j! / prod_(i=1)^(j+1) (q+i)
    den = Fr(1)
    for i in range(1, j + 2):
        den *= q + i
    return Fr(factorial(j)) / den


def D_t(P, b):
    # (1 - 2 b t) P + 2 t (1 - t) P' on dict {power: coef}
    R = {}

    def add(k, v):
        R[k] = R.get(k, 0) + v
    for k, v in P.items():
        add(k, v)
        add(k + 1, -2 * b * v)
        if k:
            add(k, 2 * k * v)
            add(k + 1, -2 * k * v)
    return {k: v for k, v in R.items() if v != 0}


def pmul(P, Q):
    R = {}
    for i, a in P.items():
        for j, b in Q.items():
            R[i + j] = R.get(i + j, 0) + a * b
    return R


def a_formula10(groups, nv):
    # groups: {b: P_b}; a/pi = (1/2) sum_(b,c) int w^(b+c-2) [D_b^2 P_b D_c^2 P_c / n^2 + D_b P_b D_c P_c] dt
    tot = Fr(0)
    for b, Pb in groups.items():
        for c_, Pc in groups.items():
            q = b + c_ - 2
            I1 = pmul(D_t(D_t(Pb, b), b), D_t(D_t(Pc, c_), c_))
            I2 = pmul(D_t(Pb, b), D_t(Pc, c_))
            tot += Fr(1, 2) * (sum(v * beta_mom(k, q) for k, v in I1.items()) / nv ** 2 +
                               sum(v * beta_mom(k, q) for k, v in I2.items()))
    return tot


fixtures = {1: (r / (1 + r ** 2) ** sp.Rational(3, 2), {Fr(3, 2): {0: Fr(1)}}),      # beta = 5/2, k = -1: P = t^0
            3: (r ** 3 / (1 + r ** 2) ** 3, {Fr(2): {1: Fr(1)}})}                     # beta = 3, k = 0: P = t
expect = {1: (Fr(3, 8), Fr(3, 4), Fr(3, 8)), 3: (Fr(6, 35), Fr(64, 315), Fr(2, 63))}
vals = {}
for nv, (ue, groups) in fixtures.items():
    d, M2, a7, b8 = direct(ue, nv)
    dE, ME, aE = expect[nv]
    ok(d == sp.Rational(dE.numerator, dE.denominator), 'd/pi fixture n=%d' % nv)
    ok(M2 == sp.Rational(ME.numerator, ME.denominator), 'M2/pi fixture n=%d' % nv)
    ok(sp.simplify(M2 - d - a7) == 0, 'a = M2 - d equals (7), n=%d' % nv)
    ok(a7 == sp.Rational(aE.numerator, aE.denominator), 'a/pi fixture n=%d' % nv)
    ok(a_formula10(groups, nv) == aE, '(10) with exact Beta moments, n=%d' % nv)
    ok(sp.simplify(b8 + a7) == 0, 'b = -a for F = -Delta psi, n=%d' % nv)
    ok(sp.simplify(M2 - b8 ** 2 / a7 - d) == 0, '(4) is exact for F = -Delta psi, n=%d' % nv)
    vals[nv] = (Fr(str(d)), Fr(str(M2)), Fr(str(a7)))
H2 = vals[1][0] + vals[3][0]
ok(H2 == Fr(153, 280), 'H^2/pi = 153/280 for F = -Delta(psi_1 + psi_3)')
one = vals[1][1] + vals[3][1] - vals[1][2]
ok(one == Fr(1457, 2520) and one - H2 == Fr(2, 63) == vals[3][2], 'one-test upper 1457/2520, gap 2/63 = a_3/pi')
# residual identity at psi = psi_1: g = F + Delta psi_1 = -Delta psi_3; 2p - d + M_g2 with p = d_1 (F has psi_1 part)
resid = 2 * vals[1][0] - vals[1][0] + vals[3][1]
ok(resid == one, 'H(F)^2 <= 2p - d + M_g2 equals the t = 1 value of (3) (M2 + 2b + a with b = -a_1)')
ok(vals[1][1] + vals[3][1] + 2 * (-vals[1][2]) + vals[1][2] == resid, 't = 1 of (3)')
# triangle comparison: 2p - d + M_g2 <= (sqrt(d) + sqrt(M_g2))^2, here with d = d_1 and M_g2 = M2_3
lhs_t = float(resid)
rhs_t = (float(vals[1][0]) ** 0.5 + float(vals[3][1]) ** 0.5) ** 2
ok(lhs_t < rhs_t, 'triangle upper is larger (FLOAT comparison of two exact rationals with a wide gap)')
print('Part C: fixtures d/pi = 3/8, 6/35; M2/pi = 3/4, 64/315; a/pi = 3/8, 2/63 three ways; b = -a; 153/280;'
      ' 1457/2520; gap 2/63; residual identity = t = 1 case;', n_ok, 'checks')
print('  residual-identity upper %s pi = %.6f pi, triangle upper %.6f pi, exact %s pi'
      % (resid, float(resid), rhs_t, H2))

# ---- Part D (FLOAT quadrature): (10), (11) against (7), (8) on a two-group trial and a positive-pole source
mp.mp.dps = 40
grp = {Fr(3, 4): {0: Fr(1), 1: Fr(-2, 3), 3: Fr(5, 7)}, Fr(13, 10): {0: Fr(-1, 2), 2: Fr(3), 3: Fr(1, 9)}}
delta_e = Fr(7, 5)                               # source exponent e = l delta/2 for one l


def u_of_r(R, groups, deriv=0):
    # u = r sum_b w^b P_b(t); deriv 0, 1 (u_y), 2 (u_yy) via the operator D_b (formula (9) is verified in Part B)
    t = R ** 2 / (1 + R ** 2)
    w = 1 - t
    s = mp.mpf(0)
    for b, P in groups.items():
        Q = P
        for _ in range(deriv):
            Q = D_t(Q, b)
        s += w ** (mp.mpf(b.numerator) / b.denominator) * sum(mp.mpf(v.numerator) / v.denominator * t ** k
                                                              for k, v in Q.items())
    return R * s


def A_src(t):
    w = 1 - t
    return (1 - 3 * t + 2 * t ** 3) / (1 + 624 * w) ** 3


for nv in (1, 3):
    # this trial needs 3 + 2k >= n with 3 + 2k - n even; for n = 3 drop the k = -1 (t^0) terms
    G = {b: {k: v for k, v in P.items() if nv == 1 or k >= 1} for b, P in grp.items()}
    if nv == 3:
        G = {b: P for b, P in G.items() if P}
    a10q = a_formula10(G, nv)
    a10 = mp.mpf(a10q.numerator) / a10q.denominator
    v1 = lambda yy: u_of_r(mp.e ** yy, G, 1)
    v2 = lambda yy: u_of_r(mp.e ** yy, G, 2)
    a7 = mp.quad(lambda yy: v2(yy) ** 2 / nv ** 2 + v1(yy) ** 2, [-mp.inf, -5, 0, 5, mp.inf])
    ok(abs(a7 / a10 - 1) < mp.mpf(10) ** -20, '(10) = (7) by quadrature, n=%d' % nv)
    # (8): b/pi = n^-2 int r f u_yy dr with f = r w^e A(t); (11): (1/(2 n^2)) sum_b int w^(e+b-3) t A D_b^2 P_b dt
    fr = lambda R: R * (1 / (1 + R ** 2)) ** (mp.mpf(delta_e.numerator) / delta_e.denominator) * A_src(R ** 2 / (1 + R ** 2))
    b8 = mp.quad(lambda R: R * fr(R) * u_of_r(R, G, 2), [0, 1, 10, 100, mp.inf]) / nv ** 2
    b11 = mp.mpf(0)
    for b, P in G.items():
        Q = D_t(D_t(P, b), b)
        ex = mp.mpf((delta_e + b - 3).numerator) / (delta_e + b - 3).denominator
        b11 += mp.quad(lambda t: (1 - t) ** ex * t * A_src(t) *
                       sum(mp.mpf(v.numerator) / v.denominator * t ** k for k, v in Q.items()), [0, 0.5, 0.99, 1])
    b11 = b11 / (2 * nv ** 2)
    ok(abs(b8 - b11) < mp.mpf(10) ** -20 * (abs(b8) + 1), '(11) = (8) by quadrature, n=%d' % nv)
    print('Part D (FLOAT): n=%d a/pi (10) exact %.15e, (7) quadrature %.15e (rel. diff %.1e); b/pi (8) %s, (11) %s'
          % (nv, float(a10), float(a7), float(abs(a7 / a10 - 1)), mp.nstr(b8, 20), mp.nstr(b11, 20)))

# ---- Part E: candidate 016, modes 1 and 3
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
HASH = {'N3_016_hdual_m13deep.json': 'a32a02e71da636635e3b1d6c3289d5dc478bd8a63cda07f06f8cae98e9a968e5',
        'N4398_mode_001.json': '53e2f9a049a97a7f85a6fcb692b272c16e048d0723a2518ee7e671065975634e',
        'N4398_mode_003.json': '2dff6601c75bdf39c6fd038ba57020ef1fd257ed5bcf9ce04a39066406eab40e',
        'N4398_result.json': 'e97891e271837201e3f4a0d18f96732825238604cbad65fc8b31923e36463603'}
J = {}
for fn, h in HASH.items():
    raw = open(os.path.join(D, fn), 'rb').read()
    ok(hashlib.sha256(raw).hexdigest() == h, 'hash ' + fn)
    J[fn] = json.loads(raw)
N3 = J['N3_016_hdual_m13deep.json']
R8 = J['N4398_result.json']
ok(N3['source_sha256'] == R8['raw_sha256'] and N3['id'] == R8['candidate'] == 'C1-N1-016-legqs25-quot013', 'same 016 raw')


def B_list(A_, z, m):
    # [B(A_, z), ..., B(A_+m, z)], B(N, z) = (N-1)!/(z (z+1) ... (z+N-1)); B(N+1, z) = B(N, z) N/(z+N)
    den = Fr(1)
    for i in range(A_):
        den *= z + i
    out = [Fr(factorial(A_ - 1)) / den]
    for N_ in range(A_, A_ + m):
        out.append(out[-1] * N_ / (z + N_))
    return out


def energies(nv, basis):
    # u = sum x m(a, s); v' = L u, v'' = L^2 u with L = r d/dr: L m(a, s) = a m(a, s) - 2 s m(a+2, s+1) and
    # L^2 m(a, s) = a^2 m0 - 4 s (a+1) m1 + 4 s (s+1) m2; int m(a+2j, s+j) m(a'+2j', s'+j') dy = B(A + j + j', z)/2 with
    # A = (a+a')/2 and z = beta + beta' - 3. Returns (d/pi, a/pi), a/pi = n^-2 int v''^2 dy + int v'^2 dy (formula (7)).
    dsum, asum = Fr(0), Fr(0)
    pre = []
    for (x_, b_, k_) in basis:
        a_, s_ = 3 + 2 * k_, b_ + k_
        pre.append((x_, b_, a_, [a_, -2 * s_], [a_ * a_, -4 * s_ * (a_ + 1), 4 * s_ * (s_ + 1)]))
    m_ = len(pre)
    for i in range(m_):
        xi, bi, ai, L1i, L2i = pre[i]
        for j in range(i, m_):
            xj, bj, aj, L1j, L2j = pre[j]
            Bs = B_list((ai + aj) // 2, bi + bj - 3, 4)
            v1 = sum(L1i[p] * L1j[q] * Bs[p + q] for p in range(2) for q in range(2))
            v2 = sum(L2i[p] * L2j[q] * Bs[p + q] for p in range(3) for q in range(3))
            w_ = (1 if i == j else 2) * xi * xj / 2
            dsum += w_ * (v1 + nv * nv * Bs[0])
            asum += w_ * (v2 / (nv * nv) + v1)
    return dsum, asum


flint.ctx.prec = 1200
PI = flint.arb.pi()
tot_impr = Fr(0)
for M in N3['modes']:
    nv = int(M['n'])
    basis = []
    for key, val in M['x_rational'].items():
        bs, ks = key.split(',')
        basis.append((Fr(val), Fr(bs), int(ks)))
    t1 = time.time()
    dq, aq = energies(nv, basis)
    rec = J['N4398_mode_%03d.json' % nv]
    ok(int(rec['n']) == nv and dq == Fr(M['grad_psi_sq_over_pi_exact']) == Fr(rec['old_d_over_pi_exact']),
       'd/pi equals c1-n3 and N4-398, n=%d' % nv)
    ok(aq > 0 and aq == Fr(rec['a_over_pi_exact']), 'a/pi equals N4-398 exactly, n=%d' % nv)
    A_ = flint.arb(flint.fmpq(aq.numerator, aq.denominator)) * PI
    bb = flint.arb(rec['b_ball'])
    q_ = bb * bb / A_
    ok(q_.overlaps(flint.arb(rec['b_squared_over_a_ball'])), 'b^2/a overlaps N4-398, n=%d' % nv)
    fl = Fr(rec['improvement_strict_lower_exact'])
    ok(flint.arb(flint.fmpq(fl.numerator, fl.denominator)) < q_, 'improvement floor below b^2/a, n=%d' % nv)
    tot_impr += fl
    apb = A_ + bb
    ok(apb > 0 and apb < flint.arb(10) ** -36, '0 < a + b < 1e-36, n=%d' % nv)
    # CONDITIONAL: c1-n3's mode Hardy display H_n_UB = ||r F_n||_2 / n (30 digits) as M2_n = H_n_UB^2
    M2n = flint.arb(M['H_n_UB_hardy']) ** 2
    LBn = flint.arb(M['LB'])
    gap = M2n - q_ - LBn * LBn
    ok(gap.overlaps(flint.arb(0)) and gap.rad() < flint.arb(10) ** -29, 'upper - lower contains 0, radius < 1e-29, n=%d' % nv)
    print('Part E: n=%d, a/pi = %.15e exactly equal to N4-398 (%.1f s); a + b = %s; optimal t = -b/a = 1 - %s'
          % (nv, float(aq), time.time() - t1, apb.str(6), (apb / A_).str(6)))
    print('  CONDITIONAL on the c1-n3 Hardy display: M2_n = %s, b^2/a = %s, LB_n^2 = %s, M2_n - b^2/a - LB_n^2 = %s'
          % (M2n.str(20), q_.str(20), (LBn * LBn).str(20), gap.str(5)))
ok(tot_impr == Fr(R8['improvement_sum_strict_lower_exact']), 'sum of the two floors equals the N4-398 sum floor')
# the stored c1-n3 complete Hardy value is a truncated string without radius; FLOAT display arithmetic only
Hup = float(N3['H_upper_hardy'].lstrip('[').split()[0][:20])
print('  FLOAT, CONDITIONAL on the c1-n3 complete Hardy display H_upper = %.12f (all modes): H(016)^2 <= %.8f,'
      ' H(016) <= %.8f; remaining gap above the N4-396 lower bound 0.52946958 comes from modes other than 1 and 3'
      % (Hup, Hup ** 2 - float(tot_impr), (Hup ** 2 - float(tot_impr)) ** 0.5))
print('checks passed', n_ok, '; elapsed %.1f s' % (time.time() - t0))
print('RESULT PASS')
