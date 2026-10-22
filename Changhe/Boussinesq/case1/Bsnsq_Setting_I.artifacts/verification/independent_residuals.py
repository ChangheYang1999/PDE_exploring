"""Independent Cartesian finite-difference residuals, including parity-axis limits.

Candidate accessors are data evaluators only: Theta, Omega, Psi, and their smooth
parity quotients F=Theta/y, G=Omega/(xy), H=Psi/(xy). No fitted derivatives enter.
Velocity is recomputed from Omega through plane_quadrature, never from candidate Psi.
Seven-point Cartesian differences differ from the solver's analytic/modal derivatives.
"""
from math import factorial
import numpy as np
from plane_quadrature import Rule,evaluate,origin_strain

NODES=np.arange(-3,4,dtype=float)
MOMENTS=np.array([NODES**j for j in range(7)])
WEIGHTS={}
for order in [1,2]:
    rhs=np.zeros(7);rhs[order]=factorial(order)
    WEIGHTS[order]=np.linalg.solve(MOMENTS,rhs)
    # Enforce the exact known stencil symmetry, including the zero odd coefficient.
    if order==1:WEIGHTS[order]=(WEIGHTS[order]-WEIGHTS[order][::-1])/2
    else:WEIGHTS[order]=(WEIGHTS[order]+WEIGHTS[order][::-1])/2


def derivative(f,x,y,h,axis,order):
    # Pair symmetric values before accumulation. Exact parity zeros and constant
    # second derivatives then cancel algebraically, without a denominator floor.
    total=np.zeros(np.broadcast(x,y,h).shape,dtype=np.longdouble)
    center=np.asarray(f(x,y),dtype=np.longdouble) if order==2 else None
    for shift in [1,2,3]:
        xp=x+shift*h if axis==0 else x;xm=x-shift*h if axis==0 else x
        yp=y+shift*h if axis==1 else y;ym=y-shift*h if axis==1 else y
        plus=np.asarray(f(xp,yp),dtype=np.longdouble)
        minus=np.asarray(f(xm,ym),dtype=np.longdouble)
        difference=plus-minus if order==1 else (plus-center)+(minus-center)
        total+=np.longdouble(WEIGHTS[order][3+shift])*difference
    return total/np.asarray(h,dtype=np.longdouble)**order


def even_derivative_over_coordinate(f,x,y,h,axis):
    coord=x if axis==0 else y
    near=np.abs(coord)<4*h
    out=np.empty(np.broadcast(x,y,h).shape,dtype=np.longdouble)
    if np.any(~near):
        out[~near]=derivative(f,x[~near],y[~near],h[~near],axis,1)/coord[~near]
    if np.any(near):
        # f_x(x,y)/x = int_0^1 f_xx(t*x,y) dt for an exactly even f.
        nodes,weights=np.polynomial.legendre.leggauss(4)
        value=np.zeros(np.count_nonzero(near),dtype=np.longdouble)
        for t,w in zip((nodes+1)/2,weights/2):
            xx=t*x[near] if axis==0 else x[near]
            yy=t*y[near] if axis==1 else y[near]
            value+=np.longdouble(w)*derivative(f,xx,yy,h[near],axis,2)
        out[near]=value
    return out


def pointwise_ratio(residual,normalizer):
    r=np.abs(np.asarray(residual,dtype=np.longdouble))
    n=np.asarray(normalizer,dtype=np.longdouble)
    out=np.full(r.shape,np.inf,dtype=np.longdouble)
    nonzero=n>0
    np.divide(r,n,out=out,where=nonzero)
    out[(n==0)&(r==0)]=0
    return out,{'zero_normalizers':int(np.sum(n==0)),
                'zero_over_zero':int(np.sum((n==0)&(r==0))),
                'nonzero_over_zero':int(np.sum((n==0)&(r!=0))),
                'normalizers_subnormal_in_float64':int(np.sum((n>0)&(n<np.finfo(float).tiny))),
                'nonfinite_entries':int(np.sum(~np.isfinite(r)|~np.isfinite(n))),
                'floor':None,'arithmetic':'longdouble term products and sums; candidate values are usually float64'}


def canonical_odd_quotient(omega,pts,vel,h,axis,rule,inverse_evaluator=evaluate):
    coord=pts[:,axis]
    scale=np.maximum(1,np.linalg.norm(pts,axis=1))
    near=np.abs(coord)<1e-7*scale
    quotient=np.empty(len(pts),dtype=np.longdouble)
    quotient[~near]=vel[~near,axis]/coord[~near]
    if np.any(near):
        idx=np.where(near)[0];base=pts[idx].copy();base[:,axis]=0
        targets=[]
        for shift in NODES:
            p=base.copy();p[:,axis]=shift*h[idx];targets.append(p)
        allvel=inverse_evaluator(omega,np.concatenate(targets),rule)['velocity'][:,axis].reshape(7,-1)
        quotient[near]=np.sum(WEIGHTS[1][:,None].astype(np.longdouble)*allvel,axis=0)/h[idx]
    return quotient,{'points_using_axis_derivative':int(np.sum(near)),
                    'axis_approximation_threshold_relative':1e-7,
                    'near_axis_approximation':'odd quotient replaced by its axis derivative; O(coordinate^2) for smooth velocity, to be checked by refinement'}


def residual_table(candidate,points,rule=Rule(),hrel=0.003,inverse_evaluator=evaluate,strain_evaluator=origin_strain):
    pts=np.atleast_2d(np.asarray(points,float));x,y=pts[:,0],pts[:,1]
    h=hrel*np.maximum(1,np.hypot(x,y))
    inv=inverse_evaluator(candidate.Omega,pts,rule);u=inv['velocity'].astype(np.longdouble)
    parity_error=np.zeros_like(u)
    parity_error[x==0,0]=u[x==0,0];parity_error[y==0,1]=u[y==0,1]
    # A1 canonical parity gives these exact zeros. Retain discarded quadrature
    # roundoff as an explicit error diagnostic; never zero a near-axis value.
    u[x==0,0]=0;u[y==0,1]=0
    b=np.longdouble(candidate.beta);xx=x.astype(np.longdouble);yy=y.astype(np.longdouble)
    w1=b*xx+u[:,0];w2=b*yy+u[:,1]
    th=np.asarray(candidate.Theta(x,y),dtype=np.longdouble);om=np.asarray(candidate.Omega(x,y),dtype=np.longdouble)
    tx=derivative(candidate.Theta,x,y,h,0,1);ty=derivative(candidate.Theta,x,y,h,1,1)
    ox=derivative(candidate.Omega,x,y,h,0,1);oy=derivative(candidate.Omega,x,y,h,1,1)
    rt=w1*tx+w2*ty-(b-2)*th;ro=w1*ox+w2*oy+om-tx
    nt=np.abs(w1*tx)+np.abs(w2*ty)+abs(b-2)*np.abs(th)
    no=np.abs(w1*ox)+np.abs(w2*oy)+np.abs(om)+np.abs(tx)
    pxx=derivative(candidate.Psi,x,y,h,0,2);pyy=derivative(candidate.Psi,x,y,h,1,2)
    ell=-pxx-pyy-om;ne=np.abs(pxx)+np.abs(pyy)+np.abs(om)
    aa,ainfo=canonical_odd_quotient(candidate.Omega,pts,u,h,0,rule,inverse_evaluator)
    bb,binfo=canonical_odd_quotient(candidate.Omega,pts,u,h,1,rule,inverse_evaluator)
    aa+=b;bb+=b
    f=np.asarray(candidate.F(x,y),dtype=np.longdouble);g=np.asarray(candidate.G(x,y),dtype=np.longdouble)
    fx=derivative(candidate.F,x,y,h,0,1);fy=derivative(candidate.F,x,y,h,1,1)
    gx=derivative(candidate.G,x,y,h,0,1);gy=derivative(candidate.G,x,y,h,1,1)
    fxox=even_derivative_over_coordinate(candidate.F,x,y,h,0)
    dt=aa*xx*fx+bb*yy*fy+(bb-b+2)*f
    do=aa*xx*gx+bb*yy*gy+(aa+bb+1)*g-fxox
    # Preserve each actual reduced transport term, without cancellation or a floor.
    ndt=np.abs(aa*xx*fx)+np.abs(bb*yy*fy)+np.abs(bb*f)+abs(b-2)*np.abs(f)
    ndo=np.abs(aa*xx*gx)+np.abs(bb*yy*gy)+np.abs(aa*g)+np.abs(bb*g)+np.abs(g)+np.abs(fxox)
    # These instead continue exactly the prompt's Cartesian term sums divided
    # by |y| or |xy|. Keep both conventions, explicitly labeled.
    ndt_raw=np.abs(aa*xx*fx)+np.abs(bb*(f+yy*fy))+abs(b-2)*np.abs(f)
    ndo_raw=np.abs(aa*(g+xx*gx))+np.abs(bb*(g+yy*gy))+np.abs(g)+np.abs(fxox)
    hxox=even_derivative_over_coordinate(candidate.H,x,y,h,0)
    hyoy=even_derivative_over_coordinate(candidate.H,x,y,h,1)
    hxx=derivative(candidate.H,x,y,h,0,2);hyy=derivative(candidate.H,x,y,h,1,2)
    de=hxx+2*hxox+hyy+2*hyoy+g
    nde=np.abs(hxx)+2*np.abs(hxox)+np.abs(hyy)+2*np.abs(hyoy)+np.abs(g)
    arrays={'R_Theta':rt,'N_Theta':nt,'R_Omega':ro,'N_Omega':no,'E':ell,'N_E':ne,
            'D_Theta':dt,'ND_Theta':ndt,'D_Omega':do,'ND_Omega':ndo,'D_E':de,'ND_E':nde,
            'U1':u[:,0],'U2':u[:,1],'A':aa,'B':bb,'ND_Theta_raw':ndt_raw,'ND_Omega_raw':ndo_raw}
    if 'psi' in inv:arrays['Psi_inverse_discrepancy']=inv['psi']-candidate.Psi(x,y)
    summary={}
    for rn,nn in [('R_Theta','N_Theta'),('R_Omega','N_Omega'),('E','N_E'),('D_Theta','ND_Theta'),('D_Omega','ND_Omega'),('D_E','ND_E')]:
        ratio,meta=pointwise_ratio(arrays[rn],arrays[nn]);arrays[rn+'_ratio']=ratio
        summary[rn]={'max_abs':float(np.max(np.abs(arrays[rn]))),'max_ratio':float(np.max(ratio)),'zero_handling':meta}
    for key,den in [('D_Theta',ndt_raw),('D_Omega',ndo_raw)]:
        ratio,meta=pointwise_ratio(arrays[key],den);arrays[key+'_ratio_raw']=ratio
        summary[key+'_raw_normalizer']={'max_ratio':float(np.max(ratio)),'zero_handling':meta,'definition':'continuous extension of the exact Cartesian term-sum normalizer divided by the parity factor'}
    summary['reduced_normalizer_convention']='ND_Theta/ND_Omega separate all expanded reduced terms; ND_Theta_raw/ND_Omega_raw preserve the original Cartesian grouping, with axis limits'
    center=np.array([0.0]);a0=float(np.asarray(candidate.F(center,center))[0])
    summary['center']={'beta':float(b),'a0':a0,'canonical_c':strain_evaluator(candidate.Omega,rule),
                       'nondegenerate_a0':bool(a0!=0),'sup_sampled_abs_Omega':float(np.max(np.abs(om))),
                       'sup_sampled_abs_Theta':float(np.max(np.abs(th)))}
    summary['max_abs_raw_inverse_axis_parity_error']=float(np.max(np.abs(parity_error)))
    summary['exact_axis_velocity_handling']='enforce analytically known A1 zeros only on exact axes; raw quadrature violation reported separately'
    summary['max_abs_Psi_inverse_discrepancy']=float(np.max(np.abs(arrays['Psi_inverse_discrepancy']))) if 'psi' in inv else None
    summary['independent_psi_comparison']='computed' if 'psi' in inv else 'not computed by this velocity-only inverse; elliptic FD is separate'
    summary['inverse_rule']=inv['metadata'];summary['hrel']=hrel
    summary['axis_U1_over_x']=ainfo;summary['axis_U2_over_y']=binfo
    return arrays,summary
