# lead check of the corollary of the verifier's seventh-order resonance proof: general-L identities
import sympy as sp
x, A, L = sp.symbols('x A L', positive=True)
u = x/L
w = -A*x*(1-u**2)/(1+u**2); g = x**2/(1+u**2); h = A+1-sp.diff(w, x)
print('w g\' - (w\'-A) g =', sp.simplify(w*sp.diff(g, x) - (sp.diff(w, x)-A)*g))
a2 = (sp.diff(g, x)-sp.diff(w, x, 2))/2; b3 = -sp.diff(a2, x)/3
F3 = -a2*sp.diff(g, x) - b3*g
F3c = -u**2*((6*A+3*L**2)*u**2 + 5*L**2 - 30*A)/(3*(1+u**2)**4)
print('F3 - claimed =', sp.simplify(F3 - F3c))
S = 6*A*(4*A-3)/(8*A-1)
br = 5*L**2-30*A+(6*A+3*L**2)*(2*A+1)/(2*A-1)
print('bracket - 2(8A-1)(L^2-S)/(2A-1) =', sp.simplify(br - 2*(8*A-1)*(L**2-S)/(2*A-1)))
# numeric FP check of B_3 at A=3, L=1.7 against closed form
import mpmath as mp
mp.mp.dps = 30
Av, Lv = mp.mpf(3), mp.mpf('1.7')
a = -2-1/Av; q = 2/Av
closed = -(8*Av-1)*mp.beta(a, q)/(3*Av*(2*Av-1))*Lv**(-4-2/Av)*(1-6*Av*(4*Av-3)/(8*Av-1)/Lv**2)
# direct: B3 = -1/(3A L^(6+2/A)) FP int_0^1 u^(-5-2/A) [(6A+3L^2)u^2+5L^2-30A](1-u^2)^(q-1) du ; t=u^2
f = lambda t: ((6*Av+3*Lv**2)*t + 5*Lv**2-30*Av)*(1-t)**(q-1)
# FP int_0^1 t^(a-1) f(t) dt /2 : subtract Taylor of f to order 2 (t^(a-1+n), a+n<0 for n=0,1,2)
N = 3
cs = mp.taylor(f, 0, N-1)
def rem(t): return t**(a-1)*(f(t)-sum(cs[n]*t**n for n in range(N)))
I = mp.quad(rem, [0, mp.mpf('0.5')]) + mp.quad(lambda t: t**(a-1)*f(t), [mp.mpf('0.5'), 1]) \
    + sum(cs[n]*mp.mpf('0.5')**(a+n)/(a+n) for n in range(N))
direct = -1/(3*Av*Lv**(6+2/Av))*I/2
print('B3 closed', closed, 'direct', direct, 'C_A>0:', -(8*Av-1)*mp.beta(a, q)/(3*Av*(2*Av-1)) > 0)
# series version of the finite part (no cancellation): f = (al t + be)(1-t)^(q-1)
al, be = 6*Av+3*Lv**2, 5*Lv**2-30*Av
def cbin(n): return mp.binomial(q-1, n)*(-1)**n
c = [be*cbin(0)] + [be*cbin(n) + al*cbin(n-1) for n in range(1, 400)]
t0 = mp.mpf('0.5')
I2 = sum(c[n]*t0**(a+n)/(a+n) for n in range(400)) + mp.quad(lambda t: t**(a-1)*f(t), [t0, 1])
print('B3 direct (series)', -1/(3*Av*Lv**(6+2/Av))*I2/2)
