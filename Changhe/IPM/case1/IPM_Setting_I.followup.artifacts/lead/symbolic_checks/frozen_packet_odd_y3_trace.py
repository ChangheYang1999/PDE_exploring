# Numerical check: y^3 axis coefficient of the frozen packet v_Phi at moderate parameters.
# v-hat = Phi(t) sgn(eta) |eta|^(2b-A-2) |zeta|^(-2b), t = xi/|eta|^A, Phi odd, supp in |t| in [1,2]  (v real, odd in s, y)
# v(s,y) = -(1/pi^2) int_0^inf d eta int_1^2 dt Phi(t) eta^(-2) (1 + t^2 eta^(2A-2))^(-b) sin(s t eta^A) sin(y eta)
# G_3(s) = (1/6) d_y^3 v(s,0) = (1/(6 pi^2)) int int Phi(t) eta (1 + t^2 eta^(2A-2))^(-b) sin(s t eta^A)
# Substituting u = s t eta^A: I(s,t) = (1/A)(s t)^(-2/A) int_0^inf u^(2/A-1) (1 + t^2 (u/(s t))^((2A-2)/A))^(-b) sin u du
# Prediction: G_3(s) = K s^((g-2)/A) + c1 s + o(s), K from the leading symbol; exponent 0.5 for A = 3, g = 3.5.
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma
import mpmath as mp
A = 3.0; g = 3.5; b = g/(2*(A-1))
def Phi(t):
    return np.exp(-1.0/((t-1.0)*(2.0-t))) if 1.0 < t < 2.0 else 0.0
tn, tw = np.polynomial.legendre.leggauss(60); tn = 1.5 + 0.5*tn; tw = 0.5*tw
def I(s, t):
    f = lambda u: u**(2/A-1)*(1.0 + t*t*(u/(s*t))**((2*A-2)/A))**(-b)
    # split [0,1] (endpoint singularity u^(2/A-1) sin u ~ u^(2/A)) and [1, inf) with the QAWF sine weight
    a = quad(lambda u: f(u)*np.sin(u), 0, 1, limit=200, epsabs=1e-15, epsrel=1e-12)[0]
    c = quad(f, 1, np.inf, weight='sin', wvar=1.0, limlst=200, epsabs=1e-15)[0]
    return (a + c)/(A*(s*t)**(2/A))
def G3(s):
    return sum(w*Phi(t)*I(s, t) for t, w in zip(tn, tw))/(6*np.pi**2)
# leading coefficient: (1 + ...)^(-b) ~ t^(-2b) (u/(s t))^(-g/A); int u^(c-1) sin u = Gamma(c) sin(pi c/2), c = (2 - g)/A
c = (2 - g)/A
Mt = sum(w*Phi(t)*t**(-2*b - 2/A + g/A) for t, w in zip(tn, tw))
K = Mt*gamma(c)*np.sin(np.pi*c/2)/(6*np.pi**2*A)
print('A, g, b =', A, g, b, ' exponent (g-2)/A =', (g-2)/A, ' predicted K =', K)
for s in [1e-1, 3e-2, 1e-2, 3e-3, 1e-3, 3e-4, 1e-4]:
    G = G3(s)
    print('s=%8.1e  G3=% .10e  G3/s^0.5=% .8e  (G3 - K s^0.5)/s=% .6e' % (s, G, G/s**0.5, (G - K*s**0.5)/s))
