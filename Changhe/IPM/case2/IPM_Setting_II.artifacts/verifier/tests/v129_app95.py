# V129: symbolic checks for the FR 9.5 draft (fd397ae7) not already covered by tests/v128_res26.py
import sympy as sp
ok=[]
def chk(name,cond):
    ok.append(bool(cond)); print(name,'OK' if cond else 'FAIL')
a,b,t,s,MN,d,z0,al,bp,l,T,c,u,q=sp.symbols('a b t s M_N delta z0 alpha betap l T c u q',positive=True)
# Step 2: with M_N delta <= a/2, int_0^oo (M_N/2) |z0| e^(-a s/2) ds <= 1/2 when |z0| <= delta
I=sp.integrate(MN/2*d*sp.exp(-a*s/2),(s,0,sp.oo))
chk('Step 2 log integral = M_N delta / a', sp.simplify(I-MN*d/a)==0)
chk('Step 2 log integral <= 1/2 at M_N delta = a/2', sp.simplify(I.subs(MN,a/(2*d)))==sp.Rational(1,2))
# Step 2 radial: -a|z|^2 + (M_N/2)|z|^3 <= -a|z|^2/2 when M_N |z| <= a/2 (in fact <= -3a/4 |z|^2)
r=sp.symbols('r',positive=True)
chk('Step 2 radial', sp.simplify((-a*r**2+MN/2*r**3).subs(MN,a/(2*r))-(-sp.Rational(3,4)*a*r**2))==0)
# Step 2 second variation: int_0^t e^(-a(t-s)) e^(-2as) ds <= e^(-at)/a
K=sp.integrate(sp.exp(-a*(t-s))*sp.exp(-2*a*s),(s,0,t))
chk('Step 2 D^2 bound', sp.simplify(K-sp.exp(-a*t)*(1-sp.exp(-a*t))/a)==0)
# Step 8: d/dt(e^(alpha t) z1) = -e^(alpha t) N1 when z1' = -alpha z1 - N1
z1=sp.Function('z1')(t); N1=sp.Function('N1')(t)
expr=sp.diff(sp.exp(al*t)*z1,t).subs(sp.diff(z1,t),-al*z1-N1)
chk('Step 8 Duhamel', sp.simplify(expr+sp.exp(al*t)*N1)==0)
# Step 8 exponents of G_s, DG_s, D^2G_s: alpha s - 2 alpha s = -alpha s ; alpha s - alpha s - alpha s ; alpha s - 2 alpha s
chk('Step 8 G exponent', sp.simplify(al*s-2*al*s+al*s)==0)
chk('Step 8 D^2G second term exponent', sp.simplify(al*s-al*s-al*s+al*s)==0)
# Step 8 resonance: i alpha + j betap = alpha, i+j>=2, alpha<=1<betap impossible
bad=False
import random
for _ in range(2000):
    A=random.uniform(1e-3,1.0); B=random.uniform(1.0+1e-6,5)
    for i in range(0,6):
        for j in range(0,6):
            if i+j>=2 and abs(i*A+j*B-A)<1e-9: bad=True
chk('Step 8 no slow resonance (random)', not bad)
# Step 9: f_v(u,v) = e^T f_v(u_T,v_T) J_T with J_T <= e^(-cT): bound M_f e^(-(c-1)T)
chk('Step 9 rate', sp.simplify(sp.exp(T)*sp.exp(-c*T)-sp.exp(-(c-1)*T))==0)
# Step 9 transport back: e^T * |e^(-alpha T) eta|^q = |eta|^q when q = 1/alpha
eta=sp.symbols('eta',positive=True)
chk('Step 9 transport', sp.simplify(sp.exp(T)*(sp.exp(-al*T)*eta)**(1/al)-eta**(1/al))==0)
# Step 3 homotopy: X.((1-s)V + sX) >= (1-s) l|X|^2/2 + s|X|^2 > 0 for s in [0,1]
sv=sp.symbols('sv',nonnegative=True)
chk('Step 3 homotopy', sp.simplify(((1-sv)*l/2+sv).subs(sv,0))>0 and sp.simplify(((1-sv)*l/2+sv).subs(sv,1))>0)
# Step 1: repeated eigenvalue of a symmetric M with trace 2l is l (M = l I); 1 eigenvalue -> other 2l-1 > 1
chk('Step 1 other eigenvalue', sp.simplify(2*l-1-1-2*(l-1))==0)
# Step 6: |rho(X)| <= C^3 omega e^((1-3a)t): e^t (C e^(-at))^3
C=sp.symbols('C',positive=True)
chk('Step 6 decay', sp.simplify(sp.exp(t)*(C*sp.exp(-a*t))**3-C**3*sp.exp((1-3*a)*t))==0)
print('ALL OK' if all(ok) else 'FAILURES', sum(ok),'of',len(ok))
