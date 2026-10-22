"""Centered finite differences independent of analytic/autodiff derivatives.

Weights are solved from polynomial moment conditions. Step-size variation is
required by the caller. No differentiation of fitting-lane code is performed.
"""
import math
import numpy as np


def stencil(derivative=1,radius=3):
    z=np.arange(-radius,radius+1,dtype=float)
    a=np.vstack([z**k for k in range(len(z))])
    rhs=np.zeros(len(z));rhs[derivative]=math.factorial(derivative)
    return z,np.linalg.solve(a,rhs)


def derivative(fun,points,axis,step,order=1,radius=3):
    p=np.atleast_2d(np.asarray(points,dtype=float))
    z,w=stencil(order,radius)
    q=np.repeat(p[:,None,:],len(z),axis=1)
    q[:,:,axis]+=step*z[None,:]
    vals=np.asarray(fun(q[:,:,0],q[:,:,1]))
    return vals@w/step**order


def mixed(fun,points,step,radius=3):
    p=np.atleast_2d(np.asarray(points,dtype=float))
    z,w=stencil(1,radius)
    q=np.repeat(p[:,None,None,:],len(z),axis=1)
    q=np.repeat(q,len(z),axis=2)
    q[:,:,:,0]+=step*z[None,:,None]
    q[:,:,:,1]+=step*z[None,None,:]
    values=np.asarray(fun(q[:,:,:,0],q[:,:,:,1]))
    return np.einsum('nij,i,j->n',values,w,w)/step**2


def safe_ratio(residual,denominator):
    """No positive floor. Computed N=R=0 -> 0; N=0,R!=0 -> infinity.

    Underflow is not distinguishable from computed zero here. Callers must
    report zero counts and check very small terms with stronger arithmetic."""
    residual=np.asarray(residual)
    denominator=np.asarray(denominator)
    result=np.full_like(denominator,np.inf,dtype=float)
    nonzero=denominator!=0
    result[nonzero]=np.abs(residual[nonzero])/denominator[nonzero]
    result[(denominator==0)&(residual==0)]=0
    return result


def cartesian_residuals(theta,omega,psi,relative_velocity,points,beta,step,radius=3):
    p=np.atleast_2d(np.asarray(points,dtype=float))
    th=theta(p[:,0],p[:,1]);om=omega(p[:,0],p[:,1])
    tx=derivative(theta,p,0,step,radius=radius)
    ty=derivative(theta,p,1,step,radius=radius)
    ox=derivative(omega,p,0,step,radius=radius)
    oy=derivative(omega,p,1,step,radius=radius)
    vel=np.asarray(relative_velocity(p))
    W=beta*p+vel
    terms_o=np.column_stack((W[:,0]*ox,W[:,1]*oy,om,-tx))
    terms_t=np.column_stack((W[:,0]*tx,W[:,1]*ty,-(beta-2)*th))
    ro=terms_o.sum(axis=1);rt=terms_t.sum(axis=1)
    no=np.abs(terms_o).sum(axis=1);nt=np.abs(terms_t).sum(axis=1)
    ell=-derivative(psi,p,0,step,order=2,radius=radius)-derivative(psi,p,1,step,order=2,radius=radius)-om
    return {'R_Omega':ro,'R_Theta':rt,'E':ell,'N_Omega':no,'N_Theta':nt,
            'normalized_Omega':safe_ratio(ro,no),'normalized_Theta':safe_ratio(rt,nt),'W':W}


def divided_field(fun,points,step,factor,axis_threshold=0.0,radius=3):
    """Evaluate f/x or f/x^2, using derivative limits exactly on x=0.

    Near-axis nonzero points are evaluated as supplied, not replaced by a limit.
    factor=1 for odd fields; factor=2 for the temperature.
    """
    p=np.atleast_2d(np.asarray(points,dtype=float))
    out=np.empty(len(p))
    axis=np.abs(p[:,0])<=axis_threshold
    off=~axis
    out[off]=fun(p[off,0],p[off,1])/p[off,0]**factor
    if np.any(axis):
        out[axis]=derivative(fun,p[axis],0,step,order=factor,radius=radius)/math.factorial(factor)
    return out


def desingularized_residuals(theta,omega,psi,relative_velocity,points,beta,step,radius=3):
    """Compute R_Theta/x^2 and R_Omega/x by separate divided-field equations.

    Coordinates remain Cartesian: F=Theta/x^2, G=Omega/x, A=W1/x,
    R_F=2 A F+W1 F_x+W2 F_y-(beta-2)F,
    R_G=(A+1)G+W1 G_x+W2 G_y-2F-x F_x.
    The x=0 limits are evaluated using derivatives, not 0/0.
    R_H=-(H_xx+2 H_x/x+H_yy)-G is computed from H=psi/x.
    A short Gauss integral regularizes H_x/x near the axis.
    """
    p=np.atleast_2d(np.asarray(points,dtype=float))
    def field_div(fun,factor):
        def call(x,y):
            shape=np.broadcast(x,y).shape
            q=np.column_stack((np.broadcast_to(x,shape).ravel(),np.broadcast_to(y,shape).ravel()))
            return divided_field(fun,q,step,factor,radius=radius).reshape(shape)
        return call
    Ffun=field_div(theta,2);Gfun=field_div(omega,1);Hfun=field_div(psi,1)
    F=Ffun(p[:,0],p[:,1]);G=Gfun(p[:,0],p[:,1])
    Fx=derivative(Ffun,p,0,step,radius=radius)
    Fy=derivative(Ffun,p,1,step,radius=radius)
    Gx=derivative(Gfun,p,0,step,radius=radius)
    Gy=derivative(Gfun,p,1,step,radius=radius)
    V=relative_velocity(p);W=beta*p+V
    axis=p[:,0]==0
    A=np.empty(len(p))
    A[~axis]=W[~axis,0]/p[~axis,0]
    if np.any(axis):
        A[axis]=beta-mixed(psi,p[axis],step,radius=radius)
    # Keep the exact Cartesian grouping when dividing out parity factors.
    # Splitting 2AF from W1 Fx changes the pointwise denominator.
    tf=np.column_stack((A*(2*F+p[:,0]*Fx),W[:,1]*Fy,-(beta-2)*F))
    tg=np.column_stack((A*(G+p[:,0]*Gx),W[:,1]*Gy,G,-(2*F+p[:,0]*Fx)))
    rf=tf.sum(axis=1);rg=tg.sum(axis=1)
    Hxx=derivative(Hfun,p,0,step,order=2,radius=radius)
    Hyy=derivative(Hfun,p,1,step,order=2,radius=radius)
    Hx_over_x=np.empty(len(p))
    near=np.abs(p[:,0])<=4*step
    far=~near
    if np.any(far):
        Hx_over_x[far]=derivative(Hfun,p[far],0,step,radius=radius)/p[far,0]
    if np.any(near):
        # For even H, H_x(x,y)/x = integral_0^1 H_xx(t*x,y) dt.
        # This avoids dividing a finite-difference cancellation by tiny x.
        t,w=np.polynomial.legendre.leggauss(8);t=(t+1)/2;w=w/2
        q=np.repeat(p[near,None,:],len(t),axis=1);q[:,:,0]*=t[None,:]
        xx=derivative(Hfun,q.reshape(-1,2),0,step,order=2,radius=radius)
        Hx_over_x[near]=xx.reshape(-1,len(t))@w
    rh=-(Hxx+2*Hx_over_x+Hyy)-G
    return {'R_F':rf,'R_G':rg,'R_H':rh,'normalized_F':safe_ratio(rf,np.abs(tf).sum(axis=1)),
            'normalized_G':safe_ratio(rg,np.abs(tg).sum(axis=1)),
            'N_F':np.abs(tf).sum(axis=1),'N_G':np.abs(tg).sum(axis=1),'F':F,'G':G,'A':A}
