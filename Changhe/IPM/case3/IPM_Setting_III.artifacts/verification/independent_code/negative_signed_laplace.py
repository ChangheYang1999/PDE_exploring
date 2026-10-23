"""Subtracted real-Euler and Laplace quadrature for result228. No hypergeometric calls."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name]='1'
from functools import lru_cache
import math
import numpy as np
from scipy.special import roots_jacobi,roots_genlaguerre,gamma

@lru_cache(None)
def rules(p,epsilon,order):
    d=1/(p+1);a=(epsilon-p)/2;c=epsilon+.5;g=a+d
    xx,bw=roots_jacobi(order,c-a-1,a);t=(xx+1)/2
    # The transformed beta weight has total B(a+1,c-a).
    beta_mass=2**c*gamma(a+1)*gamma(c-a)/gamma(c+1)
    bw=bw/beta_mass
    s,sw=roots_genlaguerre(order,g-1);sw=sw/gamma(g)
    return a,c,g,t,bw,s,sw

def laplace_jets(p,epsilon,q,order=96):
    if not 0<p<1 or epsilon not in (0,1) or q<0:raise ValueError('Outside the proved range')
    a,c,g,t,bw,s,sw=rules(float(p),int(epsilon),int(order));beta=1-a
    tt=t[None,:];ss=s[:,None];u=q*ss*tt;log=np.log1p(u)
    w=sw[:,None]*bw[None,:]
    # F and its first three ordinary q derivatives.
    ans=[float(1+(a/c)*np.sum(w*np.expm1(beta*log)/tt))]
    fall=1.
    for j in range(1,4):
        fall*=beta-j+1
        ans.append(float((a/c)*fall*np.sum(w*ss**j*tt**(j-1)*np.exp((beta-j)*log))))
    return np.array(ans)

def reduced_ode(p,epsilon,q,jets):
    a=(epsilon-p)/2;d=1/(p+1);g=a+d;c=epsilon+.5
    f,f1,f2,f3=jets
    delta=q*f1;delta2=q*f1+q*q*f2;delta3=q*f1+3*q*q*f2+q**3*f3
    b=a-1;s1=a+b+g;s2=a*b+a*g+b*g;s3=a*b*g
    pieces=[delta2+(c-1)*delta,q*(delta3+s1*delta2+s2*delta+s3*f)]
    return dict(residual=sum(pieces),scale=sum(abs(x)for x in pieces),pieces=pieces)

def h_jets(p,epsilon,z,lam,order=96):
    q=z*z/lam;f,f1,f2,f3=laplace_jets(p,epsilon,q,order)
    # Analytic derivatives, with explicit epsilon=0/1 formulas.
    if epsilon==0:
        return np.array([f,2*z/lam*f1,2/lam*f1+4*z*z/lam**2*f2,12*z/lam**2*f2+8*z**3/lam**3*f3])
    return np.array([z*f,f+2*z*z/lam*f1,6*z/lam*f1+4*z**3/lam**2*f2,6/lam*f1+24*z*z/lam**2*f2+8*z**4/lam**3*f3])

def growing_coefficient(p,epsilon,lam):
    d=1/(p+1);a=(epsilon-p)/2;c=epsilon+.5
    return gamma(c)*gamma(1+d)*lam**(-(p+2-epsilon)/2)/(gamma(a)*gamma(a+d)*gamma(c-a+1))
