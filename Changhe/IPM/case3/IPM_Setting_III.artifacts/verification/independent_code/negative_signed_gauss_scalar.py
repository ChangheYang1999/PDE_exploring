"""Independent scalar Gauss series and log-coordinate Laplace rule, result226v2."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from functools import lru_cache
import math
import numpy as np
from scipy.special import gamma,digamma
from numpy.polynomial.legendre import leggauss
@lru_cache(None)
def params(p):
    a=-p/2;c=.5;beta=1-a;d=1/(1+p);g=a+d
    L=gamma(c)/(gamma(a)*gamma(c-a+1))
    D=digamma(1)+digamma(2)-digamma(a)-digamma(c-a)
    return a,c,beta,d,g,L,D

def gauss_value(p,x,tolerance=2e-16):
    a,c,beta,d,g,L,D=params(float(p))
    if x<0:raise ValueError('Positive real branch only')
    if x<=2:
        u=x/(1+x);term=1.;terms=[1.]
        for n in range(1,400):
            term*=((a-1+n-1)*(c-a+n-1)/((c+n-1)*n))*u;terms.append(term)
            if abs(term)<tolerance*max(1.,abs(math.fsum(terms))):break
        else:raise ArithmeticError('Pfaff series did not converge')
        return (1+x)**beta*math.fsum(terms)
    B=math.log(x)+D;term=1.;terms=[]
    for k in range(400):
        inc=term*B;terms.append(inc)
        if k>3 and abs(inc)<tolerance*max(1.,abs(math.fsum(terms))):break
        term*=((a+k)*(c-a-k-1)/((k+1)*(k+2)))/x
        B+=1/(k+1)+1/(k+2)-1/(a+k)+1/(c-a-k-1)
    else:raise ArithmeticError('Inverse-argument series did not converge')
    return L*x**beta*(1+beta*(c-a)/x*math.fsum(terms))

def laplace_large_ratio(p,z,lam,order=16,step=1.):
    a,c,beta,d,g,L,D=params(float(p));q=z*z/lam
    lo=-120.;hi=math.log(100.);edges=np.linspace(lo,hi,math.ceil((hi-lo)/step)+1);nodes,weights=leggauss(order);terms=[]
    for left,right in zip(edges[:-1],edges[1:]):
        mid=(left+right)/2;half=(right-left)/2
        for u,w in zip(nodes,weights):
            v=mid+half*u;t=math.exp(v);J=gauss_value(p,q*t)
            terms.append(half*w*math.exp(-t+g*v)*J/(L*q**beta*gamma(1+d)))
    return math.fsum(terms)
