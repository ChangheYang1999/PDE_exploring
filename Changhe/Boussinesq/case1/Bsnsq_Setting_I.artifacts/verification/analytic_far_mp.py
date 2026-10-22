"""Independent angular far residual: exact endpoint reduction and MP Taylor algebra.

No fitter code is imported. Arrays are data. The input core patches are checked
but do not enter far coefficients, under the flat-tail proof in research68.
"""
from pathlib import Path
from fractions import Fraction
from math import factorial
import hashlib
import mpmath as mp
import numpy as np


def mpq(value):
    if isinstance(value, Fraction):
        return mp.mpf(value.numerator)/value.denominator
    return mp.mpf(value)


class Taylor:
    """Bivariate Taylor coefficients, divided by the two factorials."""
    def __init__(self, n, coeff):
        self.n = n
        self.c = {(i,j):mpq(coeff.get((i,j),0))
                  for i in range(n+1) for j in range(n+1-i)}

    @property
    def v(self):
        return self.c[0,0]

    def __add__(self, other):
        if not isinstance(other,Taylor):
            other=Taylor(self.n,{(0,0):other})
        n=min(self.n,other.n)
        return Taylor(n,{(i,j):self.c[i,j]+other.c[i,j]
                         for i in range(n+1) for j in range(n+1-i)})
    __radd__=__add__

    def __neg__(self):
        return Taylor(self.n,{key:-v for key,v in self.c.items()})

    def __sub__(self,other):
        return self+-other

    def __rsub__(self,other):
        return -self+other

    def __mul__(self,other):
        if not isinstance(other,Taylor):
            return Taylor(self.n,{key:v*mpq(other) for key,v in self.c.items()})
        n=min(self.n,other.n)
        return Taylor(n,{(i,j):mp.fsum(self.c[k,l]*other.c[i-k,j-l]
                              for k in range(i+1) for l in range(j+1))
                         for i in range(n+1) for j in range(n+1-i)})
    __rmul__=__mul__

    def reciprocal(self):
        if not self.v:
            raise ZeroDivisionError('zero Taylor constant')
        z=(self-self.v)*(1/self.v)
        term=Taylor(self.n,{(0,0):1})
        out=term
        for _ in range(self.n):
            term=-term*z
            out=out+term
        return out*(1/self.v)

    def __truediv__(self,other):
        if not isinstance(other,Taylor):
            return self*(1/mpq(other))
        return self*other.reciprocal()

    def __rtruediv__(self,other):
        return self.reciprocal()*other

    def derivative(self,dx,de):
        n=self.n-dx-de
        if n<0:
            raise ValueError('insufficient derivative order')
        return Taylor(n,{(i,j):self.c[i+dx,j+de]
                        *(factorial(i+dx)//factorial(i))
                        *(factorial(j+de)//factorial(j))
                        for i in range(n+1) for j in range(n+1-i)})


def derivatives(f,x,e,n):
    sx,se=1+abs(x),1+abs(e)
    values={}
    for total in range(n+1):
        for i in range(total+1):
            j=total-i
            v=mp.diff(lambda u,v:f(x+sx*u,e+se*v),(mp.mpf(0),mp.mpf(0)),(i,j))
            values[i,j]=v/(sx**i*se**j*factorial(i)*factorial(j))
    return Taylor(n,values)


def chebyshev(z,co):
    # Clenshaw recurrence in one variable, independently reduced exact rows.
    b1=b2=mp.mpf(0)
    for v in reversed(co[1:]):
        b0=2*z*b1-b2+mpq(v)
        b2,b1=b1,b0
    return z*b1-b2+mpq(co[0])


class FarModel:
    def __init__(self,rows,se,alpha,a,metadata=None):
        self.rows=rows
        self.se,self.alpha,self.a=map(mpq,(se,alpha,a))
        self.metadata=metadata or {}
        self.c1=-mp.expm1(-self.alpha)/self.alpha
        self.c2=self.alpha*self.c1**2/2

    def generators(self):
        def data(x,e):
            F=x*x+(e/self.se)**6
            w=(e/self.se)**2/F**(mp.mpf(1)/3)
            return F,[chebyshev(2*w-1,row) for row in self.rows]
        def g0(x,e):
            F,p=data(x,e)
            return x*e*F**(mp.mpf(1)/3)*p[0]
        def g1(x,e):
            F,p=data(x,e)
            return self.c1*x*e*F**(mp.mpf(1)/6)*p[1]
        def g2(x,e):
            F,p=data(x,e)
            return x*e*(self.c2*p[1]+self.c1**2*p[2]/2)
        return g0,g1,g2

    def evaluate(self,x,e):
        x,e=map(mpq,(x,e))
        funcs=self.generators()
        g0,g1,g2=[derivatives(f,x,e,n) for f,n in zip(funcs,(5,4,3))]
        A,B=g0.derivative(1,1),g0.derivative(2,0)
        if A.v<=0:
            raise ArithmeticError('Nonpositive limiting chart')
        b=B/A
        dx=lambda f:f.derivative(1,0)-b*f.derivative(0,1)
        dy=lambda f:f.derivative(0,1)/A
        lap=lambda f:dx(dx(f))+dy(dy(f))
        psi0=-g1
        psi1=-2*g2+g1.derivative(1,0)*g1.derivative(0,1)/A
        u1,u2=-dy(psi0),dx(psi0)
        om0,om1=-lap(psi0),-lap(psi1)
        ox,oy=dx(om0),dy(om0)
        X=Taylor(1,{(0,0):x,(1,0):1})
        Y=g0.derivative(1,0)
        terms=[-om1,u1*ox,u2*oy,self.a*b]
        linear=[3*X*ox,3*Y*oy,om0]
        if not x and not e:
            raise ArithmeticError('far origin undefined')
        if not e:
            axis='horizontal'
            div=lambda f:f.c[0,1]/(A.v*x)
        elif not x:
            axis='vertical'
            div=lambda f:(f.c[1,0]-b.v*f.c[0,1])/Y.v
        else:
            axis=None
            div=lambda f:f.v/(x*Y.v)
        values=[v.v for v in terms]
        ds=[div(v) for v in terms]
        ls=[v.v for v in linear]
        ld=[div(v) for v in linear]
        C,N20,N0=mp.fsum(values),mp.fsum(map(abs,values)),mp.fsum(map(abs,ls))
        Cd,N20d,N0d=mp.fsum(ds),mp.fsum(map(abs,ds)),mp.fsum(map(abs,ld))
        return dict(x=x,eta=e,y=Y.v,A=A.v,Omega0=om0.v,Omega1=om1.v,
                    U01=u1.v,U02=u2.v,Omega0_x=ox.v,Omega0_y=oy.v,
                    terms=values,linear=ls,C=C,N20=N20,N0=N0,
                    grouped_ratio=abs(C)/N20 if N20 and axis is None else None,
                    prompt_coefficient=abs(C)/N0 if N0 and axis is None else None,
                    axis=axis,terms_div_xy=ds,C_div_xy=Cd,N20_div_xy=N20d,N0_div_xy=N0d,
                    grouped_div_ratio=abs(Cd)/N20d if N20d else None,
                    prompt_div_coefficient=abs(Cd)/N0d if N0d else None,
                    omega0_Euler_error=3*x*ox.v+3*Y.v*oy.v+om0.v)

    def section(self,w):
        w=mpq(w)
        if not 0<=w<=1:
            raise ValueError('w outside section')
        return self.evaluate(mp.sqrt(1-w**3),self.se*mp.sqrt(w))


def load_far(source):
    source=Path(source)
    benign={'c','a0','J','Kw','m','beta','hist','Nt','Ns','tmin','gauge','alpha','se','gam','l',
            'core','cc','gpu_port','init','n2','nmin','fixa0','inner','lam','lam0'}
    with np.load(source,allow_pickle=False) as z:
        unknown=set(z.files)-benign
        if unknown:
            raise ValueError('unreviewed source keys: '+str(sorted(unknown)))
        if int(z['m'])!=3 or float(z['beta'])!=3 or float(z['gam'])!=0 or float(z['alpha'])<=0:
            raise ValueError('requires beta=m=3, gam=0, alpha>0')
        J,K=int(z['J']),int(z['Kw'])
        c=np.asarray(z['c'])
        if c.size!=(J+1)*(K+1) or not np.isfinite(c).all():
            raise ValueError('invalid outer coefficients')
        co=[[Fraction(float(v)) for v in row] for row in c.reshape(J+1,K+1)]
        rows=[]
        for order in range(3):
            weights=[]
            for n in range(J+1):
                sign=(-1)**n
                weights.append([Fraction(sign),Fraction(-2*sign*n*n),Fraction(4*sign*n*n*(n*n-1),3)][order])
            rows.append([sum((weights[n]*co[n][k] for n in range(J+1)),Fraction(0)) for k in range(K+1)])
        core_metadata=[]
        if 'core' in z or 'cc' in z:
            if not {'core','cc'}<=set(z.files):
                raise ValueError('incomplete core data')
            core=np.asarray(z['core'])
            cc=np.asarray(z['cc']).ravel()
            if core.ndim!=2 or core.shape[1]!=4 or not np.isfinite(core).all() or not np.isfinite(cc).all():
                raise ValueError('invalid core arrays')
            count=0
            for j,k,r,l in core:
                if int(j)!=j or int(k)!=k or j<0 or k<0 or r<=0 or l<=0:
                    raise ValueError('invalid core schema')
                count+=(int(j)+1)*(int(k)+1)
                core_metadata.append([str(Fraction(float(v))) for v in (j,k,r,l)])
            if len(cc)!=count:
                raise ValueError('core coefficient count mismatch')
        se,alpha,a=[Fraction(float(z[k])) for k in ('se','alpha','a0')]
        if se<=0:
            raise ValueError('nonpositive scale')
        meta=dict(source=str(source),sha256=hashlib.sha256(source.read_bytes()).hexdigest(),J=J,Kw=K,
                  source_keys=z.files,core=core_metadata,core_tail_scope='finite rational Gaussian patch schema, research68',
                  se=str(se),alpha=str(alpha),a0=str(a))
    return FarModel(rows,se,alpha,a,meta)


def serialize(value,digits=60):
    if isinstance(value,dict):return {k:serialize(v,digits) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [serialize(v,digits) for v in value]
    if value is None or isinstance(value,(str,int,bool)):return value
    return mp.nstr(value,digits)
