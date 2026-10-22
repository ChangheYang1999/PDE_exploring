"""Independent Cartesian and divided residuals with explicit axis limits."""
import numpy as np
from inverse import velocity, Quadrature

FIRST=np.array([1/280,-4/105,1/5,-4/5,0,4/5,-1/5,4/105,-1/280])
SECOND=np.array([-1/560,8/315,-1/5,8/5,-205/72,8/5,-1/5,8/315,-1/560])
SHIFTS=np.arange(-4,5)
EXTRAP_NODES=np.arange(1,5,dtype=float)
EXTRAP_WEIGHTS=np.array([np.prod([-k*k/(j*j-k*k) for k in EXTRAP_NODES if k!=j])
                         for j in EXTRAP_NODES])


def differentiate(fun,points,axis,derivative=1,relative_step=0.002):
    points=np.atleast_2d(np.asarray(points,dtype=float))
    h=relative_step*(1+np.linalg.norm(points,axis=1))
    shifted=np.broadcast_to(points,(9,)+points.shape).copy()
    shifted[:,:,axis]+=SHIFTS[:,None]*h[None,:]
    values=np.asarray(fun(shifted.reshape(-1,2)))
    values=values.reshape((9,len(points))+values.shape[1:])
    weights=FIRST if derivative==1 else SECOND
    out=np.tensordot(weights,values,axes=(0,0))
    return out/(h**derivative).reshape((len(points),)+(1,)*(out.ndim-1))


def quotient_limit(fun,points,powers,axis_step=0.002):
    """Parity quotient, extrapolating only coordinates exactly on axes.

    Zero-coordinate values use 4 positive offsets and a polynomial in the
    squared offset. This is an independently repeated numerical axis limit,
    not a claim of exact smooth division. Vary axis_step to audit stability.
    """
    points=np.atleast_2d(np.asarray(points,dtype=float))
    result=np.empty(len(points))
    for i,p in enumerate(points):
        options=[]
        for axis,power in enumerate(powers):
            if power and p[axis]==0:
                step=axis_step*(1+abs(p[1-axis]))
                options.append([(step*j,w) for j,w in zip(EXTRAP_NODES,EXTRAP_WEIGHTS)])
            else: options.append([(p[axis],1.0)])
        nodes=np.array([[x,y] for x,_ in options[0] for y,_ in options[1]])
        weights=np.array([wx*wy for _,wx in options[0] for _,wy in options[1]])
        denom=nodes[:,0]**powers[0]*nodes[:,1]**powers[1]
        result[i]=weights@(np.asarray(fun(nodes))/denom)
    return result


def normalized(residual,denominator):
    """No positive denominator floor. 0/0 is 0; nonzero/0 is infinity."""
    residual,denominator=np.asarray(residual),np.asarray(denominator)
    ratio=np.full_like(denominator,np.inf,dtype=float)
    np.divide(np.abs(residual),denominator,out=ratio,where=denominator>0)
    ratio[(denominator==0)&(residual==0)]=0
    return ratio


def cartesian(theta,omega,beta,points,u=None,psi=None,
              config=Quadrature(),step=0.002,elliptic=True):
    points=np.atleast_2d(np.asarray(points,dtype=float))
    if u is None: u=lambda p:velocity(omega,p,config)
    uv=u(points); w=beta*points+uv
    th,om=theta(points),omega(points)
    tx=differentiate(theta,points,0,relative_step=step)
    ty=differentiate(theta,points,1,relative_step=step)
    ox=differentiate(omega,points,0,relative_step=step)
    oy=differentiate(omega,points,1,relative_step=step)
    ro=w[:,0]*ox+w[:,1]*oy+om-tx
    rt=w[:,0]*tx+w[:,1]*ty-(beta-2)*th
    no=np.abs(w[:,0]*ox)+np.abs(w[:,1]*oy)+np.abs(om)+np.abs(tx)
    nt=np.abs(w[:,0]*tx)+np.abs(w[:,1]*ty)+abs(beta-2)*np.abs(th)
    out=dict(R_omega=ro,R_theta=rt,N_omega=no,N_theta=nt,
             ratio_omega=normalized(ro,no),ratio_theta=normalized(rt,nt),U=uv)
    if elliptic:
        if psi is not None:
            e=-differentiate(psi,points,0,2,step)-differentiate(psi,points,1,2,step)-om
            out['E_stream']=e
        dyu=differentiate(u,points,1,relative_step=step)
        dxu=differentiate(u,points,0,relative_step=step)
        out['E_curl']=dyu[:,0]-dxu[:,1]-om
        out['div_U']=dxu[:,0]+dyu[:,1]
    return out


def divided(theta,omega,beta,points,u=None,config=Quadrature(),step=0.002,axis_step=0.002):
    points=np.atleast_2d(np.asarray(points,dtype=float))
    if u is None: u=lambda p:velocity(omega,p,config)
    a=lambda p:quotient_limit(theta,p,(2,1),axis_step)
    g=lambda p:quotient_limit(omega,p,(1,1),axis_step)
    av,gv=a(points),g(points)
    A=beta+quotient_limit(lambda p:u(p)[:,0],points,(1,0),axis_step)
    B=beta+quotient_limit(lambda p:u(p)[:,1],points,(0,1),axis_step)
    ax=differentiate(a,points,0,relative_step=step)
    ay=differentiate(a,points,1,relative_step=step)
    gx=differentiate(g,points,0,relative_step=step)
    gy=differentiate(g,points,1,relative_step=step)
    x,y=points.T
    tx=2*av+x*ax; ty=av+y*ay
    ro=A*(gv+x*gx)+B*(gv+y*gy)+gv-tx
    rt=A*tx+B*ty-(beta-2)*av
    no=np.abs(A*(gv+x*gx))+np.abs(B*(gv+y*gy))+np.abs(gv)+np.abs(tx)
    nt=np.abs(A*tx)+np.abs(B*ty)+abs(beta-2)*np.abs(av)
    return dict(R_omega_div=ro,R_theta_div=rt,N_omega_div=no,N_theta_div=nt,
                ratio_omega_div=normalized(ro,no),ratio_theta_div=normalized(rt,nt),
                a=av,G=gv,A=A,B=B)


def summary(fields):
    out={}
    for name,values in fields.items():
        v=np.asarray(values)
        if name=='U': continue
        out[name]={'max_abs':float(np.max(np.abs(v))),
                   'nonfinite_count':int(np.count_nonzero(~np.isfinite(v)))}
        if name.startswith('N_'):
            positive=v[v>0]
            out[name]['zero_count']=int(np.count_nonzero(v==0))
            out[name]['minimum_positive']=float(np.min(positive)) if len(positive) else None
            out[name]['subnormal_count']=int(np.count_nonzero((v>0)&(v<np.finfo(float).tiny)))
    return out


def cartesian_from_factors(a,g,beta,points,u,step=0.002):
    """Finite-difference amplitude derivatives with exact known parity factors.

    This is a companion to raw Cartesian differentiation, not a replacement
    for its diagnostic. It avoids manufacturing nonzero axis derivatives
    from floating-point sums of an analytically odd field. It requires the
    caller to establish Theta=x^2*y*a and Omega=x*y*g independently.
    """
    points=np.atleast_2d(np.asarray(points,dtype=float));x,y=points.T
    av,gv=a(points),g(points)
    ax=differentiate(a,points,0,relative_step=step)
    ay=differentiate(a,points,1,relative_step=step)
    gx=differentiate(g,points,0,relative_step=step)
    gy=differentiate(g,points,1,relative_step=step)
    th=x*x*y*av;om=x*y*gv
    tx=x*y*(2*av+x*ax);ty=x*x*(av+y*ay)
    ox=y*(gv+x*gx);oy=x*(gv+y*gy)
    uv=u(points);w=beta*points+uv
    ro=w[:,0]*ox+w[:,1]*oy+om-tx
    rt=w[:,0]*tx+w[:,1]*ty-(beta-2)*th
    no=np.abs(w[:,0]*ox)+np.abs(w[:,1]*oy)+np.abs(om)+np.abs(tx)
    nt=np.abs(w[:,0]*tx)+np.abs(w[:,1]*ty)+abs(beta-2)*np.abs(th)
    return dict(R_omega=ro,R_theta=rt,N_omega=no,N_theta=nt,
                ratio_omega=normalized(ro,no),ratio_theta=normalized(rt,nt),U=uv)
