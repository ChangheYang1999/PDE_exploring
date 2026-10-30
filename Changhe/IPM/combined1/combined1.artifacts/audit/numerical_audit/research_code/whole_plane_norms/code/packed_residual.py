"""Exact Kronecker encoding of radial-polynomial trigonometric products."""
from pathlib import Path
from flint import fmpq,fmpq_poly
import sys,time
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
from radial import Radial,T,ZERO,put,pshift

def packed_product(C,S,verbose=False):
    start=time.monotonic()
    if not C or not S:return {}
    degree=max(P.degree() for P in C.values())+max(P.degree() for P in S.values())
    stride=degree+1
    nc=max(n for j,n in C);ns=max(n for j,n in S)
    def pack(A,center,kind):
        groups={}
        for (j,n),P in A.items():
            groups.setdefault(j,[]).append((n,P))
        out={}
        for j,rows in groups.items():
            coeffs=[fmpq(0)]*(stride*(2*center+1))
            for n,P in rows:
                for k,v in enumerate(P):
                    coeffs[stride*(center+n)+k]+=v
                    coeffs[stride*(center-n)+k]+=v if kind=='c' else -v
            out[j]=fmpq_poly(coeffs)
        return out
    cp=pack(C,nc,'c');sp=pack(S,ns,'s');products={}
    for i,P in cp.items():
        for j,Q in sp.items():
            h=i+j+1
            products[h]=products.get(h,ZERO)+P*Q
        if verbose:print('packed branch',i,'seconds',time.monotonic()-start,flush=True)
    out={};center=nc+ns
    for h,P in products.items():
        for n in range(1,center+1):
            v=fmpq_poly([P[stride*(center+n)+k]/2 for k in range(stride)])
            if v:out[h,n]=v
    return out

def residual_sine(model,verbose=False):
    sine={}
    for (j,n),P in model.rho.items():
        TP=T*P.derivative()
        L=model.c*(2*TP-3*P+2*T*(model.p[j]*P-TP))-P
        put(sine,(j,n),pshift(L,2))
    for C,S in [(model.u1,model.rx),(model.ry,model.u2)]:
        for key,P in packed_product(C,S,verbose).items():put(sine,key,pshift(P,4))
    return {key:P for key,P in sine.items() if P}

if __name__=='__main__':
    import json,hashlib
    from datetime import datetime,timezone
    path=ROOT/'research/baseline/data/state131_independent.json';model=Radial(path)
    start=time.monotonic();a=model.residual_sine();old=time.monotonic()-start
    start=time.monotonic();b=residual_sine(model,True);new=time.monotonic()-start
    assert a==b
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
         'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
         'exact_agreement':True,'components':len(a),'pairwise_seconds':old,'packed_seconds':new}
    (ROOT/'research/whole_plane_norms/verification/packed_check.json').write_text(json.dumps(out,indent=2)+'\n')
    print(out,flush=True)
