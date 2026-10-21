"""verifier: reference value of the fred15 local exclusion (FINAL_REPORT 6.4 'Local exclusion near an explicit compatible
trace'): B_3(4, w_0) = (23/110592) B(7/4, 1/2) for w_0 = -4x(1 - x^2/16)/(1 + x^2/16), g_0 = x^2/(1 + x^2/16), normalization
g/x^2 -> 1 at 0.  Two routes: (1) the m-integral of 6.3.1 (k) with R computed from w, g directly (Q = (g' - w'')/(2 g^3),
P from the series of Q in m, sympy), quadrature at 40 digits; (2) the R12 closed form x*^5 R = (1-6k)(u^5-1)+(1+2k)(u^3-1)."""
import sympy as sp
import mpmath as mp
mp.mp.dps = 40
x, m = sp.symbols('x m', positive=True)
A = sp.Integer(4); L = sp.Integer(4)
w = -A * x * (1 - x**2 / L**2) / (1 + x**2 / L**2)
g = x**2 / (1 + x**2 / L**2)
# compatibility: w g' = (w' - A) g
print('compat residual:', sp.simplify(w * sp.diff(g, x) - (sp.diff(w, x) - A) * g))
Q = sp.simplify((sp.diff(g, x) - sp.diff(w, x, 2)) / (2 * g**3))
mm = sp.simplify(-w / g)
xstar = L
Qs = sp.simplify(Q.subs(x, xstar))
print('Q(x*) =', Qs, ' m(x) =', mm)
# P(m): divergent part of Q as m -> inf (x -> 0): Q = sum_j c_j m^j + O(1/m); get x(m) by inverting m(x)
xm = sp.solve(sp.Eq(mm, m), x)
xm = [s for s in xm if sp.limit(s, m, sp.oo) == 0][0]
Qm = sp.simplify(Q.subs(x, xm))
ser = sp.series(Qm, m, sp.oo, 2).removeO()
P = sum(ser.coeff(m, j) * m**j for j in range(1, 7))
print('P(m) =', sp.factor(P))
R = sp.simplify(Qm - P - Qs)
print('R(m) =', sp.factor(R))
beta = 2 / A
# R as an exact rational function of x (m(x), Q(x) and P(m(x)) are rational), so no cancellation in the quadrature
Rx = sp.factor(sp.cancel(Q - P.subs(m, mm) - Qs))
print('R(x) =', Rx)
integ = sp.lambdify(x, sp.cancel(Rx * (-sp.diff(mm, x))) , 'mpmath')
mmf = sp.lambdify(x, mm, 'mpmath')
I = mp.quad(lambda t: integ(mp.mpf(t)) * mmf(mp.mpf(t))**(beta - 2), [0, 1, 2, 3, 4])
B3 = (beta - 1) / (3 * A**beta) * I
ref = mp.mpf(23) / 110592 * mp.beta(mp.mpf(7) / 4, mp.mpf(1) / 2)
print('route 1 B3 =', mp.nstr(B3, 30))
print('claimed     ', mp.nstr(ref, 30), ' rel diff', mp.nstr(abs(B3 / ref - 1), 5))
# route 2: R12 closed form in u, x* = L
k = A / L**2
u = sp.symbols('u', positive=True)
R12 = ((1 - 6 * k) * (u**5 - 1) + (1 + 2 * k) * (u**3 - 1)) / L**5
mu = (A / L) * (1 / u - u)
integrand = sp.lambdify(u, R12 * mu**(beta - 2) * (A / L) * (1 + 1 / u**2), 'mpmath')
I2 = mp.quad(lambda t: integrand(mp.mpf(t)), [0, mp.mpf('0.5'), 1])
B3b = (beta - 1) / (3 * A**beta) * I2
print('route 2 B3 =', mp.nstr(B3b, 30), ' rel diff', mp.nstr(abs(B3b / ref - 1), 5))
print('23/193536 =', mp.nstr(mp.mpf(23) / 193536, 10), ' B(7/4,1/2) =', mp.nstr(mp.beta(mp.mpf(7) / 4, mp.mpf(1) / 2), 15))
print('natural units B3 L^(4+beta) =', mp.nstr(B3 * mp.mpf(4)**(4 + beta), 20))
