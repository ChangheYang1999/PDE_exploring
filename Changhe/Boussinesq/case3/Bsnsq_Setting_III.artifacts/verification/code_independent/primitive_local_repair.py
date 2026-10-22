"""Exact finite-jet projection, packet132. Pure rational arithmetic when supplied."""
from fractions import Fraction as Q

def residual_coefficients(beta,a0,jet):
    l1=(beta-2)/2;l2=(3*beta+2)/2
    p,q,d,e,f,g,h=[jet.get(k,0)for k in [(3,0),(1,2),(3,1),(1,3),(5,0),(3,2),(1,4)]]
    b0=4*a0/beta;b1=-6*d-6*e;b20=-20*f-2*g;b02=-6*g-12*h
    a1=((2*beta+1)*b1-2*q*b0)/2
    a20=((3*l1+1)*b20-d*b0+3*p*b1)/4
    a02=((l1+2*l2+1)*b02-q*b1-3*e*b0)/2
    return {(2,1):l2*a1-4*q*a0,(4,0):2*l1*a20-2*d*a0+3*p*a1,(2,2):2*l2*a02-6*e*a0-3*q*a1}

def project(beta,a0,jet):
    """Return leading K4,K50,K52 coefficients and the corrected degree-five jet."""
    beta=Q(beta);a0=Q(a0);jet={k:Q(v)for k,v in jet.items()};l1=(beta-2)/2;l2=(3*beta+2)/2
    if beta<=2:raise ValueError('beta>2 required')
    if jet.get((1,1),0)!=1+beta/2 or -6*jet.get((3,0),0)-2*jet.get((1,2),0)!=4*a0/beta:raise ValueError('exact center constraints required')
    before=residual_coefficients(beta,a0,jet);e=before[(2,1)]/(3*l2*(2*beta+1));jet[(1,3)]=jet.get((1,3),0)+e
    mid=residual_coefficients(beta,a0,jet);f=mid[(4,0)]/(10*l1*(3*l1+1));h=mid[(2,2)]/(12*l2*(l1+2*l2+1))
    jet[(5,0)]=jet.get((5,0),0)+f;jet[(1,4)]=jet.get((1,4),0)+h
    assert all(v==0 for v in residual_coefficients(beta,a0,jet).values())
    return (e,f,h),jet
