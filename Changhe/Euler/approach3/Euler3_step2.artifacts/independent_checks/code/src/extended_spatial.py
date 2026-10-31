"""Independent Cartesian second derivatives and pressure-free vorticity residual.

See research/vorticity_identity/PROOF.md. No production numerical imports.
The stable radial branch is valid through order two, which is sufficient for
its velocity Jacobian. It must not be used for a stable velocity Hessian.
"""
import numpy as np
from extended_grid import DT, angular_jets, endpoint_coefficients

class Jet3:
    __array_priority__=1000
    def __init__(self,v,d=None,h=None,t=None):
        self.v=np.asarray(v,dtype=DT)
        self.d=np.zeros_like(self.v) if d is None else np.asarray(d,dtype=DT)
        self.h=np.zeros_like(self.v) if h is None else np.asarray(h,dtype=DT)
        self.t=np.zeros_like(self.v) if t is None else np.asarray(t,dtype=DT)
    def __add__(self,b):
        if not isinstance(b,Jet3):return Jet3(self.v+b,self.d,self.h,self.t)
        return Jet3(self.v+b.v,self.d+b.d,self.h+b.h,self.t+b.t)
    __radd__=__add__
    def __neg__(self):return self*(-1)
    def __sub__(self,b):return self+-b
    def __rsub__(self,b):return -self+b
    def __mul__(self,b):
        if not isinstance(b,Jet3):return Jet3(self.v*b,self.d*b,self.h*b,self.t*b)
        return Jet3(self.v*b.v,self.d*b.v+self.v*b.d,self.h*b.v+2*self.d*b.d+self.v*b.h,self.t*b.v+3*self.h*b.d+3*self.d*b.h+self.v*b.t)
    __rmul__=__mul__
    def compose(self,f0,f1,f2,f3):
        return Jet3(f0,f1*self.d,f1*self.h+f2*self.d**2,f1*self.t+3*f2*self.d*self.h+f3*self.d**3)
    def power(self,b):
        b=np.asarray(b,dtype=DT)
        return self.compose(self.v**b,b*self.v**(b-1),b*(b-1)*self.v**(b-2),b*(b-1)*(b-2)*self.v**(b-3))
    def log1p(self):
        u=1+self.v
        return self.compose(np.log1p(self.v),1/u,-1/u**2,2/u**3)
    def exp(self):
        a=np.exp(self.v);return self.compose(a,a,a,a)
    def sin(self):
        s,c=np.sin(self.v),np.cos(self.v);return self.compose(s,c,-s,-c)
    def cos(self):
        s,c=np.sin(self.v),np.cos(self.v);return self.compose(c,-s,-c,s)
    def select(self,indices):return Jet3(*(x[:,indices] for x in (self.v,self.d,self.h,self.t)))
    def first_through_order_two(self):return Jet3(self.d,self.h,self.t,np.zeros_like(self.t))


def angular_three(points,modes):
    data,ref=angular_jets(points,int(np.max(np.asarray(modes)[:,0])),3)
    axes=[()]+[(i,) for i in range(3)]+[tuple(sorted((i,j))) for i in range(3) for j in range(3)]+[tuple(sorted((i,j,k))) for i in range(3) for j in range(3) for k in range(3)]
    indices=[ref.axes.index(ax) for ax in axes];root2=DT(str(ref.sqrt2));rows=[]
    for ell,m,kind in modes:
        h=data[int(ell),int(m)];h=h.real if kind==0 else h.imag
        rows.append(h[:,indices]*(root2*(-1 if m%2 else 1) if m else DT(1)))
    table=np.stack(rows,axis=1);nm=len(modes);n=len(points)
    return table[:,:,0],table[:,:,1:4],table[:,:,4:13].reshape(n,nm,3,3),table[:,:,13:].reshape(n,nm,3,3,3)


def assemble(points,ell,f,g,angular,hessian=True):
    y=np.asarray(points,dtype=DT)[:,None,:];q=np.sum(y*y,axis=2)
    H,h,K,T=angular;eye=np.eye(3,dtype=DT);C=np.cross(h,y)
    a=(ell+1)*g.v+2*q*g.d;ap=(ell+3)*g.d+2*q*g.h
    b=-2*ell*g.d;bp=-2*ell*g.h
    u=f.v[:,:,None]*C+a[:,:,None]*h+b[:,:,None]*y*H[:,:,None]
    du=np.empty(u.shape+(3,),dtype=DT)
    cj=[]
    for j in range(3):
        x=np.cross(K[:,:,:,j],y)+np.cross(h,eye[j]);cj.append(x)
        yj=y[:,:,j,None]
        du[:,:,:,j]=2*f.d[:,:,None]*yj*C+f.v[:,:,None]*x+2*ap[:,:,None]*yj*h+a[:,:,None]*K[:,:,:,j]+2*bp[:,:,None]*yj*y*H[:,:,None]+b[:,:,None]*(eye[j]*H[:,:,None]+y*h[:,:,j,None])
    if not hessian:return np.sum(u,axis=1),np.sum(du,axis=1),None
    app=(ell+5)*g.h+2*q*g.t;bpp=-2*ell*g.t
    ddu=np.empty(u.shape+(3,3),dtype=DT)
    for j in range(3):
        for k in range(3):
            yj,yk=y[:,:,j,None],y[:,:,k,None]
            cjk=np.cross(T[:,:,:,j,k],y)+np.cross(K[:,:,:,j],eye[k])+np.cross(K[:,:,:,k],eye[j])
            fj,fk=2*f.d[:,:,None]*yj,2*f.d[:,:,None]*yk
            fjk=2*f.d[:,:,None]*int(j==k)+4*f.h[:,:,None]*yj*yk
            aj,ak=2*ap[:,:,None]*yj,2*ap[:,:,None]*yk
            ajk=2*ap[:,:,None]*int(j==k)+4*app[:,:,None]*yj*yk
            bj,bk=2*bp[:,:,None]*yj,2*bp[:,:,None]*yk
            bjk=2*bp[:,:,None]*int(j==k)+4*bpp[:,:,None]*yj*yk
            ddu[:,:,:,j,k]=fjk*C+fj*cj[k]+fk*cj[j]+f.v[:,:,None]*cjk+ajk*h+aj*K[:,:,:,k]+ak*K[:,:,:,j]+a[:,:,None]*T[:,:,:,j,k]+bjk*y*H[:,:,None]+bj*(eye[k]*H[:,:,None]+y*h[:,:,k,None])+bk*(eye[j]*H[:,:,None]+y*h[:,:,j,None])+b[:,:,None]*(eye[j]*h[:,:,k,None]+eye[k]*h[:,:,j,None]+y*K[:,:,j,k,None])
    return np.sum(u,axis=1),np.sum(du,axis=1),np.sum(ddu,axis=1)


def curl(du):return np.stack((du[...,2,1]-du[...,1,2],du[...,0,2]-du[...,2,0],du[...,1,0]-du[...,0,1]),axis=-1)
def jvector(a):return np.stack((-a[...,1],a[...,0],np.zeros_like(a[...,0])),axis=-1)

class SpatialField:
    def __init__(self,field):
        self.c=DT(field.c_l);self.omega=DT(field.omega);self.alpha=(1-self.c)/self.c
        self.r0=DT(field.r0);self.r1=DT(float(field.channels.get('R1') or field.r0));self.damp=int(field.channels['core_damp'])
        self.modes=np.asarray(field.modes,dtype=int);self.ell=self.modes[:,0];self.ms=self.modes[:,1]
        self.coeff={k:np.asarray(v,dtype=DT) for k,v in field.arrays.items() if k in ('A','C','B','D','E')}
        self.partner=np.asarray(field.partner.cpu() if hasattr(field.partner,'cpu') else field.partner,dtype=int)
        self.sign=np.asarray(field.sign.cpu() if hasattr(field.sign,'cpu') else field.sign,dtype=DT)
        self._endpoint={}
    def radial(self,rho,stable=False):
        rho=np.asarray(rho,dtype=DT).reshape(-1,1)
        if np.any(rho<0):raise ValueError('nonnegative squared radii required')
        q=Jet3(rho,np.ones_like(rho));logsr=(q*(1/self.r0**2)).log1p()*DT('.5')
        phase=logsr*(self.ms*self.omega/self.c);cs,sn=phase.cos(),phase.sin()
        t=2*q*((q+self.r0**2).power(DT('.5'))+self.r0).power(-2)-1
        cheb=[q*0+1,t]
        for _ in range(2,max(len(a) for a in self.coeff.values())):cheb.append(2*t*cheb[-1]-cheb[-2])
        ratio=q*(q+self.r1**2).power(-1);damp=q*0+1
        for _ in range(self.damp):damp=damp*ratio
        def amplitude(name):
            a=self.coeff[name];result=cheb[0]*a[0]
            for k in range(1,len(a)):result=result+cheb[k]*a[k]
            far=rho>=(256*self.r0)**2
            if np.any(far):
                if name not in self._endpoint:self._endpoint[name]=endpoint_coefficients(a)
                ep=self._endpoint[name];z=((q+self.r0**2).power(DT('.5'))+self.r0).power(-1)*(4*self.r0)
                value=cheb[0]*ep[-1]
                for k in range(len(ep)-2,-1,-1):value=value*z+ep[k]
                result=Jet3(*(np.where(far,u,v) for u,v in zip((value.v,value.d,value.h,value.t),(result.v,result.d,result.h,result.t))))
            return result if name in ('A','C') else result*damp
        core=(q+self.r0**2).power(-1)*self.r0**2
        def term(name,nu,delta,twisted=True):
            b=amplitude(name)
            if stable:
                bq=b.first_through_order_two()
                v=b*(delta+self.c*nu*core)+2*self.c*q*bq
                rotation=b.select(self.partner)*(self.omega*self.sign*self.ms)
                b=v+(core*rotation if twisted else rotation)
            if twisted:b=b*cs-b.select(self.partner)*self.sign*sn
            return (logsr*(-nu)).exp()*b
        tor=term('A',self.alpha+self.ell,DT(0));pol=term('C',self.alpha+self.ell-1,DT(0))
        if len(self.coeff['B']):tor=tor+term('B',2*self.alpha+1+self.ell,DT(-1))
        if len(self.coeff['D']):pol=pol+term('D',2*self.alpha+self.ell,DT(-1))
        if len(self.coeff['E']):pol=pol+term('E',2*self.ell+1,1-self.c*(self.ell+3),False)*(self.ell>=2)
        return tor,pol
    def values(self,points):
        points=np.asarray(points,dtype=DT).reshape(-1,3);angular=angular_three(points,self.modes);q=np.sum(points*points,axis=1)
        f,g=self.radial(q);u,du,ddu=assemble(points,self.ell,f,g,angular)
        f,g=self.radial(q,True);linear,dlinear,_=assemble(points,self.ell,f,g,angular,hessian=False)
        om=curl(du);dom=np.stack((ddu[:,2,1,:]-ddu[:,1,2,:],ddu[:,0,2,:]-ddu[:,2,0,:],ddu[:,1,0,:]-ddu[:,0,1,:]),axis=1)
        lv=curl(dlinear);nv=np.einsum('nij,nj->ni',dom,u)-np.einsum('nij,nj->ni',du,om)
        direct=om+self.c*np.einsum('nij,nj->ni',dom,points)+self.omega*(jvector(om)-np.einsum('nij,nj->ni',dom,jvector(points)))
        result={'U':u,'DU':du,'D2U':ddu,'Omega':om,'DOmega':dom,'linear':linear,'Dlinear':dlinear,'linear_vorticity':lv,'direct_linear_vorticity':direct,'nonlinear_vorticity':nv,'vorticity_residual':lv+nv,'divergence':np.trace(du,axis1=1,axis2=2),'grad_divergence':np.einsum('niik->nk',ddu)}
        if not all(np.isfinite(v).all() for v in result.values()):raise FloatingPointError('nonfinite spatial field')
        return result
