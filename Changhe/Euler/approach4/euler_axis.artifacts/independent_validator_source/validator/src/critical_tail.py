"""Critical endpoint, explicit-tail counterpart of the open-interval audit.

The pressure dipole uses the global moment identity, never a free harmonic term.
See research/critical_coefficient_compatibility/PROOF.md for its hypotheses.
"""
import numpy as np
from coefficient_tail import saved_powers,at_power,velocity_coefficients
from independent_farfield import angular_data,evaluate_vector
from piecewise_adapter import PiecewiseField

def critical_coefficient_audit(field,radii,mu,w):
    alpha=field.alpha;gamma=2*alpha+1
    if field.c_l != .5 or alpha != 1.:raise ValueError('critical audit requires c_l = 1/2 exactly')
    if not isinstance(field,PiecewiseField):raise TypeError('critical source inverse is excluded; explicit exterior powers required')
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
        scope='Critical necessary coefficient target under globally smooth full-space hypotheses in research/critical_coefficient_compatibility/PROOF.md. For a piecewise field with interface jumps this target is conditional and need not equal its bulk-only pressure asymptote. This does not prove existence, nonexistence or acceptance.', pressure_dipole_selection='Full-space moment identity Q1 = (NR1-T)/3, conditional on global smoothness', theorem='research/critical_coefficient_compatibility/PROOF.md')
