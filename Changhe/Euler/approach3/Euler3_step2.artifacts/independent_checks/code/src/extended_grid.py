"""Fixed-full-field reconstruction in recorded NumPy extended arithmetic.

No production numerical imports. Algebra follows field_reconstruction,
normalized_angular_recurrence and stable_linear_operator/PROOF.md.
"""
from functools import lru_cache
from fractions import Fraction
from decimal import Decimal, localcontext
import numpy as np
from mp_angular_recurrence import AngularReference

DT=np.longdouble
CT=np.clongdouble

class Jet2:
    # Keep NumPy arrays from coercing this jet to an object array.
    __array_priority__ = 1000
    def __init__(self,v,d=None,h=None):
        self.v=np.asarray(v,dtype=DT)
        self.d=np.zeros_like(self.v) if d is None else np.asarray(d,dtype=DT)
        self.h=np.zeros_like(self.v) if h is None else np.asarray(h,dtype=DT)
    def __add__(self,b):
        if not isinstance(b,Jet2):return Jet2(self.v+b,self.d,self.h)
        return Jet2(self.v+b.v,self.d+b.d,self.h+b.h)
    __radd__=__add__
    def __neg__(self):return self*(-1)
    def __sub__(self,b):return self+-b
    def __rsub__(self,b):return -self+b
    def __mul__(self,b):
        if not isinstance(b,Jet2):return Jet2(self.v*b,self.d*b,self.h*b)
        return Jet2(self.v*b.v,self.d*b.v+self.v*b.d,self.h*b.v+2*self.d*b.d+self.v*b.h)
    __rmul__=__mul__
    def power(self,b):
        b=np.asarray(b,dtype=DT);p=self.v**b;p1=b*self.v**(b-1);p2=b*(b-1)*self.v**(b-2)
        return Jet2(p,p1*self.d,p1*self.h+p2*self.d*self.d)
    def log(self):return Jet2(np.log(self.v),self.d/self.v,self.h/self.v-(self.d/self.v)**2)
    def sin(self):return Jet2(np.sin(self.v),np.cos(self.v)*self.d,np.cos(self.v)*self.h-np.sin(self.v)*self.d*self.d)
    def cos(self):return Jet2(np.cos(self.v),-np.sin(self.v)*self.d,-np.sin(self.v)*self.h-np.cos(self.v)*self.d*self.d)
    def select(self,indices):return Jet2(*(x[:,indices] for x in (self.v,self.d,self.h)))

@lru_cache(None)
def angular_constants(lmax,order):return AngularReference(lmax,order,70)

def angular_jets(points,lmax,order=2):
    """Normalized complex regular solid harmonics, m>=0, literal derivatives."""
    xyz=np.asarray(points,dtype=DT);ref=angular_constants(lmax,order);counts=ref.counts
    r2=np.sum(xyz*xyz,axis=1);shape=(len(xyz),len(counts))
    def linear(h,k):
        result=xyz[:,k,None]*h
        for i,a in enumerate(counts):
            if a[k]:result[:,i]+=a[k]*h[:,ref.lower[i][k]]
        return result
    def quadratic(h):
        result=r2[:,None]*h
        for i,a in enumerate(counts):
            for k in range(3):
                if a[k]:result[:,i]+=2*a[k]*xyz[:,k]*h[:,ref.lower[i][k]]
                if a[k]>1:result[:,i]+=a[k]*(a[k]-1)*h[:,ref.lower2[i][k]]
        return result
    h=np.zeros(shape,dtype=CT);h[:,0]=DT(str(ref.h00));data={(0,0):h}
    for m in range(lmax+1):
        if m:data[m,m]=DT(str(ref.diag[m]))*(linear(data[m-1,m-1],0)+CT(1j)*linear(data[m-1,m-1],1))
        if m<lmax:data[m+1,m]=DT(str(ref.vert[m]))*linear(data[m,m],2)
        for ell in range(m+2,lmax+1):
            a,b=ref.ab[ell,m]
            data[ell,m]=DT(str(a))*linear(data[ell-1,m],2)-DT(str(b))*quadratic(data[ell-2,m])
    return data,ref

def real_angular(points,modes):
    data,ref=angular_jets(points,int(np.max(np.asarray(modes)[:,0])),2)
    axes=[()]+[(i,) for i in range(3)]+[tuple(sorted((i,j))) for i in range(3) for j in range(3)]
    index=[ref.axes.index(ax) for ax in axes];sqrt2=DT(str(ref.sqrt2));rows=[]
    for ell,m,kind in modes:
        h=data[int(ell),int(m)];h=h.real if kind==0 else h.imag
        rows.append(h[:,index]*(sqrt2*(-1 if m%2 else 1) if m else DT(1)))
    return np.stack(rows,axis=1)

def complex_angular(points,lmax):
    data,ref=angular_jets(points,lmax,1);values=[];grad=[];labels=[]
    for ell in range(lmax+1):
        for m in range(-ell,ell+1):
            h=data[ell,abs(m)]
            if m<0:h=(-1 if m%2 else 1)*h.conj()
            values.append(h[:,0]);grad.append(h[:,1:4]);labels.append((ell,m))
    return np.stack(values,1),np.stack(grad,1),np.asarray(labels,dtype=int)

@lru_cache(None)
def shifted_chebyshev_integers(n):
    """Integer coefficients of T_k(1-z), with no rounded recurrence."""
    rows=[[1]]
    if n>1:rows.append([1,-1])
    for k in range(2,n):
        v=[0]*(k+1)
        for j,c in enumerate(rows[-1]):v[j]+=2*c;v[j+1]-=2*c
        for j,c in enumerate(rows[-2]):v[j]-=c
        rows.append(v)
    return rows[:n]

def endpoint_coefficients(a):
    """Convert exact represented binary inputs, then round once to long double."""
    rows=shifted_chebyshev_integers(len(a));out=np.zeros_like(a,dtype=DT)
    for col in range(a.shape[1]):
        exact=[Fraction(*x.as_integer_ratio()) for x in a[:,col]]
        for j in range(len(a)):
            b=sum((exact[k]*rows[k][j] for k in range(j,len(a))),Fraction(0))
            with localcontext() as ctx:
                ctx.prec=90
                out[j,col]=DT(str(Decimal(b.numerator)/Decimal(b.denominator)))
    return out

class ExtendedGridField:
    @property
    def coeff(self):return self._coeff
    @coeff.setter
    def coeff(self,values):
        self._coeff={k:np.asarray(v,dtype=DT) for k,v in values.items()}
        self._endpoint={}
    def __init__(self,field,directions):
        if np.finfo(DT).nmant<63:raise RuntimeError('long double has insufficient precision')
        self.c=DT(field.c_l);self.omega=DT(field.omega);self.alpha=(1-self.c)/self.c
        self.r0=DT(field.r0);self.r1=DT(float(field.channels.get('R1') or field.r0));self.damp=int(field.channels['core_damp'])
        self.modes=np.asarray(field.modes,dtype=int);self.ell=self.modes[:,0];self.ms=self.modes[:,1]
        self.coeff={k:np.asarray(v,dtype=DT) for k,v in field.arrays.items() if k in ('A','C','B','D','E')}
        self.partner=np.asarray(field.partner.cpu() if hasattr(field.partner,"cpu") else field.partner,dtype=int);self.sign=np.asarray(field.sign.cpu() if hasattr(field.sign,"cpu") else field.sign,dtype=DT)
        n=np.asarray(directions,dtype=DT);n=n/np.sqrt(np.sum(n*n,axis=1))[:,None];self.directions=n
        table=real_angular(n,self.modes);H,h,K=table[:,:,0],table[:,:,1:4],table[:,:,4:].reshape(len(n),len(self.modes),3,3)
        eye=np.eye(3,dtype=DT);nn=n[:,None,:];C=np.cross(h,nn)
        D=np.swapaxes(np.cross(np.swapaxes(K,-1,-2),n[:,None,None,:]),-1,-2)+np.swapaxes(np.cross(h[:,:,None,:],eye[None,None,:,:]),-1,-2)
        vectors=[C,h,nn*H[:,:,None]]
        matrices=[C[:,:,:,None]*nn[:,:,None,:],D,K,h[:,:,:,None]*nn[:,:,None,:],eye[None,None]*H[:,:,None,None]+nn[:,:,:,None]*h[:,:,None,:],H[:,:,None,None]*nn[:,:,:,None]*nn[:,:,None,:]]
        self.vectors=[np.ascontiguousarray(v.transpose(1,0,2).reshape(len(self.modes),-1)) for v in vectors]
        self.matrices=[np.ascontiguousarray(v.transpose(1,0,2,3).reshape(len(self.modes),-1)) for v in matrices]
    def radial(self,radii,stable=False,exterior=False):
        r=np.asarray(radii,dtype=DT).reshape(-1,1);rho=r*r;q=Jet2(rho,np.ones_like(rho))
        if np.any(r<=0):raise ValueError('positive radii required')
        sr=(q if exterior else q+self.r0**2).power(DT('.5'))*(1/self.r0)
        phase=sr.log()*(self.ms*self.omega/self.c);cs,sn=phase.cos(),phase.sin()
        if exterior:cheb=[q*0+1]
        else:
            t=2*q*((q+self.r0**2).power(DT('.5'))+self.r0).power(-2)-1;cheb=[q*0+1,t]
            for _ in range(2,max(len(a) for a in self.coeff.values())):cheb.append(2*t*cheb[-1]-cheb[-2])
        ratio=q*(q+self.r1**2).power(-1);damp=q*0+1
        for _ in range(self.damp):damp=damp*ratio
        def amp(name):
            a=self.coeff[name]
            if exterior:return (q*0+1)*np.sum(a,axis=0)
            result=cheb[0]*a[0]
            for k in range(1,len(a)):result=result+cheb[k]*a[k]
            far=r>=256*self.r0
            if np.any(far):
                if name not in self._endpoint:self._endpoint[name]=endpoint_coefficients(a)
                ep=self._endpoint[name]
                z=((q+self.r0**2).power(DT('.5'))+self.r0).power(-1)*(4*self.r0)
                val=cheb[0]*ep[-1]
                for j in range(len(ep)-2,-1,-1):val=val*z+ep[j]
                result=Jet2(*(np.where(far,b,c) for b,c in zip((val.v,val.d,val.h),(result.v,result.d,result.h))))
            return result if name in ('A','C') else damp*result
        def twist(b):return b*cs-b.select(self.partner)*self.sign*sn
        core=(q+self.r0**2).power(-1)*self.r0**2
        def term(name,nu,delta,twisted=True):
            b=amp(name)
            if stable:
                if exterior:raise ValueError('stable exterior not needed')
                bq=Jet2(b.d,b.h,np.zeros_like(b.h))
                v=b*(delta+self.c*nu*core)+2*self.c*q*bq
                rotation=b.select(self.partner)*(self.omega*self.sign*self.ms)
                b=v+(core*rotation if twisted else rotation)
            if twisted:b=twist(b)
            return sr.power(-nu)*b
        tor=term('A',self.alpha+self.ell,DT(0));pol=term('C',self.alpha+self.ell-1,DT(0))
        if not exterior:
            if len(self.coeff['B']):tor=tor+term('B',2*self.alpha+1+self.ell,DT(-1))
            if len(self.coeff['D']):pol=pol+term('D',2*self.alpha+self.ell,DT(-1))
            if len(self.coeff['E']):pol=pol+term('E',2*self.ell+1,1-self.c*(self.ell+3),False)*(self.ell>=2)
        return tor,pol
    def values(self,radii,with_linear=True,exterior=False):
        r=np.asarray(radii,dtype=DT).reshape(-1,1);q=r*r;ell=self.ell;f,g=self.radial(radii,exterior=exterior)
        A=(ell+1)*g.v+2*q*g.d;Ap=(ell+3)*g.d+2*q*g.h;B=-2*ell*g.d;Bp=-2*ell*g.h
        vc=[f.v*r**ell,A*r**(ell-1),B*r**(ell+1)]
        dc=[2*f.d*r**(ell+1),f.v*r**(ell-1),A*r**(ell-2),2*Ap*r**ell,B*r**ell,2*Bp*r**(ell+2)]
        u=sum(c@v for c,v in zip(vc,self.vectors)).reshape(len(r),len(self.directions),3)
        du=sum(c@v for c,v in zip(dc,self.matrices)).reshape(len(r),len(self.directions),3,3)
        linear=None
        if with_linear:
            f,g=self.radial(radii,stable=True)
            vc=[f.v*r**ell,((ell+1)*g.v+2*q*g.d)*r**(ell-1),-2*ell*g.d*r**(ell+1)]
            linear=sum(c@v for c,v in zip(vc,self.vectors)).reshape(u.shape)
        if not np.isfinite(u).all() or not np.isfinite(du).all() or (linear is not None and not np.isfinite(linear).all()):raise FloatingPointError('nonfinite extended field')
        return u,du,linear
