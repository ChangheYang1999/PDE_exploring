"""Independent backward-flow transport check; no solver residual code is imported."""
import numpy as np
from scipy.integrate import solve_ivp
from independent_residuals import derivative

def reconstruct(candidate,points,times=(3.,6.,9.),rtol=1e-9,atol=1e-12,hrel=.001):
    pts=np.asarray(points,float);count=len(pts);beta=float(candidate.beta)
    def rhs(t,z):
        xy=z[:2*count].reshape(count,2);x,y=xy[:,0],xy[:,1]
        w=beta*xy+np.asarray(candidate.U_modal(x,y),float)
        h=hrel*np.maximum(1,np.hypot(x,y))
        tx=np.asarray(derivative(candidate.Theta,x,y,h,0,1),float)
        return np.r_[-w.ravel(),np.exp(-t)*tx]
    initial=np.r_[pts.ravel(),np.zeros(count)]
    sol=solve_ivp(rhs,(0,max(times)),initial,method='DOP853',t_eval=times,rtol=rtol,atol=atol)
    theta=np.asarray(candidate.Theta(pts[:,0],pts[:,1]),float)
    omega=np.asarray(candidate.Omega(pts[:,0],pts[:,1]),float)
    a0=float(candidate.a0);rows=[]
    for i,t in enumerate(sol.t):
        xy=sol.y[:2*count,i].reshape(count,2);x,y=xy[:,0],xy[:,1]
        theta_finite=np.exp((beta-2)*t)*np.asarray(candidate.Theta(x,y),float)
        theta_origin=a0*np.exp((beta-2)*t)*y
        omega_integral=sol.y[2*count:,i]
        omega_finite=omega_integral+np.exp(-t)*np.asarray(candidate.Omega(x,y),float)
        rows.append({'time':float(t),'backward_points':xy.tolist(),'backward_radii':np.hypot(x,y).tolist(),
            'theta_actual':theta.tolist(),'theta_from_finite_transport':theta_finite.tolist(),'theta_from_origin':theta_origin.tolist(),
            'theta_finite_defect':(theta_finite-theta).tolist(),'theta_origin_defect':(theta_origin-theta).tolist(),
            'omega_actual':omega.tolist(),'omega_from_integral':omega_integral.tolist(),'omega_from_finite_transport':omega_finite.tolist(),
            'omega_finite_defect':(omega_finite-omega).tolist(),'omega_integral_defect':(omega_integral-omega).tolist()})
    return {'points':pts.tolist(),'rtol':rtol,'atol':atol,'hrel':hrel,'success':bool(sol.success),'message':sol.message,'nfev':sol.nfev,'rows':rows,
            'scope':'transport consistency under supplied independently reconstructed velocity; finite-time defects are exact characteristic identities up to ODE and differentiation errors; origin reconstruction additionally needs asymptotic convergence'}
