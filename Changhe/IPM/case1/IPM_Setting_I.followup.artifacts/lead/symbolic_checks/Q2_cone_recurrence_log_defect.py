# Independent check of a referee answer, part 5: cone reduction (5.1) and the Q_2 compatibility defect -1/120.
import sympy as sp
s,y,z=sp.symbols('s y z',real=True)
r=sp.symbols('r',positive=True)
A,g,p=sp.Rational(2),sp.Integer(5),sp.Integer(5)
N=13
ph=sp.symbols('ph1:%d'%(N+1)); be=sp.symbols('be1:%d'%(N+1)); al=sp.symbols('al0:%d'%(N+1))
phi=sum(ph[j-1]*z**j for j in range(1,N+1,2))
beta=sum(be[j-1]*z**j for j in range(1,N+1,2))
alpha=sum(al[j]*z**j for j in range(0,N+1,2))
# fields on s<0: r=-s, z=y/r
R_=-s
def lift(F): return R_**p*F.subs(z,y/R_)
w=lift(phi); B1=lift(alpha); B2=lift(beta)
# Q_2 and its velocity (2.2), d=3, on s<0
Rr=sp.sqrt(s**2+y**2)
v=(s/2)*(y*Rr+s**2*sp.asinh(y/(-s)))
d=3
V1=Rr**(d-2)*((d+1)*s**2+y**2)/(d*(d+2))
V2=-v+y*sp.diff(v,y)/(d+2)
# check frozen equations for v,V on s<0 at a sample point
chk=[sp.diff(V1,s)+sp.diff(V2,y), sp.diff(V2,s)-sp.diff(V1,y)+sp.diff(v,s), A*s*sp.diff(v,s)+y*sp.diff(v,y)-v+g*V2]
pt={s:-sp.Rational(3,7),y:sp.Rational(2,9)}
print('frozen checks', [sp.N(c.subs(pt),20) for c in chk])
h0=-(V1*sp.diff(v,s)+V2*sp.diff(v,y))
# h0 on cone: s=-r, y=r z ; expect r^5 H(z)
H=sp.simplify(h0.subs({s:-r,y:r*z})/r**5)
Hs=sp.series(H,z,0,N+1).removeO()
print('H series', sp.expand(Hs))
eqs=[]
E1=A*s*sp.diff(w,s)+y*sp.diff(w,y)-w+g*B2
E2=sp.diff(B1,s)+sp.diff(B2,y)
E3=sp.diff(B2,s)-sp.diff(B1,y)+sp.diff(w,s)
for E,src in [(E1,Hs),(E2,0),(E3,0)]:
    e=sp.expand(sp.simplify(E.subs({s:-r,y:r*z})/r**(p-1 if E is not E1 else p)) - (src if E is E1 else 0))
    pe=sp.Poly(sp.expand(e),z)
    for (k,),c in pe.terms():
        if k<=N-2: eqs.append(c)
pass
sol=sp.solve(eqs,list(ph)+list(be)+list(al),dict=True)
print('solutions found:',len(sol))
# find where inconsistency arises: solve truncated systems of increasing order
for K in range(1,N-1,2):
    sub=[]
    for E,src,sh in [(E1,Hs,p),(E2,0,p-1),(E3,0,p-1)]:
        e=sp.expand(sp.simplify(E.subs({s:-r,y:r*z})/r**sh) - src)
        pe=sp.Poly(e,z)
        sub+= [c for (k,),c in pe.terms() if k<=K]
    pass
    so=sp.solve(sub,list(ph)+list(be)+list(al),dict=True)
    print('order',K,'consistent' if so else 'INCONSISTENT')
