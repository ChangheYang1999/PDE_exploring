"""Exact finite angular cusp functional. Own derivation: result229/PROOF.md."""
from fractions import Fraction as F
from math import comb
import mpmath as mp

def rising(a,n):
    out=F(1)
    for j in range(n):out*=a+j
    return out

def choose(a,n):
    out=F(1)
    for j in range(n):out*=F(a-j,j+1)
    return out

def exactmp(a):
    a=F(a);return mp.mpf(a.numerator)/a.denominator

def kernel(p,M):
    p=F(p);alpha=(1-p)/2;beta=(p+2)/2
    if not 0<p<1:raise ValueError('requires0<p<1')
    return [sum(((-1)**j*comb(2*k,2*j)*rising(F(3,2),j)*rising(-beta,k-j) for j in range(k+1)),F(0))/rising(alpha,k) for k in range(M)]

def rational_data(p,b,L=20):
    p=F(p);b=list(map(F,b));w=kernel(p,len(b))
    A=[sum((bk*sum(((-1)**(k-m)*comb(2*k,2*m)*choose((p-1)/2-k,ell-m)for m in range(min(k,ell)+1)),F(0))for k,bk in enumerate(b)),F(0))for ell in range(L+1)]
    return dict(K=sum(((-1)**k*bk for k,bk in enumerate(b)),F(0)),Q=2*A[1],Cp_rational=sum((bk*wk for bk,wk in zip(b,w)),F(0)),kernel=w,A=A)

def factor(p):
    p=exactmp(p);return (p+1)*(p+2)/2*mp.beta(mp.mpf('1.5'),-(p+2)/2)

def cusp(p,b):
    return factor(p)*sum((exactmp(bk*wk)for bk,wk in zip(b,kernel(p,len(b)))),mp.mpf(0))

def monomial_cusp(p,b):
    p=exactmp(p);beta=(p+2)/2;terms=[]
    for k,bk in enumerate(b):
        a=(p-1)/2-k
        for j in range(k+1):
            n=2*(k-j);x=j+mp.mpf('1.5');y=k-j-beta
            row=n*(n-1)*mp.beta(x,y)+2*a*(2*n+1)*mp.beta(x,y+1)+4*a*(a-1)*mp.beta(x,y+2)
            terms.append(exactmp(bk)*(-1)**j*comb(2*k,2*j)*row/2)
    return mp.fsum(terms),mp.fsum(map(abs,terms))

def tail(p,b,S,L=20,data=None):
    if L<2 or S<=2:raise ValueError('L>=2 and S>2 required')
    pp=F(p);data=data or rational_data(pp,b,L);p=exactmp(pp);S=mp.mpf(S);R0=mp.mpf('.25');q=1/(R0*S*S)
    val=mp.fsum(2*ell*(2*ell-1)*exactmp(data['A'][ell])*S**(p-2*ell+2)/(2*ell-p-2)for ell in range(2,L+1))
    M0=mp.fsum(abs(exactmp(bk))*(1-R0)**((p-1)/2-k)*mp.fsum(comb(2*k,2*m)*R0**m for m in range(k+1))for k,bk in enumerate(b))
    bound=4*M0*S**(p+2)*q**(L+1)*((L+1)-L*q)/(1-q)**2
    return val,bound

def polar_curvature(p,b,t):
    # Own polar differentiation of sin(theta)*cos(2k theta).
    import numpy as np
    t=np.asarray(t,float);r=np.hypot(1.,t);sn=t/r;cs=1/r;th=np.arctan(t);theta=np.zeros_like(t);dtheta=theta.copy();ddtheta=theta.copy()
    for k,bk in enumerate(b):
        co=np.cos(2*k*th);si=np.sin(2*k*th);v=float(bk)
        theta+=v*sn*co;dtheta+=v*(cs*co-2*k*sn*si);ddtheta+=v*(-(1+4*k*k)*sn*co-4*k*cs*si)
    return r**(float(p)-2)*(float(p)*((float(p)-1)*cs*cs+sn*sn)*theta-2*(float(p)-1)*sn*cs*dtheta+sn*sn*ddtheta)

def cutoff_quadrature(p,b,S,order):
    import numpy as np
    x,w=np.polynomial.legendre.leggauss(order);edges=np.unique(np.r_[0.,np.geomspace(.0625,float(S),max(3,int(np.ceil(np.log2(float(S)/.0625)))+1))]);values=[]
    for lo,hi in zip(edges[:-1],edges[1:]):
        t=(hi+lo)/2+(hi-lo)/2*x;values.append((hi-lo)/2*np.dot(w,t*polar_curvature(p,b,t)))
    Q=sum(((-1)**k*(F(p)-1-4*k*k)*F(bk)for k,bk in enumerate(b)),F(0))
    return float(np.sum(values))-float(Q)*float(S)**float(p)/float(p)
