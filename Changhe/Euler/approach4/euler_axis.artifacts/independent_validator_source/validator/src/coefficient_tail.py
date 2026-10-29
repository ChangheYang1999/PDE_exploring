"""Representation-independent saved-coefficient tail check in the open main interval."""
from math import factorial
import numpy as np
from numpy.polynomial import Polynomial as Poly,Legendre
from scipy.special import poch
from independent_fields import ScalarExpansion
from independent_farfield import angular_data,evaluate_vector
from eta_green_basis import EtaGreenField,angular_decomposition,gegenbauer_polynomial
from piecewise_adapter import PiecewiseField

def add_power(out,p,poly,tol=2e-10):
    key=next((k for k in out if abs(k-p)<tol),float(p))
    out[key]=out.get(key,Poly([0.]))+poly

def envelope_powers(scalar,limit):
    if scalar.kernel=='gaussian':
        if any(t.beta<=0 and t.coefficient for t in scalar.terms):raise ValueError('nondecaying Gaussian term')
        return {}
    out={};one=Poly([1.,0.,-1.]);mu=Poly([0.,1.])
    for t in scalar.terms:
        p=2*t.beta-2*t.i-t.j
        if p>limit+2e-10 or t.coefficient==0:continue
        if limit-p>100:raise ValueError('unexpected asymptotic order gap')
        for n in range(max(0,int(np.floor((limit-p+2e-10)/2))+1)):
            amplitude=t.coefficient*(-1)**n*poch(t.beta,n)/factorial(n)*scalar.length**(2*n)
            add_power(out,p+2*n,amplitude*one**t.i*mu**t.j)
    return out

def angular_inverse(E,p):
    if not 0<p<3:raise ValueError('source extraction limited to powers strictly between zero and three')
    out=Poly([0.])
    for j,c in enumerate(E.coef):
        if c==0:continue
        for ell,a in angular_decomposition(0,j):
            cc=np.zeros(ell+1)
            for n,v in gegenbauer_polynomial(ell).items():cc[n]=float(v)
            out+=c*float(a)*Poly(cc)/(ell*(ell+3)+p*(3-p))
    return out

def saved_powers(field,phi_limit,q_limit):
    if isinstance(field,EtaGreenField):
        ep=envelope_powers(field.eta_expansion,phi_limit+2)
        pp={p-2:angular_inverse(E,p-2) for p,E in ep.items()}
        return pp,envelope_powers(field.q,q_limit),'full-space source inverse; homogeneous powers >=3 lie after the checked correction'
    if isinstance(field,PiecewiseField):
        out=[];e=field.elements[-1]
        for key,limit in [('phi',phi_limit),('q',q_limit)]:
            power={}
            for j,p in enumerate(field.radial_keys[2,key]):
                if p>limit+2e-10:continue
                amp=float(e['Rlo'])**p*field.dilation**(p+(key=='phi'))
                add_power(power,p,Legendre(field.matrices[2,key][:,j]*amp).convert(kind=Poly))
            out.append(power)
        return *out,'explicit exterior powers'
    return envelope_powers(field.phi,phi_limit),envelope_powers(field.q,q_limit),'power-envelope binomial expansion'

def at_power(powers,p):
    hits=[v for k,v in powers.items() if abs(k-p)<2e-10]
    return sum(hits,Poly([0.]))

def velocity_coefficients(p,A,B,mu):
    mu=np.asarray(mu);s=np.sqrt(1-mu*mu)
    return np.stack((2*mu*A(mu)-(1-mu*mu)*A.deriv()(mu),s*(p-2)*A(mu),s*B(mu)),axis=-1)

def coefficient_audit(field,radii,mu,w):
    alpha=field.alpha;gamma=2*alpha+1
    if not 1/3<alpha<1:raise ValueError('this coefficient audit requires 1/2<c_l<3/4')
    radii=np.asarray(radii,dtype=float);mu=np.asarray(mu,dtype=float);w=np.asarray(w,dtype=float)
    pp,qp,method=saved_powers(field,gamma,gamma+1)
    A=at_power(pp,alpha);B=at_power(qp,alpha+1);A1=at_power(pp,gamma);B1=at_power(qp,gamma+1)
    data=angular_data(alpha,A,B);F=velocity_coefficients(alpha,A,B,mu);H=velocity_coefficients(gamma,A1,B1,mu);G=evaluate_vector(data,mu,'G')
    def norm(v):return float(np.sqrt(2*np.pi*np.sum(w[:,None]*v*v)))
    def inventory(powers):return [dict(decay_power=float(p),angular_coefficients=v.coef.tolist(),coefficient_max=float(np.max(abs(v.coef)))) for p,v in sorted(powers.items())]
    intervening=[]
    for key,powers,leading,first in [('phi',pp,alpha,gamma),('q',qp,alpha+1,gamma+1)]:
        for p,v in powers.items():
            if p<first-2e-10 and abs(p-leading)>2e-10 and np.any(v.coef!=0):
                intervening.append(dict(field=key,decay_power=float(p),coefficient_max=float(np.max(abs(v.coef)))))
    R=radii[:,None];r=R*np.sqrt(1-mu[None,:]**2);z=R*mu[None,:]
    d=field.cylindrical(r,z,3);U=d['U'];S=np.sqrt(1-mu*mu)
    spherical=np.stack((S*U[...,0]+mu*U[...,2],mu*U[...,0]-S*U[...,2],U[...,1]),axis=-1)
    red=field.reduced(r,z);rows=[]
    for i,rr in enumerate(radii):
        observed=rr**gamma*(spherical[i]-rr**(-alpha)*F)
        rows.append(dict(R=float(rr),leading_velocity_error=norm(rr**alpha*spherical[i]-F),
            observed_first_vs_saved_error=norm(observed-H),observed_first_vs_Euler_error=norm(observed-G),
            scaled_q_residual_max=float(rr**(gamma+1)*np.max(abs(red['q'][i]))),
            scaled_eta_residual_max=float(rr**(gamma+2)*np.max(abs(red['eta'][i])))))
    expected=norm(G);actual=norm(H);mismatch=norm(H-G)
    return dict(c_l=field.c_l,alpha=alpha,correction_exponent=gamma,extraction=method,
        A=A.coef.tolist(),B=B.coef.tolist(),A1_saved=A1.coef.tolist(),B1_saved=B1.coef.tolist(),
        A1_Euler=data['A1'].coef.tolist(),B1_Euler=data['B1'].coef.tolist(),pressure_Q_legendre=data['Qmode'].tolist(),
        phi_powers=inventory(pp),q_powers=inventory(qp),intervening_powers=intervening,
        leading_sphere_norm=norm(F),swirl_sphere_norm=float(np.sqrt(2*np.pi*np.sum(w*F[:,2]**2))),
        saved_correction_sphere_norm=actual,Euler_correction_sphere_norm=expected,
        correction_mismatch_sphere_norm=mismatch,correction_relative_to_Euler=None if expected==0 else mismatch/expected,
        norm_convention='L2 over the full unit sphere, including azimuthal factor 2*pi',rows=rows,
        scope='Saved finite-representation necessary coefficient check; not a proof of existence, nonexistence or all acceptance criteria.')
