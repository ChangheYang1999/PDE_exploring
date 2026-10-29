"""Higher-precision scalar evaluation, separate from the Taylor-jet adapter."""
from fractions import Fraction
from functools import lru_cache
from math import comb,factorial
import json
import mpmath as mp
import numpy as np


def exact(x):
    return Fraction(float(x))


def mpq(x):
    x=Fraction(x)
    return mp.mpf(x.numerator)/x.denominator


@lru_cache(None)
def radial_polynomial(n,k,kind):
    if kind=='jacobi':
        out=[Fraction(0) for _ in range(k+1)]
        for m in range(k+1):
            v=Fraction(comb(k,m));top=Fraction(2*(k+n)+1,2)
            for j in range(k-m):v*= (top-j)/Fraction(j+1)
            for h in range(k-m+1):out[m+h]+=v*comb(k-m,h)*(-1)**(k-m-h)
        return tuple(out)
    if kind not in ['cheb','chebyshev']:raise ValueError('unknown ball basis')
    a=[Fraction(1)]
    if k==0:return tuple(a)
    b=[Fraction(-1),Fraction(2)]
    for _ in range(1,k):
        d=[Fraction(0) for _ in range(len(b)+1)]
        for j,v in enumerate(b):d[j]-=2*v;d[j+1]+=4*v
        for j,v in enumerate(a):d[j]-=v
        a,b=b,d
    return tuple(b)


@lru_cache(None)
def solid_legendre_coefficients(n):
    return tuple(Fraction((-1)**j*factorial(2*n-2*j),2**n*factorial(j)*factorial(n-j)*factorial(n-2*j)) for j in range(n//2+1))


def expand_ball(metadata,coefficients):
    e=metadata['elements'][0];Rb=exact(e['Rhi']);kind=e.get('radial','cheb');out={}
    for key in ['phi','q']:
        d={}
        for (n,k),value in zip(e.get('labels_'+key,e['labels']),coefficients[key+'_el0']):
            n,k=int(n),int(k);v=exact(value)
            if not v:continue
            for h,b in enumerate(radial_polynomial(n,k,kind)):
                if not b:continue
                base=v*b/Rb**(n+2*h)
                for j,a in enumerate(solid_legendre_coefficients(n)):
                    for i in range(j+h+1):
                        ab=(i,n+2*h-2*i)
                        d[ab]=d.get(ab,Fraction(0))+base*a*comb(j+h,i)
        out[key]={ab:v for ab,v in d.items() if v}
    return out


class PrecisionField:
    def __init__(self,metadata,coefficients,dilation=1.):
        self.metadata=metadata;self.coefficients=coefficients;self.dilation=exact(dilation)
        self.ball=expand_ball(metadata,coefficients)
        self.elements=metadata['elements'];self.c_l=exact(metadata.get('cl',metadata.get('c_l')))
    @classmethod
    def load(cls,path,dilation=1.):
        with np.load(path,allow_pickle=False) as a:
            meta=json.loads(str(a['meta_json']))
            co={key+'_el'+str(i):a[key+'_el'+str(i)].copy() for key in ['phi','q'] for i in range(3)}
        return cls(meta,co,dilation)
    def element(self,r,z):
        R=mp.sqrt(r*r+z*z)/mpq(self.dilation)
        for i,e in enumerate(self.elements[:-1]):
            if R<=mpq(exact(e['Rhi'])):return i
        return len(self.elements)-1
    def scalar(self,key,s,z,element):
        L=mpq(self.dilation);s=s/(L*L);z=z/L;amplitude=L if key=='phi' else mp.mpf(1)
        if element==0:return amplitude*mp.fsum(mpq(v)*s**i*z**j for (i,j),v in self.ball[key].items())
        e=self.elements[element];R=mp.sqrt(s+z*z);mu=z/R;nmax=int(e['nmax'])
        angular=[mp.mpf(1),mu]
        for n in range(2,nmax+1):angular.append(((2*n-1)*mu*angular[-1]-(n-1)*angular[-2])/n)
        labels=e.get('labels_'+key,e['labels']);co=self.coefficients[key+'_el'+str(element)]
        if e['kind']=='shell':
            lo=mpq(exact(e['Rlo']));hi=mpq(exact(e['Rhi']));x=2*mp.log(R/lo)/mp.log(hi/lo)-1
            kmax=max(int(k) for n,k in labels);rad=[mp.mpf(1),x]
            for k in range(2,kmax+1):rad.append(2*x*rad[-1]-rad[-2])
            return amplitude*mp.fsum(mpq(exact(v))*angular[int(n)]*rad[int(k)] for (n,k),v in zip(labels,co) if v)
        if e['kind']=='exterior':
            lo=mpq(exact(e['Rlo']))
            return amplitude*mp.fsum(mpq(exact(v))*angular[int(n)]*(R/lo)**(-mpq(exact(k))) for (n,k),v in zip(labels,co) if v)
        raise ValueError('unknown element')
    def jet(self,key,s,z,order,element):
        if element!=0:
            f=lambda ss,zz:self.scalar(key,ss,zz,element)
            return {(a,b):mp.diff(f,(s,z),(a,b)) for d in range(order+1) for a in range(d+1) for b in [d-a]}
        L=mpq(self.dilation);ss=s/(L*L);zz=z/L;amp=L if key=='phi' else mp.mpf(1);out={}
        for d in range(order+1):
            for a in range(d+1):
                b=d-a
                terms=[mpq(v)*mp.mpf(factorial(i)//factorial(i-a))*mp.mpf(factorial(j)//factorial(j-b))*ss**(i-a)*zz**(j-b)
                       for (i,j),v in self.ball[key].items() if i>=a and j>=b]
                out[a,b]=amp*mp.fsum(terms)/L**(2*a+b)
        return out
    def point(self,r,z,element=None):
        r=mpq(exact(r));z=mpq(exact(z));s=r*r;c=mpq(self.c_l)
        if element is None:element=self.element(r,z)
        p=self.jet('phi',s,z,3,element);q=self.jet('q',s,z,1,element)
        U=mp.matrix([-r*p[0,1],r*q[0,0],2*p[0,0]+2*s*p[1,0]])
        J=mp.matrix([[-p[0,1]-2*s*p[1,1],-q[0,0],-r*p[0,2]],
                     [q[0,0]+2*s*q[1,0],-p[0,1],r*q[0,1]],
                     [8*r*p[1,0]+4*r*s*p[2,0],0,2*p[0,1]+2*s*p[1,1]]])
        eta=-8*p[1,0]-4*s*p[2,0]-p[0,2]
        es=-12*p[2,0]-4*s*p[3,0]-p[1,2];ez=-8*p[1,1]-4*s*p[2,1]-p[0,3]
        W=c*mp.matrix([r,0,z])+U
        rq=q[0,0]+2*s*(c-p[0,1])*q[1,0]+W[2]*q[0,1]-2*p[0,1]*q[0,0]
        re=(1+c)*eta+2*s*(c-p[0,1])*es+W[2]*ez-2*q[0,0]*q[0,1]
        M=(1-c)*U+J*W;f=mp.fsum(J[i,j]*J[j,i] for i in range(3) for j in range(3))
        return dict(element=element,velocity=list(U),jacobian=[[J[i,j] for j in range(3)] for i in range(3)],
                    primitive_without_pressure=list(M),source=f,q_residual=rq,eta_residual=re,eta=eta,
                    phi_jets={str(ab):v for ab,v in p.items()},q_jets={str(ab):v for ab,v in q.items()})
