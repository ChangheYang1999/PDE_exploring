# Lead cross-review of verifier topic76 (two-series global portrait): the Euclidean radial identity (1)-(3), the elliptical
# radius variant, and the origin limit. Symbolic with generic quadratic P_j and exponent p.
import sympy as sp, json, time
t0=time.time()
s,z,a,c,p=sp.symbols('s z a c p',positive=True)
Q,T=sp.symbols('Q T',positive=True)
coef=sp.symbols('b0:12')
def Pj(v,w,off):
    b=coef[off:off+6]
    return b[0]+b[1]*v+b[2]*w+b[3]*v**2+b[4]*v*w+b[5]*w**2
u=1+a*s+z**2; v=a*s/u; w=z**2/u
phi=z*sum(u**(-j*p)*Pj(v,w,6*(j-1)) for j in (1,2))
Wr_over_r=c-sp.diff(phi,z)
Wz=c*z+2*phi+2*s*sp.diff(phi,s)
lhs=(s*Wr_over_r+z*Wz)/(s+z**2)      # W . x / R^2 with r^2 = s
V,Wv=sp.symbols('V Wv')
def N(j):
    P=Pj(V,Wv,6*(j-1))
    expr=((2*a+1)*T-1)*P+2*Q*T*(1-T)*(-j*p*(a-1)*P+(a-(a-1)*V)*sp.diff(P,V)-(1+(a-1)*Wv)*sp.diff(P,Wv))
    return expr.subs({V:Q*(1-T),Wv:Q*T})
D=1+(a-1)*T
rhs=(c*D+(1-Q)**p*N(1)+(1-Q)**(2*p)*N(2))/D
# substitute s = x(1-T)/a, z^2 = x T with x = Q/(1-Q); evaluate at random rational points (p kept symbolic is heavy; use values)
import random
random.seed(1)
maxdiff=0.0
for k in range(12):
    vals={a:sp.Rational(random.randint(1,40),10),c:sp.Rational(random.randint(51,74),100),p:sp.Rational(random.randint(67,99),100)}
    for b in coef: vals[b]=sp.Rational(random.randint(-30,30),7)
    Qv=sp.Rational(random.randint(1,99),100); Tv=sp.Rational(random.randint(1,99),100)
    x=Qv/(1-Qv); sv=x*(1-Tv)/vals[a]; zv=sp.sqrt(x*Tv)
    L=lhs.subs(vals).subs({s:sv,z:zv}); R=rhs.subs(vals).subs({Q:Qv,T:Tv})
    maxdiff=max(maxdiff,abs(float(sp.N(L-R,40))))
# elliptical radius variant: W . grad log sqrt(x), x = a s + z^2; grad of x in (r, z) is (2 a r, 2 z)
xx=a*s+z**2
lhs_e=(a*s*Wr_over_r+z*Wz)/xx
def Ne(j):
    P=Pj(V,Wv,6*(j-1))
    return ((3*T-1)*P+2*Q*T*(1-T)*(sp.diff(P,V)-sp.diff(P,Wv))).subs({V:Q*(1-T),Wv:Q*T})
rhs_e=c+(1-Q)**p*Ne(1)+(1-Q)**(2*p)*Ne(2)
maxdiff_e=0.0
for k in range(12):
    vals={a:sp.Rational(random.randint(1,40),10),c:sp.Rational(random.randint(51,74),100),p:sp.Rational(random.randint(67,99),100)}
    for b in coef: vals[b]=sp.Rational(random.randint(-30,30),7)
    Qv=sp.Rational(random.randint(1,99),100); Tv=sp.Rational(random.randint(1,99),100)
    x=Qv/(1-Qv); sv=x*(1-Tv)/vals[a]; zv=sp.sqrt(x*Tv)
    L=lhs_e.subs(vals).subs({s:sv,z:zv}); R=rhs_e.subs(vals).subs({Q:Qv,T:Tv})
    maxdiff_e=max(maxdiff_e,abs(float(sp.N(L-R,40))))
# origin limit with P1(0,0)+P2(0,0)=1/2: ratio at Q=0 is (c D + ((2a+1)T-1)/2)/D -> c-1/2 at T=0 and c+1 at T=1
lim=sp.simplify((c*D+((2*a+1)*T-1)*sp.Rational(1,2))/D)
out={'euclidean_identity_maxdiff_12pts':maxdiff,'elliptical_identity_maxdiff_12pts':maxdiff_e,
     'origin_ratio_T0':str(sp.simplify(lim.subs(T,0))),'origin_ratio_T1':str(sp.simplify(lim.subs(T,1))),
     'seconds':time.time()-t0}
json.dump(out,open('checks/topic76_radial_check_output.json','w'),indent=1)
print(out)
