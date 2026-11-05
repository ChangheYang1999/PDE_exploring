"""Equivalent residual convolution with angular parity compression."""
from finite import *

def powers(x,K):
 out=[arb(1)]
 for k in range(K):out.append(out[-1]*x)
 return out

def encode_fast(modes,K,shift,stride,scales):
    out=[arb(0)]*(shift*stride+K+1)
    for (kind,n),p in modes.items():
        assert n<=shift and (shift+n)%2==0
        pos=(shift+n)//2*stride;neg=(shift-n)//2*stride
        for k,a in enumerate(p.coeffs()[:K+1]):
            a=a*scales[k]/2
            out[pos+k]+=a;out[neg+k]+=a if kind=='c' else -a
    return arb_poly(out)

def residual_taylor_fast(e,r,K,scale=None):
    r=arb(r);scale=r/32 if scale is None else arb(scale);fields=e.modes_taylor(r,K)
    odd=max(n for field in [('u1',0,0),('u2',0,0)]for kind,n in fields[field]);assert odd%2==1
    even=max(n for field in [('rho',1,0),('rho',0,1)]for kind,n in fields[field]);assert even%2==0
    stride=2*K+1;scales=powers(scale,K)
    v1=dict(fields['u1',0,0]);v2=dict(fields['u2',0,0]);rr=arb_series([r,1],prec=K+1)
    v1['c',1]=v1.get(('c',1),arb_series([],prec=K+1))+arb(C)*rr
    v2['s',1]=v2.get(('s',1),arb_series([],prec=K+1))+arb(C)*rr
    out=encode_fast(v1,K,odd,stride,scales)*encode_fast(fields['rho',1,0],K,even,stride,scales)
    out+=encode_fast(v2,K,odd,stride,scales)*encode_fast(fields['rho',0,1],K,even,stride,scales)
    rho=fields['rho',0,0];result={}
    for n in range(1,odd+even+1,2):
        index=(odd+even+n)//2*stride
        coeffs=[2*out[index+k]/scales[k]-(rho[('s',n)][k] if ('s',n)in rho else arb(0))for k in range(K+1)]
        if any(coeffs):result[n]=arb_series(coeffs,prec=K+1)
    return result
