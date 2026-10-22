"""Independent parity-folded full-plane quadrature in a positive mixed chart.

No solver, teammate code, finite physical boundary or imposed exterior field.
The exact identities and limitations are in research/mixed_quadrant_inverse/PROOF.md.
Every finite quadrature is approximate. Refine nodes/partitions/scales independently.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq


def folded_direct(a,b,x,y):
    a,b,x,y=np.broadcast_arrays(np.longdouble(a),np.longdouble(b),np.asarray(x,dtype=np.longdouble),np.asarray(y,dtype=np.longdouble))
    out=np.zeros(x.shape+(2,),dtype=np.longdouble)
    for s in [-1,1]:
        for t in [-1,1]:
            dx,dy=a-s*x,b-t*y;d=dx*dx+dy*dy
            out[...,0]+=s*t*dy/d;out[...,1]-=s*t*dx/d
    return out/(2*np.longdouble(str(math.pi)))


def folded_rational(a,b,x,y):
    """Scaled numerator/product formula; use far from its physical poles."""
    a,b,x,y=np.broadcast_arrays(np.longdouble(a),np.longdouble(b),np.asarray(x,dtype=np.longdouble),np.asarray(y,dtype=np.longdouble))
    R=a*a+b*b+x*x+y*y
    aa,bb,xx,yy=a*a/R,b*b/R,x*x/R,y*y/R
    xy=x*y/R;D=np.ones_like(R)
    for s in [-1,1]:
        for t in [-1,1]:D*=((a-s*x)**2+(b-t*y)**2)/R
    p=8*a/R*xy*(4*bb-1-4*bb*yy+4*aa*xx)/D
    q=8*b/R*xy*(1-4*aa-4*bb*yy+4*aa*xx)/D
    return np.stack([p,q],axis=-1)/(2*np.longdouble(str(math.pi)))


def folded_kernel(a,b,x,y,switch=2.):
    x,y=np.broadcast_arrays(np.asarray(x),np.asarray(y));out=np.empty(x.shape+(2,),dtype=np.longdouble)
    far=np.hypot(x,y)>switch*max(1.,math.hypot(a,b))
    if np.any(far):out[far]=folded_rational(a,b,x[far],y[far])
    if np.any(~far):out[~far]=folded_direct(a,b,x[~far],y[~far])
    return out


def source_map(t,L,p):
    return L*t/(1-t)**p,L*(1+(p-1)*t)/(1-t)**(p+1)


def inverse_map(x,L,p):
    if x==0:return 0.
    if p==1:return x/(L+x)
    return brentq(lambda t:L*t-x*(1-t)**p,0.,1.,xtol=2e-15,rtol=2e-15)


def compact_nodes(n,Lx,Le,a,eta,breaks=(0.,.1,.3,.6,.85,.97,1.),powers=(1.,1.),infinity_corner=True):
    """Return compact Gauss cells, replacing target-incident cells by two triangles."""
    z,w=leggauss(n);z=(z+1)/2;w=w/2;uv=np.meshgrid(z,z,indexing='ij');u,v=uv
    ww=w[:,None]*w[None,:];t0=inverse_map(a,Lx,powers[0]);s0=inverse_map(eta,Le,powers[1])
    tb=sorted(set([float(q) for q in breaks]+[float(t0)]));sb=sorted(set([float(q) for q in breaks]+[float(s0)]))
    if tb[0]!=0 or tb[-1]!=1 or sb[0]!=0 or sb[-1]!=1:raise ValueError('Compact partition must span[0,1]')
    for tlo,thi in zip(tb[:-1],tb[1:]):
        for slo,shi in zip(sb[:-1],sb[1:]):
            if thi<=tlo or shi<=slo:continue
            touches=t0 in[tlo,thi] and s0 in[slo,shi]
            if touches or (infinity_corner and thi==shi==1.):
                tc,sc=(t0,s0) if touches else (1.,1.)
                dt=thi-tc if tc==tlo else tlo-tc;ds=shi-sc if sc==slo else slo-sc
                for tri in [0,1]:
                    tt=tc+dt*(u if tri==0 else u*v);ss=sc+ds*(u*v if tri==0 else u)
                    yield tt.ravel(),ss.ravel(),(ww*abs(dt*ds)*u).ravel(),dict(triangle=tri,target_incident=touches,infinity_incident=not touches)
            else:
                tt=tlo+(thi-tlo)*u;ss=slo+(shi-slo)*v
                yield tt.ravel(),ss.ravel(),(ww*(thi-tlo)*(shi-slo)).ravel(),dict(target_incident=False)


def integrate_velocity(source,target,mixed_eta,n=12,scales=(1.,1.),breaks=(0.,.1,.3,.6,.85,.97,1.),batch=512,switch=2.,powers=(1.,1.),infinity_corner=True,radial_cuts=(1.,10.,100.,1e3,1e4,1e6)):
    """source(x,eta)->dict(y,A,Omega); chart assumptions must be checked separately."""
    a,b=map(float,target);Lx,Le=map(float,scales)
    if min(a,b,mixed_eta)<0 or min(Lx,Le)<=0:raise ValueError('Use nonnegative targets and positive scales')
    if a==b==0:return dict(U=[0.,0.],absolute_integral=[0.,0.],nodes=0,min_A=None,quadrature_scope='Origin value exactly zero by parity')
    total=np.zeros(2,dtype=np.longdouble);absolute=total.copy();regional=np.zeros((len(radial_cuts)+1,2),dtype=np.longdouble);nnode=0;amin=float('inf');rmax=0.;ncell=0
    for tt,ss,weight,info in compact_nodes(n,Lx,Le,a,mixed_eta,breaks,powers,infinity_corner):
        ncell+=1
        for start in range(0,len(tt),batch):
            sl=slice(start,start+batch);t,s=tt[sl],ss[sl];x,jx=source_map(t,Lx,powers[0]);eta,je=source_map(s,Le,powers[1])
            vol=weight[sl]*jx*je
            data=source(x,eta);y,A,Omega=(np.asarray(data[k]) for k in['y','A','Omega'])
            if any(np.any(~np.isfinite(q)) for q in[x,eta,y,A,Omega]) or np.any(A<=0):raise ValueError('Nonfinite source or nonpositive sampled chart')
            ker=folded_kernel(a,b,x,y,switch);terms=ker*(np.asarray(Omega,dtype=np.longdouble)*A*vol)[...,None]
            if np.any(~np.isfinite(terms)):raise FloatingPointError('Nonfinite inverse contribution')
            total+=np.sum(terms,axis=0,dtype=np.longdouble);absolute+=np.sum(abs(terms),axis=0,dtype=np.longdouble)
            r=np.hypot(x,y);bins=np.searchsorted(radial_cuts,r)
            for i in range(len(regional)):
                regional[i]+=np.sum(terms[bins==i],axis=0,dtype=np.longdouble)
            nnode+=len(x);amin=min(amin,float(A.min()));rmax=max(rmax,float(r.max()))
    return dict(U=[float(q) for q in total],absolute_integral=[float(q) for q in absolute],radial_cuts=list(radial_cuts),regional_integral=regional.astype(float).tolist(),nodes=nnode,cells=ncell,min_A=amin,max_sample_radius=rmax,n=n,scales=list(scales),powers=list(powers),infinity_corner=infinity_corner,breaks=list(breaks),kernel_switch=switch,quadrature_scope='Full infinite source domain by compactification; finite-node quadrature, no certified error bound')


def integrate_center_strain(source,n=12,scales=(1.,1.),breaks=(0.,.1,.3,.6,.85,.97,1.),batch=512,powers=(1.,1.),infinity_corner=True,radial_cuts=(1.,10.,100.,1e3,1e4,1e6)):
    Lx,Le=scales;total=np.longdouble(0);absolute=total;regional=np.zeros(len(radial_cuts)+1,dtype=np.longdouble);nnode=0;amin=float('inf');rmax=0.
    for tt,ss,weight,info in compact_nodes(n,Lx,Le,0.,0.,breaks,powers,infinity_corner):
        for start in range(0,len(tt),batch):
            sl=slice(start,start+batch);t,s=tt[sl],ss[sl];x,jx=source_map(t,Lx,powers[0]);eta,je=source_map(s,Le,powers[1])
            vol=weight[sl]*jx*je;data=source(x,eta);y,A,Omega=(np.asarray(data[k]) for k in['y','A','Omega'])
            if any(np.any(~np.isfinite(q)) for q in[x,eta,y,A,Omega]) or np.any(A<=0):raise ValueError('Nonfinite source or nonpositive sampled chart')
            xx,yy=np.asarray(x,dtype=np.longdouble),np.asarray(y,dtype=np.longdouble);r2=xx*xx+yy*yy
            terms=(4/np.longdouble(str(math.pi)))*xx*yy/r2**2*Omega*A*vol
            if np.any(~np.isfinite(terms)):raise FloatingPointError('Nonfinite strain contribution')
            total+=terms.sum(dtype=np.longdouble);absolute+=abs(terms).sum(dtype=np.longdouble)
            r=np.hypot(x,y);bins=np.searchsorted(radial_cuts,r)
            for i in range(len(regional)):regional[i]+=terms[bins==i].sum(dtype=np.longdouble)
            nnode+=len(x);amin=min(amin,float(A.min()));rmax=max(rmax,float(r.max()))
    return dict(c=float(total),absolute_integral=float(absolute),radial_cuts=list(radial_cuts),regional_integral=regional.astype(float).tolist(),nodes=nnode,min_A=amin,max_sample_radius=rmax,n=n,scales=list(scales),powers=list(powers),infinity_corner=infinity_corner,breaks=list(breaks),quadrature_scope='Exact center integral approximated on full infinite domain; no certified error bound')
