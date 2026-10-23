# Symbolic checks (verifier, independent): origin relation, scaling, manufactured canonical pairs.
import sympy as sp
x,y,r,lam,cl,a0 = sp.symbols('x y r lambda c_l a0', real=True)
# 1. Manufactured canonical pair: rho = d_y F(r), psi = -d_x d_y H(r), Lap H = F.
g = sp.Rational(1,2)  # growth exponent gamma
F = a0*(1+r**2)**((g+1)/2)/(g+1)
Ip = sp.integrate(sp.expand(r*F), (r,0,r)) if False else None
s = sp.symbols('s', positive=True)
I = sp.integrate(s*F.subs(r,s), (s,0,r))
I = sp.simplify(I)
Hp = I/r              # H'(r)
R = sp.sqrt(x**2+y**2)
Hfun_p = Hp.subs(r,R)
# H as function of x,y: build derivatives using chain rule via H'(r)
# d_x H = H'(r) x/r ; d_y d_x H = d_y (H'(r) x / r)
dxH = Hfun_p*x/R
psi = -sp.diff(dxH, y)
rho = sp.diff(F.subs(r,R), y)
lap = sp.diff(psi,x,2)+sp.diff(psi,y,2)
chk = sp.simplify((-lap - sp.diff(rho,x)).subs({x:sp.Rational(3,7), y:sp.Rational(-5,11), a0:1}))
print('Poisson check at a point:', sp.N(chk, 20))
# psi_xy(0) by limit along a path
pxy = sp.diff(psi,x,y)
val = sp.N(pxy.subs({x:sp.Rational(1,10**6), y:sp.Rational(1,10**6)*sp.Rational(3,7), a0:1}), 15)
print('psi_xy near 0 (a0=1):', val, ' expected -a0/4 = -0.25')
# growth of U: psi/r^2 -> 0 ?
for Rv in [10**2, 10**4, 10**6]:
    v = sp.N((psi/(x**2+y**2)).subs({x:Rv*sp.Rational(3,5), y:Rv*sp.Rational(4,5), a0:1}))
    print('psi/r^2 at r=',Rv, v)
# 2. scaling: rho_l(X)=l rho(X/l), psi_l = l^2 psi(X/l) satisfies -Lap psi_l = d_x rho_l
rl = lam*rho.subs({x:x/lam, y:y/lam}, simultaneous=True)
pl = lam**2*psi.subs({x:x/lam, y:y/lam}, simultaneous=True)
chk2 = (-(sp.diff(pl,x,2)+sp.diff(pl,y,2)) - sp.diff(rl,x)).subs({x:sp.Rational(2,3), y:sp.Rational(1,5), lam:sp.Rational(7,3), a0:1})
print('scaling Poisson check:', sp.N(chk2, 20))
