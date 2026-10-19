"""V202: independent exact checks of referee result 43 (quartic rigidity, exclusion of M = N in all
degrees, top-coefficient invariant for M = N-1). Written without reading the referee check scripts or their output.
Ansatz rho = sum f_j(y) x^j, psi = sum q_j(y) x^j; -Lap psi = rho_x, V.grad rho = rho, V = (l x - psi_y, l y + psi_x),
beta = 2l - 1/2. Each check prints its name and True/False. Heavy checks (concrete Step 3 descents, exact pole family for
Steps 8-11) are in v202b_res43_steps.py."""
import sympy as sp
from math import factorial
x, y, z, l, t = sp.symbols('x y z l t')
beta = 2 * l - sp.Rational(1, 2)
R = []
def ok(name, val):
    R.append(bool(val)); print('%-100s %s' % (name, bool(val)), flush=True)
def lap(f, X=x, Y=y):
    return sp.diff(f, X, 2) + sp.diff(f, Y, 2)
def transport(rho, psi):
    return sp.expand((l * x - sp.diff(psi, y)) * sp.diff(rho, x) + (l * y + sp.diff(psi, x)) * sp.diff(rho, y) - rho)
def poisson(rho, psi):
    return sp.expand(-lap(psi) - sp.diff(rho, x))
Dy = lambda e, k=1: sp.diff(e, y, k)
def layered(N, M, fn='f', qn='q'):
    fj = [sp.Function('%s%d' % (fn, j))(y) for j in range(N + 1)]; qj = [sp.Function('%s%d' % (qn, j))(y) for j in range(M + 1)]
    return fj, qj, sum(fj[j] * x**j for j in range(N + 1)), sum(qj[j] * x**j for j in range(M + 1))

# ---------------- Step 1 ----------------
good_T = good_P = True
for (N, M) in [(5, 6), (4, 3), (4, 4), (3, 2)]:
    fj, qj, rho, psi = layered(N, M)
    F_ = lambda j: fj[j] if 0 <= j <= N else 0
    Q_ = lambda j: qj[j] if 0 <= j <= M else 0
    T = sp.Poly(transport(rho, psi), x); P = sp.Poly(poisson(rho, psi), x)
    for d in range(0, N + M):
        form = (l * d - 1) * F_(d) + l * y * Dy(F_(d)) + sum(j * Q_(j) * Dy(F_(d + 1 - j)) - (d + 1 - j) * Dy(Q_(j)) * F_(d + 1 - j) for j in range(0, d + 2))
        good_T &= sp.expand(T.coeff_monomial(x**d) - form) == 0
    for j in range(0, max(N, M) + 1):
        good_P &= sp.expand(P.coeff_monomial(x**j) + (Dy(Q_(j), 2) + (j + 2) * (j + 1) * Q_(j + 2) + (j + 1) * F_(j + 1))) == 0
ok('S1 transport x^d: (ld-1)f_d + l y f_d\' + sum_(j+k=d+1)(j q_j f_k\' - k q_j\' f_k) [(N,M)=(5,6),(4,3),(4,4),(3,2)]', good_T)
ok('S1 Poisson: q_j\'\' + (j+2)(j+1)q_(j+2) = -(j+1)f_(j+1) [same cases]', good_P)
fj, qj, rho, psi = layered(5, 3)
ok('S1 M >= N-1: for (N,M)=(5,3) the x^4 Poisson coefficient is -5 f_5 (forces f_5 = 0)', sp.expand(sp.Poly(poisson(rho, psi), x).coeff_monomial(x**4) + 5 * fj[5]) == 0)
# general degree (N,M) = (5,6) in the named notation
fj, qj, rho, psi = layered(5, 6)
k_, g_, f_, h_, a_ = fj[0], fj[1], fj[2], fj[3], fj[4]
t_, m_, n_ = qj[0], qj[2], qj[3]; b_ = l * y + qj[1]; u_ = Dy(t_)
T = sp.Poly(transport(rho, psi), x); P = sp.Poly(poisson(rho, psi), x)
x0 = b_ * Dy(k_) - g_ * u_ - k_
x1 = 2 * m_ * Dy(k_) + b_ * Dy(g_) + (2 * l - Dy(b_) - 1) * g_ - 2 * f_ * u_
x2 = 3 * n_ * Dy(k_) + 2 * m_ * Dy(g_) - Dy(m_) * g_ + b_ * Dy(f_) + 2 * (beta - Dy(b_)) * f_ - 3 * h_ * u_
x3 = 4 * qj[4] * Dy(k_) + 3 * n_ * Dy(g_) - Dy(n_) * g_ + 2 * m_ * Dy(f_) - 2 * Dy(m_) * f_ + b_ * Dy(h_) + (6 * l - 3 * Dy(b_) - 1) * h_ - 4 * a_ * u_
ok('S1 constant eq b k\' - g u = k and linear eq 2m k\' + b g\' + (2l-b\'-1)g - 2f u = 0 (degree (5,6))',
   sp.expand(T.coeff_monomial(1) - x0) == 0 and sp.expand(T.coeff_monomial(x) - x1) == 0)
ok('S1 x^2 and x^3 coefficients in every degree (5,6): x^2 = 3nk\'+2mg\'-m\'g+bf\'+2(beta-b\')f-3hu, x^3 as used',
   sp.expand(T.coeff_monomial(x**2) - x2) == 0 and sp.expand(T.coeff_monomial(x**3) - x3) == 0)
ok('S1 Poisson j=0: u\' = -g - 2m (degree (5,6))', sp.expand(P.coeff_monomial(1) + (Dy(u_) + g_ + 2 * m_)) == 0)
ok('S1 W(0)=0 <=> b(0) = u(0) = 0: psi_x(0,0) = q_1(0) = b(0), psi_y(0,0) = q_0\'(0) = u(0)',
   sp.expand(sp.diff(psi, x).subs(x, 0) - (b_ - l * y)) == 0 and sp.expand(sp.diff(psi, y).subs(x, 0) - u_) == 0)
ok('S1 jet: rho(X,y) - rho(-X,y) = 2 sum_(odd j) f_j X^j (odd part used for g = O(y^2))',
   sp.expand(rho - rho.subs(x, -x) - 2 * (fj[1] * x + fj[3] * x**3 + fj[5] * x**5)) == 0)
# generic Taylor data obeying only the jet, W(0)=0 (for general degree); higher coefficients generic
sy = sp.symbols('k3 k4 g2 g3 f1 f2 h0 h1 a0 a1 n0 n1 n2 m0 m1 m2 b1 b2 b3 u1 u2 u3 p40 p41 p50 p60 c50')
k3, k4, g2, g3, f1, f2, h0, h1, a0, a1, n0, n1, n2, m0, m1, m2, b1, b2, b3, u1, u2, u3, p40, p41, p50, p60, c50 = sy
tay = {k_: k3 * y**3 + k4 * y**4, g_: g2 * y**2 + g3 * y**3, f_: 1 + f1 * y + f2 * y**2, h_: h0 + h1 * y, a_: a0 + a1 * y, fj[5]: c50,
       n_: n0 + n1 * y + n2 * y**2, m_: m0 + m1 * y + m2 * y**2, qj[1]: b1 * y + b2 * y**2 + b3 * y**3 - l * y,
       t_: u1 * y**2 / 2 + u2 * y**3 / 3 + u3 * y**4 / 4, qj[4]: p40 + p41 * y, qj[5]: p50, qj[6]: p60}
ev = lambda e: sp.expand(e.subs(tay).doit())
ok('S1 x^2 eq at y=0 equals 2(beta - b\'(0)) for generic data (so b\'(0) = beta)', sp.expand(ev(x2).subs(y, 0) - 2 * (beta - b1)) == 0)
ok('S1 k + g u has no y^0, y^1, y^2 terms (so b k\' = O(y^3), k\' = O(y^2))', all(sp.expand(ev(k_ + g_ * u_)).coeff(y, j) == 0 for j in range(3)))
lim1 = sp.expand(sp.cancel(ev(x1).subs(b1, beta) / y)).subs(y, 0)
ok('S1 (linear eq)/y at 0 with b\'(0)=beta equals -2u\'(0) (all other terms -> 0)', sp.expand(lim1 + 2 * u1) == 0)
ok('S1 u\'(0)=0 in u\' = -g - 2m at 0 gives q_2(0) = 0; q_1\'(0) = beta - l = l - 1/2',
   sp.solve(ev(Dy(u_) + g_ + 2 * m_).subs({y: 0, u1: 0}), m0) == [0] and sp.expand(beta - l - (l - sp.Rational(1, 2))) == 0)
x3at0 = ev(x3).subs({y: 0, m0: 0, b1: beta, u1: 0})
ok('S1 x^3 eq at 0 (generic n(0), q_4, a) is h(0)/2 - 2m\'(0), so m\'(0) = h(0)/4', sp.expand(x3at0 - (h0 / 2 - 2 * m1)) == 0)

# ---------------- Step 2 ----------------
good = True
for N in range(2, 7):
    fj, qj, rho, psi = layered(N, N)
    T = sp.Poly(transport(rho, psi), x); P = sp.Poly(poisson(rho, psi), x)
    good &= sp.expand(P.coeff_monomial(x**N) + Dy(qj[N], 2)) == 0
    good &= sp.expand(T.coeff_monomial(x**(2 * N - 1)) - N * (qj[N] * Dy(fj[N]) - Dy(qj[N]) * fj[N])) == 0 and T.degree() <= 2 * N - 1
ok('S2 M=N (N=2..6): top Poisson q_N\'\' = 0, top transport (x^(2N-1)) N(q_N f_N\' - q_N\' f_N) = 0', good)
qN, fN = sp.Function('qN')(y), sp.Function('fN')(y)
ok('S2 (f_N/q_N)\' = (q_N f_N\' - q_N\' f_N)/q_N^2', sp.simplify(Dy(fN / qN) - (qN * Dy(fN) - Dy(qN) * fN) / qN**2) == 0)
# R-equation, fully general (rho, psi arbitrary functions of x, y)
C = sp.Symbol('C')
PS, RF = sp.Function('PS')(x, y), sp.Function('RF')(x, y)
br = lambda F, G: sp.diff(F, x) * sp.diff(G, y) - sp.diff(F, y) * sp.diff(G, x)
Eu = lambda F: x * sp.diff(F, x) + y * sp.diff(F, y)
Req = lambda psi_, R_: br(psi_, R_) + C * (l * Eu(psi_) - psi_) + l * Eu(R_) - R_
ok('S3 transport(R + C psi, psi) = {psi,R} + C(l(x psi_x + y psi_y) - psi) + l(x R_x + y R_y) - R (general)', sp.expand(transport(RF + C * PS, PS) - Req(PS, RF)) == 0)
# layered versions: Poisson in R-form; top R coefficient x^(N+r-1)
good = good2 = True
for N in range(3, 7):
    for r in range(2, N):
        Rj = [sp.Function('R%d' % j)(y) for j in range(r + 1)]; qj = [sp.Function('q%d' % j)(y) for j in range(N + 1)]
        Rl = sum(Rj[j] * x**j for j in range(r + 1)); psi = sum(qj[j] * x**j for j in range(N + 1))
        E = sp.Poly(sp.expand(Req(psi, Rl).doit()), x)
        good &= E.degree() <= N + r - 1 and sp.expand(E.coeff_monomial(x**(N + r - 1)) - (N * qj[N] * Dy(Rj[r]) - r * Dy(qj[N]) * Rj[r])) == 0
        if N <= 4:
            P = sp.Poly(poisson(Rl + C * psi, psi), x)
            Q_ = lambda i: qj[i] if 0 <= i <= N else 0
            RR_ = lambda i: Rj[i] if 0 <= i <= r else 0
            good2 &= all(sp.expand(P.coeff_monomial(x**i) + Dy(Q_(i), 2) + (i + 1) * (C * Q_(i + 1) + RR_(i + 1)) + (i + 2) * (i + 1) * Q_(i + 2)) == 0 for i in range(N + 1))
ok('S2 top R coefficient x^(N+r-1) = N q_N R_r\' - r q_N\' R_r (N=3..6, r=2..N-1), above degree N', good)
ok('S3 Poisson in R form: q_i\'\' = -(i+1)(C q_(i+1) + R_(i+1)) - (i+2)(i+1) q_(i+2) (N=3,4)', good2)
f20, q20 = sp.symbols('f20 q20')
ok('S2 R_2(0) = f_2(0) - C q_2(0) = 1 (f_2(0)=1, q_2(0)=0 from Step 1), so r >= 2; impossible for N = 2 (r <= 1)', (f20 - C * q20).subs({f20: 1, q20: 0}) == 1)
# zero of affine q_N inside I: R_r = c |q_N|^(r/N); derivative exponent r/N - 1 < 0
Ny, ry, pp, y0, cA = sp.symbols('N r p y0 cA', positive=True)
Rr_side = cA * (pp * (y - y0))**(ry / Ny)
ok('S2 R_r = c (p(y-y0))^(r/N) solves N q_N R_r\' - r q_N\' R_r = 0; R_r\' ~ c (r/N) p^(r/N) (y-y0)^(r/N-1)',
   sp.simplify(Ny * pp * (y - y0) * Dy(Rr_side) - ry * pp * Rr_side) == 0
   and sp.simplify(Dy(Rr_side) - cA * ry / Ny * pp**(ry / Ny) * (y - y0)**(ry / Ny - 1)) == 0)
ok('S2 0 < r/N < 1 for 2 <= r <= N-1, so r/N - 1 < 0 (blow-up of R_r\' unless c = 0) [N = 3..40]',
   all(0 < sp.Rational(r, N) < 1 for N in range(3, 41) for r in range(2, N)))

# ---------------- Step 3 ----------------
s_, j_, r_, N_ = sp.symbols('s j r N', positive=True)
D_ = 2 * N_ + s_; d_ = D_ * r_ / N_
ok('S3 exponent identity d - 2j - s j/N = (r-j)(2 + s/N)', sp.simplify(d_ - 2 * j_ - s_ * j_ / N_ - (r_ - j_) * (2 + s_ / N_)) == 0)
ok('S3 d - 2r = s r/N (R_r = A z^(sr/N) is the j=r leading term)', sp.simplify(d_ - 2 * r_ - s_ * r_ / N_) == 0)
zp = sp.Symbol('zp', positive=True); pA, AA = sp.symbols('p A')
ok('S3 R_r = A z^(sr/N) solves N q_N R_r\' - r q_N\' R_r = 0 for q_N = p (s=0) and q_N = p z (s=1) [N=3..8]',
   all(sp.simplify(N * pA * zp**s * sp.diff(AA * zp**sp.Rational(s * r, N), zp) - r * pA * s * zp**(s - 1) * AA * zp**sp.Rational(s * r, N)) == 0
       for N in range(3, 9) for r in range(2, N) for s in (0, 1)))
ok('S3 d = (2N+s) r/N > 3 for N >= 3, 2 <= r <= N-1, s in {0,1} [N = 3..40] (d >= 2r >= 4)',
   all(sp.Rational((2 * N + s) * r, N) > 3 for N in range(3, 41) for r in range(2, N) for s in (0, 1)))
i_ = sp.Symbol('i')
ok('S3 bracket exponent: (D-2i) + (d-2k) - 1 = s + d - 2j - 1 when i + k = N + j',
   sp.simplify((D_ - 2 * i_) + (d_ - 2 * (N_ + j_ - i_)) - 1 - (s_ + d_ - 2 * j_ - 1)) == 0)
rj = sp.Symbol('rj')
ok('S3 Euler solve: N p z^s (r_j z^(d-2j))\' - j s p z^(s-1) r_j z^(d-2j) = p r_j N (r-j)(2+s/N) z^(s+d-2j-1) (s=0,1)',
   all(sp.simplify(N_ * pA * zp**s * sp.diff(rj * zp**(d_.subs(s_, s) - 2 * j_), zp) - j_ * s * pA * zp**(s - 1) * rj * zp**(d_.subs(s_, s) - 2 * j_)
                   - pA * rj * N_ * (r_ - j_) * (2 + sp.Integer(s) / N_) * zp**(s + d_.subs(s_, s) - 2 * j_ - 1)) == 0 for s in (0, 1)))
ok('S3 Poisson exponents: D-2(i+1) -> D-2i after two integrations; d-2i < D-2i; D-2i-2; and D - 2i >= 2+s > 1 for i <= N-1',
   sp.simplify((D_ - 2 * (i_ + 1)) + 2 - (D_ - 2 * i_)) == 0 and sp.simplify((D_ - 2 * i_) - (d_ - 2 * i_) - (2 * N_ + s_) * (N_ - r_) / N_) == 0
   and all(2 * N + s - 2 * i >= 2 + s for N in range(3, 30) for s in (0, 1) for i in range(0, N)))
ok('S3 lowest stream index i = N+j-r >= j+1 and forcing index i+1 >= j+2 when r <= N-1', sp.simplify((N_ + j_ - r_) - (j_ + 1) - (N_ - 1 - r_)) == 0)

# ---------------- Step 4 ----------------
def Qpoly(N, s, p=1, Cv=C):
    return sum(p * (-Cv)**j * sp.Rational(factorial(N) * factorial(s), factorial(N - j) * factorial(s + 2 * j)) * x**(N - j) * zp**(s + 2 * j) for j in range(N + 1))
good = goodE = goodODE = goodP0 = goodDisc = True
for N in range(2, 9):
    for s in (0, 1):
        D = 2 * N + s; Q = Qpoly(N, s, pA)
        good &= sp.expand(sp.diff(Q, zp, 2) + C * sp.diff(Q, x)) == 0 and sp.Poly(Q, x).LC() == pA * zp**s and sp.Poly(Q, x).degree() == N
        goodE &= sp.expand(2 * x * sp.diff(Q, x) + zp * sp.diff(Q, zp) - D * Q) == 0
        Pt = sp.expand(Q.subs({zp: 1, x: t}))
        goodODE &= sp.expand(4 * t**2 * sp.diff(Pt, t, 2) + (C - (4 * D - 6) * t) * sp.diff(Pt, t) + D * (D - 1) * Pt) == 0
        goodP0 &= sp.Poly(Pt, t).degree() == N and sp.expand(Pt.subs(t, 0) - pA * (-C)**N * sp.Rational(factorial(N) * factorial(s), factorial(2 * N + s))) == 0
        disc = sp.factor(sp.discriminant(sp.Poly(Pt.subs(pA, 1), t)))
        goodDisc &= sp.simplify(disc.subs(C, 1)) != 0 and sp.simplify(disc - disc.subs(C, 1) * C**(N * (N - 1))) == 0
        # uniqueness: recursion factor (D-2i)(D-2i-1) != 0 for i < N
        good &= all((D - 2 * i) * (D - 2 * i - 1) != 0 for i in range(N))
ok('S4 Q = p sum (-C)^j N! s!/((N-j)!(s+2j)!) x^(N-j) z^(s+2j): Q_zz = -C Q_x, top coeff p z^s, unique (N=2..8, s=0,1)', good)
ok('S4 Q weighted homogeneous: 2x Q_x + z Q_z = D Q (D = 2N+s)', goodE)
ok('S4 P(t)=Q(t,1): 4t^2 P\'\' + (C-(4D-6)t)P\' + D(D-1)P = 0 (N=2..8, s=0,1)', goodODE)
ok('S4 deg P = N and P(0) = p(-C)^N N! s!/(2N+s)! != 0', goodP0)
ok('S4 disc_t P = c C^(N(N-1)) with c != 0: P has only simple roots for every C != 0 (N=2..8, s=0,1)', goodDisc)
# general ODE derivation from weighted homogeneity
Ds = sp.Symbol('D'); Pf = sp.Function('Pf'); Sf = sp.Function('Sf'); ds = sp.Symbol('d')
Qg = zp**Ds * Pf(x / zp**2)
ode = lambda Pe, tt: 4 * tt**2 * sp.diff(Pe, tt, 2) + (C - (4 * Ds - 6) * tt) * sp.diff(Pe, tt) + Ds * (Ds - 1) * Pe
lhs = sp.diff(Qg, zp, 2) + C * sp.diff(Qg, x)
rhs = (zp**(Ds - 2) * ode(Pf(t), t)).doit().subs(t, x / zp**2)
ok('S4 Q = z^D P(x/z^2) (generic P): Q_zz + C Q_x = z^(D-2) [ODE](x/z^2)', sp.simplify((lhs - rhs).doit()) == 0)
# k-th derivative of the ODE: leading coefficient 4t^2 (simple-root argument)
Pg = sp.Function('Pg')(t)
good = True
for kk in range(0, 6):
    lhs = sp.diff(4 * t**2 * sp.diff(Pg, t, 2) + (C - (4 * Ds - 6) * t) * sp.diff(Pg, t) + Ds * (Ds - 1) * Pg, t, kk)
    rhs = 4 * t**2 * sp.diff(Pg, t, kk + 2) + (C + (8 * kk - 4 * Ds + 6) * t) * sp.diff(Pg, t, kk + 1) + (4 * kk * (kk - 1) - kk * (4 * Ds - 6) + Ds * (Ds - 1)) * sp.diff(Pg, t, kk)
    good &= sp.expand(lhs - rhs) == 0
ok('S4 k-th derivative of ODE = 4t^2 P^(k+2) + (C+(8k-4D+6)t)P^(k+1) + c_k P^(k) (k=0..5): t0 != 0 double root forces all P^(j)(t0)=0', good)
# weighted Euler identity for {Q,T}
Tg = zp**ds * Sf(x / zp**2)
brQT = sp.diff(Qg, x) * sp.diff(Tg, zp) - sp.diff(Qg, zp) * sp.diff(Tg, x)
eul = (zp**(Ds + ds - 3) * (Ds * Pf(t) * sp.diff(Sf(t), t) - ds * Sf(t) * sp.diff(Pf(t), t))).doit().subs(t, x / zp**2)
ok('S4 {Q,T}_(x,z) = -z^(D+d-3) (D P S\' - d S P\')(x/z^2) for Q = z^D P(x/z^2), T = z^d S(x/z^2)', sp.simplify((brQT + eul).doit()) == 0)
ok('S4 bracket weight D + d - 3 > D iff d > 3', sp.simplify((Ds + ds - 3) - Ds - (ds - 3)) == 0)
tau_ = sp.Symbol('tau'); c1, c2, c3, ck, ck1, ck2 = sp.symbols('c1 c2 c3 ck ck1 ck2')
good = True
for kk in range(0, 8):
    Ploc = c1 * tau_ + c2 * tau_**2 + c3 * tau_**3; Sloc = ck * tau_**kk + ck1 * tau_**(kk + 1) + ck2 * tau_**(kk + 2)
    expr = sp.Poly(sp.expand(Ds * Ploc * sp.diff(Sloc, tau_) - ds * Sloc * sp.diff(Ploc, tau_)), tau_)
    good &= min(mo[0] for mo in expr.monoms()) == kk and sp.expand(expr.coeff_monomial(tau_**kk) - c1 * ck * (Ds * kk - ds)) == 0
ok('S4 at a simple root (P = c1 tau + ...), S = ck tau^k + ... (k=0..7): lowest term of D P S\' - d S P\' is c1 ck (D k - d) tau^k', good)
ok('S4 D k = d gives k = d/D = r/N, not an integer for 2 <= r <= N-1', sp.simplify(d_ / D_ - r_ / N_) == 0)
# cross-check: {Q,T} = 0 with T = sum c_j x^j z^(d-2j) forces T = 0 (N=3..8, s=0,1, r=2..N-1), computed directly
good = True
for N in range(3, 9):
    for s in (0, 1):
        D = 2 * N + s; Q = Qpoly(N, s, 1, C)
        for r in range(2, N):
            d = sp.Rational(D * r, N); cs = sp.symbols('c0:%d' % (r + 1))
            T_ = sum(cs[j] * x**j * zp**(d - 2 * j) for j in range(r + 1))
            b = sp.expand(sp.diff(Q, x) * sp.diff(T_, zp) - sp.diff(Q, zp) * sp.diff(T_, x))
            b = sp.expand(sp.powsimp(b / zp**(D + d - 3)))
            eqs = [sp.expand(sp.powsimp(cf * zp**(2 * e))) for (e,), cf in sp.Poly(b, x).terms()]
            if any(e.has(zp) for e in eqs):
                good = False; continue
            sol = sp.solve(eqs, cs, dict=True)
            good &= len(sol) == 1 and all(sp.simplify(sol[0].get(c_, c_)) == 0 for c_ in cs)
ok('S4 cross-check: {Q,T}=0 with deg_x T = r, weight d = Dr/N has only T = 0 (N=3..8, s=0,1, r=2..N-1, C symbolic)', good)

# ---------------- Step 5 ----------------
a, h, f, g, k, n, m, bq, tq = [sp.Function(nm)(y) for nm in 'a h f g k n m bq tq'.split()]
b = bq; u = Dy(tq)
rho4 = a * x**4 + h * x**3 + f * x**2 + g * x + k; psi4 = n * x**3 + m * x**2 + (b - l * y) * x + tq
T4 = sp.Poly(transport(rho4, psi4), x); P4 = sp.Poly(poisson(rho4, psi4), x)
eqT = {6: 3 * n * Dy(a) - 4 * Dy(n) * a,
       5: 3 * n * Dy(h) - 3 * Dy(n) * h + 2 * m * Dy(a) - 4 * Dy(m) * a,
       4: 3 * n * Dy(f) - 2 * Dy(n) * f + 2 * m * Dy(h) - 3 * Dy(m) * h + b * Dy(a) + (8 * l - 4 * Dy(b) - 1) * a,
       3: 3 * n * Dy(g) - Dy(n) * g + 2 * m * Dy(f) - 2 * Dy(m) * f + b * Dy(h) + (6 * l - 3 * Dy(b) - 1) * h - 4 * a * u,
       2: 3 * n * Dy(k) + 2 * m * Dy(g) - Dy(m) * g + b * Dy(f) + 2 * (beta - Dy(b)) * f - 3 * h * u,
       1: 2 * m * Dy(k) + b * Dy(g) + (2 * l - Dy(b) - 1) * g - 2 * f * u,
       0: b * Dy(k) - g * u - k}
ok('S5 the seven transport equations T6..T0 (N=4, M=3) from the PDE', T4.degree() == 6 and all(sp.expand(T4.coeff_monomial(x**d) - eqT[d]) == 0 for d in range(7)))
eqP = {3: Dy(n, 2) + 4 * a, 2: Dy(m, 2) + 3 * h, 1: Dy(b, 2) + 2 * f + 6 * n, 0: Dy(u) + g + 2 * m}
ok('S5 Poisson n\'\' = -4a, m\'\' = -3h, b\'\' = -2f - 6n, u\' = -g - 2m', all(sp.expand(P4.coeff_monomial(x**j) + eqP[j]) == 0 for j in range(4)))
vv, ha1, aa1, ff1, nn2 = sp.symbols('v ha1 aa1 ff1 nn2')
tay5 = {n: vv * y + nn2 * y**2, a: a0 + aa1 * y, h: h0 + ha1 * y, m: h0 / 4 * y + m2 * y**2, f: 1 + ff1 * y,
        b: beta * y + b2 * y**2, tq: u2 * y**3 / 3, g: g2 * y**2, k: k3 * y**3}
ev5 = lambda e: sp.expand(e.subs(tay5).doit()).subs(y, 0)
ok('S5 [n(0)=0 sub-case] T6, T5, T4 at 0: -4 a0 v, -h0(3v + a0), a0 - 3h0^2/4 - 2v',
   sp.expand(ev5(eqT[6]) + 4 * a0 * vv) == 0 and sp.expand(ev5(eqT[5]) + h0 * (3 * vv + a0)) == 0
   and sp.expand(ev5(eqT[4]) - (a0 - 3 * h0**2 / 4 - 2 * vv)) == 0)
n0s = sp.Symbol('n00')
tay5b = dict(tay5); tay5b[n] = n0s + vv * y + nn2 * y**2
ok('S5 note: with n(0) = n00 != 0, T6 at 0 has the extra term 3 n00 a\'(0) (n(0)=0 is a hypothesis of the sub-case)',
   sp.expand(sp.expand(eqT[6].subs(tay5b).doit()).subs(y, 0) - (3 * n0s * aa1 - 4 * vv * a0)) == 0)
sols = sp.solve([a0 * vv, h0 * (3 * vv + a0), a0 - 3 * h0**2 / 4 - 2 * vv], [a0, h0, vv], dict=True)
ok('S5 {a0 v = 0, h0(3v+a0) = 0, a0 - 3h0^2/4 - 2v = 0} has only v = a0 = h0 = 0', sols == [{a0: 0, h0: 0, vv: 0}])
ok('S5 T6 with a = -n\'\'/4 is -(3n n\'\'\' - 4n\'n\'\')/4 and (3n n\'\' - 7n\'^2/2)\' = 3n n\'\'\' - 4n\'n\'\'',
   sp.expand(eqT[6].subs(a, -Dy(n, 2) / 4).doit() + (3 * n * Dy(n, 3) - 4 * Dy(n) * Dy(n, 2)) / 4) == 0
   and sp.expand(Dy(3 * n * Dy(n, 2) - 7 * Dy(n)**2 / 2) - (3 * n * Dy(n, 3) - 4 * Dy(n) * Dy(n, 2))) == 0)
npos = sp.Function('npos', positive=True)(y)
inv = 3 * npos * Dy(npos, 2) - 7 * Dy(npos)**2 / 2
ok('S5 (n^(-1/6))\'\' = -n^(-13/6)(3n n\'\' - 7n\'^2/2)/18 for n > 0 (and |n| for n < 0 since the invariant is even in n)',
   sp.simplify(Dy(npos**sp.Rational(-1, 6), 2) + npos**sp.Rational(-13, 6) * inv / 18) == 0
   and sp.expand(inv.subs(npos, -npos).doit() - inv) == 0)

# ---------------- Step 6 ----------------
Ac, Ec = sp.symbols('A E')
ap = sp.Function('ap')(y)
ok('S6 (a n^(-4/3))\' = n^(-7/3)(3n a\' - 4n\'a)/3 (n > 0)', sp.simplify(Dy(ap * npos**sp.Rational(-4, 3)) - npos**sp.Rational(-7, 3) * (3 * npos * Dy(ap) - 4 * Dy(npos) * ap) / 3) == 0)
ok('S6 energy: d/dy[(n\')^2 + (24A/7) n^(7/3)] = 2n\'(n\'\' + 4A n^(4/3))',
   sp.simplify(Dy(Dy(npos)**2 + 24 * Ac / 7 * npos**sp.Rational(7, 3)) - 2 * Dy(npos) * (Dy(npos, 2) + 4 * Ac * npos**sp.Rational(4, 3))) == 0)
vp = sp.Function('vp', positive=True)(y)
nv = vp**-6
ok('S6 v = n^(-1/6): n\'^2 = E - (24A/7) n^(7/3) <=> v\'^2 = E v^14/36 - 2A/21',
   sp.simplify((Dy(nv)**2 - (Ec - 24 * Ac / 7 * nv**sp.Rational(7, 3))) / (36 * vp**-14) - (Dy(vp)**2 - (Ec * vp**14 / 36 - 2 * Ac / 21))) == 0)
w2 = sp.Symbol('w2')  # stands for v'^2
nddv = sp.expand(Dy(nv, 2) + 4 * Ac * vp**-8)  # n'' + 4A n^(4/3), n^(4/3) = v^-8 on this branch
vdd_needed = sp.solve(nddv.subs(Dy(vp, 2), sp.Symbol('V2')).subs(Dy(vp), sp.sqrt(w2)), sp.Symbol('V2'))[0]
ok('S6 with v\'^2 = E v^14/36 - 2A/21, n\'\' = -4A n^(4/3) (n = v^-6) is equivalent to v\'\' = (7E/36) v^13',
   sp.simplify(vdd_needed.subs(w2, Ec * vp**14 / 36 - 2 * Ac / 21) - 7 * Ec * vp**13 / 36) == 0)
om, Vw = sp.symbols('omega Vw')  # Vw stands for v(omega z); w(z) = v(omega z)/omega, w'' = omega v''(omega z)
vz = sp.Function('vz'); wz = vz(om * zp) / om
ok('S6 symmetry: w = v(omega z)/omega has w\'\' - (7E/36)w^13 = (7E/36)Vw^13 (omega - omega^-13) = (7E/36)Vw^13 omega^-13 (omega^14 - 1)',
   sp.simplify(om * 7 * Ec / 36 * Vw**13 - 7 * Ec / 36 * (Vw / om)**13 - 7 * Ec / 36 * Vw**13 * om**-13 * (om**14 - 1)) == 0)
# series: v = c z + ...; Picard iteration keeps only exponents 1 mod 14
cc = sp.Symbol('c')
vs = cc * zp
for it in range(3):
    rhs = sp.expand(7 * Ec / 36 * vs**13)
    rhs = sum(term for term in sp.Add.make_args(rhs) if sp.degree(term, zp) <= 43)
    vs = cc * zp + sp.integrate(sp.integrate(rhs, (zp, 0, zp)), (zp, 0, zp))
    vs = sum(term for term in sp.Add.make_args(sp.expand(vs)) if sp.degree(term, zp) <= 43)
exps = sorted({sp.degree(term, zp) for term in sp.Add.make_args(vs)})
ok('S6 series of v\'\' = (7E/36)v^13, v(0)=0, v\'(0)=c through z^43: exponents %s, all = 1 mod 14' % exps, all(e % 14 == 1 for e in exps) and exps == [1, 15, 29, 43])
nser = sp.series((vs / (cc * zp))**-6, zp, 0, 30).removeO()
Kc = cc**-6
nfull = Kc * zp**-6 * nser
aser = sp.expand(-sp.diff(nfull, zp, 2) / 4)
ok('S6 n = v^-6 = K z^-6 (1 + O(z^14)), K = c^-6; a = -n\'\'/4 = -(21/2)K z^-8 (1 + O(z^14))',
   sp.expand(nser - 1).subs(zp, 0) == 0 and all(sp.degree(tm, zp) % 14 == 0 for tm in sp.Add.make_args(sp.expand(nser)))
   and sp.simplify(sp.expand(aser * zp**8).subs(zp, 0) + sp.Rational(21, 2) * Kc) == 0
   and all((sp.Poly(sp.expand(aser * zp**8), zp).monoms()[i][0]) % 14 == 0 for i in range(len(sp.Poly(sp.expand(aser * zp**8), zp).monoms()))))
ok('S6 consistency: v\'(y*)^2 = c^2 = -2A/21 and A n^(4/3) = A c^-8 z^-8 = -(21/2) c^-6 z^-8', sp.simplify(-sp.Rational(21, 2) * cc**2 * cc**-8 + sp.Rational(21, 2) * cc**-6) == 0)

# ---------------- Step 7 ----------------
sub7 = {a: -Dy(n, 2) / 4, h: -Dy(m, 2) / 3, f: -(Dy(b, 2) + 6 * n) / 2, g: -Dy(u) - 2 * m}
def S7(e):
    return sp.expand(e.subs(sub7).doit())
Lm = Dy(m, 3) - (Dy(n) / n) * Dy(m, 2) - (Dy(n, 2) / n) * Dy(m) + Dy(n, 3) / (2 * n) * m
Lb = Dy(b, 3) - 2 * Dy(n) / (3 * n) * Dy(b, 2) - 2 * Dy(n, 2) / (3 * n) * Dy(b) + Dy(n, 3) / (6 * n) * b
Rb = -2 * Dy(n) - (8 * l - 1) * Dy(n, 2) / (6 * n) - 4 * m * Dy(m, 3) / (9 * n) + 2 * Dy(m) * Dy(m, 2) / (3 * n)
Lu = Dy(u, 2) - Dy(n) / (3 * n) * Dy(u) - Dy(n, 2) / (3 * n) * u
Ru = (-(6 * l - 1) * Dy(m, 2) / (9 * n) - b * Dy(m, 3) / (9 * n) - m * Dy(b, 3) / (3 * n) - 4 * m * Dy(n) / (3 * n)
      + Dy(b) * Dy(m, 2) / (3 * n) + Dy(b, 2) * Dy(m) / (3 * n))
ok('S7 T5 after Poisson = -n L_m m', sp.simplify(S7(eqT[5]) + n * Lm) == 0)
ok('S7 T4 after Poisson = -(3n/2)(L_b b - R_b)', sp.simplify(S7(eqT[4]) + 3 * n / 2 * (Lb - Rb)) == 0)
ok('S7 T3 after Poisson = -3n (L_u u - R_u)', sp.simplify(S7(eqT[3]) + 3 * n * (Lu - Ru)) == 0)
ok('S7 T2 is affine in k\' with coefficient 3n', sp.expand(sp.diff(eqT[2], Dy(k)) - 3 * n) == 0 and sp.expand(sp.diff(eqT[2], Dy(k), 2)) == 0)
# ---------------- Step 8 ----------------
Lm_n = (Lm.subs(m, n).doit())
ok('S8 L_m n = (3/2) n\'\'\' - 2n\'n\'\'/n, which vanishes when T6 holds (n\'\'\' = 4n\'n\'\'/(3n))',
   sp.simplify(Lm_n - (sp.Rational(3, 2) * Dy(n, 3) - 2 * Dy(n) * Dy(n, 2) / n)) == 0
   and sp.simplify(Lm_n.subs(Dy(n, 3), 4 * Dy(n) * Dy(n, 2) / (3 * n))) == 0)
Kk = sp.Symbol('K'); rr = sp.Symbol('rr')
nE = Kk * zp**-6
def euler_ind(L, var, order):
    e = L.subs(n, Kk * y**-6).subs(var, y**rr).doit()
    return sp.factor(sp.simplify(e * y**order / y**rr))
Pm = euler_ind(Lm, m, 3); Pb = euler_ind(Lb, b, 3)
uu = sp.Function('uu')(y)
Lu2 = Dy(uu, 2) - Dy(n) / (3 * n) * Dy(uu) - Dy(n, 2) / (3 * n) * uu
Pu = euler_ind(Lu2, uu, 2)
ok('S7 orders of L_m, L_b, L_u in m, b, u are 3, 3, 2 (matching m,b in C^3, u in C^2 from Poisson)',
   sp.ode_order(Lm, m) == 3 and sp.ode_order(Lb, b) == 3 and sp.ode_order(Lu, tq) == 3 and sp.ode_order(Lu2, uu) == 2)
ok('S8 indicial P_m(r) = (r+6)(r+4)(r-7) [n = K z^-6]', sp.expand(Pm - (rr + 6) * (rr + 4) * (rr - 7)) == 0)
ok('S8 indicial P_b(r) = (r+2)(r^2-r-28)', sp.expand(Pb - (rr + 2) * (rr**2 - rr - 28)) == 0)
ok('S8 indicial P_u(r) = r^2 + r - 14', sp.expand(Pu - (rr**2 + rr - 14)) == 0)
good = True
for Pr in (Pm, Pb, Pu):
    rts = sp.solve(Pr, rr)
    good &= len(rts) == sp.degree(Pr, rr)
    for r1 in rts:
        for r2 in rts:
            if r1 != r2:
                q = sp.nsimplify(sp.simplify((r1 - r2) / 14))
                good &= not q.is_integer
ok('S8 roots of P_m, P_b, P_u distinct; no root difference is a nonzero multiple of 14', good)
# Euler-form coefficients analytic in z^14 for n = K z^-6 G(z^14)
gs = sp.symbols('g1:5')
Gs = 1 + sum(gs[i] * zp**(14 * (i + 1)) for i in range(4))
nG = Kk * zp**-6 * Gs
good = True
for kord in (1, 2, 3):
    ser = sp.series(zp**kord * sp.diff(nG, zp, kord) / nG, zp, 0, 60).removeO()
    good &= all(sp.degree(tm, zp) % 14 == 0 for tm in sp.Add.make_args(sp.expand(ser)) if tm.has(zp)) and not ser.has(sp.log)
ok('S8 z n\'/n, z^2 n\'\'/n, z^3 n\'\'\'/n are series in z^14 for n = K z^-6 G(z^14) (checked through z^59)', good)
# translation invariance (complex delta allowed): residuals shift
dl = sp.Symbol('delta')
RH, PH = sp.Function('RH')(x, y), sp.Function('PH')(x, y)
Rn = RH.subs(x, x - dl); Pn = PH.subs(x, x - dl) + l * dl * y
trn = transport(Rn, Pn); trold = transport(RH, PH).subs(x, x - dl)
ok('S8 translation rho(x-delta,y), psi(x-delta,y) + l delta y: transport and Poisson residuals are the shifted ones',
   sp.simplify((trn - trold).doit()) == 0 and sp.simplify((poisson(Rn, Pn) - poisson(RH, PH).subs(x, x - dl)).doit()) == 0)
psi_sh = sp.expand((n * x**3 + m * x**2 + (b - l * y) * x + tq).subs(x, x - dl) + l * dl * y)
ok('S8 translation changes m to m - 3 delta n (and keeps n, a)', sp.expand(sp.Poly(psi_sh, x).coeff_monomial(x**2) - (m - 3 * dl * n)) == 0
   and sp.expand(sp.Poly(psi_sh, x).coeff_monomial(x**3) - n) == 0)
r_ = (1 - sp.sqrt(113)) / 2; tau = (-1 - sp.sqrt(57)) / 2; rpl = (1 + sp.sqrt(113)) / 2; taup = (-1 + sp.sqrt(57)) / 2
ok('S8 r = (1-sqrt113)/2 and tau = (-1-sqrt57)/2 are roots of P_b, P_u; -5 < r < -9/2 < tau < -4',
   sp.simplify(Pb.subs(rr, r_)) == 0 and sp.simplify(Pu.subs(rr, tau)) == 0 and (-5 < r_) == True and (r_ < -sp.Rational(9, 2)) == True
   and (-sp.Rational(9, 2) < tau) == True and (tau < -4) == True)
ok('S8 -2n\' = 12K z^-7 for n = K z^-6; P_b(-4) = 16; particular b = (12K/16) z^-4 = (3K/4) z^-4',
   sp.simplify(-2 * sp.diff(nE, zp) - 12 * Kk * zp**-7) == 0 and Pb.subs(rr, -4) == 16
   and sp.simplify(Lb.subs(b, 3 * Kk / 4 * y**-4).subs(n, Kk * y**-6).doit() - 12 * Kk * y**-7) == 0)
mu = sp.Symbol('mu')
quad = (-4 * m * Dy(m, 3) / (9 * n) + 2 * Dy(m) * Dy(m, 2) / (3 * n)).subs(m, mu * y**-4).subs(n, Kk * y**-6).doit()
ok('S8 quadratic-in-m part of R_b is O(z^-5) for m = O(z^-4) (its z^-5 coefficient is in fact 0); -(8l-1)n\'\'/(6n) = -7(8l-1) z^-2',
   sp.simplify(quad) == 0 and sp.simplify((-(8 * l - 1) * Dy(n, 2) / (6 * n)).subs(n, Kk * y**-6).doit() + 7 * (8 * l - 1) * y**-2) == 0)
Bc, mu4 = sp.symbols('B mu4')
Ru_B = Ru.subs({b: Bc * y**r_, m: mu4 * y**-4}).subs(n, Kk * y**-6).doit()
Ru_B = sp.expand(sp.powsimp(sp.expand(Ru_B)))
ok('S8 R_u with b = B z^r, m = mu z^-4: b,m terms are c z^(r-1); rest O(z^-5) (as z -> 0)',
   all(sp.simplify(tm.as_coeff_exponent(y)[1] - (r_ - 1)) == 0 or sp.N(tm.as_coeff_exponent(y)[1]) >= -5 - 1e-12 for tm in sp.Add.make_args(Ru_B)))
ok('S8 exponents r+1 and -3 exceed tau; P_u(r+1) = 4r+16 != 0, P_u(-3) = -8 (nonresonant particular terms)',
   (r_ + 1 > tau) == True and (-3 > tau) == True and sp.simplify(Pu.subs(rr, r_ + 1) - (4 * r_ + 16)) == 0 and sp.simplify(4 * r_ + 16) != 0 and Pu.subs(rr, -3) == -8)
# ---------------- Step 9 ----------------
Fv = -r_ * (r_ - 1) * Bc / 2
ok('S9 f = -(b\'\'+6n)/2 leading -r(r-1)B/2 z^(r-2) = -14B z^(r-2) (r^2 - r = 28); r-2 < -6 so n and z^-4 parts are lower',
   sp.simplify(Fv + 14 * Bc) == 0 and (r_ - 2 < -6) == True)
Fs = sp.Symbol('F')
bf = (b * Dy(f) - 2 * Dy(b) * f).subs({b: Bc * y**r_, f: Fs * y**(r_ - 2)}).doit()
ok('S9 b f\' - 2b\'f = -(r+2) B F z^(2r-3)', sp.simplify(bf + (r_ + 2) * Bc * Fs * y**(2 * r_ - 3)) == 0)
kB = Bc * Fs / (6 * Kk)
ok('S9 k = BF/(6K) z^(2r+4) solves 3K z^-6 k\' + b f\' - 2b\'f = 0; k_B = -7B^2/(3K) with F = -14B',
   sp.simplify(3 * Kk * y**-6 * Dy(kB * y**(2 * r_ + 4)) + bf) == 0 and sp.simplify(kB.subs(Fs, -14 * Bc) + 7 * Bc**2 / (3 * Kk)) == 0)
kBv = -7 * Bc**2 / (3 * Kk)
ok('S9 (2r+4) B k_B = 7(sqrt113 - 5) B^3/(3K) != 0', sp.simplify((2 * r_ + 4) * Bc * kBv - 7 * (sp.sqrt(113) - 5) * Bc**3 / (3 * Kk)) == 0 and sp.sqrt(113) > 5)
ok('S9 exponent order: 3r+3 < -21/2 < -10 < 2tau-1; 3r+3 < 2r+4 (k); 3r+3 < 2r-1 (B0 z^-4 * k\'); 2r+4 < tau+1 (m,g,u part of k); 2r+4 < r (cross terms); 2r+4 < r+5; 2r+4 < 0; tau-1 < r, tau-1 < -4 (g)',
   all(bool(c_) for c_ in [3 * r_ + 3 < -sp.Rational(21, 2), -sp.Rational(21, 2) < -10, -10 < 2 * tau - 1, 3 * r_ + 3 < 2 * r_ + 4, 3 * r_ + 3 < 2 * r_ - 1,
                           2 * r_ + 4 < tau + 1, 2 * r_ + 4 < r_, 2 * r_ + 4 < r_ + 5, 2 * r_ + 4 < 0, tau - 1 < r_, tau - 1 < -4]))
ok('S9 m,g,u terms of T2 have exponent tau-6 (2m g\', m\'g, 3hu with m~z^-4, g~z^(tau-1), u~z^tau, h~z^-6), giving k ~ z^(tau+1)',
   sp.simplify((-4 + tau - 2) - (tau - 6)) == 0 and sp.simplify((-5 + tau - 1) - (tau - 6)) == 0 and sp.simplify((-6 + tau) - (tau - 6)) == 0)
# ---------------- Step 10 ----------------
B0 = 3 * Kk / 4; F0 = -10 * B0 - 3 * Kk; k0 = B0 * F0 / (6 * Kk)
ok('S10 B0 = 3K/4, F0 = -10B0 - 3K = -21K/2, k0 = B0F0/(6K) = -21K/16',
   sp.simplify(F0 + sp.Rational(21, 2) * Kk) == 0 and sp.simplify(k0 + sp.Rational(21, 16) * Kk) == 0)
f10 = (-(Dy(b, 2) + 6 * n) / 2).subs({b: B0 * y**-4, n: Kk * y**-6}).doit()
bf10 = (b * Dy(f) - 2 * Dy(b) * f).subs({b: B0 * y**-4, f: F0 * y**-6}).doit()
ok('S10 f leading F0 z^-6; b,f part of T2 = 2B0F0 z^-11; 3K z^-6 (k0 z^-4)\' + 2B0F0 z^-11 = 0',
   sp.simplify(f10 - F0 * y**-6) == 0 and sp.simplify(bf10 - 2 * B0 * F0 * y**-11) == 0 and sp.simplify(3 * Kk * y**-6 * Dy(k0 * y**-4) + bf10) == 0)
Uc = sp.Symbol('U')
g10 = -Dy(Uc * y**tau)
ok('S10 g = -u\' leading -tau U z^(tau-1); -g u = tau U^2 z^(2tau-1); 2tau-1 = -2-sqrt57 < -9; tau+1 > -4; tau-4 > 2tau-1',
   sp.simplify(g10 + tau * Uc * y**(tau - 1)) == 0 and sp.simplify(-g10 * Uc * y**tau - tau * Uc**2 * y**(2 * tau - 1)) == 0
   and sp.simplify(2 * tau - 1 - (-2 - sp.sqrt(57))) == 0 and bool(2 * tau - 1 < -9) and bool(tau + 1 > -4) and bool(tau - 4 > 2 * tau - 1))
# ---------------- Step 11 ----------------
ok('S11 b k\' with b = B0 z^-4, k = k0 z^-4 equals (63K^2/16) z^-9; g u = O(z^-7 L^4) and k = O(z^-4) are o(z^-9)',
   sp.simplify((B0 * y**-4 * Dy(k0 * y**-4)) - sp.Rational(63, 16) * Kk**2 * y**-9) == 0 and (-4 - 3 > -9) and (-4 > -9))

# ---------------- Step 12: the two profiles, parity ----------------
Qc = sp.Symbol('Q')
hy = beta + y
fa = (beta / hy)**4; ba = beta * hy / 3 - beta**4 / (3 * hy**2)
ok('S12 curved: b\'\' = -2f, b f\' = 2(b\'-beta)f, f(0)=1, b(0)=0, b\'(0)=beta (symbolic l)',
   sp.simplify(Dy(ba, 2) + 2 * fa) == 0 and sp.simplify(ba * Dy(fa) - 2 * (Dy(ba) - beta) * fa) == 0 and sp.simplify(fa.subs(y, 0) - 1) == 0
   and sp.simplify(ba.subs(y, 0)) == 0 and sp.simplify(Dy(ba).subs(y, 0) - beta) == 0)
psa = x * (ba - l * y) + Qc
ok('S12 curved: -Lap(x(b-ly)) = 2fx = rho_x and V.grad(fx^2) = (2(2l-b\')f + bf\')x^2 = f x^2',
   sp.simplify(-lap(psa) - 2 * fa * x) == 0 and sp.simplify(transport(fa * x**2, psa) + fa * x**2 - (2 * (2 * l - Dy(ba)) * fa + ba * Dy(fa)) * x**2) == 0
   and sp.simplify(transport(fa * x**2, psa)) == 0)
psb = -x**3 / 3 + (l - sp.Rational(1, 2)) * x * y + Qc
ok('S12 polynomial: V = (x/2, beta y - x^2), -Lap psi = 2x, V.grad(x^2) = x^2',
   sp.simplify(l * x - Dy(psb) - x / 2) == 0 and sp.simplify(l * y + sp.diff(psb, x) - (beta * y - x**2)) == 0
   and sp.simplify(-lap(psb) - 2 * x) == 0 and sp.simplify(transport(x**2, psb)) == 0)
good = True
for rr_, ps_ in [(fa * x**2, psa), (x**2, psb)]:
    good &= sp.simplify(Dy(ps_).subs({x: 0, y: 0})) == 0 and sp.simplify(sp.diff(ps_, x).subs({x: 0, y: 0})) == 0
    good &= all(sp.simplify(sp.diff(rr_, x, i, y, j).subs({x: 0, y: 0}) - (2 if (i, j) == (2, 0) else 0)) == 0 for i in range(3) for j in range(3) if i + j <= 2)
    good &= sp.simplify(rr_ - rr_.subs(x, -x)) == 0 and sp.simplify((ps_ - Qc) + (ps_ - Qc).subs(x, -x)) == 0
ok('S12 both: W(0)=0, jet rho = x^2 + O(|X|^3), rho even in x, psi - Q odd in x; q_2 = q_4 = 0, q_0 = Q', good)
ok('S12 curved pair: f has a pole at y = -beta (domain y > -beta, a half-plane, maximal I = (-beta, inf))', sp.simplify(sp.denom(sp.together(fa)).subs(y, -beta)) == 0)

# ---------------- Step 13 / C / D ----------------
good = True
for N in range(5, 9):
    fj, qj, rho, psi = layered(N, N - 1)
    T = sp.Poly(transport(rho, psi), x); P = sp.Poly(poisson(rho, psi), x)
    good &= sp.expand(P.coeff_monomial(x**(N - 1)) + Dy(qj[N - 1], 2) + N * fj[N]) == 0
    good &= T.degree() <= 2 * N - 2 and sp.expand(T.coeff_monomial(x**(2 * N - 2)) - ((N - 1) * qj[N - 1] * Dy(fj[N]) - N * Dy(qj[N - 1]) * fj[N])) == 0
ok('S13 M=N-1 (N=5..8): top Poisson q\'\' = -N a and top transport (N-1) q a\' - N q\'a', good)
Nn = sp.Symbol('N', positive=True); mN = Nn - 1
q, aq = sp.Function('q')(y), sp.Function('aq')(y)
ok('S13 a = -q\'\'/N in top transport gives -(m q q\'\'\' - N q\'q\'\')/N; J\' = m q q\'\'\' - N q\'q\'\'',
   sp.expand((mN * q * Dy(aq) - Nn * Dy(q) * aq).subs(aq, -Dy(q, 2) / Nn).doit() + (mN * q * Dy(q, 3) - Nn * Dy(q) * Dy(q, 2)) / Nn) == 0
   and sp.expand(Dy(mN * q * Dy(q, 2) - (2 * Nn - 1) * Dy(q)**2 / 2) - (mN * q * Dy(q, 3) - Nn * Dy(q) * Dy(q, 2))) == 0)
qp = sp.Function('qp', positive=True)(y)
ok('S13 (a |q|^(-N/m))\' = |q|^(-N/m)(m q a\' - N q\'a)/(m q) (q > 0; q < 0 identical with |q| = -q)',
   sp.simplify(Dy(aq * qp**(-Nn / mN)) - qp**(-Nn / mN) * (mN * qp * Dy(aq) - Nn * Dy(qp) * aq) / (mN * qp)) == 0)
Jq = mN * qp * Dy(qp, 2) - (2 * Nn - 1) * Dy(qp)**2 / 2
ok('S13 H = |q|^(-1/(2m)): H\'\' = -J |q|^(-1/(2m)-2)/(2m^2) (symbolic N; J even in q)',
   sp.simplify(Dy(qp**(-1 / (2 * mN)), 2) + Jq * qp**(-1 / (2 * mN) - 2) / (2 * mN**2)) == 0 and sp.expand(Jq.subs(qp, -qp).doit() - Jq) == 0)
Q0, Q1, Q2 = sp.symbols('Q0 Q1 Q2')
ok('S13 at q = 0: J = -(2N-1)(q\')^2/2; J = 0 iff q\' = 0', sp.expand((mN * Q0 * Q2 - (2 * Nn - 1) * Q1**2 / 2).subs(Q0, 0) + (2 * Nn - 1) * Q1**2 / 2) == 0)
ok('S13 a = A|q|^(N/m): a\' = A (N/m)|q|^(N/m-1) sgn(q) q\', and N/m - 1 = 1/m > 0', sp.simplify(Nn / mN - 1 - 1 / mN) == 0
   and sp.simplify(Dy(Ac * qp**(Nn / mN)) - Ac * Nn / mN * qp**(Nn / mN - 1) * Dy(qp)) == 0)
sg, c_, d_c = sp.symbols('sigma c dd')
Hl = c_ * y + d_c
def Dcheck(Nv):
    qD = sg * Hl**(-2 * (Nv - 1)); aD = -sg * 2 * (Nv - 1) * (2 * Nv - 1) * c_**2 / Nv * Hl**(-2 * Nv)
    J = (Nv - 1) * qD * Dy(qD, 2) - (2 * Nv - 1) * Dy(qD)**2 / 2
    return (sp.simplify(Dy(qD, 2) + Nv * aD) == 0 and sp.simplify((Nv - 1) * qD * Dy(aD) - Nv * Dy(qD) * aD) == 0
            and sp.simplify((J).subs(sg, 1)) == 0 and sp.simplify(J.subs(sg, -1)) == 0)
ok('D q = sigma(cy+d)^(-2(N-1)), a = -sigma 2(N-1)(2N-1)c^2/N (cy+d)^(-2N): q\'\' = -Na, transport, J = 0 (symbolic N)', Dcheck(Nn))
ok('D same for N = 5..10 (exact)', all(Dcheck(sp.Integer(Nv)) for Nv in range(5, 11)))
Hp = sp.Symbol('Hp', positive=True)
ok('D |q|^(-1/(2m)) = cy+d and a = A|q|^(N/m) with A = -sigma 2(N-1)(2N-1)c^2/N (cy+d > 0)',
   sp.simplify((Hp**(-2 * mN))**(-1 / (2 * mN)) - Hp) == 0 and sp.simplify((Hp**(-2 * mN))**(Nn / mN) - Hp**(-2 * Nn)) == 0)
print('ALL', all(R), len(R), flush=True)
