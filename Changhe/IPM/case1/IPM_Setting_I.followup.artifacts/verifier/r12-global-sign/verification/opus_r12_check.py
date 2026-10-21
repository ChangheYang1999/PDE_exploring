# Independent check of the verifier's r12-global-sign proof (lead, 2026-10-20).
import sympy as sp, mpmath as mp
x, A = sp.symbols('x A', positive=True)
S = 6*A*(4*A-3)/(8*A-1); L = sp.sqrt(S); u = x/L
w = -A*x*(1-u**2)/(1+u**2); g = x**2/(1+u**2); h = A+1-sp.diff(w, x)
a2 = (sp.diff(g, x)-sp.diff(w, x, 2))/2; b3 = -sp.diff(a2, x)/3
F3 = -a2*sp.diff(g, x)-b3*g
G3 = 10*A*u**2/((8*A-1)*(1+u**2)**3)
res3 = sp.simplify(sp.together(w*sp.diff(G3, x)+(3*h-1)*G3-F3))
print('G3 identity residual:', res3)
a4 = (sp.diff(b3, x)+sp.diff(G3, x))/4; b5 = -sp.diff(a4, x)/5
F5 = -a2*sp.diff(G3, x)-3*b3*G3-a4*sp.diff(g, x)-b5*g
c0 = 2076*A**2+741*A-36; c2 = -3060*A**2+305*A-70; c4 = 1400*A**2-950*A+50
F5c = u**2*(c0+c2*u**2+c4*u**4)/(15*(4*A-3)*(8*A-1)*(1+u**2)**6)
print('F5 identity residual:', sp.simplify(sp.together(F5-F5c)))
# H_j'/H_j = (1 - j h)/w for j = 5
H5 = x**(10+sp.Rational(4,1)/A)*(1+u**2)**(-5)*(1-u**2)**(-4/A)
print('H5 log-derivative residual:', sp.simplify(sp.diff(sp.log(H5), x)-(1-5*h)/w))
# (2): integrand F5/(w H5) dx in u, compare with stated form
uu = sp.symbols('u', positive=True)
integ = sp.simplify((F5c/(w*H5)).subs(x, uu*L)*L)
p5 = 10+4/A
stated = -1/(15*A*(4*A-3)*(8*A-1)*L**p5)*uu**(1-p5)*(c0+c2*uu**2+c4*uu**4)*(1-uu**2)**(4/A-1)
print('integrand ratio (should be 1):', sp.simplify(integ/stated))
# (3) vs Beta continuation, and (4)
mp.mp.dps = 40
def B5_formula(Av):
    Av = mp.mpf(Av); Lv = mp.sqrt(6*Av*(4*Av-3)/(8*Av-1))
    P = 1248*Av**4-548*Av**3+297*Av**2-178*Av+84
    return P*mp.beta(-4-2/Av, 4/Av)/(15*Av*(2*Av-1)*(3*Av-2)*(4*Av-3)*(8*Av-1)*Lv**(10+4/Av))
def B5_beta_sum(Av):
    Av = mp.mpf(Av); Lv = mp.sqrt(6*Av*(4*Av-3)/(8*Av-1)); a = -4-2/Av; q = 4/Av
    c = [2076*Av**2+741*Av-36, -3060*Av**2+305*Av-70, 1400*Av**2-950*Av+50]
    FPint = sum(c[j]*mp.beta(a+j, q)/2 for j in range(3))
    return FPint/(15*Av*(4*Av-3)*(8*Av-1)*Lv**(10+4/Av))
def beta4(z):
    z = mp.mpf(z)
    return -mp.gamma(2-z)*mp.gamma(2*z)/mp.gamma(1+z)*(2-z)*(3-z)*(4-z)/((1+z)*(2+z)*(3+z)*(4+z))
for Av in ['1.25', '1.5', '3', '5', '10.150725214760579', '40']:
    f3, fs = B5_formula(Av), B5_beta_sum(Av)
    z = 2/mp.mpf(Av)
    Lv = mp.sqrt(6*mp.mpf(Av)*(4*mp.mpf(Av)-3)/(8*mp.mpf(Av)-1))
    print(Av, mp.nstr(f3, 15), mp.nstr(fs, 15), 'nat', mp.nstr(f3*Lv**(6+4/mp.mpf(Av)), 15),
          'beta4 check', mp.nstr(mp.beta(-4-z, 2*z)-beta4(z), 5))
# Direct numerical finite part at A = 10.150725214760579 (subtracting Taylor terms of (1-t)^(q-1) at t=0)
Av = mp.mpf('10.150725214760579'); a = -4-2/Av; q = 4/Av
def fp_euler(a, q, K=8):
    # FP int_0^1 t^(a-1) (1-t)^(q-1) dt by subtracting K Taylor terms at 0
    cs = [mp.binomial(q-1, k)*(-1)**k for k in range(K)]
    f = lambda t: t**(a-1)*((1-t)**(q-1)-sum(cs[k]*t**k for k in range(K)))
    return mp.quad(f, [0, mp.mpf(1)/2, 1]) + sum(cs[k]/(a+k) for k in range(K))
print('FP Euler vs Beta at a+j:', [mp.nstr(fp_euler(a+j, q)-mp.beta(a+j, q), 5) for j in range(3)])
P = lambda v: 1248*(1+v)**4-548*(1+v)**3+297*(1+v)**2-178*(1+v)+84
vv = sp.symbols('v'); print('P(1+v) =', sp.expand(1248*(1+vv)**4-548*(1+vv)**3+297*(1+vv)**2-178*(1+vv)+84))
print('limit z->1 of beta4:', mp.nstr(beta4(1+mp.mpf('1e-20')), 10))
