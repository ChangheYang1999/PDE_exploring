"""Extended-arithmetic full-space Green quadrature, retaining all raw moments.

The field source and every pressure operation use long double. No finite-radius
boundary condition or harmonic correction is imposed. Quadrature errors are not
enclosed. The optional leading term is subtracted only on the final infinite
interval, and its full-source remainder is retained in quadrature.
"""
import math
import numpy as np
from extended_grid import DT,CT,ExtendedGridField,complex_angular,angular_constants

def gauss_legendre(n):
    if n<2:raise ValueError('at least two nodes required')
    x=np.asarray(np.polynomial.legendre.leggauss(n)[0],dtype=DT)
    def pair(x):
        p0=np.ones_like(x);p1=x.copy()
        for k in range(2,n+1):p0,p1=p1,((2*k-1)*x*p1-(k-1)*p0)/k
        return p1,p0
    for _ in range(5):
        p,p0=pair(x);dp=n*(p0-x*p)/(1-x*x);x-=p/dp
    # Pairing enforces only the exact symmetry of Legendre roots.
    x=(x-x[::-1])/2
    p,p0=pair(x);dp=n*(p0-x*p)/(1-x*x);w=2/((1-x*x)*dp*dp)
    return x,w

def sphere_grid(nmu,nphi,phase):
    mu,wm=gauss_legendre(nmu)
    # h00 = 1/sqrt(4*pi), generated with90-digit mpmath before conversion.
    h00=DT(str(angular_constants(0,0).h00));pi=1/(4*h00*h00)
    phi=2*pi*(np.arange(nphi,dtype=DT)+DT(phase))/nphi
    root=np.sqrt(1-mu*mu)
    x=(root[:,None]*np.cos(phi)[None,:]).reshape(-1);y=(root[:,None]*np.sin(phi)[None,:]).reshape(-1);z=np.repeat(mu,nphi)
    directions=np.column_stack((x,y,z));directions/=np.sqrt(np.sum(directions**2,axis=1))[:,None]
    return directions,np.repeat(wm,nphi)*(2*pi/nphi)

def radial_grid(radii,n,scale):
    rr=np.asarray(radii,dtype=DT);scale=DT(scale)
    if np.any(rr<=0):raise ValueError('positive targets required')
    low=min(np.min(rr),scale);high=max(np.max(rr),scale)
    lo=math.floor(math.log2(float(low/scale)));hi=math.ceil(math.log2(float(high/scale)))+2
    edges=np.unique(np.r_[DT(0),rr,scale*np.power(DT(2),np.arange(lo,hi+1))])
    t,w=gauss_legendre(n);t=(t+1)/2;w=w/2
    nodes=[];weights=[]
    for a,b in zip(edges[:-1],edges[1:]):nodes.extend(a+(b-a)*t);weights.extend((b-a)*w)
    T=edges[-1];nodes.extend(T/t);weights.extend(T*w/t**2)
    return np.asarray(nodes,dtype=DT),np.asarray(weights,dtype=DT),edges

class ExtendedFieldSource:
    def __init__(self,field):self.field=field;self.grid=None
    def __call__(self,radii,directions):
        if self.grid is None or not np.array_equal(self.grid_input,directions):
            self.grid_input=directions.copy();self.grid=ExtendedGridField(self.field,directions)
        _,du,_=self.grid.values(radii,with_linear=False)
        return np.sum(du*np.swapaxes(du,-1,-2),axis=(-1,-2))
    def leading(self,directions,projection):
        if self.grid is None:self([DT(1)],directions)
        _,du,_=self.grid.values([DT(1)],with_linear=False,exterior=True)
        f=np.sum(du*np.swapaxes(du,-1,-2),axis=(-1,-2))[0]
        a=f@projection.real+CT(1j)*(f@projection.imag)
        return {'alpha':self.grid.alpha,'kappa':self.grid.omega/self.grid.c,'coefficients':a,'log_coefficients':np.zeros_like(a)}

class ExtendedPressure:
    def __init__(self,source,radii,lmax,nr=24,nmu=48,nphi=96,scale=1.,phase=DT('.473'),batch=8,leading_tail=True,progress=None):
        self.lmax=lmax;self.directions,self.angular_weights=sphere_grid(nmu,nphi,phase)
        yy,_,self.labels=complex_angular(self.directions,lmax)
        projection=yy.conj()*self.angular_weights[:,None]
        self.nodes,self.weights,self.edges=radial_grid(radii,nr,scale);self.tail_start=self.edges[-1]
        parts=[]
        for i in range(0,len(self.nodes),batch):
            rr=self.nodes[i:i+batch];f=np.asarray(source(rr,self.directions),dtype=DT)
            if f.shape!=(len(rr),len(self.directions)) or not np.isfinite(f).all():raise ValueError('invalid source values')
            parts.append(f@projection.real+CT(1j)*(f@projection.imag))
            if progress:progress(min(i+batch,len(self.nodes)),len(self.nodes))
        self.source_coefficients=np.concatenate(parts);self.tail=None
        if leading_tail:
            self.tail=source.leading(self.directions,projection);tail=self.tail;mask=self.nodes>self.tail_start
            exponent=-2*tail['alpha']-2+CT(1j)*self.labels[:,1]*tail['kappa'];r=self.nodes[mask,None]
            self.source_coefficients[mask]-=(tail['coefficients'][None,:]+tail['log_coefficients'][None,:]*np.log(r))*r**exponent[None,:]
        self.configuration={'n_r_per_panel':nr,'n_mu':nmu,'n_phi':nphi,'phase':str(phase),'lmax':lmax,'radial_nodes':len(self.nodes),'tail_start':str(self.tail_start),'mantissa_bits':np.finfo(DT).nmant,'raw_moments_retained':True}
    def tail_integral(self,power):
        if self.tail is None:return np.zeros(len(self.labels),dtype=CT)
        t=self.tail;e=np.asarray(power,dtype=DT)-2*t['alpha']-1+CT(1j)*self.labels[:,1]*t['kappa']
        if np.any(e.real>=0):raise ValueError('nonintegrable tail moment')
        return self.tail_start**e/(-e)*(t['coefficients']+t['log_coefficients']*(np.log(self.tail_start)-1/e))
    def coefficients(self,radii):
        rr=np.asarray(radii,dtype=DT);ell=self.labels[:,0];s=self.nodes;q=self.weights[:,None]*self.source_coefficients
        if np.any(np.diff(rr)<=0) or rr[0]<=0 or rr[-1]>=self.tail_start:raise ValueError('strictly increasing positive targets below tail required')
        if any(not np.any(r==self.edges) for r in rr):raise ValueError('targets must be exact panel edges')
        inner=np.zeros((len(rr),len(ell)),dtype=CT);outer=np.zeros_like(inner);previous=DT(0);v=np.zeros(len(ell),dtype=CT)
        for i,r in enumerate(rr):
            mask=(s>=previous)&(s<r);v=(previous/r)**(ell+1)*v+np.sum(q[mask]*r*(s[mask,None]/r)**(ell+2),axis=0);inner[i]=v;previous=r
        r=rr[-1];mask=s>=r;v=np.sum(q[mask]*s[mask,None]*(r/s[mask,None])**ell,axis=0)
        if self.tail is not None:
            t=self.tail;T=self.tail_start;e=-ell-2*t['alpha']+CT(1j)*self.labels[:,1]*t['kappa']
            v+=(r/T)**ell*T**(-2*t['alpha']+CT(1j)*self.labels[:,1]*t['kappa'])*(t['coefficients']+t['log_coefficients']*(np.log(T)-1/e))/(-e)
        outer[-1]=v
        for i in range(len(rr)-2,-1,-1):
            a,b=rr[i:i+2];mask=(s>=a)&(s<b);v=(a/b)**ell*v+np.sum(q[mask]*s[mask,None]*(a/s[mask,None])**ell,axis=0);outer[i]=v
        return (inner+outer)/(2*ell+1),(-(ell+1)*inner+ell*outer)/(rr[:,None]*(2*ell+1))
    def values(self,radii,directions):
        rr=np.asarray(radii,dtype=DT);n=np.asarray(directions,dtype=DT);n=n/np.sqrt(np.sum(n*n,axis=1))[:,None]
        yy,dh,labels=complex_angular(n,self.lmax)
        if not np.array_equal(labels,self.labels):raise ValueError('harmonic labels differ')
        gs=dh-n[:,None,:]*yy[:,:,None]*labels[None,:,0,None]
        pc,dp=self.coefficients(rr);p=pc@yy.T;radial=dp@yy.T
        tangent=((pc/rr[:,None])@gs.transpose(1,0,2).reshape(len(labels),-1)).reshape(len(rr),len(n),3)
        gp=tangent+radial[:,:,None]*n[None,:,:]
        return p.real,gp.real,max(np.max(abs(p.imag)),np.max(abs(gp.imag)))
