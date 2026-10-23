"""Independent angular Green inverse evaluated by log-radius quadrature.

No producer code is imported. Derivation: research/angular_log_inverse/PROOF.md.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.special import roots_laguerre, roots_legendre
from log_radius_inverse import LogRadiusQCheckpoint


def endpoint_quotient(coeff):
    """Exact binary-rational division (B(t)-B(-1))/(t+1), then rounding."""
    r=[Fraction(float(v)) for v in coeff]
    a=sum((v*(-1)**j for j,v in enumerate(r)),Fraction(0))
    r[0]-=a
    q=[Fraction(0) for _ in r[:-1]]
    for n in range(len(r)-1,1,-1):
        val=2*r[n];q[n-1]+=val
        r[n]=Fraction(0);r[n-1]-=val;r[n-2]-=val/2
    if len(r)>1:
        q[0]+=r[1];r[0]-=r[1];r[1]=Fraction(0)
    assert not any(r)
    rounded=np.array([float(v) for v in q])
    err=sum(abs(Fraction(float(v))-exact) for v,exact in zip(rounded,q))
    return float(a),rounded,float(err)


class QAngular(LogRadiusQCheckpoint):
    def __init__(self,path):
        super().__init__(path)
        self.a,self.quotient,self.quotient_rounding_l1=endpoint_quotient(self.coeff[0])
        self.dcoeff=[np.polynomial.chebyshev.chebder(c) for c in self.coeff]
        self.log_core=math.log(self.L)-self.kappa*math.log(2.)
        self.primitive_order=(self.N+5)//2+2
        nodes,weights=roots_legendre(self.primitive_order)
        self.pnodes=(nodes+1)/2;self.pweights=weights/2
        self.c=-self.a/4+float(self.third_primitive(np.array([1.]))[0])

    def third_primitive(self,sigma):
        sigma=np.asarray(sigma,float)
        u=sigma[...,None]*self.pnodes
        t=2*u-1
        integrand=((1-u)/4+self.kappa*u/2)*(self.polynomial(1,t)-u*self.polynomial(2,t))
        return sigma*np.sum(integrand*self.pweights,axis=-1)

    def beta2_defect(self,logr):
        _,sigma=self.coordinates_log(logr)
        return -self.third_primitive(sigma)

    def h_mode(self,logr,index,derivative=False):
        logr=np.asarray(logr,float)
        if index>=self.M:
            zero=np.zeros_like(logr)
            return (zero,zero) if derivative else zero
        t,sigma=self.coordinates_log(logr);w=(1-t)/2
        j=index
        bj=self.polynomial(j,t)
        bnext=self.polynomial(j+1,t)
        if j==0:
            div=np.polynomial.chebyshev.chebval(t,self.quotient)
            value=sigma*(2*w*div-self.a-w*bnext/2)
        else:
            value=w*sigma**j*(bj-sigma*bnext)/2
        if not derivative:return value
        dj=np.polynomial.chebyshev.chebval(t,self.dcoeff[j])
        dn=np.polynomial.chebyshev.chebval(t,self.dcoeff[j+1]) if j+1<self.M else np.zeros_like(t)
        if j==0:
            ds=-bj+2*w*dj-((1-2*sigma)*bnext+2*sigma*w*dn)/2
        else:
            ds=((j*w-sigma)*sigma**(j-1)*(bj-sigma*bnext)
                +w*sigma**j*(2*dj-bnext-2*sigma*dn))/2
        speed=2*sigma*w/(w+2*self.kappa*sigma)
        return value,ds*speed


class GaussianAngular:
    """Two-mode manufactured field from the proof, independent of Q maps."""
    M=2
    def __init__(self,q=.3,e=.04,ell=1.6):
        self.q=q;self.e=e;self.a=4*q-6*e;self.c=-q;self.cl=ell
        self.log_core=0.
    def _r2(self,logr):return np.exp(np.clip(2*np.asarray(logr,float),-745,math.log(1000.)))
    def h_mode(self,logr,index,derivative=False):
        t=self._r2(logr);ex=np.exp(-t);q=self.q;e=self.e
        if index==0:
            value=self.a*np.expm1(-t)+ex*((-2*q+6*e)*t-e*t*t)
            dt=ex*((-2*q+6*e)-2*e*t-(self.a+(-2*q+6*e)*t-e*t*t))
        elif index==1:
            value=e*ex*(t*t-4*t);dt=e*ex*(-t*t+6*t-4)
        else:value=np.zeros_like(t);dt=value
        return (value,2*t*dt) if derivative else value
    def beta2_defect(self,logr):
        t=self._r2(logr)
        return self.e/2*(-3*np.expm1(-t)+t*np.exp(-t))
    def exact_phi_coeff(self,logr):
        t=self._r2(logr);ex=np.exp(-t)
        p=np.column_stack((-self.q*np.expm1(-t)/2,self.e*t*ex/4))
        d=np.column_stack((self.q*(-np.expm1(-t)+t*ex),self.e*t*(1-t/2)*ex))
        return p,d


class AngularLogInverse:
    def __init__(self,model,order=64):
        self.model=model;self.order=order
        self.nodes,self.weights=roots_laguerre(order)
        self.n=2*np.arange(1,model.M+1)
    def coefficients(self,logr):
        logr=np.asarray(logr,float).reshape(-1);model=self.model
        hh=[];dots=[];aa=[];bb=[]
        for j,n in enumerate(self.n):
            h,dot=model.h_mode(logr,j,derivative=True)
            hh.append(h);dots.append(dot)
            lower=model.h_mode(logr[:,None]-self.nodes/(n+2),j)
            aa.append(np.sum(lower*self.weights,axis=1)/(n+2))
            if n==2:bb.append(model.beta2_defect(logr))
            else:
                upper=model.h_mode(logr[:,None]+self.nodes/(n-2),j+1)
                bb.append(np.sum(upper*self.weights,axis=1)/(n-2))
        h=np.array(hh).T;dot=np.array(dots).T
        alpha=np.array(aa).T;beta=np.array(bb).T
        neighbor=np.column_stack((h[:,1:],np.zeros(len(logr))))
        p=(beta-alpha)/2
        d=(self.n*(alpha+beta)-h-neighbor)/2
        return {'h':h,'dot':dot,'p':p,'d':d}
    def fields(self,logr,theta):
        cf=self.coefficients(logr);theta=np.asarray(theta,float)
        odd=2*np.arange(self.model.M)+1
        sine=np.sin(odd[:,None]*theta);cosine=np.cos(odd[:,None]*theta)
        H=cf['h']@sine;dot=cf['dot']@sine
        htheta=(cf['h']*odd)@cosine
        vr=-(cf['p']*self.n)@np.cos(self.n[:,None]*theta)
        vt=cf['d']@np.sin(self.n[:,None]*theta)
        ur=vr-self.model.c*np.cos(2*theta)
        ut=vt+self.model.c*np.sin(2*theta)
        v2=vr*np.sin(theta)+vt*np.cos(theta)
        fr=(self.model.cl+ur)*(H+dot)+ut*htheta-H+self.model.a*v2
        neighbor=np.column_stack((cf['h'][:,1:],np.zeros(len(cf['h']))))
        dneighbor=np.column_stack((cf['dot'][:,1:],np.zeros(len(cf['dot']))))
        source=(cf['dot']-(self.n-2)*cf['h']+dneighbor+(self.n+2)*neighbor)/2
        srr=(self.n*(cf['p']-cf['d']))@np.cos(self.n[:,None]*theta)-self.model.c*np.cos(2*theta)
        srt=(self.n*self.n*cf['p']-cf['d']-source/2)@np.sin(self.n[:,None]*theta)+self.model.c*np.sin(2*theta)
        grad_radial=H+dot+self.model.a*np.sin(theta)
        grad_angular=htheta+self.model.a*np.cos(theta)
        return dict(H=H,dotH=dot,Htheta=htheta,vr=vr,vt=vt,ur=ur,ut=ut,v2=v2,Fr=fr,
                    Srr=srr,Srtheta=srt,strain=np.hypot(srr,srt),
                    grad_radial=grad_radial,grad_angular=grad_angular,
                    gradient_norm=np.hypot(grad_radial,grad_angular))


def log_grid(z0,z1,panel_width,order):
    edges=np.linspace(z0,z1,int(math.ceil((z1-z0)/panel_width))+1)
    nodes,weights=roots_legendre(order)
    radii=[];ww=[]
    for lo,hi in zip(edges[:-1],edges[1:]):
        radii.extend((lo+hi)/2+(hi-lo)/2*nodes)
        ww.extend((hi-lo)/2*weights)
    return np.array(radii),np.array(ww)


def weighted_diagnostic(model,m,inverse_order=64,radial_order=12,z0=-10.,z1=60.,panel_width=2.,angles=None):
    z,weights=log_grid(z0,z1,panel_width,radial_order)
    angles=angles or (4*model.M+16)
    theta=(np.arange(angles)+.5)*math.pi/(2*angles)
    angular_weight=2*math.pi/angles
    inv=AngularLogInverse(model,inverse_order)
    f=inv.fields(z+model.log_core,theta)
    ww=np.exp((4-2*m)*z)*weights
    integ=lambda values:float(np.sum(ww[:,None]*values)*angular_weight)
    normh=integ(f['H']**2);normf=integ(f['Fr']**2)
    cross=integ(f['H']*f['Fr'])
    t1=((m-1)*model.cl-1)*normh
    t2=m*integ(f['ur']*f['H']**2)
    t3=model.a*integ(f['H']*f['v2'])
    boundary=inv.fields(np.array([z0,z1])+model.log_core,theta)
    flux=.5*np.exp((4-2*m)*np.array([z0,z1]))*np.sum((model.cl+boundary['ur'])*boundary['H']**2,axis=1)*angular_weight
    mass=ww*np.sum(f['H']**2,axis=1)*angular_weight
    median=float(z[np.searchsorted(np.cumsum(mass),normh/2)])
    return dict(m=m,inverse_order=inverse_order,radial_order=radial_order,z_window=[z0,z1],radial_points=len(z),angles=angles,
                E=math.sqrt(normf/normh),h_norm_squared_in_core_units=normh,F_norm_squared_in_core_units=normf,
                T1=t1/normh,T2=t2/normh,T3=t3/normh,HF=cross/normh,
                lower_flux=flux[0]/normh,upper_flux=flux[1]/normh,
                identity_defect=(cross-t1-t2-t3-flux[1]+flux[0])/normh,
                median_log_radius=median+model.log_core,
                scope='Finite log-radius quadrature with an independent canonical Green inverse. Core power canceled before integration. No tail certificate or uniform profile error bound.')
