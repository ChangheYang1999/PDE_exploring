# Check of a referee formula: G_3(0) for an imaginary even Phi = i phi, int phi = 0, A = 3, g* = 3.5 (q = 4, b = 0.875).
# v = -(2/(2 pi)^2) int_0^inf sin(y r)/r^2 int phi(t) cos(s t r^A) (1 + t^2 r^q)^(-b) dt dr  (real, even in s, odd in y)
# G_3(s) = (1/6) d_y^3 v(s,0) = (1/(12 pi^2)) int phi(t) int_0^inf r cos(s t r^A) (1 + t^2 r^q)^(-b) dr dt
# predicted G_3(0) = (1/(12 pi^2 q)) B(2/q, (g*-2)/q) int phi(t) |t|^(-2/(A-1)) dt; G_3(s) - G_3(0) ~ C s^mu_3, mu_3 = (g*-2)/A
import numpy as np
from scipy.integrate import quad
from scipy.special import beta as Beta
A = 3.0; g = 3.5; q = 2*(A-1); b = g/q
def bump(t, a, c):
    return np.exp(-1.0/((t-a)*(c-t))) if a < t < c else 0.0
m1 = quad(lambda t: bump(t, 1, 2), 1, 2, epsabs=1e-15)[0]; m2 = quad(lambda t: bump(t, 2, 3), 2, 3, epsabs=1e-15)[0]
def phi(t):  # even in t; on t > 0: bump(1,2) - (m1/m2) bump(2,3), so int phi = 0
    t = abs(t); return bump(t, 1, 2) - (m1/m2)*bump(t, 2, 3)
tn, tw = np.polynomial.legendre.leggauss(80)
nodes = []
for a, c in [(1, 2), (2, 3)]:
    nodes += [(0.5*(a+c) + 0.5*(c-a)*x, 0.5*(c-a)*w) for x, w in zip(tn, tw)]
print('int phi over t > 0 =', sum(w*phi(t) for t, w in nodes))
M = 2*sum(w*phi(t)*t**(-2/(A-1)) for t, w in nodes)
G0 = Beta(2/q, (g-2)/q)*M/(12*np.pi**2*q)
def Ir0(t):  # int_0^inf r (1 + t^2 r^q)^(-b) dr, direct
    return quad(lambda r: r*(1 + t*t*r**q)**(-b), 0, np.inf, epsabs=1e-14, epsrel=1e-12, limit=400)[0]
G0_direct = 2*sum(w*phi(t)*Ir0(t) for t, w in nodes)/(12*np.pi**2)
print('G_3(0): formula % .12e  direct quadrature % .12e' % (G0, G0_direct))
def Ic(s, t):
    f = lambda u: u**(2/A-1)*(1.0 + t*t*(u/(s*t))**(q/A))**(-b)
    a = quad(lambda u: f(u)*np.cos(u), 0, 1, limit=200, epsabs=1e-15, epsrel=1e-12)[0]
    c = quad(f, 1, np.inf, weight='cos', wvar=1.0, limlst=200, epsabs=1e-15)[0]
    return (a + c)/(A*(s*t)**(2/A))
def G3(s):
    return 2*sum(w*phi(t)*Ic(s, t) for t, w in nodes)/(12*np.pi**2)
mu = (g-2)/A
for s in [1e-1, 1e-2, 1e-3, 1e-4]:
    G = G3(s)
    print('s=%7.1e  G3=% .10e  (G3-G3(0))/s^%.2f=% .6e' % (s, G, mu, (G - G0)/s**mu))
from scipy.special import gamma
c = (2 - g)/A
K = 2*sum(w*phi(t)*t**(-2*b - 2/A + g/A) for t, w in nodes)*gamma(c)*np.cos(np.pi*c/2)/(12*np.pi**2*A)
print('predicted coefficient of s^mu_3 from the leading symbol: % .6e' % K)
