# independent check of ver 190 axis primitive: int_y^inf g_xx(0,s) ds = K(t(y)), d_y V2 = K
import mpmath as mp, sympy as sp
mp.mp.dps = 40
t, th, X, Y = sp.symbols('t theta x y', real=True)
P = sp.Rational(3, 2); Lc = sp.Rational(7, 5)
sig = (1+t)/2; w = (1-t)/2; Q = w + 2*P*sig
beta = [sp.Rational(1, 1) + t/3 - t**2/5, sp.Rational(-2, 7) + t/2, sp.Rational(1, 3) - t**3/4]
H = w*sum(sig**k*beta[k]*sp.cos(2*k*th) for k in range(3))
HA = sp.simplify(H.subs(th, sp.pi/2)); a = HA.subs(t, -1)
Jp = sum(k**2*(-1)**k*Q*sig**(k-1)*beta[k] for k in range(1, 3))
J = sp.integrate(Jp, (t, -1, t))
K = sp.expand(-HA - J.subs(t, 1) + J)
print('K(1)=', sp.simplify(K.subs(t, 1)), ' c_H=', sp.simplify(K.subs(t, -1)), ' -a-J(1)=', sp.simplify(-a-J.subs(t, 1)))
rfun = sp.lambdify(t, Lc*sp.sqrt(sig)/(2*w)**P, 'mpmath')
Hf = sp.lambdify((t, th), H, 'mpmath'); Kf = sp.lambdify(t, K, 'mpmath')
def tof(r):  # invert r(t) by monotone bisection
    lo, hi = mp.mpf(-1), mp.mpf(1)
    for _ in range(200):
        m = (lo+hi)/2
        if rfun(m) < r: lo = m
        else: hi = m
    return (lo+hi)/2
def g(x, y):
    r = mp.sqrt(x*x+y*y); return y*Hf(tof(r), mp.atan2(y, x))
def gxx0(y, h=mp.mpf('1e-6')):  # explicit central difference (mp.diff outran the fixed bisection precision)
    return (g(h, y)-2*g(0, y)+g(-h, y))/h**2
Hz_ = sp.lambdify((t, th), sp.diff(H, t)*4*sig*w/Q, 'mpmath'); Htt_ = sp.lambdify((t, th), sp.diff(H, th, 2), 'mpmath')
def gxx_polar(y):
    tt = tof(y); return (Hz_(tt, mp.pi/2)+Htt_(tt, mp.pi/2))/y
for y0 in [mp.mpf('0.3'), mp.mpf('2'), mp.mpf('15')]:
    I = mp.quad(gxx_polar, [y0, 10*y0, 100*y0, 1e4*y0, 1e6*y0, mp.inf])
    print('y=', y0, ' FD gxx =', mp.nstr(gxx0(y0), 12), ' polar gxx =', mp.nstr(gxx_polar(y0), 12),
          ' int_y^inf polar gxx =', mp.nstr(I, 12), ' K(t(y)) =', mp.nstr(Kf(tof(y0)), 12))
