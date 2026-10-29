"""Exact derivative-operator recurrence with native radial basis evaluation.

Separate implementation for cross-checking existing queued Taylor evaluations.
"""
from fractions import Fraction
from math import comb
from functools import lru_cache
import numpy as np
from scipy.special import eval_jacobi
from numpy.polynomial import legendre as leg,chebyshev as cheb,polynomial as poly
from piecewise_jacobi import JacobiPiecewiseField
from piecewise_precision import expand_ball


def _add(out,key,value):
    if value:out[key]=out.get(key,Fraction(0))+value


@lru_cache(None)
def derivative_operator(a,b):
    if a<0 or b<0:raise ValueError('Nonnegative derivative orders required')
    if a==b==0:return {(0,0,0,0):Fraction(1)}
    which='s' if a else 'z'
    old=derivative_operator(a-1,b) if a else derivative_operator(a,b-1)
    out={}
    for (i,j,p,q),v in old.items():
        if which=='s':
            _add(out,(i,j,p-2,q),v*Fraction(p-q,2))
            _add(out,(i+1,j,p-1,q),v/2)
            _add(out,(i,j+1,p-2,q+1),-v/2)
        else:
            _add(out,(i,j,p-1,q+1),v*(p-q))
            if q:_add(out,(i,j,p-1,q-1),v*q)
            _add(out,(i+1,j,p,q+1),v)
            _add(out,(i,j+1,p-1,q),v)
            _add(out,(i,j+1,p-1,q+2),-v)
    return {k:v for k,v in out.items() if v}


def falling(x,n):
    out=np.ones_like(np.asarray(x,dtype=float))
    for j in range(n):out=out*(x-j)
    return out


def compose3(js,x1,x2,x3,order):
    out=[js[0]]
    if order>=1:out.append(js[1]*x1)
    if order>=2:out.append(js[2]*x1*x1+js[1]*x2)
    if order>=3:out.append(js[3]*x1**3+3*js[2]*x1*x2+js[1]*x3)
    return out


class FastNativeField(JacobiPiecewiseField):
    format='verifier-native-operator-jacobi-v1'
    def __init__(self,metadata,coefficients,**kwargs):
        super().__init__(metadata,coefficients,**kwargs)
        exact=expand_ball(self.metadata,self.coefficients)
        self.cartesian_polynomial_jets={};self.native=[]
        width=max(self.matrices[0,key].shape[1] for key in ['phi','q'])
        self.ball_matrices={key:np.pad(self.matrices[0,key],((0,0),(0,width-self.matrices[0,key].shape[1]))) for key in ['phi','q']}
        for key in ['phi','q']:
            terms=exact[key];C=np.zeros((1+max(a for a,b in terms),1+max(b for a,b in terms)))
            for ab,v in terms.items():C[ab]=float(v)
            self.cartesian_polynomial_jets[key]={(a,b):poly.polyder(poly.polyder(C,m=a,axis=0),m=b,axis=1) for a in range(4) for b in range(4-a)}
        for i,e in enumerate(self.elements):
            L=int(e['nmax']);eye=np.eye(L+1)
            row={'D':[leg.legder(eye,m=j,axis=0) for j in range(4)]}
            if e['kind']=='shell':row['cheb']={key:[cheb.chebder(self.matrices[i,key],m=j,axis=1) for j in range(4)] for key in ['phi','q']}
            self.native.append(row)
        self.evaluator_counts={'calls':0,'points':0}

    def _native_element(self,s,z,order,i):
        e=self.elements[i];data=self.native[i];R=np.sqrt(s+z*z);m=z/R;L=int(e['nmax'])
        V=leg.legvander(m,L);angular=[V[:,:D.shape[0]]@D for D in data['D'][:order+1]]
        radials={}
        if e['kind']=='ball':
            Rb=float(e['Rhi']);x=2*(R/Rb)**2-1;x1=4*R/Rb**2;x2=np.full_like(R,4/Rb**2)
            radials={key:[np.zeros((len(R),L+1)) for _ in range(order+1)] for key in ['phi','q']}
            for n in range(L+1):
                active=np.flatnonzero((self.ball_matrices['phi'][n]!=0)|(self.ball_matrices['q'][n]!=0))
                if not len(active):continue
                js=[];beta=n+.5
                for d in range(order+1):
                    J=np.zeros((len(R),len(active)));mask=active>=d
                    if np.any(mask):
                        k=active[mask];factor=np.ones_like(k,dtype=float)
                        for j in range(d):factor*=.5*(k+beta+1+j)
                        J[:,mask]=factor[None,:]*eval_jacobi(k[None,:]-d,float(d),beta+d,x[:,None])
                    js.append(J)
                physical=compose3(js,x1[:,None],x2[:,None],np.zeros((len(R),1)),order)
                t=(R/Rb)**n
                for key in ['phi','q']:
                    w=self.ball_matrices[key][n,active]
                    base=[P@w for P in physical]
                    for d in range(order+1):
                        radials[key][d][:,n]=sum(comb(d,j)*float(falling(n,d-j))*t/R**(d-j)*base[j] for j in range(d+1))
        elif e['kind']=='shell':
            A=2/np.log(float(e['Rhi'])/float(e['Rlo']));x=A*np.log(R/float(e['Rlo']))-1
            for key in ['phi','q']:
                js=[cheb.chebval(x,C.T).T for C in data['cheb'][key][:order+1]]
                radials[key]=compose3(js,(A/R)[:,None],(-A/R**2)[:,None],(2*A/R**3)[:,None],order)
        else:
            for key in ['phi','q']:
                powers=np.asarray(self.radial_keys[i,key]);C=self.matrices[i,key]
                base=(R[:,None]/float(e['Rlo']))**(-powers[None,:])
                radials[key]=[((base*falling(-powers,d)[None,:])@C.T)/R[:,None]**d for d in range(order+1)]
        out={}
        for key in ['phi','q']:
            native={(i,j):np.sum(radials[key][i]*angular[j],axis=1) for i in range(order+1) for j in range(order+1-i)}
            out[key]={}
            for a in range(order+1):
                for b in range(order+1-a):
                    out[key][a,b]=sum(float(c)*R**p*m**q*native[i,j] for (i,j,p,q),c in derivative_operator(a,b).items())
        return out

    def jets(self,s,z,order,*,element=None):
        if order not in range(4):raise ValueError('Implemented through total (s,z) order three')
        s,z=np.broadcast_arrays(np.asarray(s,dtype=float),np.asarray(z,dtype=float))
        if np.any(s<0) or not np.all(np.isfinite(s)) or not np.all(np.isfinite(z)):raise ValueError('Invalid coordinates')
        if element is None and self._cache is not None:
            os,oz,oo,out=self._cache
            if oo>=order and np.array_equal(s,os) and np.array_equal(z,oz):return {key:{ab:v for ab,v in jet.items() if sum(ab)<=order} for key,jet in out.items()}
        shape=s.shape;sn=s.ravel()/self.dilation**2;zn=z.ravel()/self.dilation;R=np.sqrt(sn+zn*zn)
        self.evaluator_counts['calls']+=1;self.evaluator_counts['points']+=R.size
        ids=np.searchsorted([float(e['Rhi']) for e in self.elements[:-1]],R,side='left') if element is None else np.full(R.shape,element)
        if np.any((ids<0)|(ids>2)):raise ValueError('Invalid element')
        near=(ids==0)&(R<.1*float(self.elements[0]['Rhi']))
        out={key:{(a,b):np.zeros_like(R) for a in range(order+1) for b in range(order+1-a)} for key in ['phi','q']}
        if np.any(near):
            for key in out:
                for ab in out[key]:out[key][ab][near]=poly.polyval2d(sn[near],zn[near],self.cartesian_polynomial_jets[key][ab])
        for i in range(3):
            hit=(ids==i)&~near
            if not np.any(hit):continue
            values=self._native_element(sn[hit],zn[hit],order,i)
            for key in out:
                for ab in out[key]:out[key][ab][hit]=values[key][ab]
        for key in out:
            for (a,b),v in out[key].items():out[key][a,b]=(v*self.dilation**((1 if key=='phi' else 0)-2*a-b)).reshape(shape)
        if element is None:self._cache=(s.copy(),z.copy(),order,out)
        return out

    def dilate(self,L):
        return FastNativeField(self.metadata,self.coefficients,dilation=self.dilation*L,provenance=self.provenance)
