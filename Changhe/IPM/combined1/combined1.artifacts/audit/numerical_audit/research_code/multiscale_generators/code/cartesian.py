"""Arb Cartesian Taylor jets for mono, leg, legq and scaled legqs generators.

The algebra is proved in ../PROOF.md. No polar division, quadrature or
finite difference is used. Input numbers are exact rationals.
"""
from pathlib import Path
from math import comb,factorial
from fractions import Fraction
import json
from flint import arb,acb,fmpq as Q

def rational(x):
    if isinstance(x,float):
        raise TypeError('supply an exact rational, not a binary64 coefficient')
    v=Fraction(str(x));return Q(v.numerator,v.denominator)
def ar(q):return arb(q.numerator)/arb(q.denominator)
def binomial(a,k):
    v=Q(1)
    for i in range(k):v*= (a-i)/(i+1)
    return v

def convolution(a,b,d):
    out=[arb(0) for _ in range(d+1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b[:d+1-i]):out[i+j]+=x*y
    return out

def positive_power(A,a,d):
    assert A>0
    base=A**ar(a)
    return [base*ar(binomial(a,k))/A**k for k in range(d+1)]

def integer_power(A,w,d):
    assert w>=0
    return [comb(w,k)*A**(w-k) if k<=w else arb(0) for k in range(d+1)]

def bivariate_product(A,B,d):
    out={}
    for (a,b),v in A.items():
        for (i,j),w in B.items():
            if a+b+i+j<=d:out[a+i,b+j]=out.get((a+i,b+j),arb(0))+v*w
    return out

def spec_parts(spec):
    kind=spec[0]
    if kind=='mono':
        assert len(spec)==2;return int(spec[1]),0,0,Q(1)
    if kind=='leg':
        assert len(spec)==3;return int(spec[1]),int(spec[2]),0,Q(1)
    if kind=='legq':
        assert len(spec)==4;return int(spec[1]),int(spec[2]),int(spec[3]),Q(1)
    if kind=='legqs':
        assert len(spec)==5;return int(spec[1]),int(spec[2]),int(spec[3]),rational(spec[4])
    raise ValueError(kind)

def radial_series(s,p,m,spec,d):
    w,n,q,R=spec_parts(spec)
    assert min(m,w,n,q)>=0 and R>0
    A=ar(R*R)+s
    inv=positive_power(A,Q(-1),d)
    z=[-2*ar(R*R)*v for v in inv];z[0]+=1
    one=[arb(1)]+[arb(0) for _ in range(d)]
    if n==0:P=one
    else:
        P0,P=one,z
        for k in range(1,n):
            zP=convolution(z,P,d)
            P0,P=P, [((2*k+1)*zP[i]-k*P0[i])/(k+1) for i in range(d+1)]
    out=convolution(integer_power(s,w,d),positive_power(A,Q(-w-q),d),d)
    out=convolution(out,P,d)
    out=convolution(out,positive_power(1+s,p-m,d),d)
    scale=ar(R**(2*q))
    return [scale*v for v in out]

class GeneratorJet:
    def __init__(self,data,x,y,order=4):
        if isinstance(data,(str,Path)):data=json.loads(Path(data).read_text())
        self.c=rational(data.get('cl',data.get('cl_exact')))
        assert self.c>0
        self.x,self.y=ar(rational(x)),ar(rational(y))
        self.s=self.x*self.x+self.y*self.y;self.order=order
        gamma=1/self.c;delta=1-gamma
        if 'generators' in data:generators=data['generators']
        else:
            assert len(data['order'])==len(data['coefficients'])
            generators=[{'j':j,'m':m,'spec':['mono',k-m],'coef':v}
                        for (j,m,k),v in zip(data['order'],data['coefficients'])]
        grouped={};cache={}
        for g in generators:
            coefficient=rational(g['coef'])
            if coefficient==0:continue
            m=int(g['m']);j=int(g['j']);p=(3+gamma-j*delta)/2
            key=(j,m,tuple(g['spec']))
            if key not in cache:cache[key]=radial_series(self.s,p,m,g['spec'],order)
            if m not in grouped:grouped[m]=[arb(0) for _ in range(order+1)]
            a=ar(coefficient)
            for k,v in enumerate(cache[key]):grouped[m][k]+=a*v
        D={(1,0):2*self.x,(0,1):2*self.y,(2,0):arb(1),(0,2):arb(1)}
        Dp=[{(0,0):arb(1)}]
        for k in range(order):Dp.append(bivariate_product(Dp[-1],D,order))
        z=acb(self.x,self.y);powers=[acb(1)]
        for k in range(2*max(grouped,default=0)):powers.append(powers[-1]*z)
        ii=[acb(0,1)**k for k in range(order+1)]
        self.values={(a,b):arb(0) for a in range(order+1) for b in range(order+1-a)}
        for m,radial in grouped.items():
            H={(a,b):comb(2*m,a+b)*comb(a+b,a)*(powers[2*m-a-b]*ii[b]).real
               for a in range(order+1) for b in range(order+1-a) if a+b<=2*m}
            for k,C in enumerate(radial):
                for index,value in bivariate_product(H,Dp[k],order).items():
                    self.values[index]+=C*value
    def chi(self,a,b):return self.values[a,b]*factorial(a)*factorial(b)
    def fields(self):
        rho=-self.chi(2,1)-self.chi(0,3)
        u1=-self.chi(1,2);u2=self.chi(2,1)
        rx=-self.chi(3,1)-self.chi(1,3);ry=-self.chi(2,2)-self.chi(0,4)
        vx=ar(self.c)*self.x+u1;vy=ar(self.c)*self.y+u2
        return {'rho':rho,'u1':u1,'u2':u2,'rho_x':rx,'rho_y':ry,
                'residual':vx*rx+vy*ry-rho,'velocity_norm':(vx*vx+vy*vy).sqrt(),
                'gradient_norm':(rx*rx+ry*ry).sqrt()}
