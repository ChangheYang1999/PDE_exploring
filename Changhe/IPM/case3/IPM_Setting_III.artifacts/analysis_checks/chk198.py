# Lead check of the second-cusp coefficient C_d(h) (checker's trace result) by direct quadrature
import mpmath as mp, sympy as sp
mp.mp.dps=40
s,P=sp.symbols('s p',positive=True)
def Cd_direct(pv):
    d=2*pv-1; C=mp.mpf(1)/(pv+2); D=1/pv-1; A=C**2/D; beta=pv*(pv+2)
    pr=sp.Rational(str(pv)) if False else sp.nsimplify(pv)
    dd=2*pr-1; Cs=1/(pr+2); Ds=1/pr-1; As=Cs**2/Ds; bs=pr*(pr+2)
    F=-As*s*(1+s**2)**(pr-3)*(3+2*bs*s**2+bs*s**4)
    q=dd*(dd-1)*F-2*(dd-1)*s*sp.diff(F,s)+s**2*sp.diff(F,s,2)
    # Q: coefficient of s^{d-2} in q at infinity
    Qh=sp.limit(q/s**(dd-2),s,sp.oo)
    f=sp.lambdify(s,s*(q-Qh*s**(dd-2)),'mpmath')
    Sc=mp.mpf(10)**8; I=mp.quad(f,[0,1,10,100,1e4,1e6,Sc]); I+=f(Sc)*Sc/(2-d)  # tail ~ c s^{d-3}
    Jd=mp.quad(lambda t:(1+t**2)**((d-3)/2),[0,1,mp.inf])
    form1=-A*Jd*(beta*(1-d**2)/d+(3-beta)*(d+1)*(d+2)/(3-d))
    form2=-3*pv**2*(4*pv**2+5*pv-1)*Jd/((pv+2)**2*(2*pv-1)*(2-pv))
    QhF=float(Qh); Qclaim=A*beta*(1-d)
    return I,form1,form2,QhF,Qclaim
for pv in (0.6,0.75,0.9):
    I,f1,f2,Qh,Qc=Cd_direct(pv)
    print(pv,mp.nstr(I,15),mp.nstr(f1,15),mp.nstr(f2,15),'rel',mp.nstr(abs(I-f1)/abs(f1),3),'Q_h',Qh,float(Qc))
# transport factors
p=sp.symbols('p',positive=True); c=1/p
print(sp.simplify(c*(2*p-1)-1+(c-1)), sp.simplify(c*(3*p-2)-1+2*(c-1)))
# cusp quotient check for V_2[h] at fixed y by direct evaluation of the canonical formula at small x
