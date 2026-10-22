"""Own full-plane physical quadrature for dilation of native r2 spline fields."""
import numpy as np
from scipy.interpolate import BSpline
from scipy.special import roots_jacobi
from scipy.linalg import cho_factor,cho_solve


def radial_rule(state,delta=.25,R=1.,order=48,odd=0):
    ts=[];ws=[];b=state.bb;L=state.L
    for lo,hi in zip(state.edges[:-1],state.edges[1:]):
        for sign in [-1,1]:
            p=sign*delta;alpha=1-b*p if hi==1 else 0.
            exponent=p/2+odd;beta=exponent if lo==0 else 0.
            x,w=roots_jacobi(order,alpha,beta)
            t=lo+(hi-lo)*(1+x)/2;u=1-t
            logeta2=np.log(-np.expm1(2*b*np.log(u)))
            remainder=(1-b*p)*np.log(u)+exponent*logeta2
            if lo==0:remainder-=beta*np.log(t)
            if hi==1:remainder-=alpha*np.log(u)
            ws.append(b*L*L*w*((hi-lo)/2)**(1+alpha+beta)*(L/R)**p*np.exp(remainder))
            ts.append(t)
    return np.concatenate(ts),np.concatenate(ws)


def brackets(state,t):
    """Return normalized brackets of G, -rG_r and -G-rG_r for all modes."""
    t=np.asarray(t);u=1-t;eta2=-np.expm1(2*state.bb*np.log(u))
    s=state.Gs(t);ds=state.Gs.derivative()(t)
    odd=np.arange(state.K)%2
    old=((state.bb+1)/state.bb*eta2[:,None]-odd[None,:]*(1-eta2[:,None]))*s-u[:,None]*eta2[:,None]*ds/state.bb
    return s,old,old-s


def dilation_radial(state,r):
    r=np.asarray(r,dtype=float);logu=-np.log1p((r/state.L)**2)/(2*state.bb);t=-np.expm1(logu)
    s,old,true=brackets(state,t)
    scale=np.exp((state.bb+1)*logu)[:,None]*np.power((r/np.hypot(r,state.L))[:,None],np.arange(state.K)%2)
    return {'G':scale*s,'old':scale*old,'true':scale*true}


def full_plane_dilation(state,directions=None,delta=.25,R=1.,order=48,H=None,active=None):
    """Compare coefficient directions with exact radial derivatives in a physical norm.
    Angular integration is analytic. Radial integration uses Gauss-Jacobi panels.
    No fitting-lane quadrature or fit operator is used.
    """
    directions={} if directions is None else directions
    active=np.array([k*state.nb+j for k in range(state.K) for j in range(k//2,state.nb)]) if active is None else np.asarray(active)
    coeff={}
    for name,v in directions.items():
        a=np.zeros(state.K*state.nb);a[active]=v;coeff[name]=a.reshape(state.K,state.nb)
    out={k:0. for k in ['G_squared','old_squared','true_squared']}
    errors={name:{'to_old_squared':0.,'to_true_squared':0.,'field_squared':0.} for name in directions}
    rhs=np.zeros((state.K,state.nb))
    for odd in [0,1]:
        t,w=radial_rule(state,delta,R,order,odd)
        B=BSpline(state.knots,np.eye(state.nb),state.degree,extrapolate=False)(t)
        s,old,true=brackets(state,t);ks=np.arange(odd,state.K,2)
        angular=np.where(ks==0,2.,1.)*np.pi
        for name,a in [('G',s),('old',old),('true',true)]:
            out[name+'_squared']+=float(np.sum(w[:,None]*a[:,ks]**2*angular[None,:]))
        rhs[ks]=(B.T@(w[:,None]*true[:,ks])*angular[None,:]).T
        for name,a in coeff.items():
            val=B@a[ks].T
            errors[name]['field_squared']+=float(np.sum(w[:,None]*val**2*angular[None,:]))
            errors[name]['to_old_squared']+=float(np.sum(w[:,None]*(val-old[:,ks])**2*angular[None,:]))
            errors[name]['to_true_squared']+=float(np.sum(w[:,None]*(val-true[:,ks])**2*angular[None,:]))
    rhs=rhs.ravel()[active]
    out.update(errors=errors,delta=delta,R=R,order=order,rhs_true=rhs)
    if H is not None:
        z=cho_solve(cho_factor(H,lower=False,check_finite=True),rhs)
        # Difference of nearby squared norms can cancel; direct quadrature remains preferable for tiny errors.
        out['physical_projection_true']=z
        out['physical_projection_error_squared_by_subtraction']=float(out['true_squared']-rhs@z)
    return out
