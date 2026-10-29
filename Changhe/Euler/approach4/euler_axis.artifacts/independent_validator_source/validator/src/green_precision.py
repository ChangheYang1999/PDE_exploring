"""High-precision Green inversion using incomplete beta integrals.

The radial reference does not call the float64 hypergeometric recurrence.
Only exact rational angular decomposition is shared with the main evaluator.
"""
from math import factorial
import mpmath as mp
import numpy as np
from eta_green_basis import angular_decomposition,solid_harmonic
from independent_precision import mp_scalar


def number(value):
    return mp.mpf(str(value))


def rational(value):
    return mp.mpf(value.numerator)/value.denominator


def monomial_derivative(i,j,s,z,a,b):
    if a>i or b>j:return mp.mpf(0)
    return mp.mpf(factorial(i)//factorial(i-a))*mp.mpf(factorial(j)//factorial(j-b))*s**(i-a)*z**(j-b)


def beta_radial(t,ell,degree,exponent):
    """Radial inverse and its first two t derivatives, for t>0."""
    if t<=0:raise ValueError('reference requires nonzero radius')
    beta=number(exponent);m=(degree-ell)//2;A=mp.mpf(ell+degree+5)/2
    chi=t/(1+t)
    inner=mp.betainc(A,beta-A,0,chi,regularized=False)
    outer=mp.betainc(beta-m-1,m+1,0,1/(1+t),regularized=False)
    h=(t**(-ell-mp.mpf('1.5'))*inner+outer)/(2*(2*ell+3))
    ht=-inner/(4*t**(ell+mp.mpf('2.5')))
    htt=(-t**m*(1+t)**(-beta)-(4*ell+10)*ht)/(4*t)
    return h,ht,htt


def reference_potential_jet(source,s,z):
    L=number(source.length);ss=s/L**2;zz=z/L;t=ss+zz**2
    indices=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]
    result={key:mp.mpf(0) for key in indices};cache={}
    for term in source.terms:
        if term.coefficient==0:continue
        degree=2*term.i+term.j
        amplitude=number(term.coefficient)*L**(degree+2-2*number(term.beta))
        for ell,angular in angular_decomposition(term.i,term.j):
            key=(ell,degree,term.beta)
            if key not in cache:cache[key]=beta_radial(t,*key)
            h,ht,htt=cache[key]
            H={index:sum((rational(c)*monomial_derivative(i,j,ss,zz,*index) for i,j,c in solid_harmonic(ell)),mp.mpf(0)) for index in indices}
            value={(0,0):H[0,0]*h,
                   (1,0):H[1,0]*h+H[0,0]*ht,
                   (0,1):H[0,1]*h+2*zz*H[0,0]*ht,
                   (2,0):H[2,0]*h+2*H[1,0]*ht+H[0,0]*htt,
                   (1,1):H[1,1]*h+(2*zz*H[1,0]+H[0,1])*ht+2*zz*H[0,0]*htt,
                   (0,2):H[0,2]*h+(4*zz*H[0,1]+2*H[0,0])*ht+4*zz**2*H[0,0]*htt}
            for (a,b),v in value.items():result[a,b]+=amplitude*rational(angular)*v/L**(2*a+b)
    return result


def reference_green_point(field,r,z,dps=70):
    with mp.workdps(dps):
        r,z=number(r),number(z);s=r*r;c=number(field.c_l)
        p=reference_potential_jet(field.eta_expansion,s,z)
        qfun=lambda s,z:mp_scalar(field.q,s,z)
        efun=lambda s,z:mp_scalar(field.eta_expansion,s,z)
        q,qs,qz=qfun(s,z),mp.diff(qfun,(s,z),(1,0)),mp.diff(qfun,(s,z),(0,1))
        eta,etas,etaz=efun(s,z),mp.diff(efun,(s,z),(1,0)),mp.diff(efun,(s,z),(0,1))
        Ur=-r*p[0,1];Uz=2*p[0,0]+2*s*p[1,0];U=[Ur,r*q,Uz]
        J=[[-p[0,1]-2*s*p[1,1],-q,-r*p[0,2]],
           [q+2*s*qs,-p[0,1],r*qz],
           [8*r*p[1,0]+4*r*s*p[2,0],mp.mpf(0),2*p[0,1]+2*s*p[1,1]]]
        q_res=q+2*s*(c-p[0,1])*qs+(c*z+Uz)*qz-2*p[0,1]*q
        e_res=(1+c)*eta+2*s*(c-p[0,1])*etas+(c*z+Uz)*etaz-2*q*qz
        primitive=[(1-c)*U[i]+J[i][0]*(c*r+Ur)+J[i][1]*U[1]+J[i][2]*(c*z+Uz) for i in range(3)]
        result={'velocity':U,'jacobian':J,'q':q,'eta':eta,'q_residual':q_res,'eta_residual':e_res,
                'primitive_without_pressure':primitive,'source':sum(J[i][j]*J[j][i] for i in range(3) for j in range(3)),
                'elliptic_defect':-8*p[1,0]-4*s*p[2,0]-p[0,2]-eta}
        def strings(v):
            if isinstance(v,list):return [strings(x) for x in v]
            return mp.nstr(v,dps)
        return {key:strings(value) for key,value in result.items()}


def compare_green_point(field,r,z,dps=70):
    reference=reference_green_point(field,r,z,dps);point=np.array([r,0.,z])
    U,J=field.cartesian(point,True);red=field.reduced(r,z);d=field.cylindrical(r,z,3)
    actual={'velocity':U,'jacobian':J,'q':d['q'][0,0],'eta':d['eta'],'q_residual':red['q'],'eta_residual':red['eta'],
            'primitive_without_pressure':field.primitive_cartesian(point),'source':field.source(r,z),
            'elliptic_defect':d['elliptic_defect']}
    errors={}
    for key,value in actual.items():
        ref=np.asarray(reference[key],dtype=float);error=float(np.max(np.abs(np.asarray(value)-ref)));scale=float(np.max(np.abs(ref)))
        errors[key]={'absolute_error':error,'reference_scale':scale,'relative_error':error/scale if scale else None}
    return {'r':r,'z':z,'dps':dps,'errors':errors,'reference':reference}
