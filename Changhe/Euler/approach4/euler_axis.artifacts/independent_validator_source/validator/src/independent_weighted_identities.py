"""Pressure-free infinite-domain circulation and axial transport identities."""
from __future__ import annotations
import numpy as np
from scipy.special import roots_legendre,roots_jacobi


def power_nodes(n,power):
    if power<=-1:raise ValueError('nonintegrable quadrature endpoint')
    x,w=roots_jacobi(n,0.,power)
    return (x+1)/2,w/2**(power+1)


def weighted_circulation(field,p,beta,*,nradial=64,nangle=64,split_radius=None,exterior_map_power=4):
    p=int(p)
    if p not in (1,2):raise ValueError('registered diagnostic uses p=1 or p=2')
    alpha=field.alpha;c=field.c_l;lower=3+p*(1-alpha);upper=2*p+2
    if not lower<beta<upper:raise ValueError('beta outside the sufficient integrability interval')
    scale=float(split_radius if split_radius is not None else max(field.phi.length,field.q.length))
    mu,wm=roots_legendre(nangle);sine=np.sqrt(1-mu*mu);angular=(1-mu*mu)**p
    def values(R):
        r=R[:,None]*sine;z=R[:,None]*mu;d=field.cylindrical(r,z,3);red=field.reduced(r,z)
        q=d['q'][0,0];U=d['U'];ur=U[...,0]*sine+U[...,2]*mu
        return q,ur,red['q']
    x,wx=power_nodes(nradial,2*p+1-beta);R=scale*x;q,ur,rq=values(R)
    ai=(q**p*angular)@wm;aj=(q**p*ur*angular)@wm;ak=(q**(p-1)*rq*angular)@wm
    I0=2*np.pi*scale**(2*p+3-beta)*np.dot(wx,x*ai)
    J0=2*np.pi*scale**(2*p+2-beta)*np.dot(wx,aj)
    K0=2*np.pi*scale**(2*p+3-beta)*np.dot(wx,x*ak)
    # t=u^h raises the remaining fractional correction powers before
    # polynomial quadrature. The Jacobi weight includes the exact Jacobian.
    h=int(exterior_map_power)
    if h<1:raise ValueError('positive exterior mapping power required')
    exponent=beta-p*(1-alpha)-4
    u,wu=power_nodes(nradial,h*(exponent+1)-1);t=u**h;wt=h*wu
    R=scale/t;q,ur,rq=values(R)
    fq=R[:,None]**(alpha+1)*q;fu=R[:,None]**alpha*ur;fr=R[:,None]**(alpha+1)*rq
    ai=(fq**p*angular)@wm;aj=(fq**p*fu*angular)@wm;ak=(fq**(p-1)*fr*angular)@wm
    I1=2*np.pi*scale**(3+p*(1-alpha)-beta)*np.dot(wt,ai)
    # J carries one additional U_R/R power, so factor it into its own
    # endpoint weight instead of leaving a fractional power in the integrand.
    uj,wuj=power_nodes(nradial,h*(exponent+alpha+2)-1);tj=uj**h;Rj=scale/tj
    qj,urj,_=values(Rj);fqj=Rj[:,None]**(alpha+1)*qj;fuj=Rj[:,None]**alpha*urj
    aj=(fqj**p*fuj*angular)@wm
    J1=2*np.pi*scale**(2+p*(1-alpha)-alpha-beta)*np.dot(h*wuj,aj)
    K1=2*np.pi*scale**(3+p*(1-alpha)-beta)*np.dot(wt,ak)
    I=float(I0+I1);J=float(J0+J1);K=float(K0+K1)
    coefficient=c*(beta-lower);defect=beta*J+coefficient*I;residual=p*K
    denominator=abs(beta*J)+abs(coefficient*I)
    return {'p':p,'beta':float(beta),'beta_interval':[lower,upper],'nradial':nradial,'nangle':nangle,
            'split_radius':scale,'exterior_map_power':h,'I':I,'J':J,'K_residual_integral':K,
            'I_origin':float(I0),'I_exterior':float(I1),'J_origin':float(J0),'J_exterior':float(J1),
            'Euler_identity_defect':defect,'Euler_identity_relative_defect':abs(defect)/denominator if denominator else None,
            'integrated_residual_prediction':residual,'quadrature_consistency_error':defect-residual,
            'quadrature_consistency_relative':abs(defect-residual)/(denominator+abs(residual)) if denominator+abs(residual) else None,
            'scope':'Infinite-domain quadrature estimate. The residual-source equality tests the integral implementation; only a small Euler defect tests the profile.'}


def weighted_circulation_suite(field,**kwargs):
    rows=[]
    for p in (1,2):
        low=3+p*(1-field.alpha);high=2*p+2
        for fraction in (.25,.5,.75):rows.append(weighted_circulation(field,p,low+fraction*(high-low),**kwargs))
    return rows


def axial_identity(field,z,q0):
    z=np.asarray(z,dtype=np.float64);r=np.zeros_like(z)
    d=field.cylindrical(r,z,3);red=field.reduced(r,z)
    q=d['q'][0,0];qz=d['q'][0,1];eta=d['eta'];etaz=d['eta_z']
    W=field.c_l*z+d['U'][...,2];Wp=field.c_l+2*d['phi'][0,1]
    first=W*eta;second=2*q*(q-q0);H=first-second
    Hp=Wp*eta+W*etaz-2*qz*(2*q-q0)
    consistency=q*Hp-qz*H-q*red['eta']+eta*red['q']
    return {'z':z,'q':q,'Wz':W,'eta':eta,'H':H,'W_eta':first,'2q(q-q0)':second,
            'differential_identity_error':consistency,'q_residual':red['q'],'eta_residual':red['eta']}
