"""Independent global analytic B2 representation, proved in research/42.
No fitting-lane imports, interpolation, finite box, or external source.
Only NumPy and standard-library code. All spatial derivatives are analytic.
"""
from dataclasses import dataclass
import math
import numpy as np


def falling(a, n):
    out=1.
    for j in range(n):out*=a-j
    return out


def polynomial(k,imag=False,divide_x=False,dx=0,dy=0):
    terms=[]
    for l in range(k+1):
        c=math.comb(k,l)*(1j**l)
        c=float(c.imag if imag else c.real)
        if c==0:continue
        xx=k-l-int(divide_x);yy=l
        if xx<0:raise ValueError('polynomial not divisible by x')
        if xx<dx or yy<dy:continue
        terms.append((c*falling(xx,dx)*falling(yy,dy),xx-dx,yy-dy))
    return terms


def poly_eval(terms,x,y):
    out=np.zeros_like(x)
    for c,i,j in terms:out+=c*x**i*y**j
    return out


def radial(q,a,j,special=False,maxder=3):
    L=np.log1p(q)
    if special:
        z=a*L
        f=L.copy() if a==0 else np.expm1(z)/a
        out=[f]
        for d in range(1,maxder+1):out.append(falling(a-1,d-1)*np.exp((a-d)*L))
        return out
    out=[]
    b=a-j
    for d in range(maxder+1):
        ans=np.zeros_like(q)
        for i in range(min(j,d)+1):
            c=math.comb(d,i)*falling(j,i)*falling(b,d-i)
            if c:ans+=c*q**(j-i)*np.exp((b-d+i)*L)
        out.append(ans)
    return out


def stream_term(points,beta,label):
    k,n,j=label;x,y=points.T;q=x*x+y*y;imag=(k%2==0)
    a=(2-n/beta-k)/2
    f,fp,fpp,fppp=radial(q,a,j,k==1 and j==0)
    P=poly_eval(polynomial(k,imag),x,y)
    Px=poly_eval(polynomial(k,imag,dx=1),x,y)
    R=poly_eval(polynomial(k,imag,divide_x=True),x,y)
    Rx=poly_eval(polynomial(k,imag,divide_x=True,dx=1),x,y)
    Ry=poly_eval(polynomial(k,imag,divide_x=True,dy=1),x,y)
    lf=4*q*fpp+4*(k+1)*fp;lpf=4*q*fppp+4*(k+2)*fpp
    return {'A':-Ry*f-2*y*R*fp,'B':Px*f+2*x*P*fp,
            'G':-R*lf,'Gx':-Rx*lf-2*x*R*lpf,'Gy':-Ry*lf-2*y*R*lpf,
            'Psi':P*f}


def temperature_term(points,beta,label):
    l,h,j=label;x,y=points.T;q=x*x+y*y;imag=(l%2==1)
    a=-(1+(h+2)/beta+l)/2
    f,fp=radial(q,a,j,maxder=1)
    P=poly_eval(polynomial(l,imag),x,y)
    Px=poly_eval(polynomial(l,imag,dx=1),x,y)
    Py=poly_eval(polynomial(l,imag,dy=1),x,y)
    return {'F':P*f,'Fx':Px*f+2*x*P*fp,'Fy':Py*f+2*y*P*fp}


@dataclass(frozen=True)
class Resolution:
    angular:int=6
    tails:int=3
    radial:int=1


class GlobalBasis:
    def __init__(self,points,beta,resolution=Resolution()):
        self.points=np.atleast_2d(np.asarray(points,dtype=float));self.beta=float(beta);self.resolution=resolution
        if beta<2:raise ValueError('search restricted to beta>=2 by proved exclusion')
        r=resolution;self.stream_labels=[(k,n,j) for k in range(1,r.angular+1) for n in range(1,r.tails+1) for j in range(r.radial+1) if (k,n,j) not in ((1,1,0),(2,1,0))]
        self.temperature_labels=[(l,h,j) for l in range(r.angular) for h in range(r.tails) for j in range(r.radial+1) if (l,h,j)!=(0,0,0)]
        self.nv=len(self.stream_labels);self.nf=len(self.temperature_labels);self.nvar=self.nv+self.nf
        self.part={};self.matrices={};p=self.points
        ref=stream_term(p,beta,(1,1,0));strain=stream_term(p,beta,(2,1,0))
        raw=[stream_term(p,beta,label) for label in self.stream_labels]
        for key in ref:
            self.part[key]=-ref[key]/(2*beta)+(1+beta/2)*strain[key]/2
            columns=[]
            for label,item in zip(self.stream_labels,raw):
                k,n,j=label;d=float(k==1 and j<=1);e=float(k==2 and j==0)
                columns.append(item[key]-d*ref[key]-e*strain[key])
            self.matrices[key]=np.stack(columns,axis=1) if columns else np.zeros((len(p),0))
        self.part['A']+=beta;self.part['B']+=beta*p[:,1]
        tref=temperature_term(p,beta,(0,0,0));traw=[temperature_term(p,beta,label) for label in self.temperature_labels]
        for key in tref:
            self.part[key]=tref[key]
            self.matrices[key]=np.stack([item[key]-float(label[0]==0 and label[2]==0)*tref[key] for label,item in zip(self.temperature_labels,traw)],axis=1)

    def fields(self,coeff):
        coeff=np.asarray(coeff);v=coeff[:self.nv];w=coeff[self.nv:]
        return {k:self.part[k]+self.matrices[k]@(w if k in ('F','Fx','Fy') else v) for k in self.part}

    def residual(self,coeff,jacobian=False):
        a=self.fields(coeff);x=self.points[:,0];A=a['A'];B=a['B'];F=a['F'];Fx=a['Fx'];Fy=a['Fy'];G=a['G'];Gx=a['Gx'];Gy=a['Gy'];lam=self.beta-2
        RF=A*(2*F+x*Fx)+B*Fy-lam*F;RG=A*(G+x*Gx)+B*Gy+G-2*F-x*Fx
        result=np.r_[RF,RG]
        if not jacobian:return result
        C=self.matrices;XX=x[:,None];AA=A[:,None];BB=B[:,None]
        Jfv=C['A']*(2*F+x*Fx)[:,None]+C['B']*Fy[:,None]
        Jff=AA*(2*C['F']+XX*C['Fx'])+BB*C['Fy']-lam*C['F']
        Jgv=C['A']*(G+x*Gx)[:,None]+AA*(C['G']+XX*C['Gx'])+C['B']*Gy[:,None]+BB*C['Gy']+C['G']
        Jgf=-2*C['F']-XX*C['Fx']
        return result,np.block([[Jfv,Jff],[Jgv,Jgf]])

    def diagnostics(self,coeff):
        from finite_difference import safe_ratio
        a=self.fields(coeff);x=self.points[:,0];r=np.linalg.norm(self.points,axis=1);A=a['A'];B=a['B'];F=a['F'];Fx=a['Fx'];Fy=a['Fy'];G=a['G'];Gx=a['Gx'];Gy=a['Gy'];lam=self.beta-2
        terms={'F':np.column_stack((2*A*F,A*x*Fx,B*Fy,-lam*F)),
               'G':np.column_stack((A*G,A*x*Gx,B*Gy,G,-2*F,-x*Fx)),
               'Theta':np.column_stack((x*x*A*(2*F+x*Fx),x*x*B*Fy,-lam*x*x*F)),
               'Omega':np.column_stack((x*A*(G+x*Gx),x*B*Gy,x*G,-x*(2*F+x*Fx)))}
        regions={'all':np.ones(len(x),bool),'origin_near':r<.1,'inner':(r>=.1)&(r<1),'middle':(r>=1)&(r<10),'outer':(r>=10)&(r<100),'far':r>=100,'x_axis':x==0,'y_zero':self.points[:,1]==0}
        result={'beta':self.beta,'points':len(x),'coefficient_l2':float(np.linalg.norm(coeff)),'coefficient_max':float(np.max(np.abs(coeff))) if len(coeff) else 0.,'minimum_F':float(F.min()),'max_abs_Omega':float(abs(x*G).max()),'max_abs_Theta':float(abs(x*x*F).max()),'residuals':{}}
        for name,ts in terms.items():
            R=ts.sum(axis=1);N=abs(ts).sum(axis=1);rat=safe_ratio(R,N);row={'zero_N':int((N==0).sum()),'subnormal_terms':int(((abs(ts)>0)&(abs(ts)<np.finfo(float).tiny)).sum()),'regions':{}}
            for reg,mask in regions.items():
                if not mask.any():continue
                off=mask&(x!=0) if name in ('Theta','Omega') else mask
                row['regions'][reg]={'count':int(mask.sum()),'max_absolute':float(abs(R[mask]).max()),'max_normalized':float(rat[off].max()) if off.any() else None}
            result['residuals'][name]=row
        return result


class GlobalField:
    """Scalar-source adapter for independent finite differences/inverse."""
    def __init__(self,beta,coeff,resolution=Resolution()):
        self.beta=beta;self.coeff=np.asarray(coeff);self.resolution=resolution
        basis=GlobalBasis([[0.,0.]],beta,resolution)
        self.stream_weights={(1,1,0):-1/(2*beta),(2,1,0):(1+beta/2)/2}
        for label,value in zip(basis.stream_labels,self.coeff[:basis.nv]):
            self.stream_weights[label]=self.stream_weights.get(label,0.)+value
            k,n,j=label
            if k==1 and j<=1:self.stream_weights[(1,1,0)]-=value
            if k==2 and j==0:self.stream_weights[(2,1,0)]-=value
    def fields(self,x,y):
        x,y=np.broadcast_arrays(x,y);shape=x.shape;p=np.column_stack((x.ravel(),y.ravel()));b=GlobalBasis(p,self.beta,self.resolution);return {k:v.reshape(shape) for k,v in b.fields(self.coeff).items()}
    def theta(self,x,y):return np.asarray(x)**2*self.fields(x,y)['F']
    def omega(self,x,y):
        x,y=np.broadcast_arrays(np.asarray(x,dtype=float),np.asarray(y,dtype=float));q=x*x+y*y;out=np.zeros_like(q)
        for (k,n,j),v in self.stream_weights.items():
            if v==0:continue
            a=(2-n/self.beta-k)/2
            f,fp,fpp=radial(q,a,j,k==1 and j==0,maxder=2)
            P=poly_eval(polynomial(k,k%2==0),x,y)
            out-=v*P*(4*q*fpp+4*(k+1)*fp)
        return out
    def psi(self,x,y):return self.fields(x,y)['Psi']
    def velocity(self,p):
        p=np.atleast_2d(p);a=self.fields(*p.T);return np.column_stack((p[:,0]*(a['A']-self.beta),a['B']-self.beta*p[:,1]))
