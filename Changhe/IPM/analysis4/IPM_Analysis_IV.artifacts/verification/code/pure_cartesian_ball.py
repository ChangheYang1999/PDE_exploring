"""Cartesian interval algebra and independent two-continuation rational tuning."""
from functools import lru_cache
from fractions import Fraction
from gmpy2 import mpq
from flint import arb, arb_poly, fmpq

@lru_cache(None)
def ball(q):
    return arb(fmpq(str(q)))

class Field:
    def __init__(self, degree, lo=0, coefficients=None):
        self.degree=mpq(degree); self.lo=int(lo)
        self.poly=arb_poly([] if coefficients is None else coefficients)
    def coefficient(self,m):
        return self.poly[m-self.lo] if m>=self.lo else arb(0)
    def scale(self,a):
        return Field(self.degree,self.lo,self.poly*a)
    def __add__(self,other):
        assert self.degree==other.degree
        lo=min(self.lo,other.lo)
        a=arb_poly([arb(0)]*(self.lo-lo)+self.poly.coeffs())
        b=arb_poly([arb(0)]*(other.lo-lo)+other.poly.coeffs())
        return Field(self.degree,lo,a+b)
    def __sub__(self,other):return self+other.scale(-1)
    def __mul__(self,other):
        return Field(self.degree+other.degree,self.lo+other.lo,self.poly*other.poly)
    def derivative(self,y=False):
        c=self.poly.coeffs(); out=[arb(0)]*(len(c)+2)
        for j,v in enumerate(c):
            m=self.lo+j
            out[j]+=v*ball((self.degree+m)/2)
            out[j+2]+=v*ball((self.degree-m)/2)*(-1 if y else 1)
        return Field(self.degree-1,self.lo-1,out)
    def sine(self,m):return 2*self.coefficient(m)
    def project(self,maximum,parity,counts,zero_mode=None):
        data=[arb(0)]*(2*maximum+1)
        for j,v in enumerate(self.poly.coeffs()):
            m=self.lo+j
            if m==0 or abs(m)>maximum or m%2!=parity:
                assert v.contains(0),('support',m,str(v))
                counts['support_zero_checks']+=1
            elif m>0:
                assert v.overlaps(-self.coefficient(-m)),('symmetry',m)
                counts['symmetry_checks']+=1
                if m==zero_mode:
                    assert v.contains(0),('compatibility',m,str(v))
                    counts['compatibility_projections']+=1
                else:
                    data[maximum+m]=v;data[maximum-m]=-v
        return Field(self.degree,-maximum,data)
    def norm(self):
        return 2*sum((abs(v) for j,v in enumerate(self.poly.coeffs()) if self.lo+j>0),arb(0))

def sine(degree,m,amplitude):
    data=[arb(0)]*(2*m+1);data[0]=-amplitude/2;data[-1]=amplitude/2
    return Field(degree,-m,data)

def advection(g,f):
    return g.derivative()*f.derivative(True)-g.derivative(True)*f.derivative()

class Tuning:
    def __init__(self,h,Q,B=4):
        self.h,self.Q,self.B=h,Q,B
        self.delta=mpq(2*h,Q)
        self.counts=dict(support_zero_checks=0,symmetry_checks=0,compatibility_projections=0,
                         poisson_coefficient_checks=0,ordered_products=0,provisional_continuations=0)
    def p(self,n):return 1-n*self.delta
    def resonant(self,n):return n%self.Q==0 and 2*self.h*(n//self.Q)-2>0
    def frequency(self,n):return 2*self.h*(n//self.Q)-2
    def poisson(self,f,n,H=None):
        rhs=f.derivative(); P=self.p(n)+1;maximum=self.B*n
        coefficients=[arb(0)]*(2*maximum+1)
        for j,v in enumerate(rhs.poly.coeffs()):
            m=rhs.lo+j;den=mpq(m*m)-P*P
            if not m or abs(m)>maximum or m%2:
                assert v.contains(0),('poisson_support',n,m);continue
            if den:coefficients[maximum+m]=v/ball(den)
            else:assert v.contains(0),('poisson_obstruction',n,m,str(v))
        g=Field(P,-maximum,coefficients)
        if self.resonant(n) and H is not None:g=g+sine(P,self.frequency(n),H)
        g=g.project(maximum,0,self.counts)
        check=g.derivative().derivative().scale(-1)+g.derivative(True).derivative(True)-rhs
        for v in check.poly.coeffs():
            assert v.contains(0),('poisson_residual',n,str(v))
            self.counts['poisson_coefficient_checks']+=1
        return g
    def order(self,n,f,g):
        total=Field(self.p(n))
        for i in range(1,n):
            total=total+advection(g[i],f[n-i]);self.counts['ordered_products']+=1
        return total.scale(ball((1-self.delta)/(self.delta*(n-1)))).project(self.B*n-1,1,self.counts)
    def continuation(self,n,f,g,H):
        ft=dict(f);gt=dict(g);gt[n]=self.poisson(ft[n],n,H)
        for m in range(n+1,n+self.Q+1):
            ft[m]=self.order(m,ft,gt)
            if m<n+self.Q:gt[m]=self.poisson(ft[m],m)
        self.counts['provisional_continuations']+=1
        return ft[n+self.Q].sine(self.frequency(n+self.Q)-1)
    def prefix(self,b,N,progress=None):
        f={1:sine(self.p(1),1,arb(1))+sine(self.p(1),3,b)};g={1:self.poisson(f[1],1)};harmonics=[]
        for n in range(2,N+1):
            fn=self.order(n,f,g)
            if self.resonant(n):
                obstruction=fn.sine(self.frequency(n)-1)
                fn=fn.project(self.B*n-1,1,self.counts,zero_mode=self.frequency(n)-1);f[n]=fn
                R=self.continuation(n,f,g,arb(0));one=self.continuation(n,f,g,arb(1));S=one-R
                assert not S.contains(0),('response_unresolved',n,str(S))
                H=-R/S;g[n]=self.poisson(fn,n,H)
                harmonics.append(dict(n=n,k=n//self.Q,H=H,sigma=S,obstruction=obstruction))
                if progress:progress(n,H,S)
            else:f[n]=fn;g[n]=self.poisson(fn,n)
        return f,g,harmonics

def refine_root(coefficients,interval,steps):
    lo,hi=map(mpq,interval)
    def evaluate(x):
        out=mpq(0)
        for a in reversed(coefficients):out=out*x+mpq(a)
        return out
    flo=evaluate(lo);fhi=evaluate(hi);assert flo*fhi<0
    for _ in range(steps):
        mid=(lo+hi)/2;fm=evaluate(mid)
        assert fm
        if flo*fm<0:hi=mid
        else:lo=mid;flo=fm
    return ball(lo).union(ball(hi)),[str(lo),str(hi)]
