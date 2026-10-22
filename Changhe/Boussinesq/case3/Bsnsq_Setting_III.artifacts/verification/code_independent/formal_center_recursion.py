"""Own packet119 formal recursion, using rational bivariate polynomials.

No lead or NUM implementation is imported. The final result is checked by a
separate symbolic differentiation implementation after JSON serialization.
"""
from fractions import Fraction as Q
from math import isqrt, comb
import exact_bivariate as P


def harmonic(degree):
    # Re for odd degree, Im for even, represented by ordinary real monomials.
    parity = 0 if degree % 2 else 1
    return {(degree-j, j): Q(comb(degree,j)*(-1)**((j-parity)//2))
            for j in range(parity,degree+1,2)}


def base_stream(beta, a0, degree):
    beta,a0=Q(beta),Q(a0)
    rn,rd=isqrt(beta.numerator),isqrt(beta.denominator)
    if Q(rn*rn,rd*rd)!=beta or beta<=2 or a0<=0:
        raise ValueError('positive a0 and rational sqrt(beta), beta>2 required for base')
    sqrt_beta=Q(rn,rd);c=1+beta/2;p=(beta-1)/(2*beta)
    L=3*c*sqrt_beta/(4*a0);h=sqrt_beta*L;S0=L*L+h*h
    q={(2,0):1/S0,(0,2):1/S0,(0,1):-2*h/S0}
    psi=P.scale(P.mul({(1,0):Q(1)},P.unit_power(q,p,degree),degree),-c*S0/(2*p*h))
    psi.pop((1,0),None)
    return psi,{'beta':str(beta),'a0':str(a0),'L':str(L),'h':str(h),
                'S0':str(S0),'p':str(p),'c':str(c)}


def velocity(beta,psi):
    return (P.add({(1,0):Q(beta)},P.scale(P.diff(psi,1),-1)),
            P.add({(0,1):Q(beta)},P.diff(psi,0)))


def temperature(beta,a0,psi,degree):
    beta,a0=Q(beta),Q(a0);l=(beta-2)/2;m=1+3*beta/2
    theta={(2,0):a0};W=velocity(beta,psi)
    for d in range(3,degree+1):
        defect=P.homogeneous(P.add(P.dot_grad(W,theta,d),P.scale(theta,-(beta-2))),d)
        correction={key:-v/(key[0]*l+key[1]*m-2*l) for key,v in defect.items()}
        theta=P.add(theta,correction)
    return theta


def poisson_right_inverse(H,degree):
    """Solve -Lap D=H with the largest odd-x domain monomial excluded."""
    if any(i%2!=1 or i+j!=degree for i,j in H):
        raise ValueError('expected homogeneous odd-in-x polynomial')
    D={};top=degree if degree%2 else degree-1
    for i in range(top,0,-2):
        j=degree-i
        value=(-H.get((i,j),Q(0))-(i+2)*(i+1)*D.get((i+2,j),Q(0)))/((j+2)*(j+1))
        if value:D[i,j+2]=value
    if P.scale(P.lap(D),-1)!=P.clean(H):
        raise AssertionError('right inverse failed')
    return D


def run(beta,a0,N,harmonic_changes=None):
    beta,a0=Q(beta),Q(a0);l=(beta-2)/2;m=1+3*beta/2
    base,parameters=base_stream(beta,a0,N+2)
    psi=base.copy()
    for degree,value in (harmonic_changes or {}).items():
        if degree<4 or degree>N+2:raise ValueError('harmonic degree outside range')
        psi=P.add(psi,P.scale(harmonic(degree),Q(value)))
    initial=psi.copy();theta0=temperature(beta,a0,psi,N+1)
    ft0,go0=P.pde(beta,psi,theta0,N+1)
    assert not P.trunc(go0,1)
    stages=[]
    for n in range(2,N+1):
        theta=temperature(beta,a0,psi,n+1)
        defect=P.homogeneous(P.pde(beta,psi,theta,n)[1],n)
        dOmega={key:-v/(key[0]*l+key[1]*m+1) for key,v in defect.items()}
        delta=poisson_right_inverse(dOmega,n)
        psi=P.add(psi,delta)
        theta=temperature(beta,a0,psi,n+1)
        ft,go=P.pde(beta,psi,theta,n+1)
        assert not P.trunc(ft,n+1),(n,'temperature')
        assert not P.trunc(go,n),(n,'vorticity')
        stages.append({'residual_degree':n,'correction':P.serialize(delta),
                       'vorticity_residual_zero_through':n,
                       'temperature_residual_zero_through':n+1,
                       'defect_before_correction':P.serialize(defect)})
    theta=temperature(beta,a0,psi,N+1)
    return {'parameters':parameters,'max_vorticity_degree':N,'max_temperature_degree':N+1,
            'complement':'all odd monomials except the one of largest x exponent',
            'harmonic_changes':{str(k):str(v) for k,v in (harmonic_changes or {}).items()},
            'base_psi':P.serialize(base),'initial_psi':P.serialize(initial),
            'initial_R_Omega_degree2':P.serialize(P.homogeneous(go0,2)),
            'final_psi':P.serialize(psi),'final_theta':P.serialize(theta),'stages':stages,
            'scope':'Finite rational Taylor coefficients, not a convergent series or a PDE profile.'}
