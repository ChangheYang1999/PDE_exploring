"""Independent log-radius axis functional, packet112.

The velocity callback gives v(exp(t))/exp(t). Adaptive DOP853 integrates
both the logarithmic coordinate and its integral. No fitting-lane code.
"""
import numpy as np
from scipy.integrate import solve_ivp

def functional(v_over_r, beta, a0, epsilon, radii, rtol=3e-11):
    mu=1.5*beta+1.;ell=mu/beta;P=(2*beta+1)/mu;rho=(beta+1)/mu
    radii=np.asarray(radii,dtype=float)
    if epsilon<=0 or np.any(radii<epsilon) or np.any(np.diff(radii)<=0):raise ValueError('ordered positive cutoffs required')
    def rhs(t,Y):
        ratio=float(v_over_r(t))
        if ratio<=0 or not np.isfinite(ratio):raise ValueError('nonpositive axis velocity')
        Z=Y[0]
        return [mu/ratio-1.,np.exp((1.-rho)*t-rho*Z)]
    sol=solve_ivp(rhs,(np.log(epsilon),np.log(radii[-1])),[0.,epsilon**(1-rho)/(1-rho)],
                  method='DOP853',t_eval=np.log(radii),rtol=rtol,atol=rtol*.05)
    if not sol.success:raise RuntimeError(sol.message)
    Z,I=sol.y;t=sol.t;logC=Z+(1-ell)*t
    C=np.exp(logC);factor=(2*a0*beta/mu**2)*np.exp(-P*logC)
    Qraw=factor*I
    tail=beta*np.exp(-rho*logC)*radii**(-1/beta)
    return {'radii':radii.tolist(),'Q_raw':Qraw.tolist(),'Q_integral_tail_only':(factor*(I+tail)).tolist(),
            'C_R':C.tolist(),'I_R_with_inner_fill':I.tolist(),'nfev':sol.nfev,
            'epsilon':epsilon,'mu':mu,'P':P,'rho':rho,'ell':ell,
            'meaning':'finite-inner-normalization diagnostic; tail correction retains finite C_R bias'}
