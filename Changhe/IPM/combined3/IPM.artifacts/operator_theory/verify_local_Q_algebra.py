#!/usr/bin/env python3
"""Exact polynomial/Gaussian verification of all local-Q energy signs.

This verifies algebra independently of radial numerics. It is not an
actual-center coefficient or stationary-existence certificate.
"""
from fractions import Fraction as F
from pathlib import Path
import json,math

class P:
    def __init__(self,value=0):
        if isinstance(value,P):self.d=dict(value.d)
        elif isinstance(value,dict):self.d={k:F(v) for k,v in value.items() if v}
        else:self.d={} if not value else {(0,0):F(value)}
    def __add__(self,b):
        out=dict(self.d)
        for k,v in P(b).d.items():out[k]=out.get(k,F(0))+v
        return P(out)
    __radd__=__add__
    def __neg__(self):return P({k:-v for k,v in self.d.items()})
    def __sub__(self,b):return self+-P(b)
    def __rsub__(self,b):return P(b)+-self
    def __mul__(self,b):
        out={}
        for (i,j),v in self.d.items():
            for (k,l),z in P(b).d.items():
                key=i+k,j+l;out[key]=out.get(key,F(0))+v*z
        return P(out)
    __rmul__=__mul__
    def __pow__(self,n):
        out=P(1)
        for _ in range(n):out=out*self
        return out
    def D(self,axis):
        out={}
        for (i,j),v in self.d.items():
            n=i if axis==0 else j
            if n:out[i-(axis==0),j-(axis==1)]=n*v
        return P(out)
    def __eq__(self,b):return self.d==P(b).d
    def integral_pi(self):
        # Integral P(x,y) exp(-x²-y²) dxdy divided by pi.
        ans=F(0)
        for (i,j),v in self.d.items():
            if i%2 or j%2:continue
            m,n=i//2,j//2
            ans+=v*F(math.factorial(2*m),4**m*math.factorial(m))*F(math.factorial(2*n),4**n*math.factorial(n))
        return ans

x=P({(1,0):1});y=P({(0,1):1});X=[x,y]
def grad(p):return [p.D(0),p.D(1)]
def lap(p):return p.D(0).D(0)+p.D(1).D(1)
def hess(p):return [[p.D(i).D(j) for j in range(2)] for i in range(2)]
def inner(v,z):return sum((v[i]*z[i] for i in range(2)),P())
def contract(A,B):return sum((A[i][j]*B[i][j] for i in range(2) for j in range(2)),P())
def quad(A,v):return contract(A,[[v[i]*v[j] for j in range(2)] for i in range(2)])
def trace(A):return A[0][0]+A[1][1]
def cof(A):return [[A[1][1],-A[0][1]],[-A[1][0],A[0][0]]]
def div(v):return sum((v[i].D(i) for i in range(2)),P())
def divdiv(A):return sum((A[i][j].D(i).D(j) for i in range(2) for j in range(2)),P())
def addm(A,B):return [[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]
def scalarm(v):return [[P(v) if i==j else P() for j in range(2)] for i in range(2)]
def smul(v,A):return [[v*A[i][j] for j in range(2)] for i in range(2)]
def Gder(p,i):return p.D(i)-X[i]*p

def main():
    c=F(4076476460239181,2251799813685248);q=F(21,10);omega=F(25,16);beta=F(7,10)
    w=P(1)+omega*(x*x+y*y)
    phi=F(1,2)*x*x*y+F(1,4)*x**4*y+F(1,2)*x*x*y**3+F(1,5)*x*x*y**5
    rho=-lap(phi);u=[-phi.D(0).D(1),phi.D(0).D(0)]
    assert div(u)==0
    Lu=[lap(v) for v in u]
    assert Lu[0]==rho.D(0).D(1) and Lu[1]==-rho.D(0).D(0)
    S=[[F(1,2)*(u[j].D(i)+u[i].D(j)) for j in range(2)] for i in range(2)]
    K=[[-rho.D(1),F(1,2)*rho.D(0)],[F(1,2)*rho.D(0),P()]]
    D=(c+1)*w+omega*(c*(x*x+y*y)+inner(u,X))
    C=addm(scalarm(D-q*c*w),smul(-w,addm(smul(q,S),K)))
    v=[F(1,2)*w*z for z in Lu];dv=div(v)
    Dv=[[F(1,2)*(v[j].D(i)+v[i].D(j)) for j in range(2)] for i in range(2)]
    E1=addm(smul(F(1,2),cof(hess(trace(C)))),smul(q,addm(scalarm(F(1,2)*dv),smul(-1,Dv))))
    E0=F(1,2)*divdiv(addm(C,scalarm(D)))+q*F(1,2)*dv
    E0_simple=omega*(P(2*(4*c+2-q*c))+P(1-q/F(2))*inner(X,Lu)+rho.D(1)+x*rho.D(0).D(1)-y*rho.D(0).D(0))
    assert E0==E0_simple
    fp=y*(P(1)+2*x*x-3*y*y+F(1,5)*x**4)
    df=[Gder(fp,i) for i in range(2)]
    H=[[Gder(df[j],i) for j in range(2)] for i in range(2)]
    lf=trace(H);hp=fp-lf
    # Raw local equation, with the identical lower b·Uf term omitted.
    raw=-(D-q*c*w)*hp*hp-q*c*w*fp*hp-w*hp*contract(K,H)
    raw+=-q*w*hp*contract(S,H)-q*hp*inner(v,df)
    local=-sum((quad(C,H[k]) for k in range(2)),P())
    local+=-quad(addm(C,scalarm(D)),df)-D*fp*fp+quad(E1,df)+E0*fp*fp
    assert raw.integral_pi()==local.integral_pi()
    Q=w*hp*hp
    jet=w*(contract(H,H)+2*inner(df,df)+fp*fp)-2*omega*inner(df,df)-4*omega*fp*fp
    assert Q.integral_pi()==jet.integral_pi()
    cayley=lf*contract(C,H)-sum((quad(C,H[k]) for k in range(2)),P())-trace(C)*(H[0][0]*H[1][1]-H[0][1]*H[1][0])
    assert cayley==0
    # Independent full-PDE check at q=2, where every multiplier is local.
    # Choose g=-Delta(Phi_test), so U[g] is an exact Gaussian derivative.
    pt=y*(P(1)+F(1,3)*x*x-F(1,5)*y*y)
    gp=-sum((Gder(Gder(pt,i),i) for i in range(2)),P())
    UG=[-Gder(Gder(pt,0),1),Gder(Gder(pt,0),0)]
    dg=[Gder(gp,i) for i in range(2)]
    Hg=[[Gder(dg[j],i) for j in range(2)] for i in range(2)]
    hh=gp-trace(Hg);bb=grad(rho);V=[c*X[i]+u[i] for i in range(2)]
    Lg=inner(V,dg)-gp+inner(bb,UG)
    J2Lg=Lg-sum((Gder(Gder(Lg,i),i) for i in range(2)),P())
    direct=w*hh*J2Lg
    C2=addm(scalarm(D-2*c*w),smul(-w,addm(smul(2,S),K)))
    Ec1=addm(smul(F(1,2),cof(hess(trace(C2)))),smul(2,addm(scalarm(F(1,2)*dv),smul(-1,Dv))))
    Ec0=F(1,2)*divdiv(addm(C2,scalarm(D)))+dv
    loc2=-sum((quad(C2,Hg[k]) for k in range(2)),P())
    loc2+=-quad(addm(C2,scalarm(D)),dg)-D*gp*gp+quad(Ec1,dg)+Ec0*gp*gp
    Uh=[UG[0]-Hg[0][1],UG[1]+Hg[0][0]]
    src=inner(bb,UG)
    Cb=src-sum((Gder(Gder(src,i),i) for i in range(2)),P())-inner(bb,Uh)
    assembled=loc2+w*hh*inner(bb,UG)+w*hh*Cb
    assert direct.integral_pi()==assembled.integral_pi()
    out={'status':'EXACT_LOCAL_Q_ALGEBRA_CHECK_PASS','arithmetic':'fractions; exact Gaussian moments divided by pi',
         'q':str(q),'c':str(c),'weight_omega':str(omega),'test_potential':'x²y/2+x⁴y/4+x²y³/2+x²y⁵/5',
         'test_f':'y(1+2x²−3y²+x⁴/5)exp(−r²/2)',
         'raw_energy_over_pi':str(raw.integral_pi()),'local_energy_over_pi':str(local.integral_pi()),
         'Q_squared_over_pi':str(Q.integral_pi()),'jet_identity_over_pi':str(jet.integral_pi()),
         'q2_direct_PDE_energy_over_pi':str(direct.integral_pi()),'q2_complete_local_assembly_over_pi':str(assembled.integral_pi()),
         'checks':['div u=0','Delta u=(rho_xy,−rho_xx)','Cayley–Hamilton pointwise identity','complete local energy with integrated v term','exact E0 simplification','quadratic-weight norm identity','direct full PDE energy equals complete source/transport local assembly at q=2'],
         'scope':'independent algebra regression; actual-center coefficient bounds and stationary existence NOT CLAIMED'}
    dest=Path(__file__).resolve().parent/'local_Q_algebra_result.json';dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
