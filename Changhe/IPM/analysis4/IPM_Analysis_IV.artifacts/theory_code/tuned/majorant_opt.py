# Sharper explicit disk for the Theorem T majorant system: numerical search for the critical z, then an exact
# rational supersolution check Phi(z1,Yhat) <= Yhat. Parameters per root: a=||f_1||_1=1+b (upper bound), kappa=28/3,
# sigma_* = certified lower bound for inf_k |sigma_k|.
import sympy as sp, sys
from fractions import Fraction as Fr
def system(a,kap,sig):
    z,W,U,V,E=sp.symbols('z W U V E')
    d=sp.Rational(3,2)*kap*a**2; e=3*kap*a*d; P=a*z+d*z**2+e*z**3; h=sp.Rational(3,2)
    Phi=[h*kap*(d**2+2*a*e+2*d*e*z+e**2*z**2)+3*kap*P*W+h*kap*z**4*W**2+kap*E*(P+z**4*W),
         h*kap*(2*d*e+e**2*z)+3*kap*sp.expand(P/z)*W+h*kap*z**3*W**2+kap*z**3*E*W,
         h*kap*(e**2+2*(d+e*z)*W+z**2*W**2)+kap*z**2*E*W+3*kap*a*U,
         (kap/sig)*(3*e*W+h*z*W**2+z*E*W+3*a*V+3*d*U)]
    return (z,W,U,V,E),[sp.expand(f) for f in Phi]
def fiter(F,zv,n=20000):
    Y=[0.0]*4
    for it in range(n):
        try: Yn=[f(zv,*Y) for f in F]
        except OverflowError: return None
        if max(Yn)>1e300 or any(x!=x for x in Yn): return None
        if max(abs(Yn[i]-Y[i])/(abs(Yn[i])+1e-300) for i in range(4))<1e-15: return Yn
        Y=Yn
    return None
for name,a,sig in [('b1',sp.Rational(12807,10000),sp.Rational(38,10**6)),('b2',sp.Rational(16464,10000),sp.Rational(15,10**4))]:
    kap=sp.Rational(28,3)
    syms,Phi=system(a,kap,sig)
    F=[sp.lambdify(syms,f,'math') for f in Phi]
    lo,hi=0.0,1.0
    for _ in range(200):
        mid=(lo+hi)/2
        if fiter(F,mid) is None: hi=mid
        else: lo=mid
    zc=lo
    for frac in [0.99,0.98,0.95,0.9]:
        z1=sp.Rational(zc*frac); z2=zc*(frac+1)/2
        Y2=fiter(F,z2,200000)
        if Y2 is None: print(name,'no fixed point at z2'); continue
        Yh=[sp.Rational(y)*(1+sp.Rational(1,10**12)) for y in Y2]
        sub=dict(zip(syms,[z1]+Yh))
        vals=[Phi[i].subs(sub) for i in range(4)]
        ok=all(vals[i]<=Yh[i] for i in range(4))
        print(name,'z_c=%.6e'%zc,'z1=%.6e (%.2f z_c)'%(float(z1),frac),'supersolution ok:',ok,
              'margins',[float(1-vals[i]/Yh[i]) for i in range(4)],'r > %.4e = 2^%.2f'%(float(z1)**-1.5, float(-1.5*sp.log(z1,2))),
              'Yhat',[float(y) for y in Yh])
        if ok: break
