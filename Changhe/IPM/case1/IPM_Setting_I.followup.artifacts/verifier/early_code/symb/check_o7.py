# Verifier check of lead request (o7) items 2 to 4 (NOTES_FOR_TEAM 08:46Z). Own code.
# 2. A = 2, R12 with L = 2: I5 = F5/(w H5) as a Laurent polynomial, B5 = -f.p. int_0^2 I5, G5 = H5 (int_2^x I5).
# 3. J5/J3 = 5(4 - beta)/(3(beta + 4)) and C_A in the two forms.
# 4. G3(0) of the even frozen packet at the precise X3 parameters (same packet as D34).
import sympy as sp
x = sp.Symbol('x', positive=True)
print('== 2. A = 2, R12, L = 2')
w2 = -2*x*(4 - x**2)/(4 + x**2); g2 = x**2/(1 + x**2/4); A = 2
print('compatibility:', sp.simplify(w2*sp.diff(g2, x) - (sp.diff(w2, x) - A)*g2))
h2 = A + 1 - sp.diff(w2, x)
a2 = sp.simplify((sp.diff(g2, x) - sp.diff(w2, x, 2))/2)
G3 = sp.simplify(g2*a2/(3*w2))
print('G3 axis eq residual:', sp.simplify(w2*sp.diff(G3, x) + (3*h2 - 1)*G3 - (-a2*sp.diff(g2, x) + g2*sp.diff(a2, x)/3)))
a4 = (sp.diff(G3, x) - sp.diff(a2, x, 2)/3)/4
F5 = sp.diff(a2, x)*G3 - a2*sp.diff(G3, x) + g2*sp.diff(a4, x)/5 - a4*sp.diff(g2, x)
H5 = 4*g2**7/w2**2
print('H5 homogeneous residual:', sp.simplify(w2*sp.diff(H5, x) + (5*h2 - 1)*H5))
I5 = sp.factor(sp.simplify(F5/(w2*H5)))
claim = sp.Rational(5, 768)/x**5 - sp.Rational(103, 960)/x**7 + sp.Rational(143, 240)/x**9 - sp.Rational(13, 12)/x**11
print('I5 =', I5, '; minus claim:', sp.simplify(I5 - claim))
Fanti = sp.integrate(sp.expand(claim), x)   # no constant, only negative powers
B5 = -Fanti.subs(x, 2)
print('B5 = -f.p. int_0^2 I5 =', B5, ' claim 11/1474560:', B5 == sp.Rational(11, 1474560))
G5 = x**2*(11*x**6 + 88*x**4 - 1872*x**2 + 9984)/(90*(x**2 + 4)**5)
print('G5 fifth equation residual:', sp.simplify(w2*sp.diff(G5, x) + (5*h2 - 1)*G5 - F5))
print('G5/H5 - (F(x) - F(2)):', sp.simplify(G5/H5 - (Fanti - Fanti.subs(x, 2))),
      ' (so G5 = H5 (F(x) + B5) near 0, coefficient of H5 = B5; H5 F(x) has the series',
      sp.series(sp.simplify(H5*Fanti), x, 0, 10), ')')
print('H5 near 0:', sp.series(H5, x, 0, 16), '; G5 near 2: bounded,', sp.simplify(G5.subs(x, 2)))
print('== 3. J5/J3 and C_A')
b = sp.Symbol('beta', positive=True)
J = lambda n: sp.Rational(n)/(n + b - 1)*sp.gamma((n - b + 1)/2)*sp.gamma(b - 1)/sp.gamma((n - b + 1)/2 + b - 1)
r = sp.gammasimp(J(5)/J(3))
print('J5/J3 =', sp.factor(r), '; minus 5(4-beta)/(3(beta+4)):', sp.simplify(r - 5*(4 - b)/(3*(b + 4))))
Aa = 2/b
CA1 = (b - 1)*(J(5) + J(3))/(3*Aa)
CA2 = (16 - b)/(3*Aa*(4 + b))*sp.gamma(2 - b/2)*sp.gamma(b)/sp.gamma(2 + b/2)
print('C_A forms ratio:', sp.simplify(sp.gammasimp(CA1/CA2)))
for bv in [sp.Rational(6, 5), sp.Rational(3, 2), sp.Rational(9, 5)]:
    print('   beta =', bv, ': C_A =', sp.N(CA1.subs(b, bv), 20), sp.N(CA2.subs(b, bv), 20))
As = sp.Symbol('A', positive=True); SA = 6*As*(4*As - 3)/(8*As - 1)
print('S_A - 2A - 8A(A-2)/(8A-1):', sp.simplify(SA - 2*As - 8*As*(As - 2)/(8*As - 1)))
print('== 4. G3(0), even packet (D34), precise parameters')
import numpy as np, mpmath as mp
from scipy import integrate
xg, wg = np.polynomial.legendre.leggauss(200)
def bump(t, a):
    out = np.zeros_like(t); m = (t > a) & (t < a + 1); out[m] = np.exp(-1/((t[m] - a)*(a + 1 - t[m]))); return out
t1 = 0.5*xg + 1.5; t2 = 0.5*xg + 2.5; ww = 0.5*wg
tn = np.concatenate([t1, t2]); tw = np.concatenate([ww, ww]); ph = np.concatenate([bump(t1, 1), -bump(t2, 2)])
for (Av, gv) in [(10.15, 29.75), (10.150725214760579, 29.749491), (10.150725214760579, 29.74949), (10.150725, 29.74949)]:
    q = 2*Av - 2; bb = gv/(2*(Av - 1))
    G0 = float(mp.beta(2/q, (gv - 2)/q))/(6*np.pi**2*q)*np.sum(tw*ph*tn**(-2/(Av - 1)))
    G0q = sum(wt*pt*integrate.quad(lambda e_: e_*(1 + tt**2*e_**q)**(-bb), 0, np.inf, epsabs=0, epsrel=1e-13, limit=400)[0]
              for tt, wt, pt in zip(tn, tw, ph))/(6*np.pi**2)
    print('A = %.15g g* = %.8g: G3(0) Beta form %.12e, direct quadrature %.12e' % (Av, gv, G0, G0q))
