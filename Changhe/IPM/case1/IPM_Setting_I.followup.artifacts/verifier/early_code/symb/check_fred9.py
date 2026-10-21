"""verifier, request (j): fred9 01-source-estimate.  Own derivation of the second-derivative equation (13), the
leading coefficients (14), (16), and the exponent bookkeeping of sections 4-5."""
import sympy as sp

s, y, A = sp.symbols('s y A', real=True)
a = sp.Function('a')(s, y); b = sp.Function('b')(s, y); u = sp.Function('u')(s, y)
D = lambda f: a * sp.diff(f, s) + b * sp.diff(f, y)
P = D(u) - u                                   # transport defect
Dv = sp.diff(a, s) + sp.diff(b, y) - (A + 1)   # divergence defect
c = 2 * sp.diff(b, y) - 1
h = sp.diff(u, y) / a
T = D(a) / a
K = sp.diff(u, y, 2) - h * sp.diff(a, y)
ay, uy, us = sp.diff(a, y), sp.diff(u, y), sp.diff(u, s)
F = -ay * (sp.diff(b, y) * h + 2 * sp.diff(u, s, y) - ay * us / a - h * T) - (u / a) * sp.diff(a, y, 2)
E = D(K) + c * K - F
# (j1a) own derivation: d_y^2 of the transport defect, step by step
#   d_y P = D u_y + (b_y - 1) u_y + a_y u_s ;  d_y^2 P = D u_yy + (2 b_y - 1) u_yy + b_yy u_y + a_yy u_s + 2 a_y u_sy
e11 = sp.diff(P, y, 2) - (D(sp.diff(u, y, 2)) + c * sp.diff(u, y, 2) + sp.diff(b, y, 2) * uy
                          + sp.diff(a, y, 2) * us + 2 * ay * sp.diff(u, s, y))
print('(11) d_y^2 P - [(D+c) u_yy + b_yy u_y + a_yy u_s + 2 a_y u_sy] =', sp.simplify(e11))
# (j1b) E in terms of the defects: find the combination by eliminating the third derivatives
cand = sp.diff(P, y, 2) - (ay / a) * sp.diff(P, y) - (sp.diff(a, y, 2) / a) * P - uy * sp.diff(Dv, y)
print('(13) (D+c)K - F - [P_yy - (a_y/a) P_y - (a_yy/a) P - u_y d_y(div W - A - 1)] =', sp.simplify(sp.expand(E - cand)))
# also: the pieces used in the text
e_hb = sp.simplify(us + h * b - u / a - P / a)
print('     u_s + h b - u/a - P/a =', e_hb)
e_Dh = sp.simplify(D(h) + c * h - (sp.diff(b, y) * h - ay * us / a - h * T) - (sp.diff(P, y) / a))
print('     D h + c h - (b_y h - a_y u_s/a - h T) - P_y/a =', e_Dh)

# (j1c) leading coefficients on the cone: s = -r, y = eps r, Taylor data with generic coefficients
r, eps = sp.symbols('r epsilon', positive=True)
cs, gs, a20, a11, b11, b20, u11, u20, a40, a22 = sp.symbols('c_* g_* a20 a11 b11 b20 u11 u20 a40 a22')
# parity-respecting second-order Taylor models (a even, b and u odd in y), with div = A + 1 imposed at first order
aa = A * s + a20 * s ** 2 + cs * y ** 2 / 2
bb = y - 2 * a20 * s * y + b11 * y ** 3
uu = gs * y + u11 * s * y + u20 * y ** 3
sub = {a: aa, b: bb, u: uu}
Fm = F.subs(sub).doit()
K0 = -(cs * gs / A) * y / s
DK0 = (D(K0) + c * K0).subs(sub).doit()
for name, expr in [('F', Fm), ('(D+c)K_0', DK0)]:
    ex = sp.simplify(expr.subs({s: -r, y: eps * r}))
    lead = sp.limit(ex / eps, r, 0)
    print('(14/16) leading of %s / (y/s) as r -> 0, eps fixed:' % name, sp.factor(sp.simplify(-lead)),
          ' [(A-2) lambda = %s]' % sp.factor((A - 2) * cs * gs / A))

# (j3) exponents.  theta window, eps powers, source integral
al, th = sp.symbols('alpha theta', positive=True)
delta = 2 + A * (al - 1)
print('(20) (1-al)/(1+al) < 1/(A-1)  <=>  delta > 0:  (1/(A-1) - (1-al)/(1+al)) * (A-1)(1+al) =',
      sp.factor(sp.simplify((1 / (A - 1) - (1 - al) / (1 + al)) * (A - 1) * (1 + al))))
# first term of (26): e^t |y_t|^al / |y| with |y_t| = |y| e^t at t = theta log eps: |y|^(al-1) eps^(theta(1+al))
#   = r^(al-1) eps^(al - 1 + theta (1 + al));  second: e^t |y_t| r_t^(al-1)/|y| = r^(al-1) e^((2 + A(al-1)) t)
t = sp.symbols('t')
second = sp.simplify(sp.exp(t) * sp.exp(t) * sp.exp(A * t * (al - 1)))
print('(26) second-term t-exponent:', sp.simplify(sp.log(second) / t), ' = delta:', sp.simplify(sp.log(second) / t - delta) == 0)
print('     first-term eps-exponent al - 1 + th(1+al) > 0 <=> th > (1-al)/(1+al)')
# X3 numbers: alpha window and theta window at alpha = 0.85, A = 10.150725
Av = 10.150725221284
for alv in (0.81, 0.85, 0.93):
    print('     X3 A, alpha = %.2f: delta = %.5f, theta in (%.5f, %.5f), delta/A = alpha + 2/A - 1 = %.5f'
          % (alv, 2 + Av * (alv - 1), (1 - alv) / (1 + alv), 1 / (Av - 1), (2 + Av * (alv - 1)) / Av))

# (j6) velocity companion of a conormal density mode, flat model curve xi = s (s > 0 side; the s < 0 side is the
# reflection): rho = s^mu y^j; particular psi with -Lap psi = d_s rho as a finite sum c_k s^(mu+1+2k) y^(j-2k).
ss = sp.symbols('s', positive=True)
mu = sp.symbols('mu', positive=True)
for j in (1, 3, 5):
    cks = sp.symbols('k0:%d' % (j // 2 + 1))
    psi = sum(cks[k] * ss ** (mu + 1 + 2 * k) * y ** (j - 2 * k) for k in range(j // 2 + 1))
    res = sp.expand(-sp.diff(psi, ss, 2) - sp.diff(psi, y, 2) - mu * ss ** (mu - 1) * y ** j)
    eqs = [sp.simplify(res.coeff(y, j - 2 * k) / ss ** (mu - 1 + 2 * k)) for k in range(j // 2 + 1)]
    sol = sp.solve(eqs, cks, dict=True)[0]
    psi = psi.subs(sol)
    U1, U2 = sp.expand(-sp.diff(psi, y)), sp.expand(sp.diff(psi, ss))
    print('(j6) j=%d: U2 + rho =' % j, sp.factor(sp.simplify(U2 + ss ** mu * y ** j)), '| U1 =', sp.factor(U1),
          '| residual', sp.simplify(sp.expand(-sp.diff(psi, ss, 2) - sp.diff(psi, y, 2) - mu * ss ** (mu - 1) * y ** j)))
