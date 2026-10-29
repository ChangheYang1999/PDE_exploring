"""Exact leading coefficients and observed tail convergence for own basis format."""
from __future__ import annotations
import numpy as np
from numpy.polynomial import Polynomial as Poly
from independent_farfield import angular_data,evaluate_vector
from independent_identities import vorticity_and_jacobian


def leading_coefficients(field,tolerance=2e-11):
    one=Poly([1.,0.,-1.]); mu=Poly([0.,1.])
    coefficients={};terms=[]
    for name,scalar,target in [('phi',field.phi,-field.alpha),('q',field.q,-field.alpha-1)]:
        result=Poly([0.])
        for k,t in enumerate(scalar.terms):
            degree=2*t.i+t.j-2*t.beta
            if scalar.kernel=='gaussian':
                status='faster than every power' if t.beta>0 else 'nondecaying or growing'
            elif abs(degree-target)<=tolerance:
                status='leading';result=result+t.coefficient*one**t.i*mu**t.j
            elif degree<target:
                status='faster'
            else:
                status='slower than declared leading power'
            terms.append({'field':name,'index':k,'coefficient':t.coefficient,'homogeneity':degree,'classification':status})
        coefficients[name]=result
    A=coefficients['phi'];B=coefficients['q']
    return A,B,terms


def tail_audit(field,radii,mu,w,pressure_values=None,pressure_gradients=None):
    radii=np.asarray(radii);mu=np.asarray(mu);w=np.asarray(w)
    A,B,terms=leading_coefficients(field)
    data=angular_data(field.alpha,A.coef,B.coef)
    F=evaluate_vector(data,mu,'F');G=evaluate_vector(data,mu,'G')
    r=radii[:,None]*np.sqrt(1-mu[None,:]**2);z=radii[:,None]*mu[None,:]
    U=field.cylindrical(r,z)['U']
    S=np.sqrt(1-mu**2)
    Us=np.stack((S*U[...,0]+mu*U[...,2],mu*U[...,0]-S*U[...,2],U[...,1]),axis=-1)
    scaled=radii[:,None,None]**field.alpha*Us
    Fnorm=float(np.sqrt(np.sum(w[:,None]*F*F)))
    Q=data['Q'](mu)
    E=data['E'](mu)
    rows=[]
    for k,R in enumerate(radii):
        rem=R**(2*field.alpha+1)*(Us[k]-R**(-field.alpha)*F)
        row={'R':float(R),'scaled_velocity_error_l2':float(np.sqrt(np.sum(w[:,None]*(scaled[k]-F)**2))),
             'leading_velocity_l2':Fnorm,
             'first_correction_error_l2':float(np.sqrt(np.sum(w[:,None]*(rem-G)**2))),
             'scaled_q_error_max':float(np.max(np.abs(R**(field.alpha+1)*field.q.evaluate(r[k]**2,z[k])-B(mu)))),
             'scaled_eta_error_max':float(np.max(np.abs(R**(field.alpha+2)*field.eta(r[k],z[k])-E))),
             'scaled_phi_error_max':float(np.max(np.abs(R**field.alpha*field.phi.evaluate(r[k]**2,z[k])-A(mu))))}
        if pressure_values is not None:
            row['scaled_pressure_error_l2']=float(np.sqrt(np.sum(w*(R**(2*field.alpha)*pressure_values[k]-Q)**2)))
        if pressure_gradients is not None:
            expected=np.stack((-2*field.alpha*S*Q-mu*S*data['Q'].deriv()(mu),-2*field.alpha*mu*Q+(1-mu*mu)*data['Q'].deriv()(mu)),axis=-1)
            row['scaled_pressure_gradient_error_l2']=float(np.sqrt(np.sum(w[:,None]*(R**(2*field.alpha+1)*pressure_gradients[k]-expected)**2)))
        rows.append(row)
    return {'A_monomial_coefficients':A.coef.tolist(),'B_monomial_coefficients':B.coef.tolist(),
            'Q_legendre_coefficients':data['Qmode'].tolist(),'basis_terms':terms,
            'leading_sphere_velocity_squared_integral':float(2*np.pi*np.sum(w[:,None]*F*F)),
            'leading_sphere_swirl_squared_integral':float(2*np.pi*np.sum(w*F[:,2]**2)),
            'tail_energy_growth_exponent':float(3-2*field.alpha),'rows':rows,
            'scope':'Asymptotic coefficients follow exactly from this finite representation. Convergence measurements do not establish that it solves Euler.'}


def scalar_cancellation(expansion,s,z,order=3):
    """Absolute sum / absolute value, retaining a floor-free condition report."""
    s,z=np.broadcast_arrays(np.asarray(s,dtype=float),np.asarray(z,dtype=float))
    rho=expansion.length**2+s+z*z
    records=[]
    for ds in range(order+1):
        for dz in range(order+1-ds):
            terms=[]
            for t in expansion.differentiated(ds,dz):
                if expansion.kernel=='power':v=t.coefficient*(s/rho)**t.i*(z/np.sqrt(rho))**t.j*rho**(t.i+.5*t.j-t.beta)
                else:v=t.coefficient*s**t.i*z**t.j*np.exp(-t.beta*(s+z*z))
                terms.append(v)
            if terms:
                total=np.sum(terms,axis=0);absolute=np.sum(np.abs(terms),axis=0)
            else:total=np.zeros_like(s);absolute=np.zeros_like(s)
            ratio=np.divide(absolute,np.abs(total),out=np.full_like(absolute,np.inf),where=total!=0)
            ratio=np.where(absolute==0,1.,ratio)
            finite=ratio[np.isfinite(ratio)]
            records.append({'ds':ds,'dz':dz,'maximum_finite_condition':float(np.max(finite,initial=1.)),
                            'exact_cancellation_points':int(np.count_nonzero(np.isinf(ratio))),
                            'maximum_absolute_term_sum':float(np.max(absolute,initial=0.))})
    return records
