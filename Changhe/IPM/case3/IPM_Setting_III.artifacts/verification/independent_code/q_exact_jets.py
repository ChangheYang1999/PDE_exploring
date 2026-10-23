"""Rational canonical jets and exact axis samples for finite Q coefficients.

Proof written first: research/finite_q_exact_jets/PROOF.md.
No producer code or quadrature is used here.
"""
from fractions import Fraction as F
import math


def rational(x):
    return x if isinstance(x,F) else F(float(x))


def add(a,b):
    out=[F(0)]*max(len(a),len(b))
    for j,v in enumerate(a):out[j]+=v
    for j,v in enumerate(b):out[j]+=v
    return out


def scale(a,c):return [c*v for v in a]
def shift(a,n=1):return [F(0)]*n+list(a)


def chebyshev_in_sigma(cc):
    cc=list(map(rational,cc))
    if not cc:return [F(0)]
    old=[F(1)];out=scale(old,cc[0])
    if len(cc)==1:return out
    current=[F(-1),F(2)];out=add(out,scale(current,cc[1]))
    for c in cc[2:]:
        new=add(add(scale(current,-2),scale(shift(current),4)),scale(old,-1))
        out=add(out,scale(new,c));old,current=current,new
    return out


def value(poly,s):
    y=F(0)
    for v in reversed(poly):y=y*s+v
    return y


def derivative(poly):return [j*v for j,v in enumerate(poly)][1:] or [F(0)]


def beta_integral(poly,p=F(0)):
    """Integral of poly(s)*(1-s)^p for p>-1, by rational beta moments."""
    p=rational(p);assert p>-1
    moment=1/(p+1);ans=F(0)
    for k,v in enumerate(poly):
        if k:moment*=F(k)/(p+k+1)
        ans+=v*moment
    return ans


def jets(coeff,kappa,ell):
    coeff=[list(map(rational,row)) for row in coeff]
    kap=rational(kappa);ell=rational(ell);assert kap>1 and ell>1 and coeff
    pol=[chebyshev_in_sigma(row) for row in coeff]+[[F(0)]]*4
    center=lambda j:sum(((-1)**k*v for k,v in enumerate(coeff[j])),F(0)) if j<len(coeff) else F(0)
    a=center(0);d0=sum(((-1)**(j+1)*j*j*v for j,v in enumerate(coeff[0])),F(0))
    bc=2*d0-a+center(1);ec=2*d0-a-center(1)
    third=add(pol[1],scale(shift(pol[2]),-1))
    third=scale(add(third,scale(shift(third),2*kap-1)),F(1,4))
    c=-a/4+beta_integral(third)
    fifth=add(pol[2],scale(shift(pol[3]),-1))
    harmonic=add(fifth,scale(shift(fifth),2*kap-1))
    Hc=-center(1)/4+beta_integral(harmonic,2*kap)
    q1=(Hc-bc/3)/2;q2=-(Hc+bc/3)/2;A=2*ell-1;delta=ell+c-1
    minus=[F(0)];plus=[F(0)]
    for j,row in enumerate(pol[:len(coeff)]):
        plus=add(plus,shift(row,j));minus=add(minus,scale(shift(row,j),(-1)**j))
    minus=add(minus,scale(shift(minus),-1));plus=add(plus,scale(shift(plus),-1))
    return dict(a=a,c=c,ell=ell,kappa=kap,delta=delta,b_core=bc,e_core=ec,H_core=Hc,q1_core=q1,q2_core=q2,
                poisson=q1+q2+bc/3,
                profile_T1_core=2*A*bc+3*a*q1,profile_T2_core=2*ec+a*q2,
                actual_R_x2y_core=(3*ell-c-1)*bc+3*a*q1,
                actual_R_y3_core=(3*ell+3*c-1)*ec+a*q2,
                jet_elimination_core=6*ec-(a-2*A)*bc,
                a_b_core=a*bc,a_e_core=a*ec,
                axis_minus_polynomial=minus,axis_plus_polynomial=plus)


def axis_gradient(jet,s):
    s=rational(s);assert 0<s<1
    fm=jet['axis_minus_polynomial'];fp=jet['axis_plus_polynomial'];kap=jet['kappa']
    speed=2*s*(1-s)/(1-s+2*kap*s)
    return value(fm,s)+speed*value(derivative(fm),s),value(fp,s)


def pack(v):
    if isinstance(v,F):return {'exact':str(v),'approx':float(v)}
    if isinstance(v,dict):return {k:pack(x) for k,x in v.items()}
    if isinstance(v,list):return [pack(x) for x in v]
    return v
