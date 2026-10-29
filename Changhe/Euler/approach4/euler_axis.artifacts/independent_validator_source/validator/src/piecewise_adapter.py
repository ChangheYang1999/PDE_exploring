"""Independent reconstruction of the documented three-element numerics export.

Only BASIS.md, JSON metadata and coefficient/sample arrays are inputs. No
numerics-lane evaluator, differentiation matrix, or solver is imported. All
spatial derivatives are propagated as bivariate Taylor polynomials in s=r^2,z.
The ball uses regular solid Legendre polynomials, including exactly at R=0.
"""
from __future__ import annotations
import hashlib
import json
from math import factorial
from pathlib import Path
import numpy as np
from numpy.polynomial import Legendre, Polynomial
from scipy.special import roots_legendre
from independent_fields import PotentialField
from independent_farfield import angular_data, evaluate_vector


class Taylor2:
    """Arrays of Taylor coefficients (derivative divided by multi-factorial)."""
    def __init__(self, order, size):
        if order not in range(4):
            raise ValueError('implemented derivative orders are 0 through 3')
        self.order, self.size = order, size
        self.indices = [(a,b) for degree in range(order+1) for a in range(degree+1) for b in [degree-a]]
        self.lookup = {ab:i for i,ab in enumerate(self.indices)}
        self.products = [[(self.lookup[a,b],self.lookup[c-a,d-b])
                          for a in range(c+1) for b in range(d+1)] for c,d in self.indices]

    def constant(self, value):
        out=np.zeros((len(self.indices),self.size),dtype=np.float64)
        out[0]=value
        return out

    def variable(self, value, direction):
        out=self.constant(value)
        if self.order: out[self.lookup[direction]]=1.
        return out

    def multiply(self, a, b):
        out=np.empty_like(a)
        for i,pairs in enumerate(self.products):
            out[i]=sum(a[j]*b[k] for j,k in pairs)
        return out

    def power(self, a, exponent):
        if np.any(a[0]<=0): raise ValueError('positive base required for non-polynomial composition')
        u=a/a[0]
        u=u.copy(); u[0]=0.
        out=self.constant(1.); term=self.constant(1.); coefficient=1.
        for n in range(1,self.order+1):
            term=self.multiply(term,u)
            coefficient*= (exponent-n+1)/n
            out+=coefficient*term
        return out*a[0]**exponent

    def log(self,a):
        if np.any(a[0]<=0): raise ValueError('positive argument required')
        u=a/a[0]; u=u.copy(); u[0]=0.
        out=self.constant(np.log(a[0])); term=self.constant(1.)
        for n in range(1,self.order+1):
            term=self.multiply(term,u)
            out+=((-1.)**(n+1)/n)*term
        return out

    def legendre(self,x,nmax,radial_squared=None):
        # radial_squared=None: P_n(x). Otherwise x=z/Rb and
        # radial_squared=(s+z^2)/Rb^2, so this is rho^n P_n(mu).
        out=[self.constant(1.)]
        if nmax: out.append(x)
        for n in range(2,nmax+1):
            previous=out[-2] if radial_squared is None else self.multiply(radial_squared,out[-2])
            out.append(((2*n-1)*self.multiply(x,out[-1])-(n-1)*previous)/n)
        return np.stack(out,axis=1)

    def chebyshev(self,x,kmax):
        out=[self.constant(1.)]
        if kmax: out.append(x)
        for _ in range(2,kmax+1):out.append(2*self.multiply(x,out[-1])-out[-2])
        return np.stack(out,axis=1)

    def expansion(self,angular,radial,coefficients):
        # Matmul once per Taylor channel, then the Taylor product rule.
        weighted=np.einsum('nk,bkp->bnp',coefficients,radial,optimize=True)
        out=np.zeros((len(self.indices),self.size))
        for i,pairs in enumerate(self.products):
            for a,b in pairs:out[i]+=np.sum(angular[a]*weighted[b],axis=0)
        return out


class PiecewiseScalar:
    def __init__(self,owner,which):self.owner,self.which=owner,which
    @property
    def length(self):return float(self.owner.elements[0]['Rhi'])*self.owner.dilation
    def jet(self,s,z,order):
        return self.owner.jets(s,z,order)[self.which]
    def evaluate(self,s,z,ds=0,dz=0):return self.jet(s,z,ds+dz)[ds,dz]


class PiecewiseField(PotentialField):
    format='verifier-independent-piecewise-v1'
    def __init__(self,metadata,coefficients,*,dilation=1.,provenance=None):
        self.metadata=json.loads(json.dumps(metadata))
        self.elements=self.metadata['elements']
        if len(self.elements)!=3 or [e['kind'] for e in self.elements]!=['ball','shell','exterior']:
            raise ValueError('expected the explicitly documented ball/shell/exterior representation')
        self.coefficients={k:np.array(v,dtype=np.float64,copy=True) for k,v in coefficients.items()}
        if not np.isfinite(dilation) or dilation<=0:raise ValueError('invalid dilation')
        self.dilation=float(dilation);self.provenance=provenance or {};self._cache=None
        self.matrices={};self.radial_keys={}
        for i,e in enumerate(self.elements):
            for key in ['phi','q']:
                labels=e.get('labels_'+key,e['labels'])
                values=self.coefficients[f'{key}_el{i}']
                if values.shape!=(len(labels),) or not np.all(np.isfinite(values)):
                    raise ValueError(f'invalid coefficient vector {key}_el{i}')
                ks=sorted(set(float(k) for n,k in labels))
                kmap={k:j for j,k in enumerate(ks)}
                C=np.zeros((int(e['nmax'])+1,len(ks)))
                seen=set()
                for (n,k),v in zip(labels,values):
                    n=int(n);k=float(k)
                    if (n,k) in seen:raise ValueError('duplicate basis label')
                    seen.add((n,k));C[n,kmap[k]]=v
                if e['kind']!='exterior' and ks!=list(range(len(ks))):
                    raise ValueError('expected contiguous Chebyshev degrees')
                self.matrices[i,key]=C;self.radial_keys[i,key]=ks
        c_l=self.metadata.get('cl',self.metadata.get('c_l'))
        super().__init__(PiecewiseScalar(self,'phi'),PiecewiseScalar(self,'q'),c_l)
        if abs(self.alpha-float(self.metadata['alpha']))>5e-14:raise ValueError('inconsistent alpha')

    @classmethod
    def load(cls,path):
        path=Path(path)
        with np.load(path,allow_pickle=False) as data:
            meta=json.loads(str(data['meta_json']))
            coefficients={f'{key}_el{i}':data[f'{key}_el{i}'].copy() for i in range(3) for key in ['phi','q']}
        return cls(meta,coefficients,provenance={'path':str(path.resolve()),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})

    @property
    def interfaces(self):return np.array([float(e['Rhi']) for e in self.elements[:-1]])*self.dilation

    def _element_taylor(self,s,z,order,i):
        algebra=Taylor2(order,len(s));e=self.elements[i]
        sj=algebra.variable(s,(1,0));zj=algebra.variable(z,(0,1))
        tj=sj+algebra.multiply(zj,zj)
        if e['kind']=='ball':
            Rb=float(e['Rhi']);angular=algebra.legendre(zj/Rb,int(e['nmax']),tj/Rb**2)
            x=2*tj/Rb**2-algebra.constant(1.)
        else:
            invR=algebra.power(tj,-.5)
            angular=algebra.legendre(algebra.multiply(zj,invR),int(e['nmax']))
            if e['kind']=='shell':
                x=(algebra.log(tj)-algebra.constant(2*np.log(float(e['Rlo']))))/np.log(float(e['Rhi'])/float(e['Rlo']))-algebra.constant(1.)
        result={}
        for key in ['phi','q']:
            ks=self.radial_keys[i,key]
            if e['kind']=='exterior':
                radial=np.stack([algebra.power(tj/float(e['Rlo'])**2,-k/2) for k in ks],axis=1)
            else:radial=algebra.chebyshev(x,int(ks[-1]))
            result[key]=algebra.expansion(angular,radial,self.matrices[i,key])
        return algebra,result

    def jets(self,s,z,order,*,element=None):
        if order not in range(4):raise ValueError('implemented through third order')
        s,z=np.broadcast_arrays(np.asarray(s,dtype=float),np.asarray(z,dtype=float))
        if np.any(s<0):raise ValueError('s=r^2 must be nonnegative')
        if not np.all(np.isfinite(s)) or not np.all(np.isfinite(z)):raise ValueError('nonfinite coordinates')
        if element is None and self._cache is not None:
            old_s,old_z,old_order,out=self._cache
            if old_order>=order and np.array_equal(s,old_s) and np.array_equal(z,old_z):
                return {key:{ab:v for ab,v in jets.items() if sum(ab)<=order} for key,jets in out.items()}
        shape=s.shape;ss=s.ravel()/self.dilation**2;zz=z.ravel()/self.dilation
        ab=Taylor2(order,1).indices
        results={key:np.zeros((len(ab),ss.size)) for key in ['phi','q']}
        if element is None:
            R=np.sqrt(ss+zz*zz)
            # The documented field value at an interface is the lower-R trace.
            ids=np.searchsorted([float(e['Rhi']) for e in self.elements[:-1]],R,side='left')
        else:
            if element not in range(3):raise ValueError('invalid element')
            ids=np.full(ss.shape,element)
        for i in range(3):
            select=ids==i
            if not np.any(select):continue
            _,values=self._element_taylor(ss[select],zz[select],order,i)
            for key in results:results[key][:,select]=values[key]
        out={}
        for key,values in results.items():
            amplitude=self.dilation if key=='phi' else 1.
            out[key]={(a,b):(values[j]*(factorial(a)*factorial(b)*amplitude/self.dilation**(2*a+b))).reshape(shape)
                      for j,(a,b) in enumerate(ab)}
        if element is None:self._cache=(s.copy(),z.copy(),order,out)
        return out

    def dilate(self,L):
        return PiecewiseField(self.metadata,self.coefficients,dilation=self.dilation*L,provenance=self.provenance)

    def leading_polynomials(self):
        result=[];e=self.elements[-1]
        for key,exponent in [('phi',self.alpha),('q',self.alpha+1)]:
            ks=np.array(self.radial_keys[2,key]);hit=np.flatnonzero(abs(ks-exponent)<1e-12)
            if len(hit)!=1:raise ValueError('exactly one declared leading exponent required')
            coefficients=self.matrices[2,key][:,hit[0]]*float(e['Rlo'])**exponent*self.dilation**(self.alpha+1)
            result.append(Legendre(coefficients).convert(kind=Polynomial))
        return tuple(result)

    def reporting_gauge(self):
        A,B=self.leading_polynomials();mu,w=roots_legendre(96)
        F=evaluate_vector(angular_data(self.alpha,A.coef,B.coef),mu,'F')
        norm2=float(2*np.pi*np.sum(w[:,None]*F*F))
        if not np.isfinite(norm2) or norm2<=0:raise ValueError('invalid leading norm')
        L=norm2**(-1/(2*(1+self.alpha)))
        return self.dilate(L),{'input_leading_squared_norm':norm2,'dilation_L':L,
                               'reported_leading_squared_norm':norm2*L**(2+2*self.alpha)}

    def as_dict(self):
        return {'format':self.format,'metadata':self.metadata,'dilation':self.dilation,
                'coefficients':{k:v.tolist() for k,v in self.coefficients.items()},'provenance':self.provenance}


def spherical_jets(field,R,mu,order=3,*,element=None):
    """Independent chain rule from (s,z) jets to (R,mu) jets, including poles."""
    R,mu=np.broadcast_arrays(np.asarray(R,dtype=float),np.asarray(mu,dtype=float))
    shape=R.shape;R=R.ravel();mu=mu.ravel();a=Taylor2(order,R.size)
    Rj=a.variable(R,(1,0));mj=a.variable(mu,(0,1))
    sj=a.multiply(a.multiply(Rj,Rj),a.constant(1.)-a.multiply(mj,mj));zj=a.multiply(Rj,mj)
    original=field.jets(sj[0],zj[0],order,element=element)
    sj[0]=0.;zj[0]=0.
    sp=[a.constant(1.)];zp=[a.constant(1.)]
    for _ in range(order):sp.append(a.multiply(sp[-1],sj));zp.append(a.multiply(zp[-1],zj))
    result={}
    for key,jet in original.items():
        expanded=a.constant(0.)
        for (ds,dz),v in jet.items():expanded+=a.multiply(sp[ds],zp[dz])*(v/(factorial(ds)*factorial(dz)))
        result[key]={(i,j):(expanded[k]*factorial(i)*factorial(j)).reshape(shape) for k,(i,j) in enumerate(a.indices)}
    return result
