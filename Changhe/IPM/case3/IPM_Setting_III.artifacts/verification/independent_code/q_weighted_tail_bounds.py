"""Exact rational coefficient bounds for weighted tails of a finite Q density.

Mathematical derivation was written first in research/finite_q_weighted_tails.
These bounds do not certify annular quadrature.
"""
from fractions import Fraction as F
import math


def endpoint_division(coeff):
    r=[F(float(v)) for v in coeff]
    a=sum((v*(-1)**j for j,v in enumerate(r)),F(0))
    r[0]-=a;q=[F(0) for _ in r[:-1]]
    for j in range(len(r)-1,1,-1):
        v=2*r[j];q[j-1]+=v;r[j]=F(0);r[j-1]-=v;r[j-2]-=v/2
    if len(r)>1:q[0]+=r[1];r[0]-=r[1];r[1]=F(0)
    assert not any(r)
    return a,q


def constants(coeff,kappa,ell):
    coeff=[[F(float(v)) for v in row] for row in coeff]
    M=len(coeff);kap=F(float(kappa));ell=F(float(ell));a,q=endpoint_division(coeff[0])
    C=[sum(map(abs,row),F(0)) for row in coeff]+[F(0),F(0)]
    Cp=[sum((j*j*abs(v) for j,v in enumerate(row)),F(0)) for row in coeff]+[F(0),F(0)]
    CQ=sum(map(abs,q),F(0))
    H=[2*CQ+abs(a)+C[1]/2]+[(C[j]+C[j+1])/2 for j in range(1,M)]+[F(0)]
    G=[abs(a)+C[0]+C[1]/2]+H[1:]
    D=[2*C[0]+4*Cp[0]+C[1]+2*Cp[1]]+[(j+1)*(C[j]+C[j+1])+2*Cp[j]+C[j+1]+2*Cp[j+1] for j in range(1,M)]
    An=[H[j]/(2*j+6) for j in range(M)]
    Bn=[H[1]/2]+[H[j+1]*F(j+1,2*j) for j in range(1,M)]
    Ag=[G[j]/(2*j+4) for j in range(M)]
    Bg=[(C[1]+C[2])*(1+2*kap)/8]+[G[j+1]/(2*j) for j in range(1,M)]
    velocity=lambda aa,bb,hh:(sum(((j+1)*(aa[j]+bb[j]) for j in range(M)),F(0)),
                             sum(((2*(j+1)*(aa[j]+bb[j])+hh[j]+hh[j+1])/2 for j in range(M)),F(0)))
    vrn,vtn=velocity(An,Bn,H);vrg,vtg=velocity(Ag,Bg,G)
    Hs=sum(H,F(0));Gs=sum(G,F(0));Ds=sum(D,F(0))
    Ht=sum(((2*j+1)*v for j,v in enumerate(H)),F(0));Gt=sum(((2*j+1)*v for j,v in enumerate(G)),F(0))
    cg=abs(a)/4+Bg[0]
    Fn=(ell+cg+vrn)*(Hs+Ds)+(cg+vtn)*Ht+Hs+abs(a)*(vrn+vtn)
    Fg=(ell+cg+vrg)*(Gs+Ds)+(cg+vtg)*Gt+Gs+abs(a)*(vrg+vtg)
    return dict(a=a,ell=ell,kappa=kap,C=C,Cprime=Cp,Cquotient=CQ,H=H,G=G,D=D,
                Hsum=Hs,Gsum=Gs,Dsum=Ds,Htheta=Ht,Gtheta=Gt,
                near_A=An,near_B=Bn,global_A=Ag,global_B=Bg,
                near_Vr=vrn,near_Vtheta=vtn,global_Vr=vrg,global_Vtheta=vtg,
                c_upper=cg,Fnear=Fn,Fglobal=Fg)


def dyadic_exp_upper(t):
    t=F(t);assert t>=0
    n=t.numerator//t.denominator
    return F(1,1<<n)


def tails(c,m,z0,z1):
    m=F(m);z0=F(z0);z1=F(z1)
    assert 2<m<4 and z0<=0<=z1
    low=8-2*m;high=2*m-4
    lfactor=7*dyadic_exp_upper(-low*z0)/low
    hfactor=7*dyadic_exp_upper(high*z1)/high
    return dict(h_lower=lfactor*c['Hsum']**2,F_lower=lfactor*c['Fnear']**2,
                h_upper=hfactor*c['Gsum']**2,F_upper=hfactor*c['Fglobal']**2)


def serialize(value):
    if isinstance(value,F):return {'fraction':str(value),'float':float(value)}
    if isinstance(value,dict):return {k:serialize(v) for k,v in value.items()}
    if isinstance(value,list):return [serialize(v) for v in value]
    return value
