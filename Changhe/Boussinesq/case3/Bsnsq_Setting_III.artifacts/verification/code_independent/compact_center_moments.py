"""Independent per-cell Gauss-Legendre moment quadrature in compact t.

Packet172: a separate quadrature and change of variables from physical-radius
adaptive Gauss-Kronrod. This is floating evidence, not an interval certificate.
"""
import numpy as np
from scipy.special import roots_legendre

def moments(state,order=48,switch=.1):
    u,w=roots_legendre(order)
    half=np.diff(state.edges)/2;mid=(state.edges[:-1]+state.edges[1:])/2
    t=(mid[:,None]+half[:,None]*u).ravel();weight=(half[:,None]*w).ravel()
    z=1-t;logz=np.log1p(-t);S=-np.expm1(2*state.bb*logz)
    logr=np.log(state.L)-state.bb*logz+.5*np.log(S)
    P=state.Gs(t);C=[]
    for n in range(2,state.K+1):
        delta=P[:,n-1].copy()
        if n+1<state.K:delta-=P[:,n+1]
        logfactor=(n-2)*(np.log(switch)-logr)
        if n%2:logfactor-=.5*np.log(S)
        integrand=np.zeros_like(t);nz=delta!=0
        integrand[nz]=np.sign(delta[nz])*np.exp(np.log(abs(delta[nz]))+logfactor[nz])
        C.append(state.bb*state.L/2*np.dot(weight,integrand))
    return np.array(C)
